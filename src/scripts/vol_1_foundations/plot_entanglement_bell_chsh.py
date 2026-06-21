"""Bell angular correlation and CHSH violation — closed-form derivation figure.

Companion figure for Vol 1 Ch 3 (Quantum and Signal Dynamics), §"CHSH Inequality
Violation" (manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex).

Two panels, both computed from the canonical entanglement-thread physics in
``ave.topological.entanglement_thread`` (no quantum postulates imported, no
constant hard-coded here):

  (Left)  E(θ) = −cos θ                       [bell_correlation]
          Anti-correlation (θ → 0) transitioning to correlation (θ → π).
  (Right) |S(δ)| = |−3cos δ + cos 3δ|         [chsh_parameter]
          vs detector spacing δ, with the classical bound |S| = 2 and the
          Tsirelson bound 2√2 ≈ 2.828 [chsh_max], reached at δ* = π/4 (45°).

HONESTY (ave-driver-script-honesty): this is a DERIVATION plot. Both curves are
the closed-form expressions E = −cos θ and S = −3cos δ + cos 3δ that the engine
library exposes as functions — they are NOT the output of a time-domain
simulation. (The manuscript caption labels the figure "Simulation Output"; the
curves are analytic. Surfaced for the manuscript lane, not silently reconciled.)

Output: manuscript/vol_1_foundations/figures/entanglement_bell_chsh.{pdf,png}
"""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless: render-to-file driver

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

# Resolve the repo's src/ so `ave` + `ave_path_util` import when run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from ave.topological.entanglement_thread import (  # noqa: E402
    bell_correlation,
    chsh_max,
    chsh_parameter,
)
from ave.viz import style  # noqa: E402
from ave_path_util import manuscript_path  # noqa: E402

# Classical (local-hidden-variable) CHSH ceiling. Not a physical constant — it
# is the algebraic bound of the inequality itself, so it lives here as a literal.
CLASSICAL_BOUND = 2.0


def build_figure() -> "matplotlib.figure.Figure":
    """Build the two-panel Bell / CHSH derivation figure on the house style."""
    style.apply()  # print profile (white background)

    fig, (ax_e, ax_s) = plt.subplots(1, 2, figsize=style.figsize("wide"))

    # --- Left panel: angular correlation E(θ) = −cos θ -----------------------
    theta = np.linspace(0.0, np.pi, 400)
    e_curve = bell_correlation(theta)
    theta_deg = np.degrees(theta)

    ax_e.plot(
        theta_deg,
        e_curve,
        color=style.COLORS["ave"],
        linestyle="-",
        label=r"$E(\theta) = -\cos\theta$",
    )
    ax_e.axhline(0.0, color=style.COLORS["muted"], linestyle=":", linewidth=1.0)
    ax_e.set_xlabel(style.axis_label("Detector angle", r"\theta", "deg"))
    ax_e.set_ylabel(style.axis_label("Correlation", "E", "dimensionless"))
    ax_e.set_xlim(0.0, 180.0)
    ax_e.set_ylim(-1.1, 1.1)
    ax_e.set_xticks([0, 45, 90, 135, 180])
    style.legend(ax_e, where="below")

    # --- Right panel: |S(δ)| with classical + Tsirelson bounds ---------------
    delta = np.linspace(0.0, np.pi / 2.0, 400)
    s_curve = np.abs(chsh_parameter(delta))
    delta_deg = np.degrees(delta)

    tsirelson = chsh_max()                 # 2√2 from the engine
    delta_star_deg = 45.0                  # δ* = π/4 where |S| is maximised

    ax_s.plot(
        delta_deg,
        s_curve,
        color=style.COLORS["ave"],
        linestyle="-",
        label=r"$|S(\delta)| = |{-}3\cos\delta + \cos 3\delta|$",
    )
    ax_s.axhline(
        CLASSICAL_BOUND,
        color=style.COLORS["comparison"],
        linestyle="--",
        label=r"Classical bound $|S| = 2$",
    )
    ax_s.axhline(
        tsirelson,
        color=style.COLORS["accent"],
        linestyle="-.",
        label=rf"Tsirelson $2\sqrt{{2}} \approx {tsirelson:.3f}$",
    )
    # Mark the maximising detector spacing δ* = 45°.
    ax_s.axvline(
        delta_star_deg, color=style.COLORS["muted"], linestyle=":", linewidth=1.0
    )
    ax_s.plot(
        [delta_star_deg],
        [tsirelson],
        color=style.COLORS["data"],
        linestyle="none",
        marker="o",
        markersize=5,
        label=r"$\delta^{*} = 45^{\circ}$",
    )
    ax_s.set_xlabel(style.axis_label("Detector spacing", r"\delta", "deg"))
    ax_s.set_ylabel(style.axis_label("CHSH parameter", "|S|", "dimensionless"))
    ax_s.set_xlim(0.0, 90.0)
    ax_s.set_ylim(0.0, 3.1)
    ax_s.set_xticks([0, 15, 30, 45, 60, 75, 90])
    style.legend(ax_s, where="below")

    return fig


def main() -> None:
    # Sanity: the engine's Tsirelson bound is 2√2 and exceeds the classical 2.
    tsirelson = chsh_max()
    assert tsirelson > CLASSICAL_BOUND, "CHSH max must exceed the classical bound"
    assert np.isclose(tsirelson, 2.0 * np.sqrt(2.0)), "CHSH max must equal 2√2"
    print(f"Classical bound |S|       = {CLASSICAL_BOUND:.6f}")
    print(f"Tsirelson bound 2√2       = {tsirelson:.6f}  (engine chsh_max)")
    print(f"E(0) = {bell_correlation(0.0):+.3f}, E(π) = {bell_correlation(np.pi):+.3f}")

    fig = build_figure()
    # The manuscript references this figure at the committed figures/ path.
    written = style.save(fig, manuscript_path("vol_1_foundations", "figures", "entanglement_bell_chsh.png"))
    plt.close(fig)
    for p in written:
        print(f"wrote {p}")


if __name__ == "__main__":
    main()
