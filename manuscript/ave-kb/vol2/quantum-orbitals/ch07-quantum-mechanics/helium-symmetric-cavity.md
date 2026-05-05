[↑ Ch. 7: Quantum Mechanics and Atomic Orbitals](./index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: w6kk5y -->

## Helium and the Symmetric Topological Cavity

The transition from Hydrogen ($Z=1$) to Helium ($Z=2$) introduces electron-electron interaction. In standard quantum mechanics, the Hartree-Fock method assumes independent probability clouds that screen the nuclear charge, yielding a variational limit of $23.06\text{ eV}$ for the first ionization energy against an experimental target of $24.58\text{ eV}$.

The AVE framework rejects the probabilistic point-particle smearing in favor of exact topological geometry.

### The Spatial Extent of the $0_1$ Unknot

While the classical Bohr radius establishes the macroscopic acoustic resonant cavity ($a_0 \approx 10^{-11}\text{ m}$), the electron itself is a $0_1$ topological unknot — an irreducible closed flux tube. As a massive structural defect, its internal strain field decays exponentially into the vacuum, governed inherently by the Weak Interaction mass ($M_W$):

> **[Resultbox]** *Weak Interaction Decay Length*
>
> $$
> \lambda_W = \frac{\hbar}{M_W c} \approx 2.4 \times 10^{-18}\text{ m}
> $$

Because the unknot's internal structural radius ($10^{-18}\text{ m}$) is seven orders of magnitude smaller than the host acoustic cavity ($10^{-11}\text{ m}$), the electron acts as a perfect mathematical point-defect bounding the macroscopic WKB acoustic phase integral ($\int k\,dr = \pi$).

### The Mutual Cavity Loading Architecture

When multiple $0_1$ unknots (electrons) share the identical symmetric macroscopic cavity, standard approximations rely on computing continuous volumetric integrals over smeared probability distributions and deploying heuristically tuned effective screening charges ($Z_{eff}$).

The AVE framework completely rejects continuous integration and arbitrary charge fitting. Instead, the multi-electron atom is modeled exactly through **Mutual Cavity Loading**. All electrons within a principal shell are driven strictly by the bare nuclear core charge $Z$; macroscopic "screening" between them emerges purely and algebraically from their collective impedance mismatch against the $377 \; \Omega$ vacuum.

**The N-Electron Pipeline.** The atomic solver pipeline invokes three universal scale-invariant operators to compute exact ionization energies without free parameters:

1. **Op1 (Impedance Loading):** Each electron acts as a parallel admittance loading the shared macroscopic cavity. The effective loading factor $N_{eff}$ is determined by the topological geometry of the orbital intersections. Compressional $s$-orbitals load fully ($N_s = 1.0$), while transversal $p$-orbitals load exactly at half-efficiency ($N_p = 0.5$) due to the $K=2G$ vacuum modulus constraint.

2. **Op3 (Mismatch Reflection):** The continuously loaded cavity evaluates as an integrated transmission boundary against the vacuum. The structural eigenvalue of the cavity binding is rigidly scaled by the acoustic transmission coefficient $T^2$:

$$
T^2(N_{eff}) = \frac{4N_{eff}}{(1+N_{eff})^2}
$$

3. **Hund's Rule Topological Strain:** When traversing the $p$-shell ($2p^4$ to $2p^6$), electrons are forced into shared transversal axes, forming discrete Hopf intersections. The lattice strain exactly mirrors the loss of geometric symmetry.

By applying the Mutual Cavity Loading architecture to Helium's $1s^2$ shell ($N_{eff} = 2.0$), the active engine solver computes the first ionization energy algebraically:

> **[Resultbox]** *Helium 1st Ionization Energy (Mutual Cavity Loading)*
>
> $$
> IE_\text{He (AVE)} = 24.19\text{ eV} \qquad \text{(Target: } 24.587\text{ eV, } \Delta = -1.6\%\text{)}
> $$

### Field-Oriented Control (FOC) and the Secondary Density Wake

As the atom scales to Beryllium ($Z=4, 1s^2 2s^2$), a second macroscopic acoustic cavity boundary ($n=2$) is populated. The $1s^2$ inner core acts as a primary inductive rotor, generating an intense macroscopic density wake along its primary axis of oscillation.

The incoming $2s^2$ valence pair spontaneously structures itself to phase-lock **perpendicularly** ($90^\circ$ orientation offset) to the $1s$ core axis. This orthogonal topological phase-locking is mathematically isomorphic to **Field-Oriented Control (FOC)** in engineering, where stator and rotor magnetic fields are artificially maintained at $90^\circ$ to completely decouple their mutual inductance.

> **[Resultbox]** *Outer Shell Phase-Separation Limit ($2s^2$)*
>
> $$
> J_{2s} = p_c \cdot S(p_c) = p_c \sqrt{1 - p_c^2} \approx 0.18029
> $$

**Asynchronous Frequency Decoupling** cancels the *inductive* (magnetic, time-varying) coupling between principal shells:

$$
\langle M \rangle \propto \int_0^T \cos((\omega_1 - \omega_2)t) \, dt = \mathbf{0}
$$

However, the *capacitive* (Coulomb, DC) coupling persists. This capacitive cross-shell coupling enters the $N$-port admittance matrix as a mutual admittance $y_{ij}$ through the $Z_0 = 377\,\Omega$ vacuum lattice.

### The $p$-Shell Isomorphism: Orthogonal Inductive Buckling

As the atomic sequence progresses into the $p$-subshell (Boron $2p^1$ to Neon $2p^6$), the lattice undergoes a mechanical phase transition driven by the minimization of structural strain (Axiom 1).

**The Emergence of Orthogonality (Boron $Z=5$).** When the third electron ($2p^1$) enters the $n=2$ cavity, the lattice buckles the third electron's track exactly $90^\circ$ into a polar orbit. Because the tracks are globally perpendicular, the Neumann mutual inductance vanishes analytically ($M_{90} \equiv 0$). The $p$-shell emerges natively as an orthogonal relief valve for inductive frustration.

**Co-Radial Clipping vs. Spherical Shielding.** Because the $2s$ and $2p$ electrons share the exact same $n=2$ fundamental cavity radius ($R_n$), the screening fraction of intertwined unknots drops from a perfect sphere ($\sigma = 1.0$) down to exactly $\sigma_{\text{topological}} = 1/2$ per partner.

**Isomorphism to Protein Folding Torsional Limits.** The topological rigidity of these valence phase-locks is the fundamental mechanical source of molecular steric hindrance. The $p$-shell electrons strongly resist any deviation from their minimal-impedance phase angles because such deviations drastically spike their mutual inductance. This exact mechanism creates the physically impassable Ramachandran exclusion zones ($\phi, \psi$ steric crashes) that force proteins to fold exclusively into canonical $\alpha$-helices and $\beta$-sheets.

---
