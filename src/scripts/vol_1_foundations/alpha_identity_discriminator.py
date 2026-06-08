#!/usr/bin/env python3
r"""α-identity discriminator — which AVE hypothesis best matches alpha-free data?

SCOPE NOTE (2026-06-07 alpha-identity):
Scores competing AVE framings of what alpha IS against the same amplitude battery
on the unified projection lane. Alpha constants are comparison-only for scoring.
Does NOT claim to derive alpha.

Prereg: research/2026-06-07_alpha-identity-discriminator-prereg.md
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

AMPLITUDES = [0.48, 1.0, 2.0, 3.0, 3.5, 4.0]
FOUR_PI = 4.0 * math.pi
SCREENED_HALF = 0.5
SCREENED_RMS_HALF = math.sqrt(0.5)
N_STEPS = 2400
CADENCE = 4
SEED_RADIUS = 2.5
SHELL_RADIUS = 8
STRAIN_THRESHOLD_FRAC = 0.1


def verify_canonical_sources() -> None:
    constants_path = Path(_avc.__file__).as_posix()
    if not constants_path.endswith("src/ave/core/constants.py"):
        raise RuntimeError(f"ave.core.constants loaded from unexpected path: {constants_path}")


def log_rel_err(measured: float | None, target: float) -> float | None:
    if measured is None or target <= 0 or not math.isfinite(measured) or measured <= 0:
        return None
    return float(abs(math.log10(measured / target)))


def q_factor_decomposition(V_field: np.ndarray, center: tuple[int, int, int], R_boundary: float) -> tuple[float, float, float]:
    cx, cy, cz = center
    i, j, k = np.indices(V_field.shape)
    r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2)
    V_max = float(np.max(np.abs(V_field)))
    if V_max < 1e-10:
        return 0.0, 0.0, 0.0
    V_normalized = (V_field**2) / (V_max**2)
    volume_mask = r < R_boundary
    surface_mask = (r >= R_boundary - 0.5) & (r < R_boundary + 0.5)
    z_axis = (i - cx) ** 2 + (j - cy) ** 2
    line_mask = (np.abs(k - cz) < 1) & (np.sqrt(z_axis) >= R_boundary - 0.5) & (np.sqrt(z_axis) < R_boundary + 0.5)
    return (
        float(np.sum(V_normalized[volume_mask])),
        float(np.sum(V_normalized[surface_mask])),
        float(np.sum(V_normalized[line_mask])),
    )


def shell_mask(shape, center, V, active_mask, radius, threshold_frac):
    cx, cy, cz = center
    i, j, k = np.indices(shape)
    r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2)
    peak = float(np.max(np.abs(V[active_mask]))) if active_mask.any() else 0.0
    if peak <= 1e-15:
        return np.zeros(shape, dtype=bool)
    return (np.abs(V) >= threshold_frac * peak) & active_mask & (r <= radius)


def screened_variance_2d(v_inc: np.ndarray, v_ref: np.ndarray) -> float:
    samples = np.column_stack([v_inc.ravel(), v_ref.ravel()])
    if samples.shape[0] < 4:
        return 0.0
    cov = np.cov(samples, rowvar=False)
    cov = np.atleast_2d(cov)
    eig = np.maximum(np.linalg.eigvalsh(cov), 0.0)
    pos = eig[eig > 1e-12]
    total = float(np.sum(pos))
    if total <= 0 or len(pos) < 2:
        return 0.0
    return float(pos[0] / total)


def gamma_min_trace(bridge, engine, center, gamma_mins):
    return float(np.min([g for g in gamma_mins if g is not None])) if any(g is not None for g in gamma_mins) else None


def run_amplitude(amplitude: float) -> dict[str, Any]:
    center = (16, 16, 16)
    engine = MasterEquationFDTD(N=32, dx=1.0, V_yield=1.0, c0=1.0, pml_thickness=4, A_cap=0.99, S_min=0.05)
    bridge = MasterFDTDPhasorBridge(nx=engine.N, ny=engine.N, nz=engine.N, dx=engine.dx, V_yield=engine.V_yield, dt=engine.dt)
    bridge.reset_phi_link()
    engine.inject_localized_blob(center=center, radius=SEED_RADIUS, amplitude=amplitude, profile="sech")

    center_trace: list[float] = []
    theta_trace: list[float] = []
    gamma_mins: list[float | None] = []
    a_peak_trace: list[float] = []

    cx, cy, cz = center
    x_plus = (cx + 1) % engine.N
    x_minus = (cx - 1) % engine.N

    for step in range(N_STEPS + 1):
        if step > 0:
            bridge.project_from_scalar(engine.V, engine.V_prev, accumulate_phi=True, S_min=engine.S_min)
        if step % CADENCE == 0:
            a_peak_trace.append(float(np.max(np.abs(engine.V)) / engine.V_yield))
            center_trace.append(float(engine.V[center]))
            v_i = float(bridge.V_inc[center].sum())
            v_r = float(bridge.V_ref[center].sum())
            theta_trace.append(float(math.atan2(v_r, v_i)))
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

    gamma_min = gamma_min_trace(bridge, engine, center, gamma_mins)
    eps_gamma = float(1.0 - gamma_min**2) if gamma_min is not None else None
    q_gamma = math.pi / eps_gamma if eps_gamma is not None and eps_gamma > 1e-15 else None

    shell = shell_mask(engine.V.shape, center, engine.V, bridge.mask_active, SHELL_RADIUS, STRAIN_THRESHOLD_FRAC)
    screened_var = screened_variance_2d(bridge.V_inc[shell], bridge.V_ref[shell])

    strain_plus = float(np.mean(np.abs(engine.V[x_plus, cy, cz])))
    strain_minus = float(np.mean(np.abs(engine.V[x_minus, cy, cz])))
    strain_asym = abs(strain_plus - strain_minus) / max(strain_plus + strain_minus, 1e-15)

    transient = max(3, len(theta_trace) // 5)
    dtheta = np.diff(theta_trace[transient:])
    twist_rate = float(np.mean(np.abs(dtheta))) if len(dtheta) > 0 else None
    torque_coupling = (twist_rate / strain_asym) if twist_rate is not None and strain_asym > 1e-15 else None

    L_vol, L_surf, L_line = q_factor_decomposition(engine.V, center, SEED_RADIUS)
    q_lambda = L_vol + L_surf + L_line

    return {
        "amplitude": amplitude,
        "A_peak_trace": float(max(a_peak_trace) if a_peak_trace else 0.0),
        "gamma_min": gamma_min,
        "eps_gamma": eps_gamma,
        "q_gamma": q_gamma,
        "screened_variance": screened_var,
        "screened_rms": math.sqrt(screened_var) if screened_var > 0 else 0.0,
        "strain_asymmetry": strain_asym,
        "twist_rate": twist_rate,
        "torque_coupling_ratio": torque_coupling,
        "q_lambda_sum": q_lambda,
        "alpha_used_as_input": False,
    }


def score_hypothesis(row: dict[str, Any]) -> dict[str, float | None]:
    alpha = float(ALPHA_COLD)
    scores: dict[str, float | None] = {}

    # H1 cage leak: epsilon should approach alpha (only meaningful when wall forms)
    scores["H1_cage_leak_eps_vs_alpha"] = log_rel_err(row.get("eps_gamma"), alpha)

    # H2 projector: screened variance ~ alpha or rms ~ sqrt(alpha)
    scores["H2_projector_var_vs_alpha"] = log_rel_err(row.get("screened_variance"), alpha)
    scores["H2_projector_rms_vs_sqrt_alpha"] = log_rel_err(row.get("screened_rms"), math.sqrt(alpha))

    # H3 torque coupling: twist/asym ~ alpha
    scores["H3_torque_coupling_vs_alpha"] = log_rel_err(row.get("torque_coupling_ratio"), alpha)

    # H4 four-pi scale on Q_gamma
    scores["H4_q_gamma_vs_four_pi"] = log_rel_err(row.get("q_gamma"), FOUR_PI)

    # H5 static geometry Q_lambda ~ 137
    scores["H5_q_lambda_vs_137"] = log_rel_err(row.get("q_lambda_sum"), float(ALPHA_COLD_INV))

    # H2 alt: half/quadrature (prior two-node negative)
    scores["H2_half_var"] = log_rel_err(row.get("screened_variance"), SCREENED_HALF)
    scores["H2_half_rms"] = log_rel_err(row.get("screened_rms"), SCREENED_RMS_HALF)

    return scores


def aggregate_scores(rows: list[dict[str, Any]]) -> dict[str, Any]:
    all_scores: list[dict[str, float | None]] = [score_hypothesis(r) for r in rows]
    keys = all_scores[0].keys() if all_scores else []
    means: dict[str, float | None] = {}
    for key in keys:
        vals = [s[key] for s in all_scores if s.get(key) is not None]
        means[key] = float(np.mean(vals)) if vals else None

    # Group into hypotheses (min mean log error per family)
    families = {
        "H1_cage_leak": ["H1_cage_leak_eps_vs_alpha"],
        "H2_projector_alpha": ["H2_projector_var_vs_alpha", "H2_projector_rms_vs_sqrt_alpha"],
        "H2_projector_half": ["H2_half_var", "H2_half_rms"],
        "H3_torque_coupling": ["H3_torque_coupling_vs_alpha"],
        "H4_four_pi": ["H4_q_gamma_vs_four_pi"],
        "H5_static_geometry": ["H5_q_lambda_vs_137"],
    }
    family_means = {}
    for fam, fam_keys in families.items():
        vals = [means[k] for k in fam_keys if means.get(k) is not None]
        family_means[fam] = float(np.min(vals)) if vals else None

    ranked = sorted(
        [(k, v) for k, v in family_means.items() if v is not None],
        key=lambda kv: kv[1],
    )

    # H1 monotonicity: eps should decrease as |gamma| increases toward 1
    eps_series = [(r["amplitude"], r["eps_gamma"]) for r in rows if r.get("eps_gamma") is not None]
    gamma_series = [(r["amplitude"], abs(r["gamma_min"])) for r in rows if r.get("gamma_min") is not None]
    h1_monotone_eps = all(
        eps_series[i][1] >= eps_series[i + 1][1] - 1e-9 for i in range(len(eps_series) - 1)
    ) if len(eps_series) >= 2 else False
    h1_monotone_gamma = all(
        gamma_series[i][1] <= gamma_series[i + 1][1] + 1e-9 for i in range(len(gamma_series) - 1)
    ) if len(gamma_series) >= 2 else False

    closest_alpha = min(
        ((r["amplitude"], abs(r["eps_gamma"] - float(ALPHA_COLD))) for r in rows if r.get("eps_gamma") is not None),
        key=lambda x: x[1],
        default=(None, None),
    )

    if ranked and ranked[0][0] == "H1_cage_leak" and h1_monotone_gamma:
        verdict = "CAGE_LEAK_MOST_LIKELY"
        outcome = "A"
    elif ranked and ranked[0][0] in ("H2_projector_alpha", "H3_torque_coupling"):
        verdict = "SHORT_TERM_IMAGE_SURVIVES"
        outcome = "B"
    elif ranked and ranked[0][0] == "H4_four_pi":
        verdict = "FOUR_PI_LOSS_SCALE"
        outcome = "C"
    elif ranked and ranked[0][0] == "H5_static_geometry":
        verdict = "STATIC_GEOMETRY_ONLY"
        outcome = "D"
    else:
        verdict = "DISCRIMINATOR_INCONCLUSIVE"
        outcome = "E"

    return {
        "family_mean_log10_rel_err": family_means,
        "ranked_families": ranked,
        "per_row_scores": all_scores,
        "h1_eps_monotone_decreasing": h1_monotone_eps,
        "h1_gamma_monotone_increasing": h1_monotone_gamma,
        "closest_eps_to_alpha": {"amplitude": closest_alpha[0], "abs_err": closest_alpha[1]},
        "verdict": verdict,
        "outcome": outcome,
        "interpretation": (
            "Lower mean log10 relative error = better match. H1 wins on mechanism if eps tracks 1-gamma^2 "
            "and approaches alpha only near full TIR. Short-term images = H2/H3."
        ),
    }


def main() -> None:
    verify_canonical_sources()
    rows = [run_amplitude(amp) for amp in AMPLITUDES]
    scoring = aggregate_scores(rows)
    payload = {
        "scope": "alpha-identity discriminator; comparison-only scoring",
        "amplitudes": AMPLITUDES,
        "rows": rows,
        "scoring": scoring,
        "comparison_only": {
            "alpha": float(ALPHA_COLD),
            "alpha_inv": float(ALPHA_COLD_INV),
            "four_pi": FOUR_PI,
            "screened_half": SCREENED_HALF,
        },
    }
    out_path = OUT_DIR / "alpha_identity_discriminator_results.json"
    out_path.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n")

    print("Alpha identity discriminator")
    print(f"  verdict: {scoring['verdict']} ({scoring['outcome']})")
    print(f"  ranked: {scoring['ranked_families'][:4]}")
    print(f"  closest eps to alpha: amp={scoring['closest_eps_to_alpha']['amplitude']} err={scoring['closest_eps_to_alpha']['abs_err']}")
    print(f"  H1 gamma monotone: {scoring['h1_gamma_monotone_increasing']}")
    for row in rows:
        print(
            f"  amp={row['amplitude']:.2f}  gamma={row['gamma_min']}  eps={row['eps_gamma']:.4f}"
            f"  screened_var={row['screened_variance']:.4f}  torque_k={row['torque_coupling_ratio']}"
        )
    print(f"  wrote: {out_path}")


if __name__ == "__main__":
    main()
