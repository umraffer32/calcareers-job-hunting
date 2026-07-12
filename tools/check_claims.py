#!/usr/bin/env python3
"""
check_claims.py - banned-claims + scope-watchlist honesty scan across EVERY
application document (SOQ, resume, and every 678 duties .txt).

Until 2026-07-12 the banned-claims blocklist ran only on the SOQ (soq_gate.py).
The "runbooks" claim reached the 678 internship block and the signed-off SOQ
because the 678 got format+clip only. This runs the SAME matcher (claims_lib,
shared with soq_gate) on all of them, plus a WARN-level scope watchlist for
terms that are sometimes legit and need a human eye.

  banned_claims (hard FAIL) - a claim Uriah must never make; exit 1 on any hit.
  scope_watchlist (WARN) ... - scope-creep radar (asset/inventory/forensic +
                               the banned tool names as a safety net). A
                               watchlist hit whose span overlaps a banned hit
                               in the same doc is suppressed (no double-report).

The gate stays MECHANICAL. This narrows what a human must eyeball; it does not
judge the honesty of a novel claim - that stays a read against MEMORIES.md.

Usage:
    python3 tools/check_claims.py <file.docx|file.txt> [...] [--rules soq_rules.json]
Exit 1 if any banned hit, else 0 (watchlist-only is a pass).
"""
import sys
import os
import json
import argparse

from claims_lib import file_text, banned_hits, watchlist_hits

HERE = os.path.dirname(os.path.abspath(__file__))


def overlaps(span, spans):
    a, b = span
    return any(not (b <= c or a >= d) for c, d in spans)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--rules", default=os.path.join(HERE, "soq_rules.json"))
    a = ap.parse_args()

    if not os.path.exists(a.rules):
        print("ERROR: rules file not found:", a.rules)
        return 2
    with open(a.rules, encoding="utf-8") as fh:
        rules = json.load(fh)

    bar = "=" * 64
    print(bar)
    print(" check_claims.py  -  banned claims + scope watchlist (all docs)")
    print(bar)

    total_banned = total_watch = 0
    for f in a.files:
        if not os.path.exists(f):
            print(f" [MISS] {os.path.basename(f)}: file not found")
            continue
        text = file_text(f)
        banned = banned_hits(text, rules)
        banned_spans = [h[3] for h in banned]
        # suppress-duplicates: a watchlist hit already reported as a banned hit
        # in this doc is not also WARNed.
        watch = [h for h in watchlist_hits(text, rules) if not overlaps(h[3], banned_spans)]
        total_banned += len(banned)
        total_watch += len(watch)

        name = os.path.basename(f)
        if not banned and not watch:
            print(f" [PASS] {name}: clean")
            continue
        print(f" {name}: {len(banned)} banned, {len(watch)} watch")
        for hid, sn, why, _span in banned:
            print(f'   [BANNED {hid}] "{sn}"')
            print(f"       why: {why}")
        for hid, sn, why, _span in watch:
            print(f'   [WATCH {hid}] "{sn}"')

    print("-" * 64)
    verdict = "FAIL" if total_banned else "PASS"
    print(f" RESULT: {verdict} | {total_banned} banned, {total_watch} watch")
    print(bar)
    return 1 if total_banned else 0


if __name__ == "__main__":
    sys.exit(main())
