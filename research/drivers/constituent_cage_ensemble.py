#!/usr/bin/env python3
"""CONSTITUENT-CAGE-ENSEMBLE ADJUDICATOR — the open #767 fork.

Does an ENSEMBLE of BULK-ONLY-caged constituent compression cores present to the
2Ω far field (i) a sum of image-cancelled core moments (channel-asymmetric — the
LIVE BIN-2 route) or (ii) the coarse-grained uncaged mass texture (radiates at the
q1 partition — BIN-1 clean)?

Prereg (FROZEN, criteria committed ALONE first):
    research/2026-07-20_constituent-cage-ensemble_prereg-FROZEN.md
Adjudicated fork:
    research/2026-07-20_envelope-sector-reduction_result.md  §3.1 / §6.2-1  (#767)

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-FIRST SECTOR HEADER (fired before any standard-physics term)
═══════════════════════════════════════════════════════════════════════════════
  SECTOR : the TRANSLATIONAL (Cauchy-grade) VECTOR sector of the chiral srs-z3 net
           (ave.core.chiral_lattice._SRS_8A / _SRS_NN; I4₁32, Wyckoff-8a, z=3).
           Rank-2 bond tensor Φ_b = k_a·(d̂⊗d̂) + k_s·(I − d̂⊗d̂). NOT a Cartesian
           Laplacian. Rule-14 reuse of the #761/#767 srs_band_survey bond model.
  REGIME : CAGED SOURCES. The cage is a real emergent boundary realized by a
           CONSTITUTIVE GRADE of the bond stiffnesses toward the rail (S(A)→0) on a
           ~1-node shell — NOT a kinematic pin (the #767 lesson; see CLAMPED-CONTROL
           below). Cold-linear far field.
  COORDS : real-space displacement basis (A46-clean): OBSERVABLE = LONGITUDINAL
           (radial, ∇·u) vs TRANSVERSE (tangential, ∇×u). Static exterior dilatation
           θ = Σ_{j~i}(u_j−u_i)·d̂ (Leg 1); shell radial/tangential energy partition
           κ² ≡ F_∥/F_⊥ (Legs 3–5), vs frozen κ_max² = δ_DP = 1.3e-4.
  CLASS  : lattice-derived EMPIRICAL legs + analytic homogenization. FALLBACK scope:
           a self-bound saturated soliton is INFEASIBLE (electron-lock arc); cages
           are constitutive grades, interiors energized/moved by FREE dynamics.
           α-CLEAN (no α/Q_TANK). Every VALUE dimensionless.

★CLAMPED-BOUNDARY FENCE: NO kinematic pin anywhere on the SOURCE path. The clamped
 cage is a NEGATIVE CONTROL only — it MUST show image-DOUBLING (Γ=+1, opposite sign
 to the rail cage's Γ=−1). If it does not, the mirror realization is broken → STOP.

ENGINE BYTE-UNTOUCHED: imports ave.core.chiral_lattice / ave.core.constants read-only.

Run: PYTHONPATH=src:src/scripts/vol_1_foundations python3 \
        research/drivers/constituent_cage_ensemble.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy.spatial import cKDTree

# ── engine reads (read-only) ────────────────────────────────────────────────
from ave.core.chiral_lattice import _SRS_8A, _SRS_NN

# ── Rule-14 reuse of the VALIDATED survey pipeline (side-effect-free imports) ─
_VOL1 = Path(__file__).resolve().parents[2] / "src" / "scripts" / "vol_1_foundations"
sys.path.insert(0, str(_VOL1))
from srs_band_survey import srs_primitive_bcc  # noqa: E402
from srs_vector_band_survey import vector_bloch_D  # noqa: E402

TOL = 1e-9
A_YIELD = 1.0
S_RAIL = 0.03  # rail stiffness factor on the cage shell: S(A_cage)→0 (near-yield)


# ═════════════════════════════════════════════════════════════════════════════
# Finite real-space srs net (identical construction to #761/#767 — Rule-14 reuse)
# ═════════════════════════════════════════════════════════════════════════════
def build_finite_srs(L: int):
    cells = np.array(
        [(cx, cy, cz) for cx in range(L) for cy in range(L) for cz in range(L)],
        dtype=float,
    )
    pos = (cells[:, None, :] + _SRS_8A[None, :, :]).reshape(-1, 3)
    tree = cKDTree(pos)
    pairs = tree.query_pairs(r=_SRS_NN + TOL, output_type="ndarray")
    d = pos[pairs[:, 1]] - pos[pairs[:, 0]]
    ln = np.linalg.norm(d, axis=1)
    keep = np.abs(ln - _SRS_NN) < TOL
    pairs, d, ln = pairs[keep], d[keep], ln[keep]
    dhat = d / ln[:, None]
    mid = 0.5 * (pos[pairs[:, 0]] + pos[pairs[:, 1]])
    return pos, pairs[:, 0].copy(), pairs[:, 1].copy(), dhat, mid


def bond_tensors(dhat, k_a, k_s):
    """Per-bond rank-2 Φ_b = k_a·(d̂⊗d̂) + k_s·(I − d̂⊗d̂). k_a, k_s may be scalars
    OR per-bond (M,) arrays — the per-component form the CAGE uses to grade the
    central (compression) component independently from the transverse component."""
    P = np.einsum("bi,bj->bij", dhat, dhat)
    ka = np.asarray(k_a)
    ks = np.asarray(k_s)
    if ka.ndim == 0:
        ka = np.full(dhat.shape[0], float(ka))
    if ks.ndim == 0:
        ks = np.full(dhat.shape[0], float(ks))
    return ka[:, None, None] * P + ks[:, None, None] * (np.eye(3)[None] - P)


def forces(u, Phi, bi, bj, N):
    du = u[bi] - u[bj]
    fb = np.einsum("bij,bj->bi", Phi, du)
    F = np.zeros((N, 3))
    np.add.at(F, bi, -fb)
    np.add.at(F, bj, +fb)
    return F


def omega_max_cold(Phi, bi, bj, N, iters=60):
    rng = np.random.default_rng(0)
    x = rng.standard_normal((N, 3))
    x /= np.linalg.norm(x)
    lam = 0.0
    for _ in range(iters):
        Dx = -forces(x, Phi, bi, bj, N)
        lam = float(np.linalg.norm(Dx))
        x = Dx / (lam + 1e-30)
    return np.sqrt(max(lam, 1e-12))


# ═════════════════════════════════════════════════════════════════════════════
# ★THE CONSTITUTIVE CAGE PRIMITIVE (the new physics; NOT a kinematic pin)
# ═════════════════════════════════════════════════════════════════════════════
def cage_stiffness(dhat, mid, rho_star, k_s, centers, r_cage, cage_w, wall_class,
                   s_rail=S_RAIL):
    """Per-bond (k_a_bond, k_s_bond) for a set of cages realized by CONSTITUTIVE
    GRADING toward the rail on a ~cage_w-thick shell at r_cage around each center.
    `s_rail` (default = module S_RAIL=0.03, the shipped shallow depth) is the rail
    stiffness factor; PR#770 review-repair threads it so the rail-depth ladder can be
    COMPUTED rather than asserted (Findings 6/9; reconcile-don't-declare).

      wall_class = "none"       : cold everywhere (uncaged control; k_a=ρ*, k_s=k_s)
      wall_class = "symmetric"  : BOTH k_a,k_s → S_RAIL·(·) on the shell (BH melt
                                  wall; Γ_shear=Γ_bulk=−1, lattice-extreme:37 canon)
      wall_class = "bulk_only"  : ONLY k_a → S_RAIL·k_a on the shell, k_s kept full
                                  (electron-class SURROGATE for the un-derived
                                  bulk-only knot-core wall, electron-bh-iso:26 canon;
                                  Γ_bulk=−1, Γ_shear≈0)

    A bond is "on the shell" if its midpoint radial distance to the NEAREST center
    lies in [r_cage, r_cage+cage_w]. The grade is a smooth rail dip so the shell is
    a ~1-node pressure-release contour (Z_bulk→0 ⇒ Γ_bulk=−1, master-eq:105).
    Returns (k_a_bond (M,), k_s_bond (M,)).  NO kinematic pin — free dynamics.
    """
    M = dhat.shape[0]
    k_a_bond = np.full(M, float(rho_star))
    k_s_bond = np.full(M, float(k_s))
    if wall_class == "none" or not centers:
        return k_a_bond, k_s_bond
    # nearest-center shell membership (smooth rail dip centered on the shell)
    rmin = np.full(M, np.inf)
    for c in centers:
        r = np.linalg.norm(mid - np.asarray(c, float), axis=1)
        rmin = np.minimum(rmin, r)
    # rail weight: 1 (cold) far from the shell, S_RAIL at the shell center
    shell_mid = r_cage + 0.5 * cage_w
    w = np.exp(-((rmin - shell_mid) ** 2) / (2.0 * (0.5 * cage_w) ** 2))
    rail = 1.0 - (1.0 - s_rail) * w  # →s_rail on the shell, →1 cold
    if wall_class == "symmetric":
        k_a_bond = k_a_bond * rail
        k_s_bond = k_s_bond * rail
    elif wall_class == "bulk_only":
        k_a_bond = k_a_bond * rail  # compression component grades; shear kept full
    else:
        raise ValueError(f"unknown wall_class {wall_class!r}")
    return k_a_bond, k_s_bond


def cage_shell_nodes(pos, centers, r_cage, cage_w):
    """Node indices lying on the ~cage_w-thick shell (for the CLAMPED NEGATIVE
    CONTROL only — u pinned to 0 there: rigid/open wall, Γ=+1, image doubling)."""
    if not centers:
        return np.zeros(pos.shape[0], dtype=bool)
    rmin = np.full(pos.shape[0], np.inf)
    for c in centers:
        rmin = np.minimum(rmin, np.linalg.norm(pos - np.asarray(c, float), axis=1))
    return (rmin >= r_cage) & (rmin < r_cage + cage_w)


# ═════════════════════════════════════════════════════════════════════════════
# Channel-basis observables (A46-clean): dilatation ∇·u and radial/tangential split
# ═════════════════════════════════════════════════════════════════════════════
def node_dilatation(u, bi, bj, dhat, N):
    """Lattice-native discrete divergence θ_i = Σ_{j~i}(u_j−u_i)·d̂_ij at each node
    (the trace of the discrete strain; NOT a Cartesian Laplacian). Returns (N,)."""
    proj = np.einsum("bi,bi->b", u[bj] - u[bi], dhat)  # (u_j−u_i)·d̂ per bond
    theta = np.zeros(N)
    np.add.at(theta, bi, proj)
    np.add.at(theta, bj, -proj)  # antisymmetric: node j sees −(u_j−u_i)·d̂ = (u_i−u_j)·d̂
    return theta


def shell_partition(u_shell, rhat_shell):
    """Radial (longitudinal) vs tangential (transverse) energy of a shell field."""
    u_par = np.sum(u_shell * rhat_shell, axis=1)[:, None] * rhat_shell
    u_perp = u_shell - u_par
    return float(np.sum(u_par ** 2)), float(np.sum(u_perp ** 2))


def planar_wall_stiffness(mid, x_wall, wall_w, rho_star, k_s, wall_class):
    """Per-bond (k_a,k_s) for a PLANAR wall: bonds whose midpoint x lies in
    [x_wall, x_wall+wall_w] are graded toward the rail. Same three classes as the
    spherical cage. (Used by Leg 3's wall S-matrix.)"""
    M = mid.shape[0]
    k_a_bond = np.full(M, float(rho_star))
    k_s_bond = np.full(M, float(k_s))
    if wall_class == "none":
        return k_a_bond, k_s_bond
    inb = (mid[:, 0] >= x_wall) & (mid[:, 0] < x_wall + wall_w)
    if wall_class == "symmetric":
        k_a_bond[inb] *= S_RAIL
        k_s_bond[inb] *= S_RAIL
    elif wall_class == "bulk_only":
        k_a_bond[inb] *= S_RAIL          # compression grades; shear kept full
    else:
        raise ValueError(f"unknown wall_class {wall_class!r}")
    return k_a_bond, k_s_bond


def texture_displacement(pos, center, amp, sigma):
    """Curl-free dilatation texture centered at `center`: u = ∇φ, φ=exp(−r²/2σ²)
    (the pure-longitudinal seed shape #761/#767 used)."""
    rel = pos - center
    phi = np.exp(-np.sum(rel ** 2, axis=1) / (2.0 * sigma ** 2))
    u = -(rel / sigma ** 2) * phi[:, None]
    return u * (amp / (np.abs(u).max() + 1e-30))


def hamiltonian(u, v, Phi, bi, bj, N):
    du = u[bi] - u[bj]
    KE = 0.5 * float(np.sum(v ** 2))
    PE = 0.5 * float(np.einsum("bi,bij,bj->", du, Phi, du))
    return KE + PE


# ═════════════════════════════════════════════════════════════════════════════
# C-2 spectral cross-check (cold Bloch structure; #761/#767-parity)
# ═════════════════════════════════════════════════════════════════════════════
def run_c2_speeds(rho_star, k_s, n_random=24, seed=1):
    basis, bonds = srs_primitive_bcc("right")
    rng = np.random.default_rng(seed)
    dirs = {"100": [1, 0, 0], "110": [1, 1, 0], "111": [1, 1, 1]}
    rand = rng.standard_normal((n_random, 3))
    rand /= np.linalg.norm(rand, axis=1, keepdims=True)
    for i in range(n_random):
        dirs[f"rand{i}"] = rand[i].tolist()
    kl = 1e-4
    cP_list, cS_list, per_dir = [], [], {}
    for name, dd in dirs.items():
        kh = np.array(dd, float)
        kh = kh / np.linalg.norm(kh)
        D = vector_bloch_D(kh * kl, basis, bonds, rho_star, k_s)
        w2, V = np.linalg.eigh(D)
        idx = np.argsort(w2)[:3]
        w2a, Va = w2[idx], V[:, idx]
        pol = Va.reshape(4, 3, 3).mean(axis=0)
        pol /= np.linalg.norm(pol, axis=0, keepdims=True) + 1e-30
        long_frac = np.abs(pol.T @ kh) ** 2
        c = np.sqrt(np.clip(w2a, 0, None)) / kl
        pL = int(np.argmax(long_frac))
        cP = float(c[pL])
        cS = float(np.mean([c[j] for j in range(3) if j != pL]))
        if name in ("100", "110", "111"):
            per_dir[name] = cP / cS
        cP_list.append(cP)
        cS_list.append(cS)
    return float(np.mean(cP_list)), float(np.mean(cS_list)), per_dir


RHO_STAR = 9.77337  # DERIVED from ν_Hill=2/7 (imported, not fit)
K_S = 1.0


# ═════════════════════════════════════════════════════════════════════════════
# LEG 3 — WALL S-MATRIX (planar pulse reflection) + the CLAMPED STOP-gate control
# ═════════════════════════════════════════════════════════════════════════════
def leg3_wall_smatrix(L, wall_class, pulse_kind, clamped, cP, cS,
                      x_src=5.0, x_wall=14.0, x_mon=8.5, wall_w=1.0,
                      w_pulse=1.3, amp=0.05, cfl=0.2, rho_star=RHO_STAR, k_s=K_S):
    """Launch a planar P (u_x, curl-free) or S (u_y, div-free) pulse rightward at a
    wall and measure the reflected DISPLACEMENT sign + reflected COMPRESSION energy
    at an open-side monitor plane.  Γ (displacement) sign convention:
        rail (free surface, Z→0):  Γ_disp = +1  (⇔ Γ_stress=−1 = pressure-release)
        clamped (rigid,  Z→∞):     Γ_disp = −1  (⇔ Γ_stress=+1 = doubling)
    The STOP-gate reads the opposite-sign requirement between clamped and rail."""
    pos, bi, bj, dhat, mid = build_finite_srs(L)
    N = pos.shape[0]
    Phi_cold = bond_tensors(dhat, rho_star, k_s)
    omega_max = omega_max_cold(Phi_cold, bi, bj, N)
    dt = cfl * 2.0 / omega_max

    if clamped:
        ka, ks = np.full(dhat.shape[0], rho_star), np.full(dhat.shape[0], float(k_s))
        pin = (pos[:, 0] >= x_wall) & (pos[:, 0] < x_wall + wall_w)
    else:
        ka, ks = planar_wall_stiffness(mid, x_wall, wall_w, rho_star, k_s, wall_class)
        pin = np.zeros(N, dtype=bool)
    Phi = bond_tensors(dhat, ka, ks)
    free = ~pin

    comp = 0 if pulse_kind == "P" else 1          # u_x for P, u_y for S
    speed = cP if pulse_kind == "P" else cS
    x = pos[:, 0]
    g = np.exp(-((x - x_src) ** 2) / (2.0 * w_pulse ** 2))
    u = np.zeros((N, 3))
    v = np.zeros((N, 3))
    u[:, comp] = amp * g
    v[:, comp] = speed * (x - x_src) / w_pulse ** 2 * amp * g   # rightward u=f(x−ct)
    u[pin] = 0.0
    v[pin] = 0.0

    t_wall = (x_wall - x_src) / speed
    t_back = t_wall + (x_wall - x_mon) / speed                 # reflected reaches mon
    t_2nd = t_back + 2.0 * x_mon / speed                       # after free-x=0 bounce
    t_end = 1.02 * t_2nd
    n_steps = int(np.ceil(t_end / dt)) + 3
    slab = np.abs(x - x_mon) < 0.6

    F = forces(u, Phi, bi, bj, N)
    ts, sig = [], []
    for step in range(n_steps):
        t = step * dt
        ts.append(t)
        sig.append(float(np.mean(u[slab, comp])))
        u[free] = u[free] + v[free] * dt + 0.5 * F[free] * dt ** 2
        u[pin] = 0.0
        F_new = forces(u, Phi, bi, bj, N)
        v[free] = v[free] + 0.5 * (F[free] + F_new[free]) * dt
        v[pin] = 0.0
        F = F_new
    ts = np.array(ts)
    sig = np.array(sig)
    inc_win = ts < 0.92 * t_wall
    ref_win = (ts > 1.08 * t_wall) & (ts < 0.98 * t_2nd)
    i_inc = int(np.argmax(np.abs(sig * inc_win)))
    i_ref = int(np.argmax(np.abs(sig * ref_win)))
    inc_amp = float(sig[i_inc])
    ref_amp = float(sig[i_ref])
    gamma_disp = ref_amp / (inc_amp + np.sign(inc_amp) * 1e-30)
    return {
        "wall_class": ("clamped" if clamped else wall_class), "pulse": pulse_kind,
        "gamma_disp": gamma_disp, "sign": int(np.sign(gamma_disp)),
        "inc_amp": inc_amp, "ref_amp": ref_amp,
        "t_wall": float(t_wall), "t_inc": float(ts[i_inc]), "t_ref": float(ts[i_ref]),
        "dt": float(dt), "n_steps": n_steps,
    }


def leg12_cage_seal(L, wall_class, energized, clamped, cP, cS,
                    r_cage=3.0, cage_w=1.2, r_meas=6.0, shell_w=1.0,
                    sigma=1.2, amp=0.06, cfl=0.2, rho_star=RHO_STAR, k_s=K_S):
    """LEG 1 (charged-line) + LEG 2 (seal). A single cage at the box center, interior
    ENERGIZED by a curl-free dilatation seed (initial displacement, zero velocity —
    FREE dynamics, NO pin on the source), free-evolve, and measure the EXTERIOR
    dilatation ∇·u at the far r_meas shell:
      • DC (time-averaged over the reflection-free window) exterior θ  — the STATIC
        compression "charge" V (Leg 1 discriminator: →0 uncharged/sealed vs ∝ energy).
      • RMS exterior θ + radial/tangential shell energy — the total compression that
        LEAKS through the cage (Leg 2 seal; energized-vs-empty control).
    `energized=False` = empty cold cage (Leg-2 control: the cage sources nothing).
    `clamped=True` = rigid-shell control (u=0 pinned on the shell)."""
    pos, bi, bj, dhat, mid = build_finite_srs(L)
    N = pos.shape[0]
    center = np.array([L / 2.0] * 3)
    Phi_cold = bond_tensors(dhat, rho_star, k_s)
    omega_max = omega_max_cold(Phi_cold, bi, bj, N)
    dt = cfl * 2.0 / omega_max

    if clamped:
        ka, ks = np.full(dhat.shape[0], rho_star), np.full(dhat.shape[0], float(k_s))
        pin = cage_shell_nodes(pos, [center], r_cage, cage_w)
    else:
        ka, ks = cage_stiffness(dhat, mid, rho_star, k_s, [center],
                                r_cage, cage_w, wall_class)
        pin = np.zeros(N, dtype=bool)
    Phi = bond_tensors(dhat, ka, ks)
    free = ~pin

    rel = pos - center
    r = np.linalg.norm(rel, axis=1)
    rhat = rel / (r[:, None] + 1e-30)
    shell = (r >= r_meas) & (r < r_meas + shell_w)

    u = np.zeros((N, 3))
    v = np.zeros((N, 3))
    if energized:
        u_seed = texture_displacement(pos, center, amp, sigma)
        u_seed[r > r_cage] = 0.0            # energize the INTERIOR only (r<r_cage)
        u = u_seed.copy()
    u[pin] = 0.0

    # interior energy (the "charge" the cage holds), and Compton-analog k·r_core
    E_int = 0.5 * float(np.sum(v ** 2)) + 0.5 * float(
        np.einsum("bi,bij,bj->", (u[bi] - u[bj]), Phi, (u[bi] - u[bj])))
    lam_P = 2.0 * np.pi * sigma  # dominant seed wavelength ~ texture scale
    k_rcore = 2.0 * np.pi * r_cage / (lam_P + 1e-30)

    t_P = r_meas / cP
    t_reflect = (2.0 * (L / 2.0) - r_meas) / cP
    t_end = 1.05 * t_reflect
    n_steps = int(np.ceil(t_end / dt)) + 3

    F = forces(u, Phi, bi, bj, N)
    theta_acc = np.zeros(N)
    n_acc = 0
    Epar_acc = Eperp_acc = 0.0
    for step in range(n_steps):
        t = step * dt
        if t_P <= t < t_reflect:
            theta_acc += node_dilatation(u, bi, bj, dhat, N)
            n_acc += 1
            ep, eq = shell_partition(u[shell], rhat[shell])
            Epar_acc += ep
            Eperp_acc += eq
        u[free] = u[free] + v[free] * dt + 0.5 * F[free] * dt ** 2
        u[pin] = 0.0
        F_new = forces(u, Phi, bi, bj, N)
        v[free] = v[free] + 0.5 * (F[free] + F_new[free]) * dt
        v[pin] = 0.0
        F = F_new
    n_acc = max(n_acc, 1)
    theta_dc = theta_acc / n_acc                      # time-averaged (DC) θ per node
    ext = (r >= r_meas) & (r < r_meas + shell_w)
    theta_dc_ext_rms = float(np.sqrt(np.mean(theta_dc[ext] ** 2)))
    Epar = Epar_acc / n_acc
    Eperp = Eperp_acc / n_acc
    return {
        "wall_class": ("clamped" if clamped else wall_class), "energized": energized,
        "E_interior": E_int, "k_rcore": float(k_rcore),
        "theta_dc_exterior_rms": theta_dc_ext_rms,
        "shell_E_par": Epar, "shell_E_perp": Eperp,
        "shell_f_long": Epar / (Epar + Eperp + 1e-30),
        "shell_kappa2": Epar / (Eperp + 1e-30),
        "dt": float(dt), "n_win": n_acc,
    }


def _ensemble_centers(N, L, R_lobe, pack):
    """N caged cores in a DIPOLE-FREE two-lobe (±R) arrangement, N/2 per lobe packed
    on small fixed deterministic offsets. N=1 = single core at center."""
    c0 = np.array([L / 2.0] * 3)
    if N == 1:
        return [c0.copy()]
    off = np.array([[0, 0, 0], [pack, 0, 0], [0, pack, 0], [0, 0, pack],
                    [pack, pack, 0], [pack, 0, pack], [0, pack, pack],
                    [pack, pack, pack]], float)
    half = N // 2
    lobe = np.array([R_lobe, 0.0, 0.0])
    cs = []
    for s in (+1, -1):
        for j in range(half):
            cs.append(c0 + s * lobe + off[j] - 0.5 * pack)
    return cs


def leg5_ensemble_scaling(L, wall_class, N, cP, cS, R_lobe=3.5, pack=1.0,
                          r_cage=1.6, cage_w=1.0, r_meas=7.5, shell_w=1.0,
                          sigma=1.0, amp=0.05, cfl=0.2, rho_star=RHO_STAR, k_s=K_S,
                          s_rail=S_RAIL):
    """LEG 5 — the verdict-controlling N-scaling. N energized caged cores (dipole-free
    two-lobe ensemble), seeded as initial displacement (FREE dynamics, NO pin), free-
    evolve, measure the NET far-field compression at a shell ENCLOSING all N cores.
    Static seeded release (both caged and uncaged arms identical seed geometry ⇒ the
    cage is the only difference ⇒ ρ_N = caged/uncaged far-field compression removes
    the geometry). Discriminator: ρ_N → 1 as N grows = cages wash out into the
    coarse-grained texture (BIN-1); ρ_N bounded < 1 = per-core cage survives
    aggregation (BIN-2). Also the scaling exponent p of F_bulk(N) ∝ N^p."""
    pos, bi, bj, dhat, mid = build_finite_srs(L)
    Npt = pos.shape[0]
    centers = _ensemble_centers(N, L, R_lobe, pack)
    c0 = np.array([L / 2.0] * 3)
    Phi_cold = bond_tensors(dhat, rho_star, k_s)
    omega_max = omega_max_cold(Phi_cold, bi, bj, Npt)
    dt = cfl * 2.0 / omega_max

    ka, ks = cage_stiffness(dhat, mid, rho_star, k_s, centers,
                            r_cage, cage_w, wall_class, s_rail=s_rail)
    Phi = bond_tensors(dhat, ka, ks)

    rel = pos - c0
    r = np.linalg.norm(rel, axis=1)
    rhat = rel / (r[:, None] + 1e-30)
    shell = (r >= r_meas) & (r < r_meas + shell_w)

    u = np.zeros((Npt, 3))
    v = np.zeros((Npt, 3))
    for c in centers:                                   # energize each interior
        useed = texture_displacement(pos, c, amp, sigma)
        rc = np.linalg.norm(pos - c, axis=1)
        useed[rc > r_cage] = 0.0
        u += useed

    t_P = r_meas / cP
    t_reflect = (2.0 * (L / 2.0) - r_meas) / cP
    t_end = 1.05 * t_reflect
    n_steps = int(np.ceil(t_end / dt)) + 3

    F = forces(u, Phi, bi, bj, Npt)
    Epar_acc = Eperp_acc = 0.0
    n_acc = 0
    for step in range(n_steps):
        t = step * dt
        if t_P <= t < t_reflect:
            ep, eq = shell_partition(u[shell], rhat[shell])
            Epar_acc += ep
            Eperp_acc += eq
            n_acc += 1
        u = u + v * dt + 0.5 * F * dt ** 2
        F_new = forces(u, Phi, bi, bj, Npt)
        v = v + 0.5 * (F + F_new) * dt
        F = F_new
    n_acc = max(n_acc, 1)
    Epar = Epar_acc / n_acc
    Eperp = Eperp_acc / n_acc
    return {
        "N": N, "wall_class": wall_class, "n_cores": len(centers),
        "shell_E_par": Epar, "shell_E_perp": Eperp,
        "shell_kappa2": Epar / (Eperp + 1e-30),
        "shell_f_long": Epar / (Epar + Eperp + 1e-30),
        "r_meas": r_meas, "dt": float(dt),
    }


def leg4_moving_cage(L, wall_class, cP, cS, v_drive=0.12, r_cage=2.2, cage_w=1.0,
                     r_meas=6.0, shell_w=1.0, sigma=1.1, amp=0.05, cfl=0.2,
                     rho_star=RHO_STAR, k_s=K_S):
    """LEG 4 — moving single cage. Seed an energized interior (initial displacement,

    ★QUARANTINE (2026-07-21, Grant-approved, pending-rulings §1 item 12): the
    `carry_fraction` and `energy_centroid_displacement` outputs of this leg are
    ARTIFACT-DOMINATED — the track[0] sample is taken at v=0, so energy_cx=0 is
    subtracted as a spurious baseline, and the resulting reads (~2.4–5.0) are
    identical for cage and no-cage. Corpus-swept 2026-07-21: LOAD-BEARING-NOWHERE
    (no banked bin, ledger row, or shipped verdict consumes them; #770 banks rest
    on Legs 3/5/6). Do NOT reuse these two outputs in any future lane. The Leg-4
    FAR-FIELD outputs (`shell_f_long` partition) are NOT quarantined; the frozen
    #770 prereg Fork-C clause naming the far-field as co-decider stays live.
    Basis: research/2026-07-21_beta-tracking-feasibility_scoping.md §3, §8.
    FREE dynamics, NO pin), translate the CONSTITUTIVE GRADE (moving-C(x,t): the cage
    center moves at v_drive, bond tensors recomputed each step), free-evolve, and
    measure (a) the far-field compression/shear partition and (b) whether the moving
    cage CARRIES the interior energy (energy-centroid vs cage-centroid tracking).
    ★Declared fallback (prereg §3): LINEAR translation (orbital motion of a single
    cage is infeasible for a clean far-field on the L=20 box). NO pin on the source —
    so the interior is NOT dragged; whether it follows the cage is the measurement."""
    pos, bi, bj, dhat, mid = build_finite_srs(L)
    N = pos.shape[0]
    c0 = np.array([L / 2.0 - 3.0, L / 2.0, L / 2.0])  # start off-center, move +x
    Phi_cold = bond_tensors(dhat, rho_star, k_s)
    omega_max = omega_max_cold(Phi_cold, bi, bj, N)
    dt = cfl * 2.0 / omega_max

    cen = np.array([L / 2.0] * 3)
    rel0 = pos - cen
    r0 = np.linalg.norm(rel0, axis=1)
    rhat0 = rel0 / (r0[:, None] + 1e-30)
    shell = (r0 >= r_meas) & (r0 < r_meas + shell_w)

    u = texture_displacement(pos, c0, amp, sigma)
    u[np.linalg.norm(pos - c0, axis=1) > r_cage] = 0.0
    v = np.zeros((N, 3))

    def center(t):
        return c0 + np.array([v_drive * t, 0.0, 0.0])

    t_reflect = (2.0 * (L / 2.0) - r_meas) / cP
    t_end = 0.9 * t_reflect                          # reflection-free
    n_steps = int(np.ceil(t_end / dt)) + 3

    ka, ks = cage_stiffness(dhat, mid, rho_star, k_s, [c0], r_cage, cage_w, wall_class)
    Phi = bond_tensors(dhat, ka, ks)
    F = forces(u, Phi, bi, bj, N)
    Epar_acc = Eperp_acc = 0.0
    n_acc = 0
    track = []
    for step in range(n_steps):
        t = step * dt
        ep, eq = shell_partition(u[shell], rhat0[shell])
        Epar_acc += ep
        Eperp_acc += eq
        n_acc += 1
        if step % max(1, n_steps // 8) == 0:
            edens = np.sum(v ** 2, axis=1)             # kinetic energy density proxy
            tot = edens.sum() + 1e-30
            e_cx = float(np.sum(edens * pos[:, 0]) / tot)
            track.append({"t": float(t), "cage_x": float(center(t)[0]),
                          "energy_cx": e_cx})
        cs = center(t + dt)
        ka, ks = cage_stiffness(dhat, mid, rho_star, k_s, [cs], r_cage, cage_w, wall_class)
        Phi = bond_tensors(dhat, ka, ks)
        u = u + v * dt + 0.5 * F * dt ** 2
        F_new = forces(u, Phi, bi, bj, N)
        v = v + 0.5 * (F + F_new) * dt
        F = F_new
    n_acc = max(n_acc, 1)
    Epar = Epar_acc / n_acc
    Eperp = Eperp_acc / n_acc
    cage_disp = v_drive * (n_steps * dt)
    e_disp = track[-1]["energy_cx"] - track[0]["energy_cx"] if len(track) >= 2 else 0.0
    return {
        "wall_class": wall_class, "v_drive": v_drive,
        "shell_f_long": Epar / (Epar + Eperp + 1e-30),
        "shell_kappa2": Epar / (Eperp + 1e-30),
        "cage_displacement": float(cage_disp),
        "energy_centroid_displacement": float(e_disp),
        "carry_fraction": float(e_disp / (cage_disp + 1e-30)),
        "track": track, "dt": float(dt), "n_steps": n_steps,
    }


def leg3_impedance_smatrix(cP_cold, cS_cold):
    """CLEAN (artifact-free) channel S-matrix from the railed-medium Bloch speeds.
    For each wall class compute the railed (c_P,c_S) and the channel reflection
    Γ_ch = (Z_railed − Z_cold)/(Z_railed + Z_cold) with Z_ch = ρ·c_ch (ρ common).
    This is the primary channel characterization; the pulse-reflection (leg3_wall_
    smatrix) supplies the SIGN / STOP-gate only (its magnitude is wavelength-artifact
    contaminated by the finite wall thickness)."""
    def gamma(cr, cc):
        return (cr - cc) / (cr + cc)
    out = {}
    railed = {
        "symmetric": run_c2_speeds(S_RAIL * RHO_STAR, S_RAIL * K_S)[:2],
        "bulk_only": run_c2_speeds(S_RAIL * RHO_STAR, K_S)[:2],
    }
    for name, (cP, cS) in railed.items():
        out[name] = {
            "cP_railed": cP, "cS_railed": cS, "cP_over_cS_railed": cP / cS,
            "gamma_bulk": gamma(cP, cP_cold), "gamma_shear": gamma(cS, cS_cold),
            "channel_asymmetry_ratio": abs(gamma(cP, cP_cold)) /
                                       (abs(gamma(cS, cS_cold)) + 1e-30),
        }
    out["cold_ratio_1p813_frozen_note"] = (
        "symmetric cP/cS stays 1.813 (degree-0 grade-lock, electron-bh-iso:38/PR521 "
        "canon); bulk_only cP/cS SHIFTS (grade-lock broken by the surrogate — the "
        "un-derived channel-asymmetry, electron-bh-iso:26). The srs channels SHARE "
        "k_s, so a perfect Γ_bulk=−1/Γ_shear=0 wall is NOT cleanly realizable (k_s "
        "props up K); bulk_only gives a channel-ASYMMETRIC partial compression seal "
        "with near-full shear pass (Γ_bulk≫|Γ_shear|) — the electron-class SURROGATE.")
    return out


def rail_depth_scan(cP_cold, cS_cold, L, uncaged_leg5,
                    imp_ladder=(0.03, 0.003, 1e-4, 1e-6, 0.0),
                    rho_ladder=(0.03, 0.003, 1e-4),
                    rho_star=RHO_STAR, k_s=K_S):
    """★REVIEW-REPAIR (PR#770 maximum-stakes review, 2026-07-20; Findings 0/2/5/6/9).

    The originally-shipped driver HARD-CODED 'ROBUST across rail depth (S_RAIL
    0.03→0.003 all RISING, pressure-tested)' into l5['scaling']['note'] while running
    ONLY S_RAIL=0.03 (module constant, no scan loop). That is the reconcile-don't-
    declare failure mode: a machine-JSON field asserting a pressure-test the
    deterministic run never performed. This function COMPUTES the S_RAIL ladder from
    the SHIPPED pipeline (run_c2_speeds + leg5_ensemble_scaling), so the artifact
    carries computed truth. Engine byte-untouched.

    Two ladders:
      • IMPEDANCE ladder (run_c2_speeds Bloch speeds — the load-bearing Leg-6 fact,
        Findings 0/5 CRITICAL): for each s, bulk_only rails ONLY k_a (k_s full);
        symmetric rails both. Γ_ch = (c_railed − c_cold)/(c_railed + c_cold). RESULT:
        bulk_only Γ_bulk → −1 as s→0 with c_S FINITE — the canon bulk-only wall
        (electron-bh-iso:26: Γ_bulk=−1, shear un-melted at the knot core) IS
        constitutively realizable in the rank-2 bond model. The originally-shipped
        'c_P stays finite / Γ_bulk saturates −0.5…−0.8 NOT −1' claim is INVERTED (it
        stopped the scan at s=0.003; one decade deeper Γ_bulk marches to −1).
      • ρ_N ladder (leg5 at each s_rail — Finding 2): caged/uncaged far-field
        compression. Deeper rail plateaus ρ_N ~0.3 and goes flat-to-FALLING N4→N8 —
        the originally-shipped 'RISING toward 1 / all RISING' read is rail-depth-
        conditional (it holds only at the shallow, un-frozen shipped depth 0.03).
    """
    def gamma(cr, cc):
        return (cr - cc) / (cr + cc)
    imp = {"ladder": list(imp_ladder), "cold": {"cP": cP_cold, "cS": cS_cold},
           "bulk_only": {}, "symmetric": {}}
    for s in imp_ladder:
        key = f"{s:g}"
        cPb, cSb, _ = run_c2_speeds(s * rho_star, k_s)             # rail k_a only
        imp["bulk_only"][key] = {
            "cP": cPb, "cS": cSb, "gamma_bulk": gamma(cPb, cP_cold),
            "gamma_shear": gamma(cSb, cS_cold), "cP_over_cS": cPb / (cSb + 1e-30)}
        if s == 0.0:
            # symmetric melt point: cP=cS=0 (0/0 in run_c2_speeds' per_dir) — the
            # degenerate BH-melt wall, canon Γ_bulk=Γ_shear=−1 (lattice-extreme:37).
            imp["symmetric"][key] = {
                "cP": 0.0, "cS": 0.0, "gamma_bulk": -1.0, "gamma_shear": -1.0,
                "cP_over_cS": None,
                "note": "degenerate melt point cP=cS=0 (0/0); analytic limit Γ=−1 both"}
        else:
            cPs, cSs, _ = run_c2_speeds(s * rho_star, s * k_s)     # rail both
            imp["symmetric"][key] = {
                "cP": cPs, "cS": cSs, "gamma_bulk": gamma(cPs, cP_cold),
                "gamma_shear": gamma(cSs, cS_cold), "cP_over_cS": cPs / (cSs + 1e-30)}

    Ns = (1, 2, 4, 8)
    rho = {"ladder": list(rho_ladder), "bulk_only": {}, "symmetric": {}}
    for s in rho_ladder:
        key = f"{s:g}"
        for wc in ("bulk_only", "symmetric"):
            rho[wc][key] = {
                str(N): leg5_ensemble_scaling(L, wc, N, cP_cold, cS_cold, s_rail=s)[
                    "shell_E_par"] / (uncaged_leg5[str(N)] + 1e-30)
                for N in Ns}
    # honest trend read (Finding 2): the shipped note claimed 'all RISING'; report
    # the two sub-trends per depth from data (N2→N8 headline vs N4→N8 tail).
    rho["trend_bulk_only_by_depth"] = {
        f"{s:g}": {
            "N2_to_N8_rising": rho["bulk_only"][f"{s:g}"]["8"] > rho["bulk_only"][f"{s:g}"]["2"],
            "N4_to_N8_rising": rho["bulk_only"][f"{s:g}"]["8"] > rho["bulk_only"][f"{s:g}"]["4"],
            "rho_N8": rho["bulk_only"][f"{s:g}"]["8"]}
        for s in rho_ladder}
    return {
        "provenance": "PR#770 review-repair 2026-07-20 — the S_RAIL ladder the shipped "
                      "l5 note asserted ('ROBUST … pressure-tested') but never ran; "
                      "COMPUTED here from the shipped run_c2_speeds + leg5_ensemble_scaling "
                      "(engine byte-untouched, deterministic).",
        "impedance_ladder_run_c2_speeds": imp,
        "rho_N_ladder_leg5": rho,
        "finding0_5_bulk_only_gamma_bulk_to_minus1_with_shear_finite": {
            "gamma_bulk_by_s": {f"{s:g}": imp["bulk_only"][f"{s:g}"]["gamma_bulk"] for s in imp_ladder},
            "cS_bulk_only_by_s": {f"{s:g}": imp["bulk_only"][f"{s:g}"]["cS"] for s in imp_ladder},
            "canon_bulk_only_wall_realizable": bool(imp["bulk_only"]["0"]["gamma_bulk"] < -0.99
                                                    and imp["bulk_only"]["0"]["cS"] > 0.1),
        },
    }


def make_figure(out, path_png):
    """White-style figure (ave.viz.style, Okabe-Ito, honest axes/units, legend outside
    data, no on-figure title): (L) Leg-5 ρ_N vs N — the aggregation trend (rising
    toward the uncaged coarse-grained texture = BIN-1); (R) ensemble κ² vs the pulsar
    kill-lines (log)."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from ave.viz import style
    style.apply()
    C = style.COLORS

    l5 = out["leg5_ensemble_scaling"]
    Ns = [1, 2, 4, 8]
    rho_bo = [l5["rho_N_caged_over_uncaged_compression"]["bulk_only"][str(N)] for N in Ns]
    rho_sy = [l5["rho_N_caged_over_uncaged_compression"]["symmetric"][str(N)] for N in Ns]
    kappa2_uncaged = out["spectral_cold"]["continuum_import_colorcheck_F_bulk_over_F_shear"]

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(10.2, 4.2))

    axL.plot(Ns, rho_bo, "o-", color=C["ave"], ms=8,
             label="bulk-only cage (electron-class, LIVE BIN-2 route)")
    axL.plot(Ns, rho_sy, "s--", color=C["comparison"], ms=6,
             label="symmetric cage (BH-class; also kills shear — fenced)")
    axL.axhline(1.0, color=C["muted"], ls=":", label="uncaged coarse-grained texture (ρ=1)")
    axL.set_xlabel("number of caged constituent cores  N")
    axL.set_ylabel("ρ_N = caged / uncaged far-field compression")
    axL.set_xscale("log", base=2)
    axL.set_xticks(Ns)
    axL.set_xticklabels([str(n) for n in Ns])
    axL.set_ylim(0, 1.25)
    axL.legend(loc="upper center", fontsize=7, frameon=False, ncol=1)
    # ★PR#770 review-repair (Findings 2/6/9): annotation is depth-scoped + honest —
    # the rise is a SHALLOW-rail (S_RAIL=0.03) read; deeper rail plateaus ~0.3 (see
    # review_repair_rail_depth_scan). The verdict is RAIL-DEPTH-CONDITIONAL → REOPENED.
    axL.annotate("bulk-only ρ_N rises N2→N8 at the SHIPPED\nS_RAIL=0.03 (un-frozen) ONLY; deeper rail\nplateaus ~0.3 — rail-depth-conditional (REOPENED)",
                 xy=(8, rho_bo[-1]), xytext=(1.05, 0.30), fontsize=6.5, color=C["data"])

    k_uncaged = kappa2_uncaged
    k_bo = rho_bo[-1] * kappa2_uncaged
    k_sy = rho_sy[-1] * kappa2_uncaged
    labels = ["uncaged\nκ²(#767)", "bulk-only\nensemble κ²(N=8)",
              "symmetric\nensemble κ²(N=8)", "κ_max²\n(double pulsar)"]
    vals = [k_uncaged, k_bo, k_sy, 1.3e-4]
    cols = [C["muted"], C["ave"], C["comparison"], C["accent"]]
    axR.bar(range(4), vals, color=cols, width=0.62)
    axR.set_yscale("log")
    axR.set_xticks(range(4))
    axR.set_xticklabels(labels, fontsize=7.5)
    axR.set_ylabel("κ² = F_bulk / F_shear")
    axR.set_ylim(5e-5, 1e-1)
    axR.axhline(1.3e-4, color=C["accent"], ls=":", lw=1)
    axR.annotate("bulk-only ensemble\n%.0f× above the kill line" % (k_bo / 1.3e-4),
                 xy=(1, k_bo), xytext=(1.4, 4e-2), fontsize=7.5, color=C["data"])

    fig.savefig(path_png, dpi=150, bbox_inches="tight")
    fig.savefig(str(Path(path_png).with_suffix(".pdf")), bbox_inches="tight")
    plt.close(fig)


def main():
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--L", type=int, default=20)
    ap.add_argument("--out", default=str(Path(__file__).with_name(
        "constituent_cage_ensemble_results.json")))
    args = ap.parse_args()

    cP_iso, cS_iso, cpcs_dir = run_c2_speeds(RHO_STAR, K_S)
    out = {
        "provenance": {
            "class": "constituent-cage-ensemble adjudicator; cages by CONSTITUTIVE "
                     "GRADING (no kinematic pin on source path); clamped = negative "
                     "control (image-doubling STOP-gate); mints no canon; engine "
                     "byte-untouched",
            "kappa_max2_double_pulsar": 1.3e-4,
            "kappa_env2_uncaged_767_baseline": 0.034,
            "S_RAIL": S_RAIL,
            "review_repair": (
                "PR#770 maximum-stakes review-repair rerun (2026-07-20). SUPERSEDES the "
                "originally-shipped JSON at fa59998a, which hard-coded 'ROBUST across "
                "rail depth (S_RAIL 0.03->0.003 all RISING, pressure-tested)' + "
                "'shear_ratio~1' into l5['scaling']['note'] while running ONLY "
                "S_RAIL=0.03 (module constant, no scan loop) — the reconcile-don't-"
                "declare failure mode. This rerun (a) REMOVES the fabricated note, (b) "
                "adds review_repair_rail_depth_scan COMPUTING the S_RAIL ladder from the "
                "shipped run_c2_speeds + leg5_ensemble_scaling. All originally-shipped "
                "legs are bit-identical (s_rail defaults to S_RAIL=0.03). Deterministic; "
                "engine byte-untouched."),
        },
        "spectral_cold": {
            "cP_iso": cP_iso, "cS_iso": cS_iso, "cP_over_cS_iso": cP_iso / cS_iso,
            "cP_over_cS_dir": cpcs_dir,
            "continuum_import_colorcheck_F_bulk_over_F_shear":
                (2.0 / 3.0) * (cS_iso / cP_iso) ** 5,
        },
    }
    # ── LEG 1 (charged-line) + LEG 2 (seal): single-cage exterior ∇·u ──
    l12 = {}
    for wc, en, cl in (("none", True, False), ("symmetric", True, False),
                       ("bulk_only", True, False), ("none", True, True),
                       ("none", False, False), ("symmetric", False, False),
                       ("bulk_only", False, False)):
        tag = ("clamped" if cl else wc) + ("_energized" if en else "_EMPTY")
        l12[tag] = leg12_cage_seal(args.L, wc, en, cl, cP_iso, cS_iso)
    base_theta = l12["none_energized"]["theta_dc_exterior_rms"]
    base_epar = l12["none_energized"]["shell_E_par"]
    for tag, r in l12.items():
        r["theta_dc_ext_over_uncaged"] = r["theta_dc_exterior_rms"] / (base_theta + 1e-30)
        r["shell_Epar_over_uncaged"] = r["shell_E_par"] / (base_epar + 1e-30)
    out["leg12_cage_seal"] = l12
    out["leg12_discriminators"] = {
        "leg1_charged_line_exterior_DCdivu_over_uncaged": {
            "bulk_only": l12["bulk_only_energized"]["theta_dc_ext_over_uncaged"],
            "symmetric": l12["symmetric_energized"]["theta_dc_ext_over_uncaged"],
            "note": "→0 = uncharged/sealed line (BIN-2 shape); ~1 = charged line "
                    "(retains exterior compression V ⇒ BIN-1 shape). Single-cage, "
                    "k·r_core~O(1) on the lattice (NOT the deep-quasistatic 10⁻²⁵ of "
                    "the real system — Leg 6 carries that extrapolation).",
        },
        "leg2_seal_energized_vs_empty": {
            "empty_cage_sources_nothing": all(
                l12[f"{w}_EMPTY"]["shell_E_par"] < 1e-12
                for w in ("none", "symmetric", "bulk_only")),
            "bulk_only_single_cage_compression_seal_frac":
                1.0 - l12["bulk_only_energized"]["shell_Epar_over_uncaged"],
            "symmetric_single_cage_compression_seal_frac":
                1.0 - l12["symmetric_energized"]["shell_Epar_over_uncaged"],
        },
    }

    # ── LEG 4 — moving single cage (moving grade + seeded interior; carry check) ──
    out["leg4_moving_cage"] = {
        wc: leg4_moving_cage(args.L, wc, cP_iso, cS_iso)
        for wc in ("bulk_only", "symmetric")
    }

    # ── LEG 5 — the verdict-controlling N-scaling (ρ_N and the shear consistency gate) ──
    l5 = {"N_values": [1, 2, 4, 8], "by_wall": {}}
    for wc in ("none", "bulk_only", "symmetric"):
        l5["by_wall"][wc] = {str(N): leg5_ensemble_scaling(args.L, wc, N, cP_iso, cS_iso)
                             for N in (1, 2, 4, 8)}
    rho = {}
    shear_ratio = {}
    for wc in ("bulk_only", "symmetric"):
        rho[wc] = {str(N): l5["by_wall"][wc][str(N)]["shell_E_par"] /
                   (l5["by_wall"]["none"][str(N)]["shell_E_par"] + 1e-30)
                   for N in (1, 2, 4, 8)}
        shear_ratio[wc] = {str(N): l5["by_wall"][wc][str(N)]["shell_E_perp"] /
                           (l5["by_wall"]["none"][str(N)]["shell_E_perp"] + 1e-30)
                           for N in (1, 2, 4, 8)}
    l5["rho_N_caged_over_uncaged_compression"] = rho
    l5["shear_ratio_caged_over_uncaged"] = shear_ratio
    # scaling exponent p: F_bulk(N) ∝ N^p  (bulk_only, N=2→8 dipole-free branch)
    Ns = np.array([2, 4, 8], float)
    Fb = np.array([l5["by_wall"]["bulk_only"][str(int(N))]["shell_E_par"] for N in Ns])
    Fu = np.array([l5["by_wall"]["none"][str(int(N))]["shell_E_par"] for N in Ns])
    p_caged = float(np.polyfit(np.log(Ns), np.log(Fb), 1)[0])
    p_uncaged = float(np.polyfit(np.log(Ns), np.log(Fu), 1)[0])
    # ★PR#770 review-repair (Findings 2/6/9): depth-scoped, verdict-neutral trend
    # label (the shipped label baked 'BIN1/BIN2' into the artifact; the review
    # REOPENED the verdict). rho_N8>rho_N2 is TRUE only at this shallow shipped depth.
    rho_trend = ("RISING_N2_to_N8_at_shipped_depth_0p03"
                 if rho["bulk_only"]["8"] > rho["bulk_only"]["2"]
                 else "falling_N2_to_N8_at_shipped_depth_0p03")
    l5["scaling"] = {
        "p_caged_bulk_only": p_caged, "p_uncaged": p_uncaged,
        "rho_N_trend_bulk_only": rho_trend,
        "rho_bulk_only_N2": rho["bulk_only"]["2"], "rho_bulk_only_N8": rho["bulk_only"]["8"],
        "shear_ratio_bulk_only_N1": shear_ratio["bulk_only"]["1"],
        "shear_ratio_bulk_only_N8": shear_ratio["bulk_only"]["8"],
        # ★PR#770 review-repair (Findings 6/9): the fabricated 'ROBUST across rail
        # depth … all RISING, pressure-tested' + 'shear_ratio≈1' strings are REMOVED.
        # Rail-depth robustness is COMPUTED, not asserted — see review_repair_rail_
        # depth_scan below. shear_ratio is reported at its actual (suppressed) value.
        "note": (
            "SHIPPED-DEPTH (S_RAIL=%.3g, un-frozen) measurement ONLY. bulk_only rho_N "
            "N2=%.3f->N8=%.3f (%s); bulk_only shear_ratio N1=%.2f N8=%.2f — shear is "
            "SUPPRESSED to %.2fx uncaged (NOT ~1; a 40-77%% suppression). Rail-depth "
            "robustness is NOT asserted from this single depth: see review_repair_rail_"
            "depth_scan for the COMPUTED S_RAIL ladder (PR#770 review-repair). Deeper "
            "rail plateaus rho_N ~0.3 (flat-to-FALLING N4->N8) AND drives bulk_only "
            "Gamma_bulk -> -1 with shear FINITE (the canon bulk-only wall IS "
            "realizable). The symmetric wall suppresses compression more but ALSO kills "
            "shear (wall-class artifact, fenced)." % (
                S_RAIL, rho["bulk_only"]["2"], rho["bulk_only"]["8"], rho_trend,
                shear_ratio["bulk_only"]["1"], shear_ratio["bulk_only"]["8"],
                shear_ratio["bulk_only"]["8"])),
    }
    out["leg5_ensemble_scaling"] = l5

    # ── ★REVIEW-REPAIR (PR#770): the COMPUTED S_RAIL ladder the shipped l5 note
    #    asserted ('ROBUST … pressure-tested') but never ran (Findings 0/2/5/6/9;
    #    reconcile-don't-declare). Reuses the s_rail-independent uncaged 'none' leg5. ──
    uncaged_leg5 = {str(N): l5["by_wall"]["none"][str(N)]["shell_E_par"]
                    for N in (1, 2, 4, 8)}
    out["review_repair_rail_depth_scan"] = rail_depth_scan(
        cP_iso, cS_iso, args.L, uncaged_leg5)

    # ── LEG 3 — wall S-matrix (impedance, clean) + pulse sign / clamped STOP-gate ──
    out["leg3_impedance_smatrix"] = leg3_impedance_smatrix(cP_iso, cS_iso)
    sign = {}
    for wc, clamp in (("symmetric", False), ("bulk_only", False), ("none", True)):
        tag = "clamped" if clamp else wc
        sign[tag] = {
            k: leg3_wall_smatrix(args.L, wc, k, clamp, cP_iso, cS_iso)
            for k in ("P", "S")
        }
    out["leg3_pulse_sign"] = sign
    # ★STOP-gate: rail cages must show Γ_disp SIGN +1 (pressure-release); the clamped
    # control must show the OPPOSITE sign (−1 = rigid/doubling). If not → lane STOPS.
    rail_signs = [sign["symmetric"]["P"]["sign"], sign["symmetric"]["S"]["sign"],
                  sign["bulk_only"]["P"]["sign"], sign["bulk_only"]["S"]["sign"]]
    clamp_signs = [sign["clamped"]["P"]["sign"], sign["clamped"]["S"]["sign"]]
    stop_gate_pass = all(s > 0 for s in rail_signs) and all(s < 0 for s in clamp_signs)
    out["leg3_STOP_gate"] = {
        "rail_disp_signs": rail_signs, "clamped_disp_signs": clamp_signs,
        "image_doubling_opposite_sign_confirmed": bool(stop_gate_pass),
        "interpretation": "rail Γ_disp=+1 ⇔ Γ_stress=−1 (pressure-release ⇒ far-field "
                          "compression MOMENT cancels); clamped Γ_disp=−1 ⇔ "
                          "Γ_stress=+1 (rigid ⇒ compression moment DOUBLES). Opposite "
                          "sign ⇒ mirror realization VALID; lane proceeds.",
    }

    Path(args.out).write_text(json.dumps(out, indent=2))
    make_figure(out, str(Path(args.out).with_name("constituent_cage_ensemble.png")))
    print("spectral cP/cS iso =", round(cP_iso / cS_iso, 4),
          "colorcheck κ²_uncaged =",
          round(out["spectral_cold"]["continuum_import_colorcheck_F_bulk_over_F_shear"], 4))
    sm = out["leg3_impedance_smatrix"]
    print("LEG3 impedance: symmetric Γ_bulk=%+.3f Γ_shear=%+.3f | bulk_only Γ_bulk=%+.3f Γ_shear=%+.3f (asym %.1f×)" % (
        sm["symmetric"]["gamma_bulk"], sm["symmetric"]["gamma_shear"],
        sm["bulk_only"]["gamma_bulk"], sm["bulk_only"]["gamma_shear"],
        sm["bulk_only"]["channel_asymmetry_ratio"]))
    print("LEG3 STOP-gate image-doubling opposite-sign confirmed:",
          out["leg3_STOP_gate"]["image_doubling_opposite_sign_confirmed"])
    l4 = out["leg4_moving_cage"]
    print("LEG4 moving cage: bulk_only f_long=%.3f carry=%.2f | symmetric f_long=%.3f carry=%.2f" % (
        l4["bulk_only"]["shell_f_long"], l4["bulk_only"]["carry_fraction"],
        l4["symmetric"]["shell_f_long"], l4["symmetric"]["carry_fraction"]))
    sc = out["leg5_ensemble_scaling"]["scaling"]
    print("LEG5 ρ_N(bulk_only) N2=%.3f→N8=%.3f trend=%s | p_caged=%.2f p_uncaged=%.2f | "
          "shear_ratio (bulk_only,N8)=%.2f (SUPPRESSED, not ~1)" % (
              sc["rho_bulk_only_N2"], sc["rho_bulk_only_N8"], sc["rho_N_trend_bulk_only"],
              sc["p_caged_bulk_only"], sc["p_uncaged"], sc["shear_ratio_bulk_only_N8"]))
    rd = out["review_repair_rail_depth_scan"]
    gb = rd["impedance_ladder_run_c2_speeds"]["bulk_only"]
    print("REVIEW-REPAIR rail-depth ladder (bulk_only Γ_bulk): " +
          " ".join("s=%s→%+.4f" % (s, gb[s]["gamma_bulk"]) for s in gb) +
          " | cS(s=0)=%.4f FINITE ⇒ canon bulk-only wall realizable: %s" % (
              gb["0"]["cS"],
              rd["finding0_5_bulk_only_gamma_bulk_to_minus1_with_shear_finite"][
                  "canon_bulk_only_wall_realizable"]))
    d = out["leg12_discriminators"]
    print("LEG1 exterior DC∇·u (caged/uncaged): bulk_only=%.3f symmetric=%.3f | "
          "LEG2 single-cage compression seal: bulk_only=%.0f%% symmetric=%.0f%% "
          "(empty sources nothing: %s)" % (
              d["leg1_charged_line_exterior_DCdivu_over_uncaged"]["bulk_only"],
              d["leg1_charged_line_exterior_DCdivu_over_uncaged"]["symmetric"],
              100 * d["leg2_seal_energized_vs_empty"]["bulk_only_single_cage_compression_seal_frac"],
              100 * d["leg2_seal_energized_vs_empty"]["symmetric_single_cage_compression_seal_frac"],
              d["leg2_seal_energized_vs_empty"]["empty_cage_sources_nothing"]))
    return out


if __name__ == "__main__":
    main()
