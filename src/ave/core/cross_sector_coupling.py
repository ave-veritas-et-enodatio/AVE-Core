"""
Cross-sector coupling primitives — canonical engine layer
=========================================================

Unifies the conserved gyrotropic (CrystalEngine ADD-2) and trilinear buckle
(CrystalGraft v4) couplings for use across engine classes (coupled K4⊗Cosserat,
Master Equation + Cosserat FDTD, crystal graft family).

A44 adjudication (Grant 2026-06-09, recorded in crystal_engine.py): the
shear→bulk converter is an **Axiom-1 non-centrosymmetry consequence** —
engine-completeness, not a new postulate. κ̃ = pq/(p+q) = 6/5 is α-free.

Pre-reg: research/2026-06-12_cross-sector-engine-integration_prereg_FROZEN.md
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import R_II

# (2,3) torus-knot topological coupling — α-free (NOT κ_chiral = 1.2α).
KAPPA_TILDE: float = 6.0 / 5.0


def curl_central(F: np.ndarray, dx: float) -> np.ndarray:
    """∇×F for a 3-vector field (central differences, periodic via roll)."""
    Fx, Fy, Fz = F[..., 0], F[..., 1], F[..., 2]

    def d(a: np.ndarray, axis: int) -> np.ndarray:
        return (np.roll(a, -1, axis=axis) - np.roll(a, 1, axis=axis)) / (2.0 * dx)

    cx = d(Fz, 1) - d(Fy, 2)
    cy = d(Fx, 2) - d(Fz, 0)
    cz = d(Fy, 0) - d(Fx, 1)
    return np.stack([cx, cy, cz], axis=-1)


def microrotation_x(w: np.ndarray, dx: float) -> np.ndarray:
    """(∇×w)·x̂ — parity-odd helicity carrier for gyrotropic coupling."""
    c = curl_central(w, dx)
    return c[..., 0]


def saturation_front_window(
    A: np.ndarray,
    *,
    center: float = R_II,
    width: float = 0.18,
) -> np.ndarray:
    """g_front(A): thin shell at the Non-Linear→Saturated boundary (CP10)."""
    return np.exp(-((A - center) ** 2) / (2.0 * width**2))


def combined_strain_amplitude(
    V_sq: np.ndarray,
    A_cos_sq: np.ndarray,
    V_snap: float,
) -> np.ndarray:
    """Total dimensionless strain A for front localization (K4 + Cosserat)."""
    A_k4 = np.sqrt(np.maximum(V_sq, 0.0)) / V_snap
    A_cos = np.sqrt(np.maximum(A_cos_sq, 0.0))
    return np.minimum(np.sqrt(A_k4 * A_k4 + A_cos * A_cos), 1.0 - 1e-12)


def gyrotropic_converter_forces(
    V: np.ndarray,
    w: np.ndarray,
    g_front: np.ndarray,
    dx: float,
    *,
    kappa_tilde: float = KAPPA_TILDE,
) -> tuple[np.ndarray, np.ndarray]:
    """Hamiltonian gyrotropic shear↔bulk coupling (CrystalEngine ADD-2).

    H_couple = κ̃ ∫ g V Ω_w d³r,  Ω_w = (∇×w)·x̂

    Returns (f_V, f_w) acceleration contributions:
        f_V = −κ̃ g Ω_w          (sources bulk even at V≡0 if g, Ω_w ≠ 0)
        f_w_y = −κ̃ ∂_z(gV), f_w_z = +κ̃ ∂_y(gV)
    """
    Omega_w = microrotation_x(w, dx)
    f_V = -kappa_tilde * g_front * Omega_w
    gV = g_front * V
    d_gV_dy = (np.roll(gV, -1, 1) - np.roll(gV, 1, 1)) / (2.0 * dx)
    d_gV_dz = (np.roll(gV, -1, 2) - np.roll(gV, 1, 2)) / (2.0 * dx)
    f_w = np.zeros_like(w)
    f_w[..., 1] = -kappa_tilde * d_gV_dz
    f_w[..., 2] = +kappa_tilde * d_gV_dy
    return f_V, f_w


def gyrotropic_coupling_energy(
    V: np.ndarray,
    w: np.ndarray,
    g_front: np.ndarray,
    dx: float,
    *,
    kappa_tilde: float = KAPPA_TILDE,
    mask: np.ndarray | None = None,
) -> float:
    """H_couple = κ̃ ∫ g V Ω_w d³r."""
    Omega_w = microrotation_x(w, dx)
    dens = kappa_tilde * g_front * V * Omega_w
    if mask is not None:
        dens = dens * mask
    return float(dens.sum())


def trilinear_buckle_forces(
    V: np.ndarray,
    w: np.ndarray,
    omega: np.ndarray,
    g_wall: np.ndarray,
    dx: float,
    *,
    kappa_tilde: float = KAPPA_TILDE,
    photon_deplete: bool = False,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Conserved trilinear buckle (CrystalGraft v4, photon director = w).

    H = κ̃ ∫ g V [w·(∇×ω)] d³r

        f_V    = −κ̃ g (w·∇×ω)
        f_ω    = −κ̃ ∇×(g V w)
        f_w    = −κ̃ g V (∇×ω)   [only if photon_deplete=True — indefinite H arm]

    Default photon_deplete=False: w is a bounded chiral director (stable).
    """
    curl_omega = curl_central(omega, dx)
    w_dot_curl = np.sum(w * curl_omega, axis=-1)
    f_V = -kappa_tilde * g_wall * w_dot_curl
    A_vec = (g_wall * V)[..., None] * w
    f_omega = -kappa_tilde * curl_central(A_vec, dx)
    if photon_deplete:
        f_w = -kappa_tilde * (g_wall * V)[..., None] * curl_omega
    else:
        f_w = np.zeros_like(w)
    return f_V, f_w, f_omega


def trilinear_coupling_energy(
    V: np.ndarray,
    w: np.ndarray,
    omega: np.ndarray,
    g_wall: np.ndarray,
    dx: float,
    *,
    kappa_tilde: float = KAPPA_TILDE,
    mask: np.ndarray | None = None,
) -> float:
    """H_couple = κ̃ ∫ g V [w·(∇×ω)] d³r."""
    curl_omega = curl_central(omega, dx)
    dens = kappa_tilde * g_wall * V * np.sum(w * curl_omega, axis=-1)
    if mask is not None:
        dens = dens * mask
    return float(dens.sum())


def distribute_scalar_to_k4_ports(
    f_scalar: np.ndarray,
    n_ports: int = 4,
    mask: np.ndarray | None = None,
) -> np.ndarray:
    """Map per-site scalar bulk force to equal per-port K4 injection."""
    out = np.broadcast_to(f_scalar[..., None], (*f_scalar.shape, n_ports)).copy()
    out /= float(n_ports)
    if mask is not None:
        out = out * mask[..., None]
    return out


def scale_cosserat_to_front(
    u: np.ndarray,
    omega: np.ndarray,
    A_cos_sq: np.ndarray,
    *,
    target: float = R_II,
) -> tuple[np.ndarray, np.ndarray]:
    """Scale (u, ω) UP to the converter front when below target — never shrink.

    Shrinking a high-amplitude photon seed (genesis-23 A_LOCK≫R_II) would kill
    the cross-sector coupling strength."""
    A_max = float(np.sqrt(np.max(A_cos_sq)))
    if A_max < 1e-12 or A_max >= target:
        return u, omega
    scale = target / A_max
    return u * scale, omega * scale


def normalize_cosserat_amplitude(
    u: np.ndarray,
    omega: np.ndarray,
    A_cos_sq: np.ndarray,
    *,
    target: float,
) -> tuple[np.ndarray, np.ndarray, float]:
    """Scale (u, ω) to place peak Cosserat strain at a canon landmark (bidirectional).

    Used for regime placement (e.g. D-lite ``A_yield = √α``) — not an ``a_lock`` sweep."""
    A_max = float(np.sqrt(np.max(A_cos_sq)))
    if A_max < 1e-12:
        return u, omega, 0.0
    scale = float(target) / A_max
    return u * scale, omega * scale, A_max


def effective_shear_director(
    u: np.ndarray,
    omega: np.ndarray,
    omega_dot: np.ndarray,
    *,
    u_floor: float = 1e-14,
) -> np.ndarray:
    """Shear director w for trilinear coupling.

    Crystal graft carries w as an explicit photon field. Genesis-23 / Cosserat
    photon IC sets u=0 and seeds (ω, ω̇) as the LC pair — use ω̇ as the
    transverse director proxy when |u|≈0 so f_V = −κ̃ g (w·∇×ω) can fire.
    """
    if float(np.max(np.abs(u))) > u_floor * max(float(np.max(np.abs(omega))), 1.0):
        return u
    return omega_dot


def v_scalar_from_v_inc(V_inc: np.ndarray) -> np.ndarray:
    """Signed bulk scalar proxy from K4 port voltages (RMS magnitude × mean sign)."""
    v_sq = np.sum(V_inc**2, axis=-1)
    v_rms = np.sqrt(np.maximum(v_sq, 0.0))
    port_mean = np.mean(V_inc, axis=-1)
    sign = np.sign(port_mean)
    sign = np.where(np.abs(port_mean) < 1e-30, 1.0, sign)
    return v_rms * sign
