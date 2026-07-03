"""EM-readout Stage-2a — the self-consistent NONLINEAR .OP (the un-riggable instrument).

Prereg (FROZEN): research/2026-07-03_em-readout-stage2-redesign_prereg.md.
Charter: _orchestration/2026-07-03_em-readout-derivation-charter.md.
Grant-chartered 2026-07-03 ("ii) yes") after the Stage-1b static-linear tautology.

═══════════════════════════════════════════════════════════════════════════════
WHY THIS INSTRUMENT EXISTS (the tautology it escapes)
═══════════════════════════════════════════════════════════════════════════════
The Stage-1b finding (2026-07-03_em-readout-vsector-stage1b_result.md §3, verbatim):
"for a KNOWN imposed source, ∇·E = +(source − mean) by construction of the solve."
A LINEAR static solve `L φ = b` with a hand-assembled `b` is INFORMATIONALLY
TRANSPARENT — the enclosed-charge observable Q_enc = Σ_Ω(b − mean) returns the
source you built. It is a MIRROR, not an instrument. Grant CLOSED that cell.

THE UN-RIGGABILITY CORE (this instrument): there is NO right-hand-side source
term, EVER. The winding ω enters ONLY through the CONSTITUTIVE STATE:
  * Ax1 (axiom-definitions.md:16): each node is a shared LC tank whose
    translational (ε₀/E) and rotational (μ₀/B) reactances share the node.
  * Ax4 (universal-saturation-kernel-catalog.md:20): the local operating point
    A modulates them via S(A) = √(1 − A²).
  * The winding's ω texture (microrotational — the μ/magnetic DOF, Ax1) sets the
    local amplitude A(r); through S(A(r)) it modulates ε_eff(r) = ε₀·S(A(r)).

THE OPERATOR (the categorical difference from the closed cell): the field solves
the VARIABLE-COEFFICIENT HOMOGENEOUS PDE
      ∇·( ε_eff(r) ∇φ ) = 0        with  b ≡ 0 everywhere,
NOT a sourced Poisson equation L φ = b. A cold uniform medium (ε_eff ≡ ε₀) has
only φ ≡ const as its homogeneous solution ⇒ the ZERO FLOOR. A source-free
nonlinear medium (spatially-varying ε_eff via the winding's A(r)) can polarize:
whether it FORCES a nonzero exterior E is exactly what the substrate decides.

THE KEY PHYSICS INPUT (the A-composition, prereg §4 — FRAMING FORK, sweept):
how the ε and μ channel-amplitudes compose into the shared node's single A is
UNDERIVED in canon. Default (Q) energy-additive quadrature A² = A_ε² + A_μ²,
ENGINEERING-CHOICE-tagged, swept vs (M) μ-only and (X) max-channel. The winding
enters A_μ only (it is the μ DOF); A_ε is the field's own translational amplitude.

UN-RIGGABILITY LEDGER (every term): NO b = 𝒬·δ³, NO ∮E·dA = 𝒬/ε₀ enforced, NO
𝒬→e dictionary, NO Q_link/helicity/w_tor into the constitutive assembly. Gauss
(∇·E, ∮E·dA) is a DIAGNOSTIC only. Audited in equation_audit(). The winding
enters ONLY as the ω FIELD → A_μ(r) → S → ε_eff(r).

PROVENANCE: the srs-carrier machinery (EMEpsChannel scalar channel, the srs graph
Laplacian, the radial-fit helpers, the bond-projected curl/divergence) is COPIED
from src/scripts/vol_2_subatomic/em_readout_vsector_transducer.py (owned by
PR #479 — NOT edited there). Reconcile against #479's final version after it
merges. The COPIED pieces are the certified linear channel; the NEW physics is
the variable-coefficient ε_eff(r) operator + the S(A) constitutive assembly +
the self-consistent fixed-point solve — none of which exist in #479.
"""

from __future__ import annotations

# ── α-leak guard (the constitutive path carries NO α-carrier; a leak is a bug) ──
_FORBIDDEN_ALPHA = ("ALPHA", "ALPHA_COLD_INV", "Q_TANK", "ELECTRON", "V_SNAP")

# ── the topological quantities that must NEVER reach the constitutive assembly ──
# (audited at runtime in equation_audit(); listed here as the explicit denylist)
_FORBIDDEN_CONSTITUTIVE_INPUTS = ("Q_link", "helicity", "w_tor", "hel", "rho", "Q_delta")

import numpy as np
from scipy import sparse

from ave.core import chiral_lattice as cl

# NOTE: incremental build (implementer-dispatch discipline). Sections, one per commit:
#   1. NonlinearEMEpsChannel  — the variable-coefficient ε_eff(r) channel (this commit)
#   2. compose_A / assemble_eps_eff  — the S(A) constitutive assembly (the physics input)
#   3. solve_op_fixed_point   — Picard/Newton with damping + convergence diagnostics
#   4. validate_* (v1..v4)    — cold floor / linear limit / liveness control / stability
#   5. equation_audit + main  — the hardened exit gate; STOP at the hold-point


# ─────────────────────────────────────────────────────────────────────────────
# COPIED (with provenance) from em_readout_vsector_transducer.py (PR #479) — the
# certified well-posed srs graph Laplacian. The srs (z=3) carrier is the WELL-
# POSED carrier for a static scalar channel (nullspace = constant mode only);
# the diamond-K4 cage is BIPARTITE / ill-posed for a static scalar solve (the
# Stage-1 carrier finding). This function is UNCHANGED from #479.
# ─────────────────────────────────────────────────────────────────────────────


def _srs_graph_laplacian(net) -> "sparse.csr_matrix":
    """L = D − A (unweighted graph Laplacian) on the srs net adjacency.
    Symmetrised; nullspace = the constant mode only. COPIED from #479 (unchanged).
    Used ONLY for the cold-limit VoK cross-check; the nonlinear operator uses the
    variable-coefficient weighted form (assemble_weighted_L) instead."""
    Nn = net.n_nodes
    rows, cols = [], []
    for u in range(Nn):
        for v in net.neighbors[u]:
            rows.append(u)
            cols.append(int(v))
    A = sparse.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(Nn, Nn))
    A = 0.5 * (A + A.T)  # symmetrise (undirected)
    deg = np.asarray(A.sum(axis=1)).ravel()
    return (sparse.diags(deg) - A).tocsr()


class NonlinearEMEpsChannel:
    """The gapless EM-ε scalar channel on the chiral srs (z=3) carrier, with a
    VARIABLE-COEFFICIENT permittivity ε_eff(r) = ε₀·S(A(r)) set by the local
    operating point A(r).

    State: φ (per-node scalar potential). Field: E = −grad_graph φ (edge
    differences). Operator: the WEIGHTED graph Laplacian
        L_w = Bᵀ diag(w_edge) B      (w_edge = ε_eff on the bond = harmonic mean
                                       of the two incident node ε_eff)
    which is the discrete form of ∇·(ε_eff ∇φ). The STATIC field of the
    source-free channel is the solution of  L_w φ = 0  in the mean-zero gauge —
    which is φ ≡ const (the zero floor) UNLESS the boundary/geometry breaks the
    symmetry. There is NO right-hand-side b. The winding enters ONLY through the
    ε_eff(r) weights (via A(r)), NEVER as a source.

    NORMALISED UNITS: ε₀ ≡ 1 (dimensionless); ε_eff(r) = S(A(r)) ∈ (0, 1]. Cold
    ⇒ S ≡ 1 ⇒ L_w = L (the certified unweighted Laplacian) ⇒ φ ≡ const floor.
    """

    def __init__(self, srs_L: int = 8, enantiomorph: str = "right"):
        self.net = cl.build_srs_net(srs_L, enantiomorph)
        self.Nn = self.net.n_nodes
        self.pos = self.net.pos
        self.box = self.net.box
        self.enantiomorph = enantiomorph
        # undirected edge list (each unordered pair once) for the weighted operator
        self._edge_pairs = self._build_undirected_edges()
        # incidence B (n_edges × n_nodes), sparse: row e has +1 at u, −1 at v
        self.B = self._build_incidence()
        self.phi = np.zeros(self.Nn, dtype=np.float64)
        # the cold (unweighted) Laplacian, for the VoK cold-limit cross-check
        self.L_cold = _srs_graph_laplacian(self.net)

    def _build_undirected_edges(self) -> list[tuple[int, int]]:
        """Each unordered neighbour pair once (u < v), for the weighted operator."""
        seen = set()
        edges = []
        for u in range(self.Nn):
            for v in self.net.neighbors[u]:
                v = int(v)
                key = (u, v) if u < v else (v, u)
                if key not in seen:
                    seen.add(key)
                    edges.append(key)
        return edges

    def _build_incidence(self) -> "sparse.csr_matrix":
        """Signed incidence B: row e = (u,v) has +1 at column u, −1 at column v.
        Then Bᵀ diag(w) B is the weighted graph Laplacian ∇·(w ∇·)."""
        ne = len(self._edge_pairs)
        rows, cols, data = [], [], []
        for e, (u, v) in enumerate(self._edge_pairs):
            rows += [e, e]
            cols += [u, v]
            data += [1.0, -1.0]
        return sparse.csr_matrix((data, (rows, cols)), shape=(ne, self.Nn))

    def assemble_weighted_L(self, eps_node: np.ndarray) -> "sparse.csr_matrix":
        """L_w = Bᵀ diag(w_edge) B, the discrete ∇·(ε_eff ∇φ).

        w_edge = the HARMONIC MEAN of the two incident node permittivities
        (the series-capacitor / conductance-in-series rule — the physically-correct
        edge conductance for a variable-coefficient diffusion operator; two ε in
        series on a bond compose as the harmonic mean). LEDGER: harmonic-mean edge
        rule = AXIOM-DERIVED (series-reactance composition; the standard FV/FEM
        variable-coefficient Laplacian edge weight — the substrate-native series-LC
        rule, NOT an arbitrary average).
        """
        eps_node = np.asarray(eps_node, dtype=np.float64).reshape(self.Nn)
        w = np.empty(len(self._edge_pairs), dtype=np.float64)
        for e, (u, v) in enumerate(self._edge_pairs):
            a, b = eps_node[u], eps_node[v]
            # harmonic mean (series composition); guard against zero (S→0 at yield)
            denom = a + b
            w[e] = (2.0 * a * b / denom) if denom > 1e-300 else 0.0
        W = sparse.diags(w)
        return (self.B.T @ W @ self.B).tocsr()

    def field_E_edges(self, phi: np.ndarray | None = None) -> np.ndarray:
        """Per-edge E = −(φ[v] − φ[u]) along each undirected bond (the graph grad)."""
        p = self.phi if phi is None else phi
        return np.array([-(p[v] - p[u]) for (u, v) in self._edge_pairs])

    def node_field_mag(self, phi: np.ndarray | None = None) -> np.ndarray:
        """Per-node |E| ≈ RMS of the incident edge-gradients (radial-profile proxy).
        COPIED shape from #479 (adapted to the undirected edge list)."""
        p = self.phi if phi is None else phi
        Emag = np.zeros(self.Nn)
        cnt = np.zeros(self.Nn)
        for (u, v) in self._edge_pairs:
            e2 = (p[v] - p[u]) ** 2
            Emag[u] += e2
            Emag[v] += e2
            cnt[u] += 1
            cnt[v] += 1
        return np.sqrt(Emag / np.maximum(cnt, 1))

    def div_E_diagnostic(self, eps_node: np.ndarray,
                         phi: np.ndarray | None = None) -> np.ndarray:
        """∇·(ε_eff E) = −L_w φ (the Gauss DIAGNOSTIC — MEASURED, never enforced).
        Operator-consistent (the #479 adjoint-consistent form): uses the SAME L_w
        the field was solved with, so Σ_Ω(∇·(εE)) is the discrete flux through ∂Ω
        of the actual solved field. For a source-free solve this is machine-zero
        pointwise up to the boundary — the emergent exterior flux lives in the
        weighted field E itself, not in a residual."""
        p = self.phi if phi is None else phi
        L_w = self.assemble_weighted_L(eps_node)
        return -(L_w @ p)


# ─────────────────────────────────────────────────────────────────────────────
# 2. THE CONSTITUTIVE ASSEMBLY — the KEY PHYSICS INPUT (prereg §4).
#
#    THE MECHANISM (Stage-0 lane b, SURVIVES-to-the-fork, stage0_result.md:79-104):
#    the persistent winding imposes a STATIC STRAIN — a quiescent-point (DC)
#    displacement field in the translational sector, equilibrating outward as
#    ∇²φ = 0 exterior (the substrate analog of a lattice dislocation's static
#    strain field; the corpus's own gravity-strain n(r)=1+2GM/rc² is exactly this
#    class, master-equation.md:104). It is a FROZEN DC OFFSET, not a driven
#    oscillation and NOT a hand-source. The winding is a permanent topological
#    defect (Ax2, the loop cannot untie), so neighbouring nodes sit at a shifted
#    operating point A(r) that does not oscillate.
#
#    HOW THE TEXTURE POLARIZES WITHOUT A SOURCE (the un-riggable core): the
#    winding's ω texture sets the local operating point A(r); through S(A(r)) it
#    modulates ε_eff(r) = ε₀·S(A(r)). The DC-offset field φ is the equilibrium of
#    the variable-coefficient homogeneous operator ∇·(ε_eff(r) ∇φ) = 0 UNDER THE
#    QUIESCENT-STRAIN BOUNDARY the texture imposes. The polarization is the
#    bound-charge ρ_b = −∇·P of the graded medium relaxing its own reactive
#    energy — there is NO free-charge source. Whether the graded ε_eff(r) forces
#    a nonzero exterior φ is exactly what the substrate decides (prereg §2).
#
#    ⚠ THE A-COMPOSITION FORK (prereg §4.3 — FRAMING, surfaced to Grant, SWEPT):
#    how the ε and μ channel-amplitudes compose into the shared node's single A is
#    UNDERIVED in canon. CANON USES PER-CHANNEL INDEPENDENT KERNELS (Meissner-
#    asymmetric, l3-electron-soliton-synthesis.md:138): S_μ=√(1−A_μ²) vs
#    S_ε=√(1−A_ε²), two independent kernels under asymmetric drive. The winding
#    biases A_μ (it is the microrotational/μ DOF, axiom-definitions.md:16).
#
#    ⚠⚠ THE SHARP OPERATOR CONSEQUENCE I MUST SURFACE (flag-don't-fix): the SCALAR
#    EM-ε channel operator ∇·(ε_eff ∇φ) sees ε_eff = ε₀·S_ε — the ε-CHANNEL kernel.
#    Under canon's ASYMMETRIC rule (M), a STATIC winding loads S_μ ONLY (there is
#    no ∂B/∂t to load ε; CLAUDE.md:75: "a static field has no ∂B/∂t to load the μ
#    sector" — and its converse, a static μ-texture doesn't load ε without the
#    shared-node transducer). Then S_ε ≡ 1, ε_eff ≡ ε₀, the scalar operator is
#    UNMODULATED, and φ ≡ const STRUCTURALLY ⇒ [NO-FLUX] by construction of the
#    sector-separation. The winding reaches the ε-channel ONLY through the shared-
#    node ε↔μ LC coupling (the transducer) — which in the STATIC case canon says
#    does NOT fire (no ∂B/∂t). So the STATIC .OP (Stage-2a) STRUCTURALLY LEANS
#    [NO-FLUX] under rule (M); the DYNAMICAL settler (Stage-2b, where ∂B/∂t exists)
#    is where transduction can fire. This is a rule-DEPENDENT verdict — the
#    [STUCK-FRAMING] the charter predicted. THEREFORE the instrument implements ALL
#    THREE rules and lets the substrate decide per-rule; the tension is HEADLINED
#    in the hold-point report, NOT silently coded around.
#
#    LEDGER (every constitutive term):
#      A_μ(r) = amp·|ω(r)|/ω_ref .......... AXIOM-DERIVED (ω is the μ₀ DOF,
#          axiom-definitions.md:16; the microrotation magnitude the μ reactance
#          sees). ENGINEERING-CHOICE: |ω| vs |∇×ω| (f1/f2, swept); ω_ref scale.
#      A_ε(r): the field's own translational amplitude — in the static .OP with no
#          external E, A_ε starts at 0; rule (Q) injects A_μ into A_ε via quadrature
#      A(r) = compose(A_ε, A_μ) ........... ENGINEERING-CHOICE (the FORK §4.3):
#          (Q) √(A_ε²+A_μ²) quadrature / (M) A_μ-only per-channel / (X) max — swept
#      S(A) = √(1−A²) .................... AXIOM-DERIVED (Ax4 kernel, INVARIANT-S2)
#      ε_eff = ε₀·S(A) (ε₀≡1) ............ AXIOM-DERIVED (vocabulary-register.md:423)
#      A_μ from Q_link/helicity/w_tor .... FORBIDDEN-INSERTION — NOT used (the
#          winding enters as the ω FIELD only; NO integer invariant; audited §5)
# ─────────────────────────────────────────────────────────────────────────────


def compose_A(A_eps: np.ndarray, A_mu: np.ndarray, rule: str = "Q") -> np.ndarray:
    """Compose the per-channel amplitudes into the shared node's single operating
    point A (prereg §4.3 FORK — ENGINEERING-CHOICE, swept). Clamped to [0, 1).

    rule="Q": energy-additive quadrature  A = √(A_ε² + A_μ²)   (my recommended
              default — total reactive energy sets the operating point; the ε
              channel DOES pick up the winding's μ amplitude ⇒ ε_eff modulates).
    rule="M": μ-channel-only per-channel   A = A_μ  (canon's Meissner-asymmetric
              two-independent-kernels reading; for the ε-channel operator this
              means A_ε is set by A_ε ALONE — see compose_A_for_eps_channel).
    rule="X": max / dominant-channel       A = max(A_ε, A_μ)  (sharp-corner).
    """
    A_eps = np.asarray(A_eps, dtype=np.float64)
    A_mu = np.asarray(A_mu, dtype=np.float64)
    if rule == "Q":
        A = np.sqrt(A_eps**2 + A_mu**2)
    elif rule == "M":
        A = A_mu.copy()
    elif rule == "X":
        A = np.maximum(A_eps, A_mu)
    else:
        raise ValueError(f"unknown A-composition rule {rule!r} (expected Q/M/X)")
    # clamp strictly below yield so S(A) = √(1−A²) stays real and > 0
    return np.clip(A, 0.0, 1.0 - 1e-9)


def eps_channel_operating_point(A_eps: np.ndarray, A_mu: np.ndarray,
                                rule: str) -> np.ndarray:
    """The operating point the ε-CHANNEL kernel S_ε sees (ε_eff = ε₀·S_ε).

    THIS is where the sharp operator consequence lives (the ⚠⚠ note above):
      rule="Q": the ε-channel sees the COMPOSED A (quadrature) ⇒ the winding's A_μ
                DOES modulate ε_eff ⇒ the scalar operator is textured ⇒ can polarize.
      rule="M": the ε-channel sees A_ε ONLY (canon's per-channel Meissner-asymmetric
                reading) ⇒ a static μ-only winding leaves ε_eff ≡ ε₀ (cold) ⇒ φ≡const
                STRUCTURALLY (the [NO-FLUX] lean — surfaced, not coded around).
      rule="X": the ε-channel sees max(A_ε, A_μ) ⇒ modulates when A_μ dominates.

    The instrument runs all three; the substrate decides. The rule-dependence IS
    the surfaced framing fork.
    """
    if rule == "M":
        # per-channel: the ε kernel sees only the ε amplitude (μ-only winding ⇒ cold ε)
        return np.clip(np.asarray(A_eps, dtype=np.float64), 0.0, 1.0 - 1e-9)
    # Q and X: the composed operating point modulates the ε channel
    return compose_A(A_eps, A_mu, rule)


def saturation_S(A: np.ndarray) -> np.ndarray:
    """The Axiom-4 universal saturation kernel S(A) = √(1 − A²) (INVARIANT-S2;
    universal-saturation-kernel-catalog.md:20). A ∈ [0,1); S ∈ (0,1]. Cold A=0 ⇒
    S=1 (the certified linear medium); yield A→1 ⇒ S→0 (ε_eff → 0, the wall).
    AXIOM-DERIVED — the Born–Infeld n=2 squared-limit form, no free parameter."""
    A = np.clip(np.asarray(A, dtype=np.float64), 0.0, 1.0 - 1e-12)
    return np.sqrt(1.0 - A**2)


# ─────────────────────────────────────────────────────────────────────────────
# COPIED (with provenance) from em_readout_vsector_transducer.py (PR #479) — the
# bond-projected curl F=∇×ω, for the (f2) A_μ map. UNCHANGED from #479.
# ─────────────────────────────────────────────────────────────────────────────


def _srs_curl_nodes(net, omega: np.ndarray) -> np.ndarray:
    """F = ∇×ω on the srs node cloud (bond-projected curl). Per-node 3-vector.
    (∇×ω)[u] ≈ Σ_{v∈nbr(u)} ê_{u→v} × (ω[v] − ω[u]) / |bonds|. Substrate-native
    (NOT Cartesian). COPIED from #479 (unchanged)."""
    Nn = net.n_nodes
    F = np.zeros((Nn, 3))
    for u in range(Nn):
        acc = np.zeros(3)
        nb = net.neighbors[u]
        for pp, v in enumerate(nb):
            ehat = net.bond_unit[u][pp]
            acc += np.cross(ehat, omega[int(v)] - omega[u])
        F[u] = acc / max(len(nb), 1)
    return F


def winding_A_mu(net, omega: np.ndarray, amplitude: float,
                 field: str = "omega") -> np.ndarray:
    """The winding's μ-channel operating-point field A_μ(r) — the ONLY way the
    winding enters the constitutive state (prereg §4.4). NO Link integer, NO
    helicity, NO w_tor: the winding enters as the ω FIELD only (audited §5).

    field="omega": A_μ(r) = amplitude · |ω(r)| / max|ω|   (DEFAULT — ω IS the μ₀
                   DOF directly, axiom-definitions.md:16; the microrotation
                   magnitude the μ reactance sees). AXIOM-DERIVED source-field;
                   the normalisation-to-peak + `amplitude` knob is ENGINEERING-
                   CHOICE (the regime control — amplitude = the peak A_μ, prereg §7).
    field="curl": A_μ(r) = amplitude · |∇×ω(r)| / max|∇×ω|  (SWEPT — the substrate
                   flux F=∇×ω, the B-analog; the Link-carrying flux magnitude).

    Returns A_μ ∈ [0, amplitude], peak = amplitude at the winding's densest node.
    """
    if field == "omega":
        mag = np.linalg.norm(np.asarray(omega, dtype=np.float64), axis=1)
    elif field == "curl":
        mag = np.linalg.norm(_srs_curl_nodes(net, omega), axis=1)
    else:
        raise ValueError(f"unknown A_mu field {field!r} (expected omega/curl)")
    peak = float(np.max(mag))
    if peak < 1e-300:
        return np.zeros_like(mag)
    return np.clip(amplitude * mag / peak, 0.0, 1.0 - 1e-9)


# ─────────────────────────────────────────────────────────────────────────────
# 3. THE SELF-CONSISTENT FIXED-POINT SOLVE (the .OP — Picard with damping).
#
#    THE FIXED-POINT STRUCTURE (the DC state the SYSTEM finds, not hand-assembled):
#      * A_μ(r) is FIXED by the winding texture (the permanent defect — |ω| does
#        not change; the frozen DC bias, Stage-0 lane b).
#      * A_ε(r) is SELF-CONSISTENT: set by the field's OWN amplitude |E| = |∇φ|
#        (the translational amplitude the ε channel carries).
#      * ε_eff(r) = ε₀·S_ε(r), S_ε from eps_channel_operating_point(A_ε, A_μ, rule).
#      * φ relaxes toward the QUIESCENT-STRAIN OFFSET the texture imposes: the
#        winding's operating-point field is a per-node DC target (Stage-0 lane b:
#        "neighbouring nodes sit at a shifted operating point"); the scalar field
#        equilibrates as the variable-coefficient Laplace of that imposed offset.
#
#    THE OPERATOR (source-free, un-riggable): φ solves the constrained energy
#    minimisation  min_φ ½ Σ_edge w_edge (Δφ)²  s.t. the texture-offset boundary —
#    i.e. ∇·(ε_eff ∇φ) = 0 in the interior, with the winding's DC-offset field as
#    the inhomogeneous quiescent target. Implemented as: the frozen offset τ(r)
#    (the winding's operating-point field, a per-node DC bias in NORMALISED units)
#    enters as an ANCHOR, and φ minimises ½Σw(Δφ)² + κΣ(φ−τ)² pull-to-anchor with
#    κ→0⁺ (the anchor selects the physical branch of the const-null gauge; the
#    FIELD that emerges is the variable-coefficient harmonic extension of the
#    texture, NOT a hand-source). LEDGER: the anchor τ = the winding's A_μ field
#    (AXIOM-DERIVED — the frozen DC operating-point offset, Stage-0 lane b); κ is a
#    gauge-fixing infinitesimal (ENGINEERING-CHOICE, swept → 0; the RESULT is
#    κ-independent in the limit, asserted in v4). NO b=𝒬δ³. The anchor is a
#    per-node operating-point SHIFT (a constitutive boundary), never a charge.
#
#    ⚠ Under rule (M) with a μ-only winding, ε_eff ≡ ε₀ (cold) AND the anchor τ is
#    a pure gauge offset the harmonic extension flattens ⇒ φ → const ⇒ [NO-FLUX].
#    Under rule (Q)/(X) the graded ε_eff(r) makes the harmonic extension of τ
#    NON-constant ⇒ a real exterior field can emerge. This is the surfaced fork.
# ─────────────────────────────────────────────────────────────────────────────


def solve_op_fixed_point(ch: "NonlinearEMEpsChannel", A_mu: np.ndarray, *,
                         rule: str = "Q", kappa: float = 1e-6,
                         damping: float = 0.5, max_iter: int = 200,
                         tol: float = 1e-9, verbose: bool = False) -> dict:
    """Solve the self-consistent nonlinear .OP: find the DC field φ the graded
    medium settles to under the winding's frozen operating-point offset. NO RHS
    source — the winding enters ONLY through A_mu → ε_eff(r) and the DC-offset
    anchor. Picard iteration with damping; convergence diagnostics exported.

    Returns the converged φ, the ε_eff / S_ε fields, and the full residual history
    (the #479 lesson: no unchecked solver info — every iteration's residual and
    the final cg_info are exported and the caller ASSERTS convergence)."""
    from scipy.sparse.linalg import cg

    Nn = ch.Nn
    A_mu = np.asarray(A_mu, dtype=np.float64).reshape(Nn)
    # the frozen DC-offset anchor τ = the winding's operating-point field, mean-zero
    # (only gradients of A are physical, CLAUDE.md:75 — subtract the mean so τ is a
    # pure texture, no absolute-bias smuggling). This is the quiescent strain the
    # permanent defect imposes (Stage-0 lane b), NOT a source.
    tau = A_mu - A_mu.mean()

    phi = np.zeros(Nn, dtype=np.float64)
    A_eps = np.zeros(Nn, dtype=np.float64)     # the field's own translational amp
    residuals = []
    cg_infos = []
    kappa_diag = sparse.diags(np.full(Nn, kappa))

    for it in range(max_iter):
        # 1) constitutive assembly: ε_eff(r) = ε₀·S_ε from the CURRENT A_ε and the
        #    fixed A_μ, per the composition rule (the KEY physics input)
        A_eps_seen = eps_channel_operating_point(A_eps, A_mu, rule)
        S_eps = saturation_S(A_eps_seen)
        eps_eff = S_eps                          # ε₀ ≡ 1 (normalised units)
        # 2) assemble the variable-coefficient operator + the gauge-fixing anchor
        L_w = ch.assemble_weighted_L(eps_eff)
        M = (L_w + kappa_diag).tocsr()
        b = kappa * tau                          # anchor RHS: κ(φ−τ) pull, NOT a charge
        # 3) solve the linear system for THIS ε_eff (one Picard sub-solve)
        phi_new, info = cg(M, b, x0=phi, rtol=1e-11, maxiter=40000)
        cg_infos.append(int(info))
        phi_new = phi_new - phi_new.mean()       # mean-zero (physical) gauge
        # 4) damped update of the self-consistent field
        phi_upd = (1.0 - damping) * phi + damping * phi_new
        res = float(np.max(np.abs(phi_upd - phi)))
        residuals.append(res)
        phi = phi_upd
        # 5) update the field's own translational amplitude A_ε = |E| = |∇φ|
        #    (self-consistent — the ε channel's own amplitude, normalised to yield)
        Emag = ch.node_field_mag(phi)
        emax = float(np.max(Emag))
        A_eps = np.clip(Emag / emax, 0.0, 1.0 - 1e-9) * (A_mu.max() if A_mu.max() > 0 else 0.0) \
            if emax > 1e-300 else np.zeros(Nn)
        if verbose and (it % 20 == 0 or res < tol):
            print(f"  it={it:3d} res={res:.3e} cg_info={info} maxS={S_eps.max():.4f} minS={S_eps.min():.4f}")
        if res < tol and it > 1:
            break

    ch.phi = phi
    converged = bool(res < tol and cg_infos[-1] == 0)
    return {
        "phi": phi,
        "eps_eff": eps_eff,
        "S_eps": S_eps,
        "A_eps": A_eps,
        "tau": tau,
        "rule": rule,
        "kappa": kappa,
        "n_iter": len(residuals),
        "final_residual": residuals[-1] if residuals else float("nan"),
        "residual_history": residuals,
        "cg_info_final": cg_infos[-1] if cg_infos else -1,
        "cg_info_any_nonzero": bool(any(c != 0 for c in cg_infos)),
        "converged": converged,
        "S_eps_min": float(S_eps.min()),
        "S_eps_max": float(S_eps.max()),
    }
