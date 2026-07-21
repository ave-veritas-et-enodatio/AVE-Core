# Boundary-Strain Amplitude — FROZEN PRE-REGISTRATION (the Fork-W conditional's single computation)

**Date:** 2026-07-21
**Class:** DERIVATION + lattice-derived research-driver PRE-REGISTRATION (research-doc). Freezes the observable, the corpus-admissible breather-profile family, the bins, the margin, and the three-leg method — **NO verdict**. Discharges the owed follow-on registered by merged **#773** (`research/2026-07-20_forkw-kernel-keying_derivation.md` §4(a), §4(b) [NOT-YET-RATIFIABLE], §2 Step 2 ★caveat; docket `### ENTRY 2026-07-20-forkw-kernel-keying` review-repair **R2** verbatim: *"OWED (the single computation Fork-W now hinges on): the core-boundary transverse-vs-axial swing-amplitude, vs yield, for the actual srs breather envelope."*).
**Provenance:** Grant standing derivation-class authorization (the #773 §4(a) owed follow-on). This is **COMMIT 1 = the prereg ALONE**, pushed before any driver runs. Criteria committed first; the numeric verdict-controlling Leg B is built + run only after this freezes. Every `[canon]`/engine cite content-verified two-method (`grep -F`/`sed` + direct read) at base HEAD `3d07ceeb` (`origin/main` #777).
**Lane fences:** DERIVATION lane only. Engine `src/ave` BYTE-UNTOUCHED (driver lives in `research/drivers/`); **no** `manuscript/`/`ave-kb/` leaf edit; **no** port-register / falsification-ledger edit; canonizes nothing; mints no `clm-`/`def-`; propagates to no KB/tex leaf — regardless of outcome (held). DO-NOT-MERGE PR.

---

## §0 — SUBSTRATE-FIRST SECTOR / REGIME / PHASE-STATE header (fired before any standard-physics term)

**SECTOR.** Under test = the TRANSLATIONAL (Cauchy-grade) vector sector of the chiral srs-z3 net (`ave.core.chiral_lattice._SRS_8A`/`_SRS_NN`; `I4₁32`, Wyckoff-8a, z=3). Rank-2 per-bond tensor `Φ_b = k_a·(d̂⊗d̂) + k_s·(I − d̂⊗d̂)` — **NOT** a Cartesian Laplacian; Rule-14 reuse of the #770/#775 `constituent_cage_ensemble` bond model. The two stiffnesses are keyed on **orthogonal swing coordinates** (#773 §2 Step 3, `[canon-read]` `axiom-register.md:186/189/193`): `k_a` on the **axial** bond swing `d̂·du_b`, `k_s` on the **transverse** bond swing `(I−d̂d̂)·du_b`. mass = A1 dilatation-breather (`master-equation.md:20` `[canon]`, the two-"3"s banner: *"the A1 dilatation-MASS … the A1 breather"*); charge/spin = Cosserat `(2,3)` winding — A1 ⊥ T2, NOT cross-wired.

**REGIME.** Near-yield SATURATED localized A1 breather core embedded in cold-linear exterior. The object is a **LOCALIZED** radial breather `u = f(r) r̂`, NOT the uniform (affine) dilatation for which #773's mode-orthogonality is already derived.

**PHASE-STATE.** The question is **KINEMATIC** — the strain decomposition of a GIVEN displacement profile, not envelope self-consistency. Op14 saturation is NOT run dynamically; we measure the per-bond axial and transverse **swing amplitudes** the kernel *would* key on, for an imposed profile, and compare to yield. **★Scope honesty (declared, held):** a kinematically-imposed envelope is admissible HERE precisely because the observable is a strain-decomposition of a fixed profile (a self-bound saturated soliton is INFEASIBLE on the lossless engine — electron-lock arc; and self-consistency is NOT what Fork-W hinges on). This is stated as scope, not hidden.

**COORDS (A46 discipline — `phase-space-coordinate-check` FIRED: PASS).** The corpus claim under test (#773 §2 Step 2, §4b) is stated in **real-space strain coordinates**: `ε_rr = f′`, `ε_θθ = ε_φφ = f/r`, deviatoric `∝ (f′ − f/r)`, exterior `f ~ A/r²` pure-deviatoric. The test measures in the **matching** real-space per-bond strain-decomposition coordinates (axial swing vs transverse swing). This is genuinely a real-space kinematics question — NOT a phase-space (V_inc/V_ref, Clifford-torus winding) claim; there is no φ²-vs-Cartesian mismatch. Coordinates MATCH.

**CLASS (`consistency-vs-emergence` FIRED).** The observable `ρ_dev` is a pure **dimensionless kinematic ratio** (α-CLEAN; no `ave.core.constants`, no CODATA, no `Q_TANK`). Leg A is an **exact geometric IDENTITY** (spherical-elasticity kinematics of a named profile); Leg B is a lattice-derived MANIFESTATION of that identity on the discrete srs net; Leg C reads a `[canon]` remap (`axiom-register.md:193`) at the measured tension. **No emergence-class claim is headlined.** Every VALUE ships dimensionless with its computation.

---

## §1 — THE FROZEN OBSERVABLE

For a localized radial breather `u = f(r) r̂`, define per bond `b` (endpoints `i,j`, direction `d̂_b`, relative displacement `du_b = u_j − u_i`):

- **axial swing** (the coordinate `k_a` keys on): `A_axial(b) = |d̂_b · du_b|`
- **transverse swing** (the coordinate `k_s` keys on, per #773 §2 Step 3 / the `(I−d̂d̂)` projector): `A_trans(b) = |(I − d̂_b⊗d̂_b) · du_b|`

Bin bonds by midpoint radius `r_b = |mid_b − c_core|`. Per radial shell, take RMS over the shell's bonds: `Ā_axial(r)`, `Ā_trans(r)`.

**FROZEN observable — the deviatoric-to-axial swing ratio profile and its shell value:**

$$\rho_{\rm dev}(r) \;\equiv\; \frac{\bar A_{\rm trans}(r)}{\bar A_{\rm axial}(r)}, \qquad \textbf{verdict datum} = \rho_{\rm dev}(r_{\rm sat}) \ \text{and}\ \frac{\max_r \bar A_{\rm trans}(r)}{\bar A_{\rm axial}(r_{\rm sat})}.$$

- **Saturation shell** `r_sat` ≡ the radial bin that **maximizes** `Ā_axial(r)` (the shell where the axial swing first reaches yield as the amplitude is cranked).
- **Normalization** (frozen): scale the imposed amplitude so `Ā_axial(r_sat) = A_yield = 1`. Then everything is in **yield units**, and "boundary deviatoric reaches yield-scale" means `max_r Ā_trans(r) → 1`.

**Two deviatoric measures reported (BOTH frozen; the bin must be robust across both, else the measure-dependence IS the finding — anti-seduction, §5):**
- **MEASURE-1 (PRIMARY — the exact quantity the `k_s` kernel keys on):** the per-bond transverse swing `A_trans(b)` above, measured directly on the srs net (Leg B). This is `k_s`'s literal argument; it already carries the lattice orientation-average and the continuum "max bond shear = ½|f′−f/r|" factor.
- **MEASURE-2 (SECONDARY / conservative upper bound — the continuum deviatoric shape, Leg A):** `|f′ − f/r|` relative to `|f′|` (the raw `#773` "deviatoric ∝ (f′−f/r)" quantity, un-halved).

---

## §2 — THE CORPUS-ADMISSIBLE BREATHER-PROFILE FAMILY (what canon commits; enumerated where it under-determines)

**What canon COMMITS `[canon-read]`:**
1. **mass = interior A1-dilatation** (`master-equation.md:20`): `∇·u ≠ 0` in the core carries the rest mass; the exterior (no mass source) is **divergence-free**.
2. **exterior tail = `f ~ A/r²`** — the *only* decaying divergence-free radial harmonic (Lamé pressurized-cavity form; `∇·u = 0`, pure deviatoric). #773 §2 Step 2 commits this verbatim: *"its exterior/boundary field (`f ~ A/r²`, the pressurized-cavity form) has zero dilatation and pure deviatoric strain."* The gravitomagnetic-analog `A_g ∝ 1/r²` (`gravitomagnetism-frame-dragging.md:15` `[canon]`) is the same harmonic order.
3. **the geometric strain kernel argument decays `A_geom = ℓ_node/r ∝ 1/r`** (`q-g22-strain-convention.md`, `clm-4r4jiy`): the corpus's canonical soliton strain amplitude is a geometric confinement ratio, `∝1/r`, NOT the Coulomb `1/r²` field ratio.

**What canon UNDER-DETERMINES (enumerated admissible family, per the task instruction):** the corpus does **not** pin the *interior* mechanical displacement profile nor the *sharpness* of the core→tail transition. Admissible members (all: localized, `f→0` at ∞, carry net dilatation, div-free `1/r²` exterior), spanning the family from the affine-core to the sharp-boundary limit — with `s = r/r_c`:

| member | `f(s)` | interior | tail | role |
|---|---|---|---|---|
| **smooth-eshelby** (PRIMARY) | `A·s/(s²+1)^{3/2}` | affine (`f∝r`, θ=const) | `→ A/s²` div-free | canonical smooth localized dilatational breather |
| **gaussian-curlfree** | `u = ∇φ, φ=e^{−r²/2σ²}` | dilatational, compact | super-algebraic (seed shape) | the #761/#767/#770 driver seed member |
| **lorentzian** | `A·s/(s²+1)` | affine | `→ A/s` (slower) | slower-tail member |
| **sharp-eshelby** | `A·s` (s<1) hard-matched to `A/s²` (s>1) | affine core | div-free `1/s²`, **strain-discontinuous** | the sharp-boundary LIMIT |

**Analytic bracket (Leg A, exact — these are geometric identities, not the verdict):** for the exact spherical-elasticity kinematics `ε_rr=f′`, `ε_θθ=f/r`,
- **pure affine** (`f∝r`, uniform dilatation): deviatoric `= 0`, `ρ_dev = 0` — the #773 UNIFORM limit where `k_a` rails alone.
- **pure exterior tail** (`f∝1/r²`, div-free): `ρ_dev = |f′−f/r|/|f′| = 3/2` — deviatoric strictly DOMINATES axial.

So the admissible family is bracketed `ρ_dev ∈ [0, 3/2]`; the verdict is WHERE within this bracket the saturation shell falls, which canon under-determines and which Leg B measures on the discrete net.

---

## §3 — THE FROZEN BINS + MARGIN

Normalize each profile so the peak axial swing = `A_yield = 1`. Let `M ≡ max_r Ā_trans(r)` (the peak boundary deviatoric swing, yield units) and `ρ_dev(r_sat)` (the ratio at the axial-saturation shell). Reported for BOTH measures (§1), for EACH admissible profile (§2).

| BIN | frozen criterion | Fork-W consequence |
|---|---|---|
| **(1) K_A-ONLY-FORCED** | `M ≤ 0.5` (peak boundary deviatoric ≤ ½·yield) **for ALL admissible profiles AND both measures** | boundary deviatoric stays sub-yield by the frozen margin ⇒ the #773 §4(b) NOT-YET-RATIFIABLE conditional clause (*"a pure A1 dilatation breather rails `k_a` ALONE"*) becomes **RATIFIABLE** for the localized core |
| **(2) K_S-RAILS-TOO** | `M → 1` (boundary deviatoric at yield-scale) — taken as `M ≥ 0.8` — for the physically-representative (smooth) members | the wall is **NOT forced bulk-only** by the keying; a localized breather rails `k_s` at the shell too ⇒ the channel-asymmetric wall needs a **different carrier** — ROUTE TO GRANT |
| **(3) PROFILE-DEPENDENT** | the bin-1/bin-2 assignment **flips** across the admissible family (§2) OR across the two measures (§1) — e.g. smooth `≤0.5` but sharp-eshelby `≥0.8`, or MEASURE-1 `≤0.5` but MEASURE-2 `≥0.8` | STATE THE FORK: the localized-core `k_a`-alone grade is profile-conditional; canon under-determines the deciding sharpness ⇒ ROUTE TO GRANT with the bracket |
| **(4) UNDETERMINED** | the lattice measurement cannot resolve `M` to within a margin that discriminates 0.5 vs 0.8 (finite-size / binning artifact dominates) | state what box/binning would resolve it |

**Margin is frozen at 0.5** (the task's explicit example: *"peak deviatoric ≤ 0.5·yield when axial = yield"*). The yield-scale bin-2 threshold is frozen at `0.8` (a boundary deviatoric ≥ 80% of yield is "yield-scale"; the interval `(0.5, 0.8)` is a no-clean-bin zone that routes to PROFILE-DEPENDENT / the fork).

---

## §4 — THE THREE FROZEN LEGS (methods frozen; outcomes NOT)

**Leg A — ANALYTIC (exact spherical-elasticity kinematics).** For each admissible `f(r)` (§2), compute `ρ_dev(r) = |f′−f/r|/|f′|` and `θ(r)=f′+2f/r` in closed form; locate `r_sat = argmax|f′|`; report `ρ_dev(r_sat)`, `max|f′−f/r|/max|f′|` (MEASURE-2), and the bond-shear `½·|f′−f/r|` version. The affine=0 / exterior=3/2 bracket is the fence.

**Leg B — NUMERIC (per-bond srs strain decomposition; VERDICT-CONTROLLING).** On `cce.build_finite_srs(L)`, impose each admissible `u = f(r)r̂` (kinematic; NO dynamics, NO pin — §0 scope). Per bond: `A_axial=|d̂·du_b|`, `A_trans=|(I−d̂d̂)·du_b|` (MEASURE-1). Bin by `r_b`; RMS per shell; `r_sat=argmax Ā_axial`; normalize `Ā_axial(r_sat)=1`. Report `ρ_dev(r)` profile, `ρ_dev(r_sat)`, `M=max Ā_trans`, per profile. The **shell-adjacent bins are the verdict data.** Deterministic (no RNG; reruns bit-identical).

**Leg C — THE PRE-STRESS REMAP (sign matters; the #773-flagged countervailing mechanism).** With the per-bond axial tension `T_b = k_a·(d̂·du_b)` measured at the shell, evaluate the `[canon]` remap `k_{shear,eff} = k_s + T_b/ℓ_node` (`axiom-register.md:193`, `[SIGN-RULE-DERIVED]`; `ℓ_node = _SRS_NN`) per shell bond. Report: (i) the sign — does the shell-averaged `k_{shear,eff}` **soften** (`T<0`, axial compression ⇒ UNCAPPED, `axiom-register.md:193`) or **stiffen** (`T>0`) shear at the boundary; (ii) the magnitude `⟨k_{shear,eff}⟩/k_s` and the fraction of shell bonds softened; (iii) the per-orientation split (radial-bond vs hoop-bond vs diagonal-bond tension sign). The remap's `[canon]` sign rule: axial end-load ⇒ COMPRESSION ⇒ `k_{shear,eff}` SHRINKS ⇒ softens `k_s` further (reinforces bin-2 if it fires).

---

## §5 — ANTI-SEDUCTION FENCE (both ways; frozen)

**BIN-1 flatters TWO priors at once — fence BOTH.** (i) The #773 *walked picture* WANTS `k_a` alone (clean, `k_s` cold) — bin-1 is its rescue. (ii) The #770/#775 *deep-rail wall model* WANTS the bulk-only `Γ_bulk=−1` wall FORCED — bin-1 lets the keying force it. A single computation that returns bin-1 would validate both seductive narratives simultaneously; that is exactly the shared-blind-spot failure mode. **Fence:** (a) report BOTH deviatoric measures (§1) and require bin-1 robust across both; (b) report the WHOLE admissible family (§2), not one flattering profile; (c) every number ships with its computation + code path in the result JSON; (d) the exterior `ρ_dev=3/2` fence is stated — no localized profile can make the deviatoric strictly negligible, so a bare "k_s cold" is already excluded at the tail; the only live question is whether the axial strain has fallen below yield before the deviatoric reaches yield-scale.

**BIN-2 has a completion-bias too:** the #773 review R2 momentum WANTS the localized core to break the clean story. Fence: bin-2 requires `M ≥ 0.8` for the SMOOTH representative members, not just the sharp-eshelby discontinuity limit (whose 3/2 is a known Eshelby step-artifact); if only the sharp limit fires bin-2, that is PROFILE-DEPENDENT (bin 3), not bin-2.

---

## §6 — GRID / DETERMINISM / REPORT ITEMS (frozen)

- **Grid:** `L = 24` srs cells (matching #775; ~big enough for a clean core+shell separation). Core at box center. Profile scale `r_c` (and Gaussian `σ`) frozen at `2.0` node-spacings; a `r_c ∈ {1.5, 2.0, 3.0}` robustness scan is a frozen REPORT item (does the bin move with core scale within the resolvable band?).
- **Radial binning:** frozen bin width `0.5` node-spacings; shells reported from `r=0` to `r = L/2 − 1`. Saturation shell = the `argmax Ā_axial` bin.
- **Determinism:** no RNG anywhere (pure kinematic imposition + strain read-out); reruns bit-identical (asserted in the result).
- **Figure:** white house style (`ave.viz.style.apply`, Okabe-Ito, honest axes/units, legend outside data, no on-figure title): (L) `ρ_dev(r)` and `Ā_axial(r)`,`Ā_trans(r)` vs `r` for the admissible family, with the `r_sat` shell and the 0.5/0.8 margins marked; (R) the per-profile verdict metric `M` (both measures) vs the 0.5/0.8 bins.
- **Frozen REPORT items (delivered in the result, computed by the driver):** (1) the `r_c` robustness scan; (2) the Leg-C per-orientation tension-sign split; (3) the exterior-tail check that measured `ρ_dev → 3/2` far out (validates the kinematic pipeline against the analytic fence); (4) the dilatation-fraction `∫θ²/∫|ε|²` per profile (confirms the interior is genuinely dilatational).

---

> **Prereg provenance.** Frozen 2026-07-21. Discharges the #773 §4(a) owed follow-on (docket `### ENTRY 2026-07-20-forkw-kernel-keying` R2 — *"the single computation Fork-W now hinges on"*). Base HEAD `3d07ceeb`. This is COMMIT 1 (prereg ALONE); Legs A/B/C land in later commits. Cites verified two-method at base: `axiom-register.md:186/189/193`, `master-equation.md:20/90`, `electron-bh-isomorphism.md:26`, `q-g22-strain-convention.md` (`clm-4r4jiy`), `gravitomagnetism-frame-dragging.md:15`, `constituent_cage_ensemble.py` bond model, `ave.core.chiral_lattice._SRS_8A/_SRS_NN`. Engine `src/ave` byte-untouched; no KB/tex/port-register/ledger leaf touched; mints no `clm-`/`def-`. DO-NOT-MERGE. Companion (owed): the derivation (Leg A), the driver (Legs B/C), the result doc, and the docket continuation `### ENTRY 2026-07-21-boundary-strain-amplitude`.
