[↑ Ch.1 Vacuum Circuit Analysis](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [p5cf3t]
-->

## The Relativistic Inductor (Lorentz Saturation)

Under the Topo-Kinematic identity, mass maps to inductance ($L = \xi_{topo}^{-2}\, m$) and velocity maps to current ($I = \xi_{topo}\, v$). The relativistic mass increase $m_{eff} = \gamma\, m_0$ therefore maps directly to a current-dependent inductance:

> **[Resultbox]** *Relativistic Inductor*
>
> $$
> L_{eff}(I) = \frac{L_0}{\sqrt{1 - \left(\dfrac{I}{I_{max}}\right)^{\!2}}}, \qquad I_{max} = \xi_{topo}\, c \approx 124.4 \text{ A}
> $$

This is structurally identical to the varactor equation, with the substitution $V \to I$ and $V_{yield} \to I_{max}$. The symmetry is not coincidental: both are projections of the single Axiom 4 kernel onto the electric and magnetic sectors, respectively.

### Derivation of $E = mc^2$

The energy stored in a current-carrying inductor is $E = \tfrac{1}{2} L_{eff}\, I^2$. Expanding at low velocity ($v \ll c$):

$$
E = \frac{1}{2} \frac{L_0}{\sqrt{1-(v/c)^2}}\, (\xi_{topo}\, v)^2 = \frac{1}{2} \gamma\, \xi_{topo}^{-2}\, m_0\, \xi_{topo}^2\, v^2 = \frac{1}{2} \gamma\, m_0\, v^2
$$

At $v = 0$, the rest energy stored in the inductor's self-field is $E_0 = \tfrac{1}{2} L_0 I_{max}^2 = \tfrac{1}{2} (\xi_{topo}^{-2} m_0)(\xi_{topo} c)^2 = \tfrac{1}{2} m_0 c^2$. Summing with the capacitive (potential) energy via the Virial Theorem recovers $E_{total} = m_0 c^2$.

### Why SPICE Cannot Exceed $c$

In a standard SPICE transient simulation, the inductor $L_0$ limits the current slew rate to $dI/dt = V/L$. As $I \to I_{max}$, $L_{eff} \to \infty$, and the slew rate collapses to zero. The circuit physically cannot push current (matter) past the hardware limit. SPICE engines natively enforce Special Relativity without any code modification.

---
