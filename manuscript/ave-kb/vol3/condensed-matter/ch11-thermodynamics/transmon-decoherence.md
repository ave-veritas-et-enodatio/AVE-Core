[↑ Ch.11: Thermodynamics and The Arrow of Time](../index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: eaiqj1 -->

---

## Application: Transmon Qubit Decoherence

The transmon qubit provides a direct experimental demonstration. A Josephson junction is an LC oscillator with junction leads connected to a $300\;\text{K}$ reservoir. The thermal noise enters exclusively through the lead boundaries---the edge nodes where the junction impedance meets the cryogenic feedline impedance.

A correct simulation must therefore inject stochastic noise only at the boundary nodes, not uniformly across the bulk field. The resulting coherence metric (the Cauchy-Schwarz normalised overlap between the instantaneous state and the initial eigenmode) is bounded $C(t) \in [0, 1]$ and decays via oscillatory relaxation, reproducing the observed error-rate timelines of modern cryo-cooled qubits.

> ↗ See also: [Ch.10: Quantum Computing and Topological Immunity](../../../vol4/advanced-applications/ch10-quantum-computing/index.md) — decoherence as impedance mismatch; topological qubit model

### Ohmic Damping: The Dissipation Arm

The Nyquist relation has a partner: the dissipation side of the FDT. Every resistive element $R$ that radiates noise $\langle V^2 \rangle$ also absorbs energy at rate:

> **[Resultbox]** *Dissipation Power*
>
> $$P_{diss} = \frac{\langle V^2 \rangle}{4R} = k_B T \, \Delta f$$

In the lattice, dissipation arises from Ohmic damping---the irreversible conversion of coherent wave energy into incoherent lattice vibrations. The damping coefficient $\gamma$ of a standing wave embedded in the lattice is:

> **[Resultbox]** *Ohmic Damping Coefficient*
>
> $$\gamma = \frac{1}{2} \frac{Z_0}{\omega_0 L_{eff}}$$

where $\omega_0$ is the resonant frequency and $L_{eff}$ is the effective inductance of the mode. This ensures the Fluctuation-Dissipation balance: the noise power injected at the boundary is exactly compensated by the Ohmic dissipation rate, maintaining thermal equilibrium at temperature $T$.

---
