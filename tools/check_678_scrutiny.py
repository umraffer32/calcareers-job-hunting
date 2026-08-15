#!/usr/bin/env python3
"""
check_678_scrutiny.py - pre-sign-off scrutiny report for ONE 678 duties block.

The SOQ gets a fresh-eyes pass every loop iteration; the 678 historically got only
check_678 (format + clip), so blocks were signed off then reworked (JC-524404:
reordered, de-duped, metrics added, a runbook pulled). This bundles the SOQ's rigor
into one report the soq-builder attaches to a duties block BEFORE presenting it for
sign-off (skill Step 7). It is a REPORT, not a gate - it never blocks; the human reads
it and decides.

  1. Format + clip ...... runs check_678.py (measured char count, dashes, colons).
  2. Honesty ............ banned_claims (flag) + scope_watchlist (WARN) via claims_lib,
                          same matcher the pre_submit claims scan uses.
  3. Keyword coverage ... which spec keywords appear in the block. The spec keywords
                          are extracted verbatim from the posting/duty statement, so
                          this is coverage vs the duty statement.
  4. Quantification ..... WARN if the PRIMARY block carries no real metric (reuses
                          number_exempt so JC numbers/years/versions do not count);
                          whether an honest metric EXISTS stays the human's call.

Usage: python3 tools/check_678_scrutiny.py <duties.txt> [--spec soq_spec.json] [--rules soq_rules.json]
Always exits 0 (informational).
"""
import sys, os, json, argparse, subprocess

from claims_lib import banned_hits, watchlist_hits, overlaps, find_numbers

HERE = os.path.dirname(os.path.abspath(__file__))


def is_primary(path):
    """Primary internship block is Uriah_Raffer_STD678-duties_JC-######.txt (no
    -Label). Labeled past-job blocks (-BlockAdvisors, -RobertsRetirement) may
    honestly carry no metric, so the quantification WARN is scoped to the primary."""
    return "STD678-duties-" not in os.path.basename(path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("duties")
    ap.add_argument("--spec", help="soq_spec.json (default: auto-discover next to the .txt)")
    ap.add_argument("--rules", default=os.path.join(HERE, "soq_rules.json"))
    ap.add_argument("--max-chars", type=int, default=1000)
    a = ap.parse_args()

    text = open(a.duties, encoding="utf-8", errors="ignore").read().replace("\r\n", "\n")
    with open(a.rules, encoding="utf-8") as fh:
        rules = json.load(fh)
    spec_path = a.spec or os.path.join(os.path.dirname(os.path.abspath(a.duties)), "soq_spec.json")
    spec = {}
    if os.path.exists(spec_path):
        try:
            spec = json.load(open(spec_path, encoding="utf-8"))
        except Exception:
            spec = {}

    bar = "=" * 64
    print(bar)
    print(f" check_678_scrutiny.py  -  {os.path.basename(a.duties)}")
    print(bar)

    # 1. format + clip (reuse check_678.py so there is one implementation)
    p = subprocess.run([sys.executable, os.path.join(HERE, "check_678.py"),
                        a.duties, "--max-chars", str(a.max_chars)],
                       capture_output=True, text=True)
    print(" [1] FORMAT + CLIP")
    for line in (p.stdout + p.stderr).strip().splitlines():
        print("     " + line)

    # 2. honesty: banned (flag) + watchlist (WARN), suppress-duplicates
    print(" [2] HONESTY")
    banned = banned_hits(text, rules)
    banned_spans = [h[3] for h in banned]
    watch = [h for h in watchlist_hits(text, rules) if not overlaps(h[3], banned_spans)]
    if not banned and not watch:
        print("     clean - no banned claims or watchlist terms")
    for hid, sn, why, _ in banned:
        print(f'     BANNED [{hid}] "{sn}"')
        print(f"         why: {why}")
    for hid, sn, why, _ in watch:
        print(f'     WATCH  [{hid}] "{sn}"  (confirm in context)')

    # 3. keyword coverage vs the duty statement (spec keywords)
    print(" [3] KEYWORD COVERAGE (vs duty statement)")
    kws = spec.get("keywords") or []
    if not kws:
        print("     no keywords in spec; skipped")
    else:
        low = text.lower()
        covered = [k for k in kws if k.lower() in low]
        missing = [k for k in kws if k.lower() not in low]
        print(f"     {len(covered)}/{len(kws)} spec keywords present in this block")
        if missing:
            print("     absent: " + ", ".join(missing))
            print("     (cover only what he honestly did; a keyword he can't claim stays out)")

    # 4. quantification (primary block only)
    print(" [4] QUANTIFICATION")
    nums = [t for t, _span in find_numbers(text, rules.get("number_exempt", []))]
    if nums:
        print(f"     {len(nums)} metric(s) present: {', '.join(nums)}")
    elif is_primary(a.duties):
        print("     WARN: no real metric in the primary block - add one if an honest "
              "number exists (a metric anchors the strongest duty line)")
    else:
        print("     no metric (past-job block; fine if none honestly exists)")

    print("-" * 64)
    print(" RESULT: INFO | scrutiny report (read before 678 sign-off)")
    print(bar)
    return 0


if __name__ == "__main__":
    sys.exit(main())
