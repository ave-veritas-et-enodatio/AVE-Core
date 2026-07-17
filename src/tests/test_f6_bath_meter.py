"""Tests for the F6 bath meter (rebuilt mode-count detector; post-#717-review).

Charter: research/2026-07-16_f6-bath-meter_CHARTER.md (+ amendment §A).
Instrument: src/ave/thermal/f6_bath_meter.py

Fast unit tests (default suite) exercise the meter's load-bearing physics — the
real bath DOF, the Nyquist guard, the absolute-floor M-invariant occupancy read,
the on-shell global back-reaction, and the bath-live friction discriminator. One
opt-in `engine_sim` test runs the full V1-V6 battery and asserts
METER-VALID-WITHIN-ENVELOPE. NO F6 arm is fired anywhere here.
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


def test_nyquist_guard_rejects_aliasing_comb():
    """The comb must stay below Nyquist (ω_max·dt < π): building past the cap raises,
    so the twin-64 cannot resurrect via discrete-time aliasing (the #717 CRITICAL)."""
    OscillatorBath(M=90)  # ω_max = 0.30 + 89·0.03 = 2.97 < π — OK
    with pytest.raises(ValueError, match="Nyquist"):
        OscillatorBath(M=200)  # ω_max = 6.27 > π — rejected


def test_undriven_bath_reads_zero():
    """A leave that never populates modes reads N_occ = 0 (the read can fail)."""
    bath = OscillatorBath(M=64)
    assert bath.n_occ() == 0
    assert bath.energy() == 0.0


def test_absolute_floor_rejects_eps_level_energy():
    """The ABSOLUTE floor + minimum-E_bath gate read 0 on eps-level content — the
    relative-to-peak floor (shipped in #717) counted junk at E_bath~1e-21."""
    bath = OscillatorBath(M=64)
    # inject a tiny spectrally-peaked state well below the drive scale
    bath.x[10] = 1e-6
    assert bath.energy() < 1e-2
    assert bath.n_occ() == 0  # gated by e_bath_min, not counted as occupancy


def test_n_occ_M_invariant_under_fixed_drive():
    """Fixed physics (same tone), vary truncation M ⇒ N_occ invariant.

    The direct kill of the twin-64 class (ΔN_occ ≡ M_MODES): the occupancy read
    tracks the driven bandwidth, not the array size. M values stay within Nyquist."""
    occ = []
    for M in (32, 64, 90):
        bath = OscillatorBath(M=M)
        for i in range(400):
            q = 0.5 * np.sin(0.5 * i)
            bath.coupling_kick(0.5, q, 0.02)
            bath.free_rotate(1.0)
            bath.coupling_kick(0.5, q, 0.02)
        occ.append(bath.n_occ())
    assert occ[0] == occ[1] == occ[2], f"N_occ tracks M: {occ}"
    assert occ[1] <= 4, f"narrowband drive should populate few modes, got {occ[1]}"


def test_n_occ_detuning_collapses():
    """Detuning the comb off the drive band collapses N_occ to 0 — the read tracks
    physics; the old ΔN_occ≡M detector would still read M."""

    def driven_count(omega_min):
        bath = OscillatorBath(M=32, omega_min=omega_min)
        for i in range(400):
            q = 0.5 * np.sin(0.5 * i)  # drive tone at 0.5
            bath.coupling_kick(0.5, q, 0.02)
            bath.free_rotate(1.0)
            bath.coupling_kick(0.5, q, 0.02)
        return bath.n_occ()

    assert driven_count(0.30) > 0  # in-band: populated
    assert driven_count(1.5) == 0  # detuned (band 1.5..2.43, off 0.5): collapses


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


def test_reactive_coupling_closes_ledger_no_pump(driver):
    """Production coupling is lossless-reactive (Ax3): energy lost by the lattice is
    FOUND in the bath, and the GLOBAL on-shell rescale does NOT pump — total energy
    conserves to machine precision over a long run (the #717 secular-pump fix)."""
    cpl = _mk(driver)
    E0 = cpl.e_lat()
    Etot0 = E0 + cpl.e_bath()
    max_drift = 0.0
    for i in range(1, 800):
        cpl.step(i)
        max_drift = max(max_drift, abs((cpl.e_lat() + cpl.e_bath()) - Etot0) / E0)
    dE_lat = cpl.e_lat() - E0
    assert dE_lat < 0, "reactive bath should absorb lattice energy"
    R = abs(dE_lat + cpl.e_bath()) / abs(dE_lat)
    assert R < 0.2, f"ledger did not close: R={R}"
    assert cpl.bath.n_occ() > 0
    assert max_drift < 1e-10, f"secular pump present: max total-E drift {max_drift}"


def test_back_reaction_changes_lattice(driver):
    """V5 kernel: coupling ON vs OFF produces DIFFERENT lattice trajectories —
    the back-reaction is real, not a side-array."""
    on = _mk(driver)
    off = _mk(driver, kappa=0.0)
    for i in range(1, 200):
        on.step(i)
        off.step(i)
    a = on.active
    D = np.linalg.norm(on.lat.V_inc[a] - off.lat.V_inc[a]) / (np.linalg.norm(off.lat.V_inc[a]) + 1e-30)
    assert D > 1e-3, f"no back-reaction: D={D}"


def test_friction_bath_live_and_distinguished(driver):
    """V4 kernel: the friction plant keeps the bath LIVE (driven) but Re(Z)-damps
    it, so energy is DISSIPATED (gone) — R is genuinely MEASURED on both plants and
    can fail (fixes the #717 cannot-fail friction bin)."""
    reactive = _mk(driver)
    E0r = reactive.e_lat()
    for i in range(1, 800):
        reactive.step(i)
    R_reactive = abs((reactive.e_lat() - E0r) + reactive.e_bath()) / abs(reactive.e_lat() - E0r)

    fric = _mk(driver, friction=True, beta=0.01)
    E0f = fric.e_lat()
    for i in range(1, 800):
        fric.step(i)
    R_fric = abs((fric.e_lat() - E0f) + fric.e_bath()) / abs(fric.e_lat() - E0f)

    assert fric.friction_removed > 0, "friction must dissipate energy from the live bath"
    assert R_reactive < 0.2, f"reactive should store (R small): {R_reactive}"
    assert R_fric > 0.8, f"friction should dissipate (R large): {R_fric}"


def test_collar_mask_excludes_inactive(driver):
    """The collar is a shell of ACTIVE lattice sites only (clean interface)."""
    lat = K4Lattice3D(12, 12, 12, nonlinear=False, op3_bond_reflection=True, V_SNAP=1.0)
    collar = make_collar_mask(lat, (6, 6, 6), 2.0, 4.0)
    assert collar.sum() > 0
    assert not np.any(collar & ~lat.mask_active)


# --- full battery (opt-in; slow) ---------------------------------------------
@pytest.mark.engine_sim
def test_full_battery_meter_valid(driver):
    """The frozen V1-V6 battery returns METER-VALID-WITHIN-ENVELOPE (charter §7)."""
    results, verdict = driver.run_battery()
    failed = [r.vid for r in results if not r.passed]
    assert verdict == "METER-VALID-WITHIN-ENVELOPE", f"failed: {failed}"
