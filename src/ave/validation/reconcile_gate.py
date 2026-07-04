"""(f) reconcile-gate — a claimed quantity vs an INDEPENDENT recomputation, with a
liveness self-test that PROVES the halt can fire.

THE DEFECT CLASS THIS RETIRES (caught by adversarial review in THREE consecutive
arcs — the recurrence that forced this helper):

  PR #521 (saturated srs elastic tensor): the bin-selector's loud-halt `else`
      branch was DEAD CODE — unreachable given the upstream bins. The driver
      advertised "any unmatched state = loud halt"; no state could ever reach it.
      (The "#521-review dead-else defect class", fixed in the #526 round, 217f3bac
      item 5e.)
  PR #526 (prestress ν(ρ_eff) map): the first-draft live DISCREPANT-HALT was
      likewise unreachable; fix 5e rewired it to fire on a real self-contradiction
      (map DEFORMED yet VS4 exact-collapse FAILED) and proved reachability by test.
  PR #527 (bond-force sign rule): the live gate RE-CHECKED THE IDENTITY THAT
      DEFINED ITS INPUTS (k_shear_eff = S_shear + T/ℓ forces T>0 ⇒
      k_shear_eff > S_shear), so it was algebraically incapable of firing on any
      live track. Fix 6b (0d25c419) reconciles the stored prestressed-tensor ν
      against an INDEPENDENTLY-assembled cold tensor at the shifted spring
      (extract_cubic_Cij — a different solver code path) and flags the 3×
      recurrence for THIS helper.

The common anatomy: a gate that consumes what the driver declares — or re-derives
the reference through the quantity's own defining identity — can only ever agree.
That is a checklist wearing a gate's clothing (reconcile-don't-declare). The repair
shape all three fix rounds converged on, extracted here:

  (i)  reconcile the claim against an INDEPENDENT recomputation — a different
       code path / different formula, NOT the defining identity;
  (ii) PROVE the halt can fire: inject a synthetic discrepancy through the SAME
       comparator + halt code path and assert the halt triggers.

WHAT THE SELF-TEST PROVES — AND DOES NOT. `prove_can_fire()` proves the comparator,
the tolerance arithmetic, and the halt-raising path are LIVE (retires the
#521/#526-class dead plumbing, and vacuous-tolerance gates). It CANNOT prove that
your `independent` callable is algebraically independent of the claim (the
#527-class defect): if the reference recomputes the defining identity, the gate is
vacuously green on every live run even though its plumbing is live. Choosing a
genuinely different code path is the registrant's obligation; the model is the
#527 fix — reconcile the prestressed-tensor ν against `extract_cubic_Cij` at the
shifted spring, a different assembler than the one that produced the claim.

α-CLEAN: no physical constant on this path.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np


class DiscrepantHalt(AssertionError):
    """The loud halt: the claim and its independent recomputation do NOT reconcile."""


class DeadGateError(AssertionError):
    """The self-test halt: a synthetic discrepancy did NOT fire the gate — the gate
    is a checklist, not a gate (the #521/#526/#527 defect class)."""


@dataclass(frozen=True)
class ReconcileGateResult:
    """Outcome of a reconcile-gate check (or of its can-fire self-test)."""

    reconciled: bool | str  # True/False, or an error string (soft path only)
    label: str
    max_abs_discrepancy: float  # max_i |claimed_i − independent_i|
    max_rel_discrepancy: float  # max_i |claimed_i − independent_i| / |independent_i|
    rtol: float
    atol: float
    n_elements: int
    can_fire_proven: bool = False  # True ⇒ the halt plumbing was live-fire proven

    @property
    def passed(self) -> bool:
        return self.reconciled is True

    def as_dict(self) -> dict:
        return {
            "test": "reconcile_gate",
            "label": self.label,
            "reconciled": self.reconciled,
            "max_abs_discrepancy": self.max_abs_discrepancy,
            "max_rel_discrepancy": self.max_rel_discrepancy,
            "rtol": self.rtol,
            "atol": self.atol,
            "n_elements": self.n_elements,
            "can_fire_proven": self.can_fire_proven,
            "passed": self.passed,
        }


def _evaluate(v: Any) -> np.ndarray:
    """Evaluate a registered quantity (value or zero-arg callable) to a 1-D array."""
    return np.atleast_1d(np.asarray(v() if callable(v) else v, dtype=float))


def _compare(x: np.ndarray, y: np.ndarray, rtol: float, atol: float):
    """(ok, max_abs, max_rel, n). NaN-safe: any NaN discrepancy fails the tolerance
    test (a comparison with NaN is False, so `ok` can never be rubber-stamped)."""
    if x.shape != y.shape:
        return False, float("inf"), float("inf"), int(max(x.size, y.size))
    abs_d = np.abs(x - y)
    tol = atol + rtol * np.abs(y)
    ok = bool(np.all(abs_d <= tol))
    max_abs = float(np.max(abs_d)) if x.size else 0.0
    max_rel = float(np.max(abs_d / (np.abs(y) + 1e-300))) if x.size else 0.0
    return ok, max_abs, max_rel, int(x.size)


@dataclass(frozen=True)
class ReconcileGate:
    """Register (a) a claimed quantity, (b) an INDEPENDENT recomputation path,
    (c) a tolerance — then `enforce()` (loud DISCREPANT-HALT on disagreement) or
    `check()` (soft result for a driver's own halt aggregation).

    `claimed`     : the driver's claimed value — scalar, array, or zero-arg callable.
    `independent` : the independent reference — PREFER a zero-arg callable that
                    RECOMPUTES the quantity via a different code path / formula.
                    Passing the defining identity here reconstructs the #527 defect;
                    the gate cannot detect that for you (see module docstring).
    `rtol`/`atol` : reconcile criterion |claimed − independent| ≤ atol + rtol·|independent|
                    (elementwise; all elements must reconcile). Both must be finite
                    and ≥ 0 — an infinite/NaN tolerance is a checklist by construction.
    """

    label: str
    claimed: Any
    independent: Any
    rtol: float
    atol: float = 0.0

    def __post_init__(self):
        for name, v in (("rtol", self.rtol), ("atol", self.atol)):
            if not (np.isfinite(v) and v >= 0.0):
                raise ValueError(
                    f"ReconcileGate [{self.label}]: {name}={v!r} is not a finite "
                    "non-negative tolerance — such a gate could never (or trivially) "
                    "fire; refusing to register it."
                )

    # -- the single comparator + halt path (shared by enforce AND the self-test,
    #    so the self-test exercises the exact plumbing the live gate uses) --------
    def _enforce_pair(self, x: np.ndarray, y: np.ndarray, *, can_fire_proven: bool = False) -> ReconcileGateResult:
        ok, max_abs, max_rel, n = _compare(x, y, self.rtol, self.atol)
        res = ReconcileGateResult(
            reconciled=ok,
            label=self.label,
            max_abs_discrepancy=max_abs,
            max_rel_discrepancy=max_rel,
            rtol=self.rtol,
            atol=self.atol,
            n_elements=n,
            can_fire_proven=can_fire_proven,
        )
        if not ok:
            raise DiscrepantHalt(
                f"DISCREPANT-HALT [{self.label}]: the claimed quantity disagrees with its "
                f"independent recomputation (max_abs={max_abs:.3e}, max_rel={max_rel:.3e}, "
                f"criterion atol+rtol·|ref| with rtol={self.rtol:.1e}, atol={self.atol:.1e}, "
                f"n={n}). The claim does NOT reconcile — no verdict may be read past this "
                "point. NEEDS REVIEW."
            )
        return res

    def check(self) -> ReconcileGateResult:
        """Soft reconcile: never raises on disagreement (evaluation errors are
        returned as an error string). For drivers that aggregate PASS flags into
        their own halt; pair with `prove_can_fire()` so the aggregation is not a
        checklist."""
        try:
            x = _evaluate(self.claimed)
            y = _evaluate(self.independent)
            ok, max_abs, max_rel, n = _compare(x, y, self.rtol, self.atol)
        except Exception as exc:  # surfaced in the result, not swallowed
            return ReconcileGateResult(
                reconciled=f"error: {exc}",
                label=self.label,
                max_abs_discrepancy=float("nan"),
                max_rel_discrepancy=float("nan"),
                rtol=self.rtol,
                atol=self.atol,
                n_elements=0,
            )
        return ReconcileGateResult(
            reconciled=ok,
            label=self.label,
            max_abs_discrepancy=max_abs,
            max_rel_discrepancy=max_rel,
            rtol=self.rtol,
            atol=self.atol,
            n_elements=n,
        )

    def enforce(self, *, prove_first: bool = True) -> ReconcileGateResult:
        """The hard gate: DISCREPANT-HALT (raises) if claim and independent
        recomputation disagree. With `prove_first=True` (default) the can-fire
        self-test runs FIRST, so every live enforcement is preceded by a live-fire
        proof of the same comparator + halt path — the exact gap found three times
        cannot silently recur for a consumer of this method. Evaluation errors
        propagate (a gate whose inputs cannot be computed must not pass silently)."""
        if prove_first:
            self.prove_can_fire()
        x = _evaluate(self.claimed)
        y = _evaluate(self.independent)
        return self._enforce_pair(x, y, can_fire_proven=prove_first)

    def prove_can_fire(self) -> ReconcileGateResult:
        """The liveness self-test: inject a synthetic discrepancy (a corruption of
        the claim, guaranteed outside tolerance) through the SAME comparator + halt
        path and assert DiscrepantHalt triggers. Raises DeadGateError if it does
        not — the gate is dead plumbing. Returns the (fired) result on success,
        with `can_fire_proven=True`.

        Scope (honest): this proves the PLUMBING is live. It does not — cannot —
        prove `independent` is algebraically independent of the claim (module
        docstring, the #527-class defect)."""
        y = _evaluate(self.independent)
        # a corruption guaranteed to violate |x−y| ≤ atol + rtol·|y| elementwise
        delta = 10.0 * (self.atol + self.rtol * (np.abs(y) + 1.0))
        if not np.all(delta > 0):  # exact-equality gate (rtol=atol=0): any offset must fire
            delta = np.abs(y) * 1e-9 + 1e-9
        corrupted = y + delta
        try:
            self._enforce_pair(corrupted, y)
        except DiscrepantHalt:
            ok, max_abs, max_rel, n = _compare(corrupted, y, self.rtol, self.atol)
            return ReconcileGateResult(
                reconciled=True,  # the SELF-TEST passed: the gate fired on corruption
                label=f"{self.label} [can-fire self-test]",
                max_abs_discrepancy=max_abs,
                max_rel_discrepancy=max_rel,
                rtol=self.rtol,
                atol=self.atol,
                n_elements=n,
                can_fire_proven=True,
            )
        raise DeadGateError(
            f"DEAD GATE [{self.label}]: a synthetic discrepancy (Δ well outside "
            f"atol+rtol·|ref|) did NOT fire the DISCREPANT-HALT. This gate cannot fire "
            "on any input — it is a checklist, not a gate (the #521/#526/#527 defect "
            "class). Fix the gate before trusting anything it guards."
        )


def reconcile(claimed: Any, independent: Any, *, rtol: float, atol: float = 0.0, label: str = "") -> ReconcileGateResult:
    """One-shot soft reconcile (see ReconcileGate.check)."""
    return ReconcileGate(label=label, claimed=claimed, independent=independent, rtol=rtol, atol=atol).check()


def assert_reconciled(
    claimed: Any,
    independent: Any,
    *,
    rtol: float,
    atol: float = 0.0,
    label: str = "",
    prove_first: bool = True,
) -> ReconcileGateResult:
    """One-shot hard gate (see ReconcileGate.enforce): can-fire self-test first
    (default), then DISCREPANT-HALT if claim and independent recompute disagree."""
    return ReconcileGate(label=label, claimed=claimed, independent=independent, rtol=rtol, atol=atol).enforce(
        prove_first=prove_first
    )


__all__ = [
    "ReconcileGate",
    "ReconcileGateResult",
    "DiscrepantHalt",
    "DeadGateError",
    "reconcile",
    "assert_reconciled",
]
