"""(c) runtime-independence assert — the #479/#484 stub-and-compare pattern.

ENGINE-HARDENING ARC item 2(c). To prove that a result does NOT depend on some
quantity (e.g. the winding integer Q_link never enters an EM-solve RHS), the
name-independent, reconcile-grade check is: STUB the dependency to return garbage,
recompute, and assert the output is BIT-IDENTICAL. If the output does not move, the
dependency provably never entered the computation — regardless of what alias or
rigged name it was smuggled under.

LIVE-FIRE PROVENANCE. The em_readout equation_audit's RUNTIME INDEPENDENCE CHECK
(item 4d, reconcile-grade): it monkeypatched `srs_cage_winding.compute_Q_link_srs`
to return `{"Q_link": 999999, "w_tor": -7}`, recomputed the winding source `b_EM`,
and asserted `np.array_equal(b_real, b_stub)` — proving no integer/Link is routed
into the RHS by construction (`em_readout_vsector_transducer.py:789-806`). This
module extracts that into a general context-manager + assert so any driver can
certify "output X does not depend on dependency Y" the same rigorous way.

α-CLEAN: no physical constant on this path.
"""

from __future__ import annotations

import importlib
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any, Callable

import numpy as np


@dataclass(frozen=True)
class RuntimeIndependenceResult:
    """Outcome of a stub-and-compare runtime-independence check."""

    independent: bool | str  # True/False, or an error string
    target: str  # "module.attr" that was stubbed
    max_abs_diff: float  # ‖output_real − output_stub‖_max (0.0 ⇒ identical)
    label: str = ""

    @property
    def passed(self) -> bool:
        return self.independent is True

    def as_dict(self) -> dict:
        return {
            "test": "runtime_independence",
            "label": self.label,
            "target": self.target,
            "independent": self.independent,
            "max_abs_diff": self.max_abs_diff,
            "passed": self.passed,
        }


@contextmanager
def _stubbed(module_path: str, attr: str, stub: Callable[..., Any]):
    """Temporarily replace `module_path.attr` with `stub`; restore on exit."""
    mod = importlib.import_module(module_path)
    real = getattr(mod, attr)
    setattr(mod, attr, stub)
    try:
        yield
    finally:
        setattr(mod, attr, real)


def stub_and_compare(
    compute: Callable[[], np.ndarray],
    *,
    module_path: str,
    attr: str,
    stub: Callable[..., Any],
    label: str = "",
) -> RuntimeIndependenceResult:
    """Recompute `compute()` with `module_path.attr` stubbed, and compare to the
    real run BIT-for-BIT.

    Args:
        compute     : a zero-arg callable that runs the pipeline and returns the
                      output array whose dependence is at issue (e.g. the solve RHS,
                      the participation number field). Called ONCE with the real
                      dependency and ONCE with the stub.
        module_path : dotted module where the dependency lives (e.g.
                      "ave.solvers.srs_cage_winding").
        attr        : the attribute to stub (e.g. "compute_Q_link_srs").
        stub        : the garbage replacement (should return an obviously-wrong
                      value so a real dependence would visibly move the output).

    Returns RuntimeIndependenceResult. `.passed` ⇒ output is bit-identical ⇒ the
    stubbed quantity provably never entered `compute()`.
    """
    try:
        out_real = np.asarray(compute())
        with _stubbed(module_path, attr, stub):
            out_stub = np.asarray(compute())
    except Exception as exc:  # pragma: no cover - surfaced, not swallowed
        return RuntimeIndependenceResult(
            independent=f"error: {exc}",
            target=f"{module_path}.{attr}",
            max_abs_diff=float("nan"),
            label=label,
        )

    identical = bool(np.array_equal(out_real, out_stub))
    if out_real.shape == out_stub.shape and out_real.size:
        diff = float(np.max(np.abs(out_real - out_stub)))
    else:
        diff = 0.0 if identical else float("inf")
    return RuntimeIndependenceResult(
        independent=identical,
        target=f"{module_path}.{attr}",
        max_abs_diff=diff,
        label=label,
    )


def assert_runtime_independent(
    compute: Callable[[], np.ndarray],
    *,
    module_path: str,
    attr: str,
    stub: Callable[..., Any],
    label: str = "",
) -> RuntimeIndependenceResult:
    """`stub_and_compare` that RAISES if the output moved (for use as a hard gate)."""
    res = stub_and_compare(compute, module_path=module_path, attr=attr, stub=stub, label=label)
    if res.independent is not True:
        raise AssertionError(
            f"runtime-independence FAILED for {res.target}"
            + (f" [{label}]" if label else "")
            + f": output moved (max_abs_diff={res.max_abs_diff}). The stubbed quantity "
            "DOES enter the computation — it is not independent."
        )
    return res


__all__ = [
    "assert_runtime_independent",
    "stub_and_compare",
    "RuntimeIndependenceResult",
]
