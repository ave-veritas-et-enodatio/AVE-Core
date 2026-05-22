# L5 — Living Documentation Trackers

Read-only synthesis layer over `research/L3_electron_soliton/`. Tracks what the active research thread is producing that the manuscript or engine has not yet absorbed. **Source docs are not edited from this layer** — all writes happen here, all reads happen there.

**Last comprehensive sweep:** 2026-05-15. Post-sweep state:
- Added E-094 through E-101 (8 new entries) covering post-2026-05-02 canonical work — substrate-vocabulary discipline (App G propagation), Master Equation FDTD canonical engine, boundary-envelope reformulation, two-engine architecture, cubic K4 anisotropy, k4_tlm.py v14 additions, three substrate invariants observables module.
- Added A-026, A-027, A-028 (3 new axiom-status entries) capturing canonical closures: substrate-observability rule (Grant-confirmed via boundary-envelope reformulation); two-engine architecture (Master Equation FDTD + K4-TLM cover disjoint operating regimes); three substrate invariants $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ as canonical boundary observables (Grant Q1 closure).
- `terminology_canonical.md` §0 added with AVE-QED App G three-column substrate-native/EE/ME vocabulary as canonical reference + three substrate invariants table + substrate-observability rule statement.
- Living tracker rows added for docs 109-114 (post-2026-05-02 canonical work).
- Cross-repo references updated with AVE-QED + AVE-Bench-VacuumMirror citations.

**Upstream canonical for substrate vocabulary:** AVE-QED `manuscript/vol_qed_replacement/appendices/G_substrate_vocabulary.tex` (App G, 7 sections, ~340 lines, committed `ce34645` 2026-05-14). All L5 entries authored or refreshed during this sweep use App G substrate-native vocabulary (substrate / node / bond / state / boundary / envelope / linking $\mathcal{Q}$ / winding $\mathcal{J}$ / integrated strain integral $\mathcal{M}$) where the projection-frame names would obscure the substrate-native concept.

## Files

| File | Purpose |
|---|---|
| [`living_documentation_tracker.md`](living_documentation_tracker.md) | Index of every L3 source doc with its last commit SHA and last-reviewed SHA. Also holds the **Clash registry** (`C-NNN`) and **Internal-retraction log**. The mismatch between Last-commit and Last-reviewed flags docs needing re-sweeping. |
| [`manuscript_pending.md`](manuscript_pending.md) | Nested outline mirroring `manuscript/vol_*/chapters/`. Each pending change clusters under its target chapter (and section, when known). Includes top-level repo docs (README, LIVING_REFERENCE, CLAUDE.md, CURRENT_STATE) at the bottom. |
| [`engine_pending.md`](engine_pending.md) | Nested outline mirroring `src/ave/`. Each pending change clusters under its target file (and symbol). Also tracks `manuscript/predictions.yaml` and significant driver scripts. |
| [`axiom_derivation_status.md`](axiom_derivation_status.md) | Framework-level claims about **what derives what** — axiom-derived vs calibration vs imported vs open derivation gap. Tracks load-bearing meta-claims (e.g., "α is a calibration input, not derived"; "first-law T·dS=dE doesn't close axiom-first") that don't belong to a single chapter. Uses `A-NNN` IDs (independent namespace from `E-NNN`). |
| [`terminology_canonical.md`](terminology_canonical.md) | SM/QFT/CondMat/EE → AVE-native translation table. Watch list for `(CREEPER)` framings that recur incorrectly across sessions. |
| [`cross_repo_references.md`](cross_repo_references.md) | Catalog of every sibling-repo path cited by L3 docs and L5 entries (AVE-Protein, AVE-Propulsion, AVE-PONDER, AVE-HOPF, AVE-VirtualMedia, AVE-APU, AVE-Fusion). Sibling repos evolve independently; this file gives a sweepable surface to verify cited paths still resolve. |

## Entry schema (manuscript + engine)

```
- **[E-NNN] <short concept title>**
  - **Sources:** doc_NN §X.Y:L## (`<sha>`, YYYY-MM-DD); doc_MM §A.B:L## (`<sha>`, YYYY-MM-DD)
  - **Action:** <what specifically changes>
  - **Tests needed:** (engine entries only, optional) <new test files; updated existing tests; regression risks; performance/timing benchmarks if relevant>
  - **Status:** queued | in-review | applied (`<sha>`) | superseded (`E-MMM`) | adjudication-open
  - **Cross-refs:** E-NNN, E-MMM
  - **Conflicts:** (optional) doc_NN §X claims P; doc_MM §Y claims ¬P. Resolution: <canonical claim, or "open adjudication", or "see clash C-NNN in index">
  - **Supersedes / Superseded-by:** (optional) E-NNN with retraction commit `<sha>`
```

The `Tests needed:` field is mandatory for engine entries that change behavior (new function, modified algorithm, new constant). Skip it for pure docstring/comment additions. Cross-reference test files in `src/tests/` by name.

`E-NNN` IDs are monotonic and **shared across `manuscript_pending.md` and `engine_pending.md`** so cross-references are unambiguous. Next free ID is recorded at the bottom of `manuscript_pending.md`.

**When a source doc internally retracts content** (per COLLABORATION_NOTES rule 12 — retraction preserves the original body, rationale goes in the section header), cite the live (post-retraction) section in `Sources` and note the retraction explicitly in `Conflicts`. Do not cite a section that has been struck through or marked retracted as if it were canonical.

**When two source docs disagree on a substantive claim**, register the clash in the **Clash registry** of `living_documentation_tracker.md` with a `C-NNN` ID. Reference it from any tracker entry that depends on the unresolved claim.

## Sweep protocol

When reading a source doc to populate trackers:

1. Read the doc.
2. For each manuscript or engine implication:
   - Check `manuscript/...` or `src/ave/...` to confirm the implication is actually pending (the live target may already match).
   - Check `research/L3_electron_soliton/DOCUMENTATION_UPDATES_QUEUE.md` to avoid duplicating an already-captured item.
   - If genuinely new, append a tracker entry under the right destination heading. Use the next free ID.
3. Update the doc's row in `living_documentation_tracker.md`:
   - Set `Last reviewed` to the doc's current `Last commit` SHA.
   - List the new entry IDs in the `Tracker entries` column.

## Status transitions

- `queued` — entry exists, no action taken.
- `in-review` — Grant has surfaced it for adjudication this session.
- `applied (<sha>)` — change landed in target file. Keep entry in place; status field carries the applying commit.
- `superseded (E-MMM)` — a later tracker entry replaces this one. Keep both entries in place; superseded entry stays as audit trail.
- `adjudication-open` — entry depends on an unresolved Clash (see Clash registry). Cannot apply until the clash resolves.

## Discipline

- **Source docs are off-limits.** No edits to `research/L3_electron_soliton/*.md` from this layer.
- **No silent invention.** Every entry has at least one `(doc, section, commit-sha)` tuple in Sources.
- **Re-verify before recommending.** Memory of file content ≠ live state.
- **Don't preemptively populate.** Empty section headings stay empty until earned by a sweep.

## Deferred coverage (tracked here so it isn't forgotten)

Promote any of these to its own file when the volume grows enough to warrant it. Currently absorbed inside existing entries or skipped:

- **CI workflows** (`.github/workflows/`). `build_pdf.yml` is empty (CURRENT_STATE flagged this); `verify.yml` covers regression gates. New tracker entry can land in `engine_pending.md` under a `## CI / GitHub Actions` section when needed.
- **Audit playbooks** (`.agents/workflows/audit-*.md` + `peer-review.md`). Referenced from many docs as authoritative methodology. When a tracker entry lands changes that affect a playbook's known-stale list (e.g., fixing a numeric value the audit-math playbook flags), update the playbook in the same commit. Currently NOT a separate file.
- **`predictions.yaml` lifecycle tracking.** Each pre-registered `P_xxx` has a lifecycle: registered → tested → passed/falsified/null. Currently absorbed inside the engine entry that registers/retracts/tests a prediction, with the `Status:` field carrying the outcome. Promote to a `predictions_lifecycle.md` if the count grows past ~20 actively-tested preds.
- **Driver scripts in `src/scripts/`.** Most are research one-offs; not tracked. When a driver gets promoted to the canonical `make verify` chain or reused across sessions, file an engine entry under the `### `src/scripts/vol_*/` driver scripts` section.

These are explicit non-decisions: we know they exist, we've decided not to add layers for them yet, and we know what would trigger promotion.
