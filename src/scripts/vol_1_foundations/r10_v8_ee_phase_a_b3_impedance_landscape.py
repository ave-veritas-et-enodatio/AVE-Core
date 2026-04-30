"""
r10 EE Phase A — Control B3: impedance landscape characterization.

Per Grant 2026-04-29 directive + doc 94 §10 Q4: extends Phase A capture
to record the cavity's IMPEDANCE LANDSCAPE per ring node — the substrate
quantities that define the saturation walls (Γ → -1) and bond-LC
behavior. Until now we measured WAVES (V_inc, V_ref, ω) but never the
MEDIUM characteristics that those waves see.

Captured per ring node per step:
  - S_field[node]: Axiom 4 saturation factor S(A) = √(1 - A²/A_yield²)
                   At saturation: S → 0 → ε_eff → 0 → c_eff → 0 → Γ → -1
  - z_local[node]: normalized impedance Z_eff/Z_0 (= 1/√S per Op14)
  - Γ_port[node, port]: per-port reflection coefficient = V_ref/V_inc
  - I_port[node, port]: per-port current = (V_inc - V_ref)/Z_0
  - P_port[node, port]: per-port instantaneous real power = V_total · I_port

Tests:
  T1 — does S_field per ring node show ℓ=2 azimuthal antinode structure?
       (2 antinodes around the loop = alternating high/low pattern at every
        3 nodes; observed V_DC pattern A_0 ≡ A_4 ≠ A_2 is consistent)
  T2 — does Γ_port at ring nodes confirm Γ → -1 reflective wall structure
       at the 4 contributing bond ports + Γ ≈ 0 at the 2 null ports?
  T3 — does ⟨P_port⟩ time-averaged confirm the §6 real-vs-reactive
       asymmetry as ℓ=2 antinode imprint?
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
    print("  r10 EE Phase A — Control B3: impedance landscape")
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
    print(f"Recording {N_STEPS} steps with impedance instrumentation...", flush=True)

    # Wave-field captures (same as before, for cross-check)
    v_inc = np.zeros((N_STEPS, 6, 4), dtype=np.float32)
    v_ref = np.zeros((N_STEPS, 6, 4), dtype=np.float32)
    # NEW: impedance landscape per ring node
    s_field = np.zeros((N_STEPS, 6), dtype=np.float32)
    z_local = np.zeros((N_STEPS, 6), dtype=np.float32)

    t0 = time.time()
    last = t0
    for i in range(N_STEPS):
        engine.step()
        for n_idx, node in enumerate(nodes):
            ix, iy, iz = node
            v_inc[i, n_idx, :] = engine.k4.V_inc[ix, iy, iz, :]
            v_ref[i, n_idx, :] = engine.k4.V_ref[ix, iy, iz, :]
            s_field[i, n_idx] = engine.k4.S_field[ix, iy, iz]
            z_local[i, n_idx] = engine.k4.z_local_field[ix, iy, iz]
        if (time.time() - last) > 30.0:
            t_p = (i + 1) * v8.DT / v8.COMPTON_PERIOD
            print(f"    step {i}/{N_STEPS}, t={t_p:.1f}P, elapsed {time.time()-t0:.1f}s",
                  flush=True)
            last = time.time()
    elapsed = time.time() - t0
    print(f"  Recording done at {elapsed:.1f}s", flush=True)

    sw_start = N_STEPS // 4
    print(f"Steady-state window: steps [{sw_start}, {N_STEPS})")

    # ── T1: S_field per ring node ──────────────────────────────────────────
    s_mean_per_node = s_field[sw_start:].mean(axis=0)         # (6,)
    s_std_per_node = s_field[sw_start:].std(axis=0)
    print()
    print("  T1 — Saturation factor S(A) per ring node (steady-state):")
    print("    (S → 0 means full saturation, S → 1 means linear vacuum)")
    for i in range(6):
        node_type = "A" if all(c % 2 == 0 for c in nodes[i]) else "B"
        print(f"    node {i} ({node_type}): ⟨S⟩ = {s_mean_per_node[i]:.4f} ± {s_std_per_node[i]:.4f}")

    # Azimuthal Fourier decomposition: project ⟨S⟩(node) onto cos(ℓ·θ_n) for ℓ=0..3
    # θ_n = 2π·n/6 for ring node n
    azimuth = 2 * np.pi * np.arange(6) / 6
    print()
    print("  T1 — Azimuthal Fourier coefficients of ⟨S⟩(node):")
    print("    (ℓ=2 antinode structure expected if V-sector mode is GW analog)")
    for ell in range(4):
        c_ell = np.sum(s_mean_per_node * np.cos(ell * azimuth)) / 6.0
        s_ell = np.sum(s_mean_per_node * np.sin(ell * azimuth)) / 6.0
        amp = np.sqrt(c_ell**2 + s_ell**2) * (1 if ell == 0 else 2)
        print(f"    ℓ={ell}: cos coeff={c_ell:+.4e}, sin coeff={s_ell:+.4e}, |amp|={amp:.4e}")

    # ── T2: Γ_port = V_ref/V_inc per port at ring nodes ────────────────────
    # Time-averaged in steady state
    v_inc_rms = np.sqrt((v_inc[sw_start:] ** 2).mean(axis=0))
    v_ref_rms = np.sqrt((v_ref[sw_start:] ** 2).mean(axis=0))

    # Per-port Γ from RMS magnitudes (sign info lost — compute also from per-step then averaged)
    gamma_rms = v_ref_rms / np.maximum(v_inc_rms, 1e-30)

    # Per-step Γ averaged (with sign): compute per-step Γ, then mean
    gamma_per_step = v_ref[sw_start:] / np.maximum(np.abs(v_inc[sw_start:]), 1e-30) * np.sign(v_inc[sw_start:])
    gamma_signed_mean = gamma_per_step.mean(axis=0)

    print()
    print("  T2 — Reflection coefficient Γ_port per ring node (steady-state):")
    print("    (Γ → -1 means perfect reflection / saturated wall)")
    for n_idx in range(6):
        node_type = "A" if all(c % 2 == 0 for c in nodes[n_idx]) else "B"
        gammas_str = " ".join([f"{gamma_signed_mean[n_idx, p]:+.3f}" for p in range(4)])
        rms_str = " ".join([f"{gamma_rms[n_idx, p]:.3f}" for p in range(4)])
        print(f"    node {n_idx} ({node_type}): Γ_signed = [{gammas_str}], |Γ|_rms = [{rms_str}]")

    # ── T3: per-port real power flux ⟨V_inc² - V_ref²⟩ ─────────────────────
    v_inc_sq = (v_inc[sw_start:] ** 2).mean(axis=0)  # (6, 4)
    v_ref_sq = (v_ref[sw_start:] ** 2).mean(axis=0)
    real_power = v_inc_sq - v_ref_sq                  # (6, 4) - per-port net flux
    real_power_rel = real_power / np.maximum(v_inc_sq + v_ref_sq, 1e-30)

    print()
    print("  T3 — Real power flux per port (V_inc² - V_ref²)/Z₀ relative:")
    print("    (~0 means pure reactive, non-zero means net real flux through port)")
    for n_idx in range(6):
        node_type = "A" if all(c % 2 == 0 for c in nodes[n_idx]) else "B"
        rel_str = " ".join([f"{real_power_rel[n_idx, p]:+.3f}" for p in range(4)])
        print(f"    node {n_idx} ({node_type}): rel = [{rel_str}]")

    # Real-power azimuthal decomp on summed ports per node
    real_power_per_node = real_power.sum(axis=1)  # (6,)
    print()
    print("  T3 — Real power per ring node (port-summed):")
    for n_idx in range(6):
        print(f"    node {n_idx}: {real_power_per_node[n_idx]:+.4e}")
    print()
    print("  T3 — Azimuthal Fourier of real_power(node):")
    for ell in range(4):
        c_ell = np.sum(real_power_per_node * np.cos(ell * azimuth)) / 6.0
        s_ell = np.sum(real_power_per_node * np.sin(ell * azimuth)) / 6.0
        amp = np.sqrt(c_ell**2 + s_ell**2) * (1 if ell == 0 else 2)
        print(f"    ℓ={ell}: cos={c_ell:+.4e}, sin={s_ell:+.4e}, |amp|={amp:.4e}")

    # ── Output ─────────────────────────────────────────────────────────────
    out = {
        "test": "Control B3: impedance landscape characterization",
        "elapsed_recording_s": elapsed,
        "n_steps": N_STEPS,
        "s_field_mean_per_node": s_mean_per_node.tolist(),
        "s_field_std_per_node": s_std_per_node.tolist(),
        "s_field_azimuthal_coeffs": [
            {
                "ell": ell,
                "cos_coeff": float(np.sum(s_mean_per_node * np.cos(ell * azimuth)) / 6.0),
                "sin_coeff": float(np.sum(s_mean_per_node * np.sin(ell * azimuth)) / 6.0),
                "amplitude": float(np.sqrt(
                    (np.sum(s_mean_per_node * np.cos(ell * azimuth)) / 6.0) ** 2
                    + (np.sum(s_mean_per_node * np.sin(ell * azimuth)) / 6.0) ** 2
                ) * (1 if ell == 0 else 2)),
            }
            for ell in range(4)
        ],
        "z_local_mean_per_node": z_local[sw_start:].mean(axis=0).tolist(),
        "gamma_signed_mean_per_node_port": gamma_signed_mean.tolist(),
        "gamma_rms_per_node_port": gamma_rms.tolist(),
        "real_power_signature_per_node_port": real_power.tolist(),
        "real_power_relative_per_node_port": real_power_rel.tolist(),
        "real_power_per_node_summed": real_power_per_node.tolist(),
        "real_power_azimuthal_coeffs": [
            {
                "ell": ell,
                "cos_coeff": float(np.sum(real_power_per_node * np.cos(ell * azimuth)) / 6.0),
                "sin_coeff": float(np.sum(real_power_per_node * np.sin(ell * azimuth)) / 6.0),
                "amplitude": float(np.sqrt(
                    (np.sum(real_power_per_node * np.cos(ell * azimuth)) / 6.0) ** 2
                    + (np.sum(real_power_per_node * np.sin(ell * azimuth)) / 6.0) ** 2
                ) * (1 if ell == 0 else 2)),
            }
            for ell in range(4)
        ],
    }
    out_path = Path(__file__).parent / "r10_v8_ee_phase_a_b3_impedance_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
