# Interview Prep — JC-523478, Information Technology Associate (DMV, End User Support 1 Team)

Submitted 7/3/2026. Deadline 7/16/2026. Position 525-710-1401-007, Sacramento HQ, hybrid, M-F 8-5.
Duties: 40% End User Support (tickets to SLAs, hardware/software support, customer satisfaction), 35% System Support (documentation, end-user training, Identity Services, patching), 10% cloud/DevOps/databases, 10% vendor/SOW, 5% other.
Panel context: interview invites typically land 3-6 weeks after final filing (late July to late August 2026). Philippines trip Sep 23 - Oct 29 could collide with later rounds; ask for Teams/Zoom if scheduling drifts that way.

## Likely probes and how to answer

### 1. "Tell us about your help desk / ticket queue experience." (the real gap: no paid desk tenure)
The 40% duty is managing tickets to SLAs, and the honest answer is lab plus adjacent, never a tenure claim.
- Lead with the GLPI lab, and say up front it's self-built practice: self-hosted GLPI, incident and service request workflow, four-category triage with urgency/impact/priority set per ticket, an SLA with a 4-hour response and 2-day resolution target, an escalation rule that fires a day before the resolution deadline and bumps priority, a routing rule that auto-assigns Network tickets to the Network team (verified firing, not assumed).
- Bridge to the real queues he HAS run: ~70 tax returns in a season at Block Advisors, every one against a hard filing deadline, always knowing which was closest to slipping; covering the annuity caseload at Robert's on top of his own for a week.
- Close with fast-ramp: the mechanics (triage, SLA discipline, escalation, documentation) are already habits; learning DMV's specific tool is the easy part.

### 2. "This role facilitates training sessions for end users. What's your training experience?" (real gap: none)
Do not claim training. Honest shape: hasn't run formal training sessions, but does the components daily — explains technical issues in plain language matched to the listener (Block clients, walking lab users through a DNS cache flush), and writes documentation others can follow without him in the room (GitHub project docs, the GLPI knowledge base article he seeded to cut repeat tickets). Comfortable stepping up to structured sessions from there.

### 3. "Experience with databases / performance tuning? Vendor management, SOWs?" (real gaps: both 10% slices)
- Databases: none — do NOT stretch KQL into SQL/DBA; KQL is a log query language he used in Sentinel, and he can say exactly that. Honest answer is "not yet," plus how he ramps (labs first, the same way he built AD, GLPI, and AWS skills).
- Vendor/SOW: no procurement exposure. Nearest real adjacency is coordinating with partner-carrier support teams (Athene/Securian) at Robert's to keep applications moving. Offer that, labeled as adjacency, and note these are the small slices of the duty statement.

### 4. "Identity Services Management?" 
Real footing: administers AD in his own two-DC domain — user accounts, groups, OUs, password policy, DHCP failover. Frame as hands-on AD fundamentals in a lab he built, ready to ramp onto enterprise identity platforms. Do not claim GPO depth or enterprise identity tooling (Entra/Okta etc.).

### 5. Standing personal questions (settled framings — reuse, do not improvise)
- 2020-2022 gap: "During COVID I traded options independently and did well, but I wanted a stable, building career rather than something that swings year to year, so I went back to school for network engineering and security." No dollar figures, no setback talk.
- Robert's "Separated following a workplace conflict": brief and calm; a workplace disagreement, he moved on, no bad-mouthing, pivot to what he learned about professionalism (the Block hand-off story shows the matured version).
- After-hours calls: the working conditions say the incumbent carries a cell phone and responds after hours. His real position: fine with it, treats after-hours work as normal for IT support (and OT-friendly).

## Strongest cards (lead with these when the door opens)

1. **Troubleshooting method with receipts.** Reproduce, isolate, verify before close. The vuln cycle: 30 findings to 3 across six scans, criticals gone by scan two; the Edge fix that only counted after a full close-and-reopen (verification lesson); the SQLite false positive he ran down with PowerShell instead of chasing a ghost; the DHCP scope exhaustion where he fixed the lease-time cause, not just the symptom.
2. **He built a service desk to practice on.** Nobody else in the candidate pool is likely to say that sentence. GLPI specifics above; it converts the tenure gap into an initiative story.
3. **Customer service under friction.** The Block Advisors 1098 client: legal duty to ask, client took it personally, he stayed calm and respectful, handed her off without friction, return finished accurately. (Keep the "hate in my heart" line out unless telling it live adds context; spoken-only per settled call.)
4. **Learning arc.** Degree, then four CompTIA certs, then labs (AD domain, GLPI, AWS HA project) — reading isn't running it, so he runs it. Mirrors the posting's "eagerness to learn new skills."

## What NOT to say (hard honesty lines)
No ServiceNow. No Intune/SCCM/MDM/Endpoint Manager. No Microsoft 365 support. No Wireshark as a tool. No imaging (installs from ISOs, never captured an image). No SQL. No hardware support at the internship (fully remote — hardware hands-on is homelab only). No formal training delivery. No ITIL-based claims beyond the cert existing on the list. Scripts were used/directed/tested, not hand-authored.
