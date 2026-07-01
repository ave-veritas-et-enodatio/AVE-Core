"""run_electron_bind_sim — the banked sweep suite for the result doc.

FROZEN PRE-REG: research/2026-06-30_electron-bind-sim_prereg_FROZEN.md (commit f678b0fc).
Runs, at >=2 resolutions (resolution-robustness): the fixed-Q pull sweep, the winding-loop
brace sweep, the L_w circulation-conservation trace, and the alpha-robustness sweep.
Writes research/drivers/electron_bind_sim_results.json (raw, for the result doc).

Every run is on the UNITARY lossless solver (NO dissipative term) — |dH/H| banked as the
Tellegen certificate. Class-C: alpha/A=sqrt(alpha)/m_e imported/echo, NOT claimed.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from electron_bind_sim import (  # noqa: E402
    A_STAR,
    ALPHA,
    CoupledCageWinding,
    CoupledCageWindingConfig,
    _radii,
    envelope_radius_sweep,
    measure_L_w,
    winding_loop_radius_sweep,
)


def Lw_conservation_trace(N: int, *, n_steps: int = 40, dt: float = 0.05) -> dict:
    """Does the winding circulation angular momentum L_w stay CONSTANT under lossless
    evolution? (the derivation §3.1 brace premise). Reports |L_w|(t), the topological
    winding integer (conserved by construction), and |dH/H| (lossless). If |L_w| DRIFTS
    while the Link is conserved and energy is conserved, the r^{-3} brace's `L_w=const`
    premise is NOT satisfied by the engine — prereg criterion N4 territory."""
    cfg = CoupledCageWindingConfig(N=N, V_yield=1.0, dt=dt, R=7.0, r=2.3, winding_on=True,
                                   winding_mode="rigid_template", port_sigma=0.0)
    sim = CoupledCageWinding(cfg)
    sim.seed_A1_sech(amplitude=A_STAR, radius=3.0)
    sim.seed_winding(amplitude=0.5)
    c = N // 2
    i, j, k = np.indices((N, N, N))
    pos = np.stack([(i - c), (j - c), (k - c)], axis=-1) * cfg.dx

    def angmom():
        L = np.cross(pos, sim.omega_field())
        return float(np.linalg.norm(L[sim.interior].sum(axis=0)))

    L0 = angmom()
    q0 = sim.winding_integer()
    H0 = sim.total_energy()
    series = [{"step": 0, "L_w": L0, "Q_link": q0["Q_link"], "dH_over_H": 0.0}]
    for n in range(1, n_steps + 1):
        sim.step()
        if n % 5 == 0 or n == n_steps:
            q = sim.winding_integer()
            series.append({
                "step": n, "L_w": angmom(), "Q_link": q["Q_link"],
                "dH_over_H": float(abs(sim.total_energy() - H0) / max(abs(H0), 1e-30)),
            })
    L_final = series[-1]["L_w"]
    return {
        "N": N, "L_w_seed": L0, "L_w_final": L_final,
        "L_w_drift_frac": float(abs(L_final - L0) / max(abs(L0), 1e-30)),
        "topological_link_conserved": all(s["Q_link"] == q0["Q_link"] for s in series),
        "max_dH_over_H": max(s["dH_over_H"] for s in series),
        "series": series,
    }


def saturation_dynamic_range(N: int) -> dict:
    """At A=sqrt(alpha), how much does S(A) vary across the core? The ponderomotive pull
    p is the slope of a potential ∝ S(A(r)); if S is flat (S-range ~ 0), there is NO
    measurable pull slope — the varactor nonlinearity is ~OFF at the sub-saturated point.
    This is the resolution-robust root-cause diagnostic."""
    cfg = CoupledCageWindingConfig(N=N, V_yield=1.0, dt=0.05, R=7.0, r=2.3, winding_on=True,
                                   winding_mode="rigid_template", port_sigma=0.0)
    sim = CoupledCageWinding(cfg)
    sim.seed_A1_sech(amplitude=A_STAR, radius=3.0)
    sim.seed_winding(amplitude=0.5)
    S = sim.saturation_S()
    Smin, Smax = float(S[sim.interior].min()), float(S[sim.interior].max())
    return {
        "N": N, "S_min": Smin, "S_max": Smax,
        "S_range_frac": float((Smax - Smin) / Smax),
        "coupling_Omega_max": float(sim.coupling_Omega().max()),
        "front_gate_at_A_star": float(np.exp(-((A_STAR - 4 / 7) ** 2) / (2 * 0.18 ** 2))),
        "S_at_A_star": float(np.sqrt(1 - A_STAR ** 2)),
    }


def main() -> None:
    out: dict = {"alpha": ALPHA, "A_star": A_STAR, "resolutions": [24, 32]}
    r_envs = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
    loop_rs = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0]

    out["saturation_dynamic_range"] = [saturation_dynamic_range(N) for N in (24, 32)]
    out["Lw_conservation"] = [Lw_conservation_trace(N) for N in (24, 32)]

    # ── fixed-Q pull sweep (derivation §3.4 model) at 2 resolutions ──
    out["pull_sweep_fixedQ"] = {}
    for N in (24, 32):
        res = envelope_radius_sweep(r_envs, N=N, n_settle=12, n_window=20, Q_fixed=200.0)
        res.pop("rows", None)
        out["pull_sweep_fixedQ"][str(N)] = res

    # ── operating-point-fixed pull sweep (the Q-grows read; kept for contrast) ──
    out["pull_sweep_Aop_fixed"] = {}
    for N in (24, 32):
        res = envelope_radius_sweep(r_envs, N=N, n_settle=12, n_window=20, Q_fixed=None)
        res.pop("rows", None)
        out["pull_sweep_Aop_fixed"][str(N)] = res

    # ── brace in its coordinate (winding-loop radius) at 2 resolutions ──
    out["brace_loop_sweep"] = {}
    for N in (24, 32):
        b = winding_loop_radius_sweep(loop_rs, N=N, n_settle=10)
        b.pop("rows", None)
        out["brace_loop_sweep"][str(N)] = b

    # ── alpha-robustness (the keystone test): vary alpha ⇒ A=sqrt(alpha) slides ──
    alphas = [ALPHA / 4, ALPHA / 2, ALPHA, 2 * ALPHA, 4 * ALPHA]
    out["alpha_robustness"] = []
    for a in alphas:
        A_op = float(np.sqrt(a))
        # pull dynamic range at this operating point (does the pull ever get teeth?)
        cfg = CoupledCageWindingConfig(N=28, V_yield=1.0, dt=0.05, R=7.0, r=2.3,
                                       winding_on=True, winding_mode="rigid_template",
                                       port_sigma=0.0)
        sim = CoupledCageWinding(cfg)
        sim.seed_A1_sech(amplitude=A_op, radius=3.0)
        sim.seed_winding(amplitude=0.5)
        S = sim.saturation_S()
        res = envelope_radius_sweep([2.0, 2.5, 3.0, 3.5, 4.0], N=28, n_settle=10,
                                    n_window=16, A_op=A_op, Q_fixed=200.0)
        res.pop("rows", None)
        out["alpha_robustness"].append({
            "alpha_eff": a, "A_op": A_op,
            "S_min": float(S[sim.interior].min()), "S_max": float(S[sim.interior].max()),
            "S_range_frac": float((S[sim.interior].max() - S[sim.interior].min())
                                  / S[sim.interior].max()),
            "pull_slope_p": res["pull_slope_p"], "pull_r2": res["pull_r2"],
            "U_pond_slope": res["U_pond_slope"], "U_pond_r2": res["U_pond_r2"],
            "three_minus_p": res["three_minus_p"], "stable_sign": res["stable"],
            "max_dH_over_H": res["max_dH_over_H"],
        })

    dest = Path(__file__).parent / "electron_bind_sim_results.json"
    dest.write_text(json.dumps(out, indent=2))
    print(f"wrote {dest}")

    # ── console summary ──
    print("\n=== SATURATION DYNAMIC RANGE (root cause) ===")
    for d in out["saturation_dynamic_range"]:
        print(f"  N={d['N']}: S in [{d['S_min']:.5f},{d['S_max']:.5f}] "
              f"range={d['S_range_frac']:.2e}  front_gate(A*)={d['front_gate_at_A_star']:.4f}")
    print("\n=== L_w CONSERVATION ===")
    for d in out["Lw_conservation"]:
        print(f"  N={d['N']}: |L_w| {d['L_w_seed']:.2f} -> {d['L_w_final']:.2f} "
              f"(drift {d['L_w_drift_frac']:.1%})  Link_conserved={d['topological_link_conserved']}  "
              f"|dH/H|={d['max_dH_over_H']:.1e}")
    print("\n=== FIXED-Q PULL SLOPE p (resolution-robust?) ===")
    for N in ("24", "32"):
        r = out["pull_sweep_fixedQ"][N]
        print(f"  N={N}: p={r['pull_slope_p']:.3f} (r2={r['pull_r2']:.3f})  "
              f"U_pond_slope={r['U_pond_slope']:.3f} (r2={r['U_pond_r2']:.3f})  stable={r['stable']}")
    print("\n=== BRACE SLOPE (winding-loop coordinate) ===")
    for N in ("24", "32"):
        b = out["brace_loop_sweep"][N]
        print(f"  N={N}: brace b={b['brace_slope_b']:.3f} (r2={b['brace_r2']:.3f})  "
              f"U_rot_slope={b['U_rot_slope']:.3f} (r2={b['U_rot_r2']:.3f})")
    print("\n=== ALPHA ROBUSTNESS (S-range across the operating points) ===")
    for a in out["alpha_robustness"]:
        print(f"  alpha={a['alpha_eff']:.5f} A_op={a['A_op']:.4f}: S-range={a['S_range_frac']:.2e}  "
              f"p={a['pull_slope_p']:.3f} (r2={a['pull_r2']:.3f})")


if __name__ == "__main__":
    main()
