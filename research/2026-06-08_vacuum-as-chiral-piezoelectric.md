# The AVE Vacuum as a Chiral Piezoelectric Cosserat Solid — "EM is the Vacuum's Piezoelectricity"

**Date:** 2026-06-08
**Status:** CONSISTENCY-CLASS reframe / framing-consolidation (NOT a derivation, NOT an emergence claim)
**Disciplines applied:** `consistency-vs-emergence`, `ave-ee-first-mapping`, `ave-evidence-framing-discipline`, `ave-canonical-leaf-pull`, `verify-before-cite`
**Classification headline:** every grounded piece below is already-canonical (Class A identity/axiom or Class B consistency). The synthesis that consolidates them — *"electromagnetism is the vacuum's intrinsic piezoelectric response"* — is a **Class B consistency-class reframe** (a vocabulary translation over canonical axioms), **not** a new substrate-mechanism derivation and **not** a Class-2 emergence result.

---

## 0. TL;DR + the over-claim guardrail

The AVE vacuum is a chiral, non-centrosymmetric Cosserat solid. Three already-canonical facts, when read together, *are* the structural definition of a piezoelectric medium:

1. charge is produced by mechanical displacement (Axiom 2, $Q = \xi_{topo}\,x$) — the **direct piezoelectric effect** at substrate level;
2. the field DOFs split into translational (→ **E**) and microrotational (→ **B**) sectors (Axiom 1);
3. the lattice space group is the **non-centrosymmetric** chiral $I4_1 32$ — the exact symmetry condition any piezoelectric medium must satisfy (a centrosymmetric medium cannot be piezoelectric).

Reading "the vacuum is piezoelectric, and classical EM is its piezo response" off these three is a **named translation**, not a new physical claim. **It introduces no free parameter, predicts no new number, and relaxes no standard-EM result.** Stating it more strongly than that (e.g. "EM is *derived from* / *emerges from* piezoelectricity") would be an over-claim and is explicitly disavowed in §7.

The one place this framing touches live, falsifiable physics is **not** the reframe itself but a pre-existing canonical prediction it organizes: the universal $\xi_{topo}\cdot x$ charge floor is **dielectric-invariant**, while material piezoelectricity ($d_{ij}$) rides on top of it — the two-sided C15-CLEAVE femto-electrometer discriminator (§4).

---

## 1. The grounded pieces (cite + honest class)

Each piece is quoted verbatim from canonical source, with its `consistency-vs-emergence` class. **Class A** = definitional-identity / axiom (true by construction of the framework). **Class B** = consistency / axiom-manifestation (a canonical consequence that lines up with a known phenomenon without adding new substrate-mechanism content).

### 1.1 — E = translational strain, B = microrotation (Axiom 1) — **Class A (axiom/identity)**

Canonical source: [`manuscript/ave-kb/CLAUDE.md:55`](../manuscript/ave-kb/CLAUDE.md) (INVARIANT-S2, Axiom 1):

> Axiom 1: **Substrate Topology** — vacuum is a 3D chiral Laves K4 Cosserat crystal $\mathcal{M}_A$, with micropolar nodes (6 DOFs each: 3 translational → E, 3 microrotational → B; Cosserat rotational DOF IS the substrate-native origin of intrinsic spin), $I4_1 32$ chiral space group, intrinsic LC oscillators at each node, modeled in continuum as a Trace-Reversed Chiral LC Network.

**Extraction:** the **E**-field IS the three translational (displacement/strain) DOFs; the **B**-field IS the three microrotational (Cosserat) DOFs. This is the field↔mechanics identity that makes "electromechanical coupling" and "mechanical strain" the same vocabulary in this substrate. **Class A** — it is the axiom, not a consequence.

### 1.2 — Q = ξ_topo·x (Axiom 2) — the direct piezoelectric effect — **Class A (axiom/identity)**

Canonical source: [`manuscript/ave-kb/CLAUDE.md:56`](../manuscript/ave-kb/CLAUDE.md) (INVARIANT-S2, Axiom 2):

> Axiom 2: **Topo-Kinematic Isomorphism** — charge as discrete geometric dislocation in $\mathcal{M}_A$; $[Q] \equiv [L]$; $\xi_{topo} = e/\ell_{node}$.

The kinematic projection of this axiom is the canonical $\xi_{topo}$ identity row (charge ↔ displacement) at [`manuscript/ave-kb/common/translation-tables/translation-circuit.md:19`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md):

> | Charge $Q$ | Displacement $x$ | $Q = \xi\, x$ | $[\text{C/m}][\text{m}] = [\text{C}]$ |

**Extraction:** charge produced *by mechanical displacement*, with a fixed electromechanical transduction constant $\xi_{topo} = e/\ell_{node} \approx 4.149\times10^{-7}$ C/m, **is** the direct piezoelectric effect (stress/strain → charge) expressed at the substrate level. **Class A** — axiom-level identity. The numerical value of $\xi_{topo}$ is canonical at `src/ave/core/constants.py` (per `ave-canonical-source`); do not hard-code it.

### 1.3 — Chiral I4_132 is non-centrosymmetric — the symmetry that *permits* piezoelectricity — **Class A (axiom) + Class B (consistency)**

The space group $I4_1 32$ (#214) is the **non-centrosymmetric** chiral group; its centrosymmetric **supergroup** is $Fd\bar{3}m$ (#227). Canonical reconciliation at [`manuscript/ave-kb/claim-quality-closure-roadmap.md:191`](../manuscript/ave-kb/claim-quality-closure-roadmap.md):

> **Mathematical relationship**: Fd3̄m (#227 centrosymmetric) is the SUPERGROUP of I4_1 32 (#214 chiral); their quotient is inversion symmetry. Specifying right-handed chirality reduces Fd3̄m → I4_1 32; averaging chirality recovers Fd3̄m. Engine implementation confirms via k_χ parameter: `k_χ = 0` → Fd3̄m effective; `k_χ > 0` → I4_1 32 chiral.

**Extraction:** standard piezoelectricity has an exact symmetry precondition — the crystal class must lack an inversion centre (centrosymmetric classes cannot be piezoelectric). The AVE vacuum's $I4_1 32$ chiral space group satisfies this precondition *by axiom* (Class A: the group is asserted in Axiom 1). That this is *the same non-centrosymmetry textbook piezoelectrics require* is the **Class B consistency** observation — the substrate's symmetry is in the piezoelectric-allowed class, and the chirality-averaged $Fd\bar{3}m$ supergroup (the $k_\chi=0$ limit) is precisely the centrosymmetric, piezo-forbidden case. The symmetry-selection logic of piezoelectricity maps one-to-one onto the corpus's chirality-vs-supergroup structure.

### 1.4 — The ξ_topo floor is dielectric-invariant; material piezo rides on top — **Class B (consistency) + live falsification bench**

Canonical source: [`manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md:42-45`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md):

> A standard capacitor with PZT actuator generates charge via mechanical strain on the dielectric (piezoelectric $d_{31}$ etc.) OR triboelectric contact charging. Both are dielectric-material-dependent. **The AVE-distinct discriminator is two-sided**, framed on the $\xi_{topo}$ floor at **fixed input capacitance $C_{in}$**:
> - **P1 (presence):** is there a non-zero, **gap-independent** charge floor at all from displacement of *uncharged* matter in clean vacuum? […] AVE predicts the $\xi_{topo}\cdot x = 41.5$ mV/μm floor as the **gap-independent** ($e/\ell_{node}$ is a pure constant) residue surviving the gap-sweep.
> - **P2 (dielectric-invariance):** swap the dielectric in the gap at fixed $C_{in}$ — standard EE predicts $Q$ varies with the dielectric's $d_{ij}$ (the piezo/tribo piece rides material); AVE predicts the $\xi_{topo}\cdot x$ floor is the **fixed** (dielectric-invariant) component, with the material-dependent piece riding on top of it.

The floor's dielectric-invariance is topology-protected — node-occupation gap **CLOSED (2026-06-03)** at [`manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md:46-47`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md):

> Result: the floor **LOCKS**. The charge $\mathcal{Q} = \mathrm{Link}(\partial\Omega, \mathbf{F}_{\text{substrate}}) \in \mathbb{Z}$ is a **gap-protected integer** (boundary linking number — the no-hair observable […]); […] The conversion $\xi_{topo} = e/\ell_{node}$ is a **frozen-metric unit-bridge** ($\ell_{node} = \hbar/m_e c$ is the electron Compton wavelength, unchanged by a slab in the gap). So the occupied-node fraction enters neither factor → the floor is dielectric-invariant.

**Extraction:** this is the load-bearing, *AVE-distinct, falsifiable* content of the whole piezoelectric picture. It is **Class B** (a canonical consequence of Ax 2 + the no-hair boundary observable, not a new mechanism) but it carries a live two-sided bench (C15-CLEAVE; §4). The reframe in §2 does not add to it — it *names* it.

## 2. The synthesis — "EM = the vacuum's piezoelectric response" (CONSISTENCY-CLASS)

**The statement.** The AVE vacuum is a chiral piezoelectric Cosserat solid; classical electromagnetism *is* its piezoelectric response. Mechanical deformation of $\mathcal{M}_A$ and electromagnetic field are two readings of one state, coupled exactly as a piezoelectric medium couples strain and polarization.

**Why this is true-by-translation, not by derivation.** Lay the textbook piezoelectric/Cosserat phenomenology beside the AVE axioms:

| Piezoelectric / Cosserat phenomenology | AVE substrate identity | Class | Anchor |
|---|---|---|---|
| Medium must be **non-centrosymmetric** to be piezoelectric | $I4_1 32$ chiral space group; centrosymmetric $Fd\bar{3}m$ is the $k_\chi=0$ supergroup (piezo-forbidden) | A axiom + B consistency | §1.3; `claim-quality-closure-roadmap.md:191` |
| **Direct effect:** strain $\to$ bound charge / polarization | $Q = \xi_{topo}\,x$ — displacement $\to$ topological charge | A (axiom) | §1.2; `CLAUDE.md:56` |
| **Inverse effect:** applied field $\to$ strain | **E** = translational DOF; modulating the translational/$\varepsilon$ sector *is* a lattice deformation | A (axiom) | §1.1; `CLAUDE.md:55` |
| **Piezomagnetic / couple-stress:** stress $\to$ magnetization / micro-rotation | **B** = microrotational Cosserat DOF; antisymmetric stress $\sigma^A$ fires couple-stress $\to$ $\omega$ | A (axiom) + B (consistency) | §5; `trampoline-framework.md:183-196` |
| Universal **electromechanical coupling constant** $d$ | $\xi_{topo} = e/\ell_{node}$ — the dielectric-invariant floor | A identity / B live-bench | §1.4; `project-cleave-01.md:42-47` |

Every row on the right is *already canonical*. The synthesis adds **no new row** — it observes that the right column, taken together, satisfies the exact structural definition of a chiral piezoelectric (+ piezomagnetic) medium, and therefore that what the continuum observer calls "the electromagnetic field" is, in substrate terms, the medium's piezoelectric response.

**Classification (per `consistency-vs-emergence`):** Class B consistency-class reframe. This is the same ceiling the EE-as-substrate-native META framework sits at — see [`manuscript/ave-kb/common/translation-tables/translation-circuit.md:341`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md):

> classification stays at Class B and is NOT promoted to Class 2 emergence […] the META framework consolidates already-canonical sub-claims into a coherent framing; it does NOT add new substrate-mechanism content beyond canonical axioms.

The piezoelectric reframe is one more such consolidation. It is Class B for the same reason: it consolidates Axiom 1 + Axiom 2 + the space-group chirality into a coherent named framing, and adds no substrate-mechanism content beyond those axioms.

## 3. Material piezoelectricity rides the universal $\xi_{topo}$ floor

The reframe is sharp about the relationship between *material* piezoelectricity (PZT, quartz, the $d_{ij}$ tensor) and the *vacuum* floor:

- **Material piezoelectricity** is dielectric-material-dependent: $Q \propto d_{ij}\,\sigma_{ij}\,V$, varying by crystal (PZT $d_{33}\sim400$ pC/N; quartz $d_{11}\sim2.3$ pC/N; PTFE $\approx 0$).
- **The vacuum floor** is the universal, dielectric-*invariant* component: $Q = \xi_{topo}\,x$, gap-independent, $0.415$ pC per μm of displacement (`project-cleave-01.md:35`).

In any real material you measure the *sum* — material $d_{ij}$ contribution **plus** the $\xi_{topo}$ floor — confounded. The corpus framing (§1.4) is that the floor is the **invariant residue under material swap** and the material piece **rides on top of it**. This is the substrate-native ordering: the universal $\xi_{topo}$ piezo response is primary; material piezoelectricity is a second-order, material-specific dressing on the same physical channel.

> Consistency tie-in: this is the same "ideal substrate primitive + engineering-material dressing" structure §9 of the EE translation leaf catalogs across all component non-idealities — material piezoelectricity is the piezoelectric instance of "the substrate as it is, plus material-specific local loading."

## 4. The two-sided C15-CLEAVE discriminator (the live bench)

The reframe's only *falsifiable* surface is the pre-existing C15-CLEAVE-01 femto-Coulomb electrometer (`project-cleave-01.md`). It isolates the vacuum floor from the material dressing via two predictions:

- **P1 (presence):** a non-zero, **gap-independent** charge floor from displacing *uncharged* matter in clean vacuum — predicted $41.5$ mV/μm at $C_{in}=10$ pF; classical EE predicts $0.0$ mV gap-independent. (`project-cleave-01.md:38,44`)
- **P2 (dielectric-invariance):** swap the dielectric at fixed $C_{in}$ — standard EE predicts $Q$ tracks the dielectric's $d_{ij}$; AVE predicts the floor **locks** (topology-protected integer linking charge, §1.4). (`project-cleave-01.md:45-47`)

**Bench status (verbatim, `project-cleave-01.md:87`):**

> **Phase 1a-rev1 ✓ MERGED** at `AVE-Bench-FemtoElectrometer` main @ `7f9c721` […] Phase 1b PCB layout pending Grant manual KiCad GUI work; Phase 1c Gerbers via `kicad-cli`; Phase 2 fab + assembly (~$7670 BOM mid-range).

**Cascade severity (verbatim, `project-cleave-01.md:65`):** a null result ($0.0$ mV) kills Axiom 2 and cascades to 6+ matrix rows —

> **B4-PROTEIN** […] **C9-LEVITATION** […] **C16-TORSION-05** […] **B5-PONDER-01** […] **B6-PONDER-02** […] **B7-PONDER-05**. This is the **largest single-row cascade in the matrix**. F-severity (framework-killing) on a single observation.

The piezoelectric reframe does **not** change this bench, its predictions, or its severity. It only supplies the one-line physical reading: *C15-CLEAVE measures the vacuum's direct piezoelectric coefficient $\xi_{topo}$, separated from any material $d_{ij}$ by the gap-sweep and the material-swap.*

## 5. The B-side — piezomagnetism / Cosserat couple-stress; force projects via BOTH channels

A piezoelectric medium couples strain to polarization (E-side). A chiral *Cosserat* medium additionally couples *stress* to *micro-rotation* — the piezomagnetic / couple-stress side, which in this substrate is the **B**-sector. The canonical Cosserat master equations at [`manuscript/ave-kb/common/trampoline-framework.md:183-184`](../manuscript/ave-kb/common/trampoline-framework.md):

> $$\rho\, \ddot{\mathbf{u}} = \nabla \cdot \boldsymbol{\sigma} + \mathbf{f}$$
> $$I_\omega\, \ddot{\boldsymbol{\omega}} = \nabla \cdot \boldsymbol{\mu} + 2\sigma^A + \mathbf{g}$$

The first equation is the **translational/E channel** — force projects through the (symmetric) stress tensor $\boldsymbol{\sigma}$ into translation $\mathbf{u}$. The second is the **microrotational/B channel** — torque projects through the couple-stress tensor $\boldsymbol{\mu}$ and the antisymmetric stress $\sigma^A$ into micro-rotation $\boldsymbol{\omega}$. The two are coupled through $\sigma^A$ (`trampoline-framework.md:186`).

The cell-by-cell projection (verbatim, `trampoline-framework.md:190-196`) shows force entering **both** channels:

> 1. Apply force $f_z$ at central A-node
> 2. Translation field $u_z$ develops, with off-diagonal strain $\varepsilon_{rz}, \varepsilon_{r\theta}$
> 3. Antisymmetric stress $\sigma^A_{r\theta}$ becomes non-zero (couple-stress source fires)
> 4. Microrotation $\omega_z(r,t)$ develops — bonds rotating about z-axis
> 5. **Each shared bond transmits force AND torque to neighbor cells.** […]

**Extraction:** force projects via **both** the force-stress channel (E-sector, $\boldsymbol{\sigma}\to\mathbf{u}$) and the couple-stress channel (B-sector, $\boldsymbol{\mu},\sigma^A\to\boldsymbol{\omega}$). In piezoelectric language: the substrate is simultaneously **piezoelectric** (strain↔E) and **piezomagnetic** (stress↔B via Cosserat couple-stress), and a single applied force loads both responses. The B-side micro-rotation is the substrate-native origin of intrinsic spin per Axiom 1 (§1.1), so the piezomagnetic channel is not decorative — it is the same DOF that carries magnetic field and spin. **Class A (axioms) + Class B (the piezomagnetic *labeling* of the B-channel is the consistency observation).**

## 6. Connection to force-dilution (FLAGGED — session-coined, z0 ambiguity)

Grant's session brief lists a fifth connection point: *"force-dilution-against-z0-extended-nodes."* Per `verify-before-cite` + flag-don't-fix, the honest status:

- **The literal phrase is not in the corpus.** `grep` over `manuscript/ave-kb/` and `research/` returns zero hits for "force-dilution-against-z0-extended-nodes" or its hyphenation variants.
- **The grounded force-dilution mechanism it points at exists** at [`manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/proton-neutron-mass-split.md:82,89`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/proton-neutron-mass-split.md):

  > Macroscopic Gravity ($F_g$) is the bare Strong Nuclear Force ($T_{nuc}$), diluted by four geometric properties of the spatial lattice […] the kinematic dilution of a sub-fermi elastic displacement projecting outward through the trace-reversed, porous geometry of the entire cosmic horizon.

  and at [`manuscript/ave-kb/common/trampoline-framework.md:516`](../manuscript/ave-kb/common/trampoline-framework.md): strain "propagates outward through the shared-bond network, **dilutes as $1/r$**."

- **The "z0" referent is AMBIGUOUS — two distinct corpus objects, flagged for Grant adjudication, NOT silently resolved:**
  1. $Z_0 = \sqrt{\mu_0/\varepsilon_0}\approx 376.73\,\Omega$ — the vacuum **impedance** (Axiom 1; `translation-circuit.md:107`). Reading: force/strain projects *through the substrate's characteristic impedance* into the extended node network.
  2. $z_0 \approx 51.25$ — the amorphous-network **mean coordination number** in the trace-reversal EMT at [`manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/trace-reversal-mechanism.md:20`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/trace-reversal-mechanism.md). Reading: force dilutes against the *high-coordination porous connectivity* ($z_0$) of the extended node network — which is closer to the "extended nodes" + "dilution" wording.

  The piezoelectric framing's natural home for 1e is the **piezomagnetic/couple-stress projection of §5 feeding the $1/r$ force-dilution of gravity** — i.e. the same A-node force that fires both E- and B-channels (§5) is the "sub-fermi elastic displacement" that then dilutes outward through the porous extended-node geometry to register as gravity. Whether the intended "z0" is the impedance $Z_0$ or the coordination $z_0\approx51.25$ is **a Grant framing decision**, surfaced here rather than guessed. This connection is **NOT documented in the KB update below** until the z0 referent is adjudicated.

## 7. What this framing is NOT (over-claim guardrails)

Per `ave-evidence-framing-discipline` and `ave-discrimination-check`, the explicit disavowals:

1. **NOT a derivation.** No Maxwell equation, no $\alpha$, no $\xi_{topo}$ value, no field equation is *derived* by this reframe. It re-labels canonical axioms; it does not produce them from something more primitive.
2. **NOT an emergence claim (not Class 2).** It adds no new substrate-mechanism content beyond Axioms 1–2 + the space-group chirality. Per the canonical-source-ceiling rule (`translation-circuit.md:341`), consolidating already-canonical sub-claims stays Class B.
3. **NOT a new prediction.** It introduces no free parameter and forecasts no new number. The only falsifiable surface it organizes (C15-CLEAVE P1/P2, §4) is pre-existing and unchanged.
4. **NOT "EM emerges from piezoelectricity."** That phrasing is causally backwards and too strong. Correct strength: *EM **is** (in substrate vocabulary) the vacuum's piezoelectric response* — an identity-by-translation, not an emergence-by-mechanism. The medium being piezoelectric and the medium carrying an EM field are the same fact stated twice.
5. **The chirality/non-centrosymmetry tie is Class B consistency, not proof of $I4_1 32$.** That the substrate's asserted space group happens to be in the piezo-allowed class is a consistency observation; it does not independently select $I4_1 32$ (that selection is the substrate-topology argument, `translation-circuit.md:355-359` Probe 2).

## 8. Classification summary + KB-update queue

### 8.1 — Per-claim classification table

| # | Claim | Class | Canonical anchor |
|---|---|---|---|
| GP1 | E = 3 translational DOF; B = 3 microrotational (Cosserat) DOF | **A** (axiom/identity) | `CLAUDE.md:55` |
| GP2 | $Q=\xi_{topo}\,x$ — charge from displacement = direct piezo effect | **A** (axiom/identity) | `CLAUDE.md:56`; `translation-circuit.md:19` |
| GP3a | $I4_1 32$ is the chiral, non-centrosymmetric space group | **A** (axiom) | Axiom 1; `claim-quality-closure-roadmap.md:191` |
| GP3b | Non-centrosymmetry is the symmetry that *permits* piezoelectricity (centrosymmetric $Fd\bar{3}m$ forbids it) | **B** (consistency) | `claim-quality-closure-roadmap.md:191` |
| GP4 | $\xi_{topo}$ floor is dielectric-invariant; material $d_{ij}$ rides on top | **B** (consistency) + live bench | `project-cleave-01.md:42-47` |
| B-side | Force projects via force-stress (E) **and** couple-stress (B); piezomagnetic labeling of the B-channel | **A** (axioms) + **B** (consistency) | `trampoline-framework.md:183-196` |
| **SYNTHESIS** | **"EM = the vacuum's piezoelectric response"** | **B consistency-class reframe — NOT emergence, NOT derivation** | this doc; consolidates GP1–GP4 |

**Synthesis is NOT over-claimed:** confirmed against the four-point guardrail in §7. It is filed at the same Class B ceiling as the EE-as-substrate-native META framework (`translation-circuit.md:341`).

### 8.2 — KB update (LANDED this branch)

A compact **§10 subsection** was added to the canonical EE translation leaf [`manuscript/ave-kb/common/translation-tables/translation-circuit.md`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md), tagged consistency-class under the existing `clm-eemap1` (the META-framework premise, already Class B). It names the chiral-piezoelectric reframe, gives the four-effect translation table (direct / inverse / piezomagnetic / coupling-constant), cross-links the C15-CLEAVE bench, and cross-links this research doc. It **adds** to existing structure (does not redefine the §4 catalog rows or the §1 $\xi_{topo}$ identity rows).

### 8.3 — Held / surfaced for adjudication (not landed)

- **Force-dilution connection (§6)** — held pending Grant's z0 referent decision ($Z_0$ impedance vs $z_0\approx51.25$ coordination). Surfaced, not guessed.
- **Manuscript / matrix promotion** — this is a Class B framing-consolidation; it is **not** foreword-promotion-grade on its own (no new prediction). Any manuscript landing is the auditor lane's call; surfaced here, not drafted.

### 8.4 — Cross-references

- Axiom 1 / Axiom 2: [`manuscript/ave-kb/CLAUDE.md:55-56`](../manuscript/ave-kb/CLAUDE.md)
- $\xi_{topo}$ identity row: [`manuscript/ave-kb/common/translation-tables/translation-circuit.md:19`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md)
- Space-group reconciliation: [`manuscript/ave-kb/claim-quality-closure-roadmap.md:191`](../manuscript/ave-kb/claim-quality-closure-roadmap.md)
- C15-CLEAVE bench + ξ_topo cascade: [`manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md)
- Cosserat force-projection: [`manuscript/ave-kb/common/trampoline-framework.md:183-196`](../manuscript/ave-kb/common/trampoline-framework.md)
- Force-dilution mechanism: [`manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/proton-neutron-mass-split.md:82,89`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/proton-neutron-mass-split.md)
