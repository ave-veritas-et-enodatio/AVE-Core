[↑ Ch.3 Quantum and Signal Dynamics](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-ph2uux]
path-stable: "referenced from vol1 as eq:nonlinear_wave"
-->

## Section 3.6: Non-Linear Dynamics and Topological Shockwaves

The linear wave equation assumes constant compliance ($\epsilon_0$). Axiom 4, however, defines the vacuum as a non-linear dielectric bounded by the fine-structure limit ($\alpha$). The saturation operator takes a squared geometric form ($n=2$), consistent with QED energy bounds and classical electrodynamics.

To preserve dimensional homogeneity on a 1D continuous transmission line, the telegrapher equations utilize the continuous macroscopic non-linear modulus $\epsilon(\Delta\phi)$:

> **[Resultbox]** *Non-Linear Telegrapher Equation*
>
> <!-- eq:nonlinear_wave -->
>
> $$
> \frac{\partial^{2}\Delta\phi}{\partial z^{2}} = \mu_0 \epsilon(\Delta\phi)\frac{\partial^{2}\Delta\phi}{\partial t^{2}} + \mu_0 \frac{d\epsilon}{d\Delta\phi}\left(\frac{\partial \Delta\phi}{\partial t}\right)^{2}
> $$

Enforcing the Saturation Operator defined in Axiom 4:

> **[Resultbox]** *Dielectric Saturation Taylor Expansion*
>
> $$
> \epsilon(\Delta\phi) = \epsilon_{0}\sqrt{1 - \left(\frac{\Delta\phi}{\alpha}\right)^2} \implies \epsilon(\Delta\phi) \approx \epsilon_0 \left[1 - \frac{1}{2}\left(\frac{\Delta\phi}{\alpha}\right)^2\right]
> $$

The continuous dielectric displacement $D = \epsilon(\Delta\phi) \cdot \Delta\phi$ evaluates to $D_{NL} \approx \epsilon_0 \Delta\phi - \frac{\epsilon_0}{2\alpha^2}(\Delta\phi)^3$. The stored volumetric energy density ($U$) is the integral of the field with respect to displacement ($U = \int \Delta\phi \, dD$):

> **[Resultbox]** *Euler-Heisenberg $E^4$ Correction*
>
> $$
> U \approx \frac{1}{2}\epsilon_0 (\Delta\phi)^2 - \frac{3}{8\alpha^2}\epsilon_0 (\Delta\phi)^4
> $$

The $(\Delta\phi)^4$ correction term corresponds to the energy density structure of the **Euler-Heisenberg QED Lagrangian**. The corresponding $D \propto (\Delta\phi)^3$ displacement yields the 3rd-order optical non-linearity associated with the **Kerr Effect ($\chi^{(3)}$)**.

> **Do NOT read this $E^4$ as a refractive-index scaling (anti-conflation note, 2026-06-24).** The "$E^4$" here is the **energy-density / Lagrangian** quartic — the *correct, genuinely $E^4$* term (and the upstream source of the kernel-Taylor $C(V)/C_0=1+\tfrac12A^2+\tfrac38A^4$ that the IM3 datasheet validates). The **permittivity itself is $E^2$-leading** ($\varepsilon\approx\varepsilon_0[1-\tfrac12(\Delta\phi/\alpha)^2]$, eq. above), and the **refractive-index observable** $n=\sqrt{\varepsilon/\varepsilon_0}$ gives $\delta n=\sqrt S-1\approx-\tfrac14 A^2$ — **also $E^2$-leading, NOT $E^4$**. The historical "$\delta n\propto E^4$" was a $\sqrt\varepsilon$ conflation of *this* energy-density quartic with the index shift (RETRACTED, clm-pp3qwf, [`vacuum-birefringence-e4.md`](../../../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md):41; datasheet [`vacuum-node-im3-distortion.md`](../../../vol9/ch3-pin-port-configuration/vacuum-node-im3-distortion.md)). The $\chi^{(3)}$ / cubic-in-drive IM3 read off here is **shared with QED** — not an AVE discriminator.

<!-- Figure: fig:vacuum_dielectric_saturation — Axiom 4 Saturation Observables. (Top) Constitutive permittivity epsilon_eff = epsilon_0 S(A) collapses toward zero as field strain approaches the yield limit. (Bottom) Measurable capacitance C_eff = C_0/S(A) diverges. Three regimes: I (green) Linear, II (orange) Euler-Heisenberg E^4 correction, III (red) full saturation at Schwinger pair-production threshold. -->

As the local strain approaches the yield limit, the localised wave speed $c_{eff}(\Delta\phi) = c_0 [1 - (\Delta\phi/\alpha)^2]^{-1/4}$ diverges toward infinity (due to the vanishing permittivity, $\epsilon \to 0$). Because the high-amplitude peak propagates faster than the low-amplitude base, the peak overruns the leading edge, steepening it until it topologically snaps. This forward structural shockwave provides a continuous mechanical origin for discrete pair-production.

---
