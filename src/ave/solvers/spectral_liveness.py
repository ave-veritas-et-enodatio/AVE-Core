"""Spectral-liveness diagnostic — the standing pre-run readout-liveness check for
localization tests (ave-prereg v1.4 Step 3.8 made operational).

Prereg : research/2026-07-03_localization-readjudication_prereg.md §5.

═══════════════════════════════════════════════════════════════════════════════
WHY THIS EXISTS (the exposure this diagnostic would have caught pre-run)
═══════════════════════════════════════════════════════════════════════════════
The 2026-07-03 verdict-exposure sweep found the diamond TETRA operator L_D
carries a large FROZEN NULLSPACE (8-16 near-zero modes at N=8-12) onto which a
smooth centred seed projects ~93-98% of its L²-energy. An at-rest seed sitting in
that nullspace stays PUT under the energy-conserving Crank-Nicolson update
(L_D·V=0 ⇒ V^{n+1}=2V^n−V^{n-1} = the free update) — a spurious "PERSIST" that is
bookkeeping, NOT bulk self-focusing physics; and the ~6-7% the operator DOES
govern disperses. Either way the DISPERSE observable was reading the dead-leg.

This module decomposes ANY seed against ANY (real-symmetric, PSD) operator's
spectrum and reports:
  * nullspace_energy_fraction — the L²-energy fraction in the frozen kernel
    (|λ|<tol). HIGH ⇒ the operator cannot push most of the seed ⇒ the readout
    is BLIND to whatever the seed does in that subspace ⇒ any persistence verdict
    is suspect BEFORE it is read.
  * live_energy_fraction — the complement (the operator-governed subspace).
  * spectral weight profile — energy vs eigenvalue bands (where the seed lives).

It is operator-agnostic: pass the diamond L_D (native_cage_imex.assemble_L_D) OR
the srs graph Laplacian (srs_cage_winding.assemble_L_srs) OR any dense/sparse SPD
matrix. Read-only; computes nothing physical, adds no CODATA input.

CONSISTENCY-VS-EMERGENCE: INFRASTRUCTURE (a diagnostic instrument). No physics
claim; α-free by construction (touches no constants).
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np


@dataclass(frozen=True)
class SpectralLiveness:
    """The decomposition result. All fractions are of ‖seed‖² (L²-energy)."""

    n_dof: int
    nullspace_dim: int
    nullspace_tol: float
    nullspace_energy_fraction: float  # energy in |λ| < tol (the frozen dead-leg)
    live_energy_fraction: float       # complement (operator-governed subspace)
    peak_single_mode_weight: float    # largest single-mode |proj|² (concentration)
    peak_single_mode_eigenvalue: float
    eigenvalue_min: float
    eigenvalue_max: float
    smallest_nonzero_eigenvalue: float
    band_edges: np.ndarray = field(default=None)  # eigenvalue band boundaries
    band_energy_fraction: np.ndarray = field(default=None)  # energy per band

    def as_dict(self) -> dict:
        return {
            "n_dof": int(self.n_dof),
            "nullspace_dim": int(self.nullspace_dim),
            "nullspace_tol": float(self.nullspace_tol),
            "nullspace_energy_fraction": float(self.nullspace_energy_fraction),
            "live_energy_fraction": float(self.live_energy_fraction),
            "peak_single_mode_weight": float(self.peak_single_mode_weight),
            "peak_single_mode_eigenvalue": float(self.peak_single_mode_eigenvalue),
            "eigenvalue_min": float(self.eigenvalue_min),
            "eigenvalue_max": float(self.eigenvalue_max),
            "smallest_nonzero_eigenvalue": float(self.smallest_nonzero_eigenvalue),
            "band_edges": None if self.band_edges is None else self.band_edges.tolist(),
            "band_energy_fraction": (
                None if self.band_energy_fraction is None
                else self.band_energy_fraction.tolist()
            ),
        }


def _to_dense(L) -> np.ndarray:
    """Coerce a scipy-sparse or ndarray SPD operator to a dense symmetric array."""
    if hasattr(L, "toarray"):
        M = L.toarray()
    else:
        M = np.asarray(L, dtype=float)
    if M.ndim != 2 or M.shape[0] != M.shape[1]:
        raise ValueError(f"operator must be square 2D; got shape {getattr(M, 'shape', None)}")
    # symmetrise machine-eps asymmetry (the periodic-roll / graph builds are SPD
    # up to eps); a genuinely non-symmetric operator is a caller error.
    asym = np.max(np.abs(M - M.T))
    if asym > 1e-8 * max(np.max(np.abs(M)), 1e-30):
        raise ValueError(
            f"operator is not symmetric (max|M-Mᵀ|={asym:.2e}); this diagnostic "
            "assumes a real-symmetric PSD stiffness operator (div-form Laplacian)."
        )
    return 0.5 * (M + M.T)


def spectral_liveness(
    seed: np.ndarray,
    L,
    *,
    nullspace_tol: float = 1e-9,
    n_bands: int = 8,
) -> SpectralLiveness:
    """Decompose `seed` against the spectrum of the SPD operator `L` and report
    the readout-liveness diagnostic.

    Args:
        seed : the field to decompose. Flattened to 1-D; its length must equal
               L's dimension (an N³ cube seed is reshaped to N³; an srs
               node-cloud seed is already 1-D of length n_nodes).
        L    : a real-symmetric PSD operator (dense ndarray or scipy sparse) —
               the div-form stiffness Laplacian whose nullspace is the frozen
               (unpushable) subspace. Dense eigendecomposition (np.linalg.eigh),
               so keep the dimension tractable (≤ ~a few thousand DOF).
        nullspace_tol : |λ| below this counts as the frozen kernel.
        n_bands : number of eigenvalue bands for the spectral-weight profile.

    Returns:
        SpectralLiveness — nullspace-energy fraction (the HEADLINE readout-
        liveness number) + the live fraction + the spectral-weight profile.

    NOTE: this is the same computation the exposure sweep ran ad hoc; making it a
    first-class module means every localization seed gets its liveness read BEFORE
    its persistence verdict (Step 3.8a operationalised).
    """
    M = _to_dense(L)
    ndof = M.shape[0]
    s = np.asarray(seed, dtype=float).reshape(-1)
    if s.size != ndof:
        raise ValueError(
            f"seed size {s.size} != operator dim {ndof}. For a cube seed pass the "
            "N³-reshaped field; for an srs seed pass the (n_nodes,) node field."
        )
    nrm = np.linalg.norm(s)
    if nrm < 1e-300:
        raise ValueError("seed has zero norm — nothing to decompose.")
    s_hat = s / nrm

    w, V = np.linalg.eigh(M)  # ascending eigenvalues, orthonormal eigenvectors
    proj = V.T @ s_hat        # coefficients; Σ proj² = 1 (orthonormal basis)
    weight = proj ** 2        # per-mode energy fraction

    null_mask = np.abs(w) < nullspace_tol
    null_frac = float(np.sum(weight[null_mask]))
    live_frac = float(1.0 - null_frac)

    peak_idx = int(np.argmax(weight))
    nonzero = np.abs(w) >= nullspace_tol
    smallest_nonzero = float(w[nonzero].min()) if np.any(nonzero) else float("nan")

    # spectral-weight profile: energy per eigenvalue band (linear bands over the
    # nonzero spectrum; the nullspace fraction is reported separately above).
    band_edges = None
    band_energy = None
    if np.any(nonzero):
        lo, hi = float(w[nonzero].min()), float(w.max())
        if hi > lo:
            band_edges = np.linspace(lo, hi, n_bands + 1)
            band_energy = np.zeros(n_bands)
            for b in range(n_bands):
                in_band = (w >= band_edges[b]) & (
                    w < band_edges[b + 1] if b < n_bands - 1 else w <= band_edges[b + 1]
                )
                band_energy[b] = float(np.sum(weight[in_band]))

    return SpectralLiveness(
        n_dof=ndof,
        nullspace_dim=int(np.sum(null_mask)),
        nullspace_tol=nullspace_tol,
        nullspace_energy_fraction=null_frac,
        live_energy_fraction=live_frac,
        peak_single_mode_weight=float(weight[peak_idx]),
        peak_single_mode_eigenvalue=float(w[peak_idx]),
        eigenvalue_min=float(w.min()),
        eigenvalue_max=float(w.max()),
        smallest_nonzero_eigenvalue=smallest_nonzero,
        band_edges=band_edges,
        band_energy_fraction=band_energy,
    )


def project_out_nullspace(
    seed: np.ndarray, L, *, nullspace_tol: float = 1e-9
) -> np.ndarray:
    """Return the component of `seed` ORTHOGONAL to L's frozen kernel — the part
    the operator actually governs. Used to build the nullspace-orthogonal positive
    control (prereg §4 route 3): evolving only the live part removes the frozen
    dead-leg's spurious 'PERSIST'. Returns a field of the SAME shape as `seed`."""
    M = _to_dense(L)
    ndof = M.shape[0]
    original_shape = np.asarray(seed).shape
    s = np.asarray(seed, dtype=float).reshape(-1)
    if s.size != ndof:
        raise ValueError(f"seed size {s.size} != operator dim {ndof}.")
    w, V = np.linalg.eigh(M)
    null_mask = np.abs(w) < nullspace_tol
    Vn = V[:, null_mask]
    s_null = Vn @ (Vn.T @ s)  # projection onto the kernel
    s_live = s - s_null       # the operator-governed complement
    return s_live.reshape(original_shape)


def localized_eigenmode(
    L, *, band: str = "low", nullspace_tol: float = 1e-9,
    max_participation_frac: float = 0.5,
) -> tuple[np.ndarray, float, float]:
    """Pick the MOST-LOCALIZED nonzero eigenmode of L in the requested spectral
    band — the operator's own bound-like configuration (prereg §4 route 1).

    Returns (eigenvector (ndof,), eigenvalue, participation_fraction) where
    participation_fraction = participation_ratio / ndof (smaller = more localized).

    band='low'  : search the lowest-|λ| nonzero modes (soft, long-wavelength —
                  the bound-STATE-like end; a low-λ localized mode oscillates
                  slowly without dispersing).
    band='high' : the stiffest modes (rapid oscillators; a localized high-λ mode
                  is a fast breather — also non-dispersing but high-frequency).

    Among the searched half-spectrum, returns the mode with the SMALLEST
    participation fraction that is below max_participation_frac (i.e. genuinely
    localized). Raises if none qualifies (⇒ the operator has no localized nonzero
    mode ⇒ a route-1 positive control is not constructible on this operator)."""
    M = _to_dense(L)
    ndof = M.shape[0]
    w, V = np.linalg.eigh(M)
    nonzero = np.abs(w) >= nullspace_tol
    idx = np.where(nonzero)[0]
    if idx.size == 0:
        raise ValueError("operator has no nonzero eigenvalues — no bound mode.")
    if band == "low":
        search = idx[: max(1, idx.size // 2)]
    elif band == "high":
        search = idx[idx.size // 2:]
    else:
        raise ValueError("band must be 'low' or 'high'.")
    best = None
    for j in search:
        u = V[:, j]
        p = u ** 2
        pr = 1.0 / float(np.sum(p ** 2))  # participation ratio
        frac = pr / ndof
        if best is None or frac < best[2]:
            best = (u, float(w[j]), frac)
    if best is None or best[2] >= max_participation_frac:
        raise ValueError(
            f"no localized nonzero eigenmode in the '{band}' band "
            f"(best participation fraction {best[2] if best else float('nan'):.3f} "
            f"≥ threshold {max_participation_frac}). A route-1 positive control is "
            "not constructible on this operator."
        )
    return best
