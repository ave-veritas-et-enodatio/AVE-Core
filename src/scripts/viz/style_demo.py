"""Demo driver for the shared AVE house figure style (``ave.viz.style``).

Renders a 3-panel figure exercising the whole style API so the module's output
can be verified by eye against the five ave-figure-discipline axes (this render
is the module's proof-of-correctness, not just the unit test):

    (a) line plot — AVE vs comparison vs data series, with a legend off the data,
    (b) sequential field imshow — CMAP_SEQ + colorbar,
    (c) signed/diverging field imshow — CMAP_DIV (zero-centred) + colorbar.

Every axis uses ``style.axis_label`` (units in brackets, Axis 2); every series
uses a semantic ``style.COLORS`` entry paired with a distinct linestyle/marker
(never colour alone, Axis 4); output goes through ``style.save`` (PDF + PNG,
Axis 4 vector-preferred). The figure carries NO baked suptitle/Axes-title — the
caption lives in the LaTeX ``\\caption{}`` of whatever chapter embeds it.

Run::

    PYTHONPATH=src ./.venv/bin/python src/scripts/viz/style_demo.py

Writes ``assets/sim_outputs/viz/style_demo.{pdf,png}``. This is a STYLE demo: the
plotted numbers are illustrative synthetic curves, not engine output or a
forward prediction (ave-driver-script-honesty — it asserts nothing physical).
"""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless: this is a render-to-file driver

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

# Resolve the repo's src/ so `ave` + `ave_path_util` import when run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from ave.viz import style  # noqa: E402
from ave_path_util import sim_output  # noqa: E402


def build_figure(profile: str = "print") -> "matplotlib.figure.Figure":
    """Build the 3-panel demo figure on the house style. Returns the figure.

    ``profile`` selects the house profile: ``"print"`` (white background,
    manuscript default) or ``"screen"`` (dark background, interactive/field viz).
    """
    style.apply(profile)

    fig, axes = plt.subplots(1, 3, figsize=style.figsize("wide"))
    ax_line, ax_seq, ax_div = axes

    # --- Panel (a): line plot — AVE / comparison / data, legend off the data ---
    x = np.linspace(0.0, 10.0, 200)
    ave_curve = np.sin(x) * np.exp(-x / 12.0)
    comparison_curve = np.sin(x) * np.exp(-x / 30.0)  # a "standard-physics" overlay
    rng = np.random.default_rng(0)
    x_data = np.linspace(0.5, 9.5, 12)
    y_data = np.sin(x_data) * np.exp(-x_data / 12.0) + rng.normal(0, 0.02, x_data.size)

    ax_line.plot(x, ave_curve, color=style.COLORS["ave"], linestyle="-", label="AVE")
    ax_line.plot(
        x, comparison_curve, color=style.COLORS["comparison"], linestyle="--",
        label="Standard physics",
    )
    ax_line.plot(
        x_data, y_data, color=style.COLORS["data"], linestyle="none", marker="o",
        markersize=4, label="Data",
    )
    ax_line.set_xlabel(style.axis_label("Time", "t", "ns"))
    ax_line.set_ylabel(style.axis_label("Amplitude", "A", "dimensionless"))
    # Legend OUTSIDE the axes: the data is a full-range oscillation, so there is
    # no in-axes whitespace and "right" would land on the neighbouring panel —
    # place it below, spread across one row (ave-figure-discipline Axis 3).
    style.legend(ax_line, where="below", ncol=3)

    # --- Panel (b): sequential field — CMAP_SEQ + colorbar -------------------
    gy, gx = np.mgrid[-3:3:128j, -3:3:128j]
    seq_field = np.exp(-(gx**2 + gy**2))  # one-sided magnitude (>= 0)
    im_seq = ax_seq.imshow(
        seq_field, origin="lower", extent=(-3, 3, -3, 3), cmap=style.CMAP_SEQ,
        aspect="equal",
    )
    # A unit that is itself a math symbol must be passed as mathtext (the
    # caller's job — `axis_label` keeps plain-text units like "Hz" literal).
    ell = r"$\ell_{\mathrm{node}}$"
    ax_seq.set_xlabel(style.axis_label("Position", "x", ell))
    ax_seq.set_ylabel(style.axis_label("Position", "y", ell))
    cb_seq = fig.colorbar(im_seq, ax=ax_seq, shrink=0.8)
    cb_seq.set_label(style.axis_label("Energy density", r"u", "dimensionless"))

    # --- Panel (c): signed field — CMAP_DIV (zero-centred) + colorbar --------
    div_field = gx * np.exp(-(gx**2 + gy**2) / 2.0)  # signed (has a meaningful 0)
    vmax = float(np.abs(div_field).max())
    im_div = ax_div.imshow(
        div_field, origin="lower", extent=(-3, 3, -3, 3), cmap=style.CMAP_DIV,
        vmin=-vmax, vmax=vmax, aspect="equal",
    )
    ax_div.set_xlabel(style.axis_label("Position", "x", ell))
    ax_div.set_ylabel(style.axis_label("Position", "y", ell))
    cb_div = fig.colorbar(im_div, ax=ax_div, shrink=0.8)
    cb_div.set_label(style.axis_label("Signed field", r"V_{ref}", "dimensionless"))

    return fig


def main() -> None:
    # Render BOTH profiles so each is dogfooded against the figure-discipline axes
    # (print = manuscript default; screen = dark interactive/field profile).
    for profile, name in (("print", "style_demo"), ("screen", "style_demo_screen")):
        fig = build_figure(profile)
        written = style.save(fig, sim_output("viz", name))
        plt.close(fig)
        for p in written:
            print(f"wrote {p}")


if __name__ == "__main__":
    main()
