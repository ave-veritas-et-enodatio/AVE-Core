[↑ App D: Computational Graph Architecture](./index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-pf84ng]
-->

## The Genesis Algorithm (Poisson-Disk Crystallization)

The first step in simulating the vacuum is establishing the 3D coordinate positions of the discrete inductive nodes ($\mu_0$).

**The Random Noise Fallacy:** Initial computational attempts utilizing unconstrained uniformly distributed random noise resulted in a "Cauchy Implosion." The resulting lattice packing fraction converged to $\approx 0.31$, characteristic of a standard amorphous solid. This density fails to reproduce the sparse QED limit ($\approx 0.18$) required by Axiom 4.

**The Poisson-Disk Solution:** To satisfy macroscopic isotropy while enforcing the microscopic hardware cutoff, the software must generate the node coordinates using a **Poisson-Disk Hard-Sphere Sampling Algorithm**. By enforcing an exclusion radius of $r_{min} = l_{node}$ during genesis, the lattice settles into a packing fraction of $\approx 0.17$--$0.18$, creating a stable, sparse dielectric substrate.

**Rheological Tuning:** ~~Simulation confirms that the "Trace-Reversed" mechanical state ($K=2G$) is an emergent property of the Chiral LC coupling modulus.~~ *(provenance sentence struck 2026-08-02 per Rule 12 — preserved verbatim above and in git, not deleted; see the DE-CLAIM banner below.)*  <!-- rule12-freeze: base=8acacec120ab392e67efbe8524d8b90fe09cc381 region=above offset=0 lines=15 bytes=1071 sha256=f989536d39c1bcd40333c8b46da78e615962934bdb9ec5d23f868ae73297820a -->
- **Low Coupling ($k_{couple} < 3.0$):** The lattice behaves as a standard Cauchy solid ($K/G \approx 1.67$).
- **High Coupling ($k_{couple} > 4.5$):** The lattice undergoes a phase transition, locking microrotations to shear vectors, driving the bulk modulus to roughly twice the shear modulus ($K/G \approx 1.78 - 2.0$).

> **[DE-CLAIM 2026-08-02 — $K = 2G$ provenance (CRIB-1); KB-lockstep with the merged print correction]**
>
> **Status of this note.** Discharged-decision propagation of an already-ruled state — it adjudicates **nothing new**. The printed twin of the struck sentence (`manuscript/vol_0_engineering_compendium/chapters/03_computational_graph.tex`, the `[DE-CLAIM 2026-08-02] $K = 2G$ provenance (CRIB-1)` block) was corrected and **merged in PR #839**, whose own text records this leaf as the co-lagging KB mirror. Until now this leaf asserted what print had already withdrawn — an inversion of the standing rule that the KB is the truth source. **No value refill:** no replacement $k_{couple}$, $K/G$ ratio, mechanism or provenance is supplied here.
>
> **What is withdrawn.** The claim that $K = 2G$ is an **emergent property** confirmed by simulation. $K = 2G$ is **form-derived, value GR-imported**: the substrate forces the *form* of the elastic response $K/G = f(\rho)$, but the *value* — the GR trace-reversal identity — is neither crystalline-forced nor constitutively-forced ([`form-deriving-value-importing.md`](../../../common/form-deriving-value-importing.md):87, the `K = 2G` row, **GR-IMPORTED**, PR #261). The question stays open on the engine side: the genuine $48\times48$ chiral micropolar Bloch eigensolve on the ratified srs-z3 net does **not** close it — the full micropolar sector (the corpus's own proposed $K=2G$ mechanism, `clm-o3q9ul`) gives a one-parameter $\nu_{eff}(\rho)$ *family* rather than a forced $K=2G$; the independent $\kappa_{rot}$ is a $k\to0$ Cauchy-grade spectator sourcing **no** chiral coupling; and the geometry-fixed chiral $B$ moves $\nu_{eff}$ *away* from $2/7$ ([`vol1/claim-quality.md`](../../../vol1/claim-quality.md):665, *"K=2G stays GR-imported (PR #261)"*).
>
> **Scope of this note — the coupling rows are PRESERVED and are not de-claimed.** Both `k_couple` bullets above stand exactly as written. The $K/G \approx 1.67$ low-coupling row is retained **on purpose**: the 2026-06-15 KB-reconciliation note later in this leaf cites the standard-Cauchy value by name (*"A standard Cauchy solid is $K = \frac{5}{3}G$"*), and deleting the bullets would silently break that note's receipt. CRIB-1 additionally forbids labelling the AVE lock *"the Cauchy relation"* — a three-way homonym ([`vol1/claim-quality.md`](../../../vol1/claim-quality.md):652); this leaf does not do that, and no such label is introduced here.
>
> **⚑ FLAGGED, NOT FIXED (sibling co-lag, outside this lane's 8-item scope — flag-don't-fix).** [`common/appendices-overview.md`](../../../common/appendices-overview.md):119 carries this same provenance sentence **byte-verbatim and unbannered**. It is the KB mirror of `manuscript/backmatter/01_appendices.tex`, whose print twin PR #839 explicitly recorded as belonging to a *different* lane and deliberately did **not** correct. Editing that leaf here would put the KB ahead of an uncorrected print site on a claim this lane has no mandate to adjudicate. Surfaced for routing, deliberately not edited.

## Chiral LC Over-Bracing and The $p_c$ Constraint

Once the spatial nodes are safely crystallized via the Poisson-Disk algorithm, the computational architecture must generate the connective spatial edges (The Capacitive Flux Tubes, $\epsilon_0$).

**The Cauchy Delaunay Failure:** If the physics engine simply computes a standard nearest-neighbor Delaunay Triangulation on the Poisson-Disk point cloud, the resulting discrete volumetric packing fraction of the amorphous manifold evaluates to $\kappa_{cauchy} \approx 0.3068$. While less dense than a perfect crystal (FCC $\approx 0.74$), it is still too dense to survive. 🔴 *[KB-reconciliation 2026-06-15 (vol_2 brief §D, internal mislabel; mirrors vol_0 ch03:22 / PR #235)]* ~~A standard Cauchy elastic solid ($K = -\frac{4}{3}G$) is thermodynamically unstable and will implode during macroscopic continuous simulation.~~ **A standard (non-micropolar) Cauchy elastic treatment of this substrate is thermodynamically unstable: without the chiral couple-stress the effective bulk modulus is not held positive, so the longitudinal modulus collapses through its instability threshold ($M = K + \frac{4}{3}G = 0$, i.e. $K = -\frac{4}{3}G$) and the lattice implodes during macroscopic continuous simulation. (A standard Cauchy solid is $K = \frac{5}{3}G$; $K = -\frac{4}{3}G$ is the $M=0$ longitudinal-modulus instability threshold, not the Cauchy state.)** 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**

**Enforcing QED Saturation:** The analysis derived that the fundamental phase limits of the universe bounded the geometric packing fraction of the vacuum to 🔴 *[KB-reconciliation 2026-06-15 (vol_2 brief §A.2; mirrors vol_0 ch03:24 / PR #235)]* ~~$p_{c} \approx \mathbf{0.1834}$, forcing the emergence of $\alpha$~~ **$p_{c} = 8\pi\alpha \approx \mathbf{0.1834}$ — with $\alpha$ a *retained* calibration input (a value-scoped echo beneath the canonical Class-B identification, resting on $R\cdot r = 1/4$ which the substrate does not independently select; per `vol1/ch8-alpha-golden-torus.md` :11), not an output forced to emerge from the packing fraction**. To computationally force the effective geometric packing fraction ($p_{eff}$) down from the unstable $\sim 0.3068$ baseline to the stable $0.1834$ limit, the software must enforce **Chiral LC Over-Bracing**. The connective array of the physics engine cannot be limited to primary nearest neighbors; the internal structural logic must span outward to incorporate the next-nearest-neighbor lattice shell.

Because the volumetric packing fraction scales inversely with the cube of the effective structural pitch ($p_{eff} = V_{node} / l_{eff}^3$), the required spatial extension for the Chiral LC links evaluates identically to:

$$
C_{ratio} = \frac{l_{eff}}{l_{cauchy}} = \left( \frac{p_{cauchy}}{p_{c}} \right)^{1/3} \approx \left( \frac{0.3068}{0.1834} \right)^{1/3} \approx \mathbf{1.187}
$$

By structurally connecting all spatial nodes within a $\approx 1.187 \, l_{node}$ radius, the discrete graph cross-links the first and second coordination shells of the amorphous manifold. This generates the $\frac{1}{3} G_{vac}$ ambient transverse couple-stress required by micropolar elasticity. This computational architecture guarantees that all subsequent continuous macroscopic evaluations of the generated graph (e.g., metric refraction, VCFD Navier-Stokes flow, and trace-reversed gravitational strain) will align with empirical observation 🔴 *[KB-reconciliation 2026-06-15 (vol_2 brief §A.4/G; mirrors vol_0 ch03:32 / PR #235)]* ~~without requiring any further numerical calibration or arbitrary mass-tuning~~ **without requiring any further numerical calibration beyond the framework's three calibration inputs $\{m_e, \alpha, G\}$ (the named trace-reversed gravitational strain routes through $G$, which is itself a value-fitted calibration input — mixed: form-derived $/7$ form, value-fitted $\xi$; closed-form Chain B′ open)**.

## Explicit Discrete Kirchhoff Execution Algorithm

To bridge the gap between abstract continuum flow vectors ($\mathbf{J}$) and the raw geometric structure of the computational graph edge-matrix, the VCFD (Vacuum Computational Fluid Dynamics) module utilises an **Explicit Discrete Kirchhoff Methodology** mapping discrete potential ($V$) to spatial nodes and inductive flow ($I$) to discrete spatial graph edges.

To exactly map continuous differential forms into computational array memory without breaking action-minimization, the system utilizes **Symplectic Euler Update Loops**:

1. **Capacitive Node Updates (The Conservation of Flow):** The discrete potential difference acting on an isolated fractional lattice coordinate node ($V_i$) is mathematically identical to the sum of all inductive currents entering minus the currents leaving that discrete junction point.

$$
\Delta V_i = \frac{dt}{C} \left( \sum I_{in} - \sum I_{out} \right)
$$

2. **Inductive Edge Updates (The Stress Tensor Matrix):** The kinetic transport flux acting along the discrete Chiral LC tensor spatial edge connecting coordinate $(x_0, y_0, z_0)$ to $(x_1, y_1, z_1)$ is geometrically bounded to the potential gradient existing across its fractional length.

$$
\Delta I_e = \frac{dt}{L} \left( V_{start} - V_{end} \right)
$$

By combining the $C_{ratio} \approx 1.187$ Chiral LC Over-Bracing requirement over a $r_{min} = l_{node}$ Poisson-Disk genesis space, and advancing the lattice via Symplectic Kirchhoff loops, the computational framework provides a proving-ground connecting raw network mechanics to classical standard-model topological properties.

---

---

## R40 batch-2a — NEEDS-RE-DERIVATION status note (2026-08-11)

**Class:** status demotion under **R40**. This note mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`,
**moves no solidity number**, adjudicates no channel and opens no fork. Every byte of each demoted
claim is preserved; the stamped line gains a status marker only (honesty-lag pattern, Rule 12).

**The arc, in four clauses (R40's header form; clause 4 points at the LANDED artifact, not at a
ruling record).**

1. **The kill fired** — the walk-back that closed the bulk radiative-port reading.
2. **The premise localized to the imported `K = 2G` elastic modulus** — the compressible far-field
   branch was minted by a GR-imported modulus, not forced by the axioms.
3. **The axioms underdetermine the bulk sector** — the flat-direction finding: the written action
   conserves the Gauss function pointwise and never fixes its value.
4. **The replacement is the LANDED ratified bound-sector law — Axiom 5, Substrate DC Bias**, clauses
   **S** (deposit), **G** (bias coupling / bridge) and **Q** (quiescence), canonical at
   [`eq_axiom_5.tex`](../../../../common_equations/eq_axiom_5.tex) with its register entry in
   [`axiom-register.md`](../../../common/axiom-register.md) (§ *Axiom 5 — Substrate DC Bias*). Under
   clause **G** the A1 / bulk slot is a **bound response** — $\mathbf{u}_0 =
   -\mathcal{A}_g\nabla\varepsilon_{11}$, mechanism gloss **back-reaction** — with **no independent
   propagating branch, no port and zero longitudinal characteristic speed**. A bulk *wave speed*, a
   bulk *radiative port*, a bulk *band-branch* and a bulk *transit clock* therefore have **no
   referent**, and each row below owes its re-derivation on that footing.
   $\mathcal{A}_g$ (the **bias-coupling area**) is an `UNVALUED-RATIFIED-CONSTANT` per **R48**
   ([`interlock-register.md`](../../../common/interlock-register.md), § *𝒜_g — the bias-coupling
   area*): it is **not valued here or anywhere**, and **the calibration count stays 3**.

**Standing named-open debt — the honesty rider.** The ratified axiom does **not** discharge
everything. **THE BIAS PROPAGATION THEOREM is Axiom 5's standing named-open debt**, stated by the
axiom's own phase-structure paragraph, clause **(c1)**: clause G's elliptic law is the *static
abstraction of underived finite-speed bias dynamics*, and the $(u,\pi)$ no-signalling theorem does
**not** cover the bias read — the bias's finite propagation speed is *owed, not held*. Every row
tagged **⚑ BIAS-DEBT** below re-derives against the ratified axiom **with that debt standing**, never
against a closed replacement.

**Vocabulary.** Canonical nouns authored here: **the bound response** ($\mathbf{u}_0$), **the bias**
($\varepsilon_{11}$), the **DC operating point / quiescent point (Q-point)**; **back-reaction** is
the mechanism gloss. *"dress"*, *"grade"* as $\varepsilon_{11}$'s canonical noun, and *"halo"* for
the physics (the physics noun is the **near-field store / added-mass**) are RETIRED by **R50**;
*"retardation"* is retired by **R49(b)** in favour of **propagation delay / finite propagation
speed**. Corpus text quoted below is reproduced from the banked audit and is
**content-verified at HEAD (markup-reduced, not byte-identical)**; it is never reworded.

**Rows carried in this file.**

- **`:34`** — stamped at `:34`. *(family: K-backed stability)*  ⚑ **BIAS-DEBT**
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  without the chiral couple-stress the effective bulk modulus is not held positive, so the longitudinal modulus collapses through its instability threshold ($M = K + \frac{4}{3}G = 0$)
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  K-backed stability argument (the bin's named example): stability is governed by positivity of the P-wave modulus, treating K as a dynamical reservoir; under the carve stability is kinematic (no compression DOF to implode) — the leaf's job survives, its mechanism is the import's.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

**Records.** Ruling **R40** (the demotion sweep) · the banked worklist
[`r40_sweep_worklist_verified.json`](../../../../../research/drivers/r40_sweep_worklist_verified.json) · batch-0
scope verification and batch-1 execution records in `_orchestration/` · this batch's record
`_orchestration/2026-08-12_r40-sweep-batch2a.md`.

