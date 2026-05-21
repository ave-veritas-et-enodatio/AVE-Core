# C14-DAMA Amplitude Derivation — Pre-Registration

**Status:** PREREG with WORKING HYPOTHESIS (updated 2026-05-17 evening). Refresh-rate framing per Grant physical-intuition session adjudicates the prior Q1 + Q2 foundational choices into a single substrate-native picture.

**Date:** 2026-05-17 (initial: morning; refresh-rate update: evening)
**Author:** agent + corpus-grep audit (agentId: adcb9b4429afd35e4); refresh-rate hypothesis per Grant
**Matrix row:** C14-DAMA-MATERIAL
**Closure-roadmap item:** §0.5 open scope-correction "DAMA amplitude formula" — now with working hypothesis

## Working hypothesis (Grant 2026-05-17 evening)

**DAMA is a high-Q acoustic interferometer measuring Earth's local refresh-rate modulation in the K4 discrete substrate.** NaI's coherent atomic lattice provides the interferometric baseline; liquid Xe doesn't, so XENONnT sees nothing.

The K4 lattice has spatial pitch $\ell_{node} \approx 3.86 \times 10^{-13}$ m and an intrinsic LC refresh rate per node. Earth moving through the lattice at $v_{wind} = 370$ km/s encounters lattice nodes at local rate $v_{wind}/\ell_{node} \approx 9.6 \times 10^{17}$ Hz per unit perpendicular area. This is the **local refresh rate** — the rate at which Earth samples the substrate's discrete state. Earth's annual orbital ±15 km/s modulates this rate by ~4%; a coherent crystal embedded in Earth detects the rate modulation.

**Not Doppler** (which is wave-frequency shifts). **It's compression of a discrete medium under relative motion** — like driving over a corrugated road: bumps come at a rate set by your velocity / corrugation spacing. Speed up = faster bumps. Constant speed = steady drumming you stop noticing. Annual orbital modulation = your speed varying through the year → bump rate modulates with it.

## Derivation target

Derive the AVE prediction for DAMA/LIBRA's annual modulation amplitude in cpd/kg/keV at 2-6 keV single-hit window, as a function of:
- $\ell_{node}$ (substrate spatial pitch, canonical AVE)
- $v_{wind}$ (Earth velocity through CMB-rest K4 lattice, 370 km/s canonical per Q-G24 preferred-frame leaf)
- $\Delta v_{wind}$ (annual orbital modulation ±15 km/s)
- $\nu_{kin}$ (substrate refresh-viscosity = kinematic mutual inductance, $\alpha c \ell_{node}$)
- $\kappa_{crystal}$ (crystal coupling fraction = density ratio × shear-coherence factor)

Target empirical value: DAMA ~0.0103 cpd/kg/keV at 2-6 keV (single-hit).

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

## Q1 + Q2 adjudication (Grant 2026-05-17 evening — refresh-rate framing)

The two prior open questions (operator choice + frame choice) are resolved by the refresh-rate working hypothesis:

### Q1 resolved — both framings correct, conditional read

Both bulk-density (Framing A) and transverse-shear-modulus (Framing B) framings in the corpus are correct once read as **conditional**:

- **Bulk density** sets the magnitude of the crystal-substrate mutual-inductance coupling fraction (Sagnac-RLVE-like): $\kappa_{crystal} = \rho_{crystal}/\rho_{bulk}$
- **Shear-modulus support** is the BINARY LITMUS TEST for whether $\kappa_{crystal}$ is nonzero at all: solids have G > 0 → can sustain coherent transverse modes → couple ($\kappa > 0$); liquids have G = 0 → atoms dephase individually → no coherent coupling ($\kappa \approx 0$).

So $\kappa_{crystal} = (\rho_{crystal}/\rho_{bulk}) \times \Theta(\text{coherent shear support})$ where Θ is essentially binary (1 for solids, 0 for liquids), modulated continuously by crystal-quality factors (defect density, mosaicity, grain boundaries) — these determine how PERFECTLY the crystal's coherent lattice phase-locks to the substrate refresh rate.

**Plumber framing**: the crystal is a long-baseline interferometer for the substrate's discrete refresh signal. Solid lattice = coherent interferometer arms (atoms at fixed positions, coherent phase-lock); liquid = no interferometer (atoms diffusing, no phase reference). The bulk-density formula gives the right MAGNITUDE for solids; the shear-support requirement is what determines whether the coupling exists at all.

### Q2 resolved — CMB-dipole frame (Framing β) wins

The refresh-rate framing requires the K4 lattice rest frame (= CMB-dipole rest frame per Q-G24) as the operative frame, NOT the galactic-orbit frame. Earth moves through the discrete K4 substrate at $v_{wind} = 370$ km/s (CMB-dipole), encountering lattice nodes at rate $v_{wind}/\ell_{node} \approx 9.6 \times 10^{17}$ Hz per unit perpendicular area. The annual orbital ±15 km/s component modulates this rate by ~4%. This is the operative physics; the galactic-orbit frame is irrelevant because the lattice doesn't rotate with the galaxy.

### Mechanism (refresh-rate working hypothesis)

**DAMA is a high-Q acoustic interferometer measuring Earth's local refresh-rate modulation in the K4 discrete substrate.**

1. **K4 substrate refresh rate** ~ $v_{wind}/\ell_{node} \approx 9.6 \times 10^{17}$ Hz per unit area (Earth's frame)
2. **Annual modulation** ~ 4% from ±15 km/s orbital component
3. **Crystal coherent lattice** acts as a long-baseline interferometer for this discrete refresh signal:
   - Coherent atomic positions across ~10² lattice nodes per atom-pair
   - Phase-locks the refresh signal across the crystal volume → coherent absorption
   - Liquid Xe: no coherent baseline → no phase-lock → no absorption
4. **Energy scale (keV)** comes from coherent multiplication of single-node-encounter momenta ($p \sim \rho_{bulk} \times \ell_{node}^3 \times v_{wind} \approx 1.7 \times 10^{-25}$ kg·m/s = ~2 eV per encounter) by the ~1000 coherent atomic interferometer baseline → ~keV-class recoil per coherent event
5. **Annual modulation amplitude** ∝ $\nu_{kin} \times \kappa_{crystal} \times \Delta v_{wind}$ × (geometric factors)

## Remaining derivation gaps (post-Grant adjudication)

With Q1 + Q2 resolved by the refresh-rate framing, two pieces remain:

1. **Proportionality constant** — the dimensional bridge from $\nu_{kin} \times \kappa_{crystal} \times \Delta v_{wind}$ (units of m³/s²) to cpd/kg/keV. Estimated 1-2 sessions of derivation work using the substrate-native scale constants.

2. **Crystal-quality dependence (COSINE/DAMA tension)** — refining the shear-coherence factor Θ from binary (solid vs liquid) to continuous (defect density, mosaicity, growth temperature). This explains why DAMA and COSINE (both NaI) might see different amplitudes: different crystal quality → different interferometric Q at the substrate refresh rate (~9.6 × 10¹⁷ Hz). Testable via cross-correlation of crystal-quality metrics against observed modulation amplitudes across DAMA / COSINE / ANAIS batches.

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

Prereg landed in research/ branch `analysis/divergence-test-substrate-map`. **Updated 2026-05-17 evening with refresh-rate working hypothesis** per Grant physical-intuition session. Q1 + Q2 resolved (Q1: both framings correct as conditional; Q2: CMB-dipole frame wins). Two derivation gaps remain (proportionality constant + crystal-quality dependence). Estimated 1-2 sessions of derivation work + 1-2 sessions of crystal-quality refinement to close.

## Refresh-rate framing — key plumber statement

> "DAMA is a high-Q acoustic interferometer measuring Earth's local refresh-rate modulation in the K4 discrete substrate. NaI's coherent atomic lattice provides the interferometric baseline; liquid Xe doesn't, so it sees nothing.
>
> Constant velocity (Newton's first law) → no refresh-rate change → no signal.
> Annual orbital modulation (±15 km/s) → modulated refresh rate → detectable signal in coherent matter only.
>
> The energy spectrum (2-6 keV) comes from coherent multiplication of single-node-encounter momenta (~2 eV each) across the crystal's ~1000-atom-pair coherent interferometer baseline → ~keV-class recoils. Liquids can't multiply because they have no coherent baseline."

This refresh-rate framing is conceptually cleaner than Doppler-for-mutual-inductance (which I initially proposed) because it's not a wave-frequency-shift mechanism — it's COMPRESSION OF A DISCRETE MEDIUM under relative motion. Like driving over a corrugated road: the bumps come at a rate set by your velocity × corrugation spacing; constant speed → steady drumming you stop noticing; speed varying → bump rate modulates.
