"""COUPLED A1+winding EIGENSOLVE — does a confined electron eigenmode (mass+charge)
exist, and where does it sit in the V_yield/V_snap/m_e ladder.

FROZEN PRE-REG: research/2026-06-24_engine-coupled-eigensolve_prereg.md (commit 54d605f8).

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS IS (the conservative-existence keystone S3 left untested)
═══════════════════════════════════════════════════════════════════════════════
This is a CONSERVATIVE EIGENVALUE / EXISTENCE problem. We eigensolve the SAME
Hermitian generator H that S3 (coupled_cage_winding._assemble_H) time-evolved and
ask whether a CONFINED STATIONARY BOUND MODE carrying BOTH the A1 mass-amplitude
AND the (2,3) Cosserat winding-charge EXISTS in its spectrum. We report EIGENPAIRS,
NOT trajectories — this does NOT refill the twice-falsified self-formation slot
(A47 v11b; pre-reg §0/§4). Re-posing time-domain self-trap is BARRED.

  fork-b eigensolved the A1-ALONE confined mode (a graph Laplacian on the native
  connect-map). This module EXTENDS that eigensolve to the COUPLED OBJECT: the
  A1 mass-block + the b_ω winding-amplitude block + the S(A)-front-gated on-site
  coupling, the FULL Hermitian H. The genuinely new work is (i) eigensolving the
  COUPLED H, (ii) the BOTH-SECTORS-PRESENT gate (d) on the eigenstate (the
  genesis-24 guard — winding must NOT have bled into the A1 scalar), and (iii)
  the §3 V_yield/V_snap/m_e ladder readout (A*, ω_bound).

═══════════════════════════════════════════════════════════════════════════════
THE OPERATOR + THE BOUND-MODE CONVENTION (load-bearing sign flip vs fork-b)
═══════════════════════════════════════════════════════════════════════════════
H (rigid_template) on the periodic native N³ lattice, state x = [a_A1, b_ω]:
    H_A1 block : ω_b·I − c_A1²·L_D            (L_D = adjoint_div(D ∇), D=1/S(A))
    b_ω block  : ω_s·I − c_ω²·L_D             (b_ω = LC amplitude on the fixed
                                               winding template ê_w; the (2,3)
                                               winding integer lives in ê_w)
    coupling   : a_A1 ← Ω·e^{+iχθ_χ}·b_ω, b_ω ← Ω·e^{−iχθ_χ}·a_A1  (Hermitian)

L_D is the Stage-2 NATIVE K4 stiffness (NOT Cartesian 7-pt; HR1). H is Hermitian
⇒ real eigenvalues ⇒ Im(ω)=0 EXACTLY (the lossless reactive cage; gate c is
structural-by-construction for the closed operator).

SIGN-FLIP vs fork-b (RF-2 corollary): fork-b solves L_D ψ = ω² ψ and the bound
stiff-core breather is the HIGHEST ω² (gap ABOVE the band, D=1/S→∞ stiff core).
HERE the A1 block is ω_b·I − c²·L_D — the MINUS flips it: the SAME stiff-core
breather is the LOWEST-algebraic (most-bound) eigenvalue of H. So we eigensolve
the SMALLEST-algebraic ("SA") end of H, and the fork-b ω² = (ω_b − w_H)/c² maps
the H-eigenvalue back to the fork-b breathing frequency for the HALT-gate
comparison.

═══════════════════════════════════════════════════════════════════════════════
α-CLEAN (operating principle, pre-reg §0)
═══════════════════════════════════════════════════════════════════════════════
The chord-deciding reads route through the _winding_host κ̃=6/5 guard. NO ALPHA /
Q_TANK / KAPPA_CHIRAL_ELECTRON / V_SNAP on the verdict path (the operator reads a
dimensionless A=|a_A1|/V_yield; the α-carrying V_yield CANCELS). V_snap/V_yield
enter ONLY as the declared §3 operating-point CALIBRATION, never on a verdict read.
The import-guard triad below fails the import if an α-carrier leaks in.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# REUSE (anti-rebuild, Rule 14): the S3 coupled Hermitian generator + its config.
from ave.solvers.coupled_cage_winding import (
    CoupledCageWinding,
    CoupledCageWindingConfig,
)

# REUSE (anti-rebuild, Rule 14): fork-b's cluster-aware gap machinery (the bound
# LEVEL vs band-top witness; degeneracy-safe — the core breather is multiply
# degenerate by symmetry).
from ave.solvers.fork_b_saturation_tank import _cluster_spectrum

# REUSE: the (2,3) winding integer reader (the SAME coordinate S1/charge-quant use).
from ave.topological.charge_quantization import compute_Q_link

# ── the α-FREE chord-path winding factor (routed via the host guard) ──
from tests.engine_acceptance._winding_host import (
    assert_winding_host_globals_alpha_clean,
    winding_kappa_tilde,
)

# ─────────────────────────────────────────────────────────────────────────────
# α-leak guard triad (import-time). An α-carrier leaking here fails the import.
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "α-leak: ALPHA must NOT be imported"
assert "Q_TANK" not in globals(), "α-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "ELECTRON" not in globals(), "α-leak: ELECTRON instance must NOT be imported"
assert "V_SNAP" not in globals(), "α-leak: V_SNAP must NOT be on the chord path"
assert "KAPPA_CHIRAL_ELECTRON" not in globals(), "α-leak: KAPPA_CHIRAL_ELECTRON (=α·κ̃) forbidden"

KAPPA_TILDE: float = winding_kappa_tilde(2, 3)  # = 6/5, α-free (chord-path witness)


@dataclass(frozen=True)
class CoupledEigenConfig:
    """Frozen coupled-eigensolve config. The geometry defaults are the CANONICAL
    (2,3) winding scale (R=7, r=2.3, N=32 — the charge_quantization gate scale at
    which the seeded winding reads (2,3) correctly: validate-on-known PASS) with a
    WIDE A1 core (a1_radius=6.0) so the saturation FRONT reaches the winding torus
    radius R (the only regime where the coupling can hybridize A1↔winding)."""

    N: int = 32
    pml_thickness: int = 4
    V_yield: float = 1.0
    a1_amplitude: float = 0.999      # near A_cap ⇒ deep stiff core (S→S_min, D=1/S huge)
    a1_radius: float = 6.0           # WIDE ⇒ front shell reaches the winding torus R
    R: float = 7.0                   # winding torus major radius (canonical (2,3) scale)
    r: float = 2.3                   # winding tube minor radius
    rate: float = 0.3                # S2 coupling rate scale
    omega_b: float = 1.0             # A1 breather frequency
    omega_s: float = 1.0             # ω-tank LC frequency (resonant ⇒ strongest exchange)
    chi: int = +1                    # lattice handedness (matter)
    k_eigs: int = 16                 # how many SA eigenpairs to extract
    core_frac_floor: float = 0.50    # (a) the fork-b GATE1 bar
    winding_torus_floor: float = 0.20  # (d) min fraction of b_ω norm ON the winding torus
    winding_on: bool = True

    def to_coupled_cfg(self) -> CoupledCageWindingConfig:
        return CoupledCageWindingConfig(
            N=self.N,
            pml_thickness=self.pml_thickness,
            V_yield=self.V_yield,
            R=self.R,
            r=self.r,
            rate=self.rate,
            omega_b=self.omega_b,
            omega_s=self.omega_s,
            chi=self.chi,
            winding_mode="rigid_template",
            winding_on=self.winding_on,
        )


def _build_seeded_sim(cfg: CoupledEigenConfig, *, winding_on: bool) -> CoupledCageWinding:
    """Build a CoupledCageWinding at the operating point: a deep saturated A1 core
    (the posited mass, CP8 — PLANTED, not self-formed; flagged) + the separately-
    initialized (2,3) winding template (genesis-24 guard: ω is NEVER grad(V)).
    winding_on toggles the coupling Ω (False ⇒ Ω≡0 ⇒ the A1-alone HALT control)."""
    ccfg = cfg.to_coupled_cfg()
    ccfg = CoupledCageWindingConfig(**{**ccfg.__dict__, "winding_on": winding_on})
    sim = CoupledCageWinding(ccfg)
    sim.seed_A1_sech(amplitude=cfg.a1_amplitude, radius=cfg.a1_radius)
    sim.seed_winding(amplitude=1.0)
    return sim
