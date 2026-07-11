# Lab Active Directory domain (homelab, built from scratch)
DATE: 2026-06-18 | CONFIRMED-BY: Uriah
PROVES: Built a Windows Server 2022 AD domain from scratch. DC01 + DC02, two Win11 clients manually joined, Finance/Sales OUs, 16-char complex password policy, DNS forward/reverse zones, DHCP with tested failover, pfSense as recursive resolver. Lab password resets + complexity enforcement verified real (2026-07-11).
CONSTRAINTS: DECOMMISSIONED as of 2026-07-11, PAST TENSE ONLY on all docs. No shares/permissions or group-gated ACL work (group work = creating groups and managing memberships only). GPO still weak, never claim depth.
USED-IN: JC-521435 SOQ; JC-521438 SOQ; JC-521522 SOQ; JC-521544 SOQ; JC-522483 SOQ; JC-522616 SOQ; JC-523478 SOQ; JC-523777 SOQ (Q2 primary). [Signature-term search 2026-07-11.]
SOURCE: moved verbatim from MEMORIES.md (split 2026-07-11)
---

**Lab Active Directory domain (homelab, built from scratch).** Stood up on Windows Server 2022 (eval). Promoted both domain controllers himself, DC01 and DC02. Created two Windows 11 clients and manually joined them to the domain. Built mock Finance and Sales departments (OUs) with one user in each. Set a password policy requiring at least 16 characters, complex (uppercase, lowercase, number, symbol). Runs DNS and DHCP for the domain. Built forward and reverse lookup zones, manually placed his pfSense firewall in them, and DHCP auto-registers clients as they connect. Configured and tested DHCP failover by powering off one DC and watching address assignment carry over to the second. pfSense acts as the recursive DNS resolver that both DCs forward to. This is the authoritative detail behind the [[ad-domain-experience]] summary.

**Addendum 2026-07-11:** domain is decommissioned (see the tense rule in the MEMORIES core); he ran it while building and documenting it and can stand it back up. Password resets and complexity enforcement in this lab are verified real and claimable at lab scope.
