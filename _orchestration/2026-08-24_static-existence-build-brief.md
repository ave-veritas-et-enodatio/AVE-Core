# Build brief — the static-existence arc's execution lane (P1 → HB solver → G2 → P2)

**Date:** 2026-08-24 · **Consumes:** the epic
([`2026-08-24_static-existence-epic.md`](2026-08-24_static-existence-epic.md)),
the G1 walk record
([`research/2026-08-24_g1-ac-steady-state-walk_RECORD.md`](../research/2026-08-24_g1-ac-steady-state-walk_RECORD.md)),
the P0 capability report + walk packet (same directory) · **Grant launches the
build sessions and picks model + effort; the core orchestrator runs the gates
and verifies.** Arc-serial: this is THE core physics lane; nothing else
substantive runs beside it in a build session.

## ⛔ Launch gate

The epic PR must be MERGED to main (the guards, records, and this brief are
the spec; a build against an unmerged spec is a build against chat memory).

## Stage 1 — P1: the transverse graded scatter + response map

**What:** the T2 analog of the Class-C measurement. Build the transverse
per-directed-bond graded scatter (the named extension — no T2 grading hook
exists in-tree; `vacuum_varactor_scatter`'s per-bond form + cancellation gate
is the template to generalize), port the pulse/probe pipeline, and measure the
transverse Γ(A) locus.

**The branch fork is resolved BY MEASUREMENT, not declaration:** canon holds
both magnetic-first (μ_eff = μ₀S → Z→0, Γ→−1) and electric-first (ε_eff→0,
μ cold → Z→∞, Γ→+1) with opposite boundary phase (the P0 correction, epic §3).
Run BOTH loadings as separate declared configurations; the prereg freezes each
config's expectations separately. The transverse vertex behavior (the −1/3
counting fact is scalar-scoped) is measured for free in the cold gate.

**Discipline set (declared per the pre-workstream rule):**
`substrate-native-check` — with the transverse analog of the per-node
cancellation trap identified BEFORE coding (epic guard 4; P0 receipt:
per-node-uniform grading is invisible at scatter AND at connect);
`phase-space-coordinate-check` (the Γ extraction's coordinate map declared);
`ave-prereg` (frozen, firewalled author — the full Class-C chain is the
template, including the standalone sentinel checker and the raw-series
landing); `ave-driver-script-honesty`; figure house style; R40-B2a stamps
carried on any machinery reuse. Deliverable: prereg + result pair + driver
via reviewed PR, adversarially verified (≥3 lenses) before CLEARED.

## Stage 2 — the harmonic-balance solver

**What:** phasor-domain KCL fixed-point solver on the graded srs network with
varactor tone-mixing: unknowns = the phasors at the posited tone set + the
S-field; equations = graded Kirchhoff per tone including the kernel's
inter-tone coupling; solve the algebraic fixed point. No time axis. No
damping. Ax3 untouched by construction.

**Validation gates (means-test class A′, built before any P2 use):**
1. Cold linear limit → recover the arccos band structure (the frozen 1/√3
   velocity factor + band edge).
2. Single-tone graded limit → **reproduce the MEASURED Class-C response map**
   (`research/2026-08-24_engine-gamma-meanstest_result.md` — the measured
   Γ(A) locus is the validation target; the solver must draw the lattice's
   own curve before it is trusted to find modes).
3. Source-idle machinery: verified on a known driven-vs-autonomous pair
   (a driven cold tank never goes source-idle; an initialized lossless ring
   trivially does).

**Discipline:** `consistency-vs-emergence` (the solver is instrument-grade
infrastructure; its validation is implementation-verification);
`ave-module-library-discipline`; the reconcile-don't-declare rule on every
gate (each validation gate COMPUTES its pass, never asserts it).

## Stage 3 — G2: the frozen P2 prereg

Grant confirms the two PROPOSED choices (scaffold form: source-terminated
solve + injection-lock cross-check; observable set: S-railing + projected
M/Q on two imposition representatives). Then the prereg freezes: all eight
epic guards discharged in writing by name; the config-grep vs the closed
negatives (formation-dynamics configs — the phasor-domain solve is
config-disjoint by construction, and the grep proves it rather than waives
it); the ppt consistency ceiling as a frozen criterion; DISPROVE pre-frozen
(no source-idle solution with a railed core); the α-agnostic tone-set
statement (guard 8 — harmonic balance posits tones, not tube phases; the
prereg says so explicitly). Author firewalled from results.

## Stage 4 — P2: the solve, and P3 behind its gate

Run per the frozen prereg. Adversarial verify (≥3 lenses: config compliance
re-grepped on the actual solver invocation; physics/coordinates incl. the
sector-ownership read on any railed solution; independent numerics rerun).
The repairs-need-reaudit loop runs to convergence. P3 (propagation:
eigenmode-existence item, K=2G residue, clm-satnec re-grade, rim-inversion
notes, manuscript lockstep) fires only after G3 — and lands via its own
reviewed PR per the canonical-propagation discipline.

## Session plan

- **Build sessions (Stages 1–2):** satellite implementers, Grant-launched
  from this brief, worktree-isolated, stop-and-ask embedded (2-attempt cap,
  STUCK-POINT report; a physics surprise is a stuck-point, not a judgment
  call). Stages 1 and 2 may run as two satellites in parallel — they share
  no files (P1 = scatter machinery + measurement; solver = new module) and
  meet only at Stage 2's validation gate 2, which consumes P1's *merged*
  result. Sequential is also fine; parallel only if Grant wants the pace.
- **Gates and verifies (G2, G3, all CLEARED calls):** the core orchestrator
  session.
- **Standing rules travel:** ONLY GRANT MERGES; DO-NOT-MERGE → CLEARED
  protocol; pure-AVE-corpus on every tracked byte; boards regenerated before
  open-item commits; frozen criteria travel verbatim or as file:line.

## What this lane is NOT

Not the SCX Phase-1 satellite (separate brief, separate lane, already
launchable — the testing-infra spine continues in parallel and its ngspice
cross-check is independent Class-B validation for the same machinery family).
Not a formation study, not an emergence test, not a chord hunt — the epic's
§8 carve governs every doc this lane produces.
