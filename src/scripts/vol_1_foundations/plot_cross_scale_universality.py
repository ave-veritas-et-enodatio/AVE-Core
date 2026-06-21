# plot_cross_scale_universality.py
# Scale-invariance of the AVE universal operators (Vol 1, Ch 6).
#
# DERIVATION figure (not a single simulation run): it evaluates the CANONICAL
# universal operators — the reflection coefficient Gamma (Op 3) and the
# saturation factor S (Op 2 / Axiom 4) — across illustrative physical domains
# spanning many orders of magnitude, plus the characteristic vacuum impedance
# Z_0 as a scale-invariant reference. The operator formulas are imported from
# the engine (ave.core.universal_operators); the per-domain operating points are
# illustrative anchors drawn from the A-034 cross-scale catalog.
#
# Presentation follows the AVE house style (ave.viz.style) — white print
# profile, Okabe-Ito palette, no baked titles (captions live in the LaTeX).
#
# Authored 2026-06-21 to replace the orphan generator flagged in
# research/2026-06-07_figure-audit-ledger.md (S3 provenance gap). Physics values
# match the prior committed figure; constants are imported from canon.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from pathlib import Path

from ave.viz import style
from ave.core.constants import Z_0
from ave.core.universal_operators import universal_reflection, universal_saturation

# Repo-root-anchored output directory (CWD-independent). This driver lives at
# <repo-root>/src/scripts/vol_1_foundations/, so parents[3] is the repo root.
# assets/figures/ is a committed (tracked) figure tree; the Vol-1 chapter's
# \includegraphics resolves cross_scale_universality.pdf there via main.tex's
# \graphicspath.
_REPO_ROOT = Path(__file__).resolve().parents[3]
_FIG_DIR = _REPO_ROOT / "assets" / "figures"


def _panel_reflection(ax) -> None:
    """Top-left: universal Gamma across 7 domains, all -> Gamma = -1 at threshold.

    Each curve sweeps a normalised driving parameter x/x_c in [0, 1]. As the
    medium saturates its impedance diverges (Z -> 0 seen from the source line,
    the hardened wall), so the reflection coefficient evaluated with the
    canonical universal_reflection operator runs from 0 toward Gamma = -1. The
    partially-matched domains (Seismic Moho, Tachocline, Neutrino MSW) saturate
    to a finite |Gamma| < 1 set by their terminal impedance contrast.
    """
    x = np.linspace(0.0, 1.0, 400)

    # Terminal impedance contrast for each domain, expressed as the impedance
    # SEEN FROM the source line at full drive. Strong-reflection (hardened-wall)
    # domains drive the terminal impedance to ~0 (perfect short -> Gamma = -1);
    # partially-matched domains terminate at a finite contrast. The full-drive
    # |Gamma| targets below reproduce the canonical figure: -1 for the four
    # hardened-wall events, and 0.12 / 0.82 / ~-0.2 for the matched ones.
    domains = [
        # (label, color, linestyle, terminal Gamma at x=1, ramp exponent)
        # The four hardened-wall domains share Gamma(1) = -1 but approach it at
        # different rates (ramp exponent on the drive) so the curves fan out and
        # stay distinguishable, matching the prior figure. The exponent shapes
        # only the ILLUSTRATIVE contrast ramp; Gamma is always the canonical
        # universal_reflection of (Z_0, Z2(x)), and Gamma(0)=0, Gamma(1)=term.
        ("Event Horizon", style.COLORS["accent"], "-", -1.0, 3.0),
        ("Plasma Cutoff", style.COLORS["comparison"], "-", -1.0, 2.0),
        ("Meissner Effect", style.COLORS["ave"], "-", -1.0, 1.3),
        ("Pauli Exclusion", "#CC79A7", "-", -1.0, 5.0),
        ("Seismic Moho", "#E69F00", "--", 0.12, 1.5),
        ("Tachocline", "#56B4E9", "--", 0.82, 2.5),
        ("Neutrino MSW", "#7F7F7F", "--", -0.20, 1.5),
    ]

    for label, color, ls, gamma_term, ramp in domains:
        # Map the terminal Gamma back to a terminal impedance ratio via the
        # canonical operator's inverse, then sweep the contrast in proportion to
        # the normalised drive so every curve passes through Gamma(0)=0 and
        # reaches Gamma(1)=gamma_term computed by universal_reflection.
        # Gamma = (Z2 - Z1)/(Z2 + Z1); fix Z1 = Z_0, solve terminal Z2.
        z2_term = Z_0 * (1.0 + gamma_term) / (1.0 - gamma_term)
        z2 = Z_0 + (z2_term - Z_0) * (x**ramp)  # contrast ramp with the drive
        gamma = universal_reflection(Z_0, z2)
        ax.plot(x, gamma, color=color, linestyle=ls, linewidth=1.8, label=label)

    ax.axhline(-1.0, color=style.COLORS["muted"], linewidth=0.8, linestyle=":")
    ax.axhline(0.0, color=style.COLORS["muted"], linewidth=0.6, linestyle=":")
    ax.set_xlim(0.0, 1.0)
    # Range spans the hardened-wall floor (Gamma = -1) to the partially-matched
    # over-impedance domains (Tachocline Gamma = +0.82 per the summary table).
    ax.set_ylim(-1.1, 1.0)
    ax.set_xlabel(style.axis_label("Normalised drive", "x/x_c", ""))
    ax.set_ylabel(style.axis_label("Reflection coefficient", r"\Gamma", ""))
    style.legend(ax, where="below", ncol=2, fontsize=7)


def _panel_saturation(ax) -> None:
    """Top-right: universal saturation S = sqrt(1 - (V/V_c)^2) with anchors.

    Operating points span the linear regime (gravitational waves, acoustic) to
    deep saturation (pair production), all riding the single Axiom-4 kernel.
    """
    v = np.linspace(0.0, 1.0, 500)
    s = universal_saturation(v, 1.0)
    ax.plot(v, s, color=style.COLORS["comparison"], linewidth=2.0, zorder=2)

    # Illustrative operating points (V/V_c), reproduced from the prior figure.
    points = [
        (0.02, r"GW ($h\sim10^{-21}$)", style.COLORS["comparison"]),
        (0.10, "Acoustic", style.COLORS["ave"]),
        (0.40, "Galaxy outskirts", "#E69F00"),
        (0.687, "PONDER-05 (68.7%)", style.COLORS["accent"]),
        (0.85, "Tokamak 15 keV", "#CC79A7"),
        (0.95, "Pair production", "#8000A0"),
    ]
    for vp, label, color in points:
        sp = float(universal_saturation(vp, 1.0))
        ax.scatter([vp], [sp], color=color, s=45, zorder=3, edgecolors=style.COLORS["data"],
                   linewidths=0.4)
        ax.annotate(label, (vp, sp), textcoords="offset points", xytext=(8, 8),
                    fontsize=7, color=color)

    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.05)
    ax.set_xlabel(style.axis_label("Drive / critical", "V/V_c", ""))
    ax.set_ylabel(style.axis_label("Saturation factor", r"S=\sqrt{1-(V/V_c)^2}", ""))


def _panel_impedance(ax) -> None:
    """Bottom-left: characteristic impedance across length scale, vs Z_0.

    Most domains sit on the Z_0 = 376.7 Ohm matched line; the seismic mantle and
    solar tachocline are the off-line contrasts that drive their Gamma in the
    top-left panel.
    """
    # (label, length scale [m], impedance [Ohm]) — illustrative anchors,
    # reproduced from the prior figure. Z_0 is the canonical matched value.
    z0 = Z_0
    points = [
        ("Planck length", 1.6e-35, z0, style.COLORS["ave"]),
        ("Lattice pitch", 1e-13, z0 * 0.95, "#6A3D9A"),
        ("Proton radius", 8e-16, z0 * 1.02, "#8000A0"),
        ("Atom", 1e-10, z0 * 0.9, "#9C27B0"),
        ("Protein bond", 1.5e-10, z0 * 1.05, "#CC79A7"),
        ("Virus", 1e-7, z0 * 0.92, "#C2185B"),
        ("Cell", 1e-5, 1e2, "#C2185B"),
        ("LIGO arm", 4e3, z0, "#E69F00"),
        ("Seismic\n(mantle)", 1e6, 2.5e7, "#CC79A7"),
        ("Solar\ntachocline", 5e8, 4e-1, "#FB6A4A"),
        ("Solar system", 1.5e13, z0, "#E69F00"),
        ("Galaxy", 1e21, z0, "#F0E442"),
        ("Observable\nuniverse", 8e26, z0, "#F0E442"),
    ]
    for label, length, z, color in points:
        ax.scatter([length], [z], color=color, s=80, zorder=3,
                   edgecolors=style.COLORS["data"], linewidths=0.4)
        ax.annotate(label, (length, z), textcoords="offset points", xytext=(0, 10),
                    fontsize=6, ha="center", color=style.COLORS["data"])

    ax.axhline(z0, color=style.COLORS["comparison"], linewidth=1.0, linestyle=":",
               label=rf"$Z_0 = {z0:.1f}\ \Omega$")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1e-37, 1e29)
    ax.set_ylim(1e-1, 1e8)
    ax.set_xlabel(style.axis_label("Length scale", "L", "m"))
    ax.set_ylabel(style.axis_label("Characteristic impedance", "Z", r"\Omega"))
    style.legend(ax, where="below")


def _panel_table(ax) -> None:
    """Bottom-right: scale-invariant operator summary table.

    Values reproduced verbatim from the prior committed figure (no physics value
    or sign altered). NOTE the Z1/Z2 columns and the Gamma column use different
    conventions for the hardened-wall rows (see report); rendered as-is.
    """
    ax.axis("off")
    col_labels = ["Domain", "Scale", r"$Z_1$", r"$Z_2$", r"$\Gamma$"]
    rows = [
        ["Pauli exclusion", r"$10^{-15}$ m", "0", r"$Z_0$", r"$-1$"],
        ["Plasma cutoff", r"$10^{-6}$ m", "0", r"$Z_0$", r"$-1$"],
        ["Meissner effect", r"$10^{-9}$ m", "0", r"$Z_0$", r"$-1$"],
        ["Seismic (Moho)", r"$10^{6}$ m", r"$Z_{\rm crust}$", r"$Z_{\rm mantle}$", "0.12"],
        ["Event horizon", r"$10^{3}$ m", "0", r"$Z_0$", r"$-1$"],
        ["Tachocline", r"$10^{8}$ m", r"$Z_{\rm rad}$", r"$Z_{\rm conv}$", "0.82"],
        ["Neutrino MSW", r"$10^{32}$ m$^{-3}$", r"$Z_{\nu e}$", r"$Z_{\nu\mu}$", "var"],
    ]
    table = ax.table(cellText=rows, colLabels=col_labels, loc="center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1.0, 1.5)
    # Header styling on the house palette (white print profile).
    for (r, c), cell in table.get_celld().items():
        cell.set_edgecolor(style.COLORS["muted"])
        if r == 0:
            cell.set_facecolor("#E8EEF4")
            cell.set_text_props(weight="bold", color=style.COLORS["data"])
        else:
            cell.set_facecolor("white")
            cell.set_text_props(color=style.COLORS["data"])


def main() -> None:
    print("Rendering cross-scale universality (derivation figure)...")
    style.apply("print")  # white-background print profile (house style)

    fig, axes = plt.subplots(2, 2, figsize=style.figsize("wide"))
    fig.set_size_inches(11.0, 9.0)  # 2x2 grid needs more room than the wide preset

    _panel_reflection(axes[0, 0])
    _panel_saturation(axes[0, 1])
    _panel_impedance(axes[1, 0])
    _panel_table(axes[1, 1])

    # Output to the committed assets/figures tree; the Vol-1 chapter references
    # the .pdf (PNG sibling is also tracked there).
    out_path = _FIG_DIR / "cross_scale_universality.pdf"
    written = style.save(fig, out_path, formats=("pdf", "png"))
    for w in written:
        print(f"Saved: {w}")


if __name__ == "__main__":
    main()
