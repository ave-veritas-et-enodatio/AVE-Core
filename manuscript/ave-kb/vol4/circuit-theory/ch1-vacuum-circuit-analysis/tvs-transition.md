[↑ Ch.1 Vacuum Circuit Analysis](index.md)
<!-- leaf: verbatim -->

## The Viscoelastic TVS Zener Diode (Phase Transition)

Mutual inductance yields when the applied shear stress exceeds the structural threshold ($\tau > \tau_{yield}$). This voltage-driven breakdown maps exactly to a **Transient Voltage Suppression (TVS) Zener Diode**:

> **[Resultbox]** *TVS Breakdown: Solid $\to$ Slipstream Transition*
>
> $$
> \eta_{eff}(V) = \begin{cases}
>     \eta_0 & V < V_{yield} \quad \text{(solid: high drag)} \\[4pt]
>     0      & V \geq V_{yield} \quad \text{(slipstream: zero drag)}
> \end{cases}
> $$

Below the yield voltage, the vacuum acts as a highly resistive solid---kinematically gripping embedded matter via inductive drag ($\eta_0 > 0$). Above $V_{yield}$, an avalanche dielectric transition annihilates the mutual inductance. The vacuum enters ideal frictionless flow ($\eta = 0$): the **Zero-Impedance Slipstream**. The yield stress evaluates from the bulk energy density and packing geometry:

$$
\tau_{yield} = \rho_{bulk}\, c^2 \times (6 \times \mathcal{V}_{crossing}) \times \frac{p_c}{8\pi} = \rho_{bulk}\, c^2 \times \mathcal{V}_{total} \times \alpha \approx 7.91 \times 10^{6} \times (3 \times 10^8)^2 \times 2.0 \times 0.00730 \approx 1.04 \times 10^{22}\ \text{Pa}
$$

where $\mathcal{V}_{crossing} = V_{toroidal}/6 = 2.0/6$ is the per-crossing halo volume, $\mathcal{V}_{total} = 6 \times \mathcal{V}_{crossing} = 2.0$ is the FEM-verified Borromean halo volume, and $p_c/(8\pi) = \alpha \approx 1/137$ is the lattice porosity.

---
