"""EM-readout Stage-1 — the TRANSDUCER build (winding → gapless EM-ε channel).

Prereg (FROZEN + dated correction): research/2026-07-03_em-readout-vsector-stage1_prereg.md.
Charter: _orchestration/2026-07-03_em-readout-derivation-charter.md.
Grant-CONFIRMED target-(1): build the transducer (NOT a new longitudinal scalar).

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS IS (and is NOT)
═══════════════════════════════════════════════════════════════════════════════
Adds the gapless EM-ε (transverse-T2 electric-displacement) channel as a static
scalar potential φ_EM on the NATIVE K4 tetrahedral stencil, and the TRANSDUCER
coupling by which the winding's substrate flux F = ∇×ω sources it — where the
coupling traces ONLY to Axiom-1's node rotation↔translation LC structure, NEVER
a hand-written ρ-source or a 𝓠→e dictionary.

MISSION (Grant): EMERGENCE IS THE GOAL. Gauss-as-link-counting (∮E·dA = 𝒬) must
EMERGE from the axiom-native coupling. If it does NOT emerge, that is the honest
stakes-table result (charter §2) — booked, no rescue, no hand-wire.

THE GAPLESS / STATIC-CURL-FREE PAIR (prereg correction item 2, historical-
precedents.md:21): the EM-ε channel MUST support the static curl-free E component
(∇·E = the Coulomb-longitudinal field a static charge sources) while having NO
propagating longitudinal mode. The equation-audit asserts this pair:
  static_curl_free_supported / propagating_longitudinal_absent.

RULE-14 (reuse certified cores, do not rebuild):
  * native tetrahedral Grad/Div + divergence-form Laplacian
        → ave.solvers.native_cage_imex.{build_grad_div_periodic, assemble_L_D}
  * the substrate flux F = ∇×ω + the boundary Link integer 𝒬 = Link(∂Ω,F)
        → ave.topological.charge_quantization.{compute_F_curl, compute_Q_link}
  * the (2,3) winding seed
        → ave.solvers.coupled_cage_winding seeding (ω is its OWN DOF, never grad V)

UN-RIGGABILITY (charter §3, prereg §4): every update-equation term carries a
ledger tag AXIOM-DERIVED / ENGINEERING-CHOICE / FORBIDDEN-INSERTION. FORBIDDEN:
any ρ = 𝒬·δ³ source; any ∮E·dA = 𝒬/ε₀ enforced constraint; any 𝒬→e dictionary
wired by hand. Gauss (∇·E, ∮E·dA) is a DIAGNOSTIC only — measured, never enforced.
"""

from __future__ import annotations

# ── α-leak guard (the coupling path carries NO α-carrier; the leak is the signal) ──
_FORBIDDEN_ALPHA = ("ALPHA", "ALPHA_COLD_INV", "Q_TANK", "ELECTRON", "V_SNAP")

# NOTE: incremental build — the per-role functions are appended one per commit
# (skeleton first). Order:
#   1. build_em_eps_channel        — the gapless EM-ε scalar φ on the native K4 stencil
#   2. validate_zero_source        — VoK (a): zero-source → identically zero (clean floor)
#   3. validate_green_function     — VoK (b): KNOWN imposed boundary flux → 1/r outside
#   4. validate_superposition      — VoK (c): two imposed fluxes → fields add, ∮ counts
#   5. axiom1_lc_transducer        — the Ax1 rotation↔translation LC coupling ω-flux → φ_EM
#   6. measure_gauss_diagnostic    — ∮E·dA and ∇·E of what EMERGES (diagnostic, not enforced)
#   7. equation_audit              — the exit gate: every term tagged; no inserted source

import numpy as np

from ave.solvers.native_cage_imex import assemble_L_D, build_grad_div_periodic


# ─────────────────────────────────────────────────────────────────────────────
# 1. THE GAPLESS EM-ε CHANNEL — a static scalar potential φ_EM on the native K4
#    tetrahedral stencil. The channel operator is the NATIVE divergence-form
#    Laplacian L = Div·Grad (D=1 ⇒ COLD / S=1 / GAPLESS — no mass term, no ω_gap).
#    LEDGER:
#      L = Div·Grad on TETRA_OFFSETS ............... AXIOM-DERIVED (Ax1 K4 stencil;
#          the native tetrahedral Grad/Div, NOT the forbidden Cartesian 7-pt HR1;
#          reused verbatim from native_cage_imex, Rule-14)
#      D = 1 (gapless) ............................. AXIOM-DERIVED (cold far-zone
#          A→0 ⇒ S→1; the EM-ε channel is Γ_EM=0 matched/gapless by the
#          three-impedance law — NO mass term smuggled in)
#    GAPLESS/STATIC-CURL-FREE PAIR: L = Div·Grad is a pure Laplacian (∇²) — its
#    static solution space is the harmonic/curl-free E = −∇φ (Coulomb-longitudinal,
#    RETAINED by Gauss per historical-precedents.md:21). It carries NO time
#    derivative ⇒ NO propagating mode of ANY polarization ⇒ trivially no
#    propagating LONGITUDINAL mode. The pair is asserted structurally here and
#    audited in equation_audit().
# ─────────────────────────────────────────────────────────────────────────────


class EMEpsChannel:
    """The gapless EM-ε electric-scalar channel on the native K4 stencil.

    State: φ (N³ scalar potential). Field: E = −Grad φ (native tetrahedral grad).
    Operator: L = Div·Grad (D=1, SPD, gapless). The STATIC field of a source b is
    the solution of L φ = b (Poisson-form) — but b is NEVER a hand-written ρ; it
    is EITHER a KNOWN imposed boundary flux (validate-on-known, legitimately
    imposed + labeled) OR the emergent transducer output (axiom1_lc_transducer).
    """

    def __init__(self, N: int):
        self.N = int(N)
        self.ndof = self.N**3
        self.Grad, self.Div = build_grad_div_periodic(self.N)
        # D=1 everywhere ⇒ gapless cold channel. The native Laplacian L=Div·Grad.
        self.D = np.ones(self.ndof, dtype=np.float64)
        self.L = assemble_L_D(self.Grad, self.Div, self.D)  # SPD native ∇²
        self.phi = np.zeros(self.ndof, dtype=np.float64)

    def field_E(self, phi: np.ndarray | None = None) -> np.ndarray:
        """E = −Grad φ (native tetrahedral gradient, shape (3·ndof,))."""
        p = self.phi if phi is None else phi
        return -(self.Grad @ p)

    def div_E(self, phi: np.ndarray | None = None) -> np.ndarray:
        """∇·E = −Div·Grad φ = −L φ (the Gauss DIAGNOSTIC — measured, not enforced)."""
        p = self.phi if phi is None else phi
        return -(self.L @ p)

    def solve_static(self, source: np.ndarray) -> np.ndarray:
        """Solve L φ = source (the static/Laplace solve; CG on the SPD native L).

        `source` is the RHS. For validate-on-known it is a KNOWN imposed flux
        (labeled). For the transducer it is the emergent Ax1-LC output. This
        method does NOT know or care which — it is the channel's own gapless
        static dynamics, sourced from outside. NO ρ is fabricated here.
        """
        from scipy.sparse.linalg import cg

        b = np.asarray(source, dtype=np.float64).reshape(self.ndof)
        # zero-mean gauge (periodic Laplacian has a constant null space); project
        # both RHS and solution to the mean-zero subspace (the physical gauge).
        b = b - b.mean()
        phi, info = cg(self.L, b, rtol=1e-10, maxiter=5000)
        phi = phi - phi.mean()
        self.phi = phi
        return phi


# ─────────────────────────────────────────────────────────────────────────────
# 2. VALIDATE-ON-KNOWN (a) — ZERO-SOURCE FLOOR. Zero source ⇒ identically zero
#    φ and E (the clean floor: no spurious field; the channel invents nothing).
# ─────────────────────────────────────────────────────────────────────────────


def validate_zero_source(N: int = 24) -> dict:
    """VoK (a): zero source → φ ≡ 0, E ≡ 0 exactly. No spurious field."""
    ch = EMEpsChannel(N)
    phi = ch.solve_static(np.zeros(ch.ndof))
    E = ch.field_E()
    return {
        "test": "zero_source_floor",
        "max_abs_phi": float(np.max(np.abs(phi))),
        "max_abs_E": float(np.max(np.abs(E))),
        "stays_zero": bool(np.max(np.abs(phi)) < 1e-12
                           and np.max(np.abs(E)) < 1e-12),
    }

