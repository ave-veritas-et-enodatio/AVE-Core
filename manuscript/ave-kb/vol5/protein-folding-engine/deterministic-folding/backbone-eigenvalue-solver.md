[↑ Protein Folding](../index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol5 as sec:backbone_eigenvalue -->

# Backbone Eigenvalue from the Universal Solver

The backbone resonance frequency $f_0 \approx 23$ THz and quality factor $Q \approx 7$ were introduced empirically in the Ramachandran derivation (from the amide-V IR band at 725 cm$^{-1}$). The following analysis shows that **both emerge from the same 5-step universal eigenvalue method** documented in the solver toolchain appendix---the identical procedure that predicts black hole quasi-normal modes to 1.7%.

**Step 1: Saturation boundary.**
The Pauli exclusion limit for the backbone is the $C_\alpha$--$C_\alpha$ virtual bond length, computed from the Flory four-atom distance formula:

$$d_0 = 3.80\;\text{Å} \quad \text{(from 3 bond lengths + 2 sp}^2\text{ angles + trans dihedral)}$$

**Step 2: Mode number.**
The mode number is quantised by the lattice constant in Bohr units:

$$\ell = \left\lfloor \frac{d_0}{a_0} \right\rceil = \left\lfloor 7.22 \right\rceil = 7$$

This is the protein-domain analog of $\ell = 2$ for gravitational waves. The backbone resonator fits seven electron orbitals along one lattice constant.

**Step 3: Poisson correction.**
$r_\mathrm{eff} = d_0 / (1 + \nu_\mathrm{vac}) = 2.96$ Å.

**Step 4: Eigenfrequency.**

$$f = \frac{\ell \cdot v}{2\pi \, r_\mathrm{eff}} = \frac{7 \times 5770}{2\pi \times 2.96 \times 10^{-10}} = 21.7\;\mathrm{THz} \quad (\text{error: } {+0.1\%}\text{ vs IR})$$

where $v = 5770$ m/s is the measured backbone group velocity.

**Step 5: Quality factor.**

$$Q = \ell = 7, \qquad \Delta f = f_0/Q = 3.1\;\text{THz} \quad (\text{measured: } {\sim}3.3\;\text{THz})$$

The $Q = 7$ that governs the reactive impedance scaling and the backbone linewidth throughout the folding engine is therefore **not an empirical input**: it is the topological mode number, derived from the same universal procedure as the black hole quality factor $Q = \ell = 2$.

---
