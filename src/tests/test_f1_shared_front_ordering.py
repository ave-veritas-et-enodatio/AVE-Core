"""F1 DEFECT regression — Cosserat shared front must reach bond Γ.

Grant 2026-07-15: DEFECT. CoupledK4Cosserat writes z_local = √(S_μ/S_ε)
(or legacy total-A² form) before k4.step(); without external_z_local,
_scatter_all overwrote that with V-only 1/√S(V) before _connect_all.
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.core.k4_tlm import K4Lattice3D
from ave.topological.k4_cosserat_coupling import CoupledK4Cosserat


def _beltrami_omega(N: int, amp: float = 0.35) -> np.ndarray:
    """RH Beltrami ω with nonzero curvature (loads A²_μ at V=0)."""
    k = 2.0 * np.pi / N
    z_idx = np.arange(N).reshape(1, 1, N)
    omega = np.zeros((N, N, N, 3), dtype=np.float64)
    omega[..., 0] = amp * np.cos(k * z_idx)
    omega[..., 1] = amp * np.sin(k * z_idx)
    return omega


class TestF1SharedFrontSurvives:
    def test_coupled_sets_external_z_local(self):
        sim = CoupledK4Cosserat(N=8, pml=0, disable_cosserat_lc_force=True)
        assert sim.k4.external_z_local is True
        assert sim.k4.op3_bond_reflection is True

    def test_shared_front_survives_k4_step_when_v_quiet(self):
        """Cosserat-loaded, V=0: z_local after k4.step equals the shared write."""
        N = 10
        sim = CoupledK4Cosserat(N=N, pml=0, disable_cosserat_lc_force=True)
        sim.cos.omega[:] = _beltrami_omega(N)
        assert np.allclose(sim.k4.V_inc, 0.0)

        sim._update_z_local_total()
        z_shared = sim.k4.z_local_field.copy()
        # Shared front must actually load (not flat unity) somewhere active.
        active = sim.k4.mask_active
        assert float(np.max(np.abs(z_shared[active] - 1.0))) > 1e-4

        sim.k4.step()  # would have overwritten under the DEFECT
        np.testing.assert_allclose(
            sim.k4.z_local_field,
            z_shared,
            rtol=0.0,
            atol=0.0,
            err_msg="F1: k4.step() must not overwrite CoupledK4Cosserat shared front",
        )

    def test_defect_control_overwrite_without_external_flag(self):
        """Document the pre-fix failure mode: external_z_local=False kills Cosserat front."""
        N = 10
        sim = CoupledK4Cosserat(N=N, pml=0, disable_cosserat_lc_force=True)
        sim.cos.omega[:] = _beltrami_omega(N)
        sim._update_z_local_total()
        z_shared = sim.k4.z_local_field.copy()
        active = sim.k4.mask_active
        assert float(np.max(np.abs(z_shared[active] - 1.0))) > 1e-4

        sim.k4.external_z_local = False  # restore DEFECT behavior
        sim.k4.step()
        # V=0 ⇒ V-only recompute forces z ≡ 1 on active sites
        assert np.allclose(sim.k4.z_local_field[active], 1.0, atol=1e-10)
        assert not np.allclose(sim.k4.z_local_field, z_shared)

    def test_standalone_k4_still_owns_v_only_z_local(self):
        """Standalone Op3 path unchanged: V-only z_local, external_z_local=False."""
        lat = K4Lattice3D(
            nx=6, ny=6, nz=6, dx=1.0, op3_bond_reflection=True, V_SNAP=1.0
        )
        assert lat.external_z_local is False
        lat.V_inc[2, 2, 2, 0] = 0.5
        lat._update_z_local_field()
        z_v = lat.z_local_field.copy()
        lat.step()
        np.testing.assert_allclose(lat.z_local_field, z_v, rtol=1e-12, atol=1e-12)

    def test_s_field_still_advances_under_external_z_local(self):
        """CI 2026-07-15: external_z_local must not freeze memristive S_field."""
        sim = CoupledK4Cosserat(
            N=8,
            pml=0,
            disable_cosserat_lc_force=True,
            use_memristive_saturation=True,
        )
        assert sim.k4.external_z_local is True
        drive = 0.5 * sim.V_SNAP
        for _ in range(20):
            sim.k4.V_inc[2, 2, 2, 0] = drive
            sim.step()
        S_driven = float(sim.k4.S_field[2, 2, 2])
        assert S_driven < 0.98, (
            f"S_field frozen under external_z_local — still {S_driven:.4f}"
        )
        # Shared front ownership preserved (Cosserat write path still used).
        assert sim.k4.external_z_local is True


def _u_strain(N: int, amp: float = 0.8) -> np.ndarray:
    """u-displacement that loads the ELECTRIC sector (A²_ε → symmetric strain),
    driving the shared front z = √(S_μ/S_ε) ABOVE unity (the '1.045-class' value
    at amp=0.8), the electric complement to the ω-Beltrami magnetic seed above."""
    k = 2.0 * np.pi / N
    x = np.arange(N).reshape(N, 1, 1)
    u = np.zeros((N, N, N, 3), dtype=np.float64)
    u[..., 0] = amp * np.sin(k * x)
    return u


class TestF1MaterialityKernel:
    """Strengthened F1 pins (F1 lane, 2026-07-16): the magnitude the fix
    preserves ('1.045-class'), the power-conservation invariant that bounds
    materiality to spatial routing, and the Cosserat-quiet identity."""

    def test_electric_loaded_1045_class_survives_k4_step(self):
        """V-quiet + u-strain: the electric shared front z≈1.045 must survive
        k4.step() exactly (the literal '1.045-class value survives' pin), and
        collapse to unity under the DEFECT."""
        N = 12
        sim = CoupledK4Cosserat(N=N, pml=0, disable_cosserat_lc_force=True)
        sim.cos.u[:] = _u_strain(N, 0.8)
        assert np.allclose(sim.k4.V_inc, 0.0)

        sim._update_z_local_total()
        active = sim.k4.mask_active
        z_peak = float(sim.k4.z_local_field[active].max())
        # Electric loading drives z ABOVE unity into the '1.045-class' band.
        assert 1.04 < z_peak < 1.05, f"expected 1.045-class peak, got {z_peak}"
        z_shared = sim.k4.z_local_field.copy()

        sim.k4.step()  # fixed engine: shared front must survive verbatim
        np.testing.assert_allclose(
            sim.k4.z_local_field, z_shared, rtol=0.0, atol=0.0,
            err_msg="F1: electric 1.045-class front must survive k4.step()",
        )

        # DEFECT control: external_z_local=False collapses V-quiet z to unity.
        sim.k4.external_z_local = False
        sim.k4.step()
        assert np.allclose(sim.k4.z_local_field[active], 1.0, atol=1e-10)

    def test_power_conservation_bounds_materiality_to_spatial(self):
        """Bond reflection is power-conserving (Γ²+T²=1), so the V-sector ENERGY
        is invariant between fixed and defect even when the shared front loads
        strongly — materiality is confined to spatial routing, not energy."""
        N, steps = 12, 20

        def run(external):
            sim = CoupledK4Cosserat(N=N, pml=0, disable_cosserat_lc_force=True)
            sim.k4.external_z_local = external
            # Strong Cosserat curvature loads the shared front well away from V-only.
            k = 2.0 * np.pi / N
            z = np.arange(N).reshape(1, 1, N)
            sim.cos.omega[..., 0] = 2.5 * np.cos(k * z)
            sim.cos.omega[..., 1] = 2.5 * np.sin(k * z)
            c = N // 2
            for dz in (-2, 0, 2):
                if sim.k4.mask_active[c, c, c + dz]:
                    sim.k4.V_inc[c, c, c + dz, :] = 0.4
            for _ in range(steps):
                sim.step()
            return float(np.sum(sim.k4.V_inc ** 2))

        e_fixed, e_defect = run(True), run(False)
        # E_V identical to machine precision despite the loaded, differing front.
        np.testing.assert_allclose(e_fixed, e_defect, rtol=1e-10, atol=1e-10)

    def test_cosserat_quiet_shared_front_equals_v_only(self):
        """§3a: with Cosserat quiet, the shared front √(S_μ/S_ε) is IDENTICAL to
        the legacy V-only (1−A²_V)^(−1/4), so the fix is provably immaterial —
        z_local matches between fixed and defect to ~machine precision."""
        N = 12
        c = N // 2

        def z_after_step(external):
            sim = CoupledK4Cosserat(N=N, pml=0, disable_cosserat_lc_force=True)
            sim.k4.external_z_local = external
            # V active, Cosserat cold (u=ω=0).
            for dz in (-2, 0, 2):
                if sim.k4.mask_active[c, c, c + dz]:
                    sim.k4.V_inc[c, c, c + dz, :] = 0.4
            sim.step()
            return sim.k4.z_local_field.copy()

        np.testing.assert_allclose(
            z_after_step(True), z_after_step(False), rtol=0.0, atol=1e-12,
            err_msg="Cosserat-quiet: shared front must equal the V-only kernel",
        )
