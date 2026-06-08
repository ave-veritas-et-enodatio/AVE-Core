#!/usr/bin/env python3
r"""L5 alpha-free Q/leakage on unified MasterEquationFDTD + PhasorBridge lane.

SCOPE NOTE (2026-06-07 L5 leakage):
Measures alpha-free leakage/Q proxies at rest-scale (amp=0.48) vs wall-window
(amp=3.0) amplitudes identified by the calibration-crux sweep. Does NOT claim
alpha emergence, electron genesis, or Theorem 3.1' closure. Alpha constants are
comparison-only.

Prereg: research/2026-06-07_unified-l5-q-leakage-prereg.md
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np

import ave.core.constants as _avc
from ave.core.constants import ALPHA_COLD, ALPHA_COLD_INV
from ave.core.master_equation_fdtd import MasterEquationFDTD
from ave.core.master_fdtd_phasor_bridge import PORT_SHIFTS, MasterFDTDPhasorBridge


PROJECT_ROOT = next(p for p in Path(__file__).resolve().parents if (p / ".git").exists())
OUT_DIR = PROJECT_ROOT / "src" / "scripts" / "vol_1_foundations" / "_output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

CASES = [
    {"label": "rest_scale", "amplitude": 0.48, "prior_A_squared_peak": 0.23},
    {"label": "wall_window", "amplitude": 3.0, "prior_gamma_min_uncapped": -0.49},
]
FOUR_PI = 4.0 * math.pi
MATCH_TOLERANCE = 0.15
N_STEPS = 2400
CADENCE = 4
SEED_RADIUS = 2.5
SHELL_RADIUS = 8
STRAIN_THRESHOLD_FRAC = 0.1


def verify_canonical_sources() -> None:
    constants_path = Path(_avc.__file__).as_posix()
    if not constants_path.endswith("src/ave/core/constants.py"):
        raise RuntimeError(f"ave.core.constants loaded from unexpected path: {constants_path}")
    if not (100.0 < float(ALPHA_COLD_INV) < 200.0 and 0.0 < float(ALPHA_COLD) < 0.01):
        raise RuntimeError("canonical alpha comparison constants outside expected range")


def fwhm_3d(field: np.ndarray) -> float:
    mag = np.abs(field)
    peak = float(np.max(mag))
    if peak <= 1e-12:
        return 0.0
    above = mag > peak / 2.0
    n_cells = int(np.sum(above))
    if n_cells == 0:
        return 0.0
    radius = (3.0 * n_cells / (4.0 * math.pi)) ** (1.0 / 3.0)
    return float(2.0 * radius)


def q_factor_decomposition(V_field: np.ndarray, center: tuple[int, int, int], R_boundary: float) -> tuple[float, float, float]:
    cx, cy, cz = center
    i, j, k = np.indices(V_field.shape)
    r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2)
    V_sq = V_field**2
    V_max = float(np.max(np.abs(V_field)))
    if V_max < 1e-10:
        return 0.0, 0.0, 0.0
    V_normalized = V_sq / (V_max**2)

    volume_mask = r < R_boundary
    surface_mask = (r >= R_boundary - 0.5) & (r < R_boundary + 0.5)
    z_axis = (i - cx) ** 2 + (j - cy) ** 2
    line_mask = (np.abs(k - cz) < 1) & (np.sqrt(z_axis) >= R_boundary - 0.5) & (np.sqrt(z_axis) < R_boundary + 0.5)

    L_vol = float(np.sum(V_normalized[volume_mask]))
    L_surf = float(np.sum(V_normalized[surface_mask]))
    L_line = float(np.sum(V_normalized[line_mask]))
    return L_vol, L_surf, L_line


def shell_mask(
    shape: tuple[int, int, int],
    center: tuple[int, int, int],
    V: np.ndarray,
    *,
    radius: int,
    threshold_frac: float,
    active_mask: np.ndarray,
) -> np.ndarray:
    cx, cy, cz = center
    i, j, k = np.indices(shape)
    r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2)
    peak = float(np.max(np.abs(V[active_mask]))) if active_mask.any() else 0.0
    if peak <= 1e-15:
        return np.zeros(shape, dtype=bool)
    return (np.abs(V) >= threshold_frac * peak) & active_mask & (r <= radius)


def bond_gamma_values_uncapped(
    bridge: MasterFDTDPhasorBridge,
    V: np.ndarray,
    shell: np.ndarray,
    *,
    S_min: float,
) -> np.ndarray:
    S = bridge.saturation_kernel(V, S_min=S_min, A_cap=None)
    z = 1.0 / np.sqrt(np.maximum(S, S_min))
    z[~bridge.mask_active] = 1.0
    gammas: list[float] = []
    for shift in PORT_SHIFTS:
        z_nb = np.roll(z, shift=shift, axis=(0, 1, 2))
        denom = z_nb + z
        with np.errstate(divide="ignore", invalid="ignore"):
            g = (z_nb - z) / denom
        valid = shell & bridge.mask_active & (np.abs(denom) > 1e-15)
        vals = g[valid]
        gammas.extend(float(x) for x in vals if np.isfinite(x))
    return np.asarray(gammas, dtype=float)


def estimate_ringdown_q(times: np.ndarray, center_trace: np.ndarray) -> dict[str, Any]:
    if len(times) < 12:
        return {"Q_decay": None, "decay_fit_ok": False, "breathing_freq_hz": None, "decay_tau": None}
    transient = max(3, len(times) // 5)
    t = times[transient:]
    y = np.abs(center_trace[transient:])
    if len(t) < 8 or float(np.max(y)) <= 1e-12:
        return {"Q_decay": None, "decay_fit_ok": False, "breathing_freq_hz": None, "decay_tau": None}

    # Envelope via local maxima
    peaks_idx = []
    for idx in range(1, len(y) - 1):
        if y[idx] >= y[idx - 1] and y[idx] > y[idx + 1] and y[idx] > 0.02 * float(np.max(y)):
            peaks_idx.append(idx)
    if len(peaks_idx) < 3:
        return {"Q_decay": None, "decay_fit_ok": False, "breathing_freq_hz": None, "decay_tau": None}

    peak_t = t[np.array(peaks_idx)]
    peak_a = y[np.array(peaks_idx)]
    if float(np.min(peak_a)) <= 0.0:
        return {"Q_decay": None, "decay_fit_ok": False, "breathing_freq_hz": None, "decay_tau": None}

    # log-linear decay on peak envelope
    coeffs = np.polyfit(peak_t, np.log(peak_a), 1)
    decay_rate = -float(coeffs[0])
    if decay_rate <= 0.0:
        return {"Q_decay": None, "decay_fit_ok": False, "breathing_freq_hz": None, "decay_tau": None}
    tau = 1.0 / decay_rate

    dt_mean = float(np.mean(np.diff(peak_t))) if len(peak_t) > 1 else float(np.mean(np.diff(t)))
    f_est = 1.0 / (2.0 * dt_mean) if dt_mean > 0 else None
    Q_decay = math.pi * f_est * tau if f_est is not None else None
    return {
        "Q_decay": float(Q_decay) if Q_decay is not None and math.isfinite(Q_decay) else None,
        "decay_fit_ok": True,
        "breathing_freq_hz": float(f_est) if f_est is not None else None,
        "decay_tau": float(tau),
        "decay_rate": float(decay_rate),
        "n_peaks_used": len(peaks_idx),
    }


def relative_error(value: float | None, target: float) -> float | None:
    if value is None or target <= 0:
        return None
    return float(abs(value - target) / target)


def classify_q_proxies(metrics: dict[str, Any]) -> dict[str, Any]:
    proxies = {
        "Q_gamma": metrics.get("Q_gamma"),
        "Q_phasor": metrics.get("Q_phasor"),
        "Q_lambda_sum": metrics.get("Q_lambda_sum"),
        "Q_decay": metrics.get("Q_decay"),
    }
    alpha_matches = []
    four_pi_matches = []
    for name, val in proxies.items():
        if val is None or not math.isfinite(val) or val <= 0:
            continue
        if relative_error(val, float(ALPHA_COLD_INV)) is not None and relative_error(val, float(ALPHA_COLD_INV)) <= MATCH_TOLERANCE:
            alpha_matches.append(name)
        if relative_error(val, FOUR_PI) is not None and relative_error(val, FOUR_PI) <= MATCH_TOLERANCE:
            four_pi_matches.append(name)

    if alpha_matches:
        outcome = "A_alpha_proximity"
        verdict = "L5_EMERGENCE_CANDIDATE"
    elif four_pi_matches:
        outcome = "B_four_pi_geometry"
        verdict = "L5_GEOMETRY_SCALE_ONLY"
    else:
        outcome = "C_no_alpha_scale"
        verdict = "L5_NEGATIVE"

    return {
        "outcome": outcome,
        "verdict": verdict,
        "alpha_matches": alpha_matches,
        "four_pi_matches": four_pi_matches,
        "match_tolerance": MATCH_TOLERANCE,
    }


def run_case(case: dict[str, Any]) -> dict[str, Any]:
    center = (16, 16, 16)
    amplitude = float(case["amplitude"])

    engine = MasterEquationFDTD(
        N=32,
        dx=1.0,
        V_yield=1.0,
        c0=1.0,
        pml_thickness=4,
        A_cap=0.99,
        S_min=0.05,
    )
    bridge = MasterFDTDPhasorBridge(
        nx=engine.N,
        ny=engine.N,
        nz=engine.N,
        dx=engine.dx,
        V_yield=engine.V_yield,
        dt=engine.dt,
    )
    bridge.reset_phi_link()
    engine.inject_localized_blob(center=center, radius=SEED_RADIUS, amplitude=amplitude, profile="sech")

    times: list[float] = []
    center_trace: list[float] = []
    energy_trace: list[float] = []
    a_peak_trace: list[float] = []
    gamma_mins: list[float | None] = []

    for step in range(N_STEPS + 1):
        if step > 0:
            bridge.project_from_scalar(engine.V, engine.V_prev, accumulate_phi=True, S_min=engine.S_min)
        if step % CADENCE == 0:
            times.append(float(engine.time))
            center_trace.append(float(engine.V[center]))
            energy_trace.append(float(engine.total_energy()))
            a_peak_trace.append(float(np.max(np.abs(engine.V)) / engine.V_yield))
            gamma_mins.append(
                bridge.bond_gamma_min_in_shell(
                    engine.V,
                    threshold_frac=STRAIN_THRESHOLD_FRAC,
                    center=center,
                    radius=SHELL_RADIUS,
                    A_cap=None,
                    S_min=engine.S_min,
                )
            )
        if step < N_STEPS:
            engine.step()

    shell = shell_mask(
        engine.V.shape,
        center,
        engine.V,
        radius=SHELL_RADIUS,
        threshold_frac=STRAIN_THRESHOLD_FRAC,
        active_mask=bridge.mask_active,
    )
    gammas = bond_gamma_values_uncapped(bridge, engine.V, shell, S_min=engine.S_min)
    gamma_min_trace = float(np.min([g for g in gamma_mins if g is not None])) if any(g is not None for g in gamma_mins) else None
    if len(gammas) > 0:
        gamma_min_shell = float(np.min(gammas))
        gamma_mean_shell = float(np.mean(gammas))
    else:
        gamma_min_shell = None
        gamma_mean_shell = None

    # Use the strongest short (most negative Γ) seen post-transient — not the
    # shell mean, which is dominated by matched-bulk bonds when |Γ| ≪ 1.
    gamma_for_leak = gamma_min_trace if gamma_min_trace is not None else gamma_min_shell
    if gamma_for_leak is not None:
        leak_gamma = float(1.0 - gamma_for_leak**2)
        bond_q_proxy_valid = bool(abs(gamma_for_leak) >= 0.1)
    else:
        leak_gamma = None
        bond_q_proxy_valid = False

    v_inc = bridge.V_inc[shell]
    v_ref = bridge.V_ref[shell]
    p_inc = float(np.sum(v_inc**2))
    p_ref = float(np.sum(v_ref**2))
    if p_inc > 1e-15:
        rho_phasor = p_ref / p_inc
        leak_phasor = rho_phasor / (1.0 + rho_phasor)
        Q_phasor = math.pi / leak_phasor if leak_phasor > 1e-15 else None
    else:
        rho_phasor = None
        leak_phasor = None
        Q_phasor = None

    Q_gamma = math.pi / leak_gamma if leak_gamma is not None and leak_gamma > 1e-15 else None

    R_boundary = max(SEED_RADIUS, fwhm_3d(engine.V))
    L_vol, L_surf, L_line = q_factor_decomposition(engine.V, center, R_boundary)
    Q_lambda_sum = L_vol + L_surf + L_line

    ringdown = estimate_ringdown_q(np.asarray(times), np.asarray(center_trace))

    a_peak_max = float(np.max(a_peak_trace)) if a_peak_trace else 0.0
    metrics = {
        "seed_amplitude": amplitude,
        "case_label": case["label"],
        "alpha_used_as_input": False,
        "A_peak_max_trace": a_peak_max,
        "A_squared_peak_max_trace": float(a_peak_max**2),
        "A_peak_final": float(np.max(np.abs(engine.V)) / engine.V_yield),
        "gamma_min_shell_final": gamma_min_shell,
        "gamma_mean_shell_final": gamma_mean_shell,
        "gamma_min_post_transient_trace": gamma_min_trace,
        "gamma_used_for_leak": gamma_for_leak,
        "bond_q_proxy_valid": bond_q_proxy_valid,
        "leak_fraction_gamma": leak_gamma,
        "leak_fraction_phasor": leak_phasor,
        "Q_gamma": Q_gamma,
        "Q_phasor": Q_phasor,
        "L_vol": L_vol,
        "L_surf": L_surf,
        "L_line": L_line,
        "Q_lambda_sum": Q_lambda_sum,
        "R_boundary_used": R_boundary,
        "rho_phasor_ref_over_inc": rho_phasor,
        **ringdown,
    }
    metrics["classification"] = classify_q_proxies(metrics)
    metrics["comparison_only"] = {
        "alpha_cold": float(ALPHA_COLD),
        "alpha_cold_inv": float(ALPHA_COLD_INV),
        "four_pi": float(FOUR_PI),
        "rel_err_Q_gamma_vs_alpha_inv": relative_error(Q_gamma, float(ALPHA_COLD_INV)),
        "rel_err_Q_gamma_vs_four_pi": relative_error(Q_gamma, FOUR_PI),
        "rel_err_Q_lambda_vs_alpha_inv": relative_error(Q_lambda_sum, float(ALPHA_COLD_INV)),
        "rel_err_Q_lambda_vs_four_pi": relative_error(Q_lambda_sum, FOUR_PI),
        "rel_err_leak_gamma_vs_alpha": relative_error(leak_gamma, float(ALPHA_COLD)) if leak_gamma is not None else None,
    }
    return metrics


def classify_pair(rest: dict[str, Any], wall: dict[str, Any]) -> dict[str, Any]:
    rest_verdict = rest["classification"]["verdict"]
    wall_verdict = wall["classification"]["verdict"]
    if rest_verdict != wall_verdict:
        pair_outcome = "D_amplitude_dependent"
        pair_verdict = "L5_AMPLITUDE_DEPENDENT"
    elif rest_verdict == "L5_EMERGENCE_CANDIDATE":
        pair_outcome = "A_alpha_both"
        pair_verdict = "L5_EMERGENCE_CANDIDATE_BOTH"
    elif rest_verdict == "L5_GEOMETRY_SCALE_ONLY":
        pair_outcome = "B_geometry_both"
        pair_verdict = "L5_GEOMETRY_SCALE_BOTH"
    else:
        pair_outcome = "C_negative_both"
        pair_verdict = "L5_NEGATIVE_BOTH"

    rest_leak = rest.get("leak_fraction_gamma")
    wall_leak = wall.get("leak_fraction_gamma")
    # Higher leak fraction means weaker confinement (more transmission per bounce).
    leak_rises = bool(rest_leak is not None and wall_leak is not None and wall_leak > rest_leak + 0.01)

    return {
        "outcome": pair_outcome,
        "verdict": pair_verdict,
        "rest_verdict": rest_verdict,
        "wall_verdict": wall_verdict,
        "wall_leak_exceeds_rest_leak": leak_rises,
        "interpretation": (
            "Alpha-free L5 leakage/Q proxies on unified projection lane at calibration-crux amplitudes. "
            "No alpha inserted; comparison to 137 and 4π is post-hoc only."
        ),
    }


def main() -> None:
    verify_canonical_sources()
    results = [run_case(case) for case in CASES]
    by_label = {r["case_label"]: r for r in results}
    pair_classification = classify_pair(by_label["rest_scale"], by_label["wall_window"])
    payload = {
        "scope": "L5 alpha-free Q/leakage; unified projection lane; alpha comparison-only",
        "cases": CASES,
        "results": results,
        "pair_classification": pair_classification,
    }
    out_path = OUT_DIR / "unified_l5_q_leakage_results.json"
    out_path.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n")

    print("Unified L5 alpha-free Q/leakage")
    print(f"  pair verdict: {pair_classification['verdict']} ({pair_classification['outcome']})")
    for row in results:
        cls = row["classification"]
        print(f"  case={row['case_label']:12s}  amp={row['seed_amplitude']:.2f}")
        print(f"    A_peak_trace={row['A_peak_max_trace']:.3f}  gamma_min_trace={row['gamma_min_post_transient_trace']}")
        print(f"    leak_gamma={row['leak_fraction_gamma']}  Q_gamma={row['Q_gamma']}  bond_q_valid={row['bond_q_proxy_valid']}")
        print(f"    Q_lambda={row['Q_lambda_sum']:.2f}  Q_decay={row['Q_decay']}")
        print(f"    verdict={cls['verdict']} ({cls['outcome']})")
    print("  alpha: comparison-only; not inserted")
    print(f"  wrote: {out_path}")


if __name__ == "__main__":
    main()
