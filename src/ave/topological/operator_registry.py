"""Registered discrete-operator sets — the DEC-canonicalization inventory.

ENGINE-HARDENING ARC item 1 (Grant-fired 2026-07-04;
`_orchestration/2026-07-04_engine-upgrade-program.md` §1). This module is the
single source of truth for WHICH discrete div/curl/grad operator sets a live
solver may drive a verdict on, and CERTIFIES each one is a genuine adjoint pair
(`div = adjoint_sign·gradᵀ`, sign ∈ {+1, −1} per the set's convention) with the
exactness the class claims (`∂∂ = 0`).

═══════════════════════════════════════════════════════════════════════════════
WHY THIS EXISTS (the operator-failure class it retires — verify at HEAD)
═══════════════════════════════════════════════════════════════════════════════
The EM-readout Stage-1b review (see `srs_dec.py:11-24`, verbatim) proved the two
operators the retired driver used —
    _srs_curl_nodes      : 1/deg-weighted, per-node 3-vector, bond-projected curl
    _srs_node_divergence : ½ face-average, per-node bond-projected divergence
(both in src/scripts/vol_2_subatomic/em_readout_vsector_transducer.py) are NOT an
adjoint/DEC pair: div∘curl on a random field is pointwise O(1) (RMS ≈ 0.35). A
merged closure resting on that pair could only be scoped as an OPERATOR-PAIR
property, never a class theorem.

This registry generalizes the fix: every operator set a LIVE solver drives a
verdict on is enumerated here with its carrier + adjoint spec, and the CI check
`src/tests/test_operator_adjoint_consistency.py` parameterizes over the registry
and asserts, for each registered set, that the composition identities hold to the
declared precision (`exact_integer` for the pure-incidence DEC set, `machine`
for the float permutation-difference sets). A NON-adjoint heuristic that tries to
drive a verdict is caught here, not at post-merge review.

═══════════════════════════════════════════════════════════════════════════════
CARRIER DISCIPLINE (the operator sets live on DIFFERENT lattices)
═══════════════════════════════════════════════════════════════════════════════
There is no single canonical operator PAIR because the engine has two legitimate
carriers (srs-z3 production + diamond-z4 instrument, per the D1 ratification
`_orchestration/2026-07-03_srs-migration-policy.md`) plus the Cartesian-reference
Yee grid. Canonicalization means: each set is CERTIFIED adjoint on its OWN
carrier, tagged with that carrier, and the srs sets are RECONCILED to the DEC
∂₁/∂₂ (the srs-z3 `build_incidence` B = −∂₁ᵀ exactly, `srs_dec.py:99-106`). It
does NOT mean routing a diamond operator through the srs complex (they are
different lattices — that would be a category error, not a fix).

The registry tags each set:
  * carrier            — srs-z3 | diamond-z4 | cartesian-reference
  * adjoint_pair       — True  ⇒ div and grad are exact adjoints (div = s·gradᵀ
                         with s = adjoint_sign ∈ {+1, −1}); the CI check asserts
                         ‖div − s·gradᵀ‖ ≤ tol.
  * adjoint_sign       — +1 or −1: the sign in div = s·gradᵀ. The DEC set uses the
                         NEGATIVE-adjoint convention (div = −∂₁ = −gradᵀ), so that
                         L0 = div∘grad is −PSD; the diamond native sets use the
                         POSITIVE-adjoint convention (div = +gradᵀ) so that
                         L_D = div∘grad is +PSD. Both are valid — the physics
                         invariant is that div∘grad is SYMMETRIC; the sign is a
                         bookkeeping choice that flows into whether the Laplacian
                         is ±PSD. Registering the sign per-set is the honest
                         reconciliation (flag-don't-fix: the two carriers genuinely
                         differ in convention; the registry records it, does not
                         force one onto the other).
  * exactness          — "exact_integer" | "machine" — the ∂∂=0 / adjoint tol tier.
  * dd_zero            — True ⇒ the set carries a ∂∂=0 composition (curl∘grad or
                         div∘curl_adj); the CI check asserts it holds to tol.
  * provenance_frozen  — True ⇒ the set is a merged-result driver's operator; the
                         CI check must NOT alter its behavior (KEEP-BOTH); it only
                         READS + certifies. (Applies to the diamond native-cage /
                         gw sets whose byte-identical output backs a merged verdict.)

α-CLEAN: this module imports NO physical constant. The DEC operators are integer
incidence matrices; the diamond / cartesian sets are float permutation/stencil
differences with a lattice spacing only. No ALPHA / Q_TANK / V_SNAP on any path.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

import numpy as np

# import-time α-leak guard (same posture as srs_dec).
assert "ALPHA" not in globals(), "α-leak: ALPHA must NOT be imported here"
assert "Q_TANK" not in globals(), "α-leak: Q_TANK (=1/alpha) must NOT be imported here"
assert "V_SNAP" not in globals(), "α-leak: V_SNAP must NOT be on the operator-registry path"


# ═════════════════════════════════════════════════════════════════════════════
# The certifiable-set descriptor
# ═════════════════════════════════════════════════════════════════════════════
@dataclass(frozen=True)
class OperatorSet:
    """A registered discrete-operator set + the adjoint/∂∂ spec the CI check asserts.

    `build` returns a dict of the assembled sparse/dense operators for a small
    test instance, with (at minimum) the keys the declared checks need:
      * adjoint_pair ⇒ keys "grad" and "div"   (asserts div ≈ adjoint_sign·gradᵀ)
      * dd_zero      ⇒ a composition callable under "dd_compose" returning the
                       operator whose entries must be ≤ tol (e.g. div∘curl_adj).
    Keeping the build as a callable (not a stored matrix) means the registry
    itself holds no lattice state and the CI check assembles fresh each run.
    """

    name: str
    carrier: str  # srs-z3 | diamond-z4 | cartesian-reference
    module: str  # dotted path to the defining module
    adjoint_pair: bool
    adjoint_sign: int  # +1 or −1 in div = adjoint_sign · gradᵀ
    dd_zero: bool
    exactness: str  # "exact_integer" | "machine"
    provenance_frozen: bool
    build: Callable[[], dict]
    consumers: tuple[str, ...] = field(default_factory=tuple)
    note: str = ""

    def tolerance(self) -> float:
        """Adjoint / ∂∂ tolerance for this set's exactness tier."""
        return 0.0 if self.exactness == "exact_integer" else 1e-9


# ═════════════════════════════════════════════════════════════════════════════
# Set builders (each returns the assembled operators for a small test instance)
# ═════════════════════════════════════════════════════════════════════════════
def _build_srs_dec_set() -> dict:
    """The canonical srs-z3 DEC set (∂₁, ∂₂). Exact-integer adjoint + ∂∂=0."""
    from ave.topological.srs_dec import MIN_SRS_L, build_srs_dec

    dec = build_srs_dec(L=MIN_SRS_L)
    # grad = ∂₁ᵀ, div = −∂₁; dd = div∘curl_adj = −∂₁∂₂ (the THEOREM's operator),
    # and curl∘grad = ∂₂ᵀ∂₁ᵀ = (∂₁∂₂)ᵀ. Both are exact-integer zero.
    return {
        "grad": dec.grad,
        "div": dec.div,
        "curl": dec.curl,
        "curl_adj": dec.curl_adj,
        "dd_compose": (dec.div @ dec.curl_adj),  # div∘curl_adj = −∂₁∂₂ = 0
        "dd_compose_2": (dec.curl @ dec.grad),  # curl∘grad = (∂₁∂₂)ᵀ = 0
    }


def _build_srs_incidence_set() -> dict:
    """The srs-z3 solver incidence pair (B, Bᵀ), reconciled B = −∂₁ᵀ (srs_dec.py:99).

    grad_solver = B (n_bonds × n_nodes), div_solver = Bᵀ. The solver Laplacian is
    L_srs = BᵀDB, so the solver's own convention is div = +gradᵀ (POSITIVE adjoint,
    giving a +PSD Laplacian) — registered with adjoint_sign=+1. This is a DIFFERENT
    sign convention from the DEC set (div = −∂₁), and that difference is EXACTLY the
    reconciliation srs_dec.py:99-106 documents: B = −∂₁ᵀ, so the solver's +Bᵀ
    divergence equals −∂₁ = the DEC div, and L_srs = BᵀB = ∂₁∂₁ᵀ = −L0. Same
    operator; the per-set adjoint_sign records the convention each module ships."""
    from ave.core.chiral_lattice import build_srs_net
    from ave.solvers.srs_cage_winding import build_incidence

    net = build_srs_net(L=3)
    B, _bonds = build_incidence(net)
    return {"grad": B, "div": B.T.tocsr()}


def _build_diamond_native_cage_set() -> dict:
    """The diamond-z4 native-cage Grad/Div (native_cage_imex). FROZEN provenance
    (backs the Stage-2 DISPERSE merged verdict). Div = +Gradᵀ EXACTLY (positive
    adjoint; the +PSD L_D = GradᵀDGrad invariant); machine-tier."""
    from ave.solvers.native_cage_imex import build_grad_div_periodic

    # DIAMOND-Z4 instrument consumption — acknowledged (item-5 guard).
    Grad, Div = build_grad_div_periodic(N=4, instrument_scope="operator-registry adjoint certification")
    return {"grad": Grad, "div": Div}


def _build_gw_native_set() -> dict:
    """The diamond-z4 GW grad/div (gw_propagation._build_native_grad_div). FROZEN
    provenance (#86 back-reaction leg). Byte-identical build to native_cage; same
    exact-adjoint permutation-difference construction; machine-tier."""
    from ave.gravity.gw_propagation import _build_native_grad_div

    # DIAMOND-Z4 instrument consumption — acknowledged (item-5 guard).
    Grad, Div = _build_native_grad_div(N=4, instrument_scope="operator-registry adjoint certification")
    return {"grad": Grad, "div": Div}


# ═════════════════════════════════════════════════════════════════════════════
# THE REGISTRY (the CI check parameterizes over this list)
# ═════════════════════════════════════════════════════════════════════════════
OPERATOR_SETS: tuple[OperatorSet, ...] = (
    OperatorSet(
        name="srs_dec",
        carrier="srs-z3",
        module="ave.topological.srs_dec",
        adjoint_pair=True,
        adjoint_sign=-1,  # div = −∂₁ = −gradᵀ (negative-adjoint; L0 = −PSD)
        dd_zero=True,
        exactness="exact_integer",
        provenance_frozen=False,
        build=_build_srs_dec_set,
        consumers=("ave.topological.srs_dec_punctured",),
        note="THE canonical set. Integer incidence ∂₁/∂₂; div∘curl_adj = −∂₁∂₂ = 0 "
        "exactly for the whole field class (the curl-class charge-neutrality THEOREM).",
    ),
    OperatorSet(
        name="srs_incidence",
        carrier="srs-z3",
        module="ave.solvers.srs_cage_winding",
        adjoint_pair=True,
        adjoint_sign=+1,  # div = +Bᵀ = +gradᵀ (positive-adjoint; L_srs = BᵀDB = +PSD)
        dd_zero=False,  # a 1-complex only (no ∂₂ here); ∂∂ lives in srs_dec.
        exactness="exact_integer",
        provenance_frozen=False,
        build=_build_srs_incidence_set,
        consumers=(
            "ave.solvers.fork_b_saturation_tank",
            "ave.solvers.fork_b_near_saturation",
            "ave.solvers.spectral_liveness",
        ),
        note="Solver incidence B; reconciled B = −∂₁ᵀ to the DEC set (srs_dec.py:99-106). "
        "Solver ships the POSITIVE-adjoint convention (div = +Bᵀ, L_srs = BᵀDB = +PSD); "
        "combined with B = −∂₁ᵀ this equals the DEC div = −∂₁, so L_srs = ∂₁∂₁ᵀ = −L0. "
        "Same operator; the sign convention differs from srs_dec and is registered per-set.",
    ),
    OperatorSet(
        name="diamond_native_cage",
        carrier="diamond-z4",
        module="ave.solvers.native_cage_imex",
        adjoint_pair=True,
        adjoint_sign=+1,  # Div = +Gradᵀ exactly (positive-adjoint; L_D = GradᵀDGrad = +PSD)
        dd_zero=False,
        exactness="machine",
        provenance_frozen=True,
        build=_build_diamond_native_cage_set,
        consumers=("ave.solvers.coupled_cage_winding",),
        note="FROZEN: backs the Stage-2 native-cage DISPERSE merged verdict. Div = +Gradᵀ "
        "EXACTLY (empirically verified: Div−Gradᵀ max=0.0), so L_D = Div·D·Grad = "
        "GradᵀDGrad is +PSD symmetric — the load-bearing solver invariant. CI READS only "
        "(KEEP-BOTH); no behavior change. Carrier-tagged instrument, not the srs canon.",
    ),
    OperatorSet(
        name="gw_native",
        carrier="diamond-z4",
        module="ave.gravity.gw_propagation",
        adjoint_pair=True,
        adjoint_sign=+1,  # Div = +Gradᵀ (positive-adjoint; same build as native_cage)
        dd_zero=False,
        exactness="machine",
        provenance_frozen=True,
        build=_build_gw_native_set,
        consumers=("ave.gravity.gw_propagation.relax_finite_core_strain",),
        note="FROZEN: #86 back-reaction leg. Byte-identical native grad/div build to "
        "native_cage_imex (Div = +Gradᵀ). CI READS + certifies adjointness only.",
    ),
)


# ═════════════════════════════════════════════════════════════════════════════
# SCOPE-TAGGED heuristics (NOT registered — recorded here as the DEC-alternative
# pointer for the operators that are known-non-adjoint and MUST NOT drive a verdict)
# ═════════════════════════════════════════════════════════════════════════════
# Each entry names an operator that is deliberately NOT in OPERATOR_SETS because it
# is not an adjoint pair — with a pointer to the DEC set that supersedes it. The
# CI check asserts none of these names is imported by a LIVE solver in src/ave/.
SCOPE_TAGGED_HEURISTICS: dict[str, dict[str, str]] = {
    "_srs_curl_nodes / _srs_node_divergence": {
        "site": "src/scripts/vol_2_subatomic/em_readout_vsector_transducer.py",
        "why_not_registered": "non-adjoint (div∘curl RMS ≈ 0.35, not a machine zero); "
        "two independent Cartesian-embedded per-node 3-vector heuristics.",
        "dec_alternative": "ave.topological.srs_dec — the exact ∂₁/∂₂ pair supersedes it.",
        "status": "retired-instrument (capability-map §8b.3); scope-tagged in-place in the "
        "driver's equation_audit ledger; lives OUTSIDE src/ave/ (a driver, not a "
        "library operator). Registry records the pointer for provenance.",
    },
    "universal_topological_curl / universal_topological_divergence (Op11/Op12)": {
        "site": "src/ave/core/universal_operators.py:673,711",
        "why_not_registered": "Yee-staggered FDTD operators — E-curl and H-curl live on "
        "DIFFERENT staggered meshes, so they are NOT a mutual negative "
        "adjoint pair (by FDTD design, not a bug). Certifying div=−gradᵀ "
        "on them would be a category error.",
        "dec_alternative": "n/a for the incidence-adjoint sense; the Yee pair's own identity is "
        "the staggered curl-of-curl, not the DEC ∂∂. Cartesian-reference "
        "carrier; not a verdict-driving substrate operator.",
        "status": "reference FDTD operators; carrier=cartesian-reference; not a class-theorem "
        "operator. Recorded so the inventory is complete.",
    },
}


def registered_names() -> tuple[str, ...]:
    """The names of the registered (certified-adjoint) operator sets."""
    return tuple(s.name for s in OPERATOR_SETS)


def _adjoint_residual(grad, div, sign: int = -1) -> float:
    """‖div − sign·gradᵀ‖_max — zero iff div is the exact ±adjoint of grad.

    sign = −1 : negative-adjoint convention (div = −gradᵀ; the DEC set, L0 = −PSD).
    sign = +1 : positive-adjoint convention (div = +gradᵀ; the diamond/srs-incidence
                sets, L = +PSD). The physics invariant div∘grad = SYMMETRIC holds for
                either sign; the residual just certifies the shipped convention.

    Accepts scipy-sparse or dense; densifies the (small test-instance) difference."""
    gt = grad.T
    diff = div - sign * gt
    if hasattr(diff, "toarray"):
        diff = diff.toarray()
    diff = np.asarray(diff)
    return float(np.max(np.abs(diff))) if diff.size else 0.0


def _dd_residual(op) -> float:
    """‖op‖_max for a ∂∂ composition that must be zero (curl∘grad or div∘curl_adj)."""
    m = op.toarray() if hasattr(op, "toarray") else np.asarray(op)
    return float(np.max(np.abs(m))) if m.size else 0.0
