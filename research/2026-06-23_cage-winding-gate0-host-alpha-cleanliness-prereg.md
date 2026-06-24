# GATE 0 PREREG — cage⊗winding-engine host α-cleanliness (the hard STOP de-risk)

**Created:** 2026-06-23 · implementer lane · branch `analysis/cage-winding-gate0`
**Charter:** [`_orchestration/2026-06-23_cage-winding-engine-charter.md`](../_orchestration/2026-06-23_cage-winding-engine-charter.md) (FIRST MILESTONE: Gate 0 + Rung 4)
**Class:** validate-on-known · refute-by-default · STOP-gate (if it fails, the build approach is wrong and we stop)

---

## SECTOR HEADER (written BEFORE any standard-physics word)

- **WHICH SECTOR:** A1 dilatation **mass-cage** (the Γ=−1 confinement wall) proposed to be hosted **on the Cosserat
  winding engine** `src/ave/topological/cosserat_field_3d.py`. This Gate tests ONLY the cage-on-the-host + its
  α-cleanliness. The (2,3) winding, the circulator coupling, and the Observable-C chord come in LATER rungs, NOT now.
- **REGIME:** COLD. The cold-Q ring-down is a cold-linear measurement (A≪1 ring of a posited saturated cavity). The
  chord is a later driven/near-yield measurement; Gate 0 is cold by construction. A cold null here is NOT a
  wrong-regime artifact — cold is the declared regime for the Q-vs-137 decider (the existing green
  `test_l3_mass_cage.py` T3.4b measures exactly this).
- **THE WHOLE POINT — α-CLEANLINESS:** the host ships `KAPPA_CHIRAL_ELECTRON = ALPHA · κ̃` as the DEFAULT
  (`cosserat_field_3d.py:131`). Wiring that in IMPORTS α and would fake a Q=137 (=1/α). The engine MUST run on the
  α-FREE topological factor `κ̃ = pq/(p+q) = 6/5` (`cosserat_field_3d.py:94,:98`, `kappa_tilde_torus`), and MUST
  reproduce the known cold-cage NEGATIVE Q≈30.8 ≠ 137 with the **Q-slot left EMPTY** (strict anti-substitution — do
  NOT let anything refill 137).

---

## SUBSTRATE-NATIVE-CHECK (walked before any numerical wiring)

- **Dynamics:** the host is the K4-tetrahedral Cosserat field with a velocity-Verlet (energy-conserving, damping=0,
  `:940`) integrator + a moving Γ=−1 impedance-boundary cage rendered as an **exact harmonic LC-reactance Strang-split
  rotation** of the (ω, ω̇) reactance pair (`:953-998`). This is a time-domain scatter+connect, NOT a
  Lagrangian/gradient-descent/energy-basin solve. ✓ substrate-native.
- **Sector:** the cage is the A1 dilatation / Γ=−1 boundary; the winding is the Cosserat (2,3) ω. The two-3s guard
  (`master-equation.md:20`) requires the winding is never wired into the breather's (V_inc,V_ref) phasor. Gate 0
  exercises the cage ONLY (winding OFF).
- **Reactance pair (Rule 10):** the impedance cage tracks (ω = C-state, ω̇ = L-state) as the rotated pair
  (`:996`). Both half-kicks see the same per-step frozen clamp weight (`:971-975`) so the moving wall is a
  conservative potential force within the step. ✓.
- **Op14 local clock:** N/A at Gate 0 (cold, no saturation drive on the winding; the cage is the boundary, not a
  bulk c_eff(V) well).

## CONSISTENCY-vs-EMERGENCE tag

- The Q-vs-137 read is a **CHORD-vs-ECHO decider**, NOT an emergence claim. The PASS criterion is a finite α-free
  cold-Q that does NOT reproduce 137 (the corpus Q=1/α is an instance-baked ECHO; reproducing 137 from an α-free cage
  would be the instrument-echo-trap, `theorem-3-1-q-factor.md:21`). Tagged **CONSISTENCY / anti-echo**.

---

## PRE-REGISTERED PASS / STOP BINS (frozen 2026-06-23, BEFORE the run)

> Per charter PASS/FAIL, refute-by-default.

- **PASS** = ALL of:
  1. the α-leak import-guard does NOT trip when applied to the host/driver path (ALPHA / Q_TANK / ELECTRON
     unreachable in the engine globals that carry the cage dynamics);
  2. the cage MECHANISM survives on the winding-host (the L3 mass-cage rungs that were green stay green); AND
  3. the cold-Q reproduces ≈30.8 (NOT 137), with the **Q-slot EMPTY** (nothing in the measurement path refills 137).

- **STOP (HARD)** = ANY of:
  1. the α-guard TRIPS (ALPHA / Q_TANK / ELECTRON reachable in the cage-dynamics globals); OR
  2. **137 (1/α) reappears anywhere** in the Q-readout path (a baked golden-torus α⁻¹ form counts — the Q-slot is
     not empty); OR
  3. the cage mechanism BREAKS on the host.
  Report as a HARD STOP — the build approach is α-contaminated or the host can't carry the cage. **Do NOT patch
  around a 137 to make it pass; that IS the failure signal** (substitution-not-retraction / honest-closure).

## ADJUDICATION CRITERIA (locked; not droppable post-hoc)

- The guard is the **verbatim canonical pattern** copied from `src/ave/solvers/vacuum_varactor_scatter.py:110-112`
  (`assert "ALPHA" not in globals()` / `"Q_TANK"` / `"ELECTRON"`).
- α-free means κ̃=6/5 is the topological factor in the cage Γ-field, NOT κ_chiral=α·κ̃.
- "Q-slot empty" means the cold-Q is **measured from cold ring-down dynamics** (rfft linewidth + Hilbert-envelope
  decay), NOT read from a closed-form geometric formula that algebraically equals 4π³+π²+π at any normalization.

## EXECUTABLE PROBE

`src/scripts/vol_1_foundations/cage_winding_gate0_alpha_cleanliness_probe.py` — reproduces, from a clean import:
(1) the host module-globals guard probe; (2) the host Γ-field κ_chiral wiring; (3) the host
`extract_quality_factor()` golden-torus form evaluated against α⁻¹; (4) the existing α-free `_bulk.py`
cold-Q≈30.8 baseline for contrast.

## RESULT

See [`2026-06-23_cage-winding-gate0-host-alpha-cleanliness-result.md`](2026-06-23_cage-winding-gate0-host-alpha-cleanliness-result.md).
