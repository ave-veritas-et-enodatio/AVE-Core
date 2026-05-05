[↑ Ch. 7: Quantum Mechanics and Atomic Orbitals](./index.md)

<!-- kb-frontmatter
kind: leaf
claims: [oltvwy, w6kk5y]
-->

## The Chiral Factor: $p_c$ as Topological Coupling
<!-- claim-quality: w6kk5y -->

The $p_c/2$ correction in the coupling $k$ is not a fit or hypothesis. It is the **packing fraction**---the volume fraction of a lattice node that is saturated by the electron defect (Axiom 4).

Each electron saturates the lattice out to its confinement radius $d_{\text{sat}} = \ell_{\text{node}}$. The saturated volume is $V_{\text{sat}} = \frac{4}{3}\pi\,d_{\text{sat}}^3 = \frac{4}{3}\pi\,\ell_{\text{node}}^3$. The node volume is $V_{\text{node}} = \ell_{\text{node}}^3$. Therefore:

$$
p_c = \frac{V_{\text{sat}}}{V_{\text{node}}} \times \frac{e^2 / (4\pi\varepsilon_0)}{(\hbar c / 2)} = \frac{4\pi}{3} \times \frac{2 \cdot 4\pi\varepsilon_0 \alpha\hbar c}{4\pi\varepsilon_0 \hbar c} = \frac{4\pi}{3} \times 2\alpha \times 3 = 8\pi\alpha
$$

using $e^2 = 4\pi\varepsilon_0\alpha\hbar c$ (Axiom 2). The derivation is given in full in the macroscopic moduli chapter (Schwinger yield). The factor $8\pi = 2 \times 4\pi$ has the geometric interpretation established in the baryon chapter (where it appears as the Faddeev-Skyrme coupling $\kappa_{FS} = p_c/\alpha = 8\pi$):

- $4\pi$ --- the solid-angle normalisation of the spherical Gauss-law integral.
- $2$ --- the bilateral symmetry of the chiral LC condensate: two orthogonal principal strain axes jointly stabilize any topological defect against Derrick-type collapse.

The same $8\pi$ governs three distinct physical sectors:

| **Sector** | **Role of $8\pi$** | **Result** |
|---|---|---|
| Atomic (this chapter) | $J_{s^2} = \frac{1}{2}(1+8\pi\alpha)$ | He IE to 0.008% |
| Baryon | $\kappa_{FS} = 8\pi$ | Proton mass to 0.002% |
| Antenna (Vol. IV HOPF-01) | $\chi = \alpha \times f(\text{knot})$ | Chirality-shifted $f_{res}$ |

### Unification with the HOPF-01 Antenna
<!-- claim-quality: oltvwy -->

The HOPF-01 experimental antenna models torus knot resonators stitched on a PCB substrate. For each $(p,q)$ torus knot, the AVE topological coupling shifts the resonant frequency by a chiral factor $\chi_\text{knot} = \alpha \times pq/(p+q)$. The atom-antenna isomorphism maps each circuit element directly:

| **HOPF-01 Antenna** | **Atomic Orbital** |
|---|---|
| Wire loop (length $L$) | Flux loop ($2\pi R_n$) |
| Ground plane at height $h$ | Nucleus at distance $R_n$ |
| FR-4 medium ($\epsilon_\text{eff}$) | Saturated lattice ($\varepsilon_0 / \sqrt{1 - A^2}$, Axiom 4) |
| Half-wave resonator $c/(2L\sqrt{\epsilon})$ | Orbital frequency $Z^2\alpha^2 m_e c^2/(\hbar n^3)$ |
| Chiral factor $\chi = \alpha \cdot pq/(p+q)$ | $p_c = 8\pi\alpha$ |

Both systems are LC resonators on a discrete lattice, and in both cases the topological coupling enters as $\alpha$ times a purely geometric factor determined by the defect's knot or link type. At atomic scales, two linked unknots (the Hopf link of $1s^2$) produce the geometric factor $8\pi$; at macroscopic scales, the $(2,3)$ trefoil produces $6/5$. The coupling constant $\alpha$ is universal---it is the lattice's own self-coupling.

### Connection to Protein Folding

This same topological coupling determines the torsional stiffness of covalent bonds (Vol. V). The $sp^3$ tetrahedral angle ($109.5^\circ$) and the Ramachandran exclusion zones emerge from $p_c$-constrained LC phase-jitter applied to bond orbital pairs, unifying atomic ionization energy, baryon mass generation, and molecular steric hindrance under a single geometric constant.

---
