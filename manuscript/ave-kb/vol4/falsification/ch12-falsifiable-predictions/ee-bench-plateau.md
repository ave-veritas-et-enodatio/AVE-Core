[↑ Ch.12 Index](index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: trgqtf -->

## EE Bench: Macroscopic Dielectric Plateau

> → Primary: [Regimes of Operation](../../circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md) — $V_{yield}$ and $E_{yield}$ derivations
> ↗ See also: [Nonlinear Vacuum Capacitance](../../circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md) — Axiom 4 saturation kernel $S(E)$

Standard QED: $\epsilon_0$ is a fixed linear constant.
AVE (Axiom 4): $\epsilon_{eff}(E) = \epsilon_0 \sqrt{1 - (E/E_{yield})^2}$, with $E_{yield} \approx 1.13 \times 10^{17}$ V/m.

As $E \to E_{yield}$: $\varepsilon_{eff} \to 0$ and $C_{eff} = C_0/S \to \infty$.

### Falsification Protocol

Ultra-stiff vacuum gap (below Paschen curve minimum, UHV) swept toward $\sim 10^{16}$ V/m using asymmetric sharp emission tips.

**Dual-sensor measurement:**

1. **LCR capacitance tracking**: Standard physics → flat $C(E)$. AVE → asymptotic spike at $\sim 85\%$ of $E_{yield}$.
2. **Interferometry**: Stabilized laser transverse through gap. As $E \to E_{yield}$, $n_{eff} \propto S$ *decreases* — anomalous drop in refractive index.

Detection of geometric asymptote prior to atomic plasma ionization confirms the hardware limits of the spatial lattice.

### PONDER-01: Maxwell Stress Rectification

Thrust from divergence of Maxwell Stress Tensor across asymmetric boundary:

$$F_i = \oint_{\partial V} \sigma_{ij} n_j \, da - \int_V \frac{\partial \mathbf{g}}{\partial t} \, d^3x$$

- Optimal geometry: 1000:1 asymmetry ratio (1 µm emitter vs 1 mm collector)
- 30 kV RMS, swept 1 MHz → 100 MHz (VHF)
- Thrust scales as $V^2 f^2$
- Detection: vacuum torsion balance, $> 1\;\mu$N target

---
