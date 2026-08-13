---
id: key-namespace-collision
title: Decision keys are colliding — four distinct things are named "D1"
status: OPEN
owner: unassigned
opened: 2026-08-13
source: _orchestration/2026-07-20_pending-rulings-and-frontier-queue.md:123
---

Four different decisions in this corpus carry the label **D1**:

| sense | anchor |
|---|---|
| srs-vs-diamond — the lattice-identity question, Grant-ratified 2026-07-03 | `manuscript/ave-kb/common/vocabulary-register.md`:536 |
| the canonical-wall location — a gating genesis decision | `_orchestration/2026-06-06_genesis-next-steps-scope.md`:10 |
| the sector-of-storage question | this directory, `sector-of-storage` |
| a continuum radial-solver build gate | queue `:57`,`:63` |

The queue documents the collision and records a **count correction it forced** — the 2026-08-02
enumeration was internally inconsistent and had to be withdrawn under Rule 12.

**No document discipline fixes this.** It is a key-namespace failure and needs a registry with
uniqueness enforcement — the same shape as `verify-docket-keys.py`, which already does this job
for docket keys. Scoping that reuse is the work.

**Also routed and still open (bookkeeping, not physics):** whether the 2026-08-01/02 batch is
eleven rulings or twelve (queue `:112`).
