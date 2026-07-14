#!/usr/bin/env python3
"""F6 tier-1 — global two-reservoir ODE ledger (rho_latent <-> T2 bath).

Implements EXACTLY the frozen spec of

    research/2026-07-13_f6-tier1-two-reservoir-ledger_CHARTER.md   (PR #666, binding)
    research/2026-07-13_f6-tier1-ledger-driver_prereg.md          (frozen tolerances/grid)

Sector header (inherited, CHARTER 0). MODE: global bookkeeping ODE ledger, NOT
a field solve (no a(t); solve_backreaction is static-elliptic). REGIME (QUARANTINE,
CHARTER 1.4): the top-stage cascade port at the cosmic operating point. PHASE-STATE:
a held static store (rho_latent) draining one-way into the T2 bath. SECTOR (QUARANTINE):
the A-class continuous-drainage behavior of the LOCAL top port; NOT A1 dilatation-mass,
NOT a Cosserat-winding claim.

Scope lock (CC-honest, CHARTER 4.4): EXISTENCE + FORM only. The slaving coupling
kappa is a FREE parameter, NOT derived from {l_node, alpha, G}. A bin (i) PASS
certifies CONSERVATION + FORM only -- never Ax3-entropic legality (cited premise,
tier-2) and never EMERGENCE. NO magnitude match to rho_Lambda anywhere: the
normalized observable is scale-invariant (see gate_magnitude_invariance), which is
the machine-checkable form of "no magnitude tune".

State (two scalars): rho_latent(t), E_T2(t).  Conservation ledger:
    d rho_latent/dt = -Gamma,   d E_T2/dt = +Gamma,   Gamma >= 0
    => rho_latent + E_T2 = const   (tol_cons).

Dimensionless reduction (prereg 2): tau = t/t_ref, t_ref = 1/H_INFINITY (canonical
Hubble-scale anchor). rho_hat = rho/rho(tau_0). The verdict is scale-free; H_INFINITY
enters only the physical-units annotation of the window.

    d rho_hat/dtau = -g_hat(tau) * rho_hat
    g_hat_LAMBDA    = 0
    g_hat_FRONTIER  = 3 H(tau) t_ref
    g_hat_ON        = kappa * n_hat_B(tau)          kappa = k * n_B(t0) * t_ref

Observable (CHARTER 1.6):
    rho_DE(t) == rho_latent(t),  rho_hat_DE(t) = rho_DE/rho_DE(t0)
    D[A,B] = || rho_hat_DE^A - rho_hat_DE^B ||_{L2([t0,t1])} / sqrt(t1-t0)
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

from ave.core.constants import H_INFINITY

# --------------------------------------------------------------------------
# FROZEN prereg parameters (research/2026-07-13_f6-tier1-ledger-driver_prereg.md)
# --------------------------------------------------------------------------
TAU_0: float = 1.0
TAU_1: float = 10.0
N_GRID: int = 2001
RTOL: float = 1e-11
ATOL: float = 1e-13
TOL_CONS: float = 1e-8
TOL_FORM: float = 1e-2
KAPPA_FID: float = 2.0
KAPPA_SCAN: tuple[float, ...] = (0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0)

# Input-only normalized store (clm-s4n33u, solidity 0.45; CHARTER 4.4). A pure
# normalization, NOT a physics magnitude; the verdict is invariant to it.
RHO_LATENT_INPUT: float = 1.0

# Canonical Hubble-scale time anchor. The verdict is scale-free; T_REF sets only
# the physical-units annotation H(t0) = (2/3) H_INFINITY.
T_REF: float = 1.0 / H_INFINITY

# NON-FROZEN sensitivity ladder (transparency only; the FROZEN verdict uses TOL_FORM).
THRESHOLD_LADDER: tuple[float, ...] = (1e-3, 1e-2, 1e-1, 3e-1)

ARMS = ("ON", "FRONTIER", "LAMBDA")


def _asarr(tau) -> np.ndarray:
    return np.asarray(tau, dtype=float)


# --------------------------------------------------------------------------
# Imported input histories (prereg 3) -- NOT evolved; analytic matter-era profiles.
# Each returns (g_hat_frontier(tau), n_hat_B(tau)), both dimensionless.
# --------------------------------------------------------------------------
def history_physical(tau):
    """FRW matter-era lock: a ~ tau^(2/3), H = 2/(3t) => g_frontier = 2/tau,
    n_matter ~ a^-3 => n_hat_B = tau^-2. Note n_matter ~ H^2 (different powers of a)."""
    tau = _asarr(tau)
    return 2.0 / tau, tau ** -2.0


def history_decorr_H_frozen(tau):
    """Decorrelation 1: H frozen at its tau_0 value (g_frontier = 2 const),
    n_matter still falls (n_hat_B = tau^-2). Breaks the H<->n_matter lock."""
    tau = _asarr(tau)
    return np.full(tau.shape, 2.0) if tau.shape else np.asarray(2.0), tau ** -2.0


def history_decorr_n_frozen(tau):
    """Decorrelation 2: n_matter frozen (n_hat_B = 1 const), H still falls
    (g_frontier = 2/tau). Breaks the H<->n_matter lock the other way."""
    tau = _asarr(tau)
    return 2.0 / tau, np.ones(tau.shape) if tau.shape else np.asarray(1.0)


HISTORIES = {
    "PHYSICAL": history_physical,
    "DECORR_H_FROZEN": history_decorr_H_frozen,
    "DECORR_N_FROZEN": history_decorr_n_frozen,
}


# --------------------------------------------------------------------------
# Transfer laws (CHARTER 1.6) -- the actuator. Pure multiplicative rate g_hat(tau);
# no sign(rate) branch, no threshold (DIODE-RESURRECTION mechanism-class, prereg 9.4).
# --------------------------------------------------------------------------
def drain_rate(arm: str, tau, history_fn, kappa: float) -> np.ndarray:
    g_frontier, n_hat_B = history_fn(tau)
    if arm == "LAMBDA":
        return np.zeros_like(_asarr(tau))
    if arm == "FRONTIER":
        return np.asarray(g_frontier, dtype=float)
    if arm == "ON":
        return kappa * np.asarray(n_hat_B, dtype=float)
    raise ValueError(f"unknown arm {arm!r}")


# --------------------------------------------------------------------------
# Ledger evolution. Integrates the joint 2-vector [rho_hat, E_T2_hat] so
# conservation is a genuine integrator check (not booked by construction).
# `booking` / `extra` are sabotage hooks acting on the EVOLVED trajectory.
# --------------------------------------------------------------------------
def evolve(arm, history_fn, kappa=0.0, rho0=RHO_LATENT_INPUT, booking=None, extra=None,
           tau0=TAU_0, tau1=TAU_1, ngrid=N_GRID):
    # tau0/tau1/ngrid default to the FROZEN window/grid; every frozen-battery call
    # uses the defaults (behavior byte-identical). The optional args serve ONLY the
    # NON-FROZEN transparency map (lambda_boundary_map), never a frozen verdict.
    def rhs(tau, y):
        rho, e = y
        g = float(drain_rate(arm, tau, history_fn, kappa))
        drho = -g * rho
        de = +g * rho
        if booking is not None:
            de = booking(g, rho, e)
        if extra is not None:
            drho, de = extra(tau, rho, e, g, drho, de)
        return (drho, de)

    sol = solve_ivp(
        rhs, (tau0, tau1), (rho0, 0.0),
        method="RK45", rtol=RTOL, atol=ATOL, dense_output=True,
    )
    tau_grid = np.linspace(tau0, tau1, ngrid)
    try:
        y = sol.sol(tau_grid)
        rho, e = np.asarray(y[0], float), np.asarray(y[1], float)
    except Exception:
        rho = np.full(ngrid, np.inf)
        e = np.full(ngrid, np.inf)
    ok = bool(sol.success) and np.all(np.isfinite(rho)) and np.all(np.isfinite(e))
    return tau_grid, rho, e, ok


def rho_hat(rho: np.ndarray) -> np.ndarray:
    return rho / rho[0]


def d_form(rhat_a: np.ndarray, rhat_b: np.ndarray, tau: np.ndarray) -> float:
    """D[A,B] = sqrt( trapz((rhat_A - rhat_B)^2, tau) / (tau1 - tau0) )."""
    diff2 = (rhat_a - rhat_b) ** 2
    integral = float(np.trapezoid(diff2, tau))
    return float(np.sqrt(integral / (tau[-1] - tau[0])))


# --------------------------------------------------------------------------
# Frozen closed-form solutions (prereg 3.4) -- integrator validation targets.
# --------------------------------------------------------------------------
def closed_form(arm: str, history_name: str, tau: np.ndarray, kappa: float) -> np.ndarray:
    tau = _asarr(tau)
    if arm == "LAMBDA":
        return np.ones_like(tau)
    if arm == "FRONTIER":
        if history_name == "DECORR_H_FROZEN":
            return np.exp(-2.0 * (tau - 1.0))
        return tau ** -2.0  # PHYSICAL, DECORR_N_FROZEN
    if arm == "ON":
        if history_name == "DECORR_N_FROZEN":
            return np.exp(-kappa * (tau - 1.0))
        return np.exp(-kappa * (1.0 - 1.0 / tau))  # PHYSICAL, DECORR_H_FROZEN
    raise ValueError(arm)


# --------------------------------------------------------------------------
# The four charter audits as machine gates (prereg 9). Each reads the evolved
# trajectory; a plant (below) trips it.
# --------------------------------------------------------------------------
def gate_conservation(rho: np.ndarray, e: np.ndarray, rho0: float = RHO_LATENT_INPUT) -> float:
    """IMPOSED-LEAK / bin (ii): max relative |rho_hat + E_T2 - const|."""
    if not (np.all(np.isfinite(rho)) and np.all(np.isfinite(e))):
        return float("inf")
    return float(np.max(np.abs((rho + e) - rho0)) / abs(rho0))


def gate_bounded_norm(tau, rho, e, rho0=RHO_LATENT_INPUT) -> dict:
    """TRILINEAR-PUMP: drain-only (rho monotone non-increasing), total bounded, finite."""
    finite = bool(np.all(np.isfinite(rho)) and np.all(np.isfinite(e)))
    if not finite:
        return {"ok": False, "finite": False, "monotone": False, "total_max": float("inf")}
    drho = np.diff(rho)
    monotone = bool(np.all(drho <= 1e-10 * rho0))
    total_max = float(np.max(rho + e))
    bounded = bool(total_max <= rho0 * (1.0 + TOL_CONS))
    return {"ok": (finite and monotone and bounded), "finite": finite,
            "monotone": monotone, "total_max": total_max, "bounded": bounded}


def reconstruct_g_eff(tau: np.ndarray, rho: np.ndarray) -> np.ndarray:
    """g_eff(tau) = -(d rho_hat/dtau)/rho_hat reconstructed from the trajectory."""
    rhat = rho / rho[0]
    drhat = np.gradient(rhat, tau)
    with np.errstate(divide="ignore", invalid="ignore"):
        g_eff = -drhat / rhat
    return g_eff


def gate_mechanism_class(arm, history_fn, kappa, tau, rho) -> dict:
    """DIODE-RESURRECTION: reconstructed g_eff must equal the DECLARED smooth law
    (continuous, no V_f dead-zone, no sign asymmetry). A dead-zone plant makes
    g_eff jump -> large deviation."""
    if not np.all(np.isfinite(rho)):
        return {"ok": False, "rel_dev": float("inf"), "max_jump": float("inf")}
    g_eff = reconstruct_g_eff(tau, rho)
    g_decl = np.array([float(drain_rate(arm, t, history_fn, kappa)) for t in tau])
    sl = slice(2, -2)  # drop one-sided-gradient endpoints
    scale = max(float(np.max(np.abs(g_decl))), 1e-12)
    rel_dev = float(np.max(np.abs(g_eff[sl] - g_decl[sl])) / scale)
    max_jump = float(np.max(np.abs(np.diff(g_eff[sl]))) / scale)
    return {"ok": (rel_dev <= 1e-3), "rel_dev": rel_dev, "max_jump": max_jump}


def gate_input_provenance(rho0_used, expected: float = RHO_LATENT_INPUT) -> dict:
    """MAGNITUDE-TUNE clause (a) (prereg §9.3): the rho_latent(t0) actually used in a
    verdict run must be byte-identical to the frozen RHO_LATENT_INPUT. Fires on ANY
    tune toward a fabricated rho_Lambda. This gate consumes the run's real initial
    value, not a default argument, so it CAN fire."""
    ok = (float(rho0_used) == float(expected))
    return {"ok": bool(ok), "rho0_used": float(rho0_used), "expected": float(expected)}


def gate_magnitude_invariance(arm, history_fn, kappa, scales=(1.0, 7.3, 1.0e6)) -> dict:
    """MAGNITUDE-TUNE clause (b) (prereg §9.3): EVERY D[.,.] must be invariant under an
    arbitrary rescale of the input store (no-magnitude guarantee). Asserts invariance of
    BOTH D[ON,FRONTIER] AND D[ON,LAMBDA] (not just the frontier pair). Also reports the
    clause-(a) input equality on each run (the run used exactly its requested input)."""
    d_frontier, d_lambda = [], []
    inputs_exact = True
    for s in scales:
        rho0 = RHO_LATENT_INPUT * s
        tau, rho, _e, _ok = evolve(arm, history_fn, kappa, rho0=rho0)
        _t, rf, _ef, _okf = evolve("FRONTIER", history_fn, 0.0, rho0=rho0)
        _t, rl, _el, _okl = evolve("LAMBDA", history_fn, 0.0, rho0=rho0)
        d_frontier.append(d_form(rho_hat(rho), rho_hat(rf), tau))
        d_lambda.append(d_form(rho_hat(rho), rho_hat(rl), tau))
        inputs_exact = inputs_exact and (float(rho[0]) == float(rho0))
    spread_f = float(max(d_frontier) - min(d_frontier))
    spread_l = float(max(d_lambda) - min(d_lambda))
    return {"ok": (spread_f <= 1e-12 and spread_l <= 1e-12 and inputs_exact),
            "spread_frontier": spread_f, "spread_lambda": spread_l,
            "inputs_exact": bool(inputs_exact),
            "D_frontier": d_frontier, "D_lambda": d_lambda}


# --------------------------------------------------------------------------
# Sabotage plants (prereg 9) -- act on the EVOLVED trajectory, trip one gate each.
# --------------------------------------------------------------------------
def plant_imposed_leak(eta: float):
    """Booking that loses energy: bath gains only eta<1 of the source loss."""
    def booking(g, rho, e):
        return eta * g * rho
    return booking


def plant_trilinear_pump(c: float):
    """v4-style indefinite pump: +c*rho*E fed to BOTH states => total norm runs away."""
    def extra(tau, rho, e, g, drho, de):
        pump = c * rho * e
        return drho + pump, de + pump
    return extra


def plant_diode_deadzone(rho_f: float):
    """Forward-voltage dead-zone: drain freezes once rho_hat drops below rho_f."""
    def extra(tau, rho, e, g, drho, de):
        if rho / RHO_LATENT_INPUT > rho_f:
            return drho, de
        return 0.0, 0.0
    return extra


def plant_magnitude_tune_score(arm, history_fn, kappa, rho_lambda_target, scale):
    """A magnitude-dependent 'verdict' (the 10^122 tune): reads un-normalized
    rho_DE(tau_1) against a fabricated rho_Lambda target. CHANGES under rescale,
    which the honest scale-invariance gate forbids."""
    _tau, rho, _e, _ok = evolve(arm, history_fn, kappa, rho0=RHO_LATENT_INPUT * scale)
    return float(abs(rho[-1] - rho_lambda_target))


# --------------------------------------------------------------------------
# Battery runner (prereg 7).
# --------------------------------------------------------------------------
def run_battery(kappa_scan=KAPPA_SCAN) -> dict:
    out: dict = {"histories": {}, "params": {
        "TAU_0": TAU_0, "TAU_1": TAU_1, "N_GRID": N_GRID,
        "TOL_CONS": TOL_CONS, "TOL_FORM": TOL_FORM,
        "KAPPA_FID": KAPPA_FID, "KAPPA_SCAN": list(kappa_scan),
        "RHO_LATENT_INPUT": RHO_LATENT_INPUT, "H_INFINITY": H_INFINITY,
        "T_REF_seconds": T_REF, "H_at_t0": (2.0 / 3.0) * H_INFINITY,
    }}
    for hname, hfn in HISTORIES.items():
        tau, rho_L, _e, _ = evolve("LAMBDA", hfn, 0.0)
        rh_L = rho_hat(rho_L)
        tau, rho_F, e_F, ok_F = evolve("FRONTIER", hfn, 0.0)
        rh_F = rho_hat(rho_F)
        cf_dev_F = float(np.max(np.abs(rh_F - closed_form("FRONTIER", hname, tau, 0.0))))
        rows = {}
        d_on_frontier_by_k = {}
        for kappa in kappa_scan:
            tau, rho_ON, e_ON, ok_ON = evolve("ON", hfn, kappa)
            rh_ON = rho_hat(rho_ON)
            d_of = d_form(rh_ON, rh_F, tau)
            d_ol = d_form(rh_ON, rh_L, tau)
            cons = gate_conservation(rho_ON, e_ON)
            bn = gate_bounded_norm(tau, rho_ON, e_ON)
            cf_dev = float(np.max(np.abs(rh_ON - closed_form("ON", hname, tau, kappa))))
            d_on_frontier_by_k[kappa] = d_of
            rows[kappa] = {
                "D_ON_FRONTIER": d_of, "D_ON_LAMBDA": d_ol,
                "cons_resid": cons, "bounded_norm_ok": bn["ok"],
                "closed_form_dev": cf_dev,
                "rho_hat_end_ON": float(rh_ON[-1]),
            }
        out["histories"][hname] = {
            "rows_by_kappa": rows,
            "min_D_ON_FRONTIER": float(min(d_on_frontier_by_k.values())),
            "argmin_kappa": float(min(d_on_frontier_by_k, key=d_on_frontier_by_k.get)),
            "D_ON_FRONTIER_fid": d_on_frontier_by_k.get(KAPPA_FID),
            "frontier_conserves": gate_conservation(rho_F, e_F),
            "frontier_closed_form_dev": cf_dev_F,
            "rho_hat_end_FRONTIER": float(rh_F[-1]),
        }
    return out


def lambda_boundary_map(kappa_fid: float = KAPPA_FID) -> dict:
    """NON-FROZEN transparency map (beyond the frozen window) — the chord's
    Lambda-degeneracy boundary, to ARM the RESULT §5.4 adjudication. It does NOT
    touch any frozen verdict (the frozen bins consume D[ON,FRONTIER] on the frozen
    window only). Three limits:

    (a) weak-kappa limit: as kappa->0 the ON drain shuts off and ON collapses onto
        LAMBDA identically, so inf_kappa D[ON,LAMBDA] = 0 (the shipped 'min_kappa'
        was a frozen-scan edge, not the infimum). Reports the kappa threshold below
        which D[ON,LAMBDA] <= tol_form on the frozen PHYSICAL window.
    (b) late-window limit: at fixed kappa_fid, sweeping the window START to later
        decades, D[ON,LAMBDA] falls (the drain-turn-on transient leaves the window)
        while D[ON,FRONTIER] rises -> in any late decade window the chord IS Lambda
        in this homogeneous observable.
    (c) genuine-form-existence limit: at the frontier-best-mimic kappa (turn-on
        window) the chord is FAR from Lambda (large D[ON,LAMBDA])."""
    out: dict = {}
    H = history_physical

    # (a) weak-kappa Lambda collapse on the frozen PHYSICAL window
    _t, rL, _e, _ = evolve("LAMBDA", H, 0.0)
    rhL = rho_hat(rL)
    ks = np.logspace(-3, 0, 400)
    d_ol = np.array([d_form(rho_hat(evolve("ON", H, k)[1]), rhL, _t) for k in ks])
    below = ks[d_ol <= TOL_FORM]
    out["a_weak_kappa"] = {
        "D_ON_LAMBDA_floor": float(d_ol.min()), "kmin_scanned": float(ks[0]),
        "kappa_threshold_le_tol_form": float(below.max()) if below.size else None,
        "note": "inf over kappa is 0 (kappa->0 => ON == LAMBDA identically)",
    }

    # (b) window-START sweep (decade windows), kappa_fid, PHYSICAL
    sweep = []
    for t0, t1 in [(1, 10), (3, 30), (10, 100), (30, 300), (100, 1000), (300, 3000), (1000, 10000)]:
        tau, rl, _el, _ = evolve("LAMBDA", H, 0.0, tau0=t0, tau1=t1)
        _t2, rf, _ef, _ = evolve("FRONTIER", H, 0.0, tau0=t0, tau1=t1)
        _t3, ron, _eo, _ = evolve("ON", H, kappa_fid, tau0=t0, tau1=t1)
        sweep.append({"window": [t0, t1],
                      "D_ON_LAMBDA": d_form(rho_hat(ron), rho_hat(rl), tau),
                      "D_ON_FRONTIER": d_form(rho_hat(ron), rho_hat(rf), tau)})
    out["b_window_start_sweep"] = sweep

    # (c) frontier-best-mimic kappa per history -> D[ON,LAMBDA] (frozen window)
    best = {}
    fine = np.logspace(-3, 3, 600)
    for name, hfn in HISTORIES.items():
        tau, rf, _ef, _ = evolve("FRONTIER", hfn, 0.0)
        rhf = rho_hat(rf)
        dof = np.array([d_form(rho_hat(evolve("ON", hfn, k)[1]), rhf, tau) for k in fine])
        kbest = float(fine[int(np.argmin(dof))])
        _t4, rl, _el, _ = evolve("LAMBDA", hfn, 0.0)
        _t5, ron, _eo, _ = evolve("ON", hfn, kbest)
        best[name] = {"kappa_best": kbest, "D_ON_FRONTIER": float(dof.min()),
                      "D_ON_LAMBDA": d_form(rho_hat(ron), rho_hat(rl), _t5)}
    out["c_frontier_best_mimic"] = best
    return out


def _ladder(d: float) -> dict:
    return {f"<= {t:g}": bool(d <= t) for t in THRESHOLD_LADDER}


def main() -> None:
    res = run_battery()
    print("=" * 74)
    print("F6 TIER-1 TWO-RESERVOIR LEDGER  (rho_latent <-> T2)   -- FORM battery")
    print("=" * 74)
    p = res["params"]
    print(f"window tau in [{p['TAU_0']}, {p['TAU_1']}]  N={p['N_GRID']}  "
          f"tol_cons={p['TOL_CONS']:g}  tol_form={p['TOL_FORM']:g}")
    print(f"H_INFINITY={p['H_INFINITY']:.6e} s^-1   H(t0)=(2/3)H_inf={p['H_at_t0']:.6e} s^-1"
          f"   t_ref={p['T_REF_seconds']:.4e} s   (verdict is SCALE-FREE)")
    print(f"kappa_fid={p['KAPPA_FID']}  scan={p['KAPPA_SCAN']}\n")

    for hname, h in res["histories"].items():
        print(f"--- history: {hname} ---")
        print(f"    FRONTIER: conserves(resid={h['frontier_conserves']:.2e})  "
              f"closed-form dev={h['frontier_closed_form_dev']:.2e}  "
              f"rho_hat(tau1)={h['rho_hat_end_FRONTIER']:.4e}")
        print(f"    {'kappa':>7} {'D[ON,FRONTIER]':>16} {'D[ON,LAMBDA]':>14} "
              f"{'cons_resid':>12} {'bnd':>4} {'cf_dev':>10} {'rhoON(t1)':>10}")
        for kappa, row in h["rows_by_kappa"].items():
            print(f"    {kappa:>7g} {row['D_ON_FRONTIER']:>16.6e} {row['D_ON_LAMBDA']:>14.6e} "
                  f"{row['cons_resid']:>12.2e} {str(row['bounded_norm_ok']):>4} "
                  f"{row['closed_form_dev']:>10.2e} {row['rho_hat_end_ON']:>10.4e}")
        print(f"    min_k D[ON,FRONTIER]={h['min_D_ON_FRONTIER']:.6e} "
              f"(argmin kappa={h['argmin_kappa']})  "
              f"ladder(min)={_ladder(h['min_D_ON_FRONTIER'])}\n")

    # NON-FROZEN Lambda-degeneracy boundary map (arms RESULT §5.4; no verdict change).
    lbm = lambda_boundary_map()
    res["lambda_boundary_map_NONFROZEN"] = lbm
    print("--- NON-FROZEN Lambda-degeneracy boundary map (transparency; arms §5.4) ---")
    a = lbm["a_weak_kappa"]
    print(f"  (a) weak-kappa: D[ON,LAMBDA] floor={a['D_ON_LAMBDA_floor']:.3e} @kmin={a['kmin_scanned']:g}; "
          f"D[ON,LAMBDA]<=tol_form for kappa<= {a['kappa_threshold_le_tol_form']:.4f}; inf=0 (kappa->0)")
    print("  (b) window-START sweep PHYSICAL kappa_fid (D[ON,LAMBDA] falls, D[ON,FRONTIER] rises):")
    for s in lbm["b_window_start_sweep"]:
        print(f"      window {str(s['window']):>14}: D[ON,LAMBDA]={s['D_ON_LAMBDA']:.4f}  "
              f"D[ON,FRONTIER]={s['D_ON_FRONTIER']:.4f}")
    print("  (c) frontier-best-mimic kappa: chord is FAR from LAMBDA:")
    for name, c in lbm["c_frontier_best_mimic"].items():
        print(f"      {name:>16} kbest={c['kappa_best']:.3g}  "
              f"D[ON,FRONTIER]={c['D_ON_FRONTIER']:.4f}  D[ON,LAMBDA]={c['D_ON_LAMBDA']:.4f}")

    out_path = Path(__file__).with_name("f6_tier1_two_reservoir_ledger_results.json")
    out_path.write_text(json.dumps(res, indent=2))
    print(f"\n[written] {out_path}")


if __name__ == "__main__":
    main()
