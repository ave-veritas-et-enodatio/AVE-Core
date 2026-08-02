"""Pin test for the PVLAS matched-differential ARBITER (`coefficient_ratio_differential_pvlas`).

Closes a coverage gap found by the D7 gated consumer sweep
(`research/2026-08-01_pvlas-arbiter-v3-repoint_scoping.md` §2.3): before this file,
**zero tests pinned the arbiter**. The only `4.4247e5` assertion in the suite lives in
`test_birefringence_v3_chain.py` and pins a DIFFERENT module (the
`birefringence_coefficient_discriminator` v1->v2->v3 chain driver), so the live bench
arbiter could — and did — drift a whole re-freeze behind the KB with nothing failing.

Grant ruling D7 (2026-08-01), verbatim [sic]: "D7: follow your rec"; shape (B) per the
2026-08-02 "go". The arbiter's default is now the INSTANTANEOUS footing:

    delta_n_AVE/delta_n_QED = (1/2) / (2 alpha/(15 pi)) * (E_crit/E_yield)^2
                            = 15 pi/(4 alpha^2) = 3.75 pi/alpha^2 ~ 2.2123e5   (v3)

boxed at `manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/`
`vacuum-birefringence-e4.md`:34 (restated unboxed in the Option-B body at :104; the
convention chain is at :106).

DERIVED-NOT-HARDCODED: every target below is an INDEPENDENT closed form in `ALPHA`
imported from `ave.core.constants`. The arbiter's own return is never used to pin
itself, and no target is a literal transcribed from the KB prose. The decimal
`~2.2123e5` cross-checks are loose-tolerance sanity rails on top of the exact forms,
not the primary assertions. NO fit, NO fit-to-target.
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.bench import coefficient_ratio_differential_pvlas as arbiter
from ave.bench.birefringence import substrate_identity_holds
from ave.core.constants import ALPHA, E_CRIT, E_YIELD


def test_default_is_the_v3_instantaneous_refreeze() -> None:
    """The DEFAULT (no argument) is the v3 re-freeze 15 pi/(4 alpha^2) — the D7 payload.

    This is the assertion that would have caught the original drift: it pins the
    ENTRY PATH, not a named branch, so a default flip cannot pass silently.
    """
    assert np.isclose(arbiter(), 15.0 * np.pi / (4.0 * ALPHA**2), rtol=1e-12)
    assert np.isclose(arbiter(), 3.75 * np.pi / ALPHA**2, rtol=1e-12)
    # the default and the explicitly-named branch are the same object
    assert arbiter() == arbiter(geometry="instantaneous")


def test_v3_derives_from_the_ratio_form_not_a_literal() -> None:
    """v3 reconstructs from its PHYSICS pieces: AVE (1/2) leg over instantaneous QED.

    Rebuilds the ratio from the AVE differential coefficient and the instantaneous
    one-loop coefficient independently of the closed form, routed through the
    substrate identity (E_CRIT/E_YIELD)^2 == 1/alpha. Agreement of the physics
    reconstruction with the closed form is the real content.
    """
    assert substrate_identity_holds()
    ave_leg = 0.5 * (E_CRIT / E_YIELD) ** 2  # = 1/(2 alpha)
    qed_instantaneous = 2.0 * ALPHA / (15.0 * np.pi)
    assert np.isclose(arbiter(geometry="instantaneous"), ave_leg / qed_instantaneous, rtol=1e-12)
    assert np.isclose(ave_leg, 1.0 / (2.0 * ALPHA), rtol=1e-12)


def test_keep_both_legacy_branches_unmoved() -> None:
    """KEEP-BOTH: the pre-D7 branches return EXACTLY what they always returned.

    Neither is a superseded coefficient — each is the correct one-loop coefficient in
    its OWN footing per the e4 leaf's :38-41 decomposition chain. Pinning them stops a
    future 're-point' from quietly redefining a named branch in place (scoping shape
    (A), which the KEEP-BOTH pattern rules out).
    """
    assert np.isclose(arbiter(geometry="propagating"), 7.5 * np.pi / ALPHA**2, rtol=1e-12)
    assert np.isclose(arbiter(geometry="static"), 15.0 * np.pi / ALPHA**2, rtol=1e-12)


def test_carrier_average_and_geometry_factors_are_exact() -> None:
    """The two step factors of the decomposition chain, asserted as exact ratios.

    v2/v3 == 2 is the <cos^2>=1/2 carrier average the re-freeze removed — the e4 leaf's
    :106 states "v3 is exactly half v2". static/instantaneous == 4 is the head-on
    crossing-geometry factor (alpha/(30 pi) -> 2 alpha/(15 pi)).
    """
    v3 = arbiter(geometry="instantaneous")
    v2 = arbiter(geometry="propagating")
    static = arbiter(geometry="static")
    assert v2 / v3 == 2.0
    assert static / v3 == 4.0
    assert static / v2 == 2.0


def test_field_independence() -> None:
    """The arbiter takes no field argument at all — field-independence is structural.

    Both legs are E^2-leading, so the ratio is constant in E by construction. This
    pins that the signature stays field-free (a field-dependent ratio would mean one
    leg's power had drifted).
    """
    with pytest.raises(TypeError):
        arbiter(1e14)  # type: ignore[call-arg]


def test_unknown_geometry_raises_and_names_the_options() -> None:
    """A typo'd footing must fail loudly, and the message must name all three branches."""
    with pytest.raises(ValueError) as exc:
        arbiter(geometry="propogating")  # deliberate misspelling
    msg = str(exc.value)
    for expected in ("instantaneous", "propagating", "static"):
        assert expected in msg


def test_matches_the_kb_box_to_stated_precision() -> None:
    """Loose sanity rail: the KB box quotes ~2.2e5; v2 ~4.42e5; static ~8.85e5."""
    assert np.isclose(arbiter(), 2.2123e5, rtol=2e-4)
    assert np.isclose(arbiter(geometry="propagating"), 4.4247e5, rtol=2e-4)
    assert np.isclose(arbiter(geometry="static"), 8.8493e5, rtol=2e-4)
