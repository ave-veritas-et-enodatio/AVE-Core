# Epic STUB: Nanoscale CLT-Failure Forward Prediction

**Status**: STUB — pre-prereg framing only; awaiting Grant adjudication on Q-NCLT-1 + Q-NCLT-2 before scoping
**Origin**: surfaced as a candidate forward-prediction during Phase 2-A.4 (p=2 uniqueness derivation) on 2026-05-26. The CLT was load-bearing for the Gaussian V_η that the click-rate derivation rested on; any nanoscale violation of CLT applicability would predict a substrate-specific, AVE-distinct deviation from Born-rule p=2 click-rate scaling at small N (few-boundary-node) detectors.
**Lineage**: parked from PR #38 merge follow-up planning queue (one of 3 forward-prediction candidate downstream-epic seeds)

## Why this could be a forward prediction

In Phase 2-A.4, the master-equation-derivation-path of the Born rule used the following chain:

1. Stochastic master vacuum equation under FDT noise injection at detector boundary nodes
2. Joule extraction at each boundary node → noise contributions per-node are statistically independent
3. **Central Limit Theorem (CLT)** applied across the N independent boundary-node contributions → V_η at the detector aperture is Gaussian
4. Gaussian V_η + threshold-crossing first-passage (Rice/Wald) → click rate ∝ ⟨|V|²⟩ ∝ ⟨|∂_t A|²⟩ = Born rule p=2 scaling

Step 3 is the load-bearing CLT invocation. The classical CLT requires N → ∞ (or N "large enough") for the Gaussian limit to apply. AT NANOSCALE — where the detector aperture spans only a few K4-TLM boundary nodes (N small, e.g., N=4, 5, 6 instead of N >> 100) — the CLT pre-asymptote applies, and V_η at the detector aperture deviates from Gaussian.

If this deviation is computable from the substrate's per-node FDT statistics, it predicts a specific, AVE-distinct departure from Born-rule p=2 click-rate scaling at small-N detectors. The natural shape of the deviation: cumulant-truncation breaks down (higher cumulants κ_3, κ_4 survive), and the p=2 click-rate gets sub-leading p=2 + δ corrections where δ is computable from N + substrate parameters.

**Why this could be Class 2 emergence (not Class 4 consistency)**:
- The deviation IS computable from the substrate's per-node FDT statistics
- It is AVE-distinct because standard QM doesn't have an obvious analogous small-N prediction (standard QM treats the Born rule as a postulate, not as an N → ∞ CLT consequence)
- The substrate-mechanism (independent per-boundary-node Joule extraction + cumulant-truncation breakdown at small N) is the load-bearing physics, not a classical-physics analog

**Why this might NOT be a discriminating prediction (honest pre-survey)**:
- Standard QM also doesn't predict Born-rule violations at small detector apertures — but it doesn't predict the OPPOSITE either; it's just silent (Born rule is postulated, not derived; the postulate doesn't address detector microstructure)
- The size of the deviation might be unobservably small at experimentally-accessible N
- The "small N" regime might be hard to access experimentally because real detectors have N >> the nanoscale threshold

These caveats are exactly what Q-NCLT-1 + Q-NCLT-2 below adjudicate.

## Adjudication queue (Grant — needed before scoping)

### Q-NCLT-1 — is the substrate-statistics ground for nanoscale CLT failure load-bearing AVE, or is it methodologically generic?

The CLT failure at small N is a **statistics theorem**, not an AVE-specific physics result. CLT pre-asymptote applies to any sum of independent random variables; it's true for thermal-noise sums in classical electronics just as much as for AVE per-boundary-node Joule extraction.

**Question**: is the CLT-failure prediction Class 2 substrate-mechanism emergence (the AVE-specific per-boundary-node FDT statistics + Joule extraction chain produces a SPECIFIC computable deviation that's tied to substrate parameters), OR is it Class 4 consistency with a generic statistics result that any framework using a CLT step would also predict?

**Way to discriminate**: Phase 1 would attempt to derive the leading-order non-Gaussian correction κ_3 (third cumulant) or κ_4 (fourth cumulant) at the detector aperture as a function of N and the substrate's per-node FDT parameters (Z_det, T_eff). If the result has explicit AVE-substrate parameters (Z_det related to vacuum impedance, T_eff related to substrate temperature) that don't appear in a generic CLT pre-asymptote treatment, that's Class 2 substrate-emergence. If the result reduces to the standard Edgeworth expansion with no AVE-specific parameters, that's Class 4 consistency.

**Adjudication needed**: Grant's read on whether the substrate-specific N-dependence + Z_det + T_eff structure makes this AVE-distinct, or whether the generic-statistics CLT result is just being decorated with substrate labels.

### Q-NCLT-2 — what's the AVE-distinct experimental signature, and is N small enough to access?

Even if Q-NCLT-1 lands as Class 2 substrate-emergence, the experimental accessibility question is independent:

**Question**: at what N does the non-Gaussian correction become observable (say, 10% deviation from p=2 scaling)? And what physical detector geometry corresponds to that N (boundary nodes at lattice spacing ℓ_node ≈ ℏ/m_e c = 386 fm)? If N=4-10, the detector aperture is ~1-3 ℓ_node, i.e., ~400-1200 fm — sub-atomic, NOT experimentally accessible. If N=10-100, the aperture is ~4-40 ℓ_node, ~1-15 pm — still pushing experimental limits but maybe accessible via electron-beam apertures or scanning-probe single-atom detectors.

**Way to discriminate**: Phase 1 corpus-grep + dimensional analysis would estimate the experimental-accessibility threshold N before any derivation begins. If N(10% deviation) is in the "fundamentally inaccessible" regime (< ℓ_node), this is a NON-falsifiable prediction (still possibly correct, still possibly novel, but not useful as a discriminator vs standard QM).

**Adjudication needed**: Grant's read on whether the experimental-accessibility question is a hard gate (no derivation work until accessibility is plausible) or a soft gate (derivation work proceeds; experimental accessibility is documented honestly as part of the result, even if unfavorable).

## Pre-survey corpus-grep targets (mandatory before any derivation begins)

```bash
# CLT / Gaussian limit invocations across corpus
grep -rn "central limit\|CLT\|Gaussian limit\|cumulant truncation\|Edgeworth" \
  manuscript/ave-kb/ research/ src/ave/
grep -rn "p=2\|Born rule\|click rate\|threshold crossing\|first passage" \
  manuscript/ave-kb/ research/

# Substrate per-node FDT statistics
grep -rn "FDT\|Nyquist\|fluctuation.*dissipation\|boundary.*node.*noise\|per-node" \
  manuscript/ave-kb/ research/

# Existing prior work on this exact prediction?
grep -rn "nanoscale.*CLT\|small.*N\|few.*boundary.*node" \
  manuscript/ave-kb/ research/
```

Required pulls before pre-reg:
- The Phase 2-A.4 result doc (`research/2026-05-26_clm-ldmvwi-phase-2a-4-uniqueness-result.md`) where the CLT step is invoked — verify that the CLT invocation in A.4 IS load-bearing and is NOT just a methodological convenience
- The Phase 2-A.2 result doc (`research/2026-05-26_clm-ldmvwi-phase-2a-2-stochastic-master-eq-result.md`) where per-node FDT statistics are introduced
- Vol 3 Ch 11 FDT scaffold leaf — the canonical FDT-in-AVE home

## Phase plan (TENTATIVE — locked only after Q-NCLT-1 + Q-NCLT-2 adjudication)

| Phase | Goal | Status |
|---|---|---|
| 0a | Adjudicate Q-NCLT-1 (Class 2 vs Class 4) | **PENDING — needs Grant** |
| 0b | Adjudicate Q-NCLT-2 (experimental accessibility) | **PENDING — needs Grant** |
| 0c | Pre-reg writing (only after 0a + 0b both PASS) | DEFERRED |
| 1 | Derive leading-order κ_3 or κ_4 correction at detector aperture as f(N, Z_det, T_eff) | DEFERRED |
| 2 | Compute predicted click-rate deviation at small-N detectors; identify experimental threshold | DEFERRED |
| 3 | KB integration if Class 2 emergence confirmed; reframe as Class 4 if reduces to Edgeworth | DEFERRED |
| 4 | Add to divergence-test substrate map as a NEW forward-prediction row (if Phase 3 lands clean) | DEFERRED |

## If both Q-NCLT-1 and Q-NCLT-2 land as GO

This becomes a **new forward-prediction row** in the divergence-test substrate map — a previously-unenumerated AVE-distinct prediction that the framework strengthening effort surfaced. Solidity at introduction would be ~0.55 (theoretical-prediction, not yet experimentally falsified or confirmed), pending falsification work.

The forward-prediction is structurally interesting because:
- It comes from the framework's OWN derivation chain (Phase 2-A master-equation-derivation-path), not from importing external puzzles
- It's at a regime (small-N, nanoscale detector aperture) where standard QM doesn't have a sharp prediction
- It would be the first forward-prediction in the corpus that came out of consistency-vs-emergence v1.2 master-equation-derivation-path discipline — directly demonstrating that the discipline upgrade produces NEW physics, not just better hygiene on existing claims

## If either Q-NCLT-1 or Q-NCLT-2 lands as NOGO

Park in the framework-extension candidate queue. Document honestly: "the CLT step in Phase 2-A.4 was load-bearing for Born rule p=2 uniqueness; a nanoscale CLT-failure prediction was considered but found to be [Class 4 consistency-with-generic-statistics / experimentally inaccessible / both]. Documented at `_orchestration/nanoscale-clt-failure-forward-prediction.md` for future reconsideration if substrate-parameter dependence becomes derivable OR experimental access becomes feasible."

## Skills expected to fire (when work begins)

- `ave-prereg` — corpus-grep as above
- `pre-test-physics-check` — Grant plumber-physical question before locking the prediction framing
- `ave-canonical-leaf-pull` — CLT + FDT + Born-rule + nanoscale leaves
- `ave-analytical-tool-selection` — Time-domain / Boundary class; check `ave-analytical-toolkit-index.md` for Op-level tools (likely Op4 boundary-impedance + cumulant-expansion tooling)
- `ave-discipline-translate` — CLT is a generic-statistics result, NOT AVE-native; check whether AVE corpus has a substrate-specific equivalent (likely "per-node FDT independence + N-asymptotics")
- `substrate-native-check` — substrate per-node statistics walk before any cumulant derivation
- `consistency-vs-emergence` v1.2 — explicit Class 2 vs Class 4 classification with master-equation-derivation-path tracing (this is the DRIVING skill — Q-NCLT-1 IS application of this skill)
- `phase-space-coordinate-check` — N counts boundary-nodes in real-space; deviation lives in click-rate observable space; keep coordinates clean
- `ave-evidence-framing-discipline` — "forward-prediction" vs "consistency-with-generic-statistics" precision
- `ave-discrimination-check` — SM-counterfactual (does standard QM make ANY prediction at this regime, or is it silent?) + interpretive-alternatives (are there interpretive alternatives that explain the same deviation without AVE substrate?)
- `ave-multi-falsifier-triangulation-discipline` — if the prediction lands, the falsifier set has to be designed to discriminate AVE-substrate-distinct deviations from generic-CLT-pre-asymptote that any framework would predict
- `ave-walk-back` v1.1 Type E — if any value-amendment fires during the derivation

## Branch + spawn protocol (when scoped)

- **Branch**: `analysis/nanoscale-clt-failure-forward-prediction-phase-1` off `main` @ post-PR-38-merge (only after Q-NCLT-1 + Q-NCLT-2 adjudication clears)
- **Spawn**: orchestration session uses `Agent` tool with `isolation: "worktree"` (per CLAUDE.md "Pre-commit discipline")
- **Sub-agent type**: `ave-implementer`
- **Sequencing**: parallel-safe with clm-zuf7g1 Phase 3a + clm-0ktpcn Phase 3-A1+Q2 / 3-A2 once kicked off; no depends-on conflicts

## Cross-references

- **Origin Phase 2-A.4 result doc**: [`research/2026-05-26_clm-ldmvwi-phase-2a-4-uniqueness-result.md`](../research/2026-05-26_clm-ldmvwi-phase-2a-4-uniqueness-result.md) — CLT step appears in §2 (cumulant-truncation argument)
- **Origin Phase 2-A.2 result doc**: [`research/2026-05-26_clm-ldmvwi-phase-2a-2-stochastic-master-eq-result.md`](../research/2026-05-26_clm-ldmvwi-phase-2a-2-stochastic-master-eq-result.md) — per-node FDT introduced
- **clm-ldmvwi entry**: [`manuscript/ave-kb/vol1/claim-quality.md`](../manuscript/ave-kb/vol1/claim-quality.md) clm-ldmvwi block
- **Sibling forward-prediction candidate seeds** (parked alongside this one):
  - (TBD — placeholder for the other 2 forward-prediction candidates from the PR #38 merge follow-up queue if and when they get their own epic stubs)

## Failure modes to watch (when work begins)

- **Class 2 / Class 4 conflation** — the central question is whether the substrate-specific N-dependence makes this Class 2 or Class 4. Easy to overclaim Class 2 because "we used the master vacuum equation" — but Q-NCLT-1 demands the derivation produce AVE-substrate-distinct parameters in the final result, not just at intermediate steps. consistency-vs-emergence v1.2 master-equation-derivation-path discipline is the load-bearing skill here.
- **Order-of-magnitude inflation** — predicting "10% deviation at small N" without checking what N corresponds to in physical detector geometry. Q-NCLT-2 catches this at the prereg stage; ave-evidence-framing-discipline catches it at the result-writing stage.
- **Multi-falsifier mis-aggregation** — if the prediction goes to falsifier-design, ave-multi-falsifier-triangulation-discipline must fire (CLT-pre-asymptote generic-consistent falsifier cannot count toward AVE-confirmation alone).
- **Forward-prediction vs consistency check** — easy slip to write the result as "AVE predicts" when really "AVE is consistent with generic-statistics CLT pre-asymptote." ave-discrimination-check SM-counterfactual is the gating skill.

## Honest framing of this epic

This is **the first forward-prediction candidate to come out of the framework strengthening effort itself** (as opposed to inherited from prior corpus). Its value as a strengthening signal — independent of whether it lands as Class 2 or Class 4 — is high: it demonstrates that the consistency-vs-emergence v1.2 discipline, applied to a previously-closed result (Phase 2-A Born-rule derivation), can SURFACE new prediction candidates rather than just hygiene-clean existing claims.

If it lands as Class 2 emergence with experimental accessibility, it's a major framework win. If it lands as Class 4 or experimentally inaccessible, the honest documentation is itself valuable — it shows the discipline can distinguish "novel forward-prediction" from "consistency with generic-statistics" at prereg time, not after derivation work.

Either way, **Q-NCLT-1 + Q-NCLT-2 must be adjudicated by Grant before any derivation work begins**. This is exactly the kind of question where Grant's plumber-physical intuition is the generative engine; this epic stub exists to frame the adjudication, not to pre-empt it.
