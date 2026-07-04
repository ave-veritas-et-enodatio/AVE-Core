# Repo Formatting & Cleanup Audit Epic — tracker + P0 brief

**Status:** ACTIVE — P0 IN-FLIGHT (owner: orchestration session, opened 2026-07-04)
**Scope class:** ORGANIZATION AND FORMATTING ONLY — never content deletion.
**Merge discipline:** all changes via reviewed PRs (`[REVIEW: pending-orchestrator]` header), no self-merge, audit-tag-then-delete on merged branches.

## Governing constraints (verified at HEAD `43d53e06`, 2026-07-04)

These were inventoried 2026-07-03/04 and re-verified at HEAD by the orchestrator before P0 dispatch. Cite these numbers, not the inventory's approximations.

- **The corpus content is LOAD-BEARING.** 523 active docs in flat `research/` (147 more under `research/_archive/`). 149 distinct research docs are hard-linked from `manuscript/ave-kb/` — `verify-md-links` gates those as HARD errors. ~476 distinct `research/*.md` paths are referenced from outside `research/` (grep over `manuscript/ _orchestration/ src/ papers/ docs/ README.md`; second-method caveat applies — treat as scale, not exact). **Every move must be link-coupled**: move + citation update in the same commit, gates green.
- **Honesty-trail docs are UNTOUCHABLE.** RETRACTED / walk-back / correction records and frozen preregs of live claims are never archived away from a live claim. Git history is the audit trail — no in-doc preservation banners.
- **`research/_archive/` is the archive tier** — in `verify-md-links` `SKIP_DIRS` (`tools/verify-md-links.py:65`, `_archive` at any depth).
- **The claim-id spine (`clm-`/`exp-`/`sup-`/`def-`/`ilk-`, INVARIANT-S8..S13) is healthy, CI-enforced, and OUT OF SCOPE.**
- **Input artifacts, all merged:** PR #502 (engine-capability refresh + branch-triage table + figure policy + 182 MB figure disposition), PR #501 (README refresh; flagged the badge/manifest split). Audit tags on origin: 213.
- **Pure-AVE-corpus rule** applies to every tracked file, commit message, and branch name in this epic.

## Phase plan

| Phase | Content | Lane shape | Gate |
|:--|:--|:--|:--|
| **P0** | Conventions ratification — `_orchestration/2026-07_repo-conventions.md` | 1 implementor | **GRANT RATIFIES before P1** |
| **P1** | Mechanical lint sweep — read-only auditor lanes, disposition tables only. Lane (a) = citation-currency (stale `file:line` cites corpus-wide; known drift class incl. the forward-prediction-register provenance re-grep already queued at `index.md:44`). | 3–4 parallel read-only auditors | Lanes (b)+ spec to be confirmed at P0 ratification |
| P2+ | To be confirmed at P0 ratification | — | — |

> **Spec-currency note:** the P1 lane list beyond (a) and all later phases are to be re-confirmed with Grant at P0 ratification before any P1 dispatch.

---

## P0 brief — conventions doc (PENDING → IN-FLIGHT 2026-07-04)

**Deliverable:** `_orchestration/2026-07_repo-conventions.md` — a PROPOSED conventions document, each section ending in an explicit **RATIFY:** block (inline prose, bulleted options where a real choice exists, recommended default marked). Nothing in the doc executes anything; execution phases follow ratification. The doc must be pure process/formatting — no physics adjudications.

**Branch:** `analysis/2026-07-04-repo-conventions` off `origin/main`. Worktree-isolated. Incremental-write discipline: skeleton commit first, then one section per commit.

**Also include in the same PR:** commit this tracker file (it is an untracked seed in the main checkout at write time).

### Section specs (verified HEAD inputs per section)

**(a) Figure placement.** Formalize the PR #502 policy: cited figures belong in per-volume `figures/` dirs; `_output/` = gitignored scratch. Verified inputs: `.gitignore:52` ignores `src/scripts/**/_output/`; the allowlist below it (~30 `!src/scripts/...` lines) un-ignores cited renders; `.gitignore:59` already names the policy smell verbatim ("cited renders belong in `figures/`, not `_output/`"). At HEAD there are **36** tracked files under `src/scripts/vol_9_device/_output/**` (the 2026-07-03 inventory said 38 — stale; use HEAD truth) and 79 tracked under all `src/scripts` output dirs. Per-volume `figures/` dirs exist for every manuscript volume + `ave-kb/common/figures/`. Known `.md` citers of `vol_9_device/_output` paths: `manuscript/ave-kb/common/engine-capability-map.md:320`, `manuscript/ave-kb/vol9/ch3-pin-port-configuration/vacuum-node-im3-distortion.md:14` — the doc must spec a FULL citer inventory (`.md` + `.tex` + `.py`) as step 1 of the migration procedure. The migration itself EXECUTES in a later phase; this section SPECIFIES target layout, the link-coupled move procedure (move + cite update, same commit, gates green), and the data-artifact question (`.json` results in `_output/`, e.g. `birefringence_hibef_scenario_predictions.json` — figure policy vs data policy are distinct; propose the split).

**(b) `research/` naming + organization grammar.** 523 active docs, flat dir. Observed grammar: `YYYY-MM-DD_<slug>_<type>.md`, `<type>` ∈ {prereg, result, note, ruling, synthesis, registered, prereg_FROZEN, …} — plus undated registers (e.g. `2026-06-24_forward-prediction-register.md` is dated but register-class; some docs have no type suffix). Formalize: date-prefix rules, the type-suffix vocabulary, when undated/register-class names are allowed, the flat-dir policy (recommend keep-flat with grammar, vs subdirs — state trade-offs), and archive-tier criteria: what MAY move to `research/_archive/` (superseded AND not cited by any live claim AND not honesty-trail), what NEVER moves (honesty-trail docs; anything hard-linked from ave-kb unless the link moves in the same commit). Restate the link-coupling requirement with the HEAD numbers above.

**(c) `_orchestration/` lifecycle.** Active/closed/archived epic-doc states + a currency rule. Verified inputs: `index.md` is 785 lines carrying embedded staleness notices (`:3` audit-trail note, `:6` staleness notice) — lifecycle is currently in-place prose warnings; `_orchestration/_archive/` exists. Live-fire precedent for the currency rule: `2026-06-07_electron-synthesis-epic.md` §37 (~line 315–319) carried the G2 channel→DOF diagnosis later REFUTED — the correction landed as an append-only 🔴 RESOLUTION note (2026-07-03), the right pattern. Propose: a mandatory status header on every epic doc (ACTIVE / CLOSED / ARCHIVED-to-`_archive/` + last-verified date), the append-only correction pattern as the standing fix for stale physics framings in epic docs (git is the trail — no banners), and an `index.md` hygiene rule (when superseded sections migrate to `_archive/index-stale.md`).

**(d) Branch lifecycle SLA.** Audit-tag-then-delete is standing (CLAUDE.md pattern; 213 `audit/*` tags on origin at HEAD) — restate, then ADD staleness limits: resumable branches (e.g. the four 2026-06-11 resumable branches listed at `index.md` §2026-06-11, now ~3 weeks old) must be re-affirmed in the tracker or audit-tagged + deleted after a proposed N days; pushed branches with no PR triaged within a proposed M days. Consume the PR #502 branch-triage table as input. Propose concrete N/M values as the RATIFY choice.

**(e) Status-marker grammar.** RUNNING / PENDING / IN-FLIGHT / MID-FLIGHT markers in `_orchestration/` and `research/` must carry owner + date (+ optionally a stale-after horizon); grammar must be lintable (propose the regex + a CI or `make` lint target; scope `_orchestration/**.md` + `research/**.md`, excluding `_archive`). Live-fire precedent (verified): the 2026-06-22 birefringence arc's RUNNING markers masked a dead workflow until 2026-07-03 (~12 days; closed by `0b82e3f2` "reconcile stale arc tracker" — `2026-06-22_birefringence-vca-bench-arc.md:75` now records both workflows CLOSED). Informal owner+date markers already occur (e.g. "PENDING, Grant-gated") — codify the existing practice, don't invent a new one.

**(f) Badge/manifest accounting rule.** Verified split: `README.md:6` badge says `predictions-47_derived`; `manuscript/predictions.yaml` has **36** entries, validated by `src/scripts/predictions_manifest_validator.py` (+ `src/tests/test_predictions_manifest_validator.py`). Different accountings — flagged in PR #501, never reconciled into a rule. The rule must: name each public surface's accounting basis (what the badge counts, what the manifest validates, what the README Master Prediction Table rows count), require every public-facing count to name its basis, and propose a drift gate (badge number derived from a named source, or a documented 47↔36 mapping with the delta enumerated). If cheap, enumerate the 47-vs-36 delta as a disposition table (READ-ONLY — any fix lands post-ratification).

### Out of scope for P0

- Executing ANY move, rename, archive, or fix — the doc proposes; ratification gates execution.
- Claim-id spine, KB frontmatter, solidity machinery (INVARIANT-S8..S13) — healthy, CI-enforced.
- Physics content of any doc touched — this epic never adjudicates physics.

### Gates before PR

`make verify-md-links` and `make verify-kb-metadata` green from the worktree. Every `file:line` cite in the conventions doc grep-verified at the worktree's HEAD (verify-before-cite).

---

## Log

- **2026-07-04** — Epic opened. Governing constraints re-verified at HEAD `43d53e06` (two corrections vs the inventory: vol_9_device tracked output figures = 36 not 38; audit tags = 213 not ~200). P0 implementor dispatched (background, worktree-isolated, branch `analysis/2026-07-04-repo-conventions`).
