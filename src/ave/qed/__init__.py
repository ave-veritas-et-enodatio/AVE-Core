"""
AVE QED-extension engine (Stage-2)
==================================

Two dormant-in-the-QED-regime corrections ON the inherited QED / Maxwell solver:

  (1) The **Brillouin-cutoff propagator** (`brillouin_cutoff`) — a FORM-DERIVED
      loop regulator. The Axiom-1 lattice pitch ℓ_node gives the EXACT discrete-
      Hilbert commutator (DCVE App-E, dcve-specification.md:36-42):
          p_disc = (ℏ/iℓ)·sin(kℓ)  ⇒  [x,p] = iℏ·cos(kℓ) = iℏ·√(1−(ℓp/ℏ)²)
      so the lattice supplies a PHYSICAL momentum cutoff at the Brillouin edge
      |k| ≤ k_max = π/ℓ_node — NO counterterm. A 1-loop integral over the FIRST
      Brillouin zone is FINITE by mode-count (N = V/ℓ³ finite modes).

  (2) The **E-route vacuum birefringence** (`birefringence`) — the bankable chord
      (clm-pp3qwf). REUSES the saturating-ε already at
      `ave.core.fdtd_3d._compute_local_epsilon` (the canonical Op14 kernel
      S(A)=√(1−A²)); under a static/DC E-drive the ε-grade loads (ASYM):
          n_⊥ = (1−A²)^(1/4),  n_∥ = √[(1−2A²)/√(1−A²)],  δn_bir = n_∥−n_⊥ ≈ −½A²

FORM / VALUE honesty (the two halves sit at DIFFERENT rungs — NOT co-equal):
  • the ℓ_node cutoff FORM is genuinely FORM-DERIVED (Axiom-1 → the exact
    discrete-Hilbert commutator — the more-principled-than-dim-reg half);
  • the saturating-ε is FORM-POSTULATED (it IS Axiom 4);
  • α is QED's coupling — IMPORTED here (a VALUE-import, EXPECTED for a
    QED-extension; the birefringence MAGNITUDE 7.5/α³ is an α-ECHO, not α-clean).

See research/2026-06-29_grqed-stage2-qed-extension_result.md for the full ledger.
"""

from ave.qed.birefringence import (
    birefringence_dn,
    birefringence_eigenindices,
    chord_magnitude_ratio,
)
from ave.qed.brillouin_cutoff import (
    K_MAX_SPATIAL,
    continuum_loop_integral,
    lattice_dispersion_denominator,
    loop_integral_brillouin_zone,
)

__all__ = [
    # Brillouin-cutoff propagator / loop regulator
    "K_MAX_SPATIAL",
    "lattice_dispersion_denominator",
    "loop_integral_brillouin_zone",
    "continuum_loop_integral",
    # E-route vacuum birefringence
    "birefringence_dn",
    "birefringence_eigenindices",
    "chord_magnitude_ratio",
]
