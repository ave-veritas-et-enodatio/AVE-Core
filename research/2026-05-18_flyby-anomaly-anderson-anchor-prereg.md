# Flyby Anomaly Driver Anderson 2008 Anchor — Pre-Registration

**Date**: 2026-05-18 late evening
**Origin**: ave-auditor priority #3 (after Q-G19α priority #1 / Q-G27 priority #2 from earlier audit cycle 2026-05-18 evening). The auditor flagged the corpus's "13.4 mm/s" claim at [`flyby-anomaly-sagnac-operator.md:22`](../manuscript/ave-kb/vol3/cosmology/ch14-orbital-mechanics/flyby-anomaly-sagnac-operator.md) for missing per-spacecraft input grounding: the value hits the upper bound of the observed 3-13 mm/s range without specifying which spacecraft's geometry produces it.
**Branch**: `analysis/flyby-anomaly-driver`
**Skills applied**: ave-prereg, pre-test-physics-check, substrate-native-check, ave-driver-script-honesty (four-discriminator check), ave-discrimination-check, ave-evidence-framing-discipline

## Section 1 — Target

Verify whether the corpus's AVE Sagnac-RLVE shear-layer formula

$$\Delta V_{flyby} = V_{\infty} \cdot 2 \left( \frac{U_{\oplus}}{C_{0}} \right) \cdot \cos(\alpha_{geo})\cos(\delta_{geo})$$

(at [`flyby-anomaly-sagnac-operator.md:20`](../manuscript/ave-kb/vol3/cosmology/ch14-orbital-mechanics/flyby-anomaly-sagnac-operator.md)) forward-predicts the Anderson et al. 2008 (PRL 100:091102) per-spacecraft flyby anomalies, or whether the "13.4 mm/s" is reverse-fit to the NEAR-Earth observation.

Specific question: applying the formula with each spacecraft's actual V_∞ and orbital geometry, does the predicted ΔV match Anderson's per-spacecraft observations across the 6-flyby anchor set (Galileo I, Galileo II, NEAR, Cassini, Rosetta I, MESSENGER)?

## Section 1.5 — Physical picture (per pre-test-physics-check, 5 bullets)

1. **Sagnac-RLVE shear layer mechanism**: Earth is a solid topological machine deep in Regime IV. At R_⊕ = 6371 km the rigidly-rotating planet shears violently against the surrounding compliant LC vacuum, forming a macroscopic Sagnac shear layer. Boundary rotational velocity is U_⊕ = ω_⊕·R_⊕ ≈ 465 m/s.

2. **Hyper-velocity spacecraft as probe**: a conductive mass-dense spacecraft at V_sc ~ 10 km/s traverses this shear gradient and acquires a phase drag equivalent to a Sagnac loop integral along its trajectory.

3. **Geometric coupling factor**: the cos(α_geo)cos(δ_geo) factor in the formula represents the alignment of the spacecraft's asymptote direction with the Sagnac shear-layer normal — when α=δ=0 (asymptote in equatorial plane and aligned with Earth's rotation axis), maximum coupling; otherwise reduced.

4. **Per-spacecraft prediction**: each Anderson flyby has its own V_∞ (hyperbolic asymptote speed) and orbital geometry (inbound/outbound asymptote right ascensions α_in, α_out and declinations δ_in, δ_out). The formula should produce a distinct ΔV prediction per spacecraft based on these inputs.

5. **Discrete event**: ΔV is measured at perigee — single discrete event per flyby, not a continuous observable. Six events form the Anderson anchor set.

## Section 2 — Corpus state (pre-driver verification)

Per pre-execution corpus-grep:
- **Forward formula**: `flyby-anomaly-sagnac-operator.md:20` — closed-form expression, derives from Sagnac-RLVE mechanism
- **Numerical claim**: `flyby-anomaly-sagnac-operator.md:22` — "intrinsically outputs ΔV ≈ 13.4 mm/s without fitting"
- **Per-spacecraft inputs**: NOT in the leaf. The "13.4 mm/s" value is asserted without specifying V_∞, α_geo, or δ_geo
- **Driver script**: NONE. No `src/scripts/.../flyby*.py` exists at HEAD
- **Anderson 2008 anchor data**: NOT in the corpus. Will need to ingest from PRL 100:091102 Table I

## Section 3 — Pre-Registration

### Step 3a — Skill discipline classification

Per `consistency-vs-emergence` 4-class taxonomy:
- **Class 3 (consistency check)**: AVE provides alternative mechanism (Sagnac shear layer) for the observed Anderson 2008 anomaly. The "match" is conditional on whether the AVE formula per-spacecraft predictions match Anderson's per-spacecraft observations.

Per `ave-driver-script-honesty` four-discriminator check:
1. **Hardcoded-literal vs canonical-import**: C_0, R_E, OMEGA_E imported from `ave.core.constants` (no hardcoded literals)
2. **Fit-against-target vs forward-prediction**: corpus formula is closed-form forward prediction; driver evaluates it per-spacecraft using only public orbital elements; NO fit parameters
3. **Internal-contradiction**: surface mismatch between predicted vs observed per-spacecraft if found
4. **Silent-overclaim**: report all 6 spacecraft individually with explicit per-spacecraft predicted/observed/residual; do NOT aggregate to a "match rate" that obscures bad individual fits

Per `ave-discrimination-check`:
- **Anderson empirical fit (counterfactual)**: `ΔV/V_∞ = (2ω_E R_E/c) · (cos δ_in − cos δ_out)` — uses DIFFERENCE of in/out declinations, not product of α and δ. If AVE formula matches Anderson's, the mechanisms are observationally equivalent at this dataset (degenerate).
- **GR Lense-Thirring (counterfactual)**: ΔV ≈ 10⁻⁶ mm/s — categorically too small (10⁶× off); corpus claim that AVE supersedes GR here is uncontested
- **Spacecraft thermal recoil (counterfactual)**: heuristic per-spacecraft fits — corpus claim that AVE supersedes these depends on AVE being parameter-free; driver must validate this

### Step 3b — Predictions

| Spacecraft | V_∞ (km/s) | Observed ΔV (mm/s) | AVE forward (range) |
|---|---|---|---|
| Galileo I (Dec 1990) | 8.949 | +3.92 ± 0.30 | TBD per driver |
| Galileo II (Dec 1992) | 8.877 | -4.6 ± 1.0 | TBD per driver |
| NEAR (Jan 1998) | 6.851 | +13.46 ± 0.13 | TBD per driver |
| Cassini (Aug 1999) | 16.01 | -2 ± 1 | TBD per driver |
| Rosetta I (Mar 2005) | 3.863 | +1.82 ± 0.05 | TBD per driver |
| MESSENGER (Aug 2005) | 4.056 | +0.02 ± 0.01 | TBD per driver |

**Hypothesis**: corpus's "13.4 mm/s without fitting" likely corresponds to NEAR (+13.46 mm/s observed) computed with that spacecraft's specific V_∞ + geometry. If so, the formula forward-predicts NEAR exactly — but the question is whether it also predicts the OTHER 5 flybys.

If the formula is right for all 6 (or at least within Anderson uncertainties for 4+ of 6), AVE has a real forward prediction. If it only works for NEAR and fails for the other 5, the "13.4 mm/s" is a per-spacecraft-cherry-picked outcome and the broader claim is overstated.

### Step 3c — Discriminating outcomes

- **Outcome A (FULL PASS, ~20%)**: AVE formula matches Anderson's observations for 5/6 or 6/6 spacecraft within ±1σ. Real forward prediction. Headline: "AVE Sagnac-RLVE predicts all 6 Anderson flybys at parameter-free closed form."
- **Outcome B (PARTIAL PASS, ~30%)**: formula matches 2-4/6 within ±1σ. Mechanism captures part of the physics; some per-spacecraft variation unexplained. Walk-back to scope-conditional claim.
- **Outcome C (NEAR-ONLY MATCH, ~30%)**: formula matches NEAR's +13.46 mm/s closely but fails for the other 5. "13.4 mm/s" headline is NEAR-specific not general. Walk-back to acknowledge per-spacecraft variation.
- **Outcome D (CONVENTION FORK, ~15%)**: depending on which α_geo/δ_geo convention I use, the formula gives wildly different results across spacecraft. The leaf's `cos(α_geo)cos(δ_geo)` factor is ambiguous without per-spacecraft convention specification. Walk-back to clarify convention OR commission new leaf with explicit per-spacecraft inputs.
- **Outcome E (FALSIFIED, ~5%)**: formula matches NONE of the 6 within ±2σ. Mechanism fails entirely at this dataset.

### Step 3d — Falsifiers

1. If formula gives 0/6 spacecraft within ±2σ of observed, mechanism is falsified (Outcome E)
2. If formula gives NEAR at ~13 mm/s but Galileo I at <1 mm/s or >10 mm/s vs Anderson +3.92, the per-spacecraft variation is not captured (Outcome C)
3. If the leaf's α_geo/δ_geo convention is ambiguous and multiple interpretations give wildly different per-spacecraft results, the formula is under-specified (Outcome D)
4. If the formula matches Anderson's empirical fit `(cos δ_in - cos δ_out)` to higher precision than just Anderson's coincidence, AVE may be deriving Anderson's empirical formula structurally (observationally degenerate, but mechanism-distinct)

### Step 3e — Driver scope

New file: `src/scripts/verify/flyby_anomaly_anderson_anchor.py`

Must:
- Import C_0 from `ave.core.constants`; Earth physical constants (R_E, ω_E) from substrate-canonical sources OR with explicit citation
- Pin Anderson et al. 2008 PRL 100:091102 data with verbatim Table I citation
- Apply AVE formula `ΔV = V_∞ · 2(U_⊕/C_0) · cos(α_geo)cos(δ_geo)` per spacecraft using multiple plausible α_geo/δ_geo conventions (single in-direction, single out-direction, average of in/out, in-out difference) since the leaf doesn't specify
- Compare to Anderson's per-spacecraft observations
- Report ALL 6 spacecraft individually with explicit per-spacecraft predicted/observed/residual + ±σ comparison
- Per discrimination check: also compute Anderson's empirical-fit prediction `(cos δ_in - cos δ_out)` form for comparison (test whether AVE formula = Anderson formula via different convention choice)
- Per flag-don't-fix: surface ambiguity in α_geo/δ_geo convention if found

Result doc: `research/2026-05-18_flyby-anomaly-anderson-anchor-result.md` — log regardless of outcome.

## Section 4 — Falsifier discipline

Pre-reg committed BEFORE running script. Result logged regardless. No outcome rewrite.

## Section 5 — Out of scope

- Pioneer anomaly (separate Tier 3 catalog entry; different observable mechanism)
- LAGEOS / GP-B Lense-Thirring measurements (separate ~10⁻⁶ mm/s observable, GR-dominated)
- AVE formula re-derivation from first principles (corpus claim is the leaf's closed form; driver only verifies)
- Walk-back propagation to other corpus references (gated on outcome)
