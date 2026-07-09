"""Reproduction gate for the [HALF-FLUX-ECHO] verdict.

Pins the load-bearing numbers of the three half-flux framings so the verdict does not
rest on ephemeral scratchpad artifacts (adversarial-audit finding #6). See
research/2026-07-08_electron-halfflux-selection_result.md and the drivers
src/scripts/vol_2_subatomic/electron_halfflux_{k4_quantization,texture_weld,hopf_phase}.py
"""

from __future__ import annotations

import importlib.util
import os

import numpy as np
import pytest

_SCRIPTS = os.path.join(os.path.dirname(__file__), "..", "scripts", "vol_2_subatomic")


def _load(name):
    path = os.path.join(_SCRIPTS, name)
    spec = importlib.util.spec_from_file_location(name.replace(".py", ""), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


k4 = _load("electron_halfflux_k4_quantization.py")
weld = _load("electron_halfflux_texture_weld.py")

WINDINGS = [(2, 3), (2, 2), (1, 1), (3, 5), (1, 2)]


def test_no_half_angle_lift_on_path():
    """Gate (2): the whole path reads the SU(2) sign by continuity, never cos(phi/2)."""
    from ave.topological.k4_lattice_holonomy import uses_analytic_qbody
    assert uses_analytic_qbody() is False


def test_spin_loop_winding_independent():
    """The statistics sign is -1 for EVERY winding (belt trick; the ECHO signature)."""
    for (p, q) in WINDINGS:
        assert np.isclose(weld.spin_loop_monodromy(p, q), -1.0, atol=1e-6), (p, q)
        assert np.isclose(k4.spatial_2pi_loop_flux(p, q)["flux_over_flux0"], 0.5), (p, q)


def test_texture_q_keyed():
    """The texture psi-cycle IS q-keyed: odd q -> -1 (half flux), even q -> +1 (integer)."""
    assert np.isclose(weld.texture_psi_monodromy(3), -1.0, atol=1e-6)   # (2,3) odd
    assert np.isclose(weld.texture_psi_monodromy(2), +1.0, atol=1e-6)   # (2,2) even
    assert np.isclose(k4.texture_flux_continuum(2, 3)["flux_over_flux0"], 0.5)
    assert np.isclose(k4.texture_flux_continuum(2, 2)["flux_over_flux0"], 0.0)


def test_k4_equals_continuum_the_half_is_not_lattice_sourced():
    """DECISIVE: the texture flux is identical on the K4 lattice walk and in the
    continuum sigma-model for EVERY winding => the 1/2 is SO(3)-Z2, not K4-forced."""
    for (p, q) in WINDINGS:
        c = k4.texture_flux_continuum(p, q)["flux_over_flux0"]
        lat = k4.texture_flux_k4(p, q)["flux_over_flux0"]
        assert np.isclose(c, lat), (p, q, c, lat)


def test_k_hopf_pi_over_3_is_a4_c3_halfangle_not_a_fit():
    """The engine's fitted k_hopf=pi/3 is exactly the A4 C3 SU(2) double-cover
    half-angle (120deg -> pi/3), forced by the lattice C3 order z=3 -- a de-fit."""
    A = k4.k4_disclination_flux(L=8)
    assert np.isclose(A["su2_halfangle_per_encircle"], np.pi / 3.0, atol=1e-6)
    assert np.isclose(A["so3_angle_per_encircle"], 2.0 * np.pi / 3.0, atol=1e-6)
    assert A["c3_order_so3"] == 3
    assert A["uses_analytic_qbody"] is False
    assert A["encircle3"]["flux_over_flux0"] == 0.5   # 3 x pi/3 = pi = half flux
    assert A["encircle6"]["flux_over_flux0"] == 0.0   # full 2T period


def test_hopf_charge_is_loop_invariant_zero_accrued_phase():
    """Framing 3: the engine Hopf charge is a homotopy invariant, unchanged by the
    rigid 2pi frame rotation -> accrued phase theta*dQ_H = 0 for any theta (small
    grid; the spread is ~machine-precision, and negligible vs Q_H itself)."""
    hopf = _load("electron_halfflux_hopf_phase.py")
    N = 20
    for (p, q) in [(2, 3), (2, 2)]:
        omega, mask = hopf.seed_omega_pq(N, N, N, p, q, R_target=5.0, r_target=2.0)
        _, trace = hopf.loop_hopf_trace(omega, mask, dx=1.0, n_steps=9)
        spread = max(trace) - min(trace)
        assert spread < 1e-3, (p, q, spread)
        assert spread < 1e-2 * (abs(trace[0]) + 1e-9), (p, q, spread, trace[0])


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
