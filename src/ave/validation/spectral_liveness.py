"""(e) spectral-liveness — RE-EXPORT of the existing first-class module.

ENGINE-HARDENING ARC item 2(e). The spectral-liveness diagnostic already lives at
`ave.solvers.spectral_liveness` (7 keepers `test_spectral_liveness.py`; the
Step-3.8a readout-liveness gate operationalized 2026-07-03, capability-map §8b.4).
This module RE-EXPORTS it so a driver can pull all five validation guards from one
`ave.validation` namespace — it does NOT duplicate the computation (single source
of truth stays in `ave.solvers.spectral_liveness`).

Usage:
    from ave.validation import spectral_liveness, localized_eigenmode
    live = spectral_liveness(seed, L)          # read nullspace-energy fraction
    assert live.live_energy_fraction > 0.5     # seed is mostly in the live subspace
    u, lam, frac = localized_eigenmode(L)       # a route-1 positive-control mode
"""

from __future__ import annotations

from ave.solvers.spectral_liveness import (
    SpectralLiveness,
    localized_eigenmode,
    project_out_nullspace,
    spectral_liveness,
)

__all__ = [
    "SpectralLiveness",
    "spectral_liveness",
    "localized_eigenmode",
    "project_out_nullspace",
]
