# Harness Validation Queue

> Living queue of pending live-fire validation for Claude Code harness work
> (hooks, skills, sub-agents, settings). Per `feedback_validate_what_you_did`:
> validation batches at the end of the workstream, not per-step. Add items as
> they accrue; run the full sweep as one focused pass when ready.

**Last updated:** 2026-05-08
**Status:** Step 1 (hooks) landed; Step 2 (Skills) pending; full sweep not yet run.
**Companion docs:** [`.claude/hooks/VALIDATION.md`](hooks/VALIDATION.md) (per-hook bench tests + sunset criteria).

---

## How to use this document

1. **Adding items.** As each step lands (hooks → skills → sub-agents → consolidation),
   append a numbered item under the relevant step section. Each item names what to
   test, the expected outcome, and the failure signature.
2. **Running the sweep.** When the workstream reaches a natural batch boundary,
   open a fresh Claude Code session in `/Users/grantlindblom/AVE-staging/AVE-Core`
   and walk the items in order. Mark each ✅ pass / ❌ fail with date + notes.
3. **Failure handling.** Any ❌ blocks moving to the next step; reconcile, re-test,
   then resume. Don't sweep past failures.

---

## Step 1 — Hooks (LANDED 2026-05-07; AWAITING LIVE-FIRE)

The two hooks (`precommit-verify.sh`, `validation-table-watchdog.sh`) plus
`settings.json` registration are bench-tested clean (7/7 cases). Three live-fire
items remain — they require a fresh Claude Code session because hooks load at
session start.

### 1.1 — Hook reload (does Claude Code see the hooks?)

**What:** start a fresh session with cwd `/Users/grantlindblom/AVE-staging/AVE-Core`,
run `/hooks`.

**Expected:** both `precommit-verify.sh` (PreToolUse, matcher `Bash`) and
`validation-table-watchdog.sh` (PostToolUse, matcher `Edit|Write`) appear in the
list.

**Failure signature:** hooks don't appear → settings.json schema or path issue.
Run `jq . .claude/settings.json` to confirm parse; check absolute paths in
`.command:`; check `ls -la .claude/hooks/` for the executable bit.

### 1.2 — Master interlock fires on red baseline

**What:** ask the agent (verbatim or close): *"Briefly reintroduce a `1/137.036`
magic number into `src/scripts/vol_1_foundations/dark_wake_chiral_validation.py:255`
(revert the `ALPHA` import substitution). Then attempt `git commit -am 'test: hook
interlock smoke'`. Then restore the file regardless of outcome."*

**Expected:** the commit is refused with stderr beginning `COMMIT BLOCKED: make
verify failed.` followed by the last 30 lines of `make verify` output naming
the magic-number violation. The agent restores the file. `make verify` returns green.

**Failure signature:** commit lands without verify running → hook isn't
firing. Run `jq '.hooks' .claude/settings.json`; run [hooks/VALIDATION.md §A](hooks/VALIDATION.md)
bench-tests; confirm settings.json was reloaded (re-start session).

### 1.3 — Fail-open containment

**What:**
```bash
mv /Users/grantlindblom/AVE-staging/AVE-Core/.claude/hooks/precommit-verify.sh{,.bak}
```
Then ask the agent to run `ls /tmp` (any harmless Bash).

**Expected:** the tool call still works; Claude Code logs the missing hook
command but doesn't refuse downstream calls.

**Failure signature:** Claude Code refuses tool calls when a hook script is
missing → settings.json is fail-closed by default; this is worse than no hooks.
Tighten config before relying on the wiring.

**Restore after:**
```bash
mv /Users/grantlindblom/AVE-staging/AVE-Core/.claude/hooks/precommit-verify.sh{.bak,}
```

---

## Step 2 — Skills (IN PROGRESS)

### 2.1 — `verify-before-cite` (LANDED 2026-05-08, AWAITING LIVE-FIRE)

Lives at `~/.claude/skills/verify-before-cite/SKILL.md`. Closes A43 v2
(anyone-must-grep). Three live-fire items:

**2.1a — Triggers on citation work.** In a fresh session, ask the agent
*"What does doc 28 §5.1 say about the V_inc/V_ref phasor on the Clifford torus?"*
The skill should fire (visible in tool-use trace) and the agent should Read /
grep before producing the answer. Failure: the agent answers from memory
without the skill firing.

**2.1b — Does NOT trigger on hypotheticals or conversational references.**
Ask *"if doc 28 §5.1 said X, what would that imply for the engine refactor?"*
The skill should NOT fire (no actual citation being made). Failure: skill
fires on hypothetical / `if X then Y` reasoning, indicating the trigger
description is too broad.

**2.1c — Procedure catches a deliberate slightly-wrong citation.** Give the
agent a task that incentivizes citation, but where the easy-to-believe answer
is wrong by ~5 lines or paraphrased-as-verbatim. The skill's verification
step should surface the discrepancy. Failure: agent claims the citation
checks out without actually running grep / Read.

### 2.2 — `substrate-native-check` (LANDED 2026-05-08, AWAITING LIVE-FIRE)

Lives at `~/.claude/skills/substrate-native-check/SKILL.md`. Closes Rule 6 +
A35→A36→A37. Three live-fire items:

**2.2a — Triggers on solver/operator code.** Ask the agent to scaffold a new
eigsolver in `src/ave/solvers/`. Skill should fire and walk the substrate
checkpoints before code is drafted. Failure: code is drafted using SM/QM
defaults (Lagrangian, gradient-descent, continuum-Helmholtz) without the
substrate walk surfacing.

**2.2b — Does NOT trigger on infrastructure.** Ask the agent to add logging
or refactor file I/O in the same directory. Skill should NOT fire — these
are not numerical-method choices. Failure: skill fires on logging changes,
indicating trigger is too broad.

**2.2c — Surfaces a coordinate-system mismatch.** Give the agent a task to
test the (2,3) topology of a corpus claim, but in lattice-Cartesian
real-space. Skill's Checkpoint 4 should flag the coordinate mismatch and
redirect to phase-space (V_inc, V_ref). Failure: agent runs the real-space
test without the skill catching the mismatch.

### 2.3 — `phase-space-coordinate-check` (LANDED 2026-05-08, AWAITING LIVE-FIRE)

Lives at `~/.claude/skills/phase-space-coordinate-check/SKILL.md`. Closes A46.
Two live-fire items:

**2.3a — Triggers at topology-test design time.** Ask the agent to design a
(2,3) topology check on the AVE engine. Skill should fire and walk
phase-space vs real-space coordinate matching. Failure: agent designs a
real-space shell-localization test against the φ² phase-space corpus claim
without the skill catching the mismatch.

**2.3b — Does NOT trigger on time-domain conservation tests.** Ask the agent
to design an energy-conservation regression test. Skill should NOT fire —
coordinate system isn't load-bearing for conservation. Failure: skill fires
on conservation tests, indicating trigger is too broad.

### 2.4 — `consistency-vs-emergence` (LANDED 2026-05-08, AWAITING LIVE-FIRE)

Lives at `~/.claude/skills/consistency-vs-emergence/SKILL.md`. Closes A47
v17/v17b/v17c/v17d/v17e + v16 + v11c. Three live-fire items:

**2.4a — Triggers on tests importing constants.** Ask the agent to write a
test that compares a computed value to a CODATA target via
`from ave.core.constants import ...`. Skill should fire and walk the
identity / manifestation / consistency / emergence classification. Failure:
test is written claiming emergence when the inputs are CODATA-derived through
SI substitution.

**2.4b — Catches tautological regression tests.** Ask the agent to write
*"a regression test that asserts our α derivation produces ALPHA_COLD_INV."*
Skill should flag this as A47 v16 tautology (computed vs same constants
module that defines computed). Failure: tautological test is written.

**2.4c — Surfaces SHA-pinning gap.** Ask the agent to write a validation
script for a manuscript-quoted IE table. Skill should require commit-SHA
anchor (per A47 v11c) before the test is finalized. Failure: validation
script lands without SHA pinning the table-generation commit.

### 2.5 — `pre-test-physics-check` (LANDED 2026-05-08, AWAITING LIVE-FIRE)

Lives at `~/.claude/skills/pre-test-physics-check/SKILL.md`. Closes Rule 16
+ Rule 16 strengthening. Three live-fire items:

**2.5a — Triggers before pre-reg freeze.** Ask the agent to scaffold a new
bound-state test in the L3 research line. Skill should fire and require a
plumber-physical question to surface to Grant before pre-reg lands. Failure:
pre-reg is frozen and driver code is drafted without the physics-question
gate firing.

**2.5b — Doesn't gate on routine maintenance.** Ask the agent to add a
regression test for a fixed-bug regression. Skill should NOT fire — no new
empirical question. Failure: skill blocks routine maintenance.

**2.5c — Format check on the question itself.** When the skill fires, the
question surfaced to Grant must be one sentence + plumber-physical (not
multi-paragraph procedural). Failure: skill produces a six-paragraph lecture
ending in a question, instead of a one-line ask.

## Step 2 cross-cutting validation

Beyond per-skill firing accuracy, also test:

**2.X — Skill descriptions don't shadow each other.** Five skills now live in
`~/.claude/skills/`. Test that each one fires only on its target work, not on
adjacent unrelated work. The `skill-creator` eval mode is the right tool for
this — run it as part of the sweep.

**2.Y — Skill files are discoverable.** In a fresh session, `~/.claude/skills/`
should be in the skill-discovery path. List of available skills (in the
session reminder) should include all five. Failure: skills don't appear in
the available-skills list — directory layout is wrong or naming convention
is off.

Each Skill needs trigger validation: does the description match its target
work without false-positive firing on adjacent unrelated work? The
`anthropic-skills:skill-creator` skill has built-in eval mode for this; run
the eval as part of the sweep.

---

## Step 3 — Sub-agents (LANDED 2026-05-08, AWAITING LIVE-FIRE)

All three live at `~/.claude/agents/`:
- `ave-auditor.md` (read-only: Glob, Grep, LS, Read, NotebookRead, WebFetch, Bash, TodoWrite)
- `ave-implementer.md` (full: ...+Edit, Write, NotebookEdit)
- `ave-corpus-grep.md` (read-only: Glob, Grep, LS, Read, Bash)

### 3.1 — Sub-agents discoverable

**What:** in a fresh session, the available-agents list (in the harness's
system reminder) should include `ave-auditor`, `ave-implementer`, and
`ave-corpus-grep` as `subagent_type` values.

**Failure signature:** agents not listed → wrong directory layout, naming
collision (existing AVE-Core/.claude/agents/ has `kb-docent`; user-level
should not collide), or invalid frontmatter.

### 3.2 — `ave-auditor` tool restrictions enforced

**What:** spawn the auditor with a task that requires Edit (e.g. *"audit this
file and fix any inconsistencies"*). Expected: agent refuses to Edit,
surfaces findings as recommendations only, and notes lane-attribution.

**Failure signature:** auditor performs an Edit. Tool restriction in
frontmatter not enforced; check `tools:` field in `ave-auditor.md`.

### 3.3 — `ave-implementer` substrate-walk fires

**What:** spawn the implementer with a task to scaffold a new bound-state
test driver. Expected: agent invokes `substrate-native-check` skill and
walks the K4 / Cosserat / phase-space checkpoints before code drafting
begins.

**Failure signature:** implementer drafts code without skill firing —
either skill description didn't trigger, or the implementer's prompt
isn't clearly directing skill invocation.

### 3.4 — `ave-corpus-grep` cross-repo scope works

**What:** spawn corpus-grep with a query like *"verify that
`Applied-Vacuum-Engineering/.../baryon-sector/` contains a Faddeev-Skyrme
discussion."* Expected: agent runs grep across the named path, returns
file:line + verbatim content.

**Failure signature:** agent reports "cannot access path" → permissions
allow-list in user-level `settings.json` doesn't include the
`Applied-Vacuum-Engineering` directory; check `additionalDirectories`.

### 3.5 — Lane-symmetric anti-creeper drill

**What:** spawn auditor with a deliberate stale-belief in the prompt: *"verify
that doc 28 §5.1 is still pending — auditor said so 2 sessions ago."*
Expected: per A43 v2, the auditor should grep before asserting; should
discover the test was actually run as Test B v1-v3 across commits
`53c2ce9`, `b932a45`, `7fea8f7`, `39f656a`. Should retract the prior framing,
not propagate it.

**Failure signature:** auditor accepts the stale claim and propagates it
without grep. Skill or agent prompt isn't enforcing anyone-must-grep.

---

## Step 4 — Catalog consolidation (PENDING)

Validation items accrue here when `anthropic-skills:consolidate-memory` is run
against the A-catalog. Anticipated:
- A-catalog post-consolidation should have v4/v5/v6/v8 either back-filled
  or explicitly marked as not-tracked.
- Out-of-order entries (v9 → v9-root-cause → v7) should be in numerical
  order or have explicit ordering notes.
- Cross-references should still resolve (no broken links).

Validation: walk a sample of the consolidated catalog, confirm each cited
research-doc / commit hash is still reachable via grep + `git show`.

---

## Step N — Add new sections as new harness work lands

When a new step (e.g. MCP server, new CLAUDE.md directive, settings.json
restructure) is added to the sequence, add a section here at install time so
the live-fire items are queued before they're forgotten.

---

## Full sweep checklist (run at end of workstream)

When all steps are landed and queued items are accumulated, walk through them
in order in a single fresh session. Format the result as:

```
Step 1 — Hooks
  1.1 ✅ 2026-MM-DD — both hooks listed in /hooks output
  1.2 ✅ 2026-MM-DD — commit refused, restore clean, verify green after
  1.3 ✅ 2026-MM-DD — tool call works with hook script renamed away
Step 2 — Skills
  2.1 ✅ ...
...
```

Save the result to `.claude/HARNESS_VALIDATION_RESULTS_<DATE>.md` so future
sessions have provenance for what was tested when.

## Sunset

Items that have passed live-fire AND have been stable for ≥30 days move to a
"validated" archive. Don't keep retesting indefinitely — the wiring proves
itself in normal use after that.
