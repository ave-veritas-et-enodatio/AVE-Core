# KIMS CsI(Tl) Discovery Pass — Cleanest Discriminator for Bulk-EE $T^2_{matched}$ Hypothesis

**Status:** Discovery-pass research doc 2026-05-17 night. Parallel-track to MAJORANA HPGe legacy discovery pass per external-reviewer MED #3 forward item. **Headline finding**: KIMS (Korea Invisible Mass Search) ran a CsI(Tl) crystal array at 24,324.3 kg-days (66.6 kg-years) exposure with NULL result in the 2-4 keVee region — this IS the cleanest existing-data constraint on the bulk-EE framework's $T^2_{matched}$ hypothesis because CsI(Tl) has the SAME rock-salt lattice as DAMA NaI(Tl) but DIFFERENT atomic Z composition (Cs=55, I=53 vs Na=11, I=53). Isolates bulk-EE $T^2_{matched}$ (lattice-geometry-specific) from atomic-$\sigma$ (Z-specific) cleanly.

**Date:** 2026-05-17 night
**Lane:** Research discovery doc (research/ scope; parallel to MAJORANA pattern)
**Triggered by:** External-reviewer MED #3 forward item ("CsI(Tl) discovery pass in parallel with T² derivation work")

## §1 — Why CsI(Tl) is the cleanest discriminator

Per the bulk-EE framework's load-bearing claim (load-bearing discriminator is $T^2_{matched}$ at substrate-matter bulk-impedance interface, lattice-geometry-specific, NOT atomic-Z-specific):

| Detector | Lattice geometry | Atomic Z composition | Discriminates between |
|---|---|---|---|
| **DAMA NaI(Tl)** | Rock-salt | Na (11), I (53), Tl (81) dopant | baseline |
| **COSINE NaI** | Rock-salt | Same atomic content as DAMA | $G_{coherence}$ only (lattice + Z same) |
| **ANAIS NaI** | Rock-salt | Same atomic content as DAMA | $G_{coherence}$ only |
| **MAJORANA HPGe** | Diamond | Ge (32) | $T^2_{matched}$ (different lattice) + $\sigma_{atomic}$ (different Z) — confounded |
| **KIMS CsI(Tl)** | **Rock-salt** (same as NaI!) | **Cs (55), I (53), Tl dopant** (different from NaI) | **$\sigma_{atomic}$ (different Z) at FIXED lattice geometry — ISOLATES Z-vs-lattice contribution** |

KIMS CsI(Tl) is the unique row where lattice is fixed (matches NaI) but atomic Z varies. If bulk-EE framework's $T^2_{matched}$ claim is correct (lattice-geometry-specific, not atomic-Z-specific), then:

- CsI(Tl) at same single-crystal mass and same $G_{coherence}$ should have $T^2_{matched}$ ≈ DAMA NaI(Tl)
- KIMS CsI(Tl) rate per kg should scale from DAMA NaI(Tl) rate as $\sigma_{atomic}(\text{Cs+I})/\sigma_{atomic}(\text{Na+I}) \times \eta_{scintillation}(\text{CsI})/\eta_{scintillation}(\text{NaI})$
- Both factors are standard atomic + materials physics, computable from established cross-section tables and scintillator yields

If bulk-EE framework is WRONG (rate depends on per-electron coupling at atomic-Z scale rather than bulk $T^2_{matched}$):
- KIMS CsI(Tl) prediction would scale differently
- The discriminator gives a clean falsifier

## §2 — KIMS published exposure + analysis (per arXiv:1404.3443)

From the abstract (via WebFetch reconnaissance):

- **Total exposure**: 24,324.3 kg·days ≈ **66.6 kg·years**
- **Energy range**: 2-4 keVee (electron-equivalent energy; the 3.728 keV AVE-predicted line is at the upper edge of this window)
- **Detector**: low-background CsI(Tl) crystal array
- **Result**: "observed energy distribution of candidate events is consistent with null signals"
- **WIMP exclusion**: "the observed limit covers most of the low-mass region of parameter space favored by the DAMA annual modulation signal"
- **Publication**: Phys. Rev. D 90, 052006 (2014) — peer-reviewed full text exists

The KIMS null result was published as a constraint on WIMP parameter space, but the same data implicitly constrains AVE's bulk-EE framework prediction for CsI(Tl) at 3.728 keV.

## §3 — Quantitative constraint computation (rough, pending Figure digitization)

DAMA NaI(Tl) observed rate: $R_{DAMA} = 4.77 \times 10^{-7}$ events/s/kg (2-6 keV integrated)

For KIMS CsI(Tl) at same bulk-EE $T^2_{matched}$ and $G_{coherence}$, predicted rate scaling:

$$R_{KIMS}^{predicted} = R_{DAMA} \times \frac{\sigma_{atomic}(\text{CsI})}{\sigma_{atomic}(\text{NaI})} \times \frac{\eta_{scint}(\text{CsI})}{\eta_{scint}(\text{NaI})} \times \frac{G_{coherence}^{KIMS}}{G_{coherence}^{DAMA}}$$

Photoabsorption cross-sections at 3.728 keV (rough OOM estimates):
- $\sigma_{atomic}(\text{Cs}, 3.728 \text{ keV})$: K-edge of Cs is at 35.99 keV (well above); photoabsorption at 3.728 keV ~ 10⁻²² m² per Cs atom (close to I)
- $\sigma_{atomic}(\text{I}, 3.728 \text{ keV})$: L-edges at 4.56-5.19 keV; near-resonant; ~ 10⁻²² m² per I atom (DAMA case)
- $\sigma_{atomic}(\text{Na}, 3.728 \text{ keV})$: K-edge at 1.07 keV (below); photoabsorption dominated by L-shell ~ 10⁻²⁴ m² per Na atom
- $\sigma$ per molecule: CsI ≈ Cs + I ≈ 2 × 10⁻²² m²; NaI ≈ Na + I ≈ I-dominated ≈ 10⁻²² m²
- Ratio σ(CsI)/σ(NaI) ≈ 2 (CsI roughly twice as absorbing per molecule)

Per kg scaling:
- N_molecules/kg: NaI (M=150 g/mol) → 4.01e24; CsI (M=260 g/mol) → 2.32e24
- Per-kg cross-section ratio: (CsI σ × N_mol)/(NaI σ × N_mol) = 2 × (2.32e24/4.01e24) = 2 × 0.58 = 1.16
- So σ × N_atoms per kg roughly comparable between CsI and NaI

Scintillation efficiency:
- NaI(Tl): ~38 photons/keV (one of brightest scintillators)
- CsI(Tl): ~52 photons/keV (even brighter, established materials data)
- Ratio η(CsI)/η(NaI) ≈ 1.4

If $G_{coherence}^{KIMS}/G_{coherence}^{DAMA} \approx 1$ (KIMS uses commercial CsI(Tl) of presumably comparable quality to DAMA's Beam International NaI(Tl)):

$$R_{KIMS}^{predicted} \approx R_{DAMA} \times 1.16 \times 1.4 \times 1 \approx 1.6 \times R_{DAMA} \approx 7.6 \times 10^{-7}\,\text{events/s/kg}$$

KIMS observed: NULL (per published limit, presumably $\lesssim 5 \times 10^{-8}$ events/s/kg at 90% CL — quantitative limit requires Figure 1 digitization).

**If KIMS null is genuinely at $R \lesssim 5 \times 10^{-8}$ events/s/kg at 3.728 keV**:
- Predicted (bulk-EE, $\kappa_{quality}=1$): $\sim 7.6 \times 10^{-7}$
- Constraint ratio: ≥15× discrepancy at $\kappa_{quality} = 1$
- Required $G_{coherence}^{KIMS} / G_{coherence}^{DAMA} \lesssim 0.07$

This means CsI(Tl) coherence factor must be ~14× LOWER than DAMA NaI(Tl) for the bulk-EE framework to remain consistent. Plausible (KIMS uses commercial CsI(Tl) which may have lower coherence-quality than DAMA's Beam International high-quality NaI(Tl) batch); but quantitatively constrains the framework.

## §4 — Comparison with cycle-8 MAJORANA HPGe constraint

Cross-detector constraint pattern (cumulative as of 2026-05-17 night):

| Detector | Inferred $\kappa_{quality}$ at rough OOM | Constraint source |
|---|---|---|
| DAMA NaI(Tl) Beam International | ~1.0 | 0.6% match to 4π/N² per-electron formula |
| COSINE-100 NaI | $\lesssim 0.1$ | <10% DAMA modulation amplitude per published limits |
| ANAIS-112 NaI | $\lesssim 0.1$ | <10% DAMA modulation amplitude per published limits |
| **MAJORANA HPGe** | $\lesssim 0.05$ | Implicit null at 3.728 keV (cycle-8 discovery pass) |
| **KIMS CsI(Tl)** (NEW) | $\lesssim 0.07$ (rough) | KIMS null at 2-4 keVee, 66.6 kg-year exposure |

KIMS adds a 4th constraint on the κ_quality variation requirement. The bulk-EE framework's HYPOTHESIS that κ_quality (now identified as G_crystal-coherence + T²_matched composite) varies by factor 10-100 across detectors must explain ALL four constraints quantitatively.

CRITICAL: KIMS CsI(Tl) has same lattice geometry as DAMA NaI(Tl) → if bulk-EE framework's $T^2_{matched}$ is truly lattice-geometry-dependent (not atomic-Z-dependent), then both DAMA and KIMS have $T^2_{matched} \approx 1$, and the constraint is on $G_{coherence}$ alone. This is the CLEANEST single-parameter constraint from existing data.

If KIMS $G_{coherence}$ derivation lands at $\lesssim 0.07 \times G_{DAMA}$ from materials-science crystal-quality differences (Beam International high-quality NaI(Tl) vs commercial CsI(Tl)), the bulk-EE framework remains viable. If $G$ ratio cannot be supported physically (e.g., the crystals are documented as comparable quality), the framework needs walk-back.

## §5 — Next-session work (parallel to T² derivation)

Per reviewer MED #3 recommendation: CsI(Tl) discovery pass runs IN PARALLEL with the bulk-EE T²_matched + G_coherence derivation work.

**Items queued for next-session work**:

1. **Figure 1 digitization of arXiv:1404.3443** to extract published 95% CL upper limit at 3.728 keV in KIMS CsI(Tl) data — analogous to MAJORANA discovery pass next-session item
2. **Materials-science crystal-quality assessment** of KIMS commercial CsI(Tl) vs DAMA Beam International NaI(Tl) (mosaicity, defect density, Tl distribution) — sets prior on plausible $G_{coherence}$ ratio
3. **Bulk-EE forward prediction for KIMS** per the §10 pre-registration pipeline of bulk-EE research doc — compute predicted KIMS rate using derived $T^2_{matched}$(rock-salt) and derived $G_{coherence}^{commercial}$; compare to observed null
4. **Cross-detector consistency check** across DAMA + COSINE + ANAIS + MAJORANA + KIMS using bulk-EE formula — if all four constraints land within factor 3-10 of derived predictions, framework validated; if not, walk back per §10.4 decision-tree

## §6 — Why KIMS is BETTER than HPGe for discriminating bulk-EE framework

Per reviewer MED #3 elevation: CsI(Tl) at same lattice + different Z is THE cleanest discriminator. Compare:

| Detector | What it tests (under bulk-EE framework) | Confounders |
|---|---|---|
| HPGe (MAJORANA / proposed 9.39 kg) | $T^2_{matched}$(diamond) vs $T^2_{matched}$(rock-salt) AND $\sigma_{atomic}$(Ge) vs $\sigma_{atomic}$(NaI) | Both factors vary — can't isolate which dominates |
| Sapphire (proposed 2.64 kg) | $T^2_{matched}$(corundum) vs $T^2_{matched}$(rock-salt) AND $\sigma_{atomic}$(Al+O) vs $\sigma_{atomic}$(NaI) | Both factors vary; commercial Sapphire scintillator-grade crystals don't exist |
| **CsI(Tl) (KIMS or new)** | **$\sigma_{atomic}$(CsI) vs $\sigma_{atomic}$(NaI) at FIXED $T^2_{matched}$(rock-salt)** | Only $G_{coherence}$ varies (crystal-quality) |

CsI(Tl) ISOLATES the $\sigma_{atomic}$ contribution from the $T^2_{matched}$ contribution by holding lattice geometry fixed. This makes it the cleanest single-experiment test of the bulk-EE framework's load-bearing claim (lattice-geometry-specific, not atomic-Z-specific).

**Existing KIMS data already provides this constraint at 66.6 kg-year exposure** — no new hardware needed. The discovery-pass reconnaissance returns favorable outcome.

## §7 — Honest scoping (per ave-discrimination-check)

The KIMS CsI(Tl) constraint depends on:
1. Bulk-EE framework's $T^2_{matched}$ being lattice-geometry-specific (HYPOTHESIS, queued for derivation)
2. Materials-science crystal-quality of KIMS CsI(Tl) vs DAMA NaI(Tl) being assessable (HYPOTHESIS, queued for materials-physics review)
3. Photoabsorption cross-sections at 3.728 keV being accurate to factor 2 (standard atomic-physics data; should be reliable)
4. Scintillation yields being reliable (well-established materials data)

The rough computation in §3 indicates KIMS implicit-null constrains $G_{coherence}^{KIMS}/G_{coherence}^{DAMA} \lesssim 0.07$ at the bulk-EE framework's $\kappa_{quality} = 1$ ceiling. This is plausibly explainable via materials-science crystal-quality variation (commercial CsI(Tl) vs Beam International high-quality NaI(Tl)), but the explanation requires quantitative materials-science derivation that hasn't been done yet.

Per `ave-audit-of-audit`: the bulk-EE framework's prediction for KIMS may need walk-back if materials-science $G$ ratio can't support factor 14× variation between crystal classes.

## §8 — Cross-references

- **External-reviewer MED #3 forward item**: "CsI(Tl) discovery pass in parallel with T² derivation work"
- **KIMS publication**: [arXiv:1404.3443](https://arxiv.org/abs/1404.3443) Phys. Rev. D 90, 052006 (2014) — "Search for Low-Mass Dark Matter with CsI(Tl) Crystal Detectors"
- **Bulk-EE research doc** (where this discovery integrates): [`research/2026-05-17_DAMA-bulk-transfer-function-reframe.md`](2026-05-17_DAMA-bulk-transfer-function-reframe.md) §10 pre-registration pipeline
- **MAJORANA discovery pass** (parallel pattern, cycle-8 cycle): [`research/2026-05-17_MAJORANA-legacy-discovery-pass.md`](2026-05-17_MAJORANA-legacy-discovery-pass.md)
- **HPGe experimental proposal** (now superseded as cleanest discriminator by CsI(Tl) per this finding): [`research/2026-05-17_HPGe-9.39kg-experimental-proposal.md`](2026-05-17_HPGe-9.39kg-experimental-proposal.md) §10 cleanest-test framing should reference CsI(Tl) cohort search as parallel-track
- **Matrix C14 row**: [`manuscript/ave-kb/common/divergence-test-substrate-map.md`](../manuscript/ave-kb/common/divergence-test-substrate-map.md) — update needed to reflect KIMS CsI(Tl) constraint

## §9 — Lane attribution

Discovery pass landed on `analysis/divergence-test-substrate-map` branch as parallel-track to MAJORANA discovery pass (same shape). 30-minute WebSearch + WebFetch reconnaissance returns favorable Outcome 1 (published peer-reviewed paper with quantitative exposure; Figure 1 digitization needed for tight limit per same pattern as MAJORANA). **Cleanest existing-data constraint on bulk-EE framework** — CsI(Tl) at same lattice as NaI but different atomic Z isolates the load-bearing $T^2_{matched}$ claim from atomic-Z confounders. Together with MAJORANA HPGe constraint and COSINE/ANAIS NaI constraints, KIMS bounds the bulk-EE framework parameter space across 4 independent detector classes spanning 2 lattice geometries (rock-salt + diamond) and multiple atomic-Z compositions. Forward-prediction validation per bulk-EE research doc §10 pipeline gets KIMS as the most discriminating data point.

Sources:
- [arXiv:1404.3443 — Search for Low-Mass Dark Matter with CsI(Tl) Crystal Detectors](https://arxiv.org/abs/1404.3443)
- [Phys. Rev. D 90, 052006 (2014)](https://doi.org/10.1103/PhysRevD.90.052006)
