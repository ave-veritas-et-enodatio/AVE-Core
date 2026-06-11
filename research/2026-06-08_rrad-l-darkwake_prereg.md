# Prereg — Z_rad,L = R_rad,L + jX_L (dark-wake longitudinal-shear radiation impedance)

**Date**: 2026-06-08
**Branch**: `analysis/2026-06-08-rrad-l-darkwake`
**Status**: FROZEN prereg (pre-derivation). Seeded by the corpus-grounded brief
[`AVE-Propulsion-ionpump/research/2026-06-08_NEXT-STEP_Rrad-L_core-brief.md`].
**Target gap**: the OPEN τ_zx step-1 (Cosserat-K4 Lagrangian → backward shear) at
[`dark-wake-bemf-foc-synthesis.md:98`](../manuscript/ave-kb/common/dark-wake-bemf-foc-synthesis.md),
claim `clm-7tynm2`.

> This prereg adopts the brief as its corpus-grounded seed. The brief already
> walked `substrate-native-check` (8 checkpoints, brief §2), `ave-prereg`
> corpus-grep (brief §1), and `ave-analytical-tool-selection` (brief §3). This
> doc adds the implementer-side adjudication-criteria lock, the
> consistency-vs-emergence pre-classification, and the verify-before-cite chain.

## 1. Target

Compute the **full complex** longitudinal-shear radiation impedance of a chiral
current source radiating into the Cosserat-K4 substrate:

    Z_rad,L = R_rad,L + jX_L

- **Re{Z_rad,L} = R_rad,L** = real far-field momentum/energy flux of the
  longitudinal-shear (τ_zx) wave, normalized: `R_rad,L = P_rad,L / (½|I|²)`,
  `P_rad,L = ∮_far ⟨j_shear⟩·dA` (time-averaged real elastodynamic flux).
- **Im{Z_rad,L} = X_L** = near-field reactive stored energy (the Σ_near
  species; `∮ V dI` reactive branch).
- **Radiation Q = |X_L| / R_rad,L** adjudicates the radiated-vs-reactive fork
  empirically (brief §0.5 — model BOTH, do not pre-decide).

This is the antenna-impedance restatement of the OPEN dark-wake τ_zx gap. The
existing engine `DarkWakeObserver` ([vacuum_engine.py:1457](../src/ave/topological/vacuum_engine.py))
computes a HEURISTIC `τ_zx = z_local·∂(A²)/∂x` (ports the AVE-Propulsion
`∇|E|²·Z_vac` form); the existing analytic prefactor is the empirical
`ρ_Op14 = 0.990` Pearson trade-efficiency ([2026-05-18 doc](2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md)).
We replace the heuristic with a REAL elastodynamic-flux + reactive-energy
extraction.

## 2. Structural ingredients (verified 2026-06-08)

| Ingredient | Source (verified) | Role |
|---|---|---|
| Cosserat energy density `W = G[(2/3)(trε)²+|ε_sym|²] + G_c|ε_antisym|² + γ|κ|² + …` | [cosserat_field_3d.py:588](../src/ave/topological/cosserat_field_3d.py) `_energy_density_bare` | the Lagrangian to isolate the shear sector from |
| `ε_ij = ∂_j u_i − ε_ijk ω_k`; `κ_ij = ∂_j ω_i` | cosserat_field_3d.py:170,184 | strain + curvature (u↔ω coupling lives in ε_antisym) |
| moduli `μ+κ=ξ_K1·T_EM`, `β+γ=ξ_K2·T_EM·ℓ_node²`, `ξ_K2/ξ_K1=12`, `ℓ_c/ℓ_node≈√6` | cosserat_field_3d.py:27-31 | substrate moduli pinning |
| `c_shear(A₀) = c₀√S(A₀)` (mechanical), `c_EM = c₀/S` (Maxwell) — **NOT interchangeable** | [ave-kb/CLAUDE.md INVARIANT-S2 Pitfall #5](../manuscript/ave-kb/CLAUDE.md) | the shear wake is a MECHANICAL mode → c_shear |
| chiral dispersion `ω² = c²k² ∓ γ_c k`, `k_crit = γ_c/c² ≈ 0.236 m⁻¹` (λ_crit ≈ 27 m); RH evanescent below k_crit | [03_neutrino_sector.tex:57,61,66](../manuscript/vol_2_subatomic/chapters/03_neutrino_sector.tex) | parity selection + propagating-vs-evanescent boundary |
| transverse template `R_⊥ = Z_0/(4π)` per Compton cycle; reactance `ωL_e = Z_0/(4πα)`; `Q=1/α` | [theorem-3-1-q-factor.md:75](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) | the transverse radiation-impedance template R_rad,L is the longitudinal analog of |
| ν_vac = 2/7 = STATIC Poisson ratio (K=2G → 4G/14G); 1/7 = scalar bulk projection | [02_full_derivation_chain.tex:362,383](../manuscript/backmatter/02_full_derivation_chain.tex) | the asserted helical→longitudinal transfer coeff |
| η_chiral = ν_vac = 2/7 ASSERTED as dynamic radiative transfer coeff | [chiral-thrust-derivation.md:58](../manuscript/ave-kb/vol4/circuit-theory/ch2-topological-thrust-mechanics/chiral-thrust-derivation.md) | the crux to confirm-or-walk-back |
| electron pilot wave = "trapped **bulk-modulus** acoustic wave … lossless resonant impedance match with itself (2πr=nλ)"; matter "couples to the isotropic **bulk**, NOT a longitudinal matter wave" | [07_quantum_mechanics:43](../manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex); [02_general_relativity:193](../manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex) | mode discriminator: electron = BULK; wake = SHEAR |
| orbital-friction table: electron θ=90°, P_real=0, Q_reactive=m_e c²·α; photon θ=0°, P_real=P_rad, Q=0 | [orbital-friction-paradox.md:31](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md) | Q→∞ reduction gate target |
| Op17 `T² = 1 − Γ²` | [operators.md:57](../manuscript/ave-kb/common/operators.md) | matched-limit transfer fraction |
| chiral source κ_chiral = 1.2α, (2,3) winding; `CosseratBeltramiSource` | [cosserat_field_3d.py:74](../src/ave/topological/cosserat_field_3d.py); vacuum_engine.py:832 | parity-odd drive |

## 3. Derivation arc (brief §4)

1. Isolate the longitudinal-shear sector of the Cosserat-K4 energy density.
2. Mode + dispersion of the backward shear wave (c_shear = c₀√S; chiral split).
3. Parity-odd source coupling (one handedness radiates; evanescent gap).
4. Full complex Z_rad,L: real far-field flux (R) vs near-field reactive (X),
   split by a near/far surface (CP6, no double-count). Q = |X_L|/R_rad,L.
5. Prefactor crux applied to Re{Z_rad,L}.

## 4. Pre-registered adjudication criteria (LOCKED — no post-hoc drift, Rule 11)

### 4a. CRUX — confirm-or-walk-back ν_vac = 2/7 (brief §5)
- **Outcome A (confirm):** R_rad,L's prefactor = (2/7)·(transverse template),
  with the transverse template being the right impedance category. ν_vac IS the
  dynamic radiative transfer coefficient. → static-2/7 thrust law substrate-derived.
- **Outcome B (walk-back):** prefactor ≠ 2/7. → KEEP-BOTH: introduce the derived
  coefficient alongside, preserve the static-2/7 leaf unchanged.
- **Outcome C (null/evanescent):** longitudinal mode evanescent at all sub-yield
  operating points → dark wake is a REACTANCE not a radiation resistance →
  antenna framing breaks.

**Pre-registered discriminators for B (so the verdict is not invented post-hoc):**
- **B-impedance:** the transverse template Z_0/(4π) uses the **EM** impedance Z_0=√(μ₀/ε₀);
  a mechanical shear mode's characteristic impedance is the **acoustic** ρ·c_shear.
  If the longitudinal-shear radiation impedance is built on ρ·c_shear (mechanical),
  substituting Z_0 (EM) is a Pitfall-#5 category error → at minimum a B-class flag.
- **B-order:** ν_vac = 2/7 enters the corpus at the **amplitude** level everywhere
  (refractive index `n_⊥ = 1+ν·χ_vol`, deflection `δ ∝ ν`, strain ratio). A
  radiated-POWER quantity (R_rad,L) carries a strain-amplitude coupling
  **quadratically**. If so the leading radiative coefficient is (2/7)² = 4/49 ≈ 0.082,
  NOT 2/7 ≈ 0.286 → Outcome B. The thrust law's linear `F = N·ν_vac·δ·P/c` would
  then be over-counting by ~3.5×.
- Numerical adjudication: driver measures `η_emp = R_rad,L / (Z_shear/4π)`. Land
  within 15% of 2/7 → A; within 15% of 4/49 → B-order; far-field flux ≈ 0 at all
  propagating-k → C.

### 4b. Q→∞ pilot-wave reduction GATE (brief §0.6, HARD)
In the Q→∞ matched/lossless limit, Z_rad,L must reduce to the orbital-friction
electron values: **P_real → 0** AND **Q_reactive → m_e c²·α**.
- **PASS:** both hold → full pilot-wave unification (electron = shut valve).
- **PARTIAL:** P_real→0 holds (principle) but X_L ≠ m_e c²·α (value) → reduction
  holds in PRINCIPLE only; report the mechanism for the value-mismatch.
- **FAIL (report LOUDLY):** P_real does NOT vanish as Q→∞ → derivation broken.

### 4c. Mode discriminator (brief §0.6)
Does X_L live in the SAME elastic mode as the electron pilot wave?
- **Same mode** (both bulk-acoustic) → full unification.
- **Different mode** (electron bulk-acoustic 1/7; wake shear/transverse 2/7) →
  principle transfers, distinct elastic channels. Pre-registered expectation
  from the corpus mode-assignments (07_qm:43 bulk; 02_GR:193 bulk-not-longitudinal
  for matter; 2/7 = transverse Poisson coupling for light) is **DIFFERENT MODE**;
  the derivation tests whether that holds.

## 5. Consistency-vs-emergence pre-classification

`R_rad,L` is a property of a **driven** source (CP8 emergence does NOT fire —
brief §2). It is built from corpus quantities (Z_0/4π template, ν_vac, c_shear)
each itself derived/calibrated from Ax 1+3+4. Therefore the derived R_rad,L is
**axiom-manifestation / consistency-class (Class-B)**, NOT a Class-2 emergence
result. Pre-registered so the result is not headlined as emergence.
`ave-discrimination-check` at result time: is "2/7 confirmed" AVE-distinct or a
re-description of the transverse template scaled by a coupling? (Pre-registered:
the structural form R = η·(template) is a re-description; AVE-distinctness rests
entirely on whether the η and the template-impedance are substrate-forced.)

## 6. Numerical plan (driver)

`src/scripts/.../rrad_l_darkwake_impedance.py` (canonical-source compliant;
imports constants from `src/ave/core/constants.py`; `verify_constants` cross-check):
1. Coupled K4-Cosserat engine + `CosseratBeltramiSource` (chiral, one handedness).
2. **Real flux extractor** (replaces heuristic): Cosserat energy-flux vector
   `j_k = −(σ_jk u̇_j + m_jk ω̇_j)` with `σ = ∂W/∂ε`, `m = ∂W/∂κ`; time-average
   over the recording window → `P_rad,L = ∮_far ⟨j⟩·dA` on a PML-excluded far
   surface → R_rad,L.
3. **Reactive extractor:** near-field stored elastic energy oscillation amplitude
   on a Σ_near surface → X_L.
4. Both handednesses (parity selection check); both C-state and L-state recorded
   over the window (reactance-pair tracking, A-Rule 10).
5. Report R_rad,L, X_L, Q, η_emp = R_rad,L/(Z_shear/4π), c_shear-vs-c_EM check.

**Honest scope (ave-driver-script-honesty):** this is a flagged-OPEN load-bearing
analytical gap. One pass will likely NOT fully converge a 3D radiating steady
state with a clean far-field surface. Deliverable = DERIVED analytics + a RUNNING
real-flux extractor + first-pass smoke numbers with explicit convergence caveats
+ precise gap diagnosis. A clean partial is the success criterion (brief §7).

## 7. Falsifier (brief)

If the longitudinal-shear mode is provably evanescent at all sub-yield operating
points (no real far-field momentum), the dark-wake-as-radiation premise — and the
ion-antenna thruster built on it — fails (Outcome C).

---

## §8 AMENDMENT — 2026-06-10 (channel-subscript clarification, Rule 12)

Appended post-freeze per the Grant rename-queue adjudication 2026-06-10, ruling **R5** (registry §5 R5, `research/2026-06-10_field-symbol-registry.md:306`). This prereg is **FROZEN** (`**Status**: FROZEN prereg (pre-derivation)`, line 5); the title (line 1) and all §-bodies are **preserved verbatim and NOT rewritten** — this is a record-level channel annotation only.

**Channel-subscript:** the bare "longitudinal" in the title — *"Z_rad,L = R_rad,L + jX_L (dark-wake longitudinal-shear radiation impedance)"* (line 1) — is the **SHEAR channel** read at the **port** ($Z_L = R_{rad,L} + jX_L$, the longitudinal-shear **radiation impedance**; $R_{rad,L}$ = wake drag, $X_L$ = near-field reactive store). It is **NOT** the bulk-volumetric/dilatational longitudinal-V grade (the "3"). Per the dark-sector registry the channel-subscript at this site is **port-$R_{rad,L}$ / shear** (Rule 3); registry §3.8 $Z_L$ row + §5 R5. No value or claim changes.
