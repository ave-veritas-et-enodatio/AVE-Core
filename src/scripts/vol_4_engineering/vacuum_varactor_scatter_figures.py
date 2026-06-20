"""Figures for the VACUUM-VARACTOR SCATTER OPERATOR (PR#305, Class-C / consistency).

Generated FROM THE ACTUAL OPERATOR (src/ave/solvers/vacuum_varactor_scatter.py) and
the canonical Axiom-4 kernel (delegated to CrystalEngine.saturation_kernel) — NOT
hand-drawn. Reproducible / deterministic (fixed RNG seeds via VaractorConfig).

Result doc : research/2026-06-20_vacuum-varactor-scatter_result.md
KB leaf    : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/
             vacuum-varactor-scatter-operator.md

Four figures (saved to ./_output/):
  (a) vvs_fig_a_gamma_vs_A.png      — Γ(A) varactor curve: μ-load (confinement,
                                       Γ→-1) vs FORBIDDEN ε-load mirror (Γ→+1);
                                       A_cap=0.99 floor (Γ≈-0.45) + Γ=0 (vacuum) marked.
  (b) vvs_fig_b_scramble.png         — max|dScatter| under per-BOND scramble (>0) vs
                                       per-NODE scramble (~0) vs uniform-field
                                       scramble (~0, negative control): "reads saturation".
  (c) vvs_fig_c_bedrock_spectrum.png — bedrock recovery at S=1 (scatter==(2/n)J-I)
                                       + local-node spectra {+1,-1,-1} (srs) / {+1,-1,-1,-1} (dia).
  (d) vvs_fig_d_sat_admittance.png   — the varactor map: S(A)=sqrt(1-A^2) and
                                       Y_bond=Y0/sqrt(S) vs A.

Run:  PYTHONPATH=src python3 src/scripts/vol_4_engineering/vacuum_varactor_scatter_figures.py
"""

from __future__ import annotations

import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

# Make the ave package importable when run as a bare script.
_REPO_SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))
if _REPO_SRC not in sys.path:
    sys.path.insert(0, _REPO_SRC)

from ave.core.chiral_lattice import build_diamond_net, build_srs_net, scatter_matrix  # noqa: E402
from ave.solvers.node_scattering_multiplicity import assemble_global_scattering  # noqa: E402
from ave.solvers.vacuum_varactor_scatter import (  # noqa: E402
    VaractorConfig,
    admittance_scatter,
    assemble_varactor_scattering,
    bond_admittance_from_saturation,
    saturation_kernel,
)

OUT = os.path.join(os.path.dirname(__file__), "_output")
os.makedirs(OUT, exist_ok=True)

A_CAP = 0.99  # the canonical amplitude clip (the BINDING floor parameter)
DPI = 130


# ─────────────────────────────────────────────────────────────────────────────
# (a) Γ-vs-A varactor curve — μ-load (confinement) vs forbidden ε-load mirror.
# ─────────────────────────────────────────────────────────────────────────────
def fig_a_gamma_vs_A() -> str:
    """Γ(A) for the μ-load Z=Z0·√S(A), S(A)=√(1-A²), A in [0,1). μ-load → Γ→-1
    (mass-cage short, confinement). Overlay the FORBIDDEN ε-load mirror Z=Z0/√S → Γ→+1.
    Mark the A_cap=0.99 floor (Γ≈-0.45) and Γ=0 (vacuum matched).

    All Γ values are computed via the ACTUAL kernel saturation_kernel (un-clipped here,
    A_cap dropped, so the full curve toward ±1 is visible); the A_cap floor is marked
    as the operative limit the deployed operator actually reaches."""
    # un-clip the kernel so the full A→1 trend is visible (A_cap→1, S_min→0)
    A = np.linspace(0.0, 0.9995, 600)
    S = saturation_kernel(A, A_cap=0.999999, S_min=1e-12)
    Z_mu = np.sqrt(S)  # μ-load: Z=Z0·√S → 0
    Z_eps = 1.0 / np.sqrt(S)  # FORBIDDEN ε-load: Z=Z0/√S → ∞
    g_mu = (Z_mu - 1.0) / (Z_mu + 1.0)
    g_eps = (Z_eps - 1.0) / (Z_eps + 1.0)

    # the OPERATIVE floor the deployed operator reaches (A clipped at A_cap=0.99)
    S_cap = float(saturation_kernel(np.array(A_CAP)))
    Z_cap = np.sqrt(S_cap)
    g_floor = (Z_cap - 1.0) / (Z_cap + 1.0)  # ≈ -0.454

    fig, ax = plt.subplots(figsize=(8.2, 5.2))
    ax.plot(A, g_mu, color="#1f6fb2", lw=2.2, label=r"$\mu$-load (confinement): $Z=Z_0\sqrt{S}\to0,\ \Gamma\to-1$")
    ax.plot(
        A,
        g_eps,
        color="#c0392b",
        lw=2.0,
        ls="--",
        label=r"$\varepsilon$-load (FORBIDDEN): $Z=Z_0/\sqrt{S}\to\infty,\ \Gamma\to+1$",
    )
    ax.axhline(0.0, color="grey", lw=1.0, ls=":")
    ax.axhline(-1.0, color="#1f6fb2", lw=0.9, ls=":", alpha=0.6)
    ax.axhline(+1.0, color="#c0392b", lw=0.9, ls=":", alpha=0.6)

    # mark Γ=0 (vacuum matched) at A=0
    ax.plot(0.0, 0.0, "o", color="k", ms=6)
    ax.annotate(
        "vacuum matched\n$\\Gamma=0$ (A=0)",
        xy=(0.0, 0.0),
        xytext=(0.07, 0.28),
        fontsize=8.5,
        arrowprops=dict(arrowstyle="->", lw=0.9),
    )

    # mark the A_cap=0.99 operative floor (Γ≈-0.45)
    ax.plot(A_CAP, g_floor, "s", color="#1f6fb2", ms=7)
    ax.annotate(
        f"$A_{{cap}}=0.99$ operative floor\n$\\Gamma\\approx{g_floor:.3f}$",
        xy=(A_CAP, g_floor),
        xytext=(0.55, -0.30),
        fontsize=8.5,
        arrowprops=dict(arrowstyle="->", lw=0.9),
    )

    ax.set_xlabel(r"saturation amplitude $A=|V|/V_{yield}$")
    ax.set_ylabel(r"reflection coefficient $\Gamma=(Z-1)/(Z+1)$")
    ax.set_title(
        "Vacuum-varactor $\\Gamma(A)$: $\\mu$-load = confinement ($\\Gamma\\to-1$), "
        "$\\varepsilon$-load = FORBIDDEN ($\\Gamma\\to+1$)"
    )
    ax.set_ylim(-1.15, 1.15)
    ax.set_xlim(0.0, 1.0)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8.5, loc="center left")
    p = os.path.join(OUT, "vvs_fig_a_gamma_vs_A.png")
    fig.tight_layout()
    fig.savefig(p, dpi=DPI)
    plt.close(fig)
    return p


# ─────────────────────────────────────────────────────────────────────────────
# (b) Scramble demonstration — the "reads saturation" deliverable.
# ─────────────────────────────────────────────────────────────────────────────
def _scramble_maxd(net, A, kind: str, seed: int) -> float:
    """Return max|dScatter| under a scramble of `kind` in {'bond','node','uniform'}.

    'bond'    : per-directed-bond field, permuted across ALL bonds → the operator
                MUST change (reads the per-bond gradient).
    'node'    : per-NODE field (uniform within each node), permuted across nodes →
                the operator MUST NOT change (per-node-uniform cancels).
    'uniform' : a single constant field, permuted → trivially unchanged (control)."""
    rng = np.random.default_rng(seed)
    N, d = net.n_nodes, net.degree
    if kind == "bond":
        base = rng.uniform(0.2, 0.9, size=(N, d))
        flat = base.ravel().copy()
        rng.shuffle(flat)
        scram = flat.reshape(N, d)
    elif kind == "node":
        node_vals = rng.uniform(0.2, 0.9, size=N)
        base = np.repeat(node_vals[:, None], d, axis=1)
        perm = rng.permutation(N)
        scram = np.repeat(node_vals[perm][:, None], d, axis=1)
    elif kind == "uniform":
        base = np.full((N, d), 0.7)
        flat = base.ravel().copy()
        rng.shuffle(flat)
        scram = flat.reshape(N, d)
    else:
        raise ValueError(kind)
    S_base = assemble_varactor_scattering(net, base)
    S_scram = assemble_varactor_scattering(net, scram)
    return float(np.max(np.abs(S_base - S_scram)))


def fig_b_scramble() -> str:
    """Bar comparison of max|dScatter| under per-BOND vs per-NODE vs uniform-field
    scramble, for srs (L=2) and diamond (L=4). per-BOND > 0 (reads saturation);
    per-NODE ≈ 0 and uniform ≈ 0 (the negative controls)."""
    cfg = VaractorConfig()
    srs = build_srs_net(L=cfg.L_srs)
    dia = build_diamond_net(L=cfg.L_diamond)

    kinds = ["bond", "node", "uniform"]
    labels = ["per-BOND\n(reads sat.)", "per-NODE\n(cancels)", "uniform field\n(control)"]
    srs_vals = [_scramble_maxd(srs, None, k, cfg.scramble_seed + 99) for k in kinds]
    dia_vals = [_scramble_maxd(dia, None, k, cfg.scramble_seed + 99) for k in kinds]

    x = np.arange(len(kinds))
    w = 0.36
    fig, ax = plt.subplots(figsize=(8.2, 5.0))
    b1 = ax.bar(x - w / 2, srs_vals, w, color="#1f6fb2", label="srs (L=2)")
    b2 = ax.bar(x + w / 2, dia_vals, w, color="#27ae60", label="diamond (L=4)")
    ax.set_yscale("symlog", linthresh=1e-14)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel(r"$\max|\Delta\mathcal{S}|$ under scramble (symlog)")
    ax.set_title("Scramble test: the operator READS saturation only via the per-BOND gradient")
    ax.axhline(1e-9, color="grey", ls=":", lw=1.0, label="change threshold $10^{-9}$")
    ax.grid(axis="y", alpha=0.3)
    ax.legend(fontsize=8.5)
    for bars, vals in ((b1, srs_vals), (b2, dia_vals)):
        for rect, v in zip(bars, vals):
            ax.annotate(
                f"{v:.2e}",
                xy=(rect.get_x() + rect.get_width() / 2, max(v, 1e-14)),
                xytext=(0, 3),
                textcoords="offset points",
                ha="center",
                fontsize=7.5,
                rotation=0,
            )
    p = os.path.join(OUT, "vvs_fig_b_scramble.png")
    fig.tight_layout()
    fig.savefig(p, dpi=DPI)
    plt.close(fig)
    return p


# ─────────────────────────────────────────────────────────────────────────────
# (c) Bedrock recovery at S=1 + local-node scatter spectra.
# ─────────────────────────────────────────────────────────────────────────────
def fig_c_bedrock_spectrum() -> str:
    """At S=1 (A=0) the assembled varactor operator == the bedrock (2/n)J-I; show
    max|d| (bit/roundoff) per net, and the LOCAL-NODE scatter spectra
    {+1,-1,-1} (srs, degree 3) and {+1,-1,-1,-1} (diamond, degree 4)."""
    srs = build_srs_net(L=2)
    dia = build_diamond_net(L=4)

    # bedrock recovery at S=1 (A=0)
    recoveries = {}
    for net in (srs, dia):
        bed = assemble_global_scattering(net)
        var = assemble_varactor_scattering(net, 0.0)
        recoveries[net.name] = float(np.max(np.abs(var - bed)))

    # local-node spectra of (2/n)J - I for the two degrees
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.6))
    for ax, (n, name, col) in zip(
        axes, [(srs.degree, "srs[right] node (n=3)", "#1f6fb2"), (dia.degree, "diamond node (n=4)", "#27ae60")]
    ):
        S_local = admittance_scatter(np.ones(n))  # equal-Y = (2/n)J - I exactly
        ev = np.sort(np.linalg.eigvals(S_local).real)
        ax.stem(range(len(ev)), ev, linefmt=col, markerfmt="o", basefmt="grey")
        ax.axhline(1.0, color="grey", ls=":", lw=0.8)
        ax.axhline(-1.0, color="grey", ls=":", lw=0.8)
        ax.set_ylim(-1.4, 1.4)
        spectrum_str = "{" + ", ".join(f"{e:+.0f}" for e in sorted(ev, reverse=True)) + "}"
        ax.set_title(f"{name}\nspectrum {spectrum_str}")
        ax.set_xlabel("eigenvalue index")
        ax.set_ylabel(r"eigenvalue of $(2/n)J-I$")
        ax.set_xticks(range(len(ev)))
        ax.grid(alpha=0.25)

    rec_str = "  |  ".join(f"{k}: max|d|={v:.1e}" for k, v in recoveries.items())
    fig.suptitle(f"Bedrock recovery at S=1 ($\\mathcal{{S}}=(2/n)J-I$):  {rec_str}", fontsize=10)
    p = os.path.join(OUT, "vvs_fig_c_bedrock_spectrum.png")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(p, dpi=DPI)
    plt.close(fig)
    return p


# ─────────────────────────────────────────────────────────────────────────────
# (d) Saturation → admittance map: S(A) and Y_bond(A).
# ─────────────────────────────────────────────────────────────────────────────
def fig_d_sat_admittance() -> str:
    """The varactor mapping: S(A)=√(1-A²) and Y_bond=Y0/√S(A) vs A, computed via the
    ACTUAL kernel + bond_admittance_from_saturation. Twin-axis so both curves are clear."""
    A = np.linspace(0.0, 0.985, 500)  # stay below A_cap for the smooth branch
    S = saturation_kernel(A, A_cap=0.999999, S_min=1e-12)
    Y = bond_admittance_from_saturation(A, Y0=1.0)  # = 1/√S

    fig, ax1 = plt.subplots(figsize=(8.2, 5.0))
    ax1.plot(A, S, color="#8e44ad", lw=2.2, label=r"$S(A)=\sqrt{1-A^2}$ (saturation)")
    ax1.set_xlabel(r"saturation amplitude $A=|V|/V_{yield}$")
    ax1.set_ylabel(r"$S(A)$  (saturation kernel)", color="#8e44ad")
    ax1.tick_params(axis="y", labelcolor="#8e44ad")
    ax1.set_ylim(0.0, 1.05)
    ax1.grid(alpha=0.3)

    ax2 = ax1.twinx()
    ax2.plot(A, Y, color="#e67e22", lw=2.2, label=r"$Y_{bond}=Y_0/\sqrt{S(A)}$ (admittance)")
    ax2.set_ylabel(r"$Y_{bond}/Y_0$  (bond admittance)", color="#e67e22")
    ax2.tick_params(axis="y", labelcolor="#e67e22")
    ax2.axhline(1.0, color="grey", ls=":", lw=0.8)

    # mark vacuum point A=0 → S=1, Y=Y0
    ax1.plot(0.0, 1.0, "o", color="#8e44ad", ms=6)
    ax1.annotate(
        "vacuum: $S=1,\\ Y=Y_0$",
        xy=(0.0, 1.0),
        xytext=(0.18, 0.55),
        fontsize=8.5,
        arrowprops=dict(arrowstyle="->", lw=0.9),
    )

    lines = ax1.get_lines()[:1] + ax2.get_lines()[:1]
    ax1.legend(lines, [ln.get_label() for ln in lines], fontsize=8.5, loc="upper center")
    ax1.set_title(r"The varactor map: $S(A)=\sqrt{1-A^2}\ \Rightarrow\ Y_{bond}=Y_0/\sqrt{S},\ Z_{bond}=Z_0\sqrt{S}$")
    p = os.path.join(OUT, "vvs_fig_d_sat_admittance.png")
    fig.tight_layout()
    fig.savefig(p, dpi=DPI)
    plt.close(fig)
    return p


def main() -> None:
    print("VACUUM-VARACTOR SCATTER — figure generation (deterministic)")
    print("=" * 70)
    paths = [fig_a_gamma_vs_A(), fig_b_scramble(), fig_c_bedrock_spectrum(), fig_d_sat_admittance()]
    for p in paths:
        print(f"  wrote {os.path.relpath(p, _REPO_SRC)}  ({os.path.getsize(p)} bytes)")
    print("=" * 70)
    print("DONE — 4 figures written to", os.path.relpath(OUT, _REPO_SRC))


if __name__ == "__main__":
    main()
