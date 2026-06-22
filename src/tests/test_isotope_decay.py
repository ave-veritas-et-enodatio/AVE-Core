"""Regression gate: pin the topological Q-factors quoted in the isotope-decay
narrative (Vol 6 Ch 1, ``radioactive-decay-impedance.md``) and rendered by
``plot_isotope_decay.py``.

These Q-values (3H, 3He, 4He, 8Be) are stated in the manuscript + KB and are the
headline of the isotope-decay figure. They silently drifted once — the leaf carried
``3.20 -> 19.52`` while the engine had moved to ``3.27 -> 19.04`` — because nothing
pinned them. This test asserts the current engine output so any future drift fails
loudly and forces a coordinated re-baseline of the prose + figure.

(This file previously generated a ``tests/outputs`` PNG that annotated the solver's
own mass-defect energies — quantities the framework does not derive. That plotting
side-effect is removed; ``plot_isotope_decay.py`` owns the manuscript figure.)
"""

import numpy as np

from scripts.vol_6_periodic_table.simulations.simulate_element import (
    M_N_RAW,
    M_P_RAW,
    calculate_topological_mass,
    get_nucleon_coordinates,
)


def compute_topology(Z: int, A: int) -> tuple[float, float, float]:
    """Return (theoretical mass, binding energy, topological Q-factor) for (Z, A)."""
    N = A - Z
    raw_mass = (Z * M_P_RAW) + (N * M_N_RAW)
    theo_mass = calculate_topological_mass(Z, A)
    binding_energy = raw_mass - theo_mass

    nodes = get_nucleon_coordinates(Z, A)
    if len(nodes) > 1:
        com = np.mean(nodes, axis=0)
        max_radius = max(np.linalg.norm(np.array(n) - com) for n in nodes)
    else:
        max_radius = 0.85

    effective_radius = max_radius if max_radius > 0.1 else 0.85
    q_factor = (binding_energy / effective_radius) if binding_energy > 0 else 1.0
    return theo_mass, binding_energy, q_factor


def test_isotope_decay_q_factors():
    """Pin the engine Q-factors quoted in the isotope-decay narrative + figure.

    Tolerance 0.05 catches every historical drift (tritium 3.20->3.27 = 0.07,
    He-3 19.52->19.04 = 0.48) with ~14x margin over the 2-dp rounding gap; the
    engine is deterministic so there is no run-to-run noise. On failure it moved:
    re-baseline ``01_computational.tex``, ``radioactive-decay-impedance.md``, the
    ``claim-quality.md`` Q-set, and the figure (via ``plot_isotope_decay.py``) in
    lockstep.
    """
    expected = {
        (1, 3): 3.27,   # Tritium     — unstable, low-Q (beta-decay precursor)
        (2, 3): 19.04,  # Helium-3    — stable, high-Q (beta-decay product)
        (2, 4): 19.19,  # Helium-4    — alpha-node Q
        (4, 8): 4.63,   # Beryllium-8 — broken-bridge, low-Q
    }
    for (Z, A), q_exp in expected.items():
        _, _, q = compute_topology(Z, A)
        assert abs(q - q_exp) < 0.05, (
            f"Q-factor drift for (Z={Z}, A={A}): engine={q:.4f}, quoted={q_exp}. "
            "Re-baseline the isotope-decay prose + figure in lockstep."
        )
