# AVE-Core — Agent Orientation

This is the canonical engine + manuscript + KB repo for the AVE (Applied Vacuum Engineering) framework. AVE is a substrate-physics framework treating vacuum as a saturable K4-TLM lattice with Cosserat-Beltrami flux structure; this repo carries the load-bearing derivations, drivers, KB invariants, and matrix of empirical claims.

> **⚙ Maintainer-specific workflow + paths.** The **Branching pattern**, **Session conventions**, **Audit-tag + merge pattern**, **Pre-commit discipline**, and the sibling-repo / memory **paths** in **Cross-references** below describe the maintainer's personal local working setup — e.g. `/Users/grantlindblom/AVE-staging/` is a local directory layout, **not** a repo path; sibling repos live under whatever umbrella the contributor has cloned them into. These apply only where:
> ```bash
> [[ $(git config get user.name) == Grant* ]]
> ```
> Other contributors: adapt branch conventions and absolute paths to your own workspace. The **Repo structure**, **Skill ecosystem**, and **Pure-AVE-corpus rule** sections are universal.

## First read for any new session

Before doing anything substantive, read these in order:

1. **[`_orchestration/index.md`](_orchestration/index.md)** — current orchestration state: priority ladder, open decisions, active-epic table, last-updated HEAD + tag count.
2. **The active epic doc(s)** at `_orchestration/<epic-slug>.md` — current phase log for each active workstream.
3. **[`manuscript/ave-kb/CLAUDE.md`](manuscript/ave-kb/CLAUDE.md)** — cross-volume KB invariants (notation rules, tcolorbox environments, vacuum-medium notation, operator-numbering convention). Required reading before editing any manuscript file.

## Repo structure (high-level)

| Path | Purpose |
|---|---|
| `src/ave/` | Engine code (K4Lattice3D, Cosserat field, solvers, observers, integrators) |
| `src/scripts/vol_<N>_<name>/` | Per-volume driver scripts (numerical experiments + forward-prediction drivers) |
| `src/tests/` | Pytest suite (canonical-constants checks, predictions matrix, regression gates) |
| `manuscript/vol_<N>_<name>/` | LaTeX volumes (1 foundations / 2 quantum / 3 macroscopic / 4 engineering / 5 biology / 6 cosmology / 7 atomic / 8 etc.) |
| `manuscript/ave-kb/` | Knowledge base — common invariants + per-volume distillation + canonical leaf docs |
| `research/` | Active research docs (preregs, results, prereg-frozen analysis docs) |
| `research/_archive/L3_electron_soliton/` | L3 archive — 129 docs (Q-G47 electron-modeling thread) |
| `_orchestration/` | **Tracked orchestration state** — per-epic phase log + cross-cutting carry-forward |
| `.agents/handoffs/` | **Gitignored ephemeral scratch** — per-session notes, collaboration calibration, pre-execution amendment audits |

## Branching pattern

| Branch | Role |
|---|---|
| `analysis/integration` | **Dormant** (historical tracker). Superseded by main-based integration in the 2026-05-28→31 `integration→main` transition; 0 commits ahead of `main`, last live 2026-05-20. Retained for history — do not branch from it or merge to it. |
| `research/l3-electron-soliton` | **Coworker's reference** — UNTOUCHED. Active L3 research branch maintained by ave-veritas-et-enodatio. Do not merge into. |
| `main` | **Active integration target.** Implementor branches branch off `main` and merge back via PR (PR #51–#59 all merged here). The earlier "frozen until coworker done" model ended with the 2026-05-28→31 `integration→main` transition. |
| `analysis/<topic>` | Implementor-session branches off `main`. Push + open a PR; do NOT merge directly — the orchestration session does the PR merge. |
| `audit/<date>_<topic>` | Immutable audit tags at implementor branch tip — preserves commit + tree + ancestry for retrospective review. |

## Session conventions

Two distinct session types:

- **Orchestration sessions** — multi-turn with Grant directly. Plan / audit / review / merge / decide what comes next. Update `_orchestration/index.md` + active epic docs. Do the `--no-ff` + audit-tag + branch-cleanup pattern on implementor merges.
- **Implementor sessions** — single-deliverable. Kick off by reading a `## Phase X (PENDING)` section in the relevant `_orchestration/<epic>.md` doc. Branch off `main`, full skill discipline (prereg + driver + result + matrix + closure-roadmap + auditor), push branch but do NOT merge.

See memory entry `feedback_orchestration_vs_implementation_sessions.md` for full discipline.

## Skill ecosystem

Active skills live at `~/.claude/skills/ave-*/SKILL.md`. Key skills:

- `ave-prereg` — corpus-grep before any new derivation
- `ave-canonical-source` — import canonical constants from `src/ave/core/constants.py`, never hard-code
- `ave-canonical-leaf-pull` — enumerate canonical leaves before deriving Q-factor / scaling-law / matched-coupling / energy-quantum / cross-section / propagation-speed problems
- `ave-handoff-canonical-locale` — orchestration briefings land in `_orchestration/`, not `~/.claude/plans/`
- `verify-before-cite` — verify citation content + temporal currentness + cross-branch state before referencing file:line / quote / status claims
- `consistency-vs-emergence` — classify tests as definitional-identity / axiom-manifestation / consistency-check / emergence-test before writing
- `substrate-native-check` — walk K4 + Cosserat structure before scaffolding solvers
- `phase-space-coordinate-check` — match coordinate system between test + corpus claim
- `ave-discrimination-check` — SM-counterfactual + interpretive-alternatives before framing positive results as "AVE-distinct"
- `ave-evidence-framing-discipline` — precision check on strength language before assertion
- `ave-walk-back` — propagation checklist when matrix rows retire or claims rescope
- `ave-audit` + `ave-audit-of-audit` + `ave-sweep-audit` — audit-discipline triad

Memory entries at `~/.claude/projects/-Users-grantlindblom-AVE-staging/memory/` carry user persona, workflow conventions, workspace layout reference, and feedback discipline.

## Pure-AVE-corpus rule

All tracked files in this repo (manuscript, KB, research docs, drivers, _orchestration/, commit messages, branch descriptions) MUST be pure physics. NO references to investors / funds / interviews / external pitches / 1517 / etc. External-context inputs must be translated to pure-physics rationale before writing.

The `.agents/handoffs/` gitignored scratch is the only place external-context refs may appear (and even there, sparingly — they're a memory-leak risk).

## Audit-tag + merge pattern

When merging an implementor branch into `main` (the active integration target):

1. Tag the implementor branch tip with `audit/<date>_<topic>` BEFORE delete (preserves immutably)
2. `git merge --no-ff <implementor-branch>` with detailed merge-commit message (outcome + cascade implications + walk-back queue updates)
3. Push merge commit + audit tag to origin
4. Delete implementor branch (local + remote) once tag verifies on origin

Current state: 70 audit tags on origin (`git tag -l "audit/*" | wc -l`).

## Pre-commit discipline

Before any `git commit` in an orchestration session, run:

```bash
git branch --show-current
```

This verifies the target branch matches the intended orchestration branch (typically `analysis/integration`). The check is **mandatory after any Agent / Task / subagent invocation** — sub-agents that perform branch operations share the orchestration session's working tree by default and may leave it on the sub-agent's branch.

**Failure mode this prevents**: 2026-05-19 EOD orchestration commit landed on `analysis/cosmic-axis-glossary` instead of `analysis/integration` because the cosmic-axis-glossary sub-agent checked out its own branch and left the working tree there. Recovery via cherry-pick + reset.

**Structural fix for the same issue**: spawn implementors via Agent tool with `isolation: "worktree"` so the sub-agent works in a temporary git worktree (separate working dir, same `.git`). See `_orchestration/README.md` "Spawning implementors via the Agent tool — discipline" for the canonical pattern.

**Related skill**: `verify-before-cite` v1.3 trigger 8 (commit-application claims) catches the upstream version of the same failure axis — assuming a commit was applied to the current branch without running `git branch --contains <hash>`. Both fire on agent-claim-about-branch-state-without-verifying-via-git but at different timing points (trigger 8 at brief-drafting time; this section at orchestration-commit time).

## Cross-references

- **AVE workspace layout** (multi-repo map): memory entry `reference_ave_workspace.md`
- **AVE KB as primary search location**: memory entry `reference_ave_kb_primary_search.md`
- **Sibling repos** (`AVE-PONDER`, `AVE-HOPF`, `AVE-QED`, `AVE-APU`, etc.): live at `/Users/grantlindblom/AVE-staging/`; each has its own `.agents/` directory + `CLAUDE.md` (or should)
- **Parent archive**: `Applied-Vacuum-Engineering` at `/Users/grantlindblom/` (historical reference)
