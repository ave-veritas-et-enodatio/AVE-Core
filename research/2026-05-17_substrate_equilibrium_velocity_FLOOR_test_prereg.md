# Substrate-Equilibrium Velocity FLOOR Test — Pre-Registration

**Status:** PRE-REG (2026-05-17 late evening)
**Date:** 2026-05-17 late evening
**Target:** Test the αc/(2π) = 348.2 km/s **FLOOR interpretation** (vs cluster-center interpretation) of the substrate-equilibrium velocity prediction by stratifying the Gaia DR3 sample by Toomre-diagram velocity cuts.

## Working hypothesis

αc/(2π) = 348.2 km/s is the substrate-equilibrium FLOOR. Local-disk-dynamics (Local Bubble + spiral arm streaming + galactic-orbit projection) drive the thin-disk population ~27 km/s above this floor, all CMB-dipole-aligned. **Stellar populations DECOUPLED from local-disk dynamics should cluster CLOSER to the αc/(2π) floor.**

This is testable WITHOUT new data: stratify the existing 29,466-star Gaia DR3 sample by Toomre-diagram velocity cuts (which sort by dynamical class).

## Toomre stratification

- **Thin disk (|v_LSR| < 30 km/s)**: tightly bound to local-disk dynamics, expected to cluster at LSR-CMB velocity (~375 km/s) — **already confirmed in directional test**
- **Thick disk (30 < |v_LSR| < 100 km/s)**: older population, less coupled to local-flow, partially decoupled
- **Halo (|v_LSR| > 100 km/s)**: oldest population, decoupled from disk dynamics, dominated by individual orbital histories
- **Extreme halo (|v_LSR| > 200 km/s)**: counter-rotating or random-orbit halo stars; maximally decoupled from local-flow physics

## Expected outcomes per interpretation

| Interpretation | Thin-disk |v_CMB| | Thick-disk |v_CMB| | Halo |v_CMB| | Mean trend |
|---|---|---|---|---|
| **B-floor (AVE)** | ~375 km/s (LSR + local-flow) | ~360 km/s (less local-flow) | ~350 km/s (close to floor) | DECREASING toward 348 km/s as v_LSR increases |
| **A-center (alternative)** | ~375 km/s | ~375 km/s | ~375 km/s | FLAT (375 km/s is the prediction, not floor) |
| **C-coincidence** | ~375 km/s | ~varies randomly | ~varies randomly | NO TREND |

## Pre-registered outcomes

- **OUTCOME I-floor-confirmed**: Halo |v_CMB| median within 10 km/s of 348 km/s (floor) AND thick-disk between thin-disk and halo. **STRONG positive for floor interpretation**.
- **OUTCOME II-floor-partial**: Halo median between 350-365 km/s (clear DECREASING trend but not all the way to floor). **Qualitative positive**.
- **OUTCOME III-flat**: All populations cluster at ~375 km/s regardless of dynamical class. **A-center interpretation supported**; floor interpretation falsified.
- **OUTCOME IV-mixed**: Halo population has high σ but mean near 0 in CMB-frame (random kinematics). **Substrate-equilibrium interpretation falsified** (would need to explain why dynamics decoupling DESTROYS the alignment).

## Falsifier

If halo population (|v_LSR| > 100 km/s, N~few thousand stars) shows |v_CMB| median ≥ 380 km/s (i.e., HIGHER than thin-disk), the floor interpretation is falsified. The 27 km/s above-floor offset would then be something else (cosmic-scale physics that increases with stellar mobility, not local-disk-specific bulk motion).

## Data source

Existing 29,466-star Gaia DR3 sample from `/tmp/gaia_nearby_gk.csv` (no new download). Stratify by Toomre |v_LSR| velocity cuts using existing Sun-LSR-velocity computation chain in `gaia_directional_analysis.py`.

## Why this is cheap + sharp

- Zero new data download (uses existing 29k-star sample)
- 4-bin stratification (thin disk / thick disk / halo / extreme halo)
- Direct discriminator between floor (B) and center (A) interpretations
- Cleanest single test of the "LSR-class above-floor bulk motion is local-disk-specific" claim

Driver to scaffold: `src/scripts/vol_3_macroscopic/gaia_floor_test.py`
