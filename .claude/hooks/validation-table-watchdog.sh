#!/bin/bash
# Hook: PostToolUse watchdog on Edit/Write of manuscript validation tables.
# Runs the paired regen script after the edit lands; surfaces drift via
# stderr (exit 2) on the next agent turn.
#
# Plumber-physical: latching alarm relay. The contactor (Edit) already
# energized — PostToolUse cannot block. But the alarm is now lit, the agent
# sees it on its next turn, and the precommit interlock will refuse the next
# commit until either (a) the table is reconciled to match engine output, or
# (b) the engine is reconciled to match the manuscript claim.
#
# A47 v9 / v13 wiring. Sunsets when `make verify` is extended to call all
# verify_*.py scripts; this hook becomes redundant with precommit-verify.sh.

set -uo pipefail

# Read JSON payload from stdin.
PAYLOAD=$(cat)
FILE_PATH=$(printf '%s' "$PAYLOAD" | jq -r '.tool_input.file_path // empty')

# Fast-path: only fire on AVE-Core manuscript validation tables.
case "$FILE_PATH" in
    */AVE-Core/manuscript/ave-kb/*-validation.md) ;;
    *) exit 0 ;;
esac

cd /Users/grantlindblom/AVE-staging/AVE-Core 2>/dev/null || exit 0  # fail-open

# Map validation file -> regen script. Extend this table as more verify_*.py land.
SCRIPT=""
case "$FILE_PATH" in
    *ionization-energy-validation*)
        SCRIPT="src/scripts/vol_1_foundations/verify_atomic_ie_manuscript_table.py"
        ;;
esac

# No mapping yet for this file: A47 v13 calls for one. Surface that explicitly
# so the agent knows the next step is "add the regen + map it here," not silence.
if [ -z "$SCRIPT" ]; then
    {
        echo "WATCHDOG (advisory): edited $FILE_PATH"
        echo
        echo "No paired regen script is mapped in"
        echo "  .claude/hooks/validation-table-watchdog.sh"
        echo
        echo "Per A47 v13 every validation table must have a paired verify_*.py"
        echo "script. Add the regen script and a mapping entry before this file"
        echo "is committed."
    } >&2
    exit 2
fi

LOG=/tmp/ave-validation-watchdog.log
if PYTHONPATH=src python3 "$SCRIPT" >"$LOG" 2>&1; then
    exit 0
fi

# Drift detected: surface to agent + user.
{
    echo "WATCHDOG: validation-table regen FAILED."
    echo
    echo "Edited file: $FILE_PATH"
    echo "Regen script: $SCRIPT"
    echo
    echo "The edit landed (PostToolUse cannot block), but the regen script"
    echo "no longer reproduces the values in the validation table. The next"
    echo "\`git commit\` will be refused by the precommit interlock until the"
    echo "drift is reconciled. Per flag-don't-fix: do NOT silently change"
    echo "either side; surface the contradiction to Grant first."
    echo
    echo "Last 20 lines of regen output:"
    echo "------------------------------"
    tail -20 "$LOG"
    echo "------------------------------"
    echo
    echo "Full log: $LOG"
} >&2
exit 2
