#!/usr/bin/env python3
"""
3D-Printable Particle Models — STL Export
==========================================

Generates watertight STL mesh files for every fundamental particle
topology in the AVE framework, at physically correct relative scales.

Particle inventory:
  LEPTONS (Unknot variants):
    1. Electron  — smooth 0₁ unknot ring
    2. Muon      — 0₁ unknot with Cosserat torsional twist (rotation sector)
    3. Tau       — 0₁ unknot with curvature undulation (bending sector)

  NEUTRINOS (Screw dislocations):
    4. ν₁ (c=5) — 5-pitch helical coil
    5. ν₂ (c=7) — 7-pitch helical coil
    6. ν₃ (c=9) — 9-pitch helical coil

  BARYONS (Torus knots):
    7.  Proton    — (2,5) cinquefoil
    8.  Δ(1232)   — (2,7) septafoil
    9.  Δ(1620)   — (2,9) torus knot
    10. Δ(1950)   — (2,11) torus knot
    11. N(2250)   — (2,13) torus knot
    12. Proton (internal) — Borromean 6³₂ link of three (2,5) knots

Scale convention: 1 ℓ_node = 10 mm in the STL.

Output: assets/3d_models/*.stl

Usage:
    cd ..
    PYTHONPATH=src python src/scripts/vol_2_subatomic/generate_particle_stl.py
"""

import os
import pathlib

import numpy as np
from stl import mesh as stl_mesh

# Engine imports — all physics constants from the single source of truth
from ave.core.constants import KAPPA_FS, P_C
from ave.topological.borromean import FundamentalTopologies

# ═══════════════════════════════════════════════════════════════════
# Scale Convention
# ═══════════════════════════════════════════════════════════════════
# 1 ℓ_node = 10 mm in STL coordinates
MM_PER_L_NODE = 10.0

# ─── RENDERING vs DERIVED parameters ─────────────────────────────
# Parameters marked [DERIVED] come from AVE axioms / engine constants.
# Parameters marked [RENDERING] are visual choices for printability
# that do not affect the mathematical topology or scale ratios.
#
# THE ELECTRON SCALE PROBLEM:
#   The physical electron radius is R = ℓ_node/(2π) ≈ 0.16 ℓ_node.
#   At 10 mm/ℓ_node, this is 1.6 mm diameter — too small to 3D print.
#   Baryons are ~5 ℓ_node, so the true electron:proton ratio is ~1:31.
#   We apply a visual magnification to make leptons printable.
#   The RELATIVE baryon scale ratios (5/c) are exact.
LEPTON_VISUAL_SCALE = 6.0  # [RENDERING] Magnify leptons 6× for printability

# ═══════════════════════════════════════════════════════════════════
# Mesh Generation Core: Frenet-Serret Tube Sweeper
# ═══════════════════════════════════════════════════════════════════


def compute_frenet_frame(curve: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Compute the Frenet-Serret frame (T, N, B) along a 3D curve.

    Uses central differences for the tangent and a robust fallback
    for degenerate normals (straight segments).

    Args:
        curve: [M, 3] array of 3D coordinates along the curve.

    Returns:
        T, N, B: each [M, 3] arrays of unit tangent, normal, binormal vectors.
    """
    # M = len(curve)  # bulk lint fixup pass

    # Tangent via central differences (wrap for closed curves)
    T = np.zeros_like(curve)
    T[1:-1] = curve[2:] - curve[:-2]
    T[0] = curve[1] - curve[-2]  # wrap
    T[-1] = curve[1] - curve[-2]  # wrap

    # Normalise tangent
    T_norm = np.linalg.norm(T, axis=1, keepdims=True)
    T_norm = np.maximum(T_norm, 1e-12)
    T = T / T_norm

    # Normal via second derivative
    dT = np.zeros_like(curve)
    dT[1:-1] = T[2:] - T[:-2]
    dT[0] = T[1] - T[-2]
    dT[-1] = T[1] - T[-2]

    # Remove tangential component (Gram-Schmidt)
    proj = np.sum(dT * T, axis=1, keepdims=True)
    N = dT - proj * T
    N_norm = np.linalg.norm(N, axis=1, keepdims=True)

    # Fallback for degenerate normals: use perpendicular to T
    degenerate = N_norm.flatten() < 1e-8
    if np.any(degenerate):
        # Pick arbitrary perpendicular vector
        for i in np.where(degenerate)[0]:
            # Pick axis least aligned with T[i]
            abs_t = np.abs(T[i])
            min_axis = np.argmin(abs_t)
            perp = np.zeros(3)
            perp[min_axis] = 1.0
            n = perp - T[i] * T[i, min_axis]
            n = n / np.linalg.norm(n)
            N[i] = n
            N_norm[i] = 1.0

    N_norm = np.maximum(N_norm, 1e-12)
    N = N / N_norm

    # Binormal
    B = np.cross(T, N)
    B_norm = np.linalg.norm(B, axis=1, keepdims=True)
    B_norm = np.maximum(B_norm, 1e-12)
    B = B / B_norm

    return T, N, B


def sweep_tube(
    curve: np.ndarray,
    tube_radius: float,
    n_radial: int = 24,
    twist_turns: float = 0,
    curvature_amplitude: float = 0.0,
    curvature_lobes: int = 0,
) -> stl_mesh.Mesh:
    """
    Generate a watertight triangle mesh by sweeping a circular cross-section
    along a 3D curve using the Frenet-Serret frame.

    Args:
        curve: [M, 3] array of 3D centerline coordinates.
        tube_radius: Radius of the circular cross-section.
        n_radial: Number of segments around the cross-section.
        twist_turns: Number of full torsional rotations of the cross-section
                     along the curve (for muon Cosserat twist).
        curvature_amplitude: Amplitude of curvature undulation applied to
                             tube radius (for tau Cosserat bending).
        curvature_lobes: Number of curvature lobes per revolution.

    Returns:
        stl.mesh.Mesh: watertight STL mesh object.
    """
    M = len(curve)
    T, N, B = compute_frenet_frame(curve)

    # Generate surface vertices
    phi = np.linspace(0, 2 * np.pi, n_radial, endpoint=False)
    vertices = np.zeros((M, n_radial, 3))

    for i in range(M):
        frac = i / max(M - 1, 1)  # 0..1 along curve

        # Torsional twist: rotate cross-section by twist_turns full rotations
        twist_angle = 2 * np.pi * twist_turns * frac

        # Curvature undulation: modulate tube radius
        if curvature_amplitude > 0 and curvature_lobes > 0:
            r_mod = tube_radius * (1.0 + curvature_amplitude * np.sin(2 * np.pi * curvature_lobes * frac))
        else:
            r_mod = tube_radius

        for j in range(n_radial):
            angle = phi[j] + twist_angle
            offset = r_mod * (np.cos(angle) * N[i] + np.sin(angle) * B[i])
            vertices[i, j] = curve[i] + offset

    # Triangulate: connect adjacent cross-sections with quads → 2 triangles each
    n_faces = 2 * M * n_radial
    faces = np.zeros(n_faces, dtype=stl_mesh.Mesh.dtype)

    face_idx = 0
    for i in range(M):
        i_next = (i + 1) % M  # wrap for closed curves
        for j in range(n_radial):
            j_next = (j + 1) % n_radial

            v0 = vertices[i, j]
            v1 = vertices[i, j_next]
            v2 = vertices[i_next, j_next]
            v3 = vertices[i_next, j]

            # Triangle 1: v0, v1, v2
            faces["vectors"][face_idx] = [v0, v1, v2]
            face_idx += 1
            # Triangle 2: v0, v2, v3
            faces["vectors"][face_idx] = [v0, v2, v3]
            face_idx += 1

    result = stl_mesh.Mesh(faces)
    return result


def sweep_tube_open(curve: np.ndarray, tube_radius: float, n_radial: int = 24, cap: bool = True) -> stl_mesh.Mesh:
    """
    Generate a watertight triangle mesh for an OPEN curve (not closed loop).
    Used for neutrino screw dislocation helices.

    Args:
        curve: [M, 3] array of 3D centerline coordinates.
        tube_radius: Radius of the tube cross-section.
        n_radial: Number of segments around the cross-section.
        cap: Whether to add end caps.

    Returns:
        stl.mesh.Mesh: watertight STL mesh object.
    """
    M = len(curve)

    # Compute tangent (no wrap for open curves)
    T = np.zeros_like(curve)
    T[0] = curve[1] - curve[0]
    T[-1] = curve[-1] - curve[-2]
    T[1:-1] = curve[2:] - curve[:-2]
    T_norm = np.linalg.norm(T, axis=1, keepdims=True)
    T_norm = np.maximum(T_norm, 1e-12)
    T = T / T_norm

    # Normal via second derivative (open)
    dT = np.zeros_like(curve)
    dT[0] = T[1] - T[0]
    dT[-1] = T[-1] - T[-2]
    dT[1:-1] = T[2:] - T[:-2]
    proj = np.sum(dT * T, axis=1, keepdims=True)
    N = dT - proj * T
    N_norm = np.linalg.norm(N, axis=1, keepdims=True)

    # Fallback for degenerate normals
    degenerate = N_norm.flatten() < 1e-8
    if np.any(degenerate):
        for i in np.where(degenerate)[0]:
            abs_t = np.abs(T[i])
            min_axis = np.argmin(abs_t)
            perp = np.zeros(3)
            perp[min_axis] = 1.0
            n = perp - T[i] * T[i, min_axis]
            n = n / (np.linalg.norm(n) + 1e-30)
            N[i] = n
            N_norm[i] = 1.0
    N_norm = np.maximum(N_norm, 1e-12)
    N = N / N_norm

    B = np.cross(T, N)
    B_norm = np.linalg.norm(B, axis=1, keepdims=True)
    B_norm = np.maximum(B_norm, 1e-12)
    B = B / B_norm

    # Generate surface
    phi = np.linspace(0, 2 * np.pi, n_radial, endpoint=False)
    vertices = np.zeros((M, n_radial, 3))
    for i in range(M):
        for j in range(n_radial):
            offset = tube_radius * (np.cos(phi[j]) * N[i] + np.sin(phi[j]) * B[i])
            vertices[i, j] = curve[i] + offset

    # Count faces: M-1 quads × n_radial × 2 triangles + 2 caps
    n_tube_faces = 2 * (M - 1) * n_radial
    n_cap_faces = 2 * (n_radial - 2) if cap else 0
    total_faces = n_tube_faces + n_cap_faces
    faces = np.zeros(total_faces, dtype=stl_mesh.Mesh.dtype)

    face_idx = 0
    for i in range(M - 1):
        for j in range(n_radial):
            j_next = (j + 1) % n_radial
            v0 = vertices[i, j]
            v1 = vertices[i, j_next]
            v2 = vertices[i + 1, j_next]
            v3 = vertices[i + 1, j]
            faces["vectors"][face_idx] = [v0, v1, v2]
            face_idx += 1
            faces["vectors"][face_idx] = [v0, v2, v3]
            face_idx += 1

    # End caps (fan triangulation)
    if cap:
        # Start cap
        # center_start = curve[0]  # bulk lint fixup pass
        for j in range(n_radial - 2):
            faces["vectors"][face_idx] = [vertices[0, 0], vertices[0, j + 2], vertices[0, j + 1]]
            face_idx += 1
        # End cap
        for j in range(n_radial - 2):
            faces["vectors"][face_idx] = [vertices[-1, 0], vertices[-1, j + 1], vertices[-1, j + 2]]
            face_idx += 1

    result = stl_mesh.Mesh(faces[:face_idx])
    return result


# ═══════════════════════════════════════════════════════════════════
# Particle Model Generators
# ═══════════════════════════════════════════════════════════════════


def make_baryon_stl(
    q: int, scale_mm: float = MM_PER_L_NODE, n_radial: int = 24, resolution: int = 2000
) -> stl_mesh.Mesh:
    """
    Generate a (2,q) torus knot STL mesh for a baryon.

    DERIVED from engine:
      Major radius R = r_opt = κ_FS / c          [DERIVED]
      Tube orbit radius = r_opt / (2π)            [DERIVED] (ropelength)

    Args:
        q: Crossing number (odd, ≥ 3).
        scale_mm: mm per ℓ_node.

    Returns:
        stl.mesh.Mesh
    """
    r_opt = KAPPA_FS / q  # [DERIVED] confinement radius in ℓ_node
    R_mm = r_opt * scale_mm  # major radius in mm
    r_tube_physical = R_mm / (2 * np.pi)  # [DERIVED] tube orbit from ropelength
    tube_r = r_tube_physical * 0.5  # [RENDERING] 50% of physical for printability

    # Torus minor radius: sets the amplitude of the knot's excursion off
    # the torus center plane.  For visual clarity, set to 35% of major radius.
    torus_minor = R_mm * 0.35  # [RENDERING] knot amplitude scaling

    # Generate centerline
    curve = FundamentalTopologies.generate_torus_knot_2q(q=q, R=R_mm, r=torus_minor, resolution=resolution)

    return sweep_tube(curve, tube_r, n_radial=n_radial)


def make_electron_stl(scale_mm: float = MM_PER_L_NODE, n_radial: int = 24, resolution: int = 1000) -> stl_mesh.Mesh:
    """
    Generate the electron unknot: a smooth torus ring.

    DERIVED from LIVING_REFERENCE.md:
      Circumference = ℓ_node  →  R_major = ℓ_node/(2π)   [DERIVED]
      Tube radius = ℓ_node/(2π)   (ropelength = 2π)       [DERIVED]

    Note: R_major = tube_radius for the minimal unknot, giving a
    "fat torus" where the hole just closes.  This is the tightest
    possible unknot configuration (ropelength = 2π).

    Visual magnification applied for printability (see LEPTON_VISUAL_SCALE).
    """
    # Physical dimensions (in ℓ_node)
    R_physical = 1.0 / (2 * np.pi)  # [DERIVED] ℓ_node/(2π)
    tube_r_physical = 1.0 / (2 * np.pi)  # [DERIVED] ℓ_node/(2π)

    # Apply visual scaling for printability
    R_mm = R_physical * scale_mm * LEPTON_VISUAL_SCALE
    tube_r = tube_r_physical * scale_mm * LEPTON_VISUAL_SCALE

    curve = FundamentalTopologies.generate_unknot_0_1(radius=R_mm, resolution=resolution)

    return sweep_tube(curve, tube_r, n_radial=n_radial)


def make_muon_stl(scale_mm: float = MM_PER_L_NODE, n_radial: int = 24, resolution: int = 1000) -> stl_mesh.Mesh:
    """
    Generate the muon: unknot with Cosserat torsional twist.

    The muon is the rotation sector of the Cosserat Lagrangian:
    same unknot topology, but the tube cross-section absorbs
    one quantum of torsional coupling (α × √(3/7)).

    DERIVED: Same R and tube_r as electron (0₁ unknot)        [DERIVED]

    TWIST DERIVATION (from Perpendicular Axis Theorem):
      The tube cross-section rotates by √(3/7) turns as it traverses
      the ring circumference (≈ 0.655 turns = 236°).

      √(3/7) is the torsion-shear projection factor from the PAT:
        J = 2I  (Perpendicular Axis Theorem for cylindrical flux tube)
        ν_vac = 2/7  (Poisson ratio → compliance splitting)
        G_torsion/G_shear = ν/(1+ν) = (2/7)/(9/7) = 2/9
        Projection of shear onto torsion: sin(θ_PAT) = √(3/7)

      This is the SAME factor that appears in the mass formula:
        m_μ = m_e / (α × √(3/7))
      where α couples the dielectric sector and √(3/7) projects
      the translational energy onto the rotational DOF.          [DERIVED]
    """
    R_physical = 1.0 / (2 * np.pi)
    tube_r_physical = 1.0 / (2 * np.pi)
    R_mm = R_physical * scale_mm * LEPTON_VISUAL_SCALE
    tube_r = tube_r_physical * scale_mm * LEPTON_VISUAL_SCALE

    curve = FundamentalTopologies.generate_unknot_0_1(radius=R_mm, resolution=resolution)

    # Torsional twist = √(3/7) turns per revolution            [DERIVED]
    # From the PAT torsion-shear projection with ν_vac = 2/7
    twist_turns_derived = np.sqrt(3.0 / 7.0)  # ≈ 0.6547 turns = 236°
    return sweep_tube(curve, tube_r, n_radial=n_radial, twist_turns=twist_turns_derived)


def make_tau_stl(scale_mm: float = MM_PER_L_NODE, n_radial: int = 24, resolution: int = 1000) -> stl_mesh.Mesh:
    """
    Generate the tau: unknot with curvature-twist undulation.

    The tau is the curvature-twist sector of the Cosserat Lagrangian:
    same unknot topology, but with bending deformation at the maximum
    energy scale before packing saturation.

    DERIVED: Same R and tube_r as electron (0₁ unknot)        [DERIVED]
    curvature_lobes = 7: from ν_vac = 2/7 (7 compliance modes) [DERIVED]
    curvature_amplitude = P_C ≈ 0.18: packing fraction         [DERIVED]
      The maximum bending before saturation (Axiom 4).
    """
    R_physical = 1.0 / (2 * np.pi)
    tube_r_physical = 1.0 / (2 * np.pi)
    R_mm = R_physical * scale_mm * LEPTON_VISUAL_SCALE
    tube_r = tube_r_physical * scale_mm * LEPTON_VISUAL_SCALE

    curve = FundamentalTopologies.generate_unknot_0_1(radius=R_mm, resolution=resolution)

    # 7 curvature lobes from the 7-mode compliance manifold    [DERIVED]
    # Amplitude = p_c ≈ 0.18 = maximum pre-saturation bending  [DERIVED]
    return sweep_tube(curve, tube_r, n_radial=n_radial, curvature_amplitude=P_C, curvature_lobes=7)


def make_neutrino_stl(
    crossing_number: int, scale_mm: float = MM_PER_L_NODE, n_radial: int = 16, resolution: int = 2000
) -> stl_mesh.Mesh:
    """
    Generate a neutrino screw dislocation: open helical coil.

    The neutrino is a pure torsional (screw) defect with 4π internal
    phase twist and zero self-crossings (C=0).  The baryon partner's
    crossing number c sets the helical pitch (mass ∝ 5/c).

    DERIVED: pitch_count = baryon partner crossing number      [DERIVED]
      ν₁ ↔ proton (2,5),  ν₂ ↔ Δ(1232) (2,7),  ν₃ ↔ Δ(1620) (2,9)

    Note: Neutrinos are non-localized screw dislocations with no
    well-defined spatial radius. The helix dimensions below are
    rendering choices for printability.

    Args:
        crossing_number: Baryon partner crossing number (5, 7, or 9).
    """
    helix_radius = 0.5 * scale_mm  # [RENDERING] 5 mm coil radius
    helix_length = 2.0 * scale_mm  # [RENDERING] 20 mm total length
    tube_r = 0.5  # [RENDERING] 0.5 mm tube diameter

    curve = FundamentalTopologies.generate_screw_dislocation(
        pitch_count=crossing_number,  # [DERIVED] baryon partner c
        length=helix_length,
        radius=helix_radius,
        resolution=resolution,
    )

    return sweep_tube_open(curve, tube_r, n_radial=n_radial, cap=True)


def make_proton_borromean_stl(
    scale_mm: float = MM_PER_L_NODE, n_radial: int = 20, resolution: int = 1000
) -> stl_mesh.Mesh:
    """
    Generate the proton internal structure: Borromean 6³₂ link.

    Three mutually interlocking rings representing the three
    independent flux loops of the proton (V_toroidal_halo = 2).

    DERIVED: r_opt = κ_FS/5 for proton (c=5)                  [DERIVED]
    eccentricity = 1.6: pre-existing borromean.py parameter    [RENDERING]
    tube_r factor 0.35: thinner tubes for visual clarity       [RENDERING]
    """
    r_opt = KAPPA_FS / 5  # [DERIVED] proton confinement radius
    R_mm = r_opt * scale_mm
    r_tube_physical = R_mm / (2 * np.pi)  # [DERIVED] ropelength tube radius
    tube_r = r_tube_physical * 0.35  # [RENDERING] thinner for visual clarity

    # Generate the three Borromean rings
    rings = FundamentalTopologies.generate_borromean_6_3_2(
        radius=R_mm, eccentricity=1.6, resolution=resolution  # [RENDERING] pre-existing parameter
    )

    # Sweep tubes around each ring and combine
    all_data = []
    for ring in rings:
        ring_mesh = sweep_tube(ring, tube_r, n_radial=n_radial)
        all_data.append(ring_mesh.data)

    combined = np.concatenate(all_data)
    combined_mesh = stl_mesh.Mesh(combined)
    return combined_mesh


# ═══════════════════════════════════════════════════════════════════
# Main Script
# ═══════════════════════════════════════════════════════════════════


def main() -> None:
    project_root = pathlib.Path(__file__).parent.parent.parent.parent
    output_dir = project_root / "assets" / "3d_models"
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("  AVE 3D-Printable Particle Models — STL Generator")
    print("=" * 70)
    print(f"  Scale: 1 ℓ_node = {MM_PER_L_NODE} mm")
    print(f"  κ_FS = {KAPPA_FS:.4f}")
    print(f"  Output: {output_dir}")
    print()

    models = []

    # ── LEPTONS ──
    print("  LEPTONS (Unknot Variants)")
    print("  " + "─" * 50)

    print("    Generating electron (smooth 0₁ unknot)...", end="", flush=True)
    m = make_electron_stl()
    path = output_dir / "electron_unknot.stl"
    m.save(str(path))
    models.append(("Electron (e⁻)", "0₁ unknot", path))
    print(f" ✓ [{os.path.getsize(path) / 1024:.0f} KB]")

    print("    Generating muon (twisted unknot)...", end="", flush=True)
    m = make_muon_stl()
    path = output_dir / "muon_twisted_unknot.stl"
    m.save(str(path))
    models.append(("Muon (μ⁻)", "0₁ twisted", path))
    print(f" ✓ [{os.path.getsize(path) / 1024:.0f} KB]")

    print("    Generating tau (curvature unknot)...", end="", flush=True)
    m = make_tau_stl()
    path = output_dir / "tau_curvature_unknot.stl"
    m.save(str(path))
    models.append(("Tau (τ⁻)", "0₁ curvature", path))
    print(f" ✓ [{os.path.getsize(path) / 1024:.0f} KB]")

    print()

    # ── NEUTRINOS ──
    print("  NEUTRINOS (Screw Dislocations)")
    print("  " + "─" * 50)

    neutrino_data = [
        (5, "ν₁", "neutrino_1_c5.stl"),
        (7, "ν₂", "neutrino_2_c7.stl"),
        (9, "ν₃", "neutrino_3_c9.stl"),
    ]
    for c, name, fname in neutrino_data:
        print(f"    Generating {name} (c={c} helix)...", end="", flush=True)
        m = make_neutrino_stl(c)
        path = output_dir / fname
        m.save(str(path))
        models.append((f"{name} (c={c})", "screw", path))
        print(f" ✓ [{os.path.getsize(path) / 1024:.0f} KB]")

    print()

    # ── BARYONS ──
    print("  BARYONS (Torus Knots)")
    print("  " + "─" * 50)

    baryon_data = [
        (5, "Proton (p)", "proton_2_5.stl"),
        (7, "Δ(1232)", "delta1232_2_7.stl"),
        (9, "Δ(1620)", "delta1620_2_9.stl"),
        (11, "Δ(1950)", "delta1950_2_11.stl"),
        (13, "N(2250)", "n2250_2_13.stl"),
    ]
    for c, name, fname in baryon_data:
        r_opt = KAPPA_FS / c
        R_mm = r_opt * MM_PER_L_NODE
        print(
            f"    Generating {name} (2,{c}) " f"r_opt={r_opt:.2f} ℓ_node = {R_mm:.0f}mm...",
            end="",
            flush=True,
        )
        m = make_baryon_stl(c)
        path = output_dir / fname
        m.save(str(path))
        models.append((f"{name} (2,{c})", "torus knot", path))
        print(f" ✓ [{os.path.getsize(path) / 1024:.0f} KB]")

    print()

    # ── BORROMEAN PROTON ──
    print("  PROTON INTERNAL STRUCTURE")
    print("  " + "─" * 50)
    print("    Generating Borromean 6³₂ link...", end="", flush=True)
    m = make_proton_borromean_stl()
    path = output_dir / "proton_borromean.stl"
    m.save(str(path))
    models.append(("Proton (Borromean)", "6³₂ link", path))
    print(f" ✓ [{os.path.getsize(path) / 1024:.0f} KB]")

    print()
    print("=" * 70)
    print(f"  Generated {len(models)} STL files:")
    for name, topo, path in models:
        size_kb = os.path.getsize(path) / 1024
        print(f"    {name:25s}  {topo:15s}  {size_kb:6.0f} KB  {path.name}")
    print("=" * 70)


if __name__ == "__main__":
    main()
