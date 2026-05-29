# clm-0ktpcn Phase 3-A1 + Q2 Combined — Pre-Registration

**Date**: 2026-05-26
**Branch**: `analysis/clm-0ktpcn-phase-3-A1-Q2-prose-reframe` off `main` @ `cf3c913e` (post PR #39 merge)
**Epic**: `_orchestration/clm-0ktpcn-golden-torus-alpha-strengthen.md`, Phase 3a-A1+Q2 brief (implementor sub-agent A)
**Scope-class**: mechanical-edit (prose-reframe + hygiene-cleanup); NOT a new derivation. Confidence-lift lever is precision-of-classification at the chapter prose level, not new substrate work.

---

## What is the deliverable?

Two related editorial actions on Vol 1 KB material, landed in a single auditor-gated branch:

### 3-A1 — prose reframe of `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md`

Apply `consistency-vs-emergence` v1.2 master-equation-derivation-path discipline at the chapter prose level. The chapter currently blends two epistemically distinct argument types under shared rhetorical framing:

- **Class 2 axiom-manifestation steps** (substrate primitives forced by axioms): Ax 1 Nyquist regime forcing $d = 1\,\ell_{\text{node}}$; Ax 2 self-avoidance forcing $R - r = 1/2$; Ax 3 minimum-reflection + spin-1/2 half-cover forcing $R \cdot r = 1/4$. These jointly fix the Golden Torus geometry $(R, r, d)$ from substrate primitives — the (R, r, d) derivation IS the substrate-mechanism content.

- **Class 4 consistency checks** (substrate result matches a standard-physics-community value): the assembled value $4\pi^3 + \pi^2 + \pi \approx 137.036$ matches the standard-physics-community-measured fine-structure constant $\alpha^{-1}_{\text{CODATA}} \approx 137.035999$ to the cold-lattice asymptote precision. This is Class 4 consistency-class, NOT Class 2 emergence on the observable axis — the AVE-distinct content is the (R, r, d)-from-substrate derivation, not the numerical match to CODATA.

Standard-physics-community names ("fine-structure constant α", "multipole expansion", "Born rule") appear only as parenthetical translation references; substrate-native vocabulary is the primary load-bearing form throughout per `ave-discipline-translate` v1.1 trigger 6.

### 3-Q2 — hygiene cleanup of 4 cascaded claim-quality entries

In `manuscript/ave-kb/vol1/claim-quality.md`, the following entries carry stale narrative-tail breadcrumbs from prior sessions (2026-05-06 era when dependency chains were rebound to `clm-trf3bd`, since superseded). These are pure-text artifacts inconsistent with current 0.55 / 0.65 solidities post-Phase-2-A cascade lift:

- `clm-5xon03` (Zero-Parameter Closure Status): rationale ends with "solidity drops to 0.28" (line 64) — current solidity is 0.65.
- `clm-3kzmt9` (ξ vs ξ_topo): rationale ends with "Solidity dropped from 0.50 to 0.25 in 2026-05-06" (line 173) — current solidity is 0.55.
- `clm-zw6mut` (Universal Spatial Tension Mass Scaling): rationale references "Under clm-unk0bd's solidity 0.40" (line 505) — current `clm-unk0bd` solidity is 0.65.
- `clm-b2anl4` (Four-Regime Map): rationale ends with "(Solidity dropped from 0.41 to 0.31 in 2026-05-06...)" (line 564) — current solidity is 0.55.

Also `clm-8ep2b4` (Macroscopic Yield Stress, line 472) carries the same 2026-05-06 trf3bd-era breadcrumb; included in the cleanup pass as found-during-edit.

Also `clm-82dxbj` (Domain Catalog, line 593) carries the same pattern; included.

### 3-A1+Q2 — clm-0ktpcn strengthen-by list update + confidence bump

In the `clm-0ktpcn` entry of `manuscript/ave-kb/vol1/claim-quality.md`:

- Remove the "A1 prose reframe" item from the strengthen-by list (closed by this work).
- Remove the "Q2 cleanup" item from the strengthen-by list (closed by this work).
- Bump confidence 0.55 → 0.60 (the +0.05 prose-reframe lift per the epic brief; no derivation work, just classification-precision).
- Update rationale with 2026-05-26 Phase 3-A1+Q2 closure note.

NOTE: the existing strengthen-by list in `clm-0ktpcn` (lines 95-97) lists three items: (i) sum-decomposition orthogonality, (ii) reframe-prose-alternative, (iii) δ_strain magnitude derivation. The "alternative reframe" item IS the A1 reframe; closing it via this work removes that bullet. The other two remain open.

---

## What would PASS look like?

Per the epic brief adjudication criteria:

- The prose reframe applies `consistency-vs-emergence` v1.2 master-equation-derivation-path-tracing cleanly: the chapter explicitly separates Class 2 axiom-manifestation (the (R, r, d) geometry derivation from Ax 1 + Ax 2 + Ax 3) from Class 4 consistency-checking (the assembled value matching CODATA).
- The Q2 cleanups don't break any cross-references — each stale breadcrumb is replaced by accurate post-Phase-2-A solidity language, no `solidity:` lines or `depends-on:` edges touched.
- The auditor confirms no accidental walk-back of the (R, r, d) derivation itself — the substrate-mechanism content of regimes (a)+(b)+(c) is preserved in full; only the framing language and the orthogonality / sum-decomposition rhetorical positioning change.
- Verify pipeline (`make verify-kb-metadata`) returns PASS after edits (with `make refresh-kb-metadata` run if refresh-fixable failures appear).
- Auditor returns GO or GO-WITH-AMENDMENTS; all amendments applied before push.
- Confidence on `clm-0ktpcn` lifts 0.55 → 0.60. Solidity stays at 0.55 (= `min(0.60, 0.65)`, the cascade chain through `clm-unk0bd` solidity 0.65 doesn't release the cap until `clm-0ktpcn`'s own confidence climbs to 0.65).

## What would WALK-BACK look like?

Per the epic brief adjudication:

The reframe surfaces a structural problem with the chapter's existing derivation chain — e.g., a Class 2 step that's actually Class 4 in disguise (the substrate-mechanism is asserted-not-derived in a way that becomes visible only when the framing-precision discipline is applied). Document honestly; escalate to Grant before applying — don't unilaterally walk back load-bearing claims.

Specific structural problems the reframe might surface (forward pre-registration of failure modes):

- **Regime (c) "screening" actually presupposes the standard-physics SU(2) postulate, not the K4-derived $T \to 2T \subset SU(2)$ chain at substrate level**. If the prose reveals that the half-cover is imported-from-QM rather than substrate-derived, the (R, r, d) chain's regime (c) is Class 4-disguised-as-Class-2. Note: Phase 2 sub-item 2 (Finkelstein-Misner spin-half derivation) closed this caveat for `clm-unk0bd`, with depends-on edge wired through `clm-salw2h`; the chapter prose already cites this resolution. Pre-registered as resolved.
- **The sum decomposition $\alpha^{-1} = \Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}}$ is itself a Class 4 consistency-pattern step** (an additive identification that happens to land at CODATA, not a substrate-derived consequence of the geometry). This is the existing `clm-0ktpcn` open caveat (strengthen-by item: "Close the sum-decomposition rule"). The reframe must NOT silently elevate this to Class 2 framing; if anything it should clarify the existing caveat-language.
- **The "orthogonality of three sectors" framing in the existing chapter prose** (line 102) asserts that the volume / surface / line sectors are independent contributions. The rationale block of `clm-0ktpcn` already notes (line 93) that $\Lambda_{\text{vol}} = 16\pi^3(R \cdot r)$ and $\Lambda_{\text{surf}} = 4\pi^2(R \cdot r)$ have collinear $(R \cdot r)$ dependence — i.e., the (R, r, d)→Λ map has only 2-dimensional image, "orthogonality" cannot mean parameter-independence. The reframe must preserve this caveat-language, not erase it. The Phase 3-A2 Schur-orthogonality work is in flight separately; Phase 3-A1 should NOT close that question.

If the reframe pass surfaces any of these as load-bearing structural-content problems (vs the language-precision problems the reframe is scoped to fix), STOP and escalate to Grant. Don't fix them silently in this branch.

---

## Skills firing on this work

Mandatory per the orchestration brief:

- **`consistency-vs-emergence` v1.2** — the DRIVING skill. Master-equation-derivation-path tracing applied at chapter prose level. Each regime's substrate-mechanism content traced explicitly; each step classified as derived-from-axiom / definitional-given-prior / requires-additional-postulate.
- **`ave-discipline-translate` v1.1 trigger 6** — fires continuously during prose composition. Substrate-native vocabulary mandatory throughout the reframe. Standard-physics-community names appear only as parenthetical translation references.
- **`ave-evidence-framing-discipline`** — "derived" vs "matches" vs "consistent-with" precision; the MAIN editorial task is making sure Class 2 derivations don't carry Class 4 framing-language, and vice versa.
- **`ave-prereg`** — corpus-grep before deriving (done; this prereg doc lands first).
- **`ave-canonical-leaf-pull`** — pull ch8 + Nyquist + crossings + screening leaves before reframing (done; ch8 read in full, regime-specific anchors are: `axioms-and-lattice/ch1-fundamental-axioms/tetrahedral-t-universality.md` for K4 rotation group $T = A_4$; `vol2/.../finkelstein-misner-spin-half-derivation.md` for Ax 3 spin-half mechanism; `vol2/.../torus-knot-uniqueness.md` (clm-8c3yhs) for (2,3) winding uniqueness).
- **`ave-directory-enumeration-discipline`** — accurate counts on entries cleaned (4 entries explicitly named in brief; ≥ 6 entries found in corpus survey; cleanup will enumerate explicitly with grep verification).
- **`ave-walk-back` v1.1 Type E** — fires if any value-amendment is caught mid-reframe; the grep-sweep will run before re-handoff to auditor.
- **`verify-before-cite` v1.4** — every file:line citation grep-verified; the chapter's existing primary-pointer / see-also cross-refs are not touched, but any new citation added during the reframe is grep-verified.
- **`ave-auditor` agent pass** — BEFORE finalizing edits and BEFORE the push.

---

## What is NOT in scope

Important scope-boundary discipline per the epic brief:

- **NOT** attempting Schur orthogonality derivation for the sum-decomposition (that's Phase 3-A2, separate parallel-safe sub-agent).
- **NOT** attempting δ_strain magnitude derivation from G_vac + equipartition (that's Phase 3-A3, deferred).
- **NOT** touching `clm-0ktpcn`'s depends-on edges or the cascade math (chain-promotion was done in Phase 2; this is confidence-lift on `clm-0ktpcn`'s own line).
- **NOT** touching the LaTeX source `manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex` — KB / manuscript split is per the existing pattern; chapter prose-reframe lives in the KB; LaTeX is the manuscript-authority and is left alone unless explicitly authorized.
- **NOT** drafting closure-roadmap entries (orchestration session does that after merge).
- **NOT** updating `clm-unk0bd` confidence or rationale (that's at its own confidence ceiling per the 2026-05-26 Phase 2-A note).

---

## Confidence-lift expectations

Per the epic brief: **clm-0ktpcn confidence bump 0.55 → 0.60**. This is the +0.05 prose-reframe lift; if Phase 3-A2 Schur orthogonality also lands as PASS in parallel, future cascade lift to 0.65 happens in a separate commit, not this one.

Solidity remains at 0.55 (= `min(0.60, 0.65)` where the 0.65 is `clm-unk0bd`'s current solidity). The cascade dependents of `clm-0ktpcn` (the 6 entries cleaned in 3-Q2 + others further downstream) inherit solidity through the `min(...)` discipline; their solidity values do not change as a result of this work.

---

## Forward pre-registration of risks

Per the epic brief honest-closure probability ~85%:

- ~85% probability of clean closure as described above (mechanical edit; the auditor confirms classification precision is satisfied).
- ~15% probability the auditor catches a prose-precision gap that needs `ave-walk-back` Type E sweep (a value-statement somewhere in the chapter has drifted out of consistency with current claim-quality, found during the reframe; the sweep is mechanical and unblocks closure).
- ~5% conditional probability that the reframe surfaces a structural problem (Class 2 step that's Class 4 in disguise) which forces WALK-BACK escalation to Grant. Honest-closure default is to PASS; structural surfacing would be a different result-class.

Pre-registration of stop conditions:

- If the verify pipeline returns refresh-fixable failures after refresh, STOP and surface to orchestration before pushing.
- If the auditor returns HOLD (vs GO / GO-WITH-AMENDMENTS), STOP and surface to orchestration before pushing.
- If at any point the reframe surfaces a load-bearing structural-content question (vs language-precision), STOP, document honestly, escalate to Grant.

---

## Auditor pass + return-format expectation

Per the epic brief: `ave-auditor` agent BEFORE finalizing edits and BEFORE the push. Expected return-format: GO / GO-WITH-AMENDMENTS / HOLD adjudication with explicit findings list. Any GO-WITH-AMENDMENTS findings applied before final push.

---

## Cross-references

- Epic: [`_orchestration/clm-0ktpcn-golden-torus-alpha-strengthen.md`](../_orchestration/clm-0ktpcn-golden-torus-alpha-strengthen.md) §Phase 3a-A1+Q2 combined brief
- Chapter under edit: [`manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md`](../manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md)
- Claim-quality file under edit: [`manuscript/ave-kb/vol1/claim-quality.md`](../manuscript/ave-kb/vol1/claim-quality.md)
- Cascaded entries with stale breadcrumbs: `clm-5xon03` (line ~64), `clm-3kzmt9` (line ~173), `clm-zw6mut` (line ~505), `clm-b2anl4` (line ~564); also `clm-8ep2b4` (line ~472), `clm-82dxbj` (line ~593) found during pre-survey
- Translation infrastructure: [`manuscript/ave-kb/common/translation-tables/translation-qm.md`](../manuscript/ave-kb/common/translation-tables/translation-qm.md) §A for QM / Born rule mappings; [`translation-stochastics.md`](../manuscript/ave-kb/common/translation-tables/translation-stochastics.md) for stochastic-physics vocabulary
- consistency-vs-emergence v1.2: `~/.claude/skills/consistency-vs-emergence/SKILL.md`
- ave-discipline-translate v1.1 (trigger 6): `~/.claude/skills/ave-discipline-translate/SKILL.md`
