[↑ Appendices](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: [clm-pf84ng]
-->

# App D: Computational Graph Architecture

To physically validate the macroscopic inductive and elastodynamic derivations of the AVE framework, all numerical simulations and Vacuum Computational Network Dynamics (VCFD) models must be computationally instantiated on a generated, geometrically constrained discrete spatial graph. This appendix defines the software architecture constraints required to map the $\mathcal{M}_A$ topology into computational memory.

## Key Results

| Result | Statement |
|---|---|
| Poisson-Disk genesis | Exclusion radius $r_{min} = l_{node}$ yields packing fraction $\approx 0.17$--$0.18$ (matching QED saturation limit) |
| Chiral LC Over-Bracing | $C_{ratio} = (p_{cauchy}/p_c)^{1/3} \approx (0.3068/0.1834)^{1/3} \approx 1.187$ — connecting nodes within $1.187\,l_{node}$ radius |
| Trace-reversed state | $K = 2G$ emerges at coupling $k_{couple} > 4.5$ |
| Symplectic Kirchhoff | Capacitive node update: $\Delta V_i = \frac{dt}{C}(\sum I_{in} - \sum I_{out})$; Inductive edge update: $\Delta I_e = \frac{dt}{L}(V_{start} - V_{end})$ |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Graph Architecture](./graph-architecture.md) | Genesis algorithm, Chiral LC over-bracing, discrete Kirchhoff execution |

---
