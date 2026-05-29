# Phase 3-A3 Prework Brief — δ_strain as 5th Machian-G Class E Projection

**Status**: SPAWN-READY. Branch `analysis/phase-3-a3-delta-strain-machian-projection` off `main @ fb2fa923`.
**Origin**: Grant adjudication 2026-05-28 ("are we just talking Machian G?") reframed Phase 3-A3 from "derive δ_strain from G_vac + equipartition" (SM-leaked canonical language) to substrate-native: **δ_strain is the 5th Class E operating-point projection in the $\{G, H_\infty, \hat{\Omega}_{freeze}, \alpha, \delta_{strain}\}$ cosmic-substrate family tied at $u_0^* \approx 0.187$ omega-freeze cascade**. Closure target: `clm-009nkt` confidence **0.45 → 0.55-0.60 PARTIAL band** if PASS; partial closure of `clm-5xon03` "fitted scalar at $T_{CMB}$" condition; cascade through downstream observables.

This doc is the implementor-spawn-ready brief + Type B walk-back scope for SM-leaked canonical-content language cleanup. Bundled with Phase 3-A4-rev scoping in one PR per Grant 2026-05-28 directive.

## Substrate-physics derivation path (substrate-native Machian-G framing)

Per Ax 1 + Ax 4 + INVARIANT-S2 SYM scaling + omega-freeze-cosmic-grain-cascade.md canonical:

1. **Cosmic-genesis substrate operating-point** $u_0^* \approx 0.187$ (omega-freeze cascade canonical at `manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md:13-16`) — ties $\{G, H_\infty, \hat{\Omega}_{freeze}, \alpha\}$ at cosmic genesis
2. **Substrate operating-point mapping** $u_0^* \to A_0^{cosmic}/A_{yield}$ — substrate-thermodynamic identification (**OPEN derivation step**; Phase 3-A3's load-bearing substrate-physics work)
3. **Ax 4 saturation-kernel response** $S(A_0^{cosmic}) = \sqrt{1 - (A_0^{cosmic}/A_{yield})^2}$ at the substrate operating-point
4. **INVARIANT-S2 SYM scaling** (per CLAUDE.md Ax 4 canonical): $\varepsilon_{eff} = \varepsilon_0 S$, $\mu_{eff} = \mu_0 S$, $c_{eff} = c_0\sqrt{S}$
5. **$\alpha$ modulation via INVARIANT-S2**: $\alpha = e^2/(4\pi\varepsilon_0\hbar c) \Rightarrow \alpha_{eff}/\alpha_{cold} = 1/S^{3/2}$
6. **δ_strain identification**: $\delta_{strain} \equiv -\delta\alpha^{-1}/\alpha^{-1} = \frac{3}{2}(1-S)$ at $S \approx 1$

The substrate "knows about $T_{CMB}$" via cosmic-expansion-history co-evolution of substrate operating-point + temperature, NOT via direct thermal-equipartition coupling. The naive estimate ($u_{thermal}/G_{vac} \sim 5.5 \times 10^{-9}$) is the wrong mechanism — δ_strain is cosmic-genesis-residual loading carried by the substrate today, not thermal-strain from current CMB photons.

## Step 3.5 dim-analysis at canonical primitives (pre-frozen per ave-prereg v1.1)

From canonical target $\delta_{strain} \approx 2.225 \times 10^{-6}$ + INVARIANT-S2 SYM scaling:

- $S(A_0^{cosmic}) \approx 1 - \frac{2}{3}\delta_{strain} = 1 - 1.483 \times 10^{-6}$
- $(A_0^{cosmic}/A_{yield})^2 = 1 - S^2 \approx 2 \cdot 1.483 \times 10^{-6} = 2.967 \times 10^{-6}$
- $A_0^{cosmic}/A_{yield} \approx 1.722 \times 10^{-3}$ — **substrate sits at ~0.17% of yield amplitude, deeply linear regime**

The open substrate-physics derivation is the mapping $u_0^* \approx 0.187 \to A_0^{cosmic}/A_{yield} \approx 1.72 \times 10^{-3}$. The factor ~108× between them needs a substrate-thermodynamic interpretation:

- Candidate (P1): $u_0^*$ as cosmic-genesis dimensionless coordinate; mapping involves cosmic-expansion-ratio conversion
- Candidate (P2): $u_0^*$ and $A_0^{cosmic}/A_{yield}$ are at different substrate-physical scales; bridge via the canonical $R_H/\ell_{node} \sim 10^{39}$ Machian-holographic bridge
- Candidate (P3): $u_0^*$ corresponds to cosmic-genesis operating-amplitude; today's $A_0^{cosmic}/A_{yield}$ is the result of cosmic-expansion-dilution; the factor encodes how-much cosmic expansion has occurred

The substrate-physics derivation work IS Phase 3-A3's load-bearing step. The implementor should surface candidates explicitly in the prereg + adjudicate via canonical-content + Grant adjudication mid-derivation if unable to close from canonical content alone.

## Per `consistency-vs-emergence` v1.3 Step 8 — classification stays at Class E

**Canonical-source classification ceiling** (per `omega-freeze-cosmic-grain-cascade.md:13-16` + `boundary-observables-m-q-j.md` Class E framing): **Class E operating-point projection** (joint-constrained observable in the cosmic-substrate family).

**Step 8b: What NEW substrate-physics content does Phase 3-A3 add beyond canonical Machian-G framework?** Nothing structural. The work is:
- Substrate-native canonical leaf creation (formalization rigor improvement)
- Type B walk-back of SM-leaked language to substrate-native Machian-G framing (vocabulary cleanup)
- $u_0^* \to A_0^{cosmic}/A_{yield}$ mapping derivation (substrate-thermodynamic step within the canonical cascade)

None of these add substrate-mechanism content BEYOND the canonical Machian-G framework. The cascade structure is already canonical; Phase 3-A3 formalizes one more projection within it.

**Step 8c result: classification stays at Class E** matching canonical-source ceiling. Phase 3-A3 is **substrate-native formalization + vocabulary cleanup + substrate-thermodynamic-mapping closure**, NOT new substrate-mechanism emergence.

**Step 8d**: not applicable (no promotion past canonical ceiling).

**Confidence lift target**: clm-009nkt 0.45 → 0.55-0.60 PARTIAL band (canonical-leaf formalization rigor + substrate-thermodynamic-mapping closure). If the $u_0^* \to A_0^{cosmic}/A_{yield}$ mapping closes cleanly from canonical content, lift to 0.60. If mapping requires Grant adjudication mid-derivation OR partial closure, lift to 0.55.

## Type B walk-back scope (ave-walk-back v1.2 Step 3h-exhaustive pre-frozen patterns)

Phase 3-A3 work includes Type B walk-back of SM-leaked language across canonical content. Pre-frozen pattern enumeration per Step 3h-exhaustive-1:

**SM-leaked language patterns to walk back**:

| Pattern (OLD) | Target (NEW substrate-native) |
|---|---|
| `"first-principles derivation from G_vac + equipartition"` | `"substrate-thermodynamic derivation of $u_0^* \to A_0^{cosmic}/A_{yield}$ mapping in Machian-G operating-point cascade"` |
| `"thermal expansion"` (when describing δ_strain mechanism) | `"cosmic-genesis-residual substrate operating-point loading"` |
| `"spatial-metric thermal expansion"` (when applied to δ_strain) | `"substrate spatial-metric strain at cosmic operating-point via Ax 4 saturation kernel + INVARIANT-S2 SYM scaling"` |
| `"pending derivation from G_vac + equipartition"` | `"pending substrate-thermodynamic derivation of $u_0^* \to A_0^{cosmic}/A_{yield}$ mapping"` |
| `"physical narrative consistent with the predicted sign, not a derivation of magnitude"` | `"Class E operating-point projection in Machian-G family; magnitude derivable via substrate-thermodynamic mapping from $u_0^*$ to $A_0^{cosmic}$"` |

**Corpus-wide grep targets** (per Step 3h-exhaustive-2):

```bash
grep -rn "G_vac + equipartition\|G_vac.+equipartition\|first-principles derivation from G_vac" manuscript/ave-kb/ research/ _orchestration/
grep -rn "thermal expansion" manuscript/ave-kb/ | grep -i "delta.strain\|δ.strain\|cmb"
grep -rn "spatial-metric thermal expansion\|spatial metric thermal expansion" manuscript/ave-kb/
grep -rn "fitted scalar.*T_CMB\|fitted scalar.*T_{CMB}" manuscript/ave-kb/
```

**Q1/Q2 classification rules** (per Step 3h-exhaustive-3):
- LOAD-BEARING: any place that says δ_strain derivation is "pending G_vac + equipartition" without flagging this as Machian-G family projection language
- STALE-PROSE: narrative explanations of δ_strain in classical thermal-expansion language not connected to Machian-G framework
- PRESERVED-HISTORICAL (Q1): walk-back-provenance notes if any (e.g., "previously framed as G_vac + equipartition; walked back 2026-05-28 to Machian-G projection")
- FROZEN-SNAPSHOT (Q2): pre-2026-05-28 research docs / session handoffs with SM-leaked language (exempt per Q2)

**Files in scope** (pre-frozen list; implementor extends via grep):
- `manuscript/ave-kb/common/mathematical-closure.md` (canonical δ_strain framing at line 105)
- `manuscript/ave-kb/vol1/claim-quality.md` (clm-009nkt + clm-5xon03 entries)
- `manuscript/ave-kb/vol1/ch0-intro.md` (foreword bullets on δ_strain)
- `manuscript/ave-kb/entry-point.md` (top-level framework framing)
- `manuscript/ave-kb/common/claim-quality.md` (cross-volume δ_strain references)
- `manuscript/ave-kb/vol3/claim-quality.md` (vol3 cosmology references)
- `manuscript/ave-kb/vol4/claim-quality.md:1207` (vol4 reference)
- `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md:63`
- `manuscript/ave-kb/common/full-derivation-chain.md:647`
- `manuscript/ave-kb/common/divergence-test-substrate-map.md:669, 720` (Mermaid + open-item entries)

## New canonical leaf placement

**Recommended location**: `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-projection.md` (alongside `cosmological-constant-closure.md` which already carries the inherited Machian-G framework framing).

**Alternate**: `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md` could host a §"δ_strain as Class E Machian-G projection" subsection, but creating a separate canonical leaf is preferred per the KB-structure pattern (each claim gets its own leaf when substantive substrate-physics content).

Implementor decides based on corpus structure survey.

## Skills firing list — Phase 3-A3 (MANDATORY + explicit)

**Primary skill**: `consistency-vs-emergence` v1.3 — Step 8c canonical fire-case. The classification-promotion check fires because Phase 3-A3 work formalizes content already at Class E canonical-source ceiling without adding new substrate-mechanism content. Classification stays at Class E.

**Secondary skills** (all MANDATORY):

- **`ave-walk-back` v1.2** — Type B walk-back across canonical content with Step 3h-exhaustive procedure (pre-frozen patterns above; implementor extends). Companion `ave-sweep-audit` fires pre-merge per v1.2 cross-link to validate propagation completeness.
- **`ave-worktree-paths` v1.0** — first-call `git rev-parse --show-toplevel` canary + worktree-absolute-paths from FIRST call. CRITICAL — this is the NEW skill's first formal fire after PR #44 prototype.
- **`ave-discipline-translate` v1.1 Trigger 6** — substrate-native vocabulary primary throughout. This is the LOAD-BEARING discipline for Phase 3-A3 because the scope IS cleaning up SM-leaked language. "thermal expansion" / "equipartition" / "G_vac + equipartition" / "fitted scalar" all need substrate-native rewrites OR explicit translation-reference framing.
- **`ave-prereg` v1.1** — Step 3.5 dim-analysis at canonical primitives (already pre-frozen above; implementor extends with substrate-thermodynamic-mapping work for $u_0^* \to A_0^{cosmic}/A_{yield}$).
- **`ave-canonical-leaf-pull` v1.3** — Trigger 17 vocabulary-broadened pre-survey for δ_strain canonical content + omega-freeze cascade canonical anchor + Machian-G framework references.
- **`ave-canonical-source`** — canonical constants from `src/ave/core/constants.py` (DELTA_STRAIN, ALPHA, ALPHA_COLD_INV, T_CMB). The engine value `DELTA_STRAIN = 1 - (1/ALPHA)/ALPHA_COLD_INV` is the CODATA back-subtraction; the substrate-derivation target is the SAME numerical value via Machian-G cascade.
- **`substrate-native-check`** — K4 + Cosserat + Ax 1 + Ax 4 substrate walk before deriving the $u_0^* \to A_0^{cosmic}$ mapping. Bond-tension / node-LC / differential-rotation substrate modes — how does the cosmic operating-point distribute across them?
- **`phase-space-coordinate-check`** — operating-point amplitude space ($A_0/A_{yield}$ dimensionless) vs physical-mode coordinates (bond tension Pa; node-LC field V/m or T). Keep coordinates explicit in the derivation.
- **`ave-evidence-framing-discipline`** — precision on "Machian-G projection" vs "Machian-G derivation" language. δ_strain is a projection of the cascade, not a fresh derivation of the cascade.
- **`verify-before-cite` v1.4** — every canonical citation grep-verified (especially omega-freeze cascade canonical references; INVARIANT-S2 SYM scaling lines in CLAUDE.md; Ax 4 saturation kernel form).
- **`ave-discrimination-check`** — Class E operating-point projection IS substrate-distinct vs SM (SM has no analog of cosmic-substrate operating-point cascade). The δ_strain time-variation-at-higher-redshift prediction (via cosmic-substrate evolution) IS a substrate-distinct empirical handle — flag it explicitly.
- **`ave-handoff-canonical-locale`** — implementor's deliverables land at canonical locations per repo convention (`manuscript/ave-kb/`, `research/`); orchestration brief lives at `_orchestration/` (this brief).
- **`ave-analytical-tool-selection`** — toolkit consultation: Mode class (Ax 4 saturation-kernel response), Boundary class (Machian boundary impedance at Hubble horizon), Coupling class (INVARIANT-S2 SYM scaling), Power class (δα/α modulation).
- **`ave-audit`** — pre-audit grep verification before any auditor spawn.

## Branch + spawn protocol

- **Branch**: `analysis/phase-3-a3-delta-strain-machian-projection` (already created from `main @ fb2fa923` by orchestration session)
- **Implementor checkout**: in worktree, `git fetch origin && git checkout analysis/phase-3-a3-delta-strain-machian-projection` to land on existing branch with this prework brief already committed
- **Push branch but DO NOT merge** — orchestration session opens PR after Phase 3-A4-rev scoping also lands (per Grant 2026-05-28 "one PR for both" directive)
- **Worktree isolation**: `isolation: "worktree"` per `Agent` tool; STAY IN WORKTREE per `ave-worktree-paths` v1.0 discipline (this is the new skill's first formal fire)
- **Single-deliverable scope** — δ_strain canonical leaf + Type B walk-back propagation; do NOT touch Phase 3-A4-rev work or other queue items

## Expected deliverables

1. **Prereg** at `research/2026-05-28_phase-3-a3-delta-strain-machian-projection-prereg.md` — including Step 3.5 substrate-thermodynamic-mapping work (extend the pre-frozen $A_0^{cosmic}/A_{yield} \approx 1.72 \times 10^{-3}$ derivation with mapping candidate from $u_0^*$), Trigger 17 pre-survey results, master-equation-derivation-path scaffold for the Machian-G cascade applied to δ_strain projection, Class E classification statement per v1.3 Step 8c.

2. **Result doc** at `research/2026-05-28_phase-3-a3-delta-strain-machian-projection-result.md` — end-to-end substrate-thermodynamic mapping + Class E classification with substrate-native vocabulary throughout + INVARIANT-S2 SYM scaling derivation trace + cosmic-substrate-evolution time-variation forward-prediction.

3. **New canonical leaf** at `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-projection.md` (or implementor-determined location per corpus structure survey) — substrate-native Machian-G framing; cross-links to omega-freeze cascade + Op14/Op16 metric-lensing canonical + INVARIANT-S2 SYM scaling + cosmological-constant-closure leaf.

4. **Type B walk-back commits** — SM-leaked language across the file list above (and any additional sites surfaced by Step 3h-exhaustive grep) walked back to substrate-native Machian-G framing. Per Step 3h-exhaustive Q1/Q2 discipline.

5. **clm-009nkt entry update** at `manuscript/ave-kb/vol1/claim-quality.md` — confidence 0.45 → 0.55-0.60 PARTIAL band; rationale explains Class E classification + substrate-thermodynamic-mapping closure status + remaining open derivation gaps.

6. **clm-5xon03 partial-closure note** at `manuscript/ave-kb/vol1/claim-quality.md` — the "Fitted (one scalar at T_CMB)" condition partly closed via Phase 3-A3 substrate-native derivation; remaining open: the cosmic-substrate $u_0^*$ derivation itself (downstream omega-freeze cascade closure).

7. **`make refresh-kb-metadata` + `make verify-kb-metadata` PASS** pre-push.

8. **Commit messages** following project pattern + Co-Authored-By footer; format `phase-3-a3(clm-009nkt): <scope>`.

## Pure-AVE-corpus rule

NO references to investors/funds/interviews/external pitches in any deliverable. Pure substrate physics only.

## Adjudication criteria

- **PASS** (~50%): Phase 3-A3 substrate-native canonical leaf + Type B walk-back propagation lands cleanly; substrate-thermodynamic mapping $u_0^* \to A_0^{cosmic}/A_{yield}$ closes from canonical content; Class E classification explicit; pipeline verify PASS; clm-009nkt 0.45 → 0.60.
- **PARTIAL** (~40%): canonical leaf + walk-back land; substrate-thermodynamic mapping requires Grant adjudication mid-derivation OR partial closure (e.g., dimensional bridge established but specific factor unresolved); clm-009nkt 0.45 → 0.55.
- **WALK-BACK** (~10%): mapping cannot close from canonical content + Grant adjudication doesn't resolve; document honestly; flag as candidate framework-extension question Q-DELTA-MAP-1.

## Honest closure probability

The substrate-thermodynamic mapping is the load-bearing open step. If canonical omega-freeze cascade content has the substrate-amplitude scaling already implicit (just needs explicit extraction), PASS is high. If the mapping requires new substrate-physics content (e.g., cosmic-expansion-dilution factor that isn't canonical yet), PARTIAL is more likely. Step 3.5 dim-analysis pre-froze the $A_0^{cosmic}/A_{yield} \approx 1.72 \times 10^{-3}$ target value; the implementor's work is the substrate-physics mapping that produces this value from $u_0^* \approx 0.187$.

## Implementor brief (ready-to-paste post-prework-brief-commit)

```
You are an AVE implementor session executing Phase 3-A3 of the clm-009nkt δ_strain Machian-G projection epic. Your single deliverable is a substrate-native canonical leaf formalizing δ_strain as the 5th Class E operating-point projection in the Machian-G family + Type B walk-back propagation of SM-leaked language across canonical content.

Read first (mandatory, all worktree paths):
1. `_orchestration/2026-05-28_phase-3-a3-prework.md` — THE prework brief; primary briefing material (substrate-physics derivation chain, Step 3.5 dim-analysis pre-frozen, Type B walk-back pre-frozen patterns, skills firing list, deliverables, adjudication criteria)
2. `_orchestration/2026-05-27_session-handoff.md` — Phase 3-A4 full-cycle session arc (the recent prototype case + skill amendments)
3. CLAUDE.md + manuscript/ave-kb/CLAUDE.md — repo + KB conventions (especially INVARIANT-S2 Ax 4 saturation kernel + INVARIANT-S2 SYM scaling)
4. `manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md:13-16` — canonical cosmic-substrate operating-point $u_0^* \approx 0.187$ + Class E joint-constraint family
5. `manuscript/ave-kb/vol1/claim-quality.md` clm-009nkt entry — δ_strain canonical claim status
6. `manuscript/ave-kb/vol1/claim-quality.md` clm-5xon03 entry — Zero-Parameter Closure Status with "fitted scalar" caveat
7. `manuscript/ave-kb/common/mathematical-closure.md:105` — canonical δ_strain framing (SM-leaked; walk-back scope)
8. `manuscript/ave-kb/common/boundary-observables-m-q-j.md` — Class E joint-constraint structure
9. `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md` — Machian-G framework canonical example (companion canonical leaf for the new leaf's neighborhood)
10. `src/ave/core/constants.py` — DELTA_STRAIN + ALPHA + ALPHA_COLD_INV + T_CMB canonical constants

Operating parameters:
- Branch: `analysis/phase-3-a3-delta-strain-machian-projection` off `main @ fb2fa923` (already created; this prework brief already committed)
- Within worktree: `git fetch origin && git checkout analysis/phase-3-a3-delta-strain-machian-projection`
- Push branch but DO NOT merge — orchestration session opens PR after Phase 3-A4-rev scoping also lands

CRITICAL — `ave-worktree-paths` v1.0 discipline (NEW SKILL):
First call: `git rev-parse --show-toplevel` to verify worktree root. All Reads + Edits via worktree-absolute paths from FIRST call onward. Do NOT Read parent-repo absolute paths even for citation verification. This is the new skill's first formal fire; honor it strictly.

Full skill compliance mandatory (per prework brief skills firing list):
ave-prereg v1.1 (Step 3.5 substrate-thermodynamic-mapping); ave-canonical-leaf-pull v1.3 (Trigger 17 vocabulary-broadened pre-survey); ave-canonical-source; ave-discipline-translate v1.1 Trigger 6 (substrate-native vocab — LOAD-BEARING for the SM-leakage cleanup scope); substrate-native-check; consistency-vs-emergence v1.3 (Step 8c canonical fire-case — Class E stays at Class E); ave-walk-back v1.2 (Type B walk-back Step 3h-exhaustive with companion ave-sweep-audit pre-merge); ave-worktree-paths v1.0 (first-call discipline); verify-before-cite v1.4; ave-evidence-framing-discipline; ave-discrimination-check; ave-handoff-canonical-locale; ave-analytical-tool-selection; ave-audit; phase-space-coordinate-check.

Open substrate-physics question (work through in prereg):
The substrate-thermodynamic mapping $u_0^* \approx 0.187 \to A_0^{cosmic}/A_{yield} \approx 1.72 \times 10^{-3}$ is the load-bearing open step. Three candidate paths:
- (P1) $u_0^*$ as cosmic-genesis dimensionless coordinate; mapping involves cosmic-expansion-ratio conversion
- (P2) $u_0^*$ and $A_0^{cosmic}/A_{yield}$ at different substrate-physical scales; bridge via $R_H/\ell_{node} \sim 10^{39}$ Machian-holographic
- (P3) $u_0^*$ corresponds to cosmic-genesis operating-amplitude; today's $A_0^{cosmic}/A_{yield}$ via cosmic-expansion-dilution

Surface in prereg + work through via canonical content (omega-freeze cascade + Machian-G framework leaves). If unable to close from canonical content alone, STOP and surface to Grant via orchestration session before proceeding.

Pre-merge: spawn ave-sweep-audit companion (per ave-walk-back v1.2 cross-link) to validate Type B walk-back propagation completeness BEFORE branch push — much cheaper than post-merge cleanup (per Phase 3-A4 5x miss-rate lesson).

Expected deliverables: per prework brief.

Adjudication criteria: PASS (~50%) / PARTIAL (~40%) / WALK-BACK (~10%) per prework brief.

Report back: outcome + commit SHAs + branch confirmation pushed + self-audit verdict + verify pipeline PASS + cross-agent pollution check + new framework-extension questions raised mid-derivation + Q1/Q2 sweep-pattern self-check results.

Begin with worktree verification → mandatory read list → Trigger 17 vocabulary-broadened pre-survey → Step 3.5 substrate-thermodynamic-mapping extension → prereg with substrate-thermodynamic mapping framing + Class E classification per v1.3 Step 8c → derivation → canonical leaf + walk-back commits → companion sweep-audit pre-push.
```

## Phase 3-A4-rev scoping placeholder

After Phase 3-A3 implementor returns, Grant + orchestration session discuss Phase 3-A4-rev scoping (Clifford-torus codimensional embedding from K4 substrate primitives — the canonical Class 2 closure path for clm-0ktpcn). Scoping brief drafted at `_orchestration/2026-05-28_phase-3-a4-rev-scoping.md` on the same branch. ONE PR for both Phase 3-A3 execution + Phase 3-A4-rev scoping per Grant 2026-05-28 directive.

Per `consistency-vs-emergence` v1.3 Step 8d: Phase 3-A4-rev IS the canonical promotion-justification case — adds new substrate-physics content (K4-substrate-primitive derivation of the Clifford-torus embedding) beyond ch8:109-128 substrate-orthogonal-channel canonical content. Class 2 substrate-mechanism emergence IS earnable IF the K4-substrate-derivation closes.

Phase 3-A4-rev scoping work establishes the substrate-physics scope + derivation path + adjudication criteria; execution lands in a subsequent PR.
