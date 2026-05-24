[↑ Ch. 7: Quantum Mechanics and Atomic Orbitals](./index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-oltvwy]
-->

## De Broglie Refractive Index on the AVE Lattice

The atom is a **spherical radial transmission line**. The nucleus at $r = 0$ projects a Coulomb field into all $4\pi$ steradians (Axiom 2). The lattice impedance is $Z_0 = 377~\Omega$ everywhere — the nuclear voltage $V/V_{\text{yield}} \sim Z\alpha^2 \approx 10^{-4}$ places the entire atom in the linear regime (Axiom 4 check).

The cavity that traps the electron forms from the defect's own **de Broglie dispersion** on the lattice. The energy-dependent refractive index:

> **[Resultbox]** *De Broglie Refractive Index on the AVE Lattice*
>
> $$
> n(r, \xi) = \sqrt{\frac{2\,Z_{\text{eff}}(r)\,a_0}{r} - \xi}
> $$

where $\xi = E/R_y$ is the trial energy in Rydberg units. Near the nucleus $n \to \infty$ (fast defect, low impedance, short circuit); at the classical turning point $n = 0$ (defect stops, high impedance, open circuit). Standing waves between these boundaries are the orbitals.

The physical `radial_eigenvalue` solver sweeps $\xi$ and computes $S_{11}$ via the ABCD cascade through the graded $n(r,\xi)$ profile. Eigenvalues are the values of $\xi$ where $S_{11}$ dips — exactly Op6 ($\lambda_{\min}(S^\dagger S) \to 0$). The ionization energy is

$$
IE = \xi_0 \times R_y
$$

where $\xi_0$ is the lowest dip in $|S_{11}(\xi)|^2$. For bare hydrogenic ions: $\xi_0 = Z^2$ emerges automatically ($Z^2$ scaling verified to $< 2\%$).

---
