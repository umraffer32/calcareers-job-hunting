# rclone-backups (Pickleboy Glacier Backup) — resume/SOQ project brief
DATE: 2026-08-10 | CONFIRMED-BY: Uriah
PROVES: Cloud storage architecture (S3 Glacier Deep Archive tiering), IAM least-privilege design proven with a real smoke test (scoped no-delete policy), backup/DR design (copy-only sync, versioning, restore procedure), verification-driven QA (8-check byte-exact reconciliation across 13,929 objects), cost engineering (multipart chunk-size tuning, full cost model), and a real debugging catch (a config line that silently broke every write, missed by three review passes, found by testing an actual write).
CONSTRAINTS: Personal homelab project, never professional/production framing. Follow the used-not-wrote rule for the shell scripts themselves — they were AI-generated (Claude/Fable directed) from Uriah's decisions, per CLAUDE.md in the repo. The IAM policy design, the six locked architecture decisions, the rclone remote config choices, the verification-check design, and the cost analysis are his own calls and safe to claim as his work; say he "used/built and tested" the scripts, never "wrote" them. The mid-project incident (a runaway `grep` crashing the server twice, corrupting the media drive's mount) originated from an unrelated AI/Claude session process in that directory — real and honestly claimable as troubleshooting/incident response if it comes up, but it's flavor, not core evidence, and never imply he caused it by writing bad code himself. Fresh capture — read in full 2026-08-10 the same day the project finished; unspent in any resume/SOQ/678 so far.
USED-IN: none yet — captured 2026-08-10.
SOURCE: full repo read via `gh api` (private repo `umraffer32/rclone-backups`), README.md + CLAUDE.md + all three scripts + IAM policy, 2026-08-10.
---

# Pickleboy Glacier Backup — Resume/SOQ Project Brief

**Purpose:** source material for citing the rclone-backups project on a resume (Projects and Lab
Experience section), in an SOQ answer, or as interview prep. Read the *Framing note* before
drafting anything.

---

## What the project actually is

A personal homelab project backing up a 5.1TB Jellyfin media library (movies and TV shows,
13,929 files) to Amazon S3 Glacier Deep Archive using `rclone`, built around a scoped IAM user
with no delete permission of any kind. Six architecture decisions were locked before anything was
built: copy-only sync (never mirror, so a local mistake can't propagate outward), a single
pre-verified bucket, a dedicated IAM user over SSO (SSO's 12-hour session cap couldn't reliably
cover a multi-hour initial upload), bucket versioning as a second layer of protection against a
remote-side mistake, and a deliberate call to skip a junk-file exclude list because maintaining
one would cost more than just uploading the junk. The full 5.1TB upload finished 2026-08-10 and
was independently reconciled against S3 the same day. Zero differences.

The IAM security work is the strongest single piece. The policy grants exactly `ListBucket`,
`PutObject`, `GetObject`, `RestoreObject`, and multipart-cleanup actions on one bucket, nothing
more, and there's a 5-check smoke test script (`test-iam-user.sh`) that proves it before rclone
ever touches the bucket for real: list succeeds, put succeeds, read-back succeeds, delete
correctly fails, cleanup only works through a separate admin profile. That's a policy actually
tested against its own boundary, not just written and trusted.

---

## Framing note (read before writing)

The scripts (`pickleboy-backup.sh`, `verify-backup.sh`, `test-iam-user.sh`) were AI-generated
from Uriah's direction inside Claude Code / Fable sessions in that directory — the repo's own
`CLAUDE.md` confirms this. Follow the standing rule: say "used," "built and tested," "designed,"
or "configured," never "wrote" or "coded," for the scripts themselves. What's genuinely his to
claim as authorship: the six architecture decisions, the IAM policy's permission boundary, the
rclone remote config choices (storage class, chunk size, the missing-acl-line fix), the
verification script's check design (what to check and why, not the bash syntax), and the cost
analysis. This is homelab work, not professional/production experience — frame it that way on
every document, same as the AD lab and AWS HA projects.

---

## Verified facts you can cite

- **Scale:** 5,135 GiB (5,513,691,667,814 bytes) across 13,929 objects — 7,363 MOVIES files
  (3,612,780,382,420 bytes) and 6,566 SHOWS files (1,900,911,285,394 bytes).
- **IAM least privilege, proven not just designed:** a custom policy granting only
  `ListBucket`/`PutObject`/`GetObject`/`RestoreObject`/multipart-cleanup on one bucket, no delete
  action anywhere in it, verified with a 5-check smoke test (`test-iam-user.sh`) that confirms
  the denied action actually gets denied before the real backup ever runs.
- **A real bug caught by testing, not review:** an explicit `acl = unset` line in the rclone
  remote config silently broke every write against the bucket's `BucketOwnerEnforced` object
  ownership setting. It survived three review passes because none of them exercised an actual
  write — found only once a real write was tested, fixed by removing the line entirely.
- **Verification, not just an upload log:** an 8-check reconciliation script confirming a
  byte-exact match on all 13,929 objects (`rclone check --one-way --size-only`, 0 differences), a
  full storage-class census across every object rather than a sample (one object outside Deep
  Archive would silently break the cost model), and checks for orphaned multipart uploads and
  bucket-versioning state.
- **Cost engineering with a real number attached:** tuning the multipart chunk size from
  rclone's 5MB default to 64MB cut one-time multipart request fees from about $5.92 to $1.14 on
  the initial upload. Full cost model documented: $5.08/mo steady state, $494 to $585 for a full
  restore if ever needed.
- **Disaster-recovery design, honestly scoped:** a documented restore procedure and a yearly
  access-key rotation procedure (next due 2027-08-09) exist and the `GetObject` permission path
  is genuinely tested (the smoke test's read-back check authorizes the same path). The
  `RestoreObject` permission has only ever been granted, never actually drilled end to end — say
  so honestly if asked; a real restore costs money to test, which is the actual reason, not an
  oversight.

---

## Placement

Add to **Projects and Lab Experience**, matching the existing bold-label bullet format, no dates
on lab items.

---

## Ready-to-use bullet options

**Primary:**

> **Cloud Backup Architecture (AWS S3 Glacier, rclone, IAM):** Designed and built a 5.1TB backup
> pipeline (13,929 files) to S3 Glacier Deep Archive under a scoped IAM policy with no delete
> permission, proven with a 5-check smoke test before use. Caught a config bug that silently
> broke every write, verified the finished backup byte-exact against S3 with an 8-check
> reconciliation script, and tuned upload settings to cut one-time fees by over 80%.

**Tighter (space-constrained):**

> **Cloud Backup Architecture (AWS S3 Glacier, rclone, IAM):** Built a 5.1TB, 13,929-file backup
> to S3 Glacier Deep Archive under a scoped no-delete IAM policy, verified byte-exact against S3
> with an 8-check reconciliation script.

**Security-forward (for IAM/least-privilege-heavy roles):**

> **Least-Privilege Cloud Backup (AWS IAM, S3, rclone):** Designed a scoped IAM policy granting
> only the actions a 5.1TB backup pipeline needed, no delete permission anywhere, and proved the
> boundary with a smoke test confirming denied actions actually get denied before the real system
> ran. Found and fixed a config bug that silently broke every write, invisible to three prior
> review passes.

---

## Name options

Cloud Backup Architecture · Least-Privilege Cloud Backup Pipeline · S3 Glacier Backup System ·
Pickleboy Glacier Backup.

---

## Interview talking points (review the repo's README.md and CLAUDE.md before the interview)

- **The acl=unset bug:** an explicit `acl = unset` line in the rclone config, believed necessary
  against a `BucketOwnerEnforced` bucket, was actually backwards — it broke every write. Three
  review passes missed it because none of them ran a real write. Only testing the actual
  operation surfaced it. Good example of "review isn't testing."
- **Why `--size-only` and never `--download` for verification:** hash comparison against archived
  Deep Archive objects isn't possible without restoring them first, and a `--download` flag on
  the check would trigger exactly that, turning a sub-cent listing operation into a
  multi-hundred-dollar retrieval. `HeadObject`-level metadata (all a size check needs) is free on
  archived objects.
- **Why the storage-class check covers all 13,929 objects, not a sample:** `storage_class` is set
  once in the remote config, so a single object silently landing in Standard tier would blow up
  the cost model (Deep Archive runs about $0.99/TB/mo versus Standard's roughly $23). Worth
  checking exhaustively precisely because it's a set-and-forget setting nobody would notice
  drifting.
- **Why a dedicated IAM user instead of SSO:** the `AdministratorAccess` permission set's session
  cap (12 hours, confirmed via `aws sso-admin describe-permission-set`) was shorter than the
  initial multi-hour upload was likely to take. A scoped, non-expiring static-key user solved
  that without widening the blast radius, since it still has no delete permission and is scoped
  to one bucket.
- **Honest scope on the restore procedure:** the permission path is designed and partially
  tested, not drilled end to end. Restoring from Deep Archive costs a real retrieval fee, so
  testing it live wasn't free. That's a fair, specific answer if a panel probes "have you actually
  restored from this."

---

## Tailoring per posting

- **Security / IAM / cloud roles:** lead with the least-privilege IAM policy and the smoke test
  that proves it, plus the acl-bug catch as a debugging/QA story.
- **Systems / infrastructure / storage roles:** lead with the S3 storage-tier design, the cost
  model, and the chunk-size tuning as concrete cost engineering.
- **Support / general IT roles:** lead with the backup/disaster-recovery design and the
  verification rigor (8-check reconciliation) as evidence of methodical, checklist-driven work.

> Direction note: this pairs with the AD homelab lab and the AWS HA project as a third homelab
> data point on the same theme — Uriah designs a real system, builds in verification rather than
> trusting an upload log, and catches his own mistakes by testing rather than reviewing.
