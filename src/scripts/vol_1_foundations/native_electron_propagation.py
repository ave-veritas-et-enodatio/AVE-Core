#!/usr/bin/env python3
r"""Native VacuumEngine3D: translating electron-defect + bond-Γ trail.

Tests whether a seeded sub-yield / wall-scale defect can translate on the
coupled native engine while developing local TIR readout at the moving core.

HONEST FRAMING
--------------
Not a free Γ=-1 soliton (pinned at saturation per motion_stability probe).
Uses curl-free longitudinal compression bias (de Broglie bulk channel) to
drag the defect; bond-Γ read at the energy centroid each cadence.

Alpha comparison-only. Reuses bond-Γ helpers from native_k4_gamma_ceiling.

Output:
  assets/sim_outputs/native_electron_propagation.gif
  src/scripts/vol_1_foundations/_output/native_electron_propagation_results.json
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

from native_k4_gamma_ceiling import (  # noqa: E402
    EPS_ALPHA_TARGET,
    GAMMA_FULL_TIR,
    bond_gamma_min,
    seed_sech_v_inc,
    verify_canonical_sources,
)

from ave.core.constants import ALPHA_COLD, V_SNAP  # noqa: E402
from ave.topological.cosserat_field_3d import tetrahedral_gradient  # noqa: E402
from ave.topological.vacuum_engine import VacuumEngine3D  # noqa: E402
from ave_path_util import sim_output  # noqa: E402

PROJECT_ROOT = next(p for p in Path(__file__).resolve().parents if (p / ".git").exists())
OUT_DIR = PROJECT_ROOT / "src" / "scripts" / "vol_1_foundations" / "_output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

N_LATTICE = 32
PML = 4
N_STEPS = 360
CADENCE = 4
SEED_RADIUS = 2.5
SHELL_RADIUS = 6
V_DRIVE = 0.04
CX0_FRAC = 0.28
AMPLITUDES = [0.48, 1.0, 1.5]


def interior_mask(n: int, pml: int) -> np.ndarray:
    m = np.zeros((n, n, n), dtype=bool)
    m[pml : n - pml, pml : n - pml, pml : n - pml] = True
    return m


def energy_centroid(rho: np.ndarray, mask: np.ndarray) -> tuple[float, float, float]:
    vals = rho * mask
    total = float(vals.sum())
    if total <= 0.0:
        return (np.nan, np.nan, np.nan)
    i, j, k = np.indices(rho.shape)
    cx = float((i * vals).sum() / total)
    cy = float((j * vals).sum() / total)
    cz = float((k * vals).sum() / total)
    return cx, cy, cz


def apply_co_moving_longitudinal_drive(
    engine: VacuumEngine3D,
    cx: float,
    v_drive: float,
    *,
    sigma_frac: float = 0.16,
) -> None:
    """Curl-free +x compression dipole centered at cx (motion_stability variant A)."""
    if v_drive == 0.0:
        return
    n = engine.N
    i, j, k = np.indices((n, n, n), dtype=float)
    r2 = (i - cx) ** 2 + (j - cx) ** 2 + (k - cx) ** 2
    sigma = max(3.0, sigma_frac * n)
    phi = (i - cx) * np.exp(-r2 / (2.0 * sigma**2))
    grad = np.asarray(tetrahedral_gradient(phi)) / engine.cos.dx
    field = v_drive * grad
    field[~engine.cos.mask_alive] = 0.0
    engine.cos.u_dot[...] = engine.cos.u_dot + field
    engine.cos.u_dot[~engine.cos.mask_alive] = 0.0


def run_amplitude(
    amplitude: float,
    *,
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
    seed_sech_v_inc(engine, seed_center, amplitude, SEED_RADIUS)
    engine.cos.initialize_electron_unknot_sector(
        R_target=0.5, r_target=0.25, amplitude_scale=min(amplitude, 1.0)
    )

    mask = interior_mask(n, PML) & engine.k4.mask_active
    cx_trail: list[float] = []
    gamma_trail: list[float | None] = []
    a2_trail: list[float] = []
    eps_trail: list[float | None] = []
    frames_xz: list[np.ndarray] = []

    for step in range(N_STEPS + 1):
        if step % CADENCE == 0:
            engine._coupled._update_z_local_total()
            z = np.asarray(engine.k4.z_local_field)
            v_sq = np.sum(np.asarray(engine.k4.V_inc) ** 2, axis=-1)
            rho = v_sq
            cx, cy, cz = energy_centroid(rho, mask)
            ic = (int(round(cx)), int(round(cy)), int(round(cz)))
            ic = (
                min(max(ic[0], PML), n - PML - 1),
                min(max(ic[1], PML), n - PML - 1),
                min(max(ic[2], PML), n - PML - 1),
            )
            g = bond_gamma_min(z, engine.k4.mask_active, ic, SHELL_RADIUS)
            a2 = float(np.max(v_sq[mask])) if mask.any() else 0.0
            cx_trail.append(cx)
            gamma_trail.append(g)
            a2_trail.append(a2)
            eps_trail.append(float(1.0 - g**2) if g is not None else None)
            if record_frames:
                slab = rho[:, cy0, :].T
                frames_xz.append(slab.copy())

        if step < N_STEPS:
            # Co-moving compression bias tracks centroid when defined, else seed x.
            drive_cx = cx_trail[-1] if cx_trail and np.isfinite(cx_trail[-1]) else float(cx0)
            apply_co_moving_longitudinal_drive(engine, drive_cx, V_DRIVE)
            engine.step()

    x_start = cx_trail[0] if cx_trail else np.nan
    x_end = cx_trail[-1] if cx_trail else np.nan
    x_delta = x_end - x_start if np.isfinite(x_start) and np.isfinite(x_end) else np.nan
    gammas = [g for g in gamma_trail if g is not None]
    gamma_min = float(min(gammas)) if gammas else None
    eps_at_min = float(1.0 - gamma_min**2) if gamma_min is not None else None
    eps_vals = [e for e in eps_trail if e is not None]
    eps_closest_alpha = min(eps_vals, key=lambda e: abs(e - EPS_ALPHA_TARGET)) if eps_vals else None

    return {
        "amplitude_V_SNAP": amplitude,
        "seed_center": seed_center,
        "v_drive": V_DRIVE,
        "centroid_x_start": x_start,
        "centroid_x_end": x_end,
        "centroid_x_delta": x_delta,
        "centroid_moved": bool(np.isfinite(x_delta) and x_delta > 0.5),
        "A_squared_peak_v_inc": float(max(a2_trail)) if a2_trail else 0.0,
        "gamma_min_at_centroid": gamma_min,
        "eps_at_gamma_min": eps_at_min,
        "eps_closest_to_alpha": eps_closest_alpha,
        "abs_eps_closest_minus_alpha": (
            abs(eps_closest_alpha - EPS_ALPHA_TARGET) if eps_closest_alpha is not None else None
        ),
        "gamma_full_tir_pass": bool(gamma_min is not None and gamma_min <= GAMMA_FULL_TIR),
        "alpha_used_as_input": False,
        "frames_xz": frames_xz if record_frames else None,
        "cx_trail": cx_trail if record_frames else None,
        "gamma_trail": gamma_trail if record_frames else None,
    }


def classify(rows: list[dict[str, Any]]) -> dict[str, Any]:
    moved = [r for r in rows if r.get("centroid_moved")]
    tir = [r for r in rows if r.get("gamma_full_tir_pass")]
    rest = next((r for r in rows if abs(r["amplitude_V_SNAP"] - 0.48) < 0.01), None)
    wall = max(rows, key=lambda r: r["amplitude_V_SNAP"])

    if moved and tir:
        verdict = "PROPAGATION_WITH_TIR_AT_WALL"
        outcome = "A"
    elif moved and not tir:
        verdict = "PROPAGATION_WITHOUT_FULL_TIR"
        outcome = "B"
    elif not moved and tir:
        verdict = "TIR_WITHOUT_TRANSLATION"
        outcome = "C"
    else:
        verdict = "PINNED_NO_TIR"
        outcome = "D"

    return {
        "verdict": verdict,
        "outcome": outcome,
        "any_centroid_moved": bool(moved),
        "any_full_tir": bool(tir),
        "rest_row": {k: rest[k] for k in rest if k not in ("frames_xz", "cx_trail", "gamma_trail")} if rest else None,
        "wall_row": {k: wall[k] for k in wall if k not in ("frames_xz", "cx_trail", "gamma_trail")},
        "comparison_only_alpha": float(ALPHA_COLD),
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
    (trail_line,) = ax.plot([], [], color="#00e5ff", lw=1.5, alpha=0.85)
    (cent_dot,) = ax.plot([], [], "o", color="yellow", markersize=8)
    ax.set_xlabel("x", color="#ccc")
    ax.set_ylabel("z", color="#ccc")
    fig.suptitle(
        f"Native propagation  amp={row['amplitude_V_SNAP']:.2f}×V_SNAP  "
        f"(xz @ y={N_LATTICE//2})",
        color="#eee",
        fontsize=12,
    )
    info = fig.text(0.02, 0.02, "", color="#aaa", fontsize=9, family="monospace")
    plt.colorbar(im, ax=ax, fraction=0.046, label="|V_inc|² (log)")

    cx_trail = row.get("cx_trail") or []
    gamma_trail = row.get("gamma_trail") or []
    cz_fixed = N_LATTICE // 2

    def update(i: int):
        im.set_data(frames[i])
        xs = cx_trail[: i + 1]
        zs = [cz_fixed] * len(xs)
        if xs:
            trail_line.set_data(xs, zs)
            cent_dot.set_data([xs[-1]], [zs[-1]])
        g = gamma_trail[i] if i < len(gamma_trail) else None
        info.set_text(
            f"frame {i+1}/{len(frames)}  cx={xs[-1]:.1f}  "
            f"Γ_min={g:.4f}" if g is not None else f"frame {i+1}/{len(frames)}"
        )
        return im, trail_line, cent_dot, info

    anim = FuncAnimation(fig, update, frames=len(frames), interval=80, blit=False)
    anim.save(out_path, writer=PillowWriter(fps=12), dpi=110, savefig_kwargs={"facecolor": "#0a0a12"})
    plt.close(fig)


def main() -> None:
    verify_canonical_sources()
    rows = []
    gif_row = None
    for amp in AMPLITUDES:
        record = amp == 1.5
        row = run_amplitude(amp, record_frames=record)
        if record:
            gif_row = row
        rows.append({k: v for k, v in row.items() if k not in ("frames_xz", "cx_trail", "gamma_trail")})

    classification = classify([{**r, **({"centroid_moved": r["centroid_moved"]})} for r in rows])

    gif_path = sim_output("native_electron_propagation.gif")
    if gif_row:
        render_gif(gif_row, gif_path)

    payload = {
        "scope": "native VacuumEngine3D translating defect + bond-Γ at centroid",
        "amplitudes_V_SNAP": AMPLITUDES,
        "rows": rows,
        "classification": classification,
        "gif_amp": 1.5,
        "gif_path": str(gif_path) if gif_row else None,
    }
    out_json = OUT_DIR / "native_electron_propagation_results.json"
    out_json.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n")

    print("Native electron propagation")
    print(f"  verdict: {classification['verdict']} ({classification['outcome']})")
    for row in rows:
        print(
            f"  amp={row['amplitude_V_SNAP']:.2f}  Δx={row['centroid_x_delta']:.2f}"
            f"  moved={row['centroid_moved']}  Γ_min={row['gamma_min_at_centroid']}"
            f"  eps={row['eps_at_gamma_min']}"
        )
    if gif_row:
        print(f"  gif: {gif_path}")
    print(f"  wrote: {out_json}")


if __name__ == "__main__":
    main()
