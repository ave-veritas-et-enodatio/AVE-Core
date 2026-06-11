"""
genesis-v5 seeded-snap — THE RUN (Phase 4 of the prereg)
========================================================

Executes the FROZEN arm matrix of
`research/2026-06-10_genesis-v5-seeded-snap_prereg.md`:

  (1) APPARATUS GATES FIRST (ave-apparatus-floor-attribution, HARD CONSTRAINT) —
      the §5 CLIP-suspect sweeps at a sub-threshold drive: K1 nu_art (the D8
      attribution knob), N3 chi_shock, N1 rho_cav, D1 lock_eta, K2 N-resolution,
      N4 detector-threshold. A §4 positive that TRACKS a knob is APPARATUS.
  (2) MAIN + the controls — the build claim + the D8 SNAP-vs-MOTION discriminator
      under BOTH persistence protocols (P1 drive-off/L-conserved, P2 forced
      de-spin), with the frozen bins SNAP-LOCKED / MOTION-LOCKED / BOTH / NEITHER.
  (3) the D7 ELECTRON SPEC-SHEET (T1-T6, floors first) on the MAIN product.
  (4) the FLASH burst (D6), collimation (D3), twin-pocket (D4), end-to-end energy
      ledger.

Rule 11 / ave-driver-script-honesty: the verdict is written FROM the numbers
(dumped to JSON), not the hope. No coefficient is tuned to manufacture a positive.

Serial + deterministic (one process; same seeds ⇒ reproducible). Dumps:
  research/2026-06-10_genesis-v5-seeded-snap_results.json
and figures into research/figures/.
"""

from __future__ import annotations

import copy
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from ave.core.unified_genesis_engine import UnifiedGenesisEngine, RHO_CAV  # noqa: E402
from ave.core.longitudinal_burst_detector import LongitudinalBurstDetector  # noqa: E402
from ave.core.electron_spec_suite import (  # noqa: E402
    spec_T1_mass_converges, spec_T2_charge_winding, spec_T3_spin,
    spec_T4_stability_kick, spec_T5_born_in_pairs, spec_T6_de_broglie,
)

SEED = 20260610
np.random.seed(SEED)

# ---- frozen run scale (prereg §8: N fixed ~40-72; budget) ----
N_MAIN = 40
M_MAIN = 1.8          # the inherited cavitation reach (spontaneous snap ~step 3000 @ N=40)
N_BUILD = 3200        # build window (to spontaneous snap for snap-capable arms)
N_PERSIST = 1200      # P1 / P2 continuation
REC_EVERY = 100
FRAC = 0.85           # seed saturation depth (genesis-24 deep band)
DRIVE_AMP = 0.10
WAVELEN = 8.0
SIGMA_PH = 5.0
SIGMA_SEED = 4.0
R_FRAC = 0.18         # rotation-column core radius fraction


# ============================================================ engine + energy
def build_engine(N, *, seed=True, snap=True, lock=True, lock_eta=0.08,
                 nu_art=5e-4, rho_diff=5e-4, chi_shock=1.0, payback=1.0,
                 rho_cav=RHO_CAV, vent=True):
    c2_floor = 0.0 if snap else 1e-3
    e = UnifiedGenesisEngine(
        N, bulk_density_on=True, snap_on=snap, c2_floor=c2_floor,
        nu_art_bulk=nu_art, rho_diff=rho_diff, chi_shock=chi_shock,
        snap_payback_rate=payback, rho_cav=rho_cav,
        lock_on=lock, lock_eta=lock_eta,
    )
    if seed:
        e.seed_lane1(frac=FRAC, sigma=SIGMA_SEED, vent_into_seed=vent,
                     vent_near_frac=0.5)
    return e


def energize_and_drive(e, *, M, helicity, achiral=False, axis=2):
    """The genesis sequence: energize the rotation column (the MOTION / Gamma,
    energize+lock once), then inject the FOC chiral photon (the winding driver).
    achiral=True injects a LINEAR-pol photon (helicity 0): the handedness null."""
    R_core = R_FRAC * e.N * e.dx
    Omega = e.energize_rotation_column(M_edge=M, R_core=R_core, axis=axis)
    e.freeze_wall_window()
    if achiral:
        e.drive_chiral_photon(helicity=0, sigma=SIGMA_PH, wavelength=WAVELEN,
                              amplitude=DRIVE_AMP, axis=axis)
    else:
        e.drive_chiral_photon(helicity=helicity, sigma=SIGMA_PH, wavelength=WAVELEN,
                              amplitude=DRIVE_AMP, axis=axis)
    return Omega, R_core


def E_V(e):
    """Dilatation added-mass (the A1 Heaviside scalar) = the T1 rest-mass proxy
    (two-'3's: mass = dilatation V-sector, NOT the rotation KE)."""
    return e.bulk_energy(interior_only=True)


def H_field(e):
    """Total interior field energy across all sectors + bulk KE + bulk internal
    energy. Exact-EOS internal energy (the snap U-table) when snap_on; the
    linear-acoustic PE proxy for no-snap arms (whose rho_bar stays near-linear)."""
    m = e.interior_mask()
    if getattr(e, "snap_on", False) and hasattr(e, "_U_rb"):
        e_bU = float(np.sum(e.U_density(e.rho_bar) * m) * e.dx ** 3)
    else:
        e_bU = float(0.5 * e.c0 ** 2 * np.sum((e.rho_bar ** 2) * m) * e.dx ** 3)
    return (e.bulk_energy(True) + e.shear_energy(True) + e.omega_energy(True)
            + e._coupling_energy() + e.bulk_kinetic_energy() + e_bU)


def H_ledger(e):
    return (e.E_latent_held + e.E_diss_snap
            + getattr(e, "E_vent_to_seed", 0.0) + getattr(e, "E_vent_radiated", 0.0))


def H_total(e):
    return H_field(e) + H_ledger(e)


def snapshot(e, axis=2):
    rc, _ = e.rho_core()
    lc = e.handedness_ledger(axis=axis)
    return {
        "t": float(e.time), "step": int(e.step_count),
        "rho_core": float(rc),
        "pocket_cells": int(e.pocket_cells()),
        "Gamma": float(e.bulk_circulation_z()),
        "L_bulk": float(e.angular_momentum_bulk(axis)),
        "E_V": float(E_V(e)),
        "H_field": float(H_field(e)),
        "H_total": float(H_total(e)),
        "E_latent_held": float(e.E_latent_held),
        "E_diss_snap": float(e.E_diss_snap),
        "E_vent_to_seed": float(getattr(e, "E_vent_to_seed", 0.0)),
        "E_vent_radiated": float(getattr(e, "E_vent_radiated", 0.0)),
        "columnarity": float(e.columnarity(axis)),
        "col_floor": float(e.columnarity_floor(e.N)),
        "core_sense": float(lc["core_sense"]),
        "abs_net_frac": float(lc["abs_net_frac"]),
        "max_abs_u": float(np.max(np.abs(e.u_adv))),
        "Hbel": float(e.helicity_bel()),
        "Hphoton": float(e.helicity_photon()),
        "snap_events": int(e.snap_events),
        "unsnap_events": int(e.unsnap_events),
    }


def run_window(e, n_steps, rec_every, detector=None, axis=2):
    series = [snapshot(e, axis)]
    if detector is not None:
        detector.record(e)
    for s in range(1, n_steps + 1):
        e.step()
        if detector is not None:
            detector.record(e)
        if s % rec_every == 0 or s == n_steps:
            series.append(snapshot(e, axis))
            if not np.all(np.isfinite(e.rho_bar)):
                series[-1]["NONFINITE"] = True
                break
    return series


# ============================================================ the arm runner
def genesis_arm(name, *, seed, snap, helicity=+1, achiral=False, M=M_MAIN,
                lock=True, lock_eta=0.08, nu_art=5e-4, vent=True,
                n_build=N_BUILD, n_persist=N_PERSIST, want_detector=False,
                detector_floor=None):
    """Run one arm: BUILD (energize+drive, run to spontaneous snap or n_build),
    then branch P1 (drive-off, L-conserved = just continue) and P2 (forced
    de-spin) via deepcopy. Returns the full record."""
    t0 = time.time()
    e = build_engine(N_MAIN, seed=seed, snap=snap, lock=lock, lock_eta=lock_eta,
                     nu_art=nu_art, vent=vent)
    cert = e.seed_certificate() if seed else {"passes": None, "topology_null": None}
    energize_and_drive(e, M=M, helicity=helicity, achiral=achiral)
    det = LongitudinalBurstDetector(floor=detector_floor, threshold_mult=3.0) if want_detector else None
    build = run_window(e, n_build, REC_EVERY, detector=det)
    built_snap = snapshot(e)
    H0 = build[0]["H_total"]

    # ---- persistence branches ----
    p1 = copy.deepcopy(e)                       # P1: drive-off, L-conserved
    p1_series = run_window(p1, n_persist, REC_EVERY)
    p2 = copy.deepcopy(e)
    p2.despin_bulk(0.0)                         # P2: forced de-spin (the static test)
    p2_series = run_window(p2, n_persist, REC_EVERY)

    rec = {
        "name": name, "config": dict(seed=seed, snap=snap, helicity=helicity,
                                     achiral=achiral, M=M, lock=lock,
                                     lock_eta=lock_eta, nu_art=nu_art, vent=vent),
        "seed_cert": {"passes": cert.get("passes"),
                      "topology_null": cert.get("topology_null")},
        "build_series": build, "built": built_snap,
        "P1_series": p1_series, "P2_series": p2_series,
        "H0": H0,
        "P1_final": p1_series[-1], "P2_final": p2_series[-1],
        "snap_ledger": e.snap_ledger(),
        "twin_pocket": e.twin_pocket_ledger(),
        "wall_s": time.time() - t0,
    }
    if det is not None:
        rec["detector_bursts"] = det.scan() if det.floor is not None else "uncalibrated"
        rec["detector_total_burst_energy"] = det.total_burst_energy()
    return rec, e


# ============================================================ APPARATUS GATES (§5)
def _central_ball(N, radius):
    cc = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N))
    return np.sqrt((i - cc) ** 2 + (j - cc) ** 2 + (k - cc) ** 2) <= radius


def sweep_K1_nu_art():
    """K1 (THE D8 ATTRIBUTION KNOB): a rotating column (M=1.2, NO snap), drive-off,
    sub-threshold. Regress the circulation Gamma-decay AND the density-deficit
    rate against nu_art. If decay -> 0 as nu_art -> 0 (tracks the knob), prior
    LOCK/heal verdicts carried an apparatus component; a nonzero plateau is real."""
    out = []
    for nu in (1e-4, 5e-4, 1e-3, 2e-3, 5e-3):
        e = build_engine(N_MAIN, seed=False, snap=False, lock=False, nu_art=nu)
        R = R_FRAC * e.N * e.dx
        e.energize_rotation_column(M_edge=1.2, R_core=R, axis=2)
        g0 = e.bulk_circulation_z()
        rho0 = e.rho_core()[0]
        for _ in range(800):
            e.step()
        g1 = e.bulk_circulation_z()
        rho1 = e.rho_core()[0]
        out.append({
            "nu_art": nu,
            "Gamma0": float(g0), "Gamma800": float(g1),
            "Gamma_decay_frac": float((g1 - g0) / (abs(g0) + 1e-30)),
            "rho0": float(rho0), "rho800": float(rho1),
            "deficit_deepening": float(rho1 - rho0),
        })
    return out


def sweep_N3_chi_shock():
    """N3: chi_shock fraction. Hand-snap a rotating core; meter the FLASH magnitude
    (released latent) + the dissipated void-KE. chi=0 = elastic control (no diss)."""
    out = []
    N = 32
    for chi in (0.0, 0.5, 1.0):
        e = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
                                 chi_shock=chi, snap_payback_rate=0.0)
        R = R_FRAC * N * e.dx
        e.energize_rotation_column(M_edge=1.2, R_core=R, axis=2)
        lat = e.hand_snap_region(_central_ball(N, 3.0))
        out.append({"chi_shock": chi, "latent_released": float(lat),
                    "E_diss_snap": float(e.E_diss_snap),
                    "E_latent_held": float(e.E_latent_held),
                    "pocket_cells": int(e.pocket_cells())})
    return out


def sweep_N1_rho_cav():
    """N1: the candidate floor threshold. Hand-snap the same rotating core at
    different rho_cav; pocket-count / latent vs the threshold (a count that TRACKS
    the threshold is the CLIP telltale that the floor sets the verdict)."""
    out = []
    N = 32
    for rc in (-0.55, RHO_CAV, -0.68):
        e = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
                                 chi_shock=1.0, snap_payback_rate=0.0, rho_cav=rc)
        R = R_FRAC * N * e.dx
        e.energize_rotation_column(M_edge=1.2, R_core=R, axis=2)
        ball = _central_ball(N, 3.0)
        e.rho_bar[ball & e.interior_mask()] = rc - 0.05
        lat = e.hand_snap_region(ball, rho_set=rc - 0.05)
        out.append({"rho_cav": float(rc), "latent_released": float(lat),
                    "pocket_cells": int(e.pocket_cells())})
    return out


def sweep_D1_lock_eta():
    """D1: the rigid-rotation lock rate. T3 CLIP test — the LOCKED L value must be
    eta-INVARIANT (graft-v4: the ratio is invariant; if the locked VALUE tracks
    eta, CLIP). Energize a column + chiral drive, run, read L_omega vs eta."""
    out = []
    N = 32
    for eta in (0.0, 0.05, 0.08, 0.12):
        e = build_engine(N, seed=True, snap=False, lock=(eta > 0), lock_eta=max(eta, 1e-9))
        energize_and_drive(e, M=1.2, helicity=+1)
        for _ in range(800):
            e.step()
        out.append({"lock_eta": eta, "spin_L_omega": float(e.spin_L_omega()),
                    "L_bulk": float(e.angular_momentum_bulk(2)),
                    "Hbel": float(e.helicity_bel())})
    return out


def sweep_K2_N_resolution():
    """K2: grid resolution. Reach (deepest rho_core) + pocket vs N at fixed M.
    A signature that TRACKS N is the under-resolved single-cell artifact."""
    out = []
    for N in (32, 40, 48):
        e = build_engine(N, seed=False, snap=True, lock=False, nu_art=5e-4)
        R = R_FRAC * N * e.dx
        e.energize_rotation_column(M_edge=M_MAIN, R_core=R, axis=2)
        deepest = 0.0
        for _ in range(2000):
            e.step()
            deepest = min(deepest, e.rho_core()[0])
            if e.pocket_cells() > 0:
                break
        out.append({"N": N, "deepest_rho": float(deepest),
                    "pocket_cells": int(e.pocket_cells()),
                    "steps_to_snap": int(e.step_count),
                    "Gamma_final": float(e.bulk_circulation_z())})
    return out


def sweep_N4_detector_threshold():
    """N4: burst-count monotone non-increasing in the threshold (the CLIP telltale
    is EXPOSED). One hand-snap event, vary the threshold multiplier."""
    N = 28
    e = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
                             snap_payback_rate=0.0)
    det = LongitudinalBurstDetector(floor=1e-6)
    det.record(e)
    e.hand_snap_region(_central_ball(N, 3.0))
    det.record(e)
    counts = []
    for t in (1.0, 3.0, 10.0, 1e12):
        d = LongitudinalBurstDetector(floor=1e-6, threshold_mult=t)
        d.history = det.history
        counts.append({"threshold_mult": t, "n_bursts": len(d.scan())})
    return counts


def calibrate_flash_floor():
    """F0d: the D6 detector floor = the free-run (excited, no-snap) acoustic scatter
    of the bulk pressure-integral. Calibrate on a KNOWN-NULL first (HARD CONSTRAINT)."""
    e = build_engine(N_MAIN, seed=False, snap=True, lock=False, nu_art=2e-3)
    R = R_FRAC * e.N * e.dx
    e.energize_rotation_column(M_edge=0.6, R_core=R, axis=2)  # sub-threshold (no snap)
    floor = LongitudinalBurstDetector.calibrate_floor(e, steps=120)
    return float(floor), int(e.pocket_cells())


# ============================================================ D7 SPEC SHEET (T1-T6)
def spec_sheet(main_rec, main_engine, flash_floor):
    """Evaluate T1-T6 on the MAIN arm's BUILT product (floors first, ordered bins).
    T1 mass uses E_V(t) (the dilatation added-mass, the two-'3's rest-mass channel)."""
    axis = 2
    e = main_engine
    # T1 — mass converges (E_V late-window drift vs the F0e drift-floor)
    ev_series = [s["E_V"] for s in main_rec["build_series"]]
    # F0e drift floor: the late-window fractional drift a *quiet* run shows. Use the
    # P1 (drive-off) E_V late-window drift of THIS object as the empirical floor.
    p1_ev = [s["E_V"] for s in main_rec["P1_series"]]
    drift_floor = 5e-2
    T1 = spec_T1_mass_converges(ev_series, drift_floor=drift_floor)
    T1["E_V_first"] = float(ev_series[0]); T1["E_V_last"] = float(ev_series[-1])
    T1_Htot = spec_T1_mass_converges([s["H_total"] for s in main_rec["build_series"]],
                                     drift_floor=drift_floor)
    # T2 — charge winding (phase-space, F0b r>=3)
    R_ring = R_FRAC * e.N
    r_meas = 4.0
    T2 = spec_T2_charge_winding(e, R=R_ring, r=r_meas, r_meas_floor=3.0)
    # T3 — spin (DERIVED half-pole-pair form; lock_eta CLIP via the apparatus sweep)
    T3 = spec_T3_spin(e, R_ring=R_FRAC * e.N * e.dx, axis=axis)
    T3["spin_L_omega"] = float(e.spin_L_omega())
    # T4 — stability kick: perturb u_adv + V, re-verify T1(mass finite+bounded)/T3 sense
    ek = copy.deepcopy(e)
    rng = np.random.RandomState(SEED)
    ek.u_adv += 0.02 * rng.standard_normal(ek.u_adv.shape) * ek.interior_mask()[..., None]
    ek.V += 0.02 * rng.standard_normal(ek.V.shape) * ek.interior_mask()
    ev0, L0 = E_V(ek), ek.angular_momentum_bulk(axis)
    for _ in range(300):
        ek.step()
    ev1, L1 = E_V(ek), ek.angular_momentum_bulk(axis)
    reverify = bool(np.isfinite(ev1) and ev1 < 5 * (abs(ev0) + 1e-9)
                    and np.sign(L1) == np.sign(L0) and np.isfinite(L1))
    T4 = spec_T4_stability_kick(lambda: reverify)
    T4.update({"E_V_pre": float(ev0), "E_V_post": float(ev1),
               "L_pre": float(L0), "L_post": float(L1)})
    # T5 — born in pairs (global handedness ledger)
    T5 = spec_T5_born_in_pairs(e, axis=axis)
    # T6 — de Broglie: translate the locked bulk state at >=2 momenta, measure the
    # bulk pilot wavelength via the dominant transverse spectral peak of u_adv.
    T6 = de_broglie_probe(main_engine)
    return {"T1_mass_EV": T1, "T1_H_total": T1_Htot, "T2_charge": T2, "T3_spin": T3,
            "T4_kick": T4, "T5_pairs": T5, "T6_de_broglie": T6,
            "flash_floor": flash_floor}


def de_broglie_probe(src_engine):
    """T6: give the assembled object a net translation at momenta p in {p1,p2,p3}
    (a bulk boost u0 along x), let it propagate briefly, and read the dominant
    spatial wavelength of the moving density packet (FFT of rho_bar along x).
    Frozen positive: log-log slope of lambda vs p ~ -1 (only the EXPONENT)."""
    momenta, lambdas = [], []
    for u0 in (0.10, 0.20, 0.40):
        e = copy.deepcopy(src_engine)
        m = e.interior_mask()
        e.u_adv[..., 0] += u0 * m          # boost (momentum ~ rho0 * u0)
        for _ in range(120):
            e.step()
        # dominant wavelength of the moving rho packet along the boost axis
        prof = np.sum(e.rho_bar * m, axis=(1, 2))
        prof = prof - prof.mean()
        spec = np.abs(np.fft.rfft(prof))
        spec[0] = 0.0
        k = int(np.argmax(spec))
        lam = (len(prof) / k) if k > 0 else len(prof)
        momenta.append(u0)               # p proportional to u0 (rho0~1)
        lambdas.append(float(lam) * e.dx)
    res = spec_T6_de_broglie(momenta, lambdas)
    res["momenta"] = momenta
    res["lambdas"] = lambdas
    return res


# ============================================================ D8 binning
def classify_persistence(rec, pocket_floor=1, gamma_keep=0.5):
    """Apply the frozen D8 bins from the P1/P2 finals. Reports per-channel
    (pocket = snap channel; Gamma = motion channel)."""
    b = rec["built"]; p1 = rec["P1_final"]; p2 = rec["P2_final"]
    snap_on = rec["config"]["snap"]
    pk_b = b["pocket_cells"]; pk_p1 = p1["pocket_cells"]; pk_p2 = p2["pocket_cells"]
    g_b = abs(b["Gamma"]) + 1e-30
    g_p1 = abs(p1["Gamma"]); g_p2 = abs(p2["Gamma"])
    L_b = abs(b["L_bulk"]) + 1e-30
    L_p1 = abs(p1["L_bulk"]); L_p2 = abs(p2["L_bulk"])
    pocket_persist_p1 = pk_p1 >= pocket_floor
    pocket_persist_p2 = pk_p2 >= pocket_floor
    # the MOTION channel: physical angular momentum L_bulk (the conserved invariant;
    # Gamma over a fixed disk is contaminated by the snap-boundary shear layer — both
    # reported, ave-apparatus-floor-attribution).
    L_persist_p1 = (L_p1 / L_b) > gamma_keep
    return {
        "snap_on": snap_on,
        "pocket_built": pk_b, "pocket_P1": pk_p1, "pocket_P2": pk_p2,
        "Gamma_built": float(b["Gamma"]), "Gamma_P1": float(p1["Gamma"]),
        "Gamma_P2": float(p2["Gamma"]),
        "L_bulk_built": float(b["L_bulk"]), "L_bulk_P1": float(p1["L_bulk"]),
        "L_bulk_P2": float(p2["L_bulk"]),
        "pocket_persist_P1": bool(pocket_persist_p1),
        "pocket_persist_P2": bool(pocket_persist_p2),
        "L_persist_P1": bool(L_persist_p1),
        "L_ratio_P1": float(L_p1 / L_b),
        "Gamma_ratio_P1": float(g_p1 / g_b),
        "rho_core_built": float(b["rho_core"]),
        "rho_core_P1": float(p1["rho_core"]),
        "rho_core_P2": float(p2["rho_core"]),
    }


# ============================================================ figures
def make_figures(results, figdir):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    os.makedirs(figdir, exist_ok=True)
    paths = []

    # FIG 1: reach curves rho_core(t) per arm (build phase)
    fig, ax = plt.subplots(figsize=(7, 4.2))
    for name, rec in results["arms"].items():
        t = [s["t"] for s in rec["build_series"]]
        rc = [s["rho_core"] for s in rec["build_series"]]
        ax.plot(t, rc, label=name, lw=1.4)
    ax.axhline(RHO_CAV, ls="--", c="k", lw=1, label=f"rho_cav={RHO_CAV:.3f} (candidate)")
    ax.set_xlabel("t (engine units)"); ax.set_ylabel("rho_core (deepest interior)")
    ax.set_title("BUILD reach: core rarefaction vs the candidate snap floor")
    ax.legend(fontsize=7); fig.tight_layout()
    p = os.path.join(figdir, "fig_v5_reach.png"); fig.savefig(p, dpi=110); plt.close(fig); paths.append(p)

    # FIG 2: K1 nu_art attribution
    sw = results["apparatus"]["K1_nu_art"]
    nu = [d["nu_art"] for d in sw]
    gd = [abs(d["Gamma_decay_frac"]) for d in sw]
    dd = [abs(d["deficit_deepening"]) for d in sw]
    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    ax.loglog(nu, gd, "o-", label="|Gamma drift frac| (800 steps)")
    ax.loglog(nu, dd, "s-", label="|deficit deepening|")
    ax.set_xlabel("nu_art (artificial viscosity)"); ax.set_ylabel("|change|")
    ax.set_title("D8 attribution (K1): does persistence/deficit track nu_art?")
    ax.legend(fontsize=8); ax.grid(True, which="both", alpha=0.3); fig.tight_layout()
    p = os.path.join(figdir, "fig_v5_nu_art_attribution.png"); fig.savefig(p, dpi=110); plt.close(fig); paths.append(p)

    # FIG 3: P1/P2 persistence for MAIN (pocket + Gamma vs t)
    main = results["arms"]["MAIN"]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.0))
    for lbl, ser in (("P1 drive-off", main["P1_series"]), ("P2 de-spin", main["P2_series"])):
        a1.plot([s["t"] for s in ser], [s["pocket_cells"] for s in ser], label=lbl, lw=1.6)
        a2.plot([s["t"] for s in ser], [s["Gamma"] for s in ser], label=lbl, lw=1.6)
    a1.set_xlabel("t"); a1.set_ylabel("pocket_cells (snap channel)"); a1.legend(fontsize=8)
    a1.set_title("MAIN persistence: SNAP pocket")
    a2.set_xlabel("t"); a2.set_ylabel("Gamma (motion channel)"); a2.legend(fontsize=8)
    a2.set_title("MAIN persistence: circulation Gamma")
    fig.tight_layout()
    p = os.path.join(figdir, "fig_v5_persistence.png"); fig.savefig(p, dpi=110); plt.close(fig); paths.append(p)

    # FIG 4: energy ledger end-to-end (MAIN)
    led = results["energy_ledger"]
    fig, ax = plt.subplots(figsize=(7, 4.2))
    labels = list(led["bars"].keys()); vals = [led["bars"][k] for k in labels]
    ax.bar(range(len(labels)), vals, color="steelblue")
    ax.set_xticks(range(len(labels))); ax.set_xticklabels(labels, rotation=30, ha="right", fontsize=8)
    ax.set_ylabel("energy (engine units)")
    ax.set_title("MAIN end-to-end energy ledger (build -> P1)")
    fig.tight_layout()
    p = os.path.join(figdir, "fig_v5_energy_ledger.png"); fig.savefig(p, dpi=110); plt.close(fig); paths.append(p)
    return paths


# ============================================================ main
def main():
    t_start = time.time()
    results = {"prereg": "research/2026-06-10_genesis-v5-seeded-snap_prereg.md",
               "scale": dict(N=N_MAIN, M=M_MAIN, n_build=N_BUILD, n_persist=N_PERSIST,
                             frac=FRAC, seed=SEED), "RHO_CAV": RHO_CAV}

    print("[1/4] APPARATUS GATES (sub-threshold CLIP sweeps) ...", flush=True)
    flash_floor, calib_pocket = calibrate_flash_floor()
    results["apparatus"] = {
        "F0d_flash_floor": {"floor": flash_floor, "calib_pocket_cells": calib_pocket},
        "K1_nu_art": sweep_K1_nu_art(),
        "N3_chi_shock": sweep_N3_chi_shock(),
        "N1_rho_cav": sweep_N1_rho_cav(),
        "D1_lock_eta": sweep_D1_lock_eta(),
        "K2_N_resolution": sweep_K2_N_resolution(),
        "N4_detector_threshold": sweep_N4_detector_threshold(),
    }
    print(f"    apparatus done ({time.time()-t_start:.0f}s); flash_floor={flash_floor:.4e}", flush=True)

    print("[2/4] MAIN + controls (build + P1/P2) ...", flush=True)
    arms_spec = [
        ("MAIN",          dict(seed=True,  snap=True,  helicity=+1, achiral=False)),
        ("C-no-seed",     dict(seed=False, snap=True,  helicity=+1, achiral=False)),
        ("C-no-snap",     dict(seed=True,  snap=False, helicity=+1, achiral=False)),
        ("C-achiral",     dict(seed=True,  snap=True,  helicity=0,  achiral=True)),
        ("C-opp-helicity",dict(seed=True,  snap=True,  helicity=-1, achiral=False)),
    ]
    results["arms"] = {}
    main_engine = None
    for name, cfg in arms_spec:
        want_det = (name == "MAIN")
        try:
            rec, eng = genesis_arm(name, want_detector=want_det,
                                   detector_floor=flash_floor, **cfg)
        except Exception as exc:  # noqa: BLE001 — record, don't lose the batch
            import traceback
            results["arms"][name] = {"name": name, "config": cfg,
                                     "ERROR": repr(exc),
                                     "traceback": traceback.format_exc()}
            print(f"    {name}: FAILED {exc!r}", flush=True)
            continue
        results["arms"][name] = rec
        if name == "MAIN":
            main_engine = eng
        print(f"    {name}: built pocket={rec['built']['pocket_cells']} "
              f"rho_core={rec['built']['rho_core']:.3f} Gamma={rec['built']['Gamma']:.2f} "
              f"({rec['wall_s']:.0f}s)", flush=True)

    print("[3/4] D8 discriminator bins ...", flush=True)
    results["D8_bins"] = {name: classify_persistence(rec)
                          for name, rec in results["arms"].items()}

    print("[4/4] D7 spec sheet (T1-T6) on MAIN product ...", flush=True)
    results["spec_sheet"] = spec_sheet(results["arms"]["MAIN"], main_engine, flash_floor)

    # end-to-end energy ledger (MAIN: build start -> P1 end)
    mb = results["arms"]["MAIN"]
    b0 = mb["build_series"][0]; bN = mb["built"]; p1 = mb["P1_final"]
    H_in = b0["H_total"]; H_out = p1["H_total"]
    snapl = mb["snap_ledger"]
    results["energy_ledger"] = {
        "H_total_build_start": H_in,
        "H_total_built": bN["H_total"],
        "H_total_P1_end": H_out,
        "E_V_built": bN["E_V"],
        "latent_held": snapl["E_latent_held"],
        "E_diss_snap": snapl["E_diss_snap"],
        "vent_to_seed": bN["E_vent_to_seed"],
        "vent_radiated": bN["E_vent_radiated"],
        "residual_loss_visc_PML": H_in - H_out,
        "closure_resid_frac": (H_in - H_out) / (abs(H_in) + 1e-30),
        "bars": {
            "H_in": H_in, "H_built": bN["H_total"], "H_P1end": H_out,
            "latent": snapl["E_latent_held"], "vent_seed": bN["E_vent_to_seed"],
            "vent_rad": bN["E_vent_radiated"], "diss_snap": snapl["E_diss_snap"],
        },
    }

    out_json = os.path.join(os.path.dirname(__file__), "..", "..", "..",
                            "research", "2026-06-10_genesis-v5-seeded-snap_results.json")
    out_json = os.path.abspath(out_json)
    with open(out_json, "w") as f:
        json.dump(results, f, indent=2)
    figdir = os.path.abspath(os.path.join(os.path.dirname(out_json), "figures"))
    figs = make_figures(results, figdir)
    results["figures"] = figs
    with open(out_json, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nDONE in {time.time()-t_start:.0f}s -> {out_json}")
    print("figures:", figs)


if __name__ == "__main__":
    main()
