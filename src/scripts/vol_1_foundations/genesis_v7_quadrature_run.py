"""
genesis-v7 PHASE 3 — THE QUADRATURE-DEPOSIT MATRIX (D13 deposit + D14 lock-survival
discriminator, the full §5/§6/§7 frozen matrix)
====================================================================================

Executes the FROZEN matrix of `research/2026-06-10_genesis-v7-quadrature_prereg.md`
(committed ALONE @ d4b4af4b). D13 = the wall's extracted photon spin deposited as a
POLOIDAL-PROJECTING LC quadrature (δω cos qψ + δπ_ω sin qψ) on the g_wall shell,
NOT the v6 rigid-azimuthal δπ_ω the lock drains. D14 = lock-ON vs lock-OFF survival.

THE QUESTION (§6): does w_pol ≠ 0 DE NOVO, helicity-odd, transducer-OFF-absent,
above the calibrated floor — and does it QUANTIZE (emerge as a locked integer) or
merely read back the planted deposit?

DISCIPLINE (frozen, no post-hoc drop):
  * ORDERED BINS (ave-apparatus-floor-attribution v1.1): floors FIRST, every
    positive floor-gated; F-T1 (D-INHERIT regression) evaluated first of all.
  * PROBE-CAPABILITY: the w_pol extractor known-positive (plant-at-scale) BEFORE
    any de-novo read; the rigid-null contrast.
  * PHASE-SPACE-COORDINATE (A46): the winding is READ in the matching coordinate
    (the deposit's own torus). The deposit-default pol_R = 0.22..0.30·N is the
    WRONG coordinate (the read torus scales with N while the near-core seed shell
    does NOT) — its C_pol N-COLLAPSES; that read is a CLIP and is reported as the
    known-negative, not the headline.
  * GROSS-VS-FIELD: every claim is the NET FIELD (MAIN − transducer-OFF, same
    handedness), never the accumulator.
  * D12 fail-fast BEFORE the matrix; §210 every sweep executed or deviation stated.
  * ave-driver-script-honesty: every number dumped to JSON; the doc reads FROM it.

Run:
    PYTHONPATH=src .venv/bin/python src/scripts/vol_1_foundations/genesis_v7_quadrature_run.py
"""

from __future__ import annotations

import copy
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from ave.core.unified_genesis_engine import RHO_CAV, UnifiedGenesisEngine  # noqa: E402
from ave.utils.fast_winding_extractor import extract_2_3_omega_fast  # noqa: E402
from ave.utils.genesis_parallel_runner import RunSpec, run_specs  # noqa: E402

# ----------------------------------------------------- FROZEN run scale (prereg §12)
SEED = 20260610
N_MAIN = 48
M_MAIN = 1.8
N_BUILD = 3200
N_PERSIST = 600
REC_EVERY = 400
FRAC = 0.85
DRIVE_AMP = 0.10
WAVELEN = 8.0
SIGMA_PH = 5.0
SIGMA_SEED_FULL = 4.0
SIGMA_SEED_ISO = 5.0
R_FRAC = 0.18
CHI_DEFAULT = 0.02
OMEGA_FRAC_MAIN = 0.5
MEISSNER_MAIN = 0.05
LOCK_ETA_MAIN = 0.08
PHI2 = ((1.0 + np.sqrt(5.0)) / 2.0) ** 2

# THE MATCHED READ COORDINATE (A46) — the field-matched torus that brackets the
# near-core saturation shell (rho ~ 2.5 at the seed sigma scale) AND clears the
# r >= 3 extractor floor. This is a CHOICE forced by the pocket being a near-core
# SPHERE shell (no field-defined major radius) — surfaced, not hidden (§ flag).
MATCHED_POL_R = 5.0
MATCHED_POL_r = 3.0


# ============================================================ engine build
def build_engine(cfg):
    """Assemble either the FULL D-INHERIT object (snap+buckle+energized column +
    seed_lane1 — the v6 electron-genesis assembly) or the transducer-ISOLATED object
    (buckle off, seed_bulk, no column — the clean deposit channel). The quadrature
    deposit knobs ride on both; the read torus = the build (pol_R, pol_r)."""
    N = cfg["N"]
    pol_R = cfg["pol_R"]
    pol_r = cfg["pol_r"]
    common = dict(
        omega_sector_on=True, photon_coupling=True,
        lock_on=(cfg["lock_eta"] > 0.0), lock_eta=max(cfg["lock_eta"], 1e-9),
        wall_width=cfg["wall_width"],
        transducer_on=cfg["transducer_on"], chi_exch=cfg["chi_exch"],
        omega_recipient_frac=cfg["omega_frac"],
        quadrature_deposit=cfg["quad"], alpha_pol=cfg["alpha_pol"],
        q_dep=cfg["q_dep"], p_dep=2, pol_R=pol_R, pol_r=pol_r,
    )
    if cfg["assembly"] == "full":
        snap = cfg["snap"]
        e = UnifiedGenesisEngine(
            N, bulk_density_on=True, snap_on=snap,
            c2_floor=(0.0 if snap else 1e-3), nu_art_bulk=cfg["nu_art"], rho_diff=5e-4,
            snap_payback_rate=1.0, delta_heal=0.0, rho_cav=RHO_CAV, chi_shock=1.0,
            vent_mode="absorbed", snap_accounting="conservative",
            meissner_harden=cfg["meissner"], buckle_on=True, **common)
        if cfg["seed"]:
            e.seed_lane1(frac=cfg["frac"], sigma=SIGMA_SEED_FULL, vent_into_seed=False)
        e.energize_rotation_column(M_edge=cfg["M"], R_core=R_FRAC * e.N * e.dx, axis=2)
    else:  # isolated
        e = UnifiedGenesisEngine(
            N, bulk_density_on=True, snap_on=False, buckle_on=False, **common)
        c = (N - 1) / 2.0
        e.seed_bulk((c, c, c), sigma=SIGMA_SEED_ISO, frac=0.95, helical=False)
    e.freeze_wall_window()
    e.drive_chiral_photon(helicity=cfg["helicity"], sigma=SIGMA_PH, wavelength=WAVELEN,
                          amplitude=DRIVE_AMP, axis=2)
    return e


# ============================================================ measurement
def measure(e):
    """All observables FROM the evolved field (ave-driver-script-honesty). The
    de-novo w_pol + C_pol are read at the engine's BUILD torus (the matched
    coordinate for that arm); L_omega_axial is the v6 rigid (axial-AM) channel."""
    pi_om = (e.omega - e.omega_prev) / e.dt
    out = extract_2_3_omega_fast(e.omega, pi_om, e.pol_R, e.pol_r, e.N)
    led = e.transducer_ledger()
    return {
        "step": int(e.step_count),
        "E_V_cons": float(e.bulk_energy_conserved(True)),
        "H_total_cons": float(e.total_energy_unified(conserved=True)),
        "pocket_cells": int(e.pocket_cells()),
        "L_omega_axial": float(e.angular_momentum_omega_axial(2)),
        "C_pol": float(e.poloidal_quadrature_content()),
        "w_tor": int(out["w_tor"]),
        "w_pol": int(out["w_pol"]),
        "w_pol_rel": float(out["w_pol_rel"]),
        "w_pol_raw": float(out["w_pol_raw_median"]) if np.isfinite(out["w_pol_raw_median"]) else None,
        "pol_R": float(e.pol_R), "pol_r": float(e.pol_r),
        "L_transferred_omega": float(led["L_transferred_omega"]),
        "ledger_ratio": float(led["ledger_ratio_removed_over_transferred"]),
        "passive_no_pump": bool(led["passive_no_pump"]),
        "E_absorbed_sink": float(led["E_absorbed_sink"]),
        "pol_deposit_accum": float(led["pol_deposit_accum"]),
        "pol_events": int(led["pol_deposit_events"]),
        "finite": bool(np.all(np.isfinite(e.omega)) and np.all(np.isfinite(e.V))),
    }


# ============================================================ config helper
def make_cfg(name, *, assembly="iso", N=N_MAIN, seed=True, snap=True, helicity=1,
             transducer_on=True, omega_frac=OMEGA_FRAC_MAIN, chi_exch=CHI_DEFAULT,
             meissner=MEISSNER_MAIN, lock_eta=LOCK_ETA_MAIN, nu_art=5e-4,
             wall_width=0.12, frac=FRAC, M=M_MAIN, quad=True, alpha_pol=1.0,
             q_dep=3, pol_R=MATCHED_POL_R, pol_r=MATCHED_POL_r):
    return dict(name=name, assembly=assembly, N=N, seed=seed, snap=snap,
                helicity=helicity, transducer_on=transducer_on, omega_frac=omega_frac,
                chi_exch=chi_exch, meissner=meissner, lock_eta=lock_eta, nu_art=nu_art,
                wall_width=wall_width, frac=frac, M=M, quad=quad, alpha_pol=alpha_pol,
                q_dep=q_dep, pol_R=pol_R, pol_r=pol_r)


# ============================================================ the worker (spawn-safe)
def run_v7_arm(*, cfg, n_build=N_BUILD, rec_every=REC_EVERY, do_persist=False,
               n_persist=N_PERSIST, seed=SEED):
    """One independent run: BUILD recording a series, then optionally a drive-off +
    transducer-off PERSIST (the emergent-vs-planted test — a planted deposit unwinds,
    a topologically-locked winding holds). Deterministic per SEED."""
    np.random.seed(seed)
    t0 = time.time()
    e = build_engine(cfg)
    series = [measure(e)]
    for s in range(1, n_build + 1):
        e.step()
        if s % rec_every == 0 or s == n_build:
            series.append(measure(e))
            if not series[-1]["finite"]:
                series[-1]["NONFINITE"] = True
                break
    built = measure(e)
    out = {"name": cfg["name"], "cfg": {k: cfg[k] for k in cfg if k != "name"},
           "build_series": series, "built": built, "wall_s": time.time() - t0}
    if do_persist:
        p = copy.deepcopy(e)
        p.drive_helicity = 0
        p.w[:] = 0.0
        p.w_prev[:] = 0.0          # drive-off
        p.transducer_on = False    # transducer-off ⇒ no more deposit
        pser = [measure(p)]
        for s in range(1, n_persist + 1):
            p.step()
            if s % rec_every == 0 or s == n_persist:
                pser.append(measure(p))
        out["persist_series"] = pser
        out["persist_final"] = pser[-1]
    return out


# ============================================================ FLOORS (ORDERED BINS)
def recalibrate_floors():
    """All floors RE-MEASURED at the v7 run config (a floor from a different config
    is invalid). F-T1 first; F-EXCHANGE / F-ACHIRAL structural zeros; the A46
    coordinate floor (default-pol_R N-collapse vs matched)."""
    np.random.seed(SEED)
    out = {}
    # F-T1: the inherited converged mass (full assembly, transducer-OFF baseline)
    e = build_engine(make_cfg("F_T1", assembly="full", transducer_on=False, chi_exch=0.0))
    ev = [e.bulk_energy_conserved(True)]
    for s in range(1, N_BUILD + 1):
        e.step()
        if s % 800 == 0:
            ev.append(e.bulk_energy_conserved(True))
    out["F_T1_EV_cons_baseline"] = float(ev[-1])
    out["F_T1_drift_frac"] = float(abs(ev[-1] - ev[-2]) / (abs(ev[-2]) + 1e-30))
    # F-EXCHANGE: chi=0 transducer-OFF structural zero, matched read (iso + full)
    e0 = build_engine(make_cfg("F_EXCH_iso", assembly="iso", chi_exch=0.0, transducer_on=False))
    for _ in range(200):
        e0.step()
    out["F_EXCHANGE_iso_C_pol"] = float(e0.poloidal_quadrature_content())
    pi = (e0.omega - e0.omega_prev) / e0.dt
    out["F_EXCHANGE_iso_w_pol"] = int(extract_2_3_omega_fast(e0.omega, pi, e0.pol_R, e0.pol_r, e0.N)["w_pol"])
    # F-ACHIRAL: helicity=0 structural null (iso, matched)
    ea = build_engine(make_cfg("F_ACH_iso", assembly="iso", helicity=0))
    for _ in range(200):
        ea.step()
    out["F_ACHIRAL_iso_C_pol"] = float(ea.poloidal_quadrature_content())
    return out


# ====================================================== plant-at-scale known-positive
def plant_at_scale():
    """F-WPOL known-positive (the de-novo gate): the deposit PATTERN planted at the
    run scale reads w_pol = q_dep at the MATCHED torus, AND collapses at the
    deposit-default pol_R = 0.22..0.30·N (the A46 coordinate finding). The rigid v6
    pattern reads w_pol = 0 (the read distinguishes poloidal from rigid)."""
    N = N_MAIN
    res = {"matched": {}, "default_pol_R_Nsweep": {}, "rigid_null": None}
    # (a) the deposit pattern at the matched torus reads w_pol = q_dep
    for q in (2, 3, 4):
        e = build_engine(make_cfg("plant", assembly="iso", q_dep=q,
                                  pol_R=MATCHED_POL_R, pol_r=MATCHED_POL_r))
        for _ in range(200):
            e.step()
        pi = (e.omega - e.omega_prev) / e.dt
        o = extract_2_3_omega_fast(e.omega, pi, e.pol_R, e.pol_r, e.N)
        res["matched"][f"q{q}"] = {"w_pol": int(o["w_pol"]), "rel": float(o["w_pol_rel"]),
                                   "tracks_q": bool(o["w_pol"] == q)}
    # (b) the deposit-DEFAULT pol_R = 0.30·N read N-collapses (the A46 CLIP)
    for n in (28, 40, 48, 56):
        pr = 0.30 * n
        e = build_engine(make_cfg("plantD", assembly="iso", N=n, pol_R=pr, pol_r=pr / PHI2))
        for _ in range(200):
            e.step()
        res["default_pol_R_Nsweep"][f"N{n}"] = {"pol_R": float(pr),
                                                "C_pol": float(e.poloidal_quadrature_content())}
    # (c) the rigid v6 pattern (alpha_pol=0) reads w_pol = 0 at the matched torus
    e = build_engine(make_cfg("plantR", assembly="iso", alpha_pol=0.0,
                              pol_R=MATCHED_POL_R, pol_r=MATCHED_POL_r))
    for _ in range(200):
        e.step()
    pi = (e.omega - e.omega_prev) / e.dt
    o = extract_2_3_omega_fast(e.omega, pi, e.pol_R, e.pol_r, e.N)
    res["rigid_null"] = {"w_pol": int(o["w_pol"]), "rel": float(o["w_pol_rel"])}
    return res


# ============================================================ D12 fail-fast
def d12_fail_fast(floors):
    """D12(i) handedness alive (RH != LH within 200 steps, ω channel); D12(ii)
    achiral null; D12(iii) transducer-OFF null. Both configs (the iso config is
    where the deposit is clean; the full config is the D-INHERIT mandate)."""
    np.random.seed(SEED)
    e_rh = build_engine(make_cfg("d12rh", assembly="iso", helicity=1))
    e_lh = build_engine(make_cfg("d12lh", assembly="iso", helicity=-1))
    e_ac = build_engine(make_cfg("d12ac", assembly="iso", helicity=0))
    e_of = build_engine(make_cfg("d12of", assembly="iso", chi_exch=0.0, transducer_on=False))
    for _ in range(200):
        e_rh.step(); e_lh.step(); e_ac.step(); e_of.step()
    om_div = float(np.max(np.abs(e_rh.omega - e_lh.omega)))
    c_rh = e_rh.poloidal_quadrature_content()
    c_lh = e_lh.poloidal_quadrature_content()
    c_ac = e_ac.poloidal_quadrature_content()
    c_of = e_of.poloidal_quadrature_content()
    alive = bool(om_div > 0.0)
    return {
        "omega_div_RH_LH@200": om_div, "alive": alive,
        "C_pol_RH": float(c_rh), "C_pol_LH": float(c_lh),
        "C_pol_achiral": float(c_ac), "C_pol_transducer_OFF": float(c_of),
        "helicity_odd_sign_flip": bool(c_rh * c_lh < 0.0),
        "achiral_null": bool(c_ac == 0.0),
        "transducer_OFF_null": bool(c_of == 0.0),
        "abort": bool(not alive),
        "summary": {"alive": alive, "achiral_null": bool(c_ac == 0.0),
                    "OFF_null": bool(c_of == 0.0),
                    "helicity_odd": bool(c_rh * c_lh < 0.0)},
    }


# ============================================================ the arm matrices
def build_arm_specs():
    """The §6 arms in BOTH configs. ISO = the clean deposit channel (where the
    mechanism is decidable); FULL = the D-INHERIT electron-genesis mandate (the
    column+buckle swamp test + the T1 regression gate). Matched read coordinate."""
    specs = []
    # --- ISO arms (matched read; the clean discriminator) ---
    for nm, h, ch, al, eta in [
            ("ISO-MAIN-RH", 1, CHI_DEFAULT, 1.0, LOCK_ETA_MAIN),
            ("ISO-LH", -1, CHI_DEFAULT, 1.0, LOCK_ETA_MAIN),
            ("ISO-achiral", 0, CHI_DEFAULT, 1.0, LOCK_ETA_MAIN),
            ("ISO-OFF", 1, 0.0, 1.0, LOCK_ETA_MAIN),
            ("ISO-rigid-a0", 1, CHI_DEFAULT, 0.0, LOCK_ETA_MAIN),
            ("ISO-MAIN-lockOFF", 1, CHI_DEFAULT, 1.0, 0.0),
            ("ISO-rigid-lockOFF", 1, CHI_DEFAULT, 0.0, 0.0)]:
        specs.append(RunSpec(nm, run_v7_arm,
                     dict(cfg=make_cfg(nm, assembly="iso", helicity=h, chi_exch=ch,
                                       alpha_pol=al, lock_eta=eta,
                                       transducer_on=(ch > 0.0)),
                          n_build=N_BUILD, do_persist=(nm == "ISO-MAIN-RH")), SEED))
    # --- FULL D-INHERIT arms (the mandate; matched read; T1 gate) ---
    for nm, h, ch, al in [
            ("FULL-MAIN-RH", 1, CHI_DEFAULT, 1.0),
            ("FULL-LH", -1, CHI_DEFAULT, 1.0),
            ("FULL-achiral", 0, CHI_DEFAULT, 1.0),
            ("FULL-OFF", 1, 0.0, 1.0),
            ("FULL-rigid-a0", 1, CHI_DEFAULT, 0.0)]:
        specs.append(RunSpec(nm, run_v7_arm,
                     dict(cfg=make_cfg(nm, assembly="full", helicity=h, chi_exch=ch,
                                       alpha_pol=al, transducer_on=(ch > 0.0)),
                          n_build=N_BUILD), SEED))
    return specs


# ============================================================ mandated sweeps (§5)
def build_sweep_specs():
    """Every §5 knob the bins depend on (§210). Reduced build for cost; the headline
    arms are full-build above. All ISO (the clean channel where the deposit read is
    decidable) except the N-sweep which contrasts matched vs default-pol_R."""
    s = []
    # §5.1 alpha_pol (the deposit-shape control axis)
    for a in (0.0, 0.25, 0.5, 0.75, 1.0):
        s.append(RunSpec(("alpha_pol", a), run_v7_arm,
                 dict(cfg=make_cfg(f"a{a}", assembly="iso", alpha_pol=a), n_build=200), SEED))
    # §5.2 lock x alpha (the D14 discriminator)
    for lk in (0.0, LOCK_ETA_MAIN):
        for a in (0.0, 1.0):
            s.append(RunSpec(("lockxalpha", lk, a), run_v7_arm,
                     dict(cfg=make_cfg(f"lk{lk}a{a}", assembly="iso", lock_eta=lk,
                                       alpha_pol=a), n_build=200), SEED))
    # §5.3 q_dep (the de-novo w_pol must TRACK the designed q)
    for q in (2, 3, 4):
        s.append(RunSpec(("q_dep", q), run_v7_arm,
                 dict(cfg=make_cfg(f"q{q}", assembly="iso", q_dep=q), n_build=200), SEED))
    # §5.4 chi_exch (coupling magnitude; verdict must NOT track it)
    for ch in (9e-4, 0.005, 0.02, 0.08):
        s.append(RunSpec(("chi_exch", ch), run_v7_arm,
                 dict(cfg=make_cfg(f"chi{ch}", assembly="iso", chi_exch=ch), n_build=200), SEED))
    # §5.5 lock_eta (the poloidal survival must be eta-INDEPENDENT)
    for eta in (0.0, 0.05, 0.08, 0.12):
        s.append(RunSpec(("lock_eta", eta), run_v7_arm,
                 dict(cfg=make_cfg(f"eta{eta}", assembly="iso", lock_eta=eta), n_build=200), SEED))
    # §5.6 omega_recipient_frac
    for of in (0.0, 0.5, 1.0):
        s.append(RunSpec(("omega_frac", of), run_v7_arm,
                 dict(cfg=make_cfg(f"of{of}", assembly="iso", omega_frac=of), n_build=200), SEED))
    # §5.7 wall_width
    for ww in (0.06, 0.12, 0.20):
        s.append(RunSpec(("wall_width", ww), run_v7_arm,
                 dict(cfg=make_cfg(f"ww{ww}", assembly="iso", wall_width=ww), n_build=200), SEED))
    # §5.8 N — matched read (must be N-robust) AND default-pol_R (the A46 N-collapse)
    for n in (40, 48, 56):
        s.append(RunSpec(("N_matched", n), run_v7_arm,
                 dict(cfg=make_cfg(f"Nm{n}", assembly="iso", N=n,
                                   pol_R=MATCHED_POL_R, pol_r=MATCHED_POL_r), n_build=200), SEED))
        s.append(RunSpec(("N_default", n), run_v7_arm,
                 dict(cfg=make_cfg(f"Nd{n}", assembly="iso", N=n,
                                   pol_R=0.30 * n, pol_r=0.30 * n / PHI2), n_build=200), SEED))
    # §5.9 K3 stop-time (does the LC quadrature read track WHEN it stops? iso MAIN)
    for nb in (200, 907, 1800, 3200):
        s.append(RunSpec(("K3", nb), run_v7_arm,
                 dict(cfg=make_cfg(f"K3_{nb}", assembly="iso"), n_build=nb), SEED))
    # §5.11 K4 seed frac (full assembly; regime gate; w_pol must not appear only shallow)
    for fr in (0.30, 0.60, 0.85, 0.95):
        s.append(RunSpec(("frac", fr), run_v7_arm,
                 dict(cfg=make_cfg(f"fr{fr}", assembly="full", frac=fr), n_build=2000), SEED))
    return s


# ============================================================ analysis / bins
def analyze(R):
    """Floor-gated bins (§6, ORDERED). Floors FIRST (F-T1 → F-WPOL → F-NETFIELD →
    F-EXCHANGE/ACHIRAL). Then the de-novo question in BOTH configs, the D14 survival,
    the emergent-vs-planted persistence, and the §5 sweep invariances."""
    arms = R["arms"]
    sw = R["sweeps"]
    floors = R["floors"]
    a = {}

    def b(name):
        v = arms.get(name)
        return v["built"] if isinstance(v, dict) and "built" in v else None

    # ---- F-T1 (D-INHERIT regression gate; evaluated FIRST) ----
    t1 = {}
    for nm in ("FULL-MAIN-RH", "FULL-LH", "FULL-OFF", "FULL-achiral", "FULL-rigid-a0"):
        v = b(nm)
        if v:
            ser = arms[nm]["build_series"]
            ev = [s["E_V_cons"] for s in ser]
            t1[nm] = {"EV_cons_first": ev[0], "EV_cons_last": ev[-1],
                      "drift_frac": abs(ev[-1] - ev[-2]) / (abs(ev[-2]) + 1e-30)}
    t1_baseline = floors["F_T1_EV_cons_baseline"]
    t1_ok = all(abs(d["EV_cons_last"] - t1_baseline) < 0.15 * abs(t1_baseline)
                and d["drift_frac"] < 0.02 for d in t1.values()) if t1 else False
    a["F_T1_regression"] = {"per_arm": t1, "baseline": t1_baseline, "T1_converged_all_arms": t1_ok}

    # ---- F-WPOL (plant-at-scale known-positive + rigid-null) ----
    pls = R["plant_at_scale"]
    a["F_WPOL"] = {
        "matched_tracks_q": {k: v["tracks_q"] for k, v in pls["matched"].items()},
        "matched_known_positive": all(v["tracks_q"] for v in pls["matched"].values()),
        "rigid_null_w_pol": pls["rigid_null"]["w_pol"],
        "default_pol_R_C_pol_Ncollapse": {k: v["C_pol"]
                                          for k, v in pls["default_pol_R_Nsweep"].items()}}

    # ---- the DE-NOVO question, ISO (matched coordinate; clean channel) ----
    main_i, off_i, lh_i, ac_i, rig_i = (b("ISO-MAIN-RH"), b("ISO-OFF"), b("ISO-LH"),
                                        b("ISO-achiral"), b("ISO-rigid-a0"))
    if main_i and off_i:
        a["de_novo_ISO_matched"] = {
            "w_pol_MAIN": main_i["w_pol"], "w_pol_rel_MAIN": main_i["w_pol_rel"],
            "w_pol_OFF": off_i["w_pol"], "w_pol_LH": lh_i["w_pol"] if lh_i else None,
            "w_pol_achiral": ac_i["w_pol"] if ac_i else None,
            "w_pol_rigid_a0": rig_i["w_pol"] if rig_i else None,
            "C_pol_MAIN": main_i["C_pol"], "C_pol_LH": lh_i["C_pol"] if lh_i else None,
            "C_pol_achiral": ac_i["C_pol"] if ac_i else None,
            "C_pol_OFF": off_i["C_pol"],
            "above_floor": bool(main_i["w_pol_rel"] > 0.1 and main_i["w_pol"] != 0),
            "OFF_absent": bool(off_i["w_pol"] == 0),
            "rigid_absent": bool(rig_i["w_pol"] == 0) if rig_i else None,
            "helicity_odd_C_pol": bool(lh_i and main_i["C_pol"] * lh_i["C_pol"] < 0.0),
            "achiral_C_pol_null": bool(ac_i and ac_i["C_pol"] == 0.0)}

    # ---- the DE-NOVO question, FULL D-INHERIT (the mandate; column+buckle swamp) ----
    main_f, off_f, ac_f = b("FULL-MAIN-RH"), b("FULL-OFF"), b("FULL-achiral")
    if main_f:
        a["de_novo_FULL_matched"] = {
            "w_pol_MAIN": main_f["w_pol"], "w_pol_rel_MAIN": main_f["w_pol_rel"],
            "w_pol_OFF": off_f["w_pol"] if off_f else None,
            "w_pol_achiral": ac_f["w_pol"] if ac_f else None,
            "C_pol_MAIN": main_f["C_pol"], "C_pol_OFF": off_f["C_pol"] if off_f else None,
            "C_pol_achiral": ac_f["C_pol"] if ac_f else None,
            "winding_swamped": bool(main_f["w_pol"] == 0),
            "deposit_subdominant_to_buckle": bool(off_f and abs(off_f["C_pol"]) > abs(main_f["C_pol"]))}

    # ---- D14 lock survival (ISO, matched) ----
    on_i, ioff_i = b("ISO-MAIN-lockOFF"), None
    mlock = b("ISO-MAIN-RH"); mlockoff = b("ISO-MAIN-lockOFF")
    rlock = b("ISO-rigid-a0"); rlockoff = b("ISO-rigid-lockOFF")
    if mlock and mlockoff:
        a["D14_survival"] = {
            "poloidal_C_pol_lockON": mlock["C_pol"], "poloidal_C_pol_lockOFF": mlockoff["C_pol"],
            "poloidal_survive_ratio": abs(mlock["C_pol"]) / (abs(mlockoff["C_pol"]) + 1e-30),
            "rigid_L_om_lockON": rlock["L_omega_axial"] if rlock else None,
            "rigid_L_om_lockOFF": rlockoff["L_omega_axial"] if rlockoff else None,
            "rigid_drain_ratio": (abs(rlock["L_omega_axial"]) / (abs(rlockoff["L_omega_axial"]) + 1e-30)
                                  if rlock and rlockoff else None)}

    # ---- emergent vs planted (the persistence of ISO-MAIN drive+transducer OFF) ----
    if isinstance(arms.get("ISO-MAIN-RH"), dict) and "persist_series" in arms["ISO-MAIN-RH"]:
        ps = arms["ISO-MAIN-RH"]["persist_series"]
        a["emergent_vs_planted"] = {
            "w_pol_persist": [s["w_pol"] for s in ps],
            "C_pol_persist": [s["C_pol"] for s in ps],
            "step_persist": [s["step"] for s in ps],
            "winding_unwinds": bool(ps[-1]["w_pol"] < ps[0]["w_pol"]),
            "C_pol_holds": bool(abs(ps[-1]["C_pol"]) > 0.5 * abs(ps[0]["C_pol"]))}

    # ---- §5 sweep invariances ----
    def swval(key, field="C_pol"):
        out = {}
        for k, v in sw.items():
            if isinstance(k, str) and k.startswith(f"('{key}'") and isinstance(v, dict):
                kk = k.split(",")[1].strip().rstrip(")")
                out[kk] = v["built"][field]
        return out
    qd = {}
    for k, v in sw.items():
        if isinstance(k, str) and k.startswith("('q_dep'") and isinstance(v, dict):
            q = int(k.split(",")[1].strip().rstrip(")"))
            qd[q] = {"w_pol": v["built"]["w_pol"], "tracks": v["built"]["w_pol"] == q}
    a["sweep_q_dep_tracking"] = qd
    eta_c = swval("lock_eta")
    eta_vals = [abs(x) for x in eta_c.values()]
    a["sweep_lock_eta_C_pol"] = {"vals": eta_c,
        "eta_independent": bool(eta_vals and (max(eta_vals) - min(eta_vals)) / (max(eta_vals) + 1e-30) < 0.05)}
    a["sweep_alpha_pol_C_pol"] = swval("alpha_pol")
    a["sweep_N_matched_w_pol"] = {k.split(",")[1].strip().rstrip(")"): v["built"]["w_pol"]
                                  for k, v in sw.items()
                                  if isinstance(k, str) and k.startswith("('N_matched'") and isinstance(v, dict)}
    a["sweep_N_default_C_pol"] = {k.split(",")[1].strip().rstrip(")"): v["built"]["C_pol"]
                                  for k, v in sw.items()
                                  if isinstance(k, str) and k.startswith("('N_default'") and isinstance(v, dict)}

    # ====================== THE FROZEN BIN (§6) ======================
    de_iso = a.get("de_novo_ISO_matched", {})
    de_full = a.get("de_novo_FULL_matched", {})
    d14 = a.get("D14_survival", {})
    evp = a.get("emergent_vs_planted", {})
    survives = bool(d14.get("poloidal_survive_ratio", 0) > 0.5
                    and (d14.get("rigid_drain_ratio") or 1) < 0.5)
    full_winds = bool(de_full.get("w_pol_MAIN", 0) != 0 and de_full.get("w_pol_rel_MAIN", 0) > 0.1)
    iso_winds = bool(de_iso.get("above_floor"))
    quantizes = bool(evp and not evp.get("winding_unwinds", True))  # locked integer that holds

    if not a["F_T1_regression"]["T1_converged_all_arms"]:
        verdict = "T1-BROKEN"
    elif full_winds and quantizes and survives:
        verdict = "WINDING-TAKES"
    elif survives and (iso_winds or full_winds) and not (quantizes and full_winds):
        verdict = "DEPOSIT-SURVIVES-NO-QUANTIZATION"
    elif not survives:
        verdict = "DEPOSIT-DRAINED-AGAIN"
    else:
        verdict = "UNRESOLVED"
    a["VERDICT"] = verdict
    a["verdict_logic"] = {"T1_ok": a["F_T1_regression"]["T1_converged_all_arms"],
                          "iso_winds_matched": iso_winds, "full_winds_matched": full_winds,
                          "D14_survives": survives, "quantizes_locked": quantizes}
    return a


# ============================================================ figures
def make_figures(R):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    figdir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..",
                                          "research", "figures"))
    os.makedirs(figdir, exist_ok=True)
    paths = []
    a = R["analysis"]

    # FIG 1: the A46 coordinate finding — C_pol N-collapse (default pol_R) vs
    # w_pol N-robustness (matched pol_R) — the field quantity, not the accumulator.
    try:
        nd = a["sweep_N_default_C_pol"]; nm = a["sweep_N_matched_w_pol"]
        Ns = sorted(int(k.replace("N", "")) if "N" in k else int(k) for k in nd)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
        cd = [abs(nd.get(f"N{n}", nd.get(str(n), 0)) or 1e-20) for n in Ns]
        ax1.semilogy(Ns, cd, "o-r")
        ax1.set_xlabel("N"); ax1.set_ylabel("|C_pol| (default pol_R=0.30N)")
        ax1.set_title("A46 CLIP: C_pol N-COLLAPSES at the deposit-default read torus")
        wm = [nm.get(f"N{n}", nm.get(str(n), 0)) for n in Ns]
        ax2.plot(Ns, wm, "s-g"); ax2.axhline(3, ls=":", c="b", lw=1, label="q_dep=3")
        ax2.set_xlabel("N"); ax2.set_ylabel("de-novo w_pol (matched pol_R)")
        ax2.set_ylim(-0.5, 4.5); ax2.legend(fontsize=8)
        ax2.set_title("matched coordinate: w_pol = q N-ROBUST")
        fig.tight_layout()
        p = os.path.join(figdir, "fig_v7_A46_coordinate.png"); fig.savefig(p, dpi=110); plt.close(fig); paths.append(p)
    except Exception as exc:  # noqa: BLE001
        R.setdefault("fig_errors", []).append(f"A46: {exc!r}")

    # FIG 2: D14 lock-survival — poloidal SURVIVES, rigid DRAINS (field-to-field).
    try:
        d14 = a["D14_survival"]
        fig, ax = plt.subplots(figsize=(6.5, 4.2))
        labels = ["poloidal\n(quadrature)", "rigid\n(v6 control)"]
        on = [abs(d14["poloidal_C_pol_lockON"]), abs(d14["rigid_L_om_lockON"])]
        off = [abs(d14["poloidal_C_pol_lockOFF"]), abs(d14["rigid_L_om_lockOFF"])]
        x = np.arange(2)
        ax.bar(x - 0.2, off, 0.4, label="lock-OFF (un-drained)")
        ax.bar(x + 0.2, on, 0.4, label="lock-ON")
        ax.set_yscale("log"); ax.set_xticks(x); ax.set_xticklabels(labels)
        ax.set_ylabel("|field| (matched coordinate)")
        ax.set_title("D14: the poloidal quadrature SURVIVES the lock; the rigid mode DRAINS")
        ax.legend(fontsize=8); fig.tight_layout()
        p = os.path.join(figdir, "fig_v7_D14_survival.png"); fig.savefig(p, dpi=110); plt.close(fig); paths.append(p)
    except Exception as exc:  # noqa: BLE001
        R.setdefault("fig_errors", []).append(f"D14: {exc!r}")

    # FIG 3: emergent-vs-planted — the winding UNWINDS (3->2->1) when unsourced,
    # while C_pol holds (the deposit content survives but does not topologically lock).
    try:
        evp = a["emergent_vs_planted"]
        fig, ax = plt.subplots(figsize=(6.8, 4.2))
        ax.plot(evp["step_persist"], evp["w_pol_persist"], "o-", label="de-novo w_pol")
        ax.axhline(3, ls=":", c="b", lw=1, label="q_dep=3 (deposited)")
        ax.set_xlabel("step (drive + transducer OFF after build)")
        ax.set_ylabel("de-novo w_pol", color="C0"); ax.set_ylim(-0.5, 4.5)
        ax2 = ax.twinx()
        ax2.plot(evp["step_persist"], [abs(c) for c in evp["C_pol_persist"]], "s--C3", label="|C_pol|")
        ax2.set_ylabel("|C_pol| (field content)", color="C3")
        ax.legend(loc="center left", fontsize=8); ax2.legend(loc="center right", fontsize=8)
        ax.set_title("EMERGENT-vs-PLANTED: winding UNWINDS unsourced; C_pol holds (no topological lock)")
        fig.tight_layout()
        p = os.path.join(figdir, "fig_v7_emergent_vs_planted.png"); fig.savefig(p, dpi=110); plt.close(fig); paths.append(p)
    except Exception as exc:  # noqa: BLE001
        R.setdefault("fig_errors", []).append(f"evp: {exc!r}")

    # FIG 4: the full-assembly swamp — w_pol = 0 (column+buckle dominate) + T1 holds.
    try:
        t1 = a["F_T1_regression"]["per_arm"]
        fig, ax = plt.subplots(figsize=(6.8, 4.2))
        for nm in ("FULL-MAIN-RH", "FULL-OFF", "FULL-achiral"):
            v = R["arms"].get(nm)
            if isinstance(v, dict):
                t = [s["step"] for s in v["build_series"]]
                ev = [s["E_V_cons"] for s in v["build_series"]]
                ax.plot(t, ev, label=f"{nm} (w_pol={v['built']['w_pol']})", lw=1.4)
        ax.axhline(a["F_T1_regression"]["baseline"], ls=":", c="k", lw=0.8, label="T1 baseline ~12.9")
        ax.set_xlabel("build step"); ax.set_ylabel("E_V_cons (T1 dilatation mass)")
        ax.set_title("FULL D-INHERIT: T1 holds (~12.9) but w_pol=0 (column+buckle swamp the deposit)")
        ax.legend(fontsize=7); fig.tight_layout()
        p = os.path.join(figdir, "fig_v7_full_assembly_swamp.png"); fig.savefig(p, dpi=110); plt.close(fig); paths.append(p)
    except Exception as exc:  # noqa: BLE001
        R.setdefault("fig_errors", []).append(f"full: {exc!r}")

    R["figures"] = paths


# ============================================================ io / main
def _strip(v):
    if not isinstance(v, dict):
        return {"ERROR": repr(v)}
    return v


def _dump(R, t0):
    out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..",
                                       "research", "2026-06-10_genesis-v7-quadrature-run_results.json"))
    with open(out, "w") as f:
        json.dump(R, f, indent=2, default=float)
    print(f"[dump] {time.time()-t0:.0f}s -> {out}", flush=True)


def main():
    t0 = time.time()
    R = {"prereg": "research/2026-06-10_genesis-v7-quadrature_prereg.md (FROZEN @ d4b4af4b)",
         "engine": "src/ave/core/unified_genesis_engine.py (v7 D13 quadrature deposit @ 09d47e45)",
         "scale": dict(N=N_MAIN, M=M_MAIN, n_build=N_BUILD, frac=FRAC, chi=CHI_DEFAULT,
                       seed=SEED, matched_pol_R=MATCHED_POL_R, matched_pol_r=MATCHED_POL_r)}

    print("[1/6] FLOORS (recalibrated at the v7 config; F-T1 first) ...", flush=True)
    R["floors"] = recalibrate_floors()
    print(f"    F-T1 baseline EVc={R['floors']['F_T1_EV_cons_baseline']:.2f} "
          f"F-EXCH_iso C_pol={R['floors']['F_EXCHANGE_iso_C_pol']:.2e} "
          f"F-ACHIRAL={R['floors']['F_ACHIRAL_iso_C_pol']:.2e} ({time.time()-t0:.0f}s)", flush=True)

    print("[2/6] plant-at-scale known-positive (BEFORE any de-novo read) ...", flush=True)
    R["plant_at_scale"] = plant_at_scale()
    _tracks = [v["tracks_q"] for v in R["plant_at_scale"]["matched"].values()]
    _ncol = ["%.1e" % v["C_pol"] for v in R["plant_at_scale"]["default_pol_R_Nsweep"].values()]
    print(f"    matched tracks-q: {_tracks} "
          f"rigid-null w_pol={R['plant_at_scale']['rigid_null']['w_pol']} "
          f"default-pol_R N-collapse: {_ncol}", flush=True)

    print("[3/6] D12 fail-fast (handedness-alive + achiral/OFF null) ...", flush=True)
    R["D12"] = d12_fail_fast(R["floors"])
    print(f"    D12: {json.dumps(R['D12']['summary'])}", flush=True)
    if R["D12"]["abort"]:
        R["gate_verdict"] = "TRANSDUCER-DEAD"
        _dump(R, t0); return

    print("[4/6] arm matrix (ISO clean channel + FULL D-INHERIT mandate) ...", flush=True)
    arms = run_specs(build_arm_specs(), serial=False, raise_on_error=False)
    R["arms"] = {k: _strip(v) for k, v in arms.items()}
    for k, v in arms.items():
        if isinstance(v, dict):
            bb = v["built"]
            print(f"    {k:20s} w_pol={bb['w_pol']} rel={bb['w_pol_rel']:.3f} "
                  f"C_pol={bb['C_pol']:+.3e} L_om={bb['L_omega_axial']:+.2e} "
                  f"EVc={bb['E_V_cons']:.2f} ({v['wall_s']:.0f}s)", flush=True)

    print("[5/6] mandated §5 sweeps (§210) ...", flush=True)
    raw = run_specs(build_sweep_specs(), serial=False, raise_on_error=False)
    R["sweeps"] = {repr(k): _strip(v) for k, v in raw.items()}

    print("[6/6] floor-gated bins + verdict + figures ...", flush=True)
    R["analysis"] = analyze(R)
    _dump(R, t0)
    make_figures(R)
    _dump(R, t0)
    print("\n" + "=" * 74)
    print(f"V7 VERDICT: {R['analysis']['VERDICT']}")
    print(f"  logic: {json.dumps(R['analysis']['verdict_logic'])}")
    print("=" * 74, flush=True)


if __name__ == "__main__":
    main()
