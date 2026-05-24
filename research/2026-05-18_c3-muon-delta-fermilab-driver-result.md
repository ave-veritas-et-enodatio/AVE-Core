# C3-MUON-DELTA Fermilab Driver — Result Doc

**Date**: 2026-05-18 evening
**Prereg**: [`2026-05-18_c3-muon-delta-fermilab-driver-prereg.md`](./2026-05-18_c3-muon-delta-fermilab-driver-prereg.md)
**Driver**: [`src/scripts/verify/muon_g2_fermilab_anchor.py`](../src/scripts/verify/muon_g2_fermilab_anchor.py)
**Results JSON**: [`src/scripts/verify/muon_g2_fermilab_anchor_results.json`](../src/scripts/verify/muon_g2_fermilab_anchor_results.json)
**Branch**: `analysis/c3-muon-delta-fermilab-driver`
**Outcome**: **B (CORPUS ARITHMETIC FLAG)** — per flag-don't-fix discipline, surface for Grant adjudication

## Section 1 — Outcome classification

Pre-reg Section 3c discriminating outcomes:
- ✗ Outcome A (PASS, ~30%): direct calc ≈ corpus +247×10⁻¹¹
- ✓ **Outcome B (CORPUS ARITHMETIC FLAG, ~50%): direct calc differs by factor ~2 from corpus**
- ✗ Outcome C (BMW-baseline-dependent, ~15%): both match Fermilab in band
- ✗ Outcome D (FRAMEWORK FAIL, ~5%): direct calc outside Fermilab ±2σ band

**Outcome B confirmed**: my direct standard QED formula `Δa_μ^(2) = ΔC_2 × (α/π)²` gives +501.78×10⁻¹¹; corpus claim at [`q-g27-muon-cosserat-saliency.md:50`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g27-muon-cosserat-saliency.md) is +247×10⁻¹¹. Ratio: corpus / direct = 0.4922 ≈ ½.

## Section 2 — Numerical results (≥3 sig figs per evidence-framing-discipline)

### 2a — Q-G27 canonical formula verification (matches corpus exactly)

| Quantity | Formula | Computed | Pre-reg expected | Status |
|---|---|---|---|---|
| δ_Cosserat | -α√(3/7)/(2π) | -7.6032×10⁻⁴ | -7.604×10⁻⁴ | ✓ MATCH |
| δ_e (Petermann electron baseline) | -3α/2 | -1.0946×10⁻² | -0.01095 | ✓ MATCH |
| δ_μ total | -3α/2 - α√(3/7)/(2π) | -1.1706×10⁻² | -0.01171 | ✓ MATCH |

**Q-G27 formula is correct as stated.** The δ values match the corpus to all reported sig figs. The discrepancy is purely in the downstream conversion δ → Δa_μ^(2).

### 2b — C_2 shift and Δa_μ^(2) standard QED conversion

Per corpus framing at [`q-g27:48-50`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g27-muon-cosserat-saliency.md):
- C_2 electron baseline: -0.32848 (PDG)
- C_2 muon shifted: -0.32755 (AVE Q-G27)
- ΔC_2 = +9.30×10⁻⁴ (+0.283%)

Standard QED 2-loop formula for the muon anomalous magnetic moment:
```
a_μ^(2) = C_2 × (α/π)²
Δa_μ^(2) = ΔC_2 × (α/π)²
       = (9.30×10⁻⁴) × (5.395×10⁻⁶)
       = 5.018×10⁻⁹
       = +501.78 × 10⁻¹¹
```

**Corpus claim at q-g27:50: +247×10⁻¹¹ = +2.47×10⁻⁹.**

**Direct/corpus ratio: 501.78 / 247 = 2.031.**

### 2c — Fermilab Run-3 tension comparison

| AVE prediction source | Value (×10⁻¹¹) | vs +245(56)×10⁻¹¹ tension | σ |
|---|---|---|---|
| Corpus claim (q-g27:50) | +247.000 | +2.0 (+0.82%) | **0.036σ** ✓ within 1σ |
| Direct formula (this driver) | +501.781 | +256.8 (+104.81%) | **4.585σ** ✗ outside 2σ |

The corpus claim hits the Fermilab tension to within measurement precision.
The direct formula doubles the tension.

## Section 3 — Honest discrepancy analysis (per four-discriminator check D3)

The corpus claim "+247×10⁻¹¹" cannot be derived from the published δ_μ = -0.01171 via the standard QED 2-loop formula `a^(2) = C_2 × (α/π)²`. Direct application of that formula with the corpus ΔC_2 = +9.30×10⁻⁴ gives +501.78×10⁻¹¹.

Three candidate resolutions, none verifiable from current corpus state:

### Hypothesis (i): Corpus has factor-2 arithmetic error
Most parsimonious. q-g27:50 may have applied `½ × ΔC_2 × (α/π)²` (perhaps confusing 2-loop with Schwinger-leading or applying loop-counting that absorbs a 2). If so, the AVE physical prediction is actually +501.78×10⁻¹¹, NOT +247×10⁻¹¹. This would mean AVE is in 4.6σ tension with Fermilab on the e+e- baseline (genuinely concerning).

### Hypothesis (ii): Different conversion convention in corpus
Possible the corpus uses a non-standard 2-loop formula (e.g., Petermann's original 1957 normalization, or a different α scheme). Would require auditing the corpus's conversion chain at q-g27:40-70 against textbook QED conventions.

### Hypothesis (iii): The corpus C_2 shift values are wrong, not the conversion
ΔC_2 = +9.30×10⁻⁴ may not be the correct numerical translation of δ_μ = -0.01171. If the true ΔC_2 ≈ +4.58×10⁻⁴ (half of +9.30×10⁻⁴), then `ΔC_2 × (α/π)² = +247×10⁻¹¹` would match. Would require auditing how Q-G27 derives ΔC_2 from δ_μ in the form-factor expansion.

**Per flag-don't-fix discipline**: I surface this discrepancy without unilaterally choosing. The verification artifact is the driver script + this result doc. Grant adjudicates which resolution path applies, OR commissions a corpus-grep audit of q-g27:40-70 to trace the original arithmetic.

## Section 4 — Pre-registered falsifier discipline

Per prereg Section 3d:
- ✓ Falsifier 1 triggered: "If my direct calculation gives Δa_μ^(2) outside corpus's claimed +247×10⁻¹¹ by factor >1.5, surface corpus-arithmetic flag (NOT framework failure; just docs honesty)" — factor 2.03 triggers this, surfacing as Outcome B
- — Falsifier 2 (Run-4/5 drift, ~2026-2027): not yet evaluable
- — Falsifier 3 (BMW prevails over e+e-): pending theoretical resolution

**Framework status**: NOT failed. The Q-G27 formula structure (δ_Cosserat = -α√(3/7)/(2π)) is verified analytically and arithmetically. The disagreement is at the corpus's stated conversion to Δa_μ^(2), which may be a corpus arithmetic error OR a corpus convention OR a corpus C_2-derivation issue — all three are corpus-internal documentation/derivation questions, not framework-physics questions.

## Section 5 — SM-baseline conditionality (per discrimination-check D3)

Per [`Fermilab Theory Initiative 2020`](https://arxiv.org/abs/2006.04822) and [`BMW 2021`](https://www.nature.com/articles/s41586-021-03418-1):

**If e+e- baseline correct**: SM = a_μ_SM_e+e-; experiment - SM = +245(56)×10⁻¹¹.
- Corpus claim AVE +247×10⁻¹¹ → 0.036σ match (excellent if corpus is right)
- Direct calc AVE +502×10⁻¹¹ → 4.6σ over-prediction (concerning)

**If BMW lattice correct**: SM = a_μ_SM_BMW closes Fermilab tension to ~0σ.
- Corpus claim AVE +247×10⁻¹¹ → AVE in tension with BMW+Fermilab combination
- Direct calc AVE +502×10⁻¹¹ → AVE in deeper tension

**Resolution**: pending 2024-2026 theoretical adjudication + Fermilab Run-4/5 (~2026-2027) at ±10 ppm.

## Section 6 — Walk-back propagation queue (if Grant confirms Hypothesis (i))

If the corpus arithmetic error hypothesis is adjudicated TRUE:

1. **Vol 2 source**: [`manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g27-muon-cosserat-saliency.md:50`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g27-muon-cosserat-saliency.md) — correct +247×10⁻¹¹ → +502×10⁻¹¹ (or whatever the audited true value is)
2. **Matrix C3 row** (`divergence-test-substrate-map.md`): Predictions/Lifecycle/Execution must reflect +502×10⁻¹¹ ≈ 4.6σ tension with e+e-baseline (different ramification entirely)
3. **Supplementary discussion section**: replace +0.036σ framing with honest 4.6σ tension framing
4. **closure-roadmap.md §0.5**: scope-correction changelog entry
5. **appendix-experiments.md**: update entry
6. **Driver script docstring**: update once true value is canonical
7. **Local-only handoff note** in `.agents/handoffs/`

If adjudicated FALSE (i.e., corpus is correct via Hypothesis (ii) or (iii)):

1. Find the corpus's actual derivation of ΔC_2 → Δa_μ^(2) and cite it explicitly in driver script comments
2. Add a "convention note" to driver script explaining the non-standard mapping
3. Matrix C3 row stays at +247×10⁻¹¹ framing

## Section 7 — Discipline outcomes

**9-skill discipline applied**:
- ✓ ave-prereg: full prereg committed before driver execution (7a25b7b)
- ✓ pre-test-physics-check: 5-bullet picture in prereg Section 1.5
- ✓ substrate-native-check: imports from ave.core.constants + ave.topological.cosserat; no hardcoded α, m_e, m_μ
- ✓ ave-canonical-source: M_MU read from cosserat.py:552-553
- ✓ ave-driver-script-honesty: 4-discriminator check applied; D3 (internal-contradiction) caught the arithmetic flag
- ✓ ave-discrimination-check: SM-counterfactual (BMW vs e+e-) + interpretive alternatives (Hyp i/ii/iii)
- ✓ ave-evidence-framing-discipline: all numerics ≥3 sig figs
- ✓ consistency-vs-emergence: Class 3 (consistency check) with conditional SM-baseline
- ✓ verify-before-cite: corpus C_2 values cited verbatim with file:line

**Per flag-don't-fix (user-feedback-binding)**:
- ✓ Surfaced arithmetic discrepancy without unilaterally rewriting corpus or matrix
- ✓ Documented three candidate resolutions without choosing
- ✓ Driver script preserved as audit-trail artifact for future re-runs

## Section 8 — Recommendation to user

**Primary action**: spawn ave-auditor on q-g27:40-70 corpus derivation chain to trace where +247×10⁻¹¹ comes from. Two possibilities:
- Auditor finds the derivation steps with arithmetic and identifies which step has the factor-2 (Hypothesis i true)
- Auditor finds a documented non-standard convention or alternative ΔC_2 derivation (Hypothesis ii or iii true)

**Secondary action**: pending audit outcome, the walk-back propagation per Section 6 either runs (Hyp i) or the driver script gets a "non-standard convention note" added (Hyp ii/iii).

**Then**: continue to Path 2 (prime-N foundational leaf) regardless of audit outcome — the prime-N work is independent of the Q-G27 arithmetic question.
