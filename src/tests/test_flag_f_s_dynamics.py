"""Tests for the Flag-F three-form contrast battery (Stage 2 gates G2 + G3 + shape class).

Prereg (frozen-by-push): research/2026-07-19_flag-f-s-dynamics_prereg.md
Derivation:             research/2026-07-19_flag-f-s-dynamics-derivation.md
Drivers:                research/2026-07-19_flag-f-s-dynamics/{reactive_kernel,contrast_battery}.py

Location note (disclosed deviation, prereg §8): the prereg placed this test in the
research lane dir; pytest testpaths=["src/tests"] only, so it lives here to be
discovered by `make test` / `make test-engine` (same convention as the #735
test_yield_fork_discriminators.py). Verdict-invariant — the prereg's intent (a
byte-match + reactive-audit test exists and passes) is satisfied.
"""

from __future__ import annotations

import importlib.util
import os
import sys

import numpy as np
import pytest

from ave.core.constants import TAU_RELAX_NATIVE, V_SNAP
from ave.core.k4_tlm import K4Lattice3D

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_LANE = os.path.join(_ROOT, "research", "2026-07-19_flag-f-s-dynamics")


def _load(modname: str):
    path = os.path.join(_LANE, modname + ".py")
    spec = importlib.util.spec_from_file_location(modname, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[modname] = mod
    spec.loader.exec_module(mod)
    return mod


k = _load("yield_fork_kernel")
rk = _load("reactive_kernel")


class TestG2ByteMatch:
    """Form S (shipped Eq 2.1) is bit-identical to the LIVE engine's memristive update."""

    @pytest.mark.engine_sim
    def test_form_S_byte_matches_live_engine(self):
        lat = K4Lattice3D(nx=6, ny=6, nz=6, use_memristive_saturation=True)
        tau = lat.tau_relax
        dt = lat.dt
        site = (0, 0, 0)
        S_kernel = 1.0  # engine S_field initialises at 1.0
        for r in np.linspace(0.4, 1.0, 25):
            lat.V_inc[site[0], site[1], site[2], 0] = r * V_SNAP
            lat._update_z_local_field()
            S_engine = float(lat.S_field[site])
            S_kernel = k.be_step(S_kernel, float(k.s_eq(r)), tau, dt)
            assert S_engine == pytest.approx(S_kernel, rel=1e-12, abs=1e-14), f"mismatch at r={r}"

    def test_tau_relax_native_unity(self):
        assert TAU_RELAX_NATIVE == 1.0


class TestG3ReactiveAudit:
    """The reactive FFT steady-state is the EXACT linear solution; ζ=0 is lossless."""

    def test_ode_residual_machine_zero(self):
        s = rk.integrate_reactive(0.7, 0.3, omega_tau=1.0, omega_S_tau=1.0, zeta=0.1)
        assert rk.ode_residual(s, 1.0, 0.1) < 1e-10

    def test_zeta0_offharmonic_loop_is_zero(self):
        # undamped (lossless) reactive, ω_S off the harmonic grid → ∮ ≈ 0 (world-a nets zero)
        s0 = rk.integrate_reactive(0.7, 0.3, omega_tau=0.37, omega_S_tau=0.93, zeta=0.0)
        assert rk.loop_area_rS(s0) < 1e-10
        assert rk.loop_area_VI(s0)["area_VI"] < 1e-10
        assert abs(s0["H_fundamental"].imag) < 1e-14  # real transfer → no dissipative quadrature


class TestAxisIIIShapeClass:
    """The structural discriminator: Debye (Form S) vs Resonant (Forms R/T)."""

    def test_form_S_is_debye_peak_pinned_near_one(self):
        # (r,S) loop-area peak of a first-order kernel is pinned at ωτ≈1 (F-B1 theorem)
        wts = np.logspace(np.log10(0.3), np.log10(3.0), 30)
        a = [k.loop_area_rS(k.integrate_cycle(0.7, 0.3, float(w), tau_relax=1.0, tau_fn=k.tau_const)) for w in wts]
        assert abs(float(wts[int(np.argmax(a))]) - 1.0) < 0.15

    def test_form_S_debye_phase_caps_at_90(self):
        # first-order lag phase (S vs S_eq) cannot exceed ~90°
        s = k.integrate_cycle(0.7, 0.3, 8.0, tau_relax=1.0, tau_fn=k.tau_const)
        F_S = np.fft.rfft(np.asarray(s["S"])[:-1])
        F_e = np.fft.rfft(np.asarray(s["Seq"])[:-1])
        assert abs(np.degrees(np.angle(F_S[1] / F_e[1]))) < 105.0

    @pytest.mark.parametrize("omega_S", [0.5, 1.0, 2.0])
    def test_reactive_peak_tracks_omega_S(self, omega_S):
        # Resonant class: (V,I) loop-area peak follows ω_S (NOT pinned at 1)
        wts = np.logspace(np.log10(0.1), np.log10(6.0), 50)
        a = [rk.loop_area_VI(rk.integrate_reactive(0.7, 0.3, float(w), omega_S, 0.1))["area_VI"] for w in wts]
        peak = float(wts[int(np.argmax(a))])
        assert peak == pytest.approx(omega_S, rel=0.15)

    def test_reactive_phase_sweeps_to_180(self):
        # 2nd-order reactive sweeps the FULL 180° through resonance (Debye caps at 90°)
        s = rk.integrate_reactive(0.7, 0.3, omega_tau=6.0, omega_S_tau=1.0, zeta=0.1)
        assert abs(rk.fundamental_phase_deg(s)) > 150.0

    def test_zeta0_reactive_lossless_finite_zeta_dissipative(self):
        # ordering: ∮(ζ=0) ≈ 0 < ∮(ζ=0.1) (transduced work grows with the coupling)
        s0 = rk.integrate_reactive(0.7, 0.3, 0.9, 0.93, 0.0)
        s1 = rk.integrate_reactive(0.7, 0.3, 0.9, 0.93, 0.1)
        assert rk.loop_area_VI(s0)["area_VI"] < rk.loop_area_VI(s1)["area_VI"]
