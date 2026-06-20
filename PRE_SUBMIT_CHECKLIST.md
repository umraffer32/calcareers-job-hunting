# Pre-Submit Audit Checklist

Run this as ONE structured pass **before the first full review** of any SOQ, resume, cover letter, or STD 678 — not piecemeal across many review rounds. Created 2026-06-20 after the JC-522217 cycle, where honesty and format issues surfaced one at a time over ~20 edit rounds. Catch them all up front.

## 1. Honesty / claim audit (the most important)
- [ ] Every named tool, product, platform, or skill traces to something Uriah has actually done (a repo, a prior submitted doc, `Employment_History_STD678.md`, `MEMORIES.md`, or a statement he made). No tool/skill/duty claimed just because the posting names it.
- [ ] No claim of supporting end-user **hardware at a job** — his hardware experience is building his own devices and homelab (server/storage), not job support. The internship is **remote**, so it cannot include hardware support.
- [ ] No **Microsoft 365 support** claim — he has no hands-on M365 support experience (confirmed 2026-06-20).
- [ ] No claim he **wrote / coded / developed** scripts or Lambdas — AI generated the code after he had the idea and tested it. Use "used / ran / built and tested / configured," never "wrote." (Configuring AWS resources is fine to claim.)
- [ ] No ServiceNow, ESXi, Intune/SCCM, imaging (he installs from ISOs), or asset-tracking claims unless newly verified.
- [ ] Self-employment (options trading / online business) NOT reintroduced; employment gap left unexplained per settled call.
- [ ] ITIL 4 not used as evidence in prose (cert LIST only).

## 2. Cert + date sanity (678 especially)
- [ ] No certification with a **future issue date** (caught the Cloud+ 07/03/2026 typo on JC-522217 — should have been 2025).
- [ ] CompTIA certs read as ~3-year validity; issue/expiration internally consistent.
- [ ] Cert slots on the 678 (only 3 fit): Security+, Network+, Cloud+ for cloud/security-heavy roles; A+/Network+/Security+ for general help-desk/support. All four CompTIA stay on the resume regardless.
- [ ] Exam/Job Title line has JC number + position number (+ RPA number verbatim IF the posting names one). Re-read the posting's Filing Instructions for a required RPA.

## 3. Anti-AI / voice / format
- [ ] No em dashes anywhere.
- [ ] No mid-sentence colons (colon only introduces a real list).
- [ ] Acronyms spelled out exactly **ONCE per document** (first use only), then bare — including across separate SOQ answers. SOQ + 678 only; resume is exempt for common IT acronyms.
- [ ] Contractions used; no buzzwords (leverage, robust, seamless, passionate); no throat-clearing openers or empty conclusions.

## 4. Spec compliance (check the posting every time)
- [ ] SOQ: page limit, font, font size, margins, alignment exactly as the posting states; verify the built PDF's page count and that every character is the required size/font.
- [ ] Resume: Calibri house style, one page (see CLAUDE.md rule 13).
- [ ] Redundancy pass: resume = terse keyword version, SOQ = narrative; no two docs read like a paste; vary anecdotes.
- [ ] Cross-document consistency: dates, titles, degree, certs, and claims match across resume, SOQ, and 678.

## 5. Workflow hygiene
- [ ] Drafted in the scratchpad; only the FINAL approved version copied into the per-JC folder (avoids the file-lock churn).
- [ ] Claude builds the PDF via the docx → LibreOffice flow (renders as metric-compatible LiberationSans, which is visually Arial — accepted by Uriah). Claude creates the PDF, not Uriah. Do NOT use the Google Drive connector to export.
