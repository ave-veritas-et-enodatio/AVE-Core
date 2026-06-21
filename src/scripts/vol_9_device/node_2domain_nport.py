#!/usr/bin/env python3
"""
Two-domain N-port equivalent circuit of ONE vacuum node (Vol-9 Ch3/Ch4 synthesis).

Realizes Grant's "draw up the circuit + do actual analysis" request: an explicit,
runnable equivalent-circuit netlist for a single graded-vacuum node, with the
electrical (EM, Ω) sub-network and the mechanical (shear + bulk, Rayl) sub-network
joined by an EXPLICIT ideal-transformer two-port — NOT collapsed into one fake 3×3
across incommensurate impedance domains (the corpus-flagged conflation,
device-circuit-models.md:139).

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-NATIVE-CHECK (walked BEFORE any numerical code, per operating principle 1)
═══════════════════════════════════════════════════════════════════════════════
  * K4 / Cosserat : the node carries THREE substrate GRADES on ONE K4 cell:
                    - EM transverse  (the 2 photon DOF; the matched radiative PORT),
                    - bulk A1 dilatation (the MASS-"3"; Heaviside-excised longitudinal
                      scalar; m_e c² = trapped acoustic compression energy),
                    - shear Cosserat (2,3) micro-rotation (the CHARGE-"3"; winding).
                    A1 ⊥ T2 (master-equation.md:20) — the bulk and shear grades are
                    ORTHOGONAL, NEVER wired into one shared (V_inc, V_ref) phasor
                    (the genesis-24 / w_pol=0 double-count guard).
  * Op14         : the confinement wall = a μ-load SHORT (Z_core → 0, Γ → −1,
                   settled PR#260). z_core(A) = Z₀·√S(A); S(A)=√(1−A²) (Axiom 4).
  * phase vs real: every quantity here is a frequency-domain reactive impedance /
                   scattering parameter (a phasor-circuit observable). No real-space
                   lattice-Cartesian sample vs a phase-space φ² claim — Z, Γ, S are
                   coordinate-matched impedance-plane objects (A46 satisfied).
  * domains      : EM (Ω, V/A) and mechanical (Rayl = Pa·s/m, stress/velocity) do
                   NOT share a numeric axis — they are off by ~12.8 OOM AND a unit
                   change. Joining them needs a TRANSDUCER. AVE uses the
                   impedance/Maxwell analogy (mass → inductance, constants.py:389-390),
                   so the transducer is an ideal TRANSFORMER (a turns-ratio scaling
                   of an across/through pair), NOT a gyrator (which would swap
                   across↔through, the mobility analogy AVE does NOT use).

═══════════════════════════════════════════════════════════════════════════════
THE RATIO SEAM (Part 1; RESOLVED — recommendation flagged for Grant's ratification)
═══════════════════════════════════════════════════════════════════════════════
Three conflicting bulk/shear ratios exist in the corpus:
  • √2     = 1.41421  — c_bulk/c₀ = √(K/G) at K=2G; the A1 PURE-DILATATION speed.
  • √(10/3)= 1.82574  — c_L/c_T = √((K+4G/3)/G); the free MEDIUM P-WAVE / S-wave.
  • √2·√(10/3)= 2.58199 — the prereg headline (electron-Q prereg :82); ERRONEOUS.

RESOLUTION (verified against the operative code + first-principles isotropic
elasticity; full physics in the companion doc 2026-06-20_node-2domain-nport.md):

  √2 IS the bulk-PORT impedance ratio. The bulk PORT is the A1 dilatation = the
  CONFINED internal MASS mode = a pure volume/breathing common-mode (the +1
  eigenvector of the node S-matrix, node_scattering_multiplicity.py:81),
  symmetry-DECOUPLED from the deviatoric shear (vacuum_node_circuit.py:38 — shear
  is the SEPARATE differential/deviatoric axis). Its characteristic speed is the
  pure dilatational c_bulk = √(K/ρ) = √2·c₀ (constants.V_LONG, :674-676; _bulk.py:103).
    → Z_bulk/Z_shear |_port = (ρ c_bulk)/(ρ c_shear) = c_bulk/c₀ = √(K/G) = √2.

  √(10/3) IS a DIFFERENT physical object: the freely-PROPAGATING longitudinal
  P-wave of the bulk medium, whose speed c_L = √((K+4G/3)/ρ) NECESSARILY mixes the
  A1 dilatation AND the deviatoric shear (the +4G/3 deviatoric term). It is the
  P-wave-to-S-wave speed ratio of the unconfined medium (crystal_engine.py:27,96),
  the correct object for a propagating mode, NOT for the confined bulk port.

  KEEP-BOTH-DISAMBIGUATE: both are correct, for DIFFERENT objects. The error is
  using them interchangeably.

  The 2.582 DOUBLE-COUNT: the prereg multiplied (c_bulk/c₀)·(c_L/c_T) =
  (√(K/G))·(√((K+4G/3)/G)) = c_bulk·c_L/c₀². Because c_T = c_shear = c₀ on the LC
  lattice (the transverse photon speed √(G/ρ) = c₀), this product mixes TWO
  distinct longitudinal speeds (the pure-dilatation c_bulk AND the P-wave c_L)
  against the same transverse reference — a physically meaningless compound.
  graded_vacuum_network.py:67-75 already caught this and demoted 2.582 to a
  non-physical sensitivity probe; √(10/3) is its α-free primary, correct for the
  TWO-MECHANICAL-CHANNELS propagation ratio it computes (the medium gap location),
  but that is NOT the confined bulk-PORT impedance.

  RECOMMENDATION (Grant ratifies): the canonical bulk-PORT speed is c_bulk = √(K/ρ)
  → √2 ratio (the three-channel-impedances.md:22-24 value, already correct). Add a
  one-line disambiguation note distinguishing the PORT ratio (√2) from the medium
  P-wave/S-wave ratio (√(10/3)); retire the 2.582 compound everywhere as the
  flagged double-count. This driver edits NEITHER canonical leaf; it recommends.

═══════════════════════════════════════════════════════════════════════════════
THE α-LEAK LOCALIZATION (honest negative — visible, not buried)
═══════════════════════════════════════════════════════════════════════════════
RHO_BULK = ξ²·μ₀/(P_C·ℓ²) with P_C = 8πα (constants.py:664,400) ⇒ RHO_BULK ∝ 1/α,
so EVERY bare mechanical impedance magnitude (Z_shear, Z_bulk) carries α. The
mechanical-INTERNAL ratios (Z_bulk/Z_shear = √2; bulk/shear) are α-FREE (ρ cancels).
α localizes to EXACTLY the EM↔mechanical TRANSDUCER turns-ratio: the transformer
carries ξ_topo² (the honest Ω→kg/s map, constants.py:389-390) AND a residual
p_c = 8πα once the lumped↔specific reconciliation is done via ℓ_node². That residual
is kept as a SEPARATE, COMMENTED factor here so the α-echo is VISIBLE, never buried.

DISCIPLINE: lossless-reactive (Axiom 3) — R=0 everywhere; confinement = a reactive
SHORT (|Γ|=1), NOT resistive loss. Zero hardcoded canonical literals: every number
imports from ave.core.constants. Validate-on-known: recover Z₀, c₀, the Compton
clock from the cold node (hard assert gates).
"""

from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np

# ZERO hardcoded canonical literals — every number imports from the canonical source.
from ave.core.constants import (
    ALPHA,
    C_0,
    EPSILON_0,
    G_VAC,
    HBAR,
    L_NODE,
    M_E,
    MU_0,
    NU_VAC,
    P_C,
    RHO_BULK,
    V_LONG,
    XI_TOPO,
    Z_0,
)


# ═════════════════════════════════════════════════════════════════════════════
# 0.  CANONICAL-SOURCE GUARD (ave-canonical-source Step 4)
# ═════════════════════════════════════════════════════════════════════════════
def assert_canonical_source() -> None:
    """Fail loudly if ave.core.constants is not the worktree's canonical source."""
    import ave.core.constants as _avc

    assert _avc.__file__.endswith("ave/core/constants.py"), (
        f"ave.core.constants is not the AVE-Core canonical source: {_avc.__file__}"
    )


# ═════════════════════════════════════════════════════════════════════════════
# 1.  REACTIVE PRIMITIVES — lossless (Axiom 3: R = 0 everywhere)
# ═════════════════════════════════════════════════════════════════════════════
def reflection(z_load: complex, z_ref: float) -> complex:
    """Γ = (Z_load − Z_ref)/(Z_load + Z_ref). z_ref is the matched/reference
    impedance of the port's own domain (Ω for EM, Rayl for mechanical)."""
    return (z_load - z_ref) / (z_load + z_ref)


def saturation_kernel(A: float) -> float:
    """Axiom-4 quarter-arc kernel S(A) = √(1 − A²) (cold A=0 ⇒ S=1)."""
    return float(np.sqrt(max(1.0 - A**2, 0.0)))


def z_core_of_A(A: float, z0: float) -> float:
    """μ-load short under saturation: z_core(A) = z0·√S(A) → 0 as A → 1 (Op14,
    PR#260). The confined-port load impedance; the SHORT that makes Γ → −1."""
    return z0 * np.sqrt(saturation_kernel(A))


# ═════════════════════════════════════════════════════════════════════════════
# 2.  THE THREE PORTS (per domain) — each a single reactive branch
# ═════════════════════════════════════════════════════════════════════════════
@dataclass(frozen=True)
class PortResult:
    name: str
    domain: str  # "electrical" (Ω) or "mechanical" (Rayl)
    grade: str  # EM transverse / A1 dilatation MASS-3 / Cosserat (2,3) CHARGE-3
    z_ref: float  # matched/reference impedance of the port's domain
    z_cold: float  # cold-lattice port impedance
    gamma_cold: complex  # Γ at the cold (matched/open) operating point
    confined: bool  # True ⇒ Γ → −1 reactive short at saturation


def em_port() -> tuple[PortResult, dict]:
    """EM TRANSVERSE port — the SOLE external/radiative port (Ω).

    Lumped LC cell: L_cell = μ₀·ℓ_node, C_cell = ε₀·ℓ_node.
      √(L_cell/C_cell) = √(μ₀/ε₀) = Z₀  (the characteristic impedance).
      ω_LC = 1/√(L_cell·C_cell) = c₀/ℓ_node  (the Compton-clock cell frequency).
    Matched radiative termination ⇒ Γ_EM = 0 (the SYM-gravity reflectionless port).
    """
    L_cell = MU_0 * L_NODE
    C_cell = EPSILON_0 * L_NODE
    z_em = float(np.sqrt(L_cell / C_cell))  # = Z₀
    omega_lc = 1.0 / np.sqrt(L_cell * C_cell)  # = c₀/ℓ_node
    # matched radiative port: load = Z₀ ⇒ Γ = 0.
    gamma = reflection(complex(z_em), Z_0)
    pr = PortResult(
        name="EM-transverse",
        domain="electrical",
        grade="EM transverse photon (2 DOF) — matched radiative PORT",
        z_ref=Z_0,
        z_cold=z_em,
        gamma_cold=gamma,
        confined=False,
    )
    extra = {"L_cell_H": L_cell, "C_cell_F": C_cell, "omega_LC": omega_lc, "c0_over_ell": C_0 / L_NODE}
    return pr, extra


def shear_port() -> tuple[PortResult, dict]:
    """SHEAR / Cosserat (2,3) micro-rotation port — the CHARGE-"3" (Rayl).

    c_shear = √(G/ρ) = c₀ on the LC lattice (the transverse mechanical speed).
    Z_shear = ρ_bulk·c_shear. CONFINED internal channel ⇒ Γ_shear → −1 at
    saturation (z_core → 0). Same impedance DOMAIN as the bulk port (Rayl).
    """
    c_shear = float(np.sqrt(G_VAC / RHO_BULK))  # = c₀
    z_shear = RHO_BULK * c_shear
    pr = PortResult(
        name="shear-Cosserat",
        domain="mechanical",
        grade="Cosserat (2,3) micro-rotation CHARGE-3 (helicity winding)",
        z_ref=z_shear,  # matched to its own cold value (reference for Γ at saturation)
        z_cold=z_shear,
        gamma_cold=reflection(complex(z_shear), z_shear),  # 0 at the cold match
        confined=True,
    )
    extra = {"c_shear": c_shear, "c_shear_is_c0": bool(np.isclose(c_shear, C_0))}
    return pr, extra


def bulk_port() -> tuple[PortResult, dict]:
    """BULK / A1 dilatation port — the MASS-"3" (Rayl).

    THE PART-1 RESOLUTION IS REALIZED HERE. The bulk PORT speed is the
    A1 PURE-DILATATION (confined breathing-common-mode) speed:
        c_bulk = √(K/ρ) = √(2G/ρ) = V_LONG = √2·c₀   (constants.V_LONG, K=2G).
    NOT the medium P-wave c_L = √((K+4G/3)/ρ) (that mixes A1 + shear; it is the
    propagating-mode object, computed separately in medium_pwave_ratio()).
        Z_bulk = ρ_bulk·c_bulk = √2·ρ_bulk·c₀.
    CONFINED internal channel ⇒ Γ_bulk → −1 at saturation (z_core → 0). Same
    impedance DOMAIN as the shear port (Rayl) ⇒ they form ONE mechanical 2-port.
    """
    c_bulk = float(V_LONG)  # = √(K/ρ) = √2·c₀  (A1 dilatation PORT speed)
    z_bulk = RHO_BULK * c_bulk
    pr = PortResult(
        name="bulk-A1-dilatation",
        domain="mechanical",
        grade="A1 dilatation MASS-3 (Heaviside longitudinal scalar; m_e c² store)",
        z_ref=z_bulk,
        z_cold=z_bulk,
        gamma_cold=reflection(complex(z_bulk), z_bulk),
        confined=True,
    )
    extra = {
        "c_bulk_A1": c_bulk,
        "c_bulk_over_c0": c_bulk / C_0,  # = √2
        "speed_object": "A1 pure-dilatation sqrt(K/rho) (confined PORT) — NOT medium P-wave",
    }
    return pr, extra


# ═════════════════════════════════════════════════════════════════════════════
# 3.  THE RATIO SEAM — BOTH ratios side-by-side, each correctly LABELED
# ═════════════════════════════════════════════════════════════════════════════
def ratio_seam() -> dict:
    """Compute BOTH bulk/shear-style ratios + the double-count, each labeled.

    All three are α-FREE (ρ cancels): the disambiguation is PHYSICS, not α.
    """
    # A1 dilatation bulk-PORT ratio: c_bulk/c_shear with c_bulk = √(K/ρ), c_shear = c₀.
    c_bulk_A1 = float(V_LONG)
    c_shear = float(np.sqrt(G_VAC / RHO_BULK))  # = c₀
    ratio_port_A1 = c_bulk_A1 / c_shear  # = √2

    # medium P-wave / S-wave ratio: c_L/c_T = √((K+4G/3)/G) = √(2(1−ν)/(1−2ν)).
    cL2_over_cT2 = 2.0 * (1.0 - NU_VAC) / (1.0 - 2.0 * NU_VAC)  # = 10/3 at ν=2/7
    ratio_medium_pwave = float(np.sqrt(cL2_over_cT2))  # = √(10/3)

    # the prereg double-count: (c_bulk/c₀)·(c_L/c_T) = c_bulk·c_L/c₀² (meaningless).
    ratio_double_count = ratio_port_A1 * ratio_medium_pwave  # = √2·√(10/3) = 2.582

    return {
        "bulk_PORT_ratio_sqrt2": {
            "value": ratio_port_A1,
            "closed_form": "sqrt(K/G) = sqrt2",
            "object": "A1 dilatation CONFINED bulk PORT (pure breathing common-mode)",
            "speed": "c_bulk = sqrt(K/rho) = V_LONG = sqrt2*c0",
            "canonical": "three-channel-impedances.md:22-24; constants.V_LONG:674-676",
            "is_port_impedance_ratio": True,
            "alpha_free": True,
        },
        "medium_Pwave_ratio_sqrt10over3": {
            "value": ratio_medium_pwave,
            "closed_form": "sqrt((K+4G/3)/G) = sqrt(2(1-nu)/(1-2nu)) = sqrt(10/3)",
            "object": "free MEDIUM P-wave / S-wave (mixes A1 dilatation + deviatoric shear)",
            "speed": "c_L = sqrt((K+4G/3)/rho); c_T = sqrt(G/rho) = c0",
            "canonical": "crystal_engine.py:27,96; graded_vacuum_network.py:120-122",
            "is_port_impedance_ratio": False,
            "alpha_free": True,
        },
        "prereg_double_count_2p582": {
            "value": ratio_double_count,
            "closed_form": "sqrt2 * sqrt(10/3) = (c_bulk/c0)*(c_L/c_T) = c_bulk*c_L/c0^2",
            "object": "ERRONEOUS compound — multiplies the A1-port speed AND the P-wave speed",
            "diagnosis": "c_T=c_shear=c0, so this mixes TWO distinct longitudinal speeds "
            "against one transverse reference — physically meaningless",
            "flagged_at": "graded_vacuum_network.py:67-75; prereg:82 headline; "
            "device-circuit-models.md:195 (seam 4, OPEN pending Grant)",
            "alpha_free": True,
        },
        "recommendation_for_grant": (
            "RATIFY: canonical bulk-PORT speed = c_bulk = sqrt(K/rho) -> sqrt2 ratio "
            "(three-channel-impedances.md:22 value, ALREADY correct). KEEP-BOTH-DISAMBIGUATE: "
            "add a one-line note distinguishing the PORT ratio (sqrt2) from the medium "
            "P-wave/S-wave ratio (sqrt(10/3)); retire 2.582 everywhere as the double-count. "
            "This driver edits NEITHER canonical leaf."
        ),
    }


# ═════════════════════════════════════════════════════════════════════════════
# 4.  THE EM↔MECHANICAL TRANSDUCER — an ideal TRANSFORMER (NOT a gyrator)
# ═════════════════════════════════════════════════════════════════════════════
@dataclass(frozen=True)
class TransducerResult:
    kind: str  # "ideal-transformer"
    turns_ratio_squared_honest: float  # ξ_topo² — the honest Ω→kg/s map
    p_c_residual: float  # 8πα — the lumped↔specific α-leak (SEPARATE, VISIBLE)
    z_em_referred_to_mech: float  # Z_EM reflected through the transformer (Rayl-side)
    alpha_localized_here: bool


def em_mech_transformer(z_em_ohm: float) -> TransducerResult:
    """Join the electrical (Ω) and mechanical (Rayl) sub-networks via ONE explicit
    ideal-transformer two-port. AVE uses the impedance/Maxwell analogy (mass →
    inductance, constants.py:389-390), so the bridge is a TRANSFORMER (across/through
    turns-ratio scaling), NOT a gyrator (which would swap across↔through).

    The transformer carries TWO factors, kept SEPARATE so the α-leak is VISIBLE:
      (a) ξ_topo²  — the HONEST electromechanical map Ω → kg/s
                     (EE_TO_TOPO_INDUCTANCE = ξ_topo², constants.py:389-390). α-FREE.
      (b) p_c = 8πα — the residual once lumped (Ω, per-cell) is reconciled with
                     specific (Rayl, per-area·s) via ℓ_node². RHO_BULK ∝ 1/(8πα), so
                     the α-echo localizes to EXACTLY this transducer factor — kept as
                     a SEPARATE commented multiplier, NEVER folded into ξ_topo².

    Z_referred(Rayl) = Z_EM(Ω) · ξ_topo² / (p_c · ℓ_node²)   [the lumped↔specific
    reconciliation; note the (ξ_topo²·μ₀)/(p_c·ℓ²) = RHO_BULK identity makes the
    α-leak EXACTLY the RHO_BULK leak — the mechanical-internal ratios stay α-free].
    """
    turns2_honest = XI_TOPO**2  # ξ_topo² — α-FREE honest Ω→kg/s
    p_c_residual = P_C  # 8πα — the α-leak, VISIBLE and SEPARATE
    # lumped↔specific reconciliation via ℓ_node² (the α-localized referral):
    z_referred = z_em_ohm * turns2_honest / (p_c_residual * L_NODE**2)
    return TransducerResult(
        kind="ideal-transformer",
        turns_ratio_squared_honest=turns2_honest,
        p_c_residual=p_c_residual,
        z_em_referred_to_mech=float(z_referred),
        alpha_localized_here=True,
    )


# ═════════════════════════════════════════════════════════════════════════════
# 5.  PER-DOMAIN S-MATRICES (do NOT force one 3×3 across domains)
# ═════════════════════════════════════════════════════════════════════════════
def electrical_S_1port(gamma_em: complex) -> np.ndarray:
    """The electrical sub-network is a 1-port: S = [Γ_EM] (1×1). Matched ⇒ [0]."""
    return np.array([[gamma_em]], dtype=complex)


def mechanical_S_2port(
    gamma_bulk: complex, gamma_shear: complex, coupling: complex
) -> np.ndarray:
    """The mechanical sub-network is a 2-port (bulk ⊗ shear, SAME Rayl domain).

    S = [[Γ_bulk, t_bs], [t_sb, Γ_shear]]. The off-diagonals are the inter-grade
    coupling. With H_couple OFF (isolation leg) the off-diagonals vanish; with the
    chiral circulator ON they are NON-RECIPROCAL (t_bs ≠ t_sb ⇒ S ≠ Sᵀ).
    """
    t_bs = coupling
    t_sb = -coupling  # chiral circulator: non-reciprocal (sign-flipped transmission)
    return np.array([[gamma_bulk, t_bs], [t_sb, gamma_shear]], dtype=complex)


def chiral_circulator_S(theta: float) -> np.ndarray:
    """The inter-sublattice chiral-circulator coupling as a NON-RECIPROCAL 2-port
    (S ≠ Sᵀ). A lossless gyrotropic rotation by θ (the I4₁32 chirality angle):
        S = [[0, e^{+iθ}], [−e^{−iθ}, 0]]  — unitary, but S ≠ Sᵀ (non-reciprocal).
    Chirality sign selects matter vs antimatter (crystal_engine.py:41). This is the
    inter-tank coupling, the chiral CIRCULATOR (not a gyrator — it routes, lossless).
    """
    return np.array(
        [[0.0, np.exp(1j * theta)], [-np.exp(-1j * theta), 0.0]], dtype=complex
    )


# ═════════════════════════════════════════════════════════════════════════════
# 6.  CONFINEMENT SWEEP — z_core(A) = Z₀√S ⇒ Γ → −1 on the confined ports
# ═════════════════════════════════════════════════════════════════════════════
def confinement_sweep(z_ref: float) -> list[dict]:
    """Drive A → 1 on a CONFINED port. z_core(A) = z_ref·√S(A) → 0, so
    Γ = (z_core − z_ref)/(z_core + z_ref) → −1 MONOTONICALLY. Lossless reactive
    SHORT (R=0), NOT resistive loss. Q → ∞ on the confined port (no real part).

    The A grid is pushed to 1 − 1e−6 (z_core/z_ref = (1−A²)^¼) to witness the
    asymptote: Γ → −1 only in the strict A → 1 limit (it is a continuous reactive
    short, never a discontinuous flip). The gate asserts |Γ| is monotone-increasing
    toward 1 and that the deepest point is past −0.9 (the wall is forming)."""
    A_grid = [0.0, 0.5, 0.9, 0.99, 0.999, 0.9999, 0.99999, 0.999999]
    rows = []
    for A in A_grid:
        z_core = z_core_of_A(A, z_ref)
        g = reflection(complex(z_core), z_ref)
        rows.append(
            {"A": float(A), "S": saturation_kernel(A), "z_core_over_zref": float(z_core / z_ref),
             "Gamma_re": float(g.real), "Gamma_im": float(g.imag), "abs_Gamma": float(abs(g))}
        )
    # gate: |Γ| monotone increasing toward 1; deepest point past −0.9 (wall forming).
    absg = [r["abs_Gamma"] for r in rows]
    assert all(b <= a + 1e-12 for b, a in zip(absg, absg[1:])), "|Γ| not monotone toward 1"
    assert rows[-1]["Gamma_re"] < -0.9, "deepest Γ did not approach −1 (wall not forming)"
    return rows


# ═════════════════════════════════════════════════════════════════════════════
# 7.  VALIDATE-ON-KNOWN — recover Z₀, c₀, the Compton clock from the cold node
# ═════════════════════════════════════════════════════════════════════════════
def validate_on_known() -> dict:
    """Hard-assert the cold node recovers the KNOWN anchors. HALTs if any fails."""
    em, em_extra = em_port()
    sh, sh_extra = shear_port()
    # Z₀ from the lumped LC cell:
    z0_ok = bool(np.isclose(em.z_cold, Z_0, rtol=1e-12))
    # c₀ from the shear mechanical speed √(G/ρ):
    c0_ok = bool(np.isclose(sh_extra["c_shear"], C_0, rtol=1e-12))
    # the Compton clock: ω_LC = c₀/ℓ_node = m_e c²/ℏ (the rest-mass angular frequency).
    omega_compton = M_E * C_0**2 / HBAR
    clock_ok = bool(np.isclose(em_extra["omega_LC"], omega_compton, rtol=1e-9))
    out = {
        "Z0_recovered": z0_ok, "Z0_cell": em.z_cold, "Z0_const": Z_0,
        "c0_recovered": c0_ok, "c_shear": sh_extra["c_shear"], "c0_const": C_0,
        "compton_clock_recovered": clock_ok,
        "omega_LC": em_extra["omega_LC"], "omega_compton_mec2_hbar": omega_compton,
    }
    if not (z0_ok and c0_ok and clock_ok):
        print("HALT: cold node did NOT recover Z₀ / c₀ / Compton clock — model is wrong.")
        print(json.dumps(out, indent=2))
        sys.exit(1)
    return out


# ═════════════════════════════════════════════════════════════════════════════
# 8.  ASSEMBLE + REPORT
# ═════════════════════════════════════════════════════════════════════════════
def main() -> None:
    assert_canonical_source()

    # --- validate-on-known FIRST (gate) ---
    vok = validate_on_known()

    # --- the three ports ---
    em, em_extra = em_port()
    sh, sh_extra = shear_port()
    bk, bk_extra = bulk_port()

    # --- the ratio seam (BOTH ratios side-by-side) ---
    seam = ratio_seam()

    # --- the EM↔mechanical transformer (α localized here) ---
    xfmr = em_mech_transformer(em.z_cold)

    # --- per-domain S-matrices ---
    S_em = electrical_S_1port(em.gamma_cold)  # 1×1
    # cold (isolation) mechanical 2-port: no coupling, matched references.
    S_mech_cold = mechanical_S_2port(bk.gamma_cold, sh.gamma_cold, coupling=0.0 + 0j)
    # saturated (confined) mechanical 2-port: both Γ → −1, with chiral coupling.
    A_sat = 0.999999  # deep saturation: z_core/Z_ref = (1−A²)^¼ → 0 ⇒ Γ → −1
    g_bulk_sat = reflection(complex(z_core_of_A(A_sat, bk.z_ref)), bk.z_ref)
    g_shear_sat = reflection(complex(z_core_of_A(A_sat, sh.z_ref)), sh.z_ref)
    S_mech_sat = mechanical_S_2port(g_bulk_sat, g_shear_sat, coupling=0.0 + 0j)
    # the chiral circulator (non-reciprocal inter-tank coupling)
    theta_chi = 2.0 * np.pi * NU_VAC  # a chirality angle (ν_vac as the gyrotropic phase)
    S_circ = chiral_circulator_S(theta_chi)
    non_reciprocal = bool(not np.allclose(S_circ, S_circ.T))

    # --- confinement sweeps on the two confined ports ---
    sweep_bulk = confinement_sweep(bk.z_ref)
    sweep_shear = confinement_sweep(sh.z_ref)

    # --- pole / Q ---
    # Confined ports are lossless reactive (R=0) ⇒ Q → ∞ (|Γ|=1, no real part).
    # Finite Q enters ONLY via the EM matched radiative port (Γ_EM=0 ⇒ energy leaves).
    Q_confined = float("inf")
    Q_open_em = 0.0  # matched ⇒ critically damped radiative port (Γ=0, all leaks)

    # ----------------------------- REPORT --------------------------------------
    print("=" * 78)
    print("TWO-DOMAIN N-PORT EQUIVALENT CIRCUIT — ONE VACUUM NODE")
    print("=" * 78)

    print("\n(0) VALIDATE-ON-KNOWN (cold node):")
    print(f"    Z₀  : cell √(L/C) = {vok['Z0_cell']:.6f} Ω   (const {vok['Z0_const']:.6f})  ✓ {vok['Z0_recovered']}")
    print(f"    c₀  : shear √(G/ρ) = {vok['c_shear']:.6e} m/s (const {vok['c0_const']:.6e})  ✓ {vok['c0_recovered']}")
    print(f"    clock: ω_LC = {vok['omega_LC']:.6e} = m_e c²/ℏ ({vok['omega_compton_mec2_hbar']:.6e}) ✓ {vok['compton_clock_recovered']}")

    print("\n(1) PER-PORT Z and Γ (cold):")
    print(f"    EM-transverse   [{em.domain:10s}]  Z = {em.z_cold:.4f} Ω    Γ_EM = {em.gamma_cold.real:+.3e}  (matched radiative port)")
    print(f"    shear-Cosserat  [{sh.domain:10s}]  Z = {sh.z_cold:.4e} Rayl Γ_cold = {sh.gamma_cold.real:+.3e}  (CONFINED → Γ→−1 at sat)")
    print(f"    bulk-A1-dilat   [{bk.domain:10s}]  Z = {bk.z_cold:.4e} Rayl Γ_cold = {bk.gamma_cold.real:+.3e}  (CONFINED → Γ→−1 at sat)")
    print(f"    EM cell: L_cell = {em_extra['L_cell_H']:.4e} H, C_cell = {em_extra['C_cell_F']:.4e} F")
    print(f"    bulk PORT speed c_bulk/c₀ = {bk_extra['c_bulk_over_c0']:.6f} = √2  (A1 pure-dilatation √(K/ρ))")

    print("\n(2) THE RATIO SEAM — BOTH ratios side-by-side (Part-1 resolution):")
    s2 = seam["bulk_PORT_ratio_sqrt2"]; s10 = seam["medium_Pwave_ratio_sqrt10over3"]; sdc = seam["prereg_double_count_2p582"]
    print(f"    √2     = {s2['value']:.6f}  PORT  : {s2['object']}")
    print(f"                          {s2['speed']}")
    print(f"    √(10/3)= {s10['value']:.6f}  MEDIUM: {s10['object']}")
    print(f"                          {s10['speed']}")
    print(f"    2.582  = {sdc['value']:.6f}  ✗ DOUBLE-COUNT: {sdc['diagnosis']}")
    print(f"    >> RECOMMENDATION (Grant ratifies): {seam['recommendation_for_grant']}")

    print("\n(3) EM↔MECHANICAL TRANSDUCER (ideal TRANSFORMER, NOT gyrator):")
    print(f"    honest turns² = ξ_topo² = {xfmr.turns_ratio_squared_honest:.6e}  (Ω→kg/s, α-FREE)")
    print(f"    α-LEAK (visible, separate): p_c = 8πα = {xfmr.p_c_residual:.6f}  ← α localizes HERE")
    print(f"    Z_EM referred to Rayl side = {xfmr.z_em_referred_to_mech:.4e}")
    print(f"    (mechanical-internal ratios Z_bulk/Z_shear=√2 are α-FREE; ρ cancels)")

    print("\n(4) PER-DOMAIN S-MATRICES (NOT one 3×3 across domains):")
    print(f"    electrical 1-port  S_EM   = [{S_em[0,0].real:+.3e}]   (matched ⇒ 0)")
    print(f"    mechanical 2-port (cold)  S = {np.array2string(S_mech_cold.real, precision=3)}")
    print(f"    mechanical 2-port (sat)   S = {np.array2string(S_mech_sat.real, precision=3)}  (both Γ→−1)")
    print(f"    chiral circulator  S = {np.array2string(S_circ, precision=3)}")
    print(f"      non-reciprocal (S ≠ Sᵀ): {non_reciprocal}   unitary: {bool(np.allclose(S_circ@S_circ.conj().T, np.eye(2)))}")

    print("\n(5) CONFINEMENT SWEEP — z_core(A)=Z_ref√S ⇒ Γ→−1 (bulk port, A→1):")
    for r in sweep_bulk:
        print(f"    A={r['A']:.6f}  z_core/Z_ref={r['z_core_over_zref']:.5f}  Γ={r['Gamma_re']:+.5f}  |Γ|={r['abs_Gamma']:.5f}")
    print(f"    → Γ → −1 monotonically (lossless reactive short; the μ-load wall, PR#260)")

    print("\n(6) POLE / Q:")
    print(f"    confined ports (bulk, shear): lossless reactive R=0 ⇒ Q → ∞ ({Q_confined})")
    print(f"    EM matched radiative port:    Γ=0 ⇒ energy leaves ⇒ finite damping (Q_em={Q_open_em})")
    print("    (finite Q enters ONLY via the EM port; confinement = reactive short, not loss)")

    # ----------------------------- WRITE JSON ----------------------------------
    out = {
        "validate_on_known": vok,
        "ports": {
            "em": {**asdict(em), "gamma_cold": str(em.gamma_cold), **em_extra},
            "shear": {**asdict(sh), "gamma_cold": str(sh.gamma_cold), **sh_extra},
            "bulk": {**asdict(bk), "gamma_cold": str(bk.gamma_cold), **bk_extra},
        },
        "ratio_seam": seam,
        "transducer": asdict(xfmr),
        "S_matrices": {
            "electrical_1port": str(S_em.tolist()),
            "mechanical_2port_cold": str(S_mech_cold.tolist()),
            "mechanical_2port_saturated": str(S_mech_sat.tolist()),
            "chiral_circulator": str(S_circ.tolist()),
            "circulator_non_reciprocal": non_reciprocal,
        },
        "confinement_sweep_bulk": sweep_bulk,
        "confinement_sweep_shear": sweep_shear,
        "Q": {"confined_lossless": "inf", "em_matched_radiative": Q_open_em},
    }
    out_dir = Path(__file__).resolve().parent / "_output"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "node_2domain_nport.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nResults written: {out_path}")


if __name__ == "__main__":
    main()
