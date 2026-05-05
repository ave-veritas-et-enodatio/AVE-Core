[↑ Ch. 7: Quantum Mechanics and Atomic Orbitals](./index.md)

<!-- kb-frontmatter
kind: leaf
claims: [oltvwy, w6kk5y]
-->

## Scale Separation: Knot Topology vs Orbital Geometry
<!-- claim-quality: w6kk5y -->

Two solitons on the same shell interact through two physically distinct channels, set by the AVE axioms at two well-separated scales.

### Orbital Scale (Axiom 2)

The nuclear Coulomb strain field creates a Fabry--Perot cavity of radius $R \approx n^2 a_0 / Z$ (hundreds of $\ell_{\text{node}}$). The charge of each soliton ($-e$) screens the nuclear charge seen by its partner. Gauss's law applied to the Hopf link geometry gives $\sigma_{\text{Hopf}} = 1/2$ per partner. This screening is **isotropic**---it depends on the linking number (Axiom 3) and the enclosed charge fraction, but *not* on the relative orbital plane orientation ($m_l$).

### Knot Scale (Axioms 1+3)

Each soliton is an unknot flux tube with radius $\rho = 1/(2\pi)\,\ell_{\text{node}}$ (Axiom 1, ropelength). Two Hopf-linked solitons sit at poloidal positions $\theta = 0, \pi$ on the torus, tracing coplanar coaxial circles at radii $R \pm \rho$. The Neumann mutual inductance $M$ (Op1) is computed at this scale. For same-$m_l$ solitons: $M > 0$ (same azimuthal current direction). For different-$m_l$: $M = 0$ (orthogonal loops, proven by symmetry). This coupling is **anisotropic**---it depends on $m_l$.

### Scale Ratio

$$
\frac{R}{\rho} = \frac{n^2 a_0}{Z \rho} = \frac{2\pi n^2}{Z \alpha} \approx 430 \quad (n = 1,\; Z = 2)
$$

The knot and orbital scales are separated by a factor of $\sim 10^{2\text{--}3}$. They cannot be lumped into a single effective impedance. The correct procedure is:

1. **Cavity Eigenvalue** (orbital, distributed): The ABCD cascade computes the base standing wave eigenvalue $E_{\text{base}}$ from the nucleus to the radial turning point. Only *cross-shell* (different-$n$) bound states provide spherical Gauss shielding in this phase. Same-$n$ electrons are **excluded** from the CDF screening: they share the same torus and Gauss's law cannot resolve angular correlations on one torus. Same-$n$ interactions enter through Phase 2 (Hopf mode splitting) instead. The isolated core baseline is natively extracted as an effective charge bounded cavity:

$$
Z_{\text{eff\_core}} = \frac{R_{\text{target}}}{a_0} \sqrt{\frac{E_{\text{base}}}{\text{Ry}}}
$$

**Note:** Previous versions of the solver incorrectly included same-$n$ electrons in both the CDF screening (Phase 1) and the Hopf coupling (Phase 2), resulting in double-counting. For Beryllium, this produced $\text{IE} = 6.75$ eV ($-27.6\%$ error). After removing same-$n$ CDF, the corrected result is $\text{IE} = 9.72$ eV ($+4.3\%$ error, zero free parameters).

2. **Phase-Locked Orbital Expansion** (knot, anisotropic): Same-plane partners form a $\pi$ anti-phase Hopf dipole to minimize Op1 localized inductive stress. This resonant coupling lowers localized nodal frequency ($\omega_{\text{bonding}} = \omega_0 / \sqrt{1+k}$). By Axiom 4, this loss of inertial mass ($m_e \propto \hbar\omega/c^2$) forces the orbit to physically expand ($R \propto 1/m_e$). This mechanically drops the enclosed effective charge ratio, deriving Hund's Rule natively:

$$
Z_{\text{eff\_expanded}} = \frac{Z_{\text{eff\_core}}}{\sqrt{1 + k_{\text{topo}}}}
$$

where $k_{\text{topo}} = p_c/2 \approx 0.091$ represents the resonant gap of crossing unknots by Axiom 3.

3. **Co-Radial Topological Screening** (orbital, isotropic): All solitons bound to the exact same macroscopic $R_n$ cavity intersect dynamically rather than spherically shielding each other. By Axiom 3, intertwined or intersecting co-radial tracks provide exactly $\sigma_{\text{topological}} = 1/2$ shielding per partner. This $m_l$-blind reduction dynamically governs intermediate buckling domains like Boron ($2p^1$).

### The $p$-Shell Coupling

The $p$-shell has three spatial axes ($m_l = -1, 0, +1$). Two electrons in the *same* $m_l$ orbital form a Hopf link with parallel crossings (the standard $k_{\text{pair}}$). Two electrons in *different* $m_l$ orbitals have perpendicular tori---their crossings are *orthogonal* ($90^\circ$). From the nuclear scale (orthogonal flux tube crossings): the coupling at angle $\theta$ uses the crossing factor $(1+\cos\theta)/2$. For perpendicular tori ($\theta = 90^\circ$): $(1+0)/2 = 1/2$, confirmed independently by the elastic modulus ratio $G/K = 1/2$ (since $K = 2G$ from $\nu = 2/7$, Axiom 2), giving a reduced coupling:

$$
k_{\perp} = k_{\text{pair}} \times g, \qquad g = \frac{1}{2} = 0.500
$$

The $p$-shell coupling matrix is therefore a *weighted* graph (not $\mathrm{K}_6$), whose eigenvalues determine the mode spectrum.

<!-- claim-quality: oltvwy -->
### Hund's Rule Emergence

Hund's first rule emerges naturally from the phase-locked orbital expansion of same-$m_l$ pairs. Half-filled $p$-shells (e.g. nitrogen, $2p^3$) have all electrons in *different* $m_l$ orbitals, meaning no two sit on the same ring. Their orbits remain at the baseline cavity radius $R_0$, giving tighter binding and higher Ionization Energy (IE). Adding the fourth electron (oxygen, $2p^4$) forces a same-$m_l$ pairing. Pauli exclusion (Axiom 3) forces them into a $\pi$ anti-phase, creating a mutual inductance bonding mode. The resulting composite has a lower frequency $\omega$, meaning its effective orbit *expands* to $R_{\text{eff}} = R_0 \sqrt{1+k}$. This expansion reduces the nuclear binding eigenvalue, natively lowering the IE for Oxygen relative to Nitrogen.

### Orbital Expansion vs. Junction Susceptance

Initial hypotheses attempted to derive Hund's rule directly from the knot scale, modeling the $m_l$-dependent coupling as complex shunt susceptance $y = G + jB$ at the Hopf crossing, where $B \propto P_c$. However, numeric validation shows that a topologically locked soliton is highly rigid; its susceptance is $B \approx P_c / (2\pi^2) \approx 0.009$, giving a splitting $\sim 200\times$ too small to explain the Hund gap.

Instead, the mechanism is **Phase-Locked Orbital Expansion**. The same-$m_l$ pair forms a bonding mode with increased effective mass $m_{\text{eff}} = m_e\sqrt{1+k}$. By Axiom 4, this heavier composite orbits at a proportionally expanded radius $R_{\text{eff}} = R_0 \sqrt{1+k_{topo}}$, where $k_{topo} = P_c/2$. The ABCD cascade resolves this expanded cavity as a lower nuclear binding eigenvalue. This fundamentally links the topological $P_c$ parameter (knot interaction) to the macroscopic atom size (orbital standing wave), natively predicting $\text{IE}(\text{N}) > \text{IE}(\text{O})$ without free variables.

---
