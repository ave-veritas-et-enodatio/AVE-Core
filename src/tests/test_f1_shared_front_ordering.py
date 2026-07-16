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
