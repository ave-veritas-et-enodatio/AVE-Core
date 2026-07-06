"""EM-sector saturation keying functional S_E, S_B — gating tests.

FROZEN prereg: research/2026-07-05_em-saturation-keying-functional_prereg_FROZEN.md
(freeze commit bfd897c5). Locks the load-bearing derivation claims:

  piece (a): secular averaging in the node clock frame -- <E^2> does NOT vanish
             for static (naive key fails); transport-gradient DOES vanish.
  piece (b): the substrate forces the T-POYNT transport invariant; frequency-
             independence -> Table I survives; the coefficient fork (NORM-YIELD
             vs NORM-CLOCK) is honest.
  six frozen constraints: muonic-H blind (analytic), pump engaged, PVLAS/BMV
             dn_mu=0, DeLLight -1/4 A^2, boost zero-sequence.

Fast closed-form checks STAY gating. The full muonic bracket-integral pipeline
(the #539-reuse liveness pipeline, ~few s) is engine_sim.
"""
import sys
from pathlib import Path

import numpy as np
import pytest

from ave.core.constants import (
    C_0,
    E_YIELD,
    EPSILON_0,
    L_NODE,
    XI_TOPO,
    Z_0,
)

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "verify"))
import em_saturation_keying_constraints as K  # noqa: E402
import em_saturation_keying_invariant as INV  # noqa: E402
import em_saturation_keying_secular as SEC  # noqa: E402

E_C = E_YIELD


# ======================================================= PIECE (a): node clock
def test_node_clock_identity_exact():
    """hbar*omega_C == m_e c^2 and omega_C == c/ell_node (both exact)."""
    nc = SEC.node_clock_identity()
    assert nc["ratio_hbar_wc_over_mc2"] == pytest.approx(1.0, abs=1e-14)
    assert nc["omega_C"] == pytest.approx(C_0 / L_NODE, rel=1e-14)


def test_drive_bands_both_nonsecular():
    """The pump (3e-6) AND probe (0.02) both sit at omega/omega_C << 1 -> naive
    clock-frame averaging blinds BOTH (Grant's premise b)."""
    bands = SEC.drive_bands()
    assert bands["pump_1.55eV"][1] == pytest.approx(3.033e-6, rel=1e-3)
    assert bands["probe_10keV"][1] == pytest.approx(0.01957, rel=1e-3)
    assert bands["static"][1] == 0.0


def test_naive_E2_engagement_does_not_vanish_for_static():
    """<E^2> is NONZERO for a held static field (static limit (E0/Ec)^2) -> the
    naive amplitude key CANNOT distinguish static from wave (only by <cos^2>=1/2).
    This is exactly why the corpus R2 |E|-key fails muonic-H [C-EXCLUDED]."""
    b_static = SEC.secular_projection_numeric(0.0)
    assert b_static["amp2_secular"] == pytest.approx(1.0, abs=1e-9)  # static engages
    b_wave = SEC.secular_projection_numeric(0.0196)
    assert b_wave["amp2_secular"] == pytest.approx(0.5, abs=1e-6)  # wave: <cos^2>=1/2
    # they differ only by 2x -> NOT a blindness (that is the failure)


def test_transport_gradient_vanishes_for_static_scales_omega2():
    """The transport-gradient content <(dE/dt)^2>/wC^2 = (omega/wC)^2 * 1/2:
    EXACTLY zero for static (DC-blind), grows as (omega/wC)^2 for a wave."""
    b_static = SEC.secular_projection_numeric(0.0)
    assert b_static["beat_secular"] == 0.0  # static -> exactly zero (DC-blind)
    for r in [3.033e-6, 0.0196, 1.0]:
        b = SEC.secular_projection_numeric(r)
        assert b["beat_secular"] == pytest.approx(0.5 * r**2, rel=1e-3)


# ================================================= PIECE (b): transport invariant
def test_poynting_zero_for_held_nonzero_for_wave():
    """T-POYNT <E H>: zero for held stock (H=0 -> DC-blind), nonzero for a wave."""
    b_static = INV.three_invariants_numeric(0.0, held=True)
    assert b_static["poynt"] == 0.0  # held: no transport
    b_wave = INV.three_invariants_numeric(0.0196, held=False)
    assert b_wave["poynt"] == pytest.approx(0.5 / Z_0, rel=1e-6)  # <E^2>/Z0 = 1/(2 Z0)


def test_poynting_frequency_independent_table_I_survives():
    """The Poynting transport is FREQUENCY-INDEPENDENT for a co-moving wave
    (same value pump/probe/resonant) -> the pump engages fully -> Table I survives.
    This is what distinguishes T-POYNT (pump engaged) from T-BEAT (pump suppressed
    by (omega/wC)^2)."""
    vals = [INV.three_invariants_numeric(r, held=False)["poynt"]
            for r in [3.033e-6, 0.0196, 1.0]]
    assert vals[0] == pytest.approx(vals[1], rel=1e-9)
    assert vals[1] == pytest.approx(vals[2], rel=1e-9)


def test_tbeat_would_collapse_pump():
    """T-BEAT at the pump is suppressed by (omega_pump/wC)^2 ~ 9e-12 relative to the
    frequency-independent Poynting -> T-BEAT would COLLAPSE Table I. The substrate
    picks T-POYNT (Grant's Poynting candidate), not T-BEAT."""
    r_pump = 3.033e-6
    beat = INV.three_invariants_numeric(r_pump, held=False)["beat"]
    # beat (in E^2/wC^2 units) ~ (omega/wC)^2/2 -> vanishes at the pump
    assert beat == pytest.approx(0.5 * r_pump**2, rel=1e-3)
    assert beat < 1e-11  # collapsed at the pump


def test_transport_coefficient_geometric_and_normalization_honest():
    """T/(E/Ec)^2 = 1/(4pi) under NORM-CLOCK (rest-energy-per-clock); the geometric
    1/(4pi), 1/(8pi) are the sqrt(8pi) family (clm-bdualb). HONEST: this rides the
    normalization; NORM-YIELD gives coefficient 1 (Table I unchanged)."""
    P = INV.poynting_coefficient_honesty()
    assert P["T_coeff"] == pytest.approx(1.0 / (4.0 * np.pi), rel=1e-9)
    assert P["u_field_Ec_over_u_rest"] == pytest.approx(1.0 / (8.0 * np.pi), rel=1e-9)
    # NORM-YIELD recovers coefficient 1.0 exactly (self-consistent w/ E_c calibration)
    S_yield = C_0 * EPSILON_0 * E_C**2  # yield-field Poynting flux
    T_at_Ec_yield = (E_C**2 / Z_0) / S_yield
    assert T_at_Ec_yield == pytest.approx(1.0, rel=1e-12)


# ============================================= constraints (analytic, fast)
def test_constraint_pump_table_I_unchanged_norm_yield():
    """NORM-YIELD: T=(E/Ec)^2 -> dn_bir = -1/2 A^2 EXACTLY -> P_flip rescale 1.0."""
    c2 = K.constraint_2_pump()
    assert c2["A2_letter"] == pytest.approx(5.9e-7, rel=2e-2)  # Letter's A^2
    assert c2["dn_bir_yield"] == pytest.approx(c2["dn_bir_letter"], rel=1e-12)
    assert c2["Pflip_rescale_yield"] == pytest.approx(1.0, rel=1e-12)


def test_constraint_probe_dispersion_qell2_ordering():
    """Probe-energy dispersion (q ell_node)^2: monotone increasing with probe
    energy, over-determined by ell_node alone; all < 0.1% (Letter's bound)."""
    disp = K.constraint_2_pump()["probe_dispersion"]
    df = disp["dark-field"]["qell_node_sq"]
    cv = disp["conventional"]["qell_node_sq"]
    he = disp["high-energy"]["qell_node_sq"]
    assert df < cv < he  # monotone with probe energy
    assert he < 1e-3  # all under the Letter's <0.1% dispersion bound
    # over-determined by ell_node: ratio = (E_i/E_j)^2 (one scale)
    E_df, E_cv = 8766.0, 9835.0
    assert cv / df == pytest.approx((E_cv / E_df) ** 2, rel=1e-9)


def test_constraint_magnetic_pvlas_bmv_dn_mu_zero():
    """PVLAS/BMV: both DC in the clock frame (omega/wC ~ 1e-20/-18) -> A_I=0 ->
    S_mu=1 -> dn_mu=0 (Route C, clm-pvlas1)."""
    c = K.constraint_3_4_magnetic()
    assert c["pvlas_dn_mu"] == 0.0
    assert c["bmv_dn_mu"] == 0.0
    assert c["pvlas_omega_over_wC"] < 1e-18
    assert c["bmv_omega_over_wC"] < 1e-16


def test_constraint_dellight_common_mode_unchanged():
    """DeLLight common-mode dn_iso = -1/4 A^2 (NORM-YIELD, unchanged)."""
    c = K.constraint_5_dellight()
    assert c["dn_iso_yield"] == pytest.approx(c["dn_iso_letter"], rel=1e-12)


def test_constraint_boost_zero_sequence_matches_letter():
    """Boost: motional E (2.5T, 370km/s) A^2 = 6.7e-23 -> matches the Letter's
    ~7e-23. The boosted static field is a DC drift (zero-sequence), aliased to
    wC, averages out -> boost closed structurally by the transport tensor flux."""
    c = K.constraint_6_boost()
    assert c["A2_from_boosted_B"] == pytest.approx(6.7e-23, rel=5e-2)


def test_i_max_route_c_dual_scale():
    """S_B dual: I_max = xi_topo * c = 124.384 A (Route C threshold)."""
    assert XI_TOPO * C_0 == pytest.approx(124.384, rel=1e-4)


# =============================================== homonym / cross-wire guards
def test_no_mechanical_qpoint_numbers_in_em_coefficient():
    """Sector guard: the EM transport coefficient must NOT be a mechanical
    Q-point number (2/7=0.2857, 9.7734, sqrt(8)=2.828). The geometric factors
    are 1/(4pi), 1/(8pi) -- distinct from the mechanical-sector canon."""
    P = INV.poynting_coefficient_honesty()
    for forbidden in [2.0 / 7.0, 9.7734, np.sqrt(8.0)]:
        assert not np.isclose(P["T_coeff"], forbidden, rtol=1e-3)


# ===================== STANDING FALSIFIER: the physical-H atom (CRITICAL-1) ======
def test_physical_atomic_H_is_nonzero_local_poynting():
    """CRITICAL-1: the real muonic atom is NOT transport-dead. The proton magnetic
    dipole creates a permanent static H(r) -> the LOCAL Poynting engagement T(r) is
    NONZERO everywhere the physical H is nonzero. The H=0 fiat was an artifact."""
    import em_saturation_keying_constraints as KK
    a = KK.p3.A_MU
    for f in (0.1, 0.5, 1.0, 2.0):
        E_C_r = KK.p3.K / (f * a) ** 2
        T = float(KK.transport_engagement_T(E_C_r, KK.H_atomic(f * a)))
        assert T > 0.0  # physical H -> nonzero local Poynting (not transport-dead)


@pytest.mark.engine_sim
def test_muonic_physical_H_CONSTRAINT_KILLED():
    """STANDING FALSIFIER (CRITICAL-1): the boxed LOCAL-Poynting functional
    evaluated on the PHYSICAL atomic H(r) (proton dipole) OVERSHOOTS the 2.3 ueV
    CREMA window by 10^0-10^4 x -- it FAILS its own headline constraint. The
    functional keys on LOCAL pointwise E x H and cannot distinguish divergence-free
    circulation (hidden-momentum class) from net transport. This is the
    [CONSTRAINT-KILLED] result; the test is a permanent falsifier of the LOCAL form."""
    c1 = K.constraint_1_muonic()
    assert not c1["passes"]  # FAILS -> [CONSTRAINT-KILLED]
    assert c1["overshoot_factor"] > 1.0  # exceeds the window
    # even deleting everything inside 2 a_mu leaves > the window:
    outer = c1["shifts_ueV_by_rcut"]["2a_mu"]
    assert abs(outer) > c1["window_ueV"]  # near-nucleus cutoff cannot rescue
    # worst-case is far above the window (the near-nucleus r^-3 dipole dominates):
    assert c1["overshoot_factor"] > 100.0
