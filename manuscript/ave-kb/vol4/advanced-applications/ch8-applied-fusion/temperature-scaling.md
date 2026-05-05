[↑ Ch.8 Applied Fusion](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [qagkgy]
-->

## WKB Derivation of Temperature Scaling

The fusion cross-section is governed by the Gamow tunnelling probability through the Coulomb barrier. The WKB tunnelling exponent is:

$$
\eta = \frac{1}{\hbar}\int_{r_{nuc}}^{r_{turn}}\! \sqrt{2\mu\bigl(V(r) - E\bigr)}\;\mathrm{d}r
$$

In a metrically compressed space ($n_{scalar} > 1$), two transformations act simultaneously:

- **Potential invariance:** $V(r_{lab}) = \alpha\hbar c_{local}/r_{lab} = \alpha\hbar(c_0/n)/(r_0/n) = \alpha\hbar c_0/r_0 = V_{vac}(r_0)$. The Coulomb barrier height is unchanged.
- **Coordinate compression:** The spatial measure contracts: $\mathrm{d}r_{lab} = \mathrm{d}r_{vac}/n$. The WKB integral picks up a factor of $1/n$.

The Gamow energy, which sets the peak of the Maxwell-Boltzmann$\times$tunnelling integrand, is $E_G = (\pi \alpha Z_1 Z_2)^2 \times 2\mu c^2$. Since $\eta \propto \sqrt{E_G/E}$ and $\eta(n) = \eta_0/n$, the compressed Gamow energy is:

$$
E_G(n) = \frac{E_{G,0}}{n^2}
$$

The Lawson ignition criterion---where the volumetric reaction rate first exceeds radiative losses---depends on $E_G$. Therefore the ignition temperature scales as $T_{ign}(n) = T_0/n_{scalar}^2$.

---
