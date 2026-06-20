"""Fork-B Saturation-Tank Mass Confinement — reproducible figure driver.

Generates the THREE prereg-mandated figures FROM THE ACTUAL RUN of the Fork-B
solver (research/2026-06-20_fork-b-saturation-tank-confinement_prereg.md §2):

  fig1_confinement_vs_gamma_depth.png  — confinement (core_frac) vs Γ-depth, the
      S_min AND A_cap sweeps (RF-3 DEPTH: partial-short-binds vs floor-dropped).
  fig2_scramble_arms.png               — GATE2 baseline vs ARM-A / ARM-B / control.
  fig3_quarter_arc_shape.png           — GATE3 canonical-vs-comparator Δ/L + the
      null-shape control + size-convergence (the shape-generic ECHO).

Run:  PYTHONPATH=src python research/figures/2026-06-20-fork-b-saturation-tank/make_figures.py
alpha-FREE (the solver is alpha-free; these are pure plots of its output).
"""

from __future__ import annotations

import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from ave.solvers.fork_b_saturation_tank import (
    ConfinementConfig,
    electron_anchor_check,
    gamma_from_S_floor,
    quarter_arc_size_convergence,
    solve_confinement,
    solve_quarter_arc_shape,
    solve_scramble,
)

HERE = os.path.dirname(os.path.abspath(__file__))


def fig1_confinement_vs_gamma_depth(net: str = "diamond", L: int = 8) -> str:
    """Confinement-vs-Γ-depth curve (RF-3 DEPTH). Two panels: (a) core_frac vs the
    reachable Γ (the S_min floor sweep); (b) core_frac vs the A_cap clip sweep —
    shows whether a PARTIAL short binds or binding needs floor-dropping."""
    S_mins = [0.5, 0.2, 0.1, 0.05, 1e-2, 1e-3, 1e-4]
    gammas, cf_floor, conf_floor = [], [], []
    for sm in S_mins:
        r = solve_confinement(ConfinementConfig(net=net, L=L, S_min=sm))
        gammas.append(gamma_from_S_floor(sm))
        cf_floor.append(r["core_frac"])
        conf_floor.append(r["confined"])

    A_caps = [0.45, 0.6, 0.7, 0.8, 0.9, 0.99]
    cf_cap, conf_cap = [], []
    for ac in A_caps:
        r = solve_confinement(ConfinementConfig(net=net, L=L, S_min=1e-3, A_cap=ac))
        cf_cap.append(r["core_frac"])
        conf_cap.append(r["confined"])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2))
    ax1.plot(gammas, cf_floor, "o-", color="C0", lw=2)
    ax1.axhline(0.50, color="k", ls="--", lw=1, label="core_frac floor 0.50 (RF-1)")
    for g, cf, c in zip(gammas, cf_floor, conf_floor):
        ax1.scatter([g], [cf], s=90, facecolors="none" if not c else "C0",
                    edgecolors="C0", zorder=5)
    ax1.set_xlabel("reachable Γ = (√S_min − 1)/(√S_min + 1)  (gamma_bulk, crystal_engine.py:478)")
    ax1.set_ylabel("bound-mode core_frac")
    ax1.set_title(f"(a) confinement vs Γ-depth (S_min sweep)\n{net} L={L}: a PARTIAL short binds")
    ax1.set_ylim(0, 1.05)
    ax1.legend(fontsize=8)
    ax1.grid(alpha=0.3)

    ax2.plot(A_caps, cf_cap, "s-", color="C3", lw=2)
    ax2.axhline(0.50, color="k", ls="--", lw=1)
    for ac, cf, c in zip(A_caps, cf_cap, conf_cap):
        ax2.scatter([ac], [cf], s=90, facecolors="none" if not c else "C3",
                    edgecolors="C3", zorder=5)
    ax2.set_xlabel("A_cap (kernel clip, crystal_engine.py:194)")
    ax2.set_ylabel("bound-mode core_frac")
    ax2.set_title(f"(b) confinement vs A_cap clip (S_min=1e-3)\nbinds for A_cap ≳ 0.8 (open marker = NOT confined)")
    ax2.set_ylim(0, 1.05)
    ax2.grid(alpha=0.3)

    fig.suptitle("Fork-B GATE1 — confinement-vs-Γ-depth (RF-3 DEPTH): the partial short binds at the canonical floor",
                 fontsize=10)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    out = os.path.join(HERE, "fig1_confinement_vs_gamma_depth.png")
    fig.savefig(out, dpi=140)
    plt.close(fig)
    return out


def fig2_scramble_arms(nets=(("diamond", 8), ("srs", 4), ("srs", 6))) -> str:
    """GATE2 scramble: baseline (graded) vs ARM-A (S→1) / ARM-B (histogram-preserving
    permutation) / negative control, per net. The de-confinement (core_frac drop)
    proves the confinement is S-STRUCTURE-decided, NOT a BC/projector tautology."""
    labels = []
    base, armA, armB = [], [], []
    ctrl_noop, armB_survives = [], []
    for net, L in nets:
        r = solve_scramble(ConfinementConfig(net=net, L=L))
        labels.append(f"{net}\nL={L}")
        base.append(r["baseline_core_frac"])
        armA.append(r["armA_uniform_core_frac"])
        armB.append(r["armB_permute_core_frac"])
        ctrl_noop.append(r["negative_control_is_noop"])
        armB_survives.append(r["armB_survives_AUTO_VOID"])

    x = np.arange(len(labels))
    w = 0.25
    fig, ax = plt.subplots(figsize=(9, 4.6))
    ax.bar(x - w, base, w, label="baseline (graded S-structure)", color="C0")
    ax.bar(x, armA, w, label="ARM-A: S→1 uniform", color="C1")
    ax.bar(x + w, armB, w, label="ARM-B: permute S (histogram fixed)", color="C3")
    ax.axhline(0.50, color="k", ls="--", lw=1, label="core_frac floor 0.50")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("bound-mode core_frac")
    ax.set_ylim(0, 1.1)
    ax.set_title(
        "Fork-B GATE2 — scramble de-confines (anti-tautology)\n"
        "ARM-A AND ARM-B both collapse core_frac (margin ≥ 0.30) ⇒ S-STRUCTURE-decided, NOT VOID\n"
        f"(negative control no-op: {all(ctrl_noop)}; ARM-B survives: {any(armB_survives)} = no tautology)"
    )
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(alpha=0.3, axis="y")
    fig.tight_layout()
    out = os.path.join(HERE, "fig2_scramble_arms.png")
    fig.savefig(out, dpi=140)
    plt.close(fig)
    return out


def fig3_quarter_arc_shape() -> str:
    """GATE3 quarter-arc shape: (a) canonical-vs-comparator Δ/L per net (the gap is
    ~0 = shape-generic ECHO); (b) the size-convergence of the gap + the ω anchor
    (NOT converging to 2.87) — the headline ECHO evidence."""
    nets = [("diamond", 8), ("srs", 4), ("srs", 6)]
    canon, comp, gaps, nulls = [], [], [], []
    labels = []
    for net, L in nets:
        r = solve_quarter_arc_shape(ConfinementConfig(net=net, L=L))
        labels.append(f"{net}\nL={L}")
        canon.append(r["delta_over_L_canonical"])
        comp.append(r["delta_over_L_comparator"])
        gaps.append(r["shape_gap"])
        nulls.append(r["null_gap"])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.4))
    x = np.arange(len(labels))
    w = 0.35
    ax1.bar(x - w / 2, canon, w, label="canonical quarter-arc p=0.5 (=√(1−A²))", color="C0")
    ax1.bar(x + w / 2, comp, w, label="comparator (1−A²)^p, norm+depth-matched", color="C2")
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels)
    ax1.set_ylabel("Δ/L = √(Σr²|ψ|²/Σ|ψ|²)/L  (depth-invariant)")
    ax1.set_title("(a) canonical vs comparator Δ/L\nIDENTICAL ⇒ shape-generic (ECHO)")
    ax1.legend(fontsize=8)
    ax1.grid(alpha=0.3, axis="y")

    # size-convergence of the gap + the omega anchor
    sc = quarter_arc_size_convergence("srs", [2, 4, 6])
    Ls = [row["L"] for row in sc["rows"]]
    gaps_L = [row["shape_gap"] for row in sc["rows"]]
    anc = electron_anchor_check("srs", [2, 4, 6])
    anc_Ls = [L for L, _ in anc["omegas"]]
    anc_w = [w for _, w in anc["omegas"]]

    ax2.plot(Ls, np.array(gaps_L) * 100, "o-", color="C3", lw=2, label="shape gap (%)")
    ax2.axhline(10.0, color="k", ls="--", lw=1, label="10% CHORD threshold")
    ax2.set_xlabel("connect-map size L")
    ax2.set_ylabel("shape gap (%)", color="C3")
    ax2.tick_params(axis="y", labelcolor="C3")
    ax2.set_ylim(-1, 12)
    axb = ax2.twinx()
    axb.plot(anc_Ls, anc_w, "s-", color="C0", lw=2, label="bound-mode ω (srs)")
    axb.axhline(2.87, color="C0", ls=":", lw=1.5, label="cold-cage anchor ω≈2.87")
    axb.set_ylabel("bound-mode ω", color="C0")
    axb.tick_params(axis="y", labelcolor="C0")
    ax2.set_title("(b) size-convergence + electron anchor\ngap stays ~0; ω does NOT converge to 2.87 (no anchor)")
    lines1, lab1 = ax2.get_legend_handles_labels()
    lines2, lab2 = axb.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, lab1 + lab2, fontsize=7, loc="center right")
    ax2.grid(alpha=0.3)

    fig.suptitle("Fork-B GATE3 — quarter-arc shape-generic + no electron anchor ⇒ ECHO (FORM-chord)", fontsize=10)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    out = os.path.join(HERE, "fig3_quarter_arc_shape.png")
    fig.savefig(out, dpi=140)
    plt.close(fig)
    return out


if __name__ == "__main__":
    p1 = fig1_confinement_vs_gamma_depth()
    p2 = fig2_scramble_arms()
    p3 = fig3_quarter_arc_shape()
    print("Fork-B figures written:")
    for p in (p1, p2, p3):
        print(f"  {p}")
