"""Fork-B GATE3 NEAR-SATURATION re-run — the chord-residual the original GATE3 missed.

Prereg / parent: research/2026-06-20_fork-b-saturation-tank-confinement_result.md §4
Built off origin/main @ d83f77c3 (the merged Fork-B gate, PR#307).

═══════════════════════════════════════════════════════════════════════════════
WHY THIS MODULE EXISTS (the residual, brutally stated)
═══════════════════════════════════════════════════════════════════════════════
The merged GATE3 reported the quarter-arc S(A)=√(1−A²) shape-GENERIC (Δ/L gap ~0
vs a same-family (1−A²)^p comparator) ⇒ ECHO. But that result holds ONLY because
the planted well maxed at A_bond.max ≈ 0.77 (diamond L=8; only ~8/256 bonds had
A>0.5). The quarter-arc's DISTINCTIVE feature is its STEEP region near A=1
(dS/dA = −A/√(1−A²) → −∞ as A→1). That region was NEVER exercised. So the
"shape-generic" verdict is, strictly, "shape-generic in the SHALLOW regime."

This module drives the core bonds into FULL SATURATION (A_bond.max ≈ 0.95–0.99 —
the steep regime) and re-runs the SAME depth-invariant Δ/L shape discriminator,
but against GENUINELY-DIFFERENT comparator FAMILIES (not just same-family
(1−A²)^p): plain tanh(k(1−A)), exp(−kA), Lorentzian 1/(1+kA²), power (1−A^n),
linear (1−kA). Each is norm-matched to the quarter-arc norm π/4 and depth-matched
to the same well floor.

═══════════════════════════════════════════════════════════════════════════════
ANTI-TAUTOLOGY: the POSITIVE CONTROL (load-bearing)
═══════════════════════════════════════════════════════════════════════════════
A zero shape gap is only informative if the metric CAN open a gap at this regime.
So a top-hat (STEP-discontinuous) stiffness comparator is run alongside: it MUST
open a large gap (and drop the eigenvector overlap) or the test is VOID at this
regime (the metric is saturated/blind, not discriminating). The smooth families
are the AVE-distinct content; the top-hat is the discriminator-still-works witness.

═══════════════════════════════════════════════════════════════════════════════
FROZEN BINNING (honest, pre-committed)
═══════════════════════════════════════════════════════════════════════════════
At FULL saturation, judged by the SAME Δ/L metric with the SAME bound-mode
selector as the merged GATE3:
  * CHORD-PARTIAL  : gap > 10% AND eigenvector overlap < 0.95 (positive control
                     confirms the metric discriminates) ⇒ the quarter-arc IS
                     shape-SPECIAL where it is steepest ⇒ a PARTIAL mass-sector
                     chord on the shape axis (upgrade the verdict).
  * ECHO-FINAL     : gap ≈ 0 AND overlap ≈ 1 even at full saturation ⇒ the
                     quarter-arc is not shape-special even in its steep regime.

ECHO-FINAL is the EXPECTED outcome. A CHORD claim must survive the positive
control AND the overlap<0.95 bar AND the symmetric-standard bar (saturable-NLS
shape-sensitivity is generic; the AVE-distinct content is SPECIFICALLY
quarter-arc-vs-other-SMOOTH-kernel at full saturation).

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-NATIVE + ALPHA-FREE (inherited from fork_b_saturation_tank)
═══════════════════════════════════════════════════════════════════════════════
  * Operator: the SAME native connect-map graph-stiffness L = Bᵀ diag(1/S) B
    (imported, not re-posited). A1 dilatation-scalar grade (CP2).
  * The shape kernels read the DIMENSIONLESS A=|V|/V_yield ⇒ ALPHA cancels.
    ALPHA is NEVER imported. α-invariance is structural (verified by the parent
    module's α→2α gate).
  * Real-space spatial eigenmode localization (CP4), not a φ² phase-space claim.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# ── reuse the canonical native connect-map operator + selector (NOT re-posited) ──
from ave.solvers.fork_b_saturation_tank import (
    ConfinementConfig,
    _band_structure,
    _operator_from_bond_S,
    _select_core_bound_mode,
    node_radius,
    saturated_core_strain_native,
    unique_bonds,
)

# ── alpha-leak guard (HR2): the parent module is alpha-free; so is this one ──
assert "ALPHA" not in globals(), "alpha-leak: ALPHA must NOT be imported"
assert "Q_TANK" not in globals(), "alpha-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "ELECTRON" not in globals(), "alpha-leak: ELECTRON instance must NOT be imported"

QUARTER_ARC_NORM = np.pi / 4.0  # ∫₀¹ √(1−A²) dA = π/4 (the canonical kernel's norm)
