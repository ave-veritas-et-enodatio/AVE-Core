"""Decoherence regime boundary (Vol 1, Ch 3, Fig.~\\ref{fig:decoherence_regime}).

DERIVATION plot (not a time-domain simulation): evaluates the closed-form
thread-breaking probability from ``ave.topological.entanglement_thread`` over a
temperature sweep —

    P_break(T) = exp(-2 m_e c^2 / k_B T)            [decoherence_probability]

To destroy the 2 pi winding a new pair must spontaneously appear along the
thread, costing >= 2 m_e c^2; the Boltzmann factor exponentially suppresses
this. The protection energy 2 m_e c^2 ~ 1.022 MeV sets the characteristic
temperature

    T_pair = 2 m_e c^2 / k_B ~ 1.19e10 K

at which the exponent is unity (P = e^-1 ~ 0.37). Three regimes vs T: stable
(T < 1e9 K), transitional (1e9 - 1e10 K), vulnerable (T > 1e10 K). This is the
AVE-vs-standard-QM falsifiable prediction: a sharp temperature onset tied to
2 m_e c^2, absent in environment-coupling-only QM.

No physical constant is hard-coded here: m_e, c, k_B enter through the
library function and ``ave.core.constants``, so the figure tracks canon. The
figure body is restyled through ``ave.viz.style`` (house print profile); the
caption lives in the LaTeX ``\\caption{}`` of chapter 03, not in the raster.

Run::

    PYTHONPATH=src ./.venv/bin/python \\
        src/scripts/vol_1_foundations/plot_entanglement_decoherence_regime.py

Writes
``manuscript/vol_1_foundations/figures/entanglement_decoherence_regime.{png}``
(the stray companion .pdf is removed — that figures dir is PNG-only tracked).
"""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless render-to-file driver

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

# Resolve the repo's src/ so `ave` + `ave_path_util` import when run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from ave.core.constants import C_0, K_B, M_E  # noqa: E402
from ave.topological.entanglement_thread import (  # noqa: E402
    decoherence_probability,
)
from ave.viz import style  # noqa: E402
from ave_path_util import manuscript_path  # noqa: E402


def build_figure() -> "matplotlib.figure.Figure":
    """Build the decoherence-regime-boundary derivation figure."""
    style.apply()  # house print profile (white background) FIRST

    # Temperature sweep across the protected -> vulnerable transition.
    T = np.logspace(7, 11.5, 700)  # K
    p_break = np.array([decoherence_probability(Ti) for Ti in T])

    # Pair-creation characteristic temperature (canon constants, not literals).
    T_pair = 2.0 * M_E * C_0**2 / K_B  # ~ 1.19e10 K

    fig, ax = plt.subplots(figsize=style.figsize("single"))

    ax.semilogx(
        T, p_break, color=style.COLORS["ave"], linestyle="-",
        label=r"$P_{\mathrm{break}} = e^{-2 m_e c^2 / k_B T}$",
    )

    # Three-regime background shading (stable / transition / vulnerable),
    # keyed to the 1e9 and 1e10 K boundaries the caption names.
    ax.axvspan(T.min(), 1e9, color=style.COLORS["accent"], alpha=0.12)
    ax.axvspan(1e9, 1e10, color="#E69F00", alpha=0.12)  # Okabe-Ito orange
    ax.axvspan(1e10, T.max(), color=style.COLORS["comparison"], alpha=0.10)

    # P = 0.5 reference and the T_pair marker.
    ax.axhline(
        0.5, color=style.COLORS["muted"], linestyle="--", label=r"$P = 0.5$",
    )
    ax.axvline(
        T_pair, color=style.COLORS["data"], linestyle=":",
        label=r"$T_{\mathrm{pair}} = 2 m_e c^2 / k_B$",
    )

    ax.set_xlabel(style.axis_label("Temperature", "T", "K"))
    ax.set_ylabel(
        style.axis_label("Decoherence probability", r"P_{\mathrm{break}}", "")
    )
    ax.set_xlim(T.min(), T.max())
    ax.set_ylim(-0.02, 1.05)
    style.legend(ax, where="right")

    return fig


def main() -> None:
    fig = build_figure()
    out = manuscript_path(
        "vol_1_foundations", "figures", "entanglement_decoherence_regime"
    )
    written = style.save(fig, out)
    plt.close(fig)
    # figures/ is PNG-only tracked: drop the stray companion .pdf.
    for p in written:
        if p.suffix == ".pdf":
            p.unlink(missing_ok=True)
            print(f"removed stray {p}")
        else:
            print(f"wrote {p}")


if __name__ == "__main__":
    main()
