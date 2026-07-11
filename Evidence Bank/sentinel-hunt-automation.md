# Sentinel-hunter automation toolkit — resume/SOQ project brief
DATE: 2026-06-22 | CONFIRMED-BY: Uriah
PROVES: Ready-to-use bullet variants and verified facts for the threat-hunt AUTOMATION toolkit (Python, Model Context Protocol, Microsoft Sentinel/KQL).
CONSTRAINTS: ENGINEERING/AUTOMATION framing ONLY: he built the harness, an AI agent investigates inside it. Never claim he "performed threat hunts" or is a "threat hunter"; lead the project name with "Automation". Does not conflict with the one real internship KQL brute-force claim — keep both, let neither inflate the other.
USED-IN: No SUBMITTED SOQ/678 usage found. [Signature-term search 2026-07-11.]
SOURCE: moved verbatim from MEMORIES.md (split 2026-07-11)
---

# Sentinel Threat-Hunt Automation — Resume Project Brief

**Purpose:** Source material for adding the "threat-hunt automation" project to Uriah's
resume. This file is self-contained — pick a bullet variant, drop it into the Projects
section, and tailor the wording to the target posting. Read the *Framing rule* first.

---

## What the project actually is

A self-built automation toolkit (the "sentinel-hunter" skill) that drives Microsoft
Sentinel / Azure Log Analytics CTF-style threat-hunt workflows. It is a Claude Code
**skill** (a guardrailed agent workflow) backed by a custom **Model Context Protocol (MCP)
server**. Components Uriah designed and iterated:

- An **MCP server** wrapping Microsoft Sentinel / Log Analytics so Kusto Query Language
  (KQL) runs through tool calls.
- A **platform-integration layer** — session auth, question retrieval, and flag submission
  against the hunt platform's API.
- **Guardrails** — sequential + "blind" solving, idempotent/guarded submission (no
  double-submits, gates risky or low-confidence attempts), answer-type/format checks.
- **State reconciliation** that syncs local state against the live platform so a crash or
  manual edit never corrupts the source of truth.
- A **self-improving postmortem engine** — wrong submissions are mined into a cross-run
  "lessons" corpus that the workflow surfaces automatically on future questions.
- Versioned in its own private GitHub repo, separate from the MCP server repo.

---

## CRITICAL framing rule (read before writing)

Frame this strictly as an **engineering / automation** project. Uriah **built the automation
harness**; he did **not** personally perform the investigations or hand-write the KQL — an AI
agent does the reasoning *inside the harness he built*. Therefore:

- ✅ Use engineering verbs: *designed, built, engineered, integrated, hardened, automated, iterated.*
- ❌ Do **not** claim he "performed threat hunts," "investigated incidents," or "is a threat hunter."
- Why this matters: it keeps every claim defensible. In an interview he discusses
  architecture, guardrail design, and tradeoffs — his strengths — not investigation findings.
- It does **not** conflict with his existing internship bullet (which already makes a small,
  honest KQL claim about a brute-force alert). Keep both; this is the *automation* counterpart.

---

## Verified facts you can cite

- **Stack:** Python, Model Context Protocol (MCP), Microsoft Sentinel / Azure Log Analytics,
  the hunt-platform REST API, Git/GitHub, PowerShell.
- **Scale:** built and hardened across **8 multi-stage hunts (~290 questions total)**. One
  representative hunt had **38 graded objectives across 3 stages**.
- **Reliability features (concrete, all his design):** guardrailed submission, state sync
  against the live platform, a self-improving lessons corpus.

---

## Placement

Add to the **Projects** section, matching the existing project format:
`• <Name> (<stack>): <one dense sentence>.`
Lead the name with "Automation" so the engineering is front and center (not "Threat Hunter").

---

## Ready-to-use bullet options

**Primary:**

> • Threat-Hunt Automation Framework (Python, Model Context Protocol, Microsoft Sentinel):
> Designed and iterated a guardrailed automation toolkit that runs Microsoft Sentinel Kusto
> Query Language threat-hunt workflows end to end, wiring a Model Context Protocol server for
> query execution to the platform's API for question retrieval and answer submission, with
> state reconciliation against the live platform, safe idempotent submissions, and a
> self-improving postmortem engine that converts wrong submissions into reusable lessons,
> validated across 8 multi-stage hunts (290+ questions).

**Tighter (space-constrained):**

> • Security Workflow Automation (Python, Microsoft Sentinel, Model Context Protocol): Built a
> guardrailed toolkit that automates Microsoft Sentinel threat-hunt workflows — query
> execution, state tracking against the live platform, safe answer submission, and a
> postmortem engine that turns mistakes into reusable lessons — and hardened it across 8
> multi-stage hunts (290+ questions).

**AI-forward (most transparent about the agent; "agentic automation" is in demand):**

> • Agentic Security Automation (Python, Model Context Protocol, Microsoft Sentinel):
> Engineered an AI-driven framework that solves Microsoft Sentinel threat-hunt workflows under
> strict guardrails (sequential, blind, idempotent submission), integrating a large language
> model agent with a Sentinel query server and the platform API, plus state reconciliation and
> a self-improving lessons corpus, validated across 8 multi-stage hunts (290+ questions).

---

## Name options

Threat-Hunt Automation Framework · Security Workflow Automation · Agentic Security
Automation · Security Operations Automation Toolkit.

---

## Interview talking points (the "why" decisions — all his to defend)

- **Guardrails (sequential/blind):** prevent the agent from "cheating ahead" or peeking at
  future answers — integrity of the workflow.
- **State reconciliation against the API:** a crash or out-of-band edit shouldn't corrupt the
  source of truth.
- **Idempotent/guarded submission:** avoid double-submits and gate low-confidence or repeated
  attempts.
- **Postmortem engine:** convert failures into reusable patterns so the same mistake isn't
  repeated across runs.

---

## Tailoring per posting

Mirror the target posting's language:
- **Automation / scripting / IT roles:** emphasize Python, MCP integration, guardrails,
  repeatability, reliability.
- **GRC / vulnerability-management roles:** emphasize repeatable, auditable, self-documenting
  workflow and "turning findings/mistakes into reusable lessons/controls."

> Note on direction: Uriah's center of gravity is vulnerability management and compliance plus
> security automation — not hands-on investigation. Frame this project as evidence of the
> build-the-tooling instinct that fits VM/GRC automation, not as analyst/hunter experience.
