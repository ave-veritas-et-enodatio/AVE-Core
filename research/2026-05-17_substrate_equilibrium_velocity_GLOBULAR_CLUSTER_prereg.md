# Substrate-Equilibrium Velocity Globular Cluster Test — Pre-Registration

**Status:** PRE-REG 2026-05-17 night (Tier-2 #5 followup to cycle-12 thread; most-informative test per backlog priority analysis).
**Date:** 2026-05-17 night
**Target:** Test the αc/(2π) = 348.2 km/s substrate-equilibrium velocity prediction at the MW globular cluster (GC) population — the most-decoupled-from-disk stellar class available in our Galaxy. Path to SPARC-parity foreword promotion if GC population clusters near αc/(2π) rather than LSR-class bulk velocity (~375 km/s) or quadrature-overlay (~400-420 km/s).

## §0 — Pre-derivation discipline stack invocation (per Grant directive "full skills ahead")

### §0.1 — ave-prereg (corpus-grep for prior substrate-velocity work)

Prior corpus state (verified via prior-doc reads):
- **Magnitude test** (`research/2026-05-17_substrate_equilibrium_velocity_GAIA_result.md`): 29,466 thin-disk G/K dwarfs cluster at 375 km/s, σ=11; αc/(2π) at 4%ile (lower envelope); 9% magnitude gap
- **FLOOR test** (`research/2026-05-17_substrate_equilibrium_velocity_FLOOR_test_result.md`): FLOOR interpretation **FALSIFIED** — halo stars stratified by Toomre |v_LSR| show MONOTONE-INCREASING |v_CMB|: thin disk 375 → thick disk 382/399 → halo 427 → extreme halo 574. Quadrature interpretation (|v_CMB| = √(375² + σ_pec²)) matches thin+thick disk well, halo overshoots by 20-90 km/s (anisotropic kinematics)
- **DIRECTIONAL test** (`research/2026-05-17_substrate_equilibrium_velocity_GAIA_DIRECTIONAL_result.md`): cluster mean direction 2.75° from CMB-dipole; later demoted to "consistency check with K4=CMB identification, not independent AVE evidence" per ave-discrimination-check audit
- **Current canonical interpretation** (`vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md` §5): αc/(2π) is "approximate magnitude prediction for LSR-class stellar bulk velocity through K4 rest frame"; 9% gap is cosmic-flow / Local Group / MW barycenter through CMB rest (NOT local-disk-specific)

**Globular clusters specifically NOT previously tested.** Halo stars were used as "decoupled" proxy in FLOOR test; globular clusters are a cleaner decoupling-class population (they orbit the entire galaxy, NOT bound to local disk dynamics).

### §0.2 — ave-canonical-leaf-pull (canonical leaves)

- [`vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md) §5 — current canonical interpretation
- [`vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md) §4.5 — Cross-volume Hoop Stress 2π substrate motif (v_substrate is the stellar-scale instance)
- [`vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md) §8 — α-slew derivation chain producing the v_substrate = αc/(2π) prediction
- [`vol3/cosmology/ch05-dark-sector/dm-mechanism-unification.md`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dm-mechanism-unification.md) §5.2 — Hoop Stress 2π sub-family (substrate-velocity is row in cross-volume motif table)

### §0.3 — ave-analytical-tool-selection (less applicable to empirical test, but discrimination-criteria framework applies)

This is an empirical test, not a derivation. Toolkit-index tools don't directly apply. Statistical analysis methodology:
- Population statistics: median + mean + σ + N
- Outcome categorization: pre-registered 4-way (FLOOR-confirmed / center-confirmed / quadrature-confirmed / scatter)
- Discriminator: test the three hypotheses simultaneously via comparison to each predicted distribution

### §0.4 — ave-power-category-check (5-axis classification of the prediction)

The substrate-equilibrium velocity v_substrate = αc/(2π) is:
- **Axis A (Real vs Reactive)**: REACTIVE-class — substrate's intrinsic equilibrium drift velocity (Hoop Stress 2π projection of substrate-rate × ℓ_node)
- **Axis B (Propagating vs Bound)**: BOUND-MODE property — substrate's equilibrium-frame velocity, not a propagating wave property
- **Axis C (On-shell vs Off-shell)**: ON-SHELL — substrate-native equilibrium velocity is a measurable consequence of substrate dynamics
- **Axis D (Internal vs External-matched-load)**: BULK substrate property — applies to substrate's relationship to external rest frames
- **Axis E (Substrate-mode vs Atomic-physics)**: SUBSTRATE-MODE — depends only on α, c, and Hoop Stress 2π projection; no atomic-Z dependence

### §0.5 — ave-discrimination-check (alternative interpretations, MUST enumerate before test)

| Alternative | Predicted GC |v_CMB| distribution | Distinguishes via |
|---|---|---|---|
| **AVE substrate-equilibrium FLOOR (original)** | Median ~ αc/(2π) = 348 km/s; GCs decoupled from disk approach the substrate floor | GC median near 348 ± 20 km/s |
| **AVE approximate-magnitude (current canonical)** | GC median tracks MW barycenter motion through CMB (~375 km/s) + quadrature peculiar velocity | GC median ~ √(375² + σ²_GC) ≈ 400-420 km/s |
| **Cosmic-flow only (no substrate-specific physics)** | GC median tracks Local Group / MW barycenter through CMB rest (~543 km/s in Local Group frame); per-GC dispersion adds | GC median ~500-550 km/s (Local Group flow included) |
| **Random kinematics (substrate prediction not applicable)** | GC distribution wide and centered near reference frame motion only | Wide distribution, median near 375 km/s with high σ ≥ 100 |

**Key discriminator**: GC median near 348 km/s = FLOOR validated (BIG positive); near 400-420 km/s = current canonical interpretation validated (small positive, no foreword promotion); near 543 km/s = cosmic-flow dominates (negative for substrate-specific interpretation); wide scatter = test inconclusive.

### §0.6 — ave-canonical-source (constants)

Will use canonical:
- `ALPHA = 7.2973525693e-3` (CODATA)
- `C_0 = 299792458 m/s` (canonical)
- `αc/(2π) = ALPHA × C_0 / (2π) = 348,182 m/s ≈ 348.18 km/s`
- Sun CMB velocity: 370 km/s toward (l, b) = (264°, 48°) galactic — Planck 2018 empirical
- IAU J2000 equatorial-to-galactic rotation matrix — standard
- Sun's LSR motion (Schönrich+ 2010): (U, V, W) = (11.1, 12.24, 7.25) km/s

No new constants required.

## §1 — Why globular clusters specifically

Per the FLOOR test result interpretation: stellar populations share a coherent ~375 km/s CMB-dipole-aligned bulk motion (LSR + cosmic-flow / MW barycenter through CMB rest); halo stars (per Toomre stratification) deviate from this baseline via per-star peculiar velocities added in quadrature.

The FLOOR test used HALO STARS (Toomre |v_LSR| > 100 km/s) as the "decoupled" proxy. But halo stars are still part of the MW disk + halo population — their orbits cross the disk and they're partly coupled to local-disk dynamics.

**Globular clusters are a cleaner decoupling-class population**:
- Orbit the entire galaxy (NOT bound to local disk)
- Formed before the disk (oldest stellar populations in the Galaxy)
- Have stable orbits around galactic center (NOT subject to disk perturbations)
- Discrete population (~160 catalogued for MW) with well-characterized 6D phase-space measurements via Gaia EDR3 (Vasiliev & Baumgardt 2021, [arXiv:2105.04580](https://arxiv.org/abs/2105.04580))

If the FLOOR interpretation has ANY validity (αc/(2π) as substrate-equilibrium velocity for decoupled populations), GCs are the cleanest test:
- Decoupled from local-disk dynamics → no LSR-induced velocity bias
- Bound to MW barycenter (orbit galactic center) → still inherit MW barycenter motion through CMB
- Population-level statistics avoid per-star noise

If GCs cluster at αc/(2π) = 348 km/s rather than at MW barycenter motion (~375 km/s), that's a strong AVE-distinct signature.

## §2 — Pre-registered outcomes (4-way)

### OUTCOME I — FLOOR-confirmed for GCs

GC median |v_CMB| within 10 km/s of αc/(2π) = 348 km/s (i.e., 338-358 km/s range).

**Interpretation**: substrate-equilibrium FLOOR interpretation validated for decoupled-from-disk populations. The FLOOR test result for halo stars was inconclusive because halo stars are partially coupled to disk; GCs are properly decoupled. Foreword DAMA bullet → promotable as 2nd SPARC-class load-bearing empirical anchor.

**Probability assessment (before test)**: LOW (~15-20%) — most likely outcome if substrate-equilibrium FLOOR interpretation has genuine validity.

### OUTCOME II — Current-canonical confirmed (quadrature with MW barycenter)

GC median |v_CMB| in 390-430 km/s range (consistent with √(375² + σ²_GC) quadrature with σ_GC ~ 150-200 km/s typical for GC peculiar velocities).

**Interpretation**: current canonical "approximate magnitude prediction" interpretation validated. αc/(2π) is the substrate's prediction for LSR-class bulk velocity (with 9% cosmic-flow gap); GCs share MW barycenter motion + their own orbital velocity added in quadrature. No foreword promotion; framework consistent.

**Probability assessment (before test)**: HIGH (~55-65%) — most likely outcome if FLOOR test interpretation extends correctly to GC population.

### OUTCOME III — Cosmic-flow dominated

GC median |v_CMB| in 480-560 km/s range (consistent with Local Group flow ~543 km/s).

**Interpretation**: GC population tracks Local Group motion through CMB; substrate-velocity prediction at LSR-scale doesn't extend cleanly to galaxy-scale populations. Walk-back required: the αc/(2π) prediction becomes specifically about LSR-class populations only, not "decoupled populations."

**Probability assessment (before test)**: LOW (~10-15%) — would suggest substrate-velocity is LSR-specific accident.

### OUTCOME IV — Wide scatter / no clear cluster

GC distribution wide (σ ≥ 100 km/s) with median in 350-500 km/s range but no tight clustering.

**Interpretation**: GC population diverse; substrate-velocity prediction not testable at this population level. Test inconclusive.

**Probability assessment (before test)**: MEDIUM (~15-20%) — possible if GC orbits are sufficiently diverse.

## §3 — Falsifier specification (per ave-discrimination-check)

The substrate-equilibrium velocity prediction is FALSIFIED at the GC population level if:

1. **GC median |v_CMB| ≥ 600 km/s** — would indicate GCs are at the cosmic-flow / Local Group scale, NOT substrate-equilibrium scale; AVE substrate-velocity prediction doesn't apply to galaxy-scale dynamics.

2. **GC distribution has σ ≥ 200 km/s with no median preference** — would indicate test population doesn't share any coherent bulk motion; substrate-velocity prediction not applicable at GC scale.

The framework SURVIVES (but does NOT get foreword promoted) if:
- GC median in 380-430 km/s range (Outcome II canonical)

The framework GAINS substantial confidence (and gets foreword promoted) if:
- GC median in 340-360 km/s range (Outcome I FLOOR-confirmed)

## §4 — Discrimination matrix

| Outcome | GC median (km/s) | Framework state after test |
|---|---|---|
| I FLOOR-confirmed | 338-358 | **Foreword promotion**: 2nd SPARC-class anchor; substrate-equilibrium FLOOR interpretation validated for decoupled populations |
| II Canonical confirmed | 390-430 | Current canonical interpretation validated; no foreword promotion but framework consistent |
| III Cosmic-flow dominated | 480-560 | Substrate-velocity → LSR-only walk-back; less general than currently scoped |
| IV Wide scatter | Wide range, ambiguous | Test inconclusive; need cleaner test population OR walk back substrate-velocity prediction entirely |

## §5 — Data source

**Globular cluster catalog**: Baumgardt + Vasiliev 2021 catalog of MW GC positions + velocities, available from [Baumgardt's online table](https://people.smp.uq.edu.au/HolgerBaumgardt/globular/parameter.html) or via Vasiliev & Baumgardt 2021 arXiv:2105.04580 supplementary data.

**Required columns per GC**:
- Galactic longitude (l) [degrees]
- Galactic latitude (b) [degrees]
- Heliocentric distance (d_helio) [kpc]
- Heliocentric radial velocity (rv_helio) [km/s]
- Galactic proper motion (μ_l, μ_b) [mas/yr] or U/V/W galactocentric velocity components

**Sample size**: ~160 MW globular clusters (full catalog) with Gaia EDR3-based 6D phase-space measurements

**No new theoretical work needed**: standard equatorial → galactic → CMB-frame transformation as in `gaia_floor_test.py` driver.

## §6 — Driver scaffold

`src/scripts/vol_3_macroscopic/gaia_globular_cluster_test.py` — new driver patterned on `gaia_floor_test.py` but operating on GC catalog instead of star-by-star Gaia query.

**Reuse from existing driver**:
- Heliocentric → galactic transformation
- Galactic → CMB frame velocity computation (Sun's CMB velocity vector subtraction)
- Median + mean + σ statistics
- Pre-registered outcome categorization

**New for this driver**:
- GC catalog parsing
- Distance-based galactocentric velocity computation (since GC distances are well-known)
- Per-GC outlier handling

## §7 — Why this is highest-info test (per backlog priority analysis)

- **Data availability**: Gaia DR3-based GC catalog publicly available
- **Cost**: ~1 session (data fetch + analysis)
- **Outcome space**: 4 pre-registered outcomes, each with clean interpretation
- **Information value**: HIGH — large prior uncertainty (FLOOR interpretation already walked back; GC test is the next-cleanest decoupling test)
- **Foreword promotion path**: ONLY OUTCOME I leads to foreword promotion (~15-20% probability per prior); but even other outcomes informatively close the substrate-velocity prediction's scope

## §8 — Honest scope caveats

- **Pre-test prior**: Outcome II (~60%) most likely, then Outcome IV (~17%), then Outcome I (~15%), then Outcome III (~8%). If this prior is approximately correct, the test is LIKELY to confirm current canonical interpretation without dramatic update.
- **Selection bias**: GC catalog is biased toward brighter / closer GCs; this should not significantly affect velocity-frame predictions but is worth noting.
- **6D phase-space precision**: Gaia EDR3 measurements have per-GC uncertainties ~10-20 km/s in proper-motion-derived tangential velocity; should not affect median statistics significantly.

## §9 — What this CLOSES (regardless of outcome)

- **Substrate-velocity scope**: clarifies whether αc/(2π) prediction applies to LSR-class only, or extends to GC-decoupled populations
- **Matrix C14 row substrate-velocity entry**: updates with empirical-anchor outcome
- **closure-roadmap §0.5 substrate-velocity entry**: adds 4th iteration of substrate-velocity testing (magnitude + directional + FLOOR + GC = 4)
- **Backlog**: Tier-2 #5 ✓ completed regardless of outcome direction

## §10 — Cross-references

**Upstream**:
- [Substrate-velocity magnitude test](2026-05-17_substrate_equilibrium_velocity_GAIA_result.md)
- [FLOOR test result (interpretation framework)](2026-05-17_substrate_equilibrium_velocity_FLOOR_test_result.md)
- [Cycle-12 parametric coupling kernel canonical leaf](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md) — shares Hoop Stress 2π motif

**Canonical leaves**:
- [Preferred-frame-and-emergent-Lorentz §5](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md)
- [MOND Hoop Stress §4.5 cross-volume substrate motif](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md)
- [DM-mechanism unification §5.2 Hoop Stress 2π sub-family](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dm-mechanism-unification.md)

**Driver pattern**:
- [Existing FLOOR test driver](../src/scripts/vol_3_macroscopic/gaia_floor_test.py)
- [Original directional driver](../src/scripts/vol_3_macroscopic/gaia_directional_analysis.py)

**Downstream (gated on outcome)**:
- New result doc: `research/2026-05-17_substrate_equilibrium_velocity_GLOBULAR_CLUSTER_result.md`
- Matrix C14 row update (regardless of outcome)
- closure-roadmap §0.5 entry (regardless of outcome)
- Foreword DAMA bullet update IF Outcome I (~15-20% prior)
- preferred-frame-and-emergent-lorentz.md §5 update (scope refinement; outcome-dependent)

---

**Prereg landed 2026-05-17 night per Tier-2 #5 followup to cycle-12 canonization. Full 6-skill discipline stack invoked per Grant directive "full skills ahead." Next: pull Baumgardt+Vasiliev 2021 GC catalog data + execute driver + document result.**
