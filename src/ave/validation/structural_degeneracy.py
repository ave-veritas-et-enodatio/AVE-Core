"""(b) structural-degeneracy checks — retire the Stage-1 blind global-sum readout.

ENGINE-HARDENING ARC item 2(b). Some observables are forced to a value by the
graph / symmetry REGARDLESS of the physics — so a "zero" read on them was never
informative. This guard detects two such traps BEFORE a verdict trusts the
observable.

LIVE-FIRE PROVENANCE. The blind Stage-1 readout (capability-map §8b.3) was a
merged null read on a STRUCTURALLY-DEGENERATE global-sum observable: on a closed
graph the total Σ(∇·E) is annihilated by the operator's constant nullspace (`L·1 =
0` ⇒ `Σ(Lφ) = 1ᵀLφ = 0` for every φ), so the global divergence sum is IDENTICALLY
zero — the "zero enclosed charge" read was pre-ordained by topology, not physics.
The em_readout equation_audit even records WHY the local enclosed-charge PROFILE
(not the global sum) is the observable: "L annihilates the constant, so … the
global Σ(∇·E)=0 always ⇒ the LOCAL enclosed-charge profile is the observable"
(`em_readout_vsector_transducer.py` ledger, the jellium/mean-subtraction term).

Two detectors:
  * `detect_global_sum_degeneracy` — is the observable a global sum over a closed
    graph whose operator has the constant in its nullspace? If so, the sum is
    structurally forced (≈0 up to round-off) and MUST NOT drive a verdict; the
    local/spatially-resolved profile is the informative observable.
  * `detect_symmetry_forced_zero` — does a declared symmetry operation map the
    observable to its own negative (odd under the symmetry)? Then it is
    symmetry-forced to zero for ANY symmetric field, independent of physics.

α-CLEAN: no physical constant on this path.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np


@dataclass(frozen=True)
class StructuralDegeneracyResult:
    """Verdict on whether an observable is structurally forced (not physics)."""

    degenerate: bool
    kind: str  # "global_sum_nullspace" | "symmetry_forced_zero" | "none"
    forced_value: float  # the value the structure forces (≈0 for both traps)
    detail: str
    safe_to_use: bool  # False ⇒ do NOT drive a verdict on this observable

    def as_dict(self) -> dict:
        return {
            "test": "structural_degeneracy",
            "degenerate": self.degenerate,
            "kind": self.kind,
            "forced_value": self.forced_value,
            "detail": self.detail,
            "safe_to_use": self.safe_to_use,
        }


def detect_global_sum_degeneracy(
    L,
    *,
    weight=None,
    nullspace_tol: float = 1e-9,
    n_probe: int = 8,
    seed: int = 0,
) -> StructuralDegeneracyResult:
    """Is a global-weighted-sum observable `wᵀ(L·φ)` structurally forced to zero?

    A weighted global sum `wᵀ(Lφ)` equals `(Lᵀw)ᵀφ`. If the weight vector `w` is in
    the (left) nullspace of L — i.e. `Lᵀw ≈ 0` — the sum is IDENTICALLY zero for
    every φ, so a "zero" read carries no physics. This is the closed-graph
    divergence-sum trap. We test `‖Lᵀw‖` directly AND empirically over random
    probes `φ` (belt-and-suspenders against a subtle near-degeneracy).

    Args:
        L      : the operator whose weighted row/column sums are at issue (dense or
                 scipy-sparse).
        weight : the summation weight `w`. DEFAULT = the flat constant `1` (the
                 SCALAR global-sum trap: `Σ(Lφ)` on a scalar operator whose constant
                 is its nullspace — e.g. the closed-graph divergence sum). For a
                 BLOCK / multi-DOF operator (e.g. the 6-DOF micropolar Φ, whose
                 nullspace is the STRUCTURED uniform-translation vector `v[axis::6]=1`,
                 NOT the flat all-ones), pass that structured null vector as `weight`
                 so the detector probes the ACTUAL forced sum, not a spurious flat one.
                 The flat-`1` default is correct only when `1` really is L's constant.

    Returns StructuralDegeneracyResult with `safe_to_use=False` iff the weighted sum
    is forced. When forced, the caller should switch to a SPATIALLY-RESOLVED
    observable (the local enclosed-charge profile), not the global sum.
    """
    M = L.toarray() if hasattr(L, "toarray") else np.asarray(L, dtype=float)
    n = M.shape[0]
    w = np.ones(n) if weight is None else np.asarray(weight, dtype=float).reshape(-1)
    if w.size != n:
        raise ValueError(f"weight size {w.size} != operator dim {n}")
    left_null = float(np.max(np.abs(M.T @ w)))  # ‖Lᵀw‖_max

    rng = np.random.default_rng(seed)
    worst_sum = 0.0
    for _ in range(n_probe):
        phi = rng.standard_normal(n)
        s = float(abs(w @ (M @ phi)))
        # normalize by the field scale so we compare a fraction, not a magnitude
        scale = float(np.linalg.norm(M @ phi)) + 1e-300
        worst_sum = max(worst_sum, s / scale)

    forced = (left_null <= nullspace_tol) and (worst_sum <= 1e-6)
    return StructuralDegeneracyResult(
        degenerate=forced,
        kind="global_sum_nullspace" if forced else "none",
        forced_value=left_null,
        detail=(
            f"‖Lᵀw‖_max={left_null:.3e} (≤{nullspace_tol:.0e} ⇒ weight in left-nullspace); "
            f"worst normalized global sum over {n_probe} probes={worst_sum:.3e}. "
            + (
                "Global sum is STRUCTURALLY FORCED to ~0 — use the local/resolved profile."
                if forced
                else "Global sum is NOT structurally forced."
            )
        ),
        safe_to_use=not forced,
    )


def detect_symmetry_forced_zero(
    observable: Callable[[np.ndarray], float],
    field: np.ndarray,
    symmetry: Callable[[np.ndarray], np.ndarray],
    *,
    tol: float = 1e-9,
) -> StructuralDegeneracyResult:
    """Is `observable` ODD under `symmetry` (hence forced to zero for symmetric fields)?

    If `observable(S·x) ≈ −observable(x)` for a symmetry S, then any S-symmetric
    field (S·x = x) gives observable(x) = −observable(x) ⇒ 0, independent of the
    physics. We test the oddness on the SUPPLIED field (a representative), and — if
    the field is itself S-symmetric — confirm the observable actually sits at ~0.

    Args:
        observable : field-array → scalar.
        field      : a representative field to probe the oddness on.
        symmetry   : the symmetry operation on fields (e.g. spatial parity flip).

    Returns StructuralDegeneracyResult; `safe_to_use=False` iff the observable is
    symmetry-forced to zero (odd under S).
    """
    x = np.asarray(field, dtype=float)
    o = float(observable(x))
    xs = np.asarray(symmetry(x), dtype=float)
    os_ = float(observable(xs))
    scale = max(abs(o), abs(os_), 1e-300)
    is_odd = abs(os_ + o) / scale <= tol  # observable(S x) ≈ −observable(x)
    field_symmetric = bool(np.allclose(xs, x, atol=tol))
    forced = is_odd

    detail = (
        f"observable(x)={o:.3e}, observable(Sx)={os_:.3e}; "
        f"odd-under-S={is_odd} (|o(Sx)+o(x)|/scale={abs(os_ + o) / scale:.3e}); "
        f"supplied field S-symmetric={field_symmetric}. "
        + (
            "Observable is SYMMETRY-FORCED to 0 for symmetric fields — not a physics probe."
            if forced
            else "Observable is not symmetry-forced-zero on this field."
        )
    )
    return StructuralDegeneracyResult(
        degenerate=forced,
        kind="symmetry_forced_zero" if forced else "none",
        forced_value=0.0 if forced else o,
        detail=detail,
        safe_to_use=not forced,
    )


__all__ = [
    "detect_global_sum_degeneracy",
    "detect_symmetry_forced_zero",
    "StructuralDegeneracyResult",
]
