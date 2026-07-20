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

    Returns (area_rS, area_VI, W_diss_per_cycle) where W_diss = γ∮v²dt is the dissipated
    work over the steady cycle. W_diss → 0 as γ → 0 (the LOSSLESS limit) even though the
    reactive loop area ∮S dr stays FINITE — the H-ledger, not the loop area, is the
    first-vs-second-order discriminator (#735 F-B3).
    """
    dt = min(2 * np.pi / omega / ppc, TAU / 50)
    n_per = int(round(2 * np.pi / omega / dt))
    n_tot = max(n_settle * n_per, int(80 * TAU / dt)) + n_per
    kappa = omega_S ** 2
    S = s_eq(r0)
    v = 0.0
    r_hist, S_hist, v_hist = [], [], []

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
    r_h, S_h, v_h = np.array(r_hist), np.array(S_hist), np.array(v_hist)
    I_h = r_h * np.sqrt(np.maximum(S_h, 0.0))
    area_rS = abs(np.trapezoid(S_h, r_h))
    area_VI = abs(np.trapezoid(I_h, r_h))
    W_diss = gamma * np.trapezoid(v_h ** 2, dx=dt)  # dissipated work over the recorded cycle
    return area_rS, area_VI, float(W_diss)


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

    # ── §4 H-ledger: dissipated work per cycle W_diss → 0 as γ → 0 (lossless limit) ──
    #    while the reactive loop area ∮S dr stays FINITE (the true discriminator).
    hled = {}
    for gamma in (0.0, 0.05, 0.2, 0.5):
        a_rS, a_VI, W = second_order_loop(OMEGA_D, gamma=gamma)
        hled[f"gamma_{gamma}"] = {"area_rS": float(a_rS), "W_diss_per_cycle": float(W)}
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
    print("\nGLE RING-DOWN (E_S recovery after decay: high=recurrence/world-a; low=drain/world-b):")
    for model in ledger:
        rf = ledger[model]["ringdown_finite_N40"]
        rd = ledger[model]["ringdown_dense_N1500"]
        print(f"  {model:12s} finite-N40  decay_min={rf['E_S_initial_decay_min']:.3f} "
              f"recovery={rf['E_S_max_recovery_after_decay']:.3f}  |  "
              f"dense-N1500 decay_min={rd['E_S_initial_decay_min']:.3f} "
              f"recovery={rd['E_S_max_recovery_after_decay']:.3f}")
    print("\nLOOP CONTRAST (peak ωτ):")
    lc = out["loop_contrast"]
    print(f"  first-order Eq2.1     rS-peak@{lc['first_order_eq21']['peak_rS'][0]:.3f}  "
          f"VI-peak@{lc['first_order_eq21']['peak_VI'][0]:.3f}")
    print(f"  second-order reactive rS-peak@{lc['second_order_reactive']['peak_rS'][0]:.3f}  "
          f"VI-peak@{lc['second_order_reactive']['peak_VI'][0]:.3f}")
    print("\nH-LEDGER (2nd-order): W_diss→0 as γ→0 while ∮S dr stays finite (the discriminator):")
    for g, v in out["h_ledger_second_order"].items():
        print(f"  {g:12s} ∮S dr={v['area_rS']:.4f}  W_diss/cycle={v['W_diss_per_cycle']:.4e}")

    out_dir = Path(__file__).resolve().parent / "_output"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "jomega_yield_fork.json").write_text(json.dumps(out, indent=2))
    print(f"\nResults: {out_dir / 'jomega_yield_fork.json'}")
    return out


if __name__ == "__main__":
    main()
