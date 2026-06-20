"""Node-Scattering Multiplicity / Containment Gate — BEDROCK (scope b, Fork A).

Prereg: research/2026-06-20_node-scattering-containment-gate_prereg.md
        (frozen commit f87914fa, the FIRST commit of this branch).

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS MODULE IS (and is NOT)
═══════════════════════════════════════════════════════════════════════════════
GOAL  : test whether the vacuum's CONFINEMENT MULTIPLICITY is set by the lattice's
        NODE VALENCE. The degree-3 chiral srs net and the degree-4 diamond net give
        STRUCTURALLY DISTINCT scattering operators S_n = (2/n)J - I whose DIFFERENTIAL
        (-1) eigenspace has multiplicity n-1 (2 for srs, 3 for diamond).

SCOPE : (b) ONLY = Fork A (the multiplicity/sector test). Forks B/C/D are DEFERRED
        (prereg §7; Grant's bulk-saturation framing for B carried there).

BEDROCK (Stage 1, THIS FILE's load-bearing content): the operator is assembled from
        the lattice's OWN bond-graph CONNECT map (chiral_lattice.scatter_matrix(n) +
        connect_index / build_srs_net / build_diamond_net), so n=3 (srs, degree-3) and
        n=4 (diamond, degree-4) are STRUCTURALLY DIFFERENT operators -- NOT the dense
        TETRA_OFFSETS cube that graded_vacuum_network.py hardwires. This is PURE LINEAR
        ALGEBRA: no dynamics, no core, no boundary.

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-NATIVE-CHECK (walked BEFORE any numerical code, per operating principle 1)
═══════════════════════════════════════════════════════════════════════════════
  * K4 / graph   : the operator is the Op5 shunt-junction scatter S_n = (2/n)J - I
                   (chiral_lattice.py:81-102) composed with the directed-edge CONNECT
                   permutation from connect_index() (chiral_lattice.py:133-147). Built
                   FROM the graph, never imposed on a Cartesian grid. The dense
                   TETRA_OFFSETS cube (graded_vacuum_network.py) is the BUG this fixes.
  * Cosserat     : the winding sector (CHARGE-3) is validated via charge_quantization
                   (omega-grade only, A1-perp-T2 honoured). NEVER wired into the A1
                   (V_inc, V_ref) phasor (master-equation.md:20; genesis-24 caution).
  * phase vs real: S_n eigenvectors live in n-PORT space; A1/Cosserat grades in
                   real-space. The port->grade map is the bond-direction embedding
                   bond_unit[u][p] (chiral_lattice.py:114). Stage 2 SHOWS this map.
  * alpha-free   : S_n contains NO alpha; the winding integer Q_link contains NO alpha.
                   alpha-invariance is STRUCTURAL (the modules don't import ALPHA), and
                   is the load-bearing, frame-independent anchor (prereg §2d).

This file = STAGE 1 (bedrock + bare-spectrum validate-on-known). Stage 2 (the
multiplicity observable + Fork-A test) is built ONLY if Stage 1 passes.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ave.core.chiral_lattice import (
    LatticeNet,
    build_diamond_net,
    build_srs_net,
    scatter_matrix,
)

# ─────────────────────────────────────────────────────────────────────────────
# ANTI-LEAK IMPORT-GUARD: this BEDROCK is pure linear algebra on the graph. No
# alpha-carrier, no Q_TANK, no ELECTRON instance may be reachable here. The
# operator and its spectrum are alpha-free BY CONSTRUCTION (the load-bearing
# anchor, prereg §2d).
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "alpha-leak: ALPHA must NOT be imported into the bedrock"
assert "Q_TANK" not in globals(), "alpha-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "ELECTRON" not in globals(), "alpha-leak: ELECTRON instance must NOT be imported"


# (skeleton — Stage-1 functions filled incrementally per commit)
# 1. local_scatter_spectrum(n)          -> bare S_n spectrum (validate-on-known §2a)
# 2. assemble_global_scattering(net)     -> the lattice CONNECT operator C @ (I (x) S_n)
# 3. global_spectrum(net)                -> eigenvalues of the assembled operator
# 4. differential_projector(n)           -> P_{-1} from S_n's -1 eigenvectors
# 5. operators_are_distinct(...)         -> H1 collapse check (srs vs diamond)
# 6. bedrock_validate_on_known(...)      -> the Stage-1 HALT-gated runner
