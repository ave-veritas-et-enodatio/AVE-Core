#!/usr/bin/env python3
r"""Unified amplitude–Γ–retention sweep on MasterEquationFDTD + PhasorBridge.

SCOPE NOTE (2026-06-07 calibration-crux sweep):
Forward alpha-free parameter sweep over sech seed amplitude. Measures bond Γ,
strain, and energy retention on the unified projection lane. Does NOT claim
alpha emergence, electron genesis, or Q≈137. Alpha constants are comparison-only.

Prereg: research/2026-06-07_unified-amplitude-gamma-sweep-prereg.md
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np

import ave.core.constants as _avc
from ave.core.constants import ALPHA_COLD, ALPHA_COLD_INV
from ave.core.master_equation_fdtd import MasterEquationFDTD
from ave.core.master_fdtd_phasor_bridge import MasterFDTDPhasorBridge


PROJECT_ROOT = next(p for p in Path(__file__).resolve().parents if (p / ".git").exists())
OUT_DIR = PROJECT_ROOT / "src" / "scripts" / "vol_1_foundations" / "_output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SWEEP_AMPLITUDES = [0.20, 0.35, 0.48, 0.65, 0.85, 1.00, 1.25, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00]
REST_STRAIN_REFERENCE = math.sqrt(0.23)
GROWTH_BOUND = 10.0
WALL_GAMMA_THRESHOLD = -0.5


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


def run_single_amplitude(amplitude: float) -> dict[str, Any]:
    center = (16, 16, 16)
    n_steps = 1200
    cadence = 5

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
    bridge.reset_phi_link()
    engine.inject_localized_blob(center=center, radius=2.5, amplitude=amplitude, profile="sech")

    peaks: list[float] = []
    a_peak_trace: list[float] = []
    fwhm_trace: list[float] = []
    energy: list[float] = []
    gamma_shell_trace: list[float | None] = []
    gamma_shell_uncapped_trace: list[float | None] = []
    gamma_center_trace: list[float | None] = []
    nan_detected = False

    for step in range(n_steps + 1):
        if step > 0:
            bridge.project_from_scalar(engine.V, engine.V_prev, accumulate_phi=True, S_min=engine.S_min)
        if step % cadence == 0:
            if not np.isfinite(engine.V).all():
                nan_detected = True
            peaks.append(float(np.max(np.abs(engine.V))))
            a_peak_trace.append(float(np.max(np.abs(engine.V)) / engine.V_yield))
            fwhm_trace.append(fwhm_3d(engine.V))
            energy.append(float(engine.total_energy()))
            gamma_shell_trace.append(
                bridge.bond_gamma_min_in_shell(
                    engine.V,
                    threshold_frac=0.1,
                    center=center,
                    radius=8,
                    A_cap=0.99,
                    S_min=engine.S_min,
                )
            )
            gamma_shell_uncapped_trace.append(
                bridge.bond_gamma_min_in_shell(
                    engine.V,
                    threshold_frac=0.1,
                    center=center,
                    radius=8,
                    A_cap=None,
                    S_min=engine.S_min,
                )
            )
            gamma_center_trace.append(bridge.bond_gamma_at(center, port=0))
        if step < n_steps:
            engine.step()

    transient = max(1, len(peaks) // 5)
    post_peaks = np.array(peaks[transient:])
    post_a = np.array(a_peak_trace[transient:])
    post_energy = np.array(energy[transient:])
    post_fwhm = np.array(fwhm_trace[transient:])

    peak_mean = float(np.mean(post_peaks))
    peak_min = float(np.min(post_peaks))
    a_peak_max = float(np.max(a_peak_trace))
    a_peak_post_max = float(np.max(post_a))
    fwhm_cv = float(np.std(post_fwhm) / np.mean(post_fwhm)) if np.mean(post_fwhm) > 0 else math.inf

    energy_initial = float(energy[0]) if energy else 0.0
    energy_peak = float(np.max(energy)) if energy else 0.0
    energy_final = float(energy[-1]) if energy else 0.0
    energy_growth_ratio = energy_peak / energy_initial if energy_initial > 0 else math.inf
    energy_retained_fraction = energy_final / energy_peak if energy_peak > 0 else 0.0

    gamma_shell_post = [g for g in gamma_shell_trace[transient:] if g is not None]
    gamma_shell_uncapped_post = [g for g in gamma_shell_uncapped_trace[transient:] if g is not None]
    gamma_center_post = [g for g in gamma_center_trace[transient:] if g is not None]
    gamma_min_shell = float(np.min(gamma_shell_post)) if gamma_shell_post else None
    gamma_min_shell_uncapped = float(np.min(gamma_shell_uncapped_post)) if gamma_shell_uncapped_post else None
    gamma_min_center = float(np.min(gamma_center_post)) if gamma_center_post else None

    l1_pass = bool(peak_mean > 0.05 and peak_min > 0.01 and fwhm_cv < 0.75)
    bounded_pass = bool(np.isfinite(energy_growth_ratio) and energy_growth_ratio <= GROWTH_BOUND and not nan_detected)
    wall_pass = bool(gamma_min_shell is not None and gamma_min_shell <= WALL_GAMMA_THRESHOLD)
    wall_pass_uncapped = bool(
        gamma_min_shell_uncapped is not None and gamma_min_shell_uncapped <= WALL_GAMMA_THRESHOLD
    )
    window_pass = bool(wall_pass and bounded_pass and l1_pass)
    window_pass_uncapped = bool(wall_pass_uncapped and bounded_pass and l1_pass)

    return {
        "seed_amplitude": float(amplitude),
        "rest_strain_reference_amplitude": float(REST_STRAIN_REFERENCE),
        "alpha_used_as_input": False,
        "nan_detected": nan_detected,
        "A_peak_max": a_peak_max,
        "A_peak_post_transient_max": a_peak_post_max,
        "A_squared_peak_max": float(a_peak_max**2),
        "gamma_min_shell_post_transient": gamma_min_shell,
        "gamma_min_shell_uncapped_post_transient": gamma_min_shell_uncapped,
        "gamma_min_center_post_transient": gamma_min_center,
        "energy_initial": energy_initial,
        "energy_peak": energy_peak,
        "energy_final": energy_final,
        "energy_growth_ratio": float(energy_growth_ratio),
        "energy_retained_fraction": float(energy_retained_fraction),
        "l1_trapping_pass": l1_pass,
        "bounded_pass": bounded_pass,
        "wall_pass": wall_pass,
        "wall_pass_uncapped": wall_pass_uncapped,
        "window_pass": window_pass,
        "window_pass_uncapped": window_pass_uncapped,
        "peak_mean_post_transient": peak_mean,
        "peak_min_post_transient": peak_min,
    }


def classify_sweep(rows: list[dict[str, Any]]) -> dict[str, Any]:
    wall_rows = [r for r in rows if r["wall_pass"]]
    wall_uncapped_rows = [r for r in rows if r["wall_pass_uncapped"]]
    bounded_rows = [r for r in rows if r["bounded_pass"]]
    window_rows = [r for r in rows if r["window_pass"]]
    window_uncapped_rows = [r for r in rows if r["window_pass_uncapped"]]
    trap_rows = [r for r in rows if r["l1_trapping_pass"]]

    if window_rows:
        outcome = "A_window_found"
        verdict = "CALIBRATION_CRUX_WINDOW"
    elif window_uncapped_rows:
        outcome = "A_window_found_uncapped_observer"
        verdict = "CALIBRATION_CRUX_WINDOW_UNCAPPED_OBSERVER"
    elif wall_rows and bounded_rows and not window_rows:
        outcome = "B_disjoint_bands"
        verdict = "CALIBRATION_CRUX_DISJOINT"
    elif wall_uncapped_rows and bounded_rows and not window_uncapped_rows:
        outcome = "B_disjoint_bands_uncapped_observer"
        verdict = "CALIBRATION_CRUX_DISJOINT_UNCAPPED_OBSERVER"
    elif not wall_rows and not wall_uncapped_rows:
        outcome = "C_no_wall"
        verdict = "NO_SHORT_WALL_IN_SWEEP"
    elif not trap_rows:
        outcome = "D_no_trap"
        verdict = "NO_LOCALIZED_TRAP"
    else:
        outcome = "B_disjoint_bands"
        verdict = "CALIBRATION_CRUX_DISJOINT"

    return {
        "outcome": outcome,
        "verdict": verdict,
        "alpha_inserted": False,
        "comparison_only": {
            "alpha_cold": float(ALPHA_COLD),
            "alpha_cold_inv": float(ALPHA_COLD_INV),
            "four_pi": float(4.0 * math.pi),
            "rest_A_squared_reference": 0.23,
        },
        "counts": {
            "wall_pass": len(wall_rows),
            "wall_pass_uncapped": len(wall_uncapped_rows),
            "bounded_pass": len(bounded_rows),
            "window_pass": len(window_rows),
            "window_pass_uncapped": len(window_uncapped_rows),
            "l1_trapping_pass": len(trap_rows),
        },
        "window_amplitudes": [r["seed_amplitude"] for r in window_rows],
        "window_uncapped_amplitudes": [r["seed_amplitude"] for r in window_uncapped_rows],
        "wall_amplitudes": [r["seed_amplitude"] for r in wall_rows],
        "wall_uncapped_amplitudes": [r["seed_amplitude"] for r in wall_uncapped_rows],
        "bounded_amplitudes": [r["seed_amplitude"] for r in bounded_rows],
        "interpretation": (
            "Alpha-free amplitude sweep on unified MasterEquationFDTD+PhasorBridge. "
            "Tests whether bond shorting and bounded trapping share an amplitude window."
        ),
    }


def main() -> None:
    verify_canonical_sources()
    rows = [run_single_amplitude(amp) for amp in SWEEP_AMPLITUDES]
    classification = classify_sweep(rows)
    result = {
        "scope": "unified amplitude-gamma-retention sweep; no alpha in computation",
        "sweep_amplitudes": SWEEP_AMPLITUDES,
        "thresholds": {
            "wall_gamma": WALL_GAMMA_THRESHOLD,
            "energy_growth_bound": GROWTH_BOUND,
        },
        "rows": rows,
        "classification": classification,
    }
    out_path = OUT_DIR / "unified_amplitude_gamma_sweep_results.json"
    out_path.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")

    print("Unified amplitude–Γ–retention sweep")
    print(f"  verdict: {classification['verdict']} ({classification['outcome']})")
    print(f"  window_pass count: {classification['counts']['window_pass']}")
    print(f"  wall_pass count: {classification['counts']['wall_pass']}")
    print(f"  bounded_pass count: {classification['counts']['bounded_pass']}")
    for row in rows:
        g = row["gamma_min_shell_post_transient"]
        gu = row["gamma_min_shell_uncapped_post_transient"]
        gtxt = f"{g:.4f}" if g is not None else "None"
        gutxt = f"{gu:.4f}" if gu is not None else "None"
        print(
            f"  amp={row['seed_amplitude']:4.2f}  A_max={row['A_peak_max']:.3f}"
            f"  gamma={gtxt}  gamma_u={gutxt}  growth={row['energy_growth_ratio']:.2f}"
            f"  window_u={row['window_pass_uncapped']}"
        )
    print("  alpha: comparison-only; not inserted")
    print(f"  wrote: {out_path}")


if __name__ == "__main__":
    main()
