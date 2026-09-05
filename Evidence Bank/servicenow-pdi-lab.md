# servicenow-itsm (ServiceNow ITSM PDI Build) — resume/SOQ project brief
DATE: 2026-09-01 | CONFIRMED-BY: Uriah
PROVES: A complete, hands-on ITSM build in a ServiceNow Personal Developer Instance (PDI) covering all nine planned steps — incident management, request management, a self-built catalog item wired to a self-authored Flow Designer workflow, two published knowledge base articles, Role-Based Access Control, a CMDB example, and a reporting dashboard.
CONSTRAINTS: Personal PDI lab, never professional/production ServiceNow tenure — frame every claim that way. Present tense is fine for the project as a whole (the instance is live), but individual pieces of work are past-tense events (he logged, built, resolved, closed). No code-authorship hedge needed for the platform work itself (form fields, list views, Flow Designer, RBAC, CMDB) since it's UI configuration he did firsthand, not AI-generated code. The two knowledge base articles document real fixes from his own homelab (Tailscale subnet routing, SSH key hardening) — see [[tailscale-personal-use]] for the Tailscale side.
USED-IN: none yet — captured 2026-09-01.
SOURCE: full local repo read at `C:\Users\Uriah\Projects\ServiceNow Project` (README.md, BUILD_PLAN.md, WALKTHROUGH.md, CLAUDE.md, both knowledge-base drafts), 2026-09-01. Public at github.com/umraffer32/servicenow-itsm.
---

# ServiceNow ITSM PDI Build — Resume/SOQ Project Brief

**Purpose:** source material for citing the servicenow-itsm project on a resume (Projects and Lab
Experience section), in an SOQ answer, or as interview prep. This project is finished — all nine
planned steps are done. It is no longer a partial gap; it directly answers any posting that names
ServiceNow.

---

## What the project actually is

A complete hands-on ITSM build in a free ServiceNow Personal Developer Instance, closing what had
been the one real tool gap in Uriah's California state IT applications. ServiceNow is the platform
most heavily named in help-desk and service-desk duty statements, and he had zero hands-on time
with it before this project. The PDI request sat on ServiceNow's free-tier waitlist for about a
month before an instance was allocated on 2026-07-09. From there he worked the platform the way an
actual help desk agent would across a full ticket lifecycle: logging and resolving incidents,
fulfilling a service-catalog request through its full approval chain, building a catalog item with
an automated approval-and-fulfillment workflow behind it, publishing knowledge base articles,
setting up users/groups/roles and proving access follows role, tying an incident to a configuration
item and its relationships, and reading the whole queue from a dashboard. He debugged real problems
in nearly every piece, and the writeup keeps every wrong turn in rather than smoothing them out.

---

## Framing note (read before writing)

This is UI-driven platform configuration Uriah did himself in the browser — form fields, list
views, catalog item variables, Flow Designer steps, group and role assignments, CI relationships,
dashboard widgets — so there's no code-authorship hedge needed the way there is for the AWS/rclone
scripts. He built and ran every piece firsthand. The one constraint that still applies: it's a
personal PDI lab, never enterprise/professional tenure. Say "built," "worked," "resolved," "closed,"
not "administered ServiceNow at [a company]."

---

## Verified facts you can cite

- **Incident management, full lifecycle, twice:** logged INC0010003 against a real problem he'd
  already solved (a Linux client not accepting Tailscale's advertised subnet routes), with Impact
  and Urgency set from the actual scope (one workstation, blocking but not down) and Priority left
  as ServiceNow's read-only Impact-times-Urgency calculation rather than picked by hand. Worked it
  through New, In Progress (with a real technical work note), Resolved (with a deliberately chosen
  resolution code, "Solution provided," over the default "Resolved by request," since a cause was
  found and fixed, not just handled), and Closed. A second incident, INC0010012 (an OpenSSH server
  flagged by a vulnerability scan for having password authentication enabled), ran the same full
  lifecycle to Closed in Step 6, this time with a knowledge base article linked and a configuration
  item attached before resolution. Built and saved a filtered, priority-sorted view of active
  incidents.
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
  whole flow on a fresh request to confirm the fix rather than trust it. He deliberately left the
  first broken run (RITM0010002) in its stuck-open state as evidence of the defect instead of
  quietly closing it by hand.
- **Two published knowledge base articles:** wrote up and published KB0010001 (a Tailscale
  subnet-routing fix, matching the same real homelab problem behind INC0010003, see
  [[tailscale-personal-use]]) and KB0010002 (an SSH key-based authentication hardening procedure,
  including generating an ed25519 keypair, copying the public key, and locking down
  `sshd_config`). Both cover fixes he'd genuinely worked out on his own systems first. Along the
  way he added two categories the knowledge base didn't already have (Network and Remote Access,
  Security and Hardening), worked through the block-based article editor and its approval workflow,
  and caught and fixed his own mistake, he'd pasted his own instruction text into a Short
  description field, found it live on the published article, and corrected it through a Checkout
  action rather than leaving it. Linked KB0010002 directly to INC0010012 from the incident form.
- **Role-Based Access Control:** created two users, a fulfiller (Alex Rivera, added to the Network
  group with the itil role) and a requester (Jordan Lee, an ordinary user with no group or elevated
  role). Impersonated each to prove access follows role rather than asserting it: Jordan's incident
  list showed only the one ticket he'd opened, while Alex's list showed that same ticket before an
  assignment group was even set, which ruled out group membership and pointed at itil's broader
  read access instead. Assigned, worked, and resolved that incident as Alex, tying the group back
  to the same Network group used for the catalog-item approval routing rather than a throwaway
  example. Also surfaced a real platform quirk: a second group kept reappearing on Alex's record no
  matter how many times he removed it by hand, consistent with role-based automatic group
  membership rather than anything he'd set directly. He documented the quirk rather than a
  guessed explanation.
- **A CMDB example built on real seeded data, not invented records:** rather than inventing a
  server that corresponds to nothing, found `PS LinuxApp01`, an existing configuration item among
  the instance's roughly 2,800 seeded records, whose name already matched INC0010012's own
  description of a Linux application server. It came with real infrastructure relationships already
  attached (connected by network gear, contained by a set of services, depending on storage
  devices), which satisfied the CMDB relationship requirement with data that was already true. Set
  it as the incident's Configuration item before resolving and closing the ticket.
- **A reporting dashboard reading the live queue:** built a Platform Analytics dashboard,
  "Incident and Request Queue," with a list of active incidents, a list of active requested items,
  and a pie chart breaking the incident queue down by priority, all filtered on the same Active is
  true logic as the saved list view from incident management.
- **Honest about what's still cosmetic rather than hiding it:** documented a Stage field that
  stays stale on a closed flow-driven record because his flow never writes to it, and a dashboard
  widget title field he couldn't get working. Small, named, and left as-is instead of quietly
  fixed to look cleaner than the actual result.

---

## Placement

Add to **Projects and Lab Experience** as a finished project.

---

## Ready-to-use bullet options

**Primary:**

> **ServiceNow ITSM Build (Personal Developer Instance):** Built a complete ITSM slice in a
> ServiceNow PDI end to end, incident and request management, a custom catalog item with a
> self-built Flow Designer approval workflow, published knowledge base articles, role-based access
> control, a CMDB example, and a reporting dashboard, debugging and re-verifying real defects along
> the way.

**Tighter (space-constrained):**

> **ServiceNow ITSM Build:** Hands-on incident management, request fulfillment, a self-built Flow
> Designer approval workflow, knowledge base publishing, RBAC, and a CMDB example in a ServiceNow
> Personal Developer Instance.

**Process-forward (for postings that weight ITIL/service-management process over the tool):**

> **ServiceNow ITSM Build:** Worked full incident and multi-record request-fulfillment lifecycles,
> designed and debugged an automated approval workflow, published knowledge base articles tied to a
> real incident, and set up role-based access control and a configuration-management example in
> ServiceNow.

---

## Name options

ServiceNow ITSM Build · ServiceNow PDI Build · ITSM Platform Build (ServiceNow).

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
- **Reusing a seeded CI instead of inventing one:** the CMDB step didn't add new configuration
  items. He searched the instance's ~2,800 seeded CIs for one that already matched the incident's
  description, and reused its existing infrastructure relationships rather than fabricating data.
  Good example of working with the platform's real data model instead of building a toy example.
- **RBAC quirk he didn't fully chase down:** a group kept reappearing on a user's record after
  manual removal, most likely automatic membership tied to a role in the itil bundle. He documented
  the observed behavior and his best explanation rather than claiming a root cause he hadn't
  actually confirmed. Fine to say plainly at interview that he didn't isolate the exact role.
- **What's genuinely complete now:** if a panel asks how deep the ServiceNow experience goes, the
  honest answer is all of it at PDI-lab depth, incident and request management, a custom workflow,
  knowledge base publishing, RBAC, CMDB, and reporting, with the one honest limit being personal-lab
  scope rather than professional/enterprise tenure.

---

## Tailoring per posting

- **Help desk / service desk roles naming ServiceNow directly:** lead with the incident lifecycle
  and the request-fulfillment chain, since those map straight to a help desk agent's daily work.
- **Roles that weight process/ITIL over the specific tool:** lead with the multi-record
  request-fulfillment chain and the approval-workflow design as evidence of understanding service
  management structure, not just clicking through one platform.
- **Roles naming knowledge management, access control, or CMDB/asset work specifically:** those are
  now real, citable pieces of this project, not gaps to route around. Cite the specific piece that
  matches the duty statement's language.
- **Roles where ServiceNow is a large share of the duty statement:** this project now covers that
  case directly rather than triggering the old PASS guidance for heavy ServiceNow saturation. A
  heavily ServiceNow-saturated posting is a genuine fit signal now, not an automatic pass.

> Direction note: this pairs with the GLPI ticketing lab as a second ITSM data point, one built on
> an open-source platform, one on the enterprise tool most CA state postings actually name — worth
> mentioning together when a posting cares about ITSM concepts generally rather than one specific
> tool.
