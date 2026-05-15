"""
3D FDTD Maxwell Solver — JAX GPU-Accelerated Engine
=====================================================

GPU-accelerated port of fdtd_3d.py.  Every physical equation, axiom-derived
constant, and nonlinear saturation curve is **identical** to the numpy
version.  Only the compute backend changes: numpy → jax.numpy, with JIT
compilation for GPU/TPU execution.

AVE AXIOM COMPLIANCE:
  Axiom 1 (LC Network):  Yee-cell staggered grid ≡ discrete LC lattice
  Axiom 4 (Saturation):  ε_eff = ε₀·√(1−(V/V_yield)²),
                          μ_eff = μ₀·√(1−(B/B_yield)²)
  V_yield = m_e c²/e (dielectric snap voltage — zero free parameters)
  B_yield = m_e c/e  (magnetic saturation field — zero free parameters)

Usage:
  Drop-in replacement for FDTD3DEngine.  Change import:
    from ave.core.fdtd_3d_jax import FDTD3DEngineJAX as FDTD3DEngine
"""

from functools import partial

import jax
import jax.numpy as jnp
import numpy as np
from jax import jit

from ave.core.constants import B_SNAP, C_0, EPSILON_0, MU_0, V_YIELD

# Enable float64 to match numpy precision for numerical equivalence
jax.config.update("jax_enable_x64", True)

# =====================================================================
# Pure-function kernels (JIT-compiled, no side effects)
# =====================================================================


@jit
def _compute_local_epsilon_kernel(
    E_component: jax.Array,
    eps_base: jax.Array,
    dx: float,
    v_yield: float,
) -> jax.Array:
    """
    Axiom 4 — Dielectric saturation (electric sector).

    ε_eff = ε_base · √(1 − (E·dx / V_yield)²)

    The local voltage across a cell is V_local = |E| · dx.
    When V_local → V_yield, the dielectric saturates (ε → 0).
    This is the AVE mechanism for mass generation: trapped energy.

    NOTE: JIT-optimized copy of ``scale_invariant.epsilon_eff()``.
    Canonical source of truth: ``axioms/scale_invariant.py``.
    Inlined here because JAX @jit cannot call non-JAX Python functions.
    """
    V_local = jnp.abs(E_component) * dx
    ratio_sq = (V_local / v_yield) ** 2
    ratio_sq = jnp.clip(ratio_sq, 0.0, 1.0 - 1e-12)
    return eps_base * jnp.sqrt(1.0 - ratio_sq)


@jit
def _compute_local_mu_kernel(
    H_component: jax.Array,
    mu_base: jax.Array,
    mu_0: float,
    b_yield: float,
) -> jax.Array:
    """
    Axiom 4 — Inductive saturation (magnetic sector).

    μ_eff = μ_base · √(1 − (B / B_yield)²)

    where B = μ₀ · |H|.  When B → B_yield, the inductor saturates
    (μ → 0, shorts): the lattice cannot store more magnetic flux.

    NOTE: JIT-optimized copy of ``scale_invariant.mu_eff()``.
    Canonical source of truth: ``axioms/scale_invariant.py``.
    Inlined here because JAX @jit cannot call non-JAX Python functions.
    """
    B_local = mu_0 * jnp.abs(H_component)
    ratio_sq = (B_local / b_yield) ** 2
    ratio_sq = jnp.clip(ratio_sq, 0.0, 1.0 - 1e-12)
    return mu_base * jnp.sqrt(1.0 - ratio_sq)


@partial(jit, static_argnums=(7,))
def _update_fields_step(
    Ex: jax.Array,
    Ey: jax.Array,
    Ez: jax.Array,
    Hx: jax.Array,
    Hy: jax.Array,
    Hz: jax.Array,
    params: dict,
    linear_only: bool,
) -> tuple[jax.Array, jax.Array, jax.Array, jax.Array, jax.Array, jax.Array]:
    """
    One complete Yee-cell timestep: H-update (Faraday) then E-update (Ampere).

    The curl stencils, nonlinear coefficient computation, and field updates
    are fused into a single JIT-compiled kernel for maximum GPU throughput.

    All physics is axiom-derived:
      - Curl stencils = discrete ∇× on the Yee lattice (Axiom 1)
      - ε_eff, μ_eff = Axiom 4 saturation curves
      - dt, dx = CFL-stable discretisation of the LC continuum
    """
    dt = params["dt"]
    dx = params["dx"]
    epsilon_0 = params["epsilon_0"]
    mu_0 = params["mu_0"]
    v_yield = params["v_yield"]
    b_yield = params["b_yield"]
    eps_r = params["eps_r"]
    mu_r = params["mu_r"]

    # ─────────────────────────────────────────────────────────
    # 1. MAGNETIC FIELD UPDATE  (Faraday's Law: ∂H/∂t = -∇×E / μ)
    # ─────────────────────────────────────────────────────────

    # Hx curl: ∂Ez/∂y - ∂Ey/∂z
    curl_e_x = (Ez[:, 1:, :-1] - Ez[:, :-1, :-1]) - (Ey[:, :-1, 1:] - Ey[:, :-1, :-1])
    # Hy curl: ∂Ex/∂z - ∂Ez/∂x
    curl_e_y = (Ex[:-1, :, 1:] - Ex[:-1, :, :-1]) - (Ez[1:, :, :-1] - Ez[:-1, :, :-1])
    # Hz curl: ∂Ey/∂x - ∂Ex/∂y
    curl_e_z = (Ey[1:, :-1, :] - Ey[:-1, :-1, :]) - (Ex[:-1, 1:, :] - Ex[:-1, :-1, :])

    if linear_only:
        ch_x = dt / (mu_0 * mu_r[:, :-1, :-1] * dx)
        ch_y = dt / (mu_0 * mu_r[:-1, :, :-1] * dx)
        ch_z = dt / (mu_0 * mu_r[:-1, :-1, :] * dx)
    else:
        mu_base_x = mu_0 * mu_r[:, :-1, :-1]
        mu_eff_x = _compute_local_mu_kernel(Hx[:, :-1, :-1], mu_base_x, mu_0, b_yield)
        ch_x = dt / (mu_eff_x * dx)

        mu_base_y = mu_0 * mu_r[:-1, :, :-1]
        mu_eff_y = _compute_local_mu_kernel(Hy[:-1, :, :-1], mu_base_y, mu_0, b_yield)
        ch_y = dt / (mu_eff_y * dx)

        mu_base_z = mu_0 * mu_r[:-1, :-1, :]
        mu_eff_z = _compute_local_mu_kernel(Hz[:-1, :-1, :], mu_base_z, mu_0, b_yield)
        ch_z = dt / (mu_eff_z * dx)

    Hx = Hx.at[:, :-1, :-1].add(-ch_x * curl_e_x)
    Hy = Hy.at[:-1, :, :-1].add(-ch_y * curl_e_y)
    Hz = Hz.at[:-1, :-1, :].add(-ch_z * curl_e_z)

    # ─────────────────────────────────────────────────────────
    # 2. ELECTRIC FIELD UPDATE  (Ampere's Law: ∂E/∂t = +∇×H / ε)
    # ─────────────────────────────────────────────────────────

    # Ex curl: ∂Hz/∂y - ∂Hy/∂z
    curl_h_x = (Hz[:, 1:, 1:] - Hz[:, :-1, 1:]) - (Hy[:, 1:, 1:] - Hy[:, 1:, :-1])
    # Ey curl: ∂Hx/∂z - ∂Hz/∂x
    curl_h_y = (Hx[1:, :, 1:] - Hx[1:, :, :-1]) - (Hz[1:, :, 1:] - Hz[:-1, :, 1:])
    # Ez curl: ∂Hy/∂x - ∂Hx/∂y
    curl_h_z = (Hy[1:, 1:, :] - Hy[:-1, 1:, :]) - (Hx[1:, 1:, :] - Hx[1:, :-1, :])

    if linear_only:
        ce_x = dt / (epsilon_0 * eps_r[:, 1:, 1:] * dx)
        ce_y = dt / (epsilon_0 * eps_r[1:, :, 1:] * dx)
        ce_z = dt / (epsilon_0 * eps_r[1:, 1:, :] * dx)
    else:
        eps_base_x = epsilon_0 * eps_r[:, 1:, 1:]
        eps_eff_x = _compute_local_epsilon_kernel(Ex[:, 1:, 1:], eps_base_x, dx, v_yield)
        ce_x = dt / (eps_eff_x * dx)

        eps_base_y = epsilon_0 * eps_r[1:, :, 1:]
        eps_eff_y = _compute_local_epsilon_kernel(Ey[1:, :, 1:], eps_base_y, dx, v_yield)
        ce_y = dt / (eps_eff_y * dx)

        eps_base_z = epsilon_0 * eps_r[1:, 1:, :]
        eps_eff_z = _compute_local_epsilon_kernel(Ez[1:, 1:, :], eps_base_z, dx, v_yield)
        ce_z = dt / (eps_eff_z * dx)

    Ex = Ex.at[:, 1:, 1:].add(ce_x * curl_h_x)
    Ey = Ey.at[1:, :, 1:].add(ce_y * curl_h_y)
    Ez = Ez.at[1:, 1:, :].add(ce_z * curl_h_z)

    return Ex, Ey, Ez, Hx, Hy, Hz


@jit
def _apply_mur_abc_jax(
    Ex: jax.Array,
    Ey: jax.Array,
    Ez: jax.Array,
    abc_coef: float,
    ex_y0: jax.Array,
    ex_yn: jax.Array,
    ex_z0: jax.Array,
    ex_zn: jax.Array,
    ey_x0: jax.Array,
    ey_xn: jax.Array,
    ey_z0: jax.Array,
    ey_zn: jax.Array,
    ez_x0: jax.Array,
    ez_xn: jax.Array,
    ez_y0: jax.Array,
    ez_yn: jax.Array,
) -> tuple[jax.Array, jax.Array, jax.Array, tuple]:
    """
    1st-Order Mur Absorbing Boundary Conditions on all six faces.

    The Mur ABC coefficient is derived from the CFL condition:
      c_abc = (c·dt − dx) / (c·dt + dx)
    This ensures outgoing waves are absorbed at the boundary.
    """
    c1 = abc_coef

    # --- X-Boundaries ---
    Ey = Ey.at[0, :, :].set(ey_x0 + c1 * (Ey[1, :, :] - Ey[0, :, :]))
    new_ey_x0 = Ey[1, :, :]
    Ez = Ez.at[0, :, :].set(ez_x0 + c1 * (Ez[1, :, :] - Ez[0, :, :]))
    new_ez_x0 = Ez[1, :, :]
    Ey = Ey.at[-1, :, :].set(ey_xn + c1 * (Ey[-2, :, :] - Ey[-1, :, :]))
    new_ey_xn = Ey[-2, :, :]
    Ez = Ez.at[-1, :, :].set(ez_xn + c1 * (Ez[-2, :, :] - Ez[-1, :, :]))
    new_ez_xn = Ez[-2, :, :]

    # --- Y-Boundaries ---
    Ex = Ex.at[:, 0, :].set(ex_y0 + c1 * (Ex[:, 1, :] - Ex[:, 0, :]))
    new_ex_y0 = Ex[:, 1, :]
    Ez = Ez.at[:, 0, :].set(ez_y0 + c1 * (Ez[:, 1, :] - Ez[:, 0, :]))
    new_ez_y0 = Ez[:, 1, :]
    Ex = Ex.at[:, -1, :].set(ex_yn + c1 * (Ex[:, -2, :] - Ex[:, -1, :]))
    new_ex_yn = Ex[:, -2, :]
    Ez = Ez.at[:, -1, :].set(ez_yn + c1 * (Ez[:, -2, :] - Ez[:, -1, :]))
    new_ez_yn = Ez[:, -2, :]

    # --- Z-Boundaries ---
    Ex = Ex.at[:, :, 0].set(ex_z0 + c1 * (Ex[:, :, 1] - Ex[:, :, 0]))
    new_ex_z0 = Ex[:, :, 1]
    Ey = Ey.at[:, :, 0].set(ey_z0 + c1 * (Ey[:, :, 1] - Ey[:, :, 0]))
    new_ey_z0 = Ey[:, :, 1]
    Ex = Ex.at[:, :, -1].set(ex_zn + c1 * (Ex[:, :, -2] - Ex[:, :, -1]))
    new_ex_zn = Ex[:, :, -2]
    Ey = Ey.at[:, :, -1].set(ey_zn + c1 * (Ey[:, :, -2] - Ey[:, :, -1]))
    new_ey_zn = Ey[:, :, -2]

    abc_mem = (
        new_ex_y0,
        new_ex_yn,
        new_ex_z0,
        new_ex_zn,
        new_ey_x0,
        new_ey_xn,
        new_ey_z0,
        new_ey_zn,
        new_ez_x0,
        new_ez_xn,
        new_ez_y0,
        new_ez_yn,
    )

    return Ex, Ey, Ez, abc_mem


@jit
def _apply_pml_jax(
    Ex: jax.Array,
    Ey: jax.Array,
    Ez: jax.Array,
    Hx: jax.Array,
    Hy: jax.Array,
    Hz: jax.Array,
    bx: jax.Array,
    by: jax.Array,
    bz: jax.Array,
) -> tuple[jax.Array, jax.Array, jax.Array, jax.Array, jax.Array, jax.Array]:
    """
    PML absorbing boundaries using exponential conductivity damping.

    bx/by/bz = exp(−σ·dt/ε₀) along each axis, pre-computed from the
    polynomial-graded conductivity profile:
      σ(d) = σ_max · (d/d_pml)^m,  m = 3 (cubic grading)
      σ_max = (m+1) / (150π·dx)

    Applied separably per axis — each axis damps independently.
    """
    bx_3d = bx.reshape(-1, 1, 1)
    by_3d = by.reshape(1, -1, 1)
    bz_3d = bz.reshape(1, 1, -1)

    # X-axis damping
    Ex = Ex * bx_3d
    Ey = Ey * bx_3d
    Ez = Ez * bx_3d
    Hx = Hx * bx_3d
    Hy = Hy * bx_3d
    Hz = Hz * bx_3d

    # Y-axis damping
    Ex = Ex * by_3d
    Ey = Ey * by_3d
    Ez = Ez * by_3d
    Hx = Hx * by_3d
    Hy = Hy * by_3d
    Hz = Hz * by_3d

    # Z-axis damping
    Ex = Ex * bz_3d
    Ey = Ey * bz_3d
    Ez = Ez * bz_3d
    Hx = Hx * bz_3d
    Hy = Hy * bz_3d
    Hz = Hz * bz_3d

    return Ex, Ey, Ez, Hx, Hy, Hz


@partial(jit, static_argnums=(7,))
def _total_field_energy_jax(
    Ex: jax.Array,
    Ey: jax.Array,
    Ez: jax.Array,
    Hx: jax.Array,
    Hy: jax.Array,
    Hz: jax.Array,
    params: dict,
    linear_only: bool,
) -> jax.Array:
    """
    Total electromagnetic energy in the grid:

    U = Σ (½ε_eff|E|² + ½μ_eff|H|²) · dx³

    Uses Axiom 4 nonlinear ε/μ when in nonlinear mode.
    """
    dx = params["dx"]
    epsilon_0 = params["epsilon_0"]
    mu_0 = params["mu_0"]
    v_yield = params["v_yield"]
    b_yield = params["b_yield"]
    eps_r = params["eps_r"]
    mu_r = params["mu_r"]

    E_sq = Ex**2 + Ey**2 + Ez**2
    H_sq = Hx**2 + Hy**2 + Hz**2

    if linear_only:
        u_e = 0.5 * epsilon_0 * eps_r * E_sq
        u_m = 0.5 * mu_0 * mu_r * H_sq
    else:
        # Electric sector
        E_mag = jnp.sqrt(E_sq)
        V_local = E_mag * dx
        ratio_sq = jnp.clip((V_local / v_yield) ** 2, 0.0, 1.0 - 1e-12)
        eps_local = epsilon_0 * eps_r * jnp.sqrt(1.0 - ratio_sq)
        u_e = 0.5 * eps_local * E_sq

        # Magnetic sector
        H_mag = jnp.sqrt(H_sq)
        B_local = mu_0 * H_mag
        mag_ratio_sq = jnp.clip((B_local / b_yield) ** 2, 0.0, 1.0 - 1e-12)
        mu_local = mu_0 * mu_r * jnp.sqrt(1.0 - mag_ratio_sq)
        u_m = 0.5 * mu_local * H_sq

    return jnp.sum((u_e + u_m) * dx**3)


@partial(jit, static_argnums=(7,))
def _energy_density_jax(
    Ex: jax.Array,
    Ey: jax.Array,
    Ez: jax.Array,
    Hx: jax.Array,
    Hy: jax.Array,
    Hz: jax.Array,
    params: dict,
    linear_only: bool,
) -> jax.Array:
    """
    EM energy density u(x,y,z) per cell [J/m³].

    u = ½ε_eff|E|² + ½μ_eff|H|²

    Axiom 4 nonlinear ε/μ used when in nonlinear mode.
    """
    dx = params["dx"]
    epsilon_0 = params["epsilon_0"]
    mu_0 = params["mu_0"]
    v_yield = params["v_yield"]
    b_yield = params["b_yield"]
    eps_r = params["eps_r"]
    mu_r = params["mu_r"]

    E_sq = Ex**2 + Ey**2 + Ez**2
    H_sq = Hx**2 + Hy**2 + Hz**2

    if linear_only:
        u_e = 0.5 * epsilon_0 * eps_r * E_sq
        u_m = 0.5 * mu_0 * mu_r * H_sq
    else:
        E_mag = jnp.sqrt(E_sq)
        V_local = E_mag * dx
        ratio_sq = jnp.clip((V_local / v_yield) ** 2, 0.0, 1.0 - 1e-12)
        eps_local = epsilon_0 * eps_r * jnp.sqrt(1.0 - ratio_sq)
        u_e = 0.5 * eps_local * E_sq

        H_mag = jnp.sqrt(H_sq)
        B_local = mu_0 * H_mag
        mag_ratio_sq = jnp.clip((B_local / b_yield) ** 2, 0.0, 1.0 - 1e-12)
        mu_local = mu_0 * mu_r * jnp.sqrt(1.0 - mag_ratio_sq)
        u_m = 0.5 * mu_local * H_sq

    return u_e + u_m


# =====================================================================
# Engine Class (stateful wrapper around JIT-compiled kernels)
# =====================================================================


class FDTD3DEngineJAX:
    """
    3D FDTD Maxwell solver with optional Axiom 4 non-linear vacuum.
    JAX GPU-accelerated — drop-in replacement for FDTD3DEngine.

    Args:
        nx, ny, nz: Grid dimensions.
        dx: Cell size [m].
        linear_only: If True, uses constant ε₀ (standard Maxwell). Default False.
        v_yield: Dielectric yield voltage per cell [V]. Default is V_YIELD = √α × V_SNAP
                 ≈ 43.65 kV — the macroscopic onset of Axiom 4 nonlinearity.
                 Use V_SNAP (≈ 511 kV) only for subatomic/topological simulations.
        b_yield: Magnetic saturation field [T]. Default is B_SNAP.
        use_pml: If True, uses PML absorbing boundaries. Default False.
        pml_layers: Number of PML damping layers per face. Default 8.
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

        # Physical Constants (from AVE axioms — zero free parameters)
        self.c = float(C_0)
        self.mu_0 = float(MU_0)
        self.epsilon_0 = float(EPSILON_0)

        # CFL Condition for 3D stability: dt ≤ dx / (c_max · √3).
        # We inject an explicit 0.80 stability buffer because as the lattice saturates (Axiom 4),
        # eps_eff drops toward zero causing c_local to rapidly increase. Without this buffer,
        # the engine immediately diverges when driven near V_yield.
        self.dt = (self.dx / (self.c * np.sqrt(3.0))) * 0.80

        # Core Field Arrays (JAX device arrays)
        self.Ex = jnp.zeros((nx, ny, nz))
        self.Ey = jnp.zeros((nx, ny, nz))
        self.Ez = jnp.zeros((nx, ny, nz))

        self.Hx = jnp.zeros((nx, ny, nz))
        self.Hy = jnp.zeros((nx, ny, nz))
        self.Hz = jnp.zeros((nx, ny, nz))

        # Spatial material maps (relative permittivity and permeability)
        # Default: vacuum everywhere (eps_r = mu_r = 1.0)
        # Kept as numpy arrays for consumer mutability (e.g. eng.eps_r[...] = val)
        self.eps_r = np.ones((nx, ny, nz))
        self.mu_r = np.ones((nx, ny, nz))

        # Pre-computed linear coefficients
        self.ch_linear = self.dt / (self.mu_0 * self.dx)
        self.ce_linear = self.dt / (self.epsilon_0 * self.dx)

        # Mur 1st-Order ABC coefficient
        abc_coef = (self.c * self.dt - self.dx) / (self.c * self.dt + self.dx)
        self.abc_coef = abc_coef

        # ABC boundary memory (JAX arrays)
        self.ex_y0 = jnp.zeros((nx, nz))
        self.ex_yn = jnp.zeros((nx, nz))
        self.ex_z0 = jnp.zeros((nx, ny))
        self.ex_zn = jnp.zeros((nx, ny))

        self.ey_x0 = jnp.zeros((ny, nz))
        self.ey_xn = jnp.zeros((ny, nz))
        self.ey_z0 = jnp.zeros((nx, ny))
        self.ey_zn = jnp.zeros((nx, ny))

        self.ez_x0 = jnp.zeros((ny, nz))
        self.ez_xn = jnp.zeros((ny, nz))
        self.ez_y0 = jnp.zeros((nx, nz))
        self.ez_yn = jnp.zeros((nx, nz))

        # PML initialization
        if self.use_pml:
            self._init_cpml()

        # Diagnostics
        self.timestep = 0
        self.max_strain_ratio = 0.0
        self.max_mag_strain = 0.0

        # Params dict for JIT kernels (static across steps)
        self._params = {
            "dt": self.dt,
            "dx": self.dx,
            "epsilon_0": self.epsilon_0,
            "mu_0": self.mu_0,
            "v_yield": self.v_yield,
            "b_yield": self.b_yield,
            "eps_r": self.eps_r,
            "mu_r": self.mu_r,
        }

    def _init_cpml(self) -> None:
        """Initialize CPML conductivity profiles and ψ accumulator arrays."""
        d = self.pml_layers
        m = 3  # cubic grading
        sigma_max = (m + 1) / (150.0 * np.pi * self.dx)

        def _build_sigma(n_cells: int, n_pml: int) -> np.ndarray:
            sigma = np.zeros(n_cells)
            for i in range(n_pml):
                val = sigma_max * ((n_pml - i) / n_pml) ** m
                sigma[i] = val
                sigma[-(i + 1)] = val
            return sigma

        sigma_x = _build_sigma(self.nx, d)
        sigma_y = _build_sigma(self.ny, d)
        sigma_z = _build_sigma(self.nz, d)

        # CPML decay: b = exp(−σ·dt/ε₀)
        self.bx = jnp.array(np.exp(-sigma_x * self.dt / self.epsilon_0))
        self.by = jnp.array(np.exp(-sigma_y * self.dt / self.epsilon_0))
        self.bz = jnp.array(np.exp(-sigma_z * self.dt / self.epsilon_0))

    def _sync_params(self) -> None:
        """Update params dict when eps_r or mu_r change (numpy→JAX conversion)."""
        self._params["eps_r"] = jnp.array(self.eps_r)
        self._params["mu_r"] = jnp.array(self.mu_r)

    def inject_soft_source(self, field: str, x: int, y: int, z: int, amplitude: float) -> None:
        """Inject a soft source (additive) into a field component at (x, y, z)."""
        if field == "Ex":
            self.Ex = self.Ex.at[x, y, z].add(amplitude)
        elif field == "Ey":
            self.Ey = self.Ey.at[x, y, z].add(amplitude)
        elif field == "Ez":
            self.Ez = self.Ez.at[x, y, z].add(amplitude)

    def step(self) -> None:
        """Execute one complete dt timestep of the Maxwell Yee-cell algorithm."""
        # Sync material maps (numpy→JAX) before computation
        self._sync_params()
        # Field updates (JIT-compiled)
        self.Ex, self.Ey, self.Ez, self.Hx, self.Hy, self.Hz = _update_fields_step(
            self.Ex,
            self.Ey,
            self.Ez,
            self.Hx,
            self.Hy,
            self.Hz,
            self._params,
            self.linear_only,
        )

        # Boundary conditions
        if self.use_pml:
            self.Ex, self.Ey, self.Ez, self.Hx, self.Hy, self.Hz = _apply_pml_jax(
                self.Ex,
                self.Ey,
                self.Ez,
                self.Hx,
                self.Hy,
                self.Hz,
                self.bx,
                self.by,
                self.bz,
            )
        else:
            self.Ex, self.Ey, self.Ez, abc_mem = _apply_mur_abc_jax(
                self.Ex,
                self.Ey,
                self.Ez,
                self.abc_coef,
                self.ex_y0,
                self.ex_yn,
                self.ex_z0,
                self.ex_zn,
                self.ey_x0,
                self.ey_xn,
                self.ey_z0,
                self.ey_zn,
                self.ez_x0,
                self.ez_xn,
                self.ez_y0,
                self.ez_yn,
            )
            (
                self.ex_y0,
                self.ex_yn,
                self.ex_z0,
                self.ex_zn,
                self.ey_x0,
                self.ey_xn,
                self.ey_z0,
                self.ey_zn,
                self.ez_x0,
                self.ez_xn,
                self.ez_y0,
                self.ez_yn,
            ) = abc_mem

        self.timestep += 1

    def run(self, n_steps: int) -> "FDTD3DEngineJAX":
        """Run n_steps timesteps. Returns self for chaining."""
        for _ in range(n_steps):
            self.step()
        return self

    def total_field_energy(self) -> float:
        """
        Compute total electromagnetic energy:
        U = Σ (½ε_eff|E|² + ½μ_eff|H|²) · dx³
        """
        u = _total_field_energy_jax(
            self.Ex,
            self.Ey,
            self.Ez,
            self.Hx,
            self.Hy,
            self.Hz,
            self._params,
            self.linear_only,
        )
        return float(u)

    def energy_density(self) -> jax.Array:
        """
        Compute EM energy density u(x,y,z) per cell [J/m³].
        u = ½ε_eff|E|² + ½μ_eff|H|²
        """
        return _energy_density_jax(
            self.Ex,
            self.Ey,
            self.Ez,
            self.Hx,
            self.Hy,
            self.Hz,
            self._params,
            self.linear_only,
        )

    def ponderomotive_force(self) -> tuple[jax.Array, jax.Array, jax.Array]:
        """
        Compute the ponderomotive force density F = −∇u [N/m³].
        Returns (Fx, Fy, Fz) arrays.
        """
        u = self.energy_density()
        dx = self.dx

        Fx = jnp.zeros_like(u)
        Fy = jnp.zeros_like(u)
        Fz = jnp.zeros_like(u)

        Fx = Fx.at[1:-1, :, :].set(-(u[2:, :, :] - u[:-2, :, :]) / (2 * dx))
        Fy = Fy.at[:, 1:-1, :].set(-(u[:, 2:, :] - u[:, :-2, :]) / (2 * dx))
        Fz = Fz.at[:, :, 1:-1].set(-(u[:, :, 2:] - u[:, :, :-2]) / (2 * dx))

        return Fx, Fy, Fz

    def to_numpy(self) -> dict[str, np.ndarray]:
        """Return numpy copies of all field arrays (for matplotlib etc.)."""
        return {
            "Ex": np.array(self.Ex),
            "Ey": np.array(self.Ey),
            "Ez": np.array(self.Ez),
            "Hx": np.array(self.Hx),
            "Hy": np.array(self.Hy),
            "Hz": np.array(self.Hz),
        }
