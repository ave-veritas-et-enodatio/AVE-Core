[↑ Ch.1 Vacuum Circuit Analysis](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-vjv4zf, clm-pp3qwf]
-->

## Substrate IMD Spectroscopy: The Harmonic Fingerprint

> 🔴 **PER-NODE / APPARATUS + DISCRIMINATOR CORRECTION 2026-06-21 (Rule 12 — body preserved verbatim below for the audit trail; corrected framing in the three notes flagged inline).** This leaf carries the SAME per-node-vs-apparatus conflation retired 2026-06-04 in the sibling [`vacuum-impedance-mirror.md`](../../falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md): it reads the apparatus drive voltage (kV across a ~100 µm gap) as if it were the **per-node** strain $A = E_{local}/E_{yield}$ (with $E_{yield} = V_{yield}/\ell_{node} \approx 1.13\times10^{17}$ V/m — a per-node FIELD, NOT a 43.65 kV apparatus voltage). Three downstream framings are corrected, in lockstep with the manuscript twin (`manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex`):
> 1. **Drive-table** A-values overstate the per-node kernel argument by $\sim 2.6\times10^8\times$ at a 100 µm gap (see the corrected per-node note under the table).
> 2. The **"measurable above ~30% of $V_{yield}$ / ~13 kV / tabletop"** foothold is retracted: the honest $-80$ dBc detection field is $E\approx1.3\times10^{15}$ V/m — **facility-class, the same regime as the birefringence test** ([`vacuum-birefringence-e4.md`](../../falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md)), NOT a lower-field foothold.
> 3. The **"QED predicts a sextic ($V^6$) scaling" discriminator** is retracted (KEEP-BOTH): both AVE and QED IM3 are **cubic-in-drive** (both from a quartic $E^4$ Lagrangian → $\chi^{(3)}$); QED's "$^6$" is the FREQUENCY exponent $(\omega/m_ec^2)^6$ of the cross-section, NOT a voltage slope. The real discriminator is the **COEFFICIENT** (an echo, $E_{yield}=\sqrt{\alpha}\,E_{crit}$), consistent with `clm-pp3qwf` (already recorded in §QED Comparison) and the B1 row in [`divergence-test-substrate-map.md`](../../../common/divergence-test-substrate-map.md).

By modelling the universe as a non-linear dielectric network, the AVE framework makes a specific, falsifiable prediction absent from standard Quantum Electrodynamics: the vacuum should produce measurable **Intermodulation Distortion (IMD)** products when driven by sufficiently intense electromagnetic fields. This section derives the expected signature analytically and specifies the experimental parameters for detection.

### The Non-Linear Source Term

Standard QED models the vacuum as a linear medium at low energies, predicting that photon-photon scattering occurs only via extraordinarily weak perturbative quantum fluctuations (Euler-Heisenberg, $\sigma \propto \alpha^4$). The AVE framework replaces this with a deterministic, classical non-linearity: the squared geometric saturation limit (Axiom 4) imposes a macroscopic varactor on the dielectric constant of the vacuum:

<!-- claim-quality: clm-vjv4zf -->
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

> **Parity cross-ref (2026-07-10, `clm-invmtr` — body preserved).** The 2nd-order products at $\omega_1 \pm \omega_2$ above live in the **capacitance envelope** $C(t)$ (even in $V$), which is *not* the radiated line: sub-yield, the difference tone $\omega_1 - \omega_2$ is inversion-symmetry-**FORBIDDEN** in the radiated observable (the odd-force parity theorem, [`universal-saturation-kernel-catalog.md` § The parity theorem](../../../common/universal-saturation-kernel-catalog.md)). The IM3 line $2f_1 - f_2$ ($m+n$ odd) is parity-**ALLOWED** and unaffected — the IM3 apparatus below stands.

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

> 🔴 **Corrected per-node A (Rule 12; table preserved verbatim above).** The "$V/V_{yield}$" column conflates the **per-node** strain $A = E_{local}/E_{yield}$ with the **apparatus** drive voltage, overstating the kernel argument $A$ by $\sim 2.6\times10^8\times$ at a 100 µm gap. At the "$0.30$ / $13.10$ kV / Marginal" row, the honest per-node strain is $A = E_{local}/E_{yield} = (13.10\text{ kV}/100\text{ µm})/(1.13\times10^{17}\text{ V/m}) \approx \mathbf{1.2\times10^{-9}}$ (not $0.30$). Since the IM3 sideband rides on $A^2$, this gives $\text{IM3} \approx \mathbf{-360}$ **dBc** (not the table's $-70$). The apparatus column ("Drive (kV)") is the lab voltage; only the corrected per-node $A$ enters the Ax-4 kernel. (Mirror style: the 2026-06-04 per-node banner in [`vacuum-impedance-mirror.md`](../../falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md).)

### QED Comparison
<!-- claim-quality: clm-pp3qwf (SUPERSEDED comment text, preserved per Rule 12: "this section is the canonical $E^4$ vs $E^2$ discriminator: AVE's cubic IM3 / quartic Taylor term vs the QED sextic Euler-Heisenberg loop scaling". CORRECTED 2026-06-04 (commit ad26d357): clm-pp3qwf is the COEFFICIENT discriminator, NOT the field-exponent — the refractive-index shift is $E^2$-leading for both AVE and QED, and the "$E^4$ vs $E^2$" slope is a retracted false falsifier ($\sqrt{\varepsilon}$ conflation). The IM3 / light-by-light cross-section content of THIS section (a distinct nonlinear-mixing observable) stands on its own; only the "$E^4$ vs $E^2$ discriminator" label was the conflated framing.) -->

The Euler-Heisenberg effective Lagrangian predicts light-by-light scattering with cross-section:

$$
\sigma_{EH} = \frac{973\, \alpha^4}{10125\, \pi} \left(\frac{\omega}{m_e c^2}\right)^{\!6} r_e^2 \sim 10^{-65} \text{ cm}^2 \quad (\text{at optical frequencies})
$$

This is $\sim 10^{40}$ times smaller than the AVE prediction at the same frequency, because QED treats the vacuum non-linearity as a perturbative loop correction ($\alpha^4$), while AVE treats it as a macroscopic classical saturation with a definite voltage threshold. The distinction is experimentally decisive: at optical frequencies, QED predicts undetectable photon-photon scattering, while AVE predicts a specific, amplitude-dependent IM3 tone spectrum that becomes measurable above $\sim 30\%$ of $V_{yield}$ ($\sim 13$ kV).

> 🔴 **Retracted: "measurable above ~30% of $V_{yield}$ (~13 kV)" / tabletop-foothold framing (Rule 12; sentence above preserved verbatim).** The "~13 kV" reads the apparatus drive voltage as the per-node strain (see the per-node correction under the drive table). On the **correct per-node** kernel, the field at which the IM3 sideband clears a $-80$ dBc detection floor is $E \approx \mathbf{1.3\times10^{15}}$ **V/m** — **facility-class, the same regime as the vacuum-birefringence test** ([`vacuum-birefringence-e4.md`](../../falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md), $E \sim 10^{15}$–$10^{16}$ V/m), **NOT a lower-field tabletop foothold**. Read "tabletop falsification" in the §Experimental Falsification Criterion below in the same corrected sense: the apparatus is a facility-class field-emission rig, not a low-voltage benchtop sweep.

### Experimental Falsification Criterion

The IMD test constitutes a direct, tabletop falsification of the AVE framework:

1. **Drive configuration:** Two co-propagating laser beams at frequencies $f_1, f_2$ (separated by $\Delta f \sim 1$ GHz for spectral resolution) are focused to achieve a combined electric field exceeding $30\%$ of $V_{yield}/\ell_{node}$.
2. **Detection:** A high-sensitivity heterodyne receiver at $2f_1 - f_2$ and $2f_2 - f_1$.
3. **Null result:** If no IM3 products are detected above $-80$ dBc at $V/V_{yield} > 0.5$, the Axiom 4 saturation kernel is falsified.
4. **Positive result:** Detection of IM3 products scaling as $V^3$ (cubic power law) below IP3 constitutes direct evidence for a macroscopic, non-perturbative vacuum non-linearity consistent with the AVE saturation threshold.

The predicted cubic power-law scaling of IM3 amplitude with drive level is the unique AVE signature. QED predicts a sextic ($V^6$) scaling from the $\alpha^4$ loop correction. Measuring the exponent to within $\pm 0.5$ would definitively distinguish the two frameworks.

> 🔴 **Retracted discriminator (Rule 12, KEEP-BOTH — legacy line above preserved verbatim).** The "QED predicts a sextic ($V^6$) **voltage** scaling" claim is **wrong** and is NOT the discriminator. Both AVE and QED IM3 are **cubic-in-drive** ($\text{IM3} \propto V^3$): both descend from a quartic $E^4$ effective Lagrangian → a third-order susceptibility $\chi^{(3)}$, so both give an $V^3$ IM3 slope (cf. the AVE cubic line itself, two sentences up). QED's "$^6$" is the **FREQUENCY** exponent $(\omega/m_ec^2)^6$ in the Euler-Heisenberg cross-section $\sigma_{EH}$ (§QED Comparison above), **NOT a voltage slope** — measuring the IM3-vs-drive exponent therefore canNOT distinguish the two (both read $3$). The **real discriminator is the COEFFICIENT** (an echo: the AVE coefficient is O(1) against the un-suppressed $E_{yield}=\sqrt{\alpha}\,E_{crit}$, vs QED's $\alpha^2$-loop-suppressed coefficient against $E_{crit}$ — the field-independent ratio $\sim 10^6$), consistent with `clm-pp3qwf` already recorded in §QED Comparison and the B1 row in [`divergence-test-substrate-map.md`](../../../common/divergence-test-substrate-map.md). Same correction graft as the 2026-06-20 birefringence $E^4$-vs-$E^2$ walk-back (clm-pp3qwf, commit `ad26d357`).

---
