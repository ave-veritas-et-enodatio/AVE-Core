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
def cage_stiffness(dhat, mid, rho_star, k_s, centers, r_cage, cage_w, wall_class):
    """Per-bond (k_a_bond, k_s_bond) for a set of cages realized by CONSTITUTIVE
    GRADING toward the rail on a ~cage_w-thick shell at r_cage around each center.

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
    rail = 1.0 - (1.0 - S_RAIL) * w  # →S_RAIL on the shell, →1 cold
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
        },
        "spectral_cold": {
            "cP_iso": cP_iso, "cS_iso": cS_iso, "cP_over_cS_iso": cP_iso / cS_iso,
            "cP_over_cS_dir": cpcs_dir,
            "continuum_import_colorcheck_F_bulk_over_F_shear":
                (2.0 / 3.0) * (cS_iso / cP_iso) ** 5,
        },
    }
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
    return out


if __name__ == "__main__":
    main()
