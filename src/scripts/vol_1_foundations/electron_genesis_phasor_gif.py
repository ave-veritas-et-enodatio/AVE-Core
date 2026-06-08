#!/usr/bin/env python3
r"""Dynamic (V_inc, V_ref) phasor diagram for native genesis snap trap.

Reuses the closed bench protocol (finish prereg): propagate 0.48 → snap @ x≥14
→ trap_amp ≥ 1.25 → zero drive. Samples shell-mean port-0 (V_inc, V_ref) around the energy centroid each cadence
(core is Meissner-nulled); animates post-snap trajectory in bond LC-tank phase space.

Outputs:
  assets/sim_outputs/electron_genesis_phasor.gif
  assets/sim_outputs/electron_genesis_phasor.png  (full post-snap trace)
  src/scripts/vol_1_foundations/_output/electron_genesis_phasor_results.json
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Ellipse

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from native_electron_propagation import (  # noqa: E402
    apply_co_moving_longitudinal_drive,
    energy_centroid,
    interior_mask,
)
from native_k4_gamma_ceiling import (  # noqa: E402
    GAMMA_FULL_TIR,
    bond_gamma_min,
    seed_sech_v_inc,
    verify_canonical_sources,
)

from ave.core.constants import ALPHA_COLD  # noqa: E402
from ave.topological.vacuum_engine import VacuumEngine3D  # noqa: E402
from ave_path_util import sim_output  # noqa: E402

OUT_DIR = next(p for p in Path(__file__).resolve().parents if (p / ".git").exists())
OUT_DIR = OUT_DIR / "src" / "scripts" / "vol_1_foundations" / "_output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

N_LATTICE = 32
PML = 4
N_STEPS_PRE = 400
N_STEPS_POST = 600
CADENCE = 2
SEED_RADIUS = 2.5
SHELL_RADIUS = 6
V_DRIVE_PRE = 0.04
AMP_START = 0.48
TRAP_AMP = 1.25
TRIGGER_X = 14.0
CX0_FRAC = 0.28
SAMPLE_PORT = 0
MAX_GIF_FRAMES = 72
PHI_SQ = ((1.0 + math.sqrt(5.0)) / 2.0) ** 2

ALPHA_T = float(ALPHA_COLD)
GAMMA_TARGET = -math.sqrt(1.0 - ALPHA_T)


def _core_idx(cx: float, cy0: int, cz0: int, n: int) -> tuple[int, int, int]:
    return (
        min(max(int(round(cx)), PML), n - PML - 1),
        cy0,
        cz0,
    )


def _shell_mask(
    shape: tuple[int, int, int],
    center: tuple[int, int, int],
    radius: int,
    active: np.ndarray,
) -> np.ndarray:
    cx, cy, cz = center
    i, j, k = np.indices(shape)
    r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2)
    return (r <= radius) & active


def _sample_phasor(
    engine: VacuumEngine3D,
    core: tuple[int, int, int],
    port: int,
    *,
    shell_radius: int,
) -> tuple[float, float]:
    """Shell-mean (V_inc, V_ref) — core is Meissner-nulled; bond readout lives on shell."""
    sh = _shell_mask(engine.k4.V_inc.shape[:3], core, shell_radius, engine.k4.mask_active)
    if not np.any(sh):
        cx, cy, cz = core
        return (
            float(engine.k4.V_inc[cx, cy, cz, port]),
            float(engine.k4.V_ref[cx, cy, cz, port]),
        )
    vi = float(np.mean(engine.k4.V_inc[sh, port]))
    vr = float(np.mean(engine.k4.V_ref[sh, port]))
    return vi, vr


def _pca_ellipse(v_inc: np.ndarray, v_ref: np.ndarray) -> dict[str, float]:
    pts = np.column_stack([v_inc, v_ref])
    if len(pts) < 4:
        return {"R": float("nan"), "r": float("nan"), "R_over_r": float("nan")}
    cen = pts.mean(axis=0)
    centered = pts - cen
    cov = np.cov(centered.T)
    evals, evecs = np.linalg.eigh(cov)
    order = np.argsort(evals)[::-1]
    evals = evals[order]
    evecs = evecs[:, order]
    R = float(math.sqrt(max(evals[0], 0.0)))
    r = float(math.sqrt(max(evals[1], 0.0)))
    angle = float(math.degrees(math.atan2(evecs[1, 0], evecs[0, 0])))
    return {
        "R": R,
        "r": r,
        "R_over_r": R / max(r, 1e-30),
        "centroid_v_inc": float(cen[0]),
        "centroid_v_ref": float(cen[1]),
        "angle_deg": angle,
    }


def run_phasor_capture(*, trap_amp: float = TRAP_AMP) -> dict[str, Any]:
    n = N_LATTICE
    cx0 = int(CX0_FRAC * n)
    cy0 = cz0 = n // 2
    engine = VacuumEngine3D.from_args(
        N=n,
        pml=PML,
        temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )
    seed_sech_v_inc(engine, (cx0, cy0, cz0), AMP_START, SEED_RADIUS)
    engine.cos.initialize_electron_unknot_sector(
        R_target=0.5, r_target=0.25, amplitude_scale=min(AMP_START, 1.0)
    )
    mask = interior_mask(n, PML) & engine.k4.mask_active

    snap_step: int | None = None
    last_cx = float(cx0)
    records: list[dict[str, Any]] = []
    total_steps = N_STEPS_PRE + N_STEPS_POST

    for step in range(total_steps + 1):
        if step % CADENCE == 0:
            engine._coupled._update_z_local_total()
            z = np.asarray(engine.k4.z_local_field)
            v_sq = np.sum(np.asarray(engine.k4.V_inc) ** 2, axis=-1)
            cx, _, _ = energy_centroid(v_sq, mask)
            if np.isfinite(cx):
                last_cx = cx
            core = _core_idx(last_cx, cy0, cz0, n)
            gamma = bond_gamma_min(z, engine.k4.mask_active, core, SHELL_RADIUS)
            vi, vr = _sample_phasor(
                engine, core, SAMPLE_PORT, shell_radius=SHELL_RADIUS
            )
            eps = float(1.0 - gamma**2) if gamma is not None else None
            records.append(
                {
                    "step": step,
                    "phase": "post" if snap_step is not None else "pre",
                    "v_inc": vi,
                    "v_ref": vr,
                    "gamma_min": gamma,
                    "eps_gamma": eps,
                    "cx": last_cx,
                }
            )

        if step < total_steps and snap_step is None and last_cx >= TRIGGER_X:
            core = _core_idx(last_cx, cy0, cz0, n)
            seed_sech_v_inc(engine, core, trap_amp, SEED_RADIUS)
            engine.cos.initialize_electron_unknot_sector(
                R_target=0.5, r_target=0.25, amplitude_scale=min(trap_amp, 1.0)
            )
            snap_step = step
            last_cx = float(core[0])

        if step < total_steps:
            if snap_step is None:
                apply_co_moving_longitudinal_drive(engine, last_cx, V_DRIVE_PRE)
            engine.step()

    post = [r for r in records if r["phase"] == "post"]
    pre = [r for r in records if r["phase"] == "pre"]
    vi_post = np.array([r["v_inc"] for r in post], dtype=float)
    vr_post = np.array([r["v_ref"] for r in post], dtype=float)
    pca = _pca_ellipse(vi_post, vr_post)

    gammas = [r["gamma_min"] for r in post if r["gamma_min"] is not None]
    gamma_min = float(min(gammas)) if gammas else None
    gamma_final = gammas[-1] if gammas else None
    eps_mean = float(np.mean([r["eps_gamma"] for r in post if r["eps_gamma"] is not None])) if post else None
    tir_held = bool(
        gamma_min is not None
        and gamma_min <= GAMMA_FULL_TIR
        and (gamma_final is None or gamma_final <= -0.95)
    )

    return {
        "trap_amp": trap_amp,
        "snap_step": snap_step,
        "n_pre_samples": len(pre),
        "n_post_samples": len(post),
        "sample_port": SAMPLE_PORT,
        "sample_site": f"shell_mean_r<={SHELL_RADIUS}",
        "gamma_min_post": gamma_min,
        "gamma_final_post": gamma_final,
        "gamma_target_for_alpha": GAMMA_TARGET,
        "eps_gamma_mean_post": eps_mean,
        "abs_eps_minus_alpha": abs(eps_mean - ALPHA_T) if eps_mean is not None else None,
        "tir_held": tir_held,
        "pca_post_snap": pca,
        "phi_sq_target": PHI_SQ,
        "records": records,
        "comparison_only_alpha": ALPHA_T,
    }


def _axis_limits(records: list[dict[str, Any]], pad: float = 0.12) -> tuple[float, float, float, float]:
    vi = np.array([r["v_inc"] for r in records], dtype=float)
    vr = np.array([r["v_ref"] for r in records], dtype=float)
    vmin = min(vi.min(), vr.min())
    vmax = max(vi.max(), vr.max())
    span = max(vmax - vmin, 1e-6)
    lo = vmin - pad * span
    hi = vmax + pad * span
    return lo, hi, lo, hi


def render_static_png(row: dict[str, Any], out_path: Path) -> None:
    post = [r for r in row["records"] if r["phase"] == "post"]
    pre = [r for r in row["records"] if r["phase"] == "pre"]
    pca = row["pca_post_snap"]

    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_facecolor("#0a0a12")
    ax.set_facecolor("#111118")

    if pre:
        ax.plot(
            [r["v_inc"] for r in pre],
            [r["v_ref"] for r in pre],
            color="#445566",
            lw=0.8,
            alpha=0.5,
            label="pre-snap",
        )
    ax.plot(
        [r["v_inc"] for r in post],
        [r["v_ref"] for r in post],
        color="#00e5ff",
        lw=1.0,
        alpha=0.85,
        label="post-snap",
    )
    ax.plot(post[-1]["v_inc"], post[-1]["v_ref"], "o", color="#ffeb3b", markersize=8, label="final")

    if np.isfinite(pca["R"]) and pca["R"] > 0:
        ell = Ellipse(
            (pca["centroid_v_inc"], pca["centroid_v_ref"]),
            width=2 * pca["R"],
            height=2 * max(pca["r"], 1e-9),
            angle=pca["angle_deg"],
            fill=False,
            edgecolor="#ff6b6b",
            lw=1.2,
            ls="--",
            label=f"PCA R/r={pca['R_over_r']:.2f}",
        )
        ax.add_patch(ell)

    ax.axhline(0, color="#333", lw=0.5)
    ax.axvline(0, color="#333", lw=0.5)
    ax.set_xlabel(r"$\langle V_{\mathrm{inc}}\rangle_{\mathrm{shell}}$ (port 0)", color="#ccc")
    ax.set_ylabel(r"$\langle V_{\mathrm{ref}}\rangle_{\mathrm{shell}}$ (port 0)", color="#ccc")
    ax.tick_params(colors="#aaa")
    ax.set_aspect("equal", adjustable="box")
    lo_x, hi_x, lo_y, hi_y = _axis_limits(row["records"])
    ax.set_xlim(lo_x, hi_x)
    ax.set_ylim(lo_y, hi_y)
    ax.legend(loc="upper right", fontsize=8, facecolor="#1a1a22", edgecolor="#444", labelcolor="#ccc")
    fig.suptitle(
        f"Genesis trap phasor  trap={row['trap_amp']:.2f}  "
        f"ε̄={row['eps_gamma_mean_post']:.4f}  α={ALPHA_T:.4f}  "
        f"R/r={pca['R_over_r']:.2f} (φ²={PHI_SQ:.3f})",
        color="#eee",
        fontsize=10,
    )
    fig.tight_layout()
    fig.savefig(out_path, dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)


def render_gif(row: dict[str, Any], out_path: Path) -> None:
    post = [r for r in row["records"] if r["phase"] == "post"]
    if len(post) < 2:
        return

    stride = max(1, len(post) // MAX_GIF_FRAMES)
    frames_idx = list(range(0, len(post), stride))
    if frames_idx[-1] != len(post) - 1:
        frames_idx.append(len(post) - 1)

    pca = row["pca_post_snap"]
    lo_x, hi_x, lo_y, hi_y = _axis_limits(post)

    fig, ax = plt.subplots(figsize=(7, 7))
    fig.patch.set_facecolor("#0a0a12")
    ax.set_facecolor("#111118")
    ax.set_xlim(lo_x, hi_x)
    ax.set_ylim(lo_y, hi_y)
    ax.set_xlabel(r"$V_{\mathrm{inc}}$", color="#ccc")
    ax.set_ylabel(r"$V_{\mathrm{ref}}$", color="#ccc")
    ax.tick_params(colors="#aaa")
    ax.set_aspect("equal", adjustable="box")
    ax.axhline(0, color="#333", lw=0.5)
    ax.axvline(0, color="#333", lw=0.5)

    (trail,) = ax.plot([], [], color="#00e5ff", lw=1.2, alpha=0.9)
    (head,) = ax.plot([], [], "o", color="#ffeb3b", markersize=9)
    ell_patch = Ellipse(
        (pca["centroid_v_inc"], pca["centroid_v_ref"]),
        width=2 * pca["R"] if np.isfinite(pca["R"]) else 0.1,
        height=2 * max(pca["r"], 1e-9) if np.isfinite(pca["r"]) else 0.1,
        angle=pca["angle_deg"],
        fill=False,
        edgecolor="#ff6b6b",
        lw=1.0,
        ls="--",
        alpha=0.7,
    )
    if np.isfinite(pca["R"]):
        ax.add_patch(ell_patch)

    info = fig.text(0.03, 0.03, "", color="#aaa", fontsize=9, family="monospace")
    fig.suptitle(
        f"Dynamic phasor @ genesis trap (port {SAMPLE_PORT}, shell r≤{SHELL_RADIUS})",
        color="#eee",
        fontsize=11,
    )

    def update(fi: int) -> tuple[Any, ...]:
        idx = frames_idx[fi]
        chunk = post[: idx + 1]
        trail.set_data([r["v_inc"] for r in chunk], [r["v_ref"] for r in chunk])
        head.set_data([chunk[-1]["v_inc"]], [chunk[-1]["v_ref"]])
        g = chunk[-1]["gamma_min"]
        eps = chunk[-1]["eps_gamma"]
        info.set_text(
            f"post frame {fi+1}/{len(frames_idx)}  step={chunk[-1]['step']}\n"
            f"Γ_min={g:.4f}  ε_Γ={eps:.4f}  |ε−α|={abs(eps - ALPHA_T):.4f}"
            if g is not None and eps is not None
            else f"post frame {fi+1}/{len(frames_idx)}"
        )
        return trail, head, info

    anim = FuncAnimation(fig, update, frames=len(frames_idx), interval=80, blit=False)
    anim.save(out_path, writer=PillowWriter(fps=12))
    plt.close(fig)


def main() -> None:
    verify_canonical_sources()
    print(f"Electron genesis dynamic phasor (shell-mean port {SAMPLE_PORT})")
    row = run_phasor_capture(trap_amp=TRAP_AMP)
    pca = row["pca_post_snap"]
    print(
        f"  snap@{row['snap_step']}  post_samples={row['n_post_samples']}"
        f"  TIR={row['tir_held']}"
    )
    print(
        f"  ε̄={row['eps_gamma_mean_post']:.4f}  |ε−α|={row['abs_eps_minus_alpha']:.4f}"
        f"  R/r={pca['R_over_r']:.3f} (φ²={PHI_SQ:.3f})"
    )

    gif_path = sim_output("electron_genesis_phasor.gif")
    png_path = sim_output("electron_genesis_phasor.png")
    render_gif(row, gif_path)
    render_static_png(row, png_path)
    print(f"  gif: {gif_path}")
    print(f"  png: {png_path}")

    payload = {k: v for k, v in row.items() if k != "records"}
    payload["n_trajectory_points"] = len(row["records"])
    out_json = OUT_DIR / "electron_genesis_phasor_results.json"
    out_json.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n")
    print(f"  json: {out_json}")


if __name__ == "__main__":
    main()
