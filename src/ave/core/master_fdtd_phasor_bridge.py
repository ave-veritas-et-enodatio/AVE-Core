"""
Master Equation FDTD → K4 phasor projection bridge
==================================================

Projects the scalar Master Equation field ``V`` (and ``V_prev``) onto the
substrate-native K4 four-port bond phasor basis so bound-state dynamics and
``V_inc`` / ``V_ref`` / ``Phi_link`` / ``z_local`` diagnostics can be read from
the *same* dynamical object.

This is an observer bridge, not a new dynamics engine. The Master Equation
leapfrog step is unchanged; after each step the continuum field is decomposed
per bond using the TLM traveling-wave split at Z₀ = 1:

    V_phys = ½(V_here + V_neighbor)
    I_phys = (V_neighbor − V_here) / (2·dx)
    V_inc  = ½(V_phys + Z₀·I_phys)
    V_ref  = ½(V_phys − Z₀·I_phys)

``Phi_link`` accumulates ``V_phys · dt`` on directed A→B bonds (K4 convention).
``z_local`` uses the Master Equation saturation kernel S(A) with A = |V|/V_yield.
"""

from __future__ import annotations

import numpy as np

from ave.core.k4_tlm import build_scattering_matrix


PORT_SHIFTS = np.array(
    [
        [1, 1, 1],
        [1, -1, -1],
        [-1, 1, -1],
        [-1, -1, 1],
    ],
    dtype=int,
)


class MasterFDTDPhasorBridge:
    """Read-only projection of MasterEquationFDTD scalar state to K4 observables."""

    def __init__(self, nx: int, ny: int, nz: int, dx: float, V_yield: float, dt: float):
        self.nx = int(nx)
        self.ny = int(ny)
        self.nz = int(nz)
        self.dx = float(dx)
        self.V_yield = float(V_yield)
        self.dt = float(dt)

        i, j, k = np.indices((self.nx, self.ny, self.nz))
        self.mask_A = (i % 2 == 0) & (j % 2 == 0) & (k % 2 == 0)
        self.mask_B = (i % 2 == 1) & (j % 2 == 1) & (k % 2 == 1)
        self.mask_active = self.mask_A | self.mask_B

        self.V_inc = np.zeros((self.nx, self.ny, self.nz, 4), dtype=float)
        self.V_ref = np.zeros((self.nx, self.ny, self.nz, 4), dtype=float)
        self.Phi_link = np.zeros((self.nx, self.ny, self.nz, 4), dtype=float)
        self.z_local_field = np.ones((self.nx, self.ny, self.nz), dtype=float)
        self.S_field = np.ones((self.nx, self.ny, self.nz), dtype=float)

    def reset_phi_link(self) -> None:
        self.Phi_link.fill(0.0)

    def saturation_kernel(self, V: np.ndarray, S_min: float = 0.05, *, A_cap: float | None = 0.99) -> np.ndarray:
        A = np.abs(V) / self.V_yield
        if A_cap is not None:
            A = np.minimum(A, A_cap)
        return np.sqrt(np.maximum(1.0 - A**2, S_min**2))

    def project_from_scalar(
        self,
        V: np.ndarray,
        V_prev: np.ndarray | None = None,
        *,
        accumulate_phi: bool = True,
        S_min: float = 0.05,
    ) -> None:
        """Project scalar ``V`` onto four-port phasors and optional ``Phi_link``."""
        z0 = 1.0
        V_inc = np.zeros_like(self.V_inc)
        V_ref = np.zeros_like(self.V_ref)

        for port, shift in enumerate(PORT_SHIFTS):
            V_nb = np.roll(V, shift=shift, axis=(0, 1, 2))
            V_phys = 0.5 * (V + V_nb)
            I_phys = (V_nb - V) / (2.0 * self.dx)
            V_inc[..., port] = 0.5 * (V_phys + z0 * I_phys)
            V_ref[..., port] = 0.5 * (V_phys - z0 * I_phys)

            if accumulate_phi:
                V_avg = V_phys
                self.Phi_link[self.mask_A, port] += V_avg[self.mask_A] * self.dt

        inactive = ~self.mask_active
        V_inc[inactive] = 0.0
        V_ref[inactive] = 0.0

        self.V_inc = V_inc
        self.V_ref = V_ref

        S = self.saturation_kernel(V, S_min=S_min)
        self.S_field = S
        self.z_local_field = 1.0 / np.sqrt(np.maximum(S, S_min))
        self.z_local_field[~self.mask_active] = 1.0

        if V_prev is not None:
            # Optional reactive channel: time-derivative contributes to port-0
            # quadrature for C/L exchange diagnostics (does not alter dynamics).
            V_dot = (V - V_prev) / max(self.dt, 1e-30)
            reactive = 0.25 * V_dot
            self.V_inc[..., 0] += reactive
            self.V_ref[..., 2] += reactive

    def scatter_projected(self) -> None:
        """Apply the K4 junction scatter to projected phasors (observer-only)."""
        S_field = np.zeros((self.nx, self.ny, self.nz, 4, 4), dtype=float)
        for idx in np.ndindex(self.nx, self.ny, self.nz):
            if not self.mask_active[idx]:
                continue
            S_field[idx] = build_scattering_matrix(float(self.z_local_field[idx]))
        self.V_ref = np.einsum("...ij,...j->...i", S_field, self.V_inc)
        self.V_ref[~self.mask_active] = 0.0

    def bond_gamma_at(self, center: tuple[int, int, int], port: int = 0) -> float | None:
        """Op3 bond reflection coefficient at a site for diagnostics."""
        x, y, z = center
        if not self.mask_active[x, y, z]:
            return None
        shift = tuple(-int(s) for s in PORT_SHIFTS[port])
        xb, yb, zb = (x + shift[0]) % self.nx, (y + shift[1]) % self.ny, (z + shift[2]) % self.nz
        z_a = float(self.z_local_field[x, y, z])
        z_b = float(self.z_local_field[xb, yb, zb])
        denom = z_b + z_a
        if abs(denom) < 1e-15:
            return None
        return float((z_b - z_a) / denom)

    def bond_gamma_field(self) -> np.ndarray:
        """Per-site minimum bond Γ across the four tetrahedral ports."""
        gamma = np.full((self.nx, self.ny, self.nz), np.nan, dtype=float)
        z = self.z_local_field
        for port, shift in enumerate(PORT_SHIFTS):
            z_nb = np.roll(z, shift=shift, axis=(0, 1, 2))
            denom = z_nb + z
            with np.errstate(divide="ignore", invalid="ignore"):
                g = (z_nb - z) / denom
            valid = self.mask_active & (np.abs(denom) > 1e-15)
            update = valid & (np.isnan(gamma) | (g < gamma))
            gamma[update] = g[update]
        return gamma

    def bond_gamma_min_in_shell(
        self,
        V: np.ndarray,
        *,
        threshold_frac: float = 0.1,
        center: tuple[int, int, int] | None = None,
        radius: int | None = None,
        A_cap: float | None = 0.99,
        S_min: float = 0.05,
    ) -> float | None:
        """Minimum Γ on bonds where |V| exceeds threshold_frac of the field peak."""
        peak = float(np.max(np.abs(V[self.mask_active]))) if self.mask_active.any() else 0.0
        if peak <= 1e-15:
            return None
        shell = (np.abs(V) >= threshold_frac * peak) & self.mask_active
        if center is not None and radius is not None:
            cx, cy, cz = center
            i, j, k = np.indices((self.nx, self.ny, self.nz))
            r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2)
            shell &= r <= radius
        S = self.saturation_kernel(V, S_min=S_min, A_cap=A_cap)
        z = 1.0 / np.sqrt(np.maximum(S, S_min))
        z[~self.mask_active] = 1.0
        gamma = np.full((self.nx, self.ny, self.nz), np.nan, dtype=float)
        for shift in PORT_SHIFTS:
            z_nb = np.roll(z, shift=shift, axis=(0, 1, 2))
            denom = z_nb + z
            with np.errstate(divide="ignore", invalid="ignore"):
                g = (z_nb - z) / denom
            valid = self.mask_active & (np.abs(denom) > 1e-15)
            update = valid & (np.isnan(gamma) | (g < gamma))
            gamma[update] = g[update]
        vals = gamma[shell]
        vals = vals[np.isfinite(vals)]
        if len(vals) == 0:
            return None
        return float(np.min(vals))

    def total_phasor_energy(self) -> float:
        return float(np.sum(self.V_inc**2 + self.V_ref**2))
