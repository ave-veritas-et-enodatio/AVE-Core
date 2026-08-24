# Handoff brief — External-Solver Cross-Check, Phase 1 (implementer satellite)

**Date:** 2026-08-24 · **Lane:** testing-infra spine (the program's declared
north star: testing pivot, infra-first) · **Author:** core orchestrator ·
**Grant launches this session himself and picks model + effort.**

---

## ⛔ LAUNCH GATE — read before anything else

Phase 1 fires **only** on Grant's ratification of the Phase-0 trade decisions
(**T2 is the GO gate** — epic §4 Phase-0 GATE, quoted verbatim in the trade
study: *"Grant ratifies the trade-study decisions marked his"*).

**Gate check:** a docket entry dated 2026-08-24 ratifying the SCX trades
(T1–T6, T2 explicitly) must exist under `_orchestration/docket-entries/` on
main. Quote its decisions **verbatim** into your prereg. **If it does not
exist, STOP — the gate has not fired. Do not proceed on this brief's summary
of any expected ruling.**

## What this lane executes (pointers, not restatements)

| doc | role |
|---|---|
| [`_orchestration/2026-08-23_external-solver-crosscheck-epic.md`](2026-08-23_external-solver-crosscheck-epic.md) | the epic; §4 = phase plan, §5 = design fences |
| [`research/2026-08-24_solver-crosscheck-phase0_requirements.md`](../research/2026-08-24_solver-crosscheck-phase0_requirements.md) | DERIVED requirements (REQ-IDs are single-source-of-truth) |
| [`research/2026-08-24_solver-crosscheck-phase0_tradestudy.md`](../research/2026-08-24_solver-crosscheck-phase0_tradestudy.md) | the decision space T1–T6; consume the RATIFIED selections only |
| [`research/2026-08-24_solver-crosscheck-phase1-prereg-skeleton.md`](../research/2026-08-24_solver-crosscheck-phase1-prereg-skeleton.md) | prereg skeleton; values marked `FROZEN-AT-PHASE-1-GO` freeze in YOUR prereg |

Deliverables: the exporter (engine adjacency → netlist per the ratified T2/T6
selections), the `.AC` extraction per T4, the frozen Phase-1 prereg (fill the
skeleton, freeze the values, then run — never the reverse), the result doc,
one reviewed PR.

## Binding disciplines (each is load-bearing; none is boilerplate)

1. **Sector declaration re-declared in every doc you write** (epic §7): MODE
   numerical-infrastructure / Regime I lossless-reactive / cold quiescent /
   scalar-translational only / carrier srs-z3. The requirements §0 table is
   the template.
2. **Framing is IMPLEMENTATION-VERIFICATION** (a sub-class of consistency).
   Two integrators agreeing validates that the engine solves its own
   equations. No result from this lane may be framed as emergence, chord, or
   falsification — the epic's §1 register, non-negotiable.
3. **FL-1 symbol hazard (requirements §8.2):** two live engine symbols encode
   two different bond delays — `bond_lc()` (`src/ave/core/chiral_lattice.py`,
   R1 convention) vs `ANALYTIC_NETWORK_FACTOR`
   (`src/ave/core/chiral_lattice_dynamics.py`, R2). `SCX-REQ-LABEL` pins the
   exporter's convention; **your exporter must carry an explicit test that its
   emitted delay matches the pinned convention**, so the wrong-symbol reach is
   machine-caught, not vigilance-caught. If the ratification docket entry
   rules anything about these symbols' naming, execute that too.
4. **Reproduction gate first** (requirements §7): before exporting anything,
   re-run the in-tree band-structure reproduction and match the frozen
   receipts. A cross-check lane that cannot reproduce the engine's own answer
   has nothing to cross-check.
5. **Stop-and-ask protocol:** 2-attempt cap on any stuck-point, then a
   STUCK-POINT report to Grant (what was tried, receipts, the question).
   Physics surprises are stuck-points, not judgment calls — this lane owns
   zero physics decisions.
6. **Worktree self-isolation** (`git worktree` off origin/main; assert branch
   before every edit batch). **PR protocol:** open
   `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`; only Grant merges.
   **Pure-AVE-corpus rule applies to every tracked byte.**
7. **Skill-selection plan (declared here per the pre-workstream discipline):**
   `ave-prereg` (before the prereg freeze), `substrate-native-check`
   (re-run the CP walk at implementation time — requirements §0.5 is Phase-0's
   walk, not yours), `ave-driver-script-honesty` (exporter + drivers),
   `phase-space-coordinate-check` (the arccos-map comparison is a phasor-space
   claim), `verify-before-cite` (every receipt), incremental-write for large
   docs. Retro-pass before commit if the applied set drifts.

## What is OUT of scope

The vector/Cosserat channel (fenced, §6.3); any second solver (Xyce is the
§5.3(b) arm, not now); transient ringdown unless T4's ratification says
otherwise; any canonical mint (`clm-`/`def-`/`exp-`); any statement about
whether the axioms describe the vacuum.
