#!/usr/bin/env python3
"""
test_gate.py - regression + planted-failure tests for the pre-submit gate.

Re-validates a known-good package and plants the three failures from the
2026-07-12 JC-524404 Cowork session to prove each now fires:
  - a truncated tool (the check_678.py mount clip that passed silently),
  - an over-limit (1,032-char) duties block,
  - a "runbook" in a duties .txt.

Plain Python, zero dependencies. Writes only to a temp dir; never mutates a real
package. Run AFTER `python tools/check_integrity.py --regen`:
    python3 tools/tests/test_gate.py
Exit 0 if every check passes, 1 otherwise.
"""
import sys, os, shutil, tempfile, subprocess, glob

TOOLS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(TOOLS)
PY = sys.executable
GOOD = os.path.join(REPO, "JC-524404 (Security Operations Associate) - SUBMITTED")
KNOWN = os.path.join(REPO, "JC-523777 (System Security Associate) - CLOSED")

RESULTS = []


def check(name, cond, detail=""):
    RESULTS.append(cond)
    mark = "PASS" if cond else "FAIL"
    print(f"  [{mark}] {name}" + (f"   ({detail})" if detail and not cond else ""))


def run(script_dir, script, args):
    p = subprocess.run([PY, os.path.join(script_dir, script)] + args,
                       capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def pkg_docs(folder):
    return (sorted(glob.glob(os.path.join(folder, "Uriah_Raffer_SOQ_*.docx")))
            + sorted(glob.glob(os.path.join(folder, "Uriah_Raffer_Resume_*.docx")))
            + sorted(glob.glob(os.path.join(folder, "*[Dd]uties*.txt"))))


def make_block(n):
    """A valid duties block (one sentence per line, single blank line between,
    no dashes/colons) of exactly n characters."""
    sent = "Perform routine security monitoring and documentation under supervision."
    sep = "\n\n"
    text = ""
    while len(text) + len(sent) + len(sep) <= n:
        text += sent + sep
    rem = n - len(text)
    if rem >= 2:
        text += "A" * (rem - 1) + "."
    elif rem == 1:
        text += "A"
    return text


def main():
    print("gate test harness\n")

    # Preflight: the real manifest must be current, else every pre_submit below
    # short-circuits on integrity and the results would be noise.
    rc, out = run(TOOLS, "check_integrity.py", [])
    if rc != 0:
        print("real tools manifest is stale/mismatched - run "
              "'python tools/check_integrity.py --regen' first:\n")
        print(out)
        return 1

    print("1. known-good regression (JC-524404)")
    rc, out = run(TOOLS, "pre_submit.py", [GOOD])
    check("pre_submit -> OVERALL PASS", rc == 0 and "OVERALL: PASS" in out)
    check("integrity row shown", "[PASS] Tools integrity" in out)
    check("claims scan wired in", "Claims scan" in out)
    check("measured values surfaced beside verdicts",
          "chars" in out and "collisions" in out and "banned" in out)

    print("2. known-good honesty state (JC-523777)")
    rc, out = run(TOOLS, "check_claims.py", pkg_docs(KNOWN))
    check("asset-tracking false positive fixed (GLPI lab bullet)", "asset-tracking" not in out)
    check("only the documented 'simulated' hit remains",
          out.count("[BANNED") == 1 and "simulated-internship" in out,
          f"BANNED count={out.count('[BANNED')}")

    print("3. planted: truncated tool")
    tmp = tempfile.mkdtemp()
    tdir = os.path.join(tmp, "tools")
    shutil.copytree(TOOLS, tdir, ignore=shutil.ignore_patterns("__pycache__", "tests"))
    run(tdir, "check_integrity.py", ["--regen"])          # manifest matches the intact copy
    p678 = os.path.join(tdir, "check_678.py")
    body = open(p678, encoding="utf-8").read().splitlines()
    with open(p678, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(body[:47]) + "\n")             # drop main()/guard, like the mount clip
    irc, iout = run(tdir, "check_integrity.py", [])
    check("check_integrity FAILs on the truncated copy",
          irc == 1 and "check_678.py" in iout and "MISMATCH" in iout)
    pkg = os.path.join(tmp, os.path.basename(GOOD))
    shutil.copytree(GOOD, pkg)
    prc, pout = run(tdir, "pre_submit.py", [pkg])
    check("pre_submit short-circuits -> OVERALL FAIL",
          prc == 1 and "integrity mismatch" in pout)
    check("no downstream checks run after integrity fail", "Claims scan" not in pout)
    shutil.rmtree(tmp, ignore_errors=True)

    print("4. planted: 1,032-char duties block")
    tmp = tempfile.mkdtemp()
    big = os.path.join(tmp, "Uriah_Raffer_STD678-duties_JC-000000.txt")
    blk = make_block(1032)
    with open(big, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(blk)
    check("block built to exactly 1032 chars", len(blk) == 1032, f"len={len(blk)}")
    rc, out = run(TOOLS, "check_678.py", [big])
    check("check_678 FAILs the over-limit block",
          rc == 1 and "exceeds 1000" in out and "1032/1000" in out)
    shutil.rmtree(tmp, ignore_errors=True)

    print("5. planted: 'runbook' in a duties .txt")
    tmp = tempfile.mkdtemp()
    rb = os.path.join(tmp, "Uriah_Raffer_STD678-duties_JC-000000.txt")
    with open(rb, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("Create and maintain runbooks and procedures for the security team.")
    rc, out = run(TOOLS, "check_claims.py", [rb])
    check("check_claims FAILs on a runbook claim in the 678",
          rc == 1 and "runbook" in out and "BANNED" in out)
    shutil.rmtree(tmp, ignore_errors=True)

    print("6. watchlist smoke: 'forensic' WARNs, does not FAIL")
    tmp = tempfile.mkdtemp()
    fx = os.path.join(tmp, "block.txt")
    with open(fx, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("Assist with basic forensic data collection under supervision.")
    rc, out = run(TOOLS, "check_claims.py", [fx])
    check("forensic -> exit 0 with a WATCH, not a FAIL",
          rc == 0 and "WATCH" in out and "forensic" in out)
    shutil.rmtree(tmp, ignore_errors=True)

    print("7. missing-RESULT-line rule (unit)")
    sys.path.insert(0, TOOLS)
    import pre_submit
    check("no RESULT line -> None (a silent checker is a failure)",
          pre_submit.result_line("hello\nworld") is None)
    parsed = pre_submit.result_line("head\nRESULT: PASS | 993/1000 chars")
    check("RESULT line -> (verdict, measure)",
          parsed == ("PASS", "993/1000 chars"))

    print()
    passed = sum(RESULTS)
    total = len(RESULTS)
    print(f"{'OK' if passed == total else 'FAILED'}: {passed}/{total} checks passed")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
