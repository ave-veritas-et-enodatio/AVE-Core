[↑ Network Solver](./index.md)
<!-- leaf: verbatim -->

# Explicit SPICE Transient Integration (v7 Upgrade)

Folding *kinetics* are modelled by explicit time-stepping of the backbone torsion angles, treating each degree of freedom as a lumped $L$-$C$-$R$ circuit element.

## Physical Model

The torsion angle $\theta_i$ at each residue behaves as a mechanical oscillator with:

- **Inductance** $L = 1.0$ per residue (normalised inertial mass of the backbone segment)
- **Resistance** $R = 0.5$ per residue (solvent friction $+$ radiative damping). The ratio $R/L = 0.5$ is set by the backbone $Q$-factor: a resonator with $Q \approx 7$ has $R/(2L\omega_0) = 1/(2Q) \approx 0.07$, and the Debye solvent time $\tau_w$ provides the additional viscous component.
- **Driving force** $-\nabla_i f(\boldsymbol{\theta})$ from the eigenvalue target gradient

## Equations of Motion

> **[Resultbox]** *SPICE Transient Equations*
>
> $$\begin{align}
>     v_i(t + \Delta t) &= v_i(t) + \frac{-\nabla_i f(\boldsymbol{\theta}) - R \cdot v_i(t)}{L} \cdot \Delta t \\
>     \theta_i(t + \Delta t) &= \theta_i(t) + v_i(t + \Delta t) \cdot \Delta t
> \end{align}$$

The system *rings down* into a topological equilibrium: the fold emerges from physical inertia and dissipation, not from artificial gradient descent schedules.

## Cotranslational Cascade (v7 Architecture)

The full-chain integration follows the biological ribosome's cotranslational folding:

1. **Segment phase**: The chain is divided into $Q$-length ($\approx 7$ residue) segments. Each segment is integrated via the SPICE equations while prior segments are frozen. This is the electrical analog of adding a tuned filter section to a cascade.
2. **Junction phase**: Junction residues at segment boundaries are released and integrated with zero initial momentum, allowing inter-segment contacts to relax.

The segment length $Q$ is the coherence length of the backbone resonator --- torsion angles separated by more than $Q$ residues are electromagnetically decoupled. This is a physical fact, not a tuning parameter.

## Derived Damping (Axioms 1 + 2)

The ring-down friction $R$ has two dissipation channels, both derived from the circuit model:

> **[Resultbox]** *SPICE Damping: Two Channels*
>
> $$R = \underbrace{\frac{1}{Q}}_{\text{backbone bend loss}} + \underbrace{\kappa_\text{HB} \cdot Z_\text{bb}^2}_{\text{solvent shunt loading}} = \frac{1}{0.75\pi^2} + \frac{1}{2Q} \cdot \bar{Z}_\text{bond}^2 \approx 0.887$$

Channel 1: each oscillation cycle radiates $1/Q$ of the stored energy through the sp$^3$ bend discontinuity at C$_\alpha$. Channel 2: each solvent-exposed residue has shunt admittance $G = \kappa_\text{HB} = 1/(2Q)$ to the ground plane, dissipating power $P = G \cdot Z_\text{bb}^2 \cdot v^2$. Only the ratio $R/L$ matters (L = 1 normalised) --- both channels are derived, zero fitted parameters.

## Derived Timestep Scaling Law

Each cotranslational segment requires 5 ring-down time constants ($\tau = L/R$) for 99% amplitude decay. The total Euler steps emerge from the chain length:

$$n_\text{steps}(N) = \left\lceil \frac{N}{Q} \right\rceil \times 2 \times \left\lceil \frac{5L}{R \cdot \Delta t} \right\rceil$$

Evaluated: $R \approx 0.887$, $\Delta t = 0.05$, $Q \approx 7.4$, which gives $n_\text{steps} \approx 226 N/Q$ with a floor of 2000. This automatically allocates more steps for larger proteins.

**Implementation.** Function `fold_cascade_transient_v7()` in `s11_fold_engine_v4_ymatrix.py`, calling `explicit_euler_step_jax()` from the universal `spice_transient.py` in the physics engine (`ave/solvers/`). The constant $R$ is imported as `R_DAMP_TOTAL` from `protein_bond_constants.py`.

---
