#!/usr/bin/env python3
r"""2nd-shell I4₁32 screw holonomy — does the TRUE crystal chirality make the
SU(2) half-twist PATH-INDEPENDENT (intrinsic spin-½) or PATH-DEPENDENT
(projected helicity)?

DECISIVE follow-up to `chiral_orbital_holonomy.py` (verdict II: π is
chirality-required but path-dependent, because that test used a reflection-EVEN
anisotropy proxy `w_j = 1+ε·s_j` on a single ACHIRAL host tetrahedron, NOT the
true chirality). This driver makes the two corrections that test's §7 demanded:

  1. TRUE chirality — the reflection-ODD 2nd-shell A/B 4₁ SCREW (I4₁32, Axiom 1),
     not a reflection-even knob. The 1st-shell tetrahedron {p_j} is geometrically
     ACHIRAL (k4-rotation-group.md:37). The genuine handedness lives in the screw
     relation between the A- and B-sublattice tetrahedra (the 2nd shell). We
     decorate every neighbour with its Cosserat micro-rotation frame following the
     genuine 4₁ screw; the ε-anisotropy knob is GONE (equal Wahba weights).

  2. Score PATH-INDEPENDENCE, not just "is it π." Intrinsic γ⁵ spin-½ (the U(1)
     fibre phase of SU(2), finkelstein-misner-spin-half-derivation.md:141) is
     frame/path-INDEPENDENT; projected helicity S·p̂ is path-dependent by nature.
     The DISCRIMINATOR is the FRACTION of swept orbits returning −I.

TRANSPORT IS REUSED VERBATIM from chiral_orbital_holonomy.py (the brief: "extend
the geometry, don't rebuild the transport"): rotation_to_quaternion (SO(3)→SU(2)
lift), orbit_plane_basis, solid_angle, the Wahba/Kabsch SVD pattern, the
continuous-lift parallel transport, the smooth-transport guard, the double-cover
(4π → +I) check. NEW here: the canonical 2nd-shell neighbourhood + the screw
frame field + the fraction/path-dependence scoring.

Canonical geometry (ave-canonical-source — mirror, do NOT invent):
  * port vectors p_j  (k4_tlm.py:111-114) — host A's four 1st-shell B-neighbours.
  * sublattices A=all-even, B=all-odd, B=A+(1,1,1); B joins A via −p_k
    (k4_tlm.py:115,215-216). 2nd shell = canonical two-hop A→B→A = {p_j − p_k}.
  * port handedness {0,2} RH, {1,3} LH (k4_tlm.py:542) — the native screw sign.

Verdict classes (consistency-vs-emergence: EMERGENCE test as framed):
  (I)   f ≈ 100% (π for ALL paths)  → PATH-INDEPENDENT → intrinsic spin-½ emerges.
  (II)  f partial / encircling-cond → PATH-DEPENDENT  → projected helicity only.
  (III) f ≈ 0% native AND achiral   → the true screw removes the π entirely.

Run:  python3 src/scripts/vol_1_foundations/secondshell_screw_holonomy.py
Outputs: console summary + JSON + PNG (the screw neighbourhood + holonomy-vs-path
map) in this script's _output dir.
"""

from __future__ import annotations

import json
import os

import numpy as np

# ── REUSE the prior driver's transport machinery (same directory) ──────────────
# rotation_to_quaternion: SO(3)→SU(2) lift (w≥0 branch); orbit_plane_basis:
# orbit-plane spanning vectors; solid_angle: Berry solid angle; PORT_VECTORS /
# PORT_UNIT / PORT_HANDEDNESS: canonical K4 port geometry (k4_tlm.py mirror).
_HERE = os.path.dirname(os.path.abspath(__file__))
import sys

if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from chiral_orbital_holonomy import (  # noqa: E402
    PORT_HANDEDNESS,
    PORT_UNIT,
    PORT_VECTORS,
    orbit_plane_basis,
    rotation_to_quaternion,
    solid_angle,
)


# ═══════════════════════════════════════════════════════════════════════════════
# CANONICAL 2nd-SHELL NEIGHBOURHOOD (from the lattice; NOT invented)
# ═══════════════════════════════════════════════════════════════════════════════
def build_neighbourhood(include_2nd_shell: bool = True):
    """Host A at origin. Return (positions, home_unit, shell_id) for its
    canonical neighbourhood.

      * 1st shell: the 4 B-neighbours at the port vectors p_j (k4_tlm.py:111-114).
      * 2nd shell: the 12 A-neighbours reached by the canonical two-hop A→B→A.
        From host, hop A→B along p_j, then B→A along −p_k (B joins A via the
        exact negative vectors, k4_tlm.py:115): position = p_j − p_k (j ≠ k).
        The 12 distinct values are the permutations of (0,±2,±2) — the FCC /
        cuboctahedron shell. Achiral as bare positions (O_h); the chirality is
        the SCREW DECORATION, not the positions.
    """
    pos = [PORT_VECTORS[j].copy() for j in range(4)]  # 1st shell B at p_j
    shell = [1, 1, 1, 1]
    if include_2nd_shell:
        seen = set()
        for j in range(4):
            for k in range(4):
                if j == k:
                    continue
                v = PORT_VECTORS[j] - PORT_VECTORS[k]  # A→B→A two-hop
                key = tuple(np.round(v).astype(int))
                if key in seen:
                    continue
                seen.add(key)
                pos.append(v.astype(float))
                shell.append(2)
    positions = np.array(pos)
    home_unit = positions / np.linalg.norm(positions, axis=1, keepdims=True)
    return positions, home_unit, np.array(shell)


# ═══════════════════════════════════════════════════════════════════════════════
# THE GENUINE I4₁32 4₁ SCREW FRAME FIELD (the reflection-ODD ingredient)
# ═══════════════════════════════════════════════════════════════════════════════
def _rodrigues(axis_unit: np.ndarray, angle: float) -> np.ndarray:
    """Proper rotation by `angle` about `axis_unit` (Rodrigues)."""
    ax, ay, az = axis_unit
    K = np.array([[0.0, -az, ay], [az, 0.0, -ax], [-ay, ax, 0.0]])
    return np.eye(3) + np.sin(angle) * K + (1.0 - np.cos(angle)) * (K @ K)


def screw_frame(x: np.ndarray, screw_axis: np.ndarray, kappa: float) -> np.ndarray:
    """Cosserat micro-rotation frame at lattice position x for a 4₁ screw of
    rate `kappa` about `screw_axis`:  R(x) = Rot(â, κ·(x·â)).

    This is THE defining operation of a chiral (screw-axis) space group: the
    local frame rotates in proportion to displacement ALONG the axis.
      * κ > 0  → I4₁32 native 4₁ screw (right-handed)
      * κ < 0  → I4₃32 mirror 4₃ screw (left-handed enantiomorph)
      * κ = 0  → ACHIRAL control (frame field flat; recovers the prior baseline)

    Reflection-ODD: a mirror through any plane containing â sends x·â → −x·â,
    so R → Rot(â,−κ(x·â)) = the opposite-handed screw — NOT rotation-equivalent.
    (Contrast the prior ε-anisotropy, which a mirror maps to itself.)
    """
    ahat = screw_axis / np.linalg.norm(screw_axis)
    return _rodrigues(ahat, kappa * float(np.dot(x, ahat)))


# ═══════════════════════════════════════════════════════════════════════════════
# HOLONOMY around one orbit (extends compute_holonomy; transport unchanged)
# ═══════════════════════════════════════════════════════════════════════════════
def compute_screw_holonomy(
    r: float,
    plane_normal: np.ndarray,
    kappa: float,
    screw_axis: np.ndarray,
    positions: np.ndarray,
    home_unit: np.ndarray,
    n_steps: int = 512,
    n_orbits: int = 2,
) -> dict:
    """Parallel-transport the loop frame around `n_orbits` orbits of the host and
    return the SU(2) holonomy.

    The preferred orientation at azimuth φ is the Wahba/Kabsch rotation aligning
    the SCREW-DECORATED neighbour references {R_screw(x_n)·ĥ_n} to the observed
    bond directions {(x_n − p(φ))/|·|}, EQUAL WEIGHTS (no anisotropy knob). The
    chirality enters ONLY through R_screw. κ=0 + 1st-shell-only reduces EXACTLY
    to the prior ε=0 achiral baseline.
    """
    u, v = orbit_plane_basis(plane_normal)
    # Screw-decorated references, fixed per neighbour (the chiral target frame).
    refs = np.array([screw_frame(positions[n], screw_axis, kappa) @ home_unit[n] for n in range(len(positions))])

    phis = np.linspace(0.0, 2.0 * np.pi * n_orbits, n_steps * n_orbits, endpoint=True)
    quats = np.zeros((phis.size, 4))
    zaxis = np.zeros((phis.size, 3))
    rots = np.zeros((phis.size, 3, 3))
    min_gap = np.inf
    max_jump = 0.0
    prev_q = None
    for i, phi in enumerate(phis):
        p = r * (np.cos(phi) * u + np.sin(phi) * v)
        d = positions - p
        dn = np.linalg.norm(d, axis=1, keepdims=True)
        dn = np.maximum(dn, 1e-6)  # guard: loop must not sit on a neighbour
        obs = d / dn
        # Wahba: B = Σ obs_n ⊗ ref_n ; R = U diag(1,1,det) Vᵀ
        B = (obs[:, :, None] * refs[:, None, :]).sum(axis=0)
        U, S, Vt = np.linalg.svd(B)
        det = np.sign(np.linalg.det(U @ Vt))
        R = U @ np.diag([1.0, 1.0, det]) @ Vt
        min_gap = min(min_gap, S[1] - S[2])

        q = rotation_to_quaternion(R)
        if prev_q is not None:
            if np.dot(q, prev_q) < 0.0:
                q = -q  # continuous SU(2) lift = parallel transport of the sign
            jump = 2.0 * np.arccos(min(1.0, abs(float(np.dot(q, prev_q)))))
            max_jump = max(max_jump, jump)
        quats[i] = q
        prev_q = q
        zaxis[i] = R[:, 2]
        rots[i] = R

    idx_one = n_steps  # index of φ = 2π
    q0 = quats[0]
    q_one = quats[idx_one] if idx_one < phis.size else quats[-1]
    dot_one = float(np.dot(q_one, q0))
    closure_err = float(np.linalg.norm(rots[idx_one] - rots[0])) if idx_one < phis.size else float("nan")
    return {
        "return_sign": 1 if dot_one > 0 else -1,
        "signed_dot_one": dot_one,
        "double_cover_ok": bool(np.dot(quats[-1], q0) > 0.0),  # 4π → +q0
        "min_align_gap": float(min_gap),
        "max_step_jump": float(max_jump),
        "closure_error": closure_err,
        "solid_angle_over_pi": float(solid_angle(zaxis[: idx_one + 1]) / np.pi),
    }


def _smooth(rec: dict) -> bool:
    """Genuine-holonomy guard: a clean Z₂ return (|dot|≈1) reached by smooth
    transport (no ~π SVD branch-flip jump). Matches the prior driver's guard."""
    return rec["max_step_jump"] < 0.5 and abs(abs(rec["signed_dot_one"]) - 1.0) < 1e-2


# ═══════════════════════════════════════════════════════════════════════════════
# THE 400-ORBIT BATTERY (uniform orbit planes × radii) — the f discriminator
# ═══════════════════════════════════════════════════════════════════════════════
def run_path_battery(
    kappa: float,
    screw_axis: np.ndarray,
    positions: np.ndarray,
    home_unit: np.ndarray,
    n_paths: int = 400,
    seed: int = 1,
    r_lo: float = 0.2,
    r_hi: float = 2.5,
    n_steps: int = 512,
    n_orbits: int = 2,
) -> dict:
    """Sweep `n_paths` random orbits (uniform-on-sphere plane normals × uniform
    radii) and score the FRACTION returning −I. This is the path-independence
    discriminator: f≈1 → every path gives π (intrinsic); f partial → conditional
    (projected); f≈0 → no π."""
    rng = np.random.default_rng(seed)
    normals = rng.standard_normal((n_paths, 3))
    normals /= np.linalg.norm(normals, axis=1, keepdims=True)
    radii = rng.uniform(r_lo, r_hi, n_paths)

    n_minus = 0
    n_minus_smooth = 0
    double_cover_all = True
    minus_solid = []
    for i in range(n_paths):
        rec = compute_screw_holonomy(
            float(radii[i]),
            normals[i],
            kappa,
            screw_axis,
            positions,
            home_unit,
            n_steps=n_steps,
            n_orbits=n_orbits,
        )
        double_cover_all = double_cover_all and rec["double_cover_ok"]
        if rec["return_sign"] == -1:
            n_minus += 1
            if _smooth(rec):
                n_minus_smooth += 1
            minus_solid.append(rec["solid_angle_over_pi"])
    return {
        "n_paths": n_paths,
        "n_minus_I": n_minus,
        "fraction_minus_I": n_minus / n_paths,
        "n_minus_I_smooth": n_minus_smooth,
        "fraction_minus_I_smooth": n_minus_smooth / n_paths,
        "double_cover_consistent": double_cover_all,
        "minus_solid_angle_over_pi_mean": float(np.mean(minus_solid)) if minus_solid else None,
        "seed": seed,
        "r_range": [r_lo, r_hi],
    }


# ═══════════════════════════════════════════════════════════════════════════════
# PATH-DEPENDENCE MAP (structured orbit-plane grid) + degeneracy gating
# ═══════════════════════════════════════════════════════════════════════════════
def path_dependence_map(
    kappa: float,
    screw_axis: np.ndarray,
    positions: np.ndarray,
    home_unit: np.ndarray,
    r: float = 1.0,
    n_theta: int = 19,
    n_psi: int = 24,
    n_steps: int = 512,
) -> dict:
    """Sign of the holonomy over a structured grid of orbit-plane normals
    (polar θ × azimuth ψ) at fixed radius r. Returns the sign grid + whether the
    −I set is the WHOLE sweep (path-independent) or BOUNDARY-GATED by a
    Wahba-degeneracy locus (path-dependent)."""
    thetas = np.linspace(0.0, np.pi, n_theta)
    psis = np.linspace(0.0, 2.0 * np.pi, n_psi, endpoint=False)
    sign_grid = np.zeros((n_theta, n_psi), dtype=int)
    gap_grid = np.zeros((n_theta, n_psi))
    for a, th in enumerate(thetas):
        for b, ps in enumerate(psis):
            nrm = np.array([np.sin(th) * np.cos(ps), np.sin(th) * np.sin(ps), np.cos(th)])
            rec = compute_screw_holonomy(r, nrm, kappa, screw_axis, positions, home_unit, n_steps=n_steps, n_orbits=2)
            sign_grid[a, b] = rec["return_sign"]
            gap_grid[a, b] = rec["min_align_gap"]
    n_minus = int((sign_grid == -1).sum())
    n_tot = sign_grid.size
    # boundary-gated ⇔ both signs present AND the −I/+I interface sits at low gap
    both = (n_minus > 0) and (n_minus < n_tot)
    return {
        "r": r,
        "fraction_minus_I_grid": n_minus / n_tot,
        "all_minus_I": n_minus == n_tot,
        "all_plus_I": n_minus == 0,
        "both_signs_present": both,
        "min_gap_overall": float(gap_grid.min()),
        "sign_grid": sign_grid.tolist(),
        "thetas": thetas.tolist(),
        "psis": psis.tolist(),
    }


# ═══════════════════════════════════════════════════════════════════════════════
# ROBUSTNESS + REFLECTION-ODD verification
# ═══════════════════════════════════════════════════════════════════════════════
def pitch_robustness(screw_axis, positions, home_unit, kappas, seed=1, n_paths=120):
    """A genuine Z₂ invariant must depend on the SIGN of κ, not its magnitude.
    Report f for a ladder of pitches (and the achiral κ=0)."""
    out = []
    for kp in kappas:
        b = run_path_battery(kp, screw_axis, positions, home_unit, n_paths=n_paths, seed=seed)
        out.append(
            {
                "kappa": kp,
                "fraction_minus_I": b["fraction_minus_I"],
                "fraction_minus_I_smooth": b["fraction_minus_I_smooth"],
            }
        )
    return out


def axis_independence(positions, home_unit, kappa, seed=1, n_paths=120):
    """I4₁32 carries 4₁ screws along all three cubic ⟨100⟩ axes — f should be
    axis-independent for a genuine crystal-chirality observable."""
    axes = {"x": np.array([1.0, 0, 0]), "y": np.array([0, 1.0, 0]), "z": np.array([0, 0, 1.0])}
    return {
        name: run_path_battery(kappa, ax, positions, home_unit, n_paths=n_paths, seed=seed)["fraction_minus_I"]
        for name, ax in axes.items()
    }


def make_visualisation(out_png, positions, home_unit, shell, screw_axis, kappa, pmap, pr, runs):
    """3 panels (extends the prior viz #6): (A) the screw neighbourhood with
    Cosserat frames coloured by screw phase; (B) the holonomy-vs-path map
    (sign over the orbit-plane θ×ψ grid); (C) f(−I) vs screw pitch κ — the
    intrinsic(I)/projected(II) discriminator with the achiral baseline."""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

    fig = plt.figure(figsize=(16.5, 5.4))

    # Panel A — the screw neighbourhood + decorated frames
    axA = fig.add_subplot(1, 3, 1, projection="3d")
    axA.scatter([0], [0], [0], c="k", s=130, marker="o", label="host A (frame = I)")
    ahat = screw_axis / np.linalg.norm(screw_axis)
    for n in range(len(positions)):
        x = positions[n]
        phase = kappa * float(np.dot(x, ahat))  # screw phase at this node
        col = plt.cm.twilight((phase / (2 * np.pi)) % 1.0)
        mk = "^" if shell[n] == 1 else "s"
        sz = 90 if shell[n] == 1 else 55
        axA.scatter(*x, color=col, s=sz, marker=mk, edgecolor="k", linewidth=0.3)
        R = screw_frame(x, screw_axis, kappa)
        axA.quiver(*x, *R[:, 0], length=0.45, color="darkorange", lw=1.0)  # decorated e1
        axA.quiver(*x, *R[:, 2], length=0.45, color="green", lw=0.8)  # decorated axis
    # screw axis line
    t = np.linspace(-2.6, 2.6, 2)
    axA.plot(ahat[0] * t, ahat[1] * t, ahat[2] * t, "k--", lw=0.8, alpha=0.6)
    axA.scatter([], [], c="gray", marker="^", label="1st shell B (4)")
    axA.scatter([], [], c="gray", marker="s", label="2nd shell A (12)")
    axA.set_title(
        "A. Host + 2nd-shell I4₁32 screw neighbourhood\n" "(node colour = 4₁ screw phase; orange e₁, green axis)"
    )
    axA.legend(loc="upper left", fontsize=6)
    axA.view_init(elev=20, azim=35)
    axA.set_box_aspect((1, 1, 1))

    # Panel B — holonomy-vs-path map (the path-(in)dependence picture)
    axB = fig.add_subplot(1, 3, 2)
    grid = np.array(pmap["sign_grid"])
    thetas = np.degrees(pmap["thetas"])
    psis = np.degrees(pmap["psis"])
    im = axB.pcolormesh(psis, thetas, grid, cmap="coolwarm", vmin=-1, vmax=1, shading="auto")
    axB.set_xlabel("orbit-plane azimuth ψ (deg)")
    axB.set_ylabel("orbit-plane polar θ (deg)")
    frac = pmap["fraction_minus_I_grid"] * 100
    tag = (
        "WHOLE SWEEP −I (path-INDEP)"
        if pmap["all_minus_I"]
        else "ALL +I (no twist)" if pmap["all_plus_I"] else "BOTH signs (path-DEP, boundary-gated)"
    )
    axB.set_title(f"B. Holonomy vs orbit plane (native screw, r=1)\n" f"grid f(−I)={frac:.0f}% — {tag}")
    cb = fig.colorbar(im, ax=axB, ticks=[-1, 1], fraction=0.046)
    cb.set_ticklabels(["−I (π)", "+I (0)"])

    # Panel C — f(−I) vs pitch κ: the (I)/(II) discriminator
    axC = fig.add_subplot(1, 3, 3)
    ks = [row["kappa"] for row in pr]
    fs = [row["fraction_minus_I"] * 100 for row in pr]
    fss = [row["fraction_minus_I_smooth"] * 100 for row in pr]
    axC.plot(ks, fs, "o-", color="tab:red", lw=1.8, label="f(−I) all")
    axC.plot(ks, fss, "s--", color="tab:purple", lw=1.0, label="f(−I) smooth")
    f_ach = runs["achiral_1st+2nd (matched control)"]["fraction_minus_I"] * 100
    axC.axhline(f_ach, color="tab:blue", ls=":", lw=1.2, label=f"achiral matched ({f_ach:.0f}%)")
    axC.axhline(100, color="green", ls="--", lw=0.8, alpha=0.6)
    axC.axhspan(95, 100, color="green", alpha=0.08)
    axC.axhspan(0, 2, color="gray", alpha=0.08)
    axC.text(0.02, 97, "(I) intrinsic: every orbit π", fontsize=7, color="green", transform=axC.get_yaxis_transform())
    axC.set_xlabel("screw pitch κ (rad / lattice step)")
    axC.set_ylabel("fraction of orbits returning −I (%)")
    axC.set_ylim(-3, 103)
    axC.set_title(
        "C. f(−I) vs screw pitch — Z₂ is sign-of-κ only\n(I)≈100% intrinsic · (II) partial projected · (III)≈0"
    )
    axC.legend(fontsize=6, loc="center right")
    axC.grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(out_png, dpi=130)
    plt.close(fig)


def main() -> None:
    out_dir = os.path.join(_HERE, "_output")
    os.makedirs(out_dir, exist_ok=True)

    print("=" * 80)
    print("2nd-SHELL I4₁32 SCREW HOLONOMY — intrinsic (path-indep) vs projected (path-dep) spin-½")
    print("=" * 80)

    screw_axis = np.array([0.0, 0.0, 1.0])  # cubic ⟨100⟩, default ẑ
    KAPPA = np.pi / 2.0  # 4₁ rate: 90° per unit lattice step

    pos2, home2, shell2 = build_neighbourhood(include_2nd_shell=True)
    pos1, home1, _ = build_neighbourhood(include_2nd_shell=False)
    print(
        f"\nNeighbourhood: {len(pos1)} 1st-shell B + {int((shell2==2).sum())} 2nd-shell A "
        f"= {len(pos2)} nodes.  screw_axis=ẑ, κ=π/2 (4₁)."
    )

    # ── Controls + the test (matched-baseline, CP8) ───────────────────────────
    print("\n--- BATTERY (400 orbits, uniform plane × radius) — the f discriminator ---")
    runs = {
        "achiral_1st_only (= prior ε=0 baseline)": run_path_battery(0.0, screw_axis, pos1, home1),
        "achiral_1st+2nd (matched control)": run_path_battery(0.0, screw_axis, pos2, home2),
        "NATIVE screw 4₁ (κ>0)": run_path_battery(+KAPPA, screw_axis, pos2, home2),
        "MIRROR screw 4₃ (κ<0)": run_path_battery(-KAPPA, screw_axis, pos2, home2),
    }
    for label, b in runs.items():
        print(
            f"  {label:>42}: f(−I) = {b['n_minus_I']:>3}/{b['n_paths']} = "
            f"{b['fraction_minus_I']*100:5.1f}%  (smooth {b['fraction_minus_I_smooth']*100:4.1f}%)  "
            f"4π→+I:{b['double_cover_consistent']}"
        )

    f_native = runs["NATIVE screw 4₁ (κ>0)"]["fraction_minus_I"]
    f_achiral = runs["achiral_1st+2nd (matched control)"]["fraction_minus_I"]

    # ── Path-dependence map (structured grid) ─────────────────────────────────
    print("\n--- PATH-DEPENDENCE MAP (orbit-plane θ×ψ grid, native screw, r=1.0) ---")
    pmap = path_dependence_map(+KAPPA, screw_axis, pos2, home2, r=1.0)
    print(
        f"  grid f(−I) = {pmap['fraction_minus_I_grid']*100:.1f}%  | all−I:{pmap['all_minus_I']} "
        f"all+I:{pmap['all_plus_I']} both:{pmap['both_signs_present']}  min_gap={pmap['min_gap_overall']:.3f}"
    )

    # ── Robustness (Z₂ ⇒ pitch- & axis-independent) ───────────────────────────
    print("\n--- PITCH ROBUSTNESS (Z₂ depends on sign κ, not magnitude) ---")
    pr = pitch_robustness(
        screw_axis,
        pos2,
        home2,
        n_paths=200,
        kappas=[0.0, np.pi / 4, 3 * np.pi / 8, np.pi / 2, 7 * np.pi / 12, 2 * np.pi / 3, 3 * np.pi / 4, np.pi],
    )
    for row in pr:
        print(f"  κ={row['kappa']:+.4f}: f(−I)={row['fraction_minus_I']*100:5.1f}%")
    print("\n--- AXIS INDEPENDENCE (4₁ along all 3 cubic ⟨100⟩) ---")
    ax_ind = axis_independence(pos2, home2, +KAPPA)
    for nm, fr in ax_ind.items():
        print(f"  screw ∥ {nm}̂: f(−I)={fr*100:5.1f}%")

    # ── Verdict logic ─────────────────────────────────────────────────────────
    if f_native >= 0.95:
        verdict = "(I) PATH-INDEPENDENT — intrinsic spin-½ EMERGES (emergence-class)"
    elif f_native <= 0.02 and f_achiral <= 0.02:
        verdict = "(III) true screw removes the π entirely (clean negative on orbital mechanism)"
    else:
        verdict = "(II) PATH-DEPENDENT — projected helicity only (consistency-class)"
    print("\n" + "=" * 80)
    print(f"VERDICT: {verdict}")
    print(f"  f_native(−I) = {f_native*100:.1f}%   f_achiral_matched = {f_achiral*100:.1f}%")
    print("=" * 80)

    payload = {
        "verdict": verdict,
        "f_native_minus_I": f_native,
        "f_achiral_matched_minus_I": f_achiral,
        "battery": {k: v for k, v in runs.items()},
        "path_dependence_map": {k: v for k, v in pmap.items() if k != "sign_grid"},
        "sign_grid_native_r1": pmap["sign_grid"],
        "pitch_robustness": pr,
        "axis_independence": ax_ind,
        "geometry": {
            "n_first_shell": len(pos1),
            "n_second_shell": int((shell2 == 2).sum()),
            "screw_axis": screw_axis.tolist(),
            "kappa_4_1": KAPPA,
        },
    }
    out_json = os.path.join(out_dir, "secondshell_screw_holonomy.json")
    with open(out_json, "w") as fh:
        json.dump(payload, fh, indent=2, default=float)
    print(f"\nNumbers → {out_json}")

    out_png = os.path.join(out_dir, "secondshell_screw_holonomy.png")
    make_visualisation(out_png, pos2, home2, shell2, screw_axis, KAPPA, pmap, pr, runs)
    print(f"Visual  → {out_png}")


if __name__ == "__main__":
    main()
