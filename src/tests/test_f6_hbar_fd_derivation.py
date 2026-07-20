"""Independent re-derivation of the ℏ-as-FD result from the RAW banked JSON.

Derivation: research/2026-07-20_hbar-as-fd_DERIVATION_FROZEN.md
Driver:     src/scripts/vol_1_foundations/f6_hbar_fd_derivation.py
Data (in):  research/2026-07-19_f6-thermal-floor-arm_result.json (FENCED FD leg §5)

The F9 lesson: re-derive from the raw per-ρ FD-leg fields, NOT the driver's own
booleans. Independently confirm (i) the √ρ amplitude law + ½:½ quadrature split
on the ACTUAL seed_floor (live MC, no engine step); (ii) the forced form
FD = k·√ρ/relax lands within the FROZEN 1.5σ band at every ρ; (iii) the ρ→0
intercept is 0 and the curve is monotone; (iv) the zero-point ω-ratio discriminator.
"""
import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
import pytest

_REPO = Path(__file__).resolve().parents[2]
_DRIVER = _REPO / "src" / "scripts" / "vol_1_foundations" / "f6_hbar_fd_derivation.py"
_ARM_JSON = _REPO / "research" / "2026-07-19_f6-thermal-floor-arm_result.json"

N_ARM_SEEDS = 6
SIGMA_FRAC = 1.0 / np.sqrt(2 * (N_ARM_SEEDS - 1))   # 0.316 — N=6 std-estimate uncertainty
FORM_MATCH_NSIGMA = 1.5                              # FROZEN tolerance band


@pytest.fixture(scope="module")
def drv():
    spec = importlib.util.spec_from_file_location("f6_hbar_fd_derivation", _DRIVER)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def fd():
    rows = json.loads(_ARM_JSON.read_text())["fd_leg"]["rows"]
    return {
        "rho": np.array([r["rho"] for r in rows]),
        "relax": np.array([r["relax_over_trec"] for r in rows]),
        "fluct_sem": np.array([r["fluct_proxy_sem"] for r in rows]),
        "fd_ratio": np.array([r["fd_ratio"] for r in rows]),
    }


def test_banked_fd_ratio_is_fluct_over_relax(fd):
    """The banked fd_ratio IS fluct/relax (re-derive from the two raw columns)."""
    got = np.where(fd["relax"] > 1e-9, fd["fluct_sem"] / fd["relax"], 0.0)
    assert np.allclose(got, fd["fd_ratio"], atol=1e-9)


def test_sqrt_rho_amplitude_law_and_quadrature_split():
    """FIRST-PRINCIPLES: MC the ACTUAL seed_floor — std of a linear functional ∝ √ρ,
    and C-state = L-state = ½·(energy-per-mode). No engine, no lattice step."""
    from ave.thermal.f6_bath_meter import OscillatorBath
    from scripts.vol_1_foundations.f6_counting_arrow_arm import OMEGA_MIN, _m_for
    from scripts.vol_1_foundations.f6_floor_battery import _signal_per_mode, seed_floor

    dw, m = 0.050, _m_for(0.050)
    e_sig = _signal_per_mode(0.050)
    rng = np.random.default_rng(7)
    ratios, asym = [], []
    for rho in (0.3, 1.0, 2.0, 5.0):
        efm = rho * e_sig
        n = 6000
        q = np.empty(n)
        c_state = np.empty(n)
        l_state = np.empty(n)
        for i in range(n):
            bath = OscillatorBath(M=m, omega_min=OMEGA_MIN, delta_omega=dw)
            seed_floor(bath, efm, int(rng.integers(0, 2**31 - 1)))
            q[i] = bath.x.sum()
            c_state[i] = 0.5 * (bath.omega**2 * bath.x**2).sum()
            l_state[i] = 0.5 * (bath.p**2).sum()
        ratios.append(q.std() / np.sqrt(rho))                 # ∝ √ρ ⇒ this is ρ-constant
        asym.append(abs(c_state.mean() - l_state.mean()) / (0.5 * m * efm))
    ratios = np.array(ratios)
    # amplitude law: std/√ρ flat to < 3% (MC noise floor at n=6000)
    assert np.max(np.abs(ratios - ratios.mean())) / ratios.mean() < 0.03
    # equipartition: |C−L| < 5% of the half-energy per mode
    assert max(asym) < 0.05


def test_forced_form_within_frozen_band(fd):
    """Forced FD = k·√ρ/relax (single calibration anchor at ρ=1) within 1.5σ at every ρ."""
    rho, relax, data = fd["rho"], fd["relax"], fd["fd_ratio"]
    i1 = int(np.where(rho == 1.0)[0][0])
    k = data[i1] * relax[i1]                                   # anchor at ρ=1 (√1 = 1)
    pred = np.where(rho > 0, k * np.sqrt(rho) / relax, 0.0)
    nz = (rho > 0) & (data > 0)
    nsig = np.abs((pred[nz] - data[nz]) / (data[nz] * SIGMA_FRAC))
    assert np.max(nsig) <= FORM_MATCH_NSIGMA                   # FORM-MATCH condition


def test_classical_signatures_intercept_zero_and_monotone(fd):
    """Forced classical signatures (D1): ρ→0 intercept is exactly 0; the curve rises monotone."""
    rho, data = fd["rho"], fd["fd_ratio"]
    assert data[rho == 0.0][0] == 0.0                         # no zero-point term (classical seeding)
    assert np.all(np.diff(data[rho > 0]) > 0)                 # more floor ⇒ more fluctuation


def test_zero_point_omega_ratio_discriminator(drv):
    """D2: the derived quantum zero-point ω-ratio = ω_max/ω_min on the primary comb (>1);
    the classical equipartition ratio is exactly 1 (flat in ω)."""
    zp = drv.zero_point_discriminator()
    assert zp["D2_omega_ratio_classical"] == 1.0
    assert zp["D2_omega_ratio_quantum"] == pytest.approx(zp["omega_max"] / zp["omega_min"])
    assert zp["D2_omega_ratio_quantum"] > 1.0
    assert zp["D1_intercept_classical"] == 0.0


def test_driver_reproduces_form_match(drv):
    """End-to-end: the shipped driver's frozen-bin verdict is FORM-MATCH."""
    out = drv.run()
    assert out["overlay"]["verdict"] == "FORM-MATCH"
    assert out["overlay"]["max_abs_nsigma"] <= FORM_MATCH_NSIGMA
    assert out["mc_first_principles"]["amp_law_sqrt_rho_flatness"] < 0.03
