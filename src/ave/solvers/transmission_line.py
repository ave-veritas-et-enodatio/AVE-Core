from __future__ import annotations
r"""
Transmission Line Network Solver (Scale-Invariant)
====================================================

Domain-agnostic transmission line calculations used at EVERY AVE scale:
  - Protein backbone: ABCD cascade with Y-shunt at Cα junctions
  - PONDER-01 antenna: stub-loaded TL matching
  - Seismic PREM:     layered impedance profile
  - Stellar interiors: radial impedance cascade

The SAME three operators appear at all scales:
  1. ABCD matrix for a TL segment  → propagation
  2. ABCD matrix for a shunt Y     → junction coupling
  3. S₁₁ from total ABCD           → reflection (mismatch)

This module provides two backends:
  - NumPy  (analysis, plotting, debugging)
  - JAX    (gradient-based optimisation, JIT compilation)

Both backends compute the SAME physics.  The JAX version uses
lax.fori_loop for efficient gradient computation through long
cascades (e.g. 3N-1 segments for N-residue proteins).

Examples
--------
>>> from ave.solvers.transmission_line import (
...     abcd_segment, abcd_shunt, abcd_cascade,
...     s11_from_abcd, s11_frequency_sweep,
... )
>>> Z = [3.61, 3.46, 2.94]  # N-Cα, Cα-C, C-N impedances
>>> gamma = [0.1+1j, 0.1+1j, 0.1+1.3j]  # propagation constants
>>> Y = [0.05, 0.0]  # junction shunts
>>> s11 = s11_frequency_sweep(Z, gamma, Y, Z_source=1.0, Z_load=1.0)
"""

import numpy as np
from typing import Optional, Union, Sequence

# ====================================================================
# NumPy backend (analysis, plotting)
# ====================================================================

def abcd_segment(Z_c: complex, gamma_l: complex) -> np.ndarray:
    r"""
    ABCD matrix for a single transmission line segment.

    .. math::
        \begin{bmatrix} A & B \\ C & D \end{bmatrix} =
        \begin{bmatrix}
            \cosh(\gamma\ell)     & Z_c \sinh(\gamma\ell) \\
            \sinh(\gamma\ell)/Z_c & \cosh(\gamma\ell)
        \end{bmatrix}

    This is the SAME matrix at every scale.

    Args:
        Z_c: Characteristic impedance of the segment.
        gamma_l: Complex propagation constant × length (α + jβ)·ℓ.

    Returns:
        2×2 ABCD matrix (complex).
    """
    ch = np.cosh(gamma_l)
    sh = np.sinh(gamma_l)
    return np.array([
        [ch,        Z_c * sh],
        [sh / Z_c,  ch      ],
    ], dtype=complex)


def abcd_shunt(Y: complex) -> np.ndarray:
    r"""
    ABCD matrix for a shunt admittance at a junction.

    .. math::
        \begin{bmatrix} A & B \\ C & D \end{bmatrix} =
        \begin{bmatrix} 1 & 0 \\ Y & 1 \end{bmatrix}

    Args:
        Y: Shunt admittance (scalar, complex).

    Returns:
        2×2 ABCD matrix.
    """
    return np.array([
        [1.0 + 0j,  0.0 + 0j],
        [Y,         1.0 + 0j],
    ], dtype=complex)


def abcd_stub(Z_stub: complex, gamma_l_stub: complex,
              termination: str = 'open') -> np.ndarray:
    r"""
    ABCD matrix for a TL stub attached at a junction.

    A stub is a short TL segment that terminates in either an open
    or short circuit.  It creates frequency-dependent impedance
    at the junction — the mechanism for bandpass/bandstop filtering
    in RF engineering.

    Open stub:   Y_stub = j·tan(βℓ) / Z_stub  (resonant at λ/4)
    Short stub:  Y_stub = -j·cot(βℓ) / Z_stub (resonant at λ/2)

    In protein folding, H-bonds act as stubs: short TL segments
    connecting non-adjacent backbone positions through space.

    Args:
        Z_stub: Characteristic impedance of the stub line.
        gamma_l_stub: Propagation constant × stub length.
        termination: 'open' or 'short'.

    Returns:
        2×2 ABCD matrix (equivalent shunt admittance).
    """
    if termination == 'open':
        # Y_input = tanh(γℓ) / Z_stub
        Y = np.tanh(gamma_l_stub) / Z_stub
    elif termination == 'short':
        # Y_input = 1 / (Z_stub · tanh(γℓ))
        Y = 1.0 / (Z_stub * np.tanh(gamma_l_stub) + 1e-20)
    else:
        raise ValueError(f"Unknown termination: {termination}")
    return abcd_shunt(Y)


def abcd_cascade(matrices: Sequence[np.ndarray]) -> np.ndarray:
    """
    Cascade multiply a sequence of ABCD matrices.

    Args:
        matrices: List of 2×2 ABCD matrices.

    Returns:
        Total 2×2 ABCD matrix.
    """
    result = np.eye(2, dtype=complex)
    for M in matrices:
        result = result @ M
    return result


def s11_from_abcd(M: np.ndarray,
                  Z_source: float = 1.0,
                  Z_load: float = 1.0) -> complex:
    r"""
    Compute S₁₁ (reflection coefficient) from a total ABCD matrix.

    .. math::
        \Gamma = \frac{A + B/Z_L - C Z_S - D}
                      {A + B/Z_L + C Z_S + D}

    This is the SAME formula at every scale:
      - Particle: Γ at Pauli boundary
      - Protein:  S₁₁ at backbone cascade
      - Antenna:  VSWR at feed point
      - Galaxy:   impedance mismatch at core

    Args:
        M: 2×2 ABCD matrix.
        Z_source: Source impedance.
        Z_load: Load impedance.

    Returns:
        Complex reflection coefficient Γ.
    """
    A, B, C, D = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    numer = A + B / Z_load - C * Z_source - D
    denom = A + B / Z_load + C * Z_source + D + 1e-20
    return numer / denom


def s11_power(M: np.ndarray,
              Z_source: float = 1.0,
              Z_load: float = 1.0) -> float:
    """S₁₁ power reflection coefficient |Γ|²."""
    gamma = s11_from_abcd(M, Z_source, Z_load)
    return float(np.real(gamma * np.conj(gamma)))


def s21_from_abcd(M: np.ndarray,
                  Z_source: float = 1.0,
                  Z_load: float = 1.0) -> complex:
    r"""
    Compute S₂₁ (transmission coefficient) from ABCD matrix.

    .. math::
        S_{21} = \frac{2}{A + B/Z_L + C Z_S + D}

    Args:
        M: 2×2 ABCD matrix.
        Z_source: Source impedance.
        Z_load: Load impedance.

    Returns:
        Complex transmission coefficient.
    """
    A, B, C, D = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    denom = A + B / Z_load + C * Z_source + D + 1e-20
    return 2.0 / denom


def s11_frequency_sweep(
    seg_Z: Sequence[float],
    seg_gamma_l: Sequence[complex],
    junction_Y: Optional[Sequence[complex]] = None,
    stubs: Optional[dict] = None,
    freqs: Sequence[float] = (0.5, 0.8, 1.0, 1.3, 2.0),
    Z_source: float = 1.0,
    Z_load: float = 1.0,
) -> dict:
    r"""
    Frequency-swept S₁₁ for a loaded TL cascade.

    Builds the full ABCD cascade at each frequency:
      segment₀ → junction₀ → segment₁ → junction₁ → ...

    Args:
        seg_Z: Characteristic impedance per segment.
        seg_gamma_l: Propagation constant × length per segment (at ω=1).
            Scales with frequency: γℓ(ω) = γℓ(1) × ω.
        junction_Y: Shunt admittance at each junction (N_seg - 1).
        stubs: Dict mapping junction index to stub parameters:
            {idx: {'Z': float, 'gamma_l': complex, 'termination': str}}
        freqs: Frequency points to sweep.
        Z_source: Source impedance.
        Z_load: Load impedance.

    Returns:
        Dict with 's11_power', 's21_phase', 'freqs' arrays.
    """
    N = len(seg_Z)
    if junction_Y is None:
        junction_Y = [0.0] * (N - 1)
    if stubs is None:
        stubs = {}

    s11_powers = []
    s21_phases = []

    for freq in freqs:
        matrices = []
        for i in range(N):
            # Segment ABCD (frequency-scaled propagation)
            gl = seg_gamma_l[i] * freq
            matrices.append(abcd_segment(seg_Z[i], gl))

            # Junction shunt + stubs (between segments)
            if i < N - 1:
                Y_total = junction_Y[i]

                # Add stub admittance if present at this junction
                if i in stubs:
                    s = stubs[i]
                    stub_gl = s['gamma_l'] * freq
                    if s.get('termination', 'open') == 'open':
                        Y_stub = np.tanh(stub_gl) / s['Z']
                    else:
                        Y_stub = 1.0 / (s['Z'] * np.tanh(stub_gl) + 1e-20)
                    Y_total = Y_total + Y_stub

                if Y_total != 0:
                    matrices.append(abcd_shunt(Y_total))

        M_total = abcd_cascade(matrices)
        gamma = s11_from_abcd(M_total, Z_source, Z_load)
        s21 = s21_from_abcd(M_total, Z_source, Z_load)

        s11_powers.append(float(np.real(gamma * np.conj(gamma))))
        s21_phases.append(float(np.angle(s21)))

    return {
        's11_power': np.array(s11_powers),
        's21_phase': np.array(s21_phases),
        'freqs': np.array(list(freqs)),
    }


# ====================================================================
# JAX backend (gradient-based optimisation)
# ====================================================================

def _try_import_jax():
    """Import JAX if available, return (jax, jnp, lax) or None."""
    try:
        import jax
        import jax.numpy as jnp
        from jax import lax
        return jax, jnp, lax
    except ImportError:
        return None


def abcd_cascade_jax(seg_Zc, cosh_arr, sinh_arr, seg_Y, n_segs, n_junctions):
    """
    JAX-compatible ABCD cascade via lax.fori_loop.

    This is the CORE scale-invariant engine used by the protein fold
    solver.  It handles lossy TL segments with shunt admittances at
    junctions.

    Args:
        seg_Zc: (n_segs,) characteristic impedances per segment
        cosh_arr: (n_segs,) cosh(γℓ) per segment (precomputed)
        sinh_arr: (n_segs,) sinh(γℓ) per segment (precomputed)
        seg_Y: (n_junctions,) shunt admittance per junction
        n_segs: Number of TL segments
        n_junctions: Number of junctions

    Returns:
        (4,) array [A, B, C, D] — the total ABCD matrix elements
    """
    _jax_mod = _try_import_jax()
    if _jax_mod is None:
        raise ImportError("JAX not available for cascade_jax")
    jax, jnp, lax = _jax_mod

    init_state = jnp.array([1.0 + 0j, 0.0 + 0j, 0.0 + 0j, 1.0 + 0j])

    def cascade_step(i, state):
        A, B, C, D = state[0], state[1], state[2], state[3]
        ch = cosh_arr[i]
        sh = sinh_arr[i]
        Zc = seg_Zc[i] + 1e-12

        # TL segment: standard ABCD multiplication
        A_n = A * ch + B * (sh / Zc)
        B_n = A * (Zc * sh) + B * ch
        C_n = C * ch + D * (sh / Zc)
        D_n = C * (Zc * sh) + D * ch

        # Junction shunt admittance
        Y = jnp.where(i < n_junctions,
                      seg_Y[jnp.clip(i, 0, n_junctions - 1)], 0.0)
        C_n = C_n + Y * A_n
        D_n = D_n + Y * B_n

        return jnp.array([A_n, B_n, C_n, D_n])

    return lax.fori_loop(0, n_segs, cascade_step, init_state)


def s11_from_abcd_jax(abcd_state, Z_source, Z_load):
    """
    JAX-compatible S₁₁ extraction from ABCD state vector.

    Args:
        abcd_state: (4,) array [A, B, C, D]
        Z_source: Source impedance (scalar)
        Z_load: Load impedance (scalar)

    Returns:
        (s11_power, s21_phase) tuple
    """
    _jax_mod = _try_import_jax()
    if _jax_mod is None:
        raise ImportError("JAX not available")
    jax, jnp, lax = _jax_mod

    A, B, C, D = abcd_state[0], abcd_state[1], abcd_state[2], abcd_state[3]
    Z0 = Z_source

    numer = A + B / Z_load - C * Z0 - D
    denom = A + B / Z_load + C * Z0 + D + 1e-20
    gamma = numer / denom
    s11_power = jnp.real(gamma * jnp.conj(gamma))

    s21 = 2.0 / denom
    s21_phase = jnp.angle(s21)

    return s11_power, s21_phase


# ====================================================================
# Nodal Admittance Matrix (Multiport Network Analysis)
# ====================================================================
#
# Standard EE multiport analysis.  Instead of cascading ABCD matrices
# along a single path (1D), the nodal admittance matrix [Y] captures
# ALL connections between ALL nodes simultaneously:
#
#   I = [Y] × V
#
#   Y_ii = Σ_j y_ij    (self admittance = sum of all branches at node i)
#   Y_ij = -y_ij        (mutual admittance = negative of branch admittance)
#
# S-parameters are extracted via standard conversion:
#   [S] = ([Y]/Y₀ + [I])⁻¹ × ([Y]/Y₀ - [I])
#
# This is the SAME physics as ABCD but in matrix form.  Benefits:
#   - Cross-chain contacts (H-bonds, β-sheet) connect ports, not ground
#   - The N×N matrix retains full structural topology
#   - Standard linear algebra (no sequential fori_loop needed)
#
# Scale invariance: this code works for proteins (N~20-100 nodes),
# antenna networks (N~10 ports), or any multiport system.


def build_nodal_y_matrix(
    N: int,
    backbone_y: Sequence[complex],
    contacts: Optional[Sequence[tuple]] = None,
    self_y: Optional[Sequence[complex]] = None,
) -> np.ndarray:
    r"""
    Build an N×N nodal admittance matrix from backbone and contact terms.

    Args:
        N: Number of nodes (e.g., residues in a protein).
        backbone_y: (N-1,) branch admittance between sequential nodes i↔i+1.
            For a TL segment: y = 1/(Z_c × sinh(γℓ)) ≈ 1/(jωZ_c) for short ℓ.
        contacts: List of (i, j, y_ij) tuples for non-sequential connections.
            Each adds mutual admittance between nodes i and j.
        self_y: (N,) additional self-admittance at each node (e.g., solvent,
            bend loss).  Added to diagonal Y_ii.

    Returns:
        (N, N) complex nodal admittance matrix.
    """
    Y = np.zeros((N, N), dtype=complex)

    # Sequential backbone: tri-diagonal
    for i in range(N - 1):
        y = backbone_y[i]
        Y[i, i] += y
        Y[i + 1, i + 1] += y
        Y[i, i + 1] -= y
        Y[i + 1, i] -= y

    # Non-sequential contacts (H-bonds, β-sheet, hydrophobic)
    if contacts is not None:
        for (i, j, y_ij) in contacts:
            Y[i, i] += y_ij
            Y[j, j] += y_ij
            Y[i, j] -= y_ij
            Y[j, i] -= y_ij

    # Self admittance (solvent, bend, stubs)
    if self_y is not None:
        for i in range(N):
            Y[i, i] += self_y[i]

    return Y


def s11_from_y_matrix(
    Y: np.ndarray,
    port: int = 0,
    Y0: float = 1.0,
) -> complex:
    r"""
    Extract S₁₁ at a given port from a nodal admittance matrix.

    Standard conversion:
        [S] = ([Y]/Y₀ + [I])⁻¹ × ([Y]/Y₀ − [I])
        S₁₁ = S[port, port]

    Args:
        Y: (N, N) nodal admittance matrix.
        port: Port index for S₁₁ extraction (default: 0 = N-terminal).
        Y0: Reference admittance (normalisation).

    Returns:
        Complex S₁₁ at the specified port.
    """
    N = Y.shape[0]
    I = np.eye(N, dtype=complex)
    Y_norm = Y / Y0
    # S = (Y_norm + I)⁻¹ × (Y_norm − I)
    S = np.linalg.solve(Y_norm + I, Y_norm - I)
    return S[port, port]


def s_matrix_from_y(
    Y: np.ndarray,
    Y0: float = 1.0,
) -> np.ndarray:
    r"""
    Full S-parameter matrix from nodal admittance matrix.

    [S] = ([Y]/Y₀ + [I])⁻¹ × ([Y]/Y₀ − [I])

    Args:
        Y: (N, N) nodal admittance matrix.
        Y0: Reference admittance.

    Returns:
        (N, N) S-parameter matrix.
    """
    N = Y.shape[0]
    I = np.eye(N, dtype=complex)
    Y_norm = Y / Y0
    return np.linalg.solve(Y_norm + I, Y_norm - I)


# ── JAX versions ──

def build_nodal_y_matrix_jax(
    N,
    backbone_y,
    contact_i, contact_j, contact_y,
    self_y,
):
    r"""
    JAX-compatible nodal admittance matrix builder.

    Uses array indexing instead of Python loops for JIT compatibility.

    Args:
        N: Number of nodes (static int).
        backbone_y: (N-1,) complex backbone branch admittance.
        contact_i: (M,) int — source indices of contacts.
        contact_j: (M,) int — target indices of contacts.
        contact_y: (M,) complex — admittance of each contact.
        self_y: (N,) complex — self admittance per node.

    Returns:
        (N, N) complex nodal admittance matrix.
    """
    _jax_mod = _try_import_jax()
    if _jax_mod is None:
        raise ImportError("JAX not available")
    jax, jnp, lax = _jax_mod

    Y = jnp.zeros((N, N), dtype=jnp.complex64)

    # Sequential backbone: Y[i,i], Y[i+1,i+1] += y; Y[i,i+1], Y[i+1,i] -= y
    idx = jnp.arange(N - 1)
    Y = Y.at[idx, idx].add(backbone_y)
    Y = Y.at[idx + 1, idx + 1].add(backbone_y)
    Y = Y.at[idx, idx + 1].add(-backbone_y)
    Y = Y.at[idx + 1, idx].add(-backbone_y)

    # Non-sequential contacts
    Y = Y.at[contact_i, contact_i].add(contact_y)
    Y = Y.at[contact_j, contact_j].add(contact_y)
    Y = Y.at[contact_i, contact_j].add(-contact_y)
    Y = Y.at[contact_j, contact_i].add(-contact_y)

    # Self admittance (diagonal)
    diag_idx = jnp.arange(N)
    Y = Y.at[diag_idx, diag_idx].add(self_y)

    return Y


def s11_from_y_matrix_jax(Y, port=0, Y0=1.0):
    r"""
    JAX-compatible S₁₁ extraction from nodal admittance matrix.

    [S] = ([Y]/Y₀ + [I])⁻¹ × ([Y]/Y₀ − [I])

    Args:
        Y: (N, N) complex nodal admittance matrix.
        port: Port index (static int).
        Y0: Reference admittance.

    Returns:
        Complex S₁₁ at the specified port.
    """
    _jax_mod = _try_import_jax()
    if _jax_mod is None:
        raise ImportError("JAX not available")
    jax, jnp, lax = _jax_mod

    N = Y.shape[0]
    I = jnp.eye(N, dtype=jnp.complex128)
    Y_norm = Y / Y0
    S = jnp.linalg.solve(Y_norm + I, Y_norm - I)
    return S[port, port]


def abcd_to_y_backbone_jax(N, Z_eff, gamma_l):
    r"""
    Convert a sequential TL chain to Y-matrix backbone entries (JAX).

    Standard ABCD→Y conversion for a transmission line segment:
        y_mutual = -csch(γℓ)/Z   [off-diagonal: connects i ↔ i+1]
        y_self   =  coth(γℓ)/Z   [diagonal contribution per segment]

    Args:
        N: Number of nodes (static int).
        Z_eff: (N-1,) effective impedance per segment (real or complex).
        gamma_l: (N-1,) complex propagation constant × length per segment.

    Returns:
        (y_mutual, y_self_diag) tuple:
            y_mutual: (N-1,) complex — off-diagonal mutual admittance
            y_self_diag: (N,) complex — diagonal self-admittance from backbone
    """
    _jax_mod = _try_import_jax()
    if _jax_mod is None:
        raise ImportError("JAX not available")
    jax, jnp, lax = _jax_mod

    sinh_gl = jnp.sinh(gamma_l)
    cosh_gl = jnp.cosh(gamma_l)

    y_mutual = -1.0 / (Z_eff * sinh_gl + 1e-12)
    y_bb_self = cosh_gl / (Z_eff * sinh_gl + 1e-12)  # coth(γℓ)/Z

    # Distribute self-admittance to nodes: each segment contributes to
    # both of its endpoint nodes
    bb_idx = jnp.arange(N - 1)
    diag_bb = jnp.zeros(N, dtype=jnp.complex128)
    diag_bb = diag_bb.at[bb_idx].add(y_bb_self.astype(jnp.complex128))
    diag_bb = diag_bb.at[bb_idx + 1].add(y_bb_self.astype(jnp.complex128))

    return y_mutual.astype(jnp.complex128), diag_bb


def s_diagonal_from_y_matrix_jax(Y, Y0=1.0):
    r"""
    Full S-matrix diagonal from nodal admittance matrix (JAX).

    Computes |S_ii|² at ALL ports simultaneously.  For a well-matched
    multiport network, all diagonal elements should be small.

    When Y0 is a scalar: standard uniform reference.
    When Y0 is a (N,) array: per-port reference admittance (lattice coupling).
        Each port is referenced to its local environment impedance.
        Exposed ports (high Y0) → strong lattice coupling.
        Buried ports (low Y0) → weak lattice coupling.

    With diagonal Ŷ₀ = diag(Y0):
        [S] = Ŷ₀^(-½) (Y − Ŷ₀)(Y + Ŷ₀)⁻¹ Ŷ₀^(½)

    Args:
        Y: (N, N) complex nodal admittance matrix.
        Y0: Reference admittance — scalar or (N,) per-port array.

    Returns:
        dict with:
            'diag': (N,) array of |S_ii|² per port
            'mean': scalar mean |S_ii|² across all ports
            'max': scalar max |S_ii|² (worst-matched port)
    """
    _jax_mod = _try_import_jax()
    if _jax_mod is None:
        raise ImportError("JAX not available")
    jax, jnp, lax = _jax_mod

    N = Y.shape[0]

    # Build diagonal reference admittance matrix
    if jnp.ndim(Y0) == 0:
        # Scalar Y0 — use identity scaling (original behaviour)
        Y0_diag = Y0 * jnp.ones(N, dtype=jnp.complex128)
    else:
        # Per-port Y₀ vector
        Y0_diag = Y0.astype(jnp.complex128)

    # Ensure minimum reference admittance (avoid division by zero for buried ports)
    Y0_diag = jnp.maximum(jnp.abs(Y0_diag), 1e-4).astype(jnp.complex64)

    # Build matrices: Ŷ₀ = diag(Y0), √Ŷ₀, √Ŷ₀⁻¹
    Y0_mat = jnp.diag(Y0_diag)
    sqrt_Y0 = jnp.diag(jnp.sqrt(Y0_diag))
    sqrt_Y0_inv = jnp.diag(1.0 / jnp.sqrt(Y0_diag))

    # S = √Ŷ₀⁻¹ × (Y − Ŷ₀) × (Y + Ŷ₀)⁻¹ × √Ŷ₀
    Y_plus = Y + Y0_mat
    Y_minus = Y - Y0_mat
    # Solve (Y + Ŷ₀) × X = (Y − Ŷ₀) → X = (Y + Ŷ₀)⁻¹ × (Y − Ŷ₀)
    # Then S = √Ŷ₀⁻¹ × (Y − Ŷ₀) × (Y + Ŷ₀)⁻¹ × √Ŷ₀
    #        = √Ŷ₀⁻¹ × Y_minus × solve(Y_plus, √Ŷ₀)
    rhs = sqrt_Y0
    mid = jnp.linalg.solve(Y_plus, rhs)  # (Y+Ŷ₀)⁻¹ × √Ŷ₀
    S = sqrt_Y0_inv @ Y_minus @ mid

    s_diag = jnp.diagonal(S)
    s_diag_power = jnp.real(s_diag * jnp.conj(s_diag))

    # S†S eigenvalues: the modal reflection power.
    # S†S is Hermitian positive semi-definite → eigvalsh gives
    # sorted real eigenvalues = |λ_i(S)|².
    # Numerically stable and JAX-differentiable (vs eigvals for non-symmetric).
    SdagS = S.conj().T @ S
    s_eig_power = jnp.linalg.eigvalsh(SdagS)  # ascending order, real

    return {
        'diag': s_diag_power,
        'diag_complex': s_diag,            # complex Γᵢ = S_ii per port
        'mean': jnp.mean(s_diag_power),
        'max': jnp.max(s_diag_power),
        'eig': s_eig_power,
        'eig_min': s_eig_power[0],         # minimum |λ|² = root target
        'eig_mean': jnp.mean(s_eig_power),
        'S_matrix': S,
    }


def abcd_to_y_3seg_jax(N, Z_seg, d_seg, Z_node, omega, d0):
    r"""
    3-segment ABCD cascade → Y-matrix entries (JAX).

    Between consecutive nodes i and i+1, the backbone consists of
    3 transmission line segments with DIFFERENT impedances:

        node_i ──[Z₁,d₁]── junction ──[Z₂,d₂]── junction ──[Z₃,d₃]── node_{i+1}

    The sub-segment impedances are NORMALISED to unity mean so the ABCD
    cascade captures only the impedance grating (relative mismatches).
    The overall impedance scale comes from Z_node (per-residue Z_TOPO).

    Args:
        N: Number of nodes (static int).
        Z_seg: (3,) impedance per sub-segment [Z_CaC, Z_CN, Z_NCa].
        d_seg: (3,) bond length per sub-segment [d_CaC, d_CN, d_NCa].
        Z_node: (N,) per-node impedance (from Z_TOPO).
        omega: scalar angular frequency.
        d0: scalar reference Cα-Cα spacing.

    Returns:
        (y_mutual, y_self_diag) tuple:
            y_mutual: (N-1,) complex — off-diagonal mutual admittance
            y_self_diag: (N,) complex — diagonal self-admittance from backbone
    """
    _jax_mod = _try_import_jax()
    if _jax_mod is None:
        raise ImportError("JAX not available")
    jax, jnp, lax = _jax_mod

    # Normalise sub-segment impedances to unity mean
    # This isolates the impedance grating (3.46→2.94→3.61 becomes 1.04→0.88→1.08)
    Z_mean = jnp.mean(Z_seg)
    Z_norm = Z_seg / Z_mean  # (3,) ≈ [1.04, 0.88, 1.08]

    # Sub-segment propagation constants
    gamma_l = jnp.array([
        1e-4 + 1j * omega * d_seg[0] / d0,
        1e-4 + 1j * omega * d_seg[1] / d0,
        1e-4 + 1j * omega * d_seg[2] / d0,
    ])

    ch = jnp.cosh(gamma_l)
    sh = jnp.sinh(gamma_l)

    # Overall impedance scale from Z_TOPO (geometric mean of endpoints)
    z_scale = jnp.sqrt(jnp.abs(Z_node[:-1]) * jnp.abs(Z_node[1:]))  # (N-1,)

    # Cascade 3 ABCD matrices using NORMALISED impedances
    # (grating only, scale applied after)
    A1, B1, C1, D1 = ch[0], Z_norm[0] * sh[0], sh[0] / Z_norm[0], ch[0]
    A2, B2, C2, D2 = ch[1], Z_norm[1] * sh[1], sh[1] / Z_norm[1], ch[1]
    A3, B3, C3, D3 = ch[2], Z_norm[2] * sh[2], sh[2] / Z_norm[2], ch[2]

    # M12 = M1 × M2
    A12 = A1 * A2 + B1 * C2
    B12 = A1 * B2 + B1 * D2
    C12 = C1 * A2 + D1 * C2
    D12 = C1 * B2 + D1 * D2

    # M_total = M12 × M3
    A_t = A12 * A3 + B12 * C3
    B_t = A12 * B3 + B12 * D3
    C_t = C12 * A3 + D12 * C3
    D_t = C12 * B3 + D12 * D3

    # Apply physical impedance scale:
    # B_physical = B_t × z_scale (B has units of impedance)
    # C_physical = C_t / z_scale (C has units of admittance)
    # A and D are dimensionless — unchanged
    B_phys = B_t * z_scale + 1e-12

    # ABCD→Y conversion for the cascaded 2-port:
    # y₁₂ = -1/B_phys
    # y₁₁ = D_t/B_phys  (not y₂₂ — asymmetric cascade!)
    # y₂₂ = A_t/B_phys
    y_mutual = -1.0 / B_phys
    y_self_left = D_t / B_phys
    y_self_right = A_t / B_phys

    bb_idx = jnp.arange(N - 1)
    diag_bb = jnp.zeros(N, dtype=jnp.complex128)
    diag_bb = diag_bb.at[bb_idx].add(y_self_left.astype(jnp.complex128))
    diag_bb = diag_bb.at[bb_idx + 1].add(y_self_right.astype(jnp.complex128))

    return y_mutual.astype(jnp.complex128), diag_bb

