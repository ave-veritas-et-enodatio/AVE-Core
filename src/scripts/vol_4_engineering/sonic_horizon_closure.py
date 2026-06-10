"""
Sonic-horizon closure — FLASH / LOCK / CLIP / NO-HORIZON + handedness SELECTIVE / BLIND
========================================================================================

Driver for `research/2026-06-10_sonic-horizon-closure_prereg.md`.
Engine: `ave.core.sonic_horizon_flow.SonicHorizonFlow2D` (the sharp-interface closure);
control: `ave.core.cavitation_flow.CavitationFlow2D` (the predecessor's floored scheme).

HONEST SCOPE (ave-driver-script-honesty): forward-integrates the closure and CLASSIFIES
against the FROZEN prereg bins. Does NOT fit to any target. `ρ̄_cav=−1/φ` is a CANDIDATE-
CLAIM used only as the EOS-fixed interface threshold. The verdict is the engine's dynamical
behaviour. APPARATUS GATE (Stage B) runs BEFORE the physics runs (Stages C/D);
ave-apparatus-floor-attribution governs — a signature that tracks a knob is CLIP.

Stages:
  A. CALIBRATION / INSTRUMENT FLOOR: U-table energy conservation; reflectivity on a KNOWN
     pressure-release mirror (R≈1) and on a TRANSPARENT region (R≈floor).
  B. APPARATUS GATE: sweep the new BC knobs 4x each at the SUB-CROSSING drive M=0.6 (nothing
     should cavitate -> any pocket/E_diss is the knob's false-positive floor); + known-positive.
  C. HYSTERESIS ARM: up-sweep M 0.6->1.0 (fresh runs); pocket persistence after FULL de-spin
     at each peak M; chi_shock sweep on persistence (the crux CLIP test); down-sweep loop.
  D. HANDEDNESS ARM: probe a formed pocket with co (m=+1) vs counter (m=-1) bulk OAM pulses
     at matched energy; R_co vs R_counter via difference-field reflectometry.
  E. CONTROL: the floored-c² predecessor scheme at the same drives -> closure effects ABSENT.
"""

from __future__ import annotations

import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))

from ave.core.cavitation_flow import RHO_CAV, CavitationFlow2D  # noqa: E402
from ave.core.sonic_horizon_flow import SonicHorizonFlow2D  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "_output")
os.makedirs(OUT, exist_ok=True)
R_CORE = 0.18


def run_to_peak(e, nsteps, despin_step=None, despin_factor=0.0, record_every=0, series=None):
    """Integrate; optionally fully de-spin at despin_step. Track deepest core + max pocket."""
    deepest = 0.0
    max_pocket = 0
    for s in range(nsteps):
        if despin_step is not None and s == despin_step:
            e.despin(despin_factor)
        e.step()
        rc = e.rho_core()[0]
        deepest = min(deepest, rc)
        max_pocket = max(max_pocket, e.pocket_cells())
        if series is not None and record_every and (s % record_every == 0):
            led = e.ledger()
            series["t"].append(e.t)
            series["rho_core"].append(rc)
            series["pocket"].append(led["pocket_cells"])
            series["KE"].append(led["KE"])
            series["PE_exact"].append(led["PE_exact"])
            series["E_diss"].append(led["E_diss"])
            series["L"].append(e.angular_momentum())
        if not e.is_stable():
            break
    return deepest, max_pocket


def reflectance(make_pocket, m, r_meas=0.30, r_launch=0.34, amp=1e-3, width=0.03,
                nprobe=650, N=160):
    """Flux-through-circle reflectance of a bulk azimuthal-`m` OAM pulse off the pocket
    produced by `make_pocket(e)`. Incident (inward) and reflected (outward) energy flux are
    BOTH evaluated on the SAME circle `r_meas` (cylindrical-geometry-neutral). Difference-
    field method (probe-run minus baseline-run) isolates the probe from the pocket's own
    (possibly rotating) background flow. R = e_refl/e_inc via the cumulative-flux turning
    point: e_inc = −min(∫flux dt), e_refl = (∫flux dt)|_end − min(∫flux dt)."""
    e0 = SonicHorizonFlow2D(N=N, nu_art=5e-4, rho_diff=5e-4)
    make_pocket(e0)
    r = e0.R + 1e-12
    dr = 1.5 * e0.dx
    ring = (np.abs(r - r_meas) < dr) & e0.interior
    nx = (e0.X / r)[ring]
    ny = (e0.Y / r)[ring]

    def radial_flux(e):  # net acoustic intensity p*u_r summed over the ring
        ur = e.u[ring] * nx + e.v[ring] * ny
        return float(np.sum(e.c0**2 * e.rho[ring] * ur))

    st = (e0.rho.copy(), e0.u.copy(), e0.v.copy(), e0.cav_mask.copy(), e0.static_mirror.copy())
    eb = SonicHorizonFlow2D(N=N, nu_art=5e-4, rho_diff=5e-4)
    eb.rho, eb.u, eb.v, eb.cav_mask, eb.static_mirror = (a.copy() for a in st)
    base = [radial_flux(eb)]
    for _ in range(nprobe):
        eb.step()
        base.append(radial_flux(eb))
    ep = SonicHorizonFlow2D(N=N, nu_art=5e-4, rho_diff=5e-4)
    ep.rho, ep.u, ep.v, ep.cav_mask, ep.static_mirror = (a.copy() for a in st)
    ep.add_oam_pulse(m=m, r0=r_launch, amp=amp, width=width, inward=True)
    prb = [radial_flux(ep)]
    for _ in range(nprobe):
        ep.step()
        prb.append(radial_flux(ep))
    flux = np.array(prb) - np.array(base)
    cum = np.cumsum(flux) * ep.dt
    # first inward+reflection cycle: e_inc = depth of the inward accumulation,
    # e_refl = outward recovery AFTER that turning point (windowed before the runs
    # decorrelate near the sharp boundary at late time).
    imin = int(np.argmin(cum))
    cmin = float(cum[imin])
    e_inc = -cmin
    e_refl = float(np.max(cum[imin:])) - cmin
    R = e_refl / e_inc if e_inc > 1e-30 else 0.0
    return {"R": float(R), "e_inc": e_inc, "e_refl": e_refl, "imin": imin}


# ---------------------------------------------------------------- Stage A
def stage_A_calibration():
    print("\n=== STAGE A: CALIBRATION / INSTRUMENT FLOOR ===")
    out = {}
    # (A1) exact-EOS energy conservation in a free inviscid acoustic run
    e = SonicHorizonFlow2D(N=128, nu_art=0.0, rho_diff=0.0)
    e.rho = 0.02 * np.exp(-(e.R**2) / (2 * 0.08**2))
    E0 = e.total_energy_exact()
    for _ in range(600):
        e.step()
    E1 = e.total_energy_exact()
    out["free_energy_drift_pct"] = 100 * (E1 - E0) / E0
    out["cav_events_free"] = e.cav_events
    print(f"  (A1) free acoustic KE+PE_exact drift = {out['free_energy_drift_pct']:.3f}%  "
          f"(cav_events={e.cav_events}; U-table validation)")

    # (A2) reflectivity calibration: known mirror (R~1) and transparent (R~floor)
    def mk_mirror(e):
        e.set_static_mirror(radius=0.20)

    def mk_transparent(e):
        pass  # ambient, no pocket

    R_mirror = reflectance(mk_mirror, m=1)["R"]
    R_floor = reflectance(mk_transparent, m=1)["R"]
    # handedness instrument floor: m-asymmetry on a NON-rotating mirror (should be ~0 by symmetry)
    Rm_co = reflectance(mk_mirror, m=1)["R"]
    Rm_ct = reflectance(mk_mirror, m=-1)["R"]
    hand_floor = abs(Rm_co - Rm_ct)
    out["R_known_mirror"] = R_mirror
    out["R_transparent_floor"] = R_floor
    out["handedness_floor_static"] = hand_floor
    out["static_mirror_R_co"] = Rm_co
    out["static_mirror_R_counter"] = Rm_ct
    print(f"  (A2) known pressure-release mirror R = {R_mirror:.3f}  (reference, expect <=1)")
    print(f"       transparent (no pocket)      R = {R_floor:.3f}  (focal-passage baseline)")
    print(f"       static-mirror m-asymmetry |R(+1)-R(-1)| = {hand_floor:.4f}  "
          f"(handedness instrument FLOOR; R+1={Rm_co:.3f} R-1={Rm_ct:.3f})")
    return out


# ---------------------------------------------------------------- Stage B
def stage_B_apparatus_gate():
    print("\n=== STAGE B: APPARATUS GATE (sweep new BC knobs @ M=0.6 sub-crossing) ===")
    out = {"sub_crossing": {}, "known_positive": {}}
    M = 0.6  # sub-crossing: deepest ~ -0.41 (predecessor), NO cavitation should occur
    sweeps = {
        "iface_thresh": [RHO_CAV - 0.05, RHO_CAV, RHO_CAV + 0.05, RHO_CAV + 0.10],
        "heal_width": [0.0, 0.01, 0.02, 0.05],
        "chi_shock": [0.0, 0.25, 0.5, 1.0],
        "nu_art": [1e-4, 5e-4, 2e-3, 5e-3],
        "N": [128, 160, 192, 224],
    }
    for knob, vals in sweeps.items():
        rows = []
        for val in vals:
            kw = dict(nu_art=5e-4, rho_diff=5e-4)
            Nuse = 160
            if knob == "N":
                Nuse = val
            else:
                kw[knob] = val
            e = SonicHorizonFlow2D(N=Nuse, **kw)
            e.energize_solid_body(M_edge=M, R_core=R_CORE)
            L0 = e.angular_momentum()
            deepest, max_pocket = run_to_peak(e, 2000)
            led = e.ledger()
            rows.append({"val": val, "deepest": deepest, "max_pocket": max_pocket,
                         "final_pocket": led["pocket_cells"], "E_diss": led["E_diss"],
                         "cav_events": led["cav_events"], "mass_clamp": led["mass_clamp"],
                         "L_drift_pct": 100 * (e.angular_momentum() - L0) / abs(L0)})
        out["sub_crossing"][knob] = rows
        pk = [r["max_pocket"] for r in rows]
        ed = [f"{r['E_diss']:.1e}" for r in rows]
        print(f"  {knob:13s} {vals}\n      -> max_pocket {pk}  E_diss {ed}")

    # known-positive: a hand-opened static mirror must persist + reflect per the BC
    e = SonicHorizonFlow2D(N=160, nu_art=5e-4, rho_diff=5e-4)
    e.set_static_mirror(radius=0.18)
    p0 = e.pocket_cells()
    for _ in range(800):
        e.step()
    out["known_positive"] = {"pocket_initial": p0, "pocket_after_800": e.pocket_cells(),
                             "held": e.pocket_cells() >= p0}
    print(f"  known-positive (static mirror): pocket {p0} -> {e.pocket_cells()} after 800 steps "
          f"(held={out['known_positive']['held']})")
    return out


def run_persistence(M, chi_shock=1.0, despin_at=1200, total=3200, N=160, c2_floor=0.0,
                    record=False):
    """Energize M; run to peak; FULLY de-spin at despin_at; relax. Report persistence."""
    e = SonicHorizonFlow2D(N=N, nu_art=5e-4, rho_diff=5e-4, chi_shock=chi_shock, c2_floor=c2_floor)
    e.energize_solid_body(M_edge=M, R_core=R_CORE)
    L0 = e.angular_momentum()
    series = {k: [] for k in ["t", "rho_core", "pocket", "KE", "PE_exact", "E_diss", "L"]} if record else None
    deepest, max_pocket = run_to_peak(e, total, despin_step=despin_at, despin_factor=0.0,
                                      record_every=(20 if record else 0), series=series)
    led = e.ledger()
    res = {"M": M, "chi_shock": chi_shock, "c2_floor": c2_floor, "deepest": deepest,
           "max_pocket": max_pocket, "final_pocket": led["pocket_cells"],
           "final_rho_core": e.rho_core()[0], "E_diss": led["E_diss"],
           "E_latent": e.E_latent, "mass_clamp": led["mass_clamp"],
           "L_drift_pct": 100 * (e.angular_momentum() - L0) / abs(L0), "stable": e.is_stable()}
    if record:
        res["series"] = series
    return res


# ---------------------------------------------------------------- Stage C
def stage_C_hysteresis():
    print("\n=== STAGE C: HYSTERESIS ARM (up-sweep, persistence after de-spin, chi sweep, loop) ===")
    out = {}
    # (C1) UP branch: fresh runs, no de-spin (run to a long settle to capture deepest + final)
    up = []
    for M in [0.6, 0.7, 0.8, 0.9, 1.0]:
        r = run_persistence(M, chi_shock=1.0, despin_at=10**9, total=3200,
                            record=(abs(M - 0.9) < 1e-9))
        up.append({k: r[k] for k in ["M", "deepest", "max_pocket", "final_pocket",
                                     "E_diss", "mass_clamp", "L_drift_pct"]})
        if "series" in r:
            out["series_M0.9"] = r["series"]
        print(f"  UP   M={M:.1f} deepest={r['deepest']:.4f} max_pocket={r['max_pocket']:5d} "
              f"final_pocket={r['final_pocket']:5d} E_diss={r['E_diss']:.3e} Ldrift={r['L_drift_pct']:.2f}%")
    out["up_branch"] = up

    # (C2) PERSISTENCE after FULL de-spin at each peak M (chi_shock=1, the physical value)
    pers = []
    for M in [0.6, 0.7, 0.8, 0.9, 1.0]:
        r = run_persistence(M, chi_shock=1.0, despin_at=1200, total=3200)
        pers.append({k: r[k] for k in ["M", "deepest", "max_pocket", "final_pocket",
                                       "final_rho_core", "E_diss", "L_drift_pct"]})
        print(f"  PERS M={M:.1f} deepest={r['deepest']:.4f} max_pocket={r['max_pocket']:5d} "
              f"-> AFTER DE-SPIN final_pocket={r['final_pocket']:5d} final_rho_core={r['final_rho_core']:.4f}")
    out["persistence"] = pers

    # (C3) chi_shock SWEEP on persistence at M=1.0 (the crux CLIP test)
    chi = []
    for cs in [0.0, 0.25, 0.5, 1.0]:
        r = run_persistence(1.0, chi_shock=cs, despin_at=1200, total=3200)
        chi.append({k: r[k] for k in ["chi_shock", "deepest", "max_pocket", "final_pocket",
                                      "final_rho_core", "E_diss"]})
        print(f"  CHI  chi_shock={cs:.2f} max_pocket={r['max_pocket']:5d} -> final_pocket={r['final_pocket']:5d} "
              f"final_rho_core={r['final_rho_core']:.4f} E_diss={r['E_diss']:.3e}")
    out["chi_sweep"] = chi

    # (C4) DOWN-branch hysteresis loop: energize M=1.0, peak, step-down circulation through
    #      effective drive; record rho_core/pocket at each plateau vs the UP branch.
    e = SonicHorizonFlow2D(N=160, nu_art=5e-4, rho_diff=5e-4, chi_shock=1.0)
    e.energize_solid_body(M_edge=1.0, R_core=R_CORE)
    for _ in range(1200):  # reach peak
        e.step()
    down = []
    # current effective drive = 1.0; step the velocity amplitude down to each target M
    cur = 1.0
    for Mtgt in [1.0, 0.9, 0.8, 0.7, 0.6]:
        e.despin(Mtgt / cur)  # scale velocity amplitude to the target effective drive
        cur = Mtgt
        for _ in range(500):  # relax at this plateau
            e.step()
        down.append({"M_eff": Mtgt, "rho_core": e.rho_core()[0], "pocket": e.pocket_cells()})
        print(f"  DOWN M_eff={Mtgt:.1f} rho_core={e.rho_core()[0]:.4f} pocket={e.pocket_cells()}")
    out["down_branch"] = down
    return out


# ---------------------------------------------------------------- Stage D
def stage_D_handedness():
    print("\n=== STAGE D: HANDEDNESS ARM (co m=+1 vs counter m=-1 bulk OAM on the rotating pocket) ===")
    out = {}
    for M, chi in [(0.9, 1.0), (1.0, 1.0), (0.9, 0.0)]:
        # form for ~250 steps: flow established, transient pocket near its peak; the
        # frame-dragging handedness comes from the conserved circulation Γ. The probe is
        # a small bulk OAM pulse; baseline-subtraction isolates it from the rotating flow.
        co = reflectance(lambda e, _M=M, _c=chi: _form(e, _M, _c, 250), m=1)
        ct = reflectance(lambda e, _M=M, _c=chi: _form(e, _M, _c, 250), m=-1)
        asym = co["R"] - ct["R"]
        out[f"M{M}_chi{chi}"] = {"R_co": co["R"], "R_counter": ct["R"], "asym": asym,
                                 "e_inc_co": co["e_inc"], "e_inc_ct": ct["e_inc"]}
        print(f"  M={M} chi={chi}: R_co(m+1)={co['R']:.3f}  R_counter(m-1)={ct['R']:.3f}  "
              f"asym(co-counter)={asym:+.4f}")
    return out


def _form(e, M, chi, nform):
    e.chi_shock = chi
    e.energize_solid_body(M_edge=M, R_core=R_CORE)
    for _ in range(nform):
        e.step()


# ---------------------------------------------------------------- Stage E
def stage_E_control():
    print("\n=== STAGE E: CONTROL (floored-c² scheme: closure OFF -> effects must be ABSENT) ===")
    out = {"floored_predecessor": [], "closure_floor_raised": []}
    # (E1) raw predecessor CavitationFlow2D (c2_floor=1e-3): no one-way pocket, reversible
    for M in [0.6, 0.8, 1.0]:
        e = CavitationFlow2D(N=160, nu_art=5e-4, rho_diff=5e-4, c2_floor=1e-3)
        e.energize_solid_body(M_edge=M, R_core=R_CORE)
        deepest = 0.0
        for s in range(3200):
            if s == 1200:
                e.despin(0.0)
            e.step()
            deepest = min(deepest, e.rho_core()[0])
        c2raw = e.c_bulk2_raw(e.rho)
        pocket_final = int(np.count_nonzero((c2raw <= 0.0) & e.interior))
        out["floored_predecessor"].append({"M": M, "deepest": deepest,
                                            "final_rho_core": e.rho_core()[0],
                                            "pocket_final_c2le0": pocket_final})
        print(f"  FLOORED M={M:.1f} deepest={deepest:.4f} -> after de-spin final_rho_core={e.rho_core()[0]:.4f} "
              f"pocket(c2<=0)={pocket_final}")
    # (E2) closure engine with the floor RAISED back to 1e-3 + chi=0 (closure OFF): must match
    for M in [1.0]:
        r = run_persistence(M, chi_shock=0.0, despin_at=1200, total=3200, c2_floor=1e-3)
        out["closure_floor_raised"].append({k: r[k] for k in ["M", "deepest", "final_pocket",
                                                               "final_rho_core", "E_diss"]})
        print(f"  CLOSURE-OFF (c2_floor=1e-3,chi=0) M={M:.1f} deepest={r['deepest']:.4f} "
              f"final_pocket={r['final_pocket']} E_diss={r['E_diss']:.3e}")
    return out


def main():
    np.seterr(all="ignore")
    results = {
        "floor_rho_cav": RHO_CAV,
        "A_calibration": stage_A_calibration(),
        "B_gate": stage_B_apparatus_gate(),
        "C_hysteresis": stage_C_hysteresis(),
        "D_handedness": stage_D_handedness(),
        "E_control": stage_E_control(),
    }
    path = os.path.join(OUT, "sonic_horizon_closure_results.json")
    with open(path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nWrote {path}")
    return results


if __name__ == "__main__":
    main()
