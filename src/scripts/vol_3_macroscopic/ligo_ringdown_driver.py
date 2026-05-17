"""LIGO Ringdown Driver — Phase 1: Computational verification of AVE prediction.

Independently computes the AVE merger-ringdown eigenvalue $\\omega_R M_g = 18/49$
plus Kerr correction for each of three canonical LIGO O1-O2 events, then compares
against the KB-cited table at
`manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md`
lines 44-48.

Tests AVE matrix row C1-BH-RING in
`manuscript/ave-kb/common/divergence-test-substrate-map.md`.

Phase 1 (this file): numpy-only, verifies formula self-consistency against KB table.
Phase 2 (next session): PyCBC/GWpy raw-strain ringdown fit for independent f_obs extraction.

Run:
    python3 src/scripts/vol_3_macroscopic/ligo_ringdown_driver.py
"""
from __future__ import annotations

import math
from dataclasses import dataclass

# AVE-canonical constants (cold lattice).
NU_VAC = 2 / 7  # vacuum Poisson ratio (INVARIANT canonical, Vol 3 Ch 1)
X_SAT = 7  # r_sat / M_g (Axiom 4: epsilon_11(r_sat) = 1)
ELL_MODE = 2  # quadrupole mode (LIGO ringdown observed mode)

# Cold-AVE Schwarzschild eigenvalue: omega_R * M_g = ell * (1 + nu_vac) / x_sat
OMEGA_R_M_G_COLD = ELL_MODE * (1 + NU_VAC) / X_SAT  # = 18/49
# GR exact Schwarzschild ell=2, n=0 QNM eigenvalue (Leaver 1985)
OMEGA_R_M_G_GR = 0.3737

# Physical constants
G_SI = 6.674e-11  # m^3 / (kg s^2)
C_SI = 2.998e8  # m/s
M_SUN_KG = 1.989e30  # kg

# Conversion: M (in solar masses) -> M (in seconds) via M_seconds = G*M / c^3
T_SUN = G_SI * M_SUN_KG / (C_SI ** 3)  # ~ 4.92e-6 s/M_sun


@dataclass
class LigoEvent:
    """Final-state mass + spin for a LIGO binary BH merger event."""

    name: str
    m_final_msun: float
    a_star: float
    f_kb_ave_hz: float  # KB-cited AVE prediction
    f_kb_obs_hz: float  # KB-cited LIGO-collaboration observed
    tau_kb_ave_ms: float
    tau_kb_obs_ms: float


# Canonical 3-event table from
# manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md:44-48
LIGO_EVENTS = [
    LigoEvent("GW150914", 62.0, 0.67, 278.0, 251.0, 3.5, 4.0),
    LigoEvent("GW170104", 48.7, 0.64, 345.0, 312.0, 2.7, 3.0),
    LigoEvent("GW151226", 20.8, 0.74, 884.0, 750.0, 1.2, 1.4),
]


def ave_cold_f_ring_hz(m_final_msun: float) -> float:
    """Cold AVE Schwarzschild ringdown frequency (zero spin) for given final mass.

    omega_R * M_g = 18/49 (dimensionless, geometric units)
    -> omega_R = (18/49) / M_g(seconds) = (18/49) / (T_SUN * M_msun)
    -> f_ring = omega_R / (2 pi)
    """
    m_g_seconds = T_SUN * m_final_msun
    omega_r = OMEGA_R_M_G_COLD / m_g_seconds
    return omega_r / (2 * math.pi)


def kerr_correction_factor(a_star: float) -> float:
    """Kerr correction shrinking the cavity radius for spinning remnant.

    f_ring(a*) = f_ring(0) * r_ph,Schw / r_ph^+(a*)
    r_ph^+ = (2GM/c^2)(1 + cos[(2/3) arccos(-a*)])
    r_ph,Schw = 3GM/c^2

    Per ave-merger-ringdown-eigenvalue.md "Kerr-Corrected Ringdown" section.
    """
    if not -1 <= a_star <= 1:
        raise ValueError(f"a_star must be in [-1, 1], got {a_star}")
    r_ph_plus_over_2gm = 1 + math.cos((2 / 3) * math.acos(-a_star))
    r_ph_plus = 2 * r_ph_plus_over_2gm  # in units of GM/c^2
    r_ph_schw = 3  # in units of GM/c^2
    return r_ph_schw / r_ph_plus


def ave_kerr_f_ring_hz(m_final_msun: float, a_star: float) -> float:
    """Kerr-corrected AVE ringdown frequency."""
    return ave_cold_f_ring_hz(m_final_msun) * kerr_correction_factor(a_star)


def gr_f_ring_hz(m_final_msun: float, a_star: float) -> float:
    """GR exact Schwarzschild ringdown (cold), Kerr-corrected with same formula.

    Note: AVE uses the same Kerr-correction formula; the AVE-vs-GR difference is
    in the cold eigenvalue only (18/49 vs 0.3737).
    """
    m_g_seconds = T_SUN * m_final_msun
    omega_r_cold = OMEGA_R_M_G_GR / m_g_seconds
    f_cold = omega_r_cold / (2 * math.pi)
    return f_cold * kerr_correction_factor(a_star)


def verify_kb_table() -> int:
    """Verify each event in LIGO_EVENTS against KB-cited values.

    Returns:
        Number of events where computed value disagrees with KB value by > 1%.
    """
    print("\n" + "=" * 92)
    print("AVE Ringdown Prediction — Computational Verification")
    print("Phase 1: independently compute AVE prediction from formula + Kerr correction,")
    print("         compare against KB-cited table to verify self-consistency.")
    print("=" * 92)
    print(
        f"\nAVE cold eigenvalue: omega_R * M_g = ell*(1+nu_vac)/x_sat = "
        f"{ELL_MODE}*(1+{NU_VAC:.4f})/{X_SAT} = {OMEGA_R_M_G_COLD:.6f}"
    )
    print(f"GR exact (Schwarzschild ell=2, n=0): omega_R * M_g = {OMEGA_R_M_G_GR}")
    print(f"AVE departure from GR: {100 * (1 - OMEGA_R_M_G_COLD / OMEGA_R_M_G_GR):.2f}% below\n")

    print(
        f"{'Event':12} {'M (M_sun)':>10} {'a_*':>6} "
        f"{'AVE-cold':>10} {'AVE-Kerr':>10} {'KB AVE':>10} {'GR-Kerr':>10} "
        f"{'KB obs':>10} {'AVE-vs-KB':>11} {'AVE-vs-obs':>11}"
    )
    print("-" * 120)

    disagreements = 0
    for ev in LIGO_EVENTS:
        f_cold = ave_cold_f_ring_hz(ev.m_final_msun)
        f_ave_kerr = ave_kerr_f_ring_hz(ev.m_final_msun, ev.a_star)
        f_gr_kerr = gr_f_ring_hz(ev.m_final_msun, ev.a_star)
        delta_kb = 100 * abs(f_ave_kerr - ev.f_kb_ave_hz) / ev.f_kb_ave_hz
        delta_obs = 100 * (f_ave_kerr - ev.f_kb_obs_hz) / ev.f_kb_obs_hz
        flag = "" if delta_kb < 1.0 else " (>1% DRIFT)"
        if delta_kb >= 1.0:
            disagreements += 1
        print(
            f"{ev.name:12} {ev.m_final_msun:>10.1f} {ev.a_star:>6.2f} "
            f"{f_cold:>10.1f} {f_ave_kerr:>10.1f} {ev.f_kb_ave_hz:>10.1f} {f_gr_kerr:>10.1f} "
            f"{ev.f_kb_obs_hz:>10.1f} {delta_kb:>10.2f}%{flag} {delta_obs:>+10.2f}%"
        )

    print("\nLegend:")
    print("  AVE-cold:   AVE prediction at zero spin (omega_R M_g = 18/49)")
    print("  AVE-Kerr:   AVE prediction with Kerr photon-sphere correction at a_*")
    print("  KB AVE:     AVE prediction as cited in ave-merger-ringdown-eigenvalue.md")
    print("  GR-Kerr:    GR exact prediction (omega_R M_g = 0.3737) with Kerr correction")
    print("  KB obs:     LIGO-collaboration observed value as cited in KB")
    print("  AVE-vs-KB:  computed |AVE-Kerr - KB AVE| / KB AVE")
    print("  AVE-vs-obs: computed (AVE-Kerr - KB obs) / KB obs (signed; AVE is higher)")

    if disagreements:
        print(
            f"\n[FAIL] {disagreements} of {len(LIGO_EVENTS)} events show >1% drift "
            f"between computed and KB-cited AVE prediction."
        )
    else:
        print(
            f"\n[PASS] all {len(LIGO_EVENTS)} events match KB-cited AVE prediction "
            f"to within 1%. KB table is computationally self-consistent."
        )

    return disagreements


def main() -> int:
    """Phase 1 entry point. Returns nonzero exit if drift > 1%."""
    return verify_kb_table()


if __name__ == "__main__":
    import sys

    sys.exit(main())
