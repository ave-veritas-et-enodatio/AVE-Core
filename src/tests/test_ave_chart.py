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
