# Crystal-Graft v2 — pre-registration (the winding gets its OWN Cosserat-ω carrier)

**Date:** 2026-06-09 · **Branch:** `analysis/2026-06-09-crystal-graft-v2` · **Lane:** implementer
**Skills fired (pre-build):** `ave-prereg`, `substrate-native-check` (CP1/2/4/8/9/10),
`ave-conserved-vs-pumped`, `phase-space-coordinate-check`, `consistency-vs-emergence`,
`verify-before-cite`.

## 0 — The diagnosis this build acts on (verified, not assumed)

The prior crystal engine (`6af430cd`, `research/2026-06-09_crystal-engine_result.md`) was a clean
**Outcome C**: `(2,3)` did not close — `w_tor=0 AND w_pol=0` on reliable contours — and the residual was
**pinned to one mechanism**: *the scalar Master-Equation bulk has no multi-component U(1)-fibre carrier*
(result §9). I verified the mechanism in code this session:

- `crystal_engine.py:304-318` `phase_space_vinc_vref` returns `(V, ∂_tV/ω, V, −∂_tV/ω)` — **V_inc and
  V_ref are both projections of the SAME scalar `V`** (a single complex scalar `V+i∂_tV`).
- `master_fdtd_phasor_bridge.py:14-18`: `V_inc=½(V_phys+Z₀I_phys)`, `V_ref=½(V_phys−Z₀I_phys)` — both
  built from the one scalar field. `k4_tlm.py:346`: `V_ref = 0.5·ΣV_inc − V_inc` (Op5) — **not an
  independent reactance**.

A single complex scalar traces a **circle**, not a torus: one of the two windings is structurally forced
to zero. This is the genesis-24/crystal double-count. **This build removes it** by giving the winding its
own carrier.

## 1 — Target (one sentence)

Build a **3-sector** chiral Cosserat engine — (V) bulk dilatation breather/mass with a **hardened Γ=−1**
acoustic wall; (w) transverse shear photon; **(ω) an INDEPENDENT Cosserat micro-rotation winding sector
with its OWN decoupled C/L reactance** — coupled by a conserved chiral **compression→micro-rotation
BUCKLE** (ADD-2), and test whether the `(2,3)` knot can self-assemble **in the ω sector** de-novo.

## 2 — Physical picture (5 bullets, no math)

- The vacuum is a compressible chiral Cosserat continuum. Helmholtz-split: irrotational bulk (K, the
  dilatation breather = **mass**) + solenoidal shear (G, the **photon**) + micro-rotation couple-stress
  (the **winding/intrinsic spin**). These are orthogonal (A1 ⊥ T2).
- The breather over-saturates the medium and generates a **Γ=−1 acoustic wall** it cannot compress past;
  `c_eff(V)=c0·S^{−1/2}→∞` in the saturated core (refractive `n=S^{1/4}→0`) is what makes the wall.
- When the breather hits the wall (blocked longitudinal energy), it **buckles** — like an axially-loaded
  column buckling into a helix — parity-odd, into the **micro-rotation ω** sector. That is ADD-2.
- The ω sector is an **independent U(1)**: its own field + its own conjugate momentum (couple-stress),
  its own LC tank with a mass-gap restoring torque — **NOT** a read-only projection of the bulk V. So a
  poloidal winding in ω **CAN** be nonzero by construction.
- The `(2,3)` = toroidal "2" (the ω polarization-direction winding around the major circle) + poloidal
  "3" (the ω LC-phase winding around the minor circle). Charge = Beltrami helicity of ω.

## 3 — Sectors / coordinates (substrate-native-check)

- **CP1:** wave propagation (leapfrog FDTD), NOT minimization. **CP2:** the winding is a phase-space
  object; it lives in the **ω-sector phasor** `(ω, π_ω/Ω_ω)`, the ω LC reactance pair — NOT real-space,
  NOT the bulk-V phasor. **CP4:** measured in matching (phase-space) coordinates.
- **CP8:** seed the **generative precursor** (transverse photon + a pre-compressed dilatation seed =
  CP8 precursor), NOT a planted `(2,3)`; let the buckle build the winding. Matched no-photon / no-chirality
  control must be null.
- **CP9:** the ω field is **dynamically evolved** by its own wave equation (state variable integrated by
  `step()`), not an algebraic heuristic — so it CAN carry emergence. **CP10:** the wall and the buckle are
  **boundary-localized** (Γ at the saturation front), not a bulk confining force → bounded, no detonation.
- **ave-conserved-vs-pumped:** the winding/helicity is a **conserved invariant — energize+LOCK**, not
  pumped. ADD-2 is one Hamiltonian coupling term (functional-derivative source + back-reaction, total H
  cancels). `|L|` bounded; `d|H|/dt≈0`. The genesis-24 EMF pump (`|L| 2.7→43`, `E_V→6.8e8`) is the named
  failure to avoid.

## 4 — Predictions / discriminating outcomes (FROZEN before running)

**Smokes (Rule 10 — all must pass to proceed):**

- **SMOKE-1 (WALL HARDENS):** with the `c_eff` trap and a deeply-compressed core, `Γ_min` (engine
  convention `Γ=(n−1)/(n+1)`, `n=S^{1/4}`) drives toward **−1** (target `Γ_min < −0.7`, hardening as the
  core saturates), vs genesis-24's `|Γ|<0.08`. Breather **confines** (localization stays high). Floor set
  by `S_min` (named engineering knob, stated).
- **SMOKE-2 (BUCKLE conservative):** ADD-2 sources the ω sector from blocked compression; total
  `H=E_V+E_ω` flat to a few % (energize-LOCK), `|L_ω|` **bounded** (no secular growth), fields O(1) (no
  detonation), **centrosymmetric baseline (κ̃=0 / no-chirality) = 0** winding sourced.
- **SMOKE-3 (WINDING-SECTOR-INDEPENDENT — the anti-double-count check):** the ω sector is NOT a projection
  of V_inc. Two structural proofs: (a) **carrier gate** — seed ω with a KNOWN-imposed `(2,3)`, read it
  back with the ω-sector extractor → `(w_tor,w_pol)≈(2,3)` (the old scalar bulk read `(*,0)`); (b)
  **independence** — with the buckle off, perturbing V leaves the ω winding read unchanged (ω carries its
  own phase). If (a) returns `w_pol=0` the carrier is still degenerate → STOP (fix not achieved).

**Expected (my honest prior):** SMOKE-1/2/3 **PASS** (the c_eff trap is mathematically sound; the H_couple
form conserves by construction; an independent 3-vector field with its own momentum genuinely hosts two
independent phases). The **structural fix (SMOKE-3a, w_pol able to be nonzero) is the load-bearing
deliverable** — the previous run could not get here.

**Full run (if smokes pass):**

- **Outcome A (Class-D CHORD — extraordinary, state as CANDIDATE only):** `(2,3)` closes de-novo in ω
  (w_tor≈2 AND w_pol≈3 on rel>0.1 contours, no-photon control null) **AND** with α-free inputs (κ̃=6/5,
  V_yield≡1) `α⁻¹=4π³+π²+π` EMERGES as the leak-rate `Q⁻¹` **AND** the Golden-Torus self-assembles
  (`R·r→¼`, `R/r→φ²`) **AND** the joint ledger closes (mₑc² entrained-compression + charge=helicity at one
  operating point). I assign this **low prior** — and a false A is strictly worse than an honest C.
- **Outcome B (manifestation — real progress):** `(2,3)` closes but α enters as calibration (the geometry
  is imposed / α tunes the resonance). FIRST time the knot forms with its own carrier.
- **Outcome C (residual localized — likely):** w_pol is now structurally nonzero (progress over the prior
  `w_pol≡0`) but the **specific** `(2,3)` does not lock de-novo → residual = mode-SELECTION (which knot),
  **NOT** the double-count (which is fixed). Name the new residual; close honestly.

**My most-likely prior:** **C** (with SMOKE-3 PASS as the real deliverable), possibly **B**. The
joint-ledger guard **refuses** any near-137 `Q` that comes without a real `(2,3)` (no resonator → no α).

**Falsifier of the framing:** if SMOKE-3a returns `w_pol=0` on a KNOWN-imposed `(2,3)` in the ω sector,
then even the independent carrier cannot host the poloidal winding — the framing (winding lives in the
Cosserat micro-rotation) is wrong, not just the selection.

## 5 — Dimensional / parameter pre-freeze (α-free)

- `κ̃ = 6/5 = pq/(p+q)` for `(p,q)=(2,3)` — the topology, **α-free** (NOT `1.2α`). Circularity vector #1.
- `V_yield ≡ 1` (engine-natural units) — circularity vector #2. Both held α-free for the chord test.
- `c_L²/c_T² = 2(1−ν)/(1−2ν) = 10/3` at `ν_vac=2/7` (DERIVED). ω-sector speed `c_ω` and mass-gap `ω_0`
  are the couple-stress reactance: set `c_ω=c_T` (shear-family) and `ω_0` to the breather-shell resonance
  so the ω tank rings at the trap frequency (named; the ONLY ω-sector knob, and it is NOT α).
- Golden-torus targets are **canonical, derived** (`constants.py`: `RR_GOLDEN_TORUS=¼`, `R/r=φ²`,
  `ALPHA_COLD_INV=4π³+π²+π`); they are the EMERGENCE targets, never inputs.

**Verdict will be reported with REAL numbers and a DATA-derived caption on every figure (no templated
success).**
