#!/usr/bin/env python
"""Overlap-integral lane driver — the compression-line mode-overlap integral.

Prereg (FROZEN, committed+pushed ALONE before this file existed):
    research/2026-08-08_overlap-integral_prereg-FROZEN.md  (commit 52e9c1cb)

SECTOR HEADER (substrate-native declaration, #761 discipline):
    Lattice = finite srs (z=3) net, 8-site I4_1 32 Wyckoff-8a motif tiled over
    L^3 conventional cells; each bond carries the substrate-native RANK-2 bond
    tensor  Phi_b = k_a (dhat x dhat) + k_s (I - dhat x dhat)  — NOT a Cartesian
    Laplacian.  Sector = translational displacement u (the vector branch whose
    longitudinal polarization carries the A1 dilatation).  Cosserat
    micro-rotation is NOT driven and NOT read (rotational fence, prereg SS11-1).
    Saturation OFF (cold-linear, A ~ 1e-3 class; kernel-member fence prereg
    SS0 row 2).  Engine src/ave byte-untouched: imports ave.core.chiral_lattice
    (_SRS_8A, _SRS_NN) read-only; Rule-14 reuse of the validated #761 finite-net
    + Bloch-survey pipelines.

THREE ARMS (prereg SS7):
    A (spectral)   — the mode-overlap integral computed directly against the
                     lattice's own Bloch longitudinal eigenvectors on the
                     propagating shell |k| = w_d / c_P(khat):
                       O(k) = sum_shell (e_L . nhat_s) P(nhat_s) exp(-i k.x_s)
                     for P in {Y00 (RADIAL-AC class), Y22 (COMMUTATION class)};
                     rho_spec(kR) = int|O_22|^2 / int|O_00|^2  vs the continuum
                     closed form |j_2'(kR)/j_0'(kR)|^2.
    B (time domain)— driven radiation on the finite net: 3-cycle tone burst of
                     radial FORCE on the port shell (r_port = 3 cells), three
                     patterns: (a) RADIAL-AC l=0 standing, (b) COMMUTATION l=2
                     m=+2 rotating at Omega = w_d/2 (nodes see 2*Omega = w_d),
                     (c) STATIC l=2 ramp-hold control.  Longitudinal radiated
                     energy at r_meas = 12 in the analytic spectral window.
    C (eccentricity)— Kepler-orbit averages of the third-derivative moment
                     invariants vs the frozen symbolic forms (G-ECC).

FROZEN-GRID DISCLOSURE (prereg SS11 fence 6; the #761 SS4.0-1 precedent):
    The prereg froze L = 48 for arm B.  The window budget (computed below,
    shipped in the JSON) shows L = 48 cannot contain a full 3-cycle burst
    before the boundary reflection returns; the operative grid is enlarged to
    L = 64 (conservative: a larger box only delays reflections) and the frozen
    L = 48 grid is ALSO run (2-cycle burst, truncation disclosed) as the
    frozen-grid diagnostic.  Both are reported.

Ships:  overlap_integral_lattice_results.json  (+ _number_check.py gate).
Run:    PYTHONPATH=<worktree>/src python research/drivers/overlap_integral_lattice.py
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.spatial import cKDTree
from scipy.special import spherical_jn

# -- engine reads (read-only) ------------------------------------------------
from ave.core.chiral_lattice import _SRS_8A, _SRS_NN

# -- Rule-14 reuse of the VALIDATED survey pipeline (side-effect-free imports)
_VOL1 = (
    Path(__file__).resolve().parents[2]
    / "src" / "scripts" / "vol_1_foundations"
)
sys.path.insert(0, str(_VOL1))
from srs_band_survey import srs_primitive_bcc  # noqa: E402
from srs_vector_band_survey import (  # noqa: E402
    derive_rho_star,
    vector_bloch_D,
)

TOL = 1e-9

# Frozen direction-resolved speed gate (prereg SS10 G-SPEC; #761 R3(b) values)
SURVEY_CP_CS = {"100": 1.7105, "110": 1.8528, "111": 1.9041}

# Frozen parameters (prereg SS7)
R_PORT = 3.0            # port-shell radius (cells)
R_MEAS = 12.0           # measurement-shell radius (cells)
SHELL_W = 1.0           # shell width (cells)
KR_SWEEP = (1.0, 1.5, 2.2, 2.6)   # spectral-arm kR_port sweep
KR_TD = 2.6             # time-domain operating point
L_FROZEN = 48           # frozen arm-B grid (diagnostic; window-truncated)
L_OPER = 64             # operative arm-B grid (forced deviation, conservative)
N_FIB = 2000            # Fibonacci directions for the spectral integral
ECC_SWEEP = (0.0, 0.05, 0.088, 0.3, 0.6171)


# ============================================================================
# Finite srs net + rank-2 bond dynamics (Rule-14 reuse of #761 conventions)
# ============================================================================
def build_finite_srs(L: int):
    """(pos[N,3], bi[M], bj[M], dhat[M,3]) — identical construction to #761."""
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
    return pos, pairs[:, 0].copy(), pairs[:, 1].copy(), dhat


def bond_tensors(dhat, k_a, k_s):
    P = np.einsum("bi,bj->bij", dhat, dhat)
    return k_a * P + k_s * (np.eye(3)[None] - P)


def forces(u, Phi, bi, bj, N):
    """F_s = -sum_b Phi_b (u_s - u_t).  bincount scatter (large-grid speed;
    algebraically identical to the #761 np.add.at form)."""
    du = u[bi] - u[bj]
    fb = np.einsum("bij,bj->bi", Phi, du)
    F = np.empty((N, 3))
    for c in range(3):
        F[:, c] = (np.bincount(bj, weights=fb[:, c], minlength=N)
                   - np.bincount(bi, weights=fb[:, c], minlength=N))
    return F


def omega_max_power_iter(Phi, bi, bj, N, iters=60, seed=3):
    rng = np.random.default_rng(seed)
    x = rng.standard_normal((N, 3))
    x /= np.linalg.norm(x)
    lam = 0.0
    for _ in range(iters):
        y = -forces(x, Phi, bi, bj, N)
        lam = float(np.linalg.norm(y))
        x = y / (lam + 1e-300)
    return np.sqrt(lam)


# ============================================================================
# Spherical-harmonic patterns (explicit forms; complex Y22, real Y00)
# ============================================================================
def y00(nhat):
    return np.full(nhat.shape[0], 1.0 / np.sqrt(4.0 * np.pi))


def y22(nhat):
    """Complex Y_2^2 = (1/4) sqrt(15/2pi) sin^2(theta) e^{2i phi}."""
    x, y, z = nhat[:, 0], nhat[:, 1], nhat[:, 2]
    return 0.25 * np.sqrt(15.0 / (2.0 * np.pi)) * (x + 1j * y) ** 2


def real_harmonics_l012(nhat):
    """The 9 real harmonics l = 0,1,2 on unit vectors (G-MOMENT Gram basis)."""
    x, y, z = nhat[:, 0], nhat[:, 1], nhat[:, 2]
    c0 = 1.0 / np.sqrt(4 * np.pi)
    c1 = np.sqrt(3.0 / (4 * np.pi))
    out = [np.full_like(x, c0), c1 * x, c1 * y, c1 * z,
           0.5 * np.sqrt(15 / np.pi) * x * y,
           0.5 * np.sqrt(15 / np.pi) * y * z,
           0.25 * np.sqrt(5 / np.pi) * (3 * z**2 - 1),
           0.5 * np.sqrt(15 / np.pi) * x * z,
           0.25 * np.sqrt(15 / np.pi) * (x**2 - y**2)]
    return np.stack(out, axis=1)  # (N, 9)


def fibonacci_sphere(n):
    i = np.arange(n) + 0.5
    phi = np.pi * (3.0 - np.sqrt(5.0)) * i
    z = 1.0 - 2.0 * i / n
    r = np.sqrt(np.clip(1.0 - z * z, 0, None))
    return np.stack([r * np.cos(phi), r * np.sin(phi), z], axis=1)


# ============================================================================
# ARM A — the spectral mode-overlap integral (prereg SS7 Arm 2A)
# ============================================================================
def port_shell_sites(L_shell=12):
    """Port-shell site positions/normals from a finite srs net (center-relative)."""
    pos, _, _, _ = build_finite_srs(L_shell)
    center = np.array([L_shell / 2.0] * 3)
    rel = pos - center
    r = np.linalg.norm(rel, axis=1)
    sel = (r >= R_PORT - SHELL_W / 2) & (r < R_PORT + SHELL_W / 2)
    xs = rel[sel]
    nhat = xs / np.linalg.norm(xs, axis=1, keepdims=True)
    return xs, nhat


def longitudinal_eig(kvec, basis, bonds, rho_star, k_s):
    """(c_P, e_L) at the given k: longitudinal acoustic branch by max |pol.khat|^2.
    Long-wave polarization = site-uniform part (mean over the 4 sublattice
    blocks — the #761 C-2 convention; finite-k sublattice texture is part of
    the declared O((k*l_site)^2) correction budget)."""
    kn = np.linalg.norm(kvec)
    kh = kvec / kn
    D = vector_bloch_D(kvec, basis, bonds, rho_star, k_s)
    w2, V = np.linalg.eigh(D)
    idx = np.argsort(w2)[:3]
    w2a, Va = w2[idx], V[:, idx]
    pol = Va.reshape(4, 3, 3).mean(axis=0)
    pol = pol / (np.linalg.norm(pol, axis=0, keepdims=True) + 1e-30)
    long_frac = np.abs(pol.T @ kh) ** 2
    pL = int(np.argmax(long_frac))
    cP = float(np.sqrt(max(w2a[pL], 0.0)) / kn)
    eL = pol[:, pL].astype(complex)
    # fix overall sign/phase: align with +khat
    ph = eL @ kh
    if abs(ph) > 1e-12:
        eL = eL * (np.conj(ph) / abs(ph))
    return cP, eL, float(long_frac[pL])


def arm_A_spectral(rho_star, k_s=1.0, n_fib=N_FIB):
    """rho_spec(kR) = int|O_22|^2 dOmega / int|O_00|^2 dOmega on the propagating
    longitudinal shell, vs the continuum reference |j2'(kR)/j0'(kR)|^2."""
    basis, bonds = srs_primitive_bcc("right")
    xs, nhat = port_shell_sites()
    n_shell = xs.shape[0]

    # unit-L2-normalized patterns over the discrete shell
    p00 = y00(nhat); p00 = p00 / np.linalg.norm(p00)
    p22 = y22(nhat); p22 = p22 / np.linalg.norm(p22)

    # G-MOMENT: Gram conditioning + discrete l=2 moment fidelity
    H = real_harmonics_l012(nhat)                      # (n_shell, 9)
    G = H.T @ H
    gram_cond = float(np.linalg.cond(G))
    # discrete-vs-continuum norm ratio for the l=2 pattern (continuum: uniform
    # site measure on the sphere would give ||Y22||^2 * n_shell / (4pi) after
    # L2 normalization conventions; report the direct Gram diagonal fidelity)
    y22_disc = np.abs(y22(nhat)) ** 2
    l2_fidelity = float(y22_disc.sum() * (4 * np.pi / n_shell)
                        / 1.0)  # int|Y22|^2 dOmega = 1 continuum reference

    # small-k speeds per direction (one Bloch solve each), then finite-k eigvec
    dirs = fibonacci_sphere(n_fib)
    for extra in ([1, 0, 0], [1, 1, 0], [1, 1, 1]):
        v = np.array(extra, float); v /= np.linalg.norm(v)
        dirs = np.vstack([dirs, v])

    # small-k speeds per direction (kR-independent; hoisted out of the sweep).
    # The propagating shell at fixed omega is direction-resolved:
    # k(khat) = omega / cP(khat);  omega := cP_iso * kR / R_PORT.
    kl_small = 1e-4
    cPs = np.array([
        longitudinal_eig(kh * kl_small, basis, bonds, rho_star, k_s)[0]
        for kh in dirs
    ])
    cP_iso = float(np.mean(cPs))

    out = {}
    for kR in KR_SWEEP:
        O00 = np.zeros(len(dirs), dtype=complex)
        O22 = np.zeros(len(dirs), dtype=complex)
        omega = cP_iso * (kR / R_PORT)
        for i, kh in enumerate(dirs):
            k_mag = omega / cPs[i]
            kvec = kh * k_mag
            _, eL, _ = longitudinal_eig(kvec, basis, bonds, rho_star, k_s)
            phase = np.exp(-1j * (xs @ kvec))
            proj = (nhat @ eL)                      # (e_L . nhat_s), complex
            O00[i] = np.sum(proj * p00 * phase)
            O22[i] = np.sum(proj * p22 * phase)
        I00 = float(np.mean(np.abs(O00) ** 2))
        I22 = float(np.mean(np.abs(O22) ** 2))
        w5 = (1.0 / cPs) ** 5
        I00w = float(np.mean(w5 * np.abs(O00) ** 2) / np.mean(w5))
        I22w = float(np.mean(w5 * np.abs(O22) ** 2) / np.mean(w5))
        x = kR
        j0p = spherical_jn(0, x, derivative=True)
        j2p = spherical_jn(2, x, derivative=True)
        rho_ref = float((j2p / j0p) ** 2)
        out[str(kR)] = {
            "omega": omega, "cP_iso": cP_iso,
            "I_00": I00, "I_22": I22,
            "rho_spec": I22 / (I00 + 1e-300),
            "rho_spec_fluxweighted": I22w / (I00w + 1e-300),
            "rho_ref_continuum": rho_ref,
            "ratio_to_ref": (I22 / (I00 + 1e-300)) / (rho_ref + 1e-300),
        }
    return {
        "n_shell_sites": int(n_shell),
        "n_directions": int(len(dirs)),
        "gram_cond_l012": gram_cond,
        "l2_moment_fidelity": l2_fidelity,
        "sweep": out,
    }


# ============================================================================
# ARM B — time-domain driven radiation (prereg SS7 Arm 2B)
# ============================================================================
def spectral_speeds(rho_star, k_s=1.0, n_random=24, seed=1):
    """C-2-style isotropic spectral speeds + the frozen direction-resolved
    G-SPEC gate (per-direction c_P/c_S vs the survey table, < 3%)."""
    basis, bonds = srs_primitive_bcc("right")
    rng = np.random.default_rng(seed)
    dirs = {"100": [1, 0, 0], "110": [1, 1, 0], "111": [1, 1, 1]}
    rand = rng.standard_normal((n_random, 3))
    rand /= np.linalg.norm(rand, axis=1, keepdims=True)
    for i in range(n_random):
        dirs[f"rand{i}"] = rand[i].tolist()
    kl = 1e-4
    per_dir, cP_list, cS_list = {}, [], []
    for name, dd in dirs.items():
        kh = np.array(dd, float); kh /= np.linalg.norm(kh)
        D = vector_bloch_D(kh * kl, basis, bonds, rho_star, k_s)
        w2, V = np.linalg.eigh(D)
        idx = np.argsort(w2)[:3]
        w2a, Va = w2[idx], V[:, idx]
        pol = Va.reshape(4, 3, 3).mean(axis=0)
        pol /= np.linalg.norm(pol, axis=0, keepdims=True) + 1e-30
        long_frac = np.abs(pol.T @ kh) ** 2
        c = np.sqrt(np.clip(w2a, 0, None)) / kl
        pL = int(np.argmax(long_frac))
        cP = float(c[pL]); cS = float(np.mean([c[j] for j in range(3) if j != pL]))
        per_dir[name] = {"cP": cP, "cS": cS, "cP_over_cS": cP / cS}
        cP_list.append(cP); cS_list.append(cS)
    gate = {}
    for n in ("100", "110", "111"):
        meas = per_dir[n]["cP_over_cS"]; ref = SURVEY_CP_CS[n]
        rel = abs(meas - ref) / ref
        gate[n] = {"measured": meas, "survey": ref, "rel_err": rel,
                   "pass_lt_3pct": bool(rel < 0.03)}
    return {
        "cP_iso": float(np.mean(cP_list)), "cS_iso": float(np.mean(cS_list)),
        "dir_resolved_gate": gate,
        "gate_all_pass": bool(all(g["pass_lt_3pct"] for g in gate.values())),
    }


def run_time_domain(L, rho_star, cP_spec, cS_spec, n_cycles_fwhm, k_s=1.0,
                    cfl=0.2, A_force=1e-4):
    """Three driven runs on one grid: (a) RADIAL-AC l=0, (b) COMMUTATION l=2
    m=+2 rotating, (c) STATIC l=2 ramp-hold control.  Radial FORCE drive on the
    port shell (body-force class, #761 SS1.2), equal time-averaged mean-square
    force across runs.  Longitudinal radiated energy at r_meas in the analytic
    spectral window (G-WINDOW: no front-detect)."""
    pos, bi, bj, dhat = build_finite_srs(L)
    N = pos.shape[0]
    Phi = bond_tensors(dhat, rho_star, k_s)
    center = np.array([L / 2.0] * 3)
    rel = pos - center
    r = np.linalg.norm(rel, axis=1)
    rhat = rel / (r[:, None] + 1e-30)

    port = (r >= R_PORT - SHELL_W / 2) & (r < R_PORT + SHELL_W / 2)
    meas = (r >= R_MEAS) & (r < R_MEAS + SHELL_W)
    n_port, n_meas = int(port.sum()), int(meas.sum())
    nhat_p = rhat[port]

    # normalized complex patterns on the port shell
    p00 = y00(nhat_p); p00 = p00 / np.linalg.norm(p00)
    p22 = y22(nhat_p); p22 = p22 / np.linalg.norm(p22)

    # measurement-shell l-projections (unit-L2 over the measurement shell)
    nhat_m = rhat[meas]
    q00 = y00(nhat_m); q00 = q00 / np.linalg.norm(q00)
    q22 = y22(nhat_m); q22 = q22 / np.linalg.norm(q22)

    # drive frequency from the frozen kR_TD label at the spectral cP
    k_d = KR_TD / R_PORT
    omega_d = cP_spec * k_d
    T_d = 2 * np.pi / omega_d
    Omega_rot = omega_d / 2.0            # pattern rotation rate (m=+2 => 2*Omega = omega_d)

    fwhm = n_cycles_fwhm * T_d
    sig_t = fwhm / (2.0 * np.sqrt(2.0 * np.log(2.0)))
    # place t0 as late as the reflection budget allows (turn-on truncation disclosed)
    d_face = L / 2.0
    t_reflect = (2.0 * d_face - R_PORT - R_MEAS) / (cP_spec + 1e-30)
    t_travel = (R_MEAS - R_PORT) / (cP_spec + 1e-30)
    t0 = max(t_reflect - t_travel - 2.0 * sig_t, 1.5 * sig_t)
    turn_on_sigma = t0 / sig_t           # how many sigma the ramp-up gets
    t_arr = t_travel                     # earliest signal at r_meas (drive from t~0)
    t_end = 1.02 * t_reflect
    window_budget_ok = bool((t0 + 2.0 * sig_t + t_travel) <= t_reflect)

    omega_max = omega_max_power_iter(Phi, bi, bj, N)
    dt = cfl * 2.0 / omega_max
    n_steps = int(np.ceil(t_end / dt)) + 2

    def envelope(t):
        return np.exp(-((t - t0) ** 2) / (2.0 * sig_t ** 2))

    # static control: EARLY, SHORT ramp (sigma = T_d/2, completed by ~3 sigma)
    # so its transient clears the measurement shell early; its floor is read
    # from the LATE HALF of the window (settled-DC residual AC content) —
    # the floor-window definition, declared in the result doc.
    sig_ramp = T_d / 2.0
    t0_ramp = 3.0 * sig_ramp

    def env_ramp_hold(t):
        return 1.0 if t >= t0_ramp else np.exp(-((t - t0_ramp) ** 2)
                                               / (2.0 * sig_ramp ** 2))

    # equal time-averaged mean-square force normalization (prereg SS7):
    #   (a) F = A*sqrt(2)*p00*cos(w_d t)*env      <F^2> = A^2 * <env^2>
    #   (b) F = A*sqrt(2)*Re[p22 e^{-i w_d t}]*env  <F^2> = A^2 * <env^2>
    #   (c) F = A*Re[p22]/||Re[p22]||*hold          F^2  = A^2 at hold
    p22_static = np.real(p22); p22_static = p22_static / np.linalg.norm(p22_static)

    runs = {}
    H_EVERY = 5          # H-ledger sampling stride (PE einsum is the cost driver)
    for tag in ("radial_ac", "commutation", "static_control"):
        u = np.zeros((N, 3)); v = np.zeros((N, 3))
        F_int = forces(u, Phi, bi, bj, N)
        rec = {"t": [], "H_t": [], "H": [], "s22": [], "s00": [],
               "drive_ms": [], "E_par_inst": []}
        # streaming per-site window accumulators (AC-content energy: the static
        # control's DC near-field deformation must NOT read as radiated energy;
        # E_AC = sum_t u^2 - n <u>^2 per site, i.e. window variance).
        # v2 (post-v1 instrument repair, DISCLOSED as a dated deviation in the
        # result doc): THREE window variants computed SIMULTANEOUSLY, no
        # post-hoc selection —
        #   'frozen_full' : [t_arr, t_reflect)             (prereg-literal)
        #   'late_half'   : [(t_arr+t_reflect)/2, t_reflect)   (v1 definition)
        #   's_cleared'   : [t_ramp_clear, t_reflect)      (analytic: the ramp
        #       transient's SLOW S-TAIL arrival cleared — t0_ramp + 2.5 sigma
        #       + (R_MEAS-R_PORT)/c_S; all inputs analytic spectral speeds,
        #       no tuning freedom).  Empty windows report None (L=48 case).
        t_s_clear = t0_ramp + 2.5 * sig_ramp + (R_MEAS - R_PORT) / (cS_spec + 1e-30)
        windows = {
            "frozen_full": (t_arr, t_reflect),
            "late_half": (0.5 * (t_arr + t_reflect), t_reflect),
            "s_cleared": (t_s_clear, t_reflect),
        }
        acc = {w: {"n": 0, "s1p": np.zeros(n_meas), "s2p": 0.0,
                   "s1t": np.zeros((n_meas, 3)), "s2t": 0.0}
               for w in windows}
        max_u = 0.0
        for step in range(n_steps):
            t = step * dt

            def ext_force(tt):
                Fe = np.zeros((N, 3))
                if tag == "radial_ac":
                    amp = A_force * np.sqrt(2.0) * p00 * np.cos(omega_d * tt) \
                        * envelope(tt)
                elif tag == "commutation":
                    amp = A_force * np.sqrt(2.0) \
                        * np.real(p22 * np.exp(-1j * omega_d * tt)) * envelope(tt)
                else:
                    amp = A_force * p22_static * env_ramp_hold(tt)
                Fe[port] = amp[:, None] * nhat_p
                return Fe

            Fe = ext_force(t)
            # measurement-shell records
            u_m = u[meas]
            u_par = np.sum(u_m * nhat_m, axis=1)
            u_perp = u_m - u_par[:, None] * nhat_m
            rec["t"].append(t)
            rec["s22"].append(complex(np.sum(u_par * np.conj(q22))))
            rec["s00"].append(float(np.sum(u_par * q00)))
            rec["drive_ms"].append(float(np.sum(Fe[port] ** 2)))
            rec["E_par_inst"].append(float(np.sum(u_par ** 2)))
            for wname, (lo, hi) in windows.items():
                if (t >= lo) and (t < hi):
                    a = acc[wname]
                    a["n"] += 1
                    a["s1p"] += u_par; a["s2p"] += float(np.sum(u_par ** 2))
                    a["s1t"] += u_perp; a["s2t"] += float(np.sum(u_perp ** 2))
            # H ledger (sampled; free H — drive work makes it grow during burst)
            if step % H_EVERY == 0:
                du = u[bi] - u[bj]
                PE = 0.5 * np.einsum("bi,bij,bj->b", du, Phi, du)
                rec["H_t"].append(t)
                rec["H"].append(float(0.5 * np.sum(v ** 2) + np.sum(PE)))
            # velocity-Verlet with external drive
            u = u + v * dt + 0.5 * (F_int + Fe) * dt ** 2
            max_u = max(max_u, float(np.abs(u).max()))
            Fe_new = ext_force(t + dt)
            F_new = forces(u, Phi, bi, bj, N)
            v = v + 0.5 * ((F_int + Fe) + (F_new + Fe_new)) * dt
            F_int = F_new

        tarr = np.array(rec["t"])
        win = (tarr >= t_arr) & (tarr < t_reflect)
        if acc["frozen_full"]["n"] < 10:
            raise RuntimeError(
                f"ARTIFACT-class config: empty/near-empty measurement window "
                f"(t_arr={t_arr:.1f}, t_reflect={t_reflect:.1f}) "
                f"— grid too small for r_meas; enlarge L (prereg SS11 fence 5)")

        def win_energies(a):
            n = a["n"]
            if n < 10:
                return None
            EP = float((a["s2p"] - np.sum(a["s1p"] ** 2) / n) * dt)
            ES = float((a["s2t"] - np.sum(a["s1t"] ** 2) / n) * dt)
            Tw = n * dt
            return {"E_P": EP, "E_S": ES, "T_win": Tw,
                    "E_P_rate": EP / Tw, "E_S_rate": ES / Tw}

        by_window = {w: win_energies(a) for w, a in acc.items()}
        # primary window per run class: bursts read the full window (their
        # signal spans it); the static floor's instrument-correct window is
        # s_cleared (falls back to late_half where s_cleared is empty — L=48)
        prim = by_window["frozen_full"] if tag != "static_control" else (
            by_window["s_cleared"] or by_window["late_half"])
        E_P, E_S, T_win = prim["E_P"], prim["E_S"], prim["T_win"]
        E_P_rate, E_S_rate = prim["E_P_rate"], prim["E_S_rate"]
        # G-FREQ spectrum: l=2-projected radial signal in the window (zero-padded)
        s22 = np.array(rec["s22"])[win]
        s00 = np.array(rec["s00"])[win]
        npad = 8 * len(s22)
        f22 = np.fft.fft(s22 - s22.mean(), n=npad)
        freqs = 2 * np.pi * np.fft.fftfreq(npad, d=dt)
        # the m=+2 rotating response is e^{-i w t}: its line sits at NEGATIVE
        # frequency of the complex projection — fold the two-sided spectrum
        # by |f| so the peak is read at |omega| regardless of rotation sense
        absf = np.abs(freqs)
        spec22 = np.abs(f22) ** 2
        sel = absf > 1e-12
        fpos, spec22 = absf[sel], spec22[sel]
        pk = int(np.argmax(spec22))
        omega_peak = float(fpos[pk])
        band = np.abs(fpos - omega_d) < 0.15 * omega_d
        band_frac = float(spec22[band].sum() / (spec22.sum() + 1e-300))
        # content at the rotation rate Omega vs the 2*Omega peak (folded)
        mOm = np.abs(fpos - Omega_rot) < (fpos[1] - fpos[0]) * 4
        ratio_Om = float(spec22[mOm].max() / (spec22[pk] + 1e-300)) if mOm.any() else 0.0
        # post-burst free-evolution drift (after drive quenched: t > t0 + 2.5 sig)
        Hf = np.array(rec["H"]); Ht = np.array(rec["H_t"]); tq = t0 + 2.5 * sig_t
        post = Ht > tq
        H_drift = float((Hf[post].max() - Hf[post].min())
                        / (abs(Hf[post][0]) + 1e-30)) if post.sum() > 3 else None
        runs[tag] = {
            "E_P_window": E_P, "E_S_window": E_S,
            "E_P_rate": E_P_rate, "E_S_rate": E_S_rate,
            "T_win": T_win,
            "by_window": by_window,
            "band_frac_at_omega_d": band_frac,
            "omega_peak_l2proj": omega_peak,
            "omega_peak_over_2Omega": omega_peak / (omega_d + 1e-300),
            "spec_ratio_at_Omega": ratio_Om,
            "H_drift_postburst": H_drift,
            "max_u": max_u,
            "drive_ms_timeavg": float(np.mean(rec["drive_ms"])),
            "s00_window_rms": float(np.sqrt(np.mean(s00 ** 2))),
        }

    E_static = runs["static_control"]["E_P_rate"]
    E_comm = runs["commutation"]["E_P_rate"]
    E_rad = runs["radial_ac"]["E_P_rate"]
    floor_variants = {}
    for w, v in runs["static_control"]["by_window"].items():
        floor_variants[w] = (None if v is None
                             else {"floor_rate": v["E_P_rate"],
                                   "R_comm_over_floor": E_comm / (v["E_P_rate"] + 1e-300),
                                   "R_radac_over_floor": E_rad / (v["E_P_rate"] + 1e-300)})
    x = KR_TD
    rho_ref = float((spherical_jn(2, x, derivative=True)
                     / spherical_jn(0, x, derivative=True)) ** 2)
    return {
        "grid": {"L": L, "N_sites": N, "n_bonds": int(bi.shape[0]),
                 "n_port_sites": n_port, "n_meas_sites": n_meas,
                 "dt": dt, "n_steps": n_steps, "omega_max": float(omega_max),
                 "A_force": A_force, "cfl": cfl},
        "drive": {"kR_port": KR_TD, "omega_d": omega_d, "T_d": T_d,
                  "Omega_rot": Omega_rot, "n_cycles_fwhm": n_cycles_fwhm,
                  "sigma_t": sig_t, "t0": t0, "turn_on_sigma": turn_on_sigma,
                  "t_arr": t_arr, "t_reflect": t_reflect,
                  "window_budget_ok": window_budget_ok,
                  "t0_ramp": t0_ramp, "sigma_ramp": sig_ramp,
                  "t_s_clear": (t0_ramp + 2.5 * sig_ramp
                                + (R_MEAS - R_PORT) / (cS_spec + 1e-30))},
        "runs": runs,
        "R_comm_over_static": E_comm / (E_static + 1e-300),
        "R_radac_over_static": E_rad / (E_static + 1e-300),
        "floor_variants": floor_variants,
        "R_comm_over_radac": (runs["commutation"]["E_P_window"]
                              / (runs["radial_ac"]["E_P_window"] + 1e-300)),
        "rho_ref_continuum_at_kR": rho_ref,
    }


# ============================================================================
# ARM C — eccentricity: Kepler-orbit moment averages (prereg SS7 Arm 2C)
# ============================================================================
def kepler_orbit(e, n_t=20000):
    """One full orbit, uniform in mean anomaly M in [0, 2pi); a = 1, Omega = 1,
    mu = 1 (all averages are dimensionless ratios)."""
    M = np.linspace(0.0, 2 * np.pi, n_t, endpoint=False)
    E = M.copy()
    for _ in range(60):
        E = E - (E - e * np.sin(E) - M) / (1.0 - e * np.cos(E))
    x = np.cos(E) - e
    y = np.sqrt(1 - e ** 2) * np.sin(E)
    return M, x, y


def arm_C_eccentricity():
    """<(d3 trM/dt3)^2> and <d3 M_TL/dt3 : d3 M_TL/dt3> over the orbit vs the
    frozen symbolic forms: trace/TL(e=0) -> 2 e^2/32 [1+O(e^2)];
    f_TL(e) = f_PM(e) to 1% (G-ECC)."""
    res = {}
    for e in ECC_SWEEP:
        M, x, y = kepler_orbit(e)
        dM = M[1] - M[0]     # time step (Omega_mean = 1)
        Mxx, Myy, Mxy = x * x, y * y, x * y
        tr = Mxx + Myy

        def d3(f):
            # spectral differentiation on the periodic orbit (exact for
            # band-limited Kepler series; no finite-difference noise)
            F = np.fft.fft(f)
            w = 2 * np.pi * np.fft.fftfreq(len(f), d=dM)
            return np.real(np.fft.ifft((1j * w) ** 3 * F))

        d3tr = d3(tr)
        TLxx = Mxx - tr / 3.0; TLyy = Myy - tr / 3.0; TLzz = -tr / 3.0
        d3TLxx, d3TLyy, d3TLzz, d3TLxy = d3(TLxx), d3(TLyy), d3(TLzz), d3(Mxy)
        tl2 = np.mean(d3TLxx ** 2 + d3TLyy ** 2 + d3TLzz ** 2 + 2 * d3TLxy ** 2)
        tr2 = np.mean(d3tr ** 2)
        res[str(e)] = {"mean_d3TL_sq": float(tl2), "mean_d3tr_sq": float(tr2)}
    tl0 = res["0.0"]["mean_d3TL_sq"]
    for e in ECC_SWEEP:
        r = res[str(e)]
        ee = float(e)
        r["f_TL"] = r["mean_d3TL_sq"] / tl0
        r["f_PM_formula"] = float((1 + 73 * ee ** 2 / 24 + 37 * ee ** 4 / 96)
                                  / (1 - ee ** 2) ** 3.5)
        r["trace_over_TL0"] = r["mean_d3tr_sq"] / tl0
        r["trace_leading_form"] = 2.0 * ee ** 2 / 32.0
        # flux-weighted trace-channel add-on (l=0 vs l=2 angular weights)
        r["flux_addon_5_96_e2"] = 5.0 * ee ** 2 / 96.0
    # sanity: circular-limit TL invariant = 32 (mu=a=Omega=1 units)
    res["circular_TL_invariant"] = tl0
    res["circular_TL_expected_32"] = 32.0
    return res


# ============================================================================
def main():
    t_start = time.time()
    rho_star = float(derive_rho_star()[0])   # (rho_star, nu_hill, moduli)
    spec = spectral_speeds(rho_star)
    cP, cS = spec["cP_iso"], spec["cS_iso"]

    print(f"[overlap] rho_star={rho_star:.5f}  cP={cP:.4f}  cS={cS:.4f}  "
          f"G-SPEC pass={spec['gate_all_pass']}")

    armA = arm_A_spectral(rho_star)
    print("[overlap] arm A done")
    for kR, d in armA["sweep"].items():
        print(f"   kR={kR}: rho_spec={d['rho_spec']:.4f}  "
              f"ref={d['rho_ref_continuum']:.4f}  ratio={d['ratio_to_ref']:.3f}")

    armB_oper = run_time_domain(L_OPER, rho_star, cP, cS, n_cycles_fwhm=3.0)
    print(f"[overlap] arm B operative (L={L_OPER}) done: "
          f"R_c/s={armB_oper['R_comm_over_static']:.3g} "
          f"R_c/a={armB_oper['R_comm_over_radac']:.4f}")
    armB_frozen = run_time_domain(L_FROZEN, rho_star, cP, cS, n_cycles_fwhm=2.0)
    print(f"[overlap] arm B frozen-grid diagnostic (L={L_FROZEN}) done")

    armC = arm_C_eccentricity()
    print("[overlap] arm C done")

    out = {
        "provenance": {
            "prereg": "research/2026-08-08_overlap-integral_prereg-FROZEN.md",
            "prereg_commit": "52e9c1cb",
            "rho_star_derived": rho_star,
            "frozen_grid_deviation_note": (
                "prereg froze L=48 for arm B; the window budget cannot contain "
                "a 3-cycle burst at L=48 (window_budget_ok in the L=48 block); "
                "operative grid enlarged to L=64 (conservative: larger box only "
                "delays reflections; #761 SS4.0-1 precedent), frozen grid kept "
                "as diagnostic with a 2-cycle burst, truncation disclosed."),
        },
        "spectral_speeds": spec,
        "arm_A_spectral_overlap": armA,
        "arm_B_time_domain_operative_L64": armB_oper,
        "arm_B_time_domain_frozen_L48": armB_frozen,
        "arm_C_eccentricity": armC,
        "runtime_metadata": {"wall_seconds": round(time.time() - t_start, 1)},
    }
    out_path = Path(__file__).with_name("overlap_integral_lattice_results.json")
    out_path.write_text(json.dumps(out, indent=1, default=str))
    print(f"[overlap] wrote {out_path}  ({out['runtime_metadata']['wall_seconds']}s)")


if __name__ == "__main__":
    main()
