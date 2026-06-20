[↑ Ch.12: Falsifiable Predictions](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-trgqtf, clm-pp3qwf]
-->

<!-- NOTE: sec:ee_bench label is ABSENT from Ch.12 source. Inbound \ref{sec:ee_bench} from Ch.11 is a dangling reference. This section is the intended target. -->

## The EE Bench: The Macroscopic Dielectric Plateau
<!-- claim-quality: clm-trgqtf (this section establishes $E_{yield} \approx 1.13 \times 10^{17}$ V/m as the regime boundary that PONDER-class engineering operates far below — the canonical regime classification used throughout) -->

The most accessible entry point for falsifying standard Quantum Electrodynamics (QED) is the **Vacuum Yield Limit**.

Standard electrodynamics models the vacuum permittivity ($\varepsilon_0$) as a fixed linear constant. In contrast, Axiom 4 of the AVE framework mandates that the macroscopic vacuum is a non-linear dielectric bounded by the Fine Structure Constant ($\alpha$). Because the internal topological defect limit per node evaluates to $43.65\,\text{kV}$, extending this continuous strain boundary over the macroscopic length of a single fundamental node ($\ell_{node} \approx 3.86 \times 10^{-13}\,\text{m}$) defines the structural **Macroscopic Electric Field Limit**:

$$
E_{yield} = \frac{43.65\,\text{kV}}{\ell_{node}} \approx 1.13 \times 10^{17}\,\text{V/m}
$$

As the absolute electric field gradient ($\mathbf{E}$) applied across a localized gap approaches this structural yield limit, the macroscopic vacuum enters nonlinear saturation. The constitutive permittivity *collapses* toward zero under the universal saturation kernel $S(E/E_{yield})$, while the observable capacitance *diverges* as its inverse:

<!-- claim-quality: clm-pp3qwf (SUPERSEDED comment text, preserved per Rule 12: "the Taylor expansion of this saturation kernel gives $\Delta n \propto E^4$ — the AVE leg of the $E^4$ vs QED $E^2$ vacuum-birefringence discriminator". CORRECTED 2026-06-04 (commit ad26d357): the index shift is $\delta n=\sqrt{S}-1\approx -\tfrac14(E/E_{yield})^2$, $E^2$-leading like QED; "$\propto E^4$" was a $\sqrt{\varepsilon}$ conflation of the permittivity DEPTH $1-S$. clm-pp3qwf is now the COEFFICIENT discriminator ($\sim10^6\times$ QED), not the field-exponent — an $E^2$ slope does NOT falsify AVE.) -->
$$
\varepsilon_{eff}(E) = \varepsilon_0 \cdot \sqrt{1 - \left(\frac{E}{E_{yield}}\right)^2} \;\to\; 0
\qquad
C_{eff}(E) = \frac{C_0}{\sqrt{1 - \left(\frac{E}{E_{yield}}\right)^2}} \;\to\; \infty
$$

> **Sector note (Q1 = (B), Grant-ratified 2026-06-15; `research/2026-06-15_ceff-epsilon-monotonicity_result.md`) — OPEN measurement-sector flag.** Under the (B) sector split (INVARIANT-S2), $C_0/S$ (↑) is the **longitudinal-A1 bond compliance** and $\varepsilon_{eff}=\varepsilon_0 S$ (↓) the **transverse dielectric** — orthogonal reactances. The interferometry prediction (step 2, $n\propto\sqrt{\varepsilon\mu}\propto S$, refractive-index *drop*) is unambiguously the transverse measurement and **stands**. The **LCR capacitance prediction (step 1, "spike") is sector-dependent**: a static-E LCR coupling to the transverse dielectric reads $C_{diel}\propto S$ (a *rolloff*, the bench-netlist $C_0\!\cdot\!S$ form; INVARIANT-S2:60 — "a static-E-only drive loads the ε-sector"), while one coupling to the longitudinal compliance reads $C_0/S$ (the *spike* shown). **Which sector a physical precision-LCR probes is flagged to Grant** — and that makes the spike-vs-rolloff sign itself an EE-bench discriminator between the two sectors. The "spike" prediction is **NOT silently flipped** pending that ruling.

### The Falsification Protocol

To explicitly measure this, an ultra-stiff localized dielectric gap (engineered near the Paschen curve minimum in hard vacuum to avoid atomic plasma arcing) is swept incrementally toward extreme field gradients ($> 10^{16}\,\text{V/m}$) utilizing sharp, asymmetrical emission tips.

1. **LCR Capacitance Tracking:** Using an ultra-precision LCR meter, the effective capacitance of the gap is tracked. Standard physics dictates a flat capacitance ratio. AVE dictates a capacitance spike ($C_{eff} = C_0/S \to \infty$) initiating at roughly $85\%$ of $E_{yield}$.
2. **Interferometry Tracking:** By passing a stabilized laser beam transversely through the high-voltage gap, the localized refractive index ($n_{eff} \propto \sqrt{\varepsilon_{eff} \cdot \mu_{eff}} \propto S$) can be measured via interferometric phase shift. As the macroscopic gradient approaches saturation, the optical path length *decreases* (the vacuum becomes optically thinner), registering an anomalous *drop* in refractive index.

[Figure: ee_bench_plateau_prediction.png — see manuscript/vol_4_engineering/chapters/]

The detection of this geometric asymptote prior to atomic plasma ionization unequivocally confirms the hardware limits of the spatial lattice, directly falsifying the linear continuum model.

---
