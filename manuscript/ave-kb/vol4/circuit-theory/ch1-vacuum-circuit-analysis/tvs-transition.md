[↑ Ch.1 Vacuum Circuit Analysis](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-o2shcn]
-->

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

where $\mathcal{V}_{total} = 2.0$ is the **dual-reactance count** ($X_C + X_L$ reactance sectors, Axiom 1; counted, not integrated — see [`../../../common/dual-reactance-storage-taxonomy.md`](../../../common/dual-reactance-storage-taxonomy.md)), and $p_c/(8\pi) = \alpha \approx 1/137$ is the lattice porosity. The $6 \times \mathcal{V}_{crossing}$ writing (with $\mathcal{V}_{crossing} \equiv V_{toroidal}/6$) is a **re-factoring of the same $\mathcal{V}_{total} = 2.0$** — a vestige of the now-retired geometric "halo volume" framing, not an independent geometric derivation of the value (the identity $\mathcal{V}_{crossing} = V_{toroidal}/6$ is circular; the proton's $6^3_2$ Borromean topology remains as topology but does not set the value 2).

---
