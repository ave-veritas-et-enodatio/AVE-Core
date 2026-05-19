# C3-MUON-DELTA Fermilab Driver Re-Run — Pre-Registration

**Date**: 2026-05-19
**Target**: Re-frame `src/scripts/verify/muon_g2_fermilab_anchor.py` from pre-walk-back "Outcome B (CORPUS ARITHMETIC FLAG)" framing to post-walk-back canonical forward-prediction framing, with numerical BMW-lattice baseline comparison alongside the existing e+e- baseline. Driver already computes the canonical Q-G27 Cosserat-saliency formula `δ_μ = -3α/2 - α√(3/7)/(2π)` correctly and emits `+501.78×10⁻¹¹` at line 89 (matches Q-G27 leaf canonical +502×10⁻¹¹ to round-off); the rerun is surgical re-framing of pre-walk-back narrative artifacts.
**Branch**: `analysis/c3-muon-delta-driver-rerun` (off `analysis/integration` at HEAD `b53098a`)
**Predecessor**: [`2026-05-18_c3-muon-delta-fermilab-driver-prereg.md`](2026-05-18_c3-muon-delta-fermilab-driver-prereg.md) (pre-walk-back; this prereg is its post-walk-back successor)
**Walk-back commits**: `fb5a9d4` (Q-G27 + Q-G19α factor-2 Action 1 + 3-(A)); `e0e4315` (Q-G19α Action 2 two-stage reframing); `a2b4e14` (closure-roadmap §0.5 backfill)
**Skills applied**: ave-prereg (this doc), ave-canonical-leaf-pull (corpus already verified), verify-before-cite (7 verifications passed Phase 0), ave-canonical-source (existing driver imports preserved), substrate-native-check (substrate physics in Q-G27 leaf), consistency-vs-emergence (Class 3 consistency check; conditional SM-baseline), ave-driver-script-honesty (4-discriminator check at Phase 2), ave-evidence-framing-discipline (≥3 sig figs, parallel-baseline tension structure as finding), ave-discrimination-check (SM-counterfactual + interpretive alternatives), ave-walk-back (post-walk-back validation per `fb5a9d4` + `e0e4315`)

## Section 1 — Target

Re-frame the existing C3-MUON-DELTA Fermilab anchor driver per walk-back queue item #6 (driver docstring update once true value is canonical) from prior result doc [Section 6](2026-05-18_c3-muon-delta-fermilab-driver-result.md#section-6). Specifically:

- **Preserve** the canonical Cosserat-saliency formula computation at [lines 70-89](../src/scripts/verify/muon_g2_fermilab_anchor.py:70): `δ_cosserat = -α·√(3/7)/(2π)`, `δ_e_petermann = -3α/2`, `δ_mu_total = -0.01171`, `Δa_μ^(2) = ΔC_2 × (α/π)² = +501.78×10⁻¹¹`.
- **Remove** pre-walk-back artifacts: the `delta_a_mu_2_corpus = 247e-11` literal at line 92, the "Comparison 2: AVE prediction per corpus claim (+247×10⁻¹¹)" block at lines 213-219, the Outcome A/B/C/D classifier at lines 247-268, and the pre-walk-back C_2 literals (`-0.32848`, `-0.32755`) at lines 82-83 which were corpus-quoted reference values for the arithmetic-check, not canonical AVE constants.
- **Add** numerical BMW-lattice baseline tension: introduce `BMW_SM_BORSANYI_2021 = 116591954e-11` (Borsanyi+ 2021, Nature 593:51-55) matching the existing FERMILAB_* paper-pinned literal pattern; compute Fermilab-vs-BMW central tension (+101(60)×10⁻¹¹) and AVE-vs-Fermilab-on-BMW-baseline tension (+401×10⁻¹¹ ≈ +6.7σ DEEPER than e+e- 4.6σ).
- **Replace** Outcome-B (CORPUS ARITHMETIC FLAG) classification with post-walk-back PASS-conditional / FLAG / RETIRE adjudication structure.
- **Update** docstring at lines 1-23 from "Verifies corpus claim of +247×10⁻¹¹" to "Forward-predicts +502×10⁻¹¹ Cosserat-torsion saliency; reports tension on both e+e- (4.6σ above) and BMW (6.7σ DEEPER) baselines."

Output: refreshed `muon_g2_fermilab_anchor_results.json` post-rerun + result doc + matrix C3 row Lifecycle update + closure-roadmap §0.5 entry.

## Section 1.5 — Physical picture (5 bullets per pre-test-physics-check discipline)

1. **Muon topology** — muon = electron $0_1$ unknot on (2,3) phase-space trefoil + 1 Cosserat torsion quantum (per [Vol 2 Ch 6:174](../manuscript/vol_2_subatomic/chapters/06_electroweak_and_higgs.tex) + [Vol 1 Ch 5:39](../manuscript/vol_1_foundations/chapters/05_chiral_solitons.tex) + [Q-G27 canonical](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g27-muon-cosserat-saliency.md)). Real-space soliton is the unknot; the trefoil lives in phase space; the Cosserat quantum is the muon's distinguishing excitation.

2. **Cosserat saliency add-on** — torsion-quantum excitation adds an α-order saliency contribution to the Q-G19α Petermann coefficient framework: `δ_Cosserat^μ = -α·√(3/7)/(2π) ≈ -7.60×10⁻⁴`. The `√(3/7)` factor is the PAT torsion-shear projection from vacuum Poisson ratio `ν_vac = 2/7`. Combined with the universal Petermann baseline `δ_e = -3α/2 ≈ -1.095×10⁻²`, total `δ_μ = δ_e + δ_Cosserat = -1.171×10⁻²`.

3. **Lepton-mass-ladder anchoring** — the SAME `√(3/7)` PAT projection appears in the canonical lepton-mass ladder `m_μ = m_e/(α·√(3/7))` at 1.24% match to measured 105.66 MeV ([torus-knot-uniqueness.md:101](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md:101) + [cosserat.py:65,552-553](../src/ave/topological/cosserat.py:65)). Walk-back option (B) (replace Cosserat-saliency mechanism with half-strength coupling) was structurally ruled out at the 2026-05-18 walk-back because it would break the lepton-mass derivation by 2×.

4. **Textbook QED conversion** — standard two-loop formula `Δa = ΔC_2 × (α/π)²` applied to corpus's own `ΔC_2 = +9.30×10⁻⁴` (from `C_2^μ shifts from -0.32848 to -0.32755` per Route B + saliency) gives forward `Δa_μ^(2) = +502×10⁻¹¹` (501.78 engine-computed). This IS the canonical post-walk-back forward prediction; the prior `+247×10⁻¹¹` corpus claim was a silent factor-of-2 arithmetic error in the conversion step.

5. **Discrete observable + dual SM baselines** — Fermilab measures `a_μ` = 116592055(24)×10⁻¹¹ (Run-1+Run-2 world avg, PRL 131:161802); SM-baseline subtracted via either (a) e+e- data dispersion (Theory Initiative 2020): a_μ_SM_eeplus leaves `+245(56)×10⁻¹¹` tension; or (b) BMW lattice QCD (Borsanyi+ 2021): a_μ_SM_BMW = 116591954(55)×10⁻¹¹ closes the tension to `+101(60)×10⁻¹¹` (1.7σ). AVE forward `+502×10⁻¹¹` sits +4.6σ above the e+e- tension and **+6.7σ DEEPER** above the BMW tension — BMW makes the tension worse because it closes the Fermilab anomaly, leaving AVE's forward prediction unabsorbed. Falsification target: Fermilab Run-4/5 (~2026-2027) at ±10 ppm precision.

## Section 2 — Corpus state (verified at session start)

Per ave-corpus-grep dispatch (2026-05-19 09:30): 

**Locked anchors (post-walk-back canonical)**:
- BMW direction (DEEPER, not softer) — supported at 4 canonical surfaces:
  - [`finding doc:78`](2026-05-18_q-g27-q-g19a-systemic-conversion-error-finding.md:78) "If BMW lattice SM baseline prevails, AVE prediction +502×10⁻¹¹ is in *deeper* tension"
  - [`q-g27 leaf:22`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g27-muon-cosserat-saliency.md:22) "on the BMW lattice SM baseline (which closes the Fermilab tension toward 0σ vs SM), AVE would be in deeper tension"
  - [`q-g27 leaf:67`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g27-muon-cosserat-saliency.md:67) "BMW lattice baseline (which closes the Fermilab measurement toward ∼0σ vs SM), AVE's prediction is in deeper tension"
  - [`prior result:90-98`](2026-05-18_c3-muon-delta-fermilab-driver-result.md) "If BMW lattice correct... Direct calc AVE +502×10⁻¹¹ → AVE in deeper tension"
- `+502×10⁻¹¹` canonical forward value confirmed across 5 leaves (q-g27:4,10,22,65,67) + finding doc + prior result doc + KB index
- `+501.78×10⁻¹¹` is the engine-computed precision value (preserve in driver output)
- √(3/7) PAT projection identity anchors lepton-mass ladder + Q-G27 saliency simultaneously — preserved at [`cosserat.py:65`](../src/ave/topological/cosserat.py:65) `_SIN_THETA_W_PAT: float = sqrt(3.0 / 7.0)`

**Cross-repo state**:
- 11 hardware sibling repos (HOPF/PONDER/APU/Protein/Fusion/Metamaterials/Propulsion/VirtualMedia/Bench/Tesla/Umbrella): zero Q-G27 references — no cross-repo consistency-checking required.
- AVE-QED has cite-only echoes ([`2026-05-13_Q-G27_closure.md`](../../AVE-QED/docs/analysis/2026-05-13_Q-G27_closure.md), [`AVE_QED_synthesis_index.md`](../../AVE-QED/docs/AVE_QED_synthesis_index.md)) already capped with walk-back-correction headers pointing to AVE-Core canonical; no AVE-QED driver re-frame needed.
- `BMW_SM_BORSANYI_2021 = 116591954e-11` is a clean new literal — `grep -rn "116591954\|Borsanyi"` across all 14 repos returns zero canonical numerical cites; introduction does not conflict.

**Surgical-edit targets confirmed in driver**:
- Line 92: `delta_a_mu_2_corpus = 247e-11` → remove
- Lines 82-83: pre-walk-back C_2 literals → remove
- Lines 213-219: "Comparison 2 vs corpus claim" block → remove
- Lines 247-268: Outcome A/B/C/D classifier → replace with post-walk-back PASS-conditional / FLAG / RETIRE
- Lines 231-242: BMW conditionality prose-only block → augment with numerical BMW computation
- Lines 1-23: docstring → rewrite from "verifies corpus claim" to "forward-predicts +502×10⁻¹¹, reports parallel-baseline tensions"
- Lines 298-308: `skill_disciplines_applied` list → add `ave-walk-back`

**Template pattern**:
- [`flyby_anomaly_anderson_anchor.py:189-220, 277-289`](../src/scripts/verify/flyby_anomaly_anderson_anchor.py:189) — per-convention parallel-tension reporting pattern (Conv-A/B/C/D each with own σ) is the structural template for e+e- vs BMW parallel-baseline tension reporting.
- [`baryon_ladder_pdg_2024_anchor.py`](https://example) on `analysis/c8-baryon-ladder-pdg-anchor` branch — readable via `git show` only; provides docstring + result-JSON output format reference for canonical anchor drivers post-walk-back. Pattern preserved.

## Section 3 — Pre-Registration

### Step 3a — Skill discipline classification

Per `consistency-vs-emergence` 4-class taxonomy:
- **Class 3 (consistency check)** — AVE provides alternative mechanism (Cosserat saliency) for the observed Fermilab-vs-SM tension. Comparison is against empirical observable on shared baselines. Inputs (ALPHA, M_E, Q-G27 formula) are CODATA-derived + axiom-derived; the test asks "does the forward +502 prediction match the observed +245 (e+e-) or +101 (BMW) Fermilab-vs-SM tension at any baseline" — answer: no, AVE is in tension on both. The tension structure IS the finding.

Per `ave-discrimination-check`:
- **SM-counterfactual**: pure SM-QED predicts a_μ at the SM-baseline value with no Cosserat-saliency addition. Fermilab measurement deviates from SM on both baselines (e+e- by +245, BMW by +101). AVE's +502 forward prediction is a NEW mechanism (Cosserat torsion-quantum on (2,3) trefoil) that SM has no equivalent for. The AVE-distinct claim is the forward prediction itself, not a match.
- **Interpretive alternatives**:
  - (i) e+e- baseline is right: AVE 4.6σ above the +245 tension — genuine over-prediction, needs further physics (e.g., higher-order Cosserat corrections, or partial-mechanism Cosserat that contributes less than +502).
  - (ii) BMW baseline is right: AVE 6.7σ DEEPER over the +101 tension — even larger gap.
  - (iii) saliency mechanism is partially correct but needs additional structural piece (e.g., generation-dependent suppression factor that the corpus doesn't yet derive).
  - (iv) Cosserat torsion-quantum doesn't apply to muon — STRUCTURALLY RULED OUT by lepton-mass ladder consistency (m_μ = m_e/(α√(3/7)) requires the same √(3/7) projection at 1.24% match).
- **Don't anchor on (i) without enumerating (ii)+(iii)**: the prereg explicitly carries the dual-baseline tension structure forward to the result doc.

Per `ave-driver-script-honesty` four-discriminator check (post-edit):
- (1) Hardcoded-literal vs canonical-import: ALPHA, M_E from `ave.core.constants`; M_MU, M_MU_MEV from `ave.topological.cosserat`; FERMILAB_*+BMW_SM_BORSANYI_2021 as paper-pinned empirical literals with reference comments. No hardcoded α, m_e, m_μ values.
- (2) Fit-against-target vs forward-prediction: Q-G27 formula is closed-form forward prediction; no fit parameter; ΔC_2 = +9.30×10⁻⁴ is corpus-canonical derivation output, not a tuned value.
- (3) Internal-contradiction: formula in code matches formula in Q-G27 leaf at lines 51, 53, 65.
- (4) Silent-overclaim: report tensions on BOTH baselines as parallel σ values; never plot AVE-vs-Fermilab as "match" (the tension structure is the finding).

### Step 3b — Predictions

| Quantity | Formula | Expected numerical value |
|---|---|---|
| δ_Cosserat | -α·√(3/7)/(2π) | -7.604×10⁻⁴ |
| δ_e_petermann | -3α/2 | -1.0946×10⁻² |
| δ_μ_total | -3α/2 - α·√(3/7)/(2π) | -1.1706×10⁻² |
| ΔC_2 | -0.32755 - (-0.32848) | +9.30×10⁻⁴ |
| Δa_μ^(2)_forward (AVE) | ΔC_2 × (α/π)² | **+501.78×10⁻¹¹** (canonical +502) |
| Fermilab Run-1+Run-2 world avg | PRL 131:161802 | 116592055(24)×10⁻¹¹ |
| Fermilab Run-3 tension (e+e- baseline) | a_μ_exp - a_μ_SM_eeplus | +245(56)×10⁻¹¹ |
| AVE-vs-e+e- tension | AVE_forward - Fermilab_eeplus_tension | +257(56)×10⁻¹¹ → **+4.59σ over** |
| BMW SM-baseline (Borsanyi+ 2021) | Nature 593:51-55 | 116591954(55)×10⁻¹¹ |
| Fermilab-vs-BMW central tension | a_μ_exp - a_μ_SM_BMW | +101(60)×10⁻¹¹ → +1.7σ |
| AVE-vs-BMW tension | AVE_forward - Fermilab_BMW_tension | +401(60)×10⁻¹¹ → **+6.68σ DEEPER** |

### Step 3c — Discriminating Outcomes

- **Outcome PASS (~85%)**: surgical re-frame lands cleanly; driver emits +501.78×10⁻¹¹ preserved; both-baseline tensions computed numerically and reported as parallel σ values (4.6σ on e+e-, 6.7σ DEEPER on BMW); Outcome-B classifier removed; PASS-conditional / FLAG / RETIRE adjudication structure inserted; docstring + skill_disciplines_applied updated; ave-auditor returns PROMOTE on the artifact set.

- **Outcome FLAG (~10%)**: re-frame surfaces a new arithmetic gap or computation drift (e.g., post-edit +501.78 changes; BMW arithmetic gives σ-tension materially different from ~6.7σ DEEPER per Q-G27 leaf line 67 + handoff line 7 lock) → surface to Grant; do not commit until adjudicated; trigger ave-walk-back skill if new walk-back required.

- **Outcome RETIRE (~5%)**: re-frame uncovers a structural reason the deliverable can't land (e.g., BMW central value at canonical source differs from 116591954e-11; Fermilab Run-3 published value at e+e- baseline isn't +245(56)×10⁻¹¹ at session-start verification; corpus's locked claim conflicts with computed BMW tension) → defer, document, surface to Grant.

### Step 3d — Falsifiers

1. **Formula computation drift**: if the post-edit driver produces `Δa_μ^(2) ≠ +501.78×10⁻¹¹` to round-off (e.g., the canonical formula at lines 73-89 got broken by the edits), surface as FLAG and do not push. Driver was already correct at line 89.

2. **BMW arithmetic divergence**: if the BMW computation gives a tension materially different from ~6.7σ DEEPER per Q-G27 leaf line 67 + handoff line 7 lock (e.g., ~3σ or ~10σ), surface as FLAG.

3. **Two-baseline framing inconsistency**: if any post-edit framing claims "BMW gives softer tension" or "BMW may shift the sign" (the stale BMW-softer framing that the handoff post-lock sweep removed), the re-frame is propagating a stale physics direction — surface as FLAG.

4. **ave-discrimination-check failure**: if the result doc framing falls into "AVE matches muon g-2" overclaim (vs the honest "AVE forward +502 in tension with Fermilab on both baselines" structure), the ave-evidence-framing-discipline check has failed — surface as FLAG.

5. **Lepton-mass ladder break check** (sanity): the √(3/7) factor MUST remain canonical in the driver's `delta_cosserat` computation — any change would break the cross-derivation consistency at `m_μ = m_e/(α·√(3/7))`. Verify [`cosserat.py:65`](../src/ave/topological/cosserat.py:65) `_SIN_THETA_W_PAT = sqrt(3.0/7.0)` is unchanged.

### Step 3e — Driver re-frame scope

Existing file: `src/scripts/verify/muon_g2_fermilab_anchor.py` (321 lines pre-edit)

**Preserve**:
- Imports at lines 33-34 (already canonical: `from ave.core.constants import ALPHA, M_E` + `from ave.topological.cosserat import M_MU, M_MU_MEV`)
- FERMILAB_RUN1_RUN2_* + FERMILAB_RUN3_* literal block at lines 51-57 (paper-pinned)
- `compute_q_g27_prediction()` formula computation at lines 73-79 (canonical)
- `compare_to_fermilab()` helper at lines 109-132 (generic, reusable)
- Result JSON output structure at lines 274-309

**Modify**:
- Docstring at lines 1-23: "verifies corpus claim" → "forward-predicts +502×10⁻¹¹, reports parallel-baseline tensions"
- `compute_q_g27_prediction()` return dict at lines 94-106: drop `delta_a_mu_2_corpus_claim`, `arithmetic_discrepancy_factor`; rename `delta_a_mu_2_standard_formula` → `delta_a_mu_2_forward_prediction`
- Remove lines 82-83 (`c_2_electron_pdg`, `c_2_muon_corpus` literals — corpus-quoted reference values, not canonical)
- Remove line 92 (`delta_a_mu_2_corpus = 247e-11` hardcoded pre-walk-back literal)
- Remove lines 213-219 ("Comparison 2: AVE prediction per corpus claim (+247×10⁻¹¹)" block)
- Replace lines 247-268 (Outcome A/B/C/D classifier) with post-walk-back PASS-conditional / FLAG / RETIRE adjudication
- Update `skill_disciplines_applied` list at lines 298-308 to add `ave-walk-back`

**Add**:
- BMW_SM_BORSANYI_2021 + BMW_SM_BORSANYI_2021_UNCERTAINTY + BMW_SM_PAPER literals after line 57 (paper-pinned style matching FERMILAB_*)
- `compare_to_fermilab_bmw_baseline()` helper (parallel to `compare_to_fermilab()`)
- Numerical BMW tension printout block alongside e+e- tension block
- Two-baseline parallel σ-tension reporting in the OUTCOME ASSESSMENT section

Result doc: `research/2026-05-19_c3-muon-delta-fermilab-driver-rerun-result.md` — log regardless of outcome.

## Section 4 — Falsifier discipline

Pre-reg committed BEFORE running re-framed driver. Result logged regardless of outcome. No outcome rewrite. If Falsifier 1-3 triggers, FLAG to Grant; do not push branch.

## Section 5 — Out of scope

- Build C5-CMB-AXIS driver (E1b cascade) — separate session
- Activate Route 3 framework-commitment (E1c cascade) — separate session
- Close C13c-DM-MECHANISM-UNIFY META row (E2b) — separate session
- Touch any other matrix row beyond C3 — strictly scoped
- Modify Q-G27 or Q-G19α leaves — they're already canonical post-walk-back
- Merge into integration or push to L3 — branch stays at session deliverable
- Build full Route B engine `verify/electron_g2_petermann.py` for Q-G19α Stage 2 — DEFERRED multi-session per walk-back doc
- Resolve BMW vs e+e- SM-baseline dispute — multi-year theoretical debate
- Fermilab Run-4/5 data — ~2026-2027 future
- Tau g-2 — Q-G27 predicts +1000×10⁻¹¹ (doubly-scaled corrected) but not currently measured at this precision
- Cleanup of [`/Users/grantlindblom/AVE-staging/AVE-Core/CLAUDE.md`](../CLAUDE.md) atopile DSL content — flag separately at session end
