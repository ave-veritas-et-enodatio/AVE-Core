"""
T-ST Dispersion Cross-Check: linear-regime group velocity at ω_C.

Per auditor 2026-04-30 (post-T-ST FAIL): the most load-bearing finding from T-ST
was the velocity anomaly — wave packet at ω = ω_C propagated at v_g = 0.364
cells/time-unit (predicted √2 = 1.414). Saturation never engaged (A²_max =
0.0097, 12× below √(2α) = 0.121), so A-010 local-clock-modulation
(c_eff = c·√(1-A²)) does not explain the 4× slowdown.

Connection to T3: substrate has discrete reactive modes at 1.5·ω_C and
2.96·ω_C (T3 + T3b). ω_C = 1.0 is BETWEEN those modes — potentially the
off-resonance regime where coherent propagation is dispersion-suppressed.

== Pre-registered cross-check (frozen 2026-04-30) ==

Same configuration as T-ST except A = 0.001 V_SNAP (1000× below saturation
onset, deeply linear regime). Measure free-propagation v_g.

DISCRIMINATOR:
  - If v_g ≈ √2 ± 10% at A=0.001 → ω_C supports coherent propagation;
    T-ST velocity slowdown was amplitude-coupled (α). Need: higher
    amplitude / tighter focus to engage saturation.
  - If v_g ≈ 0.36 at A=0.001 (still ~4× slow) → ω_C is structurally
    off-resonance for K4-TLM at this config (β). Rifling-bullet at ω_C
    is structurally untestable without addressing off-resonance regime
    first. Anchors the medium-framing reframe with empirical evidence.
  - If v_g lands intermediate → something between; characterize-as-itself.

PASS/FAIL not framed as hypothesis test — this is a structural diagnostic.
Goal: report v_g at low amplitude, compare to T-ST's v_g at high amplitude.

== Configuration (matches T-ST exactly except amplitude) ==

- N=48, PML=4
- Cosserat ON, A28-corrected (disable_cosserat_lc_force=True,
  enable_cosserat_self_terms=True)
- SpatialDipoleCPSource: x0=8, propagation=+x, RH, omega=1.0,
  sigma_yz=4.0, envelope 2P+2P+2P
- A = 0.001 V_SNAP (vs 0.10 in T-ST — factor 100× lower)
- Run: 50 Compton periods (444 timesteps)
- Capture cadence: every 5 timesteps

== Compute estimate ==

Same engine evolution cost as T-ST: ~185s wall clock + minimal post-process.
Total: ~3-4 min.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.vacuum_engine import (
    VacuumEngine3D,
    SpatialDipoleCPSource,
)


OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi
DT = 1.0 / np.sqrt(2.0)


def setup_engine(N=48, PML=4):
    """A28-corrected coupled engine (matches T-ST)."""
    return VacuumEngine3D.from_args(
        N=N, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )


def setup_source(amplitude):
    """Same source as T-ST, only amplitude changes."""
    return SpatialDipoleCPSource(
        x0=8,
        propagation_axis=0,
        amplitude=amplitude,
        omega=OMEGA_C,
        handedness="RH",
        sigma_yz=4.0,
        t_ramp=2.0 * COMPTON_PERIOD,
        t_sustain=2.0 * COMPTON_PERIOD,
        t_decay=2.0 * COMPTON_PERIOD,
    )


def compute_centroid_along_axis(V_inc, mask_active, pml=4):
    """Energy-weighted centroid along x (PML excluded)."""
    N = V_inc.shape[0]
    energy = np.sum(V_inc ** 2, axis=-1) * mask_active.astype(float)
    energy[:pml, :, :] = 0.0
    energy[N - pml:, :, :] = 0.0
    energy[:, :pml, :] = 0.0
    energy[:, N - pml:, :] = 0.0
    energy[:, :, :pml] = 0.0
    energy[:, :, N - pml:] = 0.0
    total = float(np.sum(energy))
    if total < 1e-30:
        return float("nan"), 0.0
    coords = np.arange(N, dtype=float)
    marg = np.sum(energy, axis=(1, 2))
    centroid = float(np.sum(coords * marg) / total)
    return centroid, total


def compute_front_along_axis(V_inc, mask_active, pml=4, frac=0.5):
    """Leading edge along x: rightmost cell with E(x) > frac·E_max."""
    N = V_inc.shape[0]
    energy = np.sum(V_inc ** 2, axis=-1) * mask_active.astype(float)
    energy[:pml, :, :] = 0.0
    energy[N - pml:, :, :] = 0.0
    energy[:, :pml, :] = 0.0
    energy[:, N - pml:, :] = 0.0
    energy[:, :, :pml] = 0.0
    energy[:, :, N - pml:] = 0.0
    marg = np.sum(energy, axis=(1, 2))
    if marg.max() < 1e-30:
        return float("nan")
    threshold = frac * marg.max()
    above = np.where(marg > threshold)[0]
    if len(above) == 0:
        return float("nan")
    return float(above[-1])


def run_at_amplitude(amplitude, N=48, PML=4, n_periods=50, capture_cadence=5):
    """Single run at given source amplitude. Returns velocity diagnostic."""
    n_steps = int(n_periods * COMPTON_PERIOD / DT)

    engine = setup_engine(N=N, PML=PML)
    source = setup_source(amplitude=amplitude)
    engine.add_source(source)

    centroid_traj = []
    front_traj = []
    max_a2_traj = []

    for step_i in range(n_steps):
        engine.step()
        if step_i % capture_cadence == 0:
            t_now = step_i * DT
            V_inc = engine.k4.V_inc
            mask = engine.k4.mask_active
            cx, total_e = compute_centroid_along_axis(V_inc, mask, pml=PML)
            front_x = compute_front_along_axis(V_inc, mask, pml=PML)
            a2 = np.sum(V_inc ** 2, axis=-1) / (engine.V_SNAP ** 2)
            a2_int = a2.copy()
            a2_int[~mask] = 0.0
            a2_int[:PML, :, :] = 0.0
            a2_int[N - PML:, :, :] = 0.0
            max_a2 = float(a2_int.max())
            centroid_traj.append((t_now, cx))
            front_traj.append((t_now, front_x))
            max_a2_traj.append((t_now, max_a2))

    return centroid_traj, front_traj, max_a2_traj


def fit_velocity(traj, t_min, t_max):
    """Linear fit slope of x(t) over [t_min, t_max]. Returns v in cells/time-unit."""
    arr = np.array([(t, x) for t, x in traj if not np.isnan(x)])
    if len(arr) < 3:
        return float("nan"), 0
    mask = (arr[:, 0] >= t_min) & (arr[:, 0] <= t_max)
    if mask.sum() < 3:
        return float("nan"), int(mask.sum())
    slope = float(np.polyfit(arr[mask, 0], arr[mask, 1], 1)[0])
    return slope, int(mask.sum())


def main():
    print("=" * 78, flush=True)
    print("  T-ST Dispersion Cross-Check")
    print("  Discriminate (α) amplitude-coupled vs (β) ω_C-off-resonance")
    print("=" * 78, flush=True)

    A_LOW = 0.001
    print(f"\n  Single run: A = {A_LOW} V_SNAP (1000× below saturation onset)")
    print(f"  Lattice: N=48, PML=4, Cosserat ON, A28-corrected coupling")
    print(f"  Source: SpatialDipoleCPSource RH @ x0=8, ω=ω_C, sigma_yz=4.0")

    t_start = time.time()
    centroid_traj, front_traj, max_a2_traj = run_at_amplitude(amplitude=A_LOW)
    elapsed = time.time() - t_start
    print(f"\n  Engine evolution complete in {elapsed:.0f}s")

    # Fit velocity in free-propagation regime (before front hits PML)
    # T-ST showed front reached PML at ~11P; restrict fit to t < 8P for safety
    v_free_low, n_pts_low = fit_velocity(centroid_traj, 0.5 * COMPTON_PERIOD,
                                          8.0 * COMPTON_PERIOD)
    v_front_low, n_pts_front = fit_velocity(front_traj, 0.5 * COMPTON_PERIOD,
                                             8.0 * COMPTON_PERIOD)

    # Peak A² should be ~A² of input (≈ 1e-6) — confirms linear regime
    max_a2_overall = max(a2 for _, a2 in max_a2_traj)

    print()
    print(f"  Velocity diagnostic (centroid fit over 0.5P–8P):")
    print(f"    v_g (centroid)  = {v_free_low:.3f} cells/time-unit "
          f"({n_pts_low} fit points)")
    print(f"    v_g (front)     = {v_front_low:.3f} cells/time-unit "
          f"({n_pts_front} fit points)")
    print(f"    Predicted free  = {np.sqrt(2):.3f} (Cartesian-axis K4-TLM)")
    print(f"  Peak A² across run = {max_a2_overall:.2e} "
          f"(confirms linear regime: predicted ≈ {A_LOW**2:.2e})")

    # Comparison to T-ST result
    v_tst_high = 0.364   # from T-ST run at A=0.10
    print(f"\n  Comparison to T-ST (A=0.10):")
    print(f"    T-ST v_g (high amp)   = {v_tst_high:.3f}")
    print(f"    T-ST v_g (this, low)  = {v_free_low:.3f}")
    if not np.isnan(v_free_low):
        ratio_to_sqrt2 = v_free_low / np.sqrt(2)
        print(f"    v_low / √2            = {ratio_to_sqrt2:.3f}")

    # Verdict (NOT a hypothesis pass/fail — characterize-as-itself per Rule 10)
    print()
    print("=" * 78)
    print("  STRUCTURAL READING")
    print("=" * 78)

    if np.isnan(v_free_low):
        print("\n  Could not extract free-propagation velocity. Wave packet may have")
        print("  failed to form coherently or dissipated immediately.")
    else:
        ratio = v_free_low / np.sqrt(2)
        if ratio > 0.85:
            print(f"\n  v_g / √2 = {ratio:.3f} > 0.85 → ω_C SUPPORTS coherent")
            print(f"    propagation in linear regime. T-ST slowdown was")
            print(f"    amplitude-coupled (α): (1) source amp/focus issue, OR")
            print(f"    (2) some non-saturation nonlinear engagement at A=0.10")
            print(f"    that A-010 local-clock prediction misses.")
        elif ratio < 0.5:
            print(f"\n  v_g / √2 = {ratio:.3f} < 0.5 → ω_C is STRUCTURALLY")
            print(f"    off-resonance for K4-TLM at this config (β confirmed).")
            print(f"    Rifling-bullet at ω_C is structurally untestable without")
            print(f"    addressing off-resonance regime first. Anchors medium-")
            print(f"    framing reframe at substrate-resonance level.")
            print(f"    Connection: T3 found substrate modes at 1.5 + 2.96·ω_C;")
            print(f"    ω_C = 1.0 is between, off-resonance.")
        else:
            print(f"\n  v_g / √2 = {ratio:.3f} (intermediate) → mixed reading.")
            print(f"    Some dispersion suppression, some amplitude coupling.")
            print(f"    Characterize-as-itself per Rule 10; further sweep needed.")

    out = {
        "test": "T-ST Dispersion Cross-Check",
        "config": {
            "N": 48, "PML": 4, "n_periods": 50,
            "amplitude_VSNAP": A_LOW, "omega": OMEGA_C, "handedness": "RH",
        },
        "v_centroid_low_amp": float(v_free_low) if not np.isnan(v_free_low) else None,
        "v_front_low_amp": float(v_front_low) if not np.isnan(v_front_low) else None,
        "v_predicted_sqrt2": float(np.sqrt(2)),
        "v_centroid_T_ST_high_amp": v_tst_high,
        "max_a2_across_run": float(max_a2_overall),
        "centroid_trajectory": [[float(t), float(x) if not np.isnan(x) else None]
                                for t, x in centroid_traj],
        "front_trajectory": [[float(t), float(x) if not np.isnan(x) else None]
                             for t, x in front_traj],
        "elapsed_total_s": float(elapsed),
    }
    out_path = Path(__file__).parent / "r10_v8_t_st_dispersion_check_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
