"""Embed AVE topological particle meshes on vacuum lattice node centers."""

from __future__ import annotations

import pathlib
import sys
from collections.abc import Callable

import numpy as np
from stl import mesh as stl_mesh

from ave.core import chiral_lattice as cl

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "vol_2_subatomic"))
from generate_particle_stl import (  # noqa: E402
    make_alpha_stl,
    make_electron_stl,
    make_muon_stl,
    make_neutron_stl,
    make_proton_borromean_stl,
    make_tau_stl,
)

from generate_vacuum_lattice_stl import lattice_pos_to_mm  # noqa: E402

ParticleFactory = Callable[[], stl_mesh.Mesh]

PARTICLE_ZOO: list[tuple[str, str, ParticleFactory]] = [
    ("electron", "e⁻  0₁ unknot", lambda: make_electron_stl()),
    ("muon", "μ⁻  Cosserat rotation", lambda: make_muon_stl()),
    ("tau", "τ⁻  curvature-twist", lambda: make_tau_stl()),
    ("proton", "p  6³₂ Borromean", lambda: make_proton_borromean_stl()),
    ("neutron", "n  6³₂ ∪ 0₁", lambda: make_neutron_stl()),
    ("alpha", "α  ⁴He tetrahedron", lambda: make_alpha_stl()),
]


def mesh_centroid(mesh: stl_mesh.Mesh) -> np.ndarray:
    return mesh.vectors.reshape(-1, 3).mean(axis=0)


def mesh_max_radius(mesh: stl_mesh.Mesh) -> float:
    c = mesh_centroid(mesh)
    verts = mesh.vectors.reshape(-1, 3)
    return float(np.max(np.linalg.norm(verts - c, axis=1)))


def translate_mesh(mesh: stl_mesh.Mesh, offset: np.ndarray) -> stl_mesh.Mesh:
    out = stl_mesh.Mesh(np.copy(mesh.data))
    out.vectors += offset.reshape(1, 1, 3)
    return out


def scale_mesh_about_centroid(mesh: stl_mesh.Mesh, scale: float) -> stl_mesh.Mesh:
    c = mesh_centroid(mesh)
    out = stl_mesh.Mesh(np.copy(mesh.data))
    out.vectors = (out.vectors - c) * scale + c
    return out


def fit_mesh_to_node(
    mesh: stl_mesh.Mesh,
    center_mm: np.ndarray,
    target_radius_mm: float,
) -> stl_mesh.Mesh:
    extent = mesh_max_radius(mesh)
    scale = target_radius_mm / max(extent, 1e-9)
    fitted = scale_mesh_about_centroid(mesh, scale)
    return translate_mesh(fitted, center_mm - mesh_centroid(fitted))


def pick_spread_interior_nodes(
    net: cl.LatticeNet,
    count: int,
    pos_mm: np.ndarray | None = None,
) -> list[int]:
    """Pick ``count`` interior nodes spread apart (pedagogical particle sites)."""
    if pos_mm is None:
        pos_mm = lattice_pos_to_mm(net)
    mask = net.interior_mask
    if mask is not None and mask.any():
        candidates = list(np.where(mask)[0])
    else:
        candidates = list(range(net.n_nodes))
    center = pos_mm.mean(axis=0)
    candidates.sort(key=lambda u: float(np.linalg.norm(pos_mm[u] - center)))
    if not candidates:
        return []
    seed = candidates[len(candidates) // 2]
    picked = [seed]
    remaining = [u for u in candidates if u != seed]
    while len(picked) < count and remaining:
        best = max(
            remaining,
            key=lambda u: min(float(np.linalg.norm(pos_mm[u] - pos_mm[p])) for p in picked),
        )
        picked.append(best)
        remaining.remove(best)
    return picked[:count]


def embed_particles_on_lattice(
    net: cl.LatticeNet,
    *,
    scale_mm: float,
    lepton_radius_mm: float,
    baryon_radius_mm: float,
    alpha_radius_mm: float,
    resolution_scale: float = 1.0,
) -> tuple[list[stl_mesh.Mesh], list[dict]]:
    """Place the six canonical particles on spread interior lattice nodes."""
    pos_mm = lattice_pos_to_mm(net)
    nodes = pick_spread_interior_nodes(net, len(PARTICLE_ZOO), pos_mm)
    meshes: list[stl_mesh.Mesh] = []
    manifest: list[dict] = []

    for (key, label, factory), node_idx in zip(PARTICLE_ZOO, nodes):
        raw = factory()
        if key == "alpha":
            target = alpha_radius_mm
        elif key in ("proton", "neutron"):
            target = baryon_radius_mm
        else:
            target = lepton_radius_mm
        placed = fit_mesh_to_node(raw, pos_mm[node_idx], target)
        meshes.append(placed)
        manifest.append({
            "particle": key,
            "label": label,
            "node": int(node_idx),
            "center_mm": pos_mm[node_idx].tolist(),
            "target_radius_mm": target,
        })
    return meshes, manifest
