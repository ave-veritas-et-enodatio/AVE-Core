#!/usr/bin/env python3
"""F6 bath meter — VALIDATION driver (V1-V6 battery on synthetic plants only).

Charter: research/2026-07-16_f6-bath-meter_CHARTER.md (+ amendment §A, 2026-07-17).
Instrument: src/ave/thermal/f6_bath_meter.py
Gate: hardware-ratings-map §7 (JOINT detector-rebuild GATE, post-#711/#714).

SECTOR / REGIME: R7 thermal / entropy-sink (T2). Cold plant (LINEAR lattice) —
NO Op14 saturation, NO |Γ|→1 yield wall, NO node mint. NO F6 ARM IS FIRED HERE:
the meter is validated on hand-built plants only. A verdict here certifies the
instrument, NOT an F6 result (the arm fires in a different lane, after rebasing
onto the sibling F1 fix — charter §9).

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


def _seed_lattice(lat: K4Lattice3D) -> None:
    """Deterministic broadband seed (fixed physics across the whole battery)."""
    rng = np.random.default_rng(SEED)
    ii, jj, kk = np.indices((lat.nx, lat.ny, lat.nz))
    c = CENTER
    env = np.exp(-((ii - c[0]) ** 2 + (jj - c[1]) ** 2 + (kk - c[2]) ** 2) / (2 * 1.5**2))
    env[~lat.mask_active] = 0.0
    for p in range(4):
        lat.V_inc[..., p] += 0.08 * env
    fld = np.zeros_like(lat.V_inc)
    for _ in range(6):
        kv = rng.integers(1, lat.nx // 2, size=3) * (2 * np.pi / lat.nx) * rng.choice([-1, 1], size=3)
        ph = rng.uniform(0, 2 * np.pi)
        pw = np.cos(kv[0] * ii + kv[1] * jj + kv[2] * kk + ph)
        pw2 = rng.normal(size=4)
        for p in range(4):
            fld[..., p] += 0.03 * pw * pw2[p]
    fld[~lat.mask_active] = 0.0
    lat.V_inc += fld


def _build(
    M: int = M_DEFAULT,
    kappa: float = KAPPA,
    friction: bool = False,
    beta: float = 0.0,
    delta_omega: float = DELTA_OMEGA,
    omega_min: float = OMEGA_MIN,
) -> LatticeBathCoupler:
    """Build a coupled meter (LINEAR cold-plant lattice) with on-shell E0.

    E0 is captured after the first step() (on-shell): the V_ref=0 seed doubles at
    the first TLM connect (both arm repairs — Arm A A3 / Arm B A2).
    """
    lat = K4Lattice3D(N_GRID, N_GRID, N_GRID, nonlinear=False, op3_bond_reflection=True, V_SNAP=1.0)
    _seed_lattice(lat)
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


def main() -> None:
    ap = argparse.ArgumentParser(description="F6 bath meter validation battery (V1-V6)")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    args = ap.parse_args()
    results, verdict = run_battery()
    if args.json:
        print(json.dumps({"results": [asdict(r) for r in results], "verdict": verdict}, indent=2))
        return
    print("=" * 80)
    print("F6 BATH METER — VALIDATION BATTERY (plants only; NO F6 arm fired)")
    print("=" * 80)
    for r in results:
        print(f"[{'PASS' if r.passed else 'FAIL'}] {r.vid}: {r.detail}")
    print("-" * 80)
    print(f"VERDICT: {verdict}")
    print("=" * 80)


if __name__ == "__main__":
    main()
