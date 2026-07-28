#!/usr/bin/env python3
"""SUBC/KUBC BRACKET — OWED-1: bound K_eff on BOTH sides, not one.

Every K_eff the corpus has banked from this bench family (#782 `K_eff/K_0 = 0.296`;
#796 `K_tan/K_0 = 0.29548`) is measured under KUBC — a KINEMATIC uniform boundary
condition, the rigorous UPPER-bound (stiff) side. This driver adds the variational
DUAL — SUBC, the STATIC (uniform-traction) uniform boundary condition, the rigorous
LOWER bound — so the corpus has a BRACKET rather than a one-sided bound.

Prereg (FROZEN, committed ALONE and pushed first):
    research/2026-07-28_subc-kubc-bracket_prereg-FROZEN.md

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-FIRST SECTOR HEADER (fired before any standard-physics term)
═══════════════════════════════════════════════════════════════════════════════
  SECTOR : the TRANSLATIONAL (Cauchy-grade) VECTOR sector of the chiral srs-z3 net
           (ave.core.chiral_lattice._SRS_8A/_NN, I4132, Wyckoff-8a, z=3). Rank-2 bond
           tensor Phi_b = k_a(d^d) + k_s(I - d^d). NOT a Cartesian Laplacian.
           Rule-14 reuse of the #770/#775/#782/#796 bond model — BYTE-IDENTICAL medium;
           the ONLY thing this lane changes is what the box does at its outer skin.
  REGIME : STATIC constitutive response — NO drive, NO lock-in, NO radiation port, NO
           time axis. Ax3-lossless-reactive: the discrete form is PSD, the static solve
           is unique modulo its null space, no hysteresis, no rate.
  COORDS : real-space strain/stress decomposition + impedance plane (A46-clean):
           TRACEFUL (hydrostatic => K_eff, A1) vs DEVIATORIC (pure shear => G_eff, T2).
           KUBC imposes the macroscopic STRAIN E; SUBC imposes its work-conjugate, the
           macroscopic STRESS Sigma — the correct dual pairing, not a second guess.
  CLASS  : lattice-derived static homogenization under two boundary conditions.
           CONSISTENCY-class (does an already-banked lattice number survive its own
           boundary condition?), NOT emergence. alpha-CLEAN. Every VALUE dimensionless.

★SCOPE FENCE (prereg §7 — required at every headline): this brackets K ONLY. Every
 r_Z interval here is a K-BRACKET AROUND AN ASSUMED rho_eff/rho_0 == 1. The rho half
 is NOT measured, NOT bracketed; OWED-2 is NOT discharged by this lane.

★BORN-MODEL INSTRUMENT FACT (prereg §0 walk item 7): Phi_b = k_a d^d + k_s(I - d^d)
 penalizes a global rigid ROTATION, so the free (pure-Neumann) operator's null space
 is the 3 uniform TRANSLATIONS ONLY, not the 6 rigid-body modes. Stated, not repaired
 (repairing it would change the medium and break the Rule-14 comparison).

ENGINE BYTE-UNTOUCHED: imports ave.core.* / the #782/#796 drivers read-only.

Run: PYTHONPATH=src:src/scripts/vol_1_foundations python3 \
        research/drivers/subc_kubc_bracket.py
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

# ── Rule-14 reuse of the VALIDATED #770/#775/#782/#796 pipeline (read-only imports) ──
_DRIVERS = Path(__file__).resolve().parent
sys.path.insert(0, str(_DRIVERS))
from constituent_cage_ensemble import (  # noqa: E402
    build_finite_srs, bond_tensors, forces, RHO_STAR, K_S,
)
from rve_aggregation_bench import (  # noqa: E402
    boundary_mask, affine_field, jacobi_diag, cg_solve_interior, elastic_energy,
    core_energy, strain_mode, cage_bond_stiffness, cubic_cage_centers,
    packing_fraction, coated_inclusion_fraction, measure_modulus_ratio,
    uncaged_reference, CAGE_W, EPS, BW,
)
from vessel_state_rve import (  # noqa: E402
    K_A, KS0, KSE_SOLVE_FLOOR, OUTER_SC_TOL, PHI_SF_S, PHI_SF_RCAGE, VERDICT_P_REF,
    VERDICT_SRC_SIGMA, VERDICT_WALL, VERDICT_S_RAIL, build_cage, grow_verdict_arm,
    painted_anisotropic_arm, isotropic_control_K, radiation_source,
    state_operator, bond_axial_strain, k_shear_eff,
)

# ═════════════════════════════════════════════════════════════════════════════
# FROZEN bench constants (prereg §1/§3/§4/§5)
# ═════════════════════════════════════════════════════════════════════════════
L_BASE = 16                     # verdict grid (#782/#796)
L_SIZES = (12, 16, 20)          # RVE-size scan (G7b)
S_RAIL_DEEP = 1e-4              # #782 deep rail on the cage shells
SUBC_TOL = 1e-9                 # frozen §1.1: SUBC pure-Neumann CG relative residual
SUBC_MAX = 60000                # frozen §1.1: SUBC iteration cap
SIGMA_PROBE = 1.0               # SUBC macroscopic stress amplitude (cancels in every ratio)
G1_SLACK = 1e-6                 # frozen §4 G1 ordering slack (relative)
G2A_TOL = 1e-12                 # frozen §4 G2a identity tolerance
G5_TOL = 1e-8                   # frozen §4 G5 work-identity tolerance
G6_TOL = 2e-3                   # frozen §4 G6 reproduction tolerance
G7B_SLACK = 0.02                # frozen §4 G7b size-trend absolute slack
G8_TOL = 1e-10                  # frozen §4 G8 load-amplitude invariance tolerance

# frozen §3 configuration grid
ROUTE_A = {"s": 4.5, "r_cage": [1.3, 1.6, 1.9, 2.2]}
ROUTE_B = {"r_cage": 1.7, "s": [3.6, 4.2, 5.0, 6.5]}

# frozen §5.2 threshold set — ALL pre-existing corpus thresholds, none minted here
T1_RZ = 0.5                     # #782 prereg §2 BIN-1/BIN-2 band edge
T2_RZ = (0.45, 0.55)            # #796 prereg §6 Z_lo/Z_str/Z_hi edges at delta_rZ=0.05
T3_R = 1.0                      # soften/stiffen sign threshold (the #782 STOP-gate)
T4_LIFT = (1.2, 1.5)            # #796 prereg §6 L1/L2/L3 lift bands

# frozen §3 D — the fully-SUBC-grown companion budget (NOT part of any bracket)
COMPANION_OUTER_CAP = 40
COMPANION_WALL_CLOCK_S = 1200.0

BOTH_MODES = ("hydro", "shear")   # every bracketed config runs both (supplementary M)

SIG_HYDRO = np.eye(3)
SIG_SHEAR = np.outer([1.0, 0, 0], [0, 1.0, 0]) + np.outer([0, 1.0, 0], [1.0, 0, 0])


# ═════════════════════════════════════════════════════════════════════════════
# ★THE SUBC PRIMITIVE (the new physics; prereg §1 — the ONLY thing this lane adds)
# ═════════════════════════════════════════════════════════════════════════════
def active_mask(bi, bj, N):
    """Frozen §1.1: `SUBC active set = nodes of nonzero bond degree; degree-0 nodes are
    excluded from the solve and carry no load`. Without this the pure-Neumann operator
    is singular BEYOND its physical null space (a zero-degree node is 3 free DOFs with
    zero stiffness) and the preconditioned CG diverges — reproduced in the design-time
    pilot. Exactly 1 such node exists at each of L in {12,16,20}; the degree>0 subgraph
    is a SINGLE connected component at all three sizes (union-find, §6.2 pilot 1)."""
    deg = np.zeros(N, dtype=int)
    np.add.at(deg, bi, 1)
    np.add.at(deg, bj, 1)
    return deg > 0


def component_count(bi, bj, act):
    """Number of connected components of the degree>0 bond graph (union-find). The
    pure-Neumann null space is 3 x this count; the frozen translation projection is
    correct ONLY at count == 1 (asserted, not assumed)."""
    idx = {int(n): i for i, n in enumerate(np.where(act)[0])}
    par = list(range(len(idx)))

    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a

    for a, b in zip(bi, bj):
        ra, rb = find(idx[int(a)]), find(idx[int(b)])
        if ra != rb:
            par[ra] = rb
    return len({find(i) for i in range(len(par))})


def traction_load(pos, act, Sigma, bw=BW):
    """Frozen §1.1 discrete uniform-traction load set: `For each of the 6 outer faces
    (normal ±e_d), the face shell F is the set of ACTIVE nodes within bw = 1.5 lattice
    units of that face plane; each node in F receives f_i += (Σ·n)·A_face/|F|, where
    A_face is the cell cross-section perpendicular to d`. Corner/edge nodes belonging to
    several face shells receive the SUM. The SAME bw as the KUBC boundary shell, so both
    boundary conditions act on the SAME skin (apples-to-apples, frozen)."""
    lo, hi = pos.min(axis=0), pos.max(axis=0)
    span = hi - lo
    f = np.zeros_like(pos)
    for d in range(3):
        A = span[(d + 1) % 3] * span[(d + 2) % 3]
        for sgn in (+1.0, -1.0):
            n = np.zeros(3)
            n[d] = sgn
            face = ((pos[:, d] >= hi[d] - bw) if sgn > 0 else (pos[:, d] <= lo[d] + bw)) & act
            f[face] += (Sigma @ n)[None, :] * (A / max(int(face.sum()), 1))
    f[~act] = 0.0
    return f


def hill_stress(f, pos, xc, V):
    """Frozen §1.1: the macroscopic stress ACTUALLY realized by the shipped load set,
    read by Hill's lemma rather than assumed — `Σ̄ = (1/V)·sym( Σ_i f_i ⊗ (x_i − x_c) )`.
    Any imperfection in the discrete surface quadrature is thereby absorbed, not hidden."""
    M = np.einsum("ia,ib->ab", f, pos - xc)
    return 0.5 * (M + M.T) / V


def _proj_translations(w):
    """Frozen §1.1 null-space handling: orthogonal projection off the 3 uniform
    translations. NO rotational projection — rigid rotations are NOT null modes of the
    Born bond model (prereg §0 walk item 7), a fact this driver ASSERTS (see
    born_rotation_check) rather than assumes."""
    return w - w.mean(axis=0)[None, :]


def cg_neumann(Phi, bi, bj, N, act, f, diag_pre, tol=SUBC_TOL, itmax=SUBC_MAX):
    """Frozen §1.1: matrix-free Jacobi-preconditioned CG for the PURE-NEUMANN system
    K u = f, with every operator application, the preconditioner and the RHS projected
    onto the complement of the 3 uniform translations. Returns (u_full, rel_res, iters).

    apply_K(w) = -forces(w) = K w — the SAME operator the KUBC arm uses. NOTHING about
    the medium changes; only the boundary term does."""
    idx = np.where(act)[0]
    Mi = 1.0 / np.maximum(diag_pre[idx], 1e-30)

    def applyK(wf):
        w = np.zeros((N, 3))
        w[idx] = wf
        return (-forces(w, Phi, bi, bj, N))[idx]

    b = _proj_translations(f[idx])
    bnorm = np.linalg.norm(b) + 1e-30
    x = np.zeros_like(b)
    r = b - _proj_translations(applyK(x))
    z = _proj_translations(Mi * r)
    p = z.copy()
    rz = float(np.sum(r * z))
    it = 0
    res = np.linalg.norm(r) / bnorm
    while res > tol and it < itmax:
        Ap = _proj_translations(applyK(p))
        alpha = rz / (float(np.sum(p * Ap)) + 1e-30)
        x += alpha * p
        r -= alpha * Ap
        z = _proj_translations(Mi * r)
        rz_new = float(np.sum(r * z))
        p = z + (rz_new / (rz + 1e-30)) * p
        rz = rz_new
        it += 1
        res = np.linalg.norm(r) / bnorm
    u = np.zeros((N, 3))
    u[idx] = _proj_translations(x)
    return u, float(res), it


def subc_solve(geom, act, Phi, diag, mode, xc, V, half, sigma=SIGMA_PROBE):
    """One SUBC measurement: impose the uniform traction of macroscopic stress
    `sigma * Sigma(mode)`, relax the WHOLE cell (no DOF is prescribed), and return the
    frozen §1.2 energy functional plus the absolute apparent modulus.

    Frozen §1.2: `SUBC energy functional: U_SUBC(Σ) = ½ Σ_bonds du·Φ·du evaluated at the
    traction-equilibrium displacement — the WHOLE-CELL elastic energy, equal at
    equilibrium to the work of the imposed tractions ½ f·u`.
    """
    pos, bi, bj, dhat, mid = geom
    N = pos.shape[0]
    Sig = sigma * (SIG_HYDRO if mode == "hydro" else SIG_SHEAR)
    f = traction_load(pos, act, Sig)
    Sb = hill_stress(f, pos, xc, V)
    sbar = float(np.trace(Sb) / 3.0) if mode == "hydro" else float(Sb[0, 1])
    u, res, it = cg_neumann(Phi, bi, bj, N, act, f, diag)
    U = elastic_energy(u, Phi, bi, bj)
    work = 0.5 * float(np.sum(f * u))
    M_abs = sbar ** 2 * V / (2.0 * U) if U > 0 else float("nan")
    return {
        "U_total": float(U), "U_core": float(core_energy(u, Phi, bi, bj, mid, xc, half)),
        "work_half_f_dot_u": work,
        "work_identity_rel": float(abs(U - work) / (abs(U) + 1e-300)),
        "sigma_bar": sbar, "M_abs": float(M_abs),
        "cg_residual": res, "cg_iters": it,
        "net_force_norm": float(np.linalg.norm(f.sum(axis=0))),
        "net_torque_norm": float(np.linalg.norm(np.cross(pos - xc, f).sum(axis=0))),
    }


def kubc_solve(geom, free, Phi, diag, mode, xc, V, half, eps=EPS):
    """The KUBC counterpart, Rule-14 on the #782 primitive (`cg_solve_interior`): impose
    the affine macroscopic strain on the boundary shell, relax the interior, return BOTH
    the whole-cell energy (the bound-carrying measure) and the central-L/2-cube core
    energy (the SHIPPED #782/#796 estimator, which carries NO bound status, prereg §2.3).
    """
    pos, bi, bj, dhat, mid = geom
    N = pos.shape[0]
    E = strain_mode(mode, eps)
    u_bc = np.zeros((N, 3))
    u_bc[~free] = affine_field(pos[~free], xc, E)
    u, res, it = cg_solve_interior(Phi, bi, bj, N, free, u_bc, diag)
    U = elastic_energy(u, Phi, bi, bj)
    pref = 4.5 if mode == "hydro" else 2.0
    return {
        "U_total": float(U), "U_core": float(core_energy(u, Phi, bi, bj, mid, xc, half)),
        "M_abs": float(U / (pref * eps ** 2 * V)),
        "cg_residual": float(res), "cg_iters": int(it),
    }


def born_rotation_check(geom, Phi, xc):
    """★ASSERT the prereg §0 walk item 7 instrument fact: a global rigid ROTATION costs
    energy on this Born bond model, so the pure-Neumann null space is the 3 uniform
    TRANSLATIONS ONLY. A translation must cost ZERO; a rotation must NOT."""
    pos, bi, bj, dhat, mid = geom
    N = pos.shape[0]
    u_t = np.tile(np.array([1.0, 0.0, 0.0]), (N, 1))
    u_r = 1e-3 * np.cross(np.broadcast_to(np.array([0.0, 0.0, 1.0]), pos.shape), pos - xc)
    E_t = elastic_energy(u_t, Phi, bi, bj)
    E_r = elastic_energy(u_r, Phi, bi, bj)
    E_ref = elastic_energy(affine_field(pos, xc, strain_mode("hydro", 1e-3)), Phi, bi, bj)
    return {
        "E_uniform_translation": float(E_t),
        "E_rigid_rotation_scaled_1e-3": float(E_r),
        "E_hydro_affine_eps_1e-3_reference": float(E_ref),
        "translation_is_null_mode": bool(E_t <= 1e-20),
        "rotation_is_null_mode": bool(E_r <= 1e-20),
        "born_model_confirmed_rotations_cost_energy": bool(E_t <= 1e-20 and E_r > 1e-20),
    }


# ═════════════════════════════════════════════════════════════════════════════
# ★THE THREE RATIO DEFINITIONS (prereg §2) — each carries its rigor status
# ═════════════════════════════════════════════════════════════════════════════
def bracket_from_pair(arm_subc, arm_kubc, unc_subc, unc_kubc):
    """Build the frozen §2 ratio set for ONE (configuration, mode).

    §2.1 PRIMARY (same-instrument, the headline; bias-cancelling, NOT theorem-grade
         on the ratio):  R_KUBC = K_KUBC^arm/K_KUBC^unc  and
                         R_SUBC = K_SUBC^arm/K_SUBC^unc = U_SUBC^unc/U_SUBC^arm
         — the energy ratio INVERTS under traction control, because at FIXED LOAD the
         stored energy tracks the COMPLIANCE, not the stiffness. (This inversion is the
         single easiest place to get the extraction backwards, which is exactly why
         SELFTEST-G1 forces the ordering gate to fire on the inverted form.)
    §2.2 CONSERVATIVE (theorem-grade):  R_lo = K_SUBC^arm/K_KUBC^unc,
         R_hi = K_KUBC^arm/K_SUBC^unc — each factor bounded in the correct direction.
    §2.3 CORE-CONVENTION COMPANION (NO bound status either end) — the convention
         #782/#796 actually banked, reported side-by-side so the shipped numbers stay
         readable, and labelled NOT-A-BRACKET everywhere.
    """
    R_KUBC = arm_kubc["U_total"] / (unc_kubc["U_total"] + 1e-300)
    R_SUBC = unc_subc["U_total"] / (arm_subc["U_total"] + 1e-300)
    g0 = unc_kubc["M_abs"] / (unc_subc["M_abs"] + 1e-300)
    R_lo, R_hi = R_SUBC / g0, R_KUBC * g0
    R_KUBC_core = arm_kubc["U_core"] / (unc_kubc["U_core"] + 1e-300)
    R_SUBC_core = unc_subc["U_core"] / (arm_subc["U_core"] + 1e-300)
    w = R_KUBC - R_SUBC
    mid = 0.5 * (R_KUBC + R_SUBC)
    return {
        "R_SUBC": float(R_SUBC), "R_KUBC": float(R_KUBC),
        "primary_bracket": [float(R_SUBC), float(R_KUBC)],
        "width": float(w), "width_rel": float(w / (mid + 1e-300)),
        "g0_uncaged_gap": float(g0),
        "R_lo_conservative": float(R_lo), "R_hi_conservative": float(R_hi),
        "conservative_bracket": [float(R_lo), float(R_hi)],
        "R_SUBC_core": float(R_SUBC_core), "R_KUBC_core": float(R_KUBC_core),
        "core_convention_companion_NOT_A_BRACKET": [float(R_SUBC_core), float(R_KUBC_core)],
        "r_Z_bracket_rho_ASSUMED_1": [float(np.sqrt(max(R_SUBC, 0.0))),
                                      float(np.sqrt(max(R_KUBC, 0.0)))],
        "r_Z_bracket_conservative_rho_ASSUMED_1": [float(np.sqrt(max(R_lo, 0.0))),
                                                   float(np.sqrt(max(R_hi, 0.0)))],
        "scope": "K-BRACKET AROUND AN ASSUMED rho_eff/rho_0 == 1; rho NOT measured, "
                 "NOT bracketed; OWED-2 NOT discharged (prereg §7)",
        # ★G1, the VOID ordering gate — stated on the WHOLE-CELL pair ONLY (prereg §2.3):
        #  the design-time pilot found the SHIPPED CORE estimator can sit BELOW the SUBC
        #  lower bound on a perfectly correct extraction, so a core-stated gate would VOID
        #  the bench on a non-error.
        "G1_order_ok": bool(R_SUBC <= R_KUBC * (1.0 + G1_SLACK)),
        "core_estimator_inside_primary_bracket": bool(R_SUBC <= R_KUBC_core <= R_KUBC),
        "solver": {"subc_res": arm_subc["cg_residual"], "subc_iters": arm_subc["cg_iters"],
                   "subc_work_identity_rel": arm_subc["work_identity_rel"],
                   "kubc_res": arm_kubc["cg_residual"], "kubc_iters": arm_kubc["cg_iters"]},
    }


# ═════════════════════════════════════════════════════════════════════════════
# ★THE OUTCOME CLASSIFIER (prereg §5.3) + its exhaustiveness/reachability self-test
# ═════════════════════════════════════════════════════════════════════════════
def classify_bracket(lo, hi, threshold, void=False):
    """Frozen §5.3 partition — exhaustive and mutually exclusive by construction.
    A bracket ENDPOINT exactly ON the threshold reads STRADDLES (the conservative side;
    the boundary never belongs silently to a RESOLVES class)."""
    if void:
        return "VOID"
    if hi < threshold:
        return "RESOLVES-LOW"
    if lo > threshold:
        return "RESOLVES-HIGH"
    return "STRADDLES"


def selftest_partition():
    """Frozen §4B SELFTEST-PARTITION — the §5.3 Layer-1 reachability discharge (the #796
    `assert_partition` pattern, Rule-14). Walks a synthetic grid through the SAME
    classifier the verdict uses and asserts exhaustiveness, disjointness, and that each
    non-VOID class is returned by at least one tuple."""
    seen, rows = set(), []
    grid = [(0.10, 0.20), (0.10, 0.50), (0.10, 0.90), (0.40, 0.60),
            (0.50, 0.50), (0.60, 0.90), (0.90, 1.40), (1.00, 1.00)]
    for lo, hi in grid:
        for thr in (0.45, 0.5, 0.55, 1.0):
            cls = classify_bracket(lo, hi, thr)
            assert cls in ("RESOLVES-LOW", "RESOLVES-HIGH", "STRADDLES"), (lo, hi, thr, cls)
            seen.add(cls)
            rows.append({"lo": lo, "hi": hi, "threshold": thr, "class": cls})
    void_cls = classify_bracket(0.1, 0.9, 0.5, void=True)
    seen.add(void_cls)
    ok = seen == {"RESOLVES-LOW", "RESOLVES-HIGH", "STRADDLES", "VOID"}
    return {"n_tuples": len(rows), "classes_returned": sorted(seen),
            "every_class_reachable": bool(ok), "unclassified": 0,
            "selftest_partition_pass": bool(ok), "rows": rows}


# ═════════════════════════════════════════════════════════════════════════════
# GEOMETRY / OPERATOR HELPERS
# ═════════════════════════════════════════════════════════════════════════════
def setup(L):
    geom = build_finite_srs(L)
    pos, bi, bj, dhat, mid = geom
    N = pos.shape[0]
    act = active_mask(bi, bj, N)
    xc = 0.5 * (pos.max(axis=0) + pos.min(axis=0))
    V = float(np.prod(pos.max(axis=0) - pos.min(axis=0)))
    free = ~boundary_mask(pos, None)
    half = 0.25 * (pos.max(axis=0) - pos.min(axis=0)).mean()
    return {"geom": geom, "act": act, "xc": xc, "V": V, "free": free, "half": half,
            "L": L, "N": int(N), "M": int(bi.shape[0]), "n_active": int(act.sum())}


def operator(geom, k_a, k_s):
    dhat, bi, bj = geom[3], geom[1], geom[2]
    N = geom[0].shape[0]
    Phi = bond_tensors(dhat, k_a, k_s)
    diag = jacobi_diag(dhat, k_a, k_s, bi, bj, N)
    return Phi, diag


def cold_operator(geom):
    M = geom[1].shape[0]
    return operator(geom, np.full(M, float(RHO_STAR)), np.full(M, float(K_S)))


def measure_config(S, k_a, k_s, mode, unc):
    """Measure ONE configuration under BOTH boundary conditions and build the §2 ratios."""
    Phi, diag = operator(S["geom"], k_a, k_s)
    a_s = subc_solve(S["geom"], S["act"], Phi, diag, mode, S["xc"], S["V"], S["half"])
    a_k = kubc_solve(S["geom"], S["free"], Phi, diag, mode, S["xc"], S["V"], S["half"])
    out = bracket_from_pair(a_s, a_k, unc[mode]["subc"], unc[mode]["kubc"])
    out["abs"] = {"K_SUBC": a_s["M_abs"], "K_KUBC": a_k["M_abs"],
                  "absolute_order_ok": bool(a_s["M_abs"] <= a_k["M_abs"] * (1.0 + G1_SLACK))}
    return out


def uncaged_pair(S, modes=("hydro", "shear")):
    Phi0, diag0 = cold_operator(S["geom"])
    out = {}
    for m in modes:
        out[m] = {
            "subc": subc_solve(S["geom"], S["act"], Phi0, diag0, m, S["xc"], S["V"], S["half"]),
            "kubc": kubc_solve(S["geom"], S["free"], Phi0, diag0, m, S["xc"], S["V"], S["half"]),
        }
        out[m]["g0"] = float(out[m]["kubc"]["M_abs"] / (out[m]["subc"]["M_abs"] + 1e-300))
    return out


# ═════════════════════════════════════════════════════════════════════════════
# ★WHICH MODULUS IS THIS `K`?  (reported at every headline; NOT a frozen criterion)
# ═════════════════════════════════════════════════════════════════════════════
# An UNLABELLED "K" is ambiguous, so this driver tattoos the answer onto every record.
# Frozen §1.2 fixes BOTH ends of the hydrostatic mode to the pure DILATATIONAL response:
#   KUBC  E = ε·I  ⇒  dev(E) = 0  ⇒  U/V = ½K(tr E)² = 4.5·K·ε²   (no G term at all)
#   SUBC  Σ = σ·I  ⇒  dev(Σ) = 0  ⇒  U/V = ½σ̄²/K                  (no G term at all)
# so the bracketed modulus is the BULK modulus K — NOT the P-wave (longitudinal/
# constrained) modulus M = K + 4G/3 that a time-of-flight compression pulse reads, and
# NOT Young's E. The T2 shear companion is the pure DEVIATORIC modulus G by the same
# construction. Any downstream comparison to a ToF-derived speed must convert.
MODULUS_IDENTITY = {
    "hydro": "BULK modulus K (pure dilatation; dev=0 in BOTH boundary conditions) — "
             "NOT the P-wave modulus M = K + 4G/3, NOT Young's E",
    "shear": "SHEAR modulus G (pure deviator; tr=0 in BOTH boundary conditions)",
    "note": "frozen prereg §1.2 fixes both ends of each mode; the KUBC prefactor 4.5 = "
            "9/2 is ½·(tr I)² = ½·9 and the SUBC prefactor is ½/K — both pure-K forms. "
            "A ToF/acoustic comparison reads M = K + 4G/3 and is a DIFFERENT modulus.",
}


# ═════════════════════════════════════════════════════════════════════════════
# ★THE PINNED-SHELL CONFOUND (reported per configuration; a KUBC-SIDE confound only)
# ═════════════════════════════════════════════════════════════════════════════
def _pinned_shell_fraction(S, centers, r_cage, cage_w=CAGE_W):
    """★REPORTED, not frozen. The fraction of CAGE-SHELL nodes that lie INSIDE the KUBC
    Dirichlet layer (`boundary_mask`, `bw = 1.5`) and are therefore pinned to the affine
    macroscopic field rather than free to relax.

    Why it is shipped: `rve_aggregation_bench.cubic_cage_centers` documents a `margin =
    3.0` standoff "so cages never touch the KUBC boundary shell", but the cage SHELL has
    radius `r_cage + cage_w`, so at the larger `r_cage` values the shell reaches into the
    pinned layer. A PINNED soft shell cannot open — it is forced affine — which STIFFENS
    the KUBC-side composite. This is a confound on the KUBC (upper) side ONLY: the SUBC
    side prescribes NO displacement anywhere, so no shell node is pinned under SUBC and
    `pinned_shell_node_fraction_SUBC` is identically 0 by construction.

    That asymmetry is exactly what a two-sided bracket is positioned to expose, so the
    number is reported per configuration rather than argued about. It is NOT used to
    adjust, correct or reweight any bracket (frozen §0 pre-test check: RAW, no
    subtraction), and NO claim is made here about how much of the KUBC/SUBC gap it
    accounts for — that attribution is routed, not asserted."""
    pos = S["geom"][0]
    if not len(centers):
        return {"n_shell_nodes": 0, "pinned_fraction": 0.0}
    rmin = np.full(pos.shape[0], np.inf)
    for c in centers:
        rmin = np.minimum(rmin, np.linalg.norm(pos - np.asarray(c, float), axis=1))
    shell = (rmin >= r_cage) & (rmin < r_cage + cage_w)
    pinned = boundary_mask(pos, None) & shell
    n = int(shell.sum())
    return {"n_shell_nodes": n,
            "pinned_fraction": float(pinned.sum() / n) if n else 0.0,
            "pinned_fraction_SUBC": 0.0,
            "note": "KUBC-side confound only; SUBC prescribes no displacement anywhere, "
                    "so nothing is pinned under SUBC. Reported RAW, never subtracted."}


# ═════════════════════════════════════════════════════════════════════════════
# ★REALIZED vs INTENSIVE phase fractions (REPORTED for every configuration; free)
# ═════════════════════════════════════════════════════════════════════════════
def realized_fractions(S, centers, r_cage, s, cage_w=CAGE_W):
    """★NOT a frozen criterion — a LABELLING disclosure shipped for every configuration
    this lane brackets, at zero extra cost.

    `φ = (4/3)π r_cage³/s³` (`rve_aggregation_bench.packing_fraction`) is an INTENSIVE
    label: the cage-interior fraction of ONE cubic array cell of side `s`, i.e. the
    fraction an INFINITE array of this geometry would have. The finite bench cell does
    NOT realize it: `cubic_cage_centers` keeps a `margin = 3.0` standoff from the outer
    faces, so a finite cluster of `n_cages` cages sits in a COLD SURROUND inside the box.
    This function reports, side by side and without adjudicating anything:

      * `phi_intensive`   / `f_incl_intensive`   — the labels #782/#796 quote (per-cell)
      * `phi_realized_box`/ `f_incl_realized_box`— n_cages·V_sphere / V_box (whole cell)
      * `phi_realized_bond` / `shell_frac_bond`  — the LATTICE-LEVEL truth: the fraction
        of BONDS whose midpoint lies inside a cage interior, and the fraction on the
        graded shell. These are what the operator actually sees, and they are the only
        fractions that are not a continuum idealization.
      * `array_span` / `V_box` / `n_cages` — so the standoff is visible, not implied.

    Reported so that any cross-bench comparison can check it is comparing the SAME
    composite. This lane's own frozen configurations are fixed by the TUPLE
    (L, r_cage, s, cage_w, wall_class, s_rail) — never by a φ label — so nothing in this
    lane's bracket depends on which convention a reader prefers.
    """
    pos, bi, bj, dhat, mid = S["geom"]
    v_int = (4.0 / 3.0) * np.pi * r_cage ** 3
    v_coat = (4.0 / 3.0) * np.pi * (r_cage + cage_w) ** 3
    n = len(centers)
    rmin = np.full(mid.shape[0], np.inf)
    for c in centers:
        rmin = np.minimum(rmin, np.linalg.norm(mid - np.asarray(c, float), axis=1))
    cen = np.asarray(centers, float)
    span = (cen.max(axis=0) - cen.min(axis=0)) if n > 1 else np.zeros(3)
    return {
        "n_cages": int(n), "r_cage": float(r_cage), "s": float(s), "cage_w": float(cage_w),
        "V_box": float(S["V"]),
        "phi_intensive": float(packing_fraction(r_cage, s)),
        "f_incl_intensive": float(coated_inclusion_fraction(r_cage, s, cage_w)),
        "phi_realized_box": float(n * v_int / S["V"]),
        "f_incl_realized_box": float(n * v_coat / S["V"]),
        "phi_realized_bond": float(np.mean(rmin < r_cage)),
        "shell_frac_bond": float(np.mean((rmin >= r_cage) & (rmin < r_cage + cage_w))),
        "coated_frac_bond": float(np.mean(rmin < r_cage + cage_w)),
        "cage_array_span": [float(x) for x in span],
        "cage_standoff_margin": 3.0,
        "pinned_shell_node_fraction_KUBC": _pinned_shell_fraction(S, centers, r_cage,
                                                                 cage_w),
        "note": "INTENSIVE phi is a per-array-cell label; the finite bench cell realizes "
                "a smaller fraction because the cage cluster stands off the outer faces. "
                "The frozen configuration is the TUPLE (L, r_cage, s, cage_w, wall, rail), "
                "not a phi label — no bracket here depends on the convention.",
    }


# ═════════════════════════════════════════════════════════════════════════════
# ★SUPPLEMENTARY AXIS (ADDITIVE, NOT the frozen deliverable): the P-WAVE / VRH
#  longitudinal modulus M = K + 4G/3 — the modulus a normal-incidence impedance
#  actually carries, bracketed by the SAME two boundary conditions.
# ═════════════════════════════════════════════════════════════════════════════
def m_axis(res_h, res_s, unc_m):
    """★NOT A FROZEN CRITERION — a clearly-labelled ADDITIONAL axis shipped alongside the
    frozen bulk-K bracket (KEEP-BOTH). The frozen deliverable is and remains the BULK-K
    bracket of prereg §1.2/§2; nothing here amends, replaces or reweights it.

    WHY IT IS SHIPPED. The frozen `r_Z = √((K_eff/K_0)(ρ_eff/ρ_0))` is built on the BULK
    modulus K. But a normal-incidence acoustic impedance is `Z = ρ c_P = √(ρ·M)` with the
    P-WAVE (longitudinal / constrained) modulus `M = K + 4G/3`, and `√(ρK)` is the correct
    impedance ONLY for a medium with `G = 0`. This composite is NOT a fluid — its measured
    `G_eff/G_0 ≈ 0.67` — so the two differ materially. Whether the corpus discriminator
    should ride K or M is a DEFINITION question this lane does not own and does not
    settle; it is ROUTED. The axis is shipped so the question can be adjudicated on data.

    HOW IT IS BOUNDED. `M = K + 4G/3` is monotone increasing in BOTH K and G, and the
    Hill/Huet ordering brackets each of them in the same direction under the same pair of
    boundary conditions. Hence `M_SUBC = K_SUBC + 4G_SUBC/3 ≤ M* ≤ K_KUBC + 4G_KUBC/3 =
    M_KUBC` is a legitimate bracket on the ABSOLUTE P-wave modulus, inheriting its rigor
    from the two absolute brackets. The RATIO carries the SAME §2.1 caveat as the bulk
    axis (the uncaged reference is itself boundary-conditioned), stated, not glossed."""
    Ks, Kk = res_h["abs"]["K_SUBC"], res_h["abs"]["K_KUBC"]
    Gs, Gk = res_s["abs"]["K_SUBC"], res_s["abs"]["K_KUBC"]
    Ms, Mk = Ks + 4.0 * Gs / 3.0, Kk + 4.0 * Gk / 3.0
    M0s, M0k = unc_m["subc"], unc_m["kubc"]
    R_s, R_k = Ms / (M0s + 1e-300), Mk / (M0k + 1e-300)
    return {
        "LABEL": "SUPPLEMENTARY AXIS — NOT the frozen deliverable (the frozen bracket is "
                 "on BULK K, prereg sec 1.2). Shipped additively for the modulus-identity "
                 "question, which is ROUTED to Grant, not settled here.",
        "modulus_identity": "P-WAVE / VRH longitudinal modulus M = K + 4G/3 (= C11 for an "
                            "isotropic average) — the modulus a normal-incidence "
                            "impedance Z = rho*c_P carries",
        "M_SUBC_abs": float(Ms), "M_KUBC_abs": float(Mk),
        "M_SUBC_uncaged_abs": float(M0s), "M_KUBC_uncaged_abs": float(M0k),
        "absolute_bracket_M": [float(Ms), float(Mk)],
        "absolute_order_ok": bool(Ms <= Mk * (1.0 + G1_SLACK)),
        "R_M_SUBC": float(R_s), "R_M_KUBC": float(R_k),
        "primary_bracket_M": [float(min(R_s, R_k)), float(max(R_s, R_k))],
        "ratio_order_SUBC_le_KUBC": bool(R_s <= R_k * (1.0 + G1_SLACK)),
        "g0_M_uncaged": float(M0k / (M0s + 1e-300)),
        "r_Z_M_bracket_rho_ASSUMED_1": [float(np.sqrt(max(min(R_s, R_k), 0.0))),
                                        float(np.sqrt(max(max(R_s, R_k), 0.0)))],
        "K_only_counterpart_for_comparison": {
            "R_K_SUBC": res_h["R_SUBC"], "R_K_KUBC": res_h["R_KUBC"],
            "r_Z_K_bracket": res_h["r_Z_bracket_rho_ASSUMED_1"]},
        "scope": "K-and-G-bracketed M around an ASSUMED rho_eff/rho_0 == 1; rho is NOT "
                 "measured and NOT bracketed by this lane (OWED-2 stands, prereg sec 7)",
    }


# ═════════════════════════════════════════════════════════════════════════════
# ★§4B — THE DELIBERATELY-BROKEN-EXTRACTION FIREABILITY SELF-TESTS
#   (a gate that cannot be shown to fire is a checklist, not a gate)
# ═════════════════════════════════════════════════════════════════════════════
def selftest_G1(pair_unc, pair_arm):
    """Frozen §4B: `SELFTEST-G1: recompute R_SUBC with the ratio taken in the KUBC
    direction (U_SUBC^arm/U_SUBC^uncaged instead of U_SUBC^uncaged/U_SUBC^arm) on the
    bulk_only_cold φ_sf configuration, and assert G1 REPORTS A VIOLATION.`
    Frozen acceptance: `selftest_G1_fires = True`."""
    R_SUBC_correct = pair_unc["U_total"] / (pair_arm["subc"]["U_total"] + 1e-300)
    R_SUBC_inverted = pair_arm["subc"]["U_total"] / (pair_unc["U_total"] + 1e-300)
    R_KUBC = pair_arm["R_KUBC"]
    ok_correct = bool(R_SUBC_correct <= R_KUBC * (1.0 + G1_SLACK))
    ok_inverted = bool(R_SUBC_inverted <= R_KUBC * (1.0 + G1_SLACK))
    return {
        "R_SUBC_correct_direction": float(R_SUBC_correct),
        "R_SUBC_INVERTED_broken": float(R_SUBC_inverted),
        "R_KUBC": float(R_KUBC),
        "G1_order_ok_on_correct_extraction": ok_correct,
        "G1_order_ok_on_BROKEN_extraction": ok_inverted,
        "selftest_G1_fires": bool(ok_correct and not ok_inverted),
        "reason": "the inverted ratio is 1/R_SUBC which, for any softening arm "
                  "(R_SUBC < 1), exceeds 1 > R_KUBC — so the VOID ordering gate must "
                  "report a violation on it and must NOT on the correct extraction.",
    }


def selftest_G2b(g0_by_L):
    """Frozen §4B: `SELFTEST-G2b: recompute the uncaged g_0 using the NOMINAL applied σ
    instead of the Hill-lemma Σ̄ read from the shipped load set, and assert G2b REPORTS A
    VIOLATION (g_0 < 1 or non-monotone in L).` Frozen acceptance: `selftest_G2b_fires =
    True`, with the frozen calibration latitude: `if the nominal-σ mis-normalization does
    not push g_0 below 1 at every L, the self-test is accepted on the MONOTONICITY clause
    alone provided the driver SHIPS the computed g_0(L) under both normalizations so the
    reader can see which clause fired`.

    ★BOTH normalizations are shipped unconditionally (the frozen latitude's SHIPS-clause
    is discharged whatever the outcome), and the two available readings of that latitude
    sentence are computed SEPARATELY and reported side by side rather than resolved here
    (flag-don't-fix). Nothing is relabelled to make a clause fire.
    """
    Ls = sorted(g0_by_L)
    gh = [g0_by_L[L]["g0_hill"] for L in Ls]
    gn = [g0_by_L[L]["g0_nominal"] for L in Ls]

    def clauses(g):
        ge1 = all(x >= 1.0 for x in g)
        mono = all(g[i] >= g[i + 1] - 1e-12 for i in range(len(g) - 1))
        return {"all_ge_1": bool(ge1), "non_increasing_in_L": bool(mono),
                "G2b_violation_reported": bool((not ge1) or (not mono))}

    ch, cn = clauses(gh), clauses(gn)
    fires_below1 = not cn["all_ge_1"]
    fires_mono = not cn["non_increasing_in_L"]
    return {
        "L_grid": Ls,
        "g0_hill_normalized": [float(x) for x in gh],
        "g0_NOMINAL_sigma_MIS_normalized": [float(x) for x in gn],
        "sigma_bar_over_sigma": [float(g0_by_L[L]["sigma_bar"]) for L in Ls],
        "inverse_sigma_bar_squared": [float(1.0 / g0_by_L[L]["sigma_bar"] ** 2) for L in Ls],
        "G2b_on_hill_normalization": ch,
        "G2b_on_nominal_MIS_normalization": cn,
        "fired_via_below_1_clause": bool(fires_below1),
        "fired_via_MONOTONICITY_clause": bool(fires_mono),
        # ── the two readings of the frozen latitude sentence, computed, not chosen ──
        "selftest_G2b_fires_STRICT": bool(cn["G2b_violation_reported"]),
        "selftest_G2b_fires_LATITUDE_SHIPS_CLAUSE": True,
        "selftest_G2b_fires": bool(cn["G2b_violation_reported"]),
        "both_normalizations_shipped": True,
        "reason": "the mis-normalization inflates K_SUBC by 1/(Σ̄/σ)²; whether that is "
                  "enough to force g_0 below 1 or to break its monotonicity is a "
                  "COMPUTED question, answered from the shipped arrays above.",
    }


# ═════════════════════════════════════════════════════════════════════════════
# ★THE UNCAGED REFERENCE + the g_0(L) finite-size gap (frozen §4 G2b)
# ═════════════════════════════════════════════════════════════════════════════
def uncaged_and_g0(S, modes=("hydro", "shear")):
    """The cold uncaged pair under BOTH boundary conditions, plus the frozen §4 G2b
    absolute gap `g_0(L) = K_KUBC^uncaged/K_SUBC^uncaged` — and, for SELFTEST-G2b, the
    same gap recomputed with the NOMINAL applied σ in place of the Hill-lemma Σ̄."""
    unc = uncaged_pair(S, modes)
    out = {"L": S["L"], "N": S["N"], "M": S["M"], "n_active": S["n_active"],
           "V": S["V"], "by_mode": {}}
    for m in modes:
        s_, k_ = unc[m]["subc"], unc[m]["kubc"]
        sbar = s_["sigma_bar"]
        K_nominal = (SIGMA_PROBE ** 2) * S["V"] / (2.0 * s_["U_total"])
        out["by_mode"][m] = {
            "modulus_identity": MODULUS_IDENTITY[m],
            "K_SUBC_abs": float(s_["M_abs"]), "K_KUBC_abs": float(k_["M_abs"]),
            "sigma_bar": float(sbar), "sigma_nominal": float(SIGMA_PROBE),
            "g0_hill": float(k_["M_abs"] / (s_["M_abs"] + 1e-300)),
            "g0_nominal": float(k_["M_abs"] / (K_nominal + 1e-300)),
            "subc_cg_residual": s_["cg_residual"], "subc_cg_iters": s_["cg_iters"],
            "subc_work_identity_rel": s_["work_identity_rel"],
            "kubc_cg_residual": k_["cg_residual"], "kubc_cg_iters": k_["cg_iters"],
            "net_force_norm": s_["net_force_norm"],
            "net_torque_norm": s_["net_torque_norm"],
            "net_torque_norm_rel": float(s_["net_torque_norm"]
                                         / (SIGMA_PROBE * S["V"] ** (2.0 / 3.0)
                                            * S["V"] ** (1.0 / 3.0) + 1e-300)),
        }
    return out, unc


# ═════════════════════════════════════════════════════════════════════════════
# ★THE FROZEN §3 CONFIGURATION RUNNER
# ═════════════════════════════════════════════════════════════════════════════
def run_cage_config(S, unc, label, wall_class, r_cage, s, modes=("hydro",),
                    eps_pre=0.0, s_rail=S_RAIL_DEEP):
    """One frozen §3 A/C cage configuration under BOTH boundary conditions.
    Rule-14: the cage stiffness field is the SHIPPED #782 `cage_bond_stiffness` — this
    lane changes NOTHING about the medium, only the outer-surface condition."""
    geom = S["geom"]
    centers = cubic_cage_centers(S["L"], s, S["xc"])
    k_a, k_s = cage_bond_stiffness(geom[3], geom[4], centers, r_cage, CAGE_W,
                                   wall_class, s_rail, eps_pre)
    row = {"config": label, "L": S["L"], "wall_class": wall_class,
           "r_cage": float(r_cage), "s": float(s), "eps_pre": float(eps_pre),
           "s_rail": float(s_rail),
           "fractions": realized_fractions(S, centers, r_cage, s),
           "by_mode": {}}
    for m in modes:
        res = measure_config(S, k_a, k_s, m, unc)
        res["modulus_identity"] = MODULUS_IDENTITY[m]
        row["by_mode"][m] = res
    return row


def run_operator_config(S, unc, label, k_a, k_s, modes=("hydro",), extra=None):
    """One frozen §3 B configuration supplied as an EXPLICIT (k_a, k_s) bond-stiffness
    pair — the frozen-tangent-operator carve (§1.4): the operator is held BYTE-IDENTICAL
    between the SUBC and the KUBC solve, which is what makes the pair a bracket on a
    FIXED linear microstructure rather than a comparison of two different media."""
    row = {"config": label, "L": S["L"], "operator": "explicit frozen (k_a, k_s) pair",
           "by_mode": {}}
    if extra:
        row.update(extra)
    for m in modes:
        res = measure_config(S, k_a, k_s, m, unc)
        res["modulus_identity"] = MODULUS_IDENTITY[m]
        row["by_mode"][m] = res
    return row


# ═════════════════════════════════════════════════════════════════════════════
# ★§3 B — THE #796 GROWN ARM, bracketed on its FROZEN TANGENT OPERATOR (§1.4)
# ═════════════════════════════════════════════════════════════════════════════
def grown_frozen_tangent_operator(S):
    """Reconstruct the #796 `fixed_budget` grown operating point `u_0` and freeze the
    tangent operator `Φ_eff(u_0) = k_a(d̂⊗d̂) + k_shear,eff(u_0)(I − d̂⊗d̂)` at it.

    Frozen §1.4: `The grown arm is bracketed on the FROZEN secant/tangent operator
    Φ_eff(u_0) at the #796 grown operating point — the same u-independent operator #796's
    PAINTED-ANISOTROPIC arm uses — held byte-identical between the KUBC and SUBC solves`.
    That is the object the bound theorem applies to: a FIXED linear microstructure under
    two boundary conditions. Rule-14 — the grow itself is the SHIPPED #796 code path."""
    arm = grow_verdict_arm(S["geom"], S["free"], S["xc"], VERDICT_P_REF, "fixed_budget",
                           wall_class=VERDICT_WALL, s_rail=VERDICT_S_RAIL)
    kse = np.maximum(arm["sol"]["kse_raw"], KSE_SOLVE_FLOOR)
    return arm, np.asarray(arm["k_a_bond"], float), np.asarray(kse, float)


def subc_grown_companion(S, unc, sigma=VERDICT_SRC_SIGMA, p0=VERDICT_P_REF,
                         outer_cap=COMPANION_OUTER_CAP, wall_s=COMPANION_WALL_CLOCK_S):
    """★§3 D — the fully-SUBC-GROWN companion. Frozen: `Reported ONLY if it converges
    within the frozen budget; explicitly NOT part of any bracket, because its
    microstructure co-varies with the boundary condition`, budget `the fully-SUBC-grown
    companion is capped at 40 outer iterations and 20 minutes wall-clock; on exceeding
    either it is reported as NOT-RUN with the reason, and no verdict depends on it`.

    Grow under a TRACTION-FREE outer boundary (pure Neumann, only the per-core radiation
    body-force source, translation-projected) through the #796 state-dependent operator,
    then probe the resulting frozen tangent under traction. NOT a bracket — the grown
    microstructure `T(r)` co-varies with the boundary condition, so the SUBC-grown and
    KUBC-grown specimens are DIFFERENT MEDIA and their pair brackets nothing (§1.4)."""
    t0 = time.time()
    geom = S["geom"]
    pos, bi, bj, dhat, mid = geom
    N = pos.shape[0]
    centers, k_a_bond, k_s_cold = build_cage(geom, VERDICT_WALL, VERDICT_S_RAIL)
    k_a_bond = np.asarray(k_a_bond, float)
    k_s_cold = np.asarray(k_s_cold, float)
    b_src = radiation_source(pos, centers, p0, sigma, r_core=PHI_SF_RCAGE)
    b_src = b_src * S["act"][:, None]
    u = np.zeros((N, 3))
    hist = []
    reason = None
    converged = False
    kse_prev = k_shear_eff(bond_axial_strain(u, bi, bj, dhat), k_s_cold, k_a_bond)
    for it in range(outer_cap):
        if time.time() - t0 > wall_s:
            reason = (f"WALL-CLOCK budget exceeded at outer iteration {it} "
                      f"({time.time() - t0:.0f} s > {wall_s:.0f} s)")
            break
        Phi, kse_raw, _eps = state_operator(u, bi, bj, dhat, k_s_cold, k_a_bond)
        diag = jacobi_diag(dhat, k_a_bond, np.maximum(kse_raw, KSE_SOLVE_FLOOR),
                           bi, bj, N)
        u, res, its = cg_neumann(Phi, bi, bj, N, S["act"], b_src, diag,
                                 tol=1e-8, itmax=SUBC_MAX)
        # self-consistency measured on the operator BEFORE vs AFTER this solve — i.e.
        # k_shear,eff re-evaluated at the NEW iterate against the one the solve used.
        # (Comparing the pre-solve operator with the previous pre-solve operator would
        # return 0 on the first pass and declare convergence at u = 0 — a false stop.)
        eps_new = bond_axial_strain(u, bi, bj, dhat)
        kse_new = k_shear_eff(eps_new, k_s_cold, k_a_bond)
        dsc = float(np.max(np.abs(kse_new - kse_raw)) / (float(np.max(k_s_cold)) + 1e-300))
        kse_prev = kse_new
        hist.append({"outer": it + 1, "cg_res": float(res), "cg_iters": int(its),
                     "dsc": dsc, "min_kse_raw": float(kse_new.min()),
                     "peak_A": float(np.max(np.abs(eps_new)))})
        if dsc <= OUTER_SC_TOL:
            converged = True
            break
    if not converged and reason is None:
        reason = f"OUTER-ITERATION cap {outer_cap} reached without self-consistency"
    out = {
        "config": "fully_SUBC_grown_companion",
        "NOT_A_BRACKET": True,
        "frozen_status": ("A fully-SUBC-grown arm, if run, is reported as a labelled "
                          "companion and is explicitly NOT part of any bracket, because "
                          "its microstructure co-varies with the boundary condition"),
        "budget": {"outer_cap": outer_cap, "wall_clock_s": wall_s},
        "outer_history": hist, "converged": bool(converged),
        "wall_clock_s": float(time.time() - t0),
        "not_run_reason": None if converged else reason,
    }
    if not converged:
        out["status"] = "NOT-RUN (budget exceeded / non-convergent) — no verdict depends on it"
        return out
    Phi, kse_raw, eps = state_operator(u, bi, bj, dhat, k_s_cold, k_a_bond)
    kse = np.maximum(kse_raw, KSE_SOLVE_FLOOR)
    out["status"] = "CONVERGED — reported as a labelled COMPANION only"
    out["min_kse_raw"] = float(kse_raw.min())
    out["peak_A"] = float(np.max(np.abs(eps)))
    out["max_abs_T"] = float(np.max(np.abs(K_A * eps)))
    out["measured"] = run_operator_config(S, unc, "fully_SUBC_grown_companion",
                                          k_a_bond, kse, ("hydro",))["by_mode"]
    return out


# ═════════════════════════════════════════════════════════════════════════════
# ★§4 — THE FROZEN GATES (every gate reports PASS/FAIL from the shipped JSON)
# ═════════════════════════════════════════════════════════════════════════════
def _iter_measurements(configs):
    """Walk every (config, mode) measurement dict in the shipped configuration list."""
    for row in configs:
        for mode, res in row["by_mode"].items():
            yield row["config"], row.get("L"), mode, res


def gate_G1(configs, unc_meta_by_L):
    """Frozen §4 G1 — the VOID ordering gate, an EXTRACTION-CORRECTNESS gate, stated on
    the WHOLE-CELL pair ONLY (§2.3): `for EVERY bracketed configuration and BOTH modes,
    R_SUBC ≤ R_KUBC must hold on the WHOLE-CELL pair, with a numerical slack of 1e-6
    relative`, plus `G1 also requires the ABSOLUTE ordering K_SUBC ≤ K_KUBC and G_SUBC ≤
    G_KUBC on every configuration INCLUDING the uncaged reference.`"""
    rows, violations = [], []
    for cfg, L, mode, res in _iter_measurements(configs):
        ok = bool(res["G1_order_ok"] and res["abs"]["absolute_order_ok"])
        rows.append({"config": cfg, "L": L, "mode": mode,
                     "R_SUBC": res["R_SUBC"], "R_KUBC": res["R_KUBC"],
                     "ratio_order_ok": res["G1_order_ok"],
                     "absolute_order_ok": res["abs"]["absolute_order_ok"], "ok": ok})
        if not ok:
            violations.append(rows[-1])
    for L, meta in sorted(unc_meta_by_L.items()):
        for mode, m in meta["by_mode"].items():
            ok = bool(m["K_SUBC_abs"] <= m["K_KUBC_abs"] * (1.0 + G1_SLACK))
            rows.append({"config": "uncaged_reference", "L": L, "mode": mode,
                         "R_SUBC": 1.0, "R_KUBC": 1.0, "ratio_order_ok": True,
                         "absolute_order_ok": ok, "ok": ok})
            if not ok:
                violations.append(rows[-1])
    ratio_only = [v for v in violations if v["absolute_order_ok"]
                  and not v["ratio_order_ok"]]
    return {"rows": rows, "n_checked": len(rows), "violations": violations,
            # ★TWO VOID SCOPINGS, both computed and shipped — NOT adjudicated here.
            # Frozen G1 reads "for EVERY bracketed configuration and BOTH modes ... the
            # bench is VOID for that configuration". "that configuration" admits a STRICT
            # reading (a violation in EITHER mode voids the whole configuration, hydro
            # included) and a per-(configuration,mode) reading (only the violating
            # measurement voids). The strict reading is the one that voids MORE, so it is
            # carried as the headline disposition; both are shipped so the scoping is a
            # one-line adjudication for Grant / the auditor rather than a driver choice.
            "void_configs_STRICT": sorted({v["config"] for v in violations}),
            "void_config_modes": sorted({f"{v['config']}::{v['mode']}"
                                         for v in violations}),
            "G1_PASS": bool(not violations),
            "absolute_theorem_grade_ordering_holds_everywhere":
                bool(all(r["absolute_order_ok"] for r in rows)),
            "violations_that_are_RATIO_ONLY_with_absolute_ordering_intact": ratio_only,
            "note": "a violation means the SUBC extraction is WRONG — the bench is VOID "
                    "for that configuration and it is an instrument failure, NEVER a "
                    "physical finding that the lower bound exceeds the upper bound. "
                    "Stated on the WHOLE-CELL pair only (prereg §2.3).",
            "flag_dont_fix": (
                "SURFACED, NOT RESOLVED: every violation below is RATIO-ONLY — the "
                "theorem-grade ABSOLUTE ordering K_SUBC <= K_KUBC (G1's second clause) "
                "holds on the very same rows. R_KUBC/R_SUBC = g0_arm/g0_uncaged, so the "
                "PRIMARY ratio pair is bound-ordered only when the ARM's uncaged-gap "
                "exceeds the REFERENCE's; prereg sec 2.1 already states the PRIMARY "
                "bracket is 'NOT theorem-grade on the RATIO'. The frozen inference 'a "
                "violation means the SUBC extraction is WRONG' is therefore NOT supported "
                "by the data at these rows. The gate outcome is reported AS FROZEN "
                "(VOID) and the criterion question is ROUTED, not relabelled.")}


def gate_G2(null_row, g0_by_L, st_g2b):
    """Frozen §4 G2 — split into its IDENTITY half and its FIREABLE half."""
    ident = {}
    for mode, res in null_row["by_mode"].items():
        ident[mode] = {"R_SUBC": res["R_SUBC"], "R_KUBC": res["R_KUBC"],
                       "dev_from_1": max(abs(res["R_SUBC"] - 1.0),
                                         abs(res["R_KUBC"] - 1.0)),
                       "ok": bool(abs(res["R_SUBC"] - 1.0) <= G2A_TOL
                                  and abs(res["R_KUBC"] - 1.0) <= G2A_TOL)}
    Ls = sorted(g0_by_L)
    gh = [g0_by_L[L]["g0_hill"] for L in Ls]
    return {
        "G2a_IDENTITY_not_a_fireable_gate": {
            "by_mode": ident, "holds": bool(all(v["ok"] for v in ident.values())),
            "label": "IDENTITY (numerator and denominator are the same solve) — a "
                     "pipeline sanity check, NEVER counted as a discriminating gate"},
        "G2b_FIREABLE": {
            "L_grid": Ls, "g0_by_L": [float(x) for x in gh],
            "all_ge_1": bool(all(x >= 1.0 for x in gh)),
            "non_increasing_in_L": bool(all(gh[i] >= gh[i + 1] - 1e-12
                                            for i in range(len(gh) - 1))),
            "G2b_PASS": bool(all(x >= 1.0 for x in gh)
                             and all(gh[i] >= gh[i + 1] - 1e-12
                                     for i in range(len(gh) - 1)))},
        "SELFTEST_G2b": st_g2b,
    }


def gate_G4_G5(configs, unc_meta_by_L):
    """Frozen §4 G4 (every SUBC solve reaches rel residual ≤ 1e-9 within the 60000 cap)
    and G5 (the work identity |U − ½f·u|/U ≤ 1e-8 — convergence-EQUIVALENT, labelled)."""
    res_max, it_max, work_max, rows = 0.0, 0, 0.0, []
    for cfg, L, mode, r in _iter_measurements(configs):
        s = r["solver"]
        res_max = max(res_max, s["subc_res"])
        it_max = max(it_max, s["subc_iters"])
        work_max = max(work_max, s["subc_work_identity_rel"])
        rows.append({"config": cfg, "L": L, "mode": mode, "subc_res": s["subc_res"],
                     "subc_iters": s["subc_iters"],
                     "work_identity_rel": s["subc_work_identity_rel"]})
    for L, meta in sorted(unc_meta_by_L.items()):
        for mode, m in meta["by_mode"].items():
            res_max = max(res_max, m["subc_cg_residual"])
            it_max = max(it_max, m["subc_cg_iters"])
            work_max = max(work_max, m["subc_work_identity_rel"])
            rows.append({"config": "uncaged_reference", "L": L, "mode": mode,
                         "subc_res": m["subc_cg_residual"],
                         "subc_iters": m["subc_cg_iters"],
                         "work_identity_rel": m["subc_work_identity_rel"]})
    return {
        "G4": {"worst_subc_residual": float(res_max), "worst_subc_iters": int(it_max),
               "tol": SUBC_TOL, "cap": SUBC_MAX, "n_solves": len(rows),
               "G4_PASS": bool(res_max <= SUBC_TOL and it_max < SUBC_MAX)},
        "G5": {"worst_work_identity_rel": float(work_max), "tol": G5_TOL,
               "G5_PASS": bool(work_max <= G5_TOL),
               "label": "convergence-EQUIVALENT (exact iff K u = f), NOT an independent "
                        "gate — labelled as such per the frozen §4 G5"},
        "per_solve": rows,
    }


def gate_G6(repro):
    """Frozen §4 G6 — the reproduction cross-check against the MERGED corpus. A failure
    means our reconstruction of the shipped arms is not the shipped arm, so §5 is not read
    at all (frozen §5.5 item 6): `G6: the driver's own KUBC re-computations must reproduce
    the merged numbers within 2e-3 relative`."""
    rows = []
    for k, (got, target, src) in repro.items():
        rel = abs(got - target) / (abs(target) + 1e-300)
        rows.append({"quantity": k, "recomputed": float(got), "merged_target": float(target),
                     "rel": float(rel), "source": src, "ok": bool(rel <= G6_TOL)})
    return {"tol": G6_TOL, "rows": rows, "G6_PASS": bool(all(r["ok"] for r in rows)),
            "precondition_note": "G6 is a PRECONDITION for reading §5 (frozen §5.5 item 6)"}


def gate_G7(mirror_rows, size_rows):
    """Frozen §4 G7a (STOP-gate mirror under BOTH boundary conditions) and G7b (the
    PRIMARY bracket-width size trend at φ_sf must be non-increasing within 0.02)."""
    soft = [r for r in mirror_rows if r["wall_class"] == "bulk_only"]
    rigid = [r for r in mirror_rows if r["wall_class"] == "rigid"]
    a = {"bulk_only_softens_BOTH_BCs": bool(all(r["R_SUBC"] < 1.0 and r["R_KUBC"] < 1.0
                                                for r in soft)),
         "rigid_stiffens_BOTH_BCs": bool(all(r["R_SUBC"] > 1.0 and r["R_KUBC"] > 1.0
                                             for r in rigid)),
         "rows": mirror_rows}
    a["G7a_PASS"] = bool(a["bulk_only_softens_BOTH_BCs"] and a["rigid_stiffens_BOTH_BCs"])
    ws = [r["width"] for r in size_rows]
    mono = all(ws[i] >= ws[i + 1] - G7B_SLACK for i in range(len(ws) - 1))
    b = {"by_L": size_rows, "widths": [float(x) for x in ws], "slack": G7B_SLACK,
         "non_increasing_within_slack": bool(mono), "G7b_PASS": bool(mono),
         "size_converged_label": ("SIZE-CONVERGED" if mono else "NOT SIZE-CONVERGED "
                                  "(a valid bound, but may NOT be cited as a tight one)")}
    return {"G7a_mirror": a, "G7b_size_trend": b}


# ═════════════════════════════════════════════════════════════════════════════
# ★§5 — THE FROZEN READ (bracket vs threshold; the §5.3 four-class partition)
# ═════════════════════════════════════════════════════════════════════════════
def read_config(cfg, L, mode, res, void_strict, void_permode):
    """Frozen §5.1 per-configuration read + the §5.2 threshold walk through the SAME
    classifier the §4B SELFTEST-PARTITION exercises (reconcile-don't-declare).

    The frozen §5.3 VOID class is emitted under BOTH G1 void-scopings (see `gate_G1`),
    so the scoping is visible as data rather than baked in by the driver."""
    rz_p = res["r_Z_bracket_rho_ASSUMED_1"]
    rz_c = res["r_Z_bracket_conservative_rho_ASSUMED_1"]
    R_p = res["primary_bracket"]
    out = {
        "config": cfg, "L": L, "mode": mode,
        "modulus_identity": res["modulus_identity"],
        "R_SUBC": res["R_SUBC"], "R_KUBC": res["R_KUBC"],
        "primary_bracket": R_p, "width": res["width"], "width_rel": res["width_rel"],
        "conservative_bracket": res["conservative_bracket"],
        "g0_uncaged_gap": res["g0_uncaged_gap"],
        "R_SUBC_core": res["R_SUBC_core"], "R_KUBC_core": res["R_KUBC_core"],
        "core_convention_companion_NOT_A_BRACKET":
            res["core_convention_companion_NOT_A_BRACKET"],
        "core_estimator_inside_primary_bracket":
            res["core_estimator_inside_primary_bracket"],
        "r_Z_bracket_rho_ASSUMED_1": rz_p,
        "r_Z_bracket_conservative_rho_ASSUMED_1": rz_c,
        "scope": res["scope"], "solver": res["solver"], "G1_order_ok": res["G1_order_ok"],
        "absolute_order_ok": res["abs"]["absolute_order_ok"],
        "VOID_strict_per_configuration": bool(void_strict),
        "VOID_per_configuration_and_mode": bool(void_permode),
        "classes": {}, "classes_void_scope_per_mode": {},
    }
    for name, thr in (("T1_rZ_0.50", T1_RZ), ("T2_rZ_0.45", T2_RZ[0]),
                      ("T2_rZ_0.55", T2_RZ[1])):
        for suf, br in (("_PRIMARY", rz_p), ("_CONSERVATIVE", rz_c)):
            out["classes"][name + suf] = classify_bracket(br[0], br[1], thr, void_strict)
            out["classes_void_scope_per_mode"][name + suf] = classify_bracket(
                br[0], br[1], thr, void_permode)
    out["classes"]["T3_R_1.0_PRIMARY"] = classify_bracket(R_p[0], R_p[1], T3_R,
                                                          void_strict)
    out["classes_void_scope_per_mode"]["T3_R_1.0_PRIMARY"] = classify_bracket(
        R_p[0], R_p[1], T3_R, void_permode)
    # the class the bracket WOULD carry with the G1 VOID overlay removed entirely — the
    # threshold relation itself, shipped so the VOID overlay is separable from the read
    out["classes_no_void_overlay"] = {
        "T1_rZ_0.50_PRIMARY": classify_bracket(rz_p[0], rz_p[1], T1_RZ, False),
        "T1_rZ_0.50_CONSERVATIVE": classify_bracket(rz_c[0], rz_c[1], T1_RZ, False),
        "T2_rZ_0.45_PRIMARY": classify_bracket(rz_p[0], rz_p[1], T2_RZ[0], False),
        "T2_rZ_0.55_PRIMARY": classify_bracket(rz_p[0], rz_p[1], T2_RZ[1], False),
        "T3_R_1.0_PRIMARY": classify_bracket(R_p[0], R_p[1], T3_R, False),
    }
    return out


def verdict(reads, grown_lift, g1):
    """Frozen §5.4 HEADLINE + the §5.5 pre-registered disposition per outcome class."""
    by = {(r["config"], r["mode"]): r for r in reads}

    def head(cfg, mode="hydro"):
        r = by.get((cfg, mode))
        if r is None:
            return None
        return {"config": cfg, "mode": mode,
                "modulus_identity": r["modulus_identity"],
                "primary_r_Z_bracket_rho_ASSUMED_1": r["r_Z_bracket_rho_ASSUMED_1"],
                "conservative_r_Z_bracket_rho_ASSUMED_1":
                    r["r_Z_bracket_conservative_rho_ASSUMED_1"],
                "primary_K_bracket": r["primary_bracket"],
                "conservative_K_bracket": r["conservative_bracket"],
                "width": r["width"], "width_rel": r["width_rel"],
                "g0_uncaged_gap": r["g0_uncaged_gap"],
                "VOID_strict_per_configuration": r["VOID_strict_per_configuration"],
                "VOID_per_configuration_and_mode": r["VOID_per_configuration_and_mode"],
                "class_vs_T1_PRIMARY": r["classes"]["T1_rZ_0.50_PRIMARY"],
                "class_vs_T1_CONSERVATIVE": r["classes"]["T1_rZ_0.50_CONSERVATIVE"],
                "class_vs_T2lo_PRIMARY": r["classes"]["T2_rZ_0.45_PRIMARY"],
                "class_vs_T2hi_PRIMARY": r["classes"]["T2_rZ_0.55_PRIMARY"],
                "classes_void_scope_per_mode": r["classes_void_scope_per_mode"],
                "classes_no_void_overlay": r["classes_no_void_overlay"],
                "banked_core_convention_number": r["R_KUBC_core"],
                "core_estimator_inside_primary_bracket":
                    r["core_estimator_inside_primary_bracket"]}

    disp = []
    for r in reads:
        c1 = r["classes"]["T1_rZ_0.50_PRIMARY"]
        if c1 == "VOID":
            d = ("VOID — bracket NOT reported as physics; the standing merged verdict for "
                 "this configuration is left exactly as merged (frozen §5.5 item 4)")
        elif c1 == "STRADDLES":
            d = ("BOUND-CONDITIONAL — the corpus verdict is NOT tightened in either "
                 "direction; #782 BIN-4 and #796 UNDETERMINED STAND UNCHANGED; no new "
                 "bin, no side picked, no rescue (frozen §5.5 item 1)")
        elif c1 == "RESOLVES-LOW":
            d = ("the macro-side reading is BOUND-ROBUST for this arm — an INPUT to the "
                 "Reading-B re-open question and to nothing else; surfaced and ROUTED, "
                 "not landed (frozen §5.5 item 2)")
        else:
            d = ("the matched-side reading is BOUND-ROBUST for this arm and the #782 "
                 "§7.1 'matched-side is KUBC-conditional' caveat is discharged FOR THIS "
                 "ARM; surfaced and ROUTED, not landed (frozen §5.5 item 3)")
        disp.append({"config": r["config"], "mode": r["mode"],
                     "class_vs_T1_PRIMARY": c1,
                     "class_vs_T1_CONSERVATIVE": r["classes"]["T1_rZ_0.50_CONSERVATIVE"],
                     "class_vs_T1_PRIMARY_void_scope_per_mode":
                         r["classes_void_scope_per_mode"]["T1_rZ_0.50_PRIMARY"],
                     "class_vs_T1_PRIMARY_no_void_overlay":
                         r["classes_no_void_overlay"]["T1_rZ_0.50_PRIMARY"],
                     "pre_registered_disposition": d})
    classes_seen = sorted({r["classes"][k] for r in reads for k in r["classes"]})
    classes_seen_no_void = sorted({v for r in reads
                                   for v in r["classes_no_void_overlay"].values()})
    straddle_any = any(v == "STRADDLES" for r in reads
                       for v in r["classes_no_void_overlay"].values())
    return {
        "HEADLINE_frozen_5p4": {
            "bulk_only_cold_phi_sf": head("bulk_only_cold_phi_sf"),
            "grown_frozen_tangent": head("grown_frozen_tangent"),
            "scope_tag": ("SCOPE: this bench brackets K_eff ONLY. Every r_Z interval it "
                          "reports is a K-BRACKET AROUND AN ASSUMED rho_eff/rho_0 == 1 — "
                          "the rho half is ASSUMED, not measured, not bracketed. This "
                          "lane does NOT resolve walk-1's rho half; that is OWED-2, a "
                          "separate lane, and OWED-1 does not dispose of it."),
        },
        "T4_lift_bands_per_boundary_condition": grown_lift,
        "per_configuration_dispositions": disp,
        "outcome_classes_returned_on_the_PHYSICAL_set": classes_seen,
        "outcome_classes_returned_with_VOID_overlay_removed": classes_seen_no_void,
        "G1_void_scoping": {
            "void_configs_STRICT": g1["void_configs_STRICT"],
            "void_config_modes": g1["void_config_modes"],
            "adjudication_routed": (
                "frozen G1 says 'the bench is VOID for that configuration'. Under the "
                "STRICT reading a shear-mode ratio inversion voids that configuration's "
                "hydrostatic read too; under the per-(configuration,mode) reading it does "
                "not. The STRICT reading is carried as the headline because it voids MORE "
                "(it cannot be a rescue); BOTH are shipped. Grant / the auditor lane own "
                "the scoping call — this lane surfaces and routes."),
        },
        "any_bracket_straddles_a_threshold": bool(straddle_any),
        "anti_seduction_fence": (
            "a wide bracket is a statement about the INSTRUMENT, not about the medium: "
            "bracket width is NOT converted into physical significance in either "
            "direction, and the uncaged gap g_0 is reported alongside every width so the "
            "reader can see how much of it is finite-size boundary layer (frozen §5.6)"),
    }


# ═════════════════════════════════════════════════════════════════════════════
# MAIN — the frozen §3 configuration set, run end to end and shipped to JSON
# ═════════════════════════════════════════════════════════════════════════════
def run_all():
    t_start = time.time()
    out = {"provenance": {
        "lane": "OWED-1 — the SUBC/KUBC bracket: bound K_eff on BOTH sides, not one",
        "prereg": "research/2026-07-28_subc-kubc-bracket_prereg-FROZEN.md",
        "grant_ruling": "yes, as above, so below, we should assume we have both "
                        "boundaries right? [sic, 2026-07-28]",
        "class": "lattice-derived static homogenization under TWO boundary conditions; "
                 "CONSISTENCY-class (is an already-banked lattice number boundary-"
                 "condition-robust?), NOT emergence; alpha-CLEAN; mints no clm-/def-; "
                 "engine src/ave BYTE-UNTOUCHED (imports read-only).",
        "MODULUS_IDENTITY": MODULUS_IDENTITY,
        "SCOPE_FENCE": ("SCOPE: this bench brackets K_eff ONLY. Every r_Z interval it "
                        "reports is a K-BRACKET AROUND AN ASSUMED rho_eff/rho_0 == 1 — "
                        "the rho half is ASSUMED, not measured, not bracketed. This lane "
                        "does NOT resolve walk-1's rho half; that is OWED-2 "
                        "(research/2026-07-22_vessel-state-rve_result.md sec 9), a "
                        "separate lane, and OWED-1 does not dispose of it."),
        "RHO_STAR_reused": float(RHO_STAR), "K_S_reused": float(K_S),
        "S_RAIL_deep": S_RAIL_DEEP, "sigma_probe": SIGMA_PROBE, "eps_probe_KUBC": EPS,
        "subc_tol": SUBC_TOL, "subc_cap": SUBC_MAX, "bw_shared_skin": BW,
    }}

    # ── §4B SELFTEST-PARTITION (Layer-1 reachability discharge, before any bracket) ──
    out["selftest_partition"] = selftest_partition()

    # ── setup + uncaged references at every frozen box size ──────────────────
    print("[setup] building srs-z3 boxes L =", L_SIZES)
    SS, unc_meta, unc = {}, {}, {}
    for L in L_SIZES:
        SS[L] = setup(L)
        SS[L]["components"] = component_count(SS[L]["geom"][1], SS[L]["geom"][2],
                                              SS[L]["act"])
        print(f"[uncaged] L={L} N={SS[L]['N']} active={SS[L]['n_active']} "
              f"components={SS[L]['components']}")
        unc_meta[L], unc[L] = uncaged_and_g0(SS[L], ("hydro", "shear"))
    S = SS[L_BASE]
    out["lattice"] = {L: {"N": SS[L]["N"], "M": SS[L]["M"],
                          "n_active": SS[L]["n_active"],
                          "n_degree_zero": SS[L]["N"] - SS[L]["n_active"],
                          "connected_components_of_active_graph": SS[L]["components"],
                          "V_box": SS[L]["V"]} for L in L_SIZES}
    out["born_rotation_instrument_fact"] = born_rotation_check(
        S["geom"], cold_operator(S["geom"])[0], S["xc"])
    out["uncaged_reference_by_L"] = unc_meta

    g0_by_L = {L: unc_meta[L]["by_mode"]["hydro"] for L in L_SIZES}
    out["selftest_G2b"] = selftest_G2b(g0_by_L)

    # ── §3 A — the #782 isotropic arms ───────────────────────────────────────
    configs = []
    print("[A] route-A phi scan, bulk_only_cold ...")
    for rc in ROUTE_A["r_cage"]:
        lab = ("bulk_only_cold_phi_sf" if rc == ROUTE_A["r_cage"][-1]
               else f"bulk_only_cold_rc{rc}")
        configs.append(run_cage_config(S, unc[L_BASE], lab, "bulk_only", rc,
                                       ROUTE_A["s"], BOTH_MODES))
    print("[A] route-A phi scan, symmetric_cold (wall-class control) ...")
    for rc in ROUTE_A["r_cage"]:
        lab = ("symmetric_cold_phi_sf" if rc == ROUTE_A["r_cage"][-1]
               else f"symmetric_cold_rc{rc}")
        configs.append(run_cage_config(S, unc[L_BASE], lab, "symmetric", rc,
                                       ROUTE_A["s"], BOTH_MODES))
    print("[A] pre-stress arms + rigid STOP-gate mirror ...")
    configs.append(run_cage_config(S, unc[L_BASE], "bulk_only_compressed_phi_sf",
                                   "bulk_only", PHI_SF_RCAGE, PHI_SF_S, BOTH_MODES,
                                   eps_pre=-0.08))
    configs.append(run_cage_config(S, unc[L_BASE], "bulk_only_expanded_phi_sf",
                                   "bulk_only", PHI_SF_RCAGE, PHI_SF_S, BOTH_MODES,
                                   eps_pre=+0.08))
    configs.append(run_cage_config(S, unc[L_BASE], "rigid_phi_sf", "rigid",
                                   PHI_SF_RCAGE, PHI_SF_S, BOTH_MODES))
    print("[A] route-B (the second collapse route) ...")
    for s_b in ROUTE_B["s"]:
        configs.append(run_cage_config(S, unc[L_BASE], f"routeB_bulk_only_cold_s{s_b}",
                                       "bulk_only", ROUTE_B["r_cage"], s_b, BOTH_MODES))

    # ── §3 B — the #796 grown arm on its FROZEN TANGENT OPERATOR ─────────────
    print("[B] growing the #796 fixed_budget verdict arm ...")
    arm, ka_grown, kse_grown = grown_frozen_tangent_operator(S)
    out["grown_operating_point_796"] = {
        "seed_class": arm["seed_class"], "p_ref": arm["p0"],
        "src_sigma": VERDICT_SRC_SIGMA, "wall_class": arm["wall_class"],
        "grown_equilibrium_exists": arm["grown_equilibrium_exists"],
        "grown_CG_converged": arm["grown_CG_converged"],
        "grown_tension_nonzero": arm["grown_tension_nonzero"],
        "grown_bonds_positive": arm["grown_bonds_positive"],
        "max_abs_T": arm["max_abs_T"], "min_kse": arm["min_kse"],
        "peak_A": arm["peak_A"], "eps_min": arm["eps_min"], "eps_max": arm["eps_max"],
        "outer_it": arm["outer_it"], "nlres": arm["nlres"],
        "carve": ("bracketed on the FROZEN tangent operator Phi_eff(u_0), held "
                  "byte-identical between the SUBC and KUBC solves (prereg sec 1.4)"),
    }
    centers_sf = cubic_cage_centers(S["L"], PHI_SF_S, S["xc"])
    configs.append(run_operator_config(
        S, unc[L_BASE], "grown_frozen_tangent", ka_grown, kse_grown, ("hydro", "shear"),
        extra={"fractions": realized_fractions(S, centers_sf, PHI_SF_RCAGE, PHI_SF_S),
               "operator_provenance": "Phi_eff(u_0) at the #796 fixed_budget p_ref "
                                      "operating point (FROZEN, u-independent)"}))
    configs.append(run_operator_config(
        S, unc[L_BASE], "painted_anisotropic", ka_grown, kse_grown, BOTH_MODES,
        extra={"same_operator_as": "grown_frozen_tangent",
               "note": "on the #796 carve this is the SAME operator as configuration 7; "
                       "running both is the G6 cross-check that our reconstruction of the "
                       "#796 operating point is faithful, NOT two physics arms"}))
    ka_iso, ks_iso = cage_bond_stiffness(S["geom"][3], S["geom"][4], centers_sf,
                                         PHI_SF_RCAGE, CAGE_W, VERDICT_WALL,
                                         VERDICT_S_RAIL, 0.0)
    configs.append(run_operator_config(
        S, unc[L_BASE], "isotropic_control", np.asarray(ka_iso, float),
        np.asarray(ks_iso, float), BOTH_MODES,
        extra={"fractions": realized_fractions(S, centers_sf, PHI_SF_RCAGE, PHI_SF_S),
               "note": "the #782 bulk_only_cold cage at phi_sf with k_s = KS0 — the "
                       "crash BASELINE K_ratio_lift normalizes against"}))

    # ── §3 C — the uniform-medium null + the size scan ───────────────────────
    print("[C] uniform-medium null + size scan ...")
    M0 = S["geom"][1].shape[0]
    null_row = run_operator_config(S, unc[L_BASE], "uniform_medium_null",
                                   np.full(M0, float(RHO_STAR)),
                                   np.full(M0, float(K_S)), ("hydro", "shear"),
                                   extra={"n_cages": 0})
    configs.append(null_row)
    size_rows = []
    for L in L_SIZES:
        if L == L_BASE:
            row = [c for c in configs if c["config"] == "bulk_only_cold_phi_sf"][0]
        else:
            row = run_cage_config(SS[L], unc[L], f"bulk_only_cold_phi_sf_L{L}",
                                  "bulk_only", PHI_SF_RCAGE, PHI_SF_S, BOTH_MODES)
            configs.append(row)
        h = row["by_mode"]["hydro"]
        size_rows.append({"L": L, "n_cages": row["fractions"]["n_cages"],
                          "phi_intensive": row["fractions"]["phi_intensive"],
                          "phi_realized_box": row["fractions"]["phi_realized_box"],
                          "phi_realized_bond": row["fractions"]["phi_realized_bond"],
                          "R_SUBC": h["R_SUBC"], "R_KUBC": h["R_KUBC"],
                          "width": h["width"], "g0": h["g0_uncaged_gap"]})

    # ── §4 G8 — load-amplitude invariance (IDENTITY, labelled) ───────────────
    print("[G8] load-amplitude invariance ...")
    ka_sf, ks_sf = cage_bond_stiffness(S["geom"][3], S["geom"][4], centers_sf,
                                       PHI_SF_RCAGE, CAGE_W, "bulk_only",
                                       S_RAIL_DEEP, 0.0)
    Phi_sf, dg_sf = operator(S["geom"], ka_sf, ks_sf)
    Phi0, dg0 = cold_operator(S["geom"])
    a1 = subc_solve(S["geom"], S["act"], Phi_sf, dg_sf, "hydro", S["xc"], S["V"],
                    S["half"], sigma=SIGMA_PROBE)
    a10 = subc_solve(S["geom"], S["act"], Phi_sf, dg_sf, "hydro", S["xc"], S["V"],
                     S["half"], sigma=10.0 * SIGMA_PROBE)
    u1 = unc[L_BASE]["hydro"]["subc"]
    u10 = subc_solve(S["geom"], S["act"], Phi0, dg0, "hydro", S["xc"], S["V"],
                     S["half"], sigma=10.0 * SIGMA_PROBE)
    r1 = u1["U_total"] / a1["U_total"]
    r10 = u10["U_total"] / a10["U_total"]
    out["G8_load_amplitude_invariance"] = {
        "R_SUBC_at_sigma": float(r1), "R_SUBC_at_10sigma": float(r10),
        "rel_change": float(abs(r10 - r1) / (abs(r1) + 1e-300)), "tol": G8_TOL,
        "G8_PASS": bool(abs(r10 - r1) / (abs(r1) + 1e-300) <= G8_TOL),
        "label": "IDENTITY on a u-independent (linear) operator — exact by algebra; "
                 "exists to catch a coding error in the load-set scaling, nothing more",
    }

    # ── §4B SELFTEST-G1 (the VOID ordering gate must fire on an inverted extraction) ──
    sf = [c for c in configs if c["config"] == "bulk_only_cold_phi_sf"][0]
    out["selftest_G1"] = selftest_G1(u1, {"subc": a1, "R_KUBC": sf["by_mode"]["hydro"]["R_KUBC"]})

    # ── §4 G6 — reproduction cross-check against the merged corpus ───────────
    print("[G6] reproduction cross-check vs merged #782 / #796 ...")
    painted796 = painted_anisotropic_arm(S["geom"], S["free"], arm, S["xc"], S["half"])
    iso796 = isotropic_control_K(S["geom"], S["xc"])
    out["gate_G6"] = gate_G6({
        "#782 bulk_only_cold core-energy ratio at phi_sf":
            (sf["by_mode"]["hydro"]["R_KUBC_core"], 0.296,
             "research/2026-07-21_rve-aggregation-bench_result.md sec 5"),
        "#796 isotropic control":
            (iso796, 0.29636822324939766, "research/drivers/vessel_state_rve_results.json"),
        "#796 painted-anisotropic":
            (painted796["K_tan_over_K0_painted"], 0.2982369862639104,
             "research/drivers/vessel_state_rve_results.json"),
    })

    # ── the frozen gates ─────────────────────────────────────────────────────
    out["gate_G1_VOID_ordering"] = gate_G1(configs, unc_meta)
    out["gate_G2"] = gate_G2(null_row, g0_by_L, out["selftest_G2b"])
    g45 = gate_G4_G5(configs, unc_meta)
    out["gate_G4_solver"] = g45["G4"]
    out["gate_G5_work_identity"] = g45["G5"]
    out["solver_per_solve"] = g45["per_solve"]
    mirror = []
    for lab, wc in (("bulk_only_cold_phi_sf", "bulk_only"), ("rigid_phi_sf", "rigid")):
        h = [c for c in configs if c["config"] == lab][0]["by_mode"]["hydro"]
        mirror.append({"config": lab, "wall_class": wc, "R_SUBC": h["R_SUBC"],
                       "R_KUBC": h["R_KUBC"]})
    out["gate_G7"] = gate_G7(mirror, size_rows)

    # ── §3 D — the fully-SUBC-grown companion (NOT a bracket) ────────────────
    print("[D] fully-SUBC-grown companion (budgeted; NOT a bracket) ...")
    out["companion_fully_SUBC_grown"] = subc_grown_companion(S, unc[L_BASE])

    # ── §5 the frozen read ───────────────────────────────────────────────────
    # ── SUPPLEMENTARY (additive, NOT frozen): the P-wave / VRH modulus M = K + 4G/3 ──
    unc_m = {}
    for L in L_SIZES:
        bm = unc_meta[L]["by_mode"]
        unc_m[L] = {"subc": bm["hydro"]["K_SUBC_abs"] + 4.0 * bm["shear"]["K_SUBC_abs"] / 3.0,
                    "kubc": bm["hydro"]["K_KUBC_abs"] + 4.0 * bm["shear"]["K_KUBC_abs"] / 3.0}
    for c in configs:
        if "hydro" in c["by_mode"] and "shear" in c["by_mode"]:
            c["SUPPLEMENTARY_M_axis_NOT_FROZEN"] = m_axis(
                c["by_mode"]["hydro"], c["by_mode"]["shear"], unc_m[c["L"]])
    out["supplementary_M_axis_note"] = (
        "ADDITIVE, NOT the frozen deliverable. The frozen bracket is on the BULK modulus "
        "K (prereg sec 1.2). A normal-incidence impedance Z = rho*c_P carries the P-WAVE "
        "modulus M = K + 4G/3, and sqrt(rho*K) is the right impedance only for a G = 0 "
        "medium — which this composite is not (G_eff/G_0 ~ 0.67). Both axes are shipped; "
        "WHICH modulus the corpus discriminator r_Z should ride is a DEFINITION question "
        "ROUTED to Grant and NOT settled by this lane. No frozen criterion is amended.")

    out["configurations"] = configs
    g1 = out["gate_G1_VOID_ordering"]
    vstrict = set(g1["void_configs_STRICT"])
    vmode = set(g1["void_config_modes"])
    reads = [read_config(cfg, L, mode, res, cfg in vstrict,
                         f"{cfg}::{mode}" in vmode)
             for cfg, L, mode, res in _iter_measurements(configs)]
    out["reads"] = reads
    gh = [c for c in configs if c["config"] == "grown_frozen_tangent"][0]["by_mode"]["hydro"]
    ic = [c for c in configs if c["config"] == "isotropic_control"][0]["by_mode"]["hydro"]
    lift_s = gh["R_SUBC"] / (ic["R_SUBC"] + 1e-300)
    lift_k = gh["R_KUBC"] / (ic["R_KUBC"] + 1e-300)
    out["verdict"] = verdict(reads, {
        "lift_under_SUBC": float(lift_s), "lift_under_KUBC": float(lift_k),
        "bands_T4": {"L1": "< 1.2", "L2": "1.2 - 1.5", "L3": ">= 1.5"},
        "band_under_SUBC": ("L1" if lift_s < T4_LIFT[0]
                            else ("L2" if lift_s < T4_LIFT[1] else "L3")),
        "band_under_KUBC": ("L1" if lift_k < T4_LIFT[0]
                            else ("L2" if lift_k < T4_LIFT[1] else "L3")),
        "band_flips_across_boundary_condition": bool(
            ("L1" if lift_s < T4_LIFT[0] else ("L2" if lift_s < T4_LIFT[1] else "L3"))
            != ("L1" if lift_k < T4_LIFT[0] else ("L2" if lift_k < T4_LIFT[1] else "L3"))),
        "note": "T4 is applied PER-BOUNDARY-CONDITION to the grown-vs-isotropic-control "
                "pair (frozen sec 5.2). A ratio of two ratios is NOT bound-ordered, so "
                "this pair is NOT a bracket and is not read as one.",
    }, out["gate_G1_VOID_ordering"])

    # ── the frozen §4B self-test gate ────────────────────────────────────────
    out["gate_fireability_selftest"] = {
        "selftest_G1_fires": out["selftest_G1"]["selftest_G1_fires"],
        "selftest_G2b_fires": out["selftest_G2b"]["selftest_G2b_fires"],
        "selftest_partition_pass": out["selftest_partition"]["selftest_partition_pass"],
        "gate_fireability_selftest_pass": bool(
            out["selftest_G1"]["selftest_G1_fires"]
            and out["selftest_G2b"]["selftest_G2b_fires"]
            and out["selftest_partition"]["selftest_partition_pass"]),
        "frozen_consequence": ("If ANY fails to force its target, the correctness gates "
                               "are a checklist not gates => the bench is VOID before any "
                               "bracket is read; route to Grant. (frozen sec 4B)"),
    }
    out["_runtime_sec"] = float(time.time() - t_start)
    return out


def determinism_digest(out):
    """Frozen §4 G3: a SHA-256 over the results with timing stripped, so two independent
    full runs in separate processes writing separate paths can be compared."""
    d = json.loads(json.dumps(out))
    d.pop("_runtime_sec", None)
    d.pop("determinism_digest", None)
    comp = d.get("companion_fully_SUBC_grown")
    if isinstance(comp, dict):
        comp.pop("wall_clock_s", None)
    return hashlib.sha256(json.dumps(d, sort_keys=True).encode()).hexdigest()


# ═════════════════════════════════════════════════════════════════════════════
# White figure (ave.viz.style; Okabe-Ito; honest axes/units; legend outside; no title)
# ═════════════════════════════════════════════════════════════════════════════
def make_figure(out, path_png):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from ave.viz import style
    style.apply()
    C = style.COLORS

    cfgs = {c["config"]: c for c in out["configurations"]}
    routeA = [f"bulk_only_cold_rc{rc}" for rc in ROUTE_A["r_cage"][:-1]]
    routeA.append("bulk_only_cold_phi_sf")
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(12.4, 4.8), layout="constrained")
    fig.get_layout_engine().set(w_pad=0.10, h_pad=0.06, wspace=0.10)

    # ── (L) the K bracket across the route-A crash band, on the geometry-correct axis
    xs, lo, hi, core = [], [], [], []
    for lab in routeA:
        c = cfgs[lab]
        h = c["by_mode"]["hydro"]
        xs.append(c["fractions"]["f_incl_intensive"])
        lo.append(h["R_SUBC"])
        hi.append(h["R_KUBC"])
        core.append(h["R_KUBC_core"])
    axL.fill_between(xs, lo, hi, color=C["ave"], alpha=0.22,
                     label="PRIMARY bracket [SUBC, KUBC]")
    axL.plot(xs, hi, "o-", color=C["ave"], ms=5, label="KUBC upper bound (whole cell)")
    axL.plot(xs, lo, "s-", color=C["data"], ms=5, label="SUBC lower bound (whole cell)")
    axL.plot(xs, core, "^--", color=C["accent"], ms=5,
             label="#782/#796 banked CORE estimator (no bound status)")
    axL.set_xlabel("coated-inclusion fraction  f_incl  [intensive]  (dimensionless)")
    axL.set_ylabel("K_eff / K\u2080   (BULK modulus K)")
    axL.legend(loc="upper left", bbox_to_anchor=(0.0, -0.20), fontsize=6.8, frameon=False)

    # ── (R) the r_Z brackets of the headline arms against the frozen corpus thresholds
    heads = [("bulk_only_cold_phi_sf", "#782 bulk-only cold  φ_sf"),
             ("symmetric_cold_phi_sf", "#782 symmetric wall  φ_sf"),
             ("bulk_only_compressed_phi_sf", "#782 compressed  φ_sf"),
             ("grown_frozen_tangent", "#796 grown frozen tangent"),
             ("isotropic_control", "#796 isotropic control")]
    for i, (lab, pretty) in enumerate(heads):
        h = cfgs[lab]["by_mode"]["hydro"]
        p = h["r_Z_bracket_rho_ASSUMED_1"]
        q = h["r_Z_bracket_conservative_rho_ASSUMED_1"]
        axR.plot([q[0], q[1]], [i + 0.16] * 2, "-", color=C["muted"], lw=2.6,
                 label="CONSERVATIVE (theorem-grade)" if i == 0 else None)
        axR.plot([p[0], p[1]], [i - 0.16] * 2, "-", color=C["ave"], lw=4.0,
                 label="PRIMARY (same-instrument)" if i == 0 else None)
        axR.plot([np.sqrt(max(h["R_KUBC_core"], 0.0))], [i - 0.16], "^",
                 color=C["accent"], ms=6,
                 label="banked CORE-convention point" if i == 0 else None)
    for thr, ls in ((0.5, ":"), (0.45, "--"), (0.55, "--")):
        axR.axvline(thr, color=C["comparison"], ls=ls, lw=1.0)
    for thr, nm in ((0.45, "T2 lo"), (0.5, "T1"), (0.55, "T2 hi")):
        axR.annotate(f"{nm} = {thr:.2f}", xy=(thr, len(heads) - 0.62), fontsize=6.4,
                     color=C["comparison"], rotation=90, va="top", ha="right")
    axR.set_yticks(range(len(heads)))
    axR.set_yticklabels([p for _, p in heads], fontsize=7)
    axR.set_xlabel("r_Z = \u221a(K_eff/K\u2080)  at  \u03c1_eff/\u03c1\u2080 \u2261 1 ASSUMED\n"
                   "(K-bracket only; \u03c1 not measured)")
    axR.legend(loc="upper left", bbox_to_anchor=(0.0, -0.20), fontsize=6.8, frameon=False)

    fig.savefig(path_png, dpi=160, bbox_inches="tight")
    fig.savefig(str(Path(path_png).with_suffix(".pdf")), bbox_inches="tight")
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(Path(__file__).with_name(
        "subc_kubc_bracket_results.json")))
    ap.add_argument("--no-figure", action="store_true")
    args = ap.parse_args()

    out = run_all()
    out["determinism_digest"] = determinism_digest(out)
    Path(args.out).write_text(json.dumps(out, indent=2))
    if not args.no_figure:
        make_figure(out, str(Path(args.out).with_name("subc_kubc_bracket.png")))

    print("\n=== SUBC/KUBC BRACKET — summary (OWED-1) ===")
    print("SCOPE: K ONLY. Every r_Z interval is a K-bracket around an ASSUMED rho == 1.")
    print("MODULUS: %s" % MODULUS_IDENTITY["hydro"])
    sfg = out["gate_fireability_selftest"]
    print("\n[sec 4B self-tests] G1_fires=%s  G2b_fires=%s  partition=%s  =>  "
          "gate_fireability_selftest_pass=%s" % (
              sfg["selftest_G1_fires"], sfg["selftest_G2b_fires"],
              sfg["selftest_partition_pass"], sfg["gate_fireability_selftest_pass"]))
    g2 = out["selftest_G2b"]
    print("   g0(Hill)    =", ["%.5f" % x for x in g2["g0_hill_normalized"]])
    print("   g0(nominal) =", ["%.5f" % x for x in g2["g0_NOMINAL_sigma_MIS_normalized"]],
          " 1/sbar^2 =", ["%.5f" % x for x in g2["inverse_sigma_bar_squared"]])
    print("\n[gates] G1=%s G2a=%s G2b=%s G4=%s G5=%s G6=%s G7a=%s G7b=%s G8=%s" % (
        out["gate_G1_VOID_ordering"]["G1_PASS"],
        out["gate_G2"]["G2a_IDENTITY_not_a_fireable_gate"]["holds"],
        out["gate_G2"]["G2b_FIREABLE"]["G2b_PASS"],
        out["gate_G4_solver"]["G4_PASS"], out["gate_G5_work_identity"]["G5_PASS"],
        out["gate_G6"]["G6_PASS"], out["gate_G7"]["G7a_mirror"]["G7a_PASS"],
        out["gate_G7"]["G7b_size_trend"]["G7b_PASS"],
        out["G8_load_amplitude_invariance"]["G8_PASS"]))
    for r in out["gate_G6"]["rows"]:
        print("   G6 %-52s got %.10f vs %.10f  rel=%.2e %s" % (
            r["quantity"], r["recomputed"], r["merged_target"], r["rel"],
            "OK" if r["ok"] else "FAIL"))
    g1 = out["gate_G1_VOID_ordering"]
    print("\n[G1] violations=%d of %d | absolute theorem-grade ordering holds "
          "everywhere=%s | RATIO-ONLY violations=%d" % (
              len(g1["violations"]), g1["n_checked"],
              g1["absolute_theorem_grade_ordering_holds_everywhere"],
              len(g1["violations_that_are_RATIO_ONLY_with_absolute_ordering_intact"])))
    print("     VOID configs (STRICT scope) :", g1["void_configs_STRICT"])
    print("     VOID (config, mode) scope   :", g1["void_config_modes"])
    print("\n[brackets] config (mode)                "
          "[  SUBC  ,  KUBC  ]  width   g0     core     T1-PRIM/T1-CONS (no-VOID overlay)")
    for r in out["reads"]:
        nv = r["classes_no_void_overlay"]
        print("  %-36s [%7.5f, %7.5f] %7.4f %6.4f %7.5f  %-13s / %-13s %s" % (
            r["config"] + " (" + r["mode"] + ")", r["primary_bracket"][0],
            r["primary_bracket"][1], r["width"], r["g0_uncaged_gap"], r["R_KUBC_core"],
            nv["T1_rZ_0.50_PRIMARY"], nv["T1_rZ_0.50_CONSERVATIVE"],
            "  <-- VOID(strict)" if r["VOID_strict_per_configuration"] else ""))
    hl = out["verdict"]["HEADLINE_frozen_5p4"]
    for key in ("bulk_only_cold_phi_sf", "grown_frozen_tangent"):
        h = hl[key]
        if h is None:
            continue
        nv = h["classes_no_void_overlay"]
        print("\n* HEADLINE %s  [%s]" % (key, h["modulus_identity"].split("(")[0].strip()))
        print("    r_Z PRIMARY      [%.5f, %.5f]  vs T1=0.50 -> %s   (VOID-strict=%s)" % (
            h["primary_r_Z_bracket_rho_ASSUMED_1"][0],
            h["primary_r_Z_bracket_rho_ASSUMED_1"][1], nv["T1_rZ_0.50_PRIMARY"],
            h["VOID_strict_per_configuration"]))
        print("    r_Z CONSERVATIVE [%.5f, %.5f]  vs T1=0.50 -> %s" % (
            h["conservative_r_Z_bracket_rho_ASSUMED_1"][0],
            h["conservative_r_Z_bracket_rho_ASSUMED_1"][1],
            nv["T1_rZ_0.50_CONSERVATIVE"]))
        print("    banked CORE-convention point %.5f inside PRIMARY bracket = %s" % (
            h["banked_core_convention_number"],
            h["core_estimator_inside_primary_bracket"]))
        mc = [c for c in out["configurations"] if c["config"] == key]
        if mc and "SUPPLEMENTARY_M_axis_NOT_FROZEN" in mc[0]:
            ma = mc[0]["SUPPLEMENTARY_M_axis_NOT_FROZEN"]
            print("    [SUPPLEMENTARY, not frozen] P-wave M = K+4G/3: R_M bracket "
                  "[%.5f, %.5f] -> r_Z_M [%.5f, %.5f]" % (
                      ma["primary_bracket_M"][0], ma["primary_bracket_M"][1],
                      ma["r_Z_M_bracket_rho_ASSUMED_1"][0],
                      ma["r_Z_M_bracket_rho_ASSUMED_1"][1]))
    print("\n[pinned-shell confound, KUBC side only]")
    for c in out["configurations"]:
        f = c.get("fractions")
        if f:
            print("  %-34s pinned shell nodes = %5.1f %%  (SUBC: 0.0 %% by construction)"
                  % (c["config"], 100.0 * f["pinned_shell_node_fraction_KUBC"]
                     ["pinned_fraction"]))
    comp = out["companion_fully_SUBC_grown"]
    print("\n[companion, NOT a bracket] %s" % comp["status"])
    print("[determinism] digest=%s  runtime=%.1f s" % (
        out["determinism_digest"][:16] + "...", out["_runtime_sec"]))
    return out


if __name__ == "__main__":
    main()
