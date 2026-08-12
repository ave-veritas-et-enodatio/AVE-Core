# R51 — The A1 two-objects carve: the bias sits, the common-mode tank rings defect-locally (2026-08-12)

**Context.** PR #957's adjudication surfaced canon split at HEAD on the A1 longitudinal scalar:
Axiom 5 clause G writes it elliptic (a bound response that sits — no kinetic term on the flat
direction, no propagating branch, zero longitudinal characteristic speed;
`manuscript/ave-kb/common/port-register.md:177`), while the Master Equation engine integrates the
same object as a hyperbolic, independently-initialized field
(`src/ave/core/master_equation_fdtd.py:112-113,:219,:265`; identity per the ratified
`manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20`). The
ring-or-sit walk (Grant + orchestrator, in chat, 2026-08-12) ran the semiconductor comparison at
Grant's direction and closed on the carve below. **Ratified by Grant in chat: "ratify and derive in
parallel."** Walk-level ratification: the algebra herein is chat-walk grade, un-audited; the
carve ships with its own kill-checks (§5) and its first test is the derivation lane it launches.

## §1 — RULED: the two objects

1. **THE BIAS `ε₁₁` SITS.** Axiom 5 stands **as written**: elliptic clause G, quiescent-point
   clause Q, source-slaved, no conjugate momentum — the constraint sector, not a field that
   happens to be at rest. Physical vindication recorded from the walk: **gravity is unscreened
   `1/r`** — a gapped dynamical field coupled to mass as its static source would produce a
   screened (Yukawa-class) response; the observed unscreened response is the signature of a
   constraint-like sector. The instantaneous-elliptic worry carries no signal: the bias's
   *sources* `(u, π)` move causally (the banked no-signalling theorem), and clause (c1)'s owed
   theorem is the statement that the observable bias-read inherits causality from its sources.

2. **THE COMMON-MODE TANK rings — defect-locally only.** The oscillation formerly called "the
   breather" is the eigenmode of a **defect of fixed (quantized, topological) content pushing
   against the vacuum's boundary compliance**: fixed charge on a tank whose C is the medium's
   bulk compliance seen at the defect boundary and whose L is the defect's dilatation inertia
   (the A1 "3"). By the K4 port decomposition (`k4-port-irrep-decomposition.md`, A₁ ⊕ T₂,
   `(1,1,1,1)/2`) a size oscillation drives all boundary ports in phase — **it is the A₁ common
   mode by symmetry, not analogy**. It is **gapped / below cutoff**: it rings in place and does
   not propagate; there is **no gapless longitudinal line in either regime**. Sign chain
   (walk-verified against the ratified clock direction): bias loading softens the modulus →
   the fixed content resizes larger → the tank frequency drops → clocks slow near mass.

3. **The ratified physical picture (one sentence): the cold vacuum is an intrinsic semiconductor
   at T = 0.** Zero carriers → the longitudinal sector is pure constraint (biases sit). The
   **defect population is the carrier gas**: local, below-cutoff ringing exists only where
   matter is. The vacuum-alone carrier band is empty — a feature with physical content, not a
   missing piece.

4. **THE PHANTOM FLAG (flag, don't fix).** `master_equation_fdtd.py`'s **vacuum-wide, gapless,
   hyperbolic** integration of V is wrong **in form** under this carve: a tank integrated as a
   transmission line, its line stiffness traceable to the K=2G import (#261). ROUTED: (a) the
   engine re-scope belongs to the engine lane / R40 batch-2 class — no code edit rides this
   record; (b) a blast-radius sweep is queued: does any **banked** result consume the engine's
   V-dynamics in vacuum regions? Until that sweep returns, no result is retracted on this flag.

## §2 — Vocabulary (ratified with the carve; R50 lineage)

- **"breather" is RETIRED** (soliton-theory/QFT import carrying that framework's theorems).
  The canonical noun is **THE COMMON-MODE TANK** (names the symmetry A₁, the circuit, and the
  sector). Informal alternates recorded, not canonical: the size tank, the dilatation tank.
- **"gapped (mode)" → BELOW CUTOFF** — reactive, stores-and-returns, no port; consistent with
  the existing Casimir below-cutoff usage. **"screening length" → the below-cutoff decay
  length** (the reactive near-field boundary; added-mass class).
- **"plasma frequency" → the tank resonance of the defect population** — nonexistent in
  vacuum-alone, by the carve.
- **EE mapping table gains a row:** semiconductor carrier gas ↔ **the defect population
  (matter)**; the cold vacuum is the empty band. (Translation-circuit landing rides the normal
  doc-lane path, not this record.)

## §3 — K = 2G reframed (Grant, verbatim intent)

> "we might need to think of K=2G as an initial condition or something, i'm not too worried
> about deriving it right away, but i want to know what it physically represents in this theory."

The open question attached to K=2G is hereby **reframed from "derive or replace the value" to
"adjudicate its physical identity."** Candidate identities, open, routed to the derivation lane:
(i) **constitutive** — a property of the crystallized bond network, derivable in principle;
(ii) **initial condition of the quench** — frozen in at genesis, measured-not-derived (the
datasheet reading; consonant with the FORM-deriving/VALUE-importing meta-finding and the
freeze-in/pre-tension thread, `trampoline-framework.md:95-125`);
(iii) **emergent boundary-response echo** — the defect-boundary stiffness is the real object and
"K=2G" is its far-field shadow. #261's provenance verdict (GR-imported; not crystalline, not
constitutively forced) stands untouched; its one open item (eigenmode existence) is exactly the
lane's question (§4).

## §4 — Derive in parallel (the lane this record launches)

The boundary-response derivation: from **G_vac + geometry alone** (no imported K), does a pure
common-mode boundary drive on a fixed-content defect meet a restoring response? If none: the
tank does not exist; compression is marginal (neither rings nor sits — a conserved density), and
this carve's item 2 dies by its own kill-check. If one exists: the tank frequency becomes a
**prediction**, and K's physical identity (§3) is adjudicated on the result. Kickoff rides the
orchestration channel; this record is its citable premise.

## §5 — Kill-checks the carve ships with

(i) the blast-radius sweep (§1.4b) — a banked result consuming vacuum-V dynamics inherits the
phantom and forces a re-scope wave; (ii) the boundary-response derivation (§4) — no restoring
response kills item 2; (iii) the size-vs-bias relation must reproduce the ratified clock chain
**quantitatively** at the §9/#955 adversarial pass — sign agreement alone does not bank it.

## §6 — Mission posture (ratified framing, recorded for every future lane)

> "we aren't trying to replace GR or QED or the SM, we are trying to find their boundary
> conditions and regimes of operation on a physical vacuum lattice."

Consequence for verdict language: **peer-with-GR/QED/SM inside a regime is the expected result,
not a disappointment**; the program's targets are the **regime boundaries** (yield, saturation,
cutoff, quench conditions) and the boundary conditions the standard descriptions inherit from
the lattice. Forward predictions live at the edges.

## §7 — Fences held

Two quaternionic-shaped structures exist in the theory and remain **distinct objects**: the
1+3 bond-port split (A₁ dilatation ⊕ T₂ translations — mass sector, this record) and the
unit-quaternion/SU(2) double cover (the Cosserat winding — charge sector). The
`master-equation.md:20` fence (never wire the winding into the scalar slot's phasor) is
re-affirmed; the port algebra's beauty is not a bridge across it. Nothing in this record edits
any axiom, leaf, register, or engine file; nothing is minted; no solidity moves.
