#!/usr/bin/env python3
r"""K4 port-level control diagnostic — RF/analog analysis of the electron soliton.

Maps the K4 scatter-connect pipeline as a 4-port microwave network.
Computes the Q-point (bias), per-port power balance, bond reflection
spectrum, and small-signal varactor gain at the soliton boundary.

Tests two configurations:
  Arm A: disable_cosserat_lc_force=True  (Loop 2 CUT — v3 config)
  Arm B: disable_cosserat_lc_force=False (Loop 2 CLOSED — native coupling)
Both with ZERO script-level BEMF feedback.

Output:
  _output/k4_port_control_diagnostic_results.json
  _output/k4_port_control_diagnostic.png
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from native_electron_model import (  # noqa: E402
    N_LATTICE,
    PML,
    SHELL_RADIUS,
    _seed_canonical,
)

from ave.core.constants import ALPHA_COLD, V_SNAP  # noqa: E402
from ave.topological.vacuum_engine import VacuumEngine3D  # noqa: E402

OUT_DIR = next(p for p in Path(__file__).resolve().parents if (p / ".git").exists())
OUT_DIR = OUT_DIR / "src" / "scripts" / "vol_1_foundations" / "_output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

AMPLITUDE = 0.92
N_STEPS = 400
CADENCE = 2


def _build_engine(*, disable_cosserat_lc_force: bool = True) -> VacuumEngine3D:
    """Build the coupled K4-Cosserat engine with configurable Loop 2."""
    return VacuumEngine3D.from_args(
        N=N_LATTICE,
        pml=PML,
        temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=disable_cosserat_lc_force,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
        use_lagrangian_emf_coupling=False,
    )


def _boundary_mask(shape: tuple[int, ...], center: tuple[int, int, int],
                    radius: int, mask_active: np.ndarray) -> np.ndarray:
    """Nodes within [radius-1, radius+1] of center (the soliton boundary shell)."""
    nx, ny, nz = shape[:3]
    cx, cy, cz = center
    ix = np.arange(nx)[:, None, None]
    iy = np.arange(ny)[None, :, None]
    iz = np.arange(nz)[None, None, :]
    r_sq = (ix - cx)**2 + (iy - cy)**2 + (iz - cz)**2
    r = np.sqrt(r_sq)
    shell = (r >= radius - 1.5) & (r <= radius + 1.5) & mask_active
    return shell


def _q_point_snapshot(engine: VacuumEngine3D, center: tuple[int, int, int],
                       radius: int) -> dict[str, Any]:
    """Compute Q-point (bias point) of the soliton at current state.
    
    Returns the operating-point RF parameters at the soliton boundary.
    """
    # Get fields
    V_inc = np.asarray(engine.k4.V_inc)
    V_ref = np.asarray(engine.k4.V_ref)
    z_local = np.asarray(engine.k4.z_local_field)
    mask_A = engine.k4.mask_A
    
    # Voltage squared per node
    v_sq = np.sum(V_inc**2, axis=-1)
    
    # Boundary shell mask
    shell = _boundary_mask(v_sq.shape, center, radius, engine.k4.mask_active)
    core = _boundary_mask(v_sq.shape, center, max(1, radius - 3), engine.k4.mask_active)
    
    # --- Q-point at boundary nodes ---
    z_shell = z_local[shell]
    v_sq_shell = v_sq[shell]
    a_sq_shell = v_sq_shell / (engine.V_SNAP**2)
    
    # z_local at core nodes
    z_core = z_local[core]
    v_sq_core = v_sq[core]
    a_sq_core = v_sq_core / (engine.V_SNAP**2)
    
    # Bond reflection Γ at boundary: core (Z_B ≈ z_core) vs shell (Z_A ≈ 1)
    # Γ = (Z_B - Z_A) / (Z_B + Z_A)
    z_core_mean = float(np.mean(z_core)) if z_core.size > 0 else 1.0
    z_shell_mean = float(np.mean(z_shell)) if z_shell.size > 0 else 1.0
    gamma_boundary = (z_core_mean - z_shell_mean) / (z_core_mean + z_shell_mean + 1e-30)
    
    # Small-signal varactor gain: dz/dA² at the Q-point
    # z = √(S_μ/S_ε); for simplicity use the legacy formula z = (1-A²)^{-1/4}
    # dz/dA² = (1/4)(1-A²)^{-5/4} = z^5 / 4
    a_sq_mean = float(np.mean(a_sq_core)) if a_sq_core.size > 0 else 0.0
    s_eps = math.sqrt(max(1.0 - a_sq_mean, 1e-12))
    dz_dA2 = z_core_mean**5 / 4.0 if z_core_mean > 0 else 0.0
    
    # VCA equivalent circuit at Q-point
    # C_eff/C_0 = 1/S_ε (varactor)
    c_eff_ratio = 1.0 / max(s_eps, 1e-12)
    
    # Per-port power balance at boundary
    port_power = {}
    for port in range(4):
        p_inc = float(np.mean(V_inc[shell, port]**2)) if shell.any() else 0.0
        p_ref = float(np.mean(V_ref[shell, port]**2)) if shell.any() else 0.0
        port_power[f"port_{port}"] = {
            "P_inc": p_inc,
            "P_ref": p_ref,
            "P_absorbed": p_inc - p_ref,
            "reflection_ratio": p_ref / max(p_inc, 1e-30),
        }
    
    # Total power balance
    p_inc_total = sum(pp["P_inc"] for pp in port_power.values())
    p_ref_total = sum(pp["P_ref"] for pp in port_power.values())
    
    return {
        "z_local_core_mean": z_core_mean,
        "z_local_shell_mean": z_shell_mean,
        "A_sq_core_mean": a_sq_mean,
        "S_eps_core": s_eps,
        "gamma_boundary": gamma_boundary,
        "dz_dA2_small_signal": dz_dA2,
        "C_eff_over_C0": c_eff_ratio,
        "port_power": port_power,
        "P_inc_total": p_inc_total,
        "P_ref_total": p_ref_total,
        "P_absorbed_total": p_inc_total - p_ref_total,
        "eps_gamma": 1.0 - gamma_boundary**2,
    }


def run_arm(name: str, *, disable_cosserat_lc_force: bool) -> dict[str, Any]:
    """Run one diagnostic arm: seed soliton, evolve, record port diagnostics."""
    print(f"\n{'='*60}")
    print(f"ARM: {name}")
    print(f"  disable_cosserat_lc_force = {disable_cosserat_lc_force}")
    print(f"  Script-level BEMF = OFF")
    print(f"{'='*60}")
    
    engine = _build_engine(disable_cosserat_lc_force=disable_cosserat_lc_force)
    _seed_canonical(engine, amplitude=AMPLITUDE)
    
    center = (N_LATTICE // 2, N_LATTICE // 2, N_LATTICE // 2)
    
    # Time series for frequency analysis (per-port voltage at one boundary node)
    # Pick a node on the boundary shell
    shell = _boundary_mask(
        (N_LATTICE, N_LATTICE, N_LATTICE), center,
        SHELL_RADIUS, engine.k4.mask_active
    )
    boundary_nodes = np.argwhere(shell)
    if len(boundary_nodes) == 0:
        raise RuntimeError("No boundary nodes found")
    # Pick the node closest to the +x boundary (for reproducibility)
    probe_idx = boundary_nodes[np.argmax(boundary_nodes[:, 0])]
    probe = tuple(probe_idx)
    print(f"  Probe node: {probe}")
    
    # Storage
    records: list[dict[str, Any]] = []
    port_v_inc_ts: list[list[float]] = [[] for _ in range(4)]
    port_v_ref_ts: list[list[float]] = [[] for _ in range(4)]
    z_local_ts: list[float] = []
    omega_max_ts: list[float] = []
    gamma_ts: list[float] = []
    e_k4_ts: list[float] = []
    e_cos_ts: list[float] = []
    times: list[float] = []
    
    print(f"  Running {N_STEPS} steps (cadence={CADENCE})...", flush=True)
    
    for step in range(N_STEPS + 1):
        if step % CADENCE == 0:
            # Update z_local for diagnostics
            engine._coupled._update_z_local_total()
            
            V_inc = np.asarray(engine.k4.V_inc)
            V_ref = np.asarray(engine.k4.V_ref)
            z_local = np.asarray(engine.k4.z_local_field)
            
            # Probe node time series
            for port in range(4):
                port_v_inc_ts[port].append(float(V_inc[probe[0], probe[1], probe[2], port]))
                port_v_ref_ts[port].append(float(V_ref[probe[0], probe[1], probe[2], port]))
            z_local_ts.append(float(z_local[probe[0], probe[1], probe[2]]))
            
            # Cosserat spin
            omega = np.asarray(engine.cos.omega)
            omega_max = float(np.linalg.norm(omega, axis=-1).max())
            omega_max_ts.append(omega_max)
            
            # Q-point snapshot every 20 cadences
            if step % (CADENCE * 20) == 0:
                qp = _q_point_snapshot(engine, center, SHELL_RADIUS)
                gamma_ts.append(qp["gamma_boundary"])
                e_k4_ts.append(float(engine._coupled.k4_energy()))
                e_cos_ts.append(float(engine._coupled.cosserat_energy()))
                records.append({
                    "step": step,
                    "q_point": qp,
                    "omega_max": omega_max,
                    "E_k4": e_k4_ts[-1],
                    "E_cos": e_cos_ts[-1],
                })
                print(f"    Step {step}: z_core={qp['z_local_core_mean']:.4f} "
                      f"Γ={qp['gamma_boundary']:.4f} "
                      f"ε̄={qp['eps_gamma']:.6f} "
                      f"|ω|_max={omega_max:.4f} "
                      f"E_K4={e_k4_ts[-1]:.4f} E_Cos={e_cos_ts[-1]:.6f}",
                      flush=True)
            
            times.append(step)
        
        # Step the engine — NO script-level BEMF
        if step < N_STEPS:
            engine.step()
    
    # --- Frequency analysis ---
    dt_sample = CADENCE * float(engine._coupled.outer_dt)
    fs = 1.0 / dt_sample  # sampling frequency
    
    fft_results = {}
    for port in range(4):
        v_inc_arr = np.array(port_v_inc_ts[port])
        v_ref_arr = np.array(port_v_ref_ts[port])
        
        # Window and FFT
        n_samples = len(v_inc_arr)
        window = np.hanning(n_samples)
        
        fft_inc = np.fft.rfft(v_inc_arr * window)
        fft_ref = np.fft.rfft(v_ref_arr * window)
        freqs = np.fft.rfftfreq(n_samples, d=dt_sample)
        
        # Transfer function H(f) = V_ref(f) / V_inc(f)
        H = fft_ref / (fft_inc + 1e-30)
        
        fft_results[f"port_{port}"] = {
            "freqs": freqs.tolist(),
            "V_inc_spectrum_dB": (20 * np.log10(np.abs(fft_inc) + 1e-30)).tolist(),
            "V_ref_spectrum_dB": (20 * np.log10(np.abs(fft_ref) + 1e-30)).tolist(),
            "H_magnitude_dB": (20 * np.log10(np.abs(H) + 1e-30)).tolist(),
            "H_phase_deg": (np.angle(H, deg=True)).tolist(),
        }
    
    # Final Q-point
    engine._coupled._update_z_local_total()
    final_qp = _q_point_snapshot(engine, center, SHELL_RADIUS)
    
    # Omega persistence
    omega0 = float(np.linalg.norm(np.asarray(engine.cos.omega), axis=-1).max())
    omega_init = omega_max_ts[0] if omega_max_ts else 1e-30
    omega_persist = omega0 / max(omega_init, 1e-30)
    
    result = {
        "arm": name,
        "disable_cosserat_lc_force": disable_cosserat_lc_force,
        "script_level_bemf": False,
        "amplitude": AMPLITUDE,
        "n_steps": N_STEPS,
        "n_lattice": N_LATTICE,
        "probe_node": list(probe),
        "final_q_point": final_qp,
        "omega_persistence_ratio": omega_persist,
        "records": records,
        "fft_results": fft_results,
        "port_v_inc_ts": port_v_inc_ts,
        "port_v_ref_ts": port_v_ref_ts,
        "z_local_ts": z_local_ts,
        "omega_max_ts": omega_max_ts,
        "times": times,
        "sampling_freq": fs,
    }
    
    print(f"\n  FINAL: Γ_boundary={final_qp['gamma_boundary']:.4f} "
          f"ε̄={final_qp['eps_gamma']:.6f} "
          f"ω_persist={omega_persist:.3f}×")
    
    return result


def plot_results(results: list[dict[str, Any]], out_path: Path) -> None:
    """Generate the multi-panel RF diagnostic plot."""
    n_arms = len(results)
    fig, axes = plt.subplots(3, n_arms, figsize=(7 * n_arms, 14))
    fig.patch.set_facecolor("#0a0a12")
    if n_arms == 1:
        axes = axes[:, None]
    
    colors = ["#ff6b6b", "#4ecdc4", "#ffe66d", "#a29bfe"]
    
    for col, res in enumerate(results):
        arm_label = res["arm"]
        times = res["times"]
        
        # --- Row 0: Per-port V_inc time series + z_local ---
        ax0 = axes[0, col]
        ax0.set_facecolor("#111118")
        for port in range(4):
            ax0.plot(times, res["port_v_inc_ts"][port],
                     color=colors[port], alpha=0.7, linewidth=0.8,
                     label=f"Port {port}")
        ax0_twin = ax0.twinx()
        ax0_twin.plot(times, res["z_local_ts"], color="white", linewidth=1.5,
                      linestyle="--", alpha=0.8, label="z_local")
        ax0.set_title(f"{arm_label}\nPort V_inc + z_local (probe node)",
                      color="#ddd", fontsize=11)
        ax0.set_xlabel("Step", color="#999")
        ax0.set_ylabel("V_inc", color="#999")
        ax0_twin.set_ylabel("z_local", color="white")
        ax0.legend(loc="upper left", fontsize=7, facecolor="#222")
        ax0.tick_params(colors="#999")
        ax0_twin.tick_params(colors="#999")
        
        # --- Row 1: Bode magnitude (per-port transfer function) ---
        ax1 = axes[1, col]
        ax1.set_facecolor("#111118")
        fft = res["fft_results"]
        for port in range(4):
            key = f"port_{port}"
            freqs = fft[key]["freqs"]
            H_dB = fft[key]["H_magnitude_dB"]
            ax1.plot(freqs[1:], H_dB[1:], color=colors[port], alpha=0.8,
                     linewidth=1.0, label=f"Port {port}")
        ax1.axhline(y=0, color="white", linestyle=":", alpha=0.3, linewidth=0.5)
        ax1.set_title("Bode: |H(f)| = |V_ref/V_inc| (dB)", color="#ddd", fontsize=11)
        ax1.set_xlabel("Frequency (1/step)", color="#999")
        ax1.set_ylabel("|H| (dB)", color="#999")
        ax1.legend(loc="upper right", fontsize=7, facecolor="#222")
        ax1.tick_params(colors="#999")
        
        # --- Row 2: Energy + Omega ---
        ax2 = axes[2, col]
        ax2.set_facecolor("#111118")
        ax2.plot(times, res["omega_max_ts"], color="#ff6b6b", linewidth=1.5,
                 label="|ω|_max")
        ax2.set_ylabel("|ω|_max", color="#ff6b6b")
        ax2.tick_params(axis="y", colors="#ff6b6b")
        
        if res["records"]:
            rec_steps = [r["step"] for r in res["records"]]
            e_k4 = [r["E_k4"] for r in res["records"]]
            e_cos = [r["E_cos"] for r in res["records"]]
            gammas = [r["q_point"]["gamma_boundary"] for r in res["records"]]
            
            ax2_twin = ax2.twinx()
            ax2_twin.plot(rec_steps, gammas, color="#4ecdc4", linewidth=1.5,
                          marker="o", markersize=3, label="Γ_boundary")
            ax2_twin.set_ylabel("Γ_boundary", color="#4ecdc4")
            ax2_twin.tick_params(axis="y", colors="#4ecdc4")
            ax2_twin.legend(loc="upper right", fontsize=7, facecolor="#222")
        
        ax2.set_title("Spin (|ω|) + Boundary Γ", color="#ddd", fontsize=11)
        ax2.set_xlabel("Step", color="#999")
        ax2.legend(loc="upper left", fontsize=7, facecolor="#222")
        ax2.tick_params(axis="x", colors="#999")
    
    fig.suptitle("K4 Port-Level Control Diagnostic\n"
                 "RF Analysis of Electron Soliton (A = 0.92, N = 32, no script BEMF)",
                 color="#eee", fontsize=14, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(out_path, dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved figure to {out_path}")


def main() -> None:
    print("K4 Port-Level Control Diagnostic")
    print(f"  N={N_LATTICE}, A={AMPLITUDE}, steps={N_STEPS}, cadence={CADENCE}")
    print(f"  V_SNAP = {V_SNAP:.1f} V")
    print(f"  α_cold = {ALPHA_COLD:.10f}")
    
    # Arm A: Loop 2 CUT (current v3 config)
    arm_a = run_arm("Arm_A_Loop2_CUT", disable_cosserat_lc_force=True)
    
    # Arm B: Loop 2 CLOSED (native coupling)
    arm_b = run_arm("Arm_B_Loop2_CLOSED", disable_cosserat_lc_force=False)
    
    results = [arm_a, arm_b]
    
    # Summary comparison
    print("\n" + "=" * 70)
    print("SUMMARY: Loop 2 Comparison")
    print("=" * 70)
    print(f"{'Metric':<30} {'Arm A (CUT)':<20} {'Arm B (CLOSED)':<20}")
    print("-" * 70)
    for key in ["gamma_boundary", "eps_gamma", "z_local_core_mean",
                "P_absorbed_total", "C_eff_over_C0", "dz_dA2_small_signal"]:
        va = arm_a["final_q_point"].get(key, "N/A")
        vb = arm_b["final_q_point"].get(key, "N/A")
        if isinstance(va, float):
            print(f"  {key:<28} {va:<20.6f} {vb:<20.6f}")
        else:
            print(f"  {key:<28} {va!s:<20} {vb!s:<20}")
    print(f"  {'omega_persist':<28} {arm_a['omega_persistence_ratio']:<20.4f} {arm_b['omega_persistence_ratio']:<20.4f}")
    print(f"  {'target α':<28} {ALPHA_COLD:<20.10f}")
    
    # Save
    out_json = OUT_DIR / "k4_port_control_diagnostic_results.json"
    # Remove numpy arrays for JSON serialization
    for r in results:
        for key in ["port_v_inc_ts", "port_v_ref_ts", "z_local_ts",
                     "omega_max_ts", "times"]:
            if key in r:
                r[key] = [float(x) if isinstance(x, (float, np.floating)) else
                          [float(y) for y in x] if isinstance(x, list) and x and isinstance(x[0], list) else
                          [float(y) for y in x] if isinstance(x, list) else x
                          for x in r[key]] if isinstance(r[key], list) else r[key]
    
    out_json.write_text(json.dumps(
        {"arms": results, "alpha_target": float(ALPHA_COLD)},
        indent=2, allow_nan=False, default=str
    ) + "\n")
    print(f"\nSaved JSON to {out_json}")
    
    # Plot
    plot_results(results, OUT_DIR / "k4_port_control_diagnostic.png")


if __name__ == "__main__":
    main()
