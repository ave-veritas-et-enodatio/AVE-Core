"""Cross-sector coupling primitives + CoupledK4Cosserat converter integration."""

import numpy as np

from ave.core.cross_sector_coupling import (
    KAPPA_TILDE,
    combined_strain_amplitude,
    effective_shear_director,
    gyrotropic_converter_forces,
    saturation_front_window,
    trilinear_buckle_forces,
)
from ave.core.constants import R_II
from ave.core.cross_sector_coupling import scale_cosserat_to_front
from ave.topological.k4_cosserat_coupling import CoupledK4Cosserat, _cosserat_A_squared


def test_trilinear_f_V_nonzero_at_zero_V_with_shear_and_omega():
    N = 8
    dx = 1.0
    g = np.ones((N, N, N)) * 0.5
    V = np.zeros((N, N, N))
    x = np.linspace(0, 2 * np.pi, N)
    y = np.linspace(0, 2 * np.pi, N)
    w = np.zeros((N, N, N, 3))
    w[..., 1] = np.sin(x)[:, None, None] * np.cos(y)[None, :, None]
    omega = np.zeros((N, N, N, 3))
    omega[..., 2] = np.cos(x)[:, None, None] * np.sin(y)[None, :, None]
    f_V, _, _ = trilinear_buckle_forces(V, w, omega, g, dx)
    assert np.max(np.abs(f_V)) > 1e-8


def test_gyrotropic_f_V_nonzero_with_microrotation():
    N = 8
    dx = 1.0
    g = np.ones((N, N, N)) * 0.5
    V = np.zeros((N, N, N))
    y = np.linspace(0, 2 * np.pi, N)
    w = np.zeros((N, N, N, 3))
    w[..., 2] = np.sin(y)[None, :, None]  # ∂_y w_z ≠ 0 ⇒ Ω_w ≠ 0
    f_V, f_w = gyrotropic_converter_forces(V, w, g, dx)
    assert np.max(np.abs(f_V)) > 1e-8
    # f_w back-reaction vanishes at V≡0 (gV=0) — energize path is f_V only


def test_combined_strain_uses_cosserat_when_k4_zero():
    V_sq = np.zeros((4, 4, 4))
    A_cos = np.ones((4, 4, 4)) * 0.25
    A = combined_strain_amplitude(V_sq, A_cos, 1.0)
    assert np.allclose(A, 0.5)


def test_coupled_engine_converter_energizes_v_inc_from_cosserat_seed():
    N = 12
    sim_off = CoupledK4Cosserat(N=N, pml=3, use_trilinear_converter=False, disable_cosserat_lc_force=True)
    sim_on = CoupledK4Cosserat(
        N=N,
        pml=3,
        use_trilinear_converter=True,
        converter_mode="trilinear",
        disable_cosserat_lc_force=True,
    )
    x = np.linspace(0, 2 * np.pi, N)
    y = np.linspace(0, 2 * np.pi, N)
    u_pat = 0.35 * np.sin(x)[:, None, None] * np.cos(y)[None, :, None]
    o_pat = 0.30 * np.cos(x)[:, None, None] * np.sin(y)[None, :, None]
    for sim in (sim_off, sim_on):
        sim.cos.u[..., 1] += u_pat
        sim.cos.omega[..., 2] += o_pat
        A_cos_sq = _cosserat_A_squared(
            sim.cos.u, sim.cos.omega, sim.cos.dx, sim.cos.omega_yield, sim.cos.epsilon_yield
        )
        sim.cos.u, sim.cos.omega = scale_cosserat_to_front(sim.cos.u, sim.cos.omega, A_cos_sq, target=R_II)
        sim.freeze_converter_wall()
    f_V0, _, _ = sim_on._compute_converter_forces()
    assert np.max(np.abs(f_V0)) > 1e-10
    v0_off = float(np.max(np.abs(sim_off.k4.V_inc)))
    for _ in range(40):
        sim_off.step()
        sim_on.step()
    v_end_off = float(np.max(np.abs(sim_off.k4.V_inc)))
    v_end_on = float(np.max(np.abs(sim_on.k4.V_inc)))
    assert v0_off < 1e-12
    assert v_end_on > max(v_end_off, 1e-6)


def test_effective_shear_director_uses_omega_dot_when_u_zero():
    u = np.zeros((4, 4, 4, 3))
    omega = np.ones((4, 4, 4, 3)) * 0.1
    od = np.ones((4, 4, 4, 3)) * 0.2
    w = effective_shear_director(u, omega, od)
    assert np.allclose(w, od)


def test_kappa_tilde_is_six_fifths():
    assert abs(KAPPA_TILDE - 6.0 / 5.0) < 1e-15


def test_front_window_peaks_near_R_II():
    from ave.core.constants import R_II

    A = np.linspace(0, 1, 50)
    g = saturation_front_window(A, center=R_II, width=0.18)
    assert g[np.argmin(np.abs(A - R_II))] == np.max(g)
