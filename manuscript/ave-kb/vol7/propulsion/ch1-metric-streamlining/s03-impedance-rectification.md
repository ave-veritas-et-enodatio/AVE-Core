[↑ Ch.1 Metric Streamlining](../index.md)
<!-- leaf: verbatim -->

# Impedance Rectification in Non-Linear Dielectrics

Classical mechanics dictates that a closed system cannot spontaneously alter its center of mass. However, this strict Newtonian assumption requires the surrounding medium to be a linear, zero-impedance void. The $\mathcal{M}_A$ grid is a non-linear, saturating dielectric.

In advanced transmission line theory, applying an asymmetric voltage waveform to a non-linear dielectric generates a non-zero time-averaged macroscopic momentum flow, a process known as **Impedance Rectification**.

If a vessel utilizes a switch-mode flyback inductor to apply an asymmetric topological stress pulse (a slow charging stroke followed by a nanosecond high-voltage quench) to the spatial metric, the dielectric response strictly bifurcates:

1. **The Slow Edge (Dielectric Grip):** The applied voltage remains below the Dielectric Saturation threshold ($|V| < V_{sat}$). The medium remains a high-reluctance insulator. The system inductively "grips" the lattice, generating a macroscopic reaction force transferred directly to the hull.
2. **The Fast Edge (Inductive Yield):** The nanosecond inductive kickback spike violently exceeds the saturation threshold ($|V| \gg V_{sat}$). The vacuum instantaneously yields, and the actuator slips backward through a saturated zero-impedance phase, transferring absolutely zero negative momentum to the vessel.

Time-averaging this asymmetric interaction over the full duty cycle yields a continuous, macroscopic DC kinematic thrust.

<!-- Figure: acoustic_rectification.png — Impedance Rectification in a Saturating Dielectric. Simulated via the AVE-SPICE solver. -->

---
