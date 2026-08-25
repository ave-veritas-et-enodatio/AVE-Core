"""Tests for the AVE chart instrument (``ave.viz.ave_chart``).

Gates the instrument's analytic anchors against the canonical receipts:
  - bilinear map identities (Op3, operators.md:43)
  - the canonical Gamma(A_0) locus endpoints (cvr-reflection-smith.md Sec.2)
  - the 1-alpha rim band from ave.core.constants (cvr-reflection-smith.md Sec.3)
  - the z=3 vertex counting fact and its uniform-bias exactness
    (translation-circuit.md:189 + the 2026-08-24 uniform-bias invariance lane)
  - figure smoke: white facecolor, no baked titles (house style).
"""

from __future__ import annotations

import numpy as np
import pytest

import matplotlib

matplotlib.use("Agg")

from ave.core.constants import ALPHA
from ave.viz import ave_chart, style


# ---------------------------------------------------------------------------
# Bilinear map (Op3) identities
# ---------------------------------------------------------------------------
class TestBilinear:
    def test_matched_z1_maps_to_zero(self):
        assert ave_chart.gamma_of_z(1.0) == pytest.approx(0.0, abs=1e-15)

    def test_short_z0_maps_to_minus_one(self):
        assert ave_chart.gamma_of_z(0.0) == pytest.approx(-1.0, abs=1e-15)

    def test_open_zinf_maps_to_plus_one(self):
        assert ave_chart.gamma_of_z(np.inf) == pytest.approx(1.0, abs=1e-15)

    def test_z2_and_half_give_third_magnitude(self):
        # z and 1/z map to +/- the same |Gamma| (Mobius Z<->1/Z gauge)
        g2 = ave_chart.gamma_of_z(2.0)
        gh = ave_chart.gamma_of_z(0.5)
        assert abs(g2) == pytest.approx(1.0 / 3.0, abs=1e-15)
        assert abs(gh) == pytest.approx(1.0 / 3.0, abs=1e-15)
        assert g2.real == pytest.approx(-gh.real, abs=1e-15)


# ---------------------------------------------------------------------------
# The 1-alpha rim band (AVE-distinct; from canonical constants, not hard-code)
# ---------------------------------------------------------------------------
class TestRimBand:
    def test_wall_magnitude_is_sqrt_one_minus_alpha(self):
        assert ave_chart.GAMMA_WALL == pytest.approx(np.sqrt(1.0 - ALPHA), abs=1e-15)
        assert ave_chart.GAMMA_WALL_SQ == pytest.approx(1.0 - ALPHA, abs=1e-15)

    def test_wall_sits_inside_unit_circle(self):
        assert 0.99 < ave_chart.GAMMA_WALL < 1.0


# ---------------------------------------------------------------------------
# Bias-locus forms (canonical core + graded two-junction J/B)
# ---------------------------------------------------------------------------
class TestBiasLoci:
    def test_core_locus_endpoints_exact(self):
        # cvr-reflection-smith.md Sec.2: A=0 matched (free photon), A=1 short (TIR wall)
        assert ave_chart.gamma_of_A(0.0, "core") == pytest.approx(0.0, abs=1e-15)
        assert ave_chart.gamma_of_A(1.0, "core") == pytest.approx(-1.0, abs=1e-15)

    def test_core_locus_is_real_and_monotone(self):
        A = np.linspace(0, 1, 101)
        g = ave_chart.gamma_of_A(A, "core")
        assert np.all(np.isreal(g))
        assert np.all(np.diff(g) < 0)  # monotone toward the short

    def test_form_J_endpoints_exact(self):
        # bare z=3 vertex at A=0 (counting fact), all-arms-short at A=1
        assert ave_chart.gamma_of_A(0.0, "J") == pytest.approx(-1.0 / 3.0, abs=1e-15)
        assert ave_chart.gamma_of_A(1.0, "J") == pytest.approx(-1.0, abs=1e-15)

    def test_form_B_endpoints_and_matched_crossing(self):
        assert ave_chart.gamma_of_A(0.0, "B") == pytest.approx(-1.0 / 3.0, abs=1e-15)
        assert ave_chart.gamma_of_A(1.0, "B") == pytest.approx(1.0, abs=1e-15)
        # matched crossing at A = sqrt(15)/4 (sqrt(S) = 1/2) to 1e-12
        assert ave_chart.gamma_of_A(np.sqrt(15.0) / 4.0, "B") == pytest.approx(0.0, abs=1e-12)
        assert ave_chart.A_MATCHED_B == pytest.approx(np.sqrt(15.0) / 4.0, abs=1e-15)

    def test_unknown_form_raises(self):
        with pytest.raises(ValueError):
            ave_chart.gamma_of_A(0.5, "nope")


# ---------------------------------------------------------------------------
# Uniform-bias invariance: the -1/3 vertex reflection is EXACT at all orders
# under a uniform bias (numerically computed ratio, all tested amplitudes)
# ---------------------------------------------------------------------------
class TestUniformBiasInvariance:
    def test_minus_third_exact_at_all_tested_amplitudes(self):
        A = np.linspace(0.0, 0.999999, 400)  # S > 0 (the medium still exists)
        g = ave_chart.gamma_two_junction_uniform(A)
        np.testing.assert_allclose(g, -1.0 / 3.0, rtol=0, atol=1e-14)

    def test_differential_bias_actually_splits(self):
        # sanity counter-arm: the invariance is not a tautology of the test —
        # the differential forms DO move off -1/3 at the same amplitudes
        A = np.array([0.3, 0.7, 0.95])
        assert np.all(np.abs(ave_chart.gamma_of_A(A, "J") + 1.0 / 3.0) > 1e-3)
        assert np.all(np.abs(ave_chart.gamma_of_A(A, "B") + 1.0 / 3.0) > 1e-3)


# ---------------------------------------------------------------------------
# Two-junction composite transfer matrix
# ---------------------------------------------------------------------------
class TestTwoJunction:
    def test_cold_dc_limit(self):
        # theta=0: line transparent; near shunt Z0/2 parallel far Z0/2 = Z0/4
        g = ave_chart.two_junction_gamma(0.0)
        assert g == pytest.approx((0.25 - 1) / (0.25 + 1), abs=1e-12)

    def test_quarter_wave_limit(self):
        # theta=pi/2: far Z0/2 transforms to 2*Z0; parallel with Z0/2 -> 0.4*Z0
        g = ave_chart.two_junction_gamma(np.pi / 2 - 1e-9)
        assert g == pytest.approx((0.4 - 1) / (0.4 + 1), abs=1e-6)

    def test_locus_stays_inside_unit_disk(self):
        th = np.linspace(0, 2 * np.pi, 500)
        g = ave_chart.two_junction_gamma(th)
        assert np.all(np.abs(g) <= 1.0 + 1e-9)  # passive composite

    def test_biased_composite_approaches_rim(self):
        # composite biased hard (line + ends), cold feed: collapses to a short
        A_hard = 1.0 - 1e-12
        g = ave_chart.two_junction_gamma(0.3, A_line=A_hard, A_ends=A_hard)
        assert abs(g + 1.0) < 1e-2


# ---------------------------------------------------------------------------
# Figure smoke (house style: white facecolor, no baked titles)
# ---------------------------------------------------------------------------
class TestFigureSmoke:
    @pytest.fixture(autouse=True)
    def _style(self):
        style.apply()

    def test_base_chart_renders_white_untitled(self):
        import matplotlib.pyplot as plt

        fig, ax = ave_chart.base_chart()
        fig.canvas.draw()
        assert fig.get_facecolor()[:3] == (1.0, 1.0, 1.0)
        assert getattr(fig, "_suptitle", None) is None or not fig._suptitle.get_text()
        for a in fig.axes:
            assert not a.get_title().strip()
        # rim band + annotations actually landed on the axes
        assert any(a for a in ax.patches) or ax.collections or ax.lines
        plt.close(fig)

    def test_plot_helpers_render_on_chart(self):
        import matplotlib.pyplot as plt

        fig, (axc, axh) = plt.subplots(1, 2)
        ave_chart.base_chart(axc, annotate=False)
        A = np.linspace(0, 0.999, 200)
        ave_chart.plot_bias_trajectory(axc, A, "core", color=style.COLORS["ave"])
        ave_chart.plot_bias_trajectory(axc, A, "J", im_offset=0.03,
                                       color=style.COLORS["accent"])
        ave_chart.plot_frequency_locus(axc, np.linspace(0, 2 * np.pi, 100),
                                       color=style.COLORS["comparison"])
        t = np.linspace(0, 20 * np.pi, 4000)
        A_t = 0.5 + 0.3 * np.sin(t)  # test-local orbit (demo lives in driver)
        hb, hist_art = ave_chart.plot_occupancy(axc, A_t, "core", ax_hist=axh)
        fig.canvas.draw()
        assert hb is not None and hist_art is not None
        assert len(axc.lines) > 0
        plt.close(fig)
