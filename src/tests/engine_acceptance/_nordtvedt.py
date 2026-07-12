"""Nordtvedt-η driver helpers (strain-field register).

A thin measurement layer over the LANDED two-way back-reaction solver
(`ave.gravity.backreaction`, #86). No new physics and NO engine modification: the
helpers REUSE the certified public entry points VERBATIM
(`solve_backreaction`, `gaussian_blob`, `field_energy_density`,
`gw_propagation._build_native_grad_div`, `graded_vacuum_network.stiffness_profile`)
and only ASSEMBLE the SAME divergence-form operator the solver builds
(`gw_propagation.py:698-701`, `L = Div·diag(tile(D,3))·Grad`, symmetrized) to read
the field-side Gauss flux OUT of the converged strain. It reimplements no stencil,
stepper, or kernel (Rule-14 anti-rebuild).

FROZEN prereg: research/2026-07-11_nordtvedt-eta_prereg_FROZEN.md (frozen by push
BEFORE this driver existed; the EP-CMRR / tethered_pivot_x34b pattern).

SECTOR = A1 dilatation / gravity, sub-yield. REGISTER-2 = strain-field-distributed
energy (the gravitational binding energy `U_bind = ∫½g|∇ε₁₁|²`, living in the
substrate strain field, in no knot). The Nordtvedt fraction `f = U_bind/(M+U_bind)`
is DERIVED from the solver's own energy ledger, not asserted.

The two registers are measured by DIFFERENT routes (the crux):
  * m_g (gravitating charge)  = Σ_interior(L @ ε₁₁)         [FIELD-side Gauss flux]
  * m_i (inertial/total energy) = M_matter + U_bind          [ENERGY-side ledger]
The one-ledger identity is that these two independently-computed registers agree
(η ≈ 0). Per P10 this is ENTAILED by the single-T₀₀ construction ⇒ CERTIFICATION.
"""

from __future__ import annotations

import numpy as np
import scipy.sparse as sparse

from ave.core.categorization import (
    LedgerKind,
    PairingKind,
    classify_ledger_pairing,
    require_ledger_pairing,
)
from ave.gravity.backreaction import (
    _fit_inverse_power_model,
    field_energy_density,
    gaussian_blob,
    solve_backreaction,
)
from ave.gravity.gw_propagation import _build_native_grad_div
from ave.solvers.graded_vacuum_network import stiffness_profile


# Live #651 certification pairing (flux vs M+U) — ENTAILED under ADD Picard source.
CERTIFICATION_PAIRING = classify_ledger_pairing(
    LedgerKind.FAR_FIELD_FLUX, LedgerKind.TOTAL_ENERGY_ADD
)
# Mixed-register exposure (flux vs M_eff) — FIREABLE reconciliation, not certification.
MIXED_REGISTER_PAIRING = classify_ledger_pairing(
    LedgerKind.FAR_FIELD_FLUX, LedgerKind.ADM_DEFICIT
)
assert CERTIFICATION_PAIRING.kind is PairingKind.ENTAILED
assert MIXED_REGISTER_PAIRING.kind is PairingKind.FIREABLE
# Touch the enforcer so import-time wiring stays live under refactors.
require_ledger_pairing(
    LedgerKind.FAR_FIELD_FLUX,
    LedgerKind.TOTAL_ENERGY_ADD,
    expect=PairingKind.ENTAILED,
)


def build_grad_div(N: int):
    """The native diamond-K4 Grad/Div (the SAME operator the solve uses; no
    Cartesian gradient — the K4 checkpoint). Reused verbatim."""
    return _build_native_grad_div(N, instrument_scope="nordtvedt-eta strain-field register")


def normalized_blob(N: int, sigma: float, m_target: float) -> np.ndarray:
    """A Gaussian energy blob renormalized to a FIXED lattice rest energy
    (`Σ T₀₀^matter == m_target`), so the family holds composition/rest energy fixed
    and varies ONLY the binding fraction f. Reuses `gaussian_blob` verbatim."""
    b = gaussian_blob(N, sigma=sigma, amplitude=1.0)
    return b * (float(m_target) / float(b.sum()))


def radius_grid(N: int) -> np.ndarray:
    """Radius from the cube centre (sites), matching `solve_backreaction`'s `rr`."""
    c = N // 2
    i, j, k = np.indices((N, N, N))
    return np.sqrt((i - c) ** 2 + (j - c) ** 2 + (k - c) ** 2)


def interior_mask(N: int) -> np.ndarray:
    """All cells except the 1-cell Dirichlet boundary layer (matches the solver's
    `intr` set — the boundary is held ε=0)."""
    m = np.ones((N, N, N), bool)
    m[0, :, :] = m[-1, :, :] = m[:, 0, :] = m[:, -1, :] = m[:, :, 0] = m[:, :, -1] = False
    return m


def solve_config(N: int, T00_matter: np.ndarray, *, g_self: float, s_min: float) -> dict:
    """Run the landed two-way back-reaction solve for one configuration (verbatim
    public entry point)."""
    return solve_backreaction(
        N=N, T00_matter=T00_matter, g_self=g_self, S_min=s_min, return_fields=True
    )


def stiffness_operator(N: int, eps11: np.ndarray, Grad, Div, *, s_min: float):
    """Assemble the SAME divergence-form gravitational operator the solver builds
    on the CONVERGED field: `L = Div·diag(tile(D,3))·Grad`, symmetrized, with the
    canonical bulk stiffness `D = stiffness_profile(A, 0.5, S_min) = 1/S(A)`
    (`gw_propagation.py:698-701`). `L @ ε₁₁` returns T₀₀^total on the interior (to
    the relaxation residual) — the field-side Gauss integrand."""
    A_flat = np.clip(eps11.reshape(-1), 0.0, 1.0)
    D = stiffness_profile(A_flat, exponent=0.5, S_min=s_min)
    Dexp = sparse.diags(np.tile(D, 3))
    L = (Div @ Dexp @ Grad).tocsr()
    return 0.5 * (L + L.T)


def gravitating_charge_flux(eps11: np.ndarray, L, mask: np.ndarray) -> float:
    """m_g — the FIELD-side far-field gravitating charge: apply the gravitational
    operator to the solved strain and integrate the flux over the source-enclosing
    interior, `Σ_interior (L @ ε₁₁)` (the discrete Gauss flux)."""
    Leps = (L @ eps11.reshape(-1))
    return float(Leps.reshape(-1)[mask.reshape(-1)].sum())


def enclosed_flux_vs_radius(eps11: np.ndarray, L, T00_total: np.ndarray, rr: np.ndarray, radii):
    """Enclosed field flux `Σ_{r≤R}(L@ε)` and enclosed source `Σ_{r≤R}T₀₀^total`
    vs radius — a genuine monopole PLATEAU read (the far-field gravitating charge is
    radius-independent once the source is enclosed)."""
    Leps = (L @ eps11.reshape(-1)).reshape(eps11.shape)
    flux = [float(Leps[rr <= R].sum()) for R in radii]
    src = [float(T00_total[rr <= R].sum()) for R in radii]
    return flux, src


def energy_ledger(T00_matter: np.ndarray, eps11: np.ndarray, Grad, *, g_self: float) -> dict:
    """m_i — the ENERGY-side ledger: matter rest energy `Σ T₀₀^matter` + the
    strain-field energy functional `U_bind = Σ½g|∇ε₁₁|²` (via `field_energy_density`
    verbatim). Also returns the binding-deficit `M_eff = M − U_bind` (the SEPARATE
    register whose far-field mismatch is the surfaced flag)."""
    M = float(T00_matter.sum())
    U = float(field_energy_density(eps11, Grad, kappa=g_self).sum())
    return {"M_matter": M, "U_bind": U, "m_i": M + U, "M_eff": M - U}


def naive_monopole_K(eps11: np.ndarray, rr: np.ndarray, *, r_in: float, r_out: float):
    """DIAGNOSTIC ONLY (not a gate): the naive exterior a+b/r monopole fit
    (`_fit_inverse_power_model`, the #86 Check-1 method). Carries the documented
    finite-source window systematic (a diffuse blob's tail contaminates the fixed
    exterior window and under-reads b) — which is WHY the artifact-free Gauss flux,
    not this fit, is the certification instrument."""
    b, a, r2 = _fit_inverse_power_model(eps11, rr, r_in, r_out, 1.0)
    return float(b), float(r2)


def eta_slope(f, ratio) -> float:
    """The Nordtvedt detector: η = slope of `(ratio/ratio_ref − 1)` vs `f` across the
    family (ref = smallest-f member). ratio = m_g/m_i."""
    f = np.asarray(f, float)
    ratio = np.asarray(ratio, float)
    order = np.argsort(f)
    f = f[order]
    ratio = ratio[order]
    y = ratio / ratio[0] - 1.0
    A = np.vstack([f - f[0], np.ones_like(f)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(coef[0])
