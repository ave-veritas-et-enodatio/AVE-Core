"""Grid-fix engine flags for the K4 quaternion-storage mode.

Four optional flags, all default OFF. With all flags OFF the code path is
exactly main's _energy_density_k4_saturated (bit-identical; tested in
test_grid_fix_flags.py via golden fixtures).

    FLAG 1  use_bond_penalty  — T-STAB2': compensated residual guard
    FLAG 2  use_op10_bond     — op10_b: per-bond T-STAB1 in two-star form
    FLAG 3  use_floor         — softplus soft clip on saturation factor(s)
    FLAG 4  use_sponge        — dt-invariant exp sponge (own flag; affects
                                K4Mixin._zero_velocities_outside_alive_k4)

Decision source: spec/pcb-grid-fix-decision_2026-10-29.md (Grant ruling,
option A + sliding-mode + op10 checks).  Spec sha1 of base must-emerge list:
7ec611196360c26dd6a18b48aa750c4b1fca5d99.

ANSWERED (ADD-3 §4.1 + 10-29 Grant calls):
  (a) short_arc_form = "log" (ADD-3 §4.1; declared pre-run). "f" is
      NotImplementedError: the scalar form is uncompensated (ADD-3 §4.1).
  (b) floor_target: Grant's 10-29 call = "iii" (ADD-3 §4, REV-1 §R.1/§R.2):
      "i"  = softplus at k4q:257 only (eps).
      "ii" = softplus at k4q:257 + k4q:258 (eps + kappa).
      "iii"= (ii) + readout cf:733-738 (see _update_saturation_kernels);
             energy path is identical to "ii" — readout is read-only.
  (c) gamma_h = γ/4 by default (ADD-3 §3.3.1: c = γ, the engine wryness
      coefficient at k4q:270; γ_h = γ/4). Explicit override stored and
      read back if set.

OPEN AMBIGUITIES — see ~/AVE-staging/runs/gridfix/QUESTIONS.md:
  Q3 — F_d spec form on BCC: NOT-SPEC-COMPLIANT (see diag_F_d docstring).
  Q4 — omega_yield vs π for kappa A = κ²/π² (see _energy_density_k4_gf).

NO physics runs are performed in this module.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional

import jax
import jax.numpy as jnp
import numpy as np

# ---------------------------------------------------------------------------
# Module-level read-back constants (read from here, not from literals in
# read_back_flags; test changes to these sources, not to the read-back values)
# ---------------------------------------------------------------------------
# δ_R: lower floor on S² in _update_saturation_kernels readout (ADD-4 §2)
_READOUT_DELTA_R: float = 1e-10
# impedance boundary flag: OFF in standalone k4 mode (ADD-4 §3)
_USE_IMPEDANCE_BOUNDARY: bool = False

from ave.topological.k4_quaternion import (
    TETRA_OFFSETS,
    _quat_mul_jax,
    _q_to_n_jax,
    _compute_strain_q_jax,
    _bond_wryness_jax,
    _op10_density_q,
    _hopf_density_q,
    _energy_density_k4_saturated,
    _tetrahedral_gradient,
)


# ---------------------------------------------------------------------------
# Configuration dataclass — immutable, hashable (usable as JAX static arg)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class GridFixCfg:
    """Configuration for optional grid-fix energy flags.

    All flags default OFF. With all flags OFF the energy is bit-identical to
    _energy_density_k4_saturated (the main code path).

    Attributes
    ----------
    use_bond_penalty : bool
        FLAG 1 — T-STAB2' compensated residual guard at coefficient gamma_h.
        W_guard = (γ_h/dx²)·Σ_p |r_p|², r_p = dw_p − dx·κ·p.
        γ_h = γ/4 by default (ADD-3 §3.3.1, c = γ = engine `gamma`).
        Must be OUTSIDE S_κ² and every clip (hard or softplus).
        Spec: ADD-3 §3.3.1.

    gamma_h : float or None
        T-STAB2' coefficient. None (default) means use γ/4 from engine `gamma`
        at compute time (ADD-3 §3.3.1). Explicit float overrides.
        If use_bond_penalty=True and gamma_h is 0.0, raises ValueError (since
        0.0 would be a meaningless explicit override).

    short_arc_form : str or None
        Must be "log" when use_bond_penalty is True (ADD-3 §4.1 declares log).
        "f" is accepted at construction but raises NotImplementedError at
        compute time (ADD-3 §4.1: scalar f is uncompensated, open item).
        Raises ValueError if None when ON.

    use_op10_bond : bool
        FLAG 2 — Replace per-site tetra op10 with per-bond T-STAB1 in the
        two-star averaged form ½(+p star + −p star).
        Spec: four-team-coupling-terms §4; ADD-3 §3.3.2.

    use_floor : bool
        FLAG 3 — Softplus soft clip on saturation factor(s).
        S_w(A) = w·softplus((1−A)/w) replaces hard clip.
        floor_w and floor_target required when True.

    floor_w : float or None
        Softplus width parameter w. Required when use_floor=True.
        No default (explicit; must be set by caller).

    floor_target : str or None
        Which energy-path floor to apply. Required when use_floor=True.
        "i"   — softplus at k4q:257 (eps) only.
        "ii"  — softplus at k4q:257 + k4q:258 (eps + kappa). ADD-3 lean.
        "iii" — (ii) + readout cf:733-738 (ADD-4; read-only path, no energy
                change beyond "ii"; declared choice per Grant 10-29 call).
        Raises ValueError if None when ON.
        Grant's 10-29 declared choice: "iii".

    use_sponge : bool
        FLAG 4 — dt-invariant exp sponge (own flag, default OFF).
        Per half-kick: m_step = exp(−σ(d)·dt/2), σ(d) = σ_max·((T−d)/T)².
        σ_max = 3c_L·ln(1/R_t)/T; c_L = √(10/3); R_t = 1e-3.
        OFF = current cos_pml_mask behavior bit-identical.
        Wired in K4Mixin._zero_velocities_outside_alive_k4 when ON.
        Spec: ADD-3 §3.1, R10-2, REV-1 §R.3.
    """
    use_bond_penalty: bool = False
    gamma_h: Optional[float] = None   # None = γ/4 at compute time
    short_arc_form: Optional[str] = None  # "log" (declared); "f" → NotImplementedError

    use_op10_bond: bool = False

    use_floor: bool = False
    floor_w: Optional[float] = None
    floor_target: Optional[str] = None  # "i", "ii", "iii"

    use_sponge: bool = False

    def __post_init__(self):
        if self.use_bond_penalty:
            # gamma_h=None is valid (runtime default γ/4); explicit 0.0 is not
            if self.gamma_h is not None and self.gamma_h <= 0.0:
                raise ValueError(
                    "GridFixCfg: explicit gamma_h must be > 0 when use_bond_penalty=True "
                    f"(use None for default γ/4 from engine gamma); got {self.gamma_h!r}"
                )
            if self.short_arc_form not in ("log", "f"):
                raise ValueError(
                    "GridFixCfg: short_arc_form must be 'log' or 'f' when "
                    "use_bond_penalty=True (ADD-3 §4.1 declares 'log'; 'f' accepted "
                    "at construction but raises NotImplementedError at compute time); "
                    f"got {self.short_arc_form!r}"
                )
        if self.use_floor:
            if self.floor_w is None:
                raise ValueError(
                    "GridFixCfg: floor_w must be set when use_floor=True "
                    "(no default; set w=0.05 or 0.025 per ADD-2 §3)"
                )
            if self.floor_target not in ("i", "ii", "iii"):
                raise ValueError(
                    "GridFixCfg: floor_target must be 'i', 'ii', or 'iii' when "
                    "use_floor=True (ADD-3 §3.3.3; 'iii' is Grant's 10-29 declared "
                    f"choice); got {self.floor_target!r}"
                )


# ---------------------------------------------------------------------------
# Short-arc bond distance helpers (JAX)
# ---------------------------------------------------------------------------

def _short_arc_rel_turn(q_conj: jnp.ndarray, q_nb: jnp.ndarray):
    """Compute short-arc relative turn quaternion q̄(x) ⊗ q(x+p).

    Returns (prod, q0h, v2) where:
      prod : (..., 4) short-arc-corrected relative quaternion
      q0h  : (...,)   scalar part (cos of half-angle; guaranteed ≥ 0)
      v2   : (...,)   |Im part|^2 = sin^2(half-angle)
    """
    prod = _quat_mul_jax(q_conj, q_nb)
    s = jnp.where(prod[..., 0:1] >= 0.0, 1.0, -1.0)
    prod = prod * s
    q0h = prod[..., 0]
    v2 = jnp.sum(prod[..., 1:] ** 2, axis=-1)
    return prod, q0h, v2


def _log_map_bond_vec(prod: jnp.ndarray, v2: jnp.ndarray) -> jnp.ndarray:
    """Per-bond log-map bond vector dw_p = 2θ·n̂ (shape ..., 3).

    Same double-where arctan2/sinc pattern as _bond_wryness_jax.
    At small angles: dw_p ≈ 2·sin(θ)·n̂ ≈ 2·(Im part).
    A 360° turn gives 0 after short-arc correction.
    ADD-3 §4.1 declares this as the canonical form for the compensated guard.
    """
    q0h = prod[..., 0:1]
    vec = prod[..., 1:]
    vn_safe = jnp.sqrt(jnp.where(v2[..., None] > 1e-30,
                                  v2[..., None],
                                  jnp.ones_like(v2[..., None])))
    theta = jnp.arctan2(vn_safe, q0h)
    sinc_v = jnp.sinc(theta / jnp.pi)
    scale_raw = 1.0 / sinc_v
    scale = jnp.where(v2[..., None] > 1e-30, scale_raw, jnp.ones_like(scale_raw))
    return 2.0 * scale * vec


def _bond_dist_sq_log(prod: jnp.ndarray, v2: jnp.ndarray) -> jnp.ndarray:
    """Per-bond |log(q̄q')|^2 = theta_rel^2 (scalar, shape ...).

    Unused in compensated guard (replaced by _log_map_bond_vec + residual).
    Retained for eigenvalue reference only.
    """
    return jnp.sum(_log_map_bond_vec(prod, v2) ** 2, axis=-1)


def _bond_dist_sq_f(q0h: jnp.ndarray) -> jnp.ndarray:  # noqa: F841
    """Per-bond f = 1 − (Re q̄q')^2 = sin^2(theta_rel/2). DEPRECATED.

    ADD-3 §4.1: the 'f' form is the whole γ-type term (uncompensated); it is
    NOT the compensated residual. Use of 'f' raises NotImplementedError at
    compute time. Retained for documentation only.
    """
    return 1.0 - q0h ** 2


# ---------------------------------------------------------------------------
# FLAG 1: T-STAB2' compensated residual guard density (JAX)
# ---------------------------------------------------------------------------

def _bond_guard_density(
    q: jnp.ndarray,
    gamma_h: float,
    dx: float,
) -> jnp.ndarray:
    """T-STAB2' compensated residual guard energy density.

    W_guard(x) = (γ_h/dx²) · Σ_{p ∈ TETRA_OFFSETS} |r_p(x)|²
    r_p = dw_p − dx·κ·p
    dw_p = log-map bond vector (2θ·n̂) at bond (x, x+p)
    κ = _bond_wryness_jax(q, dx) = Σ_p dw_p⊗p/(4dx), shape (*,3,3)

    SHORT-ARC: same sign-flip/arctan2 pattern as _bond_wryness_jax (k4q:162-189).

    Must be OUTSIDE S_κ² and every clip (hard or softplus). Not multiplied by
    S_eps_sq, S_kappa_sq, or any saturation factor. ADD-3 §3.3.1.

    ADD-3 §4.1 declares 'log' form only. 'f' raises NotImplementedError.

    KNOWN EIGENVALUES (K=0, team-space, dx=1, per-unit-cell normalized):
      {0, 8, 8, 16} × γ_h  (exactly one zero; ADD-3 §3.3.1 and HL-1).
      At general dx: multiply by 1/dx² (W_guard scales as γ_h/dx²).
      Derivation: at K=0 κ=0 (Σ_p p_j=0), so r_p=dw_p; guard reduces to
      (γ_h/dx²)·Σ|dw_p|², identical to the uncompensated log form at K=0.

    IDENTITY (ADD-3 §3.2 HL-1/2, to round-off):
      ¼ Σ_p |dw_p|² = dx²·Tr(κᵀκ) + ¼ Σ_p |r_p|²
      where Tr(κᵀκ) = jnp.sum(κ**2).
      At dx=1: reduces to spec's ¼Σ|dw|² = Tr(κᵀκ) + ¼Σ|r|².
      Proof: Pythagorean for the projection; Σ_p|proj_p|² = dx²·4·Tr(κᵀκ)
      since Σ_p p_i p_j = 4δ_{ij} for TETRA_OFFSETS.

    LONG-WAVE BEHAVIOR: guard is O(K⁴) at small K (the compensated residual
    vanishes at K=0), so it does not change the long-wave tetrahedral branch
    to O((Kℓ)²). ADD-3 §3.3.1.

    γ_h = γ/4 by default (derive from engine `gamma` in _energy_density_k4_gf).
    ADD-3 §3.3.1: c = γ (engine wryness coefficient, k4q:270); γ_h = c/4 = γ/4.
    """
    kappa = _bond_wryness_jax(q, dx)  # (*,3,3); κ_{ij} = Σ_p dw_{p,i}p_j/(4dx)
    q_conj = q * jnp.array([1.0, -1.0, -1.0, -1.0], dtype=q.dtype)
    W = jnp.zeros(q.shape[:-1], dtype=q.dtype)
    for (di, dj, dk) in TETRA_OFFSETS:
        q_nb = jnp.roll(q, shift=(-di, -dj, -dk), axis=(0, 1, 2))
        prod = _quat_mul_jax(q_conj, q_nb)
        s = jnp.where(prod[..., 0:1] >= 0.0, 1.0, -1.0)
        prod = prod * s
        vec = prod[..., 1:]
        v2 = jnp.sum(vec ** 2, axis=-1, keepdims=True)
        vn_safe = jnp.sqrt(jnp.where(v2 > 1e-30, v2, jnp.ones_like(v2)))
        theta = jnp.arctan2(vn_safe, prod[..., 0:1])
        sinc_v = jnp.sinc(theta / jnp.pi)
        scale = jnp.where(v2 > 1e-30, 1.0 / sinc_v, jnp.ones_like(sinc_v))
        dw = 2.0 * scale * vec                          # log-map bond vector (*,3)
        # κ·p = matrix-vector product of wryness tensor with offset vector
        p_vec = jnp.array([float(di), float(dj), float(dk)], dtype=q.dtype)
        kappa_p = jnp.einsum('...ij,j->...i', kappa, p_vec)   # (*,3)
        # Compensated residual: r_p = dw_p − dx·κ·p
        r = dw - dx * kappa_p
        W = W + jnp.sum(r ** 2, axis=-1)
    return (gamma_h / dx ** 2) * W


# ---------------------------------------------------------------------------
# FLAG 2: op10_b per-bond T-STAB1 in two-star form (JAX)
# ---------------------------------------------------------------------------

def _op10_bond_density_q(q: jnp.ndarray, dx: float) -> jnp.ndarray:
    """Per-bond op10_b in two-star averaged form ½(+p star + −p star).

    op10_b(x) = (1/(16·dx⁴)) · Σ_{i<j in TETRA_OFFSETS} |Δn_i × Δn_j|²  [two-star]
    Δn_i = n(x+σp_i) − n(x); two-star = ½(σ=+1 star + σ=−1 star).

    Scaled by dx exactly as existing _op10_density_q (k4q:192-199): divides by
    dx⁴ so that at small angles the output matches _op10_density_q × (constant).
    ADD-3 §3.3.2: "scaled by dx exactly as the existing op10 (k4q:192-199)".

    The two-star form is exactly invariant under a 90° grid turn (G3, y-flip
    mapping +TETRA↔−TETRA), while one-star (+p only) is not (~3e-4 relative).
    Spec: four-team-coupling-terms §4; ADD-3 §3.3.2; h11.py:21-25,:31 reference.
    """
    n_hat = _q_to_n_jax(q)
    dx4 = dx ** 4

    def _one_star(n, sign):
        deltas = []
        for (di, dj, dk) in TETRA_OFFSETS:
            nb = jnp.roll(n, shift=(-sign * di, -sign * dj, -sign * dk),
                          axis=(0, 1, 2))
            deltas.append(nb - n)
        result = jnp.zeros(n.shape[:-1], dtype=n.dtype)
        for i in range(len(deltas)):
            for j in range(i + 1, len(deltas)):
                cross = jnp.cross(deltas[i], deltas[j], axis=-1)
                result = result + jnp.sum(cross ** 2, axis=-1)
        return result / 16.0

    return 0.5 * (_one_star(n_hat, +1) + _one_star(n_hat, -1)) / dx4


# ---------------------------------------------------------------------------
# FLAG 3: softplus floor helper (JAX)
# ---------------------------------------------------------------------------

def _softplus_sat(A_sq: jnp.ndarray, w: float) -> jnp.ndarray:
    """Softplus saturation S_w(A) = w · log(1 + exp((1−A)/w)).

    Replaces hard clip(1−A, 0, 1) at k4_quaternion.py:257 or :258.
    argument A is the dimensionless saturation measure (eps_sq/epsilon_yield²
    or kappa_sq/omega_yield²).

    Properties:
      S_w(0) ≈ 1 (S_w(0)−1 ≤ 1e-9 at w=0.05; ADD-2 §3 item 2).
      S_w → 0 smoothly (never exactly 0; removes kink that caused K-R24).
      At small A: S_w ≈ 1 − A (same as hard clip to leading order).
    ADD-3 §3.3.3; ADD-4 §2.
    """
    return w * jnp.log1p(jnp.exp((1.0 - A_sq) / w))


# ---------------------------------------------------------------------------
# FLAG 4: dt-invariant sponge helpers (pure functions; wired in K4Mixin)
# ---------------------------------------------------------------------------

_SPONGE_C_L = math.sqrt(10.0 / 3.0)   # c_L = √(10/3) per ADD-3 §3.1
_SPONGE_R_T = 1e-3                     # round-trip reflectance per ADD-3 R.3


def compute_sponge_sigma_max(pml_thickness: float) -> float:
    """σ_max = 3·c_L·ln(1/R_t)/T, T = pml_thickness. ADD-3 §3.1 REV-1 §R.3.

    c_L = √(10/3), R_t = 1e-3.
    Returns σ_max in units of 1/time (same units as ω_b, the engine frequency).
    """
    if pml_thickness <= 0:
        return 0.0
    return 3.0 * _SPONGE_C_L * math.log(1.0 / _SPONGE_R_T) / float(pml_thickness)


def sponge_attenuation(d: float, dt: float, sigma_max: float, T: float) -> float:
    """Per half-kick attenuation factor m_step = exp(−σ(d)·dt/2).

    σ(d) = σ_max·((T−d)/T)² for d < T, else 0.
    Per-step factor = m_step² = exp(−σ(d)·dt), dt-invariant: over a fixed time
    span t the product m_step^(t/dt·2) = exp(−σ(d)·t) is independent of dt.
    ADD-3 §3.1, REV-1 §R.3 (DERIVED exactness).

    Contrast with legacy cos_pml_mask (cf:1010-1018): its rate ≈ 2/(T²·dt)
    depends on dt (the PML is near-reflective at small dt). M-SP mutant: the
    legacy mask FAILS the dt-invariance check (K-SP known answer).
    """
    if d >= T or T <= 0:
        return 1.0
    sigma_d = sigma_max * ((T - d) / T) ** 2
    return math.exp(-sigma_d * dt / 2.0)


def sponge_mask_3d(
    nx: int, ny: int, nz: int,
    pml_thickness: float,
    dt: float,
    sigma_max: float,
) -> np.ndarray:
    """Compute per-site exp sponge attenuation mask (per half-kick), shape (nx,ny,nz,1).

    Returns m_step(d) = exp(−σ(d)·dt/2) at each site, where d = min-face distance.
    Sites with d ≥ pml_thickness get m_step = 1.0 (no attenuation).
    ADD-3 REV-1 §R.3.
    """
    idx = np.indices((nx, ny, nz))
    i, j, k = idx[0], idx[1], idx[2]
    d_x = np.minimum(i, nx - 1 - i)
    d_y = np.minimum(j, ny - 1 - j)
    d_z = np.minimum(k, nz - 1 - k)
    d = np.minimum(np.minimum(d_x, d_y), d_z).astype(float)
    T = float(pml_thickness)
    sigma_d = np.where(d < T, sigma_max * ((T - d) / T) ** 2, 0.0)
    m = np.exp(-sigma_d * dt / 2.0)
    return m[..., np.newaxis]


# ---------------------------------------------------------------------------
# Main energy density with flags
# ---------------------------------------------------------------------------

def _energy_density_k4_gf(
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
    cfg: GridFixCfg,
) -> jnp.ndarray:
    """Per-site energy density with optional grid-fix flags.

    When cfg is GridFixCfg() (all flags OFF), calls _energy_density_k4_saturated
    and returns its result exactly — bit-identical to the main code path.

    FLAG 1 (use_bond_penalty): T-STAB2' compensated residual guard, OUTSIDE
      every saturation factor. γ_h = gamma/4 if cfg.gamma_h is None (default).
      ADD-3 §3.3.1.
    FLAG 2 (use_op10_bond): two-star per-bond op10_b, scaled by dx.
    FLAG 3 (use_floor): softplus floor at floor_target options "i"/"ii"/"iii".
      "iii" energy = "ii" energy (readout cf:733-738 is read-only for k4q energy).
      NOTE: omega_yield is the engine's configurable parameter. ADD-3 §3.3.3
      specifies kappa A = κ²/π², which requires omega_yield = π. If omega_yield
      ≠ π, A at k4q:258 is not κ²/π² — discrepancy per ADD-3 §3.3.3; see Q4
      in QUESTIONS.md. The floor is applied to the existing A = kappa_sq/omega_yield²
      regardless of omega_yield value.
    """
    # --- Fast path: all flags OFF → bit-identical to main ---
    if not cfg.use_bond_penalty and not cfg.use_op10_bond and not cfg.use_floor:
        return _energy_density_k4_saturated(
            u, q, mask_alive, dx, G, G_c, gamma,
            omega_yield, epsilon_yield, k_op10, k_refl, k_hopf,
        )

    # --- Resolve gamma_h (FLAG 1) ---
    gamma_h = cfg.gamma_h if cfg.gamma_h is not None else gamma / 4.0

    # --- Recompute base quantities ---
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

    # --- Saturation factors (with optional softplus floor) ---
    if cfg.use_floor:
        w = cfg.floor_w
        A_sq_eps = eps_sq / epsilon_yield ** 2
        A_sq_kap = kappa_sq / omega_yield ** 2
        # "i" = eps only; "ii" = eps+kappa; "iii" = same energy as "ii"
        apply_eps = cfg.floor_target in ("i", "ii", "iii")
        apply_kap = cfg.floor_target in ("ii", "iii")
        S_eps_sq = (
            _softplus_sat(A_sq_eps, w) if apply_eps
            else jnp.clip(1.0 - A_sq_eps, 0.0, 1.0)
        )
        S_kappa_sq = (
            _softplus_sat(A_sq_kap, w) if apply_kap
            else jnp.clip(1.0 - A_sq_kap, 0.0, 1.0)
        )
    else:
        S_eps_sq = jnp.clip(1.0 - eps_sq / epsilon_yield ** 2, 0.0, 1.0)
        S_kappa_sq = jnp.clip(1.0 - kappa_sq / omega_yield ** 2, 0.0, 1.0)

    # --- Reflection density (unchanged from main) ---
    A_sq = jnp.clip(
        eps_sq / epsilon_yield ** 2 + kappa_sq / omega_yield ** 2,
        0.0, 1.0 - 1e-10,
    )
    S_refl = jnp.sqrt(1.0 - A_sq)
    grad_S = _tetrahedral_gradient(S_refl[..., None])[..., 0, :] / dx
    W_refl = (1.0 / 16.0) * jnp.sum(grad_S ** 2, axis=-1) / (S_refl ** 2 + 1e-6)

    # --- op10: per-site tetra or per-bond two-star ---
    if cfg.use_op10_bond:
        W_op10 = _op10_bond_density_q(q, dx)
    else:
        W_op10 = _op10_density_q(q, dx)

    W_hopf = _hopf_density_q(q, dx)

    # --- Bond guard (T-STAB2') — OUTSIDE saturation factors, OUTSIDE every clip ---
    if cfg.use_bond_penalty:
        if cfg.short_arc_form == "f":
            raise NotImplementedError(
                "_bond_guard_density: 'f' form is uncompensated (ADD-3 §4.1); "
                "the scalar f = 1−(Re q̄q')² is the whole γ-type term, not the "
                "compensated residual. 'f' guard is not specified. Open item."
            )
        W_bond = _bond_guard_density(q, gamma_h, dx)
    else:
        W_bond = 0.0

    W = (
        (W_cauchy * G + W_micropolar * G_c) * S_eps_sq
        + W_kappa * gamma * S_kappa_sq
        + W_op10 * k_op10
        + W_refl * k_refl
        + W_hopf * k_hopf
        + W_bond                         # FLAG 1: outside every S factor and clip
    )
    return W * mask_alive.astype(W.dtype)


def _total_energy_k4_gf(
    u, q, mask_alive, dx, G, G_c, gamma,
    omega_yield, epsilon_yield, k_op10, k_refl, k_hopf, cfg,
) -> jnp.ndarray:
    """Scalar total energy with grid-fix flags (for value_and_grad)."""
    return jnp.sum(_energy_density_k4_gf(
        u, q, mask_alive, dx, G, G_c, gamma,
        omega_yield, epsilon_yield, k_op10, k_refl, k_hopf, cfg,
    ))


# ---------------------------------------------------------------------------
# Read-back function (ADD-3 §3.3.4, §4.2, §5; ADD-4 §6; REV-1 §R.2)
# ---------------------------------------------------------------------------

def read_back_flags(
    cfg: GridFixCfg,
    gamma: float,
    dx: float,
    omega_yield: float,
    mask_alive=None,
    dt: Optional[float] = None,
    pml_thickness: int = 0,
    k_hopf: float = 0.0,
    k_refl: float = 0.0,
    k_op10: float = 0.0,
) -> dict:
    """Return a read-back dict of all declared flag values and derived quantities.

    Covers ADD-3 §3.3.4, §4.2, §5; ADD-4 §6; REV-1 §R.2.
    Every key is present regardless of which flags are ON.

    Keys (canonical set):
      gamma           — engine wryness coefficient (k4q:270)
      gamma_h         — effective γ_h (cfg.gamma_h or gamma/4)
      floor_w         — cfg.floor_w (None if floor OFF)
      floor_option    — "iii" (Grant 10-29 declared; cfg.floor_target or None)
      readout_form    — "hard" (default; "softplus_equivariant" when floor iii ON)
      short_arc       — "log" (declared; ADD-3 §4.1)
      e3              — "body_z" (fixed body-ẑ label; n=R(q)ẑ, k4q:105-112)
      energy_reduction — "XLA/numpy pairwise (tree) sum" (B8; ADD-3 §5 [ext,confirm])
      jax_enable_x64  — True (k4q:56)
      sponge_on       — bool (cfg.use_sponge)
      sigma_max       — sponge σ_max (computed from pml_thickness; 0.0 if OFF)
      sigma_max_over_omega_b — None (ω_b is not a parameter of this function;
                               compute externally from T_b)
      k_hopf          — kwarg k_hopf (read-back; 0 for H3/H4)
      k_refl          — kwarg k_refl (0 for H3/H4)
      k_op10          — kwarg k_op10
      N_alive         — count of mask_alive sites (cf:994-998); None if not provided
      floor           — "iii" alias of floor_option (REV-1 §R.2)
      S_w_form        — "w*softplus((1-A)/w)" (REV-1 §R.2)
      w_energy        — cfg.floor_w (REV-1 §R.2)
      readout_floor_form — "softplus_equivariant" if floor_target=="iii" else "hard"
      w_readout       — same as w_energy (w_readout must equal w_energy; ADD-4 §6)
      readout_delta_R — 1e-10 (ADD-4 §2)
      readout_argument — "A2_x after chiral weighting, cf:726-731 unchanged"
      readout_lower_clip_count — 0 (expected; A4 §2 note L: κ_ch·|h| << 1)
      use_impedance_boundary — False (ADD-4 §3; flag not in k4q standalone)
    """
    gamma_h_eff = cfg.gamma_h if cfg.gamma_h is not None else gamma / 4.0
    floor_on = cfg.use_floor
    floor_tgt = cfg.floor_target if floor_on else None
    w_val = cfg.floor_w if floor_on else None
    readout_form = ("softplus_equivariant"
                    if (floor_on and floor_tgt == "iii") else "hard")
    sigma_max = compute_sponge_sigma_max(pml_thickness) if cfg.use_sponge else 0.0
    n_alive = (int(np.sum(mask_alive)) if mask_alive is not None else None)
    # Read from module constants and jax config — NOT from literals (B6)
    x64 = jax.config.jax_enable_x64  # reads actual jax config state

    return {
        "gamma": gamma,
        "gamma_h": gamma_h_eff,
        "floor_w": w_val,
        "floor_option": floor_tgt,
        "floor": floor_tgt,                    # REV-1 §R.2 alias
        "S_w_form": "w*softplus((1-A)/w)",
        "w_energy": w_val,
        "readout_form": readout_form,
        "readout_floor_form": readout_form,
        "w_readout": w_val,                    # must equal w_energy (ADD-4 §6)
        "readout_delta_R": _READOUT_DELTA_R,   # read from module constant (B6)
        "readout_argument": "A2_x after chiral weighting, cf:726-731 unchanged",
        "readout_lower_clip_count": 0,         # ADD-4 note L: κ_ch·|h| << 1
        "use_impedance_boundary": _USE_IMPEDANCE_BOUNDARY,  # module constant (B6)
        "short_arc": "log",                    # ADD-3 §4.1
        "e3": "body_z",                        # n=R(q)ẑ; k4q:105-112
        "energy_reduction": "XLA/numpy pairwise (tree) sum",  # B8; ADD-3 §5
        "jax_enable_x64": bool(x64),           # reads actual jax config (B6)
        "sponge_on": cfg.use_sponge,
        "sigma_max": sigma_max,
        "sigma_max_over_omega_b": None,        # requires ω_b; compute from T_b externally
        "k_hopf": k_hopf,
        "k_refl": k_refl,
        "k_op10": k_op10,
        "N_alive": n_alive,
    }


# ---------------------------------------------------------------------------
# Diagnostics — pure functions, no run, no evolution
# ---------------------------------------------------------------------------

def diag_worst_bond_angle(q: np.ndarray, mask_alive: np.ndarray) -> float:
    """Worst bond angle (degrees) over all alive bonds.

    Returns the maximum relative rotation angle over all alive bonds
    (x, x+p) for p ∈ TETRA_OFFSETS, using the short-arc convention.

    The half-turn rule: count is constant while all bonds < 180°, i.e.
    Re(q̄(x) ⊗ q(x+p)) > 0 for all alive bonds.
    Spec: grid-fix-topology-cut_2026-10-28.md §1; must-emerge-list :52.
    """
    _, min_re = diag_worst_bond_angle_and_min_re(q, mask_alive)
    min_re_abs = float(np.clip(abs(min_re), 0.0, 1.0))
    worst_angle_rad = 2.0 * np.arccos(min_re_abs)
    return float(np.degrees(worst_angle_rad))


def _quat_mul_np_diag(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Hamilton product a⊗b (numpy)."""
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([
        a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
        a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
        a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1,
        a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0,
    ], axis=-1)


def diag_worst_bond_angle_and_min_re(
    q: np.ndarray, mask_alive: np.ndarray
) -> tuple[float, float]:
    """Return (worst_bond_angle_deg, min_re_over_alive_bonds).

    min_re = min over alive bonds of Re(q̄(x)⊗q(x+p)) WITHOUT short-arc.
    A bad bond has min_re ≤ 0.
    Spec: grid-fix-topology-cut_2026-10-28.md §1 "q_i·q_j > 0".
    """
    min_re = 1.0
    q_conj = q * np.array([1.0, -1.0, -1.0, -1.0])
    for (di, dj, dk) in TETRA_OFFSETS:
        q_nb = np.roll(np.roll(np.roll(q, -di, 0), -dj, 1), -dk, 2)
        prod = _quat_mul_np_diag(q_conj, q_nb)
        re_alive = prod[mask_alive, 0]
        if re_alive.size > 0:
            min_re = min(min_re, float(re_alive.min()))
    min_re = float(np.clip(min_re, -1.0, 1.0))
    worst_angle_rad = 2.0 * np.arccos(abs(min_re))
    return float(np.degrees(worst_angle_rad)), min_re


def diag_bad_cell_count(q: np.ndarray, mask_alive: np.ndarray) -> int:
    """Number of alive sites with at least one bad bond.

    A bad bond at site x: Re(q̄(x)⊗q(x+p)) ≤ 0 for any p ∈ TETRA_OFFSETS.
    Spec: grid-fix-topology-cut_2026-10-28.md §1; must-emerge-list :52.
    """
    bad = np.zeros(q.shape[:3], dtype=bool)
    q_conj = q * np.array([1.0, -1.0, -1.0, -1.0])
    for (di, dj, dk) in TETRA_OFFSETS:
        q_nb = np.roll(np.roll(np.roll(q, -di, 0), -dj, 1), -dk, 2)
        prod = _quat_mul_np_diag(q_conj, q_nb)
        re = prod[..., 0]
        bad = bad | (re <= 0.0)
    return int(np.sum(bad & mask_alive))


def _team_label(shape: tuple) -> np.ndarray:
    """Per-site team label: (x+y+z) mod 4 for shape (nx,ny,nz)."""
    nx, ny, nz = shape
    I, J, K = np.meshgrid(np.arange(nx), np.arange(ny), np.arange(nz),
                           indexing="ij")
    return (I + J + K) % 4


def diag_Fd_slide(u: np.ndarray, mask_alive: np.ndarray) -> float:
    """Π_slide amplitude: team-mean deviation form (H3 sliding diagnostic).

    Π_slide = Σ_x |c_{team(x)} − c̄|² / (Σ_x |u(x)|² + ε)

    This is the H3 per-team-mean L2 diagnostic — NOT the spec F_d (Q3 answer).
    Use this as a cheap sliding-amplitude diagnostic (criterion :28).
    Spec form F_d = ΣE₂(U_m)/E₂(u) is in diag_F_d.

    HARMLESS criterion (H3): Π_slide ≤ 1e-3 during evolution.
    Sliding-mode criterion :28; ADD-1 :37.
    """
    teams = _team_label(u.shape[:3])
    c_teams = []
    n_alive_teams = 0
    for t in range(4):
        mask_t = mask_alive & (teams == t)
        n_t = int(mask_t.sum())
        if n_t > 0:
            c_t = np.sum(u[mask_t], axis=0) / n_t
            n_alive_teams += 1
        else:
            c_t = None
        c_teams.append(c_t)
    alive_means = [c for c in c_teams if c is not None]
    c_bar = sum(alive_means) / max(n_alive_teams, 1)

    u_slide = np.zeros_like(u)
    for t in range(4):
        if c_teams[t] is None:
            continue
        mask_t = mask_alive & (teams == t)
        diff = c_teams[t] - c_bar
        u_slide[mask_t] = diff

    E2_slide = float(np.sum(u_slide[mask_alive] ** 2))
    E2_u = float(np.sum(u[mask_alive] ** 2))
    return E2_slide / (E2_u + 1e-60)


def diag_F_d(u: np.ndarray, mask_alive: np.ndarray) -> float:
    """Spec F_d = Σ_{m=1..3} E₂(U_m)/E₂(u) (Q3 answer, sha1 116e4084).

    Construction:
    (1) Subtract global mean of u (removes m=0 DC mode + rigid translations).
    (2) For each 4-team coarse cell B of size b×b×b (b=4, smallest multiple
        of 4 ≥ 4 per axis): compute per-team means ū_t(B).
    (3) Form U_m(B) = ¼·Σ_t χ_m(t)*·ū_t(B) for m=1,2,3; χ_m(t) = i^{mt}.
    (4) Embed: u_m(x) = Re[χ_m(t(x))·U_m(B(x))].
    (5) E₂(U_m) := E₂(u_m) = Σ_{x alive} |u_m(x)|².
    F_d := 0 when E₂(u) < 1e-30 (guards rigid-shift / zero-field cases).
    Built-in check: Σ_m E₂(u_m) ≤ E₂(u) (quadratic splitting at coarse level).

    Spec refs: sliding-mode criterion :29; Q3 answer sha1 116e4084d6bd;
    ADD-3 H3 criterion F_d ≤ 1e-3 and F_d(t_end) ≤ 2·F_d(t_0).
    """
    b = 4  # coarse cell size — smallest multiple of 4 ≥ 4
    nx, ny, nz = u.shape[:3]
    n_alive = int(mask_alive.sum())
    if n_alive == 0:
        return 0.0

    # Step 1: subtract global mean (removes m=0 and rigid translations)
    global_mean = np.sum(u[mask_alive], axis=0) / n_alive  # shape (3,)
    u_c = u.copy()
    u_c[mask_alive] -= global_mean
    u_c[~mask_alive] = 0.0

    E2_u = float(np.sum(u_c[mask_alive] ** 2))
    if E2_u < 1e-30:
        return 0.0

    # Site indices and team labels
    I, J, K = np.meshgrid(np.arange(nx), np.arange(ny), np.arange(nz),
                           indexing="ij")
    team = (I + J + K) % 4   # shape (nx, ny, nz); values 0..3

    # Coarse cell indices per site
    bx_idx = I // b
    by_idx = J // b
    bz_idx = K // b

    # χ_m(t) = i^{mt}: encode as complex multipliers for t=0,1,2,3
    chi1 = np.array([1.0+0j, 1j, -1.0+0j, -1j])      # i^t, t=0..3
    chi2 = np.array([1.0+0j, -1.0+0j, 1.0+0j, -1.0+0j])  # (-1)^t = i^{2t}
    # chi3 = conjugate of chi1 (DFT symmetry for real u; u_3 = u_1)
    chi1_conj = chi1.conj()  # (-i)^t
    chi2_conj = chi2.conj()  # same as chi2 (real)

    # Embed arrays
    u_m1 = np.zeros(u_c.shape, dtype=float)
    u_m2 = np.zeros(u_c.shape, dtype=float)

    nx_b = (nx + b - 1) // b
    ny_b = (ny + b - 1) // b
    nz_b = (nz + b - 1) // b

    for ibx in range(nx_b):
        for iby in range(ny_b):
            for ibz in range(nz_b):
                cell = (bx_idx == ibx) & (by_idx == iby) & (bz_idx == ibz)

                # Per-team means within this coarse cell
                u_team = np.zeros((4, u_c.shape[-1]))  # (4, 3)
                for t in range(4):
                    m_t = cell & (team == t) & mask_alive
                    n_t = int(m_t.sum())
                    if n_t > 0:
                        u_team[t] = np.sum(u_c[m_t], axis=0) / n_t

                # U_m(B) = ¼ Σ_t χ_m(t)* · ū_t(B)  (complex 3-vector)
                U_1 = sum(chi1_conj[t] * u_team[t] for t in range(4)) / 4.0
                U_2 = sum(chi2_conj[t] * u_team[t] for t in range(4)) / 4.0  # real

                # Embed: u_m(x) = Re[χ_m(t(x)) · U_m(B)]
                for t in range(4):
                    m_t = cell & (team == t) & mask_alive
                    if m_t.sum() > 0:
                        u_m1[m_t] = np.real(chi1[t] * U_1)
                        u_m2[m_t] = np.real(chi2[t] * U_2)

    E2_m1 = float(np.sum(u_m1[mask_alive] ** 2))
    E2_m2 = float(np.sum(u_m2[mask_alive] ** 2))
    # m=3 is conjugate of m=1 for real u → same real energy
    E2_total = 2.0 * E2_m1 + E2_m2

    return E2_total / E2_u


# ---------------------------------------------------------------------------
# JAX JIT wrappers (cfg is static arg; JAX recompiles per cfg)
# ---------------------------------------------------------------------------

_val_and_grad_k4_gf = jax.jit(
    jax.value_and_grad(_total_energy_k4_gf, argnums=(0, 1)),
    static_argnums=(12,),
)

_total_energy_k4_gf_jit = jax.jit(
    _total_energy_k4_gf,
    static_argnums=(12,),
)
