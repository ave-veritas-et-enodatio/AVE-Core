#!/usr/bin/env python3
r"""Electron genesis observer bridge — alpha-free instrumentation first pass.

SCOPE NOTE (2026-06-07 observer bridge):
This driver does not claim to generate an electron. It tests whether the current
AVE engines expose the observables required for a future electron-genesis
emergence test:

  * MasterEquationFDTD: nonlinear scalar bound-state / breathing diagnostics.
  * K4Lattice3D: bond phasor, Phi_link, local impedance/saturation, and
    first/second-neighbor envelope diagnostics.

Alpha is imported for COMPARISON ONLY in final classification. It is never used
as a damping coefficient, threshold, seed amplitude, Q target, or kernel.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np

import ave.core.constants as _avc
from ave.core.constants import ALPHA_COLD, ALPHA_COLD_INV
from ave.core.k4_tlm import K4Lattice3D
from ave.core.master_equation_fdtd import MasterEquationFDTD
from ave.core.master_fdtd_phasor_bridge import MasterFDTDPhasorBridge


PROJECT_ROOT = next(p for p in Path(__file__).resolve().parents if (p / ".git").exists())
OUT_DIR = PROJECT_ROOT / "src" / "scripts" / "vol_1_foundations" / "_output"
OUT_DIR.mkdir(parents=True, exist_ok=True)


PORT_VECTORS = np.array(
    [
        [1, 1, 1],
        [1, -1, -1],
        [-1, 1, -1],
        [-1, -1, 1],
    ],
    dtype=int,
)


def verify_canonical_sources() -> None:
    constants_path = Path(_avc.__file__).as_posix()
    if not constants_path.endswith("src/ave/core/constants.py"):
        raise RuntimeError(f"ave.core.constants loaded from unexpected path: {constants_path}")
    if not (100.0 < float(ALPHA_COLD_INV) < 200.0 and 0.0 < float(ALPHA_COLD) < 0.01):
        raise RuntimeError("canonical alpha comparison constants outside expected range")


def fwhm_3d(field: np.ndarray) -> float:
    mag = np.abs(field)
    peak = float(np.max(mag))
    if peak <= 1e-12:
        return 0.0
    above = mag > peak / 2.0
    n_cells = int(np.sum(above))
    if n_cells == 0:
        return 0.0
    radius = (3.0 * n_cells / (4.0 * math.pi)) ** (1.0 / 3.0)
    return float(2.0 * radius)


def pearson(a: np.ndarray, b: np.ndarray) -> float | None:
    if len(a) < 3 or len(b) < 3:
        return None
    a0 = a - np.mean(a)
    b0 = b - np.mean(b)
    denom = float(np.linalg.norm(a0) * np.linalg.norm(b0))
    if denom <= 1e-15:
        return None
    return float(np.dot(a0, b0) / denom)


def positive_covariance_metrics(samples: np.ndarray) -> dict[str, Any]:
    samples = np.asarray(samples, dtype=float)
    if samples.ndim == 1:
        samples = samples[:, None]
    centered = samples - samples.mean(axis=0, keepdims=True)
    cov = np.cov(centered, rowvar=False)
    cov = np.atleast_2d(cov)
    eig = np.maximum(np.linalg.eigvalsh(cov), 0.0)
    pos = eig[eig > 1e-12]
    total = float(np.sum(pos))
    rank = int(len(pos))
    screened = float(pos[0] / total) if rank >= 2 and total > 0 else 0.0
    return {
        "rank_positive": rank,
        "positive_eigenvalues": [float(x) for x in pos],
        "screened_variance_fraction": screened,
        "screened_rms_fraction": float(math.sqrt(screened)),
    }


def run_master_bound_state() -> dict[str, Any]:
    engine = MasterEquationFDTD(
        N=32,
        dx=1.0,
        V_yield=1.0,
        c0=1.0,
        pml_thickness=4,
        A_cap=0.99,
        S_min=0.05,
    )
    center = (16, 16, 16)
    engine.inject_localized_blob(center=center, radius=2.5, amplitude=0.85, profile="sech")

    peaks: list[float] = []
    fwhm: list[float] = []
    energy: list[float] = []
    center_trace: list[float] = []
    n_steps = 1200
    cadence = 5
    for step in range(n_steps + 1):
        if step % cadence == 0:
            peaks.append(float(np.max(np.abs(engine.V))))
            fwhm.append(fwhm_3d(engine.V))
            energy.append(float(engine.total_energy()))
            center_trace.append(float(engine.V[center]))
        if step < n_steps:
            engine.step()

    transient = max(1, len(peaks) // 5)
    post_peaks = np.array(peaks[transient:])
    post_fwhm = np.array(fwhm[transient:])
    peak_mean = float(np.mean(post_peaks))
    peak_min = float(np.min(post_peaks))
    peak_max = float(np.max(post_peaks))
    fwhm_cv = float(np.std(post_fwhm) / np.mean(post_fwhm)) if np.mean(post_fwhm) > 0 else math.inf

    # Conservative first-pass L1: the bound-state signal remains localized and
    # finite after transient; this is not a Q measurement.
    l1_pass = bool(peak_mean > 0.05 and peak_min > 0.01 and fwhm_cv < 0.75)

    return {
        "engine": "MasterEquationFDTD",
        "alpha_used_as_input": False,
        "n_steps": n_steps,
        "cadence": cadence,
        "dt": float(engine.dt),
        "seed": {"profile": "sech", "amplitude": 0.85, "radius": 2.5},
        "observables_available": {
            "bound_state_scalar_V": True,
            "V_inc_V_ref": False,
            "Phi_link": False,
            "z_local": False,
        },
        "peak_mean_post_transient": peak_mean,
        "peak_min_post_transient": peak_min,
        "peak_max_post_transient": peak_max,
        "fwhm_cv_post_transient": fwhm_cv,
        "energy_initial": float(energy[0]),
        "energy_final": float(energy[-1]),
        "l1_trapping_pass": l1_pass,
        "trace_tail": {
            "peaks": [float(x) for x in peaks[-12:]],
            "fwhm": [float(x) for x in fwhm[-12:]],
            "center": [float(x) for x in center_trace[-12:]],
        },
    }


def neighbour_positions(center: tuple[int, int, int]) -> dict[str, list[tuple[int, int, int]]]:
    c = np.array(center, dtype=int)
    first = [tuple((c + v).tolist()) for v in PORT_VECTORS]
    second_set: set[tuple[int, int, int]] = set()
    for j in range(4):
        for k in range(4):
            if j == k:
                continue
            second_set.add(tuple((c + PORT_VECTORS[j] - PORT_VECTORS[k]).tolist()))
    return {"first_shell": first, "second_shell": sorted(second_set)}


def active_energy_at(lattice: K4Lattice3D, positions: list[tuple[int, int, int]]) -> list[float]:
    density = lattice.get_energy_density()
    values = []
    for pos in positions:
        x, y, z = pos
        if 0 <= x < lattice.nx and 0 <= y < lattice.ny and 0 <= z < lattice.nz:
            values.append(float(density[x, y, z]))
        else:
            values.append(0.0)
    return values


def drive_k4_precursor(lattice: K4Lattice3D, center: tuple[int, int, int], step: int, drive_steps: int) -> None:
    if step >= drive_steps:
        return
    # Alpha-free two-quadrature precursor across the four ports. The 2:3 cadence
    # is topology-shaped but not a finished electron seed.
    t = 2.0 * math.pi * step / drive_steps
    amp = 0.32 * math.sin(math.pi * (step + 1) / (drive_steps + 1))
    pattern = np.array(
        [
            math.cos(2.0 * t),
            math.sin(3.0 * t),
            -math.cos(2.0 * t),
            -math.sin(3.0 * t),
        ],
        dtype=float,
    )
    lattice.V_inc[center] += amp * pattern / 2.0


def run_master_unified_projection() -> dict[str, Any]:
    """Bound-state dynamics with projected K4 phasor/reactance observers on same V."""
    engine = MasterEquationFDTD(
        N=32,
        dx=1.0,
        V_yield=1.0,
        c0=1.0,
        pml_thickness=4,
        A_cap=0.99,
        S_min=0.05,
    )
    bridge = MasterFDTDPhasorBridge(
        nx=engine.N,
        ny=engine.N,
        nz=engine.N,
        dx=engine.dx,
        V_yield=engine.V_yield,
        dt=engine.dt,
    )
    center = (16, 16, 16)
    shells = neighbour_positions(center)
    bridge.reset_phi_link()
    engine.inject_localized_blob(center=center, radius=2.5, amplitude=0.85, profile="sech")

    peaks: list[float] = []
    fwhm: list[float] = []
    energy: list[float] = []
    v_inc_port0: list[float] = []
    v_ref_port0: list[float] = []
    phi_port0: list[float] = []
    phi_slope_port0: list[float] = []
    phi_abs_max_local: list[float] = []
    z_center: list[float] = []
    gamma_center: list[float | None] = []
    first_shell_energy: list[list[float]] = []
    second_shell_energy: list[list[float]] = []
    n_steps = 1200
    cadence = 5
    prev_phi = 0.0

    for step in range(n_steps + 1):
        if step > 0:
            bridge.project_from_scalar(engine.V, engine.V_prev, accumulate_phi=True, S_min=engine.S_min)
        if step % cadence == 0:
            peaks.append(float(np.max(np.abs(engine.V))))
            fwhm.append(fwhm_3d(engine.V))
            energy.append(float(engine.total_energy()))
            phi = float(bridge.Phi_link[center][0])
            v_inc_port0.append(float(bridge.V_inc[center][0]))
            v_ref_port0.append(float(bridge.V_ref[center][0]))
            phi_port0.append(phi)
            phi_slope_port0.append(float((phi - prev_phi) / max(engine.dt * cadence, 1e-12)))
            prev_phi = phi
            cx, cy, cz = center
            local_phi = bridge.Phi_link[cx - 2 : cx + 3, cy - 2 : cy + 3, cz - 2 : cz + 3, :]
            phi_abs_max_local.append(float(np.max(np.abs(local_phi))))
            z_center.append(float(bridge.z_local_field[center]))
            gamma_center.append(bridge.bond_gamma_at(center, port=0))
            first_shell_energy.append(
                [float(np.abs(engine.V[pos])) for pos in shells["first_shell"]]
            )
            second_shell_energy.append(
                [float(np.abs(engine.V[pos])) for pos in shells["second_shell"]]
            )
        if step < n_steps:
            engine.step()

    transient = max(1, len(peaks) // 5)
    post_peaks = np.array(peaks[transient:])
    post_fwhm = np.array(fwhm[transient:])
    peak_mean = float(np.mean(post_peaks))
    peak_min = float(np.min(post_peaks))
    peak_max = float(np.max(post_peaks))
    fwhm_cv = float(np.std(post_fwhm) / np.mean(post_fwhm)) if np.mean(post_fwhm) > 0 else math.inf
    l1_pass = bool(peak_mean > 0.05 and peak_min > 0.01 and fwhm_cv < 0.75)

    v_arr = np.array(v_inc_port0)
    phi_arr = np.array(phi_port0)
    phi_slope_arr = np.array(phi_slope_port0)
    phi_abs_arr = np.array(phi_abs_max_local)
    post = slice(len(v_arr) // 5, None)
    cl_corr = pearson(v_arr[post] ** 2, phi_arr[post] ** 2)
    v_phi_slope_corr = pearson(v_arr[post], phi_slope_arr[post])
    first_metrics = positive_covariance_metrics(np.array(first_shell_energy))
    second_metrics = positive_covariance_metrics(np.array(second_shell_energy))

    l2_pass = bool(np.std(v_arr[post]) > 1e-6 and np.std(np.array(v_ref_port0)[post]) > 1e-6)
    l3_pass = bool(np.max(phi_abs_arr[post]) > 1e-12 or np.std(phi_slope_arr[post]) > 1e-8)
    l4_pass = bool(first_metrics["rank_positive"] >= 2 or second_metrics["rank_positive"] >= 2)

    gamma_post = [g for g in gamma_center[transient:] if g is not None]
    gamma_min = float(np.min(gamma_post)) if gamma_post else None

    return {
        "engine": "MasterEquationFDTD+PhasorBridge",
        "alpha_used_as_input": False,
        "n_steps": n_steps,
        "cadence": cadence,
        "dt": float(engine.dt),
        "seed": {"profile": "sech", "amplitude": 0.85, "radius": 2.5},
        "observables_available": {
            "bound_state_scalar_V": True,
            "V_inc_V_ref": True,
            "Phi_link": True,
            "z_local": True,
        },
        "peak_mean_post_transient": peak_mean,
        "peak_min_post_transient": peak_min,
        "peak_max_post_transient": peak_max,
        "fwhm_cv_post_transient": fwhm_cv,
        "energy_initial": float(energy[0]),
        "energy_final": float(energy[-1]),
        "v_inc_std_post_transient": float(np.std(v_arr[post])),
        "v_ref_std_post_transient": float(np.std(np.array(v_ref_port0)[post])),
        "phi_std_post_transient": float(np.std(phi_arr[post])),
        "phi_abs_max_local_post_transient": float(np.max(phi_abs_arr[post])),
        "phi_slope_std_post_transient": float(np.std(phi_slope_arr[post])),
        "c_l_energy_correlation": cl_corr,
        "v_phi_slope_correlation": v_phi_slope_corr,
        "z_center_mean_post_transient": float(np.mean(np.array(z_center)[post])),
        "bond_gamma_min_post_transient": gamma_min,
        "first_shell_envelope": first_metrics,
        "second_shell_envelope": second_metrics,
        "l1_trapping_pass": l1_pass,
        "l2_phasor_observer_pass": l2_pass,
        "l3_phi_link_observer_pass": l3_pass,
        "l4_neighbor_envelope_pass": l4_pass,
        "trace_tail": {
            "peaks": [float(x) for x in peaks[-12:]],
            "fwhm": [float(x) for x in fwhm[-12:]],
            "v_inc_port0": [float(x) for x in v_inc_port0[-12:]],
            "v_ref_port0": [float(x) for x in v_ref_port0[-12:]],
            "phi_port0": [float(x) for x in phi_port0[-12:]],
            "phi_abs_max_local": [float(x) for x in phi_abs_max_local[-12:]],
        },
    }


def run_k4_reactance_observer() -> dict[str, Any]:
    lattice = K4Lattice3D(
        24,
        24,
        24,
        dx=1.0,
        nonlinear=True,
        pml_thickness=3,
        op3_bond_reflection=True,
        use_memristive_saturation=True,
        V_SNAP=1.0,
    )
    center = (12, 12, 12)
    shells = neighbour_positions(center)
    lattice.reset_phi_link()

    n_steps = 320
    drive_steps = 64
    cadence = 2
    v_inc_port0: list[float] = []
    v_ref_port0: list[float] = []
    phi_port0: list[float] = []
    phi_slope_port0: list[float] = []
    phi_abs_max_local: list[float] = []
    z_center: list[float] = []
    energy: list[float] = []
    first_shell_energy: list[list[float]] = []
    second_shell_energy: list[list[float]] = []
    prev_phi = float(lattice.Phi_link[center][0])

    for step in range(n_steps + 1):
        if step < n_steps:
            drive_k4_precursor(lattice, center, step, drive_steps)
            lattice.step()
        if step % cadence == 0:
            phi = float(lattice.Phi_link[center][0])
            v_inc_port0.append(float(lattice.V_inc[center][0]))
            v_ref_port0.append(float(lattice.V_ref[center][0]))
            phi_port0.append(phi)
            phi_slope_port0.append(float((phi - prev_phi) / max(lattice.dt * cadence, 1e-12)))
            prev_phi = phi
            cx, cy, cz = center
            local_phi = lattice.Phi_link[cx - 2 : cx + 3, cy - 2 : cy + 3, cz - 2 : cz + 3, :]
            phi_abs_max_local.append(float(np.max(np.abs(local_phi))))
            z_center.append(float(lattice.z_local_field[center]))
            energy.append(float(lattice.total_energy()))
            first_shell_energy.append(active_energy_at(lattice, shells["first_shell"]))
            second_shell_energy.append(active_energy_at(lattice, shells["second_shell"]))

    v_arr = np.array(v_inc_port0)
    phi_arr = np.array(phi_port0)
    phi_slope_arr = np.array(phi_slope_port0)
    phi_abs_arr = np.array(phi_abs_max_local)
    post = slice(len(v_arr) // 5, None)
    c_energy = v_arr[post] ** 2
    l_energy = phi_arr[post] ** 2
    cl_corr = pearson(c_energy, l_energy)
    v_phi_slope_corr = pearson(v_arr[post], phi_slope_arr[post])

    first_metrics = positive_covariance_metrics(np.array(first_shell_energy))
    second_metrics = positive_covariance_metrics(np.array(second_shell_energy))
    total_energy_initial = float(energy[0]) if energy else 0.0
    total_energy_peak = float(np.max(energy)) if energy else 0.0
    total_energy_final = float(energy[-1]) if energy else 0.0
    retained_fraction = total_energy_final / total_energy_peak if total_energy_peak > 0 else 0.0

    # Instrumentation pass/fail, not physics pass/fail.
    l2_pass = bool(np.std(v_arr[post]) > 1e-6 and np.std(np.array(v_ref_port0)[post]) > 1e-6)
    l3_pass = bool(np.max(phi_abs_arr[post]) > 1e-12 or np.std(phi_slope_arr[post]) > 1e-8)
    l4_pass = bool(first_metrics["rank_positive"] >= 2 or second_metrics["rank_positive"] >= 2)
    l1_bound_like = bool(retained_fraction > 0.2)

    return {
        "engine": "K4Lattice3D",
        "alpha_used_as_input": False,
        "n_steps": n_steps,
        "drive_steps": drive_steps,
        "dt": float(lattice.dt),
        "seed": "alpha-free 2:3 four-port quadrature precursor, drive then free-run",
        "observables_available": {
            "bound_state_scalar_V": False,
            "V_inc_V_ref": True,
            "Phi_link": True,
            "z_local": True,
        },
        "energy_initial": total_energy_initial,
        "energy_peak": total_energy_peak,
        "energy_final": total_energy_final,
        "energy_retained_fraction_of_peak": float(retained_fraction),
        "v_inc_std_post_transient": float(np.std(v_arr[post])),
        "v_ref_std_post_transient": float(np.std(np.array(v_ref_port0)[post])),
        "phi_std_post_transient": float(np.std(phi_arr[post])),
        "phi_abs_max_local_post_transient": float(np.max(phi_abs_arr[post])),
        "phi_slope_std_post_transient": float(np.std(phi_slope_arr[post])),
        "c_l_energy_correlation": cl_corr,
        "v_phi_slope_correlation": v_phi_slope_corr,
        "z_center_mean_post_transient": float(np.mean(np.array(z_center)[post])),
        "first_shell_envelope": first_metrics,
        "second_shell_envelope": second_metrics,
        "l1_bound_like_pass": l1_bound_like,
        "l2_phasor_observer_pass": l2_pass,
        "l3_phi_link_observer_pass": l3_pass,
        "l4_neighbor_envelope_pass": l4_pass,
        "trace_tail": {
            "v_inc_port0": [float(x) for x in v_inc_port0[-12:]],
            "v_ref_port0": [float(x) for x in v_ref_port0[-12:]],
            "phi_port0": [float(x) for x in phi_port0[-12:]],
            "phi_abs_max_local": [float(x) for x in phi_abs_max_local[-12:]],
            "energy": [float(x) for x in energy[-12:]],
        },
    }


def classify(
    master: dict[str, Any],
    k4: dict[str, Any],
    unified: dict[str, Any] | None = None,
) -> dict[str, Any]:
    split_l1 = bool(master["l1_trapping_pass"])
    split_l2 = bool(k4["l2_phasor_observer_pass"])
    split_l3 = bool(k4["l3_phi_link_observer_pass"])
    split_l4 = bool(k4["l4_neighbor_envelope_pass"])
    split_unified = False

    if unified is not None:
        u_l1 = bool(unified["l1_trapping_pass"])
        u_l2 = bool(unified["l2_phasor_observer_pass"])
        u_l3 = bool(unified["l3_phi_link_observer_pass"])
        u_l4 = bool(unified["l4_neighbor_envelope_pass"])
        u_all = u_l1 and u_l2 and u_l3 and u_l4
        if u_all:
            verdict = "PROJECTION_BRIDGE_INSTRUMENTED"
        else:
            verdict = "PROJECTION_BRIDGE_PARTIAL"
        return {
            "verdict": verdict,
            "alpha_inserted": False,
            "comparison_only": {
                "alpha_cold": float(ALPHA_COLD),
                "alpha_cold_inv": float(ALPHA_COLD_INV),
                "four_pi": float(4.0 * math.pi),
            },
            "layer_passes": {
                "L1_master_trapping": u_l1,
                "L2_phasor": u_l2,
                "L3_phi_link": u_l3,
                "L4_neighbor_envelope": u_l4,
                "unified_engine_has_all_layers": u_all,
            },
            "split_lane_reference": {
                "L1_master_trapping": split_l1,
                "L2_k4_phasor": split_l2,
                "L3_k4_phi_link": split_l3,
                "L4_k4_neighbor_envelope": split_l4,
                "unified_engine_has_all_layers": split_unified,
            },
            "interpretation": (
                "MasterEquationFDTD bound-state dynamics now carry projected "
                "V_inc/V_ref/Phi_link/z_local observers via the scalar→bond "
                "projection bridge. This closes the observer-architecture gap "
                "for instrumentation; it does not yet claim alpha emergence or "
                "replace native K4-TLM bond dynamics."
            ),
        }

    if split_l1 and split_l2 and split_l3 and split_l4 and split_unified:
        verdict = "EMERGENCE_CANDIDATE"
    elif split_l1 and split_l2 and split_l3 and split_l4 and not split_unified:
        verdict = "OBSERVER_ARCHITECTURE_GAP"
    else:
        verdict = "FIRST_PASS_INCOMPLETE"

    return {
        "verdict": verdict,
        "alpha_inserted": False,
        "comparison_only": {
            "alpha_cold": float(ALPHA_COLD),
            "alpha_cold_inv": float(ALPHA_COLD_INV),
            "four_pi": float(4.0 * math.pi),
        },
        "layer_passes": {
            "L1_master_trapping": split_l1,
            "L2_k4_phasor": split_l2,
            "L3_k4_phi_link": split_l3,
            "L4_k4_neighbor_envelope": split_l4,
            "unified_engine_has_all_layers": split_unified,
        },
        "interpretation": (
            "Current engines split the required observables: MasterEquationFDTD "
            "supports scalar bound-state trapping, while K4Lattice3D exposes "
            "bond phasor/Phi_link/envelope diagnostics. A full alpha-free electron "
            "genesis test needs a unified engine or validated bridge before any "
            "Q≈137 claim is meaningful."
        ),
    }


def main() -> None:
    verify_canonical_sources()
    master = run_master_bound_state()
    k4 = run_k4_reactance_observer()
    unified = run_master_unified_projection()
    result = {
        "scope": "electron genesis observer bridge; no alpha in computation",
        "master_bound_state_lane": master,
        "k4_reactance_observer_lane": k4,
        "master_unified_projection_lane": unified,
        "classification": classify(master, k4, unified),
    }
    out_path = OUT_DIR / "electron_genesis_observer_bridge_results.json"
    out_path.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")

    cls = result["classification"]
    print("Electron genesis observer bridge")
    print(f"  verdict: {cls['verdict']}")
    print(f"  unified L1 trapping: {unified['l1_trapping_pass']}")
    print(f"  unified L2 phasor: {unified['l2_phasor_observer_pass']}")
    print(f"  unified L3 Phi_link: {unified['l3_phi_link_observer_pass']}")
    print(f"  unified L4 envelope: {unified['l4_neighbor_envelope_pass']}")
    print(f"  unified bond gamma min: {unified['bond_gamma_min_post_transient']}")
    print(f"  split L1 master trapping: {master['l1_trapping_pass']}")
    print(f"  split L2 K4 phasor observer: {k4['l2_phasor_observer_pass']}")
    print(f"  K4 retained energy fraction of peak: {k4['energy_retained_fraction_of_peak']:.4f}")
    print("  alpha: comparison-only; not inserted")
    print(f"  wrote: {out_path}")


if __name__ == "__main__":
    main()
