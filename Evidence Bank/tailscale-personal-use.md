# Tailscale personal use (homelab, ~1.5 years daily)

DATE: 2026-08-26 | CONFIRMED-BY: Uriah (self-written, verbatim in his own "why are you interested in Tailscale" application answer)
PROVES: Real, advanced daily use of Tailscale, not just basic setup. Understands why it works (SSH with no open inbound ports). Uses the subnet router feature to route from his main network into his pfSense lab subnet, working around his Eero router's lack of static-route support, which eliminated the need to remote into an Ubuntu VM just to reach the pfSense web UI. Pairs it with RustDesk over the Tailscale IP for remote desktop. Used every day for about a year and a half.
CONSTRAINTS: Personal homelab use, not professional/enterprise Tailscale administration or deployment at scale. Frame as depth of product use and understanding, not sysadmin-at-scale experience.
USED-IN: Tailscale Customer Support Engineer (Tier 1) application, 2026-08-26 (his own "why are you interested" answer; cover letter references it briefly without repeating the specifics, to avoid duplicating the story across both).
SOURCE: Uriah's own written answer, pasted into chat 2026-08-26.
---

Full text of his answer, for reference:

"I absolutely LOVE Tailscale. When I first heard about it I was a bit skeptical and thought to myself, 'How can they offer something like this for free? How is it possible that a secure SSH connection can be made that requires no open inbound ports, and give that capability away for free?' I then gave it a shot and haven't looked back since. I have it on all my devices. It allows me to securely and quickly access my home-lab from anywhere in the world as long as I have an internet connection. It allows me to share services with people that otherwise would require a complex setup. It makes HTTPS a quick and easy done deal. It allows me to use RustDesk with direct IP using my Tailscale IP address.

One of the cooler things I've done with it is experimenting with the subnet router feature to access a different subnet on my lab. I'm using an Eero router (easy and headache-free), but Eero routers can't set a static route to let traffic from the main network reach the lab network. The subnet router feature solved that. Now he can reach the pfSense firewall in the lab subnet from his main PC directly, instead of remoting into an Ubuntu VM and using the browser on that machine to manage the firewall. Used every single day for about a year and a half."
