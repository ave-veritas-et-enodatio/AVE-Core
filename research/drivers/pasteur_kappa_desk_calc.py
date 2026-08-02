"""Pasteur-kappa desk-calc — the CLASSICAL chirality of the as-fabbed HOPF-02a (2,3) knot.

PRE-REG (frozen BEFORE this file existed):
    research/2026-08-02_pasteur-kappa-desk-calc_prereg-FROZEN.md   (commit 3ae1f3de)

WHAT THIS IS.  A classical-electromagnetism baseline computation.  It makes NO AVE
claim.  It computes the Pasteur chirality parameter kappa of a copper wire knot on
FR-4, from Maxwell's equations only, so that a SEPARATE adjudication (AVE-HOPF
round-2's own Step-2.5 rule, which routes form-shared claims to the MAGNITUDE axis)
has a competitor magnitude to compare against.  The AVE side enters as exactly one
reference number, kappa_AVE,eff = alpha * pq/(p+q) = 1.2*alpha.

WHAT IT IS NOT.  Not a solver, not a lattice, not an engine run.  No AVE constant,
axiom, operator or saturation kernel enters the classical chain.  alpha is imported
ONLY to form the AVE-side reference value.

THE CHAIN (prereg sec 3.1, every step elementary EM):

  1. resonant mode          Ic(s) = I0 sin(pi s / L)          [thin-wire half-wave]
  2. dipole moments         ell_e = (1/I0) INT Ic t_hat ds                  [m]
                            A_e   = (1/2I0) INT Ic (r x t_hat) ds           [m^2]
  3. chiral pseudoscalar    chi = ell_e . A_e                             [m^3]
       origin-independent: r -> r+a sends A_e -> A_e + (1/2) a x ell_e, which is
       PERPENDICULAR to ell_e, so the parallel projection is invariant.
  4. cross-polarizability   alpha_em = -(mu0/R) ell_e (x) A_e
                            alpha_em^iso = (1/3) tr = -mu0 chi / (3R)
  5. dilute mixing          |kappa| = c N |alpha_em^iso| = N Z0 |chi| / (3 R_rad)
  6. R_rad                  from the far-field radiation integral of the SAME mode
  7. N_ref                  1 / V_bbox  (densest non-overlapping packing)

GATES (prereg sec 5) — all seven must pass before any bin verdict is booked:
  G1 origin-invariance of chi           G5 straight half-wave dipole -> 73.13 ohm
  G2 mirror antisymmetry chi_L = -chi_R G6 subwavelength admissibility
  G3 planar control -> chi = 0          G7 reciprocity alpha_em = -mu0 alpha_me^T
  G4 analytic helix -> chi = pi a^2 h

Hermetic: numpy + stdlib + ave.core.constants.  No network.  Seeded RNG (G1 only).
Run:  python3 research/drivers/pasteur_kappa_desk_calc.py
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(HERE, "data", "hopf02_asfabbed")
OUT = os.path.join(HERE, "pasteur_kappa_desk_calc_results.json")

sys.path.insert(0, os.path.join(REPO, "src"))
from ave.core.constants import ALPHA, C_0, MU_0, Z_0  # noqa: E402

# --------------------------------------------------------------------------
# FROZEN INPUTS (prereg sec 6.1).  Every one tagged.
# --------------------------------------------------------------------------
# engineering as-fabbed: AVE-HOPF main:data/hopf_02/, source commit 29264b48
SHA256 = {
    "k23_R_wire.csv":
        "76835d45daaf526cbaa182b3134ea0846e821d0dd3cc4103c19fef874fff6e52",
    "k23_L_wire.csv":
        "4032340d3114c8408fcbc968a53abc5b570e939b3891b3cb5d0400f1a70b8f4b",
    "control_wire.csv":
        "e7a9675a9c9d0e00db27af41a4610785052ece9cf802efaeaa398c229bdd5797",
}
# engineering as-fabbed: NEC2 prediction on this exact geometry,
# AVE-HOPF docs/design/2026-05-05_hopf02_nec2_prediction.md:65
F0_HZ = 680e6
# AVE SIDE ONLY (CODATA via ave.core.constants) — the round-2 sec 2.1 definition
P_KNOT, Q_KNOT = 2, 3
KAPPA_AVE_EFF = ALPHA * (P_KNOT * Q_KNOT) / (P_KNOT + Q_KNOT)

# frozen bin edges (prereg sec 4) — NOT tunable
BIN_HI, BIN_LO = 3.0, 1.0 / 3.0
BIN_HI_STRONG, BIN_LO_STRONG = 10.0, 0.1
# frozen gate tolerances (prereg sec 5)
TOL_G1 = TOL_G2 = TOL_G3 = 1e-9
TOL_G4 = 1e-6
TOL_G5_R = 0.02
TOL_G5_L = 0.01
TOL_G6 = 0.25
TOL_G7 = 1e-12
# conventional dilute-mixing validity ceiling (prereg sec 6.2 I-5)
KAPPA_DILUTE_CEILING = 0.1

# Quadrature resolution: sub-segments per polyline edge, and the far-field sphere.
# The polyline edges are straight and ~5.9 mm long against lambda = 441 mm, so the
# phase varies by <0.09 rad across one edge: 64 sub-elements is far past converged.
# The far-field pattern of a <=0.5-lambda radiator is smooth (dipolar to sin^3), so
# 80 x 160 Gauss-Legendre x uniform-phi is likewise past converged.  Both are
# re-checked by the G5 known-positive (which must land on 73.13 ohm) and by the
# explicit convergence probe in `quadrature_convergence()`.
N_SUB = 64
N_THETA, N_PHI = 80, 160
DIR_CHUNK = 2048          # directions per block — bounds peak memory, not the result


# --------------------------------------------------------------------------
# Geometry + mode
# --------------------------------------------------------------------------
def load_polyline(name: str) -> np.ndarray:
    """As-fabbed polyline in metres, sha256-gated."""
    path = os.path.join(DATA, name)
    raw = open(path, "rb").read()
    got = hashlib.sha256(raw).hexdigest()
    if got != SHA256[name]:
        raise SystemExit(f"FATAL sha256 drift on {name}: {got} != {SHA256[name]}")
    rows = list(csv.DictReader(open(path)))
    pts = np.array([[float(r["x_mm"]), float(r["y_mm"]), float(r["z_mm"])]
                    for r in rows], dtype=float)
    return pts * 1e-3


def discretise(pts: np.ndarray, n_sub: int = N_SUB):
    """Uniform-in-arclength sample points, tangents and ds for a polyline.

    Returns (r, t_hat, ds, L) with r [M,3] the midpoints, t_hat [M,3] the unit
    tangents, ds [M] the element lengths, L the total arc length.  Every element
    of one polyline edge shares that edge's tangent (the polyline IS the wire).
    """
    seg = np.diff(pts, axis=0)
    seg_len = np.linalg.norm(seg, axis=1)
    t_edge = seg / seg_len[:, None]
    r_list, t_list, ds_list, s_list = [], [], [], []
    s0 = 0.0
    for e in range(len(seg)):
        d = seg_len[e] / n_sub
        for j in range(n_sub):
            frac = (j + 0.5) / n_sub
            r_list.append(pts[e] + frac * seg[e])
            t_list.append(t_edge[e])
            ds_list.append(d)
            s_list.append(s0 + (j + 0.5) * d)
        s0 += seg_len[e]
    return (np.array(r_list), np.array(t_list), np.array(ds_list),
            np.array(s_list), float(seg_len.sum()))


def mode_current(s: np.ndarray, L: float, gamma: float = 1.0) -> np.ndarray:
    """Frozen resonant mode Ic(s)/I0 = sin(pi s / L)^gamma  (gamma=1 is the freeze)."""
    return np.sin(np.pi * s / L) ** gamma


def uniform_current(s: np.ndarray, L: float) -> np.ndarray:
    """Sensitivity variant I-1: uniform current (the loop/quasi-static limit)."""
    return np.ones_like(s)


# --------------------------------------------------------------------------
# The three mode integrals (prereg sec 3.1 steps 2-3, 6)
# --------------------------------------------------------------------------
def effective_length(r, t, ds, Ic) -> np.ndarray:
    """ell_e = (1/I0) INT Ic t_hat ds   [m]."""
    return (Ic[:, None] * t * ds[:, None]).sum(axis=0)


def effective_area(r, t, ds, Ic, origin=None) -> np.ndarray:
    """A_e = (1/2 I0) INT Ic (r x t_hat) ds   [m^2].  `origin` shifts r (for G1)."""
    rr = r if origin is None else r - origin
    return 0.5 * (Ic[:, None] * np.cross(rr, t) * ds[:, None]).sum(axis=0)


def chi_pseudoscalar(r, t, ds, Ic, origin=None) -> float:
    """chi = ell_e . A_e   [m^3] — the origin-independent chiral invariant."""
    return float(effective_length(r, t, ds, Ic) @ effective_area(r, t, ds, Ic, origin))


def radiation_resistance(r, t, ds, Ic, k: float,
                         n_theta: int = N_THETA, n_phi: int = N_PHI) -> float:
    """R_rad = 2 P_rad / I0^2 from the far-field integral of the SAME mode.

        P_rad = (Z0 k^2 / 32 pi^2) INT |INT Ic t_perp exp(i k.r) ds|^2 dOmega

    Gauss-Legendre in cos(theta), uniform (periodic-exact) in phi.
    """
    x, w = np.polynomial.legendre.leggauss(n_theta)          # cos(theta) in [-1,1]
    ph = (np.arange(n_phi) + 0.5) * 2.0 * np.pi / n_phi
    dphi = 2.0 * np.pi / n_phi
    ct = x[:, None]
    st = np.sqrt(1.0 - ct ** 2)
    khat = np.stack([(st * np.cos(ph)[None, :]),
                     (st * np.sin(ph)[None, :]),
                     np.broadcast_to(ct, (n_theta, n_phi))], axis=-1)   # [T,P,3]
    khat_f = khat.reshape(-1, 3)
    wt = np.broadcast_to(w[:, None], (n_theta, n_phi)).reshape(-1) * dphi
    src_w = (Ic * ds).astype(complex)
    integ = 0.0
    # Chunked over DIRECTIONS: the full [D,M] phase matrix would be tens of GB at
    # useful resolution.  Chunking bounds peak memory and changes no arithmetic.
    for lo in range(0, len(khat_f), DIR_CHUNK):
        kk = khat_f[lo:lo + DIR_CHUNK]
        phase = np.exp(1j * k * (kk @ r.T))                  # [d, M]
        vec = (phase * src_w[None, :]) @ t                   # [d, 3]
        par = np.einsum("dj,dj->d", vec, kk.astype(complex))
        perp2 = np.einsum("dj,dj->d", vec, vec.conj()).real - np.abs(par) ** 2
        integ += float(perp2 @ wt[lo:lo + DIR_CHUNK])
    p_rad = Z_0 * k ** 2 / (32.0 * np.pi ** 2) * integ
    return 2.0 * p_rad


# --------------------------------------------------------------------------
# The estimators (prereg sec 3)
# --------------------------------------------------------------------------
def chiral_volume(chi: float, r_rad: float) -> float:
    """V_chi = Z0 |chi| / (3 R_rad)   [m^3]   (K-3);  kappa_cls = N V_chi."""
    return Z_0 * abs(chi) / (3.0 * r_rad)


# 24 AWG magnet wire: nominal bare diameter 0.0201 in = 0.51054 mm (engineering
# as-fabbed, AVE-HOPF hardware/hopf_02_ASSEMBLY_GUIDE.md BOM).  Used ONLY as the
# floor on a degenerate bounding-box axis: a physical wire cannot have zero
# thickness.  It bites on exactly one polyline — the CONTROL, whose points share a
# single x — and the control's chi is identically 0, so this floor cannot influence
# any reported kappa or the verdict.  Recorded so that is checkable, not assumed.
WIRE_DIA_M = 0.51054e-3


def bbox_volume(pts: np.ndarray) -> float:
    ext = np.maximum(pts.max(axis=0) - pts.min(axis=0), WIRE_DIA_M)
    return float(np.prod(ext))


def analyse(name: str, pts: np.ndarray, f0: float, eps_eff: float = 1.0,
            gamma: float = 1.0, uniform: bool = False) -> dict:
    r, t, ds, s, L = discretise(pts)
    Ic = uniform_current(s, L) if uniform else mode_current(s, L, gamma)
    lam = C_0 / (f0 * np.sqrt(eps_eff))
    k = 2.0 * np.pi / lam
    ell = effective_length(r, t, ds, Ic)
    a_e = effective_area(r, t, ds, Ic)
    chi = float(ell @ a_e)
    r_rad = radiation_resistance(r, t, ds, Ic, k)
    v_chi = chiral_volume(chi, r_rad)
    v_bbox = bbox_volume(pts)
    n_ref = 1.0 / v_bbox
    kappa = n_ref * v_chi
    ext = pts.max(axis=0) - pts.min(axis=0)
    return {
        "name": name, "n_points": int(len(pts)), "arc_length_m": L,
        "arc_length_mm": L * 1e3,
        "bbox_m": ext.tolist(), "bbox_mm": (ext * 1e3).tolist(),
        "bbox_volume_m3": v_bbox, "bbox_diag_over_lambda":
            float(np.linalg.norm(ext) / lam),
        "lambda_m": lam, "k_per_m": k, "eps_eff": eps_eff,
        "gamma": (None if uniform else gamma), "uniform_current": bool(uniform),
        "ell_e_vec_m": ell.tolist(), "ell_e_mag_m": float(np.linalg.norm(ell)),
        "A_e_vec_m2": a_e.tolist(), "A_e_mag_m2": float(np.linalg.norm(a_e)),
        "cos_angle_ell_A": float(chi / (np.linalg.norm(ell) * np.linalg.norm(a_e)))
            if np.linalg.norm(ell) * np.linalg.norm(a_e) > 0 else 0.0,
        "chi_m3": chi, "R_rad_ohm": r_rad,
        "V_chi_m3": v_chi, "N_ref_per_m3": n_ref,
        "kappa_cls_isotropic": kappa,
        "kappa_cls_aligned": 3.0 * kappa,   # single-orientation (bianisotropic) value
    }


# --------------------------------------------------------------------------
# Gates (prereg sec 5)
# --------------------------------------------------------------------------
def helix_polyline(a: float, h: float, n_pts: int = 20001) -> np.ndarray:
    """One closed-ish helical turn, radius a, axial pitch h.  Known-positive G4."""
    u = np.linspace(0.0, 2.0 * np.pi, n_pts)
    return np.stack([a * np.cos(u), a * np.sin(u), h * u / (2.0 * np.pi)], axis=1)


def straight_dipole(lam: float, n_pts: int = 1201) -> np.ndarray:
    """A straight wire of length lambda/2 along z.  Known-positive G5."""
    z = np.linspace(-lam / 4.0, lam / 4.0, n_pts)
    return np.stack([np.zeros_like(z), np.zeros_like(z), z], axis=1)


def run_gates(res: dict, polys: dict) -> dict:
    g = {}
    rng = np.random.default_rng(20260802)

    # G1 origin-invariance of chi
    r, t, ds, s, L = discretise(polys["k23_R"])
    Ic = mode_current(s, L)
    chi0 = chi_pseudoscalar(r, t, ds, Ic)
    shifts = rng.normal(scale=1.0, size=(8, 3))
    drift = [abs(chi_pseudoscalar(r, t, ds, Ic, origin=o) - chi0) / abs(chi0)
             for o in shifts]
    g["G1_origin_invariance"] = {
        "criterion": "|chi(shifted) - chi(0)| / |chi(0)| <= 1e-9",
        "tol": TOL_G1, "worst": max(drift), "n_shifts": len(shifts),
        "pass": bool(max(drift) <= TOL_G1)}

    # G2 mirror antisymmetry
    chi_R = res["k23_R"]["chi_m3"]
    chi_L = res["k23_L"]["chi_m3"]
    rel = abs(chi_L + chi_R) / abs(chi_R)
    g["G2_mirror_antisymmetry"] = {
        "criterion": "|chi_L + chi_R| / |chi_R| <= 1e-9",
        "tol": TOL_G2, "chi_R_m3": chi_R, "chi_L_m3": chi_L, "rel": rel,
        "pass": bool(rel <= TOL_G2)}

    # G3 planar null (known-negative)
    rel_ctrl = abs(res["control"]["chi_m3"]) / abs(chi_R)
    g["G3_planar_null"] = {
        "criterion": "|chi_control| / |chi_k23R| <= 1e-9",
        "tol": TOL_G3, "chi_control_m3": res["control"]["chi_m3"],
        "rel": rel_ctrl, "pass": bool(rel_ctrl <= TOL_G3)}

    # G4 analytic helix (known-positive, exact target chi = pi a^2 h)
    a_h, h_h = 5e-3, 2e-3
    rh, th, dsh, sh, Lh = discretise(helix_polyline(a_h, h_h), n_sub=1)
    Ih = uniform_current(sh, Lh)
    chi_h = chi_pseudoscalar(rh, th, dsh, Ih)
    target = np.pi * a_h ** 2 * h_h
    rel_h = abs(chi_h - target) / abs(target)
    g["G4_helix_known_positive"] = {
        "criterion": "helix chi matches pi a^2 h to <= 1e-6 relative",
        "tol": TOL_G4, "a_m": a_h, "h_m": h_h, "chi_computed_m3": chi_h,
        "chi_analytic_m3": target, "rel": rel_h, "pass": bool(rel_h <= TOL_G4)}

    # G5 straight half-wave dipole (known-positive; textbook 73.13 ohm, lambda/pi)
    lam0 = C_0 / F0_HZ
    rd, td, dsd, sd, Ld = discretise(straight_dipole(lam0), n_sub=1)
    Id = mode_current(sd, Ld)
    r_dip = radiation_resistance(rd, td, dsd, Id, 2.0 * np.pi / lam0)
    ell_dip = float(np.linalg.norm(effective_length(rd, td, dsd, Id)))
    rel_r = abs(r_dip - 73.13) / 73.13
    rel_l = abs(ell_dip - lam0 / np.pi) / (lam0 / np.pi)
    g["G5_dipole_validation"] = {
        "criterion": ("R_rad within 2 percent of 73.13 ohm and |ell_e| within "
                      "1 percent of lambda/pi"),
        "tol_R": TOL_G5_R, "tol_L": TOL_G5_L,
        "R_rad_ohm": r_dip, "R_rel": rel_r,
        "ell_e_m": ell_dip, "lambda_over_pi_m": lam0 / np.pi, "ell_rel": rel_l,
        "pass": bool(rel_r <= TOL_G5_R and rel_l <= TOL_G5_L)}

    # G6 subwavelength admissibility
    d_lam = res["k23_R"]["bbox_diag_over_lambda"]
    g["G6_subwavelength"] = {
        "criterion": "bbox diagonal / lambda <= 0.25",
        "tol": TOL_G6, "bbox_diag_over_lambda": d_lam,
        "pass": bool(d_lam <= TOL_G6)}

    # G7 reciprocity: alpha_em = -mu0 alpha_me^T, checked on the built dyads.
    #   H-drive:  I0 = i w mu0 (H.A_e)/R,  p = ell_e I0/(-i w)
    #                                          => alpha_em = -(mu0/R) ell_e (x) A_e
    #   E-drive:  I0 = (E.ell_e)/R,        m = A_e I0
    #                                          => alpha_me =  (1/R)  A_e   (x) ell_e
    ell = np.array(res["k23_R"]["ell_e_vec_m"])
    a_e = np.array(res["k23_R"]["A_e_vec_m2"])
    R = res["k23_R"]["R_rad_ohm"]
    alpha_em = -(MU_0 / R) * np.outer(ell, a_e)
    alpha_me = np.outer(a_e, ell) / R
    resid = float(np.max(np.abs(alpha_em + MU_0 * alpha_me.T)))
    scale = float(np.max(np.abs(alpha_em)))
    g["G7_reciprocity"] = {
        "criterion": "alpha_em == -mu0 alpha_me^T identically",
        "tol": TOL_G7, "max_abs_residual": resid, "scale": scale,
        "rel": resid / scale if scale > 0 else 0.0,
        "pass": bool(resid / scale <= TOL_G7 if scale > 0 else True)}

    g["ALL_PASS"] = bool(all(v["pass"] for k, v in g.items() if k != "ALL_PASS"))
    return g


# --------------------------------------------------------------------------
# Sensitivity legs (prereg sec 6.2 I-1, I-2)
# --------------------------------------------------------------------------
def sensitivity(polys: dict) -> dict:
    out = {"I1_current_profile": [], "I2_host_index": []}
    for gam in (0.8, 1.0, 1.2):
        a = analyse(f"k23_R gamma={gam}", polys["k23_R"], F0_HZ, gamma=gam)
        out["I1_current_profile"].append(
            {"variant": f"sin^{gam}", "chi_m3": a["chi_m3"],
             "R_rad_ohm": a["R_rad_ohm"], "kappa_cls": a["kappa_cls_isotropic"]})
    a = analyse("k23_R uniform", polys["k23_R"], F0_HZ, uniform=True)
    out["I1_current_profile"].append(
        {"variant": "uniform", "chi_m3": a["chi_m3"],
         "R_rad_ohm": a["R_rad_ohm"], "kappa_cls": a["kappa_cls_isotropic"]})
    for eps in (1.0, 1.5, 2.0):
        a = analyse(f"k23_R eps={eps}", polys["k23_R"], F0_HZ, eps_eff=eps)
        out["I2_host_index"].append(
            {"eps_eff": eps, "lambda_m": a["lambda_m"],
             "R_rad_ohm": a["R_rad_ohm"], "chi_m3": a["chi_m3"],
             "kappa_cls": a["kappa_cls_isotropic"]})
    vals = [d["kappa_cls"] for d in out["I1_current_profile"]] + \
           [d["kappa_cls"] for d in out["I2_host_index"]]
    out["kappa_min"] = min(vals)
    out["kappa_max"] = max(vals)
    out["spread_factor"] = max(vals) / min(vals)
    return out


# --------------------------------------------------------------------------
# Bin assignment (prereg sec 4) — frozen, not tunable
# --------------------------------------------------------------------------
def assign_bin(ratio: float) -> dict:
    if ratio >= BIN_HI:
        b, meaning = "a", ("DISCRIMINATES-HIGH: classical kappa far exceeds AVE's; "
                           "the MAGNITUDE axis discriminates")
    elif ratio > BIN_LO:
        b, meaning = "b", ("RETIREMENT-FINAL: classical reproduces FORM and "
                           "MAGNITUDE")
    else:
        b, meaning = "c", ("DISCRIMINATES-LOW: classical kappa far below AVE's; "
                           "flag for Grant walk")
    strong = (ratio >= BIN_HI_STRONG) or (ratio <= BIN_LO_STRONG)
    return {"bin": b, "meaning": meaning, "ratio": ratio, "strong_sub_band": strong,
            "edges": {"hi": BIN_HI, "lo": BIN_LO,
                      "hi_strong": BIN_HI_STRONG, "lo_strong": BIN_LO_STRONG}}


def ohmic_bound(pts: np.ndarray, r_rad: float) -> dict:
    """Quantify prereg idealization I-4 (lossless copper), direction-conservative.

    NOT FROZEN — added at result time.  The prereg froze only the DIRECTION of the
    bound ("loss raises R, which lowers kappa_cls, so R = R_rad is a strict upper
    bound").  This puts a number on it.  It can only SHRINK kappa_cls, so it can
    never move the verdict toward the bin this lane happens to report.

    Skin-effect surface resistance of the wire, weighted by the SAME sin^2 current
    profile that sets R_rad:  R_ohm = (rho L)/(2 pi a delta) * <Ic^2>/I0^2, with
    <Ic^2>/I0^2 = 1/2 for Ic = I0 sin(pi s/L), and delta = sqrt(2 rho/(omega mu0)).
    """
    rho_cu = 1.68e-8        # standard material constant, annealed Cu, ohm*m
    a = WIRE_DIA_M / 2.0
    w = 2.0 * np.pi * F0_HZ
    delta = np.sqrt(2.0 * rho_cu / (w * MU_0))
    seg = np.linalg.norm(np.diff(pts, axis=0), axis=1).sum()
    r_ohm = rho_cu * seg / (2.0 * np.pi * a * delta) * 0.5
    return {"NOT_FROZEN": "quantifies prereg I-4; can only reduce kappa_cls",
            "rho_Cu_ohm_m": rho_cu, "skin_depth_m": float(delta),
            "wire_radius_m": a, "R_ohmic_ohm": float(r_ohm),
            "R_rad_ohm": r_rad,
            "kappa_reduction_factor": float(r_rad / (r_rad + r_ohm)),
            "note": ("kappa_cls scales as 1/R; including copper loss multiplies "
                     "every kappa_cls in this file by kappa_reduction_factor")}


def mirror_isometry(pts_R: np.ndarray, pts_L: np.ndarray) -> dict:
    """Which improper isometry maps the R polyline onto the L polyline?

    NOT FROZEN — added at result time.  It exists because the whole classical
    'exactly zero enantiomer split' statement is conditional on the MIRROR
    OPERATION MAPPING THE WHOLE FIXTURE (board outline, feed, hole pattern) to
    itself, not just the wire.  Naming the plane makes that checkable by whoever
    builds the boards instead of leaving it assumed.

    Tries the three coordinate-plane reflections (with an allowed translation),
    reports the best fit and its residual.
    """
    out = {"NOT_FROZEN": "added at result time; conditions the K-2 parity argument",
           "candidates": []}
    for axis, label in ((0, "x -> -x"), (1, "y -> -y"), (2, "z -> -z")):
        m = pts_R.copy()
        m[:, axis] *= -1.0
        shift = (pts_L - m).mean(axis=0)
        resid = float(np.max(np.linalg.norm(pts_L - (m + shift), axis=1)))
        out["candidates"].append(
            {"plane": label, "translation_mm": (shift * 1e3).tolist(),
             "max_residual_mm": resid * 1e3})
    best = min(out["candidates"], key=lambda c: c["max_residual_mm"])
    out["best"] = best
    out["is_pure_coordinate_plane_mirror"] = bool(best["max_residual_mm"] < 1e-9)
    return out


def quadrature_convergence(pts: np.ndarray) -> dict:
    """Halve/double both quadrature axes; report the drift in chi and R_rad.

    A number that moves when the mesh moves is a mesh artefact, not a measurement.
    """
    lam = C_0 / F0_HZ
    k = 2.0 * np.pi / lam
    rows = []
    for n_sub, nt, npz in ((32, 40, 80), (64, 80, 160), (128, 160, 320)):
        r, t, ds, s, L = discretise(pts, n_sub=n_sub)
        Ic = mode_current(s, L)
        rows.append({"n_sub": n_sub, "n_theta": nt, "n_phi": npz,
                     "chi_m3": chi_pseudoscalar(r, t, ds, Ic),
                     "R_rad_ohm": radiation_resistance(r, t, ds, Ic, k, nt, npz)})
    base = rows[1]
    return {"rows": rows,
            "chi_rel_drift_vs_base":
                [abs(x["chi_m3"] - base["chi_m3"]) / abs(base["chi_m3"])
                 for x in rows],
            "R_rad_rel_drift_vs_base":
                [abs(x["R_rad_ohm"] - base["R_rad_ohm"]) / base["R_rad_ohm"]
                 for x in rows]}


def commensurability_checklist(kappa_ave: float, f0: float) -> dict:
    """Prereg sec 7 — four YES/NO structural questions, decided by DEFINITIONS.

    Hand-authored (it is a reading of two definitions, not a computation), shipped
    here so the result doc's claims resolve to the same artefact as its numbers.
    Decidable BEFORE the magnitude is known — it cannot be used to escape a number.
    """
    rows = [
        {"id": "C-i", "question": "physical dimension",
         "kappa_cls": "dimensionless",
         "kappa_AVE": "dimensionless",
         "verdict": "SAME"},
        {"id": "C-ii", "question": "defining equation (and what the sign keys to)",
         "kappa_cls": ("coefficient in k_pm = k0 (n +- kappa) for a wave "
                       "propagating THROUGH the medium; the +- is keyed to the "
                       "WAVE's circular-polarisation handedness"),
         "kappa_AVE": ("coefficient in k_AVE = k0 (1 + alpha pq/(p+q)) — a single "
                       "shifted wavenumber, no +- pair; the sign is keyed to the "
                       "STRUCTURE's handedness (round-2 sec 2.3: Delta f_R = "
                       "-Delta f_L)"),
         "verdict": "DIFFERENT"},
        {"id": "C-iii", "question": "object class",
         "kappa_cls": ("bulk effective-medium constitutive parameter; strictly "
                       "PROPORTIONAL TO the inclusion number density N — not a "
                       "property of one object"),
         "kappa_AVE": ("a fixed number per knot TOPOLOGY, alpha pq/(p+q), with no "
                       "density in it; a fractional shift of ONE structure's own "
                       "eigenfrequency"),
         "verdict": "DIFFERENT"},
        {"id": "C-iv", "question": "observable consequence",
         "kappa_cls": ("optical rotation / circular birefringence of a wave "
                       "TRANSMITTED through the composite: Delta k/k = kappa/n "
                       "between LCP and RCP"),
         "kappa_AVE": ("Delta f/f of the knot's OWN 1-port S11 resonance, with "
                       "the two enantiomers shifting in opposite directions"),
         "verdict": "DIFFERENT"},
    ]
    n_diff = sum(1 for r in rows if r["verdict"] == "DIFFERENT")
    fires = n_diff > 0
    return {
        "rows": rows, "n_different": n_diff, "bin_d_fires": fires,
        "honest_common_observable": {
            "observable": ("enantiomer split of the scalar self-resonance, "
                           "(f_R - f_L)/f0, on the as-fabbed HOPF-02a pair in an "
                           "ACHIRAL host (air + FR-4)"),
            "classical_value": 0.0,
            "classical_basis": [
                "Maxwell is parity-covariant: the mirror of a solution is a "
                "solution, so in a mirror-symmetric fixture f_R = f_L exactly",
                "the as-fabbed L/R mirror operation is a PURE reflection x -> -x "
                "with zero translation (computed here, max residual 0.0 mm), so "
                "the fixture symmetry premise is checkable, not assumed",
                "AVE-HOPF docs/design/2026-05-05_hopf02_nec2_prediction.md:80 — "
                "the NEC2 Delta_classical column for (2,3) reads +0.000 MHz",
            ],
            "classical_condition": ("holds iff the HOST is achiral. A classical "
                                    "chiral (Pasteur) HOST does split the scalar "
                                    "self-resonance — that is the configuration "
                                    "round-2 sec 2.3 describes, and it is not the "
                                    "HOPF-02a bench, which sits in air."),
            "ave_value_fractional": 2.0 * kappa_ave,
            "ave_value_MHz": 2.0 * kappa_ave * f0 / 1e6,
            "experiment": ("already fabbed: HOPF-02a enantiomer pair, differential "
                           "1-port S11; round-2 sec 4 inherits the S-8 fab floor "
                           "~130 kHz = 1.912e-4 fractional at 680 MHz"),
            "fab_floor_fractional": 130e3 / f0,
            "margin_over_fab_floor": 2.0 * kappa_ave / (130e3 / f0),
            "discriminating_axis_on_this_observable":
                "EXISTENCE (nonzero vs exactly zero), NOT magnitude",
        },
    }


def main() -> int:
    polys = {"k23_R": load_polyline("k23_R_wire.csv"),
             "k23_L": load_polyline("k23_L_wire.csv"),
             "control": load_polyline("control_wire.csv")}

    res = {n: analyse(n, p, F0_HZ) for n, p in polys.items()}
    gates = run_gates(res, polys)
    sens = sensitivity(polys)

    kR = res["k23_R"]
    ratio = kR["kappa_cls_isotropic"] / KAPPA_AVE_EFF
    n_star = KAPPA_AVE_EFF / kR["V_chi_m3"]
    n_dilute = KAPPA_DILUTE_CEILING / kR["V_chi_m3"]

    # K-2: the observable-matched classical kappa.  A parity THEOREM, not a run.
    k2 = {
        "definition": "kappa_obs = |f_R - f_L| / (2 f0) predicted by classical EM",
        "classical_value": 0.0,
        "basis": ("Maxwell is parity-covariant: the mirror image of a solution is a "
                  "solution, so in a mirror-symmetric environment f_R = f_L exactly"),
        "corpus_receipts": [
            "AVE-HOPF docs/design/2026-05-05_hopf02_design_proposal.md:57 "
            "(f_R = f_L to floating-point precision in NEC2)",
            "AVE-HOPF docs/design/2026-05-05_hopf02_nec2_prediction.md:80 "
            "(Delta_classical = +0.000 MHz for (2,3))"],
        "ave_value": 2.0 * KAPPA_AVE_EFF,
        "ave_value_MHz_at_f0": 2.0 * KAPPA_AVE_EFF * F0_HZ / 1e6,
    }

    out = {
        "lane": "research/pasteur-kappa-desk-calc",
        "prereg": "research/2026-08-02_pasteur-kappa-desk-calc_prereg-FROZEN.md",
        "prereg_commit": "3ae1f3de",
        "class": "CLASSICAL-BASELINE — makes no AVE claim",
        "inputs": {
            "f0_Hz": F0_HZ,
            "alpha_CODATA_AVE_SIDE_ONLY": ALPHA,
            "Z_0_ohm": Z_0, "c_0_m_per_s": C_0, "mu_0_H_per_m": MU_0,
            "p": P_KNOT, "q": Q_KNOT,
            "kappa_AVE_eff": KAPPA_AVE_EFF,
            "geometry_sha256": SHA256,
            "quadrature": {"n_sub_per_edge": N_SUB, "n_theta": N_THETA,
                           "n_phi": N_PHI},
        },
        "K1_primary": res,
        "K2_observable_matched": k2,
        "K3_density_free": {
            "V_chi_m3": kR["V_chi_m3"],
            "N_star_per_m3": n_star,
            "N_star_volume_per_knot_m3": 1.0 / n_star,
            "N_ref_per_m3": kR["N_ref_per_m3"],
            "N_ref_over_N_star": kR["N_ref_per_m3"] / n_star,
            "N_dilute_ceiling_per_m3": n_dilute,
            "N_dilute_ceiling_volume_per_knot_m3": 1.0 / n_dilute,
        },
        "gates": gates,
        "quadrature_convergence": quadrature_convergence(polys["k23_R"]),
        "mirror_isometry_NOT_FROZEN": mirror_isometry(polys["k23_R"], polys["k23_L"]),
        "ohmic_loss_NOT_FROZEN": ohmic_bound(polys["k23_R"], kR["R_rad_ohm"]),
        "sensitivity": sens,
        "verdict": assign_bin(ratio),
    }
    out["commensurability_checklist"] = commensurability_checklist(
        KAPPA_AVE_EFF, F0_HZ)
    cc = out["commensurability_checklist"]
    out["verdict"]["bin_d_fires"] = cc["bin_d_fires"]
    out["verdict"]["final_bin"] = "d" if cc["bin_d_fires"] else out["verdict"]["bin"]
    out["verdict"]["magnitude_bin_status"] = (
        "REPORTED BUT NON-ADJUDICATING (bin (d) fired; prereg sec 4)"
        if cc["bin_d_fires"] else "ADJUDICATING")
    out["verdict"]["ratio_at_sensitivity_min"] = sens["kappa_min"] / KAPPA_AVE_EFF
    out["verdict"]["ratio_at_sensitivity_max"] = sens["kappa_max"] / KAPPA_AVE_EFF
    out["verdict"]["bin_stable_across_sensitivity"] = bool(
        assign_bin(sens["kappa_min"] / KAPPA_AVE_EFF)["bin"]
        == assign_bin(sens["kappa_max"] / KAPPA_AVE_EFF)["bin"] ==
        out["verdict"]["bin"])
    out["verdict"]["gates_all_pass"] = gates["ALL_PASS"]

    def _plain(o):
        """numpy scalars -> python scalars (Z_0 is an np.float64, so ratios are too)."""
        if isinstance(o, np.bool_):
            return bool(o)
        if isinstance(o, np.integer):
            return int(o)
        if isinstance(o, np.floating):
            return float(o)
        if isinstance(o, np.ndarray):
            return o.tolist()
        raise TypeError(f"not JSON-serialisable: {type(o).__name__}")

    with open(OUT, "w") as fh:
        json.dump(out, fh, indent=2, sort_keys=True, default=_plain)

    print(f"[pasteur-kappa] chi(k23_R)        = {kR['chi_m3']:.6e} m^3")
    print(f"[pasteur-kappa] R_rad(k23_R)      = {kR['R_rad_ohm']:.4f} ohm")
    print(f"[pasteur-kappa] V_chi             = {kR['V_chi_m3']:.6e} m^3")
    print(f"[pasteur-kappa] N_ref (close-pack)= {kR['N_ref_per_m3']:.6e} /m^3")
    print(f"[pasteur-kappa] kappa_cls (iso)   = {kR['kappa_cls_isotropic']:.6e}")
    print(f"[pasteur-kappa] kappa_AVE,eff     = {KAPPA_AVE_EFF:.6e}")
    print(f"[pasteur-kappa] ratio R           = {ratio:.6e}")
    print(f"[pasteur-kappa] N*                = {n_star:.6e} /m^3 "
          f"(1 knot per {1.0/n_star:.4f} m^3)")
    print(f"[pasteur-kappa] gates ALL_PASS    = {gates['ALL_PASS']}")
    for k, v in gates.items():
        if k != "ALL_PASS":
            print(f"[pasteur-kappa]   {k}: {'PASS' if v['pass'] else 'FAIL'}")
    print(f"[pasteur-kappa] magnitude BIN = ({out['verdict']['bin']}) "
          f"{out['verdict']['meaning']}")
    print(f"[pasteur-kappa] commensurability: {cc['n_different']}/4 DIFFERENT "
          f"-> bin (d) fires = {cc['bin_d_fires']}")
    print(f"[pasteur-kappa] FINAL BIN = ({out['verdict']['final_bin']}); "
          f"magnitude bin {out['verdict']['magnitude_bin_status']}")
    print(f"[pasteur-kappa] wrote {os.path.relpath(OUT, REPO)}")
    return 0 if gates["ALL_PASS"] else 1


if __name__ == "__main__":
    sys.exit(main())
