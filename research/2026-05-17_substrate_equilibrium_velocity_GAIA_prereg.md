# Substrate-Equilibrium Velocity — Gaia DR3 Test Pre-Registration

**Status:** PRE-REG (written 2026-05-17 evening, before driver run)
**Date:** 2026-05-17
**Author:** agent + Grant adjudication on test design
**Target:** Test AVE-distinct prediction `v_substrate = αc/(2π) ≈ 348.2 km/s` for gravitationally-isolated stellar systems against Gaia DR3 nearby-star kinematics
**Cross-ref:** [`2026-05-17_C14-DAMA_amplitude_result.md`](2026-05-17_C14-DAMA_amplitude_result.md) — substrate-equilibrium velocity emerged as positive prediction from α-slew framing of DAMA

## Working hypothesis

AVE predicts that gravitationally-isolated stellar systems equilibrate at:

$$v_{substrate} = \alpha c / (2\pi) = 348.2\,\text{km/s}$$

through the K4 substrate (= CMB rest frame, per Q-G24 preferred-frame leaf). Observed CMB-frame velocities of individual stars differ from this base by peculiar motions (galactic rotation participation + intracluster + local-flow components).

## Pre-test physics check (per pre-test-physics-check skill)

**Q for Grant:** what equilibrium class is the prediction for?

- **Solar System scale** ★ this draft assumes: individual stars in the solar neighborhood, low velocity dispersion (thin-disk G/K dwarfs, NOT halo stars, NOT moving groups), should cluster near αc/(2π) with peculiar-motion scatter
- **LSR scale**: the local kinematic average should be αc/(2π) ± LSR-peculiar — already tested with published values, gives 374 km/s vs 348 prediction = 7.4% high
- **Galactic Center scale**: would predict GC's CMB velocity = αc/(2π) — observed ~550 km/s, fails by 58% (likely wrong equilibrium class)
- **Local Group scale**: would predict LG's CMB velocity = αc/(2π) — observed 627 km/s, fails by 80% (definitely wrong equilibrium class)

**Pre-test computation (no Gaia needed):**

| Frame | CMB velocity (km/s) | Difference from αc/(2π) (km/s, %) |
|---|---|---|
| Sun (Planck 2018) | 370 | +22, +6.3% |
| LSR (Schönrich+ 2010 + Planck) | 374 | +26, +7.4% |
| Galactic Center (LSR + 220 km/s rotation) | 550 | +202, +58% |
| Milky Way (published) | 600 | +252, +72% |
| Local Group barycenter | 627 | +279, +80% |

Working interpretation: AVE prediction applies to LSR-scale equilibrium (thin-disk stars). Sun + LSR match within 6-7%; galactic-and-up fail. Gaia test refines via DISTRIBUTION analysis of nearby thin-disk stars.

## Test design

### Sample selection

Query Gaia DR3 for nearby thin-disk G/K dwarfs with full 6D kinematics:

- **Distance ≤ 100 pc**: `parallax > 10 mas`
- **Has measured radial velocity**: `radial_velocity IS NOT NULL`
- **G/K dwarf color**: `bp_rp BETWEEN 0.6 AND 1.2` (covers G0V through K5V)
- **Thin-disk kinematics**: filter out halo + thick-disk stars by total velocity wrt LSR < 100 km/s (avoids high-eccentric / accreted populations)
- **Quality cuts**: `parallax_over_error > 10`, `radial_velocity_error < 5 km/s`

Expected sample size: ~10,000-50,000 stars. Manageable single CSV download.

### Per-star computation

For each star, compute its velocity vector through CMB rest frame:

1. **Heliocentric velocity vector** (km/s, in galactic coords):
   - From Gaia: ra, dec, pmra, pmdec, parallax, radial_velocity
   - Convert proper motion + parallax to tangential velocity components
   - Combine with radial velocity to get full 3D heliocentric velocity vector
2. **CMB-frame velocity vector** = Heliocentric velocity vector + Sun's CMB velocity vector
   - Sun's CMB velocity: 370 km/s toward (l,b) = (264°, 48°) (Planck 2018)
3. **|v_CMB|**: magnitude of CMB-frame velocity

Output: distribution of |v_CMB| across the sample.

### Statistical analysis

- **Histogram** of |v_CMB|; identify mode, median, mean
- **Subset analyses**:
  - All sample
  - Low-peculiar subset (Toomre-diagram tight cut: |v_total - v_LSR_galactic_rotation| < 30 km/s)
  - By stellar age (if available) — older = more thin-disk-relaxed = closer to equilibrium
  - By distance bin — closest stars least affected by galactic-scale variations
- **Test statistic**: does the mode / median of low-peculiar subset fall within ±10% of αc/(2π) = 348 km/s?

## Pre-registered outcomes

- **Outcome A — CONFIRMED (sharp)**: Low-peculiar subset clusters at 348 ± 20 km/s (within 6%). AVE prediction validated; foreword update with v_substrate as new positive load-bearing zero-parameter prediction.
- **Outcome B — CONFIRMED (broad)**: Low-peculiar subset clusters at 348 ± 50 km/s (within ~15%). AVE prediction validated qualitatively; foreword update conditional on tighter analysis.
- **Outcome C — AMBIGUOUS**: Distribution shows two or more peaks (e.g., one at 348, one at 220 + galactic-rotation effects). Need framework refinement to distinguish equilibrium classes.
- **Outcome D — FALSIFIED**: Distribution centered at galactic-rotation-driven velocity (e.g., 230-270 km/s, expected from MW-frame kinematics), no clustering near 348. AVE Sun-velocity prediction is coincidence; C14 DAMA framing reverts to α-slew without cosmic-velocity claim.

**Falsifier line:** if the low-peculiar G/K dwarf subset has median |v_CMB| outside [200, 500] km/s window, the α-slew cosmic-velocity prediction is falsified at the test's sensitivity.

## Why this is AVE-distinct

The Standard Model offers NO prediction for cosmic velocities — they're set by cosmological initial conditions + gravitational dynamics, not by fundamental constants. αc/(2π) appearing in nearby-star CMB-frame velocity distributions would be:

- **Absurd in SM**: there's no SM mechanism connecting fine-structure constant × c to cosmic kinematics
- **Natural in AVE**: αc/(2π) is the substrate-native α-slew velocity at electron scale, generalized to substrate-rest-frame equilibrium velocity via Hoop Stress 2π projection (parallel to MOND a_0 = cH_∞/(2π) cosmic-scale derivation)

The 6-7% Sun+LSR match is suggestive but not conclusive — a Gaia distribution test on thousands of nearby stars sharpens the prediction substantially.

## Data source + driver scaffold plan

**Source**: Gaia DR3 catalog via direct TAP/ADQL query to ESA Gaia archive
- Public, no API key needed
- TAP endpoint: `https://gea.esac.esa.int/tap-server/tap/sync`
- Query language: ADQL (SQL-like)
- Output: CSV
- Estimated download: 1-50 MB (depending on sample size)

**Driver location** (TBD pending test):
`src/scripts/vol_3_macroscopic/gaia_substrate_equilibrium_test.py`

**Honest scope per `ave-driver-script-honesty` skill:**
- Computes Sun's CMB velocity from Planck 2018 (empirical input, NOT derived)
- Computes each star's heliocentric velocity from Gaia astrometry (empirical input)
- Computes |v_CMB| per star (forward computation, not fit)
- AVE prediction αc/(2π) is canonical (α + c only) — pure derived value
- Comparison: AVE prediction vs distribution mode/median (forward, not fit)

NO fit parameters. Distribution either clusters at 348 km/s or it doesn't. If it does, AVE prediction validated. If not, falsified.

## Cross-references

- [`research/2026-05-17_C14-DAMA_amplitude_result.md`](2026-05-17_C14-DAMA_amplitude_result.md) — α-slew framing source
- [`manuscript/ave-kb/common/divergence-test-substrate-map.md`](../manuscript/ave-kb/common/divergence-test-substrate-map.md) C14 row — substrate-equilibrium prediction surfaced
- [`manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md) — preferred-frame canonical; currently treats Sun's 370 km/s as empirical
- [`manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md) — structural parallel via Hoop Stress 2π projection

## Lane attribution

Prereg on branch `analysis/divergence-test-substrate-map`. Test design uses public Gaia DR3 via direct ADQL/TAP query; no Python package install needed.

If outcome A or B: substantial positive result for AVE (zero-parameter cosmic-velocity prediction matches data); foreword update.
If outcome C or D: substantive negative finding; α-slew Sun-velocity claim retired; DAMA energy-scale closure (α m_e c² = 3.728 keV) still stands independently.
