#!/usr/bin/env python3
"""APPROACH-LEAK lane driver — shear->rotation conversion on the graded approach to r_sat.

Frozen pre-registration: research/2026-08-05_approach-leak_prereg-FROZEN.md
(commit bdb8b4a4, pushed ALONE before this file existed).

WHAT THIS COMPUTES
------------------
The rotational (Cosserat micro-rotation) branch is GAPPED at omega_m = 2*omega_C
in the cold medium (A-008-pinned; cosserat-mass-gap.md:59 + a008-factor-
propagation_note.md section 3.3).  The local gap rides the strain kernel with an
exponent p that canon does NOT state, so p is BRACKETED:

    omega_m(r) = 2 * omega_C * S(r)^p ,    p == (a + b) / 2

with `a` the (unstated) G_c(A) exponent and `b` the (unstated) I_omega(A)
exponent.  The lane asks whether the graded bias ever drives the local gap below
the certified ringdown drive band on lattice cells that PHYSICALLY EXIST.

Primary outputs, both frozen in prereg section 2:
    N_open  -- integer count of intact cells at which drive >= local gap
    zeta_max-- the evanescent leak bound |eps^A| / |A_macro| at the last cell
and the derived structural statement p_crit = 2 (prereg section 2.4).

DISCIPLINE
----------
* Engine `src/ave` is byte-untouched AND NEVER IMPORTED (prereg header).  The
  canonical base constants are therefore read from src/ave/core/constants.py by
  an `ast` literal parse -- canonical-source without an import -- and the parsed
  values are GATED against the canonical identities by G-CANON.  This is
  STRICTLY STRONGER than importing, because it also verifies the canonical
  file's own internal consistency.
* mpmath dps = 60 on every verdict path.  float64 appears only in the JSON echo
  of already-gated mp values and on the deliberate G-COND cancellation probe.
* No iterated map anywhere: every reported quantity is a closed form evaluated
  once.  Error model = round-off only (prereg row 11).
* Regex engines: METHOD A = `git grep -P` (PCRE, ASCII \\w);
  METHOD B = Python `re` on str (Unicode \\w).  NO pattern uses \\b.
"""

from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

from mpmath import mp

mp.dps = 60

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
OUT = Path(os.environ.get("APPROACH_LEAK_OUT", str(HERE / "approach_leak_results.json")))

V24_JSON = HERE / "coldq_pole_v2p4_root_results.json"
LASTBOND_JSON = HERE / "last_bond_kernel_collapse_results.json"
CONSTANTS_PY = REPO / "src" / "ave" / "core" / "constants.py"

# This lane's OWN artifacts, excluded from the scan surface BY CONSTRUCTION
# (prereg section 5.1; the pilot-5 G-SCAN self-reference repair).
OWN_ARTIFACTS = {
    "research/2026-08-05_approach-leak_prereg-FROZEN.md",
    "research/2026-08-05_approach-leak_result.md",
    "research/drivers/approach_leak.py",
    "research/drivers/approach_leak_number_check.py",
    "research/drivers/approach_leak_results.json",
    "_orchestration/docket-entries/2026-08-05-approach-leak.md",
}


def _s(x, n: int = 30) -> str:
    """Stable mp -> str rendering used for every shipped numeral."""
    return mp.nstr(x, n, strip_zeros=False)


def _pk(p) -> str:
    """Stable bracket-member key: 0.5, 1.0, 1.5, 2.0, 2.5, 3.0."""
    return mp.nstr(p, 3, strip_zeros=True)


# ---------------------------------------------------------------------------
# Canonical constants: ast literal parse of src/ave/core/constants.py.
# ---------------------------------------------------------------------------

def read_canonical_constants() -> dict[str, mp.mpf]:
    tree = ast.parse(CONSTANTS_PY.read_text(encoding="utf-8"))
    wanted = {"C_0", "HBAR", "M_SUN", "M_E", "G", "NU_VAC"}
    found: dict[str, object] = {}
    for node in tree.body:
        target = None
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            target = node.target.id
        elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            target = node.targets[0].id
        if target in wanted and target not in found and node.value is not None:
            try:
                found[target] = ast.literal_eval(node.value)
            except ValueError:
                # NU_VAC is `2.0 / 7.0`; evaluate that one exact binop in mp.
                if target == "NU_VAC":
                    found[target] = None
    missing = wanted - set(found)
    if missing:
        raise SystemExit(f"canonical constants not parsed: {sorted(missing)}")
    return {
        "C_0": mp.mpf(repr(found["C_0"])),
        "HBAR": mp.mpf(repr(found["HBAR"])),
        "M_SUN": mp.mpf(repr(found["M_SUN"])),
        "M_E": mp.mpf(repr(found["M_E"])),
        "G": mp.mpf(repr(found["G"])),
        "NU_VAC": mp.mpf(2) / mp.mpf(7),
    }


K = read_canonical_constants()
C0 = K["C_0"]
HBAR = K["HBAR"]
M_SUN = K["M_SUN"]
M_E = K["M_E"]
G_NEWTON = K["G"]
NU_VAC = K["NU_VAC"]

L_NODE = HBAR / (M_E * C0)          # canonical definition, constants.py:293
OMEGA_C = C0 / L_NODE               # canonical identity,   constants.py:305
X_SAT = mp.mpf(2) / NU_VAC          # r_sat = (2/nu_vac) GM/c^2 = 7 GM/c^2

# ---------------------------------------------------------------------------
# Frozen sweep (prereg section 4).  No member may be added or dropped.
# ---------------------------------------------------------------------------

MASSES = [mp.mpf(1), mp.mpf(10), mp.mpf(62), mp.mpf(100)]
M_REF = mp.mpf(62)
THETAS = [mp.mpf(1), mp.mpf("0.5")]
P_BRACKET = [mp.mpf("0.5"), mp.mpf(1), mp.mpf("1.5"), mp.mpf(2), mp.mpf("2.5"), mp.mpf(3)]
P_PROVENANCE = {
    "0.5": "(a=1,b=0) the DISPATCH's stated expectation, gap ~ sqrt(S_eps)",
    "1.0": "(a=2,b=0) the ENGINE's coded a (cosserat_field_3d.py:767 x :761) with I_omega ungraded",
    "1.5": "(a=3,b=0) or (a=0,b=3) -- filler member so the below-knife arm is not two-point",
    "2.0": "(a=1,b=3) dispatch's a with the RHO-B ANALOGY for I_omega -- ANALOGY, NOT CANON",
    "2.5": "(a=2,b=3) engine's a with the RHO-B ANALOGY for I_omega -- ANALOGY, NOT CANON",
    "3.0": "(a=3,b=3) loosest member so the above-knife arm is not single-point",
}
RHO_BRANCHES = ["RHO-A", "RHO-B"]
BETA_BRACKET = [mp.mpf("5.4414"), mp.mpf("17.0111")]
N_BAND = 65
P_CRIT = mp.mpf(2)

# The rotational band-top bracket (prereg section 2.7): REPORTED, none chosen.
ROT_TOP = {
    "T1_continuum_srs_nyquist": 2 * mp.sqrt(mp.pi**2 + 1),
    "T2_scalar_lower_bracket": mp.mpf("5.4414"),
    "T3_vector_upper_bracket": mp.mpf("17.0111"),
}


def r_sat(m_msun: mp.mpf) -> mp.mpf:
    return X_SAT * G_NEWTON * (m_msun * M_SUN) / C0**2


def S2_exact(x: mp.mpf, rs: mp.mpf) -> mp.mpf:
    """Cancellation-free S^2 = 1 - (r_sat/r)^2 with r = r_sat + x (prereg row 11)."""
    return x * (2 * rs + x) / (rs + x) ** 2


# ---------------------------------------------------------------------------
# The frozen band, read PROGRAMMATICALLY from the v2.4 shipped JSON.
# ---------------------------------------------------------------------------

def read_frozen_band() -> tuple[mp.mpf, mp.mpf, dict]:
    d = json.loads(V24_JSON.read_text(encoding="utf-8"))
    root = d["certified_root"]
    om_re = mp.mpf(root["Omega_re_mp"])
    om_im = abs(mp.mpf(root["Omega_im_mp"]))
    return om_re, om_im, {
        "Omega_re_mp_shipped": root["Omega_re_mp"],
        "Omega_im_mp_shipped": root["Omega_im_mp"],
        "omega_R_M_g": repr(d["adjudication"]["omega_R_M_g"]),
        "omega_I_M_g": repr(d["adjudication"]["omega_I_M_g"]),
    }


OM_R, OM_I, V24_META = read_frozen_band()
BAND_LO = OM_R - OM_I
BAND_HI = OM_R + OM_I
BAND = [BAND_LO + (BAND_HI - BAND_LO) * mp.mpf(i) / (N_BAND - 1) for i in range(N_BAND)]


# ---------------------------------------------------------------------------
# The core closed forms (prereg section 2).
# ---------------------------------------------------------------------------

def S_open(Omega: mp.mpf, x: mp.mpf, p: mp.mpf) -> mp.mpf:
    """Kernel value at which the local gap falls to the drive: S^p = Omega*x/2."""
    return (Omega * x / 2) ** (1 / p)


def S_n(n: int, theta: mp.mpf, x: mp.mpf, rs: mp.mpf) -> mp.mpf:
    return mp.sqrt(S2_exact((mp.mpf(n) - 1 + theta) * L_NODE, rs))


def N_open_closed(Omega: mp.mpf, x: mp.mpf, p: mp.mpf, theta: mp.mpf) -> int:
    """Closed-form inversion, near-wall form (prereg section 2.3)."""
    if S_open(Omega, x, p) >= 1:
        return UNBOUNDED
    x_open_over_l = (1 / (2 * x)) * (Omega * x / 2) ** (2 / p)
    v = x_open_over_l - theta + 1
    return int(max(0, mp.floor(v)))


LINEAR_BUDGET = 4096
UNBOUNDED = -1   # sentinel: S_open >= 1, every cell of the graded region is open


def N_open_count(Omega: mp.mpf, x: mp.mpf, p: mp.mpf, theta: mp.mpf, rs: mp.mpf) -> tuple[int, bool]:
    """EXACT node-by-node count over the cancellation-free S_n -- no cap.

    S_n^2 = 1 - (r_sat/(r_sat+x_n))^2 is STRICTLY INCREASING in n (manifestly:
    it is 1 minus a strictly decreasing positive square), so the predicate
    `S_n <= S_open` is MONOTONE -- true for n <= N, false for n > N.  The count
    is therefore realised by exponential search plus bisection on that monotone
    predicate, which returns the IDENTICAL integer a linear scan would, by
    monotonicity.  DISCLOSED: this is the one implementation liberty taken
    against the frozen phrase "direct node-by-node count", and it is
    cross-checked against an ACTUAL linear scan on every row whose count is
    within LINEAR_BUDGET (which covers every GAP-CLOSED row).

    Returns (count, linear_scan_confirmed).
    """
    so = S_open(Omega, x, p)
    if so >= 1:
        # S_n -> 1 from below for all n, so EVERY cell of the graded region is
        # open and the count is unbounded.  Reported as the sentinel UNBOUNDED
        # rather than as a finite integer, so it can never be mistaken for one.
        return UNBOUNDED, True

    def open_at(n: int) -> bool:
        return S_n(n, theta, x, rs) <= so

    if not open_at(1):
        return 0, True                       # trivially linear-confirmed
    hi = 1
    while open_at(hi * 2):
        hi *= 2
        if hi > 2 ** 40:
            raise SystemExit("N_open exponential search exceeded 2^40 -- unphysical row")
    lo = hi
    hi = hi * 2
    while hi - lo > 1:                       # invariant: open_at(lo), not open_at(hi)
        mid = (lo + hi) // 2
        if open_at(mid):
            lo = mid
        else:
            hi = mid
    count = lo
    confirmed = False
    if count <= LINEAR_BUDGET:
        c = 0
        for n in range(1, LINEAR_BUDGET + 2):
            if open_at(n):
                c += 1
            else:
                break
        confirmed = (c == count)
    return count, confirmed


def zeta_from_transfer(Omega: mp.mpf, x: mp.mpf, p: mp.mpf, s1: mp.mpf) -> mp.mpf:
    """zeta = (w/wm)^2 / |1 - (w/wm)^2| evaluated at the LAST intact cell."""
    ratio = (Omega * x) / (2 * s1**p)          # omega/omega_m(S_1); omega/omega_C = Omega*x
    r2 = ratio**2
    return r2 / abs(1 - r2)


def zeta_from_identity(Omega: mp.mpf, x: mp.mpf, p: mp.mpf, s1: mp.mpf) -> mp.mpf:
    """The section-2.6 identity: zeta = u/|1-u| with u = (S_open/S_1)^(2p)."""
    u = (S_open(Omega, x, p) / s1) ** (2 * p)
    return u / abs(1 - u)


# ---------------------------------------------------------------------------
# The canon-absence pattern battery (prereg section 5.1).  NO pattern uses \b.
# ---------------------------------------------------------------------------

PATTERNS: dict[str, str] = {
    "P1": r"G_c\s*\(\s*A\s*\)",
    "P2": r"G_c[^\n]{0,24}(S\^|S_\\?eps|S\(A\)|\\sqrt\{1)",
    "P3": r"I_\\?omega\s*\(\s*A\s*\)|I_\{?\\?omega\}?\s*\(\s*A\s*\)",
    "P4": r"(I_\\?omega|micro.?inertia)[^\n]{0,40}(S\^|/\s*S|S\(A\))",
    "P5": r"(rotational|Cosserat|micro.?rotation)[^\n]{0,40}band\s*top",
}
SCAN_DIRS = ("manuscript", "research", "src")

# Sentinels for FT-SCAN, sited OUTSIDE the scanned tree by construction.
SENTINEL_ABSENT = "ZZQX" + "APPROACHLEAK" + "ABSENT" + "9137"
SENTINEL_PRESENT_FILE = "Makefile"
SENTINEL_PRESENT = "verify-md-links"


def _tracked_files() -> list[str]:
    out = subprocess.run(["git", "ls-files", "-z", *SCAN_DIRS], cwd=REPO,
                         capture_output=True, text=True, check=True).stdout
    files = [f for f in out.split("\0") if f]
    return [f for f in files if f not in OWN_ARTIFACTS]


def scan_method_a(pattern: str, files: list[str]) -> set[str]:
    """METHOD A: git grep -P (PCRE, ASCII \\w)."""
    proc = subprocess.run(
        ["git", "grep", "-P", "-I", "-n", "-e", pattern, "--", *files],
        cwd=REPO, capture_output=True, text=True)
    hits = set()
    for line in proc.stdout.splitlines():
        parts = line.split(":", 2)
        if len(parts) >= 2:
            hits.add(f"{parts[0]}:{parts[1]}")
    return hits


def scan_method_b(pattern: str, files: list[str]) -> set[str]:
    """METHOD B: Python re on str (Unicode \\w)."""
    rx = re.compile(pattern)
    hits = set()
    for f in files:
        pth = REPO / f
        try:
            text = pth.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for i, line in enumerate(text.splitlines(), start=1):
            if rx.search(line):
                hits.add(f"{f}:{i}")
    return hits


# ---------------------------------------------------------------------------
# THE SWEEP
# ---------------------------------------------------------------------------

def run_sweep() -> dict:
    rows: list[dict] = []
    worst = {
        "max_N_open": 0,
        "max_zeta": mp.mpf(0),
        "max_zid_rel": mp.mpf(0),
        "min_gap2_minus_w2_over_wC2": None,
        "min_log10_margin": None,
        "count_mismatch": 0,
        "linear_unconfirmed": 0,
        "rho_branch_max_sep": mp.mpf(0),
        "n_rows": 0,
    }
    per_p: dict[str, dict] = {}

    for p in P_BRACKET:
        pk = _pk(p)
        agg = {"N_open_values": set(), "max_zeta": mp.mpf(0), "min_log10_margin": None,
               "max_log10_margin": None}
        for m in MASSES:
            rs = r_sat(m)
            x = L_NODE / rs
            for theta in THETAS:
                s1 = mp.sqrt(S2_exact(theta * L_NODE, rs))
                for Om in BAND:
                  # The rho-branch enters the SHEAR impedance and speed, never the
                  # ROTATIONAL gap (which is built from G_c, I_omega and S alone).
                  # It is swept anyway so the degeneracy is MEASURED, not asserted.
                  per_branch = []
                  for rho_branch in RHO_BRANCHES:
                    so = S_open(Om, x, p)
                    n_cf = N_open_closed(Om, x, p, theta)
                    n_ct, lin_ok = N_open_count(Om, x, p, theta, rs)
                    worst["n_rows"] += 1
                    if not lin_ok:
                        worst["linear_unconfirmed"] += 1
                    if n_cf != n_ct:
                        worst["count_mismatch"] += 1
                    z_t = zeta_from_transfer(Om, x, p, s1)
                    z_i = zeta_from_identity(Om, x, p, s1)
                    zid_rel = abs(z_t - z_i) / max(abs(z_t), mp.mpf("1e-300"))
                    # G-REAL: reality of the transfer function at the LAST cell,
                    # in units of omega_C^2 so the comparison is scale-free.
                    gap2 = (2 * s1**p) ** 2
                    w2 = (Om * x) ** 2
                    real_margin = gap2 - w2
                    log10_margin = mp.log(s1 / so, 10)

                    agg["N_open_values"].add(n_ct)
                    if z_t > agg["max_zeta"]:
                        agg["max_zeta"] = z_t
                    for key, cmpf in (("min_log10_margin", min), ("max_log10_margin", max)):
                        cur = agg[key]
                        agg[key] = log10_margin if cur is None else cmpf(cur, log10_margin)

                    worst["max_N_open"] = max(worst["max_N_open"], n_ct)
                    if z_t > worst["max_zeta"]:
                        worst["max_zeta"] = z_t
                    if zid_rel > worst["max_zid_rel"]:
                        worst["max_zid_rel"] = zid_rel
                    if n_ct == 0:
                        cur = worst["min_gap2_minus_w2_over_wC2"]
                        worst["min_gap2_minus_w2_over_wC2"] = (
                            real_margin if cur is None else min(cur, real_margin))
                    cur = worst["min_log10_margin"]
                    worst["min_log10_margin"] = (
                        log10_margin if cur is None else min(cur, log10_margin))

                    # Ship only the reference corner rows; the sweep is gated in
                    # aggregate, and 6240 rows of JSON would be noise.
                    if m == M_REF and theta == 1 and Om in (BAND[0], BAND[-1]):
                        rows.append({
                            "p": pk,
                            "M_over_Msun": _s(m, 4),
                            "theta": _s(theta, 3),
                            "Omega": _s(Om, 30),
                            "band_end": "LO" if Om == BAND[0] else "HI",
                            "S_1": _s(s1, 30),
                            "S_open": _s(so, 30),
                            "log10_S1_over_Sopen": _s(log10_margin, 30),
                            "N_open_closed_form": n_cf,
                            "N_open_direct_count": n_ct,
                            "zeta_max_transfer": _s(z_t, 30),
                            "zeta_max_identity": _s(z_i, 30),
                            "gap_over_drive_at_last_cell": _s(2 * s1**p / (Om * x), 30),
                            "decay_depth_cells_at_last_cell": _s(1 / (mp.sqrt(2) * s1**p), 30),
                            "decay_depth_cells_far_field": _s(1 / mp.sqrt(2), 30),
                            "rho_branch": rho_branch,
                        })
                    per_branch.append((n_ct, z_t))
                  if len(per_branch) == 2:
                      sep = abs(per_branch[0][1] - per_branch[1][1])
                      if per_branch[0][0] != per_branch[1][0]:
                          sep = mp.mpf(1)
                      if sep > worst["rho_branch_max_sep"]:
                          worst["rho_branch_max_sep"] = sep

        per_p[pk] = {
            "provenance": P_PROVENANCE[pk],
            "N_open_distinct_values": sorted(agg["N_open_values"]),
            "bin": "GAP-CLOSED" if agg["N_open_values"] == {0} else "CHANNEL-OPENS",
            "zeta_max_over_sweep": _s(agg["max_zeta"], 30),
            "log10_margin_min": _s(agg["min_log10_margin"], 30),
            "log10_margin_max": _s(agg["max_log10_margin"], 30),
            "side_of_p_crit": ("below" if p < P_CRIT else ("ON" if p == P_CRIT else "above")),
        }

    return {"corner_rows": rows, "per_p": per_p, "worst": worst}


# ---------------------------------------------------------------------------
# G-KNIFE: mass-independence of S_open/S_1 exactly at p = 2 (prereg 5.3)
# ---------------------------------------------------------------------------

def knife(p: mp.mpf, theta: mp.mpf, Om: mp.mpf, near_wall: bool = True) -> tuple[mp.mpf, list[str]]:
    """S_open/S_1 across the mass grid.

    `near_wall=True` uses the frozen prereg-2.1 near-wall floor
    `S_1 -> sqrt(2 theta l_node/r_sat)` on BOTH sides -- which is the form the
    section-2.4 knife-edge derivation is a statement ABOUT (it is an x -> 0
    argument).  `near_wall=False` mixes the EXACT S_1 with the near-wall
    S_open and is reported as a NON-GATED diagnostic whose residual is the
    O(l_node/r_sat) truncation.
    """
    vals = []
    for m in MASSES:
        rs = r_sat(m)
        x = L_NODE / rs
        s1 = mp.sqrt(2 * theta * x) if near_wall else mp.sqrt(S2_exact(theta * L_NODE, rs))
        vals.append(S_open(Om, x, p) / s1)
    spread = max(vals) - min(vals)
    return spread, [_s(v, 30) for v in vals]


# ---------------------------------------------------------------------------
# The residual back-action field -- PLACEHOLDER-CONDITIONED, quarantined.
# ---------------------------------------------------------------------------

def residual_backaction(zeta_max: mp.mpf, theta: mp.mpf, p: mp.mpf, n_cells: mp.mpf) -> dict:
    """SUM_n zeta_n^2 = zeta_max^2 * theta^(2p) * SUM_n (n-1+theta)^(-2p).

    (Prereg section 2.6, exponent 2p.  At p = 1 the sum is psi'(theta).)
    The sum CONVERGES iff 2p > 1; at p = 0.5 it is the harmonic sum and is
    logarithmically divergent in the window, so the finite-window form with
    N = r_sat/l_node cells is reported instead of a closed form.

    The prefactor 2*(G_c/G) rides an ABSOLUTE-MODULUS RATIO that is an engine
    placeholder; this whole field is tagged and quarantined per prereg 2.6.
    """
    out = {
        "prefactor": "2*(G_c/G)",
        "TAG": "PLACEHOLDER-CONDITIONED -- rides the absolute-modulus ratio G_c/G",
        "exponent_2p": _s(2 * p, 4),
    }
    if 2 * p > 1:
        s_exact = mp.zeta(2 * p, theta)         # Hurwitz zeta = SUM (n-1+theta)^{-2p}
        out["convergent"] = True
        out["sum_over_zetamax2"] = _s(theta ** (2 * p) * s_exact, 30)
        out["total_sum_zeta_n_squared"] = _s(zeta_max**2 * theta ** (2 * p) * s_exact, 30)
        if p == 1:
            out["psi1_theta"] = _s(mp.polygamma(1, theta), 30)
            out["hurwitz_vs_polygamma_rel_sep"] = _s(
                abs(s_exact - mp.polygamma(1, theta)) / mp.polygamma(1, theta), 6)
    else:
        # harmonic window: SUM_{n=1..N} 1/(n-1+theta) = psi(N+theta) - psi(theta)
        h = mp.psi(0, n_cells + theta) - mp.psi(0, theta)
        out["convergent"] = False
        out["window_cells_N"] = _s(n_cells, 20)
        out["harmonic_window_sum"] = _s(h, 30)
        out["sum_over_zetamax2"] = _s(theta ** (2 * p) * h, 30)
        out["total_sum_zeta_n_squared"] = _s(zeta_max**2 * theta ** (2 * p) * h, 30)
        out["NOTE"] = ("2p <= 1: the per-cell admixture sum is logarithmically divergent in the "
                       "window, so the finite-window value over the whole graded region "
                       "(N = r_sat/l_node cells) is reported in place of a closed form")
    return out


# ---------------------------------------------------------------------------
# GATES + SELF-TESTS + MAIN
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()
    gates: dict[str, dict] = {}
    fts: dict[str, dict] = {}

    # ---- G-CANON: the ast-parsed constants satisfy the canonical identities --
    canon_l = abs(L_NODE * M_E * C0 / HBAR - 1)
    canon_w = abs(OMEGA_C * L_NODE / C0 - 1)
    canon_x = abs(X_SAT - 7)
    gates["G-CANON"] = {
        "frozen": "ast-parsed constants satisfy L_NODE=hbar/(m_e c), OMEGA_C=c/L_NODE, X_SAT=2/nu_vac=7",
        "tol": "1e-40",
        "measured_L_NODE_identity": _s(canon_l, 6),
        "measured_OMEGA_C_identity": _s(canon_w, 6),
        "measured_X_SAT_minus_7": _s(canon_x, 6),
        "L_NODE": _s(L_NODE, 30), "OMEGA_C": _s(OMEGA_C, 30),
        "pass": bool(canon_l < mp.mpf("1e-40") and canon_w < mp.mpf("1e-40")
                     and canon_x < mp.mpf("1e-40")),
    }

    # ---- G-NC-BAND: v2.4 endpoints, EXACT STRING equality ------------------
    band_str_re = mp.nstr(OM_R, 40, strip_zeros=False)
    shipped_re = V24_META["Omega_re_mp_shipped"]
    ok_band = shipped_re.startswith(band_str_re[:30]) or band_str_re.startswith(shipped_re[:30])
    gates["G-NC-BAND"] = {
        "frozen": "band endpoints read PROGRAMMATICALLY from the v2.4 shipped JSON reproduce Omega_re/|Omega_im|",
        "tol": "exact string (first 30 significant characters)",
        "shipped_Omega_re_mp": shipped_re,
        "shipped_Omega_im_mp": V24_META["Omega_im_mp_shipped"],
        "band_lo": _s(BAND_LO, 30), "band_hi": _s(BAND_HI, 30),
        "n_band_points": N_BAND,
        "pass": bool(ok_band),
    }

    # ---- G-NC-SLAST: reproduce the predecessor's shipped S_last ------------
    lb = json.loads(LASTBOND_JSON.read_text(encoding="utf-8"))
    lad = lb["task3_continuum"]["ladder"][0]
    shipped_S_last = mp.mpf(lad["S_last_from_exact_S2"])
    shipped_x = mp.mpf(lad["ell_over_rsat"])
    rs_ref = r_sat(M_REF)
    x_ref = L_NODE / rs_ref
    s1_ref = mp.sqrt(S2_exact(mp.mpf(1) * L_NODE, rs_ref))
    slast_rel = abs(s1_ref - shipped_S_last) / shipped_S_last
    xrel = abs(x_ref - shipped_x) / shipped_x
    gates["G-NC-SLAST"] = {
        "frozen": "this lane's S_1 at M_ref=62, theta=1 reproduces the predecessor's shipped S_last",
        "tol": "1e-40 rel",
        "shipped_S_last": lad["S_last_from_exact_S2"],
        "this_lane_S_1": _s(s1_ref, 30),
        "measured_rel_sep": _s(slast_rel, 6),
        "shipped_ell_over_rsat": lad["ell_over_rsat"],
        "this_lane_ell_over_rsat": _s(x_ref, 30),
        "ell_over_rsat_rel_sep": _s(xrel, 6),
        "pass": bool(slast_rel < mp.mpf("1e-40")),
        "NON_GATED_diagnosis": (
            "the two agree to 17 significant digits and separate at float64 epsilon scale. The "
            "predecessor's ladder rung is the float64 literal 6.0238983090250982e-19 (17 sig "
            "figs, a repr) which its exact-mp S_last was then SEEDED FROM; this lane derives "
            "l_node/r_sat from M = 62 M_sun at dps = 60. No mp-precision reproduction of a "
            "float64-seeded rung is possible, so the frozen 1e-40 is WRONG-IN-KIND: it was sized "
            "against a round-off error model when the actual error model is the predecessor's "
            "input precision. This is THIS LANE'S OWN FREEZE ERROR and the tolerance is NOT "
            "retuned."),
        "agreement_significant_digits": "17",
    }

    # ---- G-COND: the deliberate float64 cancellation probe ------------------
    naive = 1.0 - (1.0 / (1.0 + float(x_ref))) ** 2
    cf = S2_exact(mp.mpf(1) * L_NODE, rs_ref)
    gates["G-COND"] = {
        "frozen": "naive float64 1-A^2 at the innermost node returns exactly 0.0; cancellation-free S^2 > 0",
        "naive_float64_1_minus_A2": repr(naive),
        "cancellation_free_S2": _s(cf, 30),
        "pass": bool(naive == 0.0 and cf > 0),
    }
    fts["FT-COND"] = {"frozen": "naive float64 must return exactly 0.0",
                      "measured": repr(naive), "fires": bool(naive == 0.0)}

    # ---- the sweep ---------------------------------------------------------
    sw = run_sweep()
    w = sw["worst"]

    gates["G-COUNT"] = {
        "frozen": "N_open by closed-form inversion == N_open by direct node-by-node count, every row",
        "tol": "exact integers",
        "n_rows_swept": w["n_rows"],
        "n_rows_frozen": len(MASSES) * len(THETAS) * N_BAND * len(P_BRACKET) * len(RHO_BRANCHES),
        "mismatches": w["count_mismatch"],
        "rows_without_linear_scan_confirmation": w["linear_unconfirmed"],
        "implementation_note": ("the count is realised by exponential search + bisection on the "
                                "PROVEN-MONOTONE predicate S_n <= S_open, which returns the "
                                "identical integer a linear scan would; every row within "
                                f"LINEAR_BUDGET={LINEAR_BUDGET} is ALSO confirmed by an actual "
                                "linear scan, and that includes every GAP-CLOSED row"),
        "pass": bool(w["count_mismatch"] == 0),
    }
    gates["G-RHO-SPECTATOR"] = {
        "frozen": ("NOT a frozen gate -- a MEASURED degeneracy reported because the freeze counts "
                   "6240 rows including a rho-branch factor: the rotational gap is built from G_c, "
                   "I_omega and S alone, so RHO-A and RHO-B must be EXACTLY degenerate for both "
                   "N_open and zeta"),
        "measured_max_separation": _s(w["rho_branch_max_sep"], 6),
        "status": "NON-GATED DIAGNOSTIC",
        "pass": None,
    }
    gates["G-ZID"] = {
        "frozen": "zeta_max from the transfer function == zeta_max from the (S_open/S_1)^(2p) identity",
        "tol": "1e-45 rel",
        "measured_max_rel_sep": _s(w["max_zid_rel"], 6),
        "pass": bool(w["max_zid_rel"] < mp.mpf("1e-45")),
    }
    minreal = w["min_gap2_minus_w2_over_wC2"]
    gates["G-REAL"] = {
        "frozen": "omega_m^2 - omega^2 > 0 strictly at the last cell of every GAP-CLOSED row; the MINIMUM is reported",
        "tol": "> 0 strictly",
        "measured_min_gap2_minus_omega2_in_omegaC2_units": _s(minreal, 30) if minreal is not None else None,
        "pass": bool(minreal is not None and minreal > 0),
    }

    # ---- G-KNIFE + FT-KNIFE ------------------------------------------------
    Om_mid = BAND[(N_BAND - 1) // 2]
    sp2, vals2 = knife(mp.mpf(2), mp.mpf(1), Om_mid)
    sp2x, vals2x = knife(mp.mpf(2), mp.mpf(1), Om_mid, near_wall=False)
    gates["G-KNIFE"] = {
        "frozen": "at p = 2 exactly, S_open/S_1 is mass-INDEPENDENT: spread across the 4-mass grid is zero",
        "tol": "1e-45",
        "measured_spread": _s(sp2, 6),
        "values": vals2,
        "p_crit_derived": "2",
        "closed_form_S_open_over_S_1_at_p2": _s(mp.sqrt(Om_mid / 4), 30),
        "implementation_note": ("evaluated on the frozen prereg-2.1 NEAR-WALL floor "
                               "S_1 -> sqrt(2*theta*l_node/r_sat) on both sides, which is the form "
                               "the section-2.4 knife-edge derivation is a statement about (an "
                               "x -> 0 argument); the exact-S_1 variant is reported below as a "
                               "NON-GATED diagnostic"),
        "NON_GATED_exact_S1_variant_spread": _s(sp2x, 6),
        "NON_GATED_exact_S1_variant_values": vals2x,
        "NON_GATED_diagnosis": ("the exact-S_1 spread is the O(l_node/r_sat) near-wall truncation, "
                               "largest at the smallest mass where l_node/r_sat is largest"),
        "pass": bool(sp2 < mp.mpf("1e-45")),
    }
    sp_lo, _ = knife(mp.mpf("1.99"), mp.mpf(1), Om_mid)
    sp_hi, _ = knife(mp.mpf("2.01"), mp.mpf(1), Om_mid)
    # trend direction: sign of d(S_open/S_1)/d(mass) -- masses ascend, so compare ends
    def _trend(p):
        vs = []
        for m in MASSES:
            rs = r_sat(m); xx = L_NODE / rs
            s1 = mp.sqrt(S2_exact(L_NODE, rs))
            vs.append(S_open(Om_mid, xx, p) / s1)
        return mp.sign(vs[-1] - vs[0])
    t_lo, t_hi = _trend(mp.mpf("1.99")), _trend(mp.mpf("2.01"))
    fts["FT-KNIFE"] = {
        "frozen": "at p=1.99 and p=2.01 the mass-spread is NON-zero and the mass-TREND is of OPPOSITE sign",
        "spread_p199": _s(sp_lo, 6), "spread_p201": _s(sp_hi, 6),
        "trend_p199": _s(t_lo, 3), "trend_p201": _s(t_hi, 3),
        "fires": bool(sp_lo > 0 and sp_hi > 0 and t_lo * t_hi < 0),
    }

    # ---- G-SUM -------------------------------------------------------------
    th = mp.mpf(1)
    direct = mp.nsum(lambda n: 1 / (n - 1 + th) ** 2, [1, mp.inf])
    poly = mp.polygamma(1, th)
    sum_rel = abs(direct - poly) / poly
    gates["G-SUM"] = {
        "frozen": "SUM_n (n-1+theta)^-2 by summation-plus-tail == polygamma(1, theta)",
        "tol": "1e-30 rel",
        "measured_rel_sep": _s(sum_rel, 6),
        "polygamma_1_1": _s(poly, 30),
        "pass": bool(sum_rel < mp.mpf("1e-30")),
    }

    # ---- FT-COUNT / FT-ZID / FT-REAL --------------------------------------
    p1, th1 = mp.mpf(1), mp.mpf(1)
    n_inj, _ = N_open_count(Om_mid * mp.mpf("1e30"), x_ref, p1, th1, rs_ref)
    fts["FT-COUNT"] = {
        "frozen": "a drive scaled by 1e30 must make N_open >= 1 at M_ref, theta=1, p=1",
        "measured_N_open": ("UNBOUNDED (S_open >= 1)" if n_inj == UNBOUNDED else n_inj),
        "fires": bool(n_inj == UNBOUNDED or n_inj >= 1)}

    z_t = zeta_from_transfer(Om_mid, x_ref, p1, s1_ref)
    z_pert = z_t * (1 + mp.mpf("1e-40"))
    rel_pert = abs(z_pert - zeta_from_identity(Om_mid, x_ref, p1, s1_ref)) / z_t
    fts["FT-ZID"] = {
        "frozen": "perturbing zeta_max by 1e-40 relative must make G-ZID fail (sep >= 1e-45)",
        "measured_rel_sep_after_perturbation": _s(rel_pert, 6),
        "fires": bool(rel_pert >= mp.mpf("1e-45"))}

    p_big = mp.mpf(12)
    s1b = s1_ref
    real_inj = (2 * s1b ** p_big) ** 2 - (Om_mid * x_ref) ** 2
    fts["FT-REAL"] = {
        "frozen": "injecting p=12 at M_ref must drive omega_m^2 - omega^2 NEGATIVE at the last cell",
        "measured": _s(real_inj, 6), "fires": bool(real_inj < 0)}

    # ---- the scan ----------------------------------------------------------
    files = _tracked_files()
    scan: dict[str, dict] = {}
    scan_ok = True
    for pid, pat in PATTERNS.items():
        a = scan_method_a(pat, files)
        b = scan_method_b(pat, files)
        agree = a == b
        scan_ok = scan_ok and agree
        union = sorted(a | b)
        scan[pid] = {
            "pattern": pat,
            "method_A_git_grep_P_hits": len(a),
            "method_B_python_re_hits": len(b),
            "agree": agree,
            "union_hits": union[:40],
            "n_union": len(union),
            "ABSENCE_RECEIPT": bool(len(union) == 0),
        }
    gates["G-SCAN"] = {
        "frozen": "METHOD A and METHOD B hit sets identical per pattern; disagreement is the reported result",
        "n_files_scanned": len(files),
        "own_artifacts_excluded": sorted(OWN_ARTIFACTS),
        "pass": bool(scan_ok),
    }
    sa = scan_method_a(re.escape(SENTINEL_ABSENT), files)
    sb = scan_method_b(re.escape(SENTINEL_ABSENT), files)
    pa = scan_method_a(re.escape(SENTINEL_PRESENT), files)
    pb = scan_method_b(re.escape(SENTINEL_PRESENT), files)
    fts["FT-SCAN"] = {
        "frozen": "absent sentinel (sited OUTSIDE the scanned tree) -> zero hits on BOTH; present sentinel -> same non-zero set on BOTH",
        "absent_sentinel_A": len(sa), "absent_sentinel_B": len(sb),
        "present_sentinel_A": len(pa), "present_sentinel_B": len(pb),
        "fires": bool(len(sa) == 0 and len(sb) == 0 and len(pa) > 0 and pa == pb),
    }

    # ---- residual back-action (quarantined) --------------------------------
    n_cells_full = rs_ref / L_NODE
    resid = {}
    for pp in P_BRACKET:
        key = _pk(pp)
        s1r = mp.sqrt(S2_exact(L_NODE, rs_ref))
        zmx = zeta_from_transfer(BAND[-1], x_ref, pp, s1r)   # band TOP, M_ref, theta = 1
        resid[key] = residual_backaction(zmx, mp.mpf(1), pp, n_cells_full)
        resid[key]["zeta_max_at_M_ref_theta1_bandtop"] = _s(zmx, 30)
    resid["_scope"] = ("evaluated at M_ref = 62 M_sun, theta = 1, band TOP; "
                       f"N = r_sat/l_node = {_s(n_cells_full, 20)} cells")

    payload = {
        "_prereg": "research/2026-08-05_approach-leak_prereg-FROZEN.md (commit bdb8b4a4, pushed ALONE)",
        "_ruling": "_orchestration/docket-entries/2026-08-05-ruling-kernel-collapse-rescope.md",
        "_non_claim": ("DERIVATION result. Mints no clm-/def-/exp-/sup-/ilk-; propagates to no KB "
                       "or manuscript leaf; moves no solidity. Engine src/ave byte-untouched and "
                       "never imported."),
        "_method": {
            "dps": mp.dps,
            "constants_source": "ast literal parse of src/ave/core/constants.py (no import)",
            "regex_engines": {"METHOD_A": "git grep -P (PCRE, ASCII \\w)",
                              "METHOD_B": "python re on str (Unicode \\w)"},
            "no_word_boundary_in_battery": all("\\b" not in p for p in PATTERNS.values()),
            "error_model": "round-off only; no iterated map; closed forms evaluated once",
        },
        "_frozen_numerics": {
            "masses_Msun": [_s(m, 4) for m in MASSES],
            "thetas": [_s(t, 3) for t in THETAS],
            "p_bracket": [_s(p, 3) for p in P_BRACKET],
            "rho_branches": RHO_BRANCHES,
            "beta_bracket_omegaC": [_s(b, 8) for b in BETA_BRACKET],
            "n_band": N_BAND,
            "p_crit": "2",
            "x_sat": _s(X_SAT, 20),
            "ell_node_m": _s(L_NODE, 30),
            "omega_C_rad_s": _s(OMEGA_C, 30),
        },
        "rotational_band_top_bracket_REPORTED_NONE_CHOSEN": {
            k: _s(v, 20) for k, v in ROT_TOP.items()},
        "gates": gates,
        "self_tests": fts,
        "sweep": {"per_p": sw["per_p"], "corner_rows": sw["corner_rows"]},
        "residual_backaction_QUARANTINED": resid,
        "scan": scan,
    }
    payload["gates"]["G-DET"] = {
        "frozen": "two full runs, identical digest, byte-identical JSON apart from _runtime_sec",
        "method": ("MACHINE-GATED on every `make verify`: approach_leak_number_check.py re-runs "
                   "this driver into a temporary path via APPROACH_LEAK_OUT and requires the "
                   "re-computed _digest to equal the shipped one"),
        "pass": None,
        "status": "GATED BY THE NUMBER-CHECK",
    }

    body = json.dumps(payload, indent=1, sort_keys=True, ensure_ascii=False)
    payload["_digest"] = hashlib.sha256(body.encode("utf-8")).hexdigest()[:16]
    payload["_runtime_sec"] = round(time.time() - t0, 2)
    OUT.write_text(json.dumps(payload, indent=1, sort_keys=True, ensure_ascii=False) + "\n",
                   encoding="utf-8")

    n_fail = [k for k, v in gates.items() if v.get("pass") is False]
    n_nofire = [k for k, v in fts.items() if not v.get("fires")]
    print(f"digest={payload['_digest']}  gates_failed={n_fail}  self_tests_not_fired={n_nofire}")
    for pk, v in sw["per_p"].items():
        nv = v["N_open_distinct_values"]
        nv_s = str(nv) if len(nv) <= 4 else f"[{min(nv)} .. {max(nv)}] ({len(nv)} distinct)"
        print(f"  p={pk:<4} {v['bin']:<14} N_open={nv_s:<32} "
              f"log10(S1/Sopen) in [{v['log10_margin_min'][:10]}, {v['log10_margin_max'][:10]}]  "
              f"zeta_max={v['zeta_max_over_sweep']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
