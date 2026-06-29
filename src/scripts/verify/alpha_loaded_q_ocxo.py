#!/usr/bin/env python3
"""
Open C — OCXO-style loaded-Q delta_strain at the electron Q-point.

PREREG: research/2026-06-25_alpha-loaded-q-ocxo_prereg.md

Treat delta_strain as fractional alpha shift at a self-biased loaded resonator
(boundary clock drift / environmental pull), NOT bulk BE occupancy at T_CMB.

Quartz EE analog:
  - Q-point bias before small-signal measurement
  - df/f from loaded C/L mismatch at boundary
  - TCF sets sign of T-running; magnitude tested per route

Routes L0-L2: bias-ladder / loaded-cap / loaded-Q (expect CONSISTENCY-class recovery).
Routes L3: BE thermal negative control (FT-1 class).
Routes L4-L5: forward rim-coupling hypotheses (no delta_strain input).

SCOPE NOTE (2026-06-25): CODATA delta_strain used ONLY for post-solve comparison.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

from ave.core.constants import (
    ALPHA,
    ALPHA_COLD,
    ALPHA_COLD_INV,
    DELTA_STRAIN,
    P_C,
    V_SNAP,
    V_YIELD,
)

# FT-1 closed-negative BE reference (control only)
ETA_EPS_FT1_BE = 2.2e-37
T_CMB = 2.725  # K, canonical CMB floor (delta-strain leaf)
T_MELT_K = 5.93e9  # m_e c^2 / k_B, Vol-9 canonical order

TARGET = DELTA_STRAIN


def _rel_err(pred: float, ref: float) -> float:
    if ref == 0:
        return float("inf")
    return abs(pred - ref) / abs(ref)


def route_l0_bias_ladder() -> dict:
    """Charge-port pressure ratio sqrt(alpha) pull (FORK-A)."""
    sqrt_cold = math.sqrt(ALPHA_COLD)
    sqrt_obs = math.sqrt(ALPHA)
    delta_sqrt_over_sqrt = (sqrt_obs - sqrt_cold) / sqrt_cold
    # alpha ~ leak rate; fractional shift from port bias: delta alpha/alpha ≈ 2 delta sqrt/sqrt
    delta_alpha_over_alpha = 2.0 * delta_sqrt_over_sqrt
    delta_alpha_inv = -delta_alpha_over_alpha  # alpha^-1 moves opposite
    return {
        "sqrt_alpha_cold": sqrt_cold,
        "sqrt_alpha_obs": sqrt_obs,
        "delta_sqrt_over_sqrt": delta_sqrt_over_sqrt,
        "delta_alpha_over_alpha_predicted": delta_alpha_over_alpha,
        "delta_alpha_inv_predicted": delta_alpha_inv,
        "delta_strain_target": TARGET,
        "relative_error": _rel_err(abs(delta_alpha_inv), TARGET),
        "verdict": "CONSISTENCY — bias-ladder tautology (FORK-A)",
    }


def route_l1_parallel_cap_load() -> dict:
    """Quartz parallel-load: C_ext/C_0 from charge-port alpha ratio."""
    c_ext_over_c0 = ALPHA_COLD / ALPHA - 1.0
    # Series LC: delta f/f ≈ -1/2 * delta C/C (fixed L).  alpha^-1 ~ f/Q, so
    # delta(alpha^-1)/alpha^-1 ≈ -delta f/f to leading order (Q fixed).
    delta_f_over_f = -0.5 * c_ext_over_c0
    denom = 1.0 + c_ext_over_c0
    delta_f_parallel = 0.5 * (c_ext_over_c0 / denom) if abs(denom) > 1e-30 else float("nan")
    # Map cap ratio to alpha^-1 shift (first order): 1 - alpha_cold/alpha = -C_ext/C_0
    delta_alpha_inv_from_cap = -c_ext_over_c0
    return {
        "C_ext_over_C_0": c_ext_over_c0,
        "delta_f_over_f_series": delta_f_over_f,
        "delta_f_over_f_parallel": delta_f_parallel,
        "delta_alpha_inv_from_cap_first_order": delta_alpha_inv_from_cap,
        "relative_error_cap_to_target": _rel_err(abs(delta_alpha_inv_from_cap), TARGET),
        "note": "|delta f/f| is half delta(alpha^-1)/alpha^-1 at leading order — not a miss",
        "verdict": "CONSISTENCY — cap ratio = 1 - alpha_cold/alpha = delta_strain",
    }


def route_l2_loaded_q_leak() -> dict:
    """Loaded-Q small-load limit: delta alpha/alpha ≈ Q_0/Q_ext (high-Q electron trap)."""
    q0 = ALPHA_COLD_INV
    sqrt_cold = math.sqrt(ALPHA_COLD)
    sqrt_obs = math.sqrt(ALPHA)
    delta_sqrt_over_sqrt = (sqrt_obs - sqrt_cold) / sqrt_cold
    delta_alpha_over_alpha = 2.0 * delta_sqrt_over_sqrt
    q_ext = q0 / delta_alpha_over_alpha if delta_alpha_over_alpha > 0 else float("inf")
    q_loaded = q0 / (1.0 + q0 / q_ext)
    alpha_eff_over_cold = q0 / q_loaded
    delta_alpha_inv = -(alpha_eff_over_cold - 1.0)
    return {
        "Q_0_cold": q0,
        "Q_ext_from_small_load_limit": q_ext,
        "Q_loaded": q_loaded,
        "alpha_eff_over_alpha_cold": alpha_eff_over_cold,
        "delta_alpha_inv_predicted": delta_alpha_inv,
        "relative_error": _rel_err(abs(delta_alpha_inv), TARGET),
        "verdict": "CONSISTENCY — small-load Q_ext equivalent to bias ladder",
    }


def route_l3_be_thermal_control() -> dict:
    """FT-1 class BE occupancy — negative control."""
    eta_eps = ETA_EPS_FT1_BE
    delta_alpha_inv = eta_eps / 2.0
    log10_miss = math.log10(abs(delta_alpha_inv) / TARGET) if delta_alpha_inv else float("inf")
    return {
        "eta_epsilon_BE": eta_eps,
        "delta_alpha_inv_predicted": delta_alpha_inv,
        "log10_miss_vs_target": log10_miss,
        "verdict": "CLOSED-NEGATIVE — bulk BE (same as FT-1)",
    }


def route_l4_rim_packing_alpha_cube() -> dict:
    """Forward: eta_epsilon = 8 pi alpha_cold^3 (packing x alpha^2 boundary coupling)."""
    eta = 8.0 * math.pi * ALPHA_COLD**3
    delta_alpha_inv = eta / 2.0
    err = _rel_err(delta_alpha_inv, TARGET)
    return {
        "eta_epsilon_forward": eta,
        "delta_alpha_inv_predicted": delta_alpha_inv,
        "relative_error": err,
        "factor_over_target": delta_alpha_inv / TARGET if TARGET else float("nan"),
        "f_boundary_to_close": TARGET / delta_alpha_inv if delta_alpha_inv else float("nan"),
        "verdict": f"PARTIAL — forward 8pi*alpha^3 overshoots by factor {delta_alpha_inv/TARGET:.2f}x",
    }


def route_l5_latent_floor() -> dict:
    """Forward: steady-state latent/rad ratio x packing x T_CMB/T_melt."""
    rho_latent_over_rad = 4.0 / 3.0  # 4H rho_rad = 3H rho_latent at injection floor
    p_cold = 8.0 * math.pi * ALPHA_COLD
    eta = rho_latent_over_rad * p_cold * (T_CMB / T_MELT_K)
    delta_alpha_inv = eta / 2.0
    err = _rel_err(delta_alpha_inv, TARGET)
    log10_miss = math.log10(abs(delta_alpha_inv) / TARGET) if delta_alpha_inv else float("inf")
    return {
        "rho_latent_over_rad": rho_latent_over_rad,
        "p_cold": p_cold,
        "T_CMB_over_T_melt": T_CMB / T_MELT_K,
        "eta_epsilon_forward": eta,
        "delta_alpha_inv_predicted": delta_alpha_inv,
        "log10_miss_vs_target": log10_miss,
        "verdict": "CLOSED-NEGATIVE — latent floor undershoots",
    }


def route_l6_packing_alpha_square() -> dict:
    """DUPLICATE of L4: p_cold * alpha^2 = 8*pi*alpha^3 identically."""
    p_cold = 8.0 * math.pi * ALPHA_COLD
    eta = p_cold * ALPHA_COLD**2
    eta_l4 = 8.0 * math.pi * ALPHA_COLD**3
    return {
        "eta_epsilon": eta,
        "duplicate_of_L4": abs(eta - eta_l4) < 1e-20 * max(abs(eta), 1.0),
        "verdict": "REDUNDANT — algebraically identical to L4 (p_cold = 8*pi*alpha)",
    }


def three_channel_qpoint_summary() -> dict:
    """Document Q-point rails (no fit)."""
    return {
        "V_snap_kV": V_SNAP / 1000.0,
        "V_yield_kV": V_YIELD / 1000.0,
        "V_yield_over_V_snap": V_YIELD / V_SNAP,
        "sqrt_alpha_CODATA": math.sqrt(ALPHA),
        "sqrt_alpha_cold": math.sqrt(ALPHA_COLD),
        "P_C_CODATA": P_C,
        "P_C_cold": 8.0 * math.pi * ALPHA_COLD,
        "note": "Charge port biased at sqrt(alpha)*V_snap; cold vs CODATA alpha is the load spec split",
    }


def audit_identities() -> dict:
    """Post-hoc algebraic cross-checks (not forward routes)."""
    p_cold = 8.0 * math.pi * ALPHA_COLD
    p_obs = 8.0 * math.pi * ALPHA
    ds_pack = 1.0 - p_cold / p_obs
    ds_alpha = 1.0 - ALPHA_COLD / ALPHA
    ds_sqrt = 2.0 * (math.sqrt(ALPHA) - math.sqrt(ALPHA_COLD)) / math.sqrt(ALPHA_COLD)
    return {
        "DELTA_STRAIN_constants": TARGET,
        "1_minus_alpha_cold_over_alpha": ds_alpha,
        "1_minus_p_cold_over_p_obs": ds_pack,
        "2_delta_sqrt_over_sqrt": ds_sqrt,
        "all_equal_to_machine_precision": (
            abs(ds_alpha - TARGET) < 1e-15
            and abs(ds_pack - TARGET) < 1e-15
            and abs(ds_sqrt - TARGET) / TARGET < 2e-6
        ),
        "note": "All are the same CODATA-vs-cold residual; not independent predictions",
    }


def overall_verdict(routes: dict) -> str:
    l0 = routes["L0_bias_ladder"]
    if l0["relative_error"] < 0.01:
        return (
            "CONSISTENCY-REFRAME — delta_strain = Q-point bias-ladder / loaded-spec "
            "mismatch (L0/L1/L2 tautology); forward L4 ~2.2x high; L3/L5 dead; L6 redundant"
        )
    return "OPEN — unexpected L0 mismatch"


def main() -> int:
    routes = {
        "L0_bias_ladder": route_l0_bias_ladder(),
        "L1_parallel_cap": route_l1_parallel_cap_load(),
        "L2_loaded_Q": route_l2_loaded_q_leak(),
        "L3_BE_control": route_l3_be_thermal_control(),
        "L4_rim_8pi_alpha3": route_l4_rim_packing_alpha_cube(),
        "L5_latent_floor": route_l5_latent_floor(),
        "L6_packing_alpha2": route_l6_packing_alpha_square(),
    }
    out = {
        "prereg": "research/2026-06-25_alpha-loaded-q-ocxo_prereg.md",
        "question": "OCXO-style loaded-Q boundary drift vs bulk BE at T_CMB",
        "delta_strain_target": TARGET,
        "audit_identities": audit_identities(),
        "qpoint": three_channel_qpoint_summary(),
        "routes": routes,
        "overall_verdict": overall_verdict(routes),
        "interpretation": {
            "sign_mechanism": "E hot / B frozen at T_CMB (Cosserat-Curie) — sign only",
            "magnitude_mechanism": (
                "2 ppm is bias-ladder / loaded-system specification (cold geometry vs CODATA "
                "in-situ port coupling), not bulk phonon occupancy at 2.7 K"
            ),
            "forward_work": "L4/L6 OOM bracket; need derived boundary participation fraction",
        },
    }

    text = json.dumps(out, indent=2)
    print(text)

    results_path = Path(__file__).with_name("alpha_loaded_q_ocxo_results.json")
    results_path.write_text(text + "\n", encoding="utf-8")
    print(f"\nwrote {results_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
