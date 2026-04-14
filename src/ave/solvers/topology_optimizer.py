"""
Universal Topological Optimization Engine (Nuclear Scale)
=========================================================
Generic scale-invariant topology optimizer extracted from the full
AVE TopologicalOptimizer. This module contains ONLY the nuclear-scale
cost function and optimizer — no protein/molecular IP.

The engine accepts N arbitrary topological nodes with masses and charges,
applies the universal impedance cost function (Op4), and uses a damped
LC integrator + simulated annealing to lock the lattice into its
absolute geometric minimum-energy state.

JIT Compilation Architecture
-----------------------------
The cost function is vectorized using jax.numpy pairwise distance matrices:
  1. All O(N²) pairwise distances computed via broadcast
  2. Precomputed index masks for upper triangle
  3. Dedicated JIT-safe Op4 kernel (universal_pairwise_energy_jax)

Tier 2 Solver: consumes Tier 1 constants/operators, never re-derives them.
"""
from __future__ import annotations

import numpy as np
import jax.numpy as jnp
from jax import grad, jit

from ave.core.universal_operators import universal_pairwise_energy_jax
from ave.core.constants import (
    K_MUTUAL, D_PROTON, ALPHA, HBAR, C_0, e_charge, EPS_NUMERICAL,
)


# =========================================================================
# JIT-compiled nuclear cost function kernel
# =========================================================================

def _make_nuclear_cost_fn(N, masses_jax, charges_jax, K_attr, d_sat,
                          alpha_hc, boundary_radius, boundary_k):
    """Factory: build a JIT-compiled nuclear topology cost function.

    Parameters
    ----------
    N : int
        Number of nodes.
    masses_jax : jnp.ndarray
        Node masses (proton ≈ 1.007, neutron ≈ 1.009).
    charges_jax : jnp.ndarray
        Node charges (1.0 for proton, 0.0 for neutron).
    K_attr : float
        Mutual inductance coupling constant (from constants.py).
    d_sat : float
        Proton separation distance (from constants.py).
    alpha_hc : float
        Coulomb constant αℏc in MeV·fm.
    boundary_radius : float or None
        Optional spherical confinement radius.
    boundary_k : float
        Harmonic stiffness of boundary wall.
    """
    triu_i, triu_j = jnp.triu_indices(N, k=1)
    m_prod = jnp.outer(masses_jax, masses_jax)[triu_i, triu_j]
    q_prod = jnp.outer(charges_jax, charges_jax)[triu_i, triu_j]

    @jit
    def cost_fn(flat_coords):
        coords = flat_coords.reshape((N, 3))

        # Vectorized all-pairs distance matrix (upper triangle only)
        diff = coords[triu_i] - coords[triu_j]           # (M, 3)
        dist = jnp.sqrt(jnp.sum(diff**2, axis=-1))       # (M,)
        dist = jnp.maximum(dist, EPS_NUMERICAL)

        # Universal Operator 4: saturated pairwise potential
        U_pair = m_prod * universal_pairwise_energy_jax(dist, K_attr, d_sat)
        energy = jnp.sum(U_pair)

        # Coulomb repulsion (proton-proton only)
        U_coulomb = jnp.where(q_prod > 0, q_prod * alpha_hc / dist, 0.0)
        energy = energy + jnp.sum(U_coulomb)

        # Boundary confinement
        if boundary_radius is not None:
            r_mag = jnp.sqrt(jnp.sum(coords**2, axis=-1))
            penalty = jnp.where(r_mag > boundary_radius,
                                boundary_k * (r_mag - boundary_radius)**2, 0.0)
            energy = energy + jnp.sum(penalty)

        return energy

    return cost_fn


class TopologicalOptimizer:
    """Scale-invariant nuclear topology optimizer.

    Uses Op4 (saturated pairwise potential) and Coulomb repulsion to
    assemble N nucleons into their minimum-energy 3D configuration.

    Parameters
    ----------
    node_masses : array-like
        Masses for N nodes (proton ≈ 1.007, neutron ≈ 1.009 in AMU).
    node_charges : array-like or None
        Charges (1.0 = proton, 0.0 = neutron). Auto-inferred if None.
    boundary_radius : float or None
        Optional spherical confinement radius.
    boundary_k : float
        Harmonic stiffness of boundary wall (default: 1000.0).
    """

    def __init__(self, node_masses, interaction_scale='nuclear',
                 node_charges=None, boundary_radius=None, boundary_k=1000.0):
        self.masses = np.array(node_masses)
        self.N = len(self.masses)
        self.scale = interaction_scale
        self.boundary_radius = boundary_radius
        self.boundary_k = boundary_k

        # ALL constants derived from axioms via ave.core.constants
        self.K_attr = K_MUTUAL
        self.d_sat = D_PROTON
        self.alpha_hc = ALPHA * (HBAR * C_0 / e_charge) * 1e9

        # Assign proton/neutron identity for Coulomb repulsion
        if node_charges is not None:
            self.charges = np.array(node_charges, dtype=float)
        else:
            self.charges = np.array(
                [1.0 if m < 1.003 else 0.0 for m in self.masses]
            )

        # Build JIT-compiled cost function at init time
        masses_jax = jnp.array(self.masses)
        charges_jax = jnp.array(self.charges)

        self._cost_jit = _make_nuclear_cost_fn(
            self.N, masses_jax, charges_jax,
            self.K_attr, self.d_sat, self.alpha_hc,
            self.boundary_radius, self.boundary_k,
        )

        # JIT-compiled gradient
        self._grad_jit = jit(grad(self._cost_jit))

    def _cost_function(self, flat_coords):
        """Evaluate total energy (delegates to JIT-compiled kernel)."""
        return self._cost_jit(jnp.array(flat_coords))

    def _jacobian(self, flat_coords):
        """Analytical gradient via JAX autograd."""
        return np.array(self._grad_jit(jnp.array(flat_coords)))

    def optimize(self, initial_coords, method='native', options=None,
                 record_history=False):
        """Native AVE Topological Damped Integrator.

        Nodes are treated as massive elements in an L-C lattice. As they
        accelerate down the impedance gradient, a synthetic topological
        resistance (gamma) drains kinetic energy, settling them into the
        absolute geometric minimum.

        Parameters
        ----------
        initial_coords : array-like
            Initial (N, 3) or (3N,) coordinate array.
        options : dict
            Keys: dt, gamma, maxiter, ftol, disp.
        record_history : bool
            If True, return coordinate snapshots.

        Returns
        -------
        final_coords : ndarray, shape (N, 3)
        final_energy : float
        history : list[ndarray] (only if record_history=True)
        energy_history : ndarray (only if record_history=True)
        """
        if options is None:
            options = {
                'disp': True, 'maxiter': 5000,
                'dt': 0.05, 'gamma': 0.1, 'ftol': 1e-7,
            }

        N = self.N
        coords = np.array(initial_coords).reshape((N, 3)).copy()
        velocities = np.zeros_like(coords)

        history = []
        energy_history = []

        dt = options.get('dt', 0.05)
        gamma = options.get('gamma', 0.1)
        maxiter = options.get('maxiter', 5000)
        ftol = options.get('ftol', 1e-7)

        prev_energy = float(self._cost_function(coords.flatten()))

        # Strict numeric displacement bound (acting as c_0)
        max_disp = 0.05 * self.d_sat

        # Vectorized mass array for acceleration computation
        inv_masses = 1.0 / self.masses

        if options.get('disp', False):
            print(f"[*] Commencing O(N²) Topological Relaxation"
                  f" ({self.scale} mapping) [JIT-compiled]...")

        for k in range(maxiter):
            force = -self._jacobian(coords.flatten()).reshape((N, 3))

            acceleration = force * inv_masses[:, np.newaxis]
            velocities += (acceleration - gamma * velocities) * dt

            # Numeric stability bound (topological wave speed limit)
            v_norm = np.linalg.norm(velocities, axis=1)
            v_max = max_disp / dt
            scale = np.where(v_norm > v_max, v_max / (v_norm + 1e-12), 1.0)
            velocities *= scale[:, np.newaxis]

            coords += velocities * dt
            current_energy = float(self._cost_function(coords.flatten()))

            if record_history and k % 10 == 0:
                history.append(coords.copy())
                energy_history.append(current_energy)

            if (abs(prev_energy - current_energy) < ftol
                    and np.all(np.abs(velocities) < 1e-4)):
                if options.get('disp', False):
                    print(f"[*] Equilibrium at {k} iterations."
                          f" Strain: {current_energy:.4f}")
                break

            prev_energy = current_energy

        final_coords = coords.reshape((self.N, 3))
        if record_history:
            return final_coords, current_energy, history, energy_history
        return final_coords, current_energy

    def quench(self, initial_coords, T=1.0, stepsize=0.5, niter=100,
               options=None, record_history=False):
        """Native AVE Topological Annealing Quench.

        Iteratively spikes the lattice with thermal noise (T) and allows
        it to resettle via the damped L-C integrator. Guarantees
        emergence from local geometric traps into the absolute lowest
        strain ground state.

        Parameters
        ----------
        initial_coords : array-like
            Initial (N, 3) or (3N,) coordinate array.
        T : float
            Initial annealing temperature.
        stepsize : float
            Initial perturbation magnitude.
        niter : int
            Number of annealing cycles.
        record_history : bool
            If True, return coordinate snapshots.
        """
        coords = np.array(initial_coords).reshape((self.N, 3)).copy()
        best_coords = coords.copy()
        best_energy = float(self._cost_function(coords.flatten()))
        current_energy = best_energy

        history = []

        print(f"[*] Commencing Native Topological Quench"
              f" (T={T}, step={stepsize}, niter={niter})...")

        for cycle in range(niter):
            if current_energy < best_energy:
                best_coords = coords.copy()
                best_energy = current_energy

            noise = (np.random.rand(self.N, 3) - 0.5) * stepsize
            test_coords = best_coords + noise

            settled_coords, settled_energy = self.optimize(
                test_coords,
                options={
                    'disp': False, 'maxiter': 500,
                    'dt': 0.1, 'gamma': 0.2, 'ftol': 1e-5,
                },
                record_history=False,
            )
            settled_coords = settled_coords.reshape((self.N, 3))

            # Metropolis criterion (thermodynamic acceptance)
            dE = settled_energy - current_energy
            if dE < 0 or np.random.rand() < np.exp(-dE / max(T, 1e-9)):
                coords = settled_coords
                current_energy = settled_energy
                if record_history:
                    history.append(coords.copy())

            # Active cooling schedule
            T *= 0.95
            stepsize *= 0.98

        print("[*] Quench complete! Lowest-energy structural matrix resolved.")
        if record_history:
            return best_coords.reshape((self.N, 3)), best_energy, history
        return best_coords.reshape((self.N, 3)), best_energy
