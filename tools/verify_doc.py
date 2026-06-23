#!/usr/bin/env python3
"""
verify_doc.py - pre-submit mechanical verifier for CalCareers SOQ / resume .docx files.

It reads the RENDERED file (not the build label) and checks the deterministic
pre-submit items from PRE_SUBMIT_CHECKLIST.md sections 2-4:

    - font family on every run of text
    - font size on every run (SOQ must be uniform; resume is exempt by design)
    - page count of the LibreOffice-rendered PDF against the posting's limit
    - page margins
    - em / en dashes (zero tolerance)
    - colons (SOQ only, zero tolerance; numeric times/ratios exempt)
    - acronyms spelled out exactly once on first use (warn-level, advisory)

It does NOT judge honesty or claims (checklist section 1). That stays a human
read against MEMORIES.md. This tool only mechanizes the deterministic checks.

Usage (font is always required; size is required for an SOQ):
    python3 verify_doc.py <file.docx> --type soq    --font Arial   --size 12 [--max-pages 2] [--margins 1.0]
    python3 verify_doc.py <file.docx> --type resume --font Calibri           [--max-pages 1]

Exit code is 0 when no hard check FAILs, 1 otherwise. Warnings never fail the gate.
"""
import sys, re, os, zipfile, argparse, subprocess, tempfile, glob

# Universally known or CalCareers-native abbreviations that do not need spelling out.
ACRONYM_ALLOWLIST = {"IT", "JC", "CA", "US", "AM", "PM", "RPA", "SOQ", "STD"}

XML_ENTITIES = {"&amp;": "&", "&lt;": "<", "&gt;": ">", "&quot;": '"', "&apos;": "'"}


def unescape(s):
    for k, v in XML_ENTITIES.items():
        s = s.replace(k, v)
    return s


def read_docx_xml(path):
    with zipfile.ZipFile(path) as z:
        doc = z.read("word/document.xml").decode("utf-8", "ignore")
        try:
            styles = z.read("word/styles.xml").decode("utf-8", "ignore")
        except KeyError:
            styles = ""
    return doc, styles


def default_font_size(styles):
    """Document default font + size (half-points) from styles.xml docDefaults."""
    font = size = None
    m = re.search(r"<w:docDefaults>.*?</w:docDefaults>", styles, re.S)
    block = m.group(0) if m else styles
    fm = re.search(r"<w:rPrDefault>.*?<w:rFonts[^>]*w:ascii=\"([^\"]+)\"", block, re.S)
    if fm:
        font = fm.group(1)
    sm = re.search(r"<w:rPrDefault>.*?<w:sz w:val=\"(\d+)\"", block, re.S)
    if sm:
        size = int(sm.group(1))
    return font, size


def get_runs(doc):
    """Every run that contains visible text, with its effective font + size markers."""
    out = []
    for r in re.findall(r"<w:r\b[^>]*>.*?</w:r>", doc, re.S):
        text = unescape("".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", r, re.S)))
        if not text.strip():
            continue
        fm = re.search(r"<w:rFonts[^>]*w:ascii=\"([^\"]+)\"", r)
        sm = re.search(r"<w:sz w:val=\"(\d+)\"", r)  # not w:szCs (complex-script size)
        out.append({
            "text": text,
            "font": fm.group(1) if fm else None,
            "size": int(sm.group(1)) if sm else None,
        })
    return out


def get_paragraphs(doc):
    out = []
    for p in re.findall(r"<w:p\b[^>]*>.*?</w:p>", doc, re.S):
        t = unescape("".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, re.S)))
        if t.strip():
            out.append(t)
    return out


def snippet(t, i, w=30):
    a, b = max(0, i - w), min(len(t), i + w)
    return ("..." if a > 0 else "") + t[a:b].replace("\n", " ") + ("..." if b < len(t) else "")


def page_count(path):
    """Render to PDF with LibreOffice (isolated profile) and count pages."""
    tmp = tempfile.mkdtemp()
    prof = "file://" + os.path.join(tmp, "loprofile")
    try:
        subprocess.run(
            ["soffice", "--headless", "-env:UserInstallation=" + prof,
             "--convert-to", "pdf", "--outdir", tmp, path],
            check=True, capture_output=True, timeout=180,
        )
        pdfs = glob.glob(os.path.join(tmp, "*.pdf"))
        if not pdfs:
            return None
        info = subprocess.run(["pdfinfo", pdfs[0]], capture_output=True, text=True)
        m = re.search(r"Pages:\s+(\d+)", info.stdout)
        return int(m.group(1)) if m else None
    except Exception:
        return None


# ---- individual checks: each returns (level, message) ----

def check_font(runs, default_font, required):
    bad = [(r["font"] or default_font, r["text"]) for r in runs
           if (r["font"] or default_font) != required]
    if not bad:
        return ("PASS", f"Font: every run is {required}")
    fonts = sorted({b[0] or "(inherited/unset)" for b in bad})
    eg = bad[0][1].strip()[:40]
    return ("FAIL", f"Font: {len(bad)} run(s) not {required} -> {fonts}; e.g. \"{eg}\"")


def check_size(runs, default_size, required_pt):
    req = required_pt * 2  # half-points
    bad = [((r["size"] or default_size), r["text"]) for r in runs
           if (r["size"] or default_size) != req]
    if not bad:
        return ("PASS", f"Size: every run is {required_pt}pt")
    out = []
    for sz, txt in bad[:3]:
        pt = f"{sz/2:g}pt" if sz else "unset"
        out.append(f"{pt} -> \"{txt.strip()[:45]}\"")
    return ("FAIL", f"Size: {len(bad)} run(s) not {required_pt}pt; " + "; ".join(out))


def check_pages(path, max_pages):
    n = page_count(path)
    if n is None:
        return ("WARN", "Pages: could not render PDF to count")
    if n <= max_pages:
        return ("PASS", f"Pages: {n} of {max_pages} allowed")
    return ("FAIL", f"Pages: {n}, exceeds limit of {max_pages}")


def check_margins(doc, required_in):
    m = re.search(r"<w:pgMar([^/]*)/>", doc)
    if not m:
        return ("WARN", "Margins: not found in section properties")
    vals = {k: int(v) for k, v in re.findall(r"w:(top|right|bottom|left)=\"(-?\d+)\"", m.group(1))}
    req = int(round(required_in * 1440))
    bad = {k: v for k, v in vals.items() if v != req}
    if bad:
        detail = ", ".join(f"{k}={v/1440:.2f}in" for k, v in bad.items())
        return ("FAIL", f"Margins: {detail} (need {required_in}in)")
    return ("PASS", f"Margins: {required_in}in all sides")


def check_dashes(paras):
    hits = []
    for t in paras:
        for ch, name in (("—", "em dash"), ("–", "en dash")):
            i = t.find(ch)
            if i >= 0:
                hits.append((name, snippet(t, i)))
    if hits:
        return ("FAIL", "Em/en dashes: " + "; ".join(f'{n} -> "{s}"' for n, s in hits[:3]))
    return ("PASS", "Em dashes: none")


def check_colons(paras):
    """SOQ policy is ZERO colons (settled 2026-06-21). An SOQ answer flows as one
    paragraph with no formatted lists, so there is no list for a colon to
    introduce. Every colon is a FAIL except a true numeric colon (clock time or
    ratio). This check is SOQ-only; the resume keeps its label-colons by design."""
    hits = []
    for t in paras:
        for m in re.finditer(r":", t):
            i = m.start()
            if i > 0 and i + 1 < len(t) and t[i - 1].isdigit() and t[i + 1].isdigit():
                continue  # time / ratio like 8:00 or 3:1
            hits.append(snippet(t, i))
    if hits:
        return ("FAIL", "Colon (SOQ allows none): " + "; ".join(f'"{s}"' for s in hits[:3]))
    return ("PASS", "Colons: none")


def check_acronyms(paras):
    full = " \n ".join(paras)
    defs = {}
    dup = []
    for m in re.finditer(r"\(([A-Z]{2,6})\)", full):
        a = m.group(1)
        if a in defs:
            dup.append(a)
        else:
            defs[a] = m.start()
    issues = []
    for a in sorted(set(dup)):
        issues.append(f"{a} spelled out more than once")
    seen = set()
    for m in re.finditer(r"\b([A-Z]{2,6})\b", full):
        a, pos = m.group(1), m.start()
        if a in ACRONYM_ALLOWLIST or a in seen:
            continue
        if pos > 0 and full[pos - 1] == "(":  # the declaration itself
            continue
        seen.add(a)
        if a in defs:
            if pos < defs[a]:
                issues.append(f"{a} used before it is spelled out")
        else:
            issues.append(f"{a} never spelled out")
    if issues:
        return ("WARN", "Acronyms: " + "; ".join(issues[:6]))
    return ("PASS", "Acronyms: all spelled once on first use")


def main():
    ap = argparse.ArgumentParser(description="Pre-submit verifier for SOQ / resume .docx files.")
    ap.add_argument("docx")
    ap.add_argument("--type", choices=["soq", "resume"], default="soq")
    ap.add_argument("--font", help="required: font family from the posting (e.g. Arial, Times New Roman, Calibri)")
    ap.add_argument("--size", type=int, help="required for SOQ: the single point size the posting specifies (e.g. 12)")
    ap.add_argument("--max-pages", type=int)
    ap.add_argument("--margins", type=float)
    a = ap.parse_args()

    is_soq = a.type == "soq"

    if a.font is None:
        ap.error("--font is required; read the font from the posting's SOQ/formatting instructions")
    if is_soq and a.size is None:
        ap.error("--size is required for an SOQ; the posting specifies one font size")

    font = a.font
    size = a.size  # None for a resume, whose sizes vary by design
    max_pages = a.max_pages if a.max_pages is not None else (2 if is_soq else 1)
    margins = a.margins if a.margins is not None else (1.0 if is_soq else None)

    if not os.path.exists(a.docx):
        print("ERROR: file not found:", a.docx)
        sys.exit(2)

    doc, styles = read_docx_xml(a.docx)
    dfont, dsize = default_font_size(styles)
    runs = get_runs(doc)
    paras = get_paragraphs(doc)

    results = []
    results.append(check_font(runs, dfont, font))
    if size is not None:
        results.append(check_size(runs, dsize, size))
    results.append(check_pages(a.docx, max_pages))
    if margins is not None:
        results.append(check_margins(doc, margins))
    results.append(check_dashes(paras))
    if is_soq:
        results.append(check_colons(paras))  # SOQ-only: resume keeps label-colons
        results.append(check_acronyms(paras))

    spec = [font]
    if size is not None:
        spec.append(f"{size}pt")
    spec.append(f"<={max_pages} page" + ("s" if max_pages != 1 else ""))
    if margins is not None:
        spec.append(f"{margins}in margins")

    bar = "=" * 64
    print(bar)
    print(f" verify_doc.py  -  {a.type.upper()} check")
    print(f" file: {os.path.basename(a.docx)}")
    print(" spec: " + ", ".join(spec))
    print(bar)
    for level, msg in results:
        print(f" [{level}] {msg}")
    print("-" * 64)
    fails = sum(1 for l, _ in results if l == "FAIL")
    warns = sum(1 for l, _ in results if l == "WARN")
    verdict = "PASS" if fails == 0 else "FAIL"
    print(f" RESULT: {verdict}  ({fails} failed, {warns} warning(s))")
    print(bar)
    sys.exit(0 if fails == 0 else 1)


if __name__ == "__main__":
    main()
