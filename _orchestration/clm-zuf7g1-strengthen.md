# Epic: clm-zuf7g1 Phase-Locked Topological Thread + Bell + Born-Rule Strengthening

**Status**: QUEUED — pre-prereg stub. No driver, no run, no commits yet.
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

## Phase plan (TBD on session kickoff)

| Phase | Goal | Status |
|---|---|---|
| 0a | Orchestration epic doc + corpus-grep survey (ave-prereg) | PENDING — replace this stub with full plan |
| 0b | Workstream-level pre-registration doc | PENDING |
| 1 | Wire clm-zuf7g1 → clm-salw2h depends-on edge (partial closure of item 3 above; chain-promotion only, no new physics) | LOW-RISK — could land first session |
| 2 | Strengthen clm-ldmvwi (Born Rule from Ohmic Measurement) — the dominant solidity bottleneck | OPEN — needs its own scoping |
| 3 | Derive lossless-LC-resonator structural identification (item 2) | OPEN — likely multi-session |
| 4 | Add separate claim-quality entry for Möbius coupling (item 4) | LOW-RISK — bookkeeping |

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
