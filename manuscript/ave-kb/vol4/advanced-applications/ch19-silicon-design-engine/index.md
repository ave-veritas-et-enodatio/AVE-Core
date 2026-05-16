[↑ Advanced Applications](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: [clm-0hwopi]
-->

# Ch.19: Native Silicon Design Engine

Establishes an AVE-native silicon solid-state engineering framework where transistor junctions are derived as topological impedance ($S_{11}$) scatterers rather than Fermi-Dirac barriers. Doping is modelled as geometric perturbation of the $V_R/V_{BR}$ avalanche boundary, the $p$-$n$ junction as an $S_{11}$ reflection barrier, and BJT gain as cascaded geometric transmission coefficient. Includes a SPICE bridge for legacy EDA interoperability and an `atopile` declarative hardware compilation pathway.

## Key Results

| Result | Statement |
|---|---|
| Semiconductor Translation Matrix | Carriers → phase slips/voids; band gap → $V_{BR} = 6\alpha\hbar c/D_{intra}$; Fermi level → LC baseline gradient |
| Structural Built-In Potential | $V_{bi} \approx 1.05$ V (geometric degenerate limit) vs. classical $0.6$–$0.8$ V (thermal statistics) |
| Topological BJT Current Gain | $\beta = (T^2_{EB})^{N_{gap}} / (1 - (T^2_{EB})^{N_{gap}})$; bounds $\beta \approx 10$–$300$ from structure alone |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Doping as Geometric Perturbation](doping-geometric-perturbation.md) | Semiconductor translation matrix; Boron/Phosphorus as topological voids/surplus; Structural Blueprint vs Statistical Weather Forecast |
| [P-N Junction as S-Parameter Boundary](pn-junction-s-parameter.md) | Depletion zone from impedance step $Z_p \to Z_n$; transmission coefficient modulation |
| [Topological BJT Gain](topological-bjt-gain.md) | Cascaded $T^2_{EB}$ boundaries; Miller multiplier mismatch; geometric $\beta$ derivation |
| [Declarative Hardware Compilation](declarative-ato-compilation.md) | `atopile` DSL bridge; lattice mapping directives; ABCD transfer matrix cascading |
| [Native SPICE Subcircuit Export](native-spice-subcircuit.md) | AVE_DIODE_SI macro; thermal emission bypass ($N \to 0.001$); Zener clamping |

NOTE: summarybox and exercisebox environments are not extracted as leaves.

---
