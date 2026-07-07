"""Pinning test for the birefringence-discriminator v3 differential chain.

Locks the forward driver `scripts.vol_4_engineering.birefringence_coefficient_discriminator`
as the artifact for the register/leaf `clm-pp3qwf` v3 attribution (PR #565 FIX 4).

The driver emits the matched par-perp DIFFERENTIAL ratio on the Option-B consistent
INSTANTANEOUS footing and its v1 -> v2 -> v3 provenance:
    v1 = 7.5/alpha^3      ~ 1.93e7  (instantaneous SVE -1/2 A^2 over differenced (3/45)alpha^2)
      / (propagating re-normalization 1/(pi alpha) ~ 43.6)
    v2 = 7.5 pi/alpha^2   ~ 4.42e5  (QED denominator -> propagating alpha/(15 pi))
      x (<cos^2>=1/2 carrier average removed)
    v3 = 3.75 pi/alpha^2  ~ 2.2e5   = 15 pi/(4 alpha^2)  <-- THE HEADLINE

Every target below is an INDEPENDENT closed form in ALPHA (no import of the driver's
own intermediate to pin itself). NO fit, NO fit-to-target.
"""
from __future__ import annotations

import numpy as np

from ave.core.constants import ALPHA
from scripts.vol_4_engineering.birefringence_coefficient_discriminator import (
    differential_ratio_v1,
    differential_ratio_v3_chain,
)


def test_v1_differential_closed_form() -> None:
    """v1 == 7.5/alpha^3 (~1.93e7), the instantaneous-SVE-over-(3/45)alpha^2 differential."""
    v1 = differential_ratio_v1()
    assert np.isclose(v1, 7.5 / ALPHA**3, rtol=1e-12)
    assert np.isclose(v1, 1.9300e7, rtol=2e-4)


def test_chain_pins_v2_and_v3() -> None:
    """v2 == 7.5 pi/alpha^2 (~4.42e5); v3 == 3.75 pi/alpha^2 == 15 pi/(4 alpha^2) (~2.2e5)."""
    chain = differential_ratio_v3_chain()
    assert np.isclose(chain["v2"], 7.5 * np.pi / ALPHA**2, rtol=1e-12)
    assert np.isclose(chain["v3"], 3.75 * np.pi / ALPHA**2, rtol=1e-12)
    assert np.isclose(chain["v3"], 15.0 * np.pi / (4.0 * ALPHA**2), rtol=1e-12)
    assert np.isclose(chain["v2"], 4.4247e5, rtol=2e-4)
    assert np.isclose(chain["v3"], 2.2123e5, rtol=2e-4)


def test_step_factors() -> None:
    """v1->v2 drops by the propagating understatement 1/(pi alpha) ~ 43.6; v2->v3 by 1/2."""
    chain = differential_ratio_v3_chain()
    assert np.isclose(chain["v1_to_v2_factor"], 1.0 / (np.pi * ALPHA), rtol=1e-12)
    assert np.isclose(chain["v1_to_v2_factor"], 43.62, rtol=2e-3)
    assert np.isclose(chain["v2_to_v3_carrier"], 0.5, rtol=1e-12)
    # the actual v1->v2 headline ratio 1.93e7/4.42e5 == 1/(pi alpha):
    assert np.isclose(chain["v1"] / chain["v2"], 1.0 / (np.pi * ALPHA), rtol=1e-12)
    assert np.isclose(chain["v2"] / chain["v3"], 2.0, rtol=1e-12)


def test_full_chain_closes() -> None:
    """v1 * (pi alpha) * (1/2) identically equals the v3 closed form 15 pi/(4 alpha^2)."""
    chain = differential_ratio_v3_chain()
    assert np.isclose(
        chain["v1"] * (np.pi * ALPHA) * 0.5,
        15.0 * np.pi / (4.0 * ALPHA**2),
        rtol=1e-12,
    )


def test_per_form_understatement_factors() -> None:
    """The three coefficient-form understatement factors vs the differenced (3/45)alpha^2:
    static-duality alpha/(30 pi) -> 1/(2 pi alpha) ~ 21.8 (the 🔴-note figure),
    propagating   alpha/(15 pi)  -> 1/(pi alpha)   ~ 43.6,
    instantaneous 2 alpha/(15 pi) -> 2/(pi alpha)  ~ 87.2.
    """
    a = ALPHA
    diff_v1_qed = (3.0 / 45.0) * a**2
    assert np.isclose((a / (30.0 * np.pi)) / diff_v1_qed, 1.0 / (2.0 * np.pi * a), rtol=1e-12)
    assert np.isclose((a / (15.0 * np.pi)) / diff_v1_qed, 1.0 / (np.pi * a), rtol=1e-12)
    assert np.isclose((2.0 * a / (15.0 * np.pi)) / diff_v1_qed, 2.0 / (np.pi * a), rtol=1e-12)
    assert np.isclose(1.0 / (2.0 * np.pi * a), 21.81, rtol=2e-3)
    assert np.isclose(1.0 / (np.pi * a), 43.62, rtol=2e-3)
    assert np.isclose(2.0 / (np.pi * a), 87.24, rtol=2e-3)
