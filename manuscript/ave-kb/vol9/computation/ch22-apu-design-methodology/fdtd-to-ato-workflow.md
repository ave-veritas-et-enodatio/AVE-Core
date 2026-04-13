[↑ Ch.22: APU Design Methodology](./index.md)
<!-- leaf: verbatim -->

# FDTD-to-ato Design Workflow

Engineering Topo-Kinematic hardware shifts development systematically away from Boolean architecture pipelines natively toward wave mechanics structural arrays. The validated workflow proceeds in three stages:

1. **FDTD Simulation:** Geometric primitives (triodes, diodes, delay lines, reservoirs) are modeled using Finite-Difference Time-Domain solvers with the Axiom 4 nonlinear kernel. This validates waveform integrity, reflection suppression, and saturation behavior.

2. **Parameter Extraction:** The validated geometry parameters (cavity length, taper profiles, grating pitch, trace widths) are extracted from the converged FDTD model and converted to parametric constraints.

3. **Declarative Compilation (atopile):** The parametric constraints are projected onto the `atopile` hardware description language, generating `.ato` modules with AVE-verified impedance constraints. The compiler automatically selects real components from JLCPCB inventories and generates PCB manufacturing files.

By converting FDTD verified geometrical parameters directly onto parametrized declarative hardware, the full pipeline from axiomatic physics to physical bill of materials is automated.

> **[Resultbox]** *Chapter 22 Summary*
>
> Engineering Topo-Kinematic hardware shifts development systematically away from Boolean architecture pipelines toward wave mechanics structural arrays. By converting FDTD verified geometrical parameters directly onto parametrized declarative hardware, the APU design methodology bridges abstract physics to industrial manufacturing.
