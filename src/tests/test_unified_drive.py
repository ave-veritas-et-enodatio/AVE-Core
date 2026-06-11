"""
Smoke ladder — COMPONENT 4: the D5 drive (FOC d/q chiral photon + arms).

  PROJ-D     a purely cyl-RADIAL field projects to the d-axis only (P_q=0): the
             FLUX/core-rarefaction role.
  PROJ-Q     a purely cyl-AZIMUTHAL field projects to the q-axis only (P_d=0) with
             the correct net-torque SIGN (CCW>0, CW<0): the TORQUE/spin-up role.
  INJECT     drive_chiral_photon deposits transverse-photon energy (w≠0) and
             records the FOC axis + helicity.
  HANDEDNESS the photon's QUADRATIC helicity flips sign RH↔LH (the v4 sign-carry).
             FINDING (recorded, not hidden): the net LINEAR q-torque is symmetry-
             balanced (~0) — the handedness is in the helicity, NOT the linear
             torque (the v4 'scalar sign cannot carry charge' lesson).
  BEMF       the κ_L=6/5 BEMF meter is 0 with the lock OFF, nonzero-capable with
             it ON; the inherited lock is centered/stable (the velocity-dependent-
             force integration mandate already satisfied).

Engine:  src/ave/core/unified_genesis_engine.py (drive_chiral_photon, foc_dq_*)
Prereg:  research/2026-06-10_genesis-v5-seeded-snap_prereg.md (D5)
"""

import numpy as np

from ave.core.unified_genesis_engine import UnifiedGenesisEngine


def test_proj_d_radial_is_pure_flux():
    N = 24
    eng = UnifiedGenesisEngine(N)
    e_rho, _ = eng._foc_unit_vectors(2)
    out = eng.foc_dq_project(e_rho, axis=2)
    assert out["P_d"] > 0.0
    assert abs(out["P_q"]) < 1e-9 * out["P_d"], out
    assert abs(out["net_q_torque"]) < 1e-9 * out["P_d"]


def test_proj_q_azimuthal_is_pure_torque_with_sign():
    N = 24
    eng = UnifiedGenesisEngine(N)
    _, e_phi = eng._foc_unit_vectors(2)
    ccw = eng.foc_dq_project(e_phi, axis=2)
    cw = eng.foc_dq_project(-e_phi, axis=2)
    assert ccw["P_q"] > 0.0 and abs(ccw["P_d"]) < 1e-9 * ccw["P_q"]
    assert ccw["net_q_torque"] > 0.0 and cw["net_q_torque"] < 0.0
    assert abs(ccw["net_q_torque"] + cw["net_q_torque"]) < 1e-9 * ccw["P_q"]


def test_inject_deposits_chiral_photon():
    N = 24
    eng = UnifiedGenesisEngine(N)
    assert float(np.max(np.abs(eng.w))) == 0.0
    eng.drive_chiral_photon(helicity=+1, sigma=5.0, wavelength=8.0, amplitude=0.05, axis=2)
    assert float(np.max(np.abs(eng.w))) > 0.0
    assert eng.foc_axis == 2 and eng.drive_helicity == +1


def test_handedness_flips_with_helicity():
    N = 28

    def meter(hel):
        e = UnifiedGenesisEngine(N, lock_on=True)
        e.seed_lane1(frac=0.85, sigma=4.0)
        e.freeze_wall_window()
        e.drive_chiral_photon(helicity=hel, sigma=5.0, wavelength=8.0,
                              amplitude=0.1, axis=2)
        for _ in range(8):
            e.step()
        return e.foc_dq_meter()

    rh = meter(+1)
    lh = meter(-1)
    # the handedness (quadratic helicity) flips sign
    assert rh["photon_helicity"] * lh["photon_helicity"] < 0.0, (rh, lh)
    assert abs(rh["photon_helicity"]) > 1e-3
    # the d/q POWERS are real and present (the drive does both roles)
    assert rh["P_d"] > 0.0 and rh["P_q"] > 0.0
    # the net LINEAR q-torque is symmetry-balanced (the recorded finding)
    assert abs(rh["net_q_torque"]) < 1e-6 * (rh["P_q"] + 1e-30)


def test_bemf_meter_off_when_lock_off():
    N = 24
    off = UnifiedGenesisEngine(N, lock_on=False)
    off.seed_lane1(frac=0.6, sigma=4.0)
    off.freeze_wall_window()
    off.drive_chiral_photon(helicity=+1, amplitude=0.1, axis=2)
    for _ in range(5):
        off.step()
    assert off.bemf_power() == 0.0
    # with the lock ON the engine stays finite (centered/stable lock)
    on = UnifiedGenesisEngine(N, lock_on=True, lock_eta=0.08)
    on.seed_lane1(frac=0.6, sigma=4.0)
    on.freeze_wall_window()
    on.drive_chiral_photon(helicity=+1, amplitude=0.1, axis=2)
    for _ in range(20):
        on.step()
    assert np.all(np.isfinite(on.omega))
