#!/usr/bin/env python3
"""X33 — the clock-architecture discriminator: does the synchronous Op5 walk PIN
the multi-channel band ceiling, or does stiffness LIFT it under one universal tick?

Prereg (FROZEN): research/2026-07-09_x33-clock-architecture_prereg_FROZEN.md
Class: CONSISTENCY / characterization (math + numerics; not a falsification, not
an emergence claim; no CODATA on any verdict path).

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS IS
═══════════════════════════════════════════════════════════════════════════════
The vector band-top of the chiral srs is BRACKETED [5.441, 17.011] ω_C (#607).
The lower endpoint is the normalized-arccos "pin" (π√3, ρ-independent); the upper
is the per-channel-link √ρ* "lift". The survey flagged the tell: "the symmetric
S^{-1/2} normalization divides out the stiffness that should lift the top." This
driver TYPES that tell — is it an honest walk result or an artifact of a bad
normalization choice? — by constructing the honest synchronous coined walk from
the physical (energy-normalized) shunt scatter and computing its EXACT spectrum.

SUBSTRATE-NATIVE (prereg §0): Op5 scatter+connect coined walk. The coin is the
energy-normalized Householder reflection C_i = 2|w_i><w_i| - I, |w_i> stacked from
sqrt(Phi_b) S_i^{-1/2} — FORCED by shunt KCL + unitarity, NOT assumed. The stiffness
ratio rho* enters the coin EIGENVECTORS (band reshaping / velocities) but is locked
out of the coin EIGENVALUES (+/-1) and hence the ceiling. The bipartite pi-mode
(lambda_tilde_max = 2) saturates the eigenphase at pi for ANY rho* => the walk PINS.

The contrast partner is the CONTINUOUS (lumped) architecture omega = sqrt(eig D),
whose ceiling LIFTS as sqrt(stiffness). Both AGREE at long wavelength (VRH
velocities); they diverge only at the zone edge. Each engine confirms its own
architecture; the fork is in-engine-undecidable (Branch S).

alpha-CLEAN: no alpha/Q_TANK on any verdict path. Constants imported by SYMBOL.
Run: PYTHONPATH=src python3 src/scripts/vol_1_foundations/x33_clock_architecture.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

from ave.core.chiral_lattice import _SRS_NN
from ave.core.chiral_lattice_dynamics import ANALYTIC_NETWORK_FACTOR
from ave.core.constants import HBAR, OMEGA_C, e_charge

# survey building blocks (Rule 14 reuse of the VALIDATED srs vector pipeline)
_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
from srs_vector_band_survey import (  # noqa: E402  (script-local import)
    B1,
    B2,
    B3,
    srs_primitive_bcc,
    self_block_isqrt,
    vector_bloch_D,
)

FAC = ANALYTIC_NETWORK_FACTOR            # 1/sqrt(3), imported (never hard-coded)
OMEGA_LINK_OVER_C = 1.0 / FAC            # omega_link/omega_C = sqrt(3)
MEV_PER_OMEGA_C = HBAR * OMEGA_C / e_charge / 1e6  # ~0.511 MeV/omega_C (m_e c^2 IDENTITY)
RHO_STAR_CANON = 9.77337                 # canonical bond ratio (survey G6; derived from N_NU=2/7)
RHO_SET = [1.0, RHO_STAR_CANON, 100.0, 1000.0]
PIN_TOL = 1e-6                           # frozen adjudication threshold (prereg §4)


# ─────────────────────────────────────────────────────────────────────────────
# symmetric matrix roots
# ─────────────────────────────────────────────────────────────────────────────
def _sqrtm(M):
    w, V = np.linalg.eigh(0.5 * (M + M.conj().T))
    return V @ np.diag(np.sqrt(np.clip(w.real, 0.0, None))) @ V.conj().T


def _isqrtm(M):
    w, V = np.linalg.eigh(0.5 * (M + M.conj().T))
    return V @ np.diag(1.0 / np.sqrt(np.clip(w.real, 1e-12, None))) @ V.conj().T


# ─────────────────────────────────────────────────────────────────────────────
# (i) 1D TWO-CHANNEL zig-zag chain  (PRIMARY, tractable, exactly solvable)
#     2 sites/cell (A,B) x 2 DOF. Bonds tilt +/- theta so Phi mixes axial & shear;
#     the coin genuinely carries rho* and the two acoustic branches have c_L != c_T.
# ─────────────────────────────────────────────────────────────────────────────
ZZ_THETA = np.deg2rad(35.0)


def _zz_geometry():
    d1 = np.array([np.cos(ZZ_THETA), np.sin(ZZ_THETA)])   # A(0) -> B(0)
    d2 = np.array([np.cos(ZZ_THETA), -np.sin(ZZ_THETA)])  # B(0) -> A(1)
    acell = 2.0 * np.cos(ZZ_THETA)
    # (site_i, site_j, delta_cart, cell_shift_along_x)   sites: 0=A, 1=B
    bonds = [(0, 1, d1, 0.0), (1, 0, d2, 1.0)]
    return bonds, acell


def _zz_Phi(dn, ka, ks):
    P = np.outer(dn, dn)
    return ka * P + ks * (np.eye(2) - P)


def zz_D(kx, ka, ks):
    """4x4 continuous (lumped) dynamical matrix of the zig-zag chain."""
    bonds, acell = _zz_geometry()
    D = np.zeros((4, 4), complex)
    for (i, j, dl, nc) in bonds:
        dn = dl / np.linalg.norm(dl)
        P = _zz_Phi(dn, ka, ks)
        ph = np.exp(1j * kx * acell * nc)
        D[2 * i:2 * i + 2, 2 * j:2 * j + 2] += -P * ph
        D[2 * j:2 * j + 2, 2 * i:2 * i + 2] += -P.conj().T * np.conj(ph)
        D[2 * i:2 * i + 2, 2 * i:2 * i + 2] += P
        D[2 * j:2 * j + 2, 2 * j:2 * j + 2] += P
    return 0.5 * (D + D.conj().T)


def zz_selfblock(ka, ks):
    bonds, _ = _zz_geometry()
    S = np.zeros((4, 4))
    for (i, j, dl, nc) in bonds:
        dn = dl / np.linalg.norm(dl)
        P = _zz_Phi(dn, ka, ks)
        S[2 * i:2 * i + 2, 2 * i:2 * i + 2] += P
        S[2 * j:2 * j + 2, 2 * j:2 * j + 2] += P
    return S


def zz_bands(kx, ka, ks):
    """(omega_continuous, theta_walk, lambda_tilde). theta_walk = omega/omega_link."""
    D = zz_D(kx, ka, ks)
    w2 = np.sort(np.clip(np.linalg.eigvalsh(D).real, 0.0, None))
    cont = np.sqrt(w2)
    Sih = _isqrtm(zz_selfblock(ka, ks))
    Dn = Sih @ D @ Sih
    Dn = 0.5 * (Dn + Dn.conj().T)
    lam = np.sort(np.clip(np.linalg.eigvalsh(Dn).real, 0.0, 2.0))
    theta = np.arccos(np.clip(1.0 - lam, -1.0, 1.0))   # eigenphase in [0, pi]
    return cont, theta, lam


def zz_scan(ka, ks, n_k=241):
    _, acell = _zz_geometry()
    kxs = np.linspace(0.0, np.pi / acell, n_k)
    cont = np.array([zz_bands(kx, ka, ks)[0] for kx in kxs])
    walk = np.array([zz_bands(kx, ka, ks)[1] for kx in kxs])
    lam = np.array([zz_bands(kx, ka, ks)[2] for kx in kxs])
    return kxs, cont, walk, lam


# ─────────────────────────────────────────────────────────────────────────────
# (ii) LITERAL energy-normalized vector coined-walk UNITARY  (G2: derive, don't assume)
#      Built on the arc (directed-bond) space of the srs primitive cell. The coin is
#      the Householder reflection carrying rho* via sqrt(Phi_b); the shift is the
#      arc-reversal permutation with Bloch phase. Its eigenphases MUST equal
#      +/- arccos(eig[S^{-1/2} A(k) S^{-1/2}]) if the arccos map is the honest walk.
# ─────────────────────────────────────────────────────────────────────────────
def _srs_arcs(bonds):
    arcs = [(i, j, np.array(d, float)) for (i, j, d) in bonds]
    rev = []
    for (i, j, d) in arcs:
        match = next(b for b, (i2, j2, d2) in enumerate(arcs)
                     if i2 == j and j2 == i and np.allclose(d2, -d))
        rev.append(match)
    return arcs, rev


def srs_walk_unitary(kvec, basis, bonds, arcs, rev, ka, ks, dof=3):
    A = len(arcs)
    outs = {i: [a for a, (ii, jj, d) in enumerate(arcs) if ii == i] for i in range(len(basis))}
    C = np.zeros((A * dof, A * dof), complex)
    for i, aidx in outs.items():
        Phis = []
        for a in aidx:
            (_, _, d) = arcs[a]
            dn = d / np.linalg.norm(d)
            P = np.outer(dn, dn)
            Phis.append(ka * P + ks * (np.eye(3) - P))
        Sih = _isqrtm(sum(Phis))
        W = np.vstack([_sqrtm(P) @ Sih for P in Phis])   # (z*dof) x dof isometry
        Csub = 2.0 * (W @ W.conj().T) - np.eye(len(aidx) * dof)
        for p, a in enumerate(aidx):
            for q, b in enumerate(aidx):
                C[a * dof:(a + 1) * dof, b * dof:(b + 1) * dof] = \
                    Csub[p * dof:(p + 1) * dof, q * dof:(q + 1) * dof]
    Sh = np.zeros((A * dof, A * dof), complex)
    for a, (i, j, d) in enumerate(arcs):
        ph = np.exp(1j * np.dot(kvec, d))
        Sh[rev[a] * dof:(rev[a] + 1) * dof, a * dof:(a + 1) * dof] = ph * np.eye(dof)
    return Sh @ C


def srs_arccos_phases(kvec, basis, bonds, ka, ks):
    """+arccos(eig Atilde), Atilde = I - S^{-1/2} D S^{-1/2}  (the 12 mapped eigenphases)."""
    D = vector_bloch_D(kvec, basis, bonds, ka, ks)
    Sih, _ = self_block_isqrt(basis, bonds, ka, ks)
    At = np.eye(3 * len(basis)) - Sih @ D @ Sih
    At = 0.5 * (At + At.conj().T)
    return np.sort(np.arccos(np.clip(np.linalg.eigvalsh(At).real, -1.0, 1.0)))


# ─────────────────────────────────────────────────────────────────────────────
# srs ceilings across rho* (the verdict quantity) + continuous lift
# ─────────────────────────────────────────────────────────────────────────────
def srs_ceilings(basis, bonds, ka, ks, n_grid=12):
    Sih, _ = self_block_isqrt(basis, bonds, ka, ks)
    lam_tilde_max, lump_max = -1.0, -1.0
    fs = np.linspace(0.0, 1.0, n_grid, endpoint=False)
    for f1 in fs:
        for f2 in fs:
            for f3 in fs:
                k = f1 * B1 + f2 * B2 + f3 * B3
                D = vector_bloch_D(k, basis, bonds, ka, ks)
                lump_max = max(lump_max, float(np.linalg.eigvalsh(D).real.max()))
                Dn = Sih @ D @ Sih
                Dn = 0.5 * (Dn + Dn.conj().T)
                lam_tilde_max = max(lam_tilde_max, float(np.linalg.eigvalsh(Dn).real.max()))
    walk_top = OMEGA_LINK_OVER_C * float(np.arccos(np.clip(1.0 - lam_tilde_max, -1.0, 1.0)))
    return {"lambda_tilde_max": lam_tilde_max, "walk_top_omega_C": walk_top,
            "lump_lambda_max": lump_max, "continuous_top_sqrt_units": float(np.sqrt(lump_max))}


# ─────────────────────────────────────────────────────────────────────────────
# GATES
# ─────────────────────────────────────────────────────────────────────────────
def gate1_scalar_limit(basis, bonds):
    """G1: single channel (k_a=k_s) reduces to the validated scalar arccos band."""
    srs = srs_ceilings(basis, bonds, 1.0, 1.0)
    srs_top = srs["walk_top_omega_C"]
    # velocity factor (arccos low-k slope), same construction as the scalar survey gate (i)
    ell = _SRS_NN
    facs = []
    for qh in ([1, 0, 0], [1, 1, 0], [1, 1, 1]):
        q = np.array(qh, float) / np.linalg.norm(qh)
        D = vector_bloch_D(q * (1e-4 / ell), basis, bonds, 1.0, 1.0)
        Sih, _ = self_block_isqrt(basis, bonds, 1.0, 1.0)
        Dn = Sih @ D @ Sih
        lam_ac = np.sort(np.clip(np.linalg.eigvalsh(0.5 * (Dn + Dn.conj().T)).real, 0, 2))[0]
        facs.append(float(np.arccos(np.clip(1 - lam_ac, -1, 1)) / (1e-4)))
    vfac = float(np.mean(facs))
    # 1D chain scalar limit: top theta = pi
    _, _, walk_iso, _ = zz_scan(1.0, 1.0)
    zz_top = float(walk_iso.max())
    ok = (abs(srs_top - np.pi * np.sqrt(3)) < 1e-4
          and abs(vfac - FAC) < 1e-3
          and abs(zz_top - np.pi) < 1e-4)
    return {"srs_walk_top_omega_C": srs_top, "srs_target_pi_sqrt3": float(np.pi * np.sqrt(3)),
            "srs_velocity_factor": vfac, "target_1_over_sqrt3": float(FAC),
            "zz_walk_top_theta": zz_top, "zz_target_pi": float(np.pi), "pass": bool(ok)}


def gate2_walk_is_scatter_connect(basis, bonds):
    """G2: literal energy-normalized coined-walk UNITARY eigenphases == +/-arccos(eig Atilde)."""
    arcs, rev = _srs_arcs(bonds)
    rng = np.random.default_rng(33)
    unit_err, match_err, pin_at_pi = 0.0, 0.0, {}
    for rho in RHO_SET:
        mx = -1.0
        for _ in range(6):
            k = rng.standard_normal(3) * 2.0
            U = srs_walk_unitary(k, basis, bonds, arcs, rev, rho, 1.0)
            unit_err = max(unit_err, float(np.max(np.abs(U @ U.conj().T - np.eye(U.shape[0])))))
            wp = np.sort(np.abs(np.angle(np.linalg.eigvals(U))))
            mx = max(mx, float(wp.max()))
            for v in srs_arccos_phases(k, basis, bonds, rho, 1.0):
                match_err = max(match_err, float(np.min(np.abs(wp - v))))
        pin_at_pi[f"{rho:g}"] = mx / np.pi
    ok = unit_err < 1e-12 and match_err < 1e-12
    return {"unitarity_err": unit_err, "arccos_match_err": match_err,
            "literal_walk_max_phase_over_pi": pin_at_pi, "pass": bool(ok)}


def gate3_lowk_agreement(basis, bonds, rho=RHO_STAR_CANON):
    """G3: walk & continuous give the SAME acoustic velocities at long wavelength (single scale)."""
    ell = _SRS_NN
    Sih, _ = self_block_isqrt(basis, bonds, rho, 1.0)
    ratios = []
    for qh in ([1, 0, 0], [1, 1, 0], [1, 1, 1]):
        q = np.array(qh, float) / np.linalg.norm(qh)
        kvec = q * (1e-4 / ell)
        D = vector_bloch_D(kvec, basis, bonds, rho, 1.0)
        v_cont = np.sqrt(np.sort(np.clip(np.linalg.eigvalsh(D).real, 0, None))[:3]) / (1e-4 / ell)
        Dn = Sih @ D @ Sih
        lam = np.sort(np.clip(np.linalg.eigvalsh(0.5 * (Dn + Dn.conj().T)).real, 0, 2))[:3]
        v_walk = OMEGA_LINK_OVER_C * np.arccos(np.clip(1 - lam, -1, 1)) / (1e-4 / ell)
        ratios.extend((v_walk / v_cont).tolist())
    ratios = np.array(ratios)
    spread = float((ratios.max() - ratios.min()) / ratios.mean())
    return {"walk_over_cont_ratio_mean": float(ratios.mean()), "spread": spread,
            "n_samples": int(ratios.size), "pass": bool(spread < 1e-5)}


def gate6_coin_eigenvalues(basis, bonds):
    """G6: coin eigenvalues are +/-1 independent of rho* (the pin locus)."""
    arcs, _ = _srs_arcs(bonds)
    aidx0 = [a for a, (i, j, d) in enumerate(arcs) if i == 0]
    res, ok = {}, True
    for rho in RHO_SET:
        Phis = []
        for a in aidx0:
            (_, _, d) = arcs[a]
            dn = d / np.linalg.norm(d)
            P = np.outer(dn, dn)
            Phis.append(rho * P + 1.0 * (np.eye(3) - P))
        Sih = _isqrtm(sum(Phis))
        W = np.vstack([_sqrtm(P) @ Sih for P in Phis])
        C = 2.0 * (W @ W.conj().T) - np.eye(len(aidx0) * 3)
        ev = np.round(np.sort(np.linalg.eigvalsh(C).real), 9)
        res[f"{rho:g}"] = ev.tolist()
        ok = ok and np.allclose(np.abs(ev), 1.0, atol=1e-9)
    return {"coin_eigs_per_rho": res, "pass": bool(ok),
            "note": "+1 (D-fold), -1 ((z-1)D-fold) for ALL rho* -> stiffness is locked out of the eigenvalues"}


# ─────────────────────────────────────────────────────────────────────────────
def main():
    basis, bonds = srs_primitive_bcc("right")
    out = {"class": "CONSISTENCY / characterization",
           "prereg": "research/2026-07-09_x33-clock-architecture_prereg_FROZEN.md",
           "omega_link_over_omega_C": OMEGA_LINK_OVER_C, "MeV_per_omega_C": MEV_PER_OMEGA_C,
           "rho_set": RHO_SET}

    # ---- verdict quantity: srs ceilings vs rho* (walk pins? continuous lifts?) ----
    ceil = {f"{r:g}": srs_ceilings(basis, bonds, r, 1.0) for r in RHO_SET}
    walk_tops = np.array([ceil[f"{r:g}"]["walk_top_omega_C"] for r in RHO_SET])
    cont_tops = np.array([ceil[f"{r:g}"]["continuous_top_sqrt_units"] for r in RHO_SET])
    pin_ref = np.pi * OMEGA_LINK_OVER_C          # pi * sqrt(3) = the tick Nyquist
    walk_flat = float(np.max(np.abs(walk_tops - pin_ref)) / pin_ref)
    cont_lift = float(cont_tops[-1] / cont_tops[0])
    out["srs_ceilings_vs_rho"] = ceil
    out["verdict_metrics"] = {
        "walk_top_omega_C_per_rho": walk_tops.tolist(),
        "walk_deviation_from_pi_sqrt3": walk_flat,
        "pin_reference_pi_sqrt3_omega_C": float(pin_ref),
        "continuous_top_per_rho": cont_tops.tolist(),
        "continuous_lift_ratio_1000_over_1": cont_lift}

    branch = "S_walk_PINS" if walk_flat < PIN_TOL else "L_walk_LIFTS"
    out["BRANCH"] = branch

    # ---- gates ----
    g1 = gate1_scalar_limit(basis, bonds)
    g2 = gate2_walk_is_scatter_connect(basis, bonds)
    g3 = gate3_lowk_agreement(basis, bonds)
    # G4 continuous lifts / G5 bipartite pin locus are read from verdict metrics
    g4 = {"continuous_lift_ratio": cont_lift, "pass": bool(cont_lift > 3.0)}
    g5 = {"lambda_tilde_max_per_rho": [ceil[f"{r:g}"]["lambda_tilde_max"] for r in RHO_SET],
          "max_dev_from_2": float(max(abs(ceil[f"{r:g}"]["lambda_tilde_max"] - 2.0) for r in RHO_SET)),
          "pass": bool(max(abs(ceil[f"{r:g}"]["lambda_tilde_max"] - 2.0) for r in RHO_SET) < 1e-6)}
    g6 = gate6_coin_eigenvalues(basis, bonds)
    out["gates"] = {"G1_scalar_limit": g1, "G2_walk_is_scatter_connect": g2,
                    "G3_lowk_agreement": g3, "G4_continuous_lifts": g4,
                    "G5_bipartite_pin_locus": g5, "G6_coin_eigenvalue_locus": g6}
    out["all_gates_pass"] = bool(g1["pass"] and g2["pass"] and g3["pass"]
                                 and g4["pass"] and g5["pass"] and g6["pass"])

    # ---- discriminating observable: the longitudinal-only window ----
    # under CONTINUOUS the stiff axial band tops out ABOVE the shear top -> a window
    # [shear_top, axial_top] where ONLY the longitudinal band exists. Under the WALK
    # both top out at pi*omega_link -> no such window.
    lifted_top = 17.0111   # per-channel-link sqrt(rho*) upper bracket (survey §3)
    out["discriminating_observable_longitudinal_only_window"] = {
        "definition": "frequency band where only the longitudinal (k_a-dominated) branch propagates",
        "under_continuous_lifted_MeV": [round(pin_ref * MEV_PER_OMEGA_C, 4),
                                        round(lifted_top * MEV_PER_OMEGA_C, 4)],
        "under_walk_pinned_MeV": "ABSENT (all branches end at pi*omega_link = %.4f MeV)"
                                 % (pin_ref * MEV_PER_OMEGA_C),
        "note": ("EXISTS under continuous/lifted, ABSENT under walk/pinned. This is the "
                 "in-engine-UNDECIDABLE fork's empirical discriminator (Branch S).")}

    # ---- 1D two-channel spectra for the figure + a compact record ----
    fig_data = {}
    for r in [1.0, RHO_STAR_CANON]:
        kxs, cont, walk, _ = zz_scan(r, 1.0)
        fig_data[f"{r:g}"] = {"kx": kxs.tolist(), "cont": cont.tolist(),
                              "walk_theta": walk.tolist(),
                              "cont_top": float(cont.max()), "walk_top_theta": float(walk.max())}
    out["zz_1d_two_channel"] = {
        "theta_deg": float(np.rad2deg(ZZ_THETA)),
        "iso_walk_top_theta": fig_data["1"]["walk_top_theta"],
        "iso_cont_top": fig_data["1"]["cont_top"],
        "rho_walk_top_theta": fig_data[f"{RHO_STAR_CANON:g}"]["walk_top_theta"],
        "rho_cont_top": fig_data[f"{RHO_STAR_CANON:g}"]["cont_top"],
        "walk_pins_note": "walk theta ceiling = pi for BOTH rho* (pinned); continuous top lifts"}

    out["Op5_clock_type"] = (
        "PINNING clock (synchronous discrete-time unitary walk). The Op5 scatter+connect "
        "engine reports the pinned ceiling pi*omega_link = pi*sqrt3*omega_C for ANY rho* and "
        "CANNOT see the stiffness lift; the lifted reading requires a continuous-time "
        "(omega=sqrt eig D) solver. The bracket [5.441, 17.011] omega_C is an ARCHITECTURE fork, "
        "in-engine-undecidable — resolved only by Grant/corpus anchor (Branch S).")

    # ---- report ----
    print("=" * 78)
    print("X33 — CLOCK-ARCHITECTURE DISCRIMINATOR (synchronous walk: PIN vs LIFT)")
    print("=" * 78)
    print(f"\nVERDICT: BRANCH {branch}")
    print(f"  walk top (omega_C) per rho* {RHO_SET}: {np.round(walk_tops, 6).tolist()}")
    print(f"    deviation from pi*sqrt3={pin_ref:.5f}: {walk_flat:.2e}  (PIN if < {PIN_TOL:.0e})")
    print(f"  continuous top (sqrt units) per rho*: {np.round(cont_tops, 4).tolist()}")
    print(f"    lift ratio (rho=1000 / rho=1): {cont_lift:.2f}x  => LIFTS")
    print("\nGATES:")
    print(f"  G1 scalar-limit           : srs top={g1['srs_walk_top_omega_C']:.5f} (pi*sqrt3), "
          f"vfac={g1['srs_velocity_factor']:.6f} (1/sqrt3), 1D top={g1['zz_walk_top_theta']:.5f} (pi)  "
          f"PASS={g1['pass']}")
    print(f"  G2 walk=scatter+connect   : unit_err={g2['unitarity_err']:.1e}, "
          f"arccos_match={g2['arccos_match_err']:.1e}, max_phase/pi={g2['literal_walk_max_phase_over_pi']}  "
          f"PASS={g2['pass']}")
    print(f"  G3 low-k agreement        : walk/cont ratio spread={g3['spread']:.2e} "
          f"({g3['n_samples']} samples)  PASS={g3['pass']}")
    print(f"  G4 continuous LIFTS       : lift ratio={g4['continuous_lift_ratio']:.2f}x  PASS={g4['pass']}")
    print(f"  G5 bipartite pin locus    : lambda_tilde_max dev from 2 = {g5['max_dev_from_2']:.1e}  "
          f"PASS={g5['pass']}")
    print(f"  G6 coin eigenvalue locus  : eigs=+/-1 for all rho*  PASS={g6['pass']}")
    print(f"    coin eigs (rho*={RHO_STAR_CANON:g}): {g6['coin_eigs_per_rho'][f'{RHO_STAR_CANON:g}']}")
    print(f"\nALL GATES PASS: {out['all_gates_pass']}")
    print(f"\nDiscriminating observable (longitudinal-only window): "
          f"continuous={out['discriminating_observable_longitudinal_only_window']['under_continuous_lifted_MeV']} MeV, "
          f"walk=ABSENT")
    print(f"\nOp5 clock type: PINNING (synchronous unitary walk) -> bracket is an architecture fork")

    out_dir = Path(__file__).resolve().parent / "_output"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "x33_clock_architecture.json").write_text(json.dumps(out, indent=2))
    print(f"\nResults: {out_dir / 'x33_clock_architecture.json'}")

    try:
        make_figure(fig_data, out, out_dir)
    except Exception as e:  # pragma: no cover
        print(f"[figure skipped: {e}]")
    return out


# ─────────────────────────────────────────────────────────────────────────────
def make_figure(fig_data, out, out_dir):
    """WHITE house style: the two architectures' 1D two-channel spectra overlaid.

    ONE fixed calibration (NOT re-fit per panel): the continuous elastic units are
    converted to omega_C by matching the shared long-wavelength acoustic slope at
    rho*=1 (the VRH velocity both architectures agree on, G3). The SAME factor is
    applied in both panels, so the pin (walk top flat) vs lift (continuous top
    rising) is an honest visual comparison, not a per-panel re-scaling.
    """
    from ave.viz import style
    style.apply()
    _, acell = _zz_geometry()
    pin = np.pi * OMEGA_LINK_OVER_C     # tick Nyquist = pi*sqrt3 omega_C

    # fixed calibration R: low-k acoustic slope ratio (walk omega)/(continuous omega) at rho*=1
    kx_lo = 1e-3 * np.pi / acell
    c_lo, th_lo, _ = zz_bands(kx_lo, 1.0, 1.0)
    ac_cont = np.sqrt(np.sort(c_lo ** 2))[1]           # lowest non-zero acoustic branch
    ac_walk = OMEGA_LINK_OVER_C * np.sort(th_lo)[1]
    R = float(ac_walk / ac_cont)
    out["zz_1d_two_channel"]["continuous_to_omega_C_calibration"] = R

    fig, axes = style.plt.subplots(1, 2, figsize=style.figsize("wide"), sharey=True)
    ymax = 0.0
    for rho in ("1", f"{RHO_STAR_CANON:g}"):
        ymax = max(ymax, np.array(fig_data[rho]["cont"]).max() * R, pin)
    ymax *= 1.10

    for ax, rho, tag in ((axes[0], "1", r"$\rho^*=1$"),
                         (axes[1], f"{RHO_STAR_CANON:g}", r"$\rho^*=9.77$")):
        fd = fig_data[rho]
        kx = np.array(fd["kx"]) * acell / np.pi         # zone edge at 1
        walk = np.array(fd["walk_theta"]) * OMEGA_LINK_OVER_C
        contN = np.array(fd["cont"]) * R
        for b in range(walk.shape[1]):
            ax.plot(kx, contN[:, b], color=style.COLORS["comparison"], lw=1.5, ls="--",
                    label="continuous (LIFTS)" if b == 0 else None)
            ax.plot(kx, walk[:, b], color=style.COLORS["ave"], lw=1.8,
                    label="synchronous walk (PINS)" if b == 0 else None)
        ax.axhline(pin, color=style.COLORS["data"], ls=":", lw=1.0)
        ax.text(0.03, 0.94, tag, transform=ax.transAxes, ha="left", va="top", fontsize=10)
        ax.set_xlabel(r"$k$  ($\pi/a$)")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, ymax)
    axes[0].text(0.03, pin / ymax + 0.015, r"tick Nyquist $\pi\sqrt{3}\,\omega_C$",
                 transform=axes[0].transAxes, ha="left", va="bottom", fontsize=8,
                 color=style.COLORS["data"])
    axes[0].set_ylabel(style.axis_label("frequency", r"\omega", r"$\omega_C$"))
    style.legend(axes[1], where="right")
    paths = style.save(fig, out_dir / "x33_clock_architecture")
    print(f"Figure: {paths}")


if __name__ == "__main__":
    main()
