[↑ Ch.11 Index](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [wqmb19]
-->

## Sagnac-RLVE: The Definitive Tabletop Falsification

> → Primary: [Regimes of Operation](../../circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md) — $V_{yield}$ threshold and $\mathcal{M}_A$ bulk density definitions

The Sagnac Rotational Lattice Mutual Inductance Experiment bypasses the $G/c^2$ scalar gap by coupling *magnetically* and measuring *interferometrically*.

### Mechanism

A rapidly rotating high-density mass induces vacuum drift via **macroscopic mutual inductance**. Unlike scalar metric strain, mutual inductance operates at first-order ($v_{network}/c$).

### Derivation

**Inductive coupling** (Tungsten, $\rho_W = 19{,}300$ kg/m³):

$$\kappa_{entrain} = \frac{\rho_W}{\rho_{bulk}} = \frac{19{,}300}{7.916 \times 10^6} \approx 0.00244$$

**Vacuum drift** (15 cm radius, 10k RPM → $v_{tan} \approx 157$ m/s):

$$v_{network} = v_{tan} \times \kappa_{entrain} \approx 0.38 \text{ m/s}$$

> **[Resultbox]** *Sagnac Phase Shift*
>
> $$\Delta\phi = \frac{4\pi L_{fiber} \cdot v_{network}}{\lambda c} \approx \mathbf{2.07 \text{ Radians}}$$

### Hardware BOM (~$1,600)

| Component | Specification | Cost |
|---|---|---|
| Laser | 1550 nm telecom diode (Thorlabs S1FC1550) | $450 |
| Fiber coupler | 50/50 SMF-28 splitter | $120 |
| Sensing fiber | 200 m SMF-28 Ultra | $50 |
| Photodetector | InGaAs PIN diode (Thorlabs DET01CFC) | $180 |
| Rotors | 15 cm radius (1× Tungsten, 1× Aluminum) | $800 |

### The $\Psi$ Discriminator

Run the same experiment with Aluminum ($\rho_{Al} = 2{,}700$ kg/m³):

$$\Psi = \frac{\Delta\phi_W}{\Delta\phi_{Al}} = \frac{\rho_W}{\rho_{Al}} \approx 7.15$$

- **AVE prediction**: $\Psi \approx 7.15$ (density-dependent constitutive response)
- **GR prediction**: $\Psi = 1$ (Lense-Thirring is density-independent, $\sim 10^{-20}$ rad at this scale)
- **Null result**: AVE permanently falsified

---
