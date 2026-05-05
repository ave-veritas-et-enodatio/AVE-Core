[↑ Ch.1 Vacuum Circuit Analysis](index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: vjv4zf -->

## Constitutive Circuit Models for Vacuum Non-Linearities

Standard circuit simulators rely on ideal, linear RLC components. However, the physical $\mathcal{M}_A$ condensate exhibits precise non-linear behaviors under extreme mechanical stress, each governed by the Axiom 4 saturation kernel $S(V) = \sqrt{1-(V/V_{yield})^2}$. This section derives the exact non-linear equivalent circuit component for each physical regime.

### The Metric Varactor (Dielectric Yield)

As defined by Axiom 4, the effective compliance (capacitance) of the spatial substrate is bounded by the dielectric saturation limit at $V_{yield} = \sqrt{\alpha}\, V_{snap} \approx 43.65$ kV. The constitutive equation follows directly from the saturation kernel applied to the electric sector:

> **[Resultbox]** *Vacuum Varactor Constitutive Equation*
>
> $$
> C_{eff}(V) = \frac{C_0}{\sqrt{1 - \left(\dfrac{V}{V_{yield}}\right)^{\!2}}} = \frac{C_0}{S(V)}
> $$

To verify consistency with the weak-field limit, the Taylor expansion about $V = 0$ yields:

$$
C_{eff}(V) = C_0 \left[1 + \frac{1}{2}\left(\frac{V}{V_{yield}}\right)^{\!2} + \frac{3}{8}\left(\frac{V}{V_{yield}}\right)^{\!4} + \cdots\right]
$$

At low voltages ($V \ll V_{yield}$), the leading correction is quadratic---identical to the Euler-Heisenberg effective Lagrangian of QED. The classical linear vacuum ($C_{eff} = C_0$) is recovered to arbitrary precision.

| $V/V_{yield}$ | $V$ (kV) | $C_{eff}/C_0$ | $S(V)$ |
|---|---|---|---|
| 0.10 | 4.37 | 1.005 | 0.995 |
| 0.50 | 21.83 | 1.155 | 0.866 |
| 0.90 | 39.29 | 2.294 | 0.436 |
| 0.99 | 43.21 | 7.089 | 0.141 |
| 0.999 | 43.61 | 22.37 | 0.045 |
| 1.000 | 43.65 | $\infty$ | 0 |

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
