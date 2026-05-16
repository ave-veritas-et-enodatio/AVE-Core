[↑ Ch.11: Experimental Bench Falsification](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-kl1ern]
-->

## Project TORSION-05: Horizontal Metric Rectification

**The Hypothesis:** The Dielectric Death Spiral can be circumvented by eliminating the 1G vertical payload requirement. By mounting a heavy, heavily-potted TAMD PCBA on a delicately balanced Cavendish Torsion Pendulum suspended inside a hard vacuum chamber, the downward force of gravity is entirely neutralized by the suspension wire. The lateral resistance is effectively $0G$, allowing an EE to measure continuous micro-Newtons of pure metric thrust.

**The PCBA Implementation and Falsification:** The EE designs a High-Voltage Flyback PCBA. An ultra-fast Silicon Carbide (SiC) MOSFET drives a heavy ferrite-core ignition coil with a specifically timed asymmetric sawtooth wave.

1. **The Slow Edge (Solid Grip):** The MOSFET charges the coil slowly. The inductive voltage ($L \frac{di}{dt}$) is $+500$ Volts. Because $500\,\text{V} \ll 43.65\,\text{kV}$, the vacuum acts as a perfectly matched $377\,\Omega$ transmission line. The coil physically grips the spatial lattice, generating an induced forward lateral thrust of exactly $+0.207\,\text{mN}$.
2. **The Fast Edge (Impedance Rupture):** The SiC MOSFET snaps off in $<10\,\text{ns}$. The inductive kickback violently spikes to $-75{,}000$ Volts. Because $|-75\,\text{kV}| > 43.65\,\text{kV}$, the vacuum LC network instantly saturates. The metric undergoes absolute impedance rupture ($\Gamma = -1$), producing exactly $0.0\,\text{mN}$ of backward reaction force.

If the AVE framework is correct, the torsion balance will slowly but continuously accelerate in a perfectly circular path inside the $10^{-6}$ Torr vacuum chamber, generating a time-averaged DC thrust of roughly $\sim \mathbf{100\,\mu\text{N}}$. If the pendulum remains perfectly stationary, the LC non-linear geometry of the universe is permanently falsified.

---
