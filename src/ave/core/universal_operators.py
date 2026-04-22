import jax
import numpy as np

from ave.core.constants import EPS_CLIP, EPS_NUMERICAL

"""
Universal Topological Operators
===============================

This module defines the ten fundamental, scale-invariant operators of the
Applied Vacuum Engineering (AVE) framework:

 1. Impedance (Z)               — Axiom 1
 2. Saturation (S)              — Axiom 4
 3. Reflection (Γ)              — Axiom 3
 4. Pairwise Energy (U)         — Axioms 1-4
 5. Y-Matrix → S-Matrix (Y→S)   — Axiom 3 (multiport)
 6. Eigenvalue Target (λ_min)   — Axiom 3 (eigenstate)
 7. Spectral Analysis (FFT)     — DSP complement to SPICE
 8. Packing Reflection (Γ_pack) — Axioms 3+4 (macroscopic)
 9. Steric Reflection (Γ_steric) — Axiom 3 (pairwise exclusion)
10. Junction Projection Loss (Y) — Axioms 1+2 (crossing geometry)
11. Topological Curl (∇×V)       — Continuum constraint map
12. Topological Divergence (∇·V) — Gauss face summation
13. D'Alembertian Wave (◻²)      — Invariant wave equation
14. Dynamic Impedance (Z_eff)    — Non-linear strained divergence
15. Virtual Strain Iso (r_v)     — SwiGLU logic-to-physics map

These operators are domain-agnostic and should be imported by all downstream
solvers (Nuclear, Fluid, EE, Protein Folding, and Atomic) to ensure strict
adherence to the core axioms without local redefinitions.
"""


def _is_jax_array(x: object) -> bool:
    try:
        import jax
        import jax.numpy as jnp

        return isinstance(x, (jnp.ndarray, jax.Array))
    except ImportError:
        return False


def universal_impedance(mu: float | np.ndarray, eps: float | np.ndarray) -> float | np.ndarray:
    """
    Operator 1: The Universal Impedance Operator (Z)
    Defines the resistance of an arbitrary medium to a propagating wave.

    Args:
        mu: Inertial/magnetic density (e.g., mu_0, fluid shear resistance, inductance)
        eps: Elastic compliance (e.g., eps_0, fluid density, capacitance)

    Returns:
        Z: The characteristic impedance of the medium.
    """
    # Duck-typing allows this to work with both numpy and jax.numpy
    return (mu / eps) ** 0.5


def universal_saturation(A: float | np.ndarray, A_yield: float) -> float | np.ndarray:
    """
    Operator 2: The Universal Saturation Operator (S)
    Imposes the geometric percolation limit of the 3D lattice. Strain cannot
    increase infinitely; as the limit is approached, the metric non-linearly stiffens.

    Args:
        A: The current strain amplitude (e.g., Voltage, Velocity, Fluid Stress)
        A_yield: The absolute topological yield limit of the domain

    Returns:
        S: The saturation factor (real-valued in [0, 1]).
    """
    # Clip the ratio to a maximum of 1.0 to prevent imaginary roots (metric breakdown)
    # Using simple operators to support both raw floats, numpy arrays, and jax arrays.
    # Note: duck-typing assumes the caller handles the appropriate jnp/np where
    # branching/clipping is complex. A simple algebraic form is best for cross-compatibility.
    import numpy as np

    # Try to use JAX if the input is a JAX array, otherwise use NumPy
    is_jax = _is_jax_array(A)

    if is_jax:
        import jax.numpy as jnp

        ratio = jnp.clip(A / A_yield, -1.0, 1.0)
        return jnp.sqrt(1.0 - ratio**2)
    else:
        ratio = np.clip(A / A_yield, -1.0, 1.0)
        return np.sqrt(1.0 - ratio**2)


def universal_reflection(
    Z1: float | np.ndarray,
    Z2: float | np.ndarray,
    eps: float = EPS_NUMERICAL,
) -> float | np.ndarray:
    """
    Operator 3: The Universal Reflection Operator (Gamma)
    Governs how much energy is transferred versus reflected when a wave
    encounters a boundary between two topological impedances (Z1 -> Z2).

    Args:
        Z1: The characteristic impedance of the source/incident medium
        Z2: The characteristic impedance of the target medium
        eps: Small numerical constant to prevent div-by-zero, especially
             useful for auto-differentiation in JAX loss functions.

    Returns:
        Gamma: The reflection coefficient (-1.0 to 1.0).
    """
    return (Z2 - Z1) / (Z2 + Z1 + eps)


def universal_pairwise_energy(
    r: float | np.ndarray,
    K: float,
    d_sat: float,
) -> float | np.ndarray:
    """
    Operator 4: Full 3-Regime Pairwise Potential (Impedance-Based)

    Computes the interaction energy between two nodes at separation r
    using the FULL impedance matching dynamics of the saturated lattice.

    The three regimes are encoded through the local impedance:

    1. LINEAR (r >> d_sat): Z ≈ Z₀, Γ ≈ 0 → U ≈ -K/r
    2. NON-LINEAR (r ~ d_sat): Z rises, partial reflection → reduced coupling
    3. SATURATED (r ≤ d_sat): Z → ∞, Γ → 1 → repulsive wall (Pauli exclusion)

    The potential is:
        U(r) = -(K/r) × (T² - R²)
    where:
        A(r)  = d_sat/r           (strain amplitude, normalized to yield at d_sat)
        Z(r)  = Z₀ / (1-A²)^¼    (impedance at strain, from scale_invariant)
        Γ(r)  = (Z-Z₀)/(Z+Z₀)    (reflection coefficient)
        R² = Γ², T² = 1 - Γ²     (power reflection/transmission)

    This naturally produces:
        - No equilibrium from the potential alone (monotonic beyond wall)
        - Equilibrium comes from the eigenvalue (5-step regime boundary method)
        - Repulsive wall at exactly r = d_sat with no ad-hoc parameters

    Args:
        r: Separation distance (scalar or array, same units as d_sat)
        K: Coupling constant (K_MUTUAL, αℏc, Gm², etc.)
        d_sat: Saturation radius (D_PROTON, Slater radius, r_s, etc.)

    Returns:
        U: Pairwise energy. Negative = attractive, positive = repulsive wall.
    """

    is_jax = _is_jax_array(r)
    if is_jax:
        import jax.numpy as jnp

        ratio_sq = jnp.clip((d_sat / r) ** 2, 0.0, 1.0 - EPS_CLIP)
        # Impedance ratio: Z/Z₀ = 1/(1-A²)^(1/4) where A² = ratio_sq
        S_quarter = (1.0 - ratio_sq) ** 0.25
        Z_ratio = 1.0 / S_quarter  # Z_local / Z_0
        Gamma = (Z_ratio - 1.0) / (Z_ratio + 1.0)
        Gamma_sq = Gamma**2
        T_sq = 1.0 - Gamma_sq
        return -(K / r) * (T_sq - Gamma_sq)
    else:
        if np.isscalar(r):
            ratio_sq = (d_sat / r) ** 2
            if ratio_sq >= 1.0:
                # Deep inside saturation: Γ → 1, T² → 0, R² → 1
                # U → +(K/r) (full reflection = Pauli wall)
                return K / r
            S_quarter = (1.0 - ratio_sq) ** 0.25
            Z_ratio = 1.0 / S_quarter
            Gamma = (Z_ratio - 1.0) / (Z_ratio + 1.0)
            Gamma_sq = Gamma**2
            return -(K / r) * (1.0 - 2.0 * Gamma_sq)
        else:
            r = np.asarray(r, dtype=float)
            result = np.zeros_like(r)
            ratio_sq = (d_sat / r) ** 2
            wall = ratio_sq >= 1.0
            ok = ~wall
            # Saturated wall: Pauli repulsion
            result[wall] = K / r[wall]
            # Dynamic regime
            S_quarter = (1.0 - ratio_sq[ok]) ** 0.25
            Z_ratio = 1.0 / S_quarter
            Gamma = (Z_ratio - 1.0) / (Z_ratio + 1.0)
            Gamma_sq = Gamma**2
            result[ok] = -(K / r[ok]) * (1.0 - 2.0 * Gamma_sq)
            return result


def universal_pairwise_energy_jax(r: jax.Array, K: float, d_sat: float) -> jax.Array:
    """
    Operator 4 (JAX-only): JIT-safe pairwise impedance potential.

    Mathematically identical to universal_pairwise_energy() but uses only
    jax.numpy operations with no Python-level branching or duck-typing.
    Safe for use inside @jax.jit compiled functions.

    U(r) = -(K/r) × (T² - Γ²)
    where Γ = (Z_eff/Z₀ - 1) / (Z_eff/Z₀ + 1)
    and   Z_eff/Z₀ = 1/(1 - (d_sat/r)²)^{1/4}

    Args:
        r: Separation distance (JAX array).
        K: Coupling constant.
        d_sat: Saturation radius.

    Returns:
        U: Pairwise energy (JAX array, same shape as r).
    """
    import jax.numpy as jnp

    ratio_sq = jnp.clip((d_sat / r) ** 2, 0.0, 1.0 - EPS_CLIP)
    S_quarter = (1.0 - ratio_sq) ** 0.25
    Z_ratio = 1.0 / S_quarter
    Gamma = (Z_ratio - 1.0) / (Z_ratio + 1.0)
    Gamma_sq = Gamma**2
    T_sq = 1.0 - Gamma_sq
    return -(K / r) * (T_sq - Gamma_sq)


def universal_pairwise_gradient(
    r: float | np.ndarray,
    K: float,
    d_sat: float,
) -> float | np.ndarray:
    """
    Analytical gradient (dU/dr) of the full 3-regime impedance potential.

    For U(r) = -(K/r)(1 - 2Γ²), computed via numerical derivative
    for correctness (the analytical form is complex due to the
    impedance chain).

    Sign convention: positive = repulsive force, negative = attractive.

    Args:
        r: Separation distance
        K: Coupling constant
        d_sat: Saturation radius

    Returns:
        dU_dr: Gradient of the pairwise potential.
    """
    import numpy as np

    dr = 1e-8 * (r if np.isscalar(r) else np.maximum(r, EPS_CLIP))
    U_plus = universal_pairwise_energy(r + dr, K, d_sat)
    U_minus = universal_pairwise_energy(r - dr, K, d_sat)
    return (U_plus - U_minus) / (2.0 * dr)


def universal_ymatrix_to_s(Y: np.ndarray, Y0: float = 1.0) -> np.ndarray:
    """
    Operator 5: The Universal Y-Matrix → S-Matrix Conversion

    Converts an N-port nodal admittance matrix [Y] to its scattering
    matrix [S].  This is the multiport generalisation of the reflection
    operator Γ = (Z₂ - Z₁)/(Z₂ + Z₁).

    The conversion follows:
        [S] = (I + [Y]/Y₀)⁻¹ · (I − [Y]/Y₀)

    which is equivalent to:
        [S] = (I − Z₀[Y]) · (I + Z₀[Y])⁻¹     (impedance normalised)

    This operator is domain-agnostic and is used at:
      - Nuclear scale:  K_MUTUAL eigenvalues from nuclear Y-matrix
      - Protein scale:  λ_min(S†S) for fold eigenstate
      - Antenna scale:  S-parameters for HOPF-01 matching

    Args:
        Y:  NxN complex admittance matrix (numpy or jax array)
        Y0: Reference admittance (scalar). Default: 1.0 (normalised)

    Returns:
        S:  NxN complex scattering matrix
    """
    import numpy as np

    is_jax = _is_jax_array(Y)

    if is_jax:
        import jax.numpy as jnp

        N = Y.shape[0]
        I = jnp.eye(N, dtype=Y.dtype)
        Y_norm = Y / Y0
        A = I + Y_norm
        B = I - Y_norm
        return jnp.linalg.solve(A, B)
    else:
        N = Y.shape[0]
        I = np.eye(N, dtype=Y.dtype)
        Y_norm = Y / Y0
        A = I + Y_norm
        B = I - Y_norm
        return np.linalg.solve(A, B)


def universal_eigenvalue_target(S: np.ndarray) -> float:
    """
    Operator 6: The Universal Eigenvalue Ground-State Target

    Computes the smallest eigenvalue of S†S for an N-port scattering
    matrix [S].  When λ_min → 0, the network has a zero singular value:
    one mode is perfectly absorbed — the system is in its geometric
    ground state.

    This operator is domain-agnostic:
      - Nuclear scale:  λ_min(S†S) = 0 → nuclear binding eigenstate
      - Protein scale:  λ_min(S†S) = 0 → native fold
      - Antenna scale:  λ_min(S†S) = 0 → impedance-matched resonance

    Args:
        S:  NxN complex scattering matrix (numpy or jax array)

    Returns:
        lambda_min:  Smallest eigenvalue of S†S (real, ≥ 0)
    """
    import numpy as np

    is_jax = _is_jax_array(S)

    if is_jax:
        import jax.numpy as jnp

        SdS = jnp.conj(S.T) @ S
        eigenvalues = jnp.linalg.eigvalsh(SdS)
        return eigenvalues[0]  # smallest eigenvalue
    else:
        SdS = np.conj(S.T) @ S
        eigenvalues = np.linalg.eigvalsh(SdS)
        return eigenvalues[0]


def universal_spectral_analysis(Z_sequence: np.ndarray) -> dict[str, np.ndarray]:
    """
    Operator 7: The Universal Impedance Spectral Analyser

    Computes the spatial Fourier transform of a 1D impedance profile.
    Returns the mode amplitudes and dominant spatial frequencies.

    For a protein backbone:
      - Peak at k ≈ N/3.7 → α-helix periodicity (Q/2 ≈ 3.7 residues/turn)
      - Peak at k ≈ N/2.0 → β-sheet periodicity (2 residues/strand)
      - DC component (k=0) → mean impedance level

    For any 1D impedance sequence:
      - Peaks identify resonant mode spacings
      - Power spectrum P(k) = |FFT|² gives the spatial PSD
      - Autocorrelation R(n) = IFFT(P) gives correlation length

    This is the DSP complement to the time-domain SPICE integrator.

    Args:
        Z_sequence:  1D array of impedance values (real or complex)

    Returns:
        dict with keys:
          'spectrum':     Complex FFT coefficients
          'power':        Power spectral density |FFT|²
          'frequencies':  Spatial frequency indices (0 to N-1)
          'autocorr':     Spatial autocorrelation function
          'dominant_k':   Top 5 dominant spatial frequencies (by power)
          'dominant_periods': Corresponding spatial periods (residues)
    """
    import numpy as np

    Z = np.asarray(Z_sequence, dtype=complex)
    N = len(Z)

    # FFT of the impedance sequence
    spectrum = np.fft.fft(Z)

    # Power spectral density
    power = np.abs(spectrum) ** 2

    # Autocorrelation via Wiener-Khinchin
    autocorr = np.real(np.fft.ifft(power))
    autocorr /= autocorr[0] if autocorr[0] != 0 else 1.0  # normalise

    # Dominant modes (skip DC at k=0)
    k_indices = np.arange(N)
    power_no_dc = power.copy()
    power_no_dc[0] = 0  # mask DC
    top_k = np.argsort(power_no_dc)[::-1][:5]
    top_periods = np.where(top_k > 0, N / top_k, np.inf)

    return {
        "spectrum": spectrum,
        "power": power,
        "frequencies": k_indices,
        "autocorr": autocorr,
        "dominant_k": top_k,
        "dominant_periods": top_periods,
    }


def universal_packing_reflection(
    Rg_sq: float | np.ndarray,
    N: int,
    r_node: float,
    eta_eq: float,
) -> float | np.ndarray:
    """
    Operator 8: The Universal Packing Reflection Coefficient

    Computes the macroscopic reflection coefficient Γ_pack that measures
    how far a confined system is from its Axiom 4 equilibrium packing.

    FULL DERIVATION CHAIN (zero free parameters):
    ─────────────────────────────────────────────
    α  = 7.2973e-3           (Axiom 2: fine-structure constant, INPUT)
    P_C = 8πα ≈ 0.1834       (Axiom 4: volumetric percolation threshold)
    ν   = 2/7                (Axiom 3: Poisson ratio → 7 compliance modes)

    Of the 7 lattice compliance modes, only 5 are TRANSVERSE (spatial).
    The 2 longitudinal modes carry energy along the chain but do not
    contribute to 3D inter-element packing contacts.

    η_eq = P_C × (1 - ν) = P_C × 5/7 ≈ 0.1310

    For a system of N nodes, finite-size correction:
        η(N) = η_eq × (1 - 1/N)

    Node radius r_node is also axiom-derived (for protein):
        d₀ = 3.80 Å      (measured BC: backbone pitch)
        J  = (1/√3)(1+P_C)  (sp³ projection + packing correction)
        r_node = d₀ × J / 2  (half the steric exclusion diameter)
        = 1.298 Å

    Steps:
        1. η(N) = η_eq × (1 - 1/N)            (Axiom 4 + finite-size)
        2. V_node = (4/3)π r_node³             (geometry)
        3. R_target = (3NV / (4πη))^(1/3)      (uniform sphere model)
        4. Rg_target = √(3/5) × R_target       (sphere Rg)
        5. Γ_pack = (Rg - Rg_target)/(Rg + Rg_target)  (Axiom 3)

    Cross-scale application:
      - Protein:   r_node = R_NODE = 1.298 Å, η_eq = ETA_EQ = 0.131
      - Nuclear:   r_node = d_proton, η_eq = 1 (close-packed)
      - Fluid:     r_node = molecular radius, η_eq from lattice type

    Args:
        Rg_sq:    Radius of gyration SQUARED (same units as r_node²)
        N:        Number of nodes in the system
        r_node:   Axiom-derived node radius (R_NODE for protein)
        eta_eq:   Equilibrium packing fraction (ETA_EQ = P_C × 5/7 for protein)

    Returns:
        Gamma_pack_sq: Γ_pack² — the macroscopic packing mismatch power.
                       Add directly to any eigenvalue loss function.
    """
    import numpy as np

    is_jax = _is_jax_array(Rg_sq)

    if is_jax:
        import jax.numpy as jnp

        _max = jnp.maximum
        _sqrt = jnp.sqrt
        _pi = jnp.pi
    else:
        _max = np.maximum
        _sqrt = np.sqrt
        _pi = np.pi

    # Axiom 4: equilibrium packing fraction with finite-size correction
    eta_target = eta_eq * (1.0 - 1.0 / _max(N, 2.0))

    # Geometry: volume per node → target sphere radius → target Rg
    V_res = (4.0 / 3.0) * _pi * r_node**3
    R_target = (3.0 * N * V_res / (4.0 * _pi * eta_target + EPS_NUMERICAL)) ** (1.0 / 3.0)
    Rg_target = _sqrt(3.0 / 5.0) * R_target

    # Axiom 3: packing reflection coefficient
    Rg_actual = _sqrt(Rg_sq + EPS_NUMERICAL)
    Gamma_pack = (Rg_actual - Rg_target) / (Rg_actual + Rg_target + EPS_NUMERICAL)

    return Gamma_pack**2


def universal_steric_reflection(
    dists: np.ndarray,
    R_excl: float | np.ndarray,
    mask: np.ndarray,
) -> float | np.ndarray:
    """
    Operator 9: The Universal Steric Reflection Coefficient

    Computes the pairwise steric exclusion reflection coefficient using
    Axiom 3 applied at the atomic/node level.

    DERIVATION:
    ───────────
    Axiom 3 states that the reflection coefficient at any impedance
    boundary is:
        Γ = (Z₁ - Z₂) / (Z₁ + Z₂)

    For steric exclusion, the "impedance boundary" is the Pauli exclusion
    sphere. When two nodes approach closer than their exclusion distance R,
    the overlap creates an impedance mismatch proportional to the fractional
    violation:

        Γ_ij = max(0, (R_excl - d_ij) / (R_excl + d_ij))

    Properties:
      - d ≥ R:  Γ = 0     (no violation, no reflection)
      - d = 0:  Γ = 1     (total overlap, total reflection)
      - d = R/2: Γ = 1/3  (partial overlap)
      - Γ² ∈ [0, 1]       — same units as Ops 6 and 8

    The total steric reflection is the average Γ² over all
    non-bonded pairs:
        ⟨Γ²_steric⟩ = (1/N_pairs) Σ_{i<j} Γ_ij²

    This operator is domain-agnostic:
      - Protein:  R = R_STERIC_CC, d = Cα distances, mask = |i-j| ≥ 3
      - Nuclear:  R = d_proton, d = nucleon distances
      - Fluid:    R = molecular radius, d = particle distances

    Args:
        dists:   (N, N) distance matrix between all node pairs
        R_excl:  Exclusion radius (scalar or (N,N) matrix for heterogeneous)
        mask:    (N, N) boolean mask of non-bonded pairs to consider

    Returns:
        Gamma_steric_sq: ⟨Γ²⟩ — average pairwise steric mismatch power.
                         Add directly to any eigenvalue loss function.
    """
    import numpy as np

    is_jax = _is_jax_array(dists)

    if is_jax:
        import jax.numpy as jnp

        _max = jnp.maximum
        _sum = jnp.sum
        _where = jnp.where
        _triu = jnp.triu
    else:
        _max = np.maximum
        _sum = np.sum
        _where = np.where
        _triu = np.triu

    # Axiom 3: pairwise reflection coefficient
    gamma = _max(0.0, (R_excl - dists) / (R_excl + dists + EPS_NUMERICAL))
    gamma = _where(mask, gamma, 0.0)

    # Upper triangle to avoid double-counting
    gamma_upper = _triu(gamma, k=1)

    # Average over non-bonded pairs
    n_pairs = _max(1.0, _sum(_triu(mask.astype(float), k=1)))

    return _sum(gamma_upper**2) / n_pairs


def universal_junction_projection_loss(theta: float | np.ndarray, c_crossings: int = 1) -> float | np.ndarray:
    """
    Operator 10: The Universal Junction Projection Loss (Y_loss)

    Computes the fractional energy lost when a propagating mode encounters
    a junction (crossing, bend, or link) at angle theta between the incident
    and transmitted waveguide directions.

    FULL DERIVATION FROM AVE AXIOMS
    ===============================

    Axiom 1 (Discrete lattice):
        A wave propagating along direction u1 encounters a junction where
        the waveguide axis changes to u2.  The lattice resolves this as a
        discrete discontinuity: one node is the last node of segment 1,
        the next node is the first node of segment 2.  The angle between
        them is theta = arccos(u1 . u2).

    Axiom 2 (Wave propagation, K = 2G):
        At the junction, the incident mode amplitude projects onto the
        output direction.  The projected amplitude fraction is cos(theta).
        The fraction NOT projected is (1 - cos(theta)).

        The 2*pi^2 normalization comes from the LATTICE GEOMETRY of the
        junction, not from fitting:

            pi   — from the standing wave boundary condition.  Each
                   segment is a half-wavelength resonator; the mode
                   spans pi radians of phase per segment.

            2*pi — from the azimuthal integration around the waveguide
                   cross-section.  The junction couples all azimuthal
                   modes of the cylindrical waveguide.

            Product: 2*pi * pi = 2*pi^2

        This is the solid-angle normalization of a waveguide junction on
        the discrete lattice.  It is the ONLY value consistent with the
        lattice geometry — not a parameter.

    The complete operator:

        Y_loss(theta, c) = c * (1 - cos(theta)) / (2 * pi^2)

    where c is the number of crossings per orbit (topological invariant).

    For the energy eigenvalue, the dispersion relation determines the
    power law of the correction:

        Linear regime   (E ~ k):   E_corr = E_bare * (1 - Y_loss)
        Quadratic regime (E ~ k^2): E_corr = E_bare * (1 - Y_loss)^2

    PACKING FLOOR (Axioms 1, 2):
        The FCC lattice (K=2G) has packing fraction phi = pi*sqrt(2)/6.
        Op10 drain acts on NODAL phase space (fraction phi).
        The void fraction (1-phi ~ 0.26) is geometrically inaccessible
        to junction scattering.  Therefore the correction factor has
        a floor:  f(Y) = max((1-Y)^2, 1-phi).
        The floor activates at Y_c = 1-sqrt(1-phi) ~ 0.49.
        See coupled_resonator.ionization_energy_circuit() for implementation.

    CROSS-SCALE VALIDATION
    ----------------------
    Scale       theta       c       Validated quantity           Error
    ---------   ---------   -----   --------------------------   -----
    Protein     109.47 deg  1       Backbone Q = 0.75*pi^2       sub-3A
    Baryon      90 deg      6       Borromean tensor volume       +0.7%
    Antenna     ~70 deg     var     HOPF-01 stub coupling          --
    Atomic      90 deg      2-4     Boron IE: 8.04 eV             -3.1%

    The same operator, same formula, same normalization at every scale.
    No domain-specific physics.  No coupling constants.  Just geometry.

    Args:
        theta:        Junction angle [radians] between incident and
                      transmitted waveguide directions.  Common values:
                        pi/2     = 90 deg  (Hopf link, Borromean crossing)
                        1.9106   = 109.47 deg (sp3 tetrahedral, backbone)
                        0        = 0 deg  (parallel, no loss)
        c_crossings:  Number of crossings per orbit or per segment.
                      Topological invariant:
                        Hopf link (same shell pair):   c = 2
                        2s-2p (cross-subshell):        c = 4
                        Borromean (proton):             c = 6
                        Protein backbone:              c = 1 per peptide

    Returns:
        Y_loss:  Total fractional projection loss (dimensionless, >= 0).
                 Apply to eigenvalue as:
                   Linear:    E = E_bare * (1 - Y_loss)
                   Quadratic: E = E_bare * (1 - Y_loss)**2
    """
    import numpy as np

    is_jax = _is_jax_array(theta)
    _cos = __import__("jax").numpy.cos if is_jax else np.cos

    single_crossing_loss = (1.0 - _cos(theta)) / (2.0 * np.pi**2)
    return c_crossings * single_crossing_loss


# @jax.jit(static_argnames=['field_type'])  # Removed to fix legacy JAX decorator crash
def universal_topological_curl(
    Vx: np.ndarray,
    Vy: np.ndarray,
    Vz: np.ndarray,
    dx: float = 1.0,
    field_type: str = "E",
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Operator 11: The Universal Topological Curl (∇×V)

    Maps the macroscopic continuum curl operator onto the discrete topological
    Yee-lattice. This guarantees exact conservation of macroscopic vorticity.
    Supports both Numpy and JAX arrays transparently via duck-typing.

    Args:
        Vx, Vy, Vz: The 3D tensor vector components representing the field.
        dx: The topological lattice spacing.
        field_type: 'E' (integer node edges) or 'H' (half-node faces), determining
                    the staggered stencil shift.

    Returns:
        curl_x, curl_y, curl_z: The discrete spatial rotations mapped onto the grid.
    """
    if field_type == "E":
        # E-field curl (produces H-field updates on half-mesh)
        cx = (Vz[:, 1:, :-1] - Vz[:, :-1, :-1]) - (Vy[:, :-1, 1:] - Vy[:, :-1, :-1])
        cy = (Vx[:-1, :, 1:] - Vx[:-1, :, :-1]) - (Vz[1:, :, :-1] - Vz[:-1, :, :-1])
        cz = (Vy[1:, :-1, :] - Vy[:-1, :-1, :]) - (Vx[:-1, 1:, :] - Vx[:-1, :-1, :])
    else:
        # H-field curl (produces E-field updates on integer-mesh)
        cx = (Vz[:, 1:, 1:] - Vz[:, :-1, 1:]) - (Vy[:, 1:, 1:] - Vy[:, 1:, :-1])
        cy = (Vx[1:, :, 1:] - Vx[1:, :, :-1]) - (Vz[1:, :, 1:] - Vz[:-1, :, 1:])
        cz = (Vy[1:, 1:, :] - Vy[:-1, 1:, :]) - (Vx[1:, 1:, :] - Vx[1:, :-1, :])

    return cx / dx, cy / dx, cz / dx


@jax.jit
def universal_topological_divergence(
    Vx: np.ndarray,
    Vy: np.ndarray,
    Vz: np.ndarray,
    dx: float = 1.0,
) -> np.ndarray:
    """
    Operator 12: The Universal Topological Divergence (∇·V)

    Maps the continuum divergence operator onto the discrete LC node sums.
    Structurally translates Gauss's continuous flux to a discrete face summation
    on the LC graph, assuring zero numerical loss.

    Returns:
        div_V: The scalar divergence field mapped strictly to the node centers.
    """
    div_x = Vx[1:, :, :] - Vx[:-1, :, :]
    div_y = Vy[:, 1:, :] - Vy[:, :-1, :]
    div_z = Vz[:, :, 1:] - Vz[:, :, :-1]

    # Resolving to the common interior staggered volume mapping:
    return (div_x[:, :-1, :-1] + div_y[:-1, :, :-1] + div_z[:-1, :-1, :]) / dx


@jax.jit
def universal_d_alembertian(
    Phi_current: np.ndarray,
    Phi_past: np.ndarray,
    c_squared: float,
    dt: float,
    dx: float,
) -> np.ndarray:
    """
    Operator 13: The Universal D'Alembertian Wave Operator (◻²)

    Maps the geometric invariant wave equation: ◻²Φ = ∇²Φ - (1/c²)∂²Φ/∂t² = 0
    onto the discrete topological LC lattice without introducing artificial
    smoothing or dissipative parameters.

    Returns:
        Phi_next: The time-advanced scalar amplitude conserving the wave geometry.
    """
    # 7-point 3D spatial Laplacian stencil
    laplacian_x = (Phi_current[2:, 1:-1, 1:-1] - 2 * Phi_current[1:-1, 1:-1, 1:-1] + Phi_current[:-2, 1:-1, 1:-1]) / (
        dx**2
    )
    laplacian_y = (Phi_current[1:-1, 2:, 1:-1] - 2 * Phi_current[1:-1, 1:-1, 1:-1] + Phi_current[1:-1, :-2, 1:-1]) / (
        dx**2
    )
    laplacian_z = (Phi_current[1:-1, 1:-1, 2:] - 2 * Phi_current[1:-1, 1:-1, 1:-1] + Phi_current[1:-1, 1:-1, :-2]) / (
        dx**2
    )
    laplacian = laplacian_x + laplacian_y + laplacian_z

    # Time evolution via 2nd-order central difference:
    # (Phi_next - 2*Phi_current + Phi_past) / dt^2 = c^2 * Laplacian
    Phi_next = 2 * Phi_current[1:-1, 1:-1, 1:-1] - Phi_past[1:-1, 1:-1, 1:-1] + (c_squared * (dt**2)) * laplacian
    return Phi_next


def universal_dynamic_impedance(
    Z_0: float | np.ndarray,
    S: float | np.ndarray,
    eps: float = EPS_NUMERICAL,
) -> float | np.ndarray:
    """
    Operator 14: The Universal Dynamic Impedance (Z_eff)

    Transforms the linear characteristic impedance Z_0 into the dynamic
    non-linear impedance of a strained medium. As the medium approaches
    saturation (S -> 0), the effective impedance diverges towards infinity,
    forming the Pauli exclusion wall (physical) or the token routing wall (virtual).

    Z_eff = Z_0 / sqrt(S)

    Args:
        Z_0: Linear characteristic base impedance (scalar or array)
        S: The saturation factor from universal_saturation, S in [0, 1]
        eps: Small numerical constant to prevent div-by-zero at complete yield

    Returns:
        Z_eff: The dynamic characteristic impedance
    """
    import numpy as np

    is_jax = _is_jax_array(S)

    if is_jax:
        import jax.numpy as jnp

        S_safe = jnp.maximum(S, eps)
        return Z_0 / jnp.sqrt(S_safe)
    else:
        S_safe = np.maximum(S, eps)
        return Z_0 / np.sqrt(S_safe)


def universal_virtual_strain(x: float | np.ndarray) -> float | np.ndarray:
    """
    Operator 15: The Universal Virtual Strain Isomorphism (r_virtual)

    Maps the dimensionless gate pre-activations x of a virtual neural
    manifold (e.g. SwiGLU) to the normalized physical strain r = A/A_c
    of the AVE vacuum lattice.

    Derived from the phase-conservation identity: sigma(x)^2 + r^2 = 1
    Therefore, r = sqrt(1 - sigma(x)^2)

    Args:
        x: Pre-activation logit scalar or array

    Returns:
        r: Normalized geometric strain in [0, 1]
    """
    import numpy as np

    is_jax = _is_jax_array(x)

    if is_jax:
        import jax.numpy as jnp

        sigma = 1.0 / (1.0 + jnp.exp(-x))
        return jnp.sqrt(jnp.maximum(0.0, 1.0 - sigma**2))
    else:
        sigma = 1.0 / (1.0 + np.exp(-x))
        return np.sqrt(np.maximum(0.0, 1.0 - sigma**2))


def universal_power_transmission(
    Z1: float | np.ndarray,
    Z2: float | np.ndarray | None = None,
) -> float | np.ndarray:
    """
    Operator 17: Universal Power Transmission (T²)

    The squared transmission coefficient representing the fraction of
    power transmitted across an impedance boundary.

    T² = 1 - Γ² = 4 Z₁ Z₂ / (Z₁ + Z₂)²

    This operator can be called with two impedances, or with a single
    impedance ratio N = Z₁/Z₂ or Z₂/Z₁.

    Args:
        Z1: First impedance, or the impedance ratio N if Z2 is None.
        Z2: Second impedance (optional).

    Returns:
        T²: Power transmission fraction [0, 1].
    """
    import numpy as np

    is_jax = _is_jax_array(Z1)
    if Z2 is not None:
        is_jax = is_jax or _is_jax_array(Z2)

    if is_jax:
        import jax.numpy as jnp

        if Z2 is None:
            N = Z1
        else:
            N = Z1 / jnp.maximum(Z2, EPS_NUMERICAL)
        return 4.0 * N / (1.0 + N) ** 2
    else:
        if Z2 is None:
            N = Z1
        else:
            # Prevent division by zero
            if np.isscalar(Z1) and np.isscalar(Z2) and Z2 == 0:
                if Z1 == 0:
                    return 1.0
                return 0.0
            N = Z1 / np.maximum(Z2, EPS_NUMERICAL)

        if np.isscalar(N) and N == 0:
            return 0.0
        return 4.0 * N / (1.0 + N) ** 2


def universal_regime_eigenvalue(r_sat: float, nu_vac: float, ell: int, c_wave: float) -> float:
    """
    Operator 20: Universal Regime Boundary Eigenvalue

    Universal eigenfrequency at any saturation boundary (the 5-step method).

    ω = ℓ · c_wave / r_eff,      r_eff = r_sat / (1 + ν_vac)

    Args:
        r_sat: Regime boundary radius (where saturation_factor = 0).
        nu_vac: Poisson ratio of the medium.
        ell: Angular mode number.
        c_wave: Wave speed in the medium.

    Returns:
        Angular eigenfrequency ω [rad/s].
    """
    r_eff = r_sat / (1.0 + nu_vac)
    return ell * c_wave / r_eff


def universal_quality_factor(ell: int) -> float:
    """
    Operator 21: Universal Phase Transition Quality Factor

    Universal quality factor from lattice phase transition at saturation: Q = ℓ.

    At the saturation boundary (S = 0), the shear modulus vanishes,
    making it a perfect reflector. The mode has ℓ wavelengths around
    the circumference, each releasing ~1/ℓ of energy per cycle.

    Args:
        ell: Angular mode number (integer >= 1).

    Returns:
        Quality factor Q (dimensionless).
    """
    return float(ell)


def universal_avalanche_factor(
    V_applied: float | np.ndarray,
    V_breakdown: float,
    n_topology: int,
) -> float | np.ndarray:
    """
    Operator 22: Universal Avalanche Factor (M)

    Miller avalanche multiplication: the topological INVERSE of saturation.

    M = 1 / (1 - (V / V_BR)^n)

    At V → 0: M = 1 (linear, no avalanche).
    At V → V_BR: M → ∞ (breakdown, divergence).

    Args:
        V_applied: Applied strain/voltage.
        V_breakdown: Breakdown yielding strain/voltage.
        n_topology: Topological crossing number (controls sharpness).

    Returns:
        Avalanche factor M (dimensionless).
    """
    import numpy as np

    is_jax = _is_jax_array(V_applied)

    if is_jax:
        import jax.numpy as jnp

        ratio = jnp.abs(V_applied / V_breakdown)
        ratio = jnp.clip(ratio, 0.0, 1.0 - EPS_NUMERICAL ** (1.0 / n_topology))
        return 1.0 / (1.0 - ratio**n_topology)
    else:
        ratio = np.asarray(V_applied, dtype=float) / V_breakdown
        ratio = np.abs(ratio)
        ratio = np.clip(ratio, 0.0, 1.0 - EPS_NUMERICAL ** (1.0 / n_topology))
        return 1.0 / (1.0 - ratio**n_topology)


def universal_wave_speed(
    A: float | np.ndarray,
    A_yield: float,
    c_base: float,
) -> float | np.ndarray:
    """
    Operator 16: Universal Wave Speed (c_shear)

    Effective local shear/GW wave speed under dielectric saturation.

    c_shear(A) = c_base * (1 - (A/A_yield)^2)^(1/4)
               = c_base * sqrt(S(A))

    Note: For EM phase velocity, the scaling depends on the symmetry
    of the saturation (symmetric vs asymmetric). See rupture_solver.py
    for detailed derivations. This operator computes the shear speed.

    Args:
        A: Local strain amplitude.
        A_yield: Saturation limit.
        c_base: Base wave speed.

    Returns:
        Local shear/GW wave speed.
    """
    import numpy as np

    is_jax = _is_jax_array(A)

    if is_jax:
        import jax.numpy as jnp

        ratio_sq = jnp.clip((A / A_yield) ** 2, 0.0, 1.0 - EPS_NUMERICAL)
        return c_base * (1.0 - ratio_sq) ** 0.25
    else:
        A_arr = np.asarray(A, dtype=float)
        ratio_sq = np.clip((A_arr / A_yield) ** 2, 0.0, 1.0 - EPS_NUMERICAL)
        return c_base * (1.0 - ratio_sq) ** 0.25


def universal_coupled_mode_frequency(
    omega_0: float,
    k: float,
    adjacency_eigenvalue: float | np.ndarray,
) -> float | np.ndarray:
    """
    Operator 18: Universal Coupled Mode Frequency

    Normal mode splitting for coupled LC resonators.

    \\omega_n = \\omega_0 / \\sqrt{1 + k \\cdot \\lambda_n}

    where \\lambda_n is the adjacency matrix eigenvalue.

    Args:
        omega_0: Base resonance frequency.
        k: Coupling constant between resonators.
        adjacency_eigenvalue: Eigenvalue of the coupling topology.

    Returns:
        Coupled mode frequency \\omega_n.
    """
    import numpy as np

    is_jax = _is_jax_array(adjacency_eigenvalue)

    if is_jax:
        import jax.numpy as jnp

        return omega_0 / jnp.sqrt(1.0 + k * adjacency_eigenvalue)
    else:
        return omega_0 / np.sqrt(1.0 + k * adjacency_eigenvalue)


def universal_refractive_index(epsilon_11: float | np.ndarray, nu_vac: float = 2.0 / 7.0) -> float | np.ndarray:
    """
    Operator 19: Universal Refractive Index (n)

    The medium's total strain response to a gravitational source.
    Answers "how slow is propagation?" where S answers "how stiff is the medium?"

    n = 1 + \\nu_{vac} \\times \\epsilon_{11}

    where \\nu_vac is the Poisson ratio (default 2/7 for the vacuum lattice)
    and \\epsilon_11 is the principal strain component.

    Args:
        epsilon_11: Principal strain component.
        nu_vac: Poisson ratio of the medium.

    Returns:
        Refractive index n >= 1.
    """
    return 1.0 + nu_vac * epsilon_11


def plasma_refractive_index(omega: float | np.ndarray, omega_p: float) -> float | np.ndarray:
    """
    Operator 19 (Adapter): Plasma Refractive Index (n_plasma)

    The refractive index for transverse waves in a cold, unmagnetized plasma.
    This describes dispersion rather than geometric strain, but maps to the
    same propagation kinematics (c_local = c/n).

    n = \\sqrt{1 - (\\omega_p / \\omega)^2}

    Args:
        omega: Angular frequency of the wave.
        omega_p: Plasma frequency.

    Returns:
        Refractive index n <= 1. (0 if omega <= omega_p)
    """
    import numpy as np

    is_jax = _is_jax_array(omega)

    if is_jax:
        import jax.numpy as jnp

        ratio_sq = (omega_p / jnp.maximum(omega, EPS_NUMERICAL)) ** 2
        return jnp.sqrt(jnp.maximum(0.0, 1.0 - ratio_sq))
    else:
        omega_arr = np.asarray(omega, dtype=float)
        ratio_sq = (omega_p / np.maximum(omega_arr, EPS_NUMERICAL)) ** 2
        return np.sqrt(np.maximum(0.0, 1.0 - ratio_sq))
