#!/usr/bin/env python3
"""F6 bath meter — VALIDATION driver (V1-V6 battery on synthetic plants only).

Charter: research/2026-07-16_f6-bath-meter_CHARTER.md
Instrument: src/ave/thermal/f6_bath_meter.py
Gate: hardware-ratings-map §7 (JOINT detector-rebuild GATE, post-#711/#714).

SECTOR / REGIME: R7 thermal / entropy-sink (T2). Cold plant — NO Op14 saturation,
NO |Γ|→1 yield wall, NO node mint. NO F6 ARM IS FIRED HERE: the meter is validated
on hand-built plants only. A METER-VALID verdict is an instrument certificate, NOT
a licence to fire an arm (that happens in a different lane, after rebasing onto the
sibling F1 fix — see charter §9).

The battery proves the two §7 gate conditions and the read's honesty:
  V1 lossless control      — no coupling ⇒ machine-conserved, N_occ=0
  V2 M-variation           — fixed physics, N_occ invariant across M (kills twin-64)
  V3 known-transfer plant  — narrowband tone ⇒ few modes; count tracks bandwidth, not M
  V4 friction plant        — real Re(Z) of matched magnitude ⇒ physical discriminator
  V5 back-reaction liveness — coupling ON vs OFF ⇒ different lattice trajectory
  V6 baseline convention   — on-shell E0; lossless-control ledger closes
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass

import numpy as np

from ave.core.k4_tlm import K4Lattice3D
from ave.thermal import LatticeBathCoupler, OscillatorBath, make_collar_mask

# --- frozen validation tolerances (charter §6) ---
MACHINE_TOL = 1e-10
N_OCC_M_TOL = 1
N_OCC_V3_TOL = 1
R_BATH_MAX = 0.2
R_FRICTION_MIN = 0.8
D_LIVE_MIN = 1e-3
FRICTION_MATCH_TOL = 0.20
V6_DRIFT_MAX = 0.02  # coupled-run total-energy drift ceiling (fraction of E0)

# --- frozen instrument operating point (ENGINEERING CHOICES — tagged, not physics) ---
N_GRID = 12
CENTER = (N_GRID // 2, N_GRID // 2, N_GRID // 2)
COLLAR_R_IN = 2.0
COLLAR_R_OUT = 4.0
KAPPA = 0.02
N_STEPS = 300
SEED = 1
M_DEFAULT = 64
M_LIST = (32, 64, 128)
V3_TONE_AMP = 0.5
V3_TONE_OMEGA = 0.5  # in the comb's driven band (ω_min=0.30 … 1.23 at M=32)


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


def _build(M: int = M_DEFAULT, kappa: float = KAPPA, friction: bool = False, gamma: float = 0.0) -> LatticeBathCoupler:
    """Build a coupled meter with the on-shell E0 convention (post-first-step)."""
    lat = K4Lattice3D(N_GRID, N_GRID, N_GRID, nonlinear=True, op3_bond_reflection=True, V_SNAP=1.0)
    _seed_lattice(lat)
    lat.step()  # on-shell: the V_ref=0 seed doubles at the first TLM connect (arm repairs)
    bath = OscillatorBath(M=M)
    collar = make_collar_mask(lat, CENTER, COLLAR_R_IN, COLLAR_R_OUT)
    return LatticeBathCoupler(lat, bath, collar, kappa=kappa, friction=friction, gamma=gamma)


def _run_coupled(cpl: LatticeBathCoupler, n_steps: int = N_STEPS, track: bool = False):
    """Advance the coupled meter; optionally track the total-energy ledger."""
    E0 = cpl.e_lat()
    drift = 0.0
    Etot0 = E0 + cpl.e_bath()
    for i in range(1, n_steps):
        cpl.step(i)
        if track:
            drift = max(drift, abs((cpl.e_lat() + cpl.e_bath()) - Etot0) / E0)
    return E0, drift


@dataclass
class VResult:
    vid: str
    passed: bool
    detail: str


# --- V1: lossless control -----------------------------------------------------
def run_v1() -> VResult:
    cpl = _build(kappa=0.0)
    E0, _ = _run_coupled(cpl)
    dE = abs(cpl.e_lat() - E0) / E0
    n_occ = cpl.bath.n_occ()
    ok = dE < MACHINE_TOL and n_occ == 0
    return VResult("V1", ok, f"|ΔE_lat|/E0={dE:.2e} (<{MACHINE_TOL:.0e}), N_occ={n_occ} (=0)")


# --- V2: M-variation (kills twin-64) -----------------------------------------
def run_v2() -> VResult:
    occ = {}
    for M in M_LIST:
        cpl = _build(M=M)
        _run_coupled(cpl)
        occ[M] = cpl.bath.n_occ()
    ref = occ[M_DEFAULT]
    ok = all(abs(occ[M] - ref) <= N_OCC_M_TOL for M in M_LIST)
    counts = [occ[M] for M in M_LIST]
    return VResult("V2", ok, f"N_occ(M={list(M_LIST)})={counts} — invariant≤{N_OCC_M_TOL}; NOT tracking M")


# --- V3: known-transfer plant (narrowband tone) -------------------------------
def run_v3() -> VResult:
    occ = {}
    top = None
    for M in M_LIST:
        cpl = _build(M=M)
        cpl.q_ext = lambda i: V3_TONE_AMP * np.sin(V3_TONE_OMEGA * i)
        _run_coupled(cpl)
        occ[M] = cpl.bath.n_occ()
        if M == M_DEFAULT:
            e = cpl.bath.mode_energy()
            top = float(cpl.bath.omega[int(np.argmax(e))])
    ref = occ[M_DEFAULT]
    # narrowband ⇒ few modes; predicted resonance count is small (O(1-3)); and invariant across M
    invariant = all(abs(occ[M] - ref) <= N_OCC_V3_TOL for M in M_LIST)
    narrow = ref <= 4
    peak_on_tone = abs(top - V3_TONE_OMEGA) <= 0.06
    ok = invariant and narrow and peak_on_tone
    counts = [occ[M] for M in M_LIST]
    return VResult(
        "V3",
        ok,
        f"N_occ(M={list(M_LIST)})={counts} (narrowband, few, invariant); peak ω={top:.3f}≈ω_d={V3_TONE_OMEGA}",
    )


# --- V4: friction plant (physical discriminator) ------------------------------
def _calibrate_gamma(e_bath_target: float) -> tuple[float, float]:
    """Bisect γ so the Re(Z) friction removes ≈ e_bath_target (matched magnitude)."""
    lo, hi = 1e-4, 5e-2
    removed = 0.0
    for _ in range(14):  # bisection: 14 halvings resolve γ far finer than the 20% match tol
        gamma = 0.5 * (lo + hi)
        cpl = _build(friction=True, gamma=gamma)
        E0, _ = _run_coupled(cpl)
        removed = E0 - cpl.e_lat()
        if removed < e_bath_target:
            lo = gamma
        else:
            hi = gamma
    return gamma, removed


def run_v4() -> VResult:
    # reactive bath reference
    cpl_b = _build()
    E0b, _ = _run_coupled(cpl_b)
    e_bath = cpl_b.e_bath()
    R_bath = abs((cpl_b.e_lat() - E0b) + e_bath) / max(abs(cpl_b.e_lat() - E0b), 1e-30)
    n_occ_bath = cpl_b.bath.n_occ()
    # friction plant, matched magnitude
    gamma, removed = _calibrate_gamma(e_bath)
    cpl_f = _build(friction=True, gamma=gamma)
    E0f, _ = _run_coupled(cpl_f)
    R_fric = abs((cpl_f.e_lat() - E0f) + cpl_f.e_bath()) / max(abs(cpl_f.e_lat() - E0f), 1e-30)
    n_occ_fric = cpl_f.bath.n_occ()
    matched = abs(removed - e_bath) / e_bath <= FRICTION_MATCH_TOL
    bath_bin = R_bath < R_BATH_MAX and n_occ_bath > 0
    fric_bin = R_fric > R_FRICTION_MIN and n_occ_fric == 0
    ok = matched and bath_bin and fric_bin
    return VResult(
        "V4",
        ok,
        f"matched: friction removed {removed:.3f} vs E_bath {e_bath:.3f} "
        f"(Δ={abs(removed - e_bath) / e_bath * 100:.0f}%≤{int(FRICTION_MATCH_TOL * 100)}%); "
        f"BATH[R={R_bath:.1e},N_occ={n_occ_bath}] vs FRICTION[R={R_fric:.2f},N_occ={n_occ_fric}] — different bins",
    )


# --- V5: back-reaction liveness -----------------------------------------------
def run_v5() -> VResult:
    on = _build()
    _run_coupled(on)
    off = _build(kappa=0.0)
    _run_coupled(off)
    num = float(np.linalg.norm(on.lat.V_inc - off.lat.V_inc))
    den = float(np.linalg.norm(off.lat.V_inc)) + 1e-30
    D = num / den
    ok = D > D_LIVE_MIN
    return VResult(
        "V5",
        ok,
        f"trajectory divergence ON vs OFF D={D:.3e} (>{D_LIVE_MIN:.0e}); coupling changes lattice dynamics",
    )


# --- V6: baseline convention --------------------------------------------------
def run_v6() -> VResult:
    # lossless control ledger (on-shell E0)
    cpl0 = _build(kappa=0.0)
    E0, _ = _run_coupled(cpl0)
    lossless = abs(cpl0.e_lat() - E0) / E0
    # coupled-run drift, tracked over the window
    cpl = _build()
    _E0c, drift = _run_coupled(cpl, track=True)
    ok = lossless < MACHINE_TOL and drift < V6_DRIFT_MAX
    return VResult(
        "V6",
        ok,
        f"on-shell E0 (post-first-step); lossless-control ledger={lossless:.2e} (<{MACHINE_TOL:.0e}); "
        f"coupled total-E drift max={drift:.2e} (<{V6_DRIFT_MAX}, non-secular, «friction bin)",
    )


def run_battery() -> tuple[list[VResult], str]:
    results = [run_v1(), run_v2(), run_v3(), run_v4(), run_v5(), run_v6()]
    failed = [r.vid for r in results if not r.passed]
    if not failed:
        verdict = "METER-VALID"
    elif {"V2", "V4", "V5"} & set(failed):
        # core requirements (M-invariance, friction discrimination, back-reaction)
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
    print("=" * 78)
    print("F6 BATH METER — VALIDATION BATTERY (plants only; NO F6 arm fired)")
    print("=" * 78)
    for r in results:
        print(f"[{'PASS' if r.passed else 'FAIL'}] {r.vid}: {r.detail}")
    print("-" * 78)
    print(f"VERDICT: {verdict}")
    print("=" * 78)


if __name__ == "__main__":
    main()
