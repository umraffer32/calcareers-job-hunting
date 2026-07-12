#!/usr/bin/env python3
"""
check_678_pdf.py - audit the CalCareers-GENERATED STD 678 PDF before submission.

Built 2026-07-11 after the JC-523777 draft-1 form was missing its required RPA
number (caught only by a human read; same miss as JC-522094). Checks, against
the JC folder's soq_spec.json and saved duties .txt files:

  1. app_line_tokens (spec field): each required identifier string (position
     number, RPA, JC) appears VERBATIM somewhere in the form ......... FAIL if not
  2. Certifications: no future-dated issue date (the Cloud+ 2026 typo class),
     no expiration earlier than its issue date ...................... FAIL
  3. Duties fidelity: every Uriah_Raffer_STD678-duties*.txt in the folder
     appears in the PDF whitespace-normalized and COMPLETE (tail present,
     so the ~1,000-char field clip is caught) ....................... FAIL
  4. Education: a completion date appears in the education section ... WARN
  5. Reason for leaving: every PAST job (TO date not "Present") has a
     non-empty reason line (heuristic) .............................. WARN

Usage: python3 tools/check_678_pdf.py <generated_678.pdf> [--folder <JC folder>]
       (folder defaults to the PDF's own directory; spec read from folder)
Exit 1 on any FAIL; warnings never fail the gate.
"""
import sys, os, re, glob, json, argparse, subprocess, datetime


def pdf_text(path):
    p = subprocess.run(["pdftotext", "-layout", path, "-"], capture_output=True, text=True)
    if p.returncode != 0:
        sys.exit(f"ERROR: pdftotext failed on {path}: {p.stderr.strip()}")
    return p.stdout


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def section(text, start_pat, end_pat):
    m = re.search(start_pat, text)
    if not m:
        return ""
    rest = text[m.end():]
    e = re.search(end_pat, rest)
    return rest[:e.start()] if e else rest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--folder", help="JC folder holding soq_spec.json and duties .txt files")
    a = ap.parse_args()
    folder = a.folder or os.path.dirname(os.path.abspath(a.pdf))

    raw = pdf_text(a.pdf)
    flat = norm(raw)
    findings = []   # (level, message)

    # -- 1. required identifiers from the spec ------------------------------
    spec = {}
    sp = os.path.join(folder, "soq_spec.json")
    if os.path.exists(sp):
        try:
            spec = json.load(open(sp, encoding="utf-8"))
        except Exception as e:
            findings.append(("WARN", f"soq_spec.json unreadable ({e}); identifier check skipped"))
    tokens = spec.get("app_line_tokens") or []
    if tokens:
        for t in tokens:
            if t in flat:
                findings.append(("PASS", f'identifier present: "{t}"'))
            else:
                findings.append(("FAIL", f'REQUIRED identifier MISSING from the form: "{t}" '
                                         "(posting's Additional Application Instructions)"))
    else:
        findings.append(("NOTE", "no app_line_tokens in soq_spec.json; identifier check skipped "
                                 "(add the posting's required position/RPA/JC strings to the spec)"))

    # -- 2. certification dates ---------------------------------------------
    lic = section(raw, r"LICENSE / CERTIFICATION", r"EMPLOYMENT HISTORY")
    today = datetime.date.today()
    pairs = re.findall(r"([A-Za-z+][^\n]*?)\s{2,}(\d{2}/\d{2}/\d{4})\s{2,}(\d{2}/\d{2}/\d{4})", lic)
    if pairs:
        ok = True
        for name, iss, exp in pairs:
            d_iss = datetime.datetime.strptime(iss, "%m/%d/%Y").date()
            d_exp = datetime.datetime.strptime(exp, "%m/%d/%Y").date()
            if d_iss > today:
                findings.append(("FAIL", f"cert '{name.strip()}' has a FUTURE issue date {iss} "
                                         "(the Cloud+ year-typo class)"))
                ok = False
            if d_exp < d_iss:
                findings.append(("FAIL", f"cert '{name.strip()}' expires {exp} before its issue date {iss}"))
                ok = False
        if ok:
            findings.append(("PASS", f"cert dates sane ({len(pairs)} certificate(s))"))
    else:
        findings.append(("WARN", "no certificates parsed from the LICENSES section"))

    # -- 3. duties fidelity + clip detection --------------------------------
    duties_files = sorted(glob.glob(os.path.join(folder, "*STD678-duties*.txt")))
    if not duties_files:
        findings.append(("WARN", "no STD678-duties*.txt files in folder; duties fidelity not checked"))
    for df in duties_files:
        want = norm(open(df, encoding="utf-8").read())
        base = os.path.basename(df)
        if want in flat:
            findings.append(("PASS", f"duties block matches form exactly: {base}"))
        elif want[-60:] in flat and want[:60] in flat:
            findings.append(("FAIL", f"duties block PRESENT but ALTERED mid-block on the form: {base} "
                                     "(form text differs from the saved .txt)"))
        elif want[:60] in flat:
            findings.append(("FAIL", f"duties block CLIPPED or truncated on the form: {base} "
                                     "(start found, tail missing - check the ~1,000-char field clip)"))
        else:
            findings.append(("FAIL", f"duties block NOT FOUND on the form: {base}"))

    # -- 4. education date ---------------------------------------------------
    edu = section(raw, r"\bEDUCATION\b", r"LICENSES")
    if re.search(r"\d{2}/\d{2}/\d{4}", edu):
        findings.append(("PASS", "education completion date present"))
    else:
        findings.append(("WARN", "no completion date parsed in EDUCATION section "
                                 "(a screener may assume an undated degree is incomplete)"))

    # -- 5. reason for leaving on past jobs (heuristic) ----------------------
    jobs = re.findall(r"(\d{2}/\d{2}/\d{4})\s+(Present|\d{2}/\d{2}/\d{4})", raw)
    past_jobs = [j for j in jobs if j[1] != "Present"]
    reasons = 0
    for m in re.finditer(r"REASON FOR LEAVING\s*\n(.*)", raw):
        nxt = m.group(1).strip()
        if nxt and not nxt.startswith("STATE OF CALIFORNIA"):
            reasons += 1
    if past_jobs:
        if reasons >= len(past_jobs):
            findings.append(("PASS", f"reason-for-leaving present on all {len(past_jobs)} past job(s)"))
        else:
            findings.append(("WARN", f"only {reasons} reason-for-leaving line(s) parsed for "
                                     f"{len(past_jobs)} past job(s) - verify none are blank"))

    # -- report ---------------------------------------------------------------
    bar = "=" * 64
    print(bar)
    print(f" check_678_pdf.py  -  generated STD 678 audit\n file: {os.path.basename(a.pdf)}")
    print(bar)
    fails = 0
    for lvl, msg in findings:
        if lvl == "FAIL":
            fails += 1
        print(f" [{lvl}] {msg}")
    print("-" * 64)
    print(f" RESULT: {'PASS' if fails == 0 else 'FAIL'} | {fails} fail, "
          f"{len(duties_files)} duties block(s)")
    print(bar)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
