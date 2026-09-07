[↑ Common Resources](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-exjfai, clm-jwyy6l, clm-533gvm]
-->

# Dark Wake + Back-EMF + FOC d-q: Core Synthesis (Grant directive 2026-05-16)

> **Title clarification (2026-06-10, Grant rename-queue adjudication R3 — H1 + filename preserved; this is a Rule-12 title note, not a rename).** The title lumps a **field** and a **port**; by the **antenna-zone taxonomy** this leaf actually covers four distinct objects, class-tagged per the dark-sector registry (`research/2026-06-10_field-symbol-registry.md`):
> - **(a) the wake FIELD** — far-field, **shear** channel ($\tau^{far}_{zx}$); the radiated dark wake. _Class: field (shear)._
> - **(b) the reactive NEAR-FIELD store** — the near-field reactive energy $X_L$ (non-radiating, stored). _Class: near-field reactance._
> - **(c) the PORTS** — radiation resistance $R_{rad,L}$ (wave-making drag), near-field reactance $X_L$, and the Faraday–Lenz **back-EMF** (the terminal Lenz reaction). These are **distinct port objects** (Rule 2: a port meters a field, it is not the field). _Class: ports._
> - **(d) the FOC d-q frame** — the drive/control rotating frame (with its retraction caveat). _Class: control frame._
>
> The **filename is kept** (link-stable — referenced across volumes). A filename rename (e.g. `dark-wake / BEMF-port / FOC synthesis`) is an **optional auditor follow-up** (link-breaking — noted, NOT done here). Registry §5 R3.

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

> **🔴 CONTESTED — dated demotion 2026-07-19 (Rule-12; the §1.2 body below is preserved VERBATIM, not edited).** Both load-bearing sub-claims of clm-exjfai are contested by an unbanked engine realization recovered in the 2026-07-19 branch scrub: the moving-front freeze-in arc (archive tag `archive/analysis/moving-front-freezein` @ `f647f58b`; result `research/2026-06-30_moving-front-freezein_result.md`) — the very simulation the register strengthen-by (`claim-quality.md`, clm-exjfai) requested ("Support the ≥100-Compton-period residue persistence with a simulation or decay-rate estimate"). What the run found:  <!-- rule12-freeze: base=f909e4e0028a02514d93fc5c1fa37b81d1d248dc region=below offset=3 lines=3 bytes=557 sha256=7299b8b734f88d2dabde1f08f4a28410708238d88540e8c4f6409b2319d5a398 -->
> - **Persistence — DEMOTED to CONTESTED (not refuted).** The engine's moving-front realization gave real-space ω-defect persistence of **≤ 3.04 Compton periods** (two-arm run: memristive `3.04 / 0.45 / 1.46` Cp at v_front `0.5 / 1.0 / 4.0`; bare `1.01 / 1.35 / 1.58` Cp; all `Q_end ≤ 1`) — **~30× short** of the "≥ 100 Compton periods" asserted below. Single named mechanism (Rule-11, quoted): "the re-solidified Cosserat solid is a **linear-elastic shear-wave medium with NO topological-pinning term**" (`_bulk_accel → _bare_linear_gradient`, `cosserat_field_3d.py:1999` per the result doc), so a bare ω-loop disperses (τ_disperse ≈ 0.23 Cp) once the front's saturation lifts.
> - **Why CONTESTED, not REFUTED (flag-don't-fix).** The result doc (§4 FLAG) frames this as an **OPEN A44 fork** — *either* an engine gap (the Ax1 topological-pinning term the corpus asserts is not implemented) *or* a corpus over-claim (Ax1 may not protect a bare non-soliton ω-loop) — and **explicitly declines to adjudicate**. And the negative is **resolution-limited** (N=12–16); the result doc's own §7 states it "should be re-confirmed at N≥32 in the engine_sim lane before it is promoted to a corpus verdict." So the persistence magnitude is contested by an engine result, not cleanly falsified.
> - **Direction — FLAGGED backwards-as-stated (routed to Grant/auditor; not resolved here).** The body below reads **slow → freeze** ("crossing takes ≥ τ_relax → FREEZES"). The arc's memristive-lag ODE derivation + two-arm run give the OPPOSITE — **fast crossing (Δt_cross ≲ τ_relax) → FREEZE, slow → HEAL** — with S_min rising monotonically with v_front (`0.04 → 0.19 → 0.56`, CONFIRMED). Per the result doc §1 the prose direction is "**BACKWARDS as literally stated**." Both directions surfaced verbatim; the auditor/Grant land any Rule-12 direction correction.
> - **Confirmed (the positive).** The memristive S-lag mechanism itself is rate-dependent exactly as derived (S_min `0.04→0.19→0.56` with v_front) — the mechanism operates; the LASTING real-space freeze is what fails.
>
> Confidence demoted `0.50 → 0.20` ⇒ derived solidity `0.30 → 0.20` (CONTESTED — held at the bottom of the "do not build on" band, deliberately NOT the <0.20 "refuted" band) in the register (`claim-quality.md`, clm-exjfai). Secondary index sites (`substrate-hysteresis-index.md` §1/§2) carry dated pointers to this note.

> **🔴 RULED 2026-07-20 (RULING 2 of the 2026-07-20 ratification batch — supersedes the CONTESTED status above for the BARE-loop branch; Rule-12 KEEP-BOTH: the §1.2 body below AND the CONTESTED banner above are both preserved verbatim).** Grant ratified this ruling 2026-07-20 (**Grant-verbatim, [sic]: "2 ratified"**); the ruling *content* is the **orchestrator's walk, ratified in chat** — attribution split: the detailed wording below is the ratified walk, NOT Grant-verbatim. Two dispositions + one scope:  <!-- rule12-freeze: base=bc6a7a09a8a4d7fab1b7f772f655883f7edb49d1 region=above offset=0 lines=7 bytes=2459 sha256=8779ddd591480aab5e58d19831baba1b980122e0beedbacd4d244383964bccbc -->
> - **DIRECTION — RULED fast→freeze (the body's slow→freeze prose is BACKWARDS on its own mechanism).** Mechanism = **limited saturation time**: $\tau_{\text{relax}}$ is the state's *slew limit*. Circuit picture = **sample-and-hold** — a **fast** sweep *holds/quenches* the configuration (no time to relax across the crossing window), a **slow** sweep *tracks/anneals* it (the state follows the moving operating point and heals). The engine's monotone **$S_{\min}$-vs-$v_{\text{front}}$** rise (`0.04 → 0.19 → 0.56`) is the receipt: faster fronts leave *less* saturation-relaxed, deeper-frozen state. The §1.2 body reads "crossing takes $\geq \tau_{\text{relax}}$ → FREEZES" (slow→freeze), which is backwards on the very $\tau_{\text{relax}}$-as-slew-limit mechanism it names.
> - **PERSISTENCE — RULED REFUTED-AS-STATED for BARE $\omega$-loops (demotes CONTESTED → REFUTED, scoped).** The seed-controlled **N≥32** discharge (`research/2026-07-19_moving-front-freezein_landing-addendum.md` §2.1; all $\leq$ 3.264 Cp, ~30× short of the "$\geq 100$ Compton periods" asserted below) closes the resolution-limit caveat the CONTESTED banner rested on: **nothing pins a bare $\omega$-loop in a linear-elastic bulk** — consistent with the localization-is-boundary settlement (a bare, non-soliton loop is not a boundary/topological object). The **A44 fork thereby resolves for bare loops toward CORPUS-OVER-CLAIM**: Ax1 does **not** promise pinning for a bare, non-soliton loop, and **no engine pinning term is "missing"** for that case (no Ax5 owed — per A44 missing-axiom-vs-engine-bug this is a corpus over-reach, not an engine-violates-Ax3 case; the engine is faithful).
> - **SCOPED OPEN — soliton-dressed defects (untested).** The refutation is scoped to the BARE-loop realization the arc ran. A **soliton-dressed** defect (a loop carried by an actual $(2,3)$-winding soliton, which *does* own a boundary/topological pinning) is **not tested** by this arc and stays OPEN.
> Register: confidence demoted into the refuted band (see `claim-quality.md`, clm-exjfai — dated 2026-07-20 note). The CONFIRMED memristive S-lag mechanism (rate-dependent $S_{\min}$) is untouched. Claim body preserved verbatim (Rule-12).

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

> As the atom scales to Beryllium ($Z = 4$, $1s^2 2s^2$), a second macroscopic acoustic cavity boundary ($n = 2$) is populated. The $1s^2$ inner core acts as a primary inductive rotor, generating an intense macroscopic density wake along its primary axis of oscillation. The incoming $2s^2$ valence pair spontaneously structures itself to phase-lock **perpendicularly** ($90°$ orientation offset) to the $1s$ core axis. This orthogonal topological phase-locking is mathematically isomorphic to Field-Oriented Control (FOC) in engineering, where stator and rotor magnetic fields are artificially maintained at $90°$ to completely decouple their mutual inductance. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**

### §2.3 Asynchronous cross-shell decoupling

Per [Analog Ladder Filter](../vol2/quantum-orbitals/ch07-quantum-mechanics/analog-ladder-filter.md): each filled shell acts as an independent AC motor winding; the asynchronous frequency decoupling $\langle M \rangle \propto \int \cos((\omega_1 - \omega_2) t)\, dt \to 0$ eliminates cross-shell mutual inductance.

### §2.4 Caveat: temporal-90° within-LC-tank framing is implementer synthesis (RETRACTED)

The within-LC-tank E-vs-B 90° **TEMPORAL** phase split as "FOC d-q" is **implementer terminology**, not directly stated in the cited corpus locations (explicit retraction, retraction-preserves-body).

**The canonical FOC d-q framings in Core are SPATIAL 90°** (the BH QNM co-rotating frame; the atomic shell orientation orthogonality). The temporal within-LC-tank d-q framing remains implementer synthesis pending corpus canonicalization and is retracted from the canonical set.

## §3 — Dark wake $\tau_{zx}$ derivation (OPEN — this is the gap)

The **dark wake** is the longitudinal shear-strain $\tau_{zx}$ wave propagating backward from accelerating mass through the substrate lattice, carrying the reaction momentum that closes Newton's Third Law for AVE thrust devices. **This is asserted across multiple sibling hardware-engineering compendia but NOT yet derived from first principles in any single Core location. It is an explicit open gap, not a framework claim.** 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**

### §3.1 Phenomenology (asserted in the sibling compendia)

A separate thrust-mechanics compendium gives the canonical thrust-mechanics statement: the AVE framework identifies the vacuum itself as the physical reaction mass (the structural LC components of the substrate metric). As the asymmetric gradient pumps a luminous acoustic wave forward, it simultaneously exerts an equal and opposite stress tensor against the supporting lattice. A 3D FDTD integration isolating the longitudinal shear tensor $\tau_{zx}$ shows a structurally compressive wave propagating backward from the array at $c$. This non-luminous structural compression is the physical "reaction mass" absorbing the thruster's momentum, preserving Newton's Third Law without expelling onboard propellant. 🔴 **[DEMOTED 2026-08-11 — R40-B1; dated demotion note at the end of this file]**

A separate propulsion compendium asserts the warp-metric formula:

$$\tau_{zx} \propto \nabla |E|^2 \cdot Z_{\text{vac}}$$

This is a heuristic isomorphism to the Alcubierre bow-shock metric, **not** a substrate-physics derivation.

### §3.2 What's missing: Cosserat-Lagrangian → $\tau_{zx}$ derivation

The first-principles chain that should produce a backward-propagating $\tau_{zx}$ from accelerating mass would need to:

1. **Start from the Cosserat-K4 coupled Lagrangian** (Axiom 1, Substrate Topology + Axiom 3, Minimum Reflection Principle).
2. **Apply momentum conservation** as a constraint at the soliton-substrate boundary.
3. **Show explicitly** that the reaction momentum manifests as a backward-propagating longitudinal shear at the substrate wave speed $c$. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**
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

---

### 🔴 Dated demotion note — 2026-08-11 (R40 demotion sweep, batch 1)

**Class: DIES-WITH-THE-PHANTOM.** Status change only — the claim text is **preserved
verbatim** (honesty-lag pattern, Rule 12) and stamped in place; it is **no longer live
canon**. Nothing is deleted.

**Demoted in this file:**

- **`:126`** — *"a structurally compressive wave propagating backward from the array at $c$"*
  Stamped in place at `:126`.
  **Why it dies (audited row rationale, verbatim):** Far-field compression wave as the reaction-mass momentum port — a bulk radiative port at ANY speed is removed by the carve; the thrust reaction-mass mechanism as stated is void.

**The arc, complete — the framing R40 rules every demotion note carries:**

1. **The kill fired** (#930) — the walk-back that closed the bulk radiative-port reading.
2. **The premise localized to the #261 K = 2G import** (G-RECON, unchallenged): the compressible
   far-field branch was minted by a GR-imported elastic modulus, not forced by the axioms.
3. **The axioms underdetermine the bulk sector** — the #935 flat-direction finding: the written
   action conserves the Gauss function pointwise and never fixes its value.
4. **The replacement is the RATIFIED bound-sector law — Axiom 5, Substrate DC Bias**
   (BC-SRC clauses **S** / **G** / **Q**), ratified per `_orchestration/docket-entries/2026-08-10-ruling-r43-ratification.md`, as reconciled by `_orchestration/docket-entries/2026-08-10-ruling-r44-r43-reconciliation.md` (R44 — the
   full-scope R43 record is FINAL and authoritative; the partial
   `_orchestration/docket-entries/2026-08-10-ruling-r43-sg-ratified.md` is SUPERSEDED and is **not**
   the resolution). Under the ratified law the A1 / bulk slot is a **bound response** — mechanism
   gloss **back-reaction** — with no independent propagating branch, no port, and zero longitudinal
   characteristic speed. A bulk *wave speed*, a bulk *radiative port*, a bulk *band-branch* and a
   bulk *transit clock* therefore have **no referent**.

**Standing named-open debt (the honest rider).** The ratified axiom does **not** discharge
everything: **THE BIAS PROPAGATION THEOREM** is Axiom 5's standing named-open entry — clause G's
elliptic law is the *static abstraction* of underived finite-speed bias dynamics (`_orchestration/2026-08-10_bias-propagation-brief.md`). Where a
demoted claim's replacement depends on finite-speed bias dynamics, the resolution is the ratified
axiom **with that debt open**, not a closed replacement.

**Records.** R40 ruling `_orchestration/docket-entries/2026-08-10-rulings-r40-r42.md` · verified worklist `research/drivers/r40_sweep_worklist_verified.json` · scope verification `_orchestration/2026-08-10_r40-sweep-scope-verification.md` ·
batch-1 record `_orchestration/2026-08-11_r40-sweep-batch1.md` · vocabulary R50 `_orchestration/docket-entries/2026-08-10-ruling-r50-vocab.md` (canonical: the displacement pattern u₀ around a
deposit is **the bound response**, mechanism gloss **back-reaction**; ε₁₁ is **the bias**;
"dress", "grade"-as-canonical-noun and "halo"-for-the-physics are retired; and the owed theorem is
renamed **THE BIAS PROPAGATION THEOREM**) · vocabulary **R49(b)** `_orchestration/docket-entries/2026-08-10-rulings-r48-r49.md` (*"retardation"
is RETIRED from this role. The canonical term is **propagation delay / finite propagation speed*** —
the retardation retirement is R49(b)'s, NOT R50's; corrected 2026-08-11 at review).

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
   [`eq_axiom_5.tex`](../../common_equations/eq_axiom_5.tex) with its register entry in
   [`axiom-register.md`](../common/axiom-register.md) (§ *Axiom 5 — Substrate DC Bias*). Under
   clause **G** the A1 / bulk slot is a **bound response** — $\mathbf{u}_0 =
   -\mathcal{A}_g\nabla\varepsilon_{11}$, mechanism gloss **back-reaction** — with **no independent
   propagating branch, no port and zero longitudinal characteristic speed**. A bulk *wave speed*, a
   bulk *radiative port*, a bulk *band-branch* and a bulk *transit clock* therefore have **no
   referent**, and each row below owes its re-derivation on that footing.
   $\mathcal{A}_g$ (the **bias-coupling area**) is an `UNVALUED-RATIFIED-CONSTANT` per **R48**
   ([`interlock-register.md`](../common/interlock-register.md), § *𝒜_g — the bias-coupling
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

- **`:108`** — stamped at `:108`. *(family: acoustic-cavity-orbital; banked `uncertain`)*
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  a second macroscopic acoustic cavity boundary ($n = 2$) is populated… generating an intense macroscopic density wake
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  Atomic-shell mechanism framed as acoustic cavity + density wake; a source-bound wake could survive as reactive near-field, but the acoustic-carrier label is owed a sector re-homing (cf. atom-Q relabel).
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave.

- **`:122`** — stamped at `:122`. *(family: dark-wake-reaction-mass)*  ⚑ **BIAS-DEBT**
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  the longitudinal shear-strain $\tau_{zx}$ wave propagating backward from accelerating mass through the substrate lattice, carrying the reaction momentum
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  Momentum-closure content could survive on T2/shear or near-field (τ_zx is algebraically shear) but the 'longitudinal…compressive' carrier label consumes the phantom; leaf already tags it asserted-not-derived.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

- **`:140`** — stamped at `:140`. *(family: dark-wake-reaction-mass)*  ⚑ **BIAS-DEBT**
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  the reaction momentum manifests as a backward-propagating longitudinal shear at the substrate wave speed $c$
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  Routed derivation to-do whose target statement consumes the phantom; the to-do must be re-posed (which surviving sector carries the recoil) before any derivation is attempted.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

**Records.** Ruling **R40** (the demotion sweep) · the banked worklist
[`r40_sweep_worklist_verified.json`](../../../research/drivers/r40_sweep_worklist_verified.json) · batch-0
scope verification and batch-1 execution records in `_orchestration/` · this batch's record
`_orchestration/2026-08-12_r40-sweep-batch2a.md`.

