[↑ Ch.5 Global $A_c$ Scope](../index.md)
<!-- leaf: verbatim -->

# The Paradox of Per-Layer Buckling

In early developmental trials within virtual space, applying the Universal Saturation limit ($S = \sqrt{1 - r^2}$) on a **per-layer** basis induced catastrophic structural collapse. For advanced models (e.g., 9B parameter dense networks), executing the cutoff at $r \geq 1.0$ using a locally defined yield limit ($A_c = \text{mean}(A^2_{layer})$) forced the system to arbitrarily prune 40% to 55% of neurons *per layer*, indiscriminately scaling local variance.

This approach effectively assumed that the vacuum potential resets at every mathematical component boundary, an unphysical premise that violated the continuity of the LC cascade defined in Axiom 1.
