"""Tests for the F6 bath meter (rebuilt mode-count detector).

Charter: research/2026-07-16_f6-bath-meter_CHARTER.md
Instrument: src/ave/thermal/f6_bath_meter.py

Fast unit tests (default suite) exercise the meter's load-bearing physics — the
real bath DOF, the M-invariant occupancy read, the back-reaction, and the friction
discriminator. One opt-in `engine_sim` test runs the full V1-V6 battery and asserts
METER-VALID. NO F6 arm is fired anywhere here.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import numpy as np
import pytest

from ave.core.k4_tlm import K4Lattice3D
from ave.thermal import OscillatorBath, make_collar_mask

_DRIVER = Path(__file__).resolve().parents[1] / "scripts" / "vol_1_foundations" / "f6_bath_meter_validate.py"


@pytest.fixture(scope="module")
def driver():
    spec = importlib.util.spec_from_file_location("f6_bath_meter_validate", _DRIVER)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


# --- bath DOF is a REAL oscillator set, not a write-only accumulator ----------
def test_free_rotation_conserves_mode_energy():
    """free_rotate is exact: per-mode energy E_m (C-state x + L-state p) is
    invariant under free evolution — so E_m IS the phase-independent occupancy."""
    bath = OscillatorBath(M=16)
    rng = np.random.default_rng(0)
    bath.x = rng.normal(size=16)
    bath.p = rng.normal(size=16)
    e0 = bath.mode_energy().copy()
    for _ in range(50):
        bath.free_rotate(0.7)
    assert np.allclose(bath.mode_energy(), e0, atol=1e-12)


def test_undriven_bath_reads_zero():
    """A leave that never populates modes reads N_occ = 0 (the read can fail)."""
    bath = OscillatorBath(M=64)
    assert bath.n_occ() == 0
    assert bath.energy() == 0.0


def test_n_occ_M_invariant_under_fixed_drive():
    """Fixed physics (same tone), vary truncation M ⇒ N_occ invariant.

    The direct kill of the twin-64 class (ΔN_occ ≡ M_MODES): the occupancy read
    tracks the driven bandwidth, not the array size."""
    occ = []
    for M in (32, 64, 128):
        bath = OscillatorBath(M=M)
        # drive a fixed tone directly into the bath (fixed physics)
        for i in range(400):
            q = 0.5 * np.sin(0.5 * i)
            bath.coupling_kick(0.5, q, 0.02)
            bath.free_rotate(1.0)
            bath.coupling_kick(0.5, q, 0.02)
        occ.append(bath.n_occ())
    assert occ[0] == occ[1] == occ[2], f"N_occ tracks M: {occ}"
    assert occ[1] <= 4, f"narrowband drive should populate few modes, got {occ[1]}"


def test_n_occ_tracks_bandwidth_not_M():
    """Broadband drive populates MORE modes than a narrowband one at the same M —
    the count tracks physical bandwidth."""

    def drive_count(n_tones):
        bath = OscillatorBath(M=64)
        rng = np.random.default_rng(1)
        freqs = np.linspace(0.35, 1.0, n_tones)
        phases = rng.uniform(0, 2 * np.pi, n_tones)
        for i in range(400):
            q = float(np.sum(0.3 * np.sin(freqs * i + phases)))
            bath.coupling_kick(0.5, q, 0.02)
            bath.free_rotate(1.0)
            bath.coupling_kick(0.5, q, 0.02)
        return bath.n_occ()

    assert drive_count(8) > drive_count(1)


# --- coupled meter: conservation, back-reaction, friction ---------------------
def _mk(driver, **kw):
    return driver._build(**kw)


def test_lossless_control_conserves_and_reads_zero(driver):
    """V1 kernel: no coupling ⇒ machine-conserved AND N_occ = 0."""
    cpl = _mk(driver, kappa=0.0)
    E0 = cpl.e_lat()
    for i in range(1, 120):
        cpl.step(i)
    assert abs(cpl.e_lat() - E0) / E0 < 1e-10
    assert cpl.bath.n_occ() == 0


def test_reactive_coupling_closes_ledger(driver):
    """Production coupling is lossless-reactive: energy lost by the lattice is
    FOUND in the bath (Ax3). R = |ΔE_lat + E_bath| / |ΔE_lat| is small."""
    cpl = _mk(driver)
    E0 = cpl.e_lat()
    for i in range(1, 150):
        cpl.step(i)
    dE_lat = cpl.e_lat() - E0
    assert dE_lat < 0, "reactive bath should absorb lattice energy"
    R = abs(dE_lat + cpl.e_bath()) / abs(dE_lat)
    assert R < 0.2, f"ledger did not close: R={R}"
    assert cpl.bath.n_occ() > 0


def test_back_reaction_changes_lattice(driver):
    """V5 kernel: coupling ON vs OFF produces DIFFERENT lattice trajectories —
    the write-back is a real back-reaction, not a side-array."""
    on = _mk(driver)
    off = _mk(driver, kappa=0.0)
    for i in range(1, 120):
        on.step(i)
        off.step(i)
    D = np.linalg.norm(on.lat.V_inc - off.lat.V_inc) / (np.linalg.norm(off.lat.V_inc) + 1e-30)
    assert D > 1e-3, f"no back-reaction: D={D}"


def test_friction_plant_is_physical_and_distinguished(driver):
    """V4 kernel: real Re(Z) friction removes energy (gone, not stored) and reads
    N_occ = 0 — a different physical bin from the reactive bath, by signature not
    code path."""
    fric = _mk(driver, friction=True, gamma=0.004)
    E0 = fric.e_lat()
    for i in range(1, 150):
        fric.step(i)
    removed = E0 - fric.e_lat()
    assert removed > 0, "friction must dissipate energy"
    assert fric.bath.n_occ() == 0, "friction has no populated bath modes"
    # energy is GONE from the total ledger (bath empty)
    R = abs((fric.e_lat() - E0) + fric.e_bath()) / abs(fric.e_lat() - E0)
    assert R > 0.8


def test_collar_mask_excludes_inactive(driver):
    """The collar is a shell of ACTIVE lattice sites only (clean interface)."""
    lat = K4Lattice3D(12, 12, 12, nonlinear=True, op3_bond_reflection=True, V_SNAP=1.0)
    collar = make_collar_mask(lat, (6, 6, 6), 2.0, 4.0)
    assert collar.sum() > 0
    assert not np.any(collar & ~lat.mask_active)


# --- full battery (opt-in; slow) ---------------------------------------------
@pytest.mark.engine_sim
def test_full_battery_meter_valid(driver):
    """The frozen V1-V6 battery returns METER-VALID (charter §7 verdict)."""
    results, verdict = driver.run_battery()
    failed = [r.vid for r in results if not r.passed]
    assert verdict == "METER-VALID", f"failed: {failed}"
