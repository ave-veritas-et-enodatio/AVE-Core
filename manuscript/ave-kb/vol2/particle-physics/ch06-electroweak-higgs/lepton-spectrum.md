[↑ Ch.6 — Electroweak and Higgs](index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: q8un7j, rji99i -->
<!-- NOTE: eq:muon_twist_angle is in this section (§6.5), not §6.2 -->

## The Three-Generation Lepton Spectrum
<!-- claim-quality: rji99i (Cosserat lepton sector framework also produces neutrino mass spectrum via crossing-number splitting) -->

Each charged lepton maps to one sector of the Cosserat micropolar Lagrangian applied to the unknot ground state.

> **[Resultbox]** *Physical Interpretation*
>
> In all three lepton generations, the geometric deformation (twist, curvature) describes a pattern of **dielectric saturation density**---the varying impedance of each lattice node along the flux tube. The nodes themselves remain fixed at $l_{node}$ spacing (Axiom 1). The muon's "twist" is a helical modulation of impedance density wound around the unknot loop, and the tau's "curvature" is a radial undulation of the saturation envelope. Neither involves physical displacement of lattice nodes.

### Generation 1: Translation (Shear Modulus $\mu$)

The electron is the $0_1$ unknot ground state. No torsional excitation is present:

$$
m_e = \frac{T_{EM} \cdot l_{node}}{c^2} = \frac{\hbar}{l_{node} \cdot c} = 0.511 \text{ MeV}
$$

### Generation 2: Rotation (Cosserat Coupling $\kappa$)

> **[Examplebox]** *Deriving the Muon Mass via Cosserat Torsional Excitation*
>
> **Problem:** The muon is the $0_1$ unknot absorbing exactly one quantum of chiral torsional coupling. Derive its deterministic mass eigenvalue.
>
> **Solution:** The torsional coupling constant is $\alpha\sqrt{3/7}$, where $\alpha$ is the dielectric compliance (one chirality interaction) and $\sqrt{3/7}$ is the PAT torsion-shear projection.
> Because the muon is a stable static defect, only *one* factor of $\alpha$ appears (a single-vertex process, unlike the transient W boson which requires $\alpha^2$).
>
> $$
> m_\mu = \frac{m_e}{\alpha \sqrt{3/7}}
> $$
>
> Evaluating this structurally against $m_e \approx 0.511 \text{ MeV}$ gives:
>
> $$
> m_\mu = \frac{0.511 \text{ MeV}}{\alpha \sqrt{3/7}} \approx 107.0 \text{ MeV} \quad (\text{Exp: } 105.66 \text{ MeV, } +1.24\%)
> $$

The coupling $\alpha\sqrt{3/7}$ carries a direct geometric consequence for the unknot's flux tube. The factor $\sqrt{3/7}$ is the PAT torsion-shear projection: the fraction of the translational (shear) impedance density that maps onto the torsional (rotational) degree of freedom when $\nu_{vac} = 2/7$. As the unknot is traversed, the cross-sectional impedance pattern rotates by exactly $\sqrt{3/7}$ turns ($\approx 236°$):

$$
\Phi_{\text{twist}} = 2\pi\sqrt{\frac{3}{7}} \approx 4.11 \text{ rad} \approx 236°
$$

This helical impedance spiral is visible in the 3D-printable STL model (`assets/3d_models/muon_twisted_unknot.stl`).

### Generation 3: Curvature-Twist (Bending Stiffness $\gamma_C$)

The tau is the unknot promoted to the full bending energy scale:

$$
m_\tau = m_e \cdot \frac{p_c}{\alpha^2} = \frac{8\pi m_e}{\alpha} \approx 1{,}760 \text{ MeV} \quad (\text{Exp: } 1{,}776.9 \text{ MeV, } -0.95\%)
$$

Geometrically, the curvature-twist excitation manifests as $7$ radial undulation lobes around the unknot circumference (from $\nu_{vac} = 2/7$, giving $7$ compliance modes in the torsional sector). The amplitude of the tube-radius modulation is bounded by the packing fraction $p_c = 8\pi\alpha \approx 0.183$---the maximum bending deformation before Axiom 4 saturation clamps the lattice.

This is the maximum excitation before packing saturates. The hierarchy of Cosserat sectors yields exactly three generations:

$$
m_e \xrightarrow{\alpha\sqrt{3/7}} m_\mu \xrightarrow{\alpha \cdot p_c} m_\tau \xrightarrow{\alpha \cdot p_c} M_W
$$

| Particle | AVE Formula | Predicted | Experiment | Deviation |
|---|---|---|---|---|
| $e$ | $m_e$ | 0.511 MeV | 0.511 MeV | Input |
| $\mu$ | $m_e/(\alpha\sqrt{3/7})$ | 107.0 MeV | 105.66 MeV | $+1.24\%$ |
| $\tau$ | $m_e \cdot p_c/\alpha^2$ | 1,760 MeV | 1,776.9 MeV | $-0.95\%$ |
| $W$ | $m_e/(\alpha^2 p_c \sqrt{3/7})$ | 79,923 MeV | 80,379 MeV | $-0.57\%$ | <!-- claim-quality: q8un7j -->
| $Z$ | $M_W \cdot 3/\sqrt{7}$ | 90,624 MeV | 91,188 MeV | $-0.62\%$ | <!-- claim-quality: q8un7j -->

---
