#!/usr/bin/env python3
r"""Chiral orbital holonomy diagnostic — does a loop orbiting a host K4 node
accumulate a half-twist (SU(2) holonomy = pi) per orbit?

STANDALONE GEOMETRIC DIAGNOSTIC (no genesis sim, no engine import beyond the
canonical port-vector constants). Tests a specific, falsifiable claim:

    A loop orbits ONE host K4 node (the host = the loop's axis). The loop body
    is interstitial (Meissner-expelled, radius r). The host's K4 neighbours set
    the loop's preferred orientation (the "tension"). As the loop orbits the
    host (azimuth 0 -> 2*pi), its frame is parallel-transported in the neighbour
    field. CLAIM: the SU(2) holonomy per orbit = pi (a half-twist) -> 720 deg to
    return -> spin-1/2 emerges geometrically.

METHOD (substrate-native: this is HOLONOMY / parallel transport, NOT energy
minimisation):

  * Canonical chiral K4 geometry. The host's four tetrahedral neighbours sit
    along the canonical port vectors
        p0 = (+1,+1,+1)  p1 = (+1,-1,-1)  p2 = (-1,+1,-1)  p3 = (-1,-1,+1)
    (src/ave/core/k4_tlm.py:359-362 _connect_all A->B port directions; the same
    basis used in manuscript/ave-kb/.../k4-rotation-group.md, rotation group
    T = A4, double cover 2T in SU(2): a 2*pi SO(3) rotation lifts to -I).
    Port handedness (k4_tlm.py:542 get_helicity_density): ports {0,2} are
    right-handed, {1,3} left-handed.

  * The loop's preferred orientation at azimuth phi is the rotation R(phi) in
    SO(3) that best-aligns the canonical reference tetrahedron {p_j} to the
    bond directions {b_j(phi)} *as seen from the orbiting loop* (Wahba/Kabsch
    attitude from vector observations). This is "the orientation set by the
    local neighbour directions" with no free parameter and no energy functional.

  * Parallel transport = continuous lift of R(phi) in SO(3) to q(phi) in SU(2)
    (sign chosen to stay continuous). The frame returns geometrically after one
    orbit (R(2pi) = R(0)); the SU(2) lift returns to +q(0) (holonomy 0, no
    half-twist) or -q(0) (holonomy pi, half-twist = spin-1/2). The +/- sign is a
    Z2 homotopy invariant (pi_1(SO(3)) = Z2) -> topological if robust.

  * Sweeps over orbit radius r, orbit-plane normal, and a chirality knob eps
    (handedness weighting of the Kabsch alignment) test whether any pi is
    TOPOLOGICAL (path-independent) or TUNED.

  * Projected real-space path (orbit + accumulated twist) -> measured winding
    numbers (is it a (2,3) torus knot?).

Verdict classes (consistency-vs-emergence: this is an EMERGENCE test):
  (I)   robust topological pi  -> spin-1/2 emerges geometrically.
  (II)  pi only for tuned r/path -> suggestive, not topological.
  (III) not pi -> mechanism wrong; report the actual value + implication.

Run:  python3 src/scripts/vol_1_foundations/chiral_orbital_holonomy.py
Outputs: console summary + PNG visualisation next to this script's output dir.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field

import numpy as np

# ---------------------------------------------------------------------------
# Canonical K4 geometry (do NOT invent: mirror of k4_tlm.py:359-362, :542)
# ---------------------------------------------------------------------------
PORT_VECTORS = np.array(
    [
        [+1.0, +1.0, +1.0],  # port 0  (right-handed, k4_tlm.py:542)
        [+1.0, -1.0, -1.0],  # port 1  (left-handed)
        [-1.0, +1.0, -1.0],  # port 2  (right-handed)
        [-1.0, -1.0, +1.0],  # port 3  (left-handed)
    ]
)
# helicity handedness sign s_j: +1 right-handed (ports 0,2), -1 left-handed (1,3)
PORT_HANDEDNESS = np.array([+1.0, -1.0, +1.0, -1.0])

PORT_UNIT = PORT_VECTORS / np.linalg.norm(PORT_VECTORS, axis=1, keepdims=True)


# ---------------------------------------------------------------------------
# SO(3) <-> SU(2) (unit quaternion) helpers
# ---------------------------------------------------------------------------
def rotation_to_quaternion(R: np.ndarray) -> np.ndarray:
    """Return a unit quaternion (w,x,y,z) for rotation matrix R (w >= 0 branch)."""
    m = R
    tr = np.trace(m)
    if tr > 0.0:
        s = np.sqrt(tr + 1.0) * 2.0
        w = 0.25 * s
        x = (m[2, 1] - m[1, 2]) / s
        y = (m[0, 2] - m[2, 0]) / s
        z = (m[1, 0] - m[0, 1]) / s
    elif (m[0, 0] > m[1, 1]) and (m[0, 0] > m[2, 2]):
        s = np.sqrt(1.0 + m[0, 0] - m[1, 1] - m[2, 2]) * 2.0
        w = (m[2, 1] - m[1, 2]) / s
        x = 0.25 * s
        y = (m[0, 1] + m[1, 0]) / s
        z = (m[0, 2] + m[2, 0]) / s
    elif m[1, 1] > m[2, 2]:
        s = np.sqrt(1.0 + m[1, 1] - m[0, 0] - m[2, 2]) * 2.0
        w = (m[0, 2] - m[2, 0]) / s
        x = (m[0, 1] + m[1, 0]) / s
        y = 0.25 * s
        z = (m[1, 2] + m[2, 1]) / s
    else:
        s = np.sqrt(1.0 + m[2, 2] - m[0, 0] - m[1, 1]) * 2.0
        w = (m[1, 0] - m[0, 1]) / s
        x = (m[0, 2] + m[2, 0]) / s
        y = (m[1, 2] + m[2, 1]) / s
        z = 0.25 * s
    q = np.array([w, x, y, z])
    q /= np.linalg.norm(q)
    if q[0] < 0:
        q = -q
    return q


def wahba_rotation(ref_unit: np.ndarray, obs_unit: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """Solve Wahba's problem: R minimising sum_j w_j |R ref_j - obs_j|^2.

    ref_unit, obs_unit: (4,3) unit direction sets. Returns a proper rotation R.
    This is the substrate-native "preferred orientation set by neighbour
    directions" with no energy functional and no free parameter (weights encode
    the optional handedness anisotropy only).
    """
    B = (weights[:, None, None] * obs_unit[:, :, None] * ref_unit[:, None, :]).sum(axis=0)
    U, _, Vt = np.linalg.svd(B)
    d = np.sign(np.linalg.det(U @ Vt))
    D = np.diag([1.0, 1.0, d])
    return U @ D @ Vt


# ---------------------------------------------------------------------------
# Orbit geometry
# ---------------------------------------------------------------------------
def orbit_plane_basis(normal: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return two orthonormal vectors spanning the plane with the given normal."""
    n = normal / np.linalg.norm(normal)
    seed = np.array([1.0, 0.0, 0.0]) if abs(n[0]) < 0.9 else np.array([0.0, 1.0, 0.0])
    u = seed - np.dot(seed, n) * n
    u /= np.linalg.norm(u)
    v = np.cross(n, u)
    return u, v


@dataclass
class HolonomyResult:
    r: float
    plane_normal: tuple[float, float, float]
    eps: float
    return_sign: int  # +1 -> +I (no half-twist); -1 -> -I (half-twist, pi)
    signed_dot_one: float  # dot(q(2pi), q(0)); -1 clean half-twist, +1 clean no-twist
    double_cover_ok: bool  # q(4pi) == +q(0) within tol
    solid_angle_zaxis: float  # geometric (Berry) solid angle swept by frame z-axis
    min_align_gap: float  # smallest SVD singular-value gap along path (degeneracy proximity)
    max_step_jump: float  # max angle (rad) between consecutive lifted quaternions
    closure_error: float  # ||R(2pi) - R(0)||_F  (should be ~0 if the loop truly closes)


def compute_holonomy(
    r: float,
    plane_normal: np.ndarray,
    eps: float = 0.0,
    bond_length: float = float(np.sqrt(3.0)),
    n_steps: int = 2048,
    n_orbits: int = 2,
) -> HolonomyResult:
    """Parallel-transport the loop frame around n_orbits orbits; return holonomy.

    bond_length: |host -> neighbour|. Default sqrt(3) places the four neighbours
    exactly at the cube corners (+-1,+-1,+-1) (port vectors at unit lattice
    pitch). r is in the same units; the interstitial loop orbits at radius r.
    eps: handedness weighting; w_j = 1 + eps*s_j (eps=0 -> achiral regular
    tetrahedron control).
    """
    u, v = orbit_plane_basis(plane_normal)
    neighbours = bond_length * PORT_UNIT  # (4,3) absolute neighbour positions
    weights = 1.0 + eps * PORT_HANDEDNESS

    phis = np.linspace(0.0, 2.0 * np.pi * n_orbits, n_steps * n_orbits, endpoint=True)

    quats = np.zeros((phis.size, 4))
    zaxis = np.zeros((phis.size, 3))
    rots = np.zeros((phis.size, 3, 3))
    min_gap = np.inf
    max_jump = 0.0
    prev_q = None
    for i, phi in enumerate(phis):
        p = r * (np.cos(phi) * u + np.sin(phi) * v)  # loop centre, host at origin
        bonds = neighbours - p
        bonds_unit = bonds / np.linalg.norm(bonds, axis=1, keepdims=True)

        # Wahba alignment ref {p_j} -> obs {b_j(phi)}
        B = (weights[:, None, None] * bonds_unit[:, :, None] * PORT_UNIT[:, None, :]).sum(axis=0)
        U, S, Vt = np.linalg.svd(B)
        d = np.sign(np.linalg.det(U @ Vt))
        R = U @ np.diag([1.0, 1.0, d]) @ Vt
        min_gap = min(min_gap, S[1] - S[2])  # proximity to alignment degeneracy

        q = rotation_to_quaternion(R)
        if prev_q is not None:
            if np.dot(q, prev_q) < 0.0:
                q = -q  # continuous lift (parallel transport of the SU(2) sign)
            # step jump = geodesic angle between consecutive lifted quaternions
            jump = 2.0 * np.arccos(min(1.0, abs(float(np.dot(q, prev_q)))))
            max_jump = max(max_jump, jump)
        quats[i] = q
        prev_q = q
        zaxis[i] = R[:, 2]  # frame z-axis (the loop's transported spin axis proxy)
        rots[i] = R

    # one-orbit return: compare q at phi=2pi to q at phi=0
    idx_one = n_steps  # index of phi = 2*pi (since n_steps points per orbit)
    q0 = quats[0]
    q_one = quats[idx_one] if idx_one < phis.size else quats[-1]
    dot_one = float(np.dot(q_one, q0))
    return_sign = 1 if dot_one > 0 else -1

    # closure: does the SO(3) frame truly return after one orbit? (||R(2pi)-R(0)||)
    closure_err = float(np.linalg.norm(rots[idx_one] - rots[0])) if idx_one < phis.size else float("nan")

    # double-cover check: q at phi=4pi should equal +q0
    q_two = quats[-1]
    double_cover_ok = bool(np.dot(q_two, q0) > 0.0)

    solid = solid_angle(zaxis[: idx_one + 1])

    return HolonomyResult(
        r=r,
        plane_normal=tuple(float(x) for x in (plane_normal / np.linalg.norm(plane_normal))),
        eps=eps,
        return_sign=return_sign,
        signed_dot_one=dot_one,
        double_cover_ok=double_cover_ok,
        solid_angle_zaxis=float(solid),
        min_align_gap=float(min_gap),
        max_step_jump=float(max_jump),
        closure_error=closure_err,
    )


def locate_degeneracy(
    r: float, eps: float = 0.6, bond_length: float = float(np.sqrt(3.0)), n: int = 120
) -> dict:
    """Scan loop positions on the sphere of radius r and find where the loop's
    'preferred orientation' (Wahba alignment) is DEGENERATE (singular-value gap
    -> 0). That locus is the connection's monopole: orbits encircling it pick up
    -I, orbits that do not pick up +I. Report the minimal-gap directions and how
    they relate to the canonical port / face / edge directions.
    """
    weights = 1.0 + eps * PORT_HANDEDNESS
    neighbours = bond_length * PORT_UNIT
    # Fibonacci sphere of candidate loop directions
    idx = np.arange(n)
    phi_gold = np.pi * (3.0 - np.sqrt(5.0))
    z = 1.0 - 2.0 * (idx + 0.5) / n
    rad = np.sqrt(np.maximum(0.0, 1.0 - z * z))
    theta = phi_gold * idx
    dirs = np.stack([rad * np.cos(theta), rad * np.sin(theta), z], axis=1)

    gaps = np.zeros(n)
    for i, dhat in enumerate(dirs):
        p = r * dhat
        bonds = neighbours - p
        bu = bonds / np.linalg.norm(bonds, axis=1, keepdims=True)
        B = (weights[:, None, None] * bu[:, :, None] * PORT_UNIT[:, None, :]).sum(axis=0)
        _, S, _ = np.linalg.svd(B)
        gaps[i] = S[1] - S[2]

    order = np.argsort(gaps)
    deg_dirs = dirs[order[:6]]
    # face-centre directions of the port tetrahedron = -port directions (a
    # regular tetrahedron's face centres point opposite its vertices)
    face_dirs = -PORT_UNIT
    # nearest canonical reference to the lowest-gap direction
    d0 = deg_dirs[0]
    best_face = float(np.max(face_dirs @ d0))
    best_port = float(np.max(PORT_UNIT @ d0))
    return {
        "r_over_bond": r / bond_length,
        "min_gap": float(gaps.min()),
        "max_gap": float(gaps.max()),
        "lowest_gap_dir": d0.tolist(),
        "cos_to_nearest_face_centre": best_face,
        "cos_to_nearest_port_vertex": best_port,
        "lowest_gap_dirs": deg_dirs.tolist(),
    }


def solid_angle(unit_path: np.ndarray) -> float:
    """Signed solid angle enclosed by a closed path of unit vectors on S^2.

    Sum of signed spherical-triangle areas from the path centroid pole.
    Returns the geometric (Berry) phase magnitude for the frame axis.
    """
    pole = unit_path.mean(axis=0)
    npole = np.linalg.norm(pole)
    if npole < 1e-9:
        pole = np.array([0.0, 0.0, 1.0])
    else:
        pole = pole / npole
    total = 0.0
    for i in range(len(unit_path) - 1):
        a, b = unit_path[i], unit_path[i + 1]
        # signed area of spherical triangle (pole, a, b) via spherical excess
        cross = np.cross(a, b)
        num = np.dot(pole, cross)
        den = 1.0 + np.dot(pole, a) + np.dot(pole, b) + np.dot(a, b)
        total += 2.0 * np.arctan2(num, den)
    return total


# ---------------------------------------------------------------------------
# Projected path / winding numbers (secondary claim: (2,3) trefoil?)
# ---------------------------------------------------------------------------
def projected_path_winding(
    r: float,
    plane_normal: np.ndarray,
    eps: float,
    loop_radius: float = 0.25,
    bond_length: float = float(np.sqrt(3.0)),
    n_steps: int = 4096,
    n_orbits: int = 2,
) -> dict:
    """Trace a marked point on the loop over n_orbits, project from host view,
    and measure the (p,q) winding numbers.

    p = orbital winding (azimuth turns); q = internal/twist winding of the
    marked point about the loop axis (accumulated frame twist).
    """
    u, v = orbit_plane_basis(plane_normal)
    neighbours = bond_length * PORT_UNIT
    weights = 1.0 + eps * PORT_HANDEDNESS
    phis = np.linspace(0.0, 2.0 * np.pi * n_orbits, n_steps, endpoint=False)

    twist = np.zeros(phis.size)  # accumulated frame twist about loop axis
    pts = np.zeros((phis.size, 3))
    prev_R = None
    acc = 0.0
    e1_prev = None
    axis_prev = None
    for i, phi in enumerate(phis):
        p = r * (np.cos(phi) * u + np.sin(phi) * v)
        bonds = neighbours - p
        bonds_unit = bonds / np.linalg.norm(bonds, axis=1, keepdims=True)
        B = (weights[:, None, None] * bonds_unit[:, :, None] * PORT_UNIT[:, None, :]).sum(axis=0)
        U, S, Vt = np.linalg.svd(B)
        d = np.sign(np.linalg.det(U @ Vt))
        R = U @ np.diag([1.0, 1.0, d]) @ Vt

        axis = R[:, 2]  # loop spin axis
        e1 = R[:, 0]
        e2 = R[:, 1]
        # measure incremental twist of e1 about axis relative to a
        # parallel-transported reference (Fermi-Walker-ish, discrete)
        if e1_prev is not None:
            # transport e1_prev to be perpendicular to current axis
            tp = e1_prev - np.dot(e1_prev, axis) * axis
            if np.linalg.norm(tp) > 1e-9:
                tp /= np.linalg.norm(tp)
                cosang = np.clip(np.dot(tp, e1), -1.0, 1.0)
                sinang = np.dot(np.cross(tp, e1), axis)
                acc += np.arctan2(sinang, cosang)
        twist[i] = acc
        e1_prev = e1
        axis_prev = axis
        prev_R = R

        # marked point on the loop body (internal angle 0, carried by the frame)
        pts[i] = p + loop_radius * (np.cos(acc) * e1 + np.sin(acc) * e2)

    # orbital winding p = n_orbits (by construction over 2pi*n_orbits)
    # twist winding q = total accumulated twist / 2pi
    q_winding = twist[-1] / (2.0 * np.pi)
    p_winding = float(n_orbits)
    return {
        "p_orbital_winding": p_winding,
        "q_twist_winding": float(q_winding),
        "twist_per_orbit_rad": float(twist[-1] / n_orbits),
        "twist_per_orbit_over_pi": float(twist[-1] / n_orbits / np.pi),
        "path_points": pts,
        "twist_trace": twist,
        "phis": phis,
    }


# ---------------------------------------------------------------------------
# Sweeps + driver
# ---------------------------------------------------------------------------
def run_sweeps() -> dict:
    bond = float(np.sqrt(3.0))
    # radii from deep-interstitial (small) out toward / past the neighbour shell
    radii = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.5, 1.7]
    radii = [r * bond for r in radii]  # scale to bond length

    # orbit-plane normals: chiral axis (y), a port axis, z, and several oblique
    planes = {
        "chiral_axis_y": np.array([0.0, 1.0, 0.0]),
        "port0_axis": PORT_UNIT[0].copy(),
        "z_axis": np.array([0.0, 0.0, 1.0]),
        "x_axis": np.array([1.0, 0.0, 0.0]),
        "oblique_111b": np.array([1.0, -1.0, 1.0]),
        "oblique_213": np.array([2.0, 1.0, 3.0]),
    }
    eps_values = [0.0, 0.3, 0.6, 0.9]

    out = {"radius_sweep": [], "plane_sweep": [], "eps_sweep": [], "tilt_scan": []}

    def row(res):
        return {
            "return_sign": res.return_sign,
            "signed_dot_one": res.signed_dot_one,
            "solid_angle_over_pi": res.solid_angle_zaxis / np.pi,
            "double_cover_ok": res.double_cover_ok,
            "min_align_gap": res.min_align_gap,
            "max_step_jump": res.max_step_jump,
            "closure_error": res.closure_error,
        }

    # 1) radius sweep at BOTH a non-encircling (chiral-y) and an encircling
    #    (z-axis) plane, achiral (eps=0) and chiral (eps=.6): is the sign robust
    #    across radius within each sector? (topological-within-sector test)
    for plane_name in ("chiral_axis_y", "z_axis"):
        for eps in (0.0, 0.6):
            for r in radii:
                res = compute_holonomy(r, planes[plane_name], eps=eps, bond_length=bond)
                out["radius_sweep"].append(
                    {"r_over_bond": r / bond, "eps": eps, "plane": plane_name, **row(res)}
                )

    # 2) plane sweep at a fixed mid radius
    r_mid = 1.0 * bond
    for name, normal in planes.items():
        res = compute_holonomy(r_mid, normal, eps=0.6, bond_length=bond)
        out["plane_sweep"].append(
            {"plane": name, "r_over_bond": 1.0, "eps": 0.6, **row(res)}
        )

    # 3) eps (chirality knob) sweep at BOTH planes: does CHIRALITY control the
    #    sign, or is it the orbital-encircling topology? (Grant's claim attributes
    #    the half-twist to crystal CHIRALITY -> this is the load-bearing test.)
    for plane_name in ("chiral_axis_y", "z_axis"):
        for eps in eps_values:
            res = compute_holonomy(r_mid, planes[plane_name], eps=eps, bond_length=bond)
            out["eps_sweep"].append(
                {"eps": eps, "r_over_bond": 1.0, "plane": plane_name, **row(res)}
            )

    # 3b) n_steps robustness: a true Z2 invariant must not depend on resolution.
    out["nsteps_robustness"] = []
    for ns in (256, 512, 1024, 2048, 4096):
        res = compute_holonomy(r_mid, planes["z_axis"], eps=0.6, bond_length=bond, n_steps=ns)
        out["nsteps_robustness"].append(
            {"n_steps": ns, "plane": "z_axis", **row(res)}
        )

    # 4) tilt scan: rotate the orbit-plane normal from chiral-y (+I) toward z (-I)
    #    to locate the +I/-I boundary and check whether it sits at a degeneracy.
    for theta_deg in np.linspace(0.0, 90.0, 31):
        th = np.radians(theta_deg)
        normal = np.array([0.0, np.cos(th), np.sin(th)])  # y -> z tilt
        res = compute_holonomy(r_mid, normal, eps=0.6, bond_length=bond)
        out["tilt_scan"].append({"tilt_deg": float(theta_deg), "r_over_bond": 1.0, "eps": 0.6, **row(res)})

    return out


def summarise(sweeps: dict) -> dict:
    """Reduce the sweeps to a verdict-relevant summary."""
    rs = sweeps["radius_sweep"]
    ps = sweeps["plane_sweep"]
    es = sweeps["eps_sweep"]

    ts = sweeps["tilt_scan"]
    nr = sweeps.get("nsteps_robustness", [])
    allrows = rs + ps + es + ts + nr

    # smooth-transport guard: the genuine artifact is a large quaternion step
    # jump (an SVD/Wahba det-branch flip is ~pi). closure_error ~1e-3 is mere
    # discretization (scales as 1/n_steps), NOT non-closure -> not a guard.
    def smooth(row):
        return row["max_step_jump"] < 0.5 and abs(abs(row["signed_dot_one"]) - 1.0) < 1e-2

    # within-sector robustness (the topological-within-sector test)
    def signs_where(rows, **kw):
        sel = [r for r in rows if all(r.get(k) == v for k, v in kw.items())]
        return [r["return_sign"] for r in sel]

    rad_y_e0 = signs_where(rs, plane="chiral_axis_y", eps=0.0)
    rad_y_e6 = signs_where(rs, plane="chiral_axis_y", eps=0.6)
    rad_z_e0 = signs_where(rs, plane="z_axis", eps=0.0)
    rad_z_e6 = signs_where(rs, plane="z_axis", eps=0.6)
    eps_y = signs_where(es, plane="chiral_axis_y")
    eps_z = signs_where(es, plane="z_axis")

    minus_rows = [r for r in allrows if r["return_sign"] == -1]
    minus_smooth = [r for r in minus_rows if smooth(r)]
    transition_rows = [r for r in allrows if r["max_step_jump"] >= 0.5]

    boundary = None
    for a, b in zip(ts, ts[1:]):
        if a["return_sign"] != b["return_sign"]:
            boundary = {
                "tilt_lo_deg": a["tilt_deg"], "tilt_hi_deg": b["tilt_deg"],
                "gap_lo": a["min_align_gap"], "gap_hi": b["min_align_gap"],
                "jump_lo": a["max_step_jump"], "jump_hi": b["max_step_jump"],
            }
            break

    return {
        # within-sector robustness: is the sign constant across r / eps?
        "radius_chiral_y_eps0_signs": sorted(set(rad_y_e0)),
        "radius_chiral_y_eps0.6_signs": sorted(set(rad_y_e6)),
        "radius_z_axis_eps0_signs": sorted(set(rad_z_e0)),
        "radius_z_axis_eps0.6_signs": sorted(set(rad_z_e6)),
        "sign_robust_across_radius_each_sector": (
            len(set(rad_y_e0)) == 1 and len(set(rad_y_e6)) == 1
            and len(set(rad_z_e0)) == 1 and len(set(rad_z_e6)) == 1
        ),
        # CHIRALITY-INDEPENDENCE: does eps (handedness) flip the sign? (it should
        # NOT, if the half-twist is orbital-encircling, not chirality-driven)
        "eps_sweep_chiral_y_signs": eps_y,
        "eps_sweep_z_axis_signs": eps_z,
        "sign_independent_of_chirality_eps": (len(set(eps_y)) == 1 and len(set(eps_z)) == 1),
        "achiral_eps0_z_axis_sign": rad_z_e0[0] if rad_z_e0 else None,
        # plane / tilt dependence (the +I<->-I sectoring)
        "plane_sweep_signs": [r["return_sign"] for r in ps],
        "tilt_scan_signs": [r["return_sign"] for r in ts],
        "sign_constant_over_plane": len({r["return_sign"] for r in ps}) == 1,
        "plus_minus_boundary_at_degeneracy": boundary,
        # n_steps robustness of the Z2 invariant
        "nsteps_signs": [r["return_sign"] for r in nr],
        "sign_robust_over_nsteps": len({r["return_sign"] for r in nr}) == 1,
        # transport-quality bookkeeping
        "n_minus_I_total": len(minus_rows),
        "n_minus_I_smooth_transport": len(minus_smooth),
        "n_transition_rows_branch_flip": len(transition_rows),
        "double_cover_consistent_everywhere": all(r["double_cover_ok"] for r in allrows),
    }


def make_visualisation(out_png: str) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

    bond = float(np.sqrt(3.0))
    neighbours = bond * PORT_UNIT

    fig = plt.figure(figsize=(16, 5.2))

    # Panel A: loop orbiting host in the chiral neighbourhood + frame twist
    axA = fig.add_subplot(1, 3, 1, projection="3d")
    normal = np.array([0.0, 1.0, 0.0])  # chiral axis
    u, v = orbit_plane_basis(normal)
    r = 1.0 * bond
    phis = np.linspace(0.0, 2 * np.pi, 64, endpoint=True)
    orbit = np.array([r * (np.cos(p) * u + np.sin(p) * v) for p in phis])
    axA.plot(orbit[:, 0], orbit[:, 1], orbit[:, 2], "k-", lw=1.5, label="orbit (1 turn)")
    # host
    axA.scatter([0], [0], [0], c="k", s=120, marker="o", label="host node")
    # neighbours coloured by handedness
    for j in range(4):
        col = "crimson" if PORT_HANDEDNESS[j] > 0 else "royalblue"
        axA.scatter(*neighbours[j], c=col, s=90, marker="^")
        axA.plot(
            [0, neighbours[j, 0]],
            [0, neighbours[j, 1]],
            [0, neighbours[j, 2]],
            c=col,
            lw=1.0,
            alpha=0.5,
        )
    # frames along the orbit
    weights = 1.0 + 0.6 * PORT_HANDEDNESS
    for p in np.linspace(0, 2 * np.pi, 16, endpoint=False):
        pos = r * (np.cos(p) * u + np.sin(p) * v)
        bonds = neighbours - pos
        bu = bonds / np.linalg.norm(bonds, axis=1, keepdims=True)
        B = (weights[:, None, None] * bu[:, :, None] * PORT_UNIT[:, None, :]).sum(axis=0)
        U, S, Vt = np.linalg.svd(B)
        d = np.sign(np.linalg.det(U @ Vt))
        R = U @ np.diag([1, 1, d]) @ Vt
        axA.quiver(*pos, *R[:, 0], length=0.35, color="darkorange", lw=1.2)
        axA.quiver(*pos, *R[:, 2], length=0.35, color="green", lw=1.0)
    # degeneracy locus (the Berry-monopole the encircling orbits enclose)
    deg = locate_degeneracy(r, eps=0.6)
    for d in np.array(deg["lowest_gap_dirs"])[:4]:
        axA.scatter(*(1.6 * d), c="magenta", s=45, marker="*")
    axA.scatter([], [], c="crimson", marker="^", label="RH neighbour (ports 0,2)")
    axA.scatter([], [], c="royalblue", marker="^", label="LH neighbour (ports 1,3)")
    axA.scatter([], [], c="magenta", marker="*", label="orientation-degeneracy locus")
    axA.set_title("A. Loop orbiting host in chiral K4\nneighbourhood (frames: e1 orange, axis green)")
    axA.legend(loc="upper left", fontsize=6)
    axA.view_init(elev=22, azim=35)
    axA.set_box_aspect((1, 1, 1))

    # Panel B: SU(2) return sign vs orbit-plane tilt (path-dependence is the story)
    axB = fig.add_subplot(1, 3, 2)
    tilts = np.linspace(0.0, 90.0, 46)
    for eps, col in ((0.0, "tab:blue"), (0.6, "tab:red")):
        dots = []
        gaps = []
        for td in tilts:
            th = np.radians(td)
            nrm = np.array([0.0, np.cos(th), np.sin(th)])
            res = compute_holonomy(r, nrm, eps=eps, bond_length=bond, n_steps=1024)
            dots.append(res.signed_dot_one)
            gaps.append(res.min_align_gap)
        axB.plot(tilts, dots, "-", color=col, lw=1.6, label=f"eps={eps}: q(2pi).q(0)")
        axB.plot(tilts, gaps, ":", color=col, lw=1.0, label=f"eps={eps}: align gap")
    axB.axhline(1.0, color="gray", ls="--", lw=0.8)
    axB.axhline(-1.0, color="k", ls="--", lw=0.8)
    axB.axvspan(0, 45, color="tab:green", alpha=0.07)
    axB.axvspan(45, 90, color="tab:purple", alpha=0.07)
    axB.annotate("degeneracy\n(gap->0)", xy=(45, 0.0), xytext=(56, 0.30), fontsize=7,
                 arrowprops=dict(arrowstyle="->", lw=0.8))
    axB.text(68, -0.62, "chiral eps=0.6:\n-I half-twist", fontsize=7, ha="center", color="tab:red")
    axB.text(68, 0.82, "achiral eps=0: +I (no twist)", fontsize=7, ha="center", color="tab:blue")
    axB.set_xlabel("orbit-plane tilt from chiral y-axis (deg)")
    axB.set_ylabel("SU(2) return  /  alignment gap")
    axB.set_title("B. Holonomy vs orbit plane: PATH-DEPENDENT.\nchiral flips to -I past a degeneracy; achiral stays +I")
    axB.legend(fontsize=6, loc="lower left")
    axB.grid(alpha=0.3)

    # Panel C: projected real-space path (orbit + twist) over 2 orbits, -I plane
    axC = fig.add_subplot(1, 3, 3, projection="3d")
    znorm = np.array([0.0, 0.0, 1.0])  # a -I plane (half-twist present)
    pp = projected_path_winding(r, znorm, eps=0.6, loop_radius=0.3, n_steps=2000, n_orbits=2)
    path = pp["path_points"]
    axC.plot(path[:, 0], path[:, 1], path[:, 2], "-", color="purple", lw=1.0)
    axC.scatter([0], [0], [0], c="k", s=80, marker="o")
    axC.set_title(
        f"C. Marked-point path, 2 orbits (z-plane, -I)\n"
        f"twist/orbit = {pp['twist_per_orbit_over_pi']:.2f} pi; "
        f"(p,q)=({pp['p_orbital_winding']:.0f},{pp['q_twist_winding']:.2f})"
    )
    axC.set_box_aspect((1, 1, 1))

    fig.tight_layout()
    fig.savefig(out_png, dpi=130)
    plt.close(fig)


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(here, "_output")
    os.makedirs(out_dir, exist_ok=True)

    print("=" * 78)
    print("CHIRAL ORBITAL HOLONOMY DIAGNOSTIC")
    print("Does a loop orbiting a host K4 node accumulate a half-twist (pi) per orbit?")
    print("=" * 78)

    sweeps = run_sweeps()
    summary = summarise(sweeps)

    print("\n--- RADIUS SWEEP (non-encircling chiral-y vs encircling z-axis) ---")
    print(f"{'plane':>13} {'r/bond':>8} {'eps':>5} {'return':>7} {'dot(2pi)':>9} {'gap':>7} {'jump':>7}")
    for row in sweeps["radius_sweep"]:
        print(
            f"{row['plane']:>13} {row['r_over_bond']:>8.3f} {row['eps']:>5.1f} "
            f"{'-I' if row['return_sign'] < 0 else '+I':>7} "
            f"{row['signed_dot_one']:>9.4f} {row['min_align_gap']:>7.3f} {row['max_step_jump']:>7.3f}"
        )

    print("\n--- PLANE SWEEP (r/bond = 1.0, eps = 0.6) ---")
    for row in sweeps["plane_sweep"]:
        print(
            f"  {row['plane']:>14}: return={'-I' if row['return_sign']<0 else '+I'} "
            f"dot(2pi)={row['signed_dot_one']:+.4f} solid/pi={row['solid_angle_over_pi']:+.4f} "
            f"gap={row['min_align_gap']:.3f} jump={row['max_step_jump']:.3f} close={row['closure_error']:.1e}"
        )

    print("\n--- EPS (chirality knob) SWEEP @ r/bond=1.0 [does CHIRALITY flip the sign?] ---")
    for row in sweeps["eps_sweep"]:
        print(
            f"  {row['plane']:>13} eps={row['eps']:.1f}: return={'-I' if row['return_sign']<0 else '+I'} "
            f"dot(2pi)={row['signed_dot_one']:+.4f} solid/pi={row['solid_angle_over_pi']:+.4f}"
        )

    print("\n--- N_STEPS ROBUSTNESS of the Z2 invariant (z-axis, eps=0.6) ---")
    for row in sweeps["nsteps_robustness"]:
        print(
            f"  n_steps={row['n_steps']:>5}: return={'-I' if row['return_sign']<0 else '+I'} "
            f"dot(2pi)={row['signed_dot_one']:+.4f} jump={row['max_step_jump']:.3f}"
        )

    print("\n--- TILT SCAN (orbit normal y->z, r/bond=1.0, eps=0.6) ---")
    print(f"{'tilt_deg':>9} {'return':>7} {'dot(2pi)':>9} {'solid/pi':>9} {'gap':>7} {'jump':>7}")
    for row in sweeps["tilt_scan"]:
        print(
            f"{row['tilt_deg']:>9.1f} {'-I' if row['return_sign']<0 else '+I':>7} "
            f"{row['signed_dot_one']:>9.4f} {row['solid_angle_over_pi']:>9.4f} "
            f"{row['min_align_gap']:>7.3f} {row['max_step_jump']:>7.3f}"
        )

    print("\n--- PROJECTED PATH / WINDING (r/bond=1.0, eps=0.6) ---")
    bond = float(np.sqrt(3.0))
    pp_planes = {
        "chiral_y (+I)": np.array([0.0, 1.0, 0.0]),
        "z_axis (-I)": np.array([0.0, 0.0, 1.0]),
        "x_axis (-I)": np.array([1.0, 0.0, 0.0]),
    }
    pp_results = {}
    for label, normal in pp_planes.items():
        pp = projected_path_winding(bond, normal, eps=0.6)
        pp_results[label] = pp
        print(
            f"  {label:>14}: twist/orbit = {pp['twist_per_orbit_over_pi']:+.4f} pi  "
            f"measured (p,q) = ({pp['p_orbital_winding']:.0f}, {pp['q_twist_winding']:+.3f})"
        )
    pp = pp_results["z_axis (-I)"]  # for the JSON payload below

    print("\n--- DEGENERACY LOCUS (what the encircling orbits enclose) ---")
    for rr in (0.5 * bond, 1.0 * bond):
        deg = locate_degeneracy(rr, eps=0.6)
        print(
            f"  r/bond={deg['r_over_bond']:.2f}: gap range [{deg['min_gap']:.3f}, {deg['max_gap']:.3f}]; "
            f"lowest-gap dir cos to face-centre={deg['cos_to_nearest_face_centre']:.3f}, "
            f"to port-vertex={deg['cos_to_nearest_port_vertex']:.3f}"
        )

    print("\n--- SUMMARY (verdict inputs) ---")
    for k, val in summary.items():
        print(f"  {k}: {val}")

    out_png = os.path.join(out_dir, "chiral_orbital_holonomy.png")
    make_visualisation(out_png)
    print(f"\nVisualisation -> {out_png}")

    # persist machine-readable numbers
    payload = {
        "summary": summary,
        "sweeps": sweeps,
        "projected_path": {
            k: val for k, val in pp.items() if not isinstance(val, np.ndarray)
        },
    }
    out_json = os.path.join(out_dir, "chiral_orbital_holonomy.json")
    with open(out_json, "w") as fh:
        json.dump(payload, fh, indent=2, default=float)
    print(f"Numbers     -> {out_json}")


if __name__ == "__main__":
    main()
