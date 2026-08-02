r"""
The E-route vacuum birefringence — the bankable chord (clm-pp3qwf)
==================================================================

Substrate-native first:

  * **Sector / mechanism.** This lives in the **ε-grade** (the V-keyed varactor,
    operating-point R2). Under a static / DC E-drive the ε-grade LOADS (ASYM:
    ε saturates, μ stays linear because a static B has ∂B/∂t = 0 → S_μ = 1, the
    μ-grade is a circulation-keyed relativistic inductor). The ONE non-linearity
    is the canonical Op14 kernel S(A)=√(1−A²) — **REUSED**, not re-minted:
    `ave.core.fdtd_3d._compute_local_epsilon` already computes ε_eff = ε₀·S(A)
    via `ave.axioms.scale_invariant.saturation_factor`, and THIS module imports
    that same `saturation_factor`. No second kernel.

  * **Coordinate discipline (A46).** The claim is in field-amplitude / refractive-
    index space (n vs E), and is measured there — coordinate-clean. (No
    (V_inc, V_ref) Clifford-torus phase-space claim is at issue.)

Under a linearly-polarized pump the AVE vacuum is **uniaxial** (optic axis ∥ Ê₀).
With ``A ≡ E/E_yield`` the two probe eigen-indices and the differential are

    n_⊥ = (1 − A²)^(1/4) = √S            (≈ 1 − ¼A²)
    n_∥ = √[(1 − 2A²)/√(1 − A²)]          (≈ 1 − ¾A²)
    δn_bir = n_∥ − n_⊥ ≈ −½A²            (the par−perp DIFFERENTIAL — what a
                                          polarimeter measures; NEGATIVE, E²-leading)

THE CHORD (existence, NOT magnitude — frame precisely):
  the AVE-distinct content is the **EXISTENCE** of a tree-level O(1) birefringence-
  bearing structure that the QED vacuum LACKS (QED's birefringence is an α²-loop
  Euler-Heisenberg effect; QED-with-a-cutoff does NOT reproduce it). The
  **MAGNITUDE** δn_AVE/δn_QED = 7.5/α³ ≈ 1.93e7 is an **α-ECHO** at the value
  level: AVE imports α, so the number rides α⁻³. Symmetric standard: QED's
  a_EH·α² is *equally* α-rooted — QED does not derive α either. Do NOT headline
  the magnitude as a chord.

DISCRIMINATOR = the **E-route**. A static B is a corroborative NULL (μ
circulation-keyed, S_μ = 1, δn_μ = 0 exactly — PVLAS-consistent). Do NOT claim
static-B as the falsifier.

Canonical leaf:
  `manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md`
  (clm-pp3qwf). E-route scope + static-B-null:
  `.../ch11-experimental-bench-falsification/pvlas-static-b-verdict.md`.
"""

from __future__ import annotations

import warnings

import numpy as np

# REUSE the canonical Op14 saturation kernel (the SAME function fdtd_3d uses).
from ave.axioms.scale_invariant import saturation_factor
from ave.core.constants import ALPHA, E_CRIT, E_YIELD

# The QED Euler-Heisenberg DIFFERENCED birefringence coefficient: the parallel
# (7/45) and perpendicular (4/45) eigen-indices differenced → 3/45. This is the
# like-for-like (par−perp differential) coefficient AVE must be compared against.
QED_EH_DIFFERENCED_COEFF: float = 3.0 / 45.0


def birefringence_eigenindices(A: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    r"""
    The two probe eigen-indices of the uniaxial pumped vacuum.

    .. math::
        n_\perp = (1-A^2)^{1/4} = \sqrt{S(A)}, \qquad
        n_\parallel = \sqrt{\frac{1-2A^2}{\sqrt{1-A^2}}}

    ``n_⊥`` is built from the REUSED canonical kernel ``S(A)=√(1−A²)`` (so the
    permittivity softening is the SAME Op14 saturation the FDTD engine uses).

    Args:
        A: the saturation ratio A = E/E_yield (scalar or array, |A| < 1/√2 for
           a real n_∥).

    Returns:
        (n_perp, n_par) — same shape as ``A``.
    """
    A = np.asarray(A, dtype=float)
    S = saturation_factor(A, yield_limit=1.0)  # √(1−A²) — canonical Op14 kernel
    n_perp = np.sqrt(S)  # (1−A²)^(1/4)
    n_par = np.sqrt((1.0 - 2.0 * A**2) / S)  # inner sqrt(1-A^2) IS the canonical S (single-source)
    return n_perp, n_par


def birefringence_dn(E: np.ndarray, *, e_yield: float = E_YIELD) -> np.ndarray:
    r"""
    The par−perp birefringence differential δn_bir(E) — the polarimeter observable.

    .. math::
        \delta n_{bir} = n_\parallel - n_\perp \approx -\tfrac12 A^2,
        \qquad A \equiv E / E_{yield}

    **Recover-QED (consistency):** at ``E ≪ E_yield`` (A → 0), ``δn_bir → 0`` —
    NO tree-level birefringence, exactly as QED at tree level. The leading term
    is ``−½A²`` (E²-leading, same leading power as QED's a_EH·α²·(E/E_crit)²).

    **Activate:** as E approaches E_yield the O(1) differential appears.

    Args:
        E: applied static / DC electric field [V/m] (scalar or array).
        e_yield: the yield field (default E_YIELD = V_yield/ℓ_node ≈ 1.13e17 V/m).

    Returns:
        δn_bir (negative, E²-leading) — same shape as ``E``.
    """
    A = np.asarray(E, dtype=float) / e_yield
    n_perp, n_par = birefringence_eigenindices(A)
    return n_par - n_perp


def chord_magnitude_ratio() -> float:
    r"""
    Field-INDEPENDENT matched par−perp DIFFERENTIAL ratio (SUPERSEDED value).

    ==== SUPERSEDED (2026-07-03) — this returns the WRONG-NORMALIZATION 7.5/α³.
    The QED denominator (3/45)·α² is understated (the AVE-side differenced 3/45
    estimate, not a QED-normalized Euler-Heisenberg coefficient). The corrected,
    re-frozen ratio is the **v3 consistent-instantaneous-footing** value

        δn_AVE/δn_QED = (1/2)/(2α/15π)·(E_crit/E_yield)² = 15π/(4α²)
                      = 3.75π/α² ≈ 2.2e5

    boxed at `manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/
    vacuum-birefringence-e4.md:104`; that leaf's `:106` records the 7.5/α³ form
    returned here as **v1 convention history**. This function is retained ONLY for
    provenance — the return value is UNCHANGED so the historical number stays
    reproducible; do NOT use its value in any prediction. ====

    **Deprecation provenance:** Grant ruling **D1 (2026-08-01)**, verbatim [sic]
    *"D1: (ii)"* — option (ii) = DEPRECATE, chosen over stamp-only and re-point.
    The bench-module sibling `ave.bench.birefringence.coefficient_ratio_differential`
    already carried an equivalent SUPERSEDED banner; this is the QED-module half of
    the same quantity, previously un-stamped (routed from the 2026-07-31
    verify-cite corrections lane).

    The historical derivation, for the record:

    .. math::
        \frac{\delta n_{AVE}}{\delta n_{QED}}
            = \frac{1/2}{(3/45)\,\alpha^2}\Bigl(\frac{E_{crit}}{E_{yield}}\Bigr)^2
            = \frac{45/6}{\alpha^3} = \frac{7.5}{\alpha^3} \approx 1.93\times10^7

    using ``E_crit = α^(−1/2) E_yield`` so ``(E_crit/E_yield)² = 1/α``.

    ★ Under EITHER normalization the number is an **α-ECHO**, NOT a chord — AVE
    imports α, so the magnitude rides a power of α (v1: α⁻³; v3: α⁻²; symmetric
    standard: QED's a_EH·α² is equally α-rooted). The CHORD is the EXISTENCE of the
    tree-level O(1) structure (see module docstring), not this value.

    Raises:
        DeprecationWarning: on every call (the value is superseded).

    Returns:
        The preserved-for-provenance v1 ratio 7.5/α³ ≈ 1.93e7 (NOT the live value).
    """
    warnings.warn(
        "chord_magnitude_ratio() is SUPERSEDED: it returns the v1 wrong-normalization "
        "ratio 7.5/alpha^3 ~ 1.93e7. The re-frozen v3 (consistent instantaneous "
        "footing) matched differential ratio is 3.75*pi/alpha^2 ~ 2.2e5 — boxed at "
        "manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/"
        "vacuum-birefringence-e4.md:104 (that leaf's :106 calls the 7.5/alpha^3 form "
        "v1 convention history). The return value is PRESERVED UNCHANGED for "
        "provenance/reproducibility; do NOT use it in any prediction. "
        "Deprecated per Grant ruling D1 (2026-08-01), option (ii) = DEPRECATE.",
        DeprecationWarning,
        stacklevel=2,
    )
    return (0.5 / (QED_EH_DIFFERENCED_COEFF * ALPHA**2)) * (E_CRIT / E_YIELD) ** 2
