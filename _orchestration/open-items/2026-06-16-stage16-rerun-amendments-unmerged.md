---
id: stage16-rerun-amendments-unmerged
title: A Rule-12 retraction is stranded on an unmerged branch, and main still shows the stale result
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-06-16
source: _orchestration/index.md
anchor: "**MERGE PENDING (Grant):**"
---

Branch `analysis/2026-06-16-stage16-rerun-amendments` (`54fa23cd`) carries the Stage-1.5 (b) Rule-12
retraction + the (c) CONTESTED marker. It is **UNMERGED**, so *"`main` still shows the stale
emergence-negative."*

**★ Why this one is worth more than its size.** The source names it as *"the stale-read root cause
that produced ≥3 near-misses this session"* and states the durable fix directly: *"merging
branch-stranded retractions."* A retraction that never lands is indistinguishable from no
retraction at all to anyone reading main — which is the same failure shape as a withdrawn claim
left standing in a live document.

Needs a pre-merge audit, then Grant merges. Migrated 2026-08-13 from the index.md ledger during the
end-to-end read.
