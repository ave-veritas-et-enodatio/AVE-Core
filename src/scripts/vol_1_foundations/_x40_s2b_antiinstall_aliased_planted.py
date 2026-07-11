"""PLANTED SABOTAGE ARTIFACT (x40 S2b) — NOT PHYSICS. DO NOT REUSE.

This file DELIBERATELY violates the x40 anti-install gate (G-E) by the SLIP the
adversarial review found: it imports a forbidden dimensional-constant NAME
(L_NODE), ALIASED, from a NON-constants module — a form the original
module-path-only ImportFrom check missed. It exists only so
`test_x40_ring_closure.py` can prove that `scan_for_dimensional_constants` now
FIRES on this aliased re-export (a forbidden name is forbidden wherever it is
re-exported from).

This file is NEVER imported or executed by the physics; only its AST is scanned.
L_NODE is a GENUINE forbidden re-export from a non-constants module
(chiral_lattice.py:41), so this import RESOLVES — it passes the repo
import-resolution smoke gate — while the name-keyed G-E scanner still flags the
forbidden NAME. That is the faithful form of the aliased-re-export slip.
"""

from __future__ import annotations

from ave.core.chiral_lattice import L_NODE as w  # noqa: F401  (planted G-E slip)


def bad_scale() -> float:
    """Illegitimately installs a dimensional scale via an aliased re-export."""
    return 1.0 / w
