# Interview Prep — JC-522217 (Information Technology Associate, DMV)

_Finalized at submission, June 20, 2026. Submitted SOQ + resume + STD 678. Permanent ITA, DMV HQ Sacramento, hybrid, M-F 8-5. Position 525-710-1401-096._

## Strongest talking points (lead with these)
1. **Access-model hardening story** (also SOQ Q2, but tell it live with energy): caught that automation was running on a broad admin identity with standing SSH, and fixed it on two fronts — eliminated SSH for AWS Systems Manager Session Manager (no open port, no password to brute force, no key to steal) and moved automation onto a dedicated least-privilege role with temporary credentials via AWS Single Sign-On. Separation of duties + least privilege, validated before trusting it. Fully his own reasoning.
2. **IMDSv2 / SSRF depth:** can explain *why* IMDSv1 is exploitable (unauthenticated metadata endpoint serving role credentials, the Capital One SSRF class) and how v2 closes it (session token via PUT + required header, hop limit). Shows security understanding, not just a toggled setting.
3. **Genuine breadth, honestly split:** built and secured a two-availability-zone AWS environment (IAM, security groups, KMS, CloudTrail/CloudWatch, IMDSv2, Terraform) AND real monitoring/detection + support from the internship (Microsoft Sentinel SIEM, Defender for Endpoint, KQL, vuln remediation ~90%, DISA STIG). Covers both the support duties and the AWS-security desirable quals.
4. **SIEM bridge (desirable qual #6 names Sentinel):** his hands-on SIEM is on Azure with Microsoft Sentinel + Defender for Endpoint — say so plainly; it maps directly to their logging/monitoring desirable qual even though the SOQ (AWS-only) couldn't carry it.

## Talking points to volunteer (not in the SOQ, save for the room)

### NAT instance vs. managed NAT Gateway — a cost/availability tradeoff I made
Great answer for "tell me about a tradeoff" or "a time you balanced cost against effort."
- In my AWS lab I ran a **NAT instance** instead of a **managed NAT Gateway**. A Gateway is the production-correct, zero-maintenance option but costs roughly $65/month for two availability zones before data transfer. A `t2.micro` NAT instance is close to free in the Free Tier.
- The catch: a Gateway gives you redundancy and failover for free, with no effort. By choosing the instance, I took on that work myself — bootstrapping, routing, AMI baking, and failover handling.
- So I built the redundancy in-house: an EventBridge + Lambda route healer that repairs the private route table when a NAT instance is replaced (fires in ~0.4–0.7s, zero false positives across testing), plus auto-scaling groups per AZ.
- The honest framing: for a personal lab where I wanted to learn the internals and keep cost near zero, the instance was the right call. **For production I'd use the managed Gateway** — the engineering time isn't worth it when availability is the priority. Knowing *when* each is appropriate is the point.

## Retention / "why this support role given your cloud-security background?" (strong honest answer)
This is the most likely fit probe, because the application sells a cloud/security leaning for a support-heavy ITA. Uriah's honest, strong answer: he intends to stay 2-3+ years, likely longer. The real driver is stability for his family (wife, kids on the way) — he is not a job-hopper and can't afford to be. Frame it as: wants to get his foot in the door, build real experience, and put down roots; the AWS and security depth is a value-add he brings to the team, not a reason he'll get restless and leave. This directly defuses the "will this person bounce in eight months" concern.

## Likely probe areas
- **AWS security depth is all personal lab, not production.** Own it directly: "All of my AWS security work is from my own lab, not a production environment yet." Then pivot to how he'd ramp on a team and what he already understands (IMDSv2/SSRF, least-privilege, separation of duties, SSM-over-SSH, defense in depth).
- **The CloudTrail example is HA testing, not a security incident.** If pressed, be honest that the failover test is where he exercised reading CloudTrail/CloudWatch, and the transferable skill is reconstructing an event timeline from the audit trail — same thing you'd do in an incident.
- **Scripting was AI-assisted.** If asked "did you write the Bash/Python yourself?", answer honestly: he had the idea, directed the implementation, and battle-tested it; he understands how every part works. Don't claim hand-authorship.
- **Hardware experience is personal, not job support.** His hardware hands-on is building his own devices and homelab (server/storage), not supporting end-user hardware at a job. Frame accordingly.
