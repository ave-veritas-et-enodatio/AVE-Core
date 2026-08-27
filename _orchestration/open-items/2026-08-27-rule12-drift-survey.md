---
id: rule12-drift-survey
title: "125 Rule-12 drift candidates are shipped with no owner — including one confirmed live violation at claim-quality.md:760"
status: OPEN
owner: unassigned
opened: 2026-08-27
source: research/2026-08-26_rule12-drift-candidates.json
anchor: "each row is the QUESTION 'was this edit inside what that note froze?', addressed to whoever owns the record -- NOT an answer"
---

## What exists, and why it had no home

`research/2026-08-26_rule12-drift-candidates.json` holds **125 rows**. Each row
is a Rule-12 note whose surrounding body **changed by a REPLACE or a DELETE**
between the commit that introduced the note and the tree the survey ran on.
Insertions are excluded — appending a dated banner is the sanctioned move — so
every row is an edit *inside* a body some note said was frozen.

**Before this item, the only thing in the corpus that pointed at that file was
`manuscript/ave-kb/tools/rule12-freeze-config.json`'s `_drift_survey` string.**
A survey of append-only violations, referenced only by the tool that emitted it,
is not routed; it is filed. This item is the queue entry.

## The one that is not a candidate

**`manuscript/ave-kb/common/claim-quality.md:760` is a confirmed live Rule-12
violation, not an open question.** The note at that line is a dated demotion
banner whose own text says *"claim body + prior Quality block preserved below"*.
The survey row records that the body below it was then **edited in place**,
twice, at file lines `780` and `785`:

- `:780` — `- confidence: 0.20` → `- confidence: 0.15`, with the trailing
  provenance comment rewritten from the 2026-07-19 CONTESTED demotion to the
  2026-07-20 RULING-2 one.
- `:785` — `- solidity: 0.20 (do not build on, rework needed) [= min(0.20, 0.30)]`
  → `- solidity: 0.15 (refuted, do not use) [= min(0.15, 0.30)]`.

The banner said the block below was preserved. It was replaced. **That is the
violation the append-only rule exists to prevent**, and it is the reason this
item is OPEN rather than QUEUED.

**It has NOT been repaired, deliberately** (flag-don't-fix): rewriting the body
back would compound the violation by destroying the evidence of it. The correct
close is a *dated appended note* on `claim-quality.md` recording that the
2026-07-19 block was overwritten by the 2026-07-20 ruling, with both values
stated — a decision for whoever owns the claim register, not for the lane that
found it.

## What the other 124 rows are, and what they are not

They are **questions, not verdicts**, and the survey's own `_comment` says so.
The generator derives each frozen range **mechanically** — note to neighbouring
note — and **not from the note's prose**. A note saying *"the line above is
preserved"* does not freeze a paragraph ninety lines up, so a row can be a true
edit inside a mechanically-derived range and still be no violation at all.

Each row therefore asks one question of the record's owner: **was this edit
inside what that note actually froze?** Nothing in the file answers it.

## How to reproduce the survey

The obvious command does **not** work, and that is a property of the tree rather
than a bug: `verify-rule12-freeze.py --backfill --dry-run --drift-report <path>`
run against the current tree emits **zero rows**, because every note now carries
a stamp, so the backfill finds nothing to stamp and therefore nothing to
classify. The survey is a one-shot artifact of the pre-backfill tree. Reproduce
it by running the **current** tool against a worktree of `c6480205` (the commit
before the backfill `f7bd1e94`); the exact commands are in the survey file's own
`_comment`.

## Sizing, stated as a measurement

Counted from the shipped JSON on 2026-08-27: **125 rows**. The version first
shipped on branch `infra/2026-08-26-rule12-append-only-gate` held **124** — it
was missing `manuscript/ave-kb/common/port-register.md:87`, the note whose stamp
was reverted for the R40 content-key collision. That file has been regenerated
to the full 125; the other 124 rows are byte-identical to the version they
replace.

**No claim is made here about rows the survey does not contain.** The generator
sees only notes its detector recognises, and that detector is line-based and
direction-required — it misses notes wrapped across two lines and notes that
name no direction. Both families are counted on every gate run by the tool's
non-gating second arm and listed by `--census`. A drift inside a body whose note
is in either family is not in this survey and was never looked for.

## Blocking relationship

Blocks nothing. The gate is green with all 125 rows outstanding, by design — a
gate that went red on every historical in-place repair from day one would be
switched off within a week. The `claim-quality.md:760` case is the one row with
a named next action.
