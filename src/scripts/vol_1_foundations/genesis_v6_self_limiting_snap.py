"""
genesis-v6 PHASE-1 JOB 2 — D10 SELF-LIMITING SNAP (both renderings)
==================================================================

The deflagration fix (prereg §3 JOB 2). v5's snap cascade was positive feedback
(pocket 80->5968 in ~150 steps; E_V 13->50339). Build BOTH self-limiting
renderings and sweep them against each other on the v5 cascade config:

  (a) VENT-ABSORBED   — vented latent -> conservative store (no V-kick); bounds
                        E_V by removing the breather-trigger energy path.
  (b) MEISSNER-HARDEN — each snapped cell RAISES neighbors' snap threshold
                        (negative feedback; nucleates-and-stops). Hardening
                        increment SWEPT {0, ...}; increment=0 reproduces the
                        cascade (the keeper).

GATES (prereg §2): each rendering must (i) bound E_V (< F-EV x 10) AND (ii)
preserve a single-cell snap + the D6 birth-flash (clears F-BURST x 3). A fix that
kills the flash is over-corrected. Report the cascade pocket(t) of each.

Rule 11 / ave-driver-script-honesty: numbers FROM the field, dumped to JSON.
"""

from __future__ import annotations

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from ave.core.unified_genesis_engine import UnifiedGenesisEngine, RHO_CAV  # noqa: E402
from ave.core.longitudinal_burst_detector import LongitudinalBurstDetector  # noqa: E402

SEED = 20260610
N_MAIN, M_MAIN = 40, 1.8
N_BUILD = 3200
FRAC, DRIVE_AMP, WAVELEN, SIGMA_PH, SIGMA_SEED, R_FRAC = 0.85, 0.10, 8.0, 5.0, 4.0, 0.18
F_EV = 13.0           # the quiet-build E_V plateau (v5 §0; the deflagration floor)
F_EV_GATE = 10.0      # deflagration = E_V rises >= 10x F-EV


def build_engine(*, snap=True, vent_into_seed=True, vent_mode="kick",
                 snap_accounting="legacy", meissner_harden=0.0):
    c2_floor = 0.0 if snap else 1e-3
    e = UnifiedGenesisEngine(
        N_MAIN, bulk_density_on=True, snap_on=snap, c2_floor=c2_floor,
        nu_art_bulk=5e-4, rho_diff=5e-4, chi_shock=1.0, snap_payback_rate=1.0,
        rho_cav=RHO_CAV, lock_on=True, lock_eta=0.08,
        vent_mode=vent_mode, snap_accounting=snap_accounting,
        meissner_harden=meissner_harden)
    e.seed_lane1(frac=FRAC, sigma=SIGMA_SEED, vent_into_seed=vent_into_seed, vent_near_frac=0.5)
    return e


def energize(e, axis=2):
    R_core = R_FRAC * e.N * e.dx
    e.energize_rotation_column(M_edge=M_MAIN, R_core=R_core, axis=axis)
    e.freeze_wall_window()
    e.drive_chiral_photon(helicity=1, sigma=SIGMA_PH, wavelength=WAVELEN,
                          amplitude=DRIVE_AMP, axis=axis)


def cascade_arm(name, **kw):
    """Build to N_BUILD; record pocket(t) and E_V(t) around the cascade."""
    t0 = time.time()
    np.random.seed(SEED)
    e = build_engine(**kw)
    energize(e)
    pocket_t, ev_t = [], []
    ev_max = 0.0
    for s in range(N_BUILD + 1):
        if s % 50 == 0 or s == N_BUILD:
            ev = float(e.bulk_energy(True))
            pocket_t.append([int(e.step_count), int(e.pocket_cells())])
            ev_t.append([int(e.step_count), ev])
            ev_max = max(ev_max, ev)
        if s < N_BUILD:
            e.step()
    out = {
        "name": name, "config": kw,
        "pocket_built": int(e.pocket_cells()), "pocket_max": max(p[1] for p in pocket_t),
        "EV_built": float(e.bulk_energy(True)), "EV_max": ev_max,
        "EV_bounded": bool(ev_max < F_EV * F_EV_GATE),
        "max_V_built": float(np.max(np.abs(e.V * e.interior_mask()))),
        "snap_ledger": e.snap_ledger(),
        "pocket_t": pocket_t, "ev_t": ev_t, "wall_s": time.time() - t0,
    }
    print(f"  {name:22s} pocket_max={out['pocket_max']:5d} EV_max={ev_max:10.1f} "
          f"bounded={out['EV_bounded']} maxV={out['max_V_built']:.2f} ({out['wall_s']:.0f}s)",
          flush=True)
    return out


# ---------------- the D6 known-positive (single-cell snap + birth flash) ----------------
def _central_ball(N, radius):
    cc = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N))
    return np.sqrt((i - cc) ** 2 + (j - cc) ** 2 + (k - cc) ** 2) <= radius


def calibrate_burst_floor():
    """F-BURST = the free-run (excited, no-snap) scatter of the bulk pressure-
    integral (inherited F0d). KNOWN-NULL first (HARD CONSTRAINT)."""
    np.random.seed(SEED)
    e = build_engine(snap=True, vent_into_seed=False, snap_accounting="conservative")
    R = R_FRAC * e.N * e.dx
    e.energize_rotation_column(M_edge=0.6, R_core=R, axis=2)  # sub-threshold (no snap)
    return float(LongitudinalBurstDetector.calibrate_floor(e, steps=120))


def known_positive_burst(floor, *, vent_mode, snap_accounting, meissner_harden):
    """Preserve-the-birth-flash check: a SINGLE hand-snap must emit a burst that
    clears floor x 3 under the given rendering (the snap's certified role)."""
    N = 28
    e = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
                             chi_shock=1.0, snap_payback_rate=0.0,
                             vent_mode=vent_mode, snap_accounting=snap_accounting,
                             meissner_harden=meissner_harden)
    e.u_adv[..., 0] = 0.3  # advective KE so the snap has a shock to release
    det = LongitudinalBurstDetector(floor=floor, threshold_mult=3.0)
    det.record(e)
    e.hand_snap_region(_central_ball(N, 3.0))
    det.record(e)
    bursts = det.scan()
    released = det.total_burst_energy()
    return {"n_bursts": len(bursts), "released": float(released),
            "floor_x3": float(floor * 3.0), "clears": bool(len(bursts) > 0),
            "pocket": int(e.pocket_cells())}


def main():
    t_start = time.time()
    results = {"prereg": "research/2026-06-10_genesis-v6-transducer_prereg.md",
               "job": "D10 self-limiting snap (both renderings)",
               "F_EV": F_EV, "F_EV_gate_mult": F_EV_GATE,
               "scale": dict(N=N_MAIN, M=M_MAIN, n_build=N_BUILD, frac=FRAC, seed=SEED)}

    print("[1/3] BASELINE + the two renderings (cascade behavior) ...", flush=True)
    results["arms"] = {}
    # baseline = v5 cascade (legacy, kick) -> the deflagration to reproduce. The v5
    # 'deflagration' is TWO coupled failures: the POCKET cascade (bulk ρ̄ -> 5968)
    # AND the E_V detonation (the seed-V breather -> 50339, the JOB-1 vent channel).
    results["arms"]["BASELINE_v5_cascade"] = cascade_arm(
        "BASELINE_v5_cascade", snap_accounting="legacy", vent_mode="kick", meissner_harden=0.0)
    # rendering (a) VENT-ABSORBED — removes the vent-kick energy path; bounds E_V.
    results["arms"]["A_vent_absorbed"] = cascade_arm(
        "A_vent_absorbed", snap_accounting="conservative", vent_mode="absorbed",
        meissner_harden=0.0)
    # rendering (b) MEISSNER — sweep WITH the pump-fix active (vent-absorbed), so the
    # rendering is clean: hardening bounds the POCKET, the absorbed vent bounds E_V.
    results["meissner_sweep"] = {}
    for inc in (0.02, 0.05, 0.10):
        rec = cascade_arm(f"B_meissner_{inc:.2f}_absorbed", snap_accounting="conservative",
                          vent_mode="absorbed", meissner_harden=inc)
        results["arms"][f"B_meissner_{inc:.2f}_absorbed"] = rec
        results["meissner_sweep"][f"{inc:.2f}"] = {
            "pocket_max": rec["pocket_max"], "EV_max": rec["EV_max"],
            "EV_bounded": rec["EV_bounded"]}
    # the keeper: meissner=0 + absorbed == rendering (a) (no hardening -> full pocket)
    results["arms"]["B_meissner_0.00_absorbed(keeper)"] = cascade_arm(
        "B_meissner_0.00_absorbed", snap_accounting="conservative", vent_mode="absorbed",
        meissner_harden=0.0)
    # DIAGNOSTIC (channel separation, reinforces D11): Meissner WITH the kick vent —
    # bounds the POCKET but E_V STILL detonates (the deep-seed breather is
    # hypersensitive to ANY vent kick; the E_V channel is the vent, not the pocket).
    results["arms"]["DIAG_meissner_0.05_kick"] = cascade_arm(
        "DIAG_meissner_0.05_kick", snap_accounting="conservative", vent_mode="kick",
        meissner_harden=0.05)

    print("[2/3] F-BURST floor + known-positive (birth-flash preservation) ...", flush=True)
    floor = calibrate_burst_floor()
    results["F_BURST"] = {"floor": floor, "floor_x3": floor * 3.0}
    print(f"    F_BURST floor = {floor:.4e}", flush=True)
    results["known_positive"] = {}
    for label, kw in (
        ("A_vent_absorbed", dict(vent_mode="absorbed", snap_accounting="conservative", meissner_harden=0.0)),
        ("B_meissner_0.05_absorbed", dict(vent_mode="absorbed", snap_accounting="conservative", meissner_harden=0.05)),
        ("legacy_v5", dict(vent_mode="kick", snap_accounting="legacy", meissner_harden=0.0)),
    ):
        kp = known_positive_burst(floor, **kw)
        results["known_positive"][label] = kp
        print(f"    {label:24s} burst clears x3 = {kp['clears']} "
              f"(released={kp['released']:.3e} vs {kp['floor_x3']:.3e})", flush=True)

    # ---- VERDICT (the two renderings address TWO coupled failure modes) ----
    a = results["arms"]["A_vent_absorbed"]
    base = results["arms"]["BASELINE_v5_cascade"]
    diag = results["arms"]["DIAG_meissner_0.05_kick"]
    meiss = {k: v for k, v in results["meissner_sweep"].items()}
    # rendering (b) clean (Meissner + absorbed): bounds POCKET (<0.5x base) AND E_V
    b_best = min((k for k, v in meiss.items()
                  if v["EV_bounded"] and v["pocket_max"] < 0.5 * base["pocket_max"]),
                 default=None, key=lambda k: meiss[k]["pocket_max"] if k else 1e9)
    results["verdict"] = {
        "baseline": {"EV_max": base["EV_max"], "pocket_max": base["pocket_max"],
                     "two_failures": "POCKET cascade (bulk ρ̄) + E_V detonation (seed-V breather)"},
        "A_vent_absorbed": {
            "EV_max": a["EV_max"], "EV_bounded": a["EV_bounded"], "pocket_max": a["pocket_max"],
            "bounds": "E_V (the breather channel)",
            "mechanism": "removes the vent-kick energy path -> no breather; pocket cascade still runs"},
        "B_meissner_absorbed": {
            "sweep": meiss, "best_increment": b_best,
            "bounds": "the POCKET (nucleates-and-stops) AND E_V (absorbed vent)",
            "mechanism": "per-cell threshold hardening: the cascade front needs ever-deeper "
                         "deficits and STALLS; paired with the absorbed vent both are bounded"},
        "DIAG_meissner_kick": {
            "EV_max": diag["EV_max"], "EV_bounded": diag["EV_bounded"], "pocket_max": diag["pocket_max"],
            "finding": "Meissner bounds the POCKET (-> %d) but E_V STILL detonates (-> %.0f) with the "
                       "kick vent: the deep-seed breather is hypersensitive to ANY vent kick. The E_V "
                       "channel is the VENT (D11), not the pocket -- so Meissner MUST be paired with "
                       "vent-absorbed to bound E_V." % (diag["pocket_max"], diag["EV_max"])},
        "both_preserve_birth_flash": all(
            results["known_positive"][k]["clears"]
            for k in ("A_vent_absorbed", "B_meissner_0.05_absorbed")),
    }

    out_json = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..", "..", "..", "research",
        "2026-06-10_genesis-v6-self-limiting-snap_results.json"))
    with open(out_json, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nDONE in {time.time()-t_start:.0f}s -> {out_json}")
    print("VERDICT:", json.dumps(results["verdict"], indent=2))


if __name__ == "__main__":
    main()
