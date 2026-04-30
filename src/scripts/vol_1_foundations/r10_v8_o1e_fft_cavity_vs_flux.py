"""
O.1e — FFT Cavity-vs-Flux Discriminator on Stable Shell Mode.

Per auditor 2026-04-30 Flag 3: spatial-scale (R=8 multi-cell) closes
"not corpus electron at ℓ_node scale." FFT closes "WHICH cavity mode
is this" — substrate ℓ=2 at 1.5·ω_C (A38), ℓ=5 at 2.96·ω_C, or other.
Per A39 v2 dual-criterion, run both for proper bound-state adjudication.

Same closed-evolution setup as O.1c (amp=0.1, R=8, r=4, 50P) plus
V_inc time series captures at 5 shell-mode cells. FFT each
post-transient (t > 11P).

== Pre-registered observables ==

  At each of 5 shell-mode cells, FFT V_inc[port=0] over post-transient
  window. Extract dominant frequency.

  EXPECTED outcomes:
    (a) ω_dom = 1.5·ω_C at all 5 cells → substrate ℓ=2 cavity mode (A38)
    (b) ω_dom = 2.96·ω_C → substrate ℓ=5 cavity mode (A38)
    (c) ω_dom = ω_C = 1.0 → corpus electron candidate (surprising at
        chair-ring scale; would warrant characterize-as-itself per Rule 10)
    (d) ω_dom varies across cells → no coherent single-mode reading;
        characterize-as-itself

Bonus diagnostic: ω at substrate-mode candidates (1.5, 2.96) vs at ω_C.
Compare amplitudes — confirms substrate mode dominates over corpus
electron candidate.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
from ave.topological.vacuum_engine import VacuumEngine3D
from scripts.vol_1_foundations.tlm_electron_soliton_eigenmode import (
    initialize_2_3_voltage_ansatz,
)


COMPTON_PERIOD = 2.0 * np.pi
DT = 1.0 / np.sqrt(2.0)


def main():
    print("=" * 78, flush=True)
    print("  O.1e — FFT Cavity-vs-Flux Discriminator")
    print("=" * 78, flush=True)

    N, PML = 48, 4
    n_steps = int(50 * COMPTON_PERIOD / DT)
    R, r = 8.0, 4.0
    amp = 0.1

    t_start = time.time()
    engine = VacuumEngine3D.from_args(
        N=N, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )
    initialize_2_3_voltage_ansatz(engine.k4, R=R, r=r, amplitude=amp)

    # 5 shell-mode sample cells at varied (phi, psi)
    cx, cy, cz = (N - 1) // 2, (N - 1) // 2, (N - 1) // 2
    sample_points = []
    for phi_n, psi_n in [
        (0.0, 0.0),         # Equatorial east
        (np.pi/2, 0.0),     # Equatorial north
        (np.pi, np.pi/2),   # Top of west
        (3*np.pi/2, np.pi), # Bottom of south (psi=π puts it on inner edge)
        (np.pi/4, np.pi/4), # Diagonal
    ]:
        x = int(round(cx + (R + r * np.cos(psi_n)) * np.cos(phi_n)))
        y = int(round(cy + (R + r * np.cos(psi_n)) * np.sin(phi_n)))
        z = int(round(cz + r * np.sin(psi_n)))
        x = max(1, min(N - 2, x))
        y = max(1, min(N - 2, y))
        z = max(1, min(N - 2, z))
        sample_points.append((phi_n, psi_n, x, y, z))

    print(f"\n  Sample cells:")
    for phi_n, psi_n, x, y, z in sample_points:
        print(f"    (φ={phi_n:.3f}, ψ={psi_n:.3f}) → ({x}, {y}, {z})")

    # Time series storage
    n_samples = len(sample_points)
    v_inc_traj = np.zeros((n_samples, n_steps, 4))   # 5 cells × n_steps × 4 ports

    print(f"\n  Running {n_steps} steps...", flush=True)
    for step_i in range(n_steps):
        engine.step()
        for si, (_, _, x, y, z) in enumerate(sample_points):
            v_inc_traj[si, step_i] = engine.k4.V_inc[x, y, z, :]
        if step_i % 100 == 0:
            t_p = step_i * DT / COMPTON_PERIOD
            print(f"    t={t_p:5.2f}P  ({time.time() - t_start:.0f}s)", flush=True)

    elapsed = time.time() - t_start
    print(f"\n  Engine evolution complete in {elapsed:.0f}s")

    # FFT analysis post-transient
    transient_steps = int(11.0 * COMPTON_PERIOD / DT)
    n_post = n_steps - transient_steps
    target_freqs = [
        ('ω_C/2 (subharmonic)', 0.5),
        ('ω_C', 1.0),
        ('1.5·ω_C (substrate ℓ=2)', 1.5),
        ('2·ω_C', 2.0),
        ('2.96·ω_C (substrate ℓ=5)', 2.96),
        ('3·ω_C', 3.0),
    ]

    print(f"\n  FFT analysis (post-transient window, t > 11P):")
    print(f"  Sample window: {n_post} timesteps × dt={DT:.4f} = {n_post*DT:.2f} time units")

    fft_results_per_cell = []
    for si, (phi_n, psi_n, x, y, z) in enumerate(sample_points):
        v_traj_post = v_inc_traj[si, transient_steps:, 0]   # port 0
        n = len(v_traj_post)
        fft_vals = np.fft.rfft(v_traj_post)
        freqs_omega = np.fft.rfftfreq(n, d=DT) * 2.0 * np.pi
        fft_amp = 2.0 * np.abs(fft_vals) / n

        # Find dominant frequency
        peak_idx = int(np.argmax(fft_amp))
        peak_omega = float(freqs_omega[peak_idx])
        peak_amp = float(fft_amp[peak_idx])

        # Amplitude at each target frequency
        target_amps = {}
        for name, omega_target in target_freqs:
            idx = int(np.argmin(np.abs(freqs_omega - omega_target)))
            target_amps[name] = (float(freqs_omega[idx]), float(fft_amp[idx]))

        print(f"\n  Cell ({x}, {y}, {z}) at (φ={phi_n:.3f}, ψ={psi_n:.3f}):")
        print(f"    Dominant peak: ω = {peak_omega:.4f}, amp = {peak_amp:.4e}")
        print(f"    {'Target':>30} {'ω_actual':>12} {'amplitude':>12}")
        for name, (omega_act, amp_at) in target_amps.items():
            flag = " ★" if amp_at == peak_amp else ""
            print(f"    {name:>30} {omega_act:>12.4f} {amp_at:>12.4e}{flag}")

        fft_results_per_cell.append({
            "cell": [x, y, z],
            "phi": float(phi_n),
            "psi": float(psi_n),
            "peak_omega": peak_omega,
            "peak_amplitude": peak_amp,
            "amplitude_at_target_freqs": {name: a for name, (_, a) in target_amps.items()},
        })

    # Cross-cell consensus
    print(f"\n  CROSS-CELL CONSENSUS:")
    peaks = [r["peak_omega"] for r in fft_results_per_cell]
    peaks_arr = np.array(peaks)
    median_peak = float(np.median(peaks_arr))
    range_peak = float(peaks_arr.max() - peaks_arr.min())
    print(f"    Peak ω across {n_samples} cells: median = {median_peak:.4f}, "
          f"range = {range_peak:.4f}")
    print(f"    Compare to candidates:")
    print(f"      ω_C = 1.0: |median - 1.0| = {abs(median_peak - 1.0):.4f}")
    print(f"      1.5·ω_C = 1.5: |median - 1.5| = {abs(median_peak - 1.5):.4f}")
    print(f"      2.96·ω_C = 2.96: |median - 2.96| = {abs(median_peak - 2.96):.4f}")

    # Verdict
    if abs(median_peak - 1.5) < 0.15:
        verdict = "Substrate ℓ=2 cavity mode (A38) at 1.5·ω_C"
    elif abs(median_peak - 2.96) < 0.30:
        verdict = "Substrate ℓ=5 cavity mode (A38) at 2.96·ω_C"
    elif abs(median_peak - 1.0) < 0.05:
        verdict = "Near ω_C — corpus electron candidate (surprising at chair-ring scale)"
    else:
        verdict = f"Other (ω = {median_peak:.4f}); characterize-as-itself per Rule 10"

    print(f"\n  VERDICT: {verdict}")

    out = {
        "test": "O.1e: FFT cavity-vs-flux discriminator",
        "config": {"N": N, "amp": amp, "R": R, "r": r},
        "transient_window_starts_at": transient_steps,
        "n_post_transient_steps": n_post,
        "fft_per_cell": fft_results_per_cell,
        "cross_cell_median_peak_omega": median_peak,
        "cross_cell_range": range_peak,
        "verdict": verdict,
        "elapsed_total_s": float(elapsed),
    }
    out_path = Path(__file__).parent / "r10_v8_o1e_fft_cavity_vs_flux_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
