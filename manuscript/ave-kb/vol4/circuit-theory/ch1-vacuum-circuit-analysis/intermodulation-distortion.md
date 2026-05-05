[↑ Ch.1 Vacuum Circuit Analysis](index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: vjv4zf, pp3qwf -->

## Condensate IMD Spectroscopy: The Harmonic Fingerprint

By modelling the universe as a non-linear dielectric network, the AVE framework makes a specific, falsifiable prediction absent from standard Quantum Electrodynamics: the vacuum should produce measurable **Intermodulation Distortion (IMD)** products when driven by sufficiently intense electromagnetic fields. This section derives the expected signature analytically and specifies the experimental parameters for detection.

### The Non-Linear Source Term

Standard QED models the vacuum as a linear medium at low energies, predicting that photon-photon scattering occurs only via extraordinarily weak perturbative quantum fluctuations (Euler-Heisenberg, $\sigma \propto \alpha^4$). The AVE framework replaces this with a deterministic, classical non-linearity: the squared geometric saturation limit (Axiom 4) imposes a macroscopic varactor on the dielectric constant of the vacuum:

<!-- claim-quality: vjv4zf -->
> **[Resultbox]** *Vacuum Varactor (Axiom 4)*
>
> $$
> C_{vac}(V) = \frac{C_0}{\sqrt{1 - (V/V_{yield})^2}}, \qquad V_{yield} \approx 43.65 \text{ kV}
> $$

[Figure: vacuum_dielectric_saturation.png — see manuscript/vol_4_engineering/chapters/]

### Third-Order IMD from Taylor Expansion

The Taylor expansion of the varactor about $V = 0$ yields the non-linear susceptibility:

$$
C_{vac}(V) \approx C_0 \left[1 + \underbrace{\frac{1}{2}\left(\frac{V}{V_{yield}}\right)^{\!2}}_{\text{2nd order}} + \underbrace{\frac{3}{8}\left(\frac{V}{V_{yield}}\right)^{\!4}}_{\text{4th order}} + \cdots\right]
$$

When driven by a dual-tone signal $V(t) = V_1 \cos(\omega_1 t) + V_2 \cos(\omega_2 t)$, the squared term generates 2nd-order products at $\omega_1 \pm \omega_2$, and the quartic term generates the critical **3rd-order intermodulation** (IM3) products:

> **[Resultbox]** *3rd-Order Intermodulation Products*
>
> $$
> f_{IM3} = 2f_1 - f_2 \quad \text{and} \quad 2f_2 - f_1
> $$

These IM3 tones fall *close* to the original drive frequencies (unlike harmonic products at $2f$, $3f$ which fall far out of band), making them the most experimentally accessible non-linear signature.

### Predicted IM3 Amplitude

For a standard varactor with $C(V) = C_0 (1 - V/V_{br})^{-1/2}$, the 3rd-order intercept point (IP3) is related to the breakdown voltage by:

> **[Resultbox]** *Third-Order Intercept (IP3)*
>
> $$
> V_{IP3} = \sqrt{\frac{4}{3}}\; V_{yield} \approx 1.155 \times 43.65 \approx 50.4 \text{ kV}
> $$

The IM3 sideband power relative to the fundamental is:

$$
P_{IM3} = P_{fund} - 3(V_{IP3,\text{dBm}} - P_{fund,\text{dBm}})
$$

| $V/V_{yield}$ | Drive (kV) | IM3 Level (dBc) | Measurable? |
|---|---|---|---|
| 0.01 | 0.44 | $-160$ | No |
| 0.10 | 4.37 | $-100$ | No |
| 0.30 | 13.10 | $-70$ | Marginal |
| 0.50 | 21.83 | $-54$ | Yes |
| 0.70 | 30.56 | $-40$ | Yes |
| 0.90 | 39.29 | $-20$ | Strong |

### QED Comparison
<!-- claim-quality: pp3qwf (this section is the canonical $E^4$ vs $E^2$ discriminator: AVE's cubic IM3 / quartic Taylor term vs the QED sextic Euler-Heisenberg loop scaling) -->

The Euler-Heisenberg effective Lagrangian predicts light-by-light scattering with cross-section:

$$
\sigma_{EH} = \frac{973\, \alpha^4}{10125\, \pi} \left(\frac{\omega}{m_e c^2}\right)^{\!6} r_e^2 \sim 10^{-65} \text{ cm}^2 \quad (\text{at optical frequencies})
$$

This is $\sim 10^{40}$ times smaller than the AVE prediction at the same frequency, because QED treats the vacuum non-linearity as a perturbative loop correction ($\alpha^4$), while AVE treats it as a macroscopic classical saturation with a definite voltage threshold. The distinction is experimentally decisive: at optical frequencies, QED predicts undetectable photon-photon scattering, while AVE predicts a specific, amplitude-dependent IM3 tone spectrum that becomes measurable above $\sim 30\%$ of $V_{yield}$ ($\sim 13$ kV).

### Experimental Falsification Criterion

The IMD test constitutes a direct, tabletop falsification of the AVE framework:

1. **Drive configuration:** Two co-propagating laser beams at frequencies $f_1, f_2$ (separated by $\Delta f \sim 1$ GHz for spectral resolution) are focused to achieve a combined electric field exceeding $30\%$ of $V_{yield}/\ell_{node}$.
2. **Detection:** A high-sensitivity heterodyne receiver at $2f_1 - f_2$ and $2f_2 - f_1$.
3. **Null result:** If no IM3 products are detected above $-80$ dBc at $V/V_{yield} > 0.5$, the Axiom 4 saturation kernel is falsified.
4. **Positive result:** Detection of IM3 products scaling as $V^3$ (cubic power law) below IP3 constitutes direct evidence for a macroscopic, non-perturbative vacuum non-linearity consistent with the AVE saturation threshold.

The predicted cubic power-law scaling of IM3 amplitude with drive level is the unique AVE signature. QED predicts a sextic ($V^6$) scaling from the $\alpha^4$ loop correction. Measuring the exponent to within $\pm 0.5$ would definitively distinguish the two frameworks.

---
