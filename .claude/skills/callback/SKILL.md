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
  hear back", "show me the callback table". tools/callback_windows.py emits
  the finished markdown table deterministically (M/D dates, real events merged
  from callback_overrides.json, bolding, sort, summary); the model pastes its
  payload verbatim and only intervenes when the tool's RESULT line says WARN.
---

# Generate the callback-window table

Local to this repo. Reports, for every application Uriah has actually filed, when a
panel callback is realistically due. The tool does ALL the work - dates, windows,
real-event merging, formatting, the summary line. Do not hand-compute, hand-format,
or re-derive anything.

## Step 1 - Run the tool
From the repo root run `python tools/callback_windows.py` (`python3` in Cowork - try
one, fall back to the other). It walks every `JC-###### (Title) - SUBMITTED` folder,
pulls each posting's Final Filing Date, computes the 4-6-week window (close+28 to
close+42), merges real events from `callback_overrides.json` (repo root), scans
PROGRESS_LOG.md and PROGRESS_LOG_ARCHIVE.md for event-like prose lacking an override
entry, and prints the finished markdown table plus summary, then a diagnostics
section below a marker line.

## Step 2 - Only if the RESULT line says WARN
Resolve each WARN by editing `callback_overrides.json`, then re-run until RESULT
says INFO. Skip this step entirely on INFO. NOTE lines are informational and need
no action.
- Real event in the log (interview, rejection, withdrawal, offer) with no override
  entry, or a NEW event for a JC whose entry records an earlier one - read only the
  referenced log lines, then add or update the `overrides` entry. `window_cell` is
  required for every event status; author it in M/D style with no colon except
  clock times, e.g. "Interview confirmed Thu 7/23, 2:00 p.m."
- Filing date could not be extracted - open that folder's posting PDF, read the
  Final Filing Date, add it under `filing_dates` as YYYY-MM-DD. Never drop the row.
- False-positive log mention - add an `ack` entry copying the printed excerpt
  verbatim into its `lines` list (on a JC that already has an event entry, put the
  excerpt in that entry's `ack_lines` instead).

## Step 3 - Paste
Paste everything ABOVE the diagnostics marker into chat verbatim. Do not reformat,
re-sort, re-derive dates, add rows, or annotate. The payload is final.

## Rules
- The ONLY file this skill may write is `callback_overrides.json`.
- Never invent a confirmed date. An override entry must trace to a logged event or
  a posting PDF.
- Every SUBMITTED folder gets a row (tool-enforced). A stale window with no callback
  is still information, not a reason to hide the row.
