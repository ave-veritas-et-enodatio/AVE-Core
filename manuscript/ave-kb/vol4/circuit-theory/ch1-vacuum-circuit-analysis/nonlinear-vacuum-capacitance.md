[↑ Ch.1 Vacuum Circuit Analysis](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-8nkvwy, clm-vjv4zf]
-->

## Constitutive Circuit Models for Vacuum Non-Linearities

Standard circuit simulators rely on ideal, linear RLC components. However, the physical substrate exhibits precise non-linear behaviors under extreme mechanical stress, each governed by the Axiom 4 saturation kernel $S(V) = \sqrt{1-(V/V_{yield})^2}$. This section derives the exact non-linear equivalent circuit component for each physical regime.

### The Metric Varactor — Longitudinal Bond Compliance (Dielectric Yield)

> **Sector note (Q1 = (B), Grant-ratified 2026-06-15; `research/2026-06-15_ceff-epsilon-monotonicity_result.md`).** The diverging $C_0/S$ below is the **longitudinal-A1 bond compliance** ($1/k_a$, the stretch-reactance), **NOT** the transverse dielectric capacitance. The transverse permittivity $\varepsilon_{eff}=\varepsilon_0 S$ and the LCR-measured cell capacitance $C_{diel}=\varepsilon_{eff}A/d\propto S$ *roll off* (the bench-netlist $C_0\!\cdot\!S$ form, [ee-bench-netlist.md](../../simulation/ch17-hardware-netlists/ee-bench-netlist.md):15). The two are **orthogonal reactances** (A1 ⊥ T2) that share the EE name "capacitance"; identifying them is the genesis-24 double-count (`master-equation.md:20`). See INVARIANT-S2 sector split.

As defined by Axiom 4, the effective **bond compliance** of the spatial substrate is bounded by the saturation limit of the **longitudinal (A1) stretch sector**, which reaches $A^2=1$ ($C_{eff}\to\infty$) at $V_{snap} = m_e c^2/e \approx 511$ kV.

> **Grade-fork RESOLVED = T2 (Grant 2026-06-30; `def-vyvsn1` adjudicated, `research/2026-06-30_electron-portmap-derivation_result.md` §5).** The prior wording keyed this A1 varactor's saturation-completion voltage on $V_{yield}=\sqrt\alpha\,V_{snap}\approx43.65$ kV. That is **corrected**: $V_{yield}$ is the **transverse Cosserat ($T_2$) self-trap wall** (the electron's confining $\Gamma=-1$; [`pair-production-axiom-derivation.md`](../../../vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md):102), **not** the A1 compliance bound. The **longitudinal-A1** bond compliance below diverges at the higher $V_{snap}$ (a factor $1/\sqrt\alpha\approx11.7$ above $V_{yield}$). **Consequence:** a standing electron's A1 mass core operates at strain $A=V_{yield}/V_{snap}=\sqrt\alpha\approx0.085$ — deeply **sub-saturated** ($S(\sqrt\alpha)=\sqrt{1-\alpha}\approx0.996$), which is *why* it binds (the $S\to0$ varactor runaway never fires on the mass channel). Since $V_{yield}=\sqrt\alpha\,V_{snap}$ EXACTLY, $A=\sqrt\alpha$ is an $\alpha$-echo operating point (Class-C), not a free parameter.

The constitutive equation follows directly from the Axiom-4 saturation kernel $S(V)=\sqrt{1-(V/V_{snap})^2}$ applied to the **longitudinal (A1) stretch sector**:

<!-- claim-quality: clm-vjv4zf -->
<!-- claim-quality: clm-8nkvwy (Asymmetric saturation case: only $\varepsilon$ scales by $S$ → $C_{eff} \to \infty$, $Z_{asym} = Z_0/\sqrt{S} \to \infty$; this is the canonical statement of the asymmetric branch of the Universal Saturation Kernel) -->
> **[Resultbox]** *Vacuum Varactor Constitutive Equation*
>
> $$
> C_{eff}(V) = \frac{C_0}{\sqrt{1 - \left(\dfrac{V}{V_{snap}}\right)^{\!2}}} = \frac{C_0}{S(V)}
> $$

To verify consistency with the weak-field limit, the Taylor expansion about $V = 0$ yields:

$$
C_{eff}(V) = C_0 \left[1 + \frac{1}{2}\left(\frac{V}{V_{snap}}\right)^{\!2} + \frac{3}{8}\left(\frac{V}{V_{snap}}\right)^{\!4} + \cdots\right]
$$

At low voltages ($V \ll V_{snap}$), the leading correction is quadratic---identical to the Euler-Heisenberg effective Lagrangian of QED. The classical linear vacuum ($C_{eff} = C_0$) is recovered to arbitrary precision. **Note the electron's A1 mass-core operating point** $A=V_{yield}/V_{snap}=\sqrt\alpha\approx0.085$ sits in the **first (linear) row** of the table below ($C_{eff}/C_0\approx1.004$) — sub-saturated, far from the $V_{snap}$ divergence; the confining $\Gamma=-1$ wall is supplied by the *transverse* $T_2$ self-trap at $V_{yield}$, not by any A1-varactor divergence.

| $V/V_{snap}$ | $V$ (kV) | $C_{eff}/C_0$ | $S(V)$ | note |
|---|---|---|---|---|
| $\sqrt{\alpha}\approx0.085$ | 43.65 | 1.004 | 0.996 | **$V_{yield}$ = T2 self-trap wall; electron A1-core operating point** |
| 0.10 | 51.1 | 1.005 | 0.995 | |
| 0.50 | 255.5 | 1.155 | 0.866 | |
| 0.90 | 459.9 | 2.294 | 0.436 | |
| 0.99 | 505.9 | 7.089 | 0.141 | |
| 0.999 | 510.5 | 22.37 | 0.045 | |
| 1.000 | 511.0 | $\infty$ | 0 | **$V_{snap}$ = A1 mass-completion + Schwinger** |

### The Vacuum Memristor (Thixotropic Hysteresis)

The dielectric saturation--plastic transition requires a finite geometric relaxation time to physically liquefy the lattice:

> **[Resultbox]** *Thixotropic Relaxation Time*
>
> $$
> \tau_{relax} = \frac{\ell_{node}}{c} = \frac{3.862 \times 10^{-13}}{2.998 \times 10^{8}} \approx 1.288 \times 10^{-21} \text{ s}
> $$

Because the vacuum cannot alter its inductive resistance instantaneously, its present-state impedance depends on the historical integral of applied stress. This is the defining characteristic of a **Memristor**: a circuit element whose resistance is a function of the cumulative charge that has passed through it.

The constitutive relation is:

$$
M(q) = \frac{d\Phi}{dq}, \qquad \Phi(t) = \int_{-\infty}^{t} V(\tau)\, d\tau
$$

where $M$ is the memristance (units: $\Omega$) and $\Phi$ is the magnetic flux linkage. Under high-frequency AC topological stress, the memristive vacuum produces a classic **Pinched Hysteresis Loop**: the $V$--$I$ Lissajous figure passes through the origin but encloses a finite area proportional to the energy dissipated during each thixotropic yield--heal cycle.

At drive frequencies $f \gg 1/\tau_{relax} \approx 7.8 \times 10^{20}$ Hz, the vacuum responds too slowly to yield and behaves as a purely elastic (linear) medium. At $f \ll 1/\tau_{relax}$, complete yield and recovery occur within each cycle, producing maximum hysteresis loss. The crossover frequency is set entirely by the lattice pitch and $c$.

### The Zero-Impedance Skin Effect (Metric Faraday Cages)

In standard electrical engineering, the AC skin depth $\delta$ governs how deeply alternating current penetrates into a conductor:

> **[Resultbox]** *Classical Skin Depth*
>
> $$
> \delta = \sqrt{\frac{2\rho}{\omega\mu}} = \sqrt{\frac{2 R_{vac}}{\omega\mu_0}}
> $$

Under the Topo-Kinematic identity, $R_{vac} \equiv \xi_{topo}^{-2}\, \eta_{vac}$: the vacuum's electrical resistance maps to its mutual inductance (drag coefficient). Evaluating the skin depth in the two vacuum phases:

1. **Unsaturated Vacuum ($V < V_{yield}$):** $R_{vac} = \xi_{topo}^{-2}\, \eta_0 > 0$. The skin depth is finite; shear waves penetrate to a depth proportional to $\sqrt{\eta_0}$. At 1 GHz:

$$
\delta_{solid} = \sqrt{\frac{2\, \xi_{topo}^{-2}\, \eta_0}{2\pi \times 10^9 \times \mu_0}} \sim \text{finite (deep-space penetration)}
$$

2. **Saturated Slipstream ($V \geq V_{yield}$):** $\eta_{eff} \to 0$, therefore $R_{vac} \to 0$:

$$
\delta_{slipstream} = \sqrt{\frac{2 \times 0}{\omega\mu_0}} \equiv 0
$$

When the metric exceeds the yield threshold, the skin depth collapses to zero. The destructive, high-shear slipstream is confined *entirely* to the exterior surface of the macroscopic body. The interior metric acts as a **Topological Faraday Cage**: perfectly shielded from external structural shear, even at extreme gravitational gradients. This provides the mechanical basis for why planetary interiors remain structurally intact inside deep gravity wells.

---
