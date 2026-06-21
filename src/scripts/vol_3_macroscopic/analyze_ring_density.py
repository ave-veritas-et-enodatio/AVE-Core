"""Saturn-ring radial-density distribution (Vol 3, macroscopic).

Restyle-only regen of ``saturn_ring_impedance_distribution.png`` through the
AVE house figure style (``ave.viz.style``, print profile). The physics/data are
unchanged: this analyses the output of the dimensionless N-body toy
(``simulate_saturn_rings.simulate_rings``) and histograms the radial distance
``r = sqrt(x^2 + y^2)`` of the ring test-nodes at the first (T=0) and last
(T=end) recorded frames, to show the radial-density evolution of a flat
Keplerian disk under the 1/d coupling.

DIMENSIONLESS TOY MODEL: as documented in ``simulate_saturn_rings``, ``G`` and
``M_SATURN`` are computational parameters, NOT physical constants, and no
physics prediction is made by this figure. There are therefore no
``ave.core.constants`` quantities to import here — the histogram bin edges below
are figure-presentation choices on the toy's dimensionless radial coordinate,
not physical constants (ave-canonical-source: nothing to canonicalise).

The N-body initialiser draws random positions; the original figure was
unseeded. To make this regen a reproducible artifact without altering the
physics model, the RNG is pinned with a fixed seed in this driver only (it pins
the stochastic draw, it does not change the model). The panel-identity labels
(T=0 vs T=end) move into per-panel legends placed outside the data; the baked
Axes titles are dropped — the descriptive caption lives in the LaTeX
``\\caption{}`` of the chapter, not in the raster (ave-figure-discipline
Axis 4).

Run::

    PYTHONPATH=src ./.venv/bin/python \\
        src/scripts/vol_3_macroscopic/analyze_ring_density.py

Writes ``assets/sim_outputs/saturn_ring_impedance_distribution.{pdf,png}``.
"""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless render-to-file driver

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

# Resolve the repo's src/ (for `ave` + `ave_path_util`) and src/scripts/ (for the
# sibling `vol_3_macroscopic` sim package) so the imports below work whether the
# driver is run directly or via PYTHONPATH=src.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from vol_3_macroscopic.simulate_saturn_rings import simulate_rings  # noqa: E402

from ave.viz import style  # noqa: E402
from ave_path_util import sim_output  # noqa: E402

# Pin the stochastic ring initialisation so the regen is reproducible. This pins
# the random draw only; it does not change the toy's physics model.
_RNG_SEED = 0


def build_figure() -> "matplotlib.figure.Figure":
    """Build the two-panel radial-density-evolution figure (restyled)."""
    style.apply()  # house print profile (white background) FIRST

    np.random.seed(_RNG_SEED)
    print("[*] Evolving topological test-nodes...")
    history = simulate_rings()

    # Index 0 is the central mass (Saturn); 1: are the ring test-nodes.
    initial_pos = history[0, 1:]
    final_pos = history[-1, 1:]

    # Radial distance r = sqrt(x^2 + y^2) for each ring node.
    r_initial = np.sqrt(initial_pos[:, 0] ** 2 + initial_pos[:, 1] ** 2)
    r_final = np.sqrt(final_pos[:, 0] ** 2 + final_pos[:, 1] ** 2)

    bins = np.linspace(15, 65, 50)

    # Vertical 2-panel stack: take the full-width banner width from the `wide`
    # preset and give the two stacked panels enough height (two single-figure
    # rows) so the y-labels do not overrun the ~2-inch panels. The panel-identity
    # (T=0 vs T=end) lives in each panel's legend, placed OUTSIDE the data on the
    # right so it never lands on the neighbouring panel (ave-figure-discipline
    # Axis 3); the baked Axes titles are dropped (caption lives in LaTeX).
    fig_w = style.figsize("wide")[0]
    fig_h = 2.0 * style.figsize("single")[1] - 1.0
    fig, (ax_top, ax_bot) = plt.subplots(
        2, 1, sharex=True, figsize=(fig_w, fig_h)
    )

    ax_top.hist(
        r_initial, bins=bins, color=style.COLORS["ave"], alpha=0.85,
        edgecolor=style.COLORS["data"], linewidth=0.4,
        label="T=0: initial uniform density\n(flat topology)",
    )
    ax_top.set_ylabel(style.axis_label("Node count", "N", "count"))
    style.legend(ax_top, where="right")

    ax_bot.hist(
        r_final, bins=bins, color=style.COLORS["comparison"], alpha=0.85,
        edgecolor=style.COLORS["data"], linewidth=0.4,
        label="T=end: resonant band gaps\nemerging (topological shells)",
    )
    ax_bot.set_xlabel(style.axis_label("Radial distance from centre", "r", ""))
    ax_bot.set_ylabel(style.axis_label("Node count", "N", "count"))
    style.legend(ax_bot, where="right")

    return fig


def analyze_ring_impedance() -> None:
    fig = build_figure()
    target = sim_output("saturn_ring_impedance_distribution.png")
    written = style.save(fig, target)
    plt.close(fig)
    # assets/sim_outputs tracks this figure PNG-only; drop the stray companion
    # .pdf so the regen leaves exactly the one tracked raster changed.
    for p in written:
        if p.suffix == ".pdf":
            p.unlink(missing_ok=True)
            print(f"[*] removed stray {p}")
        else:
            print(f"[*] wrote {p}")


if __name__ == "__main__":
    analyze_ring_impedance()
