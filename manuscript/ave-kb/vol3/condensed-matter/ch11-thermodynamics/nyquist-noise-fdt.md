[↑ Ch.11: Thermodynamics and The Arrow of Time](../index.md)
<!-- leaf: verbatim -->

---

## The Fluctuation-Dissipation Theorem

The preceding sections established that temperature is RMS electromagnetic noise. This section derives the *quantitative* relationship between noise power and impedance---the Fluctuation-Dissipation Theorem (FDT)---directly from the lattice structure.

### Nyquist Noise as Lattice Impedance Thermodynamics

In 1928, Nyquist derived the thermal voltage noise across a resistor $R$ at temperature $T$:

> **[Resultbox]** *Nyquist Thermal Voltage Noise*
>
> $$\langle V^2(f) \rangle = 4 k_B T R \, \Delta f$$

Standard textbooks present this as a consequence of the equipartition theorem applied to electromagnetic modes in a transmission line. Under AVE, this equation acquires a deeper mechanical meaning: **every impedance boundary is a noise source**.

The vacuum itself is a transmission line with characteristic impedance $Z_0 = \sqrt{\mu_0 / \varepsilon_0} \approx 376.73 \;\Omega$. Therefore, the baseline vacuum noise spectral density at temperature $T$ is:

> **[Resultbox]** *The Vacuum Nyquist Baseline*
>
> $$\langle V^2_{vac}(f) \rangle = 4 k_B T \, Z_0 \, \Delta f$$

This is not an analogy. The $\mathcal{M}_A$ lattice is a physical transmission line. The Nyquist relation applies literally: each lattice node radiates thermal noise proportional to its local impedance.

### Boundary-Impedance Thermalization

A critical consequence is that **thermal noise enters a system through impedance mismatches, not through bulk injection**. Consider a topological structure (particle, qubit, or standing wave) embedded in the lattice. The interior of the structure maintains a characteristic impedance $Z_{int}$. At its boundary, the impedance transitions to the ambient vacuum impedance $Z_0$. The reflection coefficient at this junction is:

> **[Resultbox]** *Boundary Reflection Coefficient*
>
> $$\Gamma = \frac{Z_0 - Z_{int}}{Z_0 + Z_{int}}$$

The transmitted noise power at the boundary is:

> **[Resultbox]** *Transmitted Noise Power*
>
> $$P_{transmitted} = (1 - |\Gamma|^2) \cdot P_{incident} = \frac{4 Z_0 Z_{int}}{(Z_0 + Z_{int})^2} \cdot P_{incident}$$

This establishes the fundamental principle of **boundary-impedance thermalization**: thermal noise from the ambient $300\;\text{K}$ reservoir couples into a structure only through its boundary nodes, where the impedance mismatch permits partial transmission. The bulk interior of a well-matched structure remains thermally quiet.

---
