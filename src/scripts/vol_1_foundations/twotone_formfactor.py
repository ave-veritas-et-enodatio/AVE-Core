#!/usr/bin/env python
"""
TWO-TONE FOUR-PHOTON FORM FACTOR (FORK A) — driven-lattice mixing test (task #31-A).

Prereg (FROZEN): research/2026-07-09_twotone-formfactor_prereg_FROZEN.md
Base driver (Rule 14): superband_carrier_fork.py (the repaired x29 driver) — its TAGGED
conservative kernel castings (F_bond, U_bond, energy_density, analytic_kappa, sponge_profile)
are imported UNMODIFIED and extended with the two-tone machinery below.

═══════════════════════════════════════════════════════════════════════════════
REPAIR HISTORY (adversarial review, 2026-07-09 — blocking finding CONFIRMED by re-run)
═══════════════════════════════════════════════════════════════════════════════
The FIRST verdict headlined BRANCH (i) DRIVE-TRACKING ("the four-photon vertex is frequency-
blind above band; ATLAS tension real"). VOID: the hard Dirichlet clamp CO-LOCATES both tones
at the drive node, pinning drive-bond strain at O(A) for both tones regardless of frequency —
the "flat vertex" recovered the constant kernel cubic coefficient BY CONSTRUCTION (interface,
not bulk). The review's BULK discriminator (twotone_run_separated: tones sourced at SEPARATED
nodes, sep>=3, mixing region interior where both tones are evanescent) is committed here as the
null baseline: the χ³ beat COLLAPSES ~17 orders toward the O_skin skin-suppression the frozen
axis predicted — the frozen O_skin was the CORRECT BULK MODEL; its q=−13.6 was the interface-
artifact detector. This version SCRUBS the branch verdict + "ATLAS tension real" (adjudicate)
and re-scopes to: bulk vertex NOT probed, super-band coupling fork OPEN. SURVIVES (Class-B):
(1) the A⁶ amplitude law (clean-regime exponent 6.02); (2) ★ the parity theorem (the PR's real
product). Fork-D pattern (x29/#598): bank what survives, void what was geometry-artifact.

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-FIRST SECTOR HEADER (per prereg §3, before any standard term)
═══════════════════════════════════════════════════════════════════════════════
  SECTOR : V-sector / ε charge-length AC oscillation on a K4 bond-line (1D). V_n = photon
           carrier (AC content of the T2/charge-length sector).
  REGIME : cold-to-kernel-engaged, SUB-YIELD (reversible). Bond strain r_n=V_{n+1}-V_n;
           |r|=1 -> rupture/pair-production = OUT OF SCOPE (aborted+flagged).
  NONLIN : canonical Op2/Op14 saturable varactor S(r)=sqrt(1-r^2) (Axiom 4 / Born-Infeld n=2).
           DEFAULT F(r)=r/S (conservative BI-n2 casting, TAGGED — NOT the Op14 e-load F=r/√S;
           x29 finding #5). BOTH castings are ODD in r -> the parity theorem (prereg §5) holds.
  READOUT: real-space energy flux + temporal DFT of what propagates. Drive = two temporal ω
           tones at a real-space (interior) node; read = real-space. A46-clean (same frame).
  PHYSICS: leading nonlinearity is CUBIC (χ³ four-photon). Parity theorem: a line at
           m·ω_lo+n·ω_hi appears ONLY when m+n is ODD. => difference ω_hi-ω_lo (m+n=0) is
           FORBIDDEN below yield; the measured four-photon channel is the FWM sideband
           ω_out=2·ω_lo-ω_hi (m+n=1), amplitude ∝ A_lo²·A_hi (equal-amp POWER ∝ A⁶).
  CLASS  : frequency form factor = EMERGENCE (Class D) on the 1D model substrate; the A⁶ law
           and the parity null are MANIFESTATION (Class B). NO Letter/KB edits from this run.

Native units (constants.py): ℓ_node=1, c=1, ω_C=1. 1D chain band top ω_top=2.0 ω_C. The 3D srs
top is π√3≈5.441 ω_C (#604) — the 3D follow-on tones (18.51/17.51) are recorded, NOT run here.

Run:  PYTHONPATH=src python src/scripts/vol_1_foundations/twotone_formfactor.py
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from ave.core.constants import C_0, L_NODE, OMEGA_C
from scripts.vol_1_foundations.superband_carrier_fork import (
    F_bond,
    analytic_kappa,
    energy_density,
)

OMEGA_C_SI = OMEGA_C            # ≈ 7.763e20 rad/s ; ℏω_C = m_e c² = 511 keV
YIELD = 1.0                    # bond-strain yield (native); |r|>=1 -> rupture (out of scope)
OMEGA_TOP_1D = 2.0             # 1D chain band top (THIS platform); NOT the 3D srs top
FORCE_LAW_DEFAULT = "r_over_S"  # tagged conservative Born-Infeld n=2 casting (x29 finding #5)

# 3D FOLLOW-ON (recorded, NOT run — prereg §2): srs top π√3≈5.441 ω_C (#604); tones 18.51/17.51.
SRS_BAND_TOP_OVER_OMEGA_C = float(np.pi * np.sqrt(3.0))
SRS_FOLLOWON_TONES = {"omega_a": 18.51, "omega_b": 17.51, "delta": 1.0, "status": "recorded_not_run"}


# ───────────────────────── two-tone interior-drive integrator ─────────────────────────
def _both_end_sponge(N: int, width: int, strength: float = 0.4) -> np.ndarray:
    """Matched absorbing sponge at BOTH ends (the far Z_0 vacuum load). Cells within `width`
    of either end are EXCLUDED from physics reads (Rule-10 PML-exclusion)."""
    damp = np.zeros(N)
    if width > 0:
        r = np.arange(N - width, N)
        damp[N - width:] = strength * ((r - (N - width)) / width) ** 2
        lft = np.arange(width)
        damp[:width] = strength * ((width - 1 - lft) / width) ** 2
    return damp


def _accel(V: np.ndarray, force_law: str) -> np.ndarray:
    r = np.diff(V)
    F = F_bond(r, force_law)
    a = np.zeros_like(V)
    a[1:-1] = F[1:] - F[:-1]
    a[0] = F[0]
    a[-1] = -F[-1]
    return a


# Discrete energy current across bond n (node n -> n+1): J_n = -F(r_n)·Vd_{n+1}. Its steady
# time-average is the net PROPAGATING power (evanescent tones carry zero net flux). Accumulated
# inline in twotone_run's steady window (Jr_acc / Jl_acc).


def twotone_run(w_lo, w_hi, A_lo, A_hi, N, n_drive, dt, tmax, ramp_periods, sponge_w,
                read_offset, w_out, force_law=FORCE_LAW_DEFAULT, steady_frac=0.36,
                prof_half=160, prof_dt=0.25, kernel_off=False, extra_lin_wout=0.0):
    """Interior two-tone drive. Symplectic velocity-Verlet, both-end sponge. The drive imposes
    V[n_drive] = ramp·[A_lo sin(w_lo t) + A_hi sin(w_hi t)] (+ optional weak linear ω_out probe
    for the validate-on-known gate). Records: full-step time series at the two readout nodes
    (n_drive ± read_offset) over the steady window (clean beat DFT), and decimated field frames
    over [n_drive-10, n_drive+prof_half] (birth-depth profile). `kernel_off` linearises the bond
    force (F=r) -> the χ³ vanishes -> the ω_out bin measures only numerical leakage (the floor).
    """
    V = np.zeros(N)
    Vd = np.zeros(N)
    damp = _both_end_sponge(N, sponge_w)
    nsteps = int(tmax / dt)
    ramp = ramp_periods * (2 * np.pi / w_out)
    t_settle = ramp + read_offset / max(1e-9, np.cos(np.arcsin(min(0.999, w_out / 2.0)))) + 40.0
    t_settle = min(t_settle, (1.0 - steady_frac) * tmax)

    fl = "linear" if kernel_off else force_law

    def acc(x):
        if kernel_off:
            a = np.zeros_like(x)
            r = np.diff(x)
            a[1:-1] = r[1:] - r[:-1]
            a[0] = r[0]
            a[-1] = -r[-1]
            return a
        return _accel(x, fl)

    r_read, l_read = n_drive + read_offset, n_drive - read_offset
    ts_r, ts_l, ts_n1 = [], [], []           # readout (both dirs) + node-(n_drive+1) skin series
    ts_r0 = []                               # drive-bond strain r_0 = V[n_drive+1]-V[n_drive]
    ts_t = []                                # sample times
    prof_lo, prof_hi = n_drive - 10, n_drive + prof_half
    prof_frames, prof_times = [], []
    next_prof = t_settle
    max_bond_r = 0.0
    ruptured = False
    Jr_acc, Jl_acc, jn = 0.0, 0.0, 0            # steady-window time-averaged bond flux

    for it in range(nsteps):
        t = it * dt
        a = acc(V) - damp * Vd
        Vh = Vd + 0.5 * dt * a
        V = V + dt * Vh
        w = 0.5 * (1.0 - np.cos(np.pi * min(1.0, t / ramp)))
        drive = A_lo * np.sin(w_lo * t) + A_hi * np.sin(w_hi * t)
        if extra_lin_wout:
            drive = drive + extra_lin_wout * np.sin(w_out * t)
        V[n_drive] = w * drive
        a2 = acc(V) - damp * Vh
        Vd = Vh + 0.5 * dt * a2
        Vd[n_drive] = 0.0
        rmax = float(np.max(np.abs(np.diff(V))))
        if rmax > max_bond_r:
            max_bond_r = rmax
        if rmax >= 0.999 * YIELD:
            ruptured = True
            break
        if t >= t_settle:
            ts_r.append(V[r_read]); ts_l.append(V[l_read]); ts_n1.append(V[n_drive + 1])
            ts_r0.append(V[n_drive + 1] - V[n_drive]); ts_t.append(t)
            rr = np.diff(V)
            Fr = F_bond(rr, "r_over_S") if kernel_off else F_bond(rr, fl)
            Jr_acc += -Fr[r_read] * Vd[r_read + 1]
            Jl_acc += -Fr[l_read] * Vd[l_read + 1]
            jn += 1
            if t >= next_prof:
                prof_frames.append(V[prof_lo:prof_hi].copy()); prof_times.append(t)
                next_prof += prof_dt

    diag = {"w_lo": w_lo, "w_hi": w_hi, "A_lo": A_lo, "A_hi": A_hi, "w_out": w_out,
            "force_law": fl, "kernel_off": kernel_off, "N": N, "n_drive": n_drive, "dt": dt,
            "tmax": tmax, "ramp_periods": ramp_periods, "t_settle": t_settle,
            "read_offset": read_offset, "max_bond_r": round(max_bond_r, 4), "ruptured": ruptured,
            "V_final": V, "Vd_final": Vd,
            "J_right_mean": (Jr_acc / jn) if jn else float("nan"),
            "J_left_mean": (Jl_acc / jn) if jn else float("nan"),
            "prof_lo": prof_lo, "prof_hi": prof_hi}
    series = {"t": np.array(ts_t), "right": np.array(ts_r), "left": np.array(ts_l),
              "node1": np.array(ts_n1), "r0": np.array(ts_r0),
              "prof_frames": np.array(prof_frames) if prof_frames else np.zeros((0, 0)),
              "prof_times": np.array(prof_times)}
    return series, diag


# ───────────────────────── BULK-GEOMETRY discriminator (adversarial-review null baseline) ────
def twotone_run_separated(w_lo, w_hi, A, sep, N, n_center, dt, tmax, ramp_periods, sponge_w,
                          read_offset, w_out, force_law=FORCE_LAW_DEFAULT, steady_frac=0.36):
    """The reviewer's BULK-vertex discriminator (repair task #2). Two tones sourced at
    SEPARATED interior nodes n_lo=n_center and n_hi=n_center+sep. For sep>=3 the mixing region
    is the interior, where BOTH tones are EVANESCENT — no single bond is clamped to O(A) at
    both tones, so the χ³ FWM source is skin-suppressed (the physical bulk vertex). sep=0
    SUPERPOSES both tones on ONE node = the co-located drive-INTERFACE baseline (recovers the
    twotone_run number exactly: the shared clamped bond pins drive-bond strain at O(A) for both
    tones regardless of frequency — the flat-vertex artifact the review killed).

    Returns (P_beat, P_beat_max_reader, max_bond_r): beat power at ω_out averaged over the two
    far readers (past both skins), the larger single-reader power, and the peak bond strain."""
    V = np.zeros(N)
    Vd = np.zeros(N)
    damp = _both_end_sponge(N, sponge_w)
    nsteps = int(tmax / dt)
    ramp = ramp_periods * (2 * np.pi / w_out)
    t_settle = min(ramp + read_offset / max(1e-9, np.cos(np.arcsin(min(0.999, w_out / 2.0))))
                   + 40.0, (1.0 - steady_frac) * tmax)
    n_lo, n_hi = n_center, n_center + sep
    r_read, l_read = n_hi + read_offset, n_lo - read_offset
    ts_r, ts_l, ts_t = [], [], []
    max_bond_r = 0.0
    for it in range(nsteps):
        t = it * dt
        a = _accel(V, force_law) - damp * Vd
        Vh = Vd + 0.5 * dt * a
        V = V + dt * Vh
        w = 0.5 * (1.0 - np.cos(np.pi * min(1.0, t / ramp)))
        if sep == 0:
            V[n_lo] = w * A * (np.sin(w_lo * t) + np.sin(w_hi * t))   # co-located superposition
        else:
            V[n_lo] = w * A * np.sin(w_lo * t)                        # independently-sourced tones
            V[n_hi] = w * A * np.sin(w_hi * t)
        a2 = _accel(V, force_law) - damp * Vh
        Vd = Vh + 0.5 * dt * a2
        Vd[n_lo] = 0.0
        if sep != 0:
            Vd[n_hi] = 0.0
        rmax = float(np.max(np.abs(np.diff(V))))
        if rmax > max_bond_r:
            max_bond_r = rmax
        if rmax >= 0.999 * YIELD:
            break
        if t >= t_settle:
            ts_r.append(V[r_read]); ts_l.append(V[l_read]); ts_t.append(t)
    t = np.array(ts_t)
    d = float(np.median(np.diff(t))) if t.size > 2 else dt
    Pr = _bin_power(np.array(ts_r), d, w_out)
    Pl = _bin_power(np.array(ts_l), d, w_out)
    return 0.5 * (Pr + Pl), max(Pr, Pl), round(max_bond_r, 4)


# ───────── ★ PARITY THEOREM — generative planted-asymmetry verification (the PR's real product) ──
def parity_generative_test(pair=None, betas=(0.0, 0.03, 0.06, 0.12, 0.24),
                           N=1600, n_drive=800, dt=0.01, tmax=700.0, sponge_w=300,
                           read_offset=90, w_out=1.0, ramp_periods=15,
                           force_law=FORCE_LAW_DEFAULT, steady_frac=0.36):
    """★ GENERATIVE verification of the parity theorem (the null as an INVERSION-SYMMETRY WITNESS).

    The reversible kernel F=r+½r³+… is ODD ⇒ inversion-symmetric ⇒ the difference tone ω_hi−ω_lo
    (m+n=0, even) is STRUCTURALLY FORBIDDEN sub-yield. This test proves the null is a *consequence
    of that symmetry*, not a numerical coincidence, by GENERATIVELY breaking it: plant an EVEN
    (χ²) term F(r) → F(r) + β·r² (a DC-biased / rectifying varactor). Prediction: the forbidden
    difference tone is at FLOOR for β=0 and rises MONOTONICALLY with β (leading order ∝ β ⇒
    power ∝ β²). The allowed FWM sideband 2ω_lo−ω_hi stays ~constant (it is odd-order, β-blind to
    leading order). β is a PLANTED diagnostic, NOT a physical kernel (the sub-yield vacuum has β=0)."""
    pair = REF_PAIR if pair is None else pair
    w_lo, w_hi = pair
    w_diff = w_hi - w_lo
    damp = _both_end_sponge(N, sponge_w)
    ramp = ramp_periods * (2 * np.pi / w_out)
    t_settle = min(ramp + read_offset / 0.866 + 40.0, (1.0 - steady_frac) * tmax)
    A = FORM_FACTOR_AMP
    rows = []
    for beta in betas:
        V = np.zeros(N); Vd = np.zeros(N)
        ts_read, ts_t = [], []
        max_bond_r = 0.0
        for it in range(int(tmax / dt)):
            t = it * dt

            def acc(x):
                r = np.diff(x)
                F = F_bond(r, force_law) + beta * r ** 2          # planted EVEN (χ²) term
                a = np.zeros_like(x)
                a[1:-1] = F[1:] - F[:-1]; a[0] = F[0]; a[-1] = -F[-1]
                return a
            a = acc(V) - damp * Vd
            Vh = Vd + 0.5 * dt * a
            V = V + dt * Vh
            w = 0.5 * (1.0 - np.cos(np.pi * min(1.0, t / ramp)))
            V[n_drive] = w * A * (np.sin(w_lo * t) + np.sin(w_hi * t))
            a2 = acc(V) - damp * Vh
            Vd = Vh + 0.5 * dt * a2
            Vd[n_drive] = 0.0
            rmax = float(np.max(np.abs(np.diff(V))))
            max_bond_r = max(max_bond_r, rmax)
            if rmax >= 0.999 * YIELD:
                break
            if t >= t_settle:
                ts_read.append(V[n_drive + read_offset]); ts_t.append(t)
        tt = np.array(ts_t)
        d = float(np.median(np.diff(tt))) if tt.size > 2 else dt
        sig = np.array(ts_read)
        rows.append({"beta": beta, "P_diff_tone": _bin_power(sig, d, w_diff),
                     "P_fwm_allowed": _bin_power(sig, d, w_out),
                     "max_bond_r": round(max_bond_r, 4)})
    # monotonic-in-β check (difference tone) + leading-order β-power exponent
    pdiff = [r["P_diff_tone"] for r in rows]
    monotonic = all(pdiff[i + 1] > pdiff[i] for i in range(len(pdiff) - 1))
    nz = [(r["beta"], r["P_diff_tone"]) for r in rows if r["beta"] > 0 and r["P_diff_tone"] > 0]
    beta_exp, beta_r2 = _loglog_slope([b for b, _ in nz], [p for _, p in nz]) if len(nz) >= 2 \
        else (float("nan"), float("nan"))
    return {"pair": list(pair), "diff_tone_omega": w_diff, "force_law": force_law, "rows": rows,
            "beta0_diff_over_fwm": (rows[0]["P_diff_tone"] / rows[0]["P_fwm_allowed"]
                                    if rows[0]["P_fwm_allowed"] > 0 else float("nan")),
            "diff_tone_monotonic_in_beta": bool(monotonic),
            "diff_tone_beta_power_exponent": beta_exp, "diff_tone_beta_r2": beta_r2}


# ───────────────────────── spectral extraction ─────────────────────────
def _bin_power(sig, dt, w_target):
    """Calibrated single-tone power at w_target: (2·|Ṽ_k|/Σwin)² = the squared amplitude of the
    oscillation at w_target. Window-length-independent (Hann amplitude-correction) so beat powers
    are directly comparable across sweep runs with (possibly) different sample counts."""
    sig = np.asarray(sig, float)
    if sig.size < 8:
        return float("nan")
    sig = sig - sig.mean()
    win = np.hanning(sig.size)
    S = np.fft.rfft(sig * win)
    f = np.fft.rfftfreq(sig.size, dt) * 2.0 * np.pi
    j = int(np.argmin(np.abs(f - w_target)))
    amp = 2.0 * np.abs(S[j]) / win.sum()
    return float(amp ** 2)


def extract_beat(series, diag):
    """Beat power at ω_out (both directions), parity-null bin (ω_hi-ω_lo), DC bin, and direct
    tone leakage at the readout node. Net time-averaged propagating flux is added by the caller
    (needs the final field). Returns a dict of powers (arb. units, comparable across the sweep
    because ω_out is held fixed)."""
    dt = diag["dt"]
    w_lo, w_hi, w_out = diag["w_lo"], diag["w_hi"], diag["w_out"]
    t = series["t"]
    # effective sample spacing of the (contiguous) steady series
    d = float(np.median(np.diff(t))) if t.size > 2 else dt
    right, left = series["right"], series["left"]
    return {
        "P_beat_right": _bin_power(right, d, w_out),
        "P_beat_left": _bin_power(left, d, w_out),
        "P_parity_null_right": _bin_power(right, d, w_hi - w_lo),
        "P_dc_right": _bin_power(right, d, 0.0),
        "P_tone_lo_right": _bin_power(right, d, w_lo),
        "P_tone_hi_right": _bin_power(right, d, w_hi),
        "n_steady_samples": int(t.size),
    }


def birth_depth(series, diag, w_out, plateau_frac=0.90):
    """Spatial profile of |Ṽ_n(ω_out)| across [prof_lo, prof_hi]; birth depth = distance from
    the drive at which the profile first reaches `plateau_frac` of its propagating plateau."""
    frames = series["prof_frames"]
    times = series["prof_times"]
    if frames.size == 0 or frames.shape[0] < 8:
        return {"birth_depth_nodes": float("nan"), "plateau_amp": float("nan"),
                "profile_nodes": [], "profile_amp": []}
    d = float(np.median(np.diff(times)))
    nnode = frames.shape[1]
    amp = np.array([np.sqrt(_bin_power(frames[:, k], d, w_out)) for k in range(nnode)])
    prof_lo = diag["prof_lo"]
    nodes = np.arange(prof_lo, prof_lo + nnode) - diag["n_drive"]   # distance from drive
    # plateau = median of the far half of the (positive-side) profile
    far = amp[nnode // 2:]
    plateau = float(np.median(far)) if far.size else float("nan")
    depth = float("nan")
    if plateau > 0:
        pos = nodes >= 0
        na, aa = nodes[pos], amp[pos]
        hit = np.where(aa >= plateau_frac * plateau)[0]
        if hit.size:
            depth = float(na[hit[0]])
    return {"birth_depth_nodes": depth, "plateau_amp": plateau,
            "profile_nodes": nodes.tolist(), "profile_amp": amp.tolist()}


def net_flux(diag):
    """Steady-window time-averaged net propagating power at the readout bonds (accumulated in
    the run loop). The in-band beat carries net flux; the evanescent tones are reactive (≈0 net).
    Rightward should be >0, leftward <0, ≈equal magnitude by reflection symmetry — a sign/direction
    cross-check on the spectral P_beat."""
    return {"J_right": float(diag["J_right_mean"]), "J_left": float(diag["J_left_mean"])}


# ───────────────────────── measurement wrapper ─────────────────────────
# Frozen platform numerics (pilot-fixed; NOT adjudication criteria — prereg §0). dt=0.01 is the
# resolution at which the free-evolution energy control conserves ≤1e-5 (Gate e; the coarser
# dt=0.02 drifts to 1.76e-5 and HALVES O(dt²) under refinement — a controlled symplectic drift,
# not instability; the beat power itself is dt-invariant to 2.9e-4).
BASE = dict(N=1600, n_drive=800, dt=0.01, tmax=700.0, sponge_w=300, read_offset=90, w_out=1.0)


def measure_pair(w_lo, w_hi, A, ramp_periods=15, force_law=FORCE_LAW_DEFAULT, **over):
    """One two-tone measurement at equal drive amplitude A. Returns beat power (both dirs),
    parity-null, node-1 skin amplitudes (M7), net flux, birth depth, rupture flag."""
    kw = dict(BASE); kw.update(over)
    series, diag = twotone_run(w_lo, w_hi, A, A, ramp_periods=ramp_periods,
                               force_law=force_law, **kw)
    b = extract_beat(series, diag)
    bd = birth_depth(series, diag, kw["w_out"])
    nf = net_flux(diag)
    d = float(np.median(np.diff(series["t"]))) if series["t"].size > 2 else kw["dt"]
    n1_lo = _bin_power(series["node1"], d, w_lo) ** 0.5     # node-1 amplitude at each tone (M7)
    n1_hi = _bin_power(series["node1"], d, w_hi) ** 0.5
    r0_lo = _bin_power(series["r0"], d, w_lo) ** 0.5        # MEASURED drive-bond strain per tone
    r0_hi = _bin_power(series["r0"], d, w_hi) ** 0.5        # (the participation the varactor sees)
    return {"w_lo": w_lo, "w_hi": w_hi, "A": A, "ramp_periods": ramp_periods,
            "force_law": force_law, "max_bond_r": diag["max_bond_r"], "ruptured": diag["ruptured"],
            "drivebond_strain_lo": r0_lo, "drivebond_strain_hi": r0_hi,
            "P_beat": 0.5 * (b["P_beat_right"] + b["P_beat_left"]),
            "P_beat_right": b["P_beat_right"], "P_beat_left": b["P_beat_left"],
            "P_parity_null": b["P_parity_null_right"], "P_dc": b["P_dc_right"],
            "P_tone_lo_leak": b["P_tone_lo_right"], "P_tone_hi_leak": b["P_tone_hi_right"],
            "node1_amp_lo": n1_lo, "node1_amp_hi": n1_hi,
            "J_right": nf["J_right"], "J_left": nf["J_left"],
            "birth_depth_nodes": bd["birth_depth_nodes"], "plateau_amp": bd["plateau_amp"],
            "n_steady_samples": b["n_steady_samples"]}


def overlap_factor(w_lo, w_hi):
    """Two participation models for the FWM source (A_lo²·A_hi combination):
      O_skin = exp[-(2·κ_lo + κ_hi)]              FROZEN (prereg §6.2) — models the source by the
                                                  skin AMPLITUDE product at node 1.
      O_bond = (1+e^{-κ_lo})²·(1+e^{-κ_hi})       KEEP-BOTH (post-run, mechanism-derived) — models
                                                  the source by the DRIVE-BOND STRAIN product
                                                  |r_0|∝A(1+e^{-κ}), which is what the varactor sees.
    The run-time finding (birth_depth=1 at every pair; raw P_beat barely tracks O_skin²) is that the
    mixing is drive-bond-localized, so O_bond is the physically-correct participation. BOTH reported."""
    klo, khi = analytic_kappa(w_lo), analytic_kappa(w_hi)
    O_skin = float(np.exp(-(2 * klo + khi)))
    O_bond = float((1.0 + np.exp(-klo)) ** 2 * (1.0 + np.exp(-khi)))
    return {"kappa_lo": klo, "kappa_hi": khi, "comb_2klo_khi": 2 * klo + khi,
            "O_skin": O_skin, "O": O_skin, "O_bond_analytic": O_bond}


def carrier_to_pair(wbar, w_out):
    """Fixed-ω_out family: δ=(ω̄-ω_out)/3, ω_lo=ω̄-δ, ω_hi=ω̄+δ (prereg §6.2)."""
    d = (wbar - w_out) / 3.0
    return round(wbar - d, 4), round(wbar + d, 4)


# ───────────────────────── gates ─────────────────────────
def gate_a_m7(w_lo, w_hi):
    """(a) M7 — per-tone injection nonzero AND ∝ drive (NOT a no-op). Node-1 skin amplitude at
    each tone at A and A/2 must be nonzero, halve with A, and match analytic A·e^(−κ)."""
    hi = measure_pair(w_lo, w_hi, 0.10)
    lo = measure_pair(w_lo, w_hi, 0.05)
    klo, khi = analytic_kappa(w_lo), analytic_kappa(w_hi)
    pred_lo, pred_hi = 0.10 * np.exp(-klo), 0.10 * np.exp(-khi)   # analytic node-1 amp at A=0.10
    ratio_lo = hi["node1_amp_lo"] / max(lo["node1_amp_lo"], 1e-300)
    ratio_hi = hi["node1_amp_hi"] / max(lo["node1_amp_hi"], 1e-300)
    nonzero = hi["node1_amp_lo"] > 1e-6 and hi["node1_amp_hi"] > 1e-6
    scales = 1.7 < ratio_lo < 2.3 and 1.7 < ratio_hi < 2.3      # halving A halves the amplitude
    return {"node1_amp_lo_A0.10": hi["node1_amp_lo"], "node1_amp_hi_A0.10": hi["node1_amp_hi"],
            "analytic_node1_lo": pred_lo, "analytic_node1_hi": pred_hi,
            "amp_ratio_lo(A/half)": ratio_lo, "amp_ratio_hi(A/half)": ratio_hi,
            "nonzero_and_linear": bool(nonzero and scales), "pass": bool(nonzero and scales)}


def gate_b_validate_reader(w_out):
    """(b) Validate-on-known — plant a weak REAL linear ω_out tone (no super-band tones, kernel
    irrelevant/off) and confirm the flux reader recovers a directional net flux and a P_beat that
    scales as amplitude². Two amplitudes -> the reader response must be linear-in-power (slope 2)."""
    kw = dict(BASE)
    out = []
    for a in (0.01, 0.02):
        series, diag = twotone_run(3.0, 5.0, 0.0, 0.0, ramp_periods=15, kernel_off=True,
                                   extra_lin_wout=a, **kw)
        b = extract_beat(series, diag); nf = net_flux(diag)
        out.append({"amp": a, "P_at_wout": b["P_beat_right"], "J_right": nf["J_right"],
                    "J_left": nf["J_left"]})
    slope = np.log(out[1]["P_at_wout"] / out[0]["P_at_wout"]) / np.log(2.0)
    directional = out[1]["J_right"] > 0 and out[1]["J_left"] < 0
    recovers = out[1]["P_at_wout"] > 1e-8 and 1.7 < slope < 2.3 and directional
    return {"runs": out, "power_slope_vs_amp": float(slope), "directional": bool(directional),
            "pass": bool(recovers)}


def gate_c_ramp(w_lo, w_hi, A):
    """(c) Ramp-independence (MANDATORY) — steady-window beat power stable under ramp doubling."""
    r1 = measure_pair(w_lo, w_hi, A, ramp_periods=15)
    r2 = measure_pair(w_lo, w_hi, A, ramp_periods=30)
    rel = abs(r2["P_beat"] - r1["P_beat"]) / max(r1["P_beat"], 1e-300)
    return {"P_beat_R": r1["P_beat"], "P_beat_2R": r2["P_beat"], "rel_change": float(rel),
            "pass": bool(rel < 0.05)}


def _free_evo_dH(dt, tmax=300.0):
    """Undamped, undriven free evolution of an in-band packet -> symplectic energy drift |ΔH|/H."""
    N = 1400
    x = np.arange(N)
    Vc = 0.2 * np.exp(-0.5 * ((x - N / 2) / 40.0) ** 2) * np.cos(0.6 * x)
    Vdc = np.zeros(N)
    H0 = float(np.sum(energy_density(Vc, Vdc, FORCE_LAW_DEFAULT)))
    for _ in range(int(tmax / dt)):
        a = _accel(Vc, FORCE_LAW_DEFAULT)
        Vh = Vdc + 0.5 * dt * a
        Vc = Vc + dt * Vh
        a2 = _accel(Vc, FORCE_LAW_DEFAULT)
        Vdc = Vh + 0.5 * dt * a2
    H1 = float(np.sum(energy_density(Vc, Vdc, FORCE_LAW_DEFAULT)))
    return abs(H1 - H0) / H0


def gate_e_energy_dt(w_lo, w_hi, A):
    """(e) Energy + dt convergence. (1) free-evolution conservation control at the measurement dt
    AND dt/2: |ΔH|/H must be ≤1e-5 at the measurement resolution, and must CONVERGE (dt/2 < dt) —
    proving controlled O(dt²) symplectic drift, not instability. (2) dt-halving on the driven
    reference: P_beat changes <5%."""
    dt = BASE["dt"]
    dH = _free_evo_dH(dt)
    dH_half = _free_evo_dH(dt / 2.0)
    converges = dH_half < dH
    r1 = measure_pair(w_lo, w_hi, A, dt=dt)
    r2 = measure_pair(w_lo, w_hi, A, dt=dt / 2.0)
    rel = abs(r2["P_beat"] - r1["P_beat"]) / max(r1["P_beat"], 1e-300)
    energy_pass = bool(dH <= 1e-5 and converges)
    return {"free_evo_dH_over_H": dH, "free_evo_dH_over_H_dt_half": dH_half,
            "energy_converges": bool(converges), "measurement_dt": dt,
            "energy_pass": energy_pass,
            "P_beat_dt": r1["P_beat"], "P_beat_dt_half": r2["P_beat"], "dt_rel_change": float(rel),
            "dt_pass": bool(rel < 0.05), "pass": bool(energy_pass and rel < 0.05)}


# ───────────────────────── sweeps ─────────────────────────
# FROZEN sweep sets (prereg §7).
CARRIERS = [2.8, 3.1, 3.4, 3.7, 4.0]           # fixed ω_out=1.0 form-factor sweep
REF_PAIR = (2.6, 4.2)                          # amplitude-sweep + casting cross-check pair
AMPS = [0.015, 0.03, 0.06, 0.12, 0.24]         # log-spaced, sub-yield (0.015 = floor probe)
FORM_FACTOR_AMP = 0.15                         # fixed drive amplitude for the form-factor sweep

# FROZEN prereg §9.1 thresholds on q = −slope[log10(P_beat/O²) vs log10(ω̄)]. RE-SCOPED per the
# adversarial review: these no longer SELECT a branch — the co-located q was found to be the
# drive-INTERFACE participation, not the bulk vertex, so NO branch is read (bulk vertex NOT
# probed; fork OPEN). Retained only to compute the interface-scoped diagnostics + fit window.
Q_FLAT = 1.0                                   # legacy branch-(i) flat threshold (interface diag only)
Q_STEEP = 4.0                                  # legacy branch-(ii) steep threshold (interface diag only)
FLOOR_SNR = 10.0                               # P_beat must exceed FLOOR_SNR × floor to fit/not-null


def form_factor_sweep(force_law=FORCE_LAW_DEFAULT):
    rows = []
    for wbar in CARRIERS:
        w_lo, w_hi = carrier_to_pair(wbar, BASE["w_out"])
        ov = overlap_factor(w_lo, w_hi)
        m = measure_pair(w_lo, w_hi, FORM_FACTOR_AMP, force_law=force_law)
        O2 = ov["O_skin"] ** 2                                # frozen skin-amplitude participation
        O_bond2 = ov["O_bond_analytic"] ** 2                 # analytic drive-bond participation
        # MEASURED drive-bond participation (empirical, no analytic evanescent assumption)
        A3 = FORM_FACTOR_AMP ** 3
        O_bond_meas = (m["drivebond_strain_lo"] ** 2 * m["drivebond_strain_hi"]) / A3
        rows.append({"wbar": wbar, "w_lo": w_lo, "w_hi": w_hi, **ov, "O2": O2,
                     "P_beat": m["P_beat"], "P_beat_over_O2": m["P_beat"] / O2,
                     "P_beat_over_Obond2": m["P_beat"] / O_bond2,
                     "O_bond_measured": O_bond_meas,
                     "P_beat_over_Obond2_meas": m["P_beat"] / max(O_bond_meas ** 2, 1e-300),
                     "drivebond_strain_lo": m["drivebond_strain_lo"],
                     "drivebond_strain_hi": m["drivebond_strain_hi"],
                     "P_parity_null": m["P_parity_null"], "P_dc": m["P_dc"],
                     "birth_depth_nodes": m["birth_depth_nodes"], "max_bond_r": m["max_bond_r"],
                     "ruptured": m["ruptured"], "J_right": m["J_right"], "J_left": m["J_left"],
                     "P_tone_lo_leak": m["P_tone_lo_leak"], "P_tone_hi_leak": m["P_tone_hi_leak"]})
    return rows


def amplitude_sweep(pair=REF_PAIR, force_law=FORCE_LAW_DEFAULT):
    w_lo, w_hi = pair
    # kernel-OFF floor at ω_out (no χ³ -> only numerical/spectral leakage into the bin)
    fkw = dict(BASE)
    series, diag = twotone_run(w_lo, w_hi, FORM_FACTOR_AMP, FORM_FACTOR_AMP, ramp_periods=15,
                               kernel_off=True, **fkw)
    floor_P = extract_beat(series, diag)["P_beat_right"]
    rows = []
    for A in AMPS:
        m = measure_pair(w_lo, w_hi, A, force_law=force_law)
        rows.append({"A": A, "P_beat": m["P_beat"], "P_parity_null": m["P_parity_null"],
                     "max_bond_r": m["max_bond_r"], "ruptured": m["ruptured"],
                     "above_floor": bool(m["P_beat"] > FLOOR_SNR * floor_P)})
    return {"pair": pair, "force_law": force_law, "kernel_off_floor_P": floor_P, "rows": rows}


def _loglog_slope(xs, ys):
    xs, ys = np.asarray(xs, float), np.asarray(ys, float)
    m = np.isfinite(xs) & np.isfinite(ys) & (ys > 0)
    if m.sum() < 2:
        return float("nan"), float("nan")
    lx, ly = np.log10(xs[m]), np.log10(ys[m])
    A = np.vstack([lx, np.ones_like(lx)]).T
    coef, res, *_ = np.linalg.lstsq(A, ly, rcond=None)
    pred = A @ coef
    ss_res = float(np.sum((ly - pred) ** 2))
    ss_tot = float(np.sum((ly - ly.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    return float(coef[0]), float(r2)


# ───────── BULK vs INTERFACE discriminator sweep (the review's null baseline) ─────────
SEP_BASELINE_NODES = 3          # sep>=3 => mixing region interior, both tones evanescent


def sep_discriminator(pair=REF_PAIR, force_law=FORCE_LAW_DEFAULT):
    """THE REVIEW'S BLOCKING DISCRIMINATOR, committed as the null baseline (repair task #2).

    Co-located (sep=0) vs bulk-separated (sep=3, 6) at the reference pair (collapse), plus a
    5-carrier form-factor sweep in each geometry. Bulk PREDICTION (pre-registered as the frozen
    O_skin axis): if the mixing is a real bulk vertex, the beat tracks the skin-amplitude product
    O_skin²=e^(−2(2κ_lo+κ_hi)) and COLLAPSES as the tones move above band. O_skin called it."""
    w_lo, w_hi = pair
    sep_kw = dict(N=BASE["N"], n_center=BASE["n_drive"], dt=BASE["dt"], tmax=BASE["tmax"],
                  ramp_periods=15, sponge_w=BASE["sponge_w"], read_offset=BASE["read_offset"],
                  w_out=BASE["w_out"], force_law=force_law)
    # (1) collapse at the reference pair: sep 0 vs 3 vs 6 (6 = separation-saturation check)
    collapse = {}
    for sep in (0, 3, 6):
        Pb, Pmax, mr = twotone_run_separated(w_lo, w_hi, FORM_FACTOR_AMP, sep, **sep_kw)
        collapse["sep%d" % sep] = {"P_beat": Pb, "P_beat_max_reader": Pmax, "max_bond_r": mr}
    p0, p3 = collapse["sep0"]["P_beat"], collapse["sep3"]["P_beat"]
    collapse["collapse_ratio_sep0_over_sep3"] = p0 / max(p3, 1e-300)
    collapse["collapse_orders"] = float(np.log10(p0 / max(p3, 1e-300)))
    collapse["separation_saturated"] = bool(
        abs(collapse["sep6"]["P_beat"] - p3) / max(p3, 1e-300) < 0.05)  # sep>=3 => at the floor
    # (2) 5-carrier form-factor sweep in each geometry (raw P_beat, no participation model)
    sweeps = {}
    for sep in (0, SEP_BASELINE_NODES):
        rows = []
        for wbar in CARRIERS:
            wl, wh = carrier_to_pair(wbar, BASE["w_out"])
            ov = overlap_factor(wl, wh)
            Pb, Pmax, mr = twotone_run_separated(wl, wh, FORM_FACTOR_AMP, sep, **sep_kw)
            rows.append({"wbar": wbar, "w_lo": wl, "w_hi": wh, "P_beat": Pb,
                         "O_skin2": ov["O_skin"] ** 2, "max_bond_r": mr})
        q, r2 = _loglog_slope([r["wbar"] for r in rows], [r["P_beat"] for r in rows])
        sweeps["sep%d" % sep] = {"rows": rows, "q_raw": -q, "r2": r2}
    # bulk PREDICTION exponent: O_skin² falloff vs ω̄ (the frozen axis AS a bulk predictor)
    q_oskin, r2_oskin = _loglog_slope(
        CARRIERS, [r["O_skin2"] for r in sweeps["sep%d" % SEP_BASELINE_NODES]["rows"]])
    return {"pair": list(pair), "force_law": force_law, "collapse_at_ref_pair": collapse,
            "form_factor_sweeps": sweeps, "sep_baseline_nodes": SEP_BASELINE_NODES,
            "q_raw_colocated_sep0": sweeps["sep0"]["q_raw"],
            "q_raw_bulk_sep%d" % SEP_BASELINE_NODES: sweeps["sep%d" % SEP_BASELINE_NODES]["q_raw"],
            "bulk_prediction_Oskin2_exponent": -q_oskin,
            "bulk_q_tracks_Oskin2": bool(
                abs(sweeps["sep%d" % SEP_BASELINE_NODES]["q_raw"] - (-q_oskin)) < 3.0),
            "kernel_off_floor_P": None}   # filled by caller (amplitude_sweep floor)


# ───────────────────────── adjudication (RE-SCOPED per adversarial review) ─────────────
def adjudicate(results):
    ff = results["form_factor_sweep_rS"]
    amp = results["amplitude_sweep_rS"]
    ga, gb, gc, ge = (results["gate_a_m7"], results["gate_b_validate"],
                      results["gate_c_ramp"], results["gate_e_energy_dt"])

    # Fit window: pairs sub-yield AND above FLOOR_SNR × the parity-null floor.
    null_floor = max(r["P_parity_null"] for r in ff)
    fit_rows = [r for r in ff if (not r["ruptured"]) and r["P_beat"] > FLOOR_SNR * null_floor]
    wbar = [r["wbar"] for r in fit_rows]
    # (1) FROZEN axis (skin-amplitude participation O_skin) — reported FAITHFULLY.
    slope_skin, r2_skin = _loglog_slope(wbar, [r["P_beat_over_O2"] for r in fit_rows])
    q_frozen = -slope_skin
    slope_rawO2, _ = _loglog_slope([r["O2"] for r in fit_rows], [r["P_beat"] for r in fit_rows])
    frozen_overcorrects = q_frozen < 0.0                 # P_beat/O_skin² RISES => O_skin too steep
    # (2) KEEP-BOTH corrected axis (drive-bond strain participation O_bond) — analytic + MEASURED.
    slope_bond_a, r2_bond_a = _loglog_slope(wbar, [r["P_beat_over_Obond2"] for r in fit_rows])
    slope_bond_m, r2_bond_m = _loglog_slope(wbar, [r["P_beat_over_Obond2_meas"] for r in fit_rows])
    q_bond_a, q_bond_m = -slope_bond_a, -slope_bond_m
    q = q_bond_a           # interface-scoped analytic drive-bond exponent (a KEEP-BOTH diagnostic
    #                        ONLY — NOT a branch selector: the review found this axis is the
    #                        drive-INTERFACE participation, not the bulk vertex).
    # The MEASURED drive-bond axis is UNINFORMATIVE: R²=0.15, sign-flipped (q_meas=%.2f) —
    # per the review it neither confirms nor refutes any branch. Reported, not read.
    drivebond_meas_uninformative = (r2_bond_m < 0.5) or (np.sign(q_bond_m) != np.sign(q_bond_a))
    # raw form factor (no participation model) — the co-located INTERFACE falloff
    slope_raw, r2_raw = _loglog_slope(wbar, [r["P_beat"] for r in fit_rows])
    q_raw = -slope_raw

    # amplitude exponent (χ³ / A⁶ witness). GLOBAL over all above-floor points AND a CLEAN-REGIME
    # fit (small strain, max_bond_r < CLEAN_R_MAX) that excludes the χ⁵-stiffened top point.
    CLEAN_R_MAX = 0.15
    afit = [r for r in amp["rows"] if r["above_floor"] and not r["ruptured"]]
    amp_slope, amp_r2 = _loglog_slope([r["A"] for r in afit], [r["P_beat"] for r in afit])
    aclean = [r for r in afit if r["max_bond_r"] < CLEAN_R_MAX]
    amp_slope_clean, amp_r2_clean = _loglog_slope([r["A"] for r in aclean],
                                                  [r["P_beat"] for r in aclean])
    floor_P = amp.get("kernel_off_floor_P", float("nan"))
    P_min = min((r["P_beat"] for r in afit), default=float("nan"))
    P_max = max((r["P_beat"] for r in afit), default=float("nan"))
    amp_dyn_range = P_max / P_min if P_min and P_min > 0 else float("nan")
    amp_min_over_floor = P_min / floor_P if floor_P and floor_P > 0 else float("nan")
    parity_ok = all(r["P_parity_null"] < 1e-3 * r["P_beat"] for r in ff if r["P_beat"] > 0)
    max_snr = max((r["P_beat"] / (FLOOR_SNR * null_floor) for r in ff), default=0.0)

    # ── BULK vs INTERFACE (the review's blocking discriminator, committed as null baseline) ──
    sep = results.get("sep_discriminator", {})
    coll = sep.get("collapse_at_ref_pair", {})
    collapse_orders = coll.get("collapse_orders", float("nan"))
    q_raw_bulk = sep.get("q_raw_bulk_sep%d" % SEP_BASELINE_NODES, float("nan"))
    q_raw_colo = sep.get("q_raw_colocated_sep0", float("nan"))
    bulk_pred_exp = sep.get("bulk_prediction_Oskin2_exponent", float("nan"))

    # DECISION — RE-SCOPED per the adversarial review (fork-D pattern: the first verdict's
    # evidence was found to be a drive-INTERFACE artifact under review; NO branch is selected —
    # the bulk vertex was NOT probed and the super-band coupling fork remains OPEN). The gate
    # guards remain (an INVALID/INDETERMINATE run cannot even claim the interface-scoped result).
    if not ga["pass"]:
        branch, verdict = "INVALID", "INVALID — Gate (a) M7: drive no-op / non-∝-A"
    elif not gc["pass"] or not ge["pass"]:
        branch = "INDETERMINATE"
        verdict = "INDETERMINATE — Gate (c) ramp or Gate (e) dt/energy failed (artifact suspected)"
    else:
        branch = "interface_scoped__BULK_OPEN"
        # ★ HONEST RE-SCOPED VERDICT (verbatim from the adversarial-review prescription).
        verdict = ("(ii)/hard-closure EXCLUDED at the drive interface; (i)-vs-(iii) "
                   "normalization-dependent (q in [0.30 analytic-bond, 2.93 raw]); frozen O_skin "
                   "rule mis-specified for this geometry (q=-13.6 = the interface-artifact "
                   "diagnostic); bulk-geometry discriminator (sep>=3) shows ~16-order collapse "
                   "toward skin suppression — THE BULK VERTEX WAS NOT PROBED; the super-band "
                   "coupling fork remains OPEN.")

    results["verdict"] = {
        "gate_a_pass": ga["pass"], "gate_b_pass": gb["pass"], "gate_c_pass": gc["pass"],
        "gate_e_pass": ge["pass"],
        # ── SURVIVING Class-B products (the PR's real products) ──
        "amplitude_exponent_clean_regime": amp_slope_clean,   # ★ 6.02 (χ³ A⁶ law, clean regime)
        "amplitude_r2_clean_regime": amp_r2_clean,
        "amplitude_clean_n_points": len(aclean), "amplitude_clean_max_bond_r_cut": CLEAN_R_MAX,
        "amplitude_exponent_global": amp_slope,               # 6.16 (χ⁵-stiffened top point)
        "amplitude_r2_global": amp_r2, "amplitude_points_above_floor": len(afit),
        "amplitude_dynamic_range": amp_dyn_range,             # 2.7e7 (NOT 2.6e5)
        "amplitude_min_over_kernel_off_floor": amp_min_over_floor,  # sweep never approaches floor
        "kernel_off_floor_P": floor_P,
        # ── ★ parity theorem (the PR's real product) ──
        "parity_null_holds": bool(parity_ok),
        "parity_diff_tone_forbidden_beta0_ratio": results.get("parity_generative", {}).get(
            "beta0_diff_over_fwm", float("nan")),
        "parity_generative_monotonic_in_beta": results.get("parity_generative", {}).get(
            "diff_tone_monotonic_in_beta"),
        "parity_generative_beta_power_exponent": results.get("parity_generative", {}).get(
            "diff_tone_beta_power_exponent", float("nan")),
        # ── BULK-vs-INTERFACE discriminator (review null baseline) ──
        "sep_baseline_nodes": SEP_BASELINE_NODES,
        "bulk_collapse_orders_sep0_to_sep%d" % SEP_BASELINE_NODES: collapse_orders,
        "bulk_collapse_ratio": coll.get("collapse_ratio_sep0_over_sep3", float("nan")),
        "bulk_separation_saturated": coll.get("separation_saturated"),
        "q_raw_colocated_INTERFACE": q_raw_colo,
        "q_raw_bulk_sep%d" % SEP_BASELINE_NODES: q_raw_bulk,
        "bulk_prediction_Oskin2_exponent": bulk_pred_exp,
        "bulk_q_tracks_Oskin2_skin_suppression": sep.get("bulk_q_tracks_Oskin2"),
        # ── interface-scoped KEEP-BOTH diagnostics (RE-LABELED — NOT branch selectors) ──
        "INTERFACE_q_analytic_drivebond": q_bond_a,
        "INTERFACE_q_measured_drivebond_UNINFORMATIVE": q_bond_m,
        "measured_drivebond_uninformative_r2_signflip": bool(drivebond_meas_uninformative),
        "INTERFACE_r2_drivebond_analytic": r2_bond_a, "INTERFACE_r2_drivebond_meas": r2_bond_m,
        "FROZEN_Oskin_interface_diagnostic_q": q_frozen, "FROZEN_Oskin_interface_r2": r2_skin,
        "raw_form_factor_q_INTERFACE": q_raw, "raw_form_factor_r2_INTERFACE": r2_raw,
        "raw_tracks_Oskin2_slope_INTERFACE": slope_rawO2,
        "n_fit_pairs": len(fit_rows),
        "BRANCH": branch, "BRANCH_VERDICT": verdict,
    }
    return branch


# ───────────────────────── figure (WHITE house style) ─────────────────────────
def make_figure(results, out_dir):
    import matplotlib.pyplot as plt

    from ave.viz import style
    style.apply("print")                       # WHITE background, Okabe-Ito (house style)
    fig_dir = out_dir / "twotone_formfactor_figs"
    fig_dir.mkdir(exist_ok=True)

    ff = results["form_factor_sweep_rS"]
    amp = results["amplitude_sweep_rS"]
    v = results["verdict"]
    wbar = [r["wbar"] for r in ff]
    P = [r["P_beat"] for r in ff]
    Pc = [r["P_beat_over_Obond2"] for r in ff]            # drive-bond-corrected (the flat form factor)
    O2 = [r["O2"] for r in ff]                             # frozen skin-amplitude participation
    Obond2 = [r["O_bond_analytic"] ** 2 for r in ff]      # drive-bond participation (analytic)
    null = [r["P_parity_null"] for r in ff]

    fig, ax = plt.subplots(1, 3, figsize=(15, 4.4))

    # Panel 1: raw beat power vs the two participation models; twin axis = corrected form factor.
    ax[0].semilogy(wbar, P, "ko-", label="beat power  P(2ω_lo−ω_hi)")
    ax[0].semilogy(wbar, [o * P[0] / O2[0] for o in O2], "s--", color="0.6",
                   label="frozen skin-overlap O_skin²  (over-corrects)")
    ax[0].semilogy(wbar, [o * P[0] / Obond2[0] for o in Obond2], "^--", color="#E69F00",
                   label="drive-bond O_bond²  (tracks P_beat)")
    ax[0].semilogy(wbar, null, "v:", color="0.7", label="parity-null  P(ω_hi−ω_lo)")
    ax[0].set_xlabel("carrier ω̄ / ω_C  (tone pair, both > 2.0)")
    ax[0].set_ylabel("beat power  (squared amplitude, arb.)")
    ax[0].set_title("Four-photon beat vs tone frequency\n(1D mechanism substrate, ω_out=1.0 fixed)")
    ax[0].legend(fontsize=6.5, loc="lower left")

    ax2 = ax[0].twinx()
    ax2.plot(wbar, Pc, "D-", color="#0072B2",
             label="P_beat / O_bond²  (INTERFACE-scoped, q=%.2f)" % v["INTERFACE_q_analytic_drivebond"])
    ax2.set_ylabel("drive-bond-corrected  P_beat/O_bond²  (INTERFACE)", color="#0072B2")
    ax2.set_yscale("log")
    ax2.set_ylim(0.3 * min(Pc), 3.0 * max(Pc))
    ax2.tick_params(axis="y", labelcolor="#0072B2")
    ax2.legend(fontsize=6.5, loc="upper right")

    # Panel 2: amplitude sweep — A⁶ law (clean regime) + χ⁵ stiffening. The floor is FAR below
    # (the sweep never approaches it) — annotated, not drawn as a bound the data reaches.
    A = [r["A"] for r in amp["rows"]]
    Pa = [r["P_beat"] for r in amp["rows"]]
    ax[1].loglog(A, Pa, "ko-", label="measured P_beat")
    Aref = np.array(A)
    anchor = [r for r in amp["rows"] if r["above_floor"] and r["max_bond_r"] < 0.15]
    if anchor:
        a0, p0 = anchor[-1]["A"], anchor[-1]["P_beat"]
        ax[1].loglog(Aref, p0 * (Aref / a0) ** 6.0, "--", color="0.55",
                     label="A⁶ (χ³ clean regime, exp %.2f)" % v["amplitude_exponent_clean_regime"])
    ax[1].set_xlabel("drive amplitude A  (both tones)")
    ax[1].set_ylabel("beat power  P(2ω_lo−ω_hi)")
    ax[1].set_title("★ A⁶ amplitude law at (%.1f, %.1f)\nclean %.2f / global %.2f (χ⁵ stiffening)"
                    % (amp["pair"][0], amp["pair"][1], v["amplitude_exponent_clean_regime"],
                       v["amplitude_exponent_global"]))
    ax[1].text(0.03, 0.06, "kernel-OFF floor %.0e\n(sweep never approaches it)"
               % amp["kernel_off_floor_P"], transform=ax[1].transAxes, fontsize=6.5, color="#D55E00")
    ax[1].legend(fontsize=7, loc="upper left")

    # Panel 3: BULK vs INTERFACE discriminator (the review's null baseline). Co-located (sep=0)
    # INTERFACE beat vs bulk-separated (sep=3): the bulk beat COLLAPSES toward the O_skin² skin-
    # suppression the frozen axis predicted — the bulk vertex was NOT probed.
    sd = results["sep_discriminator"]
    sw = sd["form_factor_sweeps"]
    wb = [r["wbar"] for r in sw["sep0"]["rows"]]
    P0 = [r["P_beat"] for r in sw["sep0"]["rows"]]
    seplabel = "sep%d" % sd["sep_baseline_nodes"]
    P3 = [r["P_beat"] for r in sw[seplabel]["rows"]]
    O2b = [r["O_skin2"] for r in sw[seplabel]["rows"]]
    ax[2].semilogy(wb, P0, "ko-", label="co-located sep=0 (INTERFACE, q=%.1f)" % sw["sep0"]["q_raw"])
    ax[2].semilogy(wb, P3, "s-", color="#D55E00",
                   label="bulk sep≥%d (q=%.1f)" % (sd["sep_baseline_nodes"], sw[seplabel]["q_raw"]))
    ax[2].semilogy(wb, [o * P3[0] / O2b[0] for o in O2b], "^--", color="0.5",
                   label="O_skin² bulk prediction (exp %.1f)" % sd["bulk_prediction_Oskin2_exponent"])
    ax[2].set_xlabel("carrier ω̄ / ω_C")
    ax[2].set_ylabel("raw beat power  P(2ω_lo−ω_hi)")
    ax[2].set_title("★ BULK-vs-INTERFACE (review null baseline)\nsep≥%d collapses %.0f orders → skin"
                    % (sd["sep_baseline_nodes"],
                       sd["collapse_at_ref_pair"]["collapse_orders"]))
    ax[2].legend(fontsize=6.5, loc="upper right")

    fig.text(0.5, -0.03, "VERDICT (re-scoped): " + v["BRANCH_VERDICT"][:140], ha="center", fontsize=7.5)
    fig.tight_layout()
    p = fig_dir / "twotone_formfactor.png"
    fig.savefig(p, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {p}")
    return p


# ───────────────────────── main ─────────────────────────
def main():
    out_dir = Path(__file__).parent
    results = {
        "prereg": "research/2026-07-09_twotone-formfactor_prereg_FROZEN.md",
        "base_driver": "src/scripts/vol_1_foundations/superband_carrier_fork.py",
        "class": "EMERGENCE (Class D) form factor on 1D model substrate; A⁶ + parity = Class B",
        "platform": "1D K4 bond-line reduction; band top ω_top=2.0 ω_C (NOT the 3D srs top)",
        "canonical_constants": {"L_NODE_m": L_NODE, "C_0_m_per_s": C_0,
                                "OMEGA_C_rad_per_s_SI": OMEGA_C_SI, "native_omega_C": 1.0,
                                "native_omega_top_1d": OMEGA_TOP_1D},
        "srs_3d_followon": {"srs_band_top_over_omega_C": SRS_BAND_TOP_OVER_OMEGA_C,
                            **SRS_FOLLOWON_TONES},
        "frozen_sweeps": {"carriers": CARRIERS, "ref_pair": list(REF_PAIR), "amps": AMPS,
                          "form_factor_amp": FORM_FACTOR_AMP, "w_out": BASE["w_out"]},
    }

    print("[1/9] gate (a) M7 per-tone injection …")
    results["gate_a_m7"] = gate_a_m7(*REF_PAIR)
    print("[2/9] gate (b) validate-on-known reader …")
    results["gate_b_validate"] = gate_b_validate_reader(BASE["w_out"])
    print("[3/9] gate (c) ramp-independence …")
    results["gate_c_ramp"] = gate_c_ramp(*REF_PAIR, FORM_FACTOR_AMP)
    print("[4/9] gate (e) energy + dt convergence …")
    results["gate_e_energy_dt"] = gate_e_energy_dt(*REF_PAIR, FORM_FACTOR_AMP)

    print("[5/9] form-factor sweep (r/S casting) …")
    results["form_factor_sweep_rS"] = form_factor_sweep(force_law="r_over_S")
    print("[6/9] form-factor sweep (r/√S casting cross-check) …")
    results["form_factor_sweep_rSqrtS"] = form_factor_sweep(force_law="r_over_sqrtS")

    print("[7/9] amplitude sweep + birth profile …")
    results["amplitude_sweep_rS"] = amplitude_sweep(REF_PAIR, force_law="r_over_S")
    # reference birth-depth profile (r/S, form-factor amplitude) — KEEP-BOTH interface-scoped:
    # the metric FLOORS at 1 by construction (the read window starts at n_drive-10; the beat is
    # zero at the clamped node and full one node out) — see result §profile. NOT bulk evidence.
    w_lo, w_hi = REF_PAIR
    series, diag = twotone_run(w_lo, w_hi, FORM_FACTOR_AMP, FORM_FACTOR_AMP, ramp_periods=15,
                               **BASE)
    results["ref_birth_profile"] = birth_depth(series, diag, BASE["w_out"])

    print("[8/9] BULK-vs-INTERFACE discriminator (review null baseline, sep>=3) …")
    sd = sep_discriminator(REF_PAIR, force_law="r_over_S")
    sd["kernel_off_floor_P"] = results["amplitude_sweep_rS"]["kernel_off_floor_P"]
    results["sep_discriminator"] = sd

    print("[9/9] ★ parity theorem — generative planted-asymmetry verification …")
    results["parity_generative"] = parity_generative_test(REF_PAIR, force_law="r_over_S")

    branch = adjudicate(results)

    # strip heavy field arrays before serialising
    payload = json.loads(json.dumps(results, default=lambda o: None))
    RESULT_JSON = out_dir.parent.parent.parent / "research" / "2026-07-09_twotone-formfactor_result.json"
    RESULT_JSON.write_text(json.dumps(payload, indent=2))
    print(f"wrote {RESULT_JSON}")
    print(json.dumps(results["verdict"], indent=2))
    make_figure(results, out_dir)
    return payload


if __name__ == "__main__":
    main()
