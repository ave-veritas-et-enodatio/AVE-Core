#!/usr/bin/env python3
"""Driver for the A_g derivation lane (R46 derive-first).

Executes the FROZEN consumer set of research/2026-08-10_ag-derivation_prereg-FROZEN.md:
  C1 — dress normalization (canon profile + clause-G bridge; absolute-anchor sweep)
  C2 — halo added-mass row (convected-dress kinetic hosting; inversion vs the DM
       magnitude-class bracket)
  C3 — backreaction.py kappa chain (Green's-function convention, negative control
       first; the measured chain coefficient f vs the internal relation's 7)

Engines (named at freeze): sympy (symbolic), numpy/scipy fixed-seed (float),
backreaction.py (consumed read-only), BSD grep + Python re (sweeps).
Constants ONLY via ave.core.constants (ave-canonical-source).
Deterministic output: no timestamps, sorted keys; two runs must be byte-identical.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys

import numpy as np
import sympy as sp

from ave.core.constants import C_0, G, HBAR, L_NODE, M_E, M_SUN, RHO_BULK, XI_MACHIAN

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "ag_derivation_lane_results.json")

RNG = np.random.default_rng(20260810)

# ENG-CHOICE external unit bridge (prereg §3-C2; tagged, not substrate-derived).
# M_SUN is canonical (constants.py:132); the kpc is not in constants.py.
KPC = 3.0857e19  # m   [ENG-CHOICE / CODATA-external]


# ────────────────────────────────────────────────────────────────────────────────
# C1 — the dress normalization
# ────────────────────────────────────────────────────────────────────────────────
def run_c1() -> dict:
    r, M, c, Gs, Ag = sp.symbols("r M c G A_g", positive=True)
    eps = 7 * Gs * M / (c**2 * r)  # canon profile (clm-zbvfpi)
    # clause G: u0 = -A_g * d(eps)/dr (radial component)
    u0 = -Ag * sp.diff(eps, r)  # = +A_g*7GM/(c^2 r^2)  (outward)
    B_pred = sp.simplify(u0 * r**2)  # dress amplitude B in u0 = B/r^2
    internal = 7 * Ag * Gs * M / c**2
    bridge_matches_internal = sp.simplify(B_pred - internal) == 0

    # two-engine absolute-dress-amplitude sweep
    pats = [
        r"dress amplitude",
        r"4\s?[πp]i?\s?B",
        r"u.?0\s*=\s*B",
        r"B\s*=\s*[0-9]",
        r"B\(M\)\s*=",
        r"enclosed (compression|dilatation) (charge|flux)",
    ]
    roots = ["research", "manuscript"]
    # SVA row-9 (pilot-5 G-SCAN amendment): an instrument whose scan surface
    # includes its own output must exclude its own artifacts BY CONSTRUCTION.
    own = "2026-08-10_ag-derivation"
    grep_hits: dict[str, list[str]] = {}
    for p in pats:
        cmd = ["grep", "-rniE", p] + roots + [
            "--include=*.md", "--include=*.tex", f"--exclude=*{own}*",
        ]
        try:
            out = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO, timeout=120).stdout
        except Exception as e:  # noqa: BLE001
            out = f"ENGINE-ERROR: {e}"
        grep_hits[p] = sorted(out.strip().splitlines())[:400] if out.strip() else []

    py_hits: dict[str, int] = {}
    for p in pats:
        rx = re.compile(p, re.IGNORECASE)
        n = 0
        for root in roots:
            for dirpath, _dirs, files in os.walk(os.path.join(REPO, root)):
                for fn in sorted(files):
                    if not (fn.endswith(".md") or fn.endswith(".tex")):
                        continue
                    if own in fn:
                        continue
                    try:
                        txt = open(os.path.join(dirpath, fn), encoding="utf-8").read()
                    except Exception:  # noqa: BLE001
                        continue
                    n += len(rx.findall(txt))
        py_hits[p] = n

    engines_agree = {
        p: (len(grep_hits[p]) > 0) == (py_hits[p] > 0) for p in pats
    }
    return {
        "bridge_B_pred": str(B_pred),
        "bridge_matches_internal_relation": bool(bridge_matches_internal),
        "sweep_patterns": pats,
        "sweep_grep_hit_counts": {p: len(grep_hits[p]) for p in pats},
        "sweep_py_hit_counts": py_hits,
        "sweep_engines_agree_on_presence": engines_agree,
        "sweep_grep_hits": grep_hits,
    }


# ────────────────────────────────────────────────────────────────────────────────
# C2 — the halo added-mass row
# ────────────────────────────────────────────────────────────────────────────────
def run_c2() -> dict:
    # (a) exact convected-dress added mass, u0 = B r̂/r², V = V ẑ
    x, y, z, B, rc = sp.symbols("x y z B r_c", positive=False)
    r = sp.sqrt(x**2 + y**2 + z**2)
    u = sp.Matrix([B * x / r**3, B * y / r**3, B * z / r**3])
    dudz = u.diff(z)
    integrand = sp.simplify(dudz.dot(dudz))  # |∂_z u0|²
    # spherical reduction (exact): integrand = B²(1+3cos²θ)/r⁶
    rr, th = sp.symbols("rho theta", positive=True)
    integrand_sph = sp.simplify(
        integrand.subs(
            {x: rr * sp.sin(th), y: 0, z: rr * sp.cos(th)}
        )
    )
    I_exact = sp.integrate(
        sp.integrate(integrand_sph * 2 * sp.pi * rr**2 * sp.sin(th), (th, 0, sp.pi)),
        (rr, sp.Symbol("r_c", positive=True), sp.oo),
    )
    I_exact = sp.simplify(I_exact)  # expect 8*pi*B²/(3*r_c³)
    m_add_coeff = sp.simplify(I_exact / (B**2))  # rho * I = m_add ; coeff = 8π/(3 r_c³)

    # (b) independent numeric cross-check: finite-difference gradient + 2D quadrature
    from scipy.integrate import quad

    def u_num(pt):
        rn = np.sqrt((pt**2).sum())
        return pt / rn**3

    def dudz_sq(rho_v, th_v):
        pt = np.array([rho_v * np.sin(th_v), 0.0, rho_v * np.cos(th_v)])
        h = 1e-6 * rho_v
        d = (u_num(pt + np.array([0, 0, h])) - u_num(pt - np.array([0, 0, h]))) / (2 * h)
        return float((d**2).sum())

    def radial_int(th_v, rc_v=1.0):
        val, _ = quad(lambda rv: dudz_sq(rv, th_v) * rv**2, rc_v, 200.0, limit=400)
        # tail beyond 200 (integrand ~ (1+3cos²θ)/r⁴): analytic tail per θ
        tail = (1 + 3 * np.cos(th_v) ** 2) / (3 * 200.0**3)
        return val + tail

    num, _ = quad(lambda tv: radial_int(tv) * 2 * np.pi * np.sin(tv), 0, np.pi, limit=200)
    exact_at_1 = float(I_exact.subs({B: 1, sp.Symbol("r_c", positive=True): 1}))
    rel_err = abs(num - exact_at_1) / exact_at_1

    # (c) inversion at declared galactic parameters (ENG-CHOICE)
    M_b = 6e10 * M_SUN
    r_c = 10.0 * KPC
    rho = float(RHO_BULK)
    out = {}
    for chi in (1.0, 10.0):
        # m_add = rho * (8π/3) B²/r_c³ = chi*M  with  B = 7 A_g G M / c²
        # ⇒ A_g = sqrt( 3 chi M r_c³ c⁴ / (8π rho 49 G² M²) )
        Ag = float(
            np.sqrt(3.0 * chi * M_b * r_c**3 * C_0**4 / (8.0 * np.pi * rho * 49.0 * G**2 * M_b**2))
        )
        out[f"A_g_required_chi_{chi:g}"] = Ag
        out[f"c_pure_chi_{chi:g}"] = Ag / float(L_NODE) ** 2
    # strain-consistency exhibits at the chi=1 value
    Ag1 = out["A_g_required_chi_1"]
    B_gal = 7.0 * Ag1 * G * M_b / C_0**2
    strain_gal = 2.0 * B_gal / r_c**3  # |du0/dr| deviatoric scale at r_c
    M_star, R_star = M_SUN, 6.96e8  # ENG-CHOICE solar exhibit
    B_star = 7.0 * Ag1 * G * M_star / C_0**2
    strain_star = 2.0 * B_star / R_star**3
    return {
        "I_exact_sym": str(I_exact),
        "m_add_coeff_over_rhoB2": str(m_add_coeff),
        "numeric_cross_check_rel_err": rel_err,
        "rho_bulk_SI": rho,
        "params_ENG_CHOICE": {"M_b_kg": M_b, "r_c_m": r_c, "chi_bracket": [1, 10]},
        **out,
        "exhibit_dress_strain_at_galactic_rc": strain_gal,
        "exhibit_dress_strain_at_solar_surface": strain_star,
        "ell_node_sq_m2": float(L_NODE) ** 2,
        "xi_machian": float(XI_MACHIAN),
    }


# ────────────────────────────────────────────────────────────────────────────────
# C3 — the backreaction kappa chain
# ────────────────────────────────────────────────────────────────────────────────
def _fit_b_over_window(eps: np.ndarray, rr: np.ndarray, r_in: float, r_out: float):
    from ave.gravity.backreaction import _fit_inverse_power_model

    b, a, r2 = _fit_inverse_power_model(eps, rr, r_in, r_out, power=1.0)
    return {"b": b, "a": a, "R2": r2}


def run_c3() -> dict:
    from scipy import sparse
    from scipy.sparse.linalg import spsolve

    N = 32
    c = N // 2
    i, j, k = np.indices((N, N, N))
    rr = np.sqrt((i - c) ** 2 + (j - c) ** 2 + (k - c) ** 2)
    ndof = N**3
    src_amp = 1e-3
    T00 = np.zeros((N, N, N))
    T00[c, c, c] = src_amp
    M_lat = float(T00.sum())

    # (a) NEGATIVE CONTROL — standard 7-pt Cartesian Laplacian (known 1/(4πr) GF)
    lin = np.arange(ndof)
    ii, jj, kk = np.unravel_index(lin, (N, N, N))
    diag = 6.0 * np.ones(ndof)
    rows, cols, vals = [lin], [lin], [diag]
    for ax, idx in ((0, ii), (1, jj), (2, kk)):
        for s in (+1, -1):
            nb = [ii.copy(), jj.copy(), kk.copy()]
            nb[ax] = (nb[ax] + s) % N
            rows.append(lin)
            cols.append(np.ravel_multi_index(tuple(nb), (N, N, N)))
            vals.append(-1.0 * np.ones(ndof))
    L7 = sparse.csr_matrix(
        (np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(ndof, ndof)
    )
    bnd = np.zeros((N, N, N), dtype=bool)
    bnd[0] = bnd[-1] = True
    bnd[:, 0] = bnd[:, -1] = True
    bnd[:, :, 0] = bnd[:, :, -1] = True
    bnd = bnd.reshape(ndof)
    intr = ~bnd
    Li = L7[intr][:, intr]
    eps7 = np.zeros(ndof)
    eps7[intr] = spsolve(Li.tocsc(), T00.reshape(ndof)[intr])
    eps7 = eps7.reshape(N, N, N)
    fit7_near = _fit_b_over_window(eps7, rr, 3.0, 8.0)
    fit7_far = _fit_b_over_window(eps7, rr, 8.0, 12.0)
    b_expected = M_lat / (4.0 * np.pi)

    # (b) NATIVE operator via relax_finite_core_strain (linear regime, D→1)
    from ave.gravity.gw_propagation import relax_finite_core_strain

    res = relax_finite_core_strain(
        N=N, T00_override=T00, n_picard=6, picard_mix=1.0, S_min=1e-3
    )
    epsN = np.asarray(res["eps11"], dtype=float)
    max_A = float(np.abs(epsN).max())
    fitN_near = _fit_b_over_window(epsN, rr, 3.0, 8.0)
    fitN_far = _fit_b_over_window(epsN, rr, 8.0, 12.0)

    # (b2) RESIDUAL RECEIPT — the exact discrete divergence-form identity.
    # ⚑ TIER-2 RE-CLASSIFIED (2026-08-10, algebra-knife finding 3′): this identity
    # (Σ_ball L·ε = Σ_ball T00, exact by Div == Grad.T adjointness/telescoping) is
    # a SOLVE-RESIDUAL check and is NORMALIZATION-BLIND — it returns 1.0 for ANY
    # κ-rescale, including one wrong by exactly 4π (panel probe). It therefore
    # verifies the divergence form, NOT the chain coefficient f. The only native
    # GF-amplitude measurement in this driver is the smooth-blob masked fit below
    # (two_way_blob.fit_diagnostic), which separates 1× from 16× but is
    # window-fragile (R² ≈ 0.88; band ~0.74–0.99 across windows).
    # Sublattice diagnosis (three-method panel receipt): the p−p′ difference
    # lattice has index |det| = 16 in Z³ and connected_components(L) = 16 for
    # N ≡ 0 (mod 4) — a point source feeds ONE class (masked fit inflates ×16);
    # CAVEAT: at N ≡ 2 (mod 4) the torus wrap halves the count to 8.
    from ave.gravity.gw_propagation import _build_native_grad_div
    from scipy import sparse as _sp

    Grad, Div = _build_native_grad_div(
        N, instrument_scope="ag-derivation lane C3 flux receipt (read-only)"
    )
    A_flat = np.clip(epsN.reshape(ndof), 0.0, 1.0)
    from ave.solvers.graded_vacuum_network import stiffness_profile

    Dvec = stiffness_profile(A_flat, exponent=0.5, S_min=1e-3)
    Lnative = (Div @ _sp.diags(np.tile(Dvec, 3)) @ Grad).tocsr()
    Leps = np.asarray(Lnative @ epsN.reshape(ndof)).reshape(N, N, N)
    flux_receipts = {}
    for R in (6.0, 10.0):
        ball = rr <= R
        flux_receipts[f"ball_R{R:g}"] = {
            "sum_L_eps": float(Leps[ball].sum()),
            "sum_T00": float(T00[ball].sum()),
            "ratio": float(Leps[ball].sum() / max(T00[ball].sum(), 1e-300)),
        }
    zero_frac = float((np.abs(epsN) < 1e-14).mean())
    interior_mask = ~bnd.reshape(N, N, N)
    zero_frac_interior = float((np.abs(epsN[interior_mask]) < 1e-14).mean())

    # (b3) BLOB leg through the ACTUAL two-way path (frozen method: "point + blob")
    from ave.gravity.backreaction import solve_backreaction

    two_way = solve_backreaction(
        N=28, sigma=2.5, amplitude=0.002, source_mode="komar", return_fields=True
    )
    epsB = np.asarray(two_way["eps11"], dtype=float)
    rrB = np.asarray(two_way["rr"], dtype=float)
    T00B = np.asarray(two_way["T00_total"], dtype=float)
    NB = epsB.shape[0]
    GradB, DivB = _build_native_grad_div(
        NB, instrument_scope="ag-derivation lane C3 blob flux receipt (read-only)"
    )
    A_B = np.clip(epsB.reshape(NB**3), 0.0, 1.0)
    DvecB = stiffness_profile(A_B, exponent=0.5, S_min=1e-3)
    LB = (DivB @ _sp.diags(np.tile(DvecB, 3)) @ GradB).tocsr()
    LepsB = np.asarray(LB @ epsB.reshape(NB**3)).reshape(NB, NB, NB)
    blob_flux = {}
    for R in (8.0, 11.0):
        ball = rrB <= R
        blob_flux[f"ball_R{R:g}"] = {
            "sum_L_eps": float(LepsB[ball].sum()),
            "sum_T00_src": float(T00B[ball].sum()),
            "ratio": float(LepsB[ball].sum() / max(T00B[ball].sum(), 1e-300)),
        }
    blob_fit = _fit_b_over_window(epsB, rrB, 5.0, 10.0)
    blob_b_expected = float(T00B.sum()) / (4.0 * np.pi)

    # (c) SI-chain algebra (sympy), BOTH source conventions:
    #  - plain-density reading (the first cut's premise): -κ∇²ε = M c² δ³
    #  - the CANON-DECLARED convention (⚑ Tier-2: gordon-optical-metric.md:25,
    #    clm-rd9cjm): -κ∇²ε = 4π M c² δ³  — Green's fn -1/4πr ⇒ ε = 7GM/c²r EXACT
    Ms, cs, Gsym, rs = sp.symbols("M c G r", positive=True)
    kappa = cs**4 / (7 * Gsym)
    b_SI = (Ms * cs**2) / (4 * sp.pi * kappa)  # 1/r coeff, plain-density reading
    f_chain = sp.simplify(b_SI / (Gsym * Ms / cs**2))  # = 7/(4π)
    b_SI_canon = (4 * sp.pi * Ms * cs**2) / (4 * sp.pi * kappa)  # canon 4π source
    f_chain_canon = sp.simplify(b_SI_canon / (Gsym * Ms / cs**2))  # = 7 exactly
    f_profile = sp.Integer(7)  # canon-profile side: B = A_g·7GM/c²
    ratio = sp.simplify(f_profile / f_chain)  # the two READINGS differ by 4π

    return {
        "lattice_M": M_lat,
        "b_expected_bare_GF": b_expected,
        "control_7pt": {"near": fit7_near, "far": fit7_far,
                        "b_over_expected_near": fit7_near["b"] / b_expected,
                        "b_over_expected_far": fit7_far["b"] / b_expected},
        "native_relax": {"near": fitN_near, "far": fitN_far,
                         "b_over_expected_near": fitN_near["b"] / b_expected,
                         "b_over_expected_far": fitN_far["b"] / b_expected,
                         "max_A": max_A, "converged": bool(res.get("converged", False)),
                         "n_iter": int(res.get("n_iter", -1)),
                         "profile_fit_status": "DIAGNOSTIC-ONLY (parity-class confounded; see flux receipt)"},
        "native_flux_receipt_exact": flux_receipts,
        "native_sublattice_zero_fraction": zero_frac,
        "native_sublattice_zero_fraction_interior": zero_frac_interior,
        "two_way_blob": {
            "flux_receipt": blob_flux,
            "fit_diagnostic": blob_fit,
            "b_expected_bare_GF": blob_b_expected,
            "b_over_expected_DIAGNOSTIC": blob_fit["b"] / blob_b_expected,
            "converged": bool(two_way.get("converged", False)),
            "max_A": float(two_way.get("max_A", -1.0)),
        },
        "f_chain_SI_exact": str(f_chain),
        "f_chain_SI_float": float(f_chain.evalf()),
        "f_chain_CANON_convention_exact": str(f_chain_canon),
        "f_chain_CANON_convention_float": float(f_chain_canon.evalf()),
        "f_profile_exact": str(f_profile),
        "profile_over_chain_ratio_exact": str(ratio),
        "profile_over_chain_ratio_float": float(ratio.evalf()),
        "consumers_agree_under_canon_convention": bool(
            sp.simplify(f_chain_canon - f_profile) == 0
        ),
    }


def run_c3_convention_sweep() -> dict:
    """C3c — does any canon site declare the solve's source with an explicit 4π?

    ⚑ TIER-2 REPAIRED INSTRUMENT (2026-08-10). The first-cut patterns required the
    literal token T00 next to the 4π and could not match LaTeX ``4\\pi`` at all
    (``[πp]`` matches Unicode π or ASCII 'p', and the backslash of ``\\pi`` defeats
    ``4\\s?[πp]``) — a structural false-negative on every LaTeX-spelled canon
    equation. The Tier-2 panel found the declaration the first cut missed:
    ``gordon-optical-metric.md:25`` (clm-rd9cjm). Repairs: (a) symbol-agnostic
    LaTeX+Unicode patterns; (b) a KNOWN-POSITIVE control line the pattern set MUST
    match (liveness, the missing-negative-control defect); (c) the claim-id-trail
    enumeration (every host of clm-rd9cjm) alongside the regex sweep; (d) a genuine
    second engine (Python re) for THIS sweep, not only C1's.
    """
    pats = [
        r"4\s*(\\,)?\s*(\\pi|π)\s*(\\,)?\s*M\s*c",  # 4π M c² source spelling
        r"4\s*(\\,)?\s*(\\pi|π)\s*(\\,)?\s*(G|T_?\{?00\}?|\\rho|rho)",
        r"(\\delta|δ)\s*\^?\{?3\}?\s*\(",  # δ³( — point-source statements
        r"Green",
    ]
    known_positive = (
        r"-\left(\frac{c^{4}}{7G}\right)\nabla^{2}\epsilon_{11}(r) = 4\pi Mc^{2}\delta^{3}(r)"
    )
    liveness = {p: bool(re.search(p, known_positive)) for p in pats}
    roots = ["manuscript", "research", "src/ave/gravity"]
    hits: dict[str, list[str]] = {}
    py_counts: dict[str, int] = {}
    for p in pats:
        cmd = ["grep", "-rniE", p] + roots + [
            "--include=*.md", "--include=*.tex", "--include=*.py",
            "--exclude=*2026-08-10_ag-derivation*",
        ]
        try:
            out = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO, timeout=120).stdout
        except Exception as e:  # noqa: BLE001
            out = f"ENGINE-ERROR: {e}"
        hits[p] = sorted(out.strip().splitlines())[:400] if out.strip() else []
        rx = re.compile(p, re.IGNORECASE)
        n = 0
        for root in roots:
            for dirpath, _dirs, files in os.walk(os.path.join(REPO, root)):
                for fn in sorted(files):
                    if not fn.endswith((".md", ".tex", ".py")) or "2026-08-10_ag-derivation" in fn:
                        continue
                    try:
                        txt = open(os.path.join(dirpath, fn), encoding="utf-8").read()
                    except Exception:  # noqa: BLE001
                        continue
                    n += len(rx.findall(txt))
        py_counts[p] = n
    # claim-id trail: every host of clm-rd9cjm (the profile's canonical claim)
    cmd = ["grep", "-rn", "clm-rd9cjm", "manuscript", "--include=*.md", "--include=*.tex"]
    trail = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO, timeout=120).stdout
    return {
        "patterns": pats,
        "liveness_known_positive_matched": liveness,
        "hits": hits,
        "hit_counts": {p: len(hits[p]) for p in pats},
        "py_engine_counts": py_counts,
        "engines_agree_on_presence": {p: (len(hits[p]) > 0) == (py_counts[p] > 0) for p in pats},
        "clm_rd9cjm_trail": sorted(trail.strip().splitlines()),
        "declaration_found": sorted(
            h for p in pats[:1] for h in hits[p] if "gordon-optical-metric" in h or "03_macroscopic_relativity" in h
        ),
    }


def main() -> None:
    results = {
        "lane": "ag-derivation (R46 derive-first)",
        "base": "8424995f",
        "constants": {
            "L_NODE": float(L_NODE),
            "L_NODE_check_hbar_mec": float(HBAR / (M_E * C_0)),
            "RHO_BULK": float(RHO_BULK),
            "XI_MACHIAN": float(XI_MACHIAN),
            "G": float(G),
            "C_0": float(C_0),
        },
        "C1": run_c1(),
        "C2": run_c2(),
        "C3": run_c3(),
        "C3_convention_sweep": run_c3_convention_sweep(),
    }
    blob = json.dumps(results, indent=1, sort_keys=True, ensure_ascii=False) + "\n"
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(blob)
    # printed digest == file digest (Tier-2 receipts-lens nit: was pre-newline)
    print("sha256:", hashlib.sha256(blob.encode()).hexdigest())
    print("wrote", OUT)


if __name__ == "__main__":
    sys.exit(main())
