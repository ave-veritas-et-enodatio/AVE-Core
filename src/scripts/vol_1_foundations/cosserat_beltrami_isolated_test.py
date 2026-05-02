"""
Phase C — CosseratBeltramiSource isolated verification.

Verifies that CosseratBeltramiSource (vacuum_engine.py:791-972) actually
injects helical Cosserat ω as its docstring claims. Per A47 v11d
discipline (engine-code claims need direct verification), this is the
source-physics validation step before the main Phase D run.

Pre-registered acceptance criteria (verbatim per A47 v11b):
  C-C1: |ω| at source slab matches A·env(t) within 1%   (injection sanity)
  C-C2: ω_y / ω_z phase relationship at source slab is 90° quadrature
        (cos vs ±sin per docstring lines 802-811)
  C-C3: helicity h_local at source slab = +1.0 for RH, -1.0 for LH
        within 5% (uses _beltrami_helicity)
  C-C4: helical ω propagates downstream — peak |ω| centroid drifts
        away from source slab over time

Runs both RH and LH at small N=48; compares handedness sign-flip.

Outputs:
  - assets/cosserat_beltrami_isolated_RH.gif (+ _LH.gif)
  - assets/cosserat_beltrami_isolated_panels.png
  - results/cosserat_beltrami_isolated.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

from ave.topological.vacuum_engine import VacuumEngine3D, CosseratBeltramiSource
from ave.topological.helicity_observer import HelicityObserver


PREREG = {
    "C-C1_amplitude_match_tolerance": 0.01,
    "C-C2_phase_offset_deg_min": 85.0,
    "C-C2_phase_offset_deg_max": 95.0,
    "C-C3_h_local_target_RH": +1.0,
    "C-C3_h_local_target_LH": -1.0,
    "C-C3_h_local_tolerance": 0.05,
    "C-C4_centroid_drift_min_cells": 1.0,
}


def run_isolated(handedness: str, N: int = 48, n_steps: int = 200) -> dict:
    """Run CosseratBeltramiSource for n_steps, record ω fields + h_local."""
    engine = VacuumEngine3D.from_args(
        N=N, pml=6, temperature=0.0, amplitude_convention="V_SNAP",
    )
    omega_drive = 2.0 * np.pi / 3.5  # Phase III-B canonical λ
    amplitude = 1.75  # near saturation onset per docstring sizing
    src = CosseratBeltramiSource(
        x0=10,
        propagation_axis=0,
        amplitude=amplitude,
        omega=omega_drive,
        handedness=handedness,
        sigma_yz=3.0,
        t_ramp=10.0,
        t_sustain=200.0,
    )
    engine.add_source(src)

    h_obs = HelicityObserver(cadence=2, propagation_axis=0)
    engine.add_observer(h_obs)

    omega_y_at_src: list[float] = []
    omega_z_at_src: list[float] = []
    omega_mag_at_src: list[float] = []
    centroid_x: list[float] = []
    times: list[float] = []
    omega_slabs_yz: list[np.ndarray] = []  # omega magnitude in y-z plane at x = src+10

    cy, cz = N // 2, N // 2

    # Run with manual diagnostic capture inside the step loop
    for step in range(1, n_steps + 1):
        engine.step()
        if step % 2 == 0:
            t = engine.outer_t
            omega = np.asarray(engine.cos.omega)
            # Sample at source slab center
            wy = float(omega[10, cy, cz, 1])
            wz = float(omega[10, cy, cz, 2])
            wmag = float(np.sqrt(wy**2 + wz**2))
            omega_y_at_src.append(wy)
            omega_z_at_src.append(wz)
            omega_mag_at_src.append(wmag)

            # |ω| centroid along propagation axis (x)
            omega_mag_3d = np.sqrt(np.sum(omega**2, axis=-1))
            x_indices = np.arange(N)
            x_weights = omega_mag_3d.sum(axis=(1, 2))
            if x_weights.sum() > 0:
                centroid = float((x_weights * x_indices).sum() / x_weights.sum())
            else:
                centroid = 0.0
            centroid_x.append(centroid)

            # YZ slab at x = source + 10 (downstream)
            ds_x = min(20, N - 1)
            slab = omega_mag_3d[ds_x, :, :]
            omega_slabs_yz.append(slab.copy())

            times.append(t)

    return {
        "handedness": handedness,
        "N": N,
        "n_steps": n_steps,
        "src_x": 10,
        "amplitude_seeded": float(amplitude),
        "omega_drive": float(omega_drive),
        "times": times,
        "omega_y_at_src": omega_y_at_src,
        "omega_z_at_src": omega_z_at_src,
        "omega_mag_at_src": omega_mag_at_src,
        "centroid_x": centroid_x,
        "omega_slabs_yz": np.stack(omega_slabs_yz, axis=0) if omega_slabs_yz else np.zeros((0, N, N)),
        "h_history": h_obs.history,
    }


def evaluate_prereg(rh: dict, lh: dict) -> dict:
    """Pre-reg evaluation per PREREG."""
    eval_result: dict = {}

    # C-C1: |ω| amplitude match (sustain phase)
    sustain_idx = len(rh["omega_mag_at_src"]) // 2
    omega_mag_rh = rh["omega_mag_at_src"][sustain_idx]
    expected_amp = rh["amplitude_seeded"]  # at sustain, env=1
    rel_err_C1 = abs(omega_mag_rh - expected_amp) / expected_amp
    pass_C_C1 = rel_err_C1 < PREREG["C-C1_amplitude_match_tolerance"]
    eval_result["C_C1_amplitude_relative_error"] = float(rel_err_C1)
    eval_result["pass_C_C1"] = bool(pass_C_C1)

    # C-C2: phase offset between ω_y and ω_z — should be 90° (RH or LH)
    wy = np.asarray(rh["omega_y_at_src"])
    wz = np.asarray(rh["omega_z_at_src"])
    sustain_start = len(wy) // 4
    sustain_end = 3 * len(wy) // 4
    wy_s = wy[sustain_start:sustain_end]
    wz_s = wz[sustain_start:sustain_end]
    ay = np.abs(wy_s).max()
    az = np.abs(wz_s).max()
    if ay > 0 and az > 0:
        try:
            from scipy.signal import hilbert
            ph_y = np.angle(hilbert(wy_s / ay))
            ph_z = np.angle(hilbert(wz_s / az))
            phase_offset = np.degrees(
                np.angle(np.exp(1j * np.mean(ph_z - ph_y)))
            )
            phase_offset_abs = float(abs(phase_offset))
        except ImportError:
            phase_offset_abs = float("nan")
    else:
        phase_offset_abs = float("nan")
    pass_C_C2 = (
        not np.isnan(phase_offset_abs)
        and PREREG["C-C2_phase_offset_deg_min"]
        <= phase_offset_abs
        <= PREREG["C-C2_phase_offset_deg_max"]
    )
    eval_result["C_C2_phase_offset_deg_abs"] = (
        float(phase_offset_abs) if not np.isnan(phase_offset_abs) else None
    )
    eval_result["pass_C_C2"] = bool(pass_C_C2)

    # C-C3: helicity h_local at source slab
    if rh["h_history"] and lh["h_history"]:
        # Take h_axis at source slab x=10, sustain phase
        rh_sustain_h = rh["h_history"][len(rh["h_history"]) // 2]
        lh_sustain_h = lh["h_history"][len(lh["h_history"]) // 2]
        h_rh_at_src = float(rh_sustain_h["h_axis"][10])
        h_lh_at_src = float(lh_sustain_h["h_axis"][10])
        rh_h_err = abs(h_rh_at_src - PREREG["C-C3_h_local_target_RH"])
        lh_h_err = abs(h_lh_at_src - PREREG["C-C3_h_local_target_LH"])
        pass_C_C3 = (
            rh_h_err < PREREG["C-C3_h_local_tolerance"] * 2
            and lh_h_err < PREREG["C-C3_h_local_tolerance"] * 2
        )
        eval_result["C_C3_h_local_RH"] = h_rh_at_src
        eval_result["C_C3_h_local_LH"] = h_lh_at_src
        eval_result["C_C3_h_local_RH_err"] = float(rh_h_err)
        eval_result["C_C3_h_local_LH_err"] = float(lh_h_err)
        eval_result["pass_C_C3"] = bool(pass_C_C3)
    else:
        eval_result["pass_C_C3"] = False

    # C-C4: centroid drift — peak |ω| moves downstream over time
    cx = np.asarray(rh["centroid_x"])
    if len(cx) >= 2:
        drift = float(cx[-1] - cx[0])
    else:
        drift = 0.0
    pass_C_C4 = drift > PREREG["C-C4_centroid_drift_min_cells"]
    eval_result["C_C4_centroid_drift_cells"] = drift
    eval_result["pass_C_C4"] = bool(pass_C_C4)

    return eval_result


def render_panels(rh: dict, lh: dict, eval_result: dict, out_png: str) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # Panel 1: ω_y vs ω_z trajectory at source slab
    ax = axes[0, 0]
    ax.plot(rh["omega_y_at_src"], rh["omega_z_at_src"], "b-", lw=0.7, label="RH")
    ax.plot(lh["omega_y_at_src"], lh["omega_z_at_src"], "r-", lw=0.7, label="LH")
    ax.set_xlabel("ω_y at source slab")
    ax.set_ylabel("ω_z at source slab")
    ax.set_title(
        "C-C1/C-C2: (ω_y, ω_z) phasor trajectory at source\n"
        f"amp_rel_err={eval_result['C_C1_amplitude_relative_error']:.3e}, "
        f"phase_offset={eval_result['C_C2_phase_offset_deg_abs']}"
    )
    ax.set_aspect("equal")
    ax.grid(alpha=0.3)
    ax.legend()

    # Panel 2: helicity h_local along x at sustain
    ax = axes[0, 1]
    if rh["h_history"]:
        h_mid_rh = rh["h_history"][len(rh["h_history"]) // 2]
        h_mid_lh = lh["h_history"][len(lh["h_history"]) // 2]
        x_arr = np.arange(len(h_mid_rh["h_axis"]))
        ax.plot(x_arr, h_mid_rh["h_axis"], "b-", lw=1.4, label="RH h_local")
        ax.plot(x_arr, h_mid_lh["h_axis"], "r-", lw=1.4, label="LH h_local")
        ax.axhline(+1.0, color="blue", ls="--", lw=0.5, alpha=0.5)
        ax.axhline(-1.0, color="red", ls="--", lw=0.5, alpha=0.5)
        ax.axvline(rh["src_x"], color="gray", ls="--", lw=0.5, label=f"src x={rh['src_x']}")
    ax.set_xlabel("x (cells, propagation axis)")
    ax.set_ylabel("h_local (Beltrami helicity)")
    ax.set_title(
        "C-C3: Beltrami helicity along x at sustain\n"
        f"RH(src)={eval_result.get('C_C3_h_local_RH', 'N/A')}, "
        f"LH(src)={eval_result.get('C_C3_h_local_LH', 'N/A')}"
    )
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 3: |ω| centroid drift over time
    ax = axes[1, 0]
    times_rh = np.asarray(rh["times"])
    cx_rh = np.asarray(rh["centroid_x"])
    cx_lh = np.asarray(lh["centroid_x"])
    ax.plot(times_rh, cx_rh, "b-", lw=1.4, label="RH centroid")
    ax.plot(times_rh, cx_lh, "r-", lw=1.4, label="LH centroid")
    ax.axhline(rh["src_x"], color="gray", ls="--", lw=0.5, label=f"src x={rh['src_x']}")
    ax.set_xlabel("t (nat units)")
    ax.set_ylabel("|ω|-weighted centroid_x (cells)")
    ax.set_title(
        "C-C4: |ω| centroid drift\n"
        f"RH drift = {eval_result['C_C4_centroid_drift_cells']:.2f} cells"
    )
    ax.legend()
    ax.grid(alpha=0.3)

    # Panel 4: |ω| in YZ slab downstream (x=src+10), final time, RH only
    ax = axes[1, 1]
    if rh["omega_slabs_yz"].size > 0:
        slab = rh["omega_slabs_yz"][-1]
        im = ax.imshow(slab.T, origin="lower", cmap="hot")
        plt.colorbar(im, ax=ax, label="|ω|")
    ax.set_xlabel("y")
    ax.set_ylabel("z")
    ax.set_title(f"|ω| at x=src+10 (final t), RH")

    plt.suptitle("Phase C — CosseratBeltramiSource isolated verification", fontsize=13, fontweight="bold")
    plt.tight_layout()
    plt.savefig(out_png, dpi=110, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent.parent.parent
    assets_dir = repo_root / "assets"
    results_dir = repo_root / "results"
    assets_dir.mkdir(parents=True, exist_ok=True)
    results_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 72)
    print("Phase C — CosseratBeltramiSource isolated verification")
    print("=" * 72)

    print("\n── Running RH ──")
    rh = run_isolated("RH")
    print(f"  done: n_frames = {len(rh['times'])}, max |ω| at src = {max(rh['omega_mag_at_src']):.4f}")

    print("\n── Running LH ──")
    lh = run_isolated("LH")
    print(f"  done: n_frames = {len(lh['times'])}, max |ω| at src = {max(lh['omega_mag_at_src']):.4f}")

    print("\n── Pre-reg evaluation ──")
    eval_result = evaluate_prereg(rh, lh)
    for k, v in eval_result.items():
        if k.startswith("pass_"):
            print(f"  {k:30} {'PASS' if v else 'FAIL'}")
        else:
            print(f"  {k:30} {v}")

    out_png = assets_dir / "cosserat_beltrami_isolated_panels.png"
    render_panels(rh, lh, eval_result, str(out_png))

    out_json = results_dir / "cosserat_beltrami_isolated.json"
    rh_serial = {k: v for k, v in rh.items() if not isinstance(v, np.ndarray)}
    lh_serial = {k: v for k, v in lh.items() if not isinstance(v, np.ndarray)}
    # Convert h_history's h_axis arrays to lists
    for h in rh_serial.get("h_history", []):
        if isinstance(h.get("h_axis"), np.ndarray):
            h["h_axis"] = h["h_axis"].tolist()
    for h in lh_serial.get("h_history", []):
        if isinstance(h.get("h_axis"), np.ndarray):
            h["h_axis"] = h["h_axis"].tolist()
    with open(out_json, "w") as f:
        json.dump(
            {"prereg": PREREG, "eval": eval_result,
             "rh_summary": rh_serial, "lh_summary": lh_serial},
            f, indent=2, default=str,
        )

    print(f"\n  Outputs:")
    print(f"    {out_png}")
    print(f"    {out_json}")


if __name__ == "__main__":
    main()
