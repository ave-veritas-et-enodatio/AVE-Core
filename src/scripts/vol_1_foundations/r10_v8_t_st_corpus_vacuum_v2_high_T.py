"""
T-ST in Corpus Vacuum (Step 2-revised) — V_yield-threshold T regime.

Per auditor 2026-04-30 Flag 3: three physically-distinct high-T regimes
exist. T=1e-6 is the V_yield-fluctuation-threshold regime where typical
σ_V ≈ V_yield → saturation engages STOCHASTICALLY at rare-fluctuation
crossings. Cleanest test of "spontaneous formation from rare
fluctuations" mechanism, distinct from T=5.8e-5 (chronic saturation
everywhere) and T=5.8e-4 (rupture).

Per Vol 1 Ch 8:218 corpus: α runs with thermal energy; high-T regimes
manifest extreme effects. Rule 16 question: at what T does corpus
electron form? T=1e-6 is the corpus-physics-cleanest first test.

== Pre-registered observables (per Rule 10 + A39 v2 dual-criterion) ==

PRIMARY (binary):
  (1) Does ANY cell engage saturation (A² > √(2α) = 0.121) during run?
      H1: yes — fluctuations cross V_yield stochastically → saturation
          engages locally → trap formation possible
      H0: no — even at V_yield-threshold T, no cell sustains saturation
  (2) Op10 c at end: does any topological winding form?

SECONDARY:
  (3) RMS V baseline persistence (compare to Step 1's 65% retention)
  (4) Spatial distribution of saturation-engaged cells
  (5) Lifetime of any saturation-engaged region
  (6) Interaction with photon source — does propagating photon at ω_C
      preferentially trap at fluctuation-driven gradient pockets?

== A47 arithmetic at T=1e-6 ==

σ_V_per_port = √(4π · 1e-6 / α) · V_SNAP = √(4π·1e-6·137) · V_SNAP
             = 0.0415 V_SNAP
σ_V_RMS_4port = 2 × 0.0415 = 0.083 V_SNAP ≈ V_yield (0.0854)

A²_per_cell = (V_inc)²/V_SNAP² summed over 4 ports
At RMS regime: A²_RMS ≈ 0.0069 ~ 0.06·A²_op14 (below threshold)
But fluctuations of ~1.3×σ_RMS exceed V_yield; ~5% of cells at any
moment have local A² > A²_op14 → saturation engages stochastically.

T < α/(4π) ≈ 5.8e-4 stability: T=1e-6 / 5.8e-4 = 1.7e-3 (well within stable).

== Configuration (matches T-ST v1 except T) ==

- N=48, PML=4
- Cosserat ON, A28-corrected
- temperature = 1e-6, thermalize_V = True
- Source: SpatialDipoleCPSource RH @ x0=8, ω=ω_C, A=0.10·V_SNAP, σ=4.0
  (same source as T-ST v1 to test "thermal baseline + photon together")
- Run: 50 Compton periods
- Diagnostic: track saturation-engaged cells over time

== Compute estimate ==

Same as T-ST v1: ~3 min wall clock.
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


from ave.core.constants import ALPHA
V_YIELD = float(np.sqrt(ALPHA))
A2_OP14 = float(np.sqrt(2.0 * ALPHA))
OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi
DT = 1.0 / np.sqrt(2.0)

T_HIGH = 1e-6   # V_yield-threshold regime (auditor Flag 3)


def setup_engine(N=48, PML=4, T=T_HIGH):
    engine = VacuumEngine3D.from_args(
        N=N, pml=PML, temperature=T,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )
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


def saturation_stats(V_inc, mask_active, pml):
    """Count cells engaged in saturation (A² > √(2α)) and report stats."""
    N = V_inc.shape[0]
    a2 = np.sum(V_inc ** 2, axis=-1)  # / V_SNAP² but V_SNAP=1
    a2_int = a2.copy()
    a2_int[~mask_active] = 0.0
    a2_int[:pml, :, :] = 0.0
    a2_int[N - pml:, :, :] = 0.0
    a2_int[:, :pml, :] = 0.0
    a2_int[:, N - pml:, :] = 0.0
    a2_int[:, :, :pml] = 0.0
    a2_int[:, :, N - pml:] = 0.0

    saturated = a2_int > A2_OP14
    n_saturated = int(np.sum(saturated))
    interior_total = int(np.sum(mask_active.astype(int))
                         - 6 * (N**2 * pml))   # approx interior count
    frac_saturated = n_saturated / max(interior_total, 1)

    a2_rms = float(np.sqrt(np.mean(a2_int[a2_int > 0])))
    a2_max = float(a2_int.max())

    return {
        "n_saturated_cells": n_saturated,
        "frac_saturated": frac_saturated,
        "a2_rms": a2_rms,
        "a2_max": a2_max,
    }


def main():
    print("=" * 78, flush=True)
    print("  T-ST V_yield-Threshold Regime (T=1e-6) — Auditor Flag 3 first run")
    print(f"  T = {T_HIGH:.1e}, σ_V_RMS predicted ≈ V_yield ({V_YIELD:.3f})")
    print("=" * 78, flush=True)

    N = 48
    PML = 4
    n_periods = 50
    n_steps = int(n_periods * COMPTON_PERIOD / DT)

    sigma_V_per_port = float(np.sqrt(4.0 * np.pi * T_HIGH / ALPHA))
    sigma_V_rms_4port = 2.0 * sigma_V_per_port
    print(f"\n  σ_V per port = {sigma_V_per_port:.4f} V_SNAP")
    print(f"  σ_V RMS (4-port) = {sigma_V_rms_4port:.4f} V_SNAP")
    print(f"  V_yield = {V_YIELD:.4f} V_SNAP")
    print(f"  A²_op14 (saturation onset) = {A2_OP14:.4f}")

    t_start = time.time()
    engine = setup_engine(N=N, PML=PML, T=T_HIGH)

    yc, zc = N // 2, N // 2
    init_stats = saturation_stats(engine.k4.V_inc, engine.k4.mask_active, PML)
    print(f"\n  Initial thermal IC saturation stats:")
    print(f"    Cells in saturation (A² > {A2_OP14:.3f}): "
          f"{init_stats['n_saturated_cells']}")
    print(f"    Fraction saturated: {init_stats['frac_saturated']:.4f}")
    print(f"    A²_RMS (interior, where active): {init_stats['a2_rms']:.4f}")
    print(f"    A²_max (interior): {init_stats['a2_max']:.4f}")

    source = setup_source()
    engine.add_source(source)

    sat_traj = []      # (t, n_sat, frac_sat, a2_max, a2_rms)
    a2_max_loc_traj = []

    capture_cadence = 5
    print(f"\n  Running...", flush=True)

    for step_i in range(n_steps):
        engine.step()

        if step_i % capture_cadence == 0:
            t_now = step_i * DT
            stats = saturation_stats(engine.k4.V_inc, engine.k4.mask_active, PML)

            a2_field = compute_a2_field(engine.k4.V_inc, V_SNAP=engine.V_SNAP)
            a2_int = mask_interior(a2_field, engine.k4.mask_active, PML)
            a2_max_idx = np.unravel_index(int(np.argmax(a2_int)), a2_int.shape)

            sat_traj.append({
                "t": float(t_now),
                "n_saturated": stats["n_saturated_cells"],
                "frac_saturated": stats["frac_saturated"],
                "a2_max": stats["a2_max"],
                "a2_rms": stats["a2_rms"],
                "max_loc": [int(v) for v in a2_max_idx],
            })

            if step_i % (capture_cadence * 10) == 0:
                t_p = t_now / COMPTON_PERIOD
                print(f"    t={t_p:5.2f}P  n_sat={stats['n_saturated_cells']:>5}  "
                      f"frac_sat={stats['frac_saturated']:.4f}  "
                      f"A²_max={stats['a2_max']:.4f}  A²_rms={stats['a2_rms']:.4f}  "
                      f"({time.time() - t_start:.0f}s)")

    elapsed = time.time() - t_start
    print(f"\n  Engine evolution complete in {elapsed:.0f}s")

    # ============================================================
    # Adjudication
    # ============================================================
    print("\n" + "=" * 78)
    print("  ADJUDICATION")
    print("=" * 78)

    # Primary criterion (1): did saturation engage at any cell?
    max_n_sat = max(s["n_saturated"] for s in sat_traj)
    max_frac_sat = max(s["frac_saturated"] for s in sat_traj)
    saturation_ever = max_n_sat > 0
    print(f"\n  PRIMARY (1) — Saturation engagement at ANY cell during run:")
    print(f"    Max simultaneously-saturated cells: {max_n_sat}")
    print(f"    Max fraction saturated: {max_frac_sat:.4f}")
    print(f"    Saturation engaged: {'YES' if saturation_ever else 'NO'}")

    # Primary (2): Op10
    try:
        c_op10 = int(engine.cos.extract_crossing_count())
    except Exception as exc:
        c_op10 = -1
    topology_match = (c_op10 == 3)
    print(f"\n  PRIMARY (2) — Op10 c at end:")
    print(f"    extract_crossing_count = {c_op10}")
    print(f"    Topology match (c=3): {'PASS' if topology_match else 'FAIL'}")

    # Secondary: time-history of saturation
    print(f"\n  SECONDARY — Saturation-engagement time history:")
    if sat_traj:
        sat_active_times = [s for s in sat_traj if s["n_saturated"] > 0]
        if sat_active_times:
            print(f"    Times with saturation active: "
                  f"{len(sat_active_times)}/{len(sat_traj)} captures")
            t_first_sat = sat_active_times[0]["t"] / COMPTON_PERIOD
            t_last_sat = sat_active_times[-1]["t"] / COMPTON_PERIOD
            print(f"    First saturation at t={t_first_sat:.2f}P, "
                  f"last at t={t_last_sat:.2f}P")
        else:
            print(f"    No saturation engaged at ANY capture across {len(sat_traj)} captures")

    # Verdict
    print(f"\n{'=' * 78}")
    print(f"  VERDICT (per pre-registered criteria)")
    print(f"{'=' * 78}")
    h_pass = saturation_ever and topology_match
    if h_pass:
        print(f"  → BOTH primary criteria pass: spontaneous formation engaged.")
    elif saturation_ever and not topology_match:
        print(f"  → Saturation engaged stochastically but no (2,3) topology formed.")
        print(f"    Mode II/III: characterize-as-itself — what shape do the")
        print(f"    saturated cells take? Random pockets, propagating wakes,")
        print(f"    standing waves at non-(2,3) topology?")
    elif not saturation_ever and topology_match:
        print(f"  → Topology without saturation — anomalous, investigate.")
    else:
        print(f"  → Same outcome class as T_CMB: thermal regime alone insufficient")
        print(f"    to drive saturation in 50P window. May need higher T")
        print(f"    (T=5.8e-5 chronic saturation regime) for follow-up.")

    out = {
        "test": "T-ST V_yield-threshold regime (T=1e-6)",
        "config": {
            "N": N, "PML": PML, "T": T_HIGH,
            "thermalize_V": True,
            "amplitude_VSNAP": 0.10, "omega": OMEGA_C, "handedness": "RH",
        },
        "thermal_ic_arithmetic": {
            "sigma_V_per_port_pred": sigma_V_per_port,
            "sigma_V_RMS_4port_pred": sigma_V_rms_4port,
            "v_yield": V_YIELD,
            "ratio_sigma_v_RMS_to_v_yield": sigma_V_rms_4port / V_YIELD,
        },
        "primary_criteria": {
            "saturation_engaged_anywhere": bool(saturation_ever),
            "max_n_saturated_cells": int(max_n_sat),
            "max_frac_saturated": float(max_frac_sat),
            "c_op10": int(c_op10),
            "topology_match": bool(topology_match),
        },
        "saturation_trajectory": sat_traj,
        "elapsed_total_s": float(elapsed),
    }
    out_path = Path(__file__).parent / "r10_v8_t_st_corpus_vacuum_v2_high_T_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
