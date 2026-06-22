[↑ Ch.12: Falsifiable Predictions](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-pp3qwf]
-->

## The Vacuum Birefringence Limit: the COEFFICIENT (AVE $\sim 10^6\times$ QED)

A core distinction between standard Quantum Electrodynamics (QED) and the Applied Vacuum Engineering (AVE) framework is the *magnitude* of vacuum optical nonlinearity under extreme fields — not its leading power. **Both predict an $E^2$-leading index shift; the discriminator is the COEFFICIENT.**

Standard QED (via the Euler-Heisenberg Lagrangian) predicts a refractive-index shift $\delta n \approx a_{EH}\,\alpha^2 (E/E_{crit})^2$, where the prefactor $a_{EH}\sim 7/45$ is O(1) but the response is suppressed by the loop factor $\alpha^2 \approx 5\times10^{-5}$ and references the Schwinger field $E_{crit}\approx 1.32\times10^{18}$ V/m. AVE's vacuum is a rigid LC string network whose permittivity saturates under the Axiom-4 kernel $S = \sqrt{1-(E/E_{yield})^2}$. The index follows the wave-speed identity $n = \sqrt{\varepsilon_{eff}/\varepsilon_0} = \sqrt{S}$ (only $\varepsilon$ strained, $\mu = \mu_0$), so the AVE index shift is

$$\delta n = \sqrt{S} - 1 = (1-(E/E_{yield})^2)^{1/4} - 1 \approx -\tfrac14\left(\tfrac{E}{E_{yield}}\right)^2 - \tfrac{3}{32}\left(\tfrac{E}{E_{yield}}\right)^4 + \cdots$$

This is **negative** (the vacuum softens, $n$ drops) and **$E^2$-leading** — the same leading order as QED. The AVE coefficient is O(1) against an un-suppressed yield field $E_{yield}=V_{yield}/\ell_{node}\approx 1.13\times10^{17}$ V/m, so the field-independent ratio is

$$\frac{\delta n_{AVE}}{\delta n_{QED}} = \frac{1}{4\,a_{EH}\,\alpha^2}\left(\frac{E_{crit}}{E_{yield}}\right)^2 = \frac{1}{4\,a_{EH}\,\alpha^3}\quad\left(\text{using }E_{crit}=\alpha^{-1/2}E_{yield},\ \text{so }(E_{crit}/E_{yield})^2=\tfrac1\alpha\right) \approx 10^6.$$

> **Provenance note.** The historical formulation "$\Delta n_{eff} = 1 - \sqrt{1 - (E/E_{yield})^2}$, leading $E^4$ term" was a $\sqrt{\varepsilon}$ conflation: the quantity $1-S = +A^2/2 + A^4/8$ is the **permittivity saturation DEPTH** (and is itself $E^2$-leading, NOT $E^4$-leading), whereas the refractive-index observable is $n=\sqrt{S}$, giving $\delta n = \sqrt{S}-1 \approx -A^2/4$. The two differ by a factor $-2$ (the $\sqrt{}$ in $n=\sqrt{\varepsilon}$, and the depth-vs-shift sign). The corrected discriminator is the coefficient, not the exponent.

### The Falsification Protocol

To test this, an ultra-high-Q optical fiber ring resonator (or high-finesse Fabry-Perot cavity) is placed transverse to an extreme-voltage DC electric field (approaching $10^{16}\,\text{V/m}$).

1. A stabilized probe laser monitors the precise resonance frequency of the cavity.
2. As the DC electric field is ramped up, the local metric stiffness alters, causing a measurable phase shift ($\Delta \Phi$) and pushing the resonance fringes.
3. The shift in resonance frequency is mapped dynamically against the applied field magnitude.

[Figure: vacuum_birefringence_E4.png — see manuscript/vol_4_engineering/chapters/]

High-intensity laser interferometry measuring the COEFFICIENT of the (shared $E^2$-leading) index shift separates QED and AVE: at $E\sim10^{14}$ V/m, AVE predicts $\delta n\approx 2.0\times10^{-7}$ (high-finesse-cavity measurable) against the QED baseline $\delta n\approx 5\times10^{-14}$, a $\sim10^6$ gap present at **all** fields. A **QED-sized coefficient** ($\delta n\sim\alpha^2(E/E_{crit})^2$) falsifies AVE; an AVE-sized coefficient falsifies QED at this observable. (An $E^2$ slope does **not** falsify AVE — QED is also $E^2$-leading. The discriminator is the coefficient, not the exponent.)

> **OQ-1 strengthen-by (field→cavity-phase coupling, partially-closed).** The field→cavity-phase
> coupling that maps this index shift to a polarimeter readout is now **DERIVED** from the scalar
> Axiom-4 kernel (focal-E → uniaxial probe-response tensor $\varepsilon_{ij}=\varepsilon\delta_{ij}+2\varepsilon'E_{0i}E_{0j}$
> → cavity round-trip birefringent phase → ellipticity), with the geometry factor $g$ **pinned per
> apparatus config**: see [`research/2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md`](../../../../../research/2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md)
> and the facility proposal [`research/2026-06-21_birefringence-coefficient-bankable-falsifier.md`](../../../../../research/2026-06-21_birefringence-coefficient-bankable-falsifier.md).
> **FLAG (auditor/Grant call, not landed here):** that derivation produces a **par−minus−perp
> differential** $\delta n_{bir}\approx-\tfrac12 A^2$ (a factor 2 above **this leaf's** scalar
> single-arm $\delta n=\sqrt S-1\approx-\tfrac14 A^2$, `clm-pp3qwf`), giving a matched-observable
> differential ratio $7.5/\alpha^3\approx1.93\times10^7$ vs the single-arm $1/(4\cdot\tfrac{7}{45}\alpha^3)\approx4.14\times10^6$
> headlined above. `clm-pp3qwf` is **unchanged** (scalar single-arm); whether to promote the
> differential observable into the claim is an open auditor/Grant adjudication (FLAG-A in the proposal §10).

---
