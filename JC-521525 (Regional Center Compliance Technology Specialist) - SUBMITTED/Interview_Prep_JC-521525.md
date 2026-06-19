# Interview Prep — JC-521525, Regional Center Compliance Technology Specialist (ITS I, Dept. of Developmental Services)

Submitted June 18, 2026. Risk and Compliance Unit, Information Security Branch. Hybrid, Sacramento. Position 472-508-1402-009. This was a defensible STRETCH in the same GRC/compliance lane as the submitted JC-521660. Below are the things a panel is most likely to probe and how to handle each honestly.

## The 3 things they will most likely probe

### 1. "Walk us through your experience with NIST CSF, HIPAA, and security control maturity." (the core gap)
This is the role's center and the honest gap. You have NO hands-on NIST CSF maturity assessment, HIPAA Security Rule audit, or Zero Trust implementation.
- **How to answer:** Lead with what's real. "My hands-on control-assessment work is auditing system configurations against the DISA STIG baseline. I ran a Windows 11 STIG compliance scan in Tenable Nessus, worked through 10 failing controls, remediated each with PowerShell, and re-scanned to verify it passed. That's the same discipline a framework audit uses — read the control, compare the system, document where it's compliant or not, remediate, verify." Then the knowledge piece: "I know how the NIST Cybersecurity Framework organizes controls into functions like Identify, Protect, and Detect, and how a maturity assessment rates how fully a control is implemented, from my degree and Security+. I haven't run a CSF or HIPAA assessment hands-on yet, but the mechanics map directly onto what I've done, and I ramp fast."
- **Do NOT** claim CSF/HIPAA/Zero Trust hands-on experience. Honesty plus fast-ramp beats a bluff you can't survive.

### 2. "Your experience is light — one short internship. Why are you ready for this?" (applying up)
Real and unfixable in the moment. Don't apologize for it.
- **How to answer:** Anchor on the concrete, quantified work and the differentiator. "In my internship I audited 10 STIG controls to passing, ran a remediation cycle that cut findings from about 30 to 3 across six scans with all criticals cleared, and I automate this work with PowerShell and Bash. I have the degree and four CompTIA certs including Security+. The scripting and automation side, which this role uses for compliance tracking and dashboards, is something a lot of compliance candidates can't do, and I already do it."
- Frame trainability as a strength, not a deficit.

### 3. "This role trains the 21 regional centers and presents findings to stakeholders. What's your experience there?"
Honest gap — your internship was remote and largely solo, so limited formal presenting.
- **How to answer:** Pivot to real adjacent strengths. "I document my work so a reviewer can follow and reproduce it — when I remediated an exposed service I recorded the query, the reasoning, and the result so it could be verified by someone else. At Block Advisors I explained complex tax details to clients who weren't technical. I'm comfortable translating technical findings into plain language, and I'd grow into formal training and stakeholder briefings." Don't claim you've run trainings.

## Your 3 strongest talking points (lead with these)
1. **The STIG compliance project** — concrete control auditing against a real published baseline (DISA Win11 STIG v2r6, 10 controls, PowerShell fixes, re-scan to verify). This is your most on-point evidence for the assess-controls duty.
2. **Automation and visualization** — PowerShell and Bash to apply fixes consistently, plus the Microsoft Sentinel dashboard mapping successful and failed logins by geography. Maps straight to the role's compliance-tracking automation and dashboard duties, and most compliance applicants can't do it.
3. **Evidence validation discipline** — the SQLite false positive you ran down by searching the system for binaries and DLLs before dismissing it. Shows you don't take scanner output at face value, which is exactly the rigor audit work needs.

## If asked about the 2020–2022 employment gap
Frame as a deliberate choice: "During COVID I traded options independently and did well, but I wanted a stable, building career rather than year-to-year swings, so I went back to school for network engineering and security." Do not volunteer dollar figures or any setback.

## Honesty guardrails (do not cross at interview)
- Never claim hands-on NIST CSF / HIPAA / Zero Trust / formal audit-program experience.
- The vuln-management and STIG projects are internship work in a Cyber Range built on real enterprise tooling (Microsoft Azure, Tenable), not a personal toy lab — say it that way.
- The 30-to-3 and 10-control numbers are real; don't inflate them.
