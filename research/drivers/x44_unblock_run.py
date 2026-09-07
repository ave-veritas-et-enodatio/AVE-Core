#!/usr/bin/env python3
"""X44-UNBLOCK — THE PRE-REGISTERED RUN.

Executes, verbatim and in order, the gates and measurements frozen in
`research/2026-08-27_x44-unblock_prereg_FROZEN.md` (blob
1ea7b129d7527f9e4a7e0585f9066b1e8a65e803), and evaluates the frozen bin ladder
(§10.2: Z -> Y -> A -> B -> C -> D, strictly sequential, first match wins).

WHAT IS INSTALLED. The frozen weight (§3.1), behind an explicit engine mode:

    n_scalar = 1 + k*eps11 ,  w = 1/n_scalar ,  T00_src = T00_matter * w
    k        = 1/7   (canon: ponderomotive-equivalence.md:14)
    1 - w    = k*eps11 + O(eps11^2)          # LINEAR

installed as `ave.gravity.backreaction.source_mode="ponderomotive"`. The shipped
`source_mode="komar"` weight -- `(1-eps11^2)^{1/4}`, whose expansion has NO linear
term -- is retained (KEEP-BOTH) and is run here as the CONTROL.

THE DRIVER ADJUDICATES NOTHING. It computes the frozen quantities (§10.1),
evaluates the frozen clauses at their frozen edges, and prints the first bin the
frozen order reaches. Bins Z and Y are OVERRIDING: if either fires, `c`,
`k_meas` and `eta_mixed` are reported UNINTERPRETABLE, not as evidence.

ANTI-FITTING (§12.4). `k` is FROZEN at 1/7 and `g_self` at 1.0. The four-value
sweep `k in {0, 1/7, 2/7, 1/2}` is the pre-registered instrument-resolving-power
PROBE (P8), never a proposal; `k = 1/2` reconciles `eta_mixed` exactly and is
FORBIDDEN as an adopted value.

Run from the repo root:  python3 research/drivers/x44_unblock_run.py
Add `--json PATH` to also write the full measurement record.
"""

from __future__ import annotations

import argparse
import json
import sys
import time

sys.path.insert(0, "src")
sys.path.insert(0, "src/tests")

import numpy as np  # noqa: E402
import scipy.sparse as sparse  # noqa: E402

from engine_acceptance import _nordtvedt as NV  # noqa: E402

from ave.gravity.backreaction import (  # noqa: E402
    komar_weight,
    ponderomotive_weight,
    ray_trace_deflection,
)
from ave.solvers.graded_vacuum_network import stiffness_profile  # noqa: E402

# ── FROZEN CONSTANTS (prereg §5.1, §10.1) ─────────────────────────────────────
N_BASE = 24
S_MIN = 1e-3
G_SELF = 1.0                      # FROZEN, operator-forced (§4.4). No sweep.
K_FROZEN = 1.0 / 7.0              # FROZEN clock coefficient (§3.1). No sweep.
M_TARGET = 4.0

FAM_A_SIGMAS = (1.4, 1.8, 2.2, 2.6)                     # the frozen #651 family
FAM_B_SIGMA = 1.8
FAM_B_LAMBDAS = (0.25, 0.5, 1.0, 2.0, 4.0, 6.0, 8.0)    # 32x rest-energy span
RES_NS = (24, 32, 40)                                    # P7 resolution receipt
K_PROBE = (0.0, 1.0 / 7.0, 2.0 / 7.0, 0.5)               # P8 discrimination

# §5.3 PASS brackets for `c`, pre-computed in the frozen prereg. Copied verbatim
# from the frozen table; NOT recomputed here (recomputing a frozen edge from the
# run's own field would make the bracket self-referential).
PASS_BRACKET = {
    0.25: (0.2844, 0.2859),
    0.50: (0.2831, 0.2863),
    1.00: (0.2805, 0.2882),
    2.00: (0.2756, 0.2957),
    4.00: (0.2673, 0.3263),
    6.00: (0.2612, 0.3796),
    8.00: (0.2570, 0.4591),
}

# A1 edge (§10.3): k_meas in 1/7 +/- 5e-4.
A1_LO, A1_HI = 0.142357, 0.143357


def _grad_sq(eps11: np.ndarray, Grad) -> np.ndarray:
    """|grad eps11|^2 on the NATIVE diamond-K4 stencil (Z6: no np.gradient)."""
    n = eps11.shape[0]
    g = (Grad @ eps11.reshape(-1)).reshape(3, n, n, n)
    return (g**2).sum(axis=0)


def measure(
    n: int,
    T00: np.ndarray,
    *,
    source_mode: str,
    k: float,
    Grad,
    Div,
    mask: np.ndarray,
    s_min: float = S_MIN,
) -> dict:
    """One configuration -> every frozen quantity of §10.1.

    Reuses the certified entry points verbatim (`_nordtvedt.solve_config` ->
    `solve_backreaction`, `field_energy_density`, `stiffness_profile`,
    `_build_native_grad_div`). Reimplements no stencil, kernel or stepper.
    """
    res = NV.solve_config(n, T00, g_self=G_SELF, s_min=s_min, source_mode=source_mode, k_clock=k)
    eps = res["eps11"]
    T00_src = res["T00_total"]

    gsq = _grad_sq(eps, Grad)                                   # |grad eps|^2, K4
    A = np.clip(eps.reshape(-1), 0.0, 1.0)
    D = stiffness_profile(A, exponent=0.5, S_min=s_min).reshape(eps.shape)  # 1/S
    sum_gsq = float(gsq.sum())
    sum_Dgsq = float((D * gsq).sum())

    U = 0.5 * G_SELF * sum_gsq                                  # shipped register
    U_D = 0.5 * G_SELF * sum_Dgsq                               # D-consistent
    D_w = sum_Dgsq / sum_gsq                                    # <D>_w

    w = ponderomotive_weight(eps, k=k) if source_mode == "ponderomotive" else komar_weight(eps, S_min=s_min)
    D_clock = float((T00 * (1.0 - w)).sum())

    Ac = np.clip(eps, 0.0, 1.0)
    denom_chi = float((T00 * eps).sum())
    chi = float((T00 * eps / (1.0 + k * Ac)).sum()) / denom_chi  # T00*eps-weighted

    M = float(T00.sum())
    U_bind = float(res["U_bind"])
    M_eff = float(res["M_eff"])

    L = NV.stiffness_operator(n, eps, Grad, Div, s_min=s_min)
    m_g = NV.gravitating_charge_flux(eps, L, mask)
    sum_src_interior = float(T00_src[mask].sum())

    c = D_clock / U
    c_D = D_clock / U_D

    # Z1 -- the frozen broadcast detector, verbatim (§11.1): replace w by its
    # T00-weighted scalar mean and recompute.
    w_bar = float((T00 * w).sum() / M)
    D_clock_broadcast = (1.0 - w_bar) * M
    # FLAGGED DIAGNOSTIC (not the frozen gate, not an input to any bin): the same
    # broadcast built from the UNWEIGHTED interior-lattice mean of w.
    w_bar_unw = float(w[mask].mean())
    D_clock_bcast_unw = (1.0 - w_bar_unw) * M

    return {
        "N": n,
        "source_mode": source_mode,
        "k": float(k),
        "converged": bool(res["converged"]),
        "max_A": float(res["max_A"]),
        "M": M,
        "U_bind": U_bind,
        "U_bind_D": U_D,
        "M_eff": M_eff,
        "f": U_bind / (M + U_bind),
        "m_g": m_g,
        "sum_T00_src_interior": sum_src_interior,
        "ratio_mg_over_Meff": m_g / M_eff,
        "Delta_clock": D_clock,
        "Delta_clock_broadcast": D_clock_broadcast,
        "w_bar": w_bar,
        "D_w": D_w,
        "chi": chi,
        "c": c,
        "c_D": c_D,
        "k_meas": c * G_SELF / (2.0 * D_w * chi),
        "V_resid": abs(float((T00_src * eps).sum()) / sum_Dgsq - 1.0),
        "gauss_resid": abs(m_g / sum_src_interior - 1.0),
        "U_over_M": U_bind / M,
        "w_bar_unweighted": w_bar_unw,
        "_Delta_clock_unweighted_bcast": D_clock_bcast_unw,
        "_U_mine": U,          # Z6 leg 1: my K4 |grad|^2 vs the engine's own
        "_eps": eps,
    }


# ── GATE 1 (§15.1.1) — adjointness, the blind spot the freeze lane flagged ─────
def gate_adjointness(n: int) -> dict:
    """`Div == Grad^T` EXACTLY. §4.2's virial identity is void without it, and the
    freeze lane read it off the construction rather than asserting it (§14.3.4)."""
    Grad, Div = NV.build_grad_div(n)
    Dm = (Div - Grad.T).tocoo()
    nnz = int(Dm.nnz)
    max_abs = float(np.abs(Dm.data).max()) if nnz else 0.0
    return {"N": n, "nnz_diff": nnz, "max_abs_diff": max_abs, "pass": max_abs == 0.0}


def eta_of_family(rows: list[dict]) -> float:
    return NV.eta_slope([r["f"] for r in rows], [r["ratio_mg_over_Meff"] for r in rows])


def run_family_A(*, source_mode: str, k: float) -> list[dict]:
    Grad, Div = NV.build_grad_div(N_BASE)
    mask = NV.interior_mask(N_BASE)
    out = []
    for sig in FAM_A_SIGMAS:
        T00 = NV.normalized_blob(N_BASE, sig, M_TARGET)
        r = measure(N_BASE, T00, source_mode=source_mode, k=k, Grad=Grad, Div=Div, mask=mask)
        r["sigma"] = sig
        out.append(r)
    return out


def run_family_B(*, source_mode: str, k: float) -> list[dict]:
    Grad, Div = NV.build_grad_div(N_BASE)
    mask = NV.interior_mask(N_BASE)
    out = []
    for lam in FAM_B_LAMBDAS:
        T00 = NV.normalized_blob(N_BASE, FAM_B_SIGMA, M_TARGET * lam)
        r = measure(N_BASE, T00, source_mode=source_mode, k=k, Grad=Grad, Div=Div, mask=mask)
        r["lambda"] = lam
        out.append(r)
    return out


def run_resolution(*, k: float) -> list[dict]:
    """P7 / Y4 — `c` at N in {24, 32, 40}, lambda = 1."""
    out = []
    for n in RES_NS:
        Grad, Div = NV.build_grad_div(n)
        mask = NV.interior_mask(n)
        T00 = NV.normalized_blob(n, FAM_B_SIGMA, M_TARGET)
        r = measure(n, T00, source_mode="ponderomotive", k=k, Grad=Grad, Div=Div, mask=mask)
        out.append(r)
    return out


def run_k_probe() -> list[dict]:
    """P8 / Z3 — install k in {0, 1/7, 2/7, 1/2} at lambda = 1. A PROBE (§12.2)."""
    Grad, Div = NV.build_grad_div(N_BASE)
    mask = NV.interior_mask(N_BASE)
    T00 = NV.normalized_blob(N_BASE, FAM_B_SIGMA, M_TARGET)
    out = []
    for k in K_PROBE:
        r = measure(N_BASE, T00, source_mode="ponderomotive", k=k, Grad=Grad, Div=Div, mask=mask)
        out.append(r)
    return out


# ── P10 (§7, §15.1.7) — the enumeration + its numerical leg ────────────────────
P10_OBSERVABLES = (
    "far-field Gauss flux  m_g = Sum_interior(L eps11)",
    "naive exterior monopole coefficient  b  of the a + b/r fit",
    "ray-traced deflection  delta  at fixed impact parameter",
    "monopole plateau       flux(r) for r beyond the source support",
    "exterior shape         radial profile of eps11, amplitude-normalised",
)


def run_p10(k_rows: list[dict]) -> dict:
    """Every observable in P10_OBSERVABLES, measured under the four installed
    weights at lambda = 1, each normalised by that run's OWN installed source
    `Sum T00_src`. P10 is FALSIFIED by any observable whose normalised value
    varies across `k` beyond the solve residual -- that observable would carry
    information about the weight independent of the install.

    COMPLETENESS: this is the list I enumerated and tested, arrived at from the
    prereg's own §7 candidate list plus the two the code path exposes. It is NOT
    a claim that the engine has no other observable. The structural leg is the
    code-path fact (reported separately): the weight enters the pipeline at
    exactly one site, `build_picard_source`.
    """
    n = N_BASE
    rr = NV.radius_grid(n)
    rows = []
    for r in k_rows:
        eps = r["_eps"]
        src = r["sum_T00_src_interior"]
        b_fit, r2 = NV.naive_monopole_K(eps, rr, r_in=6.0, r_out=10.0)
        delta = ray_trace_deflection(eps, impact_b=6.0)
        # plateau: enclosed flux at two exterior radii, normalised
        Grad, Div = NV.build_grad_div(n)
        L = NV.stiffness_operator(n, eps, Grad, Div, s_min=S_MIN)
        flux, _ = NV.enclosed_flux_vs_radius(eps, L, np.zeros_like(eps), rr, (8.0, 10.0))
        # exterior shape: eps profile on a fixed radial window, amplitude-normalised
        shell = (rr >= 6.0) & (rr <= 10.0)
        prof = float(eps[shell].mean())
        rows.append(
            {
                "k": r["k"],
                "sum_T00_src": src,
                "m_g_norm": r["m_g"] / src,
                "b_fit_norm": b_fit / src,
                "b_fit_r2": r2,
                "delta_norm": delta / src,
                "plateau_r8_norm": flux[0] / src,
                "plateau_r10_norm": flux[1] / src,
                "shape_norm": prof / src,
            }
        )
    spreads = {}
    for key in ("m_g_norm", "b_fit_norm", "delta_norm", "plateau_r8_norm", "plateau_r10_norm", "shape_norm"):
        vals = np.array([x[key] for x in rows], float)
        spreads[key] = float(np.abs(vals / vals[1] - 1.0).max())  # ref = the frozen k = 1/7
    return {"rows": rows, "max_rel_spread": spreads, "observables": list(P10_OBSERVABLES)}


def _gate_z6(rows: list[dict]) -> dict:
    """Z6 — STENCIL. `|grad eps11|^2` in EVERY ledger term must come from the native
    diamond-K4 `Grad` (`_build_native_grad_div`), never a Cartesian gradient.

    Two independent legs, neither of which inspects THIS file's own text -- a
    scanner that greps its own source matches its own gate description and fires
    on itself (that bug was made, caught and removed here; the self-referential
    probe class).

    LEG 1 (behavioural, the load-bearing one): the `|grad eps|^2` this driver
    forms must be BIT-IDENTICAL to the engine's own `field_energy_density`
    reading, which is built on `_build_native_grad_div` inside the solver. If the
    driver had substituted any other stencil the two would part.

    LEG 2 (structural): the Cartesian-gradient call form appears nowhere on the
    gravity path. The token is assembled at runtime so that this file never
    contains the literal it searches for.
    """
    leg1_dev = max(abs(r["_U_mine"] / r["U_bind"] - 1.0) for r in rows)
    token = "np." + "gradient" + "("
    scanned = (
        "src/ave/gravity/backreaction.py",
        "src/ave/gravity/gw_propagation.py",
        "src/ave/solvers/graded_vacuum_network.py",
        "src/tests/engine_acceptance/_nordtvedt.py",
        "research/drivers/x44_unblock_run.py",
    )
    hits = {}
    for path in scanned:
        try:
            with open(path, encoding="utf-8") as fh:
                hits[path] = fh.read().count(token)
        except OSError:
            hits[path] = -1  # unreadable -> reported, never silently passed
    leg2_hits = sum(v for v in hits.values() if v > 0)
    unreadable = [p for p, v in hits.items() if v < 0]
    return {
        "fires": bool(leg1_dev != 0.0 or leg2_hits > 0 or unreadable),
        "leg1_max_dev_vs_field_energy_density": leg1_dev,
        "leg2_cartesian_call_hits": leg2_hits,
        "leg2_files_scanned": len(scanned),
        "leg2_unreadable": unreadable,
        "stencil": "diamond-K4 _build_native_grad_div (via _nordtvedt.build_grad_div)",
    }


def z1_diagnostics(*, ctrl: list[dict], famA: list[dict], famB: list[dict]) -> dict:
    """FLAGGED DIAGNOSTIC — not part of the frozen gate, not an input to any bin.

    The frozen Z1 detector (§11.1) is `Delta_broadcast = (1 - w_bar)*M` with
    `w_bar` the T00-weighted mean of `w`. Since `Delta_clock = Sum T00 (1-w)` and
    `w_bar = Sum T00 w / Sum T00`, we have

        (1 - w_bar)*M = Sum T00 - Sum T00 w = Sum T00 (1-w) = Delta_clock

    IDENTICALLY, for ANY weight. This records that, and records what a detector
    that is NOT an identity of its own target reads on the same fields: the
    UNWEIGHTED interior-lattice mean of `w`, broadcast. Reported so the reader can
    see WHICH property made Z1 fire. The frozen gate still governs the bin.
    """
    out = {}
    for name, rows in (("control_shipped_komar", ctrl), ("famA_frozen", famA), ("famB_frozen", famB)):
        out[name] = {
            "frozen_detector_max_dev": max(abs(r["Delta_clock_broadcast"] / r["Delta_clock"] - 1.0) for r in rows),
            "unweighted_variant_max_dev": max(abs(r["_Delta_clock_unweighted_bcast"] / r["Delta_clock"] - 1.0) for r in rows),
        }
    return out


# ── FROZEN BIN LADDER (§10.2 / §10.3) ─────────────────────────────────────────
def evaluate_bins(*, famA, famB, res_rows, k_rows, adj) -> dict:
    """Evaluate the frozen clauses at their frozen edges, in the frozen order.
    NOTHING here re-interprets a bin; the clause text is quoted in each label."""
    allm = list(famA) + list(famB)

    # ---- BIN Z ----------------------------------------------------------------
    z1_vals = [abs(r["Delta_clock_broadcast"] / r["Delta_clock"] - 1.0) for r in allm]
    z1 = {"fires": bool(min(z1_vals) < 0.10), "max": max(z1_vals), "min": min(z1_vals)}

    fA = [r["f"] for r in famA]
    z2_A = max(fA) / min(fA)
    z2_B = max(FAM_B_LAMBDAS) / min(FAM_B_LAMBDAS)
    z2 = {"fires": bool(z2_A < 2.0 or z2_B < 8.0), "famA_f_ratio": z2_A, "famB_lambda_ratio": z2_B}

    cs = sorted(r["c"] for r in k_rows)
    gaps = [cs[i + 1] - cs[i] for i in range(len(cs) - 1)]
    lo, hi = PASS_BRACKET[1.00]
    half = 0.5 * (hi - lo)
    z3 = {
        "fires": bool(any(g <= 10.0 * half for g in gaps)),
        "c_sorted": cs,
        "gaps": gaps,
        "required_gap": 10.0 * half,
    }

    z4 = {"fires": bool(any(r["U_over_M"] < 1e-3 for r in famA)), "min_U_over_M": min(r["U_over_M"] for r in famA)}
    z5 = {"fires": bool(any(r["max_A"] >= 0.99 for r in allm)), "max_A": max(r["max_A"] for r in allm)}
    z6 = _gate_z6(allm)

    Z = {"Z1": z1, "Z2": z2, "Z3": z3, "Z4": z4, "Z5": z5, "Z6": z6}
    Z_fires = [k for k, v in Z.items() if v["fires"]]

    # ---- BIN Y ----------------------------------------------------------------
    y1 = {"fires": bool(any(not r["converged"] for r in allm)),
          "n_unconverged": sum(1 for r in allm if not r["converged"])}
    y2 = {"fires": bool(any(r["V_resid"] > 1e-6 for r in allm)),
          "max_V_resid": max(r["V_resid"] for r in allm),
          "offenders": [(r.get("sigma", r.get("lambda")), r["V_resid"]) for r in allm if r["V_resid"] > 1e-6]}
    y3 = {"fires": bool(any(r["gauss_resid"] > 1e-4 for r in allm)),
          "max_gauss_resid": max(r["gauss_resid"] for r in allm)}
    rc = [r["c"] for r in res_rows]
    y4_drift = (max(rc) - min(rc)) / min(rc)
    y4 = {"fires": bool(y4_drift > 0.01), "drift": y4_drift, "c_by_N": dict(zip(RES_NS, rc))}
    Y = {"Y1": y1, "Y2": y2, "Y3": y3, "Y4": y4}
    Y_fires = [k for k, v in Y.items() if v["fires"]]

    # ---- BINS A / B / C / D ---------------------------------------------------
    a1_ok = all(A1_LO <= r["k_meas"] <= A1_HI for r in famB)
    a2_ok = all(PASS_BRACKET[r["lambda"]][0] <= r["c"] <= PASS_BRACKET[r["lambda"]][1] for r in famB)
    a3_dev = [abs(r["c_D"] / ((2.0 * K_FROZEN / G_SELF) * r["chi"]) - 1.0) for r in famB]
    a3_ok = all(d <= 1e-3 for d in a3_dev)
    a4_ok = all(r["V_resid"] <= 1e-6 for r in famB)
    A = {"A1": a1_ok, "A2": a2_ok, "A3": a3_ok, "A4": a4_ok,
         "A3_dev_max": max(a3_dev), "A3_dev_min": min(a3_dev),
         "k_meas_range": [min(r["k_meas"] for r in famB), max(r["k_meas"] for r in famB)]}
    B_ok = (a1_ok and a2_ok) and (not a3_ok) and max(a3_dev) <= 1e-1
    k1 = [r["k_meas"] for r in famB if r["lambda"] == 1.0][0]
    C_named = [nm for nm, val in (("0", 0.0), ("2/7", 2.0 / 7.0), ("1/2", 0.5)) if abs(k1 - val) <= 0.01]
    C_ok = (not a1_ok) and bool(C_named)

    if Z_fires:
        bin_id, why = "Z", f"ARTIFACT — clause(s) {', '.join(Z_fires)} fired (step 1, overriding)"
    elif Y_fires:
        bin_id, why = "Y", f"INCONCLUSIVE — clause(s) {', '.join(Y_fires)} fired (step 2, overriding)"
    elif a1_ok and a2_ok and a3_ok and a4_ok:
        bin_id, why = "A", "WEIGHT CONFIRMED, GAP STRUCTURAL"
    elif B_ok:
        bin_id, why = "B", "WEIGHT CONFIRMED, RESIDUAL UNEXPLAINED"
    elif C_ok:
        bin_id, why = "C", f"COEFFICIENT MISMATCH — k_meas(lambda=1) near {C_named}"
    else:
        bin_id, why = "D", "WEIGHT FALSIFIED"

    return {
        "Z": Z, "Z_fires": Z_fires, "Y": Y, "Y_fires": Y_fires,
        "A": A, "B_would_fire": B_ok, "C_would_fire": C_ok, "C_named": C_named,
        "k_meas_lambda1": k1, "adjointness": adj,
        "BIN": bin_id, "why": why,
        "interpretable": bin_id not in ("Z", "Y"),
    }


def _strip(rows):
    return [{k: v for k, v in r.items() if not k.startswith("_")} for r in rows]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default=None, help="also write the full record here")
    args = ap.parse_args()
    t0 = time.time()

    print("# X44-UNBLOCK — pre-registered run")
    print(f"# frozen weight: w = 1/(1 + k*eps11), k = 1/7 = {K_FROZEN:.10f}; g_self = {G_SELF} (both FROZEN)")
    print()

    # GATE 1 — adjointness (blind spot §14.3.4)
    print("## GATE 1 — adjointness  ||Div - Grad^T||")
    adj = [gate_adjointness(n) for n in RES_NS]
    for a in adj:
        print(f"   N={a['N']:>3}  nnz(Div - Grad^T) = {a['nnz_diff']}  max|.| = {a['max_abs_diff']:.3e}  -> {'PASS' if a['pass'] else 'FAIL'}")
    print()

    # CONTROL — the shipped quadratic weight, X44's own number
    print("## CONTROL — shipped komar weight (1-eps^2)^(1/4), FAM-A, N=24")
    ctrl = run_family_A(source_mode="komar", k=K_FROZEN)
    print(f"   {'sigma':>6} {'f':>8} {'m_g':>10} {'M_eff':>10} {'c':>9} {'maxA':>7} {'conv':>5}")
    for r in ctrl:
        print(f"   {r['sigma']:6.2f} {r['f']:8.4f} {r['m_g']:10.5f} {r['M_eff']:10.5f} "
              f"{r['c']:9.5f} {r['max_A']:7.4f} {str(r['converged']):>5}")
    eta_ctrl = eta_of_family(ctrl)
    print(f"   eta_mixed(CONTROL) = {eta_ctrl:+.6f}     [X44 measured +1.048]")
    print()

    # FAM-A under the frozen weight — the REPORTED eta_mixed (P6)
    print("## FAM-A — frozen ponderomotive weight, N=24")
    famA = run_family_A(source_mode="ponderomotive", k=K_FROZEN)
    print(f"   {'sigma':>6} {'f':>8} {'m_g':>10} {'M_eff':>10} {'c':>9} {'c_D':>9} {'maxA':>7} {'conv':>5}")
    for r in famA:
        print(f"   {r['sigma']:6.2f} {r['f']:8.4f} {r['m_g']:10.5f} {r['M_eff']:10.5f} "
              f"{r['c']:9.5f} {r['c_D']:9.6f} {r['max_A']:7.4f} {str(r['converged']):>5}")
    eta_frozen = eta_of_family(famA)
    print(f"   eta_mixed(FROZEN WEIGHT) = {eta_frozen:+.6f}   [P6 predicted +0.831 +/- 0.010 — POST-DICTED, §13.1]")
    print()

    # FAM-B — the amplitude ladder, the adjudicated quantity
    print("## FAM-B — amplitude ladder, N=24, sigma=1.8")
    famB = run_family_B(source_mode="ponderomotive", k=K_FROZEN)
    print(f"   {'lam':>6} {'maxA':>7} {'f':>8} {'c':>9} {'bracket':>18} {'c_D':>9} {'<D>_w':>9} {'chi':>9} {'k_meas':>9} {'V_res':>9} {'gauss':>9} {'conv':>5}")
    for r in famB:
        lo, hi = PASS_BRACKET[r["lambda"]]
        inb = "in" if lo <= r["c"] <= hi else "OUT"
        print(f"   {r['lambda']:6.2f} {r['max_A']:7.4f} {r['f']:8.4f} {r['c']:9.6f} "
              f"[{lo:.4f},{hi:.4f}]{inb:>4} {r['c_D']:9.6f} {r['D_w']:9.6f} {r['chi']:9.6f} "
              f"{r['k_meas']:9.6f} {r['V_resid']:9.2e} {r['gauss_resid']:9.2e} {str(r['converged']):>5}")
    print()

    # RESOLUTION receipt (P7 / Y4)
    print("## P7 — resolution receipt, lambda = 1")
    res_rows = run_resolution(k=K_FROZEN)
    for r in res_rows:
        print(f"   N={r['N']:>3}  c = {r['c']:.6f}   c_D = {r['c_D']:.6f}   maxA = {r['max_A']:.4f}   V_res = {r['V_resid']:.2e}   conv = {r['converged']}")
    print()

    # DISCRIMINATION probe (P8 / Z3)
    print("## P8 — four-coefficient discrimination PROBE (k = 1/2 is FORBIDDEN as a proposal, §12.2)")
    k_rows = run_k_probe()
    print(f"   {'k':>9} {'2k/g':>9} {'c':>9} {'c_D':>9} {'k_meas':>9} {'Delta_clk':>10}")
    for r in k_rows:
        print(f"   {r['k']:9.6f} {2*r['k']/G_SELF:9.6f} {r['c']:9.6f} {r['c_D']:9.6f} {r['k_meas']:9.6f} {r['Delta_clock']:10.6f}")
    print()

    # P10
    print("## P10 — observables that could respond to the weight other than through the install")
    p10 = run_p10(k_rows)
    for name in P10_OBSERVABLES:
        print(f"   - {name}")
    print("   max relative spread across the four installed k, each normalised by its own Sum T00_src:")
    for key, val in p10["max_rel_spread"].items():
        print(f"     {key:>20} : {val:.3e}")
    print()

    verdict = evaluate_bins(famA=famA, famB=famB, res_rows=res_rows, k_rows=k_rows, adj=adj)

    print("## Z-GATE SUITE (step 1, overriding)")
    for key in ("Z1", "Z2", "Z3", "Z4", "Z5", "Z6"):
        v = verdict["Z"][key]
        print(f"   {key}: {'FIRES' if v['fires'] else 'clear'}   {  {kk: vv for kk, vv in v.items() if kk != 'fires'} }")
    print("   Z1 DIAGNOSTIC (flagged, NOT part of the gate, NOT an input to any bin):")
    z1d = z1_diagnostics(ctrl=ctrl, famA=famA, famB=famB)
    for name, v in z1d.items():
        print(f"     {name:>22}: frozen detector max dev = {v['frozen_detector_max_dev']:.3e}"
              f"   |   unweighted-mean variant max dev = {v['unweighted_variant_max_dev']:.3e}")
    print()
    print("## Y-GATE SUITE (step 2, overriding)")
    for key in ("Y1", "Y2", "Y3", "Y4"):
        v = verdict["Y"][key]
        print(f"   {key}: {'FIRES' if v['fires'] else 'clear'}   {  {kk: vv for kk, vv in v.items() if kk != 'fires'} }")
    print()
    print("## SELECTING CLAUSES (evaluated for the record; NOT reached if Z or Y fired)")
    print(f"   A1 k_meas in [{A1_LO}, {A1_HI}] at every rung : {verdict['A']['A1']}   (measured range {verdict['A']['k_meas_range'][0]:.6f} .. {verdict['A']['k_meas_range'][1]:.6f})")
    print(f"   A2 c inside the §5.3 bracket at every rung    : {verdict['A']['A2']}")
    print(f"   A3 |c_D/((2k/g)*chi) - 1| <= 1e-3             : {verdict['A']['A3']}   (dev {verdict['A']['A3_dev_min']:.3e} .. {verdict['A']['A3_dev_max']:.3e})")
    print(f"   A4 V_resid <= 1e-6 at every rung              : {verdict['A']['A4']}")
    print()
    print("=" * 78)
    print(f"  BIN {verdict['BIN']} — {verdict['why']}")
    print(f"  eta_mixed CONTROL (shipped quadratic) = {eta_ctrl:+.6f}")
    print(f"  eta_mixed FROZEN  (ponderomotive 1/7) = {eta_frozen:+.6f}")
    if not verdict["interpretable"]:
        print("  ^^ UNINTERPRETABLE per §10.2 — an overriding bin fired; nothing is banked.")
    print("=" * 78)

    if args.json:
        rec = {
            "eta_control": eta_ctrl, "eta_frozen": eta_frozen,
            "control": _strip(ctrl), "famA": _strip(famA), "famB": _strip(famB),
            "resolution": _strip(res_rows), "k_probe": _strip(k_rows),
            "p10": p10, "verdict": verdict, "z1_diagnostic": z1_diagnostics(ctrl=ctrl, famA=famA, famB=famB),
            "frozen": {"k": K_FROZEN, "g_self": G_SELF, "N": N_BASE, "S_min": S_MIN},
            "elapsed_s": time.time() - t0,
        }
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(rec, fh, indent=1, default=float)
        print(f"# wrote {args.json}")
    print(f"# elapsed {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
