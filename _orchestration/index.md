# AVE-Core Orchestration Index

**Last updated**: 2026-05-19 EOD (post 4-merge sequence: cosmic-axis-glossary + h-infinity-derivation-audit + h-infinity-framing-forward + c5-pantheon-tightening; Class E canonized; downstream-cascade + SDSS DR17 epics drafted; Pantheon+ LFS cache landed)
**Current HEAD on `analysis/integration`**: `9f976e0` (SDSS DR17 merge tip; will advance with this commit)
**Audit tag count**: 26 (`git tag -l "audit/*" | wc -l`) — 2 added this session (h-infinity-downstream-cascade + c5-sdss-dr17-spin-orientation)
**Active branches** (local): 6 — `analysis/integration`, `research/l3-electron-soliton`, `main`, `analysis/c8-baryon-ladder-pdg-anchor`, `benn/long-running`, `golden-torus-update`. All 4 May-19 implementor branches merged + deleted (local + remote).

This is the cross-cutting carry-forward for AVE-Core orchestration. Per-epic state lives in adjacent `<epic-slug>.md` files; this doc carries the priority ladder, open decisions, and active-epic table.

## Active epics

| Epic | Doc | Status | Last phase landed |
|---|---|---|---|
| Section E cascade | [`section-e-cascade.md`](section-e-cascade.md) | ACTIVE — E1b-prime CLOSED Outcome Marginal-D; SDSS DR17 next-session candidate (separate epic) | E1b-prime merged 2026-05-19 EOD via `c587573` audit tag `audit/2026-05-19_c5-pantheon-tightening`; σ_Hubble = 24.0°, +2.83σ above 20° threshold, NOT 3σ-decisive |
| Soliton-lattice coupling operator | [`soliton-lattice-coupling-operator.md`](soliton-lattice-coupling-operator.md) | ACTIVE — Session 1 (scoping research doc only) ready to spawn | NEW 2026-05-19 EOD post-SDSS DR17 operator-output reframing. Multi-session arc: scoping → derivation → planetary test → galactic extrapolation. Session 1 deliverable: research doc only (no derivation). |

## Recently closed epics (this session)

| Epic | Doc | Closure | Audit tag |
|---|---|---|---|
| Cosmic-axis glossary | [`cosmic-axis-glossary.md`](cosmic-axis-glossary.md) | Merged 2026-05-19 EOD via `fb62fa8` | `audit/2026-05-19_cosmic-axis-glossary` |
| H_∞ derivation audit | [`h-infinity-derivation-audit.md`](h-infinity-derivation-audit.md) | Merged 2026-05-19 EOD via `ceb8205` (research doc archival) | `audit/2026-05-19_h-infinity-derivation-audit` |
| H_∞ framing-forward | [`h-infinity-framing-forward.md`](h-infinity-framing-forward.md) | Merged 2026-05-19 EOD via `a7e555e` (Class C walk-back applied; Class E refinement queued in downstream-cascade epic) | `audit/2026-05-19_h-infinity-framing-forward` |
| H_∞ downstream cascade | [`h-infinity-downstream-cascade.md`](h-infinity-downstream-cascade.md) | Merged 2026-05-19 EOD via `d2d38de` (Class C → Class E reclass + 5 anomalies + Class E candidate sweep) | `audit/2026-05-19_h-infinity-downstream-cascade` |
| C5 SDSS DR17 spin-orientation | [`c5-sdss-dr17-spin-orientation.md`](c5-sdss-dr17-spin-orientation.md) | Merged 2026-05-19 EOD via `9f976e0` (Marginal-D + operator-output reframing) | `audit/2026-05-19_c5-sdss-dr17-spin-orientation` |

Per `_orchestration/README.md` convention, these closed-epic docs will move to `_archive/` in a future hygiene pass. For now they remain in place for cross-reference accessibility.

## Queued epics (not yet kicked off — would create new docs when activated)

| Epic | Doc | Trigger | Notes |
|---|---|---|---|
| DM META closure | (no doc yet) | Grant greenlight | Independent of Section E. Closes C13c META row. ~1-2 sessions. |
| Phase 2 mass-spectrum activation | (no doc yet) | Grant greenlight | Pre-greenlit 2026-04-30 per [`research/_archive/L3_electron_soliton/98_framework_decision_ii_mass_spectrum_activation.md:5`](../research/_archive/L3_electron_soliton/98_framework_decision_ii_mass_spectrum_activation.md). W/Z/Higgs eigenvalue solver; ~1 week scope. |
| Hygiene pass | (no doc yet) | Batch convenience | Items 6-9 from "Open decisions" below; ~30 min each. |
| Closed-epic archive move | (no doc yet) | Batch hygiene | Move 3 closed epic docs to `_archive/` per README convention. ~15 min. |

## Next-move priority ladder

### Immediate (1-2 sessions each, can run in parallel with `isolation: "worktree"`)

1. **H_∞ downstream cascade** — applies Class E reclassification across 13+ files + 5 surfaced anomalies. Activates the v1.1 `consistency-vs-emergence` skill refinement on already-landed work.
2. **C5 SDSS DR17 spin-orientation** — independent observable, comparable tightening potential to E1b-prime. If 3σ-decisive, unlocks E1c gate. Scope-pick pending Grant adjudication (G1 in epic brief).
3. **DM META closure** — parallel-runnable with items 1+2. Closes C13c META row.

### Medium-term (multi-session)

4. **E1c Route 3 framework-commitment activation** — conditional on C5 settling at 3σ via SDSS DR17 (or alternative observable).
5. **Phase 2 mass-spectrum activation (W/Z/Higgs eigenvalue solver)** per doc 98 §3.2. Grant already adjudicated this track 2026-04-30; not gated on E1c.
6. **Observable 5 (E/B polarization), Observable 6 (orbital alignments), Observable 7 (G P_2 anisotropy)** — each multi-session, deferred until C5 settles.

### Hygiene tier (any session, batchable)

7. Items 6-9 from "Open decisions" below. Each is small (≤30 min). Can be batched into a single hygiene-pass session.
8. Closed-epic archive move (3 docs → `_archive/`).

## Open decisions

| # | Item | Detail |
|---|---|---|
| 1 | **H_∞ downstream cascade implementor kickoff** | Brief at [`h-infinity-downstream-cascade.md`](h-infinity-downstream-cascade.md). Grant adjudicated scope 2026-05-19 EOD; ready to spawn. Recommend `isolation: "worktree"`. |
| 2 | **C5 SDSS DR17 scope adjudication** | Brief at [`c5-sdss-dr17-spin-orientation.md`](c5-sdss-dr17-spin-orientation.md). 3 scope options A/B/C; recommend A. **Adjudication**: pick scope + kickoff or defer? |
| 3 | **DM META closure** | Independent of C5. Two of three limbs (galactic + bullet cluster) already anchored; needs DAMA refresh-rate proportionality-constant derivation + formal META unification doc. Implementation session pattern. Can run in parallel with items 1+2. |
| 4 | **Phase 2 mass-spectrum activation** per doc 98 §3.2 | Separate research track Grant already adjudicated 2026-04-30 ("(ii) works"). ~1 week scope. Not blocked by Section E cascade. **Adjudication**: queue now or after items 1-3? |
| 5 | **C3-MUON-DELTA Run-4/5 update** | Fermilab Run-4/5 expected 2026-2027 at ±10 ppm. When it lands, the C3 driver needs a re-run + matrix update. Timing-dependent. |
| 6 | **AVE-Protein 51 uncommitted files** | Mass deletions of engines + manuscript chapters. Major refactor mid-stream. Surface: intentional WIP or accidental? Grant decides commit / stash / restore. |
| 7 | **AVE-Metamaterials SOLAR_PANEL_INITIATIVE WIP** (8 uncommitted) | Active workstream not yet committed. Grant decides when to commit. |
| 8 | **AVE-QED PDF gitignore + .tex commit** | 2 uncommitted: 1 modified `09_anomalous_moment.tex` + 1 untracked `main.pdf` (build artifact). Should gitignore the PDF, commit the .tex when ready. |
| 9 | **`analysis/c8-baryon-ladder-pdg-anchor` branch fate** | 2 unpushed Q-G47 retrofit commits pushed earlier; branch still alive on local + origin. Session-record-of-stale-corpus-view per Option A. Keep as historical or delete via audit-tag pattern? |
| 10 | **Closed-epic archive move** | Move cosmic-axis-glossary + h-infinity-derivation-audit + h-infinity-framing-forward docs to `_archive/` per README convention. Inbound references (closure-roadmap, audit-tag commit messages) point at current paths — moving requires either link updates OR symlink shims. Adjudication: move + update inbound refs / move + symlinks / leave in place. |

## Skill ecosystem state (this session updates)

- **`verify-before-cite` v1.3** (was 1.2) — trigger 8 added (commit-application claims) at `~/.claude/skills/verify-before-cite/SKILL.md` commit `e0be68a`. Sixth instance of bilateral-axis pattern (commit-axis projection of cross-branch state, complementing trigger 7-c doc-axis projection at v1.2).
- **`consistency-vs-emergence` v1.1** (was 1.0) — Class E added (operating-point projection / topological equilibrium observable) at `~/.claude/skills/consistency-vs-emergence/SKILL.md` commit `8dfc31d`. Grant canonized 2026-05-19 EOD post-Thread-2 H_∞ adjudication.
- **`ave-handoff-canonical-locale` v1.0** added 2026-05-19 EOD (this directory's write-time discipline)
- **AVE-Core directives**: CLAUDE.md + `_orchestration/README.md` updated 2026-05-19 EOD with pre-commit branch-check discipline + implementor-spawn worktree-isolation default per `e9245cc` (closes the cosmic-axis-glossary→h-infinity-derivation-audit branch-confusion failure).
- 23 active skills; adversarial probes tracked at 14-for-14 finding orthogonal-axis gaps.

## Data caching state (this session updates)

- **Pantheon+SH0ES canonical cache** at `data/pantheon_plus/` — `.dat` (579 KB, regular git) + `.cov` (33 MB, git-LFS) + `README.md` with re-download instructions and MD5 checksums. Required by `c5_pantheon_bulk_flow_tightening.py` driver; tracked for E1b-prime reproducibility + future SDSS DR17 cross-check. LFS filter at `.gitattributes` + gitignore allowlist override of `data/*` pattern.

## Reference paths (canonical, tracked)

| Path | Purpose |
|---|---|
| [`_orchestration/section-e-cascade.md`](section-e-cascade.md) | Active Section E epic (E1b-prime CLOSED; SDSS DR17 spawned as separate epic) |
| [`_orchestration/h-infinity-downstream-cascade.md`](h-infinity-downstream-cascade.md) | ACTIVE — 5 surfaced anomalies + Class E reclassification |
| [`_orchestration/c5-sdss-dr17-spin-orientation.md`](c5-sdss-dr17-spin-orientation.md) | QUEUED — scope adjudication pending |
| [`_orchestration/cosmic-axis-glossary.md`](cosmic-axis-glossary.md) | CLOSED 2026-05-19 EOD (audit tag `audit/2026-05-19_cosmic-axis-glossary`) |
| [`_orchestration/h-infinity-derivation-audit.md`](h-infinity-derivation-audit.md) | CLOSED 2026-05-19 EOD (audit tag `audit/2026-05-19_h-infinity-derivation-audit`) |
| [`_orchestration/h-infinity-framing-forward.md`](h-infinity-framing-forward.md) | CLOSED 2026-05-19 EOD (audit tag `audit/2026-05-19_h-infinity-framing-forward`) |
| [`_orchestration/README.md`](README.md) | Convention doc for this directory (updated 2026-05-19 EOD with worktree-isolation discipline) |
| [`CLAUDE.md`](../CLAUDE.md) | AVE-Core agent orientation (updated 2026-05-19 EOD with pre-commit branch-check + audit-tag count 24) |
| [`manuscript/ave-kb/CLAUDE.md`](../manuscript/ave-kb/CLAUDE.md) | Cross-cutting KB invariants |
| [`manuscript/ave-kb/common/divergence-test-substrate-map.md`](../manuscript/ave-kb/common/divergence-test-substrate-map.md) | 33-row experimental-claim landscape; C5 row at Marginal-D post-E1b-prime |
| [`manuscript/ave-kb/common/closure-roadmap.md`](../manuscript/ave-kb/common/closure-roadmap.md) | Running changelog |
| [`manuscript/ave-kb/common/cosmic-axes-and-frames-glossary.md`](../manuscript/ave-kb/common/cosmic-axes-and-frames-glossary.md) | Canonical K4 rest frame ↔ Ω_freeze definitional leaf (NEW 2026-05-19 EOD) |
| [`data/pantheon_plus/README.md`](../data/pantheon_plus/README.md) | Pantheon+SH0ES canonical cache + re-download instructions |
| `git tag -l "audit/*"` | 24 immutable audit tags |
| [`.agents/handoffs/`](../.agents/handoffs/) | Ephemeral scratch (gitignored; NOT canonical — see `_orchestration/` for tracked state) |

## Playbook for the next orchestration session

1. **First read**: this file (`index.md`) + the relevant active epic doc(s).
2. **Phase 0 state verification**:
   - `git log analysis/integration -1 --oneline` should match the HEAD listed above (or have advanced)
   - `git tag -l "audit/*" | wc -l` should match (or have advanced)
   - `git branch --show-current` should report `analysis/integration` — if not, switch before any commit per CLAUDE.md "Pre-commit discipline" section
3. **Don't trust corpus-state claims here without re-verifying** (per `verify-before-cite` v1.3 trigger 7 + 8): facts here are accurate as of the Last-updated date; if days/weeks later, re-verify via `git log --since=<date>` + cross-branch `git log --all` + `git branch --contains <hash>` for commit-application claims.
4. **Ask Grant**: which item from "Open decisions" to action first. Default if not specified: priority ladder item 1 (H_∞ downstream cascade).
5. **For implementor-session kickoff**: append a `## Phase X (PENDING)` section to the relevant epic doc with assumptions A1-AN, scope boundary, phase plan, adjudication criteria, verification — that's the implementor briefing. Spawn `ave-implementer` agent with `isolation: "worktree"` per `_orchestration/README.md` "Spawning implementors via the Agent tool — discipline" section.

## Pure-AVE-corpus rule

All content in this directory is pure physics. No external context (no investor / fund / interview references). Tracked files MUST be scrubbed before commit.
