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

# (skeleton — sections filled incrementally per the implementer-dispatch
#  incremental-write discipline: skeleton -> analysis -> report.)


def main() -> None:  # pragma: no cover — filled in the analysis commit
    raise NotImplementedError("node_2domain_nport analysis — filled next commit")


if __name__ == "__main__":
    main()
