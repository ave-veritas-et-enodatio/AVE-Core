"""Isotope-decay figure driver — Q-factor optimization as the decay driver.

Replaces the fragile side-effect plot that lived inside ``test_isotope_decay.py``
(which wrote a ``tests/outputs`` PNG and annotated *solver* mass-defect energies
that are not framework-derived quantities). This driver owns the manuscript
figure ``manuscript/vol_6_periodic_table/figures/isotope_decay_analytics.png``
that ``chapters/01_computational.tex`` ``\\includegraphics``-es.

What the figure shows (and deliberately does NOT show):

  * LEFT panel — Tritium ($^3$H) $\\to$ Helium-3 ($^3$He) $\\beta$-decay. The
    HEADLINE is the engine-computed topological Q-factor jump
    ($\\approx 3.27 \\to 19.04$): the unstable, geometrically strained tritium
    topology relaxes into the tight, high-Q Helium-3 lattice. The framework's
    contribution here is *mechanistic* (why the decay runs, and which way) — so
    the only energy annotated is the EMPIRICAL mass-energy difference
    ($\\approx 0.529$ MeV, $\\beta$-endpoint $\\approx 18.6$ keV), explicitly
    labelled empirical. The solver's own $\\Delta E$ is NOT shown — it is not a
    framework-derived energy and quoting it would over-claim.

  * RIGHT panel — Beryllium-8 ($^8$Be) $\\to 2\\alpha$ fission. This is a
    STRUCTURAL story, not an energy story: $^8$Be is two $^4$He Alpha tanks with
    no central bridging neutron to mediate mutual inductance ($M_{bridge}$), so
    the open Wheatstone bridge cleaves into two independent Alphas. No energy
    number is annotated — the broken-bridge topology is the whole point.

The Q-factors are COMPUTED from the engine (the same path the regression test
asserts), never hard-coded, so this figure can never silently drift from the
engine.

Run::

    PYTHONPATH=$PWD/src ./.venv/bin/python \\
        src/scripts/vol_6_periodic_table/simulations/plot_isotope_decay.py
"""

from __future__ import annotations

import numpy as np

from ave.viz import style
from ave_path_util import manuscript_path
from scripts.vol_6_periodic_table.simulations.simulate_element import (
    M_N_RAW,
    M_P_RAW,
    calculate_topological_mass,
    get_nucleon_coordinates,
)

# Empirical (CODATA) decay energetics — labelled empirical on the figure. These
# are NOT framework-derived; they are quoted from mass-energy data so the figure
# can show "which energy actually came out" without ever printing the solver's
# (non-physical) mass-defect number.
TRITIUM_EMPIRICAL_DE_MEV = 0.529  # m(3H)c^2 - m(3He)c^2; beta endpoint ~18.6 keV


def compute_q_factor(Z: int, A: int) -> float:
    """Engine-computed topological Q-factor (binding-energy / effective-radius).

    Mirrors ``test_isotope_decay.compute_topology`` exactly so the figure tracks
    the regression-asserted engine output. Q = U_stored / R_eff, with U_stored
    the topological binding energy and R_eff the max nucleon-to-centroid radius.
    """
    N = A - Z
    raw_mass = (Z * M_P_RAW) + (N * M_N_RAW)
    binding_energy = raw_mass - calculate_topological_mass(Z, A)

    nodes = get_nucleon_coordinates(Z, A)
    if len(nodes) > 1:
        com = np.mean(nodes, axis=0)
        max_radius = max(np.linalg.norm(np.array(n) - com) for n in nodes)
    else:
        max_radius = 0.85
    effective_radius = max_radius if max_radius > 0.1 else 0.85

    return (binding_energy / effective_radius) if binding_energy > 0 else 1.0


def main() -> None:
    import matplotlib.pyplot as plt

    style.apply()  # white print profile, matching the Phase-3 figures

    # --- Engine-computed Q-factors (never hard-coded) ---------------------
    q_tritium = compute_q_factor(1, 3)   # ~3.27
    q_he3 = compute_q_factor(2, 3)       # ~19.04
    q_he4 = compute_q_factor(2, 4)       # ~19.19 per Alpha
    q_be8 = compute_q_factor(4, 8)       # open bridge, low Q

    fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize=style.figsize("wide"))

    # =====================================================================
    # LEFT: Tritium beta decay — the Q-factor jump is the headline.
    # =====================================================================
    labels_l = ["$^3$H (Tritium)\nstrained topology", "$^3$He (Helium-3)\nstable topology"]
    qvals_l = [q_tritium, q_he3]
    bars_l = ax_l.bar(
        labels_l,
        qvals_l,
        color=[style.COLORS["comparison"], style.COLORS["ave"]],
        width=0.6,
    )
    ax_l.set_ylabel(style.axis_label("Topological quality factor", "Q", ""))
    ax_l.grid(axis="y", linestyle="--", alpha=0.6, zorder=0)
    ax_l.set_ylim(0, q_he3 * 1.32)

    # Bar-value annotations (the engine Q-values themselves).
    for rect, q in zip(bars_l, qvals_l):
        ax_l.annotate(
            f"$Q = {q:.2f}$",
            xy=(rect.get_x() + rect.get_width() / 2, q),
            xytext=(0, 4),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold",
        )

    # The headline: the Q-factor jump arrow (3.27 -> 19.04).
    ax_l.annotate(
        f"Q-factor jump\n${q_tritium:.2f} \\rightarrow {q_he3:.2f}$",
        xy=(1, q_he3),
        xytext=(0.5, q_he3 * 1.18),
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=style.COLORS["accent"], lw=2.0),
    )

    # The ONLY energy: the empirical mass-energy difference, labelled empirical.
    # Placed in the clear whitespace between the two bars (mid-height) so it never
    # sits over a bar (ave-figure-discipline: no text-over-graphics).
    ax_l.annotate(
        f"empirical $\\Delta E = m(^3\\mathrm{{H}})c^2 - m(^3\\mathrm{{He}})c^2$\n"
        f"$\\approx {TRITIUM_EMPIRICAL_DE_MEV:.3f}$ MeV "
        f"($\\beta$ endpoint $\\approx 18.6$ keV)",
        xy=(0.5, q_he3 * 0.5),
        ha="center",
        va="center",
        fontsize=8.5,
        color=style.COLORS["muted"],
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=style.COLORS["muted"], lw=0.8),
    )

    # =====================================================================
    # RIGHT: Beryllium-8 alpha fission — the broken inductive bridge story.
    # =====================================================================
    labels_r = [
        "$^8$Be\nno bridging neutron\n($M_{bridge} = 0$)",
        "$2\\,^4$He\ntwo independent Alphas",
    ]
    qvals_r = [q_be8, 2.0 * q_he4]
    bars_r = ax_r.bar(
        labels_r,
        qvals_r,
        color=[style.COLORS["muted"], style.COLORS["accent"]],
        width=0.6,
    )
    ax_r.set_ylabel(style.axis_label("Total network quality factor", "Q", ""))
    ax_r.grid(axis="y", linestyle="--", alpha=0.6, zorder=0)
    ax_r.set_ylim(0, 2.0 * q_he4 * 1.32)

    for rect, q in zip(bars_r, qvals_r):
        ax_r.annotate(
            f"$Q = {q:.2f}$",
            xy=(rect.get_x() + rect.get_width() / 2, q),
            xytext=(0, 4),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold",
        )

    # The structural story (no energy number): broken bridge -> clean cleavage.
    ax_r.annotate(
        "broken Wheatstone bridge\ninstant cleavage into $2\\alpha$",
        xy=(1, 2.0 * q_he4),
        xytext=(0.5, 2.0 * q_he4 * 1.18),
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=style.COLORS["accent"], lw=2.0),
    )

    # No on-figure title (the chapter \caption carries it). Write PNG only — the
    # chapter \includegraphics-es the .png and the slot has historically been
    # PNG-only (no stray .pdf companion).
    outpath = manuscript_path(
        "vol_6_periodic_table", "figures", "isotope_decay_analytics"
    )
    written = style.save(fig, outpath, dpi=300, formats=("png",))
    for p in written:
        print(f"[+] wrote {p}")
    print(
        f"[i] engine Q: 3H={q_tritium:.4f}  3He={q_he3:.4f}  "
        f"4He={q_he4:.4f}  8Be={q_be8:.4f}"
    )


if __name__ == "__main__":
    main()
