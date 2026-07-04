# Repo Formatting & Cleanup Audit Epic — tracker + P0 brief

**Status:** ACTIVE — P0 IN-FLIGHT (owner: orchestration session, opened 2026-07-04)
**Scope class:** ORGANIZATION AND FORMATTING ONLY — never content deletion.
**Merge discipline:** all changes via reviewed PRs (`[REVIEW: pending-orchestrator]` header), no self-merge, audit-tag-then-delete on merged branches.
**Cost envelope (disclosed at kickoff):** ~7–9 agent arcs total across P0–P4; P2 is the only phase that blocks on Grant.

## Governing constraints (verified at HEAD `43d53e06`, 2026-07-04)

Inventoried 2026-07-03/04, re-verified at HEAD by the orchestrator before P0 dispatch. Cite these numbers, not the inventory's approximations.

- **The corpus content is LOAD-BEARING.** 523 active docs in flat `research/` (147 more under `research/_archive/`). 149 distinct research docs are hard-linked from `manuscript/ave-kb/` — `verify-md-links` gates those as HARD errors. ~476 distinct `research/*.md` paths are referenced from outside `research/` (grep over `manuscript/ _orchestration/ src/ papers/ docs/ README.md`; second-method caveat applies — treat as scale, not exact). **Every move must be link-coupled**: move + citation update in the same commit, gates green.
- **Honesty-trail docs are UNTOUCHABLE.** RETRACTED / walk-back / correction records and frozen preregs of live claims are never archived away from a live claim. Git history is the audit trail — no in-doc preservation banners.
- **`research/_archive/` is the archive tier** — in `verify-md-links` `SKIP_DIRS` (`manuscript/ave-kb/tools/verify-md-links.py:65`, `_archive` at any depth).
- **The claim-id spine (`clm-`/`exp-`/`sup-`/`def-`/`ilk-`, INVARIANT-S8..S13) is healthy, CI-enforced, and OUT OF SCOPE.**
- **Input artifacts, all merged:** PR #502 (engine-capability refresh + 49-branch triage §D2 + figure policy + 182 MB figure disposition §D3), PR #501 (README refresh; flagged the badge/manifest split). Audit tags on origin: 213.
- **PR #502 §D2 verified at HEAD:** 50 unmerged remote branches at audit start, 6 executed (tag-tip-then-delete), **44 remain dispositions-only** — origin has exactly 44 non-main branches today. Three families hold result docs NOT in main (keystone substrate-pump u=29, passive-eigenmode u=50/31, boundary-MQJ stage1.5/1.6) — land-vs-archive is a physics-history Grant call (P2).
- **PR #502 §D3 verified:** ~106 UNCITED orphan-non-regenerable artifacts = GRANT-CALL bucket (not auto-deleted).
- **Pure-AVE-corpus rule** applies to every tracked file, commit message, and branch name in this epic.

## Phase plan (execute in order; Grant gates marked)

| Phase | Content | Lane shape | Gate |
|:--|:--|:--|:--|
| **P0** | Conventions ratification — `_orchestration/2026-07_repo-conventions.md` (sections a–f, RATIFY blocks) | 1 implementor | **GRANT RATIFIES before P1** |
| **P1** | Mechanical lint sweep — read-only, disposition tables only: **(a)** citation-currency (stale `file:line` cites corpus-wide; known drift class — the forward-prediction-register provenance re-grep queued at `index.md:44` is an instance); **(b)** stale-marker sweep vs the P0 grammar; **(c)** figure/artifact placement vs P0 rules + the ~106 orphan GRANT-CALL bucket (PR #502 §D3); **(d)** format consistency — repo-root `CLAUDE.md` currency (branching section + `CLAUDE.md:87` "109 audit tags" vs 213 actual), `.tex` conventions spot-check, README accounting | 3–4 parallel read-only auditors | — |
| **P2** | Grant adjudication batch — zero agents; assemble pre-built one-word-per-row tables: the 44 unmerged-branch dispositions (PR #502 §D2; 3 result-doc families are physics-history calls), the ~106 orphans, the predictions-count accounting, orchestration-doc dispositions | orchestrator only | **GRANT RULES — the only phase that blocks on him** |
| **P3** | Execution — link-coupled moves per ratified dispositions; branch land-or-tag-and-delete per P2 rulings; marker reconciliation; figure migration. Bounded per-domain PRs, never one mega-PR. Gates green per commit (`make verify` + `verify-kb-metadata` + `verify-md-links`) | 2–3 implementors | **COLLISION GUARD re-run immediately before dispatch** (see below) |
| **P4** | Enforcement — lint additions to the verify chain: stale-marker linter, figure-placement checker, badge-manifest consistency, sampled citation-currency check; PROPOSE (do not create without Grant) a monthly hygiene routine on the scheduler | 1 implementor | Grant approves the routine before creation |

### Collision guard (P3 precondition)

Check for live physics arcs before P3: `git branch -r` for `analysis/*` newer than this session + local worktree activity. **State at 2026-07-04 kickoff:** `analysis/srs-chiral-micropolar` and `analysis/seven-family-cleanup` (named at scoping as in-flight) both sit at `43d53e06` = main HEAD with **zero unique commits** — placeholder worktrees from the closed 2026-07-03 session, not live arcs. Newest remote `analysis/*` tip is 2026-06-30. Collision risk currently LOW; re-verify at P3 dispatch time regardless. Do not run P3 concurrent with heavy corpus-writing arcs.

### Standing disciplines (all phases)

verify-before-cite on every claim carried into dispositions · two-method completeness on any "all/none/complete" sweep claim (live instance this session: a single grep of the PR #502 §D2 table silently missed 2 of 3 GRANT-CALL family rows; the direct read caught them) · flag-don't-fix (surface, Grant rules) · KEEP-BOTH for any convention change touching frozen documents · sober reporting — state/evidence/risks/options/recommendation-last, no urgency language on merge advice.

---

## P0 brief — conventions doc (IN-FLIGHT 2026-07-04)

**Deliverable:** `_orchestration/2026-07_repo-conventions.md` — a PROPOSED conventions document, each section ending in an explicit **RATIFY:** block (inline prose, bulleted options where a real choice exists, recommended default marked). Nothing in the doc executes anything; execution phases follow ratification. The doc must be pure process/formatting — no physics adjudications.

**Branch:** `analysis/2026-07-04-repo-conventions` off `origin/main`. Worktree-isolated. Incremental-write discipline: skeleton commit first, then one section per commit.

**Also include in the same PR:** commit this tracker file (it is an untracked seed in the main checkout at write time).

### Section specs (verified HEAD inputs per section)

**(a) Figure placement.** Formalize the PR #502 policy: cited figures belong in per-volume `figures/` dirs; `_output/` = gitignored scratch. Verified inputs: `.gitignore:52` ignores `src/scripts/**/_output/`; the allowlist below it (~30 `!src/scripts/...` lines) un-ignores cited renders; `.gitignore:59` already names the policy smell verbatim ("cited renders belong in `figures/`, not `_output/`"). At HEAD there are **36** tracked files under `src/scripts/vol_9_device/_output/**` (the 2026-07-03 inventory said 38 — stale; use HEAD truth) and 79 tracked under all `src/scripts` output dirs. Per-volume `figures/` dirs exist for every manuscript volume + `ave-kb/common/figures/`. Known `.md` citers of `vol_9_device/_output` paths: `manuscript/ave-kb/common/engine-capability-map.md:320`, `manuscript/ave-kb/vol9/ch3-pin-port-configuration/vacuum-node-im3-distortion.md:14` — the doc must spec a FULL citer inventory (`.md` + `.tex` + `.py`) as step 1 of the migration procedure. The migration itself EXECUTES in P3; this section SPECIFIES target layout, the link-coupled move procedure (move + cite update, same commit, gates green), and the data-artifact question (`.json` results in `_output/`, e.g. `birefringence_hibef_scenario_predictions.json` — figure policy vs data policy are distinct; propose the split).

**(b) `research/` naming + organization grammar.** 523 active docs, flat dir. Observed grammar: `YYYY-MM-DD_<slug>_<type>.md`, `<type>` ∈ {prereg, result, note, ruling, synthesis, registered, prereg_FROZEN, …} — plus register-class docs and docs with no type suffix. Formalize: date-prefix rules, the type-suffix vocabulary, when register-class names are allowed, the flat-dir policy (recommend keep-flat with grammar, vs subdirs — state trade-offs), and archive-tier criteria: what MAY move to `research/_archive/` (superseded AND not cited by any live claim AND not honesty-trail), what NEVER moves (honesty-trail docs; anything hard-linked from ave-kb unless the link moves in the same commit). Restate the link-coupling requirement with the HEAD numbers above.

**(c) `_orchestration/` lifecycle.** Active/closed/archived epic-doc states + a currency rule. Verified inputs: `index.md` is 784 lines carrying embedded staleness notices (`:3` audit-trail note, `:6` staleness notice) — lifecycle is currently in-place prose warnings; `_orchestration/_archive/` exists. Live-fire precedent for the currency rule: `2026-06-07_electron-synthesis-epic.md` §37 (~line 315–319) carried the G2 channel→DOF diagnosis later REFUTED — the correction landed as an append-only 🔴 RESOLUTION note (2026-07-03), the right pattern. Propose: a mandatory status header on every epic doc (ACTIVE / CLOSED / ARCHIVED-to-`_archive/` + last-verified date), the append-only correction pattern as the standing fix for stale physics framings in epic docs (git is the trail — no banners), and an `index.md` hygiene rule (when superseded sections migrate to `_archive/index-stale.md`).

**(d) Branch lifecycle SLA.** Audit-tag-then-delete is standing (CLAUDE.md pattern; 213 `audit/*` tags on origin at HEAD) — restate, then ADD staleness limits: resumable branches must be re-affirmed in the tracker or audit-tagged + deleted after a proposed N days; pushed branches with no PR triaged within a proposed M days. Consume the PR #502 §D2 branch-triage table as input (44 branches, dispositions-only — the dispositions themselves are P2 Grant calls, NOT this doc's job; this doc sets the standing SLA). Propose concrete N/M values as the RATIFY choice.

**(e) Status-marker grammar.** RUNNING / PENDING / IN-FLIGHT / MID-FLIGHT markers in `_orchestration/` and `research/` must carry owner + date (+ optionally a stale-after horizon); grammar must be lintable (propose the regex + a `make` lint-target sketch — spec only, target lands in P4; scope `_orchestration/**.md` + `research/**.md`, excluding `_archive`). Live-fire precedent (verified): the 2026-06-22 birefringence arc's RUNNING markers masked a dead workflow until 2026-07-03 (~12 days; closed by `0b82e3f2` "reconcile stale arc tracker" — `_orchestration/2026-06-22_birefringence-vca-bench-arc.md:75` now records both workflows CLOSED). Informal owner+date markers already occur (e.g. "PENDING, Grant-gated") — codify the existing practice, don't invent a new one.

**(f) Badge/manifest accounting rule.** Verified split: `README.md:6` badge says `predictions-47_derived`; `manuscript/predictions.yaml` has **36** entries, validated by `src/scripts/predictions_manifest_validator.py` (+ `src/tests/test_predictions_manifest_validator.py`). Different accountings — flagged in PR #501, never reconciled into a rule. The rule must: name each public surface's accounting basis (what the badge counts, what the manifest validates, what the README Master Prediction Table rows count), require every public-facing count to name its basis, and propose a drift gate (badge number derived from a named source, or a documented 47↔36 mapping with the delta enumerated). If cheap, enumerate the 47-vs-36 delta as a disposition table (READ-ONLY — any fix lands in P3 after the P2 predictions-count adjudication).

### Out of scope for P0

- Executing ANY move, rename, archive, or fix — the doc proposes; ratification gates execution.
- Branch dispositions (P2), orphan dispositions (P2), predictions-count adjudication (P2).
- Claim-id spine, KB frontmatter, solidity machinery (INVARIANT-S8..S13) — healthy, CI-enforced.
- Physics content of any doc touched — this epic never adjudicates physics.

### Gates before PR

`make verify-md-links` and `make verify-kb-metadata` green from the worktree. Every `file:line` cite in the conventions doc grep-verified at the worktree's HEAD (verify-before-cite).

---

## Log

- **2026-07-04** — Epic opened. Governing constraints re-verified at HEAD `43d53e06` (corrections vs the inventory: vol_9_device tracked output figures = 36 not 38; audit tags = 213 not ~200; `CLAUDE.md:87` still says 109 — P1(d) item). P0 implementor dispatched (background, worktree-isolated, branch `analysis/2026-07-04-repo-conventions`).
- **2026-07-04** — Full phase spec (P1 lanes a–d, P2–P4, collision guard, disciplines) recorded. PR #502 §D2 verified: 44 branches dispositions-only, 3 result-doc GRANT-CALL families confirmed verbatim (keystone u=29, passive-eigenmode u=50/31, boundary-MQJ). §D3 ~106 orphans GRANT-CALL confirmed. Collision guard: the two scoping-time in-flight branches hold zero unique commits at HEAD (placeholder worktrees from the closed 2026-07-03 session); newest remote analysis/* tip = 2026-06-30; P3 collision risk LOW, re-check at P3 dispatch.
- **2026-07-04** — P0 delivered: PR #510 open (`analysis/2026-07-04-repo-conventions`, 7 commits, skeleton-then-one-section-per-commit held; `verify-md-links` + `verify-kb-metadata` EXIT=0). Orchestrator review: doc verified read-and-run (47↔36 closure independently re-computed from `predictions.yaml` — 33 numbered entries expand to exactly 1–47 + 3 `P_A034_*` = 36 ✓). Five brief-vs-HEAD divergences ledgered by the implementor (two brief path-prefix errors, resumable-branch count 3 not 4, index.md 784 not 785, pre-existing `CLAUDE.md:87`/`.gitignore:59` drift → P1(d)/P3 items); this tracker carries the corrected values. Awaiting Grant ratification of the six RATIFY blocks.
