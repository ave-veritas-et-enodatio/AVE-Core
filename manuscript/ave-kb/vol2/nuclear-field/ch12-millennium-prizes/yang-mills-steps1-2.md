[↑ Ch. 12: Mathematical Limits and the Millennium Prizes](./index.md)

<!-- kb-frontmatter
kind: leaf
claims: [q5izb7]
-->

## The Yang-Mills Mass Gap: Steps 1-2

### The Mathematical Paradox (What Clay Asks)

Prove that a non-trivial quantum field theory exists based on any compact simple gauge group $G$, and that it inherently possesses a strictly positive mass gap ($\Delta > 0$).

### The Missing Physics (Regime Boundary Conditions)

Pure gauge theories lack a physical spatial scale. Without a geometric elastic limit to force field confinement, there is no mathematical reason to require a finite, non-zero energy minimum. The AVE framework provides this limit through the discrete lattice pitch (Axiom 1) and field saturation (Axiom 4), which together guarantee a non-trivial Hamiltonian with a strictly positive mass gap.

### Step 1: The Lattice Hamiltonian

The Axiom 1 discrete lattice of pitch $\ell_\mathrm{node} = \hbar/(m_e c)$ supports normal modes with the finite-difference dispersion relation:

> **[Resultbox]** *Lattice Dispersion Relation*
>
> $$
> \omega(k) = \frac{2c}{\ell_\mathrm{node}}\;\left|\sin\!\left(\frac{k\ell_\mathrm{node}}{2}\right)\right|
> $$

This imposes a hard ultraviolet cutoff at $\omega_\mathrm{max} = 2c/\ell_\mathrm{node}$. No mode can oscillate faster, eliminating UV divergence.

Each lattice cell is an $LC$ oscillator with impedance $Z_\mathrm{cell} = \sqrt{\mu_0/\varepsilon_0} = Z_0$. Including Axiom 4 saturation:

$$
H_\mathrm{cell} = \tfrac{1}{2}\,\varepsilon_\mathrm{eff}(E)\,E^2\,\ell^3 + \tfrac{1}{2}\,\mu_\mathrm{eff}(B)^{-1}\,B^2\,\ell^3 \;\leq\; m_e c^2
$$

where $\varepsilon_\mathrm{eff} = \varepsilon_0\sqrt{1-(E\ell/V_\mathrm{snap})^2}$ and $\mu_\mathrm{eff} = \mu_0\sqrt{1-(B/B_\mathrm{snap})^2}$ (Axiom 4). The Hamiltonian is:

- **Bounded below**: $H \geq 0$ (both energy terms are non-negative).
- **Bounded above**: $H_\mathrm{cell} \leq m_e c^2$ (saturation caps the field).
- **Self-adjoint**: $Z = \sqrt{\mu_\mathrm{eff}/\varepsilon_\mathrm{eff}}$ is real and positive; multiplication by a real function is self-adjoint on $L^2$.

### Step 2: The Mass Gap (Unknot Ground State)

The *simplest* topological defect on the lattice is the unknot ($0_1$) --- a single closed electromagnetic flux loop whose minimum circumference is $\ell_\mathrm{node}$. Its rest energy defines the mass gap:

> **[Resultbox]** *Mass Gap (Unknot Ground State)*
>
> $$
> \Delta = m_e c^2 \approx 0.511 \text{ MeV}
> $$

This is not a zero-point oscillator argument ($\hbar\omega/2$). It is the rest energy of the lightest stable topological defect: a closed flux loop that cannot be continuously deformed to the vacuum without cutting the lattice. To prove $\Delta > 0$ rigorously, the Bogomol'nyi variational bound on the Faddeev-Skyrme energy functional gives:

$$
E[\phi] = 4\pi\!\int_0^{R}\! r^2 \left[\tfrac{1}{2}\left(\tfrac{d\phi}{dr}\right)^{2} + \tfrac{\kappa_\mathrm{FS}^2}{2}\,\frac{\sin^2\!\phi}{r^2}\left(\tfrac{d\phi}{dr}\right)^{2}\right] dr \;\geq\; \frac{2\pi^3 c}{\kappa_\mathrm{FS}} \;>\; 0
$$

where the bound follows from the topological constraint $\int |d\phi| = \pi$ (the defect must wind from $\phi = \pi$ at the core to $\phi = 0$ at infinity). Note: the full numerical solver additionally applies Axiom 4 gradient saturation $S(|d\phi/dr|\,/\,(\pi/\ell_\mathrm{node}))$ inside the integrand; the above provides the analytic lower bound.

---
