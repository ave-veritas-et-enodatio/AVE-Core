#!/usr/bin/env python3
r"""Alpha-free snap genesis: propagate sub-yield → geometry-triggered wall trap.

Prereg: research/2026-06-08_electron-genesis-snap-prereg.md
Adjudication: research/2026-06-08_alpha-engine-input-adjudication.md
  - Inherits √α yield via axiom_4 (structural) — does NOT import α into snap logic.
  - No PairNucleationGate default (δ_lock ≠ ALPHA).
  - Snap = full seed_sech_v_inc replace at trap_amp when geometry criteria fire.

Trigger modes
-------------
  position   — replicate reseed handoff (cx ≥ trigger_x)
  autoresonant — motion + Meissner rise + measured-ε lock only
  hybrid     — first of autoresonant OR position (primary)

Output:
  assets/sim_outputs/electron_genesis_snap.gif
  src/scripts/vol_1_foundations/_output/electron_genesis_snap_results.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Literal

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
from ave.topological.vacuum_engine import PairNucleationGate, VacuumEngine3D  # noqa: E402
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
TRAP_AMP = 1.5
TRIGGER_X = 14.0
CX0_FRAC = 0.28
MOVE_MIN = 6.0
SAT_FRAC = 0.85
EPS_FLOOR = 0.01
EXPLICIT_DELTA_LOCK_FRAC = 0.02

SnapMode = Literal["position", "autoresonant", "hybrid"]

# Field helpers only — never register gate as observer (no Beltrami injection path).
_FIELD_HELPER = PairNucleationGate(delta_lock_fraction=EXPLICIT_DELTA_LOCK_FRAC)


def _core_idx(cx: float, cy0: int, cz0: int, n: int) -> tuple[int, int, int]:
    return (
        min(max(int(round(cx)), PML), n - PML - 1),
        cy0,
        cz0,
    )


def _drive_omega(engine: VacuumEngine3D) -> float:
    for src in engine._sources:
        if hasattr(src, "_omega_current"):
            return float(src._omega_current)
        if hasattr(src, "omega"):
            return float(src.omega)
    return float(engine.cos.omega_yield)


def _measured_delta_lock(omega_drive: float, gamma: float | None) -> float:
    if gamma is None:
        eps = EPS_FLOOR
    else:
        eps = max(float(1.0 - gamma**2), EPS_FLOOR)
    return omega_drive * eps


def _autoresonant_ready(
    engine: VacuumEngine3D,
    core: tuple[int, int, int],
    gamma: float | None,
    cx0: float,
    cx: float,
) -> tuple[bool, dict[str, float]]:
    A2 = _FIELD_HELPER._compute_A2_mu(engine)
    Omega = _FIELD_HELPER._compute_Omega_node(engine)
    a2_core = float(A2[core])
    omega_node = float(Omega[core])
    omega_drive = _drive_omega(engine)
    delta_lock = _measured_delta_lock(omega_drive, gamma)
    lock_err = abs(omega_node - omega_drive)
    moved = bool(np.isfinite(cx) and (cx - cx0) >= MOVE_MIN)
    meissner = a2_core >= SAT_FRAC
    locked = lock_err < delta_lock
    ready = moved and meissner and locked
    return ready, {
        "a2_core": a2_core,
        "omega_node": omega_node,
        "omega_drive": omega_drive,
        "delta_lock": delta_lock,
        "lock_err": lock_err,
        "moved": float(moved),
        "meissner": float(meissner),
        "locked": float(locked),
    }


def _position_ready(cx: float) -> bool:
    return bool(np.isfinite(cx) and cx >= TRIGGER_X)


def _should_snap(
    mode: SnapMode,
    engine: VacuumEngine3D,
    core: tuple[int, int, int],
    gamma: float | None,
    cx0: float,
    cx: float,
) -> tuple[bool, str, dict[str, float]]:
    auto, metrics = _autoresonant_ready(engine, core, gamma, cx0, cx)
    pos = _position_ready(cx)
    if mode == "position":
        return pos, "position", metrics
    if mode == "autoresonant":
        return auto, "autoresonant", metrics
    if auto:
        return True, "autoresonant", metrics
    if pos:
        return True, "position", metrics
    return False, "none", metrics


def run_snap(mode: SnapMode, *, record_frames: bool = False) -> dict[str, Any]:
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
    snap_trigger: str | None = None
    snap_center: tuple[int, int, int] | None = None
    steps_log: list[int] = []
    cx_log: list[float] = []
    gamma_log: list[float | None] = []
    phase_log: list[str] = []
    trigger_log: list[str] = []
    frames_xz: list[np.ndarray] = []

    last_cx = float(cx0)

    for step in range(N_STEPS + 1):
        if step % CADENCE == 0:
            engine._coupled._update_z_local_total()
            z = np.asarray(engine.k4.z_local_field)
            v_sq = np.sum(np.asarray(engine.k4.V_inc) ** 2, axis=-1)
            cx, _, _ = energy_centroid(v_sq, mask)
            if np.isfinite(cx):
                last_cx = cx
            core = _core_idx(last_cx, cy0, cz0, n)
            g = bond_gamma_min(z, engine.k4.mask_active, core, SHELL_RADIUS)
            phase = "post_snap" if snap_step is not None else "pre_propagate"
            steps_log.append(step)
            cx_log.append(last_cx)
            gamma_log.append(g)
            phase_log.append(phase)
            trigger_log.append(snap_trigger or "pending")
            if record_frames:
                frames_xz.append(v_sq[:, cy0, :].T.copy())

        if step < N_STEPS and snap_step is None:
            core = _core_idx(last_cx, cy0, cz0, n)
            engine._coupled._update_z_local_total()
            z = np.asarray(engine.k4.z_local_field)
            g_now = bond_gamma_min(z, engine.k4.mask_active, core, SHELL_RADIUS)
            fire, trig, _ = _should_snap(mode, engine, core, g_now, float(cx0), last_cx)
            if fire:
                seed_sech_v_inc(engine, core, TRAP_AMP, SEED_RADIUS)
                engine.cos.initialize_electron_unknot_sector(
                    R_target=0.5, r_target=0.25, amplitude_scale=min(TRAP_AMP, 1.0)
                )
                snap_step = step
                snap_trigger = trig
                snap_center = core
                last_cx = float(core[0])

        v_drive = V_DRIVE_POST if snap_step is not None else V_DRIVE_PRE
        if v_drive > 0:
            apply_co_moving_longitudinal_drive(engine, last_cx, v_drive)
        if step < N_STEPS:
            engine.step()

    pre_idx = [i for i, p in enumerate(phase_log) if p == "pre_propagate"]
    post_idx = [i for i, p in enumerate(phase_log) if p == "post_snap"]

    x_pre_delta = (
        cx_log[pre_idx[-1]] - cx_log[pre_idx[0]] if len(pre_idx) >= 2 else None
    )
    x_post_delta = (
        cx_log[post_idx[-1]] - cx_log[post_idx[0]] if len(post_idx) >= 2 else None
    )

    gammas_post = [gamma_log[i] for i in post_idx if gamma_log[i] is not None]
    gamma_min_post = float(min(gammas_post)) if gammas_post else None
    gamma_min_all = float(min(g for g in gamma_log if g is not None)) if any(
        g is not None for g in gamma_log
    ) else None

    tir_post = bool(gamma_min_post is not None and gamma_min_post <= GAMMA_FULL_TIR)
    pinned_post = bool(
        x_post_delta is not None and np.isfinite(x_post_delta) and abs(x_post_delta) < 0.4
    )
    moved_pre = bool(
        x_pre_delta is not None and np.isfinite(x_pre_delta) and x_pre_delta > 2.0
    )

    if tir_post and pinned_post and moved_pre:
        verdict, outcome = "SNAP_TRAP_PINNED_WITH_TIR", "A"
    elif tir_post and moved_pre:
        verdict, outcome = "SNAP_TRAP_TIR_PARTIAL_PIN", "B"
    elif snap_step is None:
        verdict, outcome = "SNAP_NEVER_FIRED", "C"
    elif moved_pre and not tir_post:
        verdict, outcome = "SNAP_NO_TIR", "D"
    else:
        verdict, outcome = "SNAP_HANDOFF_FAIL", "E"

    eps_post = float(1.0 - gamma_min_post**2) if gamma_min_post is not None else None

    return {
        "snap_mode": mode,
        "trap_amp": TRAP_AMP,
        "amp_start": AMP_START,
        "trigger_x_fallback": TRIGGER_X,
        "snap_step": snap_step,
        "snap_trigger": snap_trigger,
        "snap_center": list(snap_center) if snap_center else None,
        "moved_pre_snap": moved_pre,
        "x_delta_pre": x_pre_delta,
        "x_delta_post": x_post_delta,
        "pinned_post": pinned_post,
        "gamma_min_post_snap": gamma_min_post,
        "gamma_min_all": gamma_min_all,
        "eps_post_snap": eps_post,
        "abs_eps_post_minus_alpha": abs(eps_post - EPS_ALPHA_TARGET) if eps_post else None,
        "tir_post": tir_post,
        "verdict": verdict,
        "outcome": outcome,
        "alpha_used_as_input": False,
        "delta_lock_source": "measured_eps",
        "explicit_delta_lock_fraction": EXPLICIT_DELTA_LOCK_FRAC,
        "steps_log": steps_log,
        "cx_log": cx_log,
        "gamma_log": gamma_log,
        "phase_log": phase_log,
        "trigger_log": trigger_log,
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
        f"Snap genesis ({row['snap_mode']}) @ trap={row['trap_amp']:.1f}  |  {row['verdict']}",
        color="#eee",
        fontsize=11,
    )
    cx_log = row["cx_log"]
    cz = N_LATTICE // 2

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
    modes: list[SnapMode] = ["position", "autoresonant", "hybrid"]
    rows = []
    gif_row = None
    for i, mode in enumerate(modes):
        row = run_snap(mode, record_frames=(mode == "hybrid"))
        if mode == "hybrid":
            gif_row = row
        rows.append({k: v for k, v in row.items() if k != "frames_xz"})

    gif_path = sim_output("electron_genesis_snap.gif")
    if gif_row:
        render_gif(gif_row, gif_path)

    payload = {
        "adjudication": "research/2026-06-08_alpha-engine-input-adjudication.md",
        "verdict_summary": "NO engine alpha removal; alpha-free snap triggers only",
        "variants": rows,
        "gif_path": str(gif_path) if gif_row else None,
    }
    out_json = OUT_DIR / "electron_genesis_snap_results.json"
    out_json.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n")

    print("Electron genesis snap (alpha-free triggers)")
    for row in rows:
        print(
            f"  mode={row['snap_mode']:12s}  {row['verdict']} ({row['outcome']})"
            f"  trigger={row['snap_trigger']}  step={row['snap_step']}"
            f"  Γ_post={row['gamma_min_post_snap']}"
            f"  Δx_pre={row['x_delta_pre']}  Δx_post={row['x_delta_post']}"
        )
    if gif_row:
        print(f"  gif: {gif_path}")
    print(f"  wrote: {out_json}")


if __name__ == "__main__":
    main()
