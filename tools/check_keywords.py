#!/usr/bin/env python3
"""
check_keywords.py - INFORMATIONAL keyword-coverage matrix across the package.

Reads the JC folder's soq_spec.json keywords (extracted verbatim from the
posting/duty statement at spec time) and reports which appear in the SOQ,
the resume, and the combined 678 duties .txt files. Case-insensitive
substring match, so spec stems like "communicat" hit "communicated".

INFO ONLY - never a target, never a failure. A keyword Uriah can't honestly
claim STAYS uncovered; additions route through MEMORIES, never straight in.
(Built 2026-07-11; before this, coverage was reported for the SOQ only.)

Usage: python3 tools/check_keywords.py "<JC folder>"
Always exits 0.
"""
import sys, os, glob, json, argparse


def docx_text(path):
    import docx
    return " ".join(p.text for p in docx.Document(path).paragraphs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    a = ap.parse_args()

    sp = os.path.join(a.folder, "soq_spec.json")
    if not os.path.exists(sp):
        print("check_keywords: no soq_spec.json in folder; nothing to report")
        return 0
    spec = json.load(open(sp, encoding="utf-8"))
    kws = spec.get("keywords") or []
    if not kws:
        print("check_keywords: spec has no keywords; nothing to report")
        return 0

    docs = {}
    soq = sorted(glob.glob(os.path.join(a.folder, "Uriah_Raffer_SOQ_*.docx")))
    res = sorted(glob.glob(os.path.join(a.folder, "Uriah_Raffer_Resume_*.docx")))
    dut = sorted(glob.glob(os.path.join(a.folder, "*STD678-duties*.txt")))
    if soq:
        docs["SOQ"] = docx_text(soq[0]).lower()
    if res:
        docs["Resume"] = docx_text(res[0]).lower()
    if dut:
        docs["678"] = " ".join(open(f, encoding="utf-8").read() for f in dut).lower()
    if not docs:
        print("check_keywords: no package documents found")
        return 0

    names = list(docs)
    width = max(len(k) for k in kws) + 2
    print("=" * 64)
    print(" check_keywords.py  -  coverage matrix (INFORMATIONAL ONLY)")
    print("=" * 64)
    print(" " + "keyword".ljust(width) + "  ".join(n.center(6) for n in names))
    totals = {n: 0 for n in names}
    misses = []
    for k in kws:
        row = []
        hit_any = False
        for n in names:
            hit = k.lower() in docs[n]
            totals[n] += hit
            hit_any = hit_any or hit
            row.append(("X" if hit else "-").center(6))
        print(" " + k.ljust(width) + "  ".join(row))
        if not hit_any:
            misses.append(k)
    print("-" * 64)
    print(" " + "TOTAL".ljust(width)
          + "  ".join(f"{totals[n]}/{len(kws)}".center(6) for n in names))
    if misses:
        print(" nowhere in the package: " + ", ".join(misses))
        print(" (leave uncovered unless honestly claimable via MEMORIES)")
    print(f" RESULT: INFO | {len(kws) - len(misses)}/{len(kws)} covered")
    print("=" * 64)
    return 0


if __name__ == "__main__":
    sys.exit(main())
