"""
3D Cosserat field solver on the K4 diamond substrate.

Carries the translational displacement u(r) and the Cosserat microrotation
omega(r) as independent fields on the Cartesian-with-FCC-filter grid pattern
of ave.core.k4_tlm. Supports the electron topological sector (c = 3) via a
Sutcliffe-style (2,3)-torus-knot initial ansatz, relaxes to the ground state
by gradient descent on the saturated Cosserat energy functional, and reads
out the Golden-Torus geometry and multipole Q-factor.

Moduli pinning (natural units, ell_node = 1): G = G_c = gamma = rho_vac = 1.

References: research/L3_electron_soliton/02_, 03_, 04_, 07_, 08_, 09_.
"""
from __future__ import annotations

import numpy as np

from ave.core.universal_operators import universal_saturation


TETRA_OFFSETS: tuple[tuple[int, int, int], ...] = (
    (+1, +1, +1),
    (+1, -1, -1),
    (-1, +1, -1),
    (-1, -1, +1),
)


def tetrahedral_gradient(V: np.ndarray) -> np.ndarray:
    """
    Closed-form gradient via the 4 tetrahedral K4 offsets.

    For V of shape (nx, ny, nz, n_comp), returns shape (nx, ny, nz, n_comp, 3)
    with the last axis indexing d/dx, d/dy, d/dz.

    Formula: d_j V_i ~= (1/4) sum_ell p_ell^j (V(x + p_ell) - V(x)).
    Valid at both Type-A and Type-B sites (same formula; the tetrahedral
    neighbor set differs by sign but the scalar sum structure is identical).

    First-order consistent. For second-order accuracy, symmetrize across
    adjacent A and B sites (see research/L3_electron_soliton/09_ §1.4).
    """
    grad = np.zeros(V.shape + (3,), dtype=V.dtype)
    for p in TETRA_OFFSETS:
        V_neighbor = np.roll(V, shift=(-p[0], -p[1], -p[2]), axis=(0, 1, 2))
        delta = V_neighbor - V
        for j in range(3):
            if p[j] != 0:
                grad[..., j] += 0.25 * p[j] * delta
    return grad


def adjoint_tetrahedral_divergence(T: np.ndarray) -> np.ndarray:
    """
    Discrete adjoint of tetrahedral_gradient, used for variational derivatives.

    For T of shape (..., 3) with the last axis indexing direction j, returns
    the divergence-like quantity (1/4) sum_ell p_ell^j [T_j(x - p_ell) - T_j(x)]
    summed over j, with shape (...) (last axis removed).

    Identity used: sum_y (grad_j V)(y) W_j(y) = sum_y V(y) (adj_div W)(y)
    for grad_j = tetrahedral_gradient (modulo the 1/4 and p_ell^j factors
    baked in symmetrically). This makes adj_div the correct operator for
    propagating variational derivatives d(W(kappa))/dkappa back to dW/domega.
    """
    result = np.zeros(T.shape[:-1], dtype=T.dtype)
    for p in TETRA_OFFSETS:
        T_shifted = np.roll(T, shift=(p[0], p[1], p[2]), axis=(0, 1, 2))
        delta = T_shifted - T
        for j in range(3):
            if p[j] != 0:
                result += 0.25 * p[j] * delta[..., j]
    return result


class CosseratField3D:
    """
    Cartesian-with-FCC-filter solver for the 3D Cosserat field (u, omega)
    on the K4 diamond substrate. Follows the grid pattern of
    ave.core.k4_tlm.K4Lattice3D but carries a 6-DOF Cosserat state rather
    than 4-port voltages.
    """

    def __init__(self, nx: int, ny: int, nz: int, dx: float = 1.0):
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.dx = float(dx)

        idx = np.indices((nx, ny, nz))
        i, j, k = idx[0], idx[1], idx[2]
        self.mask_A = (i % 2 == 0) & (j % 2 == 0) & (k % 2 == 0)
        self.mask_B = (i % 2 == 1) & (j % 2 == 1) & (k % 2 == 1)
        self.mask_alive = self.mask_A | self.mask_B
        self._i, self._j, self._k = i, j, k

        self.u = np.zeros((nx, ny, nz, 3), dtype=np.float64)
        self.omega = np.zeros((nx, ny, nz, 3), dtype=np.float64)

        # Pinned moduli (natural units).
        self.G = 1.0
        self.G_c = 1.0
        self.gamma = 1.0

        self.omega_yield = np.pi  # |kappa| yield scale; Nyquist pi / ell_node
        self.epsilon_yield = 1.0

    # ------------------------------------------------------------------
    # Initial condition: Sutcliffe-style (2,3) torus-knot ansatz
    # ------------------------------------------------------------------

    def initialize_electron_2_3_sector(
        self,
        R_target: float,
        r_target: float,
        localization_sigma: float | None = None,
    ) -> None:
        """
        Initialize omega with a Sutcliffe-style (p,q) = (2,3) torus-knot
        phase ansatz localized on a toroidal shell of radii (R_target, r_target)
        centered on the domain midpoint. Combined phase Theta = 2*phi + 3*psi.

        Sets u = 0 everywhere (electron ground state has trivial translational
        sector; the microrotation carries the topology).

        Does NOT enforce saturation or modulus pinning — this is an initial
        guess to be relaxed by gradient descent.
        """
        cx, cy, cz = (self.nx - 1) / 2.0, (self.ny - 1) / 2.0, (self.nz - 1) / 2.0
        x = self._i - cx
        y = self._j - cy
        z = self._k - cz

        # Toroidal coordinates about the xy-plane central ring of major radius R.
        rho_xy = np.sqrt(x**2 + y**2)
        # Distance from the ring itself.
        rho_tube = np.sqrt((rho_xy - R_target) ** 2 + z**2)
        # Angles: phi around z (longitude), psi around the ring (meridian).
        phi = np.arctan2(y, x)
        psi = np.arctan2(z, rho_xy - R_target)

        sigma = localization_sigma if localization_sigma is not None else r_target
        envelope = np.pi * np.exp(-(rho_tube**2) / (sigma**2))

        theta = 2.0 * phi + 3.0 * psi

        self.omega[..., 0] = envelope * np.cos(theta)
        self.omega[..., 1] = envelope * np.sin(theta)
        self.omega[..., 2] = 0.0
        self.u.fill(0.0)

        self._zero_outside_alive()

    def _zero_outside_alive(self) -> None:
        """Mask fields to alive sites only (dead sites carry no physical data)."""
        self.u *= self.mask_alive[..., None]
        self.omega *= self.mask_alive[..., None]

    # ------------------------------------------------------------------
    # Kinematic tensors (strain, curvature-twist)
    # ------------------------------------------------------------------

    def compute_strain(self) -> np.ndarray:
        """
        epsilon_ij = d_j u_i - eps_ijk omega_k.

        Returns shape (nx, ny, nz, 3, 3) with indices (site, i, j).
        """
        grad_u = tetrahedral_gradient(self.u) / self.dx
        # eps_ijk omega_k — antisymmetric contribution to epsilon_ij.
        w = self.omega
        cross = np.zeros_like(grad_u)
        cross[..., 0, 1] = w[..., 2]
        cross[..., 0, 2] = -w[..., 1]
        cross[..., 1, 0] = -w[..., 2]
        cross[..., 1, 2] = w[..., 0]
        cross[..., 2, 0] = w[..., 1]
        cross[..., 2, 1] = -w[..., 0]
        return grad_u - cross

    def compute_curvature(self) -> np.ndarray:
        """kappa_ij = d_j omega_i. Shape (nx, ny, nz, 3, 3)."""
        return tetrahedral_gradient(self.omega) / self.dx

    # ------------------------------------------------------------------
    # Saturated energy functional
    # ------------------------------------------------------------------

    def energy_density(self) -> np.ndarray:
        """
        Local saturated Cosserat energy density per alive node.

        Structure (natural units, K = 2G, isotropic-bending ansatz,
        G = G_c = gamma = 1):
            W_Cauchy     = (2/3)(tr eps)^2 + eps^sym_ij eps^sym_ij
            W_micropolar = eps^antisym_ij eps^antisym_ij
            W_kappa      = kappa_ij kappa_ij
        Scalar-invariant Axiom-4 saturation applied to |eps| and |kappa|.
        """
        eps = self.compute_strain()
        kappa = self.compute_curvature()

        eps_sym = 0.5 * (eps + np.swapaxes(eps, -1, -2))
        eps_antisym = 0.5 * (eps - np.swapaxes(eps, -1, -2))
        trace_eps = eps[..., 0, 0] + eps[..., 1, 1] + eps[..., 2, 2]

        eps_mag = np.sqrt(np.sum(eps**2, axis=(-1, -2)))
        S_eps = universal_saturation(eps_mag, self.epsilon_yield)
        kappa_mag = np.sqrt(np.sum(kappa**2, axis=(-1, -2)))
        S_kappa = universal_saturation(kappa_mag, self.omega_yield)

        W_cauchy = (2.0 / 3.0) * (trace_eps**2) + np.sum(eps_sym**2, axis=(-1, -2))
        W_micropolar = np.sum(eps_antisym**2, axis=(-1, -2))
        W_kappa = np.sum(kappa**2, axis=(-1, -2))

        W = (
            (W_cauchy * self.G + W_micropolar * self.G_c) * (S_eps**2)
            + W_kappa * self.gamma * (S_kappa**2)
        )
        return W * self.mask_alive.astype(W.dtype)

    def total_energy(self) -> float:
        return float(np.sum(self.energy_density()))

    # ------------------------------------------------------------------
    # Stress, couple-stress, and variational gradient
    # ------------------------------------------------------------------

    def _stress_and_couple_stress(
        self,
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Compute saturated stress_ij := dW/d(eps_ij) and couple_stress_ij :=
        dW/d(kappa_ij) at every site. Returns shapes (nx, ny, nz, 3, 3).

        Derivations:
          W_cauchy = (2/3)(tr eps)^2 + eps_sym_ij eps_sym_ij
          W_micro  = eps_antisym_ij eps_antisym_ij
          W_kappa  = kappa_ij kappa_ij

          d(tr eps)^2 / d eps_mn = 2 (tr eps) delta_mn
          d(eps_sym)^2 / d eps_mn = eps_mn + eps_nm
          d(eps_antisym)^2 / d eps_mn = eps_mn - eps_nm

        Bare stresses (before saturation):
          sigma_bare_mn = G [(4/3) tr(eps) delta_mn + eps_mn + eps_nm]
                        + G_c [eps_mn - eps_nm]
          couple_bare_mn = 2 gamma kappa_mn

        Saturation (scalar-invariant, |eps|^2 and |kappa|^2 invariants):
          W_sat = W_bare * S^2,  S = sqrt(1 - |X|^2/Y^2),  |X|^2 = X_ij X_ij
          dW_sat/dX_mn = dW_bare/dX_mn * S^2 - 2 W_bare * X_mn / Y^2

        Saturation zeroes out both factors past yield; numerically we clip
        |X|^2 at the yield value to avoid NaN from negative square roots.
        """
        eps = self.compute_strain()
        kappa = self.compute_curvature()

        eps_T = np.swapaxes(eps, -1, -2)  # eps_nm
        trace_eps = eps[..., 0, 0] + eps[..., 1, 1] + eps[..., 2, 2]

        delta = np.eye(3)
        # Bare stress
        sigma_bare = (
            self.G * ((4.0 / 3.0) * trace_eps[..., None, None] * delta + eps + eps_T)
            + self.G_c * (eps - eps_T)
        )
        # Bare couple stress
        couple_bare = 2.0 * self.gamma * kappa

        # Bare Cosserat elastic energies at each site (not including kappa).
        eps_sym = 0.5 * (eps + eps_T)
        eps_antisym = 0.5 * (eps - eps_T)
        W_cauchy = (2.0 / 3.0) * (trace_eps**2) + np.sum(eps_sym**2, axis=(-1, -2))
        W_micropolar = np.sum(eps_antisym**2, axis=(-1, -2))
        W_eps_bare = W_cauchy * self.G + W_micropolar * self.G_c
        W_kappa_bare = self.gamma * np.sum(kappa**2, axis=(-1, -2))

        # Saturation factors (scalar-invariant).
        eps_sq = np.sum(eps**2, axis=(-1, -2))
        kappa_sq = np.sum(kappa**2, axis=(-1, -2))
        Y_eps_sq = self.epsilon_yield**2
        Y_kappa_sq = self.omega_yield**2

        # Clip arguments of S^2 away from (0, negative) to stay differentiable.
        S_eps_sq = np.clip(1.0 - eps_sq / Y_eps_sq, 0.0, 1.0)
        S_kappa_sq = np.clip(1.0 - kappa_sq / Y_kappa_sq, 0.0, 1.0)

        # Saturated stresses.
        sigma_sat = sigma_bare * S_eps_sq[..., None, None] - 2.0 * W_eps_bare[..., None, None] * eps / Y_eps_sq
        couple_sat = couple_bare * S_kappa_sq[..., None, None] - 2.0 * W_kappa_bare[..., None, None] * kappa / Y_kappa_sq

        return sigma_sat, couple_sat

    def energy_gradient(self) -> tuple[np.ndarray, np.ndarray]:
        """
        Variational derivative of the total energy w.r.t. the fields.
        Returns (dE/du, dE/domega), each of shape (nx, ny, nz, 3).

        Chain rule:
          dE/du_i(x)     = sum_j adj_div_j sigma_sat_ij(x)
          dE/domega_k(x) = -eps_ijk sigma_sat_ij(x) + sum_j adj_div_j couple_sat_kj(x)

        Both terms are computed per-site with O(N) complexity.
        """
        sigma, couple = self._stress_and_couple_stress()

        # u-gradient: sum_j adj_div_j sigma_ij for each i.
        # sigma shape (nx, ny, nz, i=3, j=3); treat as (i-indexed) x (j-indexed) gradient field.
        dE_du = np.zeros_like(self.u)
        for i in range(3):
            # For each i, pass sigma[..., i, :] (shape (..., 3)) through adjoint divergence.
            dE_du[..., i] = adjoint_tetrahedral_divergence(sigma[..., i, :]) / self.dx

        # omega-gradient: two contributions.
        # (a) From epsilon path: -eps_ijk sigma_ij contracts with levi-civita on (i,j) for each k.
        # cross_k = sum_{ij} eps_ijk * sigma_ij. For standard eps_ijk with eps_123 = 1:
        #   eps_123 sigma_12 + eps_132 sigma_13 + eps_213 sigma_21 + eps_231 sigma_23
        #   + eps_312 sigma_31 + eps_321 sigma_32 all give contributions to cross_k.
        cross = np.zeros_like(self.omega)
        cross[..., 0] = sigma[..., 1, 2] - sigma[..., 2, 1]
        cross[..., 1] = sigma[..., 2, 0] - sigma[..., 0, 2]
        cross[..., 2] = sigma[..., 0, 1] - sigma[..., 1, 0]

        # (b) From kappa path: sum_j adj_div_j couple_kj for each k.
        dE_from_kappa = np.zeros_like(self.omega)
        for k in range(3):
            dE_from_kappa[..., k] = adjoint_tetrahedral_divergence(couple[..., k, :]) / self.dx

        dE_dw = -cross + dE_from_kappa

        # Mask out dead nodes.
        alive = self.mask_alive[..., None].astype(dE_du.dtype)
        return dE_du * alive, dE_dw * alive

    # ------------------------------------------------------------------
    # Gradient-descent relaxation
    # ------------------------------------------------------------------

    def relax_step(self, learning_rate: float = 0.01) -> float:
        """
        One gradient-descent update. Returns the total energy BEFORE the step.
        """
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
        """
        Gradient descent with adaptive learning rate (backtracking).

        Terminates when either max_iter is reached, or the relative energy
        change between steps drops below tol.

        Returns a dict with keys: 'iterations', 'final_energy', 'converged',
        'energy_history' (list of E at each step), 'lr_final'.
        """
        lr = initial_lr
        history = []
        E_prev = self.total_energy()
        history.append(E_prev)

        for step in range(max_iter):
            u_save = self.u.copy()
            w_save = self.omega.copy()
            self.relax_step(lr)
            E_new = self.total_energy()

            if E_new < E_prev - 1e-15:
                # Accepted: try to increase lr modestly next time.
                rel_change = abs(E_new - E_prev) / max(abs(E_prev), 1e-12)
                history.append(E_new)
                if verbose and step % 10 == 0:
                    print(f"  step {step:4d}  E = {E_new:.6f}  lr = {lr:.2e}  drel = {rel_change:.2e}")
                if rel_change < tol:
                    return {
                        "iterations": step + 1,
                        "final_energy": E_new,
                        "converged": True,
                        "energy_history": history,
                        "lr_final": lr,
                    }
                lr = min(lr * 1.1, 1.0)
                E_prev = E_new
            else:
                # Reject: roll back, shrink lr.
                self.u = u_save
                self.omega = w_save
                lr *= 0.5
                if lr < 1e-12:
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
    # Diagnostics
    # ------------------------------------------------------------------

    def extract_shell_radii(self) -> tuple[float, float]:
        """
        Extract (R, r) — the toroidal-shell major and minor radii of the
        current omega field — from the intensity distribution of |omega|.

        Major radius R: radial location of peak |omega| in the xy plane at z=0.
        Minor radius r: FWHM of |omega| in the transverse direction.
        """
        omega_mag = np.sqrt(np.sum(self.omega**2, axis=-1))
        cx, cy, cz = (self.nx - 1) / 2.0, (self.ny - 1) / 2.0, (self.nz - 1) / 2.0
        kz = int(round(cz))

        slice_z = omega_mag[:, :, kz]
        xs = self._i[:, :, kz] - cx
        ys = self._j[:, :, kz] - cy
        rho = np.sqrt(xs**2 + ys**2)

        # Radial profile: sum |omega| around each rho bin.
        rho_flat = rho.flatten()
        mag_flat = slice_z.flatten()
        rho_max = rho.max()
        n_bins = max(8, int(round(rho_max)))
        edges = np.linspace(0.0, rho_max, n_bins + 1)
        hist, _ = np.histogram(rho_flat, bins=edges, weights=mag_flat)
        counts, _ = np.histogram(rho_flat, bins=edges)
        with np.errstate(divide="ignore", invalid="ignore"):
            profile = np.where(counts > 0, hist / np.maximum(counts, 1), 0.0)
        centers = 0.5 * (edges[:-1] + edges[1:])

        R = float(centers[np.argmax(profile)])

        # Minor radius: FWHM of the profile in the physical length r.
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
        """
        Estimate c by integrating the azimuthal phase gradient around the
        z-axis at the peak radial location. Uses the in-plane projection of
        omega for a minimal, Op11-like contour integral.

        Returns the absolute rounded integer winding number along the major
        cycle, which for the (2,q) torus-knot ladder equals c (= q) when the
        initialization convention is preserved through relaxation.
        """
        cx, cy, cz = (self.nx - 1) / 2.0, (self.ny - 1) / 2.0, (self.nz - 1) / 2.0
        kz = int(round(cz))
        R_found, _ = self.extract_shell_radii()

        n_theta = 64
        thetas = np.linspace(0.0, 2.0 * np.pi, n_theta, endpoint=False)
        dx_samples = cx + R_found * np.cos(thetas)
        dy_samples = cy + R_found * np.sin(thetas)

        # Trilinear-sample omega_x, omega_y along the major circle at z = 0.
        def sample(comp: int) -> np.ndarray:
            ix = np.clip(dx_samples.astype(int), 0, self.nx - 2)
            iy = np.clip(dy_samples.astype(int), 0, self.ny - 2)
            fx = dx_samples - ix
            fy = dy_samples - iy
            v00 = self.omega[ix, iy, kz, comp]
            v10 = self.omega[ix + 1, iy, kz, comp]
            v01 = self.omega[ix, iy + 1, kz, comp]
            v11 = self.omega[ix + 1, iy + 1, kz, comp]
            return (1 - fx) * (1 - fy) * v00 + fx * (1 - fy) * v10 + (1 - fx) * fy * v01 + fx * fy * v11

        ox = sample(0)
        oy = sample(1)
        phi = np.arctan2(oy, ox)
        unwrapped = np.unwrap(phi)
        total_winding = (unwrapped[-1] - unwrapped[0] + (phi[0] - unwrapped[0])) / (2.0 * np.pi)
        return int(round(abs(total_winding)))

    def extract_quality_factor(self) -> float:
        """
        Q-factor from Ch 8 multipole decomposition evaluated on the current
        shell geometry: Q = 16 pi^3 (R r) + 4 pi^2 (R r) + pi * d.

        With d = 1, Q collapses to 4 pi^3 + pi^2 + pi ~= 137.036 at the
        Golden-Torus radii (R, r) = (phi/2, (phi-1)/2).
        """
        R, r = self.extract_shell_radii()
        d = 1.0
        return 16.0 * np.pi**3 * (R * r) + 4.0 * np.pi**2 * (R * r) + np.pi * d
