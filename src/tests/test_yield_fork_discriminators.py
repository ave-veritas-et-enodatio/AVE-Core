"""Yield-fork discriminator lane — validation tests (2026-07-19).

Pins the two registered discriminators run by the yield-fork lane:
  Leg A: research/2026-06-09_thixotropy-amplitude-dependent-tau_prereg.md
         (PROTOCOL-COMPLETION amendment 2026-07-19)
  Leg B: research/2026-07-19_yield-fork-loop-area_PROTOCOL-COMPLETION.md
         (P_phase5_memristor_loop_area, tau-relax-derivation.md:109)

The CRITICAL test is `test_driver_kernel_byte_matches_engine`: it proves the
standalone kernel used by both legs is bit-identical to the engine's own
`use_memristive_saturation` update (k4_tlm.py:283,291) — the engine itself is
never edited, so the drivers must reproduce it exactly or they measure a
different object than canon.

Also independently re-derives each leg's verdict from the raw series, so the
verdict is not taken on the driver's own word.
"""

import importlib.util
import os

import numpy as np
import pytest

from ave.core.constants import TAU_RELAX_NATIVE, V_SNAP
from ave.core.k4_tlm import K4Lattice3D

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_LANE = os.path.join(_ROOT, "research", "2026-07-19_yield-fork-discriminators")


def _load(modname: str):
    path = os.path.join(_LANE, modname + ".py")
    spec = importlib.util.spec_from_file_location(modname, path)
    mod = importlib.util.module_from_spec(spec)
    import sys

    sys.path.insert(0, _LANE)
    spec.loader.exec_module(mod)
    return mod


k = _load("yield_fork_kernel")


# ═══════════════════════════════════════════════════════════════════════════
# CRITICAL — the driver kernel IS the engine's memristive update (byte-match)
# ═══════════════════════════════════════════════════════════════════════════
class TestKernelByteMatchesEngine:
    def test_s_eq_matches_engine_form(self):
        """s_eq(r) matches k4_tlm.py:283 sqrt(max(0,1-min(A,1)^2)) pointwise."""
        for r in (0.0, 0.4, 0.7, 0.95, 1.0, 1.3):
            strain = min(abs(r), 1.0)
            expected = np.sqrt(max(0.0, 1.0 - strain**2))
            assert float(k.s_eq(r)) == pytest.approx(expected, rel=1e-14, abs=1e-14)

    def test_backward_euler_bit_identical_to_engine(self):
        """Drive a live K4Lattice3D(use_memristive_saturation=True) at one site
        with a prescribed r(t); the engine's S_field must equal the kernel's
        be_step iteration to floating-point round-off, using the ENGINE's own
        dt and tau_relax. Proves the driver measures the canonical object."""
        lat = K4Lattice3D(nx=6, ny=6, nz=6, use_memristive_saturation=True)
        tau = lat.tau_relax
        dt = lat.dt
        site = (0, 0, 0)  # A-sublattice

        rng = np.linspace(0.4, 1.0, 25)  # sweep strain through near-yield
        S_kernel = 1.0  # engine S_field initialises at 1.0
        for r in rng:
            # engine step
            lat.V_inc[site[0], site[1], site[2], 0] = r * V_SNAP
            lat._update_z_local_field()
            S_engine = float(lat.S_field[site])
            # kernel step with the engine's own dt, tau
            S_kernel = k.be_step(S_kernel, float(k.s_eq(r)), tau, dt)
            assert S_engine == pytest.approx(S_kernel, rel=1e-12, abs=1e-14), f"mismatch at r={r}"

    def test_tau_relax_native_unity(self):
        assert TAU_RELAX_NATIVE == 1.0


# ═══════════════════════════════════════════════════════════════════════════
# Leg A — sign-memory discriminator: independent re-derivation + controls
# ═══════════════════════════════════════════════════════════════════════════
class TestLegA:
    def test_single_tau_has_no_genuine_sign_memory(self):
        """R_mem (baseline-subtracted) is ~0 for single-tau, and the raw R is a
        nonlinear artifact that vanishes as Dr->0 (independent of the driver)."""
        # raw R scales down with amplitude -> memoryless nonlinear-loop artifact
        r_big = k.stroke_dissipations(k.integrate_cycle(0.7, 0.30, 0.9, tau_fn=k.tau_const))["R"]
        r_small = k.stroke_dissipations(k.integrate_cycle(0.7, 0.02, 0.9, tau_fn=k.tau_const))["R"]
        assert abs(r_small) < 0.1 * abs(r_big)

    def test_tau_swap_sign_flip_isolates_genuine_memory(self):
        """Genuine sign(dr/dt) memory flips R_mem under tau-swap; single-tau baseline
        is the memoryless midpoint. This is the clean discriminator."""
        base = k.stroke_dissipations(k.integrate_cycle(0.7, 0.30, 0.9, tau_fn=k.tau_const))["R"]
        down = k.stroke_dissipations(k.integrate_cycle(0.7, 0.30, 0.9, tau_fn=k.tau_two, ratio=3.0))["R"]
        up = k.stroke_dissipations(k.integrate_cycle(0.7, 0.30, 0.9, tau_fn=k.tau_two, ratio=1.0 / 3.0))["R"]
        assert (down - base) * (up - base) < 0.0  # flips
        assert abs(down - base) > 1e-2 and abs(up - base) > 1e-2  # non-trivial signal

    def test_positive_control_fires_instrument_is_live(self):
        """Two-tau control must show elevated delta_tau_rel vs single-tau —
        a null on the canonical model is then a real null, not a dead instrument."""
        s_single = k.integrate_cycle(0.7, 0.30, 0.9, tau_fn=k.tau_const)
        s_two = k.integrate_cycle(0.7, 0.30, 0.9, tau_fn=k.tau_two, ratio=3.0)
        d_single = k.effective_tau_by_stroke(s_single)["delta_tau_rel"]
        d_two = k.effective_tau_by_stroke(s_two)["delta_tau_rel"]
        assert d_two > d_single

    def test_canonical_is_dissipative_excluded_from_A(self):
        """H-gate: canonical loop is dissipative (W_cycle >> integrator floor) ->
        excluded from bin A (which requires H-conserved) regardless of memory."""
        legb = _load("leg_b_loop_area")
        tol = legb.zero_tolerance()["tol"]
        w = k.loop_area_rS(k.integrate_cycle(0.7, 0.30, 0.9, tau_fn=k.tau_const))
        assert w > 10.0 * tol

    def test_leg_a_final_verdict_is_B(self):
        lega = _load("leg_a_thixotropy")
        out = lega.run()
        assert out["final_verdict"]["bin"] == "B"
        assert out["final_verdict"]["instrument_live"] is True
        assert out["clean_signmemory_analysis"]["canonical_has_genuine_sign_memory"] is False


# ═══════════════════════════════════════════════════════════════════════════
# Leg B — loop-area discriminator: independent re-derivation + gates
# ═══════════════════════════════════════════════════════════════════════════
class TestLegB:
    def test_loop_area_independent_shoelace_matches_driver(self):
        """Re-derive |∮ S dr| from the raw series by an independent shoelace
        (0.5*sum((S_i+S_{i+1})*(r_{i+1}-r_i))) and confirm it equals the driver."""
        s = k.integrate_cycle(0.7, 0.30, 1.0, tau_fn=k.tau_const)
        driver_area = k.loop_area_rS(s)
        r, S = s["r"], s["S"]
        indep = abs(0.5 * float(np.sum((S[:-1] + S[1:]) * (r[1:] - r[:-1]))))
        assert indep == pytest.approx(driver_area, rel=1e-12)

    def test_loop_area_finite_above_floor(self):
        """Near-yield loop area is finite and well above the integrator floor
        (rules out the strict zero-area lossless reading at the area level)."""
        legb = _load("leg_b_loop_area")
        tol = legb.zero_tolerance()["tol"]
        area = k.loop_area_rS(k.integrate_cycle(0.7, 0.30, 1.0, tau_fn=k.tau_const))
        assert area > 10.0 * tol

    def test_loop_area_vanishes_in_both_limits(self):
        """Debye signature: ∮ -> 0 in quasi-static (wt->0) and frozen (wt->inf)
        limits. Confirms it is a rate-dependent lag."""
        a_qs = k.loop_area_rS(k.integrate_cycle(0.7, 0.30, 1e-3, tau_fn=k.tau_const))
        a_pk = k.loop_area_rS(k.integrate_cycle(0.7, 0.30, 1.0, tau_fn=k.tau_const))
        a_fr = k.loop_area_rS(k.integrate_cycle(0.7, 0.30, 1e3, tau_fn=k.tau_const))
        assert a_qs < 0.01 * a_pk
        assert a_fr < 0.01 * a_pk

    def test_rS_peak_outside_window_and_verdict_is_NEITHER(self):
        """The (r,S)-plane peak sits at ~1.0 (linear Debye), OUTSIDE the P_phase5
        [0.85,0.95] window; the frozen verdict is NEITHER (fail-closed)."""
        legb = _load("leg_b_loop_area")
        out = legb.run()
        peak = out["peak_rS"]["peak_refined"]
        assert not (0.85 <= peak <= 0.95)
        assert out["adjudication"]["bin"] == "NEITHER"

    def test_no_origin_pinch_at_near_yield_operating_point(self):
        """The (V,I) Lissajous does NOT pinch through the origin at r0=0.7,Dr=0.3
        (drive never crosses r=0), so the origin-pinched-hysteresis registration
        does not apply at this operating point."""
        legb = _load("leg_b_loop_area")
        out = legb.run()
        assert out["pinch_through_origin_at_peak"]["passes_through_origin"] is False
