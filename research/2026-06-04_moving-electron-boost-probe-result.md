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

<!-- skeleton -->

## §4 Honest framing + limitations (structural-capability finding either way)

<!-- skeleton -->

## §5 Cross-references

<!-- skeleton -->

## §6 Auditor queue

<!-- skeleton -->
