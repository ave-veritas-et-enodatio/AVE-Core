"""
ANNIHILATION / EVAPORATION — the Phase-2 run of the 2026-06-11 prereg
=====================================================================

Executes the FROZEN design of `research/2026-06-11_annihilation-evaporation_prereg.md`
(committed ALONE @ b883c9b4): two v6-class converged dilatation masses, OPPOSITE
drive helicity, an energized-then-COASTED relative translation, the §6 arm matrix,
the §3 floors (re-measured at THIS config), the §8 mandated sweeps, the §5
conservation-by-channel ledger, the §7 ordered bins. All numbers FROM the evolved
field / dumped JSON (ave-driver-script-honesty); headline numbers are NET
(MAIN − control) FIELD quantities (§9 gross-vs-field).

§210 DEVIATIONS — STATED HERE, BEFORE THE RUN (the prereg's own law):

  DEV-1 (NO per-object rotation column).  The v6 DRIVER config also energized a
        GLOBAL rotation column (M=1.8 about the grid z-axis). The prereg's §0.1
        FROZEN recipe enumeration does NOT include it; the engine capability is
        global-axis-only (cannot be placed at c_A/c_B); and a grid-centered
        column would contaminate the load-bearing net-AM channel (the v6 §4
        GEOMETRIC false-positive: core_sense_u 20.00 ≈ achiral 20.00, column-
        dominated). The build therefore runs WITHOUT the column. RE-BIN
        consequence: the T1 build-validity gate (§4.1) is RE-MEASURED at this
        column-less config (E_V^cons convergence read from this run's own build
        series, not inherited); the ρ̄ pocket channel is quiescent during build
        (nothing rarefies ρ̄ without the column's centrifugal deficit).
  DEV-2 (additive per-object photon drive).  The inherited seed_photon ASSIGNS
        w_prev components (crystal_engine.py:325-326), so a second drive call
        would clobber photon A's group-velocity imprint. The build uses the
        subclass drive_chiral_photon_at (additive; single-call value-identical,
        keeper K-DRIVE-EQUIV green).
  DEV-3 (C-static-overlap is PLACED, not transplanted).  No converged-object
        transplant capability exists or was frozen; the geometric control seeds
        the two objects CO-LOCATED (superposed seed, A≈2·frac) + both drives and
        observes the same window. It discriminates placement-geometry bursts
        exactly as §6 intends.
  DEV-4 (v_approach sweep at equal closing DISPLACEMENT).  Encounter windows
        scale with 1/v (each point runs to arrival + the same persist tail) —
        the prereg §8's anticipated fixed-total-closing-displacement form. The
        regime-bracket "too gentle to arrive" point runs v=0.05 at the FIXED
        default window (it demonstrably does NOT reach overlap).
  DEV-5 (threshold_mult swept in POST).  The detector history is re-scanned at
        {2.0, 3.0, 5.0}× the same calibrated floor — exact, no new runs.
  DEV-6 (FIXED 3600-step encounter windows; stated BEFORE the matrix, from the
        N=32 smoke).  The engine lineage's CFL (graft-v2: S_min=1e-4 ⇒
        c_eff_max=100) gives dt=0.001732 — closing 18 cells at v_approach=0.2
        would need ~52,000 steps — AND the smoke shows the V-sector drift
        imprint produces ZERO centroid motion over 17k steps (the 3D scalar
        wave equation admits no subluminal rigid transport; the imprinted KE
        radiates instead of convecting the trap). Arrival-scaled windows are
        therefore both infeasible and moot. ALL encounter windows are FIXED at
        3600 steps; n_close is still computed and recorded per-run to document
        the arrival infeasibility; every approach arm's regime witness is
        recorded so never-met nulls are LABELLED wrong-regime per §1.5. The K3
        stop-time sweep {600,1200,2400} is read as cut-points of the MAIN
        encounter series (covered by the 3600 window). RE-BIN consequence:
        F-TRANSLATE's "arrives" criterion is evaluated against the WITHIN-
        WINDOW expected displacement (v_obj·n_enc·dt), not the full half-
        separation (unreachable in any feasible window at this dt).

PRE-RUN STRUCTURAL FLAG (flag-don't-fix; recorded before any number exists):
code-reading confirms the V/w/ω sectors and the ρ̄/u bulk sector are dynamically
INDEPENDENT in this engine (GAP-C couplings default-OFF; `_bulk_rhs` reads only
ρ̄,u; graft v2-v4 never touch ρ̄/u). The burst detector reads ONLY snap-machine
ledgers and the snap fires ONLY on ρ̄ ≤ ρ̄_cav crossings. The only V→ρ̄ path is
V→(converter)→w→(transducer)→u_adv→ρ̄, ~3 OOM below the cavitation floor at v6
magnitudes. The ANNIHILATE bin's burst criterion is therefore expected to be
STRUCTURALLY unreachable at this architecture — if so, that is reported under
§1.5 as a wrong-regime/missing-channel artifact for the burst criterion, NOT as
a clean annihilation negative; the V-sector dynamics still classify the
encounter (MERGE/BOUNCE/PASS-THROUGH) and the handedness contrast still answers
the §2 ontology question.

Run:
    PYTHONPATH=src .venv/bin/python src/scripts/vol_1_foundations/annihilation_evaporation_run.py
"""

from __future__ import annotations

import copy
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from ave.core.annihilation_engine import AnnihilationEngine  # noqa: E402
from ave.core.longitudinal_burst_detector import LongitudinalBurstDetector  # noqa: E402
from ave.core.unified_genesis_engine import RHO_CAV  # noqa: E402
from ave.utils.genesis_parallel_runner import RunSpec, run_specs  # noqa: E402

# ------------------------------------------------- FROZEN scale (prereg §0.1/§11)
SEED = 20260610
N_MAIN = 48
N_BUILD = 3200
N_PERSIST = 1200
REC_EVERY = 100
FRAC = 0.85
DRIVE_AMP = 0.10
WAVELEN = 8.0
SIGMA_PH = 5.0
SIGMA_SEED = 4.0
CHI_DEFAULT = 0.02
OMEGA_FRAC_MAIN = 0.5
MEISSNER_MAIN = 0.05
LOCK_ETA_MAIN = 0.08
SEP_FRAC = 18.0 / 48.0          # object separation as a fraction of N (18 cells @48)
V_APPROACH_MAIN = 0.2           # the headline closing speed (M_app = 0.2 — slow, D2)
H_REC_EVERY = 10                # H_total^cons cadence in the encounter (F-CLOSE canary)
T1_DRIFT_FLOOR = 5e-2           # the v6 T1 late-drift floor (gate lineage: v6 §7.5)
ENC_WINDOW = 3600               # DEV-6: fixed encounter window (all arms)


# ================================================================ build (§4.1)
def build_pair(cfg):
    """Two-object §4.1 build: seeds at c_A/c_B + frozen wall window + per-object
    chiral drives (DEV-1: no rotation column; DEV-2: additive drives). cfg keys:
    N, frac, chi_exch, meissner, hA, hB, b (impact parameter, cells, applied to
    c_B in y), colocated (DEV-3), single (C-translate: object A only)."""
    N = cfg["N"]
    e = AnnihilationEngine(
        N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
        nu_art_bulk=5e-4, rho_diff=5e-4,
        snap_payback_rate=1.0, delta_heal=0.0, rho_cav=RHO_CAV, chi_shock=1.0,
        vent_mode="absorbed", snap_accounting="conservative",
        meissner_harden=cfg["meissner"],
        omega_sector_on=True, buckle_on=True, photon_coupling=True,
        lock_on=True, lock_eta=LOCK_ETA_MAIN, wall_width=0.12,
        transducer_on=(cfg["chi_exch"] > 0.0), chi_exch=cfg["chi_exch"],
        omega_recipient_frac=OMEGA_FRAC_MAIN,
    )
    c = (N - 1) / 2.0
    half = SEP_FRAC * N / 2.0
    if cfg.get("colocated"):
        cA = (c, c, c)
        cB = (c, c, c)
    else:
        cA = (c - half, c, c)
        cB = (c + half, c + cfg.get("b", 0.0), c)
    e.seed_lane1(center=cA, sigma=SIGMA_SEED, frac=cfg["frac"], vent_into_seed=False)
    if not cfg.get("single"):
        e.seed_lane1(center=cB, sigma=SIGMA_SEED, frac=cfg["frac"], vent_into_seed=False)
    e.freeze_wall_window()
    e.drive_chiral_photon_at(cA, helicity=cfg["hA"], sigma=SIGMA_PH,
                             wavelength=WAVELEN, amplitude=DRIVE_AMP, axis=2)
    if not cfg.get("single"):
        e.drive_chiral_photon_at(cB, helicity=cfg["hB"], sigma=SIGMA_PH,
                                 wavelength=WAVELEN, amplitude=DRIVE_AMP, axis=2)
    return e, cA, cB


# ================================================================ measurement
def measure(e, axis=2):
    """All observables FROM the evolved field (driver-honesty). Adds the §1.5
    regime witnesses + per-object windowed reads to the v6 set."""
    mA, mB = e.half_masks(axis=0)
    rc, _ = e.rho_core()
    led = e.transducer_ledger()
    return {
        "step": int(e.step_count),
        "E_V_cons": float(e.bulk_energy_conserved(True)),
        "E_V_naive": float(e.bulk_energy(True)),
        "H_total_cons": float(e.total_energy_unified(conserved=True)),
        "E_w_int": float(e.shear_energy(True)),
        "pocket_cells": int(e.pocket_cells()),
        "rho_min": float(rc),
        "strain_max": float(e.strain_max_interior()),
        "p_integral": float(e.bulk_pressure_integral()),
        "L_bulk": float(e.angular_momentum_bulk(axis)),
        "L_omega_axial": float(e.angular_momentum_omega_axial(axis)),
        "L_total_field": float(e.angular_momentum_bulk(axis)
                               + e.angular_momentum_omega_axial(axis)),
        "Hbel": float(e.helicity_bel()),
        "S_photon_axial": float(e.photon_spin_axial(axis)),
        "massA_w": float(e.windowed_mass_cons(mA)),
        "massB_w": float(e.windowed_mass_cons(mB)),
        "spinA_w": float(e.windowed_photon_spin(mA, axis)),
        "spinB_w": float(e.windowed_photon_spin(mB, axis)),
        "P_x": float(e.field_momentum_x()),
        "x_centroid": float(e.x_centroid_V2()),
        "peaks_x": int(e.x_profile_peak_count()),
        "E_latent_held": float(e.E_latent_held),
        "E_latent_restored": float(e.E_latent_restored),
        "E_vent_absorbed": float(e.E_vent_absorbed),
        "E_diss_snap": float(e.E_diss_snap),
        "E_transduce_photon_loss": float(e.E_transduce_photon_loss),
        "E_absorbed_sink": float(led["E_absorbed_sink"]),
        "passive_no_pump": bool(led["passive_no_pump"]),
        "snap_events": int(e.snap_events),
        "max_abs_V": float(np.max(np.abs(e.V * e.interior_mask()))),
        "max_abs_u": float(np.max(np.abs(e.u_adv))),
        "finite": bool(np.all(np.isfinite(e.V)) and np.all(np.isfinite(e.w))
                       and np.all(np.isfinite(e.rho_bar))),
    }


# ====================================================== the worker (spawn-safe)
def run_encounter_worker(*, cfg, v_approach, n_build=N_BUILD, n_persist=N_PERSIST,
                         fixed_window=None, rec_every=REC_EVERY,
                         calib_steps=200, no_approach=False):
    """One independent run: BUILD (n_build) → per-run F-BURST floor calibration
    on the built STATIC state (a deepcopy; §3 floors re-measured at THIS config)
    → imprint ±v/2 drifts (unless no_approach) → COAST the encounter window
    (arrival-scaled, DEV-4) with the detector + F0c reactance pairs + F-CLOSE
    canary recording. Deterministic per SEED. Returns JSON-serializable dict."""
    np.random.seed(SEED)
    t0 = time.time()
    e, cA, cB = build_pair(cfg)
    cert = e.seed_certificate()

    build_series = [measure(e)]
    for s in range(1, n_build + 1):
        e.step()
        if s % 400 == 0 or s == n_build:
            build_series.append(measure(e))
            if not build_series[-1]["finite"]:
                build_series[-1]["NONFINITE"] = True
                break
    built = measure(e)

    # ---- T1 build-validity gate (§4.1, re-measured at THIS config; DEV-1) ----
    ev = [s["E_V_cons"] for s in build_series]
    late = ev[len(ev) // 2:]
    t1_drift = abs(late[-1] - late[0]) / (abs(late[0]) + 1e-30)
    t1_pass = bool(t1_drift < T1_DRIFT_FLOOR and built["finite"])

    # ---- per-run F-BURST floor: the built STATIC pair is the known-null ----
    e_floor = copy.deepcopy(e)
    f_burst = float(LongitudinalBurstDetector.calibrate_floor(e_floor, steps=calib_steps))
    del e_floor

    # ---- the energized approach (the §4.2 IC; ave-conserved-vs-pumped) ----
    mA, mB = e.half_masks(axis=0)
    if no_approach or v_approach == 0.0:
        book_A = book_B = {"KE_approach": 0.0}
        n_close = 0
    else:
        book_A = e.imprint_drift((+0.5 * v_approach, 0.0, 0.0), region_mask=mA)
        if not cfg.get("single"):
            book_B = e.imprint_drift((-0.5 * v_approach, 0.0, 0.0), region_mask=mB)
        else:
            book_B = {"KE_approach": 0.0}
        sep_cells = SEP_FRAC * cfg["N"]
        n_close = int(np.ceil(sep_cells * e.dx / (max(v_approach, 1e-9) * e.dt)))
    # DEV-6: fixed window (n_close recorded to document arrival infeasibility)
    n_enc = fixed_window if fixed_window is not None else ENC_WINDOW

    ke_approach = float(book_A["KE_approach"] + book_B["KE_approach"])
    eta_ke = ke_approach / (2.0 * max(built["E_V_cons"], 1e-30))
    post_imprint = measure(e)

    # ---- the encounter COAST (no further forcing) ----
    det = LongitudinalBurstDetector(floor=max(f_burst, 1e-30), threshold_mult=3.0)
    det.record(e)
    enc_series = [post_imprint]
    H0 = e.total_energy_unified(conserved=True)
    H_max = H0
    f0c = []  # per-step reactance pairs, BOTH objects (F0c completeness)
    strain_max_run = post_imprint["strain_max"]
    rho_min_run = post_imprint["rho_min"]
    for s in range(1, n_enc + 1):
        e.step()
        det.record(e)
        rpA = e.windowed_reactance_pair(mA)
        rpB = e.windowed_reactance_pair(mB)
        f0c.append((rpA["C2"], rpA["L2"], rpB["C2"], rpB["L2"]))
        if s % H_REC_EVERY == 0:
            H_max = max(H_max, e.total_energy_unified(conserved=True))
        sm = e.strain_max_interior()
        strain_max_run = max(strain_max_run, sm)
        if s % 50 == 0:
            rho_min_run = min(rho_min_run, e.rho_min_interior())
        if s % rec_every == 0 or s == n_enc:
            enc_series.append(measure(e))
            if not enc_series[-1]["finite"]:
                enc_series[-1]["NONFINITE"] = True
                break
    final = measure(e)
    rho_min_run = min(rho_min_run, final["rho_min"])

    f0c = np.asarray(f0c) if f0c else np.zeros((0, 4))
    return {
        "name": cfg["name"],
        "cfg": {k: cfg[k] for k in cfg if k != "name"},
        "dt": float(e.dt),
        "v_approach": float(v_approach),
        "seed_cert": {"passes": bool(cert.get("passes")),
                      "topology_null": bool(cert.get("topology_null"))},
        "T1_gate": {"drift_late": float(t1_drift), "passes": t1_pass,
                    "E_V_cons_first": float(ev[0]), "E_V_cons_last": float(ev[-1])},
        "F_BURST_floor": f_burst,
        "KE_approach": ke_approach,
        "eta_KE": float(eta_ke),
        "n_close": int(n_close), "n_enc": int(n_enc),
        "build_series": build_series,
        "built": built,
        "post_imprint": post_imprint,
        "enc_series": enc_series,
        "final": final,
        "bursts": det.scan(),
        # FULL per-step released history (DEV-5 post-scan must not decimate —
        # a decimated diff could merge/miss bursts; ~n_enc floats per arm)
        "burst_history_released": [h["released"] for h in det.history],
        "total_burst_energy": float(det.total_burst_energy()),
        "H_pos_excursion_frac": float((H_max - H0) / (abs(H0) + 1e-30)),
        "regime_witness": {"strain_max_run": float(strain_max_run),
                           "strain_max_build": float(max(s["strain_max"] for s in build_series)),
                           "rho_min_run": float(rho_min_run),
                           "dilatation_rupture_reached": bool(strain_max_run >= 1.0),
                           "dilatation_rupture_reached_incl_build": bool(
                               max(strain_max_run,
                                   max(s["strain_max"] for s in build_series)) >= 1.0),
                           "cavitation_rupture_reached": bool(rho_min_run <= RHO_CAV)},
        "F0c_complete": bool(f0c.shape[0] == (len(det.history) - 1)
                             and np.all(np.isfinite(f0c))),
        "wall_s": time.time() - t0,
    }


# ===================================================================== FLOORS
def floors_static(main_cfg):
    """§3 floors from the C-no-approach known-null + the empty box, ALL at this
    config (a floor carried from a different config is invalid)."""
    out = {}
    # F0a: empty-box background mass (the K-MASS empty reference, full scale)
    e_empty = AnnihilationEngine(main_cfg["N"], bulk_density_on=True, snap_on=True,
                                 c2_floor=0.0, vent_mode="absorbed",
                                 snap_accounting="conservative")
    for _ in range(200):
        e_empty.step()
    out["F0a_empty_box_mass"] = float(e_empty.bulk_energy_conserved(True))
    return out


# ============================================================== orchestration
def make_cfg(name, *, N=N_MAIN, frac=FRAC, chi_exch=CHI_DEFAULT,
             meissner=MEISSNER_MAIN, hA=+1, hB=-1, b=0.0,
             colocated=False, single=False):
    return dict(name=name, N=N, frac=frac, chi_exch=chi_exch, meissner=meissner,
                hA=hA, hB=hB, b=b, colocated=colocated, single=single)


def main():
    t_start = time.time()
    results = {
        "prereg": "research/2026-06-11_annihilation-evaporation_prereg.md (frozen ALONE @ b883c9b4)",
        "engine": "src/ave/core/annihilation_engine.py (AnnihilationEngine; no step override)",
        "scale": dict(N=N_MAIN, n_build=N_BUILD, n_persist=N_PERSIST, frac=FRAC,
                      chi_exch=CHI_DEFAULT, omega_frac=OMEGA_FRAC_MAIN,
                      meissner=MEISSNER_MAIN, sep_frac=SEP_FRAC,
                      v_approach_main=V_APPROACH_MAIN, seed=SEED),
        "RHO_CAV": RHO_CAV,
        "deviations_stated_pre_run": ["DEV-1 no-column build (recipe §0.1; AM-channel hygiene)",
                                      "DEV-2 additive per-object photon drive (w_prev clobber fix)",
                                      "DEV-3 C-static-overlap is PLACED (no transplant capability)",
                                      "DEV-4 v-sweep at equal closing displacement (arrival-scaled windows)",
                                      "DEV-5 threshold_mult swept in post (same history re-scanned)"],
        "pre_run_structural_flag": ("V→ρ̄ release channel ABSENT (GAP-C): burst criterion expected "
                                    "structurally unreachable; see driver docstring"),
    }

    print("[1/4] static floors (empty box) ...", flush=True)
    results["floors_static"] = floors_static(make_cfg("MAIN"))
    print(f"    F0a_empty={results['floors_static']['F0a_empty_box_mass']:.3e} "
          f"({time.time()-t_start:.0f}s)", flush=True)

    # ---------------- THE ARM MATRIX (§6, FROZEN) ----------------
    print("[2/4] arm matrix (5 arms) ...", flush=True)
    arm_specs = [
        RunSpec("MAIN", run_encounter_worker,
                dict(cfg=make_cfg("MAIN", hA=+1, hB=-1), v_approach=V_APPROACH_MAIN,
                     n_persist=2400)),  # 2400-persist => K3 stop-time read in post
        RunSpec("C-same-handed", run_encounter_worker,
                dict(cfg=make_cfg("C-same-handed", hA=+1, hB=+1),
                     v_approach=V_APPROACH_MAIN, n_persist=1200)),
        RunSpec("C-translate", run_encounter_worker,
                dict(cfg=make_cfg("C-translate", hA=+1, single=True),
                     v_approach=V_APPROACH_MAIN, n_persist=1200)),
        RunSpec("C-no-approach", run_encounter_worker,
                dict(cfg=make_cfg("C-no-approach", hA=+1, hB=-1), v_approach=0.0,
                     no_approach=True, fixed_window=2400)),
        RunSpec("C-static-overlap", run_encounter_worker,
                dict(cfg=make_cfg("C-static-overlap", hA=+1, hB=-1, colocated=True),
                     v_approach=0.0, no_approach=True, fixed_window=2400)),
    ]
    arms = run_specs(arm_specs, serial=False, raise_on_error=False)
    results["arms"] = {k: _strip(v) for k, v in arms.items()}
    _print_arms(arms)

    # ---------------- THE MANDATED SWEEPS (§8) ----------------
    print("[3/4] mandated sweeps (§210) ...", flush=True)
    specs = []
    # 1. approach speed (DEV-4: arrival-scaled; v=0.05 fixed-window regime bracket)
    for v in (0.1, 0.4, 0.8):
        specs.append(RunSpec(("v", v), run_encounter_worker,
                     dict(cfg=make_cfg(f"v_{v}", hA=+1, hB=-1), v_approach=v,
                          n_persist=1200)))
    specs.append(RunSpec(("v", 0.05), run_encounter_worker,
                 dict(cfg=make_cfg("v_0.05_bracket", hA=+1, hB=-1), v_approach=0.05,
                      fixed_window=N_PERSIST)))  # too gentle to arrive (regime bracket)
    # 2. impact parameter b (cells; 0 is MAIN)
    for b in (3.0, 6.0, 10.0):
        specs.append(RunSpec(("b", b), run_encounter_worker,
                     dict(cfg=make_cfg(f"b_{b}", hA=+1, hB=-1, b=b),
                          v_approach=V_APPROACH_MAIN, n_persist=1200)))
    # 3. N resolution (K2)
    for N in (40, 56):
        specs.append(RunSpec(("N", N), run_encounter_worker,
                     dict(cfg=make_cfg(f"N_{N}", N=N, hA=+1, hB=-1),
                          v_approach=V_APPROACH_MAIN, n_persist=1200)))
    # 4. chi_exch (handedness-selectivity gate 7.e)
    for chi in (0.0, 0.005, 0.08):
        specs.append(RunSpec(("chi", chi), run_encounter_worker,
                     dict(cfg=make_cfg(f"chi_{chi}", chi_exch=chi, hA=+1, hB=-1),
                          v_approach=V_APPROACH_MAIN, n_persist=1200)))
    # 5. frac (the D1 rupture-reachability bracket {0.30 below, 0.60, 0.95 above})
    for fr in (0.30, 0.60, 0.95):
        specs.append(RunSpec(("frac", fr), run_encounter_worker,
                     dict(cfg=make_cfg(f"frac_{fr}", frac=fr, hA=+1, hB=-1),
                          v_approach=V_APPROACH_MAIN, n_persist=1200)))
    # 6. meissner
    for ms in (0.0, 0.10):
        specs.append(RunSpec(("meissner", ms), run_encounter_worker,
                     dict(cfg=make_cfg(f"ms_{ms}", meissner=ms, hA=+1, hB=-1),
                          v_approach=V_APPROACH_MAIN, n_persist=1200)))
    raw = run_specs(specs, serial=False, raise_on_error=False)
    results["sweeps"] = {repr(k): _strip(v) for k, v in raw.items()}
    for k, v in raw.items():
        if isinstance(v, dict):
            rw = v["regime_witness"]
            print(f"    {k!r:18} bursts={len(v['bursts'])} strain_max={rw['strain_max_run']:.3f} "
                  f"rho_min={rw['rho_min_run']:+.4f} massF={v['final']['E_V_cons']:.2f} "
                  f"peaks={v['final']['peaks_x']} ({v['wall_s']:.0f}s)", flush=True)
        else:
            print(f"    {k!r:18} ERROR {v}", flush=True)

    # ---------------- BINS (§7, ordered, floors first) ----------------
    print("[4/4] floor-gated ordered bins ...", flush=True)
    results["analysis"] = analyze(results)
    _dump(results, t_start)


def _print_arms(arms):
    for k, v in arms.items():
        if isinstance(v, dict):
            rw = v["regime_witness"]
            print(f"    {k:18s} T1={v['T1_gate']['passes']} (drift {v['T1_gate']['drift_late']:.4f}) "
                  f"EVc_built={v['built']['E_V_cons']:.2f} KEapp={v['KE_approach']:.3f} "
                  f"etaKE={v['eta_KE']:.4f} bursts={len(v['bursts'])} "
                  f"strain={rw['strain_max_run']:.3f} rho_min={rw['rho_min_run']:+.4f} "
                  f"massF={v['final']['E_V_cons']:.2f} peaks={v['final']['peaks_x']} "
                  f"Hexc={v['H_pos_excursion_frac']:.4f} ({v['wall_s']:.0f}s)", flush=True)
        else:
            print(f"    {k:18s} ERROR {v}", flush=True)


# ============================================================== bins / analysis
def analyze(results):
    arms = results["arms"]
    a = {}

    def get(name):
        v = arms.get(name)
        return v if isinstance(v, dict) and "final" in v else None

    main = get("MAIN")
    same = get("C-same-handed")
    trans = get("C-translate")
    noap = get("C-no-approach")
    stat = get("C-static-overlap")
    if not all((main, same, trans, noap, stat)):
        a["ERROR"] = "missing arm(s); no binning"
        return a

    # ---------- FLOOR-0 + F-TRANSLATE gate (evaluated FIRST; §7.1) ----------
    f0a = results["floors_static"]["F0a_empty_box_mass"]
    f_close = noap["H_pos_excursion_frac"]          # known-null ledger excursion
    f_radiate = max(noap["built"]["E_w_int"] - noap["final"]["E_w_int"], 0.0) \
        - (noap["final"]["E_transduce_photon_loss"] - noap["built"]["E_transduce_photon_loss"])
    # F-TRANSLATE: does the single object ARRIVE with its T1 mass intact?
    m0 = trans["post_imprint"]["E_V_cons"]
    m1 = trans["final"]["E_V_cons"]
    translate_leak = abs(m1 - m0) / (abs(m0) + 1e-30)
    moved = trans["final"]["x_centroid"] - trans["built"]["x_centroid"]
    # DEV-6: within-window expectation (v_obj = v/2; dt FROM the run record)
    expected_move = 0.5 * trans["v_approach"] * trans["n_enc"] * trans["dt"]
    translate_arrived = bool(moved >= 0.5 * expected_move)
    f_translate_pass = bool(translate_leak < T1_DRIFT_FLOOR and translate_arrived)
    a["floors"] = {
        "F0a_empty_box_mass": f0a,
        "F_CLOSE_known_null_excursion": f_close,
        "F_RADIATE_known_null": f_radiate,
        "F_BURST_floor_MAIN_config": main["F_BURST_floor"],
        "F_TRANSLATE": {"leak_frac": translate_leak, "moved_cells": moved,
                        "expected_move_cells": expected_move,
                        "arrived": translate_arrived, "passes": f_translate_pass},
        "F0c_complete_MAIN": main["F0c_complete"],
        "T1_gate_MAIN": main["T1_gate"],
        "MAIN_H_excursion_vs_F_CLOSE": {"MAIN": main["H_pos_excursion_frac"],
                                        "F_CLOSE": f_close,
                                        "no_pump": bool(main["H_pos_excursion_frac"]
                                                        <= f_close + 1e-3)},
    }

    # ---------- regime witnesses (§1.5) ----------
    a["regime"] = {
        "MAIN": main["regime_witness"],
        "C_same": same["regime_witness"],
        "C_static_overlap": stat["regime_witness"],
        "structural_flag": results["pre_run_structural_flag"],
    }

    # ---------- NET FIELD headline numbers (§9 gross-vs-field) ----------
    a["net_field"] = {
        "burst_energy_MAIN_minus_Csame": main["total_burst_energy"] - same["total_burst_energy"],
        "bursts_MAIN": len(main["bursts"]), "bursts_Csame": len(same["bursts"]),
        "bursts_CstaticOverlap": len(stat["bursts"]), "bursts_CnoApproach": len(noap["bursts"]),
        "radiate_MAIN_net": (max(main["post_imprint"]["E_w_int"] - main["final"]["E_w_int"], 0.0)
                             - (main["final"]["E_transduce_photon_loss"]
                                - main["post_imprint"]["E_transduce_photon_loss"]))
        - f_radiate,
        "residual_mass_MAIN_final": main["final"]["E_V_cons"],
        "residual_net_collision_loss": (
            (main["post_imprint"]["E_V_cons"] - main["final"]["E_V_cons"])
            - 2.0 * (trans["post_imprint"]["E_V_cons"] - trans["final"]["E_V_cons"])),
        "L_total_field_MAIN_built": main["built"]["L_total_field"],
        "L_total_field_MAIN_final": main["final"]["L_total_field"],
        "L_total_field_Csame_built": same["built"]["L_total_field"],
        "L_total_field_Csame_final": same["final"]["L_total_field"],
        "handedness_contrast_massF_MAIN_minus_Csame":
            main["final"]["E_V_cons"] - same["final"]["E_V_cons"],
        "handedness_contrast_strain_MAIN_minus_Csame":
            main["regime_witness"]["strain_max_run"] - same["regime_witness"]["strain_max_run"],
    }

    # ---------- DEV-5: threshold_mult post-scan ----------
    a["threshold_mult_post"] = {}
    for arm_name, arm in (("MAIN", main), ("C-same-handed", same)):
        per = {}
        for tm in (2.0, 3.0, 5.0):
            bar = arm["F_BURST_floor"] * tm
            rel = arm["burst_history_released"]
            n = sum(1 for i in range(1, len(rel)) if rel[i] - rel[i - 1] > bar)
            per[str(tm)] = n
        a["threshold_mult_post"][arm_name] = per

    # ---------- classification per frozen §7 bins ----------
    def classify(arm, label):
        """§7 ordering: (1) wrong-regime gate FIRST — an approach arm whose
        objects never MET (overlap-rupture never reached in the encounter, no
        centroid convergence) is UNRESOLVED (wrong-regime artifact, §1.5),
        NEVER a verdict bin; (2) then the frozen verdict bins."""
        rw = arm["regime_witness"]
        burst_fired = len(arm["bursts"]) > 0
        mass_to_bg = arm["final"]["E_V_cons"] <= max(f0a, 1e-12)
        peaks = arm["final"]["peaks_x"]
        mass_f = arm["final"]["E_V_cons"]
        mass_b = arm["post_imprint"]["E_V_cons"]
        had_approach = arm["v_approach"] > 0.0 and not arm["cfg"].get("single")
        # did the two blobs actually meet? encounter-window rupture OR the
        # x-profile collapsing to a single central blob from two
        met = bool(rw["dilatation_rupture_reached"]
                   or (had_approach and arm["post_imprint"]["peaks_x"] >= 2 and peaks <= 1))
        if had_approach and not met and not burst_fired:
            cand = "UNRESOLVED-wrong-regime(never-met; transport structurally absent)"
        elif burst_fired and mass_to_bg:
            cand = "ANNIHILATE-candidate"
        elif peaks <= 1 and mass_f > max(f0a, 1e-12):
            cand = "MERGE"
        elif peaks >= 2 and mass_f >= 0.8 * mass_b:
            cand = "BOUNCE-or-PASS-THROUGH"
        else:
            cand = "UNRESOLVED-mixed"
        return {"label": label, "burst_fired": burst_fired, "mass_to_background": mass_to_bg,
                "peaks_x_final": peaks, "mass_final": mass_f, "mass_post_imprint": mass_b,
                "met": met, "had_approach": had_approach,
                "dilatation_rupture_enc": rw["dilatation_rupture_reached"],
                "dilatation_rupture_incl_build": rw.get("dilatation_rupture_reached_incl_build"),
                "cavitation_rupture": rw["cavitation_rupture_reached"],
                "candidate_bin": cand}

    a["classification"] = {n: classify(get(n), n) for n in
                           ("MAIN", "C-same-handed", "C-static-overlap", "C-no-approach")}
    return a


# ===================================================================== io
def _strip(v):
    if not isinstance(v, dict):
        return {"ERROR": repr(v)}
    out = dict(v)
    # decimate heavy per-step lists for the JSON (finals + series kept)
    return out


def _dump(results, t_start):
    out_json = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..", "..", "..", "research",
        "2026-06-11_annihilation-evaporation-run_results.json"))
    with open(out_json, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n[dump] {time.time()-t_start:.0f}s -> {out_json}", flush=True)


if __name__ == "__main__":
    main()
