#!/usr/bin/env python3
"""
check_678.py - mechanical check for a 678 Duties Performed block saved as .txt.

The 678 lives in CalCareers, not a document, so the workflow is: paste the duties
block into a .txt, then check it. Verifies:
  - character count <= limit (default 1000; the box clips ~1000, whitespace counts)
  - no en/em dashes (zero tolerance)
  - colons: the 678 allows a colon only to introduce a list, never mid-sentence.
    Telling those apart mechanically is unreliable, so this flags EVERY non-numeric
    colon (times/ratios like 7:00 or 3:1 are exempt) for a human to confirm it is a
    list colon and not a mid-sentence one.

Exit 1 if any check FAILs, else 0.

Usage:
    python3 tools/check_678.py duties.txt [--max-chars 1000]
"""
import sys, re, argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--max-chars", type=int, default=1000)
    a = ap.parse_args()

    # Normalize CRLF so a Windows-saved file's \r bytes don't inflate the count
    # vs. the text CalCareers actually counts when pasted.
    text = open(a.file, encoding="utf-8", errors="ignore").read().replace("\r\n", "\n")
    n = len(text)
    fails = []

    if n > a.max_chars:
        fails.append(f"char count {n} exceeds {a.max_chars} (box clips ~1000, whitespace/blank lines count)")
    if re.search(r"[–—]", text):
        fails.append("contains an en/em dash (zero tolerance on the 678)")
    bad = [m.start() for m in re.finditer(":", text)
           if not (0 < m.start() < len(text) - 1
                   and text[m.start() - 1].isdigit() and text[m.start() + 1].isdigit())]
    if bad:
        fails.append(f"{len(bad)} non-numeric colon(s) to review (the 678 allows a colon only to introduce a list, never mid-sentence)")

    print(f"678 duties: {n} chars (limit {a.max_chars})")
    if fails:
        print("FAIL:")
        for f in fails:
            print("  - " + f)
        return 1
    print("OK - 678 duties block passes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
