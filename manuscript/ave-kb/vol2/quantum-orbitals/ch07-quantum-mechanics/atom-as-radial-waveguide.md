[↑ Ch. 7: Quantum Mechanics and Atomic Orbitals](./index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: oltvwy, w6kk5y -->

## The Atom as a Radial Waveguide
<!-- claim-quality: oltvwy -->

The cross-shell coupling follows the same physics that governs orbits at every scale in AVE:

| System | Central source | Enclosed modifier |
|---|---|---|
| Galaxy | Central mass $M$ | Stars inside $r$: $M(r)$ |
| Planetary | Sun mass $M_\odot$ | Inner planets: $M_{\text{enc}}(r)$ |
| Atom | Nuclear charge $+Ze$ | Inner electrons: $-N_a e$ |

In each case, the orbiting body feels the **total enclosed source charge** (or mass) via Gauss's law. For the atom, Gauss's law IS Axiom 2. The outer electron at $R_b$ sees a net Coulomb potential that is still $1/r$:

$$
V_{\text{net}}(R_b) = -\frac{(Z - \sigma)\,\alpha\hbar c}{R_b}
$$

where $\sigma$ is the **Op4 orbit-averaged enclosed charge** from the inner shell.

<!-- claim-quality: w6kk5y -->
**Critical distinction from QM:**
- **QM (Slater):** $\sigma$ is an empirical parameter fitted to match data.
- **AVE (Op4):** $\sigma$ is *computed* from the orbit-averaged Coulomb integral (Stage C, Type 3). No free parameters.

### Orbit Shape and Penetration Depth (Axiom 1 + Axiom 2)

The effective potential felt by the soliton at radial position $r$:

$$
V_{\text{eff}}(r) = \underbrace{-\frac{Z\alpha\hbar c}{r}}_{\text{Coulomb (Axiom 2)}} \;+\; \underbrace{\frac{l^2\hbar^2}{2 m_e r^2}}_{\text{centrifugal (Axiom 1)}}
$$

For $l = 0$: no barrier — the soliton oscillates radially through all inner shells, seeing the full nuclear charge $Z$ part of the time. For $l = n{-}1$: fixed radius outside inner shells. The orbit-averaged enclosed charge $\sigma$ therefore depends on $l$: lower $l \to$ more penetration $\to$ smaller $\sigma \to$ higher $Z_{\text{net}} \to$ stronger binding $\to$ higher IE.

---
