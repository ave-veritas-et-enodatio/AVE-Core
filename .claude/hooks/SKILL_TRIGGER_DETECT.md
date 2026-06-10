# skill-trigger-detect — AVE skill autofire hook

**Hook**: `.claude/hooks/skill-trigger-detect.sh`
**Matcher**: `Write|Edit|Bash` (PreToolUse)
**Mode**: non-blocking nudge (always exits 0)
**Date encoded**: 2026-05-18
**Rewritten self-maintaining**: 2026-06-09
**Origin**: post-mortem of 2026-05-18 session — 11 AVE-discipline skills should have fired but didn't; root cause was no automatic mechanism (Phase 2 work flagged in `~/.claude/skills/README.md` §6). The 2026-06-09 rewrite closed a *second* gap: the original keyword table was hardcoded in the hook and covered only ~13 of 39 skills, and silently rotted every time a skill was added (none of the 2026-06-09 ion-compression-arc skills were in it).

## What it does

Before any `Write`, `Edit`, or `Bash` tool call in the AVE workspace, the hook:

1. Reads the JSON payload (file path, content, command) from stdin
2. **Dynamically scans** `~/.claude/skills/*/SKILL.md`, reads each skill's declared `trigger_patterns` regex, and tests it against FILE_PATH + CONTENT
3. Outputs reminders to stderr listing which skills MAY apply
4. **Never blocks** — agent decides whether to invoke the matched skill via the `Skill` tool

## Self-maintaining design (2026-06-09)

The keyword→skill table is **no longer hardcoded in the hook**. Each skill owns its
own mechanical trigger, declared as a single line in its frontmatter:

```yaml
trigger_patterns: 'phase.space|Lissajous|V_inc|V_ref|Clifford.torus|impedance.plane'
```

The hook unions every skill's `trigger_patterns` at runtime. Consequences:

- **Adding / removing / renaming a skill needs NO edit to the hook.** The trigger
  travels with the skill (co-located with its `description`), vanishes if the skill
  is deleted, and follows a rename.
- **Opt-in + graceful degradation.** A skill *without* `trigger_patterns` simply
  gets no mechanical nudge — it still fires on agent-discipline (its `description`
  surfaced in the system reminder). No skill is ever broken by the absence of the
  field.
- **Single source of truth.** A skill's semantic trigger (`description`) and its
  mechanical trigger (`trigger_patterns`) live in the same file. They can't drift
  into two separate registries.

### `trigger_patterns` authoring rules

- A **single-quoted, single-line POSIX ERE**, pipe-delimited alternation.
- Matched **case-insensitively** (`grep -iE`) against `FILE_PATH\nCONTENT`, so a
  path fragment (`src/ave/solvers/`) and a content keyword both work in one field.
- **No `": "` (colon-space)** in the value — the harness frontmatter loader is
  line-based, and a colon-space could read as a new key. (Backslashes are fine —
  YAML single-quoted scalars keep them literal, e.g. `\(2,3\)`, `6\.674e-11`.)
- Keep it **specific** — the hook fires on every Write/Edit/Bash, so an over-broad
  pattern produces nudge-spam the agent learns to ignore. Prefer false-negatives
  (rely on agent-discipline) over false-positive noise.
- A malformed ERE makes `grep` exit 2, which the hook treats as no-match — a bad
  pattern in one skill **never breaks the hook or the other skills**.

As of 2026-06-09, 23 skills declare `trigger_patterns` (the 13 originally hardcoded
+ the 6 ion-compression-arc skills + `ave-canonical-leaf-pull`,
`ave-power-category-check`, `ave-discipline-translate`,
`ave-newly-created-skill-self-audit`). The remaining ~16 skills rely on
agent-discipline; add `trigger_patterns` to any of them to opt into nudging.

## Example trigger output

```
[skill-trigger-detect] potential skill matches for this tool call:
  • ave-conserved-vs-pumped — Use this skill BEFORE testing, deriving, or asserting that any AVE substrate quantity can be "built …
  • ave-prereg — Use this skill at the START of any new derivation, calculation, or analytical claim …
  • pre-test-physics-check — Use this skill at the START of any new test design …

Per each skill's frontmatter description, consider invoking via:
  Skill(skill: "<skill-name>")
This is a non-blocking nudge (matched on each skill's declared trigger_patterns).
If a skill doesn't apply, proceed.
```

The reason line is the skill's own `description` (first ~100 chars), pulled live.

## Manual invocation pattern (for user)

Even with the hook firing automatically on agent tool calls, the user can ALSO trigger skills directly by typing `/skill-name` in chat (e.g. `/ave-prereg`, `/substrate-native-check`). Useful when you notice the agent about to skip a discipline, or the hook missed a case.

## How to extend coverage

**Do not edit the hook.** To add a mechanical nudge for skill X, add a
`trigger_patterns:` line to `~/.claude/skills/X/SKILL.md`'s frontmatter (right
after `description:`), following the authoring rules above. The hook picks it up
on the next tool call. To change a skill's trigger, edit that skill's field.

The hook itself only needs editing for I/O-contract changes (new tool matchers,
output format) — not for skill coverage.

## Testing the hook

```bash
cat <<'PAYLOAD' | /Users/grantlindblom/AVE-staging/AVE-Core/.claude/hooks/skill-trigger-detect.sh 2>&1
{"tool_name": "Write", "tool_input": {"file_path": "/path/under/AVE-Core/file.py", "content": "your test content"}}
PAYLOAD
```

Validated 2026-06-09 across 8 cases (solver path, "pump the spin" content, auditor
spawn, phase-space doc, non-AVE-path skip, new-SKILL.md write, malformed JSON,
timing). ~0.21 s/call (heaviest case, 23 patterns) — well under the 5 s timeout.

## False-positive / false-negative discipline

This hook is a NUDGE not a GATE. False positives are fine (agent reads the nudge, decides the skill doesn't apply, proceeds). False negatives are the failure mode to monitor — if a skill SHOULD have fired but didn't, tighten/add that skill's `trigger_patterns`. Track misses in `~/.claude/skills/_audit-log/`.

## Cross-references

- `~/.claude/skills/README.md` §3 — pre-derivation discipline stack + scope-overlap map
- `~/.claude/skills/README.md` §6 — Phase 1 telemetry helpers + Phase 2 hook plan (this is the implementation)
- `AVE-Core/research/SESSION_STATE_2026-05-18_LIGO-Phase5-thru-z0-pi-audit.md` §5 — the session that motivated this hook (11 missed firings)

## Discipline lesson

The hook does NOT replace agent-discipline of invoking the `Skill` tool. It REMINDS the agent that a skill may apply. The agent still has to read the reminder, verify the skill applies, invoke `Skill(skill: "name")` if it does, and document the firing per the skill's own protocol. If the agent reads the nudge and decides not to invoke, that's a JUDGMENT CALL — log it as an override per `~/.claude/skills/bin/record_override.py`. Don't silently dismiss nudges; either invoke or document the dismissal.
