#!/usr/bin/env python3
"""
Genesis v14 — characteristic curves + spatial snapshots.

Produces multi-panel figures for cavity+comoving transport visualization.

Run:
  python src/scripts/vol_1_foundations/chiral_lattice_v14_figures.py
  python src/scripts/vol_1_foundations/chiral_lattice_v14_figures.py --smoke
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from ave.core import chiral_lattice as cl  # noqa: E402
from ave.core.chiral_lattice_v11 import DEFAULT_TAU_STEPS  # noqa: E402
from ave.core.chiral_lattice_v14 import run_p14_trajectory  # noqa: E402

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs" / "genesis_v14_figures"

COLORS = {
    "full": "#c0392b",
    "pinned": "#2980b9",
    "open": "#27ae60",
}


def _shade_pocket(ax, traj, *, alpha: float = 0.12) -> None:
    z0 = traj.pocket_z0
    zh = traj.pocket_z_half
    ax.axvspan(z0 - zh, z0 + zh, color="#f39c12", alpha=alpha, label="Compton pocket")


def fig_characteristic_curves(
    trajectories: dict[str, object],
    *,
    out_path: Path,
) -> None:
    """Time-series: centroid, width, E_frac, peak (global vs pocket)."""
    fig, axes = plt.subplots(2, 2, figsize=(11, 8), sharex="col")
    panels = [
        ("centroid", "Energy centroid along z", "z (cell units)"),
        ("width", "Energy-weighted width", "width"),
        ("E_frac", "Fraction of energy in pocket", "E_frac"),
        ("peak", "Peak amplitude (global solid, pocket dashed)", "A / A_yield"),
    ]

    for ax, (key, title, ylab) in zip(axes.flat, panels):
        for name, traj in trajectories.items():
            c = COLORS[name]
            steps = traj.steps
            if key == "centroid":
                y = traj.centroid
            elif key == "width":
                y = traj.width
            elif key == "E_frac":
                y = traj.E_frac
            else:
                ax.plot(steps, traj.peak_global, "-", color=c, lw=1.6, label=f"{name} global")
                if traj.bulk_wall_on:
                    ax.plot(
                        steps,
                        traj.peak_pocket,
                        "--",
                        color=c,
                        lw=1.2,
                        alpha=0.85,
                        label=f"{name} pocket",
                    )
                continue
            ax.plot(steps, y, "-", color=c, lw=1.8, label=name)
        ax.set_title(title, fontsize=10)
        ax.set_ylabel(ylab)
        ax.grid(alpha=0.25)
        if key == "E_frac":
            ax.axhline(0.55, ls=":", color="gray", lw=0.8, label="P13 floor")
        if key == "width":
            w0 = trajectories["full"].width[0]
            ax.axhline(2.0 * w0, ls=":", color="gray", lw=0.8, label="2× initial")

    for ax in axes[1, :]:
        ax.set_xlabel("scatter step")
    axes[0, 0].legend(fontsize=7, loc="best")
    axes[0, 1].legend(fontsize=7, loc="best")
    axes[1, 0].legend(fontsize=7, loc="best")
    axes[1, 1].legend(fontsize=7, loc="lower left")

    fig.suptitle(
        "Genesis v14 — characteristic curves (full stack vs pinned vs open srs)",
        fontsize=12,
        y=1.01,
    )
    fig.tight_layout()
    fig.savefig(out_path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"  [figure] {out_path}")


def fig_energy_profiles(
    trajectories: dict[str, object],
    *,
    out_path: Path,
) -> None:
    """Energy density along z at multiple times."""
    fig, axes = plt.subplots(1, 3, figsize=(12, 4), sharey=True)
    names = ["full", "pinned", "open"]
    titles = [
        "Full stack (wall + comoving)",
        "Pinned cavity (wall, no comoving)",
        "Open srs (no wall, comoving)",
    ]

    for ax, name, title in zip(axes, names, titles):
        traj = trajectories[name]
        n_rec = len(traj.steps)
        pick = [0, n_rec // 3, 2 * n_rec // 3, n_rec - 1]
        pick = sorted(set(min(i, n_rec - 1) for i in pick))
        shades = np.linspace(0.35, 1.0, len(pick))
        for idx, alpha in zip(pick, shades):
            step = int(traj.steps[idx])
            prof = traj.z_profiles[idx]
            ax.fill_between(
                traj.z_centers,
                prof,
                alpha=0.15 * alpha,
                color=COLORS[name],
            )
            ax.plot(
                traj.z_centers,
                prof,
                color=COLORS[name],
                alpha=alpha,
                lw=1.5,
                label=f"step {step}",
            )
        if traj.bulk_wall_on:
            _shade_pocket(ax, traj)
        ax.set_title(title, fontsize=9)
        ax.set_xlabel("z (cell units)")
        ax.legend(fontsize=7, loc="upper right")
        ax.grid(alpha=0.25)

    axes[0].set_ylabel("binned node energy Σ|V|²")
    fig.suptitle("Genesis v14 — axial energy profiles (evolution + pocket band)", fontsize=11)
    fig.tight_layout()
    fig.savefig(out_path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"  [figure] {out_path}")


def fig_spatial_snapshots(
    traj_full,
    *,
    out_path: Path,
) -> None:
    """x–z scatter of node energy at snapshot times (full stack)."""
    axis = traj_full.axis
    perp = 0 if axis != 0 else 1
    n_snap = len(traj_full.snapshot_steps)
    ncol = min(3, n_snap)
    nrow = int(np.ceil(n_snap / ncol))
    fig, axes = plt.subplots(nrow, ncol, figsize=(4 * ncol, 3.5 * nrow))
    axes_flat = np.atleast_1d(axes).flat

    pos = traj_full.net_pos
    x = pos[:, perp]
    z = pos[:, axis]
    pocket = traj_full.pocket_mask

    e_max = float(traj_full.snapshot_node_energy.max()) or 1.0

    for ax, si in zip(axes_flat, range(n_snap)):
        step = int(traj_full.snapshot_steps[si])
        e = traj_full.snapshot_node_energy[si]
        sc = ax.scatter(
            x,
            z,
            c=e,
            s=6,
            cmap="inferno",
            vmin=0,
            vmax=e_max,
            alpha=0.85,
        )
        ax.scatter(
            x[~pocket],
            z[~pocket],
            s=2,
            c="none",
            edgecolors="#3498db",
            linewidths=0.2,
            alpha=0.25,
        )
        ax.axhline(
            traj_full.pocket_z0 - traj_full.pocket_z_half,
            color="#f39c12",
            ls="--",
            lw=0.8,
            alpha=0.7,
        )
        ax.axhline(
            traj_full.pocket_z0 + traj_full.pocket_z_half,
            color="#f39c12",
            ls="--",
            lw=0.8,
            alpha=0.7,
        )
        ax.set_title(f"step {step}", fontsize=9)
        ax.set_xlabel("x (cell units)")
        ax.set_ylabel("z (cell units)")
        ax.set_aspect("equal", adjustable="box")
        plt.colorbar(sc, ax=ax, fraction=0.046, pad=0.04, label="|V|²")

    for ax in axes_flat[n_snap:]:
        ax.set_visible(False)

    fig.suptitle(
        "Genesis v14 — spatial energy density (full stack, x–z plane)\n"
        "orange lines = pocket bounds; blue outline = exterior nodes",
        fontsize=10,
    )
    fig.tight_layout()
    fig.savefig(out_path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"  [figure] {out_path}")


def fig_metrics_summary(
    trajectories: dict[str, object],
    *,
    out_path: Path,
    transport_gain: float,
    gain_threshold: float,
) -> None:
    """Bar summary of terminal metrics + transport gain."""
    names = ["full", "pinned", "open"]
    labels = ["Full\nstack", "Pinned\ncavity", "Open\ncomoving"]
    metrics = {
        "centroid disp (from t=0)": [],
        "width× (final/init)": [],
        "E_frac": [],
        "peak pocket": [],
    }

    for name in names:
        t = trajectories[name]
        z0 = t.centroid[0]
        z1 = t.centroid[-1]
        box = float(np.max(t.net_pos[:, t.axis]) - np.min(t.net_pos[:, t.axis]))
        raw = z1 - z0
        if raw > 0.5 * box:
            raw -= box
        elif raw < -0.5 * box:
            raw += box
        metrics["centroid disp (from t=0)"].append(abs(raw))
        w0, w1 = t.width[0], t.width[-1]
        metrics["width× (final/init)"].append(w1 / (w0 + 1e-30))
        metrics["E_frac"].append(t.E_frac[-1])
        metrics["peak pocket"].append(t.peak_pocket[-1])

    fig, axes = plt.subplots(2, 2, figsize=(9, 7))
    x = np.arange(len(names))
    bar_colors = [COLORS[n] for n in names]

    for ax, (mname, vals) in zip(axes.flat, metrics.items()):
        bars = ax.bar(x, vals, color=bar_colors, edgecolor="k", linewidth=0.6)
        ax.set_xticks(x)
        ax.set_xticklabels(labels, fontsize=8)
        ax.set_title(mname, fontsize=9)
        ax.grid(axis="y", alpha=0.25)
        for bar, v in zip(bars, vals):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height(),
                f"{v:.2f}",
                ha="center",
                va="bottom",
                fontsize=7,
            )

    fig.text(
        0.5,
        0.02,
        f"Transport gain (full−pinned) = {transport_gain:.3f}  |  "
        f"P12 threshold = {gain_threshold:.3f}",
        ha="center",
        fontsize=9,
    )
    fig.suptitle("Genesis v14 — terminal metrics comparison", fontsize=11)
    fig.tight_layout(rect=[0, 0.04, 1, 0.96])
    fig.savefig(out_path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"  [figure] {out_path}")


def fig_profile_comparison_endstate(
    trajectories: dict[str, object],
    *,
    out_path: Path,
) -> None:
    """Overlay final axial profiles — shows confinement vs dispersion."""
    fig, ax = plt.subplots(figsize=(8, 4.5))
    for name, traj in trajectories.items():
        prof = traj.z_profiles[-1]
        ax.plot(
            traj.z_centers,
            prof,
            color=COLORS[name],
            lw=2,
            label=f"{name} (step {traj.steps[-1]})",
        )
        if traj.bulk_wall_on:
            _shade_pocket(ax, traj, alpha=0.08)
    ax.set_xlabel("z (cell units)")
    ax.set_ylabel("binned node energy Σ|V|²")
    ax.set_title("Genesis v14 — final axial energy profile (all arms)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(out_path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"  [figure] {out_path}")


def main() -> None:
    smoke = "--smoke" in sys.argv
    L = 8 if smoke else 10
    n_steps = 60 if smoke else 220
    record_every = 2 if smoke else 5
    tau_steps = 10 if smoke else DEFAULT_TAU_STEPS
    tag = "SMOKE" if smoke else "PRODUCTION"

    OUT.mkdir(parents=True, exist_ok=True)
    print("=" * 72)
    print(f"GENESIS v14 FIGURES ({tag})  L={L}  n_steps={n_steps}")
    print("=" * 72)

    net = cl.build_srs_net(L, "right")
    common = dict(
        n_steps=n_steps,
        record_every=record_every,
        tau_steps=tau_steps,
        v_boost=1.0,
    )

    print("Recording full stack trajectory...")
    traj_full = run_p14_trajectory(
        net,
        "full stack",
        bulk_wall=True,
        comoving=True,
        **common,
    )
    print("Recording pinned cavity trajectory...")
    traj_pinned = run_p14_trajectory(
        net,
        "pinned",
        bulk_wall=True,
        comoving=False,
        **common,
    )
    print("Recording open comoving trajectory...")
    traj_open = run_p14_trajectory(
        net,
        "open",
        bulk_wall=False,
        comoving=True,
        **common,
    )

    trajectories = {
        "full": traj_full,
        "pinned": traj_pinned,
        "open": traj_open,
    }

    from ave.core.chiral_lattice_v12 import transport_gain_threshold

    z0f, z1f = traj_full.centroid[0], traj_full.centroid[-1]
    z0p, z1p = traj_pinned.centroid[0], traj_pinned.centroid[-1]
    box = float(net.box)

    def _disp(z0: float, z1: float) -> float:
        raw = z1 - z0
        if raw > 0.5 * box:
            raw -= box
        elif raw < -0.5 * box:
            raw += box
        return abs(raw)

    transport_gain = _disp(z0f, z1f) - _disp(z0p, z1p)
    gain_thr = transport_gain_threshold(n_steps, box)

    suffix = "_smoke" if smoke else ""
    fig_characteristic_curves(
        trajectories,
        out_path=OUT / f"genesis_v14_characteristic_curves{suffix}.png",
    )
    fig_energy_profiles(
        trajectories,
        out_path=OUT / f"genesis_v14_energy_profiles{suffix}.png",
    )
    fig_spatial_snapshots(
        traj_full,
        out_path=OUT / f"genesis_v14_spatial_snapshots{suffix}.png",
    )
    fig_metrics_summary(
        trajectories,
        out_path=OUT / f"genesis_v14_metrics_summary{suffix}.png",
        transport_gain=transport_gain,
        gain_threshold=gain_thr,
    )
    fig_profile_comparison_endstate(
        trajectories,
        out_path=OUT / f"genesis_v14_final_profile_overlay{suffix}.png",
    )

    print("=" * 72)
    print(f"Figures written to {OUT}/")
    print("=" * 72)


if __name__ == "__main__":
    main()
