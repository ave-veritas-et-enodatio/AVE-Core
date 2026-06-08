#!/usr/bin/env python3
r"""Genesis handoff: propagate at rest amp then ramp to wall amp on native engine.

Protocol
--------
1. Seed at amp_start (0.48×V_SNAP) on the left interior.
2. Propagate with co-moving longitudinal compression drive.
3. From ramp_start_step, linearly ramp target amplitude to amp_end (1.5)
   via soft co-moving sech bumps at the energy centroid (blend injection).

Tests whether motion + TIR can coexist during handoff (calibration crux).

Alpha comparison-only. Parent: native_electron_propagation.py adjudication.
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

PROJECT_ROOT = next(p for p in Path(__file__).resolve().parents if (p / ".git").exists())
OUT_DIR = PROJECT_ROOT / "src" / "scripts" / "vol_1_foundations" / "_output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

N_LATTICE = 32
PML = 4
N_STEPS = 420
CADENCE = 4
SEED_RADIUS = 2.5
SHELL_RADIUS = 6
V_DRIVE = 0.04
CX0_FRAC = 0.28
AMP_START = 0.48
AMP_END = 1.5
RAMP_START_STEP = 72
RAMP_END_STEP = 280
BUMP_BLEND = 0.12
BUMP_EVERY = 8

# Aggressive handoff (v2) — stronger co-moving injection
VARIANTS: list[dict[str, Any]] = [
    {"tag": "soft", "amp_end": 1.5, "bump_blend": 0.12, "bump_every": 8},
    {"tag": "strong", "amp_end": 2.0, "bump_blend": 0.32, "bump_every": 4},
]


def amp_schedule(step: int, amp_end: float) -> float:
    if step < RAMP_START_STEP:
        return AMP_START
    if step >= RAMP_END_STEP:
        return amp_end
    t = (step - RAMP_START_STEP) / (RAMP_END_STEP - RAMP_START_STEP)
    return AMP_START + t * (amp_end - AMP_START)


def add_sech_bump(
    engine: VacuumEngine3D,
    center: tuple[int, int, int],
    amplitude: float,
    radius: float,
    blend: float,
) -> None:
    """Soft additive sech bump — does not overwrite existing V_inc."""
    cx, cy, cz = center
    i, j, k = np.indices((engine.N, engine.N, engine.N))
    r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2)
    envelope = (amplitude / np.cosh(r / radius)) * blend
    envelope = envelope * engine.k4.mask_active.astype(float)
    for port in range(4):
        engine.k4.V_inc[..., port] += envelope / 2.0
    engine.k4.V_inc[~engine.k4.mask_active] = 0.0


def run_ramp(
    *,
    amp_end: float = AMP_END,
    bump_blend: float = BUMP_BLEND,
    bump_every: int = BUMP_EVERY,
    record_frames: bool = False,
) -> dict[str, Any]:
    n = N_LATTICE
    cx0 = int(CX0_FRAC * n)
    cy0 = cz0 = n // 2
    seed_center = (cx0, cy0, cz0)

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
    seed_sech_v_inc(engine, seed_center, AMP_START, SEED_RADIUS)
    engine.cos.initialize_electron_unknot_sector(
        R_target=0.5, r_target=0.25, amplitude_scale=min(AMP_START, 1.0)
    )

    mask = interior_mask(n, PML) & engine.k4.mask_active
    steps_log: list[int] = []
    amp_log: list[float] = []
    cx_log: list[float] = []
    gamma_log: list[float | None] = []
    a2_log: list[float] = []
    eps_log: list[float | None] = []
    frames_xz: list[np.ndarray] = []
    frames_amp_line: list[float] = []

    last_cx = float(cx0)

    for step in range(N_STEPS + 1):
        if step % CADENCE == 0:
            engine._coupled._update_z_local_total()
            z = np.asarray(engine.k4.z_local_field)
            v_sq = np.sum(np.asarray(engine.k4.V_inc) ** 2, axis=-1)
            rho = v_sq
            cx, cy, cz = energy_centroid(rho, mask)
            if np.isfinite(cx):
                last_cx = cx
            ic = (
                min(max(int(round(last_cx)), PML), n - PML - 1),
                min(max(int(round(cy if np.isfinite(cy) else cy0)), PML), n - PML - 1),
                min(max(int(round(cz if np.isfinite(cz) else cz0)), PML), n - PML - 1),
            )
            g = bond_gamma_min(z, engine.k4.mask_active, ic, SHELL_RADIUS)
            cur_amp = amp_schedule(step, amp_end)
            steps_log.append(step)
            amp_log.append(cur_amp)
            cx_log.append(last_cx)
            gamma_log.append(g)
            a2 = float(np.max(v_sq[mask])) if mask.any() else 0.0
            a2_log.append(a2)
            eps_log.append(float(1.0 - g**2) if g is not None else None)
            if record_frames:
                frames_xz.append(rho[:, cy0, :].T.copy())
                frames_amp_line.append(cur_amp)

        if step < N_STEPS:
            cur_amp = amp_schedule(step, amp_end)
            drive_cx = last_cx
            apply_co_moving_longitudinal_drive(engine, drive_cx, V_DRIVE)
            if step >= RAMP_START_STEP and step % bump_every == 0:
                ic = (
                    min(max(int(round(last_cx)), PML), n - PML - 1),
                    cy0,
                    cz0,
                )
                add_sech_bump(engine, ic, cur_amp, SEED_RADIUS, bump_blend)
                engine.cos.initialize_electron_unknot_sector(
                    R_target=0.5,
                    r_target=0.25,
                    amplitude_scale=min(cur_amp, 1.0),
                )
            engine.step()

    # Handoff windows
    ramp_idx = [i for i, s in enumerate(steps_log) if s >= RAMP_START_STEP]
    late_idx = [i for i, s in enumerate(steps_log) if s >= int(0.65 * N_STEPS)]

    x_start = cx_log[0] if cx_log else np.nan
    x_end = cx_log[-1] if cx_log else np.nan
    x_delta = x_end - x_start if np.isfinite(x_start) and np.isfinite(x_end) else np.nan
    x_delta_ramp = (
        cx_log[ramp_idx[-1]] - cx_log[ramp_idx[0]]
        if ramp_idx and len(cx_log) > ramp_idx[-1]
        else np.nan
    )

    gammas = [g for g in gamma_log if g is not None]
    gamma_min = float(min(gammas)) if gammas else None
    gamma_late = [gamma_log[i] for i in late_idx if gamma_log[i] is not None]
    gamma_min_late = float(min(gamma_late)) if gamma_late else None

    eps_vals = [e for e in eps_log if e is not None]
    eps_closest = min(eps_vals, key=lambda e: abs(e - EPS_ALPHA_TARGET)) if eps_vals else None

    tir_during_ramp = any(
        gamma_log[i] is not None and gamma_log[i] <= GAMMA_FULL_TIR
        for i in ramp_idx
    )
    moving_during_ramp = bool(np.isfinite(x_delta_ramp) and x_delta_ramp > 0.3)
    moving_late = bool(
        late_idx
        and len(cx_log) > late_idx[-1]
        and cx_log[late_idx[-1]] - cx_log[late_idx[0]] > 0.2
    )
    tir_late = bool(gamma_min_late is not None and gamma_min_late <= GAMMA_FULL_TIR)

    if tir_during_ramp and moving_during_ramp:
        verdict, outcome = "HANDOFF_MOTION_AND_TIR_OVERLAP", "A"
    elif tir_late and not moving_late:
        verdict, outcome = "RAMP_TO_TIR_THEN_PIN", "B"
    elif moving_late and not tir_late:
        verdict, outcome = "MOTION_WITHOUT_LATE_TIR", "C"
    else:
        verdict, outcome = "HANDOFF_INCONCLUSIVE", "D"

    return {
        "amp_start": AMP_START,
        "amp_end": amp_end,
        "ramp_start_step": RAMP_START_STEP,
        "ramp_end_step": RAMP_END_STEP,
        "bump_blend": bump_blend,
        "bump_every": bump_every,
        "centroid_x_start": x_start,
        "centroid_x_end": x_end,
        "centroid_x_delta_total": x_delta,
        "centroid_x_delta_during_ramp": x_delta_ramp,
        "gamma_min_trace": gamma_min,
        "gamma_min_late": gamma_min_late,
        "eps_closest_to_alpha": eps_closest,
        "abs_eps_closest_minus_alpha": abs(eps_closest - EPS_ALPHA_TARGET) if eps_closest else None,
        "tir_during_ramp": tir_during_ramp,
        "moving_during_ramp": moving_during_ramp,
        "tir_late": tir_late,
        "moving_late": moving_late,
        "verdict": verdict,
        "outcome": outcome,
        "alpha_used_as_input": False,
        "steps_log": steps_log,
        "amp_log": amp_log,
        "cx_log": cx_log,
        "gamma_log": gamma_log,
        "a2_log": a2_log,
        "eps_log": eps_log,
        "frames_xz": frames_xz if record_frames else None,
        "frames_amp_line": frames_amp_line if record_frames else None,
    }


def render_gif(result: dict[str, Any], out_path: Path) -> None:
    frames = result.get("frames_xz") or []
    if not frames:
        return
    n = frames[0].shape[1]
    vmax = float(np.percentile(np.stack(frames), 99.5))
    vmin = max(vmax * 1e-4, 1e-30)
    cx_log = result["cx_log"]
    gamma_log = result["gamma_log"]
    amp_log = result["amp_log"]

    fig, (ax_im, ax_tr) = plt.subplots(2, 1, figsize=(10, 8), gridspec_kw={"height_ratios": [2, 1]})
    fig.patch.set_facecolor("#0a0a12")
    ax_im.set_facecolor("#111118")
    ax_tr.set_facecolor("#111118")

    im = ax_im.imshow(
        frames[0],
        origin="lower",
        cmap="inferno",
        norm=mcolors.LogNorm(vmin=vmin, vmax=vmax),
        extent=[0, n, 0, n],
        aspect="equal",
    )
    (trail,) = ax_im.plot([], [], color="#00e5ff", lw=1.5)
    (dot,) = ax_im.plot([], [], "o", color="yellow", markersize=7)
    ax_im.set_xlabel("x", color="#ccc")
    ax_im.set_ylabel("z", color="#ccc")
    ax_im.set_title("xz slice |V_inc|²", color="#eee")

    steps = result["steps_log"]
    ax_tr.plot(steps, amp_log, color="#f90", label="amp schedule", lw=1.2)
    ax_tr2 = ax_tr.twinx()
    gam_plot = [g if g is not None else np.nan for g in gamma_log]
    ax_tr2.plot(steps, gam_plot, color="#6cf", label="Γ_min", lw=1.2)
    ax_tr.axvline(RAMP_START_STEP, color="#666", ls="--", lw=0.8)
    ax_tr.axvline(RAMP_END_STEP, color="#666", ls="--", lw=0.8)
    ax_tr.set_xlabel("step", color="#ccc")
    ax_tr.set_ylabel("V_SNAP fraction", color="#f90")
    ax_tr2.set_ylabel("Γ_min", color="#6cf")
    ax_tr.tick_params(colors="#bbb")
    ax_tr2.tick_params(colors="#bbb")
    fig.suptitle(
        f"Genesis ramp {AMP_START}→{AMP_END}  |  {result['verdict']}",
        color="#eee",
        fontsize=12,
    )
    info = fig.text(0.02, 0.01, "", color="#aaa", fontsize=9, family="monospace")
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    cz = N_LATTICE // 2

    def update(i: int):
        im.set_data(frames[i])
        xs = cx_log[: i + 1]
        if xs:
            trail.set_data(xs, [cz] * len(xs))
            dot.set_data([xs[-1]], [cz])
        g = gamma_log[i]
        info.set_text(
            f"step={steps[i]}  amp={amp_log[i]:.2f}  cx={cx_log[i]:.1f}  "
            f"Γ={g:.4f}" if g is not None else f"step={steps[i]}  amp={amp_log[i]:.2f}"
        )
        return im, trail, dot, info

    anim = FuncAnimation(fig, update, frames=len(frames), interval=80, blit=False)
    anim.save(out_path, writer=PillowWriter(fps=12), dpi=110, savefig_kwargs={"facecolor": "#0a0a12"})
    plt.close(fig)


def main() -> None:
    verify_canonical_sources()
    rows: list[dict[str, Any]] = []
    gif_path = None
    for i, variant in enumerate(VARIANTS):
        result = run_ramp(
            amp_end=variant["amp_end"],
            bump_blend=variant["bump_blend"],
            bump_every=variant["bump_every"],
            record_frames=(i == len(VARIANTS) - 1),
        )
        result["tag"] = variant["tag"]
        rows.append({k: v for k, v in result.items() if k not in ("frames_xz", "frames_amp_line")})
        if i == len(VARIANTS) - 1:
            gif_path = sim_output("native_electron_propagation_ramp.gif")
            render_gif(result, gif_path)

    payload = {"variants": rows, "gif_path": str(gif_path) if gif_path else None}
    out_json = OUT_DIR / "native_electron_propagation_ramp_results.json"
    out_json.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n")

    print("Native electron propagation ramp")
    for row in rows:
        print(
            f"  [{row['tag']}] {row['verdict']} ({row['outcome']})"
            f"  Δx={row['centroid_x_delta_total']:.2f}"
            f"  Γ_min={row['gamma_min_trace']}"
            f"  tir@ramp={row['tir_during_ramp']}"
        )
    if gif_path:
        print(f"  gif: {gif_path}")
    print(f"  wrote: {out_json}")


if __name__ == "__main__":
    main()
