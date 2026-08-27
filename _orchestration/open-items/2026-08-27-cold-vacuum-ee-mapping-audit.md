---
id: cold-vacuum-ee-mapping-audit
title: "AUDIT REQUIRED — the cold-vacuum phase-space/real-space EE mapping walk (headline item already REFUTED)"
status: OPEN
owner: lane
opened: 2026-08-27
source: research/2026-08-27_cold-vacuum-phase-real-space-ee-mapping_walk_RECORD.md
anchor: "the checked item is REFUTED"
---

**A walk, recorded 2026-08-27, WALK-GRADE and UNAUDITED.** Provenance — Grant,
verbatim: *"what is the ee circuit mapping between phase space and real space
with a 'cold' vacuum? isolated ground/ref?"*

**THIS ITEM SUPERSEDES NOTHING.** The record mints no claim id, moves no
solidity, propagates to no leaf, and edits no canon. **Only Grant rules on any
of it** — including the three flagged canon collisions, which are surfaced
under flag-don't-fix and were deliberately left unrepaired.

## The headline is a negative, and it is already banked

**Walk item 7 — that the common-mode open explains why `M` is continuous while
`Q` and `J` are integers — is REFUTED.** Three check lanes returned REFUTES on
independent grounds and the record carries the kill up front (§0), not in a
caveat section. **Do not spend audit budget re-litigating item 7.** Kill
condition K6 states the bar for anyone who wants to try: a repair must defeat
four independent kills plus a regime problem.

## What is actually open

The walk stands or falls on **items 1–6**, which the three lanes did not test.
The record grades them independently:

- **Items 2 and 3** (the common mode is an open with zero port current; the
  differential sector is a virtual neutral at exactly 0 V; the reference
  structure is asymmetric) — **MEASURED-SUPPORTED**, and stronger than the walk
  claimed.
- **Item 4** (the gauge freedom is a property of the circuit, not a convention)
  — **MEASURED-SUPPORTED IN THE COLD LIMIT AND SHARPENED**: the global
  common-mode offset is an exact symmetry of the shipped cold dynamics
  (residual ~1e-17), and it **breaks structurally under saturation, tracking
  (1-S) across seven decades**. This is the record's only new content and the
  primary audit target.
- **Items 1 and 6** — split: the measured content survives, the `T2` label
  (z=4-only) and the bundle noun (NOT-RATIFIED) do not.
- **Item 5** (phase-only epistemology as a circuit fact) — the (1-S) result puts
  a crack in it: it may be a cold-limit statement rather than a structural one.
  **Untested, and the most interesting thing the record raises.**

## Three canon collisions, flagged not fixed — Grant rules

1. **The `T2` name is canon at z=4 ONLY** (`k4-port-irrep-decomposition.md`,
   310 lines, three methods, 0 hits for srs/trivalent/degree-3/z=3), while the
   **ratified production carrier is z=3 srs** (`unified-engine-design-doctrine.md:222`,
   Grant 2026-06-25). At z=3 the balanced eigenspace is 2-dimensional, so
   *"triply degenerate"* and *"traceless 3D subspace"* have no referent there.
   The code says the gap in its own words: `chiral_lattice.py:79`,
   *"(canon: n=4 only)"*. **Open: does the z=3 irrep naming gap get closed?**
2. **Clause Q's reference is on `eps_11` in the bound/bias sector**, a different
   object from the port-amplitude symmetry the record measured. If they ARE the
   same object the record is under-claiming a derivation route for a POSTULATED
   clause; if they are NOT, the walk's item 4 cross-wires them.
3. **A cold vacuum has no Gamma=-1 surface**, but canon defines all three
   boundary observables at one (`boundary-observables-m-q-j.md:11`). This is the
   regime error under the item-7 refutation and it constrains any repair.

## How to run the audit

**The charter is §8 of the record — eight numbered claims (A1–A8) with
per-item attack instructions**; the pre-stated kill conditions are §9 (K1–K6,
two of which would IMPROVE the walk if they fire). Priorities:

- **A1 is the highest-value lane** — read-AND-run the committed driver
  `research/drivers/cold_vacuum_ee_mapping_walk.py`, then attack the SETUP for
  self-referentiality (periodic box? seed? scalar container?), not the
  arithmetic. K1 is the primary kill.
- **A3 adversarially** — a broken symmetry is not automatically an observable.
  If no readout couples to the common mode at (1-S)>0, item 5 survives intact
  and the record's §4.4 is a distinction without a difference.
- **A7 adversarially against the record itself** — the record may be applying
  the #417/#415 decoupling fence more widely than it reaches. A fence applied
  too broadly is as much a defect as one dropped.
- **A4 must use a markup-stripping matcher.** The record documents a live grep
  false-negative: `**not** a subspace of the phasor` is invisible to both a
  literal grep AND a whitespace-only normaliser, because markdown emphasis sits
  inside the phrase. Any "0 hits" re-check that skips this will repeat the error.

Plus the standing requirements: consensus-bias symmetric standard in **both**
directions, a discrimination check (expected honest answer: one measured
scaling, zero forward predictions), and **two-attempt cap then STUCK-POINT**.
The three likely stuck-points (C2, C4, A7) are Grant-intuition questions, not
compute questions — route them to Grant rather than spiralling.
