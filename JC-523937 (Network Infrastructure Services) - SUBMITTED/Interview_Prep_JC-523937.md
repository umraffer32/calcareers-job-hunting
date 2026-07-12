# Interview Prep — JC-523937, Network Infrastructure Services (State Compensation Insurance Fund, Sacramento)

Submitted July 11, 2026, 8 days ahead of the 7/19 deadline. Twin posting of JC-523947 (Solano, submitted 7/10) — identical duty statement, so if both convert, expect the same panel material; this one ALSO has an SOQ on file, which 523947 did not. Entry-level ITA on the new Operational Technology program under an IT Manager I, supporting non-enterprise networks (Wi-Fi, IoT devices, security cameras, REM wall tablets). Sacramento County posting, telework, in-person onboarding at Vacaville (SCIF pays).

## Keep the package stories straight (this app has three documents)
- **SOQ Q1:** internship ramp through self-paced classroom tracks + the KQL brute-force investigation (within first few weeks — TRUE, confirmed); Eero wired-backhaul conversion (150 ft Cat 6, switch); homelab (Proxmox, pfSense, Pi-hole).
- **SOQ Q2:** remote delivery (internship, Tailscale/RustDesk, write-ups), phone (Robert's), in-person (Block Advisors; FRIEND'S condo Wi-Fi dead-zone fix with the 5 GHz to 2.4 GHz call; neighbor hardware upgrade).
- **Resume:** owns the internship numbers (10 STIG controls, 30 to 3 / 90%, ~100 failed logins) and the Block Advisors numbers (~70 returns, ~$24k). The SOQ owns the Wi-Fi numbers (150 ft, 50 Mbps, 2.4/5 GHz).
- **Condo story detail:** it was a FRIEND'S condo — Uriah got fed up with the bad Wi-Fi and fixed it himself. Interview color available: he verified the fix with signal-strength readings in the negative dBm range (roughly -30s to -40s dBm — excellent signal), not just bars. The resume bullet says "a friend's condo" on this app; the 523947 resume labeled it "Home Wi-Fi" — if a panel has both packages, the honest answer is the same event, friend's place.
- **Training-program framing:** the SOQ says he ramped "through the program's self-paced classroom tracks and hands-on labs." TRUE — the Cyber Range onboards via per-discipline classrooms (Cyber Theory, Defense/IR with Sentinel, Vulnerability Management with Tenable labs). Do NOT drift into "taught myself everything" in the room; the honest strength is self-paced structured learning applied immediately, without an instructor standing over him.

## The 3 things the panel is most likely to probe

### 1. "Tell us about a time you escalated an issue to a supervisor or senior staff."
The real gap: no live IT job with a formal escalation chain yet; the internship is remote and self-directed. Answer straight, then pivot to what he does understand: "I haven't been in a role yet with a formal escalation chain to draw a real story from. What I can point to is recognizing when something is bigger than a routine fix — on a WGU lab ticket, one user's DNS issue turned out to be a network-wide forward-lookup-zone problem once I traced it. That's the signal that in a live job means loop in senior staff rather than patch around it. I've also designed SLA-based escalation tiers in a GLPI ticketing system I built myself, so I understand the mechanics." Never invent an escalation event.

### 2. "Have you supported desktop or mobile devices directly?"
The real gap: no dedicated desktop-support role. Honest answer: device-level troubleshooting in the internship (Windows 10/11, Windows Server, Linux endpoints) plus the WGU labs — same hands-on configuration and troubleshooting work, not a ticket queue with a phone in hand. Never claim a support-queue job he hasn't had.

### 3. Named tools and device types he hasn't used
- **ESP incident/ticketing platform** (posting names it, undefined — don't guess the acronym in the room): "I've run ITSM ticketing I built and configured myself, GLPI, with SLA rules and category-based routing. The ticket lifecycle and SLA logic are the same idea; the specific platform is a fast ramp."
- **IoT devices, security cameras, REM wall tablets:** no hands-on with those device types. Real adjacents: the two residential Wi-Fi/network projects, WGU coursework in IoT and wireless networking. Fundamentals transfer; the device-specific parts are the ramp.
- **Enterprise-scale network hardware:** homelab and residential depth, not production tenure. Same honest-gap, fast-ramp framing.

## His 3 strongest talking points

1. **The WGU Tier 2/3 trouble tickets** — the closest literal match to the 40% duty: DNS forward-lookup-zone traced from one user's report to a network-wide root cause, DHCP scope exhaustion, an EXOS switch routing fault, a static IP misconfiguration. Same diagnostic loop the job wants: isolate scope, trace with the right tool, fix at the right layer, verify.
2. **Real hands-on network work with measured outcomes** — the friend's-condo RF fix (placement, band, channel, verified in dBm) and the Eero wired-backhaul conversion (150 ft Cat 6 through the wall, switch on the run). Residential scale, and say so — but it's genuinely physical network work with judgment calls (wired beats wireless backhaul; 2.4 GHz fits a 50 Mbps plan) that most entry candidates can't show.
3. **The monitor-triage-remediate-document loop** — Sentinel/Defender alert triage, Tenable scans remediated with PowerShell (30 findings to 3, criticals cleared by scan 2), STIG hardening, documentation for technical and non-technical readers, plus the self-built GLPI lab proving he understands SLA and escalation mechanics. Exactly the "monitor alerts, initial triage, corrective action, document" pattern in the duty statement.

Credentials backdrop: B.S. Network Engineering and Security (WGU) with coursework in IoT, wireless networking, and network automation; CompTIA A+, Network+, Security+, Cloud+.

## Logistics notes
- Telework; must reside in CA. In-person onboarding trip to Vacaville, SCIF pays. Occasional travel (up to five days) and occasional evening work — fine per his schedule preferences.
- Entry-level framing throughout the duty statement ("routine to moderately complex," "under supervision") — the self-directed pattern (GLPI build, the CalCareers scraper, the Life-Only license) is on-message.
- **Availability window:** interview invites typically land 3 to 6 weeks after final filing (7/19), which puts them mid-August to early September — but slips easily into his Philippines trip (Sep 23 to Oct 29, ~15 hrs ahead). Teams/Zoom panels are possible from abroad (Pacific morning = late night PH); fixed-window panels may not reschedule. Don't assume everything waits until November.
- New-to-state hires start at the range minimum, $4,935/mo.
