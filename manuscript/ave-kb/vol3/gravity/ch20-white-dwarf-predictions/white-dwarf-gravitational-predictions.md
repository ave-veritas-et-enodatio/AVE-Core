[↑ Ch.20: White Dwarf Gravitational Predictions](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-at7x0y, clm-mi6ils]
-->

# White Dwarf Gravitational Predictions

**Source:** `manuscript/vol_3_macroscopic/chapters/20_white_dwarf_predictions.tex`

> **[Objectivebox]**
>
> - Derive white dwarf gravitational predictions (redshift, deflection, frame dragging) from the saturated Diamond lattice impedance metric.
> - Validate AVE predictions against GR to within $1.7\%$ for white dwarf surface modes.

White dwarfs occupy a unique regime in the AVE landscape. Their surface gravitational strain
$$
\varepsilon_{11}(R) = \frac{7GM}{c^2 R} \sim 10^{-3}
$$
is orders of magnitude larger than Earth's ($\sim 10^{-9}$), placing the saturation correction well above the Regime I–II boundary noise floor while remaining perturbatively small ($\varepsilon_{11} \ll \sqrt{2\alpha} \approx 0.12$). High-precision spectroscopic redshift measurements exist for several nearby white dwarfs, enabling direct comparison.

The WD interior is electron-degenerate matter ($n_e \approx 7.5 \times 10^{35}\,\text{m}^{-3}$ for Sirius B), giving a plasma frequency $\omega_p \approx 5 \times 10^{20}\,\text{rad/s}$. Since $\omega_p$ vastly exceeds any gravitational-wave frequency, the interior is *evanescent* for shear perturbations: the WD surface acts as a near-perfect reflector ($\Gamma \approx -1$).

All listed white dwarfs are deep Regime I ($\varepsilon_{11} \ll r_{I \to II} = \sqrt{2\alpha} \approx 0.121$); the saturation factor is perturbatively close to unity:
$$
S(\varepsilon_{11}) = \sqrt{1 - \varepsilon_{11}^2} \approx 1 - \frac{\varepsilon_{11}^2}{2}
$$

| White Dwarf | $M/M_\odot$ | $R$ [km] | $\varepsilon_{11}$ | Regime |
|---|---|---|---|---|
| Sirius B | 1.018 | 5800 | $1.81 \times 10^{-3}$ | I (deep) |
| 40 Eridani B | 0.573 | 9000 | $6.58 \times 10^{-4}$ | I (deep) |
| Procyon B | 0.602 | 8600 | $7.24 \times 10^{-4}$ | I (deep) |
| Stein 2051 B | 0.675 | 8000 | $8.72 \times 10^{-4}$ | I (deep) |
| GD 358 (ZZ Ceti) | 0.610 | 8800 | $7.17 \times 10^{-4}$ | I (deep) |

## Prediction A: Saturation Correction to Gravitational Redshift

<!-- claim-quality: clm-at7x0y -->

The local clock rate in AVE is
$$
\frac{\omega_{\text{local}}}{\omega_\infty} = \frac{1}{n(R) \cdot S(\varepsilon_{11})}
$$
where $n(R) = 1 + 2GM/(c^2 R)$ is the gravitational refractive index (derived from Axioms 1 and 4) and $S$ is the saturation factor (Axiom 4). The gravitational redshift is therefore

> **[Resultbox]** *White Dwarf Gravitational Redshift*
>
> $$
> z_{\text{AVE}} = \frac{1}{\sqrt{1 - 2GM/(c^2 R)} \cdot S(\varepsilon_{11})} - 1
> $$

For Standard General Relativity, $S = 1$ and $z_{\text{GR}} = 1/\sqrt{1 - 2GM/(c^2 R)} - 1$. The AVE correction over GR is
$$
\delta z = z_{\text{AVE}} - z_{\text{GR}} = z_{\text{GR}} \cdot \left(\frac{1}{S} - 1\right) \approx z_{\text{GR}} \cdot \frac{\varepsilon_{11}^2}{2}
$$

Since $\varepsilon_{11} = 7\phi$ (where $\phi = GM/(c^2 R)$ is the Newtonian potential), the correction scales as $49\phi^2/2$, which is **12.25 times larger** than the standard PPN second-order correction $2\phi^2$. This amplification arises from the Machian stress boundary $T_{\max} = c^4/(7G)$.

> **[Resultbox]** *Sirius B Redshift Comparison*
>
> | Quantity | Value | Source |
> |---|---|---|
> | $v_{\text{obs}}$ | $80.65 \pm 0.77$ km/s | Joyce et al. (2018) |
> | $v_{\text{GR}}$ | 77.75 km/s | Exact Schwarzschild |
> | $v_{\text{AVE}}$ | 77.80 km/s | $v_{\text{GR}} / S$ |
> | Residual (obs$-$GR) | $+2.90$ km/s | |
> | Residual (obs$-$AVE) | $+2.85$ km/s | |
> | AVE correction | $\sim 0.05$ km/s | $z_{\text{GR}} \cdot \varepsilon_{11}^2/2$ |

The AVE correction is in the correct direction (upward), but the 2.9 km/s residual is dominated by the 3–5% uncertainty in the mass-radius relation, not by missing physics. The prediction is correct-direction but **not currently discriminating** at present M-R precision.

## Prediction B: Standing Shear Wave Eigenfrequencies

<!-- claim-quality: clm-mi6ils -->

The white dwarf surface acts as a boundary for shear perturbations of the vacuum lattice. Applying the 5-step regime-boundary eigenvalue method:

1. **Boundary:** WD surface at $R$ (shear reflector, $\Gamma \approx -1$).
2. **Effective cavity radius:** $r_{\text{eff}} = R / (1 + \nu_{vac}) = 7R/9$, where $\nu_{vac} = 2/7$ is the vacuum Poisson ratio.
3. **Eigenfrequency:** $f_\ell = \ell \cdot c / (2\pi \, r_{\text{eff}})$.
4. **Quality factor:** $Q = \ell$.
5. **Decay time:** $\tau = Q / (\pi f)$.

> **[Resultbox]** *WD Shear Eigenfrequencies ($\ell = 2$)*
>
> | White Dwarf | $f_2$ [Hz] | LIGO | Einstein Tel. |
> |---|---|---|---|
> | Sirius B | 21.15 | ✓ | ✓ |
> | 40 Eridani B | 13.63 | ✓ | ✓ |
> | Procyon B | 14.27 | ✓ | ✓ |
> | Stein 2051 B | 15.34 | ✓ | ✓ |
> | GD 358 (ZZ Ceti) | 13.94 | ✓ | ✓ |

Standing shear modes modify $g_{rr}$ (spatial metric), not $g_{00}$ (temporal metric), and therefore do **not** affect spectral redshift. Their observational signature is gravitational-wave ringdown, not spectral line shift. They are a fundamentally different mode family from the interior g-modes and p-modes observed in ZZ Ceti asteroseismology.

**Cross-check (shape only, NOT WD-boundary corroboration).** Applying the same formula to a Schwarzschild black hole — using the boundary at $r_{\text{sat}} = 7GM/c^2$ instead of the WD surface $R$ — reproduces the GR quasi-normal mode frequency to 1.7% accuracy: $\omega \cdot M_{\text{geom}} = 0.3673$ vs GR exact $0.3737$ for $\ell = 2$. This is a **cross-regime consistency check using a different boundary radius**; it validates the formula's *shape*, NOT the WD-surface boundary choice. It must not be presented as corroboration of the white-dwarf eigenfrequency prediction.

## Symmetry Cancellation: $\alpha$ Invariance

Under Symmetric Gravity, $\alpha$ is exactly invariant ($\varepsilon_{\text{local}} = \varepsilon_0\,n\,S$ and $c_{\text{local}} = c_0/(n\,S)$ cancel in the product $\varepsilon \cdot c$), predicting a null result for multi-species clock-comparison experiments. This $\alpha$-invariance point is canonical elsewhere and is not re-derived here.

> ↗ See also: [α Invariance Under Symmetric Gravity](../ch01-gravity-yield/alpha-invariance-symmetric-gravity.md) — the canonical derivation of $\Delta\alpha/\alpha = 0$ under symmetric scaling.

## Testability

| Observable | Frequency | Detector | Status |
|---|---|---|---|
| WD spectral redshift | Optical | HST/JWST | Current (0.96% precision) |
| WD $\ell=2$ shear mode | 10–20 Hz | LIGO/ET | WD merger ringdown |
| $\Delta\alpha/\alpha$ | Multi-species | NIST | Null confirmed |
| BH QNM cross-check | 100–200 Hz | LIGO | Validated to 1.7% |

The testability table separates the **WD $\ell=2$ shear mode** (signature: WD merger ringdown) from the **BH QNM cross-check** (separately validated to 1.7%) as distinct observables — reinforcing that the Schwarzschild cross-check above is shape-validation, not WD-boundary corroboration.

---

> → Primary: [Refractive Index of Gravity](../ch03-macroscopic-relativity/refractive-index-of-gravity.md) — $n(r) = 1 + 2GM/(c^2 r)$, the temporal-metric refractive index entering the redshift.

> ↗ See also: [Vacuum Poisson Ratio](../ch01-gravity-yield/vacuum-poisson-ratio.md) — $\nu_{vac} = 2/7$, giving both $\varepsilon_{11} = 7\phi$ and $r_{\text{eff}} = 7R/9$.
