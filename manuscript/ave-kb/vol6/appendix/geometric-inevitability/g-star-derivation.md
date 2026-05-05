[↑ Geometric Inevitability](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [ome498]
-->

<!-- PATH-STABLE: sec:g_star_derivation -->

## $g_* = 7^3/4 = 85.75$: Lattice Mode Count

The effective number of relativistic degrees of freedom $g_*$ appears in the baryon asymmetry formula. The Standard Model counts $g_{*,SM} = 106.75$ by enumerating all known particles. AVE derives this constant from lattice geometry.

### Derivation

The Poisson ratio $\nu_{vac} = 2/7$ (derived in Book 1) reveals that each lattice node has **7 independent compliance modes**: the denominator of $\nu$. Physically, these are the 7 independent small-deformation degrees of freedom of the LC network at each node: 3 translational, 3 rotational, and 1 volumetric.

In three dimensions, the total mode count is $7^3 = 343$ (7 per spatial direction, cubed for the full 3D Brillouin zone). The K4 unit cell contains 4 nodes, so the effective DOF per cell is:

$$
\boxed{g_* = \frac{7^3}{4} = \frac{343}{4} = 85.75}
$$

### Verification

Substituting into the baryon asymmetry formula with all other factors derived from AVE constants:

$$
\eta = \frac{(\pi/\kappa_{FS}) \cdot \alpha_W^4 \cdot (28/79)}{7^3/4} = 6.08 \times 10^{-10}
$$

Observed: $\eta_{obs} = 6.1 \times 10^{-10}$. **Error: 0.38%.** Using the SM value $g_* = 106.75$ gives 20% error.

---
