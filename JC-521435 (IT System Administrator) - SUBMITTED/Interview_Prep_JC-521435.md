# Interview Prep — JC-521435, IT System Administrator (ITS I, California Highway Patrol)

Submitted June 18, 2026. CAD Support Unit, Communications Infrastructure & Support Section. Position 388-048-1402-002. Panel likely includes a technical lead plus an HR/non-technical scorer.

**Posture for the whole interview:** this is an "apply up" to ITS I and the SOQ is honest about what you have. Do not pretend to experience you lack. Your edge is fundamentals + diagnostic discipline + fast ramp. Lead with what you've actually built and fixed; on gaps, be straight and pivot to how fast you close them. Never claim Intune/SCCM, production-scale AD, Group Policy depth, or CAD experience you don't have — those are exactly what a panel probes.

---

## The 3 landmines they're most likely to probe

### 1. "Describe your experience with Microsoft endpoint management tools" (Intune / SCCM)
This is SOQ Q3, and you have **zero** Intune/SCCM/MDM. Expect them to push on it.
- **Honest answer:** "I haven't worked in Intune or Configuration Manager specifically yet. My endpoint management has been through scanning, scripting, and Defender — I manage Windows 10/11, Windows Server, and Linux endpoints with Tenable for scanning, PowerShell for remediation and configuration, DISA STIG hardening, and Microsoft Defender for Endpoint for monitoring. I know what a hardened, patched, compliant endpoint should look like and how to keep it that way, which is the work those platforms automate. I'd ramp on Intune or SCCM quickly."
- **Do NOT** let Defender for Endpoint stand in for Intune/SCCM — Defender is EDR/security, not endpoint management. If they ask the difference, say so plainly; it shows you understand the distinction.

### 2. "Tell me about your enterprise Active Directory experience" + Group Policy
SOQ Q2 is a **lab** domain, and **Group Policy is your weakest area**.
- **Honest answer:** "I built and run a Windows Server 2022 domain in my own lab — I promoted two domain controllers myself, run Active Directory, DNS, and DHCP, configured DHCP failover across the two DCs, set up organizational units and users, and enforced a password policy. The fundamentals — identity, name resolution, address management, redundancy — are hands-on for me. The honest gap is scale: my domain is lab-sized, not an enterprise forest. Group Policy is the piece I have the least depth in and the one I'm actively building. I pick this kind of thing up fast."
- Don't oversell GPO. "Solid fundamentals, actively building Group Policy, fast at production scale" is the truthful frame.

### 3. "This role is advanced CAD/MDC support — what's your experience there?"
~55% of the duty statement is CAD, Mobile Digital Computer, and vendor systems-engineering for mission-critical dispatch, plus CLETS/law-enforcement systems. You have **no CAD or law-enforcement-systems experience**.
- **Honest answer:** "I haven't worked on CAD or dispatch systems specifically. What I bring is the layer they run on — server administration, Active Directory, networking, and root-cause troubleshooting — plus a track record of learning specialized environments quickly. I'd lean on the vendor relationships and documentation early and ramp on the CAD-specific pieces fast."
- If CLETS / DOJ / Criminal Justice Information Services comes up: no experience, and you're fine with the background investigation the role requires.

---

## Your 3 strongest talking points (steer toward these)

1. **Root-cause troubleshooting discipline.** The rogue DNS forward-lookup zone (reproduced across machines to localize it to shared infrastructure, then fixed at the DNS layer) and the intermittent DHCP-scope exhaustion (widened the pool for the immediate outage, then shortened the lease to fix the actual cause). Theme: localize before changing anything, fix the cause not the symptom, match the size of the fix to the fault.

2. **You build and test real systems, including for resilience.** The AD domain from scratch with DHCP failover you actually tested by powering a controller off; the AWS high-availability project with self-healing routing and a Multi-AZ database where you ran a failure-and-recovery test plan. Ties directly to the role's backup/disaster-recovery and high-availability duties.

3. **Security administration that maps to the job.** DISA STIG hardening, patching and configuration management, taking a system from ~30 findings to 3 and clearing every critical, Defender monitoring. The duty statement explicitly lists "security patching and security administration" — this is real and on-target.

---

## Logistics / fit (have ready)
- **Schedule:** Monday–Friday, 8:00 a.m.–5:00 p.m. On-call nights/weekends may be required — you're fine with that, treat it as overtime.
- **Location:** In Office, 601 N 7th St, Sacramento. No telework concern.
- **Background investigation:** required and you're fine with it.
- **Why you, honestly:** new-grad B.S. in Network Engineering and Security, four CompTIA certs, and a homelab/internship that's genuinely hands-on. You're applying up a level and you know it; the pitch is fundamentals + speed of ramp, not pretended seniority.
