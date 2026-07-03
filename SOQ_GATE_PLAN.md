# SOQ Gate + Self-Looping Builder — Implementation Plan

_Drafted 2026-07-03, out of the JC-523478 SOQ session (v1 to v6). Status: **BUILT and validated 2026-07-03** (soq_rules.json, soq_gate.py wired into pre_submit.py, soq-builder skill, JC-523478 example spec; validation record in MEMORIES). Not yet dogfooded on a live posting._

## Why this exists

The JC-523478 SOQ took six versions. Two revisions existed only because a later adversarial pass caught errors an earlier pass had produced (a drifted quantifiable, "70 clients" vs the verified "~70 returns"; and a gap-confession sentence, "rather than time on a paid desk," that violated the settled JC-521435 rule). A third fix (left-aligning the header) came from a posting advisory that was NEW to this posting and therefore not covered by lineage precedent. All three catches are mechanizable or procedurally forceable. The goal is that the first draft Uriah reviews already survived every pass, so his review starts at what used to be v5 quality.

## Component 1 — `tools/soq_gate.py` (hardened mechanical gate)

Extends what `verify_doc.py` already covers (font, size, pages, margins, em/en dashes, zero-colon rule, acronym-once advisory). New checks, in priority order:

1. **Banned-claims blocklist (hard FAIL).** Scan the SOQ text for claims Uriah must never make. Seed list from MEMORIES. ServiceNow, Intune, SCCM, Configuration Manager, MDM, Endpoint Manager, Microsoft 365 / M365, Wireshark (as tool or skill), imaging / system image, asset tracking / inventory (as experience), SQL, Cherwell, "wrote a script" / "coded" / "developed a script" (authorship verbs for AI-generated code), ITIL outside a certification list, GPO / Group Policy depth claims, VMware ESXi, hardware support at the internship, training sessions (as delivered experience). Case-insensitive, word-boundary aware. Every hit prints the settled MEMORIES rationale.
2. **Verified-numbers whitelist (WARN).** Extract every number from the doc and flag any not on the verified-quantifiables list (30, 3, 90%, 6 scans, ~100 attempts, ~70 returns, ~$24,000, 10 STIG controls, ~2 min failover, 4-hour / 2-day GLPI SLA targets, 2 domain controllers, 16-char password policy, 4 CompTIA certs...). Catches the "70 clients" drift class mechanically. Whitelist lives in the rules file and grows as new facts are verified.
3. **Confession-pattern scan (WARN).** Regex for gap-narration phrasing. "I haven't", "I have not used", "no experience", "rather than time on a", "not a real", "I'm still weak", "still learning", "yet to". Warn-level because honest sentences can match ("much of it was new to me" was fine in the Robert's story). Each hit is a prompt to justify or cut.
4. **Verbatim prompt-heading check (hard FAIL).** Given the posting's exact prompt strings (supplied in a small per-JC spec file), confirm each appears character-for-character as a heading in the doc, numbered in posting order.
5. **Formatting-advisory checks (hard FAIL when the posting asks).** No centered or justified paragraphs when the posting says left-align. No text boxes (`txbxContent`), no bullet/numbered lists (`w:numPr`), no tables when "simple formatting" is requested. Flattened-PDF check on the final PDF (no AcroForm fields, not encrypted).
6. **Cross-answer double-spend check (WARN).** Segment the doc by question headings; flag any number or distinctive proper noun appearing in two answers. Same idea as `check_cross_doc.py` but within one document.
7. **Style-tic counters (WARN).** Count "X, not Y" contrast constructions (warn above 2), flag 3+ single-sentence triads, buzzword blocklist (leverage, utilize, robust, seamless, passionate, dynamic, spearhead, proven track record), throat-clearing openers, and "genuinely".
8. **Keyword-coverage REPORT (informational only, never pass/fail).** Given the posting's desirable-qual and duty-statement keywords (in the per-JC spec file), report which appear in the SOQ. Explicitly NOT a target to maximize. An uncovered keyword Uriah can't honestly claim stays uncovered. Coverage suggestions must route through the honesty banks, never straight into the doc.

### Rules file — `tools/soq_rules.json`

The blocklist, numbers whitelist, confession patterns, buzzwords, and tic patterns live here, curated from MEMORIES, so the lessons persist as data instead of being re-derived each session. Update this file whenever MEMORIES gains a new banned claim or verified quantifiable.

### Per-JC spec file — `<JC folder>/soq_spec.json`

Written once per application after reading the posting. Exact prompt strings, page limit, font + size, margins, spacing if specified, advisory flags (left-align, simple-formatting, flatten), and the keyword list. The gate reads this instead of hardcoded values. Building it forces the to-the-letter read of the posting up front. The builder skill should also DIFF the advisory block against the previous application's posting and surface anything new (this is what would have auto-caught "left-align the text" on JC-523478).

## Component 2 — `.claude/skills/soq-builder/SKILL.md` (the loop, codified)

Same repo-skill pattern as `recommend-job`.

**Scope widened 2026-07-03 (Uriah's call): despite the name, this skill covers the FULL build phase, not just the SOQ.** Trigger phrases: "build my SOQ for JC-######", "build my application for JC-######", or equivalent once a position is locked (triage stays recommend-job's job). The skill runs the whole JC-523478-style pipeline: create the IN-PROGRESS folder and copy the posting + duty statement from the scraper repo; extract the spec and diff advisories; run the SOQ loop below; then clone and retarget the resume from the current house template (per the 6-section guideline in MEMORIES — light effort, resume is the least important doc); draft the 678 duties block with the evidence-distribution rule (no beat spent twice across SOQ/resume/678); run `pre_submit.py`; and on Uriah's "submitted", run the post-submission routine (rename folder, save the 678 export, update PROGRESS_LOG.md, write the Interview_Prep doc).

**"Good to go" means gate-clean and self-audited, awaiting Uriah's read — NOT ship-without-reading.** The stop points are fixed: (1) evidence-allocation plan approval before drafting, (2) SOQ sign-off, (3) resume sign-off (light), (4) 678 block sign-off. Rationale from the JC-523478 session: the mechanical and adversarial passes caught the drifted number, the gap confession, and the left-align advisory, but the resume section-structure call and the gap-adjacency call were taste/strategy judgments no gate can make — and everything ships under Uriah's name, with the 678 signed under penalty of perjury. His read is the point, the skill's job is to make that read short.

SOQ loop, order of operations:

1. Read MEMORIES.md, `SOQ Research/soq-writing-guide.md`, `soq-header-formatting.md`, the posting, and the duty statement in full. Extract the spec into `soq_spec.json`. Diff advisories vs the prior posting.
2. Read the relevant GitHub project docs in full for any project the answers will cite (README plus `docs/`).
3. Propose the evidence-allocation plan (one line per prompt, no double-spend). **STOP. Uriah approves before drafting.**
4. Draft v1 by cloning the closest-role submitted SOQ's format. Reword every reused story against its prior use (grep the submitted SOQs first).
5. Internal loop, capped at 3 iterations, no user review yet: build vN, run `soq_gate.py`, run the adversarial rubric pass (score vs desirable quals + duty keywords; thesis/proof alignment per paragraph; headroom use), run the honesty/claims pass (trace every claim to MEMORIES or source; catch fabrications the blocklist doesn't know yet), fix everything found, rebuild as vN+1.
6. Present ONE candidate to Uriah with the internal findings changelog (what each pass caught and fixed). Iterate on his feedback, new version number per revision.
7. On his sign-off, run the compliance-to-the-letter recheck on the final file, copy into the JC folder under the proper name, update PROGRESS_LOG.md.

## What stays human, permanently

- **Evidence allocation** is strategy. Claude proposes, Uriah approves, before any drafting.
- **Novel-claim honesty** is a judgment read. The blocklist only knows past mistakes; new fabrication patterns need the claim-by-claim trace, and anything uncertain goes to Uriah as a question, never into the doc.
- **The ship decision.** The loop converges on "nothing left that a machine or an adversarial pass can find," which is near-shippable. Uriah's review is still the gate that matters.

## Build order (est. ~1 hour total)

1. `tools/soq_rules.json` seeded from MEMORIES (15 min).
2. `soq_gate.py` checks 1-5 (the high-value ones) + wire into `pre_submit.py` (30 min).
3. Checks 6-8 (15 min).
4. `soq-builder` SKILL.md (15 min).
5. Dogfood on the next real posting; tune warn thresholds there rather than speculatively.
