# Migration changelog — MEMORIES split and Evidence Bank creation
DATE: 2026-07-11 | CONFIRMED-BY: Uriah (plan approved this date)
PROVES: n/a — historical record of the memory-store reorganization.
CONSTRAINTS: n/a.
USED-IN: n/a.
SOURCE: this file records the split; the original memory-store note below moved verbatim from MEMORIES.md.
---

## 2026-07-11 — MEMORIES.md split into core + Evidence Bank
MEMORIES.md (100,893 bytes) was split per the approved reorganization plan: rules, settled decisions, gaps, and preferences stay in the always-loaded core; narrative experience entries moved verbatim into one file each here, with pointer lines (slug, claim scope, OPEN-before trigger) in the core's Evidence Bank index. The two root project briefs (CalCareers-Scraper-Resume-Project.md, Sentinel-Hunt-Automation-Resume-Project.md) moved in as calcareers-scraper-project.md and sentinel-hunt-automation.md. Known pre-split deviation kept for the record: three early SOQs (JC-519717, JC-520934, JC-521438) shipped with an oversized title vs their required font spec (header-only, unfixable, documented 2026-06-18).

## 2026-07-11 — Full reorg completed (all six phases)
Same date, the rest of the approved plan executed: CLAUDE.md deduplicated against the core (Memory section rewritten with the routing test + mechanize-corrections clause; rules renumbered 1-14 after deleting the duplicate memory rule); TRIAGE_LEDGER compacted to tagged one-liners (full prose in TRIAGE_LEDGER_DETAIL.md; five June passes backfilled that had never been ledgered: JC-520014/520326/520577/520645/520685; JC-519900 deliberately NOT ledgered - it was shortlisted 6/15 but never decided); June PROGRESS_LOG archived; RESEARCH_INDEX.md created; old apps moved to Archive/ (gitignored); transcript and the resume research report moved out of the root. check_678.py now enforces the exact duties-block format, so pre-2026-07-11 packages fail it on their historical .txt files - expected, never rewrite submitted records. Gate validated end-to-end on JC-523777: OVERALL PASS. Byte results: MEMORIES 100,893 -> 54,590; CLAUDE.md 17,928 -> 16,576; TRIAGE_LEDGER 31,842 -> 14,329; PROGRESS_LOG 139,676 -> 41,028 (incl. this reorg's own log entry).

## Original note: memory store established
Created this project-local memory file and migrated the four facts above out of the opaque built-in auto-memory store, so nothing gets lost and Uriah can see and edit it directly. Going forward, append real experiences and decisions here as they come up.
