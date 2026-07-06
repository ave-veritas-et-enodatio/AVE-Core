#!/usr/bin/env python3
"""EM keying ROUND 2 — the SEVEN FROZEN CONSTRAINT FALSIFIERS under the WORKED functional.

FROZEN prereg: research/2026-07-05_em-keying-round2-worked-cell_prereg_FROZEN.md
Freeze commit gated on: e4312c43.

The DERIVED worked functional (STEP 1, em_keying_round2_derivation.py):
    S_E[E(.)] = sqrt(1 - c_W * W),   W = W_var = (Var_t E)/E_c^2   [WORKED-VAR, freq-independent]
                                     (alt sub-bin W_beat = <(dt E)^2>/(wC^2 Ec^2), freq-suppressed)
The keying variable is the TIME-VARIANCE of the field at the cell -- ZERO for any field STATIC
IN TIME (bare Coulomb, hidden-momentum circulation, boosted uniform static), nonzero for a cyclic
drive (pump, standing wave). This is evaluated as-derived against the seven frozen falsifiers.

REUSES the #539 machinery (import, not reimplement) for the physical-H falsifier and the Route-C
S_B dual. NO parameter is chosen to satisfy any constraint.
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

import numpy as np
from scipy.integrate import IntegrationWarning

from ave.core.constants import (
    C_0,
    E_YIELD,
    EPSILON_0,
    HBAR,
    L_NODE,
    M_PROTON,
    MU_0,
    OMEGA_C,
    XI_TOPO,
    Z_0,
    e_charge,
)

sys.path.insert(0, str(Path(__file__).resolve().parent))
import problem3_muonic_lamb_shift as p3  # noqa: E402

warnings.filterwarnings("ignore", category=IntegrationWarning)

E_C = E_YIELD
I_MAX = XI_TOPO * C_0
J_TO_ueV = 1.0 / e_charge * 1e6

# the two norm-fork coefficients (carried OPEN; STEP 4). Moot for the physical-H falsifier
# (W=0 for a static-in-time field for ANY coefficient).
C_W_YIELD = 1.0                 # NORM-YIELD: W_var = 1/2 (E/Ec)^2 for a wave; matches Letter A^2/...
C_W_CLOCK = 1.0 / (4.0 * np.pi)  # NORM-CLOCK: rest-energy-per-clock normalization


# ============================================================ the DERIVED worked functional
def worked_content_W(E_timeseries, dt, coeff=C_W_YIELD, mode="var"):
    """The worked content W of a time-series E(t) at a cell (dimensionless, /Ec^2).

    mode='var'       : W_var  = Var_t(E)/Ec^2            (AC-variance, DC-BLIND)        [WORKED-VAR, SELECTED]
    mode='meansquare': W_ms   = <E^2>/Ec^2               (mean-square, DC-INCLUDED)     [ledger-forced reading]
    mode='beat'      : W_beat = <(dE/dt)^2>/(wC^2 Ec^2)  (temporal-gradient, rate)      [WORKED-BEAT, killed]
    W_var and W_ms are IDENTICAL for a zero-mean wave and differ ONLY on the DC baseline: a held DC
    field gives W_var=0 (blind) but W_ms>0 (loaded). The LC ledger DERIVES the amplitude class (var/ms
    over beat) but does NOT discriminate var vs ms (§crux); the held-DC discriminating input picks ms.
    A field STATIC IN TIME -> W_var=0, W_beat=0, but W_ms=<E^2> != 0 (the mean-square/DC-included reading).
    """
    E = np.asarray(E_timeseries, dtype=float)
    if mode == "var":
        W = np.var(E) / E_C**2  # stable two-pass variance (a constant array -> exactly 0)
    elif mode == "meansquare":
        W = np.mean(E**2) / E_C**2  # DC-included; nonzero even for a held static field
    elif mode == "beat":
        dEdt = np.gradient(E, dt)
        W = np.mean(dEdt**2) / (OMEGA_C**2 * E_C**2)
    else:
        raise ValueError(mode)
    return coeff * float(W)


def worked_content_W_analytic(E0_over_Ec, omega_over_wC, static_in_time, coeff=C_W_YIELD, mode="var"):
    """Closed-form W for a mono-frequency cell drive E(t)=E0 cos(w t) (independent of the
    time-series path). static_in_time=True -> constant field -> W=0 for both modes."""
    if static_in_time:
        return 0.0
    if mode == "var":
        return coeff * 0.5 * E0_over_Ec**2                     # 1/2 (E0/Ec)^2  [freq-INDEP]
    elif mode == "beat":
        return coeff * 0.5 * (omega_over_wC**2) * E0_over_Ec**2  # 1/2 (w/wC)^2 (E0/Ec)^2
    raise ValueError(mode)


# ---------------------------------------------------------- physical atomic fields (STATIC in TIME)
MU_N = e_charge * HBAR / (2.0 * M_PROTON)
MU_P = 2.7928473446 * MU_N  # proton magnetic moment (CODATA 2018, EXTERNAL)


def E_coulomb(r):
    """Muon static Coulomb field E(r)=K/r^2 -- STATIC IN TIME (fixed charge)."""
    return p3.K / np.asarray(r, dtype=float) ** 2


def H_atomic(r):
    """Proton magnetic dipole H(r) -- STATIC IN TIME (permanent moment). The ROUND-1 killer field:
    it makes the LOCAL pointwise E x H nonzero, but it is CONSTANT IN TIME, so the WORKED content
    W = Var_t(E) = 0 -- the round-1 killer dissolves with NO net-vs-local machinery."""
    r = np.asarray(r, dtype=float)
    B = MU_0 * MU_P / (4.0 * np.pi * r**3)
    return B / MU_0


# ================================================= CONSTRAINT 1: MUONIC-H (physical, STATIC-IN-TIME)
def constraint_1_muonic(r_cut_factors=(0.5, 1.0, 2.0)):
    """The physical muonic-H atom under the SELECTED variance keying -- passes CONDITIONALLY.

    Under the SELECTED variance member (W_var: static-in-time -> W=0 exactly), the atom is blind.
    (Under the ledger-forced MEAN-SQUARE reading it is NOT blind -- see
    constraint_1_muonic_meansquare_counterfactual, which re-kills the E-key at ~4 OOM, reproducing
    #539.) This function evaluates the SELECTED-variance branch.

    The atom's fields (Coulomb E, proton-dipole H) are BOTH STATIC IN TIME. So the worked content
    W = Var_t(E) = 0 IDENTICALLY at every cell -> S_E = sqrt(1-0) = 1 -> delta[Delta E] = 0 EXACTLY.
    This is the round-1 killer DISSOLVING: round-1's LOCAL-Poynting keyed on the pointwise E x H
    (nonzero for the static H), and CRITICAL-1 killed it; the WORKED functional keys on the TIME
    variance (zero for a static-in-time field), so the physical H is blind for the RIGHT reason
    (static in TIME, not net-vs-local). We show delta=0 through the SAME #539 bracket pipeline.

    NULL-VERDICT LIVENESS (trigger 10): the SAME pipeline fed a TIME-VARYING drive (an optical-band
    field at the cell) returns delta != 0 -- proving the zero is physics (static-in-time -> not
    worked), NOT a bookkeeping zero for any field.
    """
    from scipy import integrate

    a = p3.A_MU
    r_hi = 60.0 * a
    N2s = p3._norm(p3.rho_2s)
    N2p = p3._norm(p3.rho_2p)

    # --- the WORKED readout on the physical (static-in-time) atom: W=0 everywhere ---
    # build a short time-series at each radius: the field is CONSTANT in time -> Var=0.
    def W_physical_at(r):
        E_series = np.full(64, float(E_coulomb(r)))  # static in time
        return worked_content_W(E_series, dt=1.0, mode="var")

    W_at = {f"{f:g}a": W_physical_at(f * a) for f in (0.1, 0.5, 1.0, 2.0)}

    # --- the level shift: S_E=1 everywhere -> dV_excess=0 -> shift=0 EXACTLY ---
    def dV_field_excess(r, r_cut):
        if r < r_cut:
            return 0.0
        E_C_r = float(E_coulomb(r))
        W = W_physical_at(r)  # == 0 for the static-in-time atom
        S = np.sqrt(np.clip(1.0 - W, 1e-12, 1.0))
        return E_C_r / S - E_C_r  # == 0 since S==1

    def shift_ueV(r_cut):
        def dV_of_r(r):
            val, _ = integrate.quad(lambda rp: dV_field_excess(rp, r_cut), r, r_hi, limit=150)
            return -val

        def bracket(rho, norm):
            val, _ = integrate.quad(
                lambda r: e_charge * dV_of_r(r) * rho(r) / norm, r_cut, r_hi, limit=100)
            return val

        return (bracket(p3.rho_2s, N2s) - bracket(p3.rho_2p, N2p)) * J_TO_ueV

    shifts = {f: shift_ueV(f * a) for f in r_cut_factors}
    worst = max(abs(v) for v in shifts.values())

    # --- NULL-VERDICT LIVENESS: a TIME-VARYING drive at the cell gives W != 0 -> shift != 0 ---
    # feed the SAME pipeline an optical-band amplitude-modulated field (worked), read nonzero.
    def W_worked_at(r):
        # an optical-band drive of local amplitude ~ the Coulomb field, cycling in time
        t = np.linspace(0.0, 2 * np.pi, 256, endpoint=False)
        E_series = float(E_coulomb(r)) * np.cos(t)  # TIME-VARYING at this cell
        return worked_content_W(E_series, dt=t[1] - t[0], mode="var")

    def dV_worked_excess(r, r_cut):
        if r < r_cut:
            return 0.0
        E_C_r = float(E_coulomb(r))
        W = min(W_worked_at(r), 0.9)  # clip below the rail for the liveness probe
        S = np.sqrt(np.clip(1.0 - W, 1e-6, 1.0))
        return E_C_r / S - E_C_r

    def live_shift_ueV(r_cut):
        def dV_of_r(r):
            val, _ = integrate.quad(lambda rp: dV_worked_excess(rp, r_cut), r, r_hi, limit=120)
            return -val

        def bracket(rho, norm):
            val, _ = integrate.quad(
                lambda r: e_charge * dV_of_r(r) * rho(r) / norm, r_cut, r_hi, limit=80)
            return val

        return (bracket(p3.rho_2s, N2s) - bracket(p3.rho_2p, N2p)) * J_TO_ueV

    live_ueV = live_shift_ueV(1.0 * a)

    return {
        "W_physical_at": W_at,                      # all == 0 (static in time)
        "shifts_ueV_by_rcut": {f"{f:g}a_mu": shifts[f] for f in r_cut_factors},
        "worst_abs_shift_ueV": worst,               # == 0 exactly
        "window_ueV": p3.WINDOW_ueV_primary,
        "passes": worst < p3.WINDOW_ueV_primary,    # TRUE -> the round-1 killer dissolves
        "liveness_worked_shift_ueV": live_ueV,      # != 0 -> the zero is physics, not bookkeeping
    }


# ============================= CONSTRAINT 1 COUNTERFACTUAL: mean-square key re-kills (reproduces #539)
def constraint_1_muonic_meansquare_counterfactual(r_cut_factors=(0.5, 1.0, 2.0)):
    """CONDITIONALITY MACHINE-ANCHOR: under the ledger-forced MEAN-SQUARE reading the muon RE-KILLS
    the E-key, reproducing #539 [C-EXCLUDED]. This is a CONSISTENCY check, NOT a falsifier of the
    SELECTED variance keying.

    The §crux establishes that the LC ledger cannot discriminate variance from mean-square, and the
    only discriminating input (a held DC) picks the MEAN-SQUARE (<A_V^2>, DC-included). Feeding that
    ledger-forced mean-square key through the SAME #539 bracket pipeline as constraint_1_muonic (the
    identical K.E_coulomb / p3.rho_2s / p3.rho_2p imports), the muon's STATIC Coulomb field is NOW
    loaded (W_ms = <E^2>/Ec^2 != 0 even though it is static in time), so S_E < 1 and the level shift
    is nonzero and LARGE -- overshooting the 2.3 ueV CREMA window by ~4 OOM at r_cut=1.0 a_mu
    (+1.36e4 ueV), reproducing #539 [C-EXCLUDED]. This is the empirical evidence that the DC-INCLUDED
    E-key is falsified at atomic scales -- i.e. under the reading the ledger actually forces, the
    E-key fails. The SELECTED variance member (W_var, static-in-time -> W=0) is what makes the muon
    PASS; the mean-square member does not.
    """
    from scipy import integrate

    a = p3.A_MU
    r_hi = 60.0 * a
    N2s = p3._norm(p3.rho_2s)
    N2p = p3._norm(p3.rho_2p)

    # the ledger-forced MEAN-SQUARE key on the physical (static-in-time) Coulomb field: W_ms != 0
    def W_ms_at(r):
        E_series = np.full(64, float(E_coulomb(r)))  # static in time
        return worked_content_W(E_series, dt=1.0, mode="meansquare")  # DC-included -> nonzero

    W_at = {f"{f:g}a": W_ms_at(f * a) for f in (0.1, 0.5, 1.0, 2.0)}

    def dV_field_excess(r, r_cut):
        if r < r_cut:
            return 0.0
        E_C_r = float(E_coulomb(r))
        W = min(W_ms_at(r), 1.0 - 1e-6)  # clip below the saturation rail
        S = np.sqrt(np.clip(1.0 - W, 1e-12, 1.0))
        return E_C_r / S - E_C_r  # != 0 since W_ms > 0 (DC loaded)

    def shift_ueV(r_cut):
        def dV_of_r(r):
            val, _ = integrate.quad(lambda rp: dV_field_excess(rp, r_cut), r, r_hi, limit=150)
            return -val

        def bracket(rho, norm):
            val, _ = integrate.quad(
                lambda r: e_charge * dV_of_r(r) * rho(r) / norm, r_cut, r_hi, limit=100)
            return val

        return (bracket(p3.rho_2s, N2s) - bracket(p3.rho_2p, N2p)) * J_TO_ueV

    shifts = {f: shift_ueV(f * a) for f in r_cut_factors}
    worst = max(abs(v) for v in shifts.values())
    shift_at_1a = shifts[1.0]

    return {
        "W_ms_at": W_at,                            # all != 0 (DC-included, static-in-time loaded)
        "shifts_ueV_by_rcut": {f"{f:g}a_mu": shifts[f] for f in r_cut_factors},
        "shift_at_1a_ueV": shift_at_1a,             # ~ +1.36e4 ueV
        "worst_abs_shift_ueV": worst,               # ~ 2.25e6 ueV (at 0.5 a)
        "window_ueV": p3.WINDOW_ueV_primary,        # 2.3 ueV
        "re_kills": worst > p3.WINDOW_ueV_primary,  # TRUE -> re-kills the E-key -> reproduces #539
        "overshoot_factor_at_1a": abs(shift_at_1a) / p3.WINDOW_ueV_primary,  # ~ 5.9e3 (>1e3)
    }


# ================================================ CONSTRAINT 2: THE PUMP (Table I, both sub-bins)
def constraint_2_pump():
    """S_E at the Letter's pump. The pump is a PROPAGATING optical wave -> the cell is cyclically
    WORKED at the pump omega. Report the DERIVED coefficient under BOTH sub-bins + BOTH norm arms."""
    I_pump = 1e21 * 1e4  # W/cm^2 -> W/m^2
    E_pump = np.sqrt(2.0 * I_pump / (C_0 * EPSILON_0))  # peak carrier amplitude
    A2_letter = (E_pump / E_C) ** 2
    r_pump = 1.55 * e_charge / HBAR / OMEGA_C  # w_pump/wC
    E0_over_Ec = E_pump / E_C

    # [WORKED-VAR]: freq-independent -> full engagement (Table I survives)
    W_var_yield = worked_content_W_analytic(E0_over_Ec, r_pump, False, C_W_YIELD, "var")
    W_var_clock = worked_content_W_analytic(E0_over_Ec, r_pump, False, C_W_CLOCK, "var")
    # [WORKED-BEAT]: freq-suppressed by (w/wC)^2 -> Table I collapses
    W_beat_yield = worked_content_W_analytic(E0_over_Ec, r_pump, False, C_W_YIELD, "beat")

    # dn_bir = -1/2 * (2*W)  since W_var = 1/2 (E/Ec)^2 and the Letter's dn=-1/2 A^2 with A^2=(E/Ec)^2
    # -> under WORKED-VAR/NORM-YIELD: 2*W_var = (E/Ec)^2 = A^2 -> dn = -1/2 A^2 (Table I UNCHANGED).
    dn_letter = -0.5 * A2_letter
    dn_var_yield = -0.5 * (2.0 * W_var_yield)   # = -1/2 A^2 (Table I unchanged; NORM-YIELD tautology)
    dn_var_clock = -0.5 * (2.0 * W_var_clock)   # x 1/(4pi)
    dn_beat_yield = -0.5 * (2.0 * W_beat_yield)  # x (w/wC)^2 -> collapse

    return {
        "E_pump": E_pump,
        "A2_letter": A2_letter,
        "w_pump_over_wC": r_pump,
        "beat_suppression_factor": r_pump**2,       # (w/wC)^2 ~ 9.2e-12
        "dn_bir_letter": dn_letter,
        "dn_bir_WORKED_VAR_yield": dn_var_yield,     # = dn_letter (Table I unchanged, tautological)
        "dn_bir_WORKED_VAR_clock": dn_var_clock,     # x 1/(4pi)
        "dn_bir_WORKED_BEAT_yield": dn_beat_yield,   # x (w/wC)^2 -> ~10^11 x below the Letter
        "Pflip_rescale_VAR_yield": (dn_var_yield / dn_letter) ** 2,   # 1.0 (tautology)
        "Pflip_rescale_BEAT_yield": (dn_beat_yield / dn_letter) ** 2,  # (w/wC)^4 collapse
        "probe_dispersion": _probe_energy_dispersion(),
    }


def _probe_energy_dispersion():
    probes_eV = {"dark-field": 8766.0, "conventional": 9835.0, "high-energy": 12914.0}
    out = {}
    for name, E_eV in probes_eV.items():
        q = E_eV * e_charge / (HBAR * C_0)
        out[name] = {"E_eV": E_eV, "qell_node_sq": (q * L_NODE) ** 2}
    return out


# ================================================= CONSTRAINT 3/4: PVLAS / BMV (S_B dual, Route C)
def S_B_functional(A_I):
    return float(np.sqrt(np.clip(1.0 - A_I**2, 0.0, 1.0)))


def A_I_from_dBdt(dBdt):
    """Route C: induced vacuum circulation per node clock period from Faraday (COMPUTED, not
    declared). Static B -> dBdt=0 -> A_I=0 -> S_B=1 (transparent). This is the B-side WORKED
    consistency: the mu-inductor is worked only by dB/dt (a static B is not worked)."""
    ell = L_NODE
    T_C = 2 * np.pi / OMEGA_C
    dPhi = dBdt * ell**2 * T_C
    I_induced = dPhi / (MU_0 * ell)
    return abs(I_induced) / I_MAX


def constraint_3_4_magnetic():
    B_pvlas, f_pvlas = 2.5, 10.0
    dBdt_pvlas = 2 * np.pi * f_pvlas * B_pvlas
    A_I_pvlas = A_I_from_dBdt(dBdt_pvlas)
    dn_pvlas = np.sqrt(S_B_functional(A_I_pvlas)) - 1.0
    B_bmv, tau_bmv = 6.0, 1e-3
    dBdt_bmv = B_bmv / tau_bmv
    A_I_bmv = A_I_from_dBdt(dBdt_bmv)
    dn_bmv = np.sqrt(S_B_functional(A_I_bmv)) - 1.0
    return {
        "pvlas_A_I": A_I_pvlas, "pvlas_dn_mu": dn_pvlas,
        "bmv_A_I": A_I_bmv, "bmv_dn_mu": dn_bmv,
    }


# ==================================================== CONSTRAINT 5: DELLIGHT (worked, propagating)
def constraint_5_dellight():
    I_dellight = 1e19 * 1e4
    E_dl = np.sqrt(2.0 * I_dellight / (C_0 * EPSILON_0))
    A2 = (E_dl / E_C) ** 2
    r_dl = 1.55 * e_charge / HBAR / OMEGA_C  # optical pump band
    W_var = worked_content_W_analytic(E_dl / E_C, r_dl, False, C_W_YIELD, "var")
    dn_iso_letter = -0.25 * A2
    dn_iso_var = -0.25 * (2.0 * W_var)  # = -1/4 A^2 (WORKED-VAR/NORM-YIELD, tautological)
    return {"A2": A2, "dn_iso_letter": dn_iso_letter, "dn_iso_WORKED_VAR": dn_iso_var}


# ==================================================== CONSTRAINT 6: BOOST (lattice-frame-anchored)
def constraint_6_boost():
    """A boosted UNIFORM static field is CONSTANT at a lattice cell -> Var_t(E) = 0 -> W = 0 ->
    BLIND, lattice-frame-anchored FOR FREE. State plainly as the frame's role, NOT covariance:
    the functional is lattice-frame-anchored (the theory's declared preferred frame); a boosted
    observer sees transformed observables, the vacuum response does not re-key. The round-1 CRITICAL-2
    aliasing story is MOOT (no aliasing needed): a uniform static field, boosted, is still uniform
    and static AT A LATTICE CELL -> nothing at the cell varies in time -> not worked."""
    v = 370e3
    B = 2.5
    E_from_B = v * B  # motional E from boosting a static B (uniform, static at a lattice cell)
    # the boosted config is a UNIFORM STATIC field at a lattice cell: constant time-series -> Var=0
    E_series = np.full(64, float(E_from_B))  # constant in time at the (lattice-frame) cell
    W_boosted = worked_content_W(E_series, dt=1.0, mode="var")
    return {
        "motional_E_from_static_B": E_from_B,
        "A2_from_boosted_B": (E_from_B / E_C) ** 2,
        "W_boosted": W_boosted,  # == 0 -> BLIND (constant at a lattice cell, not worked)
        "verdict": "BLIND (lattice-frame-anchored)",
        "note": "uniform static field, boosted, is still constant at a lattice cell -> Var_t=0 -> "
                "not worked. Lattice-frame-anchored by the declared preferred frame (NOT a covariance "
                "claim); the round-1 aliasing story is moot.",
    }


# ============================================= CONSTRAINT 7 [NEW]: slow-drive / quasi-static boundary
def constraint_7_slow_drive():
    """The quasi-static boundary of 'worked' -- a declared OPEN SCALE, not a free parameter.

    W_var is frequency-independent for w << wC (below the cell resonance). But 'worked' requires the
    field to VARY IN TIME at the cell; a field re-aimed over seconds (w ~ 1 rad/s, w/wC ~ 1e-21) is
    still time-varying at the cell, so W_var engages -- the freq-independence extends to ARBITRARILY
    slow AC in principle. What breaks it: (i) at TRUE DC (w=0 exactly, a permanently held field) W=0
    (blind); (ii) near resonance (w -> wC) the quasi-static tank approximation fails and the response
    is resonantly enhanced. Between DC and optical the vacuum WORKED-E response is UNCONSTRAINED by
    any experiment: PVLAS/BMV probe the B-side (static-B, R3, transparent); HIBEF probes the optical
    pump (R2/worked); the muon probes true-static-E (DC, R2 held). The MIDDLE E-band (RF/THz
    time-varying E, sub-optical) has NO facility bound. State this plainly: an OPEN SCALE.
    """
    anchors = {
        "muon static-E (DC, w=0)": {"w_over_wC": 0.0, "constrains": "true-DC E; W=0 blind (this arc)"},
        "PVLAS static-B (R3)": {"w_over_wC": 8e-20, "constrains": "B-side static; transparent (Route C)"},
        "HIBEF optical pump": {"w_over_wC": 3.03e-6, "constrains": "optical worked-E (pump, engaged)"},
    }
    # the UNCONSTRAINED middle band: sub-optical time-varying E (RF ~ 1e9 Hz -> THz ~ 1e12 Hz)
    middle_band = {
        "RF (1 GHz)": 2 * np.pi * 1e9 / OMEGA_C,
        "THz (1 THz)": 2 * np.pi * 1e12 / OMEGA_C,
        "IR (10 THz)": 2 * np.pi * 1e13 / OMEGA_C,
    }
    return {
        "known_anchors": anchors,
        "unconstrained_middle_band_w_over_wC": middle_band,
        "verdict": "OPEN SCALE",
        "note": "the sub-optical time-varying-E band (RF/THz, w/wC ~ 1e-11 to 1e-8) has NO facility "
                "bound. W_var is freq-independent in principle for any w<<wC, so 'worked' engages any "
                "nonzero AC; the untested middle band is a DECLARED OPEN SCALE (not a free parameter): "
                "if a future facility drives a time-varying E in this band and reads NO birefringence, "
                "that would falsify the freq-independence. Named candidates: high-rep-rate RF/THz "
                "vacuum-birefringence with an AC (not DC) E drive.",
    }


def main():
    print("=" * 78)
    print("SEVEN FROZEN CONSTRAINT FALSIFIERS — WORKED functional (evaluated as-derived)")
    print("=" * 78)

    print("\n[1] MUONIC-H (physical, STATIC-IN-TIME atom -- reuses #539 machinery)")
    print("    (A) under the SELECTED variance keying (W_var: static-in-time -> W=0):")
    c1 = constraint_1_muonic()
    print("    WORKED content W_var on the physical (static-in-time) atom fields:")
    for k, v in c1["W_physical_at"].items():
        print(f"      W_var({k}) = {v:.3e}  (static in TIME -> Var_t(E)=0 -> BLIND, no net-vs-local needed)")
    for k, v in c1["shifts_ueV_by_rcut"].items():
        print(f"      r_cut={k}: shift = {v:+.3e} ueV")
    print(f"    worst |shift| = {c1['worst_abs_shift_ueV']:.3e} ueV  window={c1['window_ueV']} ueV")
    print(f"    PASSES (< window)? = {c1['passes']}  -> the round-1 killer dissolves UNDER W_var")
    print(f"    NULL-LIVENESS: same pipeline, TIME-VARYING drive -> shift = {c1['liveness_worked_shift_ueV']:.3e} ueV"
          f" (!=0 -> the zero is physics, not bookkeeping)")
    print("    (B) COUNTERFACTUAL under the ledger-forced MEAN-SQUARE key (DC-included; §crux):")
    c1ms = constraint_1_muonic_meansquare_counterfactual()
    for k, v in c1ms["shifts_ueV_by_rcut"].items():
        print(f"      r_cut={k}: shift = {v:+.3e} ueV")
    print(f"    shift @1a_mu = {c1ms['shift_at_1a_ueV']:+.3e} ueV  overshoot x{c1ms['overshoot_factor_at_1a']:.2e}")
    print(f"    RE-KILLS (> window)? = {c1ms['re_kills']}  -> the DC-included E-key overshoots CREMA")
    print("      ~4 OOM, reproducing #539 [C-EXCLUDED] (CONSISTENCY check, not a falsifier of W_var)")

    print("\n[2] THE PUMP (worked at pump omega) -- BOTH sub-bins, BOTH norm arms")
    c2 = constraint_2_pump()
    print(f"    E_pump={c2['E_pump']:.3e} V/m  A^2(Letter)={c2['A2_letter']:.3e}  w_pump/wC={c2['w_pump_over_wC']:.3e}")
    print(f"    [WORKED-VAR/NORM-YIELD] dn_bir = {c2['dn_bir_WORKED_VAR_yield']:.3e}  (= Letter {c2['dn_bir_letter']:.3e},"
          f" Table I UNCHANGED -- NORM-YIELD tautology, P_flip x {c2['Pflip_rescale_VAR_yield']:.3f})")
    print(f"    [WORKED-VAR/NORM-CLOCK] dn_bir = {c2['dn_bir_WORKED_VAR_clock']:.3e}  (x 1/(4pi))")
    print(f"    [WORKED-BEAT/NORM-YIELD] dn_bir = {c2['dn_bir_WORKED_BEAT_yield']:.3e}  (x (w/wC)^2="
          f"{c2['beat_suppression_factor']:.2e} -> ~10^11 BELOW Letter; Table I COLLAPSES)")
    print("    -> the VAR-vs-BEAT fork gives OPPOSITE Table-I fates; decided by STEP 1 (VAR forced)")

    print("\n[3/4] PVLAS / BMV (S_B Route-C dual, computed A_I)")
    c34 = constraint_3_4_magnetic()
    print(f"    PVLAS A_I(computed)={c34['pvlas_A_I']:.2e}  dn_mu={c34['pvlas_dn_mu']:.2e}")
    print(f"    BMV   A_I(computed)={c34['bmv_A_I']:.2e}  dn_mu={c34['bmv_dn_mu']:.2e}")

    print("\n[5] DELLIGHT (worked, propagating pump)")
    c5 = constraint_5_dellight()
    print(f"    A^2={c5['A2']:.3e}  dn_iso(WORKED-VAR/NORM-YIELD)={c5['dn_iso_WORKED_VAR']:.3e}"
          f"  (= Letter {c5['dn_iso_letter']:.3e}, tautological -- fork open)")

    print("\n[6] BOOST (lattice-frame-anchored, NOT covariance)")
    c6 = constraint_6_boost()
    print(f"    motional E={c6['motional_E_from_static_B']:.3e} V/m  W_boosted={c6['W_boosted']:.3e}  -> {c6['verdict']}")
    print(f"    {c6['note']}")

    print("\n[7] SLOW-DRIVE / QUASI-STATIC BOUNDARY (NEW) -- declared OPEN SCALE")
    c7 = constraint_7_slow_drive()
    print(f"    known anchors: {list(c7['known_anchors'].keys())}")
    print(f"    UNCONSTRAINED middle band (w/wC): "
          + ", ".join(f"{k}={v:.2e}" for k, v in c7['unconstrained_middle_band_w_over_wC'].items()))
    print(f"    VERDICT: {c7['verdict']} -- {c7['note']}")

    return c1, c1ms, c2, c34, c5, c6, c7


if __name__ == "__main__":
    main()
