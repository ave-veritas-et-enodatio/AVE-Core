# Phase 3-A4 Prework Brief — Op21 Multi-Mode Mode-Counting Formalization

**Status**: SPAWN-READY after PR #45 (Benn maintenance/d12 tooling fixes) merges. Off `main` @ post-PR-#45-merge.
**Origin**: Phase 3-A2 WALK-BACK reformulated clm-0ktpcn's strengthen-by item from "establish functional orthogonality (Schur)" → "promote Op21 multi-mode generalization to fully-derived canonical leaf". Closure target: clm-0ktpcn confidence **0.60 → 0.65** if PASS; cascade through 21 dependents.

This doc is the implementor-spawn-ready brief. Future-compacted-self should: confirm PR #45 merged → spot-check clm-0ktpcn entry block in `vol1/claim-quality.md` for any Benn modifications → spawn Phase 3-A4 implementor using THIS prework brief as the briefing material.

## Prework completed by orchestration session 2026-05-27 EOD (pre-spawn)

### Op21 canonical paragraph location (verified)

**Canonical home**: `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md` §"Op21 multi-mode generalization" (paragraph-level statement, not yet a fully-derived canonical leaf).

**Verbatim paragraph content** (per grep 2026-05-27 EOD):

> The Q-factor decomposition generalizes via Op21 multi-mode form: at the saturation boundary, each mode with $\ell$ wavelengths around a 1D circumference releases $\sim 1/\ell$ of energy per cycle, giving $Q = \ell$ per mode. The Golden Torus at the Nyquist mode-count identity (single-cell-per-natural-unit) makes the mode counts equal the geometric measures: 1D mode (circumference $L$) → cell-count $L$; 2D mode → cell-count area; 3D mode → cell-count volume. The three-$\Lambda$ sum is exactly the Op21 multi-mode generalization at Golden Torus geometry.

**Phase 3-A4 deliverable**: promote this paragraph to a fully-derived canonical leaf with step-by-step substrate-primitive trace.

### Substrate-physics derivation chain to formalize

Per v1.2 consistency-vs-emergence master-equation-derivation-path discipline, the Phase 3-A4 derivation must trace explicit substrate primitives at each step:

1. **Ax 1 Nyquist cell size**: $\ell_{node}$ canonical (`src/ave/core/constants.py`). Discrete cell counting becomes the natural cardinality measure for substrate modes at the lattice level.
2. **Ax 3 minimum-reflection principle → $\Gamma = -1$ TIR boundary**: at the saturation boundary, the substrate reflects with $\Gamma = -1$ (canonical pair-production mechanism). Each mode with $\ell$ wavelengths releases $\sim 1/\ell$ of energy per cycle → $Q = \ell$ per mode (the substrate-mechanical origin of the mode-counting identity).
3. **Codimensional mode-category independence**: 1D / 2D / 3D modes are linearly independent contributions to the Q-factor sum. The substrate-mechanical reason: Nyquist cell-count over codimensional mode-categories doesn't double-count (the lattice's discrete sampling has no degeneracy across dimensions).
4. **Golden Torus geometric measures = mode counts**: at $(R, r, d) = (\varphi/2, (\varphi-1)/2, 1)$ (per `vol1/ch8-alpha-golden-torus.md:31-90` three-substrate-regime derivation), single-cell-per-natural-unit identity makes the mode counts equal the dimensionless geometric measures: 1D = $2\pi R$ → circumference; 2D = $4\pi^2 R r$ → surface area; 3D = $16\pi^3 R r d$ → volume.
5. **Three-Λ sum closure**: $\Lambda_{\text{line}} + \Lambda_{\text{surf}} + \Lambda_{\text{vol}} = \pi + \pi^2 + 4\pi^3 = \alpha^{-1}$ at Golden Torus operating point (per ch8 lines 31-90).

### Op21 canonical-identification reconciliation question (open BEFORE spawn — needs Grant adjudication)

`common/operators.md:57` explicitly flags two non-equivalent Op21 identifications:

- **Operators-table canonical**: $Q \sim 1/\ln(Z_1/Z_0)$ (Bardeen BCS mapping, Vol 1 Ch 6 §1.21 explicit formula; superconductivity threshold mechanism)
- **Theorem 3.1' multi-mode form**: $Q = \ell$ (lattice pitch in natural units, per mode at $\Gamma = -1$ saturation boundary)

Operators-table row's note: *"these may be different identifications (Q-as-lattice-pitch may be the bootstrap / $\alpha = 1/137.036$ derivation, NOT the Bardeen mapping). **Cross-reference needs auditor-lane confirmation**."*

**Substrate-mechanical question for Grant**: are these two formulas:
- **(A) Two views of the same Op21 mechanism** (Bardeen BCS impedance-mismatch formula reduces to $Q = \ell$ at the Golden Torus Nyquist mode-count identity)?
- **(B) Two distinct mechanisms** sharing the Op21 label spuriously (one is BCS-superconductivity Q-factor; one is multi-mode mode-counting Q-factor; both deserve canonical-leaf status but as distinct operators)?
- **(C) The Bardeen BCS form is downstream of the mode-counting form** (i.e., $Q = \ell$ is the foundational substrate-mechanical identity; the BCS $1/\ln(Z_1/Z_0)$ form is a specific specialization to superconductivity threshold)?

**Recommended adjudication path**: Phase 3-A4 implementor surfaces this reconciliation question in the prereg before deriving. The substrate-mechanical answer (A/B/C) shapes the structure of the canonical leaf — single Op21 with two views (A) vs Op21a/Op21b split (B) vs Op21-foundational + Op21-specialization (C).

### Step 3.5 dimensional analysis at canonical primitives (pre-frozen per v1.1 ave-prereg discipline)

Per v1.1 Step 3.5 (mandatory for scaling-law / magnitude expectations): pre-freeze the Op21 derivation's expected scaling-law magnitudes at canonical primitives BEFORE deriving from scratch.

**Op21 Q = ℓ per mode at Golden Torus**:

- $R = \varphi/2 \approx 0.809$, $r = (\varphi-1)/2 \approx 0.309$, $d = 1$ at Golden Torus (per ch8 lines 31-90)
- 1D mode (circumference): $\Lambda_{\text{line}} = 2\pi R \approx 5.083$... wait, this equals $\pi$? Check: $2\pi R = 2\pi \cdot \varphi/2 = \pi \varphi \approx 5.083$. But $\Lambda_{\text{line}} = \pi$ per ch8 line 90. **Reconciliation needed**: the "circumference $L$" in the canonical paragraph maps to $\pi$, not to $2\pi R$.
- 2D mode (surface): $\Lambda_{\text{surf}} = 4\pi^2 R r$ per ch8:107. At $Rr = \varphi(\varphi-1)/4 = (\varphi^2 - \varphi)/4 = (1)/4 = 0.25$ (using $\varphi^2 = \varphi + 1$). So $\Lambda_{\text{surf}} = 4\pi^2 \cdot 0.25 = \pi^2 \approx 9.87$. ✓ matches canonical.
- 3D mode (volume): $\Lambda_{\text{vol}} = 16\pi^3 R r d$ per ch8:107. At $Rr = 1/4$, $d = 1$: $\Lambda_{\text{vol}} = 16\pi^3 \cdot 1/4 \cdot 1 = 4\pi^3 \approx 124.0$. ✓ matches canonical.

**Dimensional check surfaces a Phase 3-A4 derivation gap**: the $\Lambda_{\text{line}} = \pi$ (NOT $2\pi R = \pi \varphi$) means the 1D mode count is NOT literally the circumference at $R = \varphi/2$ — there's an implicit normalization. The canonical Op21 paragraph says "1D mode (circumference $L$) → cell-count $L$" but at Golden Torus the cell-count is $\pi$, not $2\pi R = \pi \varphi$. The substrate-mechanical reason for this normalization needs explicit derivation in the canonical leaf.

**This is the substantive Phase 3-A4 derivation work** — the substrate-mechanical reason the $\Lambda_{\text{line}} = \pi$ value emerges (not $\pi \varphi$) is the load-bearing closure step.

**Sanity check against PONDER-05 empirical anchor**: PONDER-05 doesn't directly probe Op21 mode-counting; the α derivation that Op21 supports is the empirical anchor (CODATA $\alpha^{-1} \approx 137.036$ vs $4\pi^3 + \pi^2 + \pi \approx 137.036$ matches to ~10⁻⁶). Phase 3-A4 closure means the substrate-mechanical mechanism that produces this number is now fully canonical-leaf-derived, not paragraph-level asserted.

### Cross-reference infrastructure (Phase 3-A4 leaf needs to cite)

**Upstream canonical leaves** (Phase 3-A4 derivation depends on):

- `manuscript/ave-kb/common/operators.md:57` — Op21 canonical row + cross-reference question
- `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md` — current Op21 paragraph + Q-factor framework
- `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md:31-90` — three-substrate-regime derivation of $(R, r, d)$
- `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md:23` — K4-bond-pair LC-tank phase-space canonical positioning of (p,q) (per PR #44 cross-ref)
- `manuscript/ave-kb/common/boundary-observables-m-q-j.md` — $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ boundary-observability structure that the three-Λ decomposition corresponds to
- `manuscript/ave-kb/common/appendix-derived-numerology.md` — $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$ canonical statement

**Downstream impact** (Phase 3-A4 closure cascades through):

- `clm-0ktpcn` (Golden Torus α Derivation; **21 dependents**)
- Cascade dependents (post-Phase-2-A cascade, currently at solidity 0.60 due to clm-0ktpcn dep-cap):
  - clm-unk0bd (Electron Body Topology)
  - clm-2dwzib, clm-5xon03, clm-3kzmt9, clm-8ep2b4, clm-zw6mut, clm-82dxbj, clm-b2anl4 (per Q2 hygiene cleanup list)
  - clm-9s9apq (EMT $p_c = 8\pi\alpha$)
  - ... + more (verify post-Phase-3-A4 via `make verify-kb-metadata` + grep)

**Cascade math**: clm-0ktpcn 0.60 → 0.65 lifts dependents whose own confidence is ≥ 0.65 via dep-gate `min(confidence, depends-on-solidities)`. Each dependent at confidence 0.65 lifts solidity to 0.65; each at < 0.65 stays at own confidence ceiling.

### Q-PBP-1 + canonical (p,q) substrate-physical reframing context (per PR #43 + #44)

Phase 3-A4 derivation MUST respect the canonical (p,q) substrate-physical positioning landed in PR #43 + PR #44:

- **(p,q) labels live at K4-lattice bond-pair LC-tank phase-space level** (`electron-identification.md:23`); NOT at Cosserat-SU(2) Level 1 (L3 doc 06 §2 framing is valid continuum recasting, not the foundational level)
- **(p,q) is a NONLINEAR-saturation-confined-soliton topological property** at $\Gamma = -1$ TIR boundary above $V_{yield}$; NOT a linear-regime substrate-mode-eigenvalue label (Path B-prime FALSIFIED 2026-05-27 per outcome C)
- **The three-substrate-regime derivation forcing (R, r, d) → (2,3)** at `vol1/ch8-alpha-golden-torus.md:31-90` IS the canonical (2,3) derivation route (NOT Path B Faddeev-Skyrme; NOT Path B-prime linear-regime band-splitting)

Phase 3-A4's Op21 multi-mode mode-counting formalization is the **substrate-mechanism path** for the three-Λ assembly that ch8 derives — it's the cross-volume bridge from "three substrate regimes force (R, r, d)" (ch8) to "three-Λ sum closes at $4\pi^3 + \pi^2 + \pi$" (theorem-3-1 + Op21). Phase 3-A4 IS this bridge formalization.

### Op17 substrate-matched-impedance cross-reference (per PR #42 + ba406d65)

Phase 3-A4 may benefit from explicit cross-reference to the Op17 substrate-matched-impedance interpretation that landed at `parametric-coupling-kernel.md §14.9`:

- Op17: $T^2 = 1 - \Gamma^2$ at canonical matched-impedance condition ($\Gamma = 0$)
- Op21: $Q = \ell$ per mode at canonical saturation boundary ($\Gamma = -1$)
- **Substrate-mechanical complementary structure**: Op17 lives at $\Gamma = 0$ (perfect transmission); Op21 lives at $\Gamma = -1$ (perfect reflection / TIR saturation boundary). The two operators are the two-endpoints of the substrate $\Gamma$-space — Op17 = open-boundary energy transfer; Op21 = closed-boundary energy quantization. Worth cross-referencing in the Phase 3-A4 canonical leaf.

### Discipline candidates from PR #44 pollution incident

Phase 3-A4 implementor should bake in:

- **Worktree-absolute-paths from first-call**: in worktree-isolated implementor sessions, do ALL Reads + Edits on worktree-absolute paths from the first call, even for citation-verification reads. The PR #44 incident showed that brief-supplied path references get auto-resolved relative to most-recently-read absolute-path file; if first Read is on parent-repo absolute path, subsequent Edits inherit the bias and pollute parent. Implementor brief MUST explicitly direct: "Read + Edit all files via worktree-absolute paths from your worktree at `.claude/worktrees/agent-<id>/...`; do NOT Read parent-repo absolute paths even for verification."

### Skills firing list (pre-spawn checklist)

Phase 3-A4 implementor brief should explicitly invoke:

- **ave-prereg v1.1** — Step 3.5 dimensional analysis at canonical primitives (already pre-frozen above; implementor inherits + extends)
- **ave-canonical-leaf-pull v1.3** — Trigger 17 vocabulary-broadened pre-survey (substrate-native + standard-physics wedges; already partially executed above; implementor extends to L3 archive + AVE-HOPF sibling repo if relevant)
- **ave-analytical-tool-selection** — Mode + Network class; Op21 mode-counting is the canonical tool; cross-check ave-analytical-toolkit-index.md for full toolkit
- **ave-discipline-translate v1.1 Trigger 6** — substrate-native vocabulary primary; SM names ("BCS", "Bardeen mapping", "cavity Q-factor", "mode counting", "natural units") only as parenthetical translation references
- **substrate-native-check** — K4-TLM + Cosserat + Ax 1 + Ax 3 substrate structure walk before deriving Op21
- **consistency-vs-emergence v1.2** — explicit Class 2 substrate-mechanism vs Class 4 substrate-agnostic-consistency classification with master-equation-derivation-path tracing
- **phase-space-coordinate-check** — Op21 mode-count is in phase-space (winding indices); ch8 (R, r, d) is in real-space geometry; Golden Torus geometric-measure equality is the bridge — keep coordinates clean
- **ave-evidence-framing-discipline** — "derived from Ax 1 + Ax 3 + codimensional independence" vs "asserted at paragraph level + cited from theorem-3-1-q-factor.md" precision
- **ave-canonical-source** — if any Python computation, canonical constants from `src/ave/core/constants.py`
- **ave-walk-back v1.1** — Type E if value-amendment fires mid-derivation; reconciliation answer (A/B/C) on Op21 dual-identification may be a Type B walk-back if "Bardeen BCS" framing on operators.md row needs amendment
- **verify-before-cite v1.4** — every file:line citation grep-verified
- **ave-discrimination-check** — SM-counterfactual + interpretive-alternatives BEFORE asserting Class 2 substrate-distinct

### Branch + spawn protocol

- **Branch**: `analysis/clm-0ktpcn-phase-3-A4-op21-formalization` off `main` @ **post-PR-#45-merge** (currently main @ `6ac5d7fc`; will be updated post PR #45 merge to a new SHA)
- **Push branch but DO NOT merge** — orchestration session opens PR (PR-style policy)
- **Worktree isolation**: `isolation: "worktree"` per `Agent` tool; STAY IN WORKTREE per discipline candidate above
- **Single-deliverable scope**: Op21 multi-mode mode-counting canonical leaf + clm-0ktpcn entry update (if PASS) + cross-references at parametric-coupling-kernel.md + theorem-3-1-q-factor.md (cross-ref to new canonical leaf from existing paragraph location); do NOT also tackle Phase 3-A3 (δ_strain magnitude) or Phase 3-A5 (T = A_4) or Phase 2-LLCP

### Adjudication criteria

- **PASS**: Op21 multi-mode mode-counting derived end-to-end from Ax 1 + Ax 3 + codimensional independence; substrate-mechanical reason for $\Lambda_{\text{line}} = \pi$ normalization (not $\pi \varphi$) explicit; canonical leaf created with step-by-step derivation chain. clm-0ktpcn confidence lifts 0.60 → 0.65; cascade through 21+ dependents per `make refresh-kb-metadata`. Class 2 substrate-mechanism emergence.
- **PARTIAL**: Op21 mode-counting derived but the operators-row dual-identification reconciliation (Bardeen BCS $1/\ln(Z_1/Z_0)$ vs $Q = \ell$) gets stuck on a sub-problem. Document honestly; flag the gap; partial confidence lift 0.60 → 0.62 or 0.63 (substrate-mechanism path identified + partially formalized).
- **WALK-BACK**: derivation surfaces structural problem (e.g., the $\Lambda_{\text{line}} = \pi$ normalization isn't substrate-mechanically derivable from Ax 1 + Ax 3; needs an additional substrate primitive that doesn't exist canonically). Document honestly; reframe Phase 3-A4 scope; trigger Type B walk-back propagation.

### Honest closure probability

- **PASS**: ~60% (substrate-mechanical content already exists at paragraph level; Phase 3-A4 is formalization-not-discovery work; main risk is the operators-row dual-identification reconciliation question requiring a Grant adjudication mid-derivation)
- **PARTIAL**: ~25% (if reconciliation question can't be cleanly resolved by implementor; substrate-mechanism path identified + half-formalized)
- **WALK-BACK**: ~15% (if $\Lambda_{\text{line}} = \pi$ normalization needs additional substrate primitive)

### Post-PR-#45-merge spot-check (CRITICAL pre-spawn)

When PR #45 merges:

1. Pull main; verify HEAD advanced past `6ac5d7fc`
2. `grep -A 50 "clm-0ktpcn" manuscript/ave-kb/vol1/claim-quality.md | head -60` — verify the clm-0ktpcn entry block at line ~75-100 is unchanged by Benn's +25 lines (most likely Benn's lines are new claim entries elsewhere in the file, not modifications to clm-0ktpcn). If clm-0ktpcn IS modified, Phase 3-A4 implementor brief needs amendment.
3. Quick scan of new vol3 gravity claim entries for clm-0ktpcn dependencies: `grep -A 5 "depends-on" manuscript/ave-kb/vol3/gravity/ch20-white-dwarf-predictions/ manuscript/ave-kb/vol3/gravity/ch02-general-relativity/double-deflection.md 2>/dev/null` — if any new claim depends on clm-0ktpcn or its cascade-lifted relatives, the Phase 3-A4 lift has MORE leverage (free cascade leverage amplification).
4. Verify `make verify-kb-metadata` PASS on post-Benn-merge state (his KB tooling refactoring may have changed verify behavior; ensure baseline-PASS before spawn).
5. Verify `make refresh-kb-metadata` no-op on post-Benn-merge state (frontmatter changes already landed by Benn; no orchestration-side regeneration needed pre-spawn).

### Implementor brief (ready to paste into Agent tool prompt post-PR-#45)

Self-contained brief that just needs the branch SHA updated:

```
You are an AVE implementor session executing Phase 3-A4 of the clm-0ktpcn Golden Torus α-strengthening epic. Your single deliverable is promoting the paragraph-level Op21 multi-mode mode-counting statement at `theorem-3-1-q-factor.md` §"Op21 multi-mode generalization" to a fully-derived canonical leaf with step-by-step substrate-primitive trace.

Read first (mandatory):
1. `_orchestration/2026-05-27_phase-3-a4-prework.md` — THE prework brief; primary briefing material (this doc)
2. `_orchestration/clm-0ktpcn-golden-torus-alpha-strengthen.md` — full epic context
3. `_orchestration/2026-05-27_session-handoff.md` — session arc + skill state + canonical (p,q) substrate-physical reframing context
4. CLAUDE.md + manuscript/ave-kb/CLAUDE.md — repo + KB conventions
5. `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md` §Op21 paragraph + surrounding context
6. `manuscript/ave-kb/common/operators.md:57` — Op21 canonical row + dual-identification note
7. `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md:31-90` — three-substrate-regime derivation forcing (R, r, d)
8. `manuscript/ave-kb/common/boundary-observables-m-q-j.md` — $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ boundary-observability structure

Operating parameters:
- Branch: `analysis/clm-0ktpcn-phase-3-A4-op21-formalization` off `main` @ <POST-PR-#45-MERGE-SHA>
- Push branch but DO NOT merge — orchestration opens PR (PR-style policy)
- Single-deliverable scope per prework Adjudication criteria

CRITICAL — Worktree-absolute-paths discipline (new candidate from PR #44 incident):
You are spawned in `isolation: "worktree"` at `.claude/worktrees/agent-<your-id>/`. STAY IN YOUR WORKTREE. Do ALL Reads + Edits via worktree-absolute paths from your FIRST call onward, including citation-verification reads. Do NOT Read parent-repo absolute paths (`/Users/grantlindblom/AVE-staging/AVE-Core/...`) — only your worktree paths. The first-Read-bias-pollution failure mode that hit PR #44 must NOT recur.

Full skill compliance mandatory (per prework brief's skills firing list):
ave-prereg v1.1 (Step 3.5 dimensional analysis); ave-canonical-leaf-pull v1.3 (Trigger 17 vocabulary-broadened-grep); ave-analytical-tool-selection; ave-discipline-translate v1.1 Trigger 6; substrate-native-check; consistency-vs-emergence v1.2; phase-space-coordinate-check; ave-evidence-framing-discipline; ave-canonical-source; ave-walk-back v1.1; verify-before-cite v1.4; ave-discrimination-check.

Open canonical-identification question (surface in prereg BEFORE deriving):
operators.md:57 has two Op21 identifications — $Q \sim 1/\ln(Z_1/Z_0)$ (Bardeen BCS, Vol 1 Ch 6 §1.21) and $Q = \ell$ (lattice pitch in natural units, theorem-3-1 §Op21 multi-mode form). Reconcile: same mechanism / distinct mechanisms / specialization relationship? Surface to Grant adjudication in prereg if implementor cannot resolve from canonical content.

Expected deliverables (per prework brief):
1. Prereg at `research/<date>_clm-0ktpcn-phase-3-A4-op21-formalization-prereg.md`
2. Result doc at `research/<date>_clm-0ktpcn-phase-3-A4-op21-formalization-result.md` — end-to-end derivation + Class 2/4 classification with master-equation-derivation-path tracing
3. New canonical leaf at `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md` (recommended location) OR extension of `theorem-3-1-q-factor.md` (alternate location; smaller scope)
4. Update `manuscript/ave-kb/vol1/claim-quality.md` clm-0ktpcn entry: confidence 0.60 → 0.65 if PASS; close the "Op21 multi-mode generalization formalization" strengthen-by item; preserve δ_strain (Phase 3-A3) + T = A_4 (Phase 3-A5 speculative) items
5. `make refresh-kb-metadata` + `make verify-kb-metadata` PASS pre-push (cascade through 21+ dependents)
6. Commit messages following project pattern + Co-Authored-By footer

Adjudication criteria: per prework brief; PASS / PARTIAL / WALK-BACK.
Honest closure probability: ~60% PASS / ~25% PARTIAL / ~15% WALK-BACK.

Report back: outcome + commit SHAs + branch confirmation pushed + self-audit verdict + verify pipeline PASS + cross-agent pollution check + open Grant adjudication questions (particularly the Op21 dual-identification reconciliation).

Begin with prework brief read → vocabulary-broadened pre-survey (extending what prework already established) → Step 3.5 dimensional analysis (extending what prework pre-froze) → prereg → derivation.
```

## Post-spawn handoff

When Phase 3-A4 implementor returns, future-orchestration-session opens PR, spawns ave-auditor, runs `make verify` pipeline check via temp worktree if needed (per PR #41 + PR #43 pattern), merges PR, post-merge tasks if any cascade-leverage amplification surfaces from Benn's added KB entries (per spot-check (3) above).

Phase 3-A4 closure unlocks Phase 3-A3 (δ_strain magnitude derivation) as next clm-0ktpcn lift lever, OR Phase 2-LLCP if substrate-critical-point regime work is the next physics priority. Remaining queue per session handoff.

## Why this prework was done in advance

Per Grant 2026-05-27 EOD directive ("Let's review our next steps and handoffs and apply any prework research/skills etc. then when the PR merges we will kick off the next steps"). The Phase 3-A4 spawn becomes mechanical post-PR-#45-merge: spot-check + adjudicate Op21 dual-identification question (if you want to pre-resolve) + spawn with the implementor brief above. The substantive prework — vocabulary-broadened grep + dimensional analysis at canonical primitives + Op21 dual-identification surfacing + cross-reference infrastructure mapping + cascade dependency check — is captured here so the implementor session can focus on the substrate-mechanical derivation rather than on rediscovering the canonical context.
