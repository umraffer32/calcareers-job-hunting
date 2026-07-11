# Interview Prep — JC-523947, Network Infrastructure Associate (State Compensation Insurance Fund, Network Infrastructure Services)

Submitted July 10, 2026 (CalCareer ID 3866166), 9 days ahead of the 7/19 deadline. Entry-level ITA role on a newly established Operational Technology program, under an IT Manager I. Supports SCIF's non-enterprise networks: Wi-Fi, IoT devices, security cameras, REM wall tablets. Fully telework (must reside in CA), one in-person onboarding trip to Vacaville (SCIF pays), occasional travel and evening work. No SOQ required for this JC (678 + resume only).

## The honest landscape
This is a genuinely strong fit on paper, closer than most of your applications. The two real gaps are ones you already flagged yourselves while building it: no desktop/mobile device support story, and no real IT-job escalation story, because the internship is your first IT job and hasn't produced one yet. Everything else in the package is true. Strategy: lead with the WGU trouble tickets and the home network hardware work (the two closest real matches to the 40% Tier 2/3 duty), and be straightforward about the escalation gap rather than stretching the internship to cover it.

## The 3 things the panel is most likely to probe

### 1. "Tell us about a time you escalated an issue to a supervisor or senior staff."
The real gap: you haven't had a live IT job yet, so there's no lived escalation story to draw on. The internship is remote and self-directed.
How to answer (straight, then pivot to what you do understand about escalation): "I haven't been in a role yet with a formal escalation chain to draw a real story from, my internship experience is remote and self-directed. What I can point to is how I recognize when something is bigger than a routine fix. On a WGU lab ticket, one user's DNS issue turned out to be a network-wide forward-lookup-zone problem once I traced it, and that's the kind of signal that in a live job would tell me to loop in senior staff rather than keep patching around it myself. I've also designed SLA-based escalation tiers in a ticketing system I built and run myself, so I understand the mechanics, not just the instinct." Do not claim a real escalation event you have not had.

### 2. "Have you supported desktop or mobile devices directly?"
The real gap: no formal desktop-support job. Your device-level troubleshooting is the internship (Windows 10/11, Windows Server, and Linux endpoints) and the WGU labs, not a literal desktop-support ticket queue.
How to answer: "Not in a dedicated desktop-support role. My device-level work has been endpoint troubleshooting in my internship, Windows and Linux systems, plus the WGU labs. It's not a ticket queue with a phone in hand, but it's the same kind of hands-on configuration and troubleshooting work." Do not claim direct end-user desktop or mobile-device support experience you have not had.

### 3. Named tools and device types you haven't used
- **SCIF's incident/ticketing platform** (the posting references "ESP incident and requests" without defining it, so don't guess what it stands for in the room): "I've used ITSM ticketing I built and configured myself, GLPI, with SLA rules and category-based routing, not your specific platform. I'd expect to ramp quickly since the ticket lifecycle and SLA logic are the same idea."
- **IoT devices, security cameras, REM wall tablets specifically:** "I haven't worked hands-on with those exact device types. My network-equipment experience is homelab and residential scale, a Wi-Fi dead-zone fix and a wired backhaul install, plus WGU coursework that covered IoT and wireless networking. I'd expect the fundamentals to transfer and the device-specific parts to be a fast ramp." Do not claim hands-on IoT/camera/REM tablet experience.
- **Enterprise-scale network hardware** (routers, switches, Wi-Fi infrastructure at production scale): be upfront this is homelab and coursework depth, not enterprise tenure. Same honest-gap, fast-ramp framing as the other two.

## Your 3 strongest talking points (steer the conversation here)

1. **The WGU Tier 2/3 trouble tickets — your closest literal match to the job's biggest duty (40%).** A DNS forward-lookup-zone issue traced from one user's report to a network-wide root cause, DHCP scope exhaustion, a routing fault on an EXOS switch, and a static IP misconfiguration on a NIC. "These were simulated tickets, but the diagnostic process, isolate scope, trace with the right tool, fix at the right layer, verify it holds, is the same process this job wants for routine connectivity and configuration issues."

2. **Real, hands-on home network hardware work.** A Wi-Fi dead-zone fix (diagnosed router placement, relocated it, dropped from 5GHz to a non-overlapping 2.4GHz channel to fix range on a 50 Mbps plan) and a wired backhaul upgrade on a two-unit Eero mesh (ran a 150-foot Cat 6 line, installed a switch, fixed an unreliable wireless backhaul dropping connections upstairs). Be upfront these are residential, not enterprise, but they're genuinely hands-on physical network work, not just lab simulation.

3. **The monitor-triage-remediate-document loop from the internship, plus a self-built ticketing lab that proves you understand SLA and escalation mechanics.** Sentinel and Defender for Endpoint alert triage, Tenable scans triaged by severity and remediated with PowerShell (30 findings down to 3, every critical cleared by the second scan), STIG hardening across 10 controls, documentation written for both technical and non-technical readers. Separately, you built and run a GLPI ticketing server yourself: an SLA (4-hour response, 2-day resolution) with an escalation tier that fires a day before the deadline and auto-bumps priority, plus a verified auto-routing rule. Different subject matter than Wi-Fi/IoT, but it's the exact "monitor alerts, triage, take corrective action, document" pattern this job describes, plus a self-taught project nobody assigned you.

Plus the credentials: B.S. Network Engineering and Security (WGU), with coursework specifically in IoT, wireless networking, and network automation, and CompTIA A+, Network+, Security+, Cloud+.

## Fit / logistics notes
- Fully telework, must reside in CA upon appointment. Elk Grove qualifies. One in-person onboarding trip to Vacaville is required; SCIF pays the expenses.
- Occasional travel (plane, bus, van, taxi, or car; overnight to five days) and occasional evening work. Nothing to prep an answer for, just be aware going in.
- This is explicitly an entry-level, closely supervised role ("routine to moderately complex," "under the direction of senior staff," complex issues escalate up). The required-abilities list even calls out learning "without coordinated or organized training," so leaning into your self-directed pattern (the GLPI build, the Python scraper that reverse-engineered an undocumented ASP.NET WebForms flow, earning the CA Life-Only license on your own initiative when the job didn't require it) is on-message, not a stretch.
- New-to-state hires start at the range minimum, $4,935/mo.
- Twin posting JC-523937 (Sacramento, same duty statement, SOQ required) is still open if you want a second shot at this exact team.
