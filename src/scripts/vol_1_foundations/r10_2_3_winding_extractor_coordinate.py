"""
Coordinate-correct (2,3)-winding extractor + VALIDATION GATE.

Prereg (FROZEN): research/2026-06-05_2-3-winding-extractor-coordinate-prereg.md
Brief:           _orchestration/2026-06-05_2-3-winding-extractor.md
Resolves the prior run's auditor #1 (BLOCKING): the (2,3)-winding extractor was
UNVALIDATED — the shipped `phasor_temporal_winding`
(r10_vacuumengine3d_transverse_2_3_emergence.py) read `(8,0)/c=16` on the
Arm-C KNOWN-IMPOSED (2,3) bond. An extractor that cannot see a known-imposed
(2,3) cannot certify its absence.

KEEP-BOTH (audit-trail continuity): this is a NEW module. The shipped
`phasor_temporal_winding` is NOT redefined.

────────────────────────────────────────────────────────────────────────────
THE COORDINATE DIAGNOSIS (phase-space-coordinate-check — THE load-bearing skill)
────────────────────────────────────────────────────────────────────────────
The (2,3) is a PAIR of DISTINCT windings on the Clifford torus
(06_winding_index_projection.md §3-4):

  • Axis "2" (BASE): winding of the field-DIRECTION n̂ — the S² polarization /
    E-field direction unit vector that SURVIVES the Hopf fibration. NOT a port
    phasor angle.
  • Axis "3" (FIBRE): the U(1) internal phase — the C↔L / LC-slosh phase, built
    from the C-state `V_inc` vs the L-state `Phi_link`. The information LOST in
    the Hopf projection (§4); the axis the prior extractor IGNORED
    (`phi_traj` was an unused optional arg).

The prior extractor set θ₁ = port-1 (V_inc,V_ref) phasor angle, θ₂ = port-2
phasor angle. A port's (V_inc,V_ref) phasor angle IS that port's C↔L angle
(transmission-line identity: (V_inc,V_ref) is a 45° rotation of (V, Z₀I) =
(C-state, L-state)). Two ports of one bond ring at the SAME LC frequency →
ratio structurally ~1:1, never (2,3). Wrong axes: it lived in (C↔L, C↔L).

THE ANSATZ IS SPATIAL. `initialize_2_3_voltage_ansatz` plants
`theta_wind = 2φ + 3ψ` where φ = toroidal (major-circle) angle and
ψ = poloidal (minor-circle) angle ON A TOROIDAL SHELL. At any single fixed
bond, φ and ψ are constants → `theta_wind` is a constant → a single-bond TIME
series carries NO 2φ+3ψ winding (only the temporal LC slosh). The (2,3) is a
SPATIAL standing pattern; it must be read by WALKING THE SHELL, not by watching
one bond oscillate in time. This is why the capture npz (single-bond time
series only) cannot host V0 — and why this extractor reads the FULL FIELD.

────────────────────────────────────────────────────────────────────────────
WHAT THIS EXTRACTOR READS (the fix)
────────────────────────────────────────────────────────────────────────────
On the converged FULL field of the Arm-C bound state:

  • Axis "2" (base): walk the major circle φ at the shell's tube; at each site
    reconstruct n̂ = Σ_p V_inc[p]·p̂ / |·| (port-weighted tetrahedral direction =
    the polarization/E-field direction); project into the local toroidal tangent
    frame and unwrap the azimuth → w₁. Expect 2.
  • Axis "3" (fibre): walk the minor circle ψ; at each site form a PORT-COHERENT
    fibre phase α = arctan2(Φ_link·ŵ, V_inc·ŵ) (C-state V_inc vs L-state
    Φ_link, coherent knot-tangent port projection ŵ — NOT per-site argmax,
    which scrambles the structure); unwrap → w₂. Expect 3.
  • Native invariant c: planar self-crossing count of the closed curve in the
    correct (base-azimuth, fibre-phase) plane along the (2,3) curve. Electron
    c = 3.

V0 (BLOCKING anti-fit gate): on Arm C this must recover c=3 (±0) OR (w₁,w₂)=
(2,3), where the legacy read `(8,0)/c=16`. This is a forward READ of a KNOWN
signal — no optimizer is run onto (2,3) (ave-driver-script-honesty).
"""

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.core.constants import ALPHA  # noqa: E402

# ── Substrate-derived constants (ave-canonical-source: NO hardcoded literals) ──
PHI = (1.0 + np.sqrt(5.0)) / 2.0          # golden ratio (R/r torus aspect)
A2_OP14 = float(np.sqrt(2.0 * ALPHA))     # √(2α) — Op14 engagement
DT = 1.0 / np.sqrt(2.0)                    # K4-TLM 4-port junction timestep
COMPTON_PERIOD = 2.0 * np.pi

# K4 tetrahedral A-site port directions (A→B bond vectors); the n̂ field
# direction is the V_inc-weighted sum of these (tlm_…_eigenmode.py:99-104).
PORT_DIRS = np.array([
    [+1.0, +1.0, +1.0],
    [+1.0, -1.0, -1.0],
    [-1.0, +1.0, -1.0],
    [-1.0, -1.0, +1.0],
]) / np.sqrt(3.0)


# ══════════════════════════════════════════════════════════════════════════════
# (filled incrementally below: field-direction n̂, fibre-phase, shell geometry,
#  the two-axis extractor, the crossing count, V0 driver)
# ══════════════════════════════════════════════════════════════════════════════
