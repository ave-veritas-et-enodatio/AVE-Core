# skill-trigger-detect — AVE skill autofire hook

**Hook**: `.claude/hooks/skill-trigger-detect.sh`
**Matcher**: `Write|Edit|Bash` (PreToolUse)
**Mode**: non-blocking nudge (always exits 0)
**Date encoded**: 2026-05-18
**Origin**: post-mortem of 2026-05-18 session — 11 AVE-discipline skills should have fired but didn't; root cause was no automatic mechanism (Phase 2 work flagged in `~/.claude/skills/README.md` §6)

## What it does

Before any `Write`, `Edit`, or `Bash` tool call in the AVE-Core repo, the hook:

1. Reads the JSON payload (file path, content, command) from stdin
2. Greps the content for trigger keywords matching skill descriptions
3. Outputs reminders to stderr listing which skills MAY apply
4. **Never blocks** — agent decides whether to invoke matched skill via `Skill` tool

## Trigger map (skill → trigger keywords/conditions)

### Pre-derivation discipline stack

| Skill | Trigger condition |
|---|---|
| `ave-prereg` | New `research/*.md` (not `_archive`) OR new `src/scripts/verify/*.py` |
| `ave-canonical-source` | Python file with hardcoded numerical constants (1/137.036, 6.674e-11, m_e, ℏ, e, etc.) |
| `consistency-vs-emergence` | `ave.core.constants` import OR CODATA target compare OR `8πα` formula |
| `substrate-native-check` | File in `src/ave/{solvers,topological,core}/` OR keywords: eigenvalue, Hessian, gradient descent, Lagrangian minimization |
| `pre-test-physics-check` | New file in `src/tests/` OR `*_prereg.md` |

### Test-design discipline

| Skill | Trigger condition |
|---|---|
| `phase-space-coordinate-check` | Keywords: phase space, Lissajous, phasor, V_inc, V_ref, Clifford torus, (p,q) knot, impedance plane |

### Post-result discipline

| Skill | Trigger condition |
|---|---|
| `ave-discrimination-check` | Keywords: load-bearing, AVE-distinct, STRONG POSITIVE, foreword promotion, canonical anchor, empirical confirmation |
| `ave-evidence-framing-discipline` | Keywords: approximately matches, within N%, rigorous, exact, survives, confirms, validates, demonstrates |
| `ave-independence-check` | Keywords: N independent, N instances, N pillars, N anchors, N confirmations, multi-confirmation |
| `verify-before-cite` | file:line citations (per `path:line`, at [path:line]) |

### Continuum-vs-discrete discipline

| Skill | Trigger condition |
|---|---|
| `ave-infinity-discipline` | Keywords: continuum limit, ℓ_node→0, UV divergence/cutoff, renormalization, RG flow, Clay-class |

### Audit cycle

| Skill | Trigger condition |
|---|---|
| `ave-audit` | About to invoke ave-auditor or ave-corpus-grep agent |
| `ave-walk-back` | Editing `divergence-test-substrate-map.md` or `closure-roadmap.md` |

## Example trigger output

When the hook detects matches, it outputs to stderr:

```
[skill-trigger-detect] potential skill matches for this tool call:
  • consistency-vs-emergence — constants.py or CODATA-target compare detected
  • ave-canonical-source — hardcoded numerical constant in Python script
  • ave-prereg — new verify script — corpus-grep prior work + pre-registration

Per ~/.claude/skills/SKILL.md descriptions, consider invoking via:
  Skill(skill: "<skill-name>")
This is a non-blocking nudge. If skill doesn't apply, proceed.
```

## Manual invocation pattern (for user)

Even with the hook firing automatically on agent tool calls, the user can ALSO trigger skills directly by typing `/skill-name` in chat:

```
User: /ave-prereg
User: /consistency-vs-emergence
User: /substrate-native-check
```

This invokes the skill immediately regardless of context. Useful when:
- You notice the agent about to skip a discipline
- You want to force a specific check before proceeding
- The hook missed a case (false negative)

## How to extend trigger rules

Edit `skill-trigger-detect.sh`. Each trigger rule is a `grep` test + `trigger` call:

```bash
if echo "$HAYSTACK" | grep -qE "your-pattern-here"; then
    trigger "skill-name" "human-readable reason"
fi
```

The `HAYSTACK` variable contains FILE_PATH + CONTENT concatenated. Patterns are POSIX extended regex.

## Testing the hook

Test against synthesized tool-call JSON:

```bash
cat <<'PAYLOAD' | /Users/grantlindblom/AVE-staging/AVE-Core/.claude/hooks/skill-trigger-detect.sh 2>&1
{"tool_name": "Write", "tool_input": {"file_path": "/path/to/file.py", "content": "your test content here"}}
PAYLOAD
```

## False-positive / false-negative discipline

This hook is a NUDGE not a GATE. False positives are fine (agent reads the nudge, decides skill doesn't apply, proceeds). False negatives are the failure mode to monitor — if a skill SHOULD have fired but the hook missed it, extend the trigger rules.

Track misses in `_audit-log/` per skills ecosystem convention (`~/.claude/skills/_audit-log/`).

## Cross-references

- `~/.claude/skills/README.md` §3 — pre-derivation discipline stack + scope-overlap map
- `~/.claude/skills/README.md` §6 — Phase 1 telemetry helpers (`bin/log_firing.py`, etc.)
- `~/.claude/skills/README.md` §6 §9.2 — Phase 2 hook plan (this is the implementation)
- `AVE-Core/research/SESSION_STATE_2026-05-18_LIGO-Phase5-thru-z0-pi-audit.md` §5 — the session that motivated this hook (11 missed firings)

## Discipline lesson

The hook does NOT replace agent-discipline of invoking `Skill` tool. It REMINDS the agent that a skill may apply. The agent still has to:

1. Read the reminder
2. Verify the skill applies to the current case
3. Invoke `Skill(skill: "name")` if it does
4. Document the firing per skill's own protocol

If the agent reads the nudge and decides not to invoke, that's a JUDGMENT CALL — log it as an override per `~/.claude/skills/bin/record_override.py`. Don't silently dismiss nudges; either invoke or document the dismissal.
