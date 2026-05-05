[↑ App F: Universal Solver Toolchain](./index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: d9ivj1 -->

## Nuclear Eigenvalue: Worked Examples

The nuclear domain produces **two** eigenvalues from the same equation, corresponding to two distinct cavities.

### Cavity 1: Proton QNM (Nucleon Resonance)

The proton is a cinquefoil ($c = 5$) soliton whose core is in the saturated regime ($S \to 0$, $G_{\mathrm{shear}} = 0$). Its charge radius $D_p = 4\,\lambda_p = 0.841$ fm marks the non-linear $\to$ saturated transition --- the "event horizon" of the strong force. Applying the universal solver:

$$
\begin{align}
r_{\mathrm{sat}} &= D_p = 0.841~\mathrm{fm}, \\
r_{\mathrm{eff}} &= D_p / (1 + \nu) = 0.654~\mathrm{fm}, \\
E &= \frac{\ell\,\hbar c}{r_{\mathrm{eff}}} = \frac{5 \times 197.3}{0.654} = 1508~\mathrm{MeV}.
\end{align}
$$

The $N(1520)\;D_{13}$ nucleon resonance has measured mass 1520 MeV (error: $-0.8\%$). Like a BH QNM, this is the proton "ringing" after perturbation --- energy leaks out as pions.

### Cavity 2: Pion Mass (Inter-Nucleon Medium)

The nuclear string tension $T_{\mathrm{nuc}} = m_p c^2 / l_{\mathrm{node}}$ (from the mass-stiffened tension of the Borromean lattice) creates a strain field between nucleons. Saturation occurs when the string energy equals the quantum confinement energy:

$$
T_{\mathrm{nuc}} \times r_{\mathrm{sat}} = \frac{\hbar c}{r_{\mathrm{sat}}}
\quad\Longrightarrow\quad
r_{\mathrm{sat}} = \sqrt{l_{\mathrm{node}} \times \lambda_p} = 9.01~\mathrm{fm}
$$

This is the geometric mean of the electron and proton Compton wavelengths --- the scale where electromagnetic ($l_{\mathrm{node}}$) and nuclear ($\lambda_p$) coupling strengths balance. The eigenvalue:

$$
E = \frac{5 \times \tfrac{9}{7} \times \hbar c}{r_{\mathrm{sat}}} = \frac{45}{7}\,c^2\,\sqrt{m_e\,m_p} = 140.8~\mathrm{MeV}
$$

The measured charged pion mass: $m_{\pi^\pm} = 139.57$ MeV (error: $+0.9\%$). Expressed in Faddeev units:

$$
\boxed{m_\pi = \frac{45}{7}\,\sqrt{I_{\mathrm{baryon}}}\;\,m_e \approx 140.8~\mathrm{MeV}}
$$

where $I_{\mathrm{baryon}} \approx 1836$ is the topological Faddeev eigenvalue. The pion is the nuclear analogue of the backbone amide-V mode: the resonance of the *medium between* confined objects, not the objects themselves.

---
