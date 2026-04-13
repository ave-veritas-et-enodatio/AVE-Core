[↑ Ch.18: Geometric Instruction Set](./index.md)
<!-- leaf: verbatim -->

# GISA: Sub-Harmonic Opcode Encoding via Diffraction

Traditional IC algorithms map logic instructions via sequential binary Opcodes interpreted by active transistor decode-trees, accumulating massive cycle latencies. The APU executes logic through a Geometric Instruction Set Architecture (GISA) that eliminates the decode stage entirely.

Instructions are encoded as orthogonal sub-harmonics of the carrier wave. Each harmonic routes independently through the Tensor Plate ALU (Ch 19) by the diffraction condition:

$$\sin\theta_n = \frac{c_0}{\omega_n \cdot d_{grating}} \qquad n = 1, 2, \ldots, M_{GISA}$$

The composite wave packet enters the Tensor Plate and encounters a specialized diffractive strain matrix. Each sub-harmonic component is steered to its own spatial output port by the grating pitch $d_{grating}$. There is no software scheduler: $M_{GISA}$ is the cardinality of the physical harmonic basis. All operations execute in strict spatial parallel — not pipelined, but **geometrically simultaneous**.

> **[Resultbox]** *Chapter 18 Summary*
>
> Traditional IC algorithms map logic instructions via sequential binary Opcodes interpreted by active transistor decode-trees. The APU executes logic through a Geometric Instruction Set Architecture: sub-harmonic encoding maps opcodes to spatial diffraction angles, enabling geometrically simultaneous multi-instruction execution without any decode stage.
