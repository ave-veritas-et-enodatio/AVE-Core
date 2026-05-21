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

References: research/_archive/L3_electron_soliton/02_, 03_, 04_, 07_, 08_, 09_.

Q-G47 SUBSTRATE-SCALE CLOSURE (Sessions 9-18, 2026-05-15 evening):
This module implements the continuous Cosserat micropolar field whose
substrate-scale instance of A-034 (Universal Saturation-Kernel Strain-Snap
Mechanism) defines the K4 lattice's magic-angle operating point. Key
axiom-level relations (per Q-G47 Session 17):

  μ + κ = ξ_K1 · T_EM            (Cauchy + micropolar moduli, [Pa])
  β + γ = ξ_K2 · T_EM · ℓ_node²  (couple-stress moduli, [N])
  ℓ_c² = (β + γ) / [2(μ + κ)]    (Cosserat char length, Eringen 1966)
  ξ_K2 / ξ_K1 = 12               (K4-symmetry-forced via |T|=12 universality)
  ℓ_c / ℓ_node ≈ √6              (substrate's saturation-boundary scale)

NAMESPACE: ξ_K1, ξ_K2 are SUBSTRATE-scale O(1) Cosserat prefactors —
DISTINCT from Vol 3 Ch 1's Machian ξ = 4π(R_H/ℓ_node)α⁻² (~10⁴³, cosmological
scope, same letter). Explicitly de-collided in
ave-kb/common/xi-topo-traceability.md.

CONTINUOUS-FIELD reading (per Grant 2026-05-15 "the springs are continuous"):
this module operates in the continuous-field regime; the K4 lattice is a
sampling structure, not the physics. Sessions 12-15 discrete-bond scaffolds
(scripts/verify/q_g47_session12/14/15_*.py) are sanity-check discretizations.

A-034 cross-refs: `manuscript/backmatter/07_universal_saturation_kernel.tex`
(catalog, canonical) + `manuscript/ave-kb/common/q-g47-substrate-scale-cosserat-closure.md`
(KB synthesis for Q-G47 Sessions 1-18 substrate-scale closure including
|T|=12 universality + ξ_K1, ξ_K2 namespace).
"""

from __future__ import annotations

import jax

jax.config.update("jax_enable_x64", True)

import jax.numpy as jnp  # noqa: E402
import numpy as np  # noqa: E402

from ave.core.constants import ALPHA  # noqa: E402

# ─────────────────────────────────────────────────────────────────────────
# Phase 4 asymmetric-saturation chirality coupling
# ─────────────────────────────────────────────────────────────────────────
# Structure per [doc 20_ Sub-Theorem 3.1.1](research/_archive/L3_electron_soliton/
# 20_chirality_projection_sub_theorem.md):
#
#   κ_chiral = α · κ̃    where κ̃ = (p·q) / (p+q)  for (p,q) torus winding
#
# The dimensionless topological factor κ̃ is purely geometric — derived from
# the (p,q) torus knot winding numbers, INDEPENDENT of α. The α prefactor
# is the calibration input. This separation matters for emergence testing:
# if the chiral LC substrate's K(p)/G(p) curve crosses K/G=2 at a packing
# fraction p_c that is a pure dimensionless multiple of α (specifically
# p_c/α = 8π per Axiom 4 framing), then the "8π" emerges from substrate
# physics with κ̃ as topological input — α anchors the absolute scale.
#
# For the electron (2,3) winding:  κ̃ = 2·3/(2+3) = 6/5 = 1.2
# For the (1,1) Beltrami:           κ̃ = 1·1/(1+1) = 1/2 = 0.5
#
# Verified vs canonical Hopf-coil chirality table empirical benchmark
# (held in separate propulsion engineering compendium).
# Not a free parameter — parallel-channel impedance combination at TIR
# boundary; the (p,q) topology determines κ̃, α determines absolute scale.
#
# Refactored 2026-05-02 to expose κ̃ as separate dimensionless constant for
# emergence testing per doc 108 §11.5 + Grant directive 2026-05-02:
# "p_c is where the chiral LC vacuum hits K/G=2."

# Dimensionless topological factor for the (p,q) torus winding.
# For electron (2,3): pq/(p+q) = 6/5 = 1.2.
# This is INDEPENDENT of α — purely geometric / topological.
KAPPA_TILDE_ELECTRON: float = 6.0 / 5.0  # = 1.2 (electron (2,3) winding)
KAPPA_TILDE_BELTRAMI_11: float = 1.0 / 2.0  # = 0.5 ((1,1) Beltrami)


def kappa_tilde_torus(p: int, q: int) -> float:
    """Dimensionless topological factor κ̃ = pq/(p+q) for (p,q) torus knot.

    Independent of α and any CODATA value. Pure topological/geometric input.
    Use as the substrate-physics-native chiral coupling parameter for
    emergence testing where α should NOT be an input.

    Args:
        p, q: torus winding numbers (e.g., p=2, q=3 for electron)
    Returns:
        κ̃ = pq/(p+q) — dimensionless, geometric.
    """
    if p + q == 0:
        raise ValueError(f"kappa_tilde_torus: p+q must be nonzero, got p={p}, q={q}")
    return float(p * q) / float(p + q)


def kappa_chiral_from_topology(p: int, q: int, alpha: float = ALPHA) -> float:
    """Total chiral coupling κ_chiral = α · κ̃(p,q) for (p,q) torus knot.

    Args:
        p, q: torus winding numbers
        alpha: calibration input (default: CODATA α from constants module)
    Returns:
        κ_chiral with units matching α (dimensionless).
    """
    return float(alpha) * kappa_tilde_torus(p, q)


# Total chiral coupling for the electron (2,3) winding.
# Numerically identical to prior `1.2 * ALPHA` (≈ 8.757e-3) but structure
# now exposed: KAPPA_CHIRAL_ELECTRON = ALPHA × KAPPA_TILDE_ELECTRON, where
# the topological factor is separable from the calibration input.
KAPPA_CHIRAL_ELECTRON: float = ALPHA * KAPPA_TILDE_ELECTRON  # ≈ 8.757e-3


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


def _project_omega_to_nhat(omega: jnp.ndarray) -> jnp.ndarray:
    """Rodrigues projection omega -> n_hat = R(omega) * z_hat.

    Uses quaternion form: q0 = cos(|omega|/2),  q_vec = omega * sin(|omega|/2) / |omega|.
    Then n_hat = R(q) * (0,0,1) = (2(q1 q3 + q0 q2), 2(q2 q3 - q0 q1), 1 - 2(q1^2 + q2^2)).

    Vacuum sites (omega ~ 0) need the JAX double-where pattern: jnp.sqrt has
    an undefined gradient at 0, so we compute sqrt on a safe input and
    re-select the true value afterward.
    """
    omega_sq = jnp.sum(omega * omega, axis=-1)
    eps = 1e-20
    is_positive = omega_sq > eps
    safe_sq = jnp.where(is_positive, omega_sq, 1.0)
    safe_norm = jnp.sqrt(safe_sq)
    omega_norm = jnp.where(is_positive, safe_norm, 0.0)
    half_theta = 0.5 * omega_norm
    cos_half = jnp.cos(half_theta)
    # sin(theta/2) / theta = (1/2) * sinc(theta/(2*pi)) where jnp.sinc(y) = sin(pi*y)/(pi*y)
    # sinc is smooth at 0, so this branch is autograd-safe.
    sin_half_over_norm = 0.5 * jnp.sinc(omega_norm / (2.0 * jnp.pi))
    q_vec = omega * sin_half_over_norm[..., None]
    q1 = q_vec[..., 0]
    q2 = q_vec[..., 1]
    q3 = q_vec[..., 2]
    n_x = 2.0 * (q1 * q3 + cos_half * q2)
    n_y = 2.0 * (q2 * q3 - cos_half * q1)
    n_z = 1.0 - 2.0 * (q1 * q1 + q2 * q2)
    return jnp.stack([n_x, n_y, n_z], axis=-1)


def _op10_density(omega: jnp.ndarray, dx: float) -> jnp.ndarray:
    """AVE Op10 continuum Lagrangian density.

    Gauss's-law / magnetic-energy reading (see research/_archive/L3_electron_soliton/11_):
    L_Op10 = W_4 = sum_{i<j} |d_i n_hat ^ d_j n_hat|^2
                = (1/2) * [(tr G)^2 - ||G||_F^2]
    where G_ij = d_i n_hat . d_j n_hat. Coefficient k = 1 under the
    Z_0 = 1 magnetic-energy reading. n_hat derived from omega via Rodrigues.
    """
    n_hat = _project_omega_to_nhat(omega)
    grad_n = _tetrahedral_gradient(n_hat) / dx  # shape (nx,ny,nz,3,3), [..., comp, spatial]
    # G_ij = d_i n . d_j n = sum_a grad_n[...,a,i] * grad_n[...,a,j]
    G = jnp.einsum("...ai,...aj->...ij", grad_n, grad_n)
    diag = jnp.diagonal(G, axis1=-2, axis2=-1)
    tr_G = jnp.sum(diag, axis=-1)
    sq_G = jnp.sum(G * G, axis=(-2, -1))
    W4 = 0.5 * (tr_G * tr_G - sq_G)
    return W4


def _hopf_density(omega: jnp.ndarray, dx: float) -> jnp.ndarray:
    """AVE Hopf / Chern-Simons self-inductance density (research/_archive/L3_electron_soliton/13_).

    The Hopf 2-form F_ij = n_hat . (d_i n_hat x d_j n_hat) has a dual magnetic
    field B_k = (1/2) eps_kij F_ij. Its gauge potential A in Coulomb gauge
    (grad . A = 0) is obtained by FFT-based inverse curl:

        A_hat(k) = i (k x B_hat(k)) / |k|^2   (zero-mode fixed to 0)

    The Chern-Simons 3-form density is (1/2) A . B. Its integral over space
    equals (up to normalization) the Hopf invariant times 4*pi^2 — a
    topological quantity that survives field-superposition cancellation.

    This captures the "self-inductance of each flux contribution" physics
    identified by the AVE-HOPF sibling repo (hopf_01_classical_coupling.py):
    topological linking energy that doesn't vanish when net B cancels.
    """
    n_hat = _project_omega_to_nhat(omega)
    grad_n = _tetrahedral_gradient(n_hat) / dx  # (nx,ny,nz,3,3) [comp, spatial]
    # F_ij = n . (d_i n x d_j n) = eps_abc n_a (d_i n_b)(d_j n_c)
    # Efficient form via Levi-Civita:
    # F_ij = n . (grad_n[:,i] x grad_n[:,j])
    di_n = jnp.moveaxis(grad_n, -1, 0)  # (3, nx, ny, nz, 3) — spatial first
    # cross_{ij} = di_n[i] x di_n[j], shape (3, 3, nx, ny, nz, 3)
    # F_ij = n_hat . cross_{ij}
    # Compute F as a skew-symmetric 3x3 tensor over spatial indices.
    # For a compact implementation, loop over the 3 distinct ij pairs.
    F01 = jnp.sum(n_hat * jnp.cross(di_n[0], di_n[1], axis=-1), axis=-1)
    F02 = jnp.sum(n_hat * jnp.cross(di_n[0], di_n[2], axis=-1), axis=-1)
    F12 = jnp.sum(n_hat * jnp.cross(di_n[1], di_n[2], axis=-1), axis=-1)
    # Dual B_k = (1/2) eps_kij F_ij:
    # B_0 = F_12, B_1 = -F_02, B_2 = F_01
    B = jnp.stack([F12, -F02, F01], axis=-1)  # (nx, ny, nz, 3)

    # FFT-based inverse curl in Coulomb gauge:
    # A_hat(k) = i (k x B_hat(k)) / |k|^2,  with A_hat(0) = 0.
    nx, ny, nz = B.shape[:3]
    kx = jnp.fft.fftfreq(nx, d=dx) * (2.0 * jnp.pi)
    ky = jnp.fft.fftfreq(ny, d=dx) * (2.0 * jnp.pi)
    kz = jnp.fft.fftfreq(nz, d=dx) * (2.0 * jnp.pi)
    KX, KY, KZ = jnp.meshgrid(kx, ky, kz, indexing="ij")
    K2 = KX * KX + KY * KY + KZ * KZ
    # Zero-mode safety: replace K2=0 with 1 for the division, then zero the
    # result at that point to enforce A_hat(0) = 0.
    K2_safe = jnp.where(K2 > 0, K2, 1.0)
    zero_mask = (K2 > 0).astype(B.dtype)

    B_hat = jnp.fft.fftn(B, axes=(0, 1, 2))
    # (k x B)_x = ky*Bz - kz*By, etc.
    kB_x = KY * B_hat[..., 2] - KZ * B_hat[..., 1]
    kB_y = KZ * B_hat[..., 0] - KX * B_hat[..., 2]
    kB_z = KX * B_hat[..., 1] - KY * B_hat[..., 0]
    A_hat_x = 1j * kB_x / K2_safe * zero_mask
    A_hat_y = 1j * kB_y / K2_safe * zero_mask
    A_hat_z = 1j * kB_z / K2_safe * zero_mask
    A_x = jnp.fft.ifftn(A_hat_x, axes=(0, 1, 2)).real
    A_y = jnp.fft.ifftn(A_hat_y, axes=(0, 1, 2)).real
    A_z = jnp.fft.ifftn(A_hat_z, axes=(0, 1, 2)).real
    A = jnp.stack([A_x, A_y, A_z], axis=-1)  # (nx, ny, nz, 3)

    # Hopf / Chern-Simons density: (1/2) A . B.
    # Integrated over space, equals (up to 4*pi^2) the Hopf invariant Q_H.
    return 0.5 * jnp.sum(A * B, axis=-1)


def _s11_density(
    u: jnp.ndarray,
    omega: jnp.ndarray,
    dx: float,
    omega_yield: float,
    epsilon_yield: float,
) -> jnp.ndarray:
    """AVE field-level S11 density via composition of Op2, Op14, Op3 pointwise.

    Per the reframing in L3_PHASE3_SESSION_20260420 handoff:
        omega -> strain/curvature -> A^2 -> S (Op2) -> Z_eff (Op14) ->
        Gamma_local to each tetrahedral neighbor (Op3)
        S11_density(x) = sum_k |Gamma_{x, neighbor_k}|^2

    Integrated over the alive-mask, this IS the field-level S11 objective.
    Unlike |grad S|^2/S^2, this is bounded in [0, 4] per site (since each
    |Gamma|^2 <= 1 and there are 4 tetrahedral neighbors), pointwise
    differentiable, and corresponds directly to Op3 applied at the lattice.

    At perfect impedance match (Z_eff = Z_0 uniformly, i.e., vacuum), S11 = 0.
    Minimizing over omega subject to the topological sector c = 3 constraint
    selects the configuration whose boundary impedance matches the bulk.
    """
    eps = _compute_strain(u, omega, dx)
    kappa = _compute_curvature(omega, dx)
    eps_sq = jnp.sum(eps * eps, axis=(-1, -2))
    kappa_sq = jnp.sum(kappa * kappa, axis=(-1, -2))
    A_sq = eps_sq / (epsilon_yield * epsilon_yield) + kappa_sq / (omega_yield * omega_yield)
    A_sq_clipped = jnp.clip(A_sq, 0.0, 1.0 - 1e-10)
    S = jnp.sqrt(1.0 - A_sq_clipped)  # Op2 saturation, (nx, ny, nz)
    # Op14 dynamic impedance Z_eff = Z_0 / sqrt(S), with Z_0 = 1 per `10_`
    S_safe = jnp.maximum(S, 1e-6)
    Z_eff = 1.0 / jnp.sqrt(S_safe)

    # Op3 reflection coefficient to each of the 4 tetrahedral neighbors
    gamma_sq_total = jnp.zeros_like(Z_eff)
    for p in TETRA_OFFSETS:
        Z_neighbor = jnp.roll(Z_eff, shift=(-p[0], -p[1], -p[2]), axis=(0, 1, 2))
        gamma = (Z_neighbor - Z_eff) / (Z_neighbor + Z_eff + 1e-12)
        gamma_sq_total = gamma_sq_total + gamma * gamma
    return gamma_sq_total


def _total_s11(u, omega, mask_alive, dx, omega_yield, epsilon_yield):
    rho = _s11_density(u, omega, dx, omega_yield, epsilon_yield)
    return jnp.sum(rho * mask_alive.astype(rho.dtype))


def _reflection_density(
    u: jnp.ndarray,
    omega: jnp.ndarray,
    dx: float,
    omega_yield: float,
    epsilon_yield: float,
) -> jnp.ndarray:
    """AVE Op9-via-Op3 reflection energy density (research/_archive/L3_electron_soliton/12_).

    Chain: local strain amplitude A -> saturation S -> impedance Z_eff -> Gamma.
        A^2 = |eps|^2/eps_yield^2 + |kappa|^2/omega_yield^2
        S = sqrt(1 - A^2)  (clipped to [eps, 1])
        Z_eff / Z_0 = 1/S^(1/4)   (Op14)
        grad ln(Z_eff) = -(1/4) grad ln(S) = -(1/(4 S)) grad S
        Gamma  ~ (1/2) grad ln(Z_eff) = -(1/(8 S)) grad S    (continuum Op3)
        Gamma^2 = (1/64) |grad S|^2 / S^2

    Op3 reflection-power density, with the explicit 1/64 factor from the
    chain (not bundled into k_refl):

        L_reflection = (1/64) * |grad S|^2 / (S^2 + eps_reg)

    Vanishes in vacuum (S -> 1, grad S -> 0). Diverges at yield (S -> 0)
    unless regularized — the Pauli wall structure from the atomic solver
    (universal_pairwise_energy) recast at the field scale.
    """
    eps = _compute_strain(u, omega, dx)
    kappa = _compute_curvature(omega, dx)
    eps_sq = jnp.sum(eps * eps, axis=(-1, -2))
    kappa_sq = jnp.sum(kappa * kappa, axis=(-1, -2))
    A_sq = eps_sq / (epsilon_yield * epsilon_yield) + kappa_sq / (omega_yield * omega_yield)
    A_sq_clipped = jnp.clip(A_sq, 0.0, 1.0 - 1e-10)
    S = jnp.sqrt(1.0 - A_sq_clipped)  # scalar (nx,ny,nz), in (0, 1]
    # Gradient of S via tetrahedral operator on a scalar.
    # _tetrahedral_gradient expects a trailing vector dim; wrap scalar in a length-1.
    grad_S = _tetrahedral_gradient(S[..., None])[..., 0, :] / dx  # (nx,ny,nz,3)
    grad_S_sq = jnp.sum(grad_S * grad_S, axis=-1)  # (nx,ny,nz)
    # Regularize 1/S^2 to avoid divergence at exact yield (autograd safety).
    eps_reg = 1e-6
    # 1/64 factor is the explicit Gamma^2 coefficient from the continuum chain
    # (research/_archive/L3_electron_soliton/12_ §3.4-3.5). Not a fit parameter.
    reflection = (1.0 / 64.0) * grad_S_sq / (S * S + eps_reg)
    return reflection


# ─────────────────────────────────────────────────────────────────────
# Phase 4 — Asymmetric μ/ε saturation (Vol 1 Ch 7:252, doc 54_ §6)
# ─────────────────────────────────────────────────────────────────────
# S1 gate reopened 2026-04-23. Replaces the single-kernel symmetric
# saturation S = √(1-A²_total) with two independent tracks (S_μ, S_ε)
# biased by the local Beltrami helicity of the Cosserat ω field.
#
# Physical picture (EE-native):
#   Each K4 node is a 4-port LC tank with BOTH a nonlinear varactor
#   C_eff(V) = C_0/√(1-(V/V_yield)²) and a nonlinear varinductor
#   L_eff(I) = L_0/√(1-(I/I_max)²) per Vol 4 Ch 1:127-187. The current
#   engine collapsed these into a single S kernel (symmetric / Vol 4
#   Ch 11 Achromatic Impedance Lens — gravity regime). Phase 4 exposes
#   them as separate tracks; chirality-biased drive saturates μ vs ε
#   at different rates (Meissner-like), driving Z_eff = Z_0·√(S_μ/S_ε)
#   to 0 or ∞ per Vol 1 Ch 7:252.
#
# Regression (per 3c):
#   - Symmetric case (h_local = 0 under linear-polarization drive):
#     A²_μ_base = A²_ε_base → S_μ = S_ε → Z_eff = Z_0 constant
#     (Achromatic Lens; differs from single-kernel form which had Z
#     scale with A²_total). The single-kernel behavior was a
#     simplification, not axiom-faithful.
#   - Asymmetric case (h_local ≠ 0 under circularly-polarized drive):
#     A²_μ grows faster than A²_ε under RH drive → S_μ → 0 first →
#     Z_eff → 0 → Γ → -1 confinement wall forms.


def _tetrahedral_curl(omega: jnp.ndarray, dx: float) -> jnp.ndarray:
    """(∇×ω)_i = ε_ijk ∂_j ω_k on the K4 diamond lattice.

    Uses the same tetrahedral gradient operator as _compute_curvature.
    grad[..., i, j] = ∂_j ω_i (in natural lattice units), so curl
    components are:
        (curl ω)_0 = ∂_1 ω_2 − ∂_2 ω_1 = grad[..., 2, 1] − grad[..., 1, 2]
        (curl ω)_1 = ∂_2 ω_0 − ∂_0 ω_2 = grad[..., 0, 2] − grad[..., 2, 0]
        (curl ω)_2 = ∂_0 ω_1 − ∂_1 ω_0 = grad[..., 1, 0] − grad[..., 0, 1]

    Returns (nx, ny, nz, 3) with components in rad / ℓ_node (natural units).
    """
    grad = _tetrahedral_gradient(omega) / dx  # (nx, ny, nz, 3, 3)
    curl_x = grad[..., 2, 1] - grad[..., 1, 2]
    curl_y = grad[..., 0, 2] - grad[..., 2, 0]
    curl_z = grad[..., 1, 0] - grad[..., 0, 1]
    return jnp.stack([curl_x, curl_y, curl_z], axis=-1)


def _beltrami_helicity(omega: jnp.ndarray, dx: float) -> jnp.ndarray:
    """Normalized Beltrami helicity h_local = ω·(∇×ω) / (|ω|·|∇×ω|).

    Per doc 54_ §6 line 220, h_local ∈ [-1, +1] is the local handedness
    of the Cosserat microrotation field. h_local = +1 for right-handed
    Beltrami flow (ω parallel to ∇×ω), -1 for left-handed, 0 for
    non-helical (linear drive or ω = 0).

    Returns (nx, ny, nz) scalar field. Regularized with eps_h = 1e-12 to
    avoid 0/0 in vacuum sites.
    """
    curl = _tetrahedral_curl(omega, dx)
    dot_ω_curl = jnp.sum(omega * curl, axis=-1)  # (nx, ny, nz)
    omega_sq = jnp.sum(omega * omega, axis=-1)
    curl_sq = jnp.sum(curl * curl, axis=-1)
    eps_h = 1e-12
    # Regularized norms: sqrt(x² + eps²) is smooth at x=0
    norm_product = jnp.sqrt((omega_sq + eps_h) * (curl_sq + eps_h))
    return dot_ω_curl / norm_product


def _reflection_density_asymmetric(
    u: jnp.ndarray,
    omega: jnp.ndarray,
    V_sq: jnp.ndarray,
    dx: float,
    V_SNAP: float,
    omega_yield: float,
    epsilon_yield: float,
    kappa_chiral: float = KAPPA_CHIRAL_ELECTRON,
) -> jnp.ndarray:
    """Asymmetric μ/ε reflection density (Phase 4, doc 54_ §6).

    Splits the single Axiom-4 saturation kernel into two tracks:
        A²_μ_base = κ²/ω_yield²                       (rotational → magnetic)
        A²_ε_base = ε_sym²/ε_yield² + V²/V_SNAP²      (strain + K4 V → electric)
        h_local = Beltrami helicity of ω
        A²_μ = (1 + κ_chiral · h_local) · A²_μ_base
        A²_ε = (1 − κ_chiral · h_local) · A²_ε_base
        S_μ = √(1 − A²_μ),   S_ε = √(1 − A²_ε)

    Asymmetric impedance: Z_eff = Z_0·√(S_μ/S_ε)
    Reflection coefficient: Γ ≈ (1/2) ∇ln(Z_eff) per doc 54_ §6 Option II

        ∇ln(Z_eff) = (1/(2 S_μ)) ∇S_μ − (1/(2 S_ε)) ∇S_ε
        Γ ≈ (1/4) [∇S_μ/S_μ − ∇S_ε/S_ε]
        Γ² = (1/16) |∇S_μ/S_μ − ∇S_ε/S_ε|²

    Vanishes when S_μ = S_ε (symmetric case — Achromatic Impedance Lens,
    Vol 4 Ch 11; no confinement wall, just wave slowing). Diverges as
    S_μ → 0 with S_ε finite (Meissner asymmetric — Γ → -1 wall forms).

    V_sq: squared K4 voltage field (nx, ny, nz), already summed over ports.
    Returns (nx, ny, nz) reflection energy density.

    See VACUUM_ENGINE_MANUAL §17 A14 r6 + doc 50_ r3 §0.1 + doc 54_ §6.
    """
    eps = _compute_strain(u, omega, dx)
    eps_T = jnp.swapaxes(eps, -1, -2)
    eps_sym = 0.5 * (eps + eps_T)  # symmetric strain → electric sector
    kappa = _compute_curvature(omega, dx)  # curvature → magnetic sector

    eps_sym_sq = jnp.sum(eps_sym * eps_sym, axis=(-1, -2))
    kappa_sq = jnp.sum(kappa * kappa, axis=(-1, -2))

    # Base (isotropic) saturation contributions per doc 54_ §6 line 185-186
    A2_mu_base = kappa_sq / (omega_yield * omega_yield)
    A2_eps_base = eps_sym_sq / (epsilon_yield * epsilon_yield) + V_sq / (V_SNAP * V_SNAP)

    # Chirality bias per doc 54_ §6 line 218-219 (Form A — instantaneous;
    # h_local is a property of the current ω field, not an accumulator).
    h_local = _beltrami_helicity(omega, dx)
    A2_mu = (1.0 + kappa_chiral * h_local) * A2_mu_base
    A2_eps = (1.0 - kappa_chiral * h_local) * A2_eps_base

    # Clip to [0, 1-δ) for autograd safety past Regime IV boundary
    A2_mu_c = jnp.clip(A2_mu, 0.0, 1.0 - 1e-10)
    A2_eps_c = jnp.clip(A2_eps, 0.0, 1.0 - 1e-10)

    S_mu = jnp.sqrt(1.0 - A2_mu_c)
    S_eps = jnp.sqrt(1.0 - A2_eps_c)

    # ∇S_μ and ∇S_ε via tetrahedral gradient (same operator as symmetric
    # W_refl for consistency). Wrap scalars in length-1 vector, take the
    # gradient, strip the dummy axis.
    grad_S_mu = _tetrahedral_gradient(S_mu[..., None])[..., 0, :] / dx
    grad_S_eps = _tetrahedral_gradient(S_eps[..., None])[..., 0, :] / dx

    # Regularized 1/S to avoid autograd divergence at boundary
    eps_reg = 1e-6
    inv_S_mu = 1.0 / jnp.sqrt(S_mu * S_mu + eps_reg)
    inv_S_eps = 1.0 / jnp.sqrt(S_eps * S_eps + eps_reg)

    # Γ_vec = (1/4)[(∇S_μ / S_μ) − (∇S_ε / S_ε)]  per Option II
    gamma_vec = 0.25 * (grad_S_mu * inv_S_mu[..., None] - grad_S_eps * inv_S_eps[..., None])
    gamma_sq = jnp.sum(gamma_vec * gamma_vec, axis=-1)

    return gamma_sq


def _update_saturation_kernels(
    u: jnp.ndarray,
    omega: jnp.ndarray,
    V_sq: jnp.ndarray,
    dx: float,
    V_SNAP: float,
    omega_yield: float,
    epsilon_yield: float,
    kappa_chiral: float = KAPPA_CHIRAL_ELECTRON,
) -> tuple[jnp.ndarray, jnp.ndarray]:
    """Return (S_μ, S_ε) per-site saturation kernels for asymmetric form.

    Used by k4_cosserat_coupling._update_z_local_total to compute the
    asymmetric impedance Z_eff/Z_0 = √(S_μ/S_ε) per doc 54_ §6 line 194.

    Public helper so Phase 4 observers + coupling can share one code path
    (single source of truth for (S_μ, S_ε) across observer / coupling / test).

    Returns S_μ, S_ε each shape (nx, ny, nz), clipped to (δ, 1].
    """
    eps = _compute_strain(u, omega, dx)
    eps_T = jnp.swapaxes(eps, -1, -2)
    eps_sym = 0.5 * (eps + eps_T)
    kappa = _compute_curvature(omega, dx)

    eps_sym_sq = jnp.sum(eps_sym * eps_sym, axis=(-1, -2))
    kappa_sq = jnp.sum(kappa * kappa, axis=(-1, -2))

    A2_mu_base = kappa_sq / (omega_yield * omega_yield)
    A2_eps_base = eps_sym_sq / (epsilon_yield * epsilon_yield) + V_sq / (V_SNAP * V_SNAP)

    h_local = _beltrami_helicity(omega, dx)
    A2_mu = (1.0 + kappa_chiral * h_local) * A2_mu_base
    A2_eps = (1.0 - kappa_chiral * h_local) * A2_eps_base

    A2_mu_c = jnp.clip(A2_mu, 0.0, 1.0 - 1e-10)
    A2_eps_c = jnp.clip(A2_eps, 0.0, 1.0 - 1e-10)

    S_mu = jnp.sqrt(1.0 - A2_mu_c)
    S_eps = jnp.sqrt(1.0 - A2_eps_c)
    return S_mu, S_eps


def _energy_density_bare(
    u: jnp.ndarray,
    omega: jnp.ndarray,
    mask_alive: jnp.ndarray,
    dx: float,
    G: float,
    G_c: float,
    gamma: float,
    k_op10: float,
    k_refl: float,
    k_hopf: float,
    omega_yield: float,
    epsilon_yield: float,
) -> jnp.ndarray:
    """Cosserat energy density without the saturation kernel (but reflection
    term still uses yield scales via the A -> S -> Z -> Gamma chain).

    W = (2/3) G (tr eps)^2 + G eps_sym · eps_sym + G_c eps_antisym · eps_antisym
        + gamma kappa · kappa + k_op10 * W_Op10 + k_refl * W_reflection
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
    W_op10 = _op10_density(omega, dx)
    W_refl = _reflection_density(u, omega, dx, omega_yield, epsilon_yield)
    W_hopf = _hopf_density(omega, dx)
    W = W_cauchy * G + W_micropolar * G_c + W_kappa * gamma + W_op10 * k_op10 + W_refl * k_refl + W_hopf * k_hopf
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
    k_op10: float,
    k_refl: float,
    k_hopf: float,
) -> jnp.ndarray:
    """Cosserat energy density with scalar-invariant Axiom-4 saturation
    applied to |eps| and |kappa| separately. Op10 and reflection terms
    are added outside the saturation kernel (they implement their own
    bounded structure via n_hat unit-vector constraint and 1/S^2 regulator
    respectively)."""
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
    W_op10 = _op10_density(omega, dx)
    W_refl = _reflection_density(u, omega, dx, omega_yield, epsilon_yield)
    W_hopf = _hopf_density(omega, dx)
    W = (
        (W_cauchy * G + W_micropolar * G_c) * S_eps_sq
        + W_kappa * gamma * S_kappa_sq
        + W_op10 * k_op10
        + W_refl * k_refl
        + W_hopf * k_hopf
    )
    return W * mask_alive.astype(W.dtype)


def _total_energy_bare(u, omega, mask_alive, dx, G, G_c, gamma, k_op10, k_refl, k_hopf, omega_yield, epsilon_yield):
    return jnp.sum(
        _energy_density_bare(
            u, omega, mask_alive, dx, G, G_c, gamma, k_op10, k_refl, k_hopf, omega_yield, epsilon_yield
        )
    )


def _total_energy_saturated(
    u, omega, mask_alive, dx, G, G_c, gamma, omega_yield, epsilon_yield, k_op10, k_refl, k_hopf
):
    return jnp.sum(
        _energy_density_saturated(
            u, omega, mask_alive, dx, G, G_c, gamma, omega_yield, epsilon_yield, k_op10, k_refl, k_hopf
        )
    )


# JIT-compiled energy-and-gradient functions.
# jax.value_and_grad returns (value, gradient_tuple) for the argnums we diff.
_val_and_grad_bare = jax.jit(jax.value_and_grad(_total_energy_bare, argnums=(0, 1)))
_val_and_grad_saturated = jax.jit(jax.value_and_grad(_total_energy_saturated, argnums=(0, 1)))
_total_energy_bare_jit = jax.jit(_total_energy_bare)
_total_energy_saturated_jit = jax.jit(_total_energy_saturated)
_val_and_grad_s11 = jax.jit(jax.value_and_grad(_total_s11, argnums=(0, 1)))
_total_s11_jit = jax.jit(_total_s11)


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


def _connected_components_3d(mask: np.ndarray, connectivity: int = 26) -> tuple[np.ndarray, int]:
    """Connected-components labeling on a 3D boolean mask.

    Pure-numpy implementation (no scipy.ndimage dependency). For the
    K4 diamond lattice, use connectivity=26 (diagonal neighbors): the
    A sublattice at (even,even,even) and B at (odd,odd,odd) are only
    diagonally adjacent, so 6-connectivity sees them as disconnected.

    Returns (labels array with same shape as mask, n_components).
    Label 0 = background; labels 1..n_components = connected regions.
    """
    if connectivity == 26:
        neighbors = [
            (di, dj, dk)
            for di in (-1, 0, 1)
            for dj in (-1, 0, 1)
            for dk in (-1, 0, 1)
            if not (di == 0 and dj == 0 and dk == 0)
        ]
    elif connectivity == 6:
        neighbors = [(+1, 0, 0), (-1, 0, 0), (0, +1, 0), (0, -1, 0), (0, 0, +1), (0, 0, -1)]
    else:
        raise ValueError(f"connectivity must be 6 or 26, got {connectivity}")
    labels = np.zeros(mask.shape, dtype=np.int32)
    n_comp = 0
    nx, ny, nz = mask.shape
    it = np.nditer(mask, flags=["multi_index"])
    for val in it:
        if not val or labels[it.multi_index] != 0:
            continue
        n_comp += 1
        stack = [it.multi_index]
        labels[it.multi_index] = n_comp
        while stack:
            i, j, k = stack.pop()
            for di, dj, dk in neighbors:
                ni, nj, nk = i + di, j + dj, k + dk
                if 0 <= ni < nx and 0 <= nj < ny and 0 <= nk < nz and mask[ni, nj, nk] and labels[ni, nj, nk] == 0:
                    labels[ni, nj, nk] = n_comp
                    stack.append((ni, nj, nk))
    return labels, n_comp


# ----------------------------------------------------------------------
# Solver class
# ----------------------------------------------------------------------


class CosseratField3D:
    """Cartesian-with-FCC-filter solver for the 3D Cosserat field (u, omega)
    on the K4 diamond substrate, JAX-backed. State held as jax arrays; public
    attribute reads return numpy via __getattribute__ hooks are avoided —
    instead, users can np.asarray(solver.u) / np.asarray(solver.omega) to
    materialize when needed."""

    def __init__(
        self,
        nx: int,
        ny: int,
        nz: int,
        dx: float = 1.0,
        use_saturation: bool = True,
        rho: float = 1.0,
        I_omega: float = 1.0,
        pml_thickness: int = 0,
        damping_gamma: float = 0.0,
    ):
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.dx = float(dx)
        self.pml_thickness = int(pml_thickness)

        idx = np.indices((nx, ny, nz))
        i, j, k = idx[0], idx[1], idx[2]
        mask_A = (i % 2 == 0) & (j % 2 == 0) & (k % 2 == 0)
        mask_B = (i % 2 == 1) & (j % 2 == 1) & (k % 2 == 1)
        self.mask_A = mask_A
        self.mask_B = mask_B
        self.mask_alive = mask_A | mask_B
        self._i, self._j, self._k = i, j, k
        self._mask_alive_jax = jnp.asarray(self.mask_alive)

        # ---------------------------------------------------------
        # Cosserat-sector PML (doc 58_ derivation)
        # ---------------------------------------------------------
        # Ax1 + Ax3 require all wave-carrying sectors to have an absorbing
        # boundary at the simulation edge. Mirrors the K4 Sponge PML
        # (k4_tlm.py:174-190) applied to kinetic fields (u̇, ω̇) rather
        # than reflected voltages. Interior (d ≥ pml_thickness) has mask=1
        # and is untouched. See research/_archive/L3_electron_soliton/58_cosserat_pml_derivation.md.
        self.cos_pml_mask = np.ones((nx, ny, nz, 1), dtype=np.float64)
        if self.pml_thickness > 0:
            d_x = np.minimum(i, nx - 1 - i)
            d_y = np.minimum(j, ny - 1 - j)
            d_z = np.minimum(k, nz - 1 - k)
            d = np.minimum(np.minimum(d_x, d_y), d_z)
            pml_region = d < self.pml_thickness
            attenuation = 1.0 - ((self.pml_thickness - d[pml_region]) / self.pml_thickness) ** 2
            self.cos_pml_mask[pml_region, 0] = np.maximum(0.0, attenuation)

        # State is numpy for easy mutation; converted to jnp at each energy /
        # gradient call. The conversion overhead is small relative to the
        # jitted JAX kernels.
        self.u = np.zeros((nx, ny, nz, 3), dtype=np.float64)
        self.omega = np.zeros((nx, ny, nz, 3), dtype=np.float64)

        # Time-domain state (Phase I extension). Velocity fields conjugate to
        # (u, omega). Zero-initialised — solver remains drop-in compatible with
        # existing static ground-state finders (relax_s11, relax_to_ground_state)
        # which ignore these.
        self.u_dot = np.zeros_like(self.u)
        self.omega_dot = np.zeros_like(self.omega)
        self.time = 0.0

        self.G = 1.0
        self.G_c = 1.0
        self.gamma = 1.0
        self.k_op10 = 1.0
        self.k_refl = 1.0
        # k_hopf = pi/3 from the Hopf-invariant matching at Q_H = 6 (electron
        # (2,3) winding), per research/_archive/L3_electron_soliton/13_ §3.2.
        self.k_hopf = float(np.pi / 3.0)
        self.use_saturation = use_saturation
        self.omega_yield = float(np.pi)
        self.epsilon_yield = 1.0

        # Mass parameters for time-domain Lagrangian (Phase I).
        # L = ½·rho·|u_dot|² + ½·I_omega·|omega_dot|² − W(u, omega)
        # Defaults rho = I_omega = 1 in natural units (phase-I placeholder;
        # S4 adjudication to pin values from measured wave speed).
        self.rho = float(rho)

        # Topological Damped Integrator (TDI) coefficient — drains kinetic
        # energy on each velocity-Verlet step to enable settling into
        # Hamiltonian-stationary configurations. Default 0.0 preserves
        # energy-conserving VV behavior (bit-identical to pre-patch).
        # Modeled after AVE-Protein's protein_fold.py:295 dv = (F/m − γ·v)·dt
        # convention. Per Stage 6 Round 6 doc 66_ §16, this enables Path B
        # to find Hamiltonian-stationary states (joint −∂H/∂u = −∂H/∂ω = 0)
        # rather than only S₁₁-stationary states like doc 34_'s X4b.
        self.damping_gamma = float(damping_gamma)
        self.I_omega = float(I_omega)

    # ------------------------------------------------------------------
    # Initial condition
    # ------------------------------------------------------------------

    def initialize_electron_2_3_sector(
        self,
        R_target: float,
        r_target: float,
        localization_sigma: float | None = None,
        use_hedgehog: bool = True,
        amplitude_scale: float = 1.0,
    ) -> None:
        """
        Initialize the (2,3) torus-knot ansatz on the Cosserat ω-field.

        DEPRECATION NOTE (per research/_archive/L3_electron_soliton/101_ §9 three-layer
        canonical, Grant 2026-04-30): the original "electron" naming is
        misleading. Per the three-layer canonical:
          Layer 1 (real-space curve): electron is 0₁ UNKNOT — not (2,3)
          Layer 3 (phase-space):      (V_inc, V_ref) traces (2,3) winding on
                                      Clifford torus — but that's K4 V-tank,
                                      NOT Cosserat ω real-space
        Cosserat ω hosts Layer 1 (real-space curve) + Layer 2 (SU(2) bundle).
        This seeder writes a (2,3) torus-knot ansatz onto Cosserat ω — which
        is testing (2,3)-torus-knot dynamics in REAL SPACE (a separate
        physics question; valid for proton 5₁/5₂ family etc.), NOT the
        canonical electron.

        For the canonical electron, use `initialize_electron_unknot_sector`
        instead. The canonical alias `initialize_2_3_torus_knot_sector` on
        this class delegates to this method — preferred for any future code
        that wants (2,3) topology testing without the misleading "electron"
        label.

        If use_hedgehog=True (default): uses the AVE-canonical power-law
        hedgehog profile phi(R) = pi / (1 + (R/r_opt)^2) with the peak
        amplitude scaled to sqrt(3)/2 * pi (the Regime II→III boundary per
        AVE-VirtualMedia/scripts/generate_reflection_profile.py — the
        "active core at the stopband" condition).

        If use_hedgehog=False: retained for backwards compatibility, uses
        a Gaussian envelope — NOT topologically derived, just a QM
        wavefunction shape.

        r_opt: confinement radius from the topological crossing number,
        r_opt = kappa_FS / Q where kappa_FS = 8*pi (Axiom-derived, from
        manuscript/backmatter/02_full_derivation_chain.tex:463) and Q = 3
        for the electron (2,3) winding. So r_opt = 8*pi/3 ~ 8.38 lattice
        units by default, scaled to the r_target passed in.

        amplitude_scale: multiplier applied to the canonical envelope peak.
        Default 1.0 preserves the original sqrt(3)/2*pi peak (the static
        Regime II→III boundary). Per doc 34_ §9.4 X4a/X4b empirical sweep,
        the BOUND-STATE electron lives at peak |omega| ≈ 0.3*pi, NOT
        sqrt(3)/2*pi — at the canonical amplitude the lattice is in
        Regime III uniform-saturation with shell_Γ² → 0 (no TIR walls).
        Path B Round 6 callers should pass amplitude_scale = 0.3/(sqrt(3)/2)
        ≈ 0.3464 to seed at the empirical bound-state amplitude.
        """
        cx, cy, cz = (self.nx - 1) / 2.0, (self.ny - 1) / 2.0, (self.nz - 1) / 2.0
        x = self._i - cx
        y = self._j - cy
        z = self._k - cz

        rho_xy = np.sqrt(x**2 + y**2)
        rho_tube = np.sqrt((rho_xy - R_target) ** 2 + z**2)
        phi = np.arctan2(y, x)
        psi = np.arctan2(z, rho_xy - R_target)

        if use_hedgehog:
            # AVE-canonical power-law hedgehog (faddeev_skyrme.py, soliton_memory.py).
            # Peak amplitude = sqrt(3)/2 * pi sits at the Regime II/III boundary
            # where Gamma rises sharply — the "active core at the stopband" from
            # AVE-VirtualMedia/scripts/generate_reflection_profile.py.
            r_opt = r_target if r_target > 0 else 1.0
            envelope = amplitude_scale * (np.sqrt(3.0) / 2.0) * np.pi / (1.0 + (rho_tube / r_opt) ** 2)
        else:
            # Legacy Gaussian (QM wavefunction shape — NOT topologically derived).
            sigma = localization_sigma if localization_sigma is not None else r_target
            envelope = amplitude_scale * 0.6 * np.pi * np.exp(-(rho_tube**2) / (sigma**2))

        theta = 2.0 * phi + 3.0 * psi

        omega = np.zeros((self.nx, self.ny, self.nz, 3), dtype=np.float64)
        omega[..., 0] = envelope * np.cos(theta)
        omega[..., 1] = envelope * np.sin(theta)
        omega[..., 2] = 0.0
        omega *= self.mask_alive[..., None]

        self.omega = omega
        self.u = np.zeros_like(self.u)

    def initialize_u_displacement_2_3_sector(
        self,
        R_target: float,
        r_target: float,
        amplitude_scale: float = 0.5,
    ) -> None:
        """
        Initialize the (2,3) torus-knot ansatz on the DISPLACEMENT field u
        (not ω). This is the C-state seeder for the Cosserat translational LC
        pair (u ↔ u_dot), complementing initialize_electron_2_3_sector
        which is the L-state seeder for the rotational LC pair (θ ↔ ω).

        Use case (Round 6 F17-I): for an "all-C-state" coupled eigenmode seed,
        call this together with initialize_2_3_voltage_ansatz on the K4 side
        — both at C-state amplitude, all L-states (Φ_link, u_dot, ω) zeroed.
        Per doc 66_ §17.2.3 this is the natural LC-pair-coherent initial
        condition that Path A/B/C all violated.

        amplitude_scale: peak |u| = amplitude_scale · r_opt. For ε_yield = 1
        and r_opt ≈ r_target, |∇u| ≈ amplitude_scale gives strain at that
        fraction of yield. Default 0.5 keeps strain mid-range.

        Mirrors initialize_electron_2_3_sector exactly (same toroidal coords,
        same hedgehog envelope shape, same θ = 2φ + 3ψ winding) — but
        populates self.u and zeros self.omega.
        """
        cx, cy, cz = (self.nx - 1) / 2.0, (self.ny - 1) / 2.0, (self.nz - 1) / 2.0
        x = self._i - cx
        y = self._j - cy
        z = self._k - cz

        rho_xy = np.sqrt(x**2 + y**2)
        rho_tube = np.sqrt((rho_xy - R_target) ** 2 + z**2)
        phi = np.arctan2(y, x)
        psi = np.arctan2(z, rho_xy - R_target)

        # Peak |u| = amplitude_scale · r_opt → |∇u| ≈ amplitude_scale at hedgehog peak.
        r_opt = r_target if r_target > 0 else 1.0
        envelope = amplitude_scale * r_opt / (1.0 + (rho_tube / r_opt) ** 2)

        theta = 2.0 * phi + 3.0 * psi

        u = np.zeros((self.nx, self.ny, self.nz, 3), dtype=np.float64)
        u[..., 0] = envelope * np.cos(theta)
        u[..., 1] = envelope * np.sin(theta)
        u[..., 2] = 0.0
        u *= self.mask_alive[..., None]

        self.u = u
        self.omega = np.zeros_like(self.omega)

    def initialize_electron_unknot_sector(
        self,
        R_target: float,
        r_target: float | None = None,
        amplitude_scale: float = 1.0,
        use_hedgehog: bool = True,
    ) -> None:
        """
        Canonical electron unknot ansatz for the Cosserat ω-field.

        Per `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/
        electron-unknot.md`: the electron is a 0₁ unknot — a single closed
        flux tube loop carrying a Beltrami standing wave (∇×A = kA), at
        horn-torus geometry (R_loop = r_tube; Reading A canonical:
        R = r = ℓ_node/(2π)).

        The Cosserat ω-field is seeded TANGENT TO THE LOOP (ê_φ direction)
        with localization profile peaking at the tube centerline. NO (p,q)
        winding — this distinguishes the unknot from the (2,3) torus-knot
        ansatz hosted by `initialize_electron_2_3_sector`.

        Per research/_archive/L3_electron_soliton/101_ §9 (three-layer canonical):
            Layer 1 (real-space curve): unknot 0₁ (this seeder)
            Layer 2 (field bundle):    SU(2) double-cover via SO(3) → SU(2)
                                       Rodrigues projection of ω
                                       (post-processing observable; NOT
                                       seeder-encoded — ω has SO(3) period
                                       2π by construction)
            Layer 3 (phase-space):     (V_inc, V_ref) (2,3) winding on
                                       Clifford torus — NOT in scope of
                                       Cosserat sector; lives in K4 V-tank.

        Axiom chain:
          Ax 1 (K4 Cosserat crystal) — Cosserat ω is SO(3)-valued substrate
                                       microrotation (legacy: LC substrate).
                                       Cosserat rotational DOF = substrate-native
                                       intrinsic spin.
          Ax 2 (TKI)                 — closed flux loop topology, c=0
                                       unknot, Q_H=0; loop is the
                                       topological defect.
          Ax 3 (Min Reflection)      — Beltrami eigenmode ∇×ω = kω at
                                       fundamental k ≈ 1/R_loop (legacy
                                       name: Effective Action Principle).
          Ax 4 (Saturation)          — saturation kernel determines tube
                                       cross-section profile via hedgehog
                                       envelope.
          Bounding Limit 1           — m_e = ℏ/(ℓ_node·c); circumference
                                       = ℓ_node.
          Ropelength bound           — minimum ropelength = 2π for unknot
                                       at horn torus.

        Parameters:
          R_target: Loop major radius (grid units). Reading A canonical:
                    R = ℓ_node/(2π) ≈ 0.16 cells (sub-grid at dx=1.0).
                    For lattice-resolved diagnostic tests, R ≥ 4 cells.
          r_target: Tube minor radius (grid units). Default = R_target
                    (horn torus, Reading A canonical). Pass r ≠ R only
                    for non-canonical diagnostic tests of standard-torus
                    geometry.
          amplitude_scale: Peak |ω| multiplier. Default 1.0 sets peak |ω|
                    ≈ √3/2·π (matches `initialize_electron_2_3_sector`
                    Regime II/III boundary convention).
          use_hedgehog: True (default) uses AVE-canonical power-law hedgehog
                    π/(1 + (ρ/r_opt)²); False uses Gaussian (legacy QM
                    shape, NOT topologically derived).
        """
        if r_target is None:
            r_target = R_target  # horn torus default per Reading A

        cx, cy, cz = (self.nx - 1) / 2.0, (self.ny - 1) / 2.0, (self.nz - 1) / 2.0
        x = self._i - cx
        y = self._j - cy
        z = self._k - cz

        rho_xy = np.sqrt(x**2 + y**2)
        rho_tube = np.sqrt((rho_xy - R_target) ** 2 + z**2)
        phi = np.arctan2(y, x)

        if use_hedgehog:
            # AVE-canonical power-law hedgehog (matches initialize_electron_2_3_sector).
            # Peak amplitude = sqrt(3)/2 * pi at Regime II/III boundary.
            r_opt = r_target if r_target > 0 else 1.0
            envelope = amplitude_scale * (np.sqrt(3.0) / 2.0) * np.pi / (1.0 + (rho_tube / r_opt) ** 2)
        else:
            # Legacy Gaussian (QM wavefunction shape — NOT topologically derived).
            sigma = r_target if r_target > 0 else 1.0
            envelope = amplitude_scale * 0.6 * np.pi * np.exp(-(rho_tube**2) / (sigma**2))

        # ω = envelope · ê_φ where ê_φ = (-sin φ, cos φ, 0).
        # NO (p,q) winding — distinguishes unknot from torus-knot ansatz.
        # 2π closure of ω (SO(3) period); SU(2) double-cover is observable
        # via Rodrigues projection, not encoded in the seed.
        omega = np.zeros((self.nx, self.ny, self.nz, 3), dtype=np.float64)
        omega[..., 0] = -envelope * np.sin(phi)
        omega[..., 1] = envelope * np.cos(phi)
        omega[..., 2] = 0.0
        omega *= self.mask_alive[..., None]

        self.omega = omega
        self.u = np.zeros_like(self.u)

    def initialize_2_3_torus_knot_sector(
        self,
        R_target: float,
        r_target: float,
        localization_sigma: float | None = None,
        use_hedgehog: bool = True,
        amplitude_scale: float = 1.0,
    ) -> None:
        """
        Canonical name (per research/_archive/L3_electron_soliton/101_ §9, Grant
        2026-04-30 three-layer canonical) for seeding a (2,3)-torus-knot
        ansatz on the Cosserat ω-field. Delegates to the historical
        `initialize_electron_2_3_sector`; preserved as backward-compat alias.

        For the canonical electron, use `initialize_electron_unknot_sector`
        instead — the canonical electron is 0₁ unknot at Layer 1, NOT (2,3).
        This method tests (2,3)-torus-knot dynamics in real-space, which is
        valid physics for OTHER particles (e.g., proton 5₁/5₂ family, baryons
        with c ≥ 3 crossings) but not for the canonical electron.
        """
        self.initialize_electron_2_3_sector(
            R_target=R_target,
            r_target=r_target,
            localization_sigma=localization_sigma,
            use_hedgehog=use_hedgehog,
            amplitude_scale=amplitude_scale,
        )

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
                u_j,
                w_j,
                self._mask_alive_jax,
                self.dx,
                self.G,
                self.G_c,
                self.gamma,
                self.omega_yield,
                self.epsilon_yield,
                self.k_op10,
                self.k_refl,
                self.k_hopf,
            )
        else:
            rho = _energy_density_bare(
                u_j,
                w_j,
                self._mask_alive_jax,
                self.dx,
                self.G,
                self.G_c,
                self.gamma,
                self.k_op10,
                self.k_refl,
                self.k_hopf,
                self.omega_yield,
                self.epsilon_yield,
            )
        return np.asarray(rho)

    def total_energy(self) -> float:
        u_j = jnp.asarray(self.u)
        w_j = jnp.asarray(self.omega)
        if self.use_saturation:
            return float(
                _total_energy_saturated_jit(
                    u_j,
                    w_j,
                    self._mask_alive_jax,
                    self.dx,
                    self.G,
                    self.G_c,
                    self.gamma,
                    self.omega_yield,
                    self.epsilon_yield,
                    self.k_op10,
                    self.k_refl,
                    self.k_hopf,
                )
            )
        return float(
            _total_energy_bare_jit(
                u_j,
                w_j,
                self._mask_alive_jax,
                self.dx,
                self.G,
                self.G_c,
                self.gamma,
                self.k_op10,
                self.k_refl,
                self.k_hopf,
                self.omega_yield,
                self.epsilon_yield,
            )
        )

    def total_s11(self) -> float:
        """Field-level S11 objective: sum of |Gamma|^2 over tetrahedral
        neighbor pairs at every alive site. S11-minimization target per
        research/_archive/L3_electron_soliton handoff 2026-04-20."""
        u_j = jnp.asarray(self.u)
        w_j = jnp.asarray(self.omega)
        return float(
            _total_s11_jit(
                u_j,
                w_j,
                self._mask_alive_jax,
                self.dx,
                self.omega_yield,
                self.epsilon_yield,
            )
        )

    def s11_gradient(self) -> tuple[np.ndarray, np.ndarray]:
        """Gradient of the S11 objective wrt (u, omega)."""
        u_j = jnp.asarray(self.u)
        w_j = jnp.asarray(self.omega)
        _, (dS_du, dS_dw) = _val_and_grad_s11(
            u_j,
            w_j,
            self._mask_alive_jax,
            self.dx,
            self.omega_yield,
            self.epsilon_yield,
        )
        mask = self._mask_alive_jax[..., None].astype(dS_du.dtype)
        return np.asarray(dS_du * mask), np.asarray(dS_dw * mask)

    def relax_s11(
        self,
        max_iter: int = 500,
        tol: float = 1e-8,
        initial_lr: float = 0.01,
        verbose: bool = False,
        track_topology_every: int = 0,
    ) -> dict:
        """Gradient descent on the S11 objective (not energy).

        Same adaptive-lr / backtracking-acceptance structure as
        relax_to_ground_state, but minimizes sum|Gamma|^2 instead of
        sum Lagrangian density.
        """
        lr = initial_lr
        history = []
        trajectory = []
        S11_prev = self.total_s11()
        history.append(S11_prev)
        noise_floor = 1e-12 * max(abs(S11_prev), 1.0)

        if track_topology_every > 0:
            R0, r0 = self.extract_shell_radii()
            c0 = self.extract_crossing_count()
            trajectory.append({"step": 0, "S11": S11_prev, "R": R0, "r": r0, "c": c0, "lr": lr})
            if verbose:
                print(f"  step {0:4d}  S11 = {S11_prev:.6e}  (R, r, c) = ({R0:.3f}, {r0:.3f}, {c0})  lr = {lr:.2e}")

        for step in range(max_iter):
            u_save = self.u.copy()
            w_save = self.omega.copy()
            dS_du, dS_dw = self.s11_gradient()
            self.u = self.u - lr * dS_du
            self.omega = self.omega - lr * dS_dw
            self._zero_outside_alive()
            S11_new = self.total_s11()

            if S11_new <= S11_prev + noise_floor:
                rel_change = abs(S11_new - S11_prev) / max(abs(S11_prev), 1e-12)
                history.append(S11_new)

                if track_topology_every > 0 and ((step + 1) % track_topology_every == 0):
                    R_s, r_s = self.extract_shell_radii()
                    c_s = self.extract_crossing_count()
                    trajectory.append({"step": step + 1, "S11": S11_new, "R": R_s, "r": r_s, "c": c_s, "lr": lr})
                    if verbose:
                        print(
                            f"  step {step+1:4d}  S11 = {S11_new:.6e}  (R, r, c) = ({R_s:.3f}, {r_s:.3f}, {c_s})  lr = {lr:.2e}"
                        )

                if step > 10 and rel_change < tol:
                    return {
                        "iterations": step + 1,
                        "final_s11": S11_new,
                        "converged": True,
                        "s11_history": history,
                        "lr_final": lr,
                        "trajectory": trajectory,
                    }
                lr = min(lr * 1.1, 1.0)
                S11_prev = S11_new
                noise_floor = 1e-12 * max(abs(S11_prev), 1.0)
            else:
                self.u = u_save
                self.omega = w_save
                lr *= 0.5
                if lr < 1e-14:
                    return {
                        "iterations": step + 1,
                        "final_s11": S11_prev,
                        "converged": False,
                        "s11_history": history,
                        "lr_final": lr,
                        "trajectory": trajectory,
                    }

        return {
            "iterations": max_iter,
            "final_s11": S11_prev,
            "converged": False,
            "s11_history": history,
            "lr_final": lr,
            "trajectory": trajectory,
        }

    def energy_gradient(self) -> tuple[np.ndarray, np.ndarray]:
        """Via jax.value_and_grad on the energy functional. Exact to
        float-precision — no hand-derived stress tensors involved."""
        u_j = jnp.asarray(self.u)
        w_j = jnp.asarray(self.omega)
        if self.use_saturation:
            _, (dE_du, dE_dw) = _val_and_grad_saturated(
                u_j,
                w_j,
                self._mask_alive_jax,
                self.dx,
                self.G,
                self.G_c,
                self.gamma,
                self.omega_yield,
                self.epsilon_yield,
                self.k_op10,
                self.k_refl,
                self.k_hopf,
            )
        else:
            _, (dE_du, dE_dw) = _val_and_grad_bare(
                u_j,
                w_j,
                self._mask_alive_jax,
                self.dx,
                self.G,
                self.G_c,
                self.gamma,
                self.k_op10,
                self.k_refl,
                self.k_hopf,
                self.omega_yield,
                self.epsilon_yield,
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
        track_topology_every: int = 0,
    ) -> dict:
        """Gradient descent with backtracking-lr acceptance.

        If track_topology_every > 0, records (step, E, R, r, c) at that
        cadence in a 'trajectory' list, so the unwinding dynamics are
        visible in post-hoc analysis.
        """
        lr = initial_lr
        history = []
        trajectory = []
        E_prev = self.total_energy()
        history.append(E_prev)
        noise_floor = 1e-12 * max(abs(E_prev), 1.0)

        if track_topology_every > 0:
            R0, r0 = self.extract_shell_radii()
            c0 = self.extract_crossing_count()
            trajectory.append({"step": 0, "E": E_prev, "R": R0, "r": r0, "c": c0, "lr": lr})
            if verbose:
                print(f"  step {0:4d}  E = {E_prev:.6e}  (R, r, c) = ({R0:.3f}, {r0:.3f}, {c0})  lr = {lr:.2e}")

        for step in range(max_iter):
            u_save = self.u.copy()
            w_save = self.omega.copy()
            self.relax_step(lr)
            E_new = self.total_energy()

            if E_new <= E_prev + noise_floor:
                rel_change = abs(E_new - E_prev) / max(abs(E_prev), 1e-12)
                history.append(E_new)

                if track_topology_every > 0 and ((step + 1) % track_topology_every == 0):
                    R_s, r_s = self.extract_shell_radii()
                    c_s = self.extract_crossing_count()
                    trajectory.append({"step": step + 1, "E": E_new, "R": R_s, "r": r_s, "c": c_s, "lr": lr})
                    if verbose:
                        print(
                            f"  step {step+1:4d}  E = {E_new:.6e}  (R, r, c) = ({R_s:.3f}, {r_s:.3f}, {c_s})  lr = {lr:.2e}"
                        )

                if step > 10 and rel_change < tol:
                    return {
                        "iterations": step + 1,
                        "final_energy": E_new,
                        "converged": True,
                        "energy_history": history,
                        "lr_final": lr,
                        "trajectory": trajectory,
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
                        "trajectory": trajectory,
                    }

        return {
            "iterations": max_iter,
            "final_energy": E_prev,
            "converged": False,
            "energy_history": history,
            "lr_final": lr,
            "trajectory": trajectory,
        }

    # ------------------------------------------------------------------
    # Time-domain evolution (Phase I — AVE-ideal simulator prereq)
    # ------------------------------------------------------------------
    #
    # Velocity-Verlet (leapfrog) integrator for the Cosserat Lagrangian
    #     L = (½·rho·|u̇|² + ½·I_ω·|ω̇|²) − W(u, ω)
    # giving Euler-Lagrange equations
    #     rho·ü    = −∂W/∂u      (force per volume on translation)
    #     I_ω·ω̈  = −∂W/∂ω     (torque per volume on microrotation)
    # The spatial force is the existing `energy_gradient()` call — re-used
    # without modification. For a CLEAN linear-wave validation, set
    # `k_op10 = k_refl = k_hopf = 0` and `use_saturation = False` before
    # stepping so only the Cauchy + micropolar + curvature terms remain.

    @property
    def cfl_dt(self) -> float:
        """CFL-safe timestep for the linear Cosserat wave equation.

        Transverse shear speed  c_T = √(G/rho).
        Rotational speed         c_R = √(gamma/I_omega).
        Longitudinal (bulk)      c_L = √((K + 4G/3)/rho) with K = 2G →
                                        c_L = √(10G/(3·rho)) ≈ 1.826·c_T.

        CFL on a 3D lattice with first-order tetrahedral gradient:
            dt ≤ dx / (c_max · √3)
        Return 0.3 · dx / (c_max · √3) for a 70% safety margin.
        """
        c_T = np.sqrt(self.G / max(self.rho, 1e-30))
        c_R = np.sqrt(self.gamma / max(self.I_omega, 1e-30))
        c_L = np.sqrt((2.0 * self.G + 4.0 * self.G / 3.0) / max(self.rho, 1e-30))
        c_max = max(c_T, c_R, c_L)
        return float(0.3 * self.dx / (c_max * np.sqrt(3.0)))

    def kinetic_energy(self) -> float:
        """(½·rho·|u̇|² + ½·I_ω·|ω̇|²) summed over alive sites."""
        mask = self.mask_alive[..., None].astype(self.u_dot.dtype)
        K_u = 0.5 * self.rho * np.sum((self.u_dot * mask) ** 2)
        K_w = 0.5 * self.I_omega * np.sum((self.omega_dot * mask) ** 2)
        return float(K_u + K_w)

    def total_hamiltonian(self) -> float:
        """H = T + V where T = kinetic_energy, V = total_energy."""
        return self.kinetic_energy() + self.total_energy()

    def _zero_velocities_outside_alive(self) -> None:
        """Enforce mask_alive + PML absorption on kinetic fields (u̇, ω̇).

        Interior (pml_mask=1) unchanged; PML region attenuated; inactive
        sites zeroed. PML is only present when pml_thickness>0; for
        pml_thickness=0 this is a pure mask_alive zero-out (legacy behavior).
        Per doc 58_ Cosserat PML derivation.
        """
        mask = self.mask_alive[..., None].astype(self.u_dot.dtype)
        combined = mask * self.cos_pml_mask.astype(self.u_dot.dtype)
        self.u_dot = self.u_dot * combined
        self.omega_dot = self.omega_dot * combined

    def step(self, dt: float | None = None) -> None:
        """Advance (u, omega) one timestep via velocity-Verlet.

        Equations:
            u(t+dt)    = u(t) + u_dot(t) · dt + ½·ü(t)·dt²
            omega(t+dt) = omega(t) + omega_dot(t)·dt + ½·ω̈(t)·dt²
            u_dot(t+dt)    = u_dot(t) + ½·(ü(t) + ü(t+dt))·dt
            omega_dot(t+dt) = ...
        with
            ü     = −(1/rho)·∂W/∂u
            ω̈    = −(1/I_omega)·∂W/∂omega

        Energy-conserving to O(dt²) for the full nonlinear Lagrangian.
        Active-site masks are enforced on (u, omega, u_dot, omega_dot)
        at each sub-step.

        dt defaults to cfl_dt if not provided.
        """
        if dt is None:
            dt = self.cfl_dt

        # Force at current state  →  acceleration
        dE_du, dE_dw = self.energy_gradient()
        a_u = -dE_du / self.rho
        a_w = -dE_dw / self.I_omega

        # Half-kick: u_dot(t+dt/2)
        self.u_dot = self.u_dot + 0.5 * dt * a_u
        self.omega_dot = self.omega_dot + 0.5 * dt * a_w
        self._zero_velocities_outside_alive()

        # Drift: u(t+dt)
        self.u = self.u + dt * self.u_dot
        self.omega = self.omega + dt * self.omega_dot
        self._zero_outside_alive()

        # Force at new state  →  new acceleration
        dE_du_new, dE_dw_new = self.energy_gradient()
        a_u_new = -dE_du_new / self.rho
        a_w_new = -dE_dw_new / self.I_omega

        # Half-kick: u_dot(t+dt)
        self.u_dot = self.u_dot + 0.5 * dt * a_u_new
        self.omega_dot = self.omega_dot + 0.5 * dt * a_w_new
        self._zero_velocities_outside_alive()

        # Topological Damped Integrator (TDI) — multiplicative velocity decay
        # to drain kinetic energy and settle to Hamiltonian-stationary states.
        # γ=0 preserves energy-conserving VV; γ>0 enables TDI mode for
        # finding stable bound configurations per AVE-Protein methodology
        # (protein_fold.py:295). Stage 6 Round 6 / doc 66_ §16.
        if self.damping_gamma > 0.0:
            decay = max(0.0, 1.0 - self.damping_gamma * dt)
            self.u_dot *= decay
            self.omega_dot *= decay

        self.time += dt

    def initialize_gaussian_wavepacket_omega(
        self,
        center: tuple[float, float, float],
        sigma: float,
        direction: tuple[float, float, float],
        wavelength: float,
        amplitude: float = 1e-3,
        axis: int = 2,
    ) -> None:
        """Seed a small propagating rotational (ω) Gaussian wavepacket.

        omega(r, t=0) =
            amplitude · exp(-|r-c|²/(2σ²)) · cos(k·(r-c)) · ê_axis
        u(r, t=0) = 0
        omega_dot(r, t=0) = ω̇ chosen to give forward-propagating wave:
            ω̇ = -(c_T · k) · amplitude · exp(…) · sin(k·(r-c)) · ê_axis
        (so the superposition e^{i(k·r-ω t)} travels in +direction)

        For a clean shear-wave test: axis perpendicular to direction
        (e.g. direction=x̂, axis=ẑ).

        Args:
            center: (x0, y0, z0) in lattice cells.
            sigma: Gaussian envelope σ in lattice cells.
            direction: propagation direction (need not be unit).
            wavelength: carrier λ in lattice cells.
            amplitude: peak omega amplitude (rad).
            axis: component index (0,1,2) of omega to excite.
        """
        d_hat = np.asarray(direction, dtype=float)
        d_hat = d_hat / np.linalg.norm(d_hat)
        k_vec = (2.0 * np.pi / wavelength) * d_hat

        x0, y0, z0 = center
        rx = self._i - x0
        ry = self._j - y0
        rz = self._k - z0
        r2 = rx * rx + ry * ry + rz * rz

        envelope = np.exp(-r2 / (2.0 * sigma**2))
        phase = k_vec[0] * rx + k_vec[1] * ry + k_vec[2] * rz
        carrier_cos = np.cos(phase)
        carrier_sin = np.sin(phase)

        c_T = np.sqrt(self.G / max(self.rho, 1e-30))

        omega_field = np.zeros_like(self.omega)
        omega_dot_field = np.zeros_like(self.omega_dot)
        omega_field[..., axis] = amplitude * envelope * carrier_cos
        # Velocity chosen so (cos·f(r) at t=0, sin-like time evolution) forms a
        # traveling wave at speed c_T along +d̂. omega(r, t) ~ cos(k·r − ω t)
        # ⇒ ∂_t omega|_{t=0} = ω · sin(k·r) = c_T·|k|·sin(k·r).
        omega_dot_field[..., axis] = c_T * np.linalg.norm(k_vec) * amplitude * envelope * carrier_sin

        # Enforce active-site mask.
        mask4 = self.mask_alive[..., None].astype(omega_field.dtype)
        self.omega = omega_field * mask4
        self.omega_dot = omega_dot_field * mask4
        self.u = np.zeros_like(self.u)
        self.u_dot = np.zeros_like(self.u_dot)
        self.time = 0.0

    # ------------------------------------------------------------------
    # Phase III diagnostics: Hopf charge + soliton localization
    # ------------------------------------------------------------------
    # Rationale (per plan doc-list-for-next-chat Prereq 1):
    #   `extract_crossing_count` is noisy on time-evolving (u, ω) fields
    #   because it counts DISCRETE contour crossings that can alias.
    #   Phase III needs a continuous, topological Q measure, and also
    #   needs to identify MULTIPLE soliton centroids (for pair creation
    #   in III-B).

    def extract_hopf_charge(self) -> float:
        """Topological Hopf invariant Q_H from the Cosserat ω field.

        Uses the existing `_hopf_density` (A·B/2 Chern-Simons density).
        Integrating it over space gives 4π²·Q_H per §13 of the L3 research.

        Returns a REAL number (not integer-discretized); robust to small
        field perturbations. For (2,3)-torus-knot electron, Q_H → 6; for
        vacuum, Q_H = 0; for pair-creation, total Q_H should remain near 0
        (e+ and e− contribute opposite signs to the regional sum).
        """
        w_j = jnp.asarray(self.omega)
        rho = _hopf_density(w_j, self.dx)
        mask = jnp.asarray(self.mask_alive).astype(rho.dtype)
        integral = float(jnp.sum(rho * mask) * (self.dx**3))
        return integral / (4.0 * np.pi**2)

    def find_soliton_centroids(
        self,
        threshold_frac: float = 0.3,
        min_cluster_size: int = 8,
    ) -> list[dict]:
        """Find localized ω-field concentrations.

        Returns a list of dicts with (center_xyz, peak_mag, n_cells_above)
        for each spatially-isolated region where |ω|² exceeds
        `threshold_frac · max(|ω|²)`. Uses connected-component labeling on
        the thresholded field.

        Critical for Phase III-B: after pair creation, we expect TWO
        distinct centroids (e+ and e−). This method identifies them.
        """
        omega_mag_sq = np.sum(self.omega**2, axis=-1) * self.mask_alive
        if omega_mag_sq.max() <= 1e-30:
            return []
        threshold = threshold_frac * omega_mag_sq.max()
        above = omega_mag_sq > threshold

        # 6-connected components labeling (numpy-only implementation)
        labels, n_comp = _connected_components_3d(above)

        centroids = []
        for lab in range(1, n_comp + 1):
            mask = labels == lab
            n_cells = int(mask.sum())
            if n_cells < min_cluster_size:
                continue
            idx = np.where(mask)
            weights = omega_mag_sq[idx]
            total = weights.sum()
            cx = float((idx[0] * weights).sum() / total)
            cy = float((idx[1] * weights).sum() / total)
            cz = float((idx[2] * weights).sum() / total)
            peak = float(omega_mag_sq[mask].max())
            centroids.append(
                {
                    "center": (cx, cy, cz),
                    "peak_mag_sq": peak,
                    "n_cells": n_cells,
                }
            )
        return centroids

    def total_omega_energy_local(self, center: tuple[float, float, float], radius: float) -> float:
        """|ω|² summed over sites within `radius` cells of `center`.
        For multi-soliton Phase III-B: partition energy between centroids.
        """
        cx, cy, cz = center
        rx = self._i - cx
        ry = self._j - cy
        rz = self._k - cz
        r2 = rx * rx + ry * ry + rz * rz
        mask = (r2 <= radius**2) & self.mask_alive
        return float(np.sum(np.sum(self.omega**2, axis=-1) * mask))

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
        """
        Robust c-extraction: scan several minor-cycle radii around the major
        ring; return the max winding number found on any contour where the
        field amplitude is nontrivial.

        Motivation: a single contour at too-small a minor radius can
        undercount the winding because the field is noisy at sub-shell radii
        (amplitude near zero, phase ill-defined). Scanning larger radii
        surfaces the true topological winding.
        """
        cx, cy, cz = (self.nx - 1) / 2.0, (self.ny - 1) / 2.0, (self.nz - 1) / 2.0
        R_found, _ = self.extract_shell_radii()
        omega_np = self.omega

        def single_contour_winding(r_minor: float) -> tuple[int, float]:
            n_psi = 128
            psis = np.linspace(0.0, 2.0 * np.pi, n_psi, endpoint=False)
            dx_s = cx + (R_found + r_minor * np.cos(psis))
            dy_s = cy + np.zeros_like(psis)
            dz_s = cz + r_minor * np.sin(psis)

            ix = np.clip(dx_s.astype(int), 0, self.nx - 2)
            iy = np.clip(dy_s.astype(int), 0, self.ny - 2)
            iz = np.clip(dz_s.astype(int), 0, self.nz - 2)
            fx = dx_s - ix
            fy = dy_s - iy
            fz = dz_s - iz

            def sample(comp: int) -> np.ndarray:
                v000 = omega_np[ix, iy, iz, comp]
                v100 = omega_np[ix + 1, iy, iz, comp]
                v010 = omega_np[ix, iy + 1, iz, comp]
                v001 = omega_np[ix, iy, iz + 1, comp]
                v110 = omega_np[ix + 1, iy + 1, iz, comp]
                v101 = omega_np[ix + 1, iy, iz + 1, comp]
                v011 = omega_np[ix, iy + 1, iz + 1, comp]
                v111 = omega_np[ix + 1, iy + 1, iz + 1, comp]
                return (
                    (1 - fx) * (1 - fy) * (1 - fz) * v000
                    + fx * (1 - fy) * (1 - fz) * v100
                    + (1 - fx) * fy * (1 - fz) * v010
                    + (1 - fx) * (1 - fy) * fz * v001
                    + fx * fy * (1 - fz) * v110
                    + fx * (1 - fy) * fz * v101
                    + (1 - fx) * fy * fz * v011
                    + fx * fy * fz * v111
                )

            ox = sample(0)
            oy = sample(1)
            amp = np.sqrt(ox**2 + oy**2)
            min_amp = float(amp.min())
            max_amp = float(amp.max())

            phase = np.arctan2(oy, ox)
            unwrapped = np.unwrap(phase)
            total_winding = (unwrapped[-1] - unwrapped[0]) / (2.0 * np.pi)
            closure = phase[0] - unwrapped[-1]
            while closure > np.pi:
                closure -= 2.0 * np.pi
            while closure < -np.pi:
                closure += 2.0 * np.pi
            total_winding += closure / (2.0 * np.pi)

            # Flag the contour as "reliable" only if the minimum amplitude
            # on the loop is at least 10% of the max. Weak-amplitude contours
            # are phase-noise dominated and underreport the winding.
            reliability = min_amp / max(max_amp, 1e-12)
            return int(round(abs(total_winding))), reliability

        # Scan a range of minor radii, keeping max from reliable contours.
        max_reliable_winding = 0
        any_reliable = False
        for r_minor in np.linspace(0.5, max(3.0, R_found * 0.5), 8):
            w, rel = single_contour_winding(r_minor)
            if rel > 0.1:
                any_reliable = True
                if w > max_reliable_winding:
                    max_reliable_winding = w

        if any_reliable:
            return max_reliable_winding
        # Fallback: if no reliable contour, take the max winding read regardless.
        return max(single_contour_winding(r_minor)[0] for r_minor in np.linspace(1.0, max(3.0, R_found * 0.5), 5))

    def extract_quality_factor(self) -> float:
        R, r = self.extract_shell_radii()
        d = 1.0
        return 16.0 * np.pi**3 * (R * r) + 4.0 * np.pi**2 * (R * r) + np.pi * d
