"""
Cavitation-core probe — does a self-circulating core reach ρ̄_cav=−1/φ, FLASH/LOCK/CLIP/NO-REACH?
=================================================================================================

Driver for `research/2026-06-10_cavitation-core-probe_prereg.md`.
Engine: `ave.core.cavitation_flow.CavitationFlow2D` (the rarefaction-stiffness bulk-flow branch).

HONEST SCOPE (ave-driver-script-honesty): this script FORWARD-INTEGRATES the compressible
bulk-density flow and CLASSIFIES the outcome against the FROZEN prereg bins. It does NOT fit
to any target. `ρ̄_cav=−1/φ` is a CANDIDATE-CLAIM (Propulsion-derived), used only as the bin
boundary; the verdict is the engine's dynamical behaviour, not a match to it.

Stages:
  A. INSTRUMENT FLOOR (skill A): known-null, known-positive, free-evolution drift.
  B. APPARATUS GATE (STEP 3): sweep the §3 clips 4×each at fixed sub-floor AND super-floor drive;
     map which reading tracks which knob → establish the clip floor the verdict must clear.
  C. THE PROBE (STEP 4): sweep drive amplitude M_edge; record ρ̄_core(t), c_bulk²_core(t), the
     energy ledger (KE,PE), the conserved L, clip hits, pocket structure. Classify.
  D. MATCHED CONTROL: same KE in a curl-free radial breather (ζ=0). Does circulation beat it / the
     prior-art beam floor −0.26?
  E. HYSTERESIS: de-spin a super-floor case; does ρ̄_core recover (reversible/LOCK) or persist (FLASH)?
"""

from __future__ import annotations

import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))

from ave.core.cavitation_flow import RHO_CAV, CavitationFlow2D  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "_output")
os.makedirs(OUT, exist_ok=True)
R_CORE = 0.18


def total_circ(e):
    z = e.vorticity()
    return float(np.sum(z[e.interior]) * e.dx**2)


def run_probe(M_edge, N=160, nsteps=3000, record_every=20, despin_at=None, **knobs):
    """Energize a solid-body rotation column at M_edge; integrate; record time series.
    despin_at: if set (step index), zero the velocity field at that step (hysteresis)."""
    e = CavitationFlow2D(N=N, **knobs)
    e.energize_solid_body(M_edge=M_edge, R_core=R_CORE)
    L0 = e.angular_momentum()
    KE0 = e.kinetic_energy()
    ts = {k: [] for k in ["t", "rho_core", "c2_core_raw", "KE", "PE", "L", "clip_rho", "clip_c2"]}
    deepest = 0.0
    deepest_step = 0
    cross_step = None
    despun = False
    stable = True
    for s in range(nsteps):
        if despin_at is not None and s == despin_at and not despun:
            e.despin(0.0)
            despun = True
        e.step()
        rc = e.rho_core()[0]
        if rc < deepest:
            deepest = rc
            deepest_step = s
        if rc < RHO_CAV and cross_step is None:
            cross_step = s
        if not e.is_stable():
            stable = False
            break
        if s % record_every == 0:
            ts["t"].append(e.t)
            ts["rho_core"].append(rc)
            ts["c2_core_raw"].append(e.c2_core()[0])
            ts["KE"].append(e.kinetic_energy())
            ts["PE"].append(e.compression_pe())
            ts["L"].append(e.angular_momentum())
            ts["clip_rho"].append(e.clip_rho_hits)
            ts["clip_c2"].append(e.clip_c2_hits)
    # pocket structure: # interior cells with raw c_bulk² <= 0 (tensile-failure)
    c2raw_field = e.c_bulk2_raw(e.rho)
    pocket_cells = int(np.count_nonzero((c2raw_field <= 0.0) & e.interior))
    return {
        "M_edge": M_edge,
        "N": N,
        "knobs": knobs,
        "deepest_rho_core": deepest,
        "deepest_step": deepest_step,
        "final_rho_core": e.rho_core()[0],
        "crossed_floor": cross_step is not None,
        "cross_step": cross_step,
        "L0": L0,
        "L_final": e.angular_momentum(),
        "L_drift_pct": 100 * (e.angular_momentum() - L0) / abs(L0) if abs(L0) > 0 else 0.0,
        "KE0": KE0,
        "clip_rho_hits": e.clip_rho_hits,
        "clip_c2_hits": e.clip_c2_hits,
        "pocket_cells": pocket_cells,
        "stable": stable,
        "rho_floor": e.rho_floor,
        "c2_floor": e.c2_floor,
        "max_abs_u_c0": float(np.max(np.abs(e.u))) / e.c0,
        "ts": ts,
    }, e


def stage_A_instrument_floor():
    print("\n=== STAGE A: INSTRUMENT FLOOR (known-null / known-positive / free-drift) ===")
    out = {}
    # known-null
    e = CavitationFlow2D(N=128)
    for _ in range(400):
        e.step()
    out["known_null_rho_core"] = e.rho_core()[0]
    # known-positive: small-M linear centrifugal deficit ~ -O(1)*M^2 ; L conserved
    kp = []
    for M in [0.15, 0.25, 0.35]:
        e = CavitationFlow2D(N=128, nu_art=0.0, rho_diff=5e-4)
        e.energize_solid_body(M_edge=M, R_core=R_CORE)
        L0 = e.angular_momentum()
        deepest = 0.0
        for _ in range(2000):
            e.step()
            deepest = min(deepest, e.rho_core()[0])
        kp.append({"M": M, "deepest": deepest, "deepest_over_M2": deepest / M**2,
                   "L_drift_pct": 100 * (e.angular_momentum() - L0) / abs(L0)})
    out["known_positive"] = kp
    # free-evolution drift: L conservation over long free run (the ledger noise floor)
    e = CavitationFlow2D(N=128, nu_art=0.0)
    e.energize_solid_body(M_edge=0.2, R_core=R_CORE)
    L0 = e.angular_momentum()
    for _ in range(3000):
        e.step()
    out["free_L_drift_pct"] = 100 * (e.angular_momentum() - L0) / abs(L0)
    print(f"  known-null rho_core = {out['known_null_rho_core']:.2e} (expect ~0)")
    for r in kp:
        print(f"  known-positive M={r['M']:.2f}: deepest={r['deepest']:.4f}  deepest/M^2={r['deepest_over_M2']:.3f}  L drift={r['L_drift_pct']:.2f}%")
    print(f"  free-evolution L drift over 3000 steps = {out['free_L_drift_pct']:.3f}%  (energize+lock noise floor)")
    return out


def stage_B_apparatus_gate():
    print("\n=== STAGE B: APPARATUS GATE (sweep clips 4x each, sub-floor AND super-floor drive) ===")
    out = {"sub_floor": {}, "super_floor": {}}
    sweeps = {
        "c2_floor": [1e-4, 1e-3, 1e-2, 5e-2],
        "rho_floor": [-0.99, -0.95, -0.85, -0.75],
        "nu_art": [0.0, 5e-4, 2e-3, 5e-3],
        "rho_diff": [1e-4, 5e-4, 2e-3, 5e-3],
        "N": [128, 160, 192, 224],
    }
    defaults = dict(c2_floor=1e-3, rho_floor=-0.95, nu_art=5e-4, rho_diff=5e-4)
    for regime, M in [("sub_floor", 0.5), ("super_floor", 1.0)]:
        print(f"  -- {regime} (M_edge={M}) --")
        for knob, vals in sweeps.items():
            rows = []
            for val in vals:
                kw = dict(defaults)
                Nuse = 160
                if knob == "N":
                    Nuse = val
                else:
                    kw[knob] = val
                res, _ = run_probe(M, N=Nuse, nsteps=2200, record_every=200, **kw)
                rows.append({"val": val, "deepest": res["deepest_rho_core"],
                             "clip_rho_hits": res["clip_rho_hits"], "clip_c2_hits": res["clip_c2_hits"],
                             "crossed": res["crossed_floor"], "stable": res["stable"],
                             "L_drift_pct": res["L_drift_pct"]})
            out[regime][knob] = rows
            depths = [f"{r['deepest']:.3f}" for r in rows]
            print(f"    {knob:10s} {vals} -> deepest {depths}")
    return out


def stage_C_probe():
    print("\n=== STAGE C: THE PROBE (drive sweep M_edge) ===")
    Ms = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]
    rows = []
    series = {}
    for M in Ms:
        res, _ = run_probe(M, N=160, nsteps=3200, record_every=20, nu_art=5e-4, rho_diff=5e-4)
        rows.append({k: res[k] for k in ["M_edge", "deepest_rho_core", "deepest_step", "final_rho_core",
                                          "crossed_floor", "cross_step", "L_drift_pct", "clip_rho_hits",
                                          "clip_c2_hits", "pocket_cells", "stable", "max_abs_u_c0"]})
        series[f"M={M}"] = res["ts"]
        print(f"  M={M:.1f} | deepest={res['deepest_rho_core']:.4f} | crossed={res['crossed_floor']} "
              f"| pocket_cells={res['pocket_cells']} | rho_clip={res['clip_rho_hits']} c2_clip={res['clip_c2_hits']} "
              f"| L drift={res['L_drift_pct']:.2f}% | stable={res['stable']}")
    return {"rows": rows, "series": series}


def stage_D_matched_control():
    print("\n=== STAGE D: MATCHED CONTROL (same KE, curl-free radial breather, ζ=0) ===")
    out = []
    for M in [0.6, 0.8, 1.0]:
        # vortex KE for this M
        ev = CavitationFlow2D(N=160, nu_art=5e-4, rho_diff=5e-4)
        ev.energize_solid_body(M_edge=M, R_core=R_CORE)
        ke = ev.kinetic_energy()
        deep_v = 0.0
        for _ in range(3200):
            ev.step()
            deep_v = min(deep_v, ev.rho_core()[0])
        # matched breather
        eb = CavitationFlow2D(N=160, nu_art=5e-4, rho_diff=5e-4)
        eb.energize_radial_breather(ke_target=ke, R_core=R_CORE)
        deep_b = 0.0
        for _ in range(3200):
            eb.step()
            deep_b = min(deep_b, eb.rho_core()[0])
        out.append({"M_edge": M, "KE": ke, "vortex_deepest": deep_v, "breather_deepest": deep_b,
                    "beam_prior_art": -0.26})
        print(f"  M={M:.1f} KE={ke:.4f} | vortex deepest={deep_v:.4f} | breather(same KE) deepest={deep_b:.4f} | beam prior-art=-0.26")
    return out


def stage_E_hysteresis():
    print("\n=== STAGE E: HYSTERESIS (de-spin a super-floor case; recover or persist?) ===")
    out = []
    for M in [0.8, 1.0]:
        # find deepest step first
        res0, _ = run_probe(M, N=160, nsteps=3200, record_every=20, nu_art=5e-4, rho_diff=5e-4)
        ds = res0["deepest_step"]
        # de-spin shortly after deepest, then watch recovery
        despin_step = min(ds + 100, 2800)
        res, e = run_probe(M, N=160, nsteps=3600, record_every=20, despin_at=despin_step,
                           nu_art=5e-4, rho_diff=5e-4)
        # rho_core at despin and at end (recovery measure)
        ts = res["ts"]
        rcarr = np.array(ts["rho_core"])
        # nearest recorded index to despin and final
        rc_at_despin = res0["deepest_rho_core"]
        rc_final = rcarr[-1]
        recovered = rc_final > 0.5 * RHO_CAV  # back above half the floor depth => recovered
        out.append({"M_edge": M, "despin_step": despin_step, "rc_deepest": rc_at_despin,
                    "rc_final_after_despin": float(rc_final), "recovered": bool(recovered),
                    "pocket_cells_final": res["pocket_cells"]})
        print(f"  M={M:.1f} despin@{despin_step} | deepest={rc_at_despin:.4f} -> final after de-spin={rc_final:.4f} "
              f"| recovered={recovered} | pocket_cells_final={res['pocket_cells']}")
    return out


def main():
    np.seterr(all="ignore")
    results = {
        "floor_rho_cav": RHO_CAV,
        "A_instrument": stage_A_instrument_floor(),
        "B_gate": stage_B_apparatus_gate(),
        "C_probe": stage_C_probe(),
        "D_control": stage_D_matched_control(),
        "E_hysteresis": stage_E_hysteresis(),
    }
    path = os.path.join(OUT, "cavitation_core_probe_results.json")
    with open(path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nWrote {path}")
    return results


if __name__ == "__main__":
    main()
