"""
Extractor-misread probe — WHY did the v3 planted (2,3) read back (2,1)?

Context (RECORD-HONESTY, graft-v3 panel 2026-06-09): the v3 independence smoke
plants a KNOWN (2,3) in ω (`seed_omega_known_2_3`, R=0.22N, r=R/φ²) and reads it
back as (2,1) — the poloidal "3" fibre collapses to 1 (`w_pol` 3→1). graft-v2's
carrier-gate planted the SAME (2,3) and read (2,3) at rel 0.80/0.59; the
perf-utils equivalence gate also read planted-(2,3) correctly. A future TRUE
(2,3) could therefore be misread as a FAILURE.

This probe is an INSTRUMENT characterization, NOT a fix. It plants a FRESH (2,3)
(no optimizer, no templated answer) at a SWEEP of configurations and tabulates
the RAW reads (w_tor, w_pol, rel, and the per-walk poloidal winding list) so the
parameter that flips the poloidal read is localized from the data itself.

Discipline: ave-driver-script-honesty (every row is a real read of the planted
field; the only "conclusion" printed is the data-derived list of which configs
read w_pol≠3) + ave-representation-capability-check (this is the instrument-side
instance: the extractor's CAPABILITY to represent a planted q=3 fibre across the
configuration space, separated from the physics).

Run:  python3 src/scripts/vol_1_foundations/extractor_misread_probe.py
Reads only; writes nothing. (The finding table is transcribed by hand into
research/2026-06-09_extractor-poloidal-misread_note.md.)
"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from crystal_graft_v3_run import (  # noqa: E402
    PHI2,
    N_GRID,
    _make_engine,
    extract_2_3_omega,
    find_shell,
)

from ave.core.crystal_graft_v3 import CrystalGraftV3  # noqa: E402


def _fresh_engine(N):
    """A clean V3 engine with the buckle OFF (pure instrument: no dynamics drives
    ω) — the same posture v2's carrier-gate used (buckle_on=False)."""
    return CrystalGraftV3(N=N, S_min=1e-3, omega_gap=1.0, buckle_on=False)


def plant_and_read(label, *, R_plant, r_plant, amp, read="planted", n_steps=0, N=N_GRID):
    """Plant a FRESH known (2,3) at (R_plant, r_plant, amp); optionally step
    n_steps with the live buckle; read back with the v3 extractor.

    read = "planted"   → extract at the planted (R_plant, r_plant)  [v3 path]
    read = "findshell" → extract at find_shell(omega)               [v2 path]
    """
    if n_steps > 0:
        # replicate the smoke's stepped path exactly: a CP8 precursor + live buckle
        e = _make_engine("abc", +1, seed_frac=0.9, N=N)
    else:
        e = _fresh_engine(N)
    e.seed_omega_known_2_3(R_plant, r_plant, amplitude=amp, p=2, q=3)
    for _ in range(n_steps):
        e.step()

    if read == "findshell":
        R_read, r_read = find_shell(e.omega, N)
    else:
        R_read, r_read = R_plant, r_plant

    res = extract_2_3_omega(e.omega, e.omega_velocity(), R_read, r_read, N)
    return {
        "label": label,
        "R_plant": R_plant,
        "r_plant": r_plant,
        "amp": amp,
        "n_steps": n_steps,
        "read_path": read,
        "R_read": R_read,
        "r_read": r_read,
        "w_tor": res["w_tor"],
        "w_pol": res["w_pol"],
        "w_tor_rel": res["w_tor_rel"],
        "w_pol_rel": res["w_pol_rel"],
        "pol_raw": res["w_pol_raw_list"],
        "is_2_3": res["is_2_3"],
    }


def build_sweep():
    N = N_GRID
    R0 = 0.22 * N          # the v2/v3 SHARED plant major radius (= 9.68 at N=44)
    r0 = R0 / PHI2         # the φ²-aspect minor radius (= 3.70)
    rows = []

    # --- baseline: the SAME plant geometry v2 and v3 both used -----------------
    # v2 carrier-gate read path (find_shell-remeasured contour), FRESH, no steps:
    rows.append(plant_and_read("v2_path_findshell", R_plant=R0, r_plant=r0, amp=0.3,
                               read="findshell"))
    # v3 independence read path (planted contour), FRESH, no steps:
    rows.append(plant_and_read("v3_path_planted_fresh", R_plant=R0, r_plant=r0, amp=0.3,
                               read="planted"))

    # --- ± amplitude (read at planted contour) --------------------------------
    rows.append(plant_and_read("amp_lo_0.15", R_plant=R0, r_plant=r0, amp=0.15))
    rows.append(plant_and_read("amp_hi_0.60", R_plant=R0, r_plant=r0, amp=0.60))

    # --- ± R/r aspect: hold R0, vary the minor radius the FIBRE lives on ------
    rows.append(plant_and_read("aspect_fat_Rr2.0", R_plant=R0, r_plant=R0 / 2.0, amp=0.3))
    rows.append(plant_and_read("aspect_phi2_Rr2.62", R_plant=R0, r_plant=r0, amp=0.3))
    rows.append(plant_and_read("aspect_thin_Rr3.5", R_plant=R0, r_plant=R0 / 3.5, amp=0.3))

    # --- ± contour radius / scale: vary the absolute torus size ---------------
    rows.append(plant_and_read("scale_mid_R6.6", R_plant=0.15 * N, r_plant=(0.15 * N) / PHI2, amp=0.3))
    rows.append(plant_and_read("scale_small_fullrun_R2.9",
                               R_plant=2.9154759474226504, r_plant=1.113612718532651, amp=0.3))

    # --- the actual smoke: v3 plant + 500 live steps (instrument-vs-dynamics) --
    rows.append(plant_and_read("v3_smoke_stepped500", R_plant=R0, r_plant=r0, amp=0.3,
                               read="planted", n_steps=500))
    return rows


def main():
    rows = build_sweep()

    hdr = ("| config | R_plant | r_plant | R/r | amp | steps | read@ | "
           "(w_tor,w_pol) | rel(t,p) | pol_raw | is(2,3) |")
    sep = "|" + "|".join(["---"] * 10) + "|"
    print("\n" + hdr)
    print(sep)
    for x in rows:
        rr = x["R_plant"] / x["r_plant"] if x["r_plant"] else float("nan")
        print(
            f"| {x['label']} | {x['R_plant']:.2f} | {x['r_plant']:.2f} | {rr:.2f} | "
            f"{x['amp']:.2f} | {x['n_steps']} | {x['read_path']}({x['R_read']:.2f},{x['r_read']:.2f}) | "
            f"({x['w_tor']},{x['w_pol']}) | ({x['w_tor_rel']:.2f},{x['w_pol_rel']:.2f}) | "
            f"{x['pol_raw']} | {x['is_2_3']} |"
        )

    # data-derived summary ONLY (no hand-set conclusion): which configs miss q=3
    miss = [x["label"] for x in rows if x["w_pol"] != 3]
    hit = [x["label"] for x in rows if x["w_pol"] == 3]
    print(f"\n  reads w_pol==3 (correct): {hit}")
    print(f"  reads w_pol!=3 (misread): {miss}")
    print(f"  fresh-vs-stepped @ planted-contour: "
          f"fresh={[ (x['w_tor'],x['w_pol']) for x in rows if x['label']=='v3_path_planted_fresh']}, "
          f"stepped={[ (x['w_tor'],x['w_pol']) for x in rows if x['label']=='v3_smoke_stepped500']}")
    return rows


if __name__ == "__main__":
    main()
