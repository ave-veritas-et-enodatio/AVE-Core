[↑ Ch.4 Phase Transitions](../index.md)
<!-- leaf: verbatim -->

# Topological Cell Collapse (State II Volume)

The classic thermodynamic anomaly of water---that it shrinks upon melting to reach a maximum density at $\sim 4°$C---arises directly from the yielding of its topological LC matrix.

Classical models struggle to reproduce the density of liquid water (998 kg/m$^3$ at 20$°$C) from its molecular geometry without invoking arbitrary empirical packing radii. If one treats a water molecule as a continuous solid boundary (like a 3-sphere exact geometric union), its bare spatial volume is rigidly $5.56\ \text{A}^3$. Dividing this by the $\varphi_{FCC}$ Kepler packing fraction yields an absurd packed density of nearly 4000 kg/m$^3$.

In AVE (Axiom 1), spatial volume is not the geometric hull of a particle, but the volumetric capacity of a loaded discrete network cell. We derive the macroscopic liquid state (State II) volume without spatial bounds, relying strictly on the K=2G topological collapse (Axiom 2).

## State I: The Open Lattice ($V_I$)

The rigid, unyielded State I is a tetrahedral lattice dictated by the Op4 pairwise minimum distance ($d_{OO} = d_{OH} + d_{hb} = 2.726\ \text{A}$). The unit cell volume natively occupied by one molecule in this expanded topology is:

$$
V_I = \frac{8}{3\sqrt{3}} d_{OO}^3 = 31.21\ \text{A}^3
$$

This establishes a theoretical ice density of 958 kg/m$^3$ (experimental Ice Ih is 917 kg/m$^3$).

## State II: FCC Maximal Yield ($V_{II}$)

When the thermal energy surpasses the Op4 barrier ($f_I < 1.0$), the strict tetrahedral orientation fractures. The network yields to the universal packing ceiling prescribed by Axiom 2: $K=2G \rightarrow$ FCC packing.

Crucially, the foundational node-to-node proximity ($d_{OO} = 2.726\ \text{A}$) does not change---the Op4 minimum remains intact even in the disorganized slush. The only metric that changes is the global topology: the exact spatial cells of State I forfeit their stretched spatial arrangement and collapse into FCC maximal packing. Therefore, the volume of the fully yielded State II fluid is simply the State I volume compacted by Kepler's packing fraction $\varphi = \pi\sqrt{2}/6 \approx 0.7405$:

> **[Resultbox]** *Topological Cell Collapse (State II Volume)*
>
> $$
> V_{II} = V_I \times \varphi_{FCC} = V_I \times \frac{\pi\sqrt{2}}{6} \approx 23.11\ \text{A}^3
> $$

## The Density Anomaly

By evaluating the structural mixture at $20°$C, the lattice survival fraction (from the Op4 cooperative solver) is $f_I \approx 0.735$. Incorporating anharmonic thermal expansion ($V_{th} \approx 0.67\ \text{A}^3$):

$$
V_{avg} = f_I V_I + (1-f_I) V_{II} + V_{th} \approx 0.735(31.21) + 0.265(23.11) + 0.67 = 29.74\ \text{A}^3
$$

The resulting macroscopic density is $m_{H_2O} / V_{avg} = 1005.8$ kg/m$^3$. This yields precisely the experimental liquid state with a $\mathbf{+0.7\%}$ error, entirely devoid of empirical collision or hard-sphere parameters.

The density anomaly occurs because the melting term ($V_I \to V_{II}$) is a pure contraction, while thermal vibrations ($V_{th}$) are pure expansions. The competition balances precisely near the theoretical melting eigenmode.

---
