# Gate Hardening — Design Record

_Drafted 2026-07-12, out of the JC-524404 Cowork session. Status: **BUILT and validated 2026-07-12** (7 new/changed tools, `tools/tests/test_gate.py` 15/15, known-good JC-524404 OVERALL PASS). Sibling to the frozen `SOQ_GATE_PLAN.md`, which it extends rather than edits._

## Why this exists

Building JC-524404 in Cowork surfaced four gaps in the pre-submit gate.

1. **A truncated tool passed silently.** The Cowork file mount served a truncated `tools/check_678.py` (clipped at line 47, past the `main()` guard), so it exited 0 printing nothing. `pre_submit` reads a checker's exit code as its only signal, so it logged `[PASS]` for every 678 duties check. An over-limit block would pass undetected. The committed file was intact; the mount was the fault, but the gate should have caught it. The same mount had previously clipped `pre_submit.py` (90 bytes short) and gate data files, so this is a recurring class, not a one-off.
2. **The 678 blocks had no honesty gate.** They ran only `check_678.py` (format + clip). A "runbooks" claim (never built one) reached the internship 678 block and the signed-off SOQ. Banned-claims ran only against the SOQ.
3. **678 scrutiny came after sign-off.** All three JC-524404 blocks were signed off, then reworked (competency-first reorder, de-dup, added metrics, a KQL keyword, pulled runbook). The SOQ gets a fresh-eyes pass every loop iteration; the 678 got none.
4. **Trimming to the ~1,000-char clip was manual.** Blank lines count toward the limit, so hand-trimming the internship block ate many rebuilds.

The gate stays MECHANICAL by design. Honesty and claim accuracy remain a human read; this hardening narrows what the human must catch by hand, and makes a PASS prove itself.

## What was built

### 1. Layered truncation defense

Two independent guards, because either alone has a hole.

- **`tools/tools_manifest.json` + `check_integrity.py`.** The manifest holds a sha256 and line count for every `tools/*.py` and `soq_rules.json`. `pre_submit` runs `check_integrity` FIRST; any mismatch, missing file, or empty/unparseable manifest is a hard FAIL that **short-circuits** the whole gate (a corrupted toolchain makes every downstream verdict untrustworthy). Hashing normalizes line endings (CRLF to LF) so a Windows/Linux/mount checkout does not false-alarm; only real content change trips it.
- **Self-evidencing checks.** Every checker prints a final `RESULT: <verdict> | <measure>` line. `pre_submit` surfaces the measure beside each verdict (`678 duties: 993/1000 chars`, `SOQ format: 2/2 pages`, `Cross-doc: 0 collisions`), so a PASS shows the number it passed on. A hard check that exits 0 but prints no `RESULT` line is treated as a FAIL — the backstop that catches any silent no-op, including a truncated checker `check_integrity` somehow missed.

Why both: the manifest catches truncation that still runs (or corruption that keeps the file executable); the missing-line rule catches a checker that produces nothing, including `check_integrity` itself if the mount clips it.

### 2. Honesty gate across every document

- The banned-claims matcher moved to `tools/claims_lib.py` (regex + `allow_near` carve-outs), shared by `soq_gate.py` and the new `tools/check_claims.py`, so the SOQ, resume, and 678 can never treat the same rule differently.
- `pre_submit` runs `check_claims` across the SOQ, resume, and every 678 duties `.txt`. `banned_claims` are hard FAIL; a new `scope_watchlist` (asset, inventory, forensic, plus the banned tool names as a safety net) is WARN-level for a human read. A term already hard-failing as a banned claim is not also WARNed (suppress-duplicates).
- `runbook` is now a banned claim, mechanizing the 2026-07-12 MEMORIES rule. It was also removed from JC-524404's `soq_spec.json` keywords, and the soq-builder skill now forbids listing a banned claim as a keyword.

### 3. 678 scrutiny before sign-off

`tools/check_678_scrutiny.py` bundles four checks over one duties block into a report the soq-builder attaches before the 678 sign-off: format + clip (via `check_678`), the banned + watchlist honesty scan, keyword coverage vs the duty statement (the spec keywords are extracted verbatim from it), and a quantification WARN on the primary block. It is a report, not a gate, and does not touch the SOQ loop or the four sign-offs.

### 4. Character-fit helper

`check_678.py --fit` prints total chars, delta to the limit, and each content line's length longest-first, so trimming to the clip is one pass instead of a dozen rebuilds.

## Decisions

Three settled with Uriah before building:

- **Integrity failure short-circuits** the gate (loudest signal; downstream is untrustworthy).
- **The matcher is a shared `claims_lib.py`** (one source of truth over keeping `soq_gate` untouched).
- **The watchlist suppresses duplicates** (a banned term is not also WARNed).

Two resolved during the build:

- **`--regen` reads the working tree, not `git show HEAD`.** The workflow is edit a tool, regenerate, commit both together; a HEAD-based manifest would mismatch your own uncommitted edits and false-fail the next run. The mount-truncation guard lives in the default *check*, which is only ever run against the committed manifest.
- **The pre-flight sweep found two real hits on known-good packages.** `asset-tracking` fired on the standard GLPI-lab résumé bullet in all four recent packages — a false positive from a too-narrow `allow_near` window (widened 80 to 120 chars; GLPI is Uriah's only legitimate asset-inventory context). `simulated-internship` fired on the JC-523777/523947 678 blocks ("simulated enterprise environments"). Uriah's ruling: the Cyber Range is real enterprise tooling in a learning environment, not simulated, so the ban is correct to fire and those blocks carry a real (already-submitted) catch. The clean-package regression oracle is therefore JC-524404, not JC-523777.

## Files

New: `tools/check_integrity.py`, `tools/tools_manifest.json`, `tools/claims_lib.py`, `tools/check_claims.py`, `tools/check_678_scrutiny.py`, `tools/tests/test_gate.py`.
Changed: `tools/pre_submit.py`, `tools/soq_gate.py`, `tools/verify_doc.py`, `tools/check_678.py`, `tools/check_678_pdf.py`, `tools/check_cross_doc.py`, `tools/check_keywords.py`, `tools/check_memory_pointers.py`, `tools/spell_check.py`, `tools/soq_rules.json`, `.claude/skills/soq-builder/SKILL.md`, `MEMORIES.md`, `CLAUDE.md`, `JC-524404/soq_spec.json`.

## Running and maintaining it

- `python tools/pre_submit.py "<JC folder>"` runs the whole gate, integrity first.
- `python tools/tests/test_gate.py` runs the regression + planted-failure harness (run after `--regen`).
- **After ANY `tools/` or `soq_rules.json` edit, run `python tools/check_integrity.py --regen` and stage the manifest in the same change, in a trusted (non-mount) session.** Skipping this makes the next `pre_submit` hard-fail on the mismatch. This is wired into CLAUDE.md's mechanize-corrections clause.
