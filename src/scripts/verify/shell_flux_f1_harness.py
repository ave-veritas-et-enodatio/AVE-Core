"""Shell-flux F1 measurement harness.

Implements the force-stop + ball-sum Φ measurement protocol from
PROOF-LADDER-shell-flux-zero-2026-10-06.md (FREEZE, Math ACK 2026-10-06)
and HARNESS-PLAN-shell-flux-F1-2026-10-06.md.

NO Mac run until Engine Rigor Gate re-checks this harness vs FREEZE AND
Orchestrator schedules (after #1062 green+merged).

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

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Sequence, Tuple

import numpy as np

# ── FROZEN constants (Math ACK 2026-10-06) ───────────────────────────────────
F_STOP: float = 1e-8          # force-stop threshold (natural units G=Gc=γ=1)
K_TOL: int = 3                # coherent worst-case multiplier (not tone k=5)
C_TOL: float = 6e3            # float accumulation coefficient
EPS_MACHINE: float = 2.0**-52  # double precision machine epsilon
CONSEC_REQUIRED: int = 3      # consecutive below-F_STOP checks to declare stop

# Default radii for 64³ box (deep inside, R26.102 + r³-fit requirement)
DEFAULT_RADII: Tuple[float, ...] = (12.0, 18.0, 24.0)

# Cold seed amplitude (R26.196a: |ε|/ε_y ≪ 0.41, prefer <0.17–0.29)
# amplitude_scale * sqrt(3)/2 * pi / pi = amplitude_scale * sqrt(3)/2
# With COLD_AMPLITUDE_SCALE=0.20: peak omega / omega_yield ≈ 0.173
COLD_AMPLITUDE_SCALE: float = 0.20

# Threshold for |Q| > kill_ratio * tol(r_min) → KILL (operationalizes "≫")
DEFAULT_KILL_RATIO: float = 10.0


class Verdict(str, Enum):
    """F1 measurement verdict per FROZEN kill/pass/inconclusive table."""

    PASS_F1 = "PASS_F1"
    """force-stop + |Φ|<tol at ≥3 radii.
    Clean variant additionally requires |Q|<tol(r_min) AND |A|r_max³<tol(r_max)."""
    KILL_F1 = "KILL_F1"
    """force-stop + |Q|≫tol(r_min) stable across radii / box types, no pins/drive."""
    INCONCLUSIVE = "INCONCLUSIVE"
    """No force-stop; energy slope >1%/100 at stop; nonzero A + tiny Q."""
    OUT_OF_SCOPE = "OUT_OF_SCOPE"
    """Pins/drive present — out of scope for in-scope F1 verdict."""


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

    grid_desc: str           # e.g. "64³ periodic"
    seed_eps_ratio: float    # amplitude_scale * sqrt(3)/2 ≈ |ω_peak|/ω_yield proxy
    stop_reason: str         # "force_stop" | "max_iter" | "lr_underflow" | "untied"
    n_consec: int            # consecutive F_max < F_STOP checks at stop
    f_max: float             # measured F_max = max_alive ‖∂E/∂u‖_∞
    f_rms: float             # ‖∇_u E‖₂ / √N_alive
    energy: float
    energy_slope_pct_100: float   # %/100 steps at stop; >1 → INCONCLUSIVE
    crossings: int
    peak_omega: float        # max |ω| over alive sites
    ball_results: list       # list[BallSumResult] ordered by ascending radius
    Q_vec: np.ndarray        # shape (3,) — monopole term from Φ = Q + A r³ fit
    A_vec: np.ndarray        # shape (3,) — volume coefficient
    Q_norm: float            # ‖Q‖₂
    A_norm: float            # ‖A‖₂
    verdict: Verdict
    notes: list = field(default_factory=list)


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

def _energy_slope_pct(history: list, window: int = 100) -> float:
    """% drop in energy over the last `window` steps.

    Returns (E_{-window-1} - E_{-1}) / |E_{-window-1}| * 100.
    Positive means energy decreased (dropped), negative means it increased.
    Returns 0.0 if history is too short.
    """
    if len(history) < window + 1:
        return 0.0
    E_end = history[-1]
    E_start = history[-(window + 1)]
    denom = abs(E_start)
    if denom < 1e-12:
        return 0.0
    return 100.0 * (E_start - E_end) / denom


# ── Verdict logic ─────────────────────────────────────────────────────────────

def compute_verdict(
    stop_info: dict,
    ball_results: list,
    Q_norm: float,
    A_norm: float,
    radii: Sequence[float],
    has_pins: bool = False,
    kill_ratio: float = DEFAULT_KILL_RATIO,
) -> Tuple[Verdict, list]:
    """Apply FROZEN kill/pass/inconclusive table.

    Returns (verdict, notes).

    kill_ratio: |Q| > kill_ratio * tol(r_min) operationalizes '≫'.
    Stricter-wins: if Gate tightens kill_ratio, pass the new value.
    """
    notes: list = []

    if has_pins:
        return Verdict.OUT_OF_SCOPE, ["pins/drive present — out of scope"]

    stop_reason = stop_info["stop_reason"]
    n_consec = stop_info["n_consec"]
    f_max = stop_info["f_max"]
    E_hist = stop_info.get("energy_history", [])
    energy_slope = _energy_slope_pct(E_hist)

    if stop_reason != "force_stop" or n_consec < CONSEC_REQUIRED:
        notes.append(
            f"INCONCLUSIVE: no force-stop (stop_reason={stop_reason!r}, "
            f"n_consec={n_consec} < {CONSEC_REQUIRED})"
        )
        return Verdict.INCONCLUSIVE, notes

    if energy_slope > 1.0:
        notes.append(
            f"INCONCLUSIVE: energy still dropping {energy_slope:.2f}%/100 steps at stop "
            f"(>1% threshold)"
        )
        return Verdict.INCONCLUSIVE, notes

    tol_r_min = frozen_tol(ball_results[0].n_ball, f_max)
    tol_r_max = frozen_tol(ball_results[-1].n_ball, f_max)
    r_max = float(max(radii))

    all_phi_pass = all(br.passes for br in ball_results)

    if all_phi_pass:
        Q_pass = Q_norm < tol_r_min
        A_pass = A_norm * r_max**3 < tol_r_max
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
    max_iter: int = 20000,
    f_stop: float = F_STOP,
    consec_required: int = CONSEC_REQUIRED,
    lr_init: float = 0.01,
    verbose: bool = False,
) -> dict:
    """Force-stop relaxation gate for the F1 harness.

    External gradient-descent loop — does NOT modify engine defaults or
    relax_to_ground_state on the main physics path.

    Stops when F_max = max_alive ‖∂E/∂u‖_∞ < f_stop on ≥consec_required
    consecutive gradient evaluations.  Also checks for untying (topology loss).

    max_iter: freeze requires ≥20k; caller may pass up to 50k.

    Returns dict:
      stop_reason   "force_stop" | "max_iter" | "lr_underflow" | "untied"
      n_consec      consecutive F_max < f_stop checks at stop
      f_max         measured max_alive ‖∂E/∂u‖_∞ at stop state
      f_rms         ‖∇_u E‖₂ / √N_alive at stop state
      energy        total energy at stop state
      energy_history list of total_energy() at the start of each iteration
      crossings     extract_crossing_count() at stop
      peak_omega    max |ω| over alive sites at stop
    """
    lr = float(lr_init)
    E_history: list = []
    n_consec = 0
    f_max_last = float("inf")
    f_rms_last = 0.0
    stop_reason = "max_iter"
    c_init = -1

    for step in range(max_iter):
        dE_du, dE_dw = engine.energy_gradient()
        E = float(engine.total_energy())
        E_history.append(E)

        alive = engine.mask_alive
        du_alive = dE_du[alive]
        n_alive = int(alive.sum())

        if n_alive > 0:
            f_max_last = float(np.max(np.abs(du_alive)))
            f_rms_last = float(np.sqrt(np.sum(du_alive**2) / n_alive))
        else:
            f_max_last = 0.0
            f_rms_last = 0.0

        # Force-stop criterion
        if f_max_last < f_stop:
            n_consec += 1
            if n_consec >= consec_required:
                stop_reason = "force_stop"
                break
        else:
            n_consec = 0

        # Early-exit on untying
        try:
            c = int(engine.extract_crossing_count())
        except Exception:
            c = -1
        if step == 0:
            c_init = c
        elif c >= 0 and c_init >= 0 and c < c_init:
            stop_reason = "untied"
            break

        # Gradient descent with backtracking lr
        noise_floor = 1e-12 * max(abs(E), 1.0)
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
            if lr < 1e-14:
                stop_reason = "lr_underflow"
                break
        else:
            lr = min(lr * 1.1, 1.0)

        if verbose and step % 500 == 0:
            print(
                f"  step {step:6d}  E={E:.6e}  F_max={f_max_last:.3e}  "
                f"consec={n_consec}  lr={lr:.2e}"
            )

    # State at stop: compute derived quantities
    omega_mag = np.sqrt(np.sum(engine.omega**2, axis=-1))
    peak_omega = float(np.max(omega_mag[engine.mask_alive])) if engine.mask_alive.any() else 0.0

    try:
        crossings = int(engine.extract_crossing_count())
    except Exception:
        crossings = -1

    return {
        "stop_reason": stop_reason,
        "n_consec": n_consec,
        "f_max": f_max_last,
        "f_rms": f_rms_last,
        "energy": E_history[-1] if E_history else float("nan"),
        "energy_history": E_history,
        "crossings": crossings,
        "peak_omega": peak_omega,
    }


# ── Full measurement pipeline ─────────────────────────────────────────────────

def measure_shell_flux(
    engine,
    radii: Sequence[float] = DEFAULT_RADII,
    grid_desc: str = "64³ periodic",
    amplitude_scale: float = COLD_AMPLITUDE_SCALE,
    max_iter: int = 20000,
    verbose: bool = False,
    has_pins: bool = False,
) -> RunResult:
    """Run force-stop + ball-sum Φ measurement pipeline for F1.

    Engine must already have the (2,3)-torus-knot seeded (call seed_cold_knot
    before this).  Returns RunResult with verdict and full log.

    NO Mac run: this function exists to be audited against the FREEZE; the
    actual run is blocked until Engine Rigor Gate re-check + Orchestrator
    schedules (after #1062 green+merged).
    """
    stop_info = force_stop_relax(engine, max_iter=max_iter, verbose=verbose)

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
        stop_info, ball_results, Q_norm, A_norm, radii, has_pins=has_pins
    )

    seed_eps_ratio = amplitude_scale * (np.sqrt(3.0) / 2.0)  # ≈ |ω_peak|/ω_yield

    return RunResult(
        grid_desc=grid_desc,
        seed_eps_ratio=seed_eps_ratio,
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
    )


# ── Engine factories ──────────────────────────────────────────────────────────

def make_engine_64_periodic(use_saturation: bool = True):
    """Default 64³ periodic box (FROZEN: even edges, dx=1, G=Gc=γ=1, ε_y=1)."""
    from ave.topological.cosserat_field_3d import CosseratField3D
    return CosseratField3D(64, 64, 64, use_saturation=use_saturation)


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

    amplitude_scale=0.20 → peak |ω|/ω_yield ≈ 0.173 (prefer <0.17–0.29).
    Hot ENV-D seeds are out of scope (may have no force-stationary point).
    """
    engine.initialize_2_3_torus_knot_sector(
        R_target=R, r_target=r, amplitude_scale=amplitude_scale
    )


# ── Empty-grid sanity ─────────────────────────────────────────────────────────

def run_empty_grid_sanity(radius: float = 6.0, grid_size: int = 16) -> dict:
    """Empty-grid sanity: zero u+ω → |Φ| ≈ 0 within float tolerance.

    Uses a small grid for speed.  At u=ω=0 the energy gradient is exactly zero
    (all strain/curvature terms vanish), so Φ = 0 exactly to float precision.

    Returns dict with keys: phi_vec, phi_norm, n_ball, float_tol, passes_sanity.
    """
    from ave.topological.cosserat_field_3d import CosseratField3D
    engine = CosseratField3D(grid_size, grid_size, grid_size, use_saturation=False)
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
