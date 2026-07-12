#!/usr/bin/env python3
"""
claims_lib.py - shared banned-claims / scope-watchlist matcher.

The honesty-gate matching (regex + allow_near carve-outs) used to live only in
soq_gate.check_banned_claims and ran only on the SOQ. It now runs on the resume
and every 678 duties block too (check_claims.py), so the matching moved here to
keep ONE source of truth: soq_gate and check_claims must never treat the same
rule differently.

Self-contained on purpose (its own snippet(), no import from soq_gate) so there
is no circular import - soq_gate imports FROM here, not the other way around.
Text extraction mirrors soq_gate's stdlib approach (zipfile + <w:t> regex over
word/document.xml, NOT python-docx) so the SOQ's banned-claims verdict is
byte-identical whichever tool produces it, with no extra dependency. It reads
the document body only, not headers/footers (unchanged from soq_gate).
"""
import re
import zipfile

XML_ENTITIES = {"&amp;": "&", "&lt;": "<", "&gt;": ">", "&quot;": '"', "&apos;": "'"}


def unescape(s):
    for k, v in XML_ENTITIES.items():
        s = s.replace(k, v)
    return s


def snippet(t, i, w=32):
    a, b = max(0, i - w), min(len(t), i + w)
    return ("..." if a > 0 else "") + t[a:b].replace("\n", " ") + ("..." if b < len(t) else "")


def docx_text(path):
    """Full text of a .docx body, one line per non-empty paragraph - the same
    string soq_gate feeds its content checks, so verdicts match exactly."""
    with zipfile.ZipFile(path) as z:
        doc = z.read("word/document.xml").decode("utf-8", "ignore")
    paras = []
    for p in re.findall(r"<w:p\b[^>]*>.*?</w:p>", doc, re.S):
        t = unescape("".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, re.S)))
        if t.strip():
            paras.append(t)
    return "\n".join(paras)


def file_text(path):
    """Text of a package doc - .docx via docx_text, anything else read as UTF-8."""
    if path.lower().endswith(".docx"):
        return docx_text(path)
    return open(path, encoding="utf-8", errors="ignore").read()


def _hits(text, entries):
    """(id, snippet, why, (start, end)) for every unexcused match. An allow_near
    regex excuses a hit only when the hit span overlaps an allow_near span - the
    exact test soq_gate.check_banned_claims has always used."""
    out = []
    for entry in entries:
        pat = re.compile(entry["pattern"], re.I)
        allow_spans = []
        if entry.get("allow_near"):
            allow_spans = [m.span() for m in re.finditer(entry["allow_near"], text, re.I)]
        for m in pat.finditer(text):
            excused = any(not (m.end() <= a or m.start() >= b) for a, b in allow_spans)
            if not excused:
                out.append((entry["id"], snippet(text, m.start()), entry.get("why", ""), m.span()))
    return out


def banned_hits(text, rules):
    """Hard-FAIL claims (rules['banned_claims'])."""
    return _hits(text, rules.get("banned_claims", []))


def watchlist_hits(text, rules):
    """WARN-level scope-creep terms (rules['scope_watchlist'])."""
    return _hits(text, rules.get("scope_watchlist", []))
