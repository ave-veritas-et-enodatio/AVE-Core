[↑ Ch.6 — Electroweak and Higgs](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-q8un7j, clm-rji99i]
-->

<!-- NOTE: eq:muon_twist_angle is in this section (§6.5), not §6.2 -->

## The Three-Generation Lepton Spectrum
<!-- claim-quality: clm-rji99i (Cosserat lepton sector framework also produces neutrino mass spectrum via crossing-number splitting) -->

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

> **🔴 OPEN FLAG (Rule 12 — `√(3/7)` "PAT torsion-shear" label; Grant's physics adjudication pending. Body preserved unchanged below; label NOT swapped per substitution-not-retraction.):** $\sqrt{3/7} = \sqrt{1 - 2\nu_{vac}}$ at $\nu_{vac} = 2/7$ is EXACTLY the dilatational/compressional (bulk) elastic signature: $(1-2\nu)$ = bulk/volumetric, $(1+\nu)$ = shear/deviatoric (the corpus uses $(1+\nu) = 9/7$ as the Z-factor $3/\sqrt{7} = \sqrt{9/7}$, cf. the $M_Z = M_W \cdot 3/\sqrt{7}$ row below). The genuinely-shear combination $(1+\nu)$ is therefore used elsewhere while the bulk combination $(1-2\nu)$ here carries the "torsion-shear / PAT" label — an elastic-type contradiction. **OPEN — Grant's physics adjudication:** does an independent torsion route reach $\sqrt{3/7}$, or is this the dilatational (bulk) projection and the "torsion-shear" label wrong? The engine constant `_SIN_THETA_W_PAT` (`src/ave/topological/cosserat.py:65`) is NOT renamed — deferred to Grant.

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

The coupling $\alpha\sqrt{3/7}$ carries a direct geometric consequence for the unknot's flux tube. The factor $\sqrt{3/7}$ is the PAT torsion-shear projection: the fraction of the translational (shear) impedance density that maps onto the torsional (rotational) degree of freedom when $\nu_{vac} = 2/7$. <!-- 🔴 OPEN FLAG (Rule 12): "PAT torsion-shear" label on √(3/7) is contested — see the 🔴 flag under "Generation 2" above; $\sqrt{3/7} = \sqrt{1-2\nu_{vac}}$ is the bulk/dilatational signature, not deviatoric/shear. Grant's adjudication pending; label preserved unchanged. --> As the unknot is traversed, the cross-sectional impedance pattern rotates by exactly $\sqrt{3/7}$ turns ($\approx 236°$):

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

> **Net-$\alpha$-power reduction note (algebraic identity; retires the "$\alpha^1$ muon / $\alpha^2$ tau exponent" framing).** Because $p_c = 8\pi\alpha$, the tau's $p_c/\alpha^2 = 8\pi\alpha/\alpha^2 = 8\pi/\alpha$. The **net $\alpha$-power is $\alpha^{-1}$ for BOTH charged leptons**:
> $$ m_\mu = \frac{m_e}{\alpha\sqrt{3/7}} = \sqrt{\tfrac{7}{3}}\,\frac{m_e}{\alpha}, \qquad m_\tau = m_e\,\frac{p_c}{\alpha^2} = \frac{8\pi\,m_e}{\alpha}. $$
> The $\mu$-vs-$\tau$ differentiation is therefore carried by the **prefactor** ($\sqrt{7/3} \approx 1.528$ muon vs $8\pi \approx 25.13$ tau), **NOT an exponent** — the tau's apparent $\alpha^2$ in $p_c/\alpha^2$ reduces to $\alpha^{-1}$ once $p_c = 8\pi\alpha$ is substituted. The genuine $\alpha^1/\alpha^2$ split is **sector-level**: charged leptons (single-vertex static defect, net $\alpha^{-1}$) vs **W/Z (transient two-vertex self-energy, $\alpha^2$)** — the real $\alpha^2$ locus is the W/Z self-energy, canonical at [`weak-coupling.md`](../ch05-electroweak-mechanics/weak-coupling.md) (two-vertex second-order $\propto \alpha \times \alpha = \alpha^2$) and [`spontaneous-symmetry-breaking.md`](spontaneous-symmetry-breaking.md) ($\varepsilon_T/\mu = \pi\,\alpha^2\,p_c\,\sqrt{3/7}$, "$\alpha^2$ --- two-vertex coupling").

This is the maximum excitation before packing saturates. The hierarchy of Cosserat sectors yields exactly three generations (the arrow labels denote the **sector-coupling ingredient introduced** at each step — the geometric factor entering that generation's closed form — **NOT a literal adjacent-mass multiplier**; the true adjacent ratios are $m_\mu/m_e = 1/(\alpha\sqrt{3/7}) \approx 209.3$, $m_\tau/m_\mu = 8\pi\sqrt{3/7} \approx 16.45$, $M_W/m_\tau = 1/(p_c^2\sqrt{3/7}) \approx 45.4$):

$$
m_e \xrightarrow{\text{torsion: }\alpha\sqrt{3/7}} m_\mu \xrightarrow{\text{bending: }p_c/\alpha^2} m_\tau \xrightarrow{\text{+2nd vertex: }\alpha} M_W
$$

| Particle | AVE Formula | Predicted | Experiment | Deviation |
|---|---|---|---|---|
| $e$ | $m_e$ | 0.511 MeV | 0.511 MeV | Input |
| $\mu$ | $m_e/(\alpha\sqrt{3/7})$ | 107.0 MeV | 105.66 MeV | $+1.24\%$ |
| $\tau$ | $m_e \cdot p_c/\alpha^2$ | 1,760 MeV | 1,776.9 MeV | $-0.95\%$ |
| $W$ | $m_e/(\alpha^2 p_c \sqrt{3/7})$ | 79,923 MeV | 80,379 MeV | $-0.57\%$ | <!-- claim-quality: clm-q8un7j -->
| $Z$ | $M_W \cdot 3/\sqrt{7}$ | 90,624 MeV | 91,188 MeV | $-0.62\%$ | <!-- claim-quality: clm-q8un7j -->

> **Tier (consistency-vs-emergence): matched closed-form CONSISTENCY — NO solver.** Each lepton row above is a **matched closed-form algebraic expression** evaluated from the CODATA-input $\alpha$ and $p_c$ with $m_e$ as the input scale — **not** "derived" or "emergent", and **not** solver-backed. This is a distinct (lower) tier than the proton $m_p/m_e$ **Faddeev--Skyrme eigenvalue** (which IS a numerical-solver result; see [`full-derivation-chain.md`](../../../common/full-derivation-chain.md) Layer 6 / Baryon Sector). The corpus self-flags this honestly: the muon factor "is asserted" and the tau factor is "identified rather than derived" (Backmatter Ch. 2 full-derivation chain). Read the matrix $\checkmark$ for these rows as **closed-form match**, not first-principles Cosserat-eigenmode emergence.

---
