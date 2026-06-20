"""validate.py — recover-a-known assertion gate.

FACTORED FROM: the AVE-Core src/scripts/verify/*_anchor.py + *_results.json
pattern, specifically
  - muon_g2_fermilab_anchor.py compare_to_*_baseline (:139-203) +
    adjudicate_outcome (:206-262): the deviation / deviation_pct / n_sigma /
    PASS-or-FLAG verdict-at-tolerance contract against a LABELED reference.
  - baryon_ladder_pdg_2024_anchor.py (same anchor-vs-PDG-reference shape).

A helper that asserts a COMPUTED value matches a labeled PDG / CODATA / known
reference within tolerance. This is the recover-a-known gate (validate-on-known
discipline): the factoring of an exemplar / engine is not done until a computed
value is proven to reproduce a labeled known target.

The anchor exemplars compute deviation = value - reference, deviation_pct, and
(when an uncertainty is known) n_sigma = deviation / uncertainty, then emit a
PASS-conditional / FLAG verdict at a tolerance (muon anchor :238-262). This
module factors that into a single assert_recovers_known + a structured
KnownComparison record.

DISCIPLINE: no physical constants are imported — this is a pure comparison gate.
The caller supplies both the computed value (derived from ave.core.constants
upstream) and the labeled reference. The reference is a LABELED known input
(PDG/CODATA/measured), never an AVE-derived quantity dressed as a target.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class KnownComparison:
    """Structured record of a computed-value-vs-labeled-reference comparison.

    Mirrors the muon-anchor comparison dict (muon_g2_fermilab_anchor.py:154-163,
    :191-203): value, reference, deviation, deviation_pct, n_sigma, verdict.

    Attributes
    ----------
    label : str
        What is being recovered (e.g. "muon a_mu (Fermilab e+e- baseline)").
    value : float
        The computed value.
    reference : float
        The labeled known reference (PDG/CODATA/measured).
    tol : float
        Relative tolerance the comparison was adjudicated at.
    deviation : float
        value - reference (absolute).
    deviation_pct : float
        100 * (value - reference) / reference (signed; inf if reference == 0).
    rel_error : float
        |value - reference| / |reference| (the quantity compared to tol; inf if
        reference == 0).
    n_sigma : Optional[float]
        deviation / uncertainty when an uncertainty was supplied, else None.
    passed : bool
        True if rel_error <= tol.
    """

    label: str
    value: float
    reference: float
    tol: float
    deviation: float
    deviation_pct: float
    rel_error: float
    n_sigma: Optional[float]
    passed: bool

    def summary(self) -> str:
        """One-line PASS/FLAG summary in the anchor-exemplar style."""
        verdict = "PASS" if self.passed else "FLAG"
        sigma_str = "" if self.n_sigma is None else f", {self.n_sigma:+.2f}sigma"
        return (
            f"{verdict} — {self.label}: computed={self.value:.6g} "
            f"reference={self.reference:.6g} "
            f"(dev={self.deviation:+.3g}, {self.deviation_pct:+.3f}%, "
            f"rel_err={self.rel_error:.3g} vs tol={self.tol:.3g}{sigma_str})"
        )


def compare_to_known(
    value: float,
    reference: float,
    tol: float,
    label: str,
    *,
    uncertainty: Optional[float] = None,
) -> KnownComparison:
    """Compute the deviation / deviation_pct / n_sigma / pass record (no assert).

    The non-raising sibling of assert_recovers_known — returns the structured
    KnownComparison so a caller can adjudicate / log a batch before deciding to
    raise. Factored from the muon-anchor comparison block
    (muon_g2_fermilab_anchor.py:150-163).

    Parameters
    ----------
    value : float
        The computed value.
    reference : float
        The labeled known reference (PDG/CODATA/measured).
    tol : float
        Relative tolerance (rel_error <= tol => PASS).
    label : str
        Human-readable description of what is being recovered.
    uncertainty : float, optional
        Reference uncertainty; if given, n_sigma = (value - reference) /
        uncertainty is reported (muon anchor :152).
    """
    deviation = value - reference
    if reference != 0:
        deviation_pct = 100.0 * deviation / reference
        rel_error = abs(deviation) / abs(reference)
    else:
        deviation_pct = float("inf")
        rel_error = float("inf")

    n_sigma: Optional[float] = None
    if uncertainty is not None and uncertainty > 0:
        n_sigma = deviation / uncertainty

    passed = rel_error <= tol

    return KnownComparison(
        label=label,
        value=value,
        reference=reference,
        tol=tol,
        deviation=deviation,
        deviation_pct=deviation_pct,
        rel_error=rel_error,
        n_sigma=n_sigma,
        passed=passed,
    )


def assert_recovers_known(
    value: float,
    reference: float,
    tol: float,
    label: str,
    *,
    uncertainty: Optional[float] = None,
) -> KnownComparison:
    """Assert a computed value recovers a labeled known reference within tol.

    The recover-a-known gate. Raises AssertionError with the full deviation
    breakdown if rel_error > tol; otherwise returns the KnownComparison record.

    Factored from the muon-anchor adjudicate_outcome PASS/FLAG-at-tolerance
    pattern (muon_g2_fermilab_anchor.py:238-262), generalized to a single
    computed-value-vs-labeled-reference assertion (the baryon_ladder /
    *_anchor recover-a-known shape).

    Parameters
    ----------
    value : float
        The computed value.
    reference : float
        The labeled known reference (PDG/CODATA/measured).
    tol : float
        Relative tolerance (rel_error <= tol => PASS).
    label : str
        Human-readable description of what is being recovered.
    uncertainty : float, optional
        Reference uncertainty for an n_sigma report.

    Returns
    -------
    KnownComparison
        The passing comparison record.

    Raises
    ------
    AssertionError
        If rel_error > tol, with the full deviation breakdown in the message.
    """
    cmp = compare_to_known(value, reference, tol, label, uncertainty=uncertainty)
    if not cmp.passed:
        raise AssertionError(
            f"recover-a-known FAILED: {label} did not match reference within tol.\n"
            f"  computed   = {value:.10g}\n"
            f"  reference  = {reference:.10g}\n"
            f"  deviation  = {cmp.deviation:+.6g} ({cmp.deviation_pct:+.4f}%)\n"
            f"  rel_error  = {cmp.rel_error:.6g}\n"
            f"  tolerance  = {tol:.6g}"
            + (f"\n  n_sigma    = {cmp.n_sigma:+.4f}" if cmp.n_sigma is not None else "")
        )
    return cmp
