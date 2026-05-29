# Pre-registration: clm-0ktpcn Golden Torus α Strengthening Workstream

**Date frozen**: 2026-05-25 (BEFORE any derivation work begins)
**Workstream**: `analysis/golden-torus-alpha-strengthen` (off `main` @ `c655526b`)
**Discipline**: `ave-prereg` Phase 0 pre-registration (one-paragraph-per-sub-item with corpus-prior-work state)
**Target claim**: `clm-0ktpcn` — Golden Torus α Derivation (Three-Regime Closure)
**Current solidity**: 0.45 (highest-leverage shaky-load-bearing claim in AVE corpus; 21 dependents)
**Orchestration epic**: [`_orchestration/clm-0ktpcn-golden-torus-alpha-strengthen.md`](../_orchestration/clm-0ktpcn-golden-torus-alpha-strengthen.md)
**Corpus survey by**: ave-corpus-grep agent, 2026-05-25 (findings in epic doc Phase 0a section)

## Workstream-level frame

The 4 open sub-items in `clm-0ktpcn`'s strengthen-by list represent the structural reasons solidity is capped at 0.45. Closing any one should raise solidity meaningfully; closing all four should approach 0.75+ (move from "use as input only" to "ok to build on, see caveats"). The 21 downstream dependents inherit the cap proportionally.

Workstream goal: **close at least one of the 4 sub-items in Phase 1**, with audit by `ave-auditor` confirming the derivation is rigorous enough to raise solidity. Cascade propagation to dependents in Phase 4 only if classification changes materially (e.g., from "use as input only" to "ok to build on, see caveats").

## Per-sub-item pre-reg

### Sub-item 1 — (2,3) phase-space winding uniqueness

**What I expect**: The corpus has a knot-theoretic minimality argument (`torus-knot-uniqueness.md` + L3 doc 25) but NOT a dynamical-stability uniqueness argument from substrate primitives. If we attack this sub-item, the genuine new derivation needs to show why the K4-Cosserat substrate's *dynamics* select (2,3) — i.e., why (3,2), (2,5), (3,4), (5,3) candidates do not form stable bound states under the AVE engine. Hypothesis: (2,3) is selected because it's the smallest non-trivial closed-loop torus knot consistent with (a) the 2-conjugate-variable LC tank structure (which forces one winding-pair element = 2) and (b) the K4 4-vertex / 3-inter-vertex-edge connectivity (which fixes the other = 3 as smallest non-coprime-violating choice). This is mechanism-conjectural, not derived; the derivation work is to either confirm or refute it via substrate-dynamics argument or numerical engine test.

**Why**: clm-unk0bd Caveat 3 explicitly: "The (2,3) phase-space winding numbers are asserted as the simplest stable winding, not derived from a uniqueness argument." Closing this addresses one of the 4 cap-binding rationale bullets.

**What would discriminate**: A successful derivation must (a) produce the (2,3) selection from substrate primitives (Ax 1 K4 + Ax 2 TKI + Ax 3 minimum-reflection); (b) show that (3,2), (2,5), (3,4) candidates fail at least one stability criterion; (c) survive `ave-independence-check` (the 2 and the 3 must not be algebraically derivable from each other in a way that collapses the "two independent topological numbers" framing); (d) match the phase-space-coordinate discipline (analysis MUST be in (V_inc, V_ref) / Clifford-torus coordinates, not real-space lattice-Cartesian).

**Corpus prior-work state**: DERIVED-WEAK. `torus-knot-uniqueness.md` (clm-8c3yhs) carries doc 25's minimality argument; doc 25 §9 explicitly admits the dynamical-stability gap. Real green-field for the dynamical-stability uniqueness argument.

### Sub-item 2 — Finkelstein–Misner spin-1/2 derivation chain explicit

**What I expect**: This is mostly a **KB-curation move, not new derivation work**. L3 doc 23 (`research/_archive/L3_electron_soliton/23_step2_spin_half_from_k4.md`, 272 lines) already has the most detailed FM-on-K4-extended-unknot derivation in the corpus: §2.2 applies the belt-trick to the K4 unknot defect; §3 provides a gyroscopic-isomorphism numerical anchor (10⁻⁸ deviation between K4-native extended-unknot gyroscopic precession and quantum Pauli evolution). The KB currently just ASSERTS-BY-IMPORT in `spin-half-paradox.md` (clm-salw2h). Promotion path: distill doc 23 §2-3 into a new canonical KB leaf alongside `spin-half-paradox.md` or extending it with the K4-native belt-trick mechanism explicit.

**Why**: clm-unk0bd Strengthen-by item 2 explicitly: "Spell out the Finkelstein–Misner spin-1/2 derivation from the K4 → A4 → 2T ⊂ SU(2) chain explicitly in the leaves." The L3 doc has the content; the KB doesn't carry it forward.

**What would discriminate**: The promoted leaf must (a) cite L3 doc 23 §2.2 belt-trick mechanism + §3 numerical anchor verbatim; (b) integrate cleanly with `k4-rotation-group.md` §6 (which currently punts to FM); (c) survive `ave-auditor` review for derivation rigor; (d) be referenced from `ch8-alpha-golden-torus.md` Regime (c) screening discussion (currently the leaf says "Spin-1/2 half-cover of the standard Clifford torus" without anchor citation). Doc 23 §7 admits one limitation: "Does not provide a discrete-lattice computation of the FM kink on K4 (would require full extended-defect simulation, not currently in engine)" — this gap is explicit and bounded; the promoted leaf should carry the same scope-correction.

**Corpus prior-work state**: DERIVED-HYBRID (L3) + ASSERTED-BY-IMPORT (KB). Highest-ROI promotion path.

### Sub-item 3 — Photon-720° compatibility resolution

**What I expect**: L3 doc 06 (`research/_archive/L3_electron_soliton/06_winding_index_projection.md`) has a substantive projection-level argument: AVE Level-1 carries SU(2) windings on the Clifford phase-space torus (where 720° lives); the Hopf fibration projects to Level-2 (polarization); polarization projects to Level-4 (geometric photon trajectory, where 720° is invisible). Doc 06 §5 (lines 86-103) gives a falsifiable consistency prediction (3 tube-wraps per Clifford-minor cycle). Doc 06 §8 (lines 133-136) lists the 720° question as queue item [3], unresolved pending Phase-3 numerical work. Promotion path: distill doc 06's projection-map argument into a KB leaf, plus walk back the stale Möbius-K4 framing at `manuscript/frontmatter/00_foreword.tex:98` (the OLD framing the resolution supersedes).

**Why**: clm-unk0bd Caveat 2 explicitly: "Whether this fully closes the objection is a final determination deferred to a more intense review after the porting effort is complete." This is the framework's officially-pending open question.

**What would discriminate**: A successful promotion must (a) carry doc 06's projection-map argument verbatim into a KB leaf; (b) make explicit where the 4π lives (extended unknot defect via FM) vs where it doesn't (photon Level-4 trajectory); (c) include the falsifiable §5 prediction (3 tube-wraps per Clifford-minor cycle, observable via Cosserat-engine simulation); (d) cascade-update `00_foreword.tex:98` from Möbius-K4 framing to extended-unknot framing; (e) survive `ave-discrimination-check` (the resolution must be AVE-distinct vs SM/QED; photon spin-1 is standard, but the "no inherited 720° via Hopf-fibration phase-discard" framing is AVE-specific).

**Corpus prior-work state**: PARTIAL-DERIVATION (L3) + DEFERRED (KB). Middle-complexity promotion + walk-back work.

### Sub-item 4 — Topological protection (real-space vs phase-space)

**What I expect**: This is the **highest-truth-discovery sub-item**, with the largest gap between asserted-position and engine-evidence. clm-unk0bd Caveat 1 admits: "Topological protection is not established at the real-space-body level... phase-space-winding-as-protection is the framework's current position; not yet rigorously established." `phase-locked-topological-thread.md:187-199` gives empirical support via K4-TLM 32³ simulation (vacuum + mild-noise traces overlap; extreme-noise destroys winding). But `VACUUM_ENGINE_MANUAL.md` A30/A32/A34 documents the OPPOSITE empirical finding from L3 Round 6 + Phase 5: the K4-Cosserat engine does NOT dynamically protect localized topology — topology must be ansatz-injected, not emergent. This is the most genuinely open sub-item; attacking it forces either (a) rigorous derivation of phase-space-winding-as-protection from substrate primitives, OR (b) honest framework walk-back to "stability is purely energetic, not topological" with downstream cascade (electron-identification.md:56's "Ax1 topological protection ✅ axiom-derived" status marker would need revision).

**Why**: clm-unk0bd Caveat 1 is one of two caveats explicitly identified in the solidity rationale as "load-bearing structural elements as not established." The other is the (2,3) uniqueness from sub-item 1.

**What would discriminate**: A successful derivation (path a) must produce phase-space-winding-as-protection from Ax 1+2+3+4 primitives in a way that explains both `phase-locked-topological-thread.md`'s positive K4-TLM result AND `VACUUM_ENGINE_MANUAL.md` A30/A32/A34's negative engine-stability findings. A successful walk-back (path b) must update `electron-identification.md:56` honestly + cascade to dependent claims + clarify whether the framework's "topologically protected soliton" language is purely-energetic-stability-with-topological-label or genuine topological invariant. Either outcome materially advances clarity. `ave-evidence-framing-discipline` is the critical check: any "rigorously established" claim must actually meet the bar.

**Corpus prior-work state**: ASSERTED in KB + EMPIRICALLY-CONTESTED in L3 engine work. Real green-field with negative evidence pushing against current position.

## Cross-cutting discriminators (apply to all sub-items)

1. **`consistency-vs-emergence` classification mandatory before any sub-item Phase 1 work**: each sub-item's derivation must be classified as definitional-identity / axiom-manifestation / consistency-check / emergence-test / operating-point-projection BEFORE writing. Likely classifications: sub-item 1 = axiom-manifestation; sub-item 2 = axiom-manifestation; sub-item 3 = consistency-check; sub-item 4 = open between axiom-manifestation and operating-point-projection.

2. **`phase-space-coordinate-check` MANDATORY for sub-items 1, 3, 4**: all three involve phase-space (Clifford torus) structure. Any test design or derivation must use phase-space coordinates (V_inc, V_ref, impedance plane), NOT real-space lattice-Cartesian. The skill exists precisely to catch this failure mode.

3. **`ave-independence-check` for sub-item 1**: if a "uniqueness argument" produces N "independent reasons" for (2,3), each pair must be checked algebraically for non-derivability via canonical substrate identities. The (2,3) values themselves must not be algebraically derivable from each other in a way that collapses to "one number, two presentations."

4. **`ave-canonical-leaf-pull` for all sub-items**: scaling-law / energy-quantum class for sub-item 1; matched-coupling / topology class for sub-items 2-4. Enumerate canonical leaves before deriving.

5. **`ave-driver-script-honesty` for any numerical engine test**: if Phase 1 includes engine validation (e.g., for sub-item 4 to reconcile K4-TLM positive vs VACUUM_ENGINE_MANUAL negative findings), the four-discriminator check applies (hardcoded-literal vs canonical-import; fit-against-target vs forward-prediction; internal-contradiction; silent-overclaim plotting).

## Closure criteria

This workstream closes Phase 1 when at least one sub-item's derivation:

- (a) Lands at least one new canonical KB leaf OR materially augments existing leaves AND
- (b) Updates `clm-0ktpcn` and/or `clm-unk0bd` rationale block to reflect the closed item AND
- (c) Triggers `make refresh-kb-metadata` which recomputes solidity AND
- (d) Survives `ave-auditor` independent review on derivation rigor AND
- (e) Triggers cascade propagation to at least 1 dependent leaf (if classification changes) OR is explicitly logged as "solidity tier change applies to clm-0ktpcn only, dependents inherit no change" with rationale.

If the work surfaces a **walk-back** (e.g., honest concession in sub-item 4), closure is logged in closure-roadmap §0.5 instead of §0 dashboard.

## Plumber-physical question to Grant (pending)

Surfaced post-corpus-survey: **Which sub-item to tackle first**, given the ROI map:

- Sub-item 2 (FM chain) = mechanical promotion, ~1 session, modest solidity bump
- Sub-item 4 (topological protection) = green-field with empirical contradiction, multi-session, large solidity bump if closed
- Sub-item 1 (dynamical-stability uniqueness) = green-field, multi-session, modest-large solidity bump
- Sub-item 3 (photon-720°) = promotion + walk-back, ~1-2 sessions, modest solidity bump

And: gut intuition for the mechanism on whichever you pick.

Awaiting Grant adjudication before Phase 1 work begins.
