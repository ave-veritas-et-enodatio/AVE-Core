"""(a) planted-source positive-control runner — the #479 pattern generalized.

ENGINE-HARDENING ARC item 2(a). A null / disperse / does-not-exist verdict is only
believable if the SAME instrument can register the OPPOSITE. This guard pushes a
KNOWN-nonzero signal through an arbitrary pipeline callable and asserts the
readout registers it above a floor — the same-pipeline positive control the
Step-3.8a liveness doctrine requires (capability-map §8b.4).

LIVE-FIRE PROVENANCE. The srs localization-readjudication run
(`src/scripts/localization_readjudication_step3_srs_rerun.py`) built a KNOWN-bound
positive-control eigenmode (`seed_srs_positive_control`) and gated the DISPERSE
verdict on it reading `LOCALIZED_PERSIST` — i.e. the instrument had to be shown
ABLE to read bound before its "disperses" read on the physics seed was believed.
The em_readout Stage-1b review made the same demand: a "zero enclosed charge" read
is meaningless unless a KNOWN point source reads nonzero through the same solver
(`validate_zero_source` + the point-δ VoK). This module extracts that pattern into
a single callable-agnostic runner.

Two constructors help build the "known-nonzero" input on a lattice operator:
  * `project_out_nullspace` (re-exported) — the component of a seed ORTHOGONAL to
    the operator's frozen kernel (the part the operator actually governs), so a
    positive control is not silently planted in the unpushable nullspace.
  * a route-1 `localized_eigenmode` (from spectral_liveness) is the operator's own
    bound-like configuration — the cleanest known-nonzero for a persistence test.

α-CLEAN: no physical constant on this path.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np

from ave.solvers.spectral_liveness import project_out_nullspace


@dataclass(frozen=True)
class PlantedSourceResult:
    """Outcome of a planted-source positive control.

    registered  : True iff the readout on the planted input exceeded the floor.
    readout      : the scalar the pipeline returned on the planted input.
    floor        : the threshold the readout had to clear.
    baseline     : the readout on the zero/null input (must stay ~0 — the guard
                   also certifies the pipeline does NOT hallucinate a signal from
                   nothing, the zero-source floor).
    baseline_ok  : True iff baseline stayed below `baseline_tol`.
    """

    registered: bool
    readout: float
    floor: float
    baseline: float
    baseline_ok: bool
    baseline_tol: float
    label: str = ""

    @property
    def passed(self) -> bool:
        """The control passes iff the planted signal registered AND the zero-input
        baseline stayed quiet (both halves of a live, non-hallucinating readout)."""
        return bool(self.registered and self.baseline_ok)

    def as_dict(self) -> dict:
        return {
            "test": "planted_source_positive_control",
            "label": self.label,
            "registered": self.registered,
            "readout": self.readout,
            "floor": self.floor,
            "baseline": self.baseline,
            "baseline_ok": self.baseline_ok,
            "baseline_tol": self.baseline_tol,
            "passed": self.passed,
        }


def planted_source_control(
    pipeline: Callable[[np.ndarray], float],
    planted_input: np.ndarray,
    *,
    zero_input: np.ndarray | None = None,
    floor: float = 1e-6,
    baseline_tol: float = 1e-9,
    label: str = "",
) -> PlantedSourceResult:
    """Run `pipeline` on a KNOWN-nonzero input and certify it registers.

    Args:
        pipeline      : any callable input-array → scalar readout (the instrument
                        under certification; e.g. an enclosed-charge reader, a
                        participation-number classifier, a divergence magnitude).
                        MUST be the exact readout the verdict uses — a positive
                        control on a DIFFERENT pipeline certifies nothing.
        planted_input : the known-nonzero configuration to push through. Use
                        `project_out_nullspace(seed, L)` or a `localized_eigenmode`
                        so the signal lives in the operator's LIVE subspace.
        zero_input    : the null input (defaults to zeros_like(planted_input)); the
                        readout here must stay below `baseline_tol` (no hallucinated
                        signal from nothing — the zero-source floor).
        floor         : the planted readout must exceed this to count as registered.
        baseline_tol  : the zero-input readout must stay below this.

    Returns PlantedSourceResult. `.passed` is the load-bearing boolean: a verdict
    that consumes a null read should assert `planted_source_control(...).passed`
    FIRST (Step-3.8a: prove the instrument live before believing its null).
    """
    x = np.asarray(planted_input, dtype=float)
    if x.size == 0:
        raise ValueError("planted_input is empty — nothing to plant.")
    if np.linalg.norm(x) < 1e-300:
        raise ValueError("planted_input has zero norm — it IS the null; not a control.")

    readout = float(pipeline(x))

    z = np.zeros_like(x) if zero_input is None else np.asarray(zero_input, dtype=float)
    baseline = float(pipeline(z))

    registered = abs(readout) > floor
    baseline_ok = abs(baseline) <= baseline_tol
    return PlantedSourceResult(
        registered=registered,
        readout=readout,
        floor=floor,
        baseline=baseline,
        baseline_ok=baseline_ok,
        baseline_tol=baseline_tol,
        label=label,
    )


__all__ = ["planted_source_control", "PlantedSourceResult", "project_out_nullspace"]
