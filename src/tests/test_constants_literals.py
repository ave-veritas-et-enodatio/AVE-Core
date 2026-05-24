"""
Verify that the literals stored in ``ave.core.constants`` for values that
were historically computed at import time still match what the live solver
produces.

Background (P5-A): ``I_SCALAR_1D`` and ``BARYON_LADDER`` were previously
computed at import time by running the Faddeev-Skyrme solver via
``scipy.optimize``.  That created a structural circular dependency between
``ave.core.constants`` and ``ave.topological.faddeev_skyrme``.  The fix:
pre-compute the values once, store as literals, and verify here that the
literals remain consistent with the live computation.

When the underlying physics (integrand, ansatz, coupling) changes, this test
will fail.  The remediation is to re-run the helpers in
``ave.core._constants_compute`` and update the literals in
``ave.core.constants`` to the new values.
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.core import constants
from ave.core._constants_compute import (
    _compute_baryon_ladder,
    _compute_i_scalar_dynamic,
)

# Tolerance: float64 has ~15 significant digits, but scipy.optimize converges
# to a finite number of inner iterations and the ansatz parameters land at
# slightly different float values across runs of L-BFGS-B on different
# platforms / scipy versions.  Empirically these literals reproduce bit-for-
# bit on the development machine, so 1e-12 is comfortably tight.  If a
# scipy/BLAS upgrade ever produces sub-ppm trailing-decimal drift, loosen to
# 1e-9 and document the platform variance — anything looser than that would
# also miss real physics changes (e.g., the proton mass shifts at the ~1e-6
# level if the integrand is altered).
RTOL = 1e-12


def test_i_scalar_1d_matches_computation() -> None:
    computed = _compute_i_scalar_dynamic(crossing_number=5)
    assert np.isclose(constants.I_SCALAR_1D, computed, rtol=RTOL), (
        f"I_SCALAR_1D literal {constants.I_SCALAR_1D!r} does not match "
        f"computation {computed!r}.  If the Faddeev-Skyrme integrand or "
        f"coupling has changed, update the literal in core/constants.py."
    )


@pytest.mark.parametrize("crossing_number", constants.TORUS_KNOT_CROSSING_NUMBERS)
def test_baryon_ladder_matches_computation(crossing_number: int) -> None:
    computed = _compute_baryon_ladder()
    assert crossing_number in constants.BARYON_LADDER, f"BARYON_LADDER missing entry for c={crossing_number}"
    stored = constants.BARYON_LADDER[crossing_number]
    fresh = computed[crossing_number]
    for key in ("i_scalar", "ratio", "mass_mev"):
        assert np.isclose(stored[key], fresh[key], rtol=RTOL), (
            f"BARYON_LADDER[{crossing_number}][{key!r}] literal {stored[key]!r} "
            f"does not match computation {fresh[key]!r}.  If the Faddeev-Skyrme "
            f"integrand or coupling has changed, update the literal in "
            f"core/constants.py."
        )


def test_proton_mass_consistency() -> None:
    """``PROTON_ELECTRON_RATIO`` is derived from ``I_SCALAR_1D`` algebraically.

    Cross-check that the algebraic derivation in constants.py matches the
    ratio reported in BARYON_LADDER[5].  This catches the case where one
    literal is updated and the other is forgotten.
    """
    assert np.isclose(
        constants.PROTON_ELECTRON_RATIO,
        constants.BARYON_LADDER[5]["ratio"],
        rtol=RTOL,
    ), (
        f"PROTON_ELECTRON_RATIO ({constants.PROTON_ELECTRON_RATIO!r}) and "
        f"BARYON_LADDER[5]['ratio'] ({constants.BARYON_LADDER[5]['ratio']!r}) "
        f"disagree — both depend on I_SCALAR_1D and must be updated together."
    )
