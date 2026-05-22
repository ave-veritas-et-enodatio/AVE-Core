# Hook Validation Plan

> Lives next to the scripts so it doesn't drift from them. Re-run after any hook
> change. Plumber-physical: this is the bench-test card you'd run after wiring a
> safety relay before the press goes back into production.

## Scope

Two hooks installed in [`.claude/settings.json`](../settings.json):

1. **`precommit-verify.sh`** — PreToolUse on `Bash`. Runs `make verify` before
   any `git commit ...` is allowed to land. Master interlock.
2. **`validation-table-watchdog.sh`** — PostToolUse on `Edit|Write`. Runs the
   paired regen script after edits to `manuscript/ave-kb/**/*-validation.md`.
   Latching alarm relay; surfaces drift via stderr on the agent's next turn.

## A. Bench-test (already done at install time)

Both scripts were bench-tested with simulated stdin payloads at install time.
To re-run after changes, paste these into a shell:

```bash
# precommit-verify.sh
HOOK=/Users/grantlindblom/AVE-staging/AVE-Core/.claude/hooks/precommit-verify.sh
echo '{"tool_input":{"command":"ls -la"}}' | "$HOOK"; echo "expect 0, got $?"
echo '{"tool_input":{"command":"git status"}}' | "$HOOK"; echo "expect 0, got $?"
echo '{"tool_input":{"command":"git -C /Users/grantlindblom/AVE-staging/AVE-HOPF commit -m test"}}' | "$HOOK"; echo "expect 0, got $?"
echo '{"tool_input":{"command":"git commit -m test"}}' | "$HOOK"; echo "expect 0 if make verify is green, 2 if red. got $?"

# validation-table-watchdog.sh
HOOK=/Users/grantlindblom/AVE-staging/AVE-Core/.claude/hooks/validation-table-watchdog.sh
echo '{"tool_input":{"file_path":"/tmp/foo.py"}}' | "$HOOK"; echo "expect 0, got $?"
echo '{"tool_input":{"file_path":"/Users/grantlindblom/AVE-staging/AVE-Core/manuscript/ave-kb/vol2/foo-validation.md"}}' | "$HOOK"; echo "expect 2 (advisory), got $?"
echo '{"tool_input":{"file_path":"/Users/grantlindblom/AVE-staging/AVE-Core/manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/ionization-energy-validation.md"}}' | "$HOOK"; echo "expect 0 if regen passes, 2 if drift. got $?"
```

All seven cases passed at install time (2026-05-07). Re-run after every hook
edit; if any case diverges from expected, the hook script has regressed.

## B. Live-fire — does Claude Code actually load the hooks?

The settings file change only takes effect on a fresh Claude Code session. To
verify the harness picked them up:

1. **Start a fresh session inside AVE-Core.** `cd /Users/grantlindblom/AVE-staging/AVE-Core` then launch.
2. **Run `/hooks`** (the slash command lists registered hooks). Both
   `precommit-verify.sh` and `validation-table-watchdog.sh` should appear under
   PreToolUse and PostToolUse respectively.
3. **If they don't appear:** settings.json has a schema issue, or the path is
   wrong. Run `jq . /Users/grantlindblom/AVE-staging/AVE-Core/.claude/settings.json`
   to confirm parse; then check that `command:` paths are absolute and the
   files are executable (`ls -la .claude/hooks/`).

## C. Live-fire — master interlock smoke test

**C1. Green-baseline commit succeeds.** With `make verify` currently passing,
ask the agent to make a trivial commit (e.g. amend a CHANGELOG line). Expected:
the hook runs `make verify`, takes ~1.2s, the commit lands. The agent sees no
hook output (silent allow).

**C2. Red-baseline commit blocked.** Temporarily reintroduce a violation —
fastest way: edit one of the verify-pure scripts to inline a constant
(`alpha = 1/137.036`). Then ask the agent to commit. Expected: commit refused;
stderr shows `COMMIT BLOCKED: make verify failed.` plus the last 30 lines of
verify output. Restore the violation after the test.

**C3. Different-repo commit not gated.** From inside AVE-Core, run
`git -C /Users/grantlindblom/AVE-staging/AVE-HOPF commit ...`. Expected: hook
exits 0 immediately; AVE-HOPF commit lands without AVE-Core's verify running.

**C4. Non-commit Bash pass-through.** `ls`, `git status`, `python -c '...'` —
all should be silent. The hook spawns but exits 0 in microseconds.

## D. Live-fire — watchdog smoke test

**D1. Edit a non-validation file.** Edit any `.py`, `.tex`, `README.md`, etc.
Expected: hook fires, fast-paths to exit 0, no output.

**D2. Edit the IE-table validation file.** Edit
[`manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/ionization-energy-validation.md`](../../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/ionization-energy-validation.md).
Expected: regen script runs (`verify_atomic_ie_manuscript_table.py`); if it
passes, exit 0 silent; if drift exists, exit 2 with stderr explaining the
drift. Either way, the edit lands (PostToolUse cannot block).

**D3. Edit an unmapped validation file.** Pick any other `*-validation.md` in
`manuscript/ave-kb/` (most don't have a regen yet). Expected: exit 2 with
"WATCHDOG (advisory): edited <path> ... No paired regen script is mapped."
This is intentional — A47 v13 says every validation file needs a regen, and
the watchdog forces that gap to be visible. Add the regen + a mapping entry
in `validation-table-watchdog.sh` before the file is committed.

## E. Failure-mode containment (run once, then once after every hook edit)

The scripts are designed to fail-open: cwd missing, jq missing, malformed
stdin, unhandled error path → exit 0 (allow), not exit 2 (block). To verify:

1. **Break the script temporarily.** `mv precommit-verify.sh precommit-verify.sh.bak`.
2. **Try a tool call.** Ask the agent to `ls`. Expected: tool call still works.
   Claude Code logs that the hook command was not found; doesn't refuse
   downstream calls.
3. **Restore.** `mv precommit-verify.sh.bak precommit-verify.sh`.

If the harness *did* refuse downstream calls, the hooks are mis-configured to
fail-closed — that's a worse failure than no hooks at all. Tighten settings.json.

## F. Ongoing validation (run periodically — say, monthly or after major refactors)

1. **Re-run the bench-test from §A.** All seven cases should still match
   expected exit codes.
2. **Time `make verify`.** Currently ~1.2s. If it drifts above ~30s, raise the
   `timeout: 120` in settings.json (or investigate why verify is slow).
3. **Audit watchdog mappings vs. actual validation files.**
   `find manuscript/ave-kb -name '*-validation.md'` lists all of them. The
   `case "$FILE_PATH" in` block in the watchdog should have a mapping for
   each. Gaps are A47 v13 work items.

## G. Sunset criteria

**Watchdog (`validation-table-watchdog.sh`) sunsets** when `make verify` is
extended to call all `verify_*.py` scripts (i.e., the IE-table regen and any
others added per A47 v13). At that point, the precommit interlock catches
drift on commit anyway, and the watchdog becomes redundant noise. Remove the
PostToolUse block from settings.json; the script can stay around for ad-hoc
bench-testing.

**Master interlock (`precommit-verify.sh`) sunsets** never, unless `make verify`
is replaced by a different gate. The interlock is the load-bearing safety
relay; even when CI in GitHub Actions is also gating, this catches drift
locally before it leaves the machine.

## H. Plumber-physical reference

| Hook | Circuit topology | Failure mode if hook breaks |
|---|---|---|
| `precommit-verify.sh` | Safety relay in series with contactor coil. Master interlock. | Fail-open: commit proceeds, no protection. |
| `validation-table-watchdog.sh` | Latching alarm relay parallel to contactor. Doesn't interrupt energization but lights the alarm. | Fail-open: edit lands, no advisory surfaced. |

Both fail-open by design — the cost of a false-block (Claude Code can't do
anything until the user untangles the hook) is higher than the cost of a
false-allow (one drift slips past until the next bench-test or session).
