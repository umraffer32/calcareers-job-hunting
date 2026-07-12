# Interview Prep - JC-524404 Security Operations Associate (ITA, DDS)

Submitted 7/12/2026 (28 days ahead of the 8/9 deadline). Hybrid, 1215 O St, Sacramento. Range C, ~$5,930/mo min. 24/7 on-call and weekend support as required (fine for you).

Role weighting: 35% security-ops monitoring/triage (your lane), 35% asset management (your biggest gap), 20% project coordination (assist-level), 5% badge, 5% other. Desirable tools named: Cortex XDR, Microsoft Sentinel, Proofpoint, ServiceNow, Tenable One, AWS.

## Top 3 probes and honest answers

### 1. Asset management (35% of the job, your real gap)
They may ask how you would maintain inventories of hardware, software, and cloud assets that feed security controls. You have no professional asset-tracking or inventory tenure.
- Honest bridge: the GLPI ITSM lab you built has a working asset inventory (a lab, not a job), and Tenable vuln scanning enumerates a host's software and config state, so you understand why accurate asset data drives vulnerability management and event correlation.
- Framing: be upfront that owning an inventory in a role is new ground, then pivot to fast ramp and the fact that you already get WHY asset accuracy matters to security ops.
- Do NOT claim asset-tracking or inventory experience.

### 2. Basic forensic data collection (named in the duty and the SOQ prompt)
The duty is "basic forensic data collection under supervision." You have no forensics tooling or training.
- Honest answer: you have done basic evidence collection, not formal forensics. You documented the source and findings of the brute-force incident (roughly 100 failed sign-ons, the source IP) and ran down a host-level SQLite finding as a false positive by searching the machine. That is evidence-gathering under guidance, which is exactly what "basic, under supervision" means.
- Do NOT overclaim forensics; say you would ramp on proper forensic procedure.

### 3. Alert-triage depth and SOC tool breadth (Cortex XDR, Proofpoint, ServiceNow)
You monitor with Defender and ran ONE real KQL investigation. You have not done extensive incident-by-incident alert triage as a daily practice, and have not used Cortex XDR, Proofpoint, or ServiceNow.
- Lead with what is real: monitoring endpoints in Defender, the KQL brute-force investigation in Sentinel (failed sign-ons, confirmed brute force, identified source IP), Tenable vuln remediation, STIG compliance auditing. The triage concepts (prioritize by risk, confirm a pattern, identify the source, document) are things you have done.
- On the tools you lack: do not bluff. They are desirables, not requirements. Cortex XDR is an EDR like Defender; Sentinel is the SIEM you use; ServiceNow is ticketing, and you built a GLPI ITSM lab that mirrors that workflow. Concepts transfer, the specific consoles are a fast ramp.
- Do NOT claim Cortex XDR, Proofpoint, or ServiceNow hands-on.

## Two more likely pokes
- "You only remediated 10 of 142 STIG controls?" Yes, deliberately. Over-hardening a machine breaks the functions it is supposed to run, so you selected the 10 that fit that system's role. That is judgment, not incomplete work.
- Escalation and working under supervision: the internship is remote, part-time, and self-directed with no formal escalation chain, so you do not have a lived "I escalated X to my lead" story. Honest bridge: recognizing when an issue exceeds routine scope (the WGU rogue-DNS ticket widening from one user to a network-wide root cause) plus the GLPI lab's SLA and escalation-tier design shows you understand the mechanics.

## Strongest cards (lead with these)
1. Real security-ops cycle on enterprise tooling: Sentinel KQL brute-force investigation (roughly 100 failed sign-ons to source IP), Defender monitoring, Tenable 30-to-3 remediation, STIG audit plus PowerShell fixes. Maps straight to the 35% core.
2. Compliance and audit mindset: you audit configs against a STIG baseline, prioritize by risk, and document fixes so they repeat. Maps to the role's risk/compliance and documentation duties.
3. Fast, self-directed ramp: you ramped through the Cyber Range self-paced classrooms one discipline at a time; WGU B.S. Network Engineering and Security plus A+, Network+, Security+, Cloud+, and Linux Essentials. This is the answer to every gap above.

## Logistics and do-not-volunteer
- Availability: Philippines trip Sep 23 to Oct 29, 2026. With an 8/9 deadline, invites (typically 3 to 6 weeks out) could land late Aug to Sept, possibly into the trip. You can do Teams/Zoom from abroad (Pacific morning is PH late night); fingerprinting and onboarding are in person. Offer remote-interview flexibility if scheduling drifts late.
- Schedule: day shift Mon-Fri preferred; weekend, on-call, and OT welcome.
- Do not volunteer the 2020-2022 gap; if asked, brief COVID-era framing, no dollar figures.
- Everything on the 678, SOQ, and resume is scoped to what is real. Lab work is labeled as labs and the numbers are single-machine. Keep it that way in person.
