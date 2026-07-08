"""House-WHITE figure for the PUMP INVENTORY (P6 make-or-break gate).

Panel A: the astrophysical pump inventory -- AVE-active response A^2 per
         environment (static B is transparent by FORK-1; radiation on clean
         paths is below the lab pump).
Panel B: the FORK-1 discriminator -- the magnitude-keyed counterfactual
         (B/B_SNAP)^2 (would rupture the vacuum at magnetar B) vs the actual
         circulation-keyed response (A_I = 0, transparent, at any B).

Run:  PYTHONPATH=src python3 src/scripts/vol_9_device/pump_inventory_astrophysical_figure.py
"""

from __future__ import annotations

import os

import matplotlib.pyplot as plt
import numpy as np

from ave.core.constants import B_SNAP
from ave.viz import style
from scripts.vol_9_device import pump_inventory_astrophysical as P

FLOOR = 1e-40  # display floor for exact-zero (transparent) bars


def main() -> str:
    style.apply("print")
    fork1 = P.fork1_static_B_test()
    envs = P.build_environment_table()
    B_DUAL = P.B_DUAL

    fig, (axA, axB) = plt.subplots(1, 2, figsize=(11.0, 4.6))

    # ---- Panel A: environment inventory ----
    kind_color = {"static-B": style.COLORS["ave"],
                  "static-E": style.COLORS["accent"],
                  "radiation": style.COLORS["comparison"]}
    labels = [e.tag for e in envs]
    vals = [max(e.A2_active, FLOOR) for e in envs]
    colors = [kind_color[e.kind] for e in envs]
    x = np.arange(len(envs))
    axA.bar(x, vals, color=colors, edgecolor="black", linewidth=0.4)
    axA.set_yscale("log")
    axA.axhline(P.A_LAB_SQ, color=style.COLORS["muted"], ls="--", lw=1.2)
    axA.text(len(envs) - 0.4, P.A_LAB_SQ * 1.5, "lab pump A$^2\\approx$6e-7",
             ha="right", va="bottom", fontsize=8, color=style.COLORS["muted"])
    axA.set_xticks(x)
    axA.set_xticklabels(labels, rotation=90, fontsize=7)
    axA.set_ylabel("AVE-active response  A$^2$  (dimensionless)")
    axA.set_xlabel("environment (E1-E12; see table)")
    axA.set_ylim(FLOOR, 3.0)
    # legend for the three keying kinds (outside the data)
    handles = [plt.Rectangle((0, 0), 1, 1, color=kind_color[k]) for k in kind_color]
    axA.legend(handles, ["static B (circulation-keyed)", "static E (charge-keyed)",
                         "radiation (both)"], loc="lower center", fontsize=7,
               framealpha=0.9)
    axA.text(0.5, FLOOR * 30, "static B: A$_I$=0  (FORK-1 transparent)",
             fontsize=7, color=style.COLORS["ave"], rotation=90, va="bottom")

    # ---- Panel B: FORK-1 discriminator (magnitude-keyed vs circulation-keyed) ----
    B = np.logspace(6, 12, 400)
    A2_magnitude = (B / B_SNAP) ** 2
    axB.plot(B, A2_magnitude, color=style.COLORS["comparison"], lw=2.0,
             label="IF magnitude-keyed: (B/B$_{SNAP}$)$^2$")
    axB.axhline(1.0, color=style.REGIME_COLORS["IV"], ls="-", lw=1.4)
    axB.text(1.2e6, 1.4, "rupture (A$^2$=1)", fontsize=8,
             color=style.REGIME_COLORS["IV"])
    # the actual circulation-keyed response: A_I = 0 for a static B, at any strength
    axB.plot(B, np.full_like(B, FLOOR * 10), color=style.COLORS["ave"], lw=2.4,
             label="AVE (circulation-keyed): A$_I$=0")
    for Bx, lab in [(1e8, "pulsar\n1e8 T"), (1e11, "magnetar\n1e11 T")]:
        axB.axvline(Bx, color=style.COLORS["muted"], ls=":", lw=1.0)
        axB.text(Bx * 1.1, 3e-3, lab, fontsize=7, color=style.COLORS["muted"])
    axB.axvline(B_SNAP, color="black", ls="-.", lw=1.0)
    axB.text(B_SNAP * 1.1, 1e-6, "B$_{SNAP}$", fontsize=7, rotation=90)
    axB.set_xscale("log")
    axB.set_yscale("log")
    axB.set_ylim(FLOOR, 1e7)
    axB.set_xlabel("static magnetic field  B  [T]")
    axB.set_ylabel("would-be response  A$^2$")
    axB.legend(loc="upper left", fontsize=7, framealpha=0.9)
    axB.annotate("magnetar magnitude EXCEEDS B$_{SNAP}$:\nmagnitude-keying -> vacuum rupture\n"
                 "(excluded). Circulation-keying -> transparent.",
                 xy=(1e11, 2.8e3), xytext=(2e6, 4e4), fontsize=7,
                 color="black")

    fig.tight_layout()
    outdir = os.path.join(os.path.dirname(__file__), "_output")
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, "pump_inventory_astrophysical.png")
    fig.savefig(outpath, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"[figure] {outpath}")
    return outpath


if __name__ == "__main__":
    main()
