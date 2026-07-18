#!/usr/bin/env python3
"""F6 bath meter — VALIDATION driver (A-battery V1-V6 + W-battery W1-W6; plants only).

Charter: research/2026-07-16_f6-bath-meter_CHARTER.md (+ amendments §A / §B, 2026-07-17;
+ §B-post-review addendum, 2026-07-17 — PR #721 review repairs R-1..R-8).
Instrument: src/ave/thermal/f6_bath_meter.py
Gate: hardware-ratings-map §7 (JOINT detector-rebuild GATE, post-#711/#714).

SECTOR / REGIME: R7 thermal / entropy-sink (T2). The plant is a WEAKLY-NONLINEAR-
VIA-OP3 K4 plant, NOT a linear lattice: the `nonlinear` flag is a NO-OP given
op3_bond_reflection=True (the K4 4-port scatter matrix is z-independent, §B1 FACT-1
— verified UNCONDITIONAL, op3-OFF twin bit-identical too), so the amplitude-dependent
Op14 kernel S(A)=√(1−A²) is carried by op3's bond Γ, which is ON in every plant here.
The A-battery runs at mild amplitude (Γ(A) second-order, effectively cold); the
W-battery sweeps A_max up the op3-Γ(A) register (mild/moderate/near-knee). NO |Γ|→1
yield wall (below rupture), NO memristive hysteresis (use_memristive_saturation=False,
out of scope), NO node mint. NO F6 ARM IS FIRED HERE: the meter is validated on
hand-built plants only. A verdict here certifies the instrument, NOT an F6 result
(the arm fires in a different lane, after rebasing onto the sibling F1 fix — §9),
and is SCOPED to STANDALONE-K4 plants (§B-post-review addendum R-1: a
CoupledK4Cosserat arm or a genuine irreversible ε→T2 primitive breaks the
conservation identity ⇒ W-battery re-validation required).

Post-#717-review rebuild (see charter amendment §A). Repairs folded in:
  V6 — the secular pump is KILLED (global on-shell rescale); drift measured over
       3000 steps and its ceiling DERIVED from the reactive-bin boundary (Rule 11).
  V2 — M-invariance held INSIDE the enforced Nyquist envelope (M ≤ 95) + a
       detuning-collapse leg (comb off-band ⇒ N_occ→0; tracks physics, not M).
  V3 — the predicted resonance-window count is COMPUTED and tested (±1), not a
       hardcoded ceiling.
  V4 — the friction plant keeps the bath LIVE (driven-but-dissipating); the
       discriminator R is genuinely measured on both plants and can fail.
  N_occ — ABSOLUTE floor + minimum-E_bath gate (no junk counts on eps/detuned).
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, field

import numpy as np

from ave.core.k4_tlm import K4Lattice3D
from ave.thermal import LatticeBathCoupler, OscillatorBath, make_collar_mask
from ave.thermal.f6_bath_meter import E_BATH_MIN_DEFAULT, FLOOR_ABS_DEFAULT

# --- frozen validation tolerances (charter §6 + amendment §A) ---
MACHINE_TOL = 1e-10
N_OCC_M_TOL = 1
N_OCC_V3_TOL = 1
R_BATH_MAX = 0.2
R_FRICTION_MIN = 0.8
D_LIVE_MIN = 1e-3
FRICTION_MATCH_TOL = 0.20
# V6 drift ceiling is DERIVED, not asserted (Rule 11): the coupled-run total-energy
# drift, as a fraction of the bath transfer, must stay below R_BATH_MAX — else it
# would push the reactive ledger out of its own bin. (Amendment §A registers this.)
V6_DRIFT_CEIL_FRAC_OF_TRANSFER = R_BATH_MAX

# --- frozen instrument operating point (ENGINEERING CHOICES — tagged, not physics) ---
N_GRID = 12
CENTER = (N_GRID // 2, N_GRID // 2, N_GRID // 2)
COLLAR_R_IN = 2.0
COLLAR_R_OUT = 4.0
KAPPA = 0.012
BETA_FRICTION = 0.01
DELTA_OMEGA = 0.03
OMEGA_MIN = 0.30
N_STEPS = 800
N_STEPS_LONG = 3000  # V6 secular-drift horizon (~4× the working window)
SEED = 1
M_DEFAULT = 64
M_LIST = (32, 64, 90)  # all within the Nyquist envelope (ω_max·dt < π ⇒ M ≤ 95)
DW_LIST = (0.02, 0.03, 0.04)  # Δω-variation at fixed M (diagnostic; non-gating)
# Detuned comb (drive band ~0.5 lies OUTSIDE [ω_min, ω_max]; within Nyquist):
DETUNE_OMEGA_MIN = 1.5
DETUNE_M = 32  # ω_max = 1.5 + 31·0.03 = 2.43 < π
V3_TONE_AMP = 0.5
V3_TONE_OMEGA = 0.5


def _seed_lattice(lat: K4Lattice3D, scale: float = 1.0) -> None:
    """Deterministic broadband seed (fixed physics across the whole battery).

    `scale` multiplies the seed amplitude — the W-battery operating-point knob
    (mild/moderate/near-knee A_max, §B). Default 1.0 preserves the A-battery seed
    byte-for-byte (V1-V6 call this without `scale`).
    """
    rng = np.random.default_rng(SEED)
    ii, jj, kk = np.indices((lat.nx, lat.ny, lat.nz))
    c = CENTER
    env = np.exp(-((ii - c[0]) ** 2 + (jj - c[1]) ** 2 + (kk - c[2]) ** 2) / (2 * 1.5**2))
    env[~lat.mask_active] = 0.0
    for p in range(4):
        lat.V_inc[..., p] += scale * 0.08 * env
    fld = np.zeros_like(lat.V_inc)
    for _ in range(6):
        kv = rng.integers(1, lat.nx // 2, size=3) * (2 * np.pi / lat.nx) * rng.choice([-1, 1], size=3)
        ph = rng.uniform(0, 2 * np.pi)
        pw = np.cos(kv[0] * ii + kv[1] * jj + kv[2] * kk + ph)
        pw2 = rng.normal(size=4)
        for p in range(4):
            fld[..., p] += scale * 0.03 * pw * pw2[p]
    fld[~lat.mask_active] = 0.0
    lat.V_inc += fld


def _build(
    M: int = M_DEFAULT,
    kappa: float = KAPPA,
    friction: bool = False,
    beta: float = 0.0,
    delta_omega: float = DELTA_OMEGA,
    omega_min: float = OMEGA_MIN,
    nonlinear: bool = False,
    scale: float = 1.0,
) -> LatticeBathCoupler:
    """Build a coupled meter with on-shell E0.

    E0 is captured after the first step() (on-shell): the V_ref=0 seed doubles at
    the first TLM connect (both arm repairs — Arm A A3 / Arm B A2).

    Defaults (`nonlinear=False`, `scale=1.0`) build the A-battery cold-plant meter
    byte-for-byte. The W-battery (§B) sets `nonlinear=True` and `scale` to reach
    the mild/moderate/near-knee operating points. NB (§B1 FACT-1): with
    `op3_bond_reflection=True` the `nonlinear` flag is a no-op (the K4 4-port
    scatter is z-independent); the amplitude-dependent kernel S(A) is carried by
    op3's bond Γ, and the nonlinearity is driven by `scale` (A_max). We still set
    `nonlinear=nonlinear` faithfully; W1 banks the flag-no-op identity.
    """
    lat = K4Lattice3D(N_GRID, N_GRID, N_GRID, nonlinear=nonlinear, op3_bond_reflection=True, V_SNAP=1.0)
    _seed_lattice(lat, scale)
    lat.step()  # on-shell baseline
    bath = OscillatorBath(M=M, omega_min=omega_min, delta_omega=delta_omega)
    collar = make_collar_mask(lat, CENTER, COLLAR_R_IN, COLLAR_R_OUT)
    return LatticeBathCoupler(lat, bath, collar, kappa=kappa, friction=friction, beta=beta)


def _run(cpl: LatticeBathCoupler, n_steps: int = N_STEPS, ledger: bool = False):
    """Advance the coupled meter; optionally return the total-energy drift curve."""
    E0 = cpl.e_lat()
    Etot0 = E0 + cpl.e_bath()
    curve = []
    for i in range(1, n_steps):
        cpl.step(i)
        if ledger and (i % 100 == 0 or i == n_steps - 1):
            curve.append((i, ((cpl.e_lat() + cpl.e_bath()) - Etot0) / E0))
    return E0, curve


@dataclass
class VResult:
    vid: str
    passed: bool
    detail: str
    metrics: dict = field(default_factory=dict)


# --- V1: lossless control -----------------------------------------------------
def run_v1() -> VResult:
    cpl = _build(kappa=0.0)
    E0, _ = _run(cpl)
    dE = abs(cpl.e_lat() - E0) / E0
    n_occ = cpl.bath.n_occ()
    ok = dE < MACHINE_TOL and n_occ == 0
    return VResult("V1", ok, f"|ΔE_lat|/E0={dE:.2e} (<{MACHINE_TOL:.0e}), N_occ={n_occ} (=0)")


# --- V2: M-invariance (kills twin-64) + detuning collapse (tracks physics) ----
def run_v2() -> VResult:
    # V2a — vary the TRUNCATION count M at FIXED physics ⇒ N_occ invariant.
    occ = {}
    for M in M_LIST:
        cpl = _build(M=M)
        _run(cpl)
        occ[M] = cpl.bath.n_occ()
    ref = occ[M_DEFAULT]
    m_invariant = all(abs(occ[M] - ref) <= N_OCC_M_TOL for M in M_LIST)
    # V2b — DETUNE the comb off the drive band (within Nyquist) ⇒ N_occ collapses.
    # The old ΔN_occ≡M_MODES detector would still read M here; a physical read reads 0.
    cpl_det = _build(M=DETUNE_M, omega_min=DETUNE_OMEGA_MIN)
    _run(cpl_det)
    n_occ_det = cpl_det.bath.n_occ()
    detune_collapses = n_occ_det == 0
    # Δω-response diagnostic (NON-GATING): N_occ is not a pinned constant — it
    # responds to the comb spacing (a genuine physics change; the transfer itself
    # varies with Δω, so this is reported, not gated).
    dw_occ = {}
    for dw in DW_LIST:
        cpl = _build(delta_omega=dw)
        _run(cpl)
        dw_occ[dw] = cpl.bath.n_occ()
    ok = m_invariant and detune_collapses
    counts = [occ[M] for M in M_LIST]
    return VResult(
        "V2",
        ok,
        f"M∈{list(M_LIST)}(≤Nyquist 95)→N_occ={counts} invariant≤{N_OCC_M_TOL} (NOT tracking M); "
        f"detuned comb→N_occ={n_occ_det} (=0, tracks physics; twin-64 would read M); "
        f"Δω-response {list(dw_occ.values())} (not pinned, diag)",
        {"n_occ_M": counts, "n_occ_detuned": n_occ_det, "dw_response": list(dw_occ.values())},
    )


# --- V3: known-transfer plant (narrowband tone), COMPUTED prediction ----------
def run_v3() -> VResult:
    occ = {}
    top = None
    predicted = None
    for M in M_LIST:
        cpl = _build(M=M)
        cpl.q_ext = lambda i: V3_TONE_AMP * np.sin(V3_TONE_OMEGA * i)
        _run(cpl)
        occ[M] = cpl.bath.n_occ()
        if M == M_DEFAULT:
            e = cpl.bath.mode_energy()
            top = float(cpl.bath.omega[int(np.argmax(e))])
            # PREDICTION: modes within one comb spacing (the resolution-limited
            # resonance half-width) of the drive tone — a computed, falsifiable count.
            half = cpl.bath.delta_omega
            predicted = int(np.count_nonzero(np.abs(cpl.bath.omega - V3_TONE_OMEGA) <= half))
    ref = occ[M_DEFAULT]
    invariant = all(abs(occ[M] - ref) <= N_OCC_V3_TOL for M in M_LIST)
    matches_prediction = abs(ref - predicted) <= N_OCC_V3_TOL
    peak_on_tone = abs(top - V3_TONE_OMEGA) <= 2 * DELTA_OMEGA
    ok = invariant and matches_prediction and peak_on_tone
    counts = [occ[M] for M in M_LIST]
    return VResult(
        "V3",
        ok,
        f"N_occ(M={list(M_LIST)})={counts} vs COMPUTED prediction={predicted} (|Δ|≤{N_OCC_V3_TOL}); "
        f"invariant across M; peak ω={top:.3f}≈ω_d={V3_TONE_OMEGA}",
        {"n_occ": counts, "predicted": predicted, "peak_omega": round(top, 3)},
    )


# --- V4: friction plant (physical discriminator, bath LIVE) -------------------
def run_v4() -> VResult:
    # reactive plant: energy STORED in the bath
    cpl_b = _build()
    E0b, _ = _run(cpl_b)
    stored = cpl_b.e_bath()
    R_bath = abs((cpl_b.e_lat() - E0b) + stored) / max(abs(cpl_b.e_lat() - E0b), 1e-30)
    n_occ_bath = cpl_b.bath.n_occ()
    # friction plant: bath LIVE (driven) but Re(Z)-damped ⇒ energy DISSIPATED
    cpl_f = _build(friction=True, beta=BETA_FRICTION)
    E0f, _ = _run(cpl_f)
    dissipated = cpl_f.friction_removed
    R_fric = abs((cpl_f.e_lat() - E0f) + cpl_f.e_bath()) / max(abs(cpl_f.e_lat() - E0f), 1e-30)
    n_occ_fric = cpl_f.bath.n_occ()
    # matched magnitude: the friction plant DISSIPATES ≈ what the reactive plant STORES
    matched = abs(dissipated - stored) / stored <= FRICTION_MATCH_TOL
    bath_bin = R_bath < R_BATH_MAX  # measured; can fail
    fric_bin = R_fric > R_FRICTION_MIN  # measured on a LIVE driven bath; can fail
    ok = matched and bath_bin and fric_bin
    return VResult(
        "V4",
        ok,
        f"matched: friction dissipated {dissipated:.3f} vs reactive stored {stored:.3f} "
        f"(Δ={abs(dissipated - stored) / stored * 100:.0f}%≤{int(FRICTION_MATCH_TOL * 100)}%); "
        f"discriminator R (both baths DRIVEN, N_occ={n_occ_bath}/{n_occ_fric}): "
        f"REACTIVE R={R_bath:.1e}(<{R_BATH_MAX}) vs FRICTION R={R_fric:.3f}(>{R_FRICTION_MIN})",
        {"R_bath": R_bath, "R_fric": R_fric, "stored": stored, "dissipated": dissipated},
    )


# --- V5: back-reaction liveness -----------------------------------------------
def run_v5() -> VResult:
    on = _build()
    _run(on)
    off = _build(kappa=0.0)
    _run(off)
    a = on.active
    num = float(np.linalg.norm(on.lat.V_inc[a] - off.lat.V_inc[a]))
    den = float(np.linalg.norm(off.lat.V_inc[a])) + 1e-30
    D = num / den
    ok = D > D_LIVE_MIN
    return VResult(
        "V5",
        ok,
        f"trajectory divergence ON vs OFF D={D:.3e} (>{D_LIVE_MIN:.0e}); coupling changes lattice dynamics",
        {"D": D},
    )


# --- V6: baseline convention + MEASURED non-secular drift (derived ceiling) ----
def run_v6() -> VResult:
    # lossless control ledger (on-shell E0)
    cpl0 = _build(kappa=0.0)
    E0, _ = _run(cpl0)
    lossless = abs(cpl0.e_lat() - E0) / E0
    # coupled-run drift over the LONG horizon (secularity actually computed)
    cpl = _build()
    _E0c, curve = _run(cpl, n_steps=N_STEPS_LONG, ledger=True)
    transfer = cpl.e_bath()
    steps = np.array([s for s, _ in curve], dtype=float)
    drifts = np.array([abs(d) for _, d in curve])
    max_drift = float(drifts.max())
    # secular slope: linear fit of |drift| vs step (per-step growth rate)
    slope = float(np.polyfit(steps, drifts, 1)[0]) if len(steps) > 1 else 0.0
    # DERIVED ceiling (Rule 11): drift as a fraction of the transfer must stay
    # below the reactive-bin boundary R_BATH_MAX (else it leaves the reactive bin).
    transfer_frac = max(transfer / E0, 1e-30)
    drift_frac = max_drift / transfer_frac
    ceil = V6_DRIFT_CEIL_FRAC_OF_TRANSFER
    # non-secular: extrapolated growth over the horizon stays inside the derived ceil
    projected = abs(slope) * N_STEPS_LONG / transfer_frac
    non_secular = projected < ceil
    ok = lossless < MACHINE_TOL and drift_frac < ceil and non_secular
    lo = curve[len(curve) // 5]
    hi = curve[-1]
    endpts = f"{lo[1]:+.1e}@{lo[0]} … {hi[1]:+.1e}@{hi[0]}"
    return VResult(
        "V6",
        ok,
        f"on-shell E0; lossless ledger={lossless:.2e}(<{MACHINE_TOL:.0e}); "
        f"coupled drift over {N_STEPS_LONG} steps: {endpts}; max/transfer={drift_frac:.2e} "
        f"(<derived {ceil}=R_BATH_MAX); slope={slope:.1e}/step (non-secular={non_secular})",
        {
            "lossless": lossless,
            "max_drift": max_drift,
            "drift_frac": drift_frac,
            "slope": slope,
            "curve": [(int(s), float(d)) for s, d in curve[::5]],
        },
    )


def run_battery() -> tuple[list[VResult], str]:
    results = [run_v1(), run_v2(), run_v3(), run_v4(), run_v5(), run_v6()]
    failed = [r.vid for r in results if not r.passed]
    if not failed:
        verdict = "METER-VALID-WITHIN-ENVELOPE"
    elif {"V2", "V4", "V5"} & set(failed):
        verdict = f"METER-INVALID (core fail: {','.join(failed)})"
    else:
        verdict = f"METER-PARTIAL({','.join(failed)})"
    return results, verdict


# ═══════════════════════════════════════════════════════════════════════════
# W-BATTERY — NONLINEAR-REGIME REVALIDATION (charter Amendment §B, 2026-07-17)
# ═══════════════════════════════════════════════════════════════════════════
# Opt-in (`--w-battery`). Does NOT disturb the A-battery (V1-V6) paths: it reuses
# `_build`/`_seed_lattice` through their new behavior-preserving defaults
# (nonlinear=True + seed `scale` are the only additions). NO F6 arm/door fires.
#
# The decisive risk (§B1): with the amplitude-dependent kernel active, the §A1
# global-rescale "scalar multiple stays on-shell" conservation argument is LINEAR
# and may break — re-introducing a secular pump. FACT (§B1): `nonlinear=True` is a
# no-op given op3_bond_reflection=True (K4 4-port scatter is z-independent); the
# kernel S(A)=√(1−A²)→z_local=(1−A²)^(−1/4) flows through op3's bond Γ, and the
# nonlinearity is driven by AMPLITUDE (seed `scale`). We set nonlinear=True
# faithfully AND sweep A_max across the three operating points.

# --- frozen operating points (ENGINEERING CHOICES — tagged; §B1 table) --------
OP_SCALES = {"mild": 0.6, "moderate": 1.8, "near-knee": 2.9}  # A_max ≈ 0.10/0.30/0.50
W_NSTEP = N_STEPS_LONG  # 3000-step horizon (W1/W2), matches the A-battery V6 window
# --- frozen W thresholds (all DERIVED / inherited; Rule 11 — no retune) --------
W2_DRIFT_CEIL = R_BATH_MAX  # KILL ceiling: |proj slope·N| / transfer < R_BATH_MAX
W3_COLLAPSE_ORDERS = 100.0  # ≥2 orders (frozen): E_bath(res)/E_bath(det) ≥ 100
W3_POWER_FRAC_MAX = 1e-2  # DERIVED: detuned band q-power frac < 1/100 ⇒ ≥2-order drop
W3_HARM_GUARD = 2 * DELTA_OMEGA  # placement clearance from measured content
W4_HARM_MATCH_TOL = 2 * DELTA_OMEGA  # occupied bath ω must sit within this of a q-peak/harmonic
W4_SEA_MULT = 4.0  # a mode is on real content iff local q-power > 4× the off-resonant sea
W4_M_LIST = M_LIST  # (32, 64, 90) — Nyquist-bounded M-invariance sweep
W5_TARE_C_TOL = 0.02  # |c_fit − c|/c gate: the computable tare IS the fitted scalar
W5_RESID_FLAG = 0.5  # residual > this ⇒ tare captures < half the divergence (flag)
W_WORKING_STEPS = N_STEPS  # 800-step working window for W5 (matches V5)
EPS_TINY = 1e-300  # spectral-denominator floor (psd.sum() is never 0 in practice)
EPS_DIVZERO_LOCAL = 1e-30  # ⟨V_off·V_off⟩ floor for the W5 best-fit scalar


def _amax(cpl: LatticeBathCoupler) -> float:
    """A_max = max active-site strain ‖V_inc‖ / V_SNAP (V_SNAP=1 ⇒ = max ‖V_inc‖)."""
    v = np.sqrt(np.sum(cpl.lat.V_inc**2, axis=-1))
    return float(v[cpl.lat.mask_active].max())


def _run_w(cpl: LatticeBathCoupler, n_steps: int, record_q: bool = False):
    """Advance a W-plant; return (E0, signed total-E drift curve, q timeseries, A_peak).

    Signed drift `(E_lat+E_bath − Etot0)/E0` is the W2 curve (kept signed; a pump is
    a monotone one-sign accumulation). q is recorded for W3/W4 spectral honesty.
    """
    E0 = cpl.e_lat()
    Etot0 = E0 + cpl.e_bath()
    curve, qs = [], []
    a_peak = _amax(cpl)
    for i in range(1, n_steps):
        cpl.step(i)
        a_peak = max(a_peak, _amax(cpl))
        if record_q:
            qs.append(cpl.read_q())
        if i % 100 == 0 or i == n_steps - 1:
            curve.append((i, ((cpl.e_lat() + cpl.e_bath()) - Etot0) / E0))
    return E0, curve, np.array(qs) if record_q else None, a_peak


def _q_spectrum(qs: np.ndarray):
    """Hann-windowed angular-frequency spectrum of the collar-q timeseries.

    Returns (freqs, psd, dominant_omega, cum_power_fraction). The independent
    read of the plant's own V-spectrum harmonics (W3 placement, W4 honesty)."""
    q = qs - qs.mean()
    w = np.hanning(len(q))
    amp = np.abs(np.fft.rfft(q * w))
    psd = amp**2
    freqs = 2 * np.pi * np.fft.rfftfreq(len(q), d=1.0)  # angular ω (dt=1)
    dom = float(freqs[int(np.argmax(psd))])
    cum = np.cumsum(psd) / max(psd.sum(), EPS_TINY)
    return freqs, psd, dom, cum


def _band_power_frac(freqs, psd, lo, hi) -> float:
    m = (freqs >= lo) & (freqs <= hi)
    return float(psd[m].sum() / max(psd.sum(), EPS_TINY))


def _slope_and_kill(curve, transfer_frac: float, n_steps: int, ceil: float):
    """W1/W2 secularity read: |proj slope·N| and max|drift|, as a fraction of the
    bath transfer (W2) or E0 (W1, transfer_frac=1). KILL if either ≥ ceil."""
    steps = np.array([s for s, _ in curve], float)
    signed = np.array([d for _, d in curve])
    absd = np.abs(signed)
    max_frac = float(absd.max() / transfer_frac)
    slope = float(np.polyfit(steps, absd, 1)[0]) if len(steps) > 1 else 0.0
    projected = abs(slope) * n_steps / transfer_frac
    kill = (projected >= ceil) or (max_frac >= ceil)
    return {
        "signed_end": float(signed[-1]),
        "sign": "+" if signed[-1] > 0 else "-",
        "max_frac": max_frac,
        "slope": slope,
        "projected": projected,
        "kill": kill,
    }


# --- FACT-4 provenance measuring snippet (R-3, PR #721 review; opt-in, NOT a gate) --
def measure_noncommutation(s: float = 0.9) -> dict:
    """Reproducible FACT-4 measurement: the global rescale does NOT commute with the
    lattice step on the nonlinear plant. Returns the on-shell non-commutation residual
      resid = ‖step(s·x) − s·step(x)‖ / ‖step(x)‖
    at each operating point, where x=(V_inc,V_ref) is the on-shell active-cell state
    the §A1 global rescale actually acts on, and step = one lossless lattice step.

    OPT-IN (`--fact4`); NOT part of the W-battery gate. Provenance repair (R-3): the
    charter §B1 FACT-4 triple (1.8e-4/1.76e-3/5.4e-3) was scratch-provenance — not
    reproducible from shipped code (all natural readings are ~3-4× smaller). This
    banks the measured reproduction (charter body NOT edited — see the §B-post-review
    addendum; the reviewer's independent measurement was 4.3e-5→1.2e-3, ~28×, same
    order/trend). On a LINEAR step the two orders commute exactly (residual 0); the
    residual grows with A_max because op3's bond Γ(A) makes the step amplitude-dependent.
    """
    out = {}
    for name, scale in OP_SCALES.items():
        lat_a = _build(kappa=0.0, nonlinear=True, scale=scale).lat
        lat_b = _build(kappa=0.0, nonlinear=True, scale=scale).lat
        act = lat_a.mask_active
        # step(s·x): scale the whole active (V_inc,V_ref) state, then step
        lat_a.V_inc[act] *= s
        lat_a.V_ref[act] *= s
        lat_a.step()
        # s·step(x): step, then scale
        lat_b.step()
        lat_b.V_inc[act] *= s
        lat_b.V_ref[act] *= s
        num = float(
            np.sqrt(np.sum((lat_a.V_inc[act] - lat_b.V_inc[act]) ** 2)
                    + np.sum((lat_a.V_ref[act] - lat_b.V_ref[act]) ** 2))
        )
        den = float(np.sqrt(np.sum(lat_b.V_inc[act] ** 2) + np.sum(lat_b.V_ref[act] ** 2))) + 1e-30
        out[name] = num / den
    return {
        "s": s,
        "method": "‖step(s·x)−s·step(x)‖/‖step(x)‖ on the on-shell (V_inc,V_ref) active state",
        "noncommutation": out,
        "growth_mild_to_near_knee": out["near-knee"] / out["mild"],
    }


# --- W1: nonlinear lossless baseline (the plant's own integrator floor) --------
def run_w1() -> VResult:
    """Kernel ON, NO bath (κ=0), no drive after seed: the bare nonlinear plant's
    energy-conservation FLOOR over 3000 steps at each operating point. Also banks
    §B1 FACT-1 (nonlinear=True vs False identity). PASS: max|ΔE|/E0 < MACHINE_TOL
    AND non-secular (proj slope·N/E0 < MACHINE_TOL) at all three points.
    """
    per, floors, flag_ok = {}, {}, True
    for name, scale in OP_SCALES.items():
        cpl = _build(kappa=0.0, nonlinear=True, scale=scale)
        a0 = _amax(cpl)
        E0, curve, _, a_peak = _run_w(cpl, W_NSTEP)
        # transfer_frac=1 ⇒ read drift as a fraction of E0 vs the machine floor.
        sk = _slope_and_kill(curve, transfer_frac=1.0, n_steps=W_NSTEP, ceil=MACHINE_TOL)
        floors[name] = sk["max_frac"]
        per[name] = {"A0": round(a0, 4), "A_peak": round(a_peak, 4), **sk}
        # flag-no-op receipt: nonlinear=True must equal nonlinear=False (op3 on).
        lin = _build(kappa=0.0, nonlinear=False, scale=scale)
        nl = _build(kappa=0.0, nonlinear=True, scale=scale)
        for _ in range(60):
            lin.lat.step()
            nl.lat.step()
        if float(np.max(np.abs(lin.lat.V_inc - nl.lat.V_inc))) > 1e-12:
            flag_ok = False
    ok = all(p["max_frac"] < MACHINE_TOL and not p["kill"] for p in per.values()) and flag_ok
    floor_str = ", ".join(f"{n}(A={per[n]['A0']}):{per[n]['max_frac']:.1e}" for n in OP_SCALES)
    return VResult(
        "W1",
        ok,
        f"bare nonlinear-plant floor over {W_NSTEP} steps [max|ΔE|/E0]: {floor_str} "
        f"(all <{MACHINE_TOL:.0e}, non-secular); nonlinear=True≡False given op3 (FACT-1): {flag_ok}",
        {"per_point": per, "floors": floors, "flag_no_op_ok": flag_ok},
    )


# --- W2: kernel-ON coupled drift (LEDGER-REGRESSION + TRANSFER-HEALTH leg) ------
def run_w2() -> VResult:
    """Production coupling, driven-then-source-off, 3000 steps at each operating
    point. Signed total-E drift curve. KILL (= METER-INVALID-NONLINEAR): a monotone
    (secular) drift whose |proj slope·N| exceeds R_BATH_MAX of the bath transfer
    (same §A2 reactive-bin-boundary derivation, restated for the nonlinear plant).

    ★HONEST SCOPE (R-1, PR #721 review). On THIS plant class, energy conservation is
    IDENTITY-ENFORCED, not empirically survived: the z-independent equal-admittance
    4-port scatter S=0.5−δ is orthogonal, the bond connect [[γ,T],[T,−γ]] is orthogonal
    at any γ, and the global rescale is arithmetic-exact on the quadratic energy —
    pump-immunity was STRUCTURALLY GUARANTEED. So W2 is NOT the decisive kill leg the
    §B1 pre-reg framed; the S(A)-kernel-in-scatter pump path is INEXPRESSIBLE on this
    junction. W2's remaining content is (a) a REGRESSION guard vs #717-class ledger
    bugs (a single-field V_inc-only rescale breaks the exact-conservation identity),
    (b) TRANSFER-HEALTH (E_bath stays > E_BATH_MIN — no off-comb collapse), and (c) the
    dormant max(·,0) clamp path (d_e_bath/e_lat stays ≪ 1). A CoupledK4Cosserat arm or
    a genuine irreversible ε→T2 primitive BREAKS the identity ⇒ re-validation required.
    """
    per, any_kill, any_collapse = {}, False, False
    for name, scale in OP_SCALES.items():
        cpl = _build(nonlinear=True, scale=scale)
        E0, curve, _, a_peak = _run_w(cpl, W_NSTEP)
        transfer = cpl.e_bath() / E0
        if transfer < E_BATH_MIN_DEFAULT / E0:  # off-comb transfer collapse — a finding, not a silent pass
            any_collapse = True
            per[name] = {"A_peak": round(a_peak, 4), "transfer_frac": transfer, "collapsed": True}
            continue
        sk = _slope_and_kill(curve, transfer_frac=transfer, n_steps=W_NSTEP, ceil=W2_DRIFT_CEIL)
        any_kill = any_kill or sk["kill"]
        per[name] = {"A_peak": round(a_peak, 4), "transfer_frac": transfer, "collapsed": False, **sk}
    ok = (not any_kill) and (not any_collapse)
    det = "; ".join(
        f"{n}(A={per[n]['A_peak']}): signed_end={per[n].get('signed_end', float('nan')):+.1e} "
        f"transfer={per[n]['transfer_frac']:.2e} |slope·N|/transfer={per[n].get('projected', float('nan')):.1e} "
        f"KILL={per[n].get('kill', 'COLLAPSE')}"
        for n in OP_SCALES
    )
    return VResult("W2", ok, f"[ceil {W2_DRIFT_CEIL}=R_BATH_MAX] {det}", {"per_point": per})


def _place_detuned_band(freqs, psd, cum):
    """Choose a detuned comb off the plant's MEASURED content (§B W3 placement).

    DISCLOSED DEVIATION from the literal §B rule ("≥2Δω from every n·ω_d, n=1..6"):
    that rule is UNSATISFIABLE here — the plant is broadband-seeded, so (a) it has
    independent lines not captured by n·ω_d, and (b) ω_d's high folded harmonics
    tile (0,π) at ~ω_d spacing with NEGLIGIBLE power, so no 32-mode Nyquist band
    avoids all six. The physically-honest control is "off all significant MEASURED
    q-power": scan ω_min upward from the 99%-cumulative-power cutoff + guard for the
    lowest 32-mode Nyquist band whose q-power fraction < W3_POWER_FRAC_MAX. Returns
    (ω_min_det, ω_max_det, band_power_frac, omega_99).
    """
    idx99 = int(np.searchsorted(cum, 0.99))
    omega_99 = float(freqs[idx99])
    m_det = DETUNE_M  # 32 (frozen)
    start = omega_99 + W3_HARM_GUARD
    om = start
    while om + (m_det - 1) * DELTA_OMEGA < np.pi:
        lo, hi = om, om + (m_det - 1) * DELTA_OMEGA
        if _band_power_frac(freqs, psd, lo, hi) < W3_POWER_FRAC_MAX:
            return om, hi, _band_power_frac(freqs, psd, lo, hi), omega_99
        om += DELTA_OMEGA
    # fall back to the A-battery's proven detuned band (also off-content here)
    hi = DETUNE_OMEGA_MIN + (m_det - 1) * DELTA_OMEGA
    return DETUNE_OMEGA_MIN, hi, _band_power_frac(freqs, psd, DETUNE_OMEGA_MIN, hi), omega_99


# --- W3: detuning soul-check on the nonlinear plant (harmonic-controlled) ------
def run_w3() -> VResult:
    """Resonant vs detuned comb at the MODERATE point — the transfer collapse must
    survive on the nonlinear plant (≥2 orders, frozen). Confound controlled: the
    detuned comb is placed OFF the plant's own measured harmonic content (see
    _place_detuned_band — DISCLOSED deviation from the literal n·ω_d rule).
    """
    scale = OP_SCALES["moderate"]
    res = _build(M=M_DEFAULT, nonlinear=True, scale=scale, omega_min=OMEGA_MIN)
    _E0, _c, qs, _a = _run_w(res, W_NSTEP, record_q=True)
    e_res, n_res = res.e_bath(), res.bath.n_occ()
    freqs, psd, dom, cum = _q_spectrum(qs)
    om_min_det, om_max_det, band_frac, omega_99 = _place_detuned_band(freqs, psd, cum)
    det = _build(M=DETUNE_M, nonlinear=True, scale=scale, omega_min=om_min_det)
    _run_w(det, W_NSTEP)
    e_det, n_det = det.e_bath(), det.bath.n_occ()
    ratio = e_res / max(e_det, 1e-300)
    # folded harmonics of ω_d (reported: shows why the literal rule is unsatisfiable)
    harm = [round(float((n * dom) % (2 * np.pi) if (n * dom) % (2 * np.pi) <= np.pi
                         else 2 * np.pi - (n * dom) % (2 * np.pi)), 3) for n in range(1, 7)]
    ok = ratio >= W3_COLLAPSE_ORDERS and n_res > 0 and n_det == 0
    return VResult(
        "W3",
        ok,
        f"MODERATE: resonant E_bath={e_res:.3e}(N_occ={n_res}) vs detuned "
        f"[{om_min_det:.2f},{om_max_det:.2f}] E_bath={e_det:.3e}(N_occ={n_det}); "
        f"collapse ×{ratio:.0f} (≥{W3_COLLAPSE_ORDERS:.0f}); ω_d={dom:.3f}, ω_99={omega_99:.3f}, "
        f"detuned q-power-frac={band_frac:.1e}(<{W3_POWER_FRAC_MAX:.0e}); "
        f"[DEVIATION: off-measured-content placement — n·ω_d folds {harm} tile (0,π), literal rule unsatisfiable]",
        {"e_res": e_res, "e_det": e_det, "ratio": ratio, "n_res": n_res, "n_det": n_det,
         "omega_d": dom, "detuned_band": [om_min_det, om_max_det], "band_frac": band_frac, "harmonics": harm},
    )


# --- W4: N_occ honesty under self-generated harmonics -------------------------
def run_w4() -> VResult:
    """With the kernel ON, bath modes at drive harmonics may be LEGITIMATELY excited.
    Verify N_occ reads PHYSICAL harmonic content: every occupied bath mode sits within
    HARM_MATCH_TOL of a peak of the plant's INDEPENDENTLY measured q-spectrum; N_occ is
    M-invariant; and an off-resonant probe still reads 0. FAIL = occupied modes off all
    plant peaks, or N_occ tracking M / exploding.
    """
    scale = OP_SCALES["moderate"]
    ref = _build(M=M_DEFAULT, nonlinear=True, scale=scale)
    _E0, _c, qs, _a = _run_w(ref, W_NSTEP, record_q=True)
    freqs, psd, dom, _cum = _q_spectrum(qs)
    occ_omega = ref.bath.omega[ref.bath.mode_energy() > FLOOR_ABS_DEFAULT]  # absolute occupancy floor
    # §B "peak/HARMONIC" honesty: an occupied mode is on REAL content iff its local
    # q-power fraction (±HARM_MATCH_TOL) sits ABOVE the off-resonant sea. This admits
    # both measured peaks AND self-generated drive harmonics (n·ω_d) — the legitimate
    # harmonic excitations W4 is about (e.g. the 2nd harmonic 2·ω_d, ~8× the sea). The
    # sea floor is the minimum local band-power over the comb's Nyquist range.
    def _local_frac(w):
        return _band_power_frac(freqs, psd, w - W4_HARM_MATCH_TOL, w + W4_HARM_MATCH_TOL)

    comb_probe = np.arange(OMEGA_MIN, np.pi - W4_HARM_MATCH_TOL, DELTA_OMEGA)
    # sea = MEDIAN off-content band power (a discriminating background reference;
    # the min is trivially empty, the median lands in the true off-resonant sea).
    sea = float(np.median([_local_frac(p) for p in comb_probe])) if len(comb_probe) else EPS_TINY
    local_fracs = np.array([_local_frac(w) for w in occ_omega])
    matched = local_fracs > W4_SEA_MULT * sea  # above the sea ⇒ on a peak/harmonic
    all_matched = bool(np.all(matched)) if len(occ_omega) else True
    # which occupied modes are self-generated harmonics n·ω_d (reported)
    harm_folds = [float((n * dom) % (2 * np.pi) if (n * dom) % (2 * np.pi) <= np.pi
                        else 2 * np.pi - (n * dom) % (2 * np.pi)) for n in range(1, 7)]
    n_harmonic = int(sum(any(abs(w - h) <= W4_HARM_MATCH_TOL for h in harm_folds) for w in occ_omega))
    # coverage: fraction of q-power within tol of ANY occupied mode
    cover_mask = np.zeros(len(freqs), bool)
    for w in occ_omega:
        cover_mask |= np.abs(freqs - w) <= W4_HARM_MATCH_TOL
    coverage = float(psd[cover_mask].sum() / max(psd.sum(), EPS_TINY))
    # M-invariance (Nyquist-bounded)
    occ_M = {}
    for M in W4_M_LIST:
        c = _build(M=M, nonlinear=True, scale=scale)
        _run_w(c, W_NSTEP)
        occ_M[M] = c.bath.n_occ()
    m_invariant = all(abs(occ_M[M] - occ_M[M_DEFAULT]) <= N_OCC_M_TOL for M in W4_M_LIST)
    # off-resonant rejection
    off = _build(M=DETUNE_M, nonlinear=True, scale=scale, omega_min=DETUNE_OMEGA_MIN)
    _run_w(off, W_NSTEP)
    off_rejects = off.bath.n_occ() == 0
    ok = all_matched and coverage >= 0.5 and m_invariant and off_rejects
    return VResult(
        "W4",
        ok,
        f"MODERATE: {len(occ_omega)} occupied bath modes ({n_harmonic} at self-generated harmonics n·ω_d, "
        f"ω_d={dom:.3f}), all on real content (local q-power >{W4_SEA_MULT:.0f}×sea): {all_matched} "
        f"(coverage of q-power={coverage:.2f}≥0.5); N_occ(M={list(W4_M_LIST)})="
        f"{[occ_M[M] for M in W4_M_LIST]} invariant≤{N_OCC_M_TOL} (NOT tracking M); off-resonant→0: {off_rejects}",
        {"n_occ_M": [occ_M[M] for M in W4_M_LIST], "all_matched": all_matched, "coverage": coverage,
         "n_harmonic": n_harmonic, "omega_d": dom, "sea": float(sea),
         "occ_omega": [round(float(w), 3) for w in occ_omega],
         "local_fracs": [round(float(f), 6) for f in local_fracs], "off_rejects": off_rejects},
    )


# --- W5: tare-rule check (the arm-spatiality budget vs operating point) --------
def run_w5() -> VResult:
    """At each operating point: the §B0 tare c=sqrt(1−E_bath/E0), the best-fit global
    scalar c_fit=⟨V_on·V_off⟩/⟨V_off·V_off⟩ (§A8 V5-decomposition), and the spatial
    residual resid=‖V_on−c_fit·V_off‖/‖V_off‖. PASS (tare-usable): |c_fit−c|/c <
    W5_TARE_C_TOL at all three points (the computable tare IS the fitted attenuation).
    The residual trend vs nonlinearity is REPORTED (the arm-spatiality budget) — a
    diagnostic, flagged only if resid > W5_RESID_FLAG.

    ★HONEST SCOPE (R-4, PR #721 review). |c_fit−c|/c is ALGEBRAICALLY 1−cosθ, where θ
    is the angle between the ON and OFF trajectories: c_fit = ‖V_on‖cosθ/‖V_off‖ and
    c ≈ ‖V_on‖/‖V_off‖ (the amplitude ratio √(1−E_bath/E0)), so |c_fit−c|/c = 1−cosθ
    — verified EXACT numerically at all three points (ratio 1.00). It is therefore the
    SAME measurement as the spatial residual (both read θ), NOT an independent tare
    confirmation: the c-agreement is enforced by the rescale arithmetic and could never
    fail independently of the residual. W5's informative content is the RESIDUAL TREND
    (the arm's spatial-discriminant budget). To give this leg a genuinely independent
    liveness check, the tare-usable gate is TIGHTENED (Rule-11-legal — a strengthening,
    disclosed in the §B-post-review addendum): E_bath at each point must exceed
    E_BATH_MIN, so the tare check cannot pass on a dead coupling (c→1, c_fit→1, θ→0
    trivially agreeing on a zero transfer).
    """
    per, usable = {}, True
    for name, scale in OP_SCALES.items():
        on = _build(nonlinear=True, scale=scale)
        off = _build(kappa=0.0, nonlinear=True, scale=scale)
        E0 = on.e_lat()
        _run_w(on, W_WORKING_STEPS)
        _run_w(off, W_WORKING_STEPS)
        a = on.active
        von = on.lat.V_inc[a].ravel()
        voff = off.lat.V_inc[a].ravel()
        e_bath = on.e_bath()
        c = float(np.sqrt(max(1.0 - e_bath / E0, 0.0)))
        c_fit = float(np.dot(von, voff) / max(np.dot(voff, voff), EPS_DIVZERO_LOCAL))
        resid = float(np.linalg.norm(von - c_fit * voff) / (np.linalg.norm(voff) + 1e-30))
        match = abs(c_fit - c) / max(c, 1e-30)
        # Independent liveness (R-4): the transfer must be LIVE (> E_BATH_MIN) so the
        # tare agreement cannot pass trivially on a dead coupling.
        liveness_ok = e_bath > E_BATH_MIN_DEFAULT
        usable = usable and (match < W5_TARE_C_TOL) and liveness_ok
        per[name] = {"c": round(c, 4), "c_fit": round(c_fit, 4), "match": match,
                     "resid": round(resid, 4), "flagged": resid > W5_RESID_FLAG,
                     "e_bath": round(float(e_bath), 4), "liveness_ok": liveness_ok}
    ok = usable
    trend = " → ".join(f"{n}:{per[n]['resid']:.3f}" for n in OP_SCALES)
    det = "; ".join(f"{n}(c={per[n]['c']},c_fit={per[n]['c_fit']},|Δ|/c={per[n]['match']:.1e})" for n in OP_SCALES)
    return VResult(
        "W5",
        ok,
        f"tare-usable |c_fit−c|/c<{W5_TARE_C_TOL} (=1−cosθ, so NOT independent of resid) "
        f"AND E_bath>E_BATH_MIN (independent liveness) at all points: {det}; "
        f"★spatial-residual trend (arm-spatiality budget) {trend} (grows with nonlinearity)",
        {"per_point": per, "residual_trend": [per[n]["resid"] for n in OP_SCALES]},
    )


# --- W6: envelope restatement (Nyquist + friction discriminator on NL plant) ---
def run_w6() -> VResult:
    """The Nyquist assert is still enforced (build past the M≤95 cap raises), and the
    friction discriminator (reactive stored vs friction dissipated) persists on the
    NONLINEAR plant at the moderate point.
    """
    # Nyquist guard fires
    nyquist_ok = False
    try:
        OscillatorBath(M=200, omega_min=OMEGA_MIN, delta_omega=DELTA_OMEGA)
    except ValueError:
        nyquist_ok = True
    # friction discriminator on the nonlinear moderate plant
    scale = OP_SCALES["moderate"]
    reac = _build(nonlinear=True, scale=scale)
    E0r = reac.e_lat()
    _run_w(reac, W_WORKING_STEPS)
    stored = reac.e_bath()
    R_bath = abs((reac.e_lat() - E0r) + stored) / max(abs(reac.e_lat() - E0r), 1e-30)
    fric = _build(friction=True, beta=BETA_FRICTION, nonlinear=True, scale=scale)
    E0f = fric.e_lat()
    _run_w(fric, W_WORKING_STEPS)
    dissipated = fric.friction_removed
    R_fric = abs((fric.e_lat() - E0f) + fric.e_bath()) / max(abs(fric.e_lat() - E0f), 1e-30)
    matched = abs(dissipated - stored) / max(stored, 1e-30) <= FRICTION_MATCH_TOL
    bath_bin = R_bath < R_BATH_MAX
    fric_bin = R_fric > R_FRICTION_MIN
    ok = nyquist_ok and matched and bath_bin and fric_bin
    return VResult(
        "W6",
        ok,
        f"Nyquist guard fires: {nyquist_ok}; MODERATE friction discriminator: reactive "
        f"R={R_bath:.1e}(<{R_BATH_MAX}) stored={stored:.3f} vs friction R={R_fric:.3f}"
        f"(>{R_FRICTION_MIN}) dissipated={dissipated:.3f} (Δ={abs(dissipated - stored) / max(stored, 1e-30) * 100:.0f}%"
        f"≤{int(FRICTION_MATCH_TOL * 100)}%)",
        {"nyquist_ok": nyquist_ok, "R_bath": R_bath, "R_fric": R_fric, "stored": stored, "dissipated": dissipated},
    )


def run_w_battery() -> tuple[list[VResult], str]:
    """The frozen §B W-battery. Verdict classes (§B3, verbatim):
      • METER-VALID-NONLINEAR-ENVELOPE — all W1-W6 pass at ALL three operating points.
      • METER-PARTIAL-NONLINEAR — pass at mild/moderate, fail NEAR-KNEE (a SPECIFIC
        per-point pass map, not a catch-all for any non-kill failure).
      • METER-INVALID-NONLINEAR — the W2 kill fires at ANY point, OR the W3 collapse
        is lost.

    §B3-faithful reading (R-8 repair, PR #721 review). §B3 admits exactly three
    outcomes; a non-kill failure that is NOT the specific mild/moderate-pass /
    near-knee-fail pattern is OFF the §B3 map and must be adjudicated, NOT silently
    relabelled PARTIAL (the pre-repair `else` branch called every non-kill failure
    PARTIAL regardless of which point failed). Such a pattern returns an explicit
    METER-UNCLASSIFIED-DEVIATION demanding adjudication. The all-pass VALID path is
    unchanged.
    """
    results = [run_w1(), run_w2(), run_w3(), run_w4(), run_w5(), run_w6()]
    by = {r.vid: r for r in results}
    failed = [r.vid for r in results if not r.passed]
    # §B3 INVALID triggers, checked at ANY operating point: the W2 secular-pump kill,
    # or the W3 detuning-collapse lost.
    w2_kill = not by["W2"].passed and any(
        p.get("kill", False) for p in by["W2"].metrics.get("per_point", {}).values()
    )
    w3_lost = not by["W3"].passed
    # Per-operating-point failure map for the §B3 PARTIAL pattern (mild+moderate ALL
    # pass, near-knee any-fail). Legs W1/W2/W5 carry per-point data over all three
    # points; the moderate-only legs (W3/W4/W6) and the global receipts (W1 flag-no-op,
    # W6 Nyquist) attach to 'moderate'. W3 is handled above as an INVALID trigger.
    points = ("mild", "moderate", "near-knee")
    point_fail: dict[str, list[str]] = {pt: [] for pt in points}
    for pt, p in by["W1"].metrics.get("per_point", {}).items():
        if p.get("kill", False) or p.get("max_frac", 0.0) >= MACHINE_TOL:
            point_fail[pt].append("W1")
    for pt, p in by["W2"].metrics.get("per_point", {}).items():
        if p.get("kill", False) or p.get("collapsed", False):
            point_fail[pt].append("W2")
    for pt, p in by["W5"].metrics.get("per_point", {}).items():
        if p.get("match", 0.0) >= W5_TARE_C_TOL or not p.get("liveness_ok", True):
            point_fail[pt].append("W5")
    if not by["W1"].metrics.get("flag_no_op_ok", True):
        point_fail["moderate"].append("W1-flag")
    for vid in ("W4", "W6"):
        if not by[vid].passed:
            point_fail["moderate"].append(vid)
    near_knee_only = bool(point_fail["near-knee"]) and not point_fail["mild"] and not point_fail["moderate"]
    if not failed:
        verdict = "METER-VALID-NONLINEAR-ENVELOPE"
    elif w2_kill or w3_lost:
        verdict = f"METER-INVALID-NONLINEAR (W2-kill/W3-collapse-lost: {','.join(failed)})"
    elif near_knee_only:
        verdict = f"METER-PARTIAL-NONLINEAR({','.join(failed)})"
    else:
        # Off the §B3 map: a non-kill failure touching mild/moderate (or a
        # moderate-only leg). Not silently PARTIAL — demand adjudication.
        verdict = f"METER-UNCLASSIFIED-DEVIATION({','.join(failed)}; point_fail={point_fail}) — off §B3 map, adjudicate"
    return results, verdict


def main() -> None:
    ap = argparse.ArgumentParser(description="F6 bath meter validation battery (A: V1-V6 / W: nonlinear reval)")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    ap.add_argument(
        "--w-battery",
        action="store_true",
        help="run the §B NONLINEAR-regime revalidation battery (W1-W6) instead of the A-battery (V1-V6)",
    )
    ap.add_argument(
        "--fact4",
        action="store_true",
        help="measure the §B1 FACT-4 step/rescale non-commutation triple (opt-in provenance; NOT a gate)",
    )
    args = ap.parse_args()
    if args.fact4:
        nc = measure_noncommutation()
        if args.json:
            print(json.dumps(nc, indent=2))
        else:
            print("=" * 80)
            print("F6 BATH METER — FACT-4 non-commutation (opt-in; ‖step(s·x)−s·step(x)‖/‖step(x)‖)")
            print("=" * 80)
            for name, v in nc["noncommutation"].items():
                print(f"  {name:10s}: {v:.3e}")
            print(f"  growth mild→near-knee: {nc['growth_mild_to_near_knee']:.1f}×  (s={nc['s']})")
            print("=" * 80)
        return
    if args.w_battery:
        results, verdict = run_w_battery()
        title = "F6 BATH METER — W-BATTERY (nonlinear-regime revalidation; §B; NO F6 arm fired)"
    else:
        results, verdict = run_battery()
        title = "F6 BATH METER — VALIDATION BATTERY (plants only; NO F6 arm fired)"
    if args.json:
        print(json.dumps({"results": [asdict(r) for r in results], "verdict": verdict}, indent=2))
        return
    print("=" * 80)
    print(title)
    print("=" * 80)
    for r in results:
        print(f"[{'PASS' if r.passed else 'FAIL'}] {r.vid}: {r.detail}")
    print("-" * 80)
    print(f"VERDICT: {verdict}")
    print("=" * 80)


if __name__ == "__main__":
    main()
