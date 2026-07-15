# Interview Prep — JC-520957, Server Operations Specialist (ITS I, CUIAB)

Submitted June 10, 2026. Unemployment Insurance Appeals Board, System Engineering Domain. Position 279-319-1402-006. In Office, Sacramento County. Hiring unit contact Albert Hernandez, (916) 263-3551, Albert.Hernandez@cuiab.ca.gov — matches the name on the call, so this checks out. Interview scheduled July 15, 2026 (call received today).

**Posture for the whole interview:** the duty statement is server architecture, install/config/maintenance, monitoring, backup/recovery, and lifecycle management for CUIAB's servers. You've never held a job titled "server administrator," so the honest frame is: real hands-on fundamentals from a self-built AWS high-availability project, an internship doing vulnerability-driven remediation on Windows Server, and a homelab, plus fast ramp on their specific tools and scale. Don't let a panel question about production tenure turn into overclaiming — lead with what you built and tested, be direct about what's lab-scale versus enterprise-scale.

---

## Almost-certain opening question — have this ready cold

Per multiple sources (a former CA state hiring manager's guide, corroborated by the Reddit corpus), panels open with some version of: **"Tell us why you think your training, education, skills, and experience make you the most qualified person for this job."** Have a rehearsed 30-45 second answer, since it sets the tone for the rest of the interview.

**Draft answer:** "I have a B.S. in Network Engineering and Security from WGU, plus four CompTIA certifications, Network+, Security+, Cloud+, and A+. On top of that I have real hands-on experience building and testing server systems. I designed and built a two-availability-zone AWS environment with a self-healing network path and a Multi-AZ database, and proved it works by simulating failures and timing the recovery. In my internship I work with Windows Server and Linux systems, running vulnerability scans and remediating findings with PowerShell, and I've done DISA STIG compliance auditing, taking a system from over a hundred failing controls down to the ten I selected to fix, verified with a re-scan. I also run my own home server environment day to day, so patching and keeping systems healthy is a habit for me, not a one-time task. I haven't held a job with 'server administrator' in the title yet, but the fundamentals here are real, and I pick up new tools and environments fast."

## Panel mechanics (so nothing catches you off guard)

Panel interviews are structured: every candidate gets the same fixed question list, asked round-robin by 2-4 panelists, each scored 0-5 against a key-points checklist and summed. Questions are pulled from the Duty Statement first, then your SOQ, then the Minimum Quals, then Desirable Quals, in that order. Practically: **name the tool, the step, the specific thing** even if it feels obvious, since panelists can only score what you actually say out loud, not what they infer about you.

---

## The 3 landmines they're most likely to probe

### 1. "What production servers have you actually managed?" / "Tell us about your hands-on server administration experience"
You've never administered servers as a paid job duty. Your internship is security-focused (Tenable scanning, PowerShell remediation on Azure-hosted Windows Server VMs), and your server-build experience is the AWS project and your homelab.
- **Honest answer:** "I haven't held a job with 'server administrator' in the title. What I have is hands-on build-and-maintain experience across three places. In my internship I work with Windows Server, Windows 10/11, and Linux endpoints in Microsoft Azure, running scans and remediating findings with PowerShell. I designed and built a two-availability-zone AWS environment with Terraform that runs a Multi-AZ PostgreSQL database and a self-healing route repair for NAT failures, and I tested it by simulating failures and measuring recovery. And I run my own home server environment day to day. The common thread is I understand what a healthy server looks like and how to keep it that way. I'd expect a ramp period on your specific hardware, storage, and tooling, same as any new hire, but the fundamentals are real."
- Don't inflate homelab or AWS scale into "production" or "enterprise." If asked directly whether the AWS environment is live now, say you built and tested it, then it was decommissioned once the project was documented — that's honest and matches the resume framing.

### 2. "Walk us through your backup and recovery strategy experience" (this is a named 25% duty)
Your SOQ talks about backups conceptually ("backups you have actually tested") but you don't have hands-on time with an enterprise backup product (Veeam, Backup Exec, Windows Server Backup at scale, tape/offsite rotation, etc.).
- **Honest answer:** "I haven't run an enterprise backup product day to day. The closest real experience I have is designing for recoverability in the AWS project, a Multi-AZ database and a self-healing network path, and proving it works by actually breaking it and timing the recovery rather than assuming it would work. I think about backup and recovery the same way, the plan is only as good as the last test of it. I don't have hands-on time with whatever backup software you run here, and I'd want to learn your retention policy and restore procedure early."
- Don't name a backup product you haven't used. If pushed for a specific tool, just say you haven't used one professionally yet.

### 3. "How do you approach server lifecycle management and hardware end-of-life planning?" (10% duty)
Your hardware hands-on is homelab-scale (mini PCs, Proxmox), not enterprise rack servers, SANs, or a formal fleet-refresh/asset-tracking process.
- **Honest answer:** "My hardware experience is building and running my own home server environment, so it's smaller scale than an enterprise fleet. What transfers is the discipline, know what you're running, know when it's aging out, and have a replacement plan before it becomes an outage. I don't have experience with formal asset-tracking or inventory systems, so that piece I'd be learning here."
- Do not claim fleet refresh or inventory/asset-tracking experience. It's a genuine gap; say so plainly and move on.

---

## Your 3 strongest talking points (steer toward these)

1. **The AWS high-availability project, with real numbers.** Two AZs, two NAT instances and two private instances, every non-empty termination combination tested (15 scenarios), run three full times (45 scenarios total), about 2:29 average recovery, the route-healer Lambda firing in 0.4 to 0.7 seconds, one run logging 92 events with 15 route repairs and zero false positives. This maps directly to the 45% design/architecture duty and the monitoring/recovery half of the 25% duty. Say "used and tested" for the Lambda and simulation script, not "wrote."

2. **The vulnerability-management remediation cycle: scan, fix, verify, repeat.** Took a Windows Server from about 30 findings to 3 (about 90%), clearing every critical by the second scan. The two beats that show real judgment: the Edge finding that re-flagged after remediation because the browser needed to be closed and reopened, and the SQLite finding you ran down with PowerShell and confirmed as a false positive rather than forcing an unneeded change. This is your Q2 SOQ answer and maps straight to the 25% troubleshoot/root-cause duty.

3. **Compliance auditing and ongoing patch discipline.** The DISA Windows 11 STIG compliance scan in Tenable, remediating 10 failing controls with PowerShell and re-scanning each to PASS, ties to the 5% compliance duty. On top of that, your homelab patching habit, unattended upgrades on Linux plus a custom script you run by hand, aliased to "up," across your servers, Pi-holes, and pfSense firewall, shows patching as a maintained practice, not a one-time project.

---

## Logistics / fit (have ready)
- **List eligibility:** already have it for INFORMATION TECHNOLOGY SPECIALIST I through December 2026 — nothing to do here, don't raise it as a to-do.
- **Location:** In Office, Sacramento County. No telework, no concern.
- **Salary:** $6,513–$10,537/month range; new-to-state hires start at the range minimum.
- **Schedule:** standard daytime, Monday–Friday is your baseline preference; no schedule concerns raised in the posting.
- **HIPAA/compliance line in the duty statement:** you have working knowledge from Security+ and coursework, not hands-on HIPAA administration. If probed directly, say that plainly rather than implying practical HIPAA experience.
- **"May serve in a lead capacity over lower-level staff":** you haven't had a formal leadership role yet. If asked, say so honestly and pivot to documentation and clear communication as the groundwork for that.
- **Why you, honestly:** recent B.S. in Network Engineering and Security, four CompTIA certs, and a track record of building real systems (AWS HA infra, AD homelab, internship remediation work) and proving they hold up under test rather than just standing them up. You're new to a paid server-ops role and you know it; the pitch is real fundamentals plus a demonstrated habit of verifying your own work.
