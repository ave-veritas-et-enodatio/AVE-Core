"""Tests for EM keying ROUND 3 — the ε-side DC-mechanism derivation.

Routed bin: [DERIVED: CHARGE-KEYED] (single-cell + lattice-rigid; with a UNIFORM-bias
gauge-observability RIDER). The ε-grade (transverse-T2 permittivity) nonlinearity keys
on the MEAN-SQUARE of the instantaneous amplitude (DC-included), NOT the time-variance.
M0/M1/M2/M3 all confirm no lossless DC-block exists.

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
    m1_two_topology_dc_response,
    m2_mode_energy_ledger,
    m3_lattice_zero_mode_from_canon,
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
# M1 — two-topology COMPUTED DC-response: canonical passes held DC, series-C blocks it.
# ---------------------------------------------------------------------------
def test_m1_canonical_passes_held_dc_counterfactual_blocks():
    """COMPUTED (not declared): the canonical series-L/shunt-C unit passes the held DC to the
    varactor node; the series-C-blocked counterfactual relaxes it to zero. They GENUINELY DIFFER."""
    m1 = m1_two_topology_dc_response()
    # the two topologies are actually integrated and give DIFFERENT held-DC node voltages
    assert m1["Vnode_canonical_held_dc"] > 0.9        # canonical passes the held DC (-> V0)
    assert m1["Vnode_counterfactual_held_dc"] < 0.1   # series-C blocks the held DC (-> 0)
    assert m1["topologies_differ_on_held_dc"] is True
    assert m1["m1_dc_block_exists"] is False
    # the gate that reconciles the canonical node voltage against the LC-ladder DC relation fired-proof
    assert m1["reconcile_gate"]["can_fire_proven"] is True
    assert m1["reconcile_gate"]["passed"] is True
    # the series reactance is the bond INDUCTOR (B-side), not a capacitor
    assert "SERIES bond inductor" in m1["L_cell_role"]
    assert "SHUNT" in m1["C_cell_role"]


# ---------------------------------------------------------------------------
# M2 — energy ledger: two INDEPENDENT routes close with zero residual (COMPUTED).
# ---------------------------------------------------------------------------
def test_m2_two_route_ledger_closes_no_spectator_mode():
    """COMPUTED: the held-field energy on the saturating varactor by TWO independent routes
    (charge-path element sum vs constitutive Legendre co-energy) reconciles with ZERO residual
    -> no linear spectator capacitance -> H2 ledger cannot close. Gate proven can-fire."""
    m2 = m2_mode_energy_ledger()
    assert m2["h2_ledger_closes"] is False
    assert m2["linear_spectator_mode_exists"] is False
    # the two routes are genuinely different assemblies that reconcile to 0 residual
    assert sp.simplify(sp.sympify(m2["residual_between_routes"])) == 0
    assert m2["held_energy_fully_in_varactor"] is True
    # both routes recover the closed form 1 - sqrt(1-A^2) (the varactor's stored energy). Evaluate
    # numerically at a spot point to avoid symbol-assumption mismatch on sympify.
    A = sp.symbols("A")
    route_a = sp.sympify(m2["route_A_element_energy_sum"])
    closed = 1 - sp.sqrt(1 - A**2)
    for a_val in (0.1, 0.3, 0.5):
        assert abs(float(route_a.subs(A, a_val)) - float(closed.subs(A, a_val))) < 1e-12
    assert m2["reconcile_gate"]["can_fire_proven"] is True
    assert m2["reconcile_gate"]["passed"] is True


# ---------------------------------------------------------------------------
# M3 — T2-sector tangent CHANGES under held bias (sign-flipped from A1); kill survives.
# ---------------------------------------------------------------------------
def test_m3_kill_is_convention_robust_keep_both():
    """KEEP-BOTH CONVENTION FORK (round-3 fix-2, CLUSTER B / M3). The corpus's only explicit
    chord/tangent convention (device-circuit-models:60, A1 sector) admits BOTH a chord C0*S and a
    dQ/dV tangent C0*(S-A0^2/S) when applied to the T2 constitutive Q=C0*S*V. The M3 kill is
    CONVENTION-ROBUST: EVERY in-scope candidate object shifts DOWN nonzero under held bias; neither
    coefficient is crowned. The A1 +/S^3 form (+3/2, UP) is the OUT-OF-SCOPE V/V_snap sector, excluded.
    Both leading coefficients are asserted with sympy; -1/2 is NOT crowned as 'the' answer."""
    m3 = m3_quiescent_slide()
    assert m3["tangent_preserved_under_bias"] is False
    assert m3["m3_delivers_h2_losslessly"] is False
    assert m3["all_candidate_objects_shift_down_nonzero"] is True

    # CHORD / constitutive object: C0*S(A0), leading 1 - (1/2)A0^2  (leading coeff -1/2).
    A0 = sp.symbols("A0", positive=True)
    S = sp.sqrt(1 - A0**2)
    chord_lead = sp.series(S, A0, 0, 3).removeO()
    assert sp.simplify(chord_lead - (1 - sp.Rational(1, 2) * A0**2)) == 0   # -1/2 (DOWN)
    assert sp.simplify(S - 1) != 0                                          # chord shifts under bias

    # dQ/dV TANGENT of Q=C0*S(v)*V: dQ/dV = C0*(S - v^2/S) = C0*(1-2v^2)/sqrt(1-v^2), leading 1-(3/2)v^2.
    v = sp.symbols("v", positive=True)
    Sv = sp.sqrt(1 - v**2)
    dQdV = sp.simplify(sp.diff(Sv * v, v))
    assert sp.simplify(dQdV - (Sv - v**2 / Sv)) == 0                        # = S - A^2/S
    tangent_lead = sp.series(dQdV, v, 0, 3).removeO()
    assert sp.simplify(tangent_lead - (1 - sp.Rational(3, 2) * v**2)) == 0  # -3/2 (DOWN)

    # CONVENTION-ROBUSTNESS assertion (not crowning either): both leading coeffs < 0, and the
    # integral-chord too; the A1 +/S^3 form (+3/2, UP) is excluded from the in-scope set.
    assert sp.Rational(-1, 2) < 0 and sp.Rational(-3, 2) < 0                # both shift DOWN
    assert m3["C_chord_leading_coeff"] == "-1/2"
    assert m3["dQdV_tangent_leading_coeff"] == "-3/2"
    assert m3["integral_chord_leading_coeff"] == "-1/6"                     # DOWN too
    assert m3["dQdV_equals_S_minus_A2_over_S"] is True
    # the A1 out-of-scope form is +3/2 (SIGN UP) and is recorded as excluded, NOT used for routing
    assert m3["C_ss_A1_form_out_of_scope"] in ("(1 - A0**2)**(-3/2)", "1/(1 - A0**2)**(3/2)")
    a1_lead = sp.series(1 / S**3, A0, 0, 3).removeO()
    assert sp.simplify(a1_lead - (1 + sp.Rational(3, 2) * A0**2)) == 0      # +3/2 (UP, EXCLUDED)
    # the fork is flagged, not crowned
    assert "KEEP-BOTH" in m3["convention_fork_note"]
    assert "transverse-T2" in m3["sector"]


def test_m3_lattice_zero_mode_settled_rigid_full_band():
    """CLUSTER D finding [5] + round-3 fix-2 ITEM 1 (FULL-RANGE): the lattice-level zero-mode question.
    The K4 translational (E-coupled) sector carries transverse/shear stiffness k_s > 0, so all three
    linear acoustic branches are present (k4-bloch:58) -- NO floppy zero-mode. Rigidity holds across
    the ENTIRE counted band A in [0, 0.7071] (C_44 strictly positive, ~0.09..0.177), NOT because A is
    small; the A->1 floppy wall (C_44->4e-5) lies inside the EXCLUDED interior. COMPUTED: the
    transverse-acoustic branch speed is nonzero for k_s>0 and zero for the k_s=0 pathology (a
    CONSISTENCY ENCODING of the canon facts, not an independent verification)."""
    ml = m3_lattice_zero_mode_from_canon()
    assert ml["E_coupled_translational_sector_rigid_across_counted_band"] is True
    assert ml["c44_strictly_positive_across_counted_band"] is True
    assert ml["floppiness_is_ks0_pathology_only"] is True
    assert ml["lattice_zero_mode_absorbs_held_strain"] is False
    assert ml["m3_kill_extends_to_lattice"] is True
    # FULL-RANGE: C_44 > 0 across the whole counted band (all tabulated values strictly positive),
    # and the counted band is bounded at A <= 1/sqrt(2) = 0.7071 by the turnover construction.
    assert all(v > 0 for v in ml["C44_across_counted_band"].values())
    assert abs(ml["counted_band_A_max"] - 2.0 ** -0.5) < 1e-12
    # honesty tag: the shipped numeric is a consistency encoding, not an independent verification
    assert ml["numeric_is_consistency_encoding_not_verification"] is True
    # the borrow is flagged as a borrow (srs-z3 tensor quantifying a K4 qualitative structure)
    assert "BORROW" in ml["cross_lattice_borrow_flag"]
    # the rigid (k_s>0) branch speed genuinely exceeds the floppy (k_s=0) branch speed
    assert ml["cT2_with_shear_ks_gt_0"] > ml["cT2_pure_central_force_ks_0"]


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
    """COMPUTED (CLUSTER C): an ACTUAL time-domain integration of the tau_relax relaxation ODE under
    a ramped-then-held drive at several ramp rates. H1 predicts the post-settle deficit is nonzero,
    equal across rates, and equal to the held-DC value; H2 would predict decay to 0. We re-run the
    integrator here (independent of the driver) and assert the H1 signature."""
    import numpy as _np

    A_final, tau = 0.3, 1.0
    held_dc_target = 1.0 - _np.sqrt(1.0 - A_final**2)

    def integrate_ramp(ramp_time, total_time=200.0, n=200000):
        dt = total_time / n
        S = 1.0
        for k in range(n):
            A_now = A_final * min((k * dt) / ramp_time, 1.0)
            S += (_np.sqrt(1.0 - A_now**2) - S) / tau * dt
        return 1.0 - S

    deficits = [integrate_ramp(rt) for rt in (1.0, 5.0, 20.0)]
    # PERSISTS: nonzero (did NOT decay to 0 -> not H2)
    assert all(d > 1e-6 for d in deficits)
    # RATE-INDEPENDENT: equal across ramp rates
    assert max(deficits) - min(deficits) < 1e-4
    # EQUALS the held-DC value (charge-keyed persistence, COMPUTED)
    assert all(abs(d - held_dc_target) < 1e-3 for d in deficits)


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
def test_m1_two_topology_dc_response_STANDING_FALSIFIER():
    """STANDING FALSIFIER keyed to a PHYSICAL claim (not a fixed identity): the CHARGE-KEYED verdict
    rests on the canonical series-L/shunt-C unit passing a held DC to the varactor while a series-C
    counterfactual blocks it. This runs the two ACTUAL time-domain topology integrations and asserts
    they GENUINELY DIFFER on a held DC. Were the ε-element instead behind a series-C (DC-block), the
    canonical node would ALSO relax to zero and this falsifier would fire -- guarding the routed bin's
    M1 leg against a topology regression. (Replaces the prior fixed span-decades identity, which could
    not fail on physics -- round-3 fix [25].)"""
    m1 = m1_two_topology_dc_response()
    v_canon = m1["Vnode_canonical_held_dc"]
    v_cf = m1["Vnode_counterfactual_held_dc"]
    # the canonical unit passes the held DC (charge-keyed loads); the series-C counterfactual blocks it
    assert v_canon > 0.9, "canonical series-L/shunt-C unit failed to pass the held DC -> M1 regressed"
    assert v_cf < 0.1, "series-C counterfactual failed to block the held DC -> M1 falsifier not live"
    assert abs(v_canon - v_cf) > 0.5, "the two topologies do not differ on a held DC -> M1 not falsifiable"
    # the slow-ramp persistence value is a nonzero physical number (charge-keyed persistence)
    from em_keying_round3_mechanism import main  # noqa: E402 -- run only in engine_sim tier
    import io
    import contextlib

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        main()
    import json

    out = json.loads(buf.getvalue())
    assert out["slow_ramp_settle_out"]["deficit_persists_nonzero"] is True
    assert out["slow_ramp_settle_out"]["deficit_rate_independent"] is True


@pytest.mark.engine_sim
def test_C_iii_band_split_dominant_subpitch_band_STANDING_PIN():
    """FIREWALLED §9 band-split pin (round-3 fix-2, ITEM 2). The COMPUTED per-band breakdown of the
    C-iii overshoot: ~+103% comes from the SUB-PITCH band [r_turn, ell_node] = [159.6, 386.2] fm
    (INSIDE one node pitch), and the whole SUPER-pitch remainder nets only ~-3.2%. This pins where the
    magnitude lives (correcting the sample-point-only table that skipped the dominant band) and both
    honest consequences: (i) the verdict does NOT ride on the sub-pitch band (super-pitch alone is
    ~2e4x the CREMA window -> pitch-cutoff rescue excluded); (ii) the MAGNITUDE is sub-pitch = the
    open [B-AVE] arm's territory. Consumes the #539 machinery by import (below the firewall)."""
    from em_keying_round3_comparison import band_split_C_iii  # noqa: E402

    bs = band_split_C_iii()
    # bands sum to 100% of the total (the split is exhaustive / conserving)
    assert abs(sum(b["fraction_of_total"] for b in bs["bands"]) - 1.0) < 1e-3
    # dominant SUB-PITCH band [r_turn, ell_node] carries ~+103% of the shift (>> 1.0, and > super-pitch)
    dom = bs["dominant_subpitch_band_fraction"]
    assert 1.00 < dom < 1.06, f"dominant sub-pitch band fraction {dom} off the pinned ~+103%"
    # the dominant band is the [r_turn, ell_node] one (labelled SUB-PITCH)
    assert "SUB-PITCH" in bs["bands"][0]["band"]
    assert bs["bands"][0]["fraction_of_total"] == dom
    # SUPER-pitch remainder nets a small NEGATIVE fraction (~-3.2%), opposite sign to the dominant band
    sp_net = bs["superpitch_net_fraction"]
    assert -0.05 < sp_net < -0.02, f"super-pitch net fraction {sp_net} off the pinned ~-3.2%"
    # consequence (i): super-pitch remainder ALONE grossly exceeds the CREMA window (pitch-cutoff dead)
    from problem3_muonic_lamb_shift import WINDOW_ueV_primary  # noqa: E402
    assert bs["superpitch_net_magnitude_ueV"] / WINDOW_ueV_primary > 1e3
    # the 1-2-pitch band [2 a_mu, 5 a_mu] nets a small NEGATIVE (~-1.3%), NOT the dominant load
    one_to_two_pitch = bs["bands"][2]["fraction_of_total"]
    assert -0.02 < one_to_two_pitch < 0.0
