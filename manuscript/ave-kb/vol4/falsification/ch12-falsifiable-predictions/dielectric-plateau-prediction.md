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

As the absolute electric field gradient ($\mathbf{E}$) applied across a localized gap approaches this structural yield limit, the macroscopic vacuum enters nonlinear saturation. The constitutive **transverse-$T_2$** permittivity *rolls off* toward zero under the universal saturation kernel $S(E/E_{yield})=\sqrt{1-(E/E_{yield})^2}$, and the **observable across-gap capacitance rolls off with it** — an LCR meter couples to this transverse dielectric ($C_{diel}=\varepsilon_{eff}A/d\propto S$), *not* to the orthogonal longitudinal-$A_1$ bond compliance whose $C_0/S$ *divergence* is keyed on the higher $V_{snap}\approx511$ kV (ruling chain: `ave-kb/CLAUDE.md`:73 Grant-ratified sector split; `def-vyvsn1` = $T_2$ self-trap wall, Grant 2026-06-30; the 2026-07-03 sector-keying fix; the node-up sector-keying supersession + tangent crowning, landed PR #562 / payload PR #558, Grant-ratified 2026-07-06). The constitutive transverse-dielectric forms are therefore:

<!-- claim-quality: clm-pp3qwf (SUPERSEDED comment text, preserved per Rule 12: "the Taylor expansion of this saturation kernel gives $\Delta n \propto E^4$ — the AVE leg of the $E^4$ vs QED $E^2$ vacuum-birefringence discriminator". CORRECTED 2026-06-04 (commit ad26d357): the index shift is $\delta n=\sqrt{S}-1\approx -\tfrac14(E/E_{yield})^2$, $E^2$-leading like QED; "$\propto E^4$" was a $\sqrt{\varepsilon}$ conflation of the permittivity DEPTH $1-S$. clm-pp3qwf is now the COEFFICIENT discriminator ($\sim10^6\times$ QED), not the field-exponent — an $E^2$ slope does NOT falsify AVE.) -->
$$
\varepsilon_{eff}(E) = \varepsilon_0 \cdot \sqrt{1 - \left(\frac{E}{E_{yield}}\right)^2} \;\to\; 0
\qquad
C_{diel}(E) = C_0 \cdot \sqrt{1 - \left(\frac{E}{E_{yield}}\right)^2} \;\to\; 0
$$

Writing $S\equiv\sqrt{1-(E/E_{yield})^2}$ and $A\equiv E/E_{yield}$: the transverse permittivity and the physical **large-signal (chord) gap capacitance** $C_{diel}=C_0 S$ *roll off* together (leading order $1-\tfrac12 A^2$). The **small-signal tangent** an LCR meter actually reports, $C_{ss}=dQ/dV=C_0\,(S-A^2/S)$, falls faster ($1-\tfrac32 A^2$ to leading order) and **crosses zero at $E/E_{yield}=1/\sqrt2$** (where $S^2=A^2$; equivalently the parallel probe eigenmode $n_\parallel=\sqrt{S-A^2/S}$ goes imaginary for $A^2>\tfrac12$). The divergent $C_0/S\to\infty$ form is instead the *orthogonal* longitudinal-$A_1$ bond compliance, keyed on $V_{snap}\approx511$ kV — a different reactance an across-gap LCR meter does not read. (Canonical tangent/chord split + $1/\sqrt2$ zero: node-up `ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md` §1; C-V dip RESULT `research/2026-07-07_semiconductor-cv-dip_RESULT.md`.)

> **Sector note (Q1 = (B), Grant-ratified 2026-06-15; `research/2026-06-15_ceff-epsilon-monotonicity_result.md`) — ✅ RESOLVED 2026-07-07 (status updated, historical text preserved per house convention).** *Resolution:* an across-gap precision LCR meter couples to the **transverse-$T_2$ dielectric**, so it reads the **roll-off** $C_{diel}=\varepsilon_{eff}A/d\propto S$ (keyed on $V_{yield}\approx43.65$ kV) — **not** a spike. The $C_0/S$ (↑) *divergence* is the **orthogonal longitudinal-$A_1$ bond compliance**, keyed on the higher $V_{snap}\approx511$ kV, which the across-gap meter does not read. The step-1 prediction is therefore the roll-off (now fixed in the body above); the *sign* of the deviation is itself the $T_2$-vs-$A_1$ sector discriminator. **Ruling chain that settles the former flag:** `ave-kb/CLAUDE.md`:73 (Grant-ratified sector split); `def-vyvsn1` = $T_2$ self-trap wall (Grant 2026-06-30); the 2026-07-03 sector-keying fix; the node-up sector-keying supersession + tangent crowning (landed PR #562 / payload PR #558, Grant-ratified 2026-07-06). The step-2 interferometry index is $n_{eff}=\sqrt{\varepsilon_{eff}/\varepsilon_0}=\sqrt S$ (a static field loads $\varepsilon$ only, $\mu$ unchanged; the refractive-index *drop* stands — reconciled from the earlier $\propto S$ both-scale wording to $n_\perp=\sqrt S$ per node-up R2 and clm-pp3qwf). — *Historical (now superseded):* under the (B) split $C_0/S$ (↑) is the longitudinal-A1 bond compliance and $\varepsilon_{eff}=\varepsilon_0 S$ (↓) the transverse dielectric — orthogonal reactances; which sector a physical precision-LCR probes was flagged to Grant and the "spike" was **NOT silently flipped pending that ruling** (INVARIANT-S2:60 — "a static-E-only drive loads the ε-sector"). That ruling has since been made (chain above), so the flag is resolved and the body now reads the $T_2$ roll-off.

### The Falsification Protocol

To explicitly measure this, an ultra-stiff localized dielectric gap (engineered near the Paschen curve minimum in hard vacuum to avoid atomic plasma arcing) is swept incrementally toward extreme field gradients ($> 10^{16}\,\text{V/m}$) utilizing sharp, asymmetrical emission tips.

1. **LCR Capacitance Tracking (transverse-$T_2$ dielectric, keyed on $V_{yield}$):** Using an ultra-precision LCR meter, the small-signal capacitance of the gap is tracked. Standard physics dictates a flat capacitance ratio ($C=C_0$) up to arc-discharge. AVE dictates a capacitance **roll-off**, *not* a spike: the transverse permittivity $\varepsilon_{eff}=\varepsilon_0 S$ saturates, so the large-signal (chord) gap capacitance $C_{diel}=C_0 S$ falls as $1-\tfrac12(E/E_{yield})^2$, and the small-signal (tangent) capacitance the meter reports, $C_{ss}=dQ/dV=C_0(S-A^2/S)$, falls faster ($1-\tfrac32(E/E_{yield})^2$ to leading order) and passes through zero near $E/E_{yield}=1/\sqrt2$. The measurable "anomaly window" — where $C$ deviates by more than $10\%$ from the flat baseline — spans roughly $0.85\,E_{yield}$ to $E_{yield}$ (`ave-kb/vol4/simulation/ch17-hardware-netlists/ee-bench-netlist.md`). *Discriminating signature:* the **sign** of the deviation — a roll-off toward zero, **not** a $C_0/S$ divergence (that divergent form is the orthogonal longitudinal-$A_1$ bond compliance keyed on $V_{snap}\approx511$ kV, which an across-gap LCR meter does not read).
2. **Interferometry Tracking (transverse-$T_2$ index, static-E loads $\varepsilon$ only):** By passing a stabilized laser beam transversely through the high-voltage gap, the localized refractive index ($n_{eff} = \sqrt{\varepsilon_{eff}\mu_{eff}/(\varepsilon_0\mu_0)} = \sqrt{S}$, since a static field loads $\varepsilon$ only and leaves $\mu$ unchanged) can be measured via interferometric phase shift. As the macroscopic gradient approaches saturation, the optical path length *decreases* (the vacuum becomes optically thinner), registering an anomalous *drop* in refractive index ($\delta n\approx-\tfrac14(E/E_{yield})^2$; canonical $n_\perp=\sqrt S$ per node-up R2 and clm-pp3qwf).

[Figure: ee_bench_plateau_prediction.png — see manuscript/vol_4_engineering/chapters/ — **pending regen:** the current PNG renders the superseded $C_0/S$ spike; the corrected panel plots the $C_{ss}=C_0(S-A^2/S)$ roll-off through zero at $E/E_{yield}=1/\sqrt2$ and the $n=\sqrt S$ index drop (no figure driver exists yet — follow-on artifact task).]

The detection of this geometric saturation roll-off prior to atomic plasma ionization confirms the hardware limits of the spatial lattice, directly falsifying the linear continuum model.

---
