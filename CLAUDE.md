# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

This is not a codebase. It is Uriah Raffer's working folder for applying to California state IT jobs through CalCareers. The work here is producing application materials: tailored resumes, Statements of Qualifications (SOQs), and STD 678 application content for specific job postings.

## Folder structure and conventions

- Each job application gets its own folder, tagged with status: `JC-###### (Title) - IN-PROGRESS/` while being worked, renamed to `JC-###### (Title) - SUBMITTED/` once filed. Postings Uriah decides to pass on are **deleted entirely** — only IN-PROGRESS or SUBMITTED folders should ever be visible. Each folder holds the job posting PDF, the duty statement PDF, and the tailored deliverables.
- Deliverables are named `Uriah_Raffer_<Doc>_JC-######` (e.g., `Uriah_Raffer_Resume_JC-520957.docx`). Produce both .docx and .pdf versions.
- New postings to evaluate are surfaced by the **CalCareers Job Scraper** project (`../CalCareers Job Scraper/data/jobs/`), not found manually. When triaging multiple candidates, present them to Uriah one job at a time to avoid confusion.
- Root-level files are shared source material reused across applications.

## Key reference files — read before drafting anything

- `soq-writing-guide.md` — **Required reading before writing any SOQ, resume content, or other prose submitted under Uriah's name.** Defines his target voice (plain, direct, concrete, first person), the anti-AI checklist every draft must pass, the STAR structure for SOQ answers, and the working process: Claude asks targeted questions to pull real specifics from Uriah, then drafts; never invent specifics.
- `Employment_History_STD678.md` — Canonical, pre-approved employment history blocks for the CalCareers STD 678 form, each under the ~1,000-character field limit (the page-4 Duties Performed box clips beyond roughly 1,000 characters, not the 1,500 the form implies), with no em dashes and no mid-sentence colons. Use these as the source of truth for job duties wording. Note the field notes at the bottom (Log(N) Pacific verification contact, the approved brute-force bullet wording, the employment-gap explanation).
- `Uriah_Raffer_IT_Support_Resume.pdf` — Base resume to tailor from for each posting.
- `Transcript_UriahRaffer.pdf` — WGU transcript (B.S. Network Engineering and Security, conferred Oct 2025).
- `CA_State_Hiring_Field_Guide.docx` — Background on how CA state hiring works (exams, eligibility, SOQs, the STD 678). Among its rules: mirror each duty statement's exact language, spell out every acronym, never write "see resume."
- **Auto-memory** — Claude's persistent memory (loaded each session) holds settled application decisions and reusable experience banks. Consult it before asking Uriah to re-explain something. It records, among others: settled STD 678 choices that must NOT be re-raised (the Robert's Retirement reason-for-leaving wording and its Q2 answer, the cert-slot picks, the optional employment gap), Uriah's real experience banks (the WGU lab trouble tickets, the older Dec 2025 apps, the Block Advisors customer-service story), and the writing rules below.

## Working rules

1. **New application:** create the `JC-###### (Title)/` folder, save the posting and duty statement PDFs into it, then tailor the resume and SOQ against the duty statement and the SOQ prompt in the posting.
2. **SOQ workflow:** follow the process in `soq-writing-guide.md` — get the actual prompt and page/word limit, ask Uriah for the real specifics (situation, tools, numbers, outcome), draft with STAR, then check the draft against the anti-AI checklist before calling it done.
3. **Never fabricate experience.** Everything must trace back to `Employment_History_STD678.md`, the base resume, or facts Uriah supplies in conversation. Self-employment (options trading, online business) was deliberately removed from applications — do not reintroduce it.
4. **Formatting constraints for CalCareers fields:** under ~1,000 characters per Duties Performed block (the box clips beyond that), no em dashes, no mid-sentence colons.
5. SOQs typically must follow the exact format the posting demands (page limit, font, numbered responses to each prompt) — check the posting's SOQ instructions every time; failure to follow them disqualifies the application. Verify the built SOQ fits the page limit by converting to PDF and checking the page count before calling it done.
6. **Cert slots on the STD 678 hold only three.** The Licenses section fits three certifications. Pick the three most relevant to the role (A+, Network+, Security+ for help-desk/support roles; swap Cloud+ in for cloud- or security-heavy roles). All four CompTIA certs always stay on the resume regardless.
7. **Writing rules for everything submitted under Uriah's name (SOQ, 678, resume):**
   - **Mirror the duty statement's exact language** in both the 678 Duties Performed blocks and the SOQ, so the screening keywords match.
   - **Spell out every acronym on first use** (e.g., "Domain Name System (DNS)"), then abbreviate — the panel often includes non-technical HR readers who score these.
   - **Avoid cross-document copy/paste.** Reuse the same real experiences across the resume, SOQ, and 678, but vary the wording and use different examples so no two documents read like a paste. After drafting all three, do a redundancy pass: differentiate duplicated anecdotes and reword repeated stock phrases.
8. **Honest-fit triage.** Only pursue roles that are a genuine, defensible technical fit. "Applying up" (e.g., a new grad applying to a role pitched at an experienced candidate) is fine as long as every claim is truthful. Do not gate an application on a tool Uriah lacks when the role only uses it at a basic level (e.g., ServiceNow for a service desk that just logs tickets in it) — apply honestly without claiming it. Pass on roles whose core identity is a real skill gap (e.g., database administration, physical-security platforms).
9. **Keep the progress log current automatically.** After any application activity (drafting or revising an SOQ, resume, cover letter, or STD 678; reviewing and deciding to pass), update `PROGRESS_LOG.md` (newest day first) and the relevant tracking record (the per-JC folder, or `Non-State Applications/` for private-sector apps) without being asked. Record the date, the job, the status, and any issues or decisions.
10. **Post-submission routine.** The moment Uriah says an application is submitted, do all three without being asked: (a) rename the folder from `- IN-PROGRESS` to `- SUBMITTED`; (b) save the uploaded STD 678 into that folder as `Uriah_Raffer_STD678_JC-######.pdf`; (c) update `PROGRESS_LOG.md`.
