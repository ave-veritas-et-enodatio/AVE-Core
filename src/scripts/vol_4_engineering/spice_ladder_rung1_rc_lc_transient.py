#!/usr/bin/env python3
"""
SPICE PHASE-1 ladder — RUNG 1: RC / LC analytic transients.
===========================================================

The first rung of the validation ladder (charter STEP-4, rung 1). It runs
canonical LINEAR reference cells through a live ngspice ``.TRAN`` and checks
the integrated waveform against the textbook closed form. This rung validates
one thing only: **ngspice parses + integrates our netlists correctly** — the
engine floor before any AVE-specific constitutive law is exercised.

CLASS: consistency (engine-integrates-a-known-analytic-circuit-correctly). No
substrate DOF is claimed here; the RC / LC cells are standard lumped elements
whose Cartesian/scalar treatment is exactly correct (a known-analytic
calibration, not a substrate measurement).

Two sub-tests, each with a stated analytic target + recovery tolerance:

  (a) RC charging:  V_C(t) = V0 (1 - e^{-t/RC}).  TARGET: recover the time
      constant tau = RC from the 63.2% crossing.  R = 1 kOhm, C = 1 uF =>
      tau = 1 ms.

  (b) LC oscillation:  an undamped LC tank rings at f_res = 1/(2*pi*sqrt(LC)).
      TARGET: recover f_res from the FFT peak / zero-crossing period.
      L = 1 mH, C = 1 uF => f_res = 5032.9 Hz.

Emits: spice_ladder_rung1_rc.cir, spice_ladder_rung1_lc.cir, and a JSON
result with target / measured / rel-error for each.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from ave.bench.spice_runner import (
    ngspice_version,
    read_wrdata,
    run_ngspice,
)

# Committed artifacts (.cir + JSON) live in a TRACKED dir; transient .dat
# scratch (regenerable) goes to the gitignored _output/.
ART_DIR = Path(__file__).resolve().parent / "spice_ladder_artifacts"
OUT_DIR = Path(__file__).resolve().parent / "_output" / "spice_ladder"

# Recovery tolerances (this is a numerical-integration cross-check, not a
# physics prediction; the analytic value is EXACT, so tolerance bounds the
# integrator + sampling discretization error).
RC_TAU_TOL = 2.0e-2  # 2% — tau from a coarse .tran 63.2% crossing
LC_FRES_TOL = 2.0e-2  # 2% — f_res from a windowed FFT peak


def _rc_netlist(dat_path: Path, R: float, C: float, tau: float) -> str:
    """RC step-response: a 1V source steps at t=0 into series R, C to ground."""
    t_stop = 6.0 * tau  # 6 tau => >99.7% settled
    t_step = tau / 500.0
    return f"""* SPICE PHASE-1 rung 1(a) — RC charging transient
* V_C(t) = V0 (1 - exp(-t/RC)); tau = RC = {tau:.6e} s (R={R}, C={C})
V1 IN 0 PWL(0 0 1p 1 1 1)
R1 IN NC {R:.6e}
C1 NC 0 {C:.6e}
.tran {t_step:.6e} {t_stop:.6e} uic
.control
run
wrdata {dat_path} v(NC)
.endc
.end
"""


def _lc_netlist(dat_path: Path, L: float, C: float, f_res: float) -> str:
    """
    Undamped LC tank: capacitor pre-charged to 1V (uic), rings at f_res.

    A tiny series R keeps ngspice's integrator well-conditioned without
    materially damping the ring over the observation window (Q >> 1).
    """
    n_cycles = 20.0
    t_stop = n_cycles / f_res
    t_step = 1.0 / f_res / 400.0  # 400 samples/cycle
    return f"""* SPICE PHASE-1 rung 1(b) — LC oscillation transient
* f_res = 1/(2 pi sqrt(LC)) = {f_res:.6e} Hz (L={L}, C={C})
L1 NC 0 {L:.6e}
C1 NC 0 {C:.6e} IC=1
R1 NC 0 1e6
.tran {t_step:.6e} {t_stop:.6e} uic
.control
run
wrdata {dat_path} v(NC)
.endc
.end
"""


def _recover_tau(t: np.ndarray, v: np.ndarray, v_final: float) -> float:
    """Time constant from the 63.2% (1 - 1/e) crossing, linearly interpolated."""
    target = (1.0 - 1.0 / np.e) * v_final
    idx = int(np.argmax(v >= target))
    if idx == 0:
        return float("nan")
    t0, t1 = t[idx - 1], t[idx]
    v0, v1 = v[idx - 1], v[idx]
    return float(t0 + (target - v0) * (t1 - t0) / (v1 - v0))


def _recover_fres(t: np.ndarray, v: np.ndarray) -> float:
    """Resonant frequency from the FFT peak of the (mean-removed) ring."""
    v = v - np.mean(v)
    dt = float(np.mean(np.diff(t)))
    n = len(v)
    win = np.hanning(n)
    spec = np.abs(np.fft.rfft(v * win))
    freqs = np.fft.rfftfreq(n, dt)
    peak = int(np.argmax(spec[1:]) + 1)  # skip DC
    # Parabolic interpolation on the log-spectrum for sub-bin accuracy.
    if 1 <= peak < len(spec) - 1:
        a, b, c = np.log(spec[peak - 1] + 1e-30), np.log(spec[peak] + 1e-30), np.log(spec[peak + 1] + 1e-30)
        denom = a - 2 * b + c
        delta = 0.5 * (a - c) / denom if denom != 0 else 0.0
    else:
        delta = 0.0
    return float((peak + delta) * (freqs[1] - freqs[0]))


def run_rung1() -> dict:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ART_DIR.mkdir(parents=True, exist_ok=True)

    # ---- (a) RC ----
    R, C = 1.0e3, 1.0e-6
    tau_analytic = R * C
    rc_dat = OUT_DIR / "spice_ladder_rung1_rc.dat"
    rc_cir = ART_DIR / "spice_ladder_rung1_rc.cir"
    rc_net = _rc_netlist(rc_dat, R, C, tau_analytic)
    r_rc = run_ngspice(rc_net, rc_cir)
    assert r_rc.ok, f"RC ngspice run failed:\n{r_rc.stderr[:800]}"
    rc = read_wrdata(rc_dat, ["t", "v"])
    tau_meas = _recover_tau(rc["t"], rc["v"], v_final=1.0)
    tau_err = abs(tau_meas - tau_analytic) / tau_analytic

    # ---- (b) LC ----
    L, C_lc = 1.0e-3, 1.0e-6
    fres_analytic = 1.0 / (2.0 * np.pi * np.sqrt(L * C_lc))
    lc_dat = OUT_DIR / "spice_ladder_rung1_lc.dat"
    lc_cir = ART_DIR / "spice_ladder_rung1_lc.cir"
    lc_net = _lc_netlist(lc_dat, L, C_lc, fres_analytic)
    r_lc = run_ngspice(lc_net, lc_cir)
    assert r_lc.ok, f"LC ngspice run failed:\n{r_lc.stderr[:800]}"
    lc = read_wrdata(lc_dat, ["t", "v"])
    fres_meas = _recover_fres(lc["t"], lc["v"])
    fres_err = abs(fres_meas - fres_analytic) / fres_analytic

    passed = (tau_err < RC_TAU_TOL) and (fres_err < LC_FRES_TOL)

    return {
        "rung": 1,
        "name": "RC/LC analytic transients",
        "ngspice_version": ngspice_version(),
        "class": "consistency (engine-integrates-known-analytic-circuit)",
        "rc": {
            "R_ohm": R,
            "C_farad": C,
            "tau_analytic_s": tau_analytic,
            "tau_measured_s": tau_meas,
            "rel_error": tau_err,
            "tolerance": RC_TAU_TOL,
            "cir": rc_cir.name,
        },
        "lc": {
            "L_henry": L,
            "C_farad": C_lc,
            "fres_analytic_hz": fres_analytic,
            "fres_measured_hz": fres_meas,
            "rel_error": fres_err,
            "tolerance": LC_FRES_TOL,
            "cir": lc_cir.name,
        },
        "verdict": "PASS" if passed else "FAIL",
    }


if __name__ == "__main__":
    result = run_rung1()
    (ART_DIR / "spice_ladder_rung1_result.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8"
    )
    print("=" * 68)
    print("SPICE PHASE-1 ladder — RUNG 1: RC/LC analytic transients")
    print("=" * 68)
    print(f"  ngspice          : {result['ngspice_version']}")
    rc, lc = result["rc"], result["lc"]
    print(f"  RC tau  analytic : {rc['tau_analytic_s']:.6e} s")
    print(f"  RC tau  measured : {rc['tau_measured_s']:.6e} s   "
          f"(err {rc['rel_error']:.3e}, tol {rc['tolerance']:.1e})")
    print(f"  LC fres analytic : {lc['fres_analytic_hz']:.6e} Hz")
    print(f"  LC fres measured : {lc['fres_measured_hz']:.6e} Hz  "
          f"(err {lc['rel_error']:.3e}, tol {lc['tolerance']:.1e})")
    print(f"  VERDICT          : {result['verdict']}")
