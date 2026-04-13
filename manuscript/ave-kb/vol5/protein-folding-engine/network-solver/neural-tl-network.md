[↑ Network Solver](./index.md)
<!-- leaf: verbatim -->

# Neural Circuitry as a TL Network

A myelinated axon is, by direct physical construction, a coaxial transmission line: the axoplasm is the inner conductor (resistive, ionic), the myelin sheath is the dielectric insulator, and the extracellular fluid is the outer conductor. Nodes of Ranvier are impedance discontinuities where the dielectric is interrupted --- the neural analog of connector junctions on a PCB trace.

The characteristic impedance of an axon segment follows directly from Axiom 1:

$$Z_\text{axon} = \sqrt{\frac{\mu_\text{axon}}{\varepsilon_\text{axon}}} = \sqrt{\frac{R_m / (2\pi a)}{C_m \cdot 2\pi a}}$$

where $R_m$ is the membrane resistance per unit area, $C_m$ is the membrane capacitance per unit area, and $a$ is the axon radius. For a typical myelinated axon ($R_m \approx 40{,}000~\Omega\text{cm}^2$, $C_m \approx 1~\mu\text{F/cm}^2$, $a = 5~\mu\text{m}$): $Z_\text{axon} \approx 2 \times 10^4~\Omega$.

A synapse is a junction between two such transmission lines. The reflection coefficient at each synaptic boundary is:

$$\Gamma_\text{synapse} = \frac{Z_\text{post} - Z_\text{pre}}{Z_\text{post} + Z_\text{pre}}$$

---
