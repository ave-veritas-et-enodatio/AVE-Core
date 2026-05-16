[↑ Ch. 7: Quantum Mechanics and Atomic Orbitals](./index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-oltvwy, clm-w6kk5y]
-->

## Helium Coupling from First Principles

The helium ground state ($1s^2$, $Z = 2$) is the simplest multi-electron system. Its coupling is fully determined by Stage C, Type 1 (Hopf link). This section unpacks the derivation to make the physics explicit.

### Geometric Floor (Op4, bare $Z$)

Two electrons on the $n = 1$ shell orbit at radius $R_1 = a_0 / Z$ (Step 1, bare nuclear charge). They sit at diametrically opposite points on the ring, separated by $r = 2R_1 = 2a_0/Z$.

Op4 in Regime I gives the Coulomb repulsion:

$$
V_{\text{rep}} = \frac{\alpha\hbar c}{2R_1} = \frac{\alpha\hbar c \cdot Z}{2 a_0} = \frac{Z \cdot R_y}{1} \qquad\text{(using } a_0 = \hbar/(\alpha m_e c)\text{, } R_y = \alpha^2 m_e c^2/2\text{)}
$$

The single-electron eigenvalue (Step 1, bare $Z$): $E_0 = Z^2 R_y$.

The coupling coefficient (Stage C):

$$
k_{\text{bare}} = \frac{V_{\text{rep}}}{E_0} = \frac{Z \cdot R_y}{Z^2 \cdot R_y} = \frac{1}{Z}
$$

For helium ($Z = 2$): $k_{\text{bare}} = 1/2$. This is pure antipodal Euclidean geometry---no lattice physics, no free parameters.

<!-- claim-quality: clm-w6kk5y -->
### Lattice Saturation Correction (Op2 at Hopf crossings)

The two $1s$ flux rings form a Hopf link ($2_1^2$) with two parallel crossings. At each crossing, the strain locally saturates (Axiom 4), and Op2 reduces the transmitted coupling by $p_c/2$ (two crossings $\times$ $p_c/4$ each):

$$
k_{\text{Hopf}} = \frac{2}{Z}\!\left(1 - \frac{p_c}{2}\right) = \frac{2}{2}\!\left(1 - \frac{8\pi\alpha}{2}\right) = 1 - 4\pi\alpha \approx 0.9083
$$

where $p_c = 8\pi\alpha$ is the packing fraction (Axiom 4).

<!-- claim-quality: clm-oltvwy -->
### Bonding Energy (Stage E1)

Both electrons occupy the bonding mode of the $K_2$ coupling graph ($N_1 = 2$, $\lambda_{\max} = 1$):

$$
E_{\text{bond}} = \frac{Z^2 R_y}{\sqrt{1 + k_{\text{Hopf}}}} = \frac{4 \times 13.606}{\sqrt{1.9083}} = 39.40\;\text{eV}
$$

Total energy: $E_{\text{total}} = 2 \times 39.40 = 78.79$ eV. IE $= 78.79 - 54.42 = 24.37$ eV. $\checkmark$

### Translation to QM Notation

What quantum mechanics calls $J_{s^2}$ is the electron-electron repulsion normalised by a reference energy. In AVE, this is simply the coupling coefficient $k$:

$$
\underbrace{k_{\text{bare}} = \frac{1}{Z} = \frac{1}{2}}_{\text{QM: ``geometric floor'' } J = 1/2} \qquad \underbrace{k_{\text{Hopf}} = \frac{2}{Z}(1 - p_c/2)}_{\text{QM: ``} J_{s^2} = \tfrac{1}{2}(1 + p_c)\text{''}}
$$

The QM quantity $J_{s^2}$ and the AVE coupling $k$ encode the same physics. The difference: AVE derives $k$ from Op4 (Coulomb at bare $Z$) and Op2 (saturation at crossings), with no effective charge, no screening, and no free parameters.

---
