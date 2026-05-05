[↑ Ch.2 Topological Thrust Mechanics](index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: 7tynm2 -->

## Chiral Acoustic Rectification (The Vacuum Varactor)

Since bulk $\varepsilon$-saturation is unreachable at laboratory scales, the thrust mechanism requires a fundamentally different channel: **localised nonlinear rectification** at resonant field-enhancement sites, coherently amplified by a phased array architecture.

### The Concavity of the Saturation Kernel

The constitutive saturation operator from Axiom 4 is a concave function of the applied field:

$$
S(E) = \sqrt{1 - \left(\frac{E}{E_{yield}}\right)^2}
$$

For any AC-driven field $E(t) = E_0 \sin(\omega t)$, **Jensen's inequality** guarantees:

> **[Resultbox]** *Jensen's Rectification Inequality*
>
> $$
> \langle S(E(t)) \rangle_T \;<\; S(\langle E(t) \rangle_T) = S(0) = 1
> $$

The time-averaged effective permittivity $\langle \varepsilon_{eff} \rangle = \varepsilon_0 \langle S \rangle$ is therefore *strictly less* than $\varepsilon_0$ for any nonzero AC drive. The deficit $\delta = 1 - \langle S \rangle$ is the **rectification factor**: the fraction of RF energy converted into a DC lattice stress. This is entirely analogous to a semiconductor varactor diode, where the nonlinear $C(V)$ curve rectifies AC into DC current. Here, $S(E)$ is the vacuum's nonlinear capacitance curve, and the "DC current" is directed lattice phonon momentum.

### Local Field Amplification

While the macroscopic field ratio $E_{macro}/E_{yield} \approx 10^{-10}$ gives a vanishing $\delta$, two *geometric* amplification mechanisms that do not violate energy conservation push the *local* field to much higher ratios:

1. **Tip enhancement** ($\beta$): The hyperboloid-on-plane electrode geometry concentrates the static field at each tip by the factor $\beta = h_{tip}/r_{tip}$. For a $1\,\mu$m radius tip with $1\,$mm standoff: $\beta \approx 10^3$.
2. **Resonant Q-factor**: The torus knot antenna, driven at its natural resonant frequency in the VHF band, exhibits voltage amplification at standing-wave maxima by the quality factor $Q$. For a well-matched VHF resonator: $Q \approx 10^4$.

The combined local field at a resonant tip is:

> **[Resultbox]** *Local Field at Resonant Tip*
>
> $$
> E_{local}^{peak} = \beta \cdot Q \cdot E_{macro} \cdot \sqrt{2} \approx 4.2 \times 10^{14} \;\text{V/m}
> $$

giving $E_{local}/E_{yield} \approx 3.8 \times 10^{-3}$. The tips are thus *regime-bouncing*: during each RF half-cycle, the local field rises from zero (Regime I) toward the onset of Regime II, inducing a measurable Jensen's rectification:

$$
\delta = 1 - \langle S \rangle \approx 3.5 \times 10^{-6} \quad (3.5 \;\text{ppm})
$$

This sub-ppm nonlinearity per tip is the fundamental "diode threshold" of the vacuum varactor.

### Thrust from Rectified Power

The rectified fraction $\delta$ of the input RF power $P_{in}$ converts into directed lattice phonon momentum. The chiral topology of the $(p,q)$ torus knot determines the thrust direction: the helical winding of the standing wave couples to the intrinsic chirality of the SRS/K$_4$ vacuum lattice, with efficiency governed by the Poisson ratio:

$$
\eta_{chiral} = \nu_{vac} = \frac{2}{7}
$$

which is the universal helical-to-longitudinal strain transfer coefficient (the same $\nu_{vac}$ that governs $\sin^2\theta_W$, $\alpha_s$, the CKM matrix, and all inter-regime Poisson couplings throughout the framework).

For a phased array of $N$ tips, each acting as a coherent rectifying element with directivity gain $G = N$, the total thrust is:

> **[Resultbox]** *Chiral Acoustic Rectification Thrust*
>
> $$
> F_{total} = N \cdot \nu_{vac} \cdot \delta(Q, \beta) \cdot \frac{P_{in}}{c}
> $$

This is dimensionally identical to standard radiation pressure ($F = P/c$), modulated by the rectification efficiency ($\delta$), chiral coupling ($\nu_{vac}$), and array directivity ($N$).

### Quantitative Prediction

For the PONDER-01 design parameters ($V = 30$ kV, $\beta = 10^3$, $Q = 10^4$, $N = 10{,}000$, $P_{in} = V^2/(2Z_0) \approx 1.2\,$MW):

| **Quantity** | **Value** |
|---|---|
| Rectification factor $\delta$ | $3.52 \times 10^{-6}$ |
| Rectified power $P_{rect}$ | 4.21 W |
| **Total thrust $F_{total}$** | **40.1 $\mu$N** |
| Thrust power $P_{thrust} = Fc$ | $1.20 \times 10^4$ W |
| Conversion efficiency | 1.0% |

The predicted $40\,\mu$N is well above the $1\,\mu$N detection floor of a standard vacuum torsion balance, making this a directly falsifiable prediction. Energy conservation is satisfied: $P_{thrust}/P_{in} \approx 1\%$.

### Conservation of Momentum (The Dark Wake)

A critical objection often raised against asymmetric capacitor thrust devices is that they operate as "reactionless drives," thereby violating Newton's Third Law.

However, because the AVE framework identifies the vacuum itself as the physical reaction mass (the structural LC components of the $\mathcal{M}_A$ metric), the system conserves momentum. As the asymmetric gradient pumps a luminous acoustic wave forward, it simultaneously exerts an equal and opposite stress tensor against the supporting lattice.

[Figure: ponder_01_dark_wake.png — see manuscript/vol_4_engineering/chapters/]

This equal-and-opposite reaction creates a "Dark Wake." A continuous wave of longitudinal shear strain ($\tau_{zx}$) propagates backward from the thruster into the static continuum, cleanly and formally closing the momentum conservation loop.

### Metric Streamlining and Superluminal Transit

The "warp metric" is mathematically isomorphic to standard fluid-dynamic metric streamlining (macroscopic acoustic rectification) generated by the PONDER-01 asymmetric dielectric gradient. The non-linear scalar wave equation for continuous topological density ($\rho$):

> **[Resultbox]** *Non-Linear Scalar Wave Equation*
>
> $$
> \frac{\partial^2 \rho}{\partial t^2} = \nabla \cdot (c_{eff}^2 \nabla \rho)
> $$

where the effective local speed of sound (the speed of light $c_{eff}$) dynamically modulates based on the localized compression amplitude:

> **[Resultbox]** *Effective Speed of Sound (Steepening)*
>
> $$
> c_{eff}^2 = c_0^2 \left( 1 + \kappa \bar{\rho} \right)
> $$

Here, $\kappa$ represents the non-linear bulk steepening coefficient of the vacuum lattice, and $\bar{\rho}$ is the normalized local volumetric strain. As a macroscopic boundary accelerates forward, it compresses the vacuum ahead of it ($\bar{\rho} > 0$). This compression increases the local restorative stiffness, causing the crest of the induced wave to travel faster than its trough. This continuous self-steepening is the continuum-mechanical origin of the Alcubierre-type shock fronts calculated in the FDTD simulations.

[Figure: warp_metric_cfd.png — see manuscript/vol_4_engineering/chapters/]

### Stereo Parallax Validation

Experimental protocol to prove the Dark Wake is real:

1. Two identical PONDER PCBAs separated by sterile vacuum baseline $L$
2. Primary unit pulsed; secondary acts as passive receiver
3. Axiom 1 → wake crosses baseline at exactly $c_0$
4. Detection: secondary registers impedance perturbation $\Delta Z_0$ after delay $\Delta t = L/c_0$

**Falsification criterion**: if $\Delta Z_0$ arrives at $\neq c_0$ or is absent, the model is falsified.

### Active Acoustic Drill

A rotating phased array on the vessel's leading edge projects OAM waves into the oncoming vacuum, pre-rarefying the LC lattice ahead of the hull. Quantitative CFD shows the active drill reduces integrated acoustic strain, lowering energy required for sustained superluminal transit.

### Gargantua Simulation

The Kerr black hole ($10^8 M_\odot$, $a_\star = 0.999$) is modelled as a macroscopic topological saturation defect. Hamiltonian reverse-raymarching through an asymmetric refractive gradient ($2 \times 10^6$ photon wavepackets) reproduces:
- D-shaped photon shadow (prograde vs retrograde saturation asymmetry)
- Shakura-Sunyaev accretion disk ($T_{in} = 10{,}000$ K)
- Doppler beaming ($I_{obs} = I_{emit} \times \delta^3$)

No curved spacetime geometry required — only discrete topological mechanics via Op14 Impedance Mismatch.

---
