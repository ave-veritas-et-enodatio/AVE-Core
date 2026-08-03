"""Instrument pin for the Route-B Petermann C2 driver.

Pins the numerical output of
``src/scripts/vol_2_subatomic/simulate_g2_direction2.py`` so the retardation
quadrature cannot silently regress. Added 2026-08-03 by the core-side
instrument audit (PR #857 amendment lane, cross-session per the 2026-08-03
epic->core handoff).

WHY THIS FILE EXISTS
--------------------
The driver had ZERO test/CI coverage. That is how a 97 ppm instrument error
survived two months: the retardation was applied by rolling a ``np.gradient``
array by a TRUNCATED integer index (``int(tau_retard / dt) % n_t``), so the
retardation actually applied was ``tau_eff = 0.999997216`` at the banked
n_t = 2e6 rather than the asserted ``tau = 1``. With ``dC2/dtau = -11.4555``
that is ``+3.19e-5`` in C2, and a +-1 change in ``n_t`` moved the output
92 ppm. Nothing in the repo would have noticed.

WHAT CLASS OF TEST THIS IS
--------------------------
Per ``consistency-vs-emergence``: this is an **instrument / numerical-identity
pin**, NOT a physics claim and NOT an emergence result. It asserts only that
the quadrature returns the same number it returned when the fix landed, and
that the number does not depend on the grid. It takes NO position on:

  * the factor-2 normalization question (leaf :47 vs :48 -- ROUTED to Grant,
    open as of this file's creation); the pinned values below carry the
    driver's shipped ``2/(pi*alpha)`` convention, whichever way that resolves;
  * whether ``tau_retard = 1/omega_C`` is derived (it is ASSERTED -- see
    ``research/2026-05-31_FT-alpha-reextraction-direction-2_result.md``:126);
  * the Stage-2 n_q-additivity postulate (RESOLVED NEGATIVE 2026-05-31).

A green run here means the instrument is stable, not that the physics is right.
"""

from __future__ import annotations

import importlib.util
import os
from math import pi

import numpy as np
import pytest

_SCRIPTS = os.path.join(os.path.dirname(__file__), "..", "scripts", "vol_2_subatomic")


def _load(name):
    path = os.path.join(_SCRIPTS, name)
    spec = importlib.util.spec_from_file_location(name.replace(".py", ""), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


drv = _load("simulate_g2_direction2.py")

# --- Pinned values -----------------------------------------------------------
# Both produced by the exact-retardation instrument at the fix commit, and both
# n_t-invariant to 13 digits over n_t in [1e5, 4e6].
C2_SYMMETRIC_PIN = -0.341635434  # Stage 1, delta = 0, parameter-free
C2_SALIENCY_PIN = -0.328459258  # Stage 2, delta = -3*alpha/2 (postulate-conditional)

# STATED TOLERANCE, and why this number:
#   * observed n_t-to-n_t spread of the fixed instrument .............. 2.8e-16
#   * the defect this pin exists to catch (97 ppm at n_t=2e6) ......... 3.2e-05
# 1e-9 sits ~7 orders above the reproducibility floor (so platform/BLAS float
# variation cannot red the gate) and ~5 orders below the defect (so the defect
# class cannot pass). It corresponds to 3e-3 ppm of C2 -- far finer than any
# ppm-scale question the corpus asks of this driver.
ABS_TOL = 1e-9

# The fixed instrument is grid-independent by construction; anything above
# float-noise here means a grid-quantized retardation has come back.
NT_INVARIANCE_TOL = 1e-12

DELTA_SALIENCY = -1.5 * drv.ALPHA


def _c2(delta, n_t):
    return drv.correlation_to_A2(drv.route_b_correlation(delta=delta, tau_retard=1.0, n_t=n_t))


def test_analytic_dv2_matches_numerical_derivative():
    """The closed form is COUPLED to the current definitions; pin the coupling.

    ``_dv2_dt_analytic`` hard-codes dV^2/dt for i_d = cos(2t), i_q = sin(3t).
    If the (p, q) winding is ever changed in ``route_b_correlation`` without
    changing the closed form, every other assertion in this file would keep
    passing against a stale derivative. This is the guard for that.
    """
    n = 2_000_000
    t = np.linspace(0.0, 2.0 * pi, n, endpoint=False)
    dt = t[1] - t[0]
    v_sq = np.cos(2.0 * t) ** 2 + np.sin(3.0 * t) ** 2
    num = np.gradient(v_sq, dt)
    ana = drv._dv2_dt_analytic(t)
    # INTERIOR only. np.gradient falls back to a ONE-SIDED first-order stencil
    # at index 0 and -1, and the array here is periodic, so both endpoints are
    # wrong by ~dt/2 = 1.57e-6 * 10 = 1.6e-5 -- a second (much smaller) defect
    # of the same class in the pre-2026-08-03 driver, which fed np.gradient a
    # periodic array with no wrap. Its weight in the cycle mean is ~1e-14, i.e.
    # ~9 orders below the 97 ppm truncation defect; recorded, not headlined.
    # The 2nd-order interior stencil is accurate to ~dt^2 ~ 1e-11.
    assert np.max(np.abs(num[1:-1] - ana[1:-1])) < 1e-8


def test_c2_symmetric_stage1_pin():
    """Stage-1 (parameter-free) symmetric Route B."""
    assert _c2(0.0, 2_000_000) == pytest.approx(C2_SYMMETRIC_PIN, abs=ABS_TOL)


def test_c2_saliency_stage2_pin():
    """Stage-2 saliency closure. Postulate-conditional physics; pinned as an
    instrument output only."""
    assert _c2(DELTA_SALIENCY, 2_000_000) == pytest.approx(C2_SALIENCY_PIN, abs=ABS_TOL)


def test_c2_is_nt_invariant():
    """The retardation must not be quantized to the grid.

    Includes the +-1 grid-count pair (2e6 / 2e6+1) that exposed the original
    defect: under the truncated-index shift those two differed by 92 ppm
    (-0.328427365 vs -0.328457626). Under exact retardation they are equal to
    float noise.
    """
    grids = [100_000, 250_000, 1_000_000, 2_000_000, 2_000_001, 4_000_000]
    vals = [_c2(DELTA_SALIENCY, n) for n in grids]
    assert max(vals) - min(vals) < NT_INVARIANCE_TOL, dict(zip(grids, vals))
    for n, v in zip(grids, vals):
        assert abs(v - C2_SALIENCY_PIN) < ABS_TOL, (n, v)


def test_parity_zeros_survive_the_fix():
    """Corpus-recorded structural check (leaf 'Numerical robustness' section):
    the correlation is exactly zero at the symmetric retardations
    tau in {pi/2, pi, 3pi/2, 2pi} by parity. The repair must not disturb it."""
    for tau in (pi / 2, pi, 3 * pi / 2, 2 * pi):
        c = drv.route_b_correlation(delta=0.0, tau_retard=tau, n_t=200_000)
        assert abs(c) < 1e-15, (tau, c)
