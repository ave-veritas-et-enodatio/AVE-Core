"""Grid-fix engine flags for the K4 quaternion-storage mode.

Four optional flags, all default OFF. With all flags OFF the code path is
exactly main's _energy_density_k4_saturated (bit-identical; tested in
test_grid_fix_flags.py via golden fixtures).

    FLAG 1  use_bond_penalty  — T-STAB2': per-bond short-arc turn penalty
    FLAG 2  use_op10_bond     — op10_b: per-bond T-STAB1 in two-star form
    FLAG 3  use_floor         — softplus soft clip on saturation factor(s)
    FLAG 4  (diagnostics)     — pure functions, no flag needed

Decision source: spec/pcb-grid-fix-decision_2026-10-29.md (Grant ruling,
option A + sliding-mode + op10 checks).  Spec sha1 of base must-emerge list:
7ec611196360c26dd6a18b48aa750c4b1fca5d99.

OPEN AMBIGUITIES (pending Grant; see ~/AVE-staging/runs/gridfix/QUESTIONS.md):
  (a) floor_target in {"eps","kappa","both"}: Grant's call; raise if None when
      floor is ON. — spec/pcb-grid-fix-must-emerge-list_2026-10-29.md :111
  (b) short_arc_form in {"log","f"}: Grant's call; raise if None when
      bond_penalty is ON. Normalization note: the "f" form naturally gives
      eigenvalues {0,8,8,16}×gamma_h (matching the spec known-answer derived
      with the raw Euclidean chord). The "log" form gives {0,32,32,64}×gamma_h
      (4× larger at the same gamma_h). See QUESTIONS.md Q1.

NO physics runs are performed in this module.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import jax
import jax.numpy as jnp
import numpy as np

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
        FLAG 1 — T-STAB2' per-bond short-arc turn penalty at coefficient gamma_h.
        c = 4*gamma_h by spec notation (chain-theory-lessons :19); gamma_h is
        the new free parameter, NOT identified with any existing engine
        coefficient.  Spec: pcb-grid-fix-decision_2026-10-29.md §A3.

    gamma_h : float
        T-STAB2' coefficient.  Required (> 0) when use_bond_penalty is True.
        Raises ValueError if use_bond_penalty=True and gamma_h <= 0.

    short_arc_form : str or None
        Short-arc form for T-STAB2'.  Must be "log" or "f" when
        use_bond_penalty is True; raises ValueError if None when ON.
        PENDING GRANT'S CALL (see QUESTIONS.md Q1).
          "log" — |log(q̄_i q_j)|^2 = theta_rel^2.  At small angles 4×
                  the raw-chord metric; gives eigenvalues {0,32,32,64}×gamma_h.
          "f"   — 1 − (Re q̄_i q_j)^2 = sin^2(theta/2).  At small angles
                  same scale as raw-chord metric; gives {0,8,8,16}×gamma_h.
        Both forms correctly give 0 for a 360° bond turn (q→−q) and are
        invariant under sign flip of q at either site (short-arc correction).
        Spec: four-team-coupling-terms §2, must-emerge-list :103.

    use_op10_bond : bool
        FLAG 2 — Replace per-site tetra op10 with per-bond T-STAB1 in the
        two-star averaged form ½(+p star + −p star).  When ON, uses
        _op10_bond_density_q in place of _op10_density_q.
        Spec: four-team-coupling-terms §4; must-emerge-list :105.

    use_floor : bool
        FLAG 3 — Softplus soft clip on saturation factor(s).
        S_w(A^2) = w * log(1 + exp((1 − A^2) / w)) replaces the hard
        clip(1 − A^2, 0, 1) at the targeted factor(s).
        floor_w and floor_target are required when True.
        Spec: pcb-grid-fix-decision_2026-10-29.md §A3.

    floor_w : float or None
        Softplus width parameter w.  Required when use_floor is True.
        Raises ValueError if use_floor=True and floor_w is None.
        At w=0.05: S_w(0)−1 ≤ 1e-9 (ADDENDUM-2 §3 item 2). No default;
        Grant must set explicitly.

    floor_target : str or None
        Which saturation factor to apply the floor to.  Required when
        use_floor is True; raises ValueError if None when ON.
        PENDING GRANT'S CALL (see QUESTIONS.md, decision-page flag A3).
          "eps"   — apply floor to S_eps_sq (k4_quaternion.py:257) only.
          "kappa" — apply floor to S_kappa_sq (:258) only.
          "both"  — apply floor to both S_eps_sq and S_kappa_sq.
        Spec: pcb-grid-fix-decision_2026-10-29.md :70 (saturation-direction flag);
              must-emerge-list :111.
    """
    use_bond_penalty: bool = False
    gamma_h: float = 0.0
    short_arc_form: Optional[str] = None  # "log" or "f"

    use_op10_bond: bool = False

    use_floor: bool = False
    floor_w: Optional[float] = None
    floor_target: Optional[str] = None  # "eps", "kappa", "both"

    def __post_init__(self):
        if self.use_bond_penalty:
            if self.gamma_h <= 0.0:
                raise ValueError(
                    "GridFixCfg: gamma_h must be > 0 when use_bond_penalty=True; "
                    f"got gamma_h={self.gamma_h!r}"
                )
            if self.short_arc_form not in ("log", "f"):
                raise ValueError(
                    "GridFixCfg: short_arc_form must be 'log' or 'f' when "
                    "use_bond_penalty=True (PENDING GRANT'S CALL, see QUESTIONS.md Q1); "
                    f"got {self.short_arc_form!r}"
                )
        if self.use_floor:
            if self.floor_w is None:
                raise ValueError(
                    "GridFixCfg: floor_w must be set explicitly when use_floor=True "
                    "(no default; set w=0.05 or 0.025 per ADDENDUM-2 §3)"
                )
            if self.floor_target not in ("eps", "kappa", "both"):
                raise ValueError(
                    "GridFixCfg: floor_target must be 'eps', 'kappa', or 'both' when "
                    "use_floor=True (PENDING GRANT'S CALL, see QUESTIONS.md); "
                    f"got {self.floor_target!r}"
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
    q0h = prod[..., 0]            # cos(theta_rel/2), >= 0 after short-arc
    v2 = jnp.sum(prod[..., 1:] ** 2, axis=-1)  # sin^2(theta_rel/2)
    return prod, q0h, v2


def _bond_dist_sq_log(prod: jnp.ndarray, v2: jnp.ndarray) -> jnp.ndarray:
    """Per-bond |log(q̄q')|^2 = theta_rel^2.

    Uses the same double-where log-map pattern as _bond_wryness_jax.
    At small angles ≈ 4×sin^2(theta_rel/2), i.e. 4× the "f" form.
    A 360° turn (q→−q at one site) gives 0 after short-arc correction.
    Spec: must-emerge-list :103; four-team-coupling-terms §2.
    """
    q0h = prod[..., 0:1]
    vec = prod[..., 1:]
    vn_safe = jnp.sqrt(jnp.where(v2[..., None] > 1e-30,
                                  v2[..., None],
                                  jnp.ones_like(v2[..., None])))
    theta = jnp.arctan2(vn_safe, q0h)                   # half-angle
    sinc_v = jnp.sinc(theta / jnp.pi)                   # sin(θ)/θ
    scale_raw = 1.0 / sinc_v
    scale = jnp.where(v2[..., None] > 1e-30, scale_raw, jnp.ones_like(scale_raw))
    dw = 2.0 * scale * vec                               # rotation vector, |dw|=theta_rel
    return jnp.sum(dw ** 2, axis=-1)                     # theta_rel^2


def _bond_dist_sq_f(q0h: jnp.ndarray) -> jnp.ndarray:
    """Per-bond f = 1 − (Re q̄q')^2 = sin^2(theta_rel/2).

    At small angles ≈ (theta_rel/2)^2 = same scale as raw Euclidean chord.
    Gives eigenvalues {0,8,8,16}×gamma_h matching the spec known answer.
    A 360° turn gives 0.  Spec: must-emerge-list :103; four-team §2.
    """
    return 1.0 - q0h ** 2


# ---------------------------------------------------------------------------
# FLAG 1: T-STAB2' per-bond turn penalty density (JAX)
# ---------------------------------------------------------------------------

def _bond_penalty_density(
    q: jnp.ndarray,
    gamma_h: float,
    short_arc_form: str,
) -> jnp.ndarray:
    """T-STAB2' per-bond turn penalty energy density.

    W_bond(x) = gamma_h * Σ_{p ∈ TETRA_OFFSETS} D(q̄(x) ⊗ q(x+p))
    where D is the short-arc distance squared (log or f form).

    Bond term is OUTSIDE every saturation/clip factor: it must not be
    multiplied by S_eps_sq or S_kappa_sq (k4_quaternion.py:257-258).
    Spec: pcb-grid-fix-decision_2026-10-29.md §A3 (design guard, line ~76);
          four-team-coupling-terms §2.

    c = 4*gamma_h by spec notation (chain-theory-lessons :19);
    c is NOT identified with any existing engine coefficient.

    Normalisation note (see QUESTIONS.md Q1):
      "f"   form → eigenvalues {0,8,8,16}×gamma_h at K=0 (matches spec table).
      "log" form → eigenvalues {0,32,32,64}×gamma_h at K=0 (4× larger).
    """
    q_conj = q * jnp.array([1.0, -1.0, -1.0, -1.0], dtype=q.dtype)
    W_bond = jnp.zeros(q.shape[:-1], dtype=q.dtype)
    for (di, dj, dk) in TETRA_OFFSETS:
        q_nb = jnp.roll(q, shift=(-di, -dj, -dk), axis=(0, 1, 2))
        prod, q0h, v2 = _short_arc_rel_turn(q_conj, q_nb)
        if short_arc_form == "log":
            d_sq = _bond_dist_sq_log(prod, v2)
        else:  # "f"
            d_sq = _bond_dist_sq_f(q0h)
        W_bond = W_bond + d_sq
    return gamma_h * W_bond


# ---------------------------------------------------------------------------
# FLAG 2: op10_b per-bond T-STAB1 in two-star form (JAX)
# ---------------------------------------------------------------------------

def _op10_bond_density_q(q: jnp.ndarray) -> jnp.ndarray:
    """Per-bond op10_b in two-star averaged form ½(+p star + −p star).

    op10_b(x) = (1/16) * Σ_{i<j in TETRA_OFFSETS} |Δn_i × Δn_j|^2
    Two-star: average over (+p) and (−p) neighbor directions.

    The two-star form is exactly invariant under a 90° grid turn (at ~1e-15),
    while the one-star form (+p only, used by _op10_density_q) is not (~3e-4).
    Spec: four-team-coupling-terms §4, appendix; must-emerge-list :105.

    Note: bond differences Δn_p = n(x+p) − n(x) are used without dx
    normalization (spec formula (1/16)Σ|Δn_p×Δn_p'|^2; A8:111).
    The k_op10 coefficient absorbs dimensional factors.
    """
    n_hat = _q_to_n_jax(q)

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

    return 0.5 * (_one_star(n_hat, +1) + _one_star(n_hat, -1))


# ---------------------------------------------------------------------------
# FLAG 3: softplus floor helper (JAX)
# ---------------------------------------------------------------------------

def _softplus_sat(A_sq: jnp.ndarray, w: float) -> jnp.ndarray:
    """Softplus saturation factor S_w(A^2) = w * log(1 + exp((1−A^2)/w)).

    Replaces the hard clip(1−A^2, 0, 1) at k4_quaternion.py:257 or :258.
    Properties:
      S_w(0) ≈ 1 (S_w(0)−1 ≤ 1e-9 at w=0.05; ADDENDUM-2 §3 item 2).
      S_w → 0 smoothly (never exactly 0; removes kink that caused K-R24).
      At small A^2: S_w ≈ 1 − A^2 (same as hard clip to leading order).
    Spec: pcb-grid-fix-decision_2026-10-29.md §A3; must-emerge-list :110.
    """
    return w * jnp.log1p(jnp.exp((1.0 - A_sq) / w))


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

    With any flag ON, recomputes the energy from scratch with modifications:
      FLAG 1 (use_bond_penalty): adds T-STAB2' per-bond penalty OUTSIDE clips.
      FLAG 2 (use_op10_bond): replaces tetra op10 with two-star per-bond op10_b.
      FLAG 3 (use_floor): replaces hard S_eps_sq / S_kappa_sq clip(s) with
                          softplus S_w.

    The bond penalty (FLAG 1) is always outside every saturation factor.
    Spec: pcb-grid-fix-decision_2026-10-29.md §A3 (design guard, line ~76).
    """
    # --- Fast path: all flags OFF → bit-identical to main ---
    if not cfg.use_bond_penalty and not cfg.use_op10_bond and not cfg.use_floor:
        return _energy_density_k4_saturated(
            u, q, mask_alive, dx, G, G_c, gamma,
            omega_yield, epsilon_yield, k_op10, k_refl, k_hopf,
        )

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
        apply_eps = cfg.floor_target in ("eps", "both")
        apply_kap = cfg.floor_target in ("kappa", "both")
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
        W_op10 = _op10_bond_density_q(q)
    else:
        W_op10 = _op10_density_q(q, dx)

    W_hopf = _hopf_density_q(q, dx)

    # --- Bond penalty (T-STAB2') — OUTSIDE saturation factors ---
    if cfg.use_bond_penalty:
        W_bond = _bond_penalty_density(q, cfg.gamma_h, cfg.short_arc_form)
    else:
        W_bond = 0.0

    W = (
        (W_cauchy * G + W_micropolar * G_c) * S_eps_sq
        + W_kappa * gamma * S_kappa_sq
        + W_op10 * k_op10
        + W_refl * k_refl
        + W_hopf * k_hopf
        + W_bond                         # FLAG 1: outside every S factor
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
    # short-arc worst angle: use |min_re| so q→−q sign flip is invisible
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
    Boundary: min_re > 0 iff all bonds < 180° (topology-cut §1 line ~28).
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
    # short-arc worst angle uses |re|
    worst_angle_rad = 2.0 * np.arccos(abs(min_re))
    return float(np.degrees(worst_angle_rad)), min_re


def diag_bad_cell_count(q: np.ndarray, mask_alive: np.ndarray) -> int:
    """Number of alive sites with at least one bad bond.

    A bad bond at site x: Re(q̄(x)⊗q(x+p)) ≤ 0 for any p ∈ TETRA_OFFSETS.
    Equivalently: q(x)·q(x+p) ≤ 0 (dot product of unit quaternions = Re of
    product). Bad bond ↔ relative turn ≥ 180° (half-turn boundary).

    Exact boundary: q_i·q_j ≤ 0 (inclusive).
    Spec: grid-fix-topology-cut_2026-10-28.md §1 line ~28
          "q_i·q_j > 0, i.e. a relative turn under 180°";
          must-emerge-list :52 "q_i·q_j <= 0 per topology-cut §1 line ~28".
    """
    bad = np.zeros(q.shape[:3], dtype=bool)
    q_conj = q * np.array([1.0, -1.0, -1.0, -1.0])
    for (di, dj, dk) in TETRA_OFFSETS:
        q_nb = np.roll(np.roll(np.roll(q, -di, 0), -dj, 1), -dk, 2)
        prod = _quat_mul_np_diag(q_conj, q_nb)
        re = prod[..., 0]          # Re(q̄(x)⊗q(x+p))
        bad = bad | (re <= 0.0)
    return int(np.sum(bad & mask_alive))


def _team_label(shape: tuple) -> np.ndarray:
    """Per-site team label: (x+y+z) mod 4 for shape (nx,ny,nz)."""
    nx, ny, nz = shape
    I, J, K = np.meshgrid(np.arange(nx), np.arange(ny), np.arange(nz),
                           indexing="ij")
    return (I + J + K) % 4


def diag_F_d(u: np.ndarray, mask_alive: np.ndarray) -> float:
    """Team-differential u energy fraction F_d.

    F_d = Σ_x |Π_slide u(x)|^2 / (Σ_x |u(x)|^2 + ε)

    where Π_slide u(x) = c_{team(x)} − c̄ is the per-team mean deviation
    from the global mean (team shift pattern), summed over 3 spatial components.

    HARMLESS criterion (H3): F_d ≤ 1e-3 during evolution.
    Spec: pcb-grid-fix-must-emerge-list_ADDENDUM-1_2026-10-29.md :37.
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
    # Global mean: average over alive teams only (avoids dilution from dead teams)
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


# ---------------------------------------------------------------------------
# JAX JIT wrappers (cfg is static arg; JAX recompiles per cfg)
# ---------------------------------------------------------------------------

# _total_energy_k4_gf positional signature:
#   (u, q, mask_alive, dx, G, G_c, gamma, omega_yield, epsilon_yield,
#    k_op10, k_refl, k_hopf, cfg)
#    0   1     2       3   4   5     6        7              8
#    9     10    11    12
# cfg is positional index 12; marked static so JAX re-specializes per cfg.

_val_and_grad_k4_gf = jax.jit(
    jax.value_and_grad(_total_energy_k4_gf, argnums=(0, 1)),
    static_argnums=(12,),
)

_total_energy_k4_gf_jit = jax.jit(
    _total_energy_k4_gf,
    static_argnums=(12,),
)
