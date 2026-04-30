"""
r10 path α v8 DC/AC re-analysis.

Re-uses v8's IC + engine setup verbatim. Adds DC/AC decomposition per
Grant's plumber-physical reframe 2026-04-29:
  - DC component  = saturation core  (Ax 4 V_SNAP/B_SNAP pegging, frame-stationary)
  - AC RMS comp.  = Beltrami envelope (Ax 3 oscillating standing wave at ω_C)

v8's `cos_sim(A_oscillating, ω_full)` mixed an AC-detrended A with a
non-detrended ω. If the rotational sector has a substantial DC pinning
(saturation core), `ω_full` carries DC content that's orthogonal in
time-average to A_AC, attenuating the cos_sim metric even when the AC
sector is a perfect Beltrami eigenmode.

Load-bearing predicted relation (auditor-arithmetic per Rule 16 / A47):
  ⟨cos_sim_full⟩ = perfect_AC_Beltrami × |ω_AC| / |ω_full|
v8 observed cos_sim_full = 0.515. If this entire deficit comes from a
DC core dominating the rotational energy, then |ω_AC|/|ω_full| ≈ 0.515,
i.e. |ω_DC|² / |ω_full|² ≈ 0.735 (DC carries ~74% of |ω|² at ring nodes).

Test: re-run the recording, compute ω_DC + ω_AC = ω - ω_DC, then measure
`cos_sim(A_AC, ω_AC)` in steady-state. Prediction:
  cos_sim_AC → 1.0 (or > 0.8 PASS threshold) if the AC sector is a clean
  Beltrami eigenmode that v8 had been measuring through DC contamination.

Single T=0 run; thermal sweep deferred until the T=0 result lands.
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
from ave.core.constants import V_SNAP, B_SNAP

import r10_path_alpha_v8_corrected_measurements as v8


def detrend_with_slope(traj):
    """v8's detrend, augmented to return slope + intercept.

    Returns (residual, slope, intercept) where:
      slope[..., port] = dPhi_link/d(step_index) per port
      V_DC per port = slope / DT_engine     (volts in V_SNAP units)
    """
    n_steps = traj.shape[0]
    t = np.arange(n_steps, dtype=np.float64)
    t_mean = t.mean()
    t_var = ((t - t_mean) ** 2).sum()
    mean = traj.mean(axis=0)
    slope_num = ((t[:, None, None, None, None] - t_mean) * (traj - mean[None, ...])).sum(axis=0)
    slope = slope_num / t_var
    intercept = mean - slope * t_mean
    trend = intercept[None, ...] + slope[None, ...] * t[:, None, None, None, None]
    return traj - trend, slope, intercept


def main():
    print("=" * 78, flush=True)
    print("  r10 path α v8 DC/AC re-analysis  [T=0 only]")
    print("=" * 78, flush=True)

    nodes, bonds = v8.build_chair_ring(v8.CENTER)
    a_0_per_node, centroid = v8.compute_a_0_at_ring_nodes(
        nodes, v8.A_AMP_POL, v8.HELICAL_PITCH
    )

    engine = VacuumEngine3D.from_args(
        N=v8.N_LATTICE, pml=v8.PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )

    print("Applying v8 helical Beltrami IC (UNCHANGED from v8)...", flush=True)
    v8.initialize_helical_beltrami_ic(
        engine, nodes, bonds, a_0_per_node,
        v8.K_BELTRAMI, v8.V_AMP, v8.PHI_AMP,
    )

    nx = engine.k4.nx
    N_STEPS = v8.N_RECORDING_STEPS
    print(f"Recording {N_STEPS} steps...", flush=True)
    phi_link_traj = np.zeros((N_STEPS, nx, nx, nx, 4), dtype=np.float32)
    omega_traj = np.zeros((N_STEPS, 6, 3), dtype=np.float32)
    A2_mean_traj = np.zeros(N_STEPS)
    ring_loc_traj = np.zeros(N_STEPS)

    t0 = time.time()
    last = t0
    for i in range(N_STEPS):
        engine.step()
        phi_link_traj[i] = engine.k4.Phi_link.astype(np.float32)
        for n_idx, node in enumerate(nodes):
            omega_traj[i, n_idx, :] = engine.cos.omega[node[0], node[1], node[2], :]
        s = v8.measure_ring_state_v8(engine, nodes)
        A2_mean_traj[i] = s["A2_mean"]
        ring_loc_traj[i] = s["ring_localization"]
        if (time.time() - last) > 30.0:
            t_p = (i + 1) * v8.DT / v8.COMPTON_PERIOD
            print(f"    step {i}/{N_STEPS}, t={t_p:.1f}P, A²_mean={s['A2_mean']:.3f}, "
                  f"loc={s['ring_localization']:.3f}, elapsed {time.time()-t0:.1f}s",
                  flush=True)
            last = time.time()
    elapsed = time.time() - t0
    print(f"  Recording done at {elapsed:.1f}s", flush=True)

    # ── DC/AC decomposition ──────────────────────────────────────────────────
    print("Decomposing into DC + AC sectors...", flush=True)
    phi_oscillating, phi_slope, _ = detrend_with_slope(phi_link_traj.astype(np.float64))

    # ω sector: time-mean = DC, residual = AC
    omega_DC = omega_traj.mean(axis=0)              # (6, 3)
    omega_AC_traj = omega_traj - omega_DC[None, :, :]  # (N_steps, 6, 3)

    # |ω_DC|, |ω_AC|_RMS per ring node
    omega_DC_mag = np.linalg.norm(omega_DC, axis=1)                       # (6,)
    omega_AC_mag_per_step = np.linalg.norm(omega_AC_traj, axis=2)          # (N_steps, 6)
    omega_AC_RMS = np.sqrt((omega_AC_mag_per_step ** 2).mean(axis=0))      # (6,)
    omega_full_mag_per_step = np.linalg.norm(omega_traj, axis=2)           # (N_steps, 6)
    omega_full_RMS = np.sqrt((omega_full_mag_per_step ** 2).mean(axis=0))  # (6,)

    # Energy fractions: |ω_DC|² / |ω_full|²_RMS  vs  |ω_AC|²_RMS / |ω_full|²_RMS
    # By construction these sum to 1 because <ω_AC · ω_DC> = ω_DC · <ω_AC> = 0
    omega_DC_energy_frac = (omega_DC_mag ** 2) / (omega_full_RMS ** 2)
    omega_AC_energy_frac = (omega_AC_RMS ** 2) / (omega_full_RMS ** 2)

    # V_DC per port from Phi_link slope. slope is per-step; V = dPhi/dt
    V_DC_per_port = phi_slope / v8.DT  # shape (nx, ny, nz, 4) in V_SNAP units (engine convention)
    V_DC_at_ring_per_node = np.array([
        np.sqrt(np.sum(V_DC_per_port[node[0], node[1], node[2], :] ** 2))
        for node in nodes
    ])
    # In engine convention V_inc IS in V_SNAP units. So |V_DC|/V_SNAP is the dimensionless
    # ratio measuring saturation pinning of the capacitive sector.
    V_DC_over_V_SNAP_at_ring = V_DC_at_ring_per_node  # already engine-V_SNAP-natural per amplitude_convention

    # ── Beltrami tests ───────────────────────────────────────────────────────
    print("Beltrami AC vs full-ω cos_sim per step...", flush=True)
    cos_sim_AC = np.zeros(N_STEPS)
    cos_sim_full = np.zeros(N_STEPS)
    for i in range(N_STEPS):
        sims_AC = []
        sims_full = []
        for n_idx, node in enumerate(nodes):
            a_vec = v8.measure_a_vec_from_phi_link_oscillating(
                phi_oscillating, node[0], node[1], node[2], i,
                v8.PORT_OFFSETS_A, v8.N_LATTICE,
            )
            a_norm = np.linalg.norm(a_vec)
            for omega_vec, store in (
                (omega_AC_traj[i, n_idx, :], sims_AC),
                (omega_traj[i, n_idx, :], sims_full),
            ):
                w_norm = np.linalg.norm(omega_vec)
                if a_norm < 1e-12 or w_norm < 1e-12:
                    store.append(0.0)
                else:
                    store.append(float(np.dot(a_vec, omega_vec) / (a_norm * w_norm)))
        cos_sim_AC[i] = float(np.mean(np.abs(sims_AC)))
        cos_sim_full[i] = float(np.mean(np.abs(sims_full)))

    sw_start = N_STEPS // 4
    cos_sim_AC_steady = float(np.mean(cos_sim_AC[sw_start:]))
    cos_sim_full_steady = float(np.mean(cos_sim_full[sw_start:]))
    A2_mean_steady = float(np.mean(A2_mean_traj[sw_start:]))
    ring_loc_steady = float(np.mean(ring_loc_traj[sw_start:]))

    # Loop flux DC vs AC: DC accumulates ∮V_DC·dl × t (linear ramp); AC oscillates
    loop_flux_AC_traj = np.zeros(N_STEPS)
    for i in range(N_STEPS):
        loop_flux_AC_traj[i] = v8.measure_loop_flux_oscillating(phi_oscillating, bonds, i)
    loop_flux_AC_steady_RMS = float(np.sqrt(np.mean(loop_flux_AC_traj[sw_start:] ** 2)))
    loop_flux_AC_steady_peak = float(np.max(np.abs(loop_flux_AC_traj[sw_start:])))

    # ∮ V_DC · traversal_sign over the 6 ring bonds (DC EMF around the ring)
    loop_V_DC = 0.0
    for bnd in bonds:
        ix, iy, iz = bnd["a_site"]
        port = bnd["port"]
        # bond traversal direction relative to a→b port_offset: same direction = +1, reverse = -1
        a_to_b = np.array(bnd["a_to_b_offset"], dtype=float)
        a_to_b /= np.linalg.norm(a_to_b)
        traversal = np.array(bnd["traversal_direction"], dtype=float)
        sign = float(np.sign(np.dot(a_to_b, traversal)))
        loop_V_DC += sign * V_DC_per_port[ix, iy, iz, port]

    # ── Output ───────────────────────────────────────────────────────────────
    out = {
        "test": "v8 DC/AC re-analysis @ T=0",
        "elapsed_recording_seconds": elapsed,
        "lattice": {"N": v8.N_LATTICE, "PML": v8.PML, "center": list(v8.CENTER)},
        "recording_periods": v8.RECORDING_END_P,
        "n_steps": N_STEPS,
        "engine_DT": v8.DT,
        # Ring-resolved DC/AC observables
        "omega_DC_per_node": omega_DC.tolist(),
        "omega_DC_mag_per_node": omega_DC_mag.tolist(),
        "omega_AC_RMS_per_node": omega_AC_RMS.tolist(),
        "omega_full_RMS_per_node": omega_full_RMS.tolist(),
        "omega_DC_energy_fraction_per_node": omega_DC_energy_frac.tolist(),
        "omega_AC_energy_fraction_per_node": omega_AC_energy_frac.tolist(),
        # V (capacitive) DC per ring node
        "V_DC_at_ring_per_node": V_DC_at_ring_per_node.tolist(),
        "V_DC_over_V_SNAP_per_ring_node": V_DC_over_V_SNAP_at_ring.tolist(),
        "loop_V_DC_around_ring": loop_V_DC,
        # AC loop flux (matches v8 metric)
        "loop_flux_AC_steady_RMS": loop_flux_AC_steady_RMS,
        "loop_flux_AC_steady_peak": loop_flux_AC_steady_peak,
        # Beltrami tests — load-bearing
        "cos_sim_full_steady": cos_sim_full_steady,   # reproduces v8's 0.515
        "cos_sim_AC_steady": cos_sim_AC_steady,        # NEW: AC-decomposed
        # Sanity / state metrics
        "A2_mean_steady": A2_mean_steady,
        "ring_localization_steady": ring_loc_steady,
        # Steady-state windowed cos_sim trajectory subsamples
        "cos_sim_AC_first_50": cos_sim_AC[:50].tolist(),
        "cos_sim_AC_last_50": cos_sim_AC[-50:].tolist(),
        "cos_sim_full_first_50": cos_sim_full[:50].tolist(),
        "cos_sim_full_last_50": cos_sim_full[-50:].tolist(),
    }

    # ── Adjudication summary ─────────────────────────────────────────────────
    print()
    print("=" * 78, flush=True)
    print("  DC/AC adjudication summary")
    print("=" * 78, flush=True)
    print(f"  ω_DC_mag per ring node:        {[f'{x:+.4e}' for x in omega_DC_mag]}")
    print(f"  ω_AC_RMS per ring node:        {[f'{x:+.4e}' for x in omega_AC_RMS]}")
    print(f"  |ω_DC|² / |ω_full|² fraction:  {[f'{x:.3f}' for x in omega_DC_energy_frac]}")
    print(f"  |ω_AC|² / |ω_full|² fraction:  {[f'{x:.3f}' for x in omega_AC_energy_frac]}")
    print(f"  V_DC at ring (V_SNAP units):   {[f'{x:+.4e}' for x in V_DC_at_ring_per_node]}")
    print(f"  ∮V_DC·dl around ring:          {loop_V_DC:+.4e}  V_SNAP-natural")
    print()
    print(f"  cos_sim_full steady (v8 metric): {cos_sim_full_steady:.4f}  (v8 reported 0.515)")
    print(f"  cos_sim_AC   steady (NEW):       {cos_sim_AC_steady:.4f}")
    print(f"  Beltrami AC PASS (≥ 0.8): {cos_sim_AC_steady >= 0.8}")
    print()

    # Predicted relation check (auditor arithmetic per Rule 16):
    # cos_sim_full = perfect_AC_Beltrami × |ω_AC| / |ω_full|
    # If perfect AC Beltrami: cos_sim_full ≈ ratio_AC_to_full
    ratio_AC_to_full_per_node = omega_AC_RMS / omega_full_RMS
    ratio_AC_to_full_mean = float(ratio_AC_to_full_per_node.mean())
    print(f"  Predicted cos_sim_full = perfect_Beltrami × |ω_AC|/|ω_full|")
    print(f"    Mean |ω_AC|/|ω_full| ratio: {ratio_AC_to_full_mean:.4f}")
    print(f"    If AC is perfectly Beltrami, predicts cos_sim_full ≈ {ratio_AC_to_full_mean:.4f}")
    print(f"    Observed cos_sim_full:       {cos_sim_full_steady:.4f}")
    print(f"    Implied AC Beltrami quality: {cos_sim_full_steady / max(ratio_AC_to_full_mean, 1e-12):.4f}")
    print(f"    Direct cos_sim_AC observed:  {cos_sim_AC_steady:.4f}")
    print()

    out["audit"] = {
        "ratio_AC_to_full_mean": ratio_AC_to_full_mean,
        "implied_AC_Beltrami_quality_from_full_metric": cos_sim_full_steady / max(ratio_AC_to_full_mean, 1e-12),
        "direct_cos_sim_AC_steady": cos_sim_AC_steady,
        "v8_reported_cos_sim": 0.5152,
    }

    out_path = Path(__file__).parent / "r10_v8_dc_ac_reanalysis_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"Saved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
