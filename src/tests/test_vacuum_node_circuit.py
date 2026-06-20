"""
test_vacuum_node_circuit.py
===========================
Tests for the per-DOF vacuum node circuit model (#44).

The per-DOF node carries an INDEPENDENT reactive pair (L_i, C_i) per translation
DOF i ∈ {x,y,z} — a constitutive TENSOR. One circuit, three behaviors:

  1. ISOTROPIC saturation  → achromatic + isotropic (Z=Z₀, Γ=0; SYM ε·μ co-scale)
  2. DEVIATORIC strain      → strain-induced birefringence FORM (Δc/c ∝ split)
  3. HIGH-k dispersion      → (q·ℓ)² matter zone-edge AND (q·ℓ)⁴ photon birefringence

VALIDATE-ON-KNOWN gate: the isotropic continuum-limit node MUST recover
c₀ = 1/√(μ₀ε₀) and Z₀ = √(μ₀/ε₀). A model that fails this is wrong (HALT).

Consistency-class: this is a CONSISTENCY re-expression unifying three already-
asserted behaviors into one node-constitutive structure. No α / m_e value claim.
"""

import numpy as np
import pytest

from ave.core.constants import C_0, L_NODE, Z_0
from ave.core.vacuum_node_circuit import (
    K4_BOND_DIRECTIONS,
    PerDOFVacuumNode,
    cubic_anisotropy_invariant,
    directional_anisotropy,
    lattice_dispersion,
    phase_speed,
    photon_birefringence,
)


# ─────────────────────────────────────────────────────────────────────────────
# (c) VALIDATE-ON-KNOWN — the c₀ / Z₀ recovery gate (wire FIRST, Build-A lesson)
# ─────────────────────────────────────────────────────────────────────────────


def test_cold_node_recovers_c0_exactly():
    """The isotropic cold-vacuum node (lL=lC=1) MUST recover c₀ on every DOF.
    HALT condition if it does not."""
    cold = PerDOFVacuumNode()
    assert np.allclose(cold.c, C_0, rtol=1e-12), f"c₀ not recovered: {cold.c}"


def test_cold_node_recovers_Z0_exactly():
    """The isotropic cold-vacuum node MUST recover Z₀ = √(μ₀/ε₀) on every DOF."""
    cold = PerDOFVacuumNode()
    assert np.allclose(cold.Z, Z_0, rtol=1e-12), f"Z₀ not recovered: {cold.Z}"


def test_cold_node_isotropic():
    """Cold node: all three DOF identical (no a-priori anisotropy)."""
    cold = PerDOFVacuumNode()
    assert np.allclose(cold.c, cold.c[0])
    assert np.allclose(cold.Z, cold.Z[0])


# ─────────────────────────────────────────────────────────────────────────────
# (1) ISOTROPIC saturation — achromatic + isotropic (Z invariant, Γ=0)
# ─────────────────────────────────────────────────────────────────────────────


@pytest.mark.parametrize("n", [1.1, 1.5, 2.0, 5.0])
def test_isotropic_saturation_drops_c_uniformly(n):
    """REGIME 1: L_i,C_i co-scale equally → c drops to c₀/n uniformly (light
    bends), but the SAME on every DOF (isotropic, no dispersion)."""
    node = PerDOFVacuumNode.isotropic_saturated(n=n)
    assert np.allclose(node.c, C_0 / n, rtol=1e-12)
    assert np.allclose(node.c, node.c[0])  # isotropic across DOF


@pytest.mark.parametrize("n", [1.1, 1.5, 2.0, 5.0])
def test_isotropic_saturation_Z_invariant(n):
    """REGIME 1: the node impedance stays EXACTLY Z₀ under isotropic saturation
    → Γ = (Z−Z₀)/(Z+Z₀) = 0 (matched, no reflection). This IS the achromatic
    SYM ε·μ co-scale at the node (achromatic-impedance-matching.md)."""
    node = PerDOFVacuumNode.isotropic_saturated(n=n)
    assert np.allclose(node.Z, Z_0, rtol=1e-12)
    gamma = (node.Z - Z_0) / (node.Z + Z_0)
    assert np.allclose(gamma, 0.0, atol=1e-12)


def test_isotropic_node_no_directional_dispersion_in_continuum():
    """REGIME 1: in the continuum limit the isotropic node has the same phase
    speed along every direction (achromatic + isotropic)."""
    node = PerDOFVacuumNode.isotropic_saturated(n=1.5)
    q = 1.0 / (1e6 * L_NODE)  # deep continuum, q·ℓ ~ 1e-6
    v_bond = phase_speed(node, q, K4_BOND_DIRECTIONS[0])
    v_face = phase_speed(node, q, [1.0, 0.0, 0.0])
    assert abs(v_bond / v_face - 1.0) < 1e-10


# ─────────────────────────────────────────────────────────────────────────────
# (2) DEVIATORIC strain — strain-induced birefringence FORM
# ─────────────────────────────────────────────────────────────────────────────


def test_deviatoric_produces_birefringence():
    """REGIME 2: a deviatoric split L_x·C_x ≠ L_y·C_y produces a nonzero Δc/c
    between the x and y polarizations — strain-induced birefringence exists."""
    dev = PerDOFVacuumNode.deviatoric(n=1.0, delta=1e-3)
    assert abs(dev.birefringence()) > 0.0
    assert dev.c[0] != dev.c[1]


def test_birefringence_form_scales_with_deviatoric_strain():
    """REGIME 2: the birefringence FORM Δc/c is monotone and ~linear in the
    deviatoric strain amplitude δ (the FORM δn ∝ deviatoric strain — the
    coefficient is a separate quantitative test, vacuum-birefringence-e4.md)."""
    deltas = np.array([1e-4, 3e-4, 1e-3, 3e-3])
    bf = np.array([abs(PerDOFVacuumNode.deviatoric(1.0, d).birefringence()) for d in deltas])
    # monotone increasing
    assert np.all(np.diff(bf) > 0)
    # leading ratio Δc/c ≈ δ (the small-δ FORM): (Δc/c)/δ → ~1
    ratio = bf / deltas
    assert np.allclose(ratio, ratio[0], rtol=0.05)


def test_isotropic_node_has_zero_birefringence():
    """An isotropic (non-deviatoric) node has no birefringence — confirming the
    effect is strain-SOURCED, not an artifact."""
    iso = PerDOFVacuumNode.isotropic_saturated(n=2.0)
    assert abs(iso.birefringence()) < 1e-14


# ─────────────────────────────────────────────────────────────────────────────
# (3) HIGH-k dispersion — (q·ℓ)² matter zone-edge AND (q·ℓ)⁴ photon birefringence
# ─────────────────────────────────────────────────────────────────────────────


def test_continuum_limit_linear_dispersion():
    """REGIME 3: in the continuum limit ω ≈ c·q (linear, achromatic)."""
    cold = PerDOFVacuumNode()
    q = 1.0 / (1e6 * L_NODE)
    w = lattice_dispersion(cold, q, [1.0, 0.0, 0.0])
    assert abs(w / (C_0 * q) - 1.0) < 1e-10


def _loglog_slope(xs, ys):
    xs = np.asarray(xs, float)
    ys = np.asarray(ys, float)
    return np.polyfit(np.log(xs), np.log(ys), 1)[0]


def test_matter_zone_edge_anisotropy_scales_q_squared():
    """REGIME 3a: the lattice-LOCKED MATTER carrier's directional anisotropy is
    the (q·ℓ)² ZONE-EDGE form (the mechanical dynamical-matrix tensor is already
    anisotropic at O(q²); binary-kill-switches.md:17 'matter carriers')."""
    cold = PerDOFVacuumNode()
    qells = np.array([1e-3, 2e-3, 4e-3, 8e-3])
    aniso = np.array(
        [abs(directional_anisotropy(cold, qe / L_NODE, K4_BOND_DIRECTIONS[0], [1, 0, 0])) for qe in qells]
    )
    slope = _loglog_slope(qells, aniso)
    assert abs(slope - 2.0) < 0.05, f"matter zone-edge slope {slope}, expected 2"


def test_photon_birefringence_scales_q_fourth():
    """REGIME 3b: the continuum PHOTON birefringence is the (q·ℓ)⁴ form — the
    O(q²) EM correction is the ISOTROPIC cubic invariant |q|², so the first
    anisotropy is quartic (clm-pp3qwf, preferred-frame §2)."""
    cold = PerDOFVacuumNode()
    qells = np.array([1e-3, 2e-3, 4e-3, 8e-3])
    bf = np.array([abs(photon_birefringence(cold, qe / L_NODE, [2, 1, 0])) for qe in qells])
    slope = _loglog_slope(qells, bf)
    assert abs(slope - 4.0) < 0.05, f"photon birefringence slope {slope}, expected 4"


def test_cubic_invariant_is_traceless():
    """The quartic cubic invariant Ξ(q̂) averages to ZERO over the sphere
    (traceless) — it is the first ANISOTROPIC (sign-changing) cubic harmonic,
    distinct from the isotropic |q|⁴ (preferred-frame §2)."""
    rng = np.random.default_rng(42)
    dirs = rng.normal(size=(50000, 3))
    xis = np.array([cubic_anisotropy_invariant(d) for d in dirs])
    assert abs(np.mean(xis)) < 5e-3


def test_cubic_invariant_high_symmetry_values():
    """Ξ takes the known cubic-harmonic extremal values on [100] and [111]."""
    assert cubic_anisotropy_invariant([1, 0, 0]) == pytest.approx(2.0 / 5.0)
    assert cubic_anisotropy_invariant([1, 1, 1]) == pytest.approx(-4.0 / 15.0, abs=1e-12)


def test_tetrahedral_second_moment_isotropic():
    """SUBSTRATE-NATIVE check: the K4 bond set's 2nd moment Σ_b(q̂·b̂)² = 4/3 for
    EVERY direction — the isotropy at O(q²) that makes the lattice Lorentz-look
    isotropic at long wavelength (the diamond-crystal analogy)."""
    bonds = np.stack(K4_BOND_DIRECTIONS)
    for qhat in [[1, 0, 0], [1, 1, 1], [1, 1, 0], [0.3, 0.7, -0.2]]:
        qh = np.asarray(qhat, float)
        qh /= np.linalg.norm(qh)
        m2 = np.sum((bonds @ qh) ** 2)
        assert m2 == pytest.approx(4.0 / 3.0, abs=1e-12)


# ─────────────────────────────────────────────────────────────────────────────
# GRADE-CLARITY guard — the per-DOF L/C is the MECHANICAL layer, not the A1 phasor
# ─────────────────────────────────────────────────────────────────────────────


def test_per_dof_is_three_translation_dof_not_a1_phasor():
    """GRADE guard: the model exposes exactly THREE translation DOF (x,y,z) — the
    mechanical displacement directions (u → E). It does NOT carry a 4th
    (V_inc,V_ref) A1-dilatation phasor DOF nor a Cosserat winding DOF
    (master-equation.md:20 two-3s fence)."""
    node = PerDOFVacuumNode()
    assert node.L.shape == (3,)
    assert node.C.shape == (3,)
    with pytest.raises(ValueError):
        PerDOFVacuumNode(lL=(1.0, 1.0, 1.0, 1.0), lC=(1.0, 1.0, 1.0, 1.0))
