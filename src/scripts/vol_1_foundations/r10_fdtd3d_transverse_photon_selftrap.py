"""r10_fdtd3d_transverse_photon_selftrap.py — Option C: transverse-photon self-trap.

PRIMARY (Option C, brief §0 REDIRECT): seed a STRUCTURED TRANSVERSE PHOTON (two
counter-propagating focused circularly-polarized transverse pulses, E⊥B⊥k,
multi-node), drive the constructive-interference point past V_yield toward
V_snap, and watch for an AUTONOMOUS self-trap into a bound electron. This is the
canonical pair-production ORIGIN (pair-production-axiom-derivation.md §2 seven
steps: c_local->0 closes the longitudinal channel, blocked KE shatters sideways
into the transverse curl). We seed the ORIGIN (the transverse photon), NOT the
END-state (the compressed knot) — the phase3f end-state seed dispersed because
it omitted the transverse structure that defines + stabilizes the knot.

HEADLINE (emerge-vs-impose): does the (2,3)-signature EMERGE from the transverse
self-trap, or must it be IMPOSED (Option-D nucleation rule)?

LOAD-BEARING SCOPE (prereg §1, surfaced to Grant): fdtd_3d.py carries ONLY six
real-space Yee fields (Ex..Hz). It has NO Cosserat microrotation sector and NO
native V_inc/V_ref ports. Per 06_winding_index_projection.md §4 the poloidal "3"
of the (2,3) is the SU(2) U(1)-fibre phase — the information LOST projecting to
the E-field — so the "3" has no Maxwell-field carrier here. This driver tests
what the continuum engine CAN host: the transverse self-trap, the toroidal "2"
(E-polarization winding), and the (V_inc,V_ref)=(E±Z_0·H) phasor limit cycle
(aspect + chirality). Poloidal-"3" emergence is OUT OF SCOPE for this engine and
reported as a fork verdict, NOT forced.

PREREG: research/2026-06-04_full-electron-transverse-selftrap-result.md (frozen).

Arms:
  C-EMERGE   (primary, emergence-class): transverse photon, NO (2,3) imposed.
  C-NUCLEATE (control, consistency):     transverse photon + Option-D chirality.
  A-CONTROL  (control, the demoted seed): single-bond planted-(2,3) phasor seed.
  BASELINE   (matched, phase3f Factor-2 fix): phase-scrambled, amplitude-matched,
             topologically-trivial — NOT random-direction.

Discipline applied: ave-prereg, substrate-native-check, phase-space-coordinate-
check, ave-canonical-source, ave-canonical-leaf-pull, ave-driver-script-honesty
(emergence arm imposes nothing), consistency-vs-emergence, ave-fundamental-
ground-up-implementation (matched baseline; substrate-derived PASS bars),
ave-evidence-framing-discipline, ave-ee-first-mapping, ave-infinity-discipline
(S_min floor / NaN guard), pre-test-physics-check (the §1 finding).

Run:
    PYTHONPATH=src python3 src/scripts/vol_1_foundations/r10_fdtd3d_transverse_photon_selftrap.py
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

# ── ave-canonical-source: import constants; NO hardcoded physics literals ──────
from ave.core.constants import (
    ALPHA,
    ALPHA_COLD_INV,
    EPS_SAT_RATIO,
    PHI,
    R_I,
    V_SNAP,
    V_YIELD,
    Z_0,
)
from ave.core.fdtd_3d import FDTD3DEngine

# Derived dimensionless targets (substrate-derived PASS bars, prereg §6.1)
PHI_SQ = PHI * PHI  # ≈ 2.618 — Golden-Torus phasor aspect (P5 diagnostic)
A2_OP14 = R_I**2  # = 2α ≈ 0.0146 onset (R_I = √(2α)); P3 saturation-engagement bar
# NOTE on P3: R_I = √(2α) is the Regime-I→II strain-ratio boundary in A²-units
# where A = V/V_snap. The Op14 engagement A² bar is R_I² = 2α.

OUTPUT_JSON = Path(__file__).parent / "r10_fdtd3d_transverse_photon_selftrap_results.json"


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 1 — transverse-photon seed construction (C-EMERGE)            [stub]
# ══════════════════════════════════════════════════════════════════════════════
# Built in commit 2.


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 2 — matched baseline + A-CONTROL + C-NUCLEATE seeds            [stub]
# ══════════════════════════════════════════════════════════════════════════════
# Built in commit 3.


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 3 — phasor observable: (V_inc,V_ref)=(E±Z_0·H), aspect+chirality [stub]
# ══════════════════════════════════════════════════════════════════════════════
# Built in commit 4.


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 4 — run-and-probe + adjudication                               [stub]
# ══════════════════════════════════════════════════════════════════════════════
# Built in commit 5.


def verify_constants() -> None:
    """ave-driver-script-honesty (a): cross-check canonical imports before any verdict."""
    assert abs(ALPHA_COLD_INV - (4.0 * np.pi**3 + np.pi**2 + np.pi)) < 1e-9, "ALPHA_COLD_INV drift"
    assert abs(PHI_SQ - 2.6180339887) < 1e-6, "PHI_SQ drift"
    assert V_YIELD < V_SNAP, "V_YIELD must be < V_SNAP"
    assert abs(V_YIELD - np.sqrt(ALPHA) * V_SNAP) < 1.0, "V_YIELD ≠ √α·V_SNAP"
    assert 0.0 < EPS_SAT_RATIO < 1e-6, "EPS_SAT_RATIO out of range"
    assert abs(A2_OP14 - 2.0 * ALPHA) < 1e-9, "A2_OP14 ≠ 2α"


def main() -> dict:
    print("=" * 78, flush=True)
    print("  r10 — Transverse-photon self-trap on fdtd_3d.py (Option C primary)")
    print("  Brief: _orchestration/2026-06-04_full-electron-binding-reseed-probe.md §0")
    print("=" * 78, flush=True)
    verify_constants()
    print(f"  Canonical: V_YIELD={V_YIELD:.3e} V, V_SNAP={V_SNAP:.3e} V, Z_0={Z_0:.2f} Ω")
    print(f"  PASS bars: α⁻¹={ALPHA_COLD_INV:.4f}, φ²={PHI_SQ:.4f}, A²_Op14=2α={A2_OP14:.4f}")
    print("  SCOPE (prereg §1): fdtd_3d.py carries E/H only — toroidal-2 + phasor")
    print("    limit-cycle testable; poloidal-3 OUT OF SCOPE (Cosserat absent).")
    print("\n  [skeleton — seeds + observables + adjudication built in commits 2-5]")
    return {"status": "skeleton", "prereg": "research/2026-06-04_full-electron-transverse-selftrap-result.md"}


if __name__ == "__main__":
    main()
