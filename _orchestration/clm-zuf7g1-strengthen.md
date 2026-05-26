# Epic: clm-zuf7g1 Phase-Locked Topological Thread + Bell + Born-Rule Strengthening

**Status**: **PHASE 2-A COMPLETE** (master-equation-derivation-path of Born-rule click-probability scaling closed end-to-end via 5-session arc; workstream returns to clm-zuf7g1-strengthen Phase 1+2 closed; remaining work = Phase 3+ on the lossless-LC-resonator strengthen-by item is the next solidity-lift lever, separate workstream)
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
| **3a** | **Derive lossless-LC-resonator structural identification — Z₀ ≈ 377 Ω from substrate impedance, Q = ∞ from topological dissipationless invariant** (item 2 of strengthen-by; sub-step a — Z₀ derivation) | **PRE-REG DRAFTED — implementor brief ready** (see Phase 3a section below) |
| 3b | Derive Q = ∞ topological dissipationless invariant for phase-locked thread | OPEN — likely follows 3a closure |
| 3c | Re-integrate Z₀ + Q derivations into `phase-locked-topological-thread.md` + clm-zuf7g1 KB anchor; bump confidence 0.65 → 0.70 if closure clean | OPEN — KB integration sub-phase |
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
- Ax 1 (TLM lattice impedance): bond impedance Z_bond defined by node-capacitance / inductance ratio
- Ax 2 (ν_vac = 2/7 lattice-DOF ratio): geometric prefactor in the bond → continuum impedance map
- Continuum limit yields Z₀ = √(μ₀/ε₀) as the IMPEDANCE eigenvalue of the K4-TLM substrate in transverse propagation
- The phase-locked thread (chiral labyrinth on the unknot, per `phase-locked-topological-thread.md`) is a topologically-trapped MODE on this substrate; its characteristic impedance MATCHES Z₀ by lattice-continuity (the thread is a bound state of the same substrate that propagates Z₀ transverse waves)

If this is the right chain, the derivation is ~Class 2 emergence (the topological-thread mode's Z = Z₀ ≈ 377 Ω because it's the substrate-impedance of the lattice it lives on) — NOT Class 4 consistency (which would be: "we computed Z and got 377 Ω, matches Maxwell").

### Pre-survey — what already exists in corpus

Pre-implementor corpus-grep targets (mandatory before deriving):

```bash
grep -rn "Z_0\|Z₀\|377.*Ohm\|sqrt.*mu_0.*epsilon_0\|impedance.*vacuum\|substrate impedance" \
  manuscript/ave-kb/vol1/ manuscript/ave-kb/vol4/ src/ave/core/
grep -rn "phase-locked.*resonator\|lossless.*LC\|short-short LC" manuscript/ave-kb/
grep -rn "characteristic impedance" manuscript/ave-kb/ research/
```

Likely already-canonical anchors:
- `manuscript/ave-kb/vol1/axiom-1-impedance.md` (if exists; check) — TLM bond impedance
- `manuscript/ave-kb/vol4/circuit-theory/` — vacuum circuit analysis chapters
- `manuscript/ave-kb/common/translation-tables/translation-circuit.md` — EE-side translation of Z₀
- `src/ave/core/constants.py` — Z₀ definitely canonical here (search for `Z_0` / `Z_vac`)
- `manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md` — current home of the constructive identification

If the chain Ax1+Ax2 → continuum-impedance → topologically-bound-mode-of-substrate already exists end-to-end, Phase 3a is a leaf-wire (analogous to Phase 1's clm-zuf7g1 → clm-salw2h chain-promotion). If gaps exist (most likely: the "bound topological mode inherits substrate impedance by lattice-continuity" step), Phase 3a derives that step.

### What would discriminate (per ave-discrimination-check)

For Phase 3a to land as a genuine derivation (not a translation-table identification):

1. **The derivation must NOT bottom out at "Z₀ = √(μ₀/ε₀) by definition of Z₀"** — that's circular; Z₀'s canonical definition IS √(μ₀/ε₀). The derivation must produce 377 Ω from the substrate's K4-TLM lattice parameters (capacitance per node, inductance per bond, lattice spacing) which independently fix Z₀.
2. **The topological-thread mode's Z must come from SUBSTRATE structure**, not from a separate impedance-matching argument. I.e., the thread is on the same substrate that supports Z₀ transverse waves; its mode-impedance is Z₀ by lattice-eigenvalue, not by a tuned coupling.
3. **The classification under consistency-vs-emergence must be Class 2** (substrate-mechanism emergence) — explicit derivation-path tracing required per the v1.2 discipline upgrade. If the derivation reduces to "Maxwell gives 377 Ω and AVE matches Maxwell at continuum limit," reclassify as Class 4 consistency and lower the expected solidity-lift accordingly.

### Adjudication criteria (PASS / WALK-BACK / RESCOPE)

- **PASS**: Z₀ derivation is Class 2 substrate-emergence end-to-end, no circularity, KB integration clean. Solidity-lift target: clm-zuf7g1 0.65 → 0.70.
- **WALK-BACK**: derivation bottoms out in Class 4 consistency; document honestly, no solidity lift, refine Phase 3 scope (Q-LCR-1: is Z₀ derivable as substrate-emergence, or is it definitionally fixed by μ₀/ε₀ canonical-source link?).
- **RESCOPE**: gap is in step "topological-thread mode inherits substrate Z by lattice-continuity" rather than in Z₀ itself. Spin out as separate Phase 3a-mode workstream; Z₀-from-Ax1+Ax2 lands as a leaf-completion.

### Skills expected to fire (implementor checklist)

- `ave-prereg` — corpus-grep as above
- `ave-canonical-leaf-pull` — pull Z₀ leaves + phase-locked-thread leaf + any circuit-theory chapter
- `ave-canonical-source` — Z₀ canonical home in `src/ave/core/constants.py`; never hard-code 377
- `ave-analytical-tool-selection` — impedance / boundary problem class; check `ave-analytical-toolkit-index.md` for Op-level tools (likely Op4 boundary-impedance + Op17 mode-matching)
- `ave-discipline-translate` — check `translation-circuit.md` row for Z₀; confirm AVE-native form (not borrowed EE)
- `substrate-native-check` — K4-TLM lattice structure walk before deriving
- `consistency-vs-emergence` v1.2 — explicit Class-2 vs Class-4 classification with master-equation-derivation-path tracing
- `phase-space-coordinate-check` — Z₀ lives in impedance-plane (V/I phasor); topological thread lives in real-space lattice; need to keep coordinates clean
- `ave-evidence-framing-discipline` — "derives" vs "identifies" vs "consistent-with" precision in result framing
- `ave-discrimination-check` — discriminate Class 2 emergence from Class 4 consistency BEFORE asserting solidity lift

### Branch + spawn protocol

- **Branch**: `analysis/clm-zuf7g1-phase-3a-Z0-derivation` off `main` @ post-PR-38-merge
- **Spawn**: orchestration session uses `Agent` tool with `isolation: "worktree"` so the implementor sub-agent works in a temporary worktree (separate working dir, same `.git`) — prevents working-tree branch leak (per CLAUDE.md "Pre-commit discipline" section)
- **Sub-agent type**: `ave-implementer` (full discipline: prereg + driver + result doc + auditor + skills compliance check)
- **Sequencing**: parallel-safe with other Phase 3+ epic spawns (clm-0ktpcn + nanoscale-CLT). No depends-on conflicts between these workstreams.

### Honest closure probability

~60% probability of clean Class-2 closure. Risk: the Z₀ derivation reduces to Maxwell-matching at continuum limit (Class 4 consistency), in which case the leaf-completion still happens but no solidity bump. Walk-back path is clean (Type B demotion, no cascade impact).

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
