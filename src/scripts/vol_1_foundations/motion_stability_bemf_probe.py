"""motion_stability_bemf_probe.py — does MOTION stabilize a self-trap via its back-EMF?

GREEN-FIELD / CONTRADICTS-DEFAULT hypothesis (Grant 2026-06-04): topological
stability FROM motion. A STATIC self-trap decays; a MOVING one is held together
by its own back-reaction — the dark wake tau_zx (the mutual-inductance / back-EMF
the moving trap drags behind it). Differential prediction:

    retention(v) - retention(0) > 0, MONOTONIC in v, stability-gain TRACKS tau_zx.

The canonical corpus default CONTRADICTS this:
  - electron stability is the STATIC saturation knot (resonant-lc-solitons.md):
    confinement = static-twist dielectric saturation Gamma->-1, motion irrelevant.
  - a moving (2,3) "requires SUSTAINED EXTERNAL DRIVE"
    (_archive/L5/axiom_derivation_status.md:178) — motion is a COST, not a free
    stabilizer.
So the default predicts retention(v) FLAT/NEGATIVE; Grant predicts POSITIVE.
Both pre-registered as clean outcomes (prereg §4). EMERGENCE test.

ENGINE + BASE: fdtd_3d.py (Maxwell + Axiom-4 saturation) + the validated
Option-C transverse-photon self-trap (two counter-prop focused CP pulses;
retention 0.580 vs 0.389 matched baseline, 2026-06-04 full-electron result).

BOOST to velocity v (substrate-native-check CP8 — momentum operator on the
GENERATIVE PRECURSOR, NOT a planted moving end-state): break the counter-prop
amplitude symmetry — pulse A (+x) x(1+delta), pulse B (-x) x(1-delta). Net
Poynting flux ~ +delta drifts the trap at net group velocity v. delta=0 = the
validated zero-momentum self-trap. v is MEASURED (centroid drift), NOT tuned to
a target (ave-driver-script-honesty).

tau_zx (the back-EMF) on fdtd_3d.py (canonical DarkWakeObserver formula projected
to the E/H sector; FDTD bridge 2026-05-31_FT-darkwake-crossscale_result.md:117):
    tau_zx(r) = Z_0 * S(A(r)) * d_x[ |E(r)|^2 * dx^2 / V_SNAP^2 ]
the longitudinal energy-gradient back-reaction (the engine's ponderomotive
x-component, re-scaled). We report max|tau_zx| and the BACKWARD (trailing) wake.

ARMS (prereg §2), v in {0, ~0.2c, ~0.4c}:
  SELF-TRAP(v)  the validated self-trap, boosted. THE hypothesis arm.
  LINEAR(v)     sub-saturation pulse (no self-trap), same v. AVE-distinct
                discriminator: a linear pulse disperses regardless of v, so its
                retention should NOT rise with v. (ave-discrimination-check)
  BASELINE(v)   peak-|E|-matched phase-scramble (matched saturation depth; AVOIDS
                the (ii) global-norm A=1-clamped confound), same v.

A-INSTRUMENTATION (ii-audit lesson 1): peak_A = max|E|*dx/V_SNAP tracked EVERY
probe step for every arm; Op14 bar A>sqrt(2a); full saturation A->1 (Gamma->-1).
Gate: confirm SELF-TRAP STAYS saturated WHILE moving — else the claim FAILS.

PML-ADVECTION CONFOUND (prereg §1d): a moving trap drifts toward the +x PML and
loses energy to absorption -> false NEGATIVE. Controlled by (1) windowing so the
fastest arm stays interior + tracking centroid; (2) peak_A is PML-independent
(if A stays high while moving, the trap is intact regardless of position);
(3) LINEAR feels the SAME PML at the SAME v -> the DIFFERENTIAL is PML-robust.

Discipline: substrate-native-check CP8, consistency-vs-emergence (EMERGENCE),
ave-discrimination-check (LINEAR=SM-counterfactual), ave-canonical-source
(verify_constants), ave-driver-script-honesty (forward-predict sign §4; no fit),
ave-evidence-framing-discipline. Pure-AVE-corpus.

PREREG: _orchestration/motion-stability-bemf.md (frozen).

Run:
    PYTHONPATH=src python3 src/scripts/vol_1_foundations/motion_stability_bemf_probe.py
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

# -- ave-canonical-source: import constants; NO hardcoded physics literals -------
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

OUTPUT_JSON = Path(__file__).parent / "motion_stability_bemf_probe_results.json"

# Run config (matches the validated r10 self-trap operating point)
N_LATTICE = 48
DX = 0.01
PML = 6
N_SETTLE = 80   # steps to let the two packets collide + self-trap before locking core
N_RECORD = 180  # recording-window steps (kept short enough to keep fast arm interior)
PROBE_EVERY = 4

# Validated deep-saturation operating point (r10: 0.7*V_SNAP/dx -> peak A ~ 0.77)
AMP_FRAC_VSNAP_SELFTRAP = 0.7
# Sub-saturation LINEAR amplitude: peak A ~ amp*dx/V_SNAP well below R_I=sqrt(2a)=0.121
AMP_FRAC_VSNAP_LINEAR = 0.05   # peak A ~ 0.05*... << 0.121 -> S(A)~1, no self-trap

# Velocity sweep via counter-prop amplitude asymmetry delta (prereg §1a).
# delta=0 -> v=0 (validated self-trap); larger delta -> larger net group velocity.
DELTA_SWEEP = (0.0, 0.30, 0.55)  # measured centroid-drift v reported, NOT imposed


# ==============================================================================
# SECTION 1 — boosted transverse-photon seed (momentum operator on the precursor)
# ==============================================================================
# placeholder — filled in §1 commit


# ==============================================================================
# SECTION 2 — tau_zx (back-EMF) observable + retention/saturation diagnostics
# ==============================================================================
# placeholder — filled in §2 commit


# ==============================================================================
# SECTION 3 — run one arm; v-sweep driver; adjudication
# ==============================================================================
# placeholder — filled in §3 commit


def verify_constants() -> None:
    """ave-driver-script-honesty (a): cross-check canonical imports before any verdict."""
    assert abs(ALPHA_COLD_INV - (4.0 * np.pi**3 + np.pi**2 + np.pi)) < 1e-9, "ALPHA_COLD_INV drift"
    assert abs(R_I - np.sqrt(2.0 * ALPHA)) < 1e-12, "R_I != sqrt(2*alpha)"
    assert V_YIELD < V_SNAP, "V_YIELD must be < V_SNAP"
    assert abs(V_YIELD - np.sqrt(ALPHA) * V_SNAP) < 1.0, "V_YIELD != sqrt(alpha)*V_SNAP"
    assert 0.0 < EPS_SAT_RATIO < 1e-6, "EPS_SAT_RATIO out of range"
    assert abs(Z_0 - 376.730) < 0.01, "Z_0 drift"


if __name__ == "__main__":
    verify_constants()
    print("skeleton OK — constants verified")
