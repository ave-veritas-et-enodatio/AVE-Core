---
id: a0-glyph-collision
title: "A_0 is two objects: the Bohr radius (a length, exported by constants.py) and the Axiom-4 operating point (dimensionless) — and one live equation consumes both"
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-08-24
source: src/ave/core/constants.py
anchor: "A_0: float = L_NODE / ALPHA"
---

Surfaced by the 2026-08-24 symbol-collision sweep (dispatched under the ruling recorded at
`docket-entries/2026-08-24-pairprod-carve-and-kernel-homonym.md`). **Receipts re-verified by
the orchestrator before this item was minted**, per the same-day lesson that a collision
claim owes its own sweep.

**The two referents:**
- `src/ave/core/constants.py:348` — `A_0: float = L_NODE / ALPHA` ≈ 5.2918e-11 m. A LENGTH
  (the Bohr radius).
- `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2 — "$A_0 = V_{DC}/V_{yield}$ is a **per-node**
  ratio". DIMENSIONLESS (the Axiom-4 saturation operating point, i.e. the value of the
  kernel argument A).

**Why this is the fatal class and not a benign overload:** one live equation consumes both
senses. `manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex:4103`:

    strain_{amp} = \frac{V(r)}{V_{yield}} \approx \frac{Z \alpha^2 A_0}{r}

The LEFT side is the kernel amplitude (canon's A). The RIGHT side's `A_0` is the Bohr
radius. A reader carrying canon's dimensionless `A_0` into this expression gets nonsense
that **no unit check catches**, because `constants.py` exports a bare float and the corpus's
only guard here is letter case (KB writes lowercase `a_0` for the Bohr radius; vol_2 ch07
and `constants.py` use uppercase). Both senses are live in `src/`.

**Related, and deliberately kept separate:** the kernel argument A also carries two
NORMALIZATIONS (yield-denominated vs bare/snap) — that is open-item
`kernel-argument-normalization`. A subscripting pass that fixes only the normalization
leaves `A_0` still double-booked; whether the two passes are one job is part of this ruling.

**Candidate dispositions (nothing pre-selected):** (a) rename the constant to `a_0`/`BOHR_RADIUS`
and sweep its consumers; (b) rename the operating point; (c) leave both and add a
symbol-collision warning on the δ_CP template. Note (a) touches `src/` consumers including
`src/tests/test_x42_atomic_eigencavity.py`.
