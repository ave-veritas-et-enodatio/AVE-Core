# Constituent-cage fixture — RESULT (PR#770 fabricated-string regression fixture)

Prereg-file: research/2026-07-30_constituent-cage-fixture_prereg-FROZEN.md

Reconstructs the PR#770 **fabricated-string-labeled-frozen** pattern (dated
2026-07-30 so the gate fires with teeth): a Leg-5 robustness note surfaced as a
frozen/pressure-tested result that was never in the committed prereg and never
computed (the run evaluated only `S_RAIL=0.03`). The gate must FAIL this line.

> **Leg 5 (N-scaling) — Frozen:** `ROBUST across rail depth (S_RAIL 0.03→0.003 all RISING, pressure-tested)`

A control line whose criterion IS in the prereg (must NOT fire):

> **Leg 5 discriminator — Frozen:** `ρ_N → 1 (coarse-grained texture, BIN-1) vs bounded <1/falling (per-core cage, BIN-2)`
