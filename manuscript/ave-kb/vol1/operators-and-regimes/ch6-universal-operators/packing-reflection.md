[↑ Ch.6 Universal Operators](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [gdd70j]
path-stable: "referenced from vol1 as sec:universal_packing"
-->

## Section 6.8: The Universal Packing Reflection

Axiom 3 applied at the macroscopic scale: any confined system of $N$ nodes has an equilibrium packing fraction $\eta = P_C(1 - 1/N)$ from Axiom 4. The macroscopic reflection coefficient measures spatial mismatch:

> **[Resultbox]** *Packing Reflection Coefficient ($\Gamma_{pack}$)*
>
> <!-- eq:rg_target and eq:gamma_pack -->
>
> $$
> \begin{align}
> R_{g,target} &= \sqrt{\tfrac{3}{5}}\left(
>   \frac{3\,N\,V_{res}}{4\pi\,\eta_{target}}
> \right)^{1/3}, \qquad
> \eta_{target} = P_C\!\left(1 - \frac{1}{N}\right) \\[4pt]
> \Gamma_{pack} &= \frac{R_g - R_{g,target}}
>                       {R_g + R_{g,target}}
> \end{align}
> $$

This operator is domain-agnostic: it applies to protein globules, nuclear matter ($r_{node} = r_{proton}$), and any fluid in a finite cavity.

Code path: `universal_operators.universal_packing_reflection(Rg_sq, N, r_node, P_C)`.

---
