"""Vacuum-Varactor Scatter Operator — the S(A)-READING admittance scatter.

Prereg / context: research/2026-06-20_vacuum-varactor-scatter_result.md
Built off origin/main @ 32f29c67 (bedrock node_scattering_multiplicity.py via PR#304).

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS MODULE IS (and is NOT)
═══════════════════════════════════════════════════════════════════════════════
GOAL  : make the trivalent shunt-junction scatter READ the local saturation S(A),
        wiring the canonical Axiom-4 varactor coupling (C_eff = C0 / S, i.e. the
        LONGITUDINAL μ-load) into the operator. Today chiral_lattice.scatter_matrix
        (chiral_lattice.py:81-102) IGNORES its z_local arg -- an unimplemented
        docstring promise -- so the operator is SATURATION-BLIND (the Fork-B NO-GO
        Finding: the dead-code path). This module gives it eyes.

NOT   : the Fork-B confinement verdict (does the saturation tank confine the A1
        mass?) and the quarter-arc shape discriminator are EXPLICITLY OUT OF SCOPE.
        This module delivers ONLY the S(A)-reading operator + its four
        validate-on-known gates + the scramble-changes-operator demonstration.

═══════════════════════════════════════════════════════════════════════════════
THE CORE CHANGE — admittance-weighted scatter
═══════════════════════════════════════════════════════════════════════════════
The bedrock scatter is the EQUAL-ADMITTANCE shunt-junction reduction
S_ij = (2/n) - delta_ij  (chiral_lattice.py:89, V = (2/n) Σ_j V_j^inc).
This module implements the ADMITTANCE-WEIGHTED generalization:

    S_ij = 2 Y_j / (Σ_k Y_k) - delta_ij                                   (1)

derived from the SAME shunt-junction KCL with PER-PORT admittance Y_i:
    V_i = V_i^inc + V_i^ref = V  (common node voltage, shunt)
    Σ_i Y_i (V_i^inc - V_i^ref) = 0  (KCL)
    => V = (2 Σ_j Y_j V_j^inc) / (Σ_k Y_k)
    => S_ij = 2 Y_j / (Σ_k Y_k) - delta_ij.
Setting all Y_j equal recovers (2/n)J - I EXACTLY (gate 1, the bedrock).

═══════════════════════════════════════════════════════════════════════════════
THE VARACTOR MAP (canonical Axiom-4)
═══════════════════════════════════════════════════════════════════════════════
Bond admittance:    Y_bond = Y0 / sqrt(S(A_bond))                          (2)
Bond impedance:     Z_bond = Z0 * sqrt(S(A_bond))                          (3)
Saturation kernel:  S(A) = sqrt(1 - (A/A_yield)^2)   [crystal_engine.py:191, IMPORTED]

As the core SATURATES (S -> 0):  Z_bond -> 0  =>  Gamma -> -1  (the mass cage,
the Z->0 SHORT, the corrected sign -- NOT a Z->inf bag). This is the LONGITUDINAL
μ-LOAD (Z_eff = Z0*sqrt(S), crystal_engine.py:466-478), NOT the FORBIDDEN ε-load
(Z_eff = Z0/sqrt(S) -> inf, Gamma=+1; crystal_engine.py:466-468 SCOPE ASSERTION).

═══════════════════════════════════════════════════════════════════════════════
PER-BOND, NOT PER-NODE (load-bearing — Fork-B NO-GO Finding 2)
═══════════════════════════════════════════════════════════════════════════════
A per-NODE-UNIFORM admittance CANCELS at the shunt junction: in (1) a common
factor Y in every Y_j cancels in 2 Y_j / Σ_k Y_k, reducing back to (2/n)J - I
REGARDLESS of S. So the saturation MUST enter as PER-BOND (directed-edge)
admittances that DIFFER across ports (the S-gradient across the connect-map),
or the operator stays S-blind. This module applies S per directed bond and
VERIFIES the cancellation explicitly (per-node-uniform load MUST NOT change the
scatter; per-bond-varying load MUST).

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-NATIVE-CHECK (walked BEFORE any numerical code, operating principle 1)
═══════════════════════════════════════════════════════════════════════════════
  * K4 / graph   : (1) is the Op5 shunt KCL with per-port admittance, composed
                   with the lattice's OWN directed-edge CONNECT permutation
                   (connect_index, chiral_lattice.py:133-147). Built FROM the
                   bond-graph, never a Cartesian posit.
  * Cosserat     : the varactor reads the A1 DILATATION saturation S(A) (bulk /
                   longitudinal sector). The (2,3) WINDING (charge-3) is NOT wired
                   in -- A1 ⊥ T2 honoured (master-equation.md:20).
  * phase vs real: the scatter lives in n-PORT amplitude space = the (V_inc,V_ref)
                   phasor coordinates, the MATCHING coordinates for the impedance.
                   S enters as a dimensionless per-bond admittance weight, NOT a
                   real-space Cartesian field compared against phi^2.
  * Op14         : S(A)=sqrt(1-A^2) is the canonical kernel, IMPORTED from
                   crystal_engine (NOT hardcoded). The map Y=Y0/sqrt(S) is the
                   μ-LOAD giving Z->0/Gamma=-1 (crystal_engine.py:478), NOT the
                   FORBIDDEN ε-load (crystal_engine.py:466-468).
  * alpha-free   : the scatter takes dimensionless A_bond (=|V|/V_yield) so
                   V_yield (and hence ALPHA, which sits ONLY in the dimensionful
                   V_YIELD=sqrt(ALPHA)*V_SNAP at constants.py:427) CANCELS. ALPHA
                   is NEVER imported here. alpha-invariance is STRUCTURAL.
  * no-phasor    : the A1 scalar stays COMMON-MODE; the varactor is the
                   longitudinal C_eff=C0/S μ-load. The winding is not wired into
                   the breather's own (V_inc,V_ref) phasor (master-equation.md:20).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ave.core.chiral_lattice import LatticeNet, scatter_matrix
from ave.core.crystal_engine import CrystalEngine

# ─────────────────────────────────────────────────────────────────────────────
# ANTI-LEAK IMPORT-GUARD: the varactor scatter is alpha-FREE BY CONSTRUCTION.
# It reads a DIMENSIONLESS saturation amplitude A=|V|/V_yield per bond, so the
# alpha-carrying dimensionful V_YIELD (=sqrt(ALPHA)*V_SNAP, constants.py:427)
# CANCELS and never enters. No ALPHA / Q_TANK / ELECTRON carrier may be reachable.
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "alpha-leak: ALPHA must NOT be imported into the varactor scatter"
assert "Q_TANK" not in globals(), "alpha-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "ELECTRON" not in globals(), "alpha-leak: ELECTRON instance must NOT be imported"


# ═════════════════════════════════════════════════════════════════════════════
# 1. CANONICAL S(A) KERNEL — IMPORTED, not hardcoded (ave-canonical-source)
# ═════════════════════════════════════════════════════════════════════════════
# A single, minimal, alpha-FREE engine instance used SOLELY as the canonical
# kernel provider. V_yield=1.0 (engine-natural units) so A is dimensionless and
# the alpha-carrying dimensionful V_YIELD (constants.py:427) never enters. N=2 is
# the smallest legal grid; we never step it -- we call ONLY saturation_kernel.
_KERNEL_ENGINE = CrystalEngine(N=2, V_yield=1.0, A_cap=0.99, S_min=0.05, converter_on=False)


def saturation_kernel(A: np.ndarray, *, A_cap: float | None = None, S_min: float | None = None) -> np.ndarray:
    """Canonical Axiom-4 saturation kernel S(A) = sqrt(1 - A^2), clipped to
    [S_min, 1] at A_cap (crystal_engine.py:191, the A-034 kernel).

    IMPORTED, NOT hardcoded (ave-canonical-source): this delegates to
    CrystalEngine.saturation_kernel via a minimal alpha-free engine instance, so
    the EXACT canonical arithmetic (clip at A_cap, floor at S_min) is reused.

    A is the DIMENSIONLESS saturation amplitude |V|/V_yield in [0, A_cap]. Because
    A is dimensionless, V_yield -- and therefore ALPHA (which lives ONLY in the
    dimensionful V_YIELD=sqrt(ALPHA)*V_SNAP) -- CANCELS. alpha-FREE.

    A_cap / S_min override the engine clip/floor for testing the bare-limit
    behaviour; default None uses the canonical engine values (0.99 / 0.05)."""
    A = np.asarray(A, dtype=np.float64)
    eng = _KERNEL_ENGINE
    if A_cap is not None or S_min is not None:
        eng = CrystalEngine(
            N=2,
            V_yield=1.0,
            A_cap=eng.A_cap if A_cap is None else float(A_cap),
            S_min=eng.S_min if S_min is None else float(S_min),
            converter_on=False,
        )
    # saturation_kernel reads A = |V|/V_yield; with V_yield=1.0, pass V = A.
    return eng.saturation_kernel(A)


# ═════════════════════════════════════════════════════════════════════════════
# 2. PER-PORT ADMITTANCE -> ADMITTANCE-WEIGHTED LOCAL SCATTER  (the core change)
# ═════════════════════════════════════════════════════════════════════════════
def admittance_scatter(Y: np.ndarray) -> np.ndarray:
    """Admittance-weighted shunt-junction scatter S_ij = 2 Y_j/(Σ_k Y_k) - δ_ij.

    Y is the (n,) per-PORT admittance vector. Derived from the SAME Op5 shunt KCL
    as the bedrock, with per-port admittance retained instead of factored out:

        V_i = V_i^inc + V_i^ref = V  (shunt: common node voltage)
        Σ_i Y_i (V_i^inc - V_i^ref) = 0  (KCL)
        => V = 2 (Σ_j Y_j V_j^inc) / (Σ_k Y_k)
        => V_i^ref = V - V_i^inc  => S_ij = 2 Y_j/(Σ_k Y_k) - δ_ij.

    EQUAL admittance (all Y_j = Y) gives 2 Y/(nY) - δ_ij = (2/n) - δ_ij = the
    bedrock (2/n)J - I EXACTLY -- a UNIFORM admittance (even a saturated one)
    CANCELS (the per-node-uniform no-op, the load-bearing Fork-B Finding 2). A
    per-PORT-VARYING Y is what makes the scatter read saturation.

    Returns the (n,n) scatter matrix. alpha-FREE (linear algebra on Y only)."""
    Y = np.asarray(Y, dtype=np.float64).ravel()
    n = Y.shape[0]
    if n < 2:
        raise ValueError("Y must have length >= 2 (an n-port node, n>=2)")
    Ysum = Y.sum()
    if not np.isfinite(Ysum) or Ysum <= 0.0:
        raise ValueError("Σ Y must be finite and positive (passive shunt junction)")
    # S_ij = 2 Y_j / Σ_k Y_k - δ_ij : row-broadcast of the admittance fractions.
    S = (2.0 / Ysum) * np.broadcast_to(Y, (n, n)).copy() - np.eye(n, dtype=np.float64)
    return S


def bond_admittance_from_saturation(A_bond: np.ndarray, *, Y0: float = 1.0) -> np.ndarray:
    """The VARACTOR MAP: bond admittance Y_bond = Y0 / sqrt(S(A_bond)).

    S(A) is the canonical Axiom-4 kernel (saturation_kernel, IMPORTED). As the core
    saturates (S -> 0): Y_bond -> inf, Z_bond = Z0*sqrt(S) -> 0 => Gamma -> -1 (the
    mass cage, the Z->0 SHORT -- the corrected sign; the LONGITUDINAL mu-load, NOT
    the forbidden epsilon-load whose Y=Y0*sqrt(S)->0 / Z->inf gives Gamma=+1).

    A_bond is the dimensionless per-bond saturation amplitude |V_bond|/V_yield.
    Returns Y_bond, same shape as A_bond. alpha-FREE (dimensionless A)."""
    S = saturation_kernel(np.asarray(A_bond, dtype=np.float64))
    return Y0 / np.sqrt(S)


# ═════════════════════════════════════════════════════════════════════════════
# 3. GLOBAL S(A)-READING SCATTER on the actual lattice CONNECT map
# ═════════════════════════════════════════════════════════════════════════════
def _normalize_A_bond(net: LatticeNet, A_bond) -> np.ndarray:
    """Coerce A_bond into the canonical (N, degree) per-directed-port array.

    Accepts:
      * a scalar  -> uniform A on every directed bond (the per-node-uniform case);
      * an (N,)   -> per-NODE A broadcast to all of a node's ports (still per-node
                     uniform AT each node -> CANCELS, the Finding-2 no-op);
      * an (N, d) -> the genuine PER-BOND (directed-edge) field.
    Returns (N, d) float64. Values are dimensionless saturation amplitudes A=|V|/V_yield."""
    N, d = net.n_nodes, net.degree
    A = np.asarray(A_bond, dtype=np.float64)
    if A.ndim == 0:
        return np.full((N, d), float(A))
    if A.shape == (N,):
        return np.repeat(A[:, None], d, axis=1)
    if A.shape == (N, d):
        return A.copy()
    raise ValueError(f"A_bond must be scalar, (N,)={(N,)}, or (N,degree)={(N, d)}; got {A.shape}")


def assemble_varactor_scattering(net: LatticeNet, A_bond, *, Y0: float = 1.0) -> np.ndarray:
    """The S(A)-READING lattice scattering operator 𝓢(A) = C @ blockdiag(S_u).

    Generalizes the bedrock assemble_global_scattering (node_scattering_multiplicity.py:
    113-146): each node u scatters by its OWN admittance-weighted S_u(Y_u), where the
    per-port admittance Y_u[p] = Y0/sqrt(S(A_bond[u,p])) is the VARACTOR MAP read from
    the per-bond saturation A_bond[u,p]. Then CONNECT permutes reflected->incident along
    the lattice's directed-edge reverse-port map (connect_index()).

      1. SCATTER each node u locally by S_u = admittance_scatter(Y_u);
      2. CONNECT: V_new.flat[dst] = V_ref.flat[src].

    PER-BOND, NOT PER-NODE (Finding 2): if A_bond is per-NODE-uniform (a scalar, or an
    (N,) broadcast), every Y_u is uniform within the node and S_u collapses to (2/d)J-I
    EXACTLY -- 𝓢(A) == the bedrock operator REGARDLESS of S. Only a per-BOND-VARYING
    A_bond (ports of one node differing) makes 𝓢(A) read saturation. The validate-on-
    known gates assert exactly this.

    A_bond: scalar | (N,) | (N, degree) dimensionless saturation amplitudes (see
    _normalize_A_bond). Returns the dense (N*degree, N*degree) operator. alpha-FREE."""
    d = net.degree
    N = net.n_nodes
    ndof = N * d
    A = _normalize_A_bond(net, A_bond)

    scatter_block = np.zeros((ndof, ndof), dtype=np.float64)
    for u in range(N):
        Y_u = bond_admittance_from_saturation(A[u], Y0=Y0)  # (d,) per-port admittance
        scatter_block[u * d:(u + 1) * d, u * d:(u + 1) * d] = admittance_scatter(Y_u)

    src_flat, dst_flat = net.connect_index()
    C = np.zeros((ndof, ndof), dtype=np.float64)
    C[dst_flat, src_flat] = 1.0
    return C @ scatter_block


# ═════════════════════════════════════════════════════════════════════════════
# 4. VALIDATE-ON-KNOWN runner (the four HALT gates)
# ═════════════════════════════════════════════════════════════════════════════
@dataclass(frozen=True)
class VaractorConfig:
    """Frozen config for the varactor validate-on-known. alpha-FREE."""

    L_srs: int = 2
    L_diamond: int = 4


def varactor_validate_on_known(cfg: "VaractorConfig | None" = None) -> dict:
    """STUB (Stage 4) — the four validate-on-known gates + scramble demonstration."""
    raise NotImplementedError("varactor_validate_on_known: implemented in Stage 4")
