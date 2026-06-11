"""
Smoke ladder — COMPONENT 6: the D7 electron spec-sheet harness (T1–T6).

Per Rule 11 this harness is the success-GATE, NOT a verdict — the electron-class
result is produced by RUNNING it on an assembled object (run-time). The smoke
calibrates each Ti on its KNOWN-NULL + KNOWN-POSITIVE case (the floor gates first).

  T1  flat series ⇒ CONVERGED; secularly-rising ⇒ STILL-RISING (the falsifier).
  T2  a planted (2,3) ω ⇒ QUANTIZED-2-3; ω≡0 ⇒ NOT-2-3; r<3 ⇒ VOID (F0b floor).
  T3  a rigid rotation ⇒ finite L_bulk with the correct sense + a derived target.
  T5  a compact flow ⇒ BALANCED (born-in-pairs).
  T6  λ=h/p synthetic ⇒ INVERSE-P; λ=const ⇒ NOT-INVERSE-P.
  T4  a reverify callable ⇒ RE-VERIFIED / FAILED-POST-KICK.

Suite:  src/ave/core/electron_spec_suite.py
Prereg: research/2026-06-10_genesis-v5-seeded-snap_prereg.md (D7, §4.2)
"""

import numpy as np

from ave.core.unified_genesis_engine import UnifiedGenesisEngine
from ave.core.electron_spec_suite import (
    spec_T1_mass_converges, spec_T2_charge_winding, spec_T3_spin,
    spec_T4_stability_kick, spec_T5_born_in_pairs, spec_T6_de_broglie,
)
from ave.utils.fast_winding_extractor import _planted_2_3_field


def test_T1_converged_vs_still_rising():
    flat = 1.0 + 1e-6 * np.random.RandomState(0).randn(200)
    rising = np.linspace(1.0, 2.0, 200)
    assert spec_T1_mass_converges(flat, drift_floor=1e-2)["bin"] == "CONVERGED"
    r = spec_T1_mass_converges(rising, drift_floor=1e-2)
    assert r["bin"] == "STILL-RISING", r


def test_T2_planted_2_3_vs_null_vs_void():
    N = 48
    omega, pi_omega, R, r = _planted_2_3_field(N=N, amplitude=0.3, p=2, q=3)
    eng = UnifiedGenesisEngine(N)
    eng.omega = omega.copy()
    eng.omega_prev = (omega - pi_omega * eng.dt).copy()
    pos = spec_T2_charge_winding(eng, R, r)
    assert pos["bin"] == "QUANTIZED-2-3", pos
    # known-null: no winding
    eng.omega[:] = 0.0
    eng.omega_prev[:] = 0.0
    assert spec_T2_charge_winding(eng, R, r)["bin"] == "NOT-2-3"
    # F0b floor: r below 3 cells ⇒ VOID
    assert spec_T2_charge_winding(eng, R, 2.0)["bin"] == "VOID"


def test_T3_rigid_rotation_has_sense_and_target():
    N = 32
    eng = UnifiedGenesisEngine(N, bulk_density_on=True)
    R_core = 0.25 * N * eng.dx
    eng.energize_rotation_column(M_edge=0.5, R_core=R_core, axis=2)
    res = spec_T3_spin(eng, R_ring=R_core, axis=2)
    assert res["L_bulk"] > 0.0, res  # CCW column ⇒ positive L
    assert np.isfinite(res["ratio_to_half_form"])


def test_T5_compact_flow_balanced():
    N = 28
    eng = UnifiedGenesisEngine(N, bulk_density_on=True)
    eng.energize_rotation_column(M_edge=0.4, R_core=0.25 * N * eng.dx, axis=2)
    assert spec_T5_born_in_pairs(eng)["bin"] == "BALANCED"


def test_T6_inverse_p_vs_const():
    p = np.array([1.0, 2.0, 4.0, 8.0])
    assert spec_T6_de_broglie(p, 6.626 / p)["bin"] == "INVERSE-P"
    assert spec_T6_de_broglie(p, np.ones_like(p))["bin"] == "NOT-INVERSE-P"


def test_T4_reverify_wrapper():
    assert spec_T4_stability_kick(lambda: True)["bin"] == "RE-VERIFIED"
    assert spec_T4_stability_kick(lambda: False)["bin"] == "FAILED-POST-KICK"
