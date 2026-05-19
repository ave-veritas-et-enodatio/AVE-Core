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

## Cross-references

- Skill enforcing canonical-locale write discipline: `~/.claude/skills/ave-handoff-canonical-locale/SKILL.md`
- Memory entry: `feedback_orchestration_vs_implementation_sessions.md`
- Adjacent ephemeral-scratch convention: `.agents/handoffs/` (gitignored; for per-session notes + collaboration calibration)
