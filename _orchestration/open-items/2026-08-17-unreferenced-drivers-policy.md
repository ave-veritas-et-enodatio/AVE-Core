---
id: unreferenced-drivers-policy
title: 95 of 778 src/scripts drivers are referenced nowhere in the tracked corpus — archive, delete, or reference?
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-08-17
source: _orchestration/2026-08-17_repo-cleanup-epic.md
anchor: "95 unreferenced drivers"
---

A full-corpus stem+basename reference scan (2026-08-17 census, HEAD `36ce03b9`) found 95
of 778 `src/scripts/*.py` drivers whose name appears in **no other tracked text file**:
53 in `vol_1_foundations`, 16 `vol_4_engineering`, 13 `vol_6_periodic_table`, remainder
scattered. `src/ave/` proper is clean — 0 of 179 modules unreferenced.

**Caveats stated by the census:** cross-repo references, commit-message references, and
dynamic invocation were NOT checked; 4 of the 95 were spot-verified by hand. So the list
is a candidate set, not a verdict set.

**The decision (policy, then mechanics):**
1. **Archive** — move to a dated `src/scripts/_archive/` (mirrors `research/_archive/`);
   history keeps everything, the live tree stops advertising dead entry points; or
2. **Delete** — git holds history; heaviest but cleanest; or
3. **Reference** — some may be load-bearing-but-unlinked (run-by-hand instruments); a
   verification lane confirms per-file before any move.

Recommend (3)→(1): one lane verifies the candidate set against cross-repo + git-log
mentions, then a single PR archives the confirmed-dead with a manifest. No deletions
without Grant's word per the standing driver-honesty discipline.
