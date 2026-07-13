[↑ Falsification](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: [clm-9sujp8, clm-acgyr1, clm-fofwr1, clm-gg4wmx, clm-gw2wgc, clm-i02mhk, clm-k4d4ph, clm-om0rtq, clm-pp3qwf, clm-qx9bb8, clm-sve3xc, clm-to41c7, clm-trgqtf, clm-wcoul2]
subtree-experiments: []
-->

# Ch.12: Falsifiable Predictions and Experimental Blueprints

Three explicit experimental blueprints designed to definitively measure the structural invariants of the topological vacuum, plus additional falsification tests: Sagnac RLVG impedance drag, helicity injection, autoresonant dielectric rupture, binary kill-switches, vacuum birefringence ~~$E^4$ scaling~~ COEFFICIENT discriminator (both $E^2$-leading; $\sim 10^6\times$ QED — clm-pp3qwf, Rule-12 correction 2026-06-04), and torus knot baryon mass predictions.

## Key Results

| Result | Expression | Source |
|---|---|---|
| Macroscopic field limit | $E_{yield} = 43.65\,\text{kV}/\ell_{node} \approx 1.13 \times 10^{17}\,\text{V/m}$ | dielectric-plateau |
| Across-gap capacitance roll-off ($T_2$ dielectric) | $C_{diel}(E) = C_0\sqrt{1-(E/E_{yield})^2} \to 0$; tangent $C_{ss}=C_0(S-A^2/S)$ zeros at $E/E_{yield}=1/\sqrt2$ | dielectric-plateau |
| Active Sagnac Interferometry | Phase shift scales with $\rho_m$, $\mu_r$, altitude, latitude, and ambient $B$-field | active-sagnac-interferometry |
| Torus knot baryon masses | $(2,17)$: $\sim 2742\,\text{MeV}$; $(2,19)$: $\sim 2983\,\text{MeV}$; $(2,21)$: $\sim 3199\,\text{MeV}$ — testable at CLAS12/PANDA | torus-knot-baryon |
| Dielectric plateau / NDC onset | tangent $C_{ss}$ crosses zero (NDC snap-back) at $E/E_{yield}=1/\sqrt2\approx0.707$; tracking window opens $\gtrsim0.25\,E_{yield}$ | ee-bench |
| Active Sagnac tolerance | Zerodur cavity, $< 1$ mK thermal, $< 46$ kHz linewidth, sub-pm seismic | active-sagnac-telemetry |
| Autoresonant PLL | Phase-locked frequency tracking enables vacuum rupture at fractional Schwinger energy | autoresonant |

> **★ Supersession (KEEP-BOTH; roll-off ruling ratified 2026-07-06/07, PR #562/#558).** The two capacitance rows above formerly read a **spike, sign-inverted** vs the ratified across-gap roll-off: *"Capacitance divergence — $C_{eff}(E)=C_0/\sqrt{1-(E/E_{yield})^2}\to\infty$"* and *"Dielectric plateau onset — $C_{eff}\to\infty$ at $E\approx0.85\times E_{yield}$"*, and the detail row said *"capacitance spike"*. An across-gap precision LCR couples to the **transverse-$T_2$ dielectric** (roll-off $C\propto S$, keyed on $V_{yield}\approx43.65$ kV); the $C_0/S\to\infty$ divergence is the **orthogonal longitudinal-$A_1$ bond compliance keyed on $V_{snap}\approx511$ kV**, which the across-gap meter does not read. Corrected to the roll-off + $1/\sqrt2$ tangent NDC per [`dielectric-plateau-prediction.md`](dielectric-plateau-prediction.md):25-38.

## Derivations and Detail (Detailed Leaves — Benn)

| Document | Contents |
|---|---|
| [Dielectric Plateau Prediction](dielectric-plateau-prediction.md) | EE Bench: $E_{yield}$, across-gap capacitance roll-off + $1/\sqrt2$ NDC snap-back, interferometric refractive index drop; LCR + laser protocol |
| Ponder-01 Thrust Prediction (see AVE-PONDER repo) | Asymmetric Maxwell Stress Rectification; 1000:1 geometry; VHF sweep; torsion balance protocol |
| [Epistemology (Ch.12)](epistemology-ch12.md) | One-Parameter Effective Field Theory; falsifiability by design |
| [Active Sagnac Impedance Drag](active-sagnac-impedance-drag.md) | Kinematic/electromagnetic entrainment law; density and permeability dependence; tolerances; applied telemetry (slip-velocity, gradient compass, dark wake, chiral torsion) |
| [Helicity Injection](helicity-injection.md) | Polarization matching; Hopf Configuration ($\mathbf{A} \parallel \mathbf{B}$); topological power factor correction |
| [Autoresonant Dielectric Rupture](autoresonant-dielectric-rupture.md) | Schwinger limit bypass via PLL; nonlinear detuning; low-power pair production |
| [Binary Kill-Switches](binary-kill-switches.md) | Neutrino Parity Test; GRB Dispersion Test |
| [Vacuum Birefringence COEFFICIENT](vacuum-birefringence-e4.md) | ~~$E^2$ vs $E^4$ slope~~ → COEFFICIENT ratio $\sim 10^6\times$ QED (both $E^2$-leading; Rule-12 clm-pp3qwf); optical cavity protocol |
| [Field-Free Optical Activity](field-free-optical-activity.md) | Parity ZERO-vs-NONZERO FORM chord (QED structurally 0); signed / enantiomorph-odd / diamond-null (clm-fofwr1); MAGNITUDE NOT bankable (40 OOM over bound, $k\to0$ continuum OPEN) |
| [Chiral Mechanical & Acoustic Gyrotropy](chiral-mechanical-gyrotropy.md) | $k$-linear gyrotropy PERMITTED by srs $432$ / FORBIDDEN by diamond $m\bar3m$; geometry-fixed, parity-odd, diamond-null (clm-acgyr1); mechanical (PR #508) + photon (PR #515) faces; MAGNITUDE below-bound ($\sim$11 OOM below SME), CONSISTENCY-class not near-term |
| [Torus Knot Baryon Predictions](torus-knot-baryon-predictions.md) | $(2,q)$ mass ladder; 6 retrospective matches; 3 forward predictions; $\sim 170\,\text{MeV}$ spacing |

## Derivations and Detail (Consolidated — Grant)

| Document | Contents |
|---|---|
| [EE Bench Dielectric Plateau](ee-bench-plateau.md) | LCR capacitance tracking, interferometric refractive index, Paschen vacuum gap, PONDER-01 stress rectification |
| [Active Sagnac & Metric Telemetry](active-sagnac-telemetry.md) | Material-dependent entrainment, density/permeability sweep, slip-velocity sensor, gradient compass, dark wake sensor, chiral torsion sensor |
| [Autoresonant Rupture & Helicity Injection](autoresonant-helicity.md) | Autoresonant PLL Schwinger limit, Hopf coil power factor correction |
| [Baryon Mass Predictions](baryon-mass-predictions.md) | Torus knot ladder forward predictions, CLAS12/PANDA search targets, falsification protocol |

> **Note:** `summarybox` and `exercisebox` environments in the source chapter are not extracted as leaves in this KB.

---
