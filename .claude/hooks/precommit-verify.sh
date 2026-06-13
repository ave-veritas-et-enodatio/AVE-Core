#!/bin/bash
# Hook: pre-commit verify gate for AVE-Core. Dual-context AND worktree-aware.
#
# This one file runs in TWO contexts:
#   (1) git-native pre-commit hook  (.git/hooks/pre-commit -> this file; shared
#       by every worktree through the common git dir). git runs it with EMPTY
#       stdin and cwd = the committing worktree.
#   (2) Claude Code PreToolUse interlock (matcher "Bash", absolute path in the
#       tracked .claude/settings.json). Claude pipes a JSON payload on stdin;
#       we fire only on `git commit`.
#
# In BOTH contexts we resolve the WORKTREE BEING COMMITTED and run `make verify`
# THERE (`make -C <worktree>`) — never a hardcoded main-checkout path — so the
# worktree's code is validated against itself. (The Makefile puts the worktree's
# own src/ on PYTHONPATH and pytest gets it via pyproject.toml; otherwise the
# editable-install .pth would import the MAIN checkout's ave/* from any worktree
# and the gate would validate the wrong tree.) Fail-open (exit 0) on any
# resolution / parse error so a misconfiguration never bricks commits.
#
# Plumber-physical: safety relay on the contactor coil. The commit cannot
# energize unless the verify circuit closes — and the relay now senses the
# panel actually being worked on, not a hardcoded one.

set -uo pipefail

PAYLOAD=$(cat)

# --- Resolve the working tree being committed -------------------------------
CONTEXT=""
TARGET=""
if [ -n "$PAYLOAD" ] && printf '%s' "$PAYLOAD" | jq -e . >/dev/null 2>&1; then
    # Context (2): Claude Code PreToolUse interlock (JSON payload on stdin).
    CONTEXT="interlock"
    COMMAND=$(printf '%s' "$PAYLOAD" | jq -r '.tool_input.command // empty')
    HOOK_CWD=$(printf '%s' "$PAYLOAD" | jq -r '.cwd // empty')

    # Fire only on `git commit`. Allow all other Bash through untouched.
    case "$COMMAND" in
        *"git commit"*) ;;
        *"git -C "*" commit"*) ;;
        *) exit 0 ;;
    esac

    # Where will the commit run? Prefer an explicit dir named in the command
    # (`git -C <dir> ... commit`, or a leading `cd <dir> && ...`); else fall
    # back to the session cwd. .cwd is the pre-command working directory, which
    # is authoritative for a bare `git commit` (the dominant pattern: implementor
    # sessions launched in their worktree, and Agent isolation:"worktree").
    if printf '%s' "$COMMAND" | grep -qE '(^|[;&|[:space:]])git[[:space:]]+-C[[:space:]]'; then
        TARGET=$(printf '%s' "$COMMAND" \
            | sed -nE "s/.*git[[:space:]]+-C[[:space:]]+(\"([^\"]+)\"|'([^']+)'|([^[:space:]]+)).*/\2\3\4/p" \
            | head -1)
    elif printf '%s' "$COMMAND" | grep -qE '^[[:space:]]*cd[[:space:]]'; then
        TARGET=$(printf '%s' "$COMMAND" \
            | sed -nE "s/^[[:space:]]*cd[[:space:]]+(\"([^\"]+)\"|'([^']+)'|([^[:space:];&|]+)).*/\2\3\4/p" \
            | head -1)
    fi
    [ -z "$TARGET" ] && TARGET="$HOOK_CWD"
else
    # Context (1): git-native pre-commit hook (git passes empty / non-JSON
    # stdin). git runs us with cwd = the committing worktree's root.
    CONTEXT="git-native"
    TARGET="$(pwd)"
fi

# Normalize to the worktree root; fail-open if it isn't a git working tree.
REPO=$(git -C "$TARGET" rev-parse --show-toplevel 2>/dev/null) || exit 0
[ -n "$REPO" ] || exit 0

# Only gate AVE-Core working trees. Sentinel = the canonical constants module
# plus a Makefile `verify` target — no hardcoded path or dir-name, so a
# `git -C ../SomeOtherRepo commit` issued through Claude is correctly left alone.
[ -f "$REPO/src/ave/core/constants.py" ] || exit 0
grep -qE '^verify:' "$REPO/Makefile" 2>/dev/null || exit 0

# Dry-run for validation / debugging: report the resolution and exit (no make).
if [ -n "${AVE_PRECOMMIT_DRYRUN:-}" ]; then
    echo "ave-precommit DRYRUN: context=$CONTEXT target=$TARGET repo=$REPO" >&2
    exit 0
fi

# Drop git hook env so `make verify`'s own tooling never touches the in-flight
# commit's staged index / refs.
unset GIT_INDEX_FILE GIT_DIR GIT_PREFIX GIT_WORK_TREE GIT_OBJECT_DIRECTORY

# --- De-dupe verify across the two contexts ---------------------------------
# A Claude-driven commit verifies once in the interlock; that SAME commit then
# fires the git-native hook, which would otherwise verify the identical tree
# again. Fingerprint the prospective commit (HEAD + staged diff — both reads,
# no index lock, identical in either context) and let the git-native hook skip
# a verify the interlock just did. A manual CLI commit of *different* staged
# content has a different fingerprint, so it still re-verifies (safe default).
FP=$({ git -C "$REPO" rev-parse HEAD 2>/dev/null; git -C "$REPO" diff --cached 2>/dev/null; } \
        | shasum 2>/dev/null | cut -d' ' -f1)
MARKER=""
[ -n "$FP" ] && MARKER="/tmp/ave-verify-ok.$FP"

if [ "$CONTEXT" = "git-native" ] && [ -n "$MARKER" ] && [ -f "$MARKER" ]; then
    NOW=$(date +%s 2>/dev/null || echo 0)
    THEN=$(cat "$MARKER" 2>/dev/null || echo 0)
    AGE=$(( NOW - THEN ))
    if [ "$AGE" -ge 0 ] && [ "$AGE" -lt 120 ]; then
        exit 0   # this exact tree was verified < 120 s ago by the interlock
    fi
fi

# --- Run the gate in the committing worktree --------------------------------
LOG="/tmp/ave-precommit-verify.$$.log"
if make -C "$REPO" verify >"$LOG" 2>&1; then
    [ -n "$MARKER" ] && date +%s >"$MARKER" 2>/dev/null
    rm -f "$LOG"
    exit 0
fi

# Block: surface the failure to the agent + user via stderr.
{
    echo "COMMIT BLOCKED: make verify failed in $REPO"
    echo
    echo "Last 30 lines of output:"
    echo "------------------------"
    tail -30 "$LOG"
    echo "------------------------"
    echo
    echo "Full log: $LOG"
    echo "Re-run:   make -C $REPO verify"
} >&2
exit 2
