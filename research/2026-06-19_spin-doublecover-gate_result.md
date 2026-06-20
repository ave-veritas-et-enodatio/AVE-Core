# Result — Carrier-sector GATE #1: Spin double-cover representability

**Run:** 2026-06-19
**Branch:** `analysis/2026-06-19-spin-doublecover-gate` (HEAD off `6e962ff9`)
**Prereg (frozen BEFORE run):** [`research/2026-06-19_spin-doublecover-gate_prereg.md`](2026-06-19_spin-doublecover-gate_prereg.md)
**Probe:** `CosseratField3D.probe_spin_doublecover_holonomy` (`src/ave/topological/cosserat_field_3d.py`)
**Test:** `src/tests/test_cosserat_field_3d.py::test_spin_doublecover_gate_verdict_pass`
**Class:** D / representability (reads a group-theoretic SIGN, no CODATA number).

---

## VERDICT: **PASS** — double-cover representable; FM-on-K4 supported at the lattice level

Stable across three lattice-resolved diagnostic scales (`R = 4, 6, 8` cells —
NOT the sub-cell `~0.16 ℓ_node` canonical scale; this gate tests
TOPOLOGY/representability, not the canonical sub-cell soliton). KINEMATIC ONLY:
no time-stepping, no energy budget, no CFL/Nyquist gate binds.

| R | site (peak-\|ω\|) | trivial-vector n_hat baseline \|Δ\| @2π | OP_A sign @2π / @4π | OP_B sign @2π / @4π | verdict |
|---|---|---|---|---|---|
| 4.0 | (6, 8, 10) | 4.71e-16 (returned) | +1 / +1 | **−1 / +1** | PASS |
| 6.0 | (17, 9, 11) | 6.78e-16 (returned) | +1 / +1 | **−1 / +1** | PASS |
| 8.0 | (20, 18, 14) | 2.54e-16 (returned) | +1 / +1 | **−1 / +1** | PASS |

- **VALIDATE-ON-KNOWN (wired first):** the trivial-vector `n_hat` baseline
  returns at `φ=2π` to machine precision (`|Δ| ~ 1e-16`) at every scale → the
  calibration anchor behaves → **NOT a HALT**. The discriminator is interpretable.
- **OP_A** (re-lift of `R_body(φ)·ω`; the natural `T=A4` SO(3) action on the
  stored rotation-vector field): returns to `+I` at `φ=2π`. Identical to the
  trivial-vector baseline by construction — the SO(3) rotation-vector has period
  `2π` and the re-lift carries no memory of the twist.
- **OP_B** (SU(2) left-action `q_body(φ) ⊗ q(ω)`; the `2T ⊂ SU(2)` binary-
  tetrahedral action): returns to **`−I` at `φ=2π` AND `+I` at `φ=4π`** — the
  genuine `4π` double-cover signature, and it **DIFFERS from the trivial-vector
  baseline** (the prereg discriminator).

Frozen-bin match: PASS requires the SU(2)-lift holonomy → `−I` at 2π **AND**
`+I` at 4π **AND** differing from the trivial-vector baseline. All three met by OP_B.

---

## What the PASS means — and its honest scope (flag-don't-fix)

**What is established:** the AVE substrate *admits* the `2T ⊂ SU(2)` double-cover
action on the extended unknot defect's frame as a distinct, non-trivial,
lattice-level frame transport — provably `≠` the trivial-vector (SO(3)/`T=A4`)
baseline. This is the lattice-level representability the FM-on-K4 identification
needs: per [`finkelstein-misner-spin-half-derivation.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md)
§3, "physical fields on the K4 lattice must transform under `2T` rather than `T`"
for spin-½ to be K4-derived; the `K4 → A4 → 2T ⊂ SU(2)` chain has the `ℤ₂`
quotient (`−I`) realizing the `4π` cover. This gate confirms that the `2T` action
is representable and observable as a sign-flip at `2π` distinct from the trivial
`T` action — at the lattice level, kinematically.

**What this PASS does NOT claim (load-bearing scope fences):**

1. **Representation-dependence is explicit, not hidden.** OP_A (the field as
   STORED — an SO(3) rotation-vector, period `2π` by the seeder's own construction,
   `cosserat_field_3d.py` unknot-seeder docstring "ω has SO(3) period 2π by
   construction; SU(2) double-cover is observable via Rodrigues projection, not
   encoded in the seed") returns at `2π`. OP_B (the `2T`/SU(2) lift action)
   carries the `4π`. The gate does NOT show the seeded field DYNAMICALLY selects
   `2T` over `T` — that selection is the FM-on-K4 *physical* argument (the defect
   is EXTENDED, not a point, so the embedding-twist picks up `2T`), which this
   kinematic gate does not re-derive. The gate shows the `2T` action is
   REPRESENTABLE and distinct, which is the necessary lattice-level condition.

2. **No FAIL escape was needed.** Per the prereg, a FAIL (lift → `+I` at `2π`,
   trivial SO(3), no available distinct double-cover action) would have been a
   clean load-bearing falsification of FM-on-K4 at the lattice level. That did
   not occur; the distinct `2T` action exists and behaves. Honest-closure (Rule
   11) was held in reserve and not triggered.

3. **Kinematic, not dynamical (CP9).** The holonomy is a group-theory observable
   on the SO(3)→SU(2) bundle, not an emergent dynamical state. No energy
   minimization, no time-stepping. The gate answers "CAN the substrate carry the
   `4π` object?" (yes), not "does it dynamically settle into it?" (out of scope).

---

## Guards (held end-to-end)

1. **TWO-3s ORTHOGONALITY** (`master-equation.md:20`): the probe reads ONLY the
   Cosserat `ω` micro-rotation grade. The `(2,3)`/winding is NEVER wired into the
   A1 `(V_inc, V_ref)` dilatation-mass phasor (the genesis-24 double-count). No
   A1-sector field is touched.
2. **PHASE-SPACE-COORDINATE-CHECK** (`def-kn0t01` SOLID): the `(2,3)` is a
   phase-space winding portrait on the Clifford torus; the rotation HERE is a
   REAL-SPACE SU(2)/SO(3) frame holonomy of the `0₁` unknot's micro-rotation. The
   two coordinate systems are not conflated.
3. **VALUE-ECHO IMMUNITY:** only the holonomy SIGN is read. No `-e`
   (`constants.py:100`) or `α` is imported or read anywhere in the probe/test.
4. **Γ-SIGN LABEL COLLISION:** this is a kinematic frame holonomy (the sign of
   the SU(2) lift). It is DISTINCT from the steric Pauli wall (`Γ→+1`) and the
   spinor stability wall (`Γ_spinor=-1`, the `2π→4π` sign **stability** wall in
   `resonant-lc-solitons.md:91`). No `Γ=-1 collision` phrasing in the probe.
   Note for the auditor: the spinor stability wall `Γ_spinor=-1` is the SAME
   physical sector (T2 micro-rotation, the `4π` cover) but is a DYNAMICAL
   stability boundary — distinct from this STATIC kinematic representability gate.

---

## Reproduce

```
PYTHONPATH=$PWD/src ./.venv/bin/python -m pytest \
  src/tests/test_cosserat_field_3d.py::test_spin_doublecover_gate_verdict_pass -q
```

`make verify`: PASS (exit 0).
