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


# --- W-battery: nonlinear-regime revalidation (charter §B) --------------------
def test_w_nonlinear_flag_is_noop_given_op3(driver):
    """§B1 FACT-1: with op3_bond_reflection=True the `nonlinear` flag is a NO-OP —
    the K4 4-port scatter matrix is z-independent, so the amplitude-dependent kernel
    flows through op3's bond Γ (already on in the cold plant), NOT the flag. This is
    why the nonlinearity knob is AMPLITUDE (seed scale), not the flag."""
    lin = driver._build(kappa=0.0, nonlinear=False, scale=1.8)
    nl = driver._build(kappa=0.0, nonlinear=True, scale=1.8)
    for _ in range(80):
        lin.lat.step()
        nl.lat.step()
    assert float(np.max(np.abs(lin.lat.V_inc - nl.lat.V_inc))) < 1e-12


def test_w_operating_points_reach_target_amax(driver):
    """The frozen seed scales (§B1 table) reach mild≈0.10 / moderate≈0.30 /
    near-knee≈0.50 A_max (post-first-step, on-shell)."""
    targets = {"mild": 0.10, "moderate": 0.30, "near-knee": 0.50}
    for name, scale in driver.OP_SCALES.items():
        cpl = driver._build(nonlinear=True, scale=scale)
        assert abs(driver._amax(cpl) - targets[name]) < 0.03, name


def test_w_global_rescale_no_pump_on_nonlinear_plant(driver):
    """★The decisive W2 physics in miniature: with the kernel active at the moderate
    point, the GLOBAL energy-matched rescale STILL conserves E_lat+E_bath (no secular
    pump resurrects). Confirms conservation is ledger-enforced (rescale removes exactly
    Δe_bath; op3 is power-conserving), NOT dependent on the linear on-shell argument."""
    cpl = driver._build(nonlinear=True, scale=1.8)
    E0 = cpl.e_lat()
    Etot0 = E0 + cpl.e_bath()
    max_drift = 0.0
    for i in range(1, 500):
        cpl.step(i)
        max_drift = max(max_drift, abs((cpl.e_lat() + cpl.e_bath()) - Etot0) / E0)
    assert max_drift < 1e-10, f"nonlinear-regime pump resurrected: {max_drift}"
    assert cpl.e_bath() > 0  # genuine transfer, not a dead coupling


def test_w_tare_scalar_is_the_fitted_global_attenuation(driver):
    """W5: on the nonlinear plant the computable tare c=√(1−E_bath/E0) matches the
    best-fit global scalar c_fit=⟨V_on·V_off⟩/⟨V_off·V_off⟩ within 2% — so a future
    F6 arm can tare a spatial discriminant without a per-run fit (§B0 tare rule)."""
    on = driver._build(nonlinear=True, scale=1.8)
    off = driver._build(kappa=0.0, nonlinear=True, scale=1.8)
    E0 = on.e_lat()
    for i in range(1, 400):
        on.step(i)
        off.step(i)
    a = on.active
    von = on.lat.V_inc[a].ravel()
    voff = off.lat.V_inc[a].ravel()
    c = np.sqrt(max(1.0 - on.e_bath() / E0, 0.0))
    c_fit = float(np.dot(von, voff) / np.dot(voff, voff))
    assert abs(c_fit - c) / c < 0.02, f"tare {c} != fitted {c_fit}"


def test_w_detuning_collapses_on_nonlinear_plant(driver):
    """W3 in miniature: on the nonlinear moderate plant, a comb detuned off the drive
    band collapses N_occ to 0 (transfer is resonance-gated, not amount-matched) —
    the genuine-coupling soul-check survives the kernel."""
    res = driver._build(M=64, nonlinear=True, scale=1.8, omega_min=0.30)
    det = driver._build(M=32, nonlinear=True, scale=1.8, omega_min=1.5)
    for i in range(1, 800):
        res.step(i)
        det.step(i)
    assert res.bath.n_occ() > 0
    assert det.bath.n_occ() == 0
    assert res.e_bath() / max(det.e_bath(), 1e-30) >= 100  # ≥2 orders (frozen)


# --- full batteries (opt-in; slow) -------------------------------------------
@pytest.mark.engine_sim
def test_full_battery_meter_valid(driver):
    """The frozen V1-V6 battery returns METER-VALID-WITHIN-ENVELOPE (charter §7)."""
    results, verdict = driver.run_battery()
    failed = [r.vid for r in results if not r.passed]
    assert verdict == "METER-VALID-WITHIN-ENVELOPE", f"failed: {failed}"


@pytest.mark.engine_sim
def test_w_full_battery_meter_valid_nonlinear(driver):
    """The frozen W1-W6 nonlinear-regime battery returns METER-VALID-NONLINEAR-
    ENVELOPE (charter §B): no pump resurrects (W2), the detuning collapse survives
    (W3), N_occ is harmonic-honest (W4), and the tare is usable at all three points
    (W5). NO F6 arm is fired."""
    results, verdict = driver.run_w_battery()
    failed = [r.vid for r in results if not r.passed]
    assert verdict == "METER-VALID-NONLINEAR-ENVELOPE", f"failed: {failed}"


# --- X-battery (§C κ-reval) fast unit tests on the new pure helpers -----------
# The full X-battery is a ~4-minute driver (banked in research/); these lock the
# artifact-fix helpers (drain-robust ω_d, harmonic-aware placement, parabolic
# dressed-frequency) that the FIRST X-run got wrong, against regression.
def test_x_fold_into_nyquist(driver):
    """_fold maps any angular frequency into (0, π) (dt=1 aliasing)."""
    assert driver._fold(0.5) == pytest.approx(0.5)
    assert driver._fold(2 * np.pi - 0.5) == pytest.approx(0.5)  # folds back
    assert 0 <= driver._fold(5.0) <= np.pi


def test_x_omega_d_from_bath_is_drain_robust(driver):
    """ω_d = the bath mode that absorbed the most energy — robust to the full-
    discharge regime that collapsed the collar-q rFFT to DC in the first X-run."""
    omega = np.array([0.30, 0.40, 0.50, 0.60, 0.70])
    me = np.array([1e-4, 1e-3, 1.0, 2e-3, 1e-4])  # peak at index 2 → ω=0.50
    assert driver._omega_d_from_bath(me, omega) == pytest.approx(0.50)
    # empty / dead transfer → nan (no spurious ω_d)
    assert np.isnan(driver._omega_d_from_bath(np.zeros(5), omega))


def test_x_dressed_omega_recovers_sinusoid_frequency(driver):
    """_dressed_omega recovers a pure-tone angular frequency to sub-bin accuracy
    (parabolic rFFT peak) — the X6 mode-pulling read must resolve ≪ Δω/2 = 0.005."""
    n = 3000
    omega_true = 0.5237
    t = np.arange(n)
    series = np.cos(omega_true * t)
    assert driver._dressed_omega(series) == pytest.approx(omega_true, abs=0.002)
    # a DC / undriven series returns nan (excluded from the pulling max, not 0)
    assert np.isnan(driver._dressed_omega(np.zeros(n)))


def test_x_detuned_placement_avoids_folded_harmonics(driver):
    """_place_detuned_harmonic_aware returns a Nyquist-valid band ≥ 2·Δω clear of
    every folded harmonic n·ω_d. NB (PR #724 F1): this SUPERSEDED helper is NOT the
    X2 placement — X2 uses the frozen q-power-budget _place_detuned_band. Kept for
    provenance; test asserts the helper's own contract only."""
    dw = 0.010
    omega_d = 0.520
    om_lo, om_hi, clear, folded = driver._place_detuned_harmonic_aware(
        omega_d, dw, m_det=32, omega_max_res=0.30 + 70 * dw)
    assert om_hi < np.pi  # Nyquist
    assert clear >= 2 * dw - 1e-9  # ≥ guard from all folded harmonics
    for h in folded:
        assert not (om_lo - 2 * dw <= h <= om_hi + 2 * dw)  # band contains no harmonic


def test_x_frozen_placement_dodges_genuine_lattice_line(driver):
    """FROZEN §C X2 placement (_place_detuned_band, PR #724 F1): the detuned band is
    chosen by the MEASURED q-power budget (< W3_POWER_FRAC_MAX), so it dodges a genuine
    INDEPENDENT lattice line (not at any n·ω_d) that harmonic-avoidance is blind to.

    Synthetic q-spectrum: bulk drive power below ω≈1.10 plus a strong independent line
    at ω≈1.12 (the real plant's line that the shipped harmonic-aware band [1.07,1.38]
    sat ON, reading a manufactured ×3.6 'LOST'). The frozen rule must return a band
    whose q-power fraction is < W3_POWER_FRAC_MAX AND that does not overlap the line."""
    freqs = np.linspace(0.0, np.pi, 2000)
    psd = np.zeros_like(freqs)
    # bulk drive content (ω≈0.5) + a STRONG independent line at 1.12 (no n·0.52 harmonic)
    psd += 1.0 * np.exp(-((freqs - 0.52) ** 2) / (2 * 0.05**2))
    psd += 0.20 * np.exp(-((freqs - 1.12) ** 2) / (2 * 0.01**2))
    cum = np.cumsum(psd) / psd.sum()
    om_lo, om_hi, band_frac, omega_99 = driver._place_detuned_band(freqs, psd, cum)
    assert om_hi < np.pi  # Nyquist-valid
    assert band_frac < driver.W3_POWER_FRAC_MAX  # the frozen contract: off the power budget
    assert not (om_lo <= 1.12 <= om_hi)  # dodges the genuine line (unlike harmonic-avoidance)
