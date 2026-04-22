"""
AVE MODULE: ALPHA-CLUSTER ABCD CASCADE ENGINE
==============================================
Nuclear binding as S₁₁ minimization of a coupled resonator network.
ALL physics derived from the 4 AVE axioms — zero empirical fits.

AXIOM MAP:
    Axiom 1 → Each α-cluster is a 4-port LC resonant tank
              Vacuum between clusters is a transmission line
    Axiom 2 → Coupling scale K = (5π/2)αℏc/(1-α/3)
              Coulomb repulsion αℏc/r between proton pairs
    Axiom 3 → Not used (gravity irrelevant at nuclear scale)
    Axiom 4 → Junction capacitance C_j = 1/√(1-(d/r)²)
              (scale-invariant, same form as protein folding engine)

THREE OPERATING REGIMES:
    Saturated  (V ≥ V_SNAP):  nucleon interior — the defect itself
    Nonlinear (V_YIELD ≤ V < V_SNAP): intra-alpha coupling
    Linear    (V << V_YIELD): inter-alpha coupling (superposition valid)

GEOMETRY EMERGENCE:
    The nuclear geometry is NOT prescribed — it EMERGES from minimizing
    the total reflected power S₁₁ of the coupled resonator network.
    This is the nuclear analog of the protein folding S₁₁ engine.
"""

import time

import jax.numpy as jnp
import numpy as np
from jax import grad, jit, lax

# Import AVE constants
from ave.core.constants import (
    ALPHA,
    C_0,
    D_INTRA_ALPHA,
    D_PROTON,
    HBAR,
    K_MUTUAL,
    M_N_MEV_TARGET,
    M_P_MEV_TARGET,
    e_charge,
)

# ---- AXIOM-DERIVED CONSTANTS ----

# Proton charge radius — imported from physics engine
D_NUCLEON = D_PROTON  # ≈ 0.841 fm

# Intra-alpha distance: nucleons sit at vertices of regular tetrahedron
# Intra-alpha distance — from physics engine
D_INTRA_ALPHA_LOCAL = D_INTRA_ALPHA

# Coulomb constant: αℏc ≈ 1.44 MeV·fm (Axiom 2)
ALPHA_HC = ALPHA * (HBAR * C_0 / e_charge) * 1e9  # MeV·fm

# Proton / Neutron masses
# Proton / Neutron masses — from physics engine
M_P = M_P_MEV_TARGET  # MeV
M_N = M_N_MEV_TARGET  # MeV

# Alpha cluster mass (4 nucleons − intra-alpha binding)
# BE(He-4) = 6 pairs × K/d_intra = 6 × K / (d√8)
BE_ALPHA = 6.0 * K_MUTUAL / D_INTRA_ALPHA  # ≈ 28.3 MeV
M_ALPHA_RAW = 2 * M_P + 2 * M_N  # ≈ 3755.67 MeV
M_ALPHA = M_ALPHA_RAW - BE_ALPHA  # ≈ 3727.38 MeV (matches He-4)

# Intra-alpha Coulomb (1 p-p pair out of 6, pp_frac = 1/6)
COULOMB_INTRA_ALPHA = ALPHA_HC / (6.0 * D_INTRA_ALPHA)

# Alpha cluster effective impedance (Axiom 1)
# Z_α is the self-impedance of the 4-port resonant tetrahedron
# Derived from the stored reactive energy per unit current:
#   Z_α = BE / I² where I is the topological circulation
# In normalized units where I = 1:
Z_ALPHA = float(BE_ALPHA)  # ≈ 28.3 (dimensionless in natural units)

print(f"=== Alpha Cluster Properties (Derived from Axioms) ===")
print(f"d_nucleon      = {D_NUCLEON} fm")
print(f"d_intra_alpha  = {D_INTRA_ALPHA:.4f} fm")
print(f"K_MUTUAL       = {K_MUTUAL:.6f} MeV·fm")
print(f"αℏc            = {ALPHA_HC:.6f} MeV·fm")
print(f"BE(α)          = {BE_ALPHA:.3f} MeV")
print(f"M(α) raw       = {M_ALPHA_RAW:.3f} MeV")
print(f"M(α) bound     = {M_ALPHA:.3f} MeV")
print(f"Z_α            = {Z_ALPHA:.3f}")
print(f"CODATA He-4    = 3727.379 MeV")
print(f"Error          = {abs(M_ALPHA - 3727.379)/3727.379*100:.4f}%")
print()

# ============================================================
# ABCD Matrix Functions
# ============================================================


def abcd_vacuum_segment(distance, freq=1.0):
    """
    ABCD matrix for a vacuum transmission line segment of given length.

    From Axiom 1: vacuum is an LC network with Z₀ = 377 Ω.
    The phase delay is β·ℓ = 2πf·d/c.

    In nuclear natural units (normalized to Z₀ = 1):
        A = cos(βℓ),  B = jZ₀sin(βℓ)
        C = jsin(βℓ)/Z₀,  D = cos(βℓ)
    """
    # Phase per unit length in nuclear units
    beta_l = 2.0 * jnp.pi * freq * distance / D_INTRA_ALPHA

    cos_bl = jnp.cos(beta_l)
    sin_bl = jnp.sin(beta_l)

    # ABCD matrix [A, B; C, D] stored as (A, B, C, D)
    A = cos_bl + 0j
    B = 1j * sin_bl  # Z₀ = 1 (normalized)
    C = 1j * sin_bl  # 1/Z₀ = 1
    D = cos_bl + 0j

    return jnp.array([A, B, C, D])


def abcd_shunt_admittance(Y):
    """
    ABCD matrix for a shunt admittance element.

    [1, 0; Y, 1]

    This represents the inter-cluster coupling:
    Y = K/(Z_α × r) × C_sat(d/r) − αℏc_pp/(Z_α × r)
    """
    return jnp.array([1.0 + 0j, 0.0 + 0j, Y + 0j, 1.0 + 0j])


def cascade_abcd(M1, M2):
    """Multiply two ABCD matrices: M_total = M1 × M2."""
    A1, B1, C1, D1 = M1[0], M1[1], M1[2], M1[3]
    A2, B2, C2, D2 = M2[0], M2[1], M2[2], M2[3]

    A = A1 * A2 + B1 * C2
    B = A1 * B2 + B1 * D2
    C = C1 * A2 + D1 * C2
    D = C1 * B2 + D1 * D2

    return jnp.array([A, B, C, D])


def s11_from_abcd(M, Z_source=1.0, Z_load=1.0):
    """
    Compute S₁₁ (reflection coefficient magnitude²) from ABCD matrix.

    Γ = (A + B/Z_L − C·Z_S − D) / (A + B/Z_L + C·Z_S + D)
    |S₁₁|² = |Γ|²
    """
    A, B, C, D = M[0], M[1], M[2], M[3]

    numer = A + B / Z_load - C * Z_source - D
    denom = A + B / Z_load + C * Z_source + D + 1e-20
    gamma = numer / denom

    return jnp.real(gamma * jnp.conj(gamma))


# ============================================================
# Nuclear S₁₁ Loss Function
# ============================================================


def nuclear_s11_loss(positions_flat, n_alphas, Z_total, A_total):
    """
    Compute the total S₁₁ loss for an N-alpha-cluster nucleus.
    ALL JAX-compatible — no Python conditionals on traced values.
    """
    positions = positions_flat.reshape(n_alphas, 3)

    # Pairwise distances between alpha cluster centers
    diff = positions[:, None, :] - positions[None, :, :]  # (N, N, 3)
    dists = jnp.sqrt(jnp.sum(diff**2, axis=-1) + 1e-12)  # (N, N)

    # ---- Inter-alpha coupling ----
    # Scale-invariant junction capacitance (Axiom 4)
    sat_ratio = jnp.clip(D_INTRA_ALPHA / (dists + 1e-10), 0.0, 0.95)
    C_sat = 1.0 / jnp.sqrt(1.0 - sat_ratio**2)

    # Strong coupling: K × C_sat / r (attractive)
    strong_coupling = K_MUTUAL * C_sat / (dists + 1e-10)

    # Coulomb repulsion (Axiom 2): f_pp = 2×2/(4×4) = 0.25 for inter-alpha
    coulomb = ALPHA_HC * 0.25 / (dists + 1e-10)

    # Net coupling (symmetric matrix — no need for if/else)
    net_coupling = strong_coupling - coulomb

    # Upper triangle mask
    idx = jnp.arange(n_alphas)
    mask = idx[:, None] < idx[None, :]

    # Total inter-alpha binding energy
    be_inter = jnp.sum(jnp.where(mask, net_coupling, 0.0))

    # ---- ABCD Cascade for S₁₁ ----
    # Nearest-neighbor ring cascade using angular ordering
    com = jnp.mean(positions, axis=0)
    relative = positions - com
    angles = jnp.arctan2(relative[:, 1], relative[:, 0])
    order = jnp.argsort(angles)

    # Precompute ordered distances and couplings for lax loop
    ordered_dists = jnp.array([dists[order[k], order[(k + 1) % n_alphas]] for k in range(n_alphas - 1)])
    ordered_coupling = jnp.array([net_coupling[order[k], order[(k + 1) % n_alphas]] for k in range(n_alphas - 1)])

    # Multi-frequency S₁₁
    freqs = jnp.array([0.5, 0.8, 1.0, 1.3, 2.0])

    s11_total = 0.0
    for f in freqs:
        # Cascade via lax.fori_loop
        M_init = jnp.array([1.0 + 0j, 0.0 + 0j, 0.0 + 0j, 1.0 + 0j])

        def cascade_step(k, M):
            d_ij = ordered_dists[k]
            Y_shunt = ordered_coupling[k] / Z_ALPHA

            # Vacuum TL segment
            beta_l = 2.0 * jnp.pi * f * d_ij / D_INTRA_ALPHA
            cos_bl = jnp.cos(beta_l)
            sin_bl = jnp.sin(beta_l)
            M_tl = jnp.array([cos_bl + 0j, 1j * sin_bl, 1j * sin_bl, cos_bl + 0j])

            M = cascade_abcd(M, M_tl)

            # Shunt admittance
            M_sh = jnp.array([1.0 + 0j, 0.0 + 0j, Y_shunt + 0j, 1.0 + 0j])
            M = cascade_abcd(M, M_sh)

            return M

        M_final = lax.fori_loop(0, n_alphas - 1, cascade_step, M_init)
        s11_total += s11_from_abcd(M_final, Z_source=Z_ALPHA, Z_load=Z_ALPHA)

    s11_avg = s11_total / len(freqs)

    # ---- Total Mass ----
    remainder_nucleons = A_total - n_alphas * 4
    remainder_protons = Z_total - n_alphas * 2
    remainder_neutrons = remainder_nucleons - remainder_protons

    total_mass = (
        n_alphas * M_ALPHA
        + jnp.maximum(0, remainder_protons) * M_P
        + jnp.maximum(0, remainder_neutrons) * M_N
        - be_inter
    )

    # ---- Loss Function ----
    # Minimum distance penalty (prevent overlap)
    min_dist = jnp.min(jnp.where(mask, dists, 1e6))
    overlap_penalty = jnp.maximum(0.0, 2.0 * D_INTRA_ALPHA - min_dist) ** 2

    loss = s11_avg + 0.1 * overlap_penalty

    return loss, total_mass, be_inter


def predict_nuclear_geometry(n_alphas, Z, A, n_steps=3000, lr=0.01):
    """
    Predict nuclear geometry by minimizing S₁₁.
    Returns optimized alpha cluster positions and nuclear mass.
    """
    print(f"--- Predicting geometry: {n_alphas} α-clusters, Z={Z}, A={A} ---")

    # Initialize: random positions on a sphere
    np.random.seed(42)
    R_init = D_INTRA_ALPHA * n_alphas * 0.5  # Initial radius guess

    # Fibonacci sphere initialization
    golden = (1 + 5**0.5) / 2
    positions = np.zeros((n_alphas, 3))
    for i in range(n_alphas):
        theta = 2 * np.pi * i / golden
        phi = np.arccos(1 - 2 * (i + 0.5) / n_alphas)
        positions[i] = R_init * np.array([np.cos(theta) * np.sin(phi), np.sin(theta) * np.sin(phi), np.cos(phi)])

    positions_flat = jnp.array(positions.flatten())

    # JIT compile the loss function
    def loss_fn(pos):
        l, m, be = nuclear_s11_loss(pos, n_alphas, Z, A)
        return l

    loss_grad = jit(grad(loss_fn))
    loss_jit = jit(loss_fn)

    # Gradient descent with momentum
    velocity = jnp.zeros_like(positions_flat)
    momentum = 0.9

    t0 = time.time()
    for step in range(n_steps):
        g = loss_grad(positions_flat)
        g_norm = jnp.sqrt(jnp.sum(g**2) + 1e-12)
        g = jnp.where(g_norm > 10.0, g * 10.0 / g_norm, g)

        velocity = momentum * velocity - lr * g
        positions_flat = positions_flat + velocity

        # Re-center
        pos_3d = positions_flat.reshape(n_alphas, 3)
        pos_3d = pos_3d - jnp.mean(pos_3d, axis=0)
        positions_flat = pos_3d.flatten()

        if step % 500 == 0 or step == n_steps - 1:
            loss_val = float(loss_jit(positions_flat))
            _, mass_val, be_val = nuclear_s11_loss(positions_flat, n_alphas, Z, A)
            print(f"  step {step:5d}: loss={loss_val:.6f}  mass={float(mass_val):.3f}  BE_inter={float(be_val):.3f}")

    dt = time.time() - t0
    print(f"  Optimization: {dt:.1f}s")

    # Final results
    final_pos = np.array(positions_flat.reshape(n_alphas, 3))
    _, final_mass, final_be = nuclear_s11_loss(positions_flat, n_alphas, Z, A)

    return final_pos, float(final_mass), float(final_be)


# ============================================================
# MAIN: Test on known elements
# ============================================================
if __name__ == "__main__":
    print("=" * 80)
    print("AVE ALPHA-CLUSTER ABCD CASCADE ENGINE")
    print("Nuclear geometry from S₁₁ minimization — zero empirical fits")
    print("=" * 80)
    print()

    # CODATA targets
    targets = {
        "C-12": (3, 6, 12, 11174.863),
        "O-16": (4, 8, 16, 14895.080),
        "Ne-20": (5, 10, 20, 18617.730),
        "S-32": (8, 16, 32, 29855.525),
    }

    print(f"{'Element':8s} {'n_α':>4s} {'CODATA':>12s} {'Predicted':>12s} {'Error':>10s} {'BE_inter':>10s}")
    print("-" * 65)

    for name, (n_alpha, Z, A, emp) in targets.items():
        pos, mass, be = predict_nuclear_geometry(n_alpha, Z, A, n_steps=2000, lr=0.005)
        err = (mass - emp) / emp * 100
        print(f"{name:8s} {n_alpha:4d} {emp:12.3f} {mass:12.3f} {err:+9.4f}% {be:10.3f}")
        print()
