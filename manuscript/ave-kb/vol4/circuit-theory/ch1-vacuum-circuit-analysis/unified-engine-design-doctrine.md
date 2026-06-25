[↑ Up](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "ARCHITECTURE / ONTOLOGY doctrine for the unified vacuum engine (CONSISTENCY-class — no new physics, no new derived number). Captures the engine-design conclusions worked out 2026-06-24/25 so future engine work stays ON TRACK and knows HOW TO USE the engine. Every load-bearing statement is grounded against an existing file:line or an existing research-doc verdict; the OPEN forks (§ honesty + § open-forks) are flagged-not-closed per flag-don't-fix. Extends `computational-solver-selection.md` (the FDTD-vs-K4 selection matrix) from solver-selection to engine-architecture; referenced from `../../../common/engine-capability-map.md`. Hosts no claim id and mints no number."
-->

## The Unified-Engine Design Doctrine — ontology, scale-invariance, coupling, and what the engine is FOR

> **Class + scope (read first).** This leaf is **CONSISTENCY / ARCHITECTURE-class**. It does **not**
> derive a new number, mint a constant, or advance any chord-DOF. It records the *engine architecture*
> — the ontology the engine implements, the dispatch rule between its continuum and discrete cores, the
> coupling layer, and (the load-bearing part) **what the engine is for and what it must never be asked
> to do.** It extends the FDTD-vs-K4 [`computational-solver-selection.md`](computational-solver-selection.md)
> selection matrix from *which solver* to *the whole engine design*, and it is the design companion to the
> capability map [`../../../common/engine-capability-map.md`](../../../common/engine-capability-map.md)
> (which audits *what each engine carries*; this leaf says *how the converged engine is built and used*).
>
> **The single sentence.** The grid IS the lattice; the lattice is a distributed-reactance chiral-LC
> transmission-line network; linear excitations are its normal-mode WAVES and nonlinear saturation builds
> the soliton CAVITY; and the engine's JOB is to be the microscope **below** the screening scale that
> computes the forward-prediction leaks — **not** to watch the electron form (that is closed-negative).

---

## §A — Ontology: the grid IS the lattice

**The grid is not a discretization of a continuum — it IS the physical lattice at $\ell_{node}$.**
The physical vacuum is a *chiral Laves K4 Cosserat crystal* of nodes at pitch $\ell_{node}$
([`../../../../common_equations/eq_axiom_1.tex`](../../../../common_equations/eq_axiom_1.tex):26).
The engine's computational grid is the *same object*, not a numerical stand-in for a smooth field. This
inverts the usual FDTD reading (where the grid is a convenience that converges to a continuum truth as
$\Delta x \to 0$):

- **The lattice is NON-refinable.** $\ell_{node}=\hbar/(m_ec)$ is the physical node spacing, not a mesh
  parameter. There is no sub-$\ell_{node}$ physics to resolve — the lattice has no internal structure
  below its own nodes. **Sub-$\ell_{node}$ refinement is forbidden** (it would invent degrees of freedom
  the substrate does not carry). This is the Nyquist limit as a *physical* statement, not a numerical one.
- **The continuum is the coarse-grain-UP limit, not a refine-down convenience.** "Continuous" means the
  macroscopic effective theory you get by averaging the lattice over many cells — the direction is *up*
  (toward longer wavelengths), never *down* (toward sub-node structure). Classical mechanics and network
  dynamics are macroscopic effective theories of the substrate's bulk dynamics, not fundamental primitives
  ([`eq_axiom_1.tex`](../../../../common_equations/eq_axiom_1.tex):40).

**The lattice is a distributed-reactance chiral-LC transmission-line network.** Each node is a native LC
oscillator: three translational DOF couple capacitively ($\varepsilon_0$, the E-field), three
microrotational DOF couple inductively ($\mu_0$, the B-field) — the same structural reality described in
mechanical (Cosserat micropolar) and electromagnetic (LC resonant) terms
([`eq_axiom_1.tex`](../../../../common_equations/eq_axiom_1.tex):26). The engine therefore has:

- a **FIXED graph** — the K4 connectivity (the topology of who is wired to whom), which never changes
  during cold-lattice operation; and
- a **DYNAMIC constitutive law** $S(A)$ — the per-node saturation kernel $S(A)=\sqrt{1-A^2}$ that modulates
  the cell reactances with the local excitation amplitude $A$. The graph is the wiring diagram; $S(A)$ is
  the varactor/saturable-inductor on every cell.

**Rigid-grid Eulerian until rupture.** The engine field lives *on* fixed nodes — it is field-on-a-lattice
(Eulerian), **not** a moving substance (Lagrangian). The nodes do not flow; the excitation does. The only
exception is the **ruptured-plasma phase** (Axiom 4 Regime IV — BH interiors, pre-crystallization cosmos):
there the K4 topology is destroyed and long-range order is lost
([`eq_axiom_1.tex`](../../../../common_equations/eq_axiom_1.tex):32). The phase transition between the
crystallized and ruptured states IS the A-034 universal strain-snap, occurring identically at every scale
([`eq_axiom_1.tex`](../../../../common_equations/eq_axiom_1.tex):34). Genesis (node birth / pair production)
is likewise a topology-changing event, outside the rigid-Eulerian regime — and is deferred (see §I).

## §B — Scale-invariance: the reactance does not renormalize with resolution

**$Z_0$ and $c_0$ are scale-invariant because $\ell_{node}$ cancels.** The per-cell lumped elements are
$L_{cell}=\mu_0\,\ell_{node}$ and $C_{cell}=\varepsilon_0\,\ell_{node}$, so the cell impedance

$$
Z_{cell}=\sqrt{\frac{L_{cell}}{C_{cell}}}=\sqrt{\frac{\mu_0\,\ell_{node}}{\varepsilon_0\,\ell_{node}}}
=\sqrt{\frac{\mu_0}{\varepsilon_0}}\equiv Z_0\approx376.73\;\Omega
$$

— **the lattice pitch cancels identically** ([`z0-derivation.md`](z0-derivation.md):37,40). Every cell, at
every location, presents the same $Z_0$; this is the lattice's *node-to-node impedance ratio*, a property
independent of the absolute scale $\ell_{node}$. This is the corpus "self-similar at every scale" property
(`clm-zuf7g1`, dual-axis classification: **Class-2 substrate-mechanism emergence on the scale-invariance
sub-axis** — the K4 topology forces $L_{cell}\propto\ell_{node}$ and $C_{cell}\propto\ell_{node}$, producing
the pitch cancellation; the *numerical value* 376.73 Ω is Class-B manifestation via SI substitution of
$\mu_0/\varepsilon_0$, not a substrate-derived number — see [`claims.jsonl`](../../../.index/claims.jsonl)
`clm-zuf7g1` rationale).

**Consequence for the engine: the reactance does NOT renormalize with resolution.** Because $Z_0=\sqrt{\mu_0/\varepsilon_0}$
holds *independent of $\ell_{node}$*, the physics the engine carries (the impedance, the wave speed, the
reflection coefficients) is invariant under a change of cell size. Therefore:

- **$\Delta x$ is a NUMERICAL-convergence knob, not a physics-renormalization knob.** Refining $\Delta x$
  must *reproduce* the scale-invariant physics (it is a convergence test — does the discretization recover
  $c_0,Z_0$?), it must never *change* the physics. A correctly-built engine returns the same $c_0$ and $Z_0$
  at $\Delta x=\ell_{node}$ and at $\Delta x=2\ell_{node}$; if the answer drifts with $\Delta x$, that is a
  numerical bug, not a physical renormalization.
- This is the **validate-on-known** gate in operational form: the small-$|k|$ acoustic branch of the K4
  Bloch matrix recovers $\omega=c_0|k|$ to rel-err $\sim2\times10^{-16}$ and $Z_0$ to rel-err 0
  ([`../../falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md`](../../falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md):59-63) —
  the $\ell_{node}$ cancellation is the *check*, NOT an emergence claim.

> **🔴 CORRECTION CAPTURED (this session, 2026-06-24/25; consistency-class, no body to retract elsewhere).**
> An earlier framing held that the cell reactances "renormalize with resolution" — i.e. that
> $L_{eff}(\Delta x)$ / $C_{eff}(\Delta x)$ must be re-scaled as the grid is refined to keep the physics
> fixed. **That framing was WRONG.** $L_{cell}/C_{cell}=\mu_0/\varepsilon_0$ is scale-invariant *by
> construction* — the $\ell_{node}$ cancels in the ratio. There is no reactance renormalization-group flow
> with $\Delta x$: the reactance is fixed by the constitutive constants $\mu_0,\varepsilon_0$ and the local
> $S(A)$, period. The only $\Delta x$-dependence a correct engine shows is *numerical convergence to the
> scale-invariant answer*. (Where genuine $\Delta x$-physics DOES appear is the band edge — see §D — but
> that is dispersion *signal*, set by $q\cdot\ell_{node}$, not a renormalization of the reactance.)

## §C — Coupling architecture: linear WAVES, nonlinear CAVITY, integer winding

The engine has exactly two regimes, separated by the saturation kernel $S(A)$:

**(1) Linear → WAVES (the network's normal modes, CONTINUOUS).** Below saturation, $S(A)\approx1$, the
constitutive law is linear, and the lattice is an ordinary (chiral) LC transmission-line network. Its
excitations are *normal modes* — the four substrate resonance categories, each a wave in its own impedance
channel:

| Category | Channel | DOF | Carrier |
|---|---|---|---|
| **EM-transverse** | $Z_{EM}\equiv Z_0$ ($\Gamma_{EM}=0$, matched/radiative) | T2 transverse field | the photon |
| **shear** | $Z_{shear}=\rho_{bulk}c_{shear}$ | deviatoric $G$ | shear wave |
| **bulk** | $Z_{bulk}=\sqrt2\,\rho_{bulk}c_0$ at $K=2G$ | A1 dilatation | longitudinal/bulk wave |
| **micro-rotation** | (Cosserat $\mu$-sector) | Cosserat $(2,3)$ wryness | rotational wave |

(grade map and channel impedances per [`resonant-lc-solitons.md`](resonant-lc-solitons.md):118-120). These
are *continuous* — they live in the coarse-grain-up regime, are dispersionless at long wavelength
($\omega=c|k|$), and are what the continuum PDE core computes cheaply and exactly (§D).

**(2) Nonlinear / saturated → the soliton A1-CAVITY (mass, DISCRETE).** As $A\to1$ the kernel $S(A)\to0$
turns the linear modes nonlinear: the bulk channel's $Z_{bulk}\to0$ drives a $\Gamma\to-1$ confinement
wall, and a localized standing mode forms — the A1 dilatation breather, the work-doing $C\leftrightarrow L$
store that recovers $E=m_ec^2$ ([`resonant-lc-solitons.md`](resonant-lc-solitons.md):17-23). This is the
*rest-mass cavity*. It is localized by the saturation wall (the $\Gamma=-1$ boundary), **not** by an
autonomous bulk self-focusing well — the bulk self-trap is a ruled-out Cartesian artifact (§H, and the
Stage-2 MODE-III result, [`../../../../../research/2026-06-24_engine-stage2-native-cage_result.md`](../../../../../research/2026-06-24_engine-stage2-native-cage_result.md)).

**$S(A)$ is the ONLY nonlinear coupling — and it is the value-selector.** Every nonlinearity in the engine
flows through the single kernel $S(A)=\sqrt{1-A^2}$: it is the saturable constitutive law on every cell, the
mechanism that turns waves into the cavity, and the *only* place where the engine selects a value (where the
wall sits, where $\Gamma=-1$ forms). Structurally, $S(A)$'s saturation boundary $|\Gamma|=1$ (the wall where
mass forms) IS the **biquaternion null cone** (§F) — the algebraic re-expression of the one place the linear
network goes nonlinear. There is no second nonlinear coupling hiding elsewhere.

**The winding (charge) is an ALWAYS-INTEGER topological label — separate from amplitude.** The electron is
**two-natured** (Grant-ratified, [`../../../../../research/2026-06-24_engine-reroute-epic-summary.md`](../../../../../research/2026-06-24_engine-reroute-epic-summary.md):5):
the DYNAMICAL energy-bound MASS (the A1 cavity above, which does work) **plus** a STATIC topological CHARGE
— the Cosserat $(2,3)$ micro-rotation winding, a deformation-invariant boundary linking integer
$\mathrm{Link}(\partial\Omega,F)\in\mathbb{Z}$ (`charge_quantization.py:258`). **Preserve the two-natured
split:**

- the **charge is NOT a high-amplitude wave** — it is an integer topological Link label, invariant under
  continuous deformation (it jumps only on unwind), and is **never wired into the breather's
  $(V_{inc},V_{ref})$ phasor** (the genesis-24 no-phasor-wire guard,
  [`../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20).
  Wiring the winding into the A1 amplitude phasor is the genesis-24 double-count and is barred.
- the dynamical orbit-winding of the *coupled* system reads the **LC oscillator carrier ratio** (proven by
  carrier-ratio detuning, #59/#417), which is a *distinct* object from the static topological charge — do
  not conflate the carrier integer with the charge integer
  ([`resonant-lc-solitons.md`](resonant-lc-solitons.md):124).

So: amplitude lives on the A1 cavity (continuous, dynamical, does work); the integer winding rides the cavity
as a static reactive boundary (lossless, no work). Two natures, two sectors, orthogonal ($A1\perp T2$).

## §D — Continuum-vs-discrete dispatch

The engine carries **two cores** and dispatches between them by regime. This is the engine-architecture
generalization of the FDTD-vs-K4 *solver* selection in
[`computational-solver-selection.md`](computational-solver-selection.md): that matrix chooses a solver by
*observable*; this rule chooses a *core* by *physical regime*.

**Use the CONTINUUM PDE core for the linear, long-wavelength regime.** When $q\cdot\ell_{node}\ll1$ and
$A\ll1$ (sub-saturation), the lattice is its coarse-grain-up limit: the dispersionless LC ladder with
$\omega=c_0|k|$, $Z_0=\sqrt{\mu_0/\varepsilon_0}$ EXACTLY ($\ell_{node}$ cancels). This is cheap, $O(N)$,
and the place to compute photons, achromatic lensing, S-parameters, energy/impedance. The continuum core is
**validated-on-known here, not ground-truth** — $c_0/Z_0$ recovery is the *check that the discretization is
correct*, never an emergence result.

**Use the DISCRETE lattice core ONLY in two regimes:**

1. **The band edge** — when $q\cdot\ell_{node}\to1$, the lattice's discreteness becomes physical *signal*.
   The continuum PDE is blind here by construction; the discrete K4 Bloch operator carries the real
   dispersion. The discriminating tell is the **$(q\,\ell_{node})^4$ photon anisotropy** — the diamond-cubic
   bond set's first directional anisotropy is the QUARTIC cubic harmonic
   $\Xi(\hat q)=\hat q_x^4+\hat q_y^4+\hat q_z^4-\tfrac35$, symmetry-protected by the point group
   ([`../../falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md`](../../falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md):8-18).
   This is one of the forward-prediction leaks the engine exists to compute (§G).

   > 🟡 **LOAD-BEARING CAVEAT (carried verbatim from the dispersion leaf, flag-don't-fix).** The slope-4
   > result is **NOT a from-eigensolve derivation of quartic-ness**: the genuine node-up content the
   > eigensolve establishes is the *bond-moment identities* (the 2nd moment is isotropic $=\tfrac43$, the
   > 4th moment is the pure cubic harmonic) and the *matter-vs-photon contrast*. The slope-4 itself is a
   > re-statement of the corpus-canonical weak-C "photon carries no zone-edge $(q\ell)^2$ term" premise; an
   > independent from-scratch eigensolve of the actual $6\times6$ dynamical matrix gives anisotropy slope 2,
   > because the genuine lattice DOES carry the isotropic $O(k^2)$ zone-edge term. The rigorous proof that
   > the continuum limit is exact ($\delta=0$) remains OPEN
   > ([`k4-bloch-dispersion-quartic.md`](../../falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md):92-103).
   > Do not over-state the band-edge result as a clean from-geometry quartic.

2. **The nonlinear / soliton regime** — when $A\to1$ the kernel $S(A)$ goes nonlinear and the cavity forms
   (§C). The continuum long-wavelength approximation breaks (the cavity is $\sim\ell_{node}$-scale), so the
   soliton must be carried on the discrete lattice core. (This is the regime where the Stage-2 native-cage
   test ran — and returned MODE-III DISPERSE on the *native* stencil, §H.)

**"Continuous" ALWAYS means the coarse-grain-UP limit, NEVER sub-$\ell_{node}$ refinement.** The continuum
core is the long-wavelength average of the lattice, reached by going *up* in scale. It is not a finer grid
reached by going *down* below $\ell_{node}$. Refining the continuum PDE below $\ell_{node}$ does not buy
more physics — it invents sub-node structure the substrate does not have (the Nyquist bar, §A and §H).

## §E — Connectivity: chiral z=3 srs vs achiral z=4 diamond

**Decision 1 (RATIFIED, Grant 2026-06-25): the production engine substrate is the chiral z=3 srs net.**
The chiral $z=3$ srs (Sunada / Laves, $I4_132$) net carries the handedness — and handedness is what
distinguishes charge / spin / parity / optical-activity sign-flip. An achiral grid cannot carry these:

- the chiral $z=3$ srs net is the **only** grid that hosts structural handedness, with optical-activity
  facts confirmed signed / enantiomorph-odd / diamond-null / writhe-sourced / lossless-reciprocal
  ([`../../../common/engine-capability-map.md`](../../../common/engine-capability-map.md):48, #195);
- the achiral $z=4$ diamond net is reserved for the **coarse-grained macroscopic** regime, where chirality
  averages out over each computational cell and a Cartesian/diamond discretization introduces no systematic
  error in chirality-blind observables (energy density, ponderomotive force, impedance matching, S-parameters)
  ([`computational-solver-selection.md`](computational-solver-selection.md):17).

So the connectivity dispatch is: **chiral $z=3$ srs whenever handedness is load-bearing (charge / spin /
parity / OA), achiral $z=4$ diamond only for the macroscopic chirality-blind regime.** This is the
connectivity companion to the FDTD-vs-K4 selection matrix (which already routes "chirality is the observable"
to the native chiral grid).

> ⚠ **FLAG-DON'T-FIX — D1 adjudication tension (surfaced, NOT silently resolved).** The Decision-1
> adjudication currently recorded in canon is **older and reads the OPPOSITE WAY** on which net is the
> *production substrate*:
>
> > **[`eq_axiom_1.tex`](../../../../common_equations/eq_axiom_1.tex):37 — verbatim, "D1 adjudication, 2026-06-12":**
> > *"The production computational net is **z=4 diamond** (α, Lorentz suppression, and FDTD/TLM engines). The
> > bare **z=3 srs** (Sunada / Laves) net is a validated **discrete instrument** for structural chirality and
> > optical-activity discrimination (Genesis v9 R3 + Phase-1, test-gated); it is **not** a migration target
> > for the engine substrate."*
>
> The 2026-06-12 .tex text makes z=4 diamond the production substrate and z=3 srs an *instrument only*; this
> doctrine records a **newer Grant ratification (2026-06-25)** that promotes the chiral z=3 srs to the
> production substrate (carrying handedness as charge/spin/parity/OA). These are in direct tension. Per
> flag-don't-fix, this leaf does **not** edit `eq_axiom_1.tex` to match — the canon-propagation of the
> 2026-06-25 ratification into `eq_axiom_1.tex` (and the α / Lorentz chains that the 2026-06-12 text anchored
> to diamond) is an **auditor-lane + Grant adjudication** item, not an implementer silent fix. The doctrine
> states the ratified Decision-1 as its design basis and surfaces the unreconciled .tex with both texts
> verbatim. **Until the .tex is reconciled, treat the diamond-α/Lorentz chains as the open dependency:**
> the 2026-06-12 text justified diamond as production *by* the α + Lorentz-suppression derivations, so
> re-homing to srs must show those chains survive on srs (this is exactly P1 acceptance — see the P1 scope
> doc, and §I).

## §F — Algebra: the biquaternion at the coupling layer

**The biquaternion is the COUPLING-LAYER algebra, not a substrate primitive.** Its place in the engine is
the layer where the channels couple (the A1↔ω port and the saturation wall) — it is *not* the algebra the
cores evolve their fields in. Two properties make it the right language *there*, and exactly one is
genuinely load-bearing:

1. **Chirality is intrinsic.** The biquaternion carries handedness in its own multiplication and its
   pseudoscalar — so the chiral coupling (the srs handedness of §E) is native to the algebra, not bolted on.
2. **The saturation wall $|\Gamma|=1$ IS the null cone (the load-bearing thing).** A real (division-algebra)
   quaternion has no zero divisors; the *bi*quaternion does — its **null cone**. The substrate's
   reflection/saturation boundary ($|\Gamma|=1$, $Z\to\infty$/$\to0$, the $\Gamma=-1$ TIR wall where mass
   forms, §C) is exactly that null cone. This is the one genuinely-illuminating observation — *why*
   biquaternion and not real quaternion — and it is a clean structural re-expression of the canonical
   $\Gamma=-1$ boundary ([`../../../../../research/2026-06-06_biquaternion-node-algebra-result.md`](../../../../../research/2026-06-06_biquaternion-node-algebra-result.md) §0).

**Cores keep separate-field evolution.** The continuum and discrete cores (§D) evolve their A1 / shear /
bulk / micro-rotation fields *separately* — they do not pack the fields into a single biquaternion and step
that. The biquaternion appears only at the coupling ports and the wall. This respects Rule-14 (the algebra
is a coupling-layer facade; it defines no steppers — see §H).

**Canonized-to-nothing AS A PRIMITIVE.** Adjudicated 2026-06-06: the biquaternion is a CONSISTENCY-class
re-expression, **not** the substrate's newly-discovered number system. All three "genuinely-new" gates FAIL
— it does not force closure+longitudinal+Möbius to co-occur as a *new* necessity (they co-occur as standard
math over already-canonical, independently-derived facts), it does not forward-derive
$\alpha^{-1}=4\pi^3+\pi^2+\pi$, and it forces no new testable longitudinal prediction
([`2026-06-06_biquaternion-node-algebra-result.md`](../../../../../research/2026-06-06_biquaternion-node-algebra-result.md) §0,
G1–G3). It re-expresses the already-canonical $Cl(3,0)$ / SU(2) / Cosserat / Hopf / $4\pi$-spinor / $\Gamma$
structure in one algebra. So: **use the biquaternion as the coupling-layer notation (chirality + null cone),
never mint it as a substrate primitive or read a new number off it.**

## §G — Screening: what the engine is FOR

**The lattice is screened from all solitons.** A formed soliton (the electron) sits *below* the lattice's
resolution in every way that matters:

- **sub-Nyquist** — the electron's structure (e.g. the corpus Beltrami tube cross-section
  $\sim\ell_{node}/2\pi\approx0.16\,\ell_{node}$) is below the $\ell_{node}$ node spacing; the lattice
  cannot resolve sub-$\ell_{node}$ structure (§A), so it is structurally blind to the soliton's interior
  ([`../../../../../research/_archive/L3_electron_soliton/92_round_11_vi_v10_finer_sampling_structural.md`](../../../../../research/_archive/L3_electron_soliton/92_round_11_vi_v10_finer_sampling_structural.md) §4);
- **no-hair** — the bound mode is a closed, high-$Q$, $\Gamma=-1$ TIR cavity; with the radiative port shut
  it has no loss channel ($\mathrm{Im}(\omega)=0$, intrinsic $Q\to\infty$), so the lattice sees no leakage
  texture from the soliton's internals ([`resonant-lc-solitons.md`](resonant-lc-solitons.md):100);
- **dodges-sub-cell** — sub-cell internal physics does not couple back into the cell-level dynamics.

So the lattice and the solitons are mutually screened: the engine running cell-level dynamics does **not**
get to watch the soliton's interior, and the soliton's interior does not perturb the cell-level physics.

**The $(q\cdot\ell_{node})^4$ tell is the ONE leak.** The single place the screening is imperfect is the
band-edge dispersion (§D): the lattice's discreteness imprints a $(q\,\ell_{node})^4$ anisotropy on
propagating modes (subject to the §D caveat). That is the one channel where below-the-screening physics
reaches an observable.

**Therefore the engine is the MICROSCOPE below the screening scale — and its JOB is to compute the
forward-prediction leaks.** The AVE-distinct content lives ONLY in forward predictions (all carrying
`experimental_solidity: null`; internally peer-with-SM,
[`../../../../../research/2026-06-24_engine-reroute-epic-summary.md`](../../../../../research/2026-06-24_engine-reroute-epic-summary.md):66).
The engine exists to turn the screening-leaks into bankable numbers — the divergent-from-SM signatures:

- **optical-activity sign-flip** (the chiral-srs enantiomorph-odd OA);
- **$(q\,\ell_{node})^4$ dispersion** (the band-edge tell, §D);
- **vacuum birefringence** (the E-route coefficient $\sim7.5/\alpha^3\approx1.93\times10^7\times$ QED,
  `clm-pp3qwf` — the bankable near-term QED-discriminator);
- **GW-echo** (the lattice's discrete signature in gravitational-wave ring-down).

**What the engine's job is NOT: it is NOT "watch the electron form."** The electron is sub-Nyquist and
screened; self-formation is closed-negative (§H — Stage-2 MODE-III, S3-DISPERSE, #415, #59). Pointing the
engine at "let the electron self-assemble from a free precursor" asks it to resolve the one thing it is
structurally screened from. The engine's value is the *forward leaks*, computed from an *assembled* electron
(or from the linear network directly) — not an emergence movie of the soliton birthing itself.

## §H — Honesty guards: what keeps the engine on track

These are the guards that keep the engine honest. Violating any of them silently converts a clean negative
into a manufactured positive — each is a documented past failure mode.

**1. MEDIUM fully-dynamic; electron ASSEMBLED-not-emergent (self-formation BARRED).** The medium (the linear
network and its DOFs) is fully dynamic and may be evolved freely. The electron, by contrast, is **assembled**
(seeded as an already-localized precursor), **not** grown from a free precursor. Bulk self-formation is
closed-negative across the whole reroute campaign:

- **Stage-2 bulk A1 self-trap → MODE-III DISPERSE** (energy-certified) on the native K4 stencil WITH
  $c_{eff}(V)$ ([`2026-06-24_engine-stage2-native-cage_result.md`](../../../../../research/2026-06-24_engine-stage2-native-cage_result.md):4);
- **S3 winding+$H_{couple}$+cavity pinning → DISPERSE-FALSIFIED**
  ([`2026-06-24_engine-s3-cavity-pinning_result.md`](../../../../../research/2026-06-24_engine-s3-cavity-pinning_result.md):4);
- **#415 coupled eigensolve → gate-(d) FAIL** (winding bled out) and **#59 phase-space orbit → BREAK**
  (reads the carrier-lock $(−5,−5)=(1,1)$, not the topological $(2,3)$)
  ([`2026-06-24_engine-reroute-epic-summary.md`](../../../../../research/2026-06-24_engine-reroute-epic-summary.md):19-20).

Re-running the bulk self-trap as a fresh "maybe it forms this time" is **substitution-not-retraction**
(A47 v11b / Rule 12): the falsified bulk-soliton slot is **not** refilled with a new unverified hypothesis
([`2026-06-24_engine-stage2-native-cage_result.md`](../../../../../research/2026-06-24_engine-stage2-native-cage_result.md):
"Anti-substitution discipline"). If a new formation mechanism is to be tried, it gets a new version number
and its own verification chain — it does not silently re-occupy the closed slot.

**2. The closed-box energy gate MUST be LIVE.** Every soliton/cavity test runs closed-box with NO PML and
NO damping on the verdict path, and the energy-conservation gate must *trip* on its negative controls or the
PASS is vacuous:

- **GX3** — the backward-Euler dissipative *negative control* must DO bleed energy (>5%) on the same
  lossless cage, proving the energy gate (GX2) is live, not vacuous
  ([`2026-06-24_engine-stage2-native-cage_result.md`](../../../../../research/2026-06-24_engine-stage2-native-cage_result.md):105,179);
- **GX5** — the radiative-port-is-passive regression guards the **PML sponge-injection** artifact (the
  explicit run's post-solve sponge-MULTIPLY PML *injected* energy — a 142× gain at fine $dt$, physically
  impossible for a passive absorber — manufacturing a spurious self-focus)
  ([`2026-06-24_engine-stage2-native-cage_result.md`](../../../../../research/2026-06-24_engine-stage2-native-cage_result.md):181,
  §4).

**Pump-detonation / damping-bought localization is THE documented failure mode.** The explicit predecessor
run's apparent self-focus was *both* a CFL pump-detonation AND PML energy-injection combined — not physics.
A "localization" that only appears once you add a sponge, a damper, or let the stepper detonate is the
artifact the energy gate exists to catch. **No PML/damping on the verdict path; the energy controls must
trip.**

**3. Don't anti-alias; don't refine below $\ell_{node}$.** The Nyquist limit is *physical* (§A): there is no
sub-$\ell_{node}$ signal to recover, so anti-aliasing toward a finer grid invents structure the substrate
lacks. The band-edge dispersion (the $(q\,\ell_{node})^4$ tell, §D) is **signal, not error** — do not
"smooth it out" as a discretization artifact; it is the one screening-leak the engine exists to compute (§G).

**4. α-clean verdict path.** No baked α (no ALPHA / Q_TANK / V_SNAP / κ-chiral) may reach the
verdict-determining computation. The reroute campaign's import-time guard triad blocks these and reads pure
`arg()`; Q=137 stays EMPTY ([`2026-06-24_engine-phase-space-winding_result.md`](../../../../../research/2026-06-24_engine-phase-space-winding_result.md):30,104).
A null that depends on `ave.core.constants` for its verdict is not a clean null (consistency-vs-emergence).

**5. Rule-14 — reuse certified cores; the facade defines no steppers/stencils.** New engine work reuses the
already-certified cores (`coupled_cage_winding._assemble_H()`, the conservative evolver, the seed builders),
and the unified-engine *facade* defines **no** new stepper or stencil — it dispatches to the certified cores
([`2026-06-24_engine-coupled-eigensolve_prereg.md`](../../../../../research/2026-06-24_engine-coupled-eigensolve_prereg.md):13,
[`2026-06-24_engine-phase-space-winding_prereg.md`](../../../../../research/2026-06-24_engine-phase-space-winding_prereg.md):14).
Re-deriving a stepper inside the facade re-opens every bug the core's certification closed.

**6. Native chiral-srs stencil — NOT Cartesian-on-a-parity-mask.** Any operator on the chiral grid must use
the substrate-native srs stencil (the rank-2 bond tensor), **not** a Cartesian Laplacian masked to a parity
sublattice. A Cartesian-on-parity-mask stencil fakes an $O(k^2)$ anisotropy and validates a disabled-flag
discretization bug as physics (the wpqwmrms0 bug class, the RANK-2 lesson at
[`k4-bloch-dispersion-quartic.md`](../../falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md):54-56).

**7. Validate-on-known FIRST.** Before any chord measurement, the engine must recover $c_0/Z_0$ at long
wavelength — and that recovery is the **CHECK that the discretization is correct, NOT the ground truth**
(§B, §D). $c_0/Z_0$ recovery is validate-on-known; it is never headlined as emergence. If the validate-on-known
gate fails, the engine is wrong and HALTs before any chord is read.

## §I — Open forks: flagged, NOT closed

<!-- SECTION I PLACEHOLDER -->

---

## Cross-references

<!-- XREF PLACEHOLDER -->
