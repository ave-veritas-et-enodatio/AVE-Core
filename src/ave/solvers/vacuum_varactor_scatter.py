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
def assemble_varactor_scattering(net: LatticeNet, A_bond) -> np.ndarray:
    """STUB (Stage 3) — 𝓢(A) = C @ blockdiag(S_n(Y_u)), per-bond admittance."""
    raise NotImplementedError("assemble_varactor_scattering: implemented in Stage 3")


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
