[↑ Computational Mass Defect](../index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol6 as sec:d_derivation -->
<!-- claim-quality: llqd1n, lqanmt -->

> ↗ See also: [Axiom 1 — Lattice Structure](../../../vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md) — standing-wave condition on the $\mathcal{M}_A$ lattice that sets $d$

## Derivation of the Nucleon Spacing ($d$) from Axiom 1
<!-- claim-quality: lqanmt (the $D_{\rm intra} = d\sqrt{8}$ derived here is the geometric input substituted into the mutual-coupling-constant computation $K \approx 11.337$ MeV·fm) -->

The fundamental spatial scale of the nuclear LC network is the **proton spin radius** $d$---the radius of a single nucleon's gyroscopic orbit. This is derived directly from the substrate topology (Axiom 1) and the torus knot isomorphism (Axiom 2).

Each nucleon is a self-intersecting torus knot whose rest energy is entirely stored in the standing-wave mode of the vacuum LC lattice. By Axiom 1, the standing-wave condition requires the loop circumference to equal exactly 4 half-wavelengths of the nucleon's Compton oscillation:

$$
2\pi \cdot \frac{d}{2} = 4 \cdot \frac{\lambda_{\text{Compton}}}{2} = 4 \cdot \frac{\pi \hbar}{m_p c} \quad\Longrightarrow\quad \boxed{d = \frac{4\hbar}{m_p c} \approx 0.841 \text{ fm}}
$$

This is the `D_PROTON` constant in the physics engine. No empirical fit is involved---$d$ is fully determined by $\hbar$, $m_p$, and $c$ (all Axiom 1 substrate quantities).

### Intra-Alpha Distance ($D_{\text{intra}}$) from Tetrahedral Packing

The Helium-4 Alpha particle consists of 4 nucleons (2$p$ + 2$n$) at the vertices of a regular tetrahedron. For a tetrahedron with edge length $a$, the center-to-vertex distance is $a\sqrt{3/8}$. The nucleons pack at the minimum mutual distance set by their spin radii:

$$
a = d \cdot \sqrt{8} \quad\text{(tetrahedral edge from spin radius)}
$$

This follows from the FCC close-packing condition: four spheres of diameter $d$ touch at vertices of a tetrahedron whose edge length is $d\sqrt{8}$. Therefore the nearest-neighbor nucleon separation within the alpha is:

<!-- claim-quality: llqd1n (the $D_{\rm intra}$ value here is the axiom-derived geometric input that the per-nucleus $R$ fit references — the catalog masses are reported as multiples of $d$, and the fitting tolerance is computed against this canonical scale) -->
$$
\boxed{D_{\text{intra}} = d\sqrt{8} = \frac{4\hbar}{m_p c} \cdot \sqrt{8} \approx 2.379 \text{ fm}}
$$

---
