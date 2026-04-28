"""Photon-Tail Propagating IC — path (b) follow-up to path (a) Mode III.

Per `P_phase6_photon_tail_propagating_ic` (frozen at this commit).

PATH (B) DIFFERENCE FROM PATH (A):
  Path (a) ran with both fields seeded at peak displacement, ZERO initial
  velocities (standing-wave IC). Returned Mode III 0/4 with sector
  asymmetry (Cosserat 4.3% retention, K4 66%) — the standing-wave
  neighborhood doesn't contain the photon-tail attractor's basin.

  Path (b) seeds the Cosserat ω with NON-ZERO initial omega_dot consistent
  with photon-traveling along the loop tangent at speed c. For a (2,3)
  pattern omega = envelope·(cos(θ), sin(θ), 0) propagating at frequency
  ω_loop = 2π·c/L_loop, the time derivative at t=0 is:
      omega_dot[..., 0] = +ω_loop · omega[..., 1]
      omega_dot[..., 1] = -ω_loop · omega[..., 0]
      omega_dot[..., 2] = 0
  This corresponds to omega rotating in (x, y) plane at rate ω_loop —
  which IS propagation of the (2,3) pattern along the loop arc parameter
  since theta = 2φ + 3ψ varies along the loop's parametric path.

  K4 V_inc seed is unchanged from path (a) (corpus (2,3) chiral phasor
  ansatz on ports 0-3). V_ref starts at 0 (forward-traveling default).
  K4 dynamics evolve V_ref naturally via scatter+connect.

C4 INFORMATIONAL PER A57:
  At (R=4, r=1.5) on N=64 lattice, the (2,3) poloidal feature size
  2π·r/3 ≈ 3.14 cells is right at Nyquist boundary. Op10 aliases c=3
  to c=2 at t=0 — sub-Nyquist topology seed. Per A57 (sub-Nyquist
  topology-seed caveat from doc 75_ §10.6), C4 cannot meaningfully
  test "c=3 maintained" when c starts at 2. C4 is demoted to
  INFORMATIONAL in this pre-reg; Mode I = 3/3 of C1/C2/C3 PASS.
  c(t) trajectory is also tracked diagnostically — if c climbs from
  2 to 3 during evolution, that's a positive signal independent of
  C4's strict criterion.

CONTEXT (carried forward from path (a) / doc 75_ §10):
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

OUTPUT_JSON = Path(__file__).parent / "r8_photon_tail_propagating_ic_results.json"

# Photon loop frequency at (R=4, r=1.5): L_loop ≈ 2π·√(4R²+9r²) ≈ 55 cells
# ω_loop = 2π·c/L_loop ≈ 0.114 rad/(natural-time-unit)
# This is the natural propagation rate for a photon along the (2,3) loop
# at speed c=1 in engine natural units.
LOOP_LENGTH_CELLS = 2 * np.pi * np.sqrt(4 * R_LOOP**2 + 9 * R_MINOR**2)
OMEGA_LOOP = 2 * np.pi / LOOP_LENGTH_CELLS    # photon-loop frequency

# c(t) trajectory tracker: sample c every K periods during recording window
C_TRACK_PERIOD_INTERVAL = 10.0   # sample c every 10 Compton periods


def build_engine():
    return VacuumEngine3D.from_args(
        N=N_LATTICE, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )


def seed_dual_field(engine):
    """Seed BOTH K4 V_inc (E-field) and Cosserat ω (B-field) with corpus
    (2,3) topology at (R_LOOP, R_MINOR). PROPAGATING IC for path (b):
    omega_dot is set so the (2,3) pattern propagates along the loop at
    rate ω_loop = 2π·c/L_loop.

    For omega(x, t=0) = envelope·(cos(θ), sin(θ), 0), propagation of the
    (2,3) pattern along the loop arc s at speed c gives
    omega(x, t) = envelope·(cos(θ - ω_loop·t), sin(θ - ω_loop·t), 0).
    Time derivative at t=0:
        omega_dot[..., 0] = +ω_loop · omega[..., 1]
        omega_dot[..., 1] = -ω_loop · omega[..., 0]
        omega_dot[..., 2] = 0
    This is omega rotating in (x, y) plane at rate ω_loop — equivalent to
    the (2,3) pattern (with θ = 2φ + 3ψ) translating along the loop.

    K4 V_inc is unchanged from path (a) (existing initialize_2_3_voltage_ansatz).
    V_ref starts at 0 (forward-traveling default for K4-TLM).
    """
    engine.cos.initialize_electron_2_3_sector(
        R_target=R_LOOP, r_target=R_MINOR,
        use_hedgehog=True, amplitude_scale=A26_AMP_SCALE,
    )
    initialize_2_3_voltage_ansatz(
        engine.k4, R=R_LOOP, r=R_MINOR, amplitude=V_AMP_INIT,
    )

    # PROPAGATING IC: set omega_dot for forward propagation along loop
    omega_arr = np.asarray(engine.cos.omega)
    omega_dot_new = np.zeros_like(omega_arr)
    omega_dot_new[..., 0] = +OMEGA_LOOP * omega_arr[..., 1]
    omega_dot_new[..., 1] = -OMEGA_LOOP * omega_arr[..., 0]
    omega_dot_new[..., 2] = 0.0
    # Preserve mask_alive
    mask_alive = np.asarray(engine.cos.mask_alive)
    omega_dot_new *= mask_alive[..., None]
    engine.cos.omega_dot = omega_dot_new


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
    print(f"  Photon-Tail Propagating IC Test (path b)")
    print(f"  P_phase6_photon_tail_propagating_ic (3/3 + C4 informational)")
    print("=" * 78, flush=True)
    print(f"  Lattice N={N_LATTICE}, PML={PML}, active region {N_LATTICE - 2*PML}^3 cells")
    print(f"  Loop: R={R_LOOP}, r={R_MINOR} (R/r = {R_LOOP/R_MINOR:.3f}, corpus φ² = {PHI_SQ:.3f})")
    print(f"  Loop length L = {LOOP_LENGTH_CELLS:.2f} cells; ω_loop = 2π·c/L = {OMEGA_LOOP:.4f}")
    print(f"  Seeds: V_inc amplitude={V_AMP_INIT}, A26 ω amplitude scale = {A26_AMP_SCALE:.4f}")
    print(f"  Propagating IC: omega_dot set per ω_loop-rotation in (x,y) plane")
    print(f"  Evolution: {N_PERIODS_TOTAL} Compton periods, no drive")
    print(f"  Recording window: t∈[{T_RECORD_START_PERIOD}, {N_PERIODS_TOTAL}]P")
    print(f"  Loop sampling: {N_LOOP_NODES} nodes; c(t) tracked every {C_TRACK_PERIOD_INTERVAL}P")
    print(f"  Adjudication: Mode I = 3/3 of C1/C2/C3 PASS (C4 informational per A57)")
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

    # c(t) tracker — sample c throughout entire run (not just recording window)
    c_track_steps = sorted({
        int(p * COMPTON_PERIOD / DT)
        for p in np.arange(0, N_PERIODS_TOTAL + 1, C_TRACK_PERIOD_INTERVAL)
    })
    c_track_steps = [s for s in c_track_steps if 0 < s <= N_STEPS]
    c_trajectory = []  # list of (step, t_period, c, peak_omega)

    print(f"  Running {N_STEPS} steps (recording from step {STEP_RECORD_START}, "
          f"c sampled at {len(c_track_steps)} timesteps throughout)...")
    t0 = time.time()
    last_progress = t0
    for step in range(1, N_STEPS + 1):
        engine.step()

        # c(t) trajectory — sample throughout run (not just recording window)
        if step in c_track_steps:
            c_now = int(engine.cos.extract_crossing_count())
            peak_omega_now = float(np.linalg.norm(np.asarray(engine.cos.omega), axis=-1).max())
            c_trajectory.append({
                "step": int(step),
                "t_period": float(step * DT / COMPTON_PERIOD),
                "c": c_now,
                "peak_omega": peak_omega_now,
            })

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

    # ─── c(t) trajectory diagnostic ─────────────────────────────────────────────
    print("=" * 78, flush=True)
    print(f"  c(t) trajectory (informational, supplements C4 per A57):")
    for c_pt in c_trajectory:
        print(f"    t={c_pt['t_period']:6.1f}P: c = {c_pt['c']}, peak |ω| = {c_pt['peak_omega']:.4f}")
    c_max_post_t10 = max(
        (cp["c"] for cp in c_trajectory if cp["t_period"] >= 10.0),
        default=-1,
    )
    c_climbed_to_3 = c_max_post_t10 >= 3
    print(f"  c reached 3 at any t≥10P: {c_climbed_to_3}")
    print()

    # ─── Final adjudication (per A57: C4 informational, Mode I = 3/3 of C1/C2/C3) ─
    # Load-bearing criteria for Mode I
    load_bearing = {
        "C1_ellipse_aspect": aspect_phi_match,
        "C2_spatial_winding": winding_match,
        "C3_lc_reactance": lc_reactance_match,
    }
    informational = {
        "C4_topology_strict": topology_match,
        "c_climbed_to_3_during_evolution": c_climbed_to_3,
    }
    load_bearing_pass_count = sum(load_bearing.values())

    print("=" * 78, flush=True)
    print("  Adjudication")
    print("=" * 78, flush=True)
    print(f"  Load-bearing PASS count: {load_bearing_pass_count}/3 (Mode I requires 3/3)")
    print(f"  Per criterion (load-bearing): {load_bearing}")
    print(f"  Informational: {informational}")
    print()

    if load_bearing_pass_count == 3:
        mode = "I"
        verdict = (
            f"MODE I — All 3 load-bearing criteria (C1/C2/C3) PASS. "
            f"Photon-tail propagating IC produces corpus-electron signature "
            f"at engine-representable scale (R={R_LOOP}, r={R_MINOR}). "
            f"C4 (topology strict): {topology_match}. c climbed to 3 "
            f"during evolution: {c_climbed_to_3}. Path (b) validates the "
            f"photon-tail framework — Round 7+8 closes with positive "
            f"empirical result."
        )
    else:
        failed_load_bearing = [k for k, v in load_bearing.items() if not v]
        mode = f"III ({', '.join(failed_load_bearing)} FAIL)"
        verdict = (
            f"MODE III — {load_bearing_pass_count}/3 load-bearing criteria PASS. "
            f"Failed: {failed_load_bearing}. Even with propagating IC at "
            f"engine-representable scale, photon-tail framework doesn't "
            f"produce corpus-electron signature. Per pre-reg threshold: "
            f"photon-tail branch closes; Round 8 closes with cumulative "
            f"empirical statement that engine doesn't host corpus electron "
            f"at any tested configuration accessible to N=64. Round 9 "
            f"(if exists) escalates to N=128+ or reframes corpus prediction."
        )
    print(f"  Mode: {mode}")
    print(f"  {verdict}")
    print()

    # ─── Save payload ─────────────────────────────────────────────────────────
    payload = {
        "pre_registration": "P_phase6_photon_tail_propagating_ic",
        "test": "Photon-tail propagating IC test (path b), 3/3 + C4 informational per A57",
        "omega_loop_natural": OMEGA_LOOP,
        "loop_length_cells": LOOP_LENGTH_CELLS,
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
        "C4_topology_INFORMATIONAL": {
            "c_final": final_c,
            "target": 3,
            "pass": topology_match,
            "note": "C4 demoted to informational per A57 (sub-Nyquist topology seed at R=4, r=1.5 makes c=3 unsatisfiable from t=0). Mode I = 3/3 of C1/C2/C3.",
        },
        "c_trajectory": c_trajectory,
        "c_climbed_to_3_during_evolution": c_climbed_to_3,
        "load_bearing_pass_count": load_bearing_pass_count,
        "load_bearing_total": 3,
        "mode": mode,
        "verdict": verdict,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()
