#!/usr/bin/env python3
"""EM-sector saturation keying — the SIX FROZEN CONSTRAINT FALSIFIERS.

FROZEN prereg: research/2026-07-05_em-saturation-keying-functional_prereg_FROZEN.md
Freeze commit gated on: bfd897c5.

Evaluates the DERIVED transport functional S_E (T-POYNT, piece b) and its dual
S_B (Route C) against the six frozen constraints. NO parameter is chosen to
satisfy any constraint; the derived functional is evaluated as-derived.

  1. MUONIC-H  -- reuse the #539 evaluator machinery (import, not reimplement);
                  the static Coulomb field has H=0 -> T_POYNT=0 -> delta[DeltaE]=0
                  EXACTLY. LIVE positive control: the pump field pushed through the
                  IDENTICAL S_E->shift pipeline goes NONZERO (null-verdict-liveness).
  2. THE PUMP  -- S_E at the Letter's pump: recover A^2=5.9e-7, dn_bir coefficient.
  3. PVLAS     -- S_B rotating 2.5 T Hz-scale: I_circ=0 -> dn_mu=0 (Route C).
  4. BMV       -- S_B ms pulses large dB/dt.
  5. DELLIGHT  -- S_E common-mode dn_iso at Sagnac sensitivity.
  6. BOOST     -- static E <-> static B zero-sequence (both blind); transport keyed.
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

# import the #539 muonic-H machinery (reuse, do not reimplement)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import problem3_muonic_lamb_shift as p3  # noqa: E402

# The muonic bracket integrals over the 1/r^2 Coulomb field are slowly convergent
# near r->0 (a KNOWN, benign feature also present in the #539 evaluator); the
# positive-control liveness probe deliberately uses a divergent-tail field. Silence
# only these convergence warnings so the routed output is readable; the numeric
# results are cross-checked by the T=0 short-circuit and the ReconcileGate.
warnings.filterwarnings("ignore", category=IntegrationWarning)

E_C = E_YIELD
I_MAX = XI_TOPO * C_0  # 124.384 A (Route C)
J_TO_ueV = 1.0 / e_charge * 1e6


# ============================================================ the DERIVED S_E
# TRANSPORT-NORMALIZATION FORK — FULLY OPEN (MAJOR-b). The COEFFICIENT linking the
# transport engagement to (E/E_c)^2 depends on the node-power normalization, and two
# choices give different coefficients:
#   NORM-YIELD  : normalize Poynting against the yield-field Poynting flux
#                 S_yield = c eps0 E_c^2 = E_c^2/Z0. Then T = (E/E_c)^2, P_flip x 1.
#   NORM-CLOCK  : normalize Poynting against rest-energy-per-clock P_C=mc2 wC
#                 through a cell face ell^2. Then T = (1/4pi)(E/E_c)^2, P_flip x (1/4pi)^2.
# HONEST (MAJOR-b): NORM-YIELD's 'Table I unchanged' is a TAUTOLOGY of the
# normalization definition -- NORM-YIELD is DEFINED as the flux that reaches 1 at
# E=E_c, so it trivially reproduces the Letter's calibration; that self-consistency is
# NOT a substrate reason to prefer it (the verifier ruled the argument a near-tautology).
# The 'substrate-consistent reading' crowning is STRIPPED. The norm fork is FULLY OPEN;
# neither coefficient is substrate-forced. (Reported for completeness; the LOCAL form is
# CONSTRAINT-KILLED regardless of coefficient -- constraint 1 fails on the physical atom
# for any normalization, since the near-nucleus overshoot is 10^3 x, far beyond 4pi.)
TRANSPORT_COEFF_YIELD = 1.0  # NORM-YIELD: T = (E/Ec)^2 (tautological Table-I match)
TRANSPORT_COEFF_CLOCK = 1.0 / (4.0 * np.pi)  # NORM-CLOCK: T = (1/4pi)(E/Ec)^2


def transport_engagement_T(E_field, H_field, coeff=TRANSPORT_COEFF_YIELD):
    """T-POYNT engagement (dimensionless), gated by transport presence.

    T = coeff * (E/Ec)^2 * [H/(E/Z0)]. The bracket [H/(E/Z0)] is the co-moving
    fraction: 1 for a co-moving wave (H=E/Z0), 0 for held stock (H=0). So held
    stock (Coulomb, H=0) -> T=0 (DC-blind), a wave -> T = coeff*(E/Ec)^2. The
    default coeff=NORM-YIELD (Table I unchanged); pass TRANSPORT_COEFF_CLOCK for
    the alternate normalization.
    """
    E = np.asarray(E_field, dtype=float)
    H = np.asarray(H_field, dtype=float)
    wave_H = E / Z_0  # co-moving wave value
    with np.errstate(divide="ignore", invalid="ignore"):
        comoving = np.where(np.abs(wave_H) > 0, H / wave_H, 0.0)
    return coeff * (E / E_C) ** 2 * comoving


# ---------------------------------------------------------- physical atomic H(r)
# CRITICAL-1 (orchestrator review PR #542): the real muonic atom is NOT
# transport-dead. The muon's Coulomb field E(r)=K/r^2 co-exists with a PERMANENT
# STATIC magnetic field from (i) the proton magnetic dipole moment and (ii) the
# 2P orbital current. These create a permanent static E x H circulation
# (hidden-momentum class): divergence-free (net closed-surface flux = 0), but
# LOCALLY nonzero. The boxed functional keys on LOCAL pointwise E x H ("power flux
# through a cell face") and CANNOT distinguish divergence-free circulation from
# net transport. So H != 0 in the physical atom -> the functional engages and
# FAILS. The H=0 fiat of the original constraint 1 was an ARTIFACT.
MU_N = e_charge * HBAR / (2.0 * M_PROTON)  # nuclear magneton (m_p from constants.py)
MU_P = 2.7928473446 * MU_N  # proton magnetic moment (CODATA 2018, EXTERNAL)


def H_atomic(r):
    """Physical static H(r) co-existing with the muon Coulomb field.

    Dominant near-nucleus channel: the proton magnetic dipole field
    |B_dip(r)| ~ mu0 mu_p / (4 pi r^3) (characteristic on-axis magnitude). H=B/mu0.
    This is a divergence-free static field (net transport zero) but locally nonzero
    -- exactly the hidden-momentum circulation the local-Poynting functional cannot
    tell apart from net flux.
    """
    r = np.asarray(r, dtype=float)
    B = MU_0 * MU_P / (4.0 * np.pi * r**3)
    return B / MU_0


# ============================================== CONSTRAINT 1: MUONIC-H (physical H)
def constraint_1_muonic(r_cut_factors=(0.5, 1.0, 2.0)):
    """PHYSICAL muonic-H atom evaluation of the boxed LOCAL-Poynting functional.

    CRITICAL-1 fix: evaluate on the PHYSICAL atomic H(r) (proton dipole channel),
    NOT the H=0 fiat. The local-Poynting engagement T(r) = (E/Ec)^2 * H/(E/Z0) is
    nonzero everywhere the physical H is nonzero. Fed through the #539 bracket-
    integral (rho_2s, rho_2p, _norm, A_MU), the boxed functional produces a level
    shift that EXCEEDS the CREMA window by 10^0-10^4 x -- the functional FAILS its
    own headline constraint on the physical atom. The r^-3 dipole field diverges at
    the nucleus, so we report the shift vs a family of inner cutoffs r_cut = f*a_mu
    (the near-nucleus region cannot rescue: even deleting everything inside 2 a_mu
    leaves several x the window). This is the [CONSTRAINT-KILLED] result.

    (LIVENESS is now moot: the physical H already makes the shift nonzero. We keep a
    reduced bounded-perturbation probe ONLY as a pipeline sanity check, correctly
    LABELED as such -- not as a null-verdict-liveness proof of a passing zero, which
    no longer exists.)
    """
    from scipy import integrate

    a = p3.A_MU
    r_hi = 60.0 * a
    N2s = p3._norm(p3.rho_2s)
    N2p = p3._norm(p3.rho_2p)

    def dV_field_excess(r, r_cut):
        """Field excess (E_true - E_C) from S_E on the PHYSICAL local Poynting."""
        E_C_r = p3.K / r**2
        if r < r_cut:
            return 0.0  # inner cutoff: exclude the r^-3 dipole divergence
        T = float(transport_engagement_T(E_C_r, H_atomic(r)))
        S = np.sqrt(np.clip(1.0 - T, 1e-12, 1.0))
        return E_C_r / S - E_C_r

    def shift_ueV(r_cut):
        def dV_of_r(r):
            val, _ = integrate.quad(lambda rp: dV_field_excess(rp, r_cut), r, r_hi,
                                    limit=150)
            return -val
        def bracket(rho, norm):
            val, _ = integrate.quad(
                lambda r: e_charge * dV_of_r(r) * rho(r) / norm, r_cut, r_hi, limit=100)
            return val
        return (bracket(p3.rho_2s, N2s) - bracket(p3.rho_2p, N2p)) * J_TO_ueV

    # engagement at a few radii (shows the physical H makes T != 0 everywhere)
    T_at = {f"{f:g}a": float(transport_engagement_T(p3.K / (f * a) ** 2, H_atomic(f * a)))
            for f in (0.1, 0.5, 1.0, 2.0)}
    shifts = {f: shift_ueV(f * a) for f in r_cut_factors}
    worst = max(abs(v) for v in shifts.values())

    # pipeline sanity probe (NOT a liveness proof of a passing zero -- there is no
    # passing zero anymore): a small bounded T confirms the bracket integral is live.
    EPS = 1e-3

    def dV_probe(r):
        E_C_r = p3.K / r**2
        T = EPS * np.exp(-r / a)
        S = np.sqrt(np.clip(1.0 - T, 1e-6, 1.0))
        return E_C_r / S - E_C_r

    def bracket_probe(rho, norm):
        def dV_of_r(r):
            val, _ = integrate.quad(dV_probe, r, r_hi, limit=200)
            return -val
        val, _ = integrate.quad(
            lambda r: e_charge * dV_of_r(r) * rho(r) / norm, 1e-3 * a, r_hi, limit=120)
        return val

    probe_ueV = (bracket_probe(p3.rho_2s, N2s) - bracket_probe(p3.rho_2p, N2p)) * J_TO_ueV

    return {
        "T_physical_at": T_at,
        "shifts_ueV_by_rcut": {f"{f:g}a_mu": shifts[f] for f in r_cut_factors},
        "worst_abs_shift_ueV": worst,
        "window_ueV": p3.WINDOW_ueV_primary,
        "overshoot_factor": worst / p3.WINDOW_ueV_primary,
        "passes": worst < p3.WINDOW_ueV_primary,  # FALSE -> [CONSTRAINT-KILLED]
        "pipeline_probe_ueV": probe_ueV,  # bounded-probe sanity (labeled, not liveness)
    }


# ================================================ CONSTRAINT 2: THE PUMP (Table I)
def constraint_2_pump():
    """S_E at the Letter's demonstrated pump. Recover A^2 and the dn_bir coefficient.

    The pump is a PROPAGATING optical wave: H = E/Z0 co-moving -> T-POYNT engaged.
    The transport engagement T = (1/4pi)(E/Ec)^2. The Letter uses A^2=(E/Ec)^2 with
    coefficient -1/2 for dn_bir. Report the DERIVED coefficient vs the Letter's.
    """
    I_pump = 1e21 * 1e4  # W/cm^2 -> W/m^2
    E_pump = np.sqrt(2.0 * I_pump / (C_0 * EPSILON_0))  # peak carrier amplitude
    A2_letter = (E_pump / E_C) ** 2
    H_pump = E_pump / Z_0  # co-moving wave -> transport ENGAGED
    T_yield = float(transport_engagement_T(E_pump, H_pump, TRANSPORT_COEFF_YIELD))
    T_clock = float(transport_engagement_T(E_pump, H_pump, TRANSPORT_COEFF_CLOCK))
    dn_letter = -0.5 * A2_letter
    dn_yield = -0.5 * T_yield  # NORM-YIELD: = -1/2 A^2 -> Table I UNCHANGED
    dn_clock = -0.5 * T_clock  # NORM-CLOCK: = -1/2 (1/4pi) A^2 -> Table I x 1/(4pi)
    # P_flip ~ dn^2 (small-angle), so the Table-I rescale on P_flip is (coeff)^2
    return {
        "E_pump": E_pump,
        "A2_letter": A2_letter,
        "T_yield": T_yield,
        "T_clock": T_clock,
        "dn_bir_letter": dn_letter,
        "dn_bir_yield": dn_yield,
        "dn_bir_clock": dn_clock,
        "Pflip_rescale_yield": (dn_yield / dn_letter) ** 2 if dn_letter else float("nan"),
        "Pflip_rescale_clock": (dn_clock / dn_letter) ** 2 if dn_letter else float("nan"),
        "probe_dispersion": _probe_energy_dispersion(),
    }


def _probe_energy_dispersion():
    """Energy-dependence across the three probe energies (Keith's predicted structure).

    The transport engagement itself is set by the PUMP (1.55 eV), common to all
    probes -> the leading coefficient is probe-energy-INDEPENDENT (the Letter's
    DC-Kerr assumption). The probe-energy dependence enters at NEXT order as the
    scalar (qell_node)^2 lattice-cutoff correction (fork-memo [B] FORM, the
    ISOTROPIC scalar channel, NOT the clm-k4d4ph anisotropic quartic). Compute the
    fractional coefficient shift (q_probe ell_node)^2 for each probe; the higher-
    energy probe carries a larger fractional correction, over-determined by
    ell_node alone -- a distinct forward prediction.
    """
    probes_eV = {"dark-field": 8766.0, "conventional": 9835.0, "high-energy": 12914.0}
    out = {}
    for name, E_eV in probes_eV.items():
        q = E_eV * e_charge / (HBAR * C_0)  # probe momentum q = E/(hbar c) [1/m]
        qell2 = (q * L_NODE) ** 2
        out[name] = {"E_eV": E_eV, "q": q, "qell_node_sq": qell2}
    return out


def S_B_functional(A_I):
    """The DUAL magnetic functional S_B = sqrt(1 - A_I^2) (Route C inductor)."""
    return float(np.sqrt(np.clip(1.0 - A_I**2, 0.0, 1.0)))


def A_I_from_dBdt(dBdt, omega, contour=None):
    """COMPUTE A_I = I_induced/I_max for a slowly-varying B (Faraday), not declare it.

    Route C: a changing flux induces a vacuum circulation I_induced. Over one node
    contour of scale ell_node and one node clock period, the induced EMF ~ dPhi/dt =
    dBdt * ell_node^2; the induced circulation as a fraction of I_max scales with
    (omega/omega_C) (the rate the vacuum can respond within its clock). We build A_I
    from the physical dBdt and evaluate S_B on it -- so the near-zero is COMPUTED from
    the functional, not a hardcoded literal (MAJOR-d)."""
    ell = L_NODE
    if contour is None:
        contour = ell
    # induced flux change over one node clock period T_C = 2 pi/omega_C:
    T_C = 2 * np.pi / OMEGA_C
    dPhi = dBdt * ell**2 * T_C  # flux change in one clock period [T*m^2]
    # induced circulation ~ dPhi/(mu0 ell) mapped to I_max = xi_topo c:
    I_induced = dPhi / (MU_0 * ell)
    return abs(I_induced) / I_MAX


def constraint_3_4_magnetic():
    """S_B (Route C dual) EVALUATED on the physical PVLAS/BMV configs (MAJOR-d).

    dn_mu is COMPUTED from S_B(A_I) with A_I built from the physical dBdt -- NOT a
    hardcoded zero. PVLAS (2.5 T rotating ~Hz) and BMV (ms pulse, large dBdt) both
    give A_I -> ~0 because the induced vacuum circulation per node clock period is
    I_max-negligible, so dn_mu = sqrt(S_B)-1 -> ~0. Reported as the computed number.
    """
    # PVLAS: B=2.5 T, f_rot ~ 10 Hz
    B_pvlas, f_pvlas = 2.5, 10.0
    dBdt_pvlas = 2 * np.pi * f_pvlas * B_pvlas  # T/s
    w_pvlas = 2 * np.pi * f_pvlas
    A_I_pvlas = A_I_from_dBdt(dBdt_pvlas, w_pvlas)
    dn_pvlas = np.sqrt(S_B_functional(A_I_pvlas)) - 1.0  # COMPUTED from the functional
    # BMV: B~6 T, pulse ~ms
    B_bmv, tau_bmv = 6.0, 1e-3
    dBdt_bmv = B_bmv / tau_bmv  # T/s
    w_bmv = 2 * np.pi / tau_bmv
    A_I_bmv = A_I_from_dBdt(dBdt_bmv, w_bmv)
    dn_bmv = np.sqrt(S_B_functional(A_I_bmv)) - 1.0
    return {
        "pvlas_dBdt": dBdt_pvlas,
        "pvlas_omega_over_wC": w_pvlas / OMEGA_C,
        "pvlas_A_I": A_I_pvlas,
        "pvlas_dn_mu": dn_pvlas,  # COMPUTED, not declared
        "bmv_dBdt": dBdt_bmv,
        "bmv_omega_over_wC": w_bmv / OMEGA_C,
        "bmv_A_I": A_I_bmv,
        "bmv_dn_mu": dn_bmv,
    }


# ================================================= CONSTRAINT 5: DELLIGHT (S_E)
def constraint_5_dellight():
    """DeLLight common-mode dn_iso ~ -1/4 A^2 at their Sagnac pump.

    DeLLight uses a ~10^19 W/cm^2 focused pump (a PROPAGATING wave -> transport
    engaged). The common-mode index shift dn_iso = sqrt(S)-1 ~ -1/4 T (transport
    form) -> -1/4 (1/4pi) A^2. Report vs the Letter's -1/4 A^2.
    """
    I_dellight = 1e19 * 1e4  # W/cm^2 -> W/m^2 (order; DeLLight focal intensity)
    E_dl = np.sqrt(2.0 * I_dellight / (C_0 * EPSILON_0))
    A2 = (E_dl / E_C) ** 2
    H_dl = E_dl / Z_0  # propagating pump -> transport engaged
    T_yield = float(transport_engagement_T(E_dl, H_dl, TRANSPORT_COEFF_YIELD))
    dn_iso_letter = -0.25 * A2
    dn_iso_yield = -0.25 * T_yield  # = -1/4 A^2 (Table-I-consistent normalization)
    return {"E_dellight": E_dl, "A2": A2, "T_yield": T_yield,
            "dn_iso_letter": dn_iso_letter, "dn_iso_yield": dn_iso_yield}


# ==================================================== CONSTRAINT 6: BOOST
def constraint_6_boost():
    """BOOST-CONSISTENCY OPEN (CRITICAL-2 retraction). The aliasing story is REFUTED.

    The prereg/original result claimed the boosted-static configuration 'aliases to
    omega_C and averages out' (zero-sequence, blind). TWO of my OWN results refute it:

    (i) piece (a) shows a DC 2nd-order quantity SURVIVES clock-averaging: the static
        <E^2> secular content is 1.0 (NONZERO at omega=0). A boosted static field is
        also omega=0 (DC) in the lab frame, so by my own piece-(a) math its 2nd-order
        content does NOT average out. The 'aliases to omega_C' claim contradicts the
        secular-averaging result it rests on.
    (ii) the CODED functional gives T != 0 for the boosted config: a static B boosted
        gives a motional E, and the co-existing static B is a real H field, so the
        LOCAL E x H = motional_E x H_static is NONZERO. The functional the prose calls
        'blind' engages.

    So boost-consistency is NOT closed structurally. It is OPEN, and it requires the
    lattice-frame anchoring question resolved (the round-2 forward pointer: a NET-flux
    functional anchored in the LATTICE REST FRAME is frame-anchored by the theory's
    declared preferred frame -- a boosted observer sees transformed observables, not a
    re-keyed vacuum). This constraint is reported OPEN, not PASS.
    """
    v = 370e3
    B = 2.5  # PVLAS-scale static magnet
    E_from_B = v * B  # motional E from boosting static B
    H_static = B / MU_0  # the co-existing static B is a real H field
    # the LOCAL Poynting the CODED functional sees for the boosted config:
    T_boosted = float(transport_engagement_T(E_from_B, H_static, TRANSPORT_COEFF_YIELD))
    # piece-(a) static DC survival (the contradiction with the aliasing claim):
    static_E2_secular = 1.0  # from em_saturation_keying_secular (omega=0 -> <E^2>=1)
    return {
        "motional_E_from_static_B": E_from_B,
        "A2_from_boosted_B": (E_from_B / E_C) ** 2,
        "T_boosted_local_poynting": T_boosted,  # NONZERO -> prose 'blind' is FALSE
        "static_E2_secular_survives": static_E2_secular,  # NONZERO -> aliasing refuted
        "verdict": "OPEN",  # NOT closed; the aliasing mechanism is refuted
        "note": "aliasing REFUTED by piece-(a) DC survival + coded T!=0; boost-"
                "consistency OPEN, requires lattice-frame anchoring (round-2 pointer).",
    }


def main():
    print("=" * 74)
    print("SIX FROZEN CONSTRAINT FALSIFIERS (derived S_E, S_B evaluated as-derived)")
    print("=" * 74)

    print("\n[1] MUONIC-H (PHYSICAL atomic H(r) -- reuses #539 machinery)")
    c1 = constraint_1_muonic()
    print("    LOCAL Poynting engagement T on the PHYSICAL H(r) (proton dipole):")
    for k, v in c1["T_physical_at"].items():
        print(f"      T({k}) = {v:.3e}  (the H=0 fiat wrongly gave 0)")
    print("    level shift vs inner cutoff r_cut:")
    for k, v in c1["shifts_ueV_by_rcut"].items():
        print(f"      r_cut={k}: shift = {v:+.3e} ueV")
    print(f"    worst |shift| = {c1['worst_abs_shift_ueV']:.3e} ueV  window={c1['window_ueV']} ueV"
          f"  -> {c1['overshoot_factor']:.1f}x")
    print(f"    PASS (< window)? = {c1['passes']}  -> [CONSTRAINT-KILLED]")
    print(f"    (pipeline sanity probe, bounded T=1e-3: {c1['pipeline_probe_ueV']:.3e} ueV"
          f" -- labeled, NOT a liveness proof of a passing zero)")

    print("\n[2] THE PUMP (propagating wave, transport engaged) — NORM FORK FULLY OPEN")
    c2 = constraint_2_pump()
    print(f"    E_pump = {c2['E_pump']:.3e} V/m (PEAK carrier)  A^2(Letter) = {c2['A2_letter']:.3e}")
    print(f"    T (NORM-YIELD) = {c2['T_yield']:.3e} = (E/Ec)^2  -> dn_bir = {c2['dn_bir_yield']:.3e}")
    print(f"       vs Letter dn_bir = {c2['dn_bir_letter']:.3e}  -> P_flip rescale = "
          f"{c2['Pflip_rescale_yield']:.3f} (TAUTOLOGICAL: NORM-YIELD is DEFINED to match)")
    print(f"    T (NORM-CLOCK) = {c2['T_clock']:.3e} = (1/4pi)(E/Ec)^2 -> dn_bir = {c2['dn_bir_clock']:.3e}")
    print(f"       -> P_flip rescale = {c2['Pflip_rescale_clock']:.4e} (Table I x 1/(4pi)^2)")
    print("    (MINOR: A^2 uses the PEAK carrier E; the Letter's headline coeff is the")
    print("     cycle-AVERAGED <cos^2>=1/2 value -- a factor 2 lives in that convention.)")
    print("    NORM FORK FULLY OPEN: neither coefficient is substrate-forced.")
    print("    probe-energy dispersion (scalar (q ell_node)^2 fork-memo [B] FORM):")
    for name, d in c2["probe_dispersion"].items():
        print(f"      {name:13s} E={d['E_eV']:.0f} eV  (q ell_node)^2 = {d['qell_node_sq']:.3e}")

    print("\n[3/4] PVLAS / BMV (S_B dual EVALUATED on the physical config, not declared)")
    c34 = constraint_3_4_magnetic()
    print(f"    PVLAS  dB/dt={c34['pvlas_dBdt']:.2e} T/s  A_I(computed)={c34['pvlas_A_I']:.2e}"
          f"  dn_mu={c34['pvlas_dn_mu']:.2e}")
    print(f"    BMV    dB/dt={c34['bmv_dBdt']:.2e} T/s  A_I(computed)={c34['bmv_A_I']:.2e}"
          f"  dn_mu={c34['bmv_dn_mu']:.2e}")
    print("    (dn_mu COMPUTED from S_B(A_I), A_I from the physical dBdt via Faraday -- MAJOR-d)")

    print("\n[5] DELLIGHT (common-mode, propagating pump -> transport engaged)")
    c5 = constraint_5_dellight()
    print(f"    E_dl={c5['E_dellight']:.3e} V/m  A^2={c5['A2']:.3e}  T(NORM-YIELD)={c5['T_yield']:.3e}")
    print(f"    dn_iso Letter={c5['dn_iso_letter']:.3e}  transport(NORM-YIELD)={c5['dn_iso_yield']:.3e}"
          f"  (= -1/4 A^2 under NORM-YIELD, which is tautological -- fork open)")

    print("\n[6] BOOST — OPEN (aliasing REFUTED, CRITICAL-2)")
    c6 = constraint_6_boost()
    print(f"    motional E from static B = {c6['motional_E_from_static_B']:.3e} V/m"
          f"  A^2={c6['A2_from_boosted_B']:.3e}")
    print(f"    coded functional T on boosted config = {c6['T_boosted_local_poynting']:.3e}"
          f"  (NONZERO -> prose 'blind' is FALSE)")
    print(f"    piece-(a) static <E^2> secular = {c6['static_E2_secular_survives']:.1f}"
          f"  (NONZERO DC survives clock avg -> aliasing story refuted)")
    print(f"    VERDICT: {c6['verdict']} -- {c6['note']}")

    return c1, c2, c34, c5, c6


if __name__ == "__main__":
    main()
