"""L0 (engine RE-ROUTE) — the α-CLEAN WINDING-HOST DE-RISK. HARD-STOP gate.

The first stage of the re-routed engine pathway and a HARD-STOP: the chord
program (S1→S4) decides chord-vs-echo via an α-FREE dimensionless ratio at S4,
which is only meaningful if the host carrying the (2,3) winding DOF is α-FREE.
The re-route audit found the natural winding host α-contaminated on the readout
path. This suite establishes the de-risked host is α-clean — or HARD-STOPs.

Epic:   `_orchestration/2026-06-24_engine-reroute-pathway.md` (Stage L0).
Prereg: `research/2026-06-24_engine-reroute-l0-alpha-clean-host_prereg.md` (FROZEN).
Host:   `_winding_host.py` (the α-stripped winding host + the ported guard triad).

ORIGIN — the re-route's winding DOF lives in `cosserat_field_3d.py`, which is
α-contaminated (ALPHA :56; KAPPA_CHIRAL_ELECTRON=α·κ̃ :131; the golden-torus
closed-form Q :2422 = 137.036304 at R·r=¼, the baked-137 echo). The original
Gate 0 (PR #394) HARD-STOPPED on exactly this host. Stage 0 then re-scoped onto
the cold CrystalEngine SPINE, NEVER importing the cosserat host. The re-route
NEEDS the winding (cosserat-resident), so L0 does for the WINDING DOF what
Stage 0 did for the bulk spine: import ONLY the α-FREE symbols + carry the guard.

════════════════════════════════════════════════════════════════════════════════
L0 FROZEN-BIN OUTCOMES (BRUTAL HONESTY — Rule 11)
════════════════════════════════════════════════════════════════════════════════
  L0.1  the IMPORT-GUARD TRIAD fires LIVE on the winding host:  PASS.
        ALPHA / KAPPA_CHIRAL_ELECTRON / kappa_chiral_from_topology /
        extract_quality_factor / Q_TANK / ELECTRON / RHO_BULK / V_SNAP /
        ALPHA_COLD_INV are NOT reachable in the winding-host globals. The import
        of `_winding_host` itself executes the load-time asserts; this test
        re-asserts at runtime AND witnesses that a deliberately-injected leak
        TRIPS the guard (the guard is LIVE, not vacuous).
  L0.2  the WINDING-DOF CHORD PATH is α-FREE:  PASS.
        It carries κ̃ = 6/5 (KAPPA_TILDE_ELECTRON), invokes NO α·κ̃, reaches NO
        137-echo Q-form. The α-baked KAPPA_CHIRAL_ELECTRON = α·κ̃ and the
        golden-torus closed-form Q are NOT importable as bound names here.
  L0.3  the LITERAL SCRUBBER + the LANDING-ZONE gate stay green:  PASS.
        No '137'/'0.00729' literal in the chord-path verdict-determining code;
        the chord-path winding factor κ̃=1.2 is NOT in the 117–157 α-leak band.

PASS  = the winding host's chord path is α-clean (κ̃=6/5, no 137-echo, no ALPHA),
        the guard fires live, the scrubber + landing-zone are green. The chord
        program (S1→S4) may proceed on this host.
HARD-STOP = ANY α re-leak: a live-injected ALPHA that does NOT trip the guard;
        the chord path reaching α·κ̃ / extract_quality_factor / ALPHA; a '137'/
        '0.00729' literal on the chord path; a chord-path numeric in 117–157.
        Report it — do NOT patch around a leak; the leak is the signal. Per
        Rule 11, a HARD-STOP is the discipline working at full strength.

CLASSIFICATION (consistency-vs-emergence): Class A — identity/foundation. The
guard asserts ARE the immune system (structural, not predictive). NO Class D
(emergence) claim; NO chord; NO α-readout. The Q=137 slot stays EMPTY (gate
wmighcz1z, anti-substitution).
"""

from __future__ import annotations

import pytest

# Importing `_winding_host` EXECUTES its load-time guard triad. If an α-carrier
# had leaked into the host's globals, THIS IMPORT would fail.
from . import _winding_host as W


# ─────────────────────────────────────────────────────────────────────────────
# L0.1 — the import-guard triad fires LIVE on the winding host.
# ─────────────────────────────────────────────────────────────────────────────
def test_L0_1_winding_host_guard_triad_fires_live():
    """PASS (pinned): no α-carrier is reachable in the winding-host globals, AND
    a deliberately-injected α-carrier DOES trip the guard (the guard is live,
    not vacuous)."""
    # (a) the host is clean at runtime (the load-time asserts already passed).
    W.assert_winding_host_globals_alpha_clean()
    print("\n--- L0.1 guard triad (import-time + runtime) on the α-stripped winding host ---")
    print("  ALPHA / KAPPA_CHIRAL_ELECTRON / kappa_chiral_from_topology /")
    print("  extract_quality_factor / Q_TANK / ELECTRON / RHO_BULK / V_SNAP /")
    print("  ALPHA_COLD_INV absent from the winding-host globals?  YES (load-time asserts passed).")

    # (b) the guard is LIVE: a deliberately-injected α-carrier trips it. We inject
    #     ALPHA directly into the host's module globals and confirm the runtime
    #     re-assert raises, then restore cleanliness.
    W.ALPHA = 7.2973525693e-3  # inject a leak into the host's globals
    try:
        with pytest.raises(AssertionError, match="α-leak|alpha-leak|ALPHA"):
            W.assert_winding_host_globals_alpha_clean()
        print("  guard is LIVE: a deliberately-injected ALPHA into the winding host TRIPS the assert. ✓")
    finally:
        del W.ALPHA  # restore cleanliness (do not leave the leak in the live module)
    # confirm cleanliness is restored
    W.assert_winding_host_globals_alpha_clean()


# ─────────────────────────────────────────────────────────────────────────────
# L0.2 — the winding-DOF chord path is α-FREE (κ̃=6/5, no α·κ̃, no 137-Q form).
# ─────────────────────────────────────────────────────────────────────────────
def test_L0_2_winding_chord_path_is_alpha_free():
    """PASS (pinned): the chord-path winding factor is κ̃ = 6/5 (α-FREE), NOT
    α·κ̃; the α-baked KAPPA_CHIRAL_ELECTRON and the golden-torus closed-form Q
    are NOT bound names in the host."""
    kappa = W.winding_kappa_tilde(2, 3)
    print("\n--- L0.2 the winding-DOF chord path is α-FREE ---")
    print(f"  winding κ̃(2,3) = {kappa}  (= 6/5 = {6 / 5}; the α-FREE form, NOT α·κ̃ ≈ 8.757e-3)")

    # the chord path uses the α-FREE κ̃ = 6/5 exactly.
    assert kappa == pytest.approx(6.0 / 5.0), (
        f"L0.2 HARD-STOP: the chord-path winding factor κ̃={kappa} is NOT 6/5 — "
        f"the α-baked α·κ̃ ≈ 8.757e-3 must NOT be on the chord path."
    )
    # κ̃ must be O(1), NOT the α-suppressed α·κ̃ (≈ 8.757e-3).
    assert kappa > 1.0, (
        f"L0.2 HARD-STOP: κ̃={kappa} is α-suppressed (≈ α·κ̃) — the chord path "
        f"must use the O(1) α-FREE factor, not the α-multiply."
    )

    # the α-baked carriers are NOT bound names in the host (cannot be reached on
    # the chord path).
    for forbidden in (
        "ALPHA",
        "KAPPA_CHIRAL_ELECTRON",
        "kappa_chiral_from_topology",
        "extract_quality_factor",
    ):
        assert not hasattr(W, forbidden), (
            f"L0.2 HARD-STOP: '{forbidden}' is a bound name in the winding host — "
            f"the α-baked carrier / the 137-echo Q-form must NOT be reachable on the chord path."
        )
    print("  α·κ̃ (KAPPA_CHIRAL_ELECTRON), kappa_chiral_from_topology, extract_quality_factor")
    print("  reachable on the chord path?  NO ✓  (the chord path is α-free by selective import)")


# ─────────────────────────────────────────────────────────────────────────────
# L0.3 — the literal scrubber + the landing-zone gate stay green.
# ─────────────────────────────────────────────────────────────────────────────
def test_L0_3_literal_scrubber_and_landing_zone_green():
    """PASS (pinned): (a) no '137'/'0.00729' literal in the chord-path
    verdict-determining code; (b) the chord-path winding factor κ̃=1.2 is NOT in
    the 117–157 α-leak band (1/α ≈ 137.036 lives there)."""
    # (a) literal scrubber: the chord-path numerical functions carry no α-numeral.
    W.assert_no_alpha_literal_in_chord_path()
    print("\n--- L0.3 literal scrubber + landing-zone gate ---")
    print("  no '137'/'0.00729' literal in the chord-path verdict-determining code?  YES ✓")

    # (b) landing-zone: the chord-path winding factor is far below the band.
    kappa = W.winding_kappa_tilde(2, 3)
    W.assert_not_in_landing_zone(kappa, "winding κ̃")
    print(f"  chord-path κ̃ = {kappa} in the 117–157 α-leak band?  NO ✓")
    print("  (the Q=137 slot stays EMPTY — gate wmighcz1z, anti-substitution; the α-free")
    print("   chord path does NOT reproduce α⁻¹.)")

    assert not (117.0 < float(kappa) < 157.0), (
        f"L0.3 HARD-STOP: chord-path κ̃={kappa} landed in the 117–157 α-leak band."
    )
