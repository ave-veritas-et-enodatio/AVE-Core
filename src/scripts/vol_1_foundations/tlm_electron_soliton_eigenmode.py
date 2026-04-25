"""
TLM-based electron soliton eigenmode demonstration — L3 Phase-3.

Per the 2026-04-20 session reframing captured in
.agents/handoffs/L3_PHASE3_SESSION_20260420.md §10: the electron soliton is
a localized standing-wave eigenmode of the K4-TLM substrate, NOT an energy
minimum. Numerically demonstrate this by:

1. Initialize V_inc on the K4-TLM lattice with a (2,3)-phase-winding voltage
   pattern on a toroidal shell.
2. Run K4Lattice3D.step() evolution (no driving, closed system).
3. Observe temporal behavior:
   - Does the pattern disperse? Then it's not a stable soliton.
   - Does it settle into a repeating standing wave? Then the (2,3) sector
     has a bound state at that geometry.
4. Extract the standing-wave envelope's (R, r) — compare to Golden Torus.

This script is a first-pass scaffolding. Success criteria (optimistic): the
|V_inc| envelope on the shell stays localized and non-dispersive over many
Compton periods, indicating a bound mode.

Diagnostic readouts: total lattice energy vs time (conservation check),
shell-averaged |V| vs time (localization check), and envelope geometry.
"""
import numpy as np
from ave.core.k4_tlm import K4Lattice3D
from ave.core.constants import ALPHA, V_YIELD, V_SNAP


PHI = (1.0 + np.sqrt(5.0)) / 2.0


def initialize_2_3_voltage_ansatz(
    lattice: K4Lattice3D,
    R: float,
    r: float,
    amplitude: float = 0.5,
) -> None:
    """Populate V_inc with a (2,3) chiral-phasor voltage pattern on a
    toroidal shell.

    Chiral-phasor attributes (all three must be encoded):
      1. Magnitude — power-law hedgehog envelope (AVE-canonical, NOT Gaussian)
      2. Phase — quadrature: cos(theta) on ports 0,1; sin(theta) on ports 2,3
         gives phase-90° relationship closer to standing-wave eigenmode
      3. Chirality — port weighting by projection of tetrahedral vector onto
         the (2,3) knot tangent direction at each site; encodes the handedness
         of wave flow along the winding

    Port directions (A-sublattice -> B-sublattice tetrahedral vectors):
      p_0 = (+1,+1,+1), p_1 = (+1,-1,-1), p_2 = (-1,+1,-1), p_3 = (-1,-1,+1)

    The (2,3) torus-knot tangent at (phi, psi) on the shell:
      t = 2 * d(X)/d(phi) + 3 * d(X)/d(psi),
      where X(phi, psi) = ((R + r cos psi) cos phi, ..., r sin psi).
      Closed form (un-normalized):
        d/dphi = (-(R+r cos psi) sin phi, (R+r cos psi) cos phi, 0)
        d/dpsi = (-r sin psi cos phi, -r sin psi sin phi, r cos psi)
    """
    cx = (lattice.nx - 1) / 2.0
    cy = (lattice.ny - 1) / 2.0
    cz = (lattice.nz - 1) / 2.0

    idx = np.indices((lattice.nx, lattice.ny, lattice.nz))
    i, j, k = idx[0], idx[1], idx[2]
    x = i - cx
    y = j - cy
    z = k - cz

    rho_xy = np.sqrt(x**2 + y**2 + 1e-12)
    rho_tube = np.sqrt((rho_xy - R) ** 2 + z**2 + 1e-12)
    phi = np.arctan2(y, x)
    psi = np.arctan2(z, rho_xy - R)

    # Attribute 1: magnitude — power-law hedgehog envelope
    r_opt = max(r, 1.0)
    envelope = amplitude * np.pi / (1.0 + (rho_tube / r_opt) ** 2)

    # (2,3) knot tangent components (Cartesian, un-normalized)
    # d/dphi
    dphi_x = -(R + r * np.cos(psi)) * np.sin(phi)
    dphi_y = (R + r * np.cos(psi)) * np.cos(phi)
    dphi_z = np.zeros_like(phi)
    # d/dpsi
    dpsi_x = -r * np.sin(psi) * np.cos(phi)
    dpsi_y = -r * np.sin(psi) * np.sin(phi)
    dpsi_z = r * np.cos(psi) * np.ones_like(phi)
    # (2,3) tangent
    t_x = 2.0 * dphi_x + 3.0 * dpsi_x
    t_y = 2.0 * dphi_y + 3.0 * dpsi_y
    t_z = 2.0 * dphi_z + 3.0 * dpsi_z
    t_mag = np.sqrt(t_x**2 + t_y**2 + t_z**2 + 1e-12)
    t_hat_x = t_x / t_mag
    t_hat_y = t_y / t_mag
    t_hat_z = t_z / t_mag

    # K4 tetrahedral port directions (A-sublattice)
    ports = [
        (+1.0, +1.0, +1.0),
        (+1.0, -1.0, -1.0),
        (-1.0, +1.0, -1.0),
        (-1.0, -1.0, +1.0),
    ]
    # Normalize to unit vectors (each has magnitude sqrt(3))
    inv_sqrt3 = 1.0 / np.sqrt(3.0)

    theta_wind = 2.0 * phi + 3.0 * psi
    cos_theta = np.cos(theta_wind)
    sin_theta = np.sin(theta_wind)

    # Attribute 3: chirality weighting per port = p_k_hat . t_hat
    # Attribute 2: phase — quadrature pattern across ports
    #   ports 0, 1 carry cos(theta); ports 2, 3 carry sin(theta)
    for p_idx, (px, py, pz) in enumerate(ports):
        chirality_weight = inv_sqrt3 * (
            px * t_hat_x + py * t_hat_y + pz * t_hat_z
        )
        if p_idx < 2:
            phase_pattern = cos_theta
        else:
            phase_pattern = sin_theta
        lattice.V_inc[..., p_idx] = envelope * chirality_weight * phase_pattern

    # Zero out inactive K4 sites (A or B sublattices only).
    lattice.V_inc[~lattice.mask_active] = 0.0


def initialize_phi_link_2_3_ansatz(
    lattice: K4Lattice3D,
    R: float,
    r: float,
    amplitude: float = 0.5,
) -> None:
    """Populate K4 Phi_link (bond flux linkage) with a (2,3) chiral-phasor
    pattern at A-sites — the L-state seeder for the K4 LC pair (V_inc ↔ Φ_link).

    Use case (Round 6 F17-I): for an "all-L-state" coupled eigenmode seed,
    call this together with initialize_electron_2_3_sector on the Cosserat
    side — both at L-state amplitude, all C-states (V_inc, u) zeroed. Per
    doc 66_ §17.2.3 this is the LC-pair-coherent counterpart to all-C-state.

    Mirrors initialize_2_3_voltage_ansatz (same toroidal coords, same
    hedgehog envelope, same θ = 2φ + 3ψ winding, same chirality_weight
    port projection, same cos-on-ports-0,1 / sin-on-ports-2,3 quadrature)
    — but populates lattice.Phi_link instead of lattice.V_inc.

    Phi_link is bond-level state (4 ports per A-site, accumulated via
    V_avg·dt during integration); direct assignment is safe (test_phase3
    confirms scatter does not touch it). External seed persists and is
    augmented by integrator's V_avg·dt accumulation.

    amplitude: peak |Phi_link| in same V_avg·dt convention as the
    integrator. Default 0.5 ≈ V_max/ω_C in V_SNAP·τ_node natural units
    (V_max = 0.9·V_YIELD, ω_C = 2π/3.5 ≈ 1.795 in Phase 5 driver units).

    Per doc 54_ §3 derivation: Φ_critical = √2 in V_SNAP·τ_node natural
    units; default 0.5 is sub-critical.
    """
    cx = (lattice.nx - 1) / 2.0
    cy = (lattice.ny - 1) / 2.0
    cz = (lattice.nz - 1) / 2.0

    idx = np.indices((lattice.nx, lattice.ny, lattice.nz))
    i, j, k = idx[0], idx[1], idx[2]
    x = i - cx
    y = j - cy
    z = k - cz

    rho_xy = np.sqrt(x**2 + y**2 + 1e-12)
    rho_tube = np.sqrt((rho_xy - R) ** 2 + z**2 + 1e-12)
    phi = np.arctan2(y, x)
    psi = np.arctan2(z, rho_xy - R)

    # Magnitude — power-law hedgehog envelope (same as V_inc seeder)
    r_opt = max(r, 1.0)
    envelope = amplitude * np.pi / (1.0 + (rho_tube / r_opt) ** 2)

    # (2,3) knot tangent (un-normalized)
    dphi_x = -(R + r * np.cos(psi)) * np.sin(phi)
    dphi_y = (R + r * np.cos(psi)) * np.cos(phi)
    dphi_z = np.zeros_like(phi)
    dpsi_x = -r * np.sin(psi) * np.cos(phi)
    dpsi_y = -r * np.sin(psi) * np.sin(phi)
    dpsi_z = r * np.cos(psi) * np.ones_like(phi)
    t_x = 2.0 * dphi_x + 3.0 * dpsi_x
    t_y = 2.0 * dphi_y + 3.0 * dpsi_y
    t_z = 2.0 * dphi_z + 3.0 * dpsi_z
    t_mag = np.sqrt(t_x**2 + t_y**2 + t_z**2 + 1e-12)
    t_hat_x = t_x / t_mag
    t_hat_y = t_y / t_mag
    t_hat_z = t_z / t_mag

    # K4 tetrahedral port directions (same as V_inc seeder)
    ports = [
        (+1.0, +1.0, +1.0),
        (+1.0, -1.0, -1.0),
        (-1.0, +1.0, -1.0),
        (-1.0, -1.0, +1.0),
    ]
    inv_sqrt3 = 1.0 / np.sqrt(3.0)

    theta_wind = 2.0 * phi + 3.0 * psi
    cos_theta = np.cos(theta_wind)
    sin_theta = np.sin(theta_wind)

    # Same port quadrature as V_inc seeder: cos on ports 0,1; sin on ports 2,3.
    # This preserves the 90° phase relationship across the tetrahedral basis
    # that the Cosserat-side rotational LC has between θ and ω.
    for p_idx, (px, py, pz) in enumerate(ports):
        chirality_weight = inv_sqrt3 * (
            px * t_hat_x + py * t_hat_y + pz * t_hat_z
        )
        if p_idx < 2:
            phase_pattern = cos_theta
        else:
            phase_pattern = sin_theta
        lattice.Phi_link[..., p_idx] = envelope * chirality_weight * phase_pattern

    # Phi_link is A-site-only state (per k4_tlm.py:391 only A-sites accumulate).
    # Mask non-A sites to zero.
    lattice.Phi_link[~lattice.mask_A] = 0.0


def initialize_quadrature_2_3_eigenmode(
    lattice: K4Lattice3D,
    R: float,
    r: float,
    amplitude: float = 0.05,
    chirality: float = 1.0,
) -> None:
    """F17-K Phase 5 — phase-coherent (V_inc, V_ref) seed at 90° quadrature
    in (2,3) phase-space pattern.

    AVE-native eigenmode initial condition per [doc 28_:64-67](../../research/L3_electron_soliton/28_two_node_electron_synthesis.md#L64)
    and [doc 68_ §7](../../research/L3_electron_soliton/68_phase_quadrature_methodology.md#L7):
    the (V_inc, V_ref) phasor pair traces the (2,3) torus-knot winding
    pattern in phase-space at R_phase=φ/2, r_phase=(φ-1)/2. At t=0:

        V_inc[..., p] = envelope(x) · chirality_weight_p · cos(2φ + 3ψ)
        V_ref[..., p] = envelope(x) · chirality_weight_p · sin(2φ + 3ψ)

    Per-port phasor angle ψ_port(x, p) = arctan2(V_ref, V_inc) = 2φ + 3ψ
    winds 2 times around the major-axis (φ) and 3 times around the
    minor-axis (ψ). This is the phase-space (2,3) winding doc 28_ §3
    requires — the actual TKI invariant per Ax 2.

    `chirality` parameter:
      0.0 → port-uniform (handedness-symmetric, both helicities seeded)
      1.0 → full chirality projection per port = (p̂_k · t̂_(2,3)), encoding
            right-handed K4 chirality that distinguishes electron from positron
            (default — for explicit electron seed)

    `amplitude` defaults to 0.05 in engine natural units (V_SNAP=1).
    Engine-natural V_yield ≈ √α ≈ 0.0854; default 0.05 is sub-yield.
    Avoid the F17-I unit bug (`0.9 * V_YIELD` mixes SI+natural — see
    A29 / Flag-5e-A class).

    Use case: pair with `cos.initialize_electron_2_3_sector` (Cosserat ω
    at amplitude_scale 0.346, peak |ω|=0.3π) for a fully coupled
    phase-coherent seed across both K4 and Cosserat sectors. Drives
    [`coupled_relax_s11`](coupled_engine_eigenmode.py) to find the
    impedance-matched eigenmode under Ax-3.
    """
    cx = (lattice.nx - 1) / 2.0
    cy = (lattice.ny - 1) / 2.0
    cz = (lattice.nz - 1) / 2.0

    idx = np.indices((lattice.nx, lattice.ny, lattice.nz))
    i, j, k = idx[0], idx[1], idx[2]
    x = i - cx
    y = j - cy
    z = k - cz

    rho_xy = np.sqrt(x**2 + y**2 + 1e-12)
    rho_tube = np.sqrt((rho_xy - R) ** 2 + z**2 + 1e-12)
    phi = np.arctan2(y, x)
    psi = np.arctan2(z, rho_xy - R)

    r_opt = max(r, 1.0)
    envelope = amplitude * np.pi / (1.0 + (rho_tube / r_opt) ** 2)

    # (2,3) knot tangent (same as V_inc seeder)
    dphi_x = -(R + r * np.cos(psi)) * np.sin(phi)
    dphi_y = (R + r * np.cos(psi)) * np.cos(phi)
    dphi_z = np.zeros_like(phi)
    dpsi_x = -r * np.sin(psi) * np.cos(phi)
    dpsi_y = -r * np.sin(psi) * np.sin(phi)
    dpsi_z = r * np.cos(psi) * np.ones_like(phi)
    t_x = 2.0 * dphi_x + 3.0 * dpsi_x
    t_y = 2.0 * dphi_y + 3.0 * dpsi_y
    t_z = 2.0 * dphi_z + 3.0 * dpsi_z
    t_mag = np.sqrt(t_x**2 + t_y**2 + t_z**2 + 1e-12)
    t_hat_x = t_x / t_mag
    t_hat_y = t_y / t_mag
    t_hat_z = t_z / t_mag

    ports = [
        (+1.0, +1.0, +1.0),
        (+1.0, -1.0, -1.0),
        (-1.0, +1.0, -1.0),
        (-1.0, -1.0, +1.0),
    ]
    inv_sqrt3 = 1.0 / np.sqrt(3.0)

    theta_wind = 2.0 * phi + 3.0 * psi
    cos_theta = np.cos(theta_wind)
    sin_theta = np.sin(theta_wind)

    for p_idx, (px, py, pz) in enumerate(ports):
        chirality_weight = inv_sqrt3 * (
            px * t_hat_x + py * t_hat_y + pz * t_hat_z
        )
        # Blend port-uniform (1.0) with chirality projection per `chirality` knob
        port_factor = (1.0 - chirality) * 1.0 + chirality * chirality_weight
        # 90° quadrature: V_inc = cos·factor, V_ref = sin·factor at every port
        lattice.V_inc[..., p_idx] = envelope * port_factor * cos_theta
        lattice.V_ref[..., p_idx] = envelope * port_factor * sin_theta

    # Mask inactive sites (only K4-active sites carry V_inc/V_ref dynamics)
    lattice.V_inc[~lattice.mask_active] = 0.0
    lattice.V_ref[~lattice.mask_active] = 0.0


def _apply_2_3_ansatz_with_envelope(
    lattice: K4Lattice3D,
    R: float,
    r: float,
    amplitude: float,
    envelope_fn,
) -> None:
    """Shared implementation: populate V_inc with (2,3) chiral phasor
    pattern using an arbitrary radial-envelope shape.

    `envelope_fn(rho_tube, r_opt, amplitude) → ndarray` specifies the
    magnitude profile. Phase winding θ=2φ+3ψ, port quadrature (cos on
    ports 0,1; sin on 2,3), and chirality weighting are identical across
    all envelope variants — only the magnitude differs.

    Used by the three `initialize_2_3_voltage_ansatz_*` wrappers below
    to enable seed-independence testing: a true dynamical eigenmode
    should be reachable from any envelope in the basin of attraction.
    """
    cx = (lattice.nx - 1) / 2.0
    cy = (lattice.ny - 1) / 2.0
    cz = (lattice.nz - 1) / 2.0

    idx = np.indices((lattice.nx, lattice.ny, lattice.nz))
    i, j, k = idx[0], idx[1], idx[2]
    x = i - cx
    y = j - cy
    z = k - cz

    rho_xy = np.sqrt(x**2 + y**2 + 1e-12)
    rho_tube = np.sqrt((rho_xy - R) ** 2 + z**2 + 1e-12)
    phi_ang = np.arctan2(y, x)
    psi_ang = np.arctan2(z, rho_xy - R)

    r_opt = max(r, 1.0)
    envelope = envelope_fn(rho_tube, r_opt, amplitude)

    dphi_x = -(R + r * np.cos(psi_ang)) * np.sin(phi_ang)
    dphi_y = (R + r * np.cos(psi_ang)) * np.cos(phi_ang)
    dphi_z = np.zeros_like(phi_ang)
    dpsi_x = -r * np.sin(psi_ang) * np.cos(phi_ang)
    dpsi_y = -r * np.sin(psi_ang) * np.sin(phi_ang)
    dpsi_z = r * np.cos(psi_ang) * np.ones_like(phi_ang)
    t_x = 2.0 * dphi_x + 3.0 * dpsi_x
    t_y = 2.0 * dphi_y + 3.0 * dpsi_y
    t_z = 2.0 * dphi_z + 3.0 * dpsi_z
    t_mag = np.sqrt(t_x**2 + t_y**2 + t_z**2 + 1e-12)
    t_hat_x = t_x / t_mag
    t_hat_y = t_y / t_mag
    t_hat_z = t_z / t_mag

    ports = [
        (+1.0, +1.0, +1.0),
        (+1.0, -1.0, -1.0),
        (-1.0, +1.0, -1.0),
        (-1.0, -1.0, +1.0),
    ]
    inv_sqrt3 = 1.0 / np.sqrt(3.0)

    theta_wind = 2.0 * phi_ang + 3.0 * psi_ang
    cos_theta = np.cos(theta_wind)
    sin_theta = np.sin(theta_wind)

    for p_idx, (px, py, pz) in enumerate(ports):
        chirality_weight = inv_sqrt3 * (
            px * t_hat_x + py * t_hat_y + pz * t_hat_z
        )
        phase_pattern = cos_theta if p_idx < 2 else sin_theta
        lattice.V_inc[..., p_idx] = envelope * chirality_weight * phase_pattern

    lattice.V_inc[~lattice.mask_active] = 0.0


def initialize_2_3_voltage_ansatz_gaussian(
    lattice: K4Lattice3D,
    R: float,
    r: float,
    amplitude: float = 0.5,
) -> None:
    """(2,3) ansatz with Gaussian radial envelope `A·π·exp(−(ρ_tube/r)²)`.

    Seed-independence variant. Same phase winding, port quadrature, and
    chirality weighting as the power-law hedgehog; only the magnitude
    profile changes. See `_apply_2_3_ansatz_with_envelope` for shared
    logic.
    """
    def envelope_fn(rho_tube, r_opt, amp):
        return amp * np.pi * np.exp(-(rho_tube / r_opt) ** 2)
    _apply_2_3_ansatz_with_envelope(lattice, R, r, amplitude, envelope_fn)


def initialize_2_3_voltage_ansatz_exponential(
    lattice: K4Lattice3D,
    R: float,
    r: float,
    amplitude: float = 0.5,
) -> None:
    """(2,3) ansatz with exponential radial envelope `A·π·exp(−ρ_tube/r)`.

    Seed-independence variant. Same phase winding, port quadrature, and
    chirality weighting as the power-law hedgehog; only the magnitude
    profile changes. See `_apply_2_3_ansatz_with_envelope` for shared
    logic.
    """
    def envelope_fn(rho_tube, r_opt, amp):
        return amp * np.pi * np.exp(-rho_tube / r_opt)
    _apply_2_3_ansatz_with_envelope(lattice, R, r, amplitude, envelope_fn)


def shell_envelope(
    V_magnitude: np.ndarray, cx: float, cy: float, cz: float
) -> tuple[float, float]:
    """Extract (R_max, r_hwhm) from a scalar field magnitude via
    radial histogram at z = center. R_max is the major-axis bin with
    peak amplitude; r_hwhm is the FWHM/2 of the peak in the radial
    direction. Same scheme as CosseratField3D.extract_shell_radii.
    """
    nx, ny, nz = V_magnitude.shape
    kz = int(round(cz))
    slice_z = V_magnitude[:, :, kz]
    xs = np.indices((nx, ny))[0] - cx
    ys = np.indices((nx, ny))[1] - cy
    rho = np.sqrt(xs**2 + ys**2)

    rho_flat = rho.flatten()
    mag_flat = slice_z.flatten()
    rho_max = float(rho.max())
    n_bins = max(8, int(round(rho_max)))
    edges = np.linspace(0.0, rho_max, n_bins + 1)
    hist, _ = np.histogram(rho_flat, bins=edges, weights=mag_flat)
    counts, _ = np.histogram(rho_flat, bins=edges)
    with np.errstate(divide="ignore", invalid="ignore"):
        profile = np.where(counts > 0, hist / np.maximum(counts, 1), 0.0)
    centers = 0.5 * (edges[:-1] + edges[1:])

    if profile.max() <= 0:
        return 0.0, 0.0
    R_found = float(centers[np.argmax(profile)])
    half_max = 0.5 * profile.max()
    above = profile >= half_max
    if above.any():
        left = centers[above][0]
        right = centers[above][-1]
        r_found = float(0.5 * (right - left))
    else:
        r_found = 0.0
    return R_found, r_found


def run_tlm_electron(
    N: int = 48,
    R: float = 12.0,
    r: float = 4.58,
    n_steps: int = 400,
    amplitude: float = 0.5,
    pml_thickness: int = 6,
    sample_every: int = 20,
    verbose: bool = True,
    nonlinear: bool = False,
    op3_bond_reflection: bool = True,
    rms_avg_last_n: int = 100,
) -> dict:
    """Run a TLM electron-soliton simulation and collect diagnostics.

    With op3_bond_reflection=True (recommended), each bond applies Op3
    reflection based on the impedance mismatch between adjacent sites.
    Needed for bound solitons — without this, linear K4-TLM has no
    mechanism to confine a (2,3) voltage pattern to Golden Torus geometry.
    """
    lattice = K4Lattice3D(
        N, N, N, dx=1.0, pml_thickness=pml_thickness,
        nonlinear=nonlinear, op3_bond_reflection=op3_bond_reflection,
    )
    initialize_2_3_voltage_ansatz(lattice, R=R, r=r, amplitude=amplitude)

    cx = (lattice.nx - 1) / 2.0
    cy = (lattice.ny - 1) / 2.0
    cz = (lattice.nz - 1) / 2.0

    # Initial diagnostics
    V_mag = np.sqrt(np.sum(lattice.V_inc**2, axis=-1))
    total_energy_0 = float(np.sum(V_mag**2))
    R_0, r_0 = shell_envelope(V_mag, cx, cy, cz)

    if verbose:
        print(f"  Lattice: {N}³ (pml={pml_thickness}); target (R, r) = ({R:.2f}, {r:.2f})")
        print(f"  Initial: total_E = {total_energy_0:.4e}, shell (R, r) = ({R_0:.3f}, {r_0:.3f})")

    energy_trace = [total_energy_0]
    Rs, rs = [R_0], [r_0]
    step_sampled = [0]

    # Time-averaged V_phys² = (V_inc + V_ref)² accumulator over the last
    # rms_avg_last_n steps. This IS the capacitive energy density ½CV² at
    # each node — the Ch-8-compatible quantity for extracting the electron's
    # charge-distribution geometry. V_inc² or V_inc²+V_ref² are mixed
    # quantities that give wrong (R, r) — see handoff §18.
    rms_accumulator = np.zeros(lattice.V_inc.shape[:3], dtype=np.float64)
    rms_count = 0
    rms_start_step = max(1, n_steps - rms_avg_last_n + 1)

    for step in range(1, n_steps + 1):
        lattice.step()
        if step >= rms_start_step:
            # V_phys = V_inc + V_ref at each port, squared and summed over ports.
            V_phys = lattice.V_inc + lattice.V_ref
            rms_accumulator += np.sum(V_phys**2, axis=-1)
            rms_count += 1
        if step % sample_every == 0:
            V_mag = np.sqrt(np.sum(lattice.V_inc**2, axis=-1))
            E = float(np.sum(V_mag**2))
            R_s, r_s = shell_envelope(V_mag, cx, cy, cz)
            energy_trace.append(E)
            Rs.append(R_s)
            rs.append(r_s)
            step_sampled.append(step)
            if verbose:
                ratio = R_s / max(r_s, 1e-6)
                print(f"  step {step:4d}: E = {E:.3e}  (R, r) = ({R_s:.3f}, {r_s:.3f})  R/r = {ratio:.3f}")

    # Time-averaged |V|² = ⟨|V_inc|²⟩ over the last rms_avg_last_n steps.
    # For a pure standing wave A(r)cos(ωt), this gives A²(r)/2 ≡ RMS² envelope.
    # Extract R, r from THIS (phase-independent envelope), not from a snapshot.
    V_rms_sq_field = rms_accumulator / max(rms_count, 1)
    V_rms_field = np.sqrt(V_rms_sq_field)
    R_rms, r_rms = shell_envelope(V_rms_field, cx, cy, cz)

    if verbose:
        print(f"  Time-averaged ({rms_count} steps): (R_rms, r_rms) = ({R_rms:.3f}, {r_rms:.3f})  R/r = {R_rms/max(r_rms, 1e-9):.3f}")

    return {
        "steps": np.asarray(step_sampled),
        "energy": np.asarray(energy_trace),
        "R": np.asarray(Rs),
        "r": np.asarray(rs),
        "R_rms": R_rms,
        "r_rms": r_rms,
        "V_rms_field": V_rms_field,
        "final_Vinc": lattice.V_inc.copy(),
        "lattice": lattice,
    }


def extract_crossing_count_tlm(lattice, R_major: float) -> int:
    """Count N_crossings on a TLM lattice by Op11 topological-curl integration.

    Uses the xy-plane V_inc amplitude at z = center, scans a contour at
    major radius R_major, and counts how many phase-2π cycles the field
    winds through. For a (2,3) torus-knot pattern, expect c = 3 on a
    contour that threads the shell.

    Adapted from CosseratField3D.extract_crossing_count via port-summed V.
    """
    nx, ny, nz = lattice.nx, lattice.ny, lattice.nz
    cx = (nx - 1) / 2.0
    cy = (ny - 1) / 2.0
    cz = (nz - 1) / 2.0

    # Sample contour at varying minor radii; pick most reliable winding
    best_winding = 0
    for r_minor in np.linspace(1.0, max(3.0, R_major * 0.5), 8):
        n_psi = 128
        psis = np.linspace(0.0, 2.0 * np.pi, n_psi, endpoint=False)
        dx_s = cx + (R_major + r_minor * np.cos(psis))
        dy_s = cy + np.zeros_like(psis)
        dz_s = cz + r_minor * np.sin(psis)

        ix = np.clip(dx_s.astype(int), 0, nx - 2)
        iy = np.clip(dy_s.astype(int), 0, ny - 2)
        iz = np.clip(dz_s.astype(int), 0, nz - 2)
        fx = dx_s - ix
        fy = dy_s - iy
        fz = dz_s - iz

        def trilinear_sample(field):
            v000 = field[ix, iy, iz]
            v100 = field[ix + 1, iy, iz]
            v010 = field[ix, iy + 1, iz]
            v001 = field[ix, iy, iz + 1]
            v110 = field[ix + 1, iy + 1, iz]
            v101 = field[ix + 1, iy, iz + 1]
            v011 = field[ix, iy + 1, iz + 1]
            v111 = field[ix + 1, iy + 1, iz + 1]
            return (
                (1 - fx) * (1 - fy) * (1 - fz) * v000
                + fx * (1 - fy) * (1 - fz) * v100
                + (1 - fx) * fy * (1 - fz) * v010
                + (1 - fx) * (1 - fy) * fz * v001
                + fx * fy * (1 - fz) * v110
                + fx * (1 - fy) * fz * v101
                + (1 - fx) * fy * fz * v011
                + fx * fy * fz * v111
            )

        # Phase-quadrature pair: init puts cos(θ) on ports {0,1} and sin(θ)
        # on ports {2,3}. Combine port-pair sums to recover the complex phasor.
        ox = trilinear_sample(lattice.V_inc[..., 0] + lattice.V_inc[..., 1])
        oy = trilinear_sample(lattice.V_inc[..., 2] + lattice.V_inc[..., 3])
        amp = np.sqrt(ox**2 + oy**2)
        if amp.max() <= 0:
            continue
        if amp.min() / amp.max() < 0.05:
            continue  # too much phase noise
        phase = np.arctan2(oy, ox)
        unwrapped = np.unwrap(phase)
        total_winding = (unwrapped[-1] - unwrapped[0]) / (2.0 * np.pi)
        # Add closure term
        closure = phase[0] - unwrapped[-1]
        while closure > np.pi:
            closure -= 2.0 * np.pi
        while closure < -np.pi:
            closure += 2.0 * np.pi
        total_winding += closure / (2.0 * np.pi)
        w = int(round(abs(total_winding)))
        if w > best_winding:
            best_winding = w
    return best_winding


def _contour_winding(lattice, R_major: float, r_minor: float,
                     direction: str, n_samples: int = 128) -> tuple:
    """Sample the V_inc phasor on a circular contour and return (signed_winding, amplitude_min_max_ratio).

    direction='poloidal': contour at fixed phi=0 sweeping psi (around minor circle).
        The signed winding integer counts the q-component of the (p,q) torus-knot
        winding observed in the poloidal direction.

    direction='toroidal': contour at fixed psi=0 sweeping phi (around major axis).
        Counts the p-component (toroidal winding) of the (p,q) pattern.

    The phasor recovery uses the port-quadrature pairing from the (2,3) ansatz
    initialization (cos on ports {0,1}, sin on ports {2,3}).
    """
    nx, ny, nz = lattice.nx, lattice.ny, lattice.nz
    cx = (nx - 1) / 2.0
    cy = (ny - 1) / 2.0
    cz = (nz - 1) / 2.0

    if direction == 'poloidal':
        # Fixed phi = 0 (xz-plane), sweep psi
        s = np.linspace(0.0, 2.0 * np.pi, n_samples, endpoint=False)
        dx_s = cx + (R_major + r_minor * np.cos(s))
        dy_s = cy + np.zeros_like(s)
        dz_s = cz + r_minor * np.sin(s)
    elif direction == 'toroidal':
        # Fixed psi = 0 (outer equator at z=0), sweep phi
        s = np.linspace(0.0, 2.0 * np.pi, n_samples, endpoint=False)
        rho = R_major + r_minor  # outer equator
        dx_s = cx + rho * np.cos(s)
        dy_s = cy + rho * np.sin(s)
        dz_s = cz + np.zeros_like(s)
    else:
        raise ValueError(f"direction must be 'poloidal' or 'toroidal', got {direction!r}")

    ix = np.clip(dx_s.astype(int), 0, nx - 2)
    iy = np.clip(dy_s.astype(int), 0, ny - 2)
    iz = np.clip(dz_s.astype(int), 0, nz - 2)
    fx = dx_s - ix
    fy = dy_s - iy
    fz = dz_s - iz

    def trilinear_sample(field):
        v000 = field[ix, iy, iz]
        v100 = field[ix + 1, iy, iz]
        v010 = field[ix, iy + 1, iz]
        v001 = field[ix, iy, iz + 1]
        v110 = field[ix + 1, iy + 1, iz]
        v101 = field[ix + 1, iy, iz + 1]
        v011 = field[ix, iy + 1, iz + 1]
        v111 = field[ix + 1, iy + 1, iz + 1]
        return (
            (1 - fx) * (1 - fy) * (1 - fz) * v000
            + fx * (1 - fy) * (1 - fz) * v100
            + (1 - fx) * fy * (1 - fz) * v010
            + (1 - fx) * (1 - fy) * fz * v001
            + fx * fy * (1 - fz) * v110
            + fx * (1 - fy) * fz * v101
            + (1 - fx) * fy * fz * v011
            + fx * fy * fz * v111
        )

    # Phasor: ports {0,1} = cos, ports {2,3} = sin (quadrature from (2,3) init)
    ox = trilinear_sample(lattice.V_inc[..., 0] + lattice.V_inc[..., 1])
    oy = trilinear_sample(lattice.V_inc[..., 2] + lattice.V_inc[..., 3])
    amp = np.sqrt(ox ** 2 + oy ** 2)

    if amp.max() <= 0:
        return 0.0, 0.0
    amp_ratio = amp.min() / amp.max()
    if amp_ratio < 0.05:
        return 0.0, amp_ratio  # too noisy

    phase = np.arctan2(oy, ox)
    unwrapped = np.unwrap(phase)
    # Signed winding (positive = right-handed)
    total = (unwrapped[-1] - unwrapped[0]) / (2.0 * np.pi)
    closure = phase[0] - unwrapped[-1]
    while closure > np.pi:
        closure -= 2.0 * np.pi
    while closure < -np.pi:
        closure += 2.0 * np.pi
    total += closure / (2.0 * np.pi)
    return float(total), float(amp_ratio)


def extract_chirality_measured(lattice, R_major: float) -> dict:
    """Extract signed (p, q) windings from the TLM lattice and compute χ.

    Per Sub-theorem 3.1.1 in `research/L3_electron_soliton/20_chirality_projection_sub_theorem.md`:

        χ_(p,q) = α · pq / (p+q)

    For the (2,3) electron at Golden Torus, target χ = α·6/5 ≈ 8.757×10⁻³.
    Sign of χ distinguishes electron (right-handed (2,3)) from positron
    (left-handed (2,3) = mirror image with opposite handedness).

    Method:
    - Poloidal contour (vary psi) → measures signed q
    - Toroidal contour (vary phi) → measures signed p
    - Both at multiple minor radii; pick reading with best amplitude ratio
    - χ_measured = α · p_measured · q_measured / (p_measured + q_measured)

    Returns:
        {
            'p_measured': signed toroidal winding (float, ~ ±integer),
            'q_measured': signed poloidal winding (float, ~ ±integer),
            'chi_measured': α · pq / (p+q) signed scalar,
            'chi_target': α · 6/5 (right-handed (2,3) electron),
            'chi_error_rel': |chi_measured - chi_target| / |chi_target|,
            'amp_ratio_p': amplitude min/max on toroidal contour (quality metric),
            'amp_ratio_q': same on poloidal contour,
            'valid': True iff both contours had usable amplitude,
        }
    """
    # Sweep minor radii to find the most reliable reading
    best_p = (0.0, 0.0)  # (signed_winding, amp_ratio)
    best_q = (0.0, 0.0)
    for r_minor in np.linspace(1.0, max(3.0, R_major * 0.5), 8):
        p_w, p_amp = _contour_winding(lattice, R_major, r_minor, 'toroidal')
        q_w, q_amp = _contour_winding(lattice, R_major, r_minor, 'poloidal')
        if p_amp > best_p[1]:
            best_p = (p_w, p_amp)
        if q_amp > best_q[1]:
            best_q = (q_w, q_amp)

    p_meas = best_p[0]
    q_meas = best_q[0]
    valid = (best_p[1] > 0.05) and (best_q[1] > 0.05)

    chi_target = ALPHA * 6.0 / 5.0  # (2,3) right-handed electron
    if abs(p_meas) < 1e-3 or abs(q_meas) < 1e-3 or abs(p_meas + q_meas) < 1e-3:
        chi_measured = 0.0
    else:
        chi_measured = ALPHA * p_meas * q_meas / (p_meas + q_meas)

    chi_error_rel = (abs(chi_measured - chi_target) / abs(chi_target)
                     if chi_target != 0 else float('inf'))

    return {
        'p_measured': p_meas,
        'q_measured': q_meas,
        'chi_measured': chi_measured,
        'chi_target': chi_target,
        'chi_error_rel': chi_error_rel,
        'amp_ratio_p': best_p[1],
        'amp_ratio_q': best_q[1],
        'valid': valid,
    }


def convergence_check(alpha_inv: float, chi_measured: float,
                      alpha_target: float = None,
                      chi_target: float = None,
                      tol: float = 0.015) -> dict:
    """Two-target convergence check for the L3 electron Path C.

    Convergence requires BOTH:
    - α⁻¹ within tol fractional error of target (default 137.036)
    - χ within tol fractional error of α·6/5

    Per Path C plan §18.4 in
    `.claude/plans/read-the-collaboration-md-first-resilient-mccarthy.md`.
    """
    if alpha_target is None:
        from ave.core.constants import ALPHA_COLD_INV
        alpha_target = ALPHA_COLD_INV
    if chi_target is None:
        chi_target = ALPHA * 6.0 / 5.0

    alpha_err = (abs(alpha_inv - alpha_target) / alpha_target
                 if alpha_target != 0 else float('inf'))
    chi_err = (abs(chi_measured - chi_target) / abs(chi_target)
               if chi_target != 0 else float('inf'))

    converged = (alpha_err < tol) and (chi_err < tol)
    return {
        'converged': converged,
        'alpha_err': alpha_err,
        'chi_err': chi_err,
        'tol': tol,
    }


def extract_alpha_inverse(R: float, r: float, c: int = 3) -> dict:
    """Ch 8 multipole decomposition at extracted (R, r) with crossing count c.

    Uses d = 2(R - r) from Ch 8's self-avoidance constraint. Ch 8's Λ_surf
    scales with N_cross per Op10 (Y_loss = c (1-cos θ)/(2π²) at each crossing,
    summed — hence the surface term grows linearly with c). Grant's 2026-04-20
    note: "total reactance is tied to N number of crossings."

    For c = 3 (electron): Λ_surf = 4π² (R·r/d²)   → π² at Golden Torus.
    General c:            Λ_surf = (c/3) × 4π² (R·r/d²) = (4π²c/3) (R·r/d²).
    """
    if R <= r or r <= 0:
        return {"valid": False}
    d = 2.0 * (R - r)
    if d <= 0:
        return {"valid": False}
    ratio_self_avoid = (R - r) / d
    ratio_screen = (R * r) / (d * d)
    Lambda_vol = 16.0 * np.pi**3 * ratio_screen
    # Surface term scales linearly with crossing count (Op10). At c=3 this
    # recovers Ch 8's 4π² R·r/d² form.
    Lambda_surf = (c / 3.0) * 4.0 * np.pi**2 * ratio_screen
    Lambda_line = np.pi
    alpha_inv = Lambda_vol + Lambda_surf + Lambda_line
    return {
        "valid": True,
        "d": d,
        "c": c,
        "ratio_self_avoid": ratio_self_avoid,
        "ratio_screen": ratio_screen,
        "Lambda_vol": Lambda_vol,
        "Lambda_surf": Lambda_surf,
        "Lambda_line": Lambda_line,
        "alpha_inv": alpha_inv,
    }


def solve_eigenmode_self_consistent(
    N: int,
    R_seed: float,
    r_seed: float,
    amplitude: float,
    n_steps: int = 300,
    sample_every: int = 100,
    max_iter: int = 6,
    tol: float = 1e-3,
    verbose: bool = True,
) -> dict:
    """Op6 eigenvalue self-consistency loop for the (2,3) electron soliton.

    At each outer iteration: initialize the TLM with (R_k, r_k), evolve to
    steady state, extract (R_{k+1}, r_{k+1}) from the time-RMS V_phys^2
    envelope, and iterate. Converges when |ΔR|/R < tol AND |Δr|/r < tol.

    The physical claim: if the (2,3) sector has a self-consistent bound
    eigenmode, successive iterations converge to that mode regardless of
    seed (within the basin). If iterations diverge or cycle, no
    self-consistent eigenmode exists at this amplitude.

    Returns a trajectory of (R, r) over outer iterations + final α⁻¹.
    """
    R_k = R_seed
    r_k = r_seed
    history = [(R_k, r_k, None)]  # (R, r, alpha_inv) trajectory

    for outer_iter in range(1, max_iter + 1):
        if verbose:
            print(f"\n=== Op6 outer iteration {outer_iter} ===")
            print(f"  Seed (R, r) = ({R_k:.3f}, {r_k:.3f})")

        result = run_tlm_electron(
            N=N, R=R_k, r=r_k,
            n_steps=n_steps, sample_every=sample_every, amplitude=amplitude,
            nonlinear=False, pml_thickness=0, op3_bond_reflection=True,
            rms_avg_last_n=max(50, n_steps // 3),
            verbose=False,
        )
        R_new = float(result['R_rms'])
        r_new = float(result['r_rms'])
        alpha = extract_alpha_inverse(R_new, r_new, c=3)
        alpha_inv = alpha['alpha_inv'] if alpha['valid'] else float('nan')
        history.append((R_new, r_new, alpha_inv))

        if R_k > 0 and r_k > 0:
            dR_rel = abs(R_new - R_k) / R_k
            dr_rel = abs(r_new - r_k) / r_k
        else:
            dR_rel = dr_rel = float('inf')

        if verbose:
            print(f"  Extracted (R, r) = ({R_new:.3f}, {r_new:.3f})  "
                  f"R/r = {R_new / max(r_new, 1e-9):.3f}  α⁻¹ = {alpha_inv:.3f}")
            print(f"  ΔR/R = {dR_rel:.2e}  Δr/r = {dr_rel:.2e}  (tol={tol:.0e})")

        if dR_rel < tol and dr_rel < tol:
            if verbose:
                print(f"  → Converged after {outer_iter} iterations.")
            return {
                "converged": True,
                "iterations": outer_iter,
                "trajectory": history,
                "final_R": R_new,
                "final_r": r_new,
                "final_alpha_inv": alpha_inv,
            }

        # Feed the extracted values back as the new seed.
        R_k, r_k = R_new, r_new

    if verbose:
        print(f"  → Did NOT converge within {max_iter} iterations.")
    return {
        "converged": False,
        "iterations": max_iter,
        "trajectory": history,
        "final_R": R_k,
        "final_r": r_k,
        "final_alpha_inv": history[-1][2],
    }


def solve_eigenmode_dual_target(
    N: int,
    R_target: float,
    r_target: float,
    amp_init: float,
    n_steps: int = 200,
    pml_thickness: int = 0,
    max_outer_iter: int = 12,
    tol: float = 0.015,
    scale_exp: float = 0.1,
    damping: float = 0.5,
    verbose: bool = True,
) -> dict:
    """Path C: dual-target convergence loop for the L3 electron.

    Per `.claude/plans/read-the-collaboration-md-first-resilient-mccarthy.md`
    §18, replaces the divergent (R, r) self-consistency SCF with an
    AMPLITUDE-adjustment outer loop driven by two scalar convergence
    targets:

      - α⁻¹_measured(R, r, c) → 137.036 ± tol  (Theorem 3.1)
      - χ_measured(V_inc field) → α·6/5 ± tol (Sub-theorem 3.1.1)

    Outer loop heuristic:
      amp_proposed = amp_k * (alpha_target / alpha_inv_measured) ** scale_exp
      amp_{k+1}    = damping * amp_proposed + (1 - damping) * amp_k

    Convergence: BOTH targets within tol for the current iteration.
    Geometry (R, r) is HELD CONSTANT at (R_target, r_target) — only the
    amplitude varies.

    Returns trajectory of (amp, alpha_inv, chi_measured, errs) per iter.
    """
    from ave.core.constants import ALPHA_COLD_INV

    alpha_target = float(ALPHA_COLD_INV)
    chi_target = ALPHA * 6.0 / 5.0

    amp_k = float(amp_init)
    history = []  # list of dicts per iteration

    for outer_iter in range(1, max_outer_iter + 1):
        if verbose:
            print(f"\n=== Path C outer iter {outer_iter} ===")
            print(f"  amp = {amp_k:.4e}  (R, r) = ({R_target:.2f}, {r_target:.3f}) "
                  f"[held fixed]")

        result = run_tlm_electron(
            N=N, R=R_target, r=r_target,
            n_steps=n_steps, sample_every=n_steps + 1,
            amplitude=amp_k,
            nonlinear=False, pml_thickness=pml_thickness,
            op3_bond_reflection=True,
            rms_avg_last_n=max(50, n_steps // 3),
            verbose=False,
        )
        R_rms = float(result['R_rms'])
        r_rms = float(result['r_rms'])
        lattice = result['lattice']

        alpha_dict = extract_alpha_inverse(R_rms, r_rms, c=3)
        alpha_inv = alpha_dict['alpha_inv'] if alpha_dict['valid'] else float('nan')

        chi_dict = extract_chirality_measured(lattice, R_major=R_rms or R_target)
        chi_meas = chi_dict['chi_measured']

        conv = convergence_check(alpha_inv, chi_meas,
                                 alpha_target=alpha_target,
                                 chi_target=chi_target,
                                 tol=tol)

        history.append({
            'iter': outer_iter,
            'amp': amp_k,
            'R_rms': R_rms, 'r_rms': r_rms,
            'alpha_inv': alpha_inv,
            'chi_measured': chi_meas,
            'p_meas': chi_dict['p_measured'],
            'q_meas': chi_dict['q_measured'],
            'alpha_err': conv['alpha_err'],
            'chi_err': conv['chi_err'],
            'converged': conv['converged'],
        })

        if verbose:
            print(f"  Extracted: (R,r)=({R_rms:.3f}, {r_rms:.3f}) "
                  f"α⁻¹={alpha_inv:.3f} ({conv['alpha_err']*100:.2f}% err)")
            print(f"  Chirality: p={chi_dict['p_measured']:+.3f} "
                  f"q={chi_dict['q_measured']:+.3f}  "
                  f"χ_meas={chi_meas:+.4e}  χ_target={chi_target:+.4e} "
                  f"({conv['chi_err']*100:.2f}% err)")

        if conv['converged']:
            if verbose:
                print(f"  → CONVERGED at iter {outer_iter}: both errors < {tol*100:.1f}%")
            return {
                'converged': True,
                'iterations': outer_iter,
                'trajectory': history,
                'final_amp': amp_k,
                'final_R': R_rms, 'final_r': r_rms,
                'final_alpha_inv': alpha_inv,
                'final_chi': chi_meas,
            }

        # Adjust amplitude. If alpha_inv is NaN or bad, shrink amp.
        if np.isnan(alpha_inv) or alpha_inv <= 0:
            amp_proposed = amp_k * 0.7
        else:
            ratio = alpha_target / alpha_inv
            amp_proposed = amp_k * (ratio ** scale_exp)

        # Damping for stability
        amp_new = damping * amp_proposed + (1.0 - damping) * amp_k
        # Bound to physical range
        amp_new = max(0.001 * float(V_YIELD), min(0.99 * float(V_SNAP), amp_new))

        if verbose:
            print(f"  Amplitude update: {amp_k:.4e} → {amp_new:.4e}")
        amp_k = amp_new

    if verbose:
        print(f"  → NOT converged within {max_outer_iter} iterations.")
    return {
        'converged': False,
        'iterations': max_outer_iter,
        'trajectory': history,
        'final_amp': amp_k,
        'final_R': history[-1]['R_rms'] if history else None,
        'final_r': history[-1]['r_rms'] if history else None,
        'final_alpha_inv': history[-1]['alpha_inv'] if history else None,
        'final_chi': history[-1]['chi_measured'] if history else None,
    }


def main():
    print("=" * 78)
    print("  L3 Phase-3 — TLM electron-soliton eigenmode (2,3) voltage-wave demo")
    print("=" * 78)

    PHI_SQ = PHI**2
    # 32³ with periodic BCs — no energy leak. op3_bond_reflection=True
    # enables the bond-level impedance mismatch reflection that creates
    # bound-state confinement from the strain-induced Z_eff variation.
    # Amplitude at 0.9 × V_YIELD: core at the Regime II/III boundary per
    # AVE-VirtualMedia/scripts/generate_reflection_profile.py.
    N_grid = 96
    R_target = 24.0
    r_target = R_target / PHI_SQ
    amp = 0.9 * float(V_YIELD)
    print(f"  Golden Torus target ({N_grid}³, periodic BCs): R = {R_target:.2f}, r = {r_target:.3f}, R/r = {PHI_SQ:.3f}")
    print(f"  V_YIELD = {float(V_YIELD):.3e} V; V_SNAP = {float(V_SNAP):.3e} V")
    print(f"  Initial amplitude = {amp:.3e} V  (= 0.9 × V_YIELD, at Regime II/III boundary)")
    print()

    print(f"--- Run 1: Golden Torus init, op3=True, periodic BCs ({N_grid}³) ---")
    result1 = run_tlm_electron(
        N=N_grid, R=R_target, r=r_target,
        n_steps=400, sample_every=50, amplitude=amp,
        nonlinear=False, pml_thickness=0, op3_bond_reflection=True,
    )

    print()
    print(f"--- Run 2: perturbed (R +30%, r -30%), op3=True, periodic BCs ---")
    result2 = run_tlm_electron(
        N=N_grid, R=R_target * 1.3, r=r_target * 0.7,
        n_steps=400, sample_every=50, amplitude=amp,
        nonlinear=False, pml_thickness=0, op3_bond_reflection=True,
    )

    print()
    print("--- Summary ---")
    ALPHA_TARGET = 4 * np.pi**3 + np.pi**2 + np.pi
    for idx, result in enumerate([result1, result2], start=1):
        R_f = float(result['R'][-1])
        r_f = float(result['r'][-1])
        R_rms = float(result['R_rms'])
        r_rms = float(result['r_rms'])
        ratio = R_f / max(r_f, 1e-6)
        ratio_rms = R_rms / max(r_rms, 1e-6)
        E_var = (result['energy'].max() - result['energy'].min()) / result['energy'][0]
        c_extracted = extract_crossing_count_tlm(result['lattice'], R_major=R_f)
        print(f"\n  Run {idx} final:")
        print(f"    Snapshot  (R, r) = ({R_f:.3f}, {r_f:.3f})  R/r = {ratio:.3f}")
        print(f"    Time-RMS  (R, r) = ({R_rms:.3f}, {r_rms:.3f})  R/r = {ratio_rms:.3f}  (target {PHI_SQ:.3f})")
        print(f"    N_crossings extracted = {c_extracted}  (target 3 for electron)")
        print(f"    Energy variation: {E_var*100:.4f}%  (ideal 0.00%)")
        # Use time-averaged (R, r) for α⁻¹ extraction — the standing-wave
        # envelope, not a phase-dependent snapshot.
        c_use = c_extracted if c_extracted > 0 else 3
        alpha = extract_alpha_inverse(R_rms, r_rms, c=c_use)
        if alpha["valid"]:
            print(f"    d (self-avoidance) = {alpha['d']:.3f}  (= 2(R-r))")
            print(f"    Ch 8 ratios:")
            print(f"      (R-r)/d  = {alpha['ratio_self_avoid']:.4f}  (target 0.5000)")
            print(f"      R·r/d^2  = {alpha['ratio_screen']:.4f}  (target 0.2500)")
            print(f"    Multipole decomposition (c={alpha['c']}):")
            print(f"      Lambda_vol  = {alpha['Lambda_vol']:.4f}  (target 4π^3 = {4*np.pi**3:.4f})")
            print(f"      Lambda_surf = {alpha['Lambda_surf']:.4f}  (at c=3 target π^2 = {np.pi**2:.4f})")
            print(f"      Lambda_line = {alpha['Lambda_line']:.4f}  (target π    = {np.pi:.4f})")
            print(f"    α⁻¹ (c-weighted) = {alpha['alpha_inv']:.4f}  (target 137.0363)")
            err_pct = 100 * abs(alpha['alpha_inv'] - ALPHA_TARGET) / ALPHA_TARGET
            print(f"    Deviation from target: {err_pct:.2f}%")
        else:
            print(f"    α⁻¹: invalid (R <= r or r = 0)")

    # ─── Op6 self-consistency loop (Step 3) ──────────────────────────────────
    # Wraps the TLM run in an outer iteration that feeds back extracted (R, r)
    # into the next initialization. If the (2,3) sector has a self-consistent
    # eigenmode, iterations converge regardless of seed within the basin.
    print()
    print("=" * 78)
    print("  Op6 SELF-CONSISTENCY LOOP (iterate on extracted R, r)")
    print("=" * 78)

    for sc_label, R_seed, r_seed in [
        ("from Golden Torus seed", R_target, r_target),
        ("from perturbed seed (+30%/-30%)", R_target * 1.3, r_target * 0.7),
    ]:
        print(f"\n--- Self-consistent {sc_label} ---")
        sc = solve_eigenmode_self_consistent(
            N=N_grid, R_seed=R_seed, r_seed=r_seed, amplitude=amp,
            n_steps=300, sample_every=300, max_iter=6, tol=1e-3, verbose=True,
        )
        print(f"\n  Trajectory:")
        for k, (Rk, rk, ak) in enumerate(sc["trajectory"]):
            ak_str = f"{ak:.3f}" if ak is not None else "--- (seed)"
            print(f"    iter {k}: (R, r) = ({Rk:.3f}, {rk:.3f})  α⁻¹ = {ak_str}")
        print(f"  Converged: {sc['converged']}  iterations: {sc['iterations']}")
        if sc["final_alpha_inv"] is not None:
            err_pct = 100 * abs(sc["final_alpha_inv"] - ALPHA_TARGET) / ALPHA_TARGET
            print(f"  Final α⁻¹ = {sc['final_alpha_inv']:.3f}  (target {ALPHA_TARGET:.3f}; deviation {err_pct:.2f}%)")


if __name__ == "__main__":
    main()
