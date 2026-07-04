# Repo Formatting & Cleanup Conventions — PROPOSED (P0 deliverable)

**Status:** PROPOSED — awaiting Grant ratification (owner: P0 implementor, drafted 2026-07-04). Last-verified HEAD: `43d53e06`.
**Scope class:** ORGANIZATION AND FORMATTING ONLY — this document proposes conventions; it executes no move, rename, archive, or fix. Every execution phase is gated on Grant ratifying the relevant **RATIFY:** block below.
**Merge discipline:** lands via a reviewed PR (`[REVIEW: pending-orchestrator]`), no self-merge, per CLAUDE.md branching pattern.

> **What this doc is NOT.** It is not a physics adjudication, not a claim-id-spine change, not a KB-frontmatter change. The claim-id spine (`clm-`/`exp-`/`sup-`/`def-`/`ilk-`, INVARIANT-S8..S13) and solidity machinery are healthy + CI-enforced and OUT OF SCOPE. Nothing here touches content — only where files live, how they are named, and how their status is marked.

## How to read the RATIFY blocks

Each section (a)–(f) ends in a **RATIFY:** block written as inline prose. Where a real choice exists, options are bulleted and a recommended default is marked **[RECOMMENDED]**. Grant adjudicates in prose (no multi-choice UI). Until a block is ratified, the section is a proposal with no executable force.

## Cross-cutting invariants (apply to every section)

1. **Organization/formatting only — never content deletion.** No section may propose deleting or gutting a doc's content.
2. **Honesty-trail docs are UNTOUCHABLE.** RETRACTED / walk-back / correction records and frozen preregs of live claims are never archived away from a live claim, never rewritten, never banner-stamped. (Restated in full in section (b).)
3. **Git history is the audit trail.** No convention may introduce in-doc preservation banners. Corrections land append-only (the pattern codified in section (c)).
4. **Every move is link-coupled.** Any file move executes as move + citation update in the SAME commit, with `make verify-md-links` + `make verify-kb-metadata` green in that commit. (HEAD numbers in section (b).)
5. **Pure-AVE-corpus rule.** Every tracked file, commit message, and branch name stays pure physics/process — no external/non-physics context.

---

## (a) Figure placement

**Governing principle (formalizes the PR #502 policy).** Cited render targets belong in tracked per-volume `figures/` directories. `_output/` (and `outputs/`, `simulations/outputs/`) are gitignored scratch — a driver's regeneration workspace, not a citation surface. A figure a manuscript / KB / research doc cites must live where a clean-worktree build keeps it tracked.

### The current state (HEAD `43d53e06`)

- `.gitignore:52` ignores `src/scripts/**/_output/`. `.gitignore:59` already names the policy smell verbatim: `# pre-existing policy smell: cited renders belong in figures/, not _output/;`. An allowlist of `!src/scripts/...` un-ignore lines below it force-tracks the cited renders that currently live in scratch dirs, so a regenerate-then-readd does not silently drop them.
- **36 tracked files** have paths containing both `vol_9_device` and `_output` (recursive / `**` semantics — this includes the nested `vol_9_device/cvr_ee_sweep/_output/` dir). Of these: **20 are figures** (17 `.png` + 3 `.pdf`) and **16 are `.json` data artifacts**. (Note: a non-recursive `git ls-files 'src/scripts/vol_9_device/_output/*'` glob returns only 29 because git's single `*` does not cross into `cvr_ee_sweep/_output/`; the HEAD-true figure-policy count is 36 recursive. The 2026-07-03 inventory's "38" is stale; the `.gitignore:59` comment block's "38 CITED figures" is likewise stale and is itself a policy-smell artifact to be reconciled when the migration executes.)
- **79 tracked files** live under all `src/scripts` output dirs (`_output` + `outputs` + `simulations/outputs`): 48 `.json`, 27 `.png`, 3 `.pdf`, 1 `.cir`.
- Per-volume `figures/` dirs exist for every manuscript volume, plus `manuscript/ave-kb/common/figures/`. These are deliberately NOT ignored (`.gitignore:56-58`).

### The two distinct policies this section proposes (figure vs data)

Figure policy and data policy are **different questions** and must not be collapsed. Example: `src/scripts/vol_9_device/_output/birefringence_hibef_scenario_predictions.json` is a numeric result artifact, not a render; `vacuum-node-im3-distortion.md:14` cites `.../im3_vacuum_harmonic_distortion.json` as the datasheet-characterization result-of-record. A blanket "everything in `_output/` moves to `figures/`" rule would wrongly relocate result JSON into a figures dir.

- **Figure policy (proposed):** cited `.png`/`.pdf`/`.svg` renders move to the citing volume's `figures/` dir (or `ave-kb/common/figures/` for cross-volume). `_output/` holds only regenerable scratch renders no doc cites.
- **Data policy (proposed, OPEN — see RATIFY):** cited `.json`/`.csv` result artifacts are a distinct class. Options: (1) a tracked per-volume `results/` (or `data/`) dir mirroring the `figures/` pattern; (2) keep them tracked-in-place via the `.gitignore` allowlist but require every cited data artifact to be allowlisted with a comment; (3) treat any cited numeric artifact as regenerable and cite the driver + a checked-in expected-value fixture instead of the raw dump.

### The link-coupled migration procedure (specification only — executes post-ratification)

1. **FULL citer inventory first.** Before moving any figure, enumerate every citer across `.md` + `.tex` + `.py` (not just the ave-kb markdown links). At HEAD the citer set for `vol_9_device/_output` paths is broader than the two ave-kb leaves: it includes `manuscript/ave-kb/common/engine-capability-map.md`, `manuscript/ave-kb/vol9/ch3-pin-port-configuration/vacuum-node-im3-distortion.md`, plus research docs (`research/2026-06-10_electron-s11-sweep_result.md`, `2026-06-11_*`, `2026-06-20_*`, `2026-06-21_*`), an orchestration handoff (`_orchestration/2026-06-11_session-handoff.md`), and a driver (`src/scripts/vol_9_device/alpha_boundary_forward_check.py`). Some citers are wildcard-pattern references (`engine-capability-map.md:320` cites `.../_output/*.png`) — those need a rewritten pattern, not a one-file path swap.
2. **Move + all citer updates in ONE commit.** No orphaned citations across a commit boundary.
3. **Update `.gitignore` in the same commit.** Remove the corresponding `!src/scripts/.../_output/...` allowlist line for each moved figure (it is now under a non-ignored `figures/` dir and no longer needs an exception). Reconcile the stale `# EXCEPTIONS — 38 CITED figures...` comment block to HEAD truth.
4. **Gates green in the migration commit:** `make verify-md-links` (HARD on any broken ave-kb→figure link) + `make verify-kb-metadata`.
5. **Driver output-path update.** The generating driver's write path changes from `_output/` to `figures/`; verify the driver still runs and writes to the new tracked location.

**RATIFY:** Adopt "cited renders live in tracked per-volume `figures/`; `_output/`=scratch" as the standing figure policy, with the link-coupled 5-step migration procedure above as the only sanctioned way to execute a move (later phase). The one genuine open choice is the **data-artifact policy** for cited `.json`/`.csv` results:

- **[RECOMMENDED]** Option (1): a tracked per-volume `results/` dir mirroring `figures/`, with the same link-coupled move procedure. Keeps result-of-record artifacts tracked + discoverable + separate from renders, and makes the figure-vs-data split structural rather than convention-by-comment.
- Option (2): keep cited data in-place under `_output/` via the `.gitignore` allowlist, but require a comment on each allowlisted data line naming the citer. Lower churn; keeps the policy-smell (cited artifacts in a dir named "scratch").
- Option (3): forbid citing raw `_output/` dumps; cite the driver + a checked-in expected-value fixture. Cleanest long-term but is the largest content-touching change and edges toward scope beyond formatting — defer unless Grant wants it.

Recommended default for the figure half is not a real fork (adopt as stated); the data half is the decision point.

---

## (b) `research/` naming + organization grammar

_(section body lands in commit 3)_

---

## (c) `_orchestration/` lifecycle + currency rule

_(section body lands in commit 4)_

---

## (d) Branch lifecycle SLA

_(section body lands in commit 5)_

---

## (e) Status-marker grammar (lintable)

_(section body lands in commit 6)_

---

## (f) Badge / manifest accounting rule

_(section body lands in commit 7)_

---

## RATIFY decision list (rollup)

- **(a) Figure placement** — adopt "cited renders → tracked `figures/`, `_output/`=scratch" + the link-coupled 5-step migration; decide the **data-artifact policy** (RECOMMENDED: tracked per-volume `results/` dir).

---

## Appendix — verified-input ledger (HEAD `43d53e06`, 2026-07-04)

Every `file:line` here was grep-verified at this doc's worktree HEAD. Where the brief's cite differed from HEAD truth, the HEAD-true value is recorded and the divergence noted.

**(a) Figure placement**
- `.gitignore:52` = `src/scripts/**/_output/` ✓
- `.gitignore:59` = `# pre-existing policy smell: cited renders belong in figures/, not _output/;` ✓
- 36 tracked files matching `vol_9_device` + `_output` (recursive): 17 `.png` + 3 `.pdf` (20 figures) + 16 `.json` (data). Non-recursive `*` glob returns 29 (does not cross into `cvr_ee_sweep/_output/`).
- 79 tracked under all `src/scripts` output dirs (48 json / 27 png / 3 pdf / 1 cir).
- Full citer set for `vol_9_device/_output` (md+tex+py): `engine-capability-map.md`, `vacuum-node-im3-distortion.md`, 8 research docs, `_orchestration/2026-06-11_session-handoff.md`, `alpha_boundary_forward_check.py`. Brief named only the 2 ave-kb md-link citers.
- `engine-capability-map.md:320` cites `.../_output/*.png` (wildcard pattern) ✓; `vacuum-node-im3-distortion.md:14` cites `.../im3_vacuum_harmonic_distortion.json` (data, not figure) ✓.
- SKIP_DIRS `_archive` at `manuscript/ave-kb/tools/verify-md-links.py:65` ✓ (brief cited path as `tools/verify-md-links.py:65` — the line number is right, the directory prefix in the brief is wrong; true path is `manuscript/ave-kb/tools/`).
