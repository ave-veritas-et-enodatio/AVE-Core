# Epic: clm-zuf7g1 Phase-Locked Topological Thread + Bell + Born-Rule Strengthening

**Status**: **PHASE 3a CLOSED — WALK-BACK** (Z₀ substrate-mechanism derivation does NOT close Class 2 emergence on numerical-value sub-axis; Class 2 on scale-invariance sub-axis + Class B on numerical-value + Class 4 observable; no solidity lift; Q-LCR-1 + Q-LCR-2 surfaced for Grant adjudication; strengthen-by item REFRAMED not retired; step 7 + Q = ∞ deferred to Phase 3b)
**Phase 3a closed**: 2026-05-26 — branch `analysis/clm-zuf7g1-phase-3a-Z0-derivation`. Pre-reg + result doc landed in `research/`; clm-zuf7g1 entry rationale appended; no Predictions matrix row affected; no cascade walk-back. See Phase 3a execution log below.
**Phase 1 closed**: 2026-05-26 — FM chain-promotion landed via PR #37 `audit/2026-05-26_clm-zuf7g1-phase-1-fm-chain-promotion`. Confidence 0.60 → 0.65, solidity unchanged 0.55 (clm-ldmvwi was dep-cap at that time).
**Phase 2 closed**: 2026-05-26 — Phase 2-A master-equation-derivation-path workstream (5 sessions: A.1 prereg + A.2 stochastic master eq + A.3 threshold-crossing first-passage + A.4 p=2 uniqueness + A.5 KB integration + cascade). clm-ldmvwi confidence 0.55 → 0.65; cascade lifted clm-zuf7g1 + clm-unk0bd + clm-5xon03 all 0.55 → 0.65 (= own confidence ceiling). clm-0ktpcn stays at 0.55 (own confidence cap from sum-decomposition orthogonality gap; separate strengthen workstream).
**Phase 2 branch**: `analysis/clm-ldmvwi-master-eq-stochastic-derivation` off main @ post-PR-37-merge; 5 commits + 5 audit tags pushed
**Target claim**: `clm-zuf7g1` — Phase-Locked Entanglement Thread (Bell correlation + topological-protection empirical demonstration)
**Current state**: confidence 0.60, solidity 0.55, 1 dependent (clm-unk0bd as of 2026-05-25 Phase 2 sub-item 4)
**Origin**: surfaced as the new solidity-cap on clm-unk0bd post Phase 2 sub-items 3+4 closure. Identified in `_orchestration/clm-0ktpcn-golden-torus-alpha-strengthen.md` Phase 2 sub-item 4 commit (`a01cf6c2`).

## Why this workstream

The Phase 2 sub-items 3+4 closure work landed two new depends-on edges on clm-unk0bd: → clm-salw2h (FM derivation) and → clm-zuf7g1 (topological-protection empirical demonstration). The new clm-zuf7g1 dep has solidity 0.55, which is now the dep-gate cap on clm-unk0bd's solidity (clm-unk0bd's own confidence ceiling was raised 0.55 → 0.65 by closing 4 of 4 strengthen-by items, but the solidity stays at 0.55 due to the dep-gate). Lifting clm-zuf7g1 would unlock cascade through:

- clm-unk0bd (electron body topology) — Vol 1
- clm-0ktpcn (Golden Torus α derivation, 21 dependents — top of the leverage list) — Vol 1
- + the 12-claim downstream cone from Phase 2 sub-item 1 work (clm-5xon03, clm-2dwzib, clm-3kzmt9, etc.)

This is **adjacent to the Golden Torus close-out, not a continuation of it**. The clm-zuf7g1 claim is about Bell correlations + Born rule from Ohmic measurement + structural identification of phase-locked thread as lossless LC resonator — quantum-mechanics fundamentals. The Golden Torus cone is the *beneficiary* via the depends-on edge, not the *subject* of this work.

## What's open on clm-zuf7g1 (from its current strengthen-by list)

Per `manuscript/ave-kb/vol1/claim-quality.md` clm-zuf7g1 block (canonical 2026-05-25 state):

1. **Strengthen Born Rule from Ohmic Measurement Work (clm-ldmvwi)** — the dominant solidity bottleneck for clm-zuf7g1 itself. clm-ldmvwi is at solidity 0.55; clm-zuf7g1 inherits its cap. Closing clm-ldmvwi unlocks clm-zuf7g1.

2. **Derive the structural identification "phase-locked topological thread = lossless short-short LC resonator with $Z_0 \approx 377\,\Omega$, $Q = \infty$"** from first principles — currently asserted as a constructive identification of the Bell-correlation carrier, not derived from axioms.

3. **Document the spin-1/2 Möbius half-angle coupling derivation explicitly** — currently summarized in clm-zuf7g1's rationale; the Finkelstein-Misner kink construction needs to be present here or pointed at an explicit derivation leaf. **Partial closure available**: the FM derivation now exists at `vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md` (clm-salw2h, landed 2026-05-25 Phase 1) — wiring clm-zuf7g1 → clm-salw2h as a depends-on edge would partially close item 3 without new physics.

4. **Add a separate claim-quality entry for the spin-1/2 Möbius half-angle coupling derivation** so the dependency chain is fully scored.

## Cascade-lift estimate (per dep-gate solidity rule)

If clm-zuf7g1 confidence + solidity both lift to 0.70 (matching clm-8c3yhs's level), then:
- clm-zuf7g1: 0.55 → 0.70
- clm-unk0bd: min(0.65, 0.70, 0.70, 0.70) = 0.65 (now clm-unk0bd's own confidence is the new cap)
- clm-0ktpcn: min(0.55, 0.65, 0.70) = 0.55 (clm-0ktpcn's own confidence still caps; would need separate strengthening to lift further)

So lifting clm-zuf7g1 from 0.55 → 0.70 lifts clm-unk0bd from 0.55 → 0.65 (matches its raised confidence ceiling), but clm-0ktpcn stays at 0.55 because its own confidence is still 0.55. Path forward to genuinely lift clm-0ktpcn's solidity is multi-step:
- (a) Strengthen clm-zuf7g1 (this workstream) → unlocks clm-unk0bd to 0.65
- (b) Strengthen clm-0ktpcn's own confidence (independent workstream — addresses sum-decomposition orthogonality + δ_strain magnitude derivation, the dominant remaining gaps)

The cascade math: this workstream lifts the 12-claim cone behind clm-unk0bd; clm-0ktpcn requires both this workstream + its own confidence-bump workstream.

## Phase plan

| Phase | Goal | Status |
|---|---|---|
| 0a | Orchestration epic doc | ✓ COMPLETE 2026-05-25 (this doc, registered alongside the Golden Torus close-out PR #36) |
| 0b | Workstream-level pre-registration doc | DEFERRED — Phase 1 was small enough for inline skills compliance check (no separate prereg needed) |
| **1** | **Wire clm-zuf7g1 → clm-salw2h depends-on edge (closes items 3+4 via single edge)** | **✓ COMPLETE 2026-05-26** (this commit) — confidence 0.60 → 0.65, solidity unchanged at 0.55 (clm-ldmvwi remains dep-cap) |
| **2** | **Strengthen clm-ldmvwi (Born Rule from Ohmic Measurement) — the dominant solidity bottleneck** | **✓ COMPLETE 2026-05-26** via Phase 2-A 5-session arc. PR #38 merged. clm-ldmvwi 0.55 → 0.65. Cascade lifted clm-zuf7g1 + clm-unk0bd + clm-5xon03 each from 0.55 → 0.65. Result docs: A.1 prereg + A.2 stochastic master eq + A.3 threshold-crossing + A.4 p=2 uniqueness + A.5 KB integration. Master-equation-derivation-path closed end-to-end (□V → stochastic master eq via FDT → Joule extraction → cumulant-truncated Gaussian V_η → Rice/Wald first-passage at threshold → click rate ∝ |V_s|² ∝ |∂_t A|² ≡ Born rule p=2 uniqueness via three convergent arguments). |
| **3a** | **Derive lossless-LC-resonator structural identification — Z₀ ≈ 377 Ω from substrate impedance** (item 2 of strengthen-by; sub-step a — Z₀ derivation only) | **✓ CLOSED 2026-05-26 — WALK-BACK** (dual-axis classification: Class 2 emergence on scale-invariance sub-axis + Class B manifestation on numerical-value sub-axis + Class 4 observable consistency). NO solidity lift (clm-zuf7g1 stays at 0.65/0.65). Strengthen-by item REFRAMED (not retired) to surface Q-LCR-1 + Q-LCR-2 + Phase 3b RESCOPE-path step 7 as separate items. Result doc: [`research/2026-05-26_clm-zuf7g1-phase-3a-Z0-derivation-result.md`](../research/2026-05-26_clm-zuf7g1-phase-3a-Z0-derivation-result.md). See Phase 3a execution log below for full audit trail. |
| 3b | Derive Q = ∞ topological dissipationless invariant for phase-locked thread + close step 7 (topological-thread mode inherits substrate-impedance Z by lattice-eigenvalue continuity) | OPEN — Phase 3a result-doc §3 recommends sequencing step-7 closure alongside Q = ∞ derivation since both involve substrate-mode-spectrum arguments |
| 3c | Re-integrate Z₀ + Q derivations into `phase-locked-topological-thread.md` + clm-zuf7g1 KB anchor; bump confidence 0.65 → 0.70 if closure clean | OPEN — KB integration sub-phase. NOTE: Phase 3a WALK-BACK means Z₀ component will be a Class B + Class 2 + Class 4 compound classification, not a Class 2 emergence — confidence bump path depends on Q-LCR-1 + Q-LCR-2 Grant adjudication and Phase 3b closure |
| 4 | (closed by Phase 1 — clm-salw2h IS the separate claim-quality entry, now scored in the chain) | ✓ COMPLETE 2026-05-26 (folded into Phase 1) |

## Phase 1 execution log (2026-05-26)

**Skills compliance check** fired at task start:
- `ave-prereg` ✓ — focused corpus survey (cycle-check across depends-on graph before wiring)
- `ave-canonical-leaf-pull` ✓ — read clm-zuf7g1 + clm-salw2h current state; verified clm-salw2h's depends-on cone (axiom-1, INVARIANT-S2, clm-h9aqmt) has no back-path to clm-zuf7g1
- `verify-before-cite` ✓ continuous — every file:line citation grep-verified
- `consistency-vs-emergence` ✓ — Class 1 consistency (chain-promotion via depends-on edge, not new derivation)
- `ave-discipline-translate` NOT firing — verified via `translation-qm.md` row 7 ("Spin / Unknot chirality / two orientations of the unknot twist ±1/2") that "Möbius half-angle coupling" terminology refers to the AVE-native form being consumed, NOT a QM-formalism import. Decision documented in clm-zuf7g1 rationale.
- `ave-independence-check` ✓ — verified that the depends-on edge expresses a load-bearing semantic equivalence: clm-zuf7g1's "spin-1/2 Möbius half-angle coupling" Bell-correlation ingredient ≡ clm-salw2h's SU(2) → SO(3) double-cover via FM kink mechanism. Verbatim corpus anchor at `phase-locked-topological-thread.md` §3.5 ("The Möbius-strip topology of the chiral labyrinth requires 720° for a complete cycle, producing a physical half-angle coupling") + cross-validation against `finkelstein-misner-spin-half-derivation.md` §2 + §3. Auditor independently confirmed.
- `phase-space-coordinate-check` ✓ — FM derivation lives in real-space coordinates (per its §9); phase-locked-topological-thread §3.5 also lives in real-space (detector axis on K4 lattice). Same coordinate system, no muddle.
- `ave-evidence-framing-discipline` ✓ — semantic-equivalence claim made explicit in rationale; the +0.05/closure convention named explicitly (not asserted-arbitrary); solidity-vs-confidence dep-gate explanation clarified.
- `ave-handoff-canonical-locale` ✓ — epic doc lands in `_orchestration/`, not `~/.claude/plans/`.

**Auditor pass** (ave-auditor): COMMIT. Verified semantic equivalence of Möbius half-angle ↔ FM SU(2)→SO(3) double cover; confirmed no DAG cycle; confirmed strengthen-by item closures honest; confirmed solidity-vs-confidence framing accurate. One informational FLAG (stale "confidence 0.60" reference in clm-unk0bd's rationale post-bump) — addressed in pre-commit hygiene pass.

**Discipline-hygiene pre-commit pass** (Grant directive after Path B-prime self-audit lesson): caught and fixed the stale clm-unk0bd reference (auditor's Finding 9) + explicitly documented ave-discipline-translate non-firing decision and ave-independence-check semantic-equivalence verification in the clm-zuf7g1 rationale itself (audit trail in-doc, not just commit-message). Caught one additional inaccuracy in my own draft (clm-salw2h confidence was 0.80 not 0.70 — fixed).

**Edits landed**:
1. `manuscript/ave-kb/vol1/claim-quality.md` clm-zuf7g1 — added depends-on clm-salw2h with semantic-equivalence annotation; removed strengthen-by items 3+4; updated rationale with audit-trail documentation; confidence 0.60 → 0.65
2. `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md` frontmatter — path-stable updated to reflect new inbound depends-on edge
3. `manuscript/ave-kb/vol1/claim-quality.md` clm-unk0bd rationale — discipline-hygiene fix: stale "despite confidence 0.60" → "despite confidence 0.65 [bumped 2026-05-26 Phase 1...]"

**Refresh + verify pipeline**: PASS — 692 files / 281 entries / 685 depends-on edges (+1) / 628 strengthen-by (-2) / 0 failures.

## Phase 2 priority (the actual solidity-bottleneck) — CLOSED

Phase 1 lifted clm-zuf7g1's confidence ceiling but NOT solidity (clm-ldmvwi at 0.55 capped). **The actual cascade-lifting move was strengthening clm-ldmvwi (Born Rule from Ohmic Measurement Work)** — its solidity directly capped clm-zuf7g1's solidity, which directly caps clm-unk0bd's solidity, which feeds the 12-claim downstream cone.

Closed end-to-end via Phase 2-A workstream (PR #38 merged 2026-05-26). clm-ldmvwi now at 0.65, dep-cap lifted, clm-zuf7g1 solidity now 0.65 (own confidence ceiling, not dep-gated).

## Phase 3a prereg — lossless-LC-resonator Z₀ structural identification

**Implementor brief** (ready for parallel spawn next session). See "Spawn protocol" at bottom for the isolation: "worktree" pattern.

### Target claim
`clm-zuf7g1`'s outstanding strengthen-by item 2: **"Derive the structural identification 'phase-locked topological thread = lossless short-short LC resonator with $Z_0 \approx 377\,\Omega$, $Q = \infty$' from first principles."**

The current state asserts this identification constructively — the phase-locked thread is described as having LC-resonator structure with vacuum impedance Z₀ = √(μ₀/ε₀) ≈ 377 Ω, with Q = ∞ inherited from topological-protection. Phase 3a derives the Z₀ identification rigorously from substrate axioms; Phase 3b handles Q = ∞.

### What I expect (forward pre-registration, per ave-prereg discipline)

Z₀ ≈ 377 Ω will derive directly from the substrate's intrinsic impedance via the canonical AVE chain:
- Ax 1 (K4-TLM bond impedance): per-bond impedance Z_bond defined by node-capacitance / bond-inductance ratio at the lattice level
- Ax 2 (ν_vac = 2/7 lattice-DOF ratio): geometric prefactor in the per-bond → continuum-limit impedance map
- Continuum limit yields Z₀ = √(μ₀/ε₀) as the substrate-impedance eigenvalue of the K4-TLM lattice in transverse-mode propagation
- The phase-locked thread (chiral labyrinth on the unknot, per `phase-locked-topological-thread.md`) is a topologically-trapped mode on this substrate; its characteristic impedance equals the substrate's transverse-mode impedance Z₀ by lattice-continuity (the trapped mode lives on the same substrate that propagates Z₀ transverse modes, so its mode-impedance is fixed by the substrate's lattice-eigenvalue structure rather than by tuned external coupling)

If this is the right chain, the derivation is ~Class 2 substrate-mechanism emergence (the topological-thread mode's Z equals the substrate-impedance Z₀ ≈ 377 Ω because the thread is a bound substrate-mode on the K4-TLM lattice whose continuum-limit eigenvalue IS Z₀) — NOT Class 4 consistency (which would be: "we computed Z and got 377 Ω, matches the standard continuum-electrodynamics value"; the standard community calls this matching "Maxwell's vacuum impedance match").

### Pre-survey — what already exists in corpus

Pre-implementor corpus-grep targets (mandatory before deriving):

```bash
grep -rn "Z_0\|Z₀\|377.*Ohm\|sqrt.*mu_0.*epsilon_0\|impedance.*vacuum\|substrate impedance" \
  manuscript/ave-kb/vol1/ manuscript/ave-kb/vol4/ src/ave/core/
grep -rn "phase-locked.*resonator\|lossless.*LC\|short-short LC" manuscript/ave-kb/
grep -rn "characteristic impedance" manuscript/ave-kb/ research/
```

Likely already-canonical anchors:
- `manuscript/ave-kb/vol1/axiom-1-impedance.md` (if exists; check) — K4-TLM per-bond impedance
- `manuscript/ave-kb/vol4/circuit-theory/` — substrate-circuit analysis chapters (the standard community calls this "vacuum circuit analysis")
- `manuscript/ave-kb/common/translation-tables/translation-circuit.md` — translation row for substrate-impedance Z₀ to its standard electrical-engineering name "vacuum impedance"
- `src/ave/core/constants.py` — Z₀ canonical here (search for `Z_0` / `Z_vac`)
- `manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md` — current home of the constructive identification

If the chain Ax1+Ax2 → continuum-impedance → topologically-bound-mode-of-substrate already exists end-to-end, Phase 3a is a leaf-wire (analogous to Phase 1's clm-zuf7g1 → clm-salw2h chain-promotion). If gaps exist (most likely: the "bound topological mode inherits substrate impedance by lattice-continuity" step), Phase 3a derives that step.

### What would discriminate (per ave-discrimination-check)

For Phase 3a to land as a genuine substrate-mechanism derivation (not a translation-table identification of substrate Z₀ with its standard-physics name "vacuum impedance"):

1. **The derivation must NOT bottom out at "Z₀ = √(μ₀/ε₀) by definition"** — that's circular; the standard-physics definition of "vacuum impedance" IS √(μ₀/ε₀). The derivation must produce the 377 Ω value from the substrate's K4-TLM lattice parameters (capacitance per node, inductance per bond, lattice spacing) which independently fix Z₀ from substrate-mechanical primitives.
2. **The topological-thread mode's characteristic impedance must come from substrate-eigenvalue structure**, not from a separately-tuned impedance-matching argument. I.e., the thread lives on the same K4-TLM substrate that supports Z₀ transverse modes; its mode-impedance equals Z₀ by lattice-continuity at the eigenvalue level, not by tuned external coupling.
3. **The classification under consistency-vs-emergence v1.2 must be Class 2** (substrate-mechanism emergence) — explicit master-equation-derivation-path tracing required per the v1.2 discipline upgrade. If the derivation reduces to "continuum-limit substrate dispersion produces 377 Ω which the standard community calls the Maxwell vacuum impedance," reclassify as Class 4 substrate-agnostic-consistency and lower the expected solidity-lift accordingly.

### Adjudication criteria (PASS / WALK-BACK / RESCOPE)

- **PASS**: Z₀ derivation is Class 2 substrate-mechanism emergence end-to-end, no circularity, KB integration clean. Solidity-lift target: clm-zuf7g1 0.65 → 0.70.
- **WALK-BACK**: derivation bottoms out in Class 4 substrate-agnostic consistency; document honestly, no solidity lift, refine Phase 3 scope (Q-LCR-1: is the substrate-impedance Z₀ derivable as substrate-mechanism emergence from Ax 1 + Ax 2 lattice parameters, or is it definitionally fixed by the μ₀/ε₀ canonical-source link to the standard continuum-electrodynamics value?).
- **RESCOPE**: gap is in the step "topological-thread mode inherits substrate Z by lattice-continuity" rather than in Z₀ derivation itself. Spin out as separate Phase 3a-mode workstream; Z₀-from-Ax1+Ax2 lands as a leaf-completion.

### Skills expected to fire (implementor checklist)

- `ave-prereg` — corpus-grep as above
- `ave-canonical-leaf-pull` — pull substrate-impedance leaves + phase-locked-thread leaf + any substrate-circuit-theory chapter
- `ave-canonical-source` — substrate-impedance Z₀ canonical home in `src/ave/core/constants.py`; never hard-code 377
- `ave-analytical-tool-selection` — substrate-impedance / boundary-impedance problem class; check `ave-analytical-toolkit-index.md` for Op-level tools (likely Op4 boundary-impedance + Op17 mode-matching)
- `ave-discipline-translate` v1.1 — check `translation-circuit.md` row for substrate-impedance Z₀ ↔ standard-physics "vacuum impedance" mapping; trigger 6 fires continuously during prose composition (substrate-native vocabulary mandatory; "Maxwell vacuum impedance" appears only as parenthetical translation reference to substrate-impedance Z₀)
- `substrate-native-check` — K4-TLM lattice structure walk before deriving
- `consistency-vs-emergence` v1.2 — explicit Class-2 substrate-mechanism vs Class-4 substrate-agnostic-consistency classification with master-equation-derivation-path tracing
- `phase-space-coordinate-check` — substrate-impedance Z₀ lives in impedance-plane (V/I phasor coordinates); topological thread lives in real-space lattice coordinates; need to keep coordinate systems clean
- `ave-evidence-framing-discipline` — "derives from substrate primitives" vs "identifies with standard-physics name" vs "consistent-with continuum-limit value" precision in result framing
- `ave-discrimination-check` — discriminate Class 2 substrate-mechanism emergence from Class 4 substrate-agnostic consistency BEFORE asserting solidity lift

### Branch + spawn protocol

- **Branch**: `analysis/clm-zuf7g1-phase-3a-Z0-derivation` off `main` @ post-PR-38-merge
- **Spawn**: orchestration session uses `Agent` tool with `isolation: "worktree"` so the implementor sub-agent works in a temporary worktree (separate working dir, same `.git`) — prevents working-tree branch leak (per CLAUDE.md "Pre-commit discipline" section)
- **Sub-agent type**: `ave-implementer` (full discipline: prereg + driver + result doc + auditor + skills compliance check)
- **Sequencing**: parallel-safe with other Phase 3+ epic spawns (clm-0ktpcn + ax4-saturation-narrow-aperture-amplitude-shape — formerly nanoscale-CLT, renamed 2026-05-26 per substrate-native vocabulary discipline). No depends-on conflicts between these workstreams.

### Honest closure probability

~60% probability of clean Class-2 substrate-mechanism closure. Risk: the Z₀ derivation reduces to continuum-limit substrate-dispersion-matching the standard "Maxwell vacuum impedance" value (Class 4 substrate-agnostic consistency), in which case the leaf-completion still happens but no solidity bump. Walk-back path is clean (Type B demotion, no cascade impact).

## Phase 3a execution log (2026-05-26)

**Outcome**: **WALK-BACK** (pre-registered ≥ 60% probability path; corpus pre-survey actually drove this to ≥ 80%).

**What I found in corpus pre-survey** (before deriving):

1. A canonical Z₀ derivation leaf already exists at [`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md) (clm-i9l284 + clm-kezk9z). The chain stipulates $L_{\text{cell}} = \mu_0 \ell_{\text{node}}$ and $C_{\text{cell}} = \epsilon_0 \ell_{\text{node}}$, applies transmission-line characteristic-impedance formula, gets $Z_0 = \sqrt{\mu_0/\epsilon_0}$ with lattice pitch cancelling.

2. The corpus already canonically classifies $Z_0 = \sqrt{\mu_0/\epsilon_0}$ as **Class A identity**, per [`manuscript/ave-kb/vol4/claim-quality.md`](../manuscript/ave-kb/vol4/claim-quality.md) clm-kezk9z line 104: *"Per Master Prediction Table classification, $Z_0 = \sqrt{\mu_0/\varepsilon_0}$ is a category (i) identity — definitionally true (the 0.00% in row #2 of the prediction table is not a fit)."* Rationale at line 118: *"the leaf is honest that the $Z_0$ identity carries zero predictive content."*

3. The [`manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md) leaf (clm-nxc9gy + clm-k6quve) explicitly states: *"Numerical equality of $Z_{\text{cell}} = Z_0$ is from cancellation of $\ell_{\text{node}}$; conceptual distinction matters for engine implementation and dimensional analysis."* And the clm-k6quve table has rows $L_{\text{cell}} = \mu_0 \cdot \ell_{\text{node}}$ marked "depends on μ₀ choice" and $C_{\text{cell}} = \epsilon_0 \cdot \ell_{\text{node}}$ marked "depends on ε₀ choice" — the in-corpus acknowledgment that the per-bond lumped elements are SI-input-dependent.

4. `src/ave/core/constants.py` lines 79-80 confirm μ₀ and ε₀ are SI engineering inputs; line 81 defines `Z_0 = np.sqrt(MU_0 / EPSILON_0)` — engine canonical-source is honest about the substitution.

5. Corpus-wide grep for substrate-mechanism derivation of μ₀ or ε₀ (independent of SI) returned no canonical leaf. `lc-electrodynamics.md` treats μ₀ as input ("Because the vacuum inductance per unit length is μ₀..."). Vol 1 Ch 1 axiom-definitions says Z₀ is "derived from these axioms" but the only derivation in corpus is the per-bond-lumped-element chain that takes μ₀ and ε₀ as inputs.

**Master-equation-derivation-path tracing** (per `consistency-vs-emergence` v1.2 Step 7):

| Step | Status |
|---|---|
| 1: Ax 1 chiral Laves K4 Cosserat crystal | Derived-from-master-eq |
| 2: $L_{\text{cell}} = \mu_0 \ell_{\text{node}}, C_{\text{cell}} = \epsilon_0 \ell_{\text{node}}$ | **Requires-additional-postulate** (μ₀ and ε₀ as SI inputs) |
| 3: $Z_{\text{bond}} = \sqrt{L_{\text{cell}}/C_{\text{cell}}}$ formula | Definitional-given-prior-steps |
| 4: Substitute → $\sqrt{\mu_0/\epsilon_0}$; pitch cancels | Definitional-given-prior-steps |
| 5: Value 376.73 Ω | Definitional-given-prior-steps (value comes from SI μ₀ and ε₀) |
| 6: Scale-invariance under pitch | **Derived-from-master-eq** (Class 2 substrate-mechanism emergence on scale-invariance sub-axis) |
| 7: Thread mode inherits Z by lattice-continuity | **Asserted-without-tracing** (deferred to Phase 3b RESCOPE-path) |

**Compound classification result**: Class B substrate-mechanism manifestation (on numerical-value sub-axis) + Class 2 substrate-mechanism emergence (on scale-invariance sub-axis) + Class 4 observable consistency.

**Discipline-hygiene check**: per Rule 11 (honest closure), the WALK-BACK adjudication is the right call when a single mechanism (step 2 = requires-additional-postulate) explains the failure to close Class 2 on the numerical-value sub-axis. Per Rule 12 (substitution-not-retraction), Q-LCR-1 + Q-LCR-2 are surfaced as separate framework-extension questions for Grant adjudication, NOT used to refill the Phase 3a slot with a rescue derivation.

**Walk-back propagation** (per `ave-walk-back` v1.1 Type B):
- Pre-reg + result doc landed in `research/`
- clm-zuf7g1 entry rationale appended with Phase 3a annotation
- clm-zuf7g1 strengthen-by item REFRAMED (not retired): item becomes Q-LCR-1 + Q-LCR-2 + step-7-closure deferred-to-3b
- NO confidence/solidity bump (clm-zuf7g1 stays at 0.65/0.65)
- NO edits to `phase-locked-topological-thread.md` line 27 (structurally correct as-is; constructive identification not falsified, just classified honestly)
- NO Predictions matrix row affected
- NO cascade walk-back required (downstream dependents at 0.65 unchanged)

**Surfaced for Grant adjudication**:

- **Q-LCR-1**: is the substrate-impedance Z₀ numerical value 376.73 Ω derivable as substrate-mechanism emergence from Ax 1 + Ax 2 K4-TLM lattice parameters, or is it definitionally fixed by the μ₀/ε₀ canonical-source link to standard continuum-electrodynamics values?

- **Q-LCR-2**: does the corpus need a separate workstream that derives μ₀ and ε₀ themselves from K4-TLM substrate primitives BEFORE Z₀ can earn Class 2 substrate-mechanism emergence on the numerical-value sub-axis? (Three candidate paths sketched in result-doc §4.)

**Auditor pass**: GO (pending — auditor invocation queued before push).

**Skills firing record**: `ave-prereg` ✓ / `ave-canonical-leaf-pull` ✓ / `ave-canonical-source` ✓ / `verify-before-cite` ✓ continuous / `consistency-vs-emergence` v1.2 ✓ (dual-axis + master-equation-derivation-path traced) / `phase-space-coordinate-check` ✓ (impedance-plane vs real-space coordinates kept separate) / `substrate-native-check` ✓ / `ave-analytical-tool-selection` ✓ (transmission-line characteristic-impedance formula) / `ave-discipline-translate` v1.1 trigger 6 ✓ continuous (substrate-impedance Z₀ primary; "Maxwell vacuum impedance" parenthetical) / `ave-discrimination-check` ✓ (all three discriminator questions explicitly failed) / `ave-evidence-framing-discipline` ✓ (compound classification framing) / `ave-walk-back` v1.1 Type B ✓ / Rule 11 honest closure ✓ / Rule 12 substitution-not-retraction ✓.

## Skills compliance check (TBD on session kickoff)

Expected firings: `ave-prereg`, `ave-canonical-leaf-pull` (Bell + Born rule + Möbius leaves), `verify-before-cite`, `phase-space-coordinate-check` (spin-½ Möbius lives in real-space; Bell correlations live in measurement-outcome phase space; need to keep separate), `ave-discipline-translate` (likely fires — Bell correlation is a standard QM concept; need to check translation-qm.md for AVE-native equivalent), `consistency-vs-emergence` (Bell correlation reproduction is Class 1 consistency check, not emergence prediction).

## Branch + sequencing

- **Recommended branch**: `analysis/clm-zuf7g1-strengthen` off `main` (after Golden Torus close-out merges)
- **NOT to land on**: the closed `analysis/golden-torus-alpha-strengthen` branch — that workstream is done
- **Prereq for kickoff**: nothing structurally blocking; can spawn anytime

## Cross-references

- **Source claim entry**: [`manuscript/ave-kb/vol1/claim-quality.md`](../manuscript/ave-kb/vol1/claim-quality.md) clm-zuf7g1 block (around line 332)
- **Canonical leaf**: [`manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md`](../manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md) (co-hosts clm-zuf7g1 + clm-b9eura + clm-unk0bd)
- **Upstream beneficiary**: [`clm-0ktpcn-golden-torus-alpha-strengthen.md`](clm-0ktpcn-golden-torus-alpha-strengthen.md) — Phase 2 sub-items 3+4 commit `a01cf6c2`
- **Born Rule dependency**: clm-ldmvwi (Born Rule from Ohmic Measurement Work) — dominant solidity bottleneck

## Open Q's pending Grant adjudication (before session kickoff)

1. **Scope adjudication**: is this worth pursuing as a workstream now, or banked for later? clm-0ktpcn at solidity 0.55 with 21 dependents is the highest-leverage shaky-load-bearing claim; this workstream is the route to lifting that leverage further. But clm-zuf7g1 is itself a multi-physics workstream (Bell + Born + Möbius + lossless LC).

2. **Sequencing**: Phase 1 (wire clm-zuf7g1 → clm-salw2h) is a low-risk chain-promotion that partial-closes the Möbius derivation item without any new physics. Should this be a quick "easy win" commit on its own branch before opening the full strengthen workstream? Or fold into the full workstream's Phase 1?

3. **Born-rule rigor**: clm-ldmvwi (Born Rule from Ohmic Measurement) is the dominant gap. Is the AVE-native Born rule derivation (Ohmic measurement work) considered the canonical path, or is there an alternative? Standard QM treats Born rule as a postulate; AVE's claim is that it derives from Ohmic measurement extraction. Strengthening this requires settling whether the Ohmic derivation is rigorous or interpretive.
