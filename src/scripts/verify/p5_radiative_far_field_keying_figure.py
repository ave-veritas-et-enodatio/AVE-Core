"""P5 house-WHITE figure: (A) loading is DECORRELATED from the far-field
diagnostic (the refutation); (B) the S_B near-zone (kr)^2 suppression that makes
PVLAS/BMV consistency COMPUTED. White profile (ave.viz.style), Okabe-Ito, axes
carry quantity+symbol+unit, legend outside, no baked title (caption -> LaTeX)."""

from __future__ import annotations

import os

import matplotlib.pyplot as plt
import numpy as np

from ave.viz import style

from p5_radiative_far_field_keying import (
    E_YIELD,
    I_MAX,
    F_FAR,
    run_all,
    s_b_near_zone_limit,
)


def make_figure(outstem):
    style.apply("print")
    diags, loads, fars = run_all(E_YIELD, I_MAX)
    sb = s_b_near_zone_limit(E_YIELD, I_MAX)

    fig, (axA, axB) = plt.subplots(1, 2, figsize=style.figsize("wide"))

    # ---- Panel A: loading deficit vs far-field diagnostic F -----------------
    labels = {
        "static_E": "static E (charge)",
        "static_B": "static B (loop)",
        "traveling": "radiation (traveling)",
        "standing": "standing wave (control)",
    }
    markers = {"static_E": "o", "static_B": "s", "traveling": "^", "standing": "D"}
    for name, d in diags.items():
        F = d["F_radiated"]
        defic = max(d["deficit_eps"], d["deficit_mu"])
        loads_it = loads[name]["overall"] == "load"
        col = style.COLORS["ave"] if loads_it else style.COLORS["muted"]
        # floor tiny/zero deficits for the log axis; annotate transparent ones
        y = defic if defic > 1e-12 else 1e-12
        axA.scatter([F], [y], s=90, marker=markers[name], color=col,
                    edgecolor="black", zorder=3,
                    label=f"{labels[name]} — {'LOADS' if loads_it else 'transparent'}")
    axA.axvline(F_FAR, color=style.COLORS["muted"], ls="--", lw=1.0)
    axA.text(F_FAR + 0.02, 3e-12, "near | far", color=style.COLORS["muted"],
             rotation=90, va="bottom", ha="left", fontsize=8)
    axA.set_yscale("log")
    axA.set_xlim(-0.08, 1.08)
    axA.set_ylim(5e-13, 1e-1)
    axA.set_xlabel(style.axis_label("Far-field diagnostic", "F=|\\langle S\\rangle|/(uc)", ""))
    axA.set_ylabel(style.axis_label("Loading deficit", "1-S", ""))
    style.legend(axA, where="below", ncol=1, fontsize=7)

    # ---- Panel B: S_B near-zone (kr)^2 suppression --------------------------
    kr = np.array(sb["kr"])
    A_I = np.array(sb["A_I"])
    dn = np.abs(np.array(sb["delta_n_mu"]))
    axB.loglog(kr, A_I, "o-", color=style.COLORS["ave"], label="$A_I$ (circulation coord)")
    axB.loglog(kr, dn, "s--", color=style.COLORS["accent"],
               label="$|\\delta n_\\mu|$ (mu birefringence)")
    # slope-2 guide
    guide = A_I[-1] * (kr / kr[-1]) ** 2
    axB.loglog(kr, guide, ":", color=style.COLORS["muted"], lw=1.2,
               label="$(kr)^2$ guide (slope 2)")
    axB.set_xlabel(style.axis_label("Near-zone parameter", "kr", ""))
    axB.set_ylabel(style.axis_label("Magnitude", "A_I,\\;|\\delta n_\\mu|", ""))
    axB.annotate("PVLAS / BMV\n(kr$\\to$0):\ntransparent",
                 xy=(kr[0], A_I[0]), xytext=(kr[0] * 1.3, A_I[0] * 30),
                 fontsize=7, color=style.COLORS["muted"],
                 arrowprops=dict(arrowstyle="->", color=style.COLORS["muted"], lw=0.8))
    style.legend(axB, where="below", fontsize=7)

    written = style.save(fig, outstem)
    plt.close(fig)
    return written


def main():
    outstem = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "p5_radiative_far_field_keying")
    written = make_figure(outstem)
    print("wrote:", [str(p) for p in written])


if __name__ == "__main__":
    main()
