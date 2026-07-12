#!/usr/bin/env python3
"""
check_integrity.py - verify the gate's own tools have not been truncated or altered.

Why: on a Cowork file mount tools/check_678.py was served truncated (main() gone),
so it exited 0 printing nothing and pre_submit read [PASS] for every 678 check - a
silent false pass. pre_submit now runs this FIRST and short-circuits on any mismatch,
because a corrupted toolchain makes every downstream verdict untrustworthy.

It validates tools/tools_manifest.json (sha256 + line count of every gate tool).
Hashing normalizes line endings (CRLF -> LF) so a Windows/Linux/mount checkout does
not false-alarm; only real content change (truncation, edit) trips it.

Covered set: tools/*.py plus soq_rules.json (the load-bearing gate data). Regenerate
with --regen after ANY deliberate tool or soq_rules.json edit, in a trusted (non-mount)
session, and stage the manifest in the same change (see CLAUDE.md mechanize-corrections).
--regen reads the WORKING TREE on purpose: the manifest must capture the edits you just
made, then ship with them.

Usage:
    python3 tools/check_integrity.py                # verify working tree vs manifest
    python3 tools/check_integrity.py --regen        # rewrite the manifest from the working tree
    python3 tools/check_integrity.py --tools-dir D --manifest M   # (testing) verify a copy
Exit 1 on any missing/mismatched file or an empty/unparseable manifest, else 0.
"""
import sys, os, glob, json, hashlib, argparse

HERE = os.path.dirname(os.path.abspath(__file__))


def covered_files(tools_dir):
    """Basenames whose integrity is tracked: every tools/*.py plus soq_rules.json.
    Non-recursive glob, so __pycache__/ and tests/ are excluded."""
    names = sorted(os.path.basename(p) for p in glob.glob(os.path.join(tools_dir, "*.py")))
    if os.path.exists(os.path.join(tools_dir, "soq_rules.json")):
        names.append("soq_rules.json")
    return names


def digest(path):
    """(sha256, line_count) over line-ending-normalized content."""
    with open(path, "rb") as f:
        text = f.read().decode("utf-8", "ignore").replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(text.encode("utf-8")).hexdigest(), len(text.splitlines())


def regen(tools_dir, manifest_path):
    files = {}
    for name in covered_files(tools_dir):
        sha, lines = digest(os.path.join(tools_dir, name))
        files[name] = {"sha256": sha, "lines": lines}
    manifest = {
        "_readme": "sha256 + line count of every gate tool, line-ending-normalized. "
                   "check_integrity.py validates this FIRST in pre_submit. Regenerate with "
                   "check_integrity.py --regen after any tool/soq_rules.json edit and commit it "
                   "in the same change.",
        "generated_from": "working-tree",
        "files": files,
    }
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")
    print(f"regenerated {os.path.basename(manifest_path)}: {len(files)} files tracked")
    print(f"RESULT: PASS | {len(files)} files written")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--regen", action="store_true", help="rewrite the manifest from the working tree")
    ap.add_argument("--tools-dir", default=HERE, help="tools dir to hash (default: this script's dir)")
    ap.add_argument("--manifest", help="manifest path (default: tools_manifest.json next to this script)")
    a = ap.parse_args()
    manifest_path = a.manifest or os.path.join(HERE, "tools_manifest.json")

    if a.regen:
        return regen(a.tools_dir, manifest_path)

    if not os.path.exists(manifest_path):
        print(f"tools integrity: manifest not found ({manifest_path})")
        print("RESULT: FAIL | manifest missing")
        return 1
    try:
        with open(manifest_path, encoding="utf-8") as f:
            listed = json.load(f)["files"]
    except Exception as e:
        print(f"tools integrity: manifest unparseable ({e})")
        print("RESULT: FAIL | manifest unparseable")
        return 1
    if not listed:
        print("tools integrity: manifest lists zero files")
        print("RESULT: FAIL | manifest empty")
        return 1

    print("=" * 64)
    print(" check_integrity.py  -  gate tool integrity")
    print("=" * 64)
    fails = ok = 0
    for name, rec in sorted(listed.items()):
        path = os.path.join(a.tools_dir, name)
        if not os.path.exists(path):
            print(f" [FAIL] {name}: MISSING")
            fails += 1
            continue
        sha, lines = digest(path)
        if sha == rec["sha256"]:
            print(f" [ok]   {name}: {lines}/{rec['lines']} lines, sha ok")
            ok += 1
        else:
            tag = "truncated?" if lines < rec["lines"] else "altered?"
            print(f" [FAIL] {name}: {lines}/{rec['lines']} lines, sha MISMATCH ({tag})")
            fails += 1

    extras = sorted(set(covered_files(a.tools_dir)) - set(listed))
    for name in extras:
        print(f" [WARN] {name}: present but not in manifest (run --regen if intentional)")

    print("-" * 64)
    if fails:
        print(" if you just edited a tool or soq_rules.json on purpose, run "
              "check_integrity.py --regen and stage the manifest")
    verdict = "FAIL" if fails else "PASS"
    print(f" RESULT: {verdict} | {ok}/{len(listed)} tools verified"
          + (f", {fails} mismatch" if fails else "")
          + (f", {len(extras)} untracked" if extras else ""))
    print("=" * 64)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
