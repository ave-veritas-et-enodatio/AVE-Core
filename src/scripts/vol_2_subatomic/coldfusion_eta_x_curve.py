#!/usr/bin/env python3
"""
FT-Cold-Fusion eta(x) — Parameter-free Pd-D fusion-rate-vs-loading FORWARD curve
================================================================================
STATUS: FORWARD PREDICTION (parameter-free curve SHAPE + threshold LOCATION).
        NOT a fit to data. Executes prereg
        research/2026-05-31_FT-coldfusion-eta-x-curve_prereg.md.

This driver computes and plots the substrate-mechanism prediction for the
deuteron-deuteron tunnelling enhancement in a Pd cathode as a function of the
D/Pd atomic loading ratio x, and marks the three parameter-free loadings:

    x_onset   — where the Gamow-exponent reduction becomes significant
    x = 0.852 — radiation-less (Gamma -> 0) threshold  (n_scalar = 2.5)
    x = 0.929 — substrate shatter / operational-window edge (A_0 = 1)

----------------------------------------------------------------------------
SUBSTRATE MECHANISM (canonical — Phase-3 cold-fusion result, Class B):
  research/2026-05-31_Q-EMBED-SEL-1_step_c_phase3_cold_fusion_result.md
  AVE-Fusion/manuscript/vol_fusion/chapters/03_metric_catalyzed_fusion.tex
  AVE-Fusion/manuscript/vol_fusion/chapters/04_the_palladium_proxy.tex

  1. Macroscopic Pd-D loading x  ->  beta-phase volumetric strain
        Delta V / V_0 ~= 0.13 * x        (standard Pd metallurgy; Ch4:67)
     The 0.13 is the ONE non-substrate input. FLAGGED. Everything else is
     canonical (sqrt(2*alpha), alpha).

  2. Ax-2 Topo-Kinematic Isomorphism maps that volumetric strain to a
     continuous substrate scalar strain, normalised to the Ax-4 yield
     boundary r_yield = sqrt(2*alpha) (constants.R_I, constants.py:402):
        A_0(x) = 0.13 * x / sqrt(2*alpha)        ->  A_0 = 1 at x = 0.929 (Ch4:72)

  3. Ax-4 self-saturation kernel sets the local scalar refractive index:
        S(A_0)        = sqrt(1 - A_0^2)
        n_scalar(A_0) = 1 / S(A_0)               (n_scalar = 1/S identification)

  4. The substrate does NOT lower the Coulomb barrier; it NARROWS the Gamow
     tunnelling DISTANCE via coordinate compression (Ch3:51, dr_lab=dr_vac/n).
     The WKB integral picks up a 1/n factor (Ch3:55, eq:gamow_compressed):
        eta(x) = eta_0 / n_scalar = eta_0 * S(A_0) = eta_0 * sqrt(1 - A_0^2)
        P_fusion(x) = exp(-2 * eta(x))

  5. At n_scalar >= 2.5 (x >= 0.852): the matrix impedance Z_0/n matches the
     saturated D-D bridging node impedance Z_0/2.5; the reflection coefficient
     Gamma -> 0 (Ch4:25-26) -> acoustic-phonon (heat) channel, NOT gamma. This
     is the substrate-mechanism for FP's "missing radiation".

  6. At x ~= 0.929: A_0 = 1, Ax-4 yield (shatter, Ch4:51-55). The operational
     window is the ~2.9% sliver below (Ch4:64-80, Topological Survival Window).

----------------------------------------------------------------------------
PARAMETER-FREE CONTENT (prereg §4):
  * The curve SHAPE  eta(x)/eta_0 = sqrt(1 - (0.13 x / sqrt(2 alpha))^2)
    is parameter-free given canonical sqrt(2*alpha) + metallurgical 0.13.
  * The threshold LOCATIONS x = 0.852 (n=2.5) and x = 0.929 (shatter) are
    parameter-free.
  * eta_0 (the vacuum Gamow exponent) sets the ABSOLUTE rate but NOT the
    shape/threshold, and additionally carries environmental-screening
    uncertainty. The parameter-free DISCRIMINATORS are therefore the curve
    SHAPE + the threshold LOCATION — NOT the absolute rate.

  => This driver plots the fully-parameter-free  eta(x)/eta_0  curve as the
     primary forward prediction, and shows the enhancement P/P_0 with eta_0
     drawn as an explicit, labelled SCALE family (NOT a fitted value).

----------------------------------------------------------------------------
CLASS (consistency-vs-emergence v1.3): Class B substrate-mechanism
  manifestation. The n_scalar = 1/S(A_0) identification is substrate-canonical
  INPUT (not Class-2-derived from K4+Cosserat primitives alone). This is NOT
  Class 2, NOT an empirical validation of cold fusion.
"""

from __future__ import annotations

import os

import numpy as np

from ave.core.constants import ALPHA, R_I

# --- The one non-substrate input (FLAGGED) --------------------------------
# Pd beta-phase volumetric swelling coefficient: Delta V / V_0 ~= 0.13 * x.
# Standard Pd hydrogen-loading metallurgy (AVE-Fusion Ch4:67). This is the
# SINGLE non-substrate input in the whole curve; the parameter-free claim is
# conditional on it.
PD_VOL_COEFF = 0.13

# --- Canonical substrate yield boundary -----------------------------------
# R_I = sqrt(2*alpha) is imported from constants.py:402 (NEVER hard-coded).
# A_0(x) = PD_VOL_COEFF * x / R_I ;  A_0 = 1 at the shatter loading.
R_YIELD = R_I  # = sqrt(2*ALPHA) ~= 0.12081

# --- Canonical D-D structural-bridging impedance threshold -----------------
# n_scalar >= N_BRIDGE gives Z_matrix = Z_0/n <= Z_0/N_BRIDGE = Z_node, so
# Gamma -> 0 (radiation-less, heat-not-gamma). Canonical AVE-Fusion Ch4:25.
N_BRIDGE = 2.5


def substrate_strain(x: np.ndarray | float) -> np.ndarray | float:
    """Ax-2 TKI substrate scalar strain A_0(x) = 0.13 x / sqrt(2 alpha)."""
    return PD_VOL_COEFF * np.asarray(x, dtype=float) / R_YIELD


def saturation_kernel(x: np.ndarray | float) -> np.ndarray | float:
    """Ax-4 kernel S(A_0) = sqrt(1 - A_0^2). Equals eta(x)/eta_0 (the SHAPE).

    Clipped at A_0 = 1 (the shatter boundary): beyond it the substrate has
    yielded and the kernel is undefined (returns 0.0 = total compression).
    """
    a0 = substrate_strain(x)
    return np.sqrt(np.clip(1.0 - a0**2, 0.0, 1.0))


def n_scalar(x: np.ndarray | float) -> np.ndarray | float:
    """Local scalar refractive index n_scalar = 1/S(A_0). inf at shatter."""
    s = saturation_kernel(x)
    with np.errstate(divide="ignore"):
        return np.where(s > 0.0, 1.0 / np.where(s > 0.0, s, np.nan), np.inf)


def eta_ratio(x: np.ndarray | float) -> np.ndarray | float:
    """Parameter-free Gamow-exponent ratio eta(x)/eta_0 = S(A_0).

    This is the FULLY parameter-free forward prediction (no eta_0 needed).
    """
    return saturation_kernel(x)


def fusion_enhancement(x: np.ndarray | float, eta_0: float) -> np.ndarray | float:
    """Tunnelling enhancement P_fusion(x) / P_fusion(0).

    P = exp(-2 eta);  P(x)/P(0) = exp(-2 eta_0 (S(A_0) - 1)).
    eta_0 is an EXPLICIT SCALE parameter (carries the absolute-rate +
    environmental-screening uncertainty); it is NOT fitted to any data. The
    shape of log10(P/P0) vs x is fixed; eta_0 only rescales the vertical axis.
    """
    return np.exp(-2.0 * eta_0 * (saturation_kernel(x) - 1.0))


def threshold_loadings() -> dict[str, float]:
    """The three parameter-free marked loadings (all from canonical constants).

    Returns x_onset, x_radiationless (n=2.5), x_shatter (A_0=1), plus the
    FP extreme corner (n=200) for reference.
    """
    x_shatter = R_YIELD / PD_VOL_COEFF  # A_0 = 1

    # Radiation-less Gamma->0 threshold: n_scalar = 2.5  <=>  S = 0.4
    #   A_0 = sqrt(1 - (1/2.5)^2);  x = A_0 * sqrt(2a)/0.13
    a0_bridge = np.sqrt(1.0 - (1.0 / N_BRIDGE) ** 2)
    x_radiationless = a0_bridge * R_YIELD / PD_VOL_COEFF

    # FP extreme corner: n_scalar = 200 (room-T D-D rate matches keV-vacuum)
    a0_fp = np.sqrt(1.0 - (1.0 / 200.0) ** 2)
    x_fp_corner = a0_fp * R_YIELD / PD_VOL_COEFF

    # Onset: where the compression becomes order-unity significant, i.e.
    # n_scalar = 2.0  (S = 0.5; the Gamow tunnelling DISTANCE is halved). This
    # is a parameter-free "becomes significant" marker that lands at the left
    # edge of the operational window (x ~ 0.805).
    #   S = 0.5  =>  A_0 = sqrt(1 - 0.25);  x = A_0 * sqrt(2a)/0.13
    a0_onset = np.sqrt(1.0 - 0.5**2)
    x_onset = a0_onset * R_YIELD / PD_VOL_COEFF

    return {
        "x_onset": float(x_onset),
        "x_radiationless": float(x_radiationless),
        "x_shatter": float(x_shatter),
        "x_fp_corner": float(x_fp_corner),
    }


def _print_table(x_grid: np.ndarray) -> None:
    """Print the substrate-mechanism table at the prereg's key loadings."""
    print("\nFT-Cold-Fusion eta(x) — parameter-free forward curve")
    print("=" * 68)
    print(f"  PD_VOL_COEFF (Delta V/V0 = 0.13 x)  = {PD_VOL_COEFF}  [FLAGGED: non-substrate]")
    print(f"  ALPHA (constants.py:133)            = {ALPHA:.12g}")
    print(f"  R_I = sqrt(2 alpha) (constants:402) = {R_YIELD:.10f}")
    print(f"  N_BRIDGE (D-D node, Ch4:25)         = {N_BRIDGE}")
    print("-" * 68)
    print(f"  {'x (D/Pd)':>9} {'A_0':>8} {'S=eta/eta0':>11} {'n_scalar':>10}  regime")
    for x in x_grid:
        a0 = float(substrate_strain(x))
        s = float(saturation_kernel(x))
        n = (1.0 / s) if s > 0 else float("inf")
        if x < 0.852:
            regime = "Gamma>0 (discrete radiation channels)"
        elif x < 0.929:
            regime = "Gamma->0 (radiation-less; heat-not-gamma)"
        else:
            regime = "A_0>=1 (shatter / yield)"
        print(f"  {x:>9.3f} {a0:>8.4f} {s:>11.4f} {n:>10.3f}  {regime}")
    print("=" * 68)


def make_plot(out_path: str | None = None, eta_0_family: tuple[float, ...] = (3.0, 5.0, 7.0)) -> str:
    """Compute + plot the parameter-free curve and the enhancement family.

    Top panel  : eta(x)/eta_0 = S(A_0) — fully parameter-free SHAPE + the three
                 marked loadings.
    Bottom panel: log10(P/P_0) enhancement for a FAMILY of eta_0 (shown as an
                 explicit scale band, NOT a fit). The shape is identical; eta_0
                 only rescales the axis.
    """
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    th = threshold_loadings()
    x = np.linspace(0.80, 0.93, 1300)

    fig, (ax_top, ax_bot) = plt.subplots(
        2, 1, figsize=(11, 10), sharex=True, facecolor="#070712"
    )

    # ---- vertical markers shared by both panels --------------------------
    markers = [
        (
            th["x_onset"], "#ffaa00",
            rf"x_onset = {th['x_onset']:.3f}  ($n_{{scalar}}=2$, $S=0.5$, tunnel-dist halved)",
        ),
        (
            th["x_radiationless"],
            "#00ffaa",
            rf"x = {th['x_radiationless']:.3f}  ($n_{{scalar}}=2.5$, $\Gamma\to0$, heat-not-$\gamma$)",
        ),
        (th["x_shatter"], "#ff3366", rf"x = {th['x_shatter']:.3f}  ($A_0=1$, shatter / yield)"),
    ]

    # ---- TOP: parameter-free eta(x)/eta_0 = S(A_0) -----------------------
    ax_top.set_facecolor("#070712")
    s_curve = eta_ratio(x)
    ax_top.plot(
        x, s_curve, "-", color="#33ddff", lw=3,
        label=r"$\eta(x)/\eta_0 = S(A_0) = \sqrt{1-(0.13x/\sqrt{2\alpha})^2}$  (parameter-free)",
    )
    # shade the topological survival / operational window 0.852..0.929
    ax_top.axvspan(
        th["x_radiationless"], th["x_shatter"], color="#00ffaa", alpha=0.07,
        label=r"operational window ($\Gamma\to0$ .. shatter)",
    )
    for xv, col, lab in markers:
        ax_top.axvline(xv, color=col, ls="--", lw=1.8, label=lab)
    # n_scalar=2.5 reference line in S
    ax_top.axhline(1.0 / N_BRIDGE, color="#00ffaa", ls=":", lw=1.2)
    ax_top.text(
        0.802, 1.0 / N_BRIDGE + 0.012, r"$S=1/2.5=0.4$ ($n_{scalar}=2.5$)",
        color="#00ffaa", fontsize=9,
    )
    ax_top.set_ylabel(r"$\eta(x)/\eta_0 = S(A_0)$", color="#dddddd", fontsize=12)
    ax_top.set_ylim(0.0, 1.02)
    ax_top.set_title(
        "FT-Cold-Fusion: parameter-free Gamow-exponent reduction vs Pd-D loading\n"
        r"(substrate NARROWS tunnelling distance via $n_{scalar}=1/S$; barrier height unchanged)",
        color="#ffffff", fontsize=12,
    )
    ax_top.grid(True, color="#223", alpha=0.5)
    ax_top.legend(loc="lower left", fontsize=8.5, facecolor="#0b0b18", labelcolor="#dddddd")
    ax_top.tick_params(colors="#aaaaaa")

    # ---- BOTTOM: enhancement family (eta_0 = explicit scale, NOT a fit) ---
    ax_bot.set_facecolor("#070712")
    cmap_cols = ["#ff66cc", "#cc88ff", "#8899ff"]
    for eta0, col in zip(eta_0_family, cmap_cols):
        log_enh = np.log10(fusion_enhancement(x, eta0))
        ax_bot.plot(
            x, log_enh, "-", color=col, lw=2.2,
            label=rf"$\eta_0={eta0:.0f}$  ($\log_{{10}} P/P_0 = -2\eta_0(S-1)/\ln 10$)",
        )
    ax_bot.axvspan(th["x_radiationless"], th["x_shatter"], color="#00ffaa", alpha=0.07)
    for xv, col, _ in markers:
        ax_bot.axvline(xv, color=col, ls="--", lw=1.8)
    ax_bot.set_xlabel("D/Pd atomic loading ratio  x", color="#dddddd", fontsize=12)
    ax_bot.set_ylabel(r"$\log_{10}\,[\,P_{fusion}(x)/P_{fusion}(0)\,]$", color="#dddddd", fontsize=12)
    ax_bot.set_title(
        r"Tunnelling enhancement — $\eta_0$ drawn as an EXPLICIT SCALE FAMILY "
        r"(carries absolute-rate + screening uncertainty; NOT fitted)",
        color="#cccccc", fontsize=10.5,
    )
    ax_bot.grid(True, color="#223", alpha=0.5)
    ax_bot.legend(loc="upper left", fontsize=8.5, facecolor="#0b0b18", labelcolor="#dddddd")
    ax_bot.tick_params(colors="#aaaaaa")

    fig.text(
        0.5, 0.012,
        "FORWARD PREDICTION (NOT a fit). Parameter-free discriminators = curve SHAPE + threshold LOCATION. "
        "The 0.13 metallurgical coefficient is the one non-substrate input.",
        ha="center", color="#888899", fontsize=8.5,
    )

    if out_path is None:
        # Repo-root assets/figures (where the committed corpus figures live,
        # alongside chiral_dispersion_relation.png). __file__ is
        # src/scripts/vol_2_subatomic/ -> up 3 to repo root.
        repo_root = os.path.normpath(
            os.path.join(os.path.dirname(__file__), "..", "..", "..")
        )
        out_dir = os.path.join(repo_root, "assets", "figures")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "coldfusion_eta_x_curve.png")
    plt.savefig(out_path, dpi=200, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close(fig)
    return os.path.abspath(out_path)


def main() -> None:
    th = threshold_loadings()
    key_x = np.array([0.80, 0.82, 0.84, 0.852, 0.87, 0.90, 0.92, 0.929])
    _print_table(key_x)

    print("\nParameter-free marked loadings (all from canonical constants):")
    print(f"  x_onset        (n_scalar=2, S=0.5)      = {th['x_onset']:.4f}")
    print(f"  x_radiationless(n_scalar=2.5, Gamma->0) = {th['x_radiationless']:.4f}")
    print(f"  x_shatter      (A_0=1, yield)           = {th['x_shatter']:.4f}")
    print(f"  x_fp_corner    (n_scalar=200, FP corner)= {th['x_fp_corner']:.4f}  [reference]")

    out = make_plot()
    print(f"\nFigure written: {out}")


if __name__ == "__main__":
    main()

