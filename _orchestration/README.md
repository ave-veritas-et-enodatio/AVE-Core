# `_orchestration/` — Tracked Orchestration State

**Audit trail (2026-05-23 Benn → 2026-05-25 merge):** This directory was ported from `analysis/integration` (D7 curation, KB claim-DAG integration) on 2026-05-23, and completed-work snapshots were moved to [`_archive/index-stale.md`](_archive/index-stale.md). Merged with integration live state on 2026-05-25 — treat this doc as the current live tracker; consult git log for recent updates.
**EDIT** - 2026-05-23 Benn - document deprecated. Do not do any sweeping work from this document without evaluating current repo state. KB claim DAG has received many improvements and the KB has had many fixups in the process. This directory was ported over from `analysis/integration` branch, which has now been superseded. Work that was clearly already done has been extracted and moved to _archive/. What remains may still be relevant, but again, *check first*.

This directory carries the **revision-controlled orchestration state** for AVE-Core: per-epic state docs, cross-cutting carry-forward, and the archive of closed epics. Created 2026-05-19 to fix the drift where orchestration briefings were landing at `~/.claude/plans/` (agent-local, mutable, undiscoverable) or `.agents/handoffs/` (in-repo but gitignored).

## Directory structure (Phase B reorg, 2026-05-20)

Two top-level subdirectories under `_orchestration/`:

```
_orchestration/
├── index.md                              # Cross-cutting carry-forward (top-level entry point)
├── README.md                             # This convention doc
├── experimental/                         # Experimental-arc epic + sub-epics + supporting docs
│   ├── experimental-arc.md               # Parent epic (matrix-row hardware/measurement workstream)
│   ├── promotion-workflow-template.md    # Sibling-repo → AVE-Core promotion checklist
│   ├── <sub-epic-slug>/                  # Per-sub-epic subdirectory (one per matrix row in flight)
│   │   ├── exp-<slug>.md                 # Single consolidated sub-epic doc (phase table + per-active-phase detail + audit trail)
│   │   ├── exp-<slug>-sim-audit.md       # Sim audit / framework-readiness audit (separate; kept distinct)
│   │   └── _archive/                     # Closed-phase briefs (preserved; ARCHIVED banner header)
│   │       └── exp-<slug>-<phase>-brief.md
│   ├── a1-hopf/                          # Concrete sub-epic example
│   ├── c11-mach-zehnder/                 # Concrete sub-epic example
│   └── c15-cleave-01/                    # Concrete sub-epic example (6 closed-phase briefs in _archive/)
├── theoretical/                          # Theoretical multi-session epics (cascade adjudication, axis sweeps, etc.)
│   ├── section-e-cascade.md
│   ├── soliton-lattice-coupling-operator.md
│   └── cosmic-epsilon-de-projection-scoping.md
└── _archive/                             # Top-level closed-epic archive (pre-Phase-B; preserved)
    └── <closed-epic-slug>.md             # e.g. cosmic-axis-glossary, h-infinity 3 epics, c5-sdss-dr17, c5-shamir-2022
```

## Conventions for per-sub-epic subdirectories (new in Phase B)

Each in-flight experimental sub-epic gets a **single consolidated `exp-<slug>.md` doc** as the navigational spine, plus sibling audit docs that stay separate (sim audit / framework-readiness audit), plus a `_archive/` subdirectory for closed-phase briefs:

| Doc class | Location | Notes |
|---|---|---|
| **Sub-epic consolidated doc** | `experimental/<slug>/exp-<slug>.md` | Phase table + per-active-phase detail + audit trail. The single navigational spine for the sub-epic. |
| **Sim / framework-readiness audit** | `experimental/<slug>/exp-<slug>-sim-audit.md` | Kept SEPARATE from the consolidated doc (different audit class; different load-bearing role). |
| **Closed-phase briefs** | `experimental/<slug>/_archive/<original-brief-name>.md` | Move HERE when the phase closes; insert ARCHIVED banner header at top pointing back to the consolidated doc. |

**Why this structure** (Phase B rationale, external review 2026-05-20):
- Flat-namespace nesting collapse — pre-reorg pattern `exp-c15-cleave-01-phase-1a-rev1-atopile-walkback-brief.md` (5 levels in one filename) compounded at next sub-decision.
- Brief proliferation without merges — pre-reorg C15 had 6 separate briefs; discoverability inverted (orchestrator knew everything; new sessions didn't know which file was current).
- Subdirectory hierarchy + per-sub-epic consolidation addresses both.

## When to archive a brief

When its phase closes — i.e., the phase row in the consolidated doc's phase table shows ✓ COMPLETE or ✓ CLOSED:

1. `git mv experimental/<slug>/exp-<slug>-<phase>-brief.md experimental/<slug>/_archive/`
2. Insert ARCHIVED banner header at top of the archived brief:
   ```markdown
   > **ARCHIVED <date>** — content preserved per ave-walk-back discipline. Canonical reference: [`exp-<slug>.md`](../exp-<slug>.md) consolidated sub-epic. This brief was the active doc during phase execution; phase is now closed/superseded per the consolidated doc's phase table.
   ```
3. Walk back any `../` relative paths in the brief: it's now 2 levels deep (was at `experimental/<slug>/`), so manuscript/src refs need an extra `../`. Intra-archive sibling references stay as-is.

## Cross-reference convention (post-Phase-B)

ALL cross-refs from outside `_orchestration/` (KB leaves, manuscript LaTeX, source code, sibling-repo READMEs, research docs, etc.) to per-epic docs MUST use the new paths after Phase B:

- `_orchestration/exp-c15-cleave-01.md` (old) → `_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01.md` (new)
- `_orchestration/exp-a1-hopf.md` (old) → `_orchestration/experimental/a1-hopf/exp-a1-hopf.md` (new)
- `_orchestration/exp-c11-mach-zehnder.md` (old) → `_orchestration/experimental/c11-mach-zehnder/exp-c11-mach-zehnder.md` (new)
- `_orchestration/experimental-arc.md` (old) → `_orchestration/experimental/experimental-arc.md` (new)
- `_orchestration/promotion-workflow-template.md` (old) → `_orchestration/experimental/promotion-workflow-template.md` (new)
- `_orchestration/section-e-cascade.md` (old) → `_orchestration/theoretical/section-e-cascade.md` (new)
- `_orchestration/soliton-lattice-coupling-operator.md` (old) → `_orchestration/theoretical/soliton-lattice-coupling-operator.md` (new)
- `_orchestration/cosmic-epsilon-de-projection-scoping.md` (old) → `_orchestration/theoretical/cosmic-epsilon-de-projection-scoping.md` (new)

Orchestrator propagates cross-ref updates in the same branch as the reorganization commit. Sibling-repo cross-refs land on separate sibling-repo branches (one branch per sibling).

## What does NOT live here

- **Per-session "what I did today" notes** → `.agents/handoffs/` (gitignored ephemeral scratch) or `~/.claude/plans/` (agent-local one-shot)
- **Implementor amendment audits / pre-execution scoping** → can live at `~/.claude/plans/` if one-shot, OR be promoted to a subsection of the relevant phase entry in the epic doc if retrospectively load-bearing
- **Collaboration notes / user-persona calibration** → `.agents/handoffs/COLLABORATION_NOTES.md`
- **L3 archive / research drafts / driver code / manuscript leaves** → these live elsewhere in the repo per existing convention

## Per-epic doc lifecycle

```
[Epic kickoff]    → experimental/<slug>/exp-<slug>.md created with Status: ACTIVE,
                    Goal, Phase table, Phase 1 PENDING
[Implementor]     → Phase 1 PENDING → CLOSED; merge commit + audit tag referenced;
                    next phase PENDING appended; brief moved to _archive/ when phase closes
[Multi-phase arc] → Phases 2..N follow same pattern
[Epic closure]    → All phases CLOSED; sub-epic dir moved to a top-level `_archive/` or remains in place
                    (per orchestrator adjudication); audit tags reference immutably
```

## File-naming convention

- **Sub-epic slug**: kebab-case matching matrix row + epic name
  - `a1-hopf`
  - `c11-mach-zehnder`
  - `c15-cleave-01`
- **Sub-epic consolidated doc**: `exp-<slug>.md`
- **Sim audit / framework-readiness audit**: `exp-<slug>-sim-audit.md`
- **Closed-phase brief in `_archive/`**: original brief name preserved (e.g. `exp-c15-cleave-01-phase-0-scaffolding.md`)
- **Theoretical epic**: kebab-case epic name (no `exp-` prefix; lives at `theoretical/`)
- **Carry-forward**: `index.md` (single file at root; not dated)
- **Top-level archive**: `_archive/<closed-epic-slug>.md` for pre-Phase-B closed epics

## Pure-AVE-corpus rule

All files in this directory are tracked / public-facing. They MUST follow the pure-AVE-corpus discipline:

- No references to investors / funds / interviews / external pitches
- Translate external-context input into pure-physics rationale before writing
- Scrub during migration from loose drafts, not after

## Per-epic doc structure (template)

```markdown
# Epic: <name>

**Status**: ACTIVE | CLOSED
**Started**: <date>
**Goal**: <single-sentence goal>
**Last updated**: <date>

## Current state at HEAD <commit>

<brief summary of where the epic stands corpus-wide>

## Phases

### Phase <N>.<a> (CLOSED <date>) — <topic>
- Orchestration brief: <summary of what was scoped>
- Outcome: <result>
- Merge: <commit>, audit tag <tag>
- Artifacts: <key files/paths>

### Phase <N>.<b> (PENDING) — <topic>
<implementor briefing — assumptions A1-AN, scope boundary, phase plan, adjudication, verification>

### Phase <N>.<c> (DEFERRED) — <topic>
<gated on Phase N.b outcome>

## Open decisions
<epic-specific items requiring Grant adjudication>

## References
<canonical paths into the repo + audit tags>
```

## How orchestration sessions interact with this directory

1. **Start of orchestration session**: read `index.md` for cross-cutting state; read the active-epic doc(s) for current phase status.
2. **During session**: update active epic doc(s) as phases close + new phases append. Update `index.md` if cross-cutting state changes (priority ladder shifts, open decisions resolve / appear).
3. **End of session**: commit the updated state on `analysis/integration` (or appropriate branch); audit-tag if landing alongside an implementor merge.
4. **Next orchestration session**: picks up from tracked state in this directory — no loose handoff file needed.

## How implementor sessions interact with this directory

1. **Kickoff**: read the relevant `## Phase X (PENDING)` section of the active epic doc — that's the briefing.
2. **During session**: do NOT edit this directory; implementor work lands in the rest of the repo (driver code, manuscript edits, research docs, closure-roadmap entries).
3. **End of session**: push branch; do NOT merge. The orchestration session that reads the result will close the PENDING phase in the epic doc.

## Spawning implementors via the Agent tool — discipline

When an orchestration session spawns an implementor as a sub-agent (rather than via a separate Claude Code session), branch-mutation discipline matters: the sub-agent shares the orchestration session's working tree by default, so any `git checkout` the sub-agent performs leaves the orchestration session on the sub-agent's branch.

**Default pattern — use `isolation: "worktree"`**: when invoking the Agent tool with subagent_type `ave-implementer` (or any subagent that will do branch operations), pass `isolation: "worktree"` so the sub-agent works in a temporary git worktree. The worktree is a separate working directory backed by the same `.git`, so the sub-agent's branch operations don't mutate the orchestration session's working tree. Pushed branches land on origin and remain visible from the orchestration worktree for merge. Worktree is automatically cleaned up if the agent makes no changes; otherwise the path and branch are returned in the agent's result.

**Fallback pattern — explicit post-return branch verification**: if `isolation: "worktree"` cannot be used (e.g., implementor needs to share working state for some operation-specific reason), the orchestration session MUST verify branch-of-record AFTER the sub-agent returns and BEFORE any subsequent git commit:

```bash
git branch --show-current
# expected: analysis/integration (or whatever orchestration branch you started on)
# if NOT expected: git checkout analysis/integration before any orchestration commit
```

If you committed before checking and the commit landed on the wrong branch, the recovery is:
```bash
# from the wrong branch:
git log --oneline -1                   # capture the wrong-branch tip
git checkout analysis/integration
git cherry-pick <wrong-branch-tip>     # bring the commit forward
git checkout <wrong-branch>
git reset --hard <prior-tip>           # remove the misplaced commit
git checkout analysis/integration
```

**Failure mode this prevents**: 2026-05-19 EOD orchestration commit landed on `analysis/cosmic-axis-glossary` (implementor's branch) instead of `analysis/integration` because the cosmic-axis-glossary sub-agent had checked out its own branch and left the working tree there. Required cherry-pick + reset to fix. Worktree isolation would have prevented the issue structurally; explicit pre-commit `git branch --show-current` check would have caught it behaviorally.

**Cross-reference to skill ecosystem**: this discipline complements `verify-before-cite` v1.3 trigger 8 (commit-application claims must include `git branch --contains` check). Both address the same root cause — agent-claim-about-branch-state without verifying-via-git — at different timing points: trigger 8 fires at citation/brief-drafting time, this section fires at orchestration-commit time.

## Cross-references

- Skill enforcing canonical-locale write discipline: `~/.claude/skills/ave-handoff-canonical-locale/SKILL.md`
- Memory entry: `feedback_orchestration_vs_implementation_sessions.md`
- Adjacent ephemeral-scratch convention: `.agents/handoffs/` (gitignored; for per-session notes + collaboration calibration)
