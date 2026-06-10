"""
BEMF-feedback SMOKE driver (prereg 2026-06-10_bemf-feedback-smoke).

Tests whether the INDUCTIVE back-EMF reaction-half (CrystalGraftBEMF, derived from
the single Lagrangian L_BEMF = κ_L∫g[w·∇×ω]V̇ — the velocity-sector mirror of the
v4 buckle) SATURATES the v4 |L_ω| runaway, PAYS (source→circulation reactive
transfer, drive≈BEMF), and whether ANTI-LENZ (sign-flip) detonates FASTER.

Unified single-trajectory method (EXACT vs the v4 separate-run doubling): one
1200-step run per arm, running |L_ω|_max checkpointed at 300/600/1200 ⇒ ratio_4L
= L_max(1200)/L_max(300). The OFF arm reproduces the v4 baseline 5.035 (verified).

ALL numbers from the EVOLVED field (ave-driver-script-honesty). No frozen toys.
"""
from __future__ import annotations

import json
import os
import sys
import time

import numpy as np

from ave.core.crystal_graft_bemf import CrystalGraftBEMF

# ── FROZEN CONFIG (the v4 RH runaway config, prereg §2; UNCHANGED across arms) ──
N_GRID = 72
LOCK_ETA_V4 = 0.05            # the v4 frozen lock (the ad-hoc damper)
KAPPA_TILDE = 6.0 / 5.0       # pq/(p+q) — α-FREE
CFG = dict(
    source_mode="abc", lam_sign=1, p=2, q=3, S_min=2e-3, A_cap=0.999, omega_gap=1.0,
    wall_center=0.62, wall_width=0.30, kappa_tilde=KAPPA_TILDE, pml_thickness=6,
)
SEED_BREATHER = dict(sigma=14.0, frac=0.999)
SEED_PHOTON = dict(sigma=9.0, wavelength=10.0, amplitude=0.35)
KAPPA_L = 1.2                 # DERIVED gain = κ̃=6/5 (inductive half of the SAME coupling)
SAT_TOL = 1.3                 # |L_ω| doubling-ratio STOP gate (→1.0 = saturated)
N_STEPS = 1200
CHK = (300, 600, 1200)
CADENCE = 10


def build(*, bemf_kappa, lock_eta, with_photon=True, N=N_GRID):
    ic = N // 2
    e = CrystalGraftBEMF(N=N, bemf_kappa=bemf_kappa, lock_on=(lock_eta > 0),
                         lock_eta=lock_eta, photon_coupling=True, photon_deplete=False,
                         buckle_on=True, **CFG)
    e.seed_bulk((ic, ic, ic), **SEED_BREATHER)
    if with_photon:
        e.seed_photon((ic, ic, ic), helicity=1.0, **SEED_PHOTON)
    else:
        e.helicity = 0.0
    e.freeze_wall_window()
    return e


def run_arm(*, bemf_kappa, lock_eta, with_photon=True, n_steps=N_STEPS, record=True):
    """One 1200-step trajectory; running |L_ω|_max checkpoints + full ledger series."""
    e = build(bemf_kappa=bemf_kappa, lock_eta=lock_eta, with_photon=with_photon)
    se0 = e.stencil_energy()
    Lmax = {c: 0.0 for c in CHK}
    run_L = 0.0
    series = {k: [] for k in ("t", "EV", "Eom", "Hc", "Ew", "Lom", "Hbel",
                              "bemf_emf", "drive", "workV", "workOm", "tauzx", "maxom")}
    t_start = time.time()
    for s in range(1, n_steps + 1):
        e.step()
        run_L = max(run_L, e.spin_L_omega())
        if s in Lmax:
            Lmax[s] = run_L
        if record and (s % CADENCE == 0 or s == 1):
            se = e.stencil_energy()
            led = e.bemf_ledger()
            tau = e.tau_zx_proxy()
            m = e.interior_mask()
            series["t"].append(e.time)
            series["EV"].append(se["E_V_lin"])
            series["Eom"].append(se["E_omega"])
            series["Hc"].append(se["H_couple"])
            series["Ew"].append(e.shear_energy())
            series["Lom"].append(e.spin_L_omega())
            series["Hbel"].append(e.helicity_bel())
            series["bemf_emf"].append(led["bemf_emf"])
            series["drive"].append(led["drive"])
            series["workV"].append(led["work_V"])
            series["workOm"].append(led["work_omega"])
            series["tauzx"].append(float(np.sqrt(np.sum((tau ** 2) * m))))
            series["maxom"].append(e.omega_intensity()["max_omega"])
    ratio = Lmax[CHK[2]] / (Lmax[CHK[0]] + 1e-12)
    led = e.bemf_ledger()
    out = {
        "bemf_kappa": bemf_kappa, "lock_eta": lock_eta, "with_photon": with_photon,
        "L_max": [Lmax[c] for c in CHK], "ratio_4L": float(ratio),
        "saturates": bool(ratio <= SAT_TOL),
        "maxom_end": e.omega_intensity()["max_omega"],
        "Hbel_end": e.helicity_bel(),
        "EV_0": se0["E_V_lin"], "EV_end": e.stencil_energy()["E_V_lin"],
        "Eom_0": se0["E_omega"], "Eom_end": e.stencil_energy()["E_omega"],
        "work_V": led["work_V"], "work_omega": led["work_omega"],
        "work_imbalance": led["work_imbalance"],
        "secs": round(time.time() - t_start, 1),
    }
    if record:
        out["series"] = series
    return out


def main():
    stage = sys.argv[1] if len(sys.argv) > 1 else "all"
    outdir = os.path.dirname(os.path.abspath(__file__))
    results = {"config": {"N": N_GRID, "kappa_L": KAPPA_L, "lock_eta_v4": LOCK_ETA_V4,
                          "sat_tol": SAT_TOL, "n_steps": N_STEPS, "checkpoints": CHK,
                          "v4_baseline_ratio": 5.035}}

    # ── PRIMARY panel: v4 lock ON (lock_eta=0.05), BEMF added on top ──
    if stage in ("all", "primary"):
        print("[PRIMARY] v4 config (lock_eta=0.05) + BEMF {OFF, +Lenz, -anti}", flush=True)
        prim = {}
        for name, kap in (("OFF", 0.0), ("BEMF_pos", +KAPPA_L), ("BEMF_neg", -KAPPA_L)):
            r = run_arm(bemf_kappa=kap, lock_eta=LOCK_ETA_V4)
            prim[name] = r
            print(f"   {name:10s} kap={kap:+.2f} L_max={[round(x,3) for x in r['L_max']]} "
                  f"ratio={r['ratio_4L']:.3f} sat={r['saturates']} maxom={r['maxom_end']:.4f} "
                  f"workV={r['work_V']:+.3e} workOm={r['work_omega']:+.3e} ({r['secs']}s)", flush=True)
        results["primary"] = prim
        with open(os.path.join(outdir, "bemf_feedback_results.json"), "w") as f:
            json.dump(results, f)

    # ── SECONDARY panel: lock OFF (lock_eta=0), BEMF ALONE (the honest replacement) ──
    if stage in ("all", "secondary"):
        # reload primary if present
        p = os.path.join(outdir, "bemf_feedback_results.json")
        if os.path.exists(p):
            results = json.load(open(p))
        print("[SECONDARY] lock OFF (no ad-hoc damper) + BEMF {OFF, +Lenz, -anti}", flush=True)
        sec = {}
        for name, kap in (("OFF", 0.0), ("BEMF_pos", +KAPPA_L), ("BEMF_neg", -KAPPA_L)):
            r = run_arm(bemf_kappa=kap, lock_eta=0.0)
            sec[name] = r
            print(f"   {name:10s} kap={kap:+.2f} L_max={[round(x,3) for x in r['L_max']]} "
                  f"ratio={r['ratio_4L']:.3f} sat={r['saturates']} maxom={r['maxom_end']:.4f} "
                  f"workV={r['work_V']:+.3e} workOm={r['work_omega']:+.3e} ({r['secs']}s)", flush=True)
        results["secondary"] = sec
        with open(os.path.join(outdir, "bemf_feedback_results.json"), "w") as f:
            json.dump(results, f)

    # ── GAIN SWEEP: gain-robustness of the verdict (no series, ratio only) ──
    if stage in ("all", "sweep"):
        p = os.path.join(outdir, "bemf_feedback_results.json")
        if os.path.exists(p):
            results = json.load(open(p))
        print("[SWEEP] gain-robustness on the v4-lock config; κ_L scan both signs", flush=True)
        sweep = {}
        for kap in (+0.3, +0.6, +1.2, +2.4, -0.3, -0.6, -1.2, -2.4):
            r = run_arm(bemf_kappa=kap, lock_eta=LOCK_ETA_V4, record=False)
            sweep[f"{kap:+.1f}"] = {"ratio_4L": r["ratio_4L"], "L_max": r["L_max"],
                                    "maxom_end": r["maxom_end"], "saturates": r["saturates"]}
            print(f"   κ_L={kap:+.1f} ratio={r['ratio_4L']:.3f} sat={r['saturates']} "
                  f"maxom={r['maxom_end']:.4f}", flush=True)
        results["sweep"] = sweep
        with open(os.path.join(outdir, "bemf_feedback_results.json"), "w") as f:
            json.dump(results, f)

    print(">> DONE stage=%s" % stage, flush=True)


if __name__ == "__main__":
    main()
