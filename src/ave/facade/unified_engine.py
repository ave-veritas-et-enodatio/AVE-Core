"""The regime-dispatch facade — single-grid 6-DOF unified AVE engine (P0).

Design note: research/2026-06-25_unified-engine-P0-design.md.

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS IS (and is NOT)
═══════════════════════════════════════════════════════════════════════════════
A thin DISPATCH + WIRING facade over the certified cores. P0 = the MEDIUM-
scaffold (validate-on-known), NOT a self-formation search. The falsified bulk
self-trap (S3 DISPERSE / #415 / #59) is CLOSED-NEGATIVE and the self-formation
slot is BARRED — this facade never re-runs it.

Rule-14 anti-rebuild: every role is filled by a certified core, wired verbatim:
  * native K4 stencil + unitary CN/Cayley stepper + Hermitian A1↔ω port
        → ave.solvers.coupled_cage_winding
  * native sparse Grad/Div + IMEX-implicit 1/S cage + energy gate
        → ave.solvers.native_cage_imex
  * L0 chiral medium + scatter-connect TLM (the srs z=3 free-mode carrier)
        → ave.core.chiral_lattice{,_vector,_dynamics}
  * integer winding reader Link(∂Ω,F) ∈ ℤ
        → ave.topological.charge_quantization
  * α-clean (1−A²) saturation kernel
        → ave.solvers.graded_vacuum_network
EXCLUDED: master_equation_fdtd (Cartesian artifact), fdtd_3d (μ-on-static-|B| bug).

═══════════════════════════════════════════════════════════════════════════════
THE SINGLE-GRID 6-DOF/NODE STATE (the high-leverage bet)
═══════════════════════════════════════════════════════════════════════════════
On ONE native K4 graph, per node:
  u  ∈ R³   — 3 translational DOF ↔ E/ε₀ (2 transverse = photon; 1 longitudinal
              = the A1 dilatation MASS-"3" projection)
  ω  ∈ R³   — 3 Cosserat micro-rotation DOF ↔ B/μ₀ (the (2,3) winding = charge)
  a_A1 ∈ C  — the A1 bulk-dilatation breather as a NODE-ATTACHED scalar field on
              the SAME K4 graph (the bet that dissolves the two-grid bridge)

The A1 scalar is NEVER wired into the (V_inc,V_ref) transverse phasor
(master-equation.md:20; genesis-24 double-count guard). u and ω are SEPARATELY
conserved grades.

α-CLEAN: κ̃=6/5 (winding host), import-guard triad re-asserted at construction.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

import numpy as np

# ─────────────────────────────────────────────────────────────────────────────
# α-leak guard triad (import-time) — the SAME triad as the certified cores
# (graded_vacuum_network.py:111-114, _spine.py:76-80, _winding_host.py:69-77).
# An α-carrier leaking into the facade fails the import HERE (the leak is the
# signal; do NOT patch around it).
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "α-leak: ALPHA must NOT be imported into the facade"
assert "ALPHA_COLD_INV" not in globals(), "α-leak: ALPHA_COLD_INV (≈137) must NOT be imported"
assert "Q_TANK" not in globals(), "α-leak: Q_TANK (=1/α) must NOT be imported into the facade"
assert "ELECTRON" not in globals(), "α-leak: the ELECTRON instance must NOT be imported"
assert "RHO_BULK" not in globals(), "second-leak: the bare RHO_BULK magnitude must NOT be imported"
assert "V_SNAP" not in globals(), "α-leak: V_SNAP must NOT be on the chord path"
assert "KAPPA_CHIRAL_ELECTRON" not in globals(), "α-leak: KAPPA_CHIRAL_ELECTRON (=α·κ̃) forbidden"

_FACADE_FORBIDDEN = (
    "ALPHA", "ALPHA_COLD_INV", "Q_TANK", "ELECTRON", "RHO_BULK",
    "V_SNAP", "KAPPA_CHIRAL_ELECTRON",
)


class Regime(Enum):
    """Regime-dispatch selector. P0 exercises LINEAR_FREE; the saturated/coupled
    regimes are WIRED (the cores exist) but their dynamic exercise is P1+."""

    LINEAR_FREE = "linear_free"        # S=1, all free modes (P0 validate-on-known)
    SATURATED_CAGE = "saturated_cage"  # A1 cage (native_cage_imex), Op14 active (P1+)
    COUPLED_WINDING = "coupled_winding"  # A1↔ω coupled (coupled_cage_winding) (P1+)


@dataclass
class SingleGridState:
    """The single-grid 6-DOF/node state on ONE native K4 graph.

    Two grid CARRIERS coexist in P0 (both native-K4-family, see the single-grid
    verdict in the design note):
      * the srs TLM net (degree z=3) carries the FREE transverse modes (photon)
        as port fields — `tlm_vector` (N_node, 3, 2) and `tlm_scalar` (N_node, 3);
      * the diamond-K4 N³ node array (TETRA_OFFSETS stencil) carries the A1
        node-field `a_A1` and the ω micro-rotation field `omega` for the cage /
        winding sectors.
    The single-grid bet is that the A1 SCALAR rides the SAME diamond-K4 node set
    as ω (a per-node attribute), NOT a separate grid — verified by the energy
    gate staying green end-to-end on the shared node set.
    """

    N: int                                  # diamond-K4 cube edge (cage/winding carrier)
    # — the diamond-K4 node-field sector (A1 scalar + ω micro-rotation) —
    a_A1: np.ndarray = field(default=None)   # (N,N,N) complex — A1 dilatation node-field
    omega: np.ndarray = field(default=None)  # (N,N,N,3) real  — Cosserat micro-rotation
    # — translational u ↔ E/ε₀ (3 DOF; 2 transverse + 1 longitudinal) —
    u: np.ndarray = field(default=None)      # (N,N,N,3) real  — translational DOF
    # — the srs TLM free-mode carrier (photon) — held as a handle, not duplicated —
    tlm_handle: object = field(default=None)

    def __post_init__(self):
        N = self.N
        if self.a_A1 is None:
            self.a_A1 = np.zeros((N, N, N), dtype=np.complex128)
        if self.omega is None:
            self.omega = np.zeros((N, N, N, 3), dtype=np.float64)
        if self.u is None:
            self.u = np.zeros((N, N, N, 3), dtype=np.float64)


@dataclass(frozen=True)
class UnifiedEngineConfig:
    """Frozen facade config. Defaults mirror the certified cores' frozen defaults
    (native_cage_imex v14: N=24, dx=0.5, pml=4, exponent=0.5; srs L for the free-
    mode carrier). α-FREE.
    """

    regime: Regime = Regime.LINEAR_FREE
    # diamond-K4 cage / winding carrier (native_cage_imex defaults)
    N: int = 24
    dx: float = 0.5
    V_yield: float = 1.0
    pml_thickness: int = 4
    exponent: float = 0.5               # Op14 √S primary (carried; dormant at P0)
    S_min: float = 1e-3
    A_cap: float = 0.999
    # srs free-mode carrier (chiral_lattice)
    srs_L: int = 8                      # srs supercell edge (free-mode carrier)
    enantiomorph: str = "right"
    # winding seed geometry (the (2,3) torus)
    R: float = 7.0
    r: float = 2.3


class UnifiedEngine:
    """The regime-dispatch facade. Wires the certified cores; reimplements none.

    P0 skeleton — the per-role wiring methods are appended incrementally
    (one core per commit). At construction the α-leak guard triad is re-asserted
    (belt-and-suspenders over the import-time triad above).
    """

    def __init__(self, cfg: UnifiedEngineConfig | None = None):
        self.cfg = cfg or UnifiedEngineConfig()
        self.state = SingleGridState(N=self.cfg.N)
        self._assert_alpha_clean()
        # lazily-built core handles (wired in the per-role methods)
        self._medium = None
        self._a1_cage = None
        self._coupled = None

    def _assert_alpha_clean(self) -> None:
        """Re-assert the import-guard triad in THIS module's globals at
        construction (the leak is the signal; do NOT patch around it)."""
        g = globals()
        for sym in _FACADE_FORBIDDEN:
            assert sym not in g, (
                f"α-leak: forbidden symbol '{sym}' reachable in the facade globals "
                f"— the facade chord path must carry NO α-carrier."
            )

