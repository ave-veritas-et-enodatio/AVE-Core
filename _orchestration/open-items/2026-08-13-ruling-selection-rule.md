---
id: ruling-selection-rule
title: What counts as a "ruling" for propagation-debt purposes? — the selection rule is undefined
status: OPEN
owner: grant
opened: 2026-08-13
source: _orchestration/docket-entries/README.md
anchor: "Docket entry fragments (the news-fragments convention, adopted 2026-07-21)"
---

Surfaced by the 2026-08-13 audit of the board generator, which asked the question directly
and correctly refused to answer it.

**The problem.** The board reports how many rulings have not reached the claims register. That
requires knowing which rulings exist — and the corpus supports two different derivations:

| derivation | count | what it misses / adds |
|---|---|---|
| docket **filenames** (`-ruling-rNN-`, ranges expanded) | precise, convention-backed | misses rulings recorded in batch files that name no numbers, e.g. `2026-08-06-rulings-final-batch.md` |
| docket **bodies** (any `\bR\d+\b`) | larger | cannot distinguish a ruling *recorded* here from a *cross-reference* to one recorded elsewhere |

From the text alone the two are not separable. The board currently reports the filename set and
discloses the body-only remainder separately rather than folding it in either direction.

**What would close this.** Either (a) a naming convention that every ruling record satisfies
(then filenames are authoritative), or (b) a status field inside each docket entry naming the
rulings it *records* as opposed to *cites* — the same shape as the docket-key uniqueness that
`verify-docket-keys.py` already enforces.

**Related:** `key-namespace-collision` — the same class of failure one level up (four distinct
decisions all named "D1"). Both are registry problems, not document-discipline problems.
