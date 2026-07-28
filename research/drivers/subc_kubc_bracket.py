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
# ★TETRAGONAL mode — SUPPLEMENTARY, added by the PR #802 review repair (finding F2).
#  E = ε·diag(1,−1,0) / Σ = σ·diag(1,−1,0) measures the CUBIC tetragonal shear constant
#  C′ = (C11 − C12)/2, which is the constant the [100] longitudinal modulus needs. It is
#  NOT in `BOTH_MODES` and NOT in any `by_mode` block, so it enters NO frozen gate, NO
#  frozen read and NO frozen count — it is carried in a separate, clearly-labelled
#  SUPPLEMENTARY_anisotropy block (additive, never substitutive).
SIG_TETRA = np.diag([1.0, -1.0, 0.0])
# ★UNIAXIAL mode — SUPPLEMENTARY, added by the PR #802 RE-VERIFY repair (finding F1).
#  KUBC only: E = eps*diag(1,0,0) => U/V = 1/2*C11*eps^2, so C11 = 2U/(V eps^2) DIRECTLY,
#  without assembling it from K and C'. Its agreement with K + 4C'/3 is a CUBIC IDENTITY
#  that holds only when [100] is an elastic axis of the medium — which is the axis-
#  alignment evidence the first repair's SUBC-Sigma_bar sentence did NOT supply (that
#  Sigma_bar is a property of the LOAD SET; it never sees Phi). Like `tetra`, it is NOT in
#  BOTH_MODES and NOT in any by_mode block: NO frozen gate, read or count sees it.
SIG_UNIAX = np.diag([1.0, 0.0, 0.0])


def sigma_matrix(mode):
    """The macroscopic STRESS direction of each probe mode (SUBC side)."""
    return {"hydro": SIG_HYDRO, "shear": SIG_SHEAR, "tetra": SIG_TETRA}[mode]


def strain_matrix(mode, eps):
    """The macroscopic STRAIN of each probe mode (KUBC side). `hydro`/`shear` are the
    Rule-14 shipped `rve_aggregation_bench.strain_mode` forms, byte-unchanged; `tetra` is
    the SUPPLEMENTARY cubic C′ mode added by the F2 repair and defined here so the merged
    #782 driver stays untouched."""
    if mode == "tetra":
        return eps * SIG_TETRA
    if mode == "uniax":
        return eps * SIG_UNIAX
    return strain_mode(mode, eps)


def sigma_bar_scalar(Sb, mode):
    """The scalar amplitude of the REALIZED macroscopic stress `Σ̄` in each mode, i.e. the
    coefficient of that mode's unit tensor:
      hydro  σ̄ = tr(Σ̄)/3          ⇒ U/V = ½σ̄²/K
      shear  σ̄ = Σ̄_xy             ⇒ U/V = ½σ̄²/C44
      tetra  σ̄ = (Σ̄_xx − Σ̄_yy)/2  ⇒ U/V = ½σ̄²/C′   (complementary energy of a cubic
             medium under Σ = σ·diag(1,−1,0) is (S11 − S12)σ² = σ²/(2C′))
    """
    if mode == "hydro":
        return float(np.trace(Sb) / 3.0)
    if mode == "shear":
        return float(Sb[0, 1])
    return 0.5 * float(Sb[0, 0] - Sb[1, 1])


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
    Sig = sigma * sigma_matrix(mode)
    f = traction_load(pos, act, Sig)
    Sb = hill_stress(f, pos, xc, V)
    sbar = sigma_bar_scalar(Sb, mode)
    u, res, it = cg_neumann(Phi, bi, bj, N, act, f, diag)
    U = elastic_energy(u, Phi, bi, bj)
    work = 0.5 * float(np.sum(f * u))
    M_abs = sbar ** 2 * V / (2.0 * U) if U > 0 else float("nan")
    return {
        "U_total": float(U), "U_core": float(core_energy(u, Phi, bi, bj, mid, xc, half)),
        "work_half_f_dot_u": work,
        "work_identity_rel": float(abs(U - work) / (abs(U) + 1e-300)),
        "sigma_bar": sbar, "M_abs": float(M_abs),
        "Sigma_bar_tensor": [[float(x) for x in row] for row in Sb],
        "cg_residual": res, "cg_iters": it,
        "net_force_norm": float(np.linalg.norm(f.sum(axis=0))),
        "net_torque_norm": float(np.linalg.norm(np.cross(pos - xc, f).sum(axis=0))),
    }


def kubc_solve(geom, free, Phi, diag, mode, xc, V, half, eps=EPS, want_reaction=False):
    """The KUBC counterpart, Rule-14 on the #782 primitive (`cg_solve_interior`): impose
    the affine macroscopic strain on the boundary shell, relax the interior, return BOTH
    the whole-cell energy (the bound-carrying measure) and the central-L/2-cube core
    energy (the SHIPPED #782/#796 estimator, which carries NO bound status, prereg §2.3).

    `want_reaction` (SUPPLEMENTARY, F1 repair; OFF for every frozen call so no frozen
    record gains or loses a leaf) additionally reads the macroscopic REACTION stress by
    the same Hill lemma the SUBC side uses, from the reaction force field `r = K u`
    (which is nonzero only on the prescribed shell once the interior has equilibrated).
    Unlike the SUBC load set, `r` is a functional of `Phi` — so its tensor STRUCTURE is a
    property of the MEDIUM and can test elastic-axis alignment.
    """
    pos, bi, bj, dhat, mid = geom
    N = pos.shape[0]
    E = strain_matrix(mode, eps)
    u_bc = np.zeros((N, 3))
    u_bc[~free] = affine_field(pos[~free], xc, E)
    u, res, it = cg_solve_interior(Phi, bi, bj, N, free, u_bc, diag)
    U = elastic_energy(u, Phi, bi, bj)
    pref = {"hydro": 4.5, "uniax": 0.5}.get(mode, 2.0)
    out = {
        "U_total": float(U), "U_core": float(core_energy(u, Phi, bi, bj, mid, xc, half)),
        "M_abs": float(U / (pref * eps ** 2 * V)),
        "cg_residual": float(res), "cg_iters": int(it),
    }
    if want_reaction:
        Sb = hill_stress(-forces(u, Phi, bi, bj, N), pos, xc, V)
        out["Sigma_bar_reaction"] = [[float(x) for x in row] for row in Sb]
    return out


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


def measure_cprime_abs(S, k_a, k_s):
    """★SUPPLEMENTARY (PR #802 review repair, finding F2) — the tetragonal cubic constant
    `C' = (C11 - C12)/2` under BOTH boundary conditions, for ONE operator.

    Runs through the SAME `subc_solve` / `kubc_solve` primitives the frozen modes use, on
    the SAME medium, with the SAME tolerances. It is deliberately NOT added to `by_mode`,
    so it enters NO frozen gate (G1/G4/G5), NO frozen read, and NO frozen count — additive,
    never substitutive."""
    Phi, diag = operator(S["geom"], k_a, k_s)
    a_s = subc_solve(S["geom"], S["act"], Phi, diag, "tetra", S["xc"], S["V"], S["half"])
    a_k = kubc_solve(S["geom"], S["free"], Phi, diag, "tetra", S["xc"], S["V"], S["half"])
    return {
        "Cprime_SUBC": a_s["M_abs"], "Cprime_KUBC": a_k["M_abs"],
        "subc_cg_residual": a_s["cg_residual"], "subc_cg_iters": a_s["cg_iters"],
        "subc_work_identity_rel": a_s["work_identity_rel"],
        "kubc_cg_residual": a_k["cg_residual"], "kubc_cg_iters": a_k["cg_iters"],
        "sigma_bar_SUBC": a_s["sigma_bar"],
        "Sigma_bar_tensor_SUBC": a_s["Sigma_bar_tensor"],
        "modulus_identity": MODULUS_IDENTITY["tetra"],
    }


def _tensor_diagnostics(Sb):
    """Structure diagnostics of a 3x3 macroscopic stress, all RELATIVE so the probe
    amplitude cancels."""
    A = np.asarray(Sb, dtype=float)
    od = max(abs(A[0, 1]), abs(A[0, 2]), abs(A[1, 2]))
    dg = max(abs(A[0, 0]), abs(A[1, 1]), abs(A[2, 2]))
    return {"max_abs_offdiag": float(od), "max_abs_diag": float(dg),
            "max_offdiag_over_max_diag": float(od / (dg + 1e-300))}


def isotropy_check(S, k_a, k_s, K_KUBC, C44_KUBC, Cp_KUBC, eps=EPS):
    """★THE AXIS-ALIGNMENT EVIDENCE — PR #802 RE-VERIFY repair, finding F1.

    ★WHAT THIS REPLACES, AND WHY. The first repair offered the realized SUBC macroscopic
    stress `Sigma_bar = diag(+0.9047.., -0.9047.., 0)` as evidence that "the cubic axes
    are the lattice axes". That is a NON SEQUITUR: `Sigma_bar = hill_stress(traction_load
    (...))` is built from the load set and the node positions and NEVER SEES `Phi`, so it
    is bit-identical for a rigid medium, for a caged medium and for no medium at all. A
    medium whose elastic axes were rotated 45 deg would return the same `Sigma_bar`. It is
    a property of the LOAD SET, not of the MEDIUM. The claim it was offered for is
    nonetheless TRUE; this function measures it properly, two ways:

      (a) DIRECT UNIAXIAL PROBE. KUBC with `E = eps*diag(1,0,0)` gives `C11 = 2U/(V eps^2)`
          with NO assembly step. For a cubic medium whose [100] IS an elastic axis this
          must equal the assembled `K + 4C'/3` built from the independent `hydro` and
          `tetra` modes. It is an IDENTITY only under axis alignment: for a crystal rotated
          by 45 deg about z the same two extractions read `(C11+C12+2C44)/2` and
          `K + 4C44/3` respectively, which differ from each other and from the true C11
          whenever the Zener anisotropy `A != 1`. Both rotated comparators are computed and
          shipped so the reader can see the size of the discrimination.

      (b) KUBC REACTION-STRESS STRUCTURE. The reaction field `r = K u` IS a functional of
          `Phi`. Under the tetragonal strain a medium with aligned axes returns a purely
          tetragonal stress (Sigma_33 = 0, off-diagonals = 0); under the uniaxial strain it
          returns `Sigma_22 = Sigma_33` exactly — the cubic `C12 = C13` signature. For a
          crystal rotated by a general angle `theta` about z the tetragonal probe returns a
          lab off-diagonal `Sigma_xy = eps*(C' - C44)*sin(4 theta)`, so the measured
          off-diagonal ratio BOUNDS `|sin 4 theta|` — quantified and shipped. That bound is
          blind at exactly `theta = 45 deg` (where sin(4 theta) = 0 too), which is precisely
          the branch (a) excludes. The two together are the evidence; neither alone is.

    ★HONEST SCOPE: KUBC side only. The SUBC side has no reaction field to read (no DOF is
    prescribed), and the SUBC apparent moduli are not needed for an axis-alignment
    statement, which is a property of the medium and not of the boundary condition.
    SUPPLEMENTARY throughout: no frozen gate, read or count sees any of it."""
    Phi, diag = operator(S["geom"], k_a, k_s)
    geom, free, xc, V, half = S["geom"], S["free"], S["xc"], S["V"], S["half"]
    a_u = kubc_solve(geom, free, Phi, diag, "uniax", xc, V, half, want_reaction=True)
    a_t = kubc_solve(geom, free, Phi, diag, "tetra", xc, V, half, want_reaction=True)
    C11_direct = float(a_u["M_abs"])
    C11_assembled = float(K_KUBC + 4.0 * Cp_KUBC / 3.0)
    Su = np.asarray(a_u["Sigma_bar_reaction"], dtype=float)
    St = np.asarray(a_t["Sigma_bar_reaction"], dtype=float)
    C11_react = float(Su[0, 0] / eps)
    C12_react, C13_react = float(Su[1, 1] / eps), float(Su[2, 2] / eps)
    # what the SAME two extractions would read if the cubic axes were rotated 45 deg
    # about z (standard cubic rotation: C11' = (C11+C12+2C44)/2; the `tetra` mode then
    # returns C44 in place of C', so the assembly becomes K + 4*C44/3)
    C12_from_modes = C11_assembled - 2.0 * Cp_KUBC
    C11_rot45_direct = 0.5 * (C11_assembled + C12_from_modes + 2.0 * C44_KUBC)
    C11_rot45_assembled = float(K_KUBC + 4.0 * C44_KUBC / 3.0)
    dt, du = _tensor_diagnostics(St), _tensor_diagnostics(Su)
    A_zener = C44_KUBC / (Cp_KUBC + 1e-300)
    sin4theta_bound = (dt["max_offdiag_over_max_diag"] * 2.0
                       / (abs(1.0 - A_zener) + 1e-300))
    return {
        "STATEMENT": ("the medium is CUBIC-ANISOTROPIC: Zener A = C44/C' != 1 under BOTH "
                      "boundary conditions. No isotropy check existed in the frozen "
                      "prereg, the driver or the first result doc."),
        "SUPERSEDES": (
            "the first repair's axis-alignment sentence cited the realized SUBC "
            "Sigma_bar. That is a NON SEQUITUR — hill_stress(traction_load(...)) never "
            "sees Phi and is bit-identical for a rigid medium, a caged medium and no "
            "medium at all, so it cannot distinguish an aligned medium from a rotated "
            "one. WITHDRAWN as evidence (the conclusion it was offered for stands, on "
            "the two independent measurements below)."),
        "direct_uniaxial_C11_KUBC": C11_direct,
        "assembled_K_plus_4Cprime_over_3_KUBC": C11_assembled,
        "rel_direct_minus_assembled": float(C11_direct / C11_assembled - 1.0),
        "C11_from_uniax_reaction_traction": C11_react,
        "rel_reaction_minus_energy_C11": float(C11_react / C11_direct - 1.0),
        "C12_from_uniax_reaction": C12_react,
        "C13_from_uniax_reaction": C13_react,
        "rel_C12_minus_C13": float(abs(C12_react - C13_react)
                                   / (abs(C12_react) + 1e-300)),
        "uniax_reaction_Sigma_bar": a_u["Sigma_bar_reaction"],
        "uniax_reaction_structure": du,
        "tetra_reaction_Sigma_bar": a_t["Sigma_bar_reaction"],
        "tetra_reaction_structure": dt,
        "tetra_reaction_Sigma33_over_Sigma11": float(abs(St[2, 2])
                                                     / (abs(St[0, 0]) + 1e-300)),
        "rotated_45deg_about_z_comparators": {
            "note": ("what the SAME two extractions would read on a medium whose cubic "
                     "axes were rotated 45 deg about z — the branch the off-diagonal "
                     "test is blind to and the direct/assembled identity excludes"),
            "direct_uniaxial_C11_would_read": float(C11_rot45_direct),
            "assembled_would_read": C11_rot45_assembled,
            "their_relative_disagreement": float(C11_rot45_assembled
                                                 / (C11_rot45_direct + 1e-300) - 1.0),
            "measured_relative_disagreement": float(C11_direct / C11_assembled - 1.0),
        },
        "misalignment_bound_about_z": {
            "model": ("a cubic medium rotated by theta about z returns, under the "
                      "tetragonal strain, a lab off-diagonal Sigma_xy = eps*(C'-C44)*"
                      "sin(4 theta) against a diagonal 2*C'*eps at small theta, so "
                      "|sin 4 theta| <= 2*r/|1-A| with r the measured off-diagonal ratio"),
            "zener_A_KUBC": float(A_zener),
            "measured_offdiag_ratio_tetra": dt["max_offdiag_over_max_diag"],
            "implied_abs_sin_4theta_upper_bound": float(sin4theta_bound),
            "implied_theta_upper_bound_deg": float(
                np.degrees(np.arcsin(min(sin4theta_bound, 1.0))) / 4.0),
            "blind_at_theta_45deg": True,
            "theta_45deg_branch_excluded_by": "direct_uniaxial_C11_KUBC identity above",
        },
        "solver": {
            "uniax_cg_residual": a_u["cg_residual"], "uniax_cg_iters": a_u["cg_iters"],
            "tetra_cg_residual": a_t["cg_residual"], "tetra_cg_iters": a_t["cg_iters"],
        },
        "LABEL": ("SUPPLEMENTARY — PR #802 RE-VERIFY repair (F1). KUBC side only. Enters "
                  "NO frozen gate, read or count."),
    }


def _attach_anisotropy(S, row, k_a, k_s, unc_abs):
    """Attach the SUPPLEMENTARY F2 anisotropy block to a configuration row, if the row
    carries both frozen modes and an uncaged reference triple is available."""
    if unc_abs is None or not {"hydro", "shear"} <= set(row["by_mode"]):
        return row
    cp = measure_cprime_abs(S, k_a, k_s)
    blk = anisotropy_axis(row["by_mode"]["hydro"], row["by_mode"]["shear"],
                          cp["Cprime_SUBC"], cp["Cprime_KUBC"], unc_abs)
    blk["tetra_solver"] = {k: cp[k] for k in (
        "subc_cg_residual", "subc_cg_iters", "subc_work_identity_rel",
        "kubc_cg_residual", "kubc_cg_iters", "sigma_bar_SUBC",
        "Sigma_bar_tensor_SUBC")}
    blk["modulus_identity_tetra"] = cp["modulus_identity"]
    # ★F1 repair: the axis-alignment evidence, MEASURED (replaces the load-set Sigma_bar
    # non sequitur the first repair carried). ISOTROPY_CHECK was a bare string; it is now
    # the measurement block, with the superseded claim named inside it.
    blk["ISOTROPY_CHECK"] = isotropy_check(
        S, k_a, k_s, row["by_mode"]["hydro"]["abs"]["K_KUBC"],
        row["by_mode"]["shear"]["abs"]["K_KUBC"], cp["Cprime_KUBC"])
    row["SUPPLEMENTARY_anisotropy_NOT_FROZEN"] = blk
    return row


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
    "shear": "SHEAR modulus G = C44 (the xy engineering-shear cubic constant; pure "
             "deviator, tr=0 in BOTH boundary conditions). ★On a CUBIC medium C44 is "
             "NOT the only shear constant — the tetragonal C' = (C11-C12)/2 is "
             "independent of it, and this medium is cubic-anisotropic (Zener A != 1); "
             "see the SUPPLEMENTARY_anisotropy block.",
    "tetra": "TETRAGONAL cubic shear constant C' = (C11 - C12)/2 (SUPPLEMENTARY, added "
             "by the PR #802 review repair F2; enters NO frozen gate, read or count). "
             "C' is the shear constant the [100] longitudinal modulus C11 = K + 4C'/3 "
             "needs; C44 is the one the [111] longitudinal modulus K + 4C44/3 needs.",
    "note": "frozen prereg §1.2 fixes both ends of each mode; the KUBC prefactor 4.5 = "
            "9/2 is ½·(tr I)² = ½·9 and the SUBC prefactor is ½/K — both pure-K forms. "
            "A ToF/acoustic comparison reads a LONGITUDINAL modulus, and on a CUBIC "
            "medium that modulus is DIRECTION-DEPENDENT: [100] reads C11 = K + 4C'/3, "
            "[111] reads K + 4C44/3, and the two differ whenever the Zener anisotropy "
            "A = C44/C' differs from 1. Measured here: A != 1 under BOTH boundary "
            "conditions, so 'the longitudinal modulus' is not a single number.",
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
def _threshold_classes(rz_primary, rz_conservative):
    """The frozen §5.2 threshold walk applied to a SUPPLEMENTARY axis, through the SAME
    classifier the frozen read uses. NO VOID overlay is applied here — these axes are not
    frozen criteria, so a frozen-gate VOID is not theirs to carry; the frozen read's own
    VOID flags travel with the frozen rows."""
    out = {}
    for name, thr in (("T1_rZ_0.50", T1_RZ), ("T2_rZ_0.45", T2_RZ[0]),
                      ("T2_rZ_0.55", T2_RZ[1])):
        out[name + "_PRIMARY"] = classify_bracket(rz_primary[0], rz_primary[1], thr)
        out[name + "_CONSERVATIVE"] = classify_bracket(rz_conservative[0],
                                                       rz_conservative[1], thr)
    return out


def m_axis(res_h, res_s, unc_m):
    """★NOT A FROZEN CRITERION — a clearly-labelled ADDITIONAL axis shipped alongside the
    frozen bulk-K bracket (KEEP-BOTH). The frozen deliverable is and remains the BULK-K
    bracket of prereg §1.2/§2; nothing here amends, replaces or reweights it.

    ★★AXIS RELABEL, PR #802 review finding F2 (the shipped label was WRONG).  This axis is
    `K + 4·C44/3`.  On an ISOTROPIC medium that equals the P-wave modulus and equals C11.
    THIS MEDIUM IS NOT ISOTROPIC — it is CUBIC, with a measured Zener anisotropy
    `A = C44/C' != 1` under BOTH boundary conditions (see `anisotropy_axis`).  On a cubic
    medium `K + 4·C44/3` is the LONGITUDINAL modulus along the body diagonal [111]; the
    [100] longitudinal modulus is `C11 = K + 4·C'/3` with `C' = (C11 - C12)/2`, and the
    two differ by `(4/3)(C44 - C')`.  The previously shipped label "= C11 for an isotropic
    average" is therefore WITHDRAWN and replaced by the honest one: this is the **[111]
    longitudinal modulus**, and it OVERSTATES the [100] C11 on this medium.  The true C11
    is measured and shipped separately in `anisotropy_axis`.

    WHY IT IS STILL SHIPPED. The frozen `r_Z = √((K_eff/K_0)(ρ_eff/ρ_0))` is built on the
    BULK modulus K, while a normal-incidence acoustic impedance is `Z = ρ c_P = √(ρ·M_L)`
    with a LONGITUDINAL modulus `M_L`, and `√(ρK)` is the correct impedance ONLY for a
    medium with zero shear response. Whether the corpus discriminator should ride K or a
    longitudinal modulus — and, now, WHICH longitudinal modulus — is a DEFINITION question
    this lane does not own and does not settle; it is ROUTED.

    HOW IT IS BOUNDED. `K + 4C44/3` is monotone increasing in BOTH K and C44, and the
    Hill/Huet ordering brackets each of them in the same direction under the same pair of
    boundary conditions. Hence `M_SUBC ≤ M* ≤ M_KUBC` is a legitimate bracket on the
    ABSOLUTE [111] longitudinal modulus, inheriting its rigor from the two absolute
    brackets. The RATIO carries the SAME §2.1 caveat as the bulk axis — `the PRIMARY
    same-instrument bracket cancels the finite-size boundary-layer bias to leading order
    ... but is NOT theorem-grade on the RATIO, because the uncaged reference is itself
    boundary-conditioned` — so BOTH a PRIMARY and a CONSERVATIVE (theorem-grade) ratio
    bracket are shipped, exactly as on the frozen bulk-K axis (F1/F8 repair)."""
    Ks, Kk = res_h["abs"]["K_SUBC"], res_h["abs"]["K_KUBC"]
    Gs, Gk = res_s["abs"]["K_SUBC"], res_s["abs"]["K_KUBC"]
    Ms, Mk = Ks + 4.0 * Gs / 3.0, Kk + 4.0 * Gk / 3.0
    M0s, M0k = unc_m["subc"], unc_m["kubc"]
    R_s, R_k = Ms / (M0s + 1e-300), Mk / (M0k + 1e-300)
    g0_M = M0k / (M0s + 1e-300)
    R_lo, R_hi = R_s / g0_M, R_k * g0_M
    rz_p = [float(np.sqrt(max(min(R_s, R_k), 0.0))),
            float(np.sqrt(max(max(R_s, R_k), 0.0)))]
    rz_c = [float(np.sqrt(max(R_lo, 0.0))), float(np.sqrt(max(R_hi, 0.0)))]
    return {
        "LABEL": "SUPPLEMENTARY AXIS — NOT the frozen deliverable (the frozen bracket is "
                 "on BULK K, prereg sec 1.2). Shipped additively for the modulus-identity "
                 "question, which is ROUTED to Grant, not settled here.",
        "modulus_identity": "[111] LONGITUDINAL modulus M_[111] = K + 4*C44/3 of a CUBIC "
                            "medium. NOT C11: on this medium C11 = K + 4*C'/3 with "
                            "C' = (C11-C12)/2, and C44 != C' (Zener A != 1). The earlier "
                            "shipped label '= C11 for an isotropic average' is WITHDRAWN "
                            "(PR #802 review finding F2) — see anisotropy_axis for the "
                            "measured C' and the true C11.",
        "ANISOTROPY_DISCLOSURE": "the medium is CUBIC, not isotropic; do NOT consume "
                                 "M_SUBC_abs / M_KUBC_abs as C11. A normal-incidence "
                                 "pulse along [100] reads C11 = K + 4*C'/3, which is "
                                 "SMALLER than this axis on this medium.",
        "M_SUBC_abs": float(Ms), "M_KUBC_abs": float(Mk),
        "M_SUBC_uncaged_abs": float(M0s), "M_KUBC_uncaged_abs": float(M0k),
        "absolute_bracket_M": [float(Ms), float(Mk)],
        "absolute_order_ok": bool(Ms <= Mk * (1.0 + G1_SLACK)),
        "R_M_SUBC": float(R_s), "R_M_KUBC": float(R_k),
        "primary_bracket_M": [float(min(R_s, R_k)), float(max(R_s, R_k))],
        "primary_bracket_M_LABEL": "PRIMARY (same-instrument) — NOT theorem-grade on the "
                                   "ratio (frozen sec 2.1 caveat applies verbatim)",
        "conservative_bracket_M": [float(R_lo), float(R_hi)],
        "conservative_bracket_M_LABEL": "CONSERVATIVE (theorem-grade) = "
                                        "[R_M_SUBC/g0_M, R_M_KUBC*g0_M], the frozen "
                                        "sec 2.2 construction applied to this axis",
        "R_M_lo_conservative": float(R_lo), "R_M_hi_conservative": float(R_hi),
        "ratio_order_SUBC_le_KUBC": bool(R_s <= R_k * (1.0 + G1_SLACK)),
        "g0_M_uncaged": float(g0_M),
        "r_Z_M_bracket_rho_ASSUMED_1": rz_p,
        "r_Z_M_bracket_conservative_rho_ASSUMED_1": rz_c,
        "threshold_classes": _threshold_classes(rz_p, rz_c),
        "K_only_counterpart_for_comparison": {
            "R_K_SUBC": res_h["R_SUBC"], "R_K_KUBC": res_h["R_KUBC"],
            "r_Z_K_bracket": res_h["r_Z_bracket_rho_ASSUMED_1"],
            "r_Z_K_bracket_conservative":
                res_h["r_Z_bracket_conservative_rho_ASSUMED_1"]},
        "scope": "K-and-C44-bracketed [111] longitudinal modulus around an ASSUMED "
                 "rho_eff/rho_0 == 1; rho is NOT measured and NOT bracketed by this lane "
                 "(OWED-2 stands, prereg sec 7)",
    }


def bound_robustness_crosscheck_782(configs):
    """★NOT A FROZEN CRITERION — the PR #802 adversarial-review repair, finding F5.

    ★WHY THIS BLOCK EXISTS, stated plainly. This lane banked the status-quo-PRESERVING
    consequence ("#782 BIN-4 and #796 UNDETERMINED stand unchanged") while its own shipped
    JSON already contained the status-quo-UNDERCUTTING one and never stated it. That
    asymmetry is precisely what the anti-rescue fence exists to catch, so the undercutting
    consequence is computed HERE, in the artefact, where it cannot be softened in prose.

    THE CLAIM UNDER TEST is merged #782's, verbatim from
    `research/2026-07-21_rve-aggregation-bench_result.md` §7.1:
      `the MATCHED-side legs (cold r_Z = 0.544, expanded 0.568) are √(KUBC upper bound)
       hence UPPER bounds — consistent with the true r_Z being uniformly ≤ 0.5
       (macro-side); only compressed r_Z = 0.466 < 0.5 is bound-robust.`
    and §5/:12, which carry that compressed leg as the MACRO-side leg of the BIN-4
    `r_Z`-straddle (trigger (iii)) — the sole bound-robust macro-side reading #782 has.

    THE DEFECT. All three of those `r_Z` values are `√(R_KUBC_core)` — the CORE-energy
    estimator. The frozen prereg §2.3 states outright that the core estimator carries NO
    bound status under EITHER boundary condition, and §5.1 REQUIRES this result to report
    where each banked number falls relative to its bracket. The measure the Hill/Huet
    kinematic-uniform theorem actually bounds from above is the WHOLE-CELL apparent
    modulus. So "bound-robust" was asserted of a number on a non-bound-carrying measure.

    WHAT IS COMPUTED. For every #782 pre-stress/wall-class leg this lane also ran, on the
    SAME configuration at `φ_sf`: the core-estimator `r_Z` (which must reproduce #782's own
    shipped JSON leaf bit-for-bit — the anchor), the WHOLE-CELL KUBC `r_Z` (the actual
    upper bound), the WHOLE-CELL SUBC `r_Z` (the lower bound this lane adds), and whether
    the macro-side (`r_Z < 0.5`) reading is bound-robust on each measure. Nothing here
    edits, reframes or re-bins #782 — it is measured, shipped and ROUTED."""
    src = _DRIVERS / "rve_aggregation_bench_results.json"
    J782 = json.loads(src.read_text())
    by_class = J782["leg4_verdict"]["by_class"]
    scan = J782["leg3_phi_scan"]["scan"]
    legs = {"bulk_only_cold": "bulk_only_cold_phi_sf",
            "bulk_only_compressed": "bulk_only_compressed_phi_sf",
            "bulk_only_expanded": "bulk_only_expanded_phi_sf",
            "symmetric_cold": "symmetric_cold_phi_sf"}
    rows = []
    for leg, cfg in legs.items():
        h = [c for c in configs if c["config"] == cfg][0]["by_mode"]["hydro"]
        core_k = float(h["R_KUBC_core"])
        rz_core = float(np.sqrt(max(core_k, 0.0)))
        rz_kubc = float(np.sqrt(max(h["R_KUBC"], 0.0)))
        rz_subc = float(np.sqrt(max(h["R_SUBC"], 0.0)))
        m782 = by_class[leg]
        rows.append({
            "leg_782": leg, "config_here": cfg,
            "K_782_shipped_core": float(m782["K_eff_over_K0_sf"]),
            "K_here_core": core_k,
            "reproduces_782_core_bitwise": bool(
                core_k == float(m782["K_eff_over_K0_sf"])),
            "r_Z_782_shipped_core": float(m782["by_beta"]["beta_0"]["r_Z"]),
            "r_Z_here_CORE_estimator_NO_BOUND_STATUS": rz_core,
            "r_Z_here_WHOLE_CELL_KUBC_the_actual_UPPER_bound": rz_kubc,
            "r_Z_here_WHOLE_CELL_SUBC_the_LOWER_bound": rz_subc,
            "macro_side_on_CORE_estimator": bool(rz_core < T1_RZ),
            "macro_side_BOUND_ROBUST_on_the_bound_carrying_KUBC": bool(rz_kubc < T1_RZ),
            "two_sided_class_vs_T1": classify_bracket(rz_subc, rz_kubc, T1_RZ),
            "core_estimator_sits_BELOW_the_bound_carrying_KUBC_reading":
                bool(rz_core < rz_kubc),
        })
    n_core = sum(r["macro_side_on_CORE_estimator"] for r in rows)
    n_bound = sum(r["macro_side_BOUND_ROBUST_on_the_bound_carrying_KUBC"] for r in rows)
    # ── ★F3 (PR #802 RE-VERIFY repair): the OTHER 'cross-class flip' in #782 — the one
    #    at :114 (sec 6, LEG 4/VERDICT) — is the f_incl BIN-2-vs-BIN-4 split, and it is
    #    COLLAPSE-GATE-driven, not r_Z-driven. This lane does NOT touch it. Measured
    #    from #782's own artefact so the non-dependence is checkable, not asserted.
    coll = {k: {"max_rel_disagreement": float(v["collapse_f_incl"]
                                              ["max_rel_disagreement"]),
                "collapses": bool(v["collapse_f_incl"]["collapses"])}
            for k, v in scan.items()}
    f_incl_not_touched = {
        "WHAT_IT_IS": (
            "research/2026-07-21_rve-aggregation-bench_result.md:114 (sec 6, LEG 4 / "
            "VERDICT) uses the words 'a verdict-controlling cross-class flip' for the "
            "f_incl BIN-2-vs-BIN-4 split, NOT for the r_Z macro/matched split of :12."),
        "WHY_IT_IS_NOT_r_Z_DRIVEN": (
            "rve_aggregation_bench._bin_of returns BIN4_REGIME_UNDETERMINED whenever "
            "collapse_ok is False, BEFORE r_Z is consulted at all. bulk_only_compressed "
            "FAILS the f_incl collapse gate and therefore reads BIN-4 for ANY r_Z, "
            "while bulk_only_cold and bulk_only_expanded PASS it and read BIN-2."),
        "collapse_f_incl_by_class_782": coll,
        "collapse_threshold_782": 0.30,
        "NOT_TOUCHED_BY_THIS_LANE": (
            "this lane changes the MEASURE r_Z is read on; it does not touch the "
            "f_incl collapse gate, which is a phi-vs-f_incl scaling-collapse test on "
            "#782's own scan. The f_incl BIN-2/BIN-4 flip therefore PERSISTS UNCHANGED "
            "on the bound-carrying measure. Only :12's r_Z macro/matched clause "
            "evaporates."),
    }

    return {
        "LABEL": "SUPPLEMENTARY — NOT a frozen criterion, in no frozen gate, read or "
                 "count. PR #802 adversarial-review repair, finding F5.",
        "source_782": "research/drivers/rve_aggregation_bench_results.json "
                      "(leg4_verdict.by_class), read at run time — NOT retyped.",
        "claim_under_test_782_sec_7p1": (
            "only compressed r_Z = 0.466 < 0.5 is bound-robust "
            "(research/2026-07-21_rve-aggregation-bench_result.md:124)"),
        "rows": rows,
        "n_legs": len(rows),
        "n_macro_side_on_the_CORE_estimator": n_core,
        "n_macro_side_BOUND_ROBUST_on_the_bound_carrying_WHOLE_CELL_KUBC": n_bound,
        "f_incl_cross_class_flip_NOT_TOUCHED_F3": f_incl_not_touched,
        "FINDING": (
            "#782's macro-side legs are macro-side ONLY on the CORE estimator, which the "
            "frozen prereg §2.3 says carries NO bound status. On the WHOLE-CELL apparent "
            "modulus — the measure the Hill/Huet kinematic-uniform theorem actually bounds "
            "from above — NO leg's upper bound falls below the r_Z = 0.5 macro-cage edge. "
            "So #782's SOLE bound-robust macro-side reading does NOT survive the change to "
            "the bound-carrying measure: it is not bound-robust, it is estimator-"
            "conditional. The core estimator reads systematically BELOW the bound-carrying "
            "KUBC value at every leg (column above), which is the direction that "
            "manufactures a macro-side reading out of a measure that cannot support one."),
        "WHAT_THIS_DOES_NOT_DO": (
            "it does NOT re-bin #782. BIN-4 is UNDETERMINED, and removing a bound-robust "
            "macro-side leg makes the r_Z axis MORE undetermined, not less — see the "
            "two_sided_class_vs_T1 column, which STRADDLES at every leg on the two-sided "
            "bracket. What changes is the BASIS #782 §7.1 states for the straddle, not the "
            "bin. This lane edits no merged doc and mints no bin; the basis correction is "
            "ROUTED to Grant / the auditor lane, in the same shape as the basis correction "
            "already routed from the rho-flags audit."),
    }


def anisotropy_axis(res_h, res_s, cp_subc, cp_kubc, unc_abs):
    """★NOT A FROZEN CRITERION — the PR #802 review finding-F2 repair, shipped ADDITIVELY.

    The frozen prereg, the driver and the first result doc all assumed, without ever
    checking, that a VRH/isotropic reading of the srs-z3 composite was adequate. It is
    not: the medium is CUBIC and measurably anisotropic. This block ships, for the arm and
    for the cold uncaged reference, under BOTH boundary conditions:

      K       — bulk modulus                     (frozen `hydro` mode)
      C44     — the xy engineering shear constant (frozen `shear` mode)
      C'      — the tetragonal shear constant (C11-C12)/2 (SUPPLEMENTARY `tetra` mode)
      A       — the ZENER anisotropy ratio C44/C'  (A = 1 iff the medium is isotropic)
      M_[111] — K + 4*C44/3, the longitudinal modulus along the body diagonal
      C11     — K + 4*C'/3,  the longitudinal modulus along [100]  (the TRUE cubic C11)

    ★WHY IT MATTERS AND WHERE IT IS ROUTED. A cubic medium has NO single "longitudinal
    modulus": the longitudinal wave speed depends on the propagation direction. Protocol E
    launches its pulse along [100], so the comparator for a Protocol-E time-of-flight is
    `C11 = K + 4*C'/3` — NOT the `K + 4*C44/3` axis this driver previously (mis)labelled
    "C11 for an isotropic average", and NOT a VRH isotropic average of the two. That
    SHARPENS the already-routed modulus-identity question rather than answering it, and it
    is ROUTED to Grant with data, not settled here.

    Bound status: `C11 = K + 4C'/3` is monotone increasing in BOTH K and C', each of which
    the Hill/Huet ordering brackets in the same direction under the same boundary-condition
    pair, so `C11_SUBC <= C11* <= C11_KUBC` is a legitimate ABSOLUTE bracket, exactly as
    for the [111] axis. The RATIO again carries the frozen sec 2.1 non-theorem-grade
    caveat, so PRIMARY and CONSERVATIVE ratio brackets are both shipped."""
    Ks, Kk = res_h["abs"]["K_SUBC"], res_h["abs"]["K_KUBC"]
    C44s, C44k = res_s["abs"]["K_SUBC"], res_s["abs"]["K_KUBC"]
    Cps, Cpk = float(cp_subc), float(cp_kubc)
    M111s, M111k = Ks + 4.0 * C44s / 3.0, Kk + 4.0 * C44k / 3.0
    C11s, C11k = Ks + 4.0 * Cps / 3.0, Kk + 4.0 * Cpk / 3.0
    u = unc_abs
    C11_0s = u["K_SUBC"] + 4.0 * u["Cp_SUBC"] / 3.0
    C11_0k = u["K_KUBC"] + 4.0 * u["Cp_KUBC"] / 3.0
    M111_0s = u["K_SUBC"] + 4.0 * u["C44_SUBC"] / 3.0
    M111_0k = u["K_KUBC"] + 4.0 * u["C44_KUBC"] / 3.0
    R_s, R_k = C11s / (C11_0s + 1e-300), C11k / (C11_0k + 1e-300)
    g0_C11 = C11_0k / (C11_0s + 1e-300)
    R_lo, R_hi = R_s / g0_C11, R_k * g0_C11
    rz_p = [float(np.sqrt(max(min(R_s, R_k), 0.0))),
            float(np.sqrt(max(max(R_s, R_k), 0.0)))]
    rz_c = [float(np.sqrt(max(R_lo, 0.0))), float(np.sqrt(max(R_hi, 0.0)))]
    return {
        "LABEL": "SUPPLEMENTARY — NOT a frozen criterion, NOT in any frozen gate, read or "
                 "count. Added by the PR #802 adversarial-review repair (finding F2).",
        "ISOTROPY_CHECK": "the medium is CUBIC-ANISOTROPIC: Zener A = C44/C' != 1 under "
                          "BOTH boundary conditions. No isotropy check existed in the "
                          "frozen prereg, the driver or the first result doc.",
        "absolutes_arm": {
            "K_SUBC": float(Ks), "K_KUBC": float(Kk),
            "C44_SUBC": float(C44s), "C44_KUBC": float(C44k),
            "Cprime_SUBC": Cps, "Cprime_KUBC": Cpk,
            "M_111_SUBC": float(M111s), "M_111_KUBC": float(M111k),
            "C11_true_SUBC": float(C11s), "C11_true_KUBC": float(C11k),
        },
        "absolutes_uncaged_reference": {
            "K_SUBC": float(u["K_SUBC"]), "K_KUBC": float(u["K_KUBC"]),
            "C44_SUBC": float(u["C44_SUBC"]), "C44_KUBC": float(u["C44_KUBC"]),
            "Cprime_SUBC": float(u["Cp_SUBC"]), "Cprime_KUBC": float(u["Cp_KUBC"]),
            "M_111_SUBC": float(M111_0s), "M_111_KUBC": float(M111_0k),
            "C11_true_SUBC": float(C11_0s), "C11_true_KUBC": float(C11_0k),
        },
        "zener_A_arm": {"SUBC": float(C44s / (Cps + 1e-300)),
                        "KUBC": float(C44k / (Cpk + 1e-300))},
        "zener_A_uncaged_reference": {
            "SUBC": float(u["C44_SUBC"] / (u["Cp_SUBC"] + 1e-300)),
            "KUBC": float(u["C44_KUBC"] / (u["Cp_KUBC"] + 1e-300))},
        "M_111_overstates_C11_by_arm": {
            "SUBC": float(M111s / (C11s + 1e-300) - 1.0),
            "KUBC": float(M111k / (C11k + 1e-300) - 1.0)},
        "M_111_overstates_C11_by_uncaged": {
            "SUBC": float(M111_0s / (C11_0s + 1e-300) - 1.0),
            "KUBC": float(M111_0k / (C11_0k + 1e-300) - 1.0)},
        "absolute_bracket_C11_true": [float(C11s), float(C11k)],
        "absolute_order_ok": bool(C11s <= C11k * (1.0 + G1_SLACK)),
        "R_C11_SUBC": float(R_s), "R_C11_KUBC": float(R_k),
        "primary_bracket_C11": [float(min(R_s, R_k)), float(max(R_s, R_k))],
        "conservative_bracket_C11": [float(R_lo), float(R_hi)],
        "g0_C11_uncaged": float(g0_C11),
        "r_Z_C11_bracket_rho_ASSUMED_1": rz_p,
        "r_Z_C11_bracket_conservative_rho_ASSUMED_1": rz_c,
        "threshold_classes": _threshold_classes(rz_p, rz_c),
        "ROUTED_TO_GRANT": (
            "a CUBIC medium has a DIRECTION-DEPENDENT longitudinal modulus. Protocol E "
            "launches along [100], so a Protocol-E time-of-flight comparator is "
            "C11 = K + 4*C'/3 — NOT the K + 4*C44/3 axis and NOT a VRH isotropic "
            "average. This SHARPENS the routed modulus-identity question; it does not "
            "answer it, and this lane does not answer it."),
        "scope": "K-and-C'-bracketed [100] C11 around an ASSUMED rho_eff/rho_0 == 1; rho "
                 "is NOT measured and NOT bracketed (OWED-2 stands, prereg sec 7)",
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
                    eps_pre=0.0, s_rail=S_RAIL_DEEP, unc_abs=None):
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
    return _attach_anisotropy(S, row, k_a, k_s, unc_abs)


def run_operator_config(S, unc, label, k_a, k_s, modes=("hydro",), extra=None,
                        unc_abs=None):
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
    return _attach_anisotropy(S, row, k_a, k_s, unc_abs)


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
    # ★HONEST DENOMINATORS for the RATIO clause (PR #802 review repair, finding F3).
    #  `rows` mixes two populations: the 42 (configuration, mode) measurements, which have
    #  a real ratio pair and CAN fail the ratio clause, and the 6 uncaged-reference rows,
    #  which are written with R_SUBC = R_KUBC = 1.0 and `ratio_order_ok = True` BY
    #  CONSTRUCTION and therefore cannot fail it. Quoting "8 of 48" (or a clean "24 of 24"
    #  on the hydro side) silently inflates the denominator with rows that cannot fail.
    ratio_bearing = [r for r in rows if r["config"] != "uncaged_reference"]
    hydro_bearing = [r for r in ratio_bearing if r["mode"] == "hydro"]
    shear_bearing = [r for r in ratio_bearing if r["mode"] == "shear"]
    ratio_viol = [v for v in violations if not v["ratio_order_ok"]]
    honest = {
        "n_rows_walked_including_uncaged_identity_rows": len(rows),
        "n_uncaged_identity_rows_that_CANNOT_fail_the_ratio_clause":
            len(rows) - len(ratio_bearing),
        "n_ratio_bearing_measurements": len(ratio_bearing),
        "n_ratio_bearing_hydro": len(hydro_bearing),
        "n_ratio_bearing_shear": len(shear_bearing),
        "ratio_clause_violations": len(ratio_viol),
        "ratio_clause_inversion_rate_over_ratio_bearing_rows":
            float(len(ratio_viol) / max(len(ratio_bearing), 1)),
        "hydro_ratio_clause_violations":
            len([v for v in ratio_viol if v["mode"] == "hydro"]),
        "shear_ratio_clause_violations":
            len([v for v in ratio_viol if v["mode"] == "shear"]),
        "note": "the uncaged-reference rows carry R_SUBC = R_KUBC = 1.0 and "
                "ratio_order_ok = True BY CONSTRUCTION; they exercise only G1's ABSOLUTE "
                "clause. The honest denominator for the RATIO clause is therefore the "
                "ratio-bearing measurement count, not the walked-row count.",
    }
    return {"rows": rows, "n_checked": len(rows), "violations": violations,
            "honest_ratio_clause_denominators": honest,
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

    def _disposition(cls):
        if cls == "VOID":
            return ("VOID — bracket NOT reported as physics; the standing merged verdict "
                    "for this configuration is left exactly as merged (frozen §5.5 "
                    "item 4)")
        if cls == "STRADDLES":
            return ("BOUND-CONDITIONAL — the corpus verdict is NOT tightened in either "
                    "direction; #782 BIN-4 and #796 UNDETERMINED STAND UNCHANGED; no new "
                    "bin, no side picked, no rescue (frozen §5.5 item 1)")
        if cls == "RESOLVES-LOW":
            return ("the macro-side reading is BOUND-ROBUST for this arm — an INPUT to "
                    "the Reading-B re-open question and to nothing else; surfaced and "
                    "ROUTED, not landed (frozen §5.5 item 2)")
        return ("the matched-side reading is BOUND-ROBUST for this arm and the #782 "
                "§7.1 'matched-side is KUBC-conditional' caveat is discharged FOR THIS "
                "ARM; surfaced and ROUTED, not landed (frozen §5.5 item 3)")

    disp = []
    for r in reads:
        c1 = r["classes"]["T1_rZ_0.50_PRIMARY"]
        c1c = r["classes"]["T1_rZ_0.50_CONSERVATIVE"]
        nv_p = r["classes_no_void_overlay"]["T1_rZ_0.50_PRIMARY"]
        nv_c = r["classes_no_void_overlay"]["T1_rZ_0.50_CONSERVATIVE"]
        identity = bool(r["config"] == "uniform_medium_null")
        # ★THE THIRD FROZEN AMBIGUITY (PR #802 review repair, finding F7), surfaced.
        #  Frozen §5.5 names its items by OUTCOME CLASS ("if a bracket STRADDLES", "if a
        #  bracket RESOLVES-HIGH") but never says WHICH of the two frozen bracket
        #  definitions (§2.1 PRIMARY / §2.2 CONSERVATIVE) the word "a bracket" denotes.
        #  On this data the two definitions disagree at many rows, so item 1 and item 3
        #  have their antecedents satisfied SIMULTANEOUSLY on the same configuration.
        both = bool(nv_p in ("RESOLVES-HIGH", "RESOLVES-LOW") and nv_c == "STRADDLES")
        disp.append({"config": r["config"], "mode": r["mode"],
                     "is_G2a_IDENTITY_row_not_a_physics_disposition": identity,
                     "class_vs_T1_PRIMARY": c1,
                     "class_vs_T1_CONSERVATIVE": c1c,
                     "class_vs_T1_PRIMARY_void_scope_per_mode":
                         r["classes_void_scope_per_mode"]["T1_rZ_0.50_PRIMARY"],
                     "class_vs_T1_PRIMARY_no_void_overlay": nv_p,
                     "class_vs_T1_CONSERVATIVE_no_void_overlay": nv_c,
                     # the shipped field, basis now stated on its face rather than implied
                     "pre_registered_disposition": _disposition(c1),
                     "pre_registered_disposition_BASIS":
                         "the §2.1 PRIMARY bracket vs T1, with the STRICT G1 VOID overlay",
                     "pre_registered_disposition_on_CONSERVATIVE": _disposition(c1c),
                     "frozen_5p5_antecedent_audit": {
                         "item1_STRADDLE_antecedent_satisfied_on_PRIMARY":
                             bool(nv_p == "STRADDLES"),
                         "item1_STRADDLE_antecedent_satisfied_on_CONSERVATIVE":
                             bool(nv_c == "STRADDLES"),
                         "item3_RESOLVES_HIGH_antecedent_satisfied_on_PRIMARY":
                             bool(nv_p == "RESOLVES-HIGH"),
                         "item3_RESOLVES_HIGH_antecedent_satisfied_on_CONSERVATIVE":
                             bool(nv_c == "RESOLVES-HIGH"),
                         "BOTH_item1_and_item3_antecedents_satisfied": both,
                         "ambiguity": "frozen §5.5 does not say which of the two frozen "
                                      "bracket definitions 'a bracket' denotes; where "
                                      "BOTH is true, items 1 and 3 fire together and the "
                                      "frozen text does not adjudicate between them",
                     }})
    classes_seen = sorted({r["classes"][k] for r in reads for k in r["classes"]})
    classes_seen_no_void = sorted({v for r in reads
                                   for v in r["classes_no_void_overlay"].values()})
    straddle_any = any(v == "STRADDLES" for r in reads
                       for v in r["classes_no_void_overlay"].values())

    # ★F6 — reconcile the JSON's own §5.5-item-3 invocations with what the prose says.
    def _rows(pred):
        return sorted(f"{d['config']}::{d['mode']}" for d in disp if pred(d))

    item3_primary = _rows(lambda d: d["class_vs_T1_PRIMARY"] == "RESOLVES-HIGH")
    item3_cons = _rows(lambda d: d["class_vs_T1_CONSERVATIVE"] == "RESOLVES-HIGH")
    item3_primary_ident = _rows(
        lambda d: d["class_vs_T1_PRIMARY"] == "RESOLVES-HIGH"
        and d["is_G2a_IDENTITY_row_not_a_physics_disposition"])
    both_rows = _rows(
        lambda d: d["frozen_5p5_antecedent_audit"]["BOTH_item1_and_item3_antecedents_"
                                                   "satisfied"])
    headline_keys = {"bulk_only_cold_phi_sf::hydro", "grown_frozen_tangent::hydro"}
    item3_audit = {
        "n_rows": len(disp),
        "rows_where_the_shipped_PRIMARY_basis_emits_the_item3_string": item3_primary,
        "n_rows_item3_on_PRIMARY": len(item3_primary),
        "of_which_are_the_G2a_IDENTITY_null": item3_primary_ident,
        "rows_where_the_CONSERVATIVE_basis_would_emit_item3": item3_cons,
        "n_rows_item3_on_CONSERVATIVE": len(item3_cons),
        "item3_invoked_at_a_HEADLINE_arm_on_PRIMARY":
            sorted(headline_keys & set(item3_primary)),
        "item3_invoked_at_a_HEADLINE_arm_on_CONSERVATIVE":
            sorted(headline_keys & set(item3_cons)),
        "RECONCILIATION": (
            "the shipped per-row disposition string is generated from the §2.1 PRIMARY "
            "class with the STRICT VOID overlay, so it emits the frozen §5.5 item-3 "
            "sentence ('the #782 §7.1 caveat is discharged FOR THIS ARM') on the rows "
            "listed above — INCLUDING the G2a identity null, whose bracket is [1.0, 1.0] "
            "by construction and is not a physics disposition at all. The result doc's "
            "statement that item 3 is not invoked is TRUE OF THE HEADLINE ARMS ON THE "
            "THEOREM-GRADE BRACKET and false as a statement about the whole JSON. Both "
            "counts are shipped here so the doc and the artefact cannot drift apart."),
    }
    void_audit = {
        "VOID_scoping_carried": "STRICT (a violation in EITHER mode voids the whole "
                                "configuration)",
        "rows_VOID_under_STRICT": _rows(lambda d: d["class_vs_T1_PRIMARY"] == "VOID"),
        "n_rows_VOID_under_STRICT":
            len(_rows(lambda d: d["class_vs_T1_PRIMARY"] == "VOID")),
        "ASYMMETRY_SURFACED": (
            "frozen §5.5 item 4 says a VOIDed configuration's bracket is NOT reported as "
            "physics and its standing verdict is left exactly as merged. Item 1's "
            "STRADDLE disposition and item 4's VOID disposition therefore have the SAME "
            "practical consequence (nothing moves), which is why taking item 1 on a "
            "VOIDed arm looks harmless — but it is still a disposition taken on a row "
            "the frozen text says is not physics. Item 3 is the only item whose "
            "consequence differs from VOID's (it would DISCHARGE a standing caveat), and "
            "it is the one refused. Stated plainly: the ONLY frozen §5.5 disposition "
            "that survives a VOID is item 4 — nothing moves. Items 1, 2 and 3 all "
            "presuppose a readable bracket, so on a VOIDed row none of them is available, "
            "and the fact that item 1 and item 4 agree on the outcome does not make item "
            "1 available. This lane therefore reports NOTHING MOVED on every row, which "
            "is item 4's consequence on the VOIDed rows and item 1's on the rest."),
        "BOTH_antecedents_satisfied_rows": both_rows,
        "n_BOTH_antecedents_satisfied": len(both_rows),
    }
    return {
        "frozen_5p5_item3_invocation_audit": item3_audit,
        "VOID_and_ambiguity_consistency_audit": void_audit,
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
    SS, unc_meta, unc, unc_abs = {}, {}, {}, {}
    for L in L_SIZES:
        SS[L] = setup(L)
        SS[L]["components"] = component_count(SS[L]["geom"][1], SS[L]["geom"][2],
                                              SS[L]["act"])
        print(f"[uncaged] L={L} N={SS[L]['N']} active={SS[L]['n_active']} "
              f"components={SS[L]['components']}")
        unc_meta[L], unc[L] = uncaged_and_g0(SS[L], ("hydro", "shear"))
        # ── SUPPLEMENTARY (F2): the uncaged tetragonal C' under BOTH boundary conditions
        M0 = SS[L]["geom"][1].shape[0]
        cp0 = measure_cprime_abs(SS[L], np.full(M0, float(RHO_STAR)),
                                 np.full(M0, float(K_S)))
        bm = unc_meta[L]["by_mode"]
        unc_abs[L] = {
            "K_SUBC": bm["hydro"]["K_SUBC_abs"], "K_KUBC": bm["hydro"]["K_KUBC_abs"],
            "C44_SUBC": bm["shear"]["K_SUBC_abs"], "C44_KUBC": bm["shear"]["K_KUBC_abs"],
            "Cp_SUBC": cp0["Cprime_SUBC"], "Cp_KUBC": cp0["Cprime_KUBC"],
        }
        unc_meta[L]["SUPPLEMENTARY_anisotropy_NOT_FROZEN"] = {
            "LABEL": "SUPPLEMENTARY — PR #802 review repair (F2). NOT a frozen criterion "
                     "and in no frozen gate, read or count.",
            "Cprime_SUBC": cp0["Cprime_SUBC"], "Cprime_KUBC": cp0["Cprime_KUBC"],
            "C44_SUBC": unc_abs[L]["C44_SUBC"], "C44_KUBC": unc_abs[L]["C44_KUBC"],
            "K_SUBC": unc_abs[L]["K_SUBC"], "K_KUBC": unc_abs[L]["K_KUBC"],
            "zener_A_SUBC": float(unc_abs[L]["C44_SUBC"] / cp0["Cprime_SUBC"]),
            "zener_A_KUBC": float(unc_abs[L]["C44_KUBC"] / cp0["Cprime_KUBC"]),
            "M_111_SUBC": float(unc_abs[L]["K_SUBC"] + 4.0 * unc_abs[L]["C44_SUBC"] / 3.0),
            "M_111_KUBC": float(unc_abs[L]["K_KUBC"] + 4.0 * unc_abs[L]["C44_KUBC"] / 3.0),
            "C11_true_SUBC": float(unc_abs[L]["K_SUBC"] + 4.0 * cp0["Cprime_SUBC"] / 3.0),
            "C11_true_KUBC": float(unc_abs[L]["K_KUBC"] + 4.0 * cp0["Cprime_KUBC"] / 3.0),
            "M_111_overstates_C11_by_SUBC": float(
                (unc_abs[L]["K_SUBC"] + 4.0 * unc_abs[L]["C44_SUBC"] / 3.0)
                / (unc_abs[L]["K_SUBC"] + 4.0 * cp0["Cprime_SUBC"] / 3.0) - 1.0),
            "M_111_overstates_C11_by_KUBC": float(
                (unc_abs[L]["K_KUBC"] + 4.0 * unc_abs[L]["C44_KUBC"] / 3.0)
                / (unc_abs[L]["K_KUBC"] + 4.0 * cp0["Cprime_KUBC"] / 3.0) - 1.0),
            "tetra_solver": {k: cp0[k] for k in (
                "subc_cg_residual", "subc_cg_iters", "subc_work_identity_rel",
                "kubc_cg_residual", "kubc_cg_iters", "sigma_bar_SUBC",
                "Sigma_bar_tensor_SUBC")},
            "modulus_identity": cp0["modulus_identity"],
            "ISOTROPY_CHECK": isotropy_check(
                SS[L], np.full(M0, float(RHO_STAR)), np.full(M0, float(K_S)),
                unc_abs[L]["K_KUBC"], unc_abs[L]["C44_KUBC"], cp0["Cprime_KUBC"]),
        }
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
                                       ROUTE_A["s"], BOTH_MODES,
                                       unc_abs=unc_abs[L_BASE]))
    print("[A] route-A phi scan, symmetric_cold (wall-class control) ...")
    for rc in ROUTE_A["r_cage"]:
        lab = ("symmetric_cold_phi_sf" if rc == ROUTE_A["r_cage"][-1]
               else f"symmetric_cold_rc{rc}")
        configs.append(run_cage_config(S, unc[L_BASE], lab, "symmetric", rc,
                                       ROUTE_A["s"], BOTH_MODES,
                                       unc_abs=unc_abs[L_BASE]))
    print("[A] pre-stress arms + rigid STOP-gate mirror ...")
    configs.append(run_cage_config(S, unc[L_BASE], "bulk_only_compressed_phi_sf",
                                   "bulk_only", PHI_SF_RCAGE, PHI_SF_S, BOTH_MODES,
                                   eps_pre=-0.08, unc_abs=unc_abs[L_BASE]))
    configs.append(run_cage_config(S, unc[L_BASE], "bulk_only_expanded_phi_sf",
                                   "bulk_only", PHI_SF_RCAGE, PHI_SF_S, BOTH_MODES,
                                   eps_pre=+0.08, unc_abs=unc_abs[L_BASE]))
    configs.append(run_cage_config(S, unc[L_BASE], "rigid_phi_sf", "rigid",
                                   PHI_SF_RCAGE, PHI_SF_S, BOTH_MODES,
                                   unc_abs=unc_abs[L_BASE]))
    print("[A] route-B (the second collapse route) ...")
    for s_b in ROUTE_B["s"]:
        configs.append(run_cage_config(S, unc[L_BASE], f"routeB_bulk_only_cold_s{s_b}",
                                       "bulk_only", ROUTE_B["r_cage"], s_b, BOTH_MODES,
                                       unc_abs=unc_abs[L_BASE]))

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
                                      "operating point (FROZEN, u-independent)"},
        unc_abs=unc_abs[L_BASE]))
    configs.append(run_operator_config(
        S, unc[L_BASE], "painted_anisotropic", ka_grown, kse_grown, BOTH_MODES,
        extra={"same_operator_as": "grown_frozen_tangent",
               "note": "on the #796 carve this is the SAME operator as configuration 7; "
                       "running both is the G6 cross-check that our reconstruction of the "
                       "#796 operating point is faithful, NOT two physics arms"},
        unc_abs=unc_abs[L_BASE]))
    ka_iso, ks_iso = cage_bond_stiffness(S["geom"][3], S["geom"][4], centers_sf,
                                         PHI_SF_RCAGE, CAGE_W, VERDICT_WALL,
                                         VERDICT_S_RAIL, 0.0)
    configs.append(run_operator_config(
        S, unc[L_BASE], "isotropic_control", np.asarray(ka_iso, float),
        np.asarray(ks_iso, float), BOTH_MODES,
        extra={"fractions": realized_fractions(S, centers_sf, PHI_SF_RCAGE, PHI_SF_S),
               "note": "the #782 bulk_only_cold cage at phi_sf with k_s = KS0 — the "
                       "crash BASELINE K_ratio_lift normalizes against"},
        unc_abs=unc_abs[L_BASE]))

    # ── §3 C — the uniform-medium null + the size scan ───────────────────────
    print("[C] uniform-medium null + size scan ...")
    M0 = S["geom"][1].shape[0]
    null_row = run_operator_config(S, unc[L_BASE], "uniform_medium_null",
                                   np.full(M0, float(RHO_STAR)),
                                   np.full(M0, float(K_S)), ("hydro", "shear"),
                                   extra={"n_cages": 0},
                                   unc_abs=unc_abs[L_BASE])
    configs.append(null_row)
    size_rows = []
    for L in L_SIZES:
        if L == L_BASE:
            row = [c for c in configs if c["config"] == "bulk_only_cold_phi_sf"][0]
        else:
            row = run_cage_config(SS[L], unc[L], f"bulk_only_cold_phi_sf_L{L}",
                                  "bulk_only", PHI_SF_RCAGE, PHI_SF_S, BOTH_MODES,
                                  unc_abs=unc_abs[L])
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
        "K (prereg sec 1.2). A normal-incidence impedance Z = rho*c_P carries a "
        "LONGITUDINAL modulus, and sqrt(rho*K) is the right impedance only for a medium "
        "with no shear response — which this composite is not (G_eff/G_0 ~ 0.67). "
        "★PR #802 review finding F2: the shipped axis K + 4*C44/3 was mislabelled 'the "
        "P-wave modulus M (= C11 for an isotropic average)'. This medium is CUBIC, not "
        "isotropic (Zener A != 1 under BOTH boundary conditions), so K + 4*C44/3 is the "
        "[111] longitudinal modulus and the [100] one is C11 = K + 4*C'/3 with "
        "C' = (C11-C12)/2. BOTH are now measured and shipped (see "
        "SUPPLEMENTARY_anisotropy_NOT_FROZEN on every configuration). WHICH modulus the "
        "corpus discriminator r_Z should ride — and now, WHICH DIRECTION'S longitudinal "
        "modulus — is a DEFINITION question ROUTED to Grant and NOT settled by this lane. "
        "No frozen criterion is amended.")

    out["configurations"] = configs
    # ── SUPPLEMENTARY (additive, NOT frozen): the F5 anti-rescue cross-check ──
    out["F5_782_bound_robustness_crosscheck_NOT_FROZEN"] = \
        bound_robustness_crosscheck_782(configs)
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
    lift_s_core = gh["R_SUBC_core"] / (ic["R_SUBC_core"] + 1e-300)
    lift_k_core = gh["R_KUBC_core"] / (ic["R_KUBC_core"] + 1e-300)
    variants = {"whole_cell_SUBC": float(lift_s), "whole_cell_KUBC": float(lift_k),
                "core_convention_SUBC": float(lift_s_core),
                "core_convention_KUBC": float(lift_k_core)}
    out["verdict"] = verdict(reads, {
        "lift_under_SUBC": float(lift_s), "lift_under_KUBC": float(lift_k),
        "all_four_variants": variants,
        "worst_departure_from_unity": float(max(abs(v - 1.0)
                                                for v in variants.values())),
        "WHAT_WAS_MEASURED": (
            "this lane's lift is (grown_frozen_tangent ratio) / (isotropic_control "
            "ratio) recomputed IN THIS DRIVER under each boundary condition. It is NOT "
            "#796's banked K_ratio_lift read back — that is a different construction on "
            "#796's own arms — and the frozen T4 band test (L1 < 1.2 / L2 / L3) CANNOT "
            "FIRE on values this close to 1: all four variants sit within "
            "the worst-departure figure above of unity, so every variant is L1 by "
            "arithmetic and 'the band does not flip across the boundary condition' is "
            "not a discriminating statement. What IS supported: the grown-vs-control "
            "ratio is ~1 under BOTH boundary conditions on BOTH energy conventions, i.e. "
            "the near-null lift this bench family measures is not an artefact of "
            "clamping the outer skin."),
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
            print("    [SUPPL, not frozen] [111] long. M=K+4*C44/3: R_M PRIMARY "
                  "[%.5f, %.5f] -> r_Z [%.5f, %.5f]" % (
                      ma["primary_bracket_M"][0], ma["primary_bracket_M"][1],
                      ma["r_Z_M_bracket_rho_ASSUMED_1"][0],
                      ma["r_Z_M_bracket_rho_ASSUMED_1"][1]))
            print("    [SUPPL, not frozen] [111] long. M: R_M CONSERVATIVE "
                  "[%.5f, %.5f] -> r_Z [%.5f, %.5f]" % (
                      ma["conservative_bracket_M"][0], ma["conservative_bracket_M"][1],
                      ma["r_Z_M_bracket_conservative_rho_ASSUMED_1"][0],
                      ma["r_Z_M_bracket_conservative_rho_ASSUMED_1"][1]))
        if mc and "SUPPLEMENTARY_anisotropy_NOT_FROZEN" in mc[0]:
            an = mc[0]["SUPPLEMENTARY_anisotropy_NOT_FROZEN"]
            print("    [SUPPL, not frozen] CUBIC: Zener A arm SUBC %.4f / KUBC %.4f ; "
                  "C11_true [%.5f, %.5f]" % (
                      an["zener_A_arm"]["SUBC"], an["zener_A_arm"]["KUBC"],
                      an["absolute_bracket_C11_true"][0],
                      an["absolute_bracket_C11_true"][1]))
            print("    [SUPPL, not frozen] C11 r_Z PRIMARY [%.5f, %.5f]  "
                  "CONSERVATIVE [%.5f, %.5f]" % (
                      an["r_Z_C11_bracket_rho_ASSUMED_1"][0],
                      an["r_Z_C11_bracket_rho_ASSUMED_1"][1],
                      an["r_Z_C11_bracket_conservative_rho_ASSUMED_1"][0],
                      an["r_Z_C11_bracket_conservative_rho_ASSUMED_1"][1]))
    f5 = out["F5_782_bound_robustness_crosscheck_NOT_FROZEN"]
    print("\n[SUPPLEMENTARY F5 — #782 bound-robustness cross-check, r_Z vs T1 = 0.5]")
    print("  leg                    r_Z(core, NO bound)  r_Z(whole-cell KUBC = the "
          "UPPER bound)  macro-side?")
    for r in f5["rows"]:
        print("  %-22s %-20.5f %-32.5f %s" % (
            r["leg_782"], r["r_Z_here_CORE_estimator_NO_BOUND_STATUS"],
            r["r_Z_here_WHOLE_CELL_KUBC_the_actual_UPPER_bound"],
            "YES" if r["macro_side_BOUND_ROBUST_on_the_bound_carrying_KUBC"] else "NO"))
    print("  macro-side legs: %d of %d on the CORE estimator -> %d of %d on the "
          "BOUND-CARRYING measure" % (
              f5["n_macro_side_on_the_CORE_estimator"], f5["n_legs"],
              f5["n_macro_side_BOUND_ROBUST_on_the_bound_carrying_WHOLE_CELL_KUBC"],
              f5["n_legs"]))
    print("\n[SUPPLEMENTARY anisotropy — uncaged cold reference, both BCs]")
    for L, meta in sorted(out["uncaged_reference_by_L"].items()):
        a = meta["SUPPLEMENTARY_anisotropy_NOT_FROZEN"]
        print("  L=%-3s C44 %.5f/%.5f  C' %.5f/%.5f  Zener A %.4f/%.4f  "
              "M[111] %.5f/%.5f  C11 %.5f/%.5f  (SUBC/KUBC)" % (
                  L, a["C44_SUBC"], a["C44_KUBC"], a["Cprime_SUBC"], a["Cprime_KUBC"],
                  a["zener_A_SUBC"], a["zener_A_KUBC"], a["M_111_SUBC"], a["M_111_KUBC"],
                  a["C11_true_SUBC"], a["C11_true_KUBC"]))
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
