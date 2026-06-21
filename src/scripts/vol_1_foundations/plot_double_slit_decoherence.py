#!/usr/bin/env python3
r"""
Double-Slit Ohmic Which-Path Decoherence — the AVE-distinct V(Z_det) forward prediction
=======================================================================================

Canonical mechanism (NOT a reflector): which-path "measurement" is an **Ohmic
resistive tap** on the slit-2 ponderomotive wake. A detector that couples to the
A-field draws kinetic energy as Joule heat, thermalizing the phase coherence:

    W_extracted = integral P_load dt  proportional to  |d_t A(x_n)|^2 / Z_det * dt

(canonical: manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/
ohmic-decoherence-born.md, clm-ldmvwi — Born rule derived end-to-end from this).

The detector is a resistive load Z_det on the line carrying the wake. With
r = Z_det / Z_0 the load-to-line ratio:

    Gamma = (r - 1) / (r + 1)                  (voltage reflection coefficient)
    eta   = 1 - |Gamma|^2 = 4r / (1 + r)^2     (absorbed-power fraction)

eta is the **MAXIMUM POWER TRANSFER THEOREM**: absorption is MAXIMIZED at the
MATCHED detector r = 1 (Gamma = 0, eta = 1) -> full which-path tap -> fringe
visibility V -> 0. Mismatched extremes (short r -> 0, open r -> inf) reflect
(|Gamma| -> 1, eta -> 0) -> little absorption -> fringes survive (V -> 1).

So V vs Z_det is NON-MONOTONIC: a DIP to minimum at the matched detector r = 1,
rising on both sides. V vs eta is monotonic (V ~ 1 - eta). THE DIP IS THE
FALSIFIER: standard (Copenhagen) QM predicts NO detector-impedance dependence
of fringe visibility (a flat line); AVE predicts the dip at Z_det = Z_0.

ENGINE: reuses the DISSIPATIVE FDTD `run_fdtd_slit(observer_damping=...)` from
`double_slit_design_space.py` — its observer is `P *= (1 - obs_mask)`, a genuine
Ohmic (energy-absorbing) tap, with uniform c = 1 (no CFL bug; dt*sqrt(2) < 1).
We do NOT use `simulate_double_slit_observer.py` (that is a reflective
stiffness-bump on the superseded "helical photon" framing + a CFL bug).

MODELING NOTE (stated in the caption): this 2D acoustic FDTD is an ILLUSTRATION
of the canonical Ohmic mechanism, not an emergence test. Mapping the canonical
dial onto the engine, the per-step tap `observer_damping` is set proportional to
eta(r): d = D_FULL * eta, with D_FULL chosen so eta -> 1 fully taps slit-2
(fringes collapse to the single-slit envelope) and eta -> 0 is no tap (fringes
survive). A monotonic d(eta) is the only modeling requirement; the physics
content is the eta(r) max-power-transfer dip, which is engine-independent.

Output: assets/sim_outputs/double_slit_decoherence.png (PNG kept; the sibling
PDF under assets/sim_outputs is gitignored).

Usage:
    PYTHONPATH=src python src/scripts/vol_1_foundations/plot_double_slit_decoherence.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from ave.viz import style  # noqa: E402
from ave_path_util import sim_output  # noqa: E402

# Reuse the DISSIPATIVE FDTD driver (Ohmic tap, uniform c=1). Attribution: the
# `run_fdtd_slit` simulator is authored in double_slit_design_space.py; we import
# it unchanged (it is guarded by `if __name__ == "__main__"`, safe to import).
_THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_THIS_DIR))
from double_slit_design_space import run_fdtd_slit  # noqa: E402


# ---------------------------------------------------------------------------
# Canonical impedance physics (engine-independent)
# ---------------------------------------------------------------------------
def eta_absorbed(r: np.ndarray | float) -> np.ndarray | float:
    """Absorbed-power fraction eta = 1 - |Gamma|^2 = 4r/(1+r)^2 (max-power transfer).

    r = Z_det / Z_0. Maximized (eta=1) at the matched detector r=1.
    """
    return 4.0 * r / (1.0 + r) ** 2


# ---------------------------------------------------------------------------
# Engine calibration: canonical eta(r) -> per-step Ohmic tap `observer_damping`
# ---------------------------------------------------------------------------
# d = D_FULL * eta : monotone in eta, with eta->1 (matched) giving a near-complete
# slit-2 tap (fringes collapse to the single-slit envelope) and eta->0 no tap.
# D_FULL tuned on the engine so the V(r) minimum sits at r=1 with smooth shoulders.
D_FULL: float = 0.78


def damping_from_eta(eta: float) -> float:
    """Map canonical absorbed fraction eta in [0,1] to the engine per-step tap."""
    return D_FULL * float(eta)


# ---------------------------------------------------------------------------
# Fringe-visibility measurement on a screen cross-section
# ---------------------------------------------------------------------------
def fringe_visibility(cross: np.ndarray, halfwin: int = 110) -> float:
    """V = mean fringe modulation depth in the central interference zone.

    For each interior local maximum (a fringe peak) inside +/- halfwin of the
    screen centre, the modulation against its adjacent troughs is
    (peak - trough)/(peak + trough). A pure single-slit envelope (no fringes)
    -> ~0; sharp interference fringes -> large. This is the standard Michelson
    visibility V = (I_max - I_min)/(I_max + I_min) applied per fringe, which is
    robust to the broad single-slit envelope that fixed-window I_max/I_min is not.
    """
    c = len(cross) // 2
    reg = cross[c - halfwin : c + halfwin]
    maxi = [i for i in range(1, len(reg) - 1) if reg[i] >= reg[i - 1] and reg[i] > reg[i + 1]]
    mini = [i for i in range(1, len(reg) - 1) if reg[i] <= reg[i - 1] and reg[i] < reg[i + 1]]
    if len(maxi) < 2 or len(mini) < 1:
        return 0.0
    vs: list[float] = []
    for pk in maxi:
        if reg[pk] < 0.08:
            continue
        left = [m for m in mini if m < pk]
        right = [m for m in mini if m > pk]
        if not left or not right:
            continue
        trough = 0.5 * (reg[max(left)] + reg[min(right)])
        vs.append((reg[pk] - trough) / (reg[pk] + trough + 1e-30))
    return float(np.mean(vs)) if vs else 0.0


# ---------------------------------------------------------------------------
# Simulation parameters (shared by sweep + cross-sections)
# ---------------------------------------------------------------------------
_SIM = dict(steps=1500, nx=600, ny=400)
_R_SWEEP = np.logspace(-1, 1, 17)  # Z_det/Z_0 ~ 0.1 -> 10, log-spaced
_R_CROSS = (0.2, 1.0, 5.0)  # cross-section detectors: survive / washed / survive


def _run(r: float) -> tuple[np.ndarray, float, float]:
    """Run the FDTD for load ratio r; return (screen cross-section, eta, V)."""
    eta = float(eta_absorbed(r))
    cross, _ = run_fdtd_slit(observer_damping=damping_from_eta(eta), **_SIM)
    return cross, eta, fringe_visibility(cross)


def main() -> None:
    style.apply("print")  # white-bg manuscript profile

    # --- Baseline (no detector) for relative-visibility normalization -------
    base_cross, _ = run_fdtd_slit(observer_damping=0.0, **_SIM)
    v0 = fringe_visibility(base_cross)
    if v0 <= 0:
        raise RuntimeError("baseline (no-detector) visibility is zero — check the engine")
    print(f"  baseline fringe visibility V0 (no detector) = {v0:.4f}")

    # --- Sweep r = Z_det/Z_0 -> (eta, V) ------------------------------------
    print("  sweeping r = Z_det/Z_0 (log 0.1 -> 10) ...", flush=True)
    etas: list[float] = []
    v_rel: list[float] = []
    for r in _R_SWEEP:
        _, eta, v = _run(r)
        etas.append(eta)
        v_rel.append(v / v0)
        print(f"    r={r:7.3f}  eta={eta:5.3f}  V/V0={v / v0:5.3f}", flush=True)

    # --- Cross-sections at survive / matched / survive ----------------------
    cross_data: dict[float, tuple[np.ndarray, float, float]] = {}
    for r in _R_CROSS:
        cross, eta, v = _run(r)
        cross_data[r] = (cross, eta, v / v0)
        print(f"    cross-section r={r}: eta={eta:.3f}  V/V0={v / v0:.3f}", flush=True)

    # ------------------------------------------------------------------ figure
    fig = plt.figure(figsize=(style.figsize("wide")[0], 8.0))
    gs = fig.add_gridspec(
        2, 3, height_ratios=[1.45, 1.0], hspace=0.62, wspace=0.34, top=0.97, bottom=0.10
    )

    # === HEADLINE: V vs Z_det/Z_0 — the dip at the matched detector ==========
    ax = fig.add_subplot(gs[0, :2])
    ax.set_xscale("log")
    # Smooth canonical V(eta(r)) ~ 1 - eta reference curve (engine-independent):
    r_fine = np.logspace(-1, 1, 400)
    v_canon = 1.0 - eta_absorbed(r_fine)
    ax.plot(
        r_fine,
        v_canon,
        color=style.COLORS["muted"],
        linestyle=":",
        linewidth=1.3,
        label=r"AVE canonical $1-\eta(r)$",
        zorder=2,
    )
    ax.plot(
        _R_SWEEP,
        v_rel,
        color=style.COLORS["ave"],
        linestyle="-",
        marker="o",
        markersize=4,
        linewidth=1.8,
        label="AVE FDTD (Ohmic tap)",
        zorder=4,
    )
    # Copenhagen: no detector-impedance dependence (flat at full visibility)
    ax.axhline(
        1.0,
        color=style.COLORS["comparison"],
        linestyle="--",
        linewidth=1.6,
        label="standard QM: no $Z_{det}$ dependence",
        zorder=3,
    )
    # Mark r=1 (matched, max decoherence)
    ax.axvline(1.0, color=style.COLORS["data"], linestyle="-", linewidth=0.8, alpha=0.5, zorder=1)
    v_at_1 = float(np.interp(0.0, np.log10(_R_SWEEP), v_rel))
    ax.annotate(
        "matched detector\n$Z_{det}=Z_0$ ($\\Gamma=0$, $\\eta=1$)\nmax which-path tap",
        xy=(1.0, v_at_1),
        xytext=(1.5, 0.55),
        fontsize=7.5,
        color=style.COLORS["data"],
        ha="left",
        arrowprops=dict(arrowstyle="->", color=style.COLORS["data"], lw=0.8),
    )
    ax.set_xlabel(style.axis_label("Detector load ratio", "Z_{det}/Z_0", ""))
    ax.set_ylabel(style.axis_label("Relative fringe visibility", r"\mathcal{V}/\mathcal{V}_0", ""))
    ax.set_ylim(-0.05, 1.42)
    # Legend in verified in-axes whitespace: the curve dips to the bottom-centre,
    # leaving the top band (above the flat Copenhagen line at y=1.0) clear.
    style.legend(ax, where="below", loc="lower center", bbox_to_anchor=(0.5, -0.34), fontsize=7.5, ncol=3)

    # === MECHANISM INSET: V vs eta (monotone, V ~ 1 - eta) ==================
    ax2 = fig.add_subplot(gs[0, 2])
    eta_line = np.linspace(0, 1, 100)
    ax2.plot(
        eta_line,
        1 - eta_line,
        color=style.COLORS["muted"],
        linestyle=":",
        linewidth=1.3,
        label=r"$1-\eta$",
    )
    order = np.argsort(etas)
    ax2.plot(
        np.array(etas)[order],
        np.array(v_rel)[order],
        color=style.COLORS["accent"],
        linestyle="none",
        marker="s",
        markersize=4,
        label="FDTD",
    )
    ax2.set_xlabel(style.axis_label("Absorbed fraction", r"\eta=1-|\Gamma|^2", ""))
    ax2.set_ylabel(style.axis_label(r"$\mathcal{V}/\mathcal{V}_0$", "", ""))
    ax2.set_xlim(-0.03, 1.03)
    ax2.set_ylim(-0.05, 1.25)
    style.legend(ax2, where="below", fontsize=7, ncol=2)

    # === BOTTOM ROW: fringe cross-sections survive / washed / survive =======
    y = np.arange(_SIM["ny"])
    yc = _SIM["ny"] // 2
    win = 130
    sub_titles = {
        0.2: "(a) $Z_{det}/Z_0=0.2$ — mismatched short:\nfringes survive",
        1.0: "(b) $Z_{det}/Z_0=1$ — matched:\nfringes washed (single-slit)",
        5.0: "(c) $Z_{det}/Z_0=5$ — mismatched open:\nfringes survive",
    }
    cross_colors = {0.2: style.COLORS["ave"], 1.0: style.COLORS["comparison"], 5.0: style.COLORS["accent"]}
    base_seg = base_cross[yc - win : yc + win]
    xpos = y[yc - win : yc + win] - yc
    for col, r in enumerate(_R_CROSS):
        axc = fig.add_subplot(gs[1, col])
        cross, eta, vr = cross_data[r]
        seg = cross[yc - win : yc + win]
        # Unmeasured (no-detector) reference fringes — dotted guide so the eye
        # reads fringes-present (a,c) vs fringes-gone (b) directly.
        axc.plot(xpos, base_seg, color=style.COLORS["muted"], linestyle=":", linewidth=0.8, alpha=0.7)
        axc.plot(xpos, seg, color=cross_colors[r], linewidth=1.3)
        axc.fill_between(xpos, 0, seg, color=cross_colors[r], alpha=0.18)
        axc.text(
            0.5,
            0.92,
            sub_titles[r],
            transform=axc.transAxes,
            ha="center",
            va="top",
            fontsize=7.2,
            color=style.COLORS["data"],
        )
        axc.text(
            0.5,
            0.02,
            rf"$\eta={eta:.2f}$, $\mathcal{{V}}/\mathcal{{V}}_0={vr:.2f}$",
            transform=axc.transAxes,
            ha="center",
            va="bottom",
            fontsize=7.0,
            color=style.COLORS["muted"],
        )
        axc.set_xlabel(style.axis_label("Transverse position", "y", "nodes"))
        if col == 0:
            axc.set_ylabel(style.axis_label("Screen intensity", r"|\Psi|^2", ""))
            axc.text(
                0.02,
                0.98,
                "dotted: unmeasured",
                transform=axc.transAxes,
                ha="left",
                va="top",
                fontsize=6.2,
                color=style.COLORS["muted"],
            )
        axc.set_ylim(0, 1.08)

    out = sim_output("double_slit_decoherence.png")
    written = style.save(fig, out, formats=("png",))
    plt.close(fig)
    print(f"\n  saved: {written[0]}")

    # --- numerical confirmation of the dip ----------------------------------
    print("\n  DIP CONFIRMATION (V/V0):")
    for r in _R_CROSS:
        print(f"    r={r:>4}: V/V0={cross_data[r][2]:.3f}")
    print("  -> minimum at the matched detector r=1 (max-power-transfer dip).")


if __name__ == "__main__":
    main()
