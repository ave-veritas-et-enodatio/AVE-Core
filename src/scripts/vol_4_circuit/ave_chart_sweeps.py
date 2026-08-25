#!/usr/bin/env python3
"""
AVE chart instrument — the five demonstration sweeps.
=====================================================

Driver for the ``ave.viz.ave_chart`` instrument (vol4 circuit-theory chart
axis). Every figure is a projection of the instrument's analytic anchors —
the canonical Gamma(A_0) locus (cvr-reflection-smith.md Sec.2), the
AVE-DISTINCT 1-alpha rim band (Sec.3, clm-rtdmsn), and the z=3 vertex
counting fact (translation-circuit.md:189) — through the plotting machinery
gated by ``src/tests/test_ave_chart.py``. Re-runnable and deterministic.

    PYTHONPATH=$PWD/src python3 src/scripts/vol_4_circuit/ave_chart_sweeps.py

THE FIVE FIGURES:
  1. fig1_three_form_traces   — core/J/B Gamma(A) traces on one chart (the
                                walk picture) + the Gamma-vs-A companion panel
  2. fig2_cold_frequency_locus — cold Gamma(theta) locus of the two-junction
                                composite (the frequency axis)
  3. fig3_graded_family       — Gamma(theta, A) family: the composite biased
                                (line+ends) against a cold feed
  4. fig4_differential_split  — uniform bias pins -1/3 EXACTLY (computed);
                                only differential bias splits the vertex
  5. fig5_occupancy_demo      — envelope orbit A(t) -> chart dwell density
                                (the demo orbit is UNDERIVED-CHOICE)

PARK COMPLIANCE: instrument/engineering only, no ontology claim; the CP^1
one-chart-per-sector canonization stays PARKED
(_orchestration/open-items/2026-08-18-smith-chart-cp1-canonization.md);
whether this build trips the re-open condition is Grant's ruling.

HONESTY (ave-driver-script-honesty): every curve is computed by the tested
module; visibility offsets are drawn AND annotated; the underived choices
(J/B side-assignment, the demo orbit) are labelled ON the figures.

Output: research/figures/2026-08-24-ave-chart-instrument/*.png (+.pdf) — the
research-note gallery convention (dated subdir under research/figures/), since
these are instrument-demo figures cited from the 2026-08-24 research note, not
manuscript-cited renders.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # repo/src on path

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from ave.core.constants import ALPHA  # noqa: E402
from ave.viz import ave_chart, style  # noqa: E402

_REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_OUT = _REPO_ROOT / "research" / "figures" / "2026-08-24-ave-chart-instrument"

# House figure style: print profile, white bg, Okabe-Ito (ave-figure-discipline).
style.apply()

# The three-form palette, fixed once so every figure reads identically.
FORM_STYLE = {
    "core": dict(color=style.COLORS["ave"], lw=2.0,
                 label=r"core: $\Gamma=(\sqrt{S}-1)/(\sqrt{S}+1)$, $0\to-1$ (canonical)"),
    "J": dict(color=style.COLORS["accent"], lw=1.8, ls="--",
              label=r"J (junction-side bias): $-1/3\to-1$ [UNDERIVED side-assignment]"),
    "B": dict(color=style.COLORS["ave"], lw=1.8, ls="-.",
              label=r"B (bond-side bias): $-1/3\to+1$, matched at $A=\sqrt{15}/4$ [UNDERIVED side-assignment]"),
}


# ===========================================================================
# Figure 1 — three-form Gamma(A) traces on one chart (the walk picture)
# ===========================================================================
def fig1_three_form_traces(out: Path) -> dict:
    A = np.linspace(0.0, 1.0, 600)
    fig, (axc, axr) = plt.subplots(1, 2, figsize=(12, 5.6),
                                   gridspec_kw={"width_ratios": [1.15, 1.0]})
    ave_chart.base_chart(axc)
    # all three loci are REAL-AXIS runs; small annotated Im offsets for visibility
    offsets = {"core": 0.0, "J": 0.035, "B": -0.035}
    for form, kw in FORM_STYLE.items():
        ave_chart.plot_bias_trajectory(axc, A, form, im_offset=offsets[form], **kw)
    axc.text(-1.12, -1.12,
             "loci are real-axis runs; J/B drawn at ±0.035 Im offset for visibility only",
             fontsize=6, color=style.COLORS["muted"])
    style.legend(axc, fontsize=6.5, where="below")

    axr.axhline(-1 / 3, color=style.COLORS["muted"], lw=0.8, ls=":",
                label=r"$-1/3$ bare $z=3$ vertex (counting fact)")
    for form, kw in FORM_STYLE.items():
        g = ave_chart.gamma_of_A(A, form)
        axr.plot(A, np.real(g), **{k: v for k, v in kw.items() if k != "label"},
                 label=kw["label"].split(":")[0])
    axr.axvline(ave_chart.A_MATCHED_B, color=style.COLORS["muted"], lw=0.8, ls=":")
    axr.plot([ave_chart.A_MATCHED_B], [0.0], "o", color=style.COLORS["accent"], ms=5)
    axr.annotate(r"B matched crossing $A=\sqrt{15}/4$",
                 xy=(ave_chart.A_MATCHED_B, 0.0), xytext=(0.45, 0.35), fontsize=7,
                 arrowprops=dict(arrowstyle="->", color=style.COLORS["muted"], lw=0.8))
    axr.set_xlabel(style.axis_label("Operating point", r"A_0=|V|/V_{yield}", ""))
    axr.set_ylabel(style.axis_label("Reflection", r"\Gamma(A_0)", ""))
    style.legend(axr, fontsize=7, where="below")
    axr.grid(alpha=0.3)

    style.save(fig, out / "fig1_three_form_traces.png")
    plt.close(fig)
    return {
        "core_endpoints": [float(ave_chart.gamma_of_A(0.0, "core")),
                           float(ave_chart.gamma_of_A(1.0, "core"))],
        "J_endpoints": [float(ave_chart.gamma_of_A(0.0, "J")),
                        float(ave_chart.gamma_of_A(1.0, "J"))],
        "B_endpoints": [float(ave_chart.gamma_of_A(0.0, "B")),
                        float(ave_chart.gamma_of_A(1.0, "B"))],
        "B_matched_crossing_A": float(ave_chart.A_MATCHED_B),
        "B_gamma_at_crossing": float(np.real(
            ave_chart.gamma_of_A(ave_chart.A_MATCHED_B, "B"))),
    }


# ===========================================================================
# Figure 2 — cold Gamma(theta) locus of the two-junction composite
# ===========================================================================
def fig2_cold_frequency_locus(out: Path) -> dict:
    th = np.linspace(0.0, 2.0 * np.pi, 1200)
    g = ave_chart.two_junction_gamma(th)
    fig, ax = plt.subplots(figsize=style.figsize("square"))
    ave_chart.base_chart(ax, annotate=False)
    pts = ax.scatter(g.real, g.imag, c=th / np.pi, cmap=style.CMAP_SEQ, s=4, zorder=2.5)
    cb = fig.colorbar(pts, ax=ax, fraction=0.046, pad=0.04)
    cb.set_label(style.axis_label("Bond electrical length", r"\theta/\pi", ""))
    g0 = ave_chart.two_junction_gamma(0.0)
    ax.plot([g0.real], [g0.imag], "o", color=style.COLORS["accent"], ms=6, zorder=3)
    ax.annotate(r"$\theta=0$: $\Gamma=-3/5$ (both junction pairs in parallel)",
                xy=(g0.real, g0.imag), xytext=(-0.85, -0.75), fontsize=6.5,
                arrowprops=dict(arrowstyle="->", lw=0.8))
    ax.text(-1.12, 1.05, "cold composite: Z$_0$ bond between two z=3 junctions\n"
            "(isolated/incoherent scoping — in-band collective carriers\n"
            "homogenize the bare vertex reflection, translation-circuit.md:189)",
            fontsize=6, color=style.COLORS["muted"])
    style.save(fig, out / "fig2_cold_frequency_locus.png")
    plt.close(fig)
    return {
        "gamma_theta0": [float(g0.real), float(g0.imag)],
        "max_abs_gamma": float(np.max(np.abs(g))),
        "min_abs_gamma": float(np.min(np.abs(g))),
    }


# ===========================================================================
# Figure 3 — Gamma(theta, A) graded family (composite biased vs cold feed)
# ===========================================================================
def fig3_graded_family(out: Path) -> dict:
    th = np.linspace(0.0, 2.0 * np.pi, 1200)
    A_family = [0.0, 0.5, 0.8, 0.95, 0.99]
    cmap = plt.get_cmap(style.CMAP_SEQ)
    fig, ax = plt.subplots(figsize=style.figsize("square"))
    ave_chart.base_chart(ax, annotate=False)
    finals = {}
    for i, A in enumerate(A_family):
        col = cmap(0.15 + 0.7 * i / (len(A_family) - 1))
        ave_chart.plot_frequency_locus(ax, th, A_line=A, A_ends=A, color=col,
                                       lw=1.4, label=fr"$A={A}$")
        finals[str(A)] = float(np.max(np.abs(
            ave_chart.two_junction_gamma(th, A_line=A, A_ends=A))))
    ax.text(-1.12, 1.05, "composite (line+ends) biased by the SAME A against a COLD feed —\n"
            "a differential boundary at the feed plane; the locus collapses toward\n"
            r"the $\Gamma=-1$ rim as the biased patch shorts",
            fontsize=6, color=style.COLORS["muted"])
    style.legend(ax, fontsize=7, where="below", ncol=3)
    style.save(fig, out / "fig3_graded_family.png")
    plt.close(fig)
    return {"max_abs_gamma_by_A": finals}


# ===========================================================================
# Figure 4 — differential-bias split vs the exact uniform -1/3
# ===========================================================================
def fig4_differential_split(out: Path) -> dict:
    A = np.linspace(0.0, 0.999999, 800)
    g_uniform = ave_chart.gamma_two_junction_uniform(A)
    fig, ax = plt.subplots(figsize=style.figsize("single"))
    ax.plot(A, g_uniform, "-", color=style.COLORS["ave"], lw=2.2,
            label=r"UNIFORM bias: $\Gamma=-1/3$ exact at all $A$ (computed ratio)")
    for form in ("J", "B"):
        kw = FORM_STYLE[form]
        ax.plot(A, np.real(ave_chart.gamma_of_A(A, form)),
                color=kw["color"], lw=kw["lw"], ls=kw.get("ls", "-"),
                label=kw["label"].split(" [")[0] + " (differential)")
    ax.axvline(ave_chart.A_MATCHED_B, color=style.COLORS["comparison"], lw=0.8, ls=":")
    ax.text(0.02, 0.95,
            "uniform bias: every impedance rescales by the same $\\sqrt{S}$ —\n"
            "the bilinear map cancels it; the chart is blind to uniform\n"
            "medium changes (self-cancellation as geometry). Only a\n"
            "DIFFERENTIAL bias splits the $-1/3$ vertex reflection.",
            fontsize=6.5, transform=ax.transAxes, va="top",
            bbox=dict(boxstyle="round", fc="white", ec=style.COLORS["muted"], alpha=0.85))
    ax.set_xlabel(style.axis_label("Operating point", r"A", ""))
    ax.set_ylabel(style.axis_label("Vertex reflection", r"\Gamma", ""))
    style.legend(ax, fontsize=7, where="below")
    ax.grid(alpha=0.3)
    style.save(fig, out / "fig4_differential_split.png")
    plt.close(fig)
    dev = float(np.max(np.abs(g_uniform + 1.0 / 3.0)))
    return {"uniform_max_deviation_from_minus_third": dev,
            "J_span": [float(np.real(ave_chart.gamma_of_A(0.0, "J"))),
                       float(np.real(ave_chart.gamma_of_A(0.999999, "J")))],
            "B_span": [float(np.real(ave_chart.gamma_of_A(0.0, "B"))),
                       float(np.real(ave_chart.gamma_of_A(0.999999, "B")))]}


# ===========================================================================
# Figure 5 — occupancy demo: envelope orbit A(t) -> chart dwell density
# ===========================================================================
def fig5_occupancy_demo(out: Path) -> dict:
    # ------------------------------------------------------------------
    # UNDERIVED-CHOICE: the demo orbit below is an ILLUSTRATIVE envelope,
    # not a derived substrate trajectory. A(t) = A0 + a*sin(Omega*t) with
    # (A0, a) chosen to sweep a wide chart arc. The instrument maps whatever
    # orbit it is handed; deriving a physical A(t) is engine-lane work.
    # ------------------------------------------------------------------
    t = np.linspace(0.0, 200.0 * np.pi, 400_000)
    A0, a = 0.55, 0.42
    A_t = A0 + a * np.sin(t)

    fig, (axc, axh) = plt.subplots(1, 2, figsize=(12, 5.6),
                                   gridspec_kw={"width_ratios": [1.15, 1.0]})
    ave_chart.base_chart(axc, annotate=False)
    hb, _ = ave_chart.plot_occupancy(axc, A_t, "core", ax_hist=axh, bins=80)
    cb = fig.colorbar(hb, ax=axc, fraction=0.046, pad=0.04)
    cb.set_label(style.axis_label("Dwell count", "N", "samples"))
    axc.text(-1.12, 1.02,
             "occupancy of the demo envelope orbit  $A(t)=A_0+a\\sin\\Omega t$\n"
             "($A_0=0.55$, $a=0.42$) — UNDERIVED-CHOICE demo orbit, not a\n"
             "derived substrate trajectory; locus form = canonical 'core'",
             fontsize=6, color=style.COLORS["muted"])
    axh.axvline(float(np.real(ave_chart.gamma_of_A(A0 - a, "core"))),
                color=style.COLORS["muted"], lw=0.8, ls=":")
    axh.axvline(float(np.real(ave_chart.gamma_of_A(A0 + a, "core"))),
                color=style.COLORS["muted"], lw=0.8, ls=":")
    axh.text(0.03, 0.92, "dwell peaks at the envelope turning\npoints (as for any orbit)",
             fontsize=6.5, transform=axh.transAxes)
    axh.grid(alpha=0.3)
    style.save(fig, out / "fig5_occupancy_demo.png")
    plt.close(fig)
    g_lo = float(np.real(ave_chart.gamma_of_A(A0 + a, "core")))
    g_hi = float(np.real(ave_chart.gamma_of_A(A0 - a, "core")))
    return {"orbit": "A(t)=0.55+0.42*sin(t)  [UNDERIVED-CHOICE demo]",
            "gamma_range": [g_lo, g_hi]}


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("--outdir", type=Path, default=DEFAULT_OUT,
                    help="figure output directory (default: the dated research/figures gallery)")
    args = ap.parse_args(argv)
    out: Path = args.outdir
    out.mkdir(parents=True, exist_ok=True)

    metrics = {
        "_alpha": ALPHA,
        "_gamma_wall": ave_chart.GAMMA_WALL,
        "fig1_three_form_traces": fig1_three_form_traces(out),
        "fig2_cold_frequency_locus": fig2_cold_frequency_locus(out),
        "fig3_graded_family": fig3_graded_family(out),
        "fig4_differential_split": fig4_differential_split(out),
        "fig5_occupancy_demo": fig5_occupancy_demo(out),
    }
    (out / "ave_chart_sweeps_metrics.json").write_text(json.dumps(metrics, indent=2))
    print(json.dumps(metrics, indent=2))
    print(f"\n[OK] 5 figures -> {out}")


if __name__ == "__main__":
    main()
