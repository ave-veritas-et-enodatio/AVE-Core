# CONSOLIDATED DIRECTIVE — DISCIPLINE / INFRASTRUCTURE LANE (authoritative)

> **Supersedes the original kickoff brief below** (Grant + auditor, 2026-06-14; re-verified workflow `w9kvxbm4i` + this session's groundings `w6thjru2y`/`w8qa61lvh`). Corrections folded in — act on these, not the survey headlines.

**Charter (unchanged):** owns *how the work is checked* — the gates, the skill/hook machinery. The content lanes consume its gates; it builds them. Kept independent because the gate-builder must not be a content-producer.

**Verified findings (correct the original brief):**
- **No harness auto-fire exists** (authoritative): skills run only via `/command` or agent-decision; PreToolUse hooks can only nudge/guard, never invoke. → Posture **(A) "repair auto-fire" is off the table.**
- **The logger is orphaned** (1 firing ever, 2026-05-17 build-day) and **`fire_count` is decorative/hand-set**. "Zero firings" is mostly *no instrumentation*, not measured silence.
- **AVE-Skills is not a mirror — same repo checked out twice** (root `612d402`). The "missing 19 arc skills" are **uncommitted untracked dirs in the live `~/.claude/skills` checkout** (+ 20 modified tracked). Consolidation = commit+push of uncommitted live work, **not** a copy job.
- **PR #146 already merged** (2026-06-10; hook live + self-maintaining on main). Backlog closed — correct memory. (`bdc76283` = content commit; merge = `059440d4`.)
- **The standing trap is real and structural:** PR #221's re-verify (`532e27d5`) was the *same* producer lane as the builder (`bfa94beb`), self-merged, zero reviews. `screened-winding-probe` still carries §0 "EXONERATED" + §8 "VERDICT DEMOTED" coexisting *by Rule-12 design*. **Every Rule-12-amended source is a latent salience-trap** = the gate's mechanical trigger.

**Decisions (ratified):**
- **Posture → B** (reposition skills as on-demand reference + declutter). *Ratified.*
- **Gate → (a)+(c)** (checklist + reusable workflow template, not a blocking CI hook). *Signed off.*

**Work items (priority order):**
1. **Build the parallel-site gate (highest leverage).** ✅ DONE — `_orchestration/parallel-site-gate.md` (standing discipline + merge-checklist line) + `parallel-site-gate.template.js` (reusable, lane-agnostic). Trigger = artifact aggregating ≥3 structurally-parallel entries, built by summarizing, about to be banked; "least-salient" = every un-flagged entry, priority on Rule-12-amended sources (grep trailing `DEMOTED|PANEL ADJUDICATION|AMENDMENT|SUPERSEDED|RETRACT|REVISED|walk-back`); independent lane re-verifies vs source's *latest appended adjudication*. Serves the field-decomposition lane + magic-angle audit landing too. First run `w8qa61lvh`: 10/10 genesis-ledger entries FAITHFUL.
2. **Execute posture B:** reposition the ensemble as reference; declutter pass *proposes* (does not pre-decide) retire/merge targets. — IN FLIGHT.
3. **AVE-Skills consolidation — 🔴 OUTWARD-FACING, HARD-GATED ON GRANT'S GO:** content-check all 19 untracked arc-skill dirs (intended? no secrets/scratch) → commit + push from live `~/.claude/skills` → retire the stale second checkout. **No push without explicit authorization.**
4. **`trigger_patterns` backfill** for the *kept* skills only (17/42 lack it) — folds into the declutter.
5. **Correct memory:** ✅ DONE — PR #146 merged/live; AVE-Skills one-repo-two-checkouts; logger orphaned; no auto-fire (see `project_discipline_infra_lane.md`).

**Standing constraints:** prime directive — do NOT add skills/hooks reflexively, bias to simplify + the one gate. Recursive caveat — this lane applies its *own* parallel-site gate + independent re-verify to its own edits before they land. `~/.claude/` is user-global (change minimally); `AVE-Core/.claude/` changes go via branch+PR. Re-ground before acting.

---

# KICKOFF BRIEF — DISCIPLINE / INFRASTRUCTURE HARDENING (the "process lane")

> ⚠️ **SUPERSEDED by the CONSOLIDATED DIRECTIVE above (2026-06-14).** Retained below for audit trail — its option (A) and its "PR#146 unmerged" / "AVE-Skills mirror" framings are corrected above.
> Landed 2026-06-14. Third orchestration lane, parallel to engine (physics) and documentation (canon).
> Relayable / self-contained. Grounding addendum appended at bottom (re-verified state, this session).

## Charter
This is the **third orchestration lane**, parallel to engine (physics) and documentation (canon). It owns **how the work is checked** — the gates, the discipline infrastructure, the skill/hook machinery. The two content lanes *consume* these gates; this lane *builds and maintains* them. Keeping it separate is itself a finding: the meta-audit showed the immune system is **lane independence**, so the lane that builds the gates must not be the lane that produces the content they check.

**Owns:** `~/.claude/skills/`, `~/.claude/skills/bin/`, the firing telemetry, `AVE-Core/.claude/hooks/`, the `_orchestration/` process docs.
**Does NOT own:** any physics derivation (engine lane), any KB/manuscript content (documentation lane). If a task requires a corpus or engine *judgment*, it routes back to those lanes — this lane only touches process/tooling.

## Grounded premise (the meta-audit finding, re-verified this session)
- **The immune system is the multi-lane REDUNDANCY, not in-lane skill-firing.** Every concrete catch across this entire arc was made by an *independent second lane* (producer/auditor split, adversarial fan-out, a sibling's fresh grep, or Grant) — never by a skill triggering inside the lane about to err.
- **Grounded telemetry (re-verified, not trusted):** 45 skills; 38 carry `fire_count` frontmatter; **36 at `fire_count:0`, 2 at `fire_count:1`.** The nudge hook (`AVE-Core/.claude/hooks/skill-trigger-detect.sh`) IS wired in `AVE-Core/.claude/settings.json`, and the logger exists (`~/.claude/skills/bin/log_firing.py`, firings dir `~/.claude/skills/_audit-log/firings`) — yet the machinery produces ~zero actual invocations.
- **The biggest blind spot is the SALIENCE-GRADIENT / PARALLEL-SITE lapse:** a discipline that holds at the salient site silently lapses at the structurally-identical *dull* one. It recurred 3× self-similarly (including on its own fix), is covered by no auto-firing skill, and is *currently the live defect* (the PR#221 ledger built from §0 headlines that missed the §8 demotion).

## 🔴 Prime directive (read before scoping any work)
**Do NOT reflexively add skills or hooks.** The finding is that the existing 45-skill ensemble doesn't fire. Building *more* discipline machinery repeats the thing that already doesn't work. The leverage is in (a) **one structural redundancy gate** and (b) a **strategic declutter** — bias toward *simplification*, not a bigger immune system. If a work item's output is "a new skill," stop and ask whether it should be a checklist line in the redundancy gate instead.

## Work items

### Item 1 — [highest leverage] The standing parallel-site re-verify gate
**Problem (grounded):** the salience-gradient lapse is live, recurring, and uncovered. It's the delivery mechanism by which the echo sneaks back in *after you already know better*.
**Task:** make this a *structural* step — "**an independent lane re-verifies the least-salient entries before any ledger / synthesis / PR merges.**"
**Design options (the lane picks — do not pre-decide):** (a) a documented standing discipline + merge-checklist line in `_orchestration/`; (b) a git pre-merge / CI check that flags multi-entry/repeated-structure artifacts for a parallel-site pass; (c) a reusable "merge-gate" workflow template that fans an independent lane over the dull entries.
**Lean:** the *lightest mechanism that actually gets followed* — a heavy hook risks the same non-firing fate as the skills. Probably (a) + optionally (c).
**The crux to solve:** define "least-salient entry" *mechanically* (e.g., for a ledger → every entry; for a multi-file PR → the look-uniform/repeated-structure files; the entries the producer did NOT explicitly flag). If the trigger isn't crisp, the gate won't fire.
**Urgency note:** enforce this **manually** on the imminent documentor PR merge *now* (an independent lane re-greps the dull entries) — don't wait for the structural version.

### Item 2 — [the load-bearing decision] Diagnose what the skills do, then set the posture
**Grounded fact:** 36/38 skills never invoked; nudge wired, ~0 invocations.
**Diagnostic (re-ground first):** determine which the skills actually are — (a) auto-fire catchers silently failing to fire, (b) a nudge that influences behavior without ever invoking the Skill tool, (c) disciplines now *absorbed* into lane behavior (so the skill needn't fire), or (d) dead weight. Check: does the nudge actually emit? does it ever lead to a Skill-tool call? is `log_firing.py` ever reached? are the disciplines baked into the lanes regardless of firing?
**The decision for Grant (posture):**
- **(A) Repair auto-fire** — wire nudge→invocation, activate the parked trigger-detect hook, make skills fire. *High effort, and the meta-finding suggests this isn't where the value is.*
- **(B) Reposition as a reference library** — accept skills are on-demand reference/encoded-knowledge, stop expecting auto-fire, move the investment to the redundancy gates (Item 1), and **declutter** (retire/merge dormant skills).
- **(C) Hybrid** — keep the few genuinely-load-bearing skills as fired; reposition the rest as reference.
**Recommendation to carry in:** the meta-audit leans **B/C** (redundancy is the immune system; don't over-invest in non-firing machinery). The lane *diagnoses and recommends*; **Grant decides** — this is the one genuine fork, surface it cleanly.

### Item 3 — [encode, per Item 2's decision] The operating principle + salience defense
Encode two disciplines *wherever Item 2 decides disciplines live* (a fireable skill if kept; the redundancy-gate checklist if repositioned — **do not create new skills if Item 2 says reposition**):
- **Operating principle:** "name the counterfactual *actually exercised*, both directions, before banking" — positive needs a should-fail control that *did* fail + a counterfactual it beats + no knob/plant/fit/headline in the loop; negative needs the effect *could* have appeared in that regime/carrier + closure by functional form, not a bare null.
- **Salience-gradient defense:** "apply the per-element check at *every* structurally-identical site, especially the dullest one."

### Item 4 — [triage only] The infra backlog
Triage (execute only what Item 2's posture justifies):
- The **self-maintaining trigger-detect hook PR** (memory: #146, unmerged/activation-deferred — **verify the actual state**, don't trust the memory).
- The deferred retroactive skill-self-audit scan (`ave-newly-created-skill-self-audit`'s logged follow-up).
- The AVE-Skills mirror of the recent arc skills (memory — verify).
- `trigger_patterns` frontmatter consistency across skills.

## Recursive caveat (load-bearing)
This lane **edits the discipline infrastructure itself** — which is *exactly* where the echo/salience lapses bite hardest (the trigger-detect hook's hardcoded table drifted once; `ave-newly-created-skill-self-audit` recursively failed its own audit). **The discipline lane is not exempt from the discipline:** it must apply its *own* parallel-site gate (Item 1) and an independent-lane re-verify to its *own* edits before they land.

## Re-ground-first discipline
Every item rests on meta-audit *survey* findings. The kickoff re-grounded the load-bearing one (the fire_count distribution + hook-wired state). The lane must re-ground the rest *before acting* — the *why* behind `fire_count:0`, the PR #146 state, the AVE-Skills mirror state. Acting on a survey headline without re-verify is the exact failure mode this lane exists to close.

## Scope + sensitivity
- `~/.claude/skills/` and `~/.claude/skills/bin/` are **user-global** (affect every session and project, not just AVE). Changes there are higher-stakes than a single repo's canon — test carefully, change minimally.
- `AVE-Core/.claude/hooks/` is git-tracked; changes go via branch + reviewed PR (protected main).
- This lane does **not** block engine or documentation; it runs in parallel / when bandwidth allows.

## How to run it
- **Lanes/agents:** `ave-corpus-grep` for grounding the telemetry/PR/backlog state; `ave-implementer` for hook/skill/checklist edits; `ave-auditor` (independent lane) to re-verify this lane's own edits per the recursive caveat.
- **Sequencing:** Item 1 first (it's the live leverage + protects the next merges) → Item 2 diagnostic → surface the posture fork to Grant → Items 3/4 per his decision.
- **Decisions queued for Grant:** (1) the skill posture (A/B/C, Item 2); (2) sign-off on the parallel-site gate mechanism (Item 1) once designed.

## Done-when
- The parallel-site re-verify is a *followed* standing step (not a hope).
- The skill posture is decided and the ensemble matches it (auto-fire repaired, or repositioned + decluttered).
- The operating principle + salience defense are encoded where they'll actually be used.
- The lane's own edits passed an independent-lane re-verify.

---

## GROUNDING ADDENDUM — re-verified state (2026-06-14, this session)

Re-grounded directly (grep/read/git, not trusted from survey or memory). Where the survey headline and ground-truth differ, ground-truth wins.

### Telemetry (confirmed + sharpened)
- **42** skill dirs carry `SKILL.md` (survey said "45"; the load-bearing distribution holds).
- **38** carry `fire_count` frontmatter; **exactly 2 nonzero** — `ave-evidence-framing-discipline:1`, `ave-module-library-discipline:1`; **36 at 0**. Matches survey.
- **The firing logger is ORPHANED.** Only one firing log exists: `_audit-log/firings/ave-evidence-framing-discipline.jsonl`, a single entry dated **2026-05-17 17:45** — the day the logging infra was built (a build-day seed). `ave-module-library-discipline` shows `fire_count:1` in frontmatter but has **no jsonl entry** → the `fire_count` numbers are decorative/manual, NOT produced by the logger. Nothing in any active config (`~/.claude/settings*.json`, `AVE-Core/.claude/settings.json`, any hook) calls `log_firing.py` — the only references are historical transcript text. **The logger has been reached exactly once, ever, on build day.**
- **The nudge hook is the self-maintaining version, active and wired** (`AVE-Core/.claude/settings.json` → PreToolUse on Write|Edit|Bash). It dynamically scans `~/.claude/skills/*/SKILL.md`, unions each skill's `trigger_patterns:` ERE, emits a **stderr nudge**, and **always exits 0 (non-blocking)**. It does **NOT** call `log_firing.py` and does **NOT** invoke any Skill — it is purely advisory. So the nudge and the logger are wholly disconnected: even when the nudge fires, nothing is logged and no skill is invoked.
- **Trigger coverage is partial:** only **25 of 42** skills carry `trigger_patterns:`. **17 are invisible to the nudge hook** (it can never name them): `ave-analytical-tool-selection`, `ave-audit-of-audit`, `ave-cavity-class-identification`, `ave-dimensional-provenance-check`, `ave-directory-enumeration-discipline`, `ave-driver-script-honesty`, `ave-ee-first-mapping`, `ave-ee-intuition-summary`, `ave-fundamental-ground-up-implementation`, `ave-handoff-canonical-locale`, `ave-ip-divide-discipline`, `ave-live-fire-derivation-provenance`, `ave-loop-gap-harness-discipline`, `ave-module-library-discipline`, `ave-multi-falsifier-triangulation-discipline`, `ave-sweep-audit`, `ave-worktree-paths`.

### Diagnostic implication for Item 2 (grounded)
The telemetry **cannot distinguish** "disciplines are dead" from "disciplines live as absorbed lane-behavior or on-demand reference," because the counter was **never wired to anything**. What IS established: the *auto-fire-and-log* machinery is effectively non-functional (one build-day seed firing; advisory-only nudge; orphaned logger; decorative counters). That is independent evidence for posture **B/C** — repairing auto-fire (A) means building the wiring from scratch (nudge→invocation→logger), and the meta-finding says that's not where the catches come from.

### Git state (corrects stale memory)
- **AVE-Core is on `main`, clean** (one unrelated untracked experimental file). Memory's "main checkout parked on PR#126/#146 branch" is **STALE**. Landing this brief in `AVE-Core/_orchestration/` (tracked, 87 files) is safe.
- The active `skill-trigger-detect.sh` (dated Jun 11) IS the self-maintaining version — so either PR #146 merged or the version was applied to main directly. **PENDING cross-repo/network re-verify** (Item 4): `gh pr view 146`, hook-file `git log`, AVE-Skills mirror state, and the live PR #221 documentor ledger.
