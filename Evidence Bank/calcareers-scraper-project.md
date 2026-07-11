# CalCareers Job Search Scraper — resume/SOQ project brief
DATE: 2026-06-22 | CONFIRMED-BY: Uriah
PROVES: Ready-to-use bullet variants, verified facts, and talking points for the scraper project (Python, requests, BeautifulSoup, headless Chromium; reverse-engineered ASP.NET WebForms API). Genuinely his to claim as software engineering — the design decisions are his.
CONSTRAINTS: Honest verbs only: built, reverse-engineered, automated, engineered, hardened. Follow the used-not-wrote rule for code authorship framing. Repo docs/ pages are the interview prep.
USED-IN: JC-523947 resume (Projects bullet). No SUBMITTED SOQ/678 usage found. [Signature-term search 2026-07-11.]
SOURCE: moved verbatim from MEMORIES.md (split 2026-07-11)
---

# CalCareers Job-Search Automation — Resume Project Brief

**Purpose:** Source material for adding the "CalCareers scraper" project to Uriah's resume.
Self-contained — pick a bullet variant, drop it into the Projects section, and tailor wording
to the target posting. Read the *Framing note* first.

---

## What the project actually is

A personal tool and portfolio project that automates the Sacramento-area California state IT
job hunt end to end. CalCareers (calcareers.ca.gov) has **no public API** — it's a classic
**ASP.NET WebForms** site — so the core of the project was **reverse-engineering its search
and reproducing it in Python without a browser**, then building a reliable pipeline around it.

Given a set of saved searches, the tool:
- runs each keyword search by reproducing CalCareers' multi-step WebForms POST protocol;
- filters the broad results locally by exact **classification** and **county**;
- downloads each posting's **Duty Statement** (the document that really decides fit);
- renders the job listing itself **to PDF** using an already-installed headless Chromium
  browser (Chrome/Edge/Brave, auto-detected — zero extra dependencies);
- organizes everything into tidy **per-job folders** (`JC-<id> (<title>) - <ITA|ITS1>/`
  containing `posting.pdf` + `duty_statement.pdf`), plus a machine-readable manifest.

The output is a clean corpus that a downstream agent (a separate `recommend-job` skill) reads
against the résumé to rank fit. **This repo's job is to produce the corpus; a separate step
assesses it.**

---

## Framing note (read before writing)

Unlike a guided exercise, this is **genuine software engineering Uriah owns and can claim** —
the design decisions (phased build, local-filter strategy, idempotent writes, closed-job
lifecycle) are his. The one thing to do before interviews: **be ready to speak to the
mechanics.** The repo already includes `docs/how-it-works.md` (a plain-English study guide +
interview-prep) and `docs/findings.md` (the full reverse-engineering log) — review those so the
WebForms/HTTP details are fresh. Honest verbs: *built, reverse-engineered, automated,
engineered, designed, hardened.*

---

## Verified facts you can cite

- **Stack:** Python, `requests`, `beautifulsoup4`, headless Chromium (auto-detected, no extra
  dependency), Git/GitHub. MIT-licensed.
- **Scale:** processed **64 postings** (43 currently open + 21 auto-archived as they closed)
  across **5 counties** (Sacramento, Yolo, Placer, El Dorado, Solano) and **2 classifications**
  (IT Associate, IT Specialist I).
- **The hard part:** CalCareers has **no public API**. Search is a two-step ASP.NET WebForms
  exchange — POST the form (full ViewState) → server returns a 302 with the search criteria in
  the redirect's **URL fragment** → results render only after a *second* postback. The tool
  reproduces both POSTs directly, so no browser is needed for searching.
- **Reliability:** idempotent re-runs (skips already-collected work), **atomic writes**
  (temp → fsync → validate → `os.replace`, so an interrupted run never corrupts data), and a
  **closed-job lifecycle** (closed postings archived to `_closed/`, restored if they reopen,
  never deleted) — safe to run on a schedule.
- **Good-citizen design:** single reused session, honest User-Agent, ~1.5 s/request rate-limit,
  100 results/page to minimize requests.
- Built in **4 reviewable phases** (reverse-engineer → search runner → collect postings → widen
  the net), and ships a bundled Claude Code skill ("run the scraper").

---

## Placement

Add to the **Projects** section, matching the existing format:
`• <Name> (<stack>): <one dense sentence>.`

---

## Ready-to-use bullet options

**Primary:**

> • CalCareers Job-Search Automation (Python, requests, BeautifulSoup, headless Chromium):
> Built an end-to-end pipeline that reverse-engineers California's CalCareers job site (an
> ASP.NET WebForms application with no public API) to run saved searches from Python without a
> browser, filters results by classification and county, downloads each posting's Duty
> Statement, renders the listing to PDF via an already-installed headless Chromium browser, and
> organizes everything into per-job folders — idempotent with atomic writes and an open/closed
> posting lifecycle so it runs safely on a schedule, packaging 60+ postings across five counties
> into a clean corpus for fit review.

**Tighter (space-constrained):**

> • CalCareers Job-Search Automation (Python, requests, BeautifulSoup, headless Chromium):
> Reverse-engineered California's CalCareers ASP.NET WebForms search (no public API) to run
> saved searches from Python, then filter by classification/county, download Duty Statements,
> render listings to PDF, and organize per-job folders — idempotent and schedule-safe, packaging
> 60+ postings across five counties for downstream fit review.

**Engineering-forward (emphasizes the reverse-engineering, for software/automation roles):**

> • Web Automation Pipeline — CA State Job Postings (Python, requests, BeautifulSoup, headless
> Chromium): Reverse-engineered an ASP.NET WebForms search with no public API (multi-step POST
> with ViewState, search criteria hidden in a redirect URL fragment, results rendered only after
> a second postback) and reproduced it in Python; layered on local filtering, Duty Statement
> downloads, headless-Chromium PDF rendering with zero added dependencies, idempotent atomic
> writes, and an archive-on-close lifecycle — 60+ postings packaged across five counties.

---

## Name options

CalCareers Job-Search Automation · Web Automation Pipeline (CA State Job Postings) · Job-Posting
Scraper & Packaging Pipeline · CalCareers Data Pipeline.

---

## Interview talking points (the engineering decisions — review `docs/how-it-works.md`)

- **Two-step WebForms search + the fragment gotcha:** no JSON API; the search criteria hide in a
  302 redirect's URL *fragment*, and results render only after a separate postback — reproduced
  both POSTs directly instead of driving a browser.
- **Broad keyword, precise local filtering:** CalCareers keyword search is broad full-text, so
  fetch broadly then exact-match locally on classification and county.
- **Idempotency + atomic writes:** temp → fsync → validate → `os.replace`; an interrupted run
  never corrupts existing data, so re-runs only do new work.
- **Closed-job lifecycle:** archive closed postings to `_closed/` (never delete), restore on
  reopen — `data/jobs/` always reflects only currently-open roles, making it schedule-safe.
- **Zero-dependency PDF rendering:** drive an already-installed Chromium browser headlessly
  instead of adding a PDF library or a browser download.

---

## Tailoring per posting

- **Automation / scripting / IT roles:** lead with Python, web automation/scraping,
  reverse-engineering an undocumented interface, data-pipeline design, and reliability
  (idempotency, atomic writes, scheduling).
- **Analyst / GRC / compliance roles:** frame it as automated evidence/data collection — pulling
  and organizing source documents (Duty Statements, postings) into a clean, reviewable,
  auditable corpus.

> Direction note: this pairs naturally with the Sentinel automation project as a second data
> point on the same theme — Uriah builds tooling to automate tedious, repetitive work
> reliably — which is exactly the instinct that fits security automation and VM/GRC roles.
