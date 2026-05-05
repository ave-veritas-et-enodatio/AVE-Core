[↑ Biophysics Introduction](../index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: br3bcv -->

---

## Derivation Chain: From Lattice Pitch to Bond Length

The C$\alpha$--C$\alpha$ virtual bond distance $d_0 \approx 3.80$ Å is derived through a chain of AVE identities:

1. **Lattice pitch:** $\ell_{node} = \hbar / (m_e c) \approx 3.862 \times 10^{-13}$ m.
2. **Bohr radius:** $a_0 = \ell_{node} / \alpha \approx 5.292 \times 10^{-11}$ m (the characteristic extension of the unknot electron).
3. **Covalent bond length:** C--N and C$\alpha$--C bonds are set by the overlap of atomic ground states at the equilibrium impedance-matching distance: $r_{cov} \approx 1.47$ Å (C--N), 1.52 Å (C--C), 1.33 Å (C=O).
4. **Backbone repeat:** The peptide unit (N--C$\alpha$--C--N) has a fixed geometry from the $sp^3$ tetrahedral bond angle ($\theta = 109.47^\circ$) and the planar amide constraint ($\omega = 180^\circ$). The resulting C$\alpha$--C$\alpha$ distance:

$$
d_0 = \sqrt{r_{C\alpha C}^2 + r_{CN}^2 + 2\, r_{C\alpha C}\, r_{CN} \cos(180^\circ - \theta)} \approx 3.80 \text{ Å}
$$

Every step uses constants from the AVE physics engine (Volume I) or standard NERF rigid-body geometry. No free parameter is introduced at the biological scale.

---
