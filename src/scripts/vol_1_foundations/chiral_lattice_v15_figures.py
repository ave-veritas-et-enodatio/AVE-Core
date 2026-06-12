#!/usr/bin/env python3
"""
Genesis v15 — Lane A nucleation figures (characteristic curves + spatial snapshots).

Run:
  python src/scripts/vol_1_foundations/chiral_lattice_v15_figures.py
  python src/scripts/vol_1_foundations/chiral_lattice_v15_figures.py --smoke
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.colors import LogNorm  # noqa: E402
import numpy as np  # noqa: E402

from ave.core import chiral_lattice as cl  # noqa: E402
from ave.core.chiral_lattice_v11 import DEFAULT_TAU_STEPS  # noqa: E402
from ave.core.chiral_lattice_v13 import compton_pocket_mask  # noqa: E402
from ave.core.chiral_lattice_v15 import run_p15_trajectory  # noqa: E402
from ave.core.genesis_lane_a_provenance import build_lane_a_provenance  # noqa: E402

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs" / "genesis_v15_figures"

COLORS = {
    "cosmic": "#c0392b",
    "ablated": "#8e44ad",
    "photon": "#2980b9",
    "no_wall": "#27ae60",
}


def _shade_latent(ax, traj, *, alpha: float = 0.10) -> None:
    ax.axvspan(
        0,
        traj.n_latent_steps,
        color="#e67e22",
        alpha=alpha,
        label="latent window",
    )


def _shade_pocket(ax, traj, *, alpha: float = 0.12) -> None:
    z0 = traj.pocket_z0
    zh = traj.pocket_z_half
    ax.axvspan(z0 - zh, z0 + zh, color="#f39c12", alpha=alpha, label="Compton pocket")


def fig_lane_a_curves(
    trajectories: dict[str, object],
    *,
    out_path: Path,
) -> None:
    """r_yield, native energy, E_frac, width — cosmic vs photon vs ablation."""
    fig, axes = plt.subplots(2, 2, figsize=(11, 8), sharex="col")
    panels = [
        ("r_yield_pair", "Pair r_yield* (native yield units)", "r_yield*"),
        ("total_energy_native", "Total field energy (native m_e c²)", "E_native"),
        ("E_frac", "Energy fraction in pocket", "E_frac"),
        ("width", "Energy-weighted width", "width"),
    ]

    ref = next(iter(trajectories.values()))
    for ax, (key, title, ylab) in zip(axes.flat, panels):
        for name, traj in trajectories.items():
            c = COLORS.get(name, "#333333")
            steps = traj.steps
            y = getattr(traj, key)
            ax.plot(steps, y, "-", color=c, lw=1.8, label=name)
        if key == "r_yield_pair":
            ax.axhline(
                ref.r_yield_threshold,
                ls=":",
                color="gray",
                lw=0.9,
                label=f"P15 floor ({ref.r_yield_threshold:.2f})",
            )
            ax.axhline(
                ref.r_yield_knee,
                ls="--",
                color="#7f8c8d",
                lw=0.9,
                label=f"knee √2 ({ref.r_yield_knee:.2f})",
            )
        if key == "E_frac":
            ax.axhline(0.55, ls=":", color="gray", lw=0.8)
        _shade_latent(ax, ref)
        ax.set_title(title, fontsize=10)
        ax.set_ylabel(ylab)
        ax.grid(alpha=0.25)

    for ax in axes[1, :]:
        ax.set_xlabel("scatter step")
    axes[0, 0].legend(fontsize=7, loc="best")
    axes[0, 1].legend(fontsize=7, loc="best")

    fig.suptitle(
        "Genesis v15 — Lane A characteristic curves\n"
        "orange band = latent injection window (derived native ramp)",
        fontsize=11,
        y=1.02,
    )
    fig.tight_layout()
    fig.savefig(out_path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"  [figure] {out_path}")


def fig_spatial_snapshots(
    traj,
    *,
    out_path: Path,
    title_suffix: str = "",
) -> None:
    """x–z scatter of node energy; pair nodes highlighted."""
    axis = traj.axis
    perp = 0 if axis != 0 else 1
    n_snap = len(traj.snapshot_steps)
    ncol = min(3, n_snap)
    nrow = int(np.ceil(n_snap / ncol))
    fig, axes = plt.subplots(nrow, ncol, figsize=(4 * ncol, 3.5 * nrow))
    axes_flat = np.atleast_1d(axes).flat

    pos = traj.net_pos
    x = pos[:, perp]
    z = pos[:, axis]
    pocket = traj.pocket_mask
    pair_idx = traj.pair_node_indices

    e_all = traj.snapshot_node_energy
    e_pos = e_all[e_all > 0]
    vmin = float(e_pos.min()) if e_pos.size else 1e-12
    vmax = float(e_all.max()) if e_all.max() > 0 else 1.0
    norm = LogNorm(vmin=max(vmin, 1e-12), vmax=max(vmax, vmin * 10))

    for ax, si in zip(axes_flat, range(n_snap)):
        step = int(traj.snapshot_steps[si])
        e = traj.snapshot_node_energy[si]
        sizes = 4 + 40 * (e / (vmax + 1e-30))
        sc = ax.scatter(
            x,
            z,
            c=np.maximum(e, vmin),
            s=sizes,
            cmap="inferno",
            norm=norm,
            alpha=0.9,
        )
        if pair_idx.size > 0:
            ax.scatter(
                x[pair_idx],
                z[pair_idx],
                s=80,
                facecolors="none",
                edgecolors="#00e5ff",
                linewidths=1.2,
                label="seed pair",
            )
        ax.axhline(
            traj.pocket_z0 - traj.pocket_z_half,
            color="#f39c12",
            ls="--",
            lw=0.8,
            alpha=0.7,
        )
        ax.axhline(
            traj.pocket_z0 + traj.pocket_z_half,
            color="#f39c12",
            ls="--",
            lw=0.8,
            alpha=0.7,
        )
        latent_mark = step < traj.n_latent_steps
        phase = "latent" if latent_mark else "quiescent"
        ax.set_title(f"step {step} ({phase})", fontsize=9)
        ax.set_xlabel("x (cell units)")
        ax.set_ylabel("z (cell units)")
        ax.set_aspect("equal", adjustable="box")
        plt.colorbar(sc, ax=ax, fraction=0.046, pad=0.04, label="|V|²")

    for ax in axes_flat[n_snap:]:
        ax.set_visible(False)

    fig.suptitle(
        f"Genesis v15 — spatial energy density ({traj.label}){title_suffix}\n"
        "cyan rings = saturated node-pair seed; orange lines = pocket bounds",
        fontsize=10,
    )
    fig.tight_layout()
    fig.savefig(out_path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"  [figure] {out_path}")


def fig_ablation_comparison(
    traj_base,
    traj_ablated,
    *,
    out_path: Path,
) -> None:
    """Side-by-side r_yield during latent window — baseline vs dissipation OFF."""
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)

    for ax, traj, color, subtitle in zip(
        axes,
        [traj_base, traj_ablated],
        [COLORS["cosmic"], COLORS["ablated"]],
        ["baseline (χ=0.5, snap ON)", "ablated (latent: χ=0, snap OFF)"],
    ):
        ax.plot(
            traj.steps,
            traj.r_yield_pair,
            color=color,
            lw=2,
            label="r_yield* (pair)",
        )
        ax.plot(
            traj.steps,
            traj.A2_pair,
            color=color,
            lw=1.2,
            ls="--",
            alpha=0.7,
            label="A²_vsnap (pair)",
        )
        _shade_latent(ax, traj, alpha=0.15)
        ax.axhline(
            traj.r_yield_threshold,
            ls=":",
            color="gray",
            lw=0.9,
            label="P15 floor",
        )
        ax.axhline(
            traj.r_yield_knee,
            ls="--",
            color="#7f8c8d",
            lw=0.9,
            label="knee √2",
        )
        ax.set_title(subtitle, fontsize=9)
        ax.set_xlabel("scatter step")
        ax.grid(alpha=0.25)
        ax.legend(fontsize=7, loc="best")

    axes[0].set_ylabel("amplitude (native units)")
    gain = traj_ablated.r_yield_pair.max() / (traj_base.r_yield_pair.max() + 1e-30)
    fig.suptitle(
        f"Genesis v15a-ablation — pair amplitude during latent window\n"
        f"peak r_yield gain (ablated/baseline) = {gain:.2f}×",
        fontsize=11,
    )
    fig.tight_layout()
    fig.savefig(out_path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"  [figure] {out_path}")


def fig_battery_summary(
    trajectories: dict[str, object],
    *,
    out_path: Path,
) -> None:
    """Terminal r_yield* and E_frac for Lane A battery arms."""
    names = list(trajectories.keys())
    labels = [n.replace("_", "\n") for n in names]
    r_final = [traj.r_yield_pair[-1] for traj in trajectories.values()]
    r_peak = [float(np.max(traj.r_yield_pair)) for traj in trajectories.values()]
    e_frac = [traj.E_frac[-1] for traj in trajectories.values()]

    ref = next(iter(trajectories.values()))
    x = np.arange(len(names))
    w = 0.35
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))

    ax = axes[0]
    b1 = ax.bar(x - w / 2, r_peak, w, color=[COLORS.get(n, "#555") for n in names], label="peak")
    b2 = ax.bar(x + w / 2, r_final, w, color=[COLORS.get(n, "#555") for n in names], alpha=0.55, label="final")
    ax.axhline(ref.r_yield_threshold, ls=":", color="gray", lw=1, label="P15 floor")
    ax.axhline(ref.r_yield_knee, ls="--", color="#7f8c8d", lw=1, label="knee √2")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("r_yield* (native)")
    ax.set_title("Pair yield amplitude")
    ax.legend(fontsize=7)
    ax.grid(axis="y", alpha=0.25)
    for bars in (b1, b2):
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, h, f"{h:.2f}", ha="center", va="bottom", fontsize=7)

    ax = axes[1]
    bars = ax.bar(x, e_frac, color=[COLORS.get(n, "#555") for n in names])
    ax.axhline(0.55, ls=":", color="gray", lw=1, label="P13 floor")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("E_frac in pocket")
    ax.set_title("Confinement (terminal)")
    ax.set_ylim(0, 1.05)
    ax.legend(fontsize=7)
    ax.grid(axis="y", alpha=0.25)
    for bar, v in zip(bars, e_frac):
        ax.text(bar.get_x() + bar.get_width() / 2, v, f"{v:.2f}", ha="center", va="bottom", fontsize=7)

    fig.suptitle("Genesis v15 — Lane A battery summary (HEAL-CONFIRMED read)", fontsize=11)
    fig.tight_layout()
    fig.savefig(out_path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"  [figure] {out_path}")


def fig_energy_profiles(
    trajectories: dict[str, object],
    *,
    out_path: Path,
) -> None:
    """Axial energy profiles at end of latent window vs end of run."""
    fig, axes = plt.subplots(1, len(trajectories), figsize=(4 * len(trajectories), 4), sharey=True)
    if len(trajectories) == 1:
        axes = [axes]

    for ax, (name, traj) in zip(axes, trajectories.items()):
        n_lat = traj.n_latent_steps
        idx_lat = int(np.argmin(np.abs(traj.steps - n_lat)))
        idx_end = -1
        for idx, alpha, lbl in (
            (idx_lat, 0.5, f"end latent (step {traj.steps[idx_lat]})"),
            (idx_end, 1.0, f"terminal (step {traj.steps[idx_end]})"),
        ):
            prof = traj.z_profiles[idx]
            ax.fill_between(traj.z_centers, prof, alpha=0.12 * alpha, color=COLORS.get(name, "#333"))
            ax.plot(traj.z_centers, prof, color=COLORS.get(name, "#333"), lw=1.8, alpha=alpha, label=lbl)
        if traj.bulk_wall_on:
            _shade_pocket(ax, traj, alpha=0.08)
        ax.set_title(name, fontsize=9)
        ax.set_xlabel("z (cell units)")
        ax.legend(fontsize=7)
        ax.grid(alpha=0.25)

    axes[0].set_ylabel("binned node energy Σ|V|²")
    fig.suptitle("Genesis v15 — axial profiles: end of latent window vs terminal", fontsize=11)
    fig.tight_layout()
    fig.savefig(out_path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"  [figure] {out_path}")


def main() -> None:
    smoke = "--smoke" in sys.argv
    L = 8 if smoke else 10
    record_every = 2 if smoke else 5
    tau_steps = 10 if smoke else DEFAULT_TAU_STEPS
    tag = "SMOKE" if smoke else "PRODUCTION"

    OUT.mkdir(parents=True, exist_ok=True)
    print("=" * 72)
    print(f"GENESIS v15 FIGURES ({tag})  L={L}")
    print("=" * 72)

    net = cl.build_srs_net(L, "right")
    pocket = compton_pocket_mask(net)
    prov = build_lane_a_provenance(net, pocket, smoke=smoke)
    common = dict(prov=prov, tau_steps=tau_steps, record_every=record_every)

    print("Recording cosmic IC (baseline)...")
    traj_cosmic = run_p15_trajectory(
        net,
        "A cosmic IC",
        latent_on=True,
        seed_mode="pair",
        bulk_wall=True,
        latent_dissipation_ablation=False,
        **common,
    )
    print("Recording cosmic IC (latent ablation)...")
    traj_ablated = run_p15_trajectory(
        net,
        "A cosmic ablation",
        latent_on=True,
        seed_mode="pair",
        bulk_wall=True,
        latent_dissipation_ablation=True,
        **common,
    )
    print("Recording photon compare...")
    traj_photon = run_p15_trajectory(
        net,
        "C photon",
        latent_on=False,
        seed_mode="photon",
        bulk_wall=True,
        **common,
    )
    print("Recording latent no-wall...")
    traj_no_wall = run_p15_trajectory(
        net,
        "D no wall",
        latent_on=True,
        seed_mode="pair",
        bulk_wall=False,
        **common,
    )

    battery = {
        "cosmic": traj_cosmic,
        "photon": traj_photon,
        "no_wall": traj_no_wall,
    }
    curves = {
        "cosmic": traj_cosmic,
        "ablated": traj_ablated,
        "photon": traj_photon,
    }

    suffix = "_smoke" if smoke else ""
    fig_lane_a_curves(
        curves,
        out_path=OUT / f"genesis_v15_lane_a_curves{suffix}.png",
    )
    fig_spatial_snapshots(
        traj_cosmic,
        out_path=OUT / f"genesis_v15_spatial_snapshots{suffix}.png",
    )
    fig_ablation_comparison(
        traj_cosmic,
        traj_ablated,
        out_path=OUT / f"genesis_v15a_ablation_comparison{suffix}.png",
    )
    fig_battery_summary(
        battery,
        out_path=OUT / f"genesis_v15_battery_summary{suffix}.png",
    )
    fig_energy_profiles(
        {"cosmic": traj_cosmic, "photon": traj_photon},
        out_path=OUT / f"genesis_v15_energy_profiles{suffix}.png",
    )

    print("=" * 72)
    print(f"Figures written to {OUT}/")
    print("=" * 72)


if __name__ == "__main__":
    main()
