#!/usr/bin/env python3
"""
pre_submit.py - one-command mechanical pre-submit gate for a CalCareers application.

Over a JC application folder it runs, finding files by the Uriah_Raffer_* convention:
  - verify_doc.py   on the SOQ docx    (Arial 12 by default; --soq-pages required)
  - soq_gate.py     on the SOQ docx    (content gate: banned claims, number drift,
                    confessions, prompt headings, advisories - see SOQ_GATE_PLAN.md)
  - verify_doc.py   on the resume docx (Calibri; 1 page)
  - check_678.py    on EVERY 678 duties .txt in the folder (<=1000 chars incl
                    whitespace, no dashes, no mid-sentence colons)
  - check_cross_doc.py across SOQ + resume + all 678 duties (no copy-paste)
  - check_678_pdf.py on the CalCareers-GENERATED form PDF when present
                    (required RPA/position/JC identifiers, cert-date sanity,
                    duties fidelity + clip detection) - saved as
                    Uriah_Raffer_STD678_JC-######.pdf in the folder
  - check_keywords.py coverage matrix across SOQ/resume/678 (INFO only)
  - spell_check.py  advisory spelling pass with tools/spell_allow.txt

If the folder holds a soq_spec.json (written per-posting from its SOQ instructions),
the SOQ font/size/pages/margins come from it automatically; CLI flags still override.

Prints a PASS/FAIL per check and an overall result. Exit 1 if any hard check fails.
This mechanizes the deterministic pre-submit items only; the honesty/claims read
stays a human pass against MEMORIES.md.

Usage:
    python3 tools/pre_submit.py "<JC folder>" --soq-pages 3 \
        [--soq-font Arial] [--soq-size 12] [--resume-font Calibri] [--duties-max-chars 1000]

Save the finalized 678 duties block into the folder as a .txt first
(e.g. Uriah_Raffer_STD678-duties_JC-######.txt) so the gate can read it.
"""
import sys, os, glob, json, argparse, subprocess

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
    ap.add_argument("--soq-pages", type=int, help="SOQ page limit (or page_limit in soq_spec.json)")
    ap.add_argument("--soq-font", help="SOQ font (or font in soq_spec.json; default Arial)")
    ap.add_argument("--soq-size", type=int, help="SOQ point size (or size_pt in soq_spec.json; default 12)")
    ap.add_argument("--resume-font", default="Calibri")
    ap.add_argument("--duties-max-chars", type=int, default=1000)
    a = ap.parse_args()

    soq = find(a.folder, "Uriah_Raffer_SOQ_*.docx")
    resume = find(a.folder, "Uriah_Raffer_Resume_*.docx")
    duties_all = sorted(glob.glob(os.path.join(a.folder, "*[Dd]uties*.txt"))) or \
                 sorted(glob.glob(os.path.join(a.folder, "*STD678*.txt")))
    duties_all = [f for f in duties_all if f.lower().endswith(".txt")]

    # Per-JC spec: the posting's SOQ format, extracted once (see SOQ_GATE_PLAN.md).
    # CLI flags override it; without either, the old defaults/requirements apply.
    spec_path = find(a.folder, "soq_spec.json")
    spec = {}
    if spec_path:
        try:
            with open(spec_path, encoding="utf-8") as fh:
                spec = json.load(fh)
        except Exception as e:
            spec = {}
            print(f"WARNING: soq_spec.json unreadable ({e}); falling back to CLI flags")
    soq_pages = a.soq_pages if a.soq_pages is not None else spec.get("page_limit")
    soq_font = a.soq_font or spec.get("font") or "Arial"
    soq_size = a.soq_size if a.soq_size is not None else (spec.get("size_pt") or 12)
    if soq_pages is None:
        ap.error("--soq-pages is required (or provide page_limit in the folder's soq_spec.json)")

    results = []
    if soq:
        vargs = [soq, "--type", "soq", "--font", soq_font, "--size", str(soq_size),
                 "--max-pages", str(soq_pages)]
        if spec.get("margins_in") is not None:
            vargs += ["--margins", str(spec["margins_in"])]
        results.append(("SOQ format", *run("verify_doc.py", vargs)))
        gargs = [soq]
        if spec_path:
            gargs += ["--spec", spec_path]
        results.append(("SOQ gate", *run("soq_gate.py", gargs)))
    else:
        results.append(("SOQ format", 1, "SOQ docx not found"))

    if resume:
        results.append(("Resume format", *run("verify_doc.py",
            [resume, "--type", "resume", "--font", a.resume_font, "--max-pages", "1"])))
    else:
        results.append(("Resume format", 1, "resume docx not found"))

    if duties_all:
        for d in duties_all:
            results.append((f"678 duties ({os.path.basename(d)})", *run("check_678.py",
                [d, "--max-chars", str(a.duties_max_chars)])))
    else:
        results.append(("678 duties", 1,
            "678 duties .txt not found (save the pasted block as a .txt in the folder)"))

    files = [f for f in [resume, soq] if f] + duties_all
    if len(files) >= 2:
        results.append(("Cross-doc paste", *run("check_cross_doc.py", files)))

    # generated-678 audit (only once the CalCareers PDF has been saved into the folder)
    form = find(a.folder, "Uriah_Raffer_STD678_JC-*.pdf")
    if form:
        results.append(("678 PDF audit", *run("check_678_pdf.py",
            [form, "--folder", a.folder])))
    else:
        results.append(("678 PDF audit", 0,
            "SKIPPED - no Uriah_Raffer_STD678_JC-*.pdf in folder yet; save the "
            "CalCareers-generated form and re-run before submitting"))

    # informational passes (never fail the gate)
    results.append(("Memory pointers (INFO)", 0, run("check_memory_pointers.py", [])[1]))
    results.append(("Keyword coverage (INFO)", 0, run("check_keywords.py", [a.folder])[1]))
    spell_files = [f for f in [soq, resume] if f] + duties_all
    if spell_files:
        results.append(("Spelling (ADVISORY)", 0, run("spell_check.py", spell_files)[1]))

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
