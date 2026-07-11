---
name: soq-builder
description: >-
  Build the FULL CalCareers application package for a posting Uriah has already chosen —
  folder setup and source PDFs, soq_spec.json extraction with an advisory diff against the
  prior posting, an evidence-allocation plan (hard STOP for approval), the SOQ drafted
  through an internal build -> gate -> rubric -> honesty loop (max 3 iterations) and
  presented with a findings changelog, a light resume clone/retarget, the STD 678 duties
  block, the pre_submit gate, and the post-submission routine. Trigger whenever Uriah asks
  to build his SOQ or application for a specific posting: "build my SOQ for JC-######",
  "build my application for JC-######", "start the application for JC-######", "let's
  apply to JC-######", "draft the SOQ for the DMV job", or equivalent once a position is
  locked. Do NOT use for picking/triaging jobs (that is recommend-job's job) or for
  non-state applications. The four human sign-offs (allocation, SOQ, resume, 678) are
  non-negotiable and never skipped.
---

# Build a CalCareers application (SOQ-led, full pipeline)

Run the whole JC-523478-style build for one locked-in posting. The governing idea, from
SOQ_GATE_PLAN.md: the first draft Uriah reviews must have ALREADY survived every
mechanical and adversarial pass, so his review starts at what used to be v5 quality.
"Good to go" means gate-clean and self-audited, awaiting his read — NEVER
ship-without-reading. Everything ships under his name; the 678 is signed under penalty
of perjury.

## Non-negotiables

- **Four stop points, fixed:** (1) evidence-allocation approval BEFORE any drafting,
  (2) SOQ sign-off, (3) resume sign-off (light), (4) 678 duties sign-off. Do not merge,
  reorder, or skip them, even if Uriah seems in a hurry.
- **Honesty stays human.** The gate's blocklist only knows PAST mistakes. Every claim in
  every doc must trace to MEMORIES.md, `Base Resume and Employment History/Employment_History_STD678.md`,
  a project's own docs, or something Uriah said himself. Anything uncertain becomes a
  QUESTION to Uriah — it never goes into a doc on a guess. Never claim a tool, skill, or
  duty he hasn't done; never confess gaps on a scored doc either (reframe to real
  adjacent work; gaps are interview material, captured in Interview_Prep).
- **Draft in the outputs scratchpad, versioned.** Every rebuild gets a NEW filename
  (`_v1`, `_v2`, ...), never overwrite. Copy into the JC folder ONLY the final approved
  version. Keep a running changelog of what changed in each bump and why.
- **Large-file writes in this environment truncate silently** (>~13 KB via the file
  tools). Write big files via bash heredoc, then verify the tail and (for code) compile.
  After any real edit whose output did not change, treat it as a FILE-WRITE failure, not
  a content problem (CLAUDE.md rule 11).
- **No git commit or push, ever, without Uriah's explicit say-so.**
- **No mid-sentence colons anywhere; ZERO colons in the SOQ** (numeric times/ratios and
  the posting's own prompt wording excepted). No em/en dashes in any deliverable.

## Step 0 — Required reading (all of it, before anything)

1. `MEMORIES.md` (the always-loaded core: rules, settled decisions, gaps, and the
   Evidence Bank index). Full story narratives live in `Evidence Bank/` — read the
   specific bank files the allocation plan names (Step 3), not the whole folder.
2. `SOQ Research/soq-writing-guide.md` and `SOQ Research/soq-header-formatting.md`.
3. The posting and the duty statement IN FULL (see Step 1 for where they come from).
4. `PRE_SUBMIT_CHECKLIST.md`.
5. For every GitHub project an answer might cite: the repo's README AND its `docs/`
   pages, in full, via `github.com/umraffer32/<repo>/blob/main/<path>`. The credible
   specifics live deep (e.g. aws-ha-infra's `docs/resilience-testing.md`).

## Step 1 — Folder and source documents

- Create `JC-###### (Working Title) - IN-PROGRESS/` in this repo root.
- Copy `posting.pdf` and the duty statement from
  `../CalCareers Job Scraper/data/jobs/JC-###### (Title)/` (duty statement may be .docx;
  a closed posting lives under `../CalCareers Job Scraper/_closed/`). If the scraper has
  neither, ask Uriah for the files — the Cowork sandbox cannot run the scraper.
- Extract text with `pdftotext`/`pdfplumber` in bash (the Read tool's PDF path fails
  here); rasterize with `pdftoppm` and read visually if there is no text layer.

## Step 2 — Extract the spec (`soq_spec.json`) + advisory diff

Read the posting's SOQ / Written Response / Filing instructions TO THE LETTER and write
`soq_spec.json` into the JC folder. Fields (see the filled example in
`JC-523478 (Information Technology Associate) - SUBMITTED/soq_spec.json`):

- `jc`, `title`; `prompts` — each prompt string VERBATIM, character for character, in
  posting order; `numbered_headings` (default true when 2+ prompts).
- `page_limit`, `font`, `size_pt` (+ `size_is_minimum: true` when worded "no less
  than"; still BUILD at exactly the stated size), `margins_in`, `spacing` if specified.
- `advisories`: `left_align`, `simple_formatting` (no justified text / text boxes /
  custom bullets / tables), `flatten_pdf` — set only what the posting actually says.
- `keywords`: the desirable-qualification and duty-statement terms. Write verb keywords
  as STEMS ("communicat", "collaborat") so `check_keywords.py` matches all inflections
  instead of reporting false misses. These feed the gate's INFORMATIONAL coverage report
  only — never a target to maximize.
- `app_line_tokens`: REQUIRED whenever the posting's filing instructions name identifiers
  for the application (position number, RPA, JC) — each required string verbatim (e.g.
  "815-626-1401-012", "RPA:0961", "JC-523777"). `check_678_pdf.py` verifies them against
  the generated form.
- Optional `filing_notes`: anything else the Filing Instructions demand on the 678
  (supplemental forms, transcript copies).

Then DIFF this spec's format + advisories block against the most recent SUBMITTED
folder's `soq_spec.json` and tell Uriah what is NEW or CHANGED for this posting (this is
the mechanism that would have auto-caught JC-523478's novel "left-align" advisory). If no
prior spec exists, say so and move on.

## Step 3 — Evidence-allocation plan -> STOP (sign-off 1 of 4)

- One line per prompt: the primary evidence (project/story) that answers it, plus any
  secondary, **naming the backing `Evidence Bank/<slug>.md` file for each**. NO
  double-spend — a project may appear in two answers ONLY if the facet differs; a number
  or named result may appear exactly once in the whole SOQ.
- **READ every named bank file before drafting** — the pointer's ⚠ constraint is the
  claim ceiling, the file is the source (numbers, scope, forbidden framings). This is
  checked at this STOP: the plan is not presentable until the named files are read.
- Answerability check: if a heavily weighted prompt demands experience Uriah does not
  have, say so plainly — that can still be a late PASS decision, his call.
- Check each named bank file's USED-IN line for the story's prior use and note what must
  be reworded (the no-paste rule applies across applications too); spot-grep the
  SUBMITTED SOQs only when USED-IN looks stale or ambiguous.
- Present the plan and WAIT for approval. Do not draft anything before it.

## Step 4 — SOQ internal loop (cap: 3 iterations; no user review inside the loop)

Draft v1 by cloning the CLOSEST-ROLE submitted SOQ's document format, then overriding
with this spec. House rules: header per `soq-header-formatting.md` (no phone/email);
verbatim numbered prompt headings; each answer ONE flowing paragraph (no orphaned
stacked lines); acronyms spelled out once per document, first use only ("IT" stays
bare); real numbers from the verified list; STAR structure per the writing guide.

Each iteration N:

1. **Build vN** in the scratchpad under a new filename.
2. **Mechanical pass:** `python3 tools/soq_gate.py <vN.docx> --spec <JC folder>/soq_spec.json`
   and `python3 tools/verify_doc.py <vN.docx> --type soq --font <F> --size <S> --max-pages <P>`.
   Render the PDF fresh, page-count THAT file, rasterize page 1 and actually look at it.
3. **Fresh-eyes review — one subagent per iteration (settled 2026-07-03):** run the
   adversarial rubric pass AND the honesty/claims pass as a SINGLE fresh-context
   reviewer subagent (Agent tool) that never saw the drafting. The point is
   independence: the drafting context makes its own errors look right, and a cold
   reader sees the page the way a screener does. Give the reviewer ONLY:
   - the vN draft (docx path or extracted text), the posting and duty statement
     paths, and `soq_spec.json`;
   - instructions to read `MEMORIES.md`,
     `Base Resume and Employment History/Employment_History_STD678.md`,
     `SOQ Research/soq-writing-guide.md`, and `tools/soq_rules.json` before judging;
   - any facts Uriah verified IN THIS SESSION that are not yet in MEMORIES, passed
     explicitly (the subagent cannot see the conversation).
   Its brief: (a) score the draft against the desirable quals and duty keywords as a
   skeptical rater (coverage is data, not a quota); check thesis/proof alignment per
   paragraph (every claim shown, not asserted) and headroom use (~90%+ of the page
   limit, no padding); (b) trace EVERY claim to a source and hunt fabrications the
   blocklist does not know yet — tool names, stretched verbs (wrote vs used), duties
   implied but not done, numbers not on the verified list. It returns a FINDINGS LIST
   ONLY (location, issue, why, severity) — it never rewrites the draft. Uncertain
   claims go on the QUESTIONS list for Uriah, never into the doc. If no subagent
   capability exists in the session, run both passes in-session and note that
   fallback in the changelog.
4. Fix everything found in the MAIN session — the fixer needs the full drafting and
   allocation context; a separate editor agent is handoff loss for no gain. Log each
   catch (iteration, what, why) in the findings changelog, rebuild as vN+1.

Exit when a full iteration finds nothing new, or after 3 iterations. If a genuinely new
verified fact or a new banned-claim pattern surfaced, update `tools/soq_rules.json` (and
MEMORIES.md) in the same session.

## Step 5 — Present ONE candidate -> STOP (sign-off 2 of 4)

Present a single SOQ with:
- the FINDINGS CHANGELOG — what each internal pass caught and fixed, per iteration
  (this is the acceptance bar: the draft arrives already-audited, with receipts);
- any open honesty QUESTIONS for Uriah;
- the keyword-coverage report, labeled informational.

Iterate on his feedback (new version number per revision; batch trivial edits, only
re-render when length could change). On sign-off: run the compliance-to-the-letter
recheck on the FINAL file, produce the flattened PDF, copy both into the JC folder as
`Uriah_Raffer_SOQ_JC-######.docx/.pdf`, update `PROGRESS_LOG.md`.

## Step 6 — Resume, light effort -> STOP (sign-off 3 of 4)

The resume is the LEAST important document in a state application (Uriah's own research;
sometimes unread). Clone, retarget, verify, move on — no deep rework, no re-litigating
structure per application.

- Clone the closest-role Calibri-lineage SUBMITTED resume: support/service-desk lane =
  `Uriah_Raffer_Resume_JC-523478` (current 6-section template: Professional Summary /
  Education and Certifications / Experience / Projects and Lab Experience / Customer
  Service Experience / Technical Skills — a guideline and default, not a hard rule; the
  one firm piece is Block Advisors stays OUT of Experience); server/sysadmin/security
  lane = the `JC-521435` lineage. NEVER the plain base resume, NEVER Arial-lineage.
- After cloning, strip `all_caps` from the section-header runs so headers render Title
  Case; the 17pt name stays all-caps. Title Case the skills-row phrases; prose stays
  sentence case.
- Retarget the summary and a handful of keywords to THIS posting's language; keep
  acronyms bare (resume is exempt from spell-outs); no education/certs in the summary;
  ~90-100% page fill; verify with `tools/verify_doc.py --type resume --font Calibri`.
- Present for the light sign-off.

## Step 7 — STD 678 duties block -> STOP (sign-off 4 of 4)

- Source wording from `Employment_History_STD678.md` and the latest SUBMITTED duties
  .txt, then MIRROR THIS posting's duty-statement language for the screening keywords.
- Evidence-distribution rule: no beat spent twice across SOQ / resume / 678. When the
  678 and the resume converge, reword the 678 (it has the ~1,000-char room; the resume
  stays tight).
- Constraints: <=1,000 characters INCLUDING whitespace and blank lines; no em/en dashes;
  a colon only to introduce a list; acronyms spelled once. Save into the JC folder as
  `Uriah_Raffer_STD678-duties_JC-######.txt` (the gate reads it; it is also the record
  of the exact submitted wording).
- Surface `filing_notes` from the spec: if the posting names an RPA number, the 678
  Exam/Job Title line must carry it VERBATIM, labeled "RPA <number>", plus the position
  number. Cert slots hold three — pick the three most relevant (A+/Net+/Sec+ for
  support; swap Cloud+ in for cloud/security-heavy roles).
- Duties block format (zero tolerance): plain sentences one per line, NO bullet
  characters, exactly ONE blank line between items — `check_678.py` enforces it.
- Present for sign-off. Do not re-raise settled 678 items (county field, 2020-2022 gap,
  Criminal Record Supplemental, driver-license fields, Robert's reason-for-leaving).
- **After the duties sign-off:** Uriah fills the CalCareers template; save the GENERATED
  form into the JC folder as `Uriah_Raffer_STD678_JC-######.pdf`, run
  `python3 tools/check_678_pdf.py` on it (pre_submit also runs it automatically when the
  PDF is present), and fix anything it flags ONCE, BEFORE submission — this is what
  catches a missing RPA or a clipped duties tail while it is still fixable.

## Step 8 — Full mechanical gate

`python3 tools/pre_submit.py "<JC folder>"` — the spec supplies pages/font/size
automatically. Every check PASS; every WARN read and either fixed or explicitly
justified (e.g. known-benign acronym warns). The honesty audit stays the human pass:
one final claim-by-claim read against MEMORIES and `PRE_SUBMIT_CHECKLIST.md` section 1.

## Step 9 — The moment Uriah says "submitted"

Without being asked: (a) rename the folder to `- SUBMITTED`; (b) save the uploaded 678
into it as `Uriah_Raffer_STD678_JC-######.pdf`; (c) update `PROGRESS_LOG.md`; (d) write
`Interview_Prep_JC-######.md` — the 2-3 things a panel will most likely probe (the real
gaps for THIS role plus the gap-handling framing from MEMORIES) and his 2-3 strongest
talking points, honest and posting-specific.

## What stays human, permanently

Evidence allocation (strategy). Novel-claim honesty (the blocklist only knows past
mistakes). The ship decision. The loop's job is to make Uriah's read short, not to
replace it.
