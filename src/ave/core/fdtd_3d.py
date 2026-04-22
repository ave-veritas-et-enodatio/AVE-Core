"""
3D Finite-Difference Time-Domain (FDTD) Maxwell Solver Engine
=============================================================

Non-Linear AVE Solver implementing dual Axiom 4 saturation (ε + μ).

This module provides a rigorous, time-evolved 3D Maxwell equation solver
utilizing the standard Yee-cell grid architecture. The electric field update
uses a spatially and temporally varying permittivity:

    ε_eff(V) = ε₀ · √(1 − (V/V_yield)²)

This non-linearity causes the solver to:
  - Recover linear Maxwell exactly when E << E_crit (most of space)
  - Slow local phase velocity near strong fields (dielectric drag → mass)
  - Diverge the update coefficient near saturation (energy trapping)
  - Support both linear_only=True mode (for benchmarking) and full non-linear

Includes 1st-order Mur Absorbing Boundary Conditions (ABCs).
"""

import numpy as np

from ave.axioms.scale_invariant import saturation_factor
from ave.core.constants import B_SNAP, C_0, EPSILON_0, MU_0, V_YIELD


class FDTD3DEngine:
    """
    3D FDTD Maxwell solver with optional Axiom 4 non-linear vacuum.

    Args:
        nx, ny, nz: Grid dimensions.
        dx: Cell size [m]. This is a COMPUTATIONAL grid parameter, not the
            physical lattice pitch ℓ_node. The physics enters solely through
            V_yield and B_yield (the dielectric/magnetic saturation thresholds
            from Axiom 4). dx controls numerical resolution; results converge
            as dx → 0 with fixed V_yield.
        linear_only: If True, uses constant ε₀ (standard Maxwell). Default False.
        v_yield: Dielectric yield voltage per cell [V]. Default is V_YIELD = √α × V_SNAP
                 ≈ 43.65 kV — the macroscopic onset of Axiom 4 nonlinearity.
                 Use V_SNAP (≈ 511 kV) only for subatomic/topological simulations.
        b_yield: Magnetic saturation field [T]. Default is B_SNAP.
        eps_r: Optional 3D array of relative permittivity (default 1.0 = vacuum).
        mu_r: Optional 3D array of relative permeability (default 1.0 = vacuum).
    """

    def __init__(
        self,
        nx: int,
        ny: int,
        nz: int,
        dx: float = 0.01,
        linear_only: bool = False,
        v_yield: float = V_YIELD,
        b_yield: float = B_SNAP,
        use_pml: bool = False,
        pml_layers: int = 8,
    ) -> None:
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.dx = dx
        self.linear_only = linear_only
        self.v_yield = v_yield
        self.b_yield = b_yield
        self.use_pml = use_pml
        self.pml_layers = pml_layers

        # Physical Constants
        self.c = float(C_0)
        self.mu_0 = float(MU_0)
        self.epsilon_0 = float(EPSILON_0)

        # CFL Condition for 3D stability: dt <= dx / (c * √3)
        # Inject 0.80 stability buffer against Axiom 4 varactor steepening.
        self.dt = (self.dx / (self.c * np.sqrt(3.0))) * 0.80

        # Core Field Matrices (E and H vectors)
        self.Ex = np.zeros((nx, ny, nz))
        self.Ey = np.zeros((nx, ny, nz))
        self.Ez = np.zeros((nx, ny, nz))

        self.Hx = np.zeros((nx, ny, nz))
        self.Hy = np.zeros((nx, ny, nz))
        self.Hz = np.zeros((nx, ny, nz))

        # Spatial material maps (relative permittivity and permeability)
        # Default: vacuum everywhere (eps_r = mu_r = 1.0)
        # Users can assign material regions directly: engine.eps_r[10:20, ...] = 3000
        # Or use the convenience method: engine.set_material_region(...)
        self.eps_r = np.ones((nx, ny, nz))
        self.mu_r = np.ones((nx, ny, nz))

        # Magnetic update coefficient
        # In linear mode: constant  ch = dt / (μ₀ · dx)
        # In nonlinear mode: per-cell via _compute_ch(H)
        self.ch_linear = self.dt / (self.mu_0 * self.dx)

        # Linear electric update coefficient (used when linear_only=True)
        self.ce_linear = self.dt / (self.epsilon_0 * self.dx)

        # Mur 1st-Order ABC coefficient (fallback when PML disabled)
        abc_coef = (self.c * self.dt - self.dx) / (self.c * self.dt + self.dx)
        self.abc_coef = abc_coef

        # ABC boundary memory vectors
        self.ex_y0 = np.zeros((nx, nz))
        self.ex_yn = np.zeros((nx, nz))
        self.ex_z0 = np.zeros((nx, ny))
        self.ex_zn = np.zeros((nx, ny))

        self.ey_x0 = np.zeros((ny, nz))
        self.ey_xn = np.zeros((ny, nz))
        self.ey_z0 = np.zeros((nx, ny))
        self.ey_zn = np.zeros((nx, ny))

        self.ez_x0 = np.zeros((ny, nz))
        self.ez_xn = np.zeros((ny, nz))
        self.ez_y0 = np.zeros((nx, nz))
        self.ez_yn = np.zeros((nx, nz))

        # --- CPML Initialization ---
        if self.use_pml:
            self._init_cpml()

        # Diagnostics
        self.timestep = 0
        self.max_strain_ratio = 0.0  # Track peak |E·dx / V_yield|
        self.max_mag_strain = 0.0  # Track peak |B / B_yield|

    def set_material_region(self, slices: tuple, eps_r: float | None = None, mu_r: float | None = None) -> None:
        """
        Set material properties in a spatial region.

        Convenience method for assigning dielectric/magnetic properties.
        Equivalent to engine.eps_r[slices] = value.

        Args:
            slices: Tuple of slices defining the region,
                    e.g. (slice(10,20), slice(15,25), slice(None))
            eps_r: Relative permittivity for the region (e.g., 3000 for BaTiO₃).
            mu_r: Relative permeability for the region.
        """
        if eps_r is not None:
            self.eps_r[slices] = eps_r
        if mu_r is not None:
            self.mu_r[slices] = mu_r

    def _init_cpml(self) -> None:
        """Initialize CPML conductivity profiles and ψ accumulator arrays."""
        d = self.pml_layers
        # Optimal conductivity: σ_max = (m+1) / (150π·dx) for polynomial order m
        m = 3  # cubic grading
        sigma_max = (m + 1) / (150.0 * np.pi * self.dx)

        # Build 1D conductivity profiles for each axis
        # The profile ramps from 0 at the PML inner edge to σ_max at the boundary
        def _build_sigma(n_cells: int, n_pml: int) -> np.ndarray:
            sigma = np.zeros(n_cells)
            for i in range(n_pml):
                val = sigma_max * ((n_pml - i) / n_pml) ** m
                sigma[i] = val  # low boundary
                sigma[-(i + 1)] = val  # high boundary
            return sigma

        self.sigma_x = _build_sigma(self.nx, d)
        self.sigma_y = _build_sigma(self.ny, d)
        self.sigma_z = _build_sigma(self.nz, d)

        # CPML decay coefficients: b = exp(-σ·dt/ε₀), a = (b-1)·σ/(σ+κ) simplified
        def _cpml_coeffs(sigma_1d: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
            b = np.exp(-sigma_1d * self.dt / self.epsilon_0)
            # Avoid divide-by-zero where σ=0
            with np.errstate(divide="ignore", invalid="ignore"):
                a = np.where(sigma_1d > 0, (b - 1.0) * sigma_1d / (sigma_1d * self.dx), 0.0)
            return b, a

        self.bx, self.ax = _cpml_coeffs(self.sigma_x)
        self.by, self.ay = _cpml_coeffs(self.sigma_y)
        self.bz, self.az = _cpml_coeffs(self.sigma_z)

        # NOTE: Full CPML ψ accumulator arrays removed — the current PML
        # implementation uses multiplicative exponential damping (bx/by/bz)
        # which does not require convolution state. If a full convolutional
        # PML is needed in the future, ψ arrays should be allocated as thin
        # boundary slabs of depth pml_layers, not full (nx,ny,nz) grids.

    def _compute_local_epsilon(self, E_component: np.ndarray) -> np.ndarray:
        """
        Compute the local non-linear permittivity per cell per component.

        ε_eff = ε₀ · √(1 − (E·dx / V_yield)²)

        The local voltage across a cell is V_local = E · dx.
        The saturation ratio is V_local / V_yield.

        Returns:
            Per-cell permittivity array (same shape as E_component).
        """
        V_local = np.abs(E_component) * self.dx
        ratio_sq = (V_local / self.v_yield) ** 2

        # Track maximum strain for diagnostics
        max_r = np.max(ratio_sq) if ratio_sq.size > 0 else 0.0
        if max_r > self.max_strain_ratio:
            self.max_strain_ratio = max_r

        # Clip to prevent numerical instability near exact saturation
        # (ratio_sq >= 1.0 would mean dielectric rupture)
        ratio_sq = np.clip(ratio_sq, 0.0, 1.0 - 1e-12)

        # Base permittivity includes material: ε₀ × ε_r
        # Slice eps_r to match the shape of E_component if needed
        if E_component.shape == self.eps_r.shape:
            eps_base = self.epsilon_0 * self.eps_r
        else:
            eps_base = self.epsilon_0  # sub-grid slice, use vacuum

        return eps_base * saturation_factor(V_local, self.v_yield)

    def _compute_local_mu(self, H_component: np.ndarray) -> np.ndarray:
        """
        Compute the local non-linear permeability per cell per component.

        μ_eff = μ₀ · √(1 − (B / B_yield)²)

        where B = μ₀ · |H| (in free space approximation for the iterate).
        When B → B_yield, μ → 0: the inductor saturates (shorts).
        """
        B_local = self.mu_0 * np.abs(H_component)
        ratio_sq = (B_local / self.b_yield) ** 2

        max_r = np.max(ratio_sq) if ratio_sq.size > 0 else 0.0
        if max_r > self.max_mag_strain:
            self.max_mag_strain = max_r

        ratio_sq = np.clip(ratio_sq, 0.0, 1.0 - 1e-12)

        if H_component.shape == self.mu_r.shape:
            mu_base = self.mu_0 * self.mu_r
        else:
            mu_base = self.mu_0

        return mu_base * saturation_factor(B_local, self.b_yield)

    def _compute_ce(self, E_component: np.ndarray) -> np.ndarray | float:
        """
        Compute the electric field update coefficient.

        In linear mode: ce = dt / (ε₀ · dx) — uniform scalar.
        In non-linear mode: ce = dt / (ε_eff(E) · dx) — per-cell array.
        """
        if self.linear_only:
            # In linear mode, still respect spatial material properties
            # Handle sub-grid slices: if E_component is a sub-grid view,
            # eps_r won't match shape, so fall back to scalar vacuum
            if E_component.shape == self.eps_r.shape:
                return self.dt / (self.epsilon_0 * self.eps_r * self.dx)
            else:
                return self.ce_linear

        eps_eff = self._compute_local_epsilon(E_component)
        return self.dt / (eps_eff * self.dx)

    def _compute_ch(self, H_component: np.ndarray) -> np.ndarray | float:
        """
        Compute the magnetic field update coefficient.

        In linear mode: ch = dt / (μ₀ · dx) — uniform scalar.
        In non-linear mode: ch = dt / (μ_eff(H) · dx) — per-cell array.
        """
        if self.linear_only:
            # In linear mode, still respect spatial material properties
            if H_component.shape == self.mu_r.shape:
                return self.dt / (self.mu_0 * self.mu_r * self.dx)
            else:
                return self.ch_linear

        mu_eff = self._compute_local_mu(H_component)
        return self.dt / (mu_eff * self.dx)

    def update_magnetic_field(self) -> None:
        """
        Update H fields from the curl of E (Faraday's Law).

        In non-linear mode, the update coefficient ch is computed PER CELL
        from the local H amplitude, implementing Axiom 4 (magnetic sector):

            H^{n+1} = H^n - (dt / μ_eff(H^n)) · (∇×E) / dx
        """
        # Hx
        curl_e_x = (self.Ez[:, 1:, :-1] - self.Ez[:, :-1, :-1]) - (self.Ey[:, :-1, 1:] - self.Ey[:, :-1, :-1])
        ch_x = self._compute_ch(self.Hx[:, :-1, :-1])
        self.Hx[:, :-1, :-1] -= ch_x * curl_e_x

        # Hy
        curl_e_y = (self.Ex[:-1, :, 1:] - self.Ex[:-1, :, :-1]) - (self.Ez[1:, :, :-1] - self.Ez[:-1, :, :-1])
        ch_y = self._compute_ch(self.Hy[:-1, :, :-1])
        self.Hy[:-1, :, :-1] -= ch_y * curl_e_y

        # Hz
        curl_e_z = (self.Ey[1:, :-1, :] - self.Ey[:-1, :-1, :]) - (self.Ex[:-1, 1:, :] - self.Ex[:-1, :-1, :])
        ch_z = self._compute_ch(self.Hz[:-1, :-1, :])
        self.Hz[:-1, :-1, :] -= ch_z * curl_e_z

    def update_electric_field(self) -> None:
        """
        Update E fields from the curl of H (Ampere's Law).

        In non-linear mode, the update coefficient ce is computed PER CELL
        from the local field amplitude, implementing Axiom 4:

            E^{n+1} = E^n + (dt / ε_eff(E^n)) · (∇×H) / dx
        """
        # --- Ex update ---
        curl_h_x = (self.Hz[:, 1:, 1:] - self.Hz[:, :-1, 1:]) - (self.Hy[:, 1:, 1:] - self.Hy[:, 1:, :-1])
        ce_x = self._compute_ce(self.Ex[:, 1:, 1:])
        self.Ex[:, 1:, 1:] += ce_x * curl_h_x

        # --- Ey update ---
        curl_h_y = (self.Hx[1:, :, 1:] - self.Hx[1:, :, :-1]) - (self.Hz[1:, :, 1:] - self.Hz[:-1, :, 1:])
        ce_y = self._compute_ce(self.Ey[1:, :, 1:])
        self.Ey[1:, :, 1:] += ce_y * curl_h_y

        # --- Ez update ---
        curl_h_z = (self.Hy[1:, 1:, :] - self.Hy[:-1, 1:, :]) - (self.Hx[1:, 1:, :] - self.Hx[1:, :-1, :])
        ce_z = self._compute_ce(self.Ez[1:, 1:, :])
        self.Ez[1:, 1:, :] += ce_z * curl_h_z

    def apply_mur_abc(self) -> None:
        """Apply 1st-Order Mur ABCs to all six faces."""
        c1 = self.abc_coef

        # X-Boundaries
        self.Ey[0, :, :] = self.ey_x0 + c1 * (self.Ey[1, :, :] - self.Ey[0, :, :])
        self.ey_x0[:, :] = self.Ey[1, :, :]
        self.Ez[0, :, :] = self.ez_x0 + c1 * (self.Ez[1, :, :] - self.Ez[0, :, :])
        self.ez_x0[:, :] = self.Ez[1, :, :]
        self.Ey[-1, :, :] = self.ey_xn + c1 * (self.Ey[-2, :, :] - self.Ey[-1, :, :])
        self.ey_xn[:, :] = self.Ey[-2, :, :]
        self.Ez[-1, :, :] = self.ez_xn + c1 * (self.Ez[-2, :, :] - self.Ez[-1, :, :])
        self.ez_xn[:, :] = self.Ez[-2, :, :]

        # Y-Boundaries
        self.Ex[:, 0, :] = self.ex_y0 + c1 * (self.Ex[:, 1, :] - self.Ex[:, 0, :])
        self.ex_y0[:, :] = self.Ex[:, 1, :]
        self.Ez[:, 0, :] = self.ez_y0 + c1 * (self.Ez[:, 1, :] - self.Ez[:, 0, :])
        self.ez_y0[:, :] = self.Ez[:, 1, :]
        self.Ex[:, -1, :] = self.ex_yn + c1 * (self.Ex[:, -2, :] - self.Ex[:, -1, :])
        self.ex_yn[:, :] = self.Ex[:, -2, :]
        self.Ez[:, -1, :] = self.ez_yn + c1 * (self.Ez[:, -2, :] - self.Ez[:, -1, :])
        self.ez_yn[:, :] = self.Ez[:, -2, :]

        # Z-Boundaries
        self.Ex[:, :, 0] = self.ex_z0 + c1 * (self.Ex[:, :, 1] - self.Ex[:, :, 0])
        self.ex_z0[:, :] = self.Ex[:, :, 1]
        self.Ey[:, :, 0] = self.ey_z0 + c1 * (self.Ey[:, :, 1] - self.Ey[:, :, 0])
        self.ey_z0[:, :] = self.Ey[:, :, 1]
        self.Ex[:, :, -1] = self.ex_zn + c1 * (self.Ex[:, :, -2] - self.Ex[:, :, -1])
        self.ex_zn[:, :] = self.Ex[:, :, -2]
        self.Ey[:, :, -1] = self.ey_zn + c1 * (self.Ey[:, :, -2] - self.Ey[:, :, -1])
        self.ey_zn[:, :] = self.Ey[:, :, -2]

    def inject_soft_source(self, field: str, x: int, y: int, z: int, amplitude: float) -> None:
        """Inject a soft source (additive) into a field component at (x, y, z)."""
        if field == "Ex":
            self.Ex[x, y, z] += amplitude
        elif field == "Ey":
            self.Ey[x, y, z] += amplitude
        elif field == "Ez":
            self.Ez[x, y, z] += amplitude

    def total_field_energy(self) -> float:
        """
        Compute total electromagnetic energy in the grid.

        U = Σ (½ε_eff |E|² + ½μ₀ |H|²) · dx³
        """
        E_sq = self.Ex**2 + self.Ey**2 + self.Ez**2
        H_sq = self.Hx**2 + self.Hy**2 + self.Hz**2

        if self.linear_only:
            u_e = 0.5 * self.epsilon_0 * self.eps_r * E_sq
        else:
            # Non-linear permittivity per cell
            E_mag = np.sqrt(E_sq)
            V_local = E_mag * self.dx
            eps_local = self.epsilon_0 * saturation_factor(V_local, self.v_yield)
            u_e = 0.5 * eps_local * E_sq

        if self.linear_only:
            u_m = 0.5 * self.mu_0 * self.mu_r * H_sq
        else:
            H_mag = np.sqrt(H_sq)
            B_local = self.mu_0 * H_mag
            mu_local = self.mu_0 * saturation_factor(B_local, self.b_yield)
            u_m = 0.5 * mu_local * H_sq

        return float(np.sum((u_e + u_m) * self.dx**3))

    def energy_density(self) -> np.ndarray:
        """
        Compute the EM energy density u(x,y,z) per cell [J/m³].

        u = ½ε_eff|E|² + ½μ_eff|H|²

        Uses nonlinear ε and μ when in nonlinear mode.
        """
        E_sq = self.Ex**2 + self.Ey**2 + self.Ez**2
        H_sq = self.Hx**2 + self.Hy**2 + self.Hz**2

        if self.linear_only:
            u_e = 0.5 * self.epsilon_0 * self.eps_r * E_sq
        else:
            E_mag = np.sqrt(E_sq)
            V_local = E_mag * self.dx
            eps_local = self.epsilon_0 * self.eps_r * saturation_factor(V_local, self.v_yield)
            u_e = 0.5 * eps_local * E_sq

        if self.linear_only:
            u_m = 0.5 * self.mu_0 * self.mu_r * H_sq
        else:
            H_mag = np.sqrt(H_sq)
            B_local = self.mu_0 * H_mag
            mu_local = self.mu_0 * self.mu_r * saturation_factor(B_local, self.b_yield)
            u_m = 0.5 * mu_local * H_sq

        return u_e + u_m

    def ponderomotive_force(self) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Compute the ponderomotive force density F = -∇u [N/m³].

        Returns (Fx, Fy, Fz) arrays — the force per unit volume at each cell.
        Positive Fx means force in the +x direction.

        For PONDER-01: net thrust = sum(F) × dx³ over the material region.
        """
        u = self.energy_density()

        # Central differences for gradient (interior cells)
        Fx = np.zeros_like(u)
        Fy = np.zeros_like(u)
        Fz = np.zeros_like(u)

        Fx[1:-1, :, :] = -(u[2:, :, :] - u[:-2, :, :]) / (2 * self.dx)
        Fy[:, 1:-1, :] = -(u[:, 2:, :] - u[:, :-2, :]) / (2 * self.dx)
        Fz[:, :, 1:-1] = -(u[:, :, 2:] - u[:, :, :-2]) / (2 * self.dx)

        return Fx, Fy, Fz

    def apply_pml(self) -> None:
        """
        Apply PML absorbing boundaries using exponential conductivity damping.

        Physically: the PML region is a lossy medium where σ ramps up toward
        the boundary. Fields are damped by exp(-σ·dt/ε₀) per axis per step.
        This is separable — each axis applies its own damping independently.

        The result: outgoing radiation is absorbed with < 0.1% reflection
        for the polynomial-graded conductivity profile.
        """
        # Build 3D damping multipliers from the 1D σ profiles
        # damping = exp(-σ · dt / ε₀) — applied per axis
        dx = self.bx  # bx = exp(-σ_x · dt / ε₀) already computed
        dy = self.by
        dz = self.bz

        # Apply x-axis damping (reshape for broadcasting)
        bx_3d = dx.reshape(-1, 1, 1)
        self.Ex *= bx_3d
        self.Ey *= bx_3d
        self.Ez *= bx_3d
        self.Hx *= bx_3d
        self.Hy *= bx_3d
        self.Hz *= bx_3d

        # Apply y-axis damping
        by_3d = dy.reshape(1, -1, 1)
        self.Ex *= by_3d
        self.Ey *= by_3d
        self.Ez *= by_3d
        self.Hx *= by_3d
        self.Hy *= by_3d
        self.Hz *= by_3d

        # Apply z-axis damping
        bz_3d = dz.reshape(1, 1, -1)
        self.Ex *= bz_3d
        self.Ey *= bz_3d
        self.Ez *= bz_3d
        self.Hx *= bz_3d
        self.Hy *= bz_3d
        self.Hz *= bz_3d

    def step(self) -> None:
        """Execute one complete dt timestep of the Maxwell Yee-cell algorithm."""
        self.update_magnetic_field()
        self.update_electric_field()
        if self.use_pml:
            self.apply_pml()
        else:
            self.apply_mur_abc()
        self.timestep += 1
