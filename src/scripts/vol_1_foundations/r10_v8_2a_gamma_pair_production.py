"""
2.A — Gamma-Photon Pair Production Test.

Per [doc 30 §4.3](research/L3_electron_soliton/30_photon_identification.md):
"A single gamma photon at frequency 2·ω_C (energy 2m_ec²) can trigger
saturation at two distinct lattice regions simultaneously, creating
two TIR bubbles. The photon's transverse field pattern splits across
the two bubbles with opposite chirality, producing an electron/positron
pair."

Per Rule 14 axiom-canonical formation test:
- Ax 1: K4 LC lattice; bond LC at ω_C, photon at 2·ω_C
- Ax 2: pair carries opposite winding → ΔQ_topological = 0
- Ax 3: ℏ·2ω_C = 2·m_e c² (one gamma → e⁻ + e⁺); Noether
- Ax 4: triggered at two regions → two Γ→-1 TIR walls

Vol 1 Ch 7:53 — pair production = Regime III (yield) manifestation.

== Pre-registered observables (per A39 v2 dual-criterion) ==

PRIMARY:
  (1) Saturation engagement at TWO spatially separated regions
  (2) Op10 c at end: target c=3 (single (2,3)) OR signature of two
      paired (2,3) configurations of opposite chirality

SECONDARY:
  (3) Energy localization at TWO sites post-pulse decay
  (4) Frequency at trap sites: should be ω_C (electron rest frequency),
      NOT 2·ω_C (driver frequency) — confirms pair forms at half-driver
  (5) Spatial separation between trap sites
  (6) Symmetry: electron/positron pair should be mirror-symmetric

== Configuration ==

- N=48, PML=4
- Cosserat ON, A28-corrected
- temperature = 0 (deterministic, focus on driven mechanism)
- Source: SpatialDipoleCPSource at ω = 2·ω_C = 2.0
    x0 = 8, propagation +x, RH
    amplitude = 0.5 V_SNAP (5.9× V_yield, sufficient for Regime III)
    sigma_yz = 2.0 (tight focus to maintain peak per cell)
    envelope: 2P ramp + 2P sustain + 2P decay
- Run: 50 Compton periods

== A47 arithmetic ==

V_yield = √α ≈ 0.0854 V_SNAP
Source amp 0.5 V_SNAP = 5.86·V_yield (above threshold)
At source plane peak per cell: amp · σ · exp(-1/2) ≈ 0.5·2·0.61 = 0.61 V_SNAP
A²_peak_at_source ≈ 4·(0.61/2)² ≈ 0.37 — Regime II, near III boundary (0.75)
After propagation/dispersion: peak likely lower (T-ST v2 saw factor ~6 reduction)

== Compute estimate ==

~3 min wall clock at N=48.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path
from collections import Counter
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
from ave.topological.vacuum_engine import VacuumEngine3D, SpatialDipoleCPSource


ALPHA = 1.0 / 137.035999
V_YIELD = float(np.sqrt(ALPHA))
A2_OP14 = float(np.sqrt(2.0 * ALPHA))
OMEGA_C = 1.0
OMEGA_GAMMA = 2.0  # gamma photon = 2·ω_C
COMPTON_PERIOD = 2.0 * np.pi
DT = 1.0 / np.sqrt(2.0)


def find_two_peaks(a2_field, mask_active, pml, separation_min=4):
    """Find top-2 spatially-separated A² peaks (PML excluded)."""
    N = a2_field.shape[0]
    a2_int = a2_field * mask_active.astype(float)
    a2_int[:pml, :, :] = 0; a2_int[N-pml:, :, :] = 0
    a2_int[:, :pml, :] = 0; a2_int[:, N-pml:, :] = 0
    a2_int[:, :, :pml] = 0; a2_int[:, :, N-pml:] = 0

    flat = a2_int.flatten()
    sorted_idx = np.argsort(flat)[::-1]
    peak1 = np.unravel_index(sorted_idx[0], a2_int.shape)

    # Find second peak at least separation_min cells from first
    peak2 = None
    for si in sorted_idx[1:200]:
        cand = np.unravel_index(si, a2_int.shape)
        d = np.sqrt(sum((p1 - p2)**2 for p1, p2 in zip(peak1, cand)))
        if d >= separation_min:
            peak2 = cand
            break

    return peak1, peak2, float(a2_int[peak1]), float(a2_int[peak2]) if peak2 else 0.0


def main():
    print("=" * 78, flush=True)
    print("  2.A — Gamma-Photon Pair Production Test (doc 30 §4.3)")
    print("  ω_drive = 2·ω_C = 2.0, A = 0.5 V_SNAP")
    print("=" * 78, flush=True)

    N, PML = 48, 4
    n_steps = int(50 * COMPTON_PERIOD / DT)

    print(f"\n  Lattice: N={N}, PML={PML}")
    print(f"  V_yield={V_YIELD:.4f}, A²_op14={A2_OP14:.4f}")

    t_start = time.time()
    engine = VacuumEngine3D.from_args(
        N=N, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )

    source = SpatialDipoleCPSource(
        x0=8, propagation_axis=0, amplitude=0.5, omega=OMEGA_GAMMA,
        handedness="RH", sigma_yz=2.0,
        t_ramp=2.0 * COMPTON_PERIOD, t_sustain=2.0 * COMPTON_PERIOD,
        t_decay=2.0 * COMPTON_PERIOD,
    )
    engine.add_source(source)

    print(f"  Source: SpatialDipoleCPSource ω=2·ω_C, A=0.5 V_SNAP, σ=2.0\n")

    # Captures
    yc, zc = N // 2, N // 2
    axial_v_inc = np.zeros((n_steps, N, 4))
    sat_traj = []
    peak_loc_traj = []

    capture_cadence = 5
    print(f"  Running...", flush=True)

    for step_i in range(n_steps):
        engine.step()
        axial_v_inc[step_i] = engine.k4.V_inc[:, yc, zc, :]

        if step_i % capture_cadence == 0:
            t_now = step_i * DT
            a2 = np.sum(engine.k4.V_inc ** 2, axis=-1)
            mask = engine.k4.mask_active

            peak1, peak2, a2_p1, a2_p2 = find_two_peaks(a2, mask, PML)
            n_sat = int(np.sum((a2 * mask.astype(float)
                                * (np.indices(a2.shape)[0] >= PML)
                                * (np.indices(a2.shape)[0] < N-PML)
                                * (np.indices(a2.shape)[1] >= PML)
                                * (np.indices(a2.shape)[1] < N-PML)
                                * (np.indices(a2.shape)[2] >= PML)
                                * (np.indices(a2.shape)[2] < N-PML)
                               ) > A2_OP14))

            sat_traj.append({
                "t": float(t_now), "n_sat": n_sat,
                "peak1": [int(v) for v in peak1], "a2_peak1": a2_p1,
                "peak2": [int(v) for v in peak2] if peak2 else None,
                "a2_peak2": a2_p2,
            })
            peak_loc_traj.append((peak1, peak2))

            if step_i % 50 == 0:
                t_p = t_now / COMPTON_PERIOD
                p2_str = f"{peak2}" if peak2 else "—"
                print(f"    t={t_p:5.2f}P  n_sat={n_sat:>4}  "
                      f"peak1={peak1} A²={a2_p1:.3f}  "
                      f"peak2={p2_str} A²={a2_p2:.3f}  "
                      f"({time.time() - t_start:.0f}s)", flush=True)

    elapsed = time.time() - t_start
    print(f"\n  Engine evolution complete in {elapsed:.0f}s")

    # Adjudication
    print("\n  ADJUDICATION (per pre-registered criteria)")
    print("=" * 78)

    # Did saturation engage at 2 separate sites at any time?
    paired_engagement = [s for s in sat_traj
                         if s["peak2"] is not None
                         and s["a2_peak1"] > A2_OP14
                         and s["a2_peak2"] > A2_OP14]
    print(f"\n  PRIMARY (1) — Two-region saturation engagement:")
    print(f"    Captures with both peaks above A²_op14: "
          f"{len(paired_engagement)}/{len(sat_traj)}")
    if paired_engagement:
        first_pair = paired_engagement[0]
        print(f"    First two-region engagement at t={first_pair['t']/COMPTON_PERIOD:.2f}P")
        print(f"    Peak1={first_pair['peak1']} A²={first_pair['a2_peak1']:.3f}")
        print(f"    Peak2={first_pair['peak2']} A²={first_pair['a2_peak2']:.3f}")
        sep = np.sqrt(sum((p1 - p2)**2 for p1, p2 in
                          zip(first_pair['peak1'], first_pair['peak2'])))
        print(f"    Separation: {sep:.2f} cells")

    # Op10 at end
    try:
        c_op10 = int(engine.cos.extract_crossing_count())
    except Exception:
        c_op10 = -1
    print(f"\n  PRIMARY (2) — Op10 c at end: {c_op10}")

    # Persistent post-pulse engagement
    second_half = [s for s in sat_traj if s["t"] > 6.0 * COMPTON_PERIOD]
    persistent = [s for s in second_half if s["a2_peak1"] > A2_OP14]
    print(f"\n  Post-pulse persistence: {len(persistent)}/{len(second_half)} "
          f"captures with peak1 > A²_op14")

    # Verdict
    h_pass = len(paired_engagement) > 0 and (c_op10 == 3 or c_op10 == 6)
    # c=6 might indicate two paired (2,3) of opposite chirality
    print(f"\n  Pair-production candidate (saturation@2 sites + topology): "
          f"{'PASS' if h_pass else 'FAIL'}")

    out = {
        "test": "2.A: Gamma-photon pair production",
        "config": {"N": N, "PML": PML, "omega": OMEGA_GAMMA,
                   "amplitude": 0.5, "sigma_yz": 2.0},
        "primary": {
            "two_region_engagement_captures": len(paired_engagement),
            "first_pair_time_P": (paired_engagement[0]["t"]/COMPTON_PERIOD
                                   if paired_engagement else None),
            "c_op10": int(c_op10),
        },
        "saturation_trajectory_summary": [
            {"t": s["t"], "n_sat": s["n_sat"],
             "peak1": s["peak1"], "a2_peak1": s["a2_peak1"],
             "peak2": s["peak2"], "a2_peak2": s["a2_peak2"]}
            for s in sat_traj
        ],
        "elapsed_total_s": float(elapsed),
    }
    out_path = Path(__file__).parent / "r10_v8_2a_gamma_pair_production_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
