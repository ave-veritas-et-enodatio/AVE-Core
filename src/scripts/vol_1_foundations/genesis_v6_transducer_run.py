"""
genesis-v6 PHASE 3 — THE GENESIS-RUN MATRIX (the full T1-T6 spec-sheet under the
LIVE chiral-boundary transducer)
====================================================================================

Executes the FROZEN matrix of `research/2026-06-10_genesis-v6-transducer_prereg.md`
§7 (committed ALONE @ 8b7aa40a; the PHASE-3 freeze). With the missing primitive D9
LIVE (chiral-boundary spin-orbit transducer + the PHASE-3 ω-recipient wired) and the
two hygiene blockers fixed (D11 pump, D10 deflagration), does the assembly pass the
spec-sheet — and is the lock the MOTION (D-PERM) as v5 certified?

THE QUESTION OF THE NIGHT: with the transducer LIVE, does the photon's helicity
become WINDING — w_pol != 0, above the extractor floor, helicity-odd, absent in
transducer-OFF?

DISCIPLINE: floors FIRST (ave-apparatus-floor-attribution v1.1, ORDERED BINS); D12
fail-fast BEFORE the matrix; every §7.6 sweep executed or the deviation stated;
verdict written FROM the numbers (Rule 11, no debugging toward a rescue). All numbers
dumped to JSON; the result doc reads FROM it (ave-driver-script-honesty).

Parallel via genesis_parallel_runner (spawn-safe: run_spec_worker is top-level,
deterministic per-seed; serial==parallel by construction). Run:
    PYTHONPATH=src .venv/bin/python src/scripts/vol_1_foundations/genesis_v6_transducer_run.py
"""

from __future__ import annotations

import copy
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from ave.core.longitudinal_burst_detector import LongitudinalBurstDetector  # noqa: E402
from ave.core.unified_genesis_engine import RHO_CAV, UnifiedGenesisEngine  # noqa: E402
from ave.core.electron_spec_suite import (  # noqa: E402
    spec_T1_mass_converges, spec_T2_charge_winding, spec_T3_spin,
    spec_T4_stability_kick, spec_T5_born_in_pairs, spec_T6_de_broglie,
)
from ave.utils.fast_winding_extractor import extract_2_3_omega_fast  # noqa: E402
from ave.utils.genesis_parallel_runner import RunSpec, run_specs  # noqa: E402

# ----------------------------------------------------- FROZEN run scale (§7.2/§7.9)
SEED = 20260610
N_MAIN = 48
M_MAIN = 1.8
N_BUILD = 3200
N_PERSIST = 1200
REC_EVERY = 200
FRAC = 0.85
DRIVE_AMP = 0.10
WAVELEN = 8.0
SIGMA_PH = 5.0
SIGMA_SEED = 4.0
R_FRAC = 0.18
CHI_DEFAULT = 0.02
OMEGA_FRAC_MAIN = 0.5        # the PHASE-3 ω-recipient split (NEW knob; swept §extra)
MEISSNER_MAIN = 0.05
LOCK_ETA_MAIN = 0.08
R_MEAS = 4.0                 # T2 extractor radius (F0b: >= 3 cells)


# ============================================================ engine build
def build_engine(cfg):
    """Assemble the v6 object from a config dict. snap-capable arms use c2_floor=0
    (the Z_bulk->0 reflector); no-snap arms use the 1e-3 hyperbolicity floor."""
    N = cfg["N"]
    snap = cfg["snap"]
    e = UnifiedGenesisEngine(
        N, bulk_density_on=True, snap_on=snap,
        c2_floor=(0.0 if snap else 1e-3),
        nu_art_bulk=cfg["nu_art"], rho_diff=5e-4,
        snap_payback_rate=cfg["payback"], delta_heal=cfg["delta_heal"],
        rho_cav=RHO_CAV, chi_shock=1.0,
        vent_mode="absorbed", snap_accounting="conservative",
        meissner_harden=cfg["meissner"],
        omega_sector_on=True, buckle_on=True, photon_coupling=True,
        lock_on=(cfg["lock_eta"] > 0.0), lock_eta=max(cfg["lock_eta"], 1e-9),
        wall_width=cfg["wall_width"],
        transducer_on=cfg["transducer_on"], chi_exch=cfg["chi_exch"],
        omega_recipient_frac=cfg["omega_frac"],
    )
    if cfg["seed"]:
        e.seed_lane1(frac=cfg["frac"], sigma=SIGMA_SEED, vent_into_seed=False)
    R_core = R_FRAC * e.N * e.dx
    e.energize_rotation_column(M_edge=cfg["M"], R_core=R_core, axis=2)
    e.freeze_wall_window()
    h = cfg["helicity"]
    e.drive_chiral_photon(helicity=h, sigma=SIGMA_PH, wavelength=WAVELEN,
                          amplitude=DRIVE_AMP, axis=2,
                          tau_zx_arm=cfg.get("tau_zx", False))
    return e


# ============================================================ measurement
def measure(e, axis=2):
    """All observables FROM the evolved field (ave-driver-script-honesty). The ω
    channel (T2/T3 charge+spin) and the u_adv channel (D-PERM motion) both read."""
    R_ring = R_FRAC * e.N
    pi_om = (e.omega - e.omega_prev) / e.dt
    res = extract_2_3_omega_fast(e.omega, pi_om, R_ring, R_MEAS, e.N)
    rc, _ = e.rho_core()
    led = e.transducer_ledger()
    # the ω-vorticity core sense (the chiral-twin probe in the ω channel; the column
    # swamps the u_adv core_sense -> that one is the demonstrated GEOMETRIC twin)
    omega_axial_vort = _axial_omega_vorticity_core(e, axis)
    return {
        "step": int(e.step_count),
        "E_V_naive": float(e.bulk_energy(True)),
        "E_V_cons": float(e.bulk_energy_conserved(True)),
        "H_total_cons": float(e.total_energy_unified(conserved=True)),
        "H_total_naive": float(e.total_energy_unified(conserved=False)),
        "pocket_cells": int(e.pocket_cells()),
        "rho_core": float(rc),
        "L_bulk": float(e.angular_momentum_bulk(axis)),
        "Gamma": float(e.bulk_circulation_z()),
        "L_omega_axial": float(e.angular_momentum_omega_axial(axis)),
        "spin_L_omega": float(e.spin_L_omega()),
        "Hbel": float(e.helicity_bel()),
        "w_tor": int(res["w_tor"]),
        "w_pol": int(res["w_pol"]),
        "w_tor_rel": float(res["w_tor_rel"]),
        "w_pol_rel": float(res["w_pol_rel"]),
        "w_pol_raw_median": float(res["w_pol_raw_median"]) if np.isfinite(res["w_pol_raw_median"]) else None,
        "is_2_3": bool(res["is_2_3"]),
        "core_sense_u": float(e.core_sense(axis)),
        "core_sense_omega": float(omega_axial_vort),
        "columnarity": float(e.columnarity(axis)),
        "L_transferred": float(led["L_transferred"]),
        "L_transferred_u": float(led["L_transferred_u"]),
        "L_transferred_omega": float(led["L_transferred_omega"]),
        "E_absorbed_sink": float(led["E_absorbed_sink"]),
        "passive_no_pump": bool(led["passive_no_pump"]),
        "transduce_events": int(led["transduce_events"]),
        "max_abs_V": float(np.max(np.abs(e.V * e.interior_mask()))),
        "max_abs_omega": float(np.max(np.abs(e.omega * e.interior_mask()[..., None]))),
        "max_abs_u": float(np.max(np.abs(e.u_adv))),
        "finite": bool(np.all(np.isfinite(e.omega)) and np.all(np.isfinite(e.V))
                       and np.all(np.isfinite(e.rho_bar))),
    }


def _axial_omega_vorticity_core(e, axis):
    """Signed inner-disk circulation of the ω-z component about `axis` — the
    chiral-twin probe in the ω channel (transducer-driven; structurally 0 for the
    achiral arm). Mid-plane inner disk (column shear excluded)."""
    mid = e.N // 2
    if axis == 2:
        fz = e.omega[:, :, mid, 2]
        a1, a2 = e._bx[:, :, mid], e._by[:, :, mid]
    elif axis == 1:
        fz = e.omega[:, mid, :, 1]
        a1, a2 = e._bx[:, mid, :], e._bz[:, mid, :]
    else:
        fz = e.omega[mid, :, :, 0]
        a1, a2 = e._by[mid, :, :], e._bz[mid, :, :]
    rc = np.sqrt(a1 ** 2 + a2 ** 2)
    disk = rc < (0.25 * 0.5 * e.N * e.dx)
    return float(np.sum(fz[disk]) * e.dx ** 2)


# ============================================================ the worker (spawn-safe)
def run_spec_worker(*, cfg, do_persist=False, do_spec=False, do_burst=False,
                    burst_floor=None, n_build=N_BUILD, n_persist=N_PERSIST,
                    rec_every=REC_EVERY):
    """One independent run: BUILD (energize+drive+step n_build) recording a series,
    then optionally P1 (drive-off, L-conserved) + P2 (forced de-spin) via deepcopy,
    optionally the T1-T6 spec-sheet, optionally the D6 birth-flash detector.
    Returns a JSON-serializable dict (no engine objects). Deterministic per SEED."""
    np.random.seed(SEED)
    t0 = time.time()
    e = build_engine(cfg)
    cert = e.seed_certificate() if cfg["seed"] else {"passes": None, "topology_null": None}
    det = LongitudinalBurstDetector(floor=burst_floor, threshold_mult=3.0) if do_burst else None
    if det is not None:
        det.record(e)

    series = [measure(e)]
    onset = None
    for s in range(1, n_build + 1):
        e.step()
        if det is not None:
            det.record(e)
        if onset is None and e.pocket_cells() > 0:
            onset = int(e.step_count)
        if s % rec_every == 0 or s == n_build:
            series.append(measure(e))
            if not series[-1]["finite"]:
                series[-1]["NONFINITE"] = True
                break
    built = measure(e)
    twin = e.twin_pocket_ledger()

    out = {
        "name": cfg["name"], "cfg": {k: cfg[k] for k in cfg if k != "name"},
        "seed_cert": {"passes": cert.get("passes"), "topology_null": cert.get("topology_null")},
        "snap_onset": onset,
        "build_series": series,
        "built": built,
        "twin_pocket": {"RH_cells": twin["RH_pocket_cells"], "LH_cells": twin["LH_pocket_cells"],
                        "twin_present": twin["twin_present"], "total": twin["total_pocket_cells"]},
        "wall_s": time.time() - t0,
    }

    if do_persist:
        p1 = copy.deepcopy(e)
        p1_series = _persist(p1, n_persist, rec_every, despin=False)
        p2 = copy.deepcopy(e)
        p2.despin_bulk(0.0)
        p2_series = _persist(p2, n_persist, rec_every, despin=True)
        out["P1_final"] = p1_series[-1]
        out["P2_final"] = p2_series[-1]
        out["P1_series"] = p1_series
        out["P2_series"] = p2_series

    if do_spec:
        out["spec_sheet"] = spec_sheet(e, series)

    if det is not None and det.floor is not None:
        out["birth_flash"] = {"bursts": det.scan(),
                              "total_burst_energy": det.total_burst_energy()}
    return out


def _persist(e, n, rec_every, despin):
    ser = [measure(e)]
    for s in range(1, n + 1):
        e.step()
        if s % rec_every == 0 or s == n:
            ser.append(measure(e))
            if not ser[-1]["finite"]:
                break
    return ser


# ============================================================ spec sheet (T1-T6)
def spec_sheet(e, build_series):
    """T1-T6 on the built object, floors first (ORDERED BINS §7.5/§7.7). T1 mass in
    the CONSERVED functional (CP2/D11). T2 charge = the ω (2,3) winding (the headline
    question). T5 twin = the ω-channel chiral asymmetry (the u_adv core_sense is the
    demonstrated GEOMETRIC false positive — the column swamps it)."""
    axis = 2
    drift_floor = 5e-2
    ev_cons = [s["E_V_cons"] for s in build_series]
    htot_cons = [s["H_total_cons"] for s in build_series]
    T1_EV = spec_T1_mass_converges(ev_cons, drift_floor=drift_floor)
    T1_EV["E_V_cons_first"] = float(ev_cons[0]); T1_EV["E_V_cons_last"] = float(ev_cons[-1])
    T1_H = spec_T1_mass_converges(htot_cons, drift_floor=drift_floor)
    T1_H["H_cons_first"] = float(htot_cons[0]); T1_H["H_cons_last"] = float(htot_cons[-1])

    R_ring = R_FRAC * e.N
    T2 = spec_T2_charge_winding(e, R=R_ring, r=R_MEAS, r_meas_floor=3.0)
    T3 = spec_T3_spin(e, R_ring=R_FRAC * e.N * e.dx, axis=axis)
    T3["spin_L_omega"] = float(e.spin_L_omega())
    T3["L_omega_axial"] = float(e.angular_momentum_omega_axial(axis))

    # T4 kick: perturb u_adv + V + omega, re-verify T1(mass bounded)+T3(sign)
    ek = copy.deepcopy(e)
    rng = np.random.RandomState(SEED)
    mm = ek.interior_mask()
    ek.u_adv += 0.02 * rng.standard_normal(ek.u_adv.shape) * mm[..., None]
    ek.V += 0.02 * rng.standard_normal(ek.V.shape) * mm
    ek.omega += 0.02 * rng.standard_normal(ek.omega.shape) * mm[..., None]
    ev0 = ek.bulk_energy_conserved(True); L0 = ek.angular_momentum_omega_axial(axis)
    for _ in range(300):
        ek.step()
    ev1 = ek.bulk_energy_conserved(True); L1 = ek.angular_momentum_omega_axial(axis)
    reverify = bool(np.isfinite(ev1) and ev1 < 5.0 * (abs(ev0) + 1e-9)
                    and np.isfinite(L1))
    T4 = spec_T4_stability_kick(lambda: reverify)
    T4.update({"E_V_cons_pre": float(ev0), "E_V_cons_post": float(ev1),
               "L_omega_pre": float(L0), "L_omega_post": float(L1)})

    T5 = spec_T5_born_in_pairs(e, axis=axis)
    T5["core_sense_omega"] = float(_axial_omega_vorticity_core(e, axis))
    T5["core_sense_u_GEOMETRIC"] = float(e.core_sense(axis))

    T6 = de_broglie_probe(e)
    return {"T1_mass_EV_cons": T1_EV, "T1_H_total_cons": T1_H, "T2_charge": T2,
            "T3_spin": T3, "T4_kick": T4, "T5_pairs": T5, "T6_de_broglie": T6}


def de_broglie_probe(src):
    momenta, lambdas = [], []
    for u0 in (0.10, 0.20, 0.40):
        e = copy.deepcopy(src)
        m = e.interior_mask()
        e.u_adv[..., 0] += u0 * m
        for _ in range(120):
            e.step()
        prof = np.sum(e.rho_bar * m, axis=(1, 2))
        prof = prof - prof.mean()
        spec = np.abs(np.fft.rfft(prof)); spec[0] = 0.0
        k = int(np.argmax(spec))
        lam = (len(prof) / k) if k > 0 else len(prof)
        momenta.append(u0); lambdas.append(float(lam) * e.dx)
    res = spec_T6_de_broglie(momenta, lambdas)
    res["momenta"] = momenta; res["lambdas"] = lambdas
    return res


# ============================================================ config helper
def make_cfg(name, *, N=N_MAIN, seed=True, snap=True, helicity=1, transducer_on=True,
             omega_frac=OMEGA_FRAC_MAIN, chi_exch=CHI_DEFAULT, meissner=MEISSNER_MAIN,
             delta_heal=0.0, payback=1.0, lock_eta=LOCK_ETA_MAIN, nu_art=5e-4,
             wall_width=0.12, frac=FRAC, M=M_MAIN, tau_zx=False):
    return dict(name=name, N=N, seed=seed, snap=snap, helicity=helicity,
                transducer_on=transducer_on, omega_frac=omega_frac, chi_exch=chi_exch,
                meissner=meissner, delta_heal=delta_heal, payback=payback,
                lock_eta=lock_eta, nu_art=nu_art, wall_width=wall_width, frac=frac,
                M=M, tau_zx=tau_zx)


# ============================================================ FLOORS (ORDERED BINS)
def recalibrate_floors():
    """All inherited floors RE-MEASURED at the Run config (§7.2 — a floor carried
    from a different config is invalid). Structural zeros re-CONFIRMED."""
    np.random.seed(SEED)
    out = {}
    # F-CLOSE: no-snap drive-off known-null -> max positive H_total_cons excursion
    cfgc = make_cfg("FLOOR_close", snap=False, transducer_on=False)
    ec = build_engine(cfgc)
    for _ in range(400):
        ec.step()
    e_off = copy.deepcopy(ec)
    e_off.drive_helicity = 0
    e_off.w[:] = 0.0; e_off.w_prev[:] = 0.0   # drive-off
    H = [e_off.total_energy_unified(conserved=True)]
    for _ in range(800):
        e_off.step(); H.append(e_off.total_energy_unified(conserved=True))
    H = np.asarray(H); H0 = H[0]
    f_close = float(np.max((H - H0) / (abs(H0) + 1e-30)))
    out["F_CLOSE_max_pos_excursion_frac"] = f_close

    # F-EV: the quiet-build E_V plateau level (pre-snap)
    out["F_EV_plateau"] = float(ec.bulk_energy(True))

    # F-BURST: free-run no-snap pressure-integral scatter (D6 known-null)
    cfgb = make_cfg("FLOOR_burst", snap=True, transducer_on=False, M=0.6)  # sub-threshold
    eb = build_engine(cfgb)
    f_burst = float(LongitudinalBurstDetector.calibrate_floor(eb, steps=120))
    out["F_BURST_floor"] = f_burst
    out["F_BURST_gate_3x"] = 3.0 * f_burst

    # F0e: quiet-phase L_bulk / Gamma drift on a no-snap column (drive-off)
    cfgd = make_cfg("FLOOR_drift", seed=False, snap=False, transducer_on=False, lock_eta=0.0)
    ed = build_engine(cfgd)
    ed.w[:] = 0.0; ed.w_prev[:] = 0.0
    L0 = ed.angular_momentum_bulk(2); G0 = ed.bulk_circulation_z()
    for _ in range(800):
        ed.step()
    out["F0e_L_bulk_drift_frac"] = float((ed.angular_momentum_bulk(2) - L0) / (abs(L0) + 1e-30))
    out["F0e_Gamma_drift_frac"] = float((ed.bulk_circulation_z() - G0) / (abs(G0) + 1e-30))

    # F-EXCHANGE / F-DRIFT structural zeros (chi=0 -> no transducer source)
    cfg0 = make_cfg("FLOOR_exchange", transducer_on=True, chi_exch=0.0)
    e0 = build_engine(cfg0)
    Lom0 = e0.angular_momentum_omega_axial(2)
    for _ in range(200):
        e0.step()
    out["F_EXCHANGE_chi0_dLomega"] = float(abs(e0.angular_momentum_omega_axial(2) - Lom0))
    out["F_EXCHANGE_chi0_Ltransferred"] = float(e0.L_transferred)

    # F-PROBE (m-even): the spin probe separates +/-h on the known seed (keeper echo)
    s_rh = build_engine(make_cfg("p", helicity=1, chi_exch=0.0)).photon_spin_axial(2)
    s_lh = build_engine(make_cfg("p", helicity=-1, chi_exch=0.0)).photon_spin_axial(2)
    s_ac = build_engine(make_cfg("p", helicity=0, chi_exch=0.0)).photon_spin_axial(2)
    out["F_PROBE"] = {"S_rh": float(s_rh), "S_lh": float(s_lh), "S_ac": float(s_ac),
                      "separates": bool(s_rh * s_lh < 0.0 and abs(s_ac) < 1e-9 * (abs(s_rh) + 1e-30))}
    return out


# ============================================================ main orchestration
def main():
    t_start = time.time()
    results = {
        "prereg": "research/2026-06-10_genesis-v6-transducer_prereg.md (§7, FROZEN @ 8b7aa40a)",
        "engine": "src/ave/core/unified_genesis_engine.py (D9 + PHASE-3 ω-recipient)",
        "scale": dict(N=N_MAIN, M=M_MAIN, n_build=N_BUILD, n_persist=N_PERSIST,
                      frac=FRAC, chi_exch=CHI_DEFAULT, omega_frac=OMEGA_FRAC_MAIN,
                      meissner=MEISSNER_MAIN, seed=SEED),
        "RHO_CAV": RHO_CAV,
    }

    print("[1/5] FLOORS (recalibrated at the Run config; ORDERED BINS) ...", flush=True)
    floors = recalibrate_floors()
    results["floors"] = floors
    print(f"    F-CLOSE={floors['F_CLOSE_max_pos_excursion_frac']:.4e} "
          f"F-EV={floors['F_EV_plateau']:.3f} F-BURST={floors['F_BURST_floor']:.3e} "
          f"F-PROBE.sep={floors['F_PROBE']['separates']} "
          f"({time.time()-t_start:.0f}s)", flush=True)

    # ---------- D12 FAIL-FAST (cheap, BEFORE the matrix; §7.8) ----------
    print("[2/5] D12 fail-fast (transducer-alive + achiral-null + pump pre-gate) ...", flush=True)
    results["D12"] = d12_fail_fast(floors)
    print(f"    D12: {json.dumps(results['D12']['summary'])}", flush=True)
    if results["D12"]["abort"]:
        results["gate_verdict"] = "TRANSDUCER-DEAD"
        _dump(results, t_start)
        return

    # ---------- THE ARM MATRIX (§7.3) ----------
    print("[3/5] arm matrix (9 arms, build+P1+P2; MAIN spec-sheet+flash) ...", flush=True)
    arm_specs = [
        RunSpec("MAIN", run_spec_worker,
                dict(cfg=make_cfg("MAIN", helicity=1), do_persist=True, do_spec=True)),
        RunSpec("C-transducer-OFF", run_spec_worker,
                dict(cfg=make_cfg("C-transducer-OFF", helicity=1, transducer_on=False),
                     do_persist=True)),
        RunSpec("C-transducer-OFF-LH", run_spec_worker,
                dict(cfg=make_cfg("C-transducer-OFF-LH", helicity=-1, transducer_on=False),
                     do_persist=False, n_build=600)),  # byte-identity probe vs OFF-RH
        RunSpec("C-achiral", run_spec_worker,
                dict(cfg=make_cfg("C-achiral", helicity=0), do_persist=True)),
        RunSpec("C-LH", run_spec_worker,
                dict(cfg=make_cfg("C-LH", helicity=-1), do_persist=True)),
        RunSpec("C-no-seed", run_spec_worker,
                dict(cfg=make_cfg("C-no-seed", seed=False), do_persist=True)),
        RunSpec("C-no-snap", run_spec_worker,
                dict(cfg=make_cfg("C-no-snap", snap=False), do_persist=True)),
        RunSpec("C-tauzx-on", run_spec_worker,
                dict(cfg=make_cfg("C-tauzx-on", tau_zx=True), n_build=600)),
        RunSpec("C-tauzx-off", run_spec_worker,
                dict(cfg=make_cfg("C-tauzx-off", tau_zx=False), n_build=600)),
        # birth-flash capture: MAIN to the K3=4000 stop-point (onset ~3396 > 3200)
        RunSpec("MAIN-flash4000", run_spec_worker,
                dict(cfg=make_cfg("MAIN-flash4000", helicity=1), do_burst=True,
                     burst_floor=floors["F_BURST_floor"], n_build=4000)),
    ]
    arms = run_specs(arm_specs, serial=False, raise_on_error=False)
    results["arms"] = {k: _strip(v) for k, v in arms.items()}
    for k, v in arms.items():
        if isinstance(v, dict):
            b = v["built"]
            print(f"    {k:22s} EVc={b['E_V_cons']:.2f} pocket={b['pocket_cells']} "
                  f"Lom={b['L_omega_axial']:+.2e} Hbel={b['Hbel']:+.2e} "
                  f"(wt,wp)=({b['w_tor']},{b['w_pol']}) wprel={b['w_pol_rel']:.3f} "
                  f"onset={v.get('snap_onset')} ({v['wall_s']:.0f}s)", flush=True)
        else:
            print(f"    {k:22s} ERROR {v}", flush=True)

    # ---------- THE MANDATED SWEEPS (§7.6 + the ω-frac new knob) ----------
    print("[4/5] mandated sweeps (§210 — every knob the bins depend on) ...", flush=True)
    results["sweeps"] = run_all_sweeps(floors)

    # ---------- BINS + VERDICT (§7.5/§7.7) ----------
    print("[5/5] floor-gated bins + spec-sheet verdict ...", flush=True)
    results["analysis"] = analyze(results, floors)
    _dump(results, t_start)
    _make_figures(results)
    _dump(results, t_start)


def d12_fail_fast(floors):
    """D12(i) transducer-alive (RH != LH within 200 steps, BOTH u_adv AND ω); D12(ii)
    achiral known-null; D11 pump pre-gate (MAIN-config DRIVE-OFF H_total_cons shows no
    positive excursion above F-CLOSE — the pump test is drive-OFF; during build the
    drive legitimately injects energy)."""
    np.random.seed(SEED)
    e_rh = build_engine(make_cfg("d12_rh", helicity=1))
    e_lh = build_engine(make_cfg("d12_lh", helicity=-1))
    e_ac = build_engine(make_cfg("d12_ac", helicity=0))
    for _ in range(200):
        e_rh.step(); e_lh.step(); e_ac.step()
    u_div = float(np.max(np.abs(e_rh.u_adv - e_lh.u_adv)))
    om_div = float(np.max(np.abs(e_rh.omega - e_lh.omega)))
    Lom_ac = float(abs(e_ac.angular_momentum_omega_axial(2)))
    f_exch = max(floors["F_EXCHANGE_chi0_dLomega"], 1e-300)
    alive = bool(u_div > 0.0 or om_div > 0.0)
    achiral_null = bool(Lom_ac <= 3.0 * f_exch)
    # D11 PUMP PRE-GATE (drive-off): build MAIN to a quiet pre-snap plateau, kill the
    # drive, run, check H_total_cons never rises above F-CLOSE.
    ep = build_engine(make_cfg("d12_pump", helicity=1))
    for _ in range(400):
        ep.step()
    ep.w[:] = 0.0; ep.w_prev[:] = 0.0  # drive-off
    H0 = ep.total_energy_unified(conserved=True); Hmax = H0
    for _ in range(800):
        ep.step(); Hmax = max(Hmax, ep.total_energy_unified(conserved=True))
    H_pos_excursion = float((Hmax - H0) / (abs(H0) + 1e-30))
    pump_ok = bool(H_pos_excursion <= floors["F_CLOSE_max_pos_excursion_frac"] + 1e-9)
    return {
        "u_div_RH_LH@200": u_div, "omega_div_RH_LH@200": om_div, "alive": alive,
        "achiral_Lomega": Lom_ac, "achiral_null": achiral_null,
        "H_pos_excursion_driveoff": H_pos_excursion,
        "F_CLOSE": floors["F_CLOSE_max_pos_excursion_frac"],
        "pump_pre_gate_ok": pump_ok,
        "abort": bool(not alive),
        "summary": {"alive": alive, "achiral_null": achiral_null, "pump_ok": pump_ok},
    }


def run_all_sweeps(floors):
    sw = {}
    specs = []
    # 1. chi_exch (the D9 coupling robustness; the whole v6 thesis)
    for chi in (0.0, 9e-4, 0.005, 0.02, 0.08):
        specs.append(RunSpec(("chi", chi), run_spec_worker,
                     dict(cfg=make_cfg(f"chi_{chi}", chi_exch=chi,
                                       transducer_on=(chi > 0.0)), n_build=2400)))
    # 2/3. delta_heal x payback (snap-channel CLIP recheck under the live transducer)
    for dh in (0.0, 0.02, 0.05):
        for pb in (0.0, 1.0, 5.0):
            specs.append(RunSpec(("dhpb", dh, pb), run_spec_worker,
                         dict(cfg=make_cfg(f"dh{dh}_pb{pb}", delta_heal=dh, payback=pb),
                              n_build=3500, do_persist=True, n_persist=600)))
    # 4. K3 stop-time (T1 convergence; build {2400,3200,4000} read from one 4000 run +
    #    persist {300,600,1200} from a 4000 deepcopy handled in post)
    specs.append(RunSpec(("K3", 4000), run_spec_worker,
                 dict(cfg=make_cfg("K3_4000"), n_build=4000, do_persist=True,
                      n_persist=1200, rec_every=200)))
    # 5. meissner increment (deflagration containment)
    for ms in (0.0, 0.02, 0.05, 0.10):
        specs.append(RunSpec(("meissner", ms), run_spec_worker,
                     dict(cfg=make_cfg(f"ms_{ms}", meissner=ms), n_build=3600)))
    # 6. nu_art (D-PERM motion-lock; v5-style no-snap column drive-off decay)
    sw["nu_art"] = sweep_nu_art()
    # 7. K2 N-resolution
    for N in (40, 48, 56):
        specs.append(RunSpec(("K2", N), run_spec_worker,
                     dict(cfg=make_cfg(f"N_{N}", N=N), n_build=3600)))
    # 8. wall_width (D9 sharpness robustness)
    for ww in (0.06, 0.12, 0.20):
        specs.append(RunSpec(("ww", ww), run_spec_worker,
                     dict(cfg=make_cfg(f"ww_{ww}", wall_width=ww), n_build=2000)))
    # 9. lock_eta (T3 spin eta-invariance)
    for eta in (0.0, 0.05, 0.08, 0.12):
        specs.append(RunSpec(("lock_eta", eta), run_spec_worker,
                     dict(cfg=make_cfg(f"eta_{eta}", lock_eta=eta), n_build=2000)))
    # 10. K4 seed frac (regime gate)
    for fr in (0.30, 0.60, 0.85, 0.95):
        specs.append(RunSpec(("K4", fr), run_spec_worker,
                     dict(cfg=make_cfg(f"frac_{fr}", frac=fr), n_build=2400)))
    # EXTRA (the NEW omega-recipient knob — inventoried + swept; ave-apparatus-floor-attr)
    for of in (0.0, 0.5, 1.0):
        specs.append(RunSpec(("omega_frac", of), run_spec_worker,
                     dict(cfg=make_cfg(f"of_{of}", omega_frac=of), n_build=2000)))

    raw = run_specs(specs, serial=False, raise_on_error=False)
    sw["matrix"] = {repr(k): _strip(v) for k, v in raw.items()}
    return sw


def sweep_nu_art():
    """K1/D8 attribution: a no-snap rotating column (drive-off), regress L_bulk +
    deficit decay vs nu_art. Decay -> 0 as nu_art -> 0 (tracks the knob) => apparatus;
    a nonzero plateau => physics (the D-PERM motion-lock; v5 deficit -0.0516 invariant)."""
    out = []
    for nu in (1e-4, 5e-4, 1e-3, 2e-3, 5e-3):
        np.random.seed(SEED)
        e = build_engine(make_cfg("nu", seed=False, snap=False, transducer_on=False,
                                  lock_eta=0.0, nu_art=nu, M=1.2))
        e.w[:] = 0.0; e.w_prev[:] = 0.0
        L0 = e.angular_momentum_bulk(2); g0 = e.bulk_circulation_z(); r0 = e.rho_core()[0]
        for _ in range(800):
            e.step()
        L1 = e.angular_momentum_bulk(2); g1 = e.bulk_circulation_z(); r1 = e.rho_core()[0]
        out.append({"nu_art": nu,
                    "L_bulk_decay_frac": float((L1 - L0) / (abs(L0) + 1e-30)),
                    "Gamma_decay_frac": float((g1 - g0) / (abs(g0) + 1e-30)),
                    "deficit_deepening": float(r1 - r0),
                    "L_ratio": float(abs(L1) / (abs(L0) + 1e-30))})
    return out


# ============================================================ analysis / bins
def analyze(results, floors):
    arms = results["arms"]
    a = {}

    def built(name):
        v = arms.get(name)
        return v["built"] if isinstance(v, dict) and "built" in v else None

    main = built("MAIN"); off = built("C-transducer-OFF")
    lh = built("C-LH"); ac = built("C-achiral")
    f_exch = max(floors["F_EXCHANGE_chi0_dLomega"], 1e-300)

    # --- the load-bearing contrast: MAIN vs C-transducer-OFF (the D9-isolated signal) ---
    if main and off:
        a["D9_isolated"] = {
            "dLomega_MAIN_minus_OFF": main["L_omega_axial"] - off["L_omega_axial"],
            "dHbel_MAIN_minus_OFF": main["Hbel"] - off["Hbel"],
            "L_transferred_omega_MAIN": main["L_transferred_omega"],
            "above_F_EXCHANGE_100x": bool(abs(main["L_transferred_omega"]) >= 100 * f_exch),
        }
    # --- helicity-odd (MAIN vs C-LH) in the transducer-deposited ω channel ---
    if main and lh:
        rh_d = main["L_transferred_omega"]; lh_d = lh["L_transferred_omega"]
        odd = abs(rh_d - lh_d) / (abs(rh_d) + abs(lh_d) + 1e-30)
        a["helicity_odd_omega"] = {
            "L_transferred_omega_RH": rh_d, "L_transferred_omega_LH": lh_d,
            "sign_reversal": bool(np.sign(rh_d) == -np.sign(lh_d) and rh_d != 0),
            "odd_fraction": float(odd),
            "Lomega_axial_RH": main["L_omega_axial"], "Lomega_axial_LH": lh["L_omega_axial"],
            "Hbel_RH": main["Hbel"], "Hbel_LH": lh["Hbel"]}
    # --- the CONTAMINATION FLAG (§7.3): C-transducer-OFF byte-identity across handedness ---
    off_lh = built("C-transducer-OFF-LH")
    if off and off_lh:
        a["transducer_OFF_byte_identity"] = {
            "Hbel_OFF_RH": off["Hbel"], "Hbel_OFF_LH": off_lh["Hbel"],
            "Lbulk_OFF_RH": off["L_bulk"], "Lbulk_OFF_LH": off_lh["L_bulk"],
            "u_channel_byte_identical": bool(abs(off["L_bulk"] - off_lh["L_bulk"])
                                             <= abs(floors["F0e_L_bulk_drift_frac"]) * abs(off["L_bulk"]) + 1e-9),
            "omega_channel_byte_identical": bool(abs(off["Hbel"] - off_lh["Hbel"]) < 1e-12),
            "FLAG": "the inherited BUCKLE couples helicity->omega (Hbel); the clean D9 "
                    "contrast is MAIN-minus-OFF (same handedness), not RH-vs-LH"}
    # --- the WINDING question (T2 w_pol) ---
    if main:
        a["winding_question"] = {
            "w_pol_MAIN": main["w_pol"], "w_pol_rel_MAIN": main["w_pol_rel"],
            "w_tor_MAIN": main["w_tor"], "is_2_3_MAIN": main["is_2_3"],
            "w_pol_above_reliability_0.1": bool(main["w_pol_rel"] > 0.1),
            "w_pol_OFF": off["w_pol"] if off else None,
            "w_pol_LH": lh["w_pol"] if lh else None,
            "w_pol_achiral": ac["w_pol"] if ac else None}
    # --- the chiral twin (sharpened T5) in the omega channel ---
    if main and lh and ac:
        cs_rh = main["core_sense_omega"]; cs_lh = lh["core_sense_omega"]; cs_ac = ac["core_sense_omega"]
        a["chiral_twin_omega"] = {
            "core_sense_omega_RH": cs_rh, "core_sense_omega_LH": cs_lh,
            "core_sense_omega_achiral": cs_ac,
            "sign_reversal": bool(np.sign(cs_rh) == -np.sign(cs_lh) and cs_rh != 0),
            "achiral_at_floor": bool(abs(cs_ac) <= 0.05 * (abs(cs_rh) + abs(cs_lh) + 1e-30)),
            "u_core_sense_RH_GEOMETRIC": main["core_sense_u"],
            "u_core_sense_achiral_GEOMETRIC": ac["core_sense_u"],
            "u_twin_is_geometric_false_positive": bool(
                abs(main["core_sense_u"] - ac["core_sense_u"]) < 1e-6 * abs(main["core_sense_u"]))}
    # --- D-PERM (the motion-lock; P1 L_bulk ratio) ---
    a["D_PERM"] = {}
    for name in ("MAIN", "C-no-snap", "C-LH"):
        v = arms.get(name)
        if isinstance(v, dict) and "P1_final" in v:
            Lb = v["built"]["L_bulk"]; Lp1 = v["P1_final"]["L_bulk"]
            a["D_PERM"][name] = {"L_bulk_built": Lb, "L_bulk_P1": Lp1,
                                 "L_ratio_P1": float(abs(Lp1) / (abs(Lb) + 1e-30)),
                                 "pocket_built": v["built"]["pocket_cells"],
                                 "pocket_P2": v["P2_final"]["pocket_cells"]}
    # --- Fork-A tau_zx inertness flag ---
    on = built("C-tauzx-on"); offz = built("C-tauzx-off")
    if on and offz:
        a["tau_zx_FORK_A"] = {
            "Hbel_on": on["Hbel"], "Hbel_off": offz["Hbel"],
            "byte_identical": bool(abs(on["Hbel"] - offz["Hbel"]) < 1e-14
                                   and abs(on["L_omega_axial"] - offz["L_omega_axial"]) < 1e-14),
            "FLAG": "tau_zx_arm is an INERT flag (set, never wired into any force) — "
                    "Fork-A is NOT implemented in the unified engine; the arms are "
                    "byte-identical by construction, NOT an empirical null"}
    return a


# ============================================================ figures
def _make_figures(results):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    figdir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..",
                                          "research", "figures"))
    os.makedirs(figdir, exist_ok=True)
    paths = []
    arms = results["arms"]

    # FIG 1: T1 mass — E_V_cons(t) per chiral/control arm (bounded vs v5 detonation)
    try:
        fig, ax = plt.subplots(figsize=(7, 4.2))
        for name in ("MAIN", "C-transducer-OFF", "C-LH", "C-achiral", "C-no-snap"):
            v = arms.get(name)
            if isinstance(v, dict):
                t = [s["step"] for s in v["build_series"]]
                ev = [s["E_V_cons"] for s in v["build_series"]]
                ax.plot(t, ev, label=name, lw=1.4)
        ax.set_xlabel("build step"); ax.set_ylabel("E_V_cons (dilatation mass, CP2 functional)")
        ax.set_title("T1 mass: conserved-functional E_V bounded (v6 hygiene) — vs v5 50339 detonation")
        ax.legend(fontsize=7); fig.tight_layout()
        p = os.path.join(figdir, "fig_v6_T1_mass.png"); fig.savefig(p, dpi=110); plt.close(fig); paths.append(p)
    except Exception as exc:  # noqa: BLE001
        results.setdefault("fig_errors", []).append(f"T1: {exc!r}")

    # FIG 2: the ω-channel chiral signal — L_omega_axial(t) RH vs LH vs OFF vs achiral
    try:
        fig, ax = plt.subplots(figsize=(7, 4.2))
        for name in ("MAIN", "C-LH", "C-transducer-OFF", "C-achiral"):
            v = arms.get(name)
            if isinstance(v, dict):
                t = [s["step"] for s in v["build_series"]]
                lo = [s["L_omega_axial"] for s in v["build_series"]]
                ax.plot(t, lo, label=name, lw=1.4)
        ax.axhline(0, ls=":", c="k", lw=0.8)
        ax.set_xlabel("build step"); ax.set_ylabel("L_omega,axial (the ω winding-carrier AM)")
        ax.set_title("D9 transducer: helicity-odd ω-channel coupling (RH=−LH; OFF/achiral null)")
        ax.legend(fontsize=8); fig.tight_layout()
        p = os.path.join(figdir, "fig_v6_omega_chiral.png"); fig.savefig(p, dpi=110); plt.close(fig); paths.append(p)
    except Exception as exc:  # noqa: BLE001
        results.setdefault("fig_errors", []).append(f"omega: {exc!r}")

    # FIG 3: the winding question — w_pol & reliability vs chi_exch (does winding emerge?)
    try:
        sm = results["sweeps"]["matrix"]
        chis, wpols, rels = [], [], []
        for k, v in sm.items():
            if k.startswith("('chi'") and isinstance(v, dict):
                chis.append(v["cfg"]["chi_exch"]); wpols.append(v["built"]["w_pol"])
                rels.append(v["built"]["w_pol_rel"])
        order = np.argsort(chis)
        chis = np.array(chis)[order]; wpols = np.array(wpols)[order]; rels = np.array(rels)[order]
        fig, ax = plt.subplots(figsize=(7, 4.2))
        ax.plot(chis, wpols, "o-", label="w_pol (modal integer)")
        ax.plot(chis, rels, "s--", label="w_pol reliability")
        ax.axhline(0.1, ls=":", c="r", lw=1, label="reliability floor 0.1")
        ax.axhline(3.0, ls=":", c="g", lw=1, label="target poloidal '3'")
        ax.set_xlabel("chi_exch (transducer coupling)"); ax.set_ylabel("w_pol / reliability")
        ax.set_title("THE WINDING QUESTION: does w_pol emerge? (vs the χ̃ coupling)")
        ax.legend(fontsize=8); fig.tight_layout()
        p = os.path.join(figdir, "fig_v6_winding_question.png"); fig.savefig(p, dpi=110); plt.close(fig); paths.append(p)
    except Exception as exc:  # noqa: BLE001
        results.setdefault("fig_errors", []).append(f"winding: {exc!r}")

    # FIG 4: nu_art D-PERM attribution
    try:
        sw = results["sweeps"]["nu_art"]
        nu = [d["nu_art"] for d in sw]; ld = [abs(d["L_bulk_decay_frac"]) for d in sw]
        dd = [abs(d["deficit_deepening"]) for d in sw]
        fig, ax = plt.subplots(figsize=(6.6, 4.0))
        ax.loglog(nu, ld, "o-", label="|L_bulk decay frac|")
        ax.loglog(nu, dd, "s-", label="|deficit deepening|")
        ax.set_xlabel("nu_art"); ax.set_ylabel("|change| (800 steps)")
        ax.set_title("D-PERM (K1/D8): does the motion-lock track nu_art?")
        ax.legend(fontsize=8); ax.grid(True, which="both", alpha=0.3); fig.tight_layout()
        p = os.path.join(figdir, "fig_v6_nu_art_dperm.png"); fig.savefig(p, dpi=110); plt.close(fig); paths.append(p)
    except Exception as exc:  # noqa: BLE001
        results.setdefault("fig_errors", []).append(f"nu_art: {exc!r}")

    results["figures"] = paths


# ============================================================ io
def _strip(v):
    """Drop the heavy P1/P2 full series from the stored arm (keep finals + build
    series) so the JSON stays readable; keep everything load-bearing."""
    if not isinstance(v, dict):
        return {"ERROR": repr(v)}
    out = dict(v)
    for k in ("P1_series", "P2_series"):
        out.pop(k, None)
    return out


def _dump(results, t_start):
    out_json = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..", "..", "..", "research",
        "2026-06-10_genesis-v6-transducer-run_results.json"))
    with open(out_json, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n[dump] {time.time()-t_start:.0f}s -> {out_json}", flush=True)


if __name__ == "__main__":
    main()
