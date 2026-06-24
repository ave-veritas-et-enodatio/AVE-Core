"""S3 — the COUPLED real-space A1↔ω PDE on the native tetrahedral K4 stencil.

FROZEN PRE-REG: research/2026-06-24_engine-s3-cavity-pinning_prereg.md (commit 0b5691cd).

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS IS (the S3 make-or-break instrument — the re-route payoff)
═══════════════════════════════════════════════════════════════════════════════
Stage-2 FALSIFIED the bulk self-trap: a seeded A1 precursor DISPERSES (Mode-III,
energy-conservation-certified) on the native K4 stencil (A1-ALONE does NOT
localize, research/2026-06-24_engine-stage2-native-cage_result.md). S3 tests the
SANCTIONED successor: does the now-conserved (2,3) Cosserat winding ω (S1, #407)
+ the conservative skew-Hermitian A1↔ω lock H_couple (S2, #409) PIN the dispersing
A1 core?

This module is the GENUINE NEW WORK the pre-reg §5 names: a REAL-SPACE coupled
A1↔ω PDE on the native TETRA_OFFSETS stencil. It EXTENDS the Stage-2
native_cage_imex host (native + α-clean + energy-gated scalar A1 cage) with:
  (A) the ω Cosserat winding DOF as its OWN real-space field (genesis-24 guard:
      ω is NEVER grad(V); it is seeded by seed_pq_winding and evolves by its own
      native wave operator);
  (B) the S2 conservative skew-Hermitian H_couple A1↔ω lock, lifted from the S2
      C^{2M} chain GENERATOR/FORM onto the real-space lattice (the S2 2-mode
      machinery has NO real space and CANNOT carry this — pre-reg §5);
  (C) the closed-box energy gate + GX3/GX5 negative controls on the COUPLED
      object (NO PML, NO damping — damping-bought localization is the top trap).

═══════════════════════════════════════════════════════════════════════════════
THE COUPLED STATE + GENERATOR (real-space, native stencil)
═══════════════════════════════════════════════════════════════════════════════
Two analytic-signal fields live on the same native K4 lattice:

  a_A1(x) ∈ C        — the A1 BULK-DILATATION breather analytic signal (q + i·p):
                       |a_A1|² = trapped bulk = MASS, the longitudinal "3"
                       (the DISPERSING scalar Stage-2 falsified A1-alone).
  a_ω(x) ∈ C^3       — the Cosserat micro-rotation ω LC-quadrature analytic signal
                       (Re = the winding-carrying ω config seeded by
                       seed_pq_winding; Im = its momentum quadrature, the L-state):
                       the poloidal/toroidal (2,3) winding = CHARGE/helicity,
                       a SEPARATELY-conserved real-space DOF (S1).

The A1↔ω coupling acts on the SCALAR PROJECTION of ω onto the seeded winding
template ê_w(x) (a fixed unit field): a_ω,s(x) = ê_w(x)·a_ω(x). This is the S2
on-node 2×2 block, lifted to a per-site real-space block:

  i ∂_t a_A1   = ω_b·a_A1                              (A1 breather frequency)
               − c_A1²·L_native·a_A1                   (A1 disperses on K4)
               + Ω(x)·e^{+iχθ_χ}·a_ω,s                 (THE S2 COUPLING)
  i ∂_t a_ω    = ω_s·a_ω                               (ω-tank LC frequency)
               − c_ω² ·L_native·a_ω                    (ω disperses on K4)
               + Ω(x)·e^{−iχθ_χ}·a_A1·ê_w(x)           (= conj coupling ⇒ Hermitian)

with the SATURATION-FRONT-GATED rate (the S2 FORK A=(a) coupling PORT):
      Ω(x) = rate · g_front(A) · S(A) ,   A = |a_A1|/V_yield
and L_native = adjoint_tetrahedral_divergence(D · tetrahedral_gradient(·)),
D = 1/S(A) the native saturated stiffness (the Stage-2 operator, UNCHANGED).

The full generator H (native-Laplacian blocks + on-site conjugate-pair coupling)
is HERMITIAN ⇒ the propagator e^{-iHdt} is UNITARY ⇒ the JOINT energy
‖a_A1‖² + ‖a_ω‖² is conserved EXACTLY (the rigor guard — no damping can fake a
pin). Integrated by CRANK–NICOLSON (the Cayley transform, the energy-conserving
unitary scheme, the coupled analog of the Stage-2 IMEX), D and Ω lagged (frozen)
each step. Solved by GMRES (the generator is non-symmetric complex).

═══════════════════════════════════════════════════════════════════════════════
GENESIS-24 GUARD (pre-reg §4) — ω is its OWN DOF, NEVER grad(V)
═══════════════════════════════════════════════════════════════════════════════
A1 (= MASS) and ω (= CHARGE/helicity winding) are SEPARATELY initialized,
SEPARATELY conserved. ω is seeded by seed_pq_winding (a real-space (2,3) phase
field), NEVER read off a_A1. H_couple's chirality phase χ·θ_χ is STRUCTURAL
(lattice handedness, θ_χ = 2π·ν_vac), NOT read off V. The energy gate certifies
BOTH the A1-norm AND the ω-winding — a "pin" cannot be bought by bleeding the
winding into the scalar.

α-CLEAN: the coupling rate scale uses κ̃=6/5 (the host-certified α-free winding
factor) and the chirality phase uses θ_χ=2π·ν_vac (ν_vac=2/7, α-free). NO ALPHA
/ KAPPA_CHIRAL_ELECTRON / V_SNAP / Q_TANK on the chord-deciding path. The
_winding_host forbidden-name guard is extended into the coupled step (the load-
time guard triad re-asserted below).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# α-FREE: reuse the VALIDATED native operator + kernel (Stage-2, G1-G8 unchanged).
from ave.solvers.graded_vacuum_network import (
    saturation_kernel,
    stiffness_profile,
)
from ave.solvers.native_cage_imex import assemble_L_D, build_grad_div_periodic

# the real-space (2,3) winding seed + the α-free winding-host coupling inputs.
from ave.topological.charge_quantization import seed_pq_winding

# ─────────────────────────────────────────────────────────────────────────────
# α-leak guard triad (import-time; extends the native_cage_imex + winding-host
# guards into the COUPLED step). An α-carrier leaking here fails the import.
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "α-leak: ALPHA must NOT be imported"
assert "Q_TANK" not in globals(), "α-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "ELECTRON" not in globals(), "α-leak: ELECTRON instance must NOT be imported"
assert "V_SNAP" not in globals(), "α-leak: V_SNAP must NOT be on the chord path"
assert "KAPPA_CHIRAL_ELECTRON" not in globals(), "α-leak: KAPPA_CHIRAL_ELECTRON (=α·κ̃) forbidden"

# ── the α-FREE coupling inputs (named once; both routed via the winding host) ──
# κ̃ = 6/5 (the host-certified α-free (2,3) winding factor; NOT α·κ̃).
from tests.engine_acceptance._winding_host import winding_kappa_tilde  # noqa: E402

KAPPA_TILDE: float = winding_kappa_tilde(2, 3)  # = 6/5, α-free
# the lattice chirality PHASE θ_χ = 2π·ν_vac, ν_vac = 2/7 (α-free). Hard-coded as
# a rational so NO constants-module import (no α-carrier) on the chord path.
NU_VAC: float = 2.0 / 7.0
THETA_CHI: float = 2.0 * np.pi * NU_VAC


@dataclass(frozen=True)
class CoupledCageWindingConfig:
    """Frozen S3 coupled-cage config (α-free; Stage-2 v14 cage defaults + the
    ω-DOF + H_couple controls). The cage half mirrors NativeCageIMEXConfig."""

    N: int = 24
    dx: float = 0.5
    V_yield: float = 1.0
    pml_thickness: int = 4
    exponent: float = 0.5            # Op14 saturation (√S primary)
    S_min: float = 1e-3
    A_cap: float = 0.999
    # A1 + ω wave speeds (c_eff folds 1/S into D; these are the cold speeds).
    c_A1: float = 1.0
    c_omega: float = 1.0
    # H_couple (the S2 FORM): breather/tank frequencies + the gated rate + χ.
    omega_b: float = 1.0
    omega_s: float = 1.0             # resonant ⇒ strongest A1↔ω exchange
    rate: float = 0.3               # the S2 coupling rate scale (× g_front × S)
    chi: int = +1                   # lattice handedness (matter)
    gate: str = "front"             # saturation-front-gated coupling PORT (FORK A=(a))
    # the winding seed geometry (the (2,3) eigen-precursor torus).
    R: float = 7.0
    r: float = 2.3
    # integration controls.
    dt: float = 0.066               # accuracy-set (Stage-2 production dt)
    gmres_tol: float = 1e-10
    gmres_maxiter: int = 2000
    winding_on: bool = True          # winding OFF (False) ⇒ Ω≡0 ⇒ A1-alone control
    port_sigma: float = 0.0          # 0 = closed/lossless (the energy-gate rigor)


def front_gate(A: np.ndarray, *, center: float = 4.0 / 7.0, width: float = 0.18) -> np.ndarray:
    """g_front(A): a thin shell at the Non-Linear→Saturated boundary (CP10) — the
    saturation-FRONT window where the A1↔ω coupling ENGAGES (zero in cold vacuum
    A→0 AND in the deep frozen core A→1). center = R_II = 4/7 (α-free; the SAME
    shell s2_hcouple_gate.front_gate uses). This is the S(A)-gating that makes the
    coupling a saturation-FRONT effect (S2 FORK A=(a)), not a bulk-volume coupling."""
    return np.exp(-((A - center) ** 2) / (2.0 * width**2))


def _strain(absV: np.ndarray, V_yield: float, A_cap: float) -> np.ndarray:
    """A = |V|/V_yield, clipped to A_cap (avoids the S=0 singularity)."""
    return np.minimum(absV / V_yield, A_cap)
