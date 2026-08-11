# servicenow-itsm (ServiceNow ITSM PDI Lab) — resume/SOQ project brief
DATE: 2026-08-10 | CONFIRMED-BY: Uriah
PROVES: Real hands-on ServiceNow platform work in a Personal Developer Instance (PDI). Incident lifecycle management with a real work-note diagnosis, a full service-catalog request fulfillment chain, a self-built catalog item wired to a self-authored Flow Designer workflow, and two real debugging catches (an "Assigned to" picker root-caused to group membership, a flow that silently failed to close its parent record).
CONSTRAINTS: **PROJECT IS UNFINISHED — 4 of 9 planned build steps done as of 2026-07-29.** Knowledge base articles, Role-Based Access Control, the CMDB example, and dashboard/reporting are NOT built. Never claim those. Personal PDI lab, never professional/production ServiceNow tenure — frame every claim that way. The overall project can stay present tense ("building an ITSM lab") since the instance is live and active, unlike the decommissioned AD/AWS labs, but don't claim it as complete or closed. Not tied to any specific posting — the project's own README cites the now-closed JC-520758 as its original motivation; don't carry that stale tie-in into new documents. Confirm current build status against the live repo before citing (`gh api repos/umraffer32/servicenow-itsm/git/trees/main?recursive=1`), since Uriah is actively adding to it.
USED-IN: none yet — captured 2026-08-10.
SOURCE: full repo read via `gh api` (public repo `umraffer32/servicenow-itsm`), README.md + BUILD_PLAN.md + WALKTHROUGH.md, 2026-08-10.
---

# ServiceNow ITSM PDI Lab — Resume/SOQ Project Brief

**Purpose:** source material for citing the servicenow-itsm project on a resume (Projects and Lab
Experience section), in an SOQ answer, or as interview prep. Read the *Framing note* before
drafting anything — this project is genuinely still in progress, and the brief only covers what's
actually been built.

---

## What the project actually is

A hands-on ITSM build in a free ServiceNow Personal Developer Instance, closing the one real tool
gap in Uriah's California state IT applications — ServiceNow is the platform most heavily named in
help-desk and service-desk duty statements, and he had zero hands-on time with it before this. The
PDI request sat on ServiceNow's free-tier waitlist for about a month before an instance was finally
allocated on 2026-07-09. Since then he's worked the platform the way an actual help desk agent
would: logging and resolving a real incident, fulfilling a service-catalog request through its full
approval chain, and building a catalog item with an automated approval-and-fulfillment workflow
behind it, debugging real problems in each piece along the way.

Two of the sections that would make it a complete ITSM slice (knowledge base, RBAC, CMDB, and
dashboards) are not built yet. What follows is scoped strictly to what's actually done.

---

## Framing note (read before writing)

This is UI-driven platform configuration Uriah did himself in the browser, form fields, list
views, catalog item variables, Flow Designer steps, so there's no code-authorship hedge needed
the way there is for the AWS/rclone scripts. He built and ran every piece firsthand. The
constraints that DO apply: it's a personal lab instance, never enterprise tenure; it's unfinished,
so only cite incident management, request management, and the catalog item plus workflow; and the
project can be described as ongoing/active (the instance is live), but never as complete.

---

## Verified facts you can cite

- **Incident management, full lifecycle:** logged INC0010003 against a real problem he'd already
  solved (a Linux client not accepting Tailscale's advertised subnet routes), with Impact and
  Urgency set from the actual scope (one workstation, blocking but not down) and Priority left as
  ServiceNow's read-only Impact-times-Urgency calculation rather than picked by hand. Worked it
  through New, In Progress (with a real technical work note), Resolved (with a deliberately chosen
  resolution code, "Solution provided," over the default "Resolved by request," since a cause was
  found and fixed, not just handled), and Closed. Built and saved a filtered, priority-sorted view
  of active incidents.
- **Request fulfillment, the full chain:** ordered a laptop through the service catalog and traced
  how one order becomes three linked records, a Request, a Requested Item, and two sequential
  Catalog Tasks (procure, then deploy), with two-layer approval. Diagnosed a real bug along the
  way: the "Assigned to" field kept returning empty, traced to the qualifier filtering to
  assignment-group membership rather than a role, not the wrong theory he'd initially assumed,
  fixed by editing the form layout to add the missing Assignment Group field and adding a user to
  an empty group.
- **A catalog item and workflow built from nothing, not the demo content:** designed a VPN Access
  Request catalog item with three form variables, one of them (managed laptop vs. personal device)
  deliberately included because it changes the actual risk of granting access. Built a 4-step Flow
  Designer workflow behind it (approval gate, conditional branch, fulfillment task, closing step)
  and drove it end to end in all three roles, requester, approver, fulfiller.
- **A real debugging catch, verified by testing, not assumed fixed:** the first run left the
  requested item stuck open after its task closed, because Flow Designer doesn't auto-close parent
  records the way the legacy workflow engine does. Added the missing closing step, then re-ran the
  whole flow on a fresh request to confirm the fix rather than trust it.
- **Honest about a leftover gap rather than hiding it:** documented one cosmetic field (Stage)
  that stayed stale on the closed record because his flow never wrote to it, instead of quietly
  fixing the writeup to look cleaner than the actual result.

---

## Placement

Add to **Projects and Lab Experience** once Uriah confirms the project is far enough along to cite
— present tense is honest (the instance is live and active), but don't frame it as finished.

---

## Ready-to-use bullet options

**Primary:**

> **ServiceNow ITSM Lab (Personal Developer Instance):** Built hands-on ITSM experience in a
> ServiceNow PDI, working an incident through its full lifecycle with a real technical diagnosis,
> fulfilling a service-catalog request through its approval and fulfillment chain, and designing a
> custom catalog item with a Flow Designer approval workflow, debugging and re-verifying a
> workflow defect along the way.

**Tighter (space-constrained):**

> **ServiceNow ITSM Lab:** Hands-on incident and request management in a ServiceNow Personal
> Developer Instance, including a custom catalog item wired to a self-built Flow Designer
> approval-and-fulfillment workflow.

**Process-forward (for postings that weight ITIL/service-management process over the tool):**

> **ServiceNow ITSM Lab:** Worked a full incident lifecycle and a multi-record service-request
> fulfillment chain (request, requested item, sequential fulfillment tasks) in ServiceNow,
> designing and debugging an automated approval workflow behind a self-built catalog item.

---

## Name options

ServiceNow ITSM Lab · ServiceNow PDI Build · ITSM Platform Lab (ServiceNow).

---

## Interview talking points (review the repo's README.md and WALKTHROUGH.md before the interview)

- **Priority is calculated, not picked:** ServiceNow derives Priority from an Impact-times-Urgency
  matrix rather than letting an agent set it directly, and he set the two real inputs (scope and
  business impact) and let the field derive itself, matching how the field is actually meant to
  work.
- **The "Assigned to" picker bug:** an empty picker on a catalog task looked like a permissions
  problem at first. It turned out to be an empty assignment group, since the field's qualifier
  filters to group membership, not role. Good example of testing an assumption instead of trusting
  the first plausible explanation.
- **Why the flow didn't close on its own:** the legacy workflow engine closes parent records as a
  built-in side effect. Flow Designer does only what you explicitly tell it to, so leaving out a
  closing step left a requested item stuck open even after its task finished. Fixed and
  re-verified with a second run, not just asserted fixed.
- **The approval-gate design:** the "Ask For Approval" step in Flow Designer resumes the flow
  either way, approved or rejected, so the conditional branch afterward is what actually prevents a
  rejected request from getting a fulfillment task anyway. Deliberate design reasoning, worth being
  able to explain if asked why the flow is shaped the way it is.
- **Honest about what's built and what isn't:** if a panel asks how deep the ServiceNow experience
  goes, the honest answer is incident and request management plus one custom workflow, real and
  hands-on, with knowledge base, RBAC, and CMDB still ahead. That's a specific, defensible answer,
  not a vague "some ServiceNow experience" claim.

---

## Tailoring per posting

- **Help desk / service desk roles naming ServiceNow directly:** lead with the incident lifecycle
  and the request-fulfillment chain, since those map straight to a help desk agent's daily work.
- **Roles that weight process/ITIL over the specific tool:** lead with the multi-record
  request-fulfillment chain and the approval-workflow design as evidence of understanding service
  management structure, not just clicking through one platform.
- **Roles where ServiceNow is a large share of the duty statement:** the honest-fit gap note in
  MEMORIES.md still applies — this lab doesn't cover a heavily ServiceNow-saturated posting on its
  own (no KB, RBAC, CMDB, or reporting yet), so keep applying the existing PASS guidance for those.

> Direction note: this pairs with the GLPI ticketing lab as a second ITSM data point, one built on
> an open-source platform, one on the enterprise tool most CA state postings actually name — worth
> mentioning together when a posting cares about ITSM concepts generally rather than one specific
> tool.
