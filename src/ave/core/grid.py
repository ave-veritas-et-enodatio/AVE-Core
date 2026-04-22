from __future__ import annotations
import numpy as np
from .constants import Z_0


class VacuumGrid:
    """
    AVE Unified Python Engine: 'VacuumGrid' Core Object.
    Represents the continuous, mathematically structured LC dielectric vacuum matrix.
    Handles transverse wave propagation (c), characteristic impedance (Z0),
    and LC inductive transmission using FDTD integration.

    Thermal noise model (see Ch. 18, §4 — Fluctuation-Dissipation):
    ---------------------------------------------------------------
    ``thermal_mode='boundary'`` (default, physically correct):
        Noise enters only through the edge nodes, modelling boundary-
        impedance thermalization.  The Nyquist relation ⟨V²⟩ = 4 k_B T Z₀ Δf
        dictates that thermal noise couples into a structure through
        impedance mismatches at its boundaries, not via bulk injection.

    ``thermal_mode='bulk'`` (legacy / special purpose):
        Noise is injected uniformly across all nodes.  Use ONLY for
        simulations where the noise IS the physics (e.g., Casimir ZPF
        flooding, entropy scattering demos).
    """

    def __init__(
        self,
        nx: int,
        ny: int,
        z0: float = Z_0,
        c2: float = 0.25,
        thermal_mode: str = "boundary",
        boundary_width: int = 2,
    ):
        self.nx = nx
        self.ny = ny
        self.z0 = z0  # Vacuum characteristic macroscopic impedance
        self.c2 = c2  # Courant number (wave speed squared, dt/dx ratio)
        self.thermal_mode = thermal_mode  # 'boundary' or 'bulk'
        self.boundary_width = boundary_width  # nodes of thermal coupling depth

        # Primary Macroscopic Field Traces (Transverse Displacement / Inductive Shear)
        # Interpreted as 'Displacement' or 'Strain' in AVE Continuum Mechanics.
        self.strain_z = np.zeros((nx, ny))

        # Temperature (Background thermal RMS array)
        self.temperature = 0.0

    import typing

    def set_temperature(self, t: float, mode: typing.Optional[str] = None):
        """Sets the baseline transverse electromagnetic jitter (Heat).

        Parameters
        ----------
        t : float
            RMS noise amplitude (proportional to temperature).
        mode : str, optional
            Override the thermal injection mode ('boundary' or 'bulk').
            If None, uses the mode set at construction time.
        """
        self.temperature = t
        if mode is not None:
            self.thermal_mode = mode

    def _inject_boundary_noise(self, field: np.ndarray, amp: float):
        """Inject thermal noise only at edge nodes (boundary thermalization)."""
        bw = self.boundary_width
        # Top and bottom strips
        field[:bw, :] += np.random.normal(0, amp, (bw, self.ny))
        field[-bw:, :] += np.random.normal(0, amp, (bw, self.ny))
        # Left and right strips (excluding corners already covered)
        field[bw:-bw, :bw] += np.random.normal(0, amp, (self.nx - 2 * bw, bw))
        field[bw:-bw, -bw:] += np.random.normal(0, amp, (self.nx - 2 * bw, bw))

    def _inject_bulk_noise(self, field: np.ndarray, amp: float):
        """Inject thermal noise uniformly across all nodes (legacy mode)."""
        field += np.random.normal(0, amp, (self.nx, self.ny))

    def step_kinematic_wave_equation(self, damping: float = 0.99):
        """Standard Cartesian mechanical wave-equation integration (Laplacian)."""
        new_strain = np.copy(self.strain_z)

        # Apply thermal noise according to selected mode
        if self.temperature > 0.0:
            amp = self.temperature * 0.1
            if self.thermal_mode == "boundary":
                self._inject_boundary_noise(new_strain, amp)
            else:
                self._inject_bulk_noise(new_strain, amp)

        # Fast vector Laplacian (excluding boundaries)
        laplacian = (
            self.strain_z[2:, 1:-1]
            + self.strain_z[:-2, 1:-1]
            + self.strain_z[1:-1, 2:]
            + self.strain_z[1:-1, :-2]
            - 4 * self.strain_z[1:-1, 1:-1]
        )

        new_strain[1:-1, 1:-1] = self.strain_z[1:-1, 1:-1] + self.c2 * laplacian
        new_strain *= damping  # Geometric radiation loss

        # Fixed borders
        new_strain[0, :] = 0
        new_strain[-1, :] = 0
        new_strain[:, 0] = 0
        new_strain[:, -1] = 0

        self.strain_z = new_strain

    def get_local_strain(self, x: int, y: int) -> float:
        """Reads the local FDTD impedance strain at a grid coordinate."""
        if 0 <= x < self.nx and 0 <= y < self.ny:
            return self.strain_z[x, y]
        return 0.0

    def inject_strain(self, x: int, y: int, value: float):
        """Pumps transverse energy directly into the LC matrix."""
        if 0 < x < self.nx - 1 and 0 < y < self.ny - 1:
            self.strain_z[x, y] += value
