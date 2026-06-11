"""genesis-v8 PHASE-2 — THE TOPOLOGY GATE SMOKE (D16)
====================================================================================

Does threading OPEN a channel through the v6 MAIN bubble's snap shell? Builds the
v6 MAIN bubble (the T1-converging recipe, genesis_v6_transducer_run.build_engine)
and measures the snap shell's GENUS from snap_mask connectivity
(ave.utils.topology_genus.measure_topology — REAL topology code, not an assertion).

THE GATE (prereg frozen @ 2d43a1bf, §3.3 / §4 F-GENUS), three ORDERED bins:
  SHELL-NEVER-FORMS  no coherent connected snap shell (largest component < F-SHELL,
                     or fragmented below the dominance floor) — nothing to thread.
  NO-PENETRATION     a coherent shell forms (genus-0) but no un-snapped channel
                     threads it along the spin axis (the Meissner expulsion did NOT
                     carve a normal channel) — HONEST only after the drive-M /
                     shell-thickness sweep (the directive: sweep before concluding).
  THREADED           a connected un-snapped channel threads the shell (ball->torus).

GATE-AS-EXECUTABLE-ASSERTION (the v7 demotion-h fix): every bin is COMPUTED here
from the field, never a docstring. §210: the mandated drive-M and shell-thickness
(meissner) sweeps are executed (the NO-PENETRATION bin is honest only after them).
F-T1: every arm reports whether the bulk stayed FINITE + E_V converged (a topology
read on a detonating object is VOID; T1-BROKEN is a bin, not a tweak target).

The Run phase (the full T1-T6 + polyphase winding matrix) is GATED on THREADED.

Run: PYTHONPATH=src .venv/bin/python \
        src/scripts/vol_1_foundations/genesis_v8_threaded_smoke.py
"""

from __future__ import annotations

import json
import os
import sys
import time
import warnings

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from ave.core.unified_genesis_engine import UnifiedGenesisEngine, RHO_CAV  # noqa: E402
from ave.utils.topology_genus import measure_topology  # noqa: E402

warnings.filterwarnings("ignore", category=RuntimeWarning)  # detonation overflow is DETECTED + binned

SEED = 20260610
F_SHELL = 200          # the F-SHELL coherent-shell floor (prereg §4)
F_EV = 13.0            # the T1 converged-mass class (v6 baseline 11.70->12.91)


def build_v6_main(*, N=48, M=1.8, meissner=0.05, nu_art=5e-4, helicity=1):
    """The v6 MAIN bubble — the T1-converging recipe (byte-equivalent to
    genesis_v6_transducer_run.build_engine MAIN). The v8 knobs default to the v6
    path; the topology gate needs only the snap shell, not the polyphase deposit."""
    np.random.seed(SEED)
    e = UnifiedGenesisEngine(
        N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
        nu_art_bulk=nu_art, rho_diff=5e-4, snap_payback_rate=1.0, delta_heal=0.0,
        rho_cav=RHO_CAV, chi_shock=1.0, vent_mode="absorbed",
        snap_accounting="conservative", meissner_harden=meissner,
        omega_sector_on=True, buckle_on=True, photon_coupling=True,
        lock_on=True, lock_eta=0.08, wall_width=0.12,
        transducer_on=True, chi_exch=0.02, omega_recipient_frac=0.5)
    e.seed_lane1(frac=0.85, sigma=4.0, vent_into_seed=False)
    e.energize_rotation_column(M_edge=M, R_core=0.18 * N * e.dx, axis=2)
    e.freeze_wall_window()
    e.drive_chiral_photon(helicity=helicity, sigma=5.0, wavelength=8.0,
                          amplitude=0.10, axis=2)
    return e


def assert_t1_regression(e):
    """F-T1 (every arm): the bulk field FINITE + E_V in the converged class. A
    topology read on a non-finite (detonating) object is VOID -> T1-BROKEN."""
    finite = bool(np.all(np.isfinite(e.rho_bar)) and np.all(np.isfinite(e.omega))
                  and np.all(np.isfinite(e.u_adv)))
    ev = float(e.bulk_energy_conserved(True)) if finite else float("nan")
    t1_ok = bool(finite and ev < F_EV * 3.0)
    return {"finite": finite, "E_V_cons": ev if finite else None, "t1_ok": t1_ok}


def run_topology_arm(*, N, M, meissner, nu_art, n_build, rec_every=400):
    """Build the v6 MAIN bubble; step with a FINITENESS GUARD (break + record on
    detonation); measure the topology bin from snap_mask connectivity. Returns the
    arm record (bin, fragmentation diagnostics, T1, snap onset)."""
    t0 = time.time()
    e = build_v6_main(N=N, M=M, meissner=meissner, nu_art=nu_art)
    interior = e.interior_mask()
    onset, broke = None, None
    pocket_max = 0
    rho_min = 0.0
    series = []
    for s in range(1, n_build + 1):
        e.step()
        pocket_max = max(pocket_max, e.pocket_cells())
        if e.pocket_cells() > 0 and onset is None:
            onset = int(e.step_count)
        if not np.all(np.isfinite(e.rho_bar)):
            broke = int(e.step_count)
            break
        rho_min = min(rho_min, float(e.rho_bar[interior].min()))
        if s % rec_every == 0:
            topo_s = measure_topology(e.snap_mask, interior, axis=2, f_shell=F_SHELL)
            series.append({"step": int(e.step_count), "pocket": int(e.pocket_cells()),
                           "bin": topo_s["bin"], "shell_cells": topo_s.get("shell_cells"),
                           "largest_frac": topo_s.get("largest_frac_of_snap"),
                           "n_components": topo_s.get("n_snap_components")})
    t1 = assert_t1_regression(e)
    if t1["finite"]:
        topo = measure_topology(e.snap_mask, interior, axis=2, f_shell=F_SHELL)
        gate_bin = topo["bin"]
    else:
        topo = {"bin": "NONFINITE", "reason": f"bulk detonated at step {broke}"}
        gate_bin = "T1-BROKEN"  # a topology read on a detonating object is VOID
    rec = {
        "N": N, "M": M, "meissner": meissner, "nu_art": nu_art,
        "n_build": n_build, "snap_onset": onset, "broke_at": broke,
        "pocket_built": int(e.pocket_cells()) if t1["finite"] else None,
        "pocket_max": int(pocket_max), "rho_min": rho_min, "rho_cav": float(RHO_CAV),
        "t1": t1, "topology": {k: v for k, v in topo.items() if k != "_channel_mask"},
        "gate_bin": gate_bin, "series": series, "wall_s": round(time.time() - t0, 1),
    }
    print(f"  M={M:4.1f} ms={meissner:.2f} nu={nu_art:.0e} N={N}: "
          f"pocket_max={pocket_max:5d} onset={onset} finite={t1['finite']} "
          f"shell={topo.get('shell_cells')} bin={gate_bin} ({rec['wall_s']:.0f}s)", flush=True)
    return rec


def overall_bin(arms):
    """The ordered floor gate over all arms: THREADED if ANY arm threaded; else
    NO-PENETRATION if any arm formed a COHERENT shell but did not thread; else
    SHELL-NEVER-FORMS (no coherent shell on any finite arm). T1-BROKEN arms are
    recorded but do NOT supply a topology verdict (the read is VOID)."""
    bins = [a["gate_bin"] for a in arms]
    if "THREADED" in bins:
        return "THREADED"
    if "NO-PENETRATION" in bins:
        return "NO-PENETRATION"
    # any FINITE arm that formed a coherent shell would have binned NO-PENETRATION
    # or THREADED; reaching here means no finite arm produced a coherent shell.
    finite_arms = [a for a in arms if a["t1"]["finite"]]
    if finite_arms:
        return "SHELL-NEVER-FORMS"
    return "T1-BROKEN"  # no arm even stayed finite


def main():
    t_start = time.time()
    N = 48
    n_build = 2400
    print(f"[genesis-v8 TOPOLOGY SMOKE] N={N} n_build={n_build}; the mandated "
          f"drive-M x shell-thickness sweep (sweep before concluding).", flush=True)

    # the prereg drive-M grid x the shell-thickness (meissner) grid (§5 rows 3,4)
    M_grid = [1.8, 2.5, 3.0, 3.5]
    meissner_grid = [0.0, 0.05, 0.10]
    arms = []
    print("[1/2] drive-M x shell-thickness sweep ...", flush=True)
    for ms in meissner_grid:
        for M in M_grid:
            arms.append(run_topology_arm(N=N, M=M, meissner=ms, nu_art=5e-4,
                                         n_build=n_build))

    # the §3.5(3) stabilization probe: can higher viscosity hold the M>=3.5 snap
    # FINITE long enough to form a coherent shell? (fight the CFL detonation)
    print("[2/2] viscosity-stabilized high-drive probe (M=3.5) ...", flush=True)
    for nu in [2e-3, 5e-3, 2e-2]:
        arms.append(run_topology_arm(N=N, M=3.5, meissner=0.05, nu_art=nu,
                                     n_build=n_build))

    verdict = overall_bin(arms)
    # the coherent-shell evidence: the largest connected snap component vs total,
    # across the finite arms that DID snap (the fragmentation diagnostic)
    snapped_finite = [a for a in arms if a["t1"]["finite"] and (a["pocket_built"] or 0) > 0]
    coherence = [{"M": a["M"], "ms": a["meissner"], "nu": a["nu_art"],
                  "snap_total": a["topology"].get("total_snap"),
                  "largest_component": a["topology"].get("shell_cells"),
                  "largest_frac": a["topology"].get("largest_frac_of_snap"),
                  "n_components": a["topology"].get("n_snap_components")}
                 for a in snapped_finite]

    out = {
        "title": "genesis-v8 TOPOLOGY GATE SMOKE (D16)",
        "prereg": "research/2026-06-11_genesis-v8-threaded_prereg.md @ 2d43a1bf",
        "config": {"N": N, "n_build": n_build, "F_SHELL": F_SHELL, "F_EV": F_EV,
                   "M_grid": M_grid, "meissner_grid": meissner_grid,
                   "nu_stabilize": [2e-3, 5e-3, 2e-2]},
        "arms": arms,
        "shell_coherence_finite_snapped": coherence,
        "VERDICT": verdict,
        "run_gated_on_THREADED": bool(verdict == "THREADED"),
        "wall_s_total": round(time.time() - t_start, 1),
    }
    here = os.path.dirname(__file__)
    dst = os.path.abspath(os.path.join(here, "..", "..", "..", "research",
                          "2026-06-11_genesis-v8-threaded_smoke.json"))
    with open(dst, "w") as f:
        json.dump(out, f, indent=2)
    print("\n================ TOPOLOGY GATE VERDICT ================")
    print(f"  VERDICT: {verdict}")
    print(f"  Run phase gated on THREADED -> {'PROCEEDS' if verdict=='THREADED' else 'DOES NOT PROCEED'}")
    print(f"  coherent-shell evidence (finite snapped arms): {coherence}")
    print(f"  dump: {dst}")
    print(f"  total wall {out['wall_s_total']:.0f}s")
    return out


if __name__ == "__main__":
    main()
