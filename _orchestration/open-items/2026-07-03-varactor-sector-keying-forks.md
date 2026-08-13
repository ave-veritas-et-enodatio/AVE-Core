---
id: varactor-sector-keying-forks
title: The two varactor sector-keying forks — ADJUDICATION-PENDING
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-07-03
source: _orchestration/index.md
anchor: "**(v) The two varactor sector-keying forks — ADJUDICATION-PENDING**"
---

Created 2026-07-03 by the V_SNAP value change (`930c5964`): V_YIELD 43.65 kV → V_SNAP 511 kV,
an 11.7× = 1/√α scale — explicitly **not** "small."

1. **AVE_EE_BENCH form contradiction.** The `.lib` implements the divergent C0/S (A1) form while
   the canonical EE bench measures the collapse C0·S (T2) — *"models a different sector than the
   EE bench actually reads."* The keying (A1 ⇒ V_snap vs T2 ⇒ V_yield) rides on which sector it is.
2. **AVE_VACUUM_CELL_L1 memristor cross-sector.** An A1-compliance divergent `B_VAR` gated by a
   T2-yield memristor S-state — a cross-sector (A1×T2) construction whose knee attribution is
   ambiguous.

Both left UNCHANGED and surfaced for Grant. Migrated 2026-08-13 from the index.md ledger.
