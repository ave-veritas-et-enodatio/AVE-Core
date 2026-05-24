"""
Offline recomputation helpers for constants stored as literals in
``ave.core.constants``.

These functions reproduce the values that were historically computed at
``ave.core.constants`` import time via ``scipy.optimize`` (the 1D
Faddeev-Skyrme scalar trace and the (2,q) torus-knot baryon ladder).
The computed values are now stored as literals in ``constants.py`` so that
``import ave.core.constants`` is fast and free of any dependency on physics
modules.

This module exists solely to support the verifying tests
(``src/tests/test_constants_literals.py``) and any developer workflow that
needs to recompute the literals after a physics change. It is private:
production code must read the literals from ``ave.core.constants`` directly.

If a future physics change shifts the computed values, the verifying tests
will fail and the literals in ``constants.py`` must be updated to match the
new computation.
"""

from __future__ import annotations

from ave.core.constants import (
    C_0,
    CROSSING_NUMBER_PROTON,
    HBAR,
    KAPPA_FS,
    M_E,
    P_C,
    TORUS_KNOT_CROSSING_NUMBERS,
    V_TOROIDAL_HALO,
    e_charge,
)


def _compute_i_scalar_dynamic(crossing_number: int = CROSSING_NUMBER_PROTON) -> float:
    """Recompute ``I_SCALAR_1D`` from the Faddeev-Skyrme solver.

    Args:
        crossing_number: Torus knot crossing number.  Default 5 (proton).

    Returns:
        The minimized 1D Faddeev-Skyrme scalar trace for the given knot.
    """
    # Local import: faddeev_skyrme imports from constants, so this helper must
    # not be reached during constants module init.  As a private test-time
    # utility called only after constants is fully initialized, this is safe.
    from ave.topological.faddeev_skyrme import TopologicalHamiltonian1D

    solver = TopologicalHamiltonian1D(
        node_pitch=HBAR / (M_E * C_0),  # = L_NODE
        scaling_coupling=KAPPA_FS,
    )
    return solver.solve_scalar_trace(crossing_number=crossing_number)


def _compute_baryon_ladder() -> dict[int, dict[str, float]]:
    """Recompute the full (2,q) torus knot baryon resonance ladder.

    Returns:
        Mapping ``c -> {"i_scalar", "ratio", "mass_mev"}`` for each crossing
        number ``c`` in ``TORUS_KNOT_CROSSING_NUMBERS``.
    """
    kg_to_mev = C_0**2 / (e_charge * 1e6)
    ladder: dict[int, dict[str, float]] = {}
    for c in TORUS_KNOT_CROSSING_NUMBERS:
        i_scalar = _compute_i_scalar_dynamic(crossing_number=c)
        x_core = i_scalar / (1.0 - V_TOROIDAL_HALO * P_C)
        ratio = x_core + 1.0
        mass_mev = ratio * M_E * kg_to_mev
        ladder[c] = {
            "i_scalar": i_scalar,
            "ratio": ratio,
            "mass_mev": mass_mev,
        }
    return ladder
