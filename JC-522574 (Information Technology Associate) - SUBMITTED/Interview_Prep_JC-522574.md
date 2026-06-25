# Interview Prep — JC-522574, Cybersecurity Analyst (ITA), State Treasurer's Office

Submitted June 25, 2026. Hybrid, Sacramento. Reports to the CISO. Package was resume + STD 678 (no SOQ). Honest read going in: strong on the security-ops core, real gaps on roughly half the duty list. You're competing on the core overlap and potential, not breadth. Lead with what's real, handle the gaps with fast-ramp framing, and never claim a tool you haven't used.

---

## The likely probes (real gaps — prepare these)

These are the named duties with no honest backing in your experience. A panel that read the duty statement will likely poke at least one.

**1. Internal penetration testing.**
The duty statement lists "conduct internal penetration tests." You do vulnerability *assessment* (Tenable Nessus scanning, prioritization, remediation), which is not penetration testing. Do not claim pen testing.
- Honest answer: "I haven't run formal penetration tests. My hands-on work is on the vulnerability-management side — authenticated Nessus scans, ranking findings by risk, remediating, and re-scanning to confirm the fix. I understand the difference between assessment and exploitation, and I'd ramp on the pen-testing toolset quickly, but I want to be straight that the offensive testing is something I'd be learning on the job."

**2. Security awareness programs / phishing simulations / building training.**
Whole sub-block of the 30%. You have none of this.
- Honest answer: own it plainly. "I haven't built or run an awareness program or phishing campaigns. What I can bring is the technical side that feeds one — I can explain a threat in plain language to non-technical people, which I did when I reported remediation priorities to both technical and non-technical readers in the internship." Don't manufacture experience here.

**3. Asset decommissioning (NIST SP 800-88 sanitization, MDM removal).**
The full 10%. You understand the concepts from homelab hardware, but no enterprise decommissioning, and **MDM is your known Intune/SCCM gap.**
- Honest answer: "I know the lifecycle concepts — sanitization methods, revoking credentials, removing an asset from security tooling — from building and tearing down my own homelab systems. I haven't run an enterprise decommissioning process or worked in an MDM platform, so that's something I'd learn here."

**4. IAM governance — access review / recertification / process improvement.**
Your AD work is *foundational* identity/access (creating users, groups, OUs, password policy), not access-recertification governance.
- Honest answer: "I've administered identity and access directly — users, groups, organizational units, and an enforced password policy on a domain I built. I haven't run formal access reviews or recertification cycles, but I understand why least privilege and periodic review matter, and I apply that thinking — for example scoping my AWS automation to a least-privilege role instead of a broad admin identity."

**5. Microsoft 365 (listed desirable).**
You have no M365 and avoid it. It's only desirable, not required. Do not claim it.
- Honest answer if asked: "I haven't worked in the Microsoft 365 admin side. My Microsoft security experience is Defender for Endpoint and Sentinel on the security-operations side, plus Azure."

**6. Experience depth / "have you done this in production?"**
One ~4-month internship on a cyber range, plus homelab and AWS projects. All real, none production-tenure.
- Honest answer: frame the cyber range honestly — "a cyber range built on enterprise infrastructure and tooling, Microsoft Azure and Tenable," real work in a training environment, not production tenure. Lead with the concrete results, not the setting.

---

## Lead with these (strongest, fully defensible)

**1. Vulnerability management, 30 → 3.** Authenticated Tenable Nessus scans on a Windows Server, remediated one finding at a time with PowerShell (SMB signing, RDP NLA, LAN Manager auth, outdated software), re-scanned after each — total findings 30 down to 3 (~90%), every critical cleared by the second scan. Also ran down a SQLite finding as a false positive by searching the host for the binaries. This is your best proof for "drive remediation" and "validate the evidence."

**2. Endpoint monitoring + the one real investigation.** Monitored endpoints with Microsoft Defender for Endpoint (EDR), tracking logon failures and unusual activity. The concrete incident: in Microsoft Sentinel you ran a KQL query against failed sign-on events, confirmed a brute-force pattern (~100 failed logins), and identified the attacker's source IP. **Keep this scoped to exactly that** — it's your one real hands-on hunt; don't inflate it into broader hunting.

**3. Scripting / automation (your standout — and a named desirable).** PowerShell and Bash for repeatable remediation; Python across projects. The differentiator: the **Threat-Hunt Automation Framework** — a guardrailed toolkit you built that automates Sentinel KQL hunt workflows (MCP query server wired to the platform API, state reconciliation, idempotent submission, a self-improving postmortem engine). **Talk about it as engineering** — you built the harness; the AI agent does the investigating inside it. Your talking points are the architecture and guardrail decisions, all yours. Never say you "performed the hunts."

**4. AWS security-by-default.** Hardened your lab's access model: replaced standing SSH with Session Manager, scoped automation to a least-privilege role on temporary credentials (you can explain you only scoped the automation role, the daily user still carries admin), enforced IMDSv2 (and you can explain *why* IMDSv1 is exploitable — the SSRF/credential-theft path, Capital One class — method+header is what SSRF can't fake), encrypted RDS at rest, centralized audit logging with CloudTrail.

**5. Configuration hardening / DISA STIG.** Ran a DISA Windows 11 STIG scan in Tenable, remediated 10 failing controls with PowerShell (WDigest, 14-char passwords, Kerberos DES/RC4 removal, script-block logging, Remote SAM restriction, audit process creation), verified each back to PASS.

---

## Framing reminders

- "Used / built and tested / configured / designed" for tooling you directed — never "wrote" or "coded" AI-generated scripts.
- The threat-hunt project is **automation engineering**, not "I'm a threat hunter."
- Gap-handling template: name the real adjacent work, then claim *learnability and fast ramp* — not fictional experience. Honesty is not making false claims; it does not require volunteering every weakness unprompted, but when directly asked about a tool you lack, say so cleanly and pivot to the adjacent real work.
- Strengths to keep returning to: you build reliable tooling to automate tedious security work, you remediate vulnerabilities to closure and verify the fix, and you keep security a default in whatever you build.
