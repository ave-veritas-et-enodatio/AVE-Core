[↑ Ch.14: Sonoluminescence](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [91adfe]
-->

# Sonoluminescence: Saturated Rayleigh-Plesset Derivation

**Volume:** 3 (Macroscopic Physics)
**Chapter:** 14

## Saturated Rayleigh-Plesset ODE

The classical Rayleigh-Plesset equation governs the radial dynamics of a bubble in a liquid:

$$\rho_0\!\left(R\ddot{R} + \frac{3}{2}\dot{R}^2\right) = P_{gas}(R) - P_\infty - P_{drive}(t) - \frac{2\sigma}{R} - 4\mu\frac{\dot{R}}{R}$$

In the AVE framework, the constant density $\rho_0$ is replaced by the Axiom 4 saturated density:

$$\rho_{eff} = \frac{\rho_0}{\left(1 - \mathrm{M}^2\right)^{3/2}}, \qquad \mathrm{M} = \frac{|\dot{R}|}{c_{sound}}$$

The cubic exponent ($3/2$ rather than $1/2$) arises from longitudinal inertia in a 3D spherical collapse.

### Topological Wall Mechanism

As $\mathrm{M} \to 1$:
- $\rho_{eff} \to \infty$ — the fluid becomes infinitely massive
- $\ddot{R} \to 0$ — the wall ceases to accelerate
- The ODE solution autonomously halts before $R = 0$

This is precisely the Special Relativistic mechanism ($m_{eff} = m_0 \gamma$) instantiated in the acoustic domain.

## Experimental Parity

The peak flash temperature maps directly to the payload gas:

| Payload | Ionization Energy | Flash $T$ | Mechanism |
|---|---|---|---|
| Argon | 15.76 eV | 12,000–20,000 K | Ionization reservoir limit |
| Xenon | 12.13 eV | 8,000–15,000 K | Lower ionization threshold |
| Pure vapor | N/A | $>$2,000,000 K | Regime III → IV transition |

The pure vapor case emulates a black-hole interior transition at the bubble scale.

*Implementation*: `src/ave/regime_3_saturated/cavitation_collapse.py` — `SaturatedRayleighPlesset` class
