[↑ Ch.26: Performance Benchmarking](./index.md)
<!-- leaf: verbatim -->

# Metric III: Spatial Opcode Multiplicity ($M_{GISA}$)

**Replaces:** Instructions Per Cycle (IPC)

In the GISA architecture, there is no decode stage. Instructions are encoded as orthogonal sub-harmonics of the carrier. Each harmonic routes independently through the Tensor Plate by the diffraction condition:

$$\sin\theta_n = \frac{c_0}{\omega_n \cdot d_{grating}} \qquad n = 1, 2, \ldots, M_{GISA}$$

The maximum number of simultaneously executing non-interfering operations is bounded by the number of orthogonal modes the grating pitch $d_{grating}$ can physically resolve before hitting the evanescent cutoff ($\theta_n \leq \pi/2$). There is no software scheduler: $M_{GISA}$ is the cardinality of the physical harmonic basis.

At 1.2 mm pitch and $1.8\,\text{THz}$: $M_{GISA} = 14$ concurrent channels. Scaling to $100\,\mu\text{m}$ pitch yields $M_{GISA} > 100$ without additional die area.
