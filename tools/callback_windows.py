#!/usr/bin/env python3
"""
callback_windows.py - filing-closed dates and heuristic interview windows for
every SUBMITTED application, sorted soonest-to-close first.

Why: state panels typically call back 4-6 weeks after filing closes. Hand-
computing that across two dozen applications, and re-deriving it correctly
after every month rollover, is exactly the kind of thing that produces a
silent arithmetic error, so this mechanizes the one part that IS mechanical:
pull each posting's Final Filing Date, compute close+28 / close+42, and
report status against today.

What this does NOT do: know about a REAL confirmed interview, callback, or
rejection. That lives in prose in PROGRESS_LOG.md / PROGRESS_LOG_ARCHIVE.md,
not a structured field, so cross-checking each JC against those logs and
overriding the heuristic window with anything real is left to whoever reads
this output (see .claude/skills/callback/SKILL.md).

Usage:
    python3 tools/callback_windows.py
    python3 tools/callback_windows.py --json              # machine-readable
    python3 tools/callback_windows.py --today 2026-07-18  # testing only
"""
import sys, os, re, glob, json, argparse, subprocess
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

FOLDER_RE = re.compile(r"^JC-(\d+) \((.+)\) - SUBMITTED$")
DATE_RE = re.compile(r"Final Filing Date:\s*(\d{1,2})/(\d{1,2})/(\d{4})", re.IGNORECASE)
SOON_DAYS = 3  # flag a close/open date this many days out or fewer


def find_posting_pdf(folder):
    matches = sorted(
        p for p in glob.glob(os.path.join(folder, "*[Pp]osting*.pdf"))
        if "duty" not in os.path.basename(p).lower()
    )
    return matches[0] if matches else None


def extract_filing_date(pdf_path):
    try:
        out = subprocess.run(["pdftotext", "-layout", pdf_path, "-"],
                              capture_output=True, text=True, timeout=30)
    except Exception:
        return None
    m = DATE_RE.search(out.stdout or "")
    if not m:
        return None
    month, day, year = int(m.group(1)), int(m.group(2)), int(m.group(3))
    try:
        return date(year, month, day)
    except ValueError:
        return None


def build_row(folder_name, jc, title, close, today):
    row = {"jc": jc, "title": title, "folder": folder_name}
    if close is None:
        row.update(close=None, window_start=None, window_end=None,
                    note="COULD NOT EXTRACT filing date from posting PDF")
        return row
    start, end = close + timedelta(days=28), close + timedelta(days=42)
    row.update(close=close.isoformat(), window_start=start.isoformat(),
               window_end=end.isoformat(), closed=close <= today,
               in_window=start <= today <= end)
    days_to_close = (close - today).days
    days_to_open = (start - today).days
    if 0 < days_to_close <= SOON_DAYS:
        row["note"] = f"closes in {days_to_close}d"
    elif days_to_close <= 0 < days_to_open <= SOON_DAYS:
        row["note"] = f"window opens in {days_to_open}d"
    else:
        row["note"] = None
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="machine-readable output instead of a table")
    ap.add_argument("--today", help="override today's date as YYYY-MM-DD (testing only)")
    a = ap.parse_args()
    today = date.fromisoformat(a.today) if a.today else date.today()

    rows = []
    for path in sorted(glob.glob(os.path.join(ROOT, "JC-* - SUBMITTED"))):
        folder = os.path.basename(path)
        m = FOLDER_RE.match(folder)
        if not m:
            continue
        jc, title = m.group(1), m.group(2)
        pdf = find_posting_pdf(path)
        close = extract_filing_date(pdf) if pdf else None
        rows.append(build_row(folder, jc, title, close, today))

    rows.sort(key=lambda r: (r["close"] is None, r["close"]))

    if a.json:
        print(json.dumps({"today": today.isoformat(), "rows": rows}, indent=2))
        return 0

    print(f"{len(rows)} SUBMITTED applications, today = {today.isoformat()}")
    print("-" * 104)
    print(f"{'JC':<8} {'Title':<40} {'Filing closed':<14} {'Window (4-6 wks)':<24} note")
    print("-" * 104)
    in_window = unresolved = 0
    for r in rows:
        if r["close"] is None:
            print(f"{r['jc']:<8} {r['title']:<40} {'?':<14} {'?':<24} {r['note']}")
            unresolved += 1
            continue
        if r["in_window"]:
            in_window += 1
        window_str = f"{r['window_start']} to {r['window_end']}"
        print(f"{r['jc']:<8} {r['title']:<40} {r['close']:<14} {window_str:<24} {r['note'] or ''}")

    print("-" * 104)
    print(f"RESULT: INFO | {len(rows)} applications, {in_window} currently inside their heuristic window"
          + (f", {unresolved} unresolved" if unresolved else ""))
    print()
    print("Note: this is the heuristic 4-6 week window only. Cross-check each JC against")
    print("PROGRESS_LOG.md and PROGRESS_LOG_ARCHIVE.md for a REAL confirmed interview,")
    print("callback, or rejection before presenting - a real date always overrides this.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
