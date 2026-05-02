"""
O.1b — V_inc Topology Measurement on Shell Mode (Auditor Flag 2 follow-up).

Per auditor 2026-04-30 Flag 2: Op10 (cosserat extract_crossing_count)
reads Cosserat ω real-space winding. Doc 28 §3+§5.1 says the corpus
electron's (2,3) topology lives in (V_inc, V_ref) PHASE-SPACE on
Clifford torus, NOT Cosserat ω real-space. Op10 on Cosserat ω may be a
DIFFERENT topology measure than what corpus claims for the electron.

This driver re-runs O.1 with bond-level V_inc+V_ref captures, then
applies TWO V_inc-side topology measures:

  Measure A (doc 28 §5.1 phase-space): at sampled shell bond, extract
    (V_inc, V_ref) trajectory over time. If corpus-canonical electron,
    trajectory traces torus with R_phase/r_phase = φ² = 2.618.

  Measure B (V_inc spatial-winding analog of Op10): at final timestep,
    compute phase of V_inc[port=0] around toroidal contour in (x,y)
    plane at fixed z. Count winding number around major axis. If (2,3),
    should see 2 windings around major axis.

Per Flag 1 normalization caveat: amp=0.1 (down from 0.3 in O.1)
keeps all cells below rupture (A² < 1) — corpus-physical regime
throughout, no engine numerical-clamping.

== Pre-registered observables ==

PRIMARY (doc 28 §5.1 corpus-canonical):
  R_phase/r_phase aspect from PCA on (V_inc, V_ref) trajectory at a
  shell bond. Target: φ² = 2.618 ± 0.10 if corpus electron present.

SECONDARY (V_inc spatial winding):
  Winding number of V_inc[port=0] phase around toroidal contour at
  final timestep. Target: 2 (toroidal component of (2,3)).

TERTIARY:
  Energy retention (compare to O.1 amp=0.3: 41% retention)
  Shell localization (O.1 was 80% at end)
  Op10 c (will likely still be 0 since Cosserat ω = 0)

== Configuration ==

- N=48, PML=4
- Cosserat ON, A28-corrected
- temperature = 0
- IC: initialize_2_3_voltage_ansatz with R=8, r=4, **amp=0.1** (lower)
- 50 Compton periods
- Bond captures: 16 bonds around toroidal shell at psi=0 (varied phi)
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


PHI = (1.0 + np.sqrt(5.0)) / 2.0
PHI_SQ = PHI * PHI
COMPTON_PERIOD = 2.0 * np.pi
DT = 1.0 / np.sqrt(2.0)


def shell_bond_locations(N, R_torus, r_torus, n_bonds=16):
    """Return (n_bonds, 3) integer cell indices on the toroidal shell at psi=0."""
    cx = (N - 1) // 2
    cy = (N - 1) // 2
    cz = (N - 1) // 2
    phis = np.linspace(0, 2 * np.pi, n_bonds, endpoint=False)
    locs = []
    for phi in phis:
        x = int(round(cx + R_torus * np.cos(phi)))
        y = int(round(cy + R_torus * np.sin(phi)))
        z = cz
        # Clamp to valid range
        x = max(1, min(N - 2, x))
        y = max(1, min(N - 2, y))
        locs.append((x, y, z, phi))
    return locs


def phase_space_aspect(v_inc_traj, v_ref_traj):
    """Doc 28 §5.1: PCA aspect ratio of (V_inc, V_ref) trajectory.
    Returns R_phase/r_phase (target φ² = 2.618 if corpus electron)."""
    pts = np.stack([v_inc_traj, v_ref_traj], axis=1)
    pts = pts - pts.mean(axis=0, keepdims=True)
    cov = (pts.T @ pts) / max(len(pts) - 1, 1)
    evals, _ = np.linalg.eigh(cov)
    evals = np.sort(np.maximum(evals, 0.0))[::-1]
    if evals[1] > 1e-30:
        return float(np.sqrt(evals[0] / evals[1]))
    return float("inf")


def spatial_winding_v_inc(V_inc_field, R_torus, n_samples=64):
    """Compute winding of V_inc[port=0] phase around toroidal contour.
    Sample at z=cz (mid-plane), follow circle of radius R_torus in (x,y).
    Returns total accumulated phase divided by 2π."""
    N = V_inc_field.shape[0]
    cx, cy, cz = (N - 1) // 2, (N - 1) // 2, (N - 1) // 2
    phis = np.linspace(0, 2 * np.pi, n_samples, endpoint=False)

    # Sample V_inc on (port 0, port 2) — use as Re/Im of phasor
    # since cos goes on port 0, sin on port 2 per IC seeder
    vals_re = []
    vals_im = []
    for phi in phis:
        x = int(round(cx + R_torus * np.cos(phi)))
        y = int(round(cy + R_torus * np.sin(phi)))
        x = max(1, min(N - 2, x))
        y = max(1, min(N - 2, y))
        vals_re.append(V_inc_field[x, y, cz, 0])
        vals_im.append(V_inc_field[x, y, cz, 2])

    vals_re = np.array(vals_re)
    vals_im = np.array(vals_im)

    # Compute phase angle at each sample
    angles = np.arctan2(vals_im, vals_re)

    # Unwrap and count total winding
    unwrapped = np.unwrap(angles)
    total_phase_change = unwrapped[-1] - unwrapped[0]
    # Add wrap-around to close loop
    last_to_first = vals_re[0] * vals_re[-1] + vals_im[0] * vals_im[-1]
    closure = (np.arctan2(vals_im[0], vals_re[0])
               - np.arctan2(vals_im[-1], vals_re[-1]))
    closure_unwrapped = np.angle(np.exp(1j * closure))
    total_phase_change += closure_unwrapped

    winding = total_phase_change / (2.0 * np.pi)
    return float(winding), float(np.sqrt(np.mean(vals_re**2 + vals_im**2)))


def main():
    print("=" * 78, flush=True)
    print("  O.1b — V_inc Topology Measurement on Shell Mode")
    print("  Auditor Flag 2 follow-up: doc 28 §5.1 phase-space + V_inc spatial winding")
    print("=" * 78, flush=True)

    N, PML = 48, 4
    n_steps = int(50 * COMPTON_PERIOD / DT)
    R_torus = 8.0
    r_torus = 4.0
    amp_ic = 0.1   # Down from O.1's 0.3 per Flag 1 (corpus-physical bulk)
    n_bonds = 16

    print(f"\n  Lattice: N={N}, PML={PML}")
    print(f"  IC: (2,3) torus-knot, R={R_torus}, r={r_torus}, amp={amp_ic} (corpus-physical bulk per Flag 1)")
    print(f"  Bond captures: {n_bonds} shell bonds at psi=0")

    t_start = time.time()
    engine = VacuumEngine3D.from_args(
        N=N, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )

    initialize_2_3_voltage_ansatz(
        engine.k4, R=R_torus, r=r_torus, amplitude=amp_ic,
    )

    # IC verification
    init_a2 = np.sum(engine.k4.V_inc ** 2, axis=-1)
    init_a2_int = init_a2 * engine.k4.mask_active.astype(float)
    init_a2_int[:PML, :, :] = 0; init_a2_int[N-PML:, :, :] = 0
    init_a2_int[:, :PML, :] = 0; init_a2_int[:, N-PML:, :] = 0
    init_a2_int[:, :, :PML] = 0; init_a2_int[:, :, N-PML:] = 0
    print(f"\n  IC verification:")
    print(f"    A²_max(t=0): {init_a2_int.max():.4f}")
    print(f"    Total energy(t=0): {init_a2_int.sum():.4f}")
    print(f"    A²_max < 1.0 (corpus-physical): {'YES' if init_a2_int.max() < 1.0 else 'NO'}")

    # Set up bond capture locations
    bond_locs = shell_bond_locations(N, R_torus, r_torus, n_bonds=n_bonds)

    # Storage
    bond_v_inc = np.zeros((n_bonds, n_steps, 4))   # n_bonds × time × 4 ports
    bond_v_ref = np.zeros((n_bonds, n_steps, 4))

    energy_traj = []
    a2_max_traj = []

    capture_cadence = 5
    print(f"\n  Running...", flush=True)

    for step_i in range(n_steps):
        engine.step()

        # Per-step bond captures
        for bi, (x, y, z, _phi) in enumerate(bond_locs):
            bond_v_inc[bi, step_i] = engine.k4.V_inc[x, y, z, :]
            bond_v_ref[bi, step_i] = engine.k4.V_ref[x, y, z, :]

        if step_i % capture_cadence == 0:
            t_now = step_i * DT
            a2 = np.sum(engine.k4.V_inc ** 2, axis=-1)
            a2_int = a2 * engine.k4.mask_active.astype(float)
            a2_int[:PML, :, :] = 0; a2_int[N-PML:, :, :] = 0
            a2_int[:, :PML, :] = 0; a2_int[:, N-PML:, :] = 0
            a2_int[:, :, :PML] = 0; a2_int[:, :, N-PML:] = 0
            energy_traj.append((t_now, float(a2_int.sum())))
            a2_max_traj.append((t_now, float(a2_int.max())))

            if step_i % 50 == 0:
                t_p = t_now / COMPTON_PERIOD
                print(f"    t={t_p:5.2f}P  E={a2_int.sum():.3e}  "
                      f"A²_max={a2_int.max():.3f}  "
                      f"({time.time() - t_start:.0f}s)", flush=True)

    elapsed = time.time() - t_start
    print(f"\n  Engine evolution complete in {elapsed:.0f}s")

    # ============================================================
    # Topology Measures (Auditor Flag 2 resolution)
    # ============================================================
    print("\n  V_inc TOPOLOGY ANALYSIS")
    print("=" * 78)

    # MEASURE A: doc 28 §5.1 phase-space aspect at each shell bond
    # Use post-transient window (t > 11P) for steady-state analysis
    transient_steps = int(11.0 * COMPTON_PERIOD / DT)

    print(f"\n  MEASURE A — doc 28 §5.1 phase-space aspect at {n_bonds} shell bonds")
    print(f"  (PCA on (V_inc, V_ref) trajectory, post-transient t>11P window)")
    print(f"  Target: R_phase/r_phase ≈ φ² = {PHI_SQ:.3f} ± 0.10 if corpus electron")
    print()
    print(f"  {'phi':>8} {'(x,y,z)':>14} {'R/r per port':>40}")

    aspects_per_bond = []
    for bi, (x, y, z, phi) in enumerate(bond_locs):
        # PCA per port (port 0 chosen; could average over ports)
        aspects = []
        for port in range(4):
            v_inc_p = bond_v_inc[bi, transient_steps:, port]
            v_ref_p = bond_v_ref[bi, transient_steps:, port]
            aspect = phase_space_aspect(v_inc_p, v_ref_p)
            aspects.append(aspect)
        aspects_per_bond.append(aspects)
        # Print port-0 aspect with summary
        a_str = " ".join(f"{a:6.2f}" if not np.isinf(a) else "  inf" for a in aspects)
        print(f"  {phi:>8.3f} ({x:>2},{y:>2},{z:>2})  {a_str}")

    # Summary statistics across bonds (port 0)
    aspects_p0 = [a[0] for a in aspects_per_bond if not np.isinf(a[0])]
    if aspects_p0:
        mean_aspect = float(np.mean(aspects_p0))
        std_aspect = float(np.std(aspects_p0))
        print(f"\n  Port 0 aspect: mean = {mean_aspect:.3f}, std = {std_aspect:.3f}")
        print(f"  Compared to φ² = {PHI_SQ:.3f}: "
              f"|mean - φ²|/φ² = {abs(mean_aspect - PHI_SQ)/PHI_SQ * 100:.1f}%")
        phase_space_match = abs(mean_aspect - PHI_SQ) <= 0.10 * PHI_SQ
        print(f"  Phase-space match (R/r ≈ φ² ± 10%): "
              f"{'PASS' if phase_space_match else 'FAIL'}")
    else:
        phase_space_match = False
        mean_aspect = float("nan")

    # MEASURE B: V_inc spatial winding at final timestep
    print(f"\n  MEASURE B — V_inc[port=0,2] spatial winding around toroidal contour")
    print(f"  (final timestep, contour at z=N/2, radius R={R_torus})")
    winding, amp_rms = spatial_winding_v_inc(engine.k4.V_inc, R_torus, n_samples=64)
    print(f"  Winding number: {winding:.3f} (target: 2 if corpus (2,3) toroidal)")
    print(f"  Contour amplitude RMS: {amp_rms:.3e}")
    spatial_winding_match = abs(round(winding) - 2) == 0 and abs(winding - round(winding)) < 0.3
    print(f"  Spatial winding match (=2): {'PASS' if spatial_winding_match else 'FAIL'}")

    # Op10 (for completeness — expected 0)
    try:
        c_op10 = int(engine.cos.extract_crossing_count())
    except Exception:
        c_op10 = -1
    print(f"\n  Op10 (Cosserat ω) c = {c_op10} (expected 0 since IC seeded V_inc only)")

    # Energy retention
    e_first = energy_traj[0][1]
    e_last = energy_traj[-1][1]
    retention = e_last / max(e_first, 1e-30)
    print(f"\n  Energy retention over 50P: {retention:.3f} (O.1 amp=0.3 was 0.409)")

    # Verdict
    print(f"\n{'='*78}")
    print(f"  TOPOLOGY VERDICT")
    print(f"{'='*78}")
    if phase_space_match and spatial_winding_match:
        print(f"  → Corpus-canonical (2,3) electron topology DETECTED in V_inc")
        print(f"    Phase-space: R/r ≈ φ² (doc 28 §5.1 PASS)")
        print(f"    Spatial winding: 2 around major axis (toroidal component PASS)")
    elif phase_space_match:
        print(f"  → Phase-space (2,3) detected; spatial winding inconsistent")
        print(f"    Investigate: R/r ≈ φ² but winding = {winding:.2f}")
    elif spatial_winding_match:
        print(f"  → Spatial winding 2; phase-space aspect ≠ φ²")
        print(f"    Geometric (2,3) but trajectory not on Golden Torus")
    else:
        print(f"  → No corpus-canonical (2,3) signature in V_inc")
        print(f"    Phase-space mean R/r = {mean_aspect:.3f} (target {PHI_SQ:.3f})")
        print(f"    Spatial winding = {winding:.2f} (target 2)")
        print(f"    Shell mode is geometrically localized but topologically not (2,3)")

    out = {
        "test": "O.1b: V_inc topology measurement",
        "config": {"N": N, "PML": PML, "R": R_torus, "r": r_torus,
                   "amp_ic": amp_ic, "n_bonds": n_bonds},
        "ic_verification": {"a2_max_t0": float(init_a2_int.max())},
        "measure_A_phase_space": {
            "aspects_per_bond_port0": [
                a[0] if not np.isinf(a[0]) else None for a in aspects_per_bond
            ],
            "mean_aspect_port0": float(mean_aspect) if not np.isnan(mean_aspect) else None,
            "phi_squared_target": float(PHI_SQ),
            "phase_space_match": bool(phase_space_match),
        },
        "measure_B_spatial_winding": {
            "winding_number": float(winding),
            "contour_amp_rms": float(amp_rms),
            "spatial_winding_match": bool(spatial_winding_match),
        },
        "op10_cosserat": int(c_op10),
        "energy_retention_50P": float(retention),
        "elapsed_total_s": float(elapsed),
    }
    out_path = Path(__file__).parent / "r10_v8_o1b_v_inc_topology_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
