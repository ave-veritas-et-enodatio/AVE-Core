"""Test B v2 — multi-spatial-point phasor envelope on single A-B bond.

Per `P_phase5_bond_scale_phasor_v2_multipoint` (frozen at this commit) +
audit catch on commit 53c2ce9 + doc 26_ §1-§3 careful re-read:

    ψ(s, t) = V_0 · A(s) · exp(i (ωt + θ(s)))

The (2, 3) electron topology lives in θ(s) — the spatial phase profile
along the bond. Doc 26_ §3 defines the phase-space torus dimensions as:

    R_phase = ⟨A(s)⟩_s  (spatial mean of envelope)
    r_phase = √(⟨A²⟩_s − ⟨A⟩_s²)  (spatial std of envelope)

These are SPATIAL averages over s, not temporal at one s. At fixed s,
(V_inc, V_ref) traces a CIRCLE — single frequency, no torus structure.
Test B v1 + retry sampled one (cell, port) → one circle → R/r = 19
is amp-invariant (linear-regime ellipse aspect).

Test B v2 samples 8 spatial points spanning the local A-B bond cluster:
  - 4 ports of A = (14, 14, 14)
  - 4 ports of B = (15, 15, 15)

At each spatial point, the time-averaged amplitude
  ρ_i = √(⟨V_inc²⟩_t + ⟨V_ref²⟩_t)
gives one A(s_i) sample. Spatial mean/std over the 8 samples gives
the corpus phase-space R, r per doc 26_ §3.

Three-mode adjudication:
  Mode I-spatial:    R_spatial / r_spatial = φ² ± 0.10
                     (corpus Golden Torus on bond — doc 28_ §5.1 vindicated)
  Mode II-spatial:   R_spatial / r_spatial ≠ φ² ± 0.10 AND r_spatial / R_spatial > 0.05
                     (spatial amplitude variation present, but wrong ratio)
  Mode III-spatial:  r_spatial / R_spatial ≤ 0.05  (essentially uniform envelope)
                     (drive is spatially uniform across bond cluster — no
                      spatial structure to extract; bond doesn't host
                      (2, 3) winding at this drive)
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.vacuum_engine import VacuumEngine3D, AutoresonantCWSource

# ─── Constants per pred ───────────────────────────────────────────────────────

PHI = 0.5 * (1.0 + np.sqrt(5.0))
PHI_SQ = PHI * PHI

N_LATTICE = 32
PML = 4
OMEGA_C = 1.0
WAVELENGTH_CARRIER = 2.0 * np.pi / OMEGA_C  # ≈ 6.28 cells

# Match v1-retry drive amplitude for direct comparison; saturation-onset regime
DRIVE_AMP = 0.5

T_RAMP_PERIODS = 5.0
T_SUSTAIN_PERIODS = 50.0
T_DECAY_PERIODS = 2.0

# Spatial-phasor adjudication
R_OVER_R_TARGET = PHI_SQ
R_OVER_R_TOL = 0.10
SPATIAL_UNIFORM_THRESH = 0.05  # r/R below this ⇒ Mode III-spatial

PORT_VECTORS = np.array([
    [+1, +1, +1],
    [+1, -1, -1],
    [-1, +1, -1],
    [-1, -1, +1],
], dtype=float)

OUTPUT_JSON = Path(__file__).parent / "test_b_v2_multipoint_phasor_results.json"


def find_central_bond(engine):
    """Find an A-B bond at lattice center (mirrors v1 driver)."""
    nx = engine.k4.nx
    cx = nx // 2
    for di in range(-2, 3):
        for dj in range(-2, 3):
            for dk in range(-2, 3):
                i, j, k = cx + di, cx + dj, cx + dk
                if not (0 < i < nx - 1 and 0 < j < nx - 1 and 0 < k < nx - 1):
                    continue
                if not engine.k4.mask_A[i, j, k]:
                    continue
                for port in range(4):
                    p = PORT_VECTORS[port].astype(int)
                    ib, jb, kb = i + p[0], j + p[1], k + p[2]
                    if not (0 <= ib < nx and 0 <= jb < nx and 0 <= kb < nx):
                        continue
                    if engine.k4.mask_B[ib, jb, kb]:
                        return (i, j, k), port, (ib, jb, kb)
    raise RuntimeError("No viable A-B bond found near center")


def extract_multipoint_phasor(engine, A_idx, B_idx, n_steps, transient_steps):
    """Drive simulation; record V_inc, V_ref at all 4 ports of A and B.

    Returns:
        v_inc_traj: shape (n_steps, 8) — 4 A-ports + 4 B-ports
        v_ref_traj: shape (n_steps, 8)
        port_labels: list of (cell_label, port_idx) for each spatial sample
    """
    v_inc_all = np.zeros((n_steps, 8), dtype=np.float64)
    v_ref_all = np.zeros((n_steps, 8), dtype=np.float64)
    port_labels = (
        [("A", p) for p in range(4)] + [("B", p) for p in range(4)]
    )

    for step in range(n_steps):
        engine.step()
        # A-side: 4 ports
        for p in range(4):
            v_inc_all[step, p] = float(
                engine.k4.V_inc[A_idx[0], A_idx[1], A_idx[2], p]
            )
            v_ref_all[step, p] = float(
                engine.k4.V_ref[A_idx[0], A_idx[1], A_idx[2], p]
            )
        # B-side: 4 ports (offset by 4 in the array)
        for p in range(4):
            v_inc_all[step, 4 + p] = float(
                engine.k4.V_inc[B_idx[0], B_idx[1], B_idx[2], p]
            )
            v_ref_all[step, 4 + p] = float(
                engine.k4.V_ref[B_idx[0], B_idx[1], B_idx[2], p]
            )

    return v_inc_all, v_ref_all, port_labels


def analyze_spatial_envelope(v_inc_all, v_ref_all, transient_steps):
    """Compute per-port time-averaged amplitude and spatial statistics.

    For each of 8 spatial samples i:
        ρ_i = √(⟨V_inc[i]²⟩_t + ⟨V_ref[i]²⟩_t)
    Spatial:
        R_spatial = mean(ρ) over 8 samples
        r_spatial = std(ρ) over 8 samples
        R/r = ratio for corpus-φ² test
    """
    v_inc_steady = v_inc_all[transient_steps:]
    v_ref_steady = v_ref_all[transient_steps:]

    # Per-port time-averaged amplitude
    rho_per_port = np.sqrt(
        (v_inc_steady ** 2).mean(axis=0) + (v_ref_steady ** 2).mean(axis=0)
    )
    # rho_per_port has shape (8,)

    R_spatial = float(np.mean(rho_per_port))
    r_spatial = float(np.std(rho_per_port))
    R_over_r_spatial = R_spatial / max(r_spatial, 1e-30)

    # Spatial uniformity diagnostic
    rel_std = r_spatial / max(R_spatial, 1e-30)
    spatially_uniform = rel_std < SPATIAL_UNIFORM_THRESH

    # Per-port time-averaged (V_inc, V_ref) means — gives spatial 2D envelope
    v_inc_envelope = v_inc_steady.mean(axis=0)
    v_ref_envelope = v_ref_steady.mean(axis=0)

    return {
        "rho_per_port": rho_per_port.tolist(),
        "v_inc_envelope": v_inc_envelope.tolist(),
        "v_ref_envelope": v_ref_envelope.tolist(),
        "R_spatial": R_spatial,
        "r_spatial": r_spatial,
        "R_over_r_spatial": R_over_r_spatial,
        "rel_std": float(rel_std),
        "spatially_uniform": bool(spatially_uniform),
    }


def main():
    print("=" * 78, flush=True)
    print(f"  Test B v2 — multi-spatial-point bond phasor envelope")
    print(f"  P_phase5_bond_scale_phasor_v2_multipoint")
    print(f"  Per audit catch on commit 53c2ce9 + doc 26_ §1-§3 spatial reading")
    print("=" * 78, flush=True)
    print(f"  Lattice: N={N_LATTICE}, pml={PML}")
    print(f"  Drive: ω_C = {OMEGA_C}, λ = {WAVELENGTH_CARRIER:.4f} cells, "
          f"amp = {DRIVE_AMP}·V_SNAP")
    print(f"  Periods: ramp {T_RAMP_PERIODS} + sustain {T_SUSTAIN_PERIODS} + "
          f"decay {T_DECAY_PERIODS}")
    print(f"  Spatial samples: 4 ports of A + 4 ports of B = 8 points")
    print(f"  Pred PASS: R_spatial/r_spatial = {R_OVER_R_TARGET:.4f} ± {R_OVER_R_TOL}")
    print()

    period = 2.0 * np.pi / OMEGA_C
    t_ramp = T_RAMP_PERIODS * period
    t_sustain = T_SUSTAIN_PERIODS * period
    t_decay = T_DECAY_PERIODS * period
    total_time = t_ramp + t_sustain + t_decay
    n_steps = int(total_time * np.sqrt(2.0)) + 1
    transient_steps = int((t_ramp + 10.0 * period) * np.sqrt(2.0))

    engine = VacuumEngine3D.from_args(
        N=N_LATTICE, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )
    A_idx, port_AB, B_idx = find_central_bond(engine)
    print(f"  Bond: A={A_idx}, port_AB={port_AB}, B={B_idx}")

    src_offset = PML + 3
    engine.add_source(AutoresonantCWSource(
        x0=src_offset, direction=(1.0, 0.0, 0.0),
        amplitude=DRIVE_AMP, omega=OMEGA_C,
        sigma_yz=3.0, t_ramp=t_ramp, t_sustain=t_sustain,
        t_decay=t_decay,
    ))

    print(f"  Running {n_steps} steps ({total_time:.2f} natural-time-units)...")
    t0 = time.time()
    v_inc_all, v_ref_all, port_labels = extract_multipoint_phasor(
        engine, A_idx, B_idx, n_steps, transient_steps,
    )
    elapsed = time.time() - t0
    print(f"  Elapsed: {elapsed:.1f}s, recorded {n_steps} samples × 8 ports")
    print()

    print(f"  Spatial envelope analysis (skip first {transient_steps} samples)...")
    analysis = analyze_spatial_envelope(v_inc_all, v_ref_all, transient_steps)

    print(f"  Per-port ρ_i = √(⟨V_inc²⟩ + ⟨V_ref²⟩):")
    for i, label in enumerate(port_labels):
        print(f"    {label[0]} port {label[1]}: ρ = {analysis['rho_per_port'][i]:.6f}")
    print()
    print(f"  R_spatial = ⟨ρ⟩ = {analysis['R_spatial']:.6f}")
    print(f"  r_spatial = std(ρ) = {analysis['r_spatial']:.6f}")
    print(f"  R/r spatial = {analysis['R_over_r_spatial']:.4f}")
    print(f"  rel_std r/R = {analysis['rel_std']:.6f} "
          f"(uniform threshold = {SPATIAL_UNIFORM_THRESH})")
    print()

    R_over_r_pass = abs(analysis['R_over_r_spatial'] - R_OVER_R_TARGET) <= R_OVER_R_TOL

    print("=" * 78, flush=True)
    print("  Adjudication")
    print("=" * 78, flush=True)
    if analysis['spatially_uniform']:
        mode = "III-spatial"
        verdict = (
            f"MODE III-spatial — Spatial envelope is essentially uniform "
            f"(rel_std r/R = {analysis['rel_std']:.4f} < "
            f"{SPATIAL_UNIFORM_THRESH}). The 8-port amplitude profile across "
            f"the A-B bond cluster has no spatial structure: ⟨ρ⟩ ≈ ρ at every "
            f"port, so A(s) is flat and θ(s) winding cannot be extracted. "
            f"At this drive the bond cluster doesn't develop the spatial "
            f"phase profile that doc 26_ §1 requires for (2,3) winding."
        )
    elif R_over_r_pass:
        mode = "I-spatial"
        verdict = (
            f"MODE I-spatial — Spatial R/r = "
            f"{analysis['R_over_r_spatial']:.4f} matches corpus φ² = "
            f"{R_OVER_R_TARGET:.4f} within ±{R_OVER_R_TOL}. **Doc 28_ §5.1 "
            f"two-node-electron hypothesis vindicated** at the bond cluster: "
            f"the spatial envelope across the 8 ports of A and B traces the "
            f"corpus phase-space Golden Torus."
        )
    else:
        mode = "II-spatial"
        verdict = (
            f"MODE II-spatial — Spatial envelope has structure (rel_std r/R "
            f"= {analysis['rel_std']:.4f} ≥ {SPATIAL_UNIFORM_THRESH}) but "
            f"R/r = {analysis['R_over_r_spatial']:.4f} ≠ corpus φ² = "
            f"{R_OVER_R_TARGET:.4f} (off by "
            f"{abs(analysis['R_over_r_spatial'] - R_OVER_R_TARGET):.4f}, "
            f"tolerance {R_OVER_R_TOL}). Bond cluster has SPATIAL amplitude "
            f"variation but not the corpus Golden Torus ratio. Could "
            f"indicate different attractor at this drive, OR drive amp/freq "
            f"mismatch from corpus electron config."
        )
    print(f"  {verdict}")
    print()

    payload = {
        "pre_registration": "P_phase5_bond_scale_phasor_v2_multipoint",
        "test": "Test B v2 per audit + doc 26_ §1-§3 spatial reading",
        "N": N_LATTICE,
        "drive_amp": DRIVE_AMP,
        "drive_omega": OMEGA_C,
        "drive_periods": {
            "ramp": T_RAMP_PERIODS,
            "sustain": T_SUSTAIN_PERIODS,
            "decay": T_DECAY_PERIODS,
        },
        "n_samples": n_steps,
        "transient_steps_skipped": transient_steps,
        "elapsed_seconds": elapsed,
        "bond": {
            "A_idx": list(A_idx),
            "port_AB": port_AB,
            "B_idx": list(B_idx),
        },
        "n_spatial_samples": 8,
        "port_labels": [{"cell": l[0], "port": l[1]} for l in port_labels],
        "spatial_analysis": analysis,
        "R_over_r_target": R_OVER_R_TARGET,
        "R_over_r_tol": R_OVER_R_TOL,
        "spatial_uniform_thresh": SPATIAL_UNIFORM_THRESH,
        "R_over_r_spatial_pass": bool(R_over_r_pass),
        "mode": mode,
        "verdict": verdict,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()
