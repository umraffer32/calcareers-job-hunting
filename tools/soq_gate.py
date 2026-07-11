#!/usr/bin/env python3
"""
soq_gate.py - content-level pre-submit gate for CalCareers SOQ .docx files.

Extends verify_doc.py (which owns font/size/pages/margins/dashes/acronyms)
with the content checks from SOQ_GATE_PLAN.md, driven by two data files:

  tools/soq_rules.json      persistent rules curated from MEMORIES.md
                            (banned claims, verified numbers, confession
                            patterns, buzzwords, style tics, story anchors)
  <JC folder>/soq_spec.json per-posting spec (exact prompt strings, format
                            numbers, advisory flags, keywords). OPTIONAL -
                            spec-dependent checks are skipped without it, so
                            older folders that predate spec files still pass.

Checks and severities:
  1. banned-claims blocklist ............... FAIL (each hit prints the settled
                                             MEMORIES rationale)
  2. number drift vs verified whitelist .... known number with wrong context =
                                             FAIL (the "70 clients" class);
                                             unknown number = WARN
  3. confession-pattern scan ............... WARN (justify or cut)
  4. verbatim prompt headings (needs spec) . FAIL
  5. formatting advisories (needs spec) .... FAIL (centered/justified text when
     left_align; text boxes / lists / tables when simple_formatting; final PDF
     not flattened or encrypted, via pdfinfo, when flatten_pdf)
     + the zero-colon rule (always runs; numeric colons and colons inside a
     verbatim prompt heading are exempt)
  6. cross-answer double-spend ............. WARN (a number or story anchor
     appearing in 2+ answers; a project may repeat only if the facet differs)
  7. style-tic counters .................... WARN ("X, not Y" contrasts above
     threshold, short-sentence triads, buzzwords, throat-clearing openers)
  8. keyword-coverage report ............... INFO only, NEVER pass/fail and
     never a target; uncovered keywords Uriah can't honestly claim stay
     uncovered (additions route through the honesty banks, not the doc)

It does NOT judge the honesty of novel claims - that stays a human read
against MEMORIES.md. Exit 0 when no hard FAIL, 1 otherwise. Warnings and
notes never fail the gate.

Usage:
    python3 tools/soq_gate.py <SOQ.docx> [--spec <soq_spec.json>]
                              [--rules <soq_rules.json>] [--pdf <final.pdf>]

Defaults: --rules resolves next to this script; --spec and --pdf are
auto-discovered in the docx's folder (soq_spec.json / same-name .pdf).
"""
import sys
import os
import re
import json
import zipfile
import argparse
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))

XML_ENTITIES = {"&amp;": "&", "&lt;": "<", "&gt;": ">", "&quot;": '"', "&apos;": "'"}


def unescape(s):
    for k, v in XML_ENTITIES.items():
        s = s.replace(k, v)
    return s


def norm_quotes(s):
    return (s.replace("’", "'").replace("‘", "'")
             .replace("“", '"').replace("”", '"'))


def norm_ws(s):
    return re.sub(r"\s+", " ", s).strip()


def snippet(t, i, w=32):
    a, b = max(0, i - w), min(len(t), i + w)
    return ("..." if a > 0 else "") + t[a:b].replace("\n", " ") + ("..." if b < len(t) else "")


def read_docx_xml(path):
    with zipfile.ZipFile(path) as z:
        return z.read("word/document.xml").decode("utf-8", "ignore")


def get_paragraphs(doc):
    """Text-bearing paragraphs in order: {text, jc (alignment or None), numpr}."""
    out = []
    for p in re.findall(r"<w:p\b[^>]*>.*?</w:p>", doc, re.S):
        t = unescape("".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, re.S)))
        if not t.strip():
            continue
        jc = re.search(r'<w:jc w:val="(\w+)"', p)
        out.append({"text": t, "jc": jc.group(1) if jc else None,
                    "numpr": "<w:numPr>" in p})
    return out


def sentence_spans(text):
    """(start, end) spans of sentences; splits on ./!/? + space, and newlines."""
    spans, start = [], 0
    for m in re.finditer(r"(?<=[.!?])\s+|\n+", text):
        if m.start() > start:
            spans.append((start, m.start()))
        start = m.end()
    if start < len(text):
        spans.append((start, len(text)))
    return spans


def find_heading_indexes(paras, spec):
    """{paragraph_index: prompt_number} for paragraphs that ARE a verbatim
    prompt heading (with or without the 'N.' prefix). Used by check 4, the
    answer segmentation, and the colon exemption."""
    idxs = {}
    if not spec:
        return idxs
    prompts = [norm_ws(norm_quotes(p)) for p in spec.get("prompts", [])]
    for i, para in enumerate(paras):
        core = re.sub(r"^\d{1,2}[.)]\s*", "", norm_ws(norm_quotes(para["text"])))
        for n, pr in enumerate(prompts, 1):
            if core == pr:
                idxs[i] = n
    return idxs


# ---------------- checks: each returns (level, message) ----------------

def check_banned_claims(full_text, rules):
    hits = []
    for entry in rules.get("banned_claims", []):
        pat = re.compile(entry["pattern"], re.I)
        allow_spans = []
        if entry.get("allow_near"):
            allow_spans = [m.span() for m in
                           re.finditer(entry["allow_near"], full_text, re.I)]
        for m in pat.finditer(full_text):
            excused = any(not (m.end() <= a or m.start() >= b)
                          for a, b in allow_spans)
            if not excused:
                hits.append((entry["id"], snippet(full_text, m.start()), entry["why"]))
    if not hits:
        return ("PASS", "Banned claims: none")
    lines = [f"Banned claims: {len(hits)} hit(s)"]
    for hid, sn, why in hits[:8]:
        lines.append(f'  [{hid}] "{sn}"')
        lines.append(f"      why: {why}")
    return ("FAIL", "\n".join(lines))


def check_numbers(full_text, rules):
    exempt_spans = []
    for pat in rules.get("number_exempt", []):
        exempt_spans += [m.span() for m in re.finditer(pat, full_text)]
    sents = sentence_spans(full_text)

    def sentence_of(pos):
        for a, b in sents:
            if a <= pos < b:
                return full_text[a:b]
        return full_text[max(0, pos - 80):pos + 80]

    whitelist = {e["value"]: e for e in rules.get("verified_numbers", [])}
    drift, unknown = [], []
    for m in re.finditer(r"(?<![A-Za-z0-9_])\$?\d[\d,]*(?:\.\d+)?%?", full_text):
        if any(a <= m.start() and m.end() <= b for a, b in exempt_spans):
            continue
        token = m.group(0)
        value = token.lstrip("$").rstrip("%").replace(",", "").rstrip(".")
        sent = sentence_of(m.start())
        entry = whitelist.get(value)
        if entry is None:
            unknown.append((token, snippet(full_text, m.start())))
        else:
            hay = sent.lower()
            if not any(c.lower() in hay or c in token for c in entry["context"]):
                drift.append((token, entry, snippet(full_text, m.start())))
    if not drift and not unknown:
        return ("PASS", "Numbers: all digits match the verified-quantifiables list")
    lines = []
    for token, entry, sn in drift[:6]:
        lines.append(f'  DRIFT {token} without expected context '
                     f'({", ".join(entry["context"][:4])}...) -> "{sn}"')
        lines.append(f"      verified fact: {entry['note']}")
    for token, sn in unknown[:6]:
        lines.append(f'  UNKNOWN {token} not on the verified list -> "{sn}"')
    if drift:
        return ("FAIL", f"Numbers: {len(drift)} drifted, {len(unknown)} unknown\n" + "\n".join(lines))
    return ("WARN", f"Numbers: {len(unknown)} unknown (verify with Uriah, then add to "
                    f"soq_rules.json)\n" + "\n".join(lines))


def check_confessions(full_text, rules):
    hits = []
    for entry in rules.get("confession_patterns", []):
        for m in re.finditer(entry["pattern"], full_text, re.I):
            hits.append((entry["label"], snippet(full_text, m.start())))
    if not hits:
        return ("PASS", "Confession patterns: none")
    lines = [f'  [{lab}] "{sn}"' for lab, sn in hits[:6]]
    return ("WARN", f"Confession patterns: {len(hits)} hit(s) - justify each or cut "
                    f"(never narrate gaps on a scored SOQ)\n" + "\n".join(lines))


def check_prompt_headings(paras, spec, heading_idxs):
    prompts = spec.get("prompts", [])
    if not prompts:
        return ("NOTE", "Prompt headings: spec has no prompts; skipped")
    numbered = spec.get("numbered_headings", len(prompts) > 1)
    issues = []
    found_pos = {}
    for para_idx, n in heading_idxs.items():
        found_pos[n] = para_idx  # prompt n -> paragraph index
    for n, prompt in enumerate(prompts, 1):
        if n not in found_pos:
            issues.append(f'prompt {n} not found VERBATIM as its own heading paragraph: '
                          f'"{norm_ws(prompt)[:70]}..."')
        elif numbered:
            raw = norm_ws(paras[found_pos[n]]["text"])
            if not re.match(rf"^{n}[.)]\s", raw):
                issues.append(f'prompt {n} heading present but not numbered "{n}." '
                              f'in posting order')
    order = [found_pos[n] for n in sorted(found_pos)]
    if order != sorted(order):
        issues.append("prompt headings are out of posting order")
    if issues:
        return ("FAIL", "Prompt headings:\n" + "\n".join("  " + s for s in issues))
    return ("PASS", f"Prompt headings: all {len(prompts)} verbatim, in order"
                    + (", numbered" if numbered else ""))


def check_advisories(paras, doc, spec):
    adv = spec.get("advisories", {})
    if not adv:
        return ("NOTE", "Advisories: none set in spec; skipped")
    issues = []
    if adv.get("left_align"):
        bad = [(p["jc"], p["text"]) for p in paras
               if p["jc"] in ("center", "right", "both", "distribute")]
        for jc, t in bad[:4]:
            label = "justified" if jc == "both" else jc
            issues.append(f'{label} paragraph (posting says left-align): "{t[:50]}"')
    if adv.get("simple_formatting"):
        if "<w:txbxContent>" in doc:
            issues.append("text box present (txbxContent) - posting asks for simple formatting")
        n_lists = sum(1 for p in paras if p["numpr"])
        if n_lists:
            issues.append(f"{n_lists} bulleted/numbered paragraph(s) (w:numPr) - use flowing prose")
        if "<w:tbl>" in doc:
            issues.append("table present - posting asks for simple formatting")
        if not adv.get("left_align"):
            nj = sum(1 for p in paras if p["jc"] == "both")
            if nj:
                issues.append(f"{nj} justified paragraph(s) - posting says avoid justified text")
    if issues:
        return ("FAIL", "Advisories:\n" + "\n".join("  " + s for s in issues))
    return ("PASS", "Advisories: " + ", ".join(k for k, v in adv.items() if v) + " all clean")


def check_flatten(pdf_path, spec):
    if not spec.get("advisories", {}).get("flatten_pdf"):
        return ("NOTE", "Flatten: not requested by spec; skipped")
    if not pdf_path or not os.path.exists(pdf_path):
        return ("WARN", "Flatten: final PDF not found next to the docx - render it, "
                        "then re-run (or pass --pdf)")
    try:
        out = subprocess.run(["pdfinfo", pdf_path], capture_output=True,
                             text=True, timeout=60).stdout
    except Exception:
        return ("WARN", "Flatten: pdfinfo unavailable; could not verify the PDF")
    form = re.search(r"Form:\s+(\S+)", out)
    enc = re.search(r"Encrypted:\s+(\S+)", out)
    probs = []
    if form and form.group(1).lower() != "none":
        probs.append(f"live form fields present (Form: {form.group(1)}) - print/save to PDF to flatten")
    if enc and not enc.group(1).lower().startswith("no"):
        probs.append("PDF is encrypted - CalCareers upload must be unencrypted")
    if probs:
        return ("FAIL", "Flatten: " + "; ".join(probs))
    return ("PASS", f"Flatten: {os.path.basename(pdf_path)} has no form fields, not encrypted")


def check_colons(paras, heading_idxs):
    """SOQ zero-colon rule (settled 2026-06-21). Numeric colons exempt; colons
    inside a verbatim prompt heading are the agency's own wording and exempt."""
    hits = []
    for i, p in enumerate(paras):
        if i in heading_idxs:
            continue
        t = p["text"]
        for m in re.finditer(r":", t):
            j = m.start()
            if 0 < j < len(t) - 1 and t[j - 1].isdigit() and t[j + 1].isdigit():
                continue
            hits.append(snippet(t, j))
    if hits:
        return ("FAIL", "Colons (SOQ allows none): " + "; ".join(f'"{s}"' for s in hits[:4]))
    return ("PASS", "Colons: none")


def split_answers(paras, heading_idxs):
    """[(answer_no, body_text)] between question headings. Uses spec-matched
    headings when available, else falls back to '1.' / '2)' numbered lines."""
    idxs = dict(heading_idxs)
    if not idxs:
        for i, p in enumerate(paras):
            m = re.match(r"^(\d{1,2})[.)]\s", norm_ws(p["text"]))
            if m:
                idxs[i] = int(m.group(1))
    if len(idxs) < 2:
        return []
    marks = sorted(idxs)
    out = []
    for k, start in enumerate(marks):
        end = marks[k + 1] if k + 1 < len(marks) else len(paras)
        body = "\n".join(paras[j]["text"] for j in range(start + 1, end))
        out.append((idxs[start], body))
    return out


def check_double_spend(paras, heading_idxs, rules):
    answers = split_answers(paras, heading_idxs)
    if len(answers) < 2:
        return ("NOTE", "Double-spend: fewer than 2 question sections detected; skipped")
    num_where, anchor_where = {}, {}
    for n, body in answers:
        spans = []
        for pat in rules.get("number_exempt", []):
            spans += [m.span() for m in re.finditer(pat, body)]
        for m in re.finditer(r"(?<![A-Za-z0-9_])\$?\d[\d,]*(?:\.\d+)?%?", body):
            if any(a <= m.start() and m.end() <= b for a, b in spans):
                continue
            v = m.group(0).lstrip("$").rstrip("%").replace(",", "").rstrip(".")
            num_where.setdefault(v, set()).add(n)
        low = body.lower()
        for anchor in rules.get("story_anchors", []):
            if anchor.lower() in low:
                key = re.sub(r"[^a-z0-9]+", " ", anchor.lower()).strip()
                anchor_where.setdefault(key, (anchor, set()))[1].add(n)
    flags = []
    for v, where in sorted(num_where.items()):
        if len(where) > 1:
            flags.append(f"number {v} appears in answers {sorted(where)}")
    for key in sorted(anchor_where):
        anchor, where = anchor_where[key]
        if len(where) > 1:
            flags.append(f'story anchor "{anchor}" appears in answers {sorted(where)}')
    if not flags:
        return ("PASS", f"Double-spend: no number or story anchor shared across {len(answers)} answers")
    return ("WARN", "Double-spend (repeating a number or named result across answers "
                    "reads as a paste; same project OK only if the facet differs):\n"
                    + "\n".join("  " + f for f in flags))


def check_style_tics(paras, full_text, rules):
    style = rules.get("style", {})
    findings = []
    cpat = style.get("contrast_pattern")
    if cpat:
        hits = [snippet(full_text, m.start()) for m in re.finditer(cpat, full_text, re.I)]
        limit = style.get("contrast_warn_above", 2)
        if len(hits) > limit:
            findings.append(f'{len(hits)} "X, not Y" contrast constructions (warn above {limit}): '
                            + "; ".join(f'"{h}"' for h in hits[:3]))
    tpat = style.get("serial_triad_pattern")
    if tpat:
        hits = [snippet(full_text, m.start()) for m in re.finditer(tpat, full_text)]
        limit = style.get("serial_triad_warn_above", 4)
        if len(hits) > limit:
            findings.append(f'{len(hits)} "X, Y, and Z" serial-triad constructions (warn above {limit}): '
                            + "; ".join(f'"{h}"' for h in hits[:3]))
    maxw = style.get("triad_max_words", 7)
    need = style.get("triad_run", 3)
    for p in paras:
        sents = [s for s in re.split(r"(?<=[.!?])\s+", p["text"]) if s.strip()]
        run = 0
        for s in sents:
            words = len(re.findall(r"[A-Za-z0-9'’-]+", s))
            run = run + 1 if words <= maxw else 0
            if run >= need:
                findings.append(f'{need} consecutive short sentences (punchy-triad tic) '
                                f'near: "{s.strip()[:50]}"')
                run = 0
                break
    allow_spans = []
    for phrase in rules.get("buzzword_allow", []):
        allow_spans += [m.span() for m in re.finditer(re.escape(phrase), full_text, re.I)]
    counts = {}
    for w in rules.get("buzzwords", []):
        for m in re.finditer(r"\b" + re.escape(w) + r"\b", full_text, re.I):
            if any(not (m.end() <= a or m.start() >= b) for a, b in allow_spans):
                continue
            counts[w] = counts.get(w, 0) + 1
    if counts:
        findings.append("buzzwords: " + ", ".join(f"{w} x{c}" for w, c in sorted(counts.items())))
    for pat in style.get("opener_patterns", []):
        for p in paras:
            if re.match(pat, p["text"].strip(), re.I):
                findings.append(f'throat-clearing opener: "{p["text"].strip()[:50]}"')
    if not findings:
        return ("PASS", "Style tics: none")
    return ("WARN", "Style tics (anti-AI checklist items):\n"
                    + "\n".join("  " + f for f in findings))


def check_keyword_coverage(full_text, spec):
    kws = (spec or {}).get("keywords", [])
    if not kws:
        return ("NOTE", "Keyword coverage: no keywords in spec; skipped")
    low = full_text.lower()
    covered = [k for k in kws if k.lower() in low]
    missing = [k for k in kws if k.lower() not in low]
    lines = [f"Keyword coverage: {len(covered)}/{len(kws)} present (INFORMATIONAL ONLY, never a target)"]
    if covered:
        lines.append("  covered: " + ", ".join(covered))
    if missing:
        lines.append("  not covered: " + ", ".join(missing))
        lines.append("  a keyword Uriah can't honestly claim STAYS uncovered; any addition")
        lines.append("  routes through the honesty banks (MEMORIES), never straight into the doc")
    return ("INFO", "\n".join(lines))


def main():
    ap = argparse.ArgumentParser(description="Content-level SOQ gate (see SOQ_GATE_PLAN.md).")
    ap.add_argument("docx")
    ap.add_argument("--spec", help="per-JC soq_spec.json (default: auto-discover next to the docx)")
    ap.add_argument("--rules", default=os.path.join(HERE, "soq_rules.json"))
    ap.add_argument("--pdf", help="final PDF for the flatten check (default: same-name .pdf)")
    a = ap.parse_args()

    if not os.path.exists(a.docx):
        print("ERROR: file not found:", a.docx)
        sys.exit(2)
    if not os.path.exists(a.rules):
        print("ERROR: rules file not found:", a.rules)
        sys.exit(2)
    with open(a.rules, encoding="utf-8") as fh:
        rules = json.load(fh)

    spec_path = a.spec or os.path.join(os.path.dirname(os.path.abspath(a.docx)), "soq_spec.json")
    spec = None
    if os.path.exists(spec_path):
        try:
            with open(spec_path, encoding="utf-8") as fh:
                spec = json.load(fh)
        except Exception as e:
            print(f"ERROR: could not parse spec {spec_path}: {e}")
            sys.exit(2)

    pdf_path = a.pdf or os.path.splitext(os.path.abspath(a.docx))[0] + ".pdf"

    doc = read_docx_xml(a.docx)
    paras = get_paragraphs(doc)
    full_text = "\n".join(p["text"] for p in paras)
    heading_idxs = find_heading_indexes(paras, spec) if spec else {}

    results = [
        check_banned_claims(full_text, rules),
        check_numbers(full_text, rules),
        check_confessions(full_text, rules),
    ]
    if spec:
        results.append(check_prompt_headings(paras, spec, heading_idxs))
        results.append(check_advisories(paras, doc, spec))
        results.append(check_flatten(pdf_path, spec))
    else:
        results.append(("NOTE", "Prompt headings / advisories / flatten: no soq_spec.json "
                                "in the folder; spec-dependent checks skipped"))
    results.append(check_double_spend(paras, heading_idxs, rules))
    results.append(check_style_tics(paras, full_text, rules))
    results.append(check_keyword_coverage(full_text, spec))
    results.append(check_colons(paras, heading_idxs))

    bar = "=" * 64
    print(bar)
    print(" soq_gate.py  -  SOQ content gate")
    print(f" file: {os.path.basename(a.docx)}")
    print(f" rules: {os.path.basename(a.rules)}"
          + (f"; spec: {os.path.basename(spec_path)}" if spec else "; spec: none"))
    print(bar)
    for level, msg in results:
        first, *rest = msg.splitlines()
        print(f" [{level}] {first}")
        for line in rest:
            print("        " + line)
    print("-" * 64)
    fails = sum(1 for l, _ in results if l == "FAIL")
    warns = sum(1 for l, _ in results if l == "WARN")
    print(f" RESULT: {'PASS' if fails == 0 else 'FAIL'}  ({fails} failed, {warns} warning(s))")
    print(bar)
    sys.exit(0 if fails == 0 else 1)


if __name__ == "__main__":
    main()
