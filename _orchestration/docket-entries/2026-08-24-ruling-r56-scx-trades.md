# R56 — SCX trade ratification: T2 = (a) lossless TL element; R2 pinned as TAGGED engineering convention. The Phase-1 GO gate FIRES. (2026-08-24)

### ENTRY 2026-08-24-ruling-r56-scx-trades

**Grant, in chat, 2026-08-24, verbatim:** *"a+r2"*

**Context that makes the two tokens a ruling.** The walk framing was frozen
same-day at
[`2026-08-24-opens-walk-framing.md`](2026-08-24-opens-walk-framing.md) §W1,
which closed: *"One word from you on (a)+R2 fires the Phase-1 gate."*
Grant's *"a+r2"* is that word. Decision space:
[`research/2026-08-24_solver-crosscheck-phase0_tradestudy.md`](../../research/2026-08-24_solver-crosscheck-phase0_tradestudy.md)
(T1–T6, all authored OPEN / SELECT NOTHING).

## The ruling

1. **T2 = option (a): lossless transmission-line element per bond** — one
   SPICE `T` element per srs bond, $(Z_0, \mathrm{TD})$, the $z=3$ vertex as
   an ordinary shunt node (the $\Gamma = -1/3$ mismatch emerges from the
   junction, unmodeled). Option (b) lumped-ladder is retained ONLY as the
   trade study's internal convergence diagnostic; option (c) mutual-K stays
   pre-rejected.
2. **The ω_C label: R2 is PINNED as a TAGGED ENGINEERING CONVENTION for the
   exporter only** — $\mathrm{TD} = \texttt{ANALYTIC\_NETWORK\_FACTOR}/\omega_C$,
   band top $\pi\sqrt3\,\omega_C$. **The corpus's physics-level R1-vs-R2
   adjudication flag (`srs-band-structure.md:157`, "Flagged for adjudication")
   stays OPEN** — this ruling selects the exporter's emitted label and
   mandates the machine check that the emitted delay matches it (the Phase-1
   brief's FL-1 test); it does NOT adjudicate the corpus flag.
3. **T1 (ngspice), T3 (engine adjacency export), T4 (`.AC` driving-point /
   two-port), T6 (native/normalised emission + SI round-trip check): STAND as
   the lane's selections** under the ratify-by-exception protocol the walk
   framing declared — Grant ruled T2 explicitly and raised no exception on
   the lane calls.
4. **NOT ruled here:** the `bond_lc` symbol rename (FL-1's naming half) — the
   brief's machine-checked exporter test covers the hazard; the rename stays
   an open lane proposal.

## Consequence

**The Phase-1 GO gate (epic §4 Phase-0 GATE) FIRES.** The launch path:
[`2026-08-24_solver-crosscheck-phase1-brief.md`](../2026-08-24_solver-crosscheck-phase1-brief.md)
— its gate check requires THIS entry on main; Grant launches the satellite
and picks model + effort. Phase-1 prereg values freeze quoting this entry's
selections verbatim.
