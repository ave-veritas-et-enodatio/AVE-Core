# Handoff brief — R55 polish tail + collision executions (satellite lane)

**Date:** 2026-08-24 · **Lane:** register/hygiene satellite (deliberately OFF
the core session's critical path — this is the polish tail, triaged per the
truth-per-token discipline) · **Author:** core orchestrator · **Grant launches
and picks model + effort; a cheaper model is appropriate for this lane.**

---

## Part A — un-gated, start immediately

**A1. R55 Phase-2 scripted wording sweep.** The spec IS the open item — execute
it, do not re-derive it:
[`open-items/2026-08-24-r55-phase2-wording-sweep.md`](open-items/2026-08-24-r55-phase2-wording-sweep.md)
— binding rewrite rule (quoted there verbatim from R55 §4), the ~140-file
surface, the **HOMONYM-EXCLUDED class** (three `src/` files where `Axiom 5`
names an unrelated coupled-resonator operator — rewriting those mislabels an
operator; propose their rename as a separately-reviewable sub-task in the same
PR), and the two pre-existing drift rows (`eq:bcsrc_*` labels in
`axiom-register.md`; `CLAUDE.md:389` confirmed-by line). Script-first: the
script classifies every site (grade-bearing / pure reference / verbatim quote /
frozen), emits a reviewable per-class diff, and re-runs the measurement to a
zero-grade-bearing-residual receipt. Frozen trails (`research/`,
`docket-entries/`) are NEVER rewritten (Rule 12); ratified text quoted verbatim
is NEVER edited.

**A2. R52-compliant re-expression of the flat-direction receipt.** The spec is
[`open-items/2026-08-24-r52-panel-k-receipt.md`](open-items/2026-08-24-r52-panel-k-receipt.md):
task 1 (re-express "lattice K=0" in bond-spring / port-amplitude terms and
re-run the receipt) is lane-grade; task 2 (pilot/engine K-receipt collision
check) **escalates to Grant on any real contradiction — both receipts
verbatim, then STOP.**

## Part B — GATED on Grant rulings (check the docket before starting each)

Each item below fires only when its ruling docket entry exists on main. The
items carry their own candidate dispositions — **execute the ruled option,
nothing else**; quote the ruling verbatim in your PR.

| gated task | open item (the spec) |
|---|---|
| `A_0` glyph fix + consumer sweep | [`open-items/2026-08-24-a0-glyph-collision.md`](open-items/2026-08-24-a0-glyph-collision.md) |
| `B(M)` glyph (rename or vocab-block bind) | [`open-items/2026-08-24-axiom5-b-glyph.md`](open-items/2026-08-24-axiom5-b-glyph.md) |
| kernel-argument normalization pass | [`open-items/2026-08-24-kernel-argument-normalization.md`](open-items/2026-08-24-kernel-argument-normalization.md) |
| γ_c / G_c re-scope propagation | [`open-items/2026-08-24-gammac-gc-modulus-identity.md`](open-items/2026-08-24-gammac-gc-modulus-identity.md) |
| collision-register home (mint def-nodes) | [`open-items/2026-08-24-collision-register-home.md`](open-items/2026-08-24-collision-register-home.md) — if ruled def-nodes: mint PROPOSED-status entries under `ave-vocab-discipline`, §6 pointer rows, no new tooling |

## Binding disciplines

- **Skill plan (declared per the pre-workstream discipline):** `ave-sweep-audit`
  (A1 is a class-N>10 mechanical sweep — batch by class, correctness first,
  per-batch commits), `ave-walk-back` Type-E grep rigor for any propagation
  pass, `verify-before-cite` on every receipt, `ave-vocab-discipline` for Part
  B minting. Read-don't-grep for any completeness claim; cross-check every
  "0 residual / all sites" claim with a second method (the `**`-glob
  false-negative lesson).
- Worktree self-isolation; branch asserted before edits; board regenerated
  before every commit touching open-items; PR opens
  `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`; only Grant merges.
- Stop-and-ask: 2-attempt cap, STUCK-POINT report. A sweep site that does not
  fit the item's context classes is a stuck-point, not a judgment call.
- Pure-AVE-corpus rule on every tracked byte.

## Out of scope

Any physics adjudication (Part B executes rulings, it does not interpret
them); the solver cross-check lane (separate brief); frozen-doc rewrites;
canonical solidity moves.
