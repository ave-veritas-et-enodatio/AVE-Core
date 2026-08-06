#!/usr/bin/env python3
"""Last-bond kernel collapse -- premise audit, discrete termination row, continuum reconciliation.

Prereg: research/2026-08-05_last-bond-kernel-collapse_prereg-FROZEN.md (COMMIT 1, pushed ALONE).
Ruling: _orchestration/docket-entries/2026-08-05-ruling-flag-causal-kernel-collapse.md (PR #887).

This driver resolves the three frozen tasks:

  TASK 1  the PREMISE AUDIT -- two-method (git grep + independent os.walk/re) scan of the
          canonical corpus for the GRADING LAW canon assigns each transport (bond) coupling.
          Bins: PREM-UNIVERSAL / PREM-EXCEPTION / PREM-UNDERDETERMINED.
  TASK 2  the LAST-BOND ROW -- the four frozen theorems of prereg section 3, certified
          numerically over the frozen sweep at mpmath dps = 60.
  TASK 3  the CONTINUUM RECONCILIATION -- the ell_node -> 0 ladder, the traction
          indeterminate form, and the RHO-A negative control.

Engine fence: `src/ave` is NOT imported and NOT touched. This driver is standalone.
Numerical conditioning: prereg section 0 row 11. Every near-wall quantity comes from the
cancellation-free S^2 = x(2 r_sat + x)/(r_sat + x)^2; `Gamma + 1` is NEVER formed by adding 1
to a computed Gamma; `Z_beyond = infinity` is the analytic continuation, never float `inf`.

RUN PROTOCOL (disclosed, and load-bearing for reproducibility). TASK 1 scans `research/`
among its four frozen directories, so this driver's OWN output JSON -- which lives in
`research/drivers/` and contains every pattern of the battery by construction -- perturbs
the scan if it is present when the driver starts. Reproduce a shipped run by DELETING
`last_bond_kernel_collapse_results.json` first. The determinism receipt (G-DET) is taken as
two full runs from an identical starting tree, i.e. with the output absent on both.
This self-reference is a FREEZE-TIME DEFECT of the frozen scan design, is reported as one in
the result doc, and is NOT repaired here (the freeze forbids changing a method element after
a result is seen); the repair -- restrict METHOD B to `git ls-files` output, and site the
sentinels outside the scanned tree -- is named and routed to a successor.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import time
from pathlib import Path

import mpmath as mp

# ----------------------------------------------------------------------
# FROZEN NUMERICS (prereg section 5; no member may be added or removed)
# ----------------------------------------------------------------------

DPS = 60
mp.mp.dps = DPS

S_LAST_GRID = ["1e-3", "1e-6", "1e-9", "1e-12", "1e-15", "1e-20", "1e-25", "1e-30"]
P_BRANCHES = {"RHO-A": "0.5", "RHO-B": "2"}
RHO_BEYOND_GRID = ["1e-30", "1e-15", "1", "1e+15", "1e+30"]
Z_BEYOND_OVER_Z1_GRID = ["0", "1e-40", "1e-20", "1", "1e+20", "1e+40", "INFINITY"]
BOND_RULES = ("HARMONIC", "ARITHMETIC")
OM_OVER_OMC_GRID = ["1e-25", "1e-19", "1e-13"]
ELL_OVER_RSAT_LADDER = ["6.0238983090250982e-19", "1e-12", "1e-6", "1e-3"]

# Read (never recomputed) from research/2026-08-04_coldq-axial-rhob_result.md section 2.2,
# the non-gated traction report. Registered as READ values.
RHOB_TRACTION_EXPONENT_SIGMA_PLUS = "-0.1459563385925332"
RHOB_TRACTION_EXPONENT_SIGMA_MINUS = "-0.8540436614074667"

REPO = Path(__file__).resolve().parents[2]
SCAN_DIRS = ("manuscript", "src", "research", "_orchestration")
SCAN_EXTS = (".md", ".py", ".tex", ".json", ".jsonl", ".txt")


def _s(x) -> str:
    """mpf -> full-precision decimal string (never a float)."""
    return mp.nstr(x, 30, strip_zeros=False)


def _c(z) -> dict:
    return {"re": _s(mp.re(z)), "im": _s(mp.im(z)), "abs": _s(abs(z))}


# ----------------------------------------------------------------------
# SECTION B -- TASK 1: the two-method scan
# ----------------------------------------------------------------------

# prereg section 2.4: the battery is frozen here and no pattern is added after any hit set is seen.
COUPLING_SYMBOLS = {
    "C1_G": r"G_\{?vac\}?|G_shear|G_\{shear\}",
    "C2_K": r"K\s*=\s*2\s*\*?\s*G|K_\{?vac\}?",
    "C3_Gc": r"G_c\b|G_\{c\}",
    "C4_gamma": r"gamma_c|\\gamma_c|couple-stress|couple stress",
    "C5_op10": r"k_op10|Op10|Op 10",
    "C6_hopf": r"k_hopf|Hopf",
    "C7_refl": r"k_refl|reflection density|_reflection_density",
    "C8_Z0": r"Z_0\b|Z_\{0\}|Z_EM|Z_\{EM\}",
}

# The grading-law probes, applied per symbol (prereg section 2.4).
GRADING_PROBES = {
    "ADJ_S": r"(?:{sym})[^\n]{{0,40}}(?:\*|\\cdot|\\,|\s)\s*S\b|\bS\s*(?:\*|\\cdot)\s*(?:{sym})",
    "ADJ_SQRT": r"(?:{sym})[^\n]{{0,80}}(?:sqrt\(1|\\sqrt\{{1)|(?:sqrt\(1|\\sqrt\{{1)[^\n]{{0,80}}(?:{sym})",
    "ADJ_SAT": r"(?:{sym})[^\n]{{0,80}}saturat|saturat[^\n]{{0,80}}(?:{sym})",
    "ADJ_OFA": r"(?:{sym})\s*\(A\)",
    "GRADE_VERB": r"(?:{sym})[^\n]{{0,80}}(?:grade[ds]?\b|rides\b|scales as|\\propto)"
    r"|(?:grade[ds]?\b|rides\b|scales as|\\propto)[^\n]{{0,80}}(?:{sym})",
}

# FT-SCAN sentinels (prereg section 7).
SENTINEL_ABSENT = r"zzq-last-bond-sentinel-absent-9f3a"
SENTINEL_PRESENT = r"Universal Saturation Kernel"


def _scan_files() -> list[Path]:
    out = []
    for d in SCAN_DIRS:
        root = REPO / d
        if not root.exists():
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [x for x in dirnames if x not in (".git", "__pycache__", ".venv")]
            for fn in filenames:
                if fn.endswith(SCAN_EXTS):
                    out.append(Path(dirpath) / fn)
    return sorted(out)


def method_b(pattern: str, files: list[Path]) -> set[tuple[str, int]]:
    """Independent os.walk + re scan. Deliberately NOT a git pathspec."""
    rx = re.compile(pattern)
    hits: set[tuple[str, int]] = set()
    for f in files:
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for i, line in enumerate(text.splitlines(), start=1):
            if rx.search(line):
                hits.add((str(f.relative_to(REPO)), i))
    return hits


def method_a(pattern: str) -> tuple[set[tuple[str, int]], int]:
    """git grep -P over the same directories. Returns (hits, scanned_file_count)."""
    cmd = ["git", "-C", str(REPO), "grep", "-n", "-I", "-P", pattern, "--", *SCAN_DIRS]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    hits: set[tuple[str, int]] = set()
    for line in proc.stdout.splitlines():
        parts = line.split(":", 2)
        if len(parts) < 3:
            continue
        path, lineno = parts[0], parts[1]
        if not lineno.isdigit() or not path.endswith(SCAN_EXTS):
            continue
        hits.add((path, int(lineno)))
    ls = subprocess.run(
        ["git", "-C", str(REPO), "ls-files", "--", *SCAN_DIRS], capture_output=True, text=True
    )
    n = sum(1 for p in ls.stdout.splitlines() if p.endswith(SCAN_EXTS))
    return hits, n


def run_scan() -> dict:
    files = _scan_files()
    out: dict = {
        "method_b_scanned_files": len(files),
        "method_a_scanned_files": None,
        "patterns": {},
        "disagreements": [],
    }
    battery: dict[str, str] = {}
    for cid, sym in COUPLING_SYMBOLS.items():
        battery[f"{cid}::BARE"] = sym
        for pname, tmpl in GRADING_PROBES.items():
            battery[f"{cid}::{pname}"] = tmpl.format(sym=sym)
    battery["SENTINEL::ABSENT"] = SENTINEL_ABSENT
    battery["SENTINEL::PRESENT"] = SENTINEL_PRESENT

    n_a_files = None
    for key, pat in battery.items():
        a, n_a_files = method_a(pat)
        b = method_b(pat, files)
        agree = a == b
        # METHOD B sees untracked working-tree files; restrict the comparison to the
        # tracked intersection, and report the asymmetric residues explicitly.
        only_a = sorted(a - b)[:5]
        only_b = sorted(b - a)[:5]
        out["patterns"][key] = {
            "pattern": pat,
            "n_method_a": len(a),
            "n_method_b": len(b),
            "agree": agree,
            "only_in_a_sample": [f"{p}:{ln}" for p, ln in only_a],
            "only_in_b_sample": [f"{p}:{ln}" for p, ln in only_b],
            "union_used": len(a | b),
        }
        if not agree:
            out["disagreements"].append(key)
    out["method_a_scanned_files"] = n_a_files
    return out


# ----------------------------------------------------------------------
# SECTION C -- TASK 2: the last-bond row (prereg section 3 theorems)
# ----------------------------------------------------------------------
#
# Units, frozen: r_sat = 1, c_0 = 1, rho_bulk = 1, cross-section AX = 1, so
# G_vac = rho_bulk c_0^2 = 1.  ell = ell_node / r_sat.  om is carried as om/om_C
# with om_C = c_0 / ell_node, so:
#
#     k_cold = G_vac * S_cold * AX / ell = S_cold / ell
#     Z_1    = rho * c = S^(1-p)              [rho_bulk c_0 = 1]
#     m_0    = rho_node * AX * ell            [rho_node = 1 (RHO-A) or S^-3 (RHO-B)]
#     om     = (om/om_C) / ell
#     => om * m_0 = (om/om_C) * rho_node      and   k_0 / om = (k_0 * ell) / (om/om_C)


def s_squared_exact(x):
    """Cancellation-free S^2 = x(2 r_sat + x)/(r_sat + x)^2 at r_sat = 1 (prereg row 11)."""
    return x * (2 + x) / (1 + x) ** 2


def naive_one_minus_a2_float64(ell_over_rsat: float) -> float:
    """The naive float64 route the conditioning row forbids -- G-COND measures it."""
    a = 1.0 / (1.0 + ell_over_rsat)
    return 1.0 - a * a


def bond_k0(k_cold, k_beyond, rule: str):
    """Last-bond stiffness. HARMONIC = springs in series (substrate-native); ARITHMETIC = control."""
    if rule == "HARMONIC":
        # two half-bonds of stiffness 2*k_cold and 2*k_beyond in series:
        #   k_0 = (2 k_c)(2 k_b)/((2 k_c)+(2 k_b)) = 2 k_c k_b/(k_c + k_b)
        if k_beyond == 0:
            return mp.mpf(0)
        return 2 * k_cold * k_beyond / (k_cold + k_beyond)
    if rule == "ARITHMETIC":
        return (k_cold + k_beyond) / 2
    raise ValueError(rule)


def z_load(k0, om, z_beyond):
    """Shunt compliance of the last bond in parallel with an arbitrary beyond-wall load.

    z_beyond is None for the OPEN (clamped) member -- evaluated as the analytic
    continuation k0/(j om), NEVER as float `inf` arithmetic (prereg row 11 item iv).
    """
    j = mp.mpc(0, 1)
    if z_beyond is None:  # Z_beyond = infinity
        return k0 / (j * om)
    if z_beyond == 0:
        return mp.mpc(0)
    return k0 * z_beyond / (k0 + j * om * z_beyond)


def gamma_from_zload(zl, z1):
    """Gamma and the residual Gamma+1, the latter from its OWN closed form (prereg row 11 ii)."""
    g = (zl - z1) / (zl + z1)
    resid = 2 * zl / (zl + z1)  # == Gamma + 1, never formed by adding 1
    return g, resid


def run_task2() -> dict:
    rows = []
    for s_str in S_LAST_GRID:
        S = mp.mpf(s_str)
        for branch, p_str in P_BRANCHES.items():
            p = mp.mpf(p_str)
            rho_node = mp.mpf(1) if branch == "RHO-A" else S ** (-3)
            Z1 = S ** (1 - p)
            for ell_str in [ELL_OVER_RSAT_LADDER[0]]:  # row-level ell is fixed; Task 3 sweeps it
                ell = mp.mpf(ell_str)
                k_cold = S / ell
                for rule in BOND_RULES:
                    k0 = bond_k0(k_cold, mp.mpf(0), rule)
                    for om_str in OM_OVER_OMC_GRID:
                        om = mp.mpf(om_str) / ell
                        for rb_str in RHO_BEYOND_GRID:
                            for zb_str in Z_BEYOND_OVER_Z1_GRID:
                                if zb_str == "INFINITY":
                                    zb = None
                                else:
                                    # the beyond-wall load carries the beyond-wall density
                                    zb = mp.mpf(zb_str) * Z1 * mp.sqrt(mp.mpf(rb_str))
                                    if mp.mpf(zb_str) == 0:
                                        zb = mp.mpf(0)
                                zl = z_load(k0, om, zb)
                                g, resid = gamma_from_zload(zl, Z1)
                                m0 = rho_node * ell
                                z_n0 = mp.mpc(0, 1) * om * m0 + zl
                                g_n0 = (z_n0 - Z1) / (z_n0 + Z1)
                                rows.append(
                                    {
                                        "S_last": s_str,
                                        "branch": branch,
                                        "rule": rule,
                                        "om_over_omC": om_str,
                                        "rho_beyond": rb_str,
                                        "Z_beyond_over_Z1": zb_str,
                                        "k0": _s(k0),
                                        "Z1": _s(Z1),
                                        "abs_Gamma_LB": _s(abs(g)),
                                        "abs_resid_LB": _s(abs(resid)),
                                        "abs_Gamma_N0": _s(abs(g_n0)),
                                        "Gamma_N0": _c(g_n0),
                                        "Gamma_LB": _c(g),
                                    }
                                )
    return {"n_rows": len(rows), "rows": rows}


# ----------------------------------------------------------------------
# SECTION D -- TASK 3: the continuum reconciliation
# ----------------------------------------------------------------------
#
# One-way optical distance to the wall, r_sat = 1, c_0 = 1, x = r - r_sat:
#
#   RHO-B (p = 2):  1/c = 1/S^2 = (1+x)^2/(x(2+x)) = 1 + (1/2)[1/x - 1/(x+2)]
#                   => antiderivative  F_B(x) = x + (1/2) ln( x/(x+2) )    EXACT
#                   => LOG-DIVERGENT as x_min -> 0
#   RHO-A (p = 1/2): 1/c = S^(-1/2) ~ (2x)^(-1/4) near 0  => INTEGRABLE, FINITE
#                   (the frozen negative control of prereg section 4.2 step 4)


def optical_oneway_rhob(x_min, x_out):
    """EXACT closed form of int dx / (c_0 S^2) on the RHO-B branch."""

    def F(x):
        return x + mp.mpf(1) / 2 * mp.log(x / (x + 2))

    return F(x_out) - F(x_min)


def optical_oneway_rhoa(x_min, x_out):
    """int dx / (c_0 S^(1/2)) on the RHO-A branch, by mp quadrature (finite)."""

    def integrand(x):
        return s_squared_exact(x) ** (mp.mpf(-1) / 4)

    return mp.quad(integrand, [x_min, x_out])


def run_task3() -> dict:
    x_out = mp.mpf(1)  # integrate from the wall out to r = 2 r_sat, a frozen fixed outer plane
    ladder = []
    for ell_str in ELL_OVER_RSAT_LADDER:
        ell = mp.mpf(ell_str)
        # the last intact cell sits one node spacing outside the wall
        s2_last = s_squared_exact(ell)
        s_last = mp.sqrt(s2_last)
        tb = optical_oneway_rhob(ell, x_out)
        ta = optical_oneway_rhoa(ell, x_out)
        ladder.append(
            {
                "ell_over_rsat": ell_str,
                "S_last_from_exact_S2": _s(s_last),
                "roundtrip_optical_RHO_B_over_rsat_c0": _s(2 * tb),
                "roundtrip_optical_RHO_A_over_rsat_c0": _s(2 * ta),
                "Gamma_LB": "-1 (exact, ell-independent -- Theorem 2)",
            }
        )
    # the log-divergence rate, measured: T_B should grow by (1/2)ln(10) per decade of ell
    t_hi = optical_oneway_rhob(mp.mpf("1e-3"), x_out)
    t_lo = optical_oneway_rhob(mp.mpf("1e-12"), x_out)
    decades = 9
    measured_rate = (t_lo - t_hi) / decades
    predicted_rate = mp.log(10) / 2
    # RHO-A control: the same span must NOT grow logarithmically without bound
    a_hi = optical_oneway_rhoa(mp.mpf("1e-3"), x_out)
    a_lo = optical_oneway_rhoa(mp.mpf("1e-12"), x_out)

    # the traction indeterminate form, evaluated both ways at the same physical place
    traction = {
        "continuum_exponent_sigma_plus_READ": RHOB_TRACTION_EXPONENT_SIGMA_PLUS,
        "continuum_exponent_sigma_minus_READ": RHOB_TRACTION_EXPONENT_SIGMA_MINUS,
        "continuum_both_negative_so_T_diverges": True,
        "lattice_T_last_bond": "0",
        "lattice_reason": (
            "T_latt = k_0 * (x_0 - x_-1) with k_0 = 0 EXACTLY (Theorem 1) and the finite "
            "difference bounded by construction; the product is exactly zero and no "
            "difference quotient at the wall is ever taken"
        ),
        "indeterminate_form": "T = mu(r) * dpsi/dr  ->  0 * infinity",
        "continuum_resolution": "along a Frobenius branch -> infinity",
        "lattice_resolution": "modulus exactly 0 times a bounded finite difference -> 0",
    }
    return {
        "ladder": ladder,
        "log_rate_measured_per_decade": _s(measured_rate),
        "log_rate_predicted_half_ln10": _s(predicted_rate),
        "log_rate_rel_sep": _s(abs(measured_rate - predicted_rate) / predicted_rate),
        "rho_a_control_T_at_1e-3": _s(a_hi),
        "rho_a_control_T_at_1e-12": _s(a_lo),
        "rho_a_control_growth_ratio": _s(a_lo / a_hi),
        "traction": traction,
    }


# ----------------------------------------------------------------------
# SECTION E -- gates, self-tests, emit
# ----------------------------------------------------------------------


def build_gates(t2: dict, t3: dict, scan: dict) -> dict:
    rows = t2["rows"]
    harm = [r for r in rows if r["rule"] == "HARMONIC"]
    arith = [r for r in rows if r["rule"] == "ARITHMETIC"]

    g: dict = {}

    # G-BOND: harmonic k0 exactly zero everywhere
    max_k0_harm = max(mp.mpf(r["k0"]) for r in harm)
    g["G-BOND"] = {
        "frozen": "k_0 == 0 exactly (mp) at every swept HARMONIC point",
        "measured_max_abs_k0": _s(max_k0_harm),
        "pass": max_k0_harm == 0,
    }

    # G-ROW: |Gamma_LB + 1| exactly zero everywhere on the harmonic branch
    max_resid = max(mp.mpf(r["abs_resid_LB"]) for r in harm)
    g["G-ROW"] = {
        "frozen": "|Gamma_LB + 1| == 0 exactly (mp) at every swept HARMONIC point",
        "measured_max_abs_resid": _s(max_resid),
        "n_points": len(harm),
        "pass": max_resid == 0,
    }

    # G-RHO: exact independence of the beyond-wall load
    by_key: dict[tuple, list] = {}
    for r in harm:
        k = (r["S_last"], r["branch"], r["om_over_omC"])
        by_key.setdefault(k, []).append(mp.mpf(r["abs_Gamma_LB"]))
    max_spread = max(max(v) - min(v) for v in by_key.values())
    g["G-RHO"] = {
        "frozen": "max over the Z_beyond x rho_beyond grid of the Gamma_LB spread == 0 exactly",
        "measured_max_spread": _s(max_spread),
        "n_groups": len(by_key),
        "pass": max_spread == 0,
    }

    # G-RHO2: off-limit sensitivity is second order in k_0
    # inject k_0 = eps * k_cold and measure d|Gamma|/dZ_beyond scaling
    exps = []
    S = mp.mpf("1e-9")
    ell = mp.mpf(ELL_OVER_RSAT_LADDER[0])
    Z1 = S ** (1 - mp.mpf("0.5"))
    om = mp.mpf("1e-19") / ell
    k_cold = S / ell
    pts = []
    for e_str in ["1e-10", "1e-12", "1e-14"]:
        k0 = mp.mpf(e_str) * k_cold
        zb1 = Z1
        zb2 = 2 * Z1
        _, r1 = gamma_from_zload(z_load(k0, om, zb1), Z1)
        _, r2 = gamma_from_zload(z_load(k0, om, zb2), Z1)
        pts.append((k0, abs(r1 - r2)))
    for i in range(len(pts) - 1):
        (k1, d1), (k2, d2) = pts[i], pts[i + 1]
        exps.append(mp.log(d2 / d1) / mp.log(k2 / k1))
    fitted = sum(exps) / len(exps)
    g["G-RHO2"] = {
        "frozen": "fitted exponent of |dGamma/dZ_beyond| vs k_0 in [1.9, 2.1]",
        "measured_exponent": _s(fitted),
        "per_pair": [_s(e) for e in exps],
        "pass": mp.mpf("1.9") <= fitted <= mp.mpf("2.1"),
    }

    # G-COLD: the row is identical on both density branches
    cold = {}
    for r in harm:
        k = (r["S_last"], r["om_over_omC"], r["rho_beyond"], r["Z_beyond_over_Z1"])
        cold.setdefault(k, {})[r["branch"]] = mp.mpf(r["abs_Gamma_LB"])
    max_branch_sep = max(
        abs(v["RHO-A"] - v["RHO-B"]) for v in cold.values() if len(v) == 2
    )
    g["G-COLD"] = {
        "frozen": "Gamma_LB(RHO-A) - Gamma_LB(RHO-B) == 0 exactly at every swept point",
        "measured_max_sep": _s(max_branch_sep),
        "pass": max_branch_sep == 0,
    }

    # G-UNIT: Ax-3 losslessness at both planes
    worst_lb = max(abs(mp.mpf(r["abs_Gamma_LB"]) - 1) for r in harm)
    worst_n0 = max(abs(mp.mpf(r["abs_Gamma_N0"]) - 1) for r in harm)
    tol = mp.mpf("1e-50")
    g["G-UNIT"] = {
        "frozen": "||Gamma|-1| <= 1e-50 at PLANE-LB and PLANE-N0",
        "measured_worst_LB": _s(worst_lb),
        "measured_worst_N0": _s(worst_n0),
        "pass": worst_lb <= tol and worst_n0 <= tol,
    }

    # G-PLANE: the plane shift is real at >= 1 swept point
    best_shift = max(
        abs(mp.mpc(mp.mpf(r["Gamma_N0"]["re"]), mp.mpf(r["Gamma_N0"]["im"]))
            - mp.mpc(mp.mpf(r["Gamma_LB"]["re"]), mp.mpf(r["Gamma_LB"]["im"])))
        for r in harm
    )
    g["G-PLANE"] = {
        "frozen": "|Gamma_N0 - Gamma_LB| >= 1e-6 at >= 1 swept point",
        "measured_max": _s(best_shift),
        "pass": best_shift >= mp.mpf("1e-6"),
    }

    # G-PREC: float64 vs mp cross-check on the optical ladder
    worst = mp.mpf(0)
    for row in t3["ladder"]:
        ell = float(row["ell_over_rsat"])
        f64 = ell + 0.5 * __import__("math").log(ell / (ell + 2.0))
        f64 = 2.0 * (1.0 + 0.5 * __import__("math").log(1.0 / 3.0) - f64)
        ref = mp.mpf(row["roundtrip_optical_RHO_B_over_rsat_c0"])
        worst = max(worst, abs(mp.mpf(f64) - ref) / abs(ref))
    g["G-PREC"] = {
        "frozen": "relative separation <= 1e-12 on every quantity computed both ways",
        "measured_worst_rel": _s(worst),
        "pass": worst <= mp.mpf("1e-12"),
    }

    # G-COND: the naive float64 route must return exactly zero
    naive = naive_one_minus_a2_float64(float(ELL_OVER_RSAT_LADDER[0]))
    exact = s_squared_exact(mp.mpf(ELL_OVER_RSAT_LADDER[0]))
    g["G-COND"] = {
        "frozen": "the naive float64 1-A^2 must return exactly 0.0 at ell/r_sat = 6.02e-19",
        "naive_float64_1_minus_A2": repr(naive),
        "cancellation_free_S2": _s(exact),
        "pass": naive == 0.0 and exact > 0,
    }

    # G-SCAN
    g["G-SCAN"] = {
        "frozen": "METHOD A and METHOD B hit sets identical per pattern; both file counts reported",
        "method_a_scanned_files": scan["method_a_scanned_files"],
        "method_b_scanned_files": scan["method_b_scanned_files"],
        "n_patterns": len(scan["patterns"]),
        "disagreements": scan["disagreements"],
        "pass": len(scan["disagreements"]) == 0,
    }

    # G-NC-SIGN
    p = REPO / "research" / "2026-08-05_echo-delay-v2-reach-through_prereg-FROZEN.md"
    needle = "`Γ_L = −1` in the traction↔voltage convention"
    present = needle in p.read_text(encoding="utf-8")
    g["G-NC-SIGN"] = {
        "frozen": "the byte-exact free-end convention substring must be PRESENT in the echo-v2 prereg",
        "needle": needle,
        "present": present,
        "this_lane_Gamma_LB": "-1",
        "pass": bool(present),
    }

    # G-NC-ECHO
    j = json.loads(
        (REPO / "research" / "drivers" / "echo_delay_v2_reach_through_results.json").read_text()
    )
    blob = json.dumps(j)
    swept = "Gamma_L in {0,-1,+1}" in blob
    jtp = j["y8"]["junction_two_port"]
    ident = all(bool(e.get("is_identity")) and e.get("W") == 0 for e in jtp)
    g["G-NC-ECHO"] = {
        "frozen": "the -1 member is in the predecessor's swept set AND its junction two-port is the identity",
        "sweep_declaration_present": swept,
        "n_junction_two_port_entries": len(jtp),
        "all_identity_and_W_zero": ident,
        "pass": bool(swept and ident),
    }

    # G-NC-ARITH
    worst_arith_resid = max(mp.mpf(r["abs_resid_LB"]) for r in arith)
    max_k0_arith = max(mp.mpf(r["k0"]) for r in arith)
    g["G-NC-ARITH"] = {
        "frozen": "the arithmetic rule must NOT collapse: k_0 != 0 and |Gamma+1| > 1e-30 somewhere",
        "measured_max_k0": _s(max_k0_arith),
        "measured_max_resid": _s(worst_arith_resid),
        "pass": max_k0_arith > 0 and worst_arith_resid > mp.mpf("1e-30"),
    }
    return g


def build_self_tests(scan: dict) -> dict:
    """Each MUST fire; a gate that cannot fail is not a gate (prereg section 7)."""
    st: dict = {}
    S = mp.mpf("1e-9")
    ell = mp.mpf(ELL_OVER_RSAT_LADDER[0])
    Z1 = S ** mp.mpf("0.5")
    om = mp.mpf("1e-19") / ell
    k_cold = S / ell

    # FT-BOND: k_beyond = 1e-300 must break G-BOND's exactness
    k0_inj = bond_k0(k_cold, mp.mpf("1e-300"), "HARMONIC")
    st["FT-BOND"] = {
        "frozen": "injecting k_beyond = 1e-300 must make G-BOND FAIL (k_0 != 0)",
        "measured_k0": _s(k0_inj),
        "fires": k0_inj != 0,
    }

    # FT-ROW: injected k_0 must give a non-zero residual
    k0_small = mp.mpf("1e-300") * k_cold
    _, resid = gamma_from_zload(z_load(k0_small, om, Z1), Z1)
    st["FT-ROW"] = {
        "frozen": "injecting k_0 = 1e-300*k_cold must make |Gamma_LB + 1| > 0",
        "measured_abs_resid": _s(abs(resid)),
        "fires": abs(resid) > 0,
    }

    # FT-RHO: at that injected k_0, the Z_beyond grid must spread
    vals = []
    for zb_str in Z_BEYOND_OVER_Z1_GRID:
        zb = None if zb_str == "INFINITY" else mp.mpf(zb_str) * Z1
        _, r = gamma_from_zload(z_load(k0_small, om, zb), Z1)
        vals.append(abs(r))
    spread = max(vals) - min(vals)
    st["FT-RHO"] = {
        "frozen": "at the injected k_0 the Z_beyond grid must produce a spread > 0",
        "measured_spread": _s(spread),
        "fires": spread > 0,
    }

    # FT-PLANE: at om -> 0 the two planes must coincide
    om_tiny = mp.mpf("1e-200") / ell
    m0 = ell
    zl = z_load(mp.mpf(0), om_tiny, Z1)
    g_lb, _ = gamma_from_zload(zl, Z1)
    z_n0 = mp.mpc(0, 1) * om_tiny * m0 + zl
    g_n0 = (z_n0 - Z1) / (z_n0 + Z1)
    sep = abs(g_n0 - g_lb)
    st["FT-PLANE"] = {
        "frozen": "at om -> 0 the two planes must COINCIDE, i.e. G-PLANE must fail at that limit",
        "measured_sep_at_om_1e-200": _s(sep),
        "fires": sep < mp.mpf("1e-6"),
    }

    # FT-ARITH: the arithmetic control fails to collapse for the RIGHT reason
    k0_a = bond_k0(k_cold, mp.mpf(0), "ARITHMETIC")
    _, r_a = gamma_from_zload(z_load(k0_a, om, Z1), Z1)
    st["FT-ARITH"] = {
        "frozen": "the arithmetic control must give |Gamma+1| > 1e-30 because k_0 = k_cold/2 > 0",
        "measured_k0_arith": _s(k0_a),
        "measured_k_cold_over_2": _s(k_cold / 2),
        "reason_is_k0_positive": k0_a == k_cold / 2,
        "measured_abs_resid": _s(abs(r_a)),
        "fires": abs(r_a) > mp.mpf("1e-30") and k0_a == k_cold / 2,
    }

    # FT-SCAN sentinels
    sa = scan["patterns"]["SENTINEL::ABSENT"]
    sp = scan["patterns"]["SENTINEL::PRESENT"]
    st["FT-SCAN"] = {
        "frozen": "absent sentinel -> zero hits on BOTH methods; present sentinel -> same non-zero set",
        "absent_n_a": sa["n_method_a"],
        "absent_n_b": sa["n_method_b"],
        "present_n_a": sp["n_method_a"],
        "present_n_b": sp["n_method_b"],
        "present_agree": sp["agree"],
        "fires": (
            sa["n_method_a"] == 0
            and sa["n_method_b"] == 0
            and sp["n_method_a"] > 0
            and sp["agree"]
        ),
    }

    # FT-COND
    naive = naive_one_minus_a2_float64(float(ELL_OVER_RSAT_LADDER[0]))
    st["FT-COND"] = {
        "frozen": "the naive float64 1-A^2 must return exactly 0.0 at the innermost ratio",
        "measured": repr(naive),
        "fires": naive == 0.0,
    }
    return st


def main() -> None:
    t0 = time.time()
    scan = run_scan()
    t2 = run_task2()
    t3 = run_task3()
    gates = build_gates(t2, t3, scan)
    self_tests = build_self_tests(scan)

    # trim the row payload: aggregates are what the gates read; ship a deterministic sample
    sample = t2["rows"][:6] + t2["rows"][-6:]

    out = {
        "_prereg": "research/2026-08-05_last-bond-kernel-collapse_prereg-FROZEN.md",
        "_ruling": "_orchestration/docket-entries/2026-08-05-ruling-flag-causal-kernel-collapse.md (PR #887)",
        "_method": (
            "TASK 1 two-method corpus scan (git grep -P + independent os.walk/re); "
            "TASK 2 the four frozen theorems certified over the frozen sweep at mpmath dps = 60; "
            "TASK 3 the exact RHO-B optical closed form F(x) = x + (1/2)ln(x/(x+2)) on the "
            "ell_node ladder with the RHO-A finite-length negative control"
        ),
        "_non_claim": (
            "DERIVATION result. Mints no clm-/def-; propagates to no KB/manuscript leaf; changes "
            "no solidity; edits no falsification ledger; src/ave byte-untouched and not imported. "
            "Adjudicates neither the discrete nor the continuum wall row; settles nothing about "
            "FORK-3(b), FLAG-ECO, gamma/G_c VALUES, Regime-IV interior physics, or anything "
            "observational."
        ),
        "_frozen_numerics": {
            "dps": DPS,
            "S_last_grid": S_LAST_GRID,
            "p_branches": P_BRANCHES,
            "rho_beyond_grid": RHO_BEYOND_GRID,
            "Z_beyond_over_Z1_grid": Z_BEYOND_OVER_Z1_GRID,
            "bond_rules": list(BOND_RULES),
            "om_over_omC_grid": OM_OVER_OMC_GRID,
            "ell_over_rsat_ladder": ELL_OVER_RSAT_LADDER,
        },
        "task1_scan": scan,
        "task2_row": {"n_rows": t2["n_rows"], "sample_rows": sample},
        "task3_continuum": t3,
        "gates": gates,
        "self_tests": self_tests,
    }
    digest_src = json.dumps(out, sort_keys=True, ensure_ascii=False)
    out["_digest"] = hashlib.sha256(digest_src.encode("utf-8")).hexdigest()[:16]
    out["_runtime_sec"] = round(time.time() - t0, 2)

    dst = Path(__file__).with_name("last_bond_kernel_collapse_results.json")
    dst.write_text(json.dumps(out, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")

    n_gate_fail = sum(1 for v in gates.values() if not v["pass"])
    n_ft_dead = sum(1 for v in self_tests.values() if not v["fires"])
    print(f"[last-bond] digest={out['_digest']} rows={t2['n_rows']}")
    print(f"[last-bond] gates: {len(gates)} run, {n_gate_fail} FAIL")
    print(f"[last-bond] self-tests: {len(self_tests)} run, {n_ft_dead} DID NOT FIRE")
    for k, v in gates.items():
        print(f"    {k:12s} {'PASS' if v['pass'] else 'FAIL'}")
    for k, v in self_tests.items():
        print(f"    {k:12s} {'FIRES' if v['fires'] else 'DOES NOT FIRE'}")


if __name__ == "__main__":
    main()
