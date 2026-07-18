---
name: callback
description: >-
  Generate an updated filing-closed-date and interview-window table for every
  currently SUBMITTED CalCareers application - panels typically call back 4 to
  6 weeks after filing closes. Trigger it whenever Uriah asks to generate,
  update, refresh, or check the callback window, the callback table, or the
  interview windows, or asks when he should expect to hear back on his
  applications. Example triggers: "generate callback window", "update the
  callback table", "refresh the interview windows", "when should I expect to
  hear back", "show me the callback table". Runs tools/callback_windows.py for
  the mechanical filing-closed dates and 4-6-week windows, cross-checks
  PROGRESS_LOG.md and PROGRESS_LOG_ARCHIVE.md for any real confirmed
  interview, callback, or rejection that should override the heuristic
  window, then presents the result as a markdown table sorted soonest-to-
  close first.
---

# Generate the callback-window table

Local to this repo. Reports, for every application Uriah has actually filed, when a
panel callback is realistically due.

## Step 1 — Run the mechanical tool
Run `tools/callback_windows.py` from the repo root (`python3` in Cowork, `python` on a
native Windows session — try one, fall back to the other). It walks every
`JC-###### (Title) - SUBMITTED` folder, pulls the Final Filing Date from that folder's
posting PDF, and computes the 4-6-week window (close+28 days to close+42 days) against
today's real date. Do not hand-compute these dates or re-derive the window by hand —
that is exactly what this tool exists to make reliable across month rollovers.

If a row comes back with "COULD NOT EXTRACT filing date", open that folder's posting PDF
directly and pull the Final Filing Date manually — do not drop the row silently.

## Step 2 — Cross-check for anything real
The tool only knows the heuristic window. It does NOT know about an actual scheduled
interview, a callback, or a rejection, because those live as prose in the progress log,
not a structured field. For every JC in the tool's output:
- Check `PROGRESS_LOG.md` (current month) and, if the filing-closed date is more than a
  month old, `PROGRESS_LOG_ARCHIVE.md` too, for that JC number.
- If a real interview is confirmed, scheduled, or already happened, REPLACE that row's
  heuristic window with the real date/time (see JC-520957 as the pattern — a confirmed
  interview always overrides the 4-6-week estimate, it does not sit alongside it).
- If a rejection or pass is logged, annotate the row rather than silently dropping it —
  Uriah still benefits from seeing that an application resolved.
- If nothing real is logged, the heuristic window stands as-is.

## Step 3 — Present as a markdown table in chat
Output the table as markdown in your response text, not through a visualization tool —
this is tabular data, and the visualize skill's own design rules route tables to
response text. Match the shape already established (2026-07-18):

| JC | Role | Filing closed | Interview window (4-6 wks post-close) |
|---|---|---|---|

- Sort by filing-closed date ascending.
- Bold the JC, role, and window cells for any row with a real confirmed interview.
- Mark rows added since a screenshot or prior table Uriah pastes in for comparison as
  *(new)*, if he provides one to diff against; otherwise just present the full current
  set.
- Close with a one-line summary: total applications tracked, how many are currently
  inside their window, and a reminder that only a row with a real confirmed date is a
  guarantee, the rest are still just the 4-6-week estimate.

## Rules
- Read-only. This skill reports; it does not edit PROGRESS_LOG.md, rename folders, or
  build any deliverables.
- Never invent a confirmed interview date. If Step 2 finds nothing, the row stays a
  heuristic window, not a guess dressed up as a fact.
- Every SUBMITTED folder gets a row. Do not exclude one because it looks old or because
  its window already closed — a stale window with no callback is still information
  (it's evidence to reconsider that lead, not a reason to hide the row).
