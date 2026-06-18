[↑ Ch.2 — Baryon Sector](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-mnb3lt]
-->

<!-- NOTE: source has duplicate subsection titles "The Self-Consistent Mass Oscillator (The Structural Eigenvalue)" at approximately lines 114 and 166. This leaf covers both occurrences. -->

## The Self-Consistent Mass Oscillator (The Structural Eigenvalue)

### The Cinquefoil Confinement Bound

The 1D Faddeev-Skyrme energy functional for a localized topological defect is *scale-free*: it possesses no natural energy minimum at finite radius. Without confinement, the soliton spreads indefinitely ($r_{opt} \to \infty$, $\mathcal{I}_{scalar} \to 580$). The physical confinement is set by the topology of the phase winding itself.

The electron's phase profile follows the $(2,3)$ pattern with $c_3 = 3$ phase crossings, even though its ground-state topology is the unknot ($0_1$). In the torus knot classification, these are the $(2,q)$ torus knots with strictly **odd** $q$: the $(2,3)$ trefoil, the $(2,5)$ cinquefoil, the $(2,7)$ knot, and so on. There is no stable $(2,4)$ torus knot---the figure-eight knot ($4_1$) is not a torus knot and cannot be embedded on the chiral lattice.

The proton's phase winding passes through the **$(2,5)$ cinquefoil torus knot**---the next stable entry in the torus knot ladder after the electron's $c=3$ winding. Its $c_5 = 5$ crossings each absorb a fraction of the total Faddeev-Skyrme coupling $\kappa_{FS}$. 🔴 *[dimensional-provenance relabel 2026-06-08]* — prior text ~~"each constrain the soliton's radial phase gradient ... The confinement radius is therefore:"~~ framed $r_{opt}$ as a real-space length. $\kappa_{FS} = 8\pi$ is a **pure geometric (dimensionless) constant** (`src/ave/core/constants.py:683-687`: *"This is a pure geometric constant: the solid-angle normalisation"*), so $r_{opt} = \kappa_{FS}/c_5$ is a **dimensionless coupling-budget ratio, NOT a length**. The per-crossing coupling-budget partition is therefore:

> **[Resultbox]** *Cinquefoil Coupling-Budget Partition (dimensionless)*
>
> $$
> r_{opt} = \frac{\kappa_{FS}}{c_5} = \frac{8\pi}{5} \approx 5.03 \quad\text{(dimensionless; NOT a length)}
> $$

> 🔴 *[relabel 2026-06-08]* The prior resultbox read ~~"$r_{opt} = \kappa_{FS}/5 \approx 4.97\;\ell_{node}$"~~ and the following sentence ~~"This topological confinement means the proton extends over approximately five lattice spacings---a genuinely extended object in the substrate."~~ Both are **retired dimensional category errors**. $r_{opt}$ is a **dimensionless coupling-budget ratio, NOT a length** — the $\ell_{node}$ units were spurious, and the $4.97$ was a stale value ($8\pi/5 = 5.03$; the $4.97$ traced to an old $\delta_{th}=1/(28\pi)$ effective-coupling, mislabeled onto the cold $\kappa_{FS}=8\pi$ symbol). The proton is **NOT $\sim 5$ lattice spacings extended**: the only *measured* proton size is the charge radius $D_p = 0.841$ fm, which is **sub-node — $\approx 460\times$ smaller than one $\ell_{node} = 386$ fm**. The real-space sub-node geometry is an OPEN item, not a $\sim 5\,\ell_{node}$ extended object.

### The Structural Eigenvalue

To mathematically convert this pure topological volume into physical mass, it must be scaled by the discrete hardware limits of the substrate: the topological packing limit ($p_c \approx 0.1834$) derived in Chapter 2, and the inductive mass-stiffening ratio ($x_{core} = m_{core}/m_e$).

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

By resolving the dual-reactance count $\mathcal{V}_{total}=2$ (the node's two reactance sectors $X_L + X_C$ — NOT a geometric "toroidal halo volume"; see [`../../../common/dual-reactance-storage-taxonomy.md`](../../../common/dual-reactance-storage-taxonomy.md)), confining the soliton by the cinquefoil crossing number with Axiom 4 gradient saturation inside the energy functional, and adding the $+1$ integer twist required for global charge, the theoretical prediction converges to within $\mathbf{0.002\%}$ of the empirical CODATA proton mass ($1836.153\,m_e$). This is a **1-residual** result (the per-channel coupling $p_c = 8\pi\alpha$ is canonical-packing-plausible but not line-by-line derived — the one residual; vs standard Skyrme's two baryon-data-tuned parameters $F_\pi, e$), not a zero-parameter result. The inputs are electron-physics-provenanced ($m_e$, $\alpha$), so the parsimony claim of **zero baryon-data-tuned parameters** stands.

---
