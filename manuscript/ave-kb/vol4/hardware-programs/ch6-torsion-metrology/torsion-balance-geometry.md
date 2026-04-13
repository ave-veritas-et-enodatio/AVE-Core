[↑ Ch.6 Torsion Metrology](index.md)
<!-- leaf: verbatim -->

## The Torsion Balance Architecture

A vacuum torsion balance achieves micro-Newton resolution by converting linear force into angular deflection of a suspended arm. The fundamental design parameters are:

| Parameter | Requirement | Rationale |
|---|---|---|
| Arm length | $L > 0.25$ m | Torque amplification ($\tau = F \times L$) |
| Wire diameter | $d < 25 \mu$m | Torsional compliance ($\kappa \propto d^4$) |
| Material | W or BeCu | Low hysteresis, high fatigue life |
| Sensitivity floor | $< 1 \mu$N | $>10\times$ margin below predicted signal |
| Measurement BW | 10 mHz -- 1 Hz | Reject VHF drive feedthrough |
| Vacuum | $< 10^{-5}$ Torr | Eliminate ion wind artifacts |

The angular deflection for a coaxial wire torsion balance under force $F$ applied at arm length $L$ is:

> **[Resultbox]** *Torsion Balance Angular Deflection*
>
> $$
> \theta = \frac{F \cdot L}{\kappa} = \frac{F \cdot L \cdot 2l}{\pi G_{wire} r^4}
> $$

where $\kappa$ is the torsional spring constant, $l$ is the wire length, $G_{wire}$ is the shear modulus of the suspension wire, and $r$ is the wire radius. For a $25 \mu$m tungsten wire ($G = 161$ GPa) of length 0.3 m with arm length 0.25 m, a $45 \mu$N force produces $\theta \approx 1.16$ mrad---easily measurable by optical lever (laser reflected to a PSD at 1 m gives $\sim 2.3$ mm deflection).

[Figure: ponder_01_torsion_metrology.png — see manuscript/vol_4_engineering/chapters/]

---
