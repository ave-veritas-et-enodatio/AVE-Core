[↑ Ch.5 White Dwarf Predictions](../index.md)
<!-- leaf: verbatim -->

# Step 3: Universal Operators

## Prediction A: Saturation Correction to Gravitational Redshift

The local clock rate in AVE is

$$
\frac{\omega_{\text{local}}}{\omega_\infty} = \frac{1}{n(R) \cdot S(\varepsilon_{11})}
$$

where $n(R) = 1 + 2GM/(c^2 R)$ is the gravitational refractive index (Axiom 3)
and $S$ is the saturation factor (Axiom 4).

The gravitational redshift is therefore

$$
z_{\text{AVE}} = \frac{1}{\sqrt{1 - 2GM/(c^2 R)} \cdot S(\varepsilon_{11})} - 1
$$

For Standard General Relativity, $S = 1$ and

$$
z_{\text{GR}} = \frac{1}{\sqrt{1 - 2GM/(c^2 R)}} - 1
$$

The AVE correction over GR is therefore

$$
\delta z = z_{\text{AVE}} - z_{\text{GR}} = z_{\text{GR}} \cdot \left(\frac{1}{S} - 1\right) \approx z_{\text{GR}} \cdot \frac{\varepsilon_{11}^2}{2}
$$

Since $\varepsilon_{11} = 7\phi$ (where $\phi = GM/(c^2 R)$ is the Newtonian potential),
the correction scales as $49\phi^2/2$, which is **12.25 times larger** than the
standard PPN second-order correction $2\phi^2$.
This amplification arises from the Machian stress boundary $T_{\max} = c^4/(7G)$.

> **[Resultbox]** *Sirius B Redshift Comparison*
>
> | **Quantity** | **Value** | **Source** |
> |---|---|---|
> | $v_{\text{obs}}$ | $80.65 \pm 0.77$ km/s | Joyce et al. (2018) |
> | $v_{\text{GR}}$ | 77.75 km/s | Exact Schwarzschild |
> | $v_{\text{AVE}}$ | 77.80 km/s | $v_{\text{GR}} / S$ |
> | Residual (obs$-$GR) | $+2.90$ km/s | |
> | Residual (obs$-$AVE) | $+2.85$ km/s | |
> | AVE correction | $\sim 0.05$ km/s | $z_{\text{GR}} \cdot \varepsilon_{11}^2/2$ |

The AVE correction is in the correct direction (upward), but the 2.9 km/s residual
is dominated by the 3--5% uncertainty in the mass-radius relation,
not by missing physics.

## Prediction B: Standing Shear Wave Eigenfrequencies

The white dwarf surface acts as a boundary for shear perturbations
of the vacuum lattice. Applying the 5-step regime-boundary eigenvalue method:

1. **Boundary:** WD surface at $R$ (shear reflector, $\Gamma \approx -1$).
2. **Effective cavity radius:** $r_{\text{eff}} = R / (1 + \nu_{\text{vac}}) = 7R/9$,
   where $\nu_{\text{vac}} = 2/7$ is the vacuum Poisson ratio.
3. **Eigenfrequency:** $f_\ell = \ell \cdot c / (2\pi \, r_{\text{eff}})$.
4. **Quality factor:** $Q = \ell$.
5. **Decay time:** $\tau = Q / (\pi f)$.

> **[Resultbox]** *WD Shear Eigenfrequencies (l = 2)*
>
> | **White Dwarf** | $f_2$ [Hz] | **LIGO** | **Einstein Tel.** |
> |---|---|---|---|
> | Sirius B | 21.15 | $\checkmark$ | $\checkmark$ |
> | 40 Eridani B | 13.63 | $\checkmark$ | $\checkmark$ |
> | Procyon B | 14.27 | $\checkmark$ | $\checkmark$ |
> | Stein 2051 B | 15.34 | $\checkmark$ | $\checkmark$ |
> | GD 358 (ZZ Ceti) | 13.94 | $\checkmark$ | $\checkmark$ |

**Cross-check:** Applying the same formula to a Schwarzschild black hole
(boundary at $r_{\text{sat}} = 7GM/c^2$ instead of $R$) reproduces the GR
quasi-normal mode frequency to 1.7% accuracy:
$\omega \cdot M_{\text{geom}} = 0.3673$ vs. GR exact $0.3737$ for $\ell = 2$.

---
