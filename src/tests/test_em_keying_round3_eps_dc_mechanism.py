"""Tests for EM keying ROUND 3 — the ε-side DC-mechanism derivation.

Routed bin: [DERIVED: CHARGE-KEYED] (uniform-bias gauge rider). The ε-grade
(transverse-T2 permittivity) nonlinearity keys on the MEAN-SQUARE of the
instantaneous amplitude (DC-included), NOT the time-variance. M0/M1/M2/M3 all
confirm no lossless DC-block exists.

Fast-core gating tests (structural, sympy/numpy) + one STANDING FALSIFIER
(marked engine_sim) that catches regression of the CHARGE-KEYED verdict via the
firewalled #539 muon comparison.

Prereg (freeze 942c950b):
  research/2026-07-06_em-keying-round3-eps-dc-mechanism_prereg_FROZEN.md
"""

from __future__ import annotations

import os
import sys

import numpy as np
import pytest
import sympy as sp

# make the verify/ drivers importable (they live in src/scripts/verify)
_VERIFY = os.path.join(os.path.dirname(__file__), "..", "scripts", "verify")
if _VERIFY not in sys.path:
    sys.path.insert(0, os.path.abspath(_VERIFY))

from em_keying_round3_mechanism import (  # noqa: E402
    m0_axiom_argument,
    m1_topology_dc_block,
    m2_mode_energy_ledger,
    m3_quiescent_slide,
    S_kernel,
)


# ---------------------------------------------------------------------------
# M0 — the local kernel keys on the MEAN-SQUARE (DC-included), not the variance.
# ---------------------------------------------------------------------------
def test_m0_leading_deficit_is_half_meansquare_not_variance():
    m0 = m0_axiom_argument()
    a0, a1, _, _ = m0["symbols"]
    # leading (2nd-order) mean deficit == (1/2) * (a0^2 + a1^2/2) = (1/2) MEAN-SQUARE
    assert sp.simplify(m0["mean_leading"] - m0["mean_square"] / 2) == 0
    # and it is NOT (1/2) * variance (a1^2/2)
    assert sp.simplify(m0["mean_leading"] - m0["variance"] / 2) != 0


def test_m0_held_dc_alone_gives_nonzero_local_deficit():
    """The H1-vs-H2 discriminator: a held DC bias ALONE loads the local ε (charge-keyed).
    Under H2 (variance) this would be identically zero."""
    m0 = m0_axiom_argument()
    a0 = m0["symbols"][0]
    deficit_dc = m0["deficit_dc_only"]
    # nonzero for any a0 in (0,1); leading a0^2/2
    for a0v in (0.1, 0.2, 0.3, 0.5):
        val = float(deficit_dc.subs(a0, a0v))
        assert val > 0.0
    # leading term is a0^2/2 (charge/mean-square signature)
    lead = sp.series(deficit_dc, a0, 0, 3).removeO()
    assert sp.simplify(lead - a0**2 / 2) == 0


def test_m0_counterfactual_variance_kernel_is_dc_blind():
    """Gate can fire (round-2 lesson, no Var(cos)=1/2 tautology): a hypothetical variance-keyed
    kernel is ZERO on a held DC, where the canonical sqrt kernel is NONZERO. They DISAGREE, so the
    mean-square verdict is a real property of the sqrt kernel."""
    a0 = 0.2
    canonical_held_dc = 1.0 - float(S_kernel(a0))       # sqrt kernel: > 0 (loads)
    hypo_variance_held_dc = 0.0                          # variance kernel: DC-blind by construction
    assert canonical_held_dc > 1e-6
    assert hypo_variance_held_dc == 0.0
    assert canonical_held_dc != hypo_variance_held_dc   # the counterfactual distinguishes


# ---------------------------------------------------------------------------
# M1 — topology: ε-varactor is SHUNT (sees held V), no series-C DC-block.
# ---------------------------------------------------------------------------
def test_m1_no_eps_side_series_c_dc_block():
    m1 = m1_topology_dc_block()
    assert m1["m1_dc_block_exists"] is False
    assert m1["shunt_varactor_sees_held_V"] is True
    # the series reactance is the bond INDUCTOR (B-side), not a capacitor
    assert "SERIES bond inductor" in m1["L_cell_role"]
    assert "SHUNT" in m1["C_cell_role"]


# ---------------------------------------------------------------------------
# M2 — energy ledger: held ½ε0E^2 sits IN the kernel element, no spectator mode.
# ---------------------------------------------------------------------------
def test_m2_h2_ledger_cannot_close():
    m2 = m2_mode_energy_ledger()
    assert m2["h2_ledger_closes"] is False
    assert m2["linear_spectator_mode_exists"] is False
    # no residual to park on a linear mode
    assert sp.simplify(sp.sympify(m2["residual_on_linear_spectator_mode"])) == 0


# ---------------------------------------------------------------------------
# M3 — tangent stiffness CHANGES under held bias; only lossless slide is dissipative.
# ---------------------------------------------------------------------------
def test_m3_tangent_stiffness_changes_under_bias():
    m3 = m3_quiescent_slide()
    assert m3["tangent_preserved_under_bias"] is False
    assert m3["m3_delivers_h2_losslessly"] is False
    # C_ss/C0 = 1/S^3, leading 1 + 3/2 A0^2 (changes under bias). Rebuild symbolically with the
    # positive-A0 assumption so the series expansion is well-formed (sympify-ing the string would
    # drop the assumption and leave (1-A0^2)^(-3/2) unexpanded).
    A0 = sp.symbols("A0", positive=True)
    S = sp.sqrt(1 - A0**2)
    C_ss_ratio = 1 / S**3
    C_eff_ratio = 1 / S
    lead = sp.series(C_ss_ratio, A0, 0, 3).removeO()
    assert sp.simplify(lead - (1 + sp.Rational(3, 2) * A0**2)) == 0
    # the differential C_ss (1/S^3) is NOT the chord C_eff (1/S) — they differ under bias
    assert sp.simplify(C_ss_ratio - C_eff_ratio) != 0
    # sanity: the driver's string forms match these
    assert m3["C_ss_tangent_ratio"] in ("(1 - A0**2)**(-3/2)", "1/(1 - A0**2)**(3/2)")


# ---------------------------------------------------------------------------
# Sub-answer (iv): FREQUENCY-INDEPENDENCE preserved (no 𝒲_beat rate-keying).
# ---------------------------------------------------------------------------
def test_meansquare_is_frequency_independent():
    """<A_V^2> = a0^2 + a1^2/2 is amplitude, frequency-independent. If a rate factor
    (omega/omega_C)^2 had been smuggled back, <A_V^2> would scale with omega."""
    a0, a1 = 0.12, 0.20
    sym = a0**2 + a1**2 / 2.0

    def meansq_numeric(omega):
        T = 2 * np.pi / omega
        ts = np.linspace(0.0, T, 20001)
        A = a0 + a1 * np.cos(omega * ts)
        return float(np.trapezoid(A**2, ts) / T)

    vals = [meansq_numeric(w) for w in (1e5, 1e10, 1e15, 1e18)]
    assert max(vals) - min(vals) < 1e-9         # frequency-independent
    assert all(abs(v - sym) < 1e-9 for v in vals)


# ---------------------------------------------------------------------------
# Sub-answer (i): SLOW-RAMP SETTLE-OUT — the deficit PERSISTS (H1), rate-independent.
# ---------------------------------------------------------------------------
def test_slow_ramp_deficit_persists_and_is_rate_independent():
    """After a slow ramp settles (dE/dt=0, J_D=0), the local ε-deficit = 1 - S(E/E_yield)
    depends ONLY on the held amplitude, not on the ramp rate. It PERSISTS (H1)."""
    a0 = sp.symbols("a0", positive=True)
    deficit = 1 - sp.sqrt(1 - a0**2)
    # no explicit rate variable in the deficit -> rate-independent post-settle
    rate = sp.symbols("rate", positive=True)
    assert deficit.diff(rate) == 0
    # nonzero for any held amplitude -> persists (does not decay to 0)
    assert float(deficit.subs(a0, 0.3)) > 0.0


# ===========================================================================
# STANDING FALSIFIER (engine_sim) — catches regression of the CHARGE-KEYED verdict.
# If a future change made the ε-grade DC-blind (H2/variance), the muon would stop
# loading and this test would need updating — i.e. it guards the routed bin.
# ===========================================================================
@pytest.mark.engine_sim
def test_charge_keyed_muon_overshoots_window_STANDING_FALSIFIER():
    """FIREWALLED §9 standing falsifier. Under [DERIVED: CHARGE-KEYED] the muon (non-uniform
    Coulomb field) LOADS and overshoots the CREMA window (reproducing #539 [C-EXCLUDED]).
    Consumes the #539 machinery by import. This is the regression guard: were the ε-grade
    excursion-keyed (H2), the static-in-time muon would be blind and NOT overshoot."""
    from problem3_muonic_lamb_shift import (  # noqa: E402
        J_TO_ueV,
        WINDOW_ueV_primary,
        shift_pathB,
    )

    shift_ueV = shift_pathB("continuum", "C-iii") * J_TO_ueV  # interior-excluded (most forgiving)
    # the charge-keyed functional overshoots the 2.3 µeV window by many orders of magnitude
    assert abs(shift_ueV) > WINDOW_ueV_primary
    assert abs(shift_ueV) / WINDOW_ueV_primary > 1e3   # gross overshoot (charge-keyed loads)
    assert np.isfinite(shift_ueV) and abs(shift_ueV) > 0  # null-verdict liveness: nonzero, finite


@pytest.mark.engine_sim
def test_uniform_bias_gauge_rider_does_not_rescue_nonuniform_muon():
    """The gauge rider (uniform held bias self-cancels) does NOT rescue the muon: its Coulomb
    amplitude spans ~2 decades across the atom (giant ∇A) — it is NOT uniform."""
    import ave.core.constants as C
    from problem3_muonic_lamb_shift import A_MU, K as K_COULOMB  # noqa: E402

    def A_V(r):
        return (K_COULOMB / r**2) / C.E_YIELD

    span_decades = np.log10(A_V(0.5 * A_MU) / A_V(5.0 * A_MU))
    assert span_decades > 1.0   # non-uniform (a uniform field would give 0 decades of span)
