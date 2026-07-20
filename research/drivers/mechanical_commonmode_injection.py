#!/usr/bin/env python3
"""LEG C — mechanical common-mode injection: does a point BREATHING (isotropic
dilatation) source radiate LONGITUDINAL far-field content on the ACTUAL srs lattice?

Prereg (FROZEN, criteria committed ALONE first):
    research/2026-07-20_mechanical-commonmode-derivation_prereg-FROZEN.md  §3
Companion result:
    research/2026-07-20_mechanical-commonmode-derivation_result.md         (Leg C)

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-FIRST SECTOR HEADER (fired before any standard-physics term)
═══════════════════════════════════════════════════════════════════════════════
  SECTOR : the TRANSLATIONAL (Cauchy-grade) VECTOR sector of the chiral srs-z3 net
           (ave.core.chiral_lattice._SRS_8A / _SRS_NN; I4₁32, Wyckoff-8a, z=3).
           Each bond carries the substrate-native RANK-2 bond tensor
           Φ_b = k_a·(d̂⊗d̂) + k_s·(I − d̂⊗d̂),  k_a = axial STRETCH (longitudinal),
           k_s = transverse SHEAR/bend.  NOT a Cartesian Laplacian.
  REGIME : COLD linear, sub-yield, saturation OFF (seed amplitude A = 1e-3 ≪ yield;
           no Op14 local-clock modulation; no Op3 impedance mismatch).  This is the
           Regime-I cold far field where the gravitational-radiation question lives.
  COORDS : real-space displacement-vector basis (A46-clean): the OBSERVABLE is the
           LONGITUDINAL (radial, ∇·u) vs TRANSVERSE (tangential, ∇×u) energy partition
           of the RADIATED field — the same displacement basis the vector survey uses,
           NOT a scalar-field φ² proxy the corpus never claimed.
  CLASS  : lattice-derived EMPIRICAL leg.  The band eigenstructure is a MANIFESTATION
           (theorem of the srs D(k)); every reported VALUE is dimensionless (energy
           fractions, speed ratios) or imported-by-symbol.  α-CLEAN (no α/Q_TANK).

ENGINE BYTE-UNTOUCHED: imports ave.core.chiral_lattice / ave.core.constants read-only;
the finite real-space net, the rank-2 bond dynamics, and the time-stepper are built
HERE (Rule-14 reuse of the survey bond model + the DERIVED ρ* from ν_Hill=2/7).

Run: PYTHONPATH=src:src/scripts/vol_1_foundations python3 \
        research/drivers/mechanical_commonmode_injection.py
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

TOL = 1e-9  # bond-length match tolerance (a_conv = 1 units)

# Frozen C-2 direction-resolved reference (prereg §3 GATE): the srs vector band
# survey's per-direction c_P/c_S (2026-07-09_srs-vector-band-survey_result.md:91-93).
# The frozen gate is |measured − survey|/survey < 3% per direction (direction-resolved),
# NOT the isotropic-mean band; both are reported (KEEP-BOTH), the direction-resolved
# one is the frozen criterion.  Review fix #761 R3(b).
SURVEY_CP_CS = {"100": 1.7105, "110": 1.8528, "111": 1.9041}


# ═════════════════════════════════════════════════════════════════════════════
# Finite real-space srs net (tile the 8-site conventional cell over L³ cells)
# ═════════════════════════════════════════════════════════════════════════════
def build_finite_srs(L: int):
    """Return (pos[N,3], bond_i[M], bond_j[M], dhat[M,3]) for an L³-cell srs net.

    Sites: _SRS_8A motif (8 Wyckoff-8a) replicated over the L³ cubic grid.
    Bonds: every unordered site pair at |Δ| = _SRS_NN (± TOL), found by cKDTree.
    """
    cells = np.array(
        [(cx, cy, cz) for cx in range(L) for cy in range(L) for cz in range(L)],
        dtype=float,
    )
    pos = (cells[:, None, :] + _SRS_8A[None, :, :]).reshape(-1, 3)  # (8L³, 3)
    tree = cKDTree(pos)
    pairs = tree.query_pairs(r=_SRS_NN + TOL, output_type="ndarray")
    d = pos[pairs[:, 1]] - pos[pairs[:, 0]]
    ln = np.linalg.norm(d, axis=1)
    keep = np.abs(ln - _SRS_NN) < TOL  # exact NN shell only
    pairs, d, ln = pairs[keep], d[keep], ln[keep]
    dhat = d / ln[:, None]
    return pos, pairs[:, 0].copy(), pairs[:, 1].copy(), dhat


def bond_tensors(dhat: np.ndarray, k_a: float, k_s: float) -> np.ndarray:
    """Per-bond rank-2 Φ_b = k_a d̂⊗d̂ + k_s (I − d̂⊗d̂).  Shape (M,3,3)."""
    P = np.einsum("bi,bj->bij", dhat, dhat)
    return k_a * P + k_s * (np.eye(3)[None] - P)


def forces(u, Phi, bi, bj, N):
    """F_s = −Σ_bonds Φ_b (u_s − u_t), vectorized (undirected bonds stored once)."""
    du = u[bi] - u[bj]                     # (M,3)
    fb = np.einsum("bij,bj->bi", Phi, du)  # (M,3)
    F = np.zeros((N, 3))
    np.add.at(F, bi, -fb)
    np.add.at(F, bj, +fb)
    return F


# ═════════════════════════════════════════════════════════════════════════════
# C-1 — TIME-DOMAIN breathing-source injection (radiation at range, windowed)
# ═════════════════════════════════════════════════════════════════════════════
def run_c1(L=20, r_meas_cells=6.0, A=1e-3, cfl=0.2, rho_star=9.773,
           k_s=1.0, sigma_cells=1.2, shell_width_cells=1.0,
           cP_spec=0.5196, cS_spec=0.2854):
    """Time-domain breathing-source radiation at range, SPECTRAL-windowed.

    REVIEW FIX #761 R2 (2026-07-20): the Poincaré window is built from the C-2
    SPECTRAL acoustic speeds (cP_spec, cS_spec — pass the run's own C-2 isotropic
    values), NOT from a 5%-of-peak energy crossing.  The prior 5%-of-peak "front
    detector" fires on the Gaussian seed's near-field precursor RAMP and reports
    cP≈0.95 cells/time — ~1.8× the max acoustic speed (spectral cP≈0.52), which is
    unphysical: nothing on an acoustic branch outruns the k→0 sound speed.  That
    detector is retained ONLY as a reported diagnostic (cP_precursor_diag), never
    for the window.  The physical window uses the frozen §3 analytic definitions
    t_arrival ≈ r_meas/c_P, t_reflect ≈ (2·L_edge − r_meas)/c_P at the spectral cP;
    the lattice-converted S front at r_meas/c_S.  Defaults (0.5196/0.2854) are the
    C-2 isotropic values; main() passes the live C-2 run's speeds."""
    pos, bi, bj, dhat = build_finite_srs(L)
    N = pos.shape[0]
    Phi = bond_tensors(dhat, rho_star, k_s)
    center = np.array([L / 2.0] * 3)

    # ── breathing seed: u = ∇φ, φ = exp(−r²/2σ²)  ⇒  PURE dilatation (∇×u ≡ 0) ──
    rel = pos - center
    r = np.linalg.norm(rel, axis=1)
    sigma = sigma_cells
    phi = np.exp(-r**2 / (2.0 * sigma**2))
    u0 = -(rel / sigma**2) * phi[:, None]           # gradient of a Gaussian (curl-free)
    u0 *= A / (np.abs(u0).max() + 1e-30)            # normalize peak to A
    v0 = np.zeros_like(u0)
    seed_curl_check = _curl_energy_fraction(pos, u0, center)  # ~0 confirms pure long.

    # ── CFL dt from the finite lattice's max force eigen-rate (power iteration) ──
    omega_max = _omega_max(Phi, bi, bj, N)
    dt = cfl * 2.0 / omega_max                       # Verlet stability: dt < 2/ω_max

    # measurement shell: sites in [r_meas, r_meas+shell] cells from center
    r_meas = r_meas_cells
    shell = (r >= r_meas) & (r < r_meas + shell_width_cells)
    n_shell = int(shell.sum())
    rhat = rel / (r[:, None] + 1e-30)

    # integrate ~1.6× past the earliest boundary reflection (spectral t_reflect) so
    # the reflection-free window is fully covered AND the post-window fall is shown
    d_face = L / 2.0                                  # center→nearest-face (cells)
    t_reflect_pre = (2.0 * d_face - r_meas) / (cP_spec + 1e-30)
    n_steps = int(np.ceil(1.6 * t_reflect_pre / dt)) + 5
    u, v = u0.copy(), v0.copy()
    F = forces(u, Phi, bi, bj, N)
    inv_m = 1.0
    times, f_long_t, E_shell_t, H_t = [], [], [], []
    for step in range(n_steps):
        t = step * dt
        u_sh, rh = u[shell], rhat[shell]
        u_par = np.sum(u_sh * rh, axis=1)[:, None] * rh
        u_perp = u_sh - u_par
        E_par = float(np.sum(u_par**2))
        E_perp = float(np.sum(u_perp**2))
        E_tot = E_par + E_perp
        times.append(t)
        f_long_t.append(E_par / (E_tot + 1e-30))
        E_shell_t.append(E_tot)
        # total energy (Verlet H) for the conservation sanity
        du = u[bi] - u[bj]
        PEbond = 0.5 * np.einsum("bi,bij,bj->b", du, Phi, du)
        H_t.append(float(0.5 * np.sum(v**2) + np.sum(PEbond)))
        u = u + v * dt + 0.5 * F * inv_m * dt**2
        F_new = forces(u, Phi, bi, bj, N)
        v = v + 0.5 * (F + F_new) * inv_m * dt
        F = F_new

    times = np.array(times); f_long_t = np.array(f_long_t)
    E_shell_t = np.array(E_shell_t); H_t = np.array(H_t)

    # ── SPECTRAL Poincaré window (REVIEW FIX #761 R2) ───────────────────────────
    #   Window = frozen §3 analytic definitions at the C-2 SPECTRAL speeds.
    #   The old 5%-of-peak crossing is kept ONLY as a reported artifact diagnostic
    #   (cP_precursor_diag ≈ 0.95 cells/time — ~1.8× the physical acoustic speed;
    #   it fires on the near-field precursor ramp, NOT a wave front).
    peakE = float(E_shell_t.max())
    cross = np.where(E_shell_t > 0.05 * peakE)[0]
    front_idx = int(cross[0]) if cross.size else int(np.argmax(E_shell_t))
    cP_precursor_diag = r_meas / (float(times[front_idx]) + 1e-30)  # DIAGNOSTIC ONLY

    t_P_arr = r_meas / (cP_spec + 1e-30)             # spectral P arrival
    t_S_arr = r_meas / (cS_spec + 1e-30)             # spectral (lattice-converted) S
    t_reflect = (2.0 * d_face - r_meas) / (cP_spec + 1e-30)  # frozen §3 reflect @ cP
    reflectionfree_captures_S = bool(t_S_arr < t_reflect)

    win = (times >= t_P_arr) & (times < t_reflect)
    if win.sum() < 3:
        win = (times >= t_P_arr) & (times < 0.9 * times[-1])
    w = E_shell_t[win]
    f_long_window = float(np.sum(f_long_t[win] * w) / (np.sum(w) + 1e-30))
    f_long_peak = float(f_long_t[win][np.argmax(w)]) if win.sum() else float("nan")
    # robustness: energy-weighted f_long over the FULL trace (window-independent),
    # and f_long at the shell-energy peak (both show the ~0.99 result is not a
    # window-placement artifact)
    f_long_trace_full = float(np.sum(f_long_t * E_shell_t) / (np.sum(E_shell_t) + 1e-30))
    ipk = int(np.argmax(E_shell_t))
    f_long_at_Epeak = float(f_long_t[ipk])
    t_Epeak = float(times[ipk])
    H_drift = float((H_t.max() - H_t.min()) / (abs(H_t[0]) + 1e-30))

    return {
        "grid": {"L": L, "N_sites": N, "n_bonds": int(bi.shape[0]),
                 "r_meas_cells": r_meas, "shell_width_cells": shell_width_cells,
                 "n_shell_sites": n_shell, "A_seed": A, "sigma_cells": sigma_cells,
                 "cfl": cfl, "dt": dt, "n_steps": n_steps, "rho_star": rho_star},
        "seed_curl_energy_fraction": seed_curl_check,
        "omega_max": float(omega_max),
        "energy_drift_H": H_drift,
        "cP_spec_used": float(cP_spec),
        "cS_spec_used": float(cS_spec),
        "cP_precursor_diag_cells_per_time": float(cP_precursor_diag),
        "cP_precursor_diag_note": "ARTIFACT DIAGNOSTIC ONLY (not used for the window): "
                                  "the 5%-of-peak crossing fires on the Gaussian seed's "
                                  "near-field precursor ramp; ~1.8× the spectral acoustic "
                                  "cP — no signal outruns the k→0 sound speed.",
        "poincare_window": {"t_P_arrival_spectral": float(t_P_arr),
                            "t_reflect_spectral": float(t_reflect),
                            "t_S_arrival_spectral": float(t_S_arr),
                            "reflectionfree_window_captures_S_front": reflectionfree_captures_S,
                            "n_window_samples": int(win.sum()),
                            "definition": "frozen §3: t_arr=r_meas/cP, "
                                          "t_reflect=(2·L/2−r_meas)/cP, t_S=r_meas/cS, "
                                          "all at the C-2 spectral speeds"},
        "f_long_window": f_long_window,
        "f_long_peakE": f_long_peak,
        "f_long_trace_full": f_long_trace_full,
        "f_long_at_Epeak": f_long_at_Epeak,
        "t_Epeak": t_Epeak,
        "trace": {"t": times.tolist(), "f_long": f_long_t.tolist(),
                  "E_shell": E_shell_t.tolist()},
    }


def _curl_energy_fraction(pos, u, center):
    """Coarse finite-difference check that the seed is curl-free (∇×u≈0).
    Returns the transverse (tangential) energy fraction of the seed field itself
    at a mid shell — a pure gradient seed has ~0 tangential content only in the
    RADIAL-projection sense; here we report the tangential/total of the seed at a
    shell to confirm the injected field is longitudinal by construction."""
    rel = pos - center
    r = np.linalg.norm(rel, axis=1)
    sel = (r > 0.5) & (r < 4.0)
    rh = rel[sel] / (r[sel][:, None] + 1e-30)
    us = u[sel]
    u_par = np.sum(us * rh, axis=1)[:, None] * rh
    u_perp = us - u_par
    Epar = float(np.sum(u_par**2))
    Eperp = float(np.sum(u_perp**2))
    return Eperp / (Epar + Eperp + 1e-30)


def _omega_max(Phi, bi, bj, N, iters=60):
    """Largest force-operator eigen-rate ω_max = √λ_max via power iteration on the
    dynamical operator D u = −F(u)/m (m=1). Sets the Verlet CFL dt."""
    rng = np.random.default_rng(0)
    x = rng.standard_normal((N, 3))
    x /= np.linalg.norm(x)
    lam = 0.0
    for _ in range(iters):
        Dx = -forces(x, Phi, bi, bj, N)  # = D x  (D = −F, positive semidefinite)
        lam = float(np.linalg.norm(Dx))
        x = Dx / (lam + 1e-30)
    return np.sqrt(max(lam, 1e-12))


# ═════════════════════════════════════════════════════════════════════════════
# C-2 — SPECTRAL far-field partition (finite-size-free; the robust anchor)
# ═════════════════════════════════════════════════════════════════════════════
def run_c2(rho_star=9.773, k_s=1.0, n_random=24, seed=1):
    """From the ACTUAL lattice D(k), long-wave (k→0): acoustic eigenvectors →
    identify the LONGITUDINAL branch (max |ê·k̂|²), speeds c_P/c_S, and the far-field
    radiated-power partition of (a) a breathing dilatation source and (b) a rotating
    mass quadrupole, from |ê_b·Ŝ|² weighted by the 1/c_b⁵ flux scaling."""
    basis, bonds = srs_primitive_bcc("right")
    rng = np.random.default_rng(seed)
    dirs = {"100": [1, 0, 0], "110": [1, 1, 0], "111": [1, 1, 1]}
    rand = rng.standard_normal((n_random, 3))
    rand /= np.linalg.norm(rand, axis=1, keepdims=True)
    for i in range(n_random):
        dirs[f"rand{i}"] = rand[i].tolist()

    kl = 1e-4
    per_dir = {}
    cP_list, cS_list, long_fits = [], [], []
    for name, dd in dirs.items():
        kh = np.array(dd, float)
        kh = kh / np.linalg.norm(kh)
        D = vector_bloch_D(kh * kl, basis, bonds, rho_star, k_s)
        w2, V = np.linalg.eigh(D)
        idx = np.argsort(w2)[:3]                       # 3 acoustic branches
        w2a, Va = w2[idx], V[:, idx]
        # each acoustic eigvec is 12-dim (4 sites × 3); the LONG-WAVE acoustic
        # polarization is the site-uniform part → average the 4 site-blocks
        pol = Va.reshape(4, 3, 3).mean(axis=0)         # (3 comp, 3 branch)
        pol /= np.linalg.norm(pol, axis=0, keepdims=True) + 1e-30
        long_frac = np.abs(pol.T @ kh) ** 2            # |ê_b·k̂|² per branch
        c = np.sqrt(np.clip(w2a, 0, None)) / kl
        pL = int(np.argmax(long_frac))                 # longitudinal = max |ê·k̂|²
        cP = float(c[pL])
        cS = float(np.mean([c[j] for j in range(3) if j != pL]))
        per_dir[name] = {"cP": cP, "cS": cS, "cP_over_cS": cP / cS,
                         "long_frac_of_P_branch": float(long_frac[pL]),
                         "long_frac_all": long_frac.tolist()}
        if name in ("100", "110", "111"):
            cP_list.append(cP); cS_list.append(cS); long_fits.append(float(long_frac[pL]))

    # ── source-projection far-field partition (isotropic average) ──────────────
    # (a) breathing dilatation source: couples ∝ longitudinal polarization ⇒ the
    #     radiated long fraction = ⟨|ê_L·k̂|²⟩ over the sphere (≈1 if a P-branch exists)
    long_fracs = np.array([per_dir[n]["long_frac_of_P_branch"] for n in per_dir])
    breathing_long_fraction = float(np.mean(long_fracs))
    # (b) rotating mass quadrupole → P vs S partition = A_ang·(c_S/c_P)^5 (continuum
    #     reference; A_ang=2/3 is the isotropic P/S angular integral, q1 §1.2)
    cP_iso = float(np.mean(cP_list))
    cS_iso = float(np.mean(cS_list))
    A_ang = 2.0 / 3.0
    quad_partition = A_ang * (cS_iso / cP_iso) ** 5

    # ── frozen direction-resolved gate (prereg §3): per-dir |meas−survey|/survey<3% ─
    dir_resolved = {}
    for n in ("100", "110", "111"):
        meas = per_dir[n]["cP_over_cS"]
        ref = SURVEY_CP_CS[n]
        rel = abs(meas - ref) / ref
        dir_resolved[n] = {"measured": meas, "survey": ref, "rel_err": rel,
                           "pass_lt_3pct": bool(rel < 0.03)}
    dir_resolved_all_pass = bool(all(d["pass_lt_3pct"] for d in dir_resolved.values()))

    return {
        "per_direction": per_dir,
        "cP_iso": cP_iso,
        "cS_iso": cS_iso,
        "cP_over_cS_isotropic": cP_iso / cS_iso,
        "cP_over_cS_100_110_111": [per_dir[n]["cP_over_cS"] for n in ("100", "110", "111")],
        "direction_resolved_gate_vs_survey": dir_resolved,
        "direction_resolved_gate_all_pass": dir_resolved_all_pass,
        "breathing_source_long_fraction": breathing_long_fraction,
        "rotating_quadrupole_P_over_S_partition": {
            "A_ang": A_ang, "cS_over_cP": cS_iso / cP_iso,
            "F_bulk_over_F_shear": quad_partition,
            "note": "CONTINUUM-IMPORT color-check, NOT an independent lattice partition. "
                    "This is the continuum multipole formula A_ang·(c_S/c_P)^5 (A_ang=2/3 "
                    "the isotropic P/S angular integral, 1/c^5 the flux scaling — both "
                    "continuum imports, q1 §1.2) RE-EVALUATED at the lattice-measured "
                    "c_P/c_S.  The only lattice input is the speed ratio; it adds no "
                    "evidential weight beyond the C-2 c_P/c_S agreement (co-monotone).  "
                    "The prereg's C-2(b) |ê_b·Ŝ|² quadrupole eigenvector projection is "
                    "NOT implemented here (only the (a) breathing projection is) — routed "
                    "as an owed follow-on (#761 R4).",
        },
    }


# ═════════════════════════════════════════════════════════════════════════════
def _classify(fl):
    if fl > 0.5:
        return "PORT-OPEN (longitudinal radiation PRESENT) → NONE-DERIVES leans"
    if fl < 0.1:
        return "MODE-ABSENCE (longitudinal absent/evanescent) → PORT-CLOSED leans"
    return "INCONCLUSIVE on C-1 (0.1 ≤ f_long ≤ 0.5) → defer to C-2 + analytic"


def _verdict(c1, c2, c1_L16=None):
    fl = c1["f_long_window"]
    v = {
        "C1_f_long_window_L20": fl,
        "C1_verdict_L20": _classify(fl),
        "C1_f_long_trace_full_L20": c1["f_long_trace_full"],
        "C2_breathing_long_fraction": c2["breathing_source_long_fraction"],
        "C2_cP_over_cS_isotropic": c2["cP_over_cS_isotropic"],
        # ── frozen direction-resolved gate (prereg §3) — the OPERATIVE criterion ──
        "C2_gate_direction_resolved_lt_3pct": c2["direction_resolved_gate_all_pass"],
        # ── isotropic-mean band: a WEAKER PROXY of the frozen gate (KEEP-BOTH) ────
        "C2_gate_isotropic_band_proxy_1p60_1p95": bool(
            1.60 <= c2["cP_over_cS_isotropic"] <= 1.95),
    }
    if c1_L16 is not None:
        v["C1_f_long_window_L16_frozen_grid"] = c1_L16["f_long_window"]
        v["C1_verdict_L16_frozen_grid"] = _classify(c1_L16["f_long_window"])
        v["C1_f_long_trace_full_L16_frozen_grid"] = c1_L16["f_long_trace_full"]
    return v


def main():
    print("=" * 80)
    print("LEG C — mechanical common-mode injection (breathing source on the srs net)")
    print("=" * 80)
    rho_star, nu_at, _ = derive_rho_star()
    print(f"\nρ* (DERIVED from ν_Hill=2/7, imported) = {rho_star:.5f} (ν_Hill={nu_at:.6f})")

    print("\n── C-2 spectral far-field partition (finite-size-free anchor) ──")
    c2 = run_c2(rho_star=rho_star)
    print(f"  c_P/c_S isotropic (lattice-measured) = {c2['cP_over_cS_isotropic']:.4f} "
          f"(spectral cP_iso={c2['cP_iso']:.4f}, cS_iso={c2['cS_iso']:.4f}; "
          f"per-dir {['%.3f' % x for x in c2['cP_over_cS_100_110_111']]})")
    print(f"  C-2 direction-resolved gate (per-dir |meas−survey|/survey<3%) = "
          f"{c2['direction_resolved_gate_all_pass']}  [FROZEN §3 criterion]")
    print(f"  C-2 isotropic-band proxy gate (1.60–1.95 on the mean) = "
          f"{bool(1.60 <= c2['cP_over_cS_isotropic'] <= 1.95)}  [weaker proxy, KEEP-BOTH]")
    print(f"  breathing-source LONGITUDINAL fraction = {c2['breathing_source_long_fraction']:.4f} "
          f"(→1 if a longitudinal Bloch branch exists)")
    print(f"  rotating-quadrupole F_bulk/F_shear = "
          f"{c2['rotating_quadrupole_P_over_S_partition']['F_bulk_over_F_shear']:.4f} "
          f"[CONTINUUM-IMPORT color-check, not an independent lattice partition]")

    print("\n── C-1 time-domain radiation at range (SPECTRAL-windowed; both grids) ──")
    c1 = run_c1(L=20, r_meas_cells=6.0, A=1e-3, cfl=0.2, rho_star=rho_star,
                cP_spec=c2["cP_iso"], cS_spec=c2["cS_iso"])
    c1_L16 = run_c1(L=16, r_meas_cells=6.0, A=1e-3, cfl=0.2, rho_star=rho_star,
                    cP_spec=c2["cP_iso"], cS_spec=c2["cS_iso"])
    for tag, cc in (("L=20 (shipped/operative)", c1), ("L=16 (FROZEN prereg §3)", c1_L16)):
        g = cc["grid"]
        pw = cc["poincare_window"]
        print(f"  [{tag}] net N={g['N_sites']}, {g['n_bonds']} bonds, dt={g['dt']:.4g}, "
              f"n_steps={g['n_steps']}; drift |ΔH/H|={cc['energy_drift_H']:.2e}")
        print(f"      spectral window [t_P={pw['t_P_arrival_spectral']:.3g}, "
              f"t_reflect={pw['t_reflect_spectral']:.3g}); t_S={pw['t_S_arrival_spectral']:.3g}, "
              f"captures-S={pw['reflectionfree_window_captures_S_front']}, "
              f"samples={pw['n_window_samples']}")
        print(f"      precursor-ramp DIAGNOSTIC cP={cc['cP_precursor_diag_cells_per_time']:.3g} "
              f"(ARTIFACT; ~1.8× spectral cP — not used for the window)")
        print(f"      ★ f_long window={cc['f_long_window']:.4f} | at E-peak(t="
              f"{cc['t_Epeak']:.3g})={cc['f_long_at_Epeak']:.4f} | full-trace="
              f"{cc['f_long_trace_full']:.4f}")

    verdict = _verdict(c1, c2, c1_L16=c1_L16)
    print("\n── FROZEN-TOLERANCE VERDICT ──")
    print(f"  C-1 f_long L=20 = {verdict['C1_f_long_window_L20']:.3f}  ⇒  "
          f"{verdict['C1_verdict_L20']}")
    print(f"  C-1 f_long L=16 (frozen grid) = "
          f"{verdict['C1_f_long_window_L16_frozen_grid']:.3f}  ⇒  "
          f"{verdict['C1_verdict_L16_frozen_grid']}")
    print(f"  C-2 breathing long-fraction = {verdict['C2_breathing_long_fraction']:.3f}")
    print(f"  C-2 direction-resolved gate (<3%, FROZEN) = "
          f"{verdict['C2_gate_direction_resolved_lt_3pct']}")
    print(f"  C-2 isotropic-band proxy gate = "
          f"{verdict['C2_gate_isotropic_band_proxy_1p60_1p95']}")

    out = {"class": "LEG-C lattice-derived empirical injection",
           "rho_star": {"value": float(rho_star), "nu_Hill": float(nu_at)},
           "C1_time_domain": c1, "C1_time_domain_L16_frozen": c1_L16,
           "C2_spectral": c2, "verdict": verdict}
    out_path = Path(__file__).resolve().parent / \
        "mechanical_commonmode_injection_results.json"
    # trim the long trace arrays for the on-disk JSON (keep a decimated copy)
    for key in ("C1_time_domain", "C1_time_domain_L16_frozen"):
        tr = out[key]["trace"]
        dec = max(1, len(tr["t"]) // 200)
        out[key]["trace"] = {k: v[::dec] for k, v in tr.items()}
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nResults: {out_path}")
    try:
        _figure(c1, c2, out_path.parent)
    except Exception as e:  # pragma: no cover
        print(f"[figure skipped: {e}]")
    return out


def _figure(c1, c2, out_dir):
    from ave.viz import style
    style.apply()
    tr = c1["trace"]
    t = np.array(tr["t"]); fl = np.array(tr["f_long"]); E = np.array(tr["E_shell"])
    fig, (ax1, ax2) = style.plt.subplots(1, 2, figsize=style.figsize("double"))
    ax1.plot(t, E / (E.max() + 1e-30), color=style.COLORS["ave"], lw=1.2)
    pw = c1["poincare_window"]
    tP, tR, tS = (pw["t_P_arrival_spectral"], pw["t_reflect_spectral"],
                  pw["t_S_arrival_spectral"])
    ax1.axvline(tP, color=style.COLORS["data"], ls="--", lw=0.9)
    ax1.axvline(tR, color=style.COLORS["comparison"], ls="--", lw=0.9)
    if tS < 1.6 * tR:
        ax1.axvline(tS, color=style.COLORS["muted"], ls=":", lw=0.8)
        ax1.annotate("S-front", (tS, 0.9), fontsize=7, rotation=90, va="top")
    ax1.set_xlim(0, min(t.max(), 1.6 * tR))
    ax1.set_xlabel("time (lattice units)")
    ax1.set_ylabel("shell energy (normalized)")
    ax1.annotate("P-arrival (spectral)", (tP, 0.9), fontsize=7, rotation=90, va="top")
    ax1.annotate("reflect (spectral)", (tR, 0.9), fontsize=7, rotation=90, va="top")
    ax2.plot(t, fl, color=style.COLORS["ave"], lw=1.2)
    ax2.axhline(0.5, color=style.COLORS["muted"], ls=":", lw=0.8)
    ax2.axhline(c1["f_long_window"], color=style.COLORS["comparison"], ls="-.", lw=1.0)
    ax2.set_ylim(0, 1.05)
    ax2.set_xlim(0, min(t.max(), 1.6 * tR))
    ax2.axvspan(tP, tR, color=style.COLORS["ave"], alpha=0.08)
    ax2.set_xlabel("time (lattice units)")
    ax2.set_ylabel(r"$f_{long}=E_\parallel/(E_\parallel+E_\perp)$ at shell")
    ax2.annotate(f"window mean = {c1['f_long_window']:.2f}",
                 (t[len(t) // 2], c1["f_long_window"]), fontsize=7, va="bottom")
    paths = style.save(fig, out_dir / "mechanical_commonmode_injection")
    print(f"Figure: {paths}")


if __name__ == "__main__":
    main()
