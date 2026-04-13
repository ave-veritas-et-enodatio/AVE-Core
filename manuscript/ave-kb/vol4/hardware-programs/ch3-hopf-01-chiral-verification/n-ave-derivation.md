[↑ Ch.3 HOPF-01 Chiral Verification](index.md)
<!-- leaf: verbatim -->

## The Chiral Coupling Prediction

An open-ended wire resonator of length $L_{trace}$ in a medium with effective permittivity $\varepsilon_{eff}$ resonates at:

$$
f_{std} = \frac{c}{2 L_{trace} \sqrt{\varepsilon_{eff}}}
$$

This is the prediction for a *straight, open-ended* wire resonator. For the actual 3D torus knot geometry, curvature and inter-segment coupling will cause deviations from this formula even in standard Maxwell theory. However, the AVE prediction is not about the absolute frequency, but the *scaling law* across multiple knot topologies on the same board.

The AVE framework predicts an additional correction. Because the $(p,q)$ torus knot topology couples to the intrinsic chirality of the $\mathcal{M}_A$ lattice, the effective refractive index acquires a topological term:

> **[Resultbox]** *Chiral Topological Refractive Index*
>
> $$
> n_{AVE} = \sqrt{\varepsilon_{eff}}\left(1 + \alpha \frac{pq}{p+q}\right)
> $$

where $\alpha \approx 1/137$ is the fine-structure constant and $pq/(p+q)$ is the harmonic mean of the torus knot winding numbers. This is **not a free parameter**: $\alpha$ is fixed by Axiom 2, and $p,q$ are fixed by the physical wire geometry.

The resulting frequency shift is:

> **[Resultbox]** *Topological Frequency Shift Scaling Law*
>
> $$
> \frac{\Delta f}{f_{std}} = \alpha \frac{pq}{p+q}
> $$

### Wire Length Derivation from Knot Topology

The wire length for each antenna is **not a free parameter**---it is a deterministic consequence of the knot topology $(p,q)$ at a fixed torus aspect ratio. The arc length of a $(p,q)$ torus knot with major radius $R$ and minor radius $r$ is:

$$
L_{wire} = \int_0^{2\pi} \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2}\; dt
$$

This integral depends only on $p$, $q$, and the aspect ratio $R/r$. The PCB design fixes $R/r = 2.5$ (values $R = 1.0$, $r = 0.4$ in normalized units), chosen as the minimum ratio that keeps adjacent windings separated enough for the 1.0 mm stitching holes to be resolvable by hand.

| Knot | $L_{arc}$ (norm) | Scale (mm) | $L_{wire}$ (mm) | Footprint (mm) |
|---|---|---|---|---|
| $(2,3)$ | 14.78 | 8.12 | 120 | 23 |
| $(2,5)$ | 17.95 | 8.91 | 160 | 25 |
| $(3,5)$ | 22.86 | 7.44 | 170 | 21 |
| $(3,7)$ | 26.05 | 7.68 | 200 | 21 |
| $(3,11)$ | 33.75 | 7.41 | 250 | 21 |

### Predicted Shifts

The predicted shifts for the enamel-corrected wire-in-air model ($\varepsilon_{eff} = 1.295$) are:

| Torus Knot | $pq/(p{+}q)$ | $L_{wire}$ | $f_{std}$ (GHz) | $\Delta f$ (MHz) | $Q$ | Shift (ppm) |
|---|---|---|---|---|---|---|
| $(2,3)$ Trefoil | 1.200 | 120 mm | 1.098 | 9.6 | 681 | 8,681 |
| $(2,5)$ Cinquefoil | 1.429 | 160 mm | 0.823 | 8.6 | 590 | 10,317 |
| $(3,5)$ | 1.875 | 170 mm | 0.775 | 10.6 | 566 | 13,498 |
| $(3,7)$ | 2.100 | 200 mm | 0.659 | 10.1 | 527 | 15,093 |
| $(3,11)$ | 2.357 | 250 mm | 0.527 | 9.1 | 471 | 16,910 |

All shifts exceed 8.5 MHz---easily resolvable with a VNA. All resonant frequencies fall below 1.1 GHz (well within NanoVNA-H4 range). The $(3,5)$ knot provides an intermediate data point (five knots plus the zero-topology control give six independent measurements). When submerged in mineral oil ($\varepsilon_{eff} \approx 2.265$), frequencies drop to 0.40--0.83 GHz. The ppm values are computed from the exact relation $\Delta f/f = \alpha\,pq/(p+q)\,/\,(1 + \alpha\,pq/(p+q))$.

---
