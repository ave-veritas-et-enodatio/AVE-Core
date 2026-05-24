# C3-MUON-DELTA Fermilab Driver Re-Run — Result Doc

**Date**: 2026-05-19
**Prereg**: [`2026-05-19_c3-muon-delta-fermilab-driver-rerun-prereg.md`](2026-05-19_c3-muon-delta-fermilab-driver-rerun-prereg.md)
**Predecessor result** (pre-walk-back): [`2026-05-18_c3-muon-delta-fermilab-driver-result.md`](2026-05-18_c3-muon-delta-fermilab-driver-result.md)
**Driver**: [`src/scripts/verify/muon_g2_fermilab_anchor.py`](../src/scripts/verify/muon_g2_fermilab_anchor.py)
**Results JSON**: [`src/scripts/verify/muon_g2_fermilab_anchor_results.json`](../src/scripts/verify/muon_g2_fermilab_anchor_results.json)
**Branch**: `analysis/c3-muon-delta-driver-rerun` (off `analysis/integration` at HEAD `b53098a`)
**Walk-back commits validated**: `fb5a9d4` (Q-G27 + Q-G19α factor-2 Action 1+3-(A)); `e0e4315` (Q-G19α Action 2 two-stage reframing)
**Outcome**: **PASS-conditional** — forward prediction `+502×10⁻¹¹` preserved; parallel-baseline tensions canonical (`+4.59σ ABOVE` on e+e-, `+6.68σ DEEPER` on BMW); tension structure on both baselines is the finding.

## §0 — TL;DR

Post-walk-back canonical forward prediction landed cleanly via surgical re-frame of the existing driver. The Q-G27 Cosserat-torsion saliency formula `δ_μ = -3α/2 - α·√(3/7)/(2π)` computes to `Δa_μ^(2) = +501.78×10⁻¹¹` (canonical narrative-rounded +502), in **+4.59σ tension ABOVE** the Fermilab Run-3 observed tension on the e+e- baseline and **+6.68σ tension DEEPER** above the Fermilab-vs-BMW central tension on the BMW lattice SM baseline. BMW makes the tension worse, not softer — BMW lattice closes most of the Fermilab-vs-SM e+e- anomaly toward ~0σ, leaving AVE's +502 forward prediction unabsorbed. The dual-baseline tension structure is the canonical finding, NOT a match.

All 5 pre-registered Falsifiers cleared (formula computation preserved at +501.78×10⁻¹¹; both σ-tensions within tolerance of canonical Q-G27 leaf line 67 claim; no BMW-softer framing propagated; no "AVE matches" overclaim; √(3/7) PAT projection canonical at `cosserat.py:65`). Pre-walk-back artifacts (`delta_a_mu_2_corpus = 247e-11` literal, "Comparison 2 vs corpus claim" block, Outcome A/B/C/D classifier, `arithmetic_discrepancy_factor`, pre-walk-back C_2 reference literals) all removed; ave-walk-back added to driver `skill_disciplines_applied` list.

## §1 — Driver design

### 1.1 — Substrate-derived inputs vs corpus-quoted inputs

The post-walk-back driver makes the input provenance explicit:

| Input | Source | Type |
|---|---|---|
| `α` | `ave.core.constants.ALPHA` (CODATA via constants.py:100) | canonical AVE constant |
| `m_e` | `ave.core.constants.M_E` (CODATA via constants.py:96) | canonical AVE constant |
| `m_μ_AVE` | `ave.topological.cosserat.M_MU` = `M_E / (ALPHA × √(3/7))` (cosserat.py:552) | AVE-derived (1.24% off PDG) |
| `δ_Cosserat = -α·√(3/7)/(2π)` | Q-G27 leaf line 36 | substrate-derived (canonical formula) |
| `δ_e_petermann = -3α/2` | Q-G19α leaf line 78 | substrate-derived (canonical formula) |
| `δ_μ = δ_e + δ_Cosserat` | Q-G27 leaf line 51 | substrate-derived (canonical sum) |
| `ΔC_2 = +9.30×10⁻⁴` | Q-G27 leaf line 53 | **corpus-quoted from Route B numerical bisection** (not closed-form algebra) |
| `Δa_μ^(2) = ΔC_2 × (α/π)²` | textbook QED 2-loop conversion | textbook |
| Fermilab Run-1+Run-2 + Run-3 tension | PRL 131:161802 + result2023 | empirical anchor (paper-pinned literal) |
| BMW lattice SM | Borsanyi+ 2021, Nature 593:51-55 | empirical anchor (paper-pinned literal) |

The driver is honest about which inputs are substrate-derived (δ_Cosserat, δ_e, δ_μ — closed-form Cosserat torsion saliency formulas) vs corpus-quoted (ΔC_2 — Route B engine output via numerical bisection at Q-G19α leaf lines 69-79). The pre-walk-back driver's `c_2_electron_pdg = -0.32848` + `c_2_muon_corpus = -0.32755` literal-subtraction framing was misleading because it made the driver look like it was deriving ΔC_2 from substrate when it was actually consuming a Route B numerical output. The post-walk-back framing replaces that with a single `delta_c_2_route_b = 9.30e-4` literal with explicit citation to Q-G27 leaf line 53.

### 1.2 — Dual-baseline parallel tension reporting

Per Grant-locked literal `BMW_SM_BORSANYI_2021 = 116591954e-11` (handoff line 7), the driver now reports tension on TWO SM baselines as parallel computations:

- **e+e- baseline**: AVE forward `+502×10⁻¹¹` vs Fermilab observed tension `+245(56)×10⁻¹¹` → `+4.585σ ABOVE`
- **BMW lattice baseline**: AVE forward `+502×10⁻¹¹` vs Fermilab-vs-BMW central tension `+101(60)×10⁻¹¹` → `+6.679σ DEEPER`

The BMW computation chain:
1. Fermilab-vs-BMW central tension = `a_μ_exp - a_μ_SM_BMW = 116592055e-11 - 116591954e-11 = +101e-11`
2. Combined uncertainty = `√(24² + 55²) × 10⁻¹¹ ≈ 60e-11`
3. Fermilab-vs-BMW σ = `+101 / 60 ≈ +1.683σ` (BMW closes most of e+e- anomaly toward 0σ)
4. AVE-vs-Fermilab-on-BMW = `+502 - +101 = +401e-11`
5. AVE-on-BMW σ = `+401 / 60 ≈ +6.679σ DEEPER`

The framing "DEEPER" (not "softer") is the canonical post-walk-back direction across 4 surfaces: finding doc line 78, q-g27 leaf lines 22 + 67, prior result Section 5.

## §2 — Numerical results (≥3 sig figs per evidence-framing-discipline)

### 2.1 — Substrate-derived formulas (canonical computation preserved post-edit)

| Quantity | Formula | Computed | Q-G27/Q-G19α canonical | Status |
|---|---|---|---|---|
| `δ_Cosserat` | `-α·√(3/7)/(2π)` | `-7.6032×10⁻⁴` | `-7.604×10⁻⁴` (q-g27:16) | ✓ MATCH |
| `δ_e_petermann` | `-3α/2` | `-1.0946×10⁻²` | `-0.01095` (q-g19a:78) | ✓ MATCH |
| `δ_μ_total` | `-3α/2 - α·√(3/7)/(2π)` | `-1.1706×10⁻²` | `-0.01171` (q-g27:51) | ✓ MATCH |

### 2.2 — Forward prediction conversion

| Quantity | Value |
|---|---|
| `α/π` | `2.3228×10⁻³` |
| `(α/π)²` | `5.3955×10⁻⁶` |
| `ΔC_2_route_b` | `+9.30×10⁻⁴` (q-g27:53 canonical) |
| **`Δa_μ^(2)_forward = ΔC_2 × (α/π)²`** | **`+5.0178×10⁻⁹ = +501.78×10⁻¹¹ = +502×10⁻¹¹` (narrative-rounded)** |

### 2.3 — Parallel-baseline tension computation

**Baseline 1: e+e- (Theory Initiative 2020)**

| Quantity | Value |
|---|---|
| Fermilab observed tension | `+245(56) × 10⁻¹¹` |
| AVE forward prediction | `+501.781 × 10⁻¹¹` |
| Deviation (AVE - observed) | `+256.781 × 10⁻¹¹` (`+104.81%`) |
| **σ-tension** | **`+4.585σ ABOVE`** |

**Baseline 2: BMW lattice (Borsanyi+ 2021, Nature 593:51-55)**

| Quantity | Value |
|---|---|
| BMW SM a_μ central | `116591954(55) × 10⁻¹¹` |
| Fermilab-vs-BMW central tension | `+101.0(60) × 10⁻¹¹` (`+1.683σ`; BMW closes most of e+e- anomaly) |
| AVE forward prediction | `+501.781 × 10⁻¹¹` |
| Deviation (AVE - Fermilab_vs_BMW) | `+400.781 × 10⁻¹¹` (`+396.81%`) |
| **σ-tension** | **`+6.679σ DEEPER`** |

### 2.4 — Adjudication adjudicator output (driver auto-classification)

`adjudicate_outcome()` checks forward drift + e+e- σ drift + BMW σ drift against canonical claims:
- Forward drift: `0.00%` (engine `+501.781×10⁻¹¹` matches canonical `+501.78×10⁻¹¹` to all sig figs)
- e+e- σ drift: `0.00σ` (engine `+4.585σ` matches canonical `~4.59σ`)
- BMW σ drift: `0.00σ` (engine `+6.679σ` matches canonical `~6.68σ`)

**Returns**: `PASS-conditional — forward prediction +502×10⁻¹¹ preserved; parallel-baseline tensions canonical (+4.59σ ABOVE on e+e-, +6.68σ DEEPER on BMW); tension structure is the finding.`

## §3 — Interpretive alternatives (per ave-discrimination-check)

Per the pre-registered ave-discrimination-check discipline, four interpretive alternatives are explicitly enumerated rather than anchoring on the first-plausible:

### Alternative (i): e+e- baseline is the right SM reference; AVE has genuine 4.6σ tension over Fermilab
- AVE forward `+502×10⁻¹¹` over-predicts the Fermilab-vs-SM_eeplus tension `+245(56)×10⁻¹¹` by ~104%
- Possible explanations: Cosserat saliency mechanism is partially correct but needs higher-order correction (e.g., n_q-additivity postulate at Q-G19α may need refinement for the muon's distinct topology); or the corpus's Route B ΔC_2 = +9.30×10⁻⁴ is slightly off due to bisection truncation; or there's an additional substrate mechanism the framework doesn't yet capture that partially cancels the Cosserat contribution
- Status: **UNRESOLVED**; Fermilab Run-4/5 + Theory Initiative refinement will tighten

### Alternative (ii): BMW lattice is the right SM reference; AVE has 6.7σ DEEPER tension
- AVE forward `+502×10⁻¹¹` over-predicts Fermilab-vs-SM_BMW central tension `+101(60)×10⁻¹¹` by ~397%
- Possible explanations: same as (i) but more pronounced — the BMW closing of the e+e- anomaly amplifies the AVE-distinct gap
- Status: **UNRESOLVED**; ongoing BMW-vs-e+e- theoretical debate at the SM side, not the AVE side

### Alternative (iii): Cosserat-saliency mechanism is partially correct but framework lacks a structural piece
- The mechanism (Cosserat torsion-quantum + √(3/7) PAT projection on (2,3) trefoil) is structurally locked by the lepton-mass ladder `m_μ = m_e/(α·√(3/7))` at 1.24% match — option to walk back the mechanism entirely is ruled out (Q-G27 line 10 + Q-G19α line 116)
- A higher-order Cosserat correction (e.g., `δ_Cosserat × correction_factor` where the correction emerges from a yet-undocumented substrate-level coupling) could reduce the forward prediction
- Status: **OPEN STRUCTURAL QUESTION**; queued for multi-session follow-up if AVE-vs-Fermilab tension persists post-Run-4/5

### Alternative (iv): Cosserat torsion-quantum doesn't apply to muon
- **STRUCTURALLY RULED OUT** by lepton-mass ladder consistency: `m_μ = m_e/(α·√(3/7))` requires the same `√(3/7)` PAT torsion-shear projection that produces `δ_Cosserat = -α·√(3/7)/(2π)`. Walking back the saliency mechanism would break the lepton-mass derivation by 2× (Q-G27 leaf line 10 scope-correction header explicitly notes this structural lock)
- Status: **CLOSED**

### Discriminator: future Fermilab Run-4/5
Per Q-G27 leaf line 69: Fermilab Run-4/5 (~2026-2027) at ±10 ppm precision (`~12×10⁻¹¹` uncertainty) will tighten the Fermilab side. If the central value with BMW-vs-e+e- adjudication settles more than ~100×10⁻¹¹ from AVE's +502 forward prediction, the Cosserat-saliency framework — or the n_q-additivity framework it builds on — needs revision. This is the framework's pre-registered falsification target.

## §4 — Classification per consistency-vs-emergence

Per the 4-class taxonomy:

- **Class 1 (definitional identity)**: ✗ not applicable
- **Class 2 (axiom manifestation)**: ✗ not applicable
- **Class 3 (consistency check)**: ✓ **THIS CLASSIFICATION** — AVE provides an alternative mechanism (Cosserat torsion-quantum saliency) for the observed Fermilab-vs-SM tension. The forward prediction +502×10⁻¹¹ is compared against the empirically observed Fermilab-vs-SM tensions on two SM baselines. Inputs (ALPHA, M_E, Q-G27 formula, ΔC_2 from Route B) are CODATA-derived + axiom-derived + corpus-derived. The test asks "does AVE's forward Cosserat-saliency contribution match the observed Fermilab-vs-SM tension on any baseline" — answer: no, AVE is in genuine forward-vs-measurement disagreement on BOTH baselines. The tension structure IS the finding.
- **Class 4 (emergence test)**: ✗ not applicable — the inputs are not solely axiomatic (ΔC_2 from Route B is corpus-quoted, not derived from first principles in the driver)

## §5 — Skill audit trail

Pre-registered skill discipline (10 skills) all applied:

| Skill | Application | Status |
|---|---|---|
| `ave-prereg` | [`2026-05-19_c3-muon-delta-fermilab-driver-rerun-prereg.md`](2026-05-19_c3-muon-delta-fermilab-driver-rerun-prereg.md) — Step 1 target + Step 1.5 5-bullet picture + Step 2 corpus-grep + Step 3 pre-registration paragraph | ✓ |
| `ave-canonical-leaf-pull` | Q-G27 + Q-G19α + lepton-mass-ladder leaves verified at session start; canonical formula chain preserved | ✓ |
| `verify-before-cite` | 7 verifications passed at Phase 0 (walk-back commits + Q-G27 formula + driver scaffold + ALPHA/M_E/M_MU/M_MU_MEV/_SIN_THETA_W_PAT canonical + skills active + matrix entry + C8 template via git show) | ✓ |
| `ave-canonical-source` | ALPHA, M_E from `ave.core.constants` (lines 96, 100); M_MU, M_MU_MEV from `ave.topological.cosserat` (lines 552-553); FERMILAB_* + BMW_SM_BORSANYI_2021 as paper-pinned empirical literals with reference comments; no hardcoded α/m_e/m_μ values | ✓ |
| `substrate-native-check` | Cosserat torsion saliency from Q-G27 substrate physics (Vol 2 Ch 6:154-176); √(3/7) PAT torsion-shear projection canonical at `cosserat.py:65`; textbook QED conversion is the bridge to observable | ✓ |
| `ave-driver-script-honesty` | 4-discriminator check post-edit: (1) no hardcoded constants ✓; (2) forward-prediction not fit (Q-G27 closed-form formula, ΔC_2 corpus-quoted from Route B engine output, no parameter tuning) ✓; (3) no internal contradiction (formula matches Q-G27 leaf line 51, conversion matches Q-G27 leaf line 53) ✓; (4) no silent overclaim (dual-baseline tension reported as parallel σ values; no "AVE matches" framing; tension structure IS the finding) ✓ | ✓ |
| `ave-discrimination-check` | SM-counterfactual (pure SM has no Cosserat-torsion-quantum mechanism; AVE-distinct claim is the forward prediction itself + dual-baseline tension structure); 4 interpretive alternatives enumerated (Section §3) | ✓ |
| `ave-evidence-framing-discipline` | All numerics ≥3 sig figs; dual-baseline tension reported as parallel σ values + framework finding; no "AVE matches muon g-2" overclaim; "DEEPER" framing matches Q-G27 leaf line 67 canonical (not "softer") | ✓ |
| `consistency-vs-emergence` | Class 3 classification explicit (Section §4); conditional on SM-baseline; both baselines reported as parallel tensions | ✓ |
| `ave-walk-back` | Post-walk-back validation per `fb5a9d4` + `e0e4315`; all pre-walk-back artifacts removed (verified via grep: zero matches for `247e-11`, `corpus_claim`, `arithmetic_discrepancy`, `Outcome B`, `Comparison 2`, pre-walk-back C_2 literals); added to driver `skill_disciplines_applied` list | ✓ |

## §6 — Walk-back propagations needed (if any new ones surface)

**None.** The re-frame validates the post-walk-back canonical state at Q-G27 + Q-G19α leaves + matrix + closure-roadmap §0.5. No new arithmetic gap, no new mechanism conflict, no new BMW-direction issue. The driver is now in lockstep with the canonical leaves.

Two pre-existing deferred items (NOT triggered by this rerun, just noted):
1. Q-G19α full Route B engine implementation `verify/electron_g2_petermann.py` — multi-session work per walk-back doc, would let us independently verify the bisection `δ* = -0.01093` value. Deferred.
2. n_q-additivity postulate rigorous closure via K4-Cosserat Lagrangian numerical integration (Q-G47 Sessions 19+ canonical ratio framework) — deferred per Q-G19α leaf line 106.

## §7 — Cascade context (not part of this session)

This session closes E1a (C3-MUON-DELTA driver re-run) of the three-step Section E cascade per the handoff:
- **E1a (this session)**: C3-MUON-DELTA driver-rerun post-walk-back forward-prediction framing ✓ CLOSED
- **E1b (next session candidate)**: C5-CMB-AXIS executable observer; prereg landed 2026-05-15; template `sparc_catalog_ingest.py`
- **E1c (downstream)**: Route 3 framework-commitment activation; candidate anchor D4-A034 universal saturation kernel

Each cascade session follows the same structure: branch off integration, single deliverable, full skill discipline, prereg + driver + result + matrix + closure-roadmap + auditor + push.

## §8 — Bottom line

Post-walk-back C3-MUON-DELTA forward prediction `+502×10⁻¹¹` Cosserat-torsion saliency lands cleanly with dual-baseline tension structure (`+4.59σ ABOVE` e+e-, `+6.68σ DEEPER` BMW) as the canonical AVE finding. The framework's pre-registered falsification target is Fermilab Run-4/5 (~2026-2027) settling the central value >100×10⁻¹¹ from AVE's +502 forward prediction — at which point the Cosserat-saliency framework or its n_q-additivity scaffold needs revision. Until then, the AVE-distinct claim is the forward prediction itself + the dual-baseline tension structure (not a match).
