# EPIC — External-solver cross-check of engine linear dynamics (SPICE-class)

**Status:** ACTIVE — last-verified 2026-08-23 (owner: orchestration; every phase GO-gated on Grant)

---

## §0 — Origin and mandate

This epic is the second clause of the dt-fusion ruling
([`docket-entries/2026-08-23-dt-fusion-ruling.md`](docket-entries/2026-08-23-dt-fusion-ruling.md)):
the retired partition-orphaned driver was worthless as code, but its content walk surfaced one
concept that survives — **run the substrate's own network through an independent industrial
circuit solver and check that the engine and the solver agree.** The ruling (verbatim): *"C, and
add a full orchestration epic on the planning, validation, and execution of the idea given to us
by this effort"*. This document is that epic. **No implementation is authorized by this document
itself** — each phase carries its own GO gate.

## §1 — The idea, stated substrate-first

**Sector declaration.** MODE: numerical-infrastructure epic (no new physics claims). REGIME:
Regime I, sub-yield lossless-reactive — linear small-signal only, phases 0–2. PHASE-STATE: cold
lattice. **CHANNEL: scalar/translational first** — its band top is closed-form; the
vector/Cosserat channel's top is a live bracket pending the standing
single-scale-vs-stiffness-lifted ruling, so it enters (if at all) only after that ruling
(blind-audit finding 3.7). Phase 3 alone reaches toward the saturation kernel, and is
conditional.

The scalar/translational substrate model IS a circuit: nodes with LC storage, bonds as
transmission-line elements (the Op5 scatter+connect TLM; scalar-channel scope per
`srs-band-structure.md:53-57`), canonical ε₀/μ₀/Z₀/c as the medium constants. The engine's
TLM cores integrate this class of network with in-house numerics — the v9 chiral-srs lattice
(this carrier) and the K4-TLM (same class of network, different connectivity) (the other engine backends are different discretizations, not this network;
blind-audit finding 3.6). An industrial SPICE-class solver (ngspice / Xyce) is a mature,
independently-developed integrator for **exactly this class of network**. Exporting the engine's
own graph — same topology, same canonical element values — and comparing observables gives an
independence receipt our in-house numerics cannot give themselves.

**What agreement would prove (classified before any run, per consistency-vs-emergence):** this
is **implementation-verification, not physics validation**. Two solvers agreeing on the same
network validates that the engine solves its own equations correctly — it says nothing about
whether the axioms describe the vacuum. That is the honest register, and it is exactly the
register the program's testing pivot asks for: infrastructure that hardens the engine's
trustworthiness before its outputs are load-borne.

**What disagreement would prove:** one of {exporter, engine, solver-numerics} is wrong. Any of
the three findings is valuable; the middle one — an engine defect surfaced by an independent
integrator — is the most valuable single outcome this epic can produce, and the reason it
exists.

## §2 — Open goal framing (prove-or-disprove)

> **GOAL (open):** Does an independent industrial circuit solver, fed the substrate's own graph
> with canonical element values, reproduce the engine's certified linear-regime observables
> within pre-registered tolerances?

Both outcomes are wins; neither is assumed. The epic FAILS (and says so) if agreement cannot be
reached AND the divergence cannot be attributed to a specific defect under the §5 adjudication
protocol — an unattributable divergence means the cross-check instrument itself is not sound,
and that verdict would be banked honestly rather than tuned away.

## §3 — What this is NOT

1. **Not a restoration.** The archived exporter's tank values (1 µH/1 pF), coupling law
   (K = 0.5/d), and all-to-all star-to-ground topology are underived and wrong-by-current-canon
   (docket entry §"Evidence walked"). Zero lines are reused.
2. **Not nuclear/element modeling.** The NUCLEON-array picture is retired with its driver. This
   epic exports the VACUUM lattice, not composite matter.
3. **Not a BenchModel replacement.** The bench-model spine remains the channel-agnostic bench
   with machine-checkable gates; this epic is an *independence adjunct* that can feed it, not a
   parallel spine.
4. **Not scale.** SPICE-class solvers handle small networks well and 10⁶-node lattices not at
   all. Scope is deliberately small networks, where independence is cheap and exact.

## §4 — Phase plan (each phase GO-gated; no phase starts on this document alone)

### Phase 0 — Requirements + trade study (planning only, no code)

Per the bench-test documentation pattern: a **Requirements doc (derived)** — which graph
(the ratified z=3 srs carrier cell, per `axiom-register.md:147`; note the surface name "K4"
is adjudicated-overloaded and is NOT offered as a separate graph option — blind-audit finding
3.12), which element values (imported from `src/ave/core/constants.py`, never typed), which
observables (single-cell resonance; small-cluster eigenfrequency set; N-cell chain two-port
response), and which engine-side reference path computes each — plus a **TradeStudy doc
(decisions OPEN)** covering §6. Deliverable: both docs + the frozen Phase-1 prereg skeleton.
GATE: Grant ratifies the trade-study decisions marked his.

**★ PHASE-0 NAMED INPUTS (2026-08-23 blind-audit intake — land in the Requirements/TradeStudy
docs, do not rediscover):**

1. **The Bloch-expressibility problem (finding 3.9).** The canonical band structure is a 3D
   Bloch object on the 4-site srs primitive cell (top at H); a SPICE netlist cannot impose a
   complex Bloch phase, and a "periodic chain/ring" does not sample it. Phase 0 must pick the
   dispersion observable from the tractable substitutes — finite 3D supercell eigenfrequency
   SET (Phase-1-class observable) vs long-open-chain S21 phase-unwrap (a 1D-reduced object
   that canonical ω(k) is not) — and state exactly what each does and does not compare.
2. **An observable that is not a wiring theorem (finding 3.8).** The band-top CLASS check is
   an exporter-integrity gate (§ Phase 2); the requirements doc must name at least one
   quantitative observable whose value is not fixed by {3-regular, bipartite, identical
   lossless lines} alone.
3. **The Phase-1 anchor's termination (finding 3.10).** "Single cell" must be defined: a bare
   LC tank is exactly 1/√(LC); an srs z=3 VERTEX is an intrinsically mismatched reciprocal
   3-port (Γ = (2−z)/z = −1/3, `manuscript/ave-kb/common/translation-tables/translation-circuit.md:189`) whose resonance depends on bond
   terminations. The requirements doc states the pilot object and its termination explicitly.
4. **The ω_C scale-label fork (finding 3.11).** Under R2 (adopted) the scalar top is
   π√3 ω_C = 5.4414 ω_C; under R1 every ω_C band label divides by √3. Tolerances are frozen
   against `constants.py` values, so the requirements doc names the label convention — else a
   √3 offset can masquerade as a defect.
5. **Demotion-aware engine-side references (finding 3.13).** `srs-band-structure.md` carries
   two dated demotion notes on its longitudinal/vector rows; the §2 scalar arccos fact
   survives both, but reference extraction must not walk into demoted rows.

### Phase 1 — Pilot: single cell + smallest cluster

Export one cell, then the smallest nontrivial cluster, to the chosen solver. Adjudication
anchor: the **single cell's resonance is analytically exact**, so BOTH the engine and the solver
are first checked against the closed-form value independently — a three-way anchor that
localizes any Phase-1 divergence immediately (a solver-vs-engine diff with both-vs-analytic
receipts attributes itself). Tolerances frozen in the Phase-1 prereg BEFORE any comparison run.
GATE to Phase 2: agreement at the pilot scale, or an attributed-and-repaired divergence.

### Phase 2 — Marquee: dispersion and the band-top class

Export a periodic chain/ring of carrier cells; extract the dispersion relation from the
solver's two-port response; compare against the engine-side band structure whose methods fact
is canonical (the arccos TL map, `srs-band-structure.md` §2). Two comparisons, one quantitative
and one structural:

- **Quantitative:** dispersion curve agreement within the frozen tolerance across the scanned
  band.
- **Structural (parameter-free):** the band TOP must present as a **Bragg / half-wave
  resonance, not a stop-band edge** — the class fact carved at
  `manuscript/ave-kb/common/translation-tables/translation-circuit.md` (carve 4) and grounded
  at `srs-band-structure.md` §2. **Honest scope (blind-audit finding 3.8):** the band top
  π·ω_link is a theorem of {3-regular, bipartite, identical lossless lines} — attained iff the
  adjacency spectrum reaches μ = −3, which srs's bipartiteness guarantees. A solver
  reproducing it therefore verifies the EXPORTER built such a net (the §5.3(a) hand-audit's
  receipt), not engine independence. It stays in Phase 2 as an exporter-integrity gate; the
  independence weight rests on the quantitative dispersion comparison, and Phase 0 owes an
  observable that is NOT a wiring theorem (§4 Phase-0 named inputs).

Engine-side reference numbers are re-derived at run time under the reproduction gate (no banked
number is load-borne without a fresh receipt). GATE to Phase 3: Phase 2 banked + a named
consumer for the nonlinear extension actually existing.

### Phase 3 — CONDITIONAL: the saturation kernel as a behavioral varactor

SPICE-class solvers support voltage-dependent capacitance natively (behavioral sources). The
Ax4 kernel is canonically mapped as a varactor C-vs-V curve (`manuscript/ave-kb/common/translation-tables/translation-circuit.md`, the
saturation-kernel row). A behavioral-C export would cross-check the engine's *weakly
nonlinear* small-network response — harmonic generation onset, amplitude-dependent detuning —
against an independent nonlinear integrator. **Explicitly gated**: does not start without
Phase 2 banked, a named consumer, and its own Grant GO. If no consumer materializes, this
phase is deleted, not parked.

## §5 — Validation discipline (applies to every phase)

1. **Prereg-frozen tolerances.** Every comparison's tolerance is frozen in a prereg BEFORE the
   first cross-run; tolerance changes after first light are Rule-12 dated amendments, never
   silent edits.
2. **Reproduction gate on engine-side numbers.** Every engine-side reference is re-derived on
   the current engine at comparison time; drift between banked and fresh values is itself a
   finding, banked under a dated note.
3. **Divergence adjudication protocol.** Three suspects, fixed order: (a) exporter (checked by
   hand-audit of the emitted netlist against the graph + constants — the netlist is
   human-readable by design); (b) solver numerics (checked by integrator/tolerance sweep on
   the solver side, and where available a second solver); (c) engine (what remains). The
   Phase-1 analytic anchor localizes (a)-vs-(c) at pilot scale before either is trusted at
   Phase-2 scale.
4. **No tuning to agreement.** The exporter has no free parameters by construction — topology
   from the engine's graph, values from `constants.py`. Any knob that would let the export be
   tuned toward agreement is a design defect in the exporter.
5. **Lattice-derived completeness.** A comparison counts only when every element of the
   exported network derives from the canonical chain or carries an explicit engineering-choice
   tag (solver step ceilings, sweep ranges). Partial derivation = not yet a test.

## §6 — Trade study: decisions OPEN (Phase 0 closes these)

| # | decision | options | leaning (not a ruling) | whose call |
|:--|:--|:--|:--|:--|
| T1 | Solver | ngspice / Xyce / both | ngspice first (ubiquitous, scriptable); Xyce as the second-solver arm of §5.3b | lane, ratified by Grant |
| T2 | Bond representation | lossless TL element per bond vs lumped-LC ladder vs mutual-K | **TL element** — the substrate model is TLM; SPICE's lossless line is the same object. Mutual-K (the archived code's choice) is pre-rejected: it is not the substrate's coupling | Grant (physics-adjacent) |
| T3 | Graph source | engine's own adjacency export vs hand-built fixtures | engine export (fixtures can silently drift from the engine's graph) | lane |
| T4 | Observable extraction | two-port S-params vs driving-point impedance vs transient ringdown | frozen per-phase in the prereg; Phase-2 leaning = two-port response | lane |
| T5 | Where results live | `research/` prereg+result pair per phase, per the standing grammar | — | standing convention |

## §7 — Skill-selection plan (pre-workstream)

Applied set for the implementing lanes: `ave-canonical-source` (every element value),
`substrate-native-check` (the graph and bond representation walk BEFORE exporter code),
`consistency-vs-emergence` (register: implementation-verification — declared in §1 and
re-declared in every result doc), `ave-reproduction-gate` (§5.2), `verify-before-cite` (all
engine-side reference pointers), `phase-space-coordinate-check` (dispersion extraction
coordinates vs the canonical map's), `ave-driver-script-honesty` (exporter and comparison
drivers), stop-and-ask (2-attempt cap). Retro-pass at each phase close if the applied set
drifted.

## §8 — Kill / park criteria

- **KILL (epic-level):** Phase 1 cannot reach agreement-or-attributed-divergence after the §5.3
  protocol runs to completion — the instrument is unsound; bank the negative and stop.
- **PARK:** Phase 0 trade study surfaces a blocker priced above the epic's value (e.g. no
  solver represents the bond object without distortion), OR no consumer for Phase-2 receipts
  exists when Phase 1 closes. Parked ≠ deleted; the park reason is banked here.
- **SCOPE-KILL (standing):** any drift toward matter-modeling, scale, or physics-validation
  framing (§3) is out of scope by construction and reverts on sight.

## §9 — Relationship to existing infrastructure

- **Testing pivot:** this epic is squarely inside the program's infra-first testing posture —
  it hardens engine trust, it does not mint physics.
- **BenchModel spine:** Phase-1/2 receipts are candidate inputs to the bench-model gate
  family; wiring them in is a follow-on, not part of this epic.
- **Acceptance-test arc (Vol 9 Ch 17):** same medium-up, falsifiable-unit-test philosophy;
  this epic adds the *independent-integrator* axis that arc does not have.
- **cRIO bench (deferred):** the hardware analog of the same independence idea; nothing here
  blocks or is blocked by it.
- **Canonical anchors:** `src/ave/core/constants.py` (values), `srs-band-structure.md` §2
  (methods fact + band-top grounding), `manuscript/ave-kb/common/translation-tables/translation-circuit.md` carve 4 + saturation-kernel
  row (band-top class; varactor mapping), engine-capability-map (which engine backend computes
  each reference).

## §10 — Explicitly not worth doing (truth-per-token)

- Full-lattice export at engine scale (SPICE-class solvers are the wrong tool past small
  networks; independence is only cheap when the network is small).
- A GUI/schematic pipeline, LTspice compatibility work, or netlist aesthetics.
- Cross-checking observables the engine does not itself certify (no reference = no test).
- Restoring or "fixing" the archived exporter (§3.1 — settled by the ruling).
