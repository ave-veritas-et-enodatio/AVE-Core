"""
T-ST in Corpus Vacuum v4 — Chronic Saturation Regime (T=5.8e-5).

Auditor's original chronic-saturation target (Flag 3 second test).
Per Vol 1 Ch 8:218 "extreme thermal energy" framing — particle
collider / hot early universe / BH-interior plasma equivalent.

mean A² = 4·(4π·T/α)·V_SNAP² = 0.40 at T=5.8e-5
A²_op14 saturation threshold = 0.121
Ratio: 3.3× above threshold → ALL CELLS in saturation at IC

Substrate-everywhere-Op14-walls regime. Different physics class than
cusp regime (T=1.76e-5 stochastic) or formation-statistically-forbidden
(T<1e-5).

Stability check: T=5.8e-5 / α/(4π) = 5.8e-5 / 5.8e-4 = 0.1, well within
docstring's stability bound (T < α/(4π) ≈ 5.8e-4 to keep σ_V < V_SNAP).
σ_V_per_port at T=5.8e-5 = 0.316 V_SNAP, σ_V_RMS_4port = 0.63 V_SNAP.

Same Configuration as cusp/CMB tests except T.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
from ave.topological.vacuum_engine import VacuumEngine3D, SpatialDipoleCPSource

from ave.core.constants import ALPHA
V_YIELD = float(np.sqrt(ALPHA))
A2_OP14 = float(np.sqrt(2.0 * ALPHA))
OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi
DT = 1.0 / np.sqrt(2.0)
T_CHRONIC = 5.8e-5


def main():
    print("=" * 78, flush=True)
    print(f"  T-ST Chronic Saturation (T={T_CHRONIC:.2e}) — substrate everywhere in Op14")
    print("=" * 78, flush=True)

    N, PML = 48, 4
    n_steps = int(50 * COMPTON_PERIOD / DT)

    sigma_V_per_port = float(np.sqrt(4.0 * np.pi * T_CHRONIC / ALPHA))
    print(f"  σ_V per port = {sigma_V_per_port:.4f} V_SNAP")
    print(f"  predicted mean A² = {4 * sigma_V_per_port**2:.4f} (vs A²_op14={A2_OP14:.4f})")

    t_start = time.time()
    engine = VacuumEngine3D.from_args(
        N=N, pml=PML, temperature=T_CHRONIC,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )
    engine.initialize_thermal(T_CHRONIC, seed=42, thermalize_V=True)

    source = SpatialDipoleCPSource(
        x0=8, propagation_axis=0, amplitude=0.10, omega=OMEGA_C,
        handedness="RH", sigma_yz=4.0,
        t_ramp=2.0 * COMPTON_PERIOD, t_sustain=2.0 * COMPTON_PERIOD,
        t_decay=2.0 * COMPTON_PERIOD,
    )
    engine.add_source(source)

    sat_traj = []
    for step_i in range(n_steps):
        engine.step()
        if step_i % 5 == 0:
            t_now = step_i * DT
            a2 = np.sum(engine.k4.V_inc ** 2, axis=-1)
            mask = engine.k4.mask_active
            a2_int = a2 * mask.astype(float)
            a2_int[:PML, :, :] = 0; a2_int[N-PML:, :, :] = 0
            a2_int[:, :PML, :] = 0; a2_int[:, N-PML:, :] = 0
            a2_int[:, :, :PML] = 0; a2_int[:, :, N-PML:] = 0
            n_sat = int(np.sum(a2_int > A2_OP14))
            interior_count = int(np.sum(mask)) - 6 * (N**2 * PML)
            frac_sat = n_sat / max(interior_count, 1)
            a2_max = float(a2_int.max())
            a2_mean = float(a2_int[a2_int > 0].mean()) if (a2_int > 0).any() else 0.0
            sat_traj.append({
                "t": float(t_now), "n_sat": n_sat, "frac_sat": frac_sat,
                "a2_max": a2_max, "a2_mean": a2_mean,
            })
            if step_i % 50 == 0:
                t_p = t_now / COMPTON_PERIOD
                print(f"    t={t_p:5.2f}P  n_sat={n_sat:>6}  frac={frac_sat:.3f}  "
                      f"A²_max={a2_max:.3f}  A²_mean={a2_mean:.3f}  "
                      f"({time.time() - t_start:.0f}s)", flush=True)

    elapsed = time.time() - t_start
    print(f"\n  Engine evolution complete in {elapsed:.0f}s")

    max_n_sat = max(s["n_sat"] for s in sat_traj)
    max_frac_sat = max(s["frac_sat"] for s in sat_traj)
    try:
        c_op10 = int(engine.cos.extract_crossing_count())
    except Exception:
        c_op10 = -1

    print(f"\n  Max simultaneously-saturated cells: {max_n_sat}")
    print(f"  Max fraction saturated: {max_frac_sat:.4f}")
    print(f"  Op10 c = {c_op10}")
    print(f"  H_self_trap (saturation+c=3): "
          f"{'PASS' if max_n_sat > 0 and c_op10 == 3 else 'FAIL'}")

    out = {
        "test": "T-ST Chronic (T=5.8e-5)",
        "T": T_CHRONIC,
        "max_n_sat": max_n_sat,
        "max_frac_sat": float(max_frac_sat),
        "c_op10": c_op10,
        "saturation_trajectory": sat_traj,
        "elapsed_total_s": float(elapsed),
    }
    out_path = Path(__file__).parent / "r10_v8_t_st_corpus_vacuum_v4_chronic_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
