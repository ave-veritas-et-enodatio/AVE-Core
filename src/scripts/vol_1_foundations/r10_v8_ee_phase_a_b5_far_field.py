"""
r10 EE Phase A — Control B5: Far-field E and B characterization.

Tests whether the chair-ring trapped state is an electron by
STANDARD-PHYSICS EXTERNAL OBSERVABLES, regardless of internal structure
(corpus-canonical via Vol 2 Ch 5:15 — unsaturated vacuum acts as linear
dielectric in far-field, static structural phase strain obeys 3D
Laplace Equation; standard multipole expansion applies).

Pre-flight spec (doc 95 §1-§5):
  - r range: r ∈ [3, 10] ℓ_node from chair-ring centroid (active region
    [4,28)³, centroid ≈ (15.5, 17.5, 16.5))
  - Spin axis candidates (ranked): loop normal n̂, antinode-pair axis,
    K4-chirality direction
  - Coulomb fit: |E|·r² = q_eff/(4πε₀); slope -2 ± 0.3, R² ≥ 0.7
  - Dipole fit: 1/r³ scaling with cos θ angular pattern
  - Mode I: ≥4 of 5 PASS; Mode II: 2-3; Mode III: 0-1

Engine config: v8 baseline UNCHANGED (disable_cosserat_lc_force=True,
enable_cosserat_self_terms=True, V_AMP=0.95, HELICAL_PITCH=1/(2π)).

Memory-efficient: only time-averages of full-lattice fields are saved
(no full trajectories).
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
    print("  r10 EE Phase A — Control B5: far-field E and B characterization")
    print("  Standard-physics external-observable test of chair-ring trapped state")
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
    print("Applying v8 helical Beltrami IC (UNCHANGED)...", flush=True)
    v8.initialize_helical_beltrami_ic(
        engine, nodes, bonds, a_0_per_node,
        v8.K_BELTRAMI, v8.V_AMP, v8.PHI_AMP,
    )

    N_STEPS = v8.N_RECORDING_STEPS
    sw_start = N_STEPS // 4

    print(f"Recording {N_STEPS} steps; accumulating full-lattice DC fields after step {sw_start}...",
          flush=True)

    nx = engine.k4.nx
    # Accumulators for time-averaging during steady-state window
    V_inc_sum = np.zeros((nx, nx, nx, 4), dtype=np.float64)
    V_ref_sum = np.zeros((nx, nx, nx, 4), dtype=np.float64)
    omega_sum = np.zeros((nx, nx, nx, 3), dtype=np.float64)
    u_dot_sum = np.zeros((nx, nx, nx, 3), dtype=np.float64)
    n_avg_steps = 0

    t0 = time.time()
    last = t0
    for i in range(N_STEPS):
        engine.step()
        if i >= sw_start:
            V_inc_sum += engine.k4.V_inc
            V_ref_sum += engine.k4.V_ref
            omega_sum += engine.cos.omega
            u_dot_sum += engine.cos.u_dot
            n_avg_steps += 1
        if (time.time() - last) > 30.0:
            t_p = (i + 1) * v8.DT / v8.COMPTON_PERIOD
            print(f"    step {i}/{N_STEPS}, t={t_p:.1f}P, elapsed {time.time()-t0:.1f}s",
                  flush=True)
            last = time.time()
    elapsed = time.time() - t0
    print(f"  Recording done at {elapsed:.1f}s ({n_avg_steps} samples averaged)", flush=True)

    V_inc_DC = V_inc_sum / n_avg_steps
    V_ref_DC = V_ref_sum / n_avg_steps
    omega_DC = omega_sum / n_avg_steps
    u_dot_DC = u_dot_sum / n_avg_steps

    # Save .npz for post-hoc analysis
    out_dir = Path(__file__).parent
    npz_path = out_dir / "r10_v8_ee_phase_a_b5_far_field_capture.npz"
    np.savez_compressed(
        npz_path,
        V_inc_DC=V_inc_DC, V_ref_DC=V_ref_DC,
        omega_DC=omega_DC, u_dot_DC=u_dot_DC,
        centroid=centroid, nodes=np.array(nodes),
        n_avg_steps=np.array([n_avg_steps]),
    )
    print(f"Saved DC field capture to {npz_path.relative_to(Path.cwd())}", flush=True)

    # ── Analysis ───────────────────────────────────────────────────────────
    print("\nRunning far-field analysis...", flush=True)

    PML = v8.PML
    active_min = PML
    active_max = nx - PML
    print(f"  Active region: [{active_min}, {active_max})³ on lattice {nx}³")

    # Build E_DC vector at A-sites from V_total_DC = V_inc + V_ref via Moore-Penrose
    PORT_DIRS = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]],
                          dtype=np.float64) / np.sqrt(3.0)
    bond_length = np.sqrt(3.0)

    V_total_DC = V_inc_DC + V_ref_DC  # (nx, nx, nx, 4)

    # E vector at each A-site: Σ port_dir × V_total_DC[port] / bond_length × (3/4)
    # Note: this is the 4-port → 3D Moore-Penrose reconstruction
    E_DC = np.zeros((nx, nx, nx, 3), dtype=np.float64)
    for p in range(4):
        for axis in range(3):
            E_DC[..., axis] += PORT_DIRS[p, axis] * V_total_DC[..., p] / bond_length
    E_DC *= (3.0 / 4.0)

    B_DC = omega_DC.copy()  # Cosserat ω = B field per Vol 1 Ch 4:23

    # Build mask of active region (exclude PML)
    active_mask = np.zeros((nx, nx, nx), dtype=bool)
    active_mask[active_min:active_max, active_min:active_max, active_min:active_max] = True

    # Distance from chair-ring centroid for each site
    cx, cy, cz = centroid
    ix, iy, iz = np.indices((nx, nx, nx))
    dx = ix - cx; dy = iy - cy; dz = iz - cz
    r = np.sqrt(dx**2 + dy**2 + dz**2)

    # ── A1: radial profile of |E_DC| ────────────────────────────────────
    print("\n  A1 — Radial profile of |E_DC| in active region")
    E_mag = np.linalg.norm(E_DC, axis=-1)

    # Bin by r in shells of width 1, range [3, 10]
    r_bins = np.arange(3, 11)
    E_mean_per_shell = []
    E_std_per_shell = []
    n_per_shell = []
    for r_low in r_bins[:-1]:
        r_high = r_low + 1
        shell_mask = (r >= r_low) & (r < r_high) & active_mask
        n_in_shell = int(shell_mask.sum())
        if n_in_shell > 0:
            E_mean_per_shell.append(float(E_mag[shell_mask].mean()))
            E_std_per_shell.append(float(E_mag[shell_mask].std()))
        else:
            E_mean_per_shell.append(0.0)
            E_std_per_shell.append(0.0)
        n_per_shell.append(n_in_shell)

    r_centers = (r_bins[:-1] + r_bins[1:]) / 2.0
    print(f"    r       <|E|_DC>      std         n_sites")
    for i in range(len(r_centers)):
        print(f"    {r_centers[i]:.1f}   {E_mean_per_shell[i]:.4e}   {E_std_per_shell[i]:.4e}   {n_per_shell[i]:5d}")

    # Coulomb fit: log(|E|) = log(q/(4πε₀)) - 2·log(r)
    valid = [m > 1e-10 for m in E_mean_per_shell]
    if sum(valid) >= 3:
        r_valid = r_centers[valid]
        E_valid = np.array(E_mean_per_shell)[valid]
        log_r = np.log(r_valid)
        log_E = np.log(E_valid)
        slope, intercept = np.polyfit(log_r, log_E, 1)
        E_fit = np.exp(intercept) * (r_valid ** slope)
        ss_res = np.sum((log_E - np.log(E_fit))**2)
        ss_tot = np.sum((log_E - log_E.mean())**2)
        r_squared = 1 - ss_res / max(ss_tot, 1e-30)
        print(f"\n  Power-law fit |E| = A · r^β:")
        print(f"    β (slope) = {slope:+.4f}  (Coulomb predicts -2.0 ± 0.3)")
        print(f"    A (amp)   = {np.exp(intercept):.4e}")
        print(f"    R²        = {r_squared:.4f}  (≥ 0.7 for clean power-law)")
        coulomb_slope_pass = abs(slope - (-2.0)) <= 0.3
        coulomb_r2_pass = r_squared >= 0.7
        print(f"    Coulomb slope PASS: {coulomb_slope_pass}; R² PASS: {coulomb_r2_pass}")
    else:
        slope = None
        r_squared = None
        coulomb_slope_pass = False
        coulomb_r2_pass = False
        print(f"\n  Coulomb fit: FAILED (insufficient valid shells)")

    # ── A2: angular profile of B_DC and dipole fit ───────────────────────
    print("\n  A2 — Angular profile of B_DC (dipole test)")
    B_mag = np.linalg.norm(B_DC, axis=-1)
    print(f"    Max |B_DC| in active region: {float(B_mag[active_mask].max()):.4e}")
    print(f"    Mean |B_DC| in active region: {float(B_mag[active_mask].mean()):.4e}")

    # Three candidate spin axes
    edge1 = np.array(nodes[0]) - centroid
    edge2 = np.array(nodes[2]) - centroid
    n_loop_normal = np.cross(edge1, edge2)
    n_loop_normal = n_loop_normal / np.linalg.norm(n_loop_normal)

    n_antinode_pair = np.array(nodes[2]) - np.array(nodes[5])
    n_antinode_pair = n_antinode_pair / np.linalg.norm(n_antinode_pair)

    # K4 chirality direction: tetrahedral diagonal (1,1,1)/√3
    n_k4_chiral = np.array([1.0, 1.0, 1.0]) / np.sqrt(3.0)

    candidate_axes = {
        "loop_normal": n_loop_normal,
        "antinode_pair": n_antinode_pair,
        "k4_chiral": n_k4_chiral,
    }

    print(f"    Candidate axes:")
    for name, ax in candidate_axes.items():
        print(f"      {name}: ({ax[0]:+.4f}, {ax[1]:+.4f}, {ax[2]:+.4f})")

    # B mean per shell + dipole fit per axis
    print(f"\n    Radial profile of |B_DC|:")
    print(f"    r       <|B|_DC>      std         n_sites")
    B_mean_per_shell = []
    B_std_per_shell = []
    for r_low in r_bins[:-1]:
        r_high = r_low + 1
        shell_mask = (r >= r_low) & (r < r_high) & active_mask
        n_in_shell = int(shell_mask.sum())
        if n_in_shell > 0:
            B_mean_per_shell.append(float(B_mag[shell_mask].mean()))
            B_std_per_shell.append(float(B_mag[shell_mask].std()))
        else:
            B_mean_per_shell.append(0.0)
            B_std_per_shell.append(0.0)
        print(f"    {r_centers[len(B_mean_per_shell)-1]:.1f}   {B_mean_per_shell[-1]:.4e}   {B_std_per_shell[-1]:.4e}   {n_in_shell:5d}")

    # Power-law fit on |B| vs r
    valid_B = [m > 1e-10 for m in B_mean_per_shell]
    if sum(valid_B) >= 3:
        r_valid_B = r_centers[valid_B]
        B_valid = np.array(B_mean_per_shell)[valid_B]
        log_r_B = np.log(r_valid_B)
        log_B = np.log(B_valid)
        slope_B, intercept_B = np.polyfit(log_r_B, log_B, 1)
        B_fit = np.exp(intercept_B) * (r_valid_B ** slope_B)
        ss_res_B = np.sum((log_B - np.log(B_fit))**2)
        ss_tot_B = np.sum((log_B - log_B.mean())**2)
        r2_B = 1 - ss_res_B / max(ss_tot_B, 1e-30)
        print(f"\n    Power-law fit |B| = A · r^β:")
        print(f"      β = {slope_B:+.4f}  (Dipole predicts -3.0 ± 0.3)")
        print(f"      R² = {r2_B:.4f}")
        dipole_slope_pass = abs(slope_B - (-3.0)) <= 0.3
        dipole_r2_pass = r2_B >= 0.7
    else:
        slope_B = None
        r2_B = None
        dipole_slope_pass = False
        dipole_r2_pass = False
        print(f"\n    Dipole power-law fit FAILED (insufficient valid shells; B may be ≈ 0)")

    # ── A3: Gauss's law cross-check ────────────────────────────────────
    print("\n  A3 — Gauss's law cross-check: ∮E·dA over sphere shells")
    # Approximate: sum E·r̂ × shell_volume / shell_radius² over each shell
    print(f"    Σ E_radial × (shell volume) per shell:")
    print(f"    r       Σ E·r̂·V_shell     # cells")
    flux_per_shell = []
    for r_low in r_bins[:-1]:
        r_high = r_low + 1
        shell_mask = (r >= r_low) & (r < r_high) & active_mask
        n_in_shell = int(shell_mask.sum())
        if n_in_shell > 0:
            r_hat = np.stack([dx, dy, dz], axis=-1) / np.maximum(r[..., None], 1e-30)
            E_radial = np.sum(E_DC * r_hat, axis=-1)
            flux = float(E_radial[shell_mask].sum())  # crude ∮E·dA approximation
        else:
            flux = 0.0
        flux_per_shell.append(flux)
        print(f"    {r_low+0.5:.1f}   {flux:+.4e}     {n_in_shell:5d}")

    # ── A4: Multipole decomposition (low-ℓ) ────────────────────────────
    print("\n  A4 — Spherical-harmonic multipole decomposition (low-ℓ)")
    # For each shell, project E·r̂ onto Y_ℓ^m for ℓ=0,1,2 (real Y_ℓ^m)
    theta = np.arccos(np.clip(dz / np.maximum(r, 1e-30), -1, 1))
    phi = np.arctan2(dy, dx)

    multipole_E_per_shell = {}
    for r_low in r_bins[:-1]:
        r_high = r_low + 1
        shell_mask = (r >= r_low) & (r < r_high) & active_mask
        if int(shell_mask.sum()) < 5:
            continue
        r_hat = np.stack([dx, dy, dz], axis=-1) / np.maximum(r[..., None], 1e-30)
        E_rad = np.sum(E_DC * r_hat, axis=-1)
        E_at = E_rad[shell_mask]
        th = theta[shell_mask]
        ph = phi[shell_mask]
        # ℓ=0: monopole (Y_0^0 ∝ const)
        Y00 = 1.0 / np.sqrt(4 * np.pi)
        c00 = float(np.mean(E_at * Y00))
        # ℓ=1: dipoles m=-1,0,1 (real form)
        Y10 = np.sqrt(3 / (4 * np.pi)) * np.cos(th)
        Y11_re = -np.sqrt(3 / (4 * np.pi)) * np.sin(th) * np.cos(ph)
        Y11_im = -np.sqrt(3 / (4 * np.pi)) * np.sin(th) * np.sin(ph)
        c10 = float(np.mean(E_at * Y10))
        c11_re = float(np.mean(E_at * Y11_re))
        c11_im = float(np.mean(E_at * Y11_im))
        # ℓ=2: quadrupole m=0
        Y20 = np.sqrt(5 / (16 * np.pi)) * (3 * np.cos(th)**2 - 1)
        c20 = float(np.mean(E_at * Y20))
        amp_l0 = abs(c00)
        amp_l1 = np.sqrt(c10**2 + c11_re**2 + c11_im**2)
        amp_l2 = abs(c20)
        multipole_E_per_shell[float(r_low + 0.5)] = {
            "ell_0": amp_l0,
            "ell_1": amp_l1,
            "ell_2": amp_l2,
        }
        print(f"    r={r_low+0.5}:  ℓ=0 amp={amp_l0:.4e}, ℓ=1 amp={amp_l1:.4e}, ℓ=2 amp={amp_l2:.4e}")

    # ── A5: Mode adjudication ─────────────────────────────────────────
    print("\n  A5 — Mode I/II/III adjudication")

    # Count PASSes
    passes = []
    fails = []
    if coulomb_slope_pass:
        passes.append("Coulomb slope (β ≈ -2)")
    else:
        fails.append(f"Coulomb slope (β = {slope})" if slope else "Coulomb slope (no fit)")

    if coulomb_r2_pass:
        passes.append(f"Coulomb R² ≥ 0.7 ({r_squared:.3f})")
    else:
        fails.append(f"Coulomb R² ({r_squared:.3f if r_squared else 'no fit'})")

    # Charge sign: positive q → outward E field (E·r̂ > 0); negative → inward
    if slope and r_squared:
        # check sign of E_radial in inner shell
        inner_shell = (r >= 3) & (r < 4) & active_mask
        if int(inner_shell.sum()) > 0:
            r_hat_inner = np.stack([dx, dy, dz], axis=-1) / np.maximum(r[..., None], 1e-30)
            E_radial_inner = np.sum(E_DC * r_hat_inner, axis=-1)[inner_shell].mean()
            if abs(E_radial_inner) > 1e-10:
                charge_sign = "+1" if E_radial_inner > 0 else "-1"
                passes.append(f"Charge sign defined ({charge_sign})")
            else:
                fails.append("Charge sign undefined (|E_radial| ≈ 0)")
        else:
            fails.append("Charge sign undefined (no inner shell)")

    if dipole_slope_pass:
        passes.append("B-field dipole slope (β ≈ -3)")
    else:
        fails.append(f"B-field dipole slope (β = {slope_B})" if slope_B else "B dipole slope (no fit; B may be 0)")

    if dipole_r2_pass:
        passes.append(f"B dipole R² ≥ 0.7 ({r2_B:.3f})")
    else:
        fails.append(f"B dipole R² ({r2_B})" if r2_B else "B dipole R² (no fit)")

    n_pass = len(passes)
    n_fail = len(fails)

    print(f"\n  Pass count: {n_pass} / {n_pass + n_fail}")
    print(f"  Passes:")
    for p in passes:
        print(f"    ✓ {p}")
    print(f"  Fails:")
    for f in fails:
        print(f"    ✗ {f}")

    if n_pass >= 4:
        mode = "I"
        verdict = "Mode I (chair-ring IS an electron by far-field observables)"
    elif n_pass >= 2:
        mode = "II"
        verdict = "Mode II (partial: substrate cavity mode with some electron-like signatures)"
    else:
        mode = "III"
        verdict = "Mode III (chair-ring is NOT an electron; substrate cavity mode only)"

    print(f"\n  Verdict: {verdict}")

    # ── Save results ──────────────────────────────────────────────────
    out = {
        "test": "Control B5: far-field E and B characterization",
        "engine_config": "v8 baseline (UNCHANGED)",
        "elapsed_recording_s": elapsed,
        "n_avg_steps": int(n_avg_steps),
        "centroid": centroid.tolist(),
        "r_bins_centers": r_centers.tolist(),
        "E_mean_per_shell": E_mean_per_shell,
        "E_std_per_shell": E_std_per_shell,
        "B_mean_per_shell": B_mean_per_shell,
        "B_std_per_shell": B_std_per_shell,
        "n_per_shell": n_per_shell,
        "coulomb_fit": {
            "slope_beta": float(slope) if slope else None,
            "r_squared": float(r_squared) if r_squared else None,
            "slope_pass": bool(coulomb_slope_pass),
            "r_squared_pass": bool(coulomb_r2_pass),
        },
        "dipole_fit_B": {
            "slope_beta": float(slope_B) if slope_B else None,
            "r_squared": float(r2_B) if r2_B else None,
            "slope_pass": bool(dipole_slope_pass),
            "r_squared_pass": bool(dipole_r2_pass),
        },
        "flux_per_shell": flux_per_shell,
        "multipole_E_per_shell": multipole_E_per_shell,
        "candidate_spin_axes": {k: v.tolist() for k, v in candidate_axes.items()},
        "passes": passes,
        "fails": fails,
        "n_pass": n_pass,
        "mode": mode,
        "verdict": verdict,
    }
    out_path = out_dir / "r10_v8_ee_phase_a_b5_far_field_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
