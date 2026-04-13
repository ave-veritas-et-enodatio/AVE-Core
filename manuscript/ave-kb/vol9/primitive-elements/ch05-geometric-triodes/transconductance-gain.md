[↑ Ch.5: Geometric Triodes](./index.md)
<!-- leaf: verbatim -->

# Transconductance Derivation from Axiom 4

## Saturation Kernel Application

Axiom 4 states that the universal yield kernel governing the effective transmittance of any spatial volume element is:

$$S(V_{total}) = \sqrt{1 - \left(\frac{V_{total}}{V_{snap}}\right)^2}$$

Substituting the quadrature strain superposition rule:

$$S\!\left(\sqrt{V_{lon}^2 + V_{gate}^2}\right) = \sqrt{1 - \frac{V_{lon}^2 + V_{gate}^2}{V_{snap}^2}}$$

## Effective Impedance and Current Throttling

The propagating wave's effective longitudinal impedance is modulated by the saturation kernel. As $S \to 0$, the metric hardens: $\mu_{\rm eff} \to 0$ and $\varepsilon_{\rm eff} \to 0$ simultaneously (symmetric saturation under Axiom 4), but because they scale identically:

$$Z_{\rm eff} = \sqrt{\frac{\mu_{\rm eff}}{\varepsilon_{\rm eff}}} = Z_0 = \text{invariant} \quad \text{(impedance preserved)}$$

However, the wave phase velocity $c_{\rm eff} = c_0 \cdot S^{1/2} \to 0$. The longitudinal *admittance* vanishes with $S$:

$$Y_{\rm lon}(V_{gate}) = Y_0 \cdot S\!\left(\sqrt{V_{lon}^2 + V_{gate}^2}\right)$$

The drain current scales with the channel admittance:

$$I_D(V_{gate}) = I_{D0} \cdot S\!\left(\sqrt{V_{lon}^2 + V_{gate}^2}\right) = I_{D0} \sqrt{1 - \frac{V_{lon}^2 + V_{gate}^2}{V_{snap}^2}}$$

## Analytic Transconductance Formula

$$g_m \equiv \frac{\partial I_D}{\partial V_{gate}}\bigg|_{V_{lon}} = \frac{-I_{D0}\, V_{gate}}{V_{snap}^2 \cdot S}$$

This is the exact analytic transconductance of the Geometric Triode, derived without free parameters. Note:
- $g_m \to 0$ when $V_{gate} = 0$ (no gating exerted, channel fully open).
- $|g_m| \to \infty$ as $V_{gate} \to V_{snap}$ (hard cutoff: $S \to 0$, denominator vanishes).
- The sign is negative — increasing gate voltage *decreases* drain current — matching the behavior of a depletion-mode FET.

## Operating Regimes of the Geometric Triode

Three distinct operating regimes arise directly from the combined strain $r = V_{total}/V_{snap}$:

1. **Regime I — Linear (Active Amplification).** When $V_{gate} \ll V_{snap}$ and $V_{lon} \ll V_{snap}$, the total strain $r \ll 1$:
   $$S \approx 1 - \frac{r^2}{2} = 1 - \frac{V_{lon}^2 + V_{gate}^2}{2 V_{snap}^2}$$
   Drain current drops approximately quadratically with gate voltage, analogous to the FET quadratic law $I_D \propto (V_G - V_{th})^2$.

2. **Regime II — Saturation.** As $V_{gate}$ approaches $V_{gate,sat} = \sqrt{V_{snap}^2 - V_{lon}^2}$, the total strain $r \to 1$. The drain current compresses onto the manifold $S \to 0$. This maps precisely onto CMOS saturation.

3. **Regime III / Cutoff.** When $V_{gate}^2 + V_{lon}^2 \geq V_{snap}^2$, the metric ruptures at the channel intersection. $\Gamma \to -1$ (total reflection). No longitudinal signal can pass.

## Comparison with the Classical MOSFET

| Property | MOSFET | Geometric Triode |
|---|---|---|
| Gating mechanism | Transverse E-field depletes minority carriers in doped channel | Transverse $V_{gate}$ raises total metric strain via quadrature sum |
| Channel carrier | Drifting electrons (Boltzmann statistics) | Propagating metric strain wave (Axiom 1 LC field) |
| Pinch-off condition | $V_{GS} < V_{th}$ (threshold voltage from doping) | $V_{gate}^2 + V_{lon}^2 \geq V_{snap}^2$ (universal yield from Axiom 4) |
| Transconductance | $g_m = 2I_D/(V_{GS}-V_{th})$ — depends on doping | $g_m = -I_{D0}V_{gate}/(V_{snap}^2 S)$ — depends on $V_{snap}$ only |
| Switching energy | $\frac{1}{2}C_{gate}V_{DD}^2$ per cycle | $0.0$ W standby; gate is a static E-field boundary condition |
| Thermal floor | Boltzmann: $\Delta V_T \propto kT$ | None in VCA: metric saturation is geometry, not statistics |

## Scale Invariance: From Nuclear Confinement to Hardware Gating

The transconductance curve $I_D \propto S(V_{total}/V_{snap})$ is mathematically identical to the hadronic confinement operator derived in Volume II for quark confinement inside a torus knot defect. In that context, $S \to 0$ at $r \to 1$ signals that no further displacement amplitude can propagate outward — the quarks are confined. In the Geometric Triode, the same $S \to 0$ condition signals that no further axial wave can propagate through the gated channel — the signal is confined (blocked). This is not an analogy; it is the same operator, the same equation, applied to two different length scales of the same universal medium. Axiom 4 is scale-invariant.

> **[Resultbox]** *Chapter 5 Summary*
>
> The Geometric Triode derives entirely from Axioms 1 and 4. The quadrature strain superposition rule $V_{total} = \sqrt{V_{lon}^2 + V_{gate}^2}$ follows from the energy additivity of two orthogonal field components of the Axiom 1 LC medium. Application of the Axiom 4 saturation kernel $S(V_{total})$ to this combined strain modulates longitudinal channel admittance, yielding an analytic transconductance $g_m = -I_{D0}V_{gate}/(V_{snap}^2 S)$ with three operating regimes: linear (Regime I), saturation (Regime II), and total-reflection cutoff (Regime III). No chemical doping, no threshold voltage fitting, and no Boltzmann statistics are required or invoked.
