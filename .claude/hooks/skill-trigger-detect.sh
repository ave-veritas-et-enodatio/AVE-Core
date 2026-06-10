#!/bin/bash
# Hook: PreToolUse trigger-detect for AVE-discipline skills.
#
# Runs on Write|Edit|Bash tool calls; greps the proposed content/command for
# trigger keywords and lights an indicator lamp (stderr reminder) naming which
# skills may apply. Does NOT block (always exits 0).
#
# SELF-MAINTAINING (2026-06-09 rewrite): the keyword table is NO LONGER
# hardcoded here. Each skill declares its own detection regex in its frontmatter
# via a single-line `trigger_patterns:` field (a case-insensitive ERE, pipe-
# delimited). This hook DYNAMICALLY scans ~/.claude/skills/*/SKILL.md, unions
# every skill's declared patterns, and tests them against the tool-call content.
# Adding/removing/renaming a skill needs NO edit here — the skill carries its own
# trigger, co-located with its description. Skills without a `trigger_patterns:`
# field simply get no mechanical nudge (graceful — they still fire on
# agent-discipline via their description surfaced in the system reminder).
#
# To opt a skill into mechanical nudging, add to its frontmatter, e.g.:
#   trigger_patterns: 'phase.space|Lissajous|V_inc|V_ref|Clifford.torus'
# Keep the value a single-quoted single-line ERE with no ": " (colon-space).
#
# Plumber-physical: a passive sensor (current transformer) that reads what's
# flowing through the tool-call wire and lights a lamp if it detects current
# matching any skill's declared signature. The agent sees the lamp and chooses
# whether to invoke the skill via the Skill tool.
#
# Closes the 2026-05-18 gap (skills that should fire but don't, no auto nudge)
# AND the 2026-06-09 gap (the hardcoded table covered only ~13/39 skills and
# silently rotted every time a skill was added — none of the ion-compression-arc
# skills were in it). Companion doc: SKILL_TRIGGER_DETECT.md.

set -uo pipefail

SKILLS_DIR="${HOME}/.claude/skills"

# Read JSON payload Claude Code pipes to stdin
PAYLOAD=$(cat)
TOOL_NAME=$(printf '%s' "$PAYLOAD" | jq -r '.tool_name // empty' 2>/dev/null)

# Extract content based on tool type
CONTENT=""
FILE_PATH=""
case "$TOOL_NAME" in
    "Write")
        CONTENT=$(printf '%s' "$PAYLOAD" | jq -r '.tool_input.content // empty' 2>/dev/null)
        FILE_PATH=$(printf '%s' "$PAYLOAD" | jq -r '.tool_input.file_path // empty' 2>/dev/null)
        ;;
    "Edit")
        CONTENT=$(printf '%s' "$PAYLOAD" | jq -r '.tool_input.new_string // empty' 2>/dev/null)
        FILE_PATH=$(printf '%s' "$PAYLOAD" | jq -r '.tool_input.file_path // empty' 2>/dev/null)
        ;;
    "Bash")
        CONTENT=$(printf '%s' "$PAYLOAD" | jq -r '.tool_input.command // empty' 2>/dev/null)
        FILE_PATH=""
        ;;
    *)
        exit 0  # only fire on Write|Edit|Bash
        ;;
esac

# Skip if a FILE_PATH is set but is outside the AVE workspace (other repos use
# different disciplines). Bash calls have empty FILE_PATH and are always scanned.
if [[ -n "$FILE_PATH" ]] && [[ "$FILE_PATH" != *"AVE-Core"* ]] && [[ "$FILE_PATH" != *"AVE-staging"* ]] && [[ "$FILE_PATH" != *".claude/skills"* ]]; then
    exit 0
fi

# Combine FILE_PATH + CONTENT for matching
HAYSTACK="$FILE_PATH"$'\n'"$CONTENT"

# Accumulator for triggered-skill list
TRIGGERED=""

trigger() {
    local skill="$1"
    local reason="$2"
    TRIGGERED="${TRIGGERED}  • ${skill} — ${reason}"$'\n'
}

# ============================================================
# Dynamic scan: union every skill's declared trigger_patterns
# ============================================================
# One pass over all SKILL.md files; grep -H yields "path:trigger_patterns: '...'"
# only for skills that declare the field. Skill dir names contain no ':' so the
# split on ':trigger_patterns:' is unambiguous.
if [[ -d "$SKILLS_DIR" ]]; then
    while IFS= read -r line; do
        [[ -z "$line" ]] && continue
        file="${line%%:trigger_patterns:*}"
        raw="${line#*:trigger_patterns:}"
        # strip leading whitespace
        raw="${raw#"${raw%%[![:space:]]*}"}"
        # strip one layer of surrounding single quotes (the YAML scalar quoting)
        raw="${raw#\'}"; raw="${raw%\'}"
        [[ -z "$raw" ]] && continue
        # test the skill's ERE against the haystack (case-insensitive).
        # a malformed ERE makes grep exit 2 -> treated as no-match -> never breaks the hook.
        if printf '%s' "$HAYSTACK" | grep -qiE -- "$raw" 2>/dev/null; then
            sname="$(basename "$(dirname "$file")")"
            desc="$(grep -m1 '^description:' "$file" 2>/dev/null | sed 's/^description:[[:space:]]*//' | cut -c1-100)"
            [[ -z "$desc" ]] && desc="(see skill description)"
            trigger "$sname" "${desc}…"
        fi
    done < <(grep -H '^trigger_patterns:' "$SKILLS_DIR"/*/SKILL.md 2>/dev/null)
fi

# ============================================================
# Output reminder if any skills triggered
# ============================================================
if [[ -n "$TRIGGERED" ]]; then
    cat >&2 <<EOF
[skill-trigger-detect] potential skill matches for this tool call:
${TRIGGERED}
Per each skill's frontmatter description, consider invoking via:
  Skill(skill: "<skill-name>")
This is a non-blocking nudge (matched on each skill's declared trigger_patterns).
If a skill doesn't apply, proceed.
EOF
fi

# Always exit 0 — non-blocking nudge only
exit 0
