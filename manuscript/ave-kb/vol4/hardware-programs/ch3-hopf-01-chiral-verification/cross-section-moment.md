[↑ Ch.3 HOPF-01 Chiral Verification](index.md)
<!-- leaf: verbatim -->

## Standard Model Baseline Response: Crossing Mutual Coupling

The SM baseline is constructed in four layers, each representing a distinct classical electromagnetic effect:

1. **Layer 1 --- Dipole self-impedance.** The primary resonance arises from the standing-wave mode of an end-fed thin-wire resonator. Using the King--Middleton EMF method (Balanis, S8.4), the center-fed input impedance is

$$
\begin{align}
R_{in} &= \frac{\eta}{2\pi}\!\left[C_E + \ln(kL) - \mathrm{Ci}(kL) + \tfrac{1}{2}\sin(kL)\bigl(\mathrm{Si}(2kL) - 2\mathrm{Si}(kL)\bigr) \right. \nonumber \\
&\qquad\quad \left. + \tfrac{1}{2}\cos(kL)\bigl(C_E + \ln(kL/2) + \mathrm{Ci}(2kL) - 2\mathrm{Ci}(kL)\bigr)\right] \\
X_{in} &= \frac{\eta}{4\pi}\!\left[2\mathrm{Si}(kL) + \cos(kL)\bigl(2\mathrm{Si}(kL) - \mathrm{Si}(2kL)\bigr) \right. \nonumber \\
&\qquad\quad \left. - \sin(kL)\bigl(2\mathrm{Ci}(kL) - \mathrm{Ci}(2kL) - \mathrm{Ci}(2ka^2/L)\bigr)\right]
\end{align}
$$

   where $\eta = Z_0/\sqrt{\varepsilon_{eff}}$ is the wave impedance in the dielectric, $k = 2\pi f\sqrt{\varepsilon_{eff}}/c$, $C_E \approx 0.5772$ is Euler's constant, $\mathrm{Si}$ and $\mathrm{Ci}$ are the sine and cosine integrals, and $a$ is the wire radius.

2. **Layer 2 --- Skin-effect ohmic loss.** At $\sim$1 GHz, the copper skin depth is $\delta \approx 2\;\mu$m. The AC resistance per unit length is $R_{ac} = 1/(\sigma_{Cu} \cdot A_{skin})$, where $A_{skin} = \pi(a^2 - (a-\delta)^2)$.

3. **Layer 3 --- Curvature effective-length correction.** The RMS curvature $\kappa_{rms}$ produces an effective-length correction $L_{eff} = L(1 + a^2\kappa_{rms}^2/4)$. This effect is negligible: $<0.03\%$ for all five knots.

4. **Layer 4 --- Crossing mutual coupling.** At each crossing, standard Neumann mutual inductance couples the two wire segments:

$$
M_{cross} = \frac{\mu_0 \ell}{2\pi}\ln\!\left(\frac{\ell}{d_{sep}}\right) \cdot \cos\theta
$$

   where $\ell \approx 3$ mm is the coupling length (one hole spacing), $d_{sep} \approx 2.1$ mm is the z-separation (PCB thickness + wire diameter), and $\theta$ is the crossing angle. For torus knots, the average crossing angle is $\sim$70$^\circ$ ($\cos\theta \approx 0.34$), which strongly suppresses the mutual inductance. The fractional frequency perturbation is

$$
\frac{\Delta f}{f}\bigg|_{cross} \approx -\frac{1}{2}\frac{\sum_i M_i}{L_{self}}
$$

   where $L_{self} = (\mu_0 L/2\pi)[\ln(2L/a) - 1]$ is the wire self-inductance.

---
