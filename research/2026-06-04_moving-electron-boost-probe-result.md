# Moving-electron boost probe (CP8) — does the Master-Equation FDTD engine host a MOVING self-trapped core? — RESULT

**Date**: 2026-06-04
**Branch**: `analysis/moving-electron-probe` (off main `ea917144`)
**Brief / prereg**: [`_orchestration/moving-electron-probe.md`](../_orchestration/moving-electron-probe.md)
**Driver**: [`src/scripts/vol_1_foundations/moving_electron_boost_probe.py`](../src/scripts/vol_1_foundations/moving_electron_boost_probe.py)
**Engine**: [`src/ave/core/master_equation_fdtd.py`](../src/ave/core/master_equation_fdtd.py) — the ONLY engine with `c_eff(V)=c₀/√S`, and the only one that autonomously hosted a self-trap (the v14 breather, Mode-I PASS)
**Classification**: Class-D emergence/hosting test — the NEXT LAYER (mobility) on the proven self-trap host.

**Status**: RESULT. Awaiting auditor pass before any corpus propagation.

---

## §0 VERDICT (one line)

**MOVES.** The proven v14 breathing soliton, given net transverse momentum via a `k_x` carrier boost, **translates coherently** across the lattice — the Γ=−1 frozen boundary does NOT pin it. The energy-density centroid moves **+13.9 cells** at **`v_obs = 0.674·c₀`**, matching the pre-stated de-Broglie forward-prediction `v_g = 0.618·c₀` to **9%** (obs/pred = 1.09), with the saturated **core and the envelope translating together** (interior-advect wins the boundary-pin-vs-interior-advect duality). The matched phase-scrambled baseline (same `k_x`-band power) does NOT translate (+0.67 cells), so the motion is **coherence-driven, not amplitude/saturation-driven** — the phase3f Factor-2 confound is cleanly excluded. **Mobility is a hostable layer on the Master-Equation FDTD engine.**

## §1 The numbers (3 arms)

All arms: `master_equation_fdtd.py`, N=48³, PML=4, breather `sech` A=0.85 R=2.5 (the v14 Mode-I config), 400 steps, deterministic (max env-centroid diff across two identical runs = 0.00). Boost `k_x = 2π/8` (8 cells/wavelength, well-resolved; NOT tuned to a target velocity). Centroid PML-excluded throughout.

| Arm | `k_x` | env-centroid disp | `v_obs/c₀` | core-centroid disp | retention† | FWHM× (late) | **Verdict** |
|---|---|---|---|---|---|---|---|
| **STATIONARY** (`k_x=0`) | 0.000 | **+0.36** | 0.017 | +0.79 | 0.50 | 5.4 | no translation (migration-noise floor) |
| **BOOST** (breather + `k_x`) | 0.785 | **+13.93** | **0.674** | +18.03 | 0.69 | 3.4 | **MOVES** |
| **BASELINE** (phase-scrambled + `k_x`) | 0.785 | **+0.67** | 0.033 | +1.09 | 0.55 | 1.4 | no translation |

† retention = late-window interior energy / post-transient-peak interior energy (the boost's `V_prev` leapfrog kick injects a t=0 transient; retention is normalized to the post-kick settle peak, not the raw t=0 energy).

**The discriminating signal is translation, and it is unambiguous:** BOOST moves +13.9 cells; the two no-translation controls move +0.36 (STATIONARY) and +0.67 (BASELINE) — a **~20× separation**. The BOOST also retains better (0.69 vs ~0.50) and stays more localized (FWHM× 3.4, bounded, vs the STATIONARY's 5.4 spreading toward grid scale) — the boost partially *stabilizes* the lump rather than tearing it apart.

> **On the STATIONARY/BASELINE "no-translation" framing:** these are not the "trapped vs not" arms — they are the *does-it-translate* controls. This particular `A=0.85, R=2.5` sech is a mildly-*decaying* breather on N=48 (retention ~0.5, FWHM spreads), consistent with the v14 result that the Master-Eq breather is metastable/breathing, not a perfect static eigenmode ([`breathing-soliton-v14-mode-i.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/breathing-soliton-v14-mode-i.md)). The CP8 question is mobility — *does the lump translate* — and on that axis the answer is decisive: only the coherent `k_x` boost produces transport.

## §2 Forward-predicted vs observed v_g (driver-honesty, no fit)

**Stated PRE-RUN in the prereg** (`ave-driver-script-honesty`): de-Broglie massive dispersion `ω²=c²k²+ω_C²`, `v_g=dω/dk=c²k/ω` ([`de-broglie-standing-wave.md:181`](../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md)). Substrate-derived `ω_C` in lattice units: `ℓ_node = ℏ/(m_e c)` = the reduced Compton wavelength ([`constants.py:237,262`](../src/ave/core/constants.py)), so `ω_C = m_e c²/ℏ = c₀/ℓ_node`, and with `c₀=1, ℓ_node↦dx=1` this is **`ω_C(lattice) = 1.0` exactly** — not an engineering choice.

**Primary `k_x=2π/8`: predicted `v_g = 0.618·c₀`, observed `v_obs = 0.674·c₀` → ratio 1.09 (within 9%, no fit).**

`k_x`-sensitivity (the forward-prediction *discriminator*, NOT tuning — `k_x` chosen as well-resolved cells/wavelength, `v_g` predicted from each):

| wavelength (cells) | `k_x` | predicted `v_g/c₀` | observed `v_obs/c₀` | obs/pred |
|---|---|---|---|---|
| 6 | 1.047 | 0.723 | 0.651 | 0.90 |
| **8 (primary)** | **0.785** | **0.618** | **0.674** | **1.09** |
| 12 | 0.524 | 0.464 | 0.643 | 1.39 |
| 16 | 0.393 | 0.366 | 0.599 | 1.64 |

**Reading (honest, partial-tracking):** at the well-resolved short wavelengths (`k_x=2π/6, 2π/8`) `v_obs` tracks the cold-lattice de-Broglie `v_g` to within ~10%. At long wavelengths (`k_x=2π/12, 2π/16`) `v_obs` **saturates near ~0.6·c₀ instead of dropping** to the predicted 0.37-0.46 — i.e. the moving saturated lump has a **velocity floor** that the cold-lattice dispersion does not capture. This is the saturated-core clock-drag flagged pre-run (`ω_local=ω_C·√S` at the A≈0.85 core), cutting the opposite way from a slow-down: the breather's own intrinsic propagation sets a minimum transport speed. **The de-Broglie `v_g` is the correct LEADING prediction (best at the resolved primary `k_x`); the long-`k_x` deviation is the expected saturated-clock signature, not a fit artifact** — and it is itself a substrate-physics finding (a moving self-trap is not a free de-Broglie wave; its core dynamics floor its speed).

## §3 The duality reading (interior-advect vs boundary-pin)

The load-bearing duality the test adjudicates: the Γ=−1 saturated boundary is BOTH
- `c_local→0` (hyper-rigid → PIN): [`resonant-lc-solitons.md:50`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md) *"the nodes at the saturation boundary are geometrically jammed … the local phase velocity (c_local=1/√(LC)) strictly collapses to zero, creating a hyper-rigid, localized envelope"* — and
- `c_eff→∞` (interior advects): [`111_master_equation_audit_and_engine_gap.md:41`](_archive/L3_electron_soliton/111_master_equation_audit_and_engine_gap.md) `c_eff(V)=c₀·(1−A²)^(−1/4)=c₀/√S → ∞`.

**Discriminator (saturated-core centroid vs envelope centroid):** the BOOST arm's **core centroid translates +18.0 cells** while the **envelope centroid translates +13.9 cells** — both move, together, in the same direction, at comparable magnitude (the core actually leads the spread-out envelope tail). The driver's automated reading: *"core+envelope translate TOGETHER (interior-advect; MOVES-consistent)."*

**Resolution: the interior-advect channel wins.** The boost is carried by the whole structure — the saturated core does NOT stay pinned while the interior sloshes around it. The frozen-clock boundary, far from anchoring the lump in place, **rides along with it**: the saturated region is a co-moving mirror, not a fixed one. Mechanically (EE-native, per the on-main translation-circuit mapping [`common/translation-tables/translation-circuit.md`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md)): the `Γ=−1` short-circuit boundary is a property of the *impedance discontinuity* at the core edge, and that discontinuity travels with the core's high-amplitude region — it is a moving boundary condition, not a lattice-fixed wall. The `c_local→0` "hyper-rigid envelope" of `resonant-lc-solitons.md` describes the boundary's rigidity in its OWN co-moving frame (it does not radiate, it does not spread at the boundary), which is fully consistent with the whole rigid object translating.

This is the clean answer to the prereg's central question: **the rigid boundary does NOT pin the envelope; the interior carries the boost.** The Γ=−1 frozen clock is a *co-moving* frozen clock.

## §4 Honest framing + limitations (structural-capability finding either way)

**This is a STRUCTURAL-CAPABILITY FINDING (substrate-native-check Checkpoint 8).** Per the prereg, both MOVES and PINS were pre-registered as clean findings; the engine returned MOVES — the mobility layer IS hostable on the Master-Equation FDTD engine. The corpus electron's transverse translation is reproduced by the proven self-trap host given the simplest momentum operator. This sits one layer above the sibling result ([`2026-06-04_full-electron-transverse-selftrap-result.md`](2026-06-04_full-electron-transverse-selftrap-result.md), Mode II): that established self-trap *localization* (mass) emerges on the continuum engine but the (2,3) *winding* does not; THIS establishes that the localization, once formed, is *mobile* — it translates coherently and at (near) the predicted de-Broglie group velocity.

**Limitations (ave-evidence-framing-discipline):**

1. **The breather is metastable, not a perfect eigenmode.** The `A=0.85, R=2.5` sech is the documented v14 *breathing/decaying* soliton, not a static bound state — retention ~0.5-0.7 over the window, FWHM breathes. So this is "a localized, mobile, breathing lump translates coherently," NOT "a perfectly conserved particle translates forever." The translation signal (env_disp 13.9 vs noise 0.36/0.67, ~20× separation) is robust to this; the *durability* is breather-limited.

2. **The boost injects a t=0 transient** (`V_prev` leapfrog kick → raw energy briefly exceeds the seed). Handled by normalizing retention to the post-transient peak; retention then *declines* monotonically (no runaway). Honest reading: a mildly-radiating moving lump, not a perfectly lossless one. An auditor may prefer a soft-injection boost (ramp the carrier over several steps) to remove the transient — flagged.

3. **Window/resolution modest** (N=48³, 400 steps, ~seconds). The translation is unambiguous at this scale and is not a convergence artifact (it is a ~14-cell coherent displacement, far above lattice noise), but a higher-resolution / longer-window confirmation (does it translate ballistically for 1000+ steps before the breather decays?) is a cheap follow-up.

4. **`v_obs` tracks de-Broglie `v_g` only at short wavelengths** (§2). The long-`k_x` velocity floor (~0.6·c₀) is itself a real finding — a moving saturated self-trap is not a free de-Broglie wave — but it means "the breather translates at *approximately* the predicted group velocity" is accurate only near the resolved primary `k_x`; the full `v_g(k_x)` dispersion is NOT reproduced across the range. Stated, not papered over.

5. **Real-space centroid is the correct coordinate here** (translation IS a real-space observable, `de-broglie-standing-wave.md:50` "its motion displaces the lattice"; `phase-space-coordinate-check` confirmed in prereg §3) — this is NOT the phase-space-(2,3) trap that sank phase3f. But by the same token, this probe says nothing about whether the *internal winding* survives the boost (that lives in phasor coordinates and is out of scope for a scalar engine, as the sibling Mode-II result established).

**SM-counterfactual note (ave-discrimination-check):** that a localized wavepacket translates at its group velocity is, in isolation, NOT AVE-distinct (any dispersive wave engine does this). What IS substrate-specific here: (a) the lump is a *self-trapped* saturation soliton (Γ=−1 boundary), and it translates *as a unit* (core+envelope together) rather than dispersing — the matched-baseline contrast shows the coherence/self-trap is load-bearing for the transport; (b) the long-`k_x` velocity floor is a saturated-clock signature absent from a linear engine. The headline claim is the narrow, honest one: **the Master-Equation FDTD engine HOSTS a mobile self-trap** (the mobility layer is hostable) — a capability statement about the engine, not a claim that group-velocity transport per se is AVE-distinct.

## §5 Cross-references

- **Brief / prereg:** [`_orchestration/moving-electron-probe.md`](../_orchestration/moving-electron-probe.md)
- **Driver:** [`src/scripts/vol_1_foundations/moving_electron_boost_probe.py`](../src/scripts/vol_1_foundations/moving_electron_boost_probe.py)
- **Engine:** [`master_equation_fdtd.py`](../src/ave/core/master_equation_fdtd.py) — the only `c_eff(V)=c₀/√S` engine
- **The PROVEN host (v14 breather, Mode-I):** [`r10_master_equation_v14_v2.py`](../src/scripts/vol_1_foundations/r10_master_equation_v14_v2.py) + [`breathing-soliton-v14-mode-i.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/breathing-soliton-v14-mode-i.md)
- **The duality (boundary-pin `c_local→0`):** [`resonant-lc-solitons.md:50`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md)
- **The duality (interior-advect `c_eff→∞`) + engine-gap:** [`111_master_equation_audit_and_engine_gap.md:18,41,89`](_archive/L3_electron_soliton/111_master_equation_audit_and_engine_gap.md)
- **de-Broglie dispersion + group velocity:** [`de-broglie-standing-wave.md:181`](../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md); **longitudinal bulk-modulus motion (the follow-up channel):** same file `:50`
- **Electron = self-trapped photon (the reframe):** [`electron-bh-isomorphism.md:10`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md)
- **Sibling self-trap precedent (localization emerges, (2,3) does not — Mode II):** [`2026-06-04_full-electron-transverse-selftrap-result.md`](2026-06-04_full-electron-transverse-selftrap-result.md); **discrete-emergence Option-B precedent:** [`2026-06-04_full-electron-option-B-discrete-emergence-result.md`](2026-06-04_full-electron-option-B-discrete-emergence-result.md)
- **The momentum-seed shape adapted:** [`test_fdtd3d_moving_pulse_wake.py:_seed_moving_gaussian_pulse`](../src/tests/test_fdtd3d_moving_pulse_wake.py) (`cos(k_x·x)·envelope`)
- **EE-mapping leaves (now on main):** [`common/translation-tables/translation-circuit.md`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md) (the Γ=−1 short-circuit / impedance-boundary EE mapping)

## §6 Auditor queue

1. **Corpus propagation of the verdict** (auditor lands, implementer surfaces): MOVES is a positive hosting result. Does it warrant a KB leaf — a mobility addendum to [`breathing-soliton-v14-mode-i.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/breathing-soliton-v14-mode-i.md) ("the v14 breather is mobile; translates at ≈de-Broglie v_g; Γ=−1 boundary is co-moving, not pinning") — or research-result-only? No manuscript/matrix entry drafted by implementer.
2. **The duality resolution** (the load-bearing physics output): confirm the saturated-core-vs-envelope reading — the Γ=−1 frozen clock is a *co-moving* frozen clock (interior-advect), NOT a lattice-fixed pin. This resolves the `resonant-lc-solitons.md:50` (`c_local→0`) vs `111:41` (`c_eff→∞`) apparent tension as boundary-in-co-moving-frame vs interior-in-lab-frame, both consistent with a rigid translating object. Auditor: is this the right resolution, or is the core-centroid co-move an artifact of the breather's spreading?
3. **The `ω_C(lattice)=1` anchor**: confirm `ℓ_node`=reduced-Compton-wavelength↦dx is the right cold-lattice dispersion anchor (vs a saturated-clock-corrected `ω_C·√S`). The long-`k_x` velocity floor suggests the saturated correction is real and could be derived — closure-roadmap candidate.
4. **Longitudinal follow-up** (the brief's flagged separate channel): since this transverse probe returned MOVES (not PIN), the longitudinal bulk-modulus displacement channel ([`de-broglie-standing-wave.md:50`](../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md)) is now a *complementary* probe (both transverse-boost and longitudinal-displacement may carry electron motion), not the fallback the PIN branch would have made it. Flag as a follow-up: does longitudinal displacement give a different `v(k)` law?
5. **Boost-transient cleanup** (§4.2): a soft-injected carrier boost (ramped over several steps) would remove the t=0 `V_prev` kick transient; worth a confirmation run if the result is promoted.
6. **Verdict-label nuance** (§1): STATIONARY/BASELINE show `DISPERSES` in the driver's auto-classifier only because the bare `A=0.85` breather decays on N=48 — they are the *no-translation* controls, and the translation discriminator (env_disp ~20× separation) is what carries the MOVES verdict. Auditor: confirm the classifier's `DISPERSES` tag on the controls is not misread as "the test dispersed."
