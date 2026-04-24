"""
Engine saturation invariants — retroactive test for Flag-5e-A class of bugs.

**Why this file exists:**

Flag-5e-A (commit 098d430, 2026-04-24) revealed that
`K4Lattice3D._update_z_local_field` and `_scatter_all` used module-level
V_SNAP (≈511 kV SI) while engine natural-unit sources inject V in
engine-native V_SNAP (=1). Result: the K4 Ax4+Op14+Op3 saturation path
was DORMANT in any engine-context test that used source-driven
simulation.

The bug existed since K4 was written but was never caught because no
test asserted that the saturation mechanism ACTUALLY ACTIVATED under
engine-source drive. Tests that exercised saturation did it by directly
setting V_inc in module-V_SNAP units, inadvertently matching the
(broken) K4 strain normalization — self-consistent with the bug.

**The principle this file enforces:**

Any engine-context test that names a saturation, reflection, or
impedance mechanism in its docstring must assert that the mechanism's
state variable actually deviates from baseline during the test.

Tests that only assert "no NaN/inf" or "engine runs without error"
verify plumbing but not physics. Per AVE's axiom-first discipline:
"the test passed" ≠ "the mechanism was exercised."

**What this file tests:**

Under representative engine-source drives at stress amplitudes, verify
that each AVE saturation mechanism's state variable actually moves away
from its unsaturated baseline. If any of these tests fails, the
saturation path is dormant for that configuration — early indicator
of unit-system or plumbing regressions.

Reference:
  - fix commit 098d430 (Flag-5e-A)
  - research doc on test-design discipline (to be written)
"""
from __future__ import annotations

import numpy as np
import pytest

from ave.topological.vacuum_engine import (
    AutoresonantCWSource,
    CosseratBeltramiSource,
    VacuumEngine3D,
)


# ═══════════════════════════════════════════════════════════════════════════
# 1. K4 saturation mechanism — the Flag-5e-A canary
# ═══════════════════════════════════════════════════════════════════════════
class TestK4SaturationActivatesUnderEngineSource:
    """Under an engine-source drive at stress amplitude, K4's saturation
    state variables must depart from unsaturated baseline.

    Baseline: S_field = 1.0 everywhere, z_local_field = 1.0 everywhere,
    Γ-driven reflection negligible. Under stress drive, these MUST move.

    **Flag-5e-A canary:** if this test fails, the K4 strain calculation
    is not seeing the engine's V_SNAP — re-audit `_update_z_local_field`
    and `_scatter_all` in k4_tlm.py to verify they use `self.V_SNAP`
    (not the module-level V_SNAP constant).
    """

    def _run_stress_drive(self, use_memristive: bool) -> dict:
        """Run a small engine with stress autoresonant drive."""
        engine = VacuumEngine3D.from_args(
            N=16, pml=3, temperature=0.0,
            use_memristive_saturation=use_memristive,
        )
        omega_drive = 2 * np.pi / 3.5
        period = 2 * np.pi / omega_drive
        engine.add_source(AutoresonantCWSource(
            x0=5, direction=(1.0, 0.0, 0.0),
            amplitude=0.8,  # stress amp, above P_phase5 registered 0.5
            omega=omega_drive,
            sigma_yz=3.0,
            t_ramp=2 * period,
            t_sustain=10 * period,
        ))
        engine.run(n_steps=60)
        mask = engine.k4.mask_active
        return {
            "S_min": float(engine.k4.S_field[mask].min()),
            "z_max": float(engine.k4.z_local_field[mask].max()),
            "A2_total_max": float(
                max(np.sum(engine.k4.V_inc[mask] ** 2, axis=-1))
                if mask.any() else 0.0
            ) / (engine.V_SNAP ** 2),
        }

    def test_s_field_drops_below_one_under_memristive(self):
        """Under memristive K4 + stress source drive, S_field must drop
        below ~0.95 at least at the most-driven site. If S stays at
        1.000, K4 saturation is dormant (Flag-5e-A regression).

        Pre-Flag-5e-A-fix: this test FAILED (S stayed at 1.000).
        Post-fix: S drops to ~0.5 at peak, passes."""
        stats = self._run_stress_drive(use_memristive=True)
        assert stats["S_min"] < 0.95, (
            f"K4 S_field never saturated under engine source drive — "
            f"min S = {stats['S_min']:.4f}. Possible Flag-5e-A regression: "
            f"K4 `_update_z_local_field` may be using module-level V_SNAP "
            f"instead of `self.V_SNAP`. Re-verify k4_tlm.py:~244."
        )

    def test_z_local_field_rises_above_unity_under_memristive(self):
        """Op14 gives Z_eff = Z_0/√S, so saturation must raise z_local_field
        above baseline 1.0 at the most-driven site.

        This is the pre-memristive legacy invariant — catches the
        Flag-5e-A bug even for instantaneous Op14 codepaths."""
        stats = self._run_stress_drive(use_memristive=True)
        assert stats["z_max"] > 1.05, (
            f"K4 z_local_field never rose above baseline under engine "
            f"drive — max z = {stats['z_max']:.4f}. Op14 impedance path "
            f"is dormant — Flag-5e-A regression suspected."
        )

    def test_regime_classifier_A2_total_reaches_stress_threshold(self):
        """Sanity: the RegimeClassifierObserver (which computes A² from
        V²/V_SNAP_engine²) should see A² well above linear regime under
        stress drive. This check works even when K4's own saturation is
        broken — if it fails, the source wiring itself is broken."""
        stats = self._run_stress_drive(use_memristive=True)
        # Threshold 0.2 = exits Regime I (< √(2α) ≈ 0.121), enters Regime II.
        # The endpoint A² is lower than the peak during the run — this
        # threshold catches a broken-source condition (V_inc would be ~0)
        # without requiring the test to re-compute peak-over-time.
        assert stats["A2_total_max"] > 0.2, (
            f"A²_total at most-driven site only reached "
            f"{stats['A2_total_max']:.4f} (endpoint snapshot) — source may "
            f"not be injecting correctly. Check AutoresonantCWSource.apply() "
            f"and engine amplitude convention."
        )


# ═══════════════════════════════════════════════════════════════════════════
# 2. Cosserat saturation — forward-looking invariant
# ═══════════════════════════════════════════════════════════════════════════
class TestCosseratSaturationActivatesUnderDirectInjection:
    """Under direct-ω injection (CosseratBeltramiSource) at stress
    amplitude, Cosserat A²_μ curvature field must exceed linear regime.

    This is the Cosserat analog of the K4 invariant — protects against
    a future "Flag-5e-B" where Cosserat sector's saturation path could
    become dormant due to unit mismatch or similar plumbing regression.

    **Note:** This test does NOT require A²_μ ≥ 0.95 (the gate C1
    threshold) — that requires either very large amplitudes or gate-
    window-tuned drive per step 5b findings. We only require exiting
    the linear regime.
    """

    def test_cosserat_A2_mu_rises_under_direct_omega_injection(self):
        from ave.topological.vacuum_engine import PairNucleationGate

        engine = VacuumEngine3D.from_args(
            N=16, pml=3, temperature=0.0,
            use_memristive_saturation=True,
        )
        omega_drive = 2 * np.pi / 3.5
        period = 2 * np.pi / omega_drive
        engine.add_source(CosseratBeltramiSource(
            x0=8, propagation_axis=0, amplitude=2.0,
            omega=omega_drive, handedness="RH", sigma_yz=3.0,
            t_ramp=2 * period, t_sustain=10 * period,
        ))
        gate = PairNucleationGate(cadence=2)
        engine.add_observer(gate)
        engine.run(n_steps=60)

        # Compute peak A²_μ via gate's own machinery
        A2_mu_field = gate._compute_A2_mu(engine)
        active = engine.cos.mask_alive
        A2_peak = float(A2_mu_field[active].max()) if active.any() else 0.0

        # Linear-regime threshold: A²_μ should exceed thermal baseline + a
        # small margin that confirms the direct-ω drive is being absorbed.
        # Thermal baseline at T=0 is ~0; with amp=2.0 direct injection
        # we expect at least A²_μ > 0.01 (exits deep-linear regime).
        assert A2_peak > 0.01, (
            f"Cosserat A²_μ stayed in deep linear regime under direct-ω "
            f"injection at amp=2.0 — peak = {A2_peak:.5f}. "
            f"CosseratBeltramiSource or Cosserat integrator may have a "
            f"plumbing regression analogous to Flag-5e-A."
        )


# ═══════════════════════════════════════════════════════════════════════════
# 3. Cool-through-yield signature — the Flag-5e-A victory lap
# ═══════════════════════════════════════════════════════════════════════════
class TestCoolThroughYieldUnderMemristive:
    """Under memristive K4 + a ramp-sustain-cutoff source envelope,
    S_field must show the cool-through-yield signature: drops during
    drive, rises after drive shutoff.

    This is the macro-invariant that captures doc 59_'s yield-heal
    mechanism operating correctly end-to-end.
    """

    def test_s_field_drops_during_drive_then_rises_after(self):
        engine = VacuumEngine3D.from_args(
            N=16, pml=3, temperature=0.0,
            use_memristive_saturation=True,
        )
        omega_drive = 2 * np.pi / 3.5
        period = 2 * np.pi / omega_drive
        t_ramp = 2 * period
        t_sustain = 8 * period
        # Source with abrupt cutoff to trigger cooling phase
        engine.add_source(AutoresonantCWSource(
            x0=5, direction=(1.0, 0.0, 0.0),
            amplitude=0.8, omega=omega_drive,
            sigma_yz=3.0,
            t_ramp=t_ramp, t_sustain=t_sustain,
            t_decay=period * 0.5,
        ))
        drive_end = t_ramp + t_sustain

        # Sample S_field at mid-drive and late-cooling
        S_during_drive: list[float] = []
        S_post_drive: list[float] = []

        for step in range(80):
            engine.step()
            if engine.step_count % 4 != 0:
                continue
            mask = engine.k4.mask_active
            S_now = float(engine.k4.S_field[mask].min())
            if engine.time < drive_end:
                if engine.time > t_ramp:  # skip ramp; only sustain phase
                    S_during_drive.append(S_now)
            else:
                # Give cooling at least 2 periods to progress
                if engine.time > drive_end + 2 * period:
                    S_post_drive.append(S_now)

        if not S_during_drive or not S_post_drive:
            pytest.skip("Insufficient samples in drive or cooling window")

        S_drive_median = float(np.median(S_during_drive))
        S_post_median = float(np.median(S_post_drive))

        # During drive: should show saturation (S < 0.9)
        assert S_drive_median < 0.9, (
            f"S_field never saturated under drive — median S = "
            f"{S_drive_median:.4f} during sustain phase."
        )
        # After drive: should recover toward 1 (cool-through-yield)
        assert S_post_median > S_drive_median + 0.1, (
            f"No cool-through-yield signature. S_drive={S_drive_median:.4f}, "
            f"S_post={S_post_median:.4f}, Δ={S_post_median-S_drive_median:+.4f}. "
            f"Expected ≥ +0.1 recovery post-drive cutoff."
        )
