# The Electron as an Interstitial Rotor — a session synthesis

**Date:** 2026-06-07
**Lane:** implementer (research-doc + two formal derivations from canonical inputs)
**Branch:** `analysis/2026-06-07-electron-rotor-synthesis` (off `origin/main` @ `d3065c1c`)
**Status:** scaffold — sections filled one-per-commit (incremental-write discipline).

---

## 0. Scope, framing, and honest classification

This document is **consistency-class SYNTHESIS**. It introduces **no new physics
primitive**. It ties together canonical corpus pieces about the electron's
structure and adds **two formal derivations whose every input is already
canonical** (§4 rotor = zitterbewegung = Compton clock; §5 helicity stabilizes
the unknot). Per `consistency-vs-emergence` Step 8c, because the work adds no
new substrate primitive (no new axiom invocation, no new substrate primitive, no
new cross-volume bridge that the sources don't already carry, no new
experimental discriminator), **its classification stays at the ceiling of its
canonical sources.** The nearest-kin canonical leaf — `historical-precedents.md`
— self-classifies as *"Consistency-class (no new substrate primitive) … this
leaf does not promote past it"* (`historical-precedents.md:39`, the "echo, not
chord" ceiling). This synthesis inherits that ceiling. The two derivations are
**identity / consistency**, NOT emergence: they reproduce results the corpus (or
standard physics) already carries, via the rotor picture; they are not new
single-observable predictions.

### Skills fired (and where)

- `ave-prereg` — corpus is largely canonical; this is a CITE-don't-re-derive
  synthesis. Corpus-grep done across the KB + engine + research/ + orchestration
  before drafting; prior work enumerated in §§1–7 cross-refs.
- `ave-canonical-leaf-pull` — leaves enumerated below (§ Cross-references).
- `ave-ee-first-mapping` — the E/B ↔ LC-ladder vocabulary is the spine (§1, §2);
  EE is substrate-native, not a translation source.
- `substrate-native-check` — CP1 (the substrate runs wave propagation / elastic
  strain, NOT energy minimization), CP2 (sector: V-sector K4-TLM bond vs
  Cos-sector microrotation) walked before the prose-derivations (trigger 6).
- `consistency-vs-emergence` — every claim CLASSIFIED (ledger below). Most are
  Class B/C synthesis; the two derivations are identity/consistency.
- `ave-canonical-source` — constants are cited from `src/ave/core/constants.py`,
  never re-hardcoded.
- `verify-before-cite` — every file:line below was grep/Read-verified. The
  citation-correction ledger (§ Verify-before-cite findings) records four
  task-brief citations that did not resolve as given.
- `ave-evidence-framing-discipline` — strength language kept honest:
  "candidate mechanism", "untested-not-contradicted", "qualitative-canonical /
  quantitative-not-derived" used where the corpus warrants.

### Consistency-vs-emergence ledger

| § | Claim | Class | Basis |
|---|---|---|---|
| §1 | E, B are the two strain projections of one K4-Cosserat elastic state | **B** axiom-manifestation (ontological synthesis) | Restates Axiom 1 (`ave-kb/CLAUDE.md` INVARIANT-S2); 3 forced framings |
| §2 | E↔node shunt-C (`V_inc`); B↔bond series-L (`Φ_link`) | **A/B** identity + manifestation | The engine IS built this way (`k4_tlm.py`); `Γ=−1` = node short |
| §3 | Interstitial Meissner/maglev confinement unifies 4 canonical threads | **C** consistency synthesis | MIT-bag + asym-Meissner kernel + Bingham slipstream + Kelvin |
| §4 | rotor = zitterbewegung = Compton clock (spin & mass one oscillation) | **A** identity / **C** consistency | Reproduces Dirac zitter via the rotor; mc²=ℏω_C=½LI²; NOT new prediction |
| §5 | helicity (spin) stabilizes the `0₁` unknot; H=0 ⇒ dissolves | **C** consistency + **candidate mechanism** | poincaré `c=0` + Beltrami unknot + Woltjer/Taylor; dissolution is a hypothesis |
| §6 | charge sign from cosmic-frame (`Ω_freeze`) chirality | **C** consistency / cite-canonical + rotor framing | Qualitative chain canonical; quantitative coupling NOT derived |
| §7 | engine/genesis consequences + open-derivation queue | meta / forward-scoping | Reframes genesis Forks A/B/C/D; no class |

### Verify-before-cite findings (citation-correction ledger)

Four task-brief citations did not resolve as written; corrected here per
`verify-before-cite`. Recorded, not silently fixed (flag-don't-fix).

| Brief citation | Finding | Corrected citation |
|---|---|---|
| Axiom 1 "(CLAUDE.md: …)" | Root `CLAUDE.md` has no such text | `manuscript/ave-kb/CLAUDE.md` **INVARIANT-S2** (verbatim "3 translational → E, 3 microrotational → B") |
| MIT-Bag/dual-Meissner `Vol 4 Ch 1:469-481` | `:469-481` is the **Black-Hole Horizon Mirror** subsection | MIT-bag/flux-tube: `01_vacuum_circuit_analysis.tex:569-587` (KB `resonant-lc-solitons.md:52-54`); **Meissner** particle-core row `:432`; Bingham slipstream `:294-362` |
| MODE-III doc `research/2026-06-06_optionD-impose-under-reflective-confinement-result.md` | **Not committed on any git ref**; referenced only in `_orchestration/2026-06-06_genesis-next-steps-scope.md:62` (§8-C2). Cannot cite as corpus | cite the orchestration §8-C2 finding instead; flag the missing artifact |
| genesis "Forks A/B" | Actual doc enumerates **Forks A/B/C/D** in §9 | A = amplitude/calibration crux ("the genesis blocker"); B = polarity; C = scale; D = C3 phase-coherence |

---

## §1 — Strain ontology: E and B are not fundamental

**Claim.** The substrate does not store energy "in the electromagnetic field." It
stores energy as **elastic strain of the K4–Cosserat crystal** $\mathcal{M}_A$.
What we call $\mathbf{E}$ and $\mathbf{B}$ are not two independent fundamental
fields; they are the **two — and only two — projections** of that single strain
state. $\mathbf{E}$ is the *translational* projection; $\mathbf{B}$ is the
*microrotational* projection.

**Canonical anchor.** Axiom 1, verbatim (`manuscript/ave-kb/CLAUDE.md`
INVARIANT-S2): the vacuum is *"a 3D chiral Laves K4 Cosserat crystal, with
micropolar nodes (6 DOFs each: **3 translational → E, 3 microrotational → B**;
Cosserat rotational DOF IS the substrate-native origin of intrinsic spin)…
modeled in continuum as a Trace-Reversed Chiral LC Network."* The energy split is
the Axiom-3 node Lagrangian (same source): $\mathcal{L}_{node} =
\tfrac12\varepsilon_0|\partial_t\mathbf{A}_n|^2 -
\tfrac{1}{2\mu_0}|\nabla\times\mathbf{A}_n|^2$ — the first (capacitive) term is
the $\mathbf{E}$ / translational store, the second (inductive) term is the
$\mathbf{B}$ / microrotational store. In Cosserat field variables this reads
$\mathbf{E}=\partial_t\mathbf{u}$ (translational displacement rate) and
$\mathbf{B}=\nabla\times\boldsymbol{\omega}$ (curl of the microrotation): the
two strain channels, nothing else.

**Why exactly two — three independent forcings converge.** The "E and B are
projections, not primitives" claim is not one argument dressed three ways; it is
three *independent* closures landing on the same 2-channel answer:

1. **Reactive (EE / LC).** In any LC system, energy is *always* cycling between
   the capacitor (electric store) and the inductor (magnetic store). There is no
   third reactive element. Axiom 3's "lossless reactive cycling" (INVARIANT-S2)
   *is* this: the substrate is a network of LC tanks, and at resonance
   $X_L=-X_C$ exactly, so the energy ledger has precisely two reactive halves.
   `src/ave/core/constants.py:757-796` (the dual-reactance count, Grant-adjudicated
   2026-06-01) states it directly: *"3 translational-E DOF → capacitive $X_C$
   (dielectric storage); 3 microrotational-B DOF → inductive $X_L$ (inductive
   flywheel)… the substrate inherits standard LC reactance algebra verbatim,
   Axiom 1."* Two stores ⇒ two fields.

2. **Elastic (Cosserat).** A micropolar (Cosserat) continuum has, by
   construction, exactly two kinds of DOF per material point: translational
   displacement $\mathbf{u}$ (3) and microrotation $\boldsymbol{\omega}$ (3).
   That is the 6 DOF/node of Axiom 1. A K4–Cosserat crystal therefore admits
   exactly two strain sectors and *cannot* carry a third — there is no field
   left over to be "fundamental."

3. **Geometric (Helmholtz).** Any smooth 3D vector field splits uniquely into a
   curl-free (longitudinal) part $\oplus$ a divergence-free (transverse) part.
   The substrate strain field, being a 3D field, must obey this. The
   translational-rate ($\mathbf{E}$) and microrotational-curl ($\mathbf{B}$)
   projections are the substrate's realization of that split — the longitudinal/
   transverse decomposition is not imposed, it is the only decomposition a 3D
   field admits.

**Substrate-native check (CP1).** This is the ontological reason the engine runs
**wave propagation / reactive strain cycling**, not energy-functional
minimization: there is no scalar potential being descended — there is strain
being elastically stored and reactively traded between the translational and
microrotational channels. Reaching for "minimize $W$" here is the SM/continuum
default the substrate-walk exists to catch.

**Classification.** Class **B** axiom-manifestation / ontological synthesis. This
restates Axiom 1; it adds no primitive. The contribution is the *three-forcings*
framing (reactive ∧ elastic ∧ geometric all give 2 channels), which is an
intuition aid, not a derivation.

## §2 — The EE map: E ↔ nodes (shunt C), B ↔ bonds (series L)

§1 said the substrate has two strain channels. §2 says *where they live* in the
lattice, and that the engine is already built exactly this way. This is the
spine: the LC-ladder topology.

**The ladder.** A TLM / LC-ladder has a fixed topology: **shunt capacitors to
ground at each node, series inductors on each bond between nodes.** Voltage
develops across the shunt-C *at* the node; current/flux flows through the
series-L *along* the bond. Mapping §1's two channels onto this:

- $\mathbf{E}$ (voltage, translational) **charges the shunt capacitance AT the
  node.** The engine's node voltage is `V_inc` — a per-node array
  (`src/ave/core/k4_tlm.py:192`, indexed `[nx,ny,nz,4]`: node × 4 K4 ports). The
  local strain is read straight off it: $A=|V_{inc}|/V_{SNAP}$
  (`k4_tlm.py:264`). E lives at nodes.
- $\mathbf{B}$ (current/flux, microrotational) **threads the series inductance ON
  the bond, between nodes.** The engine's bond flux is `Φ_link`, the *per-bond
  magnetic flux linkage* $\Phi_{link}=\int V_{bond}\,dt$ (`k4_tlm.py:206`),
  accumulated each step as $\Phi_{link}{+}{=}V_{avg}\,dt$ with
  $V_{avg}=\tfrac12(V_{ref,A}+V_{ref,B})$ (`k4_tlm.py:371,386`). B lives on bonds.

This is not an analogy bolted on after the fact — it is the data layout of the
canonical K4-TLM engine. The EE-first mapping table makes it canonical:
*"Translational E DOFs at node → Capacitor; Microrotational B DOFs at node →
Inductive flywheel; Bond connecting nodes → Distributed transmission-line
element"* (`ave-ee-first-mapping` §4, mirrored from
`common/translation-tables/translation-circuit.md`).

**Three consequences fall straight out.**

1. **Charge = E-termination on a node.** Charge is where the translational
   ($\mathbf{E}$) strain *terminates* — a node where the shunt-C carries a net
   capacitive termination of E-flux. This is the EE reading of Axiom 2 (charge =
   geometric dislocation, $\xi_{topo}=e/\ell_{node}$): a charge is a node where
   E-flux ends. Charge is a **node / capacitive** property.

2. **Mass = $\tfrac12 L I^2$ of the bond-loop.** Mass is the *inductive*
   (magnetic) energy of the current circulating the closed bond-loop. Verbatim
   from `resonant-lc-solitons.md:17-23`: $E_{mag}=\tfrac12
   L_e I_{max}^2=\tfrac12 m_ec^2$, and Virial balance gives $E_{total}=m_ec^2$.
   That is the bond/inductive face of the Mass-Closure Theorem $mc^2=E_{reactive}$
   (`vol2/claim-quality.md:1199`). Mass is a **bond / inductive** property. (Charge
   on the node, mass on the bond — already the dual-reactance split that §3 and §4
   make load-bearing.)

3. **The $\Gamma=-1$ wall = node capacitor $C_{eff}\to\infty$ short.** As the
   node strain $\Delta\phi\to\alpha$ (Axiom-4 saturation), the node shunt-C
   diverges: $C_{eff}=C_0/\sqrt{1-(\Delta\phi/\alpha)^2}\to\infty$
   (`resonant-lc-solitons.md:32`). Then $Z_{core}=\sqrt{\mu_0/C_{eff}}\to 0\,\Omega$
   (`:38`), and $\Gamma=(0-Z_0)/(0+Z_0)=-1$ — a Perfect Short-Circuit Boundary
   (`:45-48`). The confining mirror is a **saturated node shorting to 0 Ω**.

**Polarity flag (load-bearing; resolved in §3).** Consequence 3 is the
*capacitive* reading of the wall (node $C_{eff}\to\infty\Rightarrow Z\to0$). But
the live engine reaches $Z\to0$ via the *magnetic* branch — the asymmetric
Meissner kernel $Z_{eff}=Z_0\sqrt{S_\mu/S_\varepsilon}\to0$ as $S_\mu\to0$
(`k4_cosserat_coupling.py:364,368`), and the genesis audit (`…genesis-next-steps-scope.md:71-74`,
C4) notes the engine's *symmetric* default $z_{local}=Z_0/\sqrt{S}\to\infty$ is
the **inverse** (open) polarity. Two reactive routes to the same $\Gamma=-1$:
$C\to\infty$ (capacitive, node) vs $\mu\to0$ (inductive/magnetic, Meissner).
They are the two halves of the dual reactance — §3 resolves which one cages the
mass.

**Classification.** Class **A** identity + **B** manifestation. The node-C /
bond-L assignment IS how the engine is constructed; the three consequences are
restatements of canonical results (`resonant-lc-solitons.md`,
`vol2/claim-quality.md:1199`). No new primitive.

## §3 — Interstitial Meissner / maglev confinement

**The picture in one sentence.** A saturated node has $Z\to0$ — it is a local
superconductor — so it **expels B (Meissner)**; the expelled B-vortex "bag"
floats in the **interstitial** pocket between nodes, **frictionlessly** (the
above-yield slipstream is a zero-drag fluid), and **self-cages** (its own B
saturates the surrounding nodes, weaving the very walls that hold it). The
electron is a B-vortex levitating in a magnetic Meissner cage of its own making.

This is not a new mechanism. It is the **single picture that four independent
canonical threads were each describing from one side.**

**Thread 1 — MIT-Bag / dual-Meissner flux-tube confinement.** The $\Gamma=-1$
TIR wall is the bag wall. `resonant-lc-solitons.md:52-54` exposes the MIT Bag
Model as *"a macroscopic impedance wall woven natively by the non-linear
varactor limits of the continuous vacuum"* (LaTeX `01_vacuum_circuit_analysis.tex:569-587`).
The impedance-regime table (`…tex:432`) gives the particle-core row verbatim:
*Particle core ($\Delta\phi\to\alpha$) | $\mu_{eff}\to0$ **(Meissner)** |
$\varepsilon_{eff}\to0$ (dielectric collapse) | $Z\to0\,\Omega$ | $\Gamma=-1$*,
and the surrounding text (`:438`) contrasts it with gravity: gravity scales
$\mu,\varepsilon$ *symmetrically* ($Z_0$ preserved, transparent), while
*"topological saturation (particles, event horizons) drives both to zero
**asymmetrically** via Axiom 4… creating perfect mirrors ($\Gamma=-1$)."* The
"dual" in dual-Meissner is the framework's own: the *particle* expels B where
*gravity* does not.

**Thread 2 — the asymmetric-Meissner kernel (the engine's live wall).** The
mechanism Thread 1 names is *coded and live by default*. The coupled engine uses
$Z_{eff}/Z_0=\sqrt{S_\mu/S_\varepsilon}$ (`k4_cosserat_coupling.py:364`; code at
`:390-393`), and the docstring states the limit explicitly: *"Asymmetric (chiral
drive): $Z_{eff}\to0$ as $S_\mu\to0$ (Meissner…)"* (`:368`), producing the
*"Meissner-like confinement wall where $S_\mu\to0$ with $S_\varepsilon$ finite"*
(`:139-140`). The genesis audit confirms it runs by default and that MODE-III ran
on it: `use_asymmetric_saturation=True` (`…genesis-next-steps-scope.md:58`, C1).

**Thread 3 — the Bingham-plastic frictionless slipstream (the maglev).** Below
$V_{yield}$ the vacuum is a rigid high-drag solid ($\eta_0>0$); above it, the
*Zero-Impedance Slipstream* ($\eta_{eff}=0$, frictionless) — the TVS-Zener
solid→slipstream transition (`01_vacuum_circuit_analysis.tex:294-362`). The
`PairNucleationGate` docstring (`vacuum_engine.py:1179-1191`) assembles the
capsule: *"when both endpoints of an A→B bond reach **Meissner saturation**
($A^2_\mu\ge1$), the local material is punched past yield into the slipstream
regime. $\Gamma\to-1$ walls form at each endpoint… A **Bingham-plastic capsule**
is formed: flowing-slipstream interior, rigid-solid exterior, $\Gamma=-1$ walls
at A and B."* The B-vortex floats in the zero-drag interior — that is the maglev:
levitated and frictionless because the surrounding saturated nodes both expel it
(Meissner) and present it no drag (slipstream).

**Thread 4 — Kelvin topological protection.** Inside that frictionless capsule,
Kelvin's 1867 theorem applies: in a perfect incompressible frictionless fluid a
knotted vortex is topologically protected — it *cannot untie*. The docstring
quotes it (`vacuum_engine.py:1191-1195`, Kelvin 1867). `historical-precedents.md:23-30`
situates the thread: Kelvin's vortex-atom + Helmholtz's frozen-in vortex lines,
with AVE supplying the **two ingredients the ideal fluid lacked** — the topology
(the $(2,q)$ classification) and the length scale $\ell_{node}$ — and the
*saturable crystal* supplying the confinement (verdict-II, 2026-06-06: the
$\Gamma=-1$ boundary converts collapse → confinement; *"the '2' Cosserat winding
forms, and charge=helicity confirms"*).

**Polarity resolution (resolves the §2 flag) — the dual reactance $V=2$.** §2
left two routes to $\Gamma=-1$: capacitive ($C_{eff}\to\infty$, node) vs magnetic
($\mu\to0$, Meissner). They are not competitors — they are the **two halves of
the node's dual reactance** (`src/ave/core/constants.py:757-796`,
`V_TOROIDAL_HALO=2.0`, Grant-adjudicated 2026-06-01): *3 microrotational-B DOF →
inductive $X_L$* and *3 translational-E DOF → capacitive $X_C$*. The assignment
is then clean:

- **Mass-confinement = MAGNETIC Meissner.** The bag that holds the mass (the
  B-vortex, §2 consequence 2) is the *inductive/magnetic* wall: $S_\mu\to0
  \Rightarrow \mu_{eff}\to0 \Rightarrow Z\to0$, expelling B. This is the branch
  the engine *must* use — the genesis audit (`…genesis-next-steps-scope.md:71-74`,
  C4) flags that the engine's symmetric default $z_{local}=Z_0/\sqrt S\to\infty$
  is *inverse* (open) polarity and reaches the canonical low-Z short *"only via
  the magnetic branch ($\mu_{eff}\to0\Rightarrow Z\to0$)."*
- **Charge-coupling = CAPACITIVE node.** The charge (E-termination, §2
  consequence 1) lives on the node's shunt-C. That is the capacitive half.

So $V=2$ is *why* the polarity question has a clean answer: the mass sits in the
inductive (Meissner) reactance, the charge in the capacitive reactance. The
confining wall is magnetic.

**Honest flags.**

- *Capacitive-vs-magnetic provenance is not fully reconciled.* `resonant-lc-solitons.md`
  derives the *same* $\Gamma=-1$ from $C_{eff}\to\infty$ (capacitive), while the
  live engine needs $\mu\to0$ (magnetic). Both reach $Z\to0$; the static
  particle-core has *both* collapsed (`…tex:432`). Which reactance is *primary*
  in the dynamics is genesis **Fork B (polarity)**, still open
  (`…genesis-next-steps-scope.md:85`). §3 takes the magnetic branch because that
  is the one the load-bearing engine uses; the capacitive derivation is the same
  wall seen from the charge side.
- *London-penetration caveat (B not strictly zero at the nodes).* A real Meissner
  superconductor does not expel B to exactly zero — B decays over the London
  depth $\lambda_L$. The AVE analog of that finite leak is the electron tank's
  *finite Q*: a fraction $1/Q=\alpha$ leaks per cycle through the TIR boundary
  (`theorem-3-1-q-factor.md:81`). The electron is not a perfect mirror; it leaks
  $\alpha$ per cycle. (Queued in §7c: "$\alpha$ as the London-depth leak,
  $Q=1/\alpha$.")

**Classification.** Class **C** consistency synthesis. It unifies four canonical
threads under one picture and adds **no primitive**; per
`historical-precedents.md:39` the Kelvin-thread ceiling is consistency-class, and
this inherits it. The unification is an intuition/coherence contribution, not a
derivation or a prediction.

## §4 — Derivation: rotor = zitterbewegung = Compton clock (spin & mass, one oscillation)

*[scaffold — filled in a following commit]*

## §5 — Derivation: spin (helicity) stabilizes the unknot

*[scaffold — filled in a following commit]*

## §6 — Charge sign from cosmic-frame chirality

*[scaffold — filled in a following commit]*

## §7 — Consequences and open derivations queued

*[scaffold — filled in a following commit]*

---

## Cross-references (canonical leaves + engine + tracker — all verify-before-cite checked)

**Axioms / ontology**
- `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2 — Axiom 1: 6 DOF/node, 3 translational→E, 3 microrotational→B; Cosserat rotational DOF = substrate-native origin of spin; `I4₁32` chiral space group.

**EE / circuit (Vol 4 Ch 1 + engine)**
- `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md` — `C_eff→∞` (:32), `Z_core→0Ω` (:38), `Γ=−1` Perfect Short-Circuit Boundary (:48), MIT-Bag exposure (:54).
- `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md` — `Q_tank=1/α` (:38), `α⁻¹=4π³+π²+π` (:15), "this IS α" (:81), 4π = K4 bipartite lobe-count (:78).
- `manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex` — Meissner particle-core impedance row (:432); MIT-Bag/flux-tube (:569-587); Bingham/TVS-Zener slipstream (:294-362).

**Particle / topology (Vol 2 Ch 1)**
- `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-unknot.md` — electron = `0₁` unknot, Beltrami `∇×A=kA` standing wave (:13), ropelength 2π (:59).
- `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md` — genesis chain (:11), C3 phase-coherence "dissipates instead" (:85), LH/RH Beltrami output (:25).
- `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/chirality-and-antimatter.md` — charge = topological twist direction; e⁻=RH unknot, e⁺=LH unknot (:10).
- `manuscript/ave-kb/vol2/claim-quality.md:1199` — Mass-Closure Theorem `mc²=E_reactive`.
- `manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md` — massive dispersion `ω²=c²k²+ω_C²`, `ω_C=m_ec²/ℏ` (:184); Op6 Coulomb-cavity eigenvalue (:212-215).
- `manuscript/ave-kb/vol2/nuclear-field/ch12-millennium-prizes/poincare-conjecture.md` — `c=0` ⇒ no crossing-number protection, radiates freely (:36, :48).

**Cosmic frame / Kelvin precedent**
- `manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md` — `Ω_freeze` direction → `I4₁32` R-handed chirality (:45); R-vs-L selected by cosmic angular momentum (:183); chirality coupling NOT derived (:100).
- `manuscript/ave-kb/common/historical-precedents.md` — Kelvin 1867 vortex-atom thread (:23-30); consistency-class ceiling (:39); verdict-II "charge=helicity confirms" (:28).

**Engine + constants**
- `src/ave/core/k4_tlm.py` — `V_inc` node-port array (:192), `Φ_link` per-bond flux linkage (:206, accumulation :371,:386).
- `src/ave/topological/k4_cosserat_coupling.py` — asymmetric-Meissner kernel `Z_eff/Z_0=√(S_μ/S_ε)` (:364), code (:390-393), "Meissner, Z_eff→0 as S_μ→0" (:368).
- `src/ave/topological/vacuum_engine.py:1172` — `PairNucleationGate` docstring: Bingham-plastic capsule, Kelvin 1867 topological protection, Meissner `A²_μ≥1`, charge sign `±Φ_critical` from lattice chirality.
- `src/ave/solvers/radial_eigenvalue.py` — atomic-orbital eigensolver: solves soliton `(n,l)` radial standing wave, Op6 eigenvalue `Z²Ry/n²` — **scalar/spinless cavity** (no spin/helicity quantum number).
- `src/ave/core/constants.py` — `V_TOROIDAL_HALO=2.0` dual-reactance count (Grant-adjudicated 2026-06-01, :757-796): 3 E-DOF→`X_C`, 3 B-DOF→`X_L`; unknot ground-state mass framing (:53-62).

**Orchestration / open state**
- `_orchestration/2026-06-06_genesis-next-steps-scope.md` — genesis chain (§0), AUDIT CORRECTIONS (§8: C1 live emergent wall, C2 amplitude-gating blocker, C4 polarity, C6 8 leaves), Forks A/B/C/D (§9).
