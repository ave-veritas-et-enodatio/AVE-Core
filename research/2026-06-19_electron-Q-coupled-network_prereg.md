# Pre-registration — Electron bound-mode Q from the graded-vacuum impedance network

**Frozen:** 2026-06-19 (Grant-ratified this session). This document is committed as the
FIRST commit of the build branch so the git trail shows frozen-before-build. No
adjudication criterion below may be dropped or relaxed post-hoc (Rule 11 honest closure;
Rule 12 substitution-not-retraction).

**Branch:** `analysis/2026-06-19-electron-Q-coupled-network` (worktree-isolated off
`origin/main` @ 39ab0a25).

---

## GOAL

Derive the electron bound-mode quality factor Q from the substrate-native graded-vacuum
impedance network.

- **CHORD** = α moves echo→chord at the electron: Q falls out of α-FREE inputs at
  Q ~ 1/α = 137.036.
- **ECHO** = it does not.
- **PRIOR** = α is an ECHO. The α-free cold cage gives Q ≈ 30.8 (NOT 137); recorded at
  `src/tests/engine_acceptance/test_l3_mass_cage.py:25` (T3.4b headline: Q_ringdown ≈ 30.8,
  Q_linewidth ≈ 3.8, ω_cutoff ≈ 2.87). This is the negative the present build must
  PRESERVE (HR4), not overwrite.

This is a DISCRIMINATING TEST. A gate FAILURE is a legitimate scientific outcome to
report honestly (moved-negative / solver-bug / re-derived-echo), NOT an error to hide.

---

## BINS (frozen — no post-hoc movement)

### CHORD bin (ALL four must hold)
1. Coupled-network complex-ω Q in **[127, 147]** (tightened from the cold-cage ±20 to
   ±10 — an eigensolve has no FFT-bin noise floor).
2. Q derived from **α-FREE inputs only**: ZERO `alpha` / `Q_TANK` / `137` / `1/alpha`
   tokens in the network-input / impedance / coupling / kernel code (grep-proven).
3. Q is **α-INVARIANT** under the α→2α perturbation test (double α in constants,
   re-solve, Q must NOT move).
4. The **isolation validate-on-known gate (GATE1) passed FIRST**.

Landing in [127, 147] WITHOUT (2)(3)(4) = re-derived ECHO → binned **ECHO**.

### ECHO bin
- (a) Q stays ~order of the isolation band [10, 60] (couplings fail to supply the store —
  corroborates the prior); OR
- (b) Q near 137 but FAILS any extraordinary-claim guard (α leaked / units-bridge / the
  isolation gate failed).

---

## THE ALPHA-LEAK (load-bearing — Finding 1; verified on HEAD 39ab0a25)

`RHO_BULK = ξ²·μ₀ / (P_C · ℓ_node²)` (`src/ave/core/constants.py:664`), with
`P_C = 8π·α` (`:400`). Therefore **RHO_BULK ∝ 1/(8π·α)**.

So the BARE impedance magnitudes carry α:
- `Z_shear = rho_bulk · c_shear`  →  ∝ 1/α
- `Z_bulk  = √2 · rho_bulk · c_0`  →  ∝ 1/α

The network MUST use ONLY **dimensionless impedance RATIOS** so RHO_BULK cancels from every
Q-determining quantity:

> **Z_bulk / Z_shear = √2 · √(10/3) = 2.581989** — exactly α-invariant.

(Derivation of the ratio: c_bulk = √(K/ρ) = √(2G/ρ) = √2·c₀ with K=2G [merged PR#261];
the shear/transverse speed is c_T from the Cosserat constitutive. With ν_vac = 2/7 the
K/G ratio fixes the speed ratio; the √(10/3) factor is the bulk/shear *speed* ratio that
multiplies the √2 amplitude split. The exact closed-form ratio is asserted here as the
frozen target and is re-derived alpha-free in the solver docstring at Stage 2.)

The STRONGEST gate is the mechanized **α→2α invariance test**: double α in constants,
re-solve, Q must NOT move (the ratios are α-free, so a Q that moves means a bare magnitude
leaked).

---

## HARD REQUIREMENTS

- **HR1 — substrate-native lattice + stencil.** `chiral_lattice.build_srs_net` primary
  (`src/ave/core/chiral_lattice.py:199`) + `build_diamond_net` achiral control (`:227`).
  Tetrahedral gradient / curl / divergence from
  `src/ave/topological/cosserat_field_3d.py` (`_tetrahedral_gradient` :148, public
  `tetrahedral_gradient` :716, `adjoint_tetrahedral_divergence` :161, `_tetrahedral_curl`
  :440), sign-verified by the keeper `test_cosserat_field_3d.py:32`
  (`test_tetrahedral_gradient_on_linear_field_reproduces_slope`).
  **FORBIDDEN:** the Cartesian 7-pt Laplacian (`crystal_engine.py:154` `_laplacian`;
  `master_equation_fdtd.py:124` `_laplacian`).
- **HR2 — no baked α.** Allowed inputs ONLY: `Z_0` (`constants.py:98`), `c_0` (`:95`),
  <!-- 🔧 citation-fix 2026-06-19 (verify-before-cite, no verdict change): `Z_0` is
  `constants.py:98` (verified on branch tip), not `:99` as first transcribed. The input
  set and the α-free verdict are untouched. -->
  `nu_vac = 2/7` (`:532`), `kappa_tilde = 6/5` (`cosserat_field_3d.py:94`
  `KAPPA_TILDE_ELECTRON`; provenance `research/2026-06-09_crystal-graft-v2_result.md`),
  `L_NODE` (`:257`), lattice geometry. **FORBIDDEN:** `Q_TANK = 1/ALPHA`
  (`cvr_model.py:72`), `coupled_resonator` `k = 2*alpha` defaults; SECOND-LEAK: no bare
  `RHO_BULK` / `Z_shear` / `Z_bulk` magnitude — ratios only.
- **HR3 — validate-on-known FIRST.** Reproduce the isolation Q at the same order as 30.8
  before any coupled claim.
- **HR4 — preserve the 30.8 negative (anti-substitution).** The cold-cage ECHO finding
  stays intact; this build does not edit/overwrite it.
- **HR5 — Op14 wall = μ-load SHORT** (Z_core→0, Γ→−1, settled PR#260); exponent per DEC-1.

---

## RATIFIED DECISIONS

- **DEC-1** — Run BOTH Op14 exponents `√S` and `S^{1/4}` as a sensitivity (`√S` primary,
  μ-load-justified). A chord counts only if it holds for the physical exponent AND we
  report exponent-robustness.
- **DEC-2** — Chord must hold at chiral-circulator = 0 (H_couple alone). The circulator
  is a swept Fork-B sensitivity only; a circulator-dependent 137 is a FIT, not a chord.
- **DEC-3** — Assume-and-FLAG the confinement-surface shape (smallest topology-consistent:
  electron = 0₁ unknot, single node); flag ASSUMED-not-derived, falsifier F8.
- **DEC-4** — Freeze on the TWO MECHANICAL channels (bulk + shear via H_couple); model the
  EM channel as a BARE matched loss-port (Γ_EM = 0 boundary admittance making the operator
  non-Hermitian). Do NOT instantiate the TKI-transformer (avoids the units-bridge-Q hazard
  F4).
- **DEC-5** — Isolation tolerance Q in [20, 45] + anti-coincidence sub-check:
  `Z_RADIATION = Z_0/(4π) = 29.98` (`constants.py:717`) sits IN the band — confirm the
  solver computes the dynamics, not silently reads 29.98.

---

## GATES

Build-A runs Gates 1, 2, 4 + anti-coincidence. Gates 3, 5 and the coupled leg are Build-B.

- **GATE1 (MANDATORY validate-on-known)** — isolation-leg Q in **[20, 45]** on
  (N=72, S_min=1e-3, A_cap=0.999, pml=12), cross-checked vs `ringdown_Q`
  (Q = ω₀·τ/2, `_bulk.py:489`). **FAIL if ~137** (leak/bake → HALT, surface
  moved-negative) **or ~3** (FFT-bin-1 artifact path → solver bug → HALT).
- **GATE2 (lossless)** — with the EM port CLOSED (Γ_EM = −1, all confined) → Q = ∞.
- **GATE4 (Nyquist)** — bound mode gapped, peak bin > 1, ω_r·dt ≪ π, shear branch
  resolved.

---

## ANTI-CIRCULARITY (enforced even at Build-A)

- grep the new solver module for `alpha` / `137` / `Q_TANK` → ZERO hits in inputs.
- import-guard assert (`Q_TANK` / `ELECTRON` not in module globals).
- every Q-determining quantity is a dimensionless RATIO (no bare RHO_BULK / Z magnitude).
- run the α→2α invariance check on the isolation Q (should be invariant).
- solver docstring carries each input's α-free provenance + the pinned Op14 exponent(s).

---

## BUILD-A SCOPE — Stages 0–3 ONLY

Do NOT implement `H_couple`, the coupled solve, or Fork-A coupling (those are Build-B).
If GATE1 fails, **HALT and report** (do not push toward the coupled leg).

- **STAGE 0 (freeze)** — write + commit THIS prereg doc as the FIRST commit. Record its SHA.
- **STAGE 1 (native operator)** — assemble `L_native = adjoint_tetrahedral_divergence ∘ D
  ∘ tetrahedral_gradient` using the tetrahedral operators (NOT the Cartesian Laplacian),
  D block-diagonal in (bulk K / shear G). Keep the bulk scalar V (MASS-3) and the
  shear/Cosserat ω (CHARGE-3) ORTHOGONAL — never a shared (V_inc, V_ref) phasor
  (A1⊥T2, `master-equation.md:20`). GATE: the keeper `test_cosserat_field_3d.py:32` still
  passes; the operator is sign-consistent with a Cartesian gradient on a smooth test field.
- **STAGE 2 (NEW eigensolver, ISOLATION leg)** — H_couple OFF, circulator OFF, bulk
  channel + EM matched loss-port. Assemble the non-Hermitian generalized eigenproblem
  `det[L_native(ω) − ω²·M] = 0` with the μ-load SHORT Γ=−1 confinement BC (Z_core→0) on
  the bulk channel and the Γ_EM = 0 matched radiative loss-port (boundary admittance, NOT
  a transducer per DEC-4). Solve via `np.linalg.eig` (dense) or
  `scipy.sparse.linalg.eigs` shift-invert near ω ~ 2.87. Q = |Re ω| / (2|Im ω|). Run for
  BOTH Op14 exponents (DEC-1). GATE1 (MANDATORY): Q_isolation in [20, 45]; cross-check vs
  ringdown_Q. If ~137 or ~3 → HALT + report binned reason. Anti-coincidence: confirm Q is
  NOT silently 29.98.
- **STAGE 3 (lossless + Nyquist sanity)** — GATE2 (EM port CLOSED → Q=∞; loss enters only
  via the matched port). GATE4 (mode gapped, peak bin > 1, ω_r·dt ≪ π, shear branch
  resolved).

---

## CITATION VERIFICATION (re-grepped on HEAD 39ab0a25 before freeze)

| Citation | On-HEAD status |
|---|---|
| `constants.py:664` RHO_BULK = ξ²μ₀/(P_C·ℓ²) | CONFIRMED |
| `constants.py:400` P_C = 8πα | CONFIRMED (⇒ RHO_BULK ∝ 1/α) |
| `constants.py:95` C_0, `:98` Z_0, `:532` NU_VAC=2/7, `:257` L_NODE | CONFIRMED (Z_0 corrected `:99`→`:98` 2026-06-19, verify-before-cite) |
| `constants.py:717` Z_RADIATION = Z_0/(4π) ≈ 29.98 | CONFIRMED |
| `cosserat_field_3d.py:148/161/440/716` tetra grad/div/curl + public alias | CONFIRMED |
| `cosserat_field_3d.py:94` KAPPA_TILDE_ELECTRON = 6/5 | CONFIRMED |
| `test_cosserat_field_3d.py:32` keeper gradient test | CONFIRMED (passes clean) |
| `crystal_engine.py:154` `_laplacian` (Cartesian 7-pt) FORBIDDEN | CONFIRMED |
| `master_equation_fdtd.py:124` `_laplacian` (Cartesian) FORBIDDEN | CONFIRMED |
| `cvr_model.py:72` Q_TANK = 1/ALPHA FORBIDDEN | CONFIRMED |
| `chiral_lattice.py:199` build_srs_net, `:227` build_diamond_net | CONFIRMED |
| `_bulk.py:489` ringdown_Q = ω₀·τ/2 | CONFIRMED |
| `test_l3_mass_cage.py:25` Q_ringdown ≈ 30.8 (the 30.8 negative) | CONFIRMED |
