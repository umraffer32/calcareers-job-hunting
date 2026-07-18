#!/usr/bin/env python3
"""
callback_windows.py - paste-ready callback-window table for every SUBMITTED
application, sorted soonest-to-close first.

Why: state panels typically call back 4-6 weeks after filing closes. Hand-
computing that across two dozen applications, re-deriving it after month
rollovers, merging in real interview/rejection events from the progress
logs, and reformatting it all into a markdown table burns reasoning tokens
and invites silent errors, so ALL of it is mechanized here:

  - pull each posting's Final Filing Date, compute close+28 / close+42
  - merge real events from callback_overrides.json (repo root)
  - scan PROGRESS_LOG.md / PROGRESS_LOG_ARCHIVE.md for event-like prose
    with no matching override entry, and WARN on it
  - print the final markdown table + summary as the paste payload, with
    diagnostics below a marker line

The reader's job (see .claude/skills/callback/SKILL.md): run this, paste
everything above the diagnostics marker verbatim, and only open the logs
or PDFs when the RESULT line says WARN. NOTE lines are informational and
need no action.

Usage:
    python tools/callback_windows.py
    python tools/callback_windows.py --json               # machine-readable
    python tools/callback_windows.py --today 2026-07-18   # testing only
    python tools/callback_windows.py --overrides FILE     # testing only
"""
import sys, os, re, glob, json, argparse, subprocess
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

FOLDER_RE = re.compile(r"^JC-(\d+) \((.+)\) - SUBMITTED$")
DATE_RE = re.compile(r"Final Filing Date:\s*(\d{1,2})/(\d{1,2})/(\d{4})", re.IGNORECASE)
SOON_DAYS = 3  # flag a close/open date this many days out or fewer

OVERRIDES_DEFAULT = os.path.join(ROOT, "callback_overrides.json")
LOG_FILES = ("PROGRESS_LOG.md", "PROGRESS_LOG_ARCHIVE.md")
EVENT_STATUSES = ("interview", "offer", "rejected", "withdrawn")
BOLD_STATUSES = ("interview", "offer")
RESOLVED_STATUSES = ("rejected", "withdrawn")
MARKER = "---- diagnostics (do not paste below this line) ----"

# Signal patterns grouped by event class. Phrase-anchored on purpose: bare
# "interview"/"offer"/"declined" false-positive on every Interview_Prep_JC
# mention, "top interview risk", triage "declined the ITS I stretch", "offer
# letter gives 5 days", etc. in the logs.
SIGNAL_RES = [(cls, re.compile(p, re.IGNORECASE)) for cls, p in (
    ("interview", r"interview\s+(scheduled|confirmed|rescheduled|completed|invite|invitation)"),
    ("interview", r"schedul\w*\s+(an?\s+|the\s+)?interview"),
    ("interview", r"called\s+to\s+schedule"),
    ("interview", r"invit(ed|ation)\s+to\s+(an?\s+)?interview"),
    ("interview", r"set\s+up\s+an?\s+interview"),
    ("interview", r"phone\s+screen"),
    ("rejected", r"reject(ed|ion)"),
    ("rejected", r"no\s+longer\s+under\s+consideration"),
    ("rejected", r"not\s+selected"),
    ("withdrawn", r"withdr(ew|awn)"),
    ("offer", r"offer\s+(received|extended|accepted)"),
    ("offer", r"job\s+offer"),
    ("offer", r"conditional\s+offer"),
    ("offer", r"(received|extended|accepted|declined|turned\s+down)\s+(an?\s+|the\s+)?(job\s+|conditional\s+)?offer"),
    ("offer", r"\bhired\b"),
    ("offer", r"start\s+date\s+(confirmed|set)"),
)]
# An event override suppresses only hits of classes the recorded event implies,
# so the NEXT event (an offer after an interview, a rejection after an offer)
# still warns. Terminal statuses cover everything - the application is resolved.
CLASS_COVER = {
    "interview": {"interview"},
    "offer": {"interview", "offer"},
    "rejected": {"interview", "offer", "rejected", "withdrawn"},
    "withdrawn": {"interview", "offer", "rejected", "withdrawn"},
}
JC_RE = re.compile(r"\b(?:JC-)?(\d{6})\b")
HEADING_RE = re.compile(r"^#{2,}\s")


def md(d):
    # M/D, no year, no zero-pad ('%-m' is not portable on Windows)
    return f"{d.month}/{d.day}"


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


def load_overrides(path, warnings):
    """Load and shape-validate the state file. Every malformed shape degrades to
    a WARN (never a traceback) so the RESULT line always prints and gates the
    paste - this file is hand-edited by design."""
    empty = {"overrides": {}, "filing_dates": {}}
    if not os.path.exists(path):
        warnings.append(f"WARN: overrides file not found at {path} - treating as empty; "
                        "restore or recreate it (the JC-520957 interview lives there)")
        return empty
    try:
        # utf-8-sig: PowerShell's -Encoding utf8 writes a BOM; accept it
        with open(path, encoding="utf-8-sig") as f:
            data = json.load(f)
    except Exception as e:
        warnings.append(f"WARN: could not parse {os.path.basename(path)} ({e}) - fix the file and re-run")
        return empty
    if not isinstance(data, dict):
        warnings.append(f"WARN: {os.path.basename(path)} must be a JSON object - treating as empty")
        return empty
    for key in ("overrides", "filing_dates"):
        if not isinstance(data.get(key), dict):
            if data.get(key) is not None:
                warnings.append(f"WARN: '{key}' in {os.path.basename(path)} must be an object - ignoring it")
            data[key] = {}
    for jc, entry in list(data["overrides"].items()):
        if not isinstance(entry, dict):
            warnings.append(f"WARN: override for JC-{jc} is not an object - ignoring it")
            del data["overrides"][jc]
            continue
        status = entry.get("status")
        if status not in EVENT_STATUSES and status != "ack":
            warnings.append(f"WARN: override for JC-{jc} has unknown status {status!r} "
                            f"(expected one of {', '.join(EVENT_STATUSES)}, ack)")
        if status in EVENT_STATUSES and not (isinstance(entry.get("window_cell"), str)
                                             and entry["window_cell"].strip()):
            warnings.append(f"WARN: override for JC-{jc} ({status}) is missing window_cell - "
                            "add the exact table-cell text before pasting")
        for field in ("lines", "ack_lines"):
            v = entry.get(field)
            if v is None:
                continue
            if isinstance(v, str):
                entry[field] = [v]  # a bare string would otherwise iterate per character
            elif isinstance(v, list):
                good = [x for x in v if isinstance(x, str) and x]
                if len(good) != len(v):
                    warnings.append(f"WARN: '{field}' for JC-{jc} must be non-empty strings - "
                                    f"ignoring {len(v) - len(good)} bad element(s)")
                entry[field] = good
            else:
                warnings.append(f"WARN: '{field}' for JC-{jc} must be a list of strings - ignoring it")
                entry[field] = []
    return data


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
        row["note"] = f"filing closes in {days_to_close}d"
    elif days_to_close <= 0 < days_to_open <= SOON_DAYS:
        row["note"] = f"window opens in {days_to_open}d"
    else:
        row["note"] = None
    return row


def scan_logs(submitted_jcs, overrides, warnings):
    """WARN on event-like log prose for a submitted JC with no override cover.

    An event override covers only the classes its status implies (CLASS_COVER),
    so a later different event for the same JC still warns. ack entries (or
    ack_lines on an event entry) suppress specific lines by substring."""
    hits = {}  # jc -> [(file, lineno, excerpt)]
    for name in LOG_FILES:
        path = os.path.join(ROOT, name)
        if not os.path.exists(path):
            continue
        heading = ""
        with open(path, encoding="utf-8", errors="ignore") as f:
            for lineno, line in enumerate(f, 1):
                if HEADING_RE.match(line):
                    heading = line
                classes = {cls for cls, rx in SIGNAL_RES if rx.search(line)}
                if not classes:
                    continue
                jcs = set(JC_RE.findall(line)) | set(JC_RE.findall(heading))
                for jc in sorted(jcs & submitted_jcs):
                    entry = overrides.get(jc)
                    if isinstance(entry, dict):
                        status = entry.get("status")
                        if status in EVENT_STATUSES and classes <= CLASS_COVER[status]:
                            continue  # this event is recorded; a different class still warns
                        ack_subs = (entry.get("ack_lines") if status in EVENT_STATUSES
                                    else entry.get("lines"))
                        if any(s in line for s in ack_subs or []):
                            continue  # this exact line acknowledged as a false positive
                    hits.setdefault(jc, []).append((name, lineno, line.strip()[:90]))
    for jc, jc_hits in sorted(hits.items()):
        warnings.append(f"WARN: JC-{jc} has {len(jc_hits)} event-like log mention(s) with no "
                        "override entry - read them, then add an overrides entry (real event) "
                        "or an ack (false positive) to callback_overrides.json:")
        for name, lineno, excerpt in jc_hits:
            warnings.append(f"  {name}:{lineno}: {excerpt}")
    return hits


def render_markdown(rows, today, warnings):
    lines = ["| JC | Role | Filing closed | Interview window (4-6 wks post-close) |",
             "|---|---|---|---|"]
    heuristic_in_window = confirmed = resolved = 0
    for r in rows:
        ov = r.get("override")
        status = ov.get("status") if ov else None
        if status in BOLD_STATUSES:
            confirmed += 1
        elif status in RESOLVED_STATUSES:
            resolved += 1
        elif r.get("in_window"):
            heuristic_in_window += 1

        close_cell = md(date.fromisoformat(r["close"])) if r["close"] else "?"
        if ov:
            # a missing window_cell already produced a WARN in load_overrides,
            # so this placeholder can never ship under a clean RESULT: INFO
            window_cell = ov.get("window_cell") or f"(override for JC-{r['jc']} has no window_cell)"
        elif r["close"] is None:
            window_cell = "? (see WARN below)"
        else:
            window_cell = (f"{md(date.fromisoformat(r['window_start']))} to "
                           f"{md(date.fromisoformat(r['window_end']))}")
            if r["note"]:
                window_cell += f" ({r['note']})"

        jc_cell, role_cell = r["jc"], r["title"]
        if status in BOLD_STATUSES:
            jc_cell, role_cell, window_cell = (f"**{jc_cell}**", f"**{role_cell}**",
                                               f"**{window_cell}**")
        lines.append(f"| {jc_cell} | {role_cell} | {close_cell} | {window_cell} |")

    confirmed_part = (f"{confirmed} confirmed interview" + ("s" if confirmed != 1 else "")
                      if confirmed else "no confirmed interviews")
    summary = (f"As of {md(today)}, {len(rows)} applications tracked, "
               f"{heuristic_in_window} inside their 4-6 week window, {confirmed_part}")
    if resolved:
        summary += f", {resolved} resolved (rejected or withdrawn)"
    summary += ". Only a confirmed row is a guarantee. The rest are the heuristic estimate."
    lines += ["", summary]

    unresolved = sum(1 for r in rows if r["close"] is None)
    n_override = sum(1 for r in rows if r.get("override"))
    n_warn = sum(1 for w in warnings if w.startswith("WARN:"))
    verdict = "WARN" if n_warn else "INFO"
    lines += ["", MARKER]
    lines += warnings
    lines.append(f"RESULT: {verdict} | {len(rows)} applications, {heuristic_in_window} in window, "
                 f"{unresolved} unresolved, {n_override} override(s), {n_warn} warning(s)")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="machine-readable output instead of the table")
    ap.add_argument("--today", help="override today's date as YYYY-MM-DD (testing only)")
    ap.add_argument("--overrides", default=OVERRIDES_DEFAULT,
                    help="path to callback_overrides.json (testing only)")
    a = ap.parse_args()
    today = date.fromisoformat(a.today) if a.today else date.today()

    warnings = []
    state = load_overrides(a.overrides, warnings)
    overrides, filing_dates = state["overrides"], state["filing_dates"]

    rows = []
    for path in sorted(glob.glob(os.path.join(ROOT, "JC-* - SUBMITTED"))):
        folder = os.path.basename(path)
        m = FOLDER_RE.match(folder)
        if not m:
            continue
        jc, title = m.group(1), m.group(2)
        pdf = find_posting_pdf(path)
        close = extract_filing_date(pdf) if pdf else None
        manual = filing_dates.get(jc)
        if manual:
            try:
                manual = date.fromisoformat(str(manual))
            except ValueError:
                warnings.append(f"WARN: filing_dates entry for JC-{jc} is not YYYY-MM-DD - fix it")
                manual = None
        if close and manual and close != manual:
            # manual wins: it was added deliberately via the documented flow.
            # NOTE (not WARN) so a legitimate correction is not a permanent gate.
            warnings.append(f"NOTE: JC-{jc} manual filing_dates entry ({manual.isoformat()}) differs "
                            f"from the posting PDF ({close.isoformat()}) - using the manual date; "
                            "delete the filing_dates entry if the PDF is actually right")
        close = manual or close
        row = build_row(folder, jc, title, close, today)
        entry = overrides.get(jc)
        if isinstance(entry, dict) and entry.get("status") in EVENT_STATUSES:
            row["override"] = {"status": entry["status"], "window_cell": entry.get("window_cell")}
        if close is None:
            warnings.append(f"WARN: JC-{jc} filing date could not be extracted from the posting PDF - "
                            "read the PDF, then add the date to filing_dates in callback_overrides.json")
        rows.append(row)

    submitted_jcs = {r["jc"] for r in rows}
    for jc in sorted(set(overrides) - submitted_jcs):
        warnings.append(f"WARN: override for JC-{jc} has no SUBMITTED folder - "
                        "folder renamed, or the JC number is a typo")
    scan_logs(submitted_jcs, overrides, warnings)

    rows.sort(key=lambda r: (r["close"] is None, r["close"] or ""))

    if a.json:
        for r in rows:
            r.setdefault("override", None)
        print(json.dumps({"today": today.isoformat(), "rows": rows, "warnings": warnings}, indent=2))
        return 0

    print(render_markdown(rows, today, warnings))
    return 0


if __name__ == "__main__":
    sys.exit(main())
