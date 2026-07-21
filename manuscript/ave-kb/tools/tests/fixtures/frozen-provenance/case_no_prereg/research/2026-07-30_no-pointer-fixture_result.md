# No-pointer fixture — RESULT (Frozen label, no resolvable prereg; must FAIL)

A gating-dated (2026-07-30) result doc that carries a `Frozen:` label but cites
NO machine-readable prereg pointer, references no `research/...prereg....md`
path, and has no naming-convention sibling prereg. The gate must HARD-FAIL it
with the "add a `Prereg-file: <path>` line" message — the missing-pointer rule
that makes a new frozen claim un-checkable impossible to ship silently.

> **Gate — Frozen:** `some criterion ≤ 0.10`
