---
name: recommend-job
description: >-
  Triage recent CalCareers IT job postings and recommend the best ones for Uriah to apply
  to — a ranked top 3 with a clear #1 lead pick — scored on honest fit against his real
  experience. Trigger it whenever Uriah asks what jobs look good, or to triage, rank,
  screen, or pick a CalCareers posting — even casually and even if he does not name the
  skill. Example
  triggers: "what jobs are looking good today?", "run the job hunt and find some good
  positions for me to apply to", "find me a job", "best jobs this week", "any new postings
  worth it", "what should I apply to next", "pick my next application". It refreshes the
  scraped data if stale, reads the scraper's candidates.json plus each posting and duty
  statement, excludes jobs already submitted, in-progress, or passed, scores fit against
  Uriah's documents, memory, and past sessions, and returns the ranked picks with verdicts.
  An optional argument sets the lookback window: a number of days, or a since-date.
---

# Recommend the best CalCareers jobs to pursue

Triage recent California state IT postings for Uriah Raffer and recommend the best
applications — a ranked top 3 with a clear #1 lead pick. Run from the "CalCareers Job
Hunting" repo; the scraper data is in the sibling "../CalCareers Job Scraper".

## Defaults — run straight through, do not stop to ask
Use these unless the data is missing or genuinely ambiguous:
- Scope: EVERY currently-open posting in the reachable classifications that has NOT already
  been evaluated (submitted, in-progress, or passed). Do NOT gate on how recently a posting
  was published. The strongest fit is often an older open posting that was never triaged
  (this is exactly how JC-521438 was nearly missed). Use publish_date only to sort
  newest-first for presentation, never to exclude an un-evaluated open posting.
- Classifications: INFORMATION TECHNOLOGY ASSOCIATE and INFORMATION TECHNOLOGY SPECIALIST I
  (Uriah's reachable, list-eligible classes through Dec 2026). Note anything outside these
  but rank it last.
- Skip jobs already handled (SUBMITTED, IN-PROGRESS, or PASSED).
- Weight honest fit first; use the filing deadline only as the tiebreaker between
  comparable fits.
- LANE HEURISTIC (Uriah's real target lane). Weight ITA-level support, service desk,
  desktop/field, and IT support roles as his TRUE fits and lead with them. Treat ITS I
  security-analyst and systems-administrator roles as defensible STRETCHES (applying up), a
  notch below. When a week is thin, say plainly that there is no clean level-matched fit
  rather than pushing a stretch to fill the list. He is rank 1 on both the ITA and ITS I
  lists, so reachability is not the constraint, honest duty-fit is. Bucket by DUTIES, not classification: an ITA-CLASSIFIED role with server or systems-administration duties (e.g. JC-522483, a CHP server-admin ITA) is a defensible STRETCH on duty domain even though the ITA classification is his level. Classification sets the pay band and reachability; the duties set the lane.
- Output a ranked top 3 (lead pick first), each with a verdict and short rationale, plus
  any remaining candidates in a compact runners-up list. If fewer than 3 are genuine fits,
  show only the real ones and say so — do not pad the list to 3 with PASS-grade jobs. Do
  not build any deliverables.

Optional override: by default there is NO date filter (all open, un-evaluated postings are
in scope). If the user passes an argument, it NARROWS to a recency window — a bare number =
days (e.g. "7" = only postings published in the last 7 days), or a date = since that date
(e.g. "since 2026-06-10"). Use this only when the user explicitly wants a narrow recent
sweep; otherwise consider all open un-evaluated postings.

## Step 1 — Check freshness
Read the generated_at timestamp at the top of ../CalCareers Job Scraper/data/candidates.json.
- If it is current (within about 1 day), use it as-is.
- If it is stale (older than ~1 day) or the file is missing, the data needs a refresh before
  scoring. Try to refresh by running the run-scraper skill. IMPORTANT: in a sandboxed
  environment such as Cowork the scraper cannot run (no network or process access), so the
  refresh will fail there. If you cannot run the scraper, do NOT keep retrying — stop and
  tell Uriah the data is stale (give the generated_at date) and that he should run the
  scraper manually first, then re-invoke this skill. Offer to proceed on the existing stale
  data if he would rather not wait.
- Either way, tell Uriah which data you are using (freshly refreshed, or existing data from
  the recorded timestamp).

Normal Cowork workflow: Uriah runs the scraper manually first, then invokes this skill, so
candidates.json is already fresh and no refresh is needed.

## Step 2 — Build the candidate set
- candidates.json is a single JSON object with a "postings" array; each record has
  job_control_id, classification, working_title, publish_date, filing_deadline (dates are
  YYYY-MM-DD), and posting_url. If it fails to parse, STOP and report it — do not analyze a
  partial file.
- Start from ALL postings in candidates.json (every currently-open posting). Do NOT filter
  by publish_date unless the user passed an explicit recency override (see Defaults).
- Keep only the two reachable classifications by default; note anything outside them but
  rank it last.
- EXCLUDE jobs already evaluated, using THREE sources together (a JC is excluded if it
  appears in any of them):
  1. TRIAGE_LEDGER.md in this repo root — the canonical list of passed JCs (each line: JC
     number, title, [category-tag] one-line reason, pass date). This is the fast, reliable
     exclusion source, and the tags double as pass-precedent patterns for scoring new
     postings. Full verbatim reasoning lives in TRIAGE_LEDGER_DETAIL.md — open it ONLY
     when a borderline call needs the full precedent, never for routine exclusion.
  2. PROGRESS_LOG.md — any JC-###### marked SUBMITTED, IN-PROGRESS, or PASSED. Note it
     holds the CURRENT MONTH only (older months are archived); that is fine, because
     folders and the ledger are the canonical sources for older decisions — do NOT open
     PROGRESS_LOG_ARCHIVE.md for exclusions.
  3. Folders in this repo — any "JC-###### (Title) - SUBMITTED/IN-PROGRESS" folder.
  Match on the 6-digit job_control_id. List what you excluded and why, briefly.
- DATA-INTEGRITY GUARD (run before finalizing exclusions): a JC must NEVER appear in BOTH a
  `- SUBMITTED`/`- IN-PROGRESS` folder AND the TRIAGE_LEDGER. Compute that intersection. If any
  JC is in both, the folder is authoritative — the job was actually submitted, and the ledger
  line is a wrong pass written by an earlier run that failed to exclude it. Exclude the JC as
  submitted (not as a pass), and SURFACE it to Uriah so the bad ledger line can be deleted (the
  ledger is passes only). This caught JC-521544 and JC-521522 on the 6/26 run — both submitted
  but logged as passes.
- What remains is the set of OPEN, UN-EVALUATED postings — these are the candidates,
  regardless of age. If this set is empty, say so plainly (everything open has been handled).
- LEDGER UPKEEP: when you (or Uriah) decide to PASS on a posting during this run, append
  BOTH records so it is never re-triaged: the compact line to TRIAGE_LEDGER.md (JC number,
  title, [category-tag] one-line reason, pass date — tag vocabulary in the ledger header)
  AND the full reasoning to TRIAGE_LEDGER_DETAIL.md, newest first in each. Do not add
  submitted/in-progress jobs to the ledger (those are tracked by folder and PROGRESS_LOG);
  the ledger is for passes.

## Step 3 — Read each surviving posting IN FULL
For every candidate, open BOTH posting.pdf AND duty_statement.pdf in
../CalCareers Job Scraper/data/jobs/JC-###### (Title)/ and read them completely.
- The duty statement is sometimes a .docx instead of a .pdf — read whichever exists.
- A posting that has since closed may live under ../CalCareers Job Scraper/data/jobs/_closed/
  JC-###### (Title)/ instead — check there if it is not in the main jobs folder.
- Many duty statements have NO text layer (image-only scans or dynamic Adobe XFA forms) and
  extract as blank. When that happens, rasterize the pages to images and read them visually
  or OCR them — do not skip a duty statement just because text extraction returned nothing.
- From each duty statement capture: essential-function percentages, named tools and
  systems, required vs desirable quals, SOQ requirement + prompts, location/telework,
  WORK HOURS / SHIFT / DAYS (and any weekend, holiday, after-hours, on-call, or rotating-
  shift requirement), and final filing date. Work hours live in the posting's "Working
  Conditions" section and/or the duty statement header. Read both. Do not assume standard
  hours just because none are stated.
- CAPTURE EMPLOYMENT TYPE: permanent vs limited term, and if limited term, the length (e.g.
  12-month LT) and whether it can extend or convert to permanent. Surface it in the output
  (see Step 5) — it is a real decision factor, not a footnote.
- CAPTURE FILING REQUIREMENTS from the posting's Filing/Application Instructions section (not
  just the duties): any required RPA number (capture it VERBATIM), required position-number
  formatting, mandatory supplemental documents (e.g. Criminal Record Supplemental
  Questionnaire, Form 700 / Conflict of Interest), and any background-investigation or
  fingerprinting requirement. If the posting names an RPA number, carry it into the
  recommendation so it lands on the STD 678 Examination/Job Title line — postings routinely
  warn that applications missing the position number AND RPA number "may not be considered,"
  so a missed RPA is a screen-out, not a nicety (caught on JC-522094, 2026-06-19). These
  required forms are also effort/eligibility factors that feed the ranking.
- CAPTURE THE SOQ PROMPTS VERBATIM and the SOQ format and burden (required or not, number of
  prompts, behavioral vs technical, page and font limit). The SOQ prompts decide as much as
  the duties. A posting can pass on duty percentages but still be a hard no because its lead
  SOQ prompt demands experience Uriah lacks. This is exactly how JC-521906 failed, where the
  first prompt asked for asset-tracking experience he does not have.

## Step 4 — Score fit against Uriah's FULL history
Do NOT score from the documents alone. Much of his real experience lives in past
conversations and memory, not in any single file. Pull from all three tiers:

1. Documents and rules (authoritative for honest-fit and writing rules):
   - CLAUDE.md (this repo), `Base Resume and Employment History/Uriah_Raffer_IT_Support_Resume.pdf`, `Base Resume and Employment History/Employment_History_STD678.md`,
     `Base Resume and Employment History/Transcript_UriahRaffer.pdf`, `SOQ Research/soq-writing-guide.md`, `Hiring Research/CA_State_Hiring_Field_Guide.docx`, and
     prior tailored apps in the JC-* folders as examples of what he can honestly claim.

2. Canonical memory (MEMORIES.md is the PRIMARY source for fit/tool decisions):
   - Read `MEMORIES.md` in the repo root FIRST (imported into CLAUDE.md, loads every
     session). The CORE is sufficient for triage: the honest-fit gap list, the
     verified-experience summary, the GitHub portfolio index, the triage strategy, and
     schedule preferences all live there. Do NOT open `Evidence Bank/` files during
     triage unless a posting names something the core summary is genuinely ambiguous
     on — the bank holds drafting-depth narratives, not fit decisions. Also check any
     relevant memory files in this project's memory store and the sibling scraper
     project's store, plus any memories already surfaced into context this session.

3. Past sessions (FALLBACK — only for experience a posting names that MEMORIES.md does not already cover):
   - For each posting's named tools, systems, and key duties, search past session
     transcripts (in this Cowork environment use `mcp__session_info__list_sessions` then `mcp__session_info__read_transcript`; there is no search_session_transcripts tool here) for Uriah's own statements of real
     hands-on experience, prior fit/PASS decisions, and tool-gap clarifications. This is how
     you catch experience he described in conversation but never wrote into a document.
   - Credit ONLY experience Uriah himself affirmed as his own real, hands-on work (a user
     message). Never credit something Claude proposed, a hypothetical, or an ambiguous
     mention. When a transcript hint is unclear, flag it and ASK him rather than assuming —
     this is the same honest-fit rule: never assume a tool or skill.
   - When you find a durable, clearly-relevant experience or decision not yet captured in
     memory or a document, note it and OFFER to save it to auto-memory so future runs keep
     it. Do not save without his okay.

4. GitHub portfolio (his actual proof of real work):
   - His repos are public at github.com/umraffer32. Fetch a repo's README by its blob URL
     (https://github.com/umraffer32/<repo>/blob/main/README.md returns rendered text; the
     /raw/ URL and the repos-tab page come back empty). Use the cached GitHub portfolio index
     in MEMORIES first, and only fetch a README when you need the specifics for a given
     posting. When you DO fetch a repo for specifics, read it IN FULL including its `docs/` subpages (fetch them by their blob URL too), not just the README — the credible numbers live deep (e.g. aws-ha-infra's `docs/resilience-testing.md` held the real failure matrix and recovery times). Map each posting's named duties and tools to a real, nameable project (for
     example control and compliance auditing maps to win11-stigs, vulnerability work to
     vulnerability-management). Treat ONLY what the repos actually show as real, and respect
     the standing rule that auto-solved threat hunts are not usable as manual-investigation
     evidence.

Then judge each posting honestly:
- Map the duty percentages to what he has actually done (internship, WGU labs, homelab, AWS
  project, Block Advisors, Robert's, plus anything surfaced from memory or past sessions).
  Title means little — score the DUTIES.
- CRITICAL tool/skill-saturation test: estimate what share of the essential functions depend
  on a specific tool, system, or duty Uriah has NO hands-on experience with. If a tool he
  lacks runs through a large share of the role (the canonical kill was JC-520758:
  ServiceNow named in ~65% of duties), that is a PASS, not a stretch — adjacent/lab
  experience and "fast ramp" do not survive an interview built around that tool. An
  incidental tool used at a basic level (e.g. logging tickets in a system) is NOT a blocker.
- SOQ-PROMPT ANSWERABILITY TEST (run whenever an SOQ is required). For each SOQ prompt, ask
  whether Uriah can answer it truthfully from real experience in his documents, memory, the
  GitHub portfolio, or past sessions. If the lead prompt or a heavily weighted prompt demands
  hands-on experience he does not have, that is a PASS even when the duty percentages look
  survivable, because the SOQ is the scored gate and he cannot answer it honestly. JC-521906
  is the canonical case, where the first prompt wanted asset-tracking experience he lacks.
- "Applying up" (new grad to a role pitched at an experienced candidate) is fine ONLY if
  every claim would be truthful. Flag seniority stretches (leading IT projects, coaching,
  stakeholder facilitation) explicitly.
- Never assume he has a tool/skill just because the duty statement names it. When unsure
  whether something is honestly claimable, say so.
- WORK-HOURS CHECK (always run, always surface the schedule so he is never surprised).
  Uriah's baseline is a regular weekday daytime schedule, Monday through Friday, and he is
  flexible around it:
  - An early start is fine: anything from about 7 a.m. onward (e.g. a 7 a.m. to 4 p.m.
    schedule is good, he likes the earlier finish).
  - Weekend, holiday, on-call/standby, and after-hours work are FINE and NOT a concern. He
    treats these as overtime, which pays well. Note them neutrally or as a plus, not a flag.
  - Only FLAG as an actual concern a schedule whose BASE hours are non-daytime: a primarily
    night/evening shift, or a rotating/variable shift where he would not have a stable
    daytime baseline. That changes his daily life rather than just adding paid extra hours.
  Always state the schedule plainly (start/end, days, any OT expectation), and ALWAYS in
  12-hour AM/PM format (Uriah dislikes 24-hour time) - convert any 24-hour times the posting
  uses (e.g. 0800-1700 becomes 8:00 a.m. to 5:00 p.m.; 1600 becomes 4:00 p.m.).

Give each posting a verdict: STRONG FIT / STRETCH (defensible) / PASS, with one or two lines
on the duty weighting, the real gaps, the deadline, and the posting URL.

## Step 5 — Recommend the top 3
Rank the surviving postings by honest fit, then use the filing deadline as the tiebreaker
between comparable fits (flag anything closing within ~2 days as act-now). Present the top
3:
- Put the #1 lead pick first, with its working title and posting URL on the FIRST line,
  then its verdict and rationale.
- Then #2 and #3, each with title, posting URL, verdict, a one- to two-line rationale, and
  the filing deadline.
- For EVERY pick, state the SOQ burden next to the deadline, namely whether an SOQ is
  required, how many prompts, and whether they are behavioral or technical. SOQ effort is a
  real decision factor. Do not undersell a heavy multi-prompt technical SOQ as low-effort
  just because the resume can be reused from a prior application.
- For EVERY pick, also state the EMPLOYMENT TYPE (permanent / limited term with length and
  whether it converts) and any REQUIRED FILING ITEMS (required RPA number, supplemental
  questionnaires, Form 700, background/fingerprint) on the same line as the deadline and SOQ
  burden. Example line: "STRONG FIT, deadline 7/2, SOQ required (3 behavioral prompts),
  12-month LT (convertible), requires RPA E-DTD 25-003 on the 678." These are filing-cost and
  job-security factors that belong at decision time, not buried in prose.
- List any remaining candidates below in one compact ranked runners-up list.
- If fewer than 3 postings are genuine fits, present only the real ones and say so plainly
  — never pad the top 3 with PASS-grade jobs just to fill the slots.

## Rules
- Do not fabricate experience or tools. Reality-first pushback — if nothing is a genuine
  fit, say so plainly rather than forcing picks.
- Do NOT build any deliverables. Stop at the recommendation and offer to set up the chosen
  job's "JC-###### (Title) - IN-PROGRESS" folder as the next step (ask which of the top
  picks Uriah wants if it is not obvious).
