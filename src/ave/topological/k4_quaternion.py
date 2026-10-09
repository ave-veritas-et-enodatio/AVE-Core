"""K4 quaternion-storage helpers (Lie-group Cosserat mode, opt-in).

Self-contained extraction of the K4 unit-quaternion rotation-storage block
formerly inline in ``cosserat_field_3d.py`` (PR-B, extracted in the B1
module-split pass). ``cosserat_field_3d`` re-imports every public symbol here
for backward compatibility; existing callers and tests keep working against
either import path.

Convention: q=(q0,q1,q2,q3), vacuum rest=(1,0,0,0).
Drift: q ← exp(½Ω dt)⊗q  (left multiply; Lie-group velocity-Verlet).
Left-trivialized torque: τ=½Im(g⊗q̄), g=dW/dq∈ℝ⁴.  Numerically verified:
  τ₁=½(−g₀q₁+g₁q₀−g₂q₃+g₃q₂),  τ₂=½(−g₀q₂+g₁q₃+g₂q₀−g₃q₁),
  τ₃=½(−g₀q₃−g₁q₂+g₂q₁+g₃q₀).
n-field: n=R(q)ẑ (cf:219-221 equivalent, skipping cf:204-215).
Bond wryness: κ_ij=(1/4dx)·Σ_l p_{l,j}·(2 Im log q̄⊗q′)_i;
  small-angle limit = ∂_j ω_i (cf:189-191).
Finite-rotation strain: ε=Rᵀ(q)(I+∇u)−I (O1 ruling, spec A5.3); frame-objective
  under director law F→QF, q→q_Q·q (ΔW/W≤2e-15; R1-9 residuals measured).
  Declared ω-engine map (spec A5.3): ω_eng ≡ −2 Im log q.  The engine's stored ω
  is the INVERSE of the rotation q encodes: a rigid rotation with director +θ has
  ω_eng = −θ (strain_ruling engine_lin_rigid result: ε_eng(Gu,−θ)=0).  At small
  angle: q(ω_eng) = (1, −ω_eng/2).  Under this map Rᵀ·F−I matches cf:175-186 to
  O(h) (max rel err ~2.8e-6 at h=1e-6; strain_ruling.py e92ca222be08).
  cf:175-186 vs cf:194-221 are jointly non-objective (K-R19).

This module is intentionally free of any import from ``cosserat_field_3d`` to
avoid a circular import; it copies the two shared primitives (``TETRA_OFFSETS``
and ``_tetrahedral_gradient``) it needs.

B10 Rule-10 table (spec §1 K-R4/R5 + ladder §7 rows 1,3,4,6,10; A5.4 K-R18/19/20;
grade: DERIVED = algebraic/convention consequence, SIM = holds in the simulation):
  | #            | cf:line       | Corpus says            | Code/sim says                                              | Grade   |
  |--------------|---------------|------------------------|------------------------------------------------------------|---------|
  | K-R4         | cf:~1047-1049 | ω "has SO(3) period 2π"| K4 stores q∈S³ (SU(2) double cover); no ω 2π representation seam | DERIVED |
  | K-R5         | cf:~1047-1049 | same                   | K4 energy not periodic in ω; only the n̂ terms are         | DERIVED |
  | B7 strain    | k4_quaternion | ε = Rᵀ(I+∇u)−I         | O1 ruling adopted; OBJECTIVE (R1-9: ΔW/W≤2e-15; FR trip: ΔW/W≈17) | DERIVED |
  | K-R20        | spec line 17  | small-angle = cf:186   | sign opposite at linear order; kept as O1 (objective) with ω map | DERIVED |
  | K-R18        | cf:497-500    | "not a fit parameter"  | E_refl ∝ 1/eps_reg exactly; regulator; k_refl=0 for this test (A5.1) | SIM |
  | K-R19        | cf:175-186 vs cf:194-221 | ε=∂u−ε·ω and n=R(ω)ẑ jointly objective | jointly non-objective: rigid rotation with co-rotating director gives strain 2.0×; ω acts as inverse of director rotation | DERIVED+SIM |
  | Row 3 (TIR)  | cf:1176-1177  | TIR confinement        | absent with k_refl=0; PASS ≠ evidence for TIR              | DERIVED |
  | Row 4 (deflt)| cf:~1038      | k_refl default 1       | R2 run uses 0; read-back assert required                   | DERIVED |
  | Row 6 (c_R)  | cf:~1969-1971 | c_R=√(γ/I)             | irrelevant at trade (b) dt                                 | DERIVED |
  | Row 10 (eps) | cf:493-494    | "autograd safety"      | E_refl ∝ 1/eps_reg exactly (bulk reflection term; Gate)    | SIM     |
  | B6 gap       | k4_quaternion | Ω_gap²=4G_c/I_ω → 2    | ω_gap=2.0021 (K4≡omega 1e-7); G_c=0 → ω=0.27 (trip)        | SIM     |
  | B3 dynamic   | charge_counters| N=1 hedgehog preserved| undamped K4 dynamics do NOT hold the charge at defaults; |q|=1 exact (honest-closure record) | SIM     |
  | B6 drift     | k4_quaternion | energy conserved       | symplectic VV: |ΔH/H0| O(dt²) (1.3e-2 @ cfl, 2e-5 @ cfl/16) | SIM     |

Checkpoint-10 note (substrate-native-check): the K4 reflection term W_refl ∝
grad_S²/(S²+eps_reg) is a BULK energy term (singular as S→0), carried forward
UNCHANGED from the omega engine (cf:441-502 analog). It is NOT re-rendered as a
Γ boundary condition in this PR; the Row-10 SIM grade flags it.
"""

import jax

jax.config.update("jax_enable_x64", True)

import jax.numpy as jnp  # noqa: E402
import numpy as np  # noqa: E402


# K4 diamond-lattice tetrahedral offsets (copied from cosserat_field_3d to keep
# this module self-contained; byte-identical tuple).
TETRA_OFFSETS: tuple[tuple[int, int, int], ...] = (
    (+1, +1, +1),
    (+1, -1, -1),
    (-1, +1, -1),
    (-1, -1, +1),
)


def _tetrahedral_gradient(V: jnp.ndarray) -> jnp.ndarray:
    """d_j V_i ~= (1/4) sum_ell p_ell^j (V(x + p_ell) - V(x)). First-order
    consistent on the diamond lattice; see 09_ §1.2.

    Copied verbatim from cosserat_field_3d._tetrahedral_gradient to keep this
    module import-cycle-free."""
    grad = jnp.zeros(V.shape + (3,), dtype=V.dtype)
    for p in TETRA_OFFSETS:
        V_neighbor = jnp.roll(V, shift=(-p[0], -p[1], -p[2]), axis=(0, 1, 2))
        delta = V_neighbor - V
        for j in range(3):
            if p[j] != 0:
                grad = grad.at[..., j].add(0.25 * p[j] * delta)
    return grad


# ======================================================================
# K4 quaternion-storage helpers (Lie-group Cosserat mode, opt-in)
# ======================================================================


def _quat_mul_jax(a: jnp.ndarray, b: jnp.ndarray) -> jnp.ndarray:
    """Hamilton product a⊗b, last axis=(q0,q1,q2,q3)."""
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return jnp.stack([
        a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
        a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
        a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1,
        a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0,
    ], axis=-1)


def _q_to_n_jax(q: jnp.ndarray) -> jnp.ndarray:
    """n=R(q)ẑ — unit director from quaternion, shape (*,3). Cf:219-221."""
    q0, q1, q2, q3 = q[..., 0], q[..., 1], q[..., 2], q[..., 3]
    return jnp.stack([
        2.0 * (q1 * q3 + q0 * q2),
        2.0 * (q2 * q3 - q0 * q1),
        1.0 - 2.0 * (q1 ** 2 + q2 ** 2),
    ], axis=-1)


def _compute_strain_q_jax(
    u: jnp.ndarray, q: jnp.ndarray, dx: float,
) -> jnp.ndarray:
    """Finite-rotation Cosserat strain ε=Rᵀ(q)·(I+∇u)−I, shape (*,3,3).
    Small-angle limit = cf:175-186; difference O(θ²).

    B7 objectivity fix: uses ε = Rᵀ·F (NOT F·R). Under a spatial rigid
    rotation Q (u → Q·u, q → Q⊗q so R → Q·R, F → Q·F), the Rᵀ·F form
    transforms as (Q·R)ᵀ·(Q·F) = Rᵀ·Qᵀ·Q·F = Rᵀ·F — invariant, so the
    stored energy is frame-objective. The old F·R form is NOT objective
    (Q·F·Q·R ≠ Q·(F·R)). Both forms share the same small-angle limit
    (R(q)≈I−[ω×] for q≈(1,ω/2)) to O(θ); the antisymmetric-part difference
    is the O(θ²) term in R.
    """
    q0, q1, q2, q3 = q[..., 0], q[..., 1], q[..., 2], q[..., 3]
    # R(q) entries (standard quaternion rotation matrix)
    R00 = 1.0 - 2.0 * (q2 ** 2 + q3 ** 2)
    R01 = 2.0 * (q1 * q2 - q0 * q3)
    R02 = 2.0 * (q1 * q3 + q0 * q2)
    R10 = 2.0 * (q1 * q2 + q0 * q3)
    R11 = 1.0 - 2.0 * (q1 ** 2 + q3 ** 2)
    R12 = 2.0 * (q2 * q3 - q0 * q1)
    R20 = 2.0 * (q1 * q3 - q0 * q2)
    R21 = 2.0 * (q2 * q3 + q0 * q1)
    R22 = 1.0 - 2.0 * (q1 ** 2 + q2 ** 2)
    # F = I + ∇u; gu[...,i,j] = ∂_j u_i
    gu = _tetrahedral_gradient(u) / dx
    F00 = 1.0 + gu[..., 0, 0];  F01 = gu[..., 0, 1];  F02 = gu[..., 0, 2]
    F10 = gu[..., 1, 0];         F11 = 1.0 + gu[..., 1, 1];  F12 = gu[..., 1, 2]
    F20 = gu[..., 2, 0];         F21 = gu[..., 2, 1];  F22 = 1.0 + gu[..., 2, 2]
    # ε = Rᵀ·F − I; ε_{ij} = Σ_k R_{ki}·F_{kj}  (row i of Rᵀ = col i of R)
    e00 = R00 * F00 + R10 * F10 + R20 * F20 - 1.0
    e01 = R00 * F01 + R10 * F11 + R20 * F21
    e02 = R00 * F02 + R10 * F12 + R20 * F22
    e10 = R01 * F00 + R11 * F10 + R21 * F20
    e11 = R01 * F01 + R11 * F11 + R21 * F21 - 1.0
    e12 = R01 * F02 + R11 * F12 + R21 * F22
    e20 = R02 * F00 + R12 * F10 + R22 * F20
    e21 = R02 * F01 + R12 * F11 + R22 * F21
    e22 = R02 * F02 + R12 * F12 + R22 * F22 - 1.0
    return jnp.stack([
        jnp.stack([e00, e01, e02], axis=-1),
        jnp.stack([e10, e11, e12], axis=-1),
        jnp.stack([e20, e21, e22], axis=-1),
    ], axis=-2)


def _bond_wryness_jax(q: jnp.ndarray, dx: float) -> jnp.ndarray:
    """Bond wryness κ_ij=(1/4dx)·Σ_l p_{l,j}·(2 Im log q̄⊗q′)_i, shape (*,3,3).
    Small-angle limit = _compute_curvature(ω,dx) (cf:189-191).
    Double-where autodiff-safe log-map pattern matching cf:194-222."""
    q_conj = q * jnp.array([1.0, -1.0, -1.0, -1.0], dtype=q.dtype)
    kappa = jnp.zeros(q.shape[:-1] + (3, 3), dtype=q.dtype)
    for (di, dj, dk) in TETRA_OFFSETS:
        qs = jnp.roll(
            jnp.roll(jnp.roll(q, -di, axis=0), -dj, axis=1), -dk, axis=2,
        )
        prod = _quat_mul_jax(q_conj, qs)
        # Short-arc: ensure scalar part ≥ 0
        s = jnp.where(prod[..., 0:1] >= 0.0, 1.0, -1.0)
        prod = prod * s
        vec = prod[..., 1:]    # (*,3); = sin(θ)·n̂
        q0h = prod[..., 0:1]   # (*,1); = cos(θ)
        # Log-map: 2θ·n̂.  θ/sin(θ) scale, double-where safe at identity.
        # 1/sinc(θ/π) = θ/sin(θ); jnp.sinc(x)=sin(πx)/(πx) so sinc(θ/π)=sin(θ)/θ.
        v2 = jnp.sum(vec ** 2, axis=-1, keepdims=True)
        vn_safe = jnp.sqrt(jnp.where(v2 > 1e-30, v2, jnp.ones_like(v2)))
        theta = jnp.arctan2(vn_safe, q0h)
        sinc_v = jnp.sinc(theta / jnp.pi)   # = sin(θ)/θ, smooth at 0
        scale_raw = 1.0 / sinc_v             # = θ/sin(θ)
        scale = jnp.where(v2 > 1e-30, scale_raw, jnp.ones_like(scale_raw))
        dw = 2.0 * scale * vec               # = 2θ·n̂, shape (*,3)
        pv = jnp.array([float(di), float(dj), float(dk)], dtype=q.dtype)
        kappa = kappa + jnp.einsum("...i,j->...ij", dw, pv) * (1.0 / (4.0 * dx))
    return kappa


def _op10_density_q(q: jnp.ndarray, dx: float) -> jnp.ndarray:
    """Op10 density with n from q directly (cf:299-316, skips cf:204-215)."""
    n_hat = _q_to_n_jax(q)
    grad_n = _tetrahedral_gradient(n_hat) / dx
    G = jnp.einsum("...ai,...aj->...ij", grad_n, grad_n)
    tr_G = jnp.sum(jnp.diagonal(G, axis1=-2, axis2=-1), axis=-1)
    sq_G = jnp.sum(G * G, axis=(-2, -1))
    return 0.5 * (tr_G * tr_G - sq_G)


def _hopf_density_q(q: jnp.ndarray, dx: float) -> jnp.ndarray:
    """Hopf density with n from q directly (cf:319-381, skips cf:204-215)."""
    n_hat = _q_to_n_jax(q)
    grad_n = _tetrahedral_gradient(n_hat) / dx
    di_n = jnp.moveaxis(grad_n, -1, 0)
    F01 = jnp.sum(n_hat * jnp.cross(di_n[0], di_n[1], axis=-1), axis=-1)
    F02 = jnp.sum(n_hat * jnp.cross(di_n[0], di_n[2], axis=-1), axis=-1)
    F12 = jnp.sum(n_hat * jnp.cross(di_n[1], di_n[2], axis=-1), axis=-1)
    B = jnp.stack([F12, -F02, F01], axis=-1)
    nx, ny, nz = B.shape[:3]
    kx = jnp.fft.fftfreq(nx, d=dx) * (2.0 * jnp.pi)
    ky = jnp.fft.fftfreq(ny, d=dx) * (2.0 * jnp.pi)
    kz = jnp.fft.fftfreq(nz, d=dx) * (2.0 * jnp.pi)
    KX, KY, KZ = jnp.meshgrid(kx, ky, kz, indexing="ij")
    K2 = KX * KX + KY * KY + KZ * KZ
    K2_safe = jnp.where(K2 > 0, K2, 1.0)
    zero_mask = (K2 > 0).astype(B.dtype)
    B_hat = jnp.fft.fftn(B, axes=(0, 1, 2))
    kBx = KY * B_hat[..., 2] - KZ * B_hat[..., 1]
    kBy = KZ * B_hat[..., 0] - KX * B_hat[..., 2]
    kBz = KX * B_hat[..., 1] - KY * B_hat[..., 0]
    Ax = jnp.fft.ifftn(1j * kBx / K2_safe * zero_mask, axes=(0, 1, 2)).real
    Ay = jnp.fft.ifftn(1j * kBy / K2_safe * zero_mask, axes=(0, 1, 2)).real
    Az = jnp.fft.ifftn(1j * kBz / K2_safe * zero_mask, axes=(0, 1, 2)).real
    A = jnp.stack([Ax, Ay, Az], axis=-1)
    return 0.5 * jnp.sum(A * B, axis=-1)


def _energy_density_k4_saturated(
    u: jnp.ndarray,
    q: jnp.ndarray,
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
    """Per-site energy density for K4 mode (mirrors _energy_density_saturated).
    Uses finite-rotation strain and bond wryness; n extracted from q directly."""
    eps = _compute_strain_q_jax(u, q, dx)
    kappa = _bond_wryness_jax(q, dx)
    eps_T = jnp.swapaxes(eps, -1, -2)
    eps_sym = 0.5 * (eps + eps_T)
    eps_antisym = 0.5 * (eps - eps_T)
    trace_eps = eps[..., 0, 0] + eps[..., 1, 1] + eps[..., 2, 2]
    W_cauchy = (2.0 / 3.0) * trace_eps ** 2 + jnp.sum(eps_sym ** 2, axis=(-1, -2))
    W_micropolar = jnp.sum(eps_antisym ** 2, axis=(-1, -2))
    W_kappa = jnp.sum(kappa ** 2, axis=(-1, -2))
    eps_sq = jnp.sum(eps ** 2, axis=(-1, -2))
    kappa_sq = W_kappa
    S_eps_sq = jnp.clip(1.0 - eps_sq / epsilon_yield ** 2, 0.0, 1.0)
    S_kappa_sq = jnp.clip(1.0 - kappa_sq / omega_yield ** 2, 0.0, 1.0)
    # Reflection density (inline to share eps/kappa; cf:441-502 analog with K4 strains)
    A_sq = jnp.clip(
        eps_sq / epsilon_yield ** 2 + kappa_sq / omega_yield ** 2, 0.0, 1.0 - 1e-10,
    )
    S_refl = jnp.sqrt(1.0 - A_sq)
    grad_S = _tetrahedral_gradient(S_refl[..., None])[..., 0, :] / dx
    W_refl = (1.0 / 16.0) * jnp.sum(grad_S ** 2, axis=-1) / (S_refl ** 2 + 1e-6)
    W_op10 = _op10_density_q(q, dx)
    W_hopf = _hopf_density_q(q, dx)
    W = (
        (W_cauchy * G + W_micropolar * G_c) * S_eps_sq
        + W_kappa * gamma * S_kappa_sq
        + W_op10 * k_op10
        + W_refl * k_refl
        + W_hopf * k_hopf
    )
    return W * mask_alive.astype(W.dtype)


def _total_energy_k4(
    u, q, mask_alive, dx, G, G_c, gamma, omega_yield, epsilon_yield, k_op10, k_refl, k_hopf,
):
    """Scalar total energy for K4 mode (for value_and_grad)."""
    return jnp.sum(_energy_density_k4_saturated(
        u, q, mask_alive, dx, G, G_c, gamma, omega_yield, epsilon_yield, k_op10, k_refl, k_hopf,
    ))


_val_and_grad_k4 = jax.jit(jax.value_and_grad(_total_energy_k4, argnums=(0, 1)))
_total_energy_k4_jit = jax.jit(_total_energy_k4)


def _left_torque_from_grad(g: jnp.ndarray, q: jnp.ndarray) -> jnp.ndarray:
    """Left-trivialized torque τ=½Im(g⊗q̄), g=dW/dq∈ℝ⁴→τ∈ℝ³.
    Numerically verified per-component formula (NOT q̄⊗g):
      τ₁=½(−g₀q₁+g₁q₀−g₂q₃+g₃q₂)
      τ₂=½(−g₀q₂+g₁q₃+g₂q₀−g₃q₁)
      τ₃=½(−g₀q₃−g₁q₂+g₂q₁+g₃q₀)"""
    g0, g1, g2, g3 = g[..., 0], g[..., 1], g[..., 2], g[..., 3]
    q0, q1, q2, q3 = q[..., 0], q[..., 1], q[..., 2], q[..., 3]
    return jnp.stack([
        0.5 * (-g0 * q1 + g1 * q0 - g2 * q3 + g3 * q2),
        0.5 * (-g0 * q2 + g1 * q3 + g2 * q0 - g3 * q1),
        0.5 * (-g0 * q3 - g1 * q2 + g2 * q1 + g3 * q0),
    ], axis=-1)


_left_torque_from_grad_jit = jax.jit(_left_torque_from_grad)


# Numpy helpers for Lie-group drift step (outside JAX trace)


def _quat_mul_np(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Hamilton product a⊗b (numpy), shape (*,4)."""
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([
        a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
        a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
        a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1,
        a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0,
    ], axis=-1)


def _quat_exp_np(v: np.ndarray) -> np.ndarray:
    """Quaternion exp((0,v)): (cos|v|, v·sinc(|v|/π)), shape (*,3)->(*,4).
    np.sinc(x)=sin(πx)/(πx) so sinc(|v|/π)=sin(|v|)/|v|; safe at zero."""
    v_norm = np.linalg.norm(v, axis=-1, keepdims=True)   # (*,1)
    cos_v = np.cos(v_norm)
    sinc_v = np.sinc(v_norm / np.pi)                     # = sin(|v|)/|v|
    return np.concatenate([cos_v, v * sinc_v], axis=-1)  # (*,4)
