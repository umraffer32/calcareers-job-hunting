#!/usr/bin/env python3
"""
check_memory_pointers.py - verify MEMORIES.md's Evidence Bank pointers both ways.

Forward: every [[slug]] in MEMORIES.md must resolve to Evidence Bank/<slug>.md
(the literal placeholder [[slug]] in the index's format explanation is exempt).
Reverse: every Evidence Bank/*.md must have a [[slug]] pointer in MEMORIES.md
(migration-changelog is exempt - it is a historical record, not evidence).

Exit 1 on any orphan in either direction, else 0.

Usage:
    python3 tools/check_memory_pointers.py
"""
import sys, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEM = os.path.join(ROOT, "MEMORIES.md")
BANK = os.path.join(ROOT, "Evidence Bank")
EXEMPT_SLUGS = {"slug"}            # documentation placeholder, not a pointer
EXEMPT_FILES = {"migration-changelog"}  # historical record, no pointer required


def main():
    core = open(MEM, encoding="utf-8").read()
    slugs = set(re.findall(r"\[\[([a-z0-9-]+)\]\]", core)) - EXEMPT_SLUGS
    bank = {f[:-3] for f in os.listdir(BANK) if f.endswith(".md")}

    missing_files = sorted(s for s in slugs if s not in bank)
    orphan_files = sorted(bank - slugs - EXEMPT_FILES)

    print(f"memory pointers: {len(slugs)} [[slug]] refs, {len(bank)} bank files")
    fails = []
    if missing_files:
        fails.append(f"pointers with NO bank file: {', '.join(missing_files)}")
    if orphan_files:
        fails.append(f"bank files with NO pointer in MEMORIES.md: {', '.join(orphan_files)}")
    if fails:
        print("FAIL:")
        for f in fails:
            print("  - " + f)
        return 1
    print("OK - all pointers resolve both ways")
    return 0


if __name__ == "__main__":
    sys.exit(main())
