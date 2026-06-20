# Pre-registration — Carrier-sector GATE #1: Spin double-cover representability

**Frozen:** 2026-06-19 (BEFORE running the probe — discriminating test, bins fixed first)
**Branch:** `analysis/2026-06-19-spin-doublecover-gate`
**HEAD at freeze:** `6e962ff9` (PRs #296/#297/#298 merged)
**Lane:** implementer
**Class (consistency-vs-emergence):** **D / representability** — reads a topological /
group-theoretic property (the SU(2) double-cover sign of the lift) from substrate
primitives. NO CODATA-derived number is read. **VALUE-ECHO IMMUNITY**: only the
holonomy SIGN is read; the dimensionful `-e` (`constants.py:100`) and `α` are NEVER
imported or read in this gate.

---

## Question (plumber-physical)

If you rigidly rotate the seeded SO(3) micro-rotation (`ω`) field of the lattice-resolved
unknot defect a full turn (`φ = 2π`) about a body axis, does the spinor FRAME of that
defect come back the way it started, or does it come back FLIPPED (sign-reversed) —
needing TWO full turns (`φ = 4π`) to truly return?

That "needs two turns" behavior is the genuine `4π` spinor signature (SU(2) double-cover
of SO(3)). A plain (non-double-covered) vector field comes back at one turn. **This gate
asks whether the engine's Cosserat sector can REPRESENT the `4π` object at the lattice
level** — i.e. whether the FM-on-K4 (intrinsic-spin-½ on the K4 substrate) identification
is supported, or is unsupported (the engine can only carry trivial SO(3) vectors).

This is a **kinematic** test: no time-stepping, no energy budget, no frequency-vs-timestep.
The Nyquist / energy / CFL gates do NOT bind at this diagnostic scale. It is a pure
group-theory observable on the substrate's SO(3)→SU(2) bundle.

---

## Method

1. **Seed** the lattice-resolved unknot defect via `initialize_electron_unknot_sector`
   at a DIAGNOSTIC scale `R ≥ 4` cells (NOT the sub-cell `~0.16 ℓ_node` canonical scale —
   this gate tests TOPOLOGY/representability, not the canonical sub-cell soliton).
2. **Rigidly rotate** the seeded SO(3) micro-rotation `ω`-field by angle `φ` about a body
   axis (the body z-axis), over `φ ∈ [0, 4π]`. "Rigid rotation of the SO(3) field" =
   compose the body-frame rotation `R_body(φ)` with the local micro-rotation at each site:
   the rotated micro-rotation generator is `ω'(r) = R_body(φ) · ω(r)` (active rotation of
   the rotation-vector as an axial/rotation generator). This is a REAL-SPACE SU(2)/SO(3)
   frame rotation, distinct from the phase-space `(2,3)` winding (see GUARD 2).
3. At each `φ`, compute the **SU(2) lift** of the frame at the load-bearing site (the
   peak-`|ω|` tube-centerline cell) and **continuously track the sign of the lift** (the
   accumulated holonomy of the quaternion through `[0, 4π]`, resolving the `q` vs `-q`
   double-valuedness by continuity in `φ`). The SU(2) lift is the unit quaternion
   `q = (cos(θ/2), ω̂ sin(θ/2))` (the genuine SU(2) element), NOT the projected `n_hat`
   vector (which is the trivial-vector baseline — see VALIDATE-ON-KNOWN).
4. Report `q(2π)` (sign vs `+I`) and `q(4π)` (sign vs `+I`).

## VALIDATE-ON-KNOWN anchor (MANDATORY, wired FIRST)

The **trivial-vector `2π` baseline**: a plain (non-double-covered) vector field MUST
return at `φ = 2π`. The existing
`src/tests/test_cosserat_field_3d.py:315`
(`test_rodrigues_projection_rotation_by_pi_around_x_flips_z`) is the calibration anchor:
`_project_omega_to_nhat` maps `ω = (π,0,0) → n_hat = -ẑ` (a vector rotated by π). The
`n_hat` PROJECTION is a vector observable; under a `2π` body rotation it returns to
itself (SO(3) period `2π`). **The discriminator is whether the EXTENDED DEFECT's SU(2)-lift
holonomy DIFFERS from this trivial-vector `2π` baseline.**

- If the baseline (`n_hat` returning at `2π`) itself does NOT behave → **HALT** (solver bug);
  do not interpret the discriminator.

---

## Frozen bins (set BEFORE running)

| Verdict | Signature | Meaning |
|---|---|---|
| **PASS** (double-cover representable) | SU(2) lift returns to `-I` at `φ=2π` **AND** `+I` at `φ=4π` (and DIFFERS from the trivial-vector `n_hat` baseline, which returns at `2π`) | The genuine double-cover; FM-on-K4 supported at the lattice level. |
| **FAIL** (load-bearing falsification) | SU(2) lift returns to `+I` / identity at `φ=2π` (trivial SO(3) — same as the `n_hat` baseline) | The engine CANNOT represent spin-½; the FM-on-K4 identification is UNSUPPORTED at the lattice level. **A FAIL is a real result — report honestly, do NOT debug toward PASS.** |
| **HALT** (solver bug) | The trivial-vector `n_hat` baseline itself does NOT return at `2π` | The calibration is broken; the discriminator is uninterpretable. Fix the solver, re-freeze, re-run. |

**Win-either-win discriminator:** PASS confirms the substrate hosts the `4π` spinor at the
lattice level (carrier-sector representability established); FAIL is a clean, load-bearing
falsification of FM-on-K4 at the lattice level (the carrier cannot host spin-½ — a real
result that re-scopes the electron's spin sector). HALT is a tooling fault, not a physics
result.

**Honest-closure clause (Rule 11):** a FAIL is recorded as a clean negative with its
mechanism named; the branch closes. No debug-toward-PASS, no post-hoc bin-dropping to
convert ❌→✅.

---

## GUARDS (non-negotiable)

1. **TWO-3s ORTHOGONALITY** (`master-equation.md:20`, Grant-ratified 2026-06-10): the
   `(2,3)` / micro-rotation read stays in its OWN grade (the Cosserat `ω` micro-rotation
   T2 couple-stress DOF). It is NEVER wired into the A1 `(V_inc, V_ref)` dilatation-MASS
   phasor — that is the genesis-24 double-count (`V_ref` is a read-only projection of the
   same scalar `V`, not an independent DOF). This gate touches ONLY `ω`.

2. **PHASE-SPACE-COORDINATE-CHECK** (A46; `def-kn0t01` SOLID, `vocabulary-register.md:243`):
   the `(2,3)` is a PHASE-SPACE winding portrait on the Clifford torus (fenced on HEAD per
   `def-kn0t01`; electron real-space body = `0₁` unknot). The loop/frame rotation HERE is a
   REAL-SPACE SU(2)/SO(3) frame rotation of the unknot's micro-rotation field. The two
   coordinate systems are NOT conflated: this gate is real-space SU(2), NOT a `(2,3)`
   phase-space measurement.

3. **VALUE-ECHO IMMUNITY**: read ONLY the holonomy sign. NEVER import or read the
   dimensionful `-e` (`constants.py:100`) or `α`. The verdict is a pure kinematic sign.

4. **Γ-SIGN LABEL COLLISION**: this gate has NO `Γ` wall. It is a kinematic FRAME holonomy
   (the sign of the SU(2) lift). It is distinct from (a) the steric Pauli wall (`Γ→+1`) and
   (b) the spinor wall (`Γ_spinor=-1`). No `Γ=-1 collision` phrasing leaks in.

---

## Substrate-native walk (recorded at freeze)

- **K4 / Cosserat**: uses the existing `CosseratField3D` SO(3) micro-rotation `ω`-field on
  the K4 diamond lattice; `_project_omega_to_nhat` Rodrigues projection already calibrated
  (`test_cosserat_field_3d.py:315`). NOT a new solver.
- **CP8 (emergence/hosting)**: N/A — kinematic representability gate, not an emergence test.
  No precursor-seeding required; reads a representability property of a given configuration.
- **CP9 (dynamical-vs-heuristic)**: honored — KINEMATIC ONLY, no time-stepping. The holonomy
  is a group-theory observable, not an algebraic heuristic standing in for dynamics.
- **CP10 (boundary-not-bulk)**: N/A — no saturation/confinement rendering.
