"""
THE SCREENED-WINDING PROBE — PHASE 2 driver
====================================================================================
Executes research/2026-06-11_screened-winding-probe_prereg.md (FROZEN @ dbb67e72,
committed ALONE). Re-scopes the v6 `w_pol≡0` verdict: is the absence a genuine
absence or an APPARATUS SCREEN?

THE APPARATUS CONFESSION (verified, exact cites @ 7484dd0b):
  unified_genesis_engine.py:396  self.u_adv[cm] = 0.0     (cm = snap_mask, :385)
  unified_genesis_engine.py:344  self.u_adv[newly] *= (1.0 - chi_shock)
  unified_genesis_engine.py:393  self.rho_bar[cm] = self.snap_clamp_val[cm]  (conservative)
  unified_genesis_engine.py:395  self.rho_bar[cm] = self.rho_cav             (legacy)
The snap zeroes u_adv + clamps rho_bar in snapped cells EVERY step. It NEVER writes
omega / pi_omega / w / V (grep _tally_latent_and_snap/_snap_step lines 304-419 ->
ZERO writes). The (2,3) the extractor reads is the Cosserat omega — PRESERVED.
The parent CrystalGraftV4.step() (unified_genesis_engine.py:852 super().step())
evolves omega/V/w UNCHANGED.

THREE ARMS, every §3 gate an assert/branch; every §5 sweep executed; all numbers
FROM the evolved field (ave-driver-script-honesty). Floors-first ORDERED BINS.

Run:
  PYTHONPATH=src .venv/bin/python src/scripts/vol_1_foundations/screened_winding_probe_run.py
"""
from __future__ import annotations

import importlib.util
import json
import os
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from ave.core.unified_genesis_engine import RHO_CAV, UnifiedGenesisEngine  # noqa: E402
from ave.utils.fast_winding_extractor import (  # noqa: E402
    extract_2_3_omega_fast, verify_equivalence,
)

np.seterr(all="ignore")
PHI2 = ((1.0 + np.sqrt(5.0)) / 2.0) ** 2

# ----------------------------------------------------- FROZEN scale (engineering choice §5)
SEED = 20260611
N_PROBE = 32          # MODEST scale (declared engineering choice; bins/thresholds unchanged)
N_FORM = 1300         # build steps to form the snapped shell at M_nominal
N_SETTLE = 80         # post-plant evolution for the indirect-screening read
PLANT_AMP = 0.40

# shell-thickness sweep (via the snap recipe drive amplitude M_edge) — §5.
# MONOTONIC LOCALIZED annuli (n_snap 144<184<328, radial thickness 0<1.0<2.7);
# M=3.0/3.8 are AVOIDED — they detonate (the cascade engulfs the whole interior,
# not a shell). Declared engineering choice §5/§210; FROZEN bins/thresholds unchanged.
M_THIN, M_NOM, M_THICK = 2.6, 2.8, 3.4

# §5 contour-radius sweep (the contour's radial/major position, as a fraction of R_shell)
R_GRID = [0.5, 0.7, 0.9, 1.0, 1.15, 1.3, 1.6]
# §5 phase-count sweep
N_PHASE_GRID = [1, 4, 8, 16]
# §5 omega_recipient_frac sweep (the read-channel coverage)
OMEGA_FRAC_GRID = [0.0, 0.5, 1.0]

# ----------------------------------------------------- FROZEN thresholds (§4.0)
REL_MIN = 0.10        # extractor reliability gate (fast_winding_extractor.py:50,:198)
SCREEN_MAX = 0.30     # transfer at/below which a read counts SUPPRESSED
PASS_MIN = 0.70       # transfer at/above which a read counts TRANSMITTED
ENV_DELTA = 0.10      # min phase-vs-average rel excursion to call ENVELOPE-STRUCTURE


# ============================================================ engine build (v6 snap recipe)
def build_engine(M, *, snap=True, transducer=False, omega_frac=0.0):
    e = UnifiedGenesisEngine(
        N_PROBE, bulk_density_on=True, snap_on=snap,
        c2_floor=(0.0 if snap else 1e-3), nu_art_bulk=5e-4, rho_diff=5e-4,
        snap_payback_rate=1.0, delta_heal=0.0, rho_cav=RHO_CAV, chi_shock=1.0,
        vent_mode="absorbed", snap_accounting="conservative", meissner_harden=0.05,
        omega_sector_on=True, buckle_on=True, photon_coupling=True, lock_on=True,
        lock_eta=0.08, wall_width=0.12, transducer_on=transducer, chi_exch=0.02,
        omega_recipient_frac=omega_frac)
    e.seed_lane1(frac=0.85, sigma=4.0, vent_into_seed=False)
    e.energize_rotation_column(M_edge=M, R_core=0.18 * e.N * e.dx, axis=2)
    e.freeze_wall_window()
    e.drive_chiral_photon(helicity=1, sigma=5.0, wavelength=8.0, amplitude=0.10, axis=2)
    return e


def _cyl(e):
    c = (e.N - 1) / 2.0
    i, j, k = np.indices((e.N, e.N, e.N))
    rho = np.sqrt((i - c) ** 2 + (j - c) ** 2)
    z = k - c
    return rho, z


def locate_shell(e):
    """CP7: shell = median cylindrical radius of snapped interior cells (NOT centroid)."""
    sm = e.snap_mask & e.interior_mask()
    n = int(sm.sum())
    if n == 0:
        return None, 0, (None, None)
    rho, _ = _cyl(e)
    rr = rho[sm]
    return float(np.median(rr)), n, (float(rr.min()), float(rr.max()))


def read_winding(e, R, r_tube):
    pio = (e.omega - e.omega_prev) / e.dt
    return extract_2_3_omega_fast(e.omega, pio, R, r_tube, e.N)


def omega_median_annulus(e, lo_frac, hi_frac, R_shell):
    rho, _ = _cyl(e)
    ann = (rho > lo_frac * R_shell) & (rho < hi_frac * R_shell) & e.interior_mask()
    if ann.sum() == 0:
        return 0.0
    return float(np.median(np.linalg.norm(e.omega[ann], axis=-1)))


# ============================================================ KEEPER (probe-capability)
def keeper():
    """fast_winding_extractor.verify_equivalence vs the ORIGINAL graft-v2 reader:
    (2,3) on a plant, (0,0) on a null, <=1e-12 vs reference. Probe-capability FLOOR 0."""
    drv = (Path(__file__).resolve().parents[2] / "scripts" / "vol_1_foundations"
           / "crystal_graft_v2_run.py")
    spec = importlib.util.spec_from_file_location("crystal_graft_v2_run", drv)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    try:
        report = verify_equivalence(mod.extract_2_3_omega, N=52, verbose=False)
        planted_ok = bool(report["planted_2_3"]["is_2_3"]) and report["planted_2_3"]["w_pol"] == 3
        null_ok = (not report["null"]["is_2_3"]) and report["null"]["w_pol"] == 0
        passes = bool(planted_ok and null_ok)
    except AssertionError as exc:
        return {"passes": False, "error": str(exc)}
    return {"passes": passes, "planted_is_2_3": report["planted_2_3"]["is_2_3"],
            "null_is_2_3": report["null"]["is_2_3"],
            "max_abs_diff_planted": report["planted_2_3"]["max_abs_diff"]}


# ============================================================ ARM 1 (screening calibration)
def arm1_one_thickness(M, tag):
    """Form a shell (snap ON) + a byte-paired control (snap OFF), plant the SAME
    validated (2,3) co-located at R_shell (ATTEMPT-A: plant AFTER forming -> the snap
    never writes omega so the plant SURVIVES), read snap-ON vs snap-OFF across the
    §5 contour-radius sweep. The transfer T(r)=read_on/read_off IS the screening
    transfer function of the apparatus."""
    np.random.seed(SEED)
    es = build_engine(M, snap=True)
    np.random.seed(SEED)
    ec = build_engine(M, snap=False)
    for _ in range(N_FORM):
        es.step(); ec.step()
    R_shell, n_snap, (rmin, rmax) = locate_shell(es)
    if R_shell is None:
        return {"tag": tag, "M": M, "shell_formed": False}
    r_tube = R_shell / PHI2

    # --- DECOUPLE PROOF (the §1 inventory at the array level) ---
    m = es.interior_mask()
    sm = es.snap_mask & m
    d_omega = float(np.max(np.abs((es.omega - ec.omega)[m]))) if m.any() else float("nan")
    d_w = float(np.max(np.abs((es.w - ec.w)[m])))
    d_V = float(np.max(np.abs((es.V - ec.V)[m])))
    both_finite = m & np.isfinite(es.rho_bar) & np.isfinite(ec.rho_bar)
    d_rho_finite = float(np.max(np.abs((es.rho_bar - ec.rho_bar)[both_finite]))) if both_finite.any() else 0.0
    ctrl_bulk_nonfinite = int(np.count_nonzero(~np.isfinite(ec.rho_bar) & m))
    # within ONE engine: snapped cells have u_adv zeroed (:396) but omega preserved
    u_in_snapped = float(np.median(np.linalg.norm(es.u_adv[sm], axis=-1))) if sm.any() else 0.0
    omega_in_snapped = float(np.median(np.linalg.norm(es.omega[sm], axis=-1))) if sm.any() else 0.0

    # --- plant the SAME (2,3) into BOTH (ATTEMPT-A) ---
    es.seed_omega_known_2_3(R=R_shell, r=r_tube, amplitude=PLANT_AMP, p=2, q=3)
    ec.seed_omega_known_2_3(R=R_shell, r=r_tube, amplitude=PLANT_AMP, p=2, q=3)

    def sweep(label):
        rows = []
        for frac in R_GRID:
            R = frac * R_shell
            ron = read_winding(es, R, r_tube)
            roff = read_winding(ec, R, r_tube)
            T = ron["w_pol_rel"] / (roff["w_pol_rel"] + 1e-30)
            rows.append({
                "frac": frac, "R": R,
                "off_w_pol": int(roff["w_pol"]), "off_w_tor": int(roff["w_tor"]),
                "off_w_pol_rel": float(roff["w_pol_rel"]), "off_is_2_3": bool(roff["is_2_3"]),
                "on_w_pol": int(ron["w_pol"]), "on_w_tor": int(ron["w_tor"]),
                "on_w_pol_rel": float(ron["w_pol_rel"]), "on_is_2_3": bool(ron["is_2_3"]),
                "T": float(T),
                "byte_identical": bool(abs(ron["w_pol_rel"] - roff["w_pol_rel"]) < 1e-12
                                       and ron["w_pol"] == roff["w_pol"]),
            })
        return rows

    sweep_t0 = sweep("t0")
    for _ in range(N_SETTLE):
        es.step(); ec.step()
    sweep_settled = sweep("settled")

    return {
        "tag": tag, "M": M, "shell_formed": True, "R_shell": R_shell,
        "n_snap": n_snap, "shell_rho_min": rmin, "shell_rho_max": rmax,
        "r_tube": r_tube,
        "decouple": {
            "max_d_omega_on_minus_off": d_omega,   # read channel: expect 0.0
            "max_d_w_on_minus_off": d_w,           # photon: expect 0.0
            "max_d_V_on_minus_off": d_V,           # longitudinal: expect 0.0
            "max_d_rho_bar_finite": d_rho_finite,  # bulk: expect >0 (snap clamps)
            "ctrl_bulk_nonfinite_cells": ctrl_bulk_nonfinite,
            "u_median_in_snapped_cells": u_in_snapped,        # expect ~0 (:396 zeroed)
            "omega_median_in_snapped_cells": omega_in_snapped,  # expect >0 (preserved)
        },
        "sweep_t0": sweep_t0, "sweep_settled": sweep_settled,
    }


def arm1():
    out = {}
    for tag, M in (("thin", M_THIN), ("nominal", M_NOM), ("thick", M_THICK)):
        t = time.time()
        out[tag] = arm1_one_thickness(M, tag)
        nf = out[tag].get("n_snap")
        print(f"    ARM1[{tag:7s}] M={M} R_shell={out[tag].get('R_shell')} "
              f"n_snap={nf} ({time.time()-t:.0f}s)", flush=True)
    return out


def arm1_gates(arm1_out):
    """G-CAL / G-IN / G-OUT-S / G-OUT-T from the NOMINAL-thickness t0 sweep.
    read_c = OFF control at the natural read radius (best is_2_3 OFF read).
    read_b = ON inside radius (largest frac<1.0 with OFF is_2_3, else 0.9).
    read_a = ON outside radius (smallest frac>1.0 with OFF is_2_3, else 1.15)."""
    nom = arm1_out["nominal"]
    if not nom.get("shell_formed"):
        return {"G_CAL": False, "reason": "shell did not form", "ARM1": "UNRESOLVED"}
    rows = nom["sweep_t0"]
    by_frac = {row["frac"]: row for row in rows}

    # read_c: the natural-radius control read = OFF read at frac=1.0
    c_row = by_frac[1.0]
    read_c_rel = c_row["off_w_pol_rel"]
    read_c_is23 = c_row["off_is_2_3"]
    G_CAL = bool(read_c_is23 and read_c_rel >= REL_MIN)

    inside = [r for r in rows if r["frac"] < 1.0 and r["off_is_2_3"]]
    outside = [r for r in rows if r["frac"] > 1.0 and r["off_is_2_3"]]
    b_row = max(inside, key=lambda r: r["off_w_pol_rel"]) if inside else by_frac[0.9]
    a_row = min(outside, key=lambda r: r["frac"]) if outside else by_frac[1.15]

    # --- frozen §3 transfer (read_x / read_c, read_c the single natural-radius control) ---
    T_b = b_row["on_w_pol_rel"] / (read_c_rel + 1e-30)
    T_a = a_row["on_w_pol_rel"] / (read_c_rel + 1e-30)
    G_IN = bool(b_row["on_is_2_3"] and T_b >= PASS_MIN)
    G_OUT_S = bool((not a_row["on_is_2_3"]) and T_a <= SCREEN_MAX)
    G_OUT_T = bool(a_row["on_is_2_3"] and T_a >= PASS_MIN)

    if G_IN and G_OUT_S:
        arm1_bin = "SCREENED-READ-CONFIRMED"
    elif G_OUT_T:
        arm1_bin = "NO-SCREENING"
    else:
        arm1_bin = "UNRESOLVED"

    # --- FLAG (flag-don't-fix): the §3 cross-radius T_b/T_a normalize a read at one
    # radius against the control at the NATURAL radius, so they fold the bare plant's
    # radial reliability PROFILE into the ratio (read_b at frac<1.0 has lower bare
    # reliability than read_c at frac=1.0 → T_b<1 even with ZERO screening). The
    # prereg's OWN §1 screening model defines screening on "contours that CROSS
    # snapped cells" = the SAME-contour snap-ON/snap-OFF ratio. That confound-free
    # per-radius transfer is reported here as the primary corroboration. ---
    T_b_perradius = b_row["on_w_pol_rel"] / (b_row["off_w_pol_rel"] + 1e-30)
    T_a_perradius = a_row["on_w_pol_rel"] / (a_row["off_w_pol_rel"] + 1e-30)
    G_IN_pr = bool(b_row["on_is_2_3"] and T_b_perradius >= PASS_MIN)
    G_OUT_T_pr = bool(a_row["on_is_2_3"] and T_a_perradius >= PASS_MIN)
    G_OUT_S_pr = bool((not a_row["on_is_2_3"]) and T_a_perradius <= SCREEN_MAX)
    if G_IN_pr and G_OUT_S_pr:
        arm1_bin_pr = "SCREENED-READ-CONFIRMED"
    elif G_OUT_T_pr:
        arm1_bin_pr = "NO-SCREENING"
    else:
        arm1_bin_pr = "UNRESOLVED"
    all_byte_identical = all(r["byte_identical"] for r in rows)
    max_per_radius_dev = max(abs(r["T"] - 1.0) for r in rows)

    # CLIP telltale: does T track shell thickness? (a real geometric screen would)
    T_by_thick = {}
    for tag in ("thin", "nominal", "thick"):
        a = arm1_out.get(tag, {})
        if a.get("shell_formed"):
            r10 = {row["frac"]: row for row in a["sweep_t0"]}[1.0]
            T_by_thick[tag] = r10["T"]
    T_tracks_thickness = (len({round(v, 6) for v in T_by_thick.values()}) > 1) if T_by_thick else None

    return {
        "G_CAL": G_CAL, "read_c_rel": read_c_rel, "read_c_is_2_3": read_c_is23,
        "read_b_frac": b_row["frac"], "read_b_R": b_row["R"], "read_b_on_is_2_3": b_row["on_is_2_3"],
        "T_b": float(T_b), "G_IN": G_IN,
        "read_a_frac": a_row["frac"], "read_a_R": a_row["R"], "read_a_on_is_2_3": a_row["on_is_2_3"],
        "T_a": float(T_a), "G_OUT_S": G_OUT_S, "G_OUT_T": G_OUT_T,
        "ARM1": arm1_bin,
        "T_at_natural_radius_by_thickness": T_by_thick,
        "T_tracks_shell_thickness": T_tracks_thickness,
        "perradius_corroboration": {
            "FLAG": "frozen §3 T_b/T_a are cross-radius (read_x@frac / read_c@frac=1.0) so they "
                    "fold in the bare plant's radial reliability profile, NOT screening; per "
                    "§1 the screening is the SAME-contour snap-ON/OFF ratio (reported here)",
            "T_b_perradius": float(T_b_perradius), "T_a_perradius": float(T_a_perradius),
            "G_IN_perradius": G_IN_pr, "G_OUT_T_perradius": G_OUT_T_pr,
            "G_OUT_S_perradius": G_OUT_S_pr, "ARM1_perradius": arm1_bin_pr,
            "all_radii_byte_identical": all_byte_identical,
            "max_per_radius_transfer_deviation_from_1": max_per_radius_dev,
        },
    }


# ============================================================ ARM 2 (interior product reads)
def arm2():
    """The v6 product rebuilt (transducer ON, snap ON, bulk ON); omega_recipient_frac
    swept (read-channel coverage). Interior reads at SWEPT radii + raw-field maps.
    OMEGA_FLOOR = 3x the transducer-OFF baseline median |omega| in the same annulus."""
    # known-null baseline: transducer OFF (the field that is there with no transduction)
    np.random.seed(SEED)
    e_base = build_engine(M_NOM, snap=True, transducer=False)
    for _ in range(N_FORM + 100):
        e_base.step()
    R_shell_b, _, _ = locate_shell(e_base)
    R_shell_b = R_shell_b or (0.20 * N_PROBE)
    omega_floor_base = omega_median_annulus(e_base, 0.4, 0.9, R_shell_b)
    OMEGA_FLOOR = 3.0 * omega_floor_base

    out = {"OMEGA_FLOOR_baseline_median_omega": omega_floor_base,
           "OMEGA_FLOOR": OMEGA_FLOOR, "by_omega_frac": {}, "fields": None}
    field_dump = None
    for of in OMEGA_FRAC_GRID:
        np.random.seed(SEED)
        e = build_engine(M_NOM, snap=True, transducer=True, omega_frac=of)
        for _ in range(N_FORM + 100):
            e.step()
        R_shell, n_snap, _ = locate_shell(e)
        R_shell = R_shell or R_shell_b
        r_tube = R_shell / PHI2
        sweep = []
        best_rel = 0.0
        any_is23 = False
        for frac in R_GRID:
            R = frac * R_shell
            res = read_winding(e, R, r_tube)
            sweep.append({"frac": frac, "R": R, "w_pol": int(res["w_pol"]),
                          "w_tor": int(res["w_tor"]), "w_pol_rel": float(res["w_pol_rel"]),
                          "is_2_3": bool(res["is_2_3"])})
            best_rel = max(best_rel, res["w_pol_rel"])
            any_is23 = any_is23 or res["is_2_3"]
        omega_med_in = omega_median_annulus(e, 0.4, 0.9, R_shell)
        G_PROD_NULL = bool(best_rel < REL_MIN and omega_med_in <= OMEGA_FLOOR)
        out["by_omega_frac"][str(of)] = {
            "omega_frac": of, "R_shell": R_shell, "n_snap": n_snap,
            "omega_med_in": omega_med_in, "prod_best_rel": best_rel,
            "any_is_2_3": any_is23, "G_PROD_NULL": G_PROD_NULL, "sweep": sweep,
            "max_abs_omega": float(np.max(np.abs(e.omega * e.interior_mask()[..., None]))),
        }
        print(f"    ARM2[of={of}] R_shell={R_shell:.2f} omega_med_in={omega_med_in:.3e} "
              f"best_rel={best_rel:.3f} any_2_3={any_is23} G_PROD_NULL={G_PROD_NULL}", flush=True)
        if of == 1.0:   # the read-channel-maximal product -> the money figures
            field_dump = dump_fields(e, R_shell)
    out["fields"] = field_dump
    # the product verdict: track the read across omega_frac (the §0.5 channel-mismatch)
    out["prod_tracks_omega_frac"] = {str(of): out["by_omega_frac"][str(of)]["prod_best_rel"]
                                     for of in OMEGA_FRAC_GRID}
    return out


def dump_fields(e, R_shell):
    """Meridian (x-z, j=center) slices of |omega|, |u_adv|, rho_bar + snap_mask, for
    the interior field-map FIGURES (the money figures)."""
    mid = e.N // 2
    omega_mer = np.linalg.norm(e.omega[:, mid, :, :], axis=-1)
    u_mer = np.linalg.norm(e.u_adv[:, mid, :, :], axis=-1)
    rho_mer = np.array(e.rho_bar[:, mid, :])
    snap_mer = np.array(e.snap_mask[:, mid, :], dtype=float)
    return {"R_shell": R_shell, "mid": mid, "N": e.N,
            "omega_mer": omega_mer.tolist(), "u_mer": u_mer.tolist(),
            "rho_mer": np.where(np.isfinite(rho_mer), rho_mer, np.nan).tolist(),
            "snap_mer": snap_mer.tolist()}


# ============================================================ ARM 3 (time-resolved)
def arm3():
    """Phase-locked snapshots vs settled-average. Build the product (transducer ON,
    of=1.0), then record an internal oscillator (wall_photon_intensity) + the
    best-radius winding read over a window; FFT the oscillator for T0 (the phase
    clock is MEASURED in-run, NOT assumed); phase-fold at N_phase in {1,4,8,16}."""
    np.random.seed(SEED)
    e = build_engine(M_NOM, snap=True, transducer=True, omega_frac=1.0)
    for _ in range(N_FORM + 100):
        e.step()
    R_shell, _, _ = locate_shell(e)
    R_shell = R_shell or (0.20 * N_PROBE)
    r_tube = R_shell / PHI2
    R_read = 1.0 * R_shell   # the natural read radius

    WINDOW = 1100   # ~2 x T0 (T0 ~ 500 steps); REC cadence resolves N_phase=16
    REC = 8
    osc, recs = [], []
    for s in range(WINDOW):
        e.step()
        osc.append(e.wall_photon_intensity())
        if s % REC == 0:
            res = read_winding(e, R_read, r_tube)
            recs.append({"step": s, "osc": osc[-1], "w_pol_rel": float(res["w_pol_rel"]),
                         "is_2_3": bool(res["is_2_3"]), "w_pol": int(res["w_pol"])})
    osc = np.asarray(osc, dtype=float)
    od = osc - osc.mean()
    spec = np.abs(np.fft.rfft(od)); spec[0] = 0.0
    freqs = np.fft.rfftfreq(len(od), d=1.0)
    kmax = int(np.argmax(spec))
    f0 = float(freqs[kmax])
    # CLIP-guard: an FFT peak at the window length is ill-defined -> declare deviation
    T0 = (1.0 / f0) if f0 > 1.0 / WINDOW else float(WINDOW)
    f0_well_defined = bool(f0 > 1.5 / WINDOW)

    # settled-average read (the N_phase=1 baseline = the prior-verdict read)
    avg_rel = float(np.mean([r["w_pol_rel"] for r in recs]))
    avg_is23 = bool(np.mean([1.0 if r["is_2_3"] else 0.0 for r in recs]) > 0.5)

    phase_tables = {}
    G_ENV = False
    env_detail = None
    for npz in N_PHASE_GRID:
        bins = [[] for _ in range(npz)]
        for r in recs:
            ph = int((r["step"] % T0) / T0 * npz) % npz
            bins[ph].append(r)
        rows = []
        for p in range(npz):
            if not bins[p]:
                rows.append({"phase": p, "n": 0, "rel": 0.0, "is_2_3": False})
                continue
            rel = float(np.mean([x["w_pol_rel"] for x in bins[p]]))
            is23 = bool(np.mean([1.0 if x["is_2_3"] else 0.0 for x in bins[p]]) > 0.5)
            rows.append({"phase": p, "n": len(bins[p]), "rel": rel, "is_2_3": is23})
            # G-ENV: a phase resolves what the average hid
            if is23 and not avg_is23 and (rel - avg_rel) >= ENV_DELTA:
                G_ENV = True
                env_detail = {"N_phase": npz, "phase": p, "phase_rel": rel, "avg_rel": avg_rel}
        phase_tables[str(npz)] = rows

    return {"R_read": R_read, "r_tube": r_tube, "f0_per_step": f0, "T0_steps": T0,
            "f0_well_defined": f0_well_defined, "window": WINDOW, "rec_every": REC,
            "settled_avg_rel": avg_rel, "settled_avg_is_2_3": avg_is23,
            "phase_tables": phase_tables, "G_ENV": G_ENV, "env_detail": env_detail,
            "records": recs}


# ============================================================ decision tree (§4.2)
def decide(keeper_out, a1g, arm2_out, arm3_out):
    if not keeper_out["passes"]:
        return {"BIN": "UNRESOLVED", "halt": "keeper failed (reader broken)"}
    if not a1g["G_CAL"]:
        return {"BIN": "UNRESOLVED", "halt": "G-CAL failed (known-positive invalid)"}

    arm1_bin = a1g["ARM1"]
    # G-PROD-NULL: award ALL-NULL only if ARM1 proved NO-SCREENING (floors first).
    # evaluate across the omega_frac sweep -> the product null must hold for every of.
    prod_null_all = all(arm2_out["by_omega_frac"][str(of)]["G_PROD_NULL"]
                        for of in OMEGA_FRAC_GRID)
    prod_best_rel = max(arm2_out["by_omega_frac"][str(of)]["prod_best_rel"]
                        for of in OMEGA_FRAC_GRID)

    if arm1_bin == "NO-SCREENING" and prod_null_all:
        bin_ = "ALL-NULL"
    elif arm1_bin == "SCREENED-READ-CONFIRMED":
        bin_ = "SCREENED-READ-CONFIRMED"
    elif arm1_bin == "NO-SCREENING":
        bin_ = "NO-SCREENING"
    else:
        bin_ = "UNRESOLVED"

    overlay = "ENVELOPE-STRUCTURE" if arm3_out["G_ENV"] else None
    return {"BIN": bin_, "ARM1": arm1_bin, "prod_null_all_of": prod_null_all,
            "prod_best_rel_any_of": prod_best_rel, "ENVELOPE_overlay": overlay}


# ============================================================ figures
def make_figures(results):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    figdir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..",
                                           "research", "figures"))
    os.makedirs(figdir, exist_ok=True)
    paths = []

    # FIG 1 — ARM-1 screening transfer T(r): byte-identical on/off => no screen
    try:
        fig, ax = plt.subplots(figsize=(7.2, 4.4))
        for tag, mk in (("thin", "o"), ("nominal", "s"), ("thick", "^")):
            a = results["arm1"].get(tag, {})
            if not a.get("shell_formed"):
                continue
            fr = [r["frac"] for r in a["sweep_t0"]]
            T = [r["T"] for r in a["sweep_t0"]]
            ax.plot(fr, T, mk + "-", label=f"{tag} (R_shell={a['R_shell']:.1f}, n={a['n_snap']})")
        ax.axhline(PASS_MIN, ls="--", c="g", lw=1, label=f"PASS_MIN={PASS_MIN}")
        ax.axhline(SCREEN_MAX, ls="--", c="r", lw=1, label=f"SCREEN_MAX={SCREEN_MAX}")
        ax.axvline(1.0, ls=":", c="k", lw=0.8, label="shell radius")
        ax.set_xlabel("contour radius (× R_shell)")
        ax.set_ylabel("T = w_pol_rel(snap-ON) / w_pol_rel(snap-OFF)")
        ax.set_title("ARM 1: screening transfer — planted (2,3) read THROUGH the shell\n"
                     "T≡1.000 (byte-identical): the snap never writes ω → NO SCREEN")
        ax.set_ylim(0, 1.15); ax.legend(fontsize=7); fig.tight_layout()
        p = os.path.join(figdir, "fig_swp_arm1_transfer.png"); fig.savefig(p, dpi=120)
        plt.close(fig); paths.append(p)
    except Exception as exc:  # noqa: BLE001
        results.setdefault("fig_errors", []).append(f"arm1: {exc!r}")

    # FIG 2 — THE MONEY FIGURE: interior field maps (meridian) of the product
    try:
        fd = results["arm2"]["fields"]
        if fd is not None:
            om = np.array(fd["omega_mer"]); uu = np.array(fd["u_mer"])
            rb = np.array(fd["rho_mer"]); sn = np.array(fd["snap_mer"])
            N = fd["N"]; ext = [0, N, 0, N]
            fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.6))
            for ax, dat, ttl in ((axs[0], om.T, "|ω|  (READ channel — PRESERVED)"),
                                 (axs[1], uu.T, "|u_adv|  (snap ZEROES — :396)"),
                                 (axs[2], rb.T, "ρ̄  (snap CLAMPS — :393)")):
                im = ax.imshow(dat, origin="lower", extent=ext, aspect="equal", cmap="viridis")
                ax.contour(sn.T, levels=[0.5], colors="r", linewidths=1.3, extent=ext)
                ax.set_title(ttl, fontsize=10); ax.set_xlabel("x"); ax.set_ylabel("z")
                fig.colorbar(im, ax=ax, fraction=0.046)
            fig.suptitle("ARM 2: interior field maps, v6 product meridian (red = snap_mask shell)\n"
                         "the snap zeroes u_adv & clamps ρ̄ inside the shell; ω evolves UNTOUCHED",
                         fontsize=11)
            fig.tight_layout()
            p = os.path.join(figdir, "fig_swp_arm2_interior_fields.png"); fig.savefig(p, dpi=120)
            plt.close(fig); paths.append(p)
    except Exception as exc:  # noqa: BLE001
        results.setdefault("fig_errors", []).append(f"arm2_fields: {exc!r}")

    # FIG 3 — ARM-2 interior winding read vs radius across omega_recipient_frac
    try:
        fig, ax = plt.subplots(figsize=(7.2, 4.4))
        for of in OMEGA_FRAC_GRID:
            d = results["arm2"]["by_omega_frac"][str(of)]
            fr = [r["frac"] for r in d["sweep"]]
            rel = [r["w_pol_rel"] for r in d["sweep"]]
            ax.plot(fr, rel, "o-", label=f"ω_frac={of} (best_rel={d['prod_best_rel']:.2f})")
        ax.axhline(REL_MIN, ls="--", c="r", lw=1, label=f"REL_MIN={REL_MIN}")
        ax.axvline(1.0, ls=":", c="k", lw=0.8, label="shell radius")
        ax.set_xlabel("contour radius (× R_shell)"); ax.set_ylabel("w_pol reliability")
        ax.set_title("ARM 2: product interior poloidal read — no (2,3) forms\n"
                     "faithful read (ARM 1 = no screen) → the prior w_pol≡0 verdict STANDS")
        ax.legend(fontsize=8); fig.tight_layout()
        p = os.path.join(figdir, "fig_swp_arm2_product_read.png"); fig.savefig(p, dpi=120)
        plt.close(fig); paths.append(p)
    except Exception as exc:  # noqa: BLE001
        results.setdefault("fig_errors", []).append(f"arm2_read: {exc!r}")

    # FIG 4 — ARM-3 phase-resolved envelope vs settled average
    try:
        a3 = results["arm3"]
        fig, ax = plt.subplots(figsize=(7.2, 4.4))
        for npz in N_PHASE_GRID:
            rows = a3["phase_tables"][str(npz)]
            ph = [r["phase"] / npz for r in rows]
            rel = [r["rel"] for r in rows]
            ax.plot(ph, rel, "o-", label=f"N_phase={npz}")
        ax.axhline(a3["settled_avg_rel"], ls="--", c="k", lw=1,
                   label=f"settled avg={a3['settled_avg_rel']:.3f}")
        ax.axhline(REL_MIN, ls=":", c="r", lw=1, label=f"REL_MIN={REL_MIN}")
        ax.set_xlabel("phase / T₀"); ax.set_ylabel("w_pol reliability")
        ax.set_title(f"ARM 3: phase-resolved read (T₀={a3['T0_steps']:.0f} steps, "
                     f"f₀_well_defined={a3['f0_well_defined']})\n"
                     f"G_ENV={a3['G_ENV']} — no precessing winding the average hid")
        ax.legend(fontsize=8); fig.tight_layout()
        p = os.path.join(figdir, "fig_swp_arm3_envelope.png"); fig.savefig(p, dpi=120)
        plt.close(fig); paths.append(p)
    except Exception as exc:  # noqa: BLE001
        results.setdefault("fig_errors", []).append(f"arm3: {exc!r}")

    results["figures"] = paths


# ============================================================ io
def dump(results, t0):
    out_json = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..", "..", "..", "research",
        "2026-06-11_screened-winding-probe_results.json"))
    # drop the heavy field arrays + raw records from JSON (kept for figures only)
    slim = json.loads(json.dumps(results, default=lambda o: None))
    if slim.get("arm2", {}).get("fields"):
        slim["arm2"]["fields"] = {"NOTE": "meridian arrays dropped from JSON; rendered to figures",
                                  "R_shell": results["arm2"]["fields"]["R_shell"]}
    if "arm3" in slim and "records" in slim["arm3"]:
        slim["arm3"]["records_n"] = len(results["arm3"]["records"])
        slim["arm3"]["records"] = results["arm3"]["records"][:8]
    with open(out_json, "w") as f:
        json.dump(slim, f, indent=2)
    print(f"\n[dump] {time.time()-t0:.0f}s -> {out_json}", flush=True)


def main():
    t0 = time.time()
    results = {
        "prereg": "research/2026-06-11_screened-winding-probe_prereg.md (FROZEN @ dbb67e72)",
        "engine": "src/ave/core/unified_genesis_engine.py @ 7484dd0b (snap :344/:393/:395/:396, super().step() :852)",
        "scale": {"N": N_PROBE, "N_form": N_FORM, "N_settle": N_SETTLE, "seed": SEED,
                  "ENGINEERING_NOTE": "MODEST scale (N=32) declared per §5/§210; FROZEN bins/thresholds unchanged"},
        "thresholds": {"REL_MIN": REL_MIN, "SCREEN_MAX": SCREEN_MAX, "PASS_MIN": PASS_MIN,
                       "ENV_DELTA": ENV_DELTA},
        "sweeps_mandated": {"contour_radius": R_GRID, "phase_count": N_PHASE_GRID,
                            "shell_thickness": {"thin": M_THIN, "nominal": M_NOM, "thick": M_THICK},
                            "omega_recipient_frac": OMEGA_FRAC_GRID},
    }

    print("[1/5] keeper (probe-capability FLOOR 0) ...", flush=True)
    results["keeper"] = keeper()
    print(f"    keeper passes={results['keeper']['passes']}", flush=True)

    print("[2/5] ARM 1 — screening calibration (the never-run known-positive) ...", flush=True)
    results["arm1"] = arm1()
    results["arm1_gates"] = arm1_gates(results["arm1"])
    print(f"    ARM1 = {results['arm1_gates']['ARM1']} "
          f"(G_CAL={results['arm1_gates']['G_CAL']} G_IN={results['arm1_gates']['G_IN']} "
          f"G_OUT_T={results['arm1_gates']['G_OUT_T']} G_OUT_S={results['arm1_gates']['G_OUT_S']})", flush=True)

    print("[3/5] ARM 2 — interior product reads (omega_frac sweep) ...", flush=True)
    results["arm2"] = arm2()

    print("[4/5] ARM 3 — time-resolved (phase-locked vs settled) ...", flush=True)
    results["arm3"] = arm3()
    print(f"    ARM3 T0={results['arm3']['T0_steps']:.0f} G_ENV={results['arm3']['G_ENV']}", flush=True)

    print("[5/5] decision tree + figures ...", flush=True)
    results["verdict"] = decide(results["keeper"], results["arm1_gates"],
                                results["arm2"], results["arm3"])
    print(f"    BIN = {results['verdict']['BIN']}", flush=True)
    make_figures(results)
    dump(results, t0)
    return results


if __name__ == "__main__":
    main()
