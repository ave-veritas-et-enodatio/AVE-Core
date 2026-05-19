# `_orchestration/` — Tracked Orchestration State

This directory carries the **revision-controlled orchestration state** for AVE-Core: per-epic state docs, cross-cutting carry-forward, and the archive of closed epics. Created 2026-05-19 to fix the drift where orchestration briefings were landing at `~/.claude/plans/` (agent-local, mutable, undiscoverable) or `.agents/handoffs/` (in-repo but gitignored).

## What lives here

| File | Purpose |
|---|---|
| `README.md` | This convention doc |
| `index.md` | Cross-cutting carry-forward — priority ladder + open decisions + active-epic table |
| `<epic-slug>.md` | Per-epic state, multi-phase, evolves through revisions |
| `_archive/<epic-slug>.md` | Closed epics (preserved; audit tags reference) |

## What does NOT live here

- **Per-session "what I did today" notes** → `.agents/handoffs/` (gitignored ephemeral scratch) or `~/.claude/plans/` (agent-local one-shot)
- **Implementor amendment audits / pre-execution scoping** → can live at `~/.claude/plans/` if one-shot, OR be promoted to a subsection of the relevant phase entry in the epic doc if retrospectively load-bearing
- **Collaboration notes / user-persona calibration** → `.agents/handoffs/COLLABORATION_NOTES.md`
- **L3 archive / research drafts / driver code / manuscript leaves** → these live elsewhere in the repo per existing convention

## Per-epic doc lifecycle

```
[Epic kickoff]    → _orchestration/<epic-slug>.md created with Status: ACTIVE,
                    Goal, Current state, Phase 1 PENDING
[Implementor]     → Phase 1 PENDING → CLOSED; merge commit + audit tag referenced;
                    next phase PENDING appended
[Multi-phase arc] → Phases 2..N follow same pattern
[Epic closure]    → All phases CLOSED; doc moved to _archive/
                    (not deleted; audit tags reference it immutably)
```

## File-naming convention

- **Epic slug**: kebab-case, descriptive, stable
  - `section-e-cascade.md`
  - `q-g47-retrofit.md`
  - `phase-2-mass-spectrum.md`
  - `dm-meta-closure.md`
- **Carry-forward**: `index.md` (single file, not dated)
- **Archive**: `_archive/<epic-slug>.md` when epic closes

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
