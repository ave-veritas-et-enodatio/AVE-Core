"""Two-tank decoherence check — DRIVER (registered check, Grant's 2026-07-15 walk).

Question (registers walk, thermal-phase-registers proposal): does
"temperature = the width of the clock-detuning distribution" hold as a MEASURED
statement — i.e., do two identical bound tanks in a common incoherent bath
phase-diffuse at a rate set by the bath energy density, via the substrate's own
Op14 clock-rate mechanism (bath energy raises time-averaged A^2 -> S = sqrt(1-A^2)
drops -> local clock slows)?

Companion note (frozen hypothesis + verdict classes + method):
  research/2026-07-15_two-tank-decoherence-check_NOTE.md

SECTOR / REGIME HEADER (declared before any number)
  SECTOR   : thermal / incoherent-propagating V-sector register (the "3" scalar
             K4 voltage field on the bond capacitance; NOT a transverse photon).
  MODE     : closed (undriven), lossless two-body phase-statistics measurement.
  REGIME   : sub-yield. Clock operating point A_clk ~= 0.08 (~ V_YIELD/V_SNAP =
             sqrt(alpha), the regime-I/II boundary); bath deep-linear
             (A_bath << R_I everywhere); total field sub-rupture (A < R_III=1),
             predominantly regime-I. Max realized strain reported per run.
  PHASE    : cold substrate + incoherent V-bath perturbation.
  KERNEL   : measured BOTH ways per substrate-native regime discipline —
             ON  (nonlinear + op3_bond_reflection: Op14 saturation active = the
                  proposed thermal-clock mechanism) and
             OFF (pure linear lattice: mechanism disabled = additive-interference
                  control). A "diffusion" that persists with the kernel OFF is
                  additive wave-interference, NOT the substrate thermal-clock
                  mechanism (regime discipline: a signal that survives disabling
                  its claimed mechanism is an ARTIFACT).

CLASS (consistency-vs-emergence): CONSISTENCY. This check adjudicates whether a
proposed DEFINITIONAL operationalization is internally consistent with the
engine. No CODATA input, no value minted, no emergence headlined.

PHASE-SPACE-COORDINATE DISCIPLINE (A46): the clock phase is read in the native
(V_inc, V_ref) / (V, Phi_link) phasor plane — a phase-space coordinate, NOT a
real-space Cartesian projection of phi^2. Delta-phi(t) is a phase-plane angle
difference. Both reactance-pair states (C-state node voltage V, L-state flux
linkage Phi_link) are recorded every step (reactance-pair-tracking discipline).

HONESTY: characterization check, hypothesis-first. Verdict thresholds are frozen
as module constants below (declared in code before the production run). The
u_bath=0 control is mandatory and runs first. Every physics constant is imported
from ave.core.constants. Discretization caveat: modest lattice (N=16 class);
this is a phase-statistics measurement, not a convergence study, so the closed
lattice is quasi-periodic (finite Poincare recurrence) — diffusion, if any, is
only asymptotic within the window.

Run:
    python two_tank_decoherence_check.py --smoke        # CI-budget
    python two_tank_decoherence_check.py --production    # full sweep
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.core.constants import ALPHA, R_I, R_II, R_III, V_SNAP, V_YIELD  # noqa: E402
from ave.core.k4_tlm import K4Lattice3D  # noqa: E402

# ─────────────────────────────────────────────────────────────────────────────
# FROZEN PARAMETERS (declared before the production run)
# ─────────────────────────────────────────────────────────────────────────────
N_LATTICE = 16          # modest lattice (phase-statistics, not convergence)
N_STEPS = 3000          # long quiet evolution window
CLK_AMP = 0.08          # clock operating point ~ V_YIELD/V_SNAP = sqrt(alpha)
CLK_SIGMA = 1.5         # clock Gaussian envelope width (cells)
CLK_K = np.pi / 2.0     # standing-carrier wavevector
BATH_MODES = 40         # plane-wave components (baseline mode density)
BATH_MODES_UP = 150     # the ONE disclosed mode-density increase (N=24)
N_LATTICE_UP = 24
# u_bath grid: control + 4 log-spaced (ratio 3), all sub-yield
U_GRID = [0.0, 1.0e-4, 3.0e-4, 9.0e-4, 2.7e-3]
N_SEEDS = 3
EDGE_TRIM = 150         # discard filter/Hilbert edge transient (steps)

# Verdict-class thresholds (FROZEN — the classify() contract)
CTRL_FLOOR = 1.0e-3     # rad: control Delta-phi span must stay below this
DIFF_LO, DIFF_HI = 0.80, 1.30   # MSD log-log slope band = diffusive
BALLISTIC_LO = 1.70             # >= => ballistic (t^2)
BOUNDED_HI = 0.30               # <= => bounded/oscillatory
P_LIN_LO, P_LIN_HI = 0.80, 1.30  # D(u) log-log exponent band = linear-in-u
EXCESS_MIN = 0.50       # kernel must drive >= this fraction of the diffusion
                        # variance for it to count as a SUBSTRATE-THERMAL effect

# MSD lag grid for the shape fit (within the diffusive window << recurrence)
MSD_TAUS = np.array([20, 60, 150, 400, 900])


# ─────────────────────────────────────────────────────────────────────────────
# PURE VERDICT LOGIC (unit-testable; record -> class)
# ─────────────────────────────────────────────────────────────────────────────
@dataclass
class Summary:
    """Reduced summary of a full sweep, consumed by classify()."""
    ctrl_span_on: float      # control Delta-phi span, kernel ON (rad)
    ctrl_span_off: float     # control Delta-phi span, kernel OFF (rad)
    shape_on: float          # median MSD log-log slope, kernel ON
    p_on: float              # log-log slope of D_ON vs u (u-scaling exponent)
    excess_frac: float       # median (Var_ON - Var_OFF)/Var_ON at t_end
    shape_iso: float         # MSD log-log slope of isolated-Op14 (lock-in) readout


def classify(s: Summary) -> str:
    """Map a sweep Summary to a frozen verdict class.

    Order matters: control gate first; then shape (bounded/ballistic fail);
    then the substrate-native MECHANISM gate (kernel-excess) before any positive
    diffusive verdict; then the u-scaling exponent.
    """
    if s.ctrl_span_on > CTRL_FLOOR or s.ctrl_span_off > CTRL_FLOOR:
        return "CONTROL-FAIL"
    if s.shape_on >= BALLISTIC_LO:
        return "NON-DIFFUSIVE"           # ballistic (t^2) inhomogeneous scatter
    if s.shape_on <= BOUNDED_HI:
        return "NON-DIFFUSIVE"           # bounded / oscillatory
    # shape_on is diffusive-shaped. Is the DIFFUSION driven by the Op14 kernel,
    # or is it additive wave-interference (present with the kernel OFF)?
    if s.excess_frac < EXCESS_MIN:
        return "ADDITIVE-ARTIFACT"       # diffusion not from the thermal mechanism
    if P_LIN_LO <= s.p_on <= P_LIN_HI:
        return "DIFFUSIVE-LINEAR"        # the definition is MEASURED
    return "DIFFUSIVE-NONLINEAR"         # survives with a nonlinear calibration


VERDICT_MEANING = {
    "CONTROL-FAIL": "u=0 control drifts -> instrument artifact; STOP before physics.",
    "NON-DIFFUSIVE": "bounded/ballistic -> proposed diffusion definition FAILS as posed.",
    "ADDITIVE-ARTIFACT": "Delta-phi diffuses but kernel-independent -> the diffusion is "
                         "additive wave-interference, NOT the Op14 thermal-clock mechanism; "
                         "the substrate-thermal definition is NOT demonstrated.",
    "DIFFUSIVE-LINEAR": "Var[Dphi] ~ t, D ~ u_bath, kernel-driven -> definition MEASURED.",
    "DIFFUSIVE-NONLINEAR": "Var[Dphi] ~ t, D ~ u_bath^p (p!=1), kernel-driven -> survives "
                           "with a nonlinear calibration; report p.",
}


# ─────────────────────────────────────────────────────────────────────────────
# LATTICE + BATH PRIMITIVES
# ─────────────────────────────────────────────────────────────────────────────
def nearest_active(lat: K4Lattice3D, x: int, y: int, z: int):
    """Snap (x,y,z) to the nearest active K4 (diamond-sublattice) site."""
    for dz in (0, 1, -1):
        for dy in (0, 1, -1):
            for dx in (0, 1, -1):
                xx, yy, zz = x + dx, y + dy, z + dz
                if 0 <= xx < lat.nx and 0 <= yy < lat.ny and 0 <= zz < lat.nz:
                    if lat.mask_active[xx, yy, zz]:
                        return (xx, yy, zz)
    raise RuntimeError("no active site near requested clock center")


def seed_clock(lat: K4Lattice3D, c, amp: float, sigma: float = CLK_SIGMA, k: float = CLK_K):
    """Seed a localized Gaussian-windowed standing V-oscillation (the clock)."""
    ii, jj, kk = np.indices((lat.nx, lat.ny, lat.nz))
    env = np.exp(-((ii - c[0]) ** 2 + (jj - c[1]) ** 2 + (kk - c[2]) ** 2) / (2 * sigma**2))
    env[~lat.mask_active] = 0.0
    pattern = amp * env * np.cos(k * (ii - c[0]))
    for p in range(4):
        lat.V_inc[..., p] += pattern / 2.0


def inject_bath(lat: K4Lattice3D, u_bath: float, rng, n_modes: int) -> float:
    """Superpose n_modes random plane waves (random k-direction, random phase,
    random per-port weight), scaled to a target mean active-site energy density
    u_bath. Returns the realized mean energy density (should ~= u_bath)."""
    if u_bath <= 0.0:
        return 0.0
    ii, jj, kk = np.indices((lat.nx, lat.ny, lat.nz))
    field = np.zeros((lat.nx, lat.ny, lat.nz, 4))
    for _ in range(n_modes):
        kv = rng.integers(1, lat.nx // 2, size=3) * (2 * np.pi / lat.nx) * rng.choice([-1, 1], size=3)
        phase = rng.uniform(0.0, 2 * np.pi)
        pw = np.cos(kv[0] * ii + kv[1] * jj + kv[2] * kk + phase)
        portw = rng.normal(size=4)
        for p in range(4):
            field[..., p] += pw * portw[p]
    field[~lat.mask_active] = 0.0
    cur = np.sum(field**2, axis=-1)[lat.mask_active].mean()
    field *= np.sqrt(u_bath / cur)
    lat.V_inc += field
    return float(np.sum(field**2, axis=-1)[lat.mask_active].mean())


def clock_states(lat: K4Lattice3D, s):
    """Native reactance pair at a clock site: C-state node voltage V (sum of
    incident+reflected over the 4 ports) and L-state flux linkage Phi (sum of
    Phi_link over ports). Both are phase-space (phasor-plane) coordinates."""
    x, y, z = s
    v = float(np.sum(lat.V_inc[x, y, z, :] + lat.V_ref[x, y, z, :]))
    phi = float(np.sum(lat.Phi_link[x, y, z, :]))
    return v, phi


# ─────────────────────────────────────────────────────────────────────────────
# PHASE ESTIMATORS
# ─────────────────────────────────────────────────────────────────────────────
def hilbert_phase(v: np.ndarray) -> np.ndarray:
    """Analytic-signal (Hilbert) phase of the local V time series. PRIMARY
    readout — the literal 'phase of the local oscillation'. Includes any additive
    bath field at the site (that is what the mechanism control disentangles)."""
    from scipy.signal import hilbert
    return np.unwrap(np.angle(hilbert(v - v.mean())))


def lockin_phase(v: np.ndarray, w0: float, cutoff_frac: float = 0.20) -> np.ndarray:
    """ISOLATED-Op14 readout: heterodyne (lock-in) demod at the clock frequency
    w0, low-passing to a baseband phasor. Rejects broadband additive bath spectrally,
    so it isolates the multiplicative Op14 clock-rate modulation."""
    from scipy.signal import butter, filtfilt
    t = np.arange(len(v))
    b, a = butter(4, min(w0 * cutoff_frac / np.pi, 0.9), btype="low")
    ic = filtfilt(b, a, v * np.cos(w0 * t))
    qs = filtfilt(b, a, v * np.sin(w0 * t))
    return np.unwrap(np.arctan2(qs, ic))


def dominant_omega(v: np.ndarray) -> float:
    """Clock carrier frequency from the FFT peak of the local V series."""
    v = v - v.mean()
    sp = np.abs(np.fft.rfft(v))
    freqs = np.fft.rfftfreq(len(v))
    return float(2 * np.pi * freqs[np.argmax(sp)])


def msd_curve(dphi: np.ndarray, taus: np.ndarray = MSD_TAUS):
    """Time-averaged mean-squared displacement of Delta-phi at lags taus."""
    return np.array([np.mean((dphi[t:] - dphi[:-t]) ** 2) for t in taus])


def msd_loglog_slope(dphi: np.ndarray, taus: np.ndarray = MSD_TAUS) -> float:
    """Anomalous-diffusion exponent: 1=diffusive, 2=ballistic, ~0=bounded."""
    m = msd_curve(dphi, taus)
    return float(np.polyfit(np.log(taus), np.log(m + 1e-30), 1)[0])


def diffusion_constant(dphi: np.ndarray, taus: np.ndarray = MSD_TAUS) -> float:
    """D from MSD ~= 2 D tau (slope of the linear-in-lag fit)."""
    m = msd_curve(dphi, taus)
    return float(np.polyfit(taus, m, 1)[0] / 2.0)


def loglog_exponent(x, y) -> float:
    """Log-log slope of y vs x over strictly positive samples."""
    x = np.asarray(x, float); y = np.asarray(y, float)
    good = (x > 0) & (y > 0)
    if good.sum() < 2:
        return float("nan")
    return float(np.polyfit(np.log(x[good]), np.log(y[good]), 1)[0])


# ─────────────────────────────────────────────────────────────────────────────
# ONE RUN
# ─────────────────────────────────────────────────────────────────────────────
def run_once(u_bath: float, seed: int, kernel_on: bool, *, N=N_LATTICE,
             n_modes=BATH_MODES, nsteps=N_STEPS, clk_amp=CLK_AMP):
    """Seed two identical clocks + a common bath; evolve; return per-clock
    reactance-pair time series and the max realized strain."""
    rng = np.random.default_rng(seed)
    lat = K4Lattice3D(N, N, N, nonlinear=kernel_on, op3_bond_reflection=kernel_on, V_SNAP=1.0)
    s1 = nearest_active(lat, N // 4, N // 2, N // 2)
    s2 = nearest_active(lat, 3 * N // 4, N // 2, N // 2)
    seed_clock(lat, s1, clk_amp)
    seed_clock(lat, s2, clk_amp)
    u_realized = inject_bath(lat, u_bath, rng, n_modes)
    max_strain = float(np.sqrt(np.sum(lat.V_inc**2, axis=-1)).max())
    v1 = np.empty(nsteps); v2 = np.empty(nsteps)
    p1 = np.empty(nsteps); p2 = np.empty(nsteps)
    energy = np.empty(nsteps)
    for n in range(nsteps):
        lat.step()
        v1[n], p1[n] = clock_states(lat, s1)
        v2[n], p2[n] = clock_states(lat, s2)
        energy[n] = lat.total_energy()
    # Conservation check over the recording window. (E is NOT measured pre-first-
    # step: at t=0 only V_inc is populated (V_ref=0), so a pre-scatter reading
    # undercounts by 2x — a TLM bookkeeping artifact, not a physics drift.)
    energy_drift = float((energy.max() - energy.min()) / (energy.mean() + 1e-30))
    sep = abs(s1[0] - s2[0])
    return dict(v1=v1, v2=v2, p1=p1, p2=p2, max_strain=max_strain,
                u_realized=u_realized, energy_drift=energy_drift,
                sep=sep, s1=s1, s2=s2)


def analyze_run(rec, w0: float):
    """Reduce one run to phase-statistics observables (both readouts)."""
    e = EDGE_TRIM
    ph1 = hilbert_phase(rec["v1"]); ph2 = hilbert_phase(rec["v2"])
    dphi = (ph1 - ph2)[e:-e]
    dphi = dphi - dphi.mean()
    t = np.arange(len(dphi))
    # common-mode mean shift (clock slowing): slope of (ph1+ph2)/2 minus carrier
    cm = 0.5 * (ph1 + ph2)
    mean_shift = float(np.polyfit(np.arange(len(cm)), cm, 1)[0] - w0)
    # variance at window end (for kernel-excess) and shape
    var_end = float(dphi.var())
    shape = msd_loglog_slope(dphi)
    D = diffusion_constant(dphi)
    # isolated-Op14 readout (lock-in), rejecting additive bath
    li1 = lockin_phase(rec["v1"], w0); li2 = lockin_phase(rec["v2"], w0)
    dphi_iso = (li1 - li2)[e:-e]; dphi_iso = dphi_iso - dphi_iso.mean()
    shape_iso = msd_loglog_slope(dphi_iso)
    var_iso = float(dphi_iso.var())
    return dict(mean_shift=mean_shift, var_end=var_end, shape=shape, D=D,
                shape_iso=shape_iso, var_iso=var_iso, dphi_rms=float(dphi.std()))


# ─────────────────────────────────────────────────────────────────────────────
# FULL SWEEP
# ─────────────────────────────────────────────────────────────────────────────
def run_sweep(*, N=N_LATTICE, n_modes=BATH_MODES, nsteps=N_STEPS,
              u_grid=U_GRID, n_seeds=N_SEEDS, clk_amp=CLK_AMP):
    """Run kernel ON + OFF across the u grid with n_seeds each, reduce, classify."""
    # carrier frequency from a kernel-ON u=0 control run
    ctrl_rec = run_once(0.0, 0, True, N=N, n_modes=n_modes, nsteps=nsteps, clk_amp=clk_amp)
    w0 = dominant_omega(ctrl_rec["v1"])

    per_u = {}          # u -> {'on': [...], 'off': [...]}
    ctrl_span = {"on": None, "off": None}
    for kon in (True, False):
        key = "on" if kon else "off"
        for u in u_grid:
            seeds = range(1, n_seeds + 1) if u > 0 else [0]
            recs = []
            for sd in seeds:
                rec = run_once(u, sd, kon, N=N, n_modes=n_modes, nsteps=nsteps, clk_amp=clk_amp)
                a = analyze_run(rec, w0)
                a["max_strain"] = rec["max_strain"]
                a["energy_drift"] = rec["energy_drift"]
                a["u_realized"] = rec["u_realized"]
                recs.append(a)
            per_u.setdefault(u, {})[key] = recs
            if u == 0.0:
                # control span = max abs Hilbert Delta-phi wander (edge-trimmed)
                ph1 = hilbert_phase(run_once(0.0, 0, kon, N=N, n_modes=n_modes,
                                             nsteps=nsteps, clk_amp=clk_amp)["v1"])
                # by translation symmetry both clocks identical => reuse rec dphi span
                ctrl_span[key] = _control_span(kon, N, n_modes, nsteps, clk_amp)

    # reduce to Summary
    us = [u for u in u_grid if u > 0]
    D_on = [np.median([r["D"] for r in per_u[u]["on"]]) for u in us]
    shape_on_vals = [np.median([r["shape"] for r in per_u[u]["on"]]) for u in us]
    shape_iso_vals = [np.median([r["shape_iso"] for r in per_u[u]["on"]]) for u in us]
    # kernel-excess fraction per u: (Var_ON - Var_OFF)/Var_ON at window end
    excess = []
    for u in us:
        v_on = np.median([r["var_end"] for r in per_u[u]["on"]])
        v_off = np.median([r["var_end"] for r in per_u[u]["off"]])
        excess.append((v_on - v_off) / (v_on + 1e-30))
    summary = Summary(
        ctrl_span_on=float(ctrl_span["on"]),
        ctrl_span_off=float(ctrl_span["off"]),
        shape_on=float(np.median(shape_on_vals)),
        p_on=loglog_exponent(us, D_on),
        excess_frac=float(np.median(excess)),
        shape_iso=float(np.median(shape_iso_vals)),
    )
    verdict = classify(summary)
    return dict(w0=w0, us=us, D_on=D_on, shape_on=shape_on_vals,
                shape_iso=shape_iso_vals, excess=excess, per_u=per_u,
                summary=asdict(summary), verdict=verdict,
                verdict_meaning=VERDICT_MEANING[verdict])


def _control_span(kon, N, n_modes, nsteps, clk_amp):
    rec = run_once(0.0, 0, kon, N=N, n_modes=n_modes, nsteps=nsteps, clk_amp=clk_amp)
    e = EDGE_TRIM
    d = (hilbert_phase(rec["v1"]) - hilbert_phase(rec["v2"]))[e:-e]
    return float(d.max() - d.min())


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--smoke", action="store_true", help="CI-budget tiny sweep")
    ap.add_argument("--production", action="store_true", help="full frozen sweep")
    ap.add_argument("--mode-density-up", action="store_true",
                    help="the one disclosed mode-density increase (N=24, M=150)")
    args = ap.parse_args(argv)

    out_dir = Path(__file__).resolve().parents[3] / "assets" / "sim_outputs"
    out_dir.mkdir(parents=True, exist_ok=True)

    t0 = time.time()
    if args.smoke:
        # N=16 keeps the two clocks non-overlapping (sep = 8 >> envelope width);
        # window > max(MSD_TAUS) + 2*EDGE_TRIM so the shape fit is well-posed.
        res = run_sweep(N=16, n_modes=16, nsteps=1300, u_grid=[0.0, 1e-4, 9e-4], n_seeds=2)
        tag = "smoke"
    elif args.mode_density_up:
        res = run_sweep(N=N_LATTICE_UP, n_modes=BATH_MODES_UP, nsteps=2500)
        tag = "mode_density_up"
    else:
        res = run_sweep()
        tag = "production"
    res["wall_seconds"] = round(time.time() - t0, 1)
    res["tag"] = tag
    res["frozen_params"] = dict(
        N=N_LATTICE, N_STEPS=N_STEPS, CLK_AMP=CLK_AMP, BATH_MODES=BATH_MODES,
        U_GRID=U_GRID, N_SEEDS=N_SEEDS, R_I=R_I, R_II=R_II, R_III=R_III,
        V_YIELD_over_V_SNAP=V_YIELD / V_SNAP, ALPHA=ALPHA,
        thresholds=dict(CTRL_FLOOR=CTRL_FLOOR, DIFF_LO=DIFF_LO, DIFF_HI=DIFF_HI,
                        BALLISTIC_LO=BALLISTIC_LO, BOUNDED_HI=BOUNDED_HI,
                        P_LIN_LO=P_LIN_LO, P_LIN_HI=P_LIN_HI, EXCESS_MIN=EXCESS_MIN),
    )

    # strip bulky per_u before JSON (keep reduced medians)
    reduced = {k: v for k, v in res.items() if k != "per_u"}
    reduced["max_strain"] = float(np.max([
        r["max_strain"] for u in res["per_u"] for kk in res["per_u"][u]
        for r in res["per_u"][u][kk]
    ]))
    reduced["energy_drift_max"] = float(np.max([
        r["energy_drift"] for u in res["per_u"] for kk in res["per_u"][u]
        for r in res["per_u"][u][kk]
    ]))
    out = out_dir / f"two_tank_decoherence_check_{tag}.json"
    out.write_text(json.dumps(reduced, indent=2, default=float))

    print(f"[{tag}] verdict = {res['verdict']}  ({res['wall_seconds']} s)")
    print(f"  {res['verdict_meaning']}")
    print(f"  summary = {res['summary']}")
    print(f"  max_strain = {reduced['max_strain']:.4f}  (R_I={R_I:.4f}, R_II={R_II:.3f})")
    print(f"  energy_drift_max = {reduced['energy_drift_max']:.2e}  -> {out}")
    return res


if __name__ == "__main__":
    main()
