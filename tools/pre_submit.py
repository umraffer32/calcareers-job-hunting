#!/usr/bin/env python3
"""
pre_submit.py - one-command mechanical pre-submit gate for a CalCareers application.

Over a JC application folder it runs, finding files by the Uriah_Raffer_* convention:
  - verify_doc.py   on the SOQ docx    (Arial 12 by default; --soq-pages required)
  - verify_doc.py   on the resume docx (Calibri; 1 page)
  - check_678.py    on the 678 duties .txt (<=1000 chars, no dashes, no mid-sentence colons)
  - check_cross_doc.py across SOQ + resume + 678 duties (no copy-paste between them)

Prints a PASS/FAIL per check and an overall result. Exit 1 if any hard check fails.
This mechanizes the deterministic pre-submit items only; the honesty/claims read
stays a human pass against MEMORIES.md.

Usage:
    python3 tools/pre_submit.py "<JC folder>" --soq-pages 3 \
        [--soq-font Arial] [--soq-size 12] [--resume-font Calibri] [--duties-max-chars 1000]

Save the finalized 678 duties block into the folder as a .txt first
(e.g. Uriah_Raffer_STD678-duties_JC-######.txt) so the gate can read it.
"""
import sys, os, glob, argparse, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))


def run(script, args):
    p = subprocess.run([sys.executable, os.path.join(HERE, script)] + args,
                       capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip()


def find(folder, *patterns):
    for pat in patterns:
        g = sorted(glob.glob(os.path.join(folder, pat)))
        if g:
            return g[0]
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--soq-pages", type=int, required=True)
    ap.add_argument("--soq-font", default="Arial")
    ap.add_argument("--soq-size", type=int, default=12)
    ap.add_argument("--resume-font", default="Calibri")
    ap.add_argument("--duties-max-chars", type=int, default=1000)
    a = ap.parse_args()

    soq = find(a.folder, "Uriah_Raffer_SOQ_*.docx")
    resume = find(a.folder, "Uriah_Raffer_Resume_*.docx")
    duties = find(a.folder, "*[Dd]uties*.txt", "*STD678*.txt")

    results = []
    if soq:
        results.append(("SOQ format", *run("verify_doc.py",
            [soq, "--type", "soq", "--font", a.soq_font, "--size", str(a.soq_size),
             "--max-pages", str(a.soq_pages)])))
    else:
        results.append(("SOQ format", 1, "SOQ docx not found"))

    if resume:
        results.append(("Resume format", *run("verify_doc.py",
            [resume, "--type", "resume", "--font", a.resume_font, "--max-pages", "1"])))
    else:
        results.append(("Resume format", 1, "resume docx not found"))

    if duties:
        results.append(("678 duties", *run("check_678.py",
            [duties, "--max-chars", str(a.duties_max_chars)])))
    else:
        results.append(("678 duties", 1,
            "678 duties .txt not found (save the pasted block as a .txt in the folder)"))

    files = [f for f in (resume, soq, duties) if f]
    if len(files) >= 2:
        results.append(("Cross-doc paste", *run("check_cross_doc.py", files)))

    print("=" * 64)
    hard_fail = 0
    for name, rc, out in results:
        if rc != 0:
            hard_fail += 1
        print(f"[{'PASS' if rc == 0 else 'FAIL'}] {name}")
        for line in out.splitlines():
            print("    " + line)
    print("=" * 64)
    print("OVERALL: " + ("PASS - mechanically clean"
                         if hard_fail == 0 else f"FAIL - {hard_fail} check(s) need attention"))
    return 1 if hard_fail else 0


if __name__ == "__main__":
    sys.exit(main())
