"""
Full-electron Option B — does a transverse wave SET the (2,3) on the DISCRETE engine?

Headline (Grant's hypothesis): on VacuumEngine3D (K4-TLM + Cosserat — the only
engine with the (2,3) carrier: native (V_inc, V_ref) ports + Cosserat ω + Op10),
seed the GENERATIVE PRECURSOR (a structured transverse photon: counter-propagating
opposite-handed CP focused pulses, multi-node, E⊥B⊥k — the Option-C precursor that
self-trapped), drive to saturation, and test whether the (2,3) winding EMERGES in
the (V_inc, V_ref) phasor sector as the trap forms — ZERO imposed.

Authoritative spec: _orchestration/2026-06-04_full-electron-option-B-discrete-emergence.md
Prereg + result:    research/2026-06-04_full-electron-option-B-discrete-emergence-result.md

Three arms (prereg §4):
  A — EMERGENCE: transverse photon, no (2,3) imposed. The headline.
  B — MATCHED BASELINE: same per-port |V_inc| stats, phase-scrambled (trivial topology).
  C — IMPOSED CONTROL: Arm A + PairNucleationGate (Option-D nucleation rule,
      pair-production-axiom-derivation.md:121). Establishes the (2,3) signature template.

PASS bars (prereg §4, substrate-derived):
  B1 self-trap:  A²_max > A²_op14 = √(2α)
  B2 localization beats baseline:  retention(A) > retention(B)
  B3 (2,3) phasor winding (HEADLINE):  (V_inc,V_ref) temporal winding c=3 OR (n₁,n₂)=(2,3)
       in Arm A, ABSENT in Arm B, MATCHES Arm C
  B4 reactance-pair consistency:  C-state(V_inc) ⟷ L-state(Phi_link) anti-correlation

Outcomes (brief §4):
  (i)   self-traps AND (2,3) emerges → Grant's hypothesis CONFIRMED
  (ii)  carries (2,3) carrier but does NOT self-trap → needs c_eff/Path-A (surface to Grant)
  (iii) self-traps but (2,3) only when IMPOSED → hypothesis REFUTED on the discrete engine

DISCIPLINE NOTES (load-bearing):
  - phase-space-coordinate-check (A47 v3): the engine's shipped Op10
    (cosserat.extract_crossing_count) reads REAL-SPACE Cosserat ω; the corpus
    (2,3) lives in (V_inc, V_ref) PHASOR (theory.md:16). HEADLINE = the phasor
    temporal-winding extractor below; the ω Op10 is reported as a FLAGGED-mismatch
    diagnostic. (flag-don't-fix; the shipped Op10 is NOT redefined.)
  - ave-driver-script-honesty: the transverse-photon source injects E⊥B⊥k ONLY;
    it injects NO (V_inc, V_ref) winding. Arm C imposes the Option-D boundary
    condition (PairNucleationGate) and is clearly labeled.
  - Rule 10: C-state (V_inc) AND L-state (Phi_link) recorded at the trap bond every
    step. PML excluded + density-peak trap-site selection.
"""

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.core.constants import ALPHA  # noqa: E402
from ave.topological.vacuum_engine import (  # noqa: E402
    PairNucleationGate,
    SpatialDipoleCPSource,
    VacuumEngine3D,
    _forward_t2_port_weights,
    amp_to_vsnap_units,
)

# ── Substrate-derived constants (ave-canonical-source: NO hardcoded literals) ──
V_YIELD = float(np.sqrt(ALPHA))           # √α ≈ 0.0854 V_SNAP — Op14 onset (theory.md:10)
A2_OP14 = float(np.sqrt(2.0 * ALPHA))     # √(2α) ≈ 0.1208 — Op14 engagement (B1 bar)
OMEGA_C = 1.0                             # ω_C natural units
COMPTON_PERIOD = 2.0 * np.pi
DT = 1.0 / np.sqrt(2.0)                   # K4-TLM 4-port junction timestep
PHI = (1.0 + np.sqrt(5.0)) / 2.0         # golden ratio (R_phase/r_phase = φ² diagnostic)


# ══════════════════════════════════════════════════════════════════════════════
# Source: counter-propagating-capable transverse-photon precursor
# ══════════════════════════════════════════════════════════════════════════════
# SpatialDipoleCPSource is forward-only (hardcodes +propagation_axis). For the
# counter-propagating precursor we need a −x pulse. _forward_t2_port_weights
# supports any direction (max(0, −d̂·p̂)), so a minimal subclass overriding the
# port-weight direction sign gives the backward pulse, reusing all the proven
# dipole-modulation + envelope machinery.
class _DirectionalCPSource(SpatialDipoleCPSource):
    """SpatialDipoleCPSource with an explicit propagation SIGN (±1) so a
    counter-propagating (−axis) opposite-handed pulse can be built."""
    # FILLED below


# ══════════════════════════════════════════════════════════════════════════════
# Engine + arm setup
# ══════════════════════════════════════════════════════════════════════════════
def setup_engine(N, PML):
    """A28-corrected coupled VacuumEngine3D (doc 67 §15 + r10_v8)."""
    raise NotImplementedError  # FILLED


def setup_transverse_photon(N, amplitude):
    """Arm A precursor: two counter-propagating opposite-handed CP pulses."""
    raise NotImplementedError  # FILLED


# ══════════════════════════════════════════════════════════════════════════════
# Observables
# ══════════════════════════════════════════════════════════════════════════════
def compute_a2_field(V_inc, V_SNAP):
    """A² = |V_inc|²/V_SNAP² (port-summed strain)."""
    raise NotImplementedError  # FILLED


def select_trap_bond(engine, PML):
    """Density-peak trap-site selection (top-K |V_inc|² interior, PML-excluded)."""
    raise NotImplementedError  # FILLED


def phasor_temporal_winding(v_inc_traj, v_ref_traj):
    """HEADLINE B3 observable: (V_inc, V_ref) temporal-winding extractor.

    Per theory.md:16 + 06_winding_index_projection §4 + the doc-26 §5.1 recipe.
    Returns (n1, n2, crossing_count_c, R_phase_over_r_phase)."""
    raise NotImplementedError  # FILLED


def omega_op10_diagnostic(engine):
    """FLAGGED-mismatch diagnostic (A47 v3): real-space Cosserat-ω Op10 +
    Hopf charge. Reported, NOT headline."""
    raise NotImplementedError  # FILLED


# ══════════════════════════════════════════════════════════════════════════════
# Single-arm run
# ══════════════════════════════════════════════════════════════════════════════
def run_arm(arm_name, N, PML, n_periods, amplitude, impose_nucleation):
    """Run one arm (A/B/C); return observables dict."""
    raise NotImplementedError  # FILLED


# ══════════════════════════════════════════════════════════════════════════════
# Adjudication + verdict
# ══════════════════════════════════════════════════════════════════════════════
def adjudicate(arm_A, arm_B, arm_C):
    """Apply B1-B4 PASS bars; return outcome (i/ii/iii)."""
    raise NotImplementedError  # FILLED


def main():
    raise NotImplementedError  # FILLED


if __name__ == "__main__":
    main()
