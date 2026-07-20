"""J(ω) derivation — yield-fork adjudicator: locking tests (2026-07-20).

Prereg (FROZEN): research/2026-07-20_jomega-derivation_prereg_FROZEN.md
Result:          research/2026-07-20_jomega-derivation_result.md
Driver:          src/scripts/vol_4_engineering/jomega_yield_fork.py  (engine byte-UNTOUCHED)

Pins the load-bearing derived numbers so a regression surfaces:
  - the arccos band top π√3·ω_C (srs-band-structure.md, clm-bnd5rq);
  - the 3D-acoustic DOS exponent g(ω)∝ω² and the two coupling-model J(ω) exponents
    (Ohmic s≈1 on-site / super-Ohmic s≈3 strain);
  - the crossing-shape coupling-model split (C1 appreciable / C2 suppressed) → UNDETERMINED;
  - the H-ledger discriminator: a lossless (γ=0) second-order S has a FINITE loop area
    ∮S dr but EXACTLY zero dissipated work — a finite loop ≠ a resistor;
  - the ring-down scope-split (finite/0D recurs = world-a; dense/∞-lattice drains = world-b);
  - the batched arccos drag-onset ratio (srs 0.80, chain 1.0) vs the cosine-branch 2/π.

Marked `engine_sim` (research-tier); opt-in via `make test-engine`.
"""

import importlib.util
from pathlib import Path

import numpy as np
import pytest

_DRV = (Path(__file__).resolve().parents[1]
        / "scripts" / "vol_4_engineering" / "jomega_yield_fork.py")
_spec = importlib.util.spec_from_file_location("jomega_yield_fork", _DRV)
jf = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(jf)

pytestmark = pytest.mark.engine_sim


@pytest.fixture(scope="module")
def band():
    basis, bonds = jf.srs_primitive_bcc()
    centres, g, _ = jf.density_of_states(bonds, n_grid=28, n_bins=140)
    J = jf.build_J(centres, g)
    return {"bonds": bonds, "centres": centres, "g": g, "J": J}


def test_arccos_band_top_pi_sqrt3(band):
    # π√3 ≈ 5.4414 ω_C — the adjudicated arccos band top (NOT the flag-F ω_C assumption)
    assert jf.BAND_TOP == pytest.approx(np.pi * np.sqrt(3.0), rel=1e-12)
    assert jf.BAND_TOP == pytest.approx(5.4414, abs=1e-3)
    # the crossing sits deep INSIDE the band (≈16% of the band top), not near the edge
    assert jf.OMEGA_D / jf.BAND_TOP < 0.2


def test_dos_is_3d_acoustic(band):
    p = jf.low_omega_exponent(band["centres"], band["g"])
    assert 1.5 < p < 2.2  # g(ω) ∝ ω²  (3D acoustic Debye)


def test_J_exponents_ohmic_vs_superohmic(band):
    centres, J = band["centres"], band["J"]

    def s_of(v):
        m = (centres > 0.05) & (centres < 0.6) & (v > 0)
        return float(np.polyfit(np.log(centres[m]), np.log(v[m]), 1)[0])

    s1, s2 = s_of(J["C1_onsite"]), s_of(J["C2_strain"])
    assert 0.6 < s1 < 1.3    # on-site coupling → Ohmic s≈1
    assert 2.3 < s2 < 3.3    # strain coupling → super-Ohmic s≈3


def test_crossing_shape_split_is_undetermined(band):
    # the (a)/(b) SHAPE verdict at ωτ≈0.9 hinges on the coupling model:
    # C1 appreciable (≥0.1 → world-b channel live), C2 suppressed (<0.1 → world-a).
    centres, J = band["centres"], band["J"]
    c1 = jf._interp_at(centres, J["C1_onsite"], jf.OMEGA_D)
    c2 = jf._interp_at(centres, J["C2_strain"], jf.OMEGA_D)
    assert c1 > 0.1      # Ohmic: finite Re(J) at crossing
    assert c2 < 0.1      # super-Ohmic: suppressed
    # both are ZERO at DC and above the band edge (elastic at f≪1/τ; loss NOT max there)
    assert jf._interp_at(centres, J["C1_onsite"], 0.02) < 0.1
    assert jf._interp_at(centres, J["C2_strain"], 0.02) < 0.1


def test_h_ledger_finite_loop_zero_loss(band):
    # THE discriminator: a lossless (γ=0) second-order S gives a FINITE reactive loop
    # area but EXACTLY zero dissipated work — a finite ∮ does not imply a resistor.
    a0, _, w0 = jf.second_order_loop(jf.OMEGA_D, gamma=0.0)
    assert a0 > 0.05                 # finite reactive loop area
    assert w0 == pytest.approx(0.0, abs=1e-14)  # zero dissipation (world-c resistor excluded)
    _, _, w2 = jf.second_order_loop(jf.OMEGA_D, gamma=0.2)
    assert w2 > 0.0                  # dissipation turns on only with an explicit γ


def test_ringdown_scope_split(band):
    # 0D few-mode bath recurs (world-a); dense/∞-lattice bath drains (world-b).
    centres, J = band["centres"], band["J"]
    fin = jf.gle_ringdown(centres, J["C1_onsite"], 40, 0.6, n_periods=60)
    den = jf.gle_ringdown(centres, J["C1_onsite"], 1500, 0.6, n_periods=60)
    assert fin["E_S_max_recovery_after_decay"] > 0.4   # returns (reactive)
    assert den["E_S_max_recovery_after_decay"] < 0.2   # drains (transductive)


def test_drag_onset_arccos_beats_cosine(band):
    srs = jf.drag_onset_srs(band["bonds"], n_scan=300)
    ch = jf.drag_onset_chain()
    # arccos srs acoustic ≈ 0.80, well ABOVE the cosine-branch 2/π ≈ 0.637
    assert 0.75 < srs["v_p_min_over_c0_srs_acoustic"] < 0.85
    assert srs["v_p_min_over_c0_srs_acoustic"] > 2.0 / np.pi
    # the 1D arccos chain is exactly dispersionless (ratio 1); the cosine chain gives 2/π
    assert ch["arccos_chain_vp_min_over_c0"] == pytest.approx(1.0, abs=1e-6)
    assert ch["cosine_chain_vp_min_over_c0"] == pytest.approx(2.0 / np.pi, abs=2e-3)
