[↑ Ch.2 — Baryon Sector](index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: mnb3lt -->
<!-- NOTE: source has duplicate subsection titles "The Self-Consistent Mass Oscillator (The Structural Eigenvalue)" at approximately lines 114 and 166. This leaf covers both occurrences. -->

## The Self-Consistent Mass Oscillator (The Structural Eigenvalue)

### The Cinquefoil Confinement Bound

The 1D Faddeev-Skyrme energy functional for a localized topological defect is *scale-free*: it possesses no natural energy minimum at finite radius. Without confinement, the soliton spreads indefinitely ($r_{opt} \to \infty$, $\mathcal{I}_{scalar} \to 580$). The physical confinement is set by the topology of the phase winding itself.

The electron's phase profile follows the $(2,3)$ pattern with $c_3 = 3$ phase crossings, even though its ground-state topology is the unknot ($0_1$). In the torus knot classification, these are the $(2,q)$ torus knots with strictly **odd** $q$: the $(2,3)$ trefoil, the $(2,5)$ cinquefoil, the $(2,7)$ knot, and so on. There is no stable $(2,4)$ torus knot---the figure-eight knot ($4_1$) is not a torus knot and cannot be embedded on the chiral lattice.

The proton's phase winding passes through the **$(2,5)$ cinquefoil torus knot**---the next stable entry in the torus knot ladder after the electron's $c=3$ winding. Its $c_5 = 5$ crossings each constrain the soliton's radial phase gradient by absorbing a fraction of the total Faddeev-Skyrme coupling $\kappa_{FS}$. The confinement radius is therefore:

> **[Resultbox]** *Cinquefoil Confinement Bound*
>
> $$
> r_{opt} = \frac{\kappa_{FS}}{c_5} = \frac{\kappa_{FS}}{5} \approx 4.97 \; \ell_{node}
> $$

This topological confinement means the proton extends over approximately five lattice spacings---a genuinely extended object in the $\mathcal{M}_A$ condensate.

### The Structural Eigenvalue

To mathematically convert this pure topological volume into physical mass, it must be scaled by the discrete hardware limits of the $\mathcal{M}_A$ condensate: the topological packing limit ($p_c \approx 0.1834$) derived in Chapter 2, and the inductive mass-stiffening ratio ($x_{core} = m_{core}/m_e$).

Because the structural tension generating the tensor mass is strictly driven by the total inductive mass of the knot, the mass generation forms a dynamic, self-consistent structural feedback loop. This is formulated as an exact linear eigenvalue equation:

> **[Resultbox]** *Self-Consistent Mass Eigenvalue Equation*
>
> $$
> x_{core} = \mathcal{I}_{scalar} + \left[ (\mathcal{V}_{total} \cdot p_c) \cdot x_{core} \right]
> $$

The 1D Faddeev-Skyrme solver, confined by the cinquefoil crossing number ($r_{opt} = \kappa_{FS}/5$), with Axiom 4 gradient saturation inside the integrand and thermally softened by $\delta_{th} = 1/(14\pi^2)$, yields $\mathcal{I}_{scalar} \approx 1162$. Substituting:

> **[Resultbox]** *Eigenvalue Substitution*
>
> $$
> x_{core} = 1162 + (2.0 \cdot p_c) \cdot x_{core} \implies x_{core} = 1162 + (2.0 \cdot 0.1834) x_{core}
> $$

> **[Resultbox]** *Neutral Core Mass Solution*
>
> $$
> x_{core}(1 - 0.3668) = 1162 \implies x_{core} = \frac{1162}{0.6332} \approx \mathbf{1835.12}
> $$

However, $1835\ m_e$ only models the uncharged, neutralized geometric core. To satisfy the global invariant charge constraint of the unbroken lattice, the Borromean cage must irrevocably trap exactly $+1$ integer topological phase twist at its center (the positron equivalent). A fundamental integer topological twist possesses exactly $1.0\ m_e$ of inductive mass.

Adding the structurally mandated integer twist to the derived core yields the true Baryon rest mass:

> **[Resultbox]** *The Baryon Mass Eigenvalue*
>
> $$
> x = 1835.12 + 1.0 = \mathbf{1836.12}
> $$

By resolving the exact saturated topological geometry of the Toroidal Halo at $\mathcal{V}_{total}=2.0$, confining the soliton by the cinquefoil crossing number with Axiom 4 gradient saturation inside the energy functional, and adding the $+1$ integer twist required for global charge, the theoretical prediction converges to within $\mathbf{0.002\%}$ of the empirical CODATA proton mass ($1836.153\,m_e$) using zero Standard Model parameters.

---
