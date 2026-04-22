"""
AVE MODULE: SATURATION-CORRECTED NUCLEAR BINDING ENGINE (JAX)
==============================================================
Implements Axiom 4 dielectric/magnetic saturation in the nuclear 
mutual coupling model.

PHYSICS:
    The bare coupling K/r assumes the vacuum between nucleon pairs
    is linear (unsaturated). In a dense nucleus, the superimposed
    strain from all nearby nucleons pushes the local vacuum toward
    its yield/snap limit. This reduces the medium's ability to
    transmit mutual inductance between deeply buried pairs.

    In Maxwell's equations with a nonlinear medium:
        ∇·(ε_eff(|E|)·E) = ρ
    
    Superposition fails. The effective coupling between pair (i,j)
    depends on the background strain from all OTHER nucleons along
    the coupling path.

    We implement this as:
        K_eff(i,j) = K × f_sat(V_bg(i,j))

    Where:
        V_bg(i,j) = Σ_{k≠i,j} K / |r_midpoint(i,j) - r_k|
        f_sat(V)  = √(max(0, 1 - (V/V_ref)²))    [Axiom 4 form]
        V_ref     = saturation reference scale (to be determined)

GPU READY: All pairwise computations use JAX vectorization.
"""

import numpy as np

# Try JAX, fall back to numpy if unavailable
try:
    import jax
    import jax.numpy as jnp

    HAS_JAX = True
    print(f"[JAX] Backend: {jax.devices()[0].platform}")
except ImportError:
    import numpy as jnp

    HAS_JAX = False
    print("[JAX] Not available, using NumPy fallback")

# ---- Import AVE constants ----
from ave.core.constants import K_MUTUAL, ALPHA

# Import nucleon coordinates from existing engine
from simulate_element import get_nucleon_coordinates, M_P_RAW, M_N_RAW

# ---- Physical constants in nuclear units ----
# K_MUTUAL is in MeV·fm
# Distances are in units of d (0.85 fm)
# We need V_ref in MeV (energy at a point from K/r contributions)

# Convert V_SNAP to nuclear energy units (MeV)
V_SNAP_MEV = 0.51099895  # m_e c² in MeV — the absolute snap voltage in energy

# V_YIELD in nuclear energy units
V_YIELD_MEV = np.sqrt(ALPHA) * V_SNAP_MEV  # ≈ 0.04365 MeV


def compute_binding_energy_bare(nodes_np):
    """
    BARE model: simple sum of K/r for all pairs (no saturation).
    This is the existing Z=1-14 model.
    """
    nodes = jnp.array(nodes_np)
    n = len(nodes)

    # Compute all pairwise distances
    diff = nodes[:, None, :] - nodes[None, :, :]  # (N, N, 3)
    dist = jnp.sqrt(jnp.sum(diff**2, axis=-1))  # (N, N)

    # Mask diagonal (self-interaction)
    mask = jnp.triu(jnp.ones((n, n), dtype=bool), k=1)

    # Sum K/r for upper triangle
    be = jnp.sum(jnp.where(mask, K_MUTUAL / jnp.maximum(dist, 1e-10), 0.0))

    return float(be)


def compute_binding_energy_saturated(nodes_np, V_ref):
    """
    SATURATED model: each pair's coupling is reduced by the background
    strain from all other nucleons at the pair's midpoint.

    K_eff(i,j) = K × √(max(0, 1 - (V_bg/V_ref)²))

    Where V_bg = Σ_{k≠i,j} K / |r_midpoint(i,j) - r_k|

    Args:
        nodes_np: (N, 3) array of nucleon positions
        V_ref: saturation reference scale in MeV

    Returns:
        binding_energy: total binding energy in MeV
        pair_data: dict with diagnostic info
    """
    nodes = jnp.array(nodes_np)
    n = len(nodes)

    # Compute all pairwise distances
    diff = nodes[:, None, :] - nodes[None, :, :]
    dist = jnp.sqrt(jnp.sum(diff**2, axis=-1))

    # Compute midpoints for all pairs: midpoint(i,j) = (r_i + r_j) / 2
    midpoints = (nodes[:, None, :] + nodes[None, :, :]) / 2.0  # (N, N, 3)

    # For each pair (i,j), compute the background strain at the midpoint
    # from all OTHER nucleons k (k ≠ i, k ≠ j)
    # V_bg(i,j) = Σ_{k≠i,j} K / |midpoint(i,j) - r_k|

    # Distance from each midpoint to each nucleon: (N, N, N)
    # midpoints[i,j] to nodes[k]
    mid_to_node = midpoints[:, :, None, :] - nodes[None, None, :, :]  # (N, N, N, 3)
    mid_to_node_dist = jnp.sqrt(jnp.sum(mid_to_node**2, axis=-1))  # (N, N, N)

    # Mask: exclude k=i and k=j for each pair
    # For pair (i,j), exclude nucleons i and j from the background sum
    idx = jnp.arange(n)
    mask_i = idx[None, None, :] != idx[:, None, None]  # k ≠ i
    mask_j = idx[None, None, :] != idx[None, :, None]  # k ≠ j
    mask_bg = mask_i & mask_j

    # Background strain at each midpoint
    strain_contributions = jnp.where(mask_bg, K_MUTUAL / jnp.maximum(mid_to_node_dist, 1e-10), 0.0)
    V_bg = jnp.sum(strain_contributions, axis=-1)  # (N, N)

    # Saturation factor: f_sat = √(max(0, 1 - (V_bg/V_ref)²))
    v_normalized = V_bg / V_ref
    f_sat = jnp.sqrt(jnp.maximum(0.0, 1.0 - v_normalized**2))

    # Corrected binding energy: K_eff = K × f_sat / r
    mask_upper = jnp.triu(jnp.ones((n, n), dtype=bool), k=1)

    be_per_pair = jnp.where(mask_upper, K_MUTUAL * f_sat / jnp.maximum(dist, 1e-10), 0.0)

    be_total = float(jnp.sum(be_per_pair))

    # Diagnostics
    v_bg_upper = jnp.where(mask_upper, V_bg, 0.0)
    f_sat_upper = jnp.where(mask_upper, f_sat, 1.0)

    pair_data = {
        "V_bg_mean": float(jnp.sum(v_bg_upper) / jnp.sum(mask_upper)),
        "V_bg_max": float(jnp.max(v_bg_upper)),
        "f_sat_mean": float(jnp.sum(f_sat_upper * mask_upper) / jnp.sum(mask_upper)),
        "f_sat_min": float(jnp.min(jnp.where(mask_upper, f_sat, 1.0))),
        "n_saturated": int(jnp.sum((f_sat_upper < 0.01) & mask_upper)),
        "n_pairs": int(jnp.sum(mask_upper)),
    }

    return be_total, pair_data


def compute_nuclear_mass(Z, A, V_ref=None):
    """
    Compute nuclear mass with optional saturation correction.

    Args:
        Z: proton number
        A: mass number
        V_ref: saturation reference scale (MeV). If None, uses bare model.

    Returns:
        mass, binding_energy, pair_data (or None)
    """
    N = A - Z
    raw_mass = Z * M_P_RAW + N * M_N_RAW

    nodes = get_nucleon_coordinates(Z, A)
    if not nodes or len(nodes) <= 1:
        return raw_mass, 0.0, None

    nodes_np = np.array(nodes)

    if V_ref is None:
        be = compute_binding_energy_bare(nodes_np)
        return raw_mass - be, be, None
    else:
        be, pair_data = compute_binding_energy_saturated(nodes_np, V_ref)
        return raw_mass - be, be, pair_data


# ---- CODATA empirical masses ----
CODATA_MASSES = {
    (1, 1): 938.272,  # H-1
    (2, 4): 3727.379,  # He-4
    (3, 7): 6533.832,  # Li-7
    (4, 9): 8394.795,  # Be-9
    (5, 11): 10252.548,  # B-11
    (6, 12): 11174.863,  # C-12
    (7, 14): 13040.204,  # N-14
    (8, 16): 14895.080,  # O-16
    (9, 19): 17692.302,  # F-19
    (10, 20): 18617.730,  # Ne-20
    (11, 23): 21409.214,  # Na-23
    (12, 24): 22335.793,  # Mg-24
    (13, 27): 25126.501,  # Al-27
    (14, 28): 26053.188,  # Si-28
    (15, 31): 28844.212,  # P-31
    (16, 32): 29855.525,  # S-32
}

ELEMENT_NAMES = {
    (1, 1): "H-1",
    (2, 4): "He-4",
    (3, 7): "Li-7",
    (4, 9): "Be-9",
    (5, 11): "B-11",
    (6, 12): "C-12",
    (7, 14): "N-14",
    (8, 16): "O-16",
    (9, 19): "F-19",
    (10, 20): "Ne-20",
    (11, 23): "Na-23",
    (12, 24): "Mg-24",
    (13, 27): "Al-27",
    (14, 28): "Si-28",
    (15, 31): "P-31",
    (16, 32): "S-32",
}


if __name__ == "__main__":
    print("=" * 90)
    print("AVE SATURATION-CORRECTED NUCLEAR BINDING ENGINE")
    print("=" * 90)
    print()

    # ---- Step 1: Baseline (bare model) ----
    print("--- BARE MODEL (no saturation) ---")
    print(f"{'Element':8s} {'Z':>3s} {'A':>3s} {'CODATA':>12s} {'AVE':>12s} {'Error':>10s} {'BE':>10s} {'Pairs':>6s}")
    print("-" * 70)

    for (Z, A), emp in sorted(CODATA_MASSES.items()):
        name = ELEMENT_NAMES.get((Z, A), f"Z={Z}")
        m, be, _ = compute_nuclear_mass(Z, A, V_ref=None)
        err = (m - emp) / emp * 100
        nodes = get_nucleon_coordinates(Z, A)
        n_pairs = len(nodes) * (len(nodes) - 1) // 2
        print(f"{name:8s} {Z:3d} {A:3d} {emp:12.3f} {m:12.3f} {err:+9.4f}% {be:10.3f} {n_pairs:6d}")

    # ---- Step 2: Sweep V_ref to find optimal saturation scale ----
    print()
    print("--- SATURATION SWEEP ---")
    print("Testing saturation reference scales to find a value that:")
    print("  1. Preserves 0.00% error for Z=1-14")
    print("  2. Fixes the S-32 over-binding")
    print()

    # Test range of V_ref values
    test_vref = [0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 200.0, 500.0, 1000.0]

    print(f"{'V_ref':>8s}", end="")
    for Z, A in [(2, 4), (6, 12), (14, 28), (15, 31), (16, 32)]:
        name = ELEMENT_NAMES.get((Z, A), f"Z={Z}")
        print(f" {name:>10s}", end="")
    print()
    print("-" * 68)

    for vref in test_vref:
        print(f"{vref:8.1f}", end="")
        for Z, A in [(2, 4), (6, 12), (14, 28), (15, 31), (16, 32)]:
            emp = CODATA_MASSES[(Z, A)]
            m, be, pd = compute_nuclear_mass(Z, A, V_ref=vref)
            err = (m - emp) / emp * 100
            print(f" {err:+9.4f}%", end="")
        print()

    # ---- Step 3: Detailed diagnostics at best V_ref ----
    print()
    print("--- DIAGNOSTICS ---")
    # Find V_ref that minimizes S-32 error
    best_vref = None
    best_s32_err = 999
    for vref in np.arange(1.0, 500.0, 0.5):
        m, _, _ = compute_nuclear_mass(16, 32, V_ref=vref)
        err = abs((m - CODATA_MASSES[(16, 32)]) / CODATA_MASSES[(16, 32)] * 100)
        if err < best_s32_err:
            best_s32_err = err
            best_vref = vref

    print(f"Best V_ref for S-32: {best_vref:.1f} MeV (S-32 error: {best_s32_err:.4f}%)")
    print()

    if best_vref:
        print(f"--- FULL RESULTS at V_ref = {best_vref:.1f} MeV ---")
        print(f"{'Element':8s} {'CODATA':>12s} {'Bare':>10s} {'Saturated':>10s} {'f_sat_mean':>10s} {'V_bg_mean':>10s}")
        print("-" * 70)

        for (Z, A), emp in sorted(CODATA_MASSES.items()):
            name = ELEMENT_NAMES.get((Z, A), f"Z={Z}")
            m_bare, _, _ = compute_nuclear_mass(Z, A, V_ref=None)
            m_sat, be_sat, pd = compute_nuclear_mass(Z, A, V_ref=best_vref)
            err_bare = (m_bare - emp) / emp * 100
            err_sat = (m_sat - emp) / emp * 100

            f_mean = pd["f_sat_mean"] if pd else 1.0
            v_mean = pd["V_bg_mean"] if pd else 0.0

            print(f"{name:8s} {emp:12.3f} {err_bare:+9.4f}% {err_sat:+9.4f}% {f_mean:10.4f} {v_mean:10.3f}")
