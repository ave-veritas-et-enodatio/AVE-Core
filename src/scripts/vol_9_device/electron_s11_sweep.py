"""
Electron S11 resonance sweep — the datasheet centerpiece.
=========================================================

Governing prereg (FROZEN, committed alone first):
    research/2026-06-10_electron-s11-sweep_prereg.md

ORDERED execution (ave-apparatus-floor-attribution):
  1. PROBE-CAPABILITY GATE — recover a KNOWN resonator (omega mass-gap
     driven-damped oscillator: c_omega=0 => f0=omega_gap/2pi exactly,
     Q=omega_gap/gamma_probe) at >=2 settings. FAIL => whole run = UNRESOLVED.
  2. LINEARITY SUB-GATE — response proportional to drive amplitude.
  3. THE UNKNOWN — plant the validated (2,3) winding (r above the r>=3 extractor
     floor) + a trapped bulk-V breather; drive a small-signal BULK probe across a
     band (set by a ring-down pre-scan); lock-in read the response spectrum;
     fit f0, Q, BVD; assign a FROZEN bin.

Rule 11 / forward-registration: the measured (f0, Q) are reported FIRST; the
alpha^-1 comparison is a separate post-hoc line, never a bin criterion. No
debugging toward a pretty resonance — a NO-RESPONSE / UNRESOLVED outcome is a
valid, pre-registered result and closes the datasheet Q row as UNTESTED.

ave-driver-script-honesty: every number from the evolved field; the lock-in fit
is reported with its residual; figures caption the actual data.
"""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

import numpy as np

# FAST = a reduced-scale end-to-end validation pass (S11_FAST=1); the full run
# (default) is the registered measurement. FAST only shrinks grids/windows.
FAST = bool(os.environ.get("S11_FAST"))

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from ave.core.constants import ALPHA_COLD_INV  # noqa: E402
from ave.core.s11_probe import S11Probe  # noqa: E402

OUT = Path(__file__).parent / "_output"
OUT.mkdir(exist_ok=True)

try:
    from scipy.optimize import curve_fit

    HAVE_SCIPY = True
except Exception:  # pragma: no cover
    HAVE_SCIPY = False


# ════════════════════════════════════════════════════════════ fit
def _driven_model(w, F, w0, gamma):
    """Steady amplitude of a driven damped oscillator:
    A(w) = F / sqrt((w0^2 - w^2)^2 + (gamma*w)^2). FWHM ~ gamma, Q = w0/gamma."""
    return F / np.sqrt((w0**2 - w**2) ** 2 + (gamma * w) ** 2)


def fit_driven(wds: np.ndarray, amps: np.ndarray) -> dict:
    """Fit the driven-damped-oscillator amplitude; return f0 (angular), Q, the
    relative fit residual, and a peak/FWHM fallback estimate."""
    wds = np.asarray(wds, float)
    amps = np.asarray(amps, float)
    ipk = int(np.argmax(amps))
    w0_guess = wds[ipk]
    peak = amps[ipk]
    # peak/FWHM fallback (model-free)
    half = peak / np.sqrt(2.0)
    above = wds[amps >= half]
    fwhm = float(above.max() - above.min()) if len(above) >= 2 else float("nan")
    Q_fwhm = float(w0_guess / fwhm) if (fwhm and np.isfinite(fwhm) and fwhm > 0) else float("nan")

    out = {
        "w0_peak": float(w0_guess),
        "peak_amp": float(peak),
        "fwhm": fwhm,
        "Q_fwhm": Q_fwhm,
        "fit_ok": False,
    }
    if HAVE_SCIPY and len(wds) >= 5:
        try:
            g0 = (fwhm if (fwhm and np.isfinite(fwhm)) else 0.1 * w0_guess) + 1e-9
            p0 = (peak * (g0 * w0_guess), w0_guess, g0)
            popt, _ = curve_fit(
                _driven_model, wds, amps, p0=p0, maxfev=20000,
                bounds=([0, wds.min(), 1e-6], [np.inf, wds.max(), wds.max()]),
            )
            F, w0, gamma = popt
            pred = _driven_model(wds, *popt)
            resid = float(np.sqrt(np.mean((pred - amps) ** 2)) / (peak + 1e-30))
            out.update(
                {
                    "fit_ok": True,
                    "F": float(F),
                    "w0_fit": float(w0),
                    "gamma_fit": float(gamma),
                    "Q_fit": float(w0 / gamma) if gamma > 0 else float("nan"),
                    "resid_rel": resid,
                }
            )
        except Exception as exc:  # pragma: no cover
            out["fit_err"] = str(exc)
    return out


def bvd_from_resonance(w0: float, Q: float) -> dict:
    """BVD motional arm in engine-natural NORMALIZED units (C_m := 1):
    L_m = 1/w0^2, R_m = 1/(w0*Q). Shunt C_0 (anti-resonance) is NOT measured
    here => UNRESOLVED. SUBORDINATE to FOC/Park (quartz-survey ruling)."""
    if not (np.isfinite(w0) and np.isfinite(Q) and w0 > 0 and Q > 0):
        return {"status": "UNRESOLVED"}
    Cm = 1.0
    Lm = 1.0 / (w0**2)
    Rm = 1.0 / (w0 * Q)
    return {
        "status": "normalized (C_m:=1, engine-natural)",
        "C_m": Cm,
        "L_m": float(Lm),
        "R_m": float(Rm),
        "C_0_shunt": "UNRESOLVED (anti-resonance not measured)",
        "note": "BVD subordinate to FOC/Park bridge (quartz-survey §6)",
    }


# ════════════════════════════════════════════════════════════ sweep helpers
def sweep(make_engine, wds, read_mask_of, n_settle, n_win, label=""):
    amps, phases, Is, Qs = [], [], [], []
    for i, wd in enumerate(wds):
        e = make_engine(wd)
        rm = read_mask_of(e)
        r = e.lockin(rm, n_settle=n_settle, n_win=n_win)
        amps.append(r["amp"])
        phases.append(r["phase"])
        Is.append(r["I"])
        Qs.append(r["Q"])
        print(f"   [{label}] {i + 1:2d}/{len(wds)} wd={wd:.4f} |resp|={r['amp']:.4e}", flush=True)
    return np.array(amps), np.array(phases), np.array(Is), np.array(Qs)


def ringdown_omega_est(engine, read_pt, n_steps):
    """Free ring-down: record the read-point series, FFT, return the dominant
    angular frequency (an INDEPENDENT band-setting estimate, not the result)."""
    series, ts = [], []
    for _ in range(n_steps):
        engine.step()
        series.append(float(engine.V[read_pt]))
        ts.append(engine.time)
    series = np.asarray(series) - np.mean(series)
    dt = float(np.mean(np.diff(ts)))
    freqs = np.fft.rfftfreq(len(series), d=dt)  # cycles per time
    spec = np.abs(np.fft.rfft(series * np.hanning(len(series))))
    spec[0] = 0.0
    f_dom = float(freqs[int(np.argmax(spec))])
    return 2.0 * np.pi * f_dom, freqs, spec  # angular


def record_offrun(engine, read_mask, n_settle, n_win):
    """Drive-OFF reference: settle, then record the read series + times. The
    breather background is reproducible, so its lock-in projection at ANY omega
    can be computed offline and SUBTRACTED from the driven run -> the breather
    background cancels, leaving the small-signal probe susceptibility."""
    for _ in range(n_settle):
        engine.step()
    sig, ts = [], []
    for _ in range(n_win):
        engine.step()
        sig.append(engine.read_signal(read_mask))
        ts.append(engine.time)
    return np.asarray(sig), np.asarray(ts)


def project(sig, ts, omega_d):
    """Offline single-frequency lock-in projection of a recorded series."""
    dt = np.diff(ts, prepend=ts[0] - (ts[1] - ts[0]))
    T = float(ts[-1] - ts[0] + (ts[1] - ts[0]))
    Iq = 2.0 / T * np.sum(sig * np.sin(omega_d * ts) * dt)
    Qq = 2.0 / T * np.sum(sig * np.cos(omega_d * ts) * dt)
    return float(Iq), float(Qq)


# ════════════════════════════════════════════════════════════ 1. GATE
def probe_gate():
    print("\n[GATE] probe-capability on KNOWN omega mass-gap resonators", flush=True)
    N = 30
    settings = [
        {"w0": 1.0, "gamma": 0.20},  # known Q = 5  (low-Q standard)
        {"w0": 1.0, "gamma": 0.10},  # known Q = 10 (high-Q standard)
    ]
    results = []
    gate_pass = True
    for s in settings:
        w0, gamma = s["w0"], s["gamma"]
        Q_known = w0 / gamma
        band = np.linspace(0.55 * w0, 1.6 * w0, 8 if FAST else 20)

        def make(wd, w0=w0, gamma=gamma):
            return S11Probe(
                N=N, drive_sector="omega", drive_omega=wd, drive_amp=1e-3,
                gamma_probe=gamma, omega_sector_on=True, buckle_on=False,
                c_omega=0.0, omega_gap=w0, S_min=0.05, pml_thickness=4, src_sigma=3.0,
            )

        amps, _, _, _ = sweep(make, band, lambda e: e.interior_mask().astype(float),
                              n_settle=(300 if FAST else int(6.0 / gamma / 0.04)),
                              n_win=(300 if FAST else 1100), label=f"gate Q={Q_known:.1f}")
        fit = fit_driven(band, amps)
        f0 = fit.get("w0_fit", fit["w0_peak"])
        Qm = fit.get("Q_fit", fit.get("Q_fwhm", float("nan")))
        f0_err = abs(f0 - w0) / w0
        Q_err = abs(Qm - Q_known) / Q_known if np.isfinite(Qm) else float("inf")
        ok = (f0_err <= 0.05) and (Q_err <= 0.20)
        gate_pass = gate_pass and ok
        print(
            f"   => known (f0={w0/(2*np.pi):.4f}, Q={Q_known:.2f}); "
            f"recovered (f0={f0/(2*np.pi):.4f} err {f0_err:.1%}, Q={Qm:.2f} err {Q_err:.1%}) "
            f"-> {'PASS' if ok else 'FAIL'}",
            flush=True,
        )
        results.append(
            {"w0": w0, "gamma": gamma, "Q_known": Q_known, "band": band.tolist(),
             "amps": amps.tolist(), "f0_rec": f0, "Q_rec": Qm,
             "f0_err": f0_err, "Q_err": Q_err, "pass": bool(ok)}
        )
    return {"pass": bool(gate_pass), "settings": results}


# ════════════════════════════════════════════════════════════ 2. LINEARITY
def linearity_subgate():
    print("\n[LINEARITY] response proportional to drive amplitude", flush=True)
    N, w0, gamma = 30, 1.0, 0.12
    amps_in = np.array([2.5e-4, 5e-4, 1e-3, 2e-3, 4e-3])
    if FAST:
        amps_in = amps_in[::2]
    resp = []
    for A in amps_in:
        e = S11Probe(
            N=N, drive_sector="omega", drive_omega=w0, drive_amp=A,
            gamma_probe=gamma, omega_sector_on=True, buckle_on=False,
            c_omega=0.0, omega_gap=w0, S_min=0.05, pml_thickness=4, src_sigma=3.0,
        )
        r = e.lockin(e.interior_mask().astype(float),
                     n_settle=(300 if FAST else 1400), n_win=(300 if FAST else 900))
        resp.append(r["amp"])
        print(f"   A={A:.2e} -> |resp|={r['amp']:.4e}", flush=True)
    resp = np.array(resp)
    coef = np.polyfit(amps_in, resp, 1)
    pred = np.polyval(coef, amps_in)
    ss_res = np.sum((resp - pred) ** 2)
    ss_tot = np.sum((resp - resp.mean()) ** 2)
    r2 = float(1 - ss_res / (ss_tot + 1e-30))
    intercept_rel = float(abs(coef[1]) / (resp.max() + 1e-30))
    linear = (r2 > 0.99) and (intercept_rel < 0.05)
    print(f"   => slope-fit R2={r2:.5f}, |intercept|/max={intercept_rel:.3%} -> "
          f"{'LINEAR' if linear else 'NONLINEAR'}", flush=True)
    return {"amps_in": amps_in.tolist(), "resp": resp.tolist(), "R2": r2,
            "intercept_rel": intercept_rel, "linear": bool(linear)}


# ════════════════════════════════════════════════════════════ 3. UNKNOWN
def unknown_run(drive_amp):
    print("\n[UNKNOWN] plant (2,3)+breather, ring-down -> band, driven BULK sweep", flush=True)
    N = 24 if FAST else 40
    S_min, A_cap = 0.0125, 0.999
    c = (N - 1) / 2.0
    ic = N // 2
    # extractor-floor-respecting (2,3): minor radius r above 3 cells
    R23, r23 = 0.26 * N, 4.0  # r=4 cells > the r>=3 floor

    def make_seeded(wd, with_seed=True):
        e = S11Probe(
            N=N, drive_sector="V", drive_omega=wd, drive_amp=drive_amp,
            src_center=(ic, ic, ic), src_sigma=2.5,
            omega_sector_on=True, buckle_on=False, c_omega=0.45, omega_gap=1.0,
            S_min=S_min, A_cap=A_cap, pml_thickness=5,
        )
        if with_seed:
            e.seed_bulk((ic, ic, ic), sigma=3.5, frac=0.9)  # trapped breather (the mass)
            e.seed_omega_known_2_3(R23, r23, amplitude=0.25, p=2, q=3)  # the planted (2,3)
        return e

    # confirm the planted winding is above the extractor floor (r=4 cells)
    e_chk = make_seeded(1.0, with_seed=True)
    print(f"   planted (2,3): R={R23:.1f}, r={r23:.1f} cells (> r>=3 floor); "
          f"max|omega|={float(np.max(np.abs(e_chk.omega))):.3f}", flush=True)

    # ring-down pre-scan to set the band (independent estimate)
    e_rd = make_seeded(1.0, with_seed=True)
    read_pt = (ic + (3 if FAST else 6), ic, ic)  # interior, off-center, PML-excluded
    w_est, rd_freqs, rd_spec = ringdown_omega_est(e_rd, read_pt, n_steps=(700 if FAST else 3000))
    print(f"   ring-down dominant angular w_est = {w_est:.4f} "
          f"(f_est={w_est/(2*np.pi):.4f})", flush=True)
    if not (np.isfinite(w_est) and w_est > 1e-3):
        w_est = 0.5  # fallback band center

    band = np.linspace(max(0.05, 0.35 * w_est), 2.6 * w_est, 8 if FAST else 16)

    def read_mask_of(e):
        m = np.zeros((N, N, N))
        m[read_pt] = 1.0
        return m * e.interior_mask()

    n_settle, n_win = (300, 300) if FAST else (2200, 2200)

    # drive-OFF reference: same seed, drive_amp=0; record the read series ONCE and
    # project at every band frequency -> the reproducible breather background to
    # SUBTRACT (so the net spectrum is the small-signal probe susceptibility).
    e_off = make_seeded(1.0, with_seed=True)
    e_off.drive_amp = 0.0
    off_sig, off_ts = record_offrun(e_off, read_mask_of(e_off), n_settle, n_win)
    off_IQ = np.array([project(off_sig, off_ts, wd) for wd in band])  # (16,2)

    # driven sweep
    amps_s, ph_s, Is, Qs = sweep(lambda wd: make_seeded(wd, True), band, read_mask_of,
                                 n_settle, n_win, label="driven")

    # NET susceptibility = (driven I,Q) - (drive-off leakage I,Q), complex
    net_I = Is - off_IQ[:, 0]
    net_Q = Qs - off_IQ[:, 1]
    net = np.hypot(net_I, net_Q)
    off_amp = np.hypot(off_IQ[:, 0], off_IQ[:, 1])

    # floor on the NET spectrum: median + 3*robust-sigma (MAD) off-resonance level
    med = float(np.median(net))
    mad = float(np.median(np.abs(net - med))) * 1.4826
    floor = med + 3.0 * (mad if mad > 0 else float(np.std(net)))
    peak_amp = float(net.max())
    clears_floor = peak_amp > floor
    at_band_edge = bool(int(np.argmax(net)) in (0, len(band) - 1))

    # subtraction-meaningful gate: if the net is not small vs the raw driven amp,
    # the breather background did not cancel (non-reproducible) -> UNRESOLVED-leaning
    subtraction_ratio = float(np.median(net) / (np.median(amps_s) + 1e-30))

    # distinct local maxima above floor (MULTI-MODE check) on the NET spectrum
    local_max = 0
    for i in range(1, len(net) - 1):
        if net[i] > net[i - 1] and net[i] > net[i + 1] and net[i] > floor:
            local_max += 1

    fit = fit_driven(band, np.maximum(net, 1e-30))

    return {
        "N": N, "S_min": S_min, "A_cap": A_cap, "drive_amp": drive_amp,
        "R23": R23, "r23": r23, "w_est_ringdown": float(w_est),
        "band": band.tolist(), "amps_driven": amps_s.tolist(),
        "off_amp": off_amp.tolist(), "net": net.tolist(), "phase_driven": ph_s.tolist(),
        "floor": floor, "peak_amp": peak_amp, "clears_floor": bool(clears_floor),
        "subtraction_ratio": subtraction_ratio,
        "local_maxima_above_floor": local_max, "at_band_edge": at_band_edge,
        "fit_seeded": fit, "rd_freqs": rd_freqs.tolist(), "rd_spec": rd_spec.tolist(),
    }


def assign_bin(uk: dict) -> dict:
    """FROZEN bins (ordered). The gate already passed (else UNRESOLVED upstream).
    Operates on the NET susceptibility (driven - drive-off background)."""
    fit = uk["fit_seeded"]
    clears = uk["clears_floor"]
    edge = uk["at_band_edge"]
    n_modes = uk["local_maxima_above_floor"]
    sub_ratio = uk.get("subtraction_ratio", 1.0)
    resid = fit.get("resid_rel", float("inf"))
    fit_ok = fit.get("fit_ok", False)

    if not clears:
        b = "NO-RESPONSE"
        why = ("net susceptibility (driven − drive-off) does not exceed its "
               "median+3σ floor anywhere in the band — the small-signal probe "
               "does not couple a resolvable resonance")
    elif sub_ratio > 0.5:
        b = "UNRESOLVED"
        why = (f"breather background did not cancel (median net / median driven = "
               f"{sub_ratio:.2f} > 0.5) — read is background-dominated, not a clean "
               f"probe susceptibility")
    elif n_modes >= 2:
        b = "MULTI-MODE"
        why = f"{n_modes} local maxima above the floor in the net spectrum"
    elif edge or not fit_ok or resid > 0.35:
        b = "UNRESOLVED"
        why = (f"net peak above floor but: band-edge={edge}, fit_ok={fit_ok}, "
               f"resid={resid if np.isfinite(resid) else 'nan'} (> 0.35)")
    else:
        b = "RESONANCE-CHARACTERIZED"
        why = "single clean Lorentzian in the net spectrum, above floor, inside band"
    return {"bin": b, "why": why}


# ════════════════════════════════════════════════════════════ figures
def make_figures(gate, lin, uk, verdict):
    paths = []
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
    for s in gate["settings"]:
        ax[0].plot(np.array(s["band"]) / (2 * np.pi), s["amps"], "o-", ms=4,
                   label=f"known Q={s['Q_known']:.1f} (rec {s['Q_rec']:.1f})")
    ax[0].set_xlabel("drive f (cycles/time)")
    ax[0].set_ylabel("|lock-in resp|")
    ax[0].set_title(f"GATE: probe recovers KNOWN f0/Q\npass={gate['pass']}")
    ax[0].legend(fontsize=8)
    ax[0].grid(alpha=0.2)
    ax[1].plot(lin["amps_in"], lin["resp"], "o-", color="C2")
    ax[1].set_xlabel("drive amplitude A")
    ax[1].set_ylabel("|lock-in resp|")
    ax[1].set_title(f"LINEARITY: resp ∝ A\nR²={lin['R2']:.4f} linear={lin['linear']}")
    ax[1].grid(alpha=0.2)
    fig.tight_layout()
    p1 = OUT / "electron_s11_gate.png"
    fig.savefig(p1, dpi=120)
    plt.close(fig)
    paths.append(p1.name)

    fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
    band = np.array(uk["band"]) / (2 * np.pi)
    ax[0].plot(band, uk["amps_driven"], "o-", color="gray", ms=3, alpha=0.6,
               label="raw driven (breather-dominated)")
    ax[0].plot(band, uk["off_amp"], "x-", color="C0", ms=4, alpha=0.6,
               label="drive-off leakage")
    ax[0].plot(band, uk["net"], "o-", color="C3", ms=5, label="NET susceptibility (driven−off)")
    ax[0].axhline(uk["floor"], ls=":", color="k", label="net floor (median+3σ)")
    ax[0].set_xlabel("drive f (cycles/time)")
    ax[0].set_ylabel("|lock-in resp|")
    ax[0].set_title(f"UNKNOWN bulk S11 sweep\nbin={verdict['bin']}")
    ax[0].legend(fontsize=8)
    ax[0].grid(alpha=0.2)
    rd_f = np.array(uk["rd_freqs"])
    ax[1].plot(rd_f, uk["rd_spec"], color="C4")
    ax[1].axvline(uk["w_est_ringdown"] / (2 * np.pi), ls="--", color="C3",
                  label=f"f_est={uk['w_est_ringdown']/(2*np.pi):.3f}")
    ax[1].set_xlabel("f (cycles/time)")
    ax[1].set_ylabel("ring-down |FFT|")
    ax[1].set_title("ring-down pre-scan (sets the band)")
    ax[1].set_xlim(0, min(rd_f.max(), 4 * uk["w_est_ringdown"] / (2 * np.pi) + 0.1))
    ax[1].legend(fontsize=8)
    ax[1].grid(alpha=0.2)
    fig.tight_layout()
    p2 = OUT / "electron_s11_unknown.png"
    fig.savefig(p2, dpi=120)
    plt.close(fig)
    paths.append(p2.name)
    return paths


# ════════════════════════════════════════════════════════════ main
def main():
    t0 = time.time()
    print("=" * 74)
    print("  ELECTRON S11 RESONANCE SWEEP (ave-apparatus-floor-attribution; ordered)")
    print("=" * 74, flush=True)

    gate = probe_gate()
    lin = linearity_subgate()
    gate_ok = gate["pass"] and lin["linear"]
    print(f"\n  GATE: probe-capability={gate['pass']} linearity={lin['linear']} "
          f"-> {'PASS' if gate_ok else 'FAIL'}", flush=True)

    out = {"gate": gate, "linearity": lin, "gate_ok": bool(gate_ok)}

    if not gate_ok:
        out["verdict"] = {"bin": "UNRESOLVED",
                          "why": "probe-capability/linearity gate FAILED -> "
                                 "no f0/Q reported for the electron state"}
        verdict = out["verdict"]
        uk = None
    else:
        uk = unknown_run(drive_amp=6e-4)
        verdict = assign_bin(uk)
        out["unknown"] = uk
        out["verdict"] = verdict
        # BVD only if characterized
        fit = uk["fit_seeded"]
        if verdict["bin"] == "RESONANCE-CHARACTERIZED":
            w0 = fit.get("w0_fit", fit["w0_peak"])
            Qm = fit.get("Q_fit", fit.get("Q_fwhm", float("nan")))
            out["bvd"] = bvd_from_resonance(w0, Qm)
            out["f0_measured_cyc"] = float(w0 / (2 * np.pi))
            out["Q_measured"] = float(Qm)
            # forward-registered post-hoc alpha comparison (NOT a bin criterion)
            out["posthoc_alpha_note"] = (
                f"measured Q={Qm:.3f}; alpha^-1={ALPHA_COLD_INV:.3f}; "
                f"ratio Q/alpha^-1={Qm/ALPHA_COLD_INV:.4f} (reported AFTER the bin, "
                f"NOT used to assign it; consistency-class)"
            )
        else:
            out["bvd"] = {"status": "UNRESOLVED (bin != RESONANCE-CHARACTERIZED)"}

    figs = make_figures(gate, lin, uk if uk else _empty_uk(), verdict)
    out["figures"] = figs
    out["elapsed_s"] = time.time() - t0
    (OUT / "electron_s11_results.json").write_text(json.dumps(out, indent=2, default=str))

    print("\n" + "=" * 74)
    print(f"  S11 BIN: {verdict['bin']}")
    print(f"  why: {verdict['why']}")
    if uk and verdict["bin"] == "RESONANCE-CHARACTERIZED":
        print(f"  measured f0={out['f0_measured_cyc']:.4f} cyc/time, Q={out['Q_measured']:.3f}")
        print(f"  {out['posthoc_alpha_note']}")
    print(f"  elapsed {out['elapsed_s']:.0f}s; figures {figs}")
    print("=" * 74, flush=True)
    return out


def _empty_uk():
    return {"band": [0, 1], "amps_driven": [0, 0], "off_amp": [0, 0], "net": [0, 0],
            "floor": 0.0, "w_est_ringdown": 1.0, "rd_freqs": [0, 1], "rd_spec": [0, 0]}


if __name__ == "__main__":
    main()
