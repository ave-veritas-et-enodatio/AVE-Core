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
    "×1836 (Baryon Phase Shear)" annotation. The 1836 multiplier reference
    is not computed by this script.

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
"""

import os

import matplotlib.pyplot as plt
import numpy as np

# Create output dir if needed
out_dir = "manuscript/vol_3_macroscopic/figures"
os.makedirs(out_dir, exist_ok=True)


# -----------------------------------------------------
# 1. Flyby Anomaly Monte Carlo Distribution
# -----------------------------------------------------
def plot_flyby() -> None:
    """
    Renders a Monte-Carlo histogram of GR Lense-Thirring (mean 2.4e-6 mm/s,
    hardcoded) alongside a vertical line at the AVE Sagnac target (13.46 mm/s,
    hardcoded literal — NOT computed by this script; sourced from external
    AVE derivation).
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

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.hist(
        lt_dist,
        bins=30,
        color="red",
        alpha=0.6,
        label="Classical GR Lense-Thirring\n(50 Transit Monte Carlo, hardcoded)",
    )

    ax.axvline(sagnac_target, color="blue", linestyle="-", linewidth=3,
               label="AVE Topo-Kinematic Sagnac (literal ref; NOT computed in this script)")
    ax.axvline(empirical, color="green", linestyle=":", linewidth=2, label="NEAR Empirical Target")

    ax.set_yscale("log")
    ax.set_title("Earth Flyby Velocity Anomaly (NEAR Transit) — illustrative")
    ax.set_xlabel(r"Velocity Anomaly ($\Delta V$) [mm/s]")
    ax.set_ylabel("Execution Probability Density (Log)")
    ax.legend()
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "flyby_monte_carlo.png"), dpi=300)
    plt.close()


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

    fig, ax = plt.subplots(figsize=(6, 5))
    # AVE-derivation bars COMMENTED OUT — incomplete figure pending AVE-engine integration:
    # width = 0.35
    # rects1 = ax.bar(x - width/2, empirical, width,
    #     label="Empirical Target", color="darkgray")
    # rects2 = ax.bar(x + width/2, vca_derived, width,
    #     label="AVE VCA Derivation", color="darkorange")

    ax.set_yscale("log")
    ax.set_ylabel(r"Magnetic Dipole Moment [A $\cdot$ m$^2$]")
    ax.set_title("Geodynamo Topo-Kinematic Limits — illustrative (incomplete)")
    ax.set_xticks(x)
    ax.set_xticklabels(planets)
    ax.legend()
    ax.grid(axis="y", alpha=0.3)

    # AVE constraint annotations (limiting factor per planet, illustrative)
    ax.text(0, 1e25, r"$X_L$ limited", ha="center", fontsize=9, color="green")
    ax.text(1, 1e20, r"$U_{eq}$ limited (Slow)", ha="center", fontsize=9, color="red")
    ax.text(2, 1e10, r"$R_{Fe}$ limited (Solid)", ha="center", fontsize=9, color="red")

    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "vca_dynamo_comparison.png"), dpi=300)
    plt.close()


# -----------------------------------------------------
# 3. Lunar Inductive Resonant Heating
# -----------------------------------------------------
def plot_lunar_heating() -> None:
    """
    Renders Apollo empirical bound (0.5-2.0 TW) for lunar heat flow with
    AVE "×1836 Baryon Phase Shear" annotation. The 1836 multiplier
    reference is NOT computed by this script (literal annotation only).
    The AVE-prediction bar plot is COMMENTED OUT below.
    """
    fig, ax = plt.subplots(figsize=(6, 4))

    # Apollo empirical bound for lunar heat flow [W]
    target_low = 0.5e12
    target_high = 2.0e12

    # AVE-prediction bar COMMENTED OUT — incomplete pending AVE-engine integration:
    # labels = ["Classical", "AVE Baryon Phase Shear"]
    # watts = [..., ...]
    # bars = ax.bar(labels, watts, color=["gray", "purple"], width=0.5)

    ax.axhspan(target_low, target_high, color="green", alpha=0.2, label="Apollo Empirical Target Bound")

    ax.set_yscale("log")
    ax.set_ylabel("Steady State Power Flow [Watts]")
    ax.set_title("Lunar Thermal Energy Budget — illustrative (incomplete)")
    ax.legend(loc="lower right")
    ax.grid(axis="y", alpha=0.3)

    # Annotation: literal "×1836" reference (NOT computed by this script)
    ax.annotate(
        r"$\times 1836$ (Baryon Phase Shear, literal ref)",
        xy=(0.5, 1e11),
        xytext=(0.5, 1e11),
        ha="center",
        va="center",
        fontsize=10,
        bbox=dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9),
    )

    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "lunar_inductive_heating.png"), dpi=300)
    plt.close()


if __name__ == "__main__":
    print("Generating illustrative astrophysical visualization plots...")
    print("(NOTE: This script visualizes hardcoded literals + empirical targets;")
    print(" does NOT compute AVE-distinct predictions. See docstring for scope.)")
    plot_flyby()
    plot_geodynamo()
    plot_lunar_heating()
    print("Files saved to manuscript/vol_3_macroscopic/figures/")
