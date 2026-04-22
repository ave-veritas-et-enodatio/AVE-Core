"""
Lattice Boltzmann Fluid Solver for the AVE Vacuum
===================================================

Solves the incompressible Navier-Stokes equations on the same 3D grid
as the FDTD Maxwell solver, treating the vacuum as a Cosserat fluid.

The vacuum has:
    - Density: ρ_vac = ε₀ μ₀ c² = ε₀ (from ε₀E² = energy density)
    - Viscosity: ν = 1/(4π) × ℓ_node × c (kinematic, from Axiom 1)
    - Yield stress: τ_y = B_snap²/(2μ₀) (Bingham plastic, from Axiom 4)

Uses the D3Q19 lattice Boltzmann model with BGK collision operator.

The FDTD ponderomotive force F = -∇(½εE²) enters as a body force
in the LBM collision step, coupling Maxwell → Navier-Stokes.

Usage:
    from ave.core.lbm_3d import LBM3DEngine
    lbm = LBM3DEngine(nx, ny, nz, dx=0.01)
    lbm.set_body_force(Fx, Fy, Fz)  # from FDTD ponderomotive_force()
    lbm.step()
"""

from __future__ import annotations

import numpy as np

# D3Q19 lattice velocities and weights
# 19 discrete velocities: 1 rest + 6 face + 12 edge
_E = np.array(
    [
        [0, 0, 0],  # 0: rest
        [1, 0, 0],  # 1-6: faces
        [-1, 0, 0],
        [0, 1, 0],
        [0, -1, 0],
        [0, 0, 1],
        [0, 0, -1],
        [1, 1, 0],  # 7-18: edges
        [-1, 1, 0],
        [1, -1, 0],
        [-1, -1, 0],
        [1, 0, 1],
        [-1, 0, 1],
        [1, 0, -1],
        [-1, 0, -1],
        [0, 1, 1],
        [0, -1, 1],
        [0, 1, -1],
        [0, -1, -1],
    ],
    dtype=np.float64,
)

_W = np.array(
    [
        1.0 / 3.0,  # rest
        1.0 / 18.0,
        1.0 / 18.0,
        1.0 / 18.0,  # faces
        1.0 / 18.0,
        1.0 / 18.0,
        1.0 / 18.0,
        1.0 / 36.0,
        1.0 / 36.0,
        1.0 / 36.0,
        1.0 / 36.0,  # edges
        1.0 / 36.0,
        1.0 / 36.0,
        1.0 / 36.0,
        1.0 / 36.0,
        1.0 / 36.0,
        1.0 / 36.0,
        1.0 / 36.0,
        1.0 / 36.0,
    ]
)

# Opposite direction indices for bounce-back
_OPP = np.array([0, 2, 1, 4, 3, 6, 5, 10, 9, 8, 7, 14, 13, 12, 11, 18, 17, 16, 15])

Q = 19


class LBM3DEngine:
    """
    3D Lattice Boltzmann solver for the AVE vacuum.

    Args:
        nx, ny, nz: Grid dimensions (must match FDTD grid).
        dx: Cell size [m].
        nu: Kinematic viscosity [m²/s]. Default from AVE: ℓ·c/(4π).
        rho0: Reference density [kg/m³]. Default 1.0 (lattice units).
    """

    def __init__(
        self,
        nx: int,
        ny: int,
        nz: int,
        dx: float = 0.01,
        nu: float = 0.1,
        rho0: float = 1.0,
    ):
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.dx = dx
        self.rho0 = rho0

        # Lattice speed: cs² = 1/3 in lattice units
        self.cs2 = 1.0 / 3.0

        # dt in lattice units = dx (for unit lattice speed)
        self.dt_lbm = dx

        # Relaxation parameter from viscosity:
        # ν = cs² (τ - 0.5) dt
        # τ = ν / (cs² dt) + 0.5
        self.tau = nu / (self.cs2 * self.dt_lbm) + 0.5
        self.omega = 1.0 / self.tau  # BGK relaxation rate

        # Distribution functions: f[Q, nx, ny, nz]
        self.f = np.zeros((Q, nx, ny, nz))
        self.f_temp = np.zeros_like(self.f)

        # Initialize to equilibrium at rest with uniform density
        for i in range(Q):
            self.f[i] = _W[i] * rho0

        # Macroscopic fields
        self.rho = np.full((nx, ny, nz), rho0)
        self.ux = np.zeros((nx, ny, nz))
        self.uy = np.zeros((nx, ny, nz))
        self.uz = np.zeros((nx, ny, nz))

        # Body force (from FDTD ponderomotive force)
        self.Fx = np.zeros((nx, ny, nz))
        self.Fy = np.zeros((nx, ny, nz))
        self.Fz = np.zeros((nx, ny, nz))

        # Solid mask (True = solid wall, bounce-back)
        self.solid = np.zeros((nx, ny, nz), dtype=bool)

        # Diagnostics
        self.timestep = 0

    def set_body_force(self, Fx, Fy, Fz):
        """Set the body force arrays (e.g. from FDTD ponderomotive force)."""
        self.Fx[:] = Fx
        self.Fy[:] = Fy
        self.Fz[:] = Fz

    def _compute_macroscopic(self):
        """Compute density and velocity from distribution functions."""
        self.rho = np.sum(self.f, axis=0)
        inv_rho = 1.0 / self.rho

        self.ux = np.sum(self.f * _E[:, 0].reshape(-1, 1, 1, 1), axis=0) * inv_rho
        self.uy = np.sum(self.f * _E[:, 1].reshape(-1, 1, 1, 1), axis=0) * inv_rho
        self.uz = np.sum(self.f * _E[:, 2].reshape(-1, 1, 1, 1), axis=0) * inv_rho

        # Add body force contribution to velocity (Guo forcing)
        self.ux += 0.5 * self.Fx * inv_rho * self.dt_lbm
        self.uy += 0.5 * self.Fy * inv_rho * self.dt_lbm
        self.uz += 0.5 * self.Fz * inv_rho * self.dt_lbm

    def _equilibrium(self, i, rho, ux, uy, uz):
        """Compute equilibrium distribution for direction i."""
        eu = _E[i, 0] * ux + _E[i, 1] * uy + _E[i, 2] * uz
        u_sq = ux**2 + uy**2 + uz**2
        return _W[i] * rho * (1.0 + eu / self.cs2 + 0.5 * eu**2 / self.cs2**2 - 0.5 * u_sq / self.cs2)

    def _collide(self):
        """BGK collision with Guo body force."""
        self._compute_macroscopic()

        for i in range(Q):
            f_eq = self._equilibrium(i, self.rho, self.ux, self.uy, self.uz)

            # Guo forcing term
            eu = _E[i, 0] * self.ux + _E[i, 1] * self.uy + _E[i, 2] * self.uz
            eF = _E[i, 0] * self.Fx + _E[i, 1] * self.Fy + _E[i, 2] * self.Fz
            uF = self.ux * self.Fx + self.uy * self.Fy + self.uz * self.Fz

            Si = (1.0 - 0.5 * self.omega) * _W[i] * ((eF - uF) / self.cs2 + eu * eF / self.cs2**2) * self.dt_lbm

            # BGK collision + forcing
            self.f[i] += -self.omega * (self.f[i] - f_eq) + Si

    def _stream(self):
        """Stream distributions to neighboring cells with periodic BCs."""
        for i in range(Q):
            self.f[i] = np.roll(
                np.roll(np.roll(self.f[i], int(_E[i, 0]), axis=0), int(_E[i, 1]), axis=1),
                int(_E[i, 2]),
                axis=2,
            )

    def _bounce_back(self):
        """Apply bounce-back boundary condition on solid nodes."""
        if not np.any(self.solid):
            return
        for i in range(Q):
            # Where the node is solid, swap with opposite direction
            self.f[i][self.solid], self.f[_OPP[i]][self.solid] = (
                self.f[_OPP[i]][self.solid].copy(),
                self.f[i][self.solid].copy(),
            )

    def step(self):
        """Execute one LBM timestep: collide → stream → bounce-back."""
        self._collide()
        self._stream()
        self._bounce_back()
        self.timestep += 1

    def velocity_magnitude(self):
        """Return |u| = √(ux² + uy² + uz²)."""
        return np.sqrt(self.ux**2 + self.uy**2 + self.uz**2)

    def max_velocity(self):
        """Return the maximum velocity magnitude (for CFL monitoring)."""
        return float(np.max(self.velocity_magnitude()))

    def total_momentum(self):
        """Return total momentum vector (should be non-zero under forcing)."""
        px = float(np.sum(self.rho * self.ux) * self.dx**3)
        py = float(np.sum(self.rho * self.uy) * self.dx**3)
        pz = float(np.sum(self.rho * self.uz) * self.dx**3)
        return px, py, pz
