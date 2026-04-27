"""Photon-Tail Dual Seed — corpus electron test at engine-representable scale.

Per `P_phase6_photon_tail_dual_seed` (frozen at this commit).

CONTEXT:
  Per Grant's photon-tail framing: a self-trapped photon catching its own
  tail in a (2,3) torus-knot loop IS the electron. R7+R8 (~30 commits)
  seeded only the Cosserat (B-field) half via initialize_electron_2_3_sector
  with V_inc held at zero. Result: the engine produced (2,3)-topological
  attractors (Move 5+7+10+11) but always with K4 V_inc DC — half-electron
  signal.

  This test seeds BOTH K4 V_inc (E-field) and Cosserat ω (B-field) with
  corpus (2,3) topology at the smallest engine-representable scale. Per
  doc 28_ §3+§4: the corpus PASS criterion is phasor-space (V_inc, V_ref)
  ellipse aspect R_phase/r_phase = φ² at any single loop node. Real-space
  frequency ω_natural ≠ ω_C is forced by lattice resolution and is NOT
  load-bearing.

LATTICE-RESOLUTION CHOICE:
  At N=32 (Move 5+ scale): loop fits but (2,3) winding sub-Nyquist OR
    (2,3) winding resolved but loop wraps active region. Can't both hold.
  At N=64 with R=4, r=1.5: loop length ~55 cells in 56³ active region;
    (2,3) toroidal cycle ~13 cells, poloidal cycle ~3 cells — both above
    Nyquist. First lattice that supports a meaningful photon-tail test.

INITIAL CONDITION CHOICE (path a — standing-wave IC):
  Both fields seeded at peak displacement at t=0 with the existing
  seeders (initialize_2_3_voltage_ansatz for K4, initialize_electron_2_3_sector
  for Cosserat). Zero initial velocities. If photon-tail is a stable
  attractor, system should find it from the standing-wave neighborhood
  via free evolution.

  Caveat: Move 5's standing-wave IC produced a static hedgehog, NOT a
  propagating mode. If this test returns Mode III, path (b) propagating
  IC (set ω_dot, V_ref velocities consistent with photon along loop
  tangent) becomes the natural follow-up before declaring photon-tail
  framing falsified.

4-CRITERION ADJUDICATION (per auditor refinement):
  C1 — Single-node ellipse aspect: at each sampled loop node, fit ellipse
       to (V_inc, V_ref)(t) trajectory over t∈[150P, 200P] window. Compute
       R_phase/r_phase via PCA. Median across loop nodes ≈ φ² ± 5%.
       (Necessary but not sufficient — generic LC could also give φ².)
  C2 — Spatial winding rotation: at each sampled loop node, compute
       ellipse orientation angle. Track angle as function of arc-length
       position along loop. Total winding = 2 toroidal + 3 poloidal
       cycles = 5 × 2π over one full loop. Tolerance ±30%.
       (Distinguishes corpus (2,3) topology from generic LC.)
  C3 — LC reactance: cross-correlation ρ(Σ|V_inc|²(t), Σ|Φ_link|²(t))
       over recording window. K4↔K4-inductive trading for the bond LC
       tank → ρ ≈ -1 ± 0.2. Confirms LC oscillation, not static fixed
       point.
  C4 — Topology preservation: c via engine.cos.extract_crossing_count()
       at end of run. c=3 maintained.

  Mode I (corpus electron at engine scale): all 4 PASS.
  Mode III variants: at least one FAIL; failure pattern names what's wrong.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ave.topological.vacuum_engine import VacuumEngine3D
from tlm_electron_soliton_eigenmode import initialize_2_3_voltage_ansatz


# ─── Constants per pred ───────────────────────────────────────────────────────

PHI = 0.5 * (1.0 + np.sqrt(5.0))
PHI_SQ = PHI * PHI

N_LATTICE = 64
PML = 4
R_LOOP = 4.0           # major radius (lattice cells); chosen so (2,3) winding resolved
R_MINOR = 1.5          # minor radius; r/R ≈ φ⁻² approx, but lattice-snapped

A26_AMP_SCALE = 0.3 / (np.sqrt(3.0) / 2.0)   # → peak |ω| = 0.3π corpus convention
V_AMP_INIT = 0.1                              # K4 V_inc seed (linear regime)

OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi / OMEGA_C
N_PERIODS_TOTAL = 200.0
DT = 1.0 / np.sqrt(2.0)
N_STEPS = int(N_PERIODS_TOTAL * COMPTON_PERIOD / DT) + 1

# Recording window for phasor extraction
T_RECORD_START_PERIOD = 150.0
STEP_RECORD_START = int(T_RECORD_START_PERIOD * COMPTON_PERIOD / DT)

# Loop sampling
N_LOOP_NODES = 30      # number of nodes sampled along (2,3) torus knot

# Adjudication thresholds
ELLIPSE_ASPECT_TOL = 0.05            # 5% on R_phase/r_phase = φ²
SPATIAL_WINDING_TOL_FRAC = 0.30      # 30% on total winding = 5·2π
LC_REACTANCE_RANGE = (-1.2, -0.8)    # ρ ≈ -1 ± 0.2

# K4 port unit vectors (from k4_tlm.py)
PORT_VECTORS = np.array([
    [+1, +1, +1],
    [+1, -1, -1],
    [-1, +1, -1],
    [-1, -1, +1],
], dtype=float) / np.sqrt(3.0)

OUTPUT_JSON = Path(__file__).parent / "r8_photon_tail_dual_seed_results.json"


def build_engine():
    return VacuumEngine3D.from_args(
        N=N_LATTICE, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )


def seed_dual_field(engine):
    """Seed BOTH K4 V_inc (E-field) and Cosserat ω (B-field) with corpus
    (2,3) topology at (R_LOOP, R_MINOR). Standing-wave initial conditions
    (no initial velocities)."""
    engine.cos.initialize_electron_2_3_sector(
        R_target=R_LOOP, r_target=R_MINOR,
        use_hedgehog=True, amplitude_scale=A26_AMP_SCALE,
    )
    initialize_2_3_voltage_ansatz(
        engine.k4, R=R_LOOP, r=R_MINOR, amplitude=V_AMP_INIT,
    )


def loop_path_samples(n_samples=N_LOOP_NODES):
    """Generate (t_param, cell_3d, port_idx, tangent, arc_length) tuples
    along the (2,3) torus knot at (R_LOOP, R_MINOR), centered at lattice
    center. Each cell is the lattice cell closest to the curve at that
    parametric t. Port chosen as max-projection onto local tangent."""
    cx = (N_LATTICE - 1) / 2.0
    p, q = 2, 3   # (2,3) torus knot

    samples = []
    cumulative_arc = 0.0
    prev_xyz = None
    for i, t in enumerate(np.linspace(0, 2 * np.pi, n_samples, endpoint=False)):
        x = (R_LOOP + R_MINOR * np.cos(q * t)) * np.cos(p * t)
        y = (R_LOOP + R_MINOR * np.cos(q * t)) * np.sin(p * t)
        z = R_MINOR * np.sin(q * t)

        # Cumulative arc length (relative to start)
        if prev_xyz is not None:
            cumulative_arc += np.linalg.norm(np.array([x, y, z]) - prev_xyz)
        prev_xyz = np.array([x, y, z])

        ix = int(round(cx + x))
        iy = int(round(cx + y))
        iz = int(round(cx + z))

        # Tangent vector at this t (for port selection)
        dx_dt = (-R_MINOR * q * np.sin(q * t) * np.cos(p * t)
                 - (R_LOOP + R_MINOR * np.cos(q * t)) * p * np.sin(p * t))
        dy_dt = (-R_MINOR * q * np.sin(q * t) * np.sin(p * t)
                 + (R_LOOP + R_MINOR * np.cos(q * t)) * p * np.cos(p * t))
        dz_dt = R_MINOR * q * np.cos(q * t)
        tangent = np.array([dx_dt, dy_dt, dz_dt])
        tangent /= np.linalg.norm(tangent)

        # Pick the port whose direction has max abs projection onto tangent
        projections = PORT_VECTORS @ tangent
        best_port = int(np.argmax(np.abs(projections)))

        samples.append({
            "t_param": float(t),
            "cell": (ix, iy, iz),
            "port": best_port,
            "tangent": tangent.tolist(),
            "arc_length": float(cumulative_arc),
        })

    return samples


def fit_ellipse_pca(v_inc_series, v_ref_series):
    """Fit ellipse via PCA on (V_inc, V_ref) trajectory.
    Returns (R_phase, r_phase, R_over_r, theta_orientation, amp_drift)."""
    v_inc = np.asarray(v_inc_series)
    v_ref = np.asarray(v_ref_series)
    pts = np.column_stack([v_inc - v_inc.mean(), v_ref - v_ref.mean()])

    if pts.std() < 1e-15:
        return float("nan"), float("nan"), float("nan"), float("nan"), float("nan")

    cov = np.cov(pts.T)
    evals, evecs = np.linalg.eigh(cov)
    order = np.argsort(evals)[::-1]
    evals = evals[order]
    evecs = evecs[:, order]
    R_phase = float(np.sqrt(max(evals[0], 0)))
    r_phase = float(np.sqrt(max(evals[1], 0)))
    R_over_r = R_phase / max(r_phase, 1e-30)
    theta = float(np.arctan2(evecs[1, 0], evecs[0, 0]))

    # Amplitude drift: 5-chunk trajectory amplitude std/mean
    chunks = 5
    chunk_size = len(v_inc) // chunks
    amps = []
    for ci in range(chunks):
        s = ci * chunk_size
        e = (ci + 1) * chunk_size
        if e <= len(v_inc) and chunk_size >= 3:
            amps.append(float(np.sqrt(np.var(v_inc[s:e]) + np.var(v_ref[s:e]))))
    amp_drift = float(np.std(amps) / max(np.mean(amps), 1e-30)) if amps else float("inf")

    return R_phase, r_phase, R_over_r, theta, amp_drift


def main():
    print("=" * 78, flush=True)
    print(f"  Photon-Tail Dual Seed Test")
    print(f"  P_phase6_photon_tail_dual_seed (4-criterion adjudication)")
    print("=" * 78, flush=True)
    print(f"  Lattice N={N_LATTICE}, PML={PML}, active region {N_LATTICE - 2*PML}^3 cells")
    print(f"  Loop: R={R_LOOP}, r={R_MINOR} (R/r = {R_LOOP/R_MINOR:.3f}, corpus φ² = {PHI_SQ:.3f})")
    print(f"  Seeds: V_inc amplitude={V_AMP_INIT}, A26 ω amplitude scale = {A26_AMP_SCALE:.4f}")
    print(f"  Evolution: {N_PERIODS_TOTAL} Compton periods, no drive (standing-wave IC)")
    print(f"  Recording window: t∈[{T_RECORD_START_PERIOD}, {N_PERIODS_TOTAL}]P")
    print(f"  Loop sampling: {N_LOOP_NODES} nodes")
    print()

    engine = build_engine()
    seed_dual_field(engine)

    # Identify loop path nodes
    loop_nodes = loop_path_samples(N_LOOP_NODES)
    print(f"  Sampled {len(loop_nodes)} cells along (2,3) torus knot")
    cells_unique = set(n["cell"] for n in loop_nodes)
    print(f"  Unique lattice cells: {len(cells_unique)} (some samples may snap to same cell)")
    print()

    # Pre-recording state check
    initial_omega_peak = float(np.linalg.norm(np.asarray(engine.cos.omega), axis=-1).max())
    initial_vinc_peak = float(np.linalg.norm(np.asarray(engine.k4.V_inc), axis=-1).max())
    initial_c = int(engine.cos.extract_crossing_count())
    print(f"  Initial state: peak |ω| = {initial_omega_peak:.4f}, "
          f"peak |V_inc| = {initial_vinc_peak:.4f}, c = {initial_c}")
    print()

    # Recording arrays
    n_record_steps = N_STEPS - STEP_RECORD_START + 1
    times = []
    v_inc_traces = [[] for _ in loop_nodes]
    v_ref_traces = [[] for _ in loop_nodes]
    sum_vinc_sq_series = []
    sum_philink_sq_series = []
    T_cos_series = []
    V_cos_series = []

    print(f"  Running {N_STEPS} steps (recording from step {STEP_RECORD_START})...")
    t0 = time.time()
    last_progress = t0
    for step in range(1, N_STEPS + 1):
        engine.step()
        if step >= STEP_RECORD_START:
            times.append(float(step * DT / COMPTON_PERIOD))

            v_inc_arr = np.asarray(engine.k4.V_inc)
            v_ref_arr = np.asarray(engine.k4.V_ref)
            phi_link = np.asarray(engine.k4.Phi_link)
            mask_active = np.asarray(engine.k4.mask_active)
            mask_A = np.asarray(engine.k4.mask_A)

            # Per-node V_inc, V_ref at chosen port
            for i, node in enumerate(loop_nodes):
                ix, iy, iz = node["cell"]
                p_idx = node["port"]
                v_inc_traces[i].append(float(v_inc_arr[ix, iy, iz, p_idx]))
                v_ref_traces[i].append(float(v_ref_arr[ix, iy, iz, p_idx]))

            # Global energy series
            T_cos_series.append(float(engine.cos.kinetic_energy()))
            V_cos_series.append(float(engine.cos.total_energy()))
            sum_vinc_sq_series.append(
                float(np.sum((v_inc_arr * mask_active[..., None]) ** 2)))
            sum_philink_sq_series.append(
                float(np.sum((phi_link * mask_A[..., None]) ** 2)))

        if (time.time() - last_progress) > 60.0:
            t_p = step * DT / COMPTON_PERIOD
            print(f"    [progress] step {step}, t={t_p:.1f}P, "
                  f"elapsed {time.time() - t0:.1f}s", flush=True)
            last_progress = time.time()

    elapsed = time.time() - t0
    print(f"  Run complete: {elapsed:.1f}s, recorded {len(times)} samples per node")
    print()

    # End-state diagnostics
    final_omega_peak = float(np.linalg.norm(np.asarray(engine.cos.omega), axis=-1).max())
    final_vinc_peak = float(np.linalg.norm(np.asarray(engine.k4.V_inc), axis=-1).max())
    final_c = int(engine.cos.extract_crossing_count())
    print(f"  Final state (t={N_PERIODS_TOTAL}P):")
    print(f"    peak |ω| = {final_omega_peak:.4f} (initial {initial_omega_peak:.4f})")
    print(f"    peak |V_inc| = {final_vinc_peak:.4f} (initial {initial_vinc_peak:.4f})")
    print(f"    c via Op10 = {final_c} (initial {initial_c})")
    print()

    # ─── Adjudication ─────────────────────────────────────────────────────────

    # C1 — Single-node ellipse aspect at each loop node
    aspect_records = []
    for i, node in enumerate(loop_nodes):
        R_p, r_p, ratio, theta, amp_drift = fit_ellipse_pca(
            v_inc_traces[i], v_ref_traces[i],
        )
        aspect_records.append({
            "node_idx": i,
            "cell": list(node["cell"]),
            "port": node["port"],
            "arc_length": node["arc_length"],
            "R_phase": R_p,
            "r_phase": r_p,
            "R_over_r": ratio,
            "theta": theta,
            "amp_drift": amp_drift,
        })

    aspects_finite = [r["R_over_r"] for r in aspect_records if np.isfinite(r["R_over_r"])]
    median_aspect = float(np.median(aspects_finite)) if aspects_finite else float("nan")
    aspect_phi_match = (np.isfinite(median_aspect)
                       and abs(median_aspect - PHI_SQ) / PHI_SQ < ELLIPSE_ASPECT_TOL)

    print(f"  C1 — Single-node ellipse aspect at {len(aspects_finite)} loop nodes:")
    print(f"    Median R_phase/r_phase = {median_aspect:.4f}, target = {PHI_SQ:.4f} ± {ELLIPSE_ASPECT_TOL:.0%}")
    print(f"    {'PASS' if aspect_phi_match else 'FAIL'}")
    print()

    # C2 — Spatial winding rotation across loop nodes
    orientations_finite = np.array(
        [r["theta"] for r in aspect_records if np.isfinite(r["theta"])])
    if len(orientations_finite) >= N_LOOP_NODES // 2:
        # Unwrap to track continuous rotation
        unwrapped = np.unwrap(orientations_finite)
        total_winding_rad = float(unwrapped[-1] - unwrapped[0])
        total_winding_2pi = abs(total_winding_rad) / (2 * np.pi)
        # Expected: 2 toroidal + 3 poloidal = 5 cycles ⇒ 5·2π
        expected_winding_2pi = 5.0
        winding_ratio = total_winding_2pi / expected_winding_2pi
        winding_match = abs(winding_ratio - 1.0) < SPATIAL_WINDING_TOL_FRAC
    else:
        total_winding_2pi = float("nan")
        winding_ratio = float("nan")
        winding_match = False

    print(f"  C2 — Spatial winding (ellipse orientation rotation along loop):")
    print(f"    Total Δθ = {total_winding_2pi:.3f} × 2π, target = 5 × 2π ± {SPATIAL_WINDING_TOL_FRAC:.0%}")
    print(f"    {'PASS' if winding_match else 'FAIL'}")
    print()

    # C3 — LC reactance
    sum_vinc_arr = np.array(sum_vinc_sq_series)
    sum_phi_arr = np.array(sum_philink_sq_series)
    if sum_vinc_arr.std() > 1e-10 and sum_phi_arr.std() > 1e-10:
        rho_LC = float(np.corrcoef(sum_vinc_arr, sum_phi_arr)[0, 1])
        lc_reactance_match = LC_REACTANCE_RANGE[0] < rho_LC < LC_REACTANCE_RANGE[1]
    else:
        rho_LC = None
        lc_reactance_match = False

    print(f"  C3 — LC reactance ρ(Σ|V_inc|², Σ|Φ_link|²):")
    print(f"    ρ = {rho_LC}, target ∈ {LC_REACTANCE_RANGE}")
    print(f"    {'PASS' if lc_reactance_match else 'FAIL'}")
    print()

    # C4 — Topology preservation
    topology_match = final_c == 3

    print(f"  C4 — Topology preservation (c via Op10 at end):")
    print(f"    c_final = {final_c}, target = 3")
    print(f"    {'PASS' if topology_match else 'FAIL'}")
    print()

    # ─── Final adjudication ─────────────────────────────────────────────────────
    pass_flags = {
        "C1_ellipse_aspect": aspect_phi_match,
        "C2_spatial_winding": winding_match,
        "C3_lc_reactance": lc_reactance_match,
        "C4_topology": topology_match,
    }
    pass_count = sum(pass_flags.values())

    print("=" * 78, flush=True)
    print("  Adjudication")
    print("=" * 78, flush=True)
    print(f"  PASS count: {pass_count}/4")
    print(f"  Per criterion: {pass_flags}")
    print()

    if pass_count == 4:
        mode = "I"
        verdict = (
            f"MODE I — All 4 criteria PASS. Photon-tail dual seed produces "
            f"corpus-electron signature at engine-representable scale "
            f"(R={R_LOOP}, r={R_MINOR}). The corpus electron exists in the "
            f"engine via the propagating-loop framework. Round 7+8 closes "
            f"with positive empirical result."
        )
    else:
        failed = [k for k, v in pass_flags.items() if not v]
        mode = f"III ({', '.join(failed)} FAIL)"
        verdict = (
            f"MODE III — {pass_count}/4 criteria PASS. Failed: {failed}. "
            f"Engine doesn't host corpus electron at this scale via "
            f"standing-wave dual-seed photon-tail. Specific failures suggest "
            f"which axis is broken. Path (b) propagating-IC test may be "
            f"warranted before declaring photon-tail framing falsified."
        )
    print(f"  Mode: {mode}")
    print(f"  {verdict}")
    print()

    # ─── Save payload ─────────────────────────────────────────────────────────
    payload = {
        "pre_registration": "P_phase6_photon_tail_dual_seed",
        "test": "Photon-tail dual seed test, standing-wave IC (path a), 4-criterion adjudication",
        "N": N_LATTICE,
        "PML": PML,
        "R_loop": R_LOOP,
        "r_minor": R_MINOR,
        "n_loop_nodes_sampled": N_LOOP_NODES,
        "n_unique_cells": len(cells_unique),
        "n_periods_total": N_PERIODS_TOTAL,
        "n_record_samples": len(times),
        "elapsed_seconds": elapsed,
        "loop_node_path": loop_nodes,
        "initial_state": {
            "peak_omega": initial_omega_peak,
            "peak_vinc": initial_vinc_peak,
            "c": initial_c,
        },
        "final_state": {
            "peak_omega": final_omega_peak,
            "peak_vinc": final_vinc_peak,
            "c": final_c,
        },
        "C1_ellipse_aspect": {
            "median_R_over_r": median_aspect,
            "target": PHI_SQ,
            "tolerance": ELLIPSE_ASPECT_TOL,
            "pass": aspect_phi_match,
            "per_node_records": aspect_records,
        },
        "C2_spatial_winding": {
            "total_winding_2pi": total_winding_2pi,
            "winding_ratio": winding_ratio,
            "target_cycles": 5,
            "tolerance_frac": SPATIAL_WINDING_TOL_FRAC,
            "pass": winding_match,
        },
        "C3_lc_reactance": {
            "rho_vinc_philink": rho_LC,
            "target_range": list(LC_REACTANCE_RANGE),
            "pass": lc_reactance_match,
        },
        "C4_topology": {
            "c_final": final_c,
            "target": 3,
            "pass": topology_match,
        },
        "pass_count": pass_count,
        "mode": mode,
        "verdict": verdict,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()
