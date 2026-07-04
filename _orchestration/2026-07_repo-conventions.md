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

**The corpus is LOAD-BEARING.** At HEAD: **523 active docs** in flat `research/`, **147 more** under `research/_archive/`. **149 distinct `research/*.md` paths are hard-linked (markdown-link form) from `manuscript/ave-kb/`** — `verify-md-links` gates those as HARD errors. Corpus-wide, `research/*.md` paths are referenced ~**477 times** in bare-token form from outside `research/` (grep over `manuscript/ _orchestration/ src/ papers/ docs/ README.md`; second-method caveat applies — treat as scale, not exact; the markdown-link subset of those is 209). This section formalizes naming so the flat dir stays navigable, and defines the ONLY conditions under which a doc may move to the archive tier.

### Filename grammar

**Canonical form:** `YYYY-MM-DD_<slug>_<type>.md`

- **Date prefix** `YYYY-MM-DD_` — the doc's authoring/registration date, ISO-8601, always present for dated research artifacts (preregs, results, notes). It is the primary sort key in a flat dir and must not be back-dated or edited after the fact (git carries the real history; the filename date is the intended-registration date).
- **Slug** `<slug>` — kebab-case topic, lowercase, hyphen-separated. May itself contain claim/topic tokens (e.g. `alpha-boundary-energy`, `birefringence-vca-bench`).
- **Type suffix** `_<type>` — the artifact class. Observed vocabulary at HEAD (by frequency): `result` (125), `prereg` (91), `note` (16), `synthesis` (2), `ruling`, `registered`, `framing`, `diagnostic`, `design`, `derivation`, `audit`, `adjudication`. Plus lifecycle-state suffixes that ride ON the type: `_FROZEN` (frozen prereg of a live claim — 19 files), `_DRAFT`/`_draft` (in-progress), `_CLOSED`.

**Proposed canonical type vocabulary (closed set — new types are a RATIFY amendment, not an ad-hoc coinage):**
`prereg` · `result` · `note` · `synthesis` · `ruling` · `adjudication` · `audit` · `derivation` · `design` · `diagnostic` · `framing` · `registered`
with lifecycle modifiers `_FROZEN` · `_DRAFT` · `_CLOSED` appended after the type where they apply (e.g. `..._prereg_FROZEN.md`).

**Undated / register-class names — when allowed.** A minority of docs are register-class (living cross-cutting registers, not dated one-shot artifacts) — e.g. `2026-06-24_forward-prediction-register.md` is date-prefixed but register-class (no `_<type>` suffix; the slug ends `-register`). Rule: a register-class doc MAY omit the `_<type>` suffix if its slug ends in a register-class token (`-register`, `-index`, `-glossary`, `-roadmap`, `-plan`, `-ledger`, `-tracker`). It still carries a date prefix. A doc with no date prefix at all is disallowed for new research artifacts (existing undated docs are grandfathered, not renamed — renaming would break the 149 hard links; see below).

### Flat-dir policy

**RECOMMENDED: keep the flat dir, enforce the grammar.** Trade-offs:
- *Keep-flat* — zero link churn (the 149 ave-kb hard links + ~477 corpus-wide references all point at `research/<file>.md`; any subdir move breaks every citer unless link-coupled across the whole corpus). Date-prefix sorting gives a usable chronological spine. Cost: 523 files in one `ls`.
- *Subdirs* (by volume, by topic, or by year) — better `ls`-ergonomics, but every move is a link-coupled corpus-wide rewrite of hundreds of citations, HARD-gated on `verify-md-links`, executed in atomic commits. High risk, low payoff given the date-prefix already provides sort order. Not recommended.

### Archive-tier criteria (`research/_archive/`)

`research/_archive/` is the archive tier and is in `verify-md-links` SKIP_DIRS (`_archive` at any depth — `manuscript/ave-kb/tools/verify-md-links.py:65`), so links INTO it do not gate and links OUT of it are frozen-stale by design.

**A doc MAY move to `research/_archive/` only if ALL of:**
1. It is **superseded** (a later doc carries the current state of its claims), AND
2. It is **not cited by any live claim** (no ave-kb hard link, no live-claim citation — grep the full citer set first), AND
3. It is **not an honesty-trail doc** (see below).

**A doc NEVER moves to archive if ANY of:**
- It is **honesty-trail** — a RETRACTED / walk-back / correction record, or a **frozen prereg of a live claim** (`*_FROZEN.md` of a claim still on the matrix). Honesty-trail docs stay next to the live claim they document. Examples at HEAD: `research/2026-05-17_C14-DAMA_audit_walk-back.md`, the `*_prereg_FROZEN.md` family. These are UNTOUCHABLE — never archived, never rewritten, never banner-stamped (git is the trail).
- It is **hard-linked from ave-kb** (one of the 149) — UNLESS the ave-kb link moves in the SAME commit (link-coupled) and `verify-md-links` stays green. In practice a hard-linked doc is by definition cited by a live claim, so criterion (2) already blocks it; this restates the gate explicitly.

**Link-coupling (restated with HEAD numbers).** Any archive move executes as move + every-citer update in ONE commit, `verify-md-links` + `verify-kb-metadata` green. The 149 ave-kb hard links are HARD-gated; the ~477 corpus-wide references are the broader coupling surface to sweep.

**RATIFY:** Adopt the filename grammar `YYYY-MM-DD_<slug>_<type>.md` with the closed type-vocabulary + lifecycle modifiers above; adopt the register-class exemption; adopt **keep-flat** as the standing dir policy; adopt the 3-of / never-if archive-tier criteria with honesty-trail docs UNTOUCHABLE. Genuine choices:

- **[RECOMMENDED]** Keep-flat with enforced grammar (vs subdirs). Low risk, preserves all links.
- The **type-vocabulary closed set** — Grant should confirm the list is complete or name additions. (RECOMMENDED closed set as listed; new types via amendment.)
- **Grandfathering** existing off-grammar filenames: RECOMMENDED do NOT mass-rename (renaming breaks the 149 hard links + hundreds of references and buys nothing); enforce the grammar only on NEW docs. Alternative: rename off-grammar docs via link-coupled commits — high churn, not recommended.

---

## (c) `_orchestration/` lifecycle + currency rule

**The problem this solves.** Epic docs accrete stale physics framings and stale status in-place. Today lifecycle is carried by ad-hoc in-prose warnings: `index.md` (784 lines at HEAD) carries an audit-trail note at `:3` and a `> **Staleness notice (2026-06-16)**` at `:6`; `_orchestration/_archive/` already exists (with `index-stale.md` as the precedent for migrating superseded index sections). This section codifies three things: a mandatory status header, the append-only correction pattern, and an `index.md` hygiene rule.

### 1. Mandatory status header on every epic doc

Every `_orchestration/*.md` epic doc must open with a status header carrying **state + last-verified date + owner**:

```
**Status:** ACTIVE | CLOSED | ARCHIVED-to-`_archive/` — last-verified YYYY-MM-DD (owner: <session/role>)
```

- **ACTIVE** — a live workstream; the doc is the current phase log. Must carry a last-verified date that is refreshed whenever the doc is materially touched.
- **CLOSED** — the workstream finished (result landed, branch closed); the doc stays in `_orchestration/` as the record but is no longer a live tracker. A CLOSED doc is a candidate for archive only under the (c)-3 hygiene rule.
- **ARCHIVED-to-`_archive/`** — the doc has been moved (link-coupled) to `_orchestration/_archive/`; the header records the move date.

### 2. Append-only correction pattern (the standing fix for stale physics framings)

When an epic doc carries a physics framing later refuted, the correction lands **append-only, in-place, dated** — it does NOT rewrite the original framing and does NOT add a preservation banner (git is the trail).

**Live-fire precedent (the pattern to codify).** `_orchestration/2026-06-07_electron-synthesis-epic.md:319` carried the G2 "channel→DOF mapping INVERTED" diagnosis pinning "photon = microrotational ω" as canonical. That side was later REFUTED. The correction landed at `:320` as an append-only `🔴 RESOLUTION (2026-07-03, append-only — this diagnosis's "photon = microrotational ω" side was REFUTED)` note that ends verbatim: *"This entry stands as history (git is the trail); the KB relabel ... carry the adjudicated forward state."* The original `:319` diagnosis was left intact; the resolution appended below it. That is the standing pattern.

**Rule:** stale physics framing in an epic doc is corrected by an append-only dated `🔴 RESOLUTION` (or `🔴 CORRECTION`) note immediately following the stale passage, naming what was refuted, by what evidence, and where the forward state now lives. The stale passage is never edited or deleted. No in-doc "PRESERVED — see git" banner (that IS the banner the constraint forbids; the append-only note carries the correction, git carries the preservation).

### 3. `index.md` hygiene rule

`index.md` is the live tracker and drifts long (784 lines). Rule:
- When a section of `index.md` is fully superseded (its workstream CLOSED and its state captured elsewhere), migrate that section to `_orchestration/_archive/index-stale.md` (the existing precedent) in a link-coupled commit — move + any citer update + gates green.
- The live `index.md` keeps only ACTIVE-epic state + the current priority ladder + open decisions + last-updated HEAD + tag count. Staleness notices (like the `:6` 2026-06-16 notice) are acceptable transitional markers but each should carry a date and a pointer to what supersedes it.
- `index.md` itself carries the mandatory status header semantics implicitly (it is always the ACTIVE live tracker); it is exempt from the ACTIVE/CLOSED/ARCHIVED enum but must carry a `last-updated HEAD + date` line.

**RATIFY:** Adopt (1) the mandatory `**Status:** ACTIVE|CLOSED|ARCHIVED — last-verified DATE (owner)` header on every `_orchestration/*.md` epic doc; (2) the append-only dated `🔴 RESOLUTION/CORRECTION` note as the ONLY sanctioned fix for stale physics framings in epic docs (no rewrites, no preservation banners); (3) the `index.md` hygiene rule (superseded sections migrate link-coupled to `_orchestration/_archive/index-stale.md`; live `index.md` carries only current state). No sub-fork here beyond confirming the header enum wording — the append-only pattern is already live-fire-precedented (`electron-synthesis-epic.md:320`) and the archive precedent already exists (`index-stale.md`); this section codifies existing practice rather than inventing it.

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
- **(b) `research/` grammar** — adopt `YYYY-MM-DD_<slug>_<type>.md` + closed type-vocab + register-class exemption + **keep-flat**; adopt archive-tier 3-of/never-if criteria with honesty-trail UNTOUCHABLE; confirm the type-vocab closed set and **grandfather** (no mass-rename) off-grammar names.
- **(c) `_orchestration/` lifecycle** — adopt the mandatory `Status:` header enum (ACTIVE/CLOSED/ARCHIVED + last-verified date + owner); adopt the append-only dated `🔴 RESOLUTION/CORRECTION` note as the ONLY stale-framing fix (no rewrites/banners); adopt the `index.md`→`_archive/index-stale.md` hygiene rule. Confirm header wording only (rest is codified existing practice).

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

**(b) `research/` grammar**
- 523 active `research/*.md` (flat) ✓; 147 under `research/_archive/` ✓.
- 149 distinct `research/*.md` paths in markdown-link form `](...research/...)` from `manuscript/ave-kb/**` ✓ (the HARD-gated set). Broader bare-token mention count from ave-kb = 236 (includes non-link references).
- ~477 (bare-token) distinct `research/*.md` references corpus-wide from outside `research/`; markdown-link subset = 209. Brief's "~476" matches the bare-token scale.
- Type-suffix frequency (flat `research/`): `result` 125, `prereg` 91, `note` 16, `synthesis` 2, `ruling`/`registered`/`framing`/`diagnostic`/`design`/`derivation`/`audit`/`adjudication` 1 each; lifecycle `_FROZEN` 19, `_DRAFT`/`_draft` 10, `_CLOSED` 1.
- Honesty-trail exemplars confirmed: `research/2026-05-17_C14-DAMA_audit_walk-back.md`, `*_prereg_FROZEN.md` family.

**(c) `_orchestration/` lifecycle**
- `index.md` = 784 lines at HEAD (brief said 785 — off-by-one; 784 is HEAD truth). `index.md:3` audit-trail note ✓; `index.md:6` `> **Staleness notice (2026-06-16)**` ✓.
- `_orchestration/_archive/` exists; contains `index-stale.md` ✓.
- Append-only precedent: `_orchestration/2026-06-07_electron-synthesis-epic.md:319` = G2 diagnosis, `:320` = append-only `🔴 RESOLUTION (2026-07-03 ...)` ending "This entry stands as history (git is the trail)" ✓ (brief said "~line 315-319"; diagnosis at 319, resolution at 320 — HEAD truth).
