"""Production run of the ELECTRON-LOCK RECONNECTION-BARRIER test (pre-reg 2026-07-08).

ONE blocking run at the production scale (N=24). Writes the results JSON and the
house-white figure. NO polling; NO pumping; unitary evolver only.

  python src/scripts/vol_2_particle_physics/electron_lock_barrier_run.py

Outputs:
  results/electron_lock_barrier_results.json
  research/figures/2026-07-08-electron-lock-barrier/electron_lock_barrier.{png,pdf}
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from ave.solvers.electron_lock_barrier import (
    BarrierConfig,
    measure_barrier,
    run_electron_lock_barrier,
)

# ── ave-canonical-source cross-check: constants import cleanly; they enter ONLY as
# off-path scale anchors (the AST firewall proves no α/m_e on the verdict path). ──
import ave.core.constants as _c  # noqa: E402

_OFF_PATH_ANCHORS = {"E_YIELD": float(_c.E_YIELD)}  # documented off-path anchor


def _verify_constants() -> dict:
    """No hardcoded physics value on the verdict path; constants import from the
    canonical module. The firewall (in the driver) asserts no α/m_e NAME token."""
    return {
        "constants_module": _c.__file__,
        "off_path_anchors": _OFF_PATH_ANCHORS,
        "note": "verdict observable is a pure arg(); constants are OFF the verdict path",
    }


def make_figure(res: dict, bc: BarrierConfig, out_dir: Path) -> list[Path]:
    import ave.viz.style as style

    style.apply("print")
    plt = style.plt
    C = style.COLORS

    fig, axes = plt.subplots(1, 3, figsize=(12.5, 3.7), constrained_layout=True)

    # ── Panel A: the DECISIVE detuning kill-gate ──
    axA = axes[0]
    a3 = res["arm3_detuning_killgate"]
    series = [
        ("rigid wall-OFF (#417 ref)", a3["rigid_wall_off_reference"]["rows"], C["muted"], "o"),
        ("rigid wall-ON (confined)", a3["rigid_wall_on"]["rows"], C["ave"], "s"),
        ("dispersive wall-ON", a3["rows"], C["accent"], "^"),
    ]
    for label, rows, col, mk in series:
        x = [r["carrier_ratio"] for r in rows]
        y = [r["winding_ratio"] for r in rows]
        order = np.argsort(x)
        x = np.array(x)[order]
        y = np.array(y)[order]
        axA.plot(x, y, mk, color=col, label=label, ms=6)
        sl, ic = np.polyfit(x, y, 1)
        xf = np.linspace(min(x), max(x), 20)
        axA.plot(xf, sl * xf + ic, "-", color=col, lw=1.0, alpha=0.7)
    xr = np.linspace(0.5, 1.5, 20)
    axA.plot(xr, xr, "k--", lw=0.9, alpha=0.5, label="perfect echo (y=x)")
    axA.axhline(2.0 / 3.0, color="k", ls=":", lw=0.9, alpha=0.5,
                label="topological pin (flat)")
    axA.set_xlabel(style.axis_label("carrier ratio", r"\omega_b/\omega_s", ""))
    axA.set_ylabel(style.axis_label("winding ratio", r"\Delta\varphi/\Delta\psi", ""))
    style.legend(axA, where="right", fontsize=6)

    # ── Panel B: the BARRIER homotopy (no barrier vs synthetic-PROTECTED) ──
    axB = axes[1]
    a4 = res["arm4_barrier"]
    lam = np.array(a4["lambda"])
    H = np.array(a4["H_conf"])
    axB.plot(lam, H - H[0], "-o", color=C["ave"], ms=4, label="confined (measured)")
    # synthetic-barrier contrast (bin-liveness: PROTECTED reachable) — OFF verdict path
    syn = measure_barrier(bc, wall_form=bc.wall_form, clamp_strength=bc.clamp_strength,
                          budget=a4["budget"], synthetic_barrier=abs(H[0]) * 3.0 + 1.0)
    Hs = np.array(syn["H_conf"])
    axB.plot(lam, Hs - Hs[0], "--", color=C["comparison"], lw=1.2,
             label="synthetic barrier (control)")
    axB.axhline(a4["budget"], color=C["accent"], ls=":", lw=1.0,
                label=f"budget = {a4['budget']:.2g}")
    axB.axhline(0.0, color="k", lw=0.6, alpha=0.4)
    axB.set_xlabel(style.axis_label("forced unwind", r"\lambda", "wound->unwound"))
    axB.set_ylabel(style.axis_label("confinement energy climb", r"\Delta H_{\rm conf}", "engine units"))
    style.legend(axB, where="right", fontsize=6)

    # ── Panel C: real-space winding decay (free vs confined) ──
    axC = axes[2]
    a1 = res["arm1_liveness"]
    a2 = res["arm2_hold"]
    axC.plot(a1["q_raw_steps"], np.abs(a1["q_raw"]), "-o", color=C["muted"], ms=3,
             label="Arm 1 free (wall OFF)")
    axC.plot(a2["q_raw_steps"], np.abs(a2["q_raw"]), "-s", color=C["ave"], ms=3,
             label="Arm 2 confined (wall ON)")
    axC.axhline(3.0, color="k", ls=":", lw=0.9, alpha=0.5, label="seeded (2,3): |Q|=3")
    axC.set_xlabel(style.axis_label("time", "n", "steps"))
    axC.set_ylabel(style.axis_label("real-space winding", r"|Q_{\rm link,raw}|", ""))
    style.legend(axC, where="right", fontsize=6)

    out_dir.mkdir(parents=True, exist_ok=True)
    return style.save(fig, out_dir / "electron_lock_barrier")


def main() -> None:
    repo = Path(__file__).resolve().parents[3]
    bc = BarrierConfig()  # production: N=24, R=7, r=2.3, 300/200 steps, K=30
    res = run_electron_lock_barrier(bc)
    res["verify_constants"] = _verify_constants()

    results_path = repo / "results" / "electron_lock_barrier_results.json"
    results_path.write_text(json.dumps(res, indent=2))

    fig_dir = repo / "research" / "figures" / "2026-07-08-electron-lock-barrier"
    figs = make_figure(res, bc, fig_dir)

    print("=" * 72)
    print("ELECTRON-LOCK RECONNECTION-BARRIER — VERDICT:", res["verdict"])
    print("REASON:", res["reason"])
    print("-" * 72)
    a3 = res["arm3_detuning_killgate"]
    print("Arm 3 DECISIVE detuning kill-gate (phase-space, reconnection-capable primary):")
    print("  classification:", a3["classification"],
          "| correlation:", round(a3["correlation"], 3),
          "| slope:", round(a3["slope"], 3))
    for r in a3["rows"]:
        print(f"    omega_b:omega_s = {r['omega_b']}:{r['omega_s']}  carrier={r['carrier_ratio']:.3f}"
              f"  winding_ratio={r['winding_ratio']:.3f}")
    print("  rigid wall-OFF:", a3["rigid_wall_off_reference"]["classification"],
          "corr", round(a3["rigid_wall_off_reference"]["correlation"], 3),
          "| rigid wall-ON:", a3["rigid_wall_on"]["classification"],
          "corr", round(a3["rigid_wall_on"]["correlation"], 3))
    a4 = res["arm4_barrier"]
    print(f"Arm 4 barrier: height={a4['barrier_height']:.4g}  budget={a4['budget']:.4g}"
          f"  barrier>budget={a4['barrier_gt_budget']}  downhill={a4['downhill']}")
    print("Arm 1 open:", res["arm1_liveness"]["channel_open"],
          "| Arm 2 holds:", res["arm2_hold"]["holds"])
    g = res["gates"]
    print("GATES: firewall_clean=", g["firewall"]["clean"],
          "| energy_all<1e-5=", g["energy_conservation"]["all_below_1e-5"],
          "| scale_invariant=", g["scale_invariance"]["scale_invariant"],
          "| bins_reachable=", all(g["bin_liveness"].values()),
          "| detuning_can_fire=", g["detuning_can_fire"]["can_report_tracks"]
          and g["detuning_can_fire"]["can_report_pinned"])
    print("locus_disagreement:", res["locus_disagreement"])
    print("-" * 72)
    print("results:", results_path)
    for f in figs:
        print("figure :", f)


if __name__ == "__main__":
    main()
