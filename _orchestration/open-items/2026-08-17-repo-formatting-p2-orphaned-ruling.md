---
id: repo-formatting-p2-orphaned-ruling
title: The repo-formatting P2 adjudication batch awaits Grant's rulings and was tracked on no current surface
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-08-17
source: _orchestration/2026-07-04_p2-adjudication-batch.md
anchor: "Each section is a one-word-per-row (or one-word-per-group) ruling surface."
---

The 2026-07-04 repo-formatting epic completed P1 (four lane reports) and assembled a P2
adjudication batch — one-word-per-row ruling tables covering unmerged-branch dispositions
(three families hold result docs NOT on main: keystone substrate-pump, passive-eigenmode,
boundary-MQJ), the ~106 orphans, the predictions-count accounting, and orchestration-doc
dispositions. P2 is "the only phase that blocks on Grant." P3 (execution) is gated on it.

**The gap:** that owed ruling was recorded only inside the two epic files. No open-item
carried it, so the generated board — the program's only live index — could not show it.
Found by the 2026-08-17 cleanup census. Third instance of the untracked-authorization
class (after the 7th-calibration-role and the date-blanking finds).

**Staleness caveat for the sitting:** the batch was assembled at HEAD `2a7d01dc`
(2026-07-04). Its branch table said 44 unmerged origin branches; origin now has 9 total.
Much of the input has moved — the sitting should start by having the orchestrator re-derive
which P2 rows are still live before Grant spends a word on any of them.

**Discharge:** Grant rules the still-live rows (or retires the batch with a dated note),
P3 executes per rulings, this item closes in that ruling PR.
