# RVE-aggregation fixture — RESULT (PR#782 swapped-criterion regression fixture)

Prereg-file: research/2026-07-30_rve-aggregation-fixture_prereg-FROZEN.md

Reconstructs the PR#782 **swapped-criterion-vs-prereg** pattern (dated
2026-07-30 so the gate fires with teeth): the Lamé gate banked on an ABSOLUTE
two-shell agreement `|ext1−ext2| ≤ 0.10` mislabeled as frozen, swapped for the
prereg's actual frozen criterion `|Δ|/mean ≤ 0.25`. The gate must FAIL this
line — and must NOT be fooled by the fact that a DIFFERENT frozen criterion IS
present in the prereg (reconcile against the prereg, not a self-declared echo).

> **Leg 2 (Lamé gate) — Frozen:** `|ext1−ext2| ≤ 0.10`

A control line whose criterion IS byte-present in the prereg (must NOT fire):

> **Leg 2 deliverable — Frozen:** `≤ 0.10`
