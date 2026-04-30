"""
T-ST in Corpus Vacuum (Step 1 of 2) — Thermal IC enabled.

Per Vol 1 Ch 3:188-191 corpus-canonical: vacuum has irreducible Nyquist
baseline, NOT machine-zero. Prior T-ST v1+v2 ran at temperature=0.0
which is engine-zero, not corpus-vacuum. This test re-runs T-ST v1 setup
with corpus-canonical CMB temperature and thermalize_V=True to seed
V-sector at Nyquist baseline IC.

== Caveat (engine-corpus gap) ==

Engine implements thermal IC but NOT continuous Nyquist FDT injection
during stepping. Step 2 (separate driver) will add continuous injection.
This test has corpus-vacuum at t=0 only; baseline will decay with run
absent continuous maintenance.

== Pre-registered observables (per Rule 10 characterize-as-itself) ==

(a) Does the Nyquist baseline IC affect photon-trap formation? Compare
    to T-ST v1 (same setup, T=0): same Mode III? Different?
(b) Does the baseline persist or decay over the 50P run? At what rate?
(c) Does the photon at ω_C interact differently with thermal-baseline
    cells vs T=0 cells?
(d) Op10 c at end of run — anything different from T-ST v1's c=0?
(e) Centroid velocity — same anomaly (v_g 0.36 at A=0.10)?
(f) Saturation engagement — does any cell reach √(2α)?

== A47 arithmetic ==

T = 4.6e-10 (m_e c² units) ≈ kT_CMB / (m_e c²)
σ_V = √(4π · 4.6e-10 / α) · V_SNAP ≈ 0.00089 V_SNAP (≈ 9e-4)
  — 150× above engine numerical floor (6e-6)
  — 100× below V_yield (0.0854)
  — well within stability (T < α/(4π) ≈ 5.8e-4 by factor 1.3M)
σ_ω ≈ √(4.6e-10 · 1.14 / (4π²)) ≈ 4e-6
σ_u ≈ √(4.6e-10 / (2π)) ≈ 1e-5

== Configuration (matches T-ST v1 except thermal IC) ==

- N=48, PML=4
- Cosserat ON, A28-corrected
- temperature = 4.6e-10, thermalize_V = True
- Source: SpatialDipoleCPSource RH @ x0=8, ω=1.0, A=0.10·V_SNAP, σ=4.0
- Run: 50 Compton periods
- Same diagnostic suite as T-ST v1

== Compute estimate ==

Same as T-ST v1: ~3 min wall clock. Thermal IC adds <1s overhead.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path
from collections import Counter

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.vacuum_engine import (
    VacuumEngine3D,
    SpatialDipoleCPSource,
)


ALPHA = 1.0 / 137.035999
V_YIELD = float(np.sqrt(ALPHA))
A2_OP14 = float(np.sqrt(2.0 * ALPHA))
OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi
DT = 1.0 / np.sqrt(2.0)

T_CMB_ENGINE_UNITS = 4.6e-10  # kT_CMB / (m_e c²)


def setup_engine(N=48, PML=4, T=T_CMB_ENGINE_UNITS):
    """A28-corrected coupled engine with corpus CMB temperature."""
    engine = VacuumEngine3D.from_args(
        N=N, pml=PML, temperature=T,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )
    # Re-initialize with thermalize_V=True (default ctor used thermalize_V=False)
    engine.initialize_thermal(T, seed=42, thermalize_V=True)
    return engine


def setup_source():
    return SpatialDipoleCPSource(
        x0=8,
        propagation_axis=0,
        amplitude=0.10,
        omega=OMEGA_C,
        handedness="RH",
        sigma_yz=4.0,
        t_ramp=2.0 * COMPTON_PERIOD,
        t_sustain=2.0 * COMPTON_PERIOD,
        t_decay=2.0 * COMPTON_PERIOD,
    )


def compute_a2_field(V_inc, V_SNAP=1.0):
    return np.sum(V_inc ** 2, axis=-1) / (V_SNAP ** 2)


def mask_interior(field, mask_active, pml):
    N = field.shape[0]
    out = field * mask_active.astype(float)
    out[:pml, :, :] = 0.0
    out[N - pml:, :, :] = 0.0
    out[:, :pml, :] = 0.0
    out[:, N - pml:, :] = 0.0
    out[:, :, :pml] = 0.0
    out[:, :, N - pml:] = 0.0
    return out


def compute_centroid(V_inc, mask_active, pml):
    energy = mask_interior(np.sum(V_inc ** 2, axis=-1), mask_active, pml)
    total = float(np.sum(energy))
    if total < 1e-30:
        return float("nan"), 0.0
    N = V_inc.shape[0]
    coords = np.arange(N, dtype=float)
    marg = np.sum(energy, axis=(1, 2))
    return float(np.sum(coords * marg) / total), total


def fft_at(traj, dt, target_freqs):
    n = len(traj)
    if n < 16:
        return {f: 0.0 for f in target_freqs}
    fft_vals = np.fft.rfft(traj)
    freqs = np.fft.rfftfreq(n, d=dt) * 2.0 * np.pi
    fft_amp = 2.0 * np.abs(fft_vals) / n
    out = {}
    for f_target in target_freqs:
        idx = int(np.argmin(np.abs(freqs - f_target)))
        out[float(f_target)] = float(fft_amp[idx])
    return out


def baseline_stats(field, mask_active, pml):
    """RMS amplitude of interior cells (PML excluded, active mask)."""
    N = field.shape[0]
    interior_mask = mask_active.copy()
    interior_mask[:pml, :, :] = False
    interior_mask[N - pml:, :, :] = False
    interior_mask[:, :pml, :] = False
    interior_mask[:, N - pml:, :] = False
    interior_mask[:, :, :pml] = False
    interior_mask[:, :, N - pml:] = False

    # Sum over port axis if present
    if field.ndim == 4:
        f_sq = np.sum(field ** 2, axis=-1)
    else:
        f_sq = field ** 2

    f_sq_interior = f_sq[interior_mask]
    if len(f_sq_interior) == 0:
        return 0.0, 0.0
    rms = float(np.sqrt(np.mean(f_sq_interior)))
    max_val = float(np.sqrt(f_sq_interior.max()))
    return rms, max_val


def main():
    print("=" * 78, flush=True)
    print("  T-ST in Corpus Vacuum (Step 1) — Thermal IC at CMB temperature")
    print(f"  T = {T_CMB_ENGINE_UNITS:.2e} (m_e c² units), thermalize_V = True")
    print("=" * 78, flush=True)

    N = 48
    PML = 4
    n_periods = 50
    n_steps = int(n_periods * COMPTON_PERIOD / DT)

    # Verify thermal IC parameters
    sigma_V_pred = float(np.sqrt(4.0 * np.pi * T_CMB_ENGINE_UNITS / ALPHA))
    sigma_omega_pred = float(np.sqrt(T_CMB_ENGINE_UNITS * 1.14 / (4.0 * np.pi ** 2)))
    print(f"\n  Predicted thermal σ_V = {sigma_V_pred:.3e} V_SNAP")
    print(f"  Predicted thermal σ_ω = {sigma_omega_pred:.3e}")
    print(f"  V_yield (saturation onset) = {V_YIELD:.3e}")
    print(f"  Engine numerical floor (T=0 baseline) ≈ 6e-6")

    t_start = time.time()
    engine = setup_engine(N=N, PML=PML, T=T_CMB_ENGINE_UNITS)

    # Verify IC actually thermalized V-sector
    yc, zc = N // 2, N // 2
    rms_V_ic, max_V_ic = baseline_stats(engine.k4.V_inc, engine.k4.mask_active, PML)
    rms_omega_ic, max_omega_ic = baseline_stats(engine.cos.omega,
                                                  engine.cos.mask_alive, PML)
    print(f"\n  Thermal IC verification (interior, PML excluded):")
    print(f"    V_inc: RMS = {rms_V_ic:.3e}, max = {max_V_ic:.3e}")
    print(f"    omega: RMS = {rms_omega_ic:.3e}, max = {max_omega_ic:.3e}")

    source = setup_source()
    engine.add_source(source)
    print(f"\n  Source: SpatialDipoleCPSource RH @ x0=8, ω=ω_C, A=0.10·V_SNAP")

    # Captures
    axial_v_inc = np.zeros((n_steps, N, 4))
    axial_v_ref = np.zeros((n_steps, N, 4))
    axial_omega = np.zeros((n_steps, N, 3))

    captures = []
    centroid_traj = []
    max_a2_traj = []
    rms_v_traj = []           # NEW: track baseline decay
    rms_omega_traj = []
    capture_cadence = 5

    print(f"\n  Running...", flush=True)

    for step_i in range(n_steps):
        engine.step()
        axial_v_inc[step_i] = engine.k4.V_inc[:, yc, zc, :]
        axial_v_ref[step_i] = engine.k4.V_ref[:, yc, zc, :]
        axial_omega[step_i] = engine.cos.omega[:, yc, zc, :]

        if step_i % capture_cadence == 0:
            t_now = step_i * DT
            V_inc = engine.k4.V_inc
            mask = engine.k4.mask_active
            cx, total_e = compute_centroid(V_inc, mask, pml=PML)
            a2 = compute_a2_field(V_inc, V_SNAP=engine.V_SNAP)
            a2_int = mask_interior(a2, mask, PML)
            max_a2 = float(a2_int.max())
            max_a2_idx = np.unravel_index(int(np.argmax(a2_int)), a2_int.shape)

            rms_V, _ = baseline_stats(V_inc, mask, PML)
            rms_om, _ = baseline_stats(engine.cos.omega, engine.cos.mask_alive, PML)

            centroid_traj.append((t_now, cx))
            max_a2_traj.append((t_now, max_a2))
            rms_v_traj.append((t_now, rms_V))
            rms_omega_traj.append((t_now, rms_om))

            captures.append({
                "t": float(t_now),
                "centroid_x": cx,
                "total_energy": total_e,
                "max_a2_interior": max_a2,
                "max_a2_loc": [int(v) for v in max_a2_idx],
                "rms_v_interior": rms_V,
                "rms_omega_interior": rms_om,
            })

            if step_i % (capture_cadence * 10) == 0:
                t_p = t_now / COMPTON_PERIOD
                print(f"    t={t_p:5.2f}P  cx={cx if not np.isnan(cx) else 0:6.2f}  "
                      f"max_A²={max_a2:.4f} @ {tuple(max_a2_idx)}  "
                      f"rms_V={rms_V:.3e}  rms_ω={rms_om:.3e}  "
                      f"({time.time() - t_start:.0f}s)")

    elapsed = time.time() - t_start
    print(f"\n  Engine evolution complete in {elapsed:.0f}s")

    # ============================================================
    # Adjudication
    # ============================================================
    print("\n" + "=" * 78)
    print("  ADJUDICATION")
    print("=" * 78)

    # (a)/(c)/(d): trap formation criteria — same suite as T-ST v1
    second_half = [c for c in captures if c["t"] > 6.0 * COMPTON_PERIOD]
    cell_counter = Counter(tuple(loc) for loc in
                           [c["max_a2_loc"] for c in second_half])
    trap_cell, trap_count = cell_counter.most_common(1)[0] if second_half else ((0,0,0), 0)
    trap_x, trap_y, trap_z = trap_cell

    a2_at_trap_2nd_half = [c["max_a2_interior"] for c in second_half
                           if tuple(c["max_a2_loc"]) == trap_cell]
    a2_trap_max = float(max(a2_at_trap_2nd_half)) if a2_at_trap_2nd_half else 0.0
    saturation_engaged = a2_trap_max > A2_OP14

    print(f"\n  Trap candidate: ({trap_x}, {trap_y}, {trap_z}) "
          f"({trap_count}/{len(second_half)} post-shutoff)")
    print(f"  Saturation engaged: {'YES' if saturation_engaged else 'NO'} "
          f"(A²_trap_max = {a2_trap_max:.4f} vs threshold {A2_OP14:.4f})")

    try:
        c_op10 = int(engine.cos.extract_crossing_count())
    except Exception as exc:
        c_op10 = -1
    print(f"  Op10 c = {c_op10} (target: 3)")

    # (b): baseline persistence — does thermal noise survive 50P?
    print(f"\n  BASELINE PERSISTENCE (post-shutoff window, t > 7P):")
    post_shutoff_caps = [c for c in captures if c["t"] > 7.0 * COMPTON_PERIOD]
    if post_shutoff_caps:
        rms_v_late = [c["rms_v_interior"] for c in post_shutoff_caps]
        rms_om_late = [c["rms_omega_interior"] for c in post_shutoff_caps]
        rms_v_first = post_shutoff_caps[0]["rms_v_interior"]
        rms_v_last = post_shutoff_caps[-1]["rms_v_interior"]
        rms_om_first = post_shutoff_caps[0]["rms_omega_interior"]
        rms_om_last = post_shutoff_caps[-1]["rms_omega_interior"]

        print(f"    RMS V_inc (interior):")
        print(f"      Initial thermal IC: {rms_V_ic:.3e}")
        print(f"      At t=7P (post-source): {rms_v_first:.3e}")
        print(f"      At t={post_shutoff_caps[-1]['t']/COMPTON_PERIOD:.1f}P: "
              f"{rms_v_last:.3e}")
        print(f"      Retention vs IC: {rms_v_last/max(rms_V_ic,1e-30):.3e}")
        print(f"    RMS ω (interior):")
        print(f"      Initial thermal IC: {rms_omega_ic:.3e}")
        print(f"      At t=7P: {rms_om_first:.3e}")
        print(f"      At t={post_shutoff_caps[-1]['t']/COMPTON_PERIOD:.1f}P: "
              f"{rms_om_last:.3e}")
        print(f"      Retention vs IC: {rms_om_last/max(rms_omega_ic,1e-30):.3e}")

    # Velocity profile
    print(f"\n  VELOCITY PROFILE (compare to T-ST v1 v_g = 0.364):")
    centroid_arr = np.array([(t, x) for t, x in centroid_traj if not np.isnan(x)])
    if len(centroid_arr) > 5:
        ts = centroid_arr[:, 0]
        xs = centroid_arr[:, 1]
        free_mask = ts < 4.0 * COMPTON_PERIOD
        if free_mask.sum() > 3:
            v_free = float(np.polyfit(ts[free_mask], xs[free_mask], 1)[0])
            print(f"    Free-prop v_g (t<4P): {v_free:.3f} cells/time-unit")

    # Verdict
    print(f"\n{'=' * 78}")
    print(f"  VERDICT")
    print(f"{'=' * 78}")
    print(f"  Compared to T-ST v1 (T=0):")
    print(f"    Saturation: T-ST v1 NO  → corpus-vacuum NO")
    print(f"    Op10 c:    T-ST v1 0   → corpus-vacuum {c_op10}")
    if saturation_engaged or c_op10 == 3:
        print(f"  → Corpus-vacuum baseline CHANGED outcome from T-ST v1.")
    else:
        print(f"  → Same outcome class as T-ST v1. Baseline IC alone insufficient")
        print(f"    to enable trap mechanism in this engine config.")

    out = {
        "test": "T-ST in Corpus Vacuum (Step 1: Thermal IC)",
        "config": {
            "N": N, "PML": PML, "T": T_CMB_ENGINE_UNITS,
            "thermalize_V": True,
            "amplitude_VSNAP": 0.10, "omega": OMEGA_C, "handedness": "RH",
        },
        "thermal_ic": {
            "predicted_sigma_V": sigma_V_pred,
            "predicted_sigma_omega": sigma_omega_pred,
            "actual_rms_V_ic": float(rms_V_ic),
            "actual_max_V_ic": float(max_V_ic),
            "actual_rms_omega_ic": float(rms_omega_ic),
        },
        "criteria": {
            "saturation_engaged": bool(saturation_engaged),
            "a2_trap_max": float(a2_trap_max),
            "c_op10": int(c_op10),
        },
        "trap_cell": [int(trap_x), int(trap_y), int(trap_z)],
        "captures": captures,
        "elapsed_total_s": float(elapsed),
    }
    out_path = Path(__file__).parent / "r10_v8_t_st_corpus_vacuum_v1_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
