"""Entanglement-thread mode properties (Vol 1, Ch 3, Fig.~\\ref{fig:thread_energy}).

DERIVATION plot (not a time-domain simulation): both panels evaluate the
closed-form entanglement-thread expressions from
``ave.topological.entanglement_thread`` over a separation sweep —

    (Left)  Mode energy  E_1 = hbar * pi * c / d   [thread_mode_energy]
            Anti-confining: E_1 ~ 1/d (opposite of a QCD flux tube E ~ d).
            Three regimes vs the k_B T scale at 300 K: energy-dominated
            (d < 1 um), comparable (~1 um), topology-dominated (d > 1 mm).

    (Right) Phase advance per node  delta_phi = 2 pi ell_node / d
            [phase_advance_per_node] -> 0 as d -> infinity (locally invisible),
            while the total winding sum(delta_phi) = 2 pi stays invariant
            (globally present).

No physical constant is hard-coded here: every quantity is imported from
``ave.core.constants`` (via the entanglement-thread library) or read back from
it, so the figure tracks canon. The figure body is restyled through
``ave.viz.style`` (house print profile); the caption lives in the LaTeX
``\\caption{}`` of chapter 03, not in the raster.

Run::

    PYTHONPATH=src ./.venv/bin/python \\
        src/scripts/vol_1_foundations/plot_entanglement_thread_energy.py

Writes ``manuscript/vol_1_foundations/figures/entanglement_thread_energy.{png}``
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

from ave.core.constants import K_B, L_NODE, e_charge  # noqa: E402
from ave.topological.entanglement_thread import (  # noqa: E402
    phase_advance_per_node,
    thread_mode_energy_eV,
)
from ave.viz import style  # noqa: E402
from ave_path_util import manuscript_path  # noqa: E402

# Reference temperature the caption names for the k_B T crossover line.
T_ROOM = 300.0  # K


def build_figure() -> "matplotlib.figure.Figure":
    """Build the two-panel entanglement-thread derivation figure."""
    style.apply()  # house print profile (white background) FIRST

    # Separation sweep spanning sub-fm to interplanetary, log-spaced.
    d = np.logspace(-15, 12, 600)  # m

    # --- Panel (left): anti-confining mode energy E_1 = hbar pi c / d --------
    e1_eV = np.array([thread_mode_energy_eV(di) for di in d])

    fig, (ax_e, ax_phi) = plt.subplots(1, 2, figsize=style.figsize("wide"))

    ax_e.loglog(
        d, e1_eV, color=style.COLORS["ave"], linestyle="-",
        label=r"$E_1 = \hbar\pi c / d$",
    )

    # k_B T at 300 K, in eV, as the energy/topology crossover reference line.
    kt_300k_eV = K_B * T_ROOM / e_charge
    ax_e.axhline(
        kt_300k_eV, color=style.COLORS["muted"], linestyle="--",
        label=r"$k_B T$ (300 K)",
    )

    # Three-regime background shading (energy- / comparable- / topology-dominated)
    # keyed to the 1 um and 1 mm separations the caption names.
    ax_e.axvspan(d.min(), 1e-6, color=style.COLORS["comparison"], alpha=0.10)
    ax_e.axvspan(1e-6, 1e-3, color="#E69F00", alpha=0.12)  # Okabe-Ito orange
    ax_e.axvspan(1e-3, d.max(), color=style.COLORS["accent"], alpha=0.12)

    ax_e.set_xlabel(style.axis_label("Separation", "d", "m"))
    ax_e.set_ylabel(style.axis_label("Mode energy", "E_1", "eV"))
    ax_e.set_xlim(d.min(), d.max())
    style.legend(ax_e, where="below", ncol=2)

    # --- Panel (right): phase advance per node delta_phi = 2 pi ell_node / d --
    # Sweep where the thread is multi-node (d >= ell_node) so delta_phi <= 2 pi.
    d_phi = np.logspace(np.log10(L_NODE), 6, 600)  # m
    dphi_rad = np.array([phase_advance_per_node(di) for di in d_phi])
    dphi_deg = np.degrees(dphi_rad)

    ax_phi.loglog(
        d_phi, dphi_deg, color=style.COLORS["ave"], linestyle="-",
        label=r"$\delta\phi = 2\pi\,\ell_{\mathrm{node}}/d$",
    )
    # Total winding is the conserved invariant: sum(delta_phi) = 2 pi = 360 deg.
    ax_phi.axhline(
        360.0, color=style.COLORS["muted"], linestyle=":",
        label=r"Full winding ($360^\circ$)",
    )
    ax_phi.set_xlabel(style.axis_label("Separation", "d", "m"))
    ax_phi.set_ylabel(style.axis_label("Phase per node", r"\delta\phi", "deg"))
    ax_phi.set_xlim(d_phi.min(), d_phi.max())
    style.legend(ax_phi, where="below", ncol=1)

    return fig


def main() -> None:
    fig = build_figure()
    out = manuscript_path("vol_1_foundations", "figures", "entanglement_thread_energy")
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
