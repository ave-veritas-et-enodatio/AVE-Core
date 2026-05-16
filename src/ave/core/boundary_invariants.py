"""
Three substrate invariants 𝓜, 𝓠, 𝓙 — engine-side observable computation.

Operationalizes the substrate-observability rule (A-026, A-028 canonical): for any
localized region Ω ⊂ 𝓜_A enclosed by a Γ = -1 saturation surface ∂Ω, only three
integrated observables are visible externally:

    𝓜 = ∫_Ω (n_grav(r) - 1) dV       (integrated strain integral; mass-equivalent)
    𝓠 = Link(∂Ω, F_substrate) ∈ ℤ    (boundary linking number; charge-equivalent)
    𝓙 = Wind(∂Ω)                      (boundary winding number; spin-equivalent;
                                       half-integer per SU(2) double-cover)

These are the canonical names locked at Grant Q1 closure 2026-05-14 evening. The
canonical reference is AVE-QED `manuscript/vol_qed_replacement/appendices/G_substrate_vocabulary.tex`
§4. The picture-first reference is `manuscript/ave-kb/common/trampoline-framework.md`
§4 (boundaries and envelopes).

Per A-031 (Grant adjudication 2026-05-15 evening), the same three observables
apply at every scale including the cosmic boundary itself:
    𝓜_cosmic   → universe mass-energy
    𝓠_cosmic   → net topological charge (~0 for our universe)
    𝓙_cosmic   → Ω_freeze · I_cosmic (the cosmological initial condition)

This module provides reference implementations of these observables for scalar V
fields (e.g., from MasterEquationFDTD). Implementation status:

  - 𝓜 (compute_M): RIGOROUS. Volume integral of (n_grav - 1) where n_grav is the
    gravitational refractive index 1/n_eff (since the engine's n_eff = S^(1/4) ∈ [0,1]
    is the substrate-native slow-down factor; gravity-style n_grav = S^(-1/4) ∈ [1, ∞)
    is the equivalent "going up with mass" form).

  - 𝓠 (compute_Q): FIRST-PASS. Counts local saturation maxima as a proxy for
    soliton count. RIGOROUS implementation requires linking-number topology
    machinery on the substrate flux field (deferred — needs Cosserat-coupled
    vector field from cosserat_field_3d, not just scalar V).

  - 𝓙 (compute_J): FIRST-PASS. Computes net angular asymmetry of the strain field
    relative to its center of mass as a proxy for boundary winding. RIGOROUS
    implementation requires Hopf invariant computation on the full Cosserat
    rotational field (deferred — same dependency as 𝓠 rigorous).

L5 tracking:
  - E-101 (this module)
  - A-026 / A-027 / A-028 / A-031 (upstream canonical entries)
  - A-034 (canonical 2026-05-15 evening): Universal Saturation-Kernel
    Strain-Snap Mechanism. A-031 was refined per A-034 — "God's Hand"
    decouples into cosmic-parameter horizon vs observable mechanism. The
    saturation-kernel mechanism IS observable at 4 smaller scales (BCS
    0.00%, NOAA solar 40-yr, BH ring-down 1.7% from GR, Schwarzschild
    exact) per the 19-instance catalog at
    `manuscript/backmatter/07_universal_saturation_kernel.tex`.
  - Engine target: `src/ave/core/master_equation_fdtd.py` MasterEquationFDTD.V field

Cross-references:
  - AVE-QED `manuscript/vol_qed_replacement/appendices/G_substrate_vocabulary.tex` §4
  - AVE-Core `manuscript/ave-kb/common/trampoline-framework.md` §4 (substrate-observability)
  - AVE-Core `research/L5/axiom_derivation_status.md` A-028 (canonical names)
  - AVE-Core `manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex`
    §sec:cosmic_J_as_IC (cosmic-scale application)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np


@dataclass
class BoundaryInvariants:
    """The three substrate observables 𝓜, 𝓠, 𝓙 for a localized region.

    Fields:
        M: Integrated strain integral (mass-equivalent observable).
           Units of V_yield² · (length_unit³) in the engine's natural units;
           proportional to substrate mass-energy content of the region.
        Q: Boundary linking number proxy (first-pass implementation).
           Integer-valued for topologically distinct configurations;
           returns 0 for unstrained vacuum.
        J: Boundary winding number proxy (first-pass implementation).
           Half-integer-valued per SU(2) double-cover at canonical (e.g., 0.5
           for canonical electron); returns 0 for spherically symmetric strain.
        M_unit_normalized: M expressed in V_yield² · (ℓ_node³) units when
           dx is set to ℓ_node; useful for cross-engine comparison.
    """

    M: float
    Q: float
    J: float
    M_unit_normalized: Optional[float] = None

    def __repr__(self) -> str:
        return (
            f"BoundaryInvariants(M={self.M:.4e}, Q={self.Q:.4f}, J={self.J:.4f}"
            + (f", M_unit_normalized={self.M_unit_normalized:.4f}" if self.M_unit_normalized is not None else "")
            + ")"
        )


def compute_M(V: np.ndarray, dx: float, V_yield: float = 1.0, A_cap: float = 0.99) -> float:
    """Compute 𝓜 — integrated strain integral over the region.

    Defined as the volume integral of (n_grav(r) - 1) where n_grav is the
    gravitational-flavored refractive index. For the engine's substrate-native
    convention where n_eff = S^(1/4) goes from 1 (no strain) to 0 (full saturation),
    the gravity-equivalent n_grav = 1/n_eff = S^(-1/4) goes from 1 (no strain) to
    ∞ (full saturation), matching standard physics' "n increases with mass" form.

    Per A-028 canonical definition; per Vol 4 Ch 1:175-184 Virial sum
    interpretation, this gives the rest-mass-equivalent of a localized soliton.

    Args:
        V: Scalar substrate field (e.g., MasterEquationFDTD.V), shape (N, N, N).
        dx: Cell size in length units; integration measure dV = dx³.
        V_yield: Substrate yield voltage; sets the strain normalization A = |V|/V_yield.
        A_cap: Strain cap to avoid division-by-zero at saturation (default 0.99).

    Returns:
        M: integrated strain integral in units of [V_yield]² · [dx]³.
    """
    A = np.abs(V) / V_yield
    A_clipped = np.minimum(A, A_cap)
    # S(A) = sqrt(1 - A²); engine n_eff = S^(1/4); gravity n_grav = S^(-1/4)
    S = np.sqrt(np.maximum(1.0 - A_clipped**2, 1e-12))
    n_grav = S ** (-0.25)
    integrand = n_grav - 1.0  # zero where unstrained, positive where strained
    M = float(np.sum(integrand) * dx**3)
    return M


def compute_Q(V: np.ndarray, dx: float, V_yield: float = 1.0, threshold_factor: float = 0.5) -> float:
    """Compute 𝓠 — boundary linking number (FIRST-PASS proxy implementation).

    First-pass: counts local maxima of |V|/V_yield above a threshold as a proxy
    for the soliton count enclosed by the boundary. For a single localized
    soliton, returns ~1; for two well-separated solitons, returns ~2; for
    unstrained vacuum, returns 0.

    RIGOROUS implementation (deferred) requires:
      - Defining the substrate flux field F (vector, derived from V via the
        Cosserat coupling)
      - Computing Link(∂Ω, F) as the integer linking number of a closed surface
        ∂Ω (level set of |V|) with the flux field
    Both require the full Cosserat-coupled engine (doc 113 §5.4 deferred work).

    Per A-028 canonical definition; per Vol 2 Ch 1 charge identity, 𝓠 = 1 for
    canonical electron (corresponds to e charge in EE projection).

    Args:
        V: Scalar substrate field, shape (N, N, N).
        dx: Cell size (unused at this proxy level; kept for API consistency).
        V_yield: Substrate yield voltage.
        threshold_factor: Fraction of max |V| to use as a local-max detection
            threshold; default 0.5 (50% of peak amplitude).

    Returns:
        Q: First-pass proxy linking number (integer-valued for clean configurations).
    """
    A = np.abs(V) / V_yield
    if A.max() < 1e-6:
        return 0.0  # unstrained vacuum

    threshold = threshold_factor * A.max()
    above_threshold = A > threshold

    # Count connected components above threshold (local-max proxy)
    # Use a simple flood-fill via scipy if available; otherwise manual.
    try:
        from scipy import ndimage

        labeled, n_components = ndimage.label(above_threshold)
        return float(n_components)
    except ImportError:
        # Fallback: count isolated local maxima manually
        return _count_local_maxima_fallback(A, threshold)


def _count_local_maxima_fallback(A: np.ndarray, threshold: float) -> float:
    """Fallback local-maximum counter without scipy."""
    count = 0
    for i in range(1, A.shape[0] - 1):
        for j in range(1, A.shape[1] - 1):
            for k in range(1, A.shape[2] - 1):
                if A[i, j, k] < threshold:
                    continue
                if (
                    A[i, j, k] >= A[i - 1, j, k]
                    and A[i, j, k] >= A[i + 1, j, k]
                    and A[i, j, k] >= A[i, j - 1, k]
                    and A[i, j, k] >= A[i, j + 1, k]
                    and A[i, j, k] >= A[i, j, k - 1]
                    and A[i, j, k] >= A[i, j, k + 1]
                ):
                    count += 1
    return float(count)


def compute_J(V: np.ndarray, dx: float, V_yield: float = 1.0) -> float:
    """Compute 𝓙 — boundary winding number (FIRST-PASS proxy implementation).

    First-pass: measures the net angular asymmetry of the strain field around
    its center of mass as a proxy for boundary winding number. For a spherically
    symmetric strain (no winding), returns ~0. For a strain field with rotational
    structure, returns a non-zero value.

    RIGOROUS implementation (deferred) requires:
      - Hopf invariant computation on the full Cosserat rotational field ω
      - SU(2) → SO(3) double-cover factor giving half-integer quantization
    Requires the full Cosserat-coupled engine (doc 113 §5.4 deferred).

    Per A-028 canonical: 𝓙 = 1/2 for canonical electron (spin-½ per SU(2)
    half-cover from `trampoline-framework.md` §1.5 bubble-wand picture).

    Args:
        V: Scalar substrate field, shape (N, N, N).
        dx: Cell size (used for COM computation in length units).
        V_yield: Substrate yield voltage.

    Returns:
        J: First-pass proxy winding number (zero for spherically symmetric strain).
    """
    A = np.abs(V) / V_yield
    if A.max() < 1e-6:
        return 0.0  # unstrained vacuum

    # Compute center of mass of |A|
    nx, ny, nz = A.shape
    coords_x, coords_y, coords_z = np.meshgrid(
        np.arange(nx) * dx, np.arange(ny) * dx, np.arange(nz) * dx, indexing="ij"
    )
    A_total = float(A.sum())
    if A_total < 1e-9:
        return 0.0
    com_x = float((A * coords_x).sum() / A_total)
    com_y = float((A * coords_y).sum() / A_total)
    com_z = float((A * coords_z).sum() / A_total)

    # Compute moment-of-inertia-style angular asymmetry tensor
    # I_ij = ∫ A(r) · (δ_ij · r² - r_i · r_j) dV / A_total
    rx = coords_x - com_x
    ry = coords_y - com_y
    rz = coords_z - com_z
    r2 = rx**2 + ry**2 + rz**2

    # Asymmetry proxy: max anisotropy in the moment-of-inertia eigenvalues
    Ixx = float((A * (ry**2 + rz**2)).sum() / A_total)
    Iyy = float((A * (rx**2 + rz**2)).sum() / A_total)
    Izz = float((A * (rx**2 + ry**2)).sum() / A_total)
    Ixy = float((A * (-rx * ry)).sum() / A_total)
    Ixz = float((A * (-rx * rz)).sum() / A_total)
    Iyz = float((A * (-ry * rz)).sum() / A_total)

    inertia_tensor = np.array(
        [
            [Ixx, Ixy, Ixz],
            [Ixy, Iyy, Iyz],
            [Ixz, Iyz, Izz],
        ]
    )
    eigenvalues = np.linalg.eigvalsh(inertia_tensor)
    # Normalized anisotropy: 0 for perfect sphere, larger for elongated/asymmetric
    mean_eig = eigenvalues.mean()
    if mean_eig < 1e-9:
        return 0.0
    anisotropy = float(eigenvalues.std() / mean_eig)
    return anisotropy


def compute_all_invariants(
    V: np.ndarray,
    dx: float,
    V_yield: float = 1.0,
    A_cap: float = 0.99,
    threshold_factor: float = 0.5,
    l_node: Optional[float] = None,
) -> BoundaryInvariants:
    """Compute all three substrate invariants for the given field.

    Convenience function combining compute_M, compute_Q, compute_J.

    Args:
        V: Scalar substrate field, shape (N, N, N).
        dx: Cell size in length units.
        V_yield: Substrate yield voltage.
        A_cap: Strain cap for 𝓜 computation.
        threshold_factor: Local-max threshold for 𝓠 computation.
        l_node: Optional ℓ_node value; if provided, computes M_unit_normalized
            = M / V_yield² / l_node³ for cross-engine comparison.

    Returns:
        BoundaryInvariants dataclass with M, Q, J (+ optional M_unit_normalized).
    """
    M = compute_M(V, dx, V_yield, A_cap)
    Q = compute_Q(V, dx, V_yield, threshold_factor)
    J = compute_J(V, dx, V_yield)
    M_unit_normalized = None
    if l_node is not None and l_node > 0:
        M_unit_normalized = M / (V_yield**2 * l_node**3)
    return BoundaryInvariants(M=M, Q=Q, J=J, M_unit_normalized=M_unit_normalized)
