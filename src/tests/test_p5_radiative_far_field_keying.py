"""Standing tests for P5 — RADIATIVE FAR-FIELD KEYING + S_B.

Routed verdict: [RADIATIVE-KEY-REFUTED]. The far-field / net-radiated-power
diagnostic does NOT track loading: static-E LOADS (eps channel) with zero
radiated power, and a standing wave LOADS both channels with zero NET radiated
power — two near-zone loaders. The eps channel keys on the local potential
coordinate |E| (charge, static-capable); the mu channel keys on the local
circulation coordinate |curl H| (rate). Both are LOCAL phase-space coordinates,
not the field's global radiative character. Two sector postulates remain.

Fast-core gates: the verdict routing, the per-config loading pattern, the
firewall (no ALPHA/M_E/m_e on the verdict path), scale-invariance, the
anti-tautology (emergent static-B null + a control that can load), and the S_B
static + near-zone limits.

Prereg (freeze 76486a59, committed BEFORE the driver):
  research/2026-07-08_p5-radiative-far-field-keying_prereg_FROZEN.md
"""

from __future__ import annotations

import os
import sys

import numpy as np
import pytest

_VERIFY = os.path.join(os.path.dirname(__file__), "..", "scripts", "verify")
if _VERIFY not in sys.path:
    sys.path.insert(0, os.path.abspath(_VERIFY))

from p5_radiative_far_field_keying import (  # noqa: E402
    E_YIELD,
    I_MAX,
    TAU_A,
    VERDICT_PATH_FNS,
    anti_tautology_check,
    firewall_ast_scan,
    null_emergence_refinement,
    run_all,
    s_b_near_zone_limit,
    scale_invariance_check,
    verdict,
)


@pytest.fixture(scope="module")
def result():
    diags, loads, fars = run_all(E_YIELD, I_MAX)
    v = verdict(diags, loads, fars)
    return dict(diags=diags, loads=loads, fars=fars, verdict=v)


# --- the routed verdict -----------------------------------------------------

def test_verdict_is_refuted(result):
    """The single radiative-far-field key is REFUTED (near-zone loaders exist)."""
    assert result["verdict"]["route"] == "RADIATIVE-KEY-REFUTED"


def test_two_near_zone_loader_violations(result):
    """static-E and the standing-wave control both LOAD with F<0.5 (near-field)."""
    viols = result["verdict"]["tracking_violations"]
    joined = " | ".join(viols)
    assert "static_E: LOADS but near-field" in joined
    assert "standing: LOADS but near-field" in joined
    assert len(viols) == 2


def test_ontology_configs_behave_as_predicted(result):
    """The per-config ontology predictions ALL hold (E loads, B transparent,
    radiation active) — the behaviors are reproduced; only their UNIFICATION by a
    far-field diagnostic fails."""
    assert result["verdict"]["ontology_configs_ok"] is True


def test_loading_pattern(result):
    loads = result["loads"]
    assert loads["static_E"]["overall"] == "load"
    assert loads["static_E"]["eps_loads"] is True
    assert loads["static_E"]["mu_loads"] is False       # no B -> mu transparent
    assert loads["static_B"]["overall"] == "transparent"
    assert loads["traveling"]["overall"] == "load"
    assert loads["traveling"]["eps_loads"] and loads["traveling"]["mu_loads"]
    assert loads["standing"]["overall"] == "load"


def test_farfield_pattern(result):
    """Radiated-power diagnostic: only the traveling wave is far-field."""
    fars = result["fars"]
    assert fars["traveling"] == "far"
    assert fars["static_E"] == "near"
    assert fars["static_B"] == "near"
    assert fars["standing"] == "near"                    # standing = zero NET flux


# --- anti-tautology: the static-B null EMERGES and the null is informative ---

def test_static_B_mu_null_emerges(result):
    """static-B mu-null is COMPUTED from curl H of the field (= 0), not imposed."""
    assert result["diags"]["static_B"]["rms_A_I"] < TAU_A
    assert result["diags"]["static_B"]["rms_A_I"] == 0.0  # uniform source-free B


def test_control_can_load(result):
    """The standing-wave control CAN report loading -> the mu-null is informative
    (the functional does not always return zero)."""
    anti = anti_tautology_check(result["diags"], result["loads"])
    assert anti["control_standing_can_load"] is True
    assert anti["informative_null"] is True
    assert anti["null_vs_active_gap_decades"] > 100     # uniform-B null is exact 0


def test_dipole_null_converges_O_h2():
    """A NON-uniform source-free static B (dipole): FD curl H -> analytic 0 as
    O(h^2) (ratio ~4 per halving) -> the mu-null is the general property."""
    ref = null_emergence_refinement(E_YIELD, I_MAX)
    assert ref["monotone_decreasing"] is True
    assert ref["converges_toward_zero"] is True
    assert 3.5 < ref["order_ratio_first_pair"] < 4.5     # 2nd-order convergence


# --- firewall + scale-invariance -------------------------------------------

def test_firewall_no_alpha_me_on_verdict_path():
    """AST scan: no ALPHA/M_E/m_e token in the verdict-path functions."""
    this = os.path.join(_VERIFY, "p5_radiative_far_field_keying.py")
    fw = firewall_ast_scan(os.path.abspath(this), VERDICT_PATH_FNS)
    assert fw["clean"] is True, fw["hits"]


def test_scale_invariance_verdict_unchanged():
    """Rescaling E_yield, I_max by +-10x does not flip the loading pattern or the
    verdict -> the alpha-echo magnitude never reaches the verdict."""
    sc = scale_invariance_check()
    assert sc["scale_invariant"] is True
    assert sc["base_route"] == "RADIATIVE-KEY-REFUTED"
    for k, v in sc["rescaled"].items():
        assert v["matches_base"] is True


# --- S_B: static limit and near-zone (kr)^2 suppression ---------------------

def test_S_B_static_limit_transparent():
    """S_B static endpoint: A_I=0 -> S_mu=1 -> delta_n_mu=0 (Letter Eq (6))."""
    A_I = 0.0
    S_mu = np.sqrt(1.0 - A_I ** 2)
    dn_mu = np.sqrt(S_mu) - 1.0
    assert S_mu == 1.0
    assert dn_mu == 0.0


def test_S_B_near_zone_kr_squared_and_transparency():
    """Near-zone A_I ~ (kr)^2 (loglog slope 2, emergent from two d/dt) and
    delta_n_mu -> 0 as kr -> 0 (PVLAS Hz / BMV ms consistency, COMPUTED)."""
    sb = s_b_near_zone_limit(E_YIELD, I_MAX)
    assert abs(sb["loglog_slope_A_I_vs_kr"] - 2.0) < 1e-6
    # deepest near-zone point is essentially transparent
    assert sb["S_mu"][0] > 1.0 - 1e-6
    assert abs(sb["delta_n_mu"][0]) < 1e-6
    # monotone: transparency improves toward kr -> 0
    assert abs(sb["delta_n_mu"][0]) < abs(sb["delta_n_mu"][-1])
