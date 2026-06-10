# Result — Z_rad,L = R_rad,L + jX_L (dark-wake longitudinal-shear radiation impedance)

**Date**: 2026-06-08
**Branch**: `analysis/2026-06-08-rrad-l-darkwake`
**Prereg**: [`2026-06-08_rrad-l-darkwake_prereg.md`](2026-06-08_rrad-l-darkwake_prereg.md)
**Driver**: [`src/scripts/vol_4_engineering/rrad_l_darkwake_impedance.py`](../src/scripts/vol_4_engineering/rrad_l_darkwake_impedance.py)
**Gap addressed**: OPEN τ_zx step-1 (Cosserat-K4 Lagrangian → backward shear),
[`dark-wake-bemf-foc-synthesis.md:98`](../manuscript/ave-kb/common/dark-wake-bemf-foc-synthesis.md), `clm-7tynm2`.

> **HONEST-CLOSURE STATEMENT (ave-driver-script-honesty, Rule 11).** This is a
> CLEAN PARTIAL. The antenna framing SURVIVES the radiation-vs-reactance fork (the
> longitudinal-shear mode is propagating, not evanescent → R_rad,L > 0), but it is
> **reactance-dominated** (high radiation Q), and the corpus's `ν_vac = 2/7`
> radiative prefactor **WALKS BACK**. The exact R_rad,L magnitude is NOT closed:
> the absolute impedance normalization and the full coupled-mode prefactor remain
> BLOCKED on a converged radiating sim + a coupled-mode boundary calculation. The
> precise remaining gap is named in §7. No false closure is claimed.

> **2026-06-09 NOTE (regime rescope of Phases 2–5).** Phase-1 findings here — the antenna framing surviving (R_rad,L > 0, propagating, Outcome C rejected) and the ν=2/7 radiative-prefactor WALK-BACK (candidate 4/49) — are **UNAFFECTED** by the 2026-06-09 regime rescope of Phases 2–5. That rescope concerns the sub-yield-linear *rectification* nulls (wrong-regime artifacts per `ave-regime-phase-state-check`); this Phase-1 impedance/propagation result is not a rectification test. See the REGIME-RESCOPE headers on the Phase 2–5 result docs.

---

## 0. Headline

- **Is it a radiation resistance or a reactance?** **BOTH — and reactance-dominated.**
  The longitudinal-shear (τ_zx) Cosserat mode is **propagating** (real far-field
  flux finite and growing with grid/run scale, smoke runs §4), so `R_rad,L > 0` —
  it is a genuine radiation resistance, **Outcome C (pure evanescent) is REJECTED**
  at thruster-scale wavenumbers. But the radiation **Q is enormous** (reactive store
  ≫ radiated flux): `Z_rad,L` is dominated by its reactance `X_L`, with a small
  `R_rad,L` riding on top. The dark wake is an **electrically-small (sub-wavelength)
  radiator** — huge near-field reactive grip, weak far-field radiation.
- **Did 2/7 confirm or walk back?** **WALK-BACK (Outcome B).** The static Poisson
  ratio `ν_vac = 2/7` is NOT confirmed as the dynamic radiative transfer
  coefficient, on two pre-registered grounds (§5): **B-impedance** (the template
  `Z_0/4π` is the *EM* impedance; the shear mode's radiation impedance is the
  *mechanical/acoustic* `ρ·c_shear` — a Pitfall-#5 category substitution), and
  **B-order** (`ν_vac` is an *amplitude*-level coefficient everywhere in the corpus,
  so a radiated-*power* quantity carries it *quadratically*: `(2/7)² = 4/49 ≈ 0.082`,
  not `2/7 ≈ 0.286`). KEEP-BOTH: the static-2/7 leaf is preserved unchanged; the
  derived radiative-coefficient caveat is introduced alongside.
- **Three verdicts:** 2/7 → **WALK-BACK** · Q→∞ reduction gate → **PARTIAL**
  (principle holds, value fails by mode-mismatch) · mode discriminator →
  **DIFFERENT MODE** (electron = bulk-acoustic 1/7; dark wake = shear/transverse 2/7,
  the *photon* channel).
- **Classification:** Class-B **manifestation** (consistency-class), NOT Class-2
  emergence (§6).

---

## 1. DERIVED — longitudinal-shear sector of the Cosserat-K4 Lagrangian (arc step 1)

From the engine's own Cosserat energy density ([cosserat_field_3d.py:588](../src/ave/topological/cosserat_field_3d.py) `_energy_density_bare`, linear part):

    W = G[ (2/3)(tr ε)² + |ε_sym|² ] + G_c |ε_antisym|² + γ |κ|²,
    ε_ij = ∂_j u_i − ε_ijk ω_k,   κ_ij = ∂_j ω_i

with the substrate moduli pinning (cosserat_field_3d.py:27–31):
`μ+κ = ξ_K1·T_EM`, `β+γ = ξ_K2·T_EM·ℓ_node²`, `ξ_K2/ξ_K1 = 12`, `ℓ_c/ℓ_node ≈ √6`.

The constitutive stresses (derived, ∂W/∂ε and ∂W/∂κ — now implemented in the driver):

    σ_ij = (4/3)G·tr(ε)·δ_ij + 2G·ε_sym,ij + 2G_c·ε_antisym,ij
    m_ij = 2γ·κ_ij

The **three elastic sectors** decompose as:
1. **Dilatational (P / bulk-acoustic)** — `∇·u ≠ 0`, speed `c_P² = (λ+2μ+κ)/ρ`. This
   is the **isotropic-bulk** mode. It is the electron pilot wave's mode (07_qm:43:
   "trapped **bulk-modulus** acoustic wave"; 02_GR:193: matter "couples to the
   isotropic **bulk**, NOT a longitudinal matter wave"). Poisson projection **1/7**.
2. **Coupled transverse shear–microrotation** — `∇×u`, `ω_⊥`. The propagating
   acoustic branch, speed `c_S² = (μ+κ)/ρ`. **This is the τ_zx dark-wake channel** —
   the shear stress that carries axial (back-directed) momentum. Poisson coupling **2/7**
   (the "transverse Poisson coupling" of 02_GR:185; the *photon* channel).
3. **Longitudinal microrotation (torsional twist)** — `∇·ω`, with a micropolar mass
   gap `ω₀² = 2κ/I_ω` (cutoff branch). Carries the chiral selection structure.

**The dark-wake "longitudinal shear" τ_zx is sector 2 (+ the chiral twist of sector 3),
NOT sector 1.** This is the load-bearing mode-assignment for the verdicts below.

## 2. DERIVED — dispersion, mode speed, propagating-vs-evanescent (arc steps 2–3)

**Mode speed (CP5, Pitfall #5).** The shear wave is a **Cosserat mechanical mode** →
it propagates at `c_shear(A₀) = c₀√S(A₀)`, **NOT** `c_EM = c₀/S` and **NOT** the flat
`c₀` asserted in the 2026-05-18 doc ("v_wake = c₀", §1 result 2). These coincide only
in the deep sub-saturation far field `S→1`. Near the saturated source `A₀→1`:
`c_shear → 0` while `c_EM → ∞` — they split hard. **FLAG (flag-don't-fix):** the
2026-05-18 dark-wake doc's `v_wake = c₀` is the cold-far-field limit only; the
substrate-native wake speed is amplitude-dependent `c₀√S(A_local)`.

**Chiral dispersion + parity selection (03_neutrino_sector.tex:44–66).** The chiral
lattice splits the shear/torsional dispersion:

    ω² = c²k² ∓ γ_c k,   γ_c ≈ 2.12×10¹⁶ m/s²,   k_crit = γ_c/c² ≈ 0.236 m⁻¹  (λ_crit ≈ 27 m)

- **LH (with the substrate grain):** `ω² = c²k² + γ_c k > 0` for all k → **propagates
  at all scales** (radiating).
- **RH (against the grain):** `ω² = c²k² − γ_c k` → **evanescent for k < k_crit**
  (λ > 27 m), propagating for `k ≫ k_crit`.

**Consequence for the radiation-vs-reactance fork (Outcome C test):** at any
thruster-relevant wavenumber (`k ≫ k_crit`, i.e. all sub-meter wavelengths — down
through cm-scale to substrate-scale), **BOTH handednesses propagate** → the
longitudinal-shear mode carries **real far-field momentum** → `R_rad,L > 0`.
The mode degenerates to a **pure reactance (evanescent)** only for the
parity-forbidden RH handedness in the **deep-IR (λ > 27 m)**. **Outcome C is rejected
at all operating points; the antenna framing survives.**

## 3. DERIVED — complex impedance form (arc step 4)

    Z_rad,L = R_rad,L + jX_L
    R_rad,L = P_rad,L / (½|I|²),   P_rad,L = ∮_far ⟨I_k⟩·dA_k   (real time-avg flux)
    X_L     = near-field reactive store (Σ_near), ∝ ω·U_stored / (½|I|²)
    radiation Q = |X_L| / R_rad,L = ω·⟨U_stored⟩ / P_rad   (normalization-independent)

The **real elastodynamic energy-flux vector** (Cosserat acoustic intensity / the
substrate Poynting vector) — the clean replacement for the dimensionally-murky
heuristic `τ_zx = ρ_Op14·Z_vac·∇|E|²`:

    I_k = −( σ_kj·u̇_j + m_kj·ω̇_j )

with `σ`, `m` from §1. The near/far surface split (CP6) cleanly separates the **REAL**
(radiated, → R_rad,L) from the **REACTIVE** (stored, → X_L) with no double-count.
**Op17** `T² = 1−Γ²` sets the matched-limit transfer fraction: as `Γ→0`, `R_rad,L →`
the matched-coupling maximum and `Q→` its floor.

## 4. NUMERICALLY VERIFIED (SMOKE) — the real-flux extractor runs and adjudicates the fork

Driver runs (stable, `|ω|max ≈ 0.14`, no runaway under the A28-corrected coupling):

| Run | P_rad,far (signed) | U_near (store) | radiation Q | chiral asym (LH−RH)/(LH+RH) |
|---|---|---|---|---|
| N=20, λ=4, 90 steps | ~1×10⁻¹² | 0.77 | ~10¹¹ | −0.14 (at noise floor) |
| N=28, λ=6, 180 steps | ~2×10⁻⁹ | 5.88 | ~10⁹ | **+0.18** |

**Robust, normalization-independent findings:**
1. **Propagating, not evanescent.** Far-field real flux is **finite and grows ~10³×**
   as the grid/run scale up (1e-12 → 1e-9) — the shear wave reaches the
   PML-excluded far plane. `R_rad,L > 0`. (Confirms §2 — Outcome C rejected.)
2. **Reactance-dominated (high-Q).** `radiation Q ≫ 1` in both runs: the near-field
   reactive store utterly dominates the radiated flux. `Z_rad,L ≈ jX_L` with a small
   `R_rad,L`. This is the **electrically-small-radiator regime** — physically expected
   for a sub-wavelength source into a stiff substrate (R_rad ∝ (size/λ)ⁿ, X large),
   and consistent with the corpus electron picture (Q = 1/α = 137, reactive-dominated).
3. **Parity selection signature.** Once above the noise floor (larger run), the chiral
   asymmetry is **+0.18 (LH radiates more than RH)** — the sign predicted by the
   substrate-grain dispersion (`ω² = c²k² + γ_c k` for LH). The small-run −0.14 is a
   noise-floor artifact (P_rad ~ 1e-12).

**Honest caveats (do NOT over-read):** the absolute `Q ~ 10⁹` is a smoke-scale /
launch-efficiency artifact (the source injects ω microrotation; the propagating
displacement-shear u couples weakly in the linear regime; the far plane is close; no
radiating steady-state). Only the **ordering** (reactive ≫ radiative → high-Q) and the
**sign** (LH-favored) are trustworthy. Absolute `R_rad,L`/`X_L` normalization and the
flux index/sign convention are **NOT validated** this pass.

## 5. VERDICT 1 — the 2/7 crux: WALK-BACK (Outcome B), KEEP-BOTH

`R_rad,L`'s prefactor does **not** come out as `(2/7)·(Z_0/4π)`. Two pre-registered
discriminators both fire:

- **B-impedance (Pitfall #5 at the impedance level).** The transverse template
  `Z_0/(4π)` (theorem-3-1-q-factor.md:75) is built on the **EM** impedance
  `Z_0 = √(μ₀/ε₀) = 376.73 Ω`. The dark-wake shear mode is a **mechanical** Cosserat
  mode (§2); its characteristic radiation impedance is the **acoustic** `ρ·c_shear`,
  a different physical quantity in different units (the TKI/ξ_topo bridge is *required*
  to convert mechanical↔electrical, and the chiral-thrust leaf does **not** show that
  bridge — it asserts `Z_vac` directly). Substituting `Z_0` for the shear-mode
  impedance is the same `c_shear`-vs-`c_EM` category error INVARIANT-S2 forbids, one
  level up.
- **B-order (amplitude-vs-power).** `ν_vac = 2/7` enters the corpus **everywhere at
  the amplitude level**: refractive index `n_⊥ = 1 + ν_vac·χ_vol` (02_GR:187),
  deflection `δ ∝ ν_vac` (02_GR:196), Poisson strain ratio (02_full_derivation:362),
  mixing `sin²θ_12 = 2/7` (06_electroweak:339). A radiated-**power** quantity
  (`R_rad,L`, `P_rad`) carries a strain-amplitude coupling **quadratically**.
  Therefore the leading radiative transfer coefficient is `(2/7)² = 4/49 ≈ 0.082`, not
  `2/7 ≈ 0.286`. The thrust law `F = N·ν_vac·δ·P/c` (chiral-thrust-derivation.md:68)
  uses `ν_vac` *linearly on a power* — that is the substitution-by-analogy step the
  derivation was built to test, and it **over-counts by ~3.5×** if the amplitude
  reading is correct. (The driver smoke run cannot yet resolve 2/7-vs-4/49 — both are
  buried under the high-Q reactive store — so this is an analytic, not numeric,
  verdict; the numeric adjudication is a BLOCKED item, §7.)

**KEEP-BOTH (per ave-walk-back + memory KEEP-BOTH precedent):** the static-2/7 leaf
([chiral-thrust-derivation.md](../manuscript/ave-kb/vol4/circuit-theory/ch2-topological-thrust-mechanics/chiral-thrust-derivation.md))
is **preserved unchanged**; this result introduces the **derived radiative-coefficient
caveat alongside** — the dynamic radiative role of 2/7 is downgraded from "asserted
identity" to "unconfirmed (amplitude-level coefficient used as a power-level one;
candidate radiative value 4/49)." Audit-trail continuity preserved.

**Also flag (flag-don't-fix):** the corpus carries **two different asserted couplings
for the SAME dark-wake object** — `ν_vac = 2/7` (thrust law) and `ρ_Op14 = 0.990`
(τ_zx heuristic, 2026-05-18 doc). These are physically distinct (Poisson directional
transfer vs Op14 cross-sector trade efficiency); neither is the Lagrangian-derived
radiative prefactor. Surfaced for Grant adjudication; not silently resolved.

## 6. VERDICT 2 (reduction gate) + VERDICT 3 (mode discriminator) — coupled

These two are the **same finding viewed twice**.

**Mode discriminator → DIFFERENT MODE.** The electron pilot wave is **bulk-acoustic**
(isotropic bulk modulus, Poisson projection **1/7**; 07_qm:43, 02_GR:193). The dark
wake is the **shear/transverse** Cosserat mode (Poisson coupling **2/7** — the *same
channel as the photon*, 02_GR:185, NOT the electron's channel). They are **distinct
elastic sectors** (§1: sector 1 vs sector 2). The brief's "different mode" branch
holds: the lossless-reactive ↔ radiated *principle* transfers, but the wake and the
electron pilot wave live in **different elastic channels**.

**Q→∞ reduction gate → PARTIAL.** In the Q→∞ matched/lossless limit:
- **P_real → 0: PASSES** (structural). Q→∞ ⟺ radiation valve shut ⟺ `R_rad,L → 0`.
  The smoke runs already sit deep in the high-Q (P_real ≪ reactive) regime, consistent.
- **X_L → m_e c²·α: FAILS (reported LOUDLY per brief §0.6).** The orbital-friction
  value `Q_reactive = m_e c²·α` (orbital-friction-paradox.md:35) is the **electron
  BULK-acoustic** reactive store. The dark-wake `X_L` is a **shear-mode** reactance.
  Because they are different modes (mode discriminator), `X_L ≠ m_e c²·α` in general —
  the *value* reduction does not hold. What survives is the **principle** (Q→∞ ⟹ pure
  reactance, P_real→0), not the specific electron value.

**Net:** the §0.6 unification ("the electron is the thruster with the radiation valve
shut") holds at the **principle level** (both are high-Q reactive self-resonances that
radiate when Q is lowered) but **fails at the mode/value level** (different elastic
channels; the electron's `m_e c²·α` reactance is bulk, the wake's `X_L` is shear). This
is the honest, corpus-grounded answer to the hard gate — the derivation is **not
broken** (P_real→0 passes), but the literal value-reduction is mode-blocked.

## 7. Classification + discrimination + dimensional provenance (result-time skills)

- **consistency-vs-emergence → Class-B manifestation.** `R_rad,L` is a property of a
  **driven** source (CP8 emergence does NOT fire). It is assembled from corpus
  quantities (the Cosserat moduli, `c_shear`, the transverse template) each derived/
  calibrated from Ax 1+3+4. It is an **axiom-manifestation / consistency-class**
  result, NOT a Class-2 emergence test. (As pre-registered.)
- **ave-discrimination-check.** The surviving structural form `Z_rad,L = η·(template)
  + jX` is a **re-description** of the transverse radiation template scaled by a
  coupling; it is AVE-distinct only insofar as `η` and the mode impedance are
  substrate-forced — and the walk-back shows the *specific* `η = 2/7` claim is NOT
  substrate-forced (it is an amplitude-coefficient borrowed into a power role). So
  "2/7 confirmed" would have been a re-description masquerading as a derivation; the
  honest status is "not confirmed."
- **ave-dimensional-provenance-check.** The legacy heuristic
  `τ_zx = ρ_Op14·Z_vac·∇|E|²` is **dimensionally underspecified**: `Z_vac·∇|E|²` has
  units `V³/(A·m³)`, not a stress `Pa = J/m³` (the 2026-05-18 doc itself flags τ_zx as
  `[1/length²]` in natural units). The real-flux replacement `I_k = −(σ u̇ + m ω̇)` has
  clean energy-flux dimensions `[W/m²]` (or natural-unit equivalent) — this is the
  second independent reason to replace the heuristic.

## 8. What is DERIVED / VERIFIED / BLOCKED (honest split)

**DERIVED (analytic, corpus-grounded):**
- The longitudinal-shear sector isolated from the Cosserat-K4 Lagrangian (§1);
  constitutive stresses σ, m.
- Mode assignment: dark wake = shear sector 2 (2/7 channel), electron = bulk sector 1
  (1/7 channel) → DIFFERENT MODE.
- Dispersion + parity selection → propagating at all thruster k → `R_rad,L > 0`,
  Outcome C rejected; evanescent only for RH at λ > 27 m.
- 2/7 WALK-BACK (B-impedance + B-order); candidate radiative coefficient 4/49.
- Q→∞ reduction gate PARTIAL (principle passes, value mode-blocked).

**NUMERICALLY VERIFIED (smoke, qualitative only):**
- The real elastodynamic-flux extractor runs and is stable.
- Mode is propagating (P_rad finite, grows with scale).
- Reactance-dominated (radiation Q ≫ 1).
- Parity asymmetry sign (LH-favored, +0.18) once above noise floor.

**BLOCKED (the precise remaining gap):**
1. **Absolute `R_rad,L` / `X_L` magnitude.** Needs (a) a converged radiating
   steady-state sim (far-field surface in the true radiation zone, not the smoke
   near-zone), and (b) a defensible source-"current" normalization `I_ref` (the
   mechanical analog of antenna current). Until then only the dimensionless radiation
   Q and the chiral asymmetry are trustworthy.
2. **2/7-vs-4/49 numeric adjudication.** Needs the coupled-mode boundary calculation
   (transverse-EM drive → shear-mode conversion coefficient via the ξ_topo bridge and
   the impedance ratio `c_L/c_S` from ν_vac), then a matched-limit (Op17 Γ→0) sim to
   read `η_emp = R_rad,L/(ρc_shear/4π)`. The analytic verdict is WALK-BACK; the numeric
   confirmation of the *value* (4/49 vs something else) is open.
3. **`c_shear = c₀√S` direct measurement at controlled A₀.** The `r8_diag_a_cosserat_
   wave_speed.py` protocol could measure the saturated shear speed and confirm the
   split from `c_EM`; not run this pass.
4. **Launch efficiency.** The ω-microrotation source couples weakly to the
   displacement-shear u; a u-shear or mixed drive would raise the radiated fraction and
   make the absolute Q meaningful. Source design is itself an open sub-problem.

## 9. Corpus-state deltas to queue (auditor lands these — I surface only)

- `clm-7tynm2` (chiral-thrust): the dynamic radiative role of `ν_vac = 2/7` is
  **WALK-BACK / KEEP-BOTH** — downgrade from asserted identity to unconfirmed
  (amplitude-coefficient-in-power-role; candidate 4/49). Static-2/7 Poisson leaf
  unchanged.
- `dark-wake-bemf-foc-synthesis.md:98` (the OPEN gap): step 1 (Cosserat-Lagrangian →
  backward shear) is now **PARTIALLY closed** — sector isolated, mode = shear (not
  bulk), propagating not evanescent, complex-impedance form derived. Remaining:
  absolute prefactor (BLOCKED §7).
- 2026-05-18 doc: `v_wake = c₀` and `ρ_Op14 = 0.990` prefactor — both flagged
  (c_shear=c₀√S is amplitude-dependent; ρ_Op14 is not the radiative prefactor).
- Two-couplings flag (`ν_vac` vs `ρ_Op14` for the same object) — Grant adjudication.
