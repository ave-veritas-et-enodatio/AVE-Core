---
id: board-check-date-blanking
title: '`--check` blanks every date in the stable region — 1 legitimate target, 57 lines of collateral'
status: OPEN
owner: unassigned
opened: 2026-08-14
source: _orchestration/tools/generate_board.py
anchor: "the scanned-tree SHA **and its date** are SELF-REFERENTIAL"
---

`generate_board.py --check` normalizes dates out of the stable compare with a blanket
`re.sub(r"\b20\d\d-\d\d-\d\d\b", "<date>", stable)`. The normalization is **correct in intent** —
the header's scanned-tree date is self-referential, since a board committed in commit X can only
name X's parent, and that made `--check` red on arrival once already when two commits straddled
midnight.

The problem is reach, not intent.

**Measured 2026-08-14** on the board at that date, by reproducing `split()`'s stable region exactly:

| | count |
|---|---|
| dates blanked in the stable region | **116** (21 unique) |
| lines affected | **58** |
| lines that are the legitimate self-referential target | **1** (`Scanned tree …`) |
| **collateral — lines whose dates are program state** | **57** |

So the guard is blind to a date change on 57 lines to protect 1.

**What that actually costs.** The open-item table renders one row per item with a link into
`open-items/<YYYY-MM-DD>-<slug>.md`. Those hrefs carry dates, so they are blanked. A hand edit that
retargets a row's link from one date-named file to another is invisible to `--check`. Same for the
`opened:`/open-since dates the table prints, and for dated references in the scope note. Every one
of those is derived program state — a change in them is exactly what the guard exists to catch.

**Not urgent, and low blast radius in practice.** The board is regenerated, hand edits are
overwritten on the next run, and `--check` is a LOCAL guard (it is in no Makefile target, no CI job,
and no git hook — verified 2026-08-13). Nothing is currently wrong. But the guard's stated purpose
is catching hand edits, and on this class it demonstrably does not.

**Provenance.** Mine, shipped with the original `--check` in #965. Found independently **twice** —
once by the #967 blind audit (recorded as a lower-severity finding, never tracked) and again by the
2026-08-14 re-review of #968, which correctly classed it as inherited rather than new. Two
independent finds and no tracker is the same shape as
[[2026-08-14-seventh-calibration-role]]; opening it so the third finder does not spend the same
effort.

**Candidate closures, un-endorsed:**

1. **Anchor the substitution to the header line only** — normalize the date only where it follows
   `Scanned tree **<sha>** (`. Smallest change; leaves every other date guarded.
2. **Move the scanned-tree line inside the volatile bounds** and drop the date normalization
   entirely. Cleaner conceptually — the whole line is derived-from-git — but it also stops guarding
   the index-record and claim counts that share it, which are real program state. Would need those
   two moved out first.
3. **Leave it and narrow the docstring's claim** so the guard stops advertising coverage it does not
   have. Cheapest, and honest, but it keeps a fail-open in a file whose own contract is fail-loud.

Note (1) and (2) are not equivalent: (2) also removes the PR-count normalization added in #968 by
making it unnecessary, which is tidier, but it is the larger change.
