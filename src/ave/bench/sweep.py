"""sweep.py — co-vary AVE-vs-SM/null divergence sweep.

FACTORED FROM: AVE-Bench-VacuumMirror/scripts/analytical_gamma_v_sweep.py
  (the gamma_bragg_2d vs gamma_sm_eh_kerr co-vary block, run_sweep()).

THE LOAD-BEARING INVARIANT (this contract IS the no-strawman rule R1):
  The SM/null callable MUST be evaluated over the SAME x_grid and through the
  same integral/profile machinery as the AVE callable. In the exemplar,
  gamma_bragg_2d (AVE) and gamma_sm_eh_kerr (SM) share the IDENTICAL Born
  integration (gamma_single_tip / gamma_sm_single_tip use the same z-grid, same
  K0, same e^(2ik0z) profile, same N^2 Bragg gain) — discrimination is purely
  delta_eps_AVE vs delta_eps_SM. See analytical_gamma_v_sweep.py:110-119
  docstring: "Uses the SAME Born-integration and same tip field profile as the
  AVE prediction".

  run_divergence_sweep takes TWO callables + ONE shared grid. It deliberately
  provides NO API path to pass a pre-baked independent SM curve (an array) —
  that would let a caller manufacture a strawman by evaluating the SM null on a
  different grid / different integral than the AVE prediction. The only way to
  supply the SM/null is as a callable that this function drives over the SAME
  x_grid the AVE callable is driven over.

This is also the phase-space-coordinate discipline (A46): AVE and SM are
measured in matching coordinates because they ride the same x_grid through the
same profile.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np

# No SI literals needed here — this module orchestrates caller-supplied
# substrate-native callables; the physics constants live inside those callables
# (which import from ave.core.constants per the exemplar).

# Floor for the divergence ratio so a zero/near-zero SM null does not produce
# inf/NaN. Matches the exemplar's np.maximum(gamma_sm, 1e-40) guard
# (analytical_gamma_v_sweep.py:147-148).
_RATIO_FLOOR: float = 1e-40


@dataclass(frozen=True)
class DivergenceSweepResult:
    """Structured result of a co-varied AVE-vs-SM/null divergence sweep.

    Attributes
    ----------
    x : np.ndarray
        The shared sweep grid (e.g. V_gap values). BOTH ave and sm were
        evaluated on exactly this grid.
    ave : np.ndarray
        AVE callable evaluated over x.
    sm : np.ndarray
        SM/null callable evaluated over THE SAME x.
    ratio : np.ndarray
        Divergence map = ave / max(sm, floor). The discrimination ratio.
    """

    x: np.ndarray
    ave: np.ndarray
    sm: np.ndarray
    ratio: np.ndarray

    def as_dict(self) -> dict:
        """Return the result as a plain dict {x, ave, sm, ratio}."""
        return {"x": self.x, "ave": self.ave, "sm": self.sm, "ratio": self.ratio}

    @property
    def max_divergence(self) -> float:
        """The peak discrimination ratio over the grid."""
        return float(np.max(self.ratio))


def run_divergence_sweep(
    ave_fn: Callable[[float], float],
    sm_fn: Callable[[float], float],
    x_grid: np.ndarray,
    *,
    ratio_floor: float = _RATIO_FLOOR,
) -> DivergenceSweepResult:
    """Co-vary an AVE prediction and an SM/null prediction over ONE shared grid.

    Parameters
    ----------
    ave_fn : callable(x) -> float
        The AVE prediction as a function of the sweep variable (e.g. a
        partial of gamma_bragg_2d binding R_tip/d_gap/N, leaving V_gap free).
    sm_fn : callable(x) -> float
        The SM/null prediction as a function of THE SAME sweep variable, driven
        over THE SAME grid through (by contract) the same integral/profile
        machinery as ave_fn. This MUST be a callable, never a pre-baked array —
        the callable signature is what enforces same-grid evaluation and
        forbids strawman SM curves (the no-strawman rule R1).
    x_grid : np.ndarray
        The shared sweep grid. Both ave_fn and sm_fn are evaluated at every
        point of this exact grid.
    ratio_floor : float, optional
        Lower clamp on the SM denominator to avoid inf/NaN when the null is
        zero. Defaults to 1e-40 (matches the exemplar's np.maximum guard).

    Returns
    -------
    DivergenceSweepResult
        {x, ave, sm, ratio} where ratio = ave / max(sm, ratio_floor).

    Notes
    -----
    The exemplar's discrimination ratio (analytical_gamma_v_sweep.py:147):
        discrim = gamma_ave / np.maximum(gamma_sm, 1e-40)
    is reproduced exactly here, generalized to arbitrary callables + grid.
    """
    x = np.asarray(x_grid, dtype=float)
    if x.ndim != 1:
        raise ValueError(f"x_grid must be 1-D; got shape {x.shape}")
    if x.size == 0:
        raise ValueError("x_grid must be non-empty")

    # Evaluate BOTH callables over THE SAME grid. This loop is the no-strawman
    # contract made operational: there is no branch that consumes a pre-baked
    # SM array — sm_fn is driven point-for-point over the identical x.
    ave = np.array([float(ave_fn(xi)) for xi in x], dtype=float)
    sm = np.array([float(sm_fn(xi)) for xi in x], dtype=float)

    ratio = ave / np.maximum(sm, ratio_floor)

    return DivergenceSweepResult(x=x, ave=ave, sm=sm, ratio=ratio)
