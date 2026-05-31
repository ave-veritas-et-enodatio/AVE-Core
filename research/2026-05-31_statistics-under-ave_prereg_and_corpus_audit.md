# Prereg + Corpus Audit — "Statistics under AVE" definitional anchor

**Date**: 2026-05-31
**Branch**: `analysis/statistics-under-ave-definition` (off `main` @ 7529f7ce, isolated worktree)
**Status**: definitional leaf landed; forward falsification-tests scoped (NOT executed — FT-1 gated on Phase 4 corpus walk-back merge).
**Deliverable**: [`manuscript/ave-kb/common/statistics-under-ave.md`](../manuscript/ave-kb/common/statistics-under-ave.md) (no-claim definitional/glossary leaf).

**Skills fired**: `ave-prereg` (this doc + the 2-agent cross-repo inventory below); `ave-handoff-canonical-locale` (research/ + common/ KB locale); `ave-canonical-leaf-pull` (canonical leaves enumerated before assembling); `ave-directory-enumeration-discipline` (enumerated `common/` before placing leaf); `verify-before-cite` v1.4 (every quote re-grepped against `main` state — caught one mis-attributed temperature citation, corrected to `macroscopic-temperature-lc-noise.md:12`); `consistency-vs-emergence` v1.3 (classified the deliverable — no-claim definitional, not a new emergence result); `substrate-native-check` (K4 6-DOF E/B split walked); `ave-discipline-translate` v1.1 trigger 6 (the FM-5 landmine is the spine of §5); `ave-evidence-framing-discipline` (Class 1 / "taxonomic not derivational" caveat carried verbatim); `ave-worktree-paths` (isolated worktree to avoid Phase-4 working-tree collision); `ave-audit`.

---

## §1 — Target

Establish the canonical AVE-native meaning of "statistics" (and the adjacent vocabulary: randomness, probability, entropy, temperature) and test the hypothesis that "statistics" is **not** fundamental randomness but an **emergent regime indicator** — a dimensionless ratio of competing substrate quantities (à la Reynolds = inertial/viscous) whose threshold marks the coherent/deterministic → incoherent/statistical transition. Grounded against the "Cosserat-rotation-sector mass-gap thermal-mode-population" mechanism the corpus assigned to δ_strain.

## §2 — Physical picture (mechanical, pre-grep)

- Each K4 node carries 6 DOF: 3 translational (E-modes) + 3 microrotational (B-modes, Cosserat) — INVARIANT-S2 Axiom 1.
- "Temperature" = incoherent excitation of substrate modes; the soliton = coherent phasor circulation.
- Statistics emerges when incoherent mode population makes coherent phasor-branch tracking intractable — you must average. The Γ=−1 saturation boundary is the coherent (locked) limit.
- A dimensionless "distance from coherent" ratio (loss-per-cycle × DOF) should mark the crossover — the Reynolds analogue.

## §3 — Corpus inventory (outcome: NOT green-field — every component already canonical)

Two `ave-corpus-grep` agents across all repos + archive. **Headline: the hypothesis is already corpus-canonical; the risk was reinvention, not novelty.** Verified verbatim against `main`:

| Component | Canonical home | Verdict |
|---|---|---|
| Determinism at bottom; randomness emergent | `quantum-foam-virtual.md:19`; `thermal-lattice-noise.md:151` | SUPPORTS — no hidden-variable/irreducible-stochasticity framing exists anywhere (informative absence) |
| Reynolds analogue **already exists** | `temporal-saturation-regime-classifier.md:26` (δ_AVE=t_sat/t_period, clm-f0jwtk), `:302` (δ_AVE×N) | SUPPORTS — near-verbatim the hypothesis; **do not reinvent** |
| Two orthogonal regime axes | `four-regimes.md:10,14` (r=A/A_c spatial ⊥ δ_AVE temporal) | REFINES — S/A₀/n_scalar candidate is the *spatial* axis, not the coherence axis |
| Entropy geometric, not microstate | `four-entropy-distinction.md:27,10`; `entropy-redefinition.md:14` | SUPPORTS — Ŝ=−k_B Σln(1−|Γ|²); Boltzmann counting rejected |
| Born rule derived deterministic | `ohmic-decoherence-born.md:34,53,56` (clm-ldmvwi) | SUPPORTS — "No Born rule input anywhere in the chain" |
| Statistics aggregation is substrate-AGNOSTIC | `translation-stochastics.md:29` (FM-5, Q-NCLT-1 adjudication) | CONSTRAINT — substrate-distinct content is per-site amplitude shape, NOT aggregation |
| Temperature = RMS EM noise | `macroscopic-temperature-lc-noise.md:12` (clm-t05mvx) | SUPPORTS |
| δ_strain E/B thermal asymmetry | `delta-strain-cosmic-tcc.md:13,33` (clm-hp7nlm) | REFINES — microrotational B-modes are FROZEN; translational E-modes carry T (sector inverted from naive intuition) |
| δ_AVE honesty | `temporal-saturation-regime-classifier.md:306,310` | Class 1 definitional; unification "TAXONOMIC, not derivational"; commit `98994c1` overstatement corrected in canon |

## §4 — Prereg

```
PREREG (target: canonical meaning of "statistics" under AVE):
  Corpus state: NOT green-field. Every physics component is already canonical (table §3).
                Missing piece = a definitional ANCHOR tying them together + the FM-5 boundary.
  My prediction: statistics = emergent coarse-graining gated by δ_AVE×N (the canonical Reynolds
                 analogue); substrate-distinct content = regime threshold + per-site amplitude shape,
                 NOT the aggregation. Randomness/probability/entropy all emergent-from-deterministic.
  Discriminating outcomes:
    A (realized): pieces exist + cohere → write a no-claim definitional leaf that routes, not a
                  clm-originating leaf (would over-claim / duplicate, S7).
    B: pieces conflict → flag contradiction, do not synthesize.
    C: a genuine new proposition is required → originate a clm- (NOT the case here).
  Falsifier of the framing: if the corpus located substrate-distinctness in the aggregation step
                 (not the shape/threshold), the FM-5 discipline would be wrong. It does not (trans-stoch:29).
```

## §5 — Structural decision

**No-claim definitional/glossary leaf in `common/`**, modeled on `cosmic-axes-and-frames-glossary.md` (the existing no-claim cross-cutting definitional precedent). Rationale:
- Every physics component lives in a canonical `clm-` already; assembling them is definitional, not originating (INVARIANT-S7 — don't manufacture a synthesis-claim that suggests implications beyond the leaves).
- A no-claim leaf needs **no `common/claim-quality.md` edit** — which sidesteps the one file the in-flight Phase 4 walk-back is also modifying.
- The leaf routes (F1/F2) + quotes verbatim; it re-derives nothing.

## §6 — Falsification tests (forward plan — scoped, not executed)

Ranked by how much each converts the framework from self-consistent to falsifiable-predictive.

- **FT-1 (highest value; gated on Phase 4 merge)** — Q-DELTA-MAP-1-quant. Derive η_ε from E-mode dispersion + Bose-Einstein occupation at T_CMB, **no back-substitution**, pre-registering the number. PASS: η_ε ≈ 4.45×10⁻⁶ (δ_strain ≈ 2.225×10⁻⁶) falls out → α gains a real second-order prediction; the residual stops being a fit. FAIL: wrong magnitude → Cosserat-thermal mechanism for δ_strain falsified, or δ_strain is a fit. **Guards:** use c_EM not c_shear in the α step (canonical Pitfall #5, Phase 3-A3 walk-back); evaluate at canonical primitives (no round numbers — same epic burned 2.7 OOM on a wrong C₀).
- **FT-2 (makes the Reynolds number predictive)** — forward-derive one δ_AVE from S(A) for a system with an independently measured loss tangent / Q / decoherence rate; predict the number. PASS: matches → δ_AVE lifts out of Class 1, retires the "taxonomic not derivational" caveat (`temporal-saturation-regime-classifier.md:310`). FAIL: δ_AVE is a label, not physics.
- **FT-3 (most Reynolds-like; predicts the transition point)** — sweep δ_AVE×N across 1 (vary N or saturation dwell) and check whether behavior flips branch-deterministic → cascade-stochastic AT the predicted boundary. PASS: sharp knee at δ_AVE×N~1. FAIL: knee elsewhere / no knee. Venue: AVE-Bench rig — separate track.
- **FT-4 (mechanism, independent of magnitude)** — the E/B asymmetry predicts ε(T) modulates while μ(T) stays frozen at low T. PASS: measured permittivity-vs-permeability thermal asymmetry. FAIL: symmetric modulation → E/B-mode-asymmetry mechanism falsified.

## §7 — Glossary / vocab reconciliation

- **`statistics` (AVE sense)** — previously had no canonical definitional home; now anchored in the new leaf.
- **δ_AVE / δ_AVE×N / "substrate-native loss tangent" / "Reynolds analogue"** — canonical in `temporal-saturation-regime-classifier.md`; the new leaf is its definitional sibling for the statistics context (reciprocal cross-link added).
- **E-modes / B-modes** (translational / microrotational) — used per INVARIANT-S2 Axiom-1 wording + `delta-strain-cosmic-tcc.md`; the new leaf explicitly corrects the common inversion (B-modes are the frozen sector).
- **substrate-agnostic vs substrate-distinct** — the FM-5 distinction (`translation-stochastics.md`, `ave-discipline-translate` v1.1 trigger 6); the new leaf §5 is the conceptual anchor, the translation table is the term-by-term map.
- **No master KB glossary exists** — the corpus uses domain-scoped no-claim glossary leaves (cosmic-axes, and now statistics). Consistent pattern; no reconciliation of a central glossary required.

## §8 — Open items + dependencies

- **Phase 4 dependency**: FT-1's α-chain sits on ch8 / theorem-3-1 / op21 provenance the in-flight Phase 4 walk-back is rewriting. Do not start FT-1 until Phase 4 merges.
- **Merge touchpoint**: this branch edits `common/index.md` (one additive Contents row); Phase 4 also modifies `common/index.md`. Expected trivial git auto-merge; flagged for the orchestration merge step.
- **Reciprocal cross-link** (optional hygiene): `translation-stochastics.md` could gain a See-also back to the new leaf. Not done here to keep the change surface minimal; queued.
