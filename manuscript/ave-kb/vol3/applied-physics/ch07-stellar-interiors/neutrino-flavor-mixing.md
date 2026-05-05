[↑ Ch.7: Stellar Interiors and Neutrino Oscillation](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [o6kgkz]
-->

---

## Neutrino MSW: Flavor Mixing as Impedance Mode Coupling

The MSW (Mikheyev--Smirnov--Wolfenstein) effect describes neutrino flavor oscillation in stellar matter. In AVE, this is impedance-dependent mode coupling between propagation channels:

- $\nu_e$ mode: impedance modified by charged-current interaction with local electrons, $Z_e = Z_0 (1 + V_{CC}/V_0)$
- $\nu_\mu$ mode: impedance unchanged (no charged-current coupling)
- When $Z_e \approx Z_\mu$ (resonance): maximal mode conversion

The matter potential is:

> **[Resultbox]** *Neutrino MSW Matter Potential*
>
> $$V_{CC} = \sqrt{2}\, G_F\, n_e$$

and MSW resonance occurs at the critical density:

> **[Resultbox]** *MSW Resonance Critical Density*
>
> $$n_e^{res} = \frac{\Delta m^2 \cos 2\theta_{12}}{2\sqrt{2}\, G_F\, E}$$

### Energy-Dependent Validation

| **Source** | $E$ (MeV) | $P_{ee}^{\text{AVE}}$ | $P_{ee}^{\text{obs}}$ |
|---|---|---|---|
| pp chain | 0.4 | 0.55 | $0.56 \pm 0.03$ (Borexino) |
| $^7$Be | 0.86 | 0.52 | $0.51 \pm 0.07$ (Borexino) |
| $^8$B (low $E$) | 5.0 | 0.38 | $\sim 0.39$ (SNO) |
| $^8$B (high $E$) | 10.0 | 0.31 | $0.34 \pm 0.02$ (SNO) |

The engine uses the same `reflection_coefficient()` function as all other domains.

---
