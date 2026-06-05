# Motion-stability BEMF probe — PREREG / BRIEF

**Date**: 2026-06-04
**Branch**: `analysis/motion-stability-bemf` (off main `adb26859`)
**Worktree**: `/tmp/ave-bemf`
**Driver**: [`src/scripts/vol_1_foundations/motion_stability_bemf_probe.py`](../src/scripts/vol_1_foundations/motion_stability_bemf_probe.py)
**Result**: [`research/2026-06-04_motion-stability-bemf-result.md`](../research/2026-06-04_motion-stability-bemf-result.md)
**Engine**: [`src/ave/core/fdtd_3d.py`](../src/ave/core/fdtd_3d.py) (full-vector Maxwell, nonlinear ε(E)/μ(H) per Axiom 4, CPML)
**Base self-trap (validated)**: [`r10_fdtd3d_transverse_photon_selftrap.py`](../src/scripts/vol_1_foundations/r10_fdtd3d_transverse_photon_selftrap.py) — retention 0.580 (self-trap) vs 0.389 (matched baseline), [`research/2026-06-04_full-electron-transverse-selftrap-result.md`](../research/2026-06-04_full-electron-transverse-selftrap-result.md)

**Status**: PREREG FROZEN. Result section filled after driver run. Forward-predicted sign locked BELOW, before any run.

---

## §0 THE HYPOTHESIS (Grant 2026-06-04) — and its GREEN-FIELD / CONTRADICTS-DEFAULT status

**Topological stability FROM motion.** A static self-trap decays; a *moving* one is held together by its own back-reaction — the dark wake `τ_zx` (the mutual-inductance / back-EMF the moving trap drags behind it). The cross being tested: the corpus stops the dark wake at "momentum trail" and never crosses to "stabilizer."

**Falsifiable differential prediction (Grant):**
> retention(v) − retention(0) **> 0**, **monotonic** in v, and the stability-gain **tracks** the measured back-EMF / `τ_zx` amplitude.

**This is a GENUINE prove-or-disprove (EMERGENCE test), because the canonical corpus default CONTRADICTS it:**

1. **Electron stability is the STATIC saturation knot.** [`resonant-lc-solitons.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md) — confinement is "extreme flux crowding at the particle's boundary … perfect macroscopic impedance mismatch" from the **static topological twist** driving local dielectric saturation `Δφ → α` (Γ→−1). Motion is **not** part of the confinement story; the bubble is a static total-internal-reflection cavity.
2. **A moving (2,3) "requires SUSTAINED EXTERNAL DRIVE."** [`_archive/L5/axiom_derivation_status.md:178`](../research/_archive/L5/axiom_derivation_status.md) — interpretation (B): the engine hosts a separate *oscillating* (2,3) electron only under **sustained external drive at ω=2**; left alone it relaxes to the static fixed point. i.e. motion is a *cost* that must be paid for, not a free stabilizer.

So the canonical default predicts retention(v) **FLAT or NEGATIVE** (the static trap is the stable object; motion is at best irrelevant and at worst destabilizing / drive-hungry). Grant predicts **POSITIVE & monotonic, tracking τ_zx**. Both are pre-registered as clean outcomes below.

**The structural seed Grant is crossing from:** the dark wake exists ONLY for a *moving* soliton — trailing-edge desaturation, Lenz back-EMF `V_BEMF = −L_eff dI/dt` ([`2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md:116`](../research/2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md) §6). The corpus calls it "momentum trail / Newton-3rd-law reaction mass." Grant's cross: that same back-EMF is also a **restoring / cohering** reaction on the core — a moving trap reflects its own backward shear wave into itself. CONTRADICTS-default because the canon's confinement is static-saturation, full stop.

---

## §1 ENGINE + BASE + the τ_zx (back-EMF) observable on fdtd_3d.py — STEP-0 findings

### (a) How to BOOST the validated self-trap to net group-velocity v while it STILL self-traps

The validated self-trap (`build_transverse_photon_seed`) is **two counter-propagating focused CP transverse pulses** with **equal & opposite k_x → ZERO net momentum** (a standing trap). To give it net group velocity v, **break the counter-prop amplitude symmetry**:

- pulse A (+x): amplitude `× (1 + δ)`
- pulse B (−x): amplitude `× (1 − δ)`

Net Poynting flux ⟨E×H⟩_x ∝ (forward power − backward power) becomes **positive ∝ δ**, so the localized energy drifts at net group velocity `v ≈ v_max · (P_A − P_B)/(P_A + P_B)`. Limits:
- `δ = 0` → the validated **zero-momentum self-trap** (v = 0 arm).
- `δ → 1` → a **single moving pulse** (pure transport, no counter-prop trapping — this degenerates toward the LINEAR-transport limit; we stay well below it).

This is a **momentum operator on the GENERATIVE PRECURSOR** (the transverse-photon seed), NOT a planted moving end-state — CP8-compliant (`substrate-native-check`). v is set by the seed's momentum content and is **NOT tuned to hit a retention target** (`ave-driver-script-honesty`); we report the measured centroid drift velocity, not an imposed one.

**BLOCKER WATCH (STEP-0, flagged):** if boosting *destroys* the trap entirely (the asymmetry advects everything out before it self-traps), that is itself a finding — report it, do not force. Mitigation: keep δ modest (v ≲ 0.4 c), and instrument peak_A so we can SEE whether the boosted seed still reaches saturation.

### (b) Measuring τ_zx (the back-EMF) at the moving core on fdtd_3d.py

`DarkWakeObserver` lives on `VacuumEngine3D` (K4-TLM + Cosserat), **not** on `fdtd_3d.py`. But its canonical formula is engine-portable:

> `τ_zx(r) ∝ Z_local(r) · ∂/∂x [ |V(r)|² / V_SNAP² ]`  ([DarkWakeObserver docstring](../src/ave/topological/vacuum_engine.py); doc 49 synthesis)

On the Yee engine `V_local = E·dx`, and the FDTD bridge is canonical at [`2026-05-31_FT-darkwake-crossscale_result.md:117`](../research/2026-05-31_FT-darkwake-crossscale_result.md): `dV²/dz ≈ ℓ_node²·∇|E|²`. So on `fdtd_3d.py`:

```
τ_zx(r)  =  Z_local(r) · ∂_x[ |E(r)|² · dx² / V_SNAP² ]      Z_local = Z_0 · S(A)    (saturation-modulated)
```

This is the **longitudinal (propagation-axis) component of the energy-gradient back-reaction** — exactly the engine's own `ponderomotive_force` x-component, re-scaled by `Z_0·S(A)/V_SNAP²`. Axiom chain (DarkWakeObserver docstring): Ax3 Noether/Newton-3rd-law back-reaction; Ax4 Op14 saturation gives the gradient its spatial structure (without saturation the back-EMF response is uniform → no wake). We report:
- `max|τ_zx|` (interior, PML-excluded) at each v,
- the **backward** (trailing, −x relative to the moving core) wake amplitude specifically (the canon: wake propagates *backward* from the moving core).

Honesty note: this is the **E/H projection** of the canonical Cosserat-side τ_zx — the longitudinal-shear back-EMF as it appears in the Maxwell sector. It is a *projection*, not the full Cosserat shear tensor (which needs `VacuumEngine3D`). Framed accordingly in the result.

### (c) Retention + saturation diagnostic

- **retention**: `interior_energy_retention` = interior-energy(final)/interior-energy(seed), PML-excluded (Rule 10). Also `peak_E_retention`.
- **saturation depth (THE load-bearing A-instrument, per (ii)-audit lesson 1)**: `peak_A_series` throughout the run, `A = |E|·dx/V_SNAP`; Op14 engagement bar `A > √(2α) = R_I`; full saturation `A → 1` (Γ→−1). **Tracked EVERY probe step** so we can state whether the self-trap STAYS saturated while moving. If the moving core desaturates, the "motion stabilizes" claim FAILS and we say so.

### (d) THE PML-ADVECTION CONFOUND (the one real methodological risk — flagged + controlled)

A moving trap drifts toward the +x PML and loses energy to **absorption**, which would push retention(v) **DOWN** purely from box geometry — a false NEGATIVE that mimics the canonical default. Controls:
1. **Window the recording so the trap stays interior** (n_record chosen so the fastest arm's centroid does not enter the +x PML), AND track `trap_still_interior` + centroid trajectory.
2. **Report peak_A (saturation depth) alongside retention** — A is PML-geometry-INDEPENDENT: if A stays high while moving, the trap is structurally intact regardless of where it sits in the box. A-trajectory is the confound-proof discriminator for "trap alive vs dispersed."
3. **The LINEAR arm at the SAME v feels the SAME PML geometry** — so any *differential* (self-trap retention rising relative to linear) is not a PML artifact; PML advection hits both arms equally.

---

## §2 THE TEST (CP8 emergence test — v-sweep × 3 arms)

Sweep **v ∈ {0, ~0.2c, ~0.4c}** (set by δ ∈ {0.0, low, mid}; report measured centroid-drift v, not imposed). For each v, three arms:

### Arm SELF-TRAP(v) — the hypothesis arm
The validated transverse-photon self-trap, boosted to v (amplitude asymmetry δ). Deep-saturation amplitude (the validated `0.7·V_SNAP/dx` operating point). Measure: retention(v), peak_E_retention(v), FWHM(v), peak_A trajectory(v), max|τ_zx|(v).

### Arm LINEAR(v) — the AVE-distinct discriminator (the SM-counterfactual)
A **sub-saturation** transverse pulse (amplitude well below the √(2α) Op14 bar → S(A)≈1, no self-trap, ordinary linear Maxwell), boosted to the **same** v. A linear pulse **disperses regardless of v** → its retention should **NOT rise with v**. If SELF-TRAP retention rises with v while LINEAR stays flat → the rise is **self-trap-specific** (the bemf is the stabilizer), not generic transport. This is the `ave-discrimination-check` arm: velocity/transport is NOT the claim; STABILITY-gain-from-motion is.

### Arm BASELINE(v) — matched saturation-depth control (AVOID the (ii) confound)
**NOT** a global-norm phase-scramble (the (ii) audit proved that pins at A≈1.0-clamped with half the energy — a saturation confound). We use the **r10 matched-distribution baseline**: phase-scrambled to destroy transverse coherence, then **peak-|E| rescaled to match SELF-TRAP's peak exactly** → engages the saturation kernel to the **same depth** (same A-trajectory ceiling), boosted to the same v. This isolates the **topology/coherence** effect from the saturation-amplitude effect at matched v. (Why matched: equal peak |E| ⇒ equal Op14 engagement ⇒ no saturation-driven retention confound in either direction.) We also report the **two-superposed-opposite-k_x** equal-band-power zero-net-momentum check as a cross-reference at v=0 (where it coincides with the SELF-TRAP seed by construction).

**Which baseline + why matched (stated, per brief):** primary = phase-scrambled **peak-matched** (matches per-component amplitude histogram's power spectrum AND peak-|E| ⇒ matched saturation depth); it is the r10-validated fix for the phase3f random-direction confound. The scramble destroys the constructive transverse coherence that makes the self-trap, while holding saturation depth fixed — so a SELF-TRAP > BASELINE gap is coherence/topology, not amplitude.

---

## §3 A-INSTRUMENTATION (the (ii)-audit lessons — do NOT repeat)

1. **Instrument peak-A / S(A) THROUGHOUT each run.** The (ii) breather decayed 0.85→0.4 and nobody tracked it → "Γ=−1" was never reached. We record `peak_A` every PROBE_EVERY steps for every arm and report the full trajectory. **Explicit gate:** confirm SELF-TRAP STAYS saturated (peak_A high, A>√(2α) throughout, ideally A→1 cusp) WHILE moving. If it desaturates as v rises, the "self-trap stabilizes" claim FAILS — reported honestly.
2. **LINEAR control at the same v.** The (ii) audit showed a linear pulse advects at the same velocity — velocity is NOT the discriminator; STABILITY is. LINEAR is arm 2; sub-saturation so it cannot self-trap.
3. **Velocity/transport is NOT the claim.** Linear engines transport too (not AVE-distinct). The claim is STABILITY-GAIN-from-motion tracking the back-EMF. The SELF-TRAP-vs-LINEAR *contrast* is the load-bearing comparison, not the absolute retention.

---

## §4 FORWARD-PREDICTED SIGN (driver-honesty — locked BEFORE the run, no fit)

| Outcome | retention(v) slope (SELF-TRAP) | LINEAR(v) slope | τ_zx vs stability-gain | Verdict |
|---|---|---|---|---|
| **Grant (hypothesis)** | **> 0, monotonic** | flat | positively correlated | **SUPPORTS** (overturns static-trap default) |
| **Canonical default** | **≤ 0 (flat / negative)** | flat | uncorrelated / n/a | **CONTRADICTS** (static trap holds; motion irrelevant-to-destabilizing) |
| Ambiguous | rises but LINEAR also rises | rises too | — | **NULL** (generic transport / PML artifact, not self-trap-specific) |

**Sign locked: Grant = POSITIVE slope; canonical = FLAT/NEGATIVE slope.** v is NOT tuned to hit a target; we report the measured retention(v) curve as-is and read the sign off it. A POSITIVE result is HIGH-STAKES (it overturns the static-trap canonical default) → framed exactly as strong as the data, no more (`ave-evidence-framing-discipline`).

---

## §5 DISCIPLINE APPLIED

- `substrate-native-check` **CP8**: boost the self-trapping SEED = momentum operator on the generative precursor, NOT a planted moving end-state; matched baseline; null is a clean structural finding. (Walk completed; exit criteria met — see result §1.)
- `consistency-vs-emergence`: **EMERGENCE test** — a NOVEL prediction the corpus default CONTRADICTS (static-saturation-knot + sustained-drive). Classified as such, not a consistency check.
- `ave-discrimination-check`: the **LINEAR arm IS the SM-counterfactual** — confirms stability-gain is self-trap-specific, not generic transport.
- `ave-canonical-source`: constants imported from `ave.core.constants`; `verify_constants()` cross-check before any verdict; no hardcoded physics literals.
- `ave-driver-script-honesty`: forward-predict the sign (§4); v NOT fit-to-target; no print-vs-compute mismatch (every printed number is computed from the run).
- `ave-evidence-framing-discipline`: prove-or-disprove; a POSITIVE overturns the static-trap default → frame exactly as strong as the data.
- `pre-test-physics-check`: one plumber-physical ambiguity surfaced (the matched-baseline choice + the PML-advection confound) — flagged in §1(d)/§2, controlled, not silently resolved.
- Pure-AVE-corpus.

---

## §6 AUDITOR QUEUE

- [ ] **τ_zx projection fidelity**: is the E/H-sector `Z_0·S(A)·∂_x|E·dx|²/V_SNAP²` a faithful projection of the canonical Cosserat τ_zx, or does the missing Cosserat sector drop a load-bearing term? (Cross-check vs `DarkWakeObserver` on `VacuumEngine3D` in a follow-up.)
- [ ] **PML-advection confound**: verify the recording window keeps the fastest arm interior; confirm the SELF-TRAP-vs-LINEAR *differential* is PML-robust (both arms feel the same geometry).
- [ ] **Matched-baseline adequacy**: does peak-|E|-matched phase-scramble fully control saturation depth at each v, or does the boost shift the A-ceiling differently for scrambled vs coherent fields?
- [ ] **δ→v monotonicity**: confirm measured centroid-drift v is monotonic in δ and the arms are compared at matched *measured* v (not matched δ) if δ→v is nonlinear.
- [ ] **Verdict strength**: if SUPPORTS, is the τ_zx-vs-gain correlation strong enough (and the LINEAR contrast clean enough) to claim overturning the static-trap default, or only "motion does not destabilize"?
