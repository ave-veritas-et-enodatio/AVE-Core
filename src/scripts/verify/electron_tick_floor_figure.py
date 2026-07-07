"""House-style (WHITE) figure for the electron tick-floor arc.

Two panels (no baked title -- caption belongs in the LaTeX/RESULT):
  (A) the SAMPLING FLOOR -- the engine's tick-sampled winding pair (w2, w3) vs division N.
      Below N_min=7 the k=3 winding aliases (N=5 -> -2 [COLLIDE], N=6 -> Nyquist-marginal);
      at N>=7 both windings read their true (2,3). This is the substrate-forced floor.
  (B) the LOSSLESS LOCK-RANGE finding -- the conservative (Ax3) lock half-range GROWS with N
      (~sqrt(N)), the OPPOSITE of the first-order dissipative Adler kappa/N. => no high-N
      lock ceiling in the lossless substrate (window routes FLOOR-ONLY).

alpha-CLEAN: no physical constant on this path (dimensionless integers + method couplings).
"""
from __future__ import annotations

import os
import sys

import matplotlib.pyplot as plt
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import electron_tick_floor_engine as eng  # noqa: E402
from ave.viz import style  # noqa: E402


def build_figure():
    style.apply()  # white print profile (house default)
    cfg = eng.LatticeConfig()
    mi = eng.measurement_i(cfg, n_lo=4, n_hi=16, spots=())
    mii = eng.measurement_ii(cfg)

    Ns = sorted(int(N) for N in mi["sweep"])
    w2 = [mi["sweep"][str(N)]["w2"] for N in Ns]
    w3 = [mi["sweep"][str(N)]["w3"] for N in Ns]

    fig, (axA, axB) = plt.subplots(1, 2, figsize=(9.2, 3.9))

    # --- Panel A: the sampling floor ---
    axA.axvspan(3.5, 6.5, color=style.COLORS["muted"], alpha=0.15, zorder=0)
    axA.axhline(2, ls=":", lw=1, color=style.COLORS["muted"])
    axA.axhline(3, ls=":", lw=1, color=style.COLORS["muted"])
    axA.plot(Ns, w2, "o-", color=style.COLORS["ave"], label="measured $k_1$ winding")
    axA.plot(Ns, w3, "s-", color=style.COLORS["comparison"], label="measured $k_2$ winding")
    axA.axvline(7, ls="--", lw=1.2, color=style.COLORS["accent"])
    axA.annotate("$N_{\\min}=7$", xy=(7, -2.4), xytext=(8.2, -2.4),
                 color=style.COLORS["accent"], fontsize=9, va="center")
    axA.set_xlabel(style.axis_label("Division ratio", "N", "ticks/period"))
    axA.set_ylabel(style.axis_label("Read winding number", "k_{\\rm read}", "1"))
    axA.set_yticks([-2, -1, 0, 1, 2, 3])
    axA.legend(loc="lower right", frameon=False, fontsize=8)

    # --- Panel B: the lossless lock-range finding ---
    lr = mii["lock_range_vs_N"]
    Nl = sorted(int(N) for N in lr)
    cons = [lr[str(N)]["conservative_halfrange_delta"] for N in Nl]
    adler = [lr[str(N)]["first_order_adler_kappa_over_N"] for N in Nl]
    sqrtref = 3.5316 * np.sqrt(np.array(Nl, float) / 7.0)  # sqrt-law ref anchored at N=7
    axB.plot(Nl, cons, "o-", color=style.COLORS["ave"],
             label="conservative (lossless) half-range")
    axB.plot(Nl, sqrtref, "-", lw=1, color=style.COLORS["muted"], label=r"$\propto\sqrt{N}$ ref")
    axB.plot(Nl, adler, "s--", color=style.COLORS["comparison"],
             label=r"1st-order Adler $\kappa/N$")
    axB.set_yscale("log")
    axB.set_xlabel(style.axis_label("Division ratio", "N", "ticks/period"))
    axB.set_ylabel(style.axis_label("Lock half-range", "\\Delta_{\\rm lock}", "1"))
    axB.legend(loc="center right", frameon=False, fontsize=8)

    return fig


def main():
    fig = build_figure()
    outdir = os.path.join(_HERE, "..", "..", "..", "research", "figures",
                          "2026-07-07-electron-tick-floor")
    outdir = os.path.abspath(outdir)
    os.makedirs(outdir, exist_ok=True)
    paths = style.save(fig, os.path.join(outdir, "electron_tick_floor"))
    print("wrote:", *[str(p) for p in paths])


if __name__ == "__main__":
    main()
