"""F1 (C′) — K4 V_inc scalar-grade seed plumbing + CP8 topology-null certificate.

Self-contained: depends only on the de-coupled ``scalar_grade_seed`` module and a
minimal ``VacuumEngine3D`` (no loop-gap harness battery, no V→ω source).

SCOPE: this validates the seed PLUMBING on the K4 V_inc (transverse-readout)
channel and the CP8 topology-null certificate. The harness scalar is a
``v_scalar_from_v_inc`` projection of the K4 port voltages
(``cross_sector_coupling.py:226``), NOT an independent A1 stiffening field — so this
is NOT a test of the A1 stiffening cage (that channel lives on
``master_equation_fdtd.py`` / ``crystal_engine.py``).
"""

import numpy as np

from ave.core.loop_gap_seeds import A_YIELD
from ave.core.scalar_grade_seed import (
    A2_V_FLOOR_FRAC,
    apply_scalar_seed_if_enabled,
    scalar_seed_certificate,
    seed_lane1_standing_v,
)
from ave.topological.vacuum_engine import EngineConfig, VacuumEngine3D


def _make_engine(N: int) -> VacuumEngine3D:
    """Minimal VacuumEngine3D using only EngineConfig fields present on main.

    Mirrors the loop-gap harness engine config minus the Increment-B
    ``v_to_omega_source_on`` flag (not on main, and irrelevant to the F1 seed
    + CP8 certificate, which never invoke the V→ω source).
    """
    cfg = EngineConfig(
        N=N,
        pml=3,
        temperature=0.0,
        use_asymmetric_saturation=True,
        disable_cosserat_lc_force=True,
        couple_v_sector=True,
        use_trilinear_converter=True,
        use_impedance_boundary=True,
    )
    return VacuumEngine3D(cfg)


def _clear_cosserat(eng: VacuumEngine3D) -> None:
    """Zero the Cosserat field — explicit CP8 null baseline before seeding."""
    cos = eng._coupled.cos
    cos.u[:] = 0.0
    cos.omega[:] = 0.0
    cos.u_dot[:] = 0.0
    cos.omega_dot[:] = 0.0


def test_f1_scalar_seed_lands_with_cp8_topology_null():
    """F1: the standing-V seed lands on K4 V_inc above the yield floor, and the
    CP8 certificate fires topology-null (the seed plants no (2,3) winding).

    Plumbing + certificate only — NOT an A1 stiffening field, NOT the cage.
    """
    eng = _make_engine(N=27)
    _clear_cosserat(eng)  # CP8 baseline: ω ≡ 0 before the seed touches V_inc
    seed_lane1_standing_v(eng, frac=0.85)
    cert = scalar_seed_certificate(eng)

    # CP8 — no planted (2,3): the seed writes only K4 V_inc, plants no winding.
    assert cert["topology_null"] is True, cert
    assert cert["omega_max"] < 1e-12, cert
    assert cert["H_bel_abs"] < 1e-12, cert

    # F1 — standing-V lands above the yield floor on the V_inc readout channel.
    floor = A2_V_FLOOR_FRAC * float(A_YIELD**2)
    assert cert["A2_peak"] > floor, cert

    # Module's own F1 gate (subsumes A²_peak ≈ frac²_k4 and the velocity nulls).
    assert cert["passes"] is True, cert


def test_keep_both_scalar_off_is_noop():
    """KEEP-BOTH: ``scalar_seed_on=False`` is a genuine no-op — returns False and
    leaves the K4 V_inc readout channel all-zero (the S0 baseline is unperturbed).
    """
    eng = _make_engine(N=14)

    applied = apply_scalar_seed_if_enabled(eng, scalar_seed_on=False)

    assert applied is False
    assert np.all(np.asarray(eng._coupled.k4.V_inc) == 0.0)
