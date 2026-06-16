"""
PRODUCTION DRIVER — passive winding-protected electron eigenmode (the keystone).

Prereg (FROZEN, every §): research/2026-06-15_passive-eigenmode_prereg_FROZEN.md
Lane brief:               _orchestration/2026-06-15_passive-eigenmode-solve.md
Build-step-zero (PASSED): src/scripts/vol_1_foundations/g0_double_count_smoke.py (G0)

THE QUESTION (prereg §1):
    Does the fully-coupled hybrid (V != 0  AND  omega != 0) wave-eigenmode of a substrate
    Gamma=-1 saturation cavity exist as a STABLE, dissipationless STANDING / BREATHER mode —
    with the conserved (2,3) winding imposed as a topological boundary condition on the
    independent Cosserat-omega carrier — and what is its radiative Q?

HEADLINE (Grant 2026-06-15 — do not drift):
    The result is EXISTENCE + STABILITY of the winding-protected hybrid breather (the FORM —
    the structural keystone). Q is the ECHO; report it, but the headline is NOT "we measured Q."

PLATFORM (b', Grant-granted eyes-open): the FIRST substrate-complete cross-firewall engine.
    crystal_engine V-tank breathing wall  (A1, the sech self-focus; TRUE n=sqrt(S) via
    c_eff^2 = c0^2/S, crystal_engine.py:197-200)   coupled to   the Cosserat-omega carrier
    (the (2,3) winding)  via the G0 Op14 coupling (trilinear_buckle_forces, KAPPA_TILDE=6/5,
    alpha-FREE).  REUSE both validated engines + the G0 coupling. NO new engine, NO *_vN file.

SEEDER (Grant 2026-06-15): the TRAVELING-(2,3) (planted_winding_field mode="traveling", the
    G4-certified carrier), NOT initialize_electron_2_3_sector (z-flat rotor, fails G4
    structurally w_tor=0). The production seed ALSO ASSERTS the real-space envelope is the
    0_1 UNKNOT (a single genus-1 torus shell), so the winding read is backed by
    "on the unknot = electron" (theory.md:16; ch8-alpha-golden-torus.md:29) — NOT a heavier
    real-space knot that merely also reads a winding (Grant's third-time wrong-object guard).

================================================================================================
SUBSTRATE-NATIVE WALK (substrate-native-check v1.2; done BEFORE this code per Operating-Principle 1)
================================================================================================
  CP1 (substrate dynamics)  : the V-tank is the validated scalar Master-Equation FDTD
                              (c_eff^2 = c0^2/S, leapfrog) — NOT a Helmholtz / energy-basin
                              eigensolve. The omega-carrier is the velocity-Verlet Cosserat
                              field. Both are time-domain wave engines; the "eigenmode" is read
                              as a CYCLIC / time-averaged breather (prereg §4), NOT a static
                              algebraic eigenvector.
  CP6 (reactance pair)      : every read records BOTH the C-state (V; omega) AND the L-state
                              (dV/dt; omega_dot) over the recording window. The extractor reads
                              the (omega, omega_dot) reactance pair. The V-tank breather is read
                              via (V, dV/dt) and the Gamma_true cycle.
  CP8 (generative precursor): we IMPOSE the winding as a topological BC (prereg charter, §7.1) —
                              this is the imposed-BC framing, NOT plant-the-finished-composite.
                              The V-tank is seeded with its OWN generative precursor (the sech
                              eigen-profile that self-focuses); the winding rides the independent
                              omega-carrier. The pure-V trap (omega=0) is cleared by the imposed
                              odd-omega winding (prereg §3 / hazard 3).
  CP9 (dynamical not algebraic): every F-read comes from the engines' OWN step() evolution
                              (V_inc/V integrated; omega field integrated) — NOT an algebraic
                              observer formula. Gamma_true, the winding, the stability eig, and
                              Q are all read off the dynamically-evolved state.
  CP10 (Gamma as boundary)  : the Gamma=-1 wall is rendered as crystal_engine's intrinsic
                              c_eff^2 = c0^2/S boundary (a self-induced impedance front), and the
                              coupling fires ONLY on the saturation-FRONT window g_wall =
                              _front_window() (a thin A~R_II shell) — NOT a bulk energy/force
                              term (which detonates, hazard 5).

PHASE-SPACE DISCIPLINE (phase-space-coordinate-check, A46): the winding is read on the
    omega-tank PHASOR (extract_2_3_omega_fast traces arg(Z) toroidally/poloidally on the
    (omega, omega_dot) LC pair), NEVER a real-space lattice-Cartesian winding count, and NEVER
    the A1 (V_inc, V_ref) phasor (the genesis-24 double-count — G0-clean, preserved here).

CONSERVED-NOT-PUMPED (ave-conserved-vs-pumped): F5 — the breather must stand with NO drive.
    The coupling is the conserved trilinear buckle (energize-LOCK, f_w==0). No gain term, no
    autoresonant pump. A drive-sustained state is a NEGATIVE.

HAZARDS PRECLUDED IN CODE (prereg §8, locked) — verified, not merely listed:
  1. NO gradient-flow stationary-point. We do NOT call relax_to_ground_state / relax_s11 /
     find_eigenstate with an energy/S11 f_fn. F1 = a time-domain breather convergence read.
  2. NO winding into (V_inc, V_ref). The winding rides eng_w.omega only; the coupling back-
     reaction f_omega lands on eng_w.omega; G0 already proved V_ref-leak <= 4.3e-16.
  3. NO pure-V seed. The (2,3) winding-BC is imposed on the omega-carrier (supplies odd omega).
  5. Gamma=-1 is the c_eff boundary + the front-window coupling (CP10), NOT a bulk term.
  9. TRUE n=sqrt(S): Gamma_true = (n-1)/(n+1) with n = c0/c_eff = sqrt(S) computed HERE; we do
     NOT call gamma_bulk()/refractive_index() (the S^{1/4} PROXY, crystal_engine.py:421-432).
 10. EXISTENCE/STABILITY read on the CYCLIC / time-averaged breather, never an instantaneous
     static Gamma.

CANONICAL-SOURCE (ave-canonical-source): all constants imported from ave.core.constants /
    ave.core.cross_sector_coupling. NOTE: there is no verify_constants function in this corpus;
    the constants are cross-checked by DIRECT IMPORT + identity assertions (see _verify_constants
    below) — 1/ALPHA == 137.036, ALPHA*1.2 -> Q=114.20, KAPPA_TILDE == 6/5.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field

import numpy as np

from ave.core.constants import ALPHA
from ave.core.cross_sector_coupling import KAPPA_TILDE, trilinear_buckle_forces
from ave.core.crystal_engine import CrystalEngine
from ave.topological.cosserat_field_3d import CosseratField3D
from ave.utils.fast_winding_extractor import (
    extract_2_3_omega_fast,
    planted_winding_field,
)

# ─────────────────────────────────────────────────────────────────────────────
# Coupling-binding declaration (prereg §6, the echo/chord verdict hinges on this):
#   the driver imports KAPPA_TILDE (= 6/5, the (2,3) topological factor pq/(p+q)) — ALPHA-FREE.
#   ALPHA is imported ONLY to (a) cross-check the canonical Q targets and (b) DECLARE that it is
#   NOT a coupling input. So a measured Q is CHORD-eligible on the coupling side; but per prereg
#   §6 the chord still will NOT fire (Lane-1 Path C open) -> the Q is reported ECHO-tagged.
# ─────────────────────────────────────────────────────────────────────────────
COUPLING_IS_ALPHA_FREE = True  # KAPPA_TILDE=6/5; ALPHA not a coupling input. See §6 declaration.

# F3 Q-bin targets (prereg §5 F3) — these are CHARACTERIZATION targets, NOT bin-deciding (§4).
Q_TARGET_BARE_ALPHA = 1.0 / ALPHA       # ~ 137.036  (LC-tank reactive leak, theorem-3-1-q-factor.md:83)
Q_TARGET_KAPPA_CHIRAL = 1.0 / (ALPHA * 1.2)  # ~ 114.20  (kappa_chiral = alpha*kappa_tilde)
Q_BIN_BAND = 0.05                        # +-5% band (prereg §5 F3)


# ============================================================================
# section: constants cross-check (ave-canonical-source; no verify_constants fn)
# ============================================================================
def _verify_constants() -> dict:
    """Cross-check the canonical constants by direct-import identity assertions
    (there is NO verify_constants function in this corpus — ave-canonical-source
    is satisfied by importing from ave.core.constants and asserting the identities
    the prereg §5/§6 commits to)."""
    checks = {
        "1/ALPHA == 137.036 (bare-alpha Q target, prereg §5 F3)": abs(Q_TARGET_BARE_ALPHA - 137.0359990837) < 1e-6,
        "1/(ALPHA*1.2) == 114.20 (kappa_chiral Q target, §5 F3)": abs(Q_TARGET_KAPPA_CHIRAL - 114.1966659) < 1e-4,
        "KAPPA_TILDE == 6/5 (alpha-FREE coupling, §6)": abs(KAPPA_TILDE - 1.2) < 1e-12,
    }
    return checks


# ============================================================================
# section: lattice / run configuration (PLACEHOLDER — filled next commit)
# ============================================================================
@dataclass
class RunConfig:
    """Lattice + seed parameters. Defaults match the G0 PASS lattice (N=48, R=10,
    r=4) so the extractor runs at HIGH reliability (rel 0.73/0.94) and r stays
    clear of the r~1.1-cell collapse zone (G4 hazard)."""
    N: int = 48
    dx: float = 1.0
    R: float = 10.0
    r: float = 4.0
    # placeholders — filled in subsequent commits
    pass


def main():  # PLACEHOLDER — filled in subsequent commits
    print("passive_eigenmode_driver: skeleton — gates + reads added in subsequent commits")
    checks = _verify_constants()
    for k, v in checks.items():
        print(f"  [{'OK' if v else 'FAIL'}] {k}")
    assert all(checks.values()), "canonical-constant cross-check failed"


if __name__ == "__main__":
    main()
