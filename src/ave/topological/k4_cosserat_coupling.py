"""
Coupled K4 ⊗ Cosserat time-domain simulator — Phase II of the AVE ideal.

S-gate resolutions (2026-04-22, all approved by Grant):
    S1 = D  : Coupling form    `L_c = (V²/V_SNAP²) · W_refl(u, ω)` — pure
              Axiom-4 reuse of `_reflection_density`, ZERO new parameters.
    S2 = γ  : Port pairing     deferred (S1-D is phase-insensitive).
    S3 = A  : Amplitude gate   NONE — S1-D is already gated by
              W_refl's 1/S² structure (vanishes for zero (u,ω)).
    S4 = A  : Cosserat params  `ρ = I_ω = 1` natural units; SI calibration
              deferred post-Phase-III.
    S5 = B  : Integrator       Unified leapfrog with coupling force applied
              to BOTH sectors at shared outer dt. Cosserat sub-steps within
              each K4 outer step to satisfy Cosserat CFL without changing
              physics (matches Phase I Verlet exactly within sub-steps).
    S6 = A  : Q conservation   Soft/diagnostic only; extract topological
              charge via cosserat.extract_crossing_count(), do not project.

Axiom mapping (plan §"Axiom compliance map"):
  • Axiom 1 (LC substrate)        — K4 scatter+connect pipeline unchanged.
  • Axiom 2 (topo-kinematic)      — Q measured, not enforced (S6=A).
  • Axiom 3 (action principle)    — Unified Lagrangian
        S = S_K4(V) + S_Cos(u, ω) + ∫ (V²/V_SNAP²)·W_refl(u, ω) dt dx³.
  • Axiom 4 (saturation)          — W_refl IS the Axiom-4 operator; coupling
        is its V²-weighted spatial structure.

Usage:
    sim = CoupledK4Cosserat(N=48, pml=6)
    # Drive the K4 sector with a wave source (see photon_propagation.PlaneSource)
    # Drive the Cosserat sector by initial condition or ansatz
    for _ in range(n_steps):
        sim.step()
    # Diagnostics
    sim.total_hamiltonian()
    sim.total_topological_charge()
"""
from __future__ import annotations

from typing import Optional

import jax
import jax.numpy as jnp
import numpy as np

from ave.core.k4_tlm import K4Lattice3D
from ave.core.constants import V_SNAP as _V_SNAP_CONST
from ave.topological.cosserat_field_3d import (
    CosseratField3D,
    KAPPA_CHIRAL_ELECTRON,
    _beltrami_helicity,
    _compute_curvature,
    _compute_strain,
    _reflection_density,
    _reflection_density_asymmetric,
    _update_saturation_kernels,
)


# ─────────────────────────────────────────────────────────────────────
# Coupling primitives (JAX-autograd-safe)
# ─────────────────────────────────────────────────────────────────────
def _v_squared_per_site(V_inc: np.ndarray) -> np.ndarray:
    """|V|² = Σ_n V_inc[...,n]² per lattice site. Shape (nx, ny, nz)."""
    return np.sum(V_inc ** 2, axis=-1)


def _cosserat_A_squared(
    u: np.ndarray, omega: np.ndarray, dx: float,
    omega_yield: float, epsilon_yield: float,
) -> np.ndarray:
    """Total saturation amplitude² from Cosserat strain + curvature.
        A² = ε²/ε_yield² + κ²/ω_yield²
    Matches the formula used inside `_reflection_density`."""
    u_j = jnp.asarray(u)
    w_j = jnp.asarray(omega)
    eps = _compute_strain(u_j, w_j, dx)
    kappa = _compute_curvature(w_j, dx)
    eps_sq = jnp.sum(eps * eps, axis=(-1, -2))
    kappa_sq = jnp.sum(kappa * kappa, axis=(-1, -2))
    A_sq = eps_sq / (epsilon_yield ** 2) + kappa_sq / (omega_yield ** 2)
    return np.asarray(A_sq)


def _coupling_energy_total(u, omega, V_sq, V_SNAP, dx, omega_yield, epsilon_yield):
    """Scalar: ∫ (V²/V_SNAP²) · W_refl(u, ω) dx³.

    Legacy S1=D coupling (symmetric, single-kernel W_refl). Retained for
    comparison / regression tests that pin pre-Phase-4 behavior. Under
    Phase 4 `use_asymmetric_saturation=True` (default in CoupledK4Cosserat),
    `_coupling_energy_total_asymmetric` is called instead.

    Differentiating wrt (u, ω) gives the coupling force on Cosserat.
    """
    W_refl = _reflection_density(u, omega, dx, omega_yield, epsilon_yield)
    integrand = (V_sq / (V_SNAP ** 2)) * W_refl
    return jnp.sum(integrand)


_coupling_grad = jax.jit(
    jax.value_and_grad(_coupling_energy_total, argnums=(0, 1))
)


def _coupling_energy_total_asymmetric(
    u, omega, V_sq, V_SNAP, dx,
    omega_yield, epsilon_yield, kappa_chiral,
):
    """Scalar: ∫ W_refl_asymmetric(u, ω, V²) dx³ — Phase 4 coupling.

    Under doc 54_ §6, V² is embedded into A²_ε (electric saturation
    sector) rather than applied as a multiplicative factor on W_refl.
    This supersedes the S1=D multiplicative form at the coupling level;
    the asymmetric reflection density already contains the K4 voltage
    contribution internally. No separate (V²/V_SNAP²) factor needed.

    Linear-polarization drive produces zero net Beltrami helicity
    (h_local = 0), so S_μ = S_ε and the reflection density vanishes
    (Achromatic Impedance Lens — Vol 4 Ch 11). Chiral drive breaks the
    symmetry and drives Γ² → large values where S_μ → 0 with S_ε
    finite, producing the Meissner-like confinement wall per
    Vol 1 Ch 7:252.

    See VACUUM_ENGINE_MANUAL §17 A14 r6 + doc 50_ r3 §0.1 + doc 54_ §6.
    """
    W_refl = _reflection_density_asymmetric(
        u, omega, V_sq, dx, V_SNAP,
        omega_yield, epsilon_yield, kappa_chiral,
    )
    return jnp.sum(W_refl)


_coupling_grad_asymmetric = jax.jit(
    jax.value_and_grad(_coupling_energy_total_asymmetric, argnums=(0, 1))
)


# ─────────────────────────────────────────────────────────────────────
# Coupled simulator
# ─────────────────────────────────────────────────────────────────────
class CoupledK4Cosserat:
    """
    Time-domain coupled K4 ⊗ Cosserat simulator implementing the AVE-ideal
    plan (plan `document-list-for-next-chat-compressed-thunder.md`, Phase II).

    State:
        k4   : K4Lattice3D  (V_inc, V_ref, z_local_field — photon sector)
        cos  : CosseratField3D  (u, omega, u_dot, omega_dot — soliton sector)

    Coupling (S1-D):
        L_c = (V²/V_SNAP²) · W_refl(u, ω)
        • ω → V:  W_refl(u, ω) modifies K4's z_local_field via Op14
                  (Z/Z_0 = (1 − A²_total)^{−1/4}), where
                  A²_total = A²_K4 (from V) + A²_Cos (from (u,ω))
        • V → ω:  the coupling energy's gradient wrt (u, ω) is ADDED to the
                  Cosserat energy gradient each sub-step.

    Integrator (S5-B, unified leapfrog):
        Each `step()` advances BOTH sectors by `outer_dt = k4.dt` in
        natural units. K4 does 1 scatter+connect. Cosserat sub-steps by
        Verlet at `dt_sub = cfl_dt` to satisfy its CFL at `ρ = I_ω = 1`
        (S4-A). Coupling force is recomputed each Cosserat sub-step (V
        frozen during the K4 cycle). `Q` is a diagnostic output (S6-A),
        not projected.
    """

    def __init__(
        self,
        N: int,
        pml: int = 6,
        rho: float = 1.0,
        I_omega: float = 1.0,
        *,
        V_SNAP: Optional[float] = None,
        cfl_safety: float = 0.3,
        use_asymmetric_saturation: bool = True,
        kappa_chiral: float = KAPPA_CHIRAL_ELECTRON,
    ):
        self.N = int(N)
        self.pml = int(pml)
        self.cfl_safety = float(cfl_safety)
        # Phase 4 — Asymmetric μ/ε saturation (S1 gate reopen per doc 54_ §6,
        # VACUUM_ENGINE_MANUAL §17 A14 r6). Default True enables the
        # axiom-native (S_μ, S_ε) split with chirality bias; False restores
        # the pre-Phase-4 single-kernel symmetric form for regression tests
        # that pin legacy behavior.
        self.use_asymmetric_saturation = bool(use_asymmetric_saturation)
        self.kappa_chiral = float(kappa_chiral)

        # K4 photon sector: nonlinear=False so K4's node-level saturation
        # doesn't duplicate Cosserat coupling; op3_bond_reflection=True so
        # z_local → bond Γ path is active (per Axiom 4 / Op3).
        self.k4 = K4Lattice3D(
            nx=N, ny=N, nz=N, dx=1.0,
            nonlinear=False, pml_thickness=pml,
            op3_bond_reflection=True,
        )
        # Override k4.dt and k4.c to natural units (c = 1, dx = 1, dt = 1/√2)
        # so both sectors share a unit system. This does NOT change K4's
        # scatter/connect kinematics — those are dimensionless. Only the
        # time scale label changes.
        self.k4.c = 1.0
        self.k4.dt = 1.0 / np.sqrt(2.0)

        # Cosserat soliton sector, natural units (S4-A), linear Lagrangian
        # (Op10, Hopf, reflection all off — reflection is carried by the
        # coupling term, NOT as a standalone energy).
        # pml_thickness inherits from K4 per doc 58_ §4.3 (same lattice,
        # same boundary, Ax3 → same rule every sector). pml=0 disables
        # Cosserat PML (legacy behavior preserved).
        self.cos = CosseratField3D(
            nx=N, ny=N, nz=N, dx=1.0,
            use_saturation=False,
            rho=rho, I_omega=I_omega,
            pml_thickness=pml,
        )
        self.cos.k_op10 = 0.0
        self.cos.k_refl = 0.0   # carried in coupling
        self.cos.k_hopf = 0.0

        self.V_SNAP = float(V_SNAP if V_SNAP is not None else _V_SNAP_CONST)
        self.time = 0.0

        # Sub-stepping: Cosserat needs N_sub sub-steps per K4 outer dt
        self._n_sub = max(1, int(np.ceil(self.k4.dt / self.cos.cfl_dt)))
        self._dt_sub = self.k4.dt / self._n_sub

        # Store diagnostics history (opt-in via step_with_history)
        self._history: dict[str, list] = {}

    # -----------------------------------------------------------------
    # Simulator properties
    # -----------------------------------------------------------------
    @property
    def outer_dt(self) -> float:
        """Outer timestep = K4 dt. Each step() advances time by this."""
        return self.k4.dt

    @property
    def dt_sub(self) -> float:
        """Cosserat sub-step dt. n_sub sub-steps per outer dt."""
        return self._dt_sub

    @property
    def n_sub(self) -> int:
        return self._n_sub

    # -----------------------------------------------------------------
    # Coupling computations
    # -----------------------------------------------------------------
    def _update_z_local_total(self) -> None:
        """Set k4.z_local_field from the active saturation model.

        Phase 4 (use_asymmetric_saturation=True, default) — doc 54_ §6:
            A²_μ = (1 + κ_chiral·h)·κ²/ω_yield²        (magnetic sector)
            A²_ε = (1 − κ_chiral·h)·(ε²/ε_yield² + V²/V_SNAP²)   (electric)
            S_μ = √(1−A²_μ), S_ε = √(1−A²_ε)
            Z_eff/Z_0 = √(S_μ/S_ε)                     (Vol 1 Ch 7:252)

          Symmetric case (h=0, linear drive): S_μ = S_ε → Z_eff = Z_0
          constant (Achromatic Impedance Lens, Vol 4 Ch 11 — gravity).
          Asymmetric (chiral drive): Z_eff → 0 as S_μ → 0 (Meissner,
          Γ → -1 confinement wall for pair formation).

        Legacy (use_asymmetric_saturation=False) — single-kernel Op14:
            A²_total = V²/V_SNAP² + ε²/ε_yield² + κ²/ω_yield²
            Z_eff/Z_0 = (1 − A²_total)^{−1/4}
          Pre-Phase-4 behavior; retained for regression tests pinning
          the simplified form.
        """
        V_sq = _v_squared_per_site(self.k4.V_inc)

        if self.use_asymmetric_saturation:
            S_mu, S_eps = _update_saturation_kernels(
                jnp.asarray(self.cos.u), jnp.asarray(self.cos.omega),
                jnp.asarray(V_sq), self.cos.dx, self.V_SNAP,
                self.cos.omega_yield, self.cos.epsilon_yield,
                self.kappa_chiral,
            )
            # Z_eff/Z_0 = √(S_μ/S_ε) per doc 54_ §6 line 194
            S_mu_np = np.asarray(S_mu)
            S_eps_np = np.asarray(S_eps)
            z_local = np.sqrt(np.maximum(S_mu_np, 1e-12)
                              / np.maximum(S_eps_np, 1e-12))
        else:
            A_sq_k4 = V_sq / (self.V_SNAP ** 2)
            A_sq_cos = _cosserat_A_squared(
                self.cos.u, self.cos.omega, self.cos.dx,
                self.cos.omega_yield, self.cos.epsilon_yield,
            )
            A_sq_total = A_sq_k4 + A_sq_cos
            A_sq_total = np.clip(A_sq_total, 0.0, 1.0 - 1e-12)
            S = np.sqrt(1.0 - A_sq_total)
            z_local = 1.0 / np.maximum(np.sqrt(S), 1e-6)

        # Inactive sites stay at Z_0 = 1 (unity).
        z_local = np.where(self.k4.mask_active, z_local, 1.0)
        self.k4.z_local_field = z_local

    def _compute_coupling_force_on_cosserat(self) -> tuple[np.ndarray, np.ndarray]:
        """Compute (∂L_c/∂u, ∂L_c/∂ω) = grad of coupling energy.

        Under use_asymmetric_saturation=True (Phase 4 default), the coupling
        Lagrangian is the unified asymmetric W_refl with V² embedded inside
        A²_ε — no separate (V²/V_SNAP²) multiplicative factor. Under the
        legacy (False) path, the S1=D multiplicative form is used.

        Returns numpy arrays matching the existing energy_gradient shape.
        """
        V_sq = _v_squared_per_site(self.k4.V_inc)
        V_sq_j = jnp.asarray(V_sq)
        u_j = jnp.asarray(self.cos.u)
        w_j = jnp.asarray(self.cos.omega)

        if self.use_asymmetric_saturation:
            _, (dEc_du, dEc_dw) = _coupling_grad_asymmetric(
                u_j, w_j, V_sq_j, self.V_SNAP, self.cos.dx,
                self.cos.omega_yield, self.cos.epsilon_yield,
                self.kappa_chiral,
            )
        else:
            _, (dEc_du, dEc_dw) = _coupling_grad(
                u_j, w_j, V_sq_j, self.V_SNAP, self.cos.dx,
                self.cos.omega_yield, self.cos.epsilon_yield,
            )

        mask = self.cos._mask_alive_jax[..., None].astype(dEc_du.dtype)
        return np.asarray(dEc_du * mask), np.asarray(dEc_dw * mask)

    # -----------------------------------------------------------------
    # Stepping (S5-B unified leapfrog with sub-stepping)
    # -----------------------------------------------------------------
    def _cosserat_sub_step(self, dt: float) -> None:
        """One Cosserat velocity-Verlet sub-step, ADDING the coupling force.

        The coupling force is computed from the current V (not updated
        within sub-steps, since V is constant during a K4 outer cycle).
        """
        # Force at current state = standalone Cosserat + coupling
        dE_du_s, dE_dw_s = self.cos.energy_gradient()
        dE_du_c, dE_dw_c = self._compute_coupling_force_on_cosserat()
        a_u = -(dE_du_s + dE_du_c) / self.cos.rho
        a_w = -(dE_dw_s + dE_dw_c) / self.cos.I_omega

        # Half-kick
        self.cos.u_dot = self.cos.u_dot + 0.5 * dt * a_u
        self.cos.omega_dot = self.cos.omega_dot + 0.5 * dt * a_w
        self.cos._zero_velocities_outside_alive()

        # Drift
        self.cos.u = self.cos.u + dt * self.cos.u_dot
        self.cos.omega = self.cos.omega + dt * self.cos.omega_dot
        self.cos._zero_outside_alive()

        # Force at new state = standalone + coupling (V still same)
        dE_du_s_new, dE_dw_s_new = self.cos.energy_gradient()
        dE_du_c_new, dE_dw_c_new = self._compute_coupling_force_on_cosserat()
        a_u_new = -(dE_du_s_new + dE_du_c_new) / self.cos.rho
        a_w_new = -(dE_dw_s_new + dE_dw_c_new) / self.cos.I_omega

        # Second half-kick
        self.cos.u_dot = self.cos.u_dot + 0.5 * dt * a_u_new
        self.cos.omega_dot = self.cos.omega_dot + 0.5 * dt * a_w_new
        self.cos._zero_velocities_outside_alive()

        self.cos.time += dt

    def step(self) -> None:
        """One outer coupled step (advances time by outer_dt = k4.dt).

        Order (S5-B unified leapfrog):
          1. Update K4 z_local_field from total A² (K4 + Cosserat).
          2. K4 scatter+connect (one step, using updated z_local).
          3. Cosserat sub-steps (n_sub Verlet sub-steps; coupling force
             applied each sub-step, V frozen during cycle).
        """
        # (1) ω → V coupling: z_local ← total A²
        self._update_z_local_total()

        # (2) K4 step
        self.k4.step()

        # (3) Cosserat sub-steps with V → ω coupling force
        for _ in range(self._n_sub):
            self._cosserat_sub_step(self._dt_sub)

        self.time += self.outer_dt

    # -----------------------------------------------------------------
    # Diagnostics (S6-A: Q measured, not enforced)
    # -----------------------------------------------------------------
    def k4_energy(self) -> float:
        return float(self.k4.total_energy())

    def cosserat_energy(self) -> float:
        return float(self.cos.total_energy())

    def cosserat_kinetic_energy(self) -> float:
        return float(self.cos.kinetic_energy())

    def coupling_energy(self) -> float:
        """⟨L_c⟩ = ∫ (V²/V_SNAP²) · W_refl dx³ at the current state."""
        V_sq = _v_squared_per_site(self.k4.V_inc)
        V_sq_j = jnp.asarray(V_sq)
        u_j = jnp.asarray(self.cos.u)
        w_j = jnp.asarray(self.cos.omega)
        E_c, _ = _coupling_grad(
            u_j, w_j, V_sq_j, self.V_SNAP, self.cos.dx,
            self.cos.omega_yield, self.cos.epsilon_yield,
        )
        return float(E_c)

    def total_hamiltonian(self) -> float:
        """H = E_K4 + E_Cos(kinetic + potential) + E_coupling."""
        return (
            self.k4_energy()
            + self.cosserat_kinetic_energy()
            + self.cosserat_energy()
            + self.coupling_energy()
        )

    def total_topological_charge(self) -> int:
        """Q = winding number from extract_crossing_count (S6-A: diagnostic)."""
        return int(self.cos.extract_crossing_count())

    def shell_radii(self) -> tuple[float, float]:
        """Current (R, r) of the Cosserat shell if any."""
        R, r = self.cos.extract_shell_radii()
        return float(R), float(r)

    def max_A_squared(self) -> float:
        """Peak A²_total value — locates saturated regions."""
        V_sq = _v_squared_per_site(self.k4.V_inc)
        A_sq_k4 = V_sq / (self.V_SNAP ** 2)
        A_sq_cos = _cosserat_A_squared(
            self.cos.u, self.cos.omega, self.cos.dx,
            self.cos.omega_yield, self.cos.epsilon_yield,
        )
        A_sq_total = A_sq_k4 + A_sq_cos
        alive = self.k4.mask_active
        return float(A_sq_total[alive].max()) if alive.any() else 0.0

    # -----------------------------------------------------------------
    # Convenience: snapshot (for diagnostic plotting)
    # -----------------------------------------------------------------
    def snapshot_scalars(self) -> dict:
        """Single-timestep summary of all key observables."""
        V_sq = _v_squared_per_site(self.k4.V_inc)
        A_sq_k4 = V_sq / (self.V_SNAP ** 2)
        A_sq_cos = _cosserat_A_squared(
            self.cos.u, self.cos.omega, self.cos.dx,
            self.cos.omega_yield, self.cos.epsilon_yield,
        )
        alive = self.k4.mask_active
        return {
            "t": float(self.time),
            "E_k4": self.k4_energy(),
            "E_cos": self.cosserat_energy(),
            "T_cos": self.cosserat_kinetic_energy(),
            "E_coupling": self.coupling_energy(),
            "H_total": self.total_hamiltonian(),
            "max_V_sq": float(V_sq[alive].max()) if alive.any() else 0.0,
            "max_A_sq_k4": float(A_sq_k4[alive].max()) if alive.any() else 0.0,
            "max_A_sq_cos": float(A_sq_cos[alive].max()) if alive.any() else 0.0,
            "max_A_sq_total": self.max_A_squared(),
            "Q_charge": self.total_topological_charge(),
        }
