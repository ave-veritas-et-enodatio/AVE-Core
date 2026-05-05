[↑ Ch. 11: The Standard Model Overdrive](./index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: dboxok -->

## The Universal Energy Functional

The optimiser minimises the total structural strain of an $N$-node system:

> **[Resultbox]** *Universal Strain Energy*
>
> $$
> U_{total} = \sum_{i < j}^{N} \frac{K_{mutual}}{d_{ij}} + \sum_{i} U_{bond}(\theta_i, \phi_i)
> $$

where $d_{ij}$ is the Euclidean separation between nodes $i$ and $j$, $K_{mutual}$ is the pairwise coupling constant, and $U_{bond}$ captures local bond-angle and torsional constraints. The first term is the $1/d$ mutual impedance; the second encodes the topological connectivity of the specific system.

Each gradient-descent step updates the nodal coordinates:

$$
\vec{r}_i^{(n+1)} = \vec{r}_i^{(n)} - \eta \, \nabla_{\vec{r}_i} U_{total}
$$

where $\eta$ is the step size. The algorithm converges when $|\nabla U| < \epsilon_{tol}$, the absolute structural strain is exhausted, and the global minimum-energy geometry is reached.

---
