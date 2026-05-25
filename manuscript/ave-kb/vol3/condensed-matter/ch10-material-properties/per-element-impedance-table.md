[↑ Ch.10: Deriving Macroscopic Material Properties](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-nxfmh0]
-->

---

## Single-Element Impedance Under Stress

The derived properties table characterises each element at equilibrium. To predict how elements behave under external stress---compression, shear, thermal excitation---the second derivatives of the energy surface must be evaluated. The Hessian matrix $\mathbf{H}$ of the $K_{mutual}/d$ energy functional captures the full curvature of the energy landscape at the equilibrium nuclear geometry.

### The Hessian of the $1/d$ Energy Surface

For an $N$-nucleon system at equilibrium coordinates $\{\vec{r}_i\}$, the total energy is:

$$U = -\sum_{i<j}^{N} \frac{K_{mutual}}{d_{ij}} + E_{Coulomb}$$

The $3N \times 3N$ Hessian matrix is defined by:

$$H_{\alpha\beta} = \frac{\partial^2 U}{\partial x_\alpha \, \partial x_\beta}\bigg|_{\text{eq}}$$

where $\alpha, \beta$ index the $3N$ Cartesian degrees of freedom. At a true equilibrium (energy minimum), all eigenvalues of $\mathbf{H}$ are non-negative. Six eigenvalues are zero---three translations and three rotations---corresponding to Goldstone modes of the freely floating nucleus. The remaining $3N - 6$ eigenvalues represent the physical vibrational modes of the nuclear cluster.

### Normal Mode Classification

Eigendecomposition of $\mathbf{H}$ yields $3N-6$ mode frequencies $\omega_k = \sqrt{\lambda_k}$ and mode shapes $\vec{v}_k$. Each mode is classified by two observables:

- **Participation Ratio** ($p$): Quantifies how many nucleons contribute to the mode. Low $p$ ($<0.3$) indicates a localised *halo ejection* mode.
- **Radial Projection** ($\rho$): Correlation of the mode displacement with the radial unit vector $\hat{r}$. High $\rho$ ($>0.6$) indicates a *breathing* (bulk compression) mode; otherwise, a *rocking* (shear) mode.

These classifications map directly to macroscopic material properties:

- **Breathing modes** $\to$ **Bulk modulus** $K$: resistance to uniform compression.
- **Rocking modes** $\to$ **Shear modulus** $G$: resistance to angular deformation.
- **Ejection modes** $\to$ **Thermal rupture energy** $E_{rupt}$: energy to eject the outermost nucleon.

### Per-Element Impedance Table

Evaluating the Hessian numerically for each element Z=1 through Z=14 yields the complete single-element impedance characterisation:

| **Element** | **Z** | **A** | $Z_{atom}$ | $K_{bulk}$ | $G_{shear}$ | $E_{rupt}$ | $Q$ | **B/R/E** |
|---|---|---|---|---|---|---|---|---|
| Hydrogen-1 | 1 | 1 | --- | --- | --- | --- | --- | 0/0/0 |
| Helium-4 | 2 | 4 | 1.376 | 2.307 | 2.307 | 0.824 | 2.0 | 0/5/0 |
| Lithium-7 | 3 | 7 | 0.396 | 0.025 | 1.165 | 0.017 | 13.9 | 1/10/0 |
| Beryllium-9 | 4 | 9 | 0.457 | 0.186 | 0.252 | 0.048 | 3.1 | 2/14/0 |
| Boron-11 | 5 | 11 | 0.373 | 0.649 | 0.649 | 0.024 | 11.8 | 0/19/0 |
| Carbon-12 | 6 | 12 | 1.370 | 2.569 | 2.043 | 0.817 | 2.0 | 7/8/0 |
| Nitrogen-14 | 7 | 14 | 0.379 | 0.021 | 0.129 | 0.006 | 15.5 | 2/14/8 |
| Oxygen-16 | 8 | 16 | 1.370 | 3.267 | 2.114 | 0.817 | 2.0 | 3/17/0 |
| Fluorine-19 | 9 | 19 | 1.473 | 3.276 | 2.120 | 0.819 | 2.8 | 2/17/4 |
| Neon-20 | 10 | 20 | 1.369 | 2.566 | 2.653 | 0.816 | 2.0 | 7/8/10 |
| Sodium-23 | 11 | 23 | 1.454 | 2.648 | 3.274 | 0.818 | 2.8 | 0/4/24 |
| Magnesium-24 | 12 | 24 | 1.369 | 2.040 | 2.448 | 0.816 | 2.0 | 12/18/0 |
| Aluminum-27 | 13 | 27 | 1.440 | 2.156 | 2.045 | 0.817 | 2.8 | 11/2/20 |
| Silicon-28 | 14 | 28 | 1.369 | 1.946 | 2.215 | 0.816 | 2.0 | 13/14/8 |

$Z_{atom}$: geometric mean mode frequency (atomic impedance). $K_{bulk}$: mean breathing-mode eigenvalue (bulk modulus proxy). $G_{shear}$: mean rocking-mode eigenvalue (shear modulus proxy). $E_{rupt}$: softest physical eigenvalue (thermal rupture proxy). $Q$: ratio of highest to lowest mode frequency. B/R/E: count of breathing, rocking, and ejection modes.

### The Two Impedance Families

The impedance table reveals a striking binary partition. The elements divide cleanly into two distinct families based on their atomic impedance $Z_{atom}$:

**Closed-Shell Alpha Cores ($Z_{atom} \approx 1.37$, $Q = 2.0$, $E_{rupt} \approx 0.82$).** Helium-4, Carbon-12, Oxygen-16, Neon-20, Magnesium-24, and Silicon-28 all share nearly identical impedance signatures. These elements are constructed entirely from tetrahedral alpha clusters (4-node closed tetrahedra). Their quality factor is exactly $Q = 2.0$---a direct signature of the tetrahedral symmetry, which admits only two distinct eigenfrequencies. Their thermal rupture energy is uniformly $\sim 0.82$ MeV, indicating that the alpha-tetrahedron itself is the fundamental "hard" building block of all nuclear matter.

**Open-Shell Halo Elements ($Z_{atom} \sim 0.37$--$0.46$, $Q = 3$--$16$, $E_{rupt} \ll 0.82$).** Lithium-7, Beryllium-9, Boron-11, and Nitrogen-14 possess halo nucleons loosely coupled to their alpha cores. Their impedances are $\sim 3\times$ lower, their quality factors are much higher (broad frequency spectrum), and their thermal rupture energies are $10$--$100\times$ softer. These elements are structurally "leaky"---a loosely coupled halo nucleon dominates the softest vibrational mode and is readily ejected by thermal perturbation.

**Composite Elements (Fluorine, Sodium, Aluminum).** Elements with an alpha-cluster core plus a halo sub-structure (e.g., Fluorine-19 = Oxygen-16 + Tritium) exhibit intermediate impedances ($Z_{atom} \approx 1.44$--$1.47$). Their $Q > 2$ reflects the additional mode complexity introduced by the halo, while their bulk and shear moduli remain dominated by the underlying alpha-core scaffold.

### Implications for Multi-Element Assembly

Elements within the same impedance family ($|\Gamma_{ij}| \to 0$) bond efficiently because their vibrational modes couple resonantly. Elements across families ($|\Gamma_{ij}| \sim 0.5$) experience strong reflection at the interface---the signature of a reactive, ionic bond.

---
