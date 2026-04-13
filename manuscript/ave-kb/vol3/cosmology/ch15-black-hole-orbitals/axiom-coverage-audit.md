[↑ Ch.15 Black Hole Orbitals](index.md)
<!-- leaf: verbatim -->

## Axiom Coverage Audit

The following table records which AVE axioms are fully exercised in the current black hole orbital model, and which require deeper integration:

| **Axiom** | **Statement** | **Status** | **Coverage** |
|---|---|---|---|
| 1 | LC lattice, $Z_0 = \sqrt{\mu_0/\varepsilon_0}$ | **Full** | Symmetric Gravity ($Z = Z_0$) |
| 2 | Topological defects (self-trapped $\gamma$) | **Full** | BH-electron isomorphism |
| 3 | Gravity = dielectric strain $n(r)$ | **Full** | Kerr saturation boundary, QPOs |
| 4 | Saturation ($V_{SNAP}$, viscosity) | **Full** | Phase transition, $Q = \ell$, $\tau_{ring}$ |

### Axiom 4 Saturation: Phase Transition and $Q = \ell$

At the saturation boundary ($\varepsilon_{11} = 1$), the lattice undergoes a **solid $\to$ fluid phase transition**. The shear modulus $G_{shear} \to 0$, eliminating transverse wave propagation in the interior. Gravitational waves, being transverse shear perturbations of the LC lattice, are **perfectly reflected** at this phase boundary.

The quality factor follows from the topological mode structure: with $\ell$ wavelengths fitting around the circumference, each releases $\sim 1/\ell$ of the mode energy per cycle via curvature radiation:

> **[Resultbox]** *QNM Quality Factor from Lattice Phase Transition*
>
> $$
> Q = \ell, \qquad \omega_I = \frac{\omega_R}{2\ell} = \frac{9}{98}\,\frac{c}{M_g}
> $$

For $\ell = 2$: $Q = 2$, $\omega_I M = 9/98 = 0.0918$ (GR exact: $0.0890$, error $3.2\%$).

This is the gravitational-scale manifestation of the **knot crossing number $\leftrightarrow$ mode number** isomorphism: the crossing number $c$ at the particle scale (confinement radius $r = \kappa/c$) plays the identical role to the angular mode number $\ell$ at the gravitational scale ($Q = \ell$). Each additional topological winding adds one unit of confinement stability.

Comparison against three LIGO events:

| **Event** | $a_*$ | $Q$ | $\tau$ AVE [ms] | $\tau$ obs [ms] | Error |
|---|---|---|---|---|---|
| GW150914 | 0.67 | 2 | 2.3 | 4.0 | 43% |
| GW170104 | 0.64 | 2 | 1.9 | 3.0 | 38% |
| GW190521 | 0.72 | 2 | 5.0 | 15.0 | $\dagger$ |

The Schwarzschild $Q = \ell = 2$ is used for all events; the Kerr correction to $Q$ (which increases Q for spinning remnants) is not yet included and accounts for the remaining $\tau$ discrepancy.

---
