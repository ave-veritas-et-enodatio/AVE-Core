"""
O.1f — (V_inc, V_ref) Quadrature Eigenmode IC Test.

Per A47 v7 corrected: `initialize_quadrature_2_3_eigenmode` (line 224 of
tlm_electron_soliton_eigenmode.py) is the doc 28-canonical eigenmode IC
that seeds BOTH V_inc and V_ref at 90° quadrature with phase-space (2,3)
winding. Every prior L3 arc test (O.1, O.1b, O.1c, O.1d, O.1e) used
V_inc-only seeder; this is the first test using the corpus-canonical
eigenmode IC.

== Pre-registered observables (per A39 v2 dual-criterion) ==

PRIMARY:
  (1) Frequency: FFT V_inc at sampled shell cells. Target ω_C if
      eigenmode is genuine corpus electron at chair-ring.
  (2) Phase-space (V_inc, V_ref) trajectory at sampled bonds traces a
      closed curve with R/r ≈ φ² (doc 28 §5.1 corpus-canonical test).

SECONDARY:
  (3) Energy retention over 50P (compare to V_inc-only IC's 39.5%)
  (4) Op10 c at end (Cosserat ω still uncoupled, expect 0)
  (5) Static residual fraction — does evolution produce coherent
      oscillation or static residual like V_inc-only IC?

== A47 v7 corrected diagnosis ==

V_inc-only seeder (initialize_2_3_voltage_ansatz):
  V_inc(t=0) = envelope · c · cos(2φ + 3ψ)   per port
  V_ref(t=0) = 0  (default, untouched)

Quadrature seeder (initialize_quadrature_2_3_eigenmode):
  V_inc(t=0) = envelope · c · cos(2φ + 3ψ)   per port
  V_ref(t=0) = envelope · c · sin(2φ + 3ψ)   per port

The 90° quadrature in V_ref encodes the L-state initial condition of the
bond LC tank — at t=0, energy is split between C-state (V_inc) and L-state
(V_ref) at quadrature, which is the corpus-canonical phase-space (2,3)
trajectory IC per doc 28 §3 + §5.1.

V_inc-only IC has V_ref=0, which is "all-C-state" (peak C-state, zero
L-state) — valid for a single bond LC tank to oscillate at ω_C, BUT
without the spatial phase quadrature pattern needed for the multi-bond
(2,3) eigenmode.

== Configuration ==

- N=48, PML=4
- Cosserat ON, A28-corrected
- temperature = 0
- IC: initialize_quadrature_2_3_eigenmode with R=8, r=4, amplitude=0.05
  (default per docstring; sub-yield at √α ≈ 0.0854)
  chirality=1.0 (default, full chirality projection — explicit electron seed)
- Run: 50 Compton periods
- Sample 5 shell-mode cells (matching O.1e for direct comparison)
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
    initialize_quadrature_2_3_eigenmode,
)


COMPTON_PERIOD = 2.0 * np.pi
DT = 1.0 / np.sqrt(2.0)
PHI = (1.0 + np.sqrt(5.0)) / 2.0
PHI_SQ = PHI * PHI


def main():
    print("=" * 78, flush=True)
    print("  O.1f — (V_inc, V_ref) Quadrature Eigenmode IC")
    print("  doc 28-canonical phase-space (2,3) IC per A47 v7 corrected")
    print("=" * 78, flush=True)

    N, PML = 48, 4
    n_steps = int(50 * COMPTON_PERIOD / DT)
    R, r = 8.0, 4.0
    amp = 0.05   # default per quadrature seeder; sub-yield

    t_start = time.time()
    engine = VacuumEngine3D.from_args(
        N=N, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )
    initialize_quadrature_2_3_eigenmode(
        engine.k4, R=R, r=r, amplitude=amp, chirality=1.0,
    )

    # IC verification — both V_inc and V_ref nonzero
    init_v_inc = engine.k4.V_inc.copy()
    init_v_ref = engine.k4.V_ref.copy()
    init_a2 = np.sum(init_v_inc ** 2 + init_v_ref ** 2, axis=-1)
    init_a2_max = float(init_a2.max())
    rms_v_inc = float(np.sqrt(np.mean(init_v_inc[engine.k4.mask_active] ** 2)))
    rms_v_ref = float(np.sqrt(np.mean(init_v_ref[engine.k4.mask_active] ** 2)))
    print(f"\n  IC verification (quadrature seeder):")
    print(f"    V_inc RMS = {rms_v_inc:.4e}")
    print(f"    V_ref RMS = {rms_v_ref:.4e}  (should be ~equal to V_inc per quadrature)")
    print(f"    A²_max(t=0) = {init_a2_max:.4f}")
    print(f"    V_ref nonzero: {'YES' if rms_v_ref > 1e-10 else 'NO (BUG: still V_inc only!)'}")

    # 5 shell-mode sample cells matching O.1e
    cx, cy, cz = (N - 1) // 2, (N - 1) // 2, (N - 1) // 2
    sample_points = []
    for phi_n, psi_n in [
        (0.0, 0.0), (np.pi/2, 0.0), (np.pi, np.pi/2),
        (3*np.pi/2, np.pi), (np.pi/4, np.pi/4),
    ]:
        x = int(round(cx + (R + r * np.cos(psi_n)) * np.cos(phi_n)))
        y = int(round(cy + (R + r * np.cos(psi_n)) * np.sin(phi_n)))
        z = int(round(cz + r * np.sin(psi_n)))
        x = max(1, min(N - 2, x)); y = max(1, min(N - 2, y)); z = max(1, min(N - 2, z))
        sample_points.append((phi_n, psi_n, x, y, z))

    print(f"\n  Sample cells:", *[f"({x},{y},{z})" for _, _, x, y, z in sample_points])

    n_samples = len(sample_points)
    v_inc_traj = np.zeros((n_samples, n_steps, 4))
    v_ref_traj = np.zeros((n_samples, n_steps, 4))
    energy_traj = []

    print(f"\n  Running {n_steps} steps...", flush=True)
    for step_i in range(n_steps):
        engine.step()
        for si, (_, _, x, y, z) in enumerate(sample_points):
            v_inc_traj[si, step_i] = engine.k4.V_inc[x, y, z, :]
            v_ref_traj[si, step_i] = engine.k4.V_ref[x, y, z, :]
        if step_i % 50 == 0:
            t_p = step_i * DT / COMPTON_PERIOD
            a2 = np.sum(engine.k4.V_inc ** 2, axis=-1)
            mask = engine.k4.mask_active
            a2_int = a2 * mask.astype(float)
            a2_int[:PML, :, :] = 0; a2_int[N-PML:, :, :] = 0
            a2_int[:, :PML, :] = 0; a2_int[:, N-PML:, :] = 0
            a2_int[:, :, :PML] = 0; a2_int[:, :, N-PML:] = 0
            e_total = float(a2_int.sum())
            energy_traj.append((t_p, e_total))
            if step_i % 100 == 0:
                print(f"    t={t_p:5.2f}P  E={e_total:.3e}  ({time.time()-t_start:.0f}s)", flush=True)

    elapsed = time.time() - t_start
    print(f"\n  Engine evolution complete in {elapsed:.0f}s")

    # PRIMARY (1): FFT post-transient
    transient_steps = int(11.0 * COMPTON_PERIOD / DT)
    target_freqs = [
        ('ω_C', 1.0),
        ('1.5·ω_C', 1.5),
        ('2.96·ω_C', 2.96),
        ('DC', 0.0),
    ]

    print(f"\n  PRIMARY (1) — FFT V_inc[port=0] post-transient:")
    print(f"  {'cell':>14} {'peak ω':>10} {'peak amp':>12}", end="")
    for name, _ in target_freqs:
        print(f" {name:>10}", end="")
    print()

    fft_per_cell = []
    for si, (phi_n, psi_n, x, y, z) in enumerate(sample_points):
        v_traj_post = v_inc_traj[si, transient_steps:, 0]
        n = len(v_traj_post)
        fft_vals = np.fft.rfft(v_traj_post)
        freqs_omega = np.fft.rfftfreq(n, d=DT) * 2.0 * np.pi
        fft_amp = 2.0 * np.abs(fft_vals) / n
        peak_idx = int(np.argmax(fft_amp))
        peak_omega = float(freqs_omega[peak_idx])
        peak_amp = float(fft_amp[peak_idx])
        target_amps = []
        for name, omega_target in target_freqs:
            idx = int(np.argmin(np.abs(freqs_omega - omega_target)))
            target_amps.append(float(fft_amp[idx]))
        print(f"  ({x:>2},{y:>2},{z:>2}) {peak_omega:>10.4f} {peak_amp:>12.4e}", end="")
        for a in target_amps:
            print(f" {a:>10.3e}", end="")
        print()
        fft_per_cell.append({
            "cell": [x, y, z], "peak_omega": peak_omega, "peak_amp": peak_amp,
            "target_amps": dict(zip([n for n, _ in target_freqs], target_amps)),
        })

    # PRIMARY (2): phase-space (V_inc, V_ref) trajectory at first cell
    # PCA aspect to estimate R/r in phase-space per doc 28 §5.1
    print(f"\n  PRIMARY (2) — phase-space (V_inc, V_ref) PCA aspect at sampled cells:")
    print(f"  Target R_phase/r_phase ≈ φ² = {PHI_SQ:.3f} (doc 28 §5.1)")
    aspects_per_cell = []
    for si, (_, _, x, y, z) in enumerate(sample_points):
        v_inc_p = v_inc_traj[si, transient_steps:, 0]
        v_ref_p = v_ref_traj[si, transient_steps:, 0]
        pts = np.stack([v_inc_p, v_ref_p], axis=1)
        pts = pts - pts.mean(axis=0, keepdims=True)
        cov = (pts.T @ pts) / max(len(pts) - 1, 1)
        evals, _ = np.linalg.eigh(cov)
        evals = np.sort(np.maximum(evals, 0.0))[::-1]
        aspect = float(np.sqrt(evals[0] / evals[1])) if evals[1] > 1e-30 else float("inf")
        aspects_per_cell.append(aspect)
        match = "★" if abs(aspect - PHI_SQ) <= 0.10 * PHI_SQ else " "
        print(f"  ({x:>2},{y:>2},{z:>2}) port=0: aspect = {aspect:>8.3f} {match}")

    # SECONDARY: energy retention
    if energy_traj:
        e_first = energy_traj[0][1]
        e_last = energy_traj[-1][1]
        retention = e_last / max(e_first, 1e-30)
        print(f"\n  Energy retention 50P: {retention:.3f} (V_inc-only IC was 0.395)")

    # Op10
    try:
        c_op10 = int(engine.cos.extract_crossing_count())
    except Exception:
        c_op10 = -1
    print(f"  Op10 c (Cosserat ω): {c_op10} (expected 0, no Cosserat seed)")

    # Verdict
    median_peak = float(np.median([r["peak_omega"] for r in fft_per_cell]))
    median_aspect = float(np.median([a for a in aspects_per_cell if not np.isinf(a)])) \
        if any(not np.isinf(a) for a in aspects_per_cell) else float("inf")

    print(f"\n  VERDICT")
    if abs(median_peak - 1.0) < 0.05:
        freq_verdict = "PASS at ω_C — corpus electron candidate"
    elif abs(median_peak - 1.5) < 0.15:
        freq_verdict = "Substrate ℓ=2 cavity mode (A38)"
    elif abs(median_peak - 2.96) < 0.30:
        freq_verdict = "Substrate ℓ=5 cavity mode"
    elif abs(median_peak) < 0.05:
        freq_verdict = "DC dominated — quasi-static residual (same as V_inc-only IC)"
    else:
        freq_verdict = f"Other ω = {median_peak:.4f}"

    print(f"  Frequency: median peak ω = {median_peak:.4f} → {freq_verdict}")
    if not np.isinf(median_aspect):
        aspect_match = abs(median_aspect - PHI_SQ) <= 0.10 * PHI_SQ
        print(f"  Topology: median R/r aspect = {median_aspect:.3f} (target φ²={PHI_SQ:.3f}): "
              f"{'PASS' if aspect_match else 'FAIL'}")

    out = {
        "test": "O.1f: quadrature eigenmode IC",
        "config": {"N": N, "amp": amp, "R": R, "r": r, "chirality": 1.0},
        "ic_verification": {"v_inc_rms": rms_v_inc, "v_ref_rms": rms_v_ref,
                            "a2_max_t0": init_a2_max},
        "fft_per_cell": fft_per_cell,
        "phase_space_aspects": aspects_per_cell,
        "median_peak_omega": median_peak,
        "median_aspect": median_aspect if not np.isinf(median_aspect) else None,
        "phi_squared_target": PHI_SQ,
        "energy_retention_50P": retention,
        "c_op10": int(c_op10),
        "elapsed_total_s": float(elapsed),
    }
    out_path = Path(__file__).parent / "r10_v8_o1f_quadrature_eigenmode_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
