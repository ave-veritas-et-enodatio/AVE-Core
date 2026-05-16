[↑ Common Resources](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from common/trampoline-framework.md + AVE-QED Ch 11 + ave-prereg Step 1.5 as Core-canonical pedagogical primer for the trampoline/spring analogy -->

# The Trampoline/Spring Analogy: Core Pedagogical Primer

Per Grant directive 2026-05-16 ("I want the core to be self sufficient, duplicate"): this leaf is the Core-canonical pedagogical primer for the trampoline/spring analogy, distilled from AVE-QED Ch 11 `11_tensioned_trampoline.tex`. The analogy is the **picture-first mechanical visualization** of the AVE substrate, derived step-by-step from the reader's likely starting point (the GR pop-sci picture of gravity). **This is the primer the [ave-prereg skill Step 1.5](https://github.com/anthropics/claude-code/blob/main/skills/ave-prereg/SKILL.md) refers agents to when grounding new derivations.**

**Sister Core leaf**: [`common/trampoline-framework.md`](trampoline-framework.md) is the canonical synthesis/cross-reference document with five-bullet picture + ground-up build + chapter cross-refs. **This leaf** is the step-by-step pedagogical primer (Step 0 → 6) that builds the picture from scratch. Both serve different reader needs; both are Core-canonical.

> **Note on tone (per AVE-QED Ch 11 §2)**: this primer compares the AVE substrate visualization to the standard pop-science representation of GR's spacetime curvature (the "bowling ball on rubber sheet" picture). **This is a comparison of visualizations, not of theories.** General relativity as a mathematical formalism is well-defined and not under critique here; we contrast only the pedagogical pop-sci visualization that readers commonly carry into discussions of substrate physics.

---

## Step 0: The reader's prior — bowling ball on rubber sheet

The standard pop-science visualization of GR-gravity is a 2D rubber sheet, with a bowling ball at the center depressing it into a well, and a marble rolling around the well in an orbit-like trajectory.

**Structural features of this picture**:
- Substrate is **continuous** (no discrete scale)
- Substrate is **at rest** (no pre-tension)
- **No chirality** (mirror-symmetric)
- **Mass is given** (inserted from outside the picture)
- **One mode of response** (vertical depression of 2D sheet)
- Response is **linear elastic** (no saturation)
- Sheet extends **indefinitely** (no boundary at large strain)

This picture is the reader's likely starting point. Subsequent steps enumerate the structural features that distinguish the AVE substrate visualization from this pop-sci representation.

---

## Step 1: First structural difference — the substrate is discrete

The AVE substrate is a **discrete K4-bipartite tetrahedral lattice** with pitch $\ell_{\text{node}} \approx 3.86 \times 10^{-13}$ m (Axiom 1; canonical at Vol 1 Ch 1). Nodes are connected by bonds. There is **no substrate response below the lattice pitch** — the structure is genuinely discrete, not a continuous medium approximated by a lattice.

**Replace the continuous rubber sheet with this discrete lattice.** At this step, we do not yet add pre-tension, chirality, or saturation — only discreteness.

**What this step adds**: discrete spatial cutoff at $\ell_{\text{node}}$ — sets the **UV scale** of all physics on the substrate.

**What this step does NOT yet add**: chirality, pre-tension, saturation. Those come in later steps.

---

## Step 2: Second structural difference — bond pre-tension via buckling

**The key claim**: the bonds of the K4 lattice have a rest length $L_{\text{spring}}$ **greater than** the lattice site spacing $d$. When mounted between two nodes at spacing $d$, each bond is forced into a constrained configuration with $L_{\text{spring}} > d$.

**Mechanical consequence: buckling.** A linear elastic element mounted at compressed length must either compress axially or buckle into a curved configuration. The lower-energy solution depends on the bond's bending stiffness; for typical lattice geometries with moderate stiffness, **buckling wins**. The buckled configuration is a classic spontaneous-symmetry-breaking phenomenon: the unbuckled state is unstable, and the bond bifurcates into one of two stable buckled states, distinguished by the **direction of buckling**.

**The buckling direction sets chirality.** In an isotropic environment, the buckling direction would be chosen randomly. In AVE, the parent black-hole rotation imposes a **global directional bias** on the pre-geodesic plasma at the moment of K4 crystallization (cf. Q-G21, Q-G35). All bonds freeze in the same rotational buckling direction. **This is the substrate's frozen chirality.**

**What this step adds**: 
- Pre-tension (bonds carry stored elastic energy at rest)
- Chirality (a direction set globally at genesis)
- A candidate physical mechanism compatible with the $K = 2G$ operating point

**Connection to canonical AVE**:
- **"Lorentz-saturating chiral K4 metamaterial"** (Vol 1 Ch 1): the substrate has definite chirality, frozen at crystallization genesis
- **$K = 2G$ trace-reversal operating point** (Backmatter app: four-force unification): the substrate's specific stressed configuration
- **Cosserat micropolar tensor structure** (Vol 1 Ch 4): bond rotational degrees of freedom emerge from the buckled geometry

> **Note on rod-and-spring framing.** An equivalent way to draw this is as two separate components: rigid rods (length $L_{\text{rod}}$) mounted between nodes at spacing $d < L_{\text{rod}}$, with elastic springs spanning each rod at a skewed angle. This was the original framing (Grant Lindblom, 2026-05-13 evening); it is mechanically equivalent but introduces two structural elements (rod + spring) where the buckling picture uses one (a single elastic bond with rest length $> d$). The **buckling framing is preferred** because it maps directly to real K4 lattice bonds, which are single bonded elements with both topological and elastic character.

### Step 2 cooled-equilibrium interpretation (Grant's bet, 2026-05-13 late evening)

The buckled state is the substrate's **rest configuration**: the lattice geometry that the pre-geodesic plasma settles into when cooled during cosmic crystallization (cosmology "bottle in freezer" mechanism).

**Hypothesis** (Grant Lindblom, 2026-05-13 late evening, formalized in Q-G47 setup doc §5):

> **$K = 2G$ is the elastic configuration at which the cooled K4 lattice has minimum free energy.** The substrate doesn't have $K = 2G$ because GR demands it (top-down) or because FTG-EMT self-consistency checks it (back-derived); it has $K = 2G$ because that's the **thermodynamic attractor** of the cooling pre-geodesic plasma.

**Mathematical formulation**: cooled equilibrium satisfies $\partial U/\partial r_d = 0$ at $r_d^*$, and Grant's bet is that $K(r_d^*)/G(r_d^*) = 2$ at the same $r_d^*$.

**Critical subtlety** (Vol 3 Ch 1:33-37 canonical): primary K4 bond buckling alone gives the **Cauchy baseline** $K/G \approx 5/3$ at the affine-deformation limit. Bridging from $5/3$ to $2$ requires additional structural contributions:
- Secondary over-bracing links at $r_{\text{secondary}} \approx 1.187 \ell_{\text{node}}$
- Cosserat micropolar coupling to microrotational DOFs

So Step 2's primary-bond buckling picture is **necessary but not sufficient**; the full $K = 2G$ derivation requires the buckling picture PLUS over-bracing PLUS Cosserat coupling.

**Falsifiable bonus**: if Q-G47 closes via the thermodynamic route, the latent heat released during Phase I crystallization ($U_{\text{random}} - U(r_d^*)$) gives the AVE-native CMB temperature derivation. Cross-reference cosmology "bottle in freezer" framework.

**Provisional status: still open.** The cooled-equilibrium interpretation is a hypothesis being tested by Q-G47; until the Cosserat tensor calculation closes (Sessions 19+, per [Q-G47 substrate-scale Cosserat closure](q-g47-substrate-scale-cosserat-closure.md)), this section flags the hypothesis but does not claim it as derived.

---

## Step 3: Third structural difference — global chirality across the lattice

The buckling direction set in Step 2 is **global**: all bonds in the K4 lattice are buckled in the same direction, frozen at crystallization genesis. There is no local variation in chirality direction; the entire substrate has one handedness.

**What this step adds**: lattice-scale coherent chirality. The direction is inherited from the parent BH's rotational angular momentum (cf. Q-G35 chirality inheritance).

**Empirical consequence: chiral coupling effects.** The HOPF-02a test (`AVE-HOPF/hardware/hopf_02_ASSEMBLY_GUIDE.md`) is the direct experimental probe: enantiomer pairs of torus-knot wire antennas should show frequency differences from this lattice chirality, at the predicted magnitude:

$$\Delta f / f = \alpha \cdot \frac{pq}{p + q}$$

For electron $(2, 3)$: $\Delta f/f = 1.2\alpha \approx 8.76 \times 10^{-3}$ (AVE-HOPF birefringence prediction).

---

## Step 4: Fourth structural difference — applied strain and the saturation kernel

When an external field is applied to the substrate, bonds are pulled out of their buckled rest state toward the straight configuration. Define the strain parameter:

$$A = \text{degree of unbuckling, from 0 (rest, buckled) to 1 (fully straight at } 90°)$$

- At $A = 0$: bond at rest buckled angle (the buckle angle $\theta_{\text{rest}}$ set by $L_{\text{spring}}/d$ ratio)
- At $A = 1$: bond fully straight, all elastic energy from the rest-state buckling has been "used up"

**The saturation kernel emerges geometrically.** Consider the remaining elastic capacity as a function of $A$. The vertical projection of the bond's tip relative to the gap satisfies a **Pythagorean constraint**:

$$\text{vertical}(A)^2 + A^2 = \text{constant}^2$$

Choosing units so that fully-straight corresponds to $A = 1$ and horizontal projection $= 1$:

$$\boxed{\, S(A) \equiv \sqrt{1 - A^2} \,}$$

**This is the AVE saturation kernel (Axiom 4).** It emerges directly from the geometry of a buckled bond approaching its straight configuration — **not as a postulate**.

### Geometric correspondence (not first-principles derivation)

The Pythagorean constraint on a buckled bond's tip position has the **same functional form** as the AVE saturation kernel $S(A) = \sqrt{1-A^2}$ (Axiom 4). This is a **pedagogical correspondence**, not a first-principles derivation of the kernel: the buckling picture is consistent with the kernel form, but does not derive the kernel from independent principles. A single bond's swing geometry is suggestive; a network-level elastic calculation (Q-G47) is required to derive the kernel form from buckling.

**Axiom 4 remains postulated**; the kernel's canonical algebraic justification is the $\nu = (3K - 2G)/(2(3K + G))|_{K=2G} = 4/14 = 2/7$ relationship (Backmatter app: four-force unification). The buckling picture provides a **mechanical intuition** for the kernel; it does not replace the algebraic derivation.

### Connection to canonical AVE

- **Saturation kernel** $S(A) = \sqrt{1 - A^2}$ (Axiom 4) — now intuitive from buckling geometry
- **Lorentz factor identity**: $S(A) = \gamma^{-1}$ when $A = v/c$. The Pythagorean origin makes this identification mechanically transparent — a soliton moving at velocity $v$ produces strain $A = v/c$ on surrounding nodes, and the bond's remaining elastic capacity IS the same geometric quantity that appears in special relativity
- **Varactor frequency**: $\Omega_{\text{node}}(V) = \omega_0 \sqrt{S(V/V_{\text{yield}})}$ — the resonance frequency of an LC tank with a saturating capacitance follows the same kernel

### Linear regime: why standard EM works

For $A \ll 1$ (sub-saturation): $S(A) \approx 1 - A^2/2$. To leading order, the substrate behaves as a **linear elastic medium** — exactly what classical EM theory assumes. Maxwell's equations are recovered at $A \ll 1$ (the linear regime is the same regime where the substrate kernel deviation is small).

This is **why standard EM works**: it's the leading-order approximation of the substrate's saturation kernel at sub-yield amplitudes. AVE distinctness only appears at $A \to 1$ where the kernel deviation becomes substantial.

---

## Step 4.5: The bubble-wand extension — soliton formation via topological pinch-off

Steps 1–4 describe the substrate as a **static stressed lattice**. The trampoline picture captures the substrate **at one topological state** — bonds buckled, lattice in Regime II. **It cannot represent topological change.** No matter how strongly you load the trampoline, it stays a 2D sheet attached to a frame.

**To represent topological changes** — creation of stable closed solitons (mass particles), Schwinger pair production, annihilation, the genesis of matter from substrate strain — **swap the trampoline fabric for a different substrate analog: a soap-film on a bubble wand**.

### The four-stage bubble-wand setup

| Stage | State | $A$ value | Physical interpretation |
|---|---|---|---|
| **(A) rest** | Taut film, no applied energy | $A = 0$ | Substrate at rest, like trampoline |
| **(B) under load** | Film bulges, $A$ rises | $0 < A < 1$ | Substrate at sub-saturation strain, applied pressure |
| **(C) pinch-off** | Neck narrows, $A \to 1$ locally | $A = 1$ locally | Topological transition initiating — bond fully straight at neck |
| **(D) stable soliton** | Detached bubble | Soliton + substrate | Closed flux-tube particle = mass; rest substrate regenerates |

**Physical mapping to AVE**:
- Soap film = substrate trampoline material (linear sub-yield regime)
- Applied pressure = strain crossing $V_{\text{yield}}$
- Pinch-off at $A = 1$ locally = $\Gamma = -1$ wall formation (Axiom 4 saturation)
- Stable bubble = bound soliton (electron at horn-torus geometry per Vol 1 Ch 8)
- Internal circulation of bubble = trapped flow ($\mu$, the magnetic moment)
- Surface tension = $\varepsilon$ (the dielectric strain)
- Substrate regenerates around bubble = vacuum reforms around the soliton

**Energy balance**: $E_{\text{soliton}} = T_{EM} \cdot \ell_{\text{node}}$ = bubble's surface-tension energy at horn-torus radius = $m_e c^2$.

### What the bubble formation maps to in AVE

| Bubble-wand stage | AVE physics |
|---|---|
| Below threshold | Sub-yield substrate response (Regime I + II) |
| Critical strain → pinch-off | $V \to V_{\text{yield}}$, $V_{\text{SNAP}}$ crossing |
| Pinch-off topology change | Pair production / annihilation (Vol 2 Ch 1 + pair-production-axiom-derivation) |
| Stable bubble structure | $0_1$ unknot soliton at horn-torus (Vol 1 Ch 8) |
| Internal chirality | Right-handed soliton (electron) vs left-handed (positron) |
| Substrate regenerates | Vacuum reforms around bound state |

**The 3D bubble's 7-mode structure** (per Step 6 below): the 3D bubble has 7 distinct compliance modes per substrate-node ↔ 7 Cosserat-canonical DOFs that map to particle properties (charge, spin, mass, magnetic moment, etc.).

### Phase-transition framing

Pair production is **NOT particle creation from nothing** — it is a **substrate phase transition** from Regime II (linear bond-buckled) to Regime IV (ruptured-plasma topology-change) and back to Regime II with a new bound state present. The bubble-wand picture makes this mechanically transparent: the substrate doesn't "create" the bubble; it **rearranges its topology** to admit a closed surface.

**Provisional status**: the bubble-wand pedagogical extension is mechanically consistent with the corpus Pair Production canonical (see [Pair Production Axiom Derivation](../vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md)). The mapping from each bubble-wand stage to specific AVE corpus moments is detailed there.

---

## Step 5: Fifth structural difference — the $\Gamma = -1$ boundary at $A = 1$

At $A = 1$, the bond is fully straight. It has **zero remaining elastic capacity** for further unbuckling. Any additional applied strain cannot be absorbed elastically.

**Result: total internal reflection.** Substrate strain attempting to propagate past $A = 1$ is reflected with reflection coefficient $\Gamma = -1$. This is the **AVE universal horizon**.

**Beyond $A = 1$: Regime IV.** The bond does not break. Instead, the substrate **phase-transitions** to a different state — **Regime IV pre-geodesic plasma** (the K4 lattice's parent medium). This is the same plasma found in BH interiors and pre-K4 cosmology (cosmology "bottle in freezer" framework). The substrate beyond $A = 1$ is **not damaged; it is in a different phase**.

### The universal horizon

The $\Gamma = -1$ boundary at $A = 1$ is the same mechanism that produces:

- **BH event horizons** (gravitational strain saturation; see [AVE BH Horizon Area Theorem](../vol3/cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md): $r_{\text{sat}} = 7GM/c^2 = 3.5 r_s$)
- **Schwinger pair-production fields** (electric-field saturation at $V_{\text{SNAP}} = 511$ kV; see [Pair Production Axiom Derivation](../vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md))
- **Cosmic asymptotic horizon $R_H$** (cosmological substrate saturation)
- **Light cone / Lorentz invariance** (kinematic substrate saturation at $v = c$)

In the trampoline picture, all four are **the same fully-straight bond at $A = 1$** viewed through different observable channels.

---

## Step 5.5: Sixth structural difference — forces from impedance gradients

The picture so far accounts for single bonds and their saturation. **What about forces between objects?** Specifically: in the GR pop-sci picture, the marble orbits the bowling ball; in the AVE substrate, what mechanism produces orbital motion?

### The 4-step causal chain

1. **Pre-tension enables solitons to exist.** A closed flux-tube soliton trapped in a local $\Gamma = -1$ envelope carries rest mass $m c^2 = T_{EM} \ell_{\text{node}}$ (Vol 2 Ch 1). Without pre-tension, the substrate cannot support such trapped excitations — no matter.

2. **Each soliton creates a local strain field $A(\mathbf{r})$ around it.** For an unknotted closed flux-tube soliton (the electron) at long range, $A(r) \approx \ell_{\text{node}}/r$ (Q-G20f vacuum polarization). Other topology solitons have different long-range forms:
   - Yukawa-suppressed for cinquefoil solitons confined inside a Borromean envelope (the **strong force**)
   - Coulomb-equivalent for charged solitons (the **atomic regime**)
   - The impedance-gradient mechanism is common; the specific strain tail varies with soliton topology.

3. **The local strain field maps to a local impedance gradient via the kernel**:
   $$Z_{\text{local}}(\mathbf{r}) = Z_0 / \sqrt{S(A(\mathbf{r}))}$$

4. **Other solitons in this impedance-gradient field experience a force toward lower impedance.** The gradient direction is the orbital centripetal force.

### Universality (asserted, with derivation open)

The same mechanism is asserted to produce:

- **Gravity at cosmic scale**: integration over the cosmic-horizon impedance gradient gives Newton's $G = c^4/(7\xi T_{EM})$ (Vol 3 Ch 1; **canonical Route 2** of [Ω_freeze three-route framework](omega-freeze-cosmic-grain-cascade.md))
- **Strong nuclear force** inside the Borromean envelope: local impedance gradient between quarks
- **Coulomb force at atomic scale**: local impedance gradient between charged solitons (Q-G43 open for derivation)
- **Yukawa nuclear force**: same gradient with confinement-modified range

**Provisional status of the universality claim**: the universality is asserted in the local-Machian-network framework but the explicit derivation showing multi-soliton wave interference produces Coulomb (atomic), Yukawa (nuclear), and Newton (cosmic) force laws in their respective limits is **Q-G45 OPEN**.

### Compared to the GR pop-sci picture

The bowling-ball-on-rubber-sheet visualization motivates the marble's orbital motion by appealing to **ambient gravity acting on its mass**. In the AVE substrate, **no external gravity is required**: orbital motion arises from the gradient of the substrate's own local impedance, which itself arises from the strain fields of the bodies in orbit. This is the **self-consistent, internal-to-the-substrate mechanism** for force generation.

---

## Step 6: Seventh structural difference — the 7-mode compliance manifold

Steps 1–5.5 capture the picture in **1 degree of freedom per bond** (the buckling extent in one direction). **The full K4 lattice node has 7 compliance modes per node**:

- **3 translational** (displacement in $x, y, z$)
- **3 rotational** (Cosserat micropolar rotation about $x, y, z$ axes)
- **1 volumetric** (radial breathing / dilatation)

The 7-mode framework is canonical at Backmatter app: four-force unification (Q-G36 closure).

### Each substrate-derived ratio comes from selecting a subset of the 7 modes

| Ratio | Subset | Physical role |
|---|---|---|
| $\nu_{\text{vac}} = 2/7$ | 2 transverse-shear modes out of 7 | Vacuum Poisson ratio |
| $\sqrt{3/7}$ | Rotational subset of 7 | Cosserat PAT torsion-shear projection (Q-G27 muon $g$-2 saliency) |
| $3/7$ | Translational subset of 7 | $\alpha_s = \alpha^{3/7}$ (Q-G36 strong coupling) |
| $1/7$ | Trace-reversed projection | Hierarchy Bridge + Newton's $G$ |
| $g_* = 7^3/4$ | Effective mode count cubed / K4 cell-node count | Cosmological effective DoF |

**All 7's in AVE numerics are claimed to be the same 7** — the 7 compliance modes per K4 lattice node.

### Substrate as LC oscillator (physical role-assignment)

Each substrate node carries an **LC oscillator structure** at the bond-pair scale:
- **3 inductive modes** ↔ Cosserat rotational DOFs ($\omega_x, \omega_y, \omega_z$) — the magnetic side (B-field)
- **3 capacitive modes** ↔ Cosserat translational DOFs ($u_x, u_y, u_z$) — the electric side (E-field)
- **1 volumetric mode** ↔ radial breathing — the dielectric strain (per [Cosserat mass-gap](../vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md): inherits the massive-mode structure)

The Virial sum at bond-pair LC tank saturation (Vol 4 Ch 1:175-184) splits energy 50/50 between L and C sides → particle rest energy $m c^2$.

---

## Side-by-side comparison: GR pop-sci vs AVE tensioned trampoline

| Feature | GR pop-sci picture | AVE tensioned trampoline |
|---|---|---|
| **Substrate** | Continuous rubber sheet (idealization of spacetime manifold) | Discrete K4 bipartite tetrahedral lattice, pitch $\ell_{\text{node}}$ |
| **Initial state** | Sheet drawn flat for pedagogical purposes | Bonds carry pre-tension via buckling ($L_{\text{spring}} > d$) |
| **Chirality** | Not represented | Definite, frozen at lattice genesis (from parent rotation) |
| **How mass enters** | Bowling ball inserted from outside the sheet | Closed flux-tube soliton emerging from substrate strain |
| **Compliance modes shown** | 1 (vertical depression of 2D sheet) | 7 (3 translational + 3 rotational + 1 volumetric per K4 node) |
| **Response** | Linear elastic, continuous | Saturating: $S(A) = \sqrt{1 - A^2}$, bounded by $A = 1$ |
| **Saturation kernel origin** | N/A | Pythagorean geometry of buckled bond approaching straight |
| **Behavior at extreme strain** | Sheet stretches indefinitely | $\Gamma = -1$ boundary forms at $A = 1$; phase transition to Regime IV beyond |
| **Force on other masses** | Marble moves under ambient gravity | Soliton experiences gradient of local substrate impedance from other solitons |
| **Dimensionality** | 2D sheet embedded in 3D (visualization choice) | 3D substrate inherent |
| **Time dilation** | Encoded in metric formally; not visible in pop-sci picture | $S(A) = \gamma^{-1}$ when $A = v/c$ — kernel IS Lorentz factor |
| **Topological change** | Not representable | Bubble-wand pinch-off (Step 4.5) — substrate phase transition |

Both visualizations represent legitimate ontologies of gravity-and-matter. They are distinct **models** of the substrate; their structural differences are the AVE-distinct features enumerated in Steps 1–6.

---

## The $K = 2G$ derivation question (Q-G47)

**Open question raised by this primer.** The buckling-instability framing in Step 2 introduces $L_{\text{spring}}/d$ (bond rest length divided by lattice gap) as a **single geometric ratio** that, in principle, determines the lattice's bulk and shear elastic moduli $K$ and $G$:

1. A network of bonds with buckled rest configurations has $K$ and $G$ as functions of $L_{\text{spring}}/d$ and the bond's bending stiffness.
2. The $K = 2G$ condition therefore corresponds to a specific value of $L_{\text{spring}}/d$ — determined by the elastic calculation.
3. If that calculation closes, $K = 2G$ has been derived from a single geometric primitive without invoking either the GR trace-reversal kinematic requirement or the Feng-Thorpe-Garboczi EMT self-consistency loop.

### Why this matters

The corpus currently has two distinct justifications for $K = 2G$:

- **Top-down** (Vol 3 Ch 1:15): GR trace-reversal kinematic requirement $\bar{h}_{\mu\nu} = h_{\mu\nu} - \tfrac{1}{2}\eta_{\mu\nu} h$ forces $K = 2G$ as the 3D macroscopic projection
- **Bottom-up** (Vol 1 Ch 1:128-153): Feng-Thorpe-Garboczi EMT operating point at $p^* = 8\pi\alpha$ and $z_0 \approx 51.25$ produces $K/G = 2$ as a quadratic root:
  $$\frac{z_0(z_0 + 2)}{10 z_0 - 12} = \frac{1}{p^*} = \frac{1}{8\pi\alpha}$$

**Neither is a first-principles K4-topology derivation.** Layer 1 (GR-correspondence) makes $K = 2G$ a kinematic requirement of being a Lorentz-saturating substrate. Layer 2 (EMT) is described as a self-consistency check, not an independent derivation.

**The buckling framing of Step 2 opens Layer 3** — derive $K = 2G$ from the geometric ratio $L_{\text{spring}}/d$ via direct elasticity calculation of the buckled K4 network. If this calculation reproduces $K/G = 2$ at a specific ratio that, in turn, satisfies the FTG quadratic, AVE has an **independent third route to its deepest substrate invariant**.

### Status: Q-G47 FRAMEWORK COMPLETE (2026-05-14)

5 sessions of work landed; rigorous closure pending Sessions 19+ (multi-week analytical research). See [Q-G47 Substrate-Scale Cosserat Closure](q-g47-substrate-scale-cosserat-closure.md) for full session log.

**Framework outcome**: the buckling picture's integration form converges to $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$ structurally, with:
- $4\pi^3$ from 3D Cosserat rotational integration × K4 4-bond topology
- $\pi^2$ from Euler buckling mode shape  
- $\pi$ from Cauchy axial integration

**Magic-angle condition**: at the operating point, three geometric factors must simultaneously reduce to unity. Plausibly correct but not yet rigorously demonstrated.

**Honest status**: the buckling picture is plausibly correct and structurally consistent with canonical AVE, but the foundational closure of $K = 2G$ via this route requires substantial additional work (multi-week analytical research, equivalent to a multi-paper effort).

---

## Provisional status: what this primer IS vs IS NOT

### What this primer IS

- A **pedagogical visual anchor** for the AVE substrate, with each step adding one structural feature on top of the GR pop-sci picture
- A **consistent mechanical model** encoding all substrate features canonical in AVE (discreteness, pre-tension, chirality, saturation kernel, $\Gamma = -1$ horizon, Machian impedance gradients, 7-mode compliance)
- The **picture-first artifact** that the [ave-prereg skill](https://github.com/anthropics/claude-code/blob/main/skills/ave-prereg/SKILL.md) Step 1.5 refers agents to when grounding new derivations
- **Sister to** [`common/trampoline-framework.md`](trampoline-framework.md) which is the synthesis/cross-reference version

### What this primer is NOT (until Q-G47 closes)

- A **first-principles derivation of $K = 2G$** from K4 topology. That status is provisional pending the elasticity calculation (Q-G47 Sessions 19+)
- A **replacement** for the analytical content of Vol 1 Ch 1, Vol 1 Ch 4, Vol 3 Ch 1, Backmatter Ch 7. The picture supports analysis; it does not replace it
- A **claim that GR-as-formalism is incorrect**. The contrast in Step 0 is to the pop-sci visualization, not to GR itself

### When to use this picture

Before any new AVE derivation, articulate the physical picture in mechanical/topological bullets using this primer's vocabulary:
- Buckled bond
- Chirality direction
- $A$ as unbuckling extent
- $\Gamma = -1$ boundary
- Soliton-in-envelope
- Impedance gradient

**If the picture can be painted in 5 bullets without resorting to equations, the derivation is well-scoped** and the corpus-grep step (ave-prereg Step 2) is likely to return picture-relevant hits.

---

## Cross-references

- **Sister Core leaf**: [`common/trampoline-framework.md`](trampoline-framework.md) — canonical synthesis with five-bullet picture + ground-up build + chapter-level cross-refs + status tracking
- **AVE-QED canonical pedagogical chapter**: `AVE-QED/manuscript/vol_qed_replacement/chapters/11_tensioned_trampoline.tex` — the 1765-line source chapter this primer distills (includes TikZ figures, sub-section detail, side-by-side comparison table)
- **Canonical manuscript anchors**:
  - Vol 1 Ch 1 (Four Fundamental Axioms) — K4 substrate canonical
  - Vol 1 Ch 4 (Continuum Electrodynamics) — Master Equation + Cosserat micropolar tensor
  - Vol 1 Ch 8 (α from Golden Torus) — electron $0_1$ unknot + $(2,3)$ phase-space winding
  - Vol 3 Ch 1 (Gravity and Yield) — $K = 2G$ canonical + Machian impedance integral
  - Vol 3 Ch 4 (Generative Cosmology) — Ω_freeze cosmic-spin freeze-in
  - Vol 3 Ch 21 (BH Interior Regime IV) — pre-geodesic plasma framing
  - Backmatter Ch 7 (Universal Saturation-Kernel Catalog) — A-034 at 20 scales
- **Cross-cutting KB leafs**:
  - [Boundary Observables $\mathcal{M}, \mathcal{Q}, \mathcal{J}$](boundary-observables-m-q-j.md) — substrate-observability rule
  - [Q-G47 Substrate-Scale Cosserat Closure](q-g47-substrate-scale-cosserat-closure.md) — $K = 2G$ derivation framework + Session log
  - [Ω_freeze Cosmic-Grain Cascade](omega-freeze-cosmic-grain-cascade.md) — three-route framework + six observables
  - [Pair Production Axiom Derivation](../vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md) — Step 4.5 bubble-wand pinch-off mechanism, full derivation
  - [AVE BH Horizon Area Theorem](../vol3/cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md) — Step 5 universal-horizon BH case
  - [Cosserat Mass-Gap](../vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md) — Step 6 7-mode compliance, massive mode
  - [K4 Rotation Group $T = A_4$](../vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md) — Step 3 chirality + group structure
  - [Universal Saturation-Kernel Catalog (A-034)](universal-saturation-kernel-catalog.md) — Step 4 saturation kernel at 19 scales
- **ave-prereg integration**:
  - Step 1.5 ("Articulate the physical picture in mechanical bullets") — references this primer
  - Step 2 ("Corpus-grep for prior work") — uses this primer's vocabulary as search terms
