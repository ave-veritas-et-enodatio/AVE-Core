[↑ Ch.5 Universal Spatial Tension](index.md)
<!-- leaf: verbatim -->

## Section 5.2: Scale Invariance across the Framework

To prove that AVE does not rely on disconnected, ad-hoc parameter tuning, it must be demonstrated that the identical $1/r$ tensor calculates the mass of an elementary particle and the mass of a complex atomic nucleus.

### The Lepton Tension Limit

The stable Ground State Electron is a $0_1$ Unknot topology---a single closed flux tube loop at minimum ropelength $= 2\pi$, spanning a normalised radius $R_e$. It generates an inductive resistance of $0.511 \text{ MeV}$.

The Muon and Tau are not new "flavors" of particles requiring new quantum numbers; they are excitations of this same unknot geometry into higher Cosserat coupling sectors (derived in full in Volume II, Chapter 5):

- **Muon:** one quantum of torsional coupling $\alpha\sqrt{3/7}$ yields $m_\mu = m_e/(\alpha\sqrt{3/7}) \approx 107.0 \text{ MeV}$ ($+1.24\%$).
- **Tau:** full bending stiffness $p_c/\alpha^2 = 8\pi/\alpha$ yields $m_\tau = 8\pi m_e / \alpha \approx 1760 \text{ MeV}$ ($-0.95\%$).

Three Cosserat sectors---translation, rotation, curvature-twist---yield exactly three generations.

### The Nuclear Tension Limit

When constructing atomic nuclei, the same law applies symmetrically. Neon-20 ($Z=10, A=20$) is defined as a 5-node Alpha particle lattice ($5\alpha$). When evaluating the most stable geometric arrangement (a Triangular Bipyramid), the $M \propto 1/d_{ij}$ mutual inductance solver computes the total binding energy as the sum over all $\binom{5}{2} = 10$ pairwise interactions:

> **[Resultbox]** *Bipyramid Pairwise Binding Energy*
>
> $$
> E_{bind} = \sum_{i<j} \frac{K_{mutual}}{d_{ij}} \qquad \text{where} \quad K_{mutual} = T_{nuc} \cdot \ell_{node} = m_p c^2
> $$

The integrator determines that the optimisation limit occurs when the polar Alphas are suspended at $R_{bipyramid} = 72.081d$. When evaluated at this Cartesian offset, the macroscopic LC integration calculates a topological mass of $18617.730$ MeV, mapping the empirical CODATA target ($18617.729$ MeV) with $<0.001\%$ error.

> **[Examplebox]** *Calculating the Baseline Nuclear Interaction*
>
> **Problem:** Using the Universal Spatial Tension metric ($M \propto 1/r$), calculate the absolute mass equivalent of a single unperturbed topological bond ($K_{mutual}$) between two nuclear nodes.
>
> **Solution:** As derived above, the baseline compliance scalar of the vacuum is $K \equiv \hbar/c$.
> However, for strong-force nuclear aggregates, the coupling transitions into the $T_{nuc}$ tension regime, establishing the fundamental strong bond distance ($1d \approx 2.4 \text{ fm}$).
> The absolute topological bonding impedance $K_{mutual}$ is evaluated physically as the rest mass of the proton:
>
> $$
> K_{mutual} = T_{nuc} \cdot \ell_{node} = m_p c^2 \approx 938.272\,\text{MeV}
> $$
>
> This means a single ideal $1/d_{ij}$ link at a nominal dimensionless distance of $1.0$ contributes exactly $938.272\,\text{MeV}$ of binding impedance to the atomic lattice. The Neon-20 computer solver simply sums 10 overlapping $1/d_{ij}$ links at their optimally packed Cartesian coordinates to trace the exact geometric condensation of the nucleus.

<!-- Figure: fig:neon20_geometry — Neon-20 Triangular Bipyramid Geometry. The precise mass of the Ne-20 nucleus is computed by summing the 1/d_ij topological inductance over all 10 pairwise alpha-particle interactions within this geometrically optimized stable lattice. -->

---
