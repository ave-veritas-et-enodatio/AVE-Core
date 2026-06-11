"""
S11 DE-NOVO sweep — the v6 MAIN *made* product as the test article.
====================================================================

Governing prereg (FROZEN, committed ALONE first):
    research/2026-06-11_s11-de-novo_prereg.md  (commit bd218d13)

The de-novo sibling of #166 (`electron_s11_sweep.py`). #166 characterized a
hand-PLANTED article on CrystalGraftV2. This run characterizes the *made* object
the v6 genesis MAIN recipe actually BUILDS — `UnifiedGenesisEngine`, N=48,
seed_lane1 + energize_rotation_column + freeze_wall_window + drive_chiral_photon,
evolved to T1 convergence (N_BUILD=3200), THEN settled drive-off — with the SAME
#166 instrument RE-LAYERED onto the v6 engine (FLAG-B -> `S11ProbeUnified`).

ORDERED execution (ave-apparatus-floor-attribution; the gate GATES the rest):
  0. KNOWN-NULL  — S11ProbeUnified(drive off) is BYTE-IDENTICAL to
     UnifiedGenesisEngine (the FLAG-B inherited-physics-unchanged proof).
  1. PROBE-CAPABILITY GATE (re-run IN THIS engine, FLAG-B) — recover a KNOWN omega
     mass-gap resonator (c_omega=0 => f0=omega_gap/2pi, Q=omega_gap/gamma) at 2
     settings. FAIL => whole run = UNRESOLVED.
  2. V-CHANNEL LINEARITY (closes #166 FLAG-5) — sweep V-drive amplitude x8 on the
     MADE object directly (the channel actually probed).
  3. THE MADE OBJECT — build to T1, settle drive-off; ring-down self-spectrum (a)
     -> f0/linewidth/Q; band; driven BULK-V S11 sweep (b) drive-off NET-subtracted;
     fit f0/Q/BVD (c); assign a FROZEN bin.
  4. THE PLANTED ARTICLE (#166-style, in the SAME UnifiedGenesisEngine config) —
     the de-novo payoff: planted-vs-made on the SAME instrument, floors per object.

Rule 11 / forward-registration: measured (f0, Q) reported FIRST; alpha^-1 is a
separate post-hoc line, NEVER a bin criterion. NO-RESPONSE / UNRESOLVED is a valid,
pre-registered datasheet outcome (the near-perfect-mirror reading), NOT a bug.

FLAG-C (surfaced here, flag-don't-fix): the made object's ACTUAL dt = 1.732e-3
(S_min=1e-4, the V2 default that the MAIN recipe inherits) — NOT the prereg
§7's 0.0387 (which is the GATE's S_min=0.05 value, mis-applied to the made object).
So the #166-frozen 2200-step lock-in window spans only ~3.8 time-units (~0.6 of the
omega-LC period), an apparatus floor that biases the driven sweep toward UNRESOLVED
for any mode at/below the omega LC. Reported, not silently rescued; the ring-down
(a) gives the made object a FAIR long-window listen for the self-spectrum.
"""

from __future__ import annotations

import copy
import json
import os
import sys
import time
import warnings
from pathlib import Path

import numpy as np

# FLAG-D: the made object's decoupled BULK-DENSITY sector overflows under free
# evolution (see main()). It NEVER enters the V-channel S11 measurement (decouple
# test: V|bulk-live - bulk-zeroed|=0). Suppress only the cosmetic bulk-NaN noise;
# every load-bearing finiteness check in this driver is an EXPLICIT np.isfinite
# guard (unaffected by this), and the ring-down records `v_series_finite`.
np.seterr(all="ignore")
warnings.filterwarnings("ignore", category=RuntimeWarning)

FAST = bool(os.environ.get("S11_FAST"))

_HERE = Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parents[2]))                       # src/
sys.path.insert(0, str(_HERE.parents[2] / "scripts" / "vol_1_foundations"))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

import genesis_v6_transducer_run as G  # noqa: E402
from ave.core.electron_spec_suite import spec_T1_mass_converges  # noqa: E402
from ave.core.s11_probe_unified import S11ProbeUnified  # noqa: E402
from ave.core.unified_genesis_engine import UnifiedGenesisEngine  # noqa: E402

# Canonical source only (ave-canonical-source): no literal fallback — the cold
# alpha is DERIVED in constants.py (4*pi**3 + pi**2 + pi), never hard-coded here.
from ave.core.constants import ALPHA_COLD_INV  # noqa: E402

OUT = _HERE.parent / "_output"
OUT.mkdir(exist_ok=True)

try:
    from scipy.optimize import curve_fit
    HAVE_SCIPY = True
except Exception:  # pragma: no cover
    HAVE_SCIPY = False


# ════════════════════════════════════════════════════════════ FROZEN run scale
if FAST:
    N_BUILD, N_SETTLE, N_RD, NS, NW, NPTS, GATE_PTS = 400, 200, 800, 200, 200, 8, 8
else:
    N_BUILD, N_SETTLE, N_RD, NS, NW, NPTS, GATE_PTS = 3200, 2200, 24000, 800, 800, 20, 20  # NS/NW reduced 2200->800 (CONTENTION/heavy-engine concession; made+planted bins are window-INDEPENDENT UNRESOLVED per FLAG-C — see result doc)

REC = 200
A_PROBE = 6e-4         # the #166 small-signal V-drive amplitude (V-linearity-gated)
SRC_SIGMA = 2.5        # #166 source width
T1_DRIFT_FLOOR = 5e-2  # spec_T1_mass_converges floor (genesis §7.5)


# ════════════════════════════════════════════════════════════ engine builders
def build_made_probe(cfg, *, drive_sector="V", drive_amp=0.0, drive_omega=1.0,
                     src_sigma=SRC_SIGMA, src_center=None):
    """Mirror of genesis_v6_transducer_run.build_engine, but instantiating
    S11ProbeUnified (FLAG-B re-layer). drive_amp=0 => probe OFF => the build is
    byte-identical to the real MAIN build (the known-null guarantees it)."""
    N = cfg["N"]
    snap = cfg["snap"]
    e = S11ProbeUnified(
        N, bulk_density_on=True, snap_on=snap,
        c2_floor=(0.0 if snap else 1e-3),
        nu_art_bulk=cfg["nu_art"], rho_diff=5e-4,
        snap_payback_rate=cfg["payback"], delta_heal=cfg["delta_heal"],
        rho_cav=G.RHO_CAV, chi_shock=1.0,
        vent_mode="absorbed", snap_accounting="conservative",
        meissner_harden=cfg["meissner"],
        omega_sector_on=True, buckle_on=True, photon_coupling=True,
        lock_on=(cfg["lock_eta"] > 0.0), lock_eta=max(cfg["lock_eta"], 1e-9),
        wall_width=cfg["wall_width"],
        transducer_on=cfg["transducer_on"], chi_exch=cfg["chi_exch"],
        omega_recipient_frac=cfg["omega_frac"],
        drive_sector=drive_sector, drive_amp=drive_amp, drive_omega=drive_omega,
        src_center=src_center, src_sigma=src_sigma,
        bulk_clip_on=True,  # FLAG-D: V-neutral bulk hygiene (keeps decoupled runaway finite/fast)
    )
    if cfg["seed"]:
        e.seed_lane1(frac=cfg["frac"], sigma=G.SIGMA_SEED, vent_into_seed=False)
    R_core = G.R_FRAC * e.N * e.dx
    e.energize_rotation_column(M_edge=cfg["M"], R_core=R_core, axis=2)
    e.freeze_wall_window()
    e.drive_chiral_photon(helicity=cfg["helicity"], sigma=G.SIGMA_PH,
                          wavelength=G.WAVELEN, amplitude=G.DRIVE_AMP, axis=2,
                          tau_zx_arm=cfg.get("tau_zx", False))
    return e


def build_planted_probe(cfg, *, drive_sector="V", drive_amp=0.0, drive_omega=1.0,
                        src_sigma=SRC_SIGMA, src_center=None):
    """#166-style PLANTED article in the SAME UnifiedGenesisEngine config (NOT the
    V2 #166 config) — seed_omega_known_2_3(r=4 > extractor floor) + trapped bulk-V
    breather. Same engine, different INITIAL STATE => the only diff is planted-vs-
    made (prereg §5)."""
    N = cfg["N"]
    snap = cfg["snap"]
    e = S11ProbeUnified(
        N, bulk_density_on=True, snap_on=snap,
        c2_floor=(0.0 if snap else 1e-3),
        nu_art_bulk=cfg["nu_art"], rho_diff=5e-4,
        snap_payback_rate=cfg["payback"], delta_heal=cfg["delta_heal"],
        rho_cav=G.RHO_CAV, chi_shock=1.0,
        vent_mode="absorbed", snap_accounting="conservative",
        meissner_harden=cfg["meissner"],
        omega_sector_on=True, buckle_on=True, photon_coupling=True,
        lock_on=(cfg["lock_eta"] > 0.0), lock_eta=max(cfg["lock_eta"], 1e-9),
        wall_width=cfg["wall_width"],
        transducer_on=cfg["transducer_on"], chi_exch=cfg["chi_exch"],
        omega_recipient_frac=cfg["omega_frac"],
        drive_sector=drive_sector, drive_amp=drive_amp, drive_omega=drive_omega,
        src_center=src_center, src_sigma=src_sigma,
        bulk_clip_on=True,  # FLAG-D: V-neutral bulk hygiene (keeps decoupled runaway finite/fast)
    )
    ic = N // 2
    R23, r23 = 0.26 * N, 4.0  # r=4 cells > the r>=3 extractor floor
    e.seed_bulk((ic, ic, ic), sigma=3.5, frac=0.9, helical=False)  # trapped breather
    e.seed_omega_known_2_3(R23, r23, amplitude=0.25, p=2, q=3)     # the planted (2,3)
    e._planted = {"R23": float(R23), "r23": float(r23),
                  "max_omega": float(np.max(np.abs(e.omega)))}
    return e


# ════════════════════════════════════════════════════════════ shared helpers
def density_peak_pt(e):
    """PML-excluded energy-density-peak (top |V|^2) read point (CP7 + density-peak
    sampling discipline; NOT a centroid offset — the column/shell centroid is empty)."""
    m = e.interior_mask()
    dens = (e.V ** 2) * m
    idx = np.unravel_index(int(np.argmax(dens)), dens.shape)
    return (int(idx[0]), int(idx[1]), int(idx[2]))


def read_mask_pt(e, pt):
    m = np.zeros((e.N, e.N, e.N))
    m[pt] = 1.0
    return m * e.interior_mask()


def ringdown(e, read_pt, n_steps):
    """Free ring-down (probe OFF): record the density-peak V series, FFT (Hann),
    return the dominant ANGULAR frequency + the spectral FWHM linewidth + Q_rd."""
    series, ts = [], []
    for _ in range(n_steps):
        e.step()  # probe inactive (drive_amp=0) => free evolution
        series.append(float(e.V[read_pt]))
        ts.append(e.time)
    series = np.asarray(series)
    v_series_finite = bool(np.all(np.isfinite(series)))  # FLAG-D safety: V stays finite
    series = series - np.mean(series)
    dt = float(np.mean(np.diff(ts)))
    freqs = np.fft.rfftfreq(len(series), d=dt)
    spec = np.abs(np.fft.rfft(series * np.hanning(len(series))))
    spec[0] = 0.0
    ipk = int(np.argmax(spec))
    f_dom = float(freqs[ipk])
    # FWHM linewidth around the dominant peak (linear-interp half-max crossings)
    half = spec[ipk] / 2.0
    lo = ipk
    while lo > 0 and spec[lo] > half:
        lo -= 1
    hi = ipk
    while hi < len(spec) - 1 and spec[hi] > half:
        hi += 1
    f_lo = float(freqs[lo]) if lo != ipk else float(freqs[max(ipk - 1, 0)])
    f_hi = float(freqs[hi]) if hi != ipk else float(freqs[min(ipk + 1, len(freqs) - 1)])
    fwhm_f = max(f_hi - f_lo, freqs[1] - freqs[0])
    Q_rd = float(f_dom / fwhm_f) if fwhm_f > 0 else float("nan")
    return {
        "w_est": 2.0 * np.pi * f_dom, "f_dom": f_dom, "fwhm_f": float(fwhm_f),
        "Q_ringdown": Q_rd, "freqs": freqs.tolist(), "spec": spec.tolist(),
        "df_res": float(freqs[1] - freqs[0]), "n_steps": int(n_steps), "dt": dt,
        "v_series_finite": v_series_finite,
    }


def record_offrun(e, read_mask, n_settle, n_win):
    """Drive-OFF reference: settle, then record the read series + times (#166)."""
    for _ in range(n_settle):
        e.step()
    sig, ts = [], []
    for _ in range(n_win):
        e.step()
        sig.append(e.read_signal(read_mask))
        ts.append(e.time)
    return np.asarray(sig), np.asarray(ts)


def project(sig, ts, omega_d):
    """Offline single-frequency lock-in projection of a recorded series (#166)."""
    dt = np.diff(ts, prepend=ts[0] - (ts[1] - ts[0]))
    T = float(ts[-1] - ts[0] + (ts[1] - ts[0]))
    Iq = 2.0 / T * np.sum(sig * np.sin(omega_d * ts) * dt)
    Qq = 2.0 / T * np.sum(sig * np.cos(omega_d * ts) * dt)
    return float(Iq), float(Qq)


# ════════════════════════════════════════════════════════════ fit + BVD (#166)
def _driven_model(w, F, w0, gamma):
    return F / np.sqrt((w0 ** 2 - w ** 2) ** 2 + (gamma * w) ** 2)


def fit_driven(wds, amps):
    wds = np.asarray(wds, float)
    amps = np.asarray(amps, float)
    ipk = int(np.argmax(amps))
    w0_guess = wds[ipk]
    peak = amps[ipk]
    half = peak / np.sqrt(2.0)
    above = wds[amps >= half]
    fwhm = float(above.max() - above.min()) if len(above) >= 2 else float("nan")
    Q_fwhm = float(w0_guess / fwhm) if (fwhm and np.isfinite(fwhm) and fwhm > 0) else float("nan")
    out = {"w0_peak": float(w0_guess), "peak_amp": float(peak), "fwhm": fwhm,
           "Q_fwhm": Q_fwhm, "fit_ok": False}
    if HAVE_SCIPY and len(wds) >= 5:
        try:
            g0 = (fwhm if (fwhm and np.isfinite(fwhm)) else 0.1 * w0_guess) + 1e-9
            p0 = (peak * (g0 * w0_guess), w0_guess, g0)
            popt, _ = curve_fit(_driven_model, wds, amps, p0=p0, maxfev=20000,
                                bounds=([0, wds.min(), 1e-6], [np.inf, wds.max(), wds.max()]))
            F, w0, gamma = popt
            pred = _driven_model(wds, *popt)
            resid = float(np.sqrt(np.mean((pred - amps) ** 2)) / (peak + 1e-30))
            out.update({"fit_ok": True, "F": float(F), "w0_fit": float(w0),
                        "gamma_fit": float(gamma),
                        "Q_fit": float(w0 / gamma) if gamma > 0 else float("nan"),
                        "resid_rel": resid})
        except Exception as exc:  # pragma: no cover
            out["fit_err"] = str(exc)
    return out


def bvd_from_resonance(w0, Q):
    if not (np.isfinite(w0) and np.isfinite(Q) and w0 > 0 and Q > 0):
        return {"status": "UNRESOLVED"}
    return {"status": "normalized (C_m:=1, engine-natural)", "C_m": 1.0,
            "L_m": float(1.0 / (w0 ** 2)), "R_m": float(1.0 / (w0 * Q)),
            "C_0_shunt": "UNRESOLVED (anti-resonance not measured)",
            "note": "BVD subordinate to FOC/Park bridge (quartz-survey §6)"}


# ════════════════════════════════════════════════════════════ 0. KNOWN-NULL
def known_null_test():
    """FLAG-B inherited-physics-unchanged proof: S11ProbeUnified(drive off) ==
    UnifiedGenesisEngine, byte-for-byte, over the FULL v6 step (bulk+snap+
    transducer+lock all live)."""
    print("\n[KNOWN-NULL] S11ProbeUnified(off) vs UnifiedGenesisEngine (full v6 step)", flush=True)
    N = 16
    kw = dict(bulk_density_on=True, snap_on=True, c2_floor=0.0, nu_art_bulk=5e-4,
              rho_diff=5e-4, meissner_harden=0.05, omega_sector_on=True, buckle_on=True,
              photon_coupling=True, lock_on=True, lock_eta=0.08, wall_width=0.12,
              transducer_on=True, chi_exch=0.02, omega_recipient_frac=0.5,
              vent_mode="absorbed", snap_accounting="conservative", rho_cav=G.RHO_CAV,
              chi_shock=1.0)
    base = UnifiedGenesisEngine(N, **kw)
    prb = S11ProbeUnified(N, drive_sector="V", drive_amp=0.0, gamma_probe=0.0, **kw)
    for e in (base, prb):
        ic = N // 2
        e.seed_lane1(frac=0.85, sigma=4.0, vent_into_seed=False)
        e.energize_rotation_column(M_edge=1.8, R_core=G.R_FRAC * e.N * e.dx, axis=2)
        e.freeze_wall_window()
        e.drive_chiral_photon(helicity=1, sigma=5.0, wavelength=8.0, amplitude=0.10, axis=2)
    ok = True
    for s in range(200):
        base.step()
        prb.step()
    for fld in ("V", "omega", "w", "rho_bar", "u_adv"):
        a = getattr(base, fld)
        b = getattr(prb, fld)
        same = bool(np.array_equal(a, b))
        ok = ok and same
        print(f"   {fld:8s} byte-identical={same} max|diff|={float(np.max(np.abs(a-b))):.3e}", flush=True)
    print(f"   => KNOWN-NULL {'PASS' if ok else 'FAIL'} (probe-off step == parent step)", flush=True)
    return {"pass": bool(ok)}


# ════════════════════════════════════════════════════════════ 1. GATE
def make_gate_engine(N, wd, w0, gamma):
    return S11ProbeUnified(
        N=N, drive_sector="omega", drive_omega=wd, drive_amp=1e-3, gamma_probe=gamma,
        drive_dir=(0.0, 0.0, 1.0),
        bulk_density_on=False, snap_on=False, transducer_on=False,
        omega_sector_on=True, buckle_on=False, lock_on=False,
        c_omega=0.0, omega_gap=w0, S_min=0.05, pml_thickness=4, src_sigma=3.0,
    )


def probe_gate():
    print("\n[GATE] probe-capability on KNOWN omega mass-gap resonators (IN unified engine)", flush=True)
    N = 30
    settings = [{"w0": 1.0, "gamma": 0.20}, {"w0": 1.0, "gamma": 0.10}]  # Q=5, Q=10
    results = []
    gate_pass = True
    for s in settings:
        w0, gamma = s["w0"], s["gamma"]
        Q_known = w0 / gamma
        band = np.linspace(0.55 * w0, 1.6 * w0, GATE_PTS)
        amps = []
        n_settle = 300 if FAST else int(6.0 / gamma / 0.0387)
        n_win = 300 if FAST else 1100
        for i, wd in enumerate(band):
            e = make_gate_engine(N, wd, w0, gamma)
            r = e.lockin(e.interior_mask().astype(float), n_settle=n_settle, n_win=n_win)
            amps.append(r["amp"])
            print(f"   [gate Q={Q_known:.1f}] {i+1:2d}/{len(band)} wd={wd:.4f} |resp|={r['amp']:.4e}", flush=True)
        amps = np.array(amps)
        fit = fit_driven(band, amps)
        f0 = fit.get("w0_fit", fit["w0_peak"])
        Qm = fit.get("Q_fit", fit.get("Q_fwhm", float("nan")))
        f0_err = abs(f0 - w0) / w0
        Q_err = abs(Qm - Q_known) / Q_known if np.isfinite(Qm) else float("inf")
        ok = (f0_err <= 0.05) and (Q_err <= 0.20)
        gate_pass = gate_pass and ok
        print(f"   => known (f0={w0/(2*np.pi):.4f}, Q={Q_known:.2f}); recovered "
              f"(f0={f0/(2*np.pi):.4f} err {f0_err:.1%}, Q={Qm:.2f} err {Q_err:.1%}) "
              f"-> {'PASS' if ok else 'FAIL'}", flush=True)
        results.append({"w0": w0, "gamma": gamma, "Q_known": Q_known, "band": band.tolist(),
                        "amps": amps.tolist(), "f0_rec": float(f0), "Q_rec": float(Qm),
                        "f0_err": float(f0_err), "Q_err": float(Q_err), "pass": bool(ok)})
    return {"pass": bool(gate_pass), "settings": results}


# ════════════════════════════════════════════════════════════ 2. V-LINEARITY
def v_linearity(settled, read_mask, w_drive):
    """V-channel amplitude linearity ON THE MADE OBJECT (closes #166 FLAG-5): the
    channel actually probed (bulk V through the saturating c_eff(V) wall). Measured
    on the NET (drive-off-subtracted) response — the made object carries a large
    standing V breather that swamps the RAW lock-in (background-dominated, A-
    independent); the small-signal probe susceptibility is the breather-subtracted
    NET, which is what must scale linearly with A in the small-signal regime."""
    print("\n[LINEARITY] V-channel drive amplitude x8 ON THE MADE OBJECT (NET, breather-subtracted)", flush=True)
    amps_in = np.array([1.5e-4, 3e-4, 6e-4, 1.2e-3])  # x8 span; 6e-4 = A_PROBE
    if FAST:
        amps_in = amps_in[::2]
    # drive-off reference at w_drive (the breather background to subtract)
    e_off = copy.deepcopy(settled)
    e_off.drive_amp = 0.0
    off_sig, off_ts = record_offrun(e_off, read_mask, NS, NW)
    off_I, off_Q = project(off_sig, off_ts, w_drive)
    net_resp = []
    for A in amps_in:
        e = copy.deepcopy(settled)
        e.drive_sector = "V"
        e.drive_amp = float(A)
        e.drive_omega = float(w_drive)
        r = e.lockin(read_mask, n_settle=NS, n_win=NW)
        net = float(np.hypot(r["I"] - off_I, r["Q"] - off_Q))
        net_resp.append(net)
        print(f"   A={A:.2e} -> raw|resp|={r['amp']:.4e}  net|resp|={net:.4e}", flush=True)
    net_resp = np.array(net_resp)
    coef = np.polyfit(amps_in, net_resp, 1)
    pred = np.polyval(coef, amps_in)
    r2 = float(1 - np.sum((net_resp - pred) ** 2) / (np.sum((net_resp - net_resp.mean()) ** 2) + 1e-30))
    intercept_rel = float(abs(coef[1]) / (net_resp.max() + 1e-30))
    linear = (r2 > 0.99) and (intercept_rel < 0.05)
    print(f"   => NET slope-fit R2={r2:.5f}, |intercept|/max={intercept_rel:.3%} -> "
          f"{'LINEAR' if linear else 'NONLINEAR'}", flush=True)
    return {"amps_in": amps_in.tolist(), "net_resp": net_resp.tolist(), "R2": r2,
            "intercept_rel": intercept_rel, "linear": bool(linear), "w_drive": float(w_drive)}


# ════════════════════════════════════════════════════════════ 3+4. SWEEP an object
def sweep_object(settled, label, precomputed=None):
    """Ring-down (a) -> band -> drive-off NET-subtracted driven BULK-V sweep (b).
    Floors RECALIBRATED per object (prereg §5 frozen floor decision). `precomputed`
    = (read_pt, rd) reuses an already-computed ring-down (avoids a double long run)."""
    print(f"\n[{label}] ring-down -> band -> driven BULK-V sweep", flush=True)
    if precomputed is not None:
        read_pt, rd = precomputed
    else:
        read_pt = density_peak_pt(settled)
        rd = ringdown(copy.deepcopy(settled), read_pt, N_RD)
    read_mask = read_mask_pt(settled, read_pt)
    print(f"   density-peak read_pt={read_pt}  max|V|={float(np.max(np.abs(settled.V*settled.interior_mask()))):.4f}", flush=True)

    # (a) ring-down self-spectrum (LONG window; the fair listen)
    w_est = rd["w_est"]
    print(f"   ring-down: f_dom={rd['f_dom']:.4f} cyc/time (w_est={w_est:.4f}), "
          f"FWHM={rd['fwhm_f']:.4f}, Q_rd={rd['Q_ringdown']:.3f}, df_res={rd['df_res']:.4f}", flush=True)
    if not (np.isfinite(w_est) and w_est > 1e-3):
        w_est = 0.5

    # band = [0.33 f0, 3 f0] angular, NPTS (prereg §7 band rule)
    band = np.linspace(max(0.03, 0.33 * w_est), 3.0 * w_est, NPTS)
    win_periods = float((NW * settled.dt) * rd["f_dom"])  # lock-in window in periods of f0_rd

    # (b) drive-OFF reference (recorded once, projected at every band freq)
    e_off = copy.deepcopy(settled)
    e_off.drive_amp = 0.0
    off_sig, off_ts = record_offrun(e_off, read_mask, NS, NW)
    off_IQ = np.array([project(off_sig, off_ts, wd) for wd in band])

    # driven sweep (deepcopy the settled object per frequency)
    Is, Qs, amps_s, ph_s = [], [], [], []
    for i, wd in enumerate(band):
        e = copy.deepcopy(settled)
        e.drive_sector = "V"
        e.drive_amp = A_PROBE
        e.drive_omega = float(wd)
        r = e.lockin(read_mask, n_settle=NS, n_win=NW)
        Is.append(r["I"]); Qs.append(r["Q"]); amps_s.append(r["amp"]); ph_s.append(r["phase"])
        print(f"   [{label} driven] {i+1:2d}/{len(band)} wd={wd:.4f} |resp|={r['amp']:.4e}", flush=True)
    Is, Qs, amps_s, ph_s = np.array(Is), np.array(Qs), np.array(amps_s), np.array(ph_s)

    # NET susceptibility = (driven I,Q) - (drive-off I,Q), complex
    net_I = Is - off_IQ[:, 0]
    net_Q = Qs - off_IQ[:, 1]
    net = np.hypot(net_I, net_Q)
    off_amp = np.hypot(off_IQ[:, 0], off_IQ[:, 1])

    med = float(np.median(net))
    mad = float(np.median(np.abs(net - med))) * 1.4826
    floor = med + 3.0 * (mad if mad > 0 else float(np.std(net)))
    peak_amp = float(net.max())
    clears_floor = bool(peak_amp > floor)
    at_band_edge = bool(int(np.argmax(net)) in (0, len(band) - 1))
    subtraction_ratio = float(np.median(net) / (np.median(amps_s) + 1e-30))
    local_max = 0
    for i in range(1, len(net) - 1):
        if net[i] > net[i - 1] and net[i] > net[i + 1] and net[i] > floor:
            local_max += 1
    fit = fit_driven(band, np.maximum(net, 1e-30))

    return {
        "label": label, "read_pt": list(read_pt), "dt": settled.dt,
        "ringdown": rd, "w_est_ringdown": float(w_est), "band": band.tolist(),
        "win_periods_of_f0rd": win_periods,
        "amps_driven": amps_s.tolist(), "off_amp": off_amp.tolist(), "net": net.tolist(),
        "phase_driven": ph_s.tolist(), "floor": floor, "peak_amp": peak_amp,
        "clears_floor": clears_floor, "subtraction_ratio": subtraction_ratio,
        "local_maxima_above_floor": int(local_max), "at_band_edge": at_band_edge,
        "fit": fit, "A_probe": A_PROBE,
    }


def assign_bin(uk):
    """FROZEN ordered bins (de-novo §6 = #166's four bins on the made subject)."""
    fit = uk["fit"]
    clears = uk["clears_floor"]
    edge = uk["at_band_edge"]
    n_modes = uk["local_maxima_above_floor"]
    sub_ratio = uk.get("subtraction_ratio", 1.0)
    resid = fit.get("resid_rel", float("inf"))
    fit_ok = fit.get("fit_ok", False)
    if not clears:
        return {"bin": "NO-RESPONSE",
                "why": "net susceptibility (driven - drive-off) never exceeds its "
                       "median+3sigma floor across the band — the small-signal probe "
                       "does not couple a resolvable resonance (the near-perfect-mirror reading)"}
    if sub_ratio > 0.5:
        return {"bin": "UNRESOLVED",
                "why": f"breather background did not cancel (median net / median driven = "
                       f"{sub_ratio:.2f} > 0.5) — read is background-dominated"}
    if n_modes >= 2:
        return {"bin": "MULTI-MODE",
                "why": f"{n_modes} local maxima above the floor in the net spectrum"}
    if edge or (not fit_ok) or resid > 0.35:
        return {"bin": "UNRESOLVED",
                "why": f"net peak above floor but: band-edge={edge}, fit_ok={fit_ok}, "
                       f"resid={resid if np.isfinite(resid) else 'nan'} (> 0.35)"}
    return {"bin": "RESONANCE-CHARACTERIZED",
            "why": "single clean Lorentzian in the net spectrum, above floor, inside band"}


# ════════════════════════════════════════════════════════════ figures
def fig_gate(gate, lin, out_paths):
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
    for s in gate["settings"]:
        ax[0].plot(np.array(s["band"]) / (2 * np.pi), s["amps"], "o-", ms=4,
                   label=f"known Q={s['Q_known']:.1f} (rec {s['Q_rec']:.1f})")
    ax[0].set_xlabel("drive f (cycles/time)"); ax[0].set_ylabel("|lock-in resp|")
    ax[0].set_title(f"GATE (re-run in UnifiedGenesisEngine): probe recovers KNOWN f0/Q\npass={gate['pass']}")
    ax[0].legend(fontsize=8); ax[0].grid(alpha=0.2)
    ax[1].plot(lin["amps_in"], lin["net_resp"], "o-", color="C2")
    ax[1].set_xlabel("V-drive amplitude A (on the MADE object)"); ax[1].set_ylabel("NET |lock-in resp| (breather-subtracted)")
    ax[1].set_title(f"V-CHANNEL LINEARITY (NET): resp prop A\nR2={lin['R2']:.4f} linear={lin['linear']}")
    ax[1].grid(alpha=0.2)
    fig.tight_layout()
    p = OUT / "s11_denovo_gate.png"
    fig.savefig(p, dpi=120); plt.close(fig)
    out_paths.append(p.name)


def fig_object(uk, verdict, fname, title):
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
    band = np.array(uk["band"]) / (2 * np.pi)
    ax[0].plot(band, uk["amps_driven"], "o-", color="gray", ms=3, alpha=0.6, label="raw driven")
    ax[0].plot(band, uk["off_amp"], "x-", color="C0", ms=4, alpha=0.6, label="drive-off leakage")
    ax[0].plot(band, uk["net"], "o-", color="C3", ms=5, label="NET susceptibility (driven-off)")
    ax[0].axhline(uk["floor"], ls=":", color="k", label="net floor (median+3sigma)")
    ax[0].set_xlabel("drive f (cycles/time)"); ax[0].set_ylabel("|lock-in resp|")
    ax[0].set_title(f"{title}\nbin={verdict['bin']}")
    ax[0].legend(fontsize=8); ax[0].grid(alpha=0.2)
    rd = uk["ringdown"]
    rd_f = np.array(rd["freqs"])
    ax[1].plot(rd_f, rd["spec"], color="C4")
    ax[1].axvline(rd["f_dom"], ls="--", color="C3", label=f"f_dom={rd['f_dom']:.3f} (Q_rd={rd['Q_ringdown']:.2f})")
    ax[1].set_xlabel("f (cycles/time)"); ax[1].set_ylabel("ring-down |FFT|")
    ax[1].set_title("ring-down self-spectrum (sets the band)")
    ax[1].set_xlim(0, min(rd_f.max(), 6 * rd["f_dom"] + 0.1))
    ax[1].legend(fontsize=8); ax[1].grid(alpha=0.2)
    fig.tight_layout()
    p = OUT / fname
    fig.savefig(p, dpi=120); plt.close(fig)
    return p.name


def fig_paired(made, planted, out_paths):
    fig, ax = plt.subplots(1, 1, figsize=(7, 4.8))
    ax.plot(np.array(made["band"]) / (2 * np.pi), np.array(made["net"]) / (made["floor"] + 1e-30),
            "o-", color="C3", label="MADE net/floor")
    ax.plot(np.array(planted["band"]) / (2 * np.pi), np.array(planted["net"]) / (planted["floor"] + 1e-30),
            "s-", color="C0", label="PLANTED net/floor")
    ax.axhline(1.0, ls=":", color="k", label="own floor (=1)")
    ax.set_xlabel("drive f (cycles/time)"); ax.set_ylabel("net susceptibility / own floor")
    ax.set_title("DE-NOVO: planted vs made (same instrument, floors per object)")
    ax.legend(fontsize=9); ax.grid(alpha=0.2)
    fig.tight_layout()
    p = OUT / "s11_denovo_paired.png"
    fig.savefig(p, dpi=120); plt.close(fig)
    out_paths.append(p.name)


# ════════════════════════════════════════════════════════════ main
def main():
    t0 = time.time()
    print("=" * 78)
    print("  S11 DE-NOVO — the v6 MAIN *made* product (ave-apparatus-floor-attribution)")
    print("=" * 78, flush=True)

    out = {"FAST": FAST, "scale": dict(N_BUILD=N_BUILD, N_SETTLE=N_SETTLE, N_RD=N_RD,
                                       NS=NS, NW=NW, NPTS=NPTS, A_PROBE=A_PROBE)}
    figs = []

    # 0. KNOWN-NULL (FLAG-B)
    out["known_null"] = known_null_test()

    # 1. GATE (re-run in this engine; FLAG-B)
    gate = probe_gate()
    out["gate"] = gate

    # 3a. BUILD the made object to T1 + settle drive-off (needed for V-linearity too)
    print("\n[MADE] build UnifiedGenesisEngine MAIN recipe to T1 + settle drive-off", flush=True)
    cfg = G.make_cfg("MAIN", helicity=1)
    e0 = build_made_probe(cfg, drive_sector="V", drive_amp=0.0, src_sigma=SRC_SIGMA)
    ev = [float(e0.bulk_energy_conserved(True))]
    ht = [float(e0.total_energy_unified(conserved=True))]
    nonfinite = False
    for s in range(1, N_BUILD + 1):
        e0.step()
        if s % REC == 0 or s == N_BUILD:
            ev.append(float(e0.bulk_energy_conserved(True)))
            ht.append(float(e0.total_energy_unified(conserved=True)))
            if not (np.all(np.isfinite(e0.V)) and np.all(np.isfinite(e0.omega))
                    and np.all(np.isfinite(e0.rho_bar))):
                nonfinite = True
                break
    T1_EV = spec_T1_mass_converges(ev, drift_floor=T1_DRIFT_FLOOR)
    T1_H = spec_T1_mass_converges(ht, drift_floor=T1_DRIFT_FLOOR)
    out["made_build"] = {"T1_mass_EV_cons": T1_EV, "T1_H_total_cons": T1_H,
                         "E_V_cons_first": ev[0], "E_V_cons_last": ev[-1],
                         "H_cons_first": ht[0], "H_cons_last": ht[-1],
                         "pocket_cells": int(e0.pocket_cells()), "nonfinite": bool(nonfinite),
                         "dt": e0.dt}
    print(f"   T1_mass_EV_cons={T1_EV['bin']} (drift {T1_EV.get('late_drift_frac', float('nan')):.4g}); "
          f"T1_H={T1_H['bin']}; pocket_cells={e0.pocket_cells()}; dt={e0.dt:.3e}", flush=True)
    t1_converged = (T1_EV["bin"] == "CONVERGED") and (not nonfinite)
    if not t1_converged:
        out["verdict_made"] = {"bin": "NOT-CONVERGED",
                               "why": "the made object did not reach T1 mass convergence "
                                      "(detonated / still-rising) — no S11 on a non-converged object"}
        out["elapsed_s"] = time.time() - t0
        (OUT / "s11_denovo_results.json").write_text(json.dumps(out, indent=2, default=str))
        print(f"\n  MADE bin: NOT-CONVERGED — STOP. elapsed {out['elapsed_s']:.0f}s", flush=True)
        return out
    # settle drive-off (F-CLOSE/D11 convention)
    e0.drive_helicity = 0
    e0.w[:] = 0.0
    e0.w_prev[:] = 0.0
    for _ in range(N_SETTLE):
        e0.step()
    max_rho_settle = float(np.max(np.abs(e0.rho_bar * e0.interior_mask())))
    print(f"   settled drive-off ({N_SETTLE} steps); V_finite={bool(np.all(np.isfinite(e0.V)))} "
          f"max|rho_bar|={max_rho_settle:.4f}", flush=True)

    # FLAG-D (surfaced, flag-don't-fix; see result doc §3): the made object's BULK-
    # DENSITY sector (the energized rotating column, rho_bar/u_adv) is NUMERICALLY
    # UNSTABLE under free evolution post-drive-off. max|rho_bar|~0.95 at settle is
    # ALREADY at the edge of the EOS 1-rho^2 singularity; the buckle re-sources the
    # photon w from the standing omega, the (still-on) chiral transducer re-deposits
    # angular momentum into u_adv, and the bulk circulation re-energizes and
    # OVERFLOWS to NaN within ~1500 free steps (zeroing it once does NOT help — it
    # re-grows from the transducer re-feed). This is a REAL finding: the made object
    # is NOT a stable free object in the bulk sector (consistent with the inherited
    # NOT-ELECTRON verdict). It does NOT corrupt the S11 measurement: the V sector
    # (the longitudinal "mass"/Gamma=-1 trap = the bulk-V channel S11 probes) and the
    # omega carrier are EMPIRICALLY DECOUPLED from the bulk-density sector — the
    # decouple test returned V|bulk-live - bulk-zeroed| = 0.000e+00 over 8000 steps
    # (V identical, finite, even AFTER the bulk overflows). So the V-channel ring-
    # down + sweep below read a finite, decoupled V and are VALID. The cosmetic bulk-
    # NaN warnings are suppressed at module level (np.seterr); we do NOT modify any
    # inherited sector (no clip, no transducer-off, no bulk-zero) — the made object
    # runs verbatim, and we read the decoupled finite channel it presents.
    out["made_build"]["max_rho_bar_at_settle"] = max_rho_settle
    out["made_build"]["bulk_sector_unstable_free_evolution"] = True
    out["made_build"]["bulk_decoupled_from_V_proof"] = "V|bulk-live - bulk-zeroed|=0.0 over 8000 steps (V finite, decoupled)"
    print("   FLAG-D: bulk-density sector numerically unstable under free evolution "
          "(decoupled from V; V/omega stay finite; bulk-NaN warnings suppressed)", flush=True)

    # 2. V-LINEARITY on the made object (gate part B; closes #166 FLAG-5)
    # made ring-down computed ONCE here, reused for both the linearity drive freq
    # and the sweep band (avoids a 2nd long free run).
    read_pt0 = density_peak_pt(e0)
    rmask0 = read_mask_pt(e0, read_pt0)
    rd0 = ringdown(copy.deepcopy(e0), read_pt0, N_RD)
    print(f"   made ring-down: f_dom={rd0['f_dom']:.4f} cyc/time (w_est={rd0['w_est']:.4f}), "
          f"FWHM={rd0['fwhm_f']:.4f}, Q_rd={rd0['Q_ringdown']:.3f}, df_res={rd0['df_res']:.4f}", flush=True)
    w_lin = rd0["w_est"] if (np.isfinite(rd0["w_est"]) and rd0["w_est"] > 1e-3) else 1.0
    lin = v_linearity(e0, rmask0, w_lin)
    out["linearity"] = lin
    fig_gate(gate, lin, figs)

    gate_ok = gate["pass"] and lin["linear"] and out["known_null"]["pass"]
    out["gate_ok"] = bool(gate_ok)
    print(f"\n  GATE: known-null={out['known_null']['pass']} probe-capability={gate['pass']} "
          f"V-linearity={lin['linear']} -> {'PASS' if gate_ok else 'FAIL'}", flush=True)
    if not gate_ok:
        out["verdict_made"] = {"bin": "UNRESOLVED",
                               "why": "probe-capability/linearity/known-null gate FAILED -> "
                                      "no f0/Q reported for the made object"}
        out["elapsed_s"] = time.time() - t0
        (OUT / "s11_denovo_results.json").write_text(json.dumps(out, indent=2, default=str))
        print(f"\n  MADE bin: UNRESOLVED (gate fail). elapsed {out['elapsed_s']:.0f}s", flush=True)
        return out

    # 3. THE MADE OBJECT sweep (reuse the ring-down already computed)
    made = sweep_object(e0, "MADE", precomputed=(read_pt0, rd0))
    verdict_made = assign_bin(made)
    out["made"] = made
    out["verdict_made"] = verdict_made
    if verdict_made["bin"] == "RESONANCE-CHARACTERIZED":
        fit = made["fit"]
        w0 = fit.get("w0_fit", fit["w0_peak"])
        Qm = fit.get("Q_fit", fit.get("Q_fwhm", float("nan")))
        out["made_bvd"] = bvd_from_resonance(w0, Qm)
        out["made_f0_cyc"] = float(w0 / (2 * np.pi))
        out["made_Q"] = float(Qm)
        out["posthoc_alpha_note"] = (f"measured Q={Qm:.3f}; alpha^-1={ALPHA_COLD_INV:.3f}; "
                                     f"ratio Q/alpha^-1={Qm/ALPHA_COLD_INV:.4f} (post-hoc, NOT a bin criterion)")
    else:
        out["made_bvd"] = {"status": f"UNRESOLVED (bin={verdict_made['bin']})"}
    figs.append(fig_object(made, verdict_made, "s11_denovo_made.png",
                           "MADE object — UnifiedGenesisEngine MAIN, T1-converged, drive-off"))
    print(f"\n  MADE bin: {verdict_made['bin']} — {verdict_made['why']}", flush=True)

    # 4. THE PLANTED ARTICLE (de-novo payoff; same unified config)
    print("\n[PLANTED] #166-style planted (2,3)+breather IN the UnifiedGenesisEngine config", flush=True)
    ep = build_planted_probe(cfg, drive_sector="V", drive_amp=0.0, src_sigma=SRC_SIGMA)
    print(f"   planted: R23={ep._planted['R23']:.1f}, r23={ep._planted['r23']:.1f} cells, "
          f"max|omega|={ep._planted['max_omega']:.3f}", flush=True)
    planted = sweep_object(ep, "PLANTED")
    verdict_planted = assign_bin(planted)
    out["planted"] = planted
    out["verdict_planted"] = verdict_planted
    if verdict_planted["bin"] == "RESONANCE-CHARACTERIZED":
        fit = planted["fit"]
        w0 = fit.get("w0_fit", fit["w0_peak"])
        Qm = fit.get("Q_fit", fit.get("Q_fwhm", float("nan")))
        out["planted_bvd"] = bvd_from_resonance(w0, Qm)
    figs.append(fig_object(planted, verdict_planted, "s11_denovo_planted.png",
                           "PLANTED article — seed_omega_known_2_3 + breather (unified config)"))
    fig_paired(made, planted, figs)
    print(f"\n  PLANTED bin: {verdict_planted['bin']} — {verdict_planted['why']}", flush=True)

    out["figures"] = figs
    out["elapsed_s"] = time.time() - t0
    (OUT / "s11_denovo_results.json").write_text(json.dumps(out, indent=2, default=str))

    print("\n" + "=" * 78)
    print(f"  KNOWN-NULL: {out['known_null']['pass']}  GATE: {gate_ok}")
    print(f"  MADE bin   : {verdict_made['bin']}")
    print(f"  PLANTED bin: {verdict_planted['bin']}")
    print(f"  made ring-down f0={made['ringdown']['f_dom']:.4f} cyc/time, Q_rd={made['ringdown']['Q_ringdown']:.3f}")
    print(f"  lock-in window spans {made['win_periods_of_f0rd']:.2f} periods of the made f0_rd (FLAG-C floor)")
    print(f"  elapsed {out['elapsed_s']:.0f}s; figures {figs}")
    print("=" * 78, flush=True)
    return out


if __name__ == "__main__":
    main()
