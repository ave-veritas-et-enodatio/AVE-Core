# Epic STUB: Ax 4 Saturation Amplitude-Shape Signature at Narrow Boundary Apertures

**Status**: STUB — substrate-native reframe of the prior `nanoscale-clt-failure-forward-prediction.md` framing (2026-05-26 rename). Pre-prereg framing only; awaiting Grant adjudication on Q-AX4-NA-1 + Q-AX4-NA-2 before scoping.
**Origin**: surfaced as a candidate forward-prediction during Phase 2-A.4 (uniqueness of quadratic-in-amplitude boundary-Joule extraction rate scaling) on 2026-05-26. The central-aggregation step across N independent boundary lattice sites was load-bearing for the assumption that aperture-aggregate substrate amplitude statistics follow the quadratic-Lagrangian shape; at narrow apertures (small N) with Ax 4 saturation active at each site, the per-site substrate-pinned amplitude-shape survives the aggregation and propagates to a substrate-distinct correction to the aperture-aggregate boundary-Joule extraction rate.
**Lineage**: parked from PR #38 merge follow-up planning queue (one of 3 forward-prediction candidate downstream-epic seeds)
**Reframe history (2026-05-26)**: prior version was framed as "nanoscale CLT failure" using standard-physics vocabulary (Born rule, Gaussian noise, FDT, CLT, photodetector) as primary load-bearing prose. Grant intervention triggered `ave-discipline-translate` v1.1 trigger 6 (prose-vocabulary-substitution check). Rewritten in substrate-native vocabulary; the AVE-distinct piece is the Ax 4 saturation-induced per-site amplitude-shape, NOT the small-N aggregation step (which is substrate-agnostic statistics).

## What the substrate does

At the boundary of the K4-TLM substrate, a region of matched-impedance lattice cells extracts energy from substrate amplitude excursions via Joule kinematics: dE/dt = V²/Z_det at each boundary site. The boundary aperture spans N independent substrate lattice sites — independent in the sense that their amplitude excursions are not correlated by the substrate's spatial correlation length.

At each boundary site, the substrate amplitude V_n is governed by the local substrate state. **In the substrate's linear regime** (□V = 0; amplitudes below the saturation onset A_c), the substrate Lagrangian is quadratic in amplitude. By quadratic-Lagrangian moment factorization (the substrate-mechanical fact that all amplitude-moment products reduce to two-point correlator products when the Lagrangian is quadratic — the standard-physics community calls this Wick's theorem), the per-site amplitude statistics have the quadratic-Lagrangian shape — no irreducible higher-order content. **In the substrate's saturation regime** (amplitudes V_n approach A_c; Ax 4 kernel active), the substrate Lagrangian gains its nonlinear constitutive limit S(A) = √(1 − (A/A_c)²). The per-site amplitude statistics then develop substrate-pinned irreducible higher-order content with shape determined by the Ax 4 kernel.

Across the boundary aperture, the aperture-aggregate amplitude is the sum of N independent per-site contributions. For wide apertures (large N), the substrate-agnostic central-aggregation theorem (the statement that summing many independent equal-variance contributions produces a quadratic-Lagrangian-shape aggregate as N → ∞; the standard community calls this the Central Limit Theorem) erases per-site shape; the aggregate is quadratic-Lagrangian-shape regardless of the per-site substrate state. For narrow apertures (small N), the per-site substrate-pinned shape survives the aggregation and propagates to the aperture-aggregate.

## The substrate-distinct prediction

In the substrate-saturation regime at a narrow boundary aperture, the aperture-aggregate boundary-Joule extraction rate carries a substrate-pinned correction to pure quadratic-in-signal-amplitude scaling. The correction is the product of two factors:

- **Ax 4 saturation depth at each boundary site** — substrate-distinct: scales as (V_n / A_c)² to leading order. Set by how close the substrate amplitude at each boundary site is operating to the Ax 4 constitutive limit.
- **Aperture-incompleteness factor** — substrate-agnostic: scales as 1/√N for the leading irreducible third-order shape correction, 1/N for the fourth-order. Set by how few independent substrate lattice sites the aperture spans.

The product (V/A_c)² × 1/√N (leading) carries the substrate-pinned content via the first factor; the second factor is a visibility filter (any framework with N independent boundary contributions would predict the same 1/√N suppression).

## What standard physics says

Standard physics treats the quadratic-in-amplitude boundary extraction as a postulated measurement rule (standard-physics community names: "Born rule p=2 scaling", "|ψ|² measurement postulate") that holds at all boundary geometries with no internal mechanism for aperture-geometry-dependent or amplitude-magnitude-dependent corrections. **Standard physics is silent in this regime** — it makes no prediction about amplitude-shape signatures at narrow apertures in the saturation regime because its measurement postulate is geometry-independent and the postulated extraction-rate / amplitude-squared identification is exact at all amplitudes by stipulation.

The silence is what makes the AVE prediction discriminating: AVE predicts a specific substrate-pinned shape correction in a specific (saturation × narrow-aperture) regime; standard physics has no prediction at all in this regime.

## Adjudication queue (Grant — needed before scoping)

### Q-AX4-NA-1 — is the Ax 4 saturation chain to per-site amplitude-shape derivable from canonical AVE primitives?

The substrate-distinct piece is the per-site amplitude-shape from Ax 4 saturation. The corpus has the saturation kernel S(A) = √(1 − (A/A_c)²) canonical (Axiom 4); the corpus has substrate-thermal-amplitude / boundary-impedance equilibrium relations canonical (Vol 3 Ch 11 — the standard-physics community calls this the fluctuation-dissipation theorem). What's NOT obviously canonical: the per-site amplitude-shape derivation from the nonlinear S(A)-modified single-site substrate dynamics at a boundary lattice site.

**Question**: is the per-site amplitude-shape derivable end-to-end from (Axiom 4 saturation kernel + Vol 3 Ch 11 substrate-thermal-amplitude / boundary-impedance scaffold + single-site substrate dynamics) without smuggled inputs? If yes, Phase 1 work derives the third-order and fourth-order shape factors explicitly. If no, the chain has a gap that needs upstream theoretical work before this epic can be scoped.

**Way to discriminate**: Phase 1 attempts to derive κ₃(V_n, A_c) and κ₄(V_n, A_c) from the single-site nonlinear substrate dynamics — the irreducible third-order and fourth-order amplitude correlators as functions of substrate state. If the derivation closes from canonical primitives, the chain is complete. If it requires new theoretical machinery (e.g., a single-site path-integral treatment of the saturation kernel that isn't in the corpus), the chain has a derivation gap.

**Adjudication needed**: your read on whether the corpus's current Ax 4 + Vol 3 Ch 11 + single-site substrate dynamics scaffold is sufficient, or whether single-site nonlinear-substrate-dynamics treatment needs to be commissioned as a sub-epic first.

### Q-AX4-NA-2 — what boundary-extraction architecture realizes the substrate-saturation × narrow-aperture regime, and is it experimentally accessible?

Even if Q-AX4-NA-1 closes cleanly, the prediction requires both substrate conditions simultaneously:

1. **Substrate operating near saturation at boundary sites**: V_n / A_c not small. Standard photon-flux extraction setups operate at V_n / A_c ~ 10⁻⁶ (far from saturation) by design. Substrate-saturation operating conditions occur at high-amplitude single-event extraction — substrate-architecturally this is the narrow-aperture-threshold-triggered single-event extraction class (standard-physics community names: avalanche photodiodes, single-photon avalanche detectors, transition-edge sensors, superconducting nanowire single-photon detectors).
2. **Aperture narrow enough that central-aggregation is incomplete**: N small. Substrate-architecturally this means the boundary aperture spans few lattice sites; the lattice spacing in AVE-canonical units is ℓ_node ≈ ℏ/m_e c ≈ 386 fm. N ~ 4-10 maps to aperture width ~ 1.5-4 pm. The substrate-correlation-length question (what makes two lattice sites "independent" — lattice spacing alone, or a longer correlation length set by Ax 4 saturation regime) is a sub-question that affects this mapping.

**Question**: are there boundary-extraction architectures in lab use that hit both regimes simultaneously? Substrate-architecturally: narrow-aperture single-event histogram-statistics extractors operating in the threshold-triggered saturation regime. The standard-physics-community lists single-photon avalanche detectors + transition-edge sensors + superconducting nanowire single-photon detectors as the candidates; whether any of these substrate-architecturally span few-enough independent lattice sites in the saturation regime is a literature + corpus survey question.

**Adjudication needed**: your read on whether the (substrate-saturation × narrow-aperture) operating regime is achievable in any existing boundary-extraction architecture, or whether the prediction is structurally inaccessible to current experimental geometry. If structurally inaccessible, this is still a Class 2 substrate-emergence prediction (Q-AX4-NA-1 result determines that), but its empirical falsifiability gates on future detector technology.

### Q-AX4-NA-3 (sub-question to Q-AX4-NA-2) — substrate correlation length

The mapping "N independent lattice sites" assumes site-independence is set by lattice spacing. The substrate's spatial correlation length (set by Ax 4 saturation regime + boundary-impedance matching length) may be longer than ℓ_node, especially in the saturation regime where the K4-TLM nonlinearity couples adjacent sites more strongly than the linear-regime baseline. If the saturation-regime correlation length is N_corr × ℓ_node for some N_corr > 1, then the "N independent lattice sites" count maps to an aperture width of N × N_corr × ℓ_node rather than N × ℓ_node — softening the narrow-aperture geometric constraint.

This could either come up as a sub-question to Q-AX4-NA-2 or as a separate Phase 0b derivation gate before Q-AX4-NA-2 can be sharpened.

## Pre-survey corpus-grep targets (mandatory before any derivation begins)

```bash
# Ax 4 saturation kernel + amplitude-shape derivations
grep -rn "saturation kernel\|S(A)\|A_c\|saturation onset\|amplitude.*shape\|sqrt.*1.*A.*A_c" \
  manuscript/ave-kb/ research/ src/ave/
grep -rn "Axiom 4\|Ax 4\|axiom.*4" manuscript/ave-kb/

# Substrate per-site amplitude statistics + single-site dynamics
grep -rn "Langevin\|stochastic master\|per-site amplitude\|boundary.*node.*amplitude" \
  manuscript/ave-kb/ research/
grep -rn "Vol 3 Ch 11\|vol3.*ch11\|substrate.*thermal.*amplitude\|fluctuation.dissipation" \
  manuscript/ave-kb/ research/

# Boundary aperture + lattice-site count
grep -rn "boundary aperture\|aperture.*width\|narrow.*aperture\|N.*independent" \
  manuscript/ave-kb/ research/

# Substrate correlation length
grep -rn "correlation length\|substrate.*correlation\|coupling length\|K4.*correlation" \
  manuscript/ave-kb/

# Prior work on amplitude-shape signatures
grep -rn "amplitude-shape\|amplitude statistics\|higher.*correlator\|irreducible.*third\|irreducible.*fourth" \
  manuscript/ave-kb/ research/
```

Required pulls before pre-reg:

- The Phase 2-A.4 result doc ([`research/2026-05-26_clm-ldmvwi-phase-2a-4-uniqueness-result.md`](../research/2026-05-26_clm-ldmvwi-phase-2a-4-uniqueness-result.md)) — verify the central-aggregation step IS load-bearing in the uniqueness chain and that the saturation-modified per-site amplitude statistics are flagged as out-of-scope for that result (line 144 + line 146 confirm this)
- The Phase 2-A.2 result doc ([`research/2026-05-26_clm-ldmvwi-phase-2a-2-stochastic-master-eq-result.md`](../research/2026-05-26_clm-ldmvwi-phase-2a-2-stochastic-master-eq-result.md)) — verify the per-site substrate-thermal-amplitude / boundary-impedance equilibrium relation is canonical
- Vol 3 Ch 11 substrate-thermal-amplitude / boundary-impedance scaffold leaf — canonical home of the substrate-amplitude / boundary-impedance equilibrium relation in AVE-Core
- Ax 4 saturation kernel canonical leaf (likely `axiom-definitions.md` line 34 per `ave-discipline-translate` skill reference)

## Phase plan (TENTATIVE — locked only after Q-AX4-NA-1 + Q-AX4-NA-2 adjudication)

| Phase | Goal | Status |
|---|---|---|
| 0a | Adjudicate Q-AX4-NA-1 (Ax 4 chain to per-site amplitude-shape derivable from canonical primitives) | **PENDING — needs Grant** |
| 0b | Adjudicate Q-AX4-NA-2 (boundary-extraction architecture × substrate-correlation-length realizes the regime) | **PENDING — needs Grant** |
| 0c | Pre-reg writing (only after 0a + 0b both PASS) | DEFERRED |
| 1 | Derive κ₃(V_n, A_c) and κ₄(V_n, A_c) — leading irreducible third-order and fourth-order substrate amplitude correlators from single-site nonlinear-substrate dynamics | DEFERRED |
| 2 | Compute aperture-aggregate amplitude-shape signature as function of (V/A_c, N); identify the substrate-saturation × narrow-aperture operating threshold for visible signature | DEFERRED |
| 3 | KB integration if Class 2 substrate-mechanism emergence confirmed; reframe scope honestly if derivation closure is partial | DEFERRED |
| 4 | Add to divergence-test substrate map as a new forward-prediction row (if Phase 3 lands clean) | DEFERRED |

## If both Q-AX4-NA-1 and Q-AX4-NA-2 land as GO

This becomes a **new forward-prediction row** in the divergence-test substrate map — a previously-unenumerated AVE-substrate-distinct prediction that the framework strengthening effort surfaced. Solidity at introduction would be ~0.55 (theoretical-prediction, not yet experimentally tested or constrained), pending falsification work.

The forward-prediction is structurally interesting because:

- It comes from the framework's OWN derivation chain (Phase 2-A master-equation-derivation-path), not from importing external puzzles
- It's at a regime (substrate-saturation × narrow-aperture) where standard physics is structurally silent (the postulated measurement rule has no aperture-geometry-dependent corrections)
- It is the first forward-prediction in the corpus to come out of `consistency-vs-emergence` v1.2 master-equation-derivation-path discipline — demonstrating that the discipline upgrade can SURFACE new physics, not just hygiene-clean existing claims

## If either Q-AX4-NA-1 or Q-AX4-NA-2 lands as NOGO

Park in the framework-extension candidate queue. Document honestly: "the central-aggregation step in Phase 2-A.4 was load-bearing for the assumption that aperture-aggregate amplitude statistics follow the quadratic-Lagrangian shape; an Ax-4-saturation-induced per-site amplitude-shape forward-prediction was considered but found to be [derivation-gated by single-site nonlinear-substrate-dynamics treatment / experimentally inaccessible at current boundary-extraction architectures / both]. Documented at `_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md` for future reconsideration if the upstream gap closes OR experimental access becomes feasible."

## Skills expected to fire (when work begins)

- `ave-prereg` — corpus-grep as above
- `pre-test-physics-check` — Grant plumber-physical question before locking the prediction framing
- `ave-canonical-leaf-pull` — Ax 4 saturation + Vol 3 Ch 11 substrate-thermal-amplitude / boundary-impedance scaffold + boundary-extraction + amplitude-shape leaves
- `ave-analytical-tool-selection` — Saturation / Time-domain / Boundary class; check `ave-analytical-toolkit-index.md` for Op-level tools (likely Op4 boundary-impedance + nonlinear-substrate-dynamics tooling)
- `ave-discipline-translate` v1.1 — trigger 6 fires continuously during prose composition; substrate-native vocabulary mandatory throughout. The standard-physics-community names (avalanche photodiode, SPAD, TES, SNSPD, dark count, quantum efficiency) appear only as parenthetical translation references to substrate-architecture descriptions
- `substrate-native-check` — walk K4 + Cosserat + Ax 4 substrate structure before any single-site substrate-dynamics treatment
- `consistency-vs-emergence` v1.2 — explicit Class 2 vs Class 4 classification with master-equation-derivation-path tracing. The DRIVING skill — Q-AX4-NA-1 IS application of this skill
- `phase-space-coordinate-check` — N counts substrate lattice sites in real-space; aperture-aggregate amplitude lives in voltage-amplitude space; substrate-correlation-length question is real-space; keep coordinates clean
- `ave-evidence-framing-discipline` — "forward-prediction" vs "consistency-with-substrate-agnostic-statistics" precision
- `ave-discrimination-check` — standard-physics-counterfactual (standard physics is silent in this regime) + interpretive-alternatives (are there interpretive alternatives that explain the same amplitude-shape signature without Ax 4 saturation kernel?)
- `ave-multi-falsifier-triangulation-discipline` — if the prediction lands, the falsifier set must discriminate substrate-distinct Ax-4-saturation-induced shape from substrate-agnostic central-aggregation-pre-asymptote
- `ave-walk-back` v1.1 Type E — value-amendments during the derivation

## Branch + spawn protocol (when scoped)

- **Branch**: `analysis/ax4-saturation-narrow-aperture-amplitude-shape-phase-1` off `main` @ post-PR-38-merge (only after Q-AX4-NA-1 + Q-AX4-NA-2 adjudication clears)
- **Spawn**: orchestration session uses `Agent` tool with `isolation: "worktree"` (per CLAUDE.md "Pre-commit discipline")
- **Sub-agent type**: `ave-implementer`
- **Sequencing**: parallel-safe with clm-zuf7g1 Phase 3a + clm-0ktpcn Phase 3-A1+Q2 / 3-A2 once kicked off; no depends-on conflicts

## Cross-references

- **Origin Phase 2-A.4 result doc**: [`research/2026-05-26_clm-ldmvwi-phase-2a-4-uniqueness-result.md`](../research/2026-05-26_clm-ldmvwi-phase-2a-4-uniqueness-result.md) — central-aggregation step appears in §2 (uniqueness argument); saturation-modified per-site amplitude statistics flagged at line 144 + line 146 as out-of-scope for that result
- **Origin Phase 2-A.2 result doc**: [`research/2026-05-26_clm-ldmvwi-phase-2a-2-stochastic-master-eq-result.md`](../research/2026-05-26_clm-ldmvwi-phase-2a-2-stochastic-master-eq-result.md) — substrate-thermal-amplitude / boundary-impedance equilibrium relation introduced
- **Source claim**: [`manuscript/ave-kb/vol1/claim-quality.md`](../manuscript/ave-kb/vol1/claim-quality.md) clm-ldmvwi block
- **Skill discipline anchor**: `ave-discipline-translate` v1.1 trigger 6 (substrate-native vocabulary mandatory in agent-output prose); this epic IS the in-session validation case for the v1.1 amendment
- **Sibling forward-prediction candidate seeds** (parked alongside this one):
  - (TBD — placeholder for the other 2 forward-prediction candidates from the PR #38 merge follow-up queue if and when they get their own epic stubs)

## Failure modes to watch (when work begins)

- **Class 2 / Class 4 conflation under substrate-native naming** — even with the reframe, the central question is whether the Ax-4-pinned per-site amplitude-shape (Class 2 substrate-mechanism) or the substrate-agnostic central-aggregation incompleteness (Class 4 generic statistics) is the load-bearing piece in the final result. The discriminator: does the prediction's amplitude scale with A_c (substrate-specific Axiom 4 parameter) in a way that's distinguishable from a free fit? `consistency-vs-emergence` v1.2 master-equation-derivation-path discipline is the gating skill
- **Standard-physics vocabulary leak during prose composition** — even after the reframe, agent-output paragraphs may slip back into "Born rule / Gaussian / CLT / detector" vocabulary because that's what the canonical-citation chain uses. `ave-discipline-translate` v1.1 trigger 6 fires continuously during composition
- **Order-of-magnitude inflation** — predicting "X% amplitude-shape signature at narrow aperture" without checking what (V/A_c, N) corresponds to in physical substrate-architecture units. Q-AX4-NA-2 catches this at the prereg stage; ave-evidence-framing-discipline catches it at the result-writing stage
- **Substrate-correlation-length skip** — Q-AX4-NA-3 sub-question matters for the geometric-accessibility argument; skipping it inflates accessibility estimates
- **Forward-prediction vs consistency check** — easy slip to write the result as "AVE predicts X" when the substrate-distinct piece (Ax 4 saturation depth) is small and the substrate-agnostic piece (central-aggregation pre-asymptote) is dominant. `ave-discrimination-check` standard-physics-counterfactual is the gating skill

## Honest framing of this epic

This is **the first forward-prediction candidate to come out of the framework strengthening effort itself**, AND **the first epic to be reframed by `ave-discipline-translate` v1.1 trigger 6**. Its value as a strengthening signal — independent of whether it lands as Class 2 substrate-mechanism emergence or Class 4 generic statistics — is structural: it demonstrates that the `consistency-vs-emergence` v1.2 discipline applied to a previously-closed result (Phase 2-A Born-rule-derivation chain) can SURFACE new prediction candidates rather than just hygiene-clean existing claims, AND it demonstrates that substrate-native prose-vocabulary discipline (v1.1 trigger 6) is necessary to surface the structural distinction (Ax 4 saturation vs central-aggregation aggregation) that the standard-physics-vocabulary framing had occluded.

If it lands as Class 2 substrate-mechanism emergence with empirical accessibility, it's a major framework win. If it lands as derivation-gated or experimentally-inaccessible, the honest documentation is itself valuable — it shows the discipline can distinguish "substrate-distinct forward-prediction" from "consistency with substrate-agnostic statistics" at the prereg-framing stage, not after derivation work.

Either way, **Q-AX4-NA-1 + Q-AX4-NA-2 must be adjudicated by Grant before any derivation work begins**. This is exactly the kind of question where your plumber-physical intuition is the generative engine; this epic stub exists to frame the adjudication, not to pre-empt it.
