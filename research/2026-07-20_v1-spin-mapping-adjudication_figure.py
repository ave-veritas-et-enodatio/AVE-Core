"""White-style figure for the v1 spin-mapping frozen adjudication.

Loads the authoritative driver module BY PATH (no formula duplication) so the figure
provably plots the same numbers the verdict cites. House white style via ave.viz.style.

Run:  PYTHONPATH=src python3 research/2026-07-20_v1-spin-mapping-adjudication_figure.py
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np

from ave.viz import style

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    "v1_adj_rerun", HERE / "2026-07-20_v1-spin-mapping-adjudication_rerun.py"
)
R = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(R)


def main() -> None:
    style.apply()  # print profile — white background
    import matplotlib.pyplot as plt

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(9.4, 4.0), constrained_layout=True)

    # continuous curves use the smooth in-lane-verified BCW fit (Kerr ref, <1% vs qnm);
    # the event MARKERS below use kerr_ref (qnm-anchored) — the two differ by <1%, invisible here.
    a = np.linspace(0.60, 0.95, 141)
    kerr_wr = np.array([R.bcw_omega_r_m(x) for x in a])
    v1 = np.array([100 * (R.ave_v1_omega_r_m(x) - kw) / kw for x, kw in zip(a, kerr_wr)])
    v2 = np.array([100 * (R.ave_v2_omega_r_m(x) - kw) / kw for x, kw in zip(a, kerr_wr)])

    # ---- Panel (a): omega_R dimensionless deviation vs corrected Kerr -------------------
    axL.axhspan(-3, 3, color=style.COLORS["muted"], alpha=0.18, label="MATCH band |dev|<3%")
    axL.axhline(0, color=style.COLORS["muted"], lw=0.8)
    axL.axhline(5, color=style.COLORS["muted"], lw=0.6, ls=":")
    axL.axhline(-5, color=style.COLORS["muted"], lw=0.6, ls=":")
    axL.plot(a, v1, color=style.COLORS["ave"], lw=2, label="v1  (retired, whole-cavity)")
    axL.plot(a, v2, color=style.COLORS["comparison"], lw=2, ls="--", label="v2  (retained, 2-component)")
    for name, sp in R.PRIMARY:
        axL.plot(sp, 100 * (R.ave_v1_omega_r_m(sp) - R.kerr_ref(sp)[0]) / R.kerr_ref(sp)[0],
                 "o", color=style.COLORS["ave"], ms=7)
    for name, sp in R.SECONDARY:
        axL.plot(sp, 100 * (R.ave_v1_omega_r_m(sp) - R.kerr_ref(sp)[0]) / R.kerr_ref(sp)[0],
                 "s", color=style.COLORS["accent"], ms=7)
    axL.text(0.615, 4.1, "primary (○) / secondary (■)", fontsize=8, color=style.COLORS["data"])
    axL.text(0.03, 0.04, "(a)", transform=axL.transAxes, fontsize=11, fontweight="bold")
    axL.set_xlabel(style.axis_label("Final spin", "a_*", ""))
    axL.set_ylabel(r"$\omega_R M$ deviation vs corrected Kerr  [%]")
    axL.set_xlim(0.60, 0.95)
    axL.set_ylim(-22, 8)
    axL.legend(loc="lower left", fontsize=7, frameon=True)

    # ---- Panel (b): quality factor Q vs spin (the tau / damping side) -------------------
    qk = np.array([kw / (2 * R.bcw_omega_i_m(x)) for x, kw in zip(a, kerr_wr)])
    axR.plot(a, qk, color=style.COLORS["data"], lw=2, label="corrected Kerr  Q")
    axR.axhline(R.ELL, color=style.COLORS["ave"], lw=2, ls="--",
                label=r"AVE cold model A  $Q=\ell=2$ (fails $-38\%$)")
    # Model B Q_v1 — CORPUS-PINNED forward chain (Omega = Ch.2 Resultbox 2Mar/(r^2+a^2)^2 at
    # r_Omega, merger leaf:85), frozen-adjudicable (PR #776 finding-0 repair — replaces the earlier
    # reverse-engineered, non-adjudicable point). Marker = Resultbox (corpus comparator); the bar
    # spans the exact-equatorial-ZAMO variant (the genuine, quantified model-form sensitivity, not a
    # rounding artifact). The triangles sit ~5% below Kerr -> tau-FAILS (near-miss), not "hugs Kerr".
    for i, (name, sp) in enumerate(R.PRIMARY):
        wr1 = R.ave_v1_omega_r_m(sp)
        q_rb = wr1 / (2 * R.modelB_omega_i_m(wr1, sp, R.omega_drag_resultbox))
        q_zamo = wr1 / (2 * R.modelB_omega_i_m(wr1, sp, R.omega_drag_zamo))
        lo, hi = min(q_rb, q_zamo), max(q_rb, q_zamo)
        axR.errorbar(sp, q_rb, yerr=[[q_rb - lo], [hi - q_rb]], fmt="v",
                     color=style.COLORS["comparison"], ms=7, capsize=3,
                     label=(r"v1 model B $Q$ ($\Omega$ corpus-pinned; pt=Resultbox, bar=ZAMO)"
                            if i == 0 else None))
    axR.text(0.615, 2.28, r"model B $Q$ $\approx 5\%$ below Kerr $\Rightarrow$ $\tau$-FAILS",
             fontsize=7, color=style.COLORS["comparison"])
    axR.text(0.03, 0.04, "(b)", transform=axR.transAxes, fontsize=11, fontweight="bold")
    axR.set_xlabel(style.axis_label("Final spin", "a_*", ""))
    axR.set_ylabel(r"Quality factor  $Q=\omega_R/(2\omega_I)$")
    axR.set_xlim(0.60, 0.95)
    axR.legend(loc="upper left", fontsize=7, frameon=True)

    out = style.save(fig, HERE / "2026-07-20_v1-spin-mapping-adjudication_figure")
    print("wrote:", *[str(p) for p in out], sep="\n  ")


if __name__ == "__main__":
    main()
