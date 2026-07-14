#!/usr/bin/env python3
"""
QED-TRACE MANY-BODY SCREENING-SUM GATE — the residual classical route to QED's log.
===================================================================================

FROZEN prereg (pushed before this ran):
    research/2026-07-14_screening-sum-gate_prereg_FROZEN.md

THE ONE QUESTION: does the SELF-CONSISTENT many-body screening SUM — the
intervening lattice cells between two seeded windings, EACH polarizing in the
TOTAL field (probe field PLUS every other cell's induced polarization: the
Clausius-Mossotti / self-consistent-screening ladder), kernel-ON — produce
NON-POWER-LAW (logarithmic) scale dependence in the TRANSFER coupling, where the
beta gate's PAIRWISE dress (research/2026-07-14_qed-trace-beta-gate_RESULT.md,
bin WRONG-FORM) gave a pure power law?

This is the route the beta gate left EXPLICITLY OPEN (RESULT §7): "the gate
computed the two-body saturation-dressed force; it never computed the lattice's
many-body screening SUM between the two probes ... UNPROBED, NOT CLOSED."

WHY IT CAN DIFFER FROM THE PAIRWISE DRESS: the many-body dipole-dipole coupling
carries a 1/r^3 kernel whose spherical-shell integral int 4*pi*r^2 dr / r^3 =
4*pi*int dr/r is LOGARITHMIC, IF the self-consistently-induced dipole density is
scale-invariant. The pairwise dress has NO inter-cell coupling and structurally
cannot carry this. A-priori expectation: GENUINELY UNKNOWN (prereg §1) — a LOG =
the QED-TRACE program's chord; a clean WRONG-FORM completes the category closure.

★ TRANSFER-REGISTER REQUIREMENT (inherited from the beta gate, load-bearing):
alpha_eff is binned on the TRANSFER register (force between the two probes through
the medium); the REACTIVE (stored-energy) register is reported KEEP-BOTH.

★ TWO GENUINENESS KNIVES gate any non-null verdict as many-body vs
RELABELED-PAIRWISE: (A) Born-vs-converged (self-consistency must change the
result); (B) remove-intermediate-cells (the intervening medium must carry it).

Sector header — MODE static two-body TRANSFER coupling through a self-consistent
polarizable medium; REGIME cold, KERNEL ON (Op14/Ax4 saturation sets per-cell
polarizability) with a kernel-OFF (alpha0=0) null; PHASE-STATE sub-yield
perturbative (bridge A<<1; near-saturated small-R excluded = Pauli-wall analog);
SECTOR graded-Coulomb screening cloud of induced cell dipoles = the
vacuum-polarization cloud.  No new ENGINE — a static electrostatic SCF solve over
Op14-graded polarizable cells.

Run:  PYTHONPATH=src python src/scripts/vol_2_subatomic/qed_trace_screening_sum_gate.py
Fast smoke (fewer scales / cells):  ... --smoke
"""
from __future__ import annotations

import argparse
import json

import numpy as np
from scipy.spatial import cKDTree

from ave.core.constants import ALPHA
from ave_path_util import sim_output

# reuse the beta gate's PROVEN fitter + machine gates (no re-implementation)
from scripts.vol_2_subatomic.qed_trace_beta_gate import (
    fit_log_vs_power,
    gate_plant_log,
    gate_plant_pow,
    gate_separability,
)

# ── native units + FROZEN parameters (prereg §5) ─────────────────────────────
K = 1.0            # bare probe coupling (native; FORM/sign is K-independent)
D_SAT = 1.0        # saturation radius (native yield scale)
ALPHA0 = 0.03      # medium polarizability density (FIREWALLED off FORM; swept for robustness)
DAMP = 0.4         # SCF outer under-relaxation (frozen)
TOL = 1e-8         # SCF convergence: rel alpha-change (frozen)
MAXITER = 400      # SCF max outer iters (frozen)
N_R = 16           # log-radial shells per probe (frozen)
N_ANG = 24         # Fibonacci-sphere directions per shell (frozen)
R_MAX_FAC = 1.2    # cloud outer radius = R_MAX_FAC * R (frozen)
R_MIN_FAC = 1.05   # innermost shell radius = R_MIN_FAC * d_sat (frozen)
MIN_SEP_FRAC = 0.25  # greedy dedup: drop cells nearer than this * local spacing (frozen)
R_SOFT_FRAC = 0.3  # dipole-kernel softening = this * local cell length (frozen, lattice discreteness)
N_ORIENT = 8       # orientation-average count (prereg AMEND A1: suppresses the DETERMINISTIC
                   # angular-discretization noise; verdict-neutral — see amendment)
ORIENT_SEED = 20260714  # reproducible SO(3) orientation seed

# perturbative SEPARATION window (the QED-running analog on the separation axis);
# small-R near-saturated bridge = non-perturbative Pauli-wall analog, EXCLUDED.
R_LO, R_HI, N_SCALE = 30.0, 3000.0, 16   # 2.0 decades


def _rand_rot(rng: np.random.Generator) -> np.ndarray:
    """Uniform-ish SO(3) rotation via QR of a Gaussian matrix (det=+1)."""
    Q, Rm = np.linalg.qr(rng.standard_normal((3, 3)))
    Q = Q * np.sign(np.diag(Rm))
    if np.linalg.det(Q) < 0:
        Q[:, 0] = -Q[:, 0]
    return Q


# ═════════════════════════════════════════════════════════════════════════════
# CELL MESH — two per-probe log-radial Fibonacci clouds, deduped, wall-excluded
# ═════════════════════════════════════════════════════════════════════════════
def _fib_sphere(n: int) -> np.ndarray:
    """ANTIPODAL-SYMMETRIC Fibonacci directions (n even): n//2 Fibonacci points +
    their antipodes. Antipodal symmetry makes probe-i's ISOTROPIC self-cloud exert
    EXACTLY zero net axial force (each radial dipole's force cancelled by its
    antipode's), so the interaction-force extraction is not contaminated by an
    angular-discretization self-force residual (prereg AMENDMENT A1)."""
    m = n // 2
    i = np.arange(m) + 0.5
    phi = np.arccos(1.0 - 2.0 * i / m)
    theta = np.pi * (1.0 + 5.0 ** 0.5) * i
    half = np.stack([np.sin(phi) * np.cos(theta),
                     np.sin(phi) * np.sin(theta), np.cos(phi)], axis=1)
    return np.concatenate([half, -half], axis=0)


def build_cells(R: float, n_r: int = N_R, n_ang: int = N_ANG,
                rot: np.ndarray | None = None) -> dict:
    """Union of two per-probe log-radial spherical clouds (probes at +-R/2 z).
    Cells within d_sat of EITHER probe excluded (Pauli wall). Near-coincident
    cells (from the two overlapping clouds in the bridge) removed by greedy dedup.
    `rot` (3x3): optional rotation of the angular pattern (for orientation-averaging,
    which suppresses the deterministic angular-discretization noise; prereg AMEND A1).
    Returns cells (M,3), vols (M,), spac (M,) local cell length."""
    centers = np.array([[0.0, 0.0, -R / 2.0], [0.0, 0.0, +R / 2.0]])
    dirs = _fib_sphere(n_ang)
    if rot is not None:
        dirs = dirs @ rot.T
    r_edges = np.geomspace(R_MIN_FAC * D_SAT, R_MAX_FAC * R, n_r + 1)
    r_mid = np.sqrt(r_edges[:-1] * r_edges[1:])
    dr = np.diff(r_edges)
    cells, vols, spac = [], [], []
    for c in centers:
        for rk, drk in zip(r_mid, dr):
            cells.append(c[None, :] + rk * dirs)
            v = (4.0 * np.pi * rk ** 2 * drk) / n_ang
            vols.append(np.full(n_ang, v))
            spac.append(np.full(n_ang, v ** (1.0 / 3.0)))
    cells = np.concatenate(cells, 0)
    vols = np.concatenate(vols, 0)
    spac = np.concatenate(spac, 0)
    d1 = np.linalg.norm(cells - centers[0], axis=1)
    d2 = np.linalg.norm(cells - centers[1], axis=1)
    keep = (d1 > D_SAT) & (d2 > D_SAT)
    cells, vols, spac = cells[keep], vols[keep], spac[keep]
    # greedy dedup, near-probe cells kept first (they carry the strongest cloud)
    order = np.argsort(np.minimum(d1[keep], d2[keep]))
    cells, vols, spac = cells[order], vols[order], spac[order]
    tree = cKDTree(cells)
    pairs = tree.query_pairs(r=float(MIN_SEP_FRAC * np.median(spac)), output_type="ndarray")
    drop = np.zeros(len(cells), dtype=bool)
    for i, j in pairs:  # i<j and i is nearer-probe (order sorted) -> drop the farther j
        if not drop[i]:
            drop[j] = True
    kept = ~drop
    return {"cells": cells[kept], "vols": vols[kept], "spac": spac[kept], "centers": centers}


def _probe_field(cells: np.ndarray, centers: np.ndarray, q=(1.0, 1.0)) -> np.ndarray:
    E = np.zeros((len(cells), 3))
    for c, qc in zip(centers, q):
        d = cells - c
        r = np.linalg.norm(d, axis=1)
        E += qc * d / r[:, None] ** 3
    return E


def _dipole_matrix(cells: np.ndarray, r_soft: np.ndarray) -> np.ndarray:
    """M[i,j] (3x3): field at i from unit dipole at j, softened at the cell scale.
    Diagonal (self) blocks zero."""
    d = cells[:, None, :] - cells[None, :, :]
    r2 = np.sum(d * d, axis=2) + r_soft[:, None] ** 2
    r = np.sqrt(r2)
    np.fill_diagonal(r, np.inf)
    nhat = d / r[:, :, None]
    outer = nhat[:, :, :, None] * nhat[:, :, None, :]
    return (3.0 * outer - np.eye(3)[None, None]) / r[:, :, None, None] ** 3


# ═════════════════════════════════════════════════════════════════════════════
# SELF-CONSISTENT SOLVE — inner exact dipole-dipole; outer saturation SCF
# ═════════════════════════════════════════════════════════════════════════════
def _chi_sat(A: np.ndarray) -> np.ndarray:
    """Op14 capacitive/saturation grade excess: chi = C_eff/C0 - 1 = 1/sqrt(1-A^2)-1."""
    return 1.0 / np.sqrt(1.0 - np.clip(A, 0.0, 1.0 - 1e-9) ** 2) - 1.0


def _chi_lin(A: np.ndarray) -> np.ndarray:
    """Leading un-saturated grade (the reactive-register linear reference): A^2/2."""
    return 0.5 * A ** 2


def solve(mesh: dict, R: float, alpha0: float, *, linear: bool = False,
          born: bool = False, mask: np.ndarray | None = None, q=(1.0, 1.0),
          tol: float = TOL, maxiter: int = MAXITER, damp: float = DAMP) -> dict:
    """SCF dipole-lattice solve.
      linear=True -> use chi_lin (reactive-register reference).
      born=True   -> Born/first-order: dipoles respond to the PROBE field ONLY
                     (inter-cell coupling M OFF in the p-equation) — the
                     self-consistency knife's comparator.
      mask        -> boolean keep-cells (for bridge-removal knife).
      q           -> probe charges (q=(1,0) isolates probe-1's self-cloud for the
                     interaction-force subtraction)."""
    cells, vols, spac, centers = mesh["cells"], mesh["vols"], mesh["spac"], mesh["centers"]
    if mask is not None:
        cells, vols, spac = cells[mask], vols[mask], spac[mask]
    N = len(cells)
    E_pr = _probe_field(cells, centers, q=q)
    r_soft = R_SOFT_FRAC * spac
    M = _dipole_matrix(cells, r_soft)
    Mf = M.transpose(0, 2, 1, 3).reshape(3 * N, 3 * N)
    Epr_f = E_pr.reshape(3 * N)
    E_yield = K / D_SAT ** 2
    chi_fn = _chi_lin if linear else _chi_sat
    I3N = np.eye(3 * N)
    alpha_i = np.zeros(N)
    conv = False
    it = 0
    for it in range(maxiter):
        Dvec = np.repeat(alpha_i, 3)
        if born:
            pf = Dvec * Epr_f                      # dipoles see probe field only
        else:
            pf = np.linalg.solve(I3N - Dvec[:, None] * Mf, Dvec * Epr_f)
        p = pf.reshape(N, 3)
        if born:
            E = E_pr.copy()                        # strain from probe field only
        else:
            E = E_pr + np.einsum("ijab,jb->ia", M, p)
        A = np.linalg.norm(E, axis=1) / E_yield
        alpha_new = alpha0 * chi_fn(A) * vols
        rel = np.linalg.norm(alpha_new - alpha_i) / (np.linalg.norm(alpha_new) + 1e-30)
        alpha_i = (1.0 - damp) * alpha_i + damp * alpha_new
        if it > 0 and rel < tol:
            conv = True
            break
    W = 0.5 * float(np.sum(p * E))                 # stored polarization energy
    return {"cells": cells, "p": p, "E": E, "spac": spac, "iters": it + 1,
            "converged": conv, "W": W}


def _dip_force_z(sol: dict, R: float) -> float:
    """Axial (z) force on probe-1 (at -R/2, q1=+1) from ALL induced dipoles."""
    cells, p, spac = sol["cells"], sol["p"], sol["spac"]
    c1 = np.array([0.0, 0.0, -R / 2.0])
    d = c1[None, :] - cells
    r_soft = R_SOFT_FRAC * spac
    r = np.sqrt(np.sum(d * d, axis=1) + r_soft ** 2)
    nhat = d / r[:, None]
    E_dip = (3.0 * np.sum(p * nhat, axis=1)[:, None] * nhat - p) / r[:, None] ** 3
    return float(np.sum(E_dip[:, 2]))


def transfer_alpha(mesh: dict, R: float, alpha0: float, *, born: bool = False,
                   mask: np.ndarray | None = None):
    """alpha_eff^transfer = [F_bare + F_dip(both) - F_dip(probe-1 alone)] / F_bare.

    The interaction force is isolated by SUBTRACTING probe-1's OWN self-cloud force
    (the q=(1,0) solve): the raw axial force on probe-1 is dominated by an unphysical
    self-force (probe-1's ~isotropic cloud that does not perfectly angularly cancel,
    R-independent), which would blow up when divided by the tiny bare force 1/R^2.
    F(both)-F(probe-1 alone) = the force attributable to probe-2 being present = the
    physical screened interaction force. Far field -> F_dip(both)->F_dip(self) -> 1."""
    sol_both = solve(mesh, R, alpha0, born=born, mask=mask, q=(1.0, 1.0))
    sol_self = solve(mesh, R, alpha0, born=born, mask=mask, q=(1.0, 0.0))
    Fbare = -1.0 / R ** 2
    a = (Fbare + _dip_force_z(sol_both, R) - _dip_force_z(sol_self, R)) / Fbare
    return a, sol_both


# ═════════════════════════════════════════════════════════════════════════════
# PRIMARY SWEEP — transfer + reactive, both registers, >=2 decades
# ═════════════════════════════════════════════════════════════════════════════
def _sweep_point(R: float, alpha0: float, n_orient: int, rng: np.random.Generator) -> dict:
    """Orientation-averaged transfer / born-transfer / reactive at one separation R.
    Averaging over random SO(3) orientations of the angular mesh pattern suppresses
    the deterministic angular-discretization noise (prereg AMEND A1)."""
    tr, born, Wsat, Wlin, iters = [], [], [], [], []
    conv = True
    for _ in range(n_orient):
        rot = _rand_rot(rng)
        mesh = build_cells(R, rot=rot)
        a_tr, sol = transfer_alpha(mesh, R, alpha0)
        a_bn, _ = transfer_alpha(mesh, R, alpha0, born=True)
        sol_lin = solve(mesh, R, alpha0, linear=True)
        tr.append(a_tr); born.append(a_bn); Wsat.append(sol["W"]); Wlin.append(sol_lin["W"])
        iters.append(sol["iters"])
        conv = conv and sol["converged"] and sol_lin["converged"]
    return {"tr": float(np.mean(tr)), "born": float(np.mean(born)),
            "re": float(np.mean(Wsat) / np.mean(Wlin)), "tr_std": float(np.std(tr)),
            "iters": int(np.mean(iters)), "conv": conv}


def primary_sweep(alpha0: float = ALPHA0, n_scale: int = N_SCALE,
                  n_orient: int = N_ORIENT) -> dict:
    r = np.geomspace(R_LO, R_HI, n_scale)
    rng = np.random.default_rng(ORIENT_SEED)
    tr, re, born_tr, tr_std = [], [], [], []
    iters, nonconv = [], []
    for R in r:
        pt = _sweep_point(R, alpha0, n_orient, rng)
        tr.append(pt["tr"]); born_tr.append(pt["born"]); re.append(pt["re"])
        tr_std.append(pt["tr_std"]); iters.append(pt["iters"])
        if not pt["conv"]:
            nonconv.append(float(R))
    tr = np.array(tr)
    born_tr = np.array(born_tr)
    re = np.array(re)                               # reactive register: saturated/linear stored energy
    fit_tr = fit_log_vs_power(r, tr)
    fit_re = fit_log_vs_power(r, re)
    fit_born = fit_log_vs_power(r, born_tr)
    decades = float(np.log10(R_HI / R_LO))
    table = [{"R_over_dsat": float(Ri), "log10_energy_proxy": float(np.log10(D_SAT / Ri)),
              "alpha_transfer": float(t), "inv_alpha_transfer": (float(1.0 / t) if t != 0 else None),
              "alpha_reactive": float(x), "alpha_transfer_BORN": float(b),
              "transfer_orient_std": float(s), "scf_iters": int(nit)}
             for Ri, t, x, b, s, nit in zip(r, tr, re, born_tr, tr_std, iters)]
    return {"scale_decades_covered": decades, "n_points": n_scale, "alpha0": alpha0,
            "n_orient": n_orient, "R_window": [R_LO, R_HI], "nonconverged_scales": nonconv,
            "fit_transfer": fit_tr, "fit_reactive": fit_re, "fit_transfer_BORN": fit_born,
            "alpha_table": table,
            "_arrays": {"r": r, "tr": tr, "re": re, "born_tr": born_tr}}


# ═════════════════════════════════════════════════════════════════════════════
# GENUINENESS KNIFE A — Born vs converged (self-consistency must change the result)
# ═════════════════════════════════════════════════════════════════════════════
def genuineness_born_vs_converged(sweep: dict) -> dict:
    tr = sweep["_arrays"]["tr"]
    born = sweep["_arrays"]["born_tr"]
    dep_conv = tr - 1.0
    dep_born = born - 1.0
    # fractional change of the (departure-from-1) at every scale
    denom = np.where(np.abs(dep_conv) > 1e-300, np.abs(dep_conv), 1e-300)
    frac = np.abs(dep_conv - dep_born) / denom
    max_frac = float(np.max(frac))
    ft, fb = sweep["fit_transfer"], sweep["fit_transfer_BORN"]
    form_changes = ft["selected"] != fb["selected"]
    # coefficient change of the dominant model
    if ft["selected"] == "M_pow" and fb["selected"] == "M_pow":
        coeff_ratio = float(ft["M_pow"]["a"] / fb["M_pow"]["a"]) if fb["M_pow"]["a"] != 0 else None
        exp_shift = float(ft["M_pow"]["p_exponent"] - fb["M_pow"]["p_exponent"])
    else:
        coeff_ratio, exp_shift = None, None
    spectator = max_frac < 1e-6
    return {"max_frac_change_conv_vs_born": max_frac,
            "self_consistency_changes_form": bool(form_changes),
            "converged_selected": ft["selected"], "born_selected": fb["selected"],
            "pow_coeff_ratio_conv_over_born": coeff_ratio, "pow_exponent_shift": exp_shift,
            "self_consistency_is_spectator_RELABELED_PAIRWISE": bool(spectator),
            "G_genuineness_A_pass": bool(not spectator)}


# ═════════════════════════════════════════════════════════════════════════════
# GENUINENESS KNIFE B — remove intervening (bridge) cells; result must change
# ═════════════════════════════════════════════════════════════════════════════
def genuineness_bridge_removal(alpha0: float = ALPHA0,
                               ref_scales=(100.0, 1000.0),
                               n_orient: int = N_ORIENT) -> dict:
    rng = np.random.default_rng(ORIENT_SEED + 1)
    rows = []
    for R in ref_scales:
        a_full_l, a_nob_l, nbridge = [], [], []
        for _ in range(n_orient):
            mesh = build_cells(R, rot=_rand_rot(rng))
            cells = mesh["cells"]
            # "bridge" = cells between the probes: |z| < R/2 AND cylinder radius < R/2
            z = cells[:, 2]
            rho = np.sqrt(cells[:, 0] ** 2 + cells[:, 1] ** 2)
            bridge = (np.abs(z) < R / 2.0) & (rho < R / 2.0)
            a_f, _ = transfer_alpha(mesh, R, alpha0)
            a_n, _ = transfer_alpha(mesh, R, alpha0, mask=~bridge)
            a_full_l.append(a_f); a_nob_l.append(a_n); nbridge.append(int(np.sum(bridge)))
        a_full = float(np.mean(a_full_l))
        a_nob = float(np.mean(a_nob_l))
        dep_full = a_full - 1.0
        frac = abs((a_nob - a_full) / dep_full) if abs(dep_full) > 1e-300 else 0.0
        rows.append({"R": float(R), "n_bridge_cells": int(np.mean(nbridge)),
                     "alpha_transfer_full": a_full,
                     "alpha_transfer_no_bridge": a_nob,
                     "frac_change_from_removing_bridge": float(frac)})
    min_frac = min(r["frac_change_from_removing_bridge"] for r in rows)
    spectator = min_frac < 1e-6
    return {"per_scale": rows, "min_frac_change": float(min_frac),
            "intervening_medium_is_spectator_RELABELED_PAIRWISE": bool(spectator),
            "G_genuineness_B_pass": bool(not spectator)}


# ═════════════════════════════════════════════════════════════════════════════
# KERNEL-OFF NULL — alpha0=0 -> no dipoles -> alpha_eff == 1 (AMENDED amplitude axis)
# ═════════════════════════════════════════════════════════════════════════════
def kernel_off_control(n_scale: int = N_SCALE) -> dict:
    r = np.geomspace(R_LO, R_HI, n_scale)
    tr = []
    for R in r:
        mesh = build_cells(R)
        a, _ = transfer_alpha(mesh, R, 0.0)
        tr.append(a)
    tr = np.array(tr)
    max_dev = float(np.max(np.abs(tr - 1.0)))
    return {"max_transfer_departure": max_dev,
            "G_null_amplitude_pass": bool(max_dev < 1e-6),
            "note": "AMENDED amplitude criterion (the beta gate's frozen fit-based G-null was "
                    "design-defective: model-selection on ~1e-10 noise + unimplementable |p|>1e-6; "
                    "NOT repeated). alpha0=0 kills every dipole so the null is flat to machine eps."}


# ═════════════════════════════════════════════════════════════════════════════
# ALPHA0 FORM-ROBUSTNESS — the FORM verdict must be alpha0-independent
# ═════════════════════════════════════════════════════════════════════════════
def alpha0_robustness(alpha0_grid=(0.01, 0.03, 0.1, 0.2), n_scale: int = 8,
                      n_orient: int = 4) -> dict:
    rows = []
    for a0 in alpha0_grid:
        sw = primary_sweep(alpha0=a0, n_scale=n_scale, n_orient=n_orient)
        ft = sw["fit_transfer"]
        rows.append({"alpha0": a0, "transfer_selected": ft["selected"],
                     "dBIC": ft["dBIC_pow_minus_log"], "p_exponent": ft["M_pow"]["p_exponent"],
                     "grows_short": ft["alpha_grows_at_short_distance"],
                     "nonconverged": sw["nonconverged_scales"]})
    forms = {r["transfer_selected"] for r in rows}
    non_log = all(r["transfer_selected"] != "M_log" for r in rows)
    return {"per_alpha0": rows, "form_is_alpha0_independent": bool(len(forms) == 1),
            "no_log_at_any_alpha0": bool(non_log), "distinct_forms": sorted(forms)}


def window_robustness(n_orient: int = N_ORIENT) -> dict:
    """3-decade window (R/d_sat in [30, 30000]) — a wider-range separability robustness
    check (prereg AMEND A1): the FORM verdict must not depend on the 2-decade window."""
    rng = np.random.default_rng(ORIENT_SEED + 2)
    r = np.geomspace(30.0, 30000.0, 12)
    tr = []
    for R in r:
        pt = _sweep_point(R, ALPHA0, n_orient, rng)
        tr.append(pt["tr"])
    fit = fit_log_vs_power(r, np.array(tr))
    return {"decades": 3.0, "R_window": [30.0, 30000.0],
            "transfer_selected": fit["selected"], "dBIC_pow_minus_log": fit["dBIC_pow_minus_log"],
            "p_exponent": fit["M_pow"]["p_exponent"],
            "alpha_grows_at_short_distance": fit["alpha_grows_at_short_distance"],
            "transfer_departures": [float(x - 1.0) for x in tr]}


# ═════════════════════════════════════════════════════════════════════════════
# BINNING — the frozen 5-bin verdict, read on the TRANSFER register (+ genuineness)
# ═════════════════════════════════════════════════════════════════════════════
def classify(sweep: dict, gnull: dict, sep_2dec: dict,
             gen_a: dict, gen_b: dict) -> dict:
    ft, fr = sweep["fit_transfer"], sweep["fit_reactive"]
    transfer_weakens = ft["departure_at_r_lo"] < 0
    if sep_2dec["INCONCLUSIVE_RANGE_fires"]:
        bin_name = "INCONCLUSIVE-RANGE"
    elif ft["selected"] == "M_log" and ft["alpha_grows_at_short_distance"]:
        bin_name = "LOG-EMERGES"        # (coeff -> -alpha/3pi check is downstream)
    elif ft["selected"] == "M_log" and not ft["alpha_grows_at_short_distance"]:
        bin_name = "WRONG-SIGN"          # genuine log, wrong direction
    elif ft["selected"] == "M_pow":
        bin_name = "WRONG-FORM"
        bin_name += " (transfer sign also WRONG: alpha weakens at short distance)" if transfer_weakens else ""
    elif abs(ft["departure_at_r_lo"]) < 1e-6:
        bin_name = "NULL-FLAT"
    else:
        bin_name = "INCONCLUSIVE-RANGE"
    # genuineness overlay: a non-null verdict is only MANY-BODY if both knives pass
    many_body = gen_a["G_genuineness_A_pass"] and gen_b["G_genuineness_B_pass"]
    relabel = (not many_body) and bin_name not in ("NULL-FLAT", "INCONCLUSIVE-RANGE")
    return {
        "verdict_bin": bin_name,
        "read_on": "TRANSFER register (primary)",
        "transfer_selected": ft["selected"], "transfer_power_exponent": ft["M_pow"]["p_exponent"],
        "transfer_dBIC_pow_minus_log": ft["dBIC_pow_minus_log"],
        "transfer_sign_grows_short": ft["alpha_grows_at_short_distance"],
        "WRONG_SIGN_cofires_on_transfer": bool(transfer_weakens),
        "reactive_selected": fr["selected"], "reactive_power_exponent": fr["M_pow"]["p_exponent"],
        "reactive_sign_grows_short": fr["alpha_grows_at_short_distance"],
        "register_flip_observed": bool(ft["alpha_grows_at_short_distance"] !=
                                       fr["alpha_grows_at_short_distance"]),
        "many_body_genuine": bool(many_body),
        "RELABELED_PAIRWISE": bool(relabel),
        "genuineness_A_born_vs_converged_pass": gen_a["G_genuineness_A_pass"],
        "genuineness_B_bridge_removal_pass": gen_b["G_genuineness_B_pass"],
        "G_null_amplitude_pass": gnull["G_null_amplitude_pass"],
    }


# ═════════════════════════════════════════════════════════════════════════════
def main() -> dict:
    ap = argparse.ArgumentParser(description="QED-TRACE many-body screening-sum gate.")
    ap.add_argument("--smoke", action="store_true", help="fewer scales/robustness for a fast pass")
    ap.add_argument("--no-robustness", action="store_true", help="skip the alpha0 robustness sweep")
    args = ap.parse_args()
    n_scale = 8 if args.smoke else N_SCALE
    n_orient = 2 if args.smoke else N_ORIENT

    print(f"[screen-sum] primary sweep (both registers, {np.log10(R_HI/R_LO):.1f} decades, "
          f"alpha0={ALPHA0}, n_orient={n_orient}) ...", flush=True)
    sweep = primary_sweep(n_scale=n_scale, n_orient=n_orient)
    print(f"           transfer selected={sweep['fit_transfer']['selected']} "
          f"dBIC={sweep['fit_transfer']['dBIC_pow_minus_log']:.1f}", flush=True)

    print("[screen-sum] kernel-OFF null control ...", flush=True)
    gnull = kernel_off_control(n_scale=n_scale)

    print("[screen-sum] genuineness knife A (Born vs converged) ...", flush=True)
    gen_a = genuineness_born_vs_converged(sweep)
    print("[screen-sum] genuineness knife B (bridge removal) ...", flush=True)
    gen_b = genuineness_bridge_removal(ref_scales=(100.0, 1000.0), n_orient=n_orient)

    print("[screen-sum] machine gates (plant-log / plant-pow / separability) ...", flush=True)
    r_full = np.geomspace(R_LO, R_HI, n_scale)
    gates = {
        "G_plant_log": gate_plant_log(r_full),
        "G_plant_pow": gate_plant_pow(r_full),
        "G_separability_2dec": gate_separability(R_LO, R_HI),
    }

    robustness = None
    window_rob = None
    if not (args.smoke or args.no_robustness):
        print("[screen-sum] alpha0 form-robustness sweep ...", flush=True)
        robustness = alpha0_robustness(n_scale=6, n_orient=4)
        print("[screen-sum] 3-decade window-robustness ...", flush=True)
        window_rob = window_robustness(n_orient=6)

    verdict = classify(sweep, gnull, gates["G_separability_2dec"], gen_a, gen_b)

    # strip private arrays before serialising
    sweep_out = {k: v for k, v in sweep.items() if k != "_arrays"}
    result = {
        "prereg": "research/2026-07-14_screening-sum-gate_prereg_FROZEN.md",
        "program": "QED-TRACE many-body screening-sum gate",
        "constants": {"K": K, "d_sat": D_SAT, "alpha0": ALPHA0, "alpha_fs_CODATA": ALPHA,
                      "damp": DAMP, "tol": TOL, "n_r": N_R, "n_ang": N_ANG,
                      "R_window": [R_LO, R_HI], "n_scale": n_scale},
        "class": "CONSISTENCY / ECHO (charge-agnostic Op14 saturation grade); the earnable content "
                 "is the FORM/SIGN category answer of the MANY-BODY SUM, not a value",
        "primary_self_consistent_screening_sweep": sweep_out,
        "kernel_off_null_control": gnull,
        "genuineness_A_born_vs_converged": gen_a,
        "genuineness_B_bridge_removal": gen_b,
        "machine_gates": gates,
        "alpha0_robustness": robustness,
        "window_robustness_3dec": window_rob,
        "VERDICT": verdict,
    }
    out = sim_output("qed_trace_screening_sum_gate.json")
    out.write_text(json.dumps(result, indent=2))
    print("\n" + "=" * 72)
    print(f"  VERDICT: {verdict['verdict_bin']}")
    print(f"  transfer: selected={verdict['transfer_selected']} p={verdict['transfer_power_exponent']:.3f} "
          f"grows_short={verdict['transfer_sign_grows_short']} dBIC={verdict['transfer_dBIC_pow_minus_log']:.1f}")
    print(f"  reactive: selected={verdict['reactive_selected']} p={verdict['reactive_power_exponent']:.3f} "
          f"grows_short={verdict['reactive_sign_grows_short']}")
    print(f"  register_flip_observed={verdict['register_flip_observed']}")
    print(f"  MANY-BODY GENUINE={verdict['many_body_genuine']}  RELABELED_PAIRWISE={verdict['RELABELED_PAIRWISE']}")
    print(f"    knife A (Born!=conv): pass={gen_a['G_genuineness_A_pass']} "
          f"max_frac_change={gen_a['max_frac_change_conv_vs_born']:.3e} form_changes={gen_a['self_consistency_changes_form']}")
    print(f"    knife B (bridge-rm) : pass={gen_b['G_genuineness_B_pass']} min_frac_change={gen_b['min_frac_change']:.3e}")
    print(f"  G-null (amplitude): pass={gnull['G_null_amplitude_pass']} max_dev={gnull['max_transfer_departure']:.3e}")
    print(f"  G-plant-log: {gates['G_plant_log']['G_plant_log_pass']}  "
          f"G-plant-pow: {gates['G_plant_pow']['G_plant_pow_pass']}  "
          f"separability@2dec: {'PASS' if not gates['G_separability_2dec']['INCONCLUSIVE_RANGE_fires'] else 'INCONCLUSIVE'}")
    if sweep["nonconverged_scales"]:
        print(f"  ⚠ non-converged scales (excluded): {sweep['nonconverged_scales']}")
    if robustness:
        print(f"  alpha0-robustness: no_log_at_any_alpha0={robustness['no_log_at_any_alpha0']} "
              f"forms={robustness['distinct_forms']}")
    if window_rob:
        print(f"  3-decade window: selected={window_rob['transfer_selected']} "
              f"dBIC={window_rob['dBIC_pow_minus_log']:+.1f} p={window_rob['p_exponent']:.3f}")
    print("=" * 72)
    print(f"[screen-sum] wrote {out}")
    _figure(result, sweep["_arrays"])
    return result


def _figure(result, arrays):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    from ave.viz import style
    style.apply()

    r, tr, re, born = arrays["r"], arrays["tr"], arrays["re"], arrays["born_tr"]
    q = D_SAT / r  # energy proxy (larger = shorter separation)
    ft = result["primary_self_consistent_screening_sweep"]["fit_transfer"]
    verdict = result["VERDICT"]

    fig, ax = plt.subplots(1, 2, figsize=(11.5, 4.6))
    ax[0].loglog(q, np.abs(tr - 1.0), "o-", color="#0072B2",
                 label="TRANSFER |alpha_eff-1| (self-consistent)")
    ax[0].loglog(q, np.abs(born - 1.0), "^--", color="#56B4E9", alpha=0.8,
                 label="TRANSFER Born (self-consistency OFF)")
    ax[0].loglog(q, np.abs(re - 1.0), "s-", color="#D55E00",
                 label="REACTIVE |alpha_eff-1| (stored energy)")
    ax[0].loglog(q, np.abs(ft["M_pow"]["a"]) * q ** ft["M_pow"]["p_exponent"], ":",
                 color="#0072B2", alpha=0.6, label=f"transfer power fit p={ft['M_pow']['p_exponent']:.2f}")
    ax[0].set_xlabel(r"$d_{\mathrm{sat}}/R$   (energy proxy; larger = shorter separation)")
    ax[0].set_ylabel(r"$|\alpha_{\mathrm{eff}}-1|$")
    ax[0].set_title("Many-body screening: straight log-log = POWER LAW; curve = LOG", fontsize=9)
    ax[0].legend(fontsize=7, loc="best")

    lnq = np.log(q)
    ax[1].plot(lnq, 1.0 / tr, "o-", color="#0072B2", label="TRANSFER 1/alpha_eff (self-consistent)")
    ax[1].plot(lnq, 1.0 / born, "^--", color="#56B4E9", alpha=0.8, label="TRANSFER 1/alpha_eff Born")
    ax[1].axhline(1.0, color="0.5", ls=":", lw=1.0, label="bare (kernel-OFF null, flat)")
    ax[1].set_xlabel(r"$\ln(d_{\mathrm{sat}}/R)$   (increasing energy $\rightarrow$)")
    ax[1].set_ylabel(r"$1/\alpha_{\mathrm{eff}}$")
    ax[1].set_title(f"verdict: {verdict['verdict_bin']}", fontsize=9)
    ax[1].legend(fontsize=7, loc="best")
    txt = (f"MANY-BODY GENUINE: {verdict['many_body_genuine']}\n"
           f"knife A (Born!=conv): {verdict['genuineness_A_born_vs_converged_pass']}\n"
           f"knife B (bridge-rm): {verdict['genuineness_B_bridge_removal_pass']}")
    ax[1].text(0.02, 0.02, txt, transform=ax[1].transAxes, fontsize=7.5, va="bottom",
               bbox=dict(boxstyle="round", fc="white", ec="#999999", alpha=0.9))
    fig.suptitle("QED-TRACE many-body screening-sum gate: self-consistent polarizable-cell "
                 "screening between two windings", fontsize=10, y=1.02)
    fig.tight_layout()
    out_png = sim_output("qed_trace_screening_sum_gate.png")
    fig.savefig(out_png, dpi=150, bbox_inches="tight")
    print(f"[screen-sum] wrote {out_png}")


if __name__ == "__main__":
    main()
