#!/usr/bin/env python3
"""
check_cross_doc.py - flag near-duplicate sentences ACROSS application documents.

Catches copy-paste between the resume, SOQ, and the 678 duties block, so the same
internship/project description does not appear nearly word-for-word in two of them.
CLAUDE.md rule 7 already requires a cross-document redundancy pass; this makes it
mechanical instead of a claim. Run it after all three documents exist, before
calling any of them done.

Usage:
    python3 tools/check_cross_doc.py resume.docx soq.docx duties678.txt [...]

Accepts .docx and .txt (paste the 678 duties block into a .txt). Flags any sentence
pair from DIFFERENT files whose word-overlap (Jaccard) >= --jaccard (default 0.55)
OR that share a run of >= --ngram consecutive words (default 10).
Exit code 1 if anything is flagged, else 0.

When a flag is between the 678 and the resume, reword the 678 (it has the
~1,000-char field room); keep the resume tight for the skim.
"""
import sys, re, argparse, itertools


def read_text(path):
    """Return clean text. .docx via python-docx (one line per paragraph)."""
    if path.lower().endswith(".docx"):
        from docx import Document
        return "\n".join(p.text for p in Document(path).paragraphs if p.text.strip())
    return open(path, encoding="utf-8", errors="ignore").read()


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [s.strip() for s in parts if len(s.split()) >= 5]


def words(s):
    return re.findall(r"[a-z0-9]+", s.lower())


def jaccard(a, b):
    sa, sb = set(a), set(b)
    return len(sa & sb) / len(sa | sb) if sa and sb else 0.0


def longest_shared_run(a, b):
    """Longest run of consecutive shared words (order-sensitive LCS-substring)."""
    if not a or not b:
        return 0
    best = 0
    prev = [0] * (len(b) + 1)
    for i in range(1, len(a) + 1):
        cur = [0] * (len(b) + 1)
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cur[j] = prev[j - 1] + 1
                best = max(best, cur[j])
        prev = cur
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--jaccard", type=float, default=0.55)
    ap.add_argument("--ngram", type=int, default=10)
    args = ap.parse_args()

    docs = {f: sentences(read_text(f)) for f in args.files}
    flags = []
    for (f1, s1), (f2, s2) in itertools.combinations(docs.items(), 2):
        for x in s1:
            wx = words(x)
            for y in s2:
                wy = words(y)
                j = jaccard(wx, wy)
                g = longest_shared_run(wx, wy)
                if j >= args.jaccard or g >= args.ngram:
                    flags.append((j, g, f1, x, f2, y))

    if not flags:
        print("OK - no cross-document near-duplicates found")
        return 0
    print(f"FOUND {len(flags)} near-duplicate sentence pair(s):\n")
    for j, g, f1, x, f2, y in sorted(flags, key=lambda t: -max(t[0], t[1] / 10.0)):
        print(f"[jaccard={j:.2f} shared_run={g} words]")
        print(f"  {f1}:\n    {x}")
        print(f"  {f2}:\n    {y}\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())
