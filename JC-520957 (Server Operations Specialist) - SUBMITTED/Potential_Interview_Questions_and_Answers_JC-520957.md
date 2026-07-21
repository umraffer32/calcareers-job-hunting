# Potential Interview Questions and Potential Answers — JC-520957, Server Operations Specialist (CUIAB)

Interview: Thursday, July 23, 2026, 2:00 p.m. Format confirmed by Uriah 2026-07-16: panel of 15-20 candidates, all asked the same fixed set of 6-7 questions, no individualized follow-ups, each scored against a key-points checklist. This list holds 16 candidate questions, drawn from the duty statement, the submitted SOQ, and general panel-behavior research, so nothing asked on the day is a surprise even though only a subset of these actually gets used.

**Rehearsal priority, set 2026-07-17 with six days left:** given the time remaining, narrowed from spreading evenly across all 16 to a core 9 to actually rehearse out loud, in order of certainty: Q13 and Q14 (the two SOQ prompts, near-certain to be re-asked live), Q3 through Q8 (one question per duty-statement essential-function block actually covered, about 80% of the role's duty weight), and Q1 and Q2 held in reserve as the near-universal opener-or-closer pairing (Cali State Job Coach Kent's research, corroborated independently in the Reddit corpus). Q9 through Q12 and Q15 through Q16 stay in this document as backup, fully or partially drafted, but are no longer the rehearsal priority.

Source doc for panel mechanics, CUIAB background, landmines, and standing personal-history answers: `Interview_Prep_JC-520957.md` in this same folder. This document is the working answer sheet; that one is the reference material.

---

## 1. Tell me about yourself.

"I finished my B.S. in Network Engineering and Security at WGU this past October. Before that I spent a few years in tax prep and customer service, and I went back to school because I wanted a career that kept building instead of resetting every season. Along the way I picked up four CompTIA certs, A+, Network+, Security+, and Cloud+.

Right now I'm interning as a Cybersecurity Analyst with Log(N) Pacific, working remotely in their Cyber Range on real Azure and Tenable infrastructure. Day to day that's Windows Server, Windows 10 and 11, and Linux endpoints, running vulnerability scans and fixing what they find with PowerShell.

Outside of work I run my own home server environment, Proxmox, a pfSense firewall, and I built a full Active Directory domain from the ground up, DNS, DHCP, two domain controllers. I also designed and tested a highly available AWS environment on my own, which is where a lot of my systems-design thinking comes from. Keeping servers patched and healthy isn't a project for me, it's a habit.

I haven't held a job with 'server administrator' in the title yet, but the hands-on foundation is real, and I'm looking for exactly this kind of role to build on it."

---

## 2. Tell us why you think your training, education, skills, and experience make you the most qualified person for this job.

Rehearse as three beats, not a memorized block:
- **Beat 1, credentials:** B.S. in Network Engineering and Security from WGU, plus A+, Network+, Security+, and Cloud+.
- **Beat 2, proof you built and broke things:** the AWS high-availability project, two AZs, self-healing network path, Multi-AZ database, 45 failure simulations across three full runs, about two and a half minutes average recovery, one run logging 92 events with 15 automatic route repairs and zero false positives.
- **Beat 3, proof you close gaps methodically:** vulnerability management internship work, 30 findings down to 3, every critical cleared by scan two, plus a DISA STIG audit that came back 142 failing checks out of 263, where you selected the 10 that mattered most for that environment and verified each one with a re-scan.
- **Close with the CIA triad line**, then the honest line about no server-administrator title yet.
- **If this lands as the LAST question**, add: "That's the case for why I'm the right fit for this role." Skip that line if it's the opener.

Full spoken draft: "Three things back that up. The credentials are the baseline, my B.S. in Network Engineering and Security from WGU, and CompTIA A+, Network+, Security+, and Cloud+ on top of it. Past that, I've actually built and broken systems to prove they hold up, not just stood them up. I designed a two-availability-zone AWS environment with a self-healing network path and a Multi-AZ database, then ran 45 failure simulations across three full test cycles and measured the recovery, about two and a half minutes average, with one run logging 92 events, 15 automatic route repairs, and zero false positives. I've also got a track record of closing gaps methodically instead of guessing. In my internship I took a Windows Server from about 30 vulnerability findings down to 3, clearing every critical by the second scan. I ran a DISA STIG compliance audit that came back with 142 failing checks out of 263, selected the 10 that mattered most for that environment, remediated them with PowerShell, and verified every one with a re-scan to pass. The way I think about all of it comes back to confidentiality, integrity, and availability, everything I do is aimed at keeping a system trustworthy and available, not just running. I haven't had a job with 'server administrator' in the title yet, so there's real onboarding ahead on your specific tools and scale, but the discipline of testing instead of assuming, and verifying my own work instead of calling it done, is already there, and I ramp fast."

**Rehearse this follow-up:** "why only 10, why not fix all 142?" Answer: over-remediating everything risks breaking the system, so picking the controls that fit the environment is the actual skill being demonstrated.

### v2 — re-cut for keyword coverage, since this is a scored, non-interactive panel

**What changed and why:** Uriah's read on the format, panelists are scoring against a checklist of what's actually said out loud, not what they can infer, so this near-certain opener-or-closer question is worth optimizing for duty-statement keyword surface, not just credibility. v1 proves depth on two projects well but never uses the words architecture, backup and recovery, monitor, root cause, or documentation, all straight from the 45% and 25% duty blocks. v2 works those words into the same two beats through better verb choice, not new facts, so it doesn't duplicate what Q3, Q5, Q6, and Q7 already own in more depth. Left out on purpose, not forced in: collaborate, SME, HIPAA, lead capacity, and lifecycle, those would each need either a new fact that duplicates another core-7 answer, or a claim he can't back up. Confidentiality, integrity, availability, and compliance were already covered in v1 and stay as-is.

Full spoken draft, v2: "Three things back that up. The credentials are the baseline, my B.S. in Network Engineering and Security from WGU, and CompTIA A+, Network+, Security+, and Cloud+ on top of it.

Past that, I've actually built and broken systems to prove they hold up, not just stood them up. I designed the architecture for a cost-effective, two-availability-zone AWS environment, a self-healing network path and a Multi-AZ database for backup and recovery, and documented the whole thing. Then I ran 45 failure simulations across three full test cycles and measured the recovery, about two and a half minutes average, with one run logging 92 events, 15 automatic route repairs, and zero false positives.

I've also got a track record of closing gaps methodically instead of guessing. In my internship I ran vulnerability scans to monitor for exposure, and took a Windows Server from about 30 findings down to 3 by tracing each one to its root cause, clearing every critical by the second scan. I also ran a DISA STIG compliance audit that came back with 142 failing checks out of 263, selected the 10 that mattered most for that environment, remediated them with PowerShell, and verified every one with a re-scan to pass.

The way I think about all of it comes back to confidentiality, integrity, and availability, everything I do is aimed at keeping a system trustworthy and available, not just running. I haven't had a job with 'server administrator' in the title yet, so there's real onboarding ahead on your specific tools and scale, but the discipline of testing instead of assuming, and verifying my own work instead of calling it done, is already there, and I ramp fast."

Same follow-up rehearsal note applies: "why only 10, why not fix all 142?" Over-remediating everything risks breaking the system, picking the controls that fit the environment is the actual skill being demonstrated.

### v3 — proof-first structure, picked by Uriah as the smoothest read (2026-07-20)

**What changed and why:** same three beats and the same facts as v2, reordered. Opens with the AWS project as the hook instead of leading with the degree and certs, then the vulnerability management and STIG work, then loops back to the WGU degree and CompTIA certs as the baseline underneath both projects, then closes with the same CIA triad line and honest gap. No new facts, no dropped keywords, just a different order. Uriah read v1, v2, and this version side by side on 2026-07-20 and called this one the smoothest flow. This is now the lead version for rehearsal; v1 and v2 stay above for reference.

Full spoken draft, v3: "The clearest proof is a highly available AWS environment I designed and built myself, two availability zones, a self-healing network path, and a Multi-AZ database for backup and recovery. I tested it by actually breaking it, 45 failure simulations across three full runs, about two and a half minutes average recovery, one run logging 92 events with 15 automatic route repairs and zero false positives. That's the habit this role needs, not just standing a system up, but proving it holds when something fails.

I've got the same track record closing gaps on a live system. In my internship I took a Windows Server from about 30 vulnerability findings down to 3, tracing each one to its root cause and clearing every critical by the second scan. I also ran a DISA STIG compliance audit that came back with 142 failing checks out of 263, picked the 10 that actually mattered for that environment, remediated them with PowerShell, and verified every one with a re-scan.

Underneath both of those is my B.S. in Network Engineering and Security from WGU, plus CompTIA A+, Network+, Security+, and Cloud+. The credentials gave me the theory, the projects are where I actually tested it against something real.

Everything I build comes back to confidentiality, integrity, and availability, keeping a system trustworthy and available, not just running. I haven't had a job with 'server administrator' in the title yet, so there's a real ramp ahead on your specific tools and scale, but the habit of verifying my own work instead of calling it done is already built in."

Same follow-up rehearsal note applies: "why only 10, why not fix all 142?" Over-remediating everything risks breaking the system, picking the controls that fit the environment is the actual skill being demonstrated.

---

## 3. Walk us through your experience designing server architecture or recommending a server solution based on business requirements.

Template, not a script, four beats to combine on the fly:
- **Beat 1, your design lens:** open with the CIA triad frame already committed to in the SOQ, confidentiality, integrity, availability, so the panel hears a designer's mindset before any project details.
- **Beat 2, primary evidence — the AWS project:** two availability zones, self-managed NAT instances instead of a managed NAT Gateway (a deliberate cost tradeoff), the self-healing route repair, Multi-AZ database. Strongest material, shows weighing cost against reliability, the "cost-effective solutions" language straight out of the duty statement.
- **Beat 3, secondary evidence — the AD homelab:** briefer mention, DNS, DHCP failover across two domain controllers. Same design instinct, different system. Past tense only, it's decommissioned.
- **Beat 4, the honest bridge:** both were self-directed, requirements set by you, not gathered from stakeholders. Name that plainly, then pivot to what transfers, weighing tradeoffs and designing for a real constraint, ready to apply it against CUIAB's actual requirements. This is the beat that matters most, "consults with stakeholders to identify server requirements" is explicitly in the duty statement and this is the honest answer to it, not a dodge.

One way the four beats combine (an example of the flow, not a script to memorize):

"When I think about designing a server or a system, I start with what I think of as the CIA triad, keep the data confidential, keep it accurate, and keep it available. That's the frame everything else hangs off of.

The clearest example of that is a highly available AWS environment I designed and built myself. I set it up across two availability zones, and instead of paying for a managed NAT Gateway I used self-managed NAT instances, which is cheaper, but it meant I had to engineer the reliability back in myself. So I built a self-healing route repair that fixes the network path automatically when a NAT instance gets replaced, running on top of a Multi-AZ database. That tradeoff, save money but design the reliability back in yourself, is exactly the kind of cost-effective decision this role is asking about.

I've done similar design work outside of AWS too. I built a Windows Server Active Directory domain from scratch, two domain controllers, DNS zones, DHCP failover between them, so the same instinct, plan for a piece failing instead of hoping it doesn't, shows up there as well. That environment isn't running anymore, I documented it and moved on once it did what I needed it to do, but I could stand it back up.

What I'll say plainly is both of those were projects I designed for myself. I set my own requirements, I wasn't gathering them from stakeholders or a business need I didn't define. What transfers is the discipline underneath it, weighing a tradeoff like cost against reliability, and designing for the failure you hope never happens. I'd be applying that same discipline here, against your actual requirements instead of my own, and that's a real difference I'd rather be upfront about than gloss over."

### v2 — fixes the overlap with Q2 (and with Q1's AD mention)

**What changed and why:** v1 restated the same AWS descriptors Q2 already owns (two AZs, self-healing route repair, Multi-AZ database) and the same AD descriptors Q1 already owns (DNS, DHCP, two domain controllers). Since a panel hears all your answers in one sitting, and you can't assume which subset of the 16 actually gets asked or in what order, each answer has to stand alone, no "as I mentioned earlier" cross-references, while still not parroting the same specific facts to make a different point. v2 keeps the same two projects (they're genuinely your strongest evidence and reusing them is expected) but re-cuts which specific facts get said out loud, so each answer teaches the panel something new about the same project instead of repeating a line.

- **Beat 1, same as v1:** open with the CIA triad frame.
- **Beat 2, AWS, re-cut to the cost-tradeoff facet:** managed NAT Gateway versus the cheaper self-managed NAT instances, and the repair that fixes the network path in under a second when an instance gets replaced, a NEW specific (the sub-second timing) not used in Q2's answer. Skip re-stating "two availability zones" and "Multi-AZ database" as a checklist, they're not the point of this answer.
- **Beat 3, AD homelab, re-cut to specific design decisions:** OU structure organized by function, the 16-character password policy, pfSense set as the DNS resolver. All three are verified real and none of them were said in Q1, which only mentioned DNS/DHCP/two domain controllers narratively in passing.
- **Beat 4, same as v1:** the honest bridge, both were self-set requirements, name that plainly, pivot to what transfers.

Flow-through:

"When I think about designing a server or a system, I start with what I think of as the CIA triad, keep the data confidential, keep it accurate, and keep it available. That's the frame everything else hangs off of.

One design decision I'm proud of came out of my AWS project. A managed NAT Gateway is the easy, reliable choice, but it costs more, so I chose the cheaper self-managed NAT instances instead and then had to engineer the reliability back in myself, an automated repair that fixes the network path in under a second when an instance gets replaced. That's the kind of cost-effective tradeoff this role is asking about, not just picking the cheap option, but understanding what you give up and building it back.

I've made similar calls in my home Active Directory domain. I organized it into OUs by function rather than leaving everything flat, enforced a 16-character password policy instead of the shorter default, and set my pfSense firewall as the DNS resolver so name resolution and network policy live in one place instead of being scattered. Small environment, but the same instinct, decide deliberately instead of accepting a default.

What I'll say plainly is both of those were projects I designed for myself. I set my own requirements, I wasn't gathering them from stakeholders or a business need I didn't define. What transfers is the discipline underneath it, weighing a tradeoff like cost against reliability, and designing for the failure you hope never happens. I'd be applying that same discipline here, against your actual requirements instead of my own, and that's a real difference I'd rather be upfront about than gloss over."

---

## 4. Tell us about your hands-on experience installing, maintaining, and testing server upgrades before they go live.

Overlaps with Interview_Prep landmine #1 ("what production servers have you actually managed") for the honest-gap framing. Deliberately does NOT re-list the internship's OS inventory (Windows Server, 10/11, Linux) since Q1 already covered that in full — repeating it here would be the same overlap flagged on Q3.

- **Beat 1, brief anchor, not a repeat of Q1's inventory:** place it in the internship in one line, install a fix, confirm it held, without re-listing the OS inventory again.
- **Beat 2, the verification story, new material:** the Edge remediation that re-flagged after a scan because the browser needed to be closed and reopened before the update applied. The sharpest example of "tested before calling it done," unused elsewhere.
- **Beat 3, home maintenance mechanics, new specifics:** unattended upgrades on Linux, the "up" alias script, documenting fixes so they're repeatable. Q1 only said patching is "a habit" with no mechanism, so this is genuinely new detail.
- **Beat 4, honest bridge:** no "server administrator" title yet, lab and internship scale, not a production fleet, ramp period expected.

Flow-through:

"In my internship, a lot of my day-to-day is exactly this, install a fix, then confirm it actually held before I move on. I learned that the hard way once. I remediated an outdated Edge install, re-scanned, and it flagged again as if nothing had happened. Edge had actually downloaded the update, it just needed to be closed and reopened before it would apply. Once I did that and re-scanned, it came back clean. A fix isn't finished when the installer finishes, it's finished when the re-scan comes back clean, and that's stuck with me since.

At home that discipline is just a daily habit instead of a project. I run unattended upgrades on my Linux boxes, and I also wrote a short script aliased to 'up' that runs update, upgrade, autoremove, and autoclean, so I can patch by hand across my servers, my Pi-holes, and my firewall whenever I want instead of waiting on a schedule. When I fix something, I document what I did so the next time, or the next person, doesn't have to solve it from scratch.

What I'll be upfront about is I haven't had a job with 'server administrator' in the title, so this has been lab and internship scale, not a production fleet. I'd expect a real ramp period on your hardware and your tools, same as anybody new, but the habit of not calling something done until it's verified is already there."

**Correction (2026-07-16):** the earlier draft of this answer hedged to "use" instead of "wrote," over-applying the 2026-06-20 AI-generated-code rule. Uriah confirmed he actually wrote this one himself, sudo apt update, upgrade, autoremove, autoclean, four lines, simple enough not to need AI help. "Wrote" is accurate here and now matches the submitted SOQ's original wording. See the refined rule in MEMORIES.md.

---

## 5. Walk us through how you monitor server performance and what your approach is to backup and recovery, including user authentication and audit controls.

Three sub-duties in one question, monitoring, authentication/audit/access, and backup/recovery, so the answer calls that structure out explicitly rather than picking one and dropping the rest. First use in this document of the KQL brute-force investigation, the one pinned, fully real hands-on Sentinel claim (~100 failed sign-ins, source IP identified).

- **Beat 1, monitoring, new specifics:** the AWS environment's CloudWatch (metrics/alarms) and CloudTrail (audit trail), plus a brief internship mention, Tenable's recurring scans. Neither used elsewhere in this document.
- **Beat 2, authentication and access, new specifics:** the AWS design decision to go SSM-only with no SSH keys, and the Sentinel KQL brute-force investigation. First use of that story in this doc.
- **Beat 3, backup and recovery, the honest gap:** no enterprise backup product experience. Reframe to designing for recoverability and proving it by testing, matching Interview_Prep landmine #2's already-approved wording. Deliberately thin on the AWS mechanism itself, since it's been described in full twice already (Q2, Q3) — a third full retelling would repeat the Q3 mistake.

Flow-through:

"I'll take this in three pieces, since it's really three different duties folded into one question.

For monitoring, I built a highly available AWS environment on my own that ran on CloudWatch for metrics and alarms and CloudTrail for an audit trail of every change. In my internship it's Tenable, recurring vulnerability and compliance scans that tell me what's drifted since the last one.

For authentication and access, I designed that same AWS environment around SSM-only access with no SSH keys at all, so there's no key sitting around to leak. And in Microsoft Sentinel I ran a KQL query that caught a brute-force pattern, about a hundred failed sign-in attempts, and traced it to the source IP, so I've seen firsthand what it looks like when someone's trying to get in the wrong way, not just read about it.

Backup and recovery specifically, I'll be upfront, I haven't run an enterprise backup product day to day. What I have done is design for recoverability and prove it by breaking things on purpose and timing how long recovery actually takes, rather than assuming a plan works because it looks right on paper. I don't have hands-on time with whatever backup software you run here, and I'd want to learn your retention policy and restore procedure early."

---

## 6. Describe how you troubleshoot a server issue and conduct root cause analysis, including when you'd escalate it.

First use in this document of the SQLite false-positive investigation, the WGU rogue DNS zone ticket, and the GLPI lab's escalation tier, all previously unused.

- **Beat 1, root-cause methodology, new material:** the SQLite finding that flapped in and out across scans in the internship's vuln-management project. Instead of remediating on reflex, searched the system with PowerShell for the actual files, found none installed, confirmed false positive. Evidence-based diagnosis, not reflexive action.
- **Beat 2, recognizing scope, new material:** the WGU rogue DNS zone ticket. A user reported one site loading wrong, asked other users to reproduce it, it failed for everyone, ruling out a single machine and pointing at shared infrastructure. Found and removed a rogue forward lookup zone. The honest bridge into "when would you escalate", recognizing when something's bigger than one report.
- **Beat 3, the honest gap:** never had a job with a formal escalation chain, the internship is remote and self-directed, so there's no real "I escalated this to my supervisor" story. Paired immediately with the GLPI lab's actual escalation tier, an SLA rule that auto-flags a ticket and bumps its priority a day before the resolution deadline, proof of understanding the mechanics without claiming the lived experience.
- **Beat 4, closing criterion:** a plain, honest personal rule for when he'd escalate, outside his access or authority, or clearly bigger than one system. Not an invented anecdote, just a defensible standard.

Flow-through:

"Root cause, I'll start with an example from my internship. I had a vulnerability finding that kept flapping, it would show up on one scan, disappear on the next, then come back. Instead of just remediating it because the scanner said to, I searched the system with PowerShell for the actual files the finding was about and found none installed. Combined with it flapping in and out, that told me it was a false positive, not a real exposure, so I documented it as one instead of forcing an unnecessary change. That's the habit, don't act on what the tool says until you've confirmed what's actually true.

Knowing when something's bigger than it looks is the other half of this. In a lab environment at WGU, a user reported one site loading the wrong page. Before I touched anything, I asked a few other people to try it too, and it failed for all of them, which told me it wasn't that one machine, it was shared infrastructure. That pointed me at DNS instead of the endpoint, and I found a rogue forward lookup zone redirecting the domain and removed it. The reproduction step is what told me this wasn't a one-user problem.

Where I'll be honest is I've never had a job with a formal escalation chain to hand something up to, my internship is remote and self-directed, so there's no supervisor I've actually escalated a live issue to. What I do understand is the structure of it. I built a self-hosted ticketing system with an SLA and an escalation tier that automatically flags a ticket and bumps its priority a day before it's due, so I know how escalation is supposed to work mechanically, even without having lived it on the job. My own rule for when I'd escalate is simple, when it's outside what I have the access or authority to fix, or when it's clearly bigger than one system and needs more than standard procedure covers."

---

## 7. How do you approach managing a server's lifecycle, including tracking end-of-life dates and planning replacements?

First use in this document of the UPS detail and the strategic plan's "incremental upgrades over a wholesale rebuild" line. Q15 already touches CUIAB's modernization priority as a motivation example, so this answer pulls a different specific from the same strategic plan instead of restating that sentence.

- **Beat 1, honest scope up front:** hardware experience is homelab scale, mini PCs running Proxmox, not an enterprise rack fleet or a SAN. Say this plainly before anything else, same pattern as the honest bridges in Q3 through Q5.
- **Beat 2, the real discipline, new specific:** at homelab scale every machine's condition is tracked from memory, no tool needed for a handful of servers. The concrete proof is the UPS those servers sit on, a power event becomes a clean shutdown instead of a hard failure or lost data. Unused elsewhere in this document.
- **Beat 3, the gap and the bridge together:** no experience with a formal asset-tracking or inventory system, the kind of tool that tracks age, support status, and replacement dates across a real fleet, name that plainly. Then pivot, the underlying judgment transfers even without the tooling, knowing what's running and not waiting for failure to force a decision applies at 5 machines or 500, and naming that a deliberate process matters more at their scale, twelve field offices, is self-awareness, not a dodge.
- **Beat 4, CUIAB-specific close, new specific:** the 2023-2027 strategic plan's preference for incremental upgrades over a wholesale rebuild is exactly what disciplined lifecycle tracking supports, replacing pieces before they force an emergency.

Flow-through:

"Where I'll start is plainly, my hardware experience is homelab scale, mini PCs running Proxmox, not an enterprise rack of servers or a SAN. I want that upfront before anything else.

What that scale does teach is the discipline underneath lifecycle management, even without a formal tool to enforce it. With a handful of machines I know their condition and their limits from memory, and I don't wait for something to fail before I act on it. A concrete example, my servers sit on a UPS, so a power event doesn't turn into a hard failure or bad data on a drive, it turns into a clean shutdown and nothing lost. That's the same instinct lifecycle planning runs on, plan for the failure before it happens instead of reacting after it.

Where I'll be honest is I don't have experience with a formal asset-tracking or inventory system, the kind of tool that tracks age, support status, and replacement dates across a real fleet. At five machines I don't need one. Across a footprint like yours, twelve field offices, that's exactly where a deliberate process instead of memory starts to matter, and it's a real piece I'd be learning here, not bringing in already built.

What I do bring is the judgment underneath it. I read your 2023-2027 strategic plan, and one thing that stood out was the preference for incremental upgrades over a wholesale rebuild, which is exactly what disciplined lifecycle tracking is for, knowing what's aging out early enough to replace it a piece at a time instead of being forced into an emergency all at once."

### v2 — STAR-labeled, anchored on one real situation instead of general disclaimers

**What changed and why:** v1 had no single situation to anchor it, just an honest-scope caveat, a general description of homelab habits, a gap admission, and a CUIAB close, none of them a real story. Uriah's correction: stay in STAR, situation, task, action, result, from beginning to end, since a string of disclaimers doesn't read well out loud. v2 anchors on the one real end-of-life decision he's actually made, retiring the AWS high-availability environment on purpose once it had proven its design, instead of a general claim about homelab discipline. Flag: this is the fourth answer to lean on the AWS project (Q2's numbers, Q3's design tradeoffs, Q5's monitoring setup, now this retirement decision), each a genuinely different facet, but worth knowing it's carrying a lot of the weight across the answer set.

- **Situation:** the AWS high-availability environment, two AZs, self-healing route repair, Multi-AZ database, had already done its job. Built, tested, the failure simulations proved the design worked.
- **Task:** decide what to do with infrastructure that had served its purpose, keep paying to run it for nothing, or retire it on purpose.
- **Action:** documented the full design and the test results, then tore the environment down instead of leaving it running idle.
- **Result:** zero ongoing cost, and because it's built in Terraform, fully rebuildable from documentation if it's ever needed again, nothing lost by retiring it deliberately instead of by neglect.
- **Honest scope, stated plainly, not dwelled on:** that's retirement at project scale, not hardware aging out of a fleet, and there's no experience with a formal asset-tracking or inventory system that would do this kind of tracking automatically across many machines.
- **Close:** the same judgment, know when something's past active service, decide about it on purpose, keep documentation so nothing is lost, is what the strategic plan calls incremental upgrades over a wholesale rebuild.

Flow-through:

"The clearest real example I have of managing something through its full lifecycle is the AWS high-availability environment I built. I'd already done what I set out to do with it, two availability zones, a self-healing route repair, a Multi-AZ database, and I'd run the failure simulations that proved the design actually worked.

That put me at a decision point. I could leave it running and keep paying for infrastructure that wasn't doing any active work anymore, or retire it on purpose. I documented the full design and the test results, then tore the environment down instead of letting it sit idle.

The result is it cost nothing going forward, and because the whole thing is built in Terraform, I can stand the exact same environment back up any time I actually need it. Nothing was lost by retiring it deliberately instead of just leaving it running out of habit.

I'll be direct that this is retirement at project scale, not hardware aging out of a fleet, and I don't have experience with a formal asset-tracking or inventory system, the kind of tool that would do this kind of tracking automatically across a lot of machines instead of the handful I can hold in my head. That's a real piece I'd be learning here. But the underlying judgment, know when something's past the point of active service, decide about it on purpose instead of by default, and keep enough documentation that nothing is lost, is the same instinct your strategic plan calls incremental upgrades over a wholesale rebuild. I'd be applying that same instinct to your hardware instead of my own cloud infrastructure."

---

## 8. What software or tools have you used for deployment, documentation, and maintenance of systems?

An inventory question, not a story question, so this stays three named categories with one concrete grounding detail each rather than forced S/T/A/R labels. New primary material here: an Ansible automation project (bastion host, NAT instance, dynamic inventory), pulled from its README and confirmed real, not used anywhere else in this document.

- **Beat 1, deployment, new project:** Ansible, from a separate AWS automation project, a bastion host and NAT instance setup managing private EC2 instances through dynamic inventory instead of a hand-maintained IP list. Concrete grounding, a real SSH ProxyJump bug and its root cause. Terraform gets one line as an honest callback, already fully detailed elsewhere in this document.
- **Beat 2, documentation, new specific:** GitHub, with the actual habit named, documenting the problem, the root cause, and the fix, not just the finished result. Different specific from Q4's documentation line, which was about repeatability, not structure.
- **Beat 3, maintenance, brief:** PowerShell and Bash, already fully established, one line each, no re-explaining.
- **Beat 4, honest scope:** no named enterprise deployment tool, nothing like Jenkins or an enterprise CI/CD pipeline.

Flow-through:

"I'll take this by category since it's really three different tools doing three different jobs.

For deployment, the tool I lean on most is Ansible, from a project where I built a bastion host and NAT instance setup in AWS and used Ansible's dynamic inventory to manage private EC2 instances without hand-maintaining a list of IPs. I hit a real bug early on, SSH connections to the private instances kept failing, and it turned out my SSH config only matched named hosts while Ansible was connecting with raw private IPs, so the bastion proxy never actually got used. I fixed it by updating the SSH config to match the private subnet range so it auto-applies the proxy jump every time. I've also used Terraform to deploy infrastructure, a highly available AWS environment across two availability zones.

For documentation, GitHub is where all of it lives, but the habit that matters more than the tool is how I write it. I don't just document what a project does, I document the actual problems I hit, what the root cause turned out to be, and exactly what fixed it, so the reasoning is still there for me or anyone else months later.

For maintenance, that's PowerShell for remediation scripting in my internship, and Bash for patch automation at home.

What I'll be upfront about is I haven't used a named enterprise deployment tool, nothing like Jenkins or an enterprise CI/CD pipeline. What I've used is infrastructure-as-code and automation tools I set up and ran myself, and I'd expect to pick up whatever your deployment pipeline looks like fairly quickly given that background."

---

## 9. Tell us about a time you collaborated with other IT teams or coordinated across domains on a project.

*Not yet drafted. Real soft spot per MEMORIES — no team-coordinated, externally-witnessed story yet. Needs care, not invention.*

---

## 10. This role may act as Subject Matter Expert on projects and take part in joint security or business continuity drills, what's your experience with either?

*Not yet drafted. AWS failure-simulation testing is a legitimate parallel to a BC drill. Acting as an SME advising others is not something he's done yet — say so plainly.*

---

## 11. How do you make sure your work complies with security, privacy, and regulatory requirements like HIPAA?

*Not yet drafted. Honest ground: working knowledge from Security+ and coursework, not hands-on HIPAA administration (already flagged in Interview_Prep's Logistics section).*

---

## 12. This role may serve in a lead capacity over lower-level staff, tell us about your experience leading or mentoring others.

*Not yet drafted. No formal leadership role yet (already flagged in Interview_Prep's Logistics section) — pivot to documentation and clear communication as groundwork.*

---

## 13. Please describe in detail what you believe are server system specialist responsibilities.

*Not yet drafted. This is the SOQ Q1 prompt, reused live. The submitted SOQ answer (CIA triad framing, daily-duties list, aws-ha-infra project) is the source material — see `Uriah_Raffer_SOQ_JC-520957.pdf` in this folder. Answer should track the SOQ closely but not read as recited.*

---

## 14. Describe your experience with patch management and system updates.

*Not yet drafted. This is the SOQ Q2 prompt, reused live. The submitted SOQ answer (Tenable/PowerShell remediation cycle, the SQLite false-positive rundown, the Edge re-scan lesson, the homelab "up" alias) is the source material — see `Uriah_Raffer_SOQ_JC-520957.pdf` in this folder.*

---

## 15. What do you know about CUIAB, and why do you want to work here?

"CUIAB is the appeals board for EDD's unemployment, disability, and paid family leave decisions, so it's a due-process function, not a benefits office, an administrative law judge hears the first appeal, and the Board reviews it if it goes further. I read your 2023-2027 strategic plan, and what stood out was the focus on modernizing legacy infrastructure and moving toward faster, more accessible service, especially after the claim volume the pandemic drove through appeals boards statewide. That's exactly the kind of work the lifecycle-management piece of this role is about, knowing what's aging out before it becomes the thing that threatens reliability for someone waiting on a hearing. That's a mission I want to be behind, not just a paycheck."

---

## 16. Tell us about a time you had to communicate something delicate to a coworker or stakeholder, or handle a difficult one.

The Block Advisors 1098 story (`Evidence Bank/block-advisors-1098.md`): "As a tax preparer, once a client discloses something, I'm legally obligated to act on it, I can't just let it go. An older client mentioned she lived alone in her own home. When I asked whether she rented or owned, she deflected, but I couldn't drop it, so I explained that if she owned the home she'd have gotten a 1098 mortgage interest statement we needed to file accurately. She admitted she owned it and said she'd look for it, but never produced it. She decided she didn't like me over it. I stayed calm and factual, told her it was completely fine to work with another preparer, and handed her off with no hard feelings. The next preparer asked for the same document for the same reason, she accepted it from them, and the return got filed correctly. The part I care about is the outcome being right, not being liked in the moment."

Numbers if asked for scale: about 70 returns that season, roughly $24,000 in filed revenue. Genuine loose end, keep it, don't resolve it for effect: never found out whether she truly couldn't find the 1098, was stalling to spite him, or just wanted a different preparer. The "hate in my heart" line is interview-only color, never lead with it.

---

## Contingency only, not on the likely-asked list

- **The 2020-2022 gap:** "During COVID I traded options independently and did well at it, but I wanted a stable, building career rather than something that swings year to year, so I went back to school for network engineering and security." Don't volunteer dollar figures.
- **Reason for leaving Robert's Retirement:** keep it to one or two sentences, calm and forward-looking, an interpersonal workplace conflict, left professionally, then pivot to what's been built since.
