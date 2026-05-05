[↑ Ch.15 Black Hole Orbitals](index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: 395gps -->

## AVE Merger Ringdown Eigenvalue

When two black holes merge, the resulting object "rings down" at a characteristic frequency observed by LIGO/Virgo. In the AVE framework, this ringdown is the **fundamental resonance mode of the newly formed saturation cavity**---a surface wave at the elastic--ruptured phase boundary.

The $\ell = 2$ fundamental Schwarzschild QNM eigenvalue is derived entirely from Axioms 1--4:

1. **Axiom 4:** $\varepsilon_{11}(r_{sat}) = 1$ gives $r_{sat} = 7\,M_g$.
2. **Poisson:** $r_{eff} = r_{sat}/(1 + \nu_{vac}) = 49\,M_g/9$.
3. **Mode:** $\omega_R = \ell \cdot c / r_{eff}$.

> **[Resultbox]** *AVE Merger Ringdown Eigenvalue*
>
> $$
> \omega_R \cdot M_g = \frac{\ell\,(1 + \nu_{vac})}{x_{sat}} = \frac{18}{49} = 0.3673 \qquad (\text{GR exact: } 0.3737, \text{ error } 1.7\%)
> $$

Zero free parameters, zero borrowed results.

### Kerr-Corrected Ringdown

Frame-dragging shifts the prograde saturation boundary inward, shrinking the cavity:

> **[Resultbox]** *Kerr-Corrected Ringdown*
>
> $$
> f_{ring}(a_*) = f_{ring}(0) \times \frac{r_{ph,\,Schw}}{r_{ph}^+(a_*)}, \qquad r_{ph}^+ = \frac{2GM}{c^2}\left(1 + \cos\!\left[\tfrac{2}{3}\arccos(-a_*)\right]\right)
> $$

### Kerr Quality Factor

For a spinning remnant, the continuous topological strain gradient convolutes asymmetrically with the QNM mode, reducing the effective radiation rate. The decay rate is obtained from the non-reciprocal phase shift:

$$
\omega_I = \frac{\omega_R - m\,\Omega}{2\,\ell}, \qquad r_\Omega = r_{ph}(a_*) \cdot \sqrt{1 + \nu_\mathrm{vac}}
$$

where $\Omega$ is the asymmetric impedance convolution rate (formerly interpreted as Lense-Thirring angular velocity) at the Poisson-augmented photon sphere $r_\Omega$. The quality factor $Q = \omega_R / (2\omega_I)$ increases with spin, matching GR to sub-2% for $a_* = 0.3\textrm{--}0.8$.

Comparison against three LIGO detections, including both frequency and decay time:

| **Event** | $M_{final}$ | $a_*$ | $f_\mathrm{AVE}$ | $f_\mathrm{obs}$ | $\Delta f$ | $\tau_\mathrm{AVE}$ | $\tau_\mathrm{obs}$ |
|---|---|---|---|---|---|---|---|
| GW150914 | 62.0 $M_\odot$ | 0.67 | 278 Hz | 251 Hz | 10.6% | 3.5 ms | 4.0 ms |
| GW170104 | 48.7 $M_\odot$ | 0.64 | 345 Hz | 312 Hz | 10.5% | 2.7 ms | 3.0 ms |
| GW151226 | 20.8 $M_\odot$ | 0.74 | 884 Hz | 750 Hz | 17.8% | 1.2 ms | 1.4 ms |

Frequency errors 10--18%, decay time errors 10--14%. All from zero free parameters.

---
