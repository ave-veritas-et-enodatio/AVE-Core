# The Chiral Vacuum Reactor — naming, reactor-family, helicity-as-acquired, the lossless formulation, and the v10 charter

**Date:** 2026-06-11
**Lane:** implementer (research-doc capture of the 2026-06-10/11 genesis mega-session)
**Branch:** `analysis/2026-06-11-cvr-framing`
**Status:** framing-capture + charter. **Adjudication-gated.** This document
*records* Grant-ratified naming decisions and *stages* the four blocking
decisions for the v10 build. It commits nothing to canon, edits no registry row,
freezes no pre-registration. The v10 charter (§5) is gated on the four Grant
calls; the v9 Phase-1 pre-registration it points at is itself a DRAFT
(`research/2026-06-11_genesis-v9-phase1-prereg_DRAFT.md`, PR #195), not frozen.

> **Companion to the in-flight vocab/operator audit** (`analysis/2026-06-11-vocab-operator-audit`,
> PR #196). The reactance-as-bookkeeping and Tellegen content this document
> cross-references *lands there*, not here. This doc does not restate or upgrade
> those rows; it points at them.

---

## Class-tag legend (used inline; per `consistency-vs-emergence` + `ave-evidence-framing-discipline`)

- **[fact]** — independently verifiable (date, attribution, grep-confirmed file content).
- **[Grant-ratified / session-record]** — a naming or framing decision Grant
  canonized in the 2026-06-10/11 session. Framing, not a numerical prediction.
  Provenance is the session transcript, not a committed canon leaf — tagged so.
- **[consistency-class]** — an internally-consistent, intuition-bearing bridge
  that is *not* a derivation or a forward prediction (the historical-precedents
  ceiling: "echo, not chord").
- **[emergence-class]** / **[consistency-class-numeric]** — a numerical claim
  graded per `consistency-vs-emergence`: emergence = zero in-sector input;
  consistency = sector inputs (e.g. `m_e`, `α`) carried through.
- **[hypothesis-class]** — a candidate claim not yet verified; carries a named
  scout-assignment or open obligation.
- **[open-gap]** — a named, currently-unmet obligation a definition carries.
- **[external-bound: requires verification]** — an external empirical bound
  cited as a *floor schema*, with the specific number NOT asserted here.

## Verification ledger (every canon anchor re-grepped this session, `AVE-Core @ origin/main f6ffd98d`)

| Anchor | What it supports | Status |
|---|---|---|
| `manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md:21` | electron = `0_1` unknot ground state, "No torsional excitation is present" | VERIFIED |
| `…/lepton-spectrum.md:33` | muon = `0_1` unknot "absorbing exactly one quantum of chiral torsional coupling" | VERIFIED |
| `…/lepton-spectrum.md:84` | lepton rows = "matched closed-form CONSISTENCY — NO solver" (distinct lower tier than proton FS eigenvalue) | VERIFIED |
| `…/lepton-spectrum.md:29` | 🔴 OPEN FLAG: `√(3/7)` "PAT torsion-shear" label contested (Rule 12, Grant pending) | VERIFIED |
| `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:18` | conflation locus: "the longitudinal re-engages at saturation = the electron" | VERIFIED |
| `…/master-equation.md:20` | 🔴 TWO-"3"s DISAMBIGUATION (A1 dilatation-MASS vs Cosserat `(2,3)` WINDING), Grant-ratified | VERIFIED |
| `manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md:23,33,41` | proton `(2,5)` c=5: 938.254 vs 938.272 MeV; bare topology **+0.74%** (emergence vs baryon sector), `δ_th` refines to **−0.002%**; "do not headline pure-geometry-to-ppm" | VERIFIED |
| `manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/proton-identification.md:13` | `m_p/m_e = 1836.12` derived, zero baryon-data-tuned params; bare +0.74% → `δ_th` → −0.002% vs CODATA 1836.153 | VERIFIED |
| `…/proton-identification.md:19` | `(2,5)` cinquefoil = **phase-space per-loop polarization winding, NOT a real-space knot** (relabel 2026-06-08); real-space = `6_2^3` Borromean | VERIFIED (load-bearing refinement) |
| `…/proton-identification.md:45` | proton stability = Ax2 TKI topology conservation, "cinquefoil is irreducible", "Topological protection same mechanism as electron", axiom-derived | VERIFIED |
| `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md:181` | the `R/r = φ²` ladder: "answered NO across all sampled sectors and views" — Mode III canonical across 10 tests | VERIFIED (the engine-scale negative) |
| `…/l3-electron-soliton-synthesis.md:11,26` | `(2,q)` family: q=3 electron, q=5 proton, q=7 Δ; Mode III canonical + 1 structural partial positive | VERIFIED |
| `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-unknot-cosserat-seeder.md:94` | Mode III defn: "Cosserat seed works at t=0 but decouples from K4 … engine doesn't autonomously sustain the bound state" | VERIFIED |
| `research/2026-06-10_foreword-proposal_two-deletions.md:151-156` | Kelvin vortex-atom ontology "died with its substrate, not by refutation"; SR (1905) "removed the need for [the medium]" | VERIFIED (grounds spacetime = post-deletion noun) |
| vocab-audit PR #196 `research/2026-06-11_vocab-operator-unification-audit.md:139,176` | "reactance as the universe's bookkeeping" Grant-ratified 2026-06-11; lossless-lattice branch-power sum | VERIFIED |
| `…vocab-operator-unification-audit.md:170-176,315` | Tellegen's theorem **VIRGIN** in canon (grep=0), staged as named EE-first import candidate | VERIFIED |
| `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md:~35` | reactance-bookkeeping table: "Electron orbital \| 90° \| 0 W \| `m_e c² · α` \| Quantized reactive shell" | VERIFIED (grounds the §5 `E_boundary = α·mc²` prereg) |
| `research/2026-06-11_dark-sector-response-characterization.md:359` (dark-sector branch) | the `:359` anchor = `H_shear / H_EM / H_bulk` transfer-function row | VERIFIED |
| `src/ave/core/sonic_horizon_flow.py:52` (dark-sector branch) | `chi_shock` default 1.0, apparatus dissipation knob ("fraction of void KE dissipated") | VERIFIED |
| v9 driver `chiral_lattice_smoke_dynamics.py` (live-fired this session) | Bishop transport `Δθ/L = +75.462°/unit` srs-R, `−75.462` mirror; writhe `∓4.0867e-02`; diamond `0.0` | VERIFIED |

**Discrepancies flagged (not silently fixed):**
1. **Bishop rate rounding.** The exact live-fired value is `±75.462°/unit`. PR #195's
   body and the v9 prereg DRAFT (`:36`) both round to `±75.5°/unit`. This document
   uses the exact value; the rounding is cosmetic but recorded.
2. **Phase-space vs real-space knot coordinate (A46).** The task framing
   "no continuous cinquefoil→trefoil path" reads naturally as a *real-space* knot
   statement. The corpus relabeled (2026-06-08) the `(2,5)` and `(2,3)` as
   **phase-space per-loop polarization windings, NOT real-space knots**
   (`proton-identification.md:19`; electron parallel at `electron-identification.md`).
   §2 states the class-separation argument in the phase-space-winding coordinate
   accordingly — flagged, not reframed.

---

## §1 — The CVR naming (Grant-ratified 2026-06-11)

### §1.1 The object class and its two registry-row candidates

[Grant-ratified / session-record] The object class condensed in the v9/v10 work
is named the **CHIRAL VACUUM REACTOR** — *the device* — which presents a
**CHIRAL VACUUM REACTANCE** — *the port quantity*. These are two registry-row
candidates, a device/port pair, NOT two names for one thing:

- **Chiral Vacuum Reactor (CVR)** — the built object. In the power-EE register
  this is the natural noun: **a reactor IS a built inductance** — a deliberately
  constructed energy-storing reactive element (a power reactor, a line reactor,
  a shunt reactor). The chiral vacuum lattice that hosts a persisting,
  handedness-bearing standing reactive state is, in this register, a reactor.
- **Chiral Vacuum Reactance** — the *port quantity* the reactor presents:
  the reactive (lossless, energy-storing, `90°`-out-of-phase) impedance seen
  at its terminals, carrying a handedness.

[Grant-ratified / session-record — voice-to-text correction trail] The
device-vs-port distinction is the correction trail itself: the dictated term
oscillated between *reactor* (the thing) and *reactance* (the quantity it
presents) before Grant fixed both as **distinct registry rows** rather than
collapsing them. The trail is preserved here per Rule 12 (record the
disambiguation, do not silently pick one): the device is the **reactor**, the
port quantity is the **reactance**, and both earn a row.

> **EE-purist metonymy note.** [consistency-class] A working EE will say "a
> reactance" to mean "a reactor" the same way "a resistance" stands in for "a
> resistor" or "a load" for the device drawing it — port-quantity-for-device
> metonymy. The corpus tolerates the metonymy in prose but the **registry keeps
> the rows separate**: when a claim is about the *built object* it cites the
> reactor row; when it is about the *measured port impedance* it cites the
> reactance row. This is the same device/quantity hygiene the vocab audit
> (PR #196) enforces on `Z_EM / Z_shear / Z_bulk` (the channel impedances) vs
> the elements that present them.

### §1.2 The rejected variant — "chiral spacetime"

[Grant-ratified / session-record] The variant **"chiral spacetime"** was
considered and **REJECTED** by the corpus-vocabulary law.

**Rationale (grounded in the foreword thesis).** [consistency-class] In the AVE
corpus, *spacetime* is the **post-deletion GR noun** — the word physics adopted
*after* deleting the medium. The foreword two-deletions thesis records this as
[fact + consistency-class framing]: Kelvin's vortex-atom ontology "did not fail
on its own terms; it lost its terms … the medium itself was taken away:
Michelson–Morley (1887) found no aether, and special relativity (1905) removed
the need for one. **The ontology died with its substrate, not by refutation**"
(`research/2026-06-10_foreword-proposal_two-deletions.md:151-156`, VERIFIED).
General relativity then built its geometric noun — *spacetime* — on that
vacancy. The AVE program's whole move is the **restoration of the medium** (the
lattice). To name the device a "chiral *spacetime*" would import the very noun
that *names the deleted medium's absence* — a category error against the
corpus's founding thesis. The medium is real and compressible; its reactive,
handedness-bearing built state is a **reactor**, not a "spacetime."

> This is a vocabulary ruling, not a physics claim. It is tagged
> [Grant-ratified / session-record]; the foreword thesis it leans on is itself
> [consistency-class] (the historical-precedents ceiling — "echo, not chord").
> The ruling does not elevate the foreword thesis past that ceiling.

### §1.3 The frozen v10 outcome bin — CVR-SET — and the failure ladder

[Grant-ratified / session-record] The single pre-committed PASS bin for the v10
convergence build is named **CVR-SET**. A CVR-SET outcome requires the
conjunction of **formed** AND **set**:

- **formed** — the condensation actually ran (a localized state assembled from
  the precursor, not planted); the handedness is **geometry-supplied** (inherited
  from the lattice, surviving the `κ_chiral = 0` ablation); and the formed state
  is **enantiomorph-odd** (its chiral observable flips sign under the
  mirror / enantiomorph swap).
- **set** — the formed state **persists with the drive off** (a standing,
  self-sustaining reactive state, not a driven transient).

The pre-committed **failure ladder** (the bins a run can land in *instead* of
CVR-SET), in order of increasing structure:

| Bin | Meaning | Maps to v9 P6 bin |
|---|---|---|
| **DISPERSES** | linear-like spreading at every sub-rupture amplitude; the lattice never localizes the precursor | BIN-D (dispersal) |
| **TRANSIENT** | localization forms then decays once the drive is removed; record lifetime vs launch amplitude; hosting-adjacent, NOT genesis | BIN-T (transient) |
| **SET-ACHIRAL** | a state forms AND persists drive-off, but it is **not** geometry-handed / not enantiomorph-odd (e.g. survives but on the diamond control, or its chirality collapses under `κ_chiral = 0`) | (a structured partial — sets but fails the chirality leg of BIN-G) |
| **CVR-SET** | formed [condensation ran, geometry-supplied handedness, enantiomorph-odd] AND set [persists drive-off] | BIN-G (genesis) |

> **SET-ACHIRAL is the load-bearing discriminator rung.** [open-gap] It is the
> bin that separates *hosting a persistent state* (P5-class: a state the lattice
> can carry) from *genesis of a chiral state* (the v9 H2 claim: handedness
> inherited from geometry). Per the v9 prereg's own Checkpoint-8 caveat
> (`…genesis-v9-phase1-prereg_DRAFT.md:73-96`), a P5-pass + BIN-D combination is
> hosting-but-no-genesis and "MUST NOT be reported as a genesis pass." SET-ACHIRAL
> is the precise name for the persist-but-not-chiral failure that the genesis
> claim must clear.


## §2 — The reactor family

[Grant-ratified / session-record] Grant's framing: *"the electron = the most
fundamental, most restricted-DOF chiral vacuum reactor; protons/neutrons = more
complex reactors."* The particle zoo, read in the reactor register, is a family
of reactors ordered by **how many degrees of freedom the standing reactive state
engages** — the electron at the floor (fewest engaged DOF, most restricted), the
baryons above it (more engaged DOF, more complex internal reactive structure).

### §2.1 The catalog (with VERIFIED canon topology anchors)

> **Coordinate discipline (A46) up front.** The `(2,q)` labels below are the
> **phase-space per-loop polarization windings** in the flux-tube cross-section's
> EM-polarization phase space `(V_inc, V_ref)`, **NOT real-space knots** — the
> 2026-06-08 relabel (`proton-identification.md:19`, VERIFIED). The real-space
> ground-state topology is a separate column (electron `0_1` unknot; proton
> `6_2^3` Borromean). Mixing the two is the phase-space-vs-real-space category
> error this catalog is built to avoid.

| Reactor | Phase-space winding `(2,q)` | Real-space topology | Engaged-DOF / Cosserat content | Mass anchor (VERIFIED) | Tier |
|---|---|---|---|---|---|
| **photon** | — (travelling, not a winding) | transverse free wave | pure transverse EM; the precursor the lattice self-traps (v9 P6) | massless | — |
| **neutrino** | crossing-number-split (lepton sector) | — | Cosserat lepton sector, neutrino mass via crossing-number splitting (`lepton-spectrum.md:11`, `clm-rji99i`) | [hypothesis-class within the sector] | matched-consistency |
| **electron** | `(2,3)` phase-space winding | `0_1` unknot ("No torsional excitation is present", `lepton-spectrum.md:21`) | the dilatation-MASS "3" CARRYING the Cosserat micro-rotation `(2,3)` WINDING — two orthogonal objects (`master-equation.md:20`) | `m_e` = input/calibration scale | identity (input scale) |
| **muon** | `0_1` + 1 torsion quantum | `0_1` unknot | "`0_1` unknot absorbing exactly **one quantum** of chiral torsional coupling" (`lepton-spectrum.md:33`) | `m_μ = m_e/(α√(3/7)) ≈ 107.0 MeV` (Exp 105.66, +1.24%) | **matched closed-form CONSISTENCY — NO solver** (`lepton-spectrum.md:84`) |
| **tau** | `0_1` + curvature-twist | `0_1` unknot | bending-stiffness sector; 7 radial undulation lobes from `ν_vac = 2/7` | `m_τ = m_e·p_c/α² ≈ 1760 MeV` (Exp 1776.9, −0.95%) | matched closed-form CONSISTENCY — NO solver |
| **proton** | `(2,5)` cinquefoil phase-space winding (`proton-identification.md:19`) | `6_2^3` Borromean linkage of 3 flux loops (`proton-identification.md:20`) | confined cinquefoil; saturated core (`S→0`, `G_shear=0`); 3 quark-equiv loops via `ℤ_3` θ-vacua | `m_p/m_e = 1836.12` — **bare topology +0.74% (emergence vs baryon sector, zero baryon input)**, `δ_th=1/(14π²)` refines to **−0.002%** vs CODATA 1836.153 (`proton-identification.md:13`) | **Faddeev–Skyrme eigenvalue (numerical solver)** — distinct higher tier than the lepton closed-forms |
| **neutron** | `(2,5)`-class baryon + balancing parts | Borromean + neutral-core balance | `n → p + e + ν̄` channel | `m_n` (proton-neutron mass split, `proton-neutron-mass-split.md`) | consistency (sector) |

> **Two-tier honesty (per `lepton-spectrum.md:84`, VERIFIED verbatim).** The
> lepton rows are *"matched closed-form algebraic expression[s] evaluated from
> the CODATA-input `α` and `p_c` with `m_e` as the input scale — not 'derived' or
> 'emergent', and not solver-backed … a distinct (lower) tier than the proton
> `m_p/m_e` Faddeev–Skyrme eigenvalue."* The corpus self-flags: the muon factor
> "is asserted" and the tau factor is "identified rather than derived." Read the
> lepton ✓ as **closed-form match**, not Cosserat-eigenmode emergence. The proton
> row alone is solver-backed; even there, the **+0.74% is the emergence magnitude**
> and the −0.002% is **post-`δ_th`** — `torus-knot-ladder-baryons.md:41`:
> "do not headline pure-geometry-to-ppm."

> **OPEN canon flag carried, not resolved (Rule 12).** The muon coupling
> `α√(3/7)` carries a live 🔴 OPEN FLAG (`lepton-spectrum.md:29`): `√(3/7) =
> √(1−2ν_vac)` is the **bulk/dilatational** elastic signature, yet it carries a
> "PAT torsion-shear" (deviatoric) label — an elastic-type contradiction, Grant's
> physics adjudication pending. The engine constant `_SIN_THETA_W_PAT`
> (`cosserat.py:65`) is NOT renamed. This flag is reproduced, not adjudicated, by
> this document.

### §2.2 Stability = topological class separation [consistency-class]

[consistency-class] The reactor family is stable not because each reactor sits
in an energy basin, but because **its winding sits in a topological class**, and
there is **no continuous path between classes**. Stated in the correct
(phase-space-winding) coordinate per A46:

- The proton's `(2,5)` cinquefoil phase-space winding and the electron's `(2,3)`
  winding are **different elements of the `(2,q)` winding ladder** (only odd `q`
  is stable; there is no stable `(2,4)`). There is no continuous deformation of a
  `(2,5)` winding into a `(2,3)` winding that holds the winding integer fixed —
  the crossing number is a topological invariant.
- Proton stability is therefore the SAME mechanism as electron stability:
  `proton-identification.md:45` (VERIFIED verbatim) — *"Ax2 TKI topology
  conservation (cinquefoil is irreducible; cannot decay to electron + neutrinos
  without breaking topology) … ✅ axiom-derived … Topological protection same
  mechanism as electron."* These are **class-floor facts**, not basin-depth
  arguments.
- **Decay runs only WITHIN a class.** `μ → e` (both `0_1` real-space unknots in
  the lepton sector; the muon sheds its single torsion quantum) and `n → p + e +
  ν̄` (within the baryon-plus-balancing structure) are intra-class transitions.
  No observed decay crosses a winding-class floor — which is exactly why the
  electron and proton are the stable floors of their respective ladders.

### §2.3 The parton-candidate reading [hypothesis-class — unaudited]

[hypothesis-class] A candidate reading of deep-inelastic-scattering (DIS)
sub-structure in the reactor register: the partons a high-`Q²` probe resolves are
the **strand-passes of ONE winding through the probe's resolution cell** — i.e.
DIS does not resolve three *separate* objects, it resolves the multiple passes a
single `(2,q)` winding (or its `6_2^3` Borromean real-space realization) makes
through a probe small enough to see individual strands. The "three quarks" become
the three loops of the one Borromean cage seen at strand resolution.

> **Status: HYPOTHESIS, scout-assignment named, unaudited.** This is NOT a
> derivation and NOT a forward prediction. It has not been checked against the
> corpus DIS / structure-function content, against the `ℤ_3`-θ-vacuum fractional-
> charge mechanism (`topological-fractionalization.md`), or for a Bjorken-scaling
> signature. **Scout assignment:** a separate scouting pass must (a) confirm
> whether the corpus already commits to a parton/structure-function reading, (b)
> check the strand-pass count against the Borromean loop count and the winding
> crossing number, and (c) decide whether this is consistency-class (an intuition
> bridge) or has any discriminating content. Until then it is parked here, tagged.

### §2.4 The neutron-as-balanced-reactor reading [hypothesis-class]

[hypothesis-class] A candidate reading of `n → p + e + ν̄`: the neutron is a
**balanced reactor** — a proton-class reactor carrying additional *balancing*
reactive parts (the parts that become the emitted electron and antineutrino) —
and β-decay is the reactor **shedding its balancing parts** to relax to the
lower-DOF proton-plus-leptons configuration. This is consistent with the corpus's
proton-neutron mass-split treatment (`proton-neutron-mass-split.md`) but is here a
**framing**, not a derivation: it does not yet compute the mass split, the
lifetime, or the spectrum. Tagged hypothesis-class, parked.


## §3 — Helicity-as-acquired

[Grant-ratified / session-record] Grant's framing: *"a photon's helicity actually
comes from the incident angles and the conjugate reflection of each of the
slats … we don't even need to inject helicity … We give it the first initial
direction."*

### §3.1 The mechanism [consistency-class]

[consistency-class] The reading: helicity is **not injected** into the photon as
a primitive. It is **acquired** from the medium's chiral geometry as the wave
propagates. The "slats" are the chiral lattice's structuring elements; at each
**conjugate reflection** at the slat pitch, the transverse polarization frame is
rotated, and the *accumulation* of those conjugate reflections along the
propagation direction **builds the rotating phase** that IS helicity. The only
thing supplied at launch is **the first initial direction** — a plain linear
(zero-helicity) transverse frame and a propagation direction. Handedness then
follows the identity:

> **helicity = enantiomorph × launch-direction.** [consistency-class] The sign of
> the acquired rotation is the product of the lattice's handedness (which
> enantiomorph) and the launch direction (which way along the screw). Reverse
> either one and the helicity flips; reverse both and it is unchanged.

### §3.2 The Phase-0 evidence — the Bishop smoke (VERIFIED, live-fired)

[VERIFIED] The v9 Phase-0 transverse smoke is the first empirical support for
"acquired, not injected." A **zero-helicity linear** polarization frame, given
only a propagation direction along the lattice's exact `4_1` screw orbit and
Bishop-transported (parallel transport, NO injected twist term), **acquired a
nonzero, exactly mirror-odd rotation from the screw geometry alone**
(`chiral_lattice_smoke_dynamics.py`, live-fired this session):

```
srs-R screw helix          : Δθ/L = +75.462 deg/unit   τ = +0.5223
mirror(srs-R) = true srs-L : Δθ/L = −75.462 deg/unit   τ = −0.5223
--> MIRROR-ODD exact: |Δθ/L sum| = 0.0,  magnitudes match
srs-L INDEPENDENT 4_3 axis : Δθ/L = +17.941 deg/unit   (same sign as srs-R)
```

with the load-bearing signed channel (reflection-odd ring writhe):

```
srs-R (I4_1 32) : −4.08672e-02   (std 2.7e-09, 36 rings)
srs-L (I4_3 32) : +4.08672e-02   (std 2.2e-09, 35 rings)
diamond control : +0.00000e+00   (std 0.0,    9 rings)
```

The launched frame carried **zero injected helicity**; the `±75.462°/unit`
rotation is built entirely by the conjugate-reflection / Bishop transport along
the screw — handedness from the geometry, flipping sign under the mirror, exactly
zero on the achiral diamond control. This is the "we don't need to inject
helicity" claim, observed at Phase-0 scaffold scale.

> **Rounding note (flag, not fix):** PR #195's body and the v9 prereg DRAFT round
> this to `±75.5°/unit`. The exact live-fired value is `±75.462°/unit`.

### §3.3 Three honest flags (NOT upgraded)

[open-gap] The Phase-0 Bishop smoke is **kinematic, not dynamical** — three flags
bound exactly what it does and does not show, carried verbatim from the v9 design
§3 / prereg:

1. **Kinematic ≠ dynamical.** Bishop transport rotates a frame along a *fixed
   geometric* helix; it is not yet the **dynamical** optical rotation of a packet
   propagating under the vector-TLM + Op14 dynamics. The per-length transport RATE
   does **not cleanly converge at Phase-0** (~9% discreteness wobble on the
   discrete 4-gon-per-turn orbit); the converged dynamical rate is the Phase-1
   vector-TLM deliverable (`…prereg_DRAFT.md:37-44`, VERIFIED). The smoke shows
   the *source* exists and is signed; it does not yet show the dynamics realize it.
2. **The reciprocity / medium-frame-observable definition is unsettled.** A single
   independently-found screw axis is **handedness-ambiguous** (srs-R `4_1` and
   srs-L `4_3` orbit-helices share sign — each enantiomorph space group contains
   screws of both senses; the live srs-L `4_3` axis read `+17.941°/unit`, same
   sign as srs-R). The clean SIGNED discriminator is the **reflection-odd writhe /
   the enantiomorph-pair difference**, NOT a single ray. What counts as the
   *observable* helicity (reciprocal vs non-reciprocal, which medium frame) must be
   pinned before the dynamical claim is testable.
3. **Helicity quantization is a Phase-1 measurable, OPEN.** Whether the acquired
   helicity is *quantized* (lands on discrete values set by the screw pitch and
   the winding) or takes a continuum of values is **not** answered by the
   kinematic smoke. It is named as a Phase-1 measurable: report the dynamical
   `Δθ_pol/L` spectrum vs launch parameters and check for plateaus.


## §4 — The lossless formulation

[Grant-ratified / session-record] Grant's challenge: *"lossless or effectively
lossless for our frequency content?"* The honest answer is three-layered — and
the three layers must NOT be collapsed into a single "the vacuum is lossless"
slogan, because they have different epistemic status.

### §4.1 Layer (i) — AXIOM: the bond LC has no R by construction

[identity / constitutive-choice] At the substrate level, the bond is a pure LC
element: it has **no resistance R by construction**. This is a **constitutive
choice**, not a measured fact — the canonical anchor is Axiom-3 `Γ = 0`
(reflectionless, impedance-matched per-channel coupling) + Op17, which the vocab
audit's three-impedance law leans on (`…vocab-operator-unification-audit.md` §4a,
VERIFIED). Because it is a modelling axiom, it is **directly unfalsifiable** — you
cannot measure "the bond has exactly zero R"; you can only **bound** R from above
by observing how little dissipation the medium exhibits. Tagged honestly:
losslessness at this layer is an *input*, not an *output*.

### §4.2 Layer (ii) — MEASURED: effectively lossless in-band / linear-regime, with floors

[consistency-class-numeric] In the linear, in-band regime the medium is
*effectively* lossless to within whatever floor the best external bound sets. The
**floor schema** is: an upper bound on dissipation per cycle → a lower bound on
the medium's quality factor `Q` at the relevant frequency. The candidate external
bounds (each carried as a SCHEMA — the specific numbers are
[external-bound: requires verification] and are NOT asserted here):

| External observable | Floor it sets (schema) | Tag |
|---|---|---|
| electron lifetime bound (`~10^28 yr`-class) `× ω_C` | a `Q` floor for the electron reactor's standing reactive state (`Q ≳` a very large number; the brief's `~10^57` is illustrative of the *class*, not a verified value) | [external-bound: requires verification] |
| cosmological photon propagation (Gyr baselines, no anomalous attenuation/dispersion attributable to the medium) | a per-length absorption floor on the EM-transverse channel | [external-bound: requires verification] |
| GW170817 (GW–EM arrival coincidence over ~`10^8` lyr) | a bound on dispersive/dissipative loss in the shear / bulk channels relative to EM | [external-bound: requires verification] |

> **Discipline note (per the empirical-driver / verify-before-cite rules).** Every
> number in the row above is tagged requires-verification. The electron-lifetime
> `Q ≳ 1e57` figure in particular is **illustrative of the order-of-magnitude
> class**, derived schematically from `lifetime × ω_C`; it is NOT a grepped corpus
> value and must be computed and cited before any use. **No invented values land
> in canon from this layer.** What IS solid: the *schema* (a long-lifetime / long-
> baseline bound translates to a high-`Q` / low-loss floor), and that all three
> point the same way (the medium is very low-loss in-band).

### §4.3 Layer (iii) — REGIME-SCOPED: near-saturation the medium is exchange-active

[consistency-class] Per the regime/phase-state discipline: the losslessness claim
is **linear-regime-scoped**. Near saturation (`A → 1`, Op14 active), the medium
becomes **exchange-active** — energy moves between channels (the cross-sector
trading / latent / upshift behavior). Per port this *looks like loss* (the source
channel loses energy); per the full ledger it is **reactive** (the energy is
stored / re-emitted in another channel, not dissipated to heat). This is the
"loss-LIKE per port, reactive per ledger" distinction — the same one the vocab
audit makes with "reactance as the universe's bookkeeping … in a lossless lattice
the branch-power sum [conserves]" (`…vocab-operator-unification-audit.md:139,176`,
VERIFIED; Grant-ratified ruling anchored at `orbital-friction-paradox.md:35`).

### §4.4 The falsifiable seam

[open-gap] The axiom (Layer i) is unfalsifiable *directly*, but the formulation
as a whole has a **clean falsifiable seam**:

> **Kill condition.** Genuine **in-band, linear-regime dissipation** that **no
> fuller ledger recovers** — i.e. energy that leaves a port and reappears as
> neither another channel's reactive store nor a radiated real-power term, but as
> true irreversible heat — would **kill the lossless axiom.** The escape hatch
> (Layer iii: "it's just exchange, recover it in another channel") is only
> legitimate when the fuller ledger *actually balances*. A measured linear-regime
> loss that survives a complete reactance-pair + cross-sector accounting is a real
> falsification, not a bookkeeping artifact — and must be reported as one
> (flag-don't-fix; do not rescue by inventing a recovery channel).

> **Cross-reference (lands elsewhere).** The reactance-as-bookkeeping ledger, the
> Tellegen-theorem import (VIRGIN in canon, grep=0 — the natural lossless-lattice
> conservation law), and the saturable-core LOOP GAP that this seam depends on are
> developed in the vocab/operator audit, branch `analysis/2026-06-11-vocab-operator-audit`
> (PR #196, in-flight). This document does not restate or upgrade that content; it
> points at it as the ledger that Layer (iii) and the seam rely on.


## §5 — The v10 charter

[charter — adjudication-gated] The v10 build is the **convergence build**: the
first run that asks the lattice to *make* the reactor, not host a planted one.

### §5.1 The convergence build, defined

[charter] v10 is: **a chiral lattice hosting a σ-equipped medium with a
loop-candidate kernel, seeded by a bare linear transverse wave given only a
direction, read interior + phase-resolved, judged against the banked
discriminators.** Concretely:

- **Substrate:** the chiral (enantiomorph-paired) lattice from v9 Phase-0, plus
  the **diamond achiral control** and the **reversed-launch-direction** control,
  and the **`κ_chiral = 0`** geometry-only ablation.
- **Medium:** σ-equipped (Op14 saturation ON, `A → 1` accessible) so the
  exchange-active regime (§4.3) is reachable — with the loop-candidate kernel
  that lets a bound reactive state close on itself.
- **Seed:** a **bare linear (zero-helicity) transverse wave given only a
  direction** — the precursor, not the end-state (the Checkpoint-8 genesis test,
  v9 P6), so handedness must be *acquired* (§3), not planted.
- **Reads:** **interior** (PML-excluded, density-peak `top-K |field|²` sampling,
  reactance-pair `V_inc/ω` AND `Φ_link/ω̇` recorded over the window) and
  **phase-resolved** (the optical-rotation / chirality coordinate, A46 — never
  real-space lattice-Cartesian vs `φ²`).
- **Judged by:** the banked **traveling-vs-standing** discriminator (does a
  standing reactive state form?) + the **genus** discriminator (does a nonzero
  conserved topological charge emerge?), each evaluated against the
  **enantiomorph + cubic(diamond) + reversed-direction** controls.
- **Outcome bins:** the §1.3 ladder — DISPERSES / TRANSIENT / SET-ACHIRAL /
  **CVR-SET** (the pre-committed PASS bin).

### §5.2 The four blocking Grant decisions (verbatim, with options)

[charter — Grant adjudicates before any v10 run]

**Decision 1 — lattice identity.** Is the v9 chiral `srs` net a **(A) deliberate
substrate challenge** to the 2026-06-07 lattice-net resolution-of-record (accept
the explicit α/Lorentz-chain-invalidation cost), or **(B) a decoration-model
diagnostic** (substrate stays the z=4 achiral diamond; `srs` is a probe)? This is
the v9 prereg's §0 adjudication, unresolved.
- *Options:* (A) substrate-challenge · (B) decoration-model · **(recommended:
  decoration-discriminator-first)** — run the chiral net as a *discriminator* on
  the achiral baseline first; only promote to substrate-challenge if the
  discriminator fires. This defers the α/Lorentz-chain cost until there is a
  signal worth paying it for.

**Decision 2 — loop scope.** What loop-candidate kernel does v10 carry?
- *Options:* **(a) σ-only** (Op14 saturation, no rate-gated snap) · **(b) σ +
  rate-gated snap** (add the irreversible snap channel) · **(c) defer** (Phase-1
  vector-TLM consistency first, loop in Phase-2). Trade: (b) is the only one that
  can show genesis-with-irreversibility, but it reopens the loss/ledger seam (§4.4)
  and needs the reactance-pair accounting armed to tell exchange from dissipation.

**Decision 3 — Phase-1 freeze items + helicity amendments.** Which items freeze
into the v9 Phase-1 pre-registration (currently DRAFT)?
- *Options / items:* the `⟨bracketed⟩` thresholds (P2 enantiomorph `|sum|`, P2
  diamond `≤5%`, P4 `κ_chiral=0` collapse, the BIN-G/T/D boundaries); **plus the
  helicity-as-acquired amendments** now staged into the prereg's
  §FREEZE-AMENDMENT-QUEUE (P6 seed = plain linear packet / zero injected helicity /
  direction only; new reversed-launch-direction control → sign flip; P4 strengthened
  = no helicity-odd term anywhere in the drive chain; CVR-SET as the P6 PASS bin
  name). Grant freezes or revises these.

**Decision 4 — `chi_shock` (the dissipation / saturation-ride knob), anchor `:359`.**
Does v10 carry the dark-sector dissipation treatment, and at what setting?
- *Referents (both flagged — not silently merged):* `chi_shock` = the
  sonic-horizon dissipation fraction knob (`sonic_horizon_flow.py:52`, default
  `1.0`, apparatus-swept) — the one-way KE-removal model; and **`:359`** =
  `research/2026-06-11_dark-sector-response-characterization.md:359`, the
  `H_shear / H_EM / H_bulk` per-channel saturation transfer-function row. Decision:
  whether v10's σ-equipped medium uses the saturation-ride transfer functions
  and/or any nonzero `chi_shock`, or runs `chi_shock = 0` (elastic, fully
  reversible — the cleanest control for the §4.4 loss seam).
- *Options:* (a) `chi_shock = 0`, transfer-functions ON (reversible exchange,
  loss seam clean) · (b) `chi_shock > 0` swept (irreversibility opt-in, tests the
  seam) · (c) defer the dark-sector coupling entirely to a later build.

> The `:359` ↔ `chi_shock` pairing is reproduced as Grant labeled it; the two
> referents are distinct objects (a transfer-function row vs a dissipation knob)
> and are flagged as such rather than collapsed.

### §5.3 Sequencing

[charter] The pre-committed order:

1. **Audit** — close the vocab/operator audit (PR #196) so the registry-v2 rows,
   the three-impedance law, and the reactance ledger are landed before v10 leans
   on them.
2. **Discriminator + the two paper-cheap preregs** (run before the expensive
   build, per parallel-pressure-test discipline):
   - **`E_boundary = α·mc²` check** — does the boundary/binding energy of any
     formed state equal the electron orbital's reactive-shell energy `m_e c² · α`
     (`orbital-friction-paradox.md:~35`, VERIFIED: "Electron orbital … `m_e c² ·
     α` … Quantized reactive shell")? A cheap consistency screen on the reactive
     ledger. [consistency-class — to be pre-registered]
   - **Layer-8** — the named paper-cheap prereg item from the session (the
     eighth-layer check). [session-record — carried as a named item; its exact
     content freezes with Grant's Decision 3.]
3. **The four calls** (§5.2) — Grant adjudicates.
4. **v10** — build and run only after 1–3.

> **CVR-SET is the pre-committed PASS-bin name** for the v10 outcome (§1.3),
> frozen *before* any run, with the DISPERSES / TRANSIENT / SET-ACHIRAL failure
> ladder. P5-pass + DISPERSES = hosting-but-no-genesis and MUST NOT be reported as
> CVR-SET (the Checkpoint-8 / Rule-11 honest-closure binding).

---

## Lane note

Implementer-lane output. This document **records** Grant-ratified naming and
framing decisions and **stages** the v10 charter + the four blocking calls; it
adjudicates none of them. The auditor lands any `common/`-leaf or registry
entries; Grant makes the four calls and freezes the v9 Phase-1 pre-registration.
Cross-refs to PR #195 (v9 Phase-0) and PR #196 (vocab/operator audit) point at
in-flight branches and are not restated or upgraded here.
