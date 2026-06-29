#!/usr/bin/env python3
"""
Open D — forward boundary participation f_b for delta_strain magnitude.

PREREG: research/2026-06-25_f-boundary-participation_prereg.md

Forward chain (no CODATA delta on verdict path):
  eta_epsilon = f_b * 8 * pi * alpha_cold^3
  delta_pred  = eta_epsilon / 2

f_b candidates are geometry / DOF-count only (see prereg table).
DELTA_STRAIN and ALPHA (CODATA) used ONLY post-solve for comparison.

SCOPE NOTE (2026-06-25): alpha_cold appears in the coupling kernel 8*pi*alpha^3
by design (Open C L4 bracket); f_b itself must not import alpha_obs or delta_strain.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

from ave.core.constants import ALPHA, ALPHA_COLD, DELTA_STRAIN

PHI = (1.0 + math.sqrt(5.0)) / 2.0
RR_GOLDEN = (PHI / 2.0) * ((PHI - 1.0) / 2.0)  # R·r = 1/4
R_SEC = 1.187  # r_secondary / ell_node, Vol-3 / Q-G47 canonical
Z0_AMORPH = 51.25  # FTG-EMT effective coordination at operating point
ETA_BE_FT1 = 2.2e-37

TARGET = DELTA_STRAIN
KAPPA = 8.0 * math.pi * ALPHA_COLD**3  # forward coupling kernel


def _pred(f_b: float) -> float:
    return f_b * KAPPA / 2.0


def _score(delta_pred: float) -> dict:
    if TARGET == 0:
        return {"relative_error": float("inf"), "log10_miss": float("inf"), "factor": float("inf")}
    rel = abs(delta_pred - TARGET) / abs(TARGET)
    factor = delta_pred / TARGET if TARGET else float("inf")
    log10 = math.log10(abs(delta_pred) / abs(TARGET)) if delta_pred else float("-inf")
    return {"relative_error": rel, "log10_miss": log10, "factor_over_target": factor}


def _route(route_id: str, f_b: float, rationale: str, *, circular: bool = False) -> dict:
    delta_pred = _pred(f_b)
    sc = _score(delta_pred)
    if circular:
        verdict = "TAUTOLOGY / CIRCULAR"
    elif sc["relative_error"] <= 0.10:
        verdict = "NEAR-HIT (<10%) — audit for hidden alpha import"
    elif sc["relative_error"] <= 0.50:
        verdict = "PARTIAL (<50%)"
    elif abs(sc["log10_miss"]) <= 0.35:  # ~2.2x band
        verdict = "OOM-BRACKET (~2x)"
    elif sc["log10_miss"] < -1:
        verdict = "CLOSED-NEGATIVE (undershoot)"
    else:
        verdict = f"MISS ({sc['relative_error']:.2f}x rel err)"
    return {
        "route_id": route_id,
        "f_b": f_b,
        "rationale": rationale,
        "eta_epsilon": f_b * KAPPA,
        "delta_strain_predicted": delta_pred,
        **sc,
        "verdict": verdict,
    }


def geometry_routes() -> dict[str, dict]:
    pi = math.pi
    routes = {
        "G1_E_dof_fraction": _route(
            "G1",
            3.0 / 6.0,
            "Cosserat E-mode fraction (3 stretch / 6 total DOFs per node)",
        ),
        "G2_exterior_E": _route(
            "G2",
            (3.0 / 6.0) * 0.5,
            "E modes × exterior-facing half of Γ boundary (interior sealed)",
        ),
        "G3_shared_bond_half": _route(
            "G3",
            0.5,
            "K4 bond shared between two cells — half ownership at boundary",
        ),
        "G4_Rr_quarter": _route(
            "G4",
            RR_GOLDEN,
            "Golden Torus R·r = 1/4 Nyquist identification (Q-EMBED-SEL-1)",
        ),
        "G5_four_over_pi_sq": _route(
            "G5",
            4.0 / pi**2,
            "Geometric 4/π² scale (tube/face area ratio order)",
        ),
        "G6_inv_two_phi": _route(
            "G6",
            1.0 / (2.0 * PHI),
            "1/(2φ) from Golden Torus minor radius r = (φ−1)/2",
        ),
        "G7_phi_minus_one": _route(
            "G7",
            PHI - 1.0,
            "φ−1 = 1/φ inverse golden ratio",
        ),
        "G8_E_times_tube_correction": _route(
            "G8",
            (3.0 / 6.0) * (1.0 - 1.0 / (2.0 * pi)),
            "E fraction × (1 − 1/(2π)) tube circumference correction",
        ),
        "G9_secondary_link_area": _route(
            "G9",
            min(1.0, 1.0 / R_SEC**2),
            f"(ℓ_node/r_sec)² with r_sec={R_SEC} ℓ_node, capped at 1",
        ),
        "G10_bondpair_over_z0": _route(
            "G10",
            2.0 / Z0_AMORPH,
            "Two-node bond-pair vs amorphous z₀=51.25 coordination",
        ),
        "G11_two_node_quadrature": _route(
            "G11",
            0.5,
            "Two-node complete projector screened variance (phase space; 68×α — wrong sector)",
        ),
        "G12_half_direct": _route(
            "G12",
            0.5,
            "Direct 1/2 hypothesis: half of boundary channels participate in env load",
        ),
    }
    return routes


def control_routes() -> dict[str, dict]:
    f_req = TARGET / (4.0 * math.pi * ALPHA_COLD**3) if KAPPA else float("nan")
    return {
        "I0_inversion": _route(
            "I0",
            f_req,
            "f_b = δ_target / (4πα_cold³) — definitional inversion",
            circular=True,
        ),
        "I1_alpha_in_f_b": _route(
            "I1",
            ALPHA_COLD,
            "f_b = α_cold — circular (α inside participation fraction)",
            circular=True,
        ),
        "I2_BE_control": {
            "route_id": "I2",
            "f_b": None,
            "rationale": "FT-1 BE thermal η_ε control (no f_b)",
            "eta_epsilon": ETA_BE_FT1,
            "delta_strain_predicted": ETA_BE_FT1 / 2.0,
            **_score(ETA_BE_FT1 / 2.0),
            "verdict": "CLOSED-NEGATIVE — bulk BE",
        },
    }


def unknot_geometry_audit() -> dict:
    """Real-space 0_1 unknot dimensions from electron-identification §1."""
    r_tube = 1.0 / (2.0 * math.pi)  # in ℓ_node; tube circumference = ℓ_node
    r_loop = 1.0  # loop length 2π ℓ_node → R_major = ℓ_node
    a_nyquist = 1.0  # face ℓ_node²
    a_tube_xsect = math.pi * r_tube**2
    f_area = a_tube_xsect / a_nyquist  # = 1/(4π)
    torus_surface_approx = 4.0 * math.pi**2 * r_loop * r_tube  # 2π² ℓ_node²
    return {
        "r_tube_over_ell_node": r_tube,
        "r_loop_over_ell_node": r_loop,
        "tube_cross_section_over_nyquist_face": f_area,
        "torus_surface_over_nyquist_face": torus_surface_approx,
        "note": "From electron-identification §1: tube circ ℓ_node, loop 2πℓ_node",
    }


def pick_best_forward(forward: dict[str, dict]) -> dict:
    eligible = [v for v in forward.values() if "CIRCULAR" not in v.get("verdict", "")]
    if not eligible:
        return {}
    best = min(eligible, key=lambda x: x["relative_error"])
    return best


def overall_verdict(forward: dict[str, dict], controls: dict[str, dict]) -> str:
    best = pick_best_forward(forward)
    if not best:
        return "CLOSED-NEGATIVE — no forward routes"
    rel = best["relative_error"]
    rid = best["route_id"]
    if rel <= 0.10:
        return (
            f"PARTIAL-NEAR-HIT — {rid} within 10%; "
            "not CHORD until unique f_b selector (I0=0.455 still tautology)"
        )
    if rel <= 0.50:
        return f"PARTIAL — best forward {rid} within 50% (factor {best['factor_over_target']:.2f})"
    if abs(best.get("log10_miss", 99)) <= 0.35:
        return f"OOM-BRACKET — best forward {rid} ~2× (factor {best['factor_over_target']:.2f})"
    return f"CLOSED-NEGATIVE — best forward {rid} misses by {rel:.1f}x"


def main() -> int:
    forward = geometry_routes()
    controls = control_routes()
    best = pick_best_forward(forward)

    out = {
        "prereg": "research/2026-06-25_f-boundary-participation_prereg.md",
        "coupling_kernel_kappa": KAPPA,
        "delta_strain_target_post_solve": TARGET,
        "alpha_cold": ALPHA_COLD,
        "alpha_codata_comparison_only": ALPHA,
        "unknot_geometry": unknot_geometry_audit(),
        "forward_routes": forward,
        "controls": controls,
        "best_forward": best,
        "f_b_required_for_exact_match": TARGET / (4.0 * math.pi * ALPHA_COLD**3),
        "overall_verdict": overall_verdict(forward, controls),
        "interpretation": {
            "G2_vs_target_factor": forward["G2_exterior_E"]["factor_over_target"],
            "G12_vs_target_factor": forward["G12_half_direct"]["factor_over_target"],
            "honest_read": (
                "If best forward is ~10% high with f_b=1/2 or 1/4, geometry brackets "
                "δ_strain but does not close without a second underived factor"
            ),
        },
    }

    text = json.dumps(out, indent=2)
    print(text)
    out_path = Path(__file__).with_name("f_boundary_participation_results.json")
    out_path.write_text(text + "\n", encoding="utf-8")
    print(f"\nwrote {out_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
