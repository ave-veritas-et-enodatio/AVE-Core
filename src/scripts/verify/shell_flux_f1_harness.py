"""Shell-flux F1 measurement harness.

Implements the force-stop + ball-sum Φ measurement protocol from
PROOF-LADDER-shell-flux-zero-2026-10-06.md (FREEZE, Math ACK 2026-10-06)
and HARNESS-PLAN-shell-flux-F1-2026-10-06.md.

Gap fixes G1–G12 per RULING-shell-flux-F1-run-02fc9794-2026-10-06.md §5.
Fix pass per FIX-BRIEF-PR1064-2026-10-07.md.

USAGE (Gate harness re-check):
    import shell_flux_f1_harness as h

    # Empty-grid sanity (fast)
    result = h.run_empty_grid_sanity()
    assert result["passes_sanity"]

    # Full measurement (Mac run — BLOCKED until gate + orchestrator schedule)
    eng = h.make_engine_64_periodic()
    h.seed_cold_knot(eng, R=6.0, r=2.0)
    run = h.measure_shell_flux(eng, grid_desc="64^3 periodic")
    print(run.verdict, run.notes)

Measurement logic only — does not modify relax_to_ground_state or any engine
default on the main physics path.  Force-stop is a harness-side loop.
"""

from __future__ import annotations

import platform as _platform
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Sequence, Tuple

import jax  # G3: ensure x64 is set before any jnp usage
jax.config.update("jax_enable_x64", True)

import numpy as np

# ── FROZEN constants (Math ACK 2026-10-06) ───────────────────────────────────
F_STOP: float = 1e-8          # force-stop threshold (natural units G=Gc=γ=1)
K_TOL: int = 3                # coherent worst-case multiplier (not tone k=5)
C_TOL: float = 6e3            # float accumulation coefficient
EPS_MACHINE: float = 2.0**-52  # double precision machine epsilon
CONSEC_REQUIRED: int = 3      # consecutive below-F_STOP checks to declare stop

# G7: one frozen MAX_ITER constant for every grid
MAX_ITER: int = 20000

# G6: seed strain fence — refuse to run if peak |eps|/eps_y >= this
SEED_STRAIN_FENCE: float = 0.41  # x = 1/6 in the saturation map

# G8: untie exit requires >=this many consecutive checks below c_init
UNTIE_CONSEC_REQUIRED: int = 3

# G9: vacuum-PASS trap floors (Math may tune)
VACUUM_E_FLOOR_FRAC: float = 0.5
VACUUM_OMEGA_FLOOR_FRAC: float = 0.5

# Default radii for 64³ box (deep inside, R26.102 + r³-fit requirement)
DEFAULT_RADII: Tuple[float, ...] = (12.0, 18.0, 24.0)

# Cold seed amplitude for shell-flux geometry (R=6, r=2, initialize_2_3_torus_knot_sector):
# measured (64³ and 32³, R=6, r=2, initialize_2_3_torus_knot_sector): |eps|/eps_y = 3.6198·A
# → A=0.05 gives 0.181 (peak x=0.0328), inside 0.17–0.29, 2.27× margin to the 0.41 fence.
# The 3.740 map is the R=8,r=3 cold-seed geometry, not this one.
COLD_AMPLITUDE_SCALE: float = 0.05


class Verdict(str, Enum):
    """F1 measurement verdict."""

    INCONCLUSIVE = "INCONCLUSIVE"
    """No force-stop; energy slope >1%/100 at stop; nonzero A + tiny Q; or drained."""
    OUT_OF_SCOPE = "OUT_OF_SCOPE"
    """Pins/drive present — out of scope for in-scope F1 verdict."""
    RECEIPT_ONLY = "RECEIPT_ONLY"
    """G10: code-identity receipt — Φ = Σ(-dE/du) = 0 holds by translation identity.
    Not an independent physical test. TODO: compare against σ·n surface quadrature
    (pending Math B2 — later PR)."""
    MONOPOLE_DETECTED = "MONOPOLE_DETECTED"
    """G1: injected-force positive control — Φ(r) matches closed form −f0(1−n_c/N_c)."""
    NO_MONOPOLE = "NO_MONOPOLE"
    """G1: injected-force control with f0=0 — Φ < tol at all radii (vacuum baseline)."""
    CONTROL_FAIL = "CONTROL_FAIL"
    """G1: injected-force control result does not satisfy all monopole conditions."""
    IDENTITY_VIOLATION = "IDENTITY_VIOLATION"
    """G10: Φ ≥ tol at a force-stopped state — impossible by the F1 identity;
    indicates a code/engine bug. Investigate."""


@dataclass
class BallSumResult:
    """Φ(r) measurement at a single radius."""

    radius: float
    n_ball: int
    phi_vec: np.ndarray  # shape (3,) — sum of -∂E/∂u over alive sites in B(r)
    phi_norm: float      # ‖Φ‖₂
    tol: float           # frozen_tol(n_ball, f_max_measured)
    passes: bool         # phi_norm < tol


@dataclass
class RunResult:
    """Full result for one grid configuration."""

    grid_desc: str
    seed_eps_ratio: float    # measured max |eps|/eps_y at seed time
    stop_reason: str         # "force_stop" | "max_iter" | "lr_underflow" | "untied"
    n_consec: int            # consecutive F_max < F_STOP checks at stop
    f_max: float             # measured F_max = max_alive ‖∂E/∂u‖_∞
    f_rms: float             # ‖∇_u E‖₂ / √N_alive
    energy: float
    energy_slope_pct_100: Optional[float]   # G2: %/100 accepted steps; None = unmeasurable
    crossings: int
    peak_omega: float        # max |ω| over alive sites
    ball_results: list       # list[BallSumResult] ordered by ascending radius
    Q_vec: np.ndarray        # shape (3,) — monopole term from Φ = Q + A r³ fit
    A_vec: np.ndarray        # shape (3,) — volume coefficient
    Q_norm: float            # ‖Q‖₂
    A_norm: float            # ‖A‖₂
    verdict: Verdict
    notes: list = field(default_factory=list)
    # G3: platform/dtype banner
    platform_line: str = ""
    # G4: per-step histories
    energy_history: list = field(default_factory=list)    # accepted steps only (G2)
    f_max_history: list = field(default_factory=list)
    f_rms_history: list = field(default_factory=list)
    crossing_history: list = field(default_factory=list)
    lr_history: list = field(default_factory=list)
    accepted: list = field(default_factory=list)          # bool per step
    # G6: measured strain metrics at seed and stop
    seed_eps_ratio_measured: float = float("nan")
    seed_peak_x: float = float("nan")
    seed_max_a2: float = float("nan")
    stop_eps_ratio_measured: float = float("nan")
    stop_peak_x: float = float("nan")
    stop_max_a2: float = float("nan")
    # G7: frozen MAX_ITER used for this run
    max_iter_used: int = MAX_ITER
    # G12: max |∂E/∂ω| at stop state
    max_dE_domega: float = float("nan")
    # G8: τ and iteration tracking
    tau_at_stop: float = float("nan")
    iter_at_stop: int = -1
    tau_history: list = field(default_factory=list)


# ── Frozen tolerance ──────────────────────────────────────────────────────────

def frozen_tol(n_ball: int, f_max: float) -> float:
    """FROZEN tolerance formula (Math ACK 2026-10-06).

    tol(r) = k * ( N_ball * F_max + C * ε * sqrt(N_ball) )
    k=3, ε=2⁻⁵², C=6×10³.

    Use MEASURED f_max after force-stop — not F_STOP.
    """
    return K_TOL * (n_ball * f_max + C_TOL * EPS_MACHINE * np.sqrt(n_ball))


# ── 4-class alive partition (12 zero modes) ───────────────────────────────────

def alive_classes(engine) -> np.ndarray:
    """Classify alive sites into 4 independently-translatable classes.

    Returns int array shape (nx, ny, nz). Dead sites → -1.
    The cf tetrahedral stencil has 4 such classes (A/B sublattice × FCC parity),
    giving 12 translational zero modes (c7 confirmed: per-class Σ∂E/∂u ≈ 1e-15,
    class-shift dE ≈ 0). Each class has exactly N_alive/4 sites.

      A sites (i,j,k all even): class ((i+j+k)//2) % 2  → 0 or 1
      B sites (i,j,k all odd):  class 2 + ((i+j+k−3)//2) % 2  → 2 or 3
    """
    i, j, k = engine._i, engine._j, engine._k
    al = engine.mask_alive
    classes = np.full(al.shape, -1, dtype=int)
    A = (i % 2 == 0) & al   # mask_A ⊂ alive
    B = (i % 2 == 1) & al   # mask_B ⊂ alive
    classes[A] = ((i + j + k)[A] // 2) % 2
    classes[B] = 2 + ((i + j + k - 3)[B] // 2) % 2
    return classes


def project_class_means(arr: np.ndarray, classes: np.ndarray) -> np.ndarray:
    """Subtract per-class mean from arr (shape …×3) on alive sites. Dead sites → 0.

    Operates in-place on a copy — returns the projected array.
    """
    out = arr.copy()
    for c in range(4):
        mask = classes == c
        if mask.any():
            out[mask] -= out[mask].mean(axis=0)
    return out


# ── Ball-mask helper ──────────────────────────────────────────────────────────

def _ball_mask(
    engine,
    radius: float,
    center: Optional[Tuple[float, float, float]] = None,
) -> np.ndarray:
    """Return bool array (nx, ny, nz): alive sites within radius of center."""
    nx, ny, nz = engine.nx, engine.ny, engine.nz
    if center is None:
        cx, cy, cz = (nx - 1) / 2.0, (ny - 1) / 2.0, (nz - 1) / 2.0
    else:
        cx, cy, cz = center
    x = engine._i - cx
    y = engine._j - cy
    z = engine._k - cz
    r2 = x**2 + y**2 + z**2
    return engine.mask_alive & (r2 <= radius**2)


# ── Ball-sum Φ estimator (primary) ───────────────────────────────────────────

def ball_sum_phi(
    engine,
    radius: float,
    center: Optional[Tuple[float, float, float]] = None,
) -> Tuple[np.ndarray, int]:
    """Primary Φ(r) estimator: Σ_{i ∈ B(r) ∩ alive} (−∂E/∂u_i) as a 3-vector.

    Returns (phi_vec, n_ball).
    """
    dE_du, _ = engine.energy_gradient()
    in_ball = _ball_mask(engine, radius, center)
    phi_vec = np.sum(-np.asarray(dE_du)[in_ball], axis=0)  # (3,)
    n_ball = int(in_ball.sum())
    return phi_vec, n_ball


# ── λ_max estimator for the u-block Hessian ──────────────────────────────────

def estimate_lambda_max_u(
    engine,
    n_iter: int = 30,
    fd_eps: float = 1e-6,
    seed: int = 0,
) -> float:
    """Power-iteration estimate of the largest eigenvalue of the u-block Hessian.

    Uses FD Hessian-vector product (dg/du)*v ≈ (grad(u+ε·v) − grad(u)) / ε
    with ω frozen.  Restores engine.u exactly on return.
    Measured: 3.318 at ω=0, 3.300 at the A=0.05 seed on 32³ (c4, c8).
    """
    rng = np.random.default_rng(seed)
    alive = engine.mask_alive
    u_orig = engine.u.copy()

    v = rng.standard_normal(engine.u.shape).astype(np.float64)
    v[~alive] = 0.0
    norm_v = np.linalg.norm(v)
    if norm_v < 1e-30:
        engine.u = u_orig
        return 1.0
    v /= norm_v

    g0 = np.asarray(engine.energy_gradient()[0]).copy()
    lam = 1.0
    for _ in range(n_iter):
        engine.u = u_orig + fd_eps * v
        g1 = np.asarray(engine.energy_gradient()[0])
        engine.u = u_orig
        Hv = (g1 - g0) / fd_eps
        Hv[~alive] = 0.0
        # Rayleigh quotient
        vv = np.dot(v.ravel(), v.ravel())
        if vv < 1e-60:
            break
        lam = float(np.dot(Hv.ravel(), v.ravel()) / vv)
        norm_Hv = np.linalg.norm(Hv)
        if norm_Hv < 1e-30:
            break
        v = Hv / norm_Hv

    engine.u = u_orig
    return abs(lam)


# ── u-only solver (B0) ────────────────────────────────────────────────────────

def relax_u_only(
    engine,
    external_force=None,   # None or ((ci, cj, ck), f0_vec)
    f_stop: float = F_STOP,
    max_iter: int = MAX_ITER,
    consec_required: int = 3,
) -> dict:
    """Fixed-lr u-only gradient descent with per-class projection.

    lr = 1/λ_max (GD stable for lr < 2/λ_max; measured λ_max ≈ 3.3).
    external_force: inject −f0 at site (ci,cj,ck) before projection.
    Safeguard: lr halved when F > 2×F_min for 3 consecutive iterations.
    Returns: stop_reason, n_consec, f_max, f_max_history, lr, lambda_max,
             lr_halvings, n_iter, tau.
    """
    classes = alive_classes(engine)
    alive = engine.mask_alive
    lam = estimate_lambda_max_u(engine)
    lr = 1.0 / lam

    f_max_history: list = []
    f_max = float("inf")
    n_consec = 0
    stop_reason = "max_iter"
    F_min = float("inf")
    consec_diverge = 0
    lr_halvings = 0
    tau = 0.0
    n_iter = 0

    for step in range(max_iter):
        n_iter = step + 1
        dE_du = np.asarray(engine.energy_gradient()[0])
        g = dE_du.copy()
        if external_force is not None:
            (ci, cj, ck), f0_vec = external_force
            g[ci, cj, ck] -= np.asarray(f0_vec, dtype=float)
        gp = project_class_means(g, classes)
        f_max = float(np.max(np.abs(gp[alive]))) if alive.any() else 0.0
        f_max_history.append(f_max)

        if f_max < f_stop:
            n_consec += 1
            if n_consec >= consec_required:
                stop_reason = "force_stop"
                break
        else:
            n_consec = 0

        # Safeguard: halve lr if F > 2×F_min for 3 consecutive steps
        if f_max > 2.0 * F_min and F_min < float("inf"):
            consec_diverge += 1
            if consec_diverge >= 3:
                lr *= 0.5
                lr_halvings += 1
                consec_diverge = 0
        else:
            consec_diverge = 0
        F_min = min(F_min, f_max)

        engine.u = engine.u - lr * gp
        engine.u = project_class_means(np.asarray(engine.u), classes)
        engine._zero_outside_alive()
        tau += lr

    return {
        "stop_reason": stop_reason,
        "n_consec": n_consec,
        "f_max": f_max,
        "f_max_history": f_max_history,
        "lr": lr,
        "lambda_max": lam,
        "lr_halvings": lr_halvings,
        "n_iter": n_iter,
        "tau": tau,
    }


# ── Q/A fit ──────────────────────────────────────────────────────────────────

def fit_qa(
    radii: Sequence[float],
    phi_vecs: Sequence[np.ndarray],
) -> Tuple[np.ndarray, np.ndarray]:
    """Fit Φ_c(r) = Q_c + A_c · r³ per component via least squares.

    Returns Q_vec (3,), A_vec (3,) — always report both per FREEZE.
    """
    r3 = np.asarray(radii, dtype=float) ** 3
    A_mat = np.column_stack([np.ones_like(r3), r3])
    Q_vec = np.zeros(3)
    A_vec = np.zeros(3)
    for c in range(3):
        phi_c = np.array([v[c] for v in phi_vecs], dtype=float)
        coeffs, _, _, _ = np.linalg.lstsq(A_mat, phi_c, rcond=None)
        Q_vec[c] = coeffs[0]
        A_vec[c] = coeffs[1]
    return Q_vec, A_vec


# ── Energy slope ─────────────────────────────────────────────────────────────

def _energy_slope_pct(history: list, window: int = 100) -> Optional[float]:
    """% drop in energy over the last `window` ACCEPTED steps.

    G2: returns None when history is too short or |E_start| is below the floor.
    Positive means energy decreased (dropped); negative means it increased.
    """
    if len(history) < window + 1:
        return None
    E_end = history[-1]
    E_start = history[-(window + 1)]
    denom = abs(E_start)
    if denom < 1e-12:
        return None
    return 100.0 * (E_start - E_end) / denom


# ── Strain metrics (G6) ───────────────────────────────────────────────────────

def _measure_strain_metrics(engine) -> Tuple[float, float, float]:
    """Return (max_eps_ratio, peak_x, max_a2) over alive sites.

    max_eps_ratio = max_alive(‖eps‖_F / eps_y)
    peak_x        = max_eps_ratio²  (saturation variable x = |eps|²/eps_y²)
    max_a2        = max_alive(|eps|²/eps_y² + |kappa|²/omega_yield²)

    Used for the G6 seed fence check and stop-state logging.
    """
    import jax.numpy as jnp
    from ave.topological.cosserat_field_3d import (
        _compute_curvature,
        _compute_strain,
    )

    u_j = jnp.asarray(engine.u)
    w_j = jnp.asarray(engine.omega)
    eps = np.asarray(_compute_strain(u_j, w_j, engine.dx))
    kappa = np.asarray(_compute_curvature(w_j, engine.dx))

    eps_sq = np.sum(eps**2, axis=(-2, -1))      # (nx, ny, nz) Frobenius²
    kappa_sq = np.sum(kappa**2, axis=(-2, -1))

    alive = engine.mask_alive
    if not alive.any():
        return 0.0, 0.0, 0.0

    eps_y = engine.epsilon_yield
    omega_y = engine.omega_yield

    eps_ratio = np.sqrt(eps_sq[alive]) / eps_y
    max_eps_ratio = float(np.max(eps_ratio))
    peak_x = max_eps_ratio**2

    a2_field = eps_sq / (eps_y**2) + kappa_sq / (omega_y**2)
    max_a2 = float(np.max(a2_field[alive]))

    return max_eps_ratio, peak_x, max_a2


# ── Platform banner (G3) ─────────────────────────────────────────────────────

def _build_platform_line(engine) -> str:
    """Build platform banner following envd_knot_run.py:143-150."""
    u_dtype = np.asarray(engine.u).dtype
    omega_dtype = np.asarray(engine.omega).dtype
    return (
        f"platform={_platform.platform()}"
        f"  backend={jax.default_backend()}"
        f"  jax={jax.__version__}"
        f"  x64={jax.config.jax_enable_x64}"
        f"  u_dtype={u_dtype}"
        f"  omega_dtype={omega_dtype}"
    )


# ── Verdict logic ─────────────────────────────────────────────────────────────

def compute_verdict(
    stop_info: dict,
    ball_results: list,
    Q_norm: float,
    A_norm: float,
    radii: Sequence[float],
    has_pins: bool = False,
) -> Tuple[Verdict, list]:
    """Apply FROZEN kill/pass/inconclusive table (G10: retired PASS_F1/KILL_F1).

    Order:
      1. pins → OUT_OF_SCOPE
      2. E_seed ≤ 1e-12 → INCONCLUSIVE "no knot seeded (vacuum box)"
      3. no force-stop → INCONCLUSIVE
      4. slope None or >1% → INCONCLUSIVE
      5. G9 drained state → INCONCLUSIVE
      6. all Φ(r) < tol(r) → RECEIPT_ONLY
      7. otherwise → IDENTITY_VIOLATION (Φ≥tol is impossible at u-equilibrium)

    Returns (verdict, notes).
    """
    notes: list = []

    if has_pins:
        return Verdict.OUT_OF_SCOPE, ["pins/drive present — out of scope"]

    # G9: vacuum-box check must precede force-stop / slope gates: on real runs with
    # amplitude_scale=0 the accepted-step history is too short and the slope gate fires
    # first, emitting the wrong label; placing this check here ensures "vacuum box" wins.
    E_seed = stop_info.get("E_seed")
    if E_seed is not None and E_seed <= 1e-12:
        notes.append("INCONCLUSIVE: no knot seeded (vacuum box)")
        return Verdict.INCONCLUSIVE, notes

    stop_reason = stop_info["stop_reason"]
    n_consec = stop_info["n_consec"]
    f_max = stop_info["f_max"]
    E_hist = stop_info.get("energy_history", [])
    energy_slope = _energy_slope_pct(E_hist)  # G2: Optional[float]

    if stop_reason != "force_stop" or n_consec < CONSEC_REQUIRED:
        if stop_reason == "untied":
            iter_s = stop_info.get("iter_at_stop", -1)
            tau_s = stop_info.get("tau_at_stop", float("nan"))
            notes.append(
                f"INCONCLUSIVE: untied at iter={iter_s}, tau={tau_s:.4f} "
                f"(n_consec={n_consec})"
            )
        else:
            notes.append(
                f"INCONCLUSIVE: no force-stop (stop_reason={stop_reason!r}, "
                f"n_consec={n_consec} < {CONSEC_REQUIRED})"
            )
        return Verdict.INCONCLUSIVE, notes

    # G2: None slope → INCONCLUSIVE
    if energy_slope is None:
        notes.append(
            "INCONCLUSIVE: energy slope unmeasurable "
            "(accepted-step history too short or |E_start| below 1e-12 floor)"
        )
        return Verdict.INCONCLUSIVE, notes

    if energy_slope > 1.0:
        notes.append(
            f"INCONCLUSIVE: energy still dropping {energy_slope:.2f}%/100 steps at stop "
            f"(>1% threshold)"
        )
        return Verdict.INCONCLUSIVE, notes

    # G9: drained-to-vacuum trap (E_seed > 1e-12 guaranteed here)
    peak_omega_seed = stop_info.get("peak_omega_seed")
    if E_seed is not None:
        energy_stop = stop_info.get("energy", 0.0)
        peak_omega_stop = stop_info.get("peak_omega", 0.0)
        e_drained = energy_stop < VACUUM_E_FLOOR_FRAC * E_seed
        o_drained = (peak_omega_seed is not None and peak_omega_seed > 0) and (
            peak_omega_stop < VACUUM_OMEGA_FLOOR_FRAC * peak_omega_seed
        )
        if e_drained or o_drained:
            notes.append(
                f"INCONCLUSIVE: drained to vacuum "
                f"(E_stop={energy_stop:.3e} vs {VACUUM_E_FLOOR_FRAC}*E_seed={VACUUM_E_FLOOR_FRAC*E_seed:.3e}; "
                f"peak_omega_stop={peak_omega_stop:.3e} vs "
                f"{VACUUM_OMEGA_FLOOR_FRAC}*peak_seed={VACUUM_OMEGA_FLOOR_FRAC*(peak_omega_seed or 0.0):.3e})"
            )
            return Verdict.INCONCLUSIVE, notes

    all_phi_pass = all(br.passes for br in ball_results)

    if all_phi_pass:
        notes.append(
            "RECEIPT_ONLY: code-identity Φ = Σ(-dE/du) = 0 holds at all radii "
            "(per-class translation identity, 4 classes; not an independent physical test). "
            "TODO: compare against σ·n surface quadrature — pending Math B2 (later PR)."
        )
        return Verdict.RECEIPT_ONLY, notes

    notes.append(
        "IDENTITY_VIOLATION: Φ ≥ tol at a force-stopped state is impossible by "
        "the F1 identity: code/engine bug, investigate"
    )
    return Verdict.IDENTITY_VIOLATION, notes


# ── Control verdict (pure function, G1) ──────────────────────────────────────

def control_verdict(
    stop_reason: str,
    phis: Sequence[np.ndarray],
    phi_exps: Sequence[np.ndarray],
    tols: Sequence[float],
    f0: np.ndarray,
) -> Tuple[Verdict, list]:
    """Pure verdict function for the injected-force control (G1).

    stop_reason != "force_stop" → INCONCLUSIVE.
    ‖f0‖ == 0:  all ‖phi‖ < tol → NO_MONOPOLE; else CONTROL_FAIL.
    ‖f0‖ > 0:  MONOPOLE_DETECTED iff:
      (a) resid(r) < tol(r) for every r;
      (b) ‖phi_exp(r_min)‖ > 10·tol(r_min)  (monopole is visible);
      (c) dot(phi(r_min), f0) < 0  (sign is −f0).
    Otherwise CONTROL_FAIL with note naming the failed condition.
    """
    notes: list = []
    f0 = np.asarray(f0, dtype=float)
    f0_norm = float(np.linalg.norm(f0))

    if stop_reason != "force_stop":
        notes.append(f"INCONCLUSIVE: no force-stop (stop_reason={stop_reason!r})")
        return Verdict.INCONCLUSIVE, notes

    if f0_norm == 0.0:
        if all(float(np.linalg.norm(p)) < t for p, t in zip(phis, tols)):
            notes.append("NO_MONOPOLE: f0=0 and all |phi| < tol (vacuum baseline)")
            return Verdict.NO_MONOPOLE, notes
        notes.append("CONTROL_FAIL: f0=0 but some |phi| >= tol")
        return Verdict.CONTROL_FAIL, notes

    # f0 ≠ 0: check monopole conditions
    resids = [float(np.linalg.norm(np.asarray(p) - np.asarray(e)))
              for p, e in zip(phis, phi_exps)]
    tols_list = list(tols)
    phi_exp_0 = np.asarray(phi_exps[0])
    phi_0 = np.asarray(phis[0])
    tol_0 = float(tols_list[0])

    cond_a = all(r < t for r, t in zip(resids, tols_list))
    cond_b = float(np.linalg.norm(phi_exp_0)) > 10.0 * tol_0
    cond_c = float(np.dot(phi_0, f0)) < 0.0

    if cond_a and cond_b and cond_c:
        notes.append(
            f"MONOPOLE_DETECTED: resid<tol all r, "
            f"|phi_exp(r_min)|={np.linalg.norm(phi_exp_0):.3e} > 10*tol={10*tol_0:.3e}, "
            f"dot(phi,f0)={np.dot(phi_0,f0):.3e} < 0"
        )
        return Verdict.MONOPOLE_DETECTED, notes

    if not cond_a:
        bad = [(r, t) for r, t in zip(resids, tols_list) if r >= t]
        notes.append(f"CONTROL_FAIL: (a) resid >= tol at {len(bad)} radius(es): {bad[:3]}")
    if not cond_b:
        notes.append(
            f"CONTROL_FAIL: (b) monopole not visible: "
            f"|phi_exp(r_min)|={np.linalg.norm(phi_exp_0):.3e} <= 10*tol={10*tol_0:.3e}"
        )
    if not cond_c:
        notes.append(
            f"CONTROL_FAIL: (c) wrong sign: dot(phi(r_min),f0)={np.dot(phi_0,f0):.3e} >= 0"
        )
    return Verdict.CONTROL_FAIL, notes


# ── Force-stop relaxation loop ────────────────────────────────────────────────

def force_stop_relax(
    engine,
    max_iter: int = MAX_ITER,   # G7: frozen constant
    f_stop: float = F_STOP,
    consec_required: int = CONSEC_REQUIRED,
    lr_init: float = 0.01,
    verbose: bool = False,
    u_only: bool = False,       # G11: delegate to relax_u_only
) -> dict:
    """Force-stop relaxation gate for the F1 harness.

    External gradient-descent loop — does NOT modify engine defaults or
    relax_to_ground_state on the main physics path.

    G2: E_history accumulates only on ACCEPTED steps.
    G4: returns energy = total_energy() at the final state.
    G7: max_iter defaults to frozen MAX_ITER.
    G8: untie exit requires >=UNTIE_CONSEC_REQUIRED consecutive checks below c_init;
        logs τ and iter at every crossing check; returns tau_history, tau_at_stop,
        iter_at_stop.
    G11: u_only=True delegates entirely to relax_u_only (stable lr=1/λ_max, no
         energy line search).
    G12: returns max_dE_domega at stop state.
    """
    # G11: delegate u-only path
    if u_only:
        ru = relax_u_only(engine, f_stop=f_stop, max_iter=max_iter,
                          consec_required=consec_required)
        # Compute derived quantities from final engine state
        alive = engine.mask_alive
        dE_du_stop, dE_dw_stop = engine.energy_gradient()
        dE_du_np = np.asarray(dE_du_stop)
        dE_dw_np = np.asarray(dE_dw_stop)
        du_alive = dE_du_np[alive]
        dw_alive = dE_dw_np[alive]
        f_rms = float(np.sqrt(np.sum(du_alive**2) / len(du_alive))) if len(du_alive) else 0.0
        omega_mag = np.sqrt(np.sum(np.asarray(engine.omega)**2, axis=-1))
        peak_omega = float(np.max(omega_mag[alive])) if alive.any() else 0.0
        try:
            crossings = int(engine.extract_crossing_count())
        except Exception:
            crossings = -1
        max_dE_domega = float(np.max(np.abs(dw_alive))) if len(dw_alive) else 0.0
        energy = float(engine.total_energy())
        return {
            "stop_reason": ru["stop_reason"],
            "n_consec": ru["n_consec"],
            "f_max": ru["f_max"],
            "f_rms": f_rms,
            "energy": energy,
            "energy_history": [],
            "f_max_history": ru["f_max_history"],
            "f_rms_history": [],
            "crossing_history": [],
            "lr_history": [],
            "accepted": [],
            "crossings": crossings,
            "peak_omega": peak_omega,
            "tau": ru["tau"],
            "tau_at_stop": ru["tau"],
            "iter_at_stop": ru["n_iter"],
            "tau_history": [],
            "check_iter_history": [],
            "max_dE_domega": max_dE_domega,
            "lr": ru["lr"],
            "lambda_max": ru["lambda_max"],
            "lr_halvings": ru["lr_halvings"],
        }

    # Full (u, ω) path
    lr = float(lr_init)
    E_history: list = []        # G2: accepted steps only
    f_max_history: list = []    # G4
    f_rms_history: list = []    # G4
    crossing_history: list = [] # G4/G8
    lr_history: list = []       # G4
    accepted_flags: list = []   # G4
    tau_history: list = []      # G8
    check_iter_history: list = []  # G8

    n_consec = 0
    f_max_last = float("inf")
    f_rms_last = 0.0
    stop_reason = "max_iter"
    c_init = -1
    c_untie_consec = 0          # G8: consecutive below-c_init checks
    tau = 0.0                   # G8: accumulated gradient-flow time Σlr
    tau_at_stop = float("nan")
    iter_at_stop = -1

    for step in range(max_iter):
        dE_du, dE_dw = engine.energy_gradient()
        E = float(engine.total_energy())

        alive = engine.mask_alive
        du_alive = np.asarray(dE_du)[alive]
        n_alive = int(alive.sum())

        if n_alive > 0:
            f_max_last = float(np.max(np.abs(du_alive)))
            f_rms_last = float(np.sqrt(np.sum(du_alive**2) / n_alive))
        else:
            f_max_last = 0.0
            f_rms_last = 0.0

        # G4: record per-step metrics
        f_max_history.append(f_max_last)
        f_rms_history.append(f_rms_last)
        lr_history.append(lr)

        # Force-stop criterion
        if f_max_last < f_stop:
            n_consec += 1
            if n_consec >= consec_required:
                stop_reason = "force_stop"
                # G8: record tau/iter at stop before break
                tau_at_stop = tau
                iter_at_stop = step
                break
        else:
            n_consec = 0

        # G8: untie check — log at EVERY check, not just when c < c_init
        try:
            c = int(engine.extract_crossing_count())
        except Exception:
            c = -1
        crossing_history.append(c)
        tau_history.append(tau)
        check_iter_history.append(step)
        if step == 0:
            c_init = c
        elif c >= 0 and c_init >= 0:
            if c < c_init:
                c_untie_consec += 1
            else:
                c_untie_consec = 0
            if verbose:
                print(
                    f"  [untie-check] iter={step} tau={tau:.4f} "
                    f"crossings={c} init={c_init} consec={c_untie_consec}"
                )
            if c_untie_consec >= UNTIE_CONSEC_REQUIRED:
                stop_reason = "untied"
                tau_at_stop = tau
                iter_at_stop = step
                break

        # Gradient descent step
        noise_floor = 1e-12 * max(abs(E), 1.0)
        u_save = engine.u.copy()
        w_save = engine.omega.copy()
        engine.u = np.asarray(engine.u) - lr * np.asarray(dE_du)
        engine.omega = np.asarray(engine.omega) - lr * np.asarray(dE_dw)
        engine._zero_outside_alive()
        E_new = float(engine.total_energy())

        if E_new > E + noise_floor:
            engine.u = u_save
            engine.omega = w_save
            lr *= 0.5
            accepted_flags.append(False)
            if lr < 1e-14:
                stop_reason = "lr_underflow"
                tau_at_stop = tau
                iter_at_stop = step
                break
        else:
            accepted_flags.append(True)
            E_history.append(E)   # G2: accepted only
            tau += lr
            lr = min(lr * 1.1, 1.0)

        if verbose and step % 500 == 0:
            print(
                f"  step {step:6d}  E={E:.6e}  F_max={f_max_last:.3e}  "
                f"consec={n_consec}  lr={lr:.2e}  tau={tau:.4f}"
            )

    # G4: energy = total_energy() at the final state (not E_history[-1])
    energy_final = float(engine.total_energy())

    # State at stop: compute derived quantities
    omega_mag = np.sqrt(np.sum(np.asarray(engine.omega)**2, axis=-1))
    peak_omega = (
        float(np.max(omega_mag[engine.mask_alive]))
        if engine.mask_alive.any()
        else 0.0
    )

    try:
        crossings = int(engine.extract_crossing_count())
    except Exception:
        crossings = -1

    # G12: max |dE/dω| at stop state
    dE_du_stop, dE_dw_stop = engine.energy_gradient()
    dw_alive = np.asarray(dE_dw_stop)[engine.mask_alive]
    max_dE_domega = float(np.max(np.abs(dw_alive))) if len(dw_alive) > 0 else 0.0

    # If we stopped by force_stop or max_iter without going through the untie break
    if tau_at_stop != tau_at_stop:  # nan
        tau_at_stop = tau
        iter_at_stop = max_iter - 1 if stop_reason == "max_iter" else (
            len(f_max_history) - 1
        )

    return {
        "stop_reason": stop_reason,
        "n_consec": n_consec,
        "f_max": f_max_last,
        "f_rms": f_rms_last,
        "energy": energy_final,
        "energy_history": E_history,
        "f_max_history": f_max_history,
        "f_rms_history": f_rms_history,
        "crossing_history": crossing_history,
        "lr_history": lr_history,
        "accepted": accepted_flags,
        "crossings": crossings,
        "peak_omega": peak_omega,
        "tau": tau,
        "tau_at_stop": tau_at_stop,
        "iter_at_stop": iter_at_stop,
        "tau_history": tau_history,
        "check_iter_history": check_iter_history,
        "max_dE_domega": max_dE_domega,
    }


# ── Full measurement pipeline ─────────────────────────────────────────────────

def measure_shell_flux(
    engine,
    radii: Sequence[float] = DEFAULT_RADII,
    grid_desc: str = "64³ periodic",
    max_iter: int = MAX_ITER,   # G7
    verbose: bool = False,
    has_pins: bool = False,
) -> RunResult:
    """Run force-stop + ball-sum Φ measurement pipeline for F1.

    Engine must already have the (2,3)-torus-knot seeded (call seed_cold_knot
    before this).

    G3: builds platform_line after engine construction.
    G6: measures and checks seed strain fence; refuses if peak |eps|/eps_y >= 0.41.
    G9: captures E_seed and peak_omega_seed for vacuum-PASS trap.
    G10: compute_verdict always returns RECEIPT_ONLY or IDENTITY_VIOLATION for
         force-stopped states (PASS_F1/KILL_F1 retired).

    Returns RunResult with verdict and full log.
    """
    # G3: platform banner (built after engine is constructed)
    plat_line = _build_platform_line(engine)

    # G6: measure seed strain and enforce fence
    seed_eps_ratio, seed_peak_x, seed_max_a2 = _measure_strain_metrics(engine)
    if seed_eps_ratio >= SEED_STRAIN_FENCE:
        raise ValueError(
            f"Seed strain fence violated: peak |eps|/eps_y = {seed_eps_ratio:.4f} "
            f">= {SEED_STRAIN_FENCE}. Use a colder seed "
            f"(A=0.05 → ~0.181, A=0.03 → ~0.109). Refusing to run."
        )

    # G9: capture seed values for vacuum-PASS trap
    E_seed = float(engine.total_energy())
    omega_mag_seed = np.sqrt(np.sum(np.asarray(engine.omega)**2, axis=-1))
    peak_omega_seed = (
        float(np.max(omega_mag_seed[engine.mask_alive]))
        if engine.mask_alive.any()
        else 0.0
    )

    stop_info = force_stop_relax(engine, max_iter=max_iter, verbose=verbose)

    # G9: inject seed values for vacuum-PASS trap in compute_verdict
    stop_info["E_seed"] = E_seed
    stop_info["peak_omega_seed"] = peak_omega_seed

    f_max = stop_info["f_max"]
    E_hist = stop_info["energy_history"]
    energy_slope = _energy_slope_pct(E_hist)

    phi_vecs: list = []
    ball_results: list = []
    for r in radii:
        phi_vec, n_ball = ball_sum_phi(engine, float(r))
        phi_norm = float(np.linalg.norm(phi_vec))
        tol = frozen_tol(n_ball, f_max)
        passes = phi_norm < tol
        ball_results.append(BallSumResult(
            radius=float(r),
            n_ball=n_ball,
            phi_vec=phi_vec,
            phi_norm=phi_norm,
            tol=tol,
            passes=passes,
        ))
        phi_vecs.append(phi_vec)

    Q_vec, A_vec = fit_qa(radii, phi_vecs)
    Q_norm = float(np.linalg.norm(Q_vec))
    A_norm = float(np.linalg.norm(A_vec))

    verdict, notes = compute_verdict(
        stop_info, ball_results, Q_norm, A_norm, radii,
        has_pins=has_pins,
    )

    # G6: measure stop strain
    stop_eps_ratio, stop_peak_x, stop_max_a2 = _measure_strain_metrics(engine)

    return RunResult(
        grid_desc=grid_desc,
        seed_eps_ratio=seed_eps_ratio,  # measured (from _measure_strain_metrics)
        stop_reason=stop_info["stop_reason"],
        n_consec=stop_info["n_consec"],
        f_max=f_max,
        f_rms=stop_info["f_rms"],
        energy=stop_info["energy"],
        energy_slope_pct_100=energy_slope,
        crossings=stop_info["crossings"],
        peak_omega=stop_info["peak_omega"],
        ball_results=ball_results,
        Q_vec=Q_vec,
        A_vec=A_vec,
        Q_norm=Q_norm,
        A_norm=A_norm,
        verdict=verdict,
        notes=notes,
        platform_line=plat_line,
        energy_history=stop_info["energy_history"],
        f_max_history=stop_info["f_max_history"],
        f_rms_history=stop_info["f_rms_history"],
        crossing_history=stop_info["crossing_history"],
        lr_history=stop_info["lr_history"],
        accepted=stop_info["accepted"],
        seed_eps_ratio_measured=seed_eps_ratio,
        seed_peak_x=seed_peak_x,
        seed_max_a2=seed_max_a2,
        stop_eps_ratio_measured=stop_eps_ratio,
        stop_peak_x=stop_peak_x,
        stop_max_a2=stop_max_a2,
        max_iter_used=max_iter,
        max_dE_domega=stop_info["max_dE_domega"],
        tau_at_stop=stop_info.get("tau_at_stop", float("nan")),
        iter_at_stop=stop_info.get("iter_at_stop", -1),
        tau_history=stop_info.get("tau_history", []),
    )


# ── Engine factories ──────────────────────────────────────────────────────────

def make_engine_64_periodic(use_saturation: bool = True):
    """Default 64³ periodic box (FROZEN: even edges, dx=1, G=Gc=γ=1, ε_y=1)."""
    from ave.topological.cosserat_field_3d import CosseratField3D
    return CosseratField3D(64, 64, 64, use_saturation=use_saturation)


def make_engine_32_periodic(use_saturation: bool = True):
    """32³ periodic box — fast convergence for unit tests (κ ≈ 104 vs 414 for 64³).

    Use in G1 injected-force control tests: ~327 steps to converge vs ~1300 on 64³.
    NOT for production measurements (too small for DEFAULT_RADII = {12, 18, 24}).
    """
    from ave.topological.cosserat_field_3d import CosseratField3D
    return CosseratField3D(32, 32, 32, use_saturation=use_saturation)


def make_engine_96_periodic(use_saturation: bool = True):
    """96³ large-pad periodic control (wrap-artifact discriminator)."""
    from ave.topological.cosserat_field_3d import CosseratField3D
    return CosseratField3D(96, 96, 96, use_saturation=use_saturation)


def make_engine_128_periodic(use_saturation: bool = True):
    """128³ large-pad periodic control (second wrap-artifact size)."""
    from ave.topological.cosserat_field_3d import CosseratField3D
    return CosseratField3D(128, 128, 128, use_saturation=use_saturation)


# ── Seed helper ───────────────────────────────────────────────────────────────

def seed_cold_knot(
    engine,
    R: float = 6.0,
    r: float = 2.0,
    amplitude_scale: float = COLD_AMPLITUDE_SCALE,
) -> None:
    """Seed a cold (2,3)-torus-knot on engine per R26.196a fence.

    amplitude_scale=0.05 → peak |eps|/eps_y ≈ 0.181 (measured, 32³ and 64³,
    R=6, r=2, initialize_2_3_torus_knot_sector); inside 0.17–0.29 band.
    Hot ENV-D seeds are out of scope (may have no force-stationary point).
    """
    engine.initialize_2_3_torus_knot_sector(
        R_target=R, r_target=r, amplitude_scale=amplitude_scale
    )


# ── Empty-grid sanity + identity sanity (G5) ─────────────────────────────────

def run_empty_grid_sanity(radii: Sequence[float] = DEFAULT_RADII) -> dict:
    """G5: Empty-grid sanity using the same factory as the knot runs.

    Uses 64³ periodic, use_saturation=True (matching make_engine_64_periodic
    defaults) at the FROZEN DEFAULT_RADII = {12, 18, 24}.

    Returns dict with keys: per_radius (list of {r, n_ball, phi_norm, float_tol,
    passes}), passes_sanity (bool).
    """
    engine = make_engine_64_periodic(use_saturation=True)
    per_radius = []
    for r in radii:
        phi_vec, n_ball = ball_sum_phi(engine, float(r))
        phi_norm = float(np.linalg.norm(phi_vec))
        float_tol = K_TOL * C_TOL * EPS_MACHINE * np.sqrt(n_ball)
        passes = phi_norm < float_tol
        per_radius.append({
            "r": float(r),
            "n_ball": n_ball,
            "phi_norm": phi_norm,
            "float_tol": float_tol,
            "passes": passes,
        })
    return {
        "per_radius": per_radius,
        "passes_sanity": all(d["passes"] for d in per_radius),
    }


def run_identity_sanity(seed: int = 0) -> dict:
    """G5: Identity sanity — random (u, ω) gives global sum of dE/du = 0.

    Translation invariance on a periodic grid: Σ_alive(∂E/∂u_i) = 0 to ≤1e-12.
    Zero field → zero is trivial; this tests a non-trivial random state.
    Ruling §3 measured 1e-15 at the seed and 2e-17 at the untie state (r4).
    Per-class sums ≤1e-15 (4 classes, 12 zero modes — confirmed c7).
    """
    rng = np.random.default_rng(seed)
    engine = make_engine_64_periodic(use_saturation=True)
    u_rand = rng.standard_normal(engine.u.shape).astype(np.float64) * 0.01
    w_rand = rng.standard_normal(engine.omega.shape).astype(np.float64) * 0.01
    engine.u = u_rand * engine.mask_alive[..., None]
    engine.omega = w_rand * engine.mask_alive[..., None]

    dE_du, _ = engine.energy_gradient()
    global_sum = np.sum(np.asarray(dE_du)[engine.mask_alive], axis=0)  # (3,)
    global_norm = float(np.linalg.norm(global_sum))
    passes = global_norm <= 1e-12
    return {
        "global_sum": global_sum,
        "global_norm": global_norm,
        "passes": passes,
    }


# ── Injected-force positive control (G1) ─────────────────────────────────────

def run_injected_force_control(
    engine,
    f0: Tuple[float, float, float] = (0.0, 0.0, 1e-2),
    radii: Sequence[float] = DEFAULT_RADII,
    max_iter: int = MAX_ITER,
    verbose: bool = False,
) -> dict:
    """G1: Injected-force positive control — uses per-class projection for exact convergence.

    The K4 cf stencil has 4 translation-zero-mode classes (12 zero modes total).
    With per-class projection and lr = 1/λ_max, the control reaches F < 1e-8 in
    ~327 steps on 32³ (9 s) and Φ(r) = −f0·(1 − n_c(r)/N_c) exactly (c7).

    f0=(0,0,0): clean field → NO_MONOPOLE.
    f0≠0: expects MONOPOLE_DETECTED when sign, magnitude, and closed-form match.
    """
    f0_vec = np.asarray(f0, dtype=float)

    # Find alive site closest to box center
    cx = (engine.nx - 1) / 2.0
    cy = (engine.ny - 1) / 2.0
    cz = (engine.nz - 1) / 2.0

    i_flat = engine._i.ravel()
    j_flat = engine._j.ravel()
    k_flat = engine._k.ravel()
    alive_flat = engine.mask_alive.ravel()

    r2 = (i_flat - cx)**2 + (j_flat - cy)**2 + (k_flat - cz)**2
    r2_masked = np.where(alive_flat, r2, np.inf)
    center_flat_idx = int(np.argmin(r2_masked))
    ci = int(i_flat[center_flat_idx])
    cj = int(j_flat[center_flat_idx])
    ck = int(k_flat[center_flat_idx])

    # Reset state: u=0, omega=0
    engine.u = np.zeros_like(engine.u)
    engine.omega = np.zeros_like(engine.omega)

    classes = alive_classes(engine)
    alive = engine.mask_alive
    c_inj = int(classes[ci, cj, ck])
    N_c = int((classes == c_inj).sum())

    # Relax u-only with injected force at center
    ru = relax_u_only(
        engine,
        external_force=((ci, cj, ck), f0_vec),
        f_stop=F_STOP,
        max_iter=max_iter,
        consec_required=CONSEC_REQUIRED,
    )
    f_max_final = ru["f_max"]
    stop_reason = ru["stop_reason"]
    n_consec = ru["n_consec"]

    if verbose:
        print(
            f"  control: stop_reason={stop_reason!r}, "
            f"F_max={f_max_final:.3e}, steps={ru['n_iter']}, "
            f"lr_halvings={ru['lr_halvings']}"
        )

    # Ball-sum INTERNAL -dE/du (unmodified by injection)
    phi_vecs: list = []
    ball_results: list = []
    phi_exps: list = []
    tols: list = []
    n_cs: list = []
    resids: list = []

    for r in radii:
        phi_vec, n_ball = ball_sum_phi(engine, float(r))
        phi_norm_r = float(np.linalg.norm(phi_vec))
        tol = frozen_tol(n_ball, f_max_final)

        # Closed-form expected: phi_exp(r) = -f0 * (1 - n_c(r)/N_c)
        ball_in = _ball_mask(engine, float(r))
        n_c_r = int((ball_in & (classes == c_inj)).sum())
        phi_exp_r = -f0_vec * (1.0 - n_c_r / N_c)

        resid = float(np.linalg.norm(phi_vec - phi_exp_r))
        resids.append(resid)
        ball_results.append(BallSumResult(
            radius=float(r),
            n_ball=n_ball,
            phi_vec=phi_vec,
            phi_norm=phi_norm_r,
            tol=tol,
            passes=(phi_norm_r < tol),
        ))
        phi_vecs.append(phi_vec)
        phi_exps.append(phi_exp_r)
        tols.append(tol)
        n_cs.append(n_c_r)

    Q_vec, A_vec = fit_qa(radii, phi_vecs)
    Q_norm = float(np.linalg.norm(Q_vec))
    A_norm = float(np.linalg.norm(A_vec))
    r_max = float(max(radii))

    verdict, verdict_notes = control_verdict(
        stop_reason, phi_vecs, phi_exps, tols, f0_vec
    )

    notes = [
        f"injected f0={tuple(f0)}, f0_norm={float(np.linalg.norm(f0_vec)):.3e}",
        f"stop_reason={stop_reason}, n_consec={n_consec}, F_max={f_max_final:.3e}",
        f"center_site=({ci},{cj},{ck}), c_inj={c_inj}, N_c={N_c}",
        f"Q_norm={Q_norm:.3e}, A*r_max³={A_norm*r_max**3:.3e}",
    ] + verdict_notes

    return {
        "stop_reason": stop_reason,
        "n_consec": n_consec,
        "f_max": f_max_final,
        "f0": f0,
        "f0_vec": f0_vec,
        "Q_vec": Q_vec,
        "A_vec": A_vec,
        "Q_norm": Q_norm,
        "A_norm": A_norm,
        "ball_results": ball_results,
        "phi_exps": phi_exps,
        "tols": tols,
        "n_cs": n_cs,
        "N_c": N_c,
        "c_inj": c_inj,
        "verdict": verdict,
        "notes": notes,
        "center_site": (ci, cj, ck),
        "f_max_history": ru["f_max_history"],
        "lambda_max": ru["lambda_max"],
        "lr_halvings": ru["lr_halvings"],
        "n_iter": ru["n_iter"],
        "tau": ru["tau"],
        "resids": resids,
    }
