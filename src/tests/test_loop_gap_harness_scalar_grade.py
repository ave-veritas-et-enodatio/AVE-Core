"""Phase C′ Increment A — standing longitudinal V seed on K4 V_inc.
Increment B — Option-D V→ω boundary source tests.
"""

import numpy as np
import pytest

from ave.core.loop_gap_harness import run_loop_gap_probe
from ave.core.loop_gap_seeds import A_YIELD
from ave.core.scalar_grade_source import boundary_v_to_omega_accel, relative_h_drift
from ave.core.scalar_grade_seed import (
    A2_V_FLOOR_FRAC,
    a2_v_field,
    apply_scalar_seed_if_enabled,
    scalar_seed_certificate,
    seed_lane1_standing_v,
)
from ave.topological.vacuum_engine import EngineConfig, VacuumEngine3D


def _make_engine(N: int = 27, *, v_to_omega: bool = False) -> VacuumEngine3D:
    cfg = EngineConfig(
        N=N,
        pml=3,
        temperature=0.0,
        use_asymmetric_saturation=True,
        disable_cosserat_lc_force=True,
        couple_v_sector=True,
        use_trilinear_converter=True,
        use_impedance_boundary=True,
        v_to_omega_source_on=v_to_omega,
    )
    return VacuumEngine3D(cfg)


def _clear_cosserat(engine: VacuumEngine3D) -> None:
    cos = engine._coupled.cos
    cos.u[:] = 0.0
    cos.omega[:] = 0.0
    cos.u_dot[:] = 0.0
    cos.omega_dot[:] = 0.0


def _a2_v_peak(engine: VacuumEngine3D) -> float:
    coupled = engine._coupled
    a2 = a2_v_field(coupled.k4)
    m = np.asarray(coupled._interior_mask(), dtype=bool) & np.asarray(
        coupled.k4.mask_active, dtype=bool
    )
    return float(np.max(a2[m])) if m.any() else 0.0


def test_scalar_seed_certificate_topology_null():
    """CP8: standing V populated, topology-NULL, A²_peak ≈ frac²."""
    N = 27
    frac = 0.85
    eng = _make_engine(N)
    _clear_cosserat(eng)
    seed_lane1_standing_v(eng, frac=frac, clear_k4=True)
    cert = scalar_seed_certificate(eng, frac=frac)
    assert cert["topology_null"] is True, cert
    assert cert["omega_max"] == 0.0
    assert cert["H_bel_abs"] < 1e-12
    assert abs(cert["A2_peak"] - cert["frac2_k4"]) < 0.05 * cert["frac2_k4"], cert
    assert 0.0 < cert["A2_seed"] < cert["A2_peak"], cert
    assert cert["passes"] is True


def test_scalar_seed_a2_above_yield_floor():
    frac = 0.85
    eng = _make_engine(27)
    _clear_cosserat(eng)
    seed_lane1_standing_v(eng, frac=frac, clear_k4=True)
    cert = scalar_seed_certificate(eng, frac=frac)
    floor = A2_V_FLOOR_FRAC * float(A_YIELD**2)
    assert cert["A2_peak"] > floor
    assert cert["A2_peak"] > 0.25 * float(A_YIELD**2)


def test_scalar_off_is_noop():
    eng = _make_engine(14)
    _clear_cosserat(eng)
    assert apply_scalar_seed_if_enabled(eng, scalar_seed_on=False) is False
    assert _a2_v_peak(eng) == 0.0


def test_s1_vs_s0_a2_differs():
    """F1: scalar_ON populates A²_V; scalar_OFF stays flat at 0 (S1 vs S0)."""
    kw = dict(
        N=10,
        rank_target=1,
        seed_mode="pair",
        amp=0.0,
        bulk_density_on=False,
        n_drive_mult=0.25,
        n_quiet_mult=0.5,
        fast=True,
    )
    s0 = run_loop_gap_probe("S0_scalar_off", scalar_seed_on=False, **kw)
    s1 = run_loop_gap_probe("S1_scalar_on", scalar_seed_on=True, scalar_seed_frac=0.85, **kw)
    assert s1.v_inc_peak > s0.v_inc_peak
    assert s0.v_inc_peak == pytest.approx(0.0, abs=1e-12)


def test_scalar_off_regression_unchanged():
    """KEEP-BOTH: default scalar_seed_on=False matches explicit False."""
    kw = dict(
        N=10,
        rank_target=1,
        seed_mode="photon_lock",
        bulk_density_on=True,
        front_target=A_YIELD,
        n_drive_mult=0.5,
        n_quiet_mult=1.5,
        fast=True,
    )
    r_default = run_loop_gap_probe("default", **kw)
    r_explicit = run_loop_gap_probe("explicit_off", scalar_seed_on=False, **kw)
    assert r_default.v_inc_peak == pytest.approx(r_explicit.v_inc_peak, rel=0.0, abs=0.0)
    assert r_default.op2_bin == r_explicit.op2_bin
    assert r_default.gamma_bulk_min_drive == pytest.approx(
        r_explicit.gamma_bulk_min_drive, rel=0.0, abs=0.0
    )


def test_standing_v_finite_after_steps():
    eng = _make_engine(24)
    _clear_cosserat(eng)
    seed_lane1_standing_v(eng, frac=0.6, clear_k4=True)
    assert _a2_v_peak(eng) > 0.0
    for _ in range(20):
        eng.step()
    assert np.all(np.isfinite(eng._coupled.k4.V_inc))


def test_boundary_source_zero_when_off():
    eng = _make_engine(14, v_to_omega=False)
    seed_lane1_standing_v(eng, frac=0.85, clear_k4=True)
    f = boundary_v_to_omega_accel(eng._coupled)
    assert float(np.max(np.abs(f))) == 0.0


def test_boundary_source_nonzero_with_scalar_v():
    eng = _make_engine(14, v_to_omega=True)
    _clear_cosserat(eng)
    seed_lane1_standing_v(eng, frac=0.85, clear_k4=True)
    f = boundary_v_to_omega_accel(eng._coupled)
    assert float(np.max(np.abs(f))) > 0.0


def test_s3_vs_s2_omega_source_fires():
    """F2: S3 (scalar + source) builds more |ω| than S2 after IC (source OFF)."""
    kw = dict(
        N=10,
        rank_target=1,
        seed_mode="photon_lock",
        bulk_density_on=True,
        front_target=A_YIELD,
        scalar_seed_on=True,
        scalar_seed_frac=0.85,
        n_drive_mult=0.75,
        n_quiet_mult=1.0,
        fast=True,
    )
    s2 = run_loop_gap_probe("S2_source_off", v_to_omega_source_on=False, **kw)
    s3 = run_loop_gap_probe("S3_source_on", v_to_omega_source_on=True, **kw)
    assert s3.max_omega_end >= s2.max_omega_end


def test_scalar_only_source_builds_omega():
    """F2: trapped-V source nucleates ω from cold Cosserat (S1 analogue)."""
    kw = dict(
        N=10,
        rank_target=1,
        seed_mode="pair",
        amp=0.0,
        bulk_density_on=False,
        scalar_seed_on=True,
        scalar_seed_frac=0.85,
        n_drive_mult=0.75,
        n_quiet_mult=1.0,
        fast=True,
    )
    off = run_loop_gap_probe("S1_off", v_to_omega_source_on=False, **kw)
    on = run_loop_gap_probe("S1_on", v_to_omega_source_on=True, **kw)
    assert off.max_omega_end == pytest.approx(0.0, abs=1e-9)
    assert on.max_omega_end > 1e-4


def test_v_to_omega_h_drift_bounded():
    """F2: S3 stack — H does not secular-pump (no runaway growth)."""
    from ave.core.loop_gap_seeds import apply_seed, A_YIELD
    from ave.core.scalar_grade_seed import apply_scalar_seed_if_enabled

    cfg = EngineConfig(
        N=10,
        pml=3,
        bulk_density_on=True,
        use_impedance_boundary=True,
        v_to_omega_source_on=True,
        use_trilinear_converter=True,
        disable_cosserat_lc_force=True,
    )
    eng = VacuumEngine3D(cfg)
    apply_seed(eng, "photon_lock", front_target=A_YIELD)
    apply_scalar_seed_if_enabled(eng, scalar_seed_on=True, scalar_seed_frac=0.85)
    eng.freeze_converter_wall()
    coupled = eng._coupled
    h0 = float(coupled.impedance_hamiltonian()["H"])
    om0 = float(np.max(np.linalg.norm(coupled.cos.omega, axis=-1)))
    for _ in range(20):
        eng.step()
    h1 = float(coupled.impedance_hamiltonian()["H"])
    om1 = float(np.max(np.linalg.norm(coupled.cos.omega, axis=-1)))
    # Bounded: no secular pump (ω must not run away orders of magnitude).
    assert om1 < 50.0 * max(om0, 1e-6)
    assert relative_h_drift(coupled, h0, h1) < 2.0


def test_bulk_force_detonation_control():
    """F2 control: A28 bulk force arm must not pass as bounded source."""
    kw = dict(
        N=10,
        rank_target=1,
        seed_mode="photon_lock",
        scalar_seed_on=True,
        bulk_density_on=False,
        n_drive_mult=0.5,
        n_quiet_mult=0.5,
        fast=True,
    )
    bounded = run_loop_gap_probe(
        "bounded_source",
        v_to_omega_source_on=True,
        bulk_force_v_to_omega=False,
        **kw,
    )
    bulk = run_loop_gap_probe(
        "bulk_force",
        v_to_omega_source_on=False,
        bulk_force_v_to_omega=True,
        **kw,
    )
    assert bulk.omega_peak > 5.0 * max(bounded.omega_peak, 1e-6)
