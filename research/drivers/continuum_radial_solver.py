"""Continuum radial-acoustic solver — STAGE 1 (INSTRUMENT CERTIFICATION ONLY).

Prereg-file: research/2026-07-28_continuum-radial-solver-stage1_prereg-FROZEN.md
Charter:     research/2026-07-21_continuum-radial-solver_CHARTER.md  (#789)

★ STAGE 1 BANKS NO PHYSICS VERDICT. Every physics-shaped number emitted by this
  driver is an INSTRUMENT-LIVENESS DEMONSTRATION and carries that label.

Formulation (Grant D3 = the charter's recommendation, T1 (a)+(c)):
  * SOLVER 1 (PRIMARY)  — frequency-domain transfer matrix through the radial
    profile.  Exact analytic layer solutions; no time stepping, hence NO CFL
    floor at k*r_core << 1 (the regime the lattice could not reach).
  * SOLVER 2 (BACKSTOP) — analytic matched asymptotics: the deep-quasistatic
    limit is a STATIC (Lame) interior matched onto a radiating monopole, giving
    the k-independent closed form  rho_N -> |B_caged / B_uncaged|^2.

Sector / regime header (prereg sec 0):
  SECTOR A1 (dilatation / compression), n = 0 monopole radial channel.
  MODE classical lossless-reactive continuum (Ax3, no Re(Z) term).
  REGIME deep-quasistatic k*r_core << 1.
  grade-frame: Eulerian, imposed (not self-bound); the instrument hosts no
  field-generated co-moving grade.

D1 (the sector-crossed c^2) is HELD by Grant.  Nothing in this driver evaluates
a c^2: the trapped-energy column is carried SYMBOLICALLY (see sec 10 of the
prereg and `two_term_rho_report` below).  No SM/GR default (no c_light, no
unlabeled c) is used anywhere (R8).

Engine `src/ave` is BYTE-UNTOUCHED; `ave.core.constants` is imported read-only.
"""

from __future__ import annotations

import hashlib
import json
import os
import time
from typing import Callable, Sequence

import numpy as np
from scipy.special import hankel1, jv, yv

# --- canonical constants: imported, never hard-coded (ave-canonical-source) ---
from ave.core.constants import N_NU  # nu_Hill = 2/7 (Axiom 2; K = 2G isotropic VRH)

HERE = os.path.dirname(os.path.abspath(__file__))
VESSEL_JSON = os.path.join(HERE, "vessel_state_rve_results.json")
OUT_JSON = os.path.join(HERE, "continuum_radial_solver_stage1_results.json")

# ----------------------------------------------------------------------------
# FROZEN instrument geometry + numerics (prereg sec 5; I15 ENGINEERING CHOICE)
# ----------------------------------------------------------------------------
R_CORE = 1.0
R_S = 0.30          # source surface
W_SHELL = 0.30      # graded-shell width: grade band r in [0.70, 1.00]
S_RAIL = 1e-3       # baseline rail depth of the grade
N_SHELL = 256       # frozen layer count
R_MATCH = 4.0       # matching radius (in units of r_core)
N_EXT = 8           # uniform exterior annulus layers r_core -> R_match

BAND = (1e-8, 1e-6, 1e-4, 1e-3, 1e-2, 1e-1, 0.3, 1.0, 3.0, 4.0)
QUASISTATIC_TOP = 1e-3     # no exponent/quasistatic read above this (R6-iii)
SOURCES = ("displacement", "traction")

FROZEN_STRINGS = {
    "grade_frame": (
        "grade-frame: Eulerian, imposed (not self-bound); the instrument hosts "
        "no field-generated co-moving grade"
    ),
    "source_fitting": (
        "source fitting reported on BOTH axes (prescribed displacement / "
        "prescribed traction); the physical fitting is Grant-routed and not "
        "picked here"
    ),
    "no_verdict": (
        "stage 1 banks NO physics verdict; every physics-shaped number in these "
        "outputs is an INSTRUMENT-LIVENESS DEMONSTRATION and is labelled "
        "DEMONSTRATION - no verdict banked"
    ),
    "n1_absent": (
        "n=0 monopole channel only; the n=1 dipole channel (F2 displaced-source "
        "p, and the structural added-mass term of rho_eff) is NOT built in "
        "stage 1"
    ),
    "op14": (
        "Op14 saturation enters as a static constitutive grade S(A); the "
        "kernel-knee marginality is NOT hosted"
    ),
    "continuum_scope": (
        "the continuum radial channel is a CONTINUUM representation whose "
        "constitutive inputs are lattice-measured; it is not a discretization "
        "of the srs stencil and carries no K4 connectivity claim"
    ),
    "d5_shape": (
        "the D5 vessel-state EXTREMA are lattice-measured; the radial SHAPE "
        "between them is an ENGINEERING CHOICE - #796 shipped no resolved "
        "radial profile, and its C-V shell reconstruction is corroborative-only "
        "by its own grading"
    ),
    "mixed_provenance": (
        "any stage-1 output that carries the #796 r_Z cites it as "
        "MIXED-provenance (K derived, rho assumed at rho_eff/rho_0 = 1); the "
        "#796 rho half is UNRESOLVED and stage 1 does not repair it"
    ),
    "beta_symbolic": (
        "beta = (u_trapped * P) / (rho_0 * c_x^2) - c_x SYMBOLIC, D1 HELD; "
        "no c^2 evaluated"
    ),
    "structural_not_built": (
        "structural dipole term NOT BUILT (n=1 channel absent in stage 1)"
    ),
    "tag_class": (
        "stage-1 outputs are CONSISTENCY-class (analytic-limit reproduction) or "
        "ENGINEERING-class (numerics); no manifestation- or emergence-class "
        "claim is made"
    ),
}

# ----------------------------------------------------------------------------
# Cold medium — LATTICE-MEASURED inputs (I11), read from the shipped #796 JSON
# ----------------------------------------------------------------------------


def load_cold_medium() -> dict:
    with open(VESSEL_JSON) as fh:
        j = json.load(fh)
    c_p = j["spectral_cold"]["cP"]
    c_s = j["spectral_cold"]["cS"]
    rho0 = 1.0                       # I12: dimensionless unit choice
    crr0 = rho0 * c_p ** 2
    g0 = rho0 * c_s ** 2
    k0 = crr0 - 4.0 * g0 / 3.0
    nu_implied = (c_p ** 2 - 2 * c_s ** 2) / (2 * (c_p ** 2 - c_s ** 2))
    return {
        "cP": c_p,
        "cS": c_s,
        "cP_over_cS": c_p / c_s,
        "rho0": rho0,
        "C_rr_0": crr0,
        "G_0": g0,
        "K_0": k0,
        "nu_implied_from_lattice_speeds": nu_implied,
        "nu_Hill_canon_N_NU": float(N_NU),
        "nu_rel_dev_vs_canon": (nu_implied - float(N_NU)) / float(N_NU),
        "source": "research/drivers/vessel_state_rve_results.json (spectral_cold)",
        "tag": "[lattice-measured] (charter I2 / prereg I11); ratio-only use",
    }


def load_d5_profile_gains() -> dict:
    """D5 (Grant): feed the MEASURED vessel profile.  Read the shipped numbers."""
    with open(VESSEL_JSON) as fh:
        j = json.load(fh)
    h = j["verdict"]["fixed_budget_headline"]
    c = j["provenance"]["constants"]
    k_a, k_s = c["k_a_RHO_STAR"], c["k_s_KS0"]
    radial_gain = h["min_kse"] / k_s
    hoop_gain = 1.0 + k_a * h["peak_A"] / k_s
    return {
        "min_kse": h["min_kse"],
        "peak_A": h["peak_A"],
        "k_a_RHO_STAR": k_a,
        "k_s_KS0": k_s,
        "eps_radial_extremum": (h["min_kse"] - k_s) / k_a,
        "eps_hoop_extremum": h["peak_A"],
        "radial_gain": radial_gain,
        "hoop_gain": hoop_gain,
        "r_Z_796_mixed_provenance": h["r_Z_structural"],
        "K_tan_over_K0_796": h["K_tan_over_K0_grown"],
        "read_from": "research/drivers/vessel_state_rve_results.json",
        "disclosure_shape": FROZEN_STRINGS["d5_shape"],
        "disclosure_mixed_provenance": FROZEN_STRINGS["mixed_provenance"],
    }


# ----------------------------------------------------------------------------
# Layer algebra — spherically orthotropic radial channel (prereg sec 2)
#   layer = (C_rr, C_rtheta, C_thetatheta + C_thetaphi, rho)
# ----------------------------------------------------------------------------


def iso_layer(k_mod: float, g_mod: float, rho: float = 1.0):
    a = k_mod + 4.0 * g_mod / 3.0
    b = k_mod - 2.0 * g_mod / 3.0
    return (a, b, a + b, rho)


def ortho_layer(k_mod: float, g_mod: float, hoop_gain: float = 1.0,
                radial_gain: float = 1.0, rho: float = 1.0):
    """R1: two radial stiffness functions -> radially varying orthotropic moduli."""
    a = k_mod + 4.0 * g_mod / 3.0
    b = k_mod - 2.0 * g_mod / 3.0
    return (a * radial_gain,
            b * np.sqrt(hoop_gain * radial_gain),
            (a + b) * hoop_gain,
            rho)


def _beta2_nu(layer):
    c_rr, c_rt, c_tt, _ = layer
    b2 = 2.0 * (c_tt - c_rt) / c_rr
    if np.iscomplexobj(b2) and abs(np.imag(b2)) <= 1e-10 * abs(np.real(b2)):
        b2 = np.real(b2)          # keep the Bessel ORDER real under a complex modulus
    return b2, np.sqrt(b2 + 0.25)


def _static_exponents(layer):
    b2, _ = _beta2_nu(layer)
    d = np.sqrt(1.0 + 4.0 * np.real(b2))
    return (-1.0 + d) / 2.0, (-1.0 - d) / 2.0


def _colnorm(m):
    d = np.array([np.linalg.norm(m[:, 0]), np.linalg.norm(m[:, 1])])
    return m / d, d


def basis_matrix(r: float, layer, omega: float, outgoing: bool = False):
    """Columns = the two independent solutions, as states y = (u, sigma_rr)."""
    c_rr, c_rt, _, rho = layer
    if omega == 0.0:
        s1, s2 = _static_exponents(layer)
        cols = [(r ** s, (c_rr * s + 2.0 * c_rt) * r ** (s - 1.0)) for s in (s1, s2)]
    else:
        _, nu = _beta2_nu(layer)
        k = omega * np.sqrt(rho / c_rr)
        x = k * r
        funcs: Sequence[Callable] = (hankel1, jv) if outgoing else (jv, yv)
        cols = []
        for fn in funcs:
            z = fn(nu, x)
            zp = fn(nu - 1.0, x) - (nu / x) * z
            u = r ** -0.5 * z
            du = -0.5 * r ** -1.5 * z + r ** -0.5 * k * zp
            cols.append((u, c_rr * du + 2.0 * c_rt * u / r))
    return np.array([[cols[0][0], cols[1][0]],
                     [cols[0][1], cols[1][1]]], dtype=complex)


def transfer(r_a: float, r_b: float, layer, omega: float):
    m_a, d_a = _colnorm(basis_matrix(r_a, layer, omega))
    m_b, d_b = _colnorm(basis_matrix(r_b, layer, omega))
    return (m_b * (d_b / d_a)) @ np.linalg.inv(m_a)


def stack_transfer(edges, layers, omega: float):
    t = np.eye(2, dtype=complex)
    for i, layer in enumerate(layers):
        t = transfer(edges[i], edges[i + 1], layer, omega) @ t
    return t


# ----------------------------------------------------------------------------
# Profile construction (frozen sec 5 geometry; log-S layer allocation)
# ----------------------------------------------------------------------------


def _shell_edges(s_rail: float, n_shell: int, uniform: bool):
    if uniform or s_rail >= 1.0:
        t = np.linspace(0.0, 1.0, n_shell + 1)
    else:
        s_j = np.exp(np.linspace(0.0, np.log(s_rail), n_shell + 1))
        t = np.sqrt((s_j - 1.0) / (s_rail - 1.0))
    return (R_CORE - W_SHELL) + t * W_SHELL


def build_profile(cold, s_rail: float = S_RAIL, shell_ortho=(1.0, 1.0),
                  n_shell: int = N_SHELL, uniform: bool = False,
                  r_match: float = R_MATCH, absorb: float = 0.0,
                  ext_grade: float = 0.0, ext_ortho=None):
    """Returns (edges, layers).  `uniform=True` is the no-cage NULL arm."""
    k0, g0 = cold["K_0"], cold["G_0"]
    edges = [R_S, R_CORE - W_SHELL]
    layers = [iso_layer(k0, g0)]
    rr = _shell_edges(s_rail, n_shell, uniform)
    for i in range(n_shell):
        r_mid = 0.5 * (rr[i] + rr[i + 1])
        t = (r_mid - (R_CORE - W_SHELL)) / W_SHELL
        s_val = 1.0 if uniform else 1.0 + (s_rail - 1.0) * t ** 2
        layer = ortho_layer(k0 * s_val, g0 * s_val, *shell_ortho)
        if absorb:
            f = 1.0 + 1j * absorb
            layer = (layer[0] * f, layer[1] * f, layer[2] * f, layer[3])
        layers.append(layer)
        edges.append(rr[i + 1])
    re = np.linspace(R_CORE, r_match, N_EXT + 1)
    for i in range(N_EXT):
        r_mid = 0.5 * (re[i] + re[i + 1])
        fac = (r_mid / R_CORE) ** (-ext_grade) if ext_grade else 1.0
        layers.append(ortho_layer(k0 * fac, g0 * fac, *ext_ortho) if ext_ortho
                      else iso_layer(k0 * fac, g0 * fac))
        edges.append(re[i + 1])
    return edges, layers


def _source_states(src: str):
    """Frozen drive: (particular state, complementary direction)."""
    if src == "displacement":
        return np.array([1.0 + 0j, 0.0]), np.array([0.0 + 0j, 1.0])
    if src == "traction":
        return np.array([0.0 + 0j, 1.0]), np.array([1.0 + 0j, 0.0])
    raise ValueError(src)


# ----------------------------------------------------------------------------
# SOLVER 2 (BACKSTOP): static Lame solve + matched asymptotics
# ----------------------------------------------------------------------------


def static_solve(edges, layers, src="displacement", amplitude: float = 1.0):
    """Infinite medium: at R_match only the DECAYING static mode survives.

    Returns (B, y_source, cond) with B the amplitude of the r^s2 (decaying) mode.
    """
    t = stack_transfer(edges, layers, 0.0)
    m_out = basis_matrix(edges[-1], layers[-1], 0.0)
    y0, y1 = _source_states(src)
    y0 = y0 * amplitude
    a = np.column_stack([t @ y1, -m_out[:, 1]])
    sol = np.linalg.solve(a, -(t @ y0))
    return sol[1], y0 + sol[0] * y1, np.linalg.cond(a)


def state_at(edges, layers, y_in, r: float, omega: float = 0.0):
    y = y_in.copy()
    for i, layer in enumerate(layers):
        r_a, r_b = edges[i], edges[i + 1]
        if r <= r_b + 1e-13:
            return transfer(r_a, r, layer, omega) @ y, layer
        y = transfer(r_a, r_b, layer, omega) @ y
    return y, layers[-1]


def div_u(r: float, layer, y):
    """Analytic dilatation from the layer's modal decomposition (static)."""
    c = np.linalg.solve(basis_matrix(r, layer, 0.0), y)
    s1, s2 = _static_exponents(layer)
    return c[0] * (s1 + 2.0) * r ** (s1 - 1.0) + c[1] * (s2 + 2.0) * r ** (s2 - 1.0)


def rho_N_matched_asymptotics(cold, src="displacement", **kw):
    """Deep-quasistatic closed form: radiated power ~ k^4 |B|^2, so the ratio is
    |B_caged/B_uncaged|^2 and is k-INDEPENDENT."""
    b1, _, _ = static_solve(*build_profile(cold, **kw), src=src)
    kw0 = {k: v for k, v in kw.items() if k in ("n_shell", "r_match")}
    b0, _, _ = static_solve(*build_profile(cold, uniform=True, **kw0), src=src)
    return abs(b1 / b0) ** 2


# ----------------------------------------------------------------------------
# SOLVER 1 (PRIMARY): frequency-domain transfer matrix
# ----------------------------------------------------------------------------


def outgoing_amplitude(edges, layers, omega: float, src="displacement",
                       amplitude: float = 1.0):
    t = stack_transfer(edges, layers, omega)
    m_out = basis_matrix(edges[-1], layers[-1], omega, outgoing=True)
    y0, y1 = _source_states(src)
    y0 = y0 * amplitude
    a = np.column_stack([t @ y1, -m_out[:, 0]])
    sol = np.linalg.solve(a, -(t @ y0))
    return sol[1], y0 + sol[0] * y1, float(np.linalg.cond(a))


def rho_N_transfer_matrix(cold, kr: float, src="displacement", **kw):
    omega = kr * cold["cP"] / R_CORE
    c1, _, cond1 = outgoing_amplitude(*build_profile(cold, **kw), omega=omega, src=src)
    kw0 = {k: v for k, v in kw.items() if k in ("n_shell", "r_match")}
    c0, _, cond0 = outgoing_amplitude(*build_profile(cold, uniform=True, **kw0),
                                      omega=omega, src=src)
    return abs(c1 / c0) ** 2, max(cond1, cond0)


def power_balance(cold, kr: float, src="displacement", **kw):
    """Ax3: work done by the source == power radiated to infinity."""
    omega = kr * cold["cP"] / R_CORE
    edges, layers = build_profile(cold, **kw)
    c_out, y_src, _ = outgoing_amplitude(edges, layers, omega, src=src)
    u_s, sig_s = y_src
    p_in = -0.5 * np.real(sig_s * np.conj(-1j * omega * u_s)) * 4 * np.pi * R_S ** 2
    m_out = basis_matrix(edges[-1], layers[-1], omega, outgoing=True)
    y_out = m_out[:, 0] * c_out
    p_rad = (-0.5 * np.real(y_out[1] * np.conj(-1j * omega * y_out[0]))
             * 4 * np.pi * edges[-1] ** 2)
    t = stack_transfer(edges, layers, omega)
    im_re = float(np.max(np.abs(t.imag)) / np.max(np.abs(t.real)))
    return float(p_in), float(p_rad), abs(p_in - p_rad) / abs(p_in), im_re


# ============================================================================
# THE FROZEN CERTIFICATION BATTERY (prereg sec 5 gates G1-G9, sec 6 FT-1..FT-4)
# ============================================================================


def gate_G1_lame(cold):
    """Lame exterior div u -> 0 static limit for a graded shell in an infinite
    medium (charter R5(a); the #782-confirmed gate)."""
    d5 = load_d5_profile_gains()
    arms = {
        "isotropic_baseline": {},
        "D5_orthotropic": {"shell_ortho": (d5["hoop_gain"], d5["radial_gain"])},
    }
    out, worst_ratio, worst_agree = {}, 0.0, 0.0
    for name, kw in arms.items():
        for src in SOURCES:
            edges, layers = build_profile(cold, **kw)
            _, y0, _ = static_solve(edges, layers, src=src)
            y_i, lay_i = state_at(edges, layers, y0, 0.5)
            d_int = abs(div_u(0.5, lay_i, y_i))
            d_ext = []
            for r_q in (1.5, 2.5, 3.5):
                y_q, lay_q = state_at(edges, layers, y0, r_q)
                d_ext.append(abs(div_u(r_q, lay_q, y_q)))
            ratio = max(d_ext) / d_int
            mean = float(np.mean(d_ext))
            agree = (max(d_ext) - min(d_ext)) / mean
            worst_ratio = max(worst_ratio, ratio)
            worst_agree = max(worst_agree, agree)
            out[f"{name}|{src}"] = {
                "div_u_interior_r0p5": d_int,
                "div_u_exterior_r1p5_2p5_3p5": d_ext,
                "lame_ratio": ratio,
                "shell_agreement": agree,
            }
    return {
        "arms": out,
        "lame_ratio_worst": worst_ratio,
        "shell_agreement_worst": worst_agree,
        "frozen": ("lame_ratio ≡ max over r in {1.5, 2.5, 3.5} of |div u|(r) / "
                   "|div u|(0.5) <= 1e-10"),
        "frozen_agreement": ("max|Δ div u| / mean(div u) <= 0.25 across the three "
                             "exterior radii"),
        "pass": bool(worst_ratio <= 1e-10 and worst_agree <= 0.25),
    }


def _K_compliance_ratio(cold, **kw):
    """Instrument-internal static-compliance ratio (traction drive).

    NOT the R4 K_eff/K_0 — that stays the lattice input I1 and is never
    recomputed here.  Used only by the G2 null check.
    """
    b1, _, _ = static_solve(*build_profile(cold, **kw), src="traction")
    kw0 = {k: v for k, v in kw.items() if k in ("n_shell", "r_match")}
    b0, _, _ = static_solve(*build_profile(cold, uniform=True, **kw0), src="traction")
    return abs(b0 / b1)


def gate_G2_uniform_null(cold):
    """Cage moduli = matrix  =>  rho_N -> 1, rho_S -> 0, r_Z -> 1 (charter R5(b)).

    KEEP-BOTH: the #775 ratio convention AND the charter's residual convention.
    """
    rows, worst = {}, 0.0
    for src in SOURCES:
        for kr in (1e-3, 0.3):
            rho_n, _ = rho_N_transfer_matrix(cold, kr, src=src, s_rail=1.0)
            rho_s = abs(rho_n - 1.0)
            k_ratio = _K_compliance_ratio(cold, s_rail=1.0)
            r_z = float(np.sqrt(k_ratio * 1.0))
            worst = max(worst, abs(rho_n - 1.0), rho_s, abs(r_z - 1.0))
            rows[f"{src}|kr={kr}"] = {"rho_N": rho_n, "rho_S": rho_s,
                                      "K_compliance_ratio": k_ratio, "r_Z": r_z}
    return {
        "rows": rows,
        "worst_deviation": worst,
        "frozen": ("at zero contrast: |rho_N - 1| <= 1e-12 AND rho_S <= 1e-12 "
                   "AND |r_Z - 1| <= 1e-12"),
        "keep_both": ("the uniform-medium NULL is read on BOTH conventions: "
                      "rho_N -> 1 and rho_S -> 0; neither convention is "
                      "redefined in place (KEEP-BOTH)"),
        "pass": bool(worst <= 1e-12),
    }


def gate_G3_ortho_reduction(cold):
    b_o, _, _ = static_solve(*build_profile(cold, shell_ortho=(1.0, 1.0)))
    b_i, _, _ = static_solve(*build_profile(cold))
    rel = abs(b_o - b_i) / abs(b_i)
    return {
        "B_ortho_unit_gains": complex(b_o).real,
        "B_isotropic": complex(b_i).real,
        "rel": float(rel),
        "frozen": ("|B_ortho(hoop=1,radial=1) - B_iso| / |B_iso| <= 1e-12"),
        "pass": bool(rel <= 1e-12),
    }


def gate_G4_tm_vs_ma(cold):
    rows, worst = {}, 0.0
    for src in SOURCES:
        ma = rho_N_matched_asymptotics(cold, src=src)
        for kr in [k for k in BAND if k <= QUASISTATIC_TOP]:
            tm, cond = rho_N_transfer_matrix(cold, kr, src=src)
            rel = abs(tm - ma) / ma
            worst = max(worst, rel)
            rows[f"{src}|kr={kr}"] = {"rho_N_TM": tm, "rho_N_MA": ma,
                                      "rel": rel, "cond": cond}
    return {
        "rows": rows,
        "worst_rel": worst,
        "frozen": ("|rho_N_TM(k·r_core) - rho_N_MA| / rho_N_MA <= 1e-6 for every "
                   "k·r_core <= 1e-3 in the frozen band"),
        "pass": bool(worst <= 1e-6),
    }


def gate_G5_ax3(cold):
    rows, worst_bal, worst_im = {}, 0.0, 0.0
    for src in SOURCES:
        p_in, p_rad, rel, im_re = power_balance(cold, 0.3, src=src)
        worst_bal = max(worst_bal, rel)
        worst_im = max(worst_im, im_re)
        rows[src] = {"P_in": p_in, "P_rad": p_rad, "rel_imbalance": rel,
                     "max_Im_over_Re_T": im_re}
    return {
        "rows": rows,
        "worst_rel_imbalance": worst_bal,
        "worst_Im_over_Re_T": worst_im,
        "frozen": ("|P_in - P_rad| / |P_in| <= 1e-10"),
        "frozen_real_T": ("max|Im T| / max|Re T| <= 1e-14"),
        "pass": bool(worst_bal <= 1e-10 and worst_im <= 1e-14),
    }


def gate_G6_refinement(cold):
    d5 = load_d5_profile_gains()
    arms = {"isotropic_baseline": {},
            "D5_orthotropic": {"shell_ortho": (d5["hoop_gain"], d5["radial_gain"])}}
    rows, worst = {}, 0.0
    for name, kw in arms.items():
        for src in SOURCES:
            v1, _ = rho_N_transfer_matrix(cold, 1e-2, src=src, n_shell=N_SHELL, **kw)
            v2, _ = rho_N_transfer_matrix(cold, 1e-2, src=src, n_shell=2 * N_SHELL, **kw)
            rel = abs(v2 - v1) / v1
            worst = max(worst, rel)
            rows[f"{name}|{src}"] = {"rho_N_n": v1, "rho_N_2n": v2, "rel": rel}
    return {
        "rows": rows, "worst_rel": worst, "n_shell": N_SHELL,
        "frozen": ("|rho_N(2·n_shell) - rho_N(n_shell)| / rho_N(n_shell) <= 1e-3 "
                   "at the frozen n_shell = 256"),
        "pass": bool(worst <= 1e-3),
    }


def gate_G7_amplitude(cold):
    rows, worst = {}, 0.0
    for src in SOURCES:
        vals = []
        for amp in (1e-6, 1.0, 1e6):
            omega = 1e-2 * cold["cP"] / R_CORE
            c1, _, _ = outgoing_amplitude(*build_profile(cold), omega=omega,
                                          src=src, amplitude=amp)
            c0, _, _ = outgoing_amplitude(*build_profile(cold, uniform=True),
                                          omega=omega, src=src, amplitude=amp)
            vals.append(abs(c1 / c0) ** 2)
        rel = (max(vals) - min(vals)) / np.mean(vals)
        worst = max(worst, rel)
        rows[src] = {"rho_N_by_amplitude": vals, "rel_spread": rel}
    return {
        "rows": rows, "worst_rel": worst,
        "frozen": ("rho_N invariant across source amplitude 1e-6 ... 1e+6 to "
                   "<= 1e-12 relative"),
        "honesty_caveat": ("G7 is STRUCTURALLY exact in a linear frequency-domain "
                           "solver; it certifies wiring, not physical linearity, "
                           "and is reported as such"),
        "pass": bool(worst <= 1e-12),
    }


def gate_G8_matching_radius(cold):
    rows, worst = {}, 0.0
    for src in SOURCES:
        vals = []
        for r_m in (2.0, 4.0, 8.0, 16.0):
            v, _ = rho_N_transfer_matrix(cold, 1e-2, src=src, r_match=r_m)
            vals.append(v)
        rel = (max(vals) - min(vals)) / np.mean(vals)
        worst = max(worst, rel)
        rows[src] = {"rho_N_by_R_match": vals, "rel_spread": rel}
    return {
        "rows": rows, "worst_rel": worst,
        "frozen": ("rho_N invariant across R_match/r_core in {2, 4, 8, 16} to "
                   "<= 1e-9 relative"),
        "pass": bool(worst <= 1e-9),
    }


def gate_G9_band_conditioning(cold):
    rows, worst = {}, 0.0
    for src in SOURCES:
        for kr in BAND:
            v, cond = rho_N_transfer_matrix(cold, kr, src=src)
            worst = max(worst, cond)
            rows[f"{src}|kr={kr}"] = {"rho_N": v, "cond": cond}
    return {
        "rows": rows, "worst_cond": worst, "band": list(BAND),
        "frozen": ("cond(system matrix) <= 1e12 at every sampled k·r_core in the "
                   "certified band k·r_core in [1e-8, 4]"),
        "pass": bool(worst <= 1e12),
    }


# ----------------------------------------------------------------------------
# GATE-FIREABILITY SELF-TESTS (prereg sec 6) — each MUST FIRE
# ----------------------------------------------------------------------------


def _lame_ratio_only(cold, **kw):
    edges, layers = build_profile(cold, **kw)
    _, y0, _ = static_solve(edges, layers)
    y_i, lay_i = state_at(edges, layers, y0, 0.5)
    d_int = abs(div_u(0.5, lay_i, y_i))
    d_ext = []
    for r_q in (1.5, 2.5, 3.5):
        y_q, lay_q = state_at(edges, layers, y0, r_q)
        d_ext.append(abs(div_u(r_q, lay_q, y_q)))
    return max(d_ext) / d_int


def selftest_FT1(cold):
    """G1 fireability: profiles whose grade does not terminate at the contour."""
    r_grade = _lame_ratio_only(cold, ext_grade=0.10)
    r_ortho = _lame_ratio_only(cold, ext_ortho=(1.02, 0.99))
    fires = bool(r_grade >= 1e-3 and r_ortho >= 1e-3)
    return {
        "lame_ratio_graded_exterior_q0p10": r_grade,
        "lame_ratio_orthotropic_exterior_1p02_0p99": r_ortho,
        "frozen": "both mis-specified profiles MUST return lame_ratio >= 1e-3",
        "targets": "G1",
        "FIRES": fires,
    }


def selftest_FT2(cold):
    """G2 fireability — the structural-null lens: rho_S must be a LIVE observable."""
    rho_n, _ = rho_N_transfer_matrix(cold, 1e-3, s_rail=0.99)
    rho_s = abs(rho_n - 1.0)
    return {
        "s_rail_contrast": 0.99, "rho_N": rho_n, "rho_S": rho_s,
        "frozen": "the contrast case MUST return rho_S >= 1e-5 at k·r_core = 1e-3",
        "targets": "G2",
        "FIRES": bool(rho_s >= 1e-5),
    }


def selftest_FT3(cold):
    """G5 fireability: a smuggled friction (complex modulus) must break Ax3."""
    p_in, p_rad, rel, im_re = power_balance(cold, 0.3, absorb=1e-3)
    return {
        "absorb_Im_over_Re": 1e-3, "P_in": p_in, "P_rad": p_rad,
        "rel_imbalance": rel, "max_Im_over_Re_T": im_re,
        "frozen": "the absorbing case MUST return |P_in - P_rad|/|P_in| >= 1e-2",
        "targets": "G5",
        "FIRES": bool(rel >= 1e-2),
    }


def selftest_FT4(cold):
    """G4 fireability: TM and MA must DISAGREE out of the backstop's regime."""
    ma = rho_N_matched_asymptotics(cold)
    tm, _ = rho_N_transfer_matrix(cold, 3.0)
    rel = abs(tm - ma) / ma
    return {
        "k_r_core": 3.0, "rho_N_TM": tm, "rho_N_MA": ma, "rel": rel,
        "frozen": ("the out-of-regime comparison MUST return |rho_N_TM - "
                   "rho_N_MA|/rho_N_MA >= 1e-1"),
        "targets": "G4",
        "FIRES": bool(rel >= 1e-1),
    }


# ----------------------------------------------------------------------------
# R2 / R4 REPORTING CONTRACT (prereg sec 10) — SEPARABLE, symbolic c^2
# ----------------------------------------------------------------------------


def two_term_rho_report(cold, d5):
    """The two rho_eff columns, NEVER pre-summed.  D1 is HELD: no c^2 evaluated."""
    with open(VESSEL_JSON) as fh:
        phi = json.load(fh)["verdict"]["fixed_budget_headline"]["phi_sf"]
    k_ratio_lattice = d5["K_tan_over_K0_796"]          # I1 — lattice input, NOT recomputed
    rows = []
    for beta in (0, 1, 3):                              # D2 disclosed sweep
        term_i = 1.0                                    # structural, n=0 volume average
        term_ii = beta * phi                            # trapped-energy loading
        rows.append({
            "beta_D2_disclosed_scan": beta,
            "phi_sf_lattice": phi,
            "term_i_structural_rho_over_rho0": term_i,
            "term_i_flag": FROZEN_STRINGS["structural_not_built"],
            "term_ii_trapped_energy_rho_over_rho0": term_ii,
            "term_ii_symbolic_c2_label": FROZEN_STRINGS["beta_symbolic"],
            "rho_eff_over_rho0_if_summed_DOWNSTREAM_ONLY": term_i + term_ii,
            "r_Z_family": float(np.sqrt(k_ratio_lattice * (term_i + term_ii))),
            "K_factor_provenance": ("I1 lattice input (#796 K_tan/K_0); R4: "
                                    "r_Z must NOT recompute or perturb K_eff/K_0"),
            "label": "DEMONSTRATION - no verdict banked",
        })
    c_p, c_s = cold["cP"], cold["cS"]
    return {
        "columns_kept_separable": True,
        "rows": rows,
        "c2_lever": {
            "candidate_swap_ratio_cP2_over_cS2": (c_p / c_s) ** 2,
            "candidate_swap_ratio_cS2_over_cP2": (c_s / c_p) ** 2,
            "c_EM": "UNEVALUATED SYMBOL - no lattice-measured value on the ledger",
            "designated_candidate": None,
            "reading": ("swapping the divisor between the two lattice-measured "
                        "candidates rescales beta by exactly this ratio; D2's "
                        "disclosed sweep and D1's sector choice therefore lie on "
                        "the SAME axis, which is what makes stage 1 "
                        "D1-INDEPENDENT by construction"),
            "frozen": ("the c^2 dependence is reported as the dimensionless "
                       "candidate-swap ratio (c_i/c_j)^2 from the lattice-measured "
                       "speeds, with NO candidate designated and c_EM carried as "
                       "an unevaluated symbol"),
        },
        "D1_status": "HELD by Grant; no c^2 evaluated anywhere in stage 1",
        "mixed_provenance_citation": FROZEN_STRINGS["mixed_provenance"],
        "r_Z_796_cited": d5["r_Z_796_mixed_provenance"],
    }


def liveness_demonstration(cold, d5):
    """Instrument liveness ONLY.  Explicitly NOT a physics verdict (prereg X4)."""
    out = {"label": "DEMONSTRATION - no verdict banked",
           "n1_fence": FROZEN_STRINGS["n1_absent"],
           "quasistatic_read_fence": ("no exponent or quasistatic quantity is read "
                                      "above k·r_core = 1e-3; the resonant band is "
                                      "reported as characterization only")}
    arms = {"isotropic_baseline": {},
            "D5_orthotropic_measured": {"shell_ortho": (d5["hoop_gain"],
                                                        d5["radial_gain"])}}
    for name, kw in arms.items():
        per_src = {}
        for src in SOURCES:
            ma = rho_N_matched_asymptotics(cold, src=src, **kw)
            curve = {}
            for kr in BAND:
                v, _ = rho_N_transfer_matrix(cold, kr, src=src, **kw)
                curve[str(kr)] = v
            sub = [k for k in BAND if k <= QUASISTATIC_TOP]
            slope = float(np.polyfit(np.log([k for k in sub]),
                                     np.log([curve[str(k)] for k in sub]), 1)[0])
            per_src[src] = {
                "rho_N_matched_asymptotics_k_to_0": ma,
                "rho_N_by_k_r_core": curve,
                "fitted_exponent_p_over_subresonant_tail": slope,
                "p_interpretation": ("the n=0 CENTRED-source channel is analytically "
                                     "k-INDEPENDENT in the deep-quasistatic limit "
                                     "(the k^4 monopole prefactor cancels in the "
                                     "caged/uncaged ratio), so p = 0 here is a "
                                     "CHANNEL property, NOT a test of the charter's "
                                     "F2 (p = 2), which is a DISPLACED-source n=1 "
                                     "statement - see prereg X5"),
            }
        out[name] = per_src
    return out


# ----------------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------------


def _digest(obj) -> str:
    payload = json.dumps(obj, sort_keys=True, default=str).encode()
    return hashlib.sha256(payload).hexdigest()


def main():
    t0 = time.time()
    cold = load_cold_medium()
    d5 = load_d5_profile_gains()

    gates = {
        "G1_lame_static": gate_G1_lame(cold),
        "G2_uniform_null": gate_G2_uniform_null(cold),
        "G3_ortho_to_iso_reduction": gate_G3_ortho_reduction(cold),
        "G4_TM_vs_matched_asymptotics": gate_G4_tm_vs_ma(cold),
        "G5_ax3_lossless": gate_G5_ax3(cold),
        "G6_layer_refinement": gate_G6_refinement(cold),
        "G7_drive_amplitude_independence": gate_G7_amplitude(cold),
        "G8_matching_radius_independence": gate_G8_matching_radius(cold),
        "G9_band_conditioning": gate_G9_band_conditioning(cold),
    }
    selftests = {
        "FT1_lame_fireability": selftest_FT1(cold),
        "FT2_null_liveness": selftest_FT2(cold),
        "FT3_ax3_fireability": selftest_FT3(cold),
        "FT4_TM_MA_nonvacuity": selftest_FT4(cold),
    }
    all_gates_pass = all(g["pass"] for g in gates.values())
    all_fire = all(s["FIRES"] for s in selftests.values())
    selftests["gate_fireability_selftest_pass"] = all_fire
    selftests["frozen"] = ("gate_fireability_selftest_pass = FT-1 AND FT-2 AND "
                           "FT-3 AND FT-4 all FIRE at their frozen thresholds")

    # --- CLASS-B reachability: the certified band/profile scope is MEASURED ---
    band_ok = sorted({float(k.split("kr=")[1])
                      for k, v in gates["G9_band_conditioning"]["rows"].items()
                      if v["cond"] <= 1e12})
    g4_ok = sorted({float(k.split("kr=")[1])
                    for k, v in gates["G4_TM_vs_matched_asymptotics"]["rows"].items()
                    if v["rel"] <= 1e-6})
    g4_frozen = [k for k in BAND if k <= QUASISTATIC_TOP]
    scope_reductions = []
    if band_ok != sorted(set(BAND)):
        scope_reductions.append(
            f"G9 certified band REDUCED to {band_ok} (frozen {list(BAND)})")
    if g4_ok != sorted(set(g4_frozen)):
        scope_reductions.append(
            f"G4 overlap sub-band REDUCED to {g4_ok} (frozen {g4_frozen})")
    for name, arms_key in (("G1_lame_static", "arms"), ("G6_layer_refinement", "rows")):
        rows = gates[name][arms_key]
        profiles = {k.split("|")[0] for k in rows}
        if len(profiles) < 2:
            scope_reductions.append(f"{name} profile class REDUCED to {profiles}")

    if all_gates_pass and all_fire and not scope_reductions:
        cls, why = "A_CERTIFIED", ("all of G1..G9 PASS on both source fittings AND "
                                   "gate_fireability_selftest_pass = True")
    elif all_gates_pass and all_fire:
        cls, why = "B_CERTIFIED_SCOPED", (
            "all of G1..G9 PASS and gate_fireability_selftest_pass = True, but at "
            "least one gate passes only over a REDUCED band or a REDUCED profile "
            "class")
    else:
        cls, why = "C_NOT_CERTIFIED_VOID", ("any of G1..G9 FAILS, OR any of "
                                            "FT-1..FT-4 fails to fire")

    results = {
        "provenance": {
            "class": ("continuum radial-acoustic solver STAGE 1 - INSTRUMENT "
                      "CERTIFICATION ONLY; banks no physics verdict; mints no "
                      "clm-/def-; engine byte-untouched; deterministic (no RNG)."),
            "prereg_file": ("research/2026-07-28_continuum-radial-solver-stage1_"
                            "prereg-FROZEN.md"),
            "charter": "research/2026-07-21_continuum-radial-solver_CHARTER.md",
            "rulings": ("Grant 2026-07-28 [sic]: 'D2: disclosed, D3: follow rec, "
                        "D4: do it, D5: do the rec'; D1 HELD"),
            "engine_fence": ("engine src/ave BYTE-UNTOUCHED; the instrument lives "
                             "entirely in research/drivers/ and imports ave.core.* "
                             "read-only"),
            "exterior": ("the exterior beyond R_match is represented by the exact "
                         "analytic outgoing solution; no sponge, no absorbing "
                         "layer, no far-field truncation"),
            "source_axis": ("every gate is evaluated for both source fittings "
                            "(prescribed displacement and prescribed traction) and "
                            "passes only if it passes for both"),
            "d5_read": ("the D5 profile gains are computed from the shipped "
                        "vessel_state_rve_results.json fields (min_kse, peak_A, "
                        "k_a_RHO_STAR, k_s_KS0) at driver runtime; no vessel-state "
                        "number is retyped from prose"),
            "R8": ("every number the solver consumes appears on the charter §3 "
                   "ledger or the §3 delta with its tag; no SM/GR convention "
                   "default (in particular no c_light and no unlabeled c) enters "
                   "anywhere"),
            "rule11": ("no adjudication criterion may be dropped or relaxed "
                       "post-hoc to convert a FAIL to a PASS"),
            "below_band": ("below k·r_core = 1e-8 the matched-asymptotics backstop "
                           "is the instrument of record; it is k-independent in "
                           "that limit and is certified against the transfer matrix "
                           "in the overlap band [1e-8, 1e-3]"),
            "disclosures": FROZEN_STRINGS,
            "geometry": {"r_core": R_CORE, "r_s": R_S, "W_shell": W_SHELL,
                         "S_rail": S_RAIL, "n_shell": N_SHELL,
                         "R_match": R_MATCH, "n_ext": N_EXT,
                         "band": list(BAND), "quasistatic_top": QUASISTATIC_TOP},
        },
        "cold_medium": cold,
        "d5_profile": d5,
        "gates": gates,
        "selftests": selftests,
        "two_term_rho_report": two_term_rho_report(cold, d5),
        "liveness_demonstration": liveness_demonstration(cold, d5),
        "certification": {
            "all_gates_pass": all_gates_pass,
            "gate_fireability_selftest_pass": all_fire,
            "measured_certified_band": band_ok,
            "measured_G4_overlap_subband": g4_ok,
            "scope_reductions": scope_reductions,
            "class": cls,
            "frozen_class_criterion": why,
            "classes_frozen": {
                "A_CERTIFIED": ("all of G1..G9 PASS on both source fittings AND "
                                "gate_fireability_selftest_pass = True"),
                "B_CERTIFIED_SCOPED": ("all of G1..G9 PASS and "
                                       "gate_fireability_selftest_pass = True, but "
                                       "at least one gate passes only over a "
                                       "REDUCED band or a REDUCED profile class"),
                "C_NOT_CERTIFIED_VOID": ("any of G1..G9 FAILS, OR any of "
                                         "FT-1..FT-4 fails to fire"),
            },
            "no_verdict_fence": FROZEN_STRINGS["no_verdict"],
        },
    }
    results["_runtime_sec"] = round(time.time() - t0, 2)
    results["runtime_budget_frozen"] = ("total certification-battery runtime <= 600 "
                                        "s on the reference machine; a longer run "
                                        "is disclosed, not silently accepted")
    results["runtime_within_budget"] = bool(results["_runtime_sec"] <= 600)
    trimmed = {k: v for k, v in results.items() if k != "_runtime_sec"}
    results["determinism_digest"] = _digest(trimmed)
    results["determinism_frozen"] = ("two independent full driver runs produce an "
                                     "identical results digest (SHA-256 over the "
                                     "results object minus timing fields)")

    with open(OUT_JSON, "w") as fh:
        json.dump(results, fh, indent=1)
    print(f"[stage-1] class = {cls}   gates_pass={all_gates_pass}  "
          f"fireability={all_fire}  runtime={results['_runtime_sec']} s")
    print(f"[stage-1] digest = {results['determinism_digest']}")
    return results


if __name__ == "__main__":
    main()
