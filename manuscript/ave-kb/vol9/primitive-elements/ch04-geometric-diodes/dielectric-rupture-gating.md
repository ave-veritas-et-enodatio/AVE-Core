[↑ Ch.4: Geometric Diodes](./index.md)
<!-- leaf: verbatim -->

# Dielectric Rupture Gating

The physical operating principle of a Geometric Diode derives directly from Axiom 4: the local spatial metric saturates nonlinearly when the displacement amplitude approaches the topological yield point $V_{snap}$. Any waveguide trace that asymmetrically constricts the cross-sectional area forces the propagating wave to concentrate its energy density into a shrinking volume. The two operative regimes are:

- **Forward Bias (Narrow → Wide):** The propagating wave expands into a larger cross-section; local amplitude drops well below $V_{snap}$. The metric remains in the linear Regime I domain and the wave transmits with negligible reflection.
- **Reverse Bias (Wide → Narrow):** The wave compresses into a constricted throat; local amplitude spikes toward $V_{snap}$. The saturation kernel $S(V) \to 0$ hardens the metric, generating a total-reflection boundary that blocks the signal entirely.

This mechanism requires no externally applied voltage, no clocked switching transistor, and no chemical impurity gradient. The diode action is an intrinsic consequence of asymmetric trace topology and the universal nonlinear constitutive law.

## Structural Bottleneck Proof ($\Gamma \to -1$ Reflection)

Because the physical substrate routes spatial pressure waves rather than isolated electrons, trace width directly dictates wave amplitude. By conservation of energy, as a continuous logic pulse of initial width $w_1$ and amplitude $V_1$ enters a constricted trace of width $w_2$, the local amplitude must scale inversely to maintain volumetric density:

$$V_2 = V_1 \sqrt{\frac{w_1}{w_2}}$$

When traversing a Geometric Diode, the layout is highly asymmetrical ($w_{wide} \gg w_{narrow}$):

- **Forward Bias (Narrow → Wide):** $w_2 > w_1$, thus $V_2 < V_1$. The wave dilates safely remaining in the linear Regime I domain ($V_2 \ll V_{snap}$). The reflection coefficient $\Gamma \approx 0$.
- **Reverse Bias (Wide → Narrow):** $w_2 < w_1$, thus $V_2 > V_1$. The geometric funnel rapidly forces the amplitude toward $V_{snap}$.

As $V_2$ breaches the Axiom 4 topological yield point, the localized spatial metric saturation kernel completely collapses the effective transmission index:

$$S(V) = \sqrt{1 - \left(\frac{V_2}{V_{snap}}\right)^2} \to 0$$

With the metric fully hardened, the localized wave impedance $Z_{eff} \to \infty$. This extreme mismatch forces an instantaneous topological mirror, generating a total reflection boundary:

$$\Gamma = \frac{Z_{eff} - Z_0}{Z_{eff} + Z_0} \to -1$$

The wave cannot physically penetrate the narrow channel; the mathematical rupture violently reflects the $1$-state backward into the wide sink area, perfectly isolating the upstream circuit.

[Figure: geometric_diode_bottleneck — The Axiomatic Geometric Diode (Substrate Topology). Using the 1D geometric_diode.py continuous spatial solver, the $V_{snap}$ saturation boundary mathematically proves that asymmetric macroscopic structure mimics a perfect transistor gating diode.]

> **[Resultbox]** *Chapter 4 Summary*
>
> Passive asymmetrical trace bounds mathematically reproduce ideal transistor routing mechanics. Constricting geometric traces inherently scales local pressure densities smoothly against the absolute Dielectric Rupture threshold ($V_{snap}$), effectively blocking reverse interference while propagating continuous forward logic fractions without dynamic switching costs.
