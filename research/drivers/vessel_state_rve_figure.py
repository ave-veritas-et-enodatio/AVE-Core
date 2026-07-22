#!/usr/bin/env python3
"""White-house-style figure for the vessel-state RVE bench (walk-1 verdict run).

Reads the shipped `vessel_state_rve_results.json` and plots:
  (L) the sign-resolved AMPLITUDE GATE — K_tan_central / K_tan_plus / K_tan_minus vs
      ε_probe for the headline grown arm (the gate reads outcome (i) clean when the
      three curves stay flat and coincident; (iii) marginality when plus/minus split).
  (R) the C-V profile K(ε_bias) — small-signal tangent vs quasi-static strain bias.

House style: ave.viz.style.apply (Okabe-Ito, white, honest axes/units, legend outside
data, no on-figure title). Engine byte-untouched (reads JSON only).

Run: PYTHONPATH=src python3 research/drivers/vessel_state_rve_figure.py
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from ave.viz import style  # noqa: E402


def main():
    here = Path(__file__).resolve().parent
    d = json.loads((here / "vessel_state_rve_results.json").read_text())
    v = d["verdict"]
    head = v["fixed_budget_headline"]
    gate = head["amplitude_gate"]
    cv = v.get("cv_profile_fixed_budget", {})

    style.apply()
    C = style.COLORS
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(10.6, 4.3))

    # (L) amplitude gate: central / plus / minus vs eps_probe
    eps = [s["eps"] for s in gate["scan"]]
    kc = [s["k_tan_central"] for s in gate["scan"]]
    kp = [s["k_tan_plus"] for s in gate["scan"]]
    km = [s["k_tan_minus"] for s in gate["scan"]]
    axL.plot(eps, kc, "o-", color=C["ave"], ms=6, label="K_tan_central (verdict)")
    axL.plot(eps, kp, "s--", color=C["accent"], ms=5, mfc="none", label="K_tan_plus (stretch)")
    axL.plot(eps, km, "^:", color=C["comparison"], ms=5, mfc="none", label="K_tan_minus (squeeze)")
    axL.set_xscale("log")
    axL.set_xlabel("probe amplitude  ε_probe  (dimensionless strain)")
    axL.set_ylabel("K_tan  (core energy 2nd difference ÷ ε², arb.)")
    axL.annotate("outcome (%s):  A_sign=%.3g,  amp_spread±=%.2g/%.2g"
                 % (gate["outcome"], gate["A_sign"], gate["amp_spread_plus"],
                    gate["amp_spread_minus"]),
                 xy=(0.03, 0.03), xycoords="axes fraction", fontsize=7, color=C["muted"])
    axL.legend(loc="best", fontsize=7, frameon=False)

    # (R) C-V profile
    if cv:
        eb = cv["eps_bias"]
        K = cv["K_of_eps_bias"]
        axR.plot(eb, K, "o-", color=C["ave"], ms=6, label="K(ε_bias)  small-signal tangent")
        axR.axvline(cv["shell_POSITION"], color=C["accent"], ls=":", lw=1,
                    label="shell POSITION")
        axR.set_xlabel("quasi-static strain bias  ε_bias")
        axR.set_ylabel("K(ε_bias)  (tangent modulus, arb.)")
        axR.annotate("WIDTH=%.2g  ASYMMETRY=%.2g (|·|%s0.15)"
                     % (cv["shell_WIDTH"], cv["shell_ASYMMETRY"],
                        "≥" if cv["anisotropic_confirmed_absasym_ge_0p15"] else "<"),
                     xy=(0.03, 0.03), xycoords="axes fraction", fontsize=7, color=C["muted"])
        axR.legend(loc="best", fontsize=7, frameon=False)
    else:
        axR.text(0.5, 0.5, "C-V not run (no grown equilibrium)", ha="center",
                 transform=axR.transAxes, fontsize=8, color=C["muted"])

    out_png = here / "vessel_state_rve.png"
    fig.savefig(out_png, dpi=150, bbox_inches="tight")
    fig.savefig(out_png.with_suffix(".pdf"), bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out_png}")


if __name__ == "__main__":
    main()
