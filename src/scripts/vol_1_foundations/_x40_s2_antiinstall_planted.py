"""PLANTED SABOTAGE ARTIFACT (x40 S2) — NOT PHYSICS. DO NOT REUSE.

This file DELIBERATELY violates the x40 anti-install gate (G-E): it imports a
dimensional constant (OMEGA_C) from ave.core.constants and uses it to set a
scale. It exists for exactly one reason — so `test_x40_ring_closure.py` can
prove that `scan_for_dimensional_constants` FIRES on a planted violation (P11:
a gate that cannot fail is not a gate). It is never imported by the physics
driver and is never executed by the physics; only its AST is scanned.

If G-E did NOT flag this file, the anti-install gate would be decorative. The
real driver (x40_ring_closure_transient.py) is dimensionless end-to-end and its
self-scan is empty.
"""

from __future__ import annotations

from ave.core.constants import OMEGA_C  # noqa: F401  (planted G-E violation)


def bad_scale() -> float:
    """Illegitimately installs a dimensional scale into the dimensionless split."""
    return 1.0 / OMEGA_C  # a scale the substrate-native split must NOT depend on
