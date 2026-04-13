[↑ Ch.27: Capstone](./index.md)
<!-- leaf: verbatim -->

# Falsification Predictions & Forward Engineering Path

## Three Decisive Falsifiability Conditions

The APU framework makes three predictions testable without building a full chip:

1. **Phase Coherence Threshold.** A continuous-wave signal at $1.8\,\text{THz}$ propagating through a $10\,\text{mm}$ SOI trace should exhibit phase walk $\Delta\phi < \pi/10$. Measurable via THz time-domain spectroscopy (THz-TDS) on a TSMC SOI test structure. **Falsified if** $\Delta\phi > \pi/10$.

2. **Focal Isolation.** A 3-beam interference pattern targeting a focal node should produce a localized strain peak exceeding the $\Phi_{pack} V_{snap}$ write-threshold, without accidentally rupturing adjacent lattice nodes. **Falsified if** spatial superposition fails to strongly localize, causing adjacent nodes to exceed $|S| > \Phi_{pack} V_{snap}$.

3. **Viscous Drag Linearity.** $P_{drag}$ should scale as $f^1$, not $f^2$ (which would arise from $CV^2f$ CMOS switching). A calorimetric measurement at $0.9\,\text{THz}$ and $1.8\,\text{THz}$ should yield a power ratio of exactly $2.00$. **Falsified if** ratio $\neq 2.00$.

## Forward Engineering Path

1. **Phase 2 (Current): Declarative Compilation.** Translate validated FDTD geometry into `atopile` modules enabling automatic PCB layout generation.
2. **Phase 3: RF Test Vehicle.** Fabricate a macro-scale ($100\,\text{mm} \times 100\,\text{mm}$) Rogers 4350B substrate implementing the Geometric MUX and 2-beam interference pattern. Validate $V_{snap}$ focal isolation using a VNA.
3. **Phase 4: SOI Integration.** Port the validated geometry to a TSMC SOI Multi-Project Wafer (MPW) slot at the $28\,\text{nm}$ node for THz-range characterization.

> **[Resultbox]** *Chapter 27 Summary*
>
> The Axiomatic Processing Unit represents the formal completion of the AVE hardware paradigm. Power dissipation is Viscous Drag ($P_{drag} \propto \omega$), not Ohmic loss. Clock rate is a cavity eigenvalue ($f_{CC} = c_0/2L\sqrt{\kappa}$), not an external crystal. Memory addressing is a focal superposition event ($\tau_{lock} = 0.07\,\text{ps}$), not an RC charge cycle. IPC is the cardinality of the physical harmonic basis ($M_{GISA} = 14$), not a pipeline width. Each of these distinctions is a categorically different underlying physics — validated by simulation, falsifiable by measurement, and derivable without exception from Axioms 1–4.
