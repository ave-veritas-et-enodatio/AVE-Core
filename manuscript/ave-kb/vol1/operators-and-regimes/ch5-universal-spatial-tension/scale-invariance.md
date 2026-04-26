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

When constructing atomic nuclei, the same $1/r$ tension law applies symmetrically. Neon-20 ($Z=10, A=20$) is modelled as a 5-node Alpha particle lattice ($5\alpha$) in a Triangular Bipyramid arrangement, with the $M \propto 1/d_{ij}$ mutual inductance summed over all $\binom{5}{2} = 10$ pairwise interactions:

> **[Resultbox]** *Bipyramid Pairwise Binding Energy*
>
> $$
> E_{bind} = \sum_{i<j} \frac{K_{mutual}}{d_{ij}} \qquad \text{where} \quad K_{mutual} = T_{nuc} \cdot \ell_{node} = m_p c^2
> $$

**Methodology disclosure (per Vol 6 introduction).** Within the $(Z,A)$-forced bipyramid topology, the inter-alpha distance $R_{bipyramid}$ is the single fitted scalar adjusted per nucleus so the pairwise summation reproduces the CODATA mass.
- *Predicted (axiom-derived):* the cluster topology as a function of $(Z,A)$ via minimum-impedance packing, the coupling $K_{mutual} = m_p c^2$, and the parameter count (one scalar per nucleus).
- *Fitted per nucleus:* the numerical value of $R_{bipyramid}$.

The Vol 6 introduction is the canonical statement of this fit/predict split; the Neon-20 result here is one application of that methodology, not a zero-parameter ab-initio prediction. The $5\alpha$ Triangular Bipyramid topology is itself the falsifiable axiomatic content; reproducing every measured nuclear mass under *one* fitted scalar per nucleus (rather than the $\sim 5$ parameters per nucleus required by liquid-drop or shell-model fits) is the structural claim that Vol 6 tests.

The optimizer (`src/scripts/vol_6_periodic_table/simulations/solve_neon.py`, Nelder–Mead with `tol=1e-8`) converges at $R_{bipyramid} \approx 81.158\,d$, at which the topological mass evaluates to $18617.730$ MeV against the CODATA target ($18617.729$ MeV). The reported $<0.001\%$ residual is the optimizer's convergence tolerance on $R$, not an independent prediction error on the mass. (Earlier editions of this chapter cited $R = 72.081\,d$ from a prior solver run with different unit conventions; the current canonical value is $81.158\,d$, matching Vol 6 Period 2.)

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
