"""
Plot the Axiom 4 saturation observables: ε_eff(A) and C_eff(A).

Under the universal saturation kernel S(A) = √(1 − (A/A_yield)²) (Operator 2,
``ave.core.universal_operators.universal_saturation``):
  - Constitutive permittivity: ε_eff = ε_0 · S(A)  → 0  (collapse)
  - Measurable capacitance:    C_eff = C_0 / S(A)  → ∞  (divergence)

These are physically distinct:
  ε  is the material compliance (drops as the lattice stiffens).
  C  is the stored charge per volt (rises as the medium shorts).

The three strain regimes are shaded at the CANONICAL regime boundaries
r₁ = √(2α) and r₂ = √3/2 (``ave.core.regime_map``), not at hand-picked values.

HONESTY (ave-driver-script-honesty): this is a DERIVATION plot of the closed-form
Axiom-4 kernel and its Taylor expansion — not the output of a time-domain
simulation. The curves are plotted in normalised form (ε_eff/ε_0 and C_eff/C_0)
so they are dimensionless; the canonical kernel and regime constants are imported
from ``ave.core``, nothing is hard-coded.

Output: assets/sim_outputs/vacuum_dielectric_saturation.{pdf,png}
"""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless: render-to-file driver

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

# Resolve the repo's src/ so `ave` + `ave_path_util` import when run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from ave.core.constants import EPS_CLIP  # noqa: E402
from ave.core.regime_map import R_LINEAR_MAX, R_NONLINEAR_MAX  # noqa: E402
from ave.core.universal_operators import universal_saturation  # noqa: E402
from ave.viz import style  # noqa: E402
from ave_path_util import sim_output  # noqa: E402


def build_figure() -> "matplotlib.figure.Figure":
    """Build the two-panel ε-collapse / C-divergence figure on the house style."""
    style.apply()  # print profile (white background)

    # Normalised field variable: r = A / A_yield, 0 → (1 − EPS_CLIP). The upper
    # bound is the canonical saturation clip (constants.EPS_CLIP), not a magic
    # 0.999: it is the largest r for which √(1 − r²) > 0 to float64 resolution.
    x = np.linspace(0.0, 1.0 - EPS_CLIP, 2000)

    # Universal saturation kernel S(A) — Operator 2 (A_yield = 1 in normalised r).
    S = universal_saturation(x, 1.0)

    # Constitutive permittivity (collapses):  ε_eff / ε_0 = S
    eps_eff = S
    # Measurable capacitance (diverges):  C_eff / C_0 = 1/S
    C_eff = 1.0 / S

    # Taylor expansion to E⁴ order for ε: ε ≈ ε_0 [1 − (1/2)(A/A_yield)²]
    eps_taylor = 1.0 - 0.5 * x**2
    # Linear regime: ε = ε_0  (and C = C_0)
    eps_linear = np.ones_like(x)

    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=style.figsize("square"), sharex=True
    )

    # Canonical regime boundaries: r₁ = √(2α) (linear→nonlinear),
    # r₂ = √3/2 (nonlinear→yield). Imported from regime_map, not hand-picked.
    r1, r2 = R_LINEAR_MAX, R_NONLINEAR_MAX

    def shade_regimes(ax):
        ax.axvspan(0.0, r1, alpha=0.08, color=style.COLORS["accent"])
        ax.axvspan(r1, r2, alpha=0.08, color=style.COLORS["comparison"])
        ax.axvspan(r2, 1.0, alpha=0.12, color=style.COLORS["muted"])
        ax.axvline(1.0, color=style.COLORS["muted"], linewidth=1.0, linestyle="-")

    # --- Top panel: ε_eff (collapse) -----------------------------------------
    ax1.plot(
        x, eps_eff, color=style.COLORS["ave"], linestyle="-",
        label=r"AVE exact: $\varepsilon_{eff} = \varepsilon_0\,S(A)$",
    )
    ax1.plot(
        x, eps_taylor, color=style.COLORS["comparison"], linestyle="--",
        label=r"Euler–Heisenberg ($E^4$): $\varepsilon_0[1 - \frac{1}{2}(A/A_y)^2]$",
    )
    ax1.plot(
        x, eps_linear, color=style.COLORS["muted"], linestyle=":",
        label=r"Linear: $\varepsilon = \varepsilon_0$",
    )
    shade_regimes(ax1)
    ax1.set_ylabel(
        style.axis_label("Permittivity", r"\varepsilon_{eff}/\varepsilon_0", "dimensionless")
    )
    ax1.set_ylim(-0.05, 1.15)
    style.legend(ax1, where="right")

    # --- Bottom panel: C_eff (divergence) ------------------------------------
    ax2.plot(
        x, C_eff, color=style.COLORS["ave"], linestyle="-",
        label=r"AVE exact: $C_{eff} = C_0/S(A)$",
    )
    ax2.plot(
        x, eps_linear, color=style.COLORS["muted"], linestyle=":",
        label=r"Linear: $C = C_0$",
    )
    shade_regimes(ax2)
    ax2.set_xlabel(
        style.axis_label("Normalised field strain", r"A/A_{yield}", "dimensionless")
    )
    ax2.set_ylabel(
        style.axis_label("Capacitance", r"C_{eff}/C_0", "dimensionless")
    )
    ax2.set_ylim(0.8, 8.0)
    ax2.set_xlim(-0.02, 1.02)
    style.legend(ax2, where="right")

    return fig


def main() -> None:
    fig = build_figure()
    written = style.save(fig, sim_output("vacuum_dielectric_saturation.png"))
    plt.close(fig)
    for p in written:
        print(f"Saved: {p}")


if __name__ == "__main__":
    main()
