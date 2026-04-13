[↑ Vol 9: Axiomatic Hardware](../index.md)

# Computation

The instruction set architecture, arithmetic logic unit, core topology, boundary interfaces, and design methodology of the Axiomatic Processing Unit. Covers the Geometric Instruction Set Architecture (GISA) — encoding opcodes as orthogonal sub-harmonics diffracted through Tensor Plates — the monolithic APU core layout, impedance-matched I/O boundaries, and the FDTD-to-atopile design workflow.

## Key Results

| Result | Statement |
|---|---|
| GISA Sub-Harmonic Opcodes | Instructions encoded as orthogonal sub-harmonics: $\sin\theta_n = c_0/(\omega_n \cdot d_{grating})$; zero-decode-stage execution [Ch.18](./ch18-geometric-instruction-set/gisa-subharmonic-opcodes.md) |
| Tensor Plate ALU | Refractive impedance structuring performs matrix multiplication passively via diffraction [Ch.19](./ch19-tensor-plates-alu/passive-matrix-multiplication.md) |
| Monolithic APU Plane | Computation plane with no Von Neumann bus — wave mechanics replaces data movement [Ch.20](./ch20-apu-core-topology/monolithic-computation-plane.md) |
| Boundary Interfaces | λ-matching stages couple $\Gamma = 0$ internal domain to $50\,\Omega$ external domain [Ch.21](./ch21-apu-boundary-interfaces/lambda-matching-stages.md) |
| FDTD-to-ato Workflow | Wave mechanics structural arrays compiled to parametric declarative hardware [Ch.22](./ch22-apu-design-methodology/fdtd-to-ato-workflow.md) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Ch.18: Geometric Instruction Set](./ch18-geometric-instruction-set/index.md) | GISA sub-harmonic opcode encoding, diffraction ISA |
| [Ch.19: Tensor Plates ALU](./ch19-tensor-plates-alu/index.md) | Passive refractive matrix multiplication |
| [Ch.20: APU Core Topology](./ch20-apu-core-topology/index.md) | Monolithic computation plane, no Von Neumann bus |
| [Ch.21: APU Boundary Interfaces](./ch21-apu-boundary-interfaces/index.md) | Lambda matching, SerDes geometry converter |
| [Ch.22: APU Design Methodology](./ch22-apu-design-methodology/index.md) | FDTD-to-atopile development workflow |
