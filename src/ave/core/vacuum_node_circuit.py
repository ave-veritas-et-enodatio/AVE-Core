"""
Per-DOF Vacuum Node Circuit Model (#44)
=======================================

The node-constitutive layer BENEATH the cell-level ``AVE_VACUUM_CELL``
(`manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md` §1)
and the graded vacuum impedance network (same leaf, §6). Where the cell model
gives ONE scalar pair (L_cell = μ₀·ℓ_node, C_cell = ε₀·ℓ_node), this module
makes the reactive pair a CONSTITUTIVE TENSOR: each translation DOF i ∈ {x,y,z}
carries its OWN reactive pair (L_i, C_i).

GRADE CLARITY (the hard guard — `2026-06-19_electrical-mechanical-projection-map.md`).
The per-DOF (L_i, C_i) is the MECHANICAL displacement-direction constitutive
layer of the TRANSVERSE / EM-translation sector (the cell's three translational
u → E modes, vol9/ch3 index:17). It is NOT:

  * the A1 (V_inc, V_ref) dilatation-MASS phasor (the "mass-3"; never wire the
    winding into that phasor — master-equation.md:20 fence), and
  * NOT the Cosserat (2,3) micro-rotation winding (the "charge-3"; orthogonal,
    A1 ⊥ T2, master-equation.md:20).

The three translation DOF here are the MECHANICAL displacement directions u_i;
they project to the EM-transverse channel (u → E). The graded-network's
EM / shear / bulk triple is a SEPARATE axis (substrate GRADES, mixed impedance
domains — Ω vs ρc). Do NOT collapse the two axes (the seam-7 refuted-bijection
guard). This module lives entirely inside the EM-translation grade and models
its node-level directional anisotropy.

CONSISTENCY-CLASS (consistency-vs-emergence v1.3).
This is a CONSISTENCY re-expression, NOT a value-prediction. The per-DOF node
is a node-constitutive STRUCTURE that UNIFIES three already-asserted behaviors
into one circuit:

  1. ISOTROPIC (volumetric saturation S): L_i, C_i co-scale EQUALLY across i →
     all c_i equal, all Z_i equal → achromatic + isotropic (the SYM ε·μ
     co-scale at the node; Z = Z₀, Γ = 0). Light bends, does not disperse or
     reflect. [achromatic-impedance-matching.md]
  2. DEVIATORIC (shear strain): the pairs SPLIT (L_x·C_x ≠ L_y·C_y) → c_i differ
     by direction → BIREFRINGENCE (a Δc/c between polarizations). The node-level
     origin of the strain-induced birefringence FORM. [vacuum-birefringence-e4.md]
  3. HIGH-k (λ ~ ℓ_node): the discrete-lattice dispersion ω(k) with per-DOF
     structure → the (q·ℓ_node)⁴ anisotropy discreteness tell; achromatic only
     in the continuum limit λ ≫ ℓ_node. [clm-pp3qwf, binary-kill-switches.md]

The model predicts NO α / m_e value (value-echo discipline). The c₀ and Z₀
recovered in the isotropic continuum limit are the KNOWN anchors, not new
predictions — they are the VALIDATE-ON-KNOWN gate (recover them or the model
is wrong; HALT).

SUBSTRATE-NATIVE (the K4 / RANK-2 guard).
The per-DOF reactive TENSOR sits on the K4 / tetrahedral lattice (the four
bond-ports of `k4_tlm.py`, directions {(+1,+1,+1),(+1,-1,-1),(-1,+1,-1),
(-1,-1,+1)}), NOT a Cartesian 6-port grid. The continuum-limit dispersion below
is sampled along the K4 bond directions; the (q·ℓ)⁴ anisotropy is read off the
DIFFERENCE between bond-direction and face-direction propagation — the cubic
symmetry the continuum photon inherits (clm-pp3qwf). The Cartesian (x,y,z)
labels for the three translation DOF are the CONTINUUM strain-tensor axes the
mechanical constitutive tensor is written in, not a grid stencil.

Canonical leaf:
  `manuscript/ave-kb/vol9/ch3-pin-port-configuration/per-dof-vacuum-node-circuit.md`
"""

import numpy as np

from ave.core.constants import EPSILON_0, L_NODE, MU_0

# Tetrahedral (K4 / diamond) bond directions — the four ports of the native
# AVE lattice (k4_tlm.py:110-117), UNIT-normalized. The continuum-limit
# dispersion is sampled along these to expose the lattice's cubic anisotropy,
# NOT along a Cartesian 6-port stencil (substrate-native / RANK-2 guard).
K4_BOND_DIRECTIONS = (
    np.array([+1.0, +1.0, +1.0]) / np.sqrt(3.0),
    np.array([+1.0, -1.0, -1.0]) / np.sqrt(3.0),
    np.array([-1.0, +1.0, -1.0]) / np.sqrt(3.0),
    np.array([-1.0, -1.0, +1.0]) / np.sqrt(3.0),
)


class PerDOFVacuumNode:
    """A single vacuum node carrying an INDEPENDENT reactive pair (L_i, C_i)
    per translation DOF i ∈ {x, y, z}.

    The cold-vacuum baseline per DOF is the cell-level pair (device-circuit-models.md
    §1, line 52):
        L_cell = μ₀ · ℓ_node   [the metric inductance per node-span]
        C_cell = ε₀ · ℓ_node   [the metric capacitance per node-span]
    giving c_i = 1/√(L_i C_i) = 1/√(μ₀ε₀) = c₀ and
            Z_i = √(L_i / C_i) = √(μ₀/ε₀) = Z₀ for every i (isotropic cold vacuum).

    A STATE is applied as a per-DOF multiplicative pair (lL_i, lC_i) on the
    baseline:  L_i = lL_i · L_cell,  C_i = lC_i · C_cell. The three regimes are
    three choices of these multipliers (see classmethods below).

    Constitutive TENSOR, not scalar: storing one pair per DOF is exactly what a
    scalar node cannot do — a scalar node cannot represent the directional
    anisotropy that deviatoric (shear) strain induces. That is the structural
    reason the per-DOF layer is REQUIRED beneath the cell model.
    """

    def __init__(self, lL=(1.0, 1.0, 1.0), lC=(1.0, 1.0, 1.0), ell_node=L_NODE):
        self.ell_node = float(ell_node)
        self.L_cell = MU_0 * self.ell_node
        self.C_cell = EPSILON_0 * self.ell_node
        self.lL = np.asarray(lL, dtype=float)
        self.lC = np.asarray(lC, dtype=float)
        if self.lL.shape != (3,) or self.lC.shape != (3,):
            raise ValueError("lL and lC must each be length-3 (per translation DOF x,y,z)")

    @property
    def L(self):
        """Per-DOF inductance L_i  [H]."""
        return self.lL * self.L_cell

    @property
    def C(self):
        """Per-DOF capacitance C_i  [F]."""
        return self.lC * self.C_cell

    @property
    def c(self):
        """Per-DOF wave speed c_i  [m/s].

        L_cell = μ₀·ℓ_node and C_cell = ε₀·ℓ_node are LUMPED per-NODE values
        (Henries, Farads), so √(L_i C_i) is the propagation DELAY across one
        node-span of physical length ℓ_node. The section wave speed is therefore
            c_i = ℓ_node / √(L_i C_i).
        For the cold cell (L_cell C_cell = μ₀ε₀·ℓ_node²) this gives
            c_i = ℓ_node / (ℓ_node √(μ₀ε₀)) = 1/√(μ₀ε₀) = c₀.
        (The bare 1/√(LC) form holds only for PER-UNIT-LENGTH L, C; here L, C
        are lumped per node, so the ℓ_node factor is required to recover c₀ —
        caught by the VALIDATE-ON-KNOWN gate.)
        """
        return self.ell_node / np.sqrt(self.L * self.C)

    @property
    def Z(self):
        """Per-DOF characteristic impedance Z_i = √(L_i / C_i)  [Ω]."""
        return np.sqrt(self.L / self.C)

    # --- The three regimes as constructors ---------------------------------

    @classmethod
    def isotropic_saturated(cls, n, ell_node=L_NODE):
        """REGIME 1 — ISOTROPIC volumetric saturation (the SYM ε·μ co-scale).

        Per achromatic-impedance-matching.md: under volumetric strain BOTH μ
        and ε scale UP by the same refractive factor n(r):
            μ' = n·μ₀,  ε' = n·ε₀   (achromatic-impedance-matching.md:20).
        At the node this is L_i and C_i co-scaling EQUALLY across all i:
            lL_i = lC_i = n  for every i.
        Consequence:
            c_i = 1/√(n·L_cell · n·C_cell) = c₀/n   (uniform, isotropic, achromatic)
            Z_i = √(n·L_cell / (n·C_cell)) = Z₀     (INVARIANT → Γ = 0, matched)
        Light bends (c drops by 1/n) but does NOT disperse (n same all dirs) or
        reflect (Z = Z₀). This is the node-level SYM ε·μ co-scale.
        """
        n = float(n)
        return cls(lL=(n, n, n), lC=(n, n, n), ell_node=ell_node)

    @classmethod
    def deviatoric(cls, n, delta, ell_node=L_NODE):
        """REGIME 2 — DEVIATORIC (shear) strain → the pairs SPLIT.

        A deviatoric (traceless) strain breaks the isotropy: it ADDS to one
        direction what it REMOVES from another (volume-preserving). We apply it
        symmetrically to the co-scaled isotropic background n, on the ε / C side
        (the metric-varactor sector that carries the index, vacuum-birefringence-e4.md:12
        "only ε strained"):
            lC = (n·(1+δ), n·(1-δ), n),   lL = (n, n, n).
        Then L_x·C_x = n²(1+δ)·L_cell·C_cell ≠ L_y·C_y = n²(1-δ)·(...), so
            c_x = c₀ / (n√(1+δ)) ≠ c_y = c₀ / (n√(1-δ))
        — a DIRECTIONAL wave speed = BIREFRINGENCE. The Δc/c between the x and y
        polarizations is the strain-induced birefringence FORM (the coefficient
        is a separate quantitative test, vacuum-birefringence-e4.md). ``delta``
        is the deviatoric-strain amplitude (dimensionless).
        """
        n = float(n)
        delta = float(delta)
        return cls(
            lL=(n, n, n),
            lC=(n * (1.0 + delta), n * (1.0 - delta), n),
            ell_node=ell_node,
        )

    def birefringence(self):
        """Δc/c between the two split polarizations (the deviatoric FORM).

        Returns (c_x − c_y)/c_mean for the first two DOF. Zero for an isotropic
        node; nonzero and ∝(deviatoric split) for a deviatoric node.
        """
        cx, cy = self.c[0], self.c[1]
        return (cx - cy) / (0.5 * (cx + cy))


def lattice_dispersion(node, q, direction):
    """Discrete-lattice dispersion ω(q) for a wave on the per-DOF K4 node lattice.

    SUBSTRATE-NATIVE (the RANK-2 lesson). The dispersion is built from the ACTUAL
    K4 / tetrahedral bond set (`K4_BOND_DIRECTIONS`, the four ports of k4_tlm.py),
    NOT a direction-projected scalar |q| ladder. A scalar-|q| sin(qℓ/2) law
    depends on |q| only and has ZERO directional anisotropy by construction — it
    CANNOT produce the cubic-symmetry (q·ℓ)⁴ tell. The genuine lattice dispersion
    is the bond-sum structure factor: a Bloch wave exp(i q·r) on the bond set has
    the dynamical-matrix eigenvalue

        ω(q)² = (c² / ℓ_node²) · (2/N_bonds) · Σ_{b}  [ 1 − cos(q · b̂ ℓ_node) ]

    summed over the N_bonds = 4 unit bond vectors b̂ (normalised so the cold-lattice
    long-wavelength limit recovers ω = c·|q|; the per-DOF c² enters through the
    direction-weighted node speed for an anisotropic node).

    Continuum (q·ℓ_node ≪ 1) expansion of the bond-sum:

        Σ_b [1 − cos(q·b̂ ℓ)] = ½(qℓ)² · Σ_b (q̂·b̂)²
                                  − (1/24)(qℓ)⁴ · Σ_b (q̂·b̂)⁴ + ...

    The ISOTROPIC part (the (qℓ)² term) is direction-independent for the
    tetrahedral set (Σ_b (q̂·b̂)² = 4/3 for any q̂, by the tetrahedral 2nd-moment
    identity). The ANISOTROPY first appears at (qℓ)⁴ through Σ_b (q̂·b̂)⁴, which
    is a CUBIC INVARIANT (it differs between bond-direction and face-direction
    propagation) — that is the clm-pp3qwf cubic-symmetry discreteness tell:
    achromatic only as λ → ∞ (qℓ → 0). The lattice is isotropic at O((qℓ)²) and
    its leading anisotropy is O((qℓ)⁴).

    Args:
        node: a PerDOFVacuumNode.
        q: wavenumber magnitude [1/m] (scalar or array).
        direction: length-3 propagation vector (need not be unit; normalised here).

    Returns:
        ω(q) [rad/s], same shape as q.
    """
    qhat = np.asarray(direction, dtype=float)
    qhat = qhat / np.linalg.norm(qhat)
    # Direction-weighted node speed (anisotropy enters only for a non-isotropic
    # node; for the cold/isotropic node c_dir = c₀ along every direction).
    c_dir = np.sqrt(np.sum(qhat**2 * node.c**2))
    ell = node.ell_node
    q = np.asarray(q, dtype=float)
    bonds = np.stack(K4_BOND_DIRECTIONS)  # (4, 3) unit bond vectors
    # phase q·b̂·ℓ for each bond; q is scalar-or-array → broadcast over bonds axis
    qb = np.multiply.outer(q, bonds @ qhat) * ell  # shape (..., 4)
    # Numerically stable structure factor: 1 − cos(x) = 2 sin²(x/2) avoids the
    # catastrophic cancellation of (1 − cos) at small x (deep-continuum q·ℓ ≪ 1).
    structure = np.sum(2.0 * np.sin(0.5 * qb) ** 2, axis=-1)  # Σ_b [1 − cos(q·b̂ ℓ)]
    # Normalised so cold long-wavelength limit → ω = c·q:
    #   structure → ½(qℓ)²·(4/3) = (2/3)(qℓ)²; with prefactor (c²/ℓ²)·(2/N)·structure
    #   = (c²/ℓ²)·(1/2)·(2/3)(qℓ)² = (c²/ℓ²)·(1/3)... — fix the constant so the
    #   coefficient is exactly c²q². The tetrahedral 2nd-moment is 4/3, N=4, so
    #   the matching prefactor is 3/(2·N)·(... ) → derived below to give c²q².
    # ω² = (c²/ℓ²)·K·structure with K chosen s.t. K·(2/3)(qℓ)² = (qℓ)² → K = 3/2.
    omega_sq = (c_dir**2 / ell**2) * 1.5 * structure
    return np.sqrt(np.maximum(omega_sq, 0.0))


def phase_speed(node, q, direction):
    """Phase speed ω(q)/q for the discrete lattice [m/s]."""
    q = np.asarray(q, dtype=float)
    w = lattice_dispersion(node, q, direction)
    return w / q


def directional_anisotropy(node, q, dir_a, dir_b):
    """Fractional phase-speed anisotropy [v(dir_a) − v(dir_b)] / v_mean at
    wavenumber q for the scalar bond-sum dispersion.

    This is the **(q·ℓ)² ZONE-EDGE form** — the leading lattice discreteness that
    a lattice-LOCKED MATTER carrier sees (binary-kill-switches.md:17 "the
    (qℓ_node)² zone-edge bending is a lattice-mode property of matter carriers").
    The leading speed correction v/c = 1 − (1/32)(qℓ)²·M₄(q̂) has a
    direction-dependent coefficient M₄ = Σ_b(q̂·b̂)⁴ (the cubic invariant), so the
    direction-to-direction anisotropy scales as (q·ℓ)². This is NOT the photon
    birefringence — see ``polarization_birefringence`` for the (q·ℓ)⁴ form.
    """
    va = phase_speed(node, q, dir_a)
    vb = phase_speed(node, q, dir_b)
    return (va - vb) / (0.5 * (va + vb))


def cubic_anisotropy_invariant(direction):
    """The traceless QUARTIC cubic invariant Ξ(q̂) = (q̂_x⁴+q̂_y⁴+q̂_z⁴) − 3/5.

    Per the diamond-cubic (Fd-3m) group theory (preferred-frame-and-emergent-lorentz.md
    §2, clm-yr6tu4):
      * the quadratic invariant is |q|² — ISOTROPIC for the cubic point group
        (so EM corrections at O(q²) carry NO anisotropy);
      * the FIRST anisotropic invariant is the QUARTIC q_x⁴+q_y⁴+q_z⁴, which
        DIFFERS from the isotropic |q|⁴.
    Subtracting the isotropic average ⟨q̂_x⁴+q̂_y⁴+q̂_z⁴⟩ = 3/5 over the sphere
    gives the TRACELESS anisotropy Ξ(q̂): it is ZERO at the isotropic average and
    nonzero (cubic-symmetric) off the high-symmetry axes. Ξ vanishes on neither
    [100] (Ξ = +2/5) nor [111] (Ξ = −2/15) — these are the extremal cubic axes;
    it is the SIGN-changing cubic harmonic that makes the photon birefringence
    direction-dependent at order (q·ℓ)⁴.
    """
    qhat = np.asarray(direction, dtype=float)
    qhat = qhat / np.linalg.norm(qhat)
    return float(np.sum(qhat**4) - 3.0 / 5.0)


def photon_birefringence(node, q, direction):
    """Continuum-EM (photon) optical birefringence δ — the corpus **(q·ℓ)⁴ form**
    (clm-pp3qwf, preferred-frame-and-emergent-lorentz.md §2).

    GRADE DISTINCTION (the honest finding of this build). The continuum PHOTON
    (Z₀-matched, sub-saturation, NOT lattice-locked — weak-C, binary-kill-switches.md:17)
    differs from a lattice-LOCKED MATTER carrier:
      * the matter carrier's zone-edge anisotropy is **(q·ℓ)²** — the mechanical
        dynamical-matrix tensor Σ_b b̂_a b̂_b(q·b̂)² is already anisotropic at O(q²);
        this is what ``directional_anisotropy`` measures.
      * the photon's O(q²) correction is the ISOTROPIC cubic invariant |q|² (no
        anisotropy at O(q²)), so its first anisotropy is the QUARTIC cubic
        invariant → **(q·ℓ)⁴**.
    The photon birefringence FORM is therefore

        δ(q, q̂) = κ · (q·ℓ_node)⁴ · Ξ(q̂)

    with Ξ the traceless cubic invariant (``cubic_anisotropy_invariant``) and κ an
    O(1) coefficient. This function returns the FORM with κ = 1/24 (the leading
    cosine-expansion coefficient of the lattice structure factor) — the SCALING
    in (q·ℓ)⁴ and the cubic direction-dependence are the demonstrated content; the
    absolute magnitude (δ ≈ 2.2×10⁻²² at λ=633 nm) is a separate quantitative test
    (vacuum-birefringence-e4.md, clm-pp3qwf), NOT re-derived here.

    A node argument is accepted for interface symmetry; the photon mode rides the
    Z₀-matched EM channel (achromatic in the continuum), so the birefringence is a
    pure lattice-geometry (q·ℓ) effect independent of the per-DOF saturation state
    of the node — the node's isotropic n only rescales c, not the anisotropy ratio.
    """
    ell = node.ell_node
    q = np.asarray(q, dtype=float)
    xi = cubic_anisotropy_invariant(direction)
    return (1.0 / 24.0) * (q * ell) ** 4 * xi
