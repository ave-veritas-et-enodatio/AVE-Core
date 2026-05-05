[↑ Ch.15 Black Hole Orbitals](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [395gps]
-->

## Untapped First-Principles Predictions

The impedance orbital framework immediately yields several additional falsifiable predictions that follow directly from the same $1/d$ topology without introducing any new parameters.

### Iron K$\alpha$ Line Profile from the Refractive Gradient

Accreting black holes emit a characteristic iron fluorescence line at $6.4$ keV. The observed line is broadened and redshifted by the gravitational potential. In the AVE framework, the line profile is directly computed from the refractive index gradient: photons emitted at radius $r$ are redshifted by the factor $E_{obs} = E_0 / n(r)$. The impedance band radii derived in Equation eq:impedance\_quantisation predict **discrete sub-peaks** in the broadened iron line---each corresponding to enhanced emission from a quantised impedance band in the accretion disk.

### Relativistic Jet Launching via Polar Impedance Matching

Black hole jets (Blandford-Znajek mechanism) preferentially launch along the spin axis. The impedance framework provides a direct physical explanation: the rotation axis is the only direction where the azimuthal Op14 topological strain gradient ($\varepsilon_{11,\,rot} = 0$) vanishes and the overall refractive gradient is minimised. Energy escapes along the path where the lattice strain is lowest---the polar axis is the "least strained" escape channel:

$$
\varepsilon_{11,\,polar} \ll \varepsilon_{11,\,equatorial}
$$

The equatorial accretion disk is strain-blocked; the polar axis is strain-matched. The predicted jet opening angle scales with $a_*$ as the equatorial strain metric widens with increasing rotation.

**Engine implementation.** The rupture physics described above is implemented in two modules of the `regime_4_rupture/` package:

- `rupture_solver.py`: Computes the lattice rupture state at a given strain $\varepsilon_{11}$. At $S = 0$ the effective wave speed $c_{eff} \to 0$ and the impedance diverges, triggering the phase transition documented in sec:compactness\_limit.
- `black_hole_jets.py`: Models the energy redirection at $(1-S) \to 1$. Energy that cannot propagate through the saturated interior is funnelled along the strain-minimised polar axis via the impedance gradient $\varepsilon_{11,\,polar} \ll \varepsilon_{11,\,equatorial}$.

Both modules delegate all saturation and impedance computations to Tier 1 operators.

### Gravitational Wave Memory as Residual Strain

After a gravitational wave passes, the local metric retains a permanent offset---so-called "memory" or residual strain. In the AVE dielectric framework, this is the **permanent plastic deformation** of the LC lattice after being driven past its linear elastic limit by the passing wave. The residual memory strain scales as:

> **[Resultbox]** *GW Memory from Lattice Yield*
>
> $$
> \Delta h_{memory} = h_{peak} \left(\frac{h_{peak}}{h_{yield}}\right)^2, \qquad h_{yield} = \sqrt{\alpha} \approx 0.085
> $$

This is directly analogous to a metal permanently deforming after exceeding its yield stress $\sigma_Y$. The dimensionless yield strain of the vacuum lattice $h_{yield} = \sqrt{\alpha}$ emerges from the same Axiom 4 saturation physics that defines $V_{yield}$.

### EHT Shadow Fine Structure

The Event Horizon Telescope (EHT) resolved the shadow of M87*. In the impedance model, the shadow boundary is not a sharp circle---it is modulated by the quantised impedance bands. Photons passing through different resonance band radii experience different deflection angles, producing **faint concentric fine structure** (the "photon ring" sub-images) whose spacing is predicted by the standing-wave condition (Equation eq:impedance\_quantisation). Next-generation EHT observations with improved baseline resolution could resolve these predicted rings.

[Figure: bh_untapped_predictions.png --- see manuscript/vol_3_macroscopic/chapters/]

---
