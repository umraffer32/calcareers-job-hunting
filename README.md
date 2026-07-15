# CalCareers Job Hunting

Uriah Raffer's working folder for applying to California state IT jobs through CalCareers. This is not a codebase. The output is application materials, tailored resumes, Statements of Qualifications (SOQs), and STD 678 content, for specific job postings. A handful of Python scripts under `tools/` check that mechanical formatting rules hold before anything gets submitted, but the real work here is writing and honesty, not code.

Full working rules live in [CLAUDE.md](CLAUDE.md) and [MEMORIES.md](MEMORIES.md). Read those before touching anything. This file is just a map.

## Folder structure

Each job application gets its own folder, tagged by status.

- `JC-###### (Title) - IN-PROGRESS/` while a draft is being worked.
- `JC-###### (Title) - SUBMITTED/` once filed, with the posting PDF, duty statement, and final deliverables.

Postings Uriah decides to pass on are deleted entirely. Only IN-PROGRESS or SUBMITTED folders exist in the repo at any time.

Deliverables inside a job folder follow `Uriah_Raffer_<Doc>_JC-######`, produced as both `.docx` and `.pdf` (e.g. `Uriah_Raffer_Resume_JC-520957.docx`). Submitted folders also carry an `Interview_Prep_JC-######.md`, written at submission time or, for older applications, the moment an interview actually gets scheduled.

## Root-level reference files

- **[CLAUDE.md](CLAUDE.md)** — the working rules for tailoring a resume, SOQ, or STD 678 to a posting, and the post-submission routine.
- **[MEMORIES.md](MEMORIES.md)** — the always-loaded memory core. Who Uriah is, settled decisions, honesty gaps that must never be papered over, and an index into `Evidence Bank/`.
- **`Evidence Bank/`** — one file per reusable story (the AWS high-availability project, the homelab AD domain, the WGU trouble tickets, and so on), each with what it proves, what it does not, and where it has already been used. Open the file before citing the story in any document.
- **[PROGRESS_LOG.md](PROGRESS_LOG.md)** — the current month's activity log, newest day first. Prior months are rolled into [PROGRESS_LOG_ARCHIVE.md](PROGRESS_LOG_ARCHIVE.md) at the start of each month.
- **[TRIAGE_LEDGER.md](TRIAGE_LEDGER.md)** — compact, tagged one-line records of every posting passed on. Full reasoning for each pass lives in [TRIAGE_LEDGER_DETAIL.md](TRIAGE_LEDGER_DETAIL.md).
- **[RESEARCH_INDEX.md](RESEARCH_INDEX.md)** — a one-line map of every research artifact in the repo, what question it answers and where it lives.
- **[PRE_SUBMIT_CHECKLIST.md](PRE_SUBMIT_CHECKLIST.md)** — the human-judgment checklist run alongside the automated gate before anything is filed.
- `SOQ_GATE_PLAN.md` and `GATE_HARDENING_PLAN.md` — frozen design records for why the pre-submit tooling is built the way it is. Historical, not something to revise casually.

## Other folders

- `Base Resume and Employment History/` — the canonical base resume, WGU transcript, and the pre-approved STD 678 employment history blocks that every application's Duties Performed sections draw from.
- `SOQ Research/` — the SOQ writing guide and header formatting rules. Required reading before drafting any SOQ.
- `Hiring Research/` — background on how CA state hiring actually works, including a sourced synthesis of 300+ r/CAStateWorkers threads at `Hiring Research/Reddit Corpus/`.
- `Cover Letter Research/` — reference material for cover letters, used less often since most postings do not require one.
- `Non-State Applications/` — private-sector applications, tracked separately from the CalCareers pipeline.
- `Archive/` — pre-project applications, kept for history and gitignored.
- `tools/` — the mechanical pre-submit gate (`pre_submit.py` and its checkers). Verifies font, page count, character limits, banned claims, and cross-document duplication. It does not check honesty or claim accuracy; that stays a human read against `MEMORIES.md` and `PRE_SUBMIT_CHECKLIST.md`.
- `.claude/skills/` — the `recommend-job` and `soq-builder` skills that drive job triage and application building.

## The one rule that matters most

Never fabricate experience, including tools. Everything claimed on a resume, SOQ, or STD 678 has to trace back to `Base Resume and Employment History/Employment_History_STD678.md`, an `Evidence Bank/` file, or something Uriah confirms directly. See MEMORIES.md's honest-fit gaps section for the specific things he has not done and should never claim.
