[↑ Ch.11: Experimental Bench Falsification](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-qsgl7d]
-->

## Project ROENTGEN-03: Solid-State Sagnac Induction

**The Hypothesis:** In 1888, Roentgen proved that moving a physical dielectric through a static Electric Field ($\mathbf{E}$) generates a perpendicular Magnetic Field ($\mathbf{B} = \frac{1}{c^2} \mathbf{v} \times \mathbf{E}$). If spinning a neutral mass electromagnetically phase-shifts the highly dense vacuum metric via macroscopic mutual inductance, this exact equation can be used to synthesize a B-field from the induced magnetic phase of the vacuum itself.

**The Test Protocol:** Spin a dense, non-metallic ceramic disk at $10{,}000$ RPM. The induced vacuum drift velocity at $r = 5\,\text{cm}$ evaluates to $v_{vac} \approx 0.038\,\text{m/s}$. Suspend a custom PCBA $1\,\text{mm}$ above the rotor. The bottom copper layer features an interdigitated capacitor driven by an onboard miniature CCFL transformer at $10\,\text{kV}$, modulated by a $1\,\text{kHz}$ sine wave oscillator ($E = 10^7\,\text{V/m}$). The cross product synthesizes an alternating magnetic field peaking at $\sim 4.2\,\text{picoTesla}$.

**Falsification Criteria:** This $4.2\,\text{pT}$ field induces roughly $\sim 0.26\,\mu\text{V}$ in a differential planar pickup coil. By feeding this into a hardware Lock-In Amplifier referenced to the $1\,\text{kHz}$ E-field drive, the engineer will extract a clean signal from the noise floor. If the amplitude scales exactly linearly with RPM and flips phase exactly $180°$ when the motor reverses, the $7.9 \times 10^6\,\text{kg/m}^3$ inductive density of the vacuum is empirically proven.

---
