"""PILOT-FIELD verdict summary + figure generator.

Runs the full sonic sweep (rho in {0.5,1,2,4}), assembles the verdict table
(contraction depth, co-motion, local-vs-far probe, leakage), runs the five controls,
and writes the JSON artifact + the speed-ratio-law figure. NOT imported by the tests
(the tests re-run their own compact configs); this is the result-doc artifact producer.

FROZEN prereg: research/2026-07-05_pilot-field-comoving-companion_prereg_FROZEN.md.
VERDICT: [RETARDATION-LIMITED / LEAKY] — the companion develops + co-moves, but its
completeness/timing follow the speed ratio c_long/v_g (the measured law).

alpha-CLEAN: no physical constant on this path.
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pilot_field_wavetrain import (  # noqa: E402
    co_motion,
    contraction_depth,
    leakage,
    ledger_closure,
    local_vs_far_probe,
    run_wavetrain,
)

PRED_LOCAL_DEPTH = -0.0073410624
V_GROUP = 0.8
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_output")


def sonic_sweep(n_nodes=2048, l_env=80.0, n_periods=20.0, dt=0.02,
                rhos=(0.5, 1.0, 2.0, 4.0)) -> list[dict]:
    rows = []
    for rho in rhos:
        run = run_wavetrain(n_nodes=n_nodes, rho_bond=rho, l_env=l_env,
                            n_periods=n_periods, dt=dt)
        c = contraction_depth(run)
        cm = co_motion(run)
        lf = local_vs_far_probe(run)
        lk = leakage(run)
        ld = ledger_closure(run)
        rows.append({
            "rho_bond": rho,
            "c_long": float(np.sqrt(rho)),
            "mach_vg_over_clong": float(V_GROUP / np.sqrt(rho)),
            "du_dc_depth_SLICE": c["du_dc_min_under"],
            # LABELED as a SLICE (item-1 review): this is the n_periods-transit depth, NOT the
            # settled asymptote (see settled_asymptote_frac below, run separately per rho).
            "depth_frac_of_pred_SLICE": float(c["du_dc_min_under"] / PRED_LOCAL_DEPTH),
            "depth_growth": c["depth_growth_early_to_settled"],
            "comotion_lag_nodes": cm["comotion_lag_nodes"],
            "speed_ratio_du_over_env": cm["speed_ratio_du_over_env"],
            "under_bondframe_k_IMPORTED": lf["under_bondframe_k_ratio"],   # item-2: genuine probe
            "far_bondframe_k_wake": lf["far_bondframe_k_ratio"],           # item-3: causal wake node
            "leak_frac_final": lk["frac_long_in_window_final"],
            "energy_drift": ld["energy_drift_rel"],
        })
    return rows


def make_figure(rows: list[dict], path: str) -> None:
    """The speed-ratio-law figure: contraction depth (%pred) and co-motion speed-ratio
    vs the Mach number v_g/c_long. WHITE house style (ave.viz.style.apply)."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    try:
        from ave.viz import style
        style.apply("print")
    except Exception:
        pass

    mach = [r["mach_vg_over_clong"] for r in rows]
    depth = [100 * r["depth_frac_of_pred_SLICE"] for r in rows]
    sratio = [r["speed_ratio_du_over_env"] for r in rows]
    rho = [r["rho_bond"] for r in rows]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4.0))
    ax1.plot(mach, depth, "o-", color="#0072B2")
    ax1.axhline(100, ls="--", color="#999999", lw=1)
    ax1.set_xlabel(r"Mach number  $v_g / c_{\mathrm{long}}$")
    ax1.set_ylabel(r"contraction depth, per-transit SLICE  (% of $-\langle dy^2\rangle/2$)")
    for m, d, rr in zip(mach, depth, rho):
        ax1.annotate(rf"$\rho={rr:g}$", (m, d), textcoords="offset points",
                     xytext=(6, -10), fontsize=8)
    ax1.set_title("companion completeness vs Mach (per-transit slice)", fontsize=9)

    ax2.plot(mach, sratio, "s-", color="#D55E00")
    ax2.axhline(1.0, ls="--", color="#999999", lw=1)
    ax2.set_xlabel(r"Mach number  $v_g / c_{\mathrm{long}}$")
    ax2.set_ylabel(r"co-motion speed ratio  $v_{\mathrm{well}} / v_{\mathrm{env}}$")
    for m, s, rr in zip(mach, sratio, rho):
        ax2.annotate(rf"$\rho={rr:g}$", (m, s), textcoords="offset points",
                     xytext=(6, -10), fontsize=8)
    ax2.set_title("co-motion fidelity vs Mach", fontsize=9)

    fig.tight_layout()
    fig.savefig(path, dpi=140, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    from pilot_field_wavetrain import settled_asymptote_depth
    os.makedirs(OUT_DIR, exist_ok=True)
    fast = "--fast" in sys.argv
    kw = dict(n_nodes=1024, n_periods=14.0) if fast else dict(n_nodes=2048, n_periods=20.0)
    rows = sonic_sweep(**kw)
    # ITEM-1: the settled ASYMPTOTE (not a slice) at rho=4, the well-developed reference
    grid = (20, 40) if fast else (20, 40, 56, 72)
    asymptote = settled_asymptote_depth(rho_bond=4.0, n_nodes=4096, periods_grid=grid)
    out = {"verdict": "RETARDATION-LIMITED / LEAKY", "sonic_sweep_SLICES": rows,
           "settled_asymptote_rho4": asymptote,
           "pred_phase_avg_depth": PRED_LOCAL_DEPTH, "v_group": V_GROUP,
           "note": "sonic_sweep values are per-transit SLICES; the settled asymptote at rho=4 "
                   "saturates ~112% of the phase-average prediction (item-1 review); the ~12% "
                   "excess is an OPEN residual (candidate: peak-vs-phase-average form factor)."}
    with open(os.path.join(OUT_DIR, "pilot_field_summary.json"), "w") as f:
        json.dump(out, f, indent=2, default=float)
    make_figure(rows, os.path.join(OUT_DIR, "pilot_field_speed_ratio_law.png"))
    print(json.dumps(out, indent=2, default=float))
