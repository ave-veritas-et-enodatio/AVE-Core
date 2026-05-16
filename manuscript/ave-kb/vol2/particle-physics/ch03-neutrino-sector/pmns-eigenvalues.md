[↑ Ch.3 — Neutrino Sector](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-7o8clt, clm-rji99i]
path-stable: "referenced from vol2 as sec:pmns_eigenvalues, eq:theta12_leading, eq:theta23_leading, eq:theta13"
-->

## Step 2: Regime Boundary Eigenvalues in Mode Space
<!-- claim-quality: clm-7o8clt -->

The regime-boundary eigenvalue method computes eigenfrequencies as $\omega = \ell \cdot c / r_{\text{eff}}$. Applied to crossing-number space:

- The "radius" is the crossing number $c$
- The "angular mode number" is the mode spacing $\Delta c$
- The eigenvalue ratio gives $\sin^2\theta$

Three distinct boundary conditions arise for the three mode pairs:

### (a) Compliance Regime ($\nu_1 \leftrightarrow \nu_2$, $\Delta c = 2 \le 3$):

Below the chiral screening threshold, the compliance channel is open. The regime-boundary eigenvalue gives:

$$
\sin^2\theta_{12}^{(0)} = \frac{\Delta c}{c_2} = \frac{2}{7} = \nu_{vac}
$$

The spacing-to-mode ratio IS the Poisson ratio. This is not coincidence: the torus knot crossing numbers $5, 7, 9$ are separated by $\Delta c = 2$ precisely because the lattice compliance manifold allocates 2 compressive and 5 transverse modes out of 7 total ($\nu_{vac} = 2/7$).

### (b) Impedance-Matched Regime ($\nu_2 \leftrightarrow \nu_3$, $c_2 = $ midpoint):

The middle crossing number $c_2 = 7$ is the arithmetic mean of the boundary values: $c_2 = (c_1 + c_3)/2 = (5 + 9)/2 = 7$. At the midpoint of a 3-port mode system, the impedances to the left and right are **matched**: $Z_{\text{left}} = Z_{\text{right}}$. The reflection coefficient vanishes ($\Gamma = 0$), and energy splits equally:

$$
\sin^2\theta_{23}^{(0)} = \frac{1}{2} \qquad \text{(impedance-matched midpoint boundary)}
$$

This is the origin of "maximal atmospheric mixing": a structural consequence of the middle torus knot sitting at the impedance-matched regime boundary.

### (c) Screened Regime ($\nu_1 \leftrightarrow \nu_3$, $\Delta c = 4 > 3$):
<!-- claim-quality: clm-rji99i (the $c_1, c_3$ crossing numbers used here also encode the neutrino mass hierarchy $m_i \propto 1/c_i^2$) -->

The compliance channel is chirally screened ($\Delta c = 4 > \Delta c_{\text{crit}} = 3$). Only perturbative **junction coupling** survives:

$$
\sin^2\theta_{13} = \frac{1}{c_1 \cdot c_3} = \frac{1}{5 \times 9} = \frac{1}{45}
$$

Physical mechanism: signal must leave at one of $c_1$'s crossings AND enter at one of $c_3$'s crossings. The coupling probability is normalised by the total number of junction pairs: $c_1 \times c_3 = 45$. This is a two-vertex process --- the same $\propto \alpha^2$ structure as the W boson self-energy.

---
