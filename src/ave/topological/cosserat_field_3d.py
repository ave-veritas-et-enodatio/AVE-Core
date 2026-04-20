"""
3D Cosserat field solver on the K4 diamond substrate (JAX-backed).

Carries the translational displacement u(r) and the Cosserat microrotation
omega(r) as independent fields on the Cartesian-with-FCC-filter grid pattern
of ave.core.k4_tlm. Supports the electron topological sector (c = 3) via a
Sutcliffe-style (2,3)-torus-knot initial ansatz, relaxes to the ground state
by gradient descent on the Cosserat energy functional (optionally with the
Axiom-4 saturation kernel), and reads out the Golden-Torus geometry and
multipole Q-factor.

Moduli pinning (natural units, ell_node = 1): G = G_c = gamma = rho_vac = 1.

The energy gradient is computed by jax.grad — no hand-derived stress tensors.
Under use_saturation=True the jax-grad version is exact; compare to the prior
hand-derived version (now removed) which disagreed with FD on the saturation
path.

References: research/L3_electron_soliton/02_, 03_, 04_, 07_, 08_, 09_.
"""
from __future__ import annotations

import jax

jax.config.update("jax_enable_x64", True)

import jax.numpy as jnp  # noqa: E402
import numpy as np  # noqa: E402


TETRA_OFFSETS: tuple[tuple[int, int, int], ...] = (
    (+1, +1, +1),
    (+1, -1, -1),
    (-1, +1, -1),
    (-1, -1, +1),
)
TETRA_P = jnp.array(TETRA_OFFSETS, dtype=jnp.float32)


# ----------------------------------------------------------------------
# Pure JAX functions (module-level; jitted below)
# ----------------------------------------------------------------------


def _tetrahedral_gradient(V: jnp.ndarray) -> jnp.ndarray:
    """d_j V_i ~= (1/4) sum_ell p_ell^j (V(x + p_ell) - V(x)). First-order
    consistent on the diamond lattice; see 09_ §1.2."""
    grad = jnp.zeros(V.shape + (3,), dtype=V.dtype)
    for p in TETRA_OFFSETS:
        V_neighbor = jnp.roll(V, shift=(-p[0], -p[1], -p[2]), axis=(0, 1, 2))
        delta = V_neighbor - V
        for j in range(3):
            if p[j] != 0:
                grad = grad.at[..., j].add(0.25 * p[j] * delta)
    return grad


def adjoint_tetrahedral_divergence(T: jnp.ndarray) -> jnp.ndarray:
    """Discrete adjoint of _tetrahedral_gradient: (1/4) sum_ell p_ell^j
    [T(x - p_ell) - T(x)] summed over j. Kept for external callers; the
    jax-grad energy path no longer needs it internally."""
    result = jnp.zeros(T.shape[:-1], dtype=T.dtype)
    for p in TETRA_OFFSETS:
        T_shifted = jnp.roll(T, shift=(p[0], p[1], p[2]), axis=(0, 1, 2))
        delta = T_shifted - T
        for j in range(3):
            if p[j] != 0:
                result += 0.25 * p[j] * delta[..., j]
    return result


def _compute_strain(u: jnp.ndarray, omega: jnp.ndarray, dx: float) -> jnp.ndarray:
    """eps_ij = d_j u_i - eps_ijk omega_k. Returns (nx, ny, nz, 3, 3)."""
    grad_u = _tetrahedral_gradient(u) / dx
    w = omega
    cross = jnp.zeros_like(grad_u)
    cross = cross.at[..., 0, 1].set(w[..., 2])
    cross = cross.at[..., 0, 2].set(-w[..., 1])
    cross = cross.at[..., 1, 0].set(-w[..., 2])
    cross = cross.at[..., 1, 2].set(w[..., 0])
    cross = cross.at[..., 2, 0].set(w[..., 1])
    cross = cross.at[..., 2, 1].set(-w[..., 0])
    return grad_u - cross


def _compute_curvature(omega: jnp.ndarray, dx: float) -> jnp.ndarray:
    """kappa_ij = d_j omega_i."""
    return _tetrahedral_gradient(omega) / dx


def _energy_density_bare(
    u: jnp.ndarray,
    omega: jnp.ndarray,
    mask_alive: jnp.ndarray,
    dx: float,
    G: float,
    G_c: float,
    gamma: float,
) -> jnp.ndarray:
    """Cosserat energy density without the saturation kernel.

    W = (2/3) G (tr eps)^2 + G eps_sym · eps_sym + G_c eps_antisym · eps_antisym
        + gamma kappa · kappa
    """
    eps = _compute_strain(u, omega, dx)
    kappa = _compute_curvature(omega, dx)
    eps_T = jnp.swapaxes(eps, -1, -2)
    eps_sym = 0.5 * (eps + eps_T)
    eps_antisym = 0.5 * (eps - eps_T)
    trace_eps = eps[..., 0, 0] + eps[..., 1, 1] + eps[..., 2, 2]
    W_cauchy = (2.0 / 3.0) * trace_eps**2 + jnp.sum(eps_sym**2, axis=(-1, -2))
    W_micropolar = jnp.sum(eps_antisym**2, axis=(-1, -2))
    W_kappa = jnp.sum(kappa**2, axis=(-1, -2))
    W = W_cauchy * G + W_micropolar * G_c + W_kappa * gamma
    return W * mask_alive.astype(W.dtype)


def _energy_density_saturated(
    u: jnp.ndarray,
    omega: jnp.ndarray,
    mask_alive: jnp.ndarray,
    dx: float,
    G: float,
    G_c: float,
    gamma: float,
    omega_yield: float,
    epsilon_yield: float,
) -> jnp.ndarray:
    """Cosserat energy density with scalar-invariant Axiom-4 saturation
    applied to |eps| and |kappa| separately."""
    eps = _compute_strain(u, omega, dx)
    kappa = _compute_curvature(omega, dx)
    eps_T = jnp.swapaxes(eps, -1, -2)
    eps_sym = 0.5 * (eps + eps_T)
    eps_antisym = 0.5 * (eps - eps_T)
    trace_eps = eps[..., 0, 0] + eps[..., 1, 1] + eps[..., 2, 2]
    W_cauchy = (2.0 / 3.0) * trace_eps**2 + jnp.sum(eps_sym**2, axis=(-1, -2))
    W_micropolar = jnp.sum(eps_antisym**2, axis=(-1, -2))
    W_kappa = jnp.sum(kappa**2, axis=(-1, -2))
    eps_sq = jnp.sum(eps**2, axis=(-1, -2))
    kappa_sq = jnp.sum(kappa**2, axis=(-1, -2))
    S_eps_sq = jnp.clip(1.0 - eps_sq / epsilon_yield**2, 0.0, 1.0)
    S_kappa_sq = jnp.clip(1.0 - kappa_sq / omega_yield**2, 0.0, 1.0)
    W = (W_cauchy * G + W_micropolar * G_c) * S_eps_sq + W_kappa * gamma * S_kappa_sq
    return W * mask_alive.astype(W.dtype)


def _total_energy_bare(u, omega, mask_alive, dx, G, G_c, gamma):
    return jnp.sum(_energy_density_bare(u, omega, mask_alive, dx, G, G_c, gamma))


def _total_energy_saturated(u, omega, mask_alive, dx, G, G_c, gamma, omega_yield, epsilon_yield):
    return jnp.sum(_energy_density_saturated(
        u, omega, mask_alive, dx, G, G_c, gamma, omega_yield, epsilon_yield
    ))


# JIT-compiled energy-and-gradient functions.
# jax.value_and_grad returns (value, gradient_tuple) for the argnums we diff.
_val_and_grad_bare = jax.jit(jax.value_and_grad(_total_energy_bare, argnums=(0, 1)))
_val_and_grad_saturated = jax.jit(jax.value_and_grad(_total_energy_saturated, argnums=(0, 1)))
_total_energy_bare_jit = jax.jit(_total_energy_bare)
_total_energy_saturated_jit = jax.jit(_total_energy_saturated)


# ----------------------------------------------------------------------
# Public numpy-style shim for backward compatibility with existing tests
# ----------------------------------------------------------------------


def tetrahedral_gradient(V):
    """Numpy-compatible wrapper around _tetrahedral_gradient.

    Accepts numpy or jax arrays; returns same type as input.
    """
    was_np = isinstance(V, np.ndarray)
    V_jax = jnp.asarray(V)
    result = _tetrahedral_gradient(V_jax)
    return np.asarray(result) if was_np else result


# ----------------------------------------------------------------------
# Solver class
# ----------------------------------------------------------------------


class CosseratField3D:
    """Cartesian-with-FCC-filter solver for the 3D Cosserat field (u, omega)
    on the K4 diamond substrate, JAX-backed. State held as jax arrays; public
    attribute reads return numpy via __getattribute__ hooks are avoided —
    instead, users can np.asarray(solver.u) / np.asarray(solver.omega) to
    materialize when needed."""

    def __init__(self, nx: int, ny: int, nz: int, dx: float = 1.0, use_saturation: bool = True):
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.dx = float(dx)

        idx = np.indices((nx, ny, nz))
        i, j, k = idx[0], idx[1], idx[2]
        mask_A = (i % 2 == 0) & (j % 2 == 0) & (k % 2 == 0)
        mask_B = (i % 2 == 1) & (j % 2 == 1) & (k % 2 == 1)
        self.mask_A = mask_A
        self.mask_B = mask_B
        self.mask_alive = mask_A | mask_B
        self._i, self._j, self._k = i, j, k
        self._mask_alive_jax = jnp.asarray(self.mask_alive)

        # State is numpy for easy mutation; converted to jnp at each energy /
        # gradient call. The conversion overhead is small relative to the
        # jitted JAX kernels.
        self.u = np.zeros((nx, ny, nz, 3), dtype=np.float64)
        self.omega = np.zeros((nx, ny, nz, 3), dtype=np.float64)

        self.G = 1.0
        self.G_c = 1.0
        self.gamma = 1.0
        self.use_saturation = use_saturation
        self.omega_yield = float(np.pi)
        self.epsilon_yield = 1.0

    # ------------------------------------------------------------------
    # Initial condition
    # ------------------------------------------------------------------

    def initialize_electron_2_3_sector(
        self,
        R_target: float,
        r_target: float,
        localization_sigma: float | None = None,
    ) -> None:
        cx, cy, cz = (self.nx - 1) / 2.0, (self.ny - 1) / 2.0, (self.nz - 1) / 2.0
        x = self._i - cx
        y = self._j - cy
        z = self._k - cz

        rho_xy = np.sqrt(x**2 + y**2)
        rho_tube = np.sqrt((rho_xy - R_target) ** 2 + z**2)
        phi = np.arctan2(y, x)
        psi = np.arctan2(z, rho_xy - R_target)

        sigma = localization_sigma if localization_sigma is not None else r_target
        envelope = np.pi * np.exp(-(rho_tube**2) / (sigma**2))
        theta = 2.0 * phi + 3.0 * psi

        omega = np.zeros((self.nx, self.ny, self.nz, 3), dtype=np.float64)
        omega[..., 0] = envelope * np.cos(theta)
        omega[..., 1] = envelope * np.sin(theta)
        omega[..., 2] = 0.0
        omega *= self.mask_alive[..., None]

        self.omega = omega
        self.u = np.zeros_like(self.u)

    def _zero_outside_alive(self) -> None:
        mask = self.mask_alive[..., None].astype(self.u.dtype)
        self.u = self.u * mask
        self.omega = self.omega * mask

    # ------------------------------------------------------------------
    # Kinematic tensors
    # ------------------------------------------------------------------

    def compute_strain(self) -> np.ndarray:
        return np.asarray(_compute_strain(jnp.asarray(self.u), jnp.asarray(self.omega), self.dx))

    def compute_curvature(self) -> np.ndarray:
        return np.asarray(_compute_curvature(jnp.asarray(self.omega), self.dx))

    # ------------------------------------------------------------------
    # Energy and gradient (via jax.grad)
    # ------------------------------------------------------------------

    def energy_density(self) -> np.ndarray:
        u_j = jnp.asarray(self.u)
        w_j = jnp.asarray(self.omega)
        if self.use_saturation:
            rho = _energy_density_saturated(
                u_j, w_j, self._mask_alive_jax, self.dx,
                self.G, self.G_c, self.gamma,
                self.omega_yield, self.epsilon_yield,
            )
        else:
            rho = _energy_density_bare(
                u_j, w_j, self._mask_alive_jax, self.dx,
                self.G, self.G_c, self.gamma,
            )
        return np.asarray(rho)

    def total_energy(self) -> float:
        u_j = jnp.asarray(self.u)
        w_j = jnp.asarray(self.omega)
        if self.use_saturation:
            return float(_total_energy_saturated_jit(
                u_j, w_j, self._mask_alive_jax, self.dx,
                self.G, self.G_c, self.gamma,
                self.omega_yield, self.epsilon_yield,
            ))
        return float(_total_energy_bare_jit(
            u_j, w_j, self._mask_alive_jax, self.dx,
            self.G, self.G_c, self.gamma,
        ))

    def energy_gradient(self) -> tuple[np.ndarray, np.ndarray]:
        """Via jax.value_and_grad on the energy functional. Exact to
        float-precision — no hand-derived stress tensors involved."""
        u_j = jnp.asarray(self.u)
        w_j = jnp.asarray(self.omega)
        if self.use_saturation:
            _, (dE_du, dE_dw) = _val_and_grad_saturated(
                u_j, w_j, self._mask_alive_jax, self.dx,
                self.G, self.G_c, self.gamma,
                self.omega_yield, self.epsilon_yield,
            )
        else:
            _, (dE_du, dE_dw) = _val_and_grad_bare(
                u_j, w_j, self._mask_alive_jax, self.dx,
                self.G, self.G_c, self.gamma,
            )
        mask = self._mask_alive_jax[..., None].astype(dE_du.dtype)
        return np.asarray(dE_du * mask), np.asarray(dE_dw * mask)

    # ------------------------------------------------------------------
    # Relaxation
    # ------------------------------------------------------------------

    def relax_step(self, learning_rate: float = 0.01) -> float:
        E_before = self.total_energy()
        dE_du, dE_dw = self.energy_gradient()
        self.u = self.u - learning_rate * dE_du
        self.omega = self.omega - learning_rate * dE_dw
        self._zero_outside_alive()
        return E_before

    def relax_to_ground_state(
        self,
        max_iter: int = 1000,
        tol: float = 1e-6,
        initial_lr: float = 0.01,
        verbose: bool = False,
    ) -> dict:
        lr = initial_lr
        history = []
        E_prev = self.total_energy()
        history.append(E_prev)
        noise_floor = 1e-12 * max(abs(E_prev), 1.0)

        for step in range(max_iter):
            u_save = self.u.copy()
            w_save = self.omega.copy()
            self.relax_step(lr)
            E_new = self.total_energy()

            if E_new <= E_prev + noise_floor:
                rel_change = abs(E_new - E_prev) / max(abs(E_prev), 1e-12)
                history.append(E_new)
                if verbose and step % 20 == 0:
                    print(f"  step {step:4d}  E = {E_new:.6e}  lr = {lr:.2e}  drel = {rel_change:.2e}")
                if step > 10 and rel_change < tol:
                    return {
                        "iterations": step + 1,
                        "final_energy": E_new,
                        "converged": True,
                        "energy_history": history,
                        "lr_final": lr,
                    }
                lr = min(lr * 1.1, 1.0)
                E_prev = E_new
                noise_floor = 1e-12 * max(abs(E_prev), 1.0)
            else:
                self.u = u_save
                self.omega = w_save
                lr *= 0.5
                if lr < 1e-14:
                    return {
                        "iterations": step + 1,
                        "final_energy": E_prev,
                        "converged": False,
                        "energy_history": history,
                        "lr_final": lr,
                    }

        return {
            "iterations": max_iter,
            "final_energy": E_prev,
            "converged": False,
            "energy_history": history,
            "lr_final": lr,
        }

    # ------------------------------------------------------------------
    # Diagnostics (numpy-backed)
    # ------------------------------------------------------------------

    def extract_shell_radii(self) -> tuple[float, float]:
        omega_mag = np.sqrt(np.sum(self.omega**2, axis=-1))
        cx, cy, cz = (self.nx - 1) / 2.0, (self.ny - 1) / 2.0, (self.nz - 1) / 2.0
        kz = int(round(cz))

        slice_z = omega_mag[:, :, kz]
        xs = self._i[:, :, kz] - cx
        ys = self._j[:, :, kz] - cy
        rho = np.sqrt(xs**2 + ys**2)

        rho_flat = rho.flatten()
        mag_flat = slice_z.flatten()
        rho_max = float(rho.max())
        n_bins = max(8, int(round(rho_max)))
        edges = np.linspace(0.0, rho_max, n_bins + 1)
        hist, _ = np.histogram(rho_flat, bins=edges, weights=mag_flat)
        counts, _ = np.histogram(rho_flat, bins=edges)
        with np.errstate(divide="ignore", invalid="ignore"):
            profile = np.where(counts > 0, hist / np.maximum(counts, 1), 0.0)
        centers = 0.5 * (edges[:-1] + edges[1:])

        R = float(centers[np.argmax(profile)])

        half_max = 0.5 * profile.max()
        above = profile >= half_max
        if above.any():
            left = centers[above][0]
            right = centers[above][-1]
            r = float(0.5 * (right - left))
        else:
            r = 0.0
        return R, r

    def extract_crossing_count(self) -> int:
        cx, cy, cz = (self.nx - 1) / 2.0, (self.ny - 1) / 2.0, (self.nz - 1) / 2.0
        R_found, _ = self.extract_shell_radii()

        n_psi = 64
        psis = np.linspace(0.0, 2.0 * np.pi, n_psi, endpoint=False)
        r_sample = max(1.5, R_found * 0.25)
        dx_s = cx + (R_found + r_sample * np.cos(psis))
        dy_s = cy + np.zeros_like(psis)
        dz_s = cz + r_sample * np.sin(psis)

        omega_np = self.omega

        def sample(comp: int) -> np.ndarray:
            ix = np.clip(dx_s.astype(int), 0, self.nx - 2)
            iy = np.clip(dy_s.astype(int), 0, self.ny - 2)
            iz = np.clip(dz_s.astype(int), 0, self.nz - 2)
            fx = dx_s - ix
            fy = dy_s - iy
            fz = dz_s - iz
            c000 = omega_np[ix, iy, iz, comp]
            c100 = omega_np[ix + 1, iy, iz, comp]
            c010 = omega_np[ix, iy + 1, iz, comp]
            c001 = omega_np[ix, iy, iz + 1, comp]
            c110 = omega_np[ix + 1, iy + 1, iz, comp]
            c101 = omega_np[ix + 1, iy, iz + 1, comp]
            c011 = omega_np[ix, iy + 1, iz + 1, comp]
            c111 = omega_np[ix + 1, iy + 1, iz + 1, comp]
            return (
                (1 - fx) * (1 - fy) * (1 - fz) * c000
                + fx * (1 - fy) * (1 - fz) * c100
                + (1 - fx) * fy * (1 - fz) * c010
                + (1 - fx) * (1 - fy) * fz * c001
                + fx * fy * (1 - fz) * c110
                + fx * (1 - fy) * fz * c101
                + (1 - fx) * fy * fz * c011
                + fx * fy * fz * c111
            )

        ox = sample(0)
        oy = sample(1)
        phase = np.arctan2(oy, ox)
        unwrapped = np.unwrap(phase)
        total_winding = (unwrapped[-1] - unwrapped[0]) / (2.0 * np.pi)
        closure = phase[0] - unwrapped[-1]
        while closure > np.pi:
            closure -= 2.0 * np.pi
        while closure < -np.pi:
            closure += 2.0 * np.pi
        total_winding += closure / (2.0 * np.pi)
        return int(round(abs(total_winding)))

    def extract_quality_factor(self) -> float:
        R, r = self.extract_shell_radii()
        d = 1.0
        return 16.0 * np.pi**3 * (R * r) + 4.0 * np.pi**2 * (R * r) + np.pi * d
