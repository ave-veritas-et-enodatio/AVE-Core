# C14-DAMA Amplitude Derivation — Pre-Registration

**Status:** PREREG ONLY (no derivation performed). Surfaces 2 foundational physics-judgment calls that block solo derivation. Per `ave-prereg` skill discipline.

**Date:** 2026-05-17
**Author:** agent + corpus-grep audit (agentId: adcb9b4429afd35e4)
**Matrix row:** C14-DAMA-MATERIAL
**Closure-roadmap item:** §0.5 open scope-correction "DAMA amplitude formula" pending

## Derivation target

Derive the AVE prediction for DAMA/LIBRA's annual modulation amplitude in cpd/kg/keV (counts per day per kg per keV) at 2-6 keV single-hit window, as a function of:
- $\kappa_{crystal}$ coupling ratio (operator choice TBD per Q1 below)
- Earth velocity through $\mathcal{M}_A$ rest frame (frame choice TBD per Q2 below)
- Annual orbital component (±15 km/s, fraction depends on frame choice)
- AVE substrate-physics rate coefficient (no corpus chain exists)

Target empirical value: DAMA ~0.0103 cpd/kg/keV at 2-6 keV.

## Corpus state

**Verdict: GREEN-FIELD for connecting chain; SUBSTANTIAL structural ingredients.**

Confirmed audit-trail leaves explicitly mark this as TBD:
- [`multi-galaxy-validation.md:41`](manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/multi-galaxy-validation.md): "the amplitude formula itself is NOT derived in the corpus."
- [`divergence-test-substrate-map.md:443`](manuscript/ave-kb/common/divergence-test-substrate-map.md) C14 row: "**no explicit amplitude formula — TBD pin**"
- [`closure-roadmap.md:96`](manuscript/ave-kb/common/closure-roadmap.md): "**DAMA amplitude formula** (C14 row): crystal-density ratios $\kappa = \rho_{crystal}/\rho_{bulk}$ computable but observable-amplitude prediction unfinished."
- DAMA empirical value 0.0103 cpd/kg/keV does not appear anywhere in corpus.

The 2026-05-16 audit retired the C13-VLBI-DARK forward-prediction claim and simultaneously demoted DAMA C14 to TBD-pin descriptive-only. **Reopening this is reopening an already-honestly-flagged gap, not new corpus work.**

## Available structural ingredients

| Ingredient | Source | Value / form |
|---|---|---|
| $\nu_{kin}$ kinematic mutual inductance | [`lc-electrodynamics.md:48-52`](manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/lc-electrodynamics.md) | $\alpha c \ell_{node} \approx 8.45 \times 10^{-7}$ m²/s |
| $\rho_{bulk}$ vacuum density | [`lc-electrodynamics.md:29`](manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/lc-electrodynamics.md) | $\xi_{topo}^2 \mu_0 / (p_c \ell_{node}^2) \approx 7.92 \times 10^6$ kg/m³ |
| Crystal densities | [`vlbi_impedance_parallax.py:62-66`](src/scripts/vol_3_macroscopic/vlbi_impedance_parallax.py) | NaI 3.67e3; Sapphire 3.98e3; Ge 5.32e3 kg/m³ |
| $\kappa_{entrain}$ template (linear scaling) | [`sagnac-rlve.md:14-26`](manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md) | $v_{network} = v_{drive} \cdot \rho_{rotor}/\rho_{bulk}$ |
| Phonon-coupling-lowers-tunneling-barrier mechanism | [`existing-experimental-signatures.md:20-24`](manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/existing-experimental-signatures.md) | Bottle-vs-beam neutron 9s anomaly; same mechanism family as DAMA |
| Earth velocity through $\mathcal{M}_A$ (CMB-dipole frame) | [`preferred-frame-and-emergent-lorentz.md:13`](manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md) | $v_\oplus \sim 370$ km/s |
| $V_{yield}$ macroscopic saturation limit | [`magnetic-saturation.md:13`](manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/magnetic-saturation.md) | $\sim 43.65$ kV |

## Two unresolved physics-judgment calls (block solo derivation)

### Q1 — Operator choice: bulk density vs transverse shear modulus

The corpus carries TWO inconsistent operator framings for the κ_crystal coupling:

**Framing A — bulk-density coupling** (per [`vlbi_impedance_parallax.py`](src/scripts/vol_3_macroscopic/vlbi_impedance_parallax.py) and [`multi-galaxy-validation.md`](manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/multi-galaxy-validation.md)):
$$\kappa_{crystal} = \rho_{crystal} / \rho_{bulk}$$
- NaI ($\rho = 3.67 \times 10^3$ kg/m³): κ ≈ 4.63e-4
- Sapphire ($\rho = 3.98 \times 10^3$): κ ≈ 5.03e-4
- Ge ($\rho = 5.32 \times 10^3$): κ ≈ 6.72e-4
- Ratio NaI:Sapph:Ge = 1 : 1.08 : 1.45

**Framing B — transverse-shear-modulus coupling** (per [`bullet-cluster.md:20-22`](manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/bullet-cluster.md)):
> "A rigid crystal lattice (NaI) can structurally couple to and detect transverse LC grid phonons. A mobile liquid (Xenon) mathematically **cannot sustain long-range transverse shear polarization**."

If transverse-shear is the operative coupling, the relevant constant is shear modulus G_crystal, not bulk density:
- NaI G ≈ 15 GPa
- Sapphire G ≈ 145 GPa
- Ge G ≈ 67 GPa
- Ratio NaI:Sapph:Ge ≈ 1 : 9.7 : 4.5 (very different scaling)

**The two framings predict materially different DAMA-vs-CDMS-vs-COSINE amplitude ratios.** The XENONnT null result is the discriminator that motivates Framing B (liquid can't sustain transverse shear) but the math implementation uses Framing A.

**The C13c META row in the matrix flags this exact issue** ([`divergence-test-substrate-map.md:442`](manuscript/ave-kb/common/divergence-test-substrate-map.md)): three DM-mechanism framings (η_eff drag, TT shockwave, κ_crystal coupling) coexist without formal unification under Cosserat substrate. **Q1 is part of C13c.**

**Need from Grant:** which is the operative coupling? Or do both apply at different scales / frequencies?

### Q2 — Frame choice: 232 km/s galactic vs 370 km/s CMB-dipole

The corpus carries TWO inconsistent reference-frame framings for the DAMA wind:

**Framing α — galactic-orbit frame** (standard DM-wind picture, per [`bullet-cluster.md:18`](manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/bullet-cluster.md)):
- $v_\oplus \approx 232$ km/s (Sun's galactic orbital velocity relative to Milky Way rest frame)
- Annual orbital component ±15 km/s → fractional modulation ~6.5%

**Framing β — CMB-dipole / K4 lattice rest frame** (cohesive narrative per [`preferred-frame-and-emergent-lorentz.md:13`](manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md)):
- $v_\oplus \approx 370$ km/s (Earth velocity relative to CMB-dipole rest frame = K4 lattice rest frame per Q-G24)
- Annual orbital component ±15 km/s → fractional modulation ~4.1%

The two framings give different baseline wind magnitudes AND different fractional modulation amplitudes. The standard DM literature uses Framing α; AVE's preferred-frame leaf identifies the lattice rest frame as the CMB rest frame (Framing β).

**Need from Grant:** which frame does the DAMA wind couple to?
- (β) is the natural AVE choice if the K4 lattice rest frame is the operative frame
- (α) is the natural choice if galactic-rotation-curve physics (per C13a) is the source of the DM wind
- A third possibility: both frames apply but to different physics (e.g., bulk wind is CMB-frame, but the modulation we DETECT is galactic-frame because of solar orbital geometry)

## Additional missing pieces

Even with Q1 + Q2 resolved, the derivation needs:

3. **v_wind exponent** — no corpus commitment on whether rate scales linearly, quadratically, or otherwise in v_wind. Sagnac-RLVE template is linear (v_network = κ × v_drive); neutron-9s anomaly is qualitative.

4. **Transduction chain** — substrate-driven acoustic event → keV-scale scintillation energy deposit. This is the largest derivation gap; no corpus content. Possibilities:
   - Direct: substrate event excites NaI vibrational mode → de-excites via scintillation
   - Indirect: substrate event couples to electron cloud → keV electron recoil → scintillation
   - Other: phonon → exciton → photon cascade

5. **Q-factor numerics** — multi-galaxy-validation.md asserts amplitude scales with "structural acoustic Q-factor" but provides no numerical handle.

6. **Background rate baseline** — what's the AVE-predicted DC (non-modulated) DAMA count rate? Without this, the modulation amplitude is dimensionless ratio not absolute cpd/kg/keV.

## Scope of work

**If Grant adjudicates Q1 + Q2** + commits to v_wind exponent assumption (linear is the corpus default):
- Estimated **2-3 sessions** of derivation work building on Sagnac-RLVE template + κ-coupling + phonon-tunneling mechanism
- Output would be: closed-form for cpd/kg/keV as f(κ, v_wind, Q, T, …) + comparison to DAMA empirical
- Validation: bottle-vs-beam neutron 9s anomaly should fall out of same machinery as cross-check

**If Grant adjudicates only one of Q1/Q2:**
- The other choice carries proportional uncertainty; derivation can proceed but with explicit alternative-pictures branching

**If Grant defers both:**
- Derivation cannot proceed; row stays TBD-pin in matrix
- C13c META row continues to track the unification gap

## Discriminating outcomes (post-derivation)

- **Outcome A (target match):** AVE-predicted cpd/kg/keV within factor 2-3 of DAMA empirical at canonical κ + v_wind. C14 promotes from TBD-pin descriptive-only to forward-prediction. C13c META gap partially closed (κ_crystal limb derived).
- **Outcome B (OOM off):** AVE-predicted amplitude differs by 10× or more. Indicates wrong operator choice OR wrong v_wind exponent OR wrong transduction; back to Q1/Q2.
- **Outcome C (null prediction):** AVE-predicted amplitude effectively zero (e.g., from saturation or cubic-symmetry suppression). Would parallel C17 walk-back; C14 retires to corroborative-null.

## Falsifier on the derivation framing

If Grant's physics judgment on Q1 + Q2 produces an AVE-distinct prediction that conflicts with COSINE-100 or ANAIS-112 null results (both NaI-based; should match DAMA per the bulk-density framing), the κ_crystal mechanism itself is falsified. This is already the C14 row's discriminative test.

## Cross-references

- [`closure-roadmap.md`](manuscript/ave-kb/common/closure-roadmap.md) §0.5 open scope-correction items
- [`divergence-test-substrate-map.md`](manuscript/ave-kb/common/divergence-test-substrate-map.md) C13c (META) + C14 (DAMA) rows
- [`preferred-frame-and-emergent-lorentz.md`](manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md) (CMB-frame lattice identification)
- [`bullet-cluster.md`](manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/bullet-cluster.md) (transverse-shear framing)
- [`sagnac-rlve.md`](manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md) (κ_entrain linear template)
- [`existing-experimental-signatures.md`](manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/existing-experimental-signatures.md) (bottle-vs-beam neutron 9s as related mechanism)

## Lane attribution

Prereg landed in research/ branch `analysis/divergence-test-substrate-map`. Honest-flag-the-gap status; no derivation attempted. Awaits Grant's physics-judgment call on Q1 + Q2 before any solo derivation session.
