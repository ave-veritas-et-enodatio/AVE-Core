"""r9_canonical_phase_space_phasor.py — Round 9 entry per P_phase8_canonical_phase_space_phasor.

Doc 28 §5.1 canonical single-bond (V_inc, V_ref) phasor test in its corpus-canonical
phase-space interpretation (per doc 28 §5.4 + doc 29 §3.3 + doc 07 §3 scalar c).

Per Grant plumber reframe (electron = trapped node vortex, intrinsic per-node L+C,
genesis chirality) + auditor pattern thesis (R, r are phase-space NOT real-space;
(2, 3)-as-Hopfion-pair was Vol 1 Ch 8 spatial creeper; Op10 c is scalar invariant).

Setup IDENTICAL to Move 5 (P_phase6_self_consistent_orbit_hunt). Per-bond V_inc(t)/
V_ref(t) capture added at top-K=4 interior bonds during recording window t ∈ [50, 200] P.

Dual-criterion adjudication:
  C1 (load-bearing): median R_phase/r_phase across top-K bonds = φ² ± 5%
  C2 (load-bearing): chirality consensus ≥ 75% across top-K bonds
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


# ─── Constants per pred (matching Move 5 exactly for engine setup) ────────────

PHI = 0.5 * (1.0 + np.sqrt(5.0))
PHI_SQ = PHI * PHI

# Lattice (matches Move 5)
N_LATTICE = 32
PML = 4
R_ANCHOR = 10.0
R_MINOR = R_ANCHOR / PHI_SQ

# Seeds (matches Move 5)
A26_AMP_SCALE = 0.3 / (np.sqrt(3.0) / 2.0)
GT_PEAK_OMEGA = 0.3 * np.pi
A26_GUARD_LOW = 0.85 * GT_PEAK_OMEGA
A26_GUARD_HIGH = 1.15 * GT_PEAK_OMEGA
V_AMP_INIT = 0.14

# Time evolution (matches Move 5)
OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi / OMEGA_C
N_PERIODS_TOTAL = 200.0
DT = 1.0 / np.sqrt(2.0)
N_STEPS_TOTAL = int(N_PERIODS_TOTAL * COMPTON_PERIOD / DT) + 1

# Phase-space sampling windows (NEW vs Move 5)
PRE_EVOLVE_END_P = 40.0          # no sampling, just evolve through transient
SELECTION_END_P = 50.0           # selection window: [40, 50] P
RECORDING_END_P = 200.0          # recording window: [50, 200] P, 150 Compton periods

PRE_EVOLVE_END_STEP = int(PRE_EVOLVE_END_P * COMPTON_PERIOD / DT)
SELECTION_END_STEP = int(SELECTION_END_P * COMPTON_PERIOD / DT)
RECORDING_END_STEP = N_STEPS_TOTAL  # =1777

N_SELECTION_STEPS = SELECTION_END_STEP - PRE_EVOLVE_END_STEP
N_RECORDING_STEPS = RECORDING_END_STEP - SELECTION_END_STEP

# Sampler config
TOP_K_BONDS = 4
SAMPLE_PORT = 0  # port 0, matching Test B v1 convention

# Adjudication thresholds
PHI_SQ_TOL = 0.05  # ±5%
CHIRALITY_CONSISTENCY_THRESHOLD = 0.75  # ≥3 of 4 same sign
PERSISTENCE_GUARD = 0.40  # if peak |ω| < 40% at end, attractor dissolved

OUTPUT_JSON = Path(__file__).parent / "r9_canonical_phase_space_phasor_results.json"


def build_engine():
    return VacuumEngine3D.from_args(
        N=N_LATTICE, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )


def seed_corpus_2_3_joint(engine):
    engine.cos.initialize_electron_2_3_sector(
        R_target=R_ANCHOR, r_target=R_MINOR,
        use_hedgehog=True, amplitude_scale=A26_AMP_SCALE,
    )
    initialize_2_3_voltage_ansatz(
        engine.k4, R=R_ANCHOR, r=R_MINOR, amplitude=V_AMP_INIT,
    )


def make_interior_mask(nx, pml):
    mask = np.zeros((nx, nx, nx), dtype=bool)
    mask[pml:nx - pml, pml:nx - pml, pml:nx - pml] = True
    return mask


def fit_ellipse_pca(v_inc_traj, v_ref_traj):
    """PCA on (V_inc, V_ref) point cloud → ellipse axes.
    Returns (R_phase, r_phase) = (major, minor) axis lengths.
    """
    points = np.column_stack([v_inc_traj, v_ref_traj])
    points = points - points.mean(axis=0)
    cov = np.cov(points.T)
    eigvals = np.sort(np.linalg.eigvalsh(cov))  # ascending
    r_phase = float(np.sqrt(max(eigvals[0], 1e-30)))
    R_phase = float(np.sqrt(max(eigvals[1], 1e-30)))
    return R_phase, r_phase


def chirality_direction(v_inc_traj, v_ref_traj):
    """Mean angular momentum P × dP/dt around centroid.
    Sign: + = CCW, - = CW.
    """
    v_inc = np.asarray(v_inc_traj)
    v_ref = np.asarray(v_ref_traj)
    v_inc_c = v_inc - v_inc.mean()
    v_ref_c = v_ref - v_ref.mean()
    dv_inc = np.diff(v_inc_c)
    dv_ref = np.diff(v_ref_c)
    v_inc_mid = 0.5 * (v_inc_c[:-1] + v_inc_c[1:])
    v_ref_mid = 0.5 * (v_ref_c[:-1] + v_ref_c[1:])
    cross = v_inc_mid * dv_ref - v_ref_mid * dv_inc
    return float(cross.mean()), float(cross.std()), int(np.sign(cross.mean()))


def main():
    print("=" * 78, flush=True)
    print("  r9 — Canonical phase-space (V_inc, V_ref) phasor on Move 5 attractor")
    print("  P_phase8_canonical_phase_space_phasor")
    print("=" * 78, flush=True)
    print(f"  Lattice: N={N_LATTICE}, PML={PML} (interior {N_LATTICE - 2*PML}^3)")
    print(f"  Corpus GT: R={R_ANCHOR}, r={R_MINOR:.4f} (R/φ²)")
    print(f"  Seed: peak |ω|={GT_PEAK_OMEGA:.4f} (A26 scale {A26_AMP_SCALE:.4f}); "
          f"V_amp={V_AMP_INIT}")
    print(f"  Evolution: {N_PERIODS_TOTAL} Compton periods ({N_STEPS_TOTAL} steps "
          f"at dt={DT:.4f})")
    print(f"  Pre-evolve: t ∈ [0, {PRE_EVOLVE_END_P}] P "
          f"(steps 0..{PRE_EVOLVE_END_STEP-1})")
    print(f"  Selection: t ∈ [{PRE_EVOLVE_END_P}, {SELECTION_END_P}] P "
          f"({N_SELECTION_STEPS} steps; accumulate |V_inc[port {SAMPLE_PORT}]|²)")
    print(f"  Recording: t ∈ [{SELECTION_END_P}, {RECORDING_END_P}] P "
          f"({N_RECORDING_STEPS} steps; capture V_inc, V_ref at top-{TOP_K_BONDS} bonds)")
    print(f"  C1 (load-bearing): median R/r = φ²={PHI_SQ:.4f} ± {PHI_SQ_TOL:.0%}")
    print(f"  C2 (load-bearing): chirality consensus ≥ {CHIRALITY_CONSISTENCY_THRESHOLD:.0%}")
    print()

    engine = build_engine()
    seed_corpus_2_3_joint(engine)

    omega_init = np.asarray(engine.cos.omega)
    omega_peak_init = float(np.linalg.norm(omega_init, axis=-1).max())
    assert A26_GUARD_LOW <= omega_peak_init <= A26_GUARD_HIGH, (
        f"A26 guard FAILED: peak |ω|={omega_peak_init:.4f} not in "
        f"[{A26_GUARD_LOW:.4f}, {A26_GUARD_HIGH:.4f}]"
    )
    print(f"  Initial peak |ω| = {omega_peak_init:.4f} (A26 guard OK)")

    # ─── Phase 1: pre-evolve ───────────────────────────────────────────────────
    print(f"  Pre-evolving to t={PRE_EVOLVE_END_P} P...", flush=True)
    t0 = time.time()
    last_progress = t0
    for step in range(PRE_EVOLVE_END_STEP):
        engine.step()
        if (time.time() - last_progress) > 30.0:
            t_period = step * DT / COMPTON_PERIOD
            print(f"    [progress] t={t_period:6.1f} P  step={step:5d}  "
                  f"elapsed {time.time()-t0:.1f}s", flush=True)
            last_progress = time.time()
    print(f"    pre-evolve done at {time.time()-t0:.1f}s", flush=True)

    # ─── Phase 2: cell selection (accumulate |V_inc|² per port=0) ──────────────
    print(f"  Cell selection window...", flush=True)
    interior_mask = make_interior_mask(engine.k4.nx, PML)
    v_inc_sq_accum = np.zeros((engine.k4.nx, engine.k4.nx, engine.k4.nx))

    for i in range(N_SELECTION_STEPS):
        engine.step()
        v_inc = np.asarray(engine.k4.V_inc)  # (nx, nx, nx, 4)
        v_inc_sq_accum += v_inc[..., SAMPLE_PORT] ** 2
        if (time.time() - last_progress) > 30.0:
            t_period = (PRE_EVOLVE_END_STEP + i) * DT / COMPTON_PERIOD
            print(f"    [progress] t={t_period:6.1f} P  step={PRE_EVOLVE_END_STEP+i:5d}  "
                  f"elapsed {time.time()-t0:.1f}s", flush=True)
            last_progress = time.time()

    v_inc_mean_sq = v_inc_sq_accum / N_SELECTION_STEPS
    v_inc_mean_sq_interior = v_inc_mean_sq.copy()
    v_inc_mean_sq_interior[~interior_mask] = 0.0

    flat_idx = np.argpartition(v_inc_mean_sq_interior.ravel(), -TOP_K_BONDS)[-TOP_K_BONDS:]
    sorted_idx = flat_idx[np.argsort(-v_inc_mean_sq_interior.ravel()[flat_idx])]
    top_cells = []
    for idx in sorted_idx:
        ix, iy, iz = np.unravel_index(idx, v_inc_mean_sq_interior.shape)
        top_cells.append((int(ix), int(iy), int(iz)))
        print(f"    Top-{len(top_cells)} cell: ({ix},{iy},{iz})  "
              f"|V_inc[port {SAMPLE_PORT}]|²={v_inc_mean_sq_interior[ix,iy,iz]:.4e}",
              flush=True)
    print(f"    selection done at {time.time()-t0:.1f}s", flush=True)

    # ─── Phase 3: recording window (per-step trajectory capture) ────────────────
    print(f"  Recording window: capturing V_inc, V_ref at top-{TOP_K_BONDS} bonds...",
          flush=True)
    v_inc_traj = np.zeros((N_RECORDING_STEPS, TOP_K_BONDS))
    v_ref_traj = np.zeros((N_RECORDING_STEPS, TOP_K_BONDS))

    for i in range(N_RECORDING_STEPS):
        engine.step()
        v_inc = np.asarray(engine.k4.V_inc)
        v_ref = np.asarray(engine.k4.V_ref)
        for k, (ix, iy, iz) in enumerate(top_cells):
            v_inc_traj[i, k] = v_inc[ix, iy, iz, SAMPLE_PORT]
            v_ref_traj[i, k] = v_ref[ix, iy, iz, SAMPLE_PORT]
        if (time.time() - last_progress) > 30.0:
            t_period = (SELECTION_END_STEP + i) * DT / COMPTON_PERIOD
            print(f"    [progress] t={t_period:6.1f} P  step={SELECTION_END_STEP+i:5d}  "
                  f"elapsed {time.time()-t0:.1f}s", flush=True)
            last_progress = time.time()

    elapsed_total = time.time() - t0
    print(f"  Recording done; total elapsed {elapsed_total:.1f}s", flush=True)

    # ─── Phase 4: per-bond ellipse + chirality ─────────────────────────────────
    print()
    print("=" * 78, flush=True)
    print("  Per-bond phase-space ellipse + chirality")
    print("=" * 78, flush=True)

    bond_results = []
    for k in range(TOP_K_BONDS):
        R_phase, r_phase = fit_ellipse_pca(v_inc_traj[:, k], v_ref_traj[:, k])
        R_over_r = R_phase / max(r_phase, 1e-30)
        cross_mean, cross_std, chirality_sign = chirality_direction(
            v_inc_traj[:, k], v_ref_traj[:, k])
        chir_label = "CCW" if chirality_sign > 0 else "CW" if chirality_sign < 0 else "AMBIG"
        bond_results.append({
            "cell": list(top_cells[k]),
            "port": SAMPLE_PORT,
            "R_phase": R_phase,
            "r_phase": r_phase,
            "R_over_r": R_over_r,
            "chirality_cross_mean": cross_mean,
            "chirality_cross_std": cross_std,
            "chirality_sign": chirality_sign,
            "chirality_label": chir_label,
        })
        print(f"  Bond {k}: cell={top_cells[k]}  R/r={R_over_r:8.4f}  "
              f"chirality={chir_label} (cross_mean={cross_mean:+.3e}, "
              f"std/|mean|={cross_std/max(abs(cross_mean), 1e-30):.2f})",
              flush=True)

    # ─── Phase 5: dual-criterion adjudication ──────────────────────────────────
    R_over_r_values = [b["R_over_r"] for b in bond_results]
    median_R_over_r = float(np.median(R_over_r_values))
    chirality_signs = [b["chirality_sign"] for b in bond_results]
    n_ccw = sum(1 for s in chirality_signs if s > 0)
    n_cw = sum(1 for s in chirality_signs if s < 0)
    consensus_count = max(n_ccw, n_cw)
    consensus_fraction = consensus_count / len(chirality_signs)
    consensus_direction = "CCW" if n_ccw > n_cw else "CW" if n_cw > n_ccw else "TIE"

    c1_pass = abs(median_R_over_r - PHI_SQ) <= PHI_SQ_TOL * PHI_SQ
    c2_pass = consensus_fraction >= CHIRALITY_CONSISTENCY_THRESHOLD

    omega_final = np.asarray(engine.cos.omega)
    omega_peak_final = float(np.linalg.norm(omega_final, axis=-1).max())
    persistence = omega_peak_final / max(omega_peak_init, 1e-30)
    persistence_ok = persistence >= PERSISTENCE_GUARD

    if c1_pass and c2_pass:
        mode = "I"
        verdict = (
            f"MODE I — CORPUS VINDICATED at canonical phase-space scale. "
            f"Median R_phase/r_phase = {median_R_over_r:.4f} (target φ²={PHI_SQ:.4f} ± {PHI_SQ_TOL:.0%}) "
            f"AND chirality consensus {consensus_fraction:.0%} ({consensus_direction}). "
            f"Trapped-node-vortex picture empirically confirmed; the seven Mode III tests "
            f"retroactively reread as wrong-sampler. L3 branch closes positive at canonical "
            f"doc 28 §5.1 single-bond phase-space test."
        )
    elif (not c1_pass) and c2_pass:
        mode = "II-aspect"
        verdict = (
            f"MODE II-aspect — phase-space ellipse with consistent chirality but not at φ². "
            f"Median R/r = {median_R_over_r:.4f} (target {PHI_SQ:.4f}). Chirality consensus "
            f"{consensus_fraction:.0%} ({consensus_direction}). Stable phasor exists but aspect "
            f"ratio doesn't match corpus; characterize-as-itself per Rule 10."
        )
    elif c1_pass and (not c2_pass):
        mode = "II-chirality"
        verdict = (
            f"MODE II-chirality — R/r matches φ² but chirality inconsistent. "
            f"Median R/r = {median_R_over_r:.4f} (target {PHI_SQ:.4f}, PASS), but consensus "
            f"only {consensus_fraction:.0%}. Closed ellipse at right aspect but not a vortex."
        )
    else:
        mode = "III"
        verdict = (
            f"MODE III — phase-space framing also fails. Median R/r = {median_R_over_r:.4f} "
            f"(target {PHI_SQ:.4f} ± {PHI_SQ_TOL:.0%}, FAIL); chirality consensus "
            f"{consensus_fraction:.0%} (threshold {CHIRALITY_CONSISTENCY_THRESHOLD:.0%}, FAIL). "
            f"Trapped-node-vortex picture empirically fails; deeper reframe needed."
        )

    if not persistence_ok:
        verdict += (
            f" CAVEAT: peak |ω| persistence {persistence:.0%} below {PERSISTENCE_GUARD:.0%} "
            f"threshold — Move 5 attractor may have dissolved during recording window, "
            f"corrupting phase-space measurements."
        )

    print()
    print("=" * 78, flush=True)
    print("  Dual-criterion adjudication")
    print("=" * 78, flush=True)
    print(f"  Median R_phase/r_phase = {median_R_over_r:.4f}  "
          f"(target φ²={PHI_SQ:.4f} ± {PHI_SQ_TOL:.0%}) → C1 "
          f"{'PASS' if c1_pass else 'FAIL'}")
    print(f"  Chirality consensus = {consensus_fraction:.0%} ({consensus_direction})  "
          f"(threshold {CHIRALITY_CONSISTENCY_THRESHOLD:.0%}) → C2 "
          f"{'PASS' if c2_pass else 'FAIL'}")
    print(f"  Persistence = {persistence:.0%}  (Move 5 attractor alive: "
          f"{'YES' if persistence_ok else 'NO'})")
    print()
    print(f"  Mode: {mode}")
    print(f"  Verdict: {verdict}")
    print()

    payload = {
        "pre_registration": "P_phase8_canonical_phase_space_phasor",
        "test": "Round 9 entry: doc 28 §5.1 canonical phase-space (V_inc, V_ref) phasor on Move 5 attractor",
        "N": N_LATTICE,
        "PML": PML,
        "R": R_ANCHOR,
        "r": R_MINOR,
        "phi_sq": PHI_SQ,
        "v_amp_init": V_AMP_INIT,
        "a26_amp_scale": A26_AMP_SCALE,
        "n_periods_total": N_PERIODS_TOTAL,
        "pre_evolve_end_p": PRE_EVOLVE_END_P,
        "selection_end_p": SELECTION_END_P,
        "recording_end_p": RECORDING_END_P,
        "n_recording_steps": N_RECORDING_STEPS,
        "top_k_bonds": TOP_K_BONDS,
        "sample_port": SAMPLE_PORT,
        "elapsed_seconds": elapsed_total,
        "omega_peak_init": omega_peak_init,
        "omega_peak_final": omega_peak_final,
        "persistence": persistence,
        "persistence_guard": PERSISTENCE_GUARD,
        "persistence_ok": bool(persistence_ok),
        "bonds": bond_results,
        "median_R_over_r": median_R_over_r,
        "phi_sq_target": PHI_SQ,
        "phi_sq_tolerance": PHI_SQ_TOL,
        "c1_pass": bool(c1_pass),
        "consensus_fraction": consensus_fraction,
        "consensus_direction": consensus_direction,
        "consensus_threshold": CHIRALITY_CONSISTENCY_THRESHOLD,
        "c2_pass": bool(c2_pass),
        "mode": mode,
        "verdict": verdict,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()
