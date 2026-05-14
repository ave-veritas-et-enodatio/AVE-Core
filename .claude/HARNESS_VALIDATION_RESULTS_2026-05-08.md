# Harness Validation Sweep — Results 2026-05-08

> Single-session live-fire walk of [`HARNESS_VALIDATION_QUEUE.md`](HARNESS_VALIDATION_QUEUE.md)
> against the harness installed in commits `b9830f7` + `9c71e37`.
> Per `feedback_validate_what_you_did` (batch at end of workstream) and
> `feedback_flag_dont_fix` (surface defects with verbatim evidence; do not
> silently repair).

**Status:** 17 of 20 ✅ pass · 2 ❌ fail · 1 ⏸ blocked. Hook layer is the failure
locus; skill layer + sub-agent layer are clean.

---

## Full sweep checklist

```
Step 1 — Hooks
  1.1 ❌ 2026-05-08 — hook NOT loaded (disambiguated via 1.2 — see below)
  1.2 ❌ 2026-05-08 — `git commit` of red-baseline file (1/137.036 literal at
                     dark_wake_chiral_validation.py:256) landed clean as commit
                     fe7c83e WITHOUT `make verify` running — precommit-verify.sh
                     did not fire. (Test commit reset --soft + file restored to
                     ALPHA; HEAD now back to 9c71e37, working tree clean.)
  1.3 ⏸  2026-05-08 — BLOCKED: with hooks not firing at all, renaming the script
                     while running harmless Bash cannot disambiguate fail-open
                     from "hook never engaged." Re-test once 1.1/1.2 are
                     reconciled.

Step 2 — Skills
  2.Y ✅ 2026-05-08 — all 5 skills present in the available-skills system
                     reminder: verify-before-cite, substrate-native-check,
                     phase-space-coordinate-check, consistency-vs-emergence,
                     pre-test-physics-check
  2.1a ✅ 2026-05-08 — verify-before-cite fires on canonical citation
                     ("doc 28 §5.1 V_inc/V_ref phasor")
  2.1b ✅ 2026-05-08 — does NOT fire on hypothetical ("if doc said X, what
                     would that imply") — sub-agent correctly cited the skill's
                     explicit "Do NOT fire on" hypotheticals clause
  2.1c ✅ 2026-05-08 — fires on incentivized citation trap (claim "ALPHA at
                     line 250"); sub-agent named Read-with-offset + grep -n
                     ALPHA as the verification path before asserting
  2.2a ✅ 2026-05-08 — substrate-native-check fires on solver scaffold
                     (`src/ave/solvers/` eigsolver)
  2.2b ✅ 2026-05-08 — does NOT fire on logging-only refactor (sub-agent named
                     skill's pure-infrastructure exclusion)
  2.2c ✅ 2026-05-08 — substrate-native-check Ckpt 4 + phase-space-coordinate-
                     check both fire on (2,3) test in lattice-Cartesian (the
                     A46 trap)
  2.3a ✅ 2026-05-08 — phase-space-coordinate-check fires on Op10 c=N (2,3)
                     topology test
  2.3b ✅ 2026-05-08 — does NOT fire on time-domain energy-conservation
                     regression (sub-agent cited skill's conservation-test
                     exclusion)
  2.4a ✅ 2026-05-08 — consistency-vs-emergence fires on `α = e²/(4πε₀ℏc)`
                     test using ave.core.constants for inputs; sub-agent
                     correctly classified Identity-class structural
                     circularity per A47 v17
  2.4b ✅ 2026-05-08 — fires on tautological regression `assert |computed −
                     ALPHA_COLD_INV| < 1e-12`; classified as A47 v16 tautology
  2.4c ✅ 2026-05-08 — fires on manuscript-table validation; demands
                     commit-SHA pin or paired verify_*.py per A47 v11c
  2.5a ✅ 2026-05-08 — pre-test-physics-check fires on new L3 bound-state
                     pre-reg
  2.5b ✅ 2026-05-08 — does NOT fire on regression test for already-fixed bug
                     (no new empirical question)
  2.5c ✅ 2026-05-08 — question to Grant is one sentence, plumber-physical,
                     about substrate not implementation. Sub-agent draft:
                     *"Plumber-wise, is the (V-sector) corpus electron at
                     σ ≈ 0.0357 a free standing eigenmode of the K4-TLM
                     block-Helmholtz operator, or is it a driven equilibrium
                     that only exists when something is pumping it?"* — the
                     same free-vacuum-vs-driven-equilibrium framing Rule 16
                     cites as the R7.1 collapse case.
  2.X ✅ 2026-05-08 — no shadowing observed between the 5 skills; each fires
                     only on its target work in the cluster tests above.
                     Note: skill-creator eval mode was not invoked
                     separately (caveat below).

Step 3 — Sub-agents
  3.1 ✅ 2026-05-08 — ave-auditor, ave-implementer, ave-corpus-grep all
                     present in the available-agents system reminder
  3.2 ✅ 2026-05-08 — ave-auditor refused Edit on a "find inconsistency
                     and fix it inline" task; performed read-only audit,
                     found no inconsistency, surfaced as recommendation
                     with explicit lane-attribution. (Independent finding:
                     §3 and §4.2 of doc 28 are consistent on phase-vs-real
                     space R/r — no fix needed.)
  3.3 ✅ 2026-05-08 — ave-implementer named all 5 substrate-discipline
                     skills before drafting code (substrate-native-check,
                     phase-space-coordinate-check, pre-test-physics-check,
                     consistency-vs-emergence, verify-before-cite) AND
                     surfaced a one-sentence plumber-physical question to
                     Grant before pre-reg lands. Caveat below.
  3.4 ✅ 2026-05-08 — ave-corpus-grep grepped Applied-Vacuum-Engineering,
                     returned ~70 Faddeev-Skyrme hits with file:line +
                     verbatim, plus authority caveat (archive is reference-
                     only; AVE-Core is canonical)
  3.5 ✅ 2026-05-08 — ave-auditor REFUSED to propagate stale "doc 28 §5.1
                     pending" belief; grepped, found Test B v1 / v1-retry /
                     v2 / v3 ran 2026-04-26 across SHAs 53c2ce9, b932a45,
                     7fea8f7, 39f656a; retracted prior framing with
                     verbatim git-show evidence. Anti-creeper discipline
                     load-bearing.
```

---

## Defects to surface (per `feedback_flag_dont_fix`)

### DEFECT 1 — precommit-verify.sh hook does not fire on `git commit` Bash calls

**Severity:** HIGH. The hook layer is the master interlock per A47 v13 wiring.
If commit cannot be blocked on red-baseline `make verify`, the discipline
relies entirely on agent vigilance — exactly what the hook was installed to
backstop.

**Verbatim evidence:**

- Substituted `np.sqrt(2 * (1/137.036))` back into
  `src/scripts/vol_1_foundations/dark_wake_chiral_validation.py:256` (the
  exact literal `verify_universe.py`'s magic-number guard scans for).
- Ran `git commit -am "test: hook interlock smoke"`.
- Bash returned: `[research/l3-electron-soliton fe7c83e] test: hook interlock smoke / 1 file changed, 1 insertion(+), 1 deletion(-)` — i.e., commit succeeded with no `COMMIT BLOCKED` stderr, no `make verify` invocation, no exit-2 refusal.
- Reset via `git reset --soft HEAD~1`; restored file to `ALPHA`; HEAD back at `9c71e37`; `git status --short` clean; `git diff HEAD` empty.

**Wiring confirmed correct (so failure is at the harness load layer, not the
script layer):**

- `.claude/settings.json` parses; `jq .hooks` returns the expected
  `PreToolUse` matcher `Bash` → `precommit-verify.sh` plus `PostToolUse`
  matcher `Edit|Write` → `validation-table-watchdog.sh` with absolute paths
  and 120s/90s timeouts.
- Both scripts exist, are executable (`-rwxr-xr-x`), and bench-tested clean
  per [`hooks/VALIDATION.md`](hooks/VALIDATION.md) (per the queue, 7/7
  cases).
- User-level `~/.claude/settings.json` contains zero hook entries
  (`grep -c '"hooks"'` returns 0), so there is no user-level override
  shadowing the project-level config.

**Most likely root causes (hypotheses for Grant to decide between, not for me
to silently fix):**

1. **Project-level hook approval gate.** Claude Code may require explicit
   user approval of project-level hooks (running `/hooks` interactively in
   an authoritative session and accepting them) before they execute, as a
   supply-chain-safety measure. The settings.json defines them; the user
   has not yet approved them at the harness level for this session. This
   matches the queue's anticipated 1.1 failure signature ("if hooks don't
   appear in /hooks list, harness didn't load the new settings.json") —
   except they DID load configurationally; they are just not engaged.
2. **Timing / session-scope.** The hook scripts were installed in commit
   `9c71e37` (2026-05-07/08), but Claude Code's session-start hook
   discovery may have cached an earlier settings state. A fresh restart
   of the Claude Code CLI in this directory may be sufficient.
3. **`tool_input.command` JSON shape mismatch.** The hook reads
   `.tool_input.command` from stdin. If Claude Code is now piping a
   different JSON shape (e.g. `.parameters.command` or wrapping it
   differently), the `case "$COMMAND" in *"git commit"*) ;;` match never
   succeeds and the hook silently exits 0 on every Bash call. **A 30-second
   diagnostic that disambiguates 1 vs 2/3:** add an `echo
   "$PAYLOAD" >> /tmp/hook-ping.log` line at the top of
   `precommit-verify.sh`, run any Bash via Claude Code, and check whether
   the file appears. If empty: hook never fires (1 or 2). If populated:
   hook fires but JSON shape mismatch (3) — fix the jq path.

**Reconciliation is Grant's call.** Diagnostic is read-only; suggested but
not executed.

### DEFECT 2 — `AVE-Core/CLAUDE.md` content is atopile/PCB material, not AVE

**Severity:** MEDIUM. CLAUDE.md auto-loads into every session that starts in
or near AVE-Core. Currently the file's content is a 20 KB atopile/ato
declarative DSL tutorial (PCB design, modules, components, traits, ato
syntax, package generation, footprint selection). It is correct atopile
content — just not for this project.

**Verbatim evidence:**

```
$ head -5 /Users/grantlindblom/AVE-staging/AVE-Core/CLAUDE.md
# CLAUDE.md

ato is a declarative DSL to design electronics (PCBs) with.
It is part of the atopile project.
Atopile is run by the vscode/cursor/windsurf extension.
```

File timestamp: `Mar 30 20:47`, size 20086 bytes. Predates the harness work
(b9830f7/9c71e37 are May).

**Effect on harness behavior:** every session loads ~20 KB of irrelevant
declarative-DSL syntax, library-module APIs, package-generation procedures,
and "vibe coding a project" guidance into context. None of it relates to
K4-TLM, Cosserat, AVE substrate, A-catalog discipline, lane symmetry,
research-doc structure, or any AVE concept. It would push real AVE-relevant
context out of the prompt budget and could induce wrong defaults
("declarative DSL" framing for Python solver code, etc.).

**Reconciliation is Grant's call.** Suspect leftover from an earlier
project initialization (`/init` command or copied template) that was never
replaced with AVE-specific guidance. Whether to (a) replace with an
AVE-discipline summary, (b) delete entirely, or (c) move to a sibling
filename so the auto-load is opt-in — not for me to pick.

---

## Caveats on what was tested

- **Skill-trigger tests (2.1a–2.5c)** were behavior-judgment tests run by
  spawning sub-agents who were instructed to read the SKILL.md first and
  decide whether each prompt would trigger. This confirms (a) the skill
  descriptions are well-targeted relative to the queue's prompts and (b)
  an agent that has the skill in context applies its trigger logic
  correctly. It does NOT confirm that Claude Code's auto-trigger
  mechanism spontaneously surfaces the skill name to a fresh agent before
  the agent starts the task. That deeper test would require a session
  where a sub-agent was given a target task without being told about the
  skills, and observing whether it volunteers the skill invocation.
  Recommendation: defer that test to organic future use; if the skill
  fires in actual implementer/auditor work over the next 30 days, mark
  validated; if not, re-run a no-prompt-hint version.
- **`anthropic-skills:skill-creator` eval mode** was NOT run as a separate
  cross-shadowing audit. The queue's 2.X note suggested it. Manual
  inspection of the five descriptions found no false-positive language
  overlap, but the eval mode is the more rigorous tool. Defer.
- **Step 3.3 (ave-implementer substrate walk)** — the implementer
  sub-agent named the five skills it would invoke and articulated the
  substrate-walk checkpoints, but its tool-use trace shows zero Read /
  Grep calls in this turn. Because the prompt explicitly said "STOP at
  the substrate-walk / pre-design phase," that is expected — but the test
  does not confirm the agent would ACTUALLY grep doc 28 / doc 73 / etc.
  before drafting code if asked to proceed. The discipline is *named* and
  load-bearing in the agent's framing; whether it is *executed* needs
  organic future use to confirm.
- **Step 1.3** is genuinely blocked, not just untested. Re-running it
  before the hook layer is reconciled provides no additional signal.

---

## Repo state after sweep

```
$ git status --short
(empty — working tree clean)

$ git log --oneline -3
9c71e37 chore: install Claude Code harness — hooks + validation queue
b9830f7 fix: migrate 137.036 literal to ALPHA in dark_wake_chiral_validation
6844cc0 research(docs 107-108 + L5 layer + κ̃ refactor): ...
```

Test commit `fe7c83e` was created during 1.2, soft-reset, and the file
content restored. The commit object remains in the local reflog but is no
longer reachable from any branch.

---

## Recommendation

Per the queue's failure-handling rule ("Any ❌ blocks moving to the next
step"), the hook layer (Step 1) is currently a hard block on relying on
either the precommit interlock or the validation-table watchdog as a
trusted backstop. Skills layer + sub-agent layer are validated; those
primitives can be relied on now.

Surfacing for Grant:
1. **DEFECT 1** — diagnose hook-firing failure (suggested 30s diagnostic
   above). Likely either an interactive `/hooks` approval gate or a JSON
   shape mismatch in the hook's stdin parser.
2. **DEFECT 2** — replace or remove `AVE-Core/CLAUDE.md` atopile content.
3. **Caveat queue** — schedule organic re-test of skills 2.1–2.5 over
   normal use; if no spurious triggers / no missed triggers in 30 days,
   sunset to validated archive.
