"""EP-CMRR body-force driver helpers (U5).

A thin body-force driver over the CERTIFIED Master-Equation medium
(`ave.core.master_equation_fdtd.MasterEquationFDTD`). No new physics and no
engine modification: the driver REUSES the certified primitives verbatim
(`eng.c_eff_squared`, `eng._laplacian`, `eng.saturation_kernel`) and only adds a
body-force source `f(x)` to the RHS of the Master Equation
(`∂²V/∂t² = c_eff²·∇²V + f`) — the source term the driven wave equation already
carries. It reimplements no stencil, stepper, or kernel (Rule-14 anti-rebuild).

Smooth-drive note (frozen prereg): the uniform and linear-gradient drives satisfy
`∇²V = 0` for their analytic particular solution `V_p = ½·f(x)·t²`, so they launch
NO propagating wave — the response is the (analytically exact) rigid/tidal
profile. PML damping is therefore NOT applied here (there is no outgoing wave to
absorb; the PML would only seed a spurious boundary gradient). Strain is still
read on the PML-excluded deep interior (Rule-10 PML-exclusion corollary).
"""

from __future__ import annotations

import numpy as np


def body_force_step(eng, f: np.ndarray) -> None:
    """One leapfrog step of the CERTIFIED medium WITH a body-force source `f`.

    Reuses `eng.c_eff_squared` (certified kernel) and `eng._laplacian` (certified
    7-point stencil) verbatim; adds `dt²·f` (the body-force source). PML damping
    is intentionally not applied — the smooth drives launch no wave (see module
    docstring). The engine module itself is NOT modified.
    """
    c_eff_sq = eng.c_eff_squared(eng.V)
    lap = eng._laplacian(eng.V)
    v_new = 2.0 * eng.V - eng.V_prev + (eng.dt**2) * (c_eff_sq * lap + f)
    eng.V_prev = eng.V.copy()
    eng.V = v_new
    eng.time += eng.dt
    eng.step_count += 1


def evolve_body_force(eng, f: np.ndarray, n_steps: int) -> None:
    """Evolve the certified medium under a fixed body force `f` for `n_steps`."""
    for _ in range(n_steps):
        body_force_step(eng, f)


def uniform_body_force(eng, f0: float) -> np.ndarray:
    """Common-mode drive: a spatially-uniform body force `f(x) ≡ f0`."""
    return np.full((eng.N, eng.N, eng.N), float(f0), dtype=np.float64)


def gradient_body_force(eng, gamma: float, axis: int = 0) -> np.ndarray:
    """Differential (tidal) drive: a pure linear gradient centred at the box
    centre — `f(i) = gamma·(i − i_center)` along `axis`, zero elsewhere.

    `∇²f = 0`, so the analytic response `V_p = ½·f(x)·t²` also has `∇²V_p = 0`
    (no wave). The differential strain is uniform `= gamma·t²/(2·V_yield)`.
    """
    idx = np.arange(eng.N, dtype=np.float64)
    i_c = (eng.N - 1) / 2.0
    line = gamma * (idx - i_c)
    shape = [1, 1, 1]
    shape[axis] = eng.N
    return np.broadcast_to(line.reshape(shape), (eng.N, eng.N, eng.N)).copy()


def _interior_slice(eng, margin_cells: int):
    """A PML-excluded deep-interior slice (Rule-10 PML-exclusion corollary)."""
    lo = eng.pml_thickness + margin_cells
    hi = eng.N - eng.pml_thickness - margin_cells
    return (slice(lo, hi),) * 3


def differential_strain_field(eng, margin_cells: int = 4) -> np.ndarray:
    """`A_strain(x) = |∇V(x)|·dx / V_yield` (central differences) on the
    PML-excluded deep interior. Rigid (uniform) response → ~0; tidal → ∝ tide.
    """
    gx, gy, gz = np.gradient(eng.V, eng.dx)
    grad_mag = np.sqrt(gx * gx + gy * gy + gz * gz)
    a = grad_mag * eng.dx / eng.V_yield
    return a[_interior_slice(eng, margin_cells)]


def strain_keyed_S(eng, a_strain: np.ndarray) -> np.ndarray:
    """Feed the differential strain through the CERTIFIED `√(1−A²)` kernel form.

    `eng.saturation_kernel(V)` computes `S(|V|/V_yield)`; passing
    `a_strain·V_yield` makes its internal `A == a_strain`, so the certified,
    clipped `√(1−A²)` form is exercised on the EP-correct (differential) variable.
    """
    return eng.saturation_kernel(a_strain * eng.V_yield)


def magnitude_keyed_S(eng, f: np.ndarray, f_yield: float, margin_cells: int = 4) -> np.ndarray:
    """P11 SABOTAGE keying: key the certified kernel on the DRIVE MAGNITUDE `|f|`
    (force magnitude) instead of the strain — `A_sab = |f|/f_yield` — on the
    PML-excluded deep interior. Under a uniform drive `|f|` is nonzero everywhere,
    so this loads (S<1) and LEG-A FIRES.
    """
    a_sab = np.abs(f) / float(f_yield)
    a_sab = a_sab[_interior_slice(eng, margin_cells)]
    return eng.saturation_kernel(a_sab * eng.V_yield)
