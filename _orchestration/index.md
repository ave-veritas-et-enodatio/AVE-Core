# AVE-Core Orchestration Index

**Last updated**: 2026-05-19 EOD (post orchestration-tracking-promoted + claude-md-atopile-cleanup + cosmic-axis-glossary epic queued)
**Current HEAD on `analysis/integration`**: `720a7df`
**E1b cascade-anchor commit**: `54f0698` (Section E cascade state anchored here; later commits are meta-work)
**Audit tag count**: 20 (`git tag -l "audit/*" | wc -l`)
**Active branches**: 6 (`analysis/integration`, `research/l3-electron-soliton`, `main`, `analysis/c8-baryon-ladder-pdg-anchor`, `benn/long-running`, `golden-torus-update`)

This is the cross-cutting carry-forward for AVE-Core orchestration. Per-epic state lives in adjacent `<epic-slug>.md` files; this doc carries the priority ladder, open decisions, and active-epic table.

## Active epics

| Epic | Doc | Status | Last phase landed |
|---|---|---|---|
| Section E cascade | [`section-e-cascade.md`](section-e-cascade.md) | ACTIVE | E1b CLOSED 2026-05-19 (`54f0698`); E1b-prime PENDING |
| Cosmic-axis glossary | [`cosmic-axis-glossary.md`](cosmic-axis-glossary.md) | IN-FLIGHT — merge HELD | Phases 1-3+5 landed on branch `analysis/cosmic-axis-glossary`; Phase 4 (H_∞ hygiene) DEFERRED to h-infinity-derivation-audit epic |
| H_∞ derivation audit | [`h-infinity-derivation-audit.md`](h-infinity-derivation-audit.md) | ACTIVE — implementor kickoff pending | Spawned from cosmic-axis-glossary Phase 4 Class-A halt. Math audit on H_∞ ↔ G derivation circularity. Single research doc deliverable. |

## Queued epics (not yet kicked off — would create new docs when activated)

| Epic | Doc | Trigger | Notes |
|---|---|---|---|
| DM META closure | (no doc yet) | Grant greenlight | Independent of Section E. Closes C13c META row. ~1-2 sessions. |
| Phase 2 mass-spectrum activation | (no doc yet) | Grant greenlight | Pre-greenlit 2026-04-30 per [`research/_archive/L3_electron_soliton/98_framework_decision_ii_mass_spectrum_activation.md:5`](../research/_archive/L3_electron_soliton/98_framework_decision_ii_mass_spectrum_activation.md). W/Z/Higgs eigenvalue solver; ~1 week scope. |
| Hygiene pass | (no doc yet) | Batch convenience | Items 4-9 from "Open decisions" below; ~30 min each. |

## Next-move priority ladder

### Immediate (1-2 sessions each, independent)

1. **E1b-prime — Pantheon+ raw-SN bulk-flow re-fit** — highest leverage. Pushes C5 Outcome D → A/A+ or C decisively. Unlocks E1c gate. Briefing to be drafted into `section-e-cascade.md` as Phase E1b-prime PENDING when greenlit.
2. **DM META closure session** — parallel-runnable with item 1. Closes C13c META row tracking 3 coexisting DM framings (DAMA refresh-rate proportionality-constant + formal META unification doc).

### Medium-term (multi-session)

3. **E1c Route 3 framework-commitment activation** — conditional on item 1 outcome (PASS or PARTIAL).
4. **Phase 2 mass-spectrum activation (W/Z/Higgs eigenvalue solver)** per doc 98 §3.2. Grant already adjudicated this track 2026-04-30; not gated on E1c.

### Hygiene tier (any session, batchable)

5. Items 4-9 from "Open decisions" below. Each is small (≤30 min). Can be batched into a single hygiene-pass session.

## Open decisions

| # | Item | Detail |
|---|---|---|
| 1 | **E1b-prime — Pantheon+ tightening session** | Highest-leverage next move per E1b result. ~1-2 sessions. Would push CMB-vs-Hubble to 3σ-decisive, settling C5 D → A/A+ or C. Implementation session pattern. **Adjudication**: kick off now or defer? |
| 2 | **DM META closure** | Independent of C5. Two of three limbs (galactic + bullet cluster) already anchored; needs DAMA refresh-rate proportionality-constant derivation + formal META unification doc. Implementation session pattern. Can run in parallel with item 1. |
| 3 | **Phase 2 mass-spectrum activation** per doc 98 §3.2 | Separate research track Grant already adjudicated 2026-04-30 ("(ii) works"). ~1 week scope. Not blocked by Section E cascade. **Adjudication**: queue now or after items 1/2? |
| 4 | **C3-MUON-DELTA Run-4/5 update** | Fermilab Run-4/5 expected 2026-2027 at ±10 ppm. When it lands, the C3 driver needs a re-run + matrix update. Timing-dependent. |
| 5 | **AVE-Core CLAUDE.md atopile pollution** | Replaced 2026-05-19 EOD with proper AVE orientation pointing to `manuscript/ave-kb/CLAUDE.md` + `_orchestration/` + `.agents/handoffs/`. **CLOSED**. |
| 6 | **AVE-Protein 51 uncommitted files** | Mass deletions of engines + manuscript chapters. Major refactor mid-stream. Surface: intentional WIP or accidental? Grant decides commit / stash / restore. |
| 7 | **AVE-Metamaterials SOLAR_PANEL_INITIATIVE WIP** (8 uncommitted) | Active workstream not yet committed. Grant decides when to commit. |
| 8 | **AVE-QED PDF gitignore + .tex commit** | 2 uncommitted: 1 modified `09_anomalous_moment.tex` + 1 untracked `main.pdf` (build artifact). Should gitignore the PDF, commit the .tex when ready. |
| 9 | **`analysis/c8-baryon-ladder-pdg-anchor` branch fate** | 2 unpushed Q-G47 retrofit commits pushed earlier; branch still alive on local + origin. Session-record-of-stale-corpus-view per Option A. Keep as historical or delete via audit-tag pattern? |
| 10 | **Cosmic-axis glossary scope adjudication** | RESOLVED 2026-05-19 EOD: scope C + H_∞ hygiene fold-in. Implementor kickoff pending. |

## Skill ecosystem state

- 22 active skills with `verify-before-cite` v1.2 as the most recently updated (cross-branch sub-projection of trigger 7)
- `ave-handoff-canonical-locale` v1.0 added 2026-05-19 EOD (this directory's write-time discipline)
- Adversarial probes tracked at 9-for-9 finding orthogonal-axis gaps

## Reference paths (canonical, tracked)

| Path | Purpose |
|---|---|
| [`_orchestration/section-e-cascade.md`](section-e-cascade.md) | Active Section E epic |
| [`_orchestration/cosmic-axis-glossary.md`](cosmic-axis-glossary.md) | Cosmic-axis glossary epic (IN-FLIGHT, merge HELD) |
| [`_orchestration/h-infinity-derivation-audit.md`](h-infinity-derivation-audit.md) | H_∞ derivation audit epic (ACTIVE) |
| [`_orchestration/README.md`](README.md) | Convention doc for this directory |
| [`CLAUDE.md`](../CLAUDE.md) | AVE-Core agent orientation (replaces atopile pollution as of 2026-05-19 EOD) |
| [`manuscript/ave-kb/CLAUDE.md`](../manuscript/ave-kb/CLAUDE.md) | Cross-cutting KB invariants |
| [`manuscript/ave-kb/common/divergence-test-substrate-map.md`](../manuscript/ave-kb/common/divergence-test-substrate-map.md) | 33-row experimental-claim landscape |
| [`manuscript/ave-kb/common/closure-roadmap.md`](../manuscript/ave-kb/common/closure-roadmap.md) | Running changelog |
| `git tag -l "audit/*"` | 20 immutable audit tags |
| [`.agents/handoffs/`](../.agents/handoffs/) | Ephemeral scratch (gitignored; NOT canonical — see `_orchestration/` for tracked state) |

## Playbook for the next orchestration session

1. **First read**: this file (`index.md`) + the relevant active epic doc(s).
2. **Phase 0 state verification**:
   - `git log analysis/integration -1 --oneline` should match the HEAD listed above (or have advanced)
   - `git tag -l "audit/*" | wc -l` should match (or have advanced)
   - `git branch` should show the active branches listed above
3. **Don't trust corpus-state claims here without re-verifying** (per `verify-before-cite` v1.2 trigger 7): facts here are accurate as of the Last-updated date; if days/weeks later, re-verify via `git log --since=<date>` + cross-branch `git log --all`.
4. **Ask Grant**: which item from "Open decisions" to action first. Default if not specified: priority ladder item 1 (E1b-prime Pantheon+ tightening).
5. **For implementor-session kickoff**: append a `## Phase X (PENDING)` section to the relevant epic doc with assumptions A1-AN, scope boundary, phase plan, adjudication criteria, verification — that's the implementor briefing. The implementor reads that section as their input.

## Pure-AVE-corpus rule

All content in this directory is pure physics. No external context (no investor / fund / interview references). Tracked files MUST be scrubbed before commit.
