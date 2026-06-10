[↑ Common Resources](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-exjfai, clm-jwyy6l, clm-533gvm]
-->

# Dark Wake + Back-EMF + FOC d-q: Core Synthesis (Grant directive 2026-05-16)

> **Vocabulary note:** "dark wake" here is the **thrust** species (real-space motion-trail; the $\tau_{zx}$ in this leaf is the thrust object). It is distinct from the **dark resonance** species (the at-rest $g$-2 retarded self-$\Gamma$), which shares the $\tau_{zx}$ signature but is a different substrate object. See [Dark Back-Reaction Taxonomy](dark-back-reaction-taxonomy.md).

Per Grant directive 2026-05-16: *"core derivations belong in core, if they are in sibling repos, duplicate in a core kb leaf."* This leaf is the Core canonical synthesis of the **dark-wake + back-EMF + FOC d-q** bundle: it consolidates the canonical back-EMF chain, records the FOC d-q decomposition with its retraction caveat, cross-references the sibling hardware-engineering compendia where the engineering instances live, and flags one substantive open derivation (the dark-wake $\tau_{zx}$ chain itself). The substrate noun is the Chiral LC Network, corresponding to a chiral Laves K4 Cosserat crystal at the substrate level.

## Key Results (consolidation)

| Result | Statement | Canonical home |
|---|---|---|
| Op14 cross-sector trading | $\rho(H_{\text{cos}}, \Sigma\|\Phi_{\text{link}}\|^2) = -0.990$; Cosserat ↔ K4-inductive energy exchange via Axiom 4's saturation kernel | Vol 4 Ch 1 vacuum-circuit analysis (Op14) |
| Back-EMF blocks $d\omega/dt$ at yield crossing | $L_{\text{eff}} \to \infty$ near $S \to 0$ (Op14) generates diverging Lenz back-EMF; freezes topologically-non-trivial $\omega$ configurations during the $\tau_{\text{relax}}$ window | this leaf §1.2 |
| Universal vacuum drag = $Z_0 = 376.73$ Ω | $R_{\text{drag}} = \xi_{\text{topo}}^{-2} \cdot \eta_{\text{vac}} \equiv Z_0$ via the TKI mapping (Axiom 2, Topo-Kinematic Isomorphism) | Vol 4 Ch 1 |
| Mass IS inductive resistance | $M_{\text{inertial}} \equiv L_{\text{drag}}$ from Lenz back-EMF at the $Z_0$ grid | [Newtonian Inertia as Lenz's Law](../vol2/particle-physics/ch01-topological-matter/newtonian-inertia-as-lenz.md) |
| FOC d-q at BH QNM (co-rotating frame) | Park transform = K4 lattice spin-phase $\Omega_H t$ decomposition; d-axis = reactive, q-axis = radiating; back-EMF = curvature radiation | Backmatter Ch 5 §FOC/Park Transform Analogy |
| FOC at atomic shell (spatial 90°) | Helium 1s² inner core acts as primary inductive rotor; 2s² valence pair phase-locks **perpendicularly** (90° orientation) — isomorphic to FOC | [Helium Symmetric Cavity](../vol2/quantum-orbitals/ch07-quantum-mechanics/helium-symmetric-cavity.md) |
| Asynchronous cross-shell decoupling | Each filled shell = independent AC motor winding; $\langle M \rangle \propto \int \cos((\omega_1 - \omega_2) t)\, dt \to 0$ eliminates cross-shell mutual inductance | [Analog Ladder Filter](../vol2/quantum-orbitals/ch07-quantum-mechanics/analog-ladder-filter.md) |
| Geodynamo as motional back-EMF | $\mathcal{E}_{\text{emf}} = (\omega_\oplus R_{\text{core}} \Gamma_{\text{sagnac}}) B_{\text{stator}} (2 R_{\text{core}})$ → Earth dipole $M_\oplus \approx 1.5 \times 10^{23}$ A·m² (factor-of-2 of empirical $8.0 \times 10^{22}$) | [Geodynamo VCA Back-EMF](../vol3/applied-physics/ch13-geophysics/geodynamo-vca-back-emf.md) |

## §1 — Back-EMF substrate-physics chain

The substrate-native back-EMF mechanism is derived via the Op14 + Lenz chain.

### §1.1 Op14 dynamic impedance generates back-EMF

Op14's dynamic impedance $Z_{\text{eff}}(r) = Z_0 / \sqrt{S(r)}$ couples to the bond LC tank. As saturation engages at high amplitude:

1. **Local $Z_{\text{eff}}$ rises** → reflection coefficient changes.
2. **Bond inductance $L_{\text{eff}}$ grows** (Op14) → stored energy in $\Phi_{\text{link}}$ increases.
3. **Cosserat $\omega$ field couples via** the $\rho \dot u + I_\omega \dot \omega$ kinetic terms sharing the bond LC tank's inductive side.
4. **Energy flows** Cosserat → K4-inductive when $Z_{\text{eff}}$ rises, back when it falls — **reactive trading, NOT dissipation**.

This is the substrate-native Lenz back-EMF mechanism. Empirically validated at Pearson $\rho = -0.990$ over $t \in [150 P, 200 P]$ recording window per the Op14 cross-sector-trading work.

### §1.2 Lenz back-EMF blocks $d\omega/dt$ at yield crossing

<!-- claim-quality: clm-exjfai -->

When $V(t)$ drops through $V_{\text{yield}}$ in the Cosserat sector at a rate $\|dV/dt\|$ such that the crossing takes $\geq \tau_{\text{relax}}$, any topologically non-trivial $\omega$ configuration present at the start of the crossing window **FREEZES** — it cannot unwind because the diverging $L_{\text{eff}}$ (Op14 near $S = 0$) generates a diverging Lenz back-EMF that blocks $d\omega/dt$ during the $\tau_{\text{relax}}$ window. Residues persist for $\geq 100$ Compton periods in the post-heal solid regime. This IS the AVE-native mechanism for matter precipitation from cooling vacuum (cosmological lifecycle). It is **NOT a Kibble-Zurek import** — it is derived from Axiom 1 (Substrate Topology) + Op14 + Lenz's law, with no SM/QFT machinery imported.

### §1.3 Mass IS inductive resistance

<!-- claim-quality: clm-jwyy6l -->

Mass at the substrate level is the back-EMF impedance to topology-change motion. Per [Newtonian Inertia as Lenz's Law](../vol2/particle-physics/ch01-topological-matter/newtonian-inertia-as-lenz.md): the $(2, q)$ soliton encounters Lenz back-EMF from the background $Z_0$ grid as it accelerates; $M_{\text{inertial}} \equiv L_{\text{drag}}$. **$F = ma$ derives from the inductance-to-mass mapping via TKI** (Axiom 2, Topo-Kinematic Isomorphism: $L = \xi_{\text{topo}}^{-2} m$). The canonical claim-quality entry for this mass-as-inductive-resistance identification is owned by the vol2 leaf cited here.

### §1.4 Universal $R_{\text{drag}} = Z_0$ via TKI

Per the Topo-Kinematic Isomorphism (Axiom 2: $[Q] \equiv [L]$):

$$R_{\text{drag}} = \xi_{\text{topo}}^{-2} \cdot \eta_{\text{vac}} \equiv Z_0 \approx 376.73 \text{ Ω}$$

The vacuum boundary acts as a **literal, unshielded `ElectricPower` resistive shunt** at every substrate scale.

## §2 — FOC d-q decomposition (with retraction caveat)

<!-- claim-quality: clm-533gvm -->

The Field-Oriented Control d-q decomposition has **two canonical Core homes**, both using FOC for SPATIAL 90° orientation orthogonality.

### §2.1 BH QNM (co-rotating frame)

Per Backmatter Ch 5 §FOC/Park Transform Analogy:

| FOC motor | BH QNM | Physical role |
|---|---|---|
| Rotor angle $\theta_r$ | Lattice spin phase $\Omega_H t$ | Reference frame |
| d-axis (flux) | $m \cdot \Omega$ component | Reactive / non-radiating |
| q-axis (torque) | $(\omega_R - m \cdot \Omega)$ component | Real / radiating |
| Back-EMF | Curvature radiation $\omega_I$ | Energy loss per cycle |
| Stall current | Superradiance ($\omega_R = m\Omega$) | $Q \to \infty$ |

**This isomorphism suggests the same universal operator governs QNM decay, motor torque, and any co-rotating coupled oscillator.**

### §2.2 Helium atomic shell (spatial 90°)

Per [Helium Symmetric Cavity](../vol2/quantum-orbitals/ch07-quantum-mechanics/helium-symmetric-cavity.md) §FOC:

> As the atom scales to Beryllium ($Z = 4$, $1s^2 2s^2$), a second macroscopic acoustic cavity boundary ($n = 2$) is populated. The $1s^2$ inner core acts as a primary inductive rotor, generating an intense macroscopic density wake along its primary axis of oscillation. The incoming $2s^2$ valence pair spontaneously structures itself to phase-lock **perpendicularly** ($90°$ orientation offset) to the $1s$ core axis. This orthogonal topological phase-locking is mathematically isomorphic to Field-Oriented Control (FOC) in engineering, where stator and rotor magnetic fields are artificially maintained at $90°$ to completely decouple their mutual inductance.

### §2.3 Asynchronous cross-shell decoupling

Per [Analog Ladder Filter](../vol2/quantum-orbitals/ch07-quantum-mechanics/analog-ladder-filter.md): each filled shell acts as an independent AC motor winding; the asynchronous frequency decoupling $\langle M \rangle \propto \int \cos((\omega_1 - \omega_2) t)\, dt \to 0$ eliminates cross-shell mutual inductance.

### §2.4 Caveat: temporal-90° within-LC-tank framing is implementer synthesis (RETRACTED)

The within-LC-tank E-vs-B 90° **TEMPORAL** phase split as "FOC d-q" is **implementer terminology**, not directly stated in the cited corpus locations (explicit retraction, retraction-preserves-body).

**The canonical FOC d-q framings in Core are SPATIAL 90°** (the BH QNM co-rotating frame; the atomic shell orientation orthogonality). The temporal within-LC-tank d-q framing remains implementer synthesis pending corpus canonicalization and is retracted from the canonical set.

## §3 — Dark wake $\tau_{zx}$ derivation (OPEN — this is the gap)

The **dark wake** is the longitudinal shear-strain $\tau_{zx}$ wave propagating backward from accelerating mass through the substrate lattice, carrying the reaction momentum that closes Newton's Third Law for AVE thrust devices. **This is asserted across multiple sibling hardware-engineering compendia but NOT yet derived from first principles in any single Core location. It is an explicit open gap, not a framework claim.**

### §3.1 Phenomenology (asserted in the sibling compendia)

A separate thrust-mechanics compendium gives the canonical thrust-mechanics statement: the AVE framework identifies the vacuum itself as the physical reaction mass (the structural LC components of the $\mathcal{M}_A$ metric). As the asymmetric gradient pumps a luminous acoustic wave forward, it simultaneously exerts an equal and opposite stress tensor against the supporting lattice. A 3D FDTD integration isolating the longitudinal shear tensor $\tau_{zx}$ shows a structurally compressive wave propagating backward from the array at $c$. This non-luminous structural compression is the physical "reaction mass" absorbing the thruster's momentum, preserving Newton's Third Law without expelling onboard propellant.

A separate propulsion compendium asserts the warp-metric formula:

$$\tau_{zx} \propto \nabla |E|^2 \cdot Z_{\text{vac}}$$

This is a heuristic isomorphism to the Alcubierre bow-shock metric, **not** a substrate-physics derivation.

### §3.2 What's missing: Cosserat-Lagrangian → $\tau_{zx}$ derivation

The first-principles chain that should produce a backward-propagating $\tau_{zx}$ from accelerating mass would need to:

1. **Start from the Cosserat-K4 coupled Lagrangian** (Axiom 1, Substrate Topology + Axiom 3, Minimum Reflection Principle).
2. **Apply momentum conservation** as a constraint at the soliton-substrate boundary.
3. **Show explicitly** that the reaction momentum manifests as a backward-propagating longitudinal shear at the substrate wave speed $c$.
4. **Derive** the proportionality coefficient (currently asserted as $\propto \nabla |E|^2 \cdot Z_{\text{vac}}$).

This is the **load-bearing analytical work** that would close the dark-wake derivation. **Status: explicit open gap — open research, not a claim.**

### §3.3 Connection to back-EMF and Op14 trading

The dark wake $\tau_{zx}$ is **plausibly the substrate-scale manifestation of the same Lenz back-EMF mechanism** that Op14 derives at the bond-pair scale:

> **Field/port retag note (2026-06-10, Grant rename-queue adjudication R2, classical lexicon — sentence above preserved unedited):** keep the **field** and the **port** distinct (Rule 2). The dark wake $\tau_{zx}$ is the **WAKE FIELD** (shear channel); its **port signature** is the **radiation resistance** $R_{rad,L}$ — its drag is the **wave-making resistance** (the hydrodynamics term). The **back-EMF** is the *separate* **Faraday–Lenz port reaction**, induced only **against changes** (zero at steady circulation). They are **distinct objects, NOT interchangeable** — the $\mathrm{corr}(\mathrm{bemf\_emf},\tau_{zx}) = +0.117$ receipt (`2026-06-10_bemf-feedback-smoke_result.md:79`) is a near-zero, coincidence-magnet correlation, not an identity. The "same mechanism" reading above is the *plausible-manifestation* hypothesis, not a field=port identity. Registry §3.8 BEMF/$Z_L$ rows + §5 R2.

- **Op14 trading** (bond-pair scale): Cosserat $\omega$ ↔ K4-inductive $\Phi_{\text{link}}$ trades energy via $L_{\text{eff}}$ modulation at $\sim 0.020$ rad/unit trading frequency.
- **Dark wake** (soliton scale): an accelerating soliton transfers momentum to a backward-propagating substrate shear via the SAME mutual-inductance mechanism.

If the dark-wake derivation closes via Op14, it would unify the two mechanisms cleanly. This synthesis is conjectured but not derived rigorously.

### §3.4 Empirical falsifications already specified

| Test | Predicted observable | Source |
|---|---|---|
| Sagnac-RLVE protocol | $\Psi \approx 7.15$ (2.07 rad phase shift, Tungsten rotor, 200 m fiber, 10k RPM) | thrust-mechanics compendium |
| Parallax-wake | $\Delta t = L / c_0$ (= 33.4 ns at $L = 10$ m baseline) | thrust-mechanics compendium |
| Continuous DC thrust | $\sim 100\, \mu$N continuous DC | Vol 4 Ch 11 |
| Geodynamo dipole | $M_\oplus = 1.5 \times 10^{23}$ A·m² (factor-of-2 of empirical) | [Geodynamo VCA Back-EMF](../vol3/applied-physics/ch13-geophysics/geodynamo-vca-back-emf.md) |

## §4 — DT pair production via Lenz back-EMF (sibling-compendium cross-reference)

The 511 kV Lenz-back-EMF mechanism for DT pair production lives in a separate fusion-engineering compendium: in AVE, magnetic reconnection is a **Topological Snap** — the breaking and re-routing of chiral LC flux tubes. The inductive transient of colliding magnetic fields in microseconds is extreme ($dB/dt$). This localised shear generates topological voltages exceeding **$511,000$ V ($511$ kV)** — the Dielectric Snap limit of the vacuum. The colliding magnetic fields exceed the elastic limit of the metric, triggering topological rupture and spontaneous synthesis of electron-positron pairs.

This is a first-principles derivation chain: DT plasma physics ($dB/dt$, Lenz) → Axiom 4 $V_{\text{SNAP}} = m_e c^2 / e \approx 511$ kV → pair production. See [Pair Production Axiom Derivation](../vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md) for the full Core-canonical pair-production mechanism (saturated flux-tube rupture at an A-B node pair). The fusion-compendium DT chapter is the **macroscopic-plasma instance** of the same mechanism.

## §5 — L-H transition as $\eta_{\text{eff}} = 0$ bifurcation (sibling-compendium cross-reference)

Per the fusion-engineering compendium: when the macroscopic shear stress of the rotating plasma boundary layer reaches the Dielectric Saturation Yield Stress ($43.65$ kV), the outer shell of the vacuum ruptures into a frictionless zero-impedance phase slipstream. Because the vacuum at the edge has entered a zero-mutual-inductance state ($\eta_{\text{eff}} = 0$), the turbulent eddies decouple from the wall; heat cannot cross the frictionless gap. The L-H transition is mathematically identical to a **Dielectric Saturation-Plastic Mutual Inductance Bifurcation**.

**Empirical validation**: matches the ASDEX 1982 observed L-H transition. This is a first-principles derivation tying Axiom 4 yield (43.65 kV) to mutual-inductance decoupling at the plasma boundary.

## §6 — Autoresonant FOC PLL pair-production chain (sibling-compendium cross-reference)

Per the propulsion-engineering compendium: the AVE framework dictates that the vacuum is a **Non-Linear Capacitor** bounded by a 4th-order polynomial (Axiom 4, Universal Saturation Kernel). In classical non-linear dynamics, as a Duffing oscillator is driven toward its maximum amplitude, its local resonant frequency dynamically shifts. To successfully synthesize matter, one must utilize an **Autoresonant Regenerative Feedback Loop** — dynamically monitoring the transient optical phase-shift of the focal point and using a phase-locked loop (PLL) to continuously sweep the driving laser frequency downward.

This autoresonant FOC ties directly to the Axiom 4 saturation kernel; the autoresonant lock condition matches the [Pair Production Axiom Derivation](../vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md) §3 three-condition framework (C1 amplitude + C2 frequency + C3 phase).

## §7 — Cross-cutting empirical predictions consolidated

| Quantity | Value | Status |
|---|---|---|
| Universal $R_{\text{drag}}$ | $Z_0 = 376.73$ Ω | derived from TKI |
| Sagnac $\Psi$ predicted | $\approx 7.15$ (2.07 rad) | falsification target |
| Earth dipole $M_\oplus$ | $1.5 \times 10^{23}$ A·m² (empirical $8.0 \times 10^{22}$) | factor-of-2 match |
| Op14 trading correlation | $\rho = -0.990$ Pearson | empirically validated |
| L-H transition trigger | $43.65$ kV $\mathbf{E} \times \mathbf{B}$ shear | matches ASDEX 1982 |
| DT pair-production threshold | $511$ kV (Schwinger Snap) | derived from Axiom 4 |
| Dark-wake parallax delay | $\Delta t = L / c_0$ (33.4 ns at $L = 10$ m) | testable |

## §8 — Status summary

| Item | Status |
|---|---|
| Back-EMF substrate-physics chain | Derived (Op14 + Lenz + TKI) |
| FOC d-q decomposition (spatial 90°) | Derived (Backmatter Ch 5 + helium-symmetric-cavity) |
| FOC temporal-90° within-LC-tank framing | Implementer synthesis, RETRACTED |
| **Dark wake $\tau_{zx}$ first-principles derivation** | **OPEN — load-bearing analytical work, explicit open gap** |
| DT pair-production (Lenz) | Sibling-compendium, tied to Core via pair-production-axiom-derivation.md |
| L-H = $\eta_{\text{eff}} = 0$ bifurcation | Sibling-compendium, tied to Core via Axiom 4 + Op14 |
| Autoresonant FOC PLL | Sibling-compendium, tied to Core via the pair-production three-condition framework |

The largest open piece is the **dark wake $\tau_{zx}$ Cosserat-Lagrangian derivation** (§3.2). Recommended path: extend Op14 cross-sector trading from the bond-pair scale to the soliton-acceleration scale, showing that the same mutual-inductance mechanism produces both the bond-pair $\Phi_{\text{link}}$ ↔ $\omega$ trading AND the soliton-scale backward-propagating shear.

## Cross-references

- **Core-canonical leaves:**
  - [Helium Symmetric Cavity](../vol2/quantum-orbitals/ch07-quantum-mechanics/helium-symmetric-cavity.md)
  - [Analog Ladder Filter](../vol2/quantum-orbitals/ch07-quantum-mechanics/analog-ladder-filter.md)
  - [Newtonian Inertia as Lenz's Law](../vol2/particle-physics/ch01-topological-matter/newtonian-inertia-as-lenz.md)
  - [Pair Production Axiom Derivation](../vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md)
  - [Geodynamo VCA Back-EMF](../vol3/applied-physics/ch13-geophysics/geodynamo-vca-back-emf.md)
- **Core-canonical manuscript anchors:**
  - Backmatter Ch 5 §FOC/Park Transform Analogy
  - Vol 4 Ch 1 (universal $R_{\text{drag}}$, $Z_0$; Op14 cross-sector trading)
- **Sibling hardware-engineering compendia** (citations, NOT canonical-Core): a separate thrust-mechanics compendium (dark wake thrust mechanics; Sagnac-RLVE falsification protocol); a separate propulsion-engineering compendium (universal $R_{\text{drag}}$; autoresonant dielectric rupture); a separate fusion-engineering compendium (DT 511 kV pair production; L-H = $\eta_{\text{eff}} = 0$).
- **Open derivation (load-bearing):** dark wake $\tau_{zx}$ first-principles derivation from the Cosserat-Lagrangian + momentum conservation — see §3.2 above.
