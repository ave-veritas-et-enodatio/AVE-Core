#!/usr/bin/env python3
"""
α-as-TWIST test: the per-revolution cross-section twist (Calugareanu-White framing
Tw in Lk = Tw + Wr) of the (2,3) flux tube, computed ALPHA-FREE.

Grant's framing: α = how much the 2-D cross-section of the (2,3) flux tube TURNS PER
REVOLUTION = the framing / self-linking twist Tw on the (V_inc, V_ref) Clifford torus
(phase-space). DISTINCT from the Golden-Torus mode-count (4π³+π²+π, a vol/surf/line
MEASURE); Tw is the FRAMING (a rotation/holonomy) on the same (2,3) torus.

Computes Tw alpha-free in TWO coordinate systems:
  A) PHASE-SPACE  : flat Clifford torus in R⁴ = C²  (load-bearing; corpus claim lives here)
  B) REAL-SPACE   : torus of revolution in R³        (diagnostic shadow)
for the Golden Torus (R=φ/2, r=(φ-1)/2, R·r=1/4) and a generic (2,3) control torus.

ALPHA / ALPHA_COLD_INV are imported COMPARISON-ONLY (final block), never as inputs.
See research/2026-06-07_alpha-twist-framing-test.md for the frozen pre-reg + circularity
guard + adjudication criteria.

Reference: manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md
           manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md
"""

import json
import os

import numpy as np

# Canonical-source COMPARISON-ONLY imports (never inputs to Tw):
from ave.core.constants import ALPHA, ALPHA_COLD_INV, PHI, RR_GOLDEN_TORUS

# Canonical-source verification (ave-canonical-source Step 4):
import ave.core.constants as _avc

assert _avc.__file__.endswith("ave/core/constants.py"), \
    "ave.core.constants is not the AVE-Core canonical source"
assert abs(RR_GOLDEN_TORUS - 0.25) < 1e-9, "R·r != 1/4 — golden torus constant drift"

PI = np.pi


# ═══════════════════════════════════════════════════════════════════════════
# Spectral (FFT) periodic derivatives — exact for smooth closed curves
# ═══════════════════════════════════════════════════════════════════════════
def dperiodic(f, order=1):
    """k-th derivative wrt t of a function sampled on a uniform [0,2π) grid."""
    n = f.shape[0]
    k = np.fft.fftfreq(n, d=1.0 / n)  # integer wavenumbers
    fk = np.fft.fft(f, axis=0)
    factor = (1j * k) ** order
    if f.ndim == 2:
        factor = factor[:, None]
    return np.real(np.fft.ifft(factor * fk, axis=0))


# ═══════════════════════════════════════════════════════════════════════════
# Geometric primitives (ALPHA-FREE: inputs are only p, q, R, r, π)
# ═══════════════════════════════════════════════════════════════════════════
def frenet_torsion_total(gamma, t):
    """∮ τ ds  (total torsion) and (1/2π)∮ τ ds (Frenet twist, in turns)."""
    d1 = dperiodic(gamma, 1)
    d2 = dperiodic(gamma, 2)
    d3 = dperiodic(gamma, 3)
    cross = np.cross(d1, d2)
    cross_norm2 = np.sum(cross * cross, axis=1)
    triple = np.sum(cross * d3, axis=1)
    tau = triple / cross_norm2  # torsion (per unit t-scaling cancels in τ·|γ'|)
    speed = np.linalg.norm(d1, axis=1)
    dt = t[1] - t[0]
    total_torsion = np.sum(tau * speed) * dt  # ∮ τ ds
    return total_torsion, total_torsion / (2 * PI)


def writhe_gauss(gamma, t):
    """Writhe via the Gauss double integral (R³ only). Diagonal i=j skipped."""
    d1 = dperiodic(gamma, 1)
    dt = t[1] - t[0]
    n = gamma.shape[0]
    # tangent-weighted: contribution_ij = (ri-rj)·(Ti×Tj)/|ri-rj|³
    acc = 0.0
    for i in range(n):
        diff = gamma[i] - gamma  # (n,3)
        Tcross = np.cross(d1[i], d1)  # Ti × Tj  (n,3)
        num = np.sum(diff * Tcross, axis=1)
        dist = np.linalg.norm(diff, axis=1)
        dist[i] = np.inf  # skip self
        acc += np.sum(num / dist**3)
    return acc * dt * dt / (4 * PI)


def surface_framing_twist(gamma, U, t):
    """(1/2π)∮ (T̂ × Û)·dÛ/ds ds  for a unit normal framing field U(t). In turns."""
    d1 = dperiodic(gamma, 1)
    speed = np.linalg.norm(d1, axis=1)
    That = d1 / speed[:, None]
    Uds = dperiodic(U, 1)  # dU/dt
    dt = t[1] - t[0]
    integrand = np.sum(np.cross(That, U) * Uds, axis=1)  # (T̂×U)·dU/dt
    return np.sum(integrand) * dt / (2 * PI)


# ═══════════════════════════════════════════════════════════════════════════
# Embedding B — REAL-SPACE torus of revolution in R³  (diagnostic shadow)
# ═══════════════════════════════════════════════════════════════════════════
def realspace_curve(p, q, R, r, n):
    t = np.linspace(0.0, 2 * PI, n, endpoint=False)
    phi, psi = p * t, q * t
    A = R + r * np.cos(psi)
    gamma = np.column_stack([A * np.cos(phi), A * np.sin(phi), r * np.sin(psi)])
    # outward tube-surface normal (unit): radial from centerline circle
    U = np.column_stack([np.cos(psi) * np.cos(phi), np.cos(psi) * np.sin(phi), np.sin(psi)])
    return t, gamma, U


# ═══════════════════════════════════════════════════════════════════════════
# Embedding A — PHASE-SPACE flat Clifford torus in R⁴ = C²  (load-bearing)
# ═══════════════════════════════════════════════════════════════════════════
def phasespace_curve(p, q, R, r, n):
    t = np.linspace(0.0, 2 * PI, n, endpoint=False)
    phi, psi = p * t, q * t
    gamma = np.column_stack([R * np.cos(phi), R * np.sin(phi), r * np.cos(psi), r * np.sin(psi)])
    # torus surface normals in R⁴ (the cross-section / normal-plane directions):
    n1 = np.column_stack([np.cos(phi), np.sin(phi), np.zeros(n), np.zeros(n)])  # V_inc radial
    n2 = np.column_stack([np.zeros(n), np.zeros(n), np.cos(psi), np.sin(psi)])  # V_ref radial
    return t, gamma, n1, n2


def phasespace_framing_twist(p, q, R, r, n):
    """
    R⁴ normal-plane framing twist of the (p,q) geodesic on the flat Clifford torus.

    The cross-section disk lives in the 2-plane span(n1, n2) (the two torus-surface
    normals, one per C-factor). The framing twist = total rotation rate of that
    2-frame within the normal bundle, integrated, in turns. n1 rotates by Δφ=2πp in
    the (x1,x2)-plane, n2 by Δψ=2πq in the (x3,x4)-plane.
    """
    t, gamma, n1, n2 = phasespace_curve(p, q, R, r, n)
    dt = t[1] - t[0]
    # rotation rate of n1 within its own 2-plane = (n1 × n1')_z-analog = ω1 = p
    dn1 = dperiodic(n1, 1)
    dn2 = dperiodic(n2, 1)
    # signed planar rotation rate in each C-factor: rate = (a·b' - b·a')/(a²+b²)
    # n1 lives in components 0,1; n2 in 2,3
    a1, b1 = n1[:, 0], n1[:, 1]
    da1, db1 = dn1[:, 0], dn1[:, 1]
    rate1 = (a1 * db1 - b1 * da1) / (a1**2 + b1**2)  # = p
    a2, b2 = n2[:, 2], n2[:, 3]
    da2, db2 = dn2[:, 2], dn2[:, 3]
    rate2 = (a2 * db2 - b2 * da2) / (a2**2 + b2**2)  # = q
    turns_n1 = np.sum(rate1) * dt / (2 * PI)
    turns_n2 = np.sum(rate2) * dt / (2 * PI)
    return turns_n1, turns_n2  # ≈ p, q (full turns each over the whole knot)


# ═══════════════════════════════════════════════════════════════════════════
# Driver
# ═══════════════════════════════════════════════════════════════════════════
def analyze(label, p, q, R, r, n_torsion=20000, n_writhe=1600):
    res = {"label": label, "p": p, "q": q, "R": R, "r": r, "Rr": R * r}

    # --- Embedding B: REAL-SPACE (R³) ---
    t, gamma3, U = realspace_curve(p, q, R, r, n_torsion)
    tt_total, tw_frenet = frenet_torsion_total(gamma3, t)
    tw_surf = surface_framing_twist(gamma3, U, t)
    # writhe on a coarser grid (O(N²)):
    tw_, gw, _ = realspace_curve(p, q, R, r, n_writhe)
    wr = writhe_gauss(gw, tw_)
    sl_pohl = wr + tw_frenet
    lk_surf_check = wr + tw_surf  # should ≈ pq
    res["realspace"] = {
        "writhe_Wr": wr,
        "total_torsion": tt_total,
        "twist_frenet_turns": tw_frenet,
        "twist_surface_turns": tw_surf,
        "pohl_self_linking_SL": sl_pohl,
        "Lk_surface_check_Wr_plus_Twsurf": lk_surf_check,
        "pq_topological": p * q,
        # per-revolution normalizations (÷ p toroidal revolutions):
        "Twsurf_per_rev_turns": tw_surf / p,
        "Twsurf_per_rev_rad": tw_surf / p * 2 * PI,
        "Twsurf_per_rev_deg": tw_surf / p * 360.0,
        "TwFrenet_per_rev_turns": tw_frenet / p,
        "TwFrenet_per_rev_rad": tw_frenet / p * 2 * PI,
        "Wr_per_rev_turns": wr / p,
        # integer-defect candidates (Tw = N + ε, ε ~ α?):
        "Twsurf_defect_from_nearest_int": tw_surf - round(tw_surf),
        "Wr_defect_from_nearest_int": wr - round(wr),
        "SL_defect_from_nearest_int": sl_pohl - round(sl_pohl),
    }

    # --- Embedding A: PHASE-SPACE (R⁴ flat Clifford torus) — LOAD-BEARING ---
    turns_n1, turns_n2 = phasespace_framing_twist(p, q, R, r, n_torsion)
    # natural winding-ratio twist: poloidal advance per toroidal revolution
    winding_twist_per_rev_turns = q / p  # cross-section turns per toroidal revolution
    res["phasespace"] = {
        "framing_turns_Vinc_axis": turns_n1,   # ≈ p
        "framing_turns_Vref_axis": turns_n2,   # ≈ q
        "self_linking_pq": p * q,              # topological (Hopf)
        "winding_twist_per_rev_turns": winding_twist_per_rev_turns,  # q/p
        "winding_twist_per_rev_rad": winding_twist_per_rev_turns * 2 * PI,
        "winding_twist_per_rev_deg": winding_twist_per_rev_turns * 360.0,
        "note": "flat torus: geodesic, no R³ writhe; twist is the winding ratio q/p",
    }
    return res


def adjudicate(res):
    """COMPARISON-ONLY block: compare every reported twist to α-targets."""
    targets = {
        "alpha_rad": ALPHA,                 # 0.0072974
        "inv137_dimensionless": 1.0 / 137,  # 0.0072993
        "inv137_turn_rad": 2 * PI / 137,    # 0.045862
        "alpha_cold_inv": ALPHA_COLD_INV,   # 137.0363 (the mode-count)
    }
    # collect all numeric twist quantities (per-rev, in rad/turns) for scan
    candidates = {}
    rs = res["realspace"]
    ps = res["phasespace"]
    for k in ("Twsurf_per_rev_rad", "TwFrenet_per_rev_rad", "Twsurf_per_rev_turns",
              "Wr_per_rev_turns", "Twsurf_defect_from_nearest_int",
              "Wr_defect_from_nearest_int"):
        candidates[f"realspace.{k}"] = rs[k]
    for k in ("winding_twist_per_rev_rad", "winding_twist_per_rev_turns"):
        candidates[f"phasespace.{k}"] = ps[k]

    hits = []
    for cname, cval in candidates.items():
        for tname, tval in targets.items():
            if tval == 0:
                continue
            rel = abs(cval - tval) / abs(tval)
            if rel < 0.01:
                hits.append({"candidate": cname, "cval": cval, "target": tname,
                             "tval": tval, "rel_err": rel})
    # loss-tangent identity (the NON-independent 1/Q route, reported explicitly):
    loss_tangent_if_Q_is_modecount = 1.0 / ALPHA_COLD_INV  # = α_cold, trivially
    return {
        "targets": targets,
        "candidates_scanned": candidates,
        "hits_within_1pct": hits,
        "loss_tangent_1_over_modecount": loss_tangent_if_Q_is_modecount,
        "loss_tangent_note": "1/(4π³+π²+π) = α_cold by definition of Q=mode-count; "
                             "NOT an independent twist-geometry derivation (see prereg §2)",
    }


def main():
    out = {
        "test": "alpha-as-twist (Calugareanu-White framing Tw of the (2,3) flux tube)",
        "date": "2026-06-07",
        "alpha_free_inputs": {"p": 2, "q": 3, "R_golden": PHI / 2, "r_golden": (PHI - 1) / 2,
                              "Rr": (PHI / 2) * ((PHI - 1) / 2)},
        "comparison_only_constants": {"ALPHA": ALPHA, "ALPHA_COLD_INV": ALPHA_COLD_INV},
        "geometries": {},
    }
    cases = [
        ("golden_torus_(2,3)", 2, 3, PHI / 2.0, (PHI - 1.0) / 2.0),
        ("generic_torus_(2,3)_R1_r0.3", 2, 3, 1.0, 0.3),
        ("generic_torus_(2,3)_R1_r0.5", 2, 3, 1.0, 0.5),
    ]
    for label, p, q, R, r in cases:
        res = analyze(label, p, q, R, r)
        res["adjudication"] = adjudicate(res)
        out["geometries"][label] = res
        print(f"\n=== {label} (R={R:.4f}, r={r:.4f}, R·r={R*r:.4f}) ===")
        rs, ps = res["realspace"], res["phasespace"]
        print(f"  REAL-SPACE  Wr={rs['writhe_Wr']:.5f}  Tw_surf={rs['twist_surface_turns']:.5f}"
              f"  (Wr+Tw_surf={rs['Lk_surface_check_Wr_plus_Twsurf']:.4f} vs pq={p*q})")
        print(f"              Tw_Frenet={rs['twist_frenet_turns']:.5f}  SL_Pohl={rs['pohl_self_linking_SL']:.4f}")
        print(f"              Tw_surf/rev = {rs['Twsurf_per_rev_turns']:.5f} turns "
              f"= {rs['Twsurf_per_rev_rad']:.5f} rad = {rs['Twsurf_per_rev_deg']:.3f}°")
        print(f"  PHASE-SPACE framing turns (Vinc,Vref)=({ps['framing_turns_Vinc_axis']:.4f},"
              f"{ps['framing_turns_Vref_axis']:.4f})  self-link pq={ps['self_linking_pq']}")
        print(f"              winding twist/rev = {ps['winding_twist_per_rev_turns']:.5f} turns "
              f"= {ps['winding_twist_per_rev_rad']:.5f} rad = {ps['winding_twist_per_rev_deg']:.3f}°")
        if res["adjudication"]["hits_within_1pct"]:
            print(f"  *** α-HITS (<1%): {res['adjudication']['hits_within_1pct']}")
        else:
            print(f"  no twist normalization within 1% of α / 1-137 / 1-137-turn")

    print(f"\nα (CODATA, comparison-only) = {ALPHA:.7f} rad = {ALPHA*360/(2*PI):.5f}°")
    print(f"1/137 = {1/137:.7f}   1/137-turn = {2*PI/137:.7f} rad")
    print(f"mode-count α_cold⁻¹ = {ALPHA_COLD_INV:.5f}  (the DISTINCT vol/surf/line measure)")

    here = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.abspath(os.path.join(here, "..", "..", ".."))
    outpath = os.path.join(repo, "research", "2026-06-07_alpha-twist-framing-result.json")
    with open(outpath, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nwrote {outpath}")


if __name__ == "__main__":
    main()
