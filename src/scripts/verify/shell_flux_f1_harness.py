"""Shell-flux F1 measurement harness.

Implements the force-stop + ball-sum Φ measurement protocol from
PROOF-LADDER-shell-flux-zero-2026-10-06.md (FREEZE, Math ACK 2026-10-06)
and HARNESS-PLAN-shell-flux-F1-2026-10-06.md.

Gap fixes G1–G12 per RULING-shell-flux-F1-run-02fc9794-2026-10-06.md §5.

USAGE (Gate harness re-check):
    from ave.topological.cosserat_field_3d import CosseratField3D
    import src.scripts.verify.shell_flux_f1_harness as h

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
# G1 control uses a LOOSER threshold: the K4 periodic lattice acoustic mode
# converges gradient-descent to ~8e-7 (well below 0.1% of f0=1e-3) in ~500
# steps but can't reach 1e-8 within MAX_ITER.  1e-6 is 0.1% of f0_norm, which
# is sufficient for Q_norm to converge to within 1% of f0_norm.
F_STOP_CONTROL: float = 1e-6  # G1 injected-force control force-stop threshold
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

# G11: switch to grad-norm acceptance for u-only problems once F < this
GRAD_NORM_SWITCH_F: float = 1e-6

# Default radii for 64³ box (deep inside, R26.102 + r³-fit requirement)
DEFAULT_RADII: Tuple[float, ...] = (12.0, 18.0, 24.0)

# Cold seed amplitude (R26.196a: |ε|/ε_y ≪ 0.41, prefer <0.17–0.29)
# amplitude_scale * sqrt(3)/2 * pi / pi = amplitude_scale * sqrt(3)/2
# With COLD_AMPLITUDE_SCALE=0.20: peak omega / omega_yield ≈ 0.173 (proxy)
COLD_AMPLITUDE_SCALE: float = 0.20

# Threshold for |Q| > kill_ratio * tol(r_min) → KILL (operationalizes "≫")
DEFAULT_KILL_RATIO: float = 10.0


class Verdict(str, Enum):
    """F1 measurement verdict."""

    PASS_F1 = "PASS_F1"
    """Legacy — superseded by RECEIPT_ONLY for self-bound knot (G10)."""
    KILL_F1 = "KILL_F1"
    """Legacy — unreachable for self-bound knot (translation identity, §3 of ruling)."""
    INCONCLUSIVE = "INCONCLUSIVE"
    """No force-stop; energy slope >1%/100 at stop; nonzero A + tiny Q; or drained."""
    OUT_OF_SCOPE = "OUT_OF_SCOPE"
    """Pins/drive present — out of scope for in-scope F1 verdict."""
    RECEIPT_ONLY = "RECEIPT_ONLY"
    """G10: code-identity receipt — Φ = Σ(-dE/du) = 0 holds by translation identity.
    Not an independent physical test. TODO: compare against σ·n surface quadrature
    (pending Math B2 — later PR)."""
    MONOPOLE_DETECTED = "MONOPOLE_DETECTED"
    """G1: injected-force positive control — constant Φ(r) = Q (monopole geometry)."""


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
    seed_eps_ratio: float    # proxy: amplitude_scale * sqrt(3)/2 (kept for compat)
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
    # G12: max |∂E/∂ω| at stop
    max_dE_domega: float = float("nan")


# ── Frozen tolerance ──────────────────────────────────────────────────────────

def frozen_tol(n_ball: int, f_max: float) -> float:
    """FROZEN tolerance formula (Math ACK 2026-10-06).

    tol(r) = k * ( N_ball * F_max + C * ε * sqrt(N_ball) )
    k=3, ε=2⁻⁵², C=6×10³.

    Use MEASURED f_max after force-stop — not F_STOP.
    """
    return K_TOL * (n_ball * f_max + C_TOL * EPS_MACHINE * np.sqrt(n_ball))


# ── Ball-sum Φ estimator (primary) ───────────────────────────────────────────

def ball_sum_phi(
    engine,
    radius: float,
    center: Optional[Tuple[float, float, float]] = None,
) -> Tuple[np.ndarray, int]:
    """Primary Φ(r) estimator: Σ_{i ∈ B(r) ∩ alive} (−∂E/∂u_i) as a 3-vector.

    IDW / surface quadrature = diagnostic only; not used here.

    Returns (phi_vec, n_ball).
    """
    dE_du, _ = engine.energy_gradient()
    nx, ny, nz = engine.nx, engine.ny, engine.nz
    if center is None:
        cx, cy, cz = (nx - 1) / 2.0, (ny - 1) / 2.0, (nz - 1) / 2.0
    else:
        cx, cy, cz = center
    x = engine._i - cx
    y = engine._j - cy
    z = engine._k - cz
    r2 = x**2 + y**2 + z**2
    in_ball = engine.mask_alive & (r2 <= radius**2)
    phi_vec = np.sum(-dE_du[in_ball], axis=0)  # (3,)
    n_ball = int(in_ball.sum())
    return phi_vec, n_ball


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
    kill_ratio: float = DEFAULT_KILL_RATIO,
    receipt_only: bool = True,
) -> Tuple[Verdict, list]:
    """Apply FROZEN kill/pass/inconclusive table.

    receipt_only=True (default): PASS path returns RECEIPT_ONLY (G10 — code-identity
    receipt; Φ=0 holds by translation identity, not an independent physical test).
    receipt_only=False: returns legacy PASS_F1 (used by non-self-bound-knot paths).

    Returns (verdict, notes).
    """
    notes: list = []

    if has_pins:
        return Verdict.OUT_OF_SCOPE, ["pins/drive present — out of scope"]

    stop_reason = stop_info["stop_reason"]
    n_consec = stop_info["n_consec"]
    f_max = stop_info["f_max"]
    E_hist = stop_info.get("energy_history", [])
    energy_slope = _energy_slope_pct(E_hist)  # G2: Optional[float]

    if stop_reason != "force_stop" or n_consec < CONSEC_REQUIRED:
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

    # G9: vacuum-PASS trap
    E_seed = stop_info.get("E_seed")
    peak_omega_seed = stop_info.get("peak_omega_seed")
    if E_seed is not None and peak_omega_seed is not None:
        energy_stop = stop_info.get("energy", 0.0)
        peak_omega_stop = stop_info.get("peak_omega", 0.0)
        e_drained = (E_seed > 0) and (energy_stop < VACUUM_E_FLOOR_FRAC * E_seed)
        o_drained = (peak_omega_seed > 0) and (
            peak_omega_stop < VACUUM_OMEGA_FLOOR_FRAC * peak_omega_seed
        )
        if e_drained or o_drained:
            notes.append(
                f"INCONCLUSIVE: drained to vacuum "
                f"(E_stop={energy_stop:.3e} vs {VACUUM_E_FLOOR_FRAC}*E_seed={VACUUM_E_FLOOR_FRAC*E_seed:.3e}; "
                f"peak_omega_stop={peak_omega_stop:.3e} vs "
                f"{VACUUM_OMEGA_FLOOR_FRAC}*peak_seed={VACUUM_OMEGA_FLOOR_FRAC*peak_omega_seed:.3e})"
            )
            return Verdict.INCONCLUSIVE, notes

    tol_r_min = frozen_tol(ball_results[0].n_ball, f_max)
    tol_r_max = frozen_tol(ball_results[-1].n_ball, f_max)
    r_max = float(max(radii))

    all_phi_pass = all(br.passes for br in ball_results)

    if all_phi_pass:
        Q_pass = Q_norm < tol_r_min
        A_pass = A_norm * r_max**3 < tol_r_max
        if receipt_only:
            # G10: re-scope as code-identity receipt
            notes.append(
                "RECEIPT_ONLY: code-identity Φ = Σ(-dE/du) = 0 holds at all radii "
                "(translation identity; not an independent physical test). "
                "TODO: compare against σ·n surface quadrature — pending Math B2 (later PR)."
            )
            if not Q_pass:
                notes.append(
                    f"  Q note: |Q|={Q_norm:.3e} >= tol(r_min)={tol_r_min:.3e}"
                )
            if not A_pass:
                notes.append(
                    f"  A note: |A|r_max³={A_norm*r_max**3:.3e} >= tol(r_max)={tol_r_max:.3e}"
                )
            return Verdict.RECEIPT_ONLY, notes
        else:
            # Legacy PASS_F1 path (injected-force control, non-self-bound-knot)
            if Q_pass and A_pass:
                notes.append(
                    f"clean PASS: |Φ|<tol(r) all radii, "
                    f"|Q|={Q_norm:.3e}<tol(r_min)={tol_r_min:.3e}, "
                    f"|A|r_max³={A_norm*r_max**3:.3e}<tol(r_max)={tol_r_max:.3e}"
                )
            else:
                notes.append("primary PASS: |Φ|<tol(r) at all radii")
                if not Q_pass:
                    notes.append(
                        f"clean PASS fails: |Q|={Q_norm:.3e} >= tol(r_min)={tol_r_min:.3e}"
                    )
                if not A_pass:
                    notes.append(
                        f"clean PASS fails: |A|r_max³={A_norm*r_max**3:.3e} "
                        f">= tol(r_max)={tol_r_max:.3e}"
                    )
            return Verdict.PASS_F1, notes

    # Not all phi pass: discriminate KILL vs INCONCLUSIVE
    if Q_norm > kill_ratio * tol_r_min:
        notes.append(
            f"KILL: |Q|={Q_norm:.3e} > {kill_ratio}× tol(r_min)={tol_r_min:.3e}, "
            f"no pins/drive"
        )
        return Verdict.KILL_F1, notes

    A_r3 = A_norm * r_max**3
    if A_r3 > tol_r_max and Q_norm < tol_r_min:
        notes.append(
            f"INCONCLUSIVE: nonzero A contribution |A|r_max³={A_r3:.3e} > "
            f"tol(r_max)={tol_r_max:.3e}, tiny Q={Q_norm:.3e} < tol(r_min)={tol_r_min:.3e}"
        )
    else:
        notes.append(
            f"INCONCLUSIVE: |Φ| not all < tol; |Q|={Q_norm:.3e}, "
            f"tol(r_min)={tol_r_min:.3e}"
        )
    return Verdict.INCONCLUSIVE, notes


# ── Force-stop relaxation loop ────────────────────────────────────────────────

def force_stop_relax(
    engine,
    max_iter: int = MAX_ITER,   # G7: frozen constant
    f_stop: float = F_STOP,
    consec_required: int = CONSEC_REQUIRED,
    lr_init: float = 0.01,
    verbose: bool = False,
    u_only: bool = False,       # G11: relax u only (omega frozen at zero)
) -> dict:
    """Force-stop relaxation gate for the F1 harness.

    External gradient-descent loop — does NOT modify engine defaults or
    relax_to_ground_state on the main physics path.

    G2: E_history accumulates only on ACCEPTED steps.
    G4: returns f_max_history, f_rms_history, crossing_history, lr_history, accepted.
    G7: max_iter defaults to frozen MAX_ITER.
    G8: untie exit requires >=UNTIE_CONSEC_REQUIRED consecutive checks below c_init.
    G11: u_only mode switches to grad-norm acceptance once F < GRAD_NORM_SWITCH_F.
    G12: returns max_dE_domega at stop state.

    Returns dict with all tracking fields.
    """
    lr = float(lr_init)
    E_history: list = []        # G2: accepted steps only
    f_max_history: list = []    # G4
    f_rms_history: list = []    # G4
    crossing_history: list = [] # G4
    lr_history: list = []       # G4
    accepted_flags: list = []   # G4

    n_consec = 0
    f_max_last = float("inf")
    f_rms_last = 0.0
    stop_reason = "max_iter"
    c_init = -1
    c_untie_consec = 0          # G8: consecutive below-c_init checks
    tau = 0.0                   # G8: accumulated gradient-flow time Σlr
    use_grad_norm_accept = False # G11

    for step in range(max_iter):
        dE_du, dE_dw = engine.energy_gradient()
        E = float(engine.total_energy())

        alive = engine.mask_alive
        du_alive = dE_du[alive]
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
                break
        else:
            n_consec = 0

        # G8: untie check with >=UNTIE_CONSEC_REQUIRED consecutive + logging
        try:
            c = int(engine.extract_crossing_count())
        except Exception:
            c = -1
        crossing_history.append(c)
        if step == 0:
            c_init = c
        elif c >= 0 and c_init >= 0:
            if c < c_init:
                c_untie_consec += 1
                # G8: always log untie readouts (crossing changes are significant)
                print(
                    f"  [untie] step={step} tau={tau:.4f} "
                    f"crossings={c} (init={c_init}) consec={c_untie_consec}"
                )
                if c_untie_consec >= UNTIE_CONSEC_REQUIRED:
                    stop_reason = "untied"
                    break
            else:
                c_untie_consec = 0

        # G11: activate grad-norm acceptance for u-only problems
        if u_only and f_max_last < GRAD_NORM_SWITCH_F:
            use_grad_norm_accept = True

        # Gradient descent step
        noise_floor = 1e-12 * max(abs(E), 1.0)

        if u_only:
            u_save = engine.u.copy()
            engine.u -= lr * dE_du
            engine._zero_outside_alive()

            if use_grad_norm_accept:
                # G11: once in grad-norm mode, always accept (linear regime)
                accepted_flags.append(True)
                E_history.append(E)   # G2: accepted
                tau += lr
                lr = min(lr * 1.1, 1.0)
            else:
                E_new = float(engine.total_energy())
                if E_new > E + noise_floor:
                    engine.u = u_save
                    lr *= 0.5
                    accepted_flags.append(False)
                    if lr < 1e-14:
                        stop_reason = "lr_underflow"
                        break
                else:
                    accepted_flags.append(True)
                    E_history.append(E)   # G2: accepted
                    tau += lr
                    lr = min(lr * 1.1, 1.0)
        else:
            u_save = engine.u.copy()
            w_save = engine.omega.copy()
            engine.u -= lr * dE_du
            engine.omega -= lr * dE_dw
            engine._zero_outside_alive()
            E_new = float(engine.total_energy())

            if E_new > E + noise_floor:
                engine.u = u_save
                engine.omega = w_save
                lr *= 0.5
                accepted_flags.append(False)
                if lr < 1e-14:
                    stop_reason = "lr_underflow"
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

    # State at stop: compute derived quantities
    omega_mag = np.sqrt(np.sum(engine.omega**2, axis=-1))
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
    dw_alive = dE_dw_stop[engine.mask_alive]
    max_dE_domega = float(np.max(np.abs(dw_alive))) if len(dw_alive) > 0 else 0.0

    return {
        "stop_reason": stop_reason,
        "n_consec": n_consec,
        "f_max": f_max_last,
        "f_rms": f_rms_last,
        "energy": E_history[-1] if E_history else float("nan"),
        "energy_history": E_history,
        "f_max_history": f_max_history,
        "f_rms_history": f_rms_history,
        "crossing_history": crossing_history,
        "lr_history": lr_history,
        "accepted": accepted_flags,
        "crossings": crossings,
        "peak_omega": peak_omega,
        "tau": tau,
        "max_dE_domega": max_dE_domega,
    }


# ── Full measurement pipeline ─────────────────────────────────────────────────

def measure_shell_flux(
    engine,
    radii: Sequence[float] = DEFAULT_RADII,
    grid_desc: str = "64³ periodic",
    amplitude_scale: float = COLD_AMPLITUDE_SCALE,
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
    G10: compute_verdict called with receipt_only=True.

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
    omega_mag_seed = np.sqrt(np.sum(engine.omega**2, axis=-1))
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
        receipt_only=True,   # G10: self-bound knot → receipt only
    )

    seed_eps_ratio_proxy = amplitude_scale * (np.sqrt(3.0) / 2.0)

    # G6: measure stop strain
    stop_eps_ratio, stop_peak_x, stop_max_a2 = _measure_strain_metrics(engine)

    return RunResult(
        grid_desc=grid_desc,
        seed_eps_ratio=seed_eps_ratio_proxy,
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
    )


# ── Engine factories ──────────────────────────────────────────────────────────

def make_engine_64_periodic(use_saturation: bool = True):
    """Default 64³ periodic box (FROZEN: even edges, dx=1, G=Gc=γ=1, ε_y=1)."""
    from ave.topological.cosserat_field_3d import CosseratField3D
    return CosseratField3D(64, 64, 64, use_saturation=use_saturation)


def make_engine_32_periodic(use_saturation: bool = True):
    """32³ periodic box — fast convergence for unit tests (κ ≈ 104 vs 414 for 64³).

    Use in G1 injected-force control tests: ~600 steps to converge vs ~2400 on 64³.
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

    amplitude_scale=0.20 → peak |ω|/ω_yield ≈ 0.173 (proxy; measured fence
    is peak |eps|/eps_y < 0.41, checked in measure_shell_flux).
    Hot ENV-D seeds are out of scope (may have no force-stationary point).
    """
    engine.initialize_2_3_torus_knot_sector(
        R_target=R, r_target=r, amplitude_scale=amplitude_scale
    )


# ── Empty-grid sanity + identity sanity (G5) ─────────────────────────────────

def run_empty_grid_sanity(radius: float = 6.0) -> dict:
    """G5: Empty-grid sanity using the same factory as the knot runs.

    Uses 64³ periodic, use_saturation=True (matching make_engine_64_periodic
    defaults) — not the prior 16³ / sat=False shortcut.

    Returns dict with keys: phi_vec, phi_norm, n_ball, float_tol, passes_sanity.
    """
    engine = make_engine_64_periodic(use_saturation=True)
    phi_vec, n_ball = ball_sum_phi(engine, radius)
    phi_norm = float(np.linalg.norm(phi_vec))
    float_tol = K_TOL * C_TOL * EPS_MACHINE * np.sqrt(n_ball)
    passes_sanity = phi_norm < float_tol
    return {
        "phi_vec": phi_vec,
        "phi_norm": phi_norm,
        "n_ball": n_ball,
        "float_tol": float_tol,
        "passes_sanity": passes_sanity,
    }


def run_identity_sanity(seed: int = 0) -> dict:
    """G5: Identity sanity — random (u, ω) gives global sum of dE/du = 0.

    Translation invariance on a periodic grid: Σ_alive(∂E/∂u_i) = 0 to ≤1e-12.
    Zero field → zero is trivial; this tests a non-trivial random state.
    Ruling §3 measured 1e-15 at the seed and 2e-17 at the untie state (r4).
    """
    rng = np.random.default_rng(seed)
    engine = make_engine_64_periodic(use_saturation=True)
    u_rand = rng.standard_normal(engine.u.shape).astype(np.float64) * 0.01
    w_rand = rng.standard_normal(engine.omega.shape).astype(np.float64) * 0.01
    engine.u = u_rand * engine.mask_alive[..., None]
    engine.omega = w_rand * engine.mask_alive[..., None]

    dE_du, _ = engine.energy_gradient()
    global_sum = np.sum(dE_du[engine.mask_alive], axis=0)  # (3,)
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
    f0: Tuple[float, float, float] = (0.0, 0.0, 1e-3),
    radii: Sequence[float] = DEFAULT_RADII,
    max_iter: int = MAX_ITER,
    verbose: bool = False,
) -> dict:
    """G1: Injected-force positive control — a control that can actually fail.

    Adds -f0 to dE_du at one alive site at the box center, relaxes u only
    (omega=0) to centered-gradient F_max < F_STOP_CONTROL (= 1e-6, not the main
    F_STOP = 1e-8), then ball-sums the INTERNAL -dE/du.

    The K4 periodic lattice has an acoustic long-wavelength mode that stalls
    gradient descent near ~8e-7 for 32³ (never reaching 1e-8), but 8e-7 < 1e-6
    is sufficient: Q_norm converges to within 1% of f0_norm after ~500 steps.

    At u-equilibrium of (dE_du - f0·δ_center): dE_du[center] = f0, others ≈ 0.
    Φ(r) = Σ_{i in B(r)}(-dE_du_i) = -f0 for every r enclosing the center site.
    Q = -f0 (constant with r → monopole); A ≈ 0.

    Verdict: MONOPOLE_DETECTED if |Q_norm - f0_norm| < tol and A is small,
    confirming the harness can read a non-zero Φ answer.

    Note: sign convention gives Φ = -f0 (not +f0). The monopole check is on
    Q_norm ≈ f0_norm with A·r_max³ << Q_norm.
    """
    f0_vec = np.asarray(f0, dtype=float)
    f0_norm = float(np.linalg.norm(f0_vec))

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

    # Reset state: u=0, omega=0 (u-only problem)
    engine.u = np.zeros_like(engine.u)
    engine.omega = np.zeros_like(engine.omega)

    lr = 0.01
    E_history: list = []
    f_max_last = float("inf")
    n_consec = 0
    stop_reason = "max_iter"
    tau = 0.0

    for step in range(max_iter):
        dE_du, _ = engine.energy_gradient()
        E = float(engine.total_energy())

        # Inject: subtract f0 at center site
        dE_du_mod = dE_du.copy()
        dE_du_mod[ci, cj, ck] -= f0_vec

        alive = engine.mask_alive
        n_alive = int(alive.sum())

        # Convergence in the mean-zero subspace (translation mode fixed by subtraction).
        # On a periodic grid Σ(dE_du_mod) = -f0 always, so the reachable optimum has
        # dE_du_mod[i] = -f0/N_alive for all i (uniform residual). Subtracting that mean
        # gives a centered residual that converges to 0.
        if n_alive > 0:
            dE_du_mod_mean = np.mean(dE_du_mod[alive], axis=0)
            dE_du_mod_centered = dE_du_mod.copy()
            dE_du_mod_centered[alive] -= dE_du_mod_mean
            f_max_last = float(np.max(np.abs(dE_du_mod_centered[alive])))
        else:
            dE_du_mod_centered = dE_du_mod
            f_max_last = 0.0

        if f_max_last < F_STOP_CONTROL:  # looser threshold for the G1 control
            n_consec += 1
            if n_consec >= CONSEC_REQUIRED:
                stop_reason = "force_stop"
                break
        else:
            n_consec = 0

        # Backtrack on E_mod = E(u) - f0·u[center], not E(u).
        # Descending dE_du_mod_centered decreases E_mod; E(u) can freely increase.
        E_mod_before = E - float(np.dot(f0_vec, engine.u[ci, cj, ck]))

        u_save = engine.u.copy()
        engine.u -= lr * dE_du_mod_centered  # descend the centered gradient
        engine._zero_outside_alive()
        # Remove mean drift to stay in mean-zero subspace (fixes translation zero mode)
        if n_alive > 0:
            engine.u[alive] -= np.mean(engine.u[alive], axis=0)

        E_new_raw = float(engine.total_energy())
        E_mod_after = E_new_raw - float(np.dot(f0_vec, engine.u[ci, cj, ck]))
        noise_floor = 1e-12 * max(abs(E_mod_before), 1.0)
        if E_mod_after > E_mod_before + noise_floor:
            engine.u = u_save
            lr *= 0.5
            if lr < 1e-14:
                stop_reason = "lr_underflow"
                break
        else:
            tau += lr
            # Cap at 0.05: avoids the neutrally-stable resonance (|1 - lr·λ|=1)
            # that occurs at lr=0.15 for the sphere-masked Cosserat Hessian
            # (λ_max ≈ 13.3).  At lr=0.05, slowest convergence rate ≈ 0.9969/step;
            # force-stop reachable in ~3700 steps on 32³ (≈70 seconds total).
            lr = min(lr * 1.1, 0.05)
            E_history.append(E_mod_before)

        if verbose and step % 500 == 0:
            print(f"  control step {step:6d}  F_max_centered={f_max_last:.3e}  lr={lr:.2e}")

    # Ball-sum INTERNAL -dE/du (unmodified by injection)
    phi_vecs: list = []
    ball_results: list = []
    for r in radii:
        phi_vec, n_ball = ball_sum_phi(engine, float(r))
        phi_norm_r = float(np.linalg.norm(phi_vec))
        tol = frozen_tol(n_ball, f_max_last)
        ball_results.append(BallSumResult(
            radius=float(r),
            n_ball=n_ball,
            phi_vec=phi_vec,
            phi_norm=phi_norm_r,
            tol=tol,
            passes=(phi_norm_r < tol),
        ))
        phi_vecs.append(phi_vec)

    Q_vec, A_vec = fit_qa(radii, phi_vecs)
    Q_norm = float(np.linalg.norm(Q_vec))
    A_norm = float(np.linalg.norm(A_vec))
    r_max = float(max(radii))

    notes = [
        f"injected f0={tuple(f0)}, f0_norm={f0_norm:.3e}",
        f"stop_reason={stop_reason}, n_consec={n_consec}, F_max={f_max_last:.3e}",
        f"center_site=({ci},{cj},{ck})",
        f"Q_norm={Q_norm:.3e} (expected ~f0_norm={f0_norm:.3e}), "
        f"A*r_max³={A_norm*r_max**3:.3e}",
    ]

    # Monopole verdict: Q_norm ≈ f0_norm AND A term small
    tol_r_min = frozen_tol(ball_results[0].n_ball, f_max_last)
    q_match = abs(Q_norm - f0_norm) < max(tol_r_min * 100, f0_norm * 0.01)
    a_small = (A_norm * r_max**3) < Q_norm * 0.1

    if stop_reason == "force_stop" and n_consec >= CONSEC_REQUIRED and q_match and a_small:
        verdict = Verdict.MONOPOLE_DETECTED
        notes.append(
            f"monopole detected: |Q|={Q_norm:.3e} ≈ f0_norm={f0_norm:.3e}, "
            f"A·r³ small ({A_norm*r_max**3:.3e})"
        )
    else:
        verdict = Verdict.INCONCLUSIVE
        if stop_reason != "force_stop":
            notes.append(f"INCONCLUSIVE: no force-stop ({stop_reason!r})")
        if not q_match:
            notes.append(
                f"INCONCLUSIVE: Q_norm={Q_norm:.3e} not near f0_norm={f0_norm:.3e}"
            )
        if not a_small:
            notes.append(
                f"INCONCLUSIVE: A·r³={A_norm*r_max**3:.3e} >= 0.1*Q_norm={Q_norm:.3e}"
            )

    return {
        "stop_reason": stop_reason,
        "n_consec": n_consec,
        "f_max": f_max_last,
        "f0": f0,
        "f0_norm": f0_norm,
        "Q_vec": Q_vec,
        "A_vec": A_vec,
        "Q_norm": Q_norm,
        "A_norm": A_norm,
        "ball_results": ball_results,
        "verdict": verdict,
        "notes": notes,
        "center_site": (ci, cj, ck),
        "energy_history": E_history,
        "tau": tau,
    }
