[↑ Ch.15 Black Hole Orbitals](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-395gps]
-->

## Untapped First-Principles Predictions

The impedance orbital framework immediately yields several additional falsifiable predictions that follow directly from the same $1/d$ topology without introducing any new parameters.

### Near-Extremal Ringdown Overshoot: $\omega_R M_g \to 54/49$ as $a_* \to 1$

> **[Resultbox]** *Near-Extremal Ringdown Limit (AVE-distinct forward prediction)*
>
> $$
> \omega_R M_g \xrightarrow[a_* \to 1]{} \frac{\ell(1 + \nu_{vac})}{x_{sat,v1}(1)} = \frac{18}{49/3} = \frac{54}{49} \approx 1.102 \qquad (\text{ZDM limit } m/2 = 1;\ \text{AVE overshoots by } +10.2\%)
> $$

Under the standing v1 spin mapping ($x_{sat,v1} = 7\,r_{ph}^+/3M$, whole-cavity-compliant; re-selected as canonical per **Grant Ruling B1, 2026-07-21** — see [`ave-merger-ringdown-eigenvalue.md` § GRANT RULING](ave-merger-ringdown-eigenvalue.md)), the fundamental $\ell=2$ ringdown eigenvalue **rises toward the exact zero-damped-mode (ZDM) limit** as the remnant approaches extremal spin. Because $r_{ph}^+ \to M$ at $a_* \to 1$, $x_{sat,v1} = 7\,r_{ph}^+/3M \to 7/3$, giving $\omega_R M_g \to \ell(1+\nu_{vac})/x_{sat,v1} = 2\cdot(9/7)/(7/3) = 54/49 = 1.102$. This is **an AVE-distinct near-extremal forward prediction**: v1 overshoots the GR ZDM limit $m/2 = 1$ by $+10.2\%$, testable once LIGO/LISA/ET resolves a **near-extremal ($a_* \gtrsim 0.9$)** ringdown (none in the current catalog). Live promotion under Ruling B1: from routed-candidate to **LIVE FORWARD PREDICTION** at the clm-395gps-inherited grade (**solidity 0.55, disclosed-phenomenological, mapping-conditional; ★provenance rider (#780 review F5): the DEVIATION FORM (+10.2% overshoot rising toward the ZDM limit) is the AVE-distinct content — the ABSOLUTE value 54/49 embeds the GR-imported ν_vac = 2/7 via K=2G (form-deriving-value-importing.md; PR#261), and that value-import rider travels wherever 54/49 is load-bearing** — v1 is the standing mapping).

The near-extremal axis is a **qualitative discriminator between the two spin mappings**: v1 *rises toward* the ZDM limit (qualitatively correct sign), whereas the superseded v2 mapping **floors at $54/77 \approx 0.701$** ($-29.9\%$ below ZDM — qualitatively wrong, cannot approach the ZDM limit because the rigid $\nu_{vac}$ skeleton fraction bounds $x_{sat}$ from below). At the near-extremal $a_* = 0.95$ (beyond the current catalog, whose maximum is $a_* \approx 0.74$) the two are already $+6.5\%$ (v1) vs $-20.1\%$ (v2). This is the **beyond-Kerr deviation organizer** of the BH soft-mode transition — the mode-ratio-locking + arrested-critical-slowing systematics carried at [`research/2026-07-20_ringdown-systematics_derivation.md`](../../../../../research/2026-07-20_ringdown-systematics_derivation.md) (ORG-1/ORG-2) — read here as v1's *rising* near-extremal limit rather than v2's *floored* one. Provenance + the frozen a\*=0.90/0.95 numbers: [`research/2026-07-20_v1-spin-mapping-adjudication_result.md`](../../../../../research/2026-07-20_v1-spin-mapping-adjudication_result.md) Leg 5 (#776).

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
