"""
Astrophysical Visualization Generator (illustrative figures — NOT a derivation driver).

SCOPE NOTE (2026-05-17 audit per driver-script honesty cleanup pass):
This script plots ILLUSTRATIVE reference figures for the manuscript using
hardcoded literal values + empirical targets. It does NOT compute the AVE
predictions it labels. The values plotted are sourced from external
derivations (corpus leaves or external publications); this script renders
them as visualization, not as the AVE-engine computation chain.

Specifically:
  - plot_flyby(): renders Monte-Carlo histogram of GR Lense-Thirring prediction
    (mean = 2.4e-6 mm/s hardcoded) alongside a vertical line at the "AVE Topo-
    Kinematic Sagnac" value (13.46 mm/s hardcoded). The 13.46 value is NOT
    computed by this script — it's a literal target from external AVE derivation
    (corpus reference TBD-pin).
  - plot_geodynamo(): plots empirical dipole moments for Earth/Venus/Mars +
    AVE constraint annotations. The "VCA Derivation" bar plot is COMMENTED OUT
    (lines 70-72) — the figure is incomplete on the AVE-prediction side and
    needs proper AVE-engine integration to be complete.
  - plot_lunar_heating(): plots Apollo empirical bound (0.5-2.0 TW) with
    "×1836 (Baryon Phase Shear)" annotation. The 1836 multiplier is the
    canonical MACROSCOPIC_BARYON_PHASE_SCALAR (= PROTON_ELECTRON_RATIO) imported
    from ave.core.constants (no longer a hard-coded literal in the annotation).

This script is preserved as an ILLUSTRATIVE figure renderer for the
manuscript pipeline. For AVE-distinct prediction COMPUTATION (not just
visualization), see:
  - simulate_galactic_rotation_curve.py (a_0 + saturation kernel)
  - simulate_bullet_cluster_fdtd.py (static halo superposition; see docstring
    for the 2026-05-17 ponderomotive-halo reframe)
  - sparc_catalog_ingest.py (SPARC 135-galaxy benchmark, 11.5% Q=1 mean
    |residual| at zero parameters)

Class B driver-script honesty cleanup: docstring updated 2026-05-17 to
honestly state this script does not compute AVE-distinct predictions; it
visualizes external values. Rewire option (replace hardcoded literals with
calls to canonical AVE-engine operators like compute_acoustic_sagnac_drag,
ave_saturation_acceleration, etc.) is queued as future cleanup but not
load-bearing — the visualizations serve the manuscript's illustrative
purpose adequately as-is, with the honest-scope acknowledgment.

House-style restyle (Vol-3 Phase-3b figure regen): figure bodies are now
rendered through ``ave.viz.style`` (print profile — white background, Okabe-Ito
palette, legends OUTSIDE the data, no baked titles). This restyle changes only
how the figures LOOK, never the numbers/physics they show. Baked Axes titles
were removed (the title belongs in the LaTeX ``\\caption{}``, not the raster).
"""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless render-to-file driver

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

# Resolve the repo's src/ so `ave` + `ave_path_util` import when run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from ave.core.constants import MACROSCOPIC_BARYON_PHASE_SCALAR  # noqa: E402
from ave.viz import style  # noqa: E402
from ave_path_util import manuscript_path  # noqa: E402


# -----------------------------------------------------
# 1. Flyby Anomaly Monte Carlo Distribution
# -----------------------------------------------------
def plot_flyby() -> None:
    """
    Renders a Monte-Carlo histogram of GR Lense-Thirring (mean 2.4e-6 mm/s,
    hardcoded) alongside a vertical line at the AVE Sagnac target (13.46 mm/s,
    hardcoded literal — NOT computed by this script; sourced from external
    AVE derivation).

    Rendering note: the GR Lense-Thirring cluster sits at ~2.4e-6 mm/s while the
    AVE/NEAR target is at 13.46 mm/s — seven decades apart. A linear x-axis
    spanning 0–14 mm/s renders the GR distribution as an invisible spike at the
    origin (the defect in the previous raster). A symmetric-log x-axis makes both
    populations visible in one frame, so the figure shows what the caption claims.
    """
    # GR Lense-Thirring Monte Carlo (parameters hardcoded; not AVE-distinct)
    mean_lt = 2.4e-6  # mm/s — standard GR Lense-Thirring expectation
    std_lt = 0.5e-6
    lt_dist = np.random.normal(mean_lt, std_lt, 1000)

    # AVE Sagnac target — HARDCODED LITERAL, sourced from external AVE
    # derivation (NOT computed by this script). Corpus reference for the
    # 13.46 mm/s value: TBD-pin (flagged 2026-05-17 audit).
    sagnac_target = 13.46  # mm/s — literal reference value
    empirical = 13.46  # NEAR transit empirical target (matches the AVE prediction by construction)

    style.apply()  # house print profile (white background) FIRST

    fig, ax = plt.subplots(figsize=style.figsize("wide"))

    # Symlog x so the ~1e-6 mm/s GR cluster AND the 13.46 mm/s AVE line both
    # render. linthresh sits below the GR mean so that population is in the log
    # region (visible), not crushed into the linear core around zero.
    ax.set_xscale("symlog", linthresh=1e-7)

    ax.hist(
        lt_dist,
        bins=30,
        color=style.COLORS["comparison"],  # vermillion — standard-physics overlay
        alpha=0.7,
        label="Classical GR Lense-Thirring\n(50-transit Monte Carlo, hardcoded)",
    )

    ax.axvline(
        sagnac_target,
        color=style.COLORS["ave"],  # blue — AVE prediction
        linestyle="-",
        linewidth=3,
        label="AVE Topo-Kinematic Sagnac\n(literal ref; NOT computed here)",
    )
    ax.axvline(
        empirical,
        color=style.COLORS["accent"],  # bluish-green — empirical target
        linestyle=":",
        linewidth=2,
        label="NEAR empirical target",
    )

    ax.set_yscale("log")
    ax.set_xlabel(style.axis_label(r"Velocity anomaly", r"\Delta V", "mm/s"))
    ax.set_ylabel(style.axis_label("Counts", "N", ""))
    ax.set_xlim(1e-7, 1e2)
    style.legend(ax, where="right")

    fig.savefig(
        manuscript_path("vol_3_macroscopic", "figures", "flyby_monte_carlo.png")
    )
    plt.close(fig)


# -----------------------------------------------------
# 2. Geodynamo Topo-Kinematic Impedance Limits
# -----------------------------------------------------
def plot_geodynamo() -> None:
    """
    Renders Earth/Venus/Mars empirical dipole moments + AVE constraint
    annotations. The AVE-derivation bar plot is COMMENTED OUT below
    (lines marked `# bulk lint fixup pass`) — the figure is incomplete on
    the AVE-prediction side; needs AVE-engine integration to complete.
    """
    planets = ["Earth", "Venus", "Mars"]

    # Empirical dipole moments [A*m^2] — standard astronomy values
    empirical = [8.0e22, 1e18, 1e18]  # treating Venus/Mars dead as ~1e18 noise floor

    x = np.arange(len(planets))

    style.apply()  # house print profile (white background) FIRST

    fig, ax = plt.subplots(figsize=style.figsize("single"))
    # AVE-derivation bars COMMENTED OUT — incomplete figure pending AVE-engine integration:
    # width = 0.35
    # rects1 = ax.bar(x - width/2, empirical, width,
    #     label="Empirical Target", color=style.COLORS["data"])
    # rects2 = ax.bar(x + width/2, vca_derived, width,
    #     label="AVE VCA Derivation", color=style.COLORS["ave"])

    ax.set_yscale("log")
    # Explicit y-limits: with the AVE-derivation bars commented out there are no
    # data artists, so without a fixed range the log axis collapses and
    # constrained_layout degenerates the aspect ratio. The range brackets the
    # empirical dipole moments + the annotation positions below; it changes no
    # numbers (there is no data series to alter).
    ax.set_ylim(1e9, 1e26)
    ax.set_xlim(-0.5, len(planets) - 0.5)
    ax.set_ylabel(style.axis_label("Magnetic dipole moment", r"m", r"$\mathrm{A\,m^2}$"))
    ax.set_xticks(x)
    ax.set_xticklabels(planets)
    ax.grid(axis="y")

    # AVE constraint annotations (limiting factor per planet, illustrative).
    # Okabe-Ito accent (green) / comparison (vermillion) for the "ok" vs
    # "limited" read so the annotation is colourblind-safe.
    ax.text(0, 1e25, r"$X_L$ limited", ha="center", fontsize=9, color=style.COLORS["accent"])
    ax.text(1, 1e20, r"$U_{eq}$ limited (slow)", ha="center", fontsize=9, color=style.COLORS["comparison"])
    ax.text(2, 1e10, r"$R_{Fe}$ limited (solid)", ha="center", fontsize=9, color=style.COLORS["comparison"])

    fig.savefig(
        manuscript_path("vol_3_macroscopic", "figures", "vca_dynamo_comparison.png")
    )
    plt.close(fig)


# -----------------------------------------------------
# 3. Lunar Inductive Resonant Heating
# -----------------------------------------------------
def plot_lunar_heating() -> None:
    """
    Renders Apollo empirical bound (0.5-2.0 TW) for lunar heat flow with
    AVE "×1836 Baryon Phase Shear" annotation. The 1836 multiplier is the
    canonical MACROSCOPIC_BARYON_PHASE_SCALAR (= PROTON_ELECTRON_RATIO),
    imported from ave.core.constants rather than hard-coded in the label.
    The AVE-prediction bar plot is COMMENTED OUT below.
    """
    style.apply()  # house print profile (white background) FIRST

    fig, ax = plt.subplots(figsize=style.figsize("single"))

    # Apollo empirical bound for lunar heat flow [W]
    target_low = 0.5e12
    target_high = 2.0e12

    # AVE-prediction bar COMMENTED OUT — incomplete pending AVE-engine integration:
    # labels = ["Classical", "AVE Baryon Phase Shear"]
    # watts = [..., ...]
    # bars = ax.bar(labels, watts, color=[style.COLORS["muted"], style.COLORS["ave"]], width=0.5)

    ax.axhspan(
        target_low,
        target_high,
        color=style.COLORS["accent"],
        alpha=0.25,
        label="Apollo empirical target bound",
    )

    ax.set_yscale("log")
    ax.set_ylabel(style.axis_label("Steady-state power flow", "P", "W"))
    ax.set_xticks([])  # no bar series in the live driver — x is categorical-empty
    ax.set_ylim(1e9, 1e13)

    # Annotation: the ×1836 macroscopic baryon-phase-shear multiplier, sourced
    # from canon (MACROSCOPIC_BARYON_PHASE_SCALAR). Placed in interior whitespace
    # below the Apollo band; with the legend moved OUTSIDE the data (style.legend
    # where="below") it no longer collides with a legend box.
    ax.annotate(
        rf"$\times {MACROSCOPIC_BARYON_PHASE_SCALAR:.0f}$ (baryon phase shear)",
        xy=(0.5, 3e10),
        xytext=(0.5, 3e10),
        ha="center",
        va="center",
        fontsize=10,
        color=style.COLORS["muted"],
    )

    style.legend(ax, where="below")

    fig.savefig(
        manuscript_path("vol_3_macroscopic", "figures", "lunar_inductive_heating.png")
    )
    plt.close(fig)


if __name__ == "__main__":
    print("Generating illustrative astrophysical visualization plots...")
    print("(NOTE: This script visualizes hardcoded literals + empirical targets;")
    print(" does NOT compute AVE-distinct predictions. See docstring for scope.)")
    plot_flyby()
    plot_geodynamo()
    plot_lunar_heating()
    print("Files saved to manuscript/vol_3_macroscopic/figures/")
