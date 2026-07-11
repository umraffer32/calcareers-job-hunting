# Interview Prep — JC-523777 System Security Associate (ITA, CalSTRS SSA Unit)

Submitted 7/11/2026. Final filing 7/16/2026, so expect interview contact roughly mid-August to early September if screened in. SOQ was "the first interview," so a panel invite means the written package already scored competitively. Panel will likely include the SSA Manager and possibly a non-technical HR scorer.

**Scheduling note.** Philippines trip Sep 23 to Oct 29. An interview window could slip into it. State panels often do Teams interviews, so ask for remote if contact comes late; Pacific-morning slots are late night PH.

**Process reminders.** Background investigation before appointment (Personal History Statement plus DOJ fingerprinting, in person). Possible Form 700 (economic interest disclosure). Hybrid, West Sacramento HQ, Yolo County.

---

## The three probes to expect, and the honest answers

### 1. "This position administers access to our MAINFRAME. What's your mainframe experience?" (also Entra ID, a named ideal-candidate skill)

Zero exposure to both. Do not bluff a product name.

The honest bridge is that access administration reasoning is platform independent, and I have done that reasoning end to end in two identity systems. In Active Directory I created and managed users, groups, and organizational units, enforced password policy, and handled resets. In AWS IAM I scoped roles to least privilege, separated automation identities from human ones, and moved standing credentials to temporary ones. Whatever the platform, the questions are the same. Who is this identity, what do they actually need, who approved it, and when does it get reviewed or cleaned up. The mainframe piece of this job is assist-level by the duty statement, and I ramp fast on unfamiliar tools. The proof I offer is the annuity coverage week at Robert's Retirement, where I picked up an unfamiliar carrier workflow in days with the partner team's help and kept two workloads moving, and the certification ladder at Block Advisors.

### 2. "Your provisioning experience is labs and a homelab. Have you done this for real users in a real organization?"

Truthfully, no employer tenure doing provisioning, and I say that plainly if asked directly. Then the reframe, which is also true. I built the environments myself, from bare metal to working domain, which means I understand the whole stack underneath an account, not just the ticket steps for one system. Promoted the domain controllers, built the OUs, created the users and groups, set the password policy, joined the clients, ran resets. The AWS work shows the judgment side, since I caught my own overprovisioned automation identity and fixed it the way an enterprise would.

If asked whether those environments are running today, the honest answer is that I ran them while building and documenting them, they're documented on GitHub, and I can stand any of them back up. Don't claim they're currently live.

### 3. "This role assists with backup and recovery, daily media management, file restoration. Walk us through your experience."

Claim ceiling is basic Proxmox VM backup and restore in the homelab, personal scale. Do not stretch into enterprise backup tooling or media management. The honest bridge is the recovery mindset, which I've practiced for real. I configured DHCP failover across two domain controllers and proved it by powering one off. In AWS I built a Multi-AZ database with failover and ran a scripted failure test across every termination combination, forty-five scenarios, and timed every recovery. I test the failure before it happens. Their specific backup stack I'd learn on the job, and the duty statement's verb is assist.

Secondary probe in the same family, ITSM ticket queue tenure (duty 1 opens with monitoring the ITSM system). Honest bridge is the GLPI lab, mechanics not tenure. Built the SLA with response and resolution targets, an escalation rule that fires before deadline, and category-based auto-routing. I know how a queue is supposed to work; I haven't sat in a production one.

---

## Strongest talking points, lead with these when the door opens

1. **The AWS least-privilege story.** Caught my own Terraform automation running under a broad admin identity with long-lived credentials. Scoped a dedicated role to only what it needed, backed by SSO issuing temporary credentials, and separately eliminated standing SSH in favor of Session Manager gated by IAM with CloudTrail auditability. Every beat is mine and defensible. This is the story that shows security judgment, not just tasks.
2. **The AD domain build.** Two domain controllers, DNS, DHCP with tested failover, Finance and Sales OUs, users and groups, sixteen-character password policy, resets. It's their 30% duty block in miniature, built from nothing.
3. **STIG account controls with verification discipline.** Ten failing DISA STIG controls remediated with PowerShell on a Windows 11 system, each verified with a rescan, two of them account and access settings (minimum password length, remote SAM restriction). Maps straight to their Auditing section, and the verify-every-fix habit is what auditors want to hear.

Behavioral rounds. Customer with limited technical experience = Jason hardware story plus Block Advisors (about 70 returns, anxious clients, plain language). Teamwork = the Athene annuity coverage week. Difficult customer = the Block 1098 client, including the graceful hand-off (keep the "hate in my heart" line as spoken color only if it flows naturally).

**Core-competency map (they score against these five).** Communication = Block varied-audiences work and the GitHub documentation habit. Customer/Client Focus = Jason and Block. Teamwork = Athene coverage week. Adaptability = certification ladder, Sophia-to-WGU self-directed degree path. Work Standards/Quality = re-scan verification habit, return-review discipline.

**Do not volunteer anywhere.** The 2020-2022 gap (if asked, deliberate career decision, traded options independently and did well, wanted a stable building career, went back to school; no dollar figures). ServiceNow, Intune/SCCM, M365, imaging, Wireshark-as-tool. That the lab environments are currently decommissioned, unless directly asked (then the honest line above).
