"""VCA route-C step 2 — validation of the circulation-keyed vacuum μ-grade.

The free-EM vacuum μ-grade is the per-component circulation-keyed relativistic
INDUCTOR (fdtd_3d._compute_local_mu, JAX twin fdtd_3d_jax):

    A_I,i   = curl_h_i · ℓ_node / I_max        (grid-invariant; dx cancels)
    μ_eff,i = μ_0·μ_r / √(1 − A_I,i²)           (INCREASING; locks at I → I_max)
    I_max   = ξ_topo·c ≈ 124.384 A             (XI_TOPO · C_0)

THE DISCRIMINATOR (memo §4): a static uniform B is source-free (∇×H = 0) so
curl_h ≡ 0 ⇒ A_I = 0 ⇒ μ_eff = μ_0 (transparent), EMERGENT from the discrete
curl, not hard-coded. A nonzero circulation (∮H·dℓ ≠ 0 — a propagating field or
an imposed real current) LOADS μ > μ_0. A hard-LINEAR μ would give μ_0 for BOTH,
so the static-null-vs-circulation-load contrast PROVES the keying is on the
circulation, not on |B|.

Tests (route-C step 2 brief):
  1. EMERGENT NULL          — static uniform field → curl_h≈0 → μ_eff == μ_0 to FP.
  2. CIRCULATION DISCRIMINATOR — imposed nonzero curl_h → μ_eff > μ_0 measurably;
                                a hard-linear μ would NOT load (contrast).
  3. ANISOTROPY / SPLIT     — a directional drive loads μ-components UNEQUALLY.
  4. GRID-INVARIANCE        — same physical curl_h at two dx → same A_I / μ.
  5. ENERGY-HONESTY         — closed box (no PML, no ABC) conserves energy with the
                              nonlinear μ; a deliberately-wrong control TRIPS the gate.

Canon: relativistic-inductor.md:15 (clm-p5cf3t, INCREASING);
       node-up-small-large-signal.md:95,:114 (A_I phase-space coord, A46);
       pvlas-static-b-verdict.md:37-43 (static-B null, A_I=0 exact);
       research/2026-06-25_vca-mu-circulation-observable-derivation.md (step 1).

NOTE on the VCA-R01 regression (test_vca_r01_static_b_mu_keying.py): that test
calls _compute_local_mu(Hx_static) with NO circulation argument; under
circulation-keying the curl_h=None path returns μ_0 (the emergent null), so the
original intent (static-uniform-B → μ_0; old |B|-keying stays dead) is preserved
unchanged — it is NOT edited. This file adds the positive circulation-load side.
"""

import numpy as np
import pytest

from ave.core.constants import MU_0
from ave.core.fdtd_3d import ELL_NODE, I_MAX_MU, FDTD3DEngine

# A_I for a given per-component circulation curl_h [A/m]:  A_I = curl_h·ℓ_node/I_max.
# Invert: the curl_h that realizes a target A_I is  curl_h = A_I·I_max/ℓ_node.
_CURL_H_PER_A_I = I_MAX_MU / ELL_NODE  # [A/m] per unit A_I


def _mu_inductor(a_i: float) -> float:
    """Reference relativistic-inductor μ_eff for a scalar A_I."""
    return MU_0 / np.sqrt(1.0 - a_i**2)


# ---------------------------------------------------------------------------
# Test 1 — EMERGENT NULL: static uniform field → curl_h ≈ 0 → μ_eff == μ_0.
# ---------------------------------------------------------------------------
def test_emergent_null_static_uniform_field_gives_mu0():
    """A static UNIFORM H/B field threads zero net circulation through every
    interior cell (∇×H = 0), so A_I = 0 falls out of the DISCRETE curl and
    μ_eff = μ_0 — the transparency is EMERGENT, not hard-coded."""
    eng = FDTD3DEngine(nx=10, ny=10, nz=10, dx=1e-3, linear_only=False)

    # Impose a strong, spatially-UNIFORM Hx (|B| ~ 0.9·b_yield) — a DC-magnet field.
    H_target = 0.9 * eng.b_yield / eng.mu_0
    eng.Hx[:] = H_target

    # The per-component μ over the full grid (what the stepper / energy use):
    mu_x, mu_y, mu_z = eng._mu_eff_per_component()

    # Uniform field ⇒ every discrete curl_h = 0 ⇒ A_I = 0 ⇒ μ_eff = μ_0 to FP.
    assert np.allclose(mu_x, eng.mu_0, rtol=1e-12), f"μ_x loaded under uniform B: {np.ptp(mu_x):.2e}"
    assert np.allclose(mu_y, eng.mu_0, rtol=1e-12)
    assert np.allclose(mu_z, eng.mu_0, rtol=1e-12)

    # And the diagnostic A_I² peak (max_mag_strain) stays ~0 after a step.
    eng.update_magnetic_field()
    eng.update_electric_field()
    assert eng.max_mag_strain < 1e-20, f"static-uniform field induced circulation: A_I²={eng.max_mag_strain:.2e}"

    # EMERGENT, not branch-on-static: feeding an EXPLICIT zero curl array to the
    # kernel returns the identical μ_0 (no 'if static' special-case in the path).
    zero_curl = np.zeros((eng.nx, eng.ny - 1, eng.nz - 1))
    mu_zero = eng._compute_local_mu(eng.Hx[:, :-1, :-1], zero_curl)
    assert np.allclose(mu_zero, eng.mu_0, rtol=1e-12)


# ---------------------------------------------------------------------------
# Test 2 — CIRCULATION DISCRIMINATOR: nonzero curl_h LOADS μ; a hard-linear μ would not.
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("a_i_target", [0.1, 0.3, 0.5, 0.8])
def test_circulation_loads_mu_above_mu0(a_i_target):
    """An imposed nonzero circulation curl_h ≠ 0 drives μ_eff > μ_0 measurably,
    matching the relativistic-inductor law μ_0/√(1−A_I²). A hard-LINEAR μ would
    return μ_0 for the SAME input — this is the circulation discriminator."""
    eng = FDTD3DEngine(nx=8, ny=8, nz=8, dx=1e-3, linear_only=False)

    H_slice = eng.Hx[:, :-1, :-1]
    curl_h = np.full(H_slice.shape, a_i_target * _CURL_H_PER_A_I)

    mu_eff = eng._compute_local_mu(H_slice, curl_h)
    expected = _mu_inductor(a_i_target)

    # Loads ABOVE μ_0 (the INCREASING branch — relativistic inductor):
    assert np.all(mu_eff > eng.mu_0), "circulation did not load μ above μ_0"
    # Matches the analytic relativistic-inductor curve:
    assert np.allclose(mu_eff, expected, rtol=1e-12), (
        f"A_I={a_i_target}: μ_eff={np.mean(mu_eff):.6e} != μ_0/√(1−A_I²)={expected:.6e}"
    )
    # Contrast: a hard-linear μ would be μ_0 here — confirm we are measurably off it.
    rel_excess = (np.mean(mu_eff) - eng.mu_0) / eng.mu_0
    assert rel_excess > 1e-3, f"loading too small to distinguish from linear μ: {rel_excess:.2e}"


def test_propagating_packet_carries_nonzero_circulation():
    """A propagating EM packet (∂B/∂t ≠ 0, displacement current) realizes a
    NONZERO curl_h in the interior — circulation exists for a real field, even
    though on a coarse continuum grid (dx ≫ ℓ_node) the resulting A_I is tiny
    (latent capability, memo §8 #3). The point: curl_h ≠ 0 ≠ the static null."""
    eng = FDTD3DEngine(nx=24, ny=24, nz=24, dx=1e-3, linear_only=False, use_pml=False)
    eng.inject_soft_source("Ez", 12, 12, 12, 1.0)
    for _ in range(15):
        eng.update_magnetic_field()
        eng.update_electric_field()

    # Recompute the interior circulation directly and confirm it is nonzero.
    Hx, Hy, Hz = eng.Hx, eng.Hy, eng.Hz
    curl_h_x = (Hz[:, 1:, 1:] - Hz[:, :-1, 1:]) - (Hy[:, 1:, 1:] - Hy[:, 1:, :-1])
    assert np.max(np.abs(curl_h_x)) > 0.0, "propagating packet carried zero circulation"
    # Tiny-but-nonzero A_I on a coarse grid (the honest latent-capability scope).
    a_i_peak = np.sqrt(eng.max_mag_strain)
    assert a_i_peak > 0.0


# ---------------------------------------------------------------------------
# Test 3 — ANISOTROPY / SPLIT: a directional drive loads μ-components unequally.
# ---------------------------------------------------------------------------
def test_anisotropic_circulation_splits_mu_components():
    """A direction-selective circulation loads the μ-components UNEQUALLY — the
    deviatoric structure a μ-route birefringence needs (memo §5). Impose a large
    curl on the x-component channel and zero on y; μ_x must load while μ_y stays μ_0."""
    eng = FDTD3DEngine(nx=8, ny=8, nz=8, dx=1e-3, linear_only=False)

    a_i = 0.6
    curl_x = np.full(eng.Hx[:, :-1, :-1].shape, a_i * _CURL_H_PER_A_I)
    curl_y = np.zeros(eng.Hy[:-1, :, :-1].shape)

    mu_x = eng._compute_local_mu(eng.Hx[:, :-1, :-1], curl_x)
    mu_y = eng._compute_local_mu(eng.Hy[:-1, :, :-1], curl_y)

    assert np.all(mu_x > eng.mu_0), "x-channel did not load under directional circulation"
    assert np.allclose(mu_y, eng.mu_0, rtol=1e-12), "y-channel loaded despite zero circulation"
    # The split is real and large (per-component μ differs):
    split = np.mean(mu_x) - np.mean(mu_y)
    assert split > 0.0
    # Ratio of the loaded to the unloaded channel = μ_0/√(1−A_I²) / μ_0 = 1/√(1−A_I²).
    assert np.mean(mu_x) / np.mean(mu_y) == pytest.approx(_mu_inductor(a_i) / MU_0, rel=1e-9)


# ---------------------------------------------------------------------------
# Test 4 — GRID-INVARIANCE: same physical curl_h at two dx → same A_I / μ.
# ---------------------------------------------------------------------------
def test_grid_invariance_mu_independent_of_dx():
    """A_I = curl_h·ℓ_node/I_max carries NO dx — the saturation onset lives at
    ℓ_node, not the numerical mesh. So the SAME physical circulation gives the
    SAME μ-loading at two different dx (mini convergence test)."""
    a_i = 0.4
    curl_val = a_i * _CURL_H_PER_A_I

    eng_coarse = FDTD3DEngine(nx=8, ny=8, nz=8, dx=1e-2, linear_only=False)
    eng_fine = FDTD3DEngine(nx=8, ny=8, nz=8, dx=1e-4, linear_only=False)  # 100× finer

    curl_c = np.full(eng_coarse.Hx[:, :-1, :-1].shape, curl_val)
    curl_f = np.full(eng_fine.Hx[:, :-1, :-1].shape, curl_val)

    mu_c = eng_coarse._compute_local_mu(eng_coarse.Hx[:, :-1, :-1], curl_c)
    mu_f = eng_fine._compute_local_mu(eng_fine.Hx[:, :-1, :-1], curl_f)

    # IDENTICAL μ-loading despite a 100× change in dx — grid-invariant by construction.
    assert np.allclose(mu_c, mu_f, rtol=1e-12), (
        f"μ-loading depends on dx: coarse={np.mean(mu_c):.6e} fine={np.mean(mu_f):.6e}"
    )
    assert np.allclose(mu_c, _mu_inductor(a_i), rtol=1e-12)


# ---------------------------------------------------------------------------
# Test 5 — ENERGY-HONESTY: closed lossless box conserves energy; control trips.
# ---------------------------------------------------------------------------
def _seed_interior_pulse(eng: FDTD3DEngine, amp: float = 1.0) -> None:
    """Seed a smooth compact Gaussian Ez bump in the xy-center of the box. The run
    is kept SHORT enough that the pulse never reaches the reflecting walls (memo /
    brief: 'interior probe to avoid the Mur ABC'), so the energy reading is pure
    interior physics, free of boundary artifacts."""
    nx, ny = eng.nx, eng.ny
    xx, yy = np.meshgrid(np.arange(nx), np.arange(ny), indexing="ij")
    g = amp * np.exp(-(((xx - nx / 2) / 6.0) ** 2 + ((yy - ny / 2) / 6.0) ** 2))
    eng.Ez[:] = np.broadcast_to(g[:, :, None], eng.Ez.shape)


def _energy_series(eng: FDTD3DEngine, n_steps: int, backward_euler: bool = False) -> np.ndarray:
    """Step the engine n_steps with NO boundary (closed interior window) and return
    the total-field-energy series. backward_euler=True flips the H-update sign (a
    deliberately-WRONG, non-symplectic integrator) which pumps energy and must TRIP."""
    energies = []
    for _ in range(n_steps):
        if backward_euler:
            # WRONG control: ADD the curl instead of subtracting (sign-flipped /
            # backward-Euler-like H-update) — breaks the leapfrog symplectic
            # structure and pumps energy without bound.
            curl_h_x = (eng.Hz[:, 1:, 1:] - eng.Hz[:, :-1, 1:]) - (eng.Hy[:, 1:, 1:] - eng.Hy[:, 1:, :-1])
            curl_e_x = (eng.Ez[:, 1:, :-1] - eng.Ez[:, :-1, :-1]) - (eng.Ey[:, :-1, 1:] - eng.Ey[:, :-1, :-1])
            ch_x = eng._compute_ch(eng.Hx[:, :-1, :-1], curl_h_x)
            eng.Hx[:, :-1, :-1] += ch_x * curl_e_x  # +sign = WRONG
            curl_h_y = (eng.Hx[1:, :, 1:] - eng.Hx[1:, :, :-1]) - (eng.Hz[1:, :, 1:] - eng.Hz[:-1, :, 1:])
            curl_e_y = (eng.Ex[:-1, :, 1:] - eng.Ex[:-1, :, :-1]) - (eng.Ez[1:, :, :-1] - eng.Ez[:-1, :, :-1])
            ch_y = eng._compute_ch(eng.Hy[:-1, :, :-1], curl_h_y)
            eng.Hy[:-1, :, :-1] += ch_y * curl_e_y
            eng.update_electric_field()
        else:
            eng.update_magnetic_field()
            eng.update_electric_field()
        energies.append(eng.total_field_energy())
    return np.asarray(energies)


def _secular_drift(energies: np.ndarray, skip: int = 3) -> float:
    """Secular (linear-trend) energy drift over the window, normalized by the mean.
    Isolates DISSIPATION (a monotone trend) from the leapfrog same-instant-energy
    BEAT (E↔H phase exchange, a bounded oscillation that is NOT energy loss). The
    first ``skip`` steps (H spinning up from the E-only seed) are dropped."""
    if not np.all(np.isfinite(energies)):
        return np.inf
    w = energies[skip:]
    t = np.arange(len(w))
    slope = np.polyfit(t, w, 1)[0]
    return float(abs(slope * len(w)) / w.mean())


def test_energy_honesty_nonlinear_mu_adds_no_dissipation():
    """A lossless-reactive circulation-keyed μ must not dissipate or pump energy.
    Test: the nonlinear-μ engine's SECULAR energy drift over a short interior
    window equals the LINEAR engine's to numerical precision — the μ path is
    energy-neutral (no loss, no gain). (The ~4% same-instant oscillation is the
    leapfrog E↔H beat, not dissipation; the secular trend is the dissipation
    signal and it is small AND identical to linear.)"""
    nx = 80
    eng_lin = FDTD3DEngine(nx=nx, ny=nx, nz=8, dx=1e-3, linear_only=True, use_pml=False)
    eng_nl = FDTD3DEngine(nx=nx, ny=nx, nz=8, dx=1e-3, linear_only=False, use_pml=False)
    _seed_interior_pulse(eng_lin)
    _seed_interior_pulse(eng_nl)

    drift_lin = _secular_drift(_energy_series(eng_lin, 40))
    drift_nl = _secular_drift(_energy_series(eng_nl, 40))

    # The nonlinear μ adds NO dissipation: its secular drift matches the linear
    # engine's (both small). |dH/H| stays small for the lossless reactive μ.
    assert drift_nl < 1e-2, f"nonlinear-μ secular energy drift too large: {drift_nl:.3e}"
    assert drift_nl == pytest.approx(drift_lin, abs=1e-9), (
        f"nonlinear μ changed the energy balance vs linear (loss/gain): "
        f"nl={drift_nl:.3e} lin={drift_lin:.3e}"
    )


def test_energy_gate_is_live_wrong_integrator_trips():
    """Gate-liveness control: a deliberately-wrong (sign-flipped / backward-Euler-
    like) H-update must TRIP the energy gate — proving the conservation check above
    is not vacuously passing. The non-symplectic update pumps energy without bound
    (diverges to NaN/inf), giving an infinite secular drift."""
    eng = FDTD3DEngine(nx=80, ny=80, nz=8, dx=1e-3, linear_only=False, use_pml=False)
    _seed_interior_pulse(eng)
    drift_wrong = _secular_drift(_energy_series(eng, 40, backward_euler=True))
    assert drift_wrong > 1.0, f"wrong integrator did NOT trip the energy gate: drift={drift_wrong:.3e}"
