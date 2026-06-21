"""
Node circulator coupling — the shear↔bulk (charge↔mass) coupling as a
NORM-PRESERVING ROTATION (a skew-Hermitian / gyrotropic GENERATOR).
=====================================================================

THE ONE REMAINING LIVE PATH FOR FORK-A.

Fork-A (`device-circuit-models.md`:210-215) asks: does the mass channel (bulk /
A1 dilatation) couple to the charge channel (shear / Cosserat micro-rotation) via
a conserved H_couple, or is it galvanic ISOLATION? Every potential-energy coupling
tried so far DETONATES or is INERT:

  • graft-v3 / graft-v4 trilinear potential  H = κ̃ ∫ g·V·[w·(∇×ω)]  is INDEFINITE
    (linear in each of V, w, ω ⇒ unbounded below). The conserve-and-transfer arm
    (`photon_deplete=True`) DETONATES (`H_bel −4107`); the bounded arm transfers
    ~2 % and is inert (`research/2026-06-10_graft-v4-photon-helicity_result.md` §6).
  • The named escape (graft-v4 §9, 2nd bullet): "a BOUNDED, helicity-TRANSFERRING
    coupling — norm-preserving H_photon↔H_bel exchange ... an orthogonal field-space
    rotation à la the crystal_engine converter, rather than a trilinear potential."

THE ESCAPE REALIZED HERE.  A circulator / gyrator is a NON-RECIPROCAL, LOSSLESS
element whose coupling is ANTISYMMETRIC/SKEW. Formulate the coupling NOT as a
potential V-term but as a SKEW-HERMITIAN GENERATOR on the two mode AMPLITUDES:

    d/dt [a_bulk; a_shear] = -i H [a_bulk; a_shear],     H Hermitian,

        H = [[ ω_b      ,  -i Ω(χ) ],
             [ +i Ω(χ)* ,   ω_s     ]]

The OFF-DIAGONAL Ω is the circulator rate; e^{-iHt} is UNITARY ⇒
|a_bulk|² + |a_shear|² is conserved EXACTLY, regardless of depletion — there is no
indefinite-Hamiltonian pump because the generator is anti-Hermitian by construction,
not a trilinear potential. The non-reciprocity / circulation SENSE is sourced from
the I4₁32 lattice CHIRALITY (the sign of χ), the SAME handedness phase the idealized
S-matrix circulator carries (`node_2domain_nport.py`:376 `chiral_circulator_S`,
S = [[0, e^{+iθ}], [−e^{−iθ}, 0]]). This driver builds the TIME-DOMAIN GENERATOR
whose frequency-domain shadow is that S-matrix.

THE TWO MODES (pinned from the corpus, phase-space coordinates — A46 discipline):
  • a_bulk  = the A1 dilatation / BULK-COMPRESSION mode. Its |a_bulk|² IS the trapped
              bulk energy E_V = "the latent MASS" (crystal_engine.py:354). Real-space
              scalar V, longitudinal "3".
  • a_shear = the Cosserat micro-rotation POLOIDAL-CIRCULATION mode — the LOCAL
              (ω, π_ω) LC quadrature that IS the poloidal winding / the CHARGE "3"
              (crystal_graft_v4.py:46-47). PHASE-SPACE reactance pair, NOT the
              orthogonal global rigid rotation L_ω the previous INERT lock targeted.

The complex amplitude a = q + i·p/ω is the analytic-signal of an LC reactance pair
(q = displacement, p = momentum); |a|² = the mode energy / ω. The skew generator
rotates ENERGY between the two |a|², which is exactly the bounded, norm-preserving,
helicity-transferring exchange the trilinear potential could not deliver.

α-FREEDOM: the circulator RATE magnitude uses the topological converter
κ̃ = 6/5 = pq/(p+q) (`cross_sector_coupling.py`:23, α-FREE — NOT κ_chiral=1.2α);
the chirality PHASE uses θ_χ = 2π·ν_vac (ν_vac = 2/7, α-free, the same gyrotropic
phase as `node_2domain_nport.py`:473). No α-bearing literal enters any rate, energy,
or amplitude. CI-style guard: `assert_alpha_free()`.

FOUR GATES (each PASS/FAIL reported honestly; a circulator that ALSO fails on the
winding CLOSES Fork-A as ISOLATION — a real, valuable negative):
  (A) CONSERVE      — |a_bulk|²+|a_shear|² conserved to machine precision; no pump.
  (B) TRANSFER      — energy actually FLOWS bulk↔shear; transfer-fraction ≫ 2 %.
  (C) LOCK-ON-WIND  — the coupling acts on the POLOIDAL WINDING amplitude (charge
                      mode), and coupling-ON differs from coupling-OFF ON THAT
                      observable (else it is the same inert failure).
  (D) MOTION→MASS   — bulk-compression energy (mass) scales with the shear
                      CIRCULATION RATE (more circulation ⇒ more trapped compression
                      ⇒ more effective mass), winding (charge) fixed.

SELF-SKEPTICAL DISCIPLINE: every gate guards against the way the previous efforts
FOOLED THEMSELVES — INERT-LOCK (ON≡OFF on the winding), TAUTOLOGICAL-TRANSFER
(closure identity not a measured flow), VACUOUS-CONSERVATION (norm conserved because
the coupling does nothing), and FORCED-vs-IMPOSED (is the non-reciprocity FORCED by
the chiral lattice or IMPOSED by hand?).

Driver: research/2026-06-20_node-circulator-coupling.md
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

import numpy as np

# ── canonical, α-free constants only ────────────────────────────────────────
from ave.core.constants import NU_VAC, M_E, C_0, HBAR
from ave.core.cross_sector_coupling import KAPPA_TILDE  # 6/5 = pq/(p+q), α-free

_OUT = Path(__file__).resolve().parent / "_output" / "node_circulator_coupling.json"


# ═════════════════════════════════════════════════════════════════════════════
# 0.  α-FREEDOM GUARD  (no α-bearing literal in any rate / energy / amplitude)
# ═════════════════════════════════════════════════════════════════════════════
def assert_alpha_free() -> None:
    """HALT if any α-bearing canonical symbol leaked into the engine constants
    this driver uses. κ̃=6/5 topology + θ_χ=2π·ν_vac (ν_vac=2/7) are the ONLY
    coupling inputs; both are α-free. (Mirrors the graft-v* CI gates.)"""
    raise NotImplementedError


# ═════════════════════════════════════════════════════════════════════════════
# 1.  THE SKEW-HERMITIAN GENERATOR  (the circulator, NOT a potential)
# ═════════════════════════════════════════════════════════════════════════════
def circulator_generator(omega_b, omega_s, rate, chi):
    """Build the 2×2 Hermitian generator H with a skew (anti-Hermitian-real)
    off-diagonal sourced from the lattice chirality χ."""
    raise NotImplementedError


def evolve(a0, H, dt, n_steps):
    """Unitary time-evolution a(t+dt) = e^{-iHdt} a(t) via the exact 2×2
    propagator. Returns the amplitude trajectory."""
    raise NotImplementedError


# ═════════════════════════════════════════════════════════════════════════════
# GATE A — CONSERVE
# ═════════════════════════════════════════════════════════════════════════════
def gate_A_conserve(*args, **kwargs):
    raise NotImplementedError


# ═════════════════════════════════════════════════════════════════════════════
# GATE B — TRANSFER
# ═════════════════════════════════════════════════════════════════════════════
def gate_B_transfer(*args, **kwargs):
    raise NotImplementedError


# ═════════════════════════════════════════════════════════════════════════════
# GATE C — LOCK-ON-WINDING (ON vs OFF)
# ═════════════════════════════════════════════════════════════════════════════
def gate_C_lock_on_winding(*args, **kwargs):
    raise NotImplementedError


# ═════════════════════════════════════════════════════════════════════════════
# GATE D — MOTION → MASS
# ═════════════════════════════════════════════════════════════════════════════
def gate_D_motion_to_mass(*args, **kwargs):
    raise NotImplementedError


# ═════════════════════════════════════════════════════════════════════════════
# FORCED-vs-IMPOSED verdict
# ═════════════════════════════════════════════════════════════════════════════
def forced_vs_imposed(*args, **kwargs):
    raise NotImplementedError


# ═════════════════════════════════════════════════════════════════════════════
# VALIDATE-ON-KNOWN
# ═════════════════════════════════════════════════════════════════════════════
def validate_on_known() -> dict:
    raise NotImplementedError


# ═════════════════════════════════════════════════════════════════════════════
# MAIN
# ═════════════════════════════════════════════════════════════════════════════
def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
