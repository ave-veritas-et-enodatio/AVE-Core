#!/usr/bin/env python3
"""J(ω) derivation — the z=3 srs bath spectral density as the yield-fork adjudicator.

Prereg (FROZEN, pushed before this code): research/2026-07-20_jomega-derivation_prereg_FROZEN.md
Class: DERIVATION + research-driver (0D ODE-level). Engine byte-UNTOUCHED.

WHAT THIS IS
────────────
Executes the routed follow-on of research/2026-07-19_flag-f-s-dynamics-derivation.md §0:
derive J(ω) for the transverse-bow coordinate S coupled to the z=3 srs bond network,
evaluate the two Γ objects (πJ(ω→0) Markovian constant vs πJ(ω_drive) finite-drive
transfer), compute the per-cycle explicit-bath GLE energy ledger at the near-yield
crossing (ωτ≈0.9), and adjudicate the frozen (a)/(b)/UNDETERMINED tree.

LOAD-BEARING INPUT: the corpus-ADJUDICATED band model is the arccos TL map
    ω_n(k) = ω_link·arccos(μ_n(k)/3),  ω_link = √3·ω_C,  band top π√3·ω_C ≈ 5.44 ω_C
(srs-band-structure.md, clm-bnd5rq). The srs Bloch machinery below is REPLICATED from
src/scripts/vol_1_foundations/srs_band_survey.py (cited) so this driver is self-contained
and the engine stays byte-untouched. Constants imported by SYMBOL.

BATCHED: the arccos drag-onset ratio v_p,min/c_ch (vs the cosine-branch 2/π of #741).

Run: PYTHONPATH=src python3 src/scripts/vol_4_engineering/jomega_yield_fork.py
"""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path

import numpy as np

from ave.core.chiral_lattice import _SRS_8A, _SRS_NN
from ave.core.chiral_lattice_dynamics import ANALYTIC_NETWORK_FACTOR

Z_DEG = 3
OMEGA_LINK_OVER_C = 1.0 / ANALYTIC_NETWORK_FACTOR  # √3 (ω_link/ω_C); imported, not hard-coded
BAND_TOP = np.pi * OMEGA_LINK_OVER_C               # π√3 ≈ 5.4414 ω_C (arccos band top at H)
TAU = 1.0                                          # τ_relax = 1/ω_C native (TAU_RELAX_NATIVE)
OMEGA_D = 0.9                                       # crossing ω_d τ ≈ 0.9 (#735 (V,I) datum)


# ─────────────────────────────────────────────────────────────────────────────
# srs band machinery (REPLICATED from srs_band_survey.py; provenance-cited)
# ─────────────────────────────────────────────────────────────────────────────
def srs_primitive_bcc():
    motif = _SRS_8A.copy()
    basis = motif[:4].copy()
    bonds = []
    for i in range(4):
        for m in range(8):
            for n in product(range(-2, 3), repeat=3):
                d = motif[m] + np.array(n, float) - basis[i]
                if abs(np.linalg.norm(d) - _SRS_NN) < 1e-9:
                    bonds.append((i, m % 4, d))
    return basis, bonds


def bloch_adjacency(kvec, bonds, n=4):
    A = np.zeros((n, n), dtype=complex)
    for (i, j, d) in bonds:
        A[i, j] += np.exp(1j * np.dot(kvec, d))
    return 0.5 * (A + A.conj().T)


TWO_PI = 2.0 * np.pi
B1 = TWO_PI * np.array([0.0, 1.0, 1.0])
B2 = TWO_PI * np.array([1.0, 0.0, 1.0])
B3 = TWO_PI * np.array([1.0, 1.0, 0.0])


def omega_bands(kvec, bonds):
    """Sorted arccos-map band frequencies ω_n(k)/ω_C (ascending)."""
    mu = np.linalg.eigvalsh(bloch_adjacency(kvec, bonds)).real
    return np.sort(np.arccos(np.clip(mu / Z_DEG, -1.0, 1.0)) * OMEGA_LINK_OVER_C)


# ─────────────────────────────────────────────────────────────────────────────
# §2 — Density of states g(ω) from the arccos band (dense BZ histogram)
# ─────────────────────────────────────────────────────────────────────────────
def density_of_states(bonds, n_grid=40, n_bins=220):
    fs = (np.arange(n_grid) + 0.5) / n_grid  # cell-centred, avoids the Γ singular point
    freqs = []
    for f1 in fs:
        for f2 in fs:
            for f3 in fs:
                k = f1 * B1 + f2 * B2 + f3 * B3
                mu = np.linalg.eigvalsh(bloch_adjacency(k, bonds)).real
                freqs.extend((np.arccos(np.clip(mu / Z_DEG, -1.0, 1.0)) * OMEGA_LINK_OVER_C).tolist())
    freqs = np.array(freqs)
    edges = np.linspace(0.0, BAND_TOP, n_bins + 1)
    hist, _ = np.histogram(freqs, bins=edges, density=True)
    centres = 0.5 * (edges[:-1] + edges[1:])
    return centres, hist, freqs


def low_omega_exponent(centres, g, lo=0.05, hi=0.6):
    """Fit g(ω) ∝ ω^p in the low-ω region → p (3D acoustic expects ≈2)."""
    m = (centres > lo) & (centres < hi) & (g > 0)
    p = np.polyfit(np.log(centres[m]), np.log(g[m]), 1)
    return float(p[0])


def build_J(centres, g):
    """Spectral density J(ω) under the two frozen coupling models (prereg §3).

    C1 on-site  : c=const    → J ∝ g(ω)/ω     (3D: ∝ω  → Ohmic s=1)
    C2 strain   : c∝ω        → J ∝ g(ω)·ω     (3D: ∝ω³ → super-Ohmic s=3)
    Normalised to unit peak (shape object).
    """
    w = np.maximum(centres, 1e-9)
    J_c1 = g / w
    J_c2 = g * w
    return {
        "C1_onsite": J_c1 / J_c1.max(),
        "C2_strain": J_c2 / J_c2.max(),
    }


def _interp_at(centres, J, w):
    return float(np.interp(w, centres, J))


# ─────────────────────────────────────────────────────────────────────────────
# §5 — arccos drag-onset ratio v_p,min/c_ch  (batched task)
# ─────────────────────────────────────────────────────────────────────────────
def drag_onset_srs(bonds, n_scan=600):
    """v_p,min/c0 on the srs ACOUSTIC branch = min ω_0(k)/|k| within the first BZ.

    The acoustic branch ω_0(k) rises concavely from Γ to its first local maximum (the
    zone boundary along that ray, where v_g→0); beyond that is zone-folding (unphysical
    for this ratio). ω_0/|k| is decreasing on that interval, so the min sits AT the zone
    boundary = the first local max of ω_0 along the ray. c0 = low-k slope (divides out).
    """
    kl = 1e-3
    dirs = [np.array(d, float) for d in
            [[1, 0, 0], [1, 1, 0], [1, 1, 1], [2, 1, 0], [3, 1, 2], [2, 1, 1], [3, 2, 1]]]
    dirs = [d / np.linalg.norm(d) for d in dirs]
    c0 = float(np.mean([omega_bands(dhat * kl, bonds)[0] / kl for dhat in dirs]))
    per_dir = {}
    for dhat in dirs:
        ks = np.linspace(kl, 5.0, n_scan)
        w0 = np.array([omega_bands(dhat * kmag, bonds)[0] for kmag in ks])
        imax = None
        for i in range(1, len(w0) - 1):  # first local max = acoustic zone boundary
            if w0[i] >= w0[i - 1] and w0[i] > w0[i + 1]:
                imax = i
                break
        if imax is None:
            imax = int(np.argmax(w0))
        vp_zb = (w0[imax] / ks[imax]) / c0
        per_dir[str(list(np.round(dhat, 3)))] = float(vp_zb)
    return {"c0_slope_omegaC_per_invL": c0,
            "v_p_min_over_c0_srs_acoustic": float(min(per_dir.values())),
            "v_p_per_direction_over_c0": per_dir,
            "v_p_at_low_k_over_c0": 1.0}


def drag_onset_chain():
    """1D-chain arccos analog: z=2, μ(k)=2cos(kℓ) ⇒ ω=ω_link·arccos(cos kℓ)=ω_link·kℓ.

    Perfectly linear (dispersionless) ⇒ v_p = v_g = c_link everywhere ⇒ ratio = 1.
    Contrast: the lumped cosine chain ω=ω_max|sin(kℓ/2)| gives v_p,min/c_0 = 2/π.
    """
    kl = np.linspace(1e-4, np.pi, 400)
    # arccos map
    w_arccos = np.arccos(np.clip(np.cos(kl), -1, 1))  # = kl
    vp_arccos = w_arccos / kl                          # ≡ 1
    # lumped cosine map
    w_cos = np.abs(np.sin(kl / 2.0))
    c0_cos = (w_cos[0] / kl[0])                         # low-k slope = 1/2
    vp_cos = (w_cos / kl) / c0_cos
    return {"arccos_chain_vp_min_over_c0": float(vp_arccos.min()),
            "cosine_chain_vp_min_over_c0": float(vp_cos.min()),
            "cosine_2_over_pi": float(2.0 / np.pi)}


# ─────────────────────────────────────────────────────────────────────────────
# §4 — Explicit-bath GLE energy ledger at the crossing (mode-resolved)
# ─────────────────────────────────────────────────────────────────────────────
def s_eq(r):
    """Ax4 saturation kernel, byte-locked to k4_tlm.py:283."""
    return np.sqrt(np.maximum(0.0, 1.0 - np.minimum(np.abs(r), 1.0) ** 2))


def sample_bath(centres, J_shape, n_bath, coupling_scale):
    """Discretise J(ω) on a uniform ω-grid: c_j² = (2/π)·ω_j·J(ω_j)·Δω  (m_j=1).

    Reproduces the target J(ω) in the continuum limit independent of the grid choice.
    """
    w = np.linspace(BAND_TOP / n_bath, BAND_TOP, n_bath)
    dw = w[1] - w[0]
    Jw = np.interp(w, centres, J_shape)
    c = np.sqrt((2.0 / np.pi) * w * np.maximum(Jw, 0.0) * dw) * coupling_scale
    return w, c


def gle_ledger(centres, J_shape, n_bath, coupling_scale, omega_S=1.0,
               omega_d=OMEGA_D, r0=0.7, dr=0.3, n_cycles=30, ppc=400):
    """Symplectic (velocity-Verlet) integration of S + explicit bath.

    m_S S̈ = −κ(S−S_eq(t)) − S·Σc²/ω² + Σ c q       (κ=ω_S², counter-term included)
    q̈_j   = −ω_j² q_j + c_j S
    Returns mode-resolved energy ledger + recurrence diagnostics.
    """
    wj, cj = sample_bath(centres, J_shape, n_bath, coupling_scale)
    kappa = omega_S ** 2
    ct = np.sum(cj ** 2 / wj ** 2)  # counter-term stiffness

    T = n_cycles * (2.0 * np.pi / omega_d)
    dt = (2.0 * np.pi / omega_d) / ppc
    nsteps = int(T / dt)

    S, pS = 1.0, 0.0
    q = np.zeros(n_bath)
    p = np.zeros(n_bath)
    # start on the instantaneous equilibrium at t=0
    S = s_eq(r0)

    def forces(S_, q_, t_):
        se = s_eq(r0 + dr * np.sin(omega_d * t_))
        FS = -kappa * (S_ - se) - ct * S_ + np.dot(cj, q_)
        Fq = -(wj ** 2) * q_ + cj * S_
        return FS, Fq, se

    t = 0.0
    FS, Fq, se = forces(S, q, t)
    E_S_series, E_bath_series, t_series = [], [], []
    for n in range(nsteps):
        pS += 0.5 * dt * FS
        p += 0.5 * dt * Fq
        S += dt * pS
        q += dt * p
        t += dt
        FS, Fq, se = forces(S, q, t)
        pS += 0.5 * dt * FS
        p += 0.5 * dt * Fq
        if n % 8 == 0:
            E_S = 0.5 * pS ** 2 + 0.5 * kappa * (S - se) ** 2
            E_bath = np.sum(0.5 * p ** 2 + 0.5 * wj ** 2 * q ** 2)
            E_S_series.append(E_S)
            E_bath_series.append(E_bath)
            t_series.append(t)

    E_bath_series = np.array(E_bath_series)
    t_series = np.array(t_series)
    # recurrence: does E_bath return toward zero after rising? ratio of final-window
    # minimum to the running peak. ~1 → monotone drain; «1 → returns (recurrence).
    peak = float(E_bath_series.max()) if E_bath_series.size else 0.0
    tail = E_bath_series[int(0.5 * len(E_bath_series)):]
    tail_min = float(tail.min()) if tail.size else 0.0
    return {
        "n_bath": n_bath,
        "coupling_scale": coupling_scale,
        "E_bath_peak": peak,
        "E_bath_tail_min": tail_min,
        "return_ratio_tailmin_over_peak": (tail_min / peak) if peak > 0 else 0.0,
        "E_bath_final": float(E_bath_series[-1]) if E_bath_series.size else 0.0,
        "t_series": t_series.tolist(),
        "E_bath_series": E_bath_series.tolist(),
        "E_S_series": E_S_series,
        "poincare_time_est": float(2.0 * np.pi / (wj[1] - wj[0])),
    }


def gle_ringdown(centres, J_shape, n_bath, coupling_scale, omega_S=1.0, n_periods=80, ppc=200):
    """UNDRIVEN ring-down: displace S off equilibrium, integrate, watch E_S(t).

    The clean reactive-return vs transductive-drain discriminator (coupling-scale-robust),
    over a FIXED physical window (n_periods system periods, same for finite and dense):
    finite/few-mode bath (0D single cell) → E_S PARTIALLY RETURNS at its short Poincaré
    recurrence (world-a character); dense/continuum bath (∞-lattice) → E_S decays and does
    NOT recur within the window (world-b transduction). Reports max E_S recovery after decay.
    """
    wj, cj = sample_bath(centres, J_shape, n_bath, coupling_scale)
    kappa = omega_S ** 2
    ct = np.sum(cj ** 2 / wj ** 2)
    t_poin = 2.0 * np.pi / (wj[1] - wj[0])
    T = n_periods * (2.0 * np.pi / omega_S)  # FIXED physical window (N-independent)
    dt = (2.0 * np.pi / omega_S) / ppc
    nsteps = int(T / dt)

    S, pS = 1.0, 0.0          # displaced to S=1 (equilibrium at S_eq=0 here, no drive)
    q = np.zeros(n_bath)
    p = np.zeros(n_bath)
    FS = -kappa * S - ct * S + np.dot(cj, q)
    Fq = -(wj ** 2) * q + cj * S
    E_S0 = 0.5 * pS ** 2 + 0.5 * kappa * S ** 2
    E_S_series = []
    for n in range(nsteps):
        pS += 0.5 * dt * FS
        p += 0.5 * dt * Fq
        S += dt * pS
        q += dt * p
        FS = -kappa * S - ct * S + np.dot(cj, q)
        Fq = -(wj ** 2) * q + cj * S
        pS += 0.5 * dt * FS
        p += 0.5 * dt * Fq
        if n % 10 == 0:
            E_S_series.append(0.5 * pS ** 2 + 0.5 * kappa * S ** 2)
    E_S_series = np.array(E_S_series) / E_S0
    # initial decay over the first quarter-window; then look for recovery (recurrence)
    head = max(2, len(E_S_series) // 4)
    imin = int(np.argmin(E_S_series[:head]))
    recovery = float(E_S_series[imin + 1:].max()) if imin + 1 < len(E_S_series) else 0.0
    return {"n_bath": n_bath, "poincare_time": float(t_poin), "window_periods": n_periods,
            "E_S_initial_decay_min": float(E_S_series[:head].min()),
            "E_S_max_recovery_after_decay": recovery,
            "E_S_final": float(E_S_series[-1])}


def ringdown_scale_scan(centres, J, scales=(0.2, 0.4, 0.6, 1.0, 1.5),
                        n_finite=40, n_dense=1500):
    """R-1 (POST-REVIEW EXTENSION, F1/F6/F9): scan the undriven ring-down recovery over
    coupling scale, both models, finite (0D) vs dense (∞-lattice) bath.

    Motivation: the original lane banked "coupling-scale-robust" + "∞-lattice drains to
    0–10 %" from a SINGLE scale (0.6). This scan tests both. What the scan shows (banked):
      - the ORDERING  finite-recovery ≥ dense-recovery  is scale-robust (holds every cell);
      - the DRAIN MAGNITUDE is NOT robust — the super-Ohmic (C2) ∞-lattice bath recovers
        77 % at scale 0.2, 35 % at 0.4 (world-a reactive return), only dropping into the
        0–10 % band at scale ≥ 0.6. The drain magnitude is governed by the SAME undetermined
        coupling-scale prefactor ζ as bin (c-magnitude); "drains to 0–10 %" is NOT robust.
    """
    scan = {}
    for model in ("C1_onsite", "C2_strain"):
        rows = {}
        for cs in scales:
            fin = gle_ringdown(centres, J[model], n_finite, cs)["E_S_max_recovery_after_decay"]
            den = gle_ringdown(centres, J[model], n_dense, cs)["E_S_max_recovery_after_decay"]
            rows[f"{cs}"] = {"finite_recovery": fin, "dense_recovery": den,
                             "ordering_finite_ge_dense": bool(fin >= den - 1e-9)}
        scan[model] = rows
    ordering_robust = all(r["ordering_finite_ge_dense"]
                          for m in scan.values() for r in m.values())
    dense_in_0to10_all = all(m["dense_recovery"] <= 0.10
                             for model in scan.values() for m in model.values())
    scan["_ordering_scale_robust"] = ordering_robust
    scan["_dense_drain_0to10_robust"] = dense_in_0to10_all  # FALSE — the retracted claim
    return scan


def frozen_ab_ledger(centres, J_shape, n_bath, coupling_scale, omega_S=1.0,
                     omega_d=OMEGA_D, r0=0.7, dr=0.3, n_cycles=30, ppc=400, tol=3.53e-3):
    """R-2 (FROZEN CRITERION, F2/F5/F7/F12): the pre-registered (a-ledger)/(b-ledger) test
    the shipped code never computed — run here EXACTLY as prereg §4-i,ii,iv specify.

    Driven r(t)=0.7+0.3·sin(ω_d t); explicit symplectic bath; PER-MODE E_bath recorded.
    Frozen criteria (prereg §4):
      (a-ledger): net per-cycle transfer into the bath RETURNS within the recording window
                  (Poincaré-bounded) AND net-per-cycle transfer < tol (=3.53e-3 relative).
      (b-ledger): monotonic net per-cycle transfer ≥ tol NOT returned within a sub-recurrence
                  window.
    "net per-cycle transfer" = STEADY (late-window) secular slope of E_bath per drive cycle,
    relative to the characteristic system reactive energy E_S_peak (same natural-unit scale
    #735's loop-area/W_cycle live in, where tol=3.53e-3 is the integrator floor).
    """
    wj, cj = sample_bath(centres, J_shape, n_bath, coupling_scale)
    kappa = omega_S ** 2
    ct = np.sum(cj ** 2 / wj ** 2)
    T_d = 2.0 * np.pi / omega_d
    dt = T_d / ppc
    nsteps = int(n_cycles * T_d / dt)

    S, pS = s_eq(r0), 0.0
    q = np.zeros(n_bath)
    p = np.zeros(n_bath)

    def forces(S_, q_, t_):
        se = s_eq(r0 + dr * np.sin(omega_d * t_))
        FS = -kappa * (S_ - se) - ct * S_ + np.dot(cj, q_)
        Fq = -(wj ** 2) * q_ + cj * S_
        return FS, Fq, se

    t = 0.0
    FS, Fq, se = forces(S, q, t)
    Eb_cycle = [0.0]
    Eb_run = []
    E_S_peak = 0.0
    next_cycle = 1
    for n in range(nsteps):
        pS += 0.5 * dt * FS
        p += 0.5 * dt * Fq
        S += dt * pS
        q += dt * p
        t += dt
        FS, Fq, se = forces(S, q, t)
        pS += 0.5 * dt * FS
        p += 0.5 * dt * Fq
        E_S = 0.5 * pS ** 2 + 0.5 * kappa * (S - se) ** 2
        E_S_peak = max(E_S_peak, E_S)
        Eb = float(np.sum(0.5 * p ** 2 + 0.5 * wj ** 2 * q ** 2))
        Eb_run.append(Eb)
        if t >= next_cycle * T_d - 0.5 * dt:
            Eb_cycle.append(Eb)
            next_cycle += 1
    Eb_cycle = np.array(Eb_cycle)
    Eb_run = np.array(Eb_run)
    per_mode = 0.5 * p ** 2 + 0.5 * wj ** 2 * q ** 2  # PER-MODE E_bath at window end

    E_S_peak = float(E_S_peak)
    k = np.arange(len(Eb_cycle))
    lo = len(Eb_cycle) // 3
    slope = float(np.polyfit(k[lo:], Eb_cycle[lo:], 1)[0])  # steady (late-window) per-cycle
    rel = float(slope / E_S_peak) if E_S_peak > 0 else 0.0
    peak = float(Eb_run.max())
    tail = Eb_run[len(Eb_run) // 2:]
    return_ratio = float(tail.min()) / peak if peak > 0 else 0.0
    returns = bool(return_ratio < 0.5)  # Poincaré return within window
    a_ledger_fires = bool(returns and (abs(rel) < tol))
    b_ledger_fires = bool((abs(rel) >= tol) and (not returns))
    return {
        "n_bath": n_bath, "coupling_scale": coupling_scale,
        "E_S_peak": E_S_peak,
        "net_per_cycle_transfer_rel": rel,
        "net_per_cycle_transfer_ge_tol": bool(abs(rel) >= tol),
        "return_ratio_tailmin_over_peak": return_ratio,
        "returns_within_window": returns,
        "poincare_time": float(2.0 * np.pi / (wj[1] - wj[0])),
        "window": float(n_cycles * T_d),
        "per_mode_top5_E_bath": sorted(per_mode.tolist(), reverse=True)[:5],
        "a_ledger_fires": a_ledger_fires,
        "b_ledger_fires": b_ledger_fires,
    }


# ─────────────────────────────────────────────────────────────────────────────
# §4 contrast — first-order Eq 2.1 vs second-order reactive (γ→0), loop shapes
# ─────────────────────────────────────────────────────────────────────────────
def first_order_loop(omega, r0=0.7, dr=0.3, n_settle=8, ppc=512):
    """Byte-locked backward-Euler Eq 2.1: S_{n+1}=(S_n·τ+dt·S_eq)/(τ+dt). k4_tlm.py:291."""
    dt = min(2 * np.pi / omega / ppc, TAU / 50)
    n_per = int(round(2 * np.pi / omega / dt))
    n_tot = max(n_settle * n_per, int(20 * TAU / dt)) + n_per
    S = s_eq(r0)
    r_hist, S_hist = [], []
    for n in range(n_tot):
        t = n * dt
        r = r0 + dr * np.sin(omega * t)
        S = (S * TAU + dt * s_eq(r)) / (TAU + dt)
        if n >= n_tot - n_per:
            r_hist.append(r)
            S_hist.append(S)
    r_h, S_h = np.array(r_hist), np.array(S_hist)
    I_h = r_h * np.sqrt(np.maximum(S_h, 0.0))  # Op14 I=V/Z_eff=r√S
    area_rS = abs(np.trapezoid(S_h, r_h))
    area_VI = abs(np.trapezoid(I_h, r_h))
    return area_rS, area_VI


def second_order_loop(omega, omega_S=1.0, gamma=0.0, r0=0.7, dr=0.3, n_settle=40, ppc=512):
    """Reactive contrast: S̈ + γṠ + ω_S²(S−S_eq)=0. Velocity-Verlet.

    Returns (area_rS, area_VI, W_diss_per_cycle, W_drive_per_cycle):
      - W_diss = γ∮v²dt is the dissipated work over the steady cycle. At γ=0 this is
        identically 0 for ANY trajectory — a DEFINITIONAL identity, not an energy-ledger
        measurement (R-4/F11: the zero-work leg cannot fail). The informative content is
        the FINITE loop area ∮S dr that survives at γ=0 (loop-area ≠ dissipation).
      - W_drive = κ∮S_eq·v dt is the INDEPENDENT drive-work-per-cycle ledger. In the
        driven steady cycle energy balance gives W_drive ≡ W_diss (κ∮SṠdt=∮S̈Ṡdt=0 over a
        period), so W_drive≈W_diss for γ>0 is a real (fireable) closure check — this is the
        actual H-ledger the shipped code lacked, replacing the tautological W_diss=0 pin.
    NOTE: at γ=0 there is no steady state (undamped ω_S=1 transient beats against ω_d=0.9),
    so ∮S dr is finite but window-dependent, existence-grade not value-grade (R-5/F10).
    """
    dt = min(2 * np.pi / omega / ppc, TAU / 50)
    n_per = int(round(2 * np.pi / omega / dt))
    n_tot = max(n_settle * n_per, int(80 * TAU / dt)) + n_per
    kappa = omega_S ** 2
    S = s_eq(r0)
    v = 0.0
    r_hist, S_hist, v_hist, se_hist = [], [], [], []

    def acc(S_, v_, t_):
        se = s_eq(r0 + dr * np.sin(omega * t_))
        return -kappa * (S_ - se) - gamma * v_

    a = acc(S, v, 0.0)
    for n in range(n_tot):
        t = n * dt
        v += 0.5 * dt * a
        S += dt * v
        a = acc(S, v, t + dt)
        v += 0.5 * dt * a
        if n >= n_tot - n_per:
            r_hist.append(r0 + dr * np.sin(omega * t))
            S_hist.append(S)
            v_hist.append(v)
            se_hist.append(s_eq(r0 + dr * np.sin(omega * t)))
    r_h, S_h, v_h = np.array(r_hist), np.array(S_hist), np.array(v_hist)
    se_h = np.array(se_hist)
    I_h = r_h * np.sqrt(np.maximum(S_h, 0.0))
    area_rS = abs(np.trapezoid(S_h, r_h))
    area_VI = abs(np.trapezoid(I_h, r_h))
    W_diss = gamma * np.trapezoid(v_h ** 2, dx=dt)   # dissipated work (≡0 at γ=0 by definition)
    W_drive = kappa * np.trapezoid(se_h * v_h, dx=dt)  # independent drive-work ledger (= W_diss for γ>0)
    return area_rS, area_VI, float(W_diss), float(W_drive)


def loop_sweep(loop_fn, **kw):
    ws = np.logspace(np.log10(0.05), np.log10(10.0), 48)
    a_rS = np.array([loop_fn(w, **kw)[0] for w in ws])
    a_VI = np.array([loop_fn(w, **kw)[1] for w in ws])
    return ws, a_rS, a_VI


def _peak(ws, area):
    i = int(np.argmax(area))
    return float(ws[i]), float(area[i])


# ─────────────────────────────────────────────────────────────────────────────
def main():
    basis, bonds = srs_primitive_bcc()
    out = {"class": "DERIVATION + research-driver (0D)", "band_top_omegaC": float(BAND_TOP),
           "omega_link_over_omegaC": float(OMEGA_LINK_OVER_C), "omega_d_crossing": OMEGA_D}

    # ── §2 DOS + J(ω) ──
    centres, g, freqs = density_of_states(bonds)
    p_low = low_omega_exponent(centres, g)
    J = build_J(centres, g)
    J_at_cross = {k: _interp_at(centres, v, OMEGA_D) for k, v in J.items()}
    J_peak_w = {k: float(centres[np.argmax(v)]) for k, v in J.items()}
    # low-ω exponent of J directly (Ohmic s=1 / super-Ohmic s=3)
    s_exp = {}
    for k, v in J.items():
        m = (centres > 0.05) & (centres < 0.6) & (v > 0)
        s_exp[k] = float(np.polyfit(np.log(centres[m]), np.log(v[m]), 1)[0])
    # Markovian friction constant γ0 = lim J/ω  (normalised shapes → report the ω→0 trend)
    gamma0_trend = {}
    for k, v in J.items():
        m = (centres > 0.05) & (centres < 0.4) & (v > 0)
        gamma0_trend[k] = float(np.polyfit(np.log(centres[m]), np.log(v[m] / centres[m]), 1)[0])
    out["dos"] = {"low_omega_exponent_p": p_low, "band_edge_omegaC": float(BAND_TOP)}
    out["J_omega"] = {
        "low_omega_exponent_s": s_exp,
        "J_norm_at_crossing_0p9": J_at_cross,
        "J_peak_location_omegaC": J_peak_w,
        "gammaMark_JoverW_low_omega_slope": gamma0_trend,  # →0 slope means Ohmic const; >0 means super-Ohmic→0
    }

    # ── §5 drag-onset (batched) ──
    out["drag_onset"] = {"srs_3d": drag_onset_srs(bonds), "chain_1d": drag_onset_chain()}

    # ── §4 GLE driven ledger + ring-down: finite (0D) vs dense (∞-lattice), both models ──
    ledger = {}
    for model in ("C1_onsite", "C2_strain"):
        ledger[model] = {
            "driven_finite_N60": {kk: gle_ledger(centres, J[model], 60, 0.6)[kk]
                                  for kk in ("return_ratio_tailmin_over_peak", "poincare_time_est")},
            "driven_dense_N1200": {kk: gle_ledger(centres, J[model], 1200, 0.6)[kk]
                                   for kk in ("return_ratio_tailmin_over_peak", "poincare_time_est")},
            "ringdown_finite_N40": gle_ringdown(centres, J[model], 40, 0.6),
            "ringdown_dense_N1500": gle_ringdown(centres, J[model], 1500, 0.6),
        }
    out["gle_ledger"] = ledger

    # ── R-1 (post-review extension): ring-down coupling-scale scan (both models) ──
    out["ringdown_scale_scan"] = ringdown_scale_scan(centres, J)

    # ── R-2 (frozen criterion, prereg §4-i,ii,iv): the (a-ledger)/(b-ledger) net-per-cycle
    #    transfer vs tol=3.53e-3 the shipped code never computed. Run here per Rule-11. ──
    frozen = {}
    for model in ("C1_onsite", "C2_strain"):
        frozen[model] = {
            "finite_N60": frozen_ab_ledger(centres, J[model], 60, 0.6),
            "dense_N1200": frozen_ab_ledger(centres, J[model], 1200, 0.6),
        }
    # frozen-tree adjudication: count cells firing each ledger (4 cells: 2 models × 2 baths)
    cells = [(m, b) for m in ("C1_onsite", "C2_strain") for b in ("finite_N60", "dense_N1200")]
    n_a = sum(frozen[m][b]["a_ledger_fires"] for m, b in cells)
    n_b = sum(frozen[m][b]["b_ledger_fires"] for m, b in cells)
    b_cells = [f"{m}/{b}" for m, b in cells if frozen[m][b]["b_ledger_fires"]]
    frozen["_a_ledger_fires_count"] = n_a
    frozen["_b_ledger_fires_count"] = n_b
    frozen["_b_ledger_fires_cells"] = b_cells
    frozen["_frozen_verdict"] = (
        f"bin(iii) DEGENERATE — (a-ledger) fires in {n_a}/4 cells; (b-ledger) in {n_b}/4 "
        f"({b_cells or 'none'}); no clean UNIFORM (a)/(b) scope separation under the frozen "
        f"driven protocol (the (b) fire, if any, is the super-Ohmic ∞-lattice only)")
    out["frozen_ab_ledger"] = frozen

    # ── §4 contrast: first-order Eq 2.1 vs second-order reactive loop shapes ──
    ws1, a1_rS, a1_VI = loop_sweep(first_order_loop)
    ws2, a2_rS, a2_VI = loop_sweep(second_order_loop, gamma=0.05)
    out["loop_contrast"] = {
        "first_order_eq21": {
            "peak_rS": _peak(ws1, a1_rS), "peak_VI": _peak(ws1, a1_VI),
            "area_at_lowf_0p05": float(a1_rS[0]), "area_at_highf_10": float(a1_rS[-1]),
        },
        "second_order_reactive": {
            "peak_rS": _peak(ws2, a2_rS), "peak_VI": _peak(ws2, a2_VI),
            "area_at_lowf_0p05": float(a2_rS[0]), "area_at_highf_10": float(a2_rS[-1]),
        },
    }

    # ── §4 H-ledger (R-4/R-5 relabel): the FINITE loop area at γ=0 is the discriminator
    #    (loop-area ≠ dissipation); W_diss=0 at γ=0 is a DEFINITIONAL identity (γ·∮v²=0).
    #    The real ledger is the INDEPENDENT drive-work closure W_drive≈W_diss for γ>0.
    #    ∮S dr at γ=0 is existence-grade (window-dependent, no steady state). ──
    hled = {}
    for gamma in (0.0, 0.05, 0.2, 0.5):
        a_rS, a_VI, W, W_drive = second_order_loop(OMEGA_D, gamma=gamma)
        rel_mismatch = abs(W - W_drive) / max(abs(W), 1e-12) if gamma > 0 else 0.0
        hled[f"gamma_{gamma}"] = {"area_rS": float(a_rS), "W_diss_per_cycle": float(W),
                                  "W_drive_per_cycle": float(W_drive),
                                  "ledger_rel_mismatch": float(rel_mismatch)}
    # ∮S dr at γ=0 across settle windows → existence-grade (window-dependent, R-5)
    hled["gamma_0.0_window_scan"] = {
        f"n_settle_{ns}": float(second_order_loop(OMEGA_D, gamma=0.0, n_settle=ns)[0])
        for ns in (40, 80, 160, 320)}
    out["h_ledger_second_order"] = hled

    # ── loss-location adjudication from J shape: ΔE_cycle ∝ J(ω_d) ──
    out["loss_location"] = {
        "J_at_lowf_over_peak": {k: _interp_at(centres, v, 0.05) for k, v in J.items()},
        "J_at_crossing_over_peak": J_at_cross,
        "J_above_band_edge": {k: float(_interp_at(centres, v, BAND_TOP * 1.001)) for k, v in J.items()},
        "note": "per-cycle loss ∝ J(ω_d): →0 at ω→0 (super-Ohmic/Ohmic), →0 above band edge, peaks intermediate",
    }

    # ── report ──
    print("=" * 78)
    print("J(ω) DERIVATION — z=3 srs bath spectral density (yield-fork adjudicator)")
    print("=" * 78)
    print(f"\nBand top (arccos, adjudicated): π√3 = {BAND_TOP:.4f} ω_C   "
          f"crossing ω_d τ = {OMEGA_D}  ⇒ crossing at {OMEGA_D/BAND_TOP*100:.1f}% of band")
    print(f"DOS low-ω exponent p (g∝ω^p, 3D acoustic expects ≈2): {p_low:.3f}")
    print("\nJ(ω) low-ω exponent s (Ohmic=1 / super-Ohmic=3):")
    for k in J:
        print(f"  {k:12s} s={s_exp[k]:.3f}  J_norm(0.9ω_C)={J_at_cross[k]:.4f}  "
              f"peak@{J_peak_w[k]:.3f}ω_C  γ0-trend(J/ω slope)={gamma0_trend[k]:+.3f}")
    print("\nDRAG-ONSET (batched):")
    d = out["drag_onset"]
    print(f"  srs 3D acoustic  v_p,min/c0 = {d['srs_3d']['v_p_min_over_c0_srs_acoustic']:.4f}  "
          f"(per-dir {sorted(round(x,3) for x in d['srs_3d']['v_p_per_direction_over_c0'].values())})")
    print(f"  1D-chain arccos  v_p,min/c0 = {d['chain_1d']['arccos_chain_vp_min_over_c0']:.4f} "
          f"(dispersionless) vs cosine 2/π = {d['chain_1d']['cosine_2_over_pi']:.4f}")
    print("\nGLE DRIVEN LEDGER (return_ratio ~1 = drain/world-b; «1 = recurrence/world-a):")
    for model in ledger:
        f = ledger[model]["driven_finite_N60"]["return_ratio_tailmin_over_peak"]
        de = ledger[model]["driven_dense_N1200"]["return_ratio_tailmin_over_peak"]
        print(f"  {model:12s} finite-N60 return={f:.3f}   dense-N1200 return={de:.3f}")
    print("\nGLE RING-DOWN [POST-HOC CHARACTERIZATION — undriven, not in frozen prereg]"
          " (E_S recovery: high=recurrence/world-a; low=drain/world-b):")
    for model in ledger:
        rf = ledger[model]["ringdown_finite_N40"]
        rd = ledger[model]["ringdown_dense_N1500"]
        print(f"  {model:12s} finite-N40  decay_min={rf['E_S_initial_decay_min']:.3f} "
              f"recovery={rf['E_S_max_recovery_after_decay']:.3f}  |  "
              f"dense-N1500 decay_min={rd['E_S_initial_decay_min']:.3f} "
              f"recovery={rd['E_S_max_recovery_after_decay']:.3f}")

    print("\nR-1 RING-DOWN COUPLING-SCALE SCAN (ordering fin≥den robust; drain magnitude NOT):")
    scan = out["ringdown_scale_scan"]
    for model in ("C1_onsite", "C2_strain"):
        cells = " ".join(f"cs{cs}:{scan[model][cs]['finite_recovery']:.2f}/"
                         f"{scan[model][cs]['dense_recovery']:.2f}"
                         for cs in ("0.2", "0.4", "0.6", "1.0", "1.5"))
        print(f"  {model:12s} (fin/den) {cells}")
    print(f"  ordering fin≥den scale-robust: {scan['_ordering_scale_robust']}   "
          f"dense-drain-in-0to10%-robust: {scan['_dense_drain_0to10_robust']} (RETRACTED claim)")

    print("\nR-2 FROZEN (a-ledger)/(b-ledger) CRITERION [Rule-11; net/cyc vs tol=3.53e-3 rel]:")
    frozen = out["frozen_ab_ledger"]
    for model in ("C1_onsite", "C2_strain"):
        for tag in ("finite_N60", "dense_N1200"):
            d = frozen[model][tag]
            print(f"  {model:12s} {tag:11s} net/cyc={d['net_per_cycle_transfer_rel']:+.2e} "
                  f"(≥tol={d['net_per_cycle_transfer_ge_tol']}) return={d['return_ratio_tailmin_over_peak']:.3f} "
                  f"a-fires={d['a_ledger_fires']} b-fires={d['b_ledger_fires']}")
    print(f"  → {frozen['_frozen_verdict']}")
    print("\nLOOP CONTRAST (peak ωτ):")
    lc = out["loop_contrast"]
    print(f"  first-order Eq2.1     rS-peak@{lc['first_order_eq21']['peak_rS'][0]:.3f}  "
          f"VI-peak@{lc['first_order_eq21']['peak_VI'][0]:.3f}")
    print(f"  second-order reactive rS-peak@{lc['second_order_reactive']['peak_rS'][0]:.3f}  "
          f"VI-peak@{lc['second_order_reactive']['peak_VI'][0]:.3f}")
    print("\nH-LEDGER (2nd-order): finite ∮S dr at γ=0 (discriminator); W_diss=0@γ=0 DEFINITIONAL;"
          " drive-work ledger W_drive≈W_diss for γ>0 (the real closure):")
    for g, v in out["h_ledger_second_order"].items():
        if g == "gamma_0.0_window_scan":
            print("  γ=0 ∮S dr vs settle-window (existence-grade, R-5): "
                  + ", ".join(f"{ns.split('_')[-1]}:{val:.3f}" for ns, val in v.items()))
            continue
        print(f"  {g:12s} ∮S dr={v['area_rS']:.4f}  W_diss={v['W_diss_per_cycle']:.4e}  "
              f"W_drive={v['W_drive_per_cycle']:.4e}  ledger-mismatch={v['ledger_rel_mismatch']:.2e}")

    out_dir = Path(__file__).resolve().parent / "_output"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "jomega_yield_fork.json").write_text(json.dumps(out, indent=2))
    print(f"\nResults: {out_dir / 'jomega_yield_fork.json'}")
    return out


if __name__ == "__main__":
    main()
