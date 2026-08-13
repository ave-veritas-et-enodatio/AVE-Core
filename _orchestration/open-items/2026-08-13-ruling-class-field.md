---
id: ruling-class-field
title: Docket rulings need a physics-vs-process class field — the coverage number can't distinguish them
status: OPEN
owner: unassigned
opened: 2026-08-13
source: _orchestration/docket-entries/2026-08-06-rulings-final-batch.md
anchor: "## R12 — records-class merge convention: SPLIT BY CONTENT"
---

The board's ruling-token coverage line counts every docketed `R<N>` against the claims register.
That conflates two populations with opposite meanings:

- **A physics ruling absent from the register** means claims may still carry scores earned under
  a superseded reading. That is real debt.
- **A process ruling absent from it** means nothing. `R12` (records-class merge convention),
  `R25` (frozen-note surface-notes: GO), `R33` (classify_sign: CENSUS-SCRIPT FIX), `R47` (the
  tracking-integration spec: GO) will never appear in a claims register and should not.

Two entries in the set **self-declare they are not rulings at all**: `R8 — the phase-inventory
walk (continuation; leans and routings, NOT rulings)` and `R19 — the pitch walk: Grant LEAN
recorded (NOT a ruling)`.

**Second, independent defect on the same line — the `R<N>` glyph is overloaded.** The scan cannot
distinguish ruling `R4` from `Route R4`, `Registry §5 R2`, a review repair-ID `R1`, or a varactor
operating point. At least five live namespaces share it in the scanned text, and every collision
reads as *propagated* — so the count under-reports. R1–R4 are confirmed false clears.

**What would close this.** A `class:` field on docket ruling records (`physics` / `process` /
`lean`), so the board can count the population the sentence is about. Same shape as
`key-namespace-collision` (four things named `D1`) and `ruling-selection-rule` (two competing
number conventions) — all three are registry problems, not document-discipline problems, and one
field would likely close two of them.
