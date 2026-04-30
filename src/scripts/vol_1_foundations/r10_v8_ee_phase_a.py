"""
r10 path α v8 EE Phase A — power-electronics analysis suite.

Implements the [doc 93 §6.1 + §7](../../research/L3_electron_soliton/93_ee_to_ave_mapping.md)
single re-run capture spec. Runs v8's IC + engine config UNCHANGED, captures
ring-node trajectories of (V_inc, V_ref, Phi_link, ω, ω_dot, u_dot), saves
to .npz, then executes Phase A1–A7 analyses on the saved trajectories:

  A1. FFT of V_inc, V_ref, ω, ω_dot at ring node 0 — engine actual frequency
  A2. Faraday's law check on chair-ring DC EMF
  A3. Bond-LC characteristic frequency (numerical)
  A4. Real vs reactive power per port — ⟨V_inc²⟩ vs ⟨V_ref²⟩
  A5. Q factor from amplitude trajectory
  A6. B-H Lissajous: ω(t) vs Phi_link(t) at ring node 0
  A7. Coupled-mode eigenvalue analysis (analytical, no traj needed)
  A8 (deferred): lock-in at ω_engine (after A1)

Total wall: ~270s capture + ~30s analyses.
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
from ave.core.constants import V_SNAP, B_SNAP, MU_0, EPSILON_0, C_0, L_NODE, Z_0

import r10_path_alpha_v8_corrected_measurements as v8


# ─── Capture stage ───────────────────────────────────────────────────────────

def capture_ring_trajectories():
    print("=" * 78, flush=True)
    print("  r10 EE Phase A — capture ring-node trajectories  [T=0, 200P]")
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
    print("Applying v8 helical Beltrami IC...", flush=True)
    v8.initialize_helical_beltrami_ic(
        engine, nodes, bonds, a_0_per_node,
        v8.K_BELTRAMI, v8.V_AMP, v8.PHI_AMP,
    )

    N_STEPS = v8.N_RECORDING_STEPS
    print(f"Recording {N_STEPS} steps...", flush=True)

    # Per-ring-node trajectories
    v_inc = np.zeros((N_STEPS, 6, 4), dtype=np.float32)
    v_ref = np.zeros((N_STEPS, 6, 4), dtype=np.float32)
    phi_link = np.zeros((N_STEPS, 6, 4), dtype=np.float32)
    omega = np.zeros((N_STEPS, 6, 3), dtype=np.float32)
    omega_dot = np.zeros((N_STEPS, 6, 3), dtype=np.float32)
    u_dot = np.zeros((N_STEPS, 6, 3), dtype=np.float32)

    # Centroid point + a few interior points for Faraday Φ_B integration
    cx, cy, cz = v8.CENTER
    centroid_int = (int(round(cx + (centroid[0] - cx))),
                    int(round(cy + (centroid[1] - cy))),
                    int(round(cz + (centroid[2] - cz))))
    interior_pts = [centroid_int]
    interior_omega = np.zeros((N_STEPS, len(interior_pts), 3), dtype=np.float32)

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
        for p_idx, pt in enumerate(interior_pts):
            interior_omega[i, p_idx, :] = engine.cos.omega[pt[0], pt[1], pt[2], :]
        if (time.time() - last) > 30.0:
            t_p = (i + 1) * v8.DT / v8.COMPTON_PERIOD
            print(f"    step {i}/{N_STEPS}, t={t_p:.1f}P, elapsed {time.time()-t0:.1f}s",
                  flush=True)
            last = time.time()
    elapsed = time.time() - t0
    print(f"  Recording done at {elapsed:.1f}s", flush=True)

    capture = {
        "n_steps": N_STEPS,
        "DT": v8.DT,
        "compton_period": v8.COMPTON_PERIOD,
        "nodes": np.array(nodes, dtype=int),
        "bonds": bonds,
        "centroid": centroid,
        "interior_pts": np.array(interior_pts, dtype=int),
        "v_inc": v_inc,
        "v_ref": v_ref,
        "phi_link": phi_link,
        "omega": omega,
        "omega_dot": omega_dot,
        "u_dot": u_dot,
        "interior_omega": interior_omega,
        "elapsed_recording_s": elapsed,
    }
    return capture, nodes, bonds, centroid


# ─── Phase A analyses ────────────────────────────────────────────────────────

def analysis_a1_fft(cap, results):
    """A1 — FFT of V_inc, V_ref, ω, ω_dot at ring node 0."""
    DT = cap["DT"]
    N = cap["n_steps"]
    sw_start = N // 4  # skip transient

    # Use ring node 0, take magnitude along ports/axes
    v_inc_n0 = np.linalg.norm(cap["v_inc"][sw_start:, 0, :], axis=1)  # |V_inc|(t)
    v_ref_n0 = np.linalg.norm(cap["v_ref"][sw_start:, 0, :], axis=1)
    omega_n0 = np.linalg.norm(cap["omega"][sw_start:, 0, :], axis=1)
    omega_dot_n0 = np.linalg.norm(cap["omega_dot"][sw_start:, 0, :], axis=1)

    n_samples = len(v_inc_n0)
    freqs = np.fft.rfftfreq(n_samples, d=DT)  # in 1/(engine time units)
    # Compton frequency in same units: ω_C = c/ℓ_node = 1 in natural units → period 2π
    omega_c_natural = 1.0
    f_c_natural = omega_c_natural / (2 * np.pi)
    bond_length = np.sqrt(3.0)  # in ℓ_node units
    omega_lc = 1.0 / bond_length  # = c/bond_length in natural units (engine c=1)
    f_lc_natural = omega_lc / (2 * np.pi)

    # Subtract DC before FFT (we already characterized DC)
    def fft_mag(x):
        x_ac = x - x.mean()
        return np.abs(np.fft.rfft(x_ac))

    fft_v_inc = fft_mag(v_inc_n0)
    fft_v_ref = fft_mag(v_ref_n0)
    fft_omega = fft_mag(omega_n0)
    fft_omega_dot = fft_mag(omega_dot_n0)

    def find_peaks(spec, k=3):
        idxs = np.argsort(spec)[::-1][:k]
        return [(int(i), float(freqs[i]), float(spec[i])) for i in idxs]

    out = {
        "engine_DT": DT,
        "n_samples_post_transient": n_samples,
        "f_compton_natural": f_c_natural,
        "f_LC_natural": f_lc_natural,
        "ratio_f_LC_to_f_C": f_lc_natural / f_c_natural,
        "v_inc_top3_peaks": find_peaks(fft_v_inc),
        "v_ref_top3_peaks": find_peaks(fft_v_ref),
        "omega_top3_peaks": find_peaks(fft_omega),
        "omega_dot_top3_peaks": find_peaks(fft_omega_dot),
    }
    results["A1_fft"] = out
    return out


def analysis_a2_faraday(cap, results):
    """A2 — Faraday's law check on chair-ring DC EMF."""
    DT = cap["DT"]
    N = cap["n_steps"]
    bonds = cap["bonds"]
    centroid = cap["centroid"]
    nodes = cap["nodes"]

    # Compute ∮V·dl(t) per step using V_inc + V_ref (V_total at A-site port)
    # For each ring bond: V_along_bond = V_inc + V_ref at A-site port (with traversal sign)
    n_node_idx = {tuple(n): i for i, n in enumerate(nodes.tolist())}

    loop_V_traj = np.zeros(N)
    for i in range(N):
        loop_V = 0.0
        for bnd in bonds:
            a_site = tuple(bnd["a_site"])
            ring_idx_of_a = n_node_idx[a_site]
            port = bnd["port"]
            a_to_b = np.array(bnd["a_to_b_offset"], dtype=float)
            a_to_b /= np.linalg.norm(a_to_b)
            traversal = np.array(bnd["traversal_direction"], dtype=float)
            sign = float(np.sign(np.dot(a_to_b, traversal)))
            v_total = float(cap["v_inc"][i, ring_idx_of_a, port] + cap["v_ref"][i, ring_idx_of_a, port])
            loop_V += sign * v_total
        loop_V_traj[i] = loop_V

    # DC component of ∮V·dl
    sw_start = N // 4
    loop_V_DC = float(loop_V_traj[sw_start:].mean())
    loop_V_AC_RMS = float(np.sqrt(((loop_V_traj[sw_start:] - loop_V_DC) ** 2).mean()))

    # Compute Φ_B(t) ≈ ⟨ω·n̂⟩_ring × area_enclosed
    # Loop normal n̂: cross product of two edges from centroid
    edge1 = nodes[0] - centroid
    edge2 = nodes[2] - centroid  # 60°-spaced ring node
    n_hat = np.cross(edge1, edge2)
    n_hat = n_hat / np.linalg.norm(n_hat)

    # Hexagonal area: (3√3/2) × R² where R = ring radius
    R_ring = float(np.linalg.norm(edge1))
    area_enclosed = (3.0 * np.sqrt(3.0) / 2.0) * R_ring ** 2

    # ⟨ω·n̂⟩ per step averaged over 6 ring nodes
    omega_normal_t = (cap["omega"] @ n_hat).mean(axis=1)  # shape (N_steps,)
    Phi_B_t = area_enclosed * omega_normal_t

    # Linear fit to get d⟨Φ_B⟩/dt over steady-state window
    t_vec = np.arange(N) * DT
    sw = slice(sw_start, N)
    fit = np.polyfit(t_vec[sw], Phi_B_t[sw], 1)
    dPhiB_dt = float(fit[0])  # slope = dΦ_B/dt

    # Faraday: ∮V·dl = -dΦ_B/dt
    faraday_residual = loop_V_DC + dPhiB_dt
    faraday_relative_residual = faraday_residual / max(abs(loop_V_DC), 1e-15)

    out = {
        "loop_V_DC_steady": loop_V_DC,
        "loop_V_AC_RMS_steady": loop_V_AC_RMS,
        "ring_radius_lnode": R_ring,
        "area_enclosed_lnode2": area_enclosed,
        "loop_normal_hat": n_hat.tolist(),
        "Phi_B_initial_steady": float(Phi_B_t[sw_start]),
        "Phi_B_final": float(Phi_B_t[-1]),
        "dPhi_B_dt_steady": dPhiB_dt,
        "expected_dPhi_B_dt_from_Faraday": -loop_V_DC,
        "faraday_residual_abs": faraday_residual,
        "faraday_residual_rel": faraday_relative_residual,
    }
    results["A2_faraday"] = out
    return out


def analysis_a3_bond_lc(results):
    """A3 — Bond LC characteristic frequency derivation."""
    bond_length_SI = np.sqrt(3.0) * L_NODE
    L_bond = MU_0 * bond_length_SI
    C_bond = EPSILON_0 * bond_length_SI
    Z_bond = np.sqrt(L_bond / C_bond)
    omega_LC_SI = 1.0 / np.sqrt(L_bond * C_bond)
    omega_C_SI = C_0 / L_NODE
    ratio = omega_LC_SI / omega_C_SI

    out = {
        "L_node_m": L_NODE,
        "bond_length_m": float(bond_length_SI),
        "L_bond_H": float(L_bond),
        "C_bond_F": float(C_bond),
        "Z_bond_ohm": float(Z_bond),
        "Z_0_ohm": float(Z_0),
        "Z_bond_equals_Z_0": bool(abs(Z_bond - Z_0) < 1e-6),
        "omega_LC_SI_rad_per_s": float(omega_LC_SI),
        "omega_C_SI_rad_per_s": float(omega_C_SI),
        "omega_LC_over_omega_C": float(ratio),
        "expected_one_over_sqrt3": float(1.0 / np.sqrt(3.0)),
    }
    results["A3_bond_LC"] = out
    return out


def analysis_a4_power_split(cap, results):
    """A4 — Real vs reactive power per port at ring nodes."""
    sw_start = cap["n_steps"] // 4
    v_inc = cap["v_inc"][sw_start:]  # shape (N_post, 6, 4)
    v_ref = cap["v_ref"][sw_start:]

    v_inc_sq = (v_inc ** 2).mean(axis=0)  # shape (6, 4)
    v_ref_sq = (v_ref ** 2).mean(axis=0)
    real_power_signature = v_inc_sq - v_ref_sq  # (V_inc² - V_ref²)/Z₀ ∝ this
    relative = real_power_signature / np.maximum(v_inc_sq + v_ref_sq, 1e-30)

    out = {
        "v_inc_sq_per_node_port": v_inc_sq.tolist(),
        "v_ref_sq_per_node_port": v_ref_sq.tolist(),
        "real_power_signature_per_node_port": real_power_signature.tolist(),
        "relative_real_power_per_node_port": relative.tolist(),
        "max_abs_relative_real_power": float(np.max(np.abs(relative))),
        "mean_abs_relative_real_power": float(np.mean(np.abs(relative))),
        "interpretation": (
            "If ⟨V_inc²⟩ ≈ ⟨V_ref²⟩ (relative ≈ 0) at every port: pure reactive ringing, "
            "lossless Γ=-1 wall confinement. If non-zero: net real power flux."
        ),
    }
    results["A4_power_split"] = out
    return out


def analysis_a5_q_factor(cap, results):
    """A5 — Q factor from amplitude trajectory."""
    DT = cap["DT"]
    N = cap["n_steps"]
    # Use total energy at ring nodes: V_inc² + V_ref² + ω² (proxy for stored energy)
    e_traj = (
        (cap["v_inc"] ** 2).sum(axis=(1, 2))
        + (cap["v_ref"] ** 2).sum(axis=(1, 2))
        + (cap["omega"] ** 2).sum(axis=(1, 2))
    )
    sw_start = N // 4
    t_vec = np.arange(N) * DT
    e_steady = e_traj[sw_start:]
    e_mean = float(e_steady.mean())
    e_std = float(e_steady.std())

    # Linear fit log(E) vs t for decay rate
    log_e = np.log(np.maximum(e_steady, 1e-30))
    slope, _ = np.polyfit(t_vec[sw_start:], log_e, 1)
    decay_rate_per_t = float(slope)
    # Q = ω / (2 × decay_rate). Use ω_engine ≈ ω_C natural units = 1.
    q_factor = float(1.0 / (2.0 * abs(decay_rate_per_t))) if abs(decay_rate_per_t) > 1e-12 else float("inf")

    out = {
        "energy_mean_steady": e_mean,
        "energy_std_steady": e_std,
        "energy_relative_drift": e_std / max(e_mean, 1e-30),
        "decay_rate_per_t_natural": decay_rate_per_t,
        "Q_factor_estimate": q_factor,
        "Q_factor_estimate_inf_threshold": "treats |decay_rate| < 1e-12 as Q→∞",
    }
    results["A5_q_factor"] = out
    return out


def analysis_a6_bh_lissajous(cap, results):
    """A6 — B-H Lissajous: ω(t) vs Phi_link(t) at ring node 0."""
    sw_start = cap["n_steps"] // 4
    # ω at ring node 0 → magnitude
    omega_0 = np.linalg.norm(cap["omega"][sw_start:, 0, :], axis=1)
    # Phi_link at ring node 0 → magnitude across 4 ports
    phi_0 = np.linalg.norm(cap["phi_link"][sw_start:, 0, :], axis=1)

    # Hysteresis loop area via shoelace on (phi_0, omega_0)
    # Skip first 25% as transient already; further detrend phi_0 (which drifts linearly)
    t_vec = np.arange(len(phi_0)) * cap["DT"]
    phi_slope, phi_int = np.polyfit(t_vec, phi_0, 1)
    phi_0_detrended = phi_0 - (phi_int + phi_slope * t_vec)

    # Take a window of one estimated period (use omega_C natural = 2π period)
    period_steps = int(cap["compton_period"] / cap["DT"])
    if period_steps > len(omega_0):
        period_steps = len(omega_0)

    # Loop area via shoelace formula on (phi_0_detrended, omega_0) within one period
    omega_window = omega_0[:period_steps]
    phi_window = phi_0_detrended[:period_steps]
    area_oneperiod = 0.5 * abs(
        np.sum(phi_window[:-1] * omega_window[1:] - phi_window[1:] * omega_window[:-1])
    )

    out = {
        "phi_link_n0_drift_rate_per_t": float(phi_slope),
        "phi_link_n0_detrended_RMS": float(np.sqrt((phi_0_detrended ** 2).mean())),
        "omega_n0_RMS": float(np.sqrt((omega_0 ** 2).mean())),
        "period_steps_used": int(period_steps),
        "BH_loop_area_oneperiod": float(area_oneperiod),
        "interpretation": (
            "Hysteresis loop area ∝ energy lost per cycle to saturation rectification. "
            "Thin/zero area = lossless reactive trap; non-zero area = real dissipation per cycle."
        ),
    }
    results["A6_bh_lissajous"] = out
    return out


def analysis_a7_coupled_modes(results, nodes, bonds):
    """A7 — Coupled-mode eigenvalue analysis on 6-bond chair ring (analytical)."""
    # Build a discrete Laplacian-like adjacency matrix on the 6-bond ring
    # M[i,j] = mutual coupling between bonds i and j (= 1 if they share a node, -1 if anti-parallel, 0 else)
    M = np.zeros((6, 6))
    for i in range(6):
        bi = bonds[i]
        a_i = tuple(bi["a_site"])
        b_i = tuple(bi["b_site"])
        for j in range(6):
            if i == j:
                M[i, j] = 1.0  # self
            else:
                bj = bonds[j]
                a_j = tuple(bj["a_site"])
                b_j = tuple(bj["b_site"])
                # Shared endpoint?
                shared_a = (a_i == a_j) or (a_i == b_j)
                shared_b = (b_i == a_j) or (b_i == b_j)
                if shared_a or shared_b:
                    # Coupling sign: if traversal directions agree at shared node, +; else -
                    t_i = np.array(bi["traversal_direction"])
                    t_j = np.array(bj["traversal_direction"])
                    M[i, j] = float(np.sign(np.dot(t_i, t_j))) * 0.5
    M = 0.5 * (M + M.T)  # symmetrize

    eigvals, eigvecs = np.linalg.eigh(M)
    # Mode frequencies: ω_n = ω_LC × √eigenvalue (in natural units)
    omega_LC_natural = 1.0 / np.sqrt(3.0)  # = c/bond_length in engine c=1, ℓ_node=1
    mode_freqs = omega_LC_natural * np.sqrt(np.abs(eigvals))

    out = {
        "coupling_matrix_M": M.tolist(),
        "eigenvalues": eigvals.tolist(),
        "mode_frequencies_natural": mode_freqs.tolist(),
        "ratio_to_omega_C": (mode_freqs / 1.0).tolist(),
        "omega_LC_natural": float(omega_LC_natural),
        "note": (
            "Simple bond-coupling model: M[i,j]=0.5 if bonds share endpoint with aligned "
            "traversal, -0.5 if anti-aligned, 1 on diagonal. Mode freqs are estimates "
            "of the chair-ring's natural cavity modes."
        ),
    }
    results["A7_coupled_modes"] = out
    return out


# ─── Main orchestrator ───────────────────────────────────────────────────────

def main():
    out_dir = Path(__file__).parent
    capture_npz = out_dir / "r10_v8_ee_phase_a_capture.npz"
    results_json = out_dir / "r10_v8_ee_phase_a_results.json"

    # Capture
    capture, nodes, bonds, centroid = capture_ring_trajectories()

    # Save .npz (capture only — analyses go to JSON)
    npz_save = {
        k: v for k, v in capture.items()
        if isinstance(v, np.ndarray) or isinstance(v, (int, float))
    }
    # Convert nodes / interior_pts / centroid which may be ndarray
    np.savez_compressed(
        capture_npz,
        v_inc=capture["v_inc"], v_ref=capture["v_ref"],
        phi_link=capture["phi_link"], omega=capture["omega"],
        omega_dot=capture["omega_dot"], u_dot=capture["u_dot"],
        interior_omega=capture["interior_omega"],
        nodes=capture["nodes"], interior_pts=capture["interior_pts"],
        centroid=capture["centroid"],
        DT=np.array([v8.DT]), n_steps=np.array([v8.N_RECORDING_STEPS]),
    )
    print(f"Saved capture .npz to {capture_npz.relative_to(Path.cwd())}", flush=True)

    # ── Phase A analyses ───────────────────────────────────────────────────
    results = {
        "test": "v8 EE Phase A — power-electronics analysis suite at T=0",
        "elapsed_recording_s": capture["elapsed_recording_s"],
    }

    print("\nRunning Phase A analyses...", flush=True)
    t_a = time.time()

    print("  A1 — FFT...", flush=True)
    a1 = analysis_a1_fft(capture, results)
    print("  A2 — Faraday's law check...", flush=True)
    a2 = analysis_a2_faraday(capture, results)
    print("  A3 — Bond LC characteristic frequency...", flush=True)
    a3 = analysis_a3_bond_lc(results)
    print("  A4 — Real vs reactive power split...", flush=True)
    a4 = analysis_a4_power_split(capture, results)
    print("  A5 — Q factor...", flush=True)
    a5 = analysis_a5_q_factor(capture, results)
    print("  A6 — B-H Lissajous...", flush=True)
    a6 = analysis_a6_bh_lissajous(capture, results)
    print("  A7 — Coupled-mode eigenvalues (analytical)...", flush=True)
    a7 = analysis_a7_coupled_modes(results, nodes, bonds)

    print(f"  Phase A analyses done at {time.time()-t_a:.1f}s")

    # ── Print summary ──────────────────────────────────────────────────────
    print()
    print("=" * 78, flush=True)
    print("  Phase A summary")
    print("=" * 78, flush=True)

    print("\n  A1 — FFT (post-transient, |V_inc| at ring node 0 magnitude):")
    print(f"    f_Compton (natural):    {a1['f_compton_natural']:.6f}")
    print(f"    f_LC (= 1/(2π√3)):      {a1['f_LC_natural']:.6f}  (ratio to f_C: {a1['ratio_f_LC_to_f_C']:.4f})")
    print(f"    Top-3 V_inc peaks (idx, freq, mag):")
    for p in a1["v_inc_top3_peaks"]:
        ratio_to_fc = p[1] / a1["f_compton_natural"]
        print(f"      idx={p[0]:5d}, f={p[1]:.6f} (= {ratio_to_fc:.4f} × f_C), mag={p[2]:.4e}")
    print(f"    Top-3 ω peaks:")
    for p in a1["omega_top3_peaks"]:
        ratio_to_fc = p[1] / a1["f_compton_natural"]
        print(f"      idx={p[0]:5d}, f={p[1]:.6f} (= {ratio_to_fc:.4f} × f_C), mag={p[2]:.4e}")

    print(f"\n  A2 — Faraday's law check:")
    print(f"    ∮V·dl steady DC: {a2['loop_V_DC_steady']:+.4e}")
    print(f"    dΦ_B/dt steady (from ω at ring): {a2['dPhi_B_dt_steady']:+.4e}")
    print(f"    Faraday expects dΦ_B/dt = -∮V·dl = {a2['expected_dPhi_B_dt_from_Faraday']:+.4e}")
    print(f"    Residual ∮V·dl + dΦ_B/dt: {a2['faraday_residual_abs']:+.4e}")
    print(f"    Relative residual: {a2['faraday_residual_rel']*100:.2f}%")

    print(f"\n  A3 — Bond LC characteristic:")
    print(f"    bond_length:   {a3['bond_length_m']:.4e} m")
    print(f"    L_bond:        {a3['L_bond_H']:.4e} H")
    print(f"    C_bond:        {a3['C_bond_F']:.4e} F")
    print(f"    Z_bond:        {a3['Z_bond_ohm']:.4f} Ω  (Z_0 = {a3['Z_0_ohm']:.4f}, equal: {a3['Z_bond_equals_Z_0']})")
    print(f"    ω_LC / ω_C:    {a3['omega_LC_over_omega_C']:.4f}  (expected 1/√3 = {a3['expected_one_over_sqrt3']:.4f})")

    print(f"\n  A4 — Real vs reactive power per port:")
    print(f"    max |⟨V_inc²⟩-⟨V_ref²⟩|/(⟨V_inc²⟩+⟨V_ref²⟩): {a4['max_abs_relative_real_power']:.4e}")
    print(f"    mean: {a4['mean_abs_relative_real_power']:.4e}")
    print(f"    {a4['interpretation']}")

    print(f"\n  A5 — Q factor:")
    print(f"    energy mean (steady): {a5['energy_mean_steady']:.4e}")
    print(f"    energy relative drift: {a5['energy_relative_drift']:.4e}")
    print(f"    decay rate per t (natural): {a5['decay_rate_per_t_natural']:+.4e}")
    print(f"    Q estimate: {a5['Q_factor_estimate']:.2e}")

    print(f"\n  A6 — B-H Lissajous:")
    print(f"    Φ_link drift rate per t at node 0: {a6['phi_link_n0_drift_rate_per_t']:+.4e}")
    print(f"    Φ_link AC RMS: {a6['phi_link_n0_detrended_RMS']:.4e}")
    print(f"    ω RMS at node 0: {a6['omega_n0_RMS']:.4e}")
    print(f"    B-H loop area (one period): {a6['BH_loop_area_oneperiod']:.4e}")

    print(f"\n  A7 — Coupled-mode eigenvalues:")
    print(f"    Mode frequencies (natural units, ω_C=1): {[f'{f:.4f}' for f in a7['mode_frequencies_natural']]}")

    results_json.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nSaved results JSON to {results_json.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
