"""S1 — the (2,3) winding as a separately-conserved DOF: the DYNAMICAL gate.

FROZEN PRE-REG: research/2026-06-24_engine-s1-winding-dof_prereg.md (commit bed0b2d3).
This module is the S1 make-or-break gate (pre-reg §3 SUB-CLAIM A): single-knot
(2,3)-winding conservation under the engine's ACTUAL `step()` (NOT static
`deform_continuous`) + a LOCAL winding-current continuity law (∂_t W + ∇·J_W ≈
source). Two-soliton TRANSFER is DEFERRED (pre-reg §3 (d), §6 SUB-CLAIM B).

AXIOM CHAIN (recorded per pre-reg §8.8): charge = the Beltrami helicity
H_bel = ∫ ω·(∇×ω) read off the real-space Cosserat ω micro-rotation grade
(master-equation.md:20). The (2,3) winding is the toroidal "2" (ω polarization-
direction) × poloidal "3" (the ω-tank LC quadrature phase). Coordinate category
RULED real-space ω-grade (pre-reg §7 Fork 2): the phase-space (V_inc, V_ref)
Clifford torus is V's read-only projection (NOT an independent DOF, so it cannot
host the separately-conserved winding); the real-space ω is the only genuinely
independent DOF (own field + own momentum I_ω·ω̇, cosserat_field_3d.py:934,948).

ANTI-REBUILD (Rule 14): this gate REUSES the crystal_graft_v2/v4 immune system
(slaved_omega positive control, real_dynamics_ran flag, alias canary, H_bel
pre/post-lock drift, helicity ledger) + charge_quantization.compute_Q_link /
seed_pq_winding. It PORTS the chord-deciding readout onto the α-clean host
`src/tests/engine_acceptance/_winding_host.py` (κ̃=6/5). It NEVER imports/routes
ALPHA / KAPPA_CHIRAL_ELECTRON / V_SNAP / L_NODE / M_E / Q_TANK on the readout
path (pre-reg §0 α-clean host; §5 trap 8).

CLASSIFICATION (consistency-vs-emergence): CONSISTENCY-class (pre-reg §2). It
upgrades "A1-sustains-rotation" from asserted-CLASS to derived-REAL for the
declared real-space ω coordinate and the single-knot conservation claim ONLY.
It is NOT the α-free chord (that is S4). The Q=137 slot stays EMPTY (gate
wmighcz1z, anti-substitution).
"""

from __future__ import annotations

import numpy as np

# ── α-CLEAN HOST (the chord-deciding readout path; κ̃=6/5, NO α). Importing this
#    module executes its load-time guard triad — an α-leak fails HERE. ──────────
from tests.engine_acceptance import _winding_host as HOST

# ── the engine: α-clean on all forbidden readout symbols (verified 2026-06-24;
#    crystal_engine/v2/v3/v4 import only NU_VAC + R_II from constants, never
#    ALPHA / KAPPA_CHIRAL_ELECTRON / V_SNAP / L_NODE / M_E / Q_TANK). κ̃ defaults
#    to the 6/5 literal in CrystalEngine.__init__ (α-FREE). ──────────────────────
from ave.core.crystal_graft_v4 import CrystalGraftV4

# ── the ported immune-system readouts (α-free: charge_quantization carries its
#    OWN value-echo import-guard; fast_winding_extractor is a pure instrument). ──
from ave.topological.charge_quantization import compute_Q_link, seed_pq_winding
from ave.utils.fast_winding_extractor import extract_2_3_omega_fast

# ── the engine config (frozen, α-FREE; mirrors crystal_graft_v4_run CFG). ──────
_CFG = dict(
    source_mode="abc", lam_sign=1, p=2, q=3, S_min=2e-3, A_cap=0.999,
    omega_gap=1.0, wall_center=0.62, wall_width=0.30,
    kappa_tilde=6.0 / 5.0, pml_thickness=6,
)
# the α-free winding factor the host certifies (κ̃ = 6/5); engine + host AGREE.
_KAPPA_TILDE = HOST.winding_kappa_tilde(2, 3)

# pre-stated tolerances (FROZEN before the run; do NOT tune to force a verdict).
ALIAS_TOL = 0.34            # pre-reg §3(c) alias canary
CONTINUITY_REL_TOL = 0.35   # interior dW/dt accounted by source+flux to this rel
MIN_CELLS_PER_TURN = 3.0    # pre-reg §4 resolution ceiling (q resolved ≥ 3-4 cells/turn)
NEG_CTRL_PUMP_RATIO = 3.0   # lock-OFF |L_ω| must exceed lock-ON by this factor (FIRES)
