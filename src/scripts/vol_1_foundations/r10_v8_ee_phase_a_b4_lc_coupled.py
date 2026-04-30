"""
r10 EE Phase A — Control B4: LC-coupled re-run (disable_cosserat_lc_force=False).

The corpus-electron test that v6→v10 has never actually run. The (1,1)
Beltrami eigenmode requires A∥B parallelism, which requires V↔ω LC
coupling — the wire snipped by `disable_cosserat_lc_force=True` in v8.
With LC coupling enabled, V and ω sectors lock through Maxwell-Heaviside
coupling, and the system finds its self-consistent eigenmode.

IC: same v8 helical Beltrami (V_inc cos pattern + ω = k·A_0 Beltrami
eigenvector) — NOT V_inc=0 Phase A which v7 found doesn't evolve. The
v7 failure was about IC starvation, not about LC coupling itself.

Captures everything Phase A needs:
  - V_inc, V_ref, Phi_link at ring nodes (FFT + power split + Faraday)
  - ω, ω_dot, u_dot at ring nodes (FFT + Beltrami test)
  - S_field, z_local at ring nodes (impedance landscape)
  - ω at chair-ring centroid (Faraday Φ_B integration)

Tests:
  T1 — does V-sector FFT shift from 1.48·ω_C (ℓ=2 GW-analog) to
       something else (e.g., ℓ=1 corpus electron at 0.775·ω_C)?
  T2 — does ω-sector FFT lock to V-sector frequency?
  T3 — does Beltrami |cos_sim(A_AC, ω_AC)| → 1 with LC coupling on?
  T4 — does S_field per ring node show a different ℓ pattern (e.g., ℓ=1
       uniform with one antinode, vs ℓ=2 quadrupole with 2 antinodes)?
  T5 — does ∮V·dl + dΦ_B/dt = 0 (Faraday's law restored)?
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).parent))

from ave.topological.vacuum_engine import VacuumEngine3D

import r10_path_alpha_v8_corrected_measurements as v8


def main():
    print("=" * 78, flush=True)
    print("  r10 EE Phase A — Control B4: LC-coupled re-run")
    print("  disable_cosserat_lc_force = False  (the wire is reconnected)")
    print("=" * 78, flush=True)

    nodes, bonds = v8.build_chair_ring(v8.CENTER)
    a_0_per_node, centroid = v8.compute_a_0_at_ring_nodes(
        nodes, v8.A_AMP_POL, v8.HELICAL_PITCH
    )

    engine = VacuumEngine3D.from_args(
        N=v8.N_LATTICE, pml=v8.PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=False,  # ← THE KEY CHANGE
        enable_cosserat_self_terms=True,
    )

    print("Applying v8 helical Beltrami IC (UNCHANGED IC; only engine config changes)...",
          flush=True)
    v8.initialize_helical_beltrami_ic(
        engine, nodes, bonds, a_0_per_node,
        v8.K_BELTRAMI, v8.V_AMP, v8.PHI_AMP,
    )

    omega_per_node_ic = np.array([engine.cos.omega[n[0], n[1], n[2], :].copy()
                                   for n in nodes])
    beltrami_ic_cos_sims = v8.beltrami_eigenvector_sanity_check(
        a_0_per_node, omega_per_node_ic, v8.K_BELTRAMI
    )
    print(f"  Beltrami IC sanity (ω vs k·A_0): {[f'{c:+.4f}' for c in beltrami_ic_cos_sims]}")

    # Pre-flight: 1-step smoke test
    print("Pre-flight: 1-step smoke test...", flush=True)
    pre_v_inc_max = float(np.max(np.abs(engine.k4.V_inc)))
    pre_omega_max = float(np.max(np.abs(engine.cos.omega)))
    engine.step()
    post_v_inc_max = float(np.max(np.abs(engine.k4.V_inc)))
    post_omega_max = float(np.max(np.abs(engine.cos.omega)))
    print(f"  V_inc max: {pre_v_inc_max:.4e} → {post_v_inc_max:.4e}")
    print(f"  ω max:     {pre_omega_max:.4e} → {post_omega_max:.4e}")
    if post_v_inc_max < 1e-10:
        print("  ⚠ V_inc collapsed to ~0 after 1 step — LC coupling may be unstable")
    if post_omega_max < 1e-10:
        print("  ⚠ ω collapsed to ~0 after 1 step")

    # Re-initialize for clean recording
    print("Re-initializing for clean recording...", flush=True)
    engine = VacuumEngine3D.from_args(
        N=v8.N_LATTICE, pml=v8.PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=False,
        enable_cosserat_self_terms=True,
    )
    v8.initialize_helical_beltrami_ic(
        engine, nodes, bonds, a_0_per_node,
        v8.K_BELTRAMI, v8.V_AMP, v8.PHI_AMP,
    )

    N_STEPS = v8.N_RECORDING_STEPS
    print(f"Recording {N_STEPS} steps...", flush=True)

    v_inc = np.zeros((N_STEPS, 6, 4), dtype=np.float32)
    v_ref = np.zeros((N_STEPS, 6, 4), dtype=np.float32)
    phi_link = np.zeros((N_STEPS, 6, 4), dtype=np.float32)
    omega = np.zeros((N_STEPS, 6, 3), dtype=np.float32)
    omega_dot = np.zeros((N_STEPS, 6, 3), dtype=np.float32)
    u_dot = np.zeros((N_STEPS, 6, 3), dtype=np.float32)
    s_field = np.zeros((N_STEPS, 6), dtype=np.float32)
    z_local = np.zeros((N_STEPS, 6), dtype=np.float32)

    cx, cy, cz = v8.CENTER
    centroid_int = (int(round(centroid[0])), int(round(centroid[1])), int(round(centroid[2])))
    interior_omega = np.zeros((N_STEPS, 3), dtype=np.float32)

    # Track A²_mean and ring localization for sanity
    A2_mean_traj = np.zeros(N_STEPS)

    t0 = time.time()
    last = t0
    for i in range(N_STEPS):
        engine.step()
        for n_idx, node in enumerate(nodes):
            ix, iy, iz = node
            v_inc[i, n_idx, :] = engine.k4.V_inc[ix, iy, iz, :]
            v_ref[i, n_idx, :] = engine.k4.V_ref[ix, iy, iz, :]
            phi_link[i, n_idx, :] = engine.k4.Phi_link[ix, iy, iz, :]
            omega[i, n_idx, :] = engine.cos.omega[ix, iy, iz, :]
            omega_dot[i, n_idx, :] = engine.cos.omega_dot[ix, iy, iz, :]
            u_dot[i, n_idx, :] = engine.cos.u_dot[ix, iy, iz, :]
            s_field[i, n_idx] = engine.k4.S_field[ix, iy, iz]
            z_local[i, n_idx] = engine.k4.z_local_field[ix, iy, iz]
        interior_omega[i, :] = engine.cos.omega[centroid_int[0], centroid_int[1], centroid_int[2], :]

        s_v8 = v8.measure_ring_state_v8(engine, nodes)
        A2_mean_traj[i] = s_v8["A2_mean"]

        if (time.time() - last) > 30.0:
            t_p = (i + 1) * v8.DT / v8.COMPTON_PERIOD
            print(f"    step {i}/{N_STEPS}, t={t_p:.1f}P, A²={s_v8['A2_mean']:.3f}, "
                  f"loc={s_v8['ring_localization']:.3f}, elapsed {time.time()-t0:.1f}s",
                  flush=True)
            last = time.time()
    elapsed = time.time() - t0
    print(f"  Recording done at {elapsed:.1f}s", flush=True)

    sw_start = N_STEPS // 4
    print(f"\nSteady-state window: steps [{sw_start}, {N_STEPS}) ({N_STEPS - sw_start} samples)")
    print(f"  A²_mean steady: {A2_mean_traj[sw_start:].mean():.4f}")
    print(f"  Persistence (A²_mean ≥ 0.5): {sum(A2_mean_traj >= 0.5) * v8.DT / v8.COMPTON_PERIOD:.1f} P")

    # ── T1+T2: FFT V_inc and ω at ring node 0 ─────────────────────────────
    v_inc_n0 = np.linalg.norm(v_inc[sw_start:, 0, :], axis=1)
    omega_n0 = np.linalg.norm(omega[sw_start:, 0, :], axis=1)
    n_samples = len(v_inc_n0)
    freqs = np.fft.rfftfreq(n_samples, d=v8.DT)
    f_C = 1.0 / (2 * np.pi)

    def fft_mag(x):
        return np.abs(np.fft.rfft(x - x.mean()))

    def find_peaks(spec, k=5):
        idxs = np.argsort(spec)[::-1][:k]
        return [(int(i), float(freqs[i]), float(spec[i])) for i in idxs]

    fft_v = fft_mag(v_inc_n0)
    fft_w = fft_mag(omega_n0)
    v_peaks = find_peaks(fft_v)
    w_peaks = find_peaks(fft_w)

    print()
    print("  T1+T2 — FFT (post-transient):")
    print(f"    V_inc top-5 peaks (idx, f, mag, f/f_C):")
    for p in v_peaks:
        print(f"      idx={p[0]:5d}, f={p[1]:.5f}, mag={p[2]:.3e}, ratio={p[1]/f_C:.4f}")
    print(f"    ω top-5 peaks (idx, f, mag, f/f_C):")
    for p in w_peaks:
        print(f"      idx={p[0]:5d}, f={p[1]:.5f}, mag={p[2]:.3e}, ratio={p[1]/f_C:.4f}")

    # ── T3: Beltrami |cos_sim(A_AC, ω_AC)| ────────────────────────────────
    # Compute A_AC from Phi_link detrending (v8 method) and ω_AC = ω - mean(ω)
    def detrend(traj):
        t = np.arange(traj.shape[0], dtype=np.float64)
        t_mean = t.mean()
        t_var = ((t - t_mean) ** 2).sum()
        mean = traj.mean(axis=0)
        slope_num = ((t.reshape((-1,) + (1,)*(traj.ndim - 1)) - t_mean)
                     * (traj - mean[None, ...])).sum(axis=0)
        slope = slope_num / t_var
        intercept = mean - slope * t_mean
        return traj - intercept[None, ...] - slope[None, ...] * t.reshape(
            (-1,) + (1,)*(traj.ndim - 1)
        )

    phi_oscillating = detrend(phi_link.astype(np.float64))
    omega_DC = omega.mean(axis=0)
    omega_AC = omega - omega_DC[None, :, :]

    # A vector reconstruction from ring-node phi_oscillating (4-port → 3D Moore-Penrose)
    PORT_DIRS = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]],
                          dtype=np.float64) / np.sqrt(3.0)
    bond_length_lnode = np.sqrt(3.0)

    cos_sim_AC = np.zeros(N_STEPS)
    for i in range(N_STEPS):
        sims = []
        for n_idx in range(6):
            a_vec = np.zeros(3, dtype=np.float64)
            for p in range(4):
                a_vec += PORT_DIRS[p] * phi_oscillating[i, n_idx, p] / bond_length_lnode
            a_vec *= (3.0 / 4.0)  # Moore-Penrose
            b_vec = omega_AC[i, n_idx, :].astype(np.float64)
            a_norm, b_norm = np.linalg.norm(a_vec), np.linalg.norm(b_vec)
            if a_norm < 1e-12 or b_norm < 1e-12:
                sims.append(0.0)
            else:
                sims.append(float(np.dot(a_vec, b_vec) / (a_norm * b_norm)))
        cos_sim_AC[i] = float(np.mean(np.abs(sims)))
    cos_sim_AC_steady = float(cos_sim_AC[sw_start:].mean())

    print()
    print(f"  T3 — Beltrami |cos_sim(A_AC, ω_AC)| steady: {cos_sim_AC_steady:.4f}")
    print(f"        (v8 baseline: 0.5151. → 1.0 = perfect Beltrami parallelism with LC coupling)")
    if cos_sim_AC_steady > 0.8:
        print(f"        ✓ PASS Beltrami threshold — A∥B parallelism achieved with LC coupling")
    elif cos_sim_AC_steady > 0.6:
        print(f"        ↗ improvement over v8 (0.515) but below 0.8 threshold")
    else:
        print(f"        ↘ no significant change from v8 baseline")

    # ── T4: S_field azimuthal Fourier ─────────────────────────────────────
    s_mean = s_field[sw_start:].mean(axis=0)
    azimuth = 2 * np.pi * np.arange(6) / 6
    s_fourier = []
    for ell in range(4):
        c_ell = float(np.sum(s_mean * np.cos(ell * azimuth)) / 6.0)
        s_ell = float(np.sum(s_mean * np.sin(ell * azimuth)) / 6.0)
        amp = float(np.sqrt(c_ell**2 + s_ell**2) * (1 if ell == 0 else 2))
        s_fourier.append({"ell": ell, "cos": c_ell, "sin": s_ell, "amp": amp})

    print()
    print("  T4 — S_field per ring node + azimuthal Fourier:")
    for n_idx in range(6):
        node_type = "A" if all(c % 2 == 0 for c in nodes[n_idx]) else "B"
        print(f"    node {n_idx} ({node_type}): ⟨S⟩ = {s_mean[n_idx]:.4f}")
    print(f"    Fourier amplitudes by ℓ:")
    for f in s_fourier:
        print(f"      ℓ={f['ell']}: amp = {f['amp']:.4e}")

    # ── T5: Faraday's law check ───────────────────────────────────────────
    # ∮V·dl from V_total = V_inc + V_ref
    n_node_idx = {tuple(n): i for i, n in enumerate(nodes)}
    loop_V_traj = np.zeros(N_STEPS)
    for i in range(N_STEPS):
        loop_V = 0.0
        for bnd in bonds:
            ring_idx = n_node_idx[tuple(bnd["a_site"])]
            port = bnd["port"]
            a_to_b = np.array(bnd["a_to_b_offset"], dtype=float)
            a_to_b /= np.linalg.norm(a_to_b)
            traversal = np.array(bnd["traversal_direction"], dtype=float)
            sign = float(np.sign(np.dot(a_to_b, traversal)))
            v_total = float(v_inc[i, ring_idx, port] + v_ref[i, ring_idx, port])
            loop_V += sign * v_total
        loop_V_traj[i] = loop_V
    loop_V_DC = float(loop_V_traj[sw_start:].mean())

    edge1 = nodes[0] - centroid
    edge2 = nodes[2] - centroid
    n_hat = np.cross(edge1, edge2)
    n_hat = n_hat / np.linalg.norm(n_hat)
    R_ring = float(np.linalg.norm(edge1))
    hex_area = (3.0 * np.sqrt(3.0) / 2.0) * R_ring ** 2

    omega_normal_ring = omega @ n_hat
    omega_normal_int = interior_omega @ n_hat
    Phi_B_t = np.zeros(N_STEPS)
    area_tri = hex_area / 6.0
    for i in range(N_STEPS):
        omega_c = omega_normal_int[i]
        accum = 0.0
        for k in range(6):
            v1 = omega_normal_ring[i, k]
            v2 = omega_normal_ring[i, (k+1) % 6]
            accum += (v1 + v2 + omega_c) / 3.0 * area_tri
        Phi_B_t[i] = accum

    t_vec = np.arange(N_STEPS) * v8.DT
    sw = slice(sw_start, N_STEPS)
    dPhiB_dt = float(np.polyfit(t_vec[sw], Phi_B_t[sw], 1)[0])
    expected = -loop_V_DC
    residual = dPhiB_dt - expected
    rel_residual = abs(residual) / max(abs(loop_V_DC), 1e-15) * 100

    print()
    print(f"  T5 — Faraday's law check:")
    print(f"    ∮V·dl steady DC: {loop_V_DC:+.4e}")
    print(f"    dΦ_B/dt steady:  {dPhiB_dt:+.4e}")
    print(f"    Faraday expects: {expected:+.4e}")
    print(f"    Residual:        {residual:+.4e}  ({rel_residual:.2f}% of ∮V·dl)")
    if rel_residual < 10:
        print(f"        ✓ Faraday HOLDS at LC-coupled config")
    elif rel_residual < 50:
        print(f"        ↗ Faraday partially restored (was 99.98% violated at v8)")
    else:
        print(f"        ↘ Faraday still violated (similar to v8 99.98%)")

    out = {
        "test": "Control B4: LC-coupled re-run (disable_cosserat_lc_force=False)",
        "engine_config": {
            "disable_cosserat_lc_force": False,
            "enable_cosserat_self_terms": True,
        },
        "elapsed_recording_s": elapsed,
        "n_steps": N_STEPS,
        "A2_mean_steady": float(A2_mean_traj[sw_start:].mean()),
        "v_inc_top5_peaks": v_peaks,
        "omega_top5_peaks": w_peaks,
        "v_inc_dominant_ratio_to_fC": v_peaks[0][1] / f_C,
        "omega_dominant_ratio_to_fC": w_peaks[0][1] / f_C,
        "v8_baseline_v_inc_ratio": 1.4798,
        "v8_baseline_omega_ratio": 3.9863,
        "cos_sim_AC_steady": cos_sim_AC_steady,
        "v8_baseline_cos_sim_AC": 0.5151,
        "s_field_mean_per_node": s_mean.tolist(),
        "s_field_fourier": s_fourier,
        "loop_V_DC_steady": loop_V_DC,
        "dPhi_B_dt_steady": dPhiB_dt,
        "faraday_residual_rel_pct": rel_residual,
        "v8_baseline_faraday_violation_pct": 99.98,
    }
    out_path = Path(__file__).parent / "r10_v8_ee_phase_a_b4_lc_coupled_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
