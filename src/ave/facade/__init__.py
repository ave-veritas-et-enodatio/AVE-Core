"""ave.facade — the regime-dispatch facade for the fully-dynamic unified AVE engine.

P0 scaffold (branch engine/p0-unified-dynamic). Design note:
research/2026-06-25_unified-engine-P0-design.md.

The facade is a thin DISPATCH + WIRING layer over the certified cores (Rule-14
anti-rebuild): it REUSES coupled_cage_winding / native_cage_imex /
chiral_lattice{,_vector,_dynamics} / charge_quantization / graded_vacuum_network
VERBATIM — it reimplements no stencil, stepper, eigensolver, kernel, or winding
reader. It does NOT carry master_equation_fdtd (Cartesian-grid artifact) or
fdtd_3d (μ-on-static-|B| bug).

THE SINGLE-GRID BET (Grant-ratified): the 6 DOF/node (3 translation u ↔ E/ε₀ +
3 Cosserat micro-rotation ω ↔ B/μ₀) AND the A1 bulk-dilatation scalar all live on
the SAME native K4 graph; the A1 scalar is a NODE-ATTACHED field, NOT a second
grid. If this works the two-grid Stage-3 bridge dissolves.
"""

from __future__ import annotations

from .unified_engine import (
    Regime,
    SingleGridState,
    UnifiedEngine,
    UnifiedEngineConfig,
)

__all__ = [
    "Regime",
    "SingleGridState",
    "UnifiedEngine",
    "UnifiedEngineConfig",
]
