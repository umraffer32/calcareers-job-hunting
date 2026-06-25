# Interview Prep — JC-522483, Information Technology Associate (California Highway Patrol, Technical Services Group)

Submitted June 24, 2026. Role: junior member of a systems-administration team, under ITS Is/IIs. CHP servers (Windows + Linux/Unix) on physical, virtual, and cloud. In office, Mon–Fri 8:00 a.m.–5:00 p.m., some after-hours and travel, background investigation before hire.

## The honest landscape
This is a defensible stretch — the duties are server systems administration, and your real depth is your homelab plus a cybersecurity internship lab, not production/enterprise tenure. Every claim in the package is true. The gaps are about SCALE and a few specific tools, not honesty. Strategy: lead with what you have genuinely done end to end, and frame the gaps as fast ramp. Never fake a tool.

## The 3 things the panel is most likely to probe

### 1. "Have you done this in production / at enterprise scale?"
The real gap: your server work is one homelab domain and a few Linux servers, plus an internship Cyber Range. No production fleet, no SAN or fabric switches, no enterprise backup platform.
How to answer (straight, then pivot): "My hands-on server work is in my homelab and a cybersecurity internship built on enterprise tooling, Microsoft Azure and Tenable, not a production fleet yet. What I bring is the fundamentals done end to end myself — standing up and running a domain, hardening and patching to baselines, testing failure and recovery — and a track record of ramping fast. The scale changes; the fundamentals carry." Then go to a concrete example (the AD domain build or the 30-to-3 remediation).

### 2. "Did you write that automation / failure test?"
Own the design, be honest about the code. "I designed the failure test — terminating the four instances in every combination and timing each recovery — and I ran it and read the results. I used an AI assistant to generate the script itself, then validated it did what I intended." You can explain what it proves and why: self-managed NAT instances don't self-recover like a managed NAT gateway, so the private route breaks when one is replaced; the self-healing route (EventBridge to Lambda) repairs it automatically. Never claim you hand-wrote code you didn't.

### 3. Named tools you haven't used (gap + adjacent real work + fast ramp)
- VMware (ESXi): "I virtualize on Proxmox for Type 1 and VMware Workstation / Hyper-V for Type 2. I haven't run ESXi, but hosts, datastores, VM lifecycle, and snapshots transfer, and I'd ramp quickly."
- System Center (SCCM/SCOM): "Haven't used System Center. My system and endpoint management has been Tenable, PowerShell, and Defender for Endpoint — same job of inventory, patch, monitor, report, different console."
- SAN / fabric switches: "No hands-on with enterprise SAN or fabric switches yet; my storage work is server-local and Proxmox. I understand the role of shared block storage and would learn the platform."
- SQL Server administration: "I've supported a database at the project level, a Multi-AZ PostgreSQL setup, not deep SQL Server admin. Comfortable with the fundamentals, would ramp on the SQL Server specifics."
- Enterprise backup: "My backup and restore experience is Proxmox VM backups/restores in my homelab plus failover and recovery testing on AWS, not a dedicated enterprise backup product. Would learn the tool."

## Your 3 strongest talking points (steer the conversation here)

1. **Vulnerability management (your best, fully real).** "On an internship Windows Server I ran credentialed Tenable scans, prioritized by risk, remediated with PowerShell, and took it from 30 findings to 3, with every critical cleared by the second scan. I also caught a SQLite finding as a false positive by searching the host instead of forcing a change." Shows the full loop and judgment.

2. **Built and run a Windows domain from scratch.** Windows Server 2022, two domain controllers (DC01/DC02), Active Directory, DNS, DHCP, organizational units, an enforced password policy, DHCP failover, and a DNS replica on the second controller. "It runs end to end like a small production domain, and I administer it day to day." Proves real install/config/maintain plus redundancy.

3. **High availability and security-by-default on AWS.** Self-healing route that repairs the path when a NAT instance is replaced, a Multi-AZ database with tested ~10–13-second write recovery, SSM instead of SSH (no open port 22, no keys), least-privilege roles, and enforced IMDSv2. Shows engineering judgment and a security-first habit.

Plus the credentials: B.S. Network Engineering and Security (WGU) and CompTIA A+, Network+, Security+, Cloud+.

## Fit / logistics notes
- The schedule (8–5, Mon–Fri, in office, some after-hours OT and travel) is a good fit — say so plainly; the earlier-finish and OT are fine by you.
- This is an "under the guidance of ITS Is and IIs" junior role — they expect to train. Lean into genuine eagerness to learn the enterprise stack (System Center, VMware, SAN), not pretend you already have it.
- If salary placement comes up: your WGU bachelor's qualifies you for the Range C minimum ($5,930/mo) on the degree alone.
