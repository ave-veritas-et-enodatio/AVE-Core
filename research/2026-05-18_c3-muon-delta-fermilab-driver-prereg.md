# C3-MUON-DELTA Fermilab Driver — Pre-Registration

**Date**: 2026-05-18 evening
**Target**: Build AVE-canonical Fermilab muon g-2 driver per matrix:552 task (now UN-GATED post-FI-13 resolution). Use Q-G27 Cosserat-torsion saliency canonical formula: δ_μ = -3α/2 - α√(3/7)/(2π). Compute Δa_μ^(2) numerically; compare to Fermilab Run-3 tension +245(56)×10⁻¹¹.
**Branch**: `analysis/c3-muon-delta-fermilab-driver`
**Skills applied**: ave-prereg, pre-test-physics-check, substrate-native-check, ave-canonical-source, ave-driver-script-honesty (four-discriminator check), ave-discrimination-check (SM-counterfactual + interpretive alternatives), ave-evidence-framing-discipline (≥3 sig figs), consistency-vs-emergence (Class 3 consistency check with conditional SM-baseline)

## Section 1 — Target

Compute and verify AVE-predicted Δa_μ^(2) Cosserat-torsion contribution; compare against:
- Fermilab Run-1+Run-2 world average: a_μ = 0.00116592055(24) per PRL 131:161802 (2023)
- Fermilab Run-3 tension: a_μ_exp - a_μ_SM = +245(56)×10⁻¹¹

Verify the corpus claim that Q-G27 formula produces +247×10⁻¹¹ (per q-g27:48-50); report what standard QED expansion `a^(2) = C_2 × (α/π)²` ACTUALLY gives when fed the shifted C_2.

## Section 1.5 — Physical picture (5 bullets per pre-test-physics-check)

1. Muon = single-loop (N=1) lepton on (2,3) trefoil topology + 1 Cosserat torsion quantum per FI-13 resolution + Vol 1 Ch 5 + Q-G27 canonical
2. Petermann coefficient C_2 for muon shifts from electron's -0.32848 to -0.32755 via Cosserat-torsion-induced d/q kernel asymmetry
3. δ_Cosserat = -α√(3/7)/(2π) ≈ -7.6×10⁻⁴ adds to electron Petermann base δ_e = -3α/2; full δ_μ = -3α/2 - α√(3/7)/(2π) = -0.01171
4. The +247×10⁻¹¹ corpus claim is "Δa_μ^(2) AVE contribution"; need to verify this arithmetic via direct numerical computation
5. Discrete event: Fermilab measures a_μ; SM-baseline (BMW lattice OR e+e-) is subtracted; AVE Q-G27 prediction matches IF e+e- baseline used (245(56) tension) or doesn't match IF BMW baseline (closes tension)

## Section 2 — Corpus state (verified previously)

Per FI-13 corpus-grep (1cf0227 commit):
- Q-G27 canonical: δ_μ formula at `q-g27:48`
- Q-G19α Petermann baseline: δ_e = -3α/2 at `q-g19a:72`
- Faddeev-Skyrme solver canonical at `constants.py:660-756`
- M_MU canonical at `cosserat.py:552-553` (107.0 MeV, 1.24% off PDG)

Existing g-2 driver: [`src/scripts/vol_2_subatomic/simulate_g2.py`](../src/scripts/vol_2_subatomic/simulate_g2.py) — covers electron Schwinger leading order ONLY; no muon, no Fermilab data ingest.

## Section 3 — Pre-Registration

**Step 3a — Skill discipline classification**:

Per `consistency-vs-emergence` 4-class taxonomy:
- **Class 3 (consistency check)** — AVE provides alternative mechanism (Cosserat torsion) for the observed Fermilab-vs-SM tension. The "match" is conditional on SM-baseline choice (BMW vs e+e-). If BMW lattice prevails, tension dissolves into SM and AVE distinct claim weakens.

Per `ave-discrimination-check` SM-counterfactual:
- SM prediction with BMW lattice: a_μ_SM closes the tension (~0 σ vs Fermilab)
- SM prediction with e+e- data: a_μ_SM leaves +245(56)×10⁻¹¹ tension (~4.2σ)
- AVE Q-G27 predicts +247×10⁻¹¹ contribution
- Discrimination: only IF e+e- baseline is correct does AVE-vs-SM distinction emerge; this is BMW-vs-e+e--conditional

Per `ave-driver-script-honesty` four-discriminator check:
- (1) Hardcoded-literal vs canonical-import: import α, m_e, m_μ from ave.core.constants + ave.topological.cosserat
- (2) Fit-against-target vs forward-prediction: Q-G27 formula is closed-form forward prediction; NOT a fit
- (3) Internal-contradiction: verify the corpus's +247×10⁻¹¹ arithmetic via direct numerical computation
- (4) Silent-overclaim: report errors to ≥3 sig figs; flag SM-baseline conditional explicitly

**Step 3b — Predictions**:

| Quantity | Formula | Expected numerical value |
|---|---|---|
| δ_Cosserat | -α√(3/7)/(2π) | -7.604×10⁻⁴ |
| δ_e (Petermann electron baseline) | -3α/2 | -0.01095 |
| δ_μ total | -3α/2 - α√(3/7)/(2π) | -0.01171 |
| C_2^μ shift (per corpus) | from -0.32848 to -0.32755 | ΔC_2 = +9.30×10⁻⁴ |
| Δa_μ^(2) via (α/π)² × ΔC_2 | standard QED formula | **~5.02×10⁻⁹ = ~5020×10⁻¹²** (will compare to corpus +247×10⁻¹¹) |
| Corpus-claimed Δa_μ^(2) | per q-g27:50 | +247×10⁻¹¹ = +2.47×10⁻⁹ |
| Fermilab Run-3 tension | a_μ_exp - a_μ_SM(e+e-) | +245(56)×10⁻¹¹ |

**Hypothesis**: corpus's "+247×10⁻¹¹" may have an arithmetic factor (could be ½ × my computed 5020×10⁻¹² = 2510×10⁻¹², still off but closer). Driver will compute directly and surface the discrepancy if real.

**Step 3c — Discriminating Outcomes**:

- **Outcome A (PASS, ~30%)**: my direct computation yields ~+247×10⁻¹¹ matching corpus → Q-G27 formula validates as-stated; AVE prediction matches Fermilab Run-3 tension within ±23% measurement uncertainty
- **Outcome B (PARTIAL/CORPUS-ARITHMETIC-FLAG, ~50%)**: my direct computation differs from +247×10⁻¹¹ by factor ~2 → corpus arithmetic flag; either alternative formula in corpus OR genuine corpus error; SURFACE not FIX
- **Outcome C (BMW-BASELINE-DEPENDENT, ~15%)**: regardless of (a) or (b), AVE-vs-SM match depends on BMW vs e+e- adjudication; both predictions in band of Fermilab measurement at current precision; awaits Run-4/5
- **Outcome D (FRAMEWORK FAIL, ~5%)**: my computation gives AVE prediction OUTSIDE Fermilab ±2σ band → Q-G27 mechanism fails at this precision

**Step 3d — Falsifiers**:
1. If my direct calculation gives Δa_μ^(2) outside corpus's claimed +247×10⁻¹¹ by factor >1.5, surface corpus-arithmetic flag (NOT framework failure; just docs honesty)
2. If Run-4/5 (~2026-2027) tightens Fermilab measurement and central value drifts >50×10⁻¹¹ from AVE prediction, Q-G27 mechanism in trouble
3. If BMW lattice consensus prevails over e+e-, AVE-vs-SM distinction at this row weakens

**Step 3e — Driver scope**:

New file: `src/scripts/verify/muon_g2_fermilab_anchor.py`

Must:
- Import from `ave.core.constants` + `ave.topological.cosserat` (no hardcoded α, m_μ, etc.)
- Compute δ_Cosserat, δ_μ, ΔC_2, Δa_μ^(2) directly with explicit formulas
- Pin Fermilab paper citations (PRL 131:161802 2023 for Run-1+Run-2; Run-3 reference)
- Flag BMW vs e+e- SM-baseline dependency explicitly
- Report ALL numerical values to ≥3 sig figs
- Apply 4-discriminator check (honest about corpus arithmetic if discrepancy found)

Result doc: `research/2026-05-18_c3-muon-delta-fermilab-driver-result.md` — log regardless of outcome.

## Section 4 — Falsifier discipline

Pre-reg committed BEFORE running script. Result logged regardless. No outcome rewrite.

## Section 5 — Out of scope

- Resolving BMW vs e+e- SM-baseline dispute (multi-year theoretical debate)
- Fermilab Run-4/5 data (~2026-2027 future)
- Tau g-2 (Q-G27 predicts +490×10⁻¹¹ but not currently measured at this precision)
- Corpus-arithmetic walk-back IF Outcome B (separate cycle per flag-don't-fix)
