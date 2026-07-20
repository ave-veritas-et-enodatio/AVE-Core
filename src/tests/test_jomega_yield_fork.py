"""J(ω) derivation — yield-fork adjudicator: locking tests (2026-07-20).

Prereg (FROZEN): research/2026-07-20_jomega-derivation_prereg_FROZEN.md
Result:          research/2026-07-20_jomega-derivation_result.md
Driver:          src/scripts/vol_4_engineering/jomega_yield_fork.py  (engine byte-UNTOUCHED)

Pins the load-bearing derived numbers so a regression surfaces:
  - the arccos band top π√3·ω_C (srs-band-structure.md, clm-bnd5rq);
  - the 3D-acoustic DOS exponent g(ω)∝ω² and the two coupling-model J(ω) exponents
    (Ohmic s≈1 on-site / super-Ohmic s≈3 strain);
  - the crossing-shape coupling-model split (C1 appreciable / C2 suppressed) → UNDETERMINED;
  - the H-ledger discriminator (R-4 relabel): the FINITE loop area at γ=0 (loop-area ≠
    dissipation); W_diss=0 at γ=0 is a definitional identity; the real (fireable) ledger is
    the drive-work closure W_drive≈W_diss for γ>0; ∮S dr at γ=0 is existence-grade (R-5);
  - R-1 (post-review): the ring-down scale-scan — the ORDERING (0D recovery ≥ ∞-lattice
    recovery) is scale-robust; the drain MAGNITUDE is NOT ("drains to 0–10 %" retracted);
  - R-2 (Rule-11): the FROZEN (a-ledger)/(b-ledger) net-per-cycle-transfer criterion lands
    bin (iii) DEGENERATE — the clean split came only from the POST-HOC undriven ring-down;
  - the batched arccos drag-onset ratio (srs 0.80, chain 1.0) vs the cosine-branch 2/π.

Post-review-repair note (wrapper wf_d07d804e): the ring-down scope-split test was relabeled
POST-HOC single-scale (KEEP-BOTH) and the false "coupling-scale-robust" pin was replaced by
the honest ordering-robust / magnitude-not scale-scan test. See research result §0, §4.

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


def test_h_ledger_finite_loop_is_the_discriminator(band):
    # R-4/F11 relabel: the INFORMATIVE content is the FINITE loop area at γ=0 (loop-area
    # ≠ dissipation), NOT the zero-work leg. W_diss=γ∮v²dt ≡ 0 at γ=0 is a DEFINITIONAL
    # identity (cannot fail on any input — the #721-W2 identity class), so it is asserted
    # here only to document the identity, not as a fireable gate.
    a0, _, w0, _ = jf.second_order_loop(jf.OMEGA_D, gamma=0.0)
    assert a0 > 0.05                 # ★ the discriminator: finite reactive loop at γ=0
    assert w0 == 0.0                 # definitional identity (γ=0 ⇒ γ∮v²=0); not a gate


def test_h_ledger_drive_work_closure_is_the_real_ledger(band):
    # R-4: the actual (fireable) energy ledger the shipped code lacked — the INDEPENDENT
    # drive-work W_drive=κ∮S_eq·v dt must equal the dissipated work W_diss=γ∮v²dt in the
    # driven steady cycle (energy balance). This CAN fail (it is not an identity), so it is
    # the real H-ledger; the world-(c) exclusion rests on this closure, not on the γ=0 pin.
    _, _, w2, wdrv2 = jf.second_order_loop(jf.OMEGA_D, gamma=0.2)
    _, _, w5, wdrv5 = jf.second_order_loop(jf.OMEGA_D, gamma=0.5)
    assert w2 > 0.0 and w5 > 0.0                       # dissipation turns on only with γ>0
    assert w2 == pytest.approx(wdrv2, rel=0.02)        # ledger closes: drive-work = dissipated
    assert w5 == pytest.approx(wdrv5, rel=0.02)


def test_h_ledger_gamma0_loop_area_is_existence_grade(band):
    # R-5/F10: ∮S dr at γ=0 is a SETTLE-WINDOW ARTIFACT (γ=0 has no steady state — the
    # undamped ω_S=1 transient beats against ω_d=0.9). The value is finite at every window
    # but varies ~8× with the settle length, so it is EXISTENCE-grade (finite, O(0.2–1.4)),
    # never value-grade. This test pins the window-DEPENDENCE, refuting any "∮S dr=0.183"
    # value-grade citation.
    areas = [jf.second_order_loop(jf.OMEGA_D, gamma=0.0, n_settle=ns)[0]
             for ns in (40, 80, 160, 320)]
    assert all(a > 0.05 for a in areas)                # finite at every window (existence)
    assert max(areas) / min(areas) > 3.0               # but NOT converged (window-dependent)


def test_ringdown_scope_split_posthoc_single_scale(band):
    # POST-HOC CHARACTERIZATION (F5/R-2): the undriven ring-down is NOT in the frozen prereg
    # (§4-iv freezes only the DRIVEN protocol) and its 0.4/0.2 thresholds were chosen after
    # seeing the data. This cell holds ONLY at the single scale (0.6) the shipped driver ran;
    # it is retained (KEEP-BOTH) to document the scale-0.6 point, NOT as a frozen adjudication.
    # The scale-robust claim is tested honestly in test_ringdown_scale_scan_* below.
    centres, J = band["centres"], band["J"]
    fin = jf.gle_ringdown(centres, J["C1_onsite"], 40, 0.6, n_periods=60)
    den = jf.gle_ringdown(centres, J["C1_onsite"], 1500, 0.6, n_periods=60)
    assert fin["E_S_max_recovery_after_decay"] > 0.4   # returns (reactive) — at scale 0.6 only
    assert den["E_S_max_recovery_after_decay"] < 0.2   # drains (transductive) — at scale 0.6 only


def test_ringdown_scale_scan_ordering_robust_magnitude_not(band):
    # R-1/F1/F6/F9 (post-review extension): the HONEST claim. Scan both coupling models over
    # coupling scale {0.2..1.5}, finite (0D) vs dense (∞-lattice) bath.
    #   (a) the ORDERING  finite-recovery ≥ dense-recovery  IS scale-robust (every cell);
    #   (b) the DRAIN MAGNITUDE is NOT robust — the retracted "∞-lattice drains to 0–10 %"
    #       fails: the super-Ohmic (C2) dense bath recovers 77 % at scale 0.2, 35 % at 0.4
    #       (world-a reactive return), reaching the 0–10 % band only at scale ≥ 0.6. The drain
    #       magnitude is set by the SAME undetermined coupling prefactor ζ as bin (c-magnitude).
    centres, J = band["centres"], band["J"]
    scan = jf.ringdown_scale_scan(centres, J)
    assert scan["_ordering_scale_robust"] is True          # (a) ordering robust — SURVIVES
    assert scan["_dense_drain_0to10_robust"] is False       # (b) drain magnitude NOT robust
    # the specific weak-coupling counterexample the review surfaced (world-a at scale 0.2):
    assert scan["C2_strain"]["0.2"]["dense_recovery"] > 0.5    # ∞-lattice RETURNS at weak coupling
    assert scan["C2_strain"]["0.6"]["dense_recovery"] < 0.15   # only drains at stronger coupling


def test_frozen_ab_ledger_is_degenerate(band):
    # R-2/F2/F5/F7/F12 (Rule-11): the FROZEN (a-ledger)/(b-ledger) criterion the shipped code
    # never computed — net per-cycle transfer vs tol=3.53e-3, driven protocol, per-mode E_bath.
    # PRECISE frozen output: net-per-cycle transfer EXCEEDS tol in every cell (even the finite/0D
    # bath), so (a-ledger) fires in 0/4 cells; the finite baths RETURN within the window so
    # (b-ledger) fails there; only the C2 super-Ohmic ∞-lattice fires (b-ledger) → 1/4. No clean
    # UNIFORM (a)/(b) scope separation (3/4 in the degenerate gap; the 1 world-(b) read is
    # coupling-model-specific) ⇒ bin (iii) DEGENERATE. The clean scope-split came only from the
    # POST-HOC ring-down, not this frozen instrument.
    centres, J = band["centres"], band["J"]
    cells = {}
    for model in ("C1_onsite", "C2_strain"):
        fin = jf.frozen_ab_ledger(centres, J[model], 60, 0.6)
        den = jf.frozen_ab_ledger(centres, J[model], 1200, 0.6)
        # net-per-cycle transfer above the integrator floor in every driven cell:
        assert fin["net_per_cycle_transfer_ge_tol"] is True
        assert den["net_per_cycle_transfer_ge_tol"] is True
        # the finite/0D bath RETURNS within the window (Poincaré) — directionally world-a:
        assert fin["returns_within_window"] is True
        cells[(model, "fin")] = fin
        cells[(model, "den")] = den
    # (a-ledger) never fires: the <tol "reactive refusal" conjunct fails everywhere:
    assert not any(c["a_ledger_fires"] for c in cells.values())
    # (b-ledger) fires ONLY for the super-Ohmic (C2) ∞-lattice — no finite bath, not C1:
    assert not cells[("C1_onsite", "fin")]["b_ledger_fires"]
    assert not cells[("C2_strain", "fin")]["b_ledger_fires"]
    assert cells[("C2_strain", "den")]["b_ledger_fires"]   # the lone world-(b) cell (model-specific)


def test_drag_onset_arccos_beats_cosine(band):
    srs = jf.drag_onset_srs(band["bonds"], n_scan=300)
    ch = jf.drag_onset_chain()
    # arccos srs acoustic ≈ 0.80, well ABOVE the cosine-branch 2/π ≈ 0.637
    assert 0.75 < srs["v_p_min_over_c0_srs_acoustic"] < 0.85
    assert srs["v_p_min_over_c0_srs_acoustic"] > 2.0 / np.pi
    # the 1D arccos chain is exactly dispersionless (ratio 1); the cosine chain gives 2/π
    assert ch["arccos_chain_vp_min_over_c0"] == pytest.approx(1.0, abs=1e-6)
    assert ch["cosine_chain_vp_min_over_c0"] == pytest.approx(2.0 / np.pi, abs=2e-3)
