# WALK RECORD — G1: the AC-steady-state reframe of the static-existence test (2026-08-24)

**Status: the G1 ontology walk of the static-existence epic, WALKED and
RECORDED.** Grant's pushbacks refuted the presented framing; the corrected
framing below is the walk's outcome. WALK-grade where marked; the reframe
itself is a TEST-DESIGN ruling (what the test IS), not a physics claim.

**Grant, verbatim (the four pushbacks that did the work):**
- Q4: *"this doesnt make physical sense to me? have you mapped the ee
  circuit?"*
- Q1: *"again, whats the definition of clamp? saturation? what do the network
  equations say?"*
- Q2: *"what?"*
- Q3: *"we can map the electrons behavior to 1.3 ppt, what does that tell
  us?"*
- On the reframe's key concept: *"ah! ac steady state, what do you mean?"* —
  followed by *"ok, whats next?"* (the walk's close).

---

## §1 — The correction the walk produced

The G1 packet's framing ("impose a static texture, relax the lattice") was a
MECHANICS framing of an EE problem, and it failed the EE-first mapping it
should have started with:

**The (2,3) is an AC object.** Two resonances of the bond-pair tank,
frequency-locked 3:2, in steady state. There is no DC state of a network that
"is" a winding — the winding number is bookkeeping of an AC steady state.
"Static" in the named test therefore means **STATIONARY, not DC**: everything
moves, nothing changes — the phasor description is a fixed point, the orbit
closes on itself identically every period, envelope and class are constants
of motion. Canon already runs on this without saying the words: DP-1's kernel
argument A is *"the cycle time-average … NOT an instantaneous phase
snapshot"* — the Axiom-4 machinery was always an AC-steady-state theory.

**The two-layer completion** [ASSEMBLY over R43–R50 + DP-1]: the source law
owns the DC side — the quiescent Q-point IS the DC operating point — and
**the particle is the AC steady state riding on it**. Bias point plus signal;
a bench amplifier's anatomy. The R46 "Substrate DC Bias" naming lands
exactly on this structure.

## §2 — The test, reformulated (the walk's design outcome)

**Old form (refuted):** impose a texture, relax, read railing. "Relax" is
undefined on a lossless reactive substrate; texture-clamping conflates DC and
AC; bleeding-under-hold created an unadjudicable ambiguity.

**New form: autonomous-mode existence via HARMONIC BALANCE.**
1. Posit the tone set (the 2 and 3 lines on the bond-pair structure).
2. Write phasor-domain Kirchhoff on the graded network, INCLUDING the
   varactor's tone-mixing (S(A) is the nonlinearity coupling the tones —
   the same per-directed-bond admittance machinery the Class-C lane used).
3. Solve the algebraic fixed point — no time-stepping, no transients, no
   damping device, Ax3 never touched.
4. **The existence criterion is SOURCE-IDLE self-consistency:** solve the
   driven steady state, then check the scaffold sources go idle at the
   solution (source current → 0, delivered power → 0). The wall the solution
   maintains must be made of the solution's own amplitude — *"the mirror is
   made of the thing it confines"* — which is what Grant's one-word
   *"saturation?"* answer to the clamp question meant: the real electron's
   clamp is the self-clamp; external sources are scaffolding, and the test
   is whether the scaffold can be removed.
5. **DISPROVE, pre-frozen:** no source-idle solution with a railed core
   exists. The old bleeding-ambiguity never arises — nothing is held at the
   solution.

**"Clamp," defined in network equations** (Grant's Q1): source termination
(the KUBC/voltage-clamp class, canon's own homogenization row) for the
solve; injection lock as the entrainment-only variant. Both are scaffolds
subordinate to the source-idle criterion.

## §3 — The ppt resolution of the sector question (Grant's Q3)

The electron's behavior is mapped to ~ppt entirely through its projections
(moment, charge, mass), and canon's boundary law says only the edges project
— the interior trace is invisible. Two consequences, both adopted as test
design:

1. **Imposition routes are behaviorally equivalence-classed by their
   projections.** "Which sector receives the imposition" has no observable
   answer; the test picks the computationally cleanest representative and
   claims nothing sector-specific. [Adopted; the equivalence itself gets a
   RECEIPT — see §4 item 2.]
2. **The ppt map is a consistency ceiling:** any railed-core solution found
   must leave the projected moment within the measured band, or it is not
   describing an electron. Goes in the frozen criteria.

## §4 — Residual choices (PROPOSED at the walk's close; confirm at G2)

1. **Scaffold:** source-terminated boundary phasors for the solve;
   injection-lock as the cross-check. [Orchestrator lean adopted as
   PROPOSED per Grant's "ok, whats next" close; G2 confirms.]
2. **Observable set:** S-profile railing (the named verdict) + the projected
   M/Q read on TWO different imposition representatives — turning §3's
   equivalence claim from an argument into a receipt. [PROPOSED, same
   basis.]

## §5 — Consequences routed

- The epic's P2 is REWRITTEN to the autonomous-mode existence solve (same
  commit as this record). The α-agnostic guard (epic guard 8) carries over
  naturally: harmonic balance posits tones, not tube phases.
- The named-extension list changes: the "texture-hold constraint" extension
  is RETIRED (nothing is held at the solution); the HARMONIC-BALANCE SOLVER
  on the graded srs network is the new build item; the transverse graded
  scatter (P1) and the α-family sweep harness stand.
- The prereg's config-grep obligations are UNCHANGED (the closed negatives
  are formation-dynamics configs; a phasor-domain fixed-point solve is
  config-disjoint from all of them by construction — but the grep is still
  owed, not waived).
