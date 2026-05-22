"""
HelicityObserver — track Cosserat-ω Beltrami helicity along propagation axis.

Companion observer for Path A (CosseratBeltramiSource + DarkWakeObserver)
chiral validation. Records h_local = ω·(∇×ω) / (|ω|·|∇×ω|) at each cadence
step, sliced along the chosen propagation axis.

Reuses _beltrami_helicity from cosserat_field_3d.py (corpus-canonical
formula per doc 54_ §6 line 220, regularized with ε=1e-12).

Output history per record_cadence step:
  - h_field: (N,) array — helicity along propagation axis at transverse center
  - h_at_source: scalar — helicity at source slab
  - h_max, h_min, h_mean over interior

References:
  - cosserat_field_3d.py:358-376 — _beltrami_helicity definition
  - vacuum_engine.py:791-972 — CosseratBeltramiSource (handedness="RH"/"LH")
  - doc 20 chirality projection sub-theorem (κ_chiral = 1.2·α)
  - doc 54 §6 (asymmetric μ/ε saturation, h_local role)
"""

from __future__ import annotations

from typing import Any

import numpy as np

try:
    from ave.topological.cosserat_field_3d import _beltrami_helicity

    _has_jax = True
except ImportError:
    _has_jax = False

from ave.topological.vacuum_engine import Observer


class HelicityObserver(Observer):
    """Sample Beltrami helicity h_local along propagation axis.

    Args:
        cadence: record every N outer steps
        propagation_axis: 0=x, 1=y, 2=z — slice direction
    """

    def __init__(self, cadence: int = 3, propagation_axis: int = 0):
        if propagation_axis not in (0, 1, 2):
            raise ValueError(f"propagation_axis must be 0/1/2, got {propagation_axis}")
        super().__init__(cadence=cadence)
        self.propagation_axis = int(propagation_axis)

    def _capture(self, engine: Any) -> dict[str, Any]:
        """Compute h_local from engine.cos.omega and return slice + diagnostics."""
        omega = engine.cos.omega  # shape (N, N, N, 3)
        dx = float(engine.cos.dx)

        # Compute helicity field. _beltrami_helicity is JAX; works on numpy too.
        h_field_full = _beltrami_helicity(omega, dx)
        h_field = np.asarray(h_field_full)  # convert from jax if needed

        # Slice along propagation axis at transverse center
        N = engine.cos.nx
        center = N // 2
        if self.propagation_axis == 0:
            h_axis = h_field[:, center, center]
        elif self.propagation_axis == 1:
            h_axis = h_field[center, :, center]
        else:
            h_axis = h_field[center, center, :]

        # Mask PML region for interior diagnostics
        pml = getattr(engine.cos, "pml_thickness", 0)
        if pml > 0 and 2 * pml < N:
            interior = h_field[pml:-pml, pml:-pml, pml:-pml]
        else:
            interior = h_field

        h_max = float(interior.max()) if interior.size > 0 else 0.0
        h_min = float(interior.min()) if interior.size > 0 else 0.0
        h_mean = float(interior.mean()) if interior.size > 0 else 0.0
        h_abs_max = max(abs(h_max), abs(h_min))

        return {
            "t": engine.time,
            "h_axis": np.asarray(h_axis).copy(),
            "h_max": h_max,
            "h_min": h_min,
            "h_mean": h_mean,
            "h_abs_max": h_abs_max,
        }
