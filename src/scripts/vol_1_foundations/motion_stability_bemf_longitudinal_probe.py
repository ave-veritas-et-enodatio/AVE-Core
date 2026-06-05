"""
Motion-stability via back-EMF — the LONGITUDINAL (decisive) channel.

Grant's hypothesis (stability FROM motion): a moving self-trap's back-EMF /
dark-wake reaction STABILIZES it — retention(v) slope > 0, stability gain tracking
the native longitudinal τ_zx (positive), MORE than a linear (SM-counterfactual)
control at matched amplitude/saturation.

WHY LONGITUDINAL IS DECISIVE (the prior runs were on the WRONG channel):
  Both transverse runs (Maxwell 059ae318 NULL-lean-CONTRADICTS; native-Cosserat
  c6613c26 CONTRADICTS-via-PIN) boosted the V-SECTOR winding phasor (ox,oy)=
  (V0+V1, V2+V3). But:
    1. The electron moves LONGITUDINALLY, not transversally —
       de-broglie-standing-wave.md:50: "its motion displaces the lattice,
       generating longitudinal acoustic pressure waves governed by the vacuum's
       Bulk Modulus."
    2. The dark-wake τ_zx IS a longitudinal shear strain (the bemf) —
       vacuum_engine.py:46, dark-wake-bemf-foc-synthesis.md §3.
  ∴ drive in the channel the electron moves (longitudinal displacement u) + read
  the channel the bemf lives in (native longitudinal τ_zx). THIS is the coherent
  adjudication.

THE ONLY CHANGE vs the validated Cosserat run (c6613c26): swap the transverse
phasor boost on V_inc for a LONGITUDINAL displacement-field (u) drive on the
bulk-modulus compression channel. Everything else (durable Arm-C host, native
DarkWakeObserver, LINEAR/BASELINE arms, adjudicator) is reused.

THE LONGITUDINAL DRIVE (substrate map):
  The displacement DOF is the Cosserat u field (cosserat_field_3d.py:817), velocity
  u_dot, velocity-Verlet integrated. The bulk/longitudinal channel runs at
  c_L = √((2G + 4G/3)/ρ) = √(10/3) ≈ 1.826 (cosserat_field_3d.py:1500) — separate
  from and faster than the transverse c_T = √(G/ρ) = 1, and NOT frozen by the
  V-sector saturation S (c_L depends on G/ρ, not S). The drive imparts NET +x
  longitudinal momentum by writing a +x displacement-velocity blob onto
  u_dot[...,0] (Variant A) localized on the host: the lattice moves +x (net
  momentum) with an x-varying envelope ⇒ ∂_x u_x ≠ 0 ⇒ div u ≠ 0 ⇒ bulk
  compression excited. ONE-SHOT momentum imprint (a sustained pump injects energy —
  rejected, same as the Cosserat run).

COUPLING (honest, load-bearing): with disable_cosserat_lc_force=True (validated
  config), the K4→Cosserat FORCE channel is OFF. The path is u-strain → ε_sym →
  A²_ε → S_ε → z_local = √(S_μ/S_ε) (k4_cosserat_coupling.py:393), which both
  modulates the K4 scatter (asymmetric impedance) AND is the prefactor of
  τ_zx = z_local·∂_x A². A longitudinal u-momentum biases the saturation-impedance
  field along +x; if the knot tracks that bias it translates (and the native τ_zx
  carries it). If it does NOT (z_local bias too weak to move a c_eff→0 frozen core)
  → a clean PIN-EVEN-LONGITUDINAL finding (a tension with de-broglie:50).

ANTI-STALL (hard 2-try cap): validate the drive on a sub-saturation LINEAR
  displacement pulse FIRST. Moves (v>0, sign-symmetric) → proceed. Does NOT move
  after 2 drive variants → BLOCKED-drive, return.

FORWARD-PREDICTED SIGN (pre-run, no fit — ave-driver-script-honesty):
  substrate-default = PIN-EVEN-LONGITUDINAL. The LINEAR pulse advects (~c_L); the
  SELF-TRAP knot's frozen V-core does NOT track the z_local bias enough to
  translate; retention(v) flat-or-falling; native-τ_zx-vs-stability corr ≤ 0.
  A SUPPORTS overturns the static-trap canon → FULL ave-discrimination-check.

Brief / prereg: _orchestration/motion-stability-bemf-longitudinal.md
Result:        research/2026-06-04_motion-stability-bemf-longitudinal-result.md
"""

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ave.core.constants import ALPHA  # noqa: E402
from ave.topological.vacuum_engine import (  # noqa: E402
    DarkWakeObserver,
    VacuumEngine3D,
)
from tlm_electron_soliton_eigenmode import (  # noqa: E402
    initialize_2_3_voltage_ansatz,
)

# ── Substrate-derived constants (ave-canonical-source: NO hardcoded literals) ──
A2_OP14 = float(np.sqrt(2.0 * ALPHA))   # √(2α) ≈ 0.1208 — Op14 engagement (self-trap bar)
PHI = (1.0 + np.sqrt(5.0)) / 2.0
DT = 1.0 / np.sqrt(2.0)                  # K4-TLM 4-port junction outer timestep
C_LONG = float(np.sqrt(10.0 / 3.0))     # bulk-modulus longitudinal sound speed (K=2G, ρ=G=1)

# Host (Arm-C) geometry — the confirmed durable host (retention ~0.88–0.91, peak A²≈8.9)
HOST_R_FRAC = 0.22                       # R_shell = 0.22·N
HOST_AMP = 0.40                          # peak A²_interior ≈ 8.9 during evolution

# FORWARD-PREDICTED SIGN (no fit). Substrate default: frozen V-core pins even
# longitudinally (the longitudinal channel moves the LINEAR pulse but not the knot).
FORWARD_PREDICTED_VERDICT = "PIN-even-longitudinal"
FORWARD_PREDICTED_SIGN = {
    "linear_moves": True,
    "knot_moves": False,
    "retention_slope_sign": "<= 0 (flat or falling)",
    "tau_zx_vs_stability_corr_sign": "<= 0",
}


# ══════════════════════════════════════════════════════════════════════════════
# Engine + host (confirmed config — reused verbatim from the Cosserat run c6613c26)
# ══════════════════════════════════════════════════════════════════════════════
def setup_engine(N, PML):
    """A28-corrected coupled VacuumEngine3D (doc 67 §15 + r10_v8 config).
    disable_cosserat_lc_force=True ⇒ K4→Cos FORCE off; coupling is via z_local
    (the saturation-impedance channel τ_zx reads)."""
    return VacuumEngine3D.from_args(
        N=N,
        pml=PML,
        temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )


def seed_host(engine, N, amplitude=HOST_AMP):
    """Plant the durable (2,3) host (Arm-C config): the confirmed self-trap that
    holds retention ~0.88–0.91 at peak A²≈8.9. R = 0.22·N, r = R/φ². Populates
    V_inc only; the Cosserat u field starts at zero (the drive lives there)."""
    R = HOST_R_FRAC * N
    r = R / (PHI**2)
    initialize_2_3_voltage_ansatz(engine.k4, R=R, r=r, amplitude=amplitude)
    return R, r


def _interior_mask(N, PML):
    m = np.zeros((N, N, N), dtype=bool)
    m[PML : N - PML, PML : N - PML, PML : N - PML] = True
    return m
