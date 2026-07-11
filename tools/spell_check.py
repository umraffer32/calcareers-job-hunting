#!/usr/bin/env python3
"""
spell_check.py - ADVISORY spelling pass over application documents.

Checks .docx and .txt files with pyspellchecker's English frequency dictionary
plus tools/spell_allow.txt (products, names, real-but-rare technical words).
Skips tokens containing digits, ALL-CAPS tokens (acronyms), and single letters.

WARN-level by design: unknown words are listed for a human eye; the tool never
fails the gate (exit 0), because dictionary noise trained past gates to be
ignored. Add false positives to spell_allow.txt; never allowlist a real typo.
If pyspellchecker isn't installed it says so and exits 0 (install with
`pip install pyspellchecker`).

Usage: python3 tools/spell_check.py <file.docx|file.txt> [...]
"""
import sys, os, re, argparse

HERE = os.path.dirname(os.path.abspath(__file__))


def file_text(path):
    if path.lower().endswith(".docx"):
        import docx
        return " ".join(p.text for p in docx.Document(path).paragraphs)
    return open(path, encoding="utf-8").read()


def tokens(text):
    for w in re.findall(r"[A-Za-z][A-Za-z'’-]*[A-Za-z]|[A-Za-z]", text):
        w = w.replace("’", "'")
        if len(w) < 2 or w.isupper():
            continue
        yield w


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    a = ap.parse_args()

    try:
        from spellchecker import SpellChecker
    except ImportError:
        print("spell_check: pyspellchecker not installed; skipped "
              "(pip install pyspellchecker)")
        return 0

    allow = set()
    ap_path = os.path.join(HERE, "spell_allow.txt")
    if os.path.exists(ap_path):
        for line in open(ap_path, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#"):
                allow.add(line.lower())

    sc = SpellChecker()
    bar = "=" * 64
    print(bar)
    print(" spell_check.py  -  advisory spelling pass")
    print(bar)
    total_unknown = 0
    for f in a.files:
        words = {}
        for w in tokens(file_text(f)):
            lw = w.lower()
            if lw in allow:
                continue
            # hyphenated: pass if every part is known/allowed
            parts = [p for p in lw.split("-") if p]
            if len(parts) > 1 and all(p in allow or not sc.unknown([p]) for p in parts):
                continue
            if sc.unknown([lw]):
                words.setdefault(w, 0)
                words[w] += 1
        name = os.path.basename(f)
        if words:
            total_unknown += len(words)
            listing = ", ".join(f"{w} x{c}" if c > 1 else w
                                for w, c in sorted(words.items(), key=str))
            print(f" [WARN] {name}: {len(words)} unknown word(s): {listing}")
        else:
            print(f" [PASS] {name}: no unknown words")
    print("-" * 64)
    print(f" RESULT: ADVISORY  ({total_unknown} unknown word(s) across "
          f"{len(a.files)} file(s) - human judges; allowlist false positives)")
    print(bar)
    return 0


if __name__ == "__main__":
    sys.exit(main())
