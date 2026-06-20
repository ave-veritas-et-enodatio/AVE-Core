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


# ═════════════════════════════════════════════════════════════════════════════
# 1. THE CROSS-FAMILY SATURABLE KERNELS  S(A): S(0)=1, decreasing on [0,1]
# ═════════════════════════════════════════════════════════════════════════════
# Each is a GENUINELY DIFFERENT family from the quarter-arc √(1−A²) — NOT the
# same-family (1−A²)^p the merged GATE3 used. The retired RF-5 endpoint-tanh
# 0.5(1+tanh(k(0.5−A))) is sup-norm-pinned at 0.500 < π/4 = norm-INFEASIBLE; the
# PLAIN tanh(k(1−A)) used here DOES reach π/4 (norm-feasible). All five reach the
# quarter-arc norm π/4 (verified by the brentq norm-match below) — so "cross-family
# is norm-infeasible" was an OVER-GENERALIZATION from the ONE retired parameterization.


def kernel_quarter_arc(A: np.ndarray) -> np.ndarray:
    """The CANONICAL AVE kernel S(A)=√(1−A²) (p=0.5). The quarter circle exactly
    (S²+A²=1). Parameter-free. The steep region near A=1 (dS/dA→−∞) is its
    distinctive feature — exercised ONLY at full saturation. alpha-FREE."""
    return np.sqrt(np.maximum(1.0 - A**2, 0.0))


def kernel_plain_tanh(A: np.ndarray, k: float) -> np.ndarray:
    """PLAIN tanh saturable kernel 0.5(1+tanh(k(1−A))). Distinct from the RETIRED
    RF-5 0.5(1+tanh(k(0.5−A))) (which sup-pinned at 0.500). This one reaches π/4."""
    return 0.5 * (1.0 + np.tanh(k * (1.0 - A)))


def kernel_exp(A: np.ndarray, k: float) -> np.ndarray:
    """Exponential saturable kernel exp(−kA). A genuinely different family."""
    return np.exp(-k * A)


def kernel_lorentzian(A: np.ndarray, k: float) -> np.ndarray:
    """Lorentzian saturable kernel 1/(1+kA²). A genuinely different family."""
    return 1.0 / (1.0 + k * A**2)


def kernel_power(A: np.ndarray, n: float) -> np.ndarray:
    """Power-law saturable kernel (1−Aⁿ). NOTE: this is (1−Aⁿ), a DIFFERENT family
    from the same-family (1−A²)^p of the merged GATE3 (different functional form)."""
    return np.maximum(1.0 - A**n, 0.0)


def kernel_linear(A: np.ndarray, k: float) -> np.ndarray:
    """Linear saturable kernel (1−kA). The straight-line ramp; no curvature."""
    return np.maximum(1.0 - k * A, 0.0)


def kernel_tophat(A: np.ndarray, A_step: float) -> np.ndarray:
    """POSITIVE CONTROL: a STEP-DISCONTINUOUS stiffness — S=1 for A<A_step, S=0
    (clipped to the floor) for A≥A_step. A discontinuous stiffness IS discriminable
    (it changes the confining-region topology, not its smooth curvature); the metric
    MUST open a gap here or the test is void at this regime. NOT a smooth saturable
    kernel — the anti-tautology witness."""
    return np.where(A >= A_step, 0.0, 1.0)


# ── the cross-family registry: (builder, brentq bracket for the norm-match) ──
_SMOOTH_FAMILIES: dict[str, tuple] = {
    "plain_tanh": (kernel_plain_tanh, (0.01, 50.0)),
    "exp": (kernel_exp, (1e-3, 50.0)),
    "lorentzian": (kernel_lorentzian, (1e-3, 50.0)),
    "power": (kernel_power, (0.1, 20.0)),
    "linear": (kernel_linear, (1e-3, 1.0)),
}


def norm_match_family(builder, bracket: tuple[float, float], *, target_norm: float = QUARTER_ARC_NORM) -> dict:
    """Solve the family parameter so ∫₀¹ S(A) dA = target_norm (default π/4, the
    quarter-arc norm). Returns {ok, param, norm} or {ok:False} if INFEASIBLE (the
    target is outside the family's reachable norm range — the HALT the RF-5
    endpoint-tanh hit). This is the load-bearing check that the cross-family
    comparators are norm-FEASIBLE (NOT assumed-away). alpha-FREE."""
    from scipy.integrate import quad
    from scipy.optimize import brentq

    lo, hi = bracket

    def _norm(k: float) -> float:
        val, _ = quad(lambda A: builder(A, k), 0.0, 1.0, limit=200)
        return float(val)

    n_lo, n_hi = _norm(lo), _norm(hi)
    if not (min(n_lo, n_hi) <= target_norm <= max(n_lo, n_hi)):
        return {"ok": False, "reason": f"target_norm {target_norm:.4f} outside [{min(n_lo, n_hi):.4f},{max(n_lo, n_hi):.4f}]"}
    k = brentq(lambda kk: _norm(kk) - target_norm, lo, hi)
    return {"ok": True, "param": float(k), "norm": _norm(k), "target_norm": target_norm}


def depth_match_affine(S_raw: np.ndarray, target_min_S: float) -> np.ndarray:
    """Affine-rescale a raw per-bond S field so its MINIMUM equals target_min_S
    (the well floor), PRESERVING the kernel's curvature signature. The IDENTICAL
    construction as fork_b_saturation_tank._depth_matched_bond_S (so the depth axis
    is matched exactly the same way): S' = target + (S−S.min)·(1−target)/(1−S.min),
    clipped to [target, 1]. Isolates curvature from floor-depth. alpha-FREE."""
    s0 = float(S_raw.min())
    if abs(1.0 - s0) < 1e-12:
        return np.clip(S_raw, target_min_S, 1.0)
    S_scaled = target_min_S + (S_raw - s0) * (1.0 - target_min_S) / (1.0 - s0)
    return np.clip(S_scaled, target_min_S, 1.0)
