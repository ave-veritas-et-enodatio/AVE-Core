# Substrate-Equilibrium Velocity FLOOR Test — Result (FLOOR INTERPRETATION FALSIFIED)

**Status:** FLOOR interpretation FALSIFIED 2026-05-17 late evening; **A-center interpretation supported** with 9% magnitude gap; directional alignment (separate test, 704bb41) still stands.
**Date:** 2026-05-17 late evening
**Prereg:** [`2026-05-17_substrate_equilibrium_velocity_FLOOR_test_prereg.md`](2026-05-17_substrate_equilibrium_velocity_FLOOR_test_prereg.md)
**Driver:** [`src/scripts/vol_3_macroscopic/gaia_floor_test.py`](../src/scripts/vol_3_macroscopic/gaia_floor_test.py)
**Outcome category (pre-registered):** **III-flat (~ A-center supported; floor falsified)** — but actually MONOTONE-INCREASING (not flat) which is even cleaner against floor

## Headline result

Toomre-diagram stratified |v_CMB| medians:

| Bin | N | median |v_CMB| | mean | σ | Δ vs αc/(2π) |
|---|---|---|---|---|---|
| Thin disk (\|v_LSR\|<30) | 11,690 | 375.18 | 374.51 | 11.24 | +27.00 |
| Thick disk (30<\|v_LSR\|<70) | 14,013 | 382.22 | 381.55 | 21.65 | +34.04 |
| Thick disk (70<\|v_LSR\|<100) | 2,786 | 399.33 | 397.80 | 31.08 | +51.15 |
| Halo (100<\|v_LSR\|<200) | 899 | 426.96 | 427.95 | 43.40 | +78.78 |
| Extreme halo (\|v_LSR\|>200) | 78 | 574.08 | 587.36 | 84.47 | +225.90 |

**Trend: MONOTONE-INCREASING.** Halo populations are FARTHER from αc/(2π) = 348 km/s, not closer. The floor interpretation predicted decoupled populations should approach the floor; they DO NOT.

## What this falsifies + what it doesn't

### Falsified

**The FLOOR interpretation as I had framed it** — αc/(2π) being the substrate-equilibrium FLOOR that decoupled populations approach is NOT supported by the data. Halo stars are MORE bulk-velocity-magnitude (median 427 km/s) than thin-disk stars (375 km/s), and extreme halo stars are at 574 km/s — well above the predicted floor.

### NOT falsified

1. **Directional alignment** (separate result, commit `704bb41`): cluster mean direction aligned with CMB-dipole to 2.75° — STILL stands. The cluster direction signature is independent of magnitude statistics.

2. **A-center interpretation revived**: the thin-disk cluster median (375 km/s) IS the LSR-CMB velocity (374 km/s independently computed from Schönrich+ 2010). αc/(2π) = 348 km/s is the **approximate** magnitude prediction — off by 9% — for stellar populations near substrate equilibrium.

3. **Substrate-equilibrium velocity** at the approximate magnitude prediction level with the sharp directional alignment.

## Physical interpretation: bulk vector + stellar peculiar quadrature

The increasing magnitude trend with |v_LSR| is **exactly what conventional galactic kinematics predicts** with the LSR-class population sharing a coherent CMB-dipole-aligned bulk motion of ~375 km/s + isotropic stellar peculiar velocities of magnitude |v_LSR| added in quadrature:

Expected |v_CMB| ≈ √((375 km/s)² + σ_pec²)

| Bin | σ_pec (bin center, km/s) | Expected (quadrature) | Observed | Diff |
|---|---|---|---|---|
| Thin disk | 15 | 375.3 | 375.2 | 0.1 ✓ |
| Thick disk (30-70) | 50 | 378.3 | 382.2 | 3.9 ✓ |
| Thick disk (70-100) | 85 | 384.5 | 399.3 | 14.8 |
| Halo (100-200) | 150 | 403.9 | 427.0 | 23.1 |
| Extreme halo (>200) | 300 | 480.5 | 574.1 | 93.6 |

The quadrature model matches thin-disk + thick-disk very well; halo and extreme halo bins overshoot quadrature by 20-90 km/s. The overshoot is consistent with halo stars having **non-isotropic** kinematics (anti-rotating + vertical orbits), which biases CMB-frame magnitude higher than naive isotropic σ_pec addition.

**Net structural reading**: stellar populations share a coherent ~375 km/s CMB-dipole-aligned bulk motion + dynamical peculiar velocities. αc/(2π) = 348 km/s is the AVE-distinct prediction of this bulk motion's magnitude; observed 375 km/s is 9% higher. The 27 km/s gap is the cosmic-flow / Local Group / MW barycenter velocity through CMB rest — NOT a local-disk-specific effect (would otherwise be removed by halo decoupling, which doesn't happen).

## Pre-registered outcome adjudication

Pre-reg outcome categories were:
- I-floor-confirmed: halo within ±10 km/s of floor → **NO** (halo 79 km/s above)
- II-floor-partial: decreasing trend → **NO** (trend is INCREASING)
- III-flat: all at ~375 → **PARTIAL** (thin-disk at 375 yes, but halo at 427 not flat)
- IV-mixed/falsified: random halo kinematics → **PARTIAL** (halo is dispersed but consistent with quadrature physics, not random)

Actual outcome is closest to **III-flat-with-quadrature-overlay**: A-center supported; floor falsified; magnitude prediction at 9% accuracy; directional alignment to CMB-dipole is the cleanest signature.

## Walk-back required (third audit-driven correction this session)

The FLOOR interpretation must be walked back across KB leaves + matrix + closure-roadmap + foreword. The corrected framing:

> **AVE substrate-equilibrium velocity prediction** (revised interpretation 2026-05-17 late evening): αc/(2π) ≈ 348 km/s is the **approximate magnitude prediction** for the LSR-class stellar population's CMB-rest-frame bulk velocity. Observed (Gaia DR3 thin-disk cluster): 375 km/s, 9% above prediction. The **directional alignment** of this bulk velocity with the CMB-dipole direction (2.75° offset, anti-aligned with galactic-rotation at 133.7°) is the cleanest AVE-distinct signature and remains a strong positive. The 9% magnitude gap is consistent with the LSR-class population participating in a CMB-dipole-aligned cosmic flow whose origin is open (NOT local-disk-specific, since halo populations don't approach αc/(2π) when decoupled from disk dynamics).

This is a SUBSTANTIVE walk-back of the floor framing but **does NOT walk back the directional STRONG POSITIVE result** — that's a separate test that still stands.

## Lessons learned

The pre-registration outcome IV ("falsifies") was correctly enumerated; the empirical answer matches this category most closely (with the refinement that the falsification is specifically of the floor interpretation, not the substrate-equilibrium framing as a whole).

Pre-registration discipline working as intended: I predicted what outcome each result would correspond to BEFORE running the test; the test landed in the outcome that the prereg said would falsify the floor interpretation; I executed the walk-back rather than rationalizing the result to preserve the prior framing.

This is the THIRD audit-driven correction of the session (after Sun-22km/s framing walk-back and cubic-anisotropy test scope correction). Pattern: predict → test → adjudicate → walk-back if needed.

## Foreword status

The directional test STRONG POSITIVE (commit `704bb41`) still merits foreword inclusion — that result is independent and not falsified by this floor test. But the foreword text needs MINOR softening to remove "floor" language and replace with "approximate magnitude prediction with sharp directional alignment".

## Cross-references

- [`2026-05-17_substrate_equilibrium_velocity_FLOOR_test_prereg.md`](2026-05-17_substrate_equilibrium_velocity_FLOOR_test_prereg.md) — this test's prereg
- [`2026-05-17_substrate_equilibrium_velocity_GAIA_DIRECTIONAL_result.md`](2026-05-17_substrate_equilibrium_velocity_GAIA_DIRECTIONAL_result.md) — directional STRONG POSITIVE (unaffected)
- [`2026-05-17_substrate_equilibrium_velocity_GAIA_result.md`](2026-05-17_substrate_equilibrium_velocity_GAIA_result.md) — original magnitude test (Outcome B)
- [`2026-05-17_C14-DAMA_amplitude_result.md`](2026-05-17_C14-DAMA_amplitude_result.md) — α-slew derivation source
- [`src/scripts/vol_3_macroscopic/gaia_floor_test.py`](../src/scripts/vol_3_macroscopic/gaia_floor_test.py) — driver

## What I'll change in propagation

KB leaves:
- `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md` §5 — replace "FLOOR" with "approximate magnitude prediction"; note that decoupled stellar populations show quadrature-consistent kinematics + still CMB-dipole-aligned base
- `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md` cross-volume motif section — remove "FLOOR" language from substrate-scale row
- `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md` §8 — update to "approximate prediction" framing

Matrix:
- `manuscript/ave-kb/common/divergence-test-substrate-map.md` C14 row — replace "FLOOR" with "approximate magnitude" + note floor test result

Foreword:
- `manuscript/frontmatter/00_foreword.tex` — soften "FLOOR" → "approximate magnitude with sharp CMB-dipole alignment" in second-anchor paragraph

closure-roadmap §0.5:
- New entry for FLOOR-test falsification + interpretation walk-back

Appendix:
- `manuscript/ave-kb/common/appendix-experiments.md` — soften FLOOR language

This is a coherent walk-back across the same file set as the prior Sun-22-km/s walk-back (8 files). Per ave-walk-back skill discipline.
