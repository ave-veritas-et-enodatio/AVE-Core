[↑ Ch.11: Thermodynamics and The Arrow of Time](../index.md)
<!-- leaf: verbatim -->

---

## Phase Transitions as Impedance Matching Events

Classical thermodynamics describes phase transitions---solid$\to$liquid, normal$\to$superconducting, paramagnetic$\to$ferromagnetic---as spontaneous symmetry breaking driven by free energy minimisation. Under AVE, phase transitions are **impedance matching events**: abrupt changes in the local transmission and reflection coefficients of the LC lattice.

### The Superconducting Transition

In a normal conductor, the conduction electrons (topological defects drifting through the lattice) experience continuous impedance mismatches at grain boundaries, phonon scattering centers, and lattice impurities. Each mismatch produces a partial reflection ($|\Gamma| > 0$), and the cumulative reflected power constitutes electrical resistance.

At the critical temperature $T_c$, the Kuramoto order parameter $R$ of the electron ensemble undergoes a spontaneous phase transition from $R \approx 0$ (chaotic, high resistance) to $R = 1$ (perfect phase-lock, zero resistance). In impedance terms:

> **[Resultbox]** *Superconducting Impedance Transition*
>
> $$Z_{eff} \to 0 \;\Omega, \quad |\Gamma| \to 1, \quad \text{(total reflection, zero dissipation)}$$

The Meissner effect follows directly: when $\mu_{eff} \to 0$ at saturation (Axiom 4), the magnetic field cannot penetrate the bulk. Applied magnetic flux reflects completely at the boundary ($\Gamma = -1$), which is macroscopically observed as the total expulsion of the B-field.

### Casimir Cooling: Geometric Phase Transitions

The Casimir effect provides a mechanism for **engineering** phase transitions without cryogenic cooling. By placing a conductor inside a nanoscale cavity of gap width $d$, long-wavelength thermal modes ($\lambda > 2d$) are geometrically excluded from the cavity interior.

This acts as a high-pass filter on the ambient noise spectrum. The effective local temperature inside the cavity is:

> **[Resultbox]** *Casimir Effective Temperature*
>
> $$T_{eff} = T_{ambient} \cdot \sqrt{1 - \left(\frac{f_c}{f_{max}}\right)^2}$$

where $f_c = c_0 / (2d)$ is the cavity cutoff frequency. When the resulting $T_{eff}$ drops below $T_c$, the enclosed conductor undergoes a geometric phase transition into the superconducting state---at room ambient temperature.

---
