"""PLANTED SABOTAGE ARTIFACT (x40 S2b) — NOT PHYSICS. DO NOT REUSE.

This file DELIBERATELY violates the x40 anti-install gate (G-E) by the SLIP the
adversarial review found: it imports a forbidden dimensional-constant NAME
(OMEGA_C), ALIASED, from a NON-constants module — a form the original
module-path-only ImportFrom check missed. It exists only so
`test_x40_ring_closure.py` can prove that `scan_for_dimensional_constants` now
FIRES on this aliased re-export (a forbidden name is forbidden wherever it is
re-exported from).

This file is NEVER imported or executed by the physics; only its AST is scanned.
The import target need not even resolve at runtime — the STATIC scan flags the
intent regardless.
"""

from __future__ import annotations

from ave.core.chiral_lattice import OMEGA_C as w  # noqa: F401  (planted G-E slip)


def bad_scale() -> float:
    """Illegitimately installs a dimensional scale via an aliased re-export."""
    return 1.0 / w
