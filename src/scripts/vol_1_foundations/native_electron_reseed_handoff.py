#!/usr/bin/env python3
r"""Full re-seed handoff: propagate sub-yield, then replace with wall-scale trap.

Protocol
--------
1. Seed 0.48×V_SNAP left; longitudinal drive until centroid x ≥ trigger_x.
2. **Full** seed_sech_v_inc replace at centroid (not additive bump).
3. Continue with reduced / zero drive; read Γ at core and centroid motion.

Parent: native_electron_propagation_ramp (additive ramp failed).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors as mcolors
from matplotlib.animation import FuncAnimation, PillowWriter

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from native_electron_propagation import (  # noqa: E402
    apply_co_moving_longitudinal_drive,
    energy_centroid,
    interior_mask,
)
from native_k4_gamma_ceiling import (  # noqa: E402
    EPS_ALPHA_TARGET,
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
N_STEPS = 400
CADENCE = 4
SEED_RADIUS = 2.5
SHELL_RADIUS = 6
V_DRIVE_PRE = 0.04
V_DRIVE_POST = 0.0
AMP_START = 0.48
TRIGGER_X = 14.0
CX0_FRAC = 0.28

TRAP_AMPS = [1.0, 1.5, 2.0]


def run_reseed(trap_amp: float, *, record_frames: bool = False) -> dict[str, Any]:
    n = N_LATTICE
    cx0 = int(CX0_FRAC * n)
    cy0 = cz0 = n // 2
    mask = None
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

    reseed_step: int | None = None
    reseed_center: tuple[int, int, int] | None = None
    steps_log: list[int] = []
    cx_log: list[float] = []
    gamma_log: list[float | None] = []
    phase_log: list[str] = []
    frames_xz: list[np.ndarray] = []

    last_cx = float(cx0)

    for step in range(N_STEPS + 1):
        if step % CADENCE == 0:
            engine._coupled._update_z_local_total()
            z = np.asarray(engine.k4.z_local_field)
            v_sq = np.sum(np.asarray(engine.k4.V_inc) ** 2, axis=-1)
            cx, cy, cz = energy_centroid(v_sq, mask)
            if np.isfinite(cx):
                last_cx = cx
            ic = (
                min(max(int(round(last_cx)), PML), n - PML - 1),
                cy0,
                cz0,
            )
            g = bond_gamma_min(z, engine.k4.mask_active, ic, SHELL_RADIUS)
            phase = "post_trap" if reseed_step is not None else "pre_propagate"
            steps_log.append(step)
            cx_log.append(last_cx)
            gamma_log.append(g)
            phase_log.append(phase)
            if record_frames:
                frames_xz.append(v_sq[:, cy0, :].T.copy())

        if step < N_STEPS:
            if reseed_step is None and last_cx >= TRIGGER_X:
                ic = (
                    min(max(int(round(last_cx)), PML), n - PML - 1),
                    cy0,
                    cz0,
                )
                seed_sech_v_inc(engine, ic, trap_amp, SEED_RADIUS)
                engine.cos.initialize_electron_unknot_sector(
                    R_target=0.5, r_target=0.25, amplitude_scale=min(trap_amp, 1.0)
                )
                reseed_step = step
                reseed_center = ic
                last_cx = float(ic[0])

            v_drive = V_DRIVE_POST if reseed_step is not None else V_DRIVE_PRE
            if v_drive > 0:
                apply_co_moving_longitudinal_drive(engine, last_cx, v_drive)
            engine.step()

    pre_idx = [i for i, p in enumerate(phase_log) if p == "pre_propagate"]
    post_idx = [i for i, p in enumerate(phase_log) if p == "post_trap"]

    x_pre_delta = (
        cx_log[pre_idx[-1]] - cx_log[pre_idx[0]] if len(pre_idx) >= 2 else np.nan
    )
    x_post_delta = (
        cx_log[post_idx[-1]] - cx_log[post_idx[0]] if len(post_idx) >= 2 else np.nan
    )

    gammas_post = [gamma_log[i] for i in post_idx if gamma_log[i] is not None]
    gamma_min_post = float(min(gammas_post)) if gammas_post else None
    gamma_min_all = float(min(g for g in gamma_log if g is not None)) if any(
        g is not None for g in gamma_log
    ) else None

    tir_post = bool(gamma_min_post is not None and gamma_min_post <= GAMMA_FULL_TIR)
    pinned_post = bool(np.isfinite(x_post_delta) and abs(x_post_delta) < 0.4)
    moved_pre = bool(np.isfinite(x_pre_delta) and x_pre_delta > 2.0)

    if tir_post and pinned_post and moved_pre:
        verdict, outcome = "TRAP_AT_MOTION_SITE_PINNED_WITH_TIR", "A"
    elif tir_post and moved_pre:
        verdict, outcome = "TRAP_WITH_TIR_PARTIAL_MOTION", "B"
    elif tir_post:
        verdict, outcome = "TRAP_TIR_NO_PRIOR_MOTION", "C"
    elif moved_pre and not tir_post:
        verdict, outcome = "MOTION_NO_TRAP", "D"
    else:
        verdict, outcome = "HANDOFF_FAIL", "E"

    eps_post = float(1.0 - gamma_min_post**2) if gamma_min_post is not None else None

    return {
        "trap_amp": trap_amp,
        "trigger_x": TRIGGER_X,
        "reseed_step": reseed_step,
        "reseed_center": list(reseed_center) if reseed_center else None,
        "moved_pre_reseed": moved_pre,
        "x_delta_pre": x_pre_delta,
        "x_delta_post": x_post_delta,
        "pinned_post": pinned_post,
        "gamma_min_post_trap": gamma_min_post,
        "gamma_min_all": gamma_min_all,
        "eps_post_trap": eps_post,
        "abs_eps_post_minus_alpha": abs(eps_post - EPS_ALPHA_TARGET) if eps_post else None,
        "tir_post": tir_post,
        "verdict": verdict,
        "outcome": outcome,
        "alpha_used_as_input": False,
        "steps_log": steps_log,
        "cx_log": cx_log,
        "gamma_log": gamma_log,
        "phase_log": phase_log,
        "frames_xz": frames_xz if record_frames else None,
    }


def render_gif(row: dict[str, Any], out_path: Path) -> None:
    frames = row.get("frames_xz") or []
    if not frames:
        return
    n = frames[0].shape[1]
    vmax = float(np.percentile(np.stack(frames), 99.5))
    vmin = max(vmax * 1e-4, 1e-30)
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor("#0a0a12")
    ax.set_facecolor("#111118")
    im = ax.imshow(
        frames[0],
        origin="lower",
        cmap="inferno",
        norm=mcolors.LogNorm(vmin=vmin, vmax=vmax),
        extent=[0, n, 0, n],
        aspect="equal",
    )
    (trail,) = ax.plot([], [], color="#00e5ff", lw=1.5)
    ax.axvline(TRIGGER_X, color="#666", ls="--", lw=0.8)
    fig.suptitle(
        f"Full re-seed @ trap_amp={row['trap_amp']:.1f}  |  {row['verdict']}",
        color="#eee",
        fontsize=11,
    )
    cx_log = row["cx_log"]
    cz = N_LATTICE // 2
    rs = row.get("reseed_step")

    def update(i: int):
        im.set_data(frames[i])
        xs = cx_log[: i + 1]
        trail.set_data(xs, [cz] * len(xs))
        return im, trail

    anim = FuncAnimation(fig, update, frames=len(frames), interval=80, blit=False)
    anim.save(out_path, writer=PillowWriter(fps=12), dpi=110, savefig_kwargs={"facecolor": "#0a0a12"})
    plt.close(fig)


def main() -> None:
    verify_canonical_sources()
    rows = []
    gif_row = None
    for i, amp in enumerate(TRAP_AMPS):
        row = run_reseed(amp, record_frames=(i == len(TRAP_AMPS) - 1))
        if i == len(TRAP_AMPS) - 1:
            gif_row = row
        rows.append({k: v for k, v in row.items() if k != "frames_xz"})

    gif_path = sim_output("native_electron_reseed_handoff.gif")
    if gif_row:
        render_gif(gif_row, gif_path)

    payload = {"variants": rows, "gif_path": str(gif_path) if gif_row else None}
    out_json = OUT_DIR / "native_electron_reseed_handoff_results.json"
    out_json.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n")

    print("Native electron reseed handoff")
    for row in rows:
        print(
            f"  trap={row['trap_amp']:.1f}  {row['verdict']} ({row['outcome']})"
            f"  reseed@step={row['reseed_step']}  Γ_post={row['gamma_min_post_trap']}"
            f"  Δx_pre={row['x_delta_pre']:.1f}  Δx_post={row['x_delta_post']:.2f}"
        )
    if gif_row:
        print(f"  gif: {gif_path}")
    print(f"  wrote: {out_json}")


if __name__ == "__main__":
    main()
