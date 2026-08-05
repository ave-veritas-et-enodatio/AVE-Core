[↑ Ch.2 General Relativity](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-07kd5v, clm-8nkvwy, clm-y9old1]
-->

---

## The Ontology of Spacetime Curvature

Einstein's General Relativity (GR) is a comprehensive framework in differential geometry. It models gravity not as a direct force, but as the curvature of a 4-dimensional Spacetime manifold caused by the presence of mass and energy.

A long-standing interpretive question in GR is the physical ontology of the manifold itself. The metric carries momentum, possesses effective inertia, and transmits waves at finite speed ($c$)---properties typically associated with a physical medium rather than pure geometry.

Applied Vacuum Engineering (AVE) resolves this ontological paradox by defining "Curved Spacetime" as the variable scalar Capacitance ($C$) and Inductance ($L$) of a structured, continuous dielectric super-fluid.

## The Stress-Energy Tensor as LC Energy Density
<!-- claim-quality: clm-y9old1 -->

The core of General Relativity is Einstein's Field Equation:

> **[Resultbox]** *Einstein Field Equation*
>
> $$
> R_{\mu\nu} - \frac{1}{2}R g_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}
> $$

In the AVE framework, the Stress-Energy Tensor ($T_{\mu\nu}$) on the right side of the equation is the classical Electromagnetic Energy Density ($U$) of the local LC vacuum:

> **[Resultbox]** *Stress-Energy as LC Energy Density*
>
> $$
> T_{\mu\nu} \equiv U_{\mu\nu} = \frac{1}{2}\epsilon_0 |\mathbf{E}|^2 + \frac{1}{2}\mu_0 |\mathbf{H}|^2
> $$

Furthermore, the mathematical Metric Tensor ($g_{\mu\nu}$) describing the curvature on the left side of the equation is isomorphic to the macroscopic structural variable impedance parameters ($\varepsilon_{eff}, \mu_{eff}$) of the dielectric matrix. Under **Symmetric Gravity**, both constitutive parameters scale with the refractive index $n(r) = 1 + 2GM/(rc^2)$:

<!-- claim-quality: clm-07kd5v (canonical statement of Symmetric-Gravity invariant impedance $Z(r) \equiv Z_0$ implying $\Gamma = 0$ across any gravitational gradient — the lossless-LIGO consistency claim) -->
<!-- claim-quality: clm-8nkvwy (Symmetric saturation case: both $\mu$ and $\varepsilon$ scale by $n \cdot S$ → $Z = Z_0$ invariant; this is the canonical statement of the symmetric branch of the Universal Saturation Kernel) -->
> **[Resultbox]** *Symmetric Gravity Impedance*
>
> $$
> \varepsilon_{eff}(r) = \varepsilon_0 \cdot n(r), \qquad
> \mu_{eff}(r) = \mu_0 \cdot n(r), \qquad
> Z(r) = \sqrt{\frac{\mu_{eff}}{\varepsilon_{eff}}} = Z_0 \;\text{(invariant)}
> $$

The Schwarzschild radius $r_s = 2GM/c^2$ marks the point where $n(r) \to \infty$ and the local strain reaches the Axiom 4 saturation limit ($S \to 0$). Under Symmetric Gravity, both $\mu_{eff}$ and $\varepsilon_{eff}$ scale together by the same factor $n(r)$, so their ratio — the **EM-transverse** constitutive impedance $Z_{EM} = \sqrt{\mu_{eff}/\varepsilon_{eff}}$ — **remains invariant at $Z_0$ everywhere**, including at $r_s$. The EM reflection coefficient $\Gamma_{EM}(r) = (Z_{EM}(r) - Z_0)/(Z_{EM}(r) + Z_0) = 0$ everywhere; **there are no EM-channel echoes** (light is transparent / index-gradient-captured). This is the physical Event Horizon — not a coordinate singularity, and not an EM impedance boundary, but a **refractive singularity** ($n \to \infty$, $c_{local} = c/n \to 0$).

> 🔴 **SCOPED 2026-06-17 (BH shear-reflect walk-back, Rule-12).** The prior
> sentence (struck through below) extended the EM-channel result ("no black
> hole echoes … perfect absorber … $\Gamma=-1$ is electron-only") to the
> shear/bulk channels — a **channel conflation**. The substrate-forced result
> is the **channel-split**, per the three-impedance law (field-symbol registry
> §3.11) and the canonical leaf
> [`electron-bh-isomorphism.md`](../../cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md):34–42:
> - **EM-transverse channel:** $Z_{EM} \equiv Z_0$ (SYM scaling), $\Gamma_{EM}
>   = 0$ — light transparent / index-captured, **no EM echoes** (correct, retained above).
> - **Shear + bulk channels:** at $r_{sat} = 7GM/c^2 = 3.5\,r_s$ the lattice
>   phase-transitions, $G_{shear} \to 0$, so $Z_{shear} = \rho\,c_{shear} \to
>   0$ (and $Z_{bulk} \to 0$) — an Op3 short giving $\Gamma_{shear} =
>   \Gamma_{bulk} = -1$. GW are **transverse shear** modes, so they **reflect
>   totally** off $r_{sat}$: **gravitational ringdown echoes ARE predicted**
>   (reflect $\Rightarrow$ echo; retrospective — reflect off a $Z\to0$ free
>   surface — not yet a SHA-pinned forward prereg). The $\Gamma = -1$ short is
>   the **universal** $Z\to0$ kernel (not electron-only): the electron applies
>   it in the bulk channel at the knot core; the BH applies it in the
>   shear+bulk channels at $r_{sat}$. Corroborated by
>   [`existing-signatures.md`](../../../vol4/falsification/ch11-experimental-bench/existing-signatures.md):36,
>   [`bulk-impedance-at-saturation-boundary.md`](../../cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md):51,
>   [`lattice-extreme-bh-rationality.md`](../../cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md):95.

~~The horizon acts as a perfect absorber (dissipative sink for shear waves entering the saturated region), not a reflective boundary. The $\Gamma = -1$ total-confinement mechanism is the **electron** confinement pattern (asymmetric magnetic-branch saturation, see Symmetric vs Asymmetric Saturation in [`claim-quality.md`](../../../claim-quality.md) and the magnetic-branch confinement passage in [`master-equation.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md)), distinct from the BH symmetric-saturation pattern.~~ *(superseded 2026-06-17 — channel conflation; see SCOPED banner above. Preserved per Rule-12.)* The asymmetric magnetic-branch passage in [`master-equation.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md) describes the electron's *bulk*-channel knot-core short; the BH realises the same $Z\to0$ short in its *shear+bulk* channels. Engine-canonical reference: [`src/ave/gravity/gw_propagation.py`](../../../../../src/ave/gravity/gw_propagation.py) (`gravitational_impedance()` / `horizon_reflection()` = EM channel $\Gamma_{EM}=0$; `shear_impedance()` / `shear_horizon_reflection()` = shear channel $\Gamma_{shear}=-1$).

When localised topological energy (mass) is present, it draws continuous phase-locked energy from the surrounding LC grid. This creates an inductive deficit in the adjacent vacuum, analogous to a density gradient in fluid dynamics. This impedance gradient ($Z = \sqrt{\mu/\epsilon}$) acts as an optical refractive index, bending the propagation trajectories of passing light and accelerating other mass-bearing geometric knots down the gradient. "Gravity" is macroscopic dielectric refraction.

## Gravitational Waves as Inductive Shear

In 2015, LIGO detected "Gravitational Waves" from merging black holes. Mainstream physics describes this as "ripples in the fabric of spacetime itself."

In the AVE framework, a black hole corresponds to a localized region of maximum dielectric saturation where the LC grid reaches its **topological yield point** at the Event Horizon — the saturation onset at $r_s$ where the lattice loses topology-supporting capacity (the bulk Regime IV ruptured-topology interior begins deeper still, at $r_{sat} = 7GM/c^2 = 3.5\,r_s$; see the BH-interior entry in [`vol3/claim-quality.md`](../../claim-quality.md)). When two such massive topological stress-concentrations orbit each other, they act as macroscopic impellers driving transverse shear waves through the electro-mechanical substrate.

In this interpretation, gravitational waves are low-frequency macroscopic inductive strain-waves propagating through the structured LC network.

By identifying the vacuum as a physical, variable-impedance LC medium, General Relativity is placed in direct correspondence with classical Continuum Mechanics and Electrodynamics. The unification of gravity with quantum field theory reduces to recognising the electromagnetic character of the spacetime substrate.

### Gravitational Wave Regime Classification

| **Source** | **Strain $h$** | **$V_{GW}/V_{snap}$** | **Regime** |
|---|---|---|---|
| GW150914 (BBH) | $10^{-21}$ | $\sim 10^{-28}$ | I (deeply linear) |
| GW170817 (BNS) | $10^{-22}$ | $\sim 10^{-29}$ | I (deeply linear) |
| Pulsar timing | $10^{-15}$ | $\sim 10^{-22}$ | I (linear) |
| Near-merger ($r \lesssim 10\,r_s$) | $10^{-1}$ | $\sim 10^{-8}$ | I--II boundary |

All observed GW signals operate far below the dielectric yield threshold. The vacuum responds linearly, producing lossless propagation at speed $c$---the mathematical predictions of linearized GR emerge exactly. The nonlinear regime (II--III) is only reached in the near-merger zone where waveform corrections become significant.

---

> **[2026-08-04 — TWO RULING PROPAGATIONS ONTO THE REGIME TABLE ABOVE. Additive: no row, number or verdict in the table is edited.]**
>
> **(1) R13 — the two columns are TWO PER-CHANNEL RULERS, not two readings of one quantity.** The table's $h$ column is a **metric-strain** ruler (its wall is $h_{yield} = \sqrt\alpha = 0.0854$) and its $V_{GW}/V_{snap}$ column is a **lattice-voltage** ruler (its wall is $1$). Across all four rows the columns are related by exactly $V_{GW}/V_{snap} = 10^{-7}h$, so the two walls sit $1.17\times10^{8}$ apart on a shared $h$ axis — which was booked as corpus-wide debt (routed follow-on **#8** of `_orchestration/docket-entries/2026-08-03-rulings-mr-batch.md`). **RULED: the $10^8$ is not a contradiction and needs no reconciliation** — a voltage-over-voltage-wall ratio and a strain-over-strain-wall ratio are different quantity kinds on different channels. **The consequence is a labelling duty, and this table is where it bites:** the **near-merger row** ($h = 10^{-1}$) is simultaneously *past yield* on the strain ruler ($h/h_{yield} = 1.171$, which is what earns its **"I–II boundary"** label) and $10^{-8}$ *of saturation* on the voltage ruler (deeply Regime I). **Both are true, of different channels.** A regime verdict quoted from this table must name **which column** it is a verdict on. *(The Regime column is left exactly as printed; it follows the strain ruler, and that is now stated rather than implied.)* ⚑ The channel **labels** (which sector owns $V_{snap}$ vs $h_{yield}$) are **flagged, not picked** — see the fuller flag with both verbatim quotes at [`ligo-gw-saturation-ratio.md`](../ch08-gravitational-waves/ligo-gw-saturation-ratio.md).
>
> **(2) R4 — the Axiom-4 kernel keys on the TOTAL LOCAL FIELD.** The internal-vs-total-field keying fork (T4) is ruled: the kernel argument $A$ is the **total local amplitude — internal plus external** — since an external field is also local field. **Consequence for this table, stated as a scope caveat rather than a re-classification:** every entry above is computed from **the source's own field alone**, so each $A$ is a **lower bound** on the total local amplitude at the measurement point, and each row's regime label is conditional on the ambient contribution being negligible **on that row's channel** — which the table does not check. ⚑ **FLAGGED, NOT COMPUTED (routed):** the same ruling dissolved the solar-system Axiom-4 boundary precisely because the *ambient* term dominated the local one there ([`oort-cloud-saturation-boundary.md`](../../cosmology/ch06-solar-system/oort-cloud-saturation-boundary.md), 2026-08-04: the Sun already sits at $g_{ext} \approx 1.8$–$2.0\,a_0$). Whether an ambient term likewise dominates for a laboratory GW detector is a **computation nobody has run**, and re-classifying rows on an un-run computation would be exactly the fiat this lane must not commit. **No row is re-classified here.**
>
> **(3) What is NOT changed by either.** Every number, the $10^{-7}$ column relation, the "far below the dielectric yield threshold" reading, and the deeply-linear-regime losslessness of the shear channel all stand. Ruling execution only; zero ids minted, zero grades moved. ⚑ The `vol3` ch08/ch15 **print** twins of both rulers are **wave-held** and untouched.
