"""
Operating-regimes phase-diagram plotter (illustrative — NOT the Axiom 4 kernel).

SCOPE NOTE (2026-05-17 driver-script honesty sweep):
This script plots an illustrative stress-strain phase diagram of the three
operating regimes (linear / non-linear stiffening / rupture). The curve labeled
"Illustrative cubic-stiffening" is a phenomenological `strain + 0.5*strain^3`
curve chosen for visual clarity — NOT the canonical Axiom 4 dielectric
saturation kernel `S(A) = sqrt(1 - A^2)`. The diagram serves as pedagogical
narrative for the three-regime concept; quantitative saturation behavior must be
computed via the canonical engine. The V_snap annotation reads the canonical
ave.core.constants.V_SNAP value (= m_e c^2 / e ~ 511 kV).
"""

import matplotlib.pyplot as plt
import numpy as np

from ave.core.constants import V_SNAP
from ave.viz import style
from ave_path_util import SIM_OUTPUTS

# assets/figures (repo-root-anchored sibling of assets/sim_outputs).
_FIGURES_DIR = SIM_OUTPUTS.parent / "figures"

# Canonical absolute snap voltage, formatted for the annotation (~511 kV).
_V_SNAP_KV = V_SNAP / 1.0e3


def create_phase_diagram() -> None:
    style.apply("print")

    fig, ax = plt.subplots(figsize=style.figsize("wide"))

    strain = np.linspace(0, 1.2, 500)
    stress_linear = strain
    stress_actual = strain + 0.5 * strain**3

    rupture_strain = 0.85
    rupture_stress = rupture_strain + 0.5 * rupture_strain**3
    stress_actual[strain > rupture_strain] = np.nan

    ax.plot(
        strain, stress_linear, "--", color=style.COLORS["muted"], lw=2,
        label="Ideal Hookean (classical physics)",
    )
    ax.plot(
        strain, stress_actual, "-", color=style.COLORS["ave"], lw=3,
        label="Illustrative cubic-stiffening (NOT Axiom 4 kernel)",
    )

    # Regime I: linear.
    ax.axvspan(0, 0.4, alpha=0.12, color=style.COLORS["ave"])
    ax.text(
        0.2, 0.12, "I. Linear regime\n(acoustic modes)",
        color=style.COLORS["data"], ha="center", fontweight="bold", fontsize=11,
    )

    # Regime II: tensor stiffening.
    ax.axvspan(0.4, rupture_strain, alpha=0.12, color=style.COLORS["accent"])
    ax.text(
        0.625, 0.12, "II. Tensor regime\n(non-linear stiffening)",
        color=style.COLORS["data"], ha="center", fontweight="bold", fontsize=11,
    )

    # Regime III: rupture.
    ax.axvspan(rupture_strain, 1.2, alpha=0.18, color=style.COLORS["comparison"], hatch="//")
    ax.text(
        1.025, 0.5, "III. Rupture limit\n(topological defect formation)",
        color=style.COLORS["comparison"], ha="center", fontweight="bold", fontsize=11,
        rotation=90, va="center",
    )

    ax.axvline(0.4, color=style.COLORS["muted"], ls=":")
    ax.axvline(rupture_strain, color=style.COLORS["comparison"], ls="-", lw=2)

    bbox_props = dict(boxstyle="round,pad=0.4", fc="white", ec=style.COLORS["muted"], lw=1.5)
    ax.annotate(
        "Electromagnetism\nWeak gravity (Newtonian)",
        xy=(0.15, 0.15 + 0.5 * 0.15**3),
        xytext=(0.03, 0.85),
        arrowprops=dict(facecolor=style.COLORS["data"], shrink=0.05, width=1, headwidth=6,
                        edgecolor=style.COLORS["data"]),
        color=style.COLORS["data"], fontsize=10, bbox=bbox_props,
    )
    ax.annotate(
        "MOND acceleration scale ($a_0$)\nStrong-force confinement",
        xy=(0.6, 0.6 + 0.5 * 0.6**3),
        xytext=(0.4, 1.15),
        arrowprops=dict(facecolor=style.COLORS["data"], shrink=0.05, width=1, headwidth=6,
                        edgecolor=style.COLORS["data"]),
        color=style.COLORS["data"], fontsize=10,
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=style.COLORS["accent"], lw=1.5),
    )
    ax.annotate(
        r"Absolute snap limit ($V_{snap} = " + f"{_V_SNAP_KV:.0f}" + r"$ kV)"
        + "\nPair production / event horizon",
        xy=(rupture_strain, rupture_stress),
        xytext=(0.5, 1.42),
        arrowprops=dict(facecolor=style.COLORS["comparison"], shrink=0.05, width=2, headwidth=8,
                        edgecolor=style.COLORS["comparison"]),
        color=style.COLORS["comparison"], fontsize=10,
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=style.COLORS["comparison"], lw=1.5),
    )

    ax.set_xlim(0, 1.2)
    ax.set_ylim(0, 1.6)
    ax.set_xlabel(style.axis_label("Local vacuum strain magnitude", r"|\nabla \Psi|", ""))
    ax.set_ylabel(style.axis_label("Restoring tension / topological resistance", "T", ""))
    ax.set_xticks([])
    ax.set_yticks([])

    style.legend(ax, where="below", ncol=2)

    _FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    out_path = _FIGURES_DIR / "operating_regimes_phase_diagram.png"
    style.save(fig, out_path)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    create_phase_diagram()
