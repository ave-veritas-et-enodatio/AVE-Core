#!/bin/bash
# Hook: PreToolUse interlock on `git commit` inside AVE-Core.
# Runs `make verify`; blocks the commit (exit 2) if verify fails.
#
# Plumber-physical: safety relay on the contactor coil. The commit cannot
# energize unless the verify circuit closes. Fail-open on cwd / parsing errors
# (return 0 = allow) so a misconfiguration never bricks Claude Code.
#
# A47 v13 wiring: this is the master interlock. Once `make verify` is extended
# to call all manuscript-validation regen scripts, the PostToolUse watchdog
# becomes redundant with this gate.

set -uo pipefail

# Read the JSON payload Claude Code pipes to stdin.
PAYLOAD=$(cat)
COMMAND=$(printf '%s' "$PAYLOAD" | jq -r '.tool_input.command // empty')

# Fast-path: only fire on `git commit`. Allow all other Bash through.
case "$COMMAND" in
    *"git commit"*) ;;
    *"git -C"*" commit"*) ;;
    *) exit 0 ;;
esac

# If the commit explicitly targets a different repo via `git -C <path>`,
# don't run AVE-Core's verify. Bare `git commit` falls through to the run.
case "$COMMAND" in
    *"git -C "*"AVE-Core"*) ;;
    *"git -C "*) exit 0 ;;
    *) ;;
esac

cd /Users/grantlindblom/AVE-staging/AVE-Core 2>/dev/null || exit 0  # fail-open

LOG=/tmp/ave-precommit-verify.log
if make verify >"$LOG" 2>&1; then
    exit 0
fi

# Block: surface the failure to the agent + user via stderr.
{
    echo "COMMIT BLOCKED: make verify failed."
    echo
    echo "Last 30 lines of output:"
    echo "------------------------"
    tail -30 "$LOG"
    echo "------------------------"
    echo
    echo "Full log: $LOG"
    echo "Re-run:   cd /Users/grantlindblom/AVE-staging/AVE-Core && make verify"
} >&2
exit 2
