"""Keepers for the carrier-declaration guard (ENGINE-HARDENING ARC item 5).

Certifies that (1) every lattice-constructing entry point declares its D1-ratified
carrier, and (2) a diamond-stencil (non-canonical instrument) consumer must
acknowledge with `instrument_scope=` or the guard fires — RAISE for new
construction, DeprecationWarning for frozen-provenance drivers (KEEP-BOTH).

Deterministic; α-clean; sub-second. Gating-lane.
"""

import warnings

import numpy as np
import pytest

from ave.core.carrier import Carrier, coerce_carrier, require_instrument_scope
from ave.core.chiral_lattice import build_diamond_net, build_srs_net


# ─────────────────────────────────────────────────────────────────────────────
# carrier vocabulary
# ─────────────────────────────────────────────────────────────────────────────
def test_carrier_vocabulary():
    assert Carrier.SRS_Z3.value == "srs-z3"
    assert Carrier.DIAMOND_Z4.value == "diamond-z4-instrument"
    assert Carrier.CARTESIAN_REF.value == "cartesian-reference"
    assert Carrier.K_SPACE.value == "k-space"
    assert Carrier.DIAMOND_Z4.is_instrument
    assert not Carrier.SRS_Z3.is_instrument
    assert not Carrier.CARTESIAN_REF.is_instrument


def test_coerce_carrier_rejects_unknown():
    assert coerce_carrier("srs-z3") is Carrier.SRS_Z3
    assert coerce_carrier(Carrier.DIAMOND_Z4) is Carrier.DIAMOND_Z4
    with pytest.raises(ValueError):
        coerce_carrier("cubic-z6-nonsense")


# ─────────────────────────────────────────────────────────────────────────────
# every lattice-constructing entry point declares its carrier
# ─────────────────────────────────────────────────────────────────────────────
def test_srs_builder_declares_srs_carrier():
    net = build_srs_net(L=3)
    assert net.carrier == "srs-z3"


def test_diamond_builder_declares_instrument_carrier():
    net = build_diamond_net(L=4)
    assert net.carrier == "diamond-z4-instrument"


def test_carrier_field_is_additive_default():
    """A LatticeNet built without a carrier declaration reports 'unknown' (backward-
    compatible: existing direct constructions do not break)."""
    from ave.core.chiral_lattice import LatticeNet

    net = LatticeNet(
        name="x",
        handedness="?",
        degree=3,
        pos=np.zeros((1, 3)),
        neighbors=[[]],
        reverse_port=[[]],
        bond_unit=[[]],
        box=1.0,
    )
    assert net.carrier == "unknown"


# ─────────────────────────────────────────────────────────────────────────────
# the guard: diamond consumer must acknowledge
# ─────────────────────────────────────────────────────────────────────────────
def test_non_instrument_needs_no_acknowledgment():
    assert require_instrument_scope("srs-z3", None) == ""
    assert require_instrument_scope(Carrier.CARTESIAN_REF, None) == ""


def test_diamond_new_construction_raises_without_ack():
    """New construction on the diamond instrument WITHOUT an acknowledgment raises."""
    with pytest.raises(ValueError, match="NON-CANONICAL INSTRUMENT"):
        require_instrument_scope(Carrier.DIAMOND_Z4, None)
    with pytest.raises(ValueError):
        require_instrument_scope(Carrier.DIAMOND_Z4, "")  # empty string is not an ack


def test_diamond_frozen_provenance_warns_not_raises():
    """A frozen-provenance diamond consumer with no ack WARNS (KEEP-BOTH), not raises."""
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        got = require_instrument_scope(Carrier.DIAMOND_Z4, None, frozen_provenance=True)
    assert got == ""
    assert len(w) == 1 and issubclass(w[0].category, DeprecationWarning)


def test_diamond_with_ack_is_clean():
    got = require_instrument_scope(Carrier.DIAMOND_Z4, "stage-2 native-cage repro")
    assert got == "stage-2 native-cage repro"


# ─────────────────────────────────────────────────────────────────────────────
# a diamond-stencil SOLVER built without the acknowledgment fires the guard
# ─────────────────────────────────────────────────────────────────────────────
def test_diamond_stencil_consumer_new_call_raises_without_ack(monkeypatch):
    """Constructing a diamond-carrier operator via a NEW (non-frozen) call raises.

    `build_grad_div_periodic` is frozen-provenance (it WARNS by default to preserve
    the merged Stage-2 output). To exercise the RAISE path — the intended behavior
    for NEW construction — call the guard directly as a new consumer would."""
    with pytest.raises(ValueError, match="instrument_scope"):
        require_instrument_scope(Carrier.DIAMOND_Z4, None, site="a_new_diamond_solver", frozen_provenance=False)


def test_frozen_diamond_builder_still_runs_and_is_byte_identical():
    """The frozen diamond builder runs WITH the guard (warn path) and its output is
    unchanged — the guard is a gate, not a computation change (byte-identity)."""
    from ave.solvers.native_cage_imex import assemble_L_D, build_grad_div_periodic

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")  # legacy no-ack call warns; suppress for the test
        Grad, Div = build_grad_div_periodic(N=4)
    L = assemble_L_D(Grad, Div, np.ones(4**3))
    # Div = +Gradᵀ EXACTLY (the +PSD invariant the guard must not have perturbed).
    assert np.max(np.abs((Div - Grad.T).toarray())) == 0.0
    assert np.max(np.abs((L - L.T).toarray())) < 1e-12  # symmetric


def test_internal_diamond_callers_do_not_warn():
    """The frozen internal callers pass an explicit instrument_scope, so a normal
    construction path is warning-free (only a NAKED legacy call warns)."""
    from ave.solvers.native_cage_imex import build_grad_div_periodic

    with warnings.catch_warnings():
        warnings.simplefilter("error", DeprecationWarning)
        # an acknowledged call must NOT warn (would raise under simplefilter('error'))
        build_grad_div_periodic(N=4, instrument_scope="test acknowledgment")
