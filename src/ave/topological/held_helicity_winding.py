"""OPTION C′ — the NO-WORK Beltrami-helicity HOLD (the conserved charge, held conservatively).

This is the C′ amendment to OPTION C (prereg `2026-06-15_passive-eigenmode-solve.md` §9.1,
Grant-greenlit 2026-06-16). It is built ALONGSIDE `held_bc_winding.py` (OPTION C, the per-cell
director-template hold that DISQUALIFIED — it pumped 56× by overwriting local ω-directions against
the free gradient flow). C is preserved intact (KEEP-BOTH / audit-trail discipline); C′ holds a
DIFFERENT object by a DIFFERENT mechanism.

WHAT C HELD (wrong object): a real-space per-cell DIRECTOR TEMPLATE (`WindingHold`), re-aligned each
    step → fought the free dynamics → did gradient-W work → 56× pump → DISQUALIFY.

WHAT C′ HOLDS (the corpus charge): the conserved **Beltrami helicity** `H_bel = ∫ ω·(∇×ω) dV`
    (`master-equation.md`, two-"3"s disambiguation block, verbatim: "charge = Beltrami helicity
    H_bel = ∫ω·(∇×ω)") — a single GLOBAL scalar invariant on the independent Cosserat-ω carrier.

═════════════════════════════════════════════════════════════════════════════════════════════════
🔴 LOAD-BEARING SPEC-vs-CODE CONFLICT (flag-don't-fix; surfaced before scaffolding, 2026-06-16):
═════════════════════════════════════════════════════════════════════════════════════════════════
    §9.1 gives the LITERAL formula  `H_bel(omega) = sum(_beltrami_helicity(omega, dx)) * dx**3`.
    BUT the engine's `cosserat_field_3d._beltrami_helicity` returns the NORMALIZED handedness
    density  h_local = ω·(∇×ω) / (|ω|·|∇×ω|) ∈ [−1, +1]  (a per-cell handedness, doc 54_ §6),
    NOT the raw helicity density ω·(∇×ω) the corpus integral `∫ω·(∇×ω)dV` calls for.

    Measured on the planted (2,3) traveling seed (N=26, R=5, r=2.5, dx=0.5, amp=0.3):
      • sum(_beltrami_helicity)*dx³  = 137.19  — but 125.5 (91.5%) of that is VACUUM-CELL ARTIFACT
        (cells where |ω|≈0, the eps_h=1e-12 regularizer manufacturing spurious handedness); only
        11.7 comes from the actual shell. Its ∇_ω is stiff (‖grad‖≈5.6e6), vacuum-cell dominated.
        The 137≈1/α resemblance is a COINCIDENCE (it tracks the vacuum-cell count of the box), NOT
        the corpus charge.
      • ∫ω·(∇×ω)dV (RAW)             = 2.1e-4 — the verbatim corpus object: smooth (‖grad‖≈0.71),
        scales as s² in ω (as helicity must), robust 0.269 on the (1,1) Beltrami control. Small on
        the (2,3) plant because the SIGNED helicity nearly cancels (shell density −5.1e-3,
        |density| integral 0.34 — there IS structure, it is sign-cancellation, not absence).

    RESOLUTION (per the brief: "§9.1 wins; flag the conflict, don't silently diverge"): §9.1's
    PROSE intent ("hold the conserved H_bel = ∫ω·(∇×ω), the corpus's actual charge") and its
    LITERAL Python formula CONFLICT, because the named engine helper is normalized. The corpus
    charge — the object `master-equation.md` defines and §9.1's prose names — is the RAW integral.
    C′ HOLDS THE RAW INTEGRAL `H_bel_raw = ∫ω·(∇×ω)dV` as the conserved charge, and ALSO records
    the spec-literal normalized-sum each step for transparency / audit. The held target is the raw
    integral. This conflict is reported to the orchestrator (do not silently pick one).
═════════════════════════════════════════════════════════════════════════════════════════════════

MECHANISM (NO-WORK constraint — energy-neutral BY CONSTRUCTION, unlike C where it was only
    measured and failed):
      g       = ∇_ω H_bel      (gradient of the helicity scalar wrt the ω field; jax.grad)
      e       = ∇_ω E_ω        (gradient of the ω-sector energy = the ω part of the Hamiltonian)
      g_perp  = g − (⟨g,e⟩/⟨e,e⟩) e     (Gram-Schmidt: remove the energy-changing component)
      ω      += λ g_perp       (λ from a 1-D Newton/line-solve on the scalar H_bel(λ) = target)
    Because g_perp ⊥ e, to first order  dE = ⟨e, λ g_perp⟩ = 0  → energy-neutral BY DESIGN. The
    residual second-order curvature is why the FULL-Hamiltonian ledger is STILL verified (the
    `ave-conserved-vs-pumped` witness = eng_w.total_hamiltonian(), NOT sum(ω²) which the C
    false-positive guard-bug read — fixed in commit 86c1a641).

SUBSTRATE-NATIVE WALK (substrate-native-check v1.2, done BEFORE this code):
  CP1 (dynamics)   : the ω-carrier evolves via velocity-Verlet step() (wave propagation). C′ adds a
                     CONSTRAINT correction after the free step — NOT a gradient-descent settle, NOT
                     energy minimization (Rule 6 SM-leak avoided).
  CP2 (sector)     : Cos-sector (Cosserat ω), the INDEPENDENT carrier. H_bel is a Cosserat-sector
                     invariant. The A1 (V_inc,V_ref) phasor is NEVER read or written (G0-clean).
  CP3 (objective)  : AVE-native — a Lagrange constraint on a conserved invariant, projected ⊥ the
                     ω-sector energy gradient. NOT energy-basin minimization.
  CP4 (phase-space): H_bel and ∇_ω H_bel are computed on the ω field directly, the same coordinate
                     the corpus charge=helicity claim lives in. The (2,3) PAIR is read on the
                     (ω, π_ω) phasor (extract_2_3_omega_fast), never real-space lattice-Cartesian.
  CP9 (dynamical)  : the field evolves freely via the engine's OWN step(); the H_bel correction is
                     applied to the EVOLVED state (a projection of the evolved field), not a re-seed.
  CP10 (boundary)  : the correction is a GLOBAL SCALAR constraint closed by a line-solve, NOT a bulk
                     confining force ∝ dS/dA (which is singular at the wall and detonates).

CARRIER DISCIPLINE (load-bearing): operates ONLY on eng_w.omega / eng_w.omega_dot (the independent
    Cosserat-ω carrier). NEVER reads or writes the A1 (V_inc, V_ref) phasor — preserves the G0
    double-count-clean result (`master-equation.md`: never wire the winding into (V_inc, V_ref)).
"""

from __future__ import annotations

from dataclasses import dataclass, field

import jax
import jax.numpy as jnp
import numpy as np

from ave.topological.cosserat_field_3d import (
    _beltrami_helicity,
    _tetrahedral_curl,
)


# ============================================================================
# section: the conserved Beltrami-helicity INTEGRAL (the corpus charge)
# ============================================================================
def H_bel_raw(omega: jnp.ndarray, dx: float) -> jnp.ndarray:
    """The CORPUS CHARGE: the Beltrami-helicity INTEGRAL  H_bel = ∫ ω·(∇×ω) dV.

    `master-equation.md` (two-"3"s disambiguation, verbatim): "charge = Beltrami helicity
    H_bel = ∫ω·(∇×ω)". Discretized as  sum_cells( ω·(∇×ω) ) · dx³  with the SAME tetrahedral
    curl operator the engine uses (`_tetrahedral_curl`, cosserat_field_3d.py). This is the RAW
    (un-normalized) helicity density — quadratic in ω, smooth, scales as s² under ω→sω — NOT the
    normalized handedness `_beltrami_helicity` (see the module-header SPEC-vs-CODE conflict).

    A single global scalar (jnp 0-d array, jax.grad-differentiable wrt omega)."""
    curl = _tetrahedral_curl(omega, dx)
    return jnp.sum(jnp.sum(omega * curl, axis=-1)) * dx**3


def H_bel_normalized_sum(omega: jnp.ndarray, dx: float) -> jnp.ndarray:
    """The SPEC-LITERAL §9.1 formula  sum(_beltrami_helicity(omega,dx)) * dx³ — recorded for
    TRANSPARENCY/audit ONLY, NOT held. This sums the NORMALIZED handedness h_local ∈ [−1,+1]
    (`_beltrami_helicity`), which is dominated by vacuum cells (≈91% artifact on the (2,3) seed;
    see the module-header conflict block). The held charge is `H_bel_raw`, not this."""
    return jnp.sum(_beltrami_helicity(omega, dx)) * dx**3


# jax.grad of the corpus charge wrt the ω field (the constraint gradient g = ∇_ω H_bel).
# jitted: the curl + sum are pure jnp; differentiating is exact (no FD).
_grad_H_bel_raw = jax.jit(jax.grad(H_bel_raw), static_argnums=())


def grad_H_bel(omega: np.ndarray, dx: float) -> np.ndarray:
    """g = ∇_ω H_bel_raw — the gradient of the corpus charge wrt the ω field, as numpy.

    For the symmetric bilinear H = Σ ω·(∇×ω)·dx³, ∇_ω H = (∇×ω + ∇×^T ω)·dx³; jax.grad gets this
    exactly via the tetrahedral-curl adjoint. Returned numpy (the engine state is numpy)."""
    g = _grad_H_bel_raw(jnp.asarray(omega), float(dx))
    return np.asarray(g)
