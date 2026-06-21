"""AVE constants-derivation pipeline flowchart (schematic).

SCOPE NOTE: this is a SCHEMATIC of the calibration pipeline, not a computed
figure. It shows how the three empirical calibration inputs (h, c, e) define the
substrate LC network constants, which in turn set the continuum moduli. No
physical value is computed here; the arrows are pipeline edges, not derivations.
"""

import matplotlib.patches as patches
import matplotlib.pyplot as plt

from ave.viz import style
from ave_path_util import SIM_OUTPUTS

# assets/figures (repo-root-anchored sibling of assets/sim_outputs).
_FIGURES_DIR = SIM_OUTPUTS.parent / "figures"


def create_flowchart() -> None:
    style.apply("print")

    fig, ax = plt.subplots(figsize=style.figsize("wide"))
    ax.set_axis_off()
    ax.set_xlim(0, 1)
    ax.set_ylim(0.05, 0.95)

    inputs_y = 0.8
    network_y = 0.5
    macro_y = 0.2

    def draw_box(
        x: float, y: float, text: str, color: str, width: float = 0.24, height: float = 0.13
    ) -> None:
        box = patches.FancyBboxPatch(
            (x - width / 2, y - height / 2),
            width,
            height,
            boxstyle="round,pad=0.02",
            ec=color,
            fc="white",
            lw=1.8,
        )
        ax.add_patch(box)
        ax.text(x, y, text, ha="center", va="center", color="black", fontsize=9, fontweight="bold")

    def draw_arrow(start: tuple[float, float], end: tuple[float, float]) -> None:
        ax.annotate(
            "",
            xy=end,
            xytext=start,
            arrowprops=dict(
                arrowstyle="->", color=style.COLORS["muted"], lw=1.8,
                connectionstyle="arc3,rad=0.1",
            ),
        )

    # 1. Empirical calibration inputs (accent / highlight).
    in_color = style.COLORS["accent"]
    draw_box(0.2, inputs_y, "Planck's constant ($h$)\nCirculation quantum", in_color)
    draw_box(0.5, inputs_y, "Speed of light ($c$)\nPhase velocity", in_color)
    draw_box(0.8, inputs_y, "Elementary charge ($e$)\nFlux quantum", in_color)
    ax.text(
        0.5, inputs_y + 0.1, "1. Empirical calibration inputs",
        color=in_color, fontsize=12, fontweight="bold", ha="center",
    )

    # 2. Derived network constants (ave / blue).
    net_color = style.COLORS["ave"]
    draw_box(0.2, network_y, "Node inductance\n$L = h / (e^2 c)$", net_color)
    draw_box(0.5, network_y, "Node distance\n$\\ell_{node}$ (topology)", net_color)
    draw_box(0.8, network_y, "Link capacitance\n$C = e^2 / (h c)$", net_color)
    ax.text(
        0.5, network_y + 0.1, "2. Derived network constants (LC lattice)",
        color=net_color, fontsize=12, fontweight="bold", ha="center",
    )

    # 3. Continuum moduli (comparison / vermillion for contrast).
    mac_color = style.COLORS["comparison"]
    draw_box(0.2, macro_y, "Permeability\n$\\mu_0 = L / \\ell_{node}$", mac_color)
    draw_box(0.5, macro_y, "Impedance\n$Z_0 = \\sqrt{L/C}$", mac_color)
    draw_box(0.8, macro_y, "Permittivity\n$\\epsilon_0 = C / \\ell_{node}$", mac_color)
    ax.text(
        0.5, macro_y + 0.1, "3. Continuum moduli",
        color=mac_color, fontsize=12, fontweight="bold", ha="center",
    )

    # Arrows: inputs -> network -> moduli.
    draw_arrow((0.2, inputs_y - 0.07), (0.2, network_y + 0.07))
    draw_arrow((0.5, inputs_y - 0.07), (0.5, network_y + 0.07))
    draw_arrow((0.8, inputs_y - 0.07), (0.8, network_y + 0.07))

    draw_arrow((0.2, network_y - 0.07), (0.2, macro_y + 0.07))
    draw_arrow((0.8, network_y - 0.07), (0.8, macro_y + 0.07))
    draw_arrow((0.2, network_y - 0.07), (0.5, macro_y + 0.07))
    draw_arrow((0.8, network_y - 0.07), (0.5, macro_y + 0.07))

    _FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    out_path = _FIGURES_DIR / "calibration_flowchart.png"
    style.save(fig, out_path)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    create_flowchart()
