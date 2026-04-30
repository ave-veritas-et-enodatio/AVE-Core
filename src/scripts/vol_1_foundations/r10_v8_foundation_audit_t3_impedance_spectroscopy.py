"""
Foundation Audit Test 3: Impedance Spectroscopy (drive-frequency sweep).

Drives the substrate at a continuous wave (CW) at varying frequencies,
measures the steady-state response amplitude. Maps mode coupling
strength vs drive frequency without seeding any specific topology.

Per auditor 2026-04-30 analytical note: Test 3 is the most direct
extension of T1's mode-spectrum finding. Pulse-ringdown FFT shows what's
there (broadband response); impedance spectroscopy shows what couples
strongest to drive at each frequency.

Discriminator for the chair-ring 1.48·ω_C interpretation:
  - If 1.5·ω_C is sharply resonant under CW drive (peak >> nearby
    frequencies): substrate has a discrete resonance, chair-ring
    amplifies it
  - If 1.5·ω_C is broadly preferred without sharp peak: substrate prefers
    1.5 generally, chair-ring just lives there

Test design:
  - 16³ K4 lattice, PML=4, low-amplitude CW drive (no saturation)
  - Drive on 4 ports at center A-site (symmetric, isotropic IC drive)
  - Sweep drive frequencies: ω/ω_C ∈ {0.3, 0.5, 0.577, 0.7, 1.0, 1.2,
    1.5, 1.7, 1.81, 2.0, 2.5, 2.96, 3.5, 4.0}
  - Each drive: 50 Compton periods, take steady-state amplitude
    (post-25P transient)
  - Plot |V_inc|²_steady vs ω → resonance map
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.vacuum_engine import VacuumEngine3D


def run_cw_drive(omega_drive, n_periods=50, N=16, PML=4, drive_amplitude=0.001):
    """Drive at frequency omega_drive (in ω_C units), measure steady-state response."""
    DT = 1.0 / np.sqrt(2.0)
    COMPTON_PERIOD = 2.0 * np.pi
    N_STEPS = int(n_periods * COMPTON_PERIOD / DT)

    engine = VacuumEngine3D.from_args(
        N=N, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=False,
    )

    center = (N // 2, N // 2, N // 2)

    # Track V_inc at center port 0 over time
    v_traj = np.zeros(N_STEPS)

    for i in range(N_STEPS):
        # CW drive: inject sinusoidal V_inc at center, all 4 ports
        t = i * DT
        drive_value = drive_amplitude * np.cos(omega_drive * t)
        for p in range(4):
            engine.k4.V_inc[center[0], center[1], center[2], p] += drive_value

        engine.step()

        v_traj[i] = engine.k4.V_inc[center[0], center[1], center[2], 0]

    # Steady-state RMS (post-25P transient)
    sw_start = int(25.0 * COMPTON_PERIOD / DT)
    if sw_start < N_STEPS:
        v_steady = v_traj[sw_start:]
        v_rms = float(np.sqrt(np.mean(v_steady**2)))
        v_peak = float(np.max(np.abs(v_steady)))
        # Lock-in at drive frequency for response amplitude
        t_steady = np.arange(len(v_steady)) * DT + sw_start * DT
        cos_drive = np.cos(omega_drive * t_steady)
        sin_drive = np.sin(omega_drive * t_steady)
        I = 2.0 * float(np.mean(v_steady * cos_drive))  # in-phase
        Q = 2.0 * float(np.mean(v_steady * sin_drive))  # quadrature
        amplitude_at_drive_freq = float(np.sqrt(I**2 + Q**2))
        phase_at_drive_freq = float(np.arctan2(Q, I))
    else:
        v_rms = 0.0
        v_peak = 0.0
        amplitude_at_drive_freq = 0.0
        phase_at_drive_freq = 0.0

    return {
        "omega_drive": omega_drive,
        "v_rms_steady": v_rms,
        "v_peak_steady": v_peak,
        "amplitude_at_drive_freq": amplitude_at_drive_freq,
        "phase_at_drive_freq": phase_at_drive_freq,
        "n_steps": N_STEPS,
    }


def main():
    print("=" * 78, flush=True)
    print("  Foundation Audit Test 3: Impedance Spectroscopy")
    print("  Drive-frequency sweep at low amplitude")
    print("=" * 78, flush=True)

    # Drive frequencies to sweep (ω in ω_C units)
    drive_freqs = [0.3, 0.5, 0.577, 0.7, 0.9, 1.0, 1.2, 1.4, 1.5,
                   1.6, 1.7, 1.81, 2.0, 2.5, 2.96, 3.5, 4.0]

    print(f"  Sweeping {len(drive_freqs)} drive frequencies")
    print(f"  Each drive: 50 Compton periods (~14s each)")
    print()

    results = []
    t_start = time.time()
    for ω in drive_freqs:
        t0 = time.time()
        r = run_cw_drive(omega_drive=ω, n_periods=50)
        elapsed = time.time() - t0
        print(f"    ω={ω:.3f}: lockin amp={r['amplitude_at_drive_freq']:.3e}, "
              f"phase={np.degrees(r['phase_at_drive_freq']):+.1f}°, "
              f"steady RMS={r['v_rms_steady']:.3e}  ({elapsed:.1f}s)")
        results.append(r)

    total_elapsed = time.time() - t_start
    print(f"\n  Total elapsed: {total_elapsed:.1f}s")

    # Find resonance peaks
    print()
    print("  Lock-in amplitude at drive frequency vs ω:")
    print(f"    {'ω/ω_C':>8} {'amplitude':>12} {'phase°':>10}")
    omegas = [r["omega_drive"] for r in results]
    amps = [r["amplitude_at_drive_freq"] for r in results]
    phases = [np.degrees(r["phase_at_drive_freq"]) for r in results]
    for o, a, p in zip(omegas, amps, phases):
        flag = " ★" if a == max(amps) else ""
        print(f"    {o:>8.3f} {a:>12.4e} {p:>+10.1f}{flag}")

    # Identify peaks (local maxima)
    print()
    print("  Local maxima in response amplitude (resonances):")
    for i in range(1, len(amps) - 1):
        if amps[i] > amps[i-1] and amps[i] > amps[i+1]:
            print(f"    ω={omegas[i]:.3f}: amplitude={amps[i]:.4e}")

    # Compare to T1 findings
    print()
    print("  Comparison to T1 pulse-ringdown candidate frequencies:")
    candidates = {"ω_TL=0.577": 0.577, "ω_C=1.0": 1.0, "1.5·ω_C": 1.5,
                  "π/√3=1.81": 1.81, "2.96·ω_C": 2.96}
    for name, ω_target in candidates.items():
        # Find nearest drive frequency
        nearest_idx = np.argmin([abs(o - ω_target) for o in omegas])
        print(f"    {name}: drive ω={omegas[nearest_idx]:.3f}, "
              f"amp={amps[nearest_idx]:.4e}")

    out = {
        "test": "Foundation Audit Test 3: Impedance Spectroscopy",
        "drive_frequencies": drive_freqs,
        "results": results,
        "elapsed_total_s": total_elapsed,
    }
    out_path = Path(__file__).parent / "r10_v8_foundation_audit_t3_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
