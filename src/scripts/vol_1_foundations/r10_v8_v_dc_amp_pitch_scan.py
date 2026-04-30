"""
r10 path α v8 V_DC scaling test — V_AMP and HELICAL_PITCH scan.

Disambiguates substrate-native ratio vs IC-parameter propagation for the
observed per-bond V_DC ≈ V_AMP/6 finding (0.18% match) at v8 baseline
(V_AMP=0.95, HELICAL_PITCH=1/(2π), 200P).

Hypothesis A (substrate-native): per-bond V_DC = V_AMP / 6 always
  (substrate-anchored to chair-ring 6-node perimeter, discrete-π=3 per
  Vol 1 Ch 1:32). Predicts linear scaling with V_AMP, independent of
  HELICAL_PITCH.

Hypothesis B (IC propagation): per-bond V_DC ≈ V_AMP × HELICAL_PITCH × κ
  where κ ≈ 1.046 is rectification factor. Predicts V_DC → 0 at
  HELICAL_PITCH = 0, and V_DC scales jointly with V_AMP × HELICAL_PITCH.

Hypothesis C (saturation-mechanism dominated): V_DC = V_AMP × f(V_AMP/V_yield)
  where f → 0 at low V_AMP and f → 1/6 near saturation. Predicts
  non-linear scaling — V_DC much smaller than V_AMP/6 at V_AMP = 0.5.

Two control runs at 100P each (~135s wall × 2 = ~5 min total):
  Run 1: V_AMP = 0.5, HELICAL_PITCH = 1/(2π)  — V_AMP scan
  Run 2: V_AMP = 0.95, HELICAL_PITCH = 0       — HELICAL_PITCH scan
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


def detrend_with_slope(traj):
    n_steps = traj.shape[0]
    t = np.arange(n_steps, dtype=np.float64)
    t_mean = t.mean()
    t_var = ((t - t_mean) ** 2).sum()
    mean = traj.mean(axis=0)
    slope_num = ((t[:, None, None, None, None] - t_mean) * (traj - mean[None, ...])).sum(axis=0)
    return slope_num / t_var


def run_control(v_amp, helical_pitch, n_periods, label):
    print("=" * 78, flush=True)
    print(f"  V_DC scaling test — {label}")
    print(f"  V_AMP = {v_amp}, HELICAL_PITCH = {helical_pitch:.6f}, recording = {n_periods} P")
    print("=" * 78, flush=True)

    nodes, bonds = v8.build_chair_ring(v8.CENTER)
    a_0_per_node, centroid = v8.compute_a_0_at_ring_nodes(nodes, v_amp, helical_pitch)

    engine = VacuumEngine3D.from_args(
        N=v8.N_LATTICE, pml=v8.PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )
    v8.initialize_helical_beltrami_ic(
        engine, nodes, bonds, a_0_per_node,
        v8.K_BELTRAMI, v_amp, v_amp,  # V_AMP and PHI_AMP both = v_amp
    )

    nx = engine.k4.nx
    n_steps = int(n_periods * v8.COMPTON_PERIOD / v8.DT)
    print(f"Recording {n_steps} steps ({n_periods}P)...", flush=True)
    phi_link_traj = np.zeros((n_steps, nx, nx, nx, 4), dtype=np.float32)

    t0 = time.time()
    last = t0
    for i in range(n_steps):
        engine.step()
        phi_link_traj[i] = engine.k4.Phi_link.astype(np.float32)
        if (time.time() - last) > 30.0:
            print(f"    step {i}/{n_steps}, elapsed {time.time()-t0:.1f}s", flush=True)
            last = time.time()
    elapsed = time.time() - t0
    print(f"  Recording done at {elapsed:.1f}s", flush=True)

    phi_slope = detrend_with_slope(phi_link_traj.astype(np.float64))
    V_DC_per_port = phi_slope / v8.DT  # V_SNAP units

    # Per-bond contributions to ∮V_DC·dl
    contribs = []
    for bnd in bonds:
        ix, iy, iz = bnd["a_site"]
        port = bnd["port"]
        a_to_b = np.array(bnd["a_to_b_offset"], dtype=float)
        a_to_b /= np.linalg.norm(a_to_b)
        traversal = np.array(bnd["traversal_direction"], dtype=float)
        sign = float(np.sign(np.dot(a_to_b, traversal)))
        v_dc_at_port = float(V_DC_per_port[ix, iy, iz, port])
        contrib = sign * v_dc_at_port
        contribs.append({
            "ring_idx": bnd["ring_idx"],
            "a_site": list(bnd["a_site"]),
            "port": port,
            "V_DC_at_port": v_dc_at_port,
            "contribution": contrib,
        })

    # Identify "contributing" bonds (|contribution| > 1% of V_AMP)
    threshold = max(0.01 * v_amp, 1e-5)
    contributing = [c for c in contribs if abs(c["contribution"]) > threshold]
    near_zero = [c for c in contribs if abs(c["contribution"]) <= threshold]

    if contributing:
        per_bond_avg = float(np.mean([abs(c["contribution"]) for c in contributing]))
    else:
        per_bond_avg = 0.0
    loop_total = float(sum(c["contribution"] for c in contribs))

    # Hypothesis predictions
    pred_substrate_per_bond = v_amp / 6.0
    pred_IC_per_bond = v_amp * helical_pitch  # IC propagation
    pred_substrate_loop = 4.0 * v_amp / 6.0    # 4 contributing × V_AMP/6
    pred_IC_loop = 4.0 * v_amp * helical_pitch

    pct_off_substrate = abs(per_bond_avg - pred_substrate_per_bond) / max(pred_substrate_per_bond, 1e-15) * 100
    pct_off_IC = abs(per_bond_avg - pred_IC_per_bond) / max(pred_IC_per_bond, 1e-15) * 100 if pred_IC_per_bond > 1e-15 else float("inf")

    print()
    print(f"  Per-bond contributions ({len(contribs)} bonds):")
    for c in contribs:
        flag = "  *" if abs(c["contribution"]) > threshold else "   "
        print(f"  {flag} bond {c['ring_idx']} (a={c['a_site']}, port={c['port']}): "
              f"contrib={c['contribution']:+.4e}")
    print(f"  Contributing bonds: {len(contributing)} / 6")
    print(f"  Mean |per-bond contribution|: {per_bond_avg:.4e}")
    print(f"  Σ ∮V_DC·dl: {loop_total:+.4e}")
    print()
    print(f"  Hypothesis A (substrate-native V_AMP/6):  pred {pred_substrate_per_bond:.4e}, "
          f"obs {per_bond_avg:.4e}, off {pct_off_substrate:.2f}%")
    if pred_IC_per_bond > 1e-15:
        print(f"  Hypothesis B (IC V_AMP × HELICAL_PITCH):  pred {pred_IC_per_bond:.4e}, "
              f"obs {per_bond_avg:.4e}, off {pct_off_IC:.2f}%")
    else:
        print(f"  Hypothesis B (IC V_AMP × HELICAL_PITCH):  pred 0 (HELICAL_PITCH = 0), "
              f"obs {per_bond_avg:.4e}")
    print()

    return {
        "label": label,
        "V_AMP": v_amp,
        "HELICAL_PITCH": helical_pitch,
        "n_periods": n_periods,
        "n_steps": n_steps,
        "elapsed_s": elapsed,
        "contribs": contribs,
        "n_contributing": len(contributing),
        "per_bond_mean_abs": per_bond_avg,
        "loop_total": loop_total,
        "pred_substrate_per_bond": pred_substrate_per_bond,
        "pred_IC_per_bond": pred_IC_per_bond,
        "pct_off_substrate": pct_off_substrate,
        "pct_off_IC": pct_off_IC if pred_IC_per_bond > 1e-15 else None,
    }


def main():
    n_periods = 100  # half of v8's 200P; slope linear-fit precision still sufficient

    runs = []

    # Run 1: V_AMP scan — half V_AMP, original HELICAL_PITCH
    runs.append(run_control(
        v_amp=0.5, helical_pitch=1.0 / (2.0 * np.pi),
        n_periods=n_periods,
        label="Run 1: V_AMP=0.5, HELICAL_PITCH=1/(2π) (V_AMP scan)",
    ))

    # Run 2: HELICAL_PITCH scan — original V_AMP, zero HELICAL_PITCH
    runs.append(run_control(
        v_amp=0.95, helical_pitch=0.0,
        n_periods=n_periods,
        label="Run 2: V_AMP=0.95, HELICAL_PITCH=0 (HELICAL_PITCH scan)",
    ))

    # ── Cross-run summary ────────────────────────────────────────────────────
    print()
    print("=" * 78, flush=True)
    print("  Cross-run summary")
    print("=" * 78, flush=True)
    print(f"  {'V_AMP':>6} {'PITCH':>8} {'mean|contrib|':>14} {'V_AMP/6 pred':>14} "
          f"{'off %':>7} {'V_AMP×PITCH pred':>17} {'off %':>9}")
    # Existing baseline from prior 200P run for context
    baseline = {
        "label": "Baseline (200P, prior run)",
        "V_AMP": 0.95,
        "HELICAL_PITCH": 1.0 / (2.0 * np.pi),
        "per_bond_mean_abs": 0.15804,
        "n_contributing": 4,
    }
    all_rows = [baseline] + runs
    for r in all_rows:
        v_amp = r["V_AMP"]; pitch = r["HELICAL_PITCH"]
        per_bond = r["per_bond_mean_abs"]
        sub = v_amp / 6.0
        ic = v_amp * pitch
        sub_off = abs(per_bond - sub) / max(sub, 1e-15) * 100
        ic_off = abs(per_bond - ic) / max(ic, 1e-15) * 100 if ic > 1e-15 else float("inf")
        ic_str = f"{ic:.5f}" if ic > 1e-15 else "(IC=0)"
        ic_off_str = f"{ic_off:.2f}" if ic > 1e-15 else "—"
        print(f"  {v_amp:>6.3f} {pitch:>8.5f} {per_bond:>14.5e} {sub:>14.5f} "
              f"{sub_off:>7.2f} {ic_str:>17} {ic_off_str:>9}")
    print()
    print("Verdict logic:")
    print("  - If V_AMP/6 holds across all 3 rows (off < 2%): substrate-native confirmed")
    print("  - If Run 2 (HELICAL_PITCH=0) gives V_DC ≈ 0: IC propagation dominant")
    print("  - If Run 1 (V_AMP=0.5) deviates strongly from V_AMP/6: saturation-mechanism dominated")
    print()

    out = {
        "test": "v8 V_DC scaling test (V_AMP × HELICAL_PITCH scan)",
        "n_periods_per_run": n_periods,
        "baseline_200P_prior": baseline,
        "runs": runs,
    }
    out_path = Path(__file__).parent / "r10_v8_v_dc_amp_pitch_scan_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"Saved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
