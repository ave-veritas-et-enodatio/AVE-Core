"""Move 7 / Phase 1 — Characterize Move 5's settled (2,3) attractor as itself.

Per `P_phase1_attractor_characterization` (frozen at this commit).

PIVOT FROM PRIOR PATTERN (per audit on Move 6):
  Round 7 + §10 + Move 5 + Move 6 ran ≥9 distinct configurations all
  pre-registered as "is corpus electron at config X?" — all returned
  Mode III. The accumulated signal is "engine doesn't produce
  corpus-electron-shaped object at any pre-specifiable corpus-claimed
  configuration." Continuing to specify configurations elaborates the
  same finding at higher resolution.

  Move 7 inverts the question: the engine produced a system-found stable
  c=3 attractor at t=200P. We extracted persistence + binary verdict
  but never characterized what kind of object it is. This driver does
  the descriptive characterization with a frozen extraction scope —
  NO PASS/FAIL adjudication. The result IS the characterization.

FROZEN EXTRACTIONS (5):

  (1) SPATIAL MOMENTS at t=200P:
      Centroid (cx, cy, cz) of |ω|² and V_inc² density.
      Second moments (extent_x, extent_y, extent_z) for each.
      Total energy (Cosserat potential + kinetic, K4 V-pressure proxy).

  (2) FFT AT 5 FIXED SPATIAL POINTS over t∈[150P, 200P]:
      Centroid + 4 displaced points (±2 cells in x and y).
      V_inc(t) port-0 sum and ω(t) magnitude at each point.
      Top 3 frequencies (rad / natural-time-unit) per point per signal.

  (3) Q-FACTOR from log-decay over t∈[10P, 50P]:
      Linear fit to log(peak |ω|) vs t.
      Slope → 1/τ. Q = ω_C · τ / 2 if assuming ω_C oscillation.
      Also report τ in Compton periods (frequency-agnostic decay timescale).

  (4) (V_inc, V_ref) PHASOR TRAJECTORY at centroid over t∈[150P, 200P]:
      Record V_inc[centroid, port=0](t) and V_ref[centroid, port=0](t).
      PCA-aspect ratio R/r (descriptive only — NO comparison to φ²).
      Closed-trajectory diagnostic (amplitude drift over 5 chunks).

  (5) ENERGY PARTITION at t=200P:
      Cosserat: total_energy() (potential V), kinetic_energy() (T = ½ρ|u̇|² + ½I|ω̇|²).
      Per-sector amplitude proxies:
        ω-sector: sum(|ω|²)
        u-sector: sum(|u|²)
        V-sector: sum(|V_inc|²) at active K4 sites
      No corpus-comparison; just where energy lives.

POST-EXTRACTION DECISION (Phase 2, NOT in this run):
  Based on the 5 extracted properties, decide which branch:
    (a) electron-like: Q ≈ 137, dominant freq at ω_C or simple multiple,
        c=3, energy ~ m_e c² in natural units
    (b) (2,3)-topological but not electron-like (different Q or freq)
    (c) none of the above (engine missing physics, OR corpus claim about
        engine-electron correspondence wrong)
  Each branch implies different Round 8+ next move.
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


# ─── Constants (match Move 5 + 6 exactly for deterministic reproduction) ─────

PHI = 0.5 * (1.0 + np.sqrt(5.0))
PHI_SQ = PHI * PHI

N_LATTICE = 32
PML = 4
R_ANCHOR = 10.0
R_MINOR = R_ANCHOR / PHI_SQ                      # ≈ 3.82

A26_AMP_SCALE = 0.3 / (np.sqrt(3.0) / 2.0)
GT_PEAK_OMEGA = 0.3 * np.pi
V_AMP_INIT = 0.14

OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi / OMEGA_C
N_PERIODS_TOTAL = 200.0
DT = 1.0 / np.sqrt(2.0)
N_STEPS = int(N_PERIODS_TOTAL * COMPTON_PERIOD / DT) + 1

# Recording windows
T_DECAY_START_PERIOD = 10.0
T_DECAY_END_PERIOD = 50.0
T_FFT_START_PERIOD = 150.0
T_FFT_END_PERIOD = 200.0

STEP_DECAY_START = int(T_DECAY_START_PERIOD * COMPTON_PERIOD / DT)
STEP_DECAY_END = int(T_DECAY_END_PERIOD * COMPTON_PERIOD / DT)
STEP_FFT_START = int(T_FFT_START_PERIOD * COMPTON_PERIOD / DT)
STEP_FFT_END = N_STEPS

OUTPUT_JSON = Path(__file__).parent / "r8_phase1_attractor_characterization_results.json"


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


# ─── Extraction (1): spatial moments ─────────────────────────────────────────

def spatial_moments(field_density):
    """Centroid + per-axis std dev (sqrt of second central moment) of a 3D density."""
    nx, ny, nz = field_density.shape
    total = float(field_density.sum())
    if total <= 0:
        return None
    i, j, k = np.indices((nx, ny, nz))
    norm = field_density / total
    cx = float(np.sum(i * norm))
    cy = float(np.sum(j * norm))
    cz = float(np.sum(k * norm))
    var_x = float(np.sum((i - cx) ** 2 * norm))
    var_y = float(np.sum((j - cy) ** 2 * norm))
    var_z = float(np.sum((k - cz) ** 2 * norm))
    return {
        "centroid": [cx, cy, cz],
        "extent": [float(np.sqrt(var_x)), float(np.sqrt(var_y)), float(np.sqrt(var_z))],
        "extent_total": float(np.sqrt(var_x + var_y + var_z)),
        "total": total,
    }


# ─── Extraction (5): energy partition ────────────────────────────────────────

def measure_energy_partition(engine):
    """Cosserat potential + kinetic + amplitude-proxy partition."""
    # Engine-provided
    V_cos = float(engine.cos.total_energy())
    T_cos = float(engine.cos.kinetic_energy())
    H_cos = V_cos + T_cos

    # Amplitude proxies (no corpus comparison)
    omega = np.asarray(engine.cos.omega)
    u = np.asarray(engine.cos.u)
    v_inc = np.asarray(engine.k4.V_inc)
    mask_alive = np.asarray(engine.cos.mask_alive)
    mask_active_k4 = np.asarray(engine.k4.mask_active)

    omega_sq = float(np.sum((omega * mask_alive[..., None]) ** 2))
    u_sq = float(np.sum((u * mask_alive[..., None]) ** 2))
    vinc_sq = float(np.sum((v_inc * mask_active_k4[..., None]) ** 2))

    return {
        "cosserat_potential_V": V_cos,
        "cosserat_kinetic_T": T_cos,
        "cosserat_hamiltonian_H": H_cos,
        "amplitude_proxy_omega_sq": omega_sq,
        "amplitude_proxy_u_sq": u_sq,
        "amplitude_proxy_vinc_sq": vinc_sq,
    }


# ─── Extraction (2)+(3)+(4): time-series + FFT helpers ───────────────────────

def select_5_fixed_points(centroid, nx):
    """Centroid + 4 displaced points (±2 cells in x and y)."""
    cx_int = int(round(centroid[0]))
    cy_int = int(round(centroid[1]))
    cz_int = int(round(centroid[2]))

    def clip(v):
        return int(max(2, min(nx - 3, v)))

    return [
        (clip(cx_int), clip(cy_int), clip(cz_int)),
        (clip(cx_int + 2), clip(cy_int), clip(cz_int)),
        (clip(cx_int - 2), clip(cy_int), clip(cz_int)),
        (clip(cx_int), clip(cy_int + 2), clip(cz_int)),
        (clip(cx_int), clip(cy_int - 2), clip(cz_int)),
    ]


def fft_top_freqs(signal, dt, n_top=3):
    """FFT a real signal; return top-n peak (omega_natural, power) tuples."""
    if len(signal) < 4:
        return []
    s = np.asarray(signal) - np.mean(signal)
    fft_power = np.abs(np.fft.rfft(s)) ** 2
    freqs = np.fft.rfftfreq(len(s), d=dt)
    idx = np.argsort(fft_power)[::-1]
    top = []
    for i in idx:
        if freqs[i] > 0:
            omega_natural = 2.0 * np.pi * float(freqs[i])
            top.append([omega_natural, float(fft_power[i])])
        if len(top) >= n_top:
            break
    return top


def main():
    print("=" * 78, flush=True)
    print(f"  Move 7 / Phase 1 — Attractor characterization (Move 5 settled state)")
    print(f"  P_phase1_attractor_characterization (frozen extraction; no PASS/FAIL)")
    print("=" * 78, flush=True)
    print(f"  Lattice N={N_LATTICE}, deterministic Move 5 reproduction")
    print(f"  Decay window for Q-fit:  t∈[{T_DECAY_START_PERIOD}, "
          f"{T_DECAY_END_PERIOD}] Compton periods")
    print(f"  FFT/phasor window:       t∈[{T_FFT_START_PERIOD}, "
          f"{T_FFT_END_PERIOD}] Compton periods")
    print()

    engine = build_engine()
    seed_corpus_2_3_joint(engine)

    # ─── Run + record ─────────────────────────────────────────────────────────
    decay_stream = []        # peak |ω|, t — for Q-fit
    fft_step_stream = []     # raw V_inc, ω at 5 fixed points — for FFT
    fft_step_indices = []
    final_omega = None
    final_v_inc = None
    final_state_snapshot = None

    # We need to know centroid before recording at 5 fixed points.
    # Strategy: do a first-pass run to get t=200P snapshot for centroid,
    # then second-pass run to record at the 5 cells. Move 5 dynamics are
    # deterministic so this reproduces. Two ~5-min runs = ~10 min total.

    print(f"  Pass 1: run to t={N_PERIODS_TOTAL}P to extract centroid…")
    t0 = time.time()
    last_progress = t0
    for step in range(1, N_STEPS + 1):
        engine.step()
        if STEP_DECAY_START <= step <= STEP_DECAY_END:
            omega = np.asarray(engine.cos.omega)
            peak_om = float(np.linalg.norm(omega, axis=-1).max())
            decay_stream.append({
                "step": int(step),
                "t_period": float(step * DT / COMPTON_PERIOD),
                "peak_omega": peak_om,
            })
        if (time.time() - last_progress) > 30.0:
            t_p = step * DT / COMPTON_PERIOD
            print(f"    [progress P1] step {step}, t={t_p:.1f}P, "
                  f"elapsed {time.time() - t0:.1f}s", flush=True)
            last_progress = time.time()
    elapsed_p1 = time.time() - t0
    print(f"  Pass 1 complete: {elapsed_p1:.1f}s")

    final_omega = np.asarray(engine.cos.omega).copy()
    final_v_inc = np.asarray(engine.k4.V_inc).copy()
    final_u = np.asarray(engine.cos.u).copy()
    final_state_snapshot = measure_energy_partition(engine)

    # ─── Extraction (1): spatial moments at t=200P ───────────────────────────
    print()
    print(f"  (1) SPATIAL MOMENTS at t=200P")
    omega_density = np.sum(final_omega ** 2, axis=-1)
    vinc_density = np.sum(final_v_inc ** 2, axis=-1)
    u_density = np.sum(final_u ** 2, axis=-1)

    moments_omega = spatial_moments(omega_density)
    moments_vinc = spatial_moments(vinc_density)
    moments_u = spatial_moments(u_density)

    print(f"    |ω|² centroid: ({moments_omega['centroid'][0]:.2f}, "
          f"{moments_omega['centroid'][1]:.2f}, {moments_omega['centroid'][2]:.2f})")
    print(f"    |ω|² extent:   ({moments_omega['extent'][0]:.2f}, "
          f"{moments_omega['extent'][1]:.2f}, {moments_omega['extent'][2]:.2f})  "
          f"total={moments_omega['extent_total']:.2f}")
    print(f"    V_inc² centroid: ({moments_vinc['centroid'][0]:.2f}, "
          f"{moments_vinc['centroid'][1]:.2f}, {moments_vinc['centroid'][2]:.2f})")
    print(f"    V_inc² extent: ({moments_vinc['extent'][0]:.2f}, "
          f"{moments_vinc['extent'][1]:.2f}, {moments_vinc['extent'][2]:.2f})  "
          f"total={moments_vinc['extent_total']:.2f}")
    print(f"    |u|² centroid: ({moments_u['centroid'][0]:.2f}, "
          f"{moments_u['centroid'][1]:.2f}, {moments_u['centroid'][2]:.2f})")
    print(f"    |u|² extent total: {moments_u['extent_total']:.2f}")
    print()

    # ─── Pick 5 fixed points based on omega centroid ─────────────────────────
    five_points = select_5_fixed_points(moments_omega['centroid'], N_LATTICE)
    print(f"  5 fixed points (around |ω|² centroid):")
    for idx, p in enumerate(five_points):
        print(f"    P{idx}: cell {p}")
    print()

    # ─── Pass 2: re-run, record at 5 fixed points during FFT window ──────────
    print(f"  Pass 2: re-run with recording at 5 fixed points "
          f"in t∈[{T_FFT_START_PERIOD}, {T_FFT_END_PERIOD}]P…")
    engine = build_engine()
    seed_corpus_2_3_joint(engine)

    five_point_v_inc_traces = [[] for _ in five_points]   # port 0 sum proxy
    five_point_v_ref_traces = [[] for _ in five_points]
    five_point_omega_traces = [[] for _ in five_points]   # |ω| at point
    centroid_vinc_p0 = []
    centroid_vref_p0 = []
    fft_step_indices = []

    t0 = time.time()
    last_progress = t0
    for step in range(1, N_STEPS + 1):
        engine.step()
        if STEP_FFT_START <= step <= STEP_FFT_END:
            for pi, (ix, iy, iz) in enumerate(five_points):
                v_inc_at_pt = engine.k4.V_inc[ix, iy, iz, :]
                v_ref_at_pt = engine.k4.V_ref[ix, iy, iz, :]
                # Use sum across 4 ports as the "phasor pressure" at this cell
                five_point_v_inc_traces[pi].append(float(np.sum(v_inc_at_pt)))
                five_point_v_ref_traces[pi].append(float(np.sum(v_ref_at_pt)))
                five_point_omega_traces[pi].append(float(np.linalg.norm(
                    engine.cos.omega[ix, iy, iz, :])))
            # Centroid point P0 port-0 trace for phasor trajectory
            ix, iy, iz = five_points[0]
            centroid_vinc_p0.append(float(engine.k4.V_inc[ix, iy, iz, 0]))
            centroid_vref_p0.append(float(engine.k4.V_ref[ix, iy, iz, 0]))
            fft_step_indices.append(int(step))
        if (time.time() - last_progress) > 30.0:
            t_p = step * DT / COMPTON_PERIOD
            print(f"    [progress P2] step {step}, t={t_p:.1f}P, "
                  f"elapsed {time.time() - t0:.1f}s", flush=True)
            last_progress = time.time()
    elapsed_p2 = time.time() - t0
    print(f"  Pass 2 complete: {elapsed_p2:.1f}s, "
          f"{len(fft_step_indices)} FFT samples per point")
    print()

    # ─── Extraction (2): FFT at 5 fixed points ───────────────────────────────
    print(f"  (2) FFT AT 5 FIXED POINTS over t∈[{T_FFT_START_PERIOD}, "
          f"{T_FFT_END_PERIOD}]P  (top freqs in natural-units ω):")
    fft_results = []
    for pi, p in enumerate(five_points):
        v_inc_top = fft_top_freqs(five_point_v_inc_traces[pi], DT, n_top=3)
        omega_top = fft_top_freqs(five_point_omega_traces[pi], DT, n_top=3)
        fft_results.append({
            "point_idx": pi,
            "cell": list(p),
            "v_inc_top_omega_natural": v_inc_top,
            "omega_top_omega_natural": omega_top,
        })
        v_inc_str = ", ".join(f"{w:.4f}" for w, _ in v_inc_top)
        omega_str = ", ".join(f"{w:.4f}" for w, _ in omega_top)
        print(f"    P{pi} {p}: V_inc top ω = [{v_inc_str}], "
              f"|ω| top ω = [{omega_str}]")
    print()

    # ─── Extraction (3): Q-factor from log-decay fit ─────────────────────────
    print(f"  (3) Q-FACTOR from log-decay over t∈[{T_DECAY_START_PERIOD}, "
          f"{T_DECAY_END_PERIOD}]P")
    if len(decay_stream) >= 4:
        ts_periods = np.array([d["t_period"] for d in decay_stream])
        peak_oms = np.array([d["peak_omega"] for d in decay_stream])
        # Linear fit: log(peak_om) = log(A) - t / tau
        valid = peak_oms > 1e-10
        if valid.sum() >= 4:
            log_om = np.log(peak_oms[valid])
            ts_v = ts_periods[valid]
            slope, intercept = np.polyfit(ts_v, log_om, 1)
            tau_periods = -1.0 / slope if slope < 0 else float("inf")
            tau_natural = tau_periods * COMPTON_PERIOD  # in natural-time-units
            Q_at_omega_C = 0.5 * OMEGA_C * tau_natural if np.isfinite(tau_natural) else None
        else:
            tau_periods = float("inf")
            Q_at_omega_C = None
            slope = None
            intercept = None
    else:
        tau_periods = float("inf")
        Q_at_omega_C = None
        slope = None
        intercept = None

    print(f"    log(peak |ω|) slope: {slope}")
    print(f"    τ (Compton periods): {tau_periods:.4f}")
    print(f"    Q at ω_C = ω_C·τ/2: {Q_at_omega_C}")
    print()

    # ─── Extraction (4): (V_inc, V_ref) phasor trajectory at centroid ────────
    print(f"  (4) (V_inc, V_ref) PHASOR TRAJECTORY at centroid P0 over "
          f"t∈[{T_FFT_START_PERIOD}, {T_FFT_END_PERIOD}]P")
    if len(centroid_vinc_p0) >= 8:
        v_inc_arr = np.array(centroid_vinc_p0)
        v_ref_arr = np.array(centroid_vref_p0)
        pts = np.column_stack([v_inc_arr - v_inc_arr.mean(),
                                v_ref_arr - v_ref_arr.mean()])
        cov = np.cov(pts.T)
        evals, _ = np.linalg.eigh(cov)
        evals = np.sort(evals)[::-1]
        R_phasor = float(np.sqrt(max(evals[0], 0)))
        r_phasor = float(np.sqrt(max(evals[1], 0)))
        R_over_r_phasor = R_phasor / max(r_phasor, 1e-30)

        # Closed-trajectory diagnostic over 5 chunks
        chunks = 5
        chunk_size = len(v_inc_arr) // chunks
        chunk_R = []
        for ci in range(chunks):
            cinc = v_inc_arr[ci * chunk_size:(ci + 1) * chunk_size]
            cref = v_ref_arr[ci * chunk_size:(ci + 1) * chunk_size]
            if len(cinc) >= 3:
                chunk_R.append(float(np.sqrt(np.var(cinc) + np.var(cref))))
        amp_drift = float(np.std(chunk_R) / max(np.mean(chunk_R), 1e-30)) if chunk_R else float("inf")

        print(f"    Centroid P0 V_inc range: [{v_inc_arr.min():.4f}, "
              f"{v_inc_arr.max():.4f}]  mean={v_inc_arr.mean():.4f}")
        print(f"    Centroid P0 V_ref range: [{v_ref_arr.min():.4f}, "
              f"{v_ref_arr.max():.4f}]  mean={v_ref_arr.mean():.4f}")
        print(f"    PCA aspect R/r (descriptive): {R_over_r_phasor:.4f}")
        print(f"    Amplitude drift over 5 chunks: {amp_drift:.4f}")
    else:
        R_phasor = r_phasor = R_over_r_phasor = amp_drift = float("nan")
        print(f"    Insufficient samples for phasor analysis")
    print()

    # ─── Extraction (5): energy partition at t=200P (already measured) ──────
    print(f"  (5) ENERGY PARTITION at t=200P")
    print(f"    Cosserat potential V: {final_state_snapshot['cosserat_potential_V']:.6e}")
    print(f"    Cosserat kinetic T:   {final_state_snapshot['cosserat_kinetic_T']:.6e}")
    print(f"    Cosserat H = V + T:   {final_state_snapshot['cosserat_hamiltonian_H']:.6e}")
    print(f"    Σ|ω|²:                {final_state_snapshot['amplitude_proxy_omega_sq']:.6e}")
    print(f"    Σ|u|²:                {final_state_snapshot['amplitude_proxy_u_sq']:.6e}")
    print(f"    Σ|V_inc|²:            {final_state_snapshot['amplitude_proxy_vinc_sq']:.6e}")
    print()

    # ─── Topology check at t=200P ────────────────────────────────────────────
    c_final = int(engine.cos.extract_crossing_count())
    peak_omega_final = float(np.linalg.norm(np.asarray(engine.cos.omega), axis=-1).max())
    print(f"  Sanity (t=200P): c via Op10 = {c_final}, peak |ω| = {peak_omega_final:.4f}")
    print()

    # ─── Save full extraction payload ────────────────────────────────────────
    payload = {
        "pre_registration": "P_phase1_attractor_characterization",
        "test": "Move 7 / Phase 1 — descriptive characterization, no PASS/FAIL",
        "N": N_LATTICE,
        "n_periods_total": N_PERIODS_TOTAL,
        "elapsed_seconds_pass1": elapsed_p1,
        "elapsed_seconds_pass2": elapsed_p2,

        "extraction_1_spatial_moments": {
            "omega_density": moments_omega,
            "vinc_density": moments_vinc,
            "u_density": moments_u,
        },
        "five_fixed_points": [list(p) for p in five_points],
        "extraction_2_fft_at_5_points": fft_results,
        "extraction_3_q_factor": {
            "n_decay_samples": len(decay_stream),
            "decay_stream_window_periods": [T_DECAY_START_PERIOD, T_DECAY_END_PERIOD],
            "log_slope_per_period": float(slope) if slope is not None else None,
            "tau_compton_periods": float(tau_periods) if np.isfinite(tau_periods) else None,
            "Q_at_omega_C": float(Q_at_omega_C) if Q_at_omega_C is not None else None,
            "decay_stream": decay_stream,
        },
        "extraction_4_phasor_at_centroid": {
            "n_samples": len(centroid_vinc_p0),
            "centroid_p0_cell": list(five_points[0]),
            "v_inc_p0_min": float(min(centroid_vinc_p0)) if centroid_vinc_p0 else None,
            "v_inc_p0_max": float(max(centroid_vinc_p0)) if centroid_vinc_p0 else None,
            "v_inc_p0_mean": float(np.mean(centroid_vinc_p0)) if centroid_vinc_p0 else None,
            "v_ref_p0_min": float(min(centroid_vref_p0)) if centroid_vref_p0 else None,
            "v_ref_p0_max": float(max(centroid_vref_p0)) if centroid_vref_p0 else None,
            "v_ref_p0_mean": float(np.mean(centroid_vref_p0)) if centroid_vref_p0 else None,
            "R_phasor_pca": R_phasor if isinstance(R_phasor, float) else None,
            "r_phasor_pca": r_phasor if isinstance(r_phasor, float) else None,
            "R_over_r_phasor_pca": R_over_r_phasor if isinstance(R_over_r_phasor, float) else None,
            "amp_drift_5_chunks": amp_drift if isinstance(amp_drift, float) else None,
        },
        "extraction_5_energy_partition": final_state_snapshot,
        "topology_at_t_final": {
            "c_via_Op10": c_final,
            "peak_omega": peak_omega_final,
        },
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()
