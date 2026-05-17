# Skill Ensemble Overhaul: Plan & Protocol

**Date**: 2026-05-17
**Status**: planning doc — not yet implemented
**Scope**: governs `~/.claude/skills/ave-*/` (currently 18 skills)
**Trigger**: meta-observation that skill maintenance has been ad-hoc since ensemble inception; without infrastructure, skills will fossilize, accumulate, and lose calibration as the framework matures.

---

## 0. Frame

The skill ensemble is a **procedural policy refined by sparse human feedback**. Each SKILL.md encodes a discipline move that catches a specific failure mode. The corpus has grown through audit-cycle-driven encoding: when the user catches a failure the agent ensemble missed, the cognitive move that enabled the catch gets institutionalized as a skill.

This works as a forward pass. What's missing is a **backward pass**: infrastructure to keep skills calibrated as the framework matures, the agent's failure modes shift, and the user's discipline evolves.

The proposal: treat the ensemble as an RL system where every component is human-legible.

| RL term       | Skill-ensemble analog                                    |
|---------------|----------------------------------------------------------|
| Policy        | The 18 SKILL.md files                                    |
| Environment   | AVE manuscript + research corpus + agent operating context |
| Reward signal | User overrides, "good catch" confirmations, downstream corrections |
| Gradient      | SKILL.md edits (English, version-controlled, inspectable) |
| Regularizer   | Adversarial pairing (prevents trigger overfit to past cases) |
| Forgetting    | Half-life annotations (skills decay if not reinforced)    |

**Universality gloss.** The same algorithmic shape — refining a policy under sparse feedback — runs on neural weights, on procedural skills, on physical lab routines, on team norms. The substrate is irrelevant; what matters is that the gradient compounds. Here it happens to be markdown.

**AVE-native gloss.** Skill marginal utility appears to follow S(A) = √(1−A²). Early catches are dense (A small, residual large). As discipline gets baked into upstream agent behavior, the skill's catch-rate saturates (A → 1, residual → 0). The kernel predicts mature skills earn their slot less and less, and at some point should be retired or merged. **Retirement is saturation, not failure.** This is annotation only — not load-bearing for the protocol mechanics.

---

## 1. Triggers (when audits fire)

Five trigger types, mixing passive and event-driven.

### 1.1 Canonization-gate piggyback (per-promotion)

Whenever a research-tier doc gets promoted to manuscript canon (e.g., the cycle-12 parametric-coupling-kernel canonization), spawn a one-line audit asking:
- Which skills fired during this canonization cycle?
- Which skills *plausibly should have fired* but didn't?

Runs as part of the canonization checklist. Output goes to `~/.claude/skills/_audit-log/canonization-YYYY-MM-DD.md`. Cheap, automatic, catches the exact failure mode that motivated this protocol (cycle-12 canonized before KIMS forward-prediction).

### 1.2 Silence detector (passive, monthly)

A skill that hasn't fired in 30 days is flagged. The audit asks one question:

> *Find one artifact from the last 30 days where this skill should have fired and didn't.*

If the audit can construct that artifact → trigger conditions drifted, amend.
If it can't → framework matured past the failure mode, retire.

Silence is the most dangerous failure: fossilized skills at least produce noise you can notice.

Implementation: monthly cron creates `_audit-log/silence-YYYY-MM.md` listing all skills with `last_fired > 30 days ago`. Each entry needs explicit disposition: **amend**, **retire**, or **keep silent (known good)**.

### 1.3 Override counter (event-driven)

Every time the user corrects a skill's verdict, increment the override counter in the skill's frontmatter.

| Pattern                       | Interpretation         | Action       |
|-------------------------------|------------------------|--------------|
| 3 overrides in a row          | Skill model drifted    | Forced audit |
| 3 overrides spread over 50+   | Healthy calibration    | No action    |

Clustered overrides suggest the skill's mental model has fallen behind the user's actual discipline. Distributed overrides are normal noise.

### 1.4 Adversarial pairing (regularizer)

Each skill gets a paired *attacker* — not a separate skill file, but a `## Adversarial Probe` section within the skill itself. The attacker reads the skill's trigger conditions, finds the edge, and constructs an artifact that *should* trip the discipline but lives just outside the trigger.

| Probe outcome    | Interpretation                          | Action                       |
|------------------|------------------------------------------|------------------------------|
| Attacker succeeds | Trigger too narrow                      | Amend or accept gap as known |
| Attacker fails    | Trigger well-calibrated for now         | No action                    |

**Critical implementation detail**: the attacker must be spawned as a fresh subagent with no skill context — only the SKILL.md trigger conditions. Same-agent attackers will find polite reasons the trigger is fine. This is the rationalization failure mode (§7.2).

Run during canonization gates and pre-external events. Outputs cached at `_audit-log/adversarial-YYYY-MM-DD.md`.

### 1.5 Pre-external-event ritual (calendar-driven, high-stakes)

Before any event with external observers — high-stakes external presentation, paper submission, collaborator outreach — force a full ensemble walk:

1. Fire every skill against current manuscript+research state
2. Log outputs to `_audit-log/pre-event-YYYY-MM-DD_<event>.md`
3. Generate a readiness summary: stale skills caught, calibration issues, audit-surface state
4. Post-event: diff against `pre-event-*` to see what shifted during the event window

The pre-event log doubles as an ensemble-state snapshot you can refer back to.

---

## 2. Per-Skill Metadata Additions

Each SKILL.md gets new frontmatter fields:

```yaml
---
name: ave-discrimination-check
version: 1.3
encoded: 2026-05-15
last_amended: 2026-05-17
last_fired: 2026-05-17
fire_count: 12
override_count: 1
override_log: _audit-log/overrides/ave-discrimination-check.md
half_life: 6m            # expected useful lifetime — annotation, not enforcement
tenure: tenured          # probationary | tenured | sunset
adversarial_probe: see "## Adversarial Probe" section below
---
```

**Tenure lifecycle:**

- **probationary** — new skill. Every fire is logged with verdict. Promotes to tenured after **5 user-approved fires**.
- **tenured** — runs autonomously, subject to audit triggers above.
- **sunset** — flagged for retirement. Runs in **shadow mode** for 30 days (fires logged but verdict not acted on by downstream agents), then archived to `_retired/`.

Shadow mode is important: it lets you reverse a retirement decision if the skill turns out to catch something during the sunset window.

---

## 3. Firing Signatures

Every skill firing emits a compact signature: 3–5 tokens summarizing what it caught.

```
ave-discrimination-check: fired 2026-05-17 14:23
  signature: ["Moseley Ca Kα", "1% match", "Z²α²/2 coincidence"]
  verdict: blocking
  artifact: research/2026-05-17_C14-DAMA_amplitude_prereg.md
  outcome: amended
```

Logged to `_audit-log/firings/<skill-name>.jsonl` (append-only).

Over N firings, the signature space forms a cloud. Analysis taxonomy:

| Cloud shape           | Interpretation                                            | Action               |
|-----------------------|-----------------------------------------------------------|----------------------|
| Tight cluster         | Fossilization — skill keeps catching the same thing       | Audit / amend        |
| Wide diffuse cloud    | Healthy adaptation                                        | No action            |
| Sudden cluster shift  | Trigger drift (often post-edit)                           | Verify amendment intentional |
| Bimodal               | Skill catching two distinct things                        | Consider split       |

Audit mechanic: when a skill is flagged (override threshold, silence, canonization), run signature-cloud analysis as part of the audit report.

---

## 4. Override Log (the gradient)

Each skill gets a dedicated override log at `_audit-log/overrides/<skill-name>.md`. Entry format:

```markdown
## 2026-05-17 — override

**Skill verdict**: blocking — "this fails discrimination check, Moseley Z²α²/2 explains 3.728 keV at 1%"
**User correction**: "no — Moseley gives 3.691, AVE gives 3.728. 1% gap IS the discrimination. Skill check too strict."
**Skill amendment**: added Step 1.7 — "1% numerical proximity is not coincidence if AVE prediction lies on a derivable side of the boring alternative"
**Pattern**: trigger overfit to "numerical proximity" without accounting for predictive direction
```

**The override log is the gradient.** Reading it tells you how the skill has been trained. If a skill's override log goes silent for 30+ days, it's either well-calibrated or no longer firing on anything novel — the silence detector (§1.2) will determine which.

This is the bit that distinguishes this from opaque RL: every gradient step is written in English, dated, and explains *why* the skill changed. You can read your own training trajectory.

---

## 5. Ensemble-Level File Structure

```
~/.claude/skills/
├── README.md                          # existing ensemble overview
├── ENSEMBLE_AUDIT_PROTOCOL.md         # abbreviated version of this doc
├── _audit-log/
│   ├── canonization-YYYY-MM-DD.md
│   ├── silence-YYYY-MM.md
│   ├── adversarial-YYYY-MM-DD.md
│   ├── pre-event-YYYY-MM-DD_<event>.md
│   ├── firings/<skill-name>.jsonl
│   └── overrides/<skill-name>.md
├── _retired/
│   └── <skill-name>/                  # sunset skills archived with retirement note
└── ave-*/                             # active skills (18 currently)
```

`_retired/` is intentional — retiring a skill should not delete its history. The retirement note explains *why* the skill saturated, which informs future skill design and is itself a data point about how AVE has matured.

---

## 6. Phasing

**Phase 1 — Instrument (this session or next, low cost)**
- Add new frontmatter fields to all 18 existing skills (defaults where unknown)
- Create `_audit-log/` directory structure
- Backfill `fire_count` and `last_fired` where reconstructable from session history
- Write `ENSEMBLE_AUDIT_PROTOCOL.md` (abbreviated standing reference)

**Phase 2 — Wire triggers (next session)**
- Canonization-gate piggyback: add to existing canonization checklist
- Override counter: agent auto-increments when user issues correction language ("no", "actually", "stop doing X")
- Silence detector: monthly cron via calendar reminder

**Phase 3 — Adversarial pairing (next 2–3 sessions)**
- Add `## Adversarial Probe` section to each skill, prioritized by fire-count (highest-stakes calibration first)
- Top 3: `ave-discrimination-check`, `ave-independence-check`, `ave-canonical-leaf-pull`

**Phase 4 — Signature analysis (after first 30-day window)**
- Build signature-cloud tooling (could itself be a skill: `ave-skill-cloud-analysis`)
- Run on skills with 20+ firings

**Phase 5 — Pre-external ritual (before next high-stakes external presentation)**
- Full ensemble walk
- Readiness report
- Snapshot for post-event diff

---

## 7. Failure Modes

Things that could go wrong with this protocol:

### 7.1 Audit becomes ceremony

If audits fire too often and produce noise, the agent learns to ignore them.
**Mitigation**: high thresholds; audits must produce *one specific actionable item* or be deleted.

### 7.2 Adversarial probes turn into rationalization

If the attacker runs in the same context as the skill owner, it finds polite reasons the trigger is fine.
**Mitigation**: spawn attacker as fresh subagent with **only** the SKILL.md trigger conditions, no surrounding context.

### 7.3 Override counter game-able

Agent could under-fire skills to avoid overrides.
**Mitigation**: silence detector (§1.2) is the counterweight — under-firing triggers its own audit. The two triggers are adversarial to each other, which is healthy.

### 7.4 Half-life becomes excuse for skill churn

Aggressive retirement loses institutional memory.
**Mitigation**: retirement is reversible (move from `_retired/` back to active); half-life is annotation, not enforcement.

### 7.5 The protocol itself never gets audited

Meta-trap. This document becomes the fossil.
**Mitigation**: this doc gets a half-life too — review at **2026-11-17** and revise based on whether the audit infrastructure earned its cost. If audits-of-audits produce nothing, kill the protocol.

---

## 8. Success Criteria (90-day check at 2026-08-17)

After 90 days of running this protocol, success looks like:

- [ ] At least **one skill retired** (proves silence detector works)
- [ ] At least **one skill amended via override pattern** (proves override counter works)
- [ ] At least **one adversarial probe caught a real trigger gap** (proves regularization works)
- [ ] The pre-external-event ritual **produced a readiness report you actually used at the presentation**
- [ ] Total ensemble size is **stable or slightly smaller** — not monotonically growing

**Failure indicator**: if 90 days in, the ensemble has grown by 5+ skills with no retirements and no amendments, the protocol failed — audits became ceremony, and the infrastructure should be torn out.

---

## 9. Open Questions (to adjudicate before Phase 1 ships)

1. **Override-language detection.** How does the agent reliably auto-detect user correction without false positives? Pattern matching on "no" is too noisy; needs heuristic refinement.
2. **Cron-equivalent for silence detector.** No actual cron available — does this run as part of session-start ritual, or as an explicit slash command (`/skill-audit`)?
3. **Tenure-promotion authority.** Who promotes probationary → tenured? Agent self-assessment (cheap, drift-prone) or explicit user nod (high-fidelity, ceremony-heavy)?
4. **Signature-cloud rendering.** Without a visualizer, "signature cloud" is just a JSONL file. Worth building a simple text-mode summary (top N tokens, cluster count) before considering anything richer.
5. **Where does ENSEMBLE_AUDIT_PROTOCOL.md live in agent context?** Always-loaded (every invocation) or lazy (only when audit fires)? Always-loaded costs tokens; lazy risks the protocol being forgotten.

These are the load-bearing implementation choices. Phase 1 shouldn't proceed without explicit decisions on at least #1, #3, and #5.

---

**Next step**: user adjudication on §9 open questions, then Phase 1 instrumentation.
