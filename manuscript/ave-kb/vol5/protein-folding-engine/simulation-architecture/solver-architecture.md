[↑ Simulation Architecture](./index.md)
<!-- leaf: verbatim -->

# Solver Architecture

As of the v4/v5 engine, all machine-learning optimisers (Adam, Optax) have been **removed**. The protein fold is determined by two complementary analytical methods, both derived from first-principles EE/RF circuit theory.

## Method 1: Newton-Raphson Eigenvalue Root-Finding

The folded protein is the *eigenstate* of its impedance network. Finding it is a **root-finding** problem, not optimisation:

> **[Resultbox]** *Eigenvalue Root Target*
>
> $$\text{Find } \boldsymbol{\theta} \text{ such that } f(\boldsymbol{\theta}) = \lambda_{\min}\bigl(S^\dagger S(\boldsymbol{\theta})\bigr) \cdot S_\text{pack} + \mathcal{P}_\text{steric} = 0$$

where $\lambda_{\min}$ is the smallest eigenvalue of the Hermitian matrix $S^\dagger S$, $S_\text{pack} = \sqrt{1 - (\eta/P_C)^2}$ is the Axiom 4 packing saturation, and $\mathcal{P}_\text{steric}$ is the steric exclusion penalty.

The Newton-Raphson step is:

$$\Delta\boldsymbol{\theta} = -f(\boldsymbol{\theta}) \cdot \frac{\nabla f}{|\nabla f|^2}, \qquad |\Delta\theta_i| \leq \pi \;\;(\text{trust region})$$

The step size is *entirely determined* by the function value and gradient---no learning rate, no hyperparameters. The trust region $\pi$ is the geometric bound on angular variables. Convergence criterion: $|f| < 1/Q^2 \approx 0.018$ (the noise floor of the backbone resonator).

This is the *exact same* eigenvalue method used by the Periodic Table solver for nuclear binding ($K_{\text{MUTUAL}}$ eigenvalues), applied at the protein scale.

## Method 2: Explicit SPICE Transient Integration

Folding *kinetics* are modelled by explicit time-stepping (forward Euler integration) of lumped $L$-$C$-$R$ circuit elements:

> **[Resultbox]** *SPICE Transient Equations of Motion*
>
> $$\begin{align}
> v_i(t + \Delta t) &= v_i(t) + \frac{-\nabla_i f(\boldsymbol{\theta}) - R \cdot v_i(t)}{L} \cdot \Delta t \\
> \theta_i(t + \Delta t) &= \theta_i(t) + v_i(t + \Delta t) \cdot \Delta t
> \end{align}$$

where $L$ is the inertial mass (normalised to 1.0 per residue), $R$ is the combined radiative damping and solvent viscous friction (0.5 per residue), and $\nabla_i f$ is the eigenvalue target gradient.

The system naturally *rings down* into a topological equilibrium---the fold emerges from physical inertia and dissipation, not from artificial gradient descent schedules. The integration timestep $\Delta t$ is a *physical* parameter (not a learning rate) set by the Courant stability condition.

## Cotranslational Cascade (v7 Architecture)

The full-chain integration follows the biological ribosome's cotranslational folding:

1. **Segment Phase**: The chain is divided into $Q$-length ($\approx 7$ residue) segments. Each segment is integrated via SPICE transient while prior segments are frozen---like a tuned filter section being added to a cascade.
2. **Junction Phase**: Junction residues at segment boundaries are released and integrated with zero initial momentum, allowing inter-segment contacts to relax.

All constants in the solver ($Q$, $\kappa_\text{HB}$, trust region, convergence threshold) are derived from the axioms. The solver has **zero tunable hyperparameters**.

## Ramachandran-Basin Initialisation

The initial torsion angles are seeded from the three axiom-derived Ramachandran basins:

- $\alpha$-helix: $(\varphi, \psi) = (-57^\circ, -47^\circ)$
- $\beta$-sheet: $(\varphi, \psi) = (-120^\circ, 130^\circ)$
- PPII: $(\varphi, \psi) = (-75^\circ, 150^\circ)$

Sidechain $\chi_1, \chi_2$ angles are randomised uniformly in $[-\pi, \pi]$ (Glycine: $\chi = 0$; Alanine: $\chi_2 = 0$). Multiple random restarts verify that the solver converges to the same eigenstate regardless of initial topology.

---
