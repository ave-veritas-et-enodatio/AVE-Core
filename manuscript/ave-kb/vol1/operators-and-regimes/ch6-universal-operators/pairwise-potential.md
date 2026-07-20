[↑ Ch.6 Universal Operators](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-gdd70j]
path-stable: "referenced from vol1 as sec:universal_pairwise"
-->

## Section 6.4: The Universal Pairwise Potential

The pairwise interaction between two nodes at separation $r$ is constructed by composing Operators 1--3:

> **[Resultbox]** *Universal Pairwise Potential ($U$)*
>
> <!-- eq:universal_pairwise -->
>
> $$
> U(r) = -\frac{K}{r}\bigl(T^2 - \Gamma^2\bigr), \qquad
> \Gamma(r) = \frac{Z(r) - Z_0}{Z(r) + Z_0}, \qquad
> Z(r) = \frac{Z_0}{\bigl(1 - (d_{sat}/r)^2\bigr)^{1/4}}
> $$

The three regime behaviours emerge automatically:

| **Regime** | **$r$ range** | **$\Gamma$** | **Physics** |
|---|---|---|---|
| I (Linear) | $r \gg d_{sat}$ | $\approx 0$ | Coulomb / gravity |
| II (Nonlinear) | $r \sim d_{sat}$ | $0 < \Gamma < 1$ | Nuclear / H-bond |
| III (Saturated) | $r \leq d_{sat}$ | $\to 1$ | Pauli wall |

Code path: `universal_operators.universal_pairwise_energy(r, K, d_sat)`. A JIT-compiled variant (`universal_pairwise_energy_jax`) is provided for $O(N^2)$ pairwise cost functions where the energy matrix must be evaluated at every optimiser step. The JAX variant replaces runtime duck-typing dispatch with static branching to satisfy `@jit` tracing requirements; the numerical output is identical.

---

### Blessing: pairwise-only composition is substrate-native

> **RULED 2026-07-20 (Grant verbatim [sic] "op4 bless"): the pairwise-only composition is BLESSED as substrate-native, not an approximation — every lattice coupling is bond-mediated and bonds are two-terminal (the pairwise composition IS the netlist; there are no three-terminal elements in the lattice). This tag is where any future derivation surfacing a genuine multi-node simultaneous term must record its contradiction.**

**Implementation grounding (verified 2026-07-20):** `universal_pairwise_energy(r, K, d_sat)` takes a single scalar separation $r$ between exactly two nodes; every N-body caller (e.g. `src/scripts/peer_review/high_z_boundary_analysis.py`, `src/scripts/vol_1_foundations/charge_sector_two_winding.py`) sums over pairs, so an N-body energy is $O(N^2)$ two-node evaluations, never a simultaneous three-or-more-node term. Multi-port structure in the lattice (the K4 vertex $A_1 \oplus T_2$ scattering, [`k4-port-irrep-decomposition.md`](./k4-port-irrep-decomposition.md); the Op5 multiport $Y\to S$ conversion) lives at the **junction** where two-terminal bonds meet under continuity + current conservation — a Kirchhoff node, not an irreducible three-terminal constitutive element. The blessing is therefore consistent with the multiport vertex physics: the vertex S-matrix is emergent from the two-terminal bonds, and the pairwise composition remains the netlist.

---
