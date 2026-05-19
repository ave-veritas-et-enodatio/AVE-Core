# Systemic Factor-2 Conversion Error in AVE g-2 Derivations (Q-G27 + Q-G19α)

**Date**: 2026-05-18 late evening
**Branch**: `analysis/q-g19a-electron-petermann-driver`
**Related branches**: `analysis/c3-muon-delta-fermilab-driver` (06e42f4)
**Origin**: ave-auditor sweep of `09_computational_proof.tex:62-103` anomaly catalog identified Q-G19α as priority #1 follow-up after C3 driver surfaced Q-G27 factor-2 arithmetic flag. Direct arithmetic verification at Q-G19α confirms the systemic pattern.

## Section 1 — Confirmed systemic findings

### 1a — Q-G19α electron Petermann factor-2 conversion error (NEW, 2026-05-18 late evening)

[`manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md:82`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md):

> "Δa_e^(2),AVE = -8.857×10⁻⁷, C_2^AVE = -0.32846"

Direct verification using canonical α from `ave.core.constants.ALPHA`:

```
α/π = 2.322819×10⁻³
(α/π)² = 5.395490×10⁻⁶

Standard QED: Δa_e^(2) = C_2 × (α/π)²
  C_2 (corpus -0.32846) × (α/π)² = -1.772203×10⁻⁶
  C_2 (PDG -0.328479)   × (α/π)² = -1.772305×10⁻⁶

Corpus claim Δa_e^(2),AVE = -8.857×10⁻⁷
My direct calc            = -1.772×10⁻⁶
Ratio corpus/direct       = 0.4998  ← exact factor of 2
```

**Verdict**: same factor-2 conversion error as Q-G27. The C_2 value (-0.32846) is paired with a Δa_e^(2) value that is half what the standard QED formula gives for that C_2.

### 1b — Q-G27 muon Cosserat saliency factor-2 conversion error (CONFIRMED earlier, 06e42f4)

[`manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g27-muon-cosserat-saliency.md:50`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g27-muon-cosserat-saliency.md):

> "producing the observed +247×10⁻¹¹ contribution to a_μ^(2)"

vs direct standard QED with corpus's ΔC_2 = +9.30×10⁻⁴:
```
ΔC_2 × (α/π)² = +9.30×10⁻⁴ × 5.395×10⁻⁶ = +501.78×10⁻¹¹
Corpus +247×10⁻¹¹ / Direct +502×10⁻¹¹ = 0.4922  ← exact factor of 2
```

**Verdict**: corpus's +247×10⁻¹¹ is half the standard QED conversion of corpus's own stated ΔC_2.

### 1c — Both at same chapter, same author convention, same "Route B + saliency" framing

`vol2/particle-physics/ch06-electroweak-higgs/`:
- `q-g19a-petermann-saliency-closure.md` (electron)
- `q-g27-muon-cosserat-saliency.md` (muon)

Same factor-2 substitution pattern. Almost certainly the same author applied the same wrong conversion convention to both leaves.

## Section 2 — Implications when corrected

**Critically**: applying the factor-2 correction gives OPPOSITE outcomes for the two predictions.

### 2a — Electron: prediction STRENGTHENS substantially

| Quantity | Corpus (uncorrected) | Direct (corrected) | Measured |
|---|---|---|---|
| Δa_e^(2),AVE | -8.857×10⁻⁷ | **-1.772×10⁻⁶** | -1.766×10⁻⁶ (from PDG decomp) |
| a_e = α/(2π) + Δa_e^(2) | 1.160524×10⁻³ | **1.159638×10⁻³** | 1.159650×10⁻³ |
| Deviation from measured | +750 ppm (corpus claims +0.075%) | **+10 ppm** | — |

If the AVE C_2 = -0.32846 is genuinely substrate-derived (separate audit concern, Section 3), then the **forward AVE prediction matches measured a_e to 10 ppm** — *better* than the 50 ppm headline claim, and 75× better than what the corpus's broken arithmetic reports.

The corpus is currently UNDERSELLING the electron Petermann result.

### 2b — Muon: prediction WEAKENS substantially (4.6σ tension on e+e- baseline)

| Quantity | Corpus (uncorrected) | Direct (corrected) |
|---|---|---|
| Δa_μ^(2),AVE | +247×10⁻¹¹ | **+502×10⁻¹¹** |
| vs Fermilab tension +245(56)×10⁻¹¹ | +0.036σ (excellent match) | **+4.585σ (4.6σ over)** |

If BMW lattice SM baseline prevails, AVE prediction +502×10⁻¹¹ is in *deeper* tension with Fermilab; if e+e- SM baseline prevails, AVE is 4.6σ over the +245 tension. **Either way, the corrected forward prediction does not match Fermilab at the precision Q-G27 claimed.**

## Section 3 — Separate concern: bisection-first / closed-form-after at Q-G19α

Independent of the factor-2 conversion error, the Q-G19α leaf has a structural derivation concern:

[`q-g19a-petermann-saliency-closure.md:63-72`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md):

> "High-precision bisection at N_t = 2×10⁶ locates: δ* = -0.01093, δ*/α = -1.4982. The trefoil topology supplies the closed form cleanly: δ = -α n_q / 2 = -3α/2"

The bisection on the Route B engine FIRST located δ* = -0.01093 that produces PDG's C_2 = -0.32848. The closed form δ = -3α/2 = -0.01095 then differs from the bisection result by 0.12%. The corpus admits at line 98:

> "single remaining intuitive step is the n_q-additivity assumption (each of n_q windings contributes one independent α-order kernel-shift unit, scaling linearly in n_q). Alternatives (√n_q collective, n_q² interference) give wrong magnitudes; additive scaling matches at 0.12% structural agreement"

**This is the structural reverse-fit signature**: bisection identified a target δ that matches PDG; closed form was postulated to align with the bisection; alternative closed forms (√n_q, n_q²) were rejected because they don't match the bisection.

The honest framing: the Route B engine forward-computes C_2 = -0.3416 (4% off PDG) without saliency. WITH saliency postulate δ = -3α/2 (n_q-additive, not yet substrate-derived per line 98), C_2 = -0.32846 (50 ppm). **The 50 ppm match is conditional on the n_q-additivity postulate's correctness.**

## Section 4 — Three orthogonal walk-back actions queued

After Grant adjudicates, three independent walk-back actions are queued:

### Action 1: Factor-2 conversion error fix at BOTH q-g19a:82 AND q-g27:50

**Mechanical fix** — verifiable arithmetic, no physics call needed:
- q-g19a:82: replace `Δa_e^(2),AVE = -8.857×10⁻⁷` with `Δa_e^(2),AVE = -1.772×10⁻⁶`
- q-g19a:90: replace `a_e^(1) + a_e^(2) = 1.16052×10⁻³ ... deviation +0.075%` with `a_e^(1) + a_e^(2) = 1.15964×10⁻³ ... deviation -10 ppm` (or thereabouts — *much closer match than current claim*)
- q-g27:50: replace `+247×10⁻¹¹` with `+502×10⁻¹¹`
- q-g27:54-58 tau prediction (`+490×10⁻¹¹ from 2× muon`): scale doubly, becomes `+1000×10⁻¹¹`
- Matrix C3 row: update Δa_μ^(2) value and σ-tension claim
- closure-roadmap.md §0.5 changelog entry

### Action 2: Honest reframing of "50 ppm headline" at Q-G19α

**Honesty call** — needs Grant's adjudication on framing:
- Current: "AVE-Native Petermann Coefficient: 50 ppm Match via Route B + Saliency"
- Honest alternative: "AVE Route B + Saliency Postulate: 4% Forward / 10 ppm with postulate, conditional on n_q-additivity"

The 50 ppm matches both observations (PDG C_2 and measured a_e) given the bisection-postulated δ = -3α/2 input. Whether to count this as a forward prediction, a postulate-conditional fit, or a structural conjecture is a framing call.

### Action 3: Honest reframing of "matches Fermilab" at Q-G27

**Honesty call** — needs Grant's adjudication on (A) vs (B):
- (A) Preserve Cosserat-saliency physics; report +502×10⁻¹¹ forward; acknowledge 4.6σ tension with e+e- baseline as a real (BMW-baseline-dependent) prediction-vs-measurement disagreement
- (B) Walk back Cosserat-saliency derivation itself; commission new mechanism that forward-produces ~+247×10⁻¹¹ (likely requires different topology or different conversion convention)

## Section 5 — Cascade affected files (preliminary list — multi-branch walk-back)

Files known to need touch when (A)/(B) and Action 1 land:

**AVE-Core branch `analysis/c3-muon-delta-fermilab-driver`** (existing, 06e42f4):
- closure-roadmap.md §0.5 (audit entry exists, will update with corrected status)

**AVE-Core walk-back propagation (new branch or extension)**:
- manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md (lines 82, 90 minimum; potentially 6 if reframing the headline)
- manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g27-muon-cosserat-saliency.md (lines 16, 50, 54-58)
- manuscript/vol_2_subatomic/chapters/06_electroweak_and_higgs.tex (mirror leaf changes)
- manuscript/vol_2_subatomic/chapters/09_computational_proof.tex (anomaly catalog line 73-74 reframe; line 38-50 verification table may need C_2 update)
- manuscript/ave-kb/common/divergence-test-substrate-map.md (C3 row at line 426, 512, 552, 665 per closure-roadmap)
- manuscript/ave-kb/common/closure-roadmap.md §0.5 (new entries for Q-G19α + corrected Q-G27)
- manuscript/ave-kb/common/appendix-experiments.md (electron g-2 + muon g-2 entries)
- manuscript/frontmatter/00_foreword.tex (if 50 ppm electron is foreword-promoted)
- src/scripts/verify/muon_g2_fermilab_anchor.py docstring (update once canonical Δa_μ^(2) value is decided)
- NEW: src/scripts/verify/electron_g2_petermann.py (full Route B engine implementation — multi-session work; not blocking the arithmetic fix)

**Cross-repo**:
- AVE-QED, AVE-HOPF chapter narratives referencing electron/muon g-2 anchors
- Other repos' README / foreword if they cite the 50 ppm electron headline

## Section 6 — Recommendations (priority order)

1. **PRIORITY 1 — Action 1 (mechanical arithmetic fix)**: factor-2 correction is verifiable arithmetic, no physics call needed. Apply to q-g19a:82, q-g27:50, q-g27:54-58, matrix, closure-roadmap. Surface the resulting CORRECTED forward predictions: electron strengthens (10 ppm), muon weakens (4.6σ tension on e+e-).

2. **PRIORITY 2 — Action 3 (Q-G27 (A) vs (B) framing)**: pending Grant adjudication. After Action 1 lands, the choice becomes: live with 4.6σ tension and present it honestly, OR walk back the Cosserat-saliency mechanism. Cannot decide without you.

3. **PRIORITY 3 — Action 2 (Q-G19α 50 ppm reframing)**: pending Grant adjudication on whether to keep "50 ppm" headline or reframe as "10 ppm forward (when arithmetic corrected) conditional on n_q-additivity postulate." The reframing is more honest but loses the headline number.

4. **DEFERRED — Q-G19α full Route B engine implementation as verify/electron_g2_petermann.py**: would let us independently confirm the bisection δ* = -0.01093 and reproduce the symmetric Route B 4% base case. Multi-session work; not blocking the arithmetic fix.

5. **DEFERRED — Audit of OTHER anomaly-catalog entries for reverse-fit**: per ave-auditor cycle today, flagged for follow-up: flyby anomaly 13.4 mm/s (no driver), cosmological constant ρ_Λ factor 1.54 (foreword-promoted), water T_m 273.46 K. None as clean-cut as Q-G27/Q-G19α factor-2 case.

## Section 7 — Discipline outcomes

**ave-audit + ave-prereg discipline applied**:
- ✓ Audit dispatched with verified starting state (pre-audit grep at 09_computational_proof.tex)
- ✓ Audit returned systemic-pattern verdict
- ✓ Top-priority audit recommendation (Q-G19α driver) acted on
- ✓ Direct arithmetic verification ran in <5 minutes (didn't need full engine reproduction)
- ✓ Per flag-don't-fix: surfaced the factor-2 inconsistency cleanly; did NOT unilaterally edit any corpus location

**Per ave-evidence-framing-discipline**:
- ✓ All numerics ≥3 sig figs
- ✓ Ratios computed explicitly
- ✓ Both directions of impact (electron strengthens / muon weakens) reported honestly
- ✓ No selective presentation favoring one outcome

**Per executing-actions-with-care**:
- ✓ Multi-branch walk-back NOT executed pending Grant adjudication on (A)/(B) AND on Q-G19α reframing
- ✓ Arithmetic fix (Action 1) is mechanical and uncontroversial but still surfaced for Grant approval before executing

## Section 8 — Net standing

Tonight's three audit-driven findings (C3 driver, prime-N falsification, systemic factor-2):

| Discovery | Direction | Walk-back complexity |
|---|---|---|
| Q-G27 muon factor-2 + reverse-fit | Muon prediction worsens (4.6σ on e+e-) | High — needs Grant (A)/(B) call + multi-file walk-back |
| Prime-N hypothesis falsified | Foundational extension blocked | Zero — never made it to corpus |
| Q-G19α electron factor-2 (NEW) | Electron prediction strengthens (10 ppm) | Medium — arithmetic fix + honest reframing |

**Net framework standing post-tonight (if all walk-backs apply correctly)**:
- Electron Petermann: 10 ppm forward match (better than current 50 ppm headline by 5×, but conditional on n_q-additivity postulate)
- Muon Cosserat-saliency: 4.6σ tension with Fermilab on e+e- baseline (worse than current corpus claim by 130×, but corresponds to genuine forward prediction)
- Loop-count taxonomy + (2,q) odd-q baryon ladder: corpus-canonical and unchanged
- Three confirmed-at-scale anchors (SPARC kpc + LIGO km + C8 baryon ladder fm): unchanged
- A-034 saturation kernel + 21-instance catalog: unchanged

The net is: AVE framework is MORE-correct than the corpus prose currently states for the electron, LESS-correct than the corpus prose currently states for the muon. Both directions are honest moves toward better evidence-framing.
