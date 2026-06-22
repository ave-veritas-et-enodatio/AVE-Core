[↑ Ch.12: Falsifiable Predictions](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-pp3qwf]
-->

## The Vacuum Birefringence Limit: the COEFFICIENT (AVE $\sim 10^7\times$ QED at the matched differential observable)

A core distinction between standard Quantum Electrodynamics (QED) and the Applied Vacuum Engineering (AVE) framework is the *magnitude* of vacuum optical nonlinearity under extreme fields — not its leading power. **Both predict an $E^2$-leading index shift; the discriminator is the COEFFICIENT.**

A birefringence instrument (polarimeter / ellipsometer, PVLAS/BMV lineage) measures the **DIFFERENCE** $n_\parallel - n_\perp$ between the two polarization eigenmodes of the pumped vacuum — a pure phase/interference observable. The isotropic (common-mode) index shift, shared by both eigenmodes, is **rejected by the instrument**. The falsifier observable is therefore the *differential*, and the AVE-vs-QED comparison must be made differential-against-differential (matched observables).

Under a linearly-polarized pump, the AVE vacuum is **uniaxial** (optic axis $\parallel$ the pump). The probe-response tensor is $\varepsilon_{ij}=\varepsilon\,\delta_{ij}+2\varepsilon' E_{0i}E_{0j}$ (the exact differential of the scalar Axiom-4 kernel $S=\sqrt{1-(E/E_{yield})^2}$, optic axis $\parallel \hat E_0$; DERIVED, OQ-1 Step 1). The two eigen-indices and the **birefringence** are

$$n_\perp = (1-A^2)^{1/4} \approx 1-\tfrac14 A^2, \qquad n_\parallel = \sqrt{\tfrac{1-2A^2}{\sqrt{1-A^2}}} \approx 1-\tfrac34 A^2,$$
$$\boxed{\;\delta n_{bir} = n_\parallel - n_\perp \approx -\tfrac12 A^2\;}\qquad A \equiv E/E_{yield}.$$

This is **negative**, **$E^2$-leading**, and **exactly $2\times$ the scalar single-arm (isotropic) shift** $\delta n_{iso}=\sqrt{S}-1\approx-\tfrac14 A^2$ — which is the **common-mode** quantity the polarimeter is blind to (see below). The AVE coefficient is O(1) against an un-suppressed yield field $E_{yield}=V_{yield}/\ell_{node}\approx 1.13\times10^{17}$ V/m.

Standard QED (Euler-Heisenberg) must be differenced the **same** way: its birefringence rides the **difference** coefficient $3/45$ (the parallel $7/45$ and perpendicular $4/45$ eigen-indices differenced — the standard Euler-Heisenberg result), not the single $7/45$. So the matched, like-for-like, field-independent ratio is

$$\frac{\delta n_{AVE}}{\delta n_{QED}} = \frac{1/2}{(3/45)\,\alpha^2}\left(\frac{E_{crit}}{E_{yield}}\right)^2 = \frac{45/6}{\alpha^3} = \frac{7.5}{\alpha^3}\quad\left(\text{using }E_{crit}=\alpha^{-1/2}E_{yield},\ \text{so }(E_{crit}/E_{yield})^2=\tfrac1\alpha\right) \approx 1.93\times10^7.$$

> **The common-mode (isotropic) shift the polarimeter is blind to.** The historical single quantity, $\delta n_{iso}=\sqrt{S}-1=(1-A^2)^{1/4}-1\approx-\tfrac14 A^2-\tfrac{3}{32}A^4+\cdots$, is the **isotropic index shift** — the *common-mode* permittivity softening shared by both eigenmodes. A birefringence instrument rejects it; it is **not** the birefringence. (Comparing this AVE single-arm $-\tfrac14 A^2$ against QED's *parallel single-mode* $7/45$ gives the **single-arm/isotropic-vs-parallel** ratio $1/(4\cdot\tfrac{7}{45}\,\alpha^3)\approx4.14\times10^6$ — a comparison of MISMATCHED observables, retained here only for traceability, **not** the falsifier headline.)

> **Provenance note.** The earlier formulation "$\Delta n_{eff} = 1 - \sqrt{1 - (E/E_{yield})^2}$, leading $E^4$ term" was a $\sqrt{\varepsilon}$ conflation: the quantity $1-S = +A^2/2 + A^4/8$ is the **permittivity saturation DEPTH** (itself $E^2$-leading, NOT $E^4$-leading), whereas the refractive-index observable is $n=\sqrt{S}$, giving $\delta n_{iso} = \sqrt{S}-1 \approx -A^2/4$. The corrected discriminator is the coefficient, not the exponent; the corrected *observable* is the par$-$perp **differential** $-\tfrac12 A^2$, not the isotropic single-arm.

> **Chord vs echo (honest split, symmetric standard).** The AVE-distinct **CHORD** is that the vacuum *saturates at all* — a tree-level O(1) birefringence-bearing structure the QED vacuum lacks (QED's birefringence is an $\alpha^2$-loop effect). The **MAGNITUDE** $1.93\times10^7=7.5/\alpha^3$ is an **$\alpha$-echo** at the value level: AVE does not derive $\alpha$, so the number rides $\alpha^{-3}$. Symmetric standard: QED's $a_{EH}\alpha^2$ is *equally* $\alpha$-rooted — QED does not derive $\alpha$ either. The chord is the existence/form; the magnitude is an echo. Do not headline the magnitude as a chord.

### The Falsification Protocol

To test this, an ultra-high-Q optical fiber ring resonator (or high-finesse Fabry-Perot cavity) is placed transverse to an extreme-voltage DC electric field (approaching $10^{16}\,\text{V/m}$).

1. A stabilized probe laser monitors the precise resonance frequency of the cavity.
2. As the DC electric field is ramped up, the local metric stiffness alters, causing a measurable phase shift ($\Delta \Phi$) and pushing the resonance fringes.
3. The shift in resonance frequency is mapped dynamically against the applied field magnitude.

[Figure: vacuum_birefringence_E4.png — see manuscript/vol_4_engineering/chapters/]

A linearly-polarized pump + a 45°-launched probe in a high-finesse cavity, read out by an ellipsometer, measures the **par$-$perp differential** $\delta n_{bir}\approx-\tfrac12 A^2$ as accumulated ellipticity $\psi$ (the birefringence readout is a polarization-**phase** difference, accumulated as ellipticity $\psi$ — a dissipationless retardance, not absorption). At the **matched differential observable**, AVE sits a field-independent $\delta n_{AVE}/\delta n_{QED}=7.5/\alpha^3\approx1.93\times10^7$ above QED's differenced Euler-Heisenberg ($3/45$) birefringence, present at **all** fields. A **QED-sized differential coefficient** ($\delta n_{bir}\sim(3/45)\alpha^2(E/E_{crit})^2$) falsifies AVE; an AVE-sized coefficient falsifies QED at this observable. (An $E^2$ slope does **not** falsify AVE — QED is also $E^2$-leading. The discriminator is the coefficient, not the exponent.)

> **OQ-1 strengthen-by — CLOSED (field→cavity-phase coupling DERIVED; FLAG-A adjudicated).** The
> field→cavity-phase coupling that maps the index shift to a polarimeter readout is now **DERIVED**
> from the scalar Axiom-4 kernel (focal-E → uniaxial probe-response tensor
> $\varepsilon_{ij}=\varepsilon\delta_{ij}+2\varepsilon'E_{0i}E_{0j}$ → cavity round-trip birefringent
> phase → ellipticity), with the geometry factor $g$ **pinned per apparatus config**: see
> [`research/2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md`](../../../../../research/2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md)
> and the facility proposal [`research/2026-06-21_birefringence-coefficient-bankable-falsifier.md`](../../../../../research/2026-06-21_birefringence-coefficient-bankable-falsifier.md).
> This closes the prior "Gaussian-overlap asserted" residual — the coupling is no longer asserted.
>
> **FLAG-A adjudicated (Grant, 2026-06-21).** A birefringence instrument measures the **par−minus−perp
> differential**, so the falsifier observable is now $\delta n_{bir}=n_\parallel-n_\perp\approx-\tfrac12 A^2$
> (DERIVED), headlined above at the matched-observable ratio $7.5/\alpha^3\approx1.93\times10^7$ (AVE
> $-\tfrac12$ vs QED differenced $3/45$). The scalar $\delta n_{iso}\approx-\tfrac14 A^2$ is retained
> as the **isotropic (common-mode) index shift** the polarimeter is blind to — **not** the
> birefringence. The single-arm/isotropic-vs-parallel ratio $4.14\times10^6$ compared MISMATCHED
> observables (AVE scalar single-arm vs QED parallel single-mode) and is no longer the falsifier
> headline; it is kept only for traceability.
>
> **Named residuals carried (do NOT over-state "closed"):**
> (a) **CHECK-3** — the gated-cavity round-trip $\tau_{rt}$ factor-of-2 / "recovers both finesse and
> temporal overlap" approximation (axial overlap integral exact; transverse/config trade study
> modeled, not uniquely derived).
> (b) **Polarimetry-floor validate-on-known** still owed against a published cavity. **The COEFFICIENT
> ($7.5/\alpha^3$) does not depend on either residual** — it is field- and apparatus-independent.

---
