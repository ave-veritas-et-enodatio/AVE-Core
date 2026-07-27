#!/usr/bin/env python3
"""VESSEL-STATE RVE BENCH — the walk-1 instrument (#792-extends-#782).

Does the GROWN vessel-state shell BRIDGE the load path (HARD) or BOTTLENECK it
(SOFT) — or read NULL / DISCORDANT / MARGINAL / UNDETERMINED / (iv)-ANOMALY?

Prereg (FROZEN, the contract this driver executes MECHANICALLY):
    research/2026-07-22_vessel-state-rve_prereg-FROZEN.md   (REVISION 3)

★Extends the merged #782 RVE aggregation bench (Rule-14 reuse of its KUBC static-
 homogenization scaffold, its Lamé gate, its STOP-gate, its RVE-size/determinism
 gates) — but SWAPS the linear #782 primitive for a STATE-DEPENDENT (geometric-
 stiffness) operator and the verdict frame from painted-pre-stress isotropic
 classes to a GROWN anisotropic vessel state read by small-signal tangent response.

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-FIRST SECTOR HEADER (fired before any standard-physics term; prereg §0)
═══════════════════════════════════════════════════════════════════════════════
  SECTOR : A1 bulk/compression (K_eff, mass/dilatation) AND T2 shear (G_eff).
           The k_a-only bulk-only wall is the verdict wall; SYMMETRIC a control.
           Sector-ownership NOT cross-wired (A1 owns dilatation; T2 owns shear;
           the (2,3) Cosserat winding owns charge/spin — untouched here).
  REGIME : Regime-I cold-linear STATIC constitutive response, read as a SMALL-
           SIGNAL TANGENT about a GROWN finite-pre-stress operating point through
           a STATE-DEPENDENT operator. NO drive, NO lock-in, NO dissipative port
           (Ax3-lossless-reactive).
  PHASE  : Grown pressure-vessel shells — hoop bonds TENSION (k_shear,eff
           stiffened), radial bonds COMPRESSION (softened toward buckling), with
           T(r) EMERGENT from the relaxed nonlinear equilibrium and the remap
           term T(u)/l re-evaluated LIVE inside the operator.
  COORDS : real-space small-signal tangent moduli (K_tan/K_0, K(eps_bias)) +
           impedance plane (r_Z = Z_bulk,eff/Z_0), the ρ-side MEASURED (Protocol
           E). A46-clean: matched to the corpus's real-space constitutive claim.
  CLASS  : lattice-derived static homogenization + relaxed-equilibrium growth
           through the state-dependent operator. α-CLEAN. Every VALUE a
           dimensionless RATIO. ρ*=9.77337 is [import] (ν_Hill=2/7, N_NU); the
           imposed source amplitude p_0 / A_yield_scale are [engineering-choice].

★THE S(A(u)) DECISION (frozen, prereg §0): S-grade IMPOSED (Eulerian, static);
 geometric-tension T(u) LIVE. A live kernel S(A(u)) is a field-generated co-moving
 grade = self-binding = INFEASIBLE on the lossless engine (β-scoping absence-3;
 keystone-energize-LOCK negative). The genuine nonlinearity is carried ENTIRELY by
 the LIVE geometric term T(u)/l = k_a·ε_axial(u) (the #779 remap; hostable on the
 lossless engine — geometric/stress stiffness, no dissipation, no self-binding).

★THE CARVE (mandatory disclosure — every output carries both strings, prereg §1):
  grade-frame: Eulerian, imposed (not self-bound; the engine hosts no
               field-generated co-moving grade)
  source imposed (radiation-stress surrogate body-force ∝⟨A²⟩); stress state
               emergent through the nonlinear force balance

ENGINE BYTE-UNTOUCHED: imports ave.core.* / the #782 driver scaffold read-only.
Driver-level only; no src/ave edit.

Run: PYTHONPATH=src python3 research/drivers/vessel_state_rve.py --legs 0
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

# ── Rule-14 reuse of the VALIDATED #770/#775/#782 pipeline (read-only imports) ──
_DRIVERS = Path(__file__).resolve().parent
sys.path.insert(0, str(_DRIVERS))
from constituent_cage_ensemble import (  # noqa: E402
    build_finite_srs, bond_tensors, forces, node_dilatation,
    run_c2_speeds, omega_max_cold, RHO_STAR, K_S,
)
from rve_aggregation_bench import (  # noqa: E402
    boundary_mask, affine_field, jacobi_diag, cage_bond_stiffness,
    strain_mode, cubic_cage_centers, packing_fraction,
    coated_inclusion_fraction, lame_gate, uncaged_reference,
    measure_modulus_ratio, core_energy, elastic_energy,
    rho_ratio, z_over_z0, BW, CAGE_W,
)
from ave.core.chiral_lattice import _SRS_NN  # noqa: E402  (bond rest length)

# ═════════════════════════════════════════════════════════════════════════════
# FROZEN bench constants (prereg §1/§2/§3/§5/§6)
# ═════════════════════════════════════════════════════════════════════════════
K_A = float(RHO_STAR)          # axial (compression) bond stiffness — [import] ν_Hill=2/7
KS0 = float(K_S)               # cold transverse (shear) bond stiffness = 1.0
A_YIELD = 1.0                  # prereg §1 WARN(ii): native kernel/strain units, #782 inherit
ELL = float(_SRS_NN)           # bond rest length (all bonds equal on the srs net)

# Newton / self-consistent solve (prereg §2, FROZEN)
INNER_CG_TOL = 1e-10           # inner CG relative residual
INNER_CG_MAX = 4000            # inner CG iteration cap
OUTER_SC_TOL = 1e-6            # outer self-consistency  max_bond |Δk_shear,eff|/k_s
OUTER_RES_TOL = 1e-8           # outer nonlinear residual ||K(u)u - b||/||b||
OUTER_MAX = 100                # outer iteration cap
# Armijo backtracking line-search fallback (prereg §2, FROZEN)
LS_RHO = 0.5                   # backtracking factor ρ_ls
LS_C1 = 1e-4                   # Armijo sufficient-decrease constant c_1
LS_MAX_BACKTRACK = 20          # max backtracks before STALLED

# Amplitude gate (prereg §3, FROZEN)
EPS_PROBE_BASE = 1e-4
AMP_SCAN = (1e-5, 1e-4, 1e-3, 1e-2)     # ≥3 decades, both signs
AMP_SPREAD_THRESH = 0.05
A_SIGN_THRESH = 0.10
INNER_CG_TOL_TIGHT = 1e-11              # residual-tightening robustness guard (10×)
A_SIGN_ROBUST_BAND = 0.10

# Verdict bins (prereg §6, FROZEN)
DELTA_RZ = 0.05                # r_Z straddle band half-width
LIFT_L2 = 1.2                  # lift band edges
LIFT_L3 = 1.5

# C-V profiling (prereg §5, FROZEN)
EPS_BIAS_MAX = 3e-3
N_BIAS = 11
ASYMMETRY_THRESH = 0.15

# minimum SPD guard for the transverse stiffness inside a solve (a bond at/through
# buckling is caught by grown_bonds_positive; the solve floor keeps CG well-posed
# WITHOUT masking the crossing — the raw (unfloored) k_shear,eff is what the STOP
# criterion and every observable read).
KSE_SOLVE_FLOOR = 1e-6

# ── Protocol E — long-λ compression ToF, ρ_eff MEASURED (prereg §4; PR#796 F2 repair) ──
# The shipped extraction was UNDER-GUARDED (no PML exclusion, slab-mean not density-peak,
# window ~12× the frozen formula, unfrozen argmax arrival, reactance-pair flag hardcoded).
# This block reimplements the frozen §4 sub-requirements AS WRITTEN: PML/window boundary-
# cell exclusion, density-peak (top-K |field|²) monitor sampling, the FROZEN reflection-free
# window t_end ≤ 0.9·(L/2−r_meas)/c_P, a FROZEN two-monitor cross-correlation arrival
# criterion (the "first-arrival group speed", operationalized + documented), a REAL
# reactance-pair flag, and BOTH L∈{32,48}.
PE_PML_THICKNESS = 2.0     # boundary-cell exclusion margin (≥ KUBC bw=1.5), lattice units
PE_R1_FRAC = 0.07          # near density-peak monitor distance from centered source (·Lx)
PE_R2_FRAC = 0.13          # far  density-peak monitor distance from centered source (·Lx)
PE_W_FRAC = 0.06           # compression-pulse Gaussian width (·Lx). ★DISCLOSED: on L∈{32,48}
#                            w≈1.9–2.9 ≲ cage radius 2.2 ⇒ k·r_core≈2–4, LONG-λ MARGINAL —
#                            the grown cage medium is a locally-resonant scatterer, so the
#                            ToF c_eff is EXTRACTION-DEPENDENT (see protocol_E method band).
PE_TOPK = 48               # density-peak sampling: top-K |field|² nodes per monitor slab
PE_CFL = 0.2               # velocity-Verlet CFL
PE_SC_MAXIT = 4            # self-consistent launch-speed iterations (coherent forward eigenmode)
PE_SC_TOL = 0.01           # SC convergence: |Δc|/c ≤ 1%
PE_WINDOW_SAFETY = 0.9     # frozen reflection-free window safety factor
PE_AMP = 1e-3              # linear-regime pulse amplitude
# ToF-medium grow: a fail-fast capped grow (the ToF medium is a homogenized TANGENT operator,
# insensitive to the last outer/inner digits — verified: L=32 capped min_kse=0.34722 IDENTICAL
# to the full frozen 1e-10/100-outer solve; the VERDICT K_tan solve keeps the frozen 1e-10).
PE_GROW_OUTER = 12
PE_GROW_INNER_TOL = 1e-6

# ── yield_saturated ascending-p0 scan (prereg §1/§6; PR#796 F11/F3/F8/F9 repair) ──
# The shipped scan stopped at an UNDISCLOSED hard-coded p0=0.06 ceiling with every point
# STABLE, then banked yield_saturated as an *extrapolated* NULL. This grid EXTENDS past the
# ceiling to OBSERVE the terminal buckling onset. ALL yield-scan solves run at a fail-fast cap
# (F9: the cap applies to EVERY yield-scan solve, not only buckled ones).
YIELD_SCAN_P0 = (0.005, 0.01, 0.02, 0.03, 0.04, 0.05, 0.055, 0.06,
                 0.062, 0.064, 0.066, 0.068, 0.07, 0.08)
YIELD_OUTER_CAP = 8
YIELD_INNER_CAP = 800


# ═════════════════════════════════════════════════════════════════════════════
# ★THE STATE-DEPENDENT OPERATOR (prereg §2 — the F2 root; what makes it NONLINEAR)
# ═════════════════════════════════════════════════════════════════════════════
def bond_axial_strain(u, bi, bj, dhat):
    """ε_axial,b(u) = [d̂_b·(u_i − u_j)]/ℓ_b — the CURRENT axial strain per bond."""
    return np.einsum("bi,bi->b", u[bi] - u[bj], dhat) / ELL


def k_shear_eff(eps_axial, k_s_cold, k_a=K_A):
    """LIVE geometric-stiffness remap k_shear,eff(u) = k_s + k_a·ε_axial(u)
    (axiom-register.md:193; T(u)/ℓ = k_a·ε_axial with the LOCAL axial stiffness k_a).
    Tension (ε>0) STIFFENS, compression (ε<0) SOFTENS toward buckling. `k_s_cold` is
    the per-bond cold transverse stiffness (KS0 everywhere, OR the #782 rail grade for
    the CONTROL arms); `k_a` the local axial stiffness (railed on cage shells)."""
    return k_s_cold + k_a * eps_axial


def bond_tension_remap(eps_axial, k_a=K_A):
    """T(u)/ℓ = k_a·ε_axial — the remap term that shifts k_shear,eff. This is the
    'T' the STOP criterion `grown_tension_nonzero: max_r |T(r)| ≥ 0.05·k_a·A_yield`
    reads (the tension CONTRIBUTION to the stiffness; DISCLOSED choice — see result
    doc deviations: T is taken as the remap term k_a·ε_axial that the operator
    actually sees, not the un-normalized axial force k_a·ε_axial·ℓ)."""
    return k_a * eps_axial


def state_operator(u, bi, bj, dhat, k_s_cold, k_a_bond=None, floor=KSE_SOLVE_FLOOR):
    """Build Φ_eff(u)_b = k_a·(d̂⊗d̂) + k_shear,eff(u)_b·(I − d̂⊗d̂) at the current u.
    Returns (Phi, kse_raw, eps_axial) — kse_raw is the UNFLOORED k_shear,eff (what the
    buckling STOP reads); Phi uses max(kse_raw, floor) so the inner CG stays well-posed.
    `k_a_bond` defaults to the uniform axial stiffness K_A (per-bond array allowed for
    the #782 rail/rigid cage shells); the remap uses the SAME local k_a."""
    eps = bond_axial_strain(u, bi, bj, dhat)
    ka = K_A if k_a_bond is None else k_a_bond
    kse_raw = k_shear_eff(eps, k_s_cold, ka)
    Phi = bond_tensors(dhat, ka, np.maximum(kse_raw, floor))
    return Phi, kse_raw, eps


# ═════════════════════════════════════════════════════════════════════════════
# ★THE NEWTON / SELF-CONSISTENT SOLVE (prereg §2 — outer re-eval of T(u), inner CG)
# ═════════════════════════════════════════════════════════════════════════════
def _cg_interior(applyK, rhs, x0, Mi, tol, itmax):
    """Matrix-free Jacobi-preconditioned CG for K_II x = rhs. Returns (x, rel_res, it)."""
    bn = np.linalg.norm(rhs) + 1e-30
    x = x0.copy()
    r = rhs - applyK(x)
    z = Mi * r
    p = z.copy()
    rz = float(np.sum(r * z))
    it = 0
    res = np.linalg.norm(r) / bn
    while res > tol and it < itmax:
        Ap = applyK(p)
        alpha = rz / (float(np.sum(p * Ap)) + 1e-30)
        x += alpha * p
        r -= alpha * Ap
        z = Mi * r
        rz_new = float(np.sum(r * z))
        beta = rz_new / (rz + 1e-30)
        p = z + beta * p
        rz = rz_new
        it += 1
        res = np.linalg.norm(r) / bn
    return x, float(res), it


def solve_state_dependent(geom, free, u_bc, b_src, k_s_cold, k_a_bond=K_A,
                          inner_tol=INNER_CG_TOL, inner_max=INNER_CG_MAX,
                          outer_max=OUTER_MAX, u_init=None, ls_fallback=True):
    """Solve the NONLINEAR KUBC balance K(u)·u = b_src with the state-dependent
    operator (prereg §2). Boundary pinned to u_bc; interior additionally loaded by the
    body-force source b_src. Self-consistent SECANT outer loop (re-evaluate T(u) each
    outer step; inner Jacobi-CG on the current tangent operator). Armijo-backtracking
    damped line-search fallback (ρ_ls=0.5, c_1=1e-4, ≤20 backtracks) when the secant
    stalls — STALLED routes to STOP (converged=False), NOT silently accepted.

    Returns dict: u, kse_raw (unfloored k_shear,eff), eps_axial, converged (§2 dual
    tolerance), inner_res_last, inner_it_last, outer_it, nlres, dsc, stalled.
    """
    pos, bi, bj, dhat, mid = geom
    N = pos.shape[0]
    idx = np.where(free)[0]
    u = np.zeros((N, 3)) if u_init is None else u_init.copy()
    u[~free] = u_bc[~free]                       # pin boundary
    if u_init is None:
        u[free] = 0.0
    bsrc_free = b_src[idx]

    def merit(uu, Phi):
        # ½‖K(u)u − b‖² on the interior (the frozen line-search merit)
        resid = (-forces(uu, Phi, bi, bj, N)[idx] - bsrc_free)
        return 0.5 * float(np.sum(resid ** 2))

    kse_prev = k_shear_eff(bond_axial_strain(u, bi, bj, dhat), k_s_cold)
    nlres = np.inf
    dsc = np.inf
    inner_res = np.nan
    inner_it = 0
    stalled = False
    outer_it = 0
    for it in range(outer_max):
        outer_it = it + 1
        Phi, kse_raw, eps = state_operator(u, bi, bj, dhat, k_s_cold, k_a_bond)
        # RHS = b_src_I − K_IB u_B = b_src_I + forces(u_bc, Phi)_I  (u_bc free part = 0)
        u_bc_only = np.zeros((N, 3))
        u_bc_only[~free] = u_bc[~free]
        rhs = bsrc_free + forces(u_bc_only, Phi, bi, bj, N)[idx]
        diag = jacobi_diag(dhat, k_a_bond if np.ndim(k_a_bond) else np.full(bi.shape[0], K_A),
                           np.maximum(kse_raw, KSE_SOLVE_FLOOR), bi, bj, N)
        Mi = 1.0 / np.maximum(diag[free], 1e-30)

        def applyK(wf):
            w = np.zeros((N, 3))
            w[idx] = wf
            return (-forces(w, Phi, bi, bj, N))[idx]

        x_new, inner_res, inner_it = _cg_interior(applyK, rhs, u[idx], Mi, inner_tol, inner_max)

        # candidate full secant step
        u_cand = u.copy()
        u_cand[idx] = x_new
        m_old = merit(u, Phi)
        m_new = merit(u_cand, state_operator(u_cand, bi, bj, dhat, k_s_cold, k_a_bond)[0])
        alpha = 1.0
        if ls_fallback and m_new > m_old * (1.0 - LS_C1) and it > 0:
            # Armijo backtracking on the secant increment direction (frozen params)
            step = x_new - u[idx]
            bt = 0
            accepted = False
            while bt < LS_MAX_BACKTRACK:
                alpha *= LS_RHO
                u_try = u.copy()
                u_try[idx] = u[idx] + alpha * step
                Phi_try = state_operator(u_try, bi, bj, dhat, k_s_cold, k_a_bond)[0]
                if merit(u_try, Phi_try) <= m_old * (1.0 - LS_C1 * alpha):
                    u_cand = u_try
                    accepted = True
                    break
                bt += 1
            if not accepted:
                stalled = True     # 20-backtrack cap hit without sufficient decrease
        u = u_cand

        Phi2, kse2, eps2 = state_operator(u, bi, bj, dhat, k_s_cold, k_a_bond)
        rhs2_norm = np.linalg.norm(bsrc_free + forces(u_bc_only, Phi2, bi, bj, N)[idx]) + 1e-30
        nlres = np.linalg.norm(-forces(u, Phi2, bi, bj, N)[idx] - bsrc_free) / rhs2_norm
        dsc = float(np.max(np.abs(kse2 - kse_prev)) / KS0)
        kse_prev = kse2
        if stalled:
            break
        if it > 0 and dsc <= OUTER_SC_TOL and nlres <= OUTER_RES_TOL:
            break

    _, kse_raw, eps = state_operator(u, bi, bj, dhat, k_s_cold, k_a_bond)
    converged = bool((not stalled) and dsc <= OUTER_SC_TOL and nlres <= OUTER_RES_TOL
                     and inner_res <= inner_tol * 10)
    return {
        "u": u, "kse_raw": kse_raw, "eps_axial": eps,
        "converged": converged, "stalled": bool(stalled),
        "inner_res_last": float(inner_res), "inner_it_last": int(inner_it),
        "outer_it": int(outer_it), "nlres": float(nlres), "dsc": float(dsc),
    }


# ═════════════════════════════════════════════════════════════════════════════
# ★THE IMPOSED SOURCE (prereg §1 — radiation-stress surrogate body-force ∝⟨A²⟩)
# ═════════════════════════════════════════════════════════════════════════════
def radiation_source(pos, centers, p0, sigma=2.5, r_core=None):
    """b_source(r) = p_0·f(r)·r̂ — an OUTWARD ponderomotive pressure ∝⟨A²⟩ on each
    core (the #767 object; equivalently a frozen radial eigenstrain). f(r) a Gaussian
    core bump about each center; net force zero by radial symmetry (no rigid drift).
    Returns (N,3) body force."""
    b = np.zeros_like(pos)
    for c in centers:
        rel = pos - np.asarray(c, float)
        rr = np.linalg.norm(rel, axis=1)
        rh = rel / (rr[:, None] + 1e-30)
        f = np.exp(-(rr ** 2) / (2.0 * sigma ** 2))
        if r_core is not None:
            f = np.where(rr <= r_core, f, 0.0)
        b += p0 * f[:, None] * rh
    return b


def shell_band_mask(pos, mid, centers, r_lo, r_hi, on_nodes=False):
    """Bonds (midpoints) — or nodes — whose nearest-center radius lies in [r_lo, r_hi]
    (the 'shell band' the SELFTEST-(iii) near-buckling fraction is measured over)."""
    ref = pos if on_nodes else mid
    rmin = np.full(ref.shape[0], np.inf)
    for c in centers:
        rmin = np.minimum(rmin, np.linalg.norm(ref - np.asarray(c, float), axis=1))
    return (rmin >= r_lo) & (rmin < r_hi)


# ═════════════════════════════════════════════════════════════════════════════
# ★THE GROW STEP + the THREE numbered STOP criteria (prereg §1, FROZEN)
# ═════════════════════════════════════════════════════════════════════════════
def grow_vessel(geom, free, centers, p0, k_s_cold=None, sigma=2.5, r_core=None,
                inner_tol=INNER_CG_TOL):
    """`.OP`: grow the vessel state (imposed radiation-stress source + nonlinear relax
    to the static force-balance equilibrium u_0). Evaluate the THREE numbered STOP
    criteria (prereg §1):
      grown_CG_converged   — the §2 dual tolerance met within the outer cap
      grown_tension_nonzero — max_r |T(r)| ≥ 0.05·k_a·A_yield  (T = k_a·ε_axial remap term)
      grown_bonds_positive  — min_bond k_shear,eff(u_0) > 0    (no bond crossed buckling)
    grown_equilibrium_exists = the conjunction.
    """
    pos, bi, bj, dhat, mid = geom
    N = pos.shape[0]
    if k_s_cold is None:
        k_s_cold = np.full(bi.shape[0], KS0)
    b_src = radiation_source(pos, centers, p0, sigma, r_core)
    u_bc = np.zeros((N, 3))                       # boundary pinned to 0 (no macro strain)
    sol = solve_state_dependent(geom, free, u_bc, b_src, k_s_cold, inner_tol=inner_tol)
    T = bond_tension_remap(sol["eps_axial"])      # = k_a·ε_axial, the remap term
    max_abs_T = float(np.max(np.abs(T)))
    min_kse = float(sol["kse_raw"].min())
    tension_thresh = 0.05 * K_A * A_YIELD
    grown_CG_converged = bool(sol["converged"])
    grown_tension_nonzero = bool(max_abs_T >= tension_thresh)
    grown_bonds_positive = bool(min_kse > 0.0)
    exists = bool(grown_CG_converged and grown_tension_nonzero and grown_bonds_positive)
    return {
        "u0": sol["u"], "b_src": b_src, "sol": sol, "T": T,
        "p0": p0, "centers_n": len(centers),
        "max_abs_T": max_abs_T, "tension_threshold_0p05kaAyield": tension_thresh,
        "min_kse": min_kse, "eps_min": float(sol["eps_axial"].min()),
        "eps_max": float(sol["eps_axial"].max()),
        "grown_CG_converged": grown_CG_converged,
        "grown_tension_nonzero": grown_tension_nonzero,
        "grown_bonds_positive": grown_bonds_positive,
        "grown_equilibrium_exists": exists,
        "outer_it": sol["outer_it"], "nlres": sol["nlres"],
        "inner_it_last": sol["inner_it_last"],
    }


# ═════════════════════════════════════════════════════════════════════════════
# ★THE FIVE-POINT TANGENT PROBE + the CENTRAL / ONE-SIDED second differences (§2)
# ═════════════════════════════════════════════════════════════════════════════
def _probe_energy(geom, free, u0, b_src, k_s_cold, xc, half, E, inner_tol, k_a_bond=K_A):
    """Impose macro strain E on the boundary (superposed on u0), re-relax the interior
    through the state-dependent operator with the source, return (U_core, converged)."""
    pos, bi, bj, dhat, mid = geom
    N = pos.shape[0]
    u_bc = np.zeros((N, 3))
    u_bc[~free] = u0[~free] + affine_field(pos[~free], xc, E)
    sol = solve_state_dependent(geom, free, u_bc, b_src, k_s_cold, k_a_bond=k_a_bond,
                                inner_tol=inner_tol, u_init=u0)
    Phi = state_operator(sol["u"], bi, bj, dhat, k_s_cold, k_a_bond)[0]
    Uc = core_energy(sol["u"], Phi, bi, bj, mid, xc, half)
    return Uc, bool(sol["converged"])


def tangent_probe(geom, free, u0, b_src, k_s_cold, mode, eps_probe, xc, half,
                  inner_tol=INNER_CG_TOL, U0_core=None, k_a_bond=K_A):
    """FIVE-POINT re-relaxation set {u_0, u_0±δ, u_0±2δ} at one probe amplitude
    (prereg §2, BLOCKER-1 stencil split). Returns the CENTRAL second difference
    (JOB 1 — outcome-(i) verdict observable) and the two ONE-SIDED second differences
    K_tan_plus/K_tan_minus (JOB 2 — sign-resolved gate observables), each ÷ε² (V_core
    drops out in every frozen metric)."""
    Ep = strain_mode(mode, eps_probe)
    E2 = strain_mode(mode, 2.0 * eps_probe)
    conv = []
    if U0_core is None:
        U0_core, c0 = _probe_energy(geom, free, u0, b_src, k_s_cold, xc, half,
                                    strain_mode(mode, 0.0), inner_tol, k_a_bond)
        conv.append(c0)
    Up, cp = _probe_energy(geom, free, u0, b_src, k_s_cold, xc, half, Ep, inner_tol, k_a_bond)
    Um, cm = _probe_energy(geom, free, u0, b_src, k_s_cold, xc, half, -Ep, inner_tol, k_a_bond)
    Up2, cp2 = _probe_energy(geom, free, u0, b_src, k_s_cold, xc, half, E2, inner_tol, k_a_bond)
    Um2, cm2 = _probe_energy(geom, free, u0, b_src, k_s_cold, xc, half, -E2, inner_tol, k_a_bond)
    conv += [cp, cm, cp2, cm2]
    e2 = eps_probe ** 2
    k_central = (Up + Um - 2.0 * U0_core) / e2
    k_plus = (Up2 - 2.0 * Up + U0_core) / e2      # curvature centered at u_0+δE (STRETCH)
    k_minus = (Um2 - 2.0 * Um + U0_core) / e2     # curvature centered at u_0−δE (SQUEEZE)
    return {
        "eps_probe": eps_probe, "mode": mode,
        "U0": U0_core, "U_plus": Up, "U_minus": Um, "U_plus2": Up2, "U_minus2": Um2,
        "k_tan_central": float(k_central), "k_tan_plus": float(k_plus),
        "k_tan_minus": float(k_minus), "all_converged": bool(all(conv)),
    }


def cold_central_modulus(geom, free, mode, eps_probe, xc, half):
    """K_0 central-difference reference: cold uncaged lattice, NO source, the SAME
    central second difference (prereg §2 JOB 1 normalizer). Cold U(0)=0."""
    pos = geom[0]
    N = pos.shape[0]
    kzero = np.full(geom[1].shape[0], KS0)
    zero = np.zeros((N, 3))
    Up, _ = _probe_energy(geom, free, zero, zero, kzero, xc, half,
                          strain_mode(mode, eps_probe), INNER_CG_TOL)
    Um, _ = _probe_energy(geom, free, zero, zero, kzero, xc, half,
                          strain_mode(mode, -eps_probe), INNER_CG_TOL)
    return (Up + Um) / (eps_probe ** 2)           # U0_cold = 0


# ═════════════════════════════════════════════════════════════════════════════
# ★THE FOUR-OUTCOME SIGN-RESOLVED AMPLITUDE GATE (prereg §3, FROZEN thresholds)
# ═════════════════════════════════════════════════════════════════════════════
def classify_amplitude_outcome(amp_spread_plus, amp_spread_minus, A_sign,
                               k_plus_emax, k_minus_emax):
    """The single frozen classifier (prereg §3; used by BOTH the self-tests and the
    verdict — reconcile-don't-declare). Returns one of 'i'|'ii'|'iii'|'iv'."""
    not_i = (amp_spread_plus > AMP_SPREAD_THRESH) or (amp_spread_minus > AMP_SPREAD_THRESH)
    if not not_i:
        return "i"                                  # clean both signs
    if A_sign <= A_SIGN_THRESH:
        return "ii"                                 # symmetric drift = artifact
    # A_sign > 0.10 forces k_plus ≠ k_minus → clean (iii)/(iv) split
    return "iii" if (k_minus_emax < k_plus_emax) else "iv"


def amplitude_gate(geom, free, u0, b_src, k_s_cold, mode, xc, half,
                   op_converged=True, robustness=True, scan=AMP_SCAN,
                   inner_tol=INNER_CG_TOL, label="", k_a_bond=K_A):
    """Scan ε_probe over ≥3 decades both signs; read K_tan_plus/K_tan_minus (gate) +
    K_tan_central (verdict) by the §2 five-point formulas; compute the frozen metrics
    amp_spread(±)/A_sign/A_dir; apply the CG-convergence PRECONDITION + the residual-
    tightening ROBUSTNESS GUARD; classify (i)/(ii)/(iii)/(iv) via the frozen thresholds."""
    pos, bi, bj, dhat, mid = geom
    Phi0 = state_operator(u0, bi, bj, dhat, k_s_cold, k_a_bond)[0]
    U0_core = core_energy(u0, Phi0, bi, bj, mid, xc, half)
    legs = []
    for e in scan:
        pr = tangent_probe(geom, free, u0, b_src, k_s_cold, mode, e, xc, half,
                           inner_tol=inner_tol, U0_core=U0_core, k_a_bond=k_a_bond)
        legs.append(pr)
    kc0 = legs[0]["k_tan_central"]                   # K_tan_central(ε→0), frozen normalizer
    kc0 = kc0 if abs(kc0) > 1e-300 else 1e-300
    kp = [L["k_tan_plus"] for L in legs]
    km = [L["k_tan_minus"] for L in legs]
    amp_spread_plus = (max(kp) - min(kp)) / kc0
    amp_spread_minus = (max(km) - min(km)) / kc0
    kp_emax, km_emax = legs[-1]["k_tan_plus"], legs[-1]["k_tan_minus"]
    A_sign = abs(kp_emax - km_emax) / kc0
    A_dir = int(np.sign(kp_emax - km_emax))
    all_scan_legs_converged = bool(op_converged and all(L["all_converged"] for L in legs))

    # residual-tightening robustness guard: re-run ε_max both signs at 10× tighter tol
    robust = None
    A_sign_tight = None
    if robustness:
        pr_t = tangent_probe(geom, free, u0, b_src, k_s_cold, mode, scan[-1], xc, half,
                             inner_tol=INNER_CG_TOL_TIGHT, U0_core=U0_core, k_a_bond=k_a_bond)
        A_sign_tight = abs(pr_t["k_tan_plus"] - pr_t["k_tan_minus"]) / kc0
        denom = A_sign if A_sign > 1e-30 else 1e-30
        robust = bool(abs(A_sign_tight - A_sign) / denom <= A_SIGN_ROBUST_BAND)

    outcome = classify_amplitude_outcome(amp_spread_plus, amp_spread_minus, A_sign,
                                         kp_emax, km_emax)
    return {
        "label": label, "mode": mode,
        "scan": [{"eps": L["eps_probe"], "k_tan_central": L["k_tan_central"],
                  "k_tan_plus": L["k_tan_plus"], "k_tan_minus": L["k_tan_minus"],
                  "all_converged": L["all_converged"]} for L in legs],
        "k_tan_central_eps0": float(kc0),
        "amp_spread_plus": float(amp_spread_plus),
        "amp_spread_minus": float(amp_spread_minus),
        "A_sign": float(A_sign), "A_dir": A_dir,
        "k_tan_plus_emax": float(kp_emax), "k_tan_minus_emax": float(km_emax),
        "all_scan_legs_converged": all_scan_legs_converged,
        "residual_tightening_robust": robust, "A_sign_tight": A_sign_tight,
        "outcome": outcome,
    }


# ═════════════════════════════════════════════════════════════════════════════
# ★§3B — THE GATE-FIREABILITY ACCEPTANCE SELF-TESTS (mandatory, FROZEN; the F2 repair)
# ═════════════════════════════════════════════════════════════════════════════
def selftest_ii(geom, free, centers, xc, half, p0, loose_tol=1e-3):
    """SELFTEST-(ii): a deliberately under-converged solve FORCES the (ii) ARTIFACT and
    is diagnosed as convergence-caused (prereg §3B dual frozen assertion). Grow + gate at
    a LOOSE inner CG tol (under-converges symmetrically) AND at the tight frozen tol.
    Acceptance:  amp_spread(loose) > 0.05 in at least one sign  AND
                 amp_spread(tight 1e-10) <= 0.05 for both signs  AND
                 (A_sign(loose) <= 0.10  OR  all_scan_legs_converged = False)."""
    grown = grow_vessel(geom, free, centers, p0, inner_tol=INNER_CG_TOL)
    u0, b_src = grown["u0"], grown["b_src"]
    k_s_cold = np.full(geom[1].shape[0], KS0)
    loose = amplitude_gate(geom, free, u0, b_src, k_s_cold, "hydro", xc, half,
                           op_converged=grown["grown_CG_converged"],
                           robustness=False, inner_tol=loose_tol, label="selftest_ii_loose")
    tight = amplitude_gate(geom, free, u0, b_src, k_s_cold, "hydro", xc, half,
                           op_converged=grown["grown_CG_converged"],
                           robustness=False, inner_tol=INNER_CG_TOL, label="selftest_ii_tight")
    loose_fires = (loose["amp_spread_plus"] > AMP_SPREAD_THRESH
                   or loose["amp_spread_minus"] > AMP_SPREAD_THRESH)
    tight_clean = (tight["amp_spread_plus"] <= AMP_SPREAD_THRESH
                   and tight["amp_spread_minus"] <= AMP_SPREAD_THRESH)
    diagnosed = (loose["A_sign"] <= A_SIGN_THRESH
                 or not loose["all_scan_legs_converged"])
    fires = bool(loose_fires and tight_clean and diagnosed)
    return {
        "loose_tol": loose_tol, "p0": p0,
        "loose_amp_spread_plus": loose["amp_spread_plus"],
        "loose_amp_spread_minus": loose["amp_spread_minus"],
        "loose_A_sign": loose["A_sign"],
        "loose_all_scan_legs_converged": loose["all_scan_legs_converged"],
        "tight_amp_spread_plus": tight["amp_spread_plus"],
        "tight_amp_spread_minus": tight["amp_spread_minus"],
        "loose_fires_artifact": bool(loose_fires),
        "tight_removes_artifact": bool(tight_clean),
        "diagnosed_convergence_caused": bool(diagnosed),
        "SELFTEST_ii_FIRES": fires,
    }


def selftest_iii(geom, free, centers, xc, half, p0, sigma, r_core,
                 shell_lo, shell_hi):
    """SELFTEST-(iii): a near-buckling SHELL-BOND FRACTION FORCES COMPRESSIVE MARGINALITY
    in the AGGREGATE (prereg §3B forcing repair). Grow a state with the source tuned so
    ≥50% of shell-band bonds sit at k_shear,eff(u_0) ≤ 0.2·k_s (near buckling). Acceptance:
    the gate returns outcome (iii): amp_spread > 0.05 in at least one sign AND A_sign > 0.10
    AND K_tan_minus(ε_max) < K_tan_plus(ε_max), converged+robust."""
    pos, bi, bj, dhat, mid = geom
    grown = grow_vessel(geom, free, centers, p0, sigma=sigma, r_core=r_core,
                        inner_tol=INNER_CG_TOL)
    u0, b_src, kse = grown["u0"], grown["b_src"], grown["sol"]["kse_raw"]
    band = shell_band_mask(pos, mid, centers, shell_lo, shell_hi, on_nodes=False)
    n_band = int(band.sum())
    near_buckling = (kse <= 0.2 * KS0)
    frac_near = float((near_buckling & band).sum() / max(n_band, 1))
    k_s_cold = np.full(bi.shape[0], KS0)
    gate = amplitude_gate(geom, free, u0, b_src, k_s_cold, "hydro", xc, half,
                          op_converged=grown["grown_CG_converged"],
                          robustness=True, label="selftest_iii")
    fires = bool(gate["outcome"] == "iii"
                 and gate["all_scan_legs_converged"]
                 and gate["residual_tightening_robust"])
    return {
        "p0": p0, "sigma": sigma, "r_core": r_core,
        "shell_band": [shell_lo, shell_hi], "n_band_bonds": n_band,
        "frac_shell_bonds_near_buckling_le_0p2ks": frac_near,
        "frac_target_ge_0p5": bool(frac_near >= 0.5),
        "grown_bonds_positive": grown["grown_bonds_positive"],
        "min_kse": grown["min_kse"],
        "gate_outcome": gate["outcome"], "A_sign": gate["A_sign"],
        "amp_spread_plus": gate["amp_spread_plus"],
        "amp_spread_minus": gate["amp_spread_minus"],
        "k_tan_plus_emax": gate["k_tan_plus_emax"],
        "k_tan_minus_emax": gate["k_tan_minus_emax"],
        "all_scan_legs_converged": gate["all_scan_legs_converged"],
        "residual_tightening_robust": gate["residual_tightening_robust"],
        "SELFTEST_iii_FIRES": fires, "_gate": gate,
    }


# ═════════════════════════════════════════════════════════════════════════════
# FROZEN bench geometry + seed-budget (prereg §1/§6/§8; p_ref an [engineering-choice])
# ═════════════════════════════════════════════════════════════════════════════
# Verdict arm cage geometry — MATCHED to #782 φ_sf = 0.489 (route-A largest point).
PHI_SF_S = 4.5                 # cubic cage spacing (#782 route A)
PHI_SF_RCAGE = 2.2             # cage radius → φ = (4/3)π r³/s³ = 0.489
# Seed budget (§1): fixed_budget p_ref in the stable-vessel window (probe: tension@0.0147,
# buckling-edge≈0.030). p_ref chosen mid-window so the {0.25,0.5,1.0}·p_ref sweep spans it.
P_REF = 0.020                  # [engineering-choice], DISCLOSED; grade-frame Eulerian/imposed
P0_SWEEP_FRACS = (0.25, 0.5, 1.0)      # anti-seduction seed-independence (fixed_budget)
A_YIELD_SCALE_SWEEP = (0.9, 1.0, 1.1)  # yield_saturated-native reservoir knob (§1 F7)
SRC_SIGMA = 2.5                # source Gaussian width (single-core .OP)

# SELF-TEST calibration params (§3B; finalized from the design-time calibration run,
# banked in the result-doc Leg-0 section — set post-calibration below).
SELFTEST_II_LOOSE_TOL = 1e-3   # the FROZEN loose inner CG tol (§3B); forces the (ii) artifact
SELFTEST_II_P0 = 0.020
SELFTEST_III_P0 = 0.028        # near-buckling grown state (calibrated; min k_shear,eff≈0.054)
SELFTEST_III_SIGMA = 2.5
SELFTEST_III_SHELL = (0.0, 3.0)   # band the near-buckling bonds concentrate in (calibrated)


# ═════════════════════════════════════════════════════════════════════════════
# ★LEG 0 — gate-fireability self-tests + instrument validation (prereg exec order)
# ═════════════════════════════════════════════════════════════════════════════
def _geom_cache(Ls=(12, 16, 20)):
    return {L: build_finite_srs(L) for L in Ls}


def _setup(geom):
    pos = geom[0]
    xc = 0.5 * (pos.max(0) + pos.min(0))
    free = ~boundary_mask(pos, None)
    half = 0.25 * (pos.max(0) - pos.min(0)).mean()
    return xc, free, half


def leg0_selftests(cache):
    """LEG 0 — the mandatory gate-fireability self-tests (§3B). SELFTEST-(ii) AND
    SELFTEST-(iii) must FORCE their target outcomes, else the bench is VOID."""
    geom = cache[16]
    xc, free, half = _setup(geom)
    centers = [xc.copy()]
    st_ii = selftest_ii(geom, free, centers, xc, half, SELFTEST_II_P0,
                        loose_tol=SELFTEST_II_LOOSE_TOL)
    st_iii = selftest_iii(geom, free, centers, xc, half, SELFTEST_III_P0,
                          SELFTEST_III_SIGMA, None, *SELFTEST_III_SHELL)
    st_iii.pop("_gate", None)
    gate_pass = bool(st_ii["SELFTEST_ii_FIRES"] and st_iii["SELFTEST_iii_FIRES"])
    # ★PR#796 F4/F15: the calibration_disclosure is REGENERATED to match COMPUTED truth. The
    # shipped string falsely claimed 'the frozen 1e-3 did not perturb the tangent by >5%, tuned'
    # beside a measured spread of ~649 — the frozen 1e-3 was shipped UNCHANGED and FIRED the
    # artifact with NO tuning. (%% literal bug also fixed.)
    ii_loose_spread = max(st_ii["loose_amp_spread_plus"], st_ii["loose_amp_spread_minus"])
    ii_tight_spread = max(st_ii["tight_amp_spread_plus"], st_ii["tight_amp_spread_minus"])
    calibration_disclosure = (
        f"SELFTEST-(ii): the FROZEN loose inner CG tol = {SELFTEST_II_LOOSE_TOL:g} was shipped "
        f"UNCHANGED and FIRED the artifact with NO calibration latitude used — measured loose "
        f"amp_spread = {ii_loose_spread:.3g} (>> the 0.05 threshold), tight-tol "
        f"({INNER_CG_TOL:g}) amp_spread = {ii_tight_spread:.3g} (≤ 0.05, removed by tightening), "
        f"A_sign(loose) = {st_ii['loose_A_sign']:.3g} (≤ 0.10, symmetric) with "
        f"all_scan_legs_converged(loose) = {st_ii['loose_all_scan_legs_converged']}. "
        f"SELFTEST-(iii): p0={SELFTEST_III_P0:g}, sigma={SELFTEST_III_SIGMA:g}, shell band "
        f"{SELFTEST_III_SHELL} (design-time numeric-confirmation run; achieved near-buckling "
        f"fraction = {st_iii['frac_shell_bonds_near_buckling_le_0p2ks']:.4g}, min k_shear,eff = "
        f"{st_iii['min_kse']:.4g}, fired A_sign = {st_iii['A_sign']:.4g}, amp_spread+ = "
        f"{st_iii['amp_spread_plus']:.4g}).")
    return {
        "selftest_ii": st_ii, "selftest_iii": st_iii,
        "gate_fireability_selftest_pass": gate_pass,
        "frozen": "gate_fireability_selftest_pass = SELFTEST-(ii) fires (ii) AND "
                  "SELFTEST-(iii) fires (iii), each with the correct convergence/robustness flags",
        "calibration_disclosure": calibration_disclosure,
    }


def leg0_instrument_validation(cache):
    """Instrument validation (prereg §7): Lamé exterior gate, uniform-medium NULL,
    determinism bit-compare, RVE-size gap, STOP-gate class check."""
    geom = cache[16]
    xc, free, half = _setup(geom)
    ks_cold = np.full(geom[1].shape[0], KS0)
    out = {}

    # (a) uniform-medium NULL — no cage, no source, cold → K_tan/K_0 = 1, ρ_N → 0, r_Z → 1
    u0_null = np.zeros((geom[0].shape[0], 3))
    kc_grown = amplitude_gate(geom, free, u0_null, np.zeros_like(u0_null), ks_cold, "hydro",
                              xc, half, op_converged=True, robustness=False,
                              label="uniform_null")["scan"]
    kc_null = [s for s in kc_grown if abs(s["eps"] - EPS_PROBE_BASE) < 1e-12][0]["k_tan_central"]
    kc_cold = cold_central_modulus(geom, free, "hydro", EPS_PROBE_BASE, xc, half)
    r_null = kc_null / (kc_cold + 1e-300)
    out["uniform_medium_null"] = {
        "K_tan_over_K0": float(r_null), "rho_N": 0.0,
        "r_Z": float(np.sqrt(max(r_null, 0.0) * 1.0)),
        "pass": bool(abs(r_null - 1.0) <= 0.02),
        "note": "uniform cold medium, no cage/source: K_tan/K_0→1, ρ_N→0, r_Z→1",
    }

    # (b) determinism in-process bit-compare — two independent grows are bit-identical (no
    # per-step RNG). ★PR#796 F5/F13: this is a PROXY (two in-process grow calls). The FROZEN
    # criterion is 'two independent full driver runs diff -q clean' — satisfied by the
    # determinism_digest emitted at the end of main() (two full runs → identical digest).
    g1 = grow_vessel(geom, free, [xc.copy()], P_REF, inner_tol=INNER_CG_TOL)
    g2 = grow_vessel(geom, free, [xc.copy()], P_REF, inner_tol=INNER_CG_TOL)
    bit_identical = bool(np.array_equal(g1["u0"], g2["u0"])
                         and np.array_equal(g1["sol"]["kse_raw"], g2["sol"]["kse_raw"]))
    out["determinism"] = {"reruns_bit_identical": bit_identical,
                          "u0_max_abs_diff": float(np.max(np.abs(g1["u0"] - g2["u0"]))),
                          "pass": bit_identical,
                          "note": "IN-PROCESS PROXY (two grow calls). The frozen 'two independent "
                                  "full driver runs diff -q clean' criterion = the determinism_digest "
                                  "(main() emits a content hash; two full runs → identical digest)."}

    # (c) Lamé exterior gate — reuse #782 lame_gate on a single pressurized bulk_only cage
    lame = lame_gate(geom, xc, "bulk_only", 3.0, CAGE_W)
    out["lame_gate"] = {
        "deliverable_exterior_over_interior_max": lame["deliverable_exterior_over_interior_max"],
        "deliverable_pass_tol0p10": lame["deliverable_pass_tol0p10"],
        "cg_residual": lame["cg_residual"], "lame_pass": lame["lame_pass"],
        "note": "carried from #782 §4 Leg 2 (byte-reuse); exterior ∇·u/interior ∇·u ≤ 0.10",
    }

    # (d) RVE-size gap — cold cage-array K_tan/K_0 across L∈{12,16,20} at fixed φ_sf
    size_rows = []
    for L in (12, 16, 20):
        g = cache[L]
        xcL, freeL, halfL = _setup(g)
        cen = cubic_cage_centers(L, PHI_SF_S, xcL)
        ks_coldL = np.full(g[1].shape[0], KS0)
        # cold cage: bulk_only rail on k_a via #782 stiffness; state operator reduces to
        # linear at cold (ε≈0). Measure K_tan/K_0 via the #782 linear ratio (Rule-14).
        unc = uncaged_reference(g, xcL, "hydro")
        m = measure_modulus_ratio(g, xcL, "bulk_only", cen, PHI_SF_RCAGE, CAGE_W, "hydro",
                                  s_rail=1e-4, uncaged=unc)
        size_rows.append({"L": L, "n_cages": len(cen), "phi": packing_fraction(PHI_SF_RCAGE, PHI_SF_S),
                          "K_eff_over_K0": m["ratio"]})
    big = [r["K_eff_over_K0"] for r in size_rows[-2:]]
    size_gap = abs(big[0] - big[1]) / (np.mean(big) + 1e-30)
    out["rve_size_gap"] = {"by_L": size_rows, "gap_two_largest_rel": float(size_gap),
                           "pass": bool(size_gap <= 0.15)}

    # (e) STOP-gate class check — rail SOFTENS (K<1) vs rigid STIFFENS (K>1): opposite sign
    cen = cubic_cage_centers(16, PHI_SF_S, xc)
    unc = uncaged_reference(geom, xc, "hydro")
    rail = measure_modulus_ratio(geom, xc, "bulk_only", cen, PHI_SF_RCAGE, CAGE_W, "hydro",
                                 s_rail=1e-4, uncaged=unc)["ratio"]
    rigid = measure_modulus_ratio(geom, xc, "rigid", cen, PHI_SF_RCAGE, CAGE_W, "hydro",
                                  s_rail=1e-4, uncaged=unc)["ratio"]
    out["stop_gate"] = {"rail_K_eff_over_K0": rail, "rigid_K_eff_over_K0": rigid,
                        "opposite_sign": bool(rail < 1.0 < rigid),
                        "STOP_GATE_PASS": bool(rail < 1.0 < rigid)}

    # (f) Bloch cross-check (prereg §8; PR#796 F14 — never ran before). Cold uncaged P & S
    # compression/shear ToF speeds (the repaired _pe_pulse_xcorr) vs the Bloch c_P/c_S from
    # run_c2_speeds, rel ≤ 0.20. Advisory (a §8 internal validation, not a §7 VOID STOP).
    gB = cache[20]
    posB, biB, bjB, dhatB = gB[0], gB[1], gB[2], gB[3]
    cP_b, cS_b, _ = run_c2_speeds(RHO_STAR, K_S)
    Phi_cold_B = bond_tensors(dhatB, K_A, KS0)
    cP_tof = _pe_pulse_xcorr(gB, Phi_cold_B, cP_b, cP_b, comp=0)["c"]     # P: longitudinal
    cS_tof = _pe_pulse_xcorr(gB, Phi_cold_B, cS_b, cS_b, comp=1)["c"]     # S: transverse
    relP = float(abs(cP_tof - cP_b) / cP_b)
    relS = float(abs(cS_tof - cS_b) / cS_b)
    out["bloch_crosscheck"] = {
        "cP_Bloch": float(cP_b), "cP_ToF_cold": float(cP_tof), "rel_P": relP,
        "cS_Bloch": float(cS_b), "cS_ToF_cold": float(cS_tof), "rel_S": relS,
        "pass_rel_le_0p20_P": bool(relP <= 0.20), "pass_rel_le_0p20_S": bool(relS <= 0.20),
        "note": "cold uncaged P/S ToF speeds (repaired _pe_pulse_xcorr, L=20) vs run_c2_speeds "
                "Bloch c_P/c_S; frozen §8 internal validation (advisory, rel ≤ 0.20)."}

    out["all_validation_pass"] = bool(
        out["uniform_medium_null"]["pass"] and out["determinism"]["pass"]
        and out["lame_gate"]["lame_pass"] and out["rve_size_gap"]["pass"]
        and out["stop_gate"]["STOP_GATE_PASS"])
    return out


# ═════════════════════════════════════════════════════════════════════════════
# ★THE CELL-WALK BINNING (prereg §6 — the 12-row table walked MECHANICALLY)
# ═════════════════════════════════════════════════════════════════════════════
def rz_band(r_Z):
    if r_Z < 0.5 - DELTA_RZ:
        return "Z_lo"
    if r_Z > 0.5 + DELTA_RZ:
        return "Z_hi"
    return "Z_str"                                  # tie r_Z=0.5 → straddling (frozen)


def lift_band(lift):
    if lift < LIFT_L2:
        return "L1"
    if lift < LIFT_L3:
        return "L2"
    return "L3"


def cell_walk_bin(gate_outcome, lift, r_Z):
    """Walk one (gate_outcome, lift, r_Z) tuple through the frozen 12-row table (§6)."""
    if gate_outcome == "ii":
        return "VOID", "ii"
    if gate_outcome == "iii":
        return "MARGINAL", "iii"
    if gate_outcome == "iv":
        return "ANOMALY_STOP_route_to_Grant", "iv"
    lb, zb = lift_band(lift), rz_band(r_Z)
    table = {
        ("L1", "Z_lo"): "SOFT", ("L1", "Z_str"): "UNDETERMINED", ("L1", "Z_hi"): "NULL",
        ("L2", "Z_lo"): "UNDETERMINED", ("L2", "Z_str"): "UNDETERMINED", ("L2", "Z_hi"): "UNDETERMINED",
        ("L3", "Z_lo"): "DISCORDANT", ("L3", "Z_str"): "UNDETERMINED", ("L3", "Z_hi"): "HARD",
    }
    return table[(lb, zb)], "i"


def assert_partition():
    """Driver-side proof the 12-row table partitions the (gate, lift, r_Z) space
    exhaustively + disjointly (prereg §6: 'the result driver asserts this partition by
    walking every shipped tuple through the table')."""
    seen = {}
    for go in ("ii", "iii", "iv"):
        seen[(go, "any", "any")] = cell_walk_bin(go, 1.0, 0.5)[0]
    for lb, lv in (("L1", 1.0), ("L2", 1.3), ("L3", 1.6)):
        for zb, zv in (("Z_lo", 0.30), ("Z_str", 0.50), ("Z_hi", 0.80)):
            seen[("i", lb, zb)] = cell_walk_bin("i", lv, zv)[0]
    # every cell resolved to exactly one bin/disposition; 3 + 9 = 12 rows
    return {"n_rows": len(seen), "partition_ok": bool(len(seen) == 12),
            "rows": {f"{k[0]}|{k[1]}|{k[2]}": v for k, v in seen.items()}}


# ═════════════════════════════════════════════════════════════════════════════
# ★THE VERDICT ARM — grown cage-array vessel at φ_sf (prereg §6/§8)
# ═════════════════════════════════════════════════════════════════════════════
VERDICT_P_REF = 0.040          # [engineering-choice] per-core source for the cage-array arm
VERDICT_SRC_SIGMA = 1.6        # per-core source width (confined to r < r_core) [engineering-choice]
#                                ★PR#796 F10/F14: an UNDISCLOSED knob differing from the single-
#                                core calibrated SRC_SIGMA=2.5 — now ledgered + tested by a σ-variant
#                                verdict arm (below); grade-frame Eulerian/imposed.
VERDICT_SRC_SIGMA_VARIANT = 2.5   # the single-core calibrated width — σ-verdict-relevance probe
VERDICT_WALL = "bulk_only"     # the k_a-only verdict wall (§0 Fork W; SYMMETRIC is a control)
VERDICT_S_RAIL = 1e-4          # #782 deep rail on the cage shells


def build_cage(geom, wall_class=VERDICT_WALL, s_rail=VERDICT_S_RAIL, eps_pre=0.0):
    """Cage array at φ_sf: centers + per-bond (k_a_bond railed on shells, k_s_cold).
    Rule-14 reuse of the #782 cage_bond_stiffness (bulk_only rails k_a; k_s = KS0)."""
    pos, bi, bj, dhat, mid = geom
    L = int(round((pos.max(0) - pos.min(0)).mean())) + 1
    xc = 0.5 * (pos.max(0) + pos.min(0))
    centers = cubic_cage_centers(L, PHI_SF_S, xc)
    k_a_bond, k_s_cold = cage_bond_stiffness(dhat, mid, centers, PHI_SF_RCAGE, CAGE_W,
                                             wall_class, s_rail, eps_pre)
    return centers, np.asarray(k_a_bond, float), np.asarray(k_s_cold, float)


def grow_verdict_arm(geom, free, xc, p0, seed_class="fixed_budget",
                     wall_class=VERDICT_WALL, s_rail=VERDICT_S_RAIL,
                     sigma=VERDICT_SRC_SIGMA, a_yield_scale=1.0):
    """Grow the cage-array vessel (bulk-only wall + per-core radiation source) and read
    the THREE STOP criteria. `yield_saturated` grows p0 until max_r A(r) reaches
    A_yield·a_yield_scale (A(r) = local |ε_axial|), conditional on a stable equilibrium."""
    pos, bi, bj, dhat, mid = geom
    N = pos.shape[0]
    centers, k_a_bond, k_s_cold = build_cage(geom, wall_class, s_rail)
    yield_reached = None
    peak_A_ceiling = None
    yield_scan = None
    if seed_class == "yield_saturated":
        # BOUNDED ascending p0 scan, EXTENDED PAST the buckling onset to OBSERVE the terminal
        # state (PR#796 F11/F3/F8 repair — the shipped scan stopped at an UNDISCLOSED p0=0.06
        # ceiling with every point STABLE and banked yield_saturated as an *extrapolated* NULL).
        # ALL yield-scan solves run at a fail-fast cap (outer≤8, inner≤800) — the empirical-driver
        # runtime fix (Rule 10): the near-buckling secant grinds the frozen 100×4000 caps. F9:
        # the cap applies to EVERY yield-scan solve, not only buckled ones. The first non-stable
        # point is the OBSERVED terminal state, classified physical BUCKLING (min k_shear,eff ≤ 0)
        # vs a converged=False STALL ((ii)-artifact per §2).
        target = A_YIELD * a_yield_scale
        scan_p0 = YIELD_SCAN_P0
        best_stable = None
        reached = None
        peak_A_ceiling = 0.0
        highest_stable_p0 = None
        onset = None
        for pm in scan_p0:
            b_src = radiation_source(pos, centers, pm, sigma, r_core=PHI_SF_RCAGE)
            sol = solve_state_dependent(geom, free, np.zeros((N, 3)), b_src, k_s_cold,
                                        k_a_bond=k_a_bond, inner_tol=INNER_CG_TOL,
                                        outer_max=YIELD_OUTER_CAP, inner_max=YIELD_INNER_CAP)
            peakA = float(np.max(np.abs(sol["eps_axial"])))
            mkse = float(sol["kse_raw"].min())
            stable = bool(sol["converged"] and mkse > 0.0)
            if stable:
                best_stable = (pm, sol, b_src, peakA)
                highest_stable_p0 = float(pm)
                peak_A_ceiling = max(peak_A_ceiling, peakA)
                if peakA >= target:
                    reached = (pm, sol, b_src, peakA)
                    break
            else:
                onset = {"p0": float(pm), "min_kse": mkse, "peak_A": peakA,
                         "converged": bool(sol["converged"]),
                         "kind": "buckled" if mkse <= 0.0 else "stall_ii_artifact",
                         "outer_it": int(sol["outer_it"]), "nlres": float(sol["nlres"])}
                break                                # OBSERVED terminal state — STOP the scan
        # capped-vs-uncapped confirmation at the terminal point (F9): re-solve the onset p0 with
        # 2× MORE outer/inner iterations than the fail-fast cap and confirm the classification is
        # unchanged (more iterations do NOT rescue the buckled state → the cap hid no would-be-
        # stable state). NOT the full frozen 100×4000 — a buckled (non-SPD) state makes the inner
        # CG non-convergent, so the full cap would grind indefinitely (exactly the pathology the
        # fail-fast cap avoids, Rule 10); a bounded 2× confirmation is sufficient.
        capped_vs_uncapped = None
        if onset is not None:
            b_on = radiation_source(pos, centers, onset["p0"], sigma, r_core=PHI_SF_RCAGE)
            sol_full = solve_state_dependent(geom, free, np.zeros((N, 3)), b_on, k_s_cold,
                                             k_a_bond=k_a_bond, inner_tol=INNER_CG_TOL,
                                             outer_max=2 * YIELD_OUTER_CAP,
                                             inner_max=2 * YIELD_INNER_CAP)
            mkse_full = float(sol_full["kse_raw"].min())
            kind_full = ("buckled" if mkse_full <= 0.0
                         else ("stall_ii_artifact" if not sol_full["converged"] else "stable"))
            capped_vs_uncapped = {
                "onset_p0": onset["p0"], "failfast_cap": [YIELD_OUTER_CAP, YIELD_INNER_CAP],
                "confirm_cap_2x": [2 * YIELD_OUTER_CAP, 2 * YIELD_INNER_CAP],
                "failfast_min_kse": onset["min_kse"], "failfast_kind": onset["kind"],
                "confirm_min_kse": mkse_full, "confirm_kind": kind_full,
                "confirm_outer_it": int(sol_full["outer_it"]),
                "classification_unchanged": bool(kind_full == onset["kind"])}
        pick = reached if reached is not None else best_stable
        if pick is None:
            pm = scan_p0[0]
            b_src = radiation_source(pos, centers, pm, sigma, r_core=PHI_SF_RCAGE)
            sol = solve_state_dependent(geom, free, np.zeros((N, 3)), b_src, k_s_cold,
                                        k_a_bond=k_a_bond, inner_tol=INNER_CG_TOL,
                                        outer_max=YIELD_OUTER_CAP, inner_max=YIELD_INNER_CAP)
        else:
            pm, sol, b_src, _ = pick
        p0 = pm
        yield_reached = bool(reached is not None)
        yield_scan = {
            "scan_grid_p0": list(scan_p0), "outer_cap": YIELD_OUTER_CAP,
            "inner_cap": YIELD_INNER_CAP, "a_yield_target": target,
            "highest_stable_p0": highest_stable_p0, "peak_A_ceiling": peak_A_ceiling,
            "terminal_onset": onset, "capped_vs_uncapped": capped_vs_uncapped,
            "yield_reached_before_buckling": yield_reached}
    else:
        b_src = radiation_source(pos, centers, p0, sigma, r_core=PHI_SF_RCAGE)
        sol = solve_state_dependent(geom, free, np.zeros((N, 3)), b_src, k_s_cold,
                                    k_a_bond=k_a_bond, inner_tol=INNER_CG_TOL)
    T = bond_tension_remap(sol["eps_axial"], k_a_bond)
    max_abs_T = float(np.max(np.abs(T)))
    min_kse = float(sol["kse_raw"].min())
    tension_thresh = 0.05 * K_A * A_YIELD
    g_cg = bool(sol["converged"])
    g_tension = bool(max_abs_T >= tension_thresh)
    g_bonds = bool(min_kse > 0.0)
    exists = bool(g_cg and g_tension and g_bonds)
    if seed_class == "yield_saturated":
        # a yield_saturated state EXISTS only if the peak strain reached A_yield with a
        # stable equilibrium (else the source buckled the vessel before yield — the state
        # realized is a fixed-budget-at-the-buckling-edge, NOT a yield-saturated one).
        exists = bool(exists and yield_reached)
    return {
        "seed_class": seed_class, "p0": float(p0), "a_yield_scale": a_yield_scale,
        "u0": sol["u"], "b_src": b_src, "sol": sol, "T": T,
        "centers": centers, "k_a_bond": k_a_bond, "k_s_cold": k_s_cold,
        "wall_class": wall_class, "phi_sf": packing_fraction(PHI_SF_RCAGE, PHI_SF_S),
        "max_abs_T": max_abs_T, "tension_threshold_0p05kaAyield": tension_thresh,
        "min_kse": min_kse, "peak_A": float(np.max(np.abs(sol["eps_axial"]))),
        "peak_A_ceiling": peak_A_ceiling, "yield_reached": yield_reached,
        "yield_scan": yield_scan,
        "eps_min": float(sol["eps_axial"].min()), "eps_max": float(sol["eps_axial"].max()),
        "grown_CG_converged": g_cg, "grown_tension_nonzero": g_tension,
        "grown_bonds_positive": g_bonds,
        "grown_equilibrium_exists": exists,
        "outer_it": sol["outer_it"], "nlres": sol["nlres"],
    }


def measure_K_ratio(geom, free, arm, xc, half, mode="hydro", robustness=True):
    """Amplitude gate + K_tan/K_0 for a grown arm. K_tan/K_0 = central second diff of
    the grown core energy ÷ cold central second diff, at ε_probe = base (prereg §2 JOB 1).
    Runs the state operator with the arm's railed k_a_bond + live remap."""
    k_s_cold, k_a_bond = arm["k_s_cold"], arm["k_a_bond"]
    gate = amplitude_gate(geom, free, arm["u0"], arm["b_src"], k_s_cold, mode, xc, half,
                          op_converged=arm["grown_CG_converged"], robustness=robustness,
                          label=f"{arm['seed_class']}_{mode}", k_a_bond=k_a_bond)
    # K_tan/K_0 at base amplitude
    kc_grown = [s for s in gate["scan"] if abs(s["eps"] - EPS_PROBE_BASE) < 1e-12][0]["k_tan_central"]
    kc_cold = cold_central_modulus(geom, free, mode, EPS_PROBE_BASE, xc, half)
    return {"gate": gate, "K_tan_over_K0": float(kc_grown / (kc_cold + 1e-300)),
            "k_central_grown_base": float(kc_grown), "k_central_cold_base": float(kc_cold)}


# ═════════════════════════════════════════════════════════════════════════════
# ★C-V PROFILING (prereg §5 — sweep ε_bias, read small-signal K(ε_bias))
# ═════════════════════════════════════════════════════════════════════════════
def cv_profile(geom, free, arm, xc, half):
    """Sweep a quasi-static STRAIN bias ε_bias both signs; read K(ε_bias) = central
    tangent about each biased operating point; reconstruct the shell POSITION / WIDTH /
    ASYMMETRY by the frozen §5 formulas (rewired to the LIVE geometric term)."""
    pos, bi, bj, dhat, mid = geom
    N = pos.shape[0]
    k_s_cold, k_a_bond, b_src = arm["k_s_cold"], arm["k_a_bond"], arm["b_src"]
    biases = np.linspace(-EPS_BIAS_MAX, EPS_BIAS_MAX, N_BIAS)
    K_of = []
    for eb in biases:
        u_bc = np.zeros((N, 3))
        u_bc[~free] = affine_field(pos[~free], xc, strain_mode("hydro", eb))
        sol = solve_state_dependent(geom, free, u_bc, b_src, k_s_cold, k_a_bond=k_a_bond,
                                    inner_tol=INNER_CG_TOL, u_init=arm["u0"])
        pr = tangent_probe(geom, free, sol["u"], b_src, k_s_cold, "hydro", EPS_PROBE_BASE,
                           xc, half, k_a_bond=k_a_bond)
        K_of.append(pr["k_tan_central"])
    K_of = np.array(K_of)
    K0_bias = float(K_of[N_BIAS // 2])               # ε_bias=0 (unbiased grown OP), frozen normalizer
    # dK/dε_bias (central), |dK/dε_bias| shell profile
    dK = np.gradient(K_of, biases)
    absdK = np.abs(dK)
    imax = int(np.argmax(absdK))
    span_truncated = bool(imax in (0, len(biases) - 1))
    # 3-point parabolic interpolation of the argmax (POSITION)
    if 0 < imax < len(biases) - 1:
        y0, y1, y2 = absdK[imax - 1], absdK[imax], absdK[imax + 1]
        denom = (y0 - 2 * y1 + y2)
        shift = 0.5 * (y0 - y2) / denom if abs(denom) > 1e-30 else 0.0
        position = float(biases[imax] + shift * (biases[1] - biases[0]))
    else:
        position = float(biases[imax])
    # FWHM of |dK/dε_bias| by linear interp of half-max crossings
    hm = 0.5 * absdK.max()
    above = absdK >= hm
    idxs = np.where(above)[0]
    if idxs.size >= 1:
        lo_i, hi_i = idxs[0], idxs[-1]
        width_total = float(biases[hi_i] - biases[lo_i])
        # squeeze-side (ε<0) vs stretch-side (ε>0) half-widths about the peak
        w_sq = float(max(biases[imax] - biases[lo_i], 0.0))
        w_st = float(max(biases[hi_i] - biases[imax], 0.0))
    else:
        width_total = w_sq = w_st = 0.0
    asymmetry = float((w_st - w_sq) / (width_total + 1e-30)) if width_total > 0 else 0.0
    return {
        "eps_bias": [float(b) for b in biases],
        "K_of_eps_bias": [float(k) for k in K_of],
        "K0_unbiased": K0_bias,
        "shell_POSITION": position, "shell_WIDTH": width_total,
        "shell_WIDTH_squeeze": w_sq, "shell_WIDTH_stretch": w_st,
        "shell_ASYMMETRY": asymmetry,
        "anisotropic_confirmed_absasym_ge_0p15": bool(abs(asymmetry) >= ASYMMETRY_THRESH),
        "span_truncated": span_truncated,
    }


# ═════════════════════════════════════════════════════════════════════════════
# ★PERCOLATION SUB-CHECK (prereg §6 — hoop-tense spanning cluster)
# ═════════════════════════════════════════════════════════════════════════════
def percolation(geom, arm):
    """Build the graph of grown TENSILE (hoop-class) bonds (relaxed T ≥ 0.5·max T) and
    test for a face-to-face SPANNING cluster across the RVE (union-find)."""
    pos, bi, bj, dhat, mid = geom
    T = arm["T"]
    Tmax = float(np.max(T))
    if Tmax <= 0:
        return {"hoop_percolates": False, "largest_tense_cluster_frac": 0.0,
                "n_tense_bonds": 0, "note": "no tensile bonds (max T ≤ 0)"}
    tense = T >= 0.5 * Tmax
    tb_i, tb_j = bi[tense], bj[tense]
    N = pos.shape[0]
    parent = np.arange(N)

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for a, b in zip(tb_i, tb_j):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
    nodes_in = np.unique(np.concatenate([tb_i, tb_j]))
    roots = np.array([find(a) for a in nodes_in])
    # spanning: some cluster touches both the min-x and max-x faces
    lo = pos[:, 0].min()
    hi = pos[:, 0].max()
    near_lo = nodes_in[pos[nodes_in, 0] <= lo + 1.0]
    near_hi = nodes_in[pos[nodes_in, 0] >= hi - 1.0]
    roots_lo = {find(a) for a in near_lo}
    roots_hi = {find(a) for a in near_hi}
    spans = bool(roots_lo & roots_hi)
    _, counts = np.unique(roots, return_counts=True)
    largest = int(counts.max()) if counts.size else 0
    return {"hoop_percolates": spans,
            "largest_tense_cluster_frac": float(largest / max(N, 1)),
            "n_tense_bonds": int(tense.sum()),
            "corroborative": "percolation True corroborates HARD; False corroborates SOFT/NULL"}


# ═════════════════════════════════════════════════════════════════════════════
# ★PAINTED-ANISOTROPIC provenance-ablation arm (prereg §8 — grown-vs-painted)
# ═════════════════════════════════════════════════════════════════════════════
def painted_anisotropic_arm(geom, free, arm, xc, half):
    """Copy the grown k_shear,eff(u_0) anisotropy pattern and PAINT it (static,
    u-independent) onto a fresh un-relaxed config; measure K_tan/K_0 with the SAME
    central second-difference on the PAINTED (linear) operator. Separates provenance
    (grown vs painted) from anisotropy (vs isotropic)."""
    pos, bi, bj, dhat, mid = geom
    kse_painted = np.maximum(arm["sol"]["kse_raw"], KSE_SOLVE_FLOOR)   # frozen k_s pattern
    k_a_bond = arm["k_a_bond"]
    # painted operator is u-INDEPENDENT: linear KUBC measure (the #782 primitive on the
    # painted k_s), central second difference at base amplitude.
    def painted_energy(E):
        N = pos.shape[0]
        u_bc = np.zeros((N, 3))
        u_bc[~free] = affine_field(pos[~free], xc, E)
        Phi = bond_tensors(dhat, k_a_bond, kse_painted)
        diag = jacobi_diag(dhat, k_a_bond, kse_painted, bi, bj, N)
        idx = np.where(free)[0]
        Mi = 1.0 / np.maximum(diag[free], 1e-30)

        def applyK(wf):
            w = np.zeros((N, 3)); w[idx] = wf
            return (-forces(w, Phi, bi, bj, N))[idx]
        rhs = forces(u_bc, Phi, bi, bj, N)[idx]
        x, _, _ = _cg_interior(applyK, rhs, np.zeros_like(rhs), Mi, INNER_CG_TOL, INNER_CG_MAX)
        u = u_bc.copy(); u[idx] = x
        return core_energy(u, Phi, bi, bj, mid, xc, half)
    e = EPS_PROBE_BASE
    Up = painted_energy(strain_mode("hydro", e))
    Um = painted_energy(strain_mode("hydro", -e))
    U0 = painted_energy(strain_mode("hydro", 0.0))
    k_central_painted = (Up + Um - 2.0 * U0) / e ** 2
    kc_cold = cold_central_modulus(geom, free, "hydro", e, xc, half)
    return {"K_tan_over_K0_painted": float(k_central_painted / (kc_cold + 1e-300)),
            "note": "painted = grown k_shear,eff(u_0) pattern frozen u-independent; "
                    "GROWN≠PAINTED ⇒ provenance-real; GROWN≈PAINTED ⇒ anisotropy-driven"}


# ═════════════════════════════════════════════════════════════════════════════
# ★ABLATION DECOMPOSITION — the F6 "cancellation"-mechanism REFUTATION (PR#796)
# ═════════════════════════════════════════════════════════════════════════════
def _painted_K_ratio(geom, free, kse_pattern, k_a_bond, xc, half):
    """Central second-difference K_tan/K_0 (core-restricted) for an arbitrary PAINTED
    (u-independent) transverse-stiffness pattern — the driver's own painted machinery."""
    pos, bi, bj, dhat, mid = geom
    N = pos.shape[0]
    kse = np.maximum(kse_pattern, KSE_SOLVE_FLOOR)

    def energy(E):
        u_bc = np.zeros((N, 3))
        u_bc[~free] = affine_field(pos[~free], xc, E)
        Phi = bond_tensors(dhat, k_a_bond, kse)
        diag = jacobi_diag(dhat, k_a_bond, kse, bi, bj, N)
        idx = np.where(free)[0]
        Mi = 1.0 / np.maximum(diag[free], 1e-30)

        def applyK(wf):
            w = np.zeros((N, 3)); w[idx] = wf
            return (-forces(w, Phi, bi, bj, N))[idx]
        rhs = forces(u_bc, Phi, bi, bj, N)[idx]
        x, _, _ = _cg_interior(applyK, rhs, np.zeros_like(rhs), Mi, INNER_CG_TOL, INNER_CG_MAX)
        u = u_bc.copy(); u[idx] = x
        return core_energy(u, Phi, bi, bj, mid, xc, half)
    e = EPS_PROBE_BASE
    kc = (energy(strain_mode("hydro", e)) + energy(strain_mode("hydro", -e))
          - 2.0 * energy(strain_mode("hydro", 0.0))) / e ** 2
    kc_cold = cold_central_modulus(geom, free, "hydro", e, xc, half)
    return float(kc / (kc_cold + 1e-300))


def ablation_decomposition(geom, free, arm, xc, half, control_K):
    """DECOMPOSE the grown small-signal tangent into its named 'hoop-stiffen' (ε_axial>0)
    and 'radial-soften' (ε_axial<0) painted components — the PR#796 F6 repair. The retracted
    result-doc headline claimed the null lift (≈1.0) is a hoop-stiffen ⊕ radial-soften
    CANCELLATION. That mechanism predicts hoop_only > control AND radial_only < control (one
    stiffens, one softens, they cancel to ≈control). The cheapest ablation (this function)
    tests it: paint ONLY the tensile-bond remap (radial bonds reset cold) vs ONLY the
    compressive-bond remap (hoop bonds reset cold), each measured core-restricted vs the
    isotropic control. If radial_only does NOT drop below control, the cancellation mechanism
    is REFUTED — both named components STIFFEN and the null lift is provenance/live-operator-
    driven (grown≈painted≈control), NOT a hoop-vs-radial cancellation."""
    kse_grown = np.asarray(arm["sol"]["kse_raw"], float)
    eps = np.asarray(arm["sol"]["eps_axial"], float)
    k_a_bond = arm["k_a_bond"]
    ks_cold = np.asarray(arm["k_s_cold"], float)   # the cold (railed) transverse baseline
    # full painted grown pattern
    k_full = _painted_K_ratio(geom, free, kse_grown, k_a_bond, xc, half)
    # hoop-only: keep the remap where ε_axial>0 (tension stiffens); reset ε_axial<0 bonds cold
    kse_hoop = np.where(eps > 0.0, kse_grown, ks_cold)
    k_hoop = _painted_K_ratio(geom, free, kse_hoop, k_a_bond, xc, half)
    # radial-only: keep the remap where ε_axial<0 (compression softens); reset ε_axial>0 cold
    kse_rad = np.where(eps < 0.0, kse_grown, ks_cold)
    k_rad = _painted_K_ratio(geom, free, kse_rad, k_a_bond, xc, half)
    d_full = float(k_full / control_K - 1.0)
    d_hoop = float(k_hoop / control_K - 1.0)
    d_rad = float(k_rad / control_K - 1.0)
    # cancellation mechanism REQUIRES the radial-only component to SOFTEN the core tangent
    radial_softens = bool(d_rad < 0.0)
    cancellation_supported = bool((d_hoop > 0.0) and (d_rad < 0.0))
    return {
        "control_K_eff_over_K0": float(control_K),
        "K_tan_over_K0_full_painted": k_full,
        "K_tan_over_K0_hoop_only": k_hoop,
        "K_tan_over_K0_radial_only": k_rad,
        "delta_full_vs_control_pct": 100.0 * d_full,
        "delta_hoop_only_vs_control_pct": 100.0 * d_hoop,
        "delta_radial_only_vs_control_pct": 100.0 * d_rad,
        "radial_only_softens_core_tangent": radial_softens,
        "cancellation_mechanism_supported": cancellation_supported,
        "n_tension_bonds_eps_gt_0": int((eps > 0.0).sum()),
        "n_compression_bonds_eps_lt_0": int((eps < 0.0).sum()),
        "attribution": ("cancellation SUPPORTED (hoop stiffens, radial softens)" if cancellation_supported
                        else "cancellation REFUTED — the radial-soften pattern does NOT soften the "
                             "core tangent; both named components stiffen ⇒ the null lift is "
                             "provenance/live-operator-driven, NOT a hoop-vs-radial cancellation"),
    }


# ═════════════════════════════════════════════════════════════════════════════
# ★PROTOCOL E — ρ_eff MEASURED via long-λ compression-pulse time-of-flight (§4)
# ═════════════════════════════════════════════════════════════════════════════
def _pe_pulse_xcorr(geom, Phi, c_launch, cP_window, comp=0, amp=PE_AMP):
    """Coherent rightward long-λ compression pulse launched into a FROZEN medium operator
    Phi; TWO density-peak monitors (top-K |field|², PML-excluded); cross-correlation
    transit-time between them → the group speed (prereg §4; the PR#796 F2 repair). Source at
    box CENTER (the frozen (L/2−r_meas) window frame). The reactance pair — C-state
    (compression amplitude) AND L-state (kinetic flux) — is recorded at EVERY step over the
    frozen reflection-free window (Rule-10 corollary; NOT hardcoded)."""
    pos, bi, bj, dhat, mid = geom
    N = pos.shape[0]
    x = pos[:, 0]
    lo, hi = float(x.min()), float(x.max())
    Lx = hi - lo
    x_src = lo + 0.5 * Lx
    r1 = PE_R1_FRAC * Lx; r2 = PE_R2_FRAC * Lx; w = PE_W_FRAC * Lx
    # PML/window boundary-cell exclusion (prereg §4 Rule-10 corollary): drop nodes within
    # PE_PML_THICKNESS of ANY face BEFORE the top-K density argpartition (PML cells return a
    # frozen-absorbing artifact, not interior physics).
    interior = ((pos >= (lo + PE_PML_THICKNESS)) & (pos <= (hi - PE_PML_THICKNESS))).all(axis=1)
    s1 = np.where((np.abs(x - (x_src + r1)) < 0.5 * w) & interior)[0]
    s2 = np.where((np.abs(x - (x_src + r2)) < 0.5 * w) & interior)[0]
    omega = omega_max_cold(Phi, bi, bj, N)
    dt = PE_CFL * 2.0 / omega
    # FROZEN reflection-free window: t_end ≤ 0.9·(L/2 − r_meas)/c_P (r_meas = far monitor r2)
    t_end = PE_WINDOW_SAFETY * (0.5 * Lx - r2) / cP_window
    n = int(np.ceil(t_end / dt)) + 1
    g = np.exp(-((x - x_src) ** 2) / (2.0 * w ** 2))
    u = np.zeros((N, 3)); v = np.zeros((N, 3))
    u[:, comp] = amp * g
    v[:, comp] = c_launch * (x - x_src) / w ** 2 * amp * g       # coherent rightward launch
    F = forces(u, Phi, bi, bj, N)
    t1, t2, cstate, lstate = [], [], [], []

    def _peak(si):
        """density-peak (top-K |field|²) selection → (signed-disp mean, |disp| mean, kin flux mean)."""
        fld = u[si, comp]
        d2 = fld * fld
        top = np.argpartition(d2, -PE_TOPK)[-PE_TOPK:] if d2.size > PE_TOPK else np.arange(d2.size)
        return float(np.mean(fld[top])), float(np.mean(np.abs(fld[top]))), float(np.mean(v[si, comp][top] ** 2))

    for _ in range(n):
        s1v, s1a, s1l = _peak(s1)
        s2v, _, _ = _peak(s2)
        t1.append(s1v); t2.append(s2v)
        cstate.append(s1a); lstate.append(s1l)        # reactance pair at monitor 1, every step
        u = u + v * dt + 0.5 * F * dt ** 2
        Fn = forces(u, Phi, bi, bj, N)
        v = v + 0.5 * (F + Fn) * dt
        F = Fn
    a = np.array(t1) - np.mean(t1)
    b = np.array(t2) - np.mean(t2)
    xc = np.correlate(b, a, mode="full")
    lags = np.arange(-n + 1, n)
    xcp = xc.copy(); xcp[lags <= 0] = -np.inf           # far monitor arrives LATER (positive lag)
    im = int(np.argmax(xcp))
    if 0 < im < len(xc) - 1:                            # parabolic sub-step interpolation
        y0, y1, y2 = xc[im - 1], xc[im], xc[im + 1]
        den = (y0 - 2 * y1 + y2)
        sh = 0.5 * (y0 - y2) / den if abs(den) > 1e-300 else 0.0
    else:
        sh = 0.0
    lag = (lags[im] + sh) * dt
    c = float((r2 - r1) / lag) if lag > 0 else float("nan")
    cstate = np.array(cstate); lstate = np.array(lstate)
    pair_ok = bool(cstate.size and lstate.size
                   and (cstate.max() - cstate.min()) > 1e-9 * amp
                   and (lstate.max() - lstate.min()) > 1e-15 * amp ** 2)
    return {
        "c": c, "lag_steps": int(lags[im]), "n_steps": int(n), "dt": float(dt),
        "t_end": float(t_end), "n_mon1": int(s1.size), "n_mon2": int(s2.size),
        "reactance_pair_recorded": pair_ok,
        "C_state_peak_step": int(np.argmax(cstate)) if cstate.size else -1,
        "L_state_peak_step": int(np.argmax(lstate)) if lstate.size else -1,
    }


def _pe_sc_speed(geom, Phi, cP_window):
    """Self-consistent coherent group speed: iterate the launch speed to the medium's own
    forward-eigenmode fixed point (c_launch = c_measured), capped at PE_SC_MAXIT. The FROZEN
    arrival criterion (prereg §4 'first-arrival group speed', operationalized as the coherent
    forward-eigenmode transit speed). Returns (c, history, last_pulse_dict)."""
    c = cP_window
    hist = [float(c)]
    last = None
    for _ in range(PE_SC_MAXIT):
        r = _pe_pulse_xcorr(geom, Phi, c, cP_window)
        cn = r["c"]; last = r
        if not (cn == cn):                              # nan guard
            break
        hist.append(float(cn))
        if abs(cn - c) / max(abs(c), 1e-9) <= PE_SC_TOL:
            c = cn
            break
        c = cn
    return float(c), hist, last


def _rz(K_ratio, c0, ce):
    """r_Z = Z_eff/Z_0 = (K_eff/c_eff)/(K_0/c_0) = (K_eff/K_0)·(c_0/c_eff)."""
    return float(K_ratio * (c0 / ce)) if (ce and ce == ce and c0 == c0) else float("nan")


def _rho(K_ratio, c0, ce):
    return float(K_ratio * (c0 / ce) ** 2) if (ce and ce == ce and c0 == c0) else float("nan")


def protocol_E(L_pe, arm_builder, cP_cold, K_ratio, label="", do_sc=True):
    """Measure ρ_eff/ρ_0 on the grown-vessel RVE via a long-λ compression-pulse ToF (prereg
    §4; REVISION per PR#796 F2 — PML exclusion, density-peak top-K sampling, the FROZEN
    reflection-free window, a FROZEN cross-correlation arrival criterion, a REAL reactance-pair
    flag, run at L∈{32,48}). ρ_eff/ρ_0 = K_ratio·(c_0/c_eff)²; r_Z = K_ratio·(c_0/c_eff).
    STRUCTURAL term only (no trapped-energy inertia; C-load open, clm-m5swh9; NO β claim).

    ★F2 METHOD-SENSITIVITY (surfaced, not hidden): the grown cage medium is a MARGINAL-λ
    (k·r_core≈2–4 on L∈{32,48}) locally-resonant scatterer, so the ToF c_eff is EXTRACTION-
    DEPENDENT. Two frozen coherent extractions are shipped as a method-band plus the structural
    anchor: (a) launch@cP one-shot (the fast coherent FRONT = the prereg's 'first-arrival');
    (b) SC-coherent (the self-consistent forward-eigenmode group speed); (c) structural
    ρ_eff/ρ_0≡1 (the long-λ k→0 limit for uniform point masses). method_indeterminate = the
    band straddles >1 r_Z verdict bin ⇒ the ρ-correction CANNOT move the bin off the structural
    anchor (route to Grant; the SUBC/periodic lower-bound bracket is the owed resolver, NOT a
    ToF). The ToF-medium is grown with a fail-fast capped solve (PE_GROW_OUTER/PE_GROW_INNER_TOL
    — verified identical grown OP to the frozen full solve; the VERDICT K_tan keeps 1e-10)."""
    geom = build_finite_srs(L_pe)
    pos, bi, bj, dhat, mid = geom
    Phi_cold = bond_tensors(dhat, K_A, KS0)
    xc = 0.5 * (pos.max(0) + pos.min(0))
    free = ~boundary_mask(pos, None)
    centers, k_a_bond, k_s_cold, u0 = arm_builder(geom, free, xc)
    Phi_grown = state_operator(u0, bi, bj, dhat, k_s_cold, k_a_bond)[0]

    # (a) launch@cP one-shot — the fast coherent front ("first-arrival")
    p_c0 = _pe_pulse_xcorr(geom, Phi_cold, cP_cold, cP_cold)
    p_ce = _pe_pulse_xcorr(geom, Phi_grown, cP_cold, cP_cold)
    c0_1, ce_1 = p_c0["c"], p_ce["c"]
    rZ_1 = _rz(K_ratio, c0_1, ce_1)

    # (b) SC-coherent forward-eigenmode group speed (the band's slow end)
    if do_sc:
        c0_sc, c0_hist, _ = _pe_sc_speed(geom, Phi_cold, cP_cold)
        ce_sc, ce_hist, ce_pulse = _pe_sc_speed(geom, Phi_grown, cP_cold)
        rZ_sc = _rz(K_ratio, c0_sc, ce_sc)
    else:
        c0_sc = ce_sc = rZ_sc = float("nan"); c0_hist = ce_hist = []; ce_pulse = None

    # (c) structural anchor (ρ_eff/ρ_0 ≡ 1; long-λ k→0 limit, uniform point masses)
    rZ_struct = float(np.sqrt(max(K_ratio, 0.0)))

    band = sorted(v for v in (rZ_1, rZ_sc, rZ_struct) if v == v)
    bins_in_band = sorted({rz_band(v) for v in band})
    method_indeterminate = bool(len(bins_in_band) > 1)
    # Bloch cross-check (prereg §8): cold ToF speed vs run_c2_speeds cP, rel ≤ 0.20
    bloch_rel = float(abs(c0_1 - cP_cold) / cP_cold) if c0_1 == c0_1 else float("nan")

    return {
        "L_pe": L_pe,
        "c_0_launch_cP": c0_1, "c_eff_launch_cP": ce_1,
        "c0_over_ceff_launch_cP": float(c0_1 / ce_1) if ce_1 else float("nan"),
        "c_0_SC": c0_sc, "c_eff_SC": ce_sc,
        "K_tan_over_K0_static": float(K_ratio),
        "rho_eff_over_rho0_launch_cP": _rho(K_ratio, c0_1, ce_1),
        "rho_eff_over_rho0_SC": _rho(K_ratio, c0_sc, ce_sc),
        "r_Z_launch_cP_headline": rZ_1, "r_Z_SC": rZ_sc, "r_Z_structural": rZ_struct,
        "r_Z_method_band": [band[0], band[-1]] if band else [float("nan"), float("nan")],
        "method_indeterminate": method_indeterminate,
        "bins_spanned_by_band": bins_in_band,
        "sc_cold_history": c0_hist, "sc_grown_history": ce_hist,
        "reactance_pair_recorded": bool(p_ce["reactance_pair_recorded"]),
        "reactance_C_peak_step": int(p_ce["C_state_peak_step"]),
        "reactance_L_peak_step": int(p_ce["L_state_peak_step"]),
        "reactance_note": "C-state (compression amp) & L-state (kinetic flux) recorded EVERY "
                          "step over the frozen window; distinct peak steps ⇒ a genuine reactive "
                          "C↔L exchange, not a one-phase snapshot (Rule-10 corollary).",
        "window_frozen": "t_end ≤ 0.9·(L/2 − r_meas)/c_P (reflection-free; r_meas = far monitor)",
        "n_steps": int(p_ce["n_steps"]), "pml_thickness": PE_PML_THICKNESS,
        "n_mon1": int(p_ce["n_mon1"]), "n_mon2": int(p_ce["n_mon2"]),
        "bloch_crosscheck_cold_ToF_vs_cP_rel": bloch_rel,
        "bloch_crosscheck_pass_rel_le_0p20": bool(bloch_rel <= 0.20) if bloch_rel == bloch_rel else False,
        "method_band_note": "grown cage medium = MARGINAL-λ (k·r_core≈2–4 on L∈{32,48}) locally-"
                            "resonant scatterer ⇒ ToF c_eff EXTRACTION-DEPENDENT; r_Z spans "
                            "[launch@cP front, SC-coherent] bracketing the structural ρ≡1 value; "
                            "method_indeterminate ⇒ the ρ-correction cannot move the bin off the "
                            "structural anchor (route to Grant / SUBC bracket owed).",
        "structural_scope": "Protocol E measures the STRUCTURAL ρ term only; the engine hosts "
                            "no trapped-energy inertia (C-load open, clm-m5swh9); NO β claim "
                            "from this bench",
    }


# ═════════════════════════════════════════════════════════════════════════════
# ★THE VERDICT ASSEMBLY (prereg §6 — grow → gate → lift → r_Z → cell-walk bin)
# ═════════════════════════════════════════════════════════════════════════════
def isotropic_control_K(geom, xc):
    """The #782 isotropic bulk_only-cold cage K_eff/K_0 at φ_sf — the crash BASELINE
    K_ratio_lift normalizes against (Rule-14; reproduces #782's 0.296)."""
    centers = cubic_cage_centers(int(round((geom[0].max(0) - geom[0].min(0)).mean())) + 1,
                                 PHI_SF_S, xc)
    unc = uncaged_reference(geom, xc, "hydro")
    return float(measure_modulus_ratio(geom, xc, VERDICT_WALL, centers, PHI_SF_RCAGE, CAGE_W,
                                       "hydro", s_rail=VERDICT_S_RAIL, uncaged=unc)["ratio"])


def _protocolE_builder(p0, wall_class, s_rail, sigma):
    """Closure that grows the verdict arm on a Protocol-E box (any L). ★PR#796: the ToF-medium
    grow uses a fail-fast capped solve (PE_GROW_OUTER/PE_GROW_INNER_TOL) — DISCLOSED engineering
    choice: the ToF medium is a homogenized TANGENT operator, insensitive to the last
    outer/inner digits (verified: L=32 capped min_kse=0.34722 IDENTICAL to the frozen full
    1e-10/100-outer solve); the VERDICT K_tan solve keeps the frozen 1e-10."""
    def build(geom, free, xc):
        pos = geom[0]; N = pos.shape[0]
        L = int(round((pos.max(0) - pos.min(0)).mean())) + 1
        centers = cubic_cage_centers(L, PHI_SF_S, xc)
        k_a_bond, k_s_cold = cage_bond_stiffness(geom[3], geom[4], centers, PHI_SF_RCAGE,
                                                 CAGE_W, wall_class, s_rail, 0.0)
        k_a_bond = np.asarray(k_a_bond, float); k_s_cold = np.asarray(k_s_cold, float)
        b_src = radiation_source(pos, centers, p0, sigma, r_core=PHI_SF_RCAGE)
        sol = solve_state_dependent(geom, free, np.zeros((N, 3)), b_src, k_s_cold,
                                    k_a_bond=k_a_bond, inner_tol=PE_GROW_INNER_TOL,
                                    outer_max=PE_GROW_OUTER, inner_max=2000)
        return centers, k_a_bond, k_s_cold, sol["u"]
    return build


def measure_full_arm(geom, free, xc, half, arm, cP_cold, control_K, run_protocol_E,
                     protocolE_Ls=(32, 48)):
    """Full verdict measurement of ONE grown arm: hydro amplitude gate + K_tan/K_0 + G +
    K_ratio_lift + (Protocol E → r_Z at L∈{32,48}) + cell-walk bin.

    ★PR#796 F2: Protocol E is run at BOTH L=32 (with the SC method-band) and L=48; the headline
    r_Z is the launch@cP 'first-arrival' value at L=32. If the ToF is method-indeterminate (the
    r_Z band straddles >1 verdict bin) OR the mechanical bin FLIPS between L=32 and L=48, the
    ρ-correction cannot decide the bin — it is routed to the structural anchor r_Z=√K_ratio and
    the disposition is UNDETERMINED (frozen §9 verdict-controlling-flip / straddle rule)."""
    mK = measure_K_ratio(geom, free, arm, xc, half, "hydro", robustness=True)
    # G_eff/G_0 (shear central diff, corroborative)
    mG = measure_K_ratio(geom, free, arm, xc, half, "shear", robustness=False)
    K_ratio = mK["K_tan_over_K0"]
    lift = float(K_ratio / (control_K + 1e-300))
    gate_outcome = mK["gate"]["outcome"]
    r_Z_structural = float(np.sqrt(max(K_ratio, 0.0)))
    pe_by_L = {}
    if run_protocol_E and arm["grown_equilibrium_exists"]:
        for i, L in enumerate(protocolE_Ls):
            print(f"[protocol_E]   L={L} ...", flush=True)
            pe_by_L[L] = protocol_E(L, _protocolE_builder(arm["p0"], arm["wall_class"],
                                    VERDICT_S_RAIL, VERDICT_SRC_SIGMA), cP_cold, K_ratio,
                                    label=arm["seed_class"], do_sc=(i == 0))
        L0 = protocolE_Ls[0]
        r_Z_headline = pe_by_L[L0]["r_Z_launch_cP_headline"]
        # mechanical bin at each L (frozen table, gate (i) branch reads lift×r_Z)
        bins_by_L = {L: cell_walk_bin(gate_outcome, lift, pe_by_L[L]["r_Z_launch_cP_headline"])[0]
                     for L in protocolE_Ls}
        size_flip = bool(len({b for b in bins_by_L.values()}) > 1)
        method_indeterminate = bool(any(pe_by_L[L]["method_indeterminate"] for L in protocolE_Ls))
        # F2 disposition: a ToF that is method-indeterminate OR size-flips CANNOT move the bin
        # off the structural anchor → the r_Z that decides the headline bin is the structural
        # anchor (UNDETERMINED zone), the ToF band disclosed. Else use the measured headline r_Z.
        rz_decides = r_Z_structural if (method_indeterminate or size_flip) else r_Z_headline
        pe = {"by_L": pe_by_L, "r_Z_headline_launch_cP_L%d" % L0: r_Z_headline,
              "r_Z_structural_anchor": r_Z_structural,
              "bins_by_L_from_launch_cP": {str(L): b for L, b in bins_by_L.items()},
              "size_flip_L32_vs_L48": size_flip,
              "method_indeterminate_any_L": method_indeterminate,
              "rz_used_for_headline_bin": rz_decides,
              "rz_decider": ("structural_anchor (ToF method-indeterminate/size-flip)"
                             if (method_indeterminate or size_flip) else "launch_cP_measured")}
        r_Z = rz_decides
    else:
        pe = {"skipped": True, "rho_eff_over_rho0_assumed": 1.0,
              "note": "Protocol E not run for this arm; structural ρ_eff/ρ_0=1 assumed"}
        r_Z = r_Z_structural
    bin_name, gate_tag = cell_walk_bin(gate_outcome, lift, r_Z)
    return {
        "seed_class": arm["seed_class"], "p0": arm["p0"], "a_yield_scale": arm["a_yield_scale"],
        "phi_sf": arm["phi_sf"], "wall_class": arm["wall_class"],
        "grown_equilibrium_exists": arm["grown_equilibrium_exists"],
        "grown_CG_converged": arm["grown_CG_converged"],
        "grown_tension_nonzero": arm["grown_tension_nonzero"],
        "grown_bonds_positive": arm["grown_bonds_positive"],
        "max_abs_T": arm["max_abs_T"], "min_kse": arm["min_kse"], "peak_A": arm["peak_A"],
        "K_tan_over_K0_grown": K_ratio, "G_tan_over_G0_grown": mG["K_tan_over_K0"],
        "control_K_eff_over_K0": control_K, "K_ratio_lift": lift,
        "amplitude_gate": mK["gate"], "amplitude_gate_outcome": gate_outcome,
        "protocol_E": pe, "r_Z": r_Z, "r_Z_structural": r_Z_structural,
        "cell_walk_bin": bin_name, "gate_tag": gate_tag,
    }


def verdict_leg(cache, run_protocol_E=True, protocolE_Ls=(32, 48)):
    """The verdict arms (prereg §6): both seed_class values, the p_0 seed-independence
    sweep, the yield_saturated reservoir knob, the isotropic control, the PAINTED-
    ANISOTROPIC provenance-ablation arm, the ablation decomposition (PR#796 F6), the σ-variant
    arm (PR#796 F10), the C-V profile, percolation, anti-seduction."""
    geom = cache[16]
    xc, free, half = _setup(geom)
    cP, cS, _ = run_c2_speeds(RHO_STAR, K_S)
    control_K = isotropic_control_K(geom, xc)
    out = {"isotropic_control_K_eff_over_K0": control_K,
           "note_control": "#782 bulk_only-cold cage at φ_sf (Rule-14; reproduces #782 0.296)"}

    # ── fixed_budget headline (p_ref) + full measurement ──
    print("[verdict] fixed_budget headline (p_ref) ...", flush=True)
    arm = grow_verdict_arm(geom, free, xc, VERDICT_P_REF, "fixed_budget")
    head = measure_full_arm(geom, free, xc, half, arm, cP, control_K, run_protocol_E, protocolE_Ls)
    out["fixed_budget_headline"] = head
    # C-V + percolation + painted + ablation decomposition only if a stable grown equilibrium exists
    if arm["grown_equilibrium_exists"]:
        print("[verdict]   C-V profile ...", flush=True)
        out["cv_profile_fixed_budget"] = cv_profile(geom, free, arm, xc, half)
        out["percolation_fixed_budget"] = percolation(geom, arm)
        print("[verdict]   painted-anisotropic ablation ...", flush=True)
        out["painted_anisotropic_fixed_budget"] = painted_anisotropic_arm(geom, free, arm, xc, half)
        print("[verdict]   ablation decomposition (F6 cancellation-mechanism test) ...", flush=True)
        out["ablation_decomposition_fixed_budget"] = ablation_decomposition(
            geom, free, arm, xc, half, control_K)

    # ── σ-variant arm (PR#796 F10/F14 — VERDICT_SRC_SIGMA is a verdict-adjacent knob) ──
    print("[verdict] σ-variant arm ...", flush=True)
    arm_sig = grow_verdict_arm(geom, free, xc, VERDICT_P_REF, "fixed_budget",
                               sigma=VERDICT_SRC_SIGMA_VARIANT)
    mK_sig = measure_K_ratio(geom, free, arm_sig, xc, half, "hydro", robustness=False)
    lift_sig = float(mK_sig["K_tan_over_K0"] / (control_K + 1e-300))
    rz_sig_struct = float(np.sqrt(max(mK_sig["K_tan_over_K0"], 0.0)))
    bin_sig, _ = cell_walk_bin(mK_sig["gate"]["outcome"], lift_sig, rz_sig_struct)
    bin_head_struct, _ = cell_walk_bin(head["amplitude_gate_outcome"],
                                       head["K_ratio_lift"], head["r_Z_structural"])
    out["sigma_variant_arm"] = {
        "sigma_headline": VERDICT_SRC_SIGMA, "sigma_variant": VERDICT_SRC_SIGMA_VARIANT,
        "grown_equilibrium_exists": arm_sig["grown_equilibrium_exists"],
        "max_abs_T": arm_sig["max_abs_T"], "min_kse": arm_sig["min_kse"],
        "K_tan_over_K0": mK_sig["K_tan_over_K0"], "K_ratio_lift": lift_sig,
        "r_Z_structural": rz_sig_struct, "gate_outcome": mK_sig["gate"]["outcome"],
        "bin_from_structural_rZ": bin_sig,
        "headline_bin_from_structural_rZ": bin_head_struct,
        "verdict_relevant_flip": bool(bin_sig != bin_head_struct),
        "note": "VERDICT_SRC_SIGMA is a DISCLOSED [engineering-choice] knob (per-core source "
                "width, confined to r<r_core). This variant tests whether the headline bin is "
                "σ-sensitive; a bin flip ⇒ verdict-relevant ⇒ route to Grant."}

    # ── fixed_budget seed-independence sweep {0.25,0.5,1.0}·p_ref ──
    print("[verdict] fixed_budget seed sweep ...", flush=True)
    sweep = {}
    for frac in P0_SWEEP_FRACS:
        a = grow_verdict_arm(geom, free, xc, VERDICT_P_REF * frac, "fixed_budget")
        mK = measure_K_ratio(geom, free, a, xc, half, "hydro", robustness=False)
        lift = float(mK["K_tan_over_K0"] / (control_K + 1e-300))
        rz = float(np.sqrt(max(mK["K_tan_over_K0"], 0.0)))   # structural ρ for the sweep stability check
        sweep[f"{frac:g}xp_ref"] = {
            "p0": a["p0"], "grown_equilibrium_exists": a["grown_equilibrium_exists"],
            "grown_tension_nonzero": a["grown_tension_nonzero"], "max_abs_T": a["max_abs_T"],
            "K_tan_over_K0": mK["K_tan_over_K0"], "K_ratio_lift": lift,
            "r_Z_structural": rz, "gate_outcome": mK["gate"]["outcome"]}
    out["fixed_budget_seed_sweep"] = sweep
    lifts = [v["K_ratio_lift"] for v in sweep.values()]
    rzs = [v["r_Z_structural"] for v in sweep.values()]
    out["seed_independence_fixed_budget"] = {
        "lift_rel_spread": float((max(lifts) - min(lifts)) / (np.mean(lifts) + 1e-30)),
        "rZ_rel_spread": float((max(rzs) - min(rzs)) / (np.mean(rzs) + 1e-30)),
        "stable_tol_0p15": bool((max(lifts) - min(lifts)) / (np.mean(lifts) + 1e-30) <= 0.15
                                and (max(rzs) - min(rzs)) / (np.mean(rzs) + 1e-30) <= 0.15)}

    # ── yield_saturated arms (the headline arm IF equilibrium exists) + reservoir knob ──
    print("[verdict] yield_saturated reservoir knob ...", flush=True)
    ys = {}
    for ays in A_YIELD_SCALE_SWEEP:
        a = grow_verdict_arm(geom, free, xc, None, "yield_saturated", a_yield_scale=ays)
        entry = {"p0_grown": a["p0"], "a_yield_scale": ays, "peak_A": a["peak_A"],
                 "peak_A_ceiling": a["peak_A_ceiling"], "yield_reached": a["yield_reached"],
                 "A_yield_target": A_YIELD * ays,
                 "grown_equilibrium_exists": a["grown_equilibrium_exists"],
                 "grown_CG_converged": a["grown_CG_converged"],
                 "grown_bonds_positive": a["grown_bonds_positive"],
                 "grown_tension_nonzero": a["grown_tension_nonzero"], "min_kse": a["min_kse"],
                 "yield_scan": a["yield_scan"]}   # OBSERVED buckling onset (PR#796 F11)
        if a["grown_equilibrium_exists"]:
            mK = measure_K_ratio(geom, free, a, xc, half, "hydro", robustness=False)
            entry["K_tan_over_K0"] = mK["K_tan_over_K0"]
            entry["K_ratio_lift"] = float(mK["K_tan_over_K0"] / (control_K + 1e-300))
            entry["r_Z_structural"] = float(np.sqrt(max(mK["K_tan_over_K0"], 0.0)))
            entry["gate_outcome"] = mK["gate"]["outcome"]
        ys[f"A_yield_scale_{ays:g}"] = entry
    out["yield_saturated_reservoir_knob"] = ys
    out["yield_saturated_equilibrium_exists_any"] = bool(
        any(v["grown_equilibrium_exists"] for v in ys.values()))

    # ── headline selection (§9 Fork SEED) ──
    ys_exists = out["yield_saturated_equilibrium_exists_any"]
    if ys_exists:
        headline_arm = "yield_saturated"
    else:
        headline_arm = "fixed_budget"
    out["headline_arm_selected"] = headline_arm
    out["headline_bin"] = (head["cell_walk_bin"] if headline_arm == "fixed_budget"
                           else "see yield_saturated_reservoir_knob")

    # ── anti-seduction fence (§6) — matched-ish r_Z is CANDIDATE only ──
    r_Z = head["r_Z"]
    matched_ish = bool(0.8 <= r_Z <= 1.25)
    out["anti_seduction_fence"] = {
        "headline_r_Z": r_Z, "matched_ish_0p8_1p25": matched_ish,
        "seed_independence_passes": out["seed_independence_fixed_budget"]["stable_tol_0p15"],
        "disposition": ("CANDIDATE-only, EXCLUDED from headline (routes to Grant)"
                        if matched_ish else "not matched-ish; no candidate flag"),
        "frozen_rule": "a matched-ish r_Z fed by a single source reservoir is a CANDIDATE "
                       "ONLY, excluded from the headline verdict regardless of arm"}
    return out


# ═════════════════════════════════════════════════════════════════════════════
# MAIN — leg dispatch
# ═════════════════════════════════════════════════════════════════════════════
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--legs", default="0", help="comma list: 0 (self-test+validation), "
                    "verdict, all")
    ap.add_argument("--out", default=str(Path(__file__).with_name("vessel_state_rve_results.json")))
    ap.add_argument("--protocolE-Ls", default="32,48",
                    help="comma list of Protocol E box sizes (frozen §4 L∈{32,48})")
    ap.add_argument("--no-protocolE", action="store_true")
    args = ap.parse_args()
    legs = set(args.legs.split(","))
    protocolE_Ls = tuple(int(s) for s in args.protocolE_Ls.split(","))

    t0 = time.time()
    cache = _geom_cache()
    cP, cS, _ = run_c2_speeds(RHO_STAR, K_S)
    out = {
        "provenance": {
            "class": "vessel-state RVE bench (walk-1 instrument, #792-extends-#782); "
                     "state-dependent geometric-stiffness operator; grown-from-imposed-"
                     "source; grade-frame Eulerian/imposed; engine byte-untouched; "
                     "mints no clm-/def-; deterministic (run_c2_speeds seed=1, no per-step RNG).",
            "prereg_file": "research/2026-07-22_vessel-state-rve_prereg-FROZEN.md",
            "grade_frame_disclosure": "grade-frame: Eulerian, imposed (not self-bound; the "
                     "engine hosts no field-generated co-moving grade)",
            "source_disclosure": "source imposed (radiation-stress surrogate body-force "
                     "∝⟨A²⟩); stress state emergent through the nonlinear force balance",
            "constants": {"k_a_RHO_STAR": K_A, "k_s_KS0": KS0, "A_YIELD": A_YIELD,
                          "ELL_SRS_NN": ELL, "p_ref_verdict": VERDICT_P_REF},
        },
        "spectral_cold": {"cP": cP, "cS": cS, "cP_over_cS": cP / cS},
        "cell_walk_partition_proof": assert_partition(),
    }

    if "0" in legs or "all" in legs:
        print("[leg0] gate-fireability self-tests ...", flush=True)
        out["leg0_selftests"] = leg0_selftests(cache)
        gp = out["leg0_selftests"]["gate_fireability_selftest_pass"]
        print(f"[leg0]   gate_fireability_selftest_pass = {gp}", flush=True)
        print("[leg0] instrument validation ...", flush=True)
        out["leg0_instrument_validation"] = leg0_instrument_validation(cache)
        out["leg0_VOID"] = bool(not gp)
        if not gp:
            print("[leg0] ★VOID — self-tests did not force their targets; STOP.", flush=True)
            out["_runtime_sec"] = time.time() - t0
            Path(args.out).write_text(json.dumps(out, indent=2, default=float))
            return out

    if "verdict" in legs or "all" in legs:
        out["verdict"] = verdict_leg(cache, run_protocol_E=not args.no_protocolE,
                                     protocolE_Ls=protocolE_Ls)
        hb = out["verdict"].get("headline_bin")
        print(f"[verdict]   headline_arm={out['verdict']['headline_arm_selected']} "
              f"headline_bin={hb}", flush=True)

    # ── determinism digest (PR#796 F5/F13) — a content hash over the results EXCLUDING the
    # wall-clock timing + the digest itself. Two INDEPENDENT full driver runs producing the
    # SAME digest IS the frozen 'two independent full driver runs diff -q clean' criterion
    # (the shipped in-process bit-compare is a PROXY; this is the frozen full-run check).
    digest_payload = {k: v for k, v in out.items() if k not in ("_runtime_sec", "determinism_digest")}
    out["determinism_digest"] = hashlib.sha256(
        json.dumps(digest_payload, sort_keys=True, default=float).encode()).hexdigest()
    out["_runtime_sec"] = time.time() - t0
    Path(args.out).write_text(json.dumps(out, indent=2, default=float))
    print(f"[done] wrote {args.out}  ({out['_runtime_sec']:.0f}s)  "
          f"determinism_digest={out['determinism_digest'][:16]}…", flush=True)
    return out


if __name__ == "__main__":
    main()
