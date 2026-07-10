#!/usr/bin/env python3
"""X37 — srs vertex junction-parasitic EXTRACTION (the vertex equivalent circuit
DERIVED from bond geometry, not installed).

Prereg (FROZEN): research/2026-07-10_x37-junction-parasitics_prereg_FROZEN.md
Derivation:      research/2026-07-10_x37-junction-parasitics_derivation.md

═══════════════════════════════════════════════════════════════════════════════
THE ANTI-INSTALL BOUNDARY (G-A) — READ BEFORE EDITING
═══════════════════════════════════════════════════════════════════════════════
This module is THE EXTRACTION PATH. It is the code the G-A gate scans. It may
consume ONLY geometry:
    { L' = mu_0, C' = eps_0 (they CANCEL — see below), the 120-deg bond angles,
      the srs twist, ell_node as the bond length, the DERIVED extent d = f*ell }
It MUST NOT import or reference any physical SCALE:
    FORBIDDEN: OMEGA_C, M_E, L_CELL, C_CELL, and any assignment setting
    1/sqrt(L_j*C_j) == omega_C. That last one is the #613 INSTALL — the exact
    error X37 exists to avoid.

WHY THE EXTRACTION IS PURE GEOMETRY (dimensionless). The junction of extent
d = f*ell is a lump of the SAME medium: excess shunt capacitance C_j = s_C*eps_0*d
(the accumulator) and excess series inductance L_j = s_L*mu_0*d (the throat). The
loaded dispersion depends on the junction ONLY through the dimensionless products
    p = B*Z_0 = (omega C_j)(sqrt(mu_0/eps_0)) = s_C * f * (omega ell / c) = s_C*f*theta
    x = X*Y_0 = (omega L_j)(sqrt(eps_0/mu_0)) = s_L * f * (omega ell / c) = s_L*f*theta
so mu_0 and eps_0 CANCEL and ell folds into theta = omega/omega_C (a reporting
unit). This module therefore imports NO scale from ave.core.constants — only the
geometric network factor sqrt(3) = ell_link/ell for the srs (a Class-B geometric
manifestation, ANALYTIC_NETWORK_FACTOR), used to report g = omega_top/omega_C.

CLASS: MIXED. The g VALUE is derived-geometric (this module). The SCALE
omega_C = c/ell_node is dimensional-forced / identity, and lives only in the
driver's REPORTING layer — never here.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.optimize import brentq

# Geometric network factor ONLY (1/sqrt(3), Class-B manifestation). This is the
# srs graph geometry, NOT a physical scale: omega = omega_link * theta with
# omega_link/omega_C = 1/ANALYTIC_NETWORK_FACTOR = sqrt(3). Importing it keeps the
# sqrt(3) in one canonical place. NO scale (OMEGA_C/M_E/L_CELL/C_CELL) is imported.
from ave.core.chiral_lattice_dynamics import ANALYTIC_NETWORK_FACTOR

# omega_link / omega_C for the srs scalar channel = sqrt(3) (geometry, not a scale)
OMEGA_LINK_OVER_OMEGA_C = 1.0 / ANALYTIC_NETWORK_FACTOR

# The srs vertex coordination (3 bonds per vertex at 120 deg, z = 3). Geometry.
SRS_COORDINATION = 3

# Memoryless adjacency floor: the pi-mode eigenvalue of the srs Bloch adjacency.
# (mu in [-3, 3]; the band top sits at mu = -3.) Geometry of the srs graph.
MU_FLOOR = -float(SRS_COORDINATION)


# ─────────────────────────────────────────────────────────────────────────────
# Vertex extent (G-C): canon fixes NO transverse bond scale, so the extent
# fraction f = d/ell_node is not a canonical number. We expose the canon-faithful
# limit, the Wigner-Seitz upper-bound probe, and the swept range — all GEOMETRY.
# ─────────────────────────────────────────────────────────────────────────────
F_CANON_FAITHFUL = 0.0  # 1D-line bonds -> point junction -> parasitic -> 0
F_WIGNER_SEITZ = 0.5  # node "owns" the medium out to each bond midpoint (upper bound)


def vertex_extent_sweep(n: int = 26) -> np.ndarray:
    """Geometry-only sweep of the extent fraction f = d/ell_node over [0, 0.5].

    The junction has parasitics only because it has finite extent d where the
    three bond fields merge. Canon provides no transverse scale to pin f, so the
    ceiling's sensitivity to f is a first-class result (G-C). Pure geometry.
    """
    return np.linspace(F_CANON_FAITHFUL, F_WIGNER_SEITZ, n)


# ─────────────────────────────────────────────────────────────────────────────
# The extracted junction equivalent circuit (dimensionless descriptors).
# ─────────────────────────────────────────────────────────────────────────────
@dataclass(frozen=True)
class VertexCircuit:
    """The srs vertex equivalent circuit for the scalar/compression channel.

    All fields dimensionless (in ell_node / c / omega_C units); NO physical scale.
    """

    f: float  # extent fraction d/ell_node (geometry)
    s_L: float  # series-throat shape factor (O(1) geometry)
    s_C: float  # shunt-accumulator shape factor (O(1) geometry)
    L_j_over_Lprime_ell: float  # L_j / (mu_0 * ell_node) = s_L * f
    C_j_over_Cprime_ell: float  # C_j / (eps_0 * ell_node) = s_C * f
    omega_vertex_over_omega_C: float  # junction LC self-resonance 1/sqrt(L_j C_j)/omega_C


def extract_vertex_circuit(f: float, s_L: float = 1.0, s_C: float = 1.0) -> VertexCircuit:
    """Extract the vertex equivalent circuit from the merge-region geometry.

    C_j = s_C * eps_0 * d,  L_j = s_L * mu_0 * d,  d = f * ell_node. The junction
    self-resonance omega_vertex = 1/sqrt(L_j C_j) = c/(sqrt(s_L s_C) f ell) =
    omega_C/(sqrt(s_L s_C) f). Reported as a dimensionless RATIO to omega_C — the
    ratio is pure geometry (c and ell cancel into omega_C). No scale installed.
    """
    Lj = s_L * f  # in units of mu_0 * ell_node
    Cj = s_C * f  # in units of eps_0 * ell_node
    if Lj > 0.0 and Cj > 0.0:
        # omega_vertex/omega_C = 1/sqrt((L_j/mu_0 ell)(C_j/eps_0 ell)) since
        # 1/sqrt(mu_0 eps_0)/ell = c/ell = omega_C (cancels; pure ratio).
        w_vertex = 1.0 / np.sqrt(Lj * Cj)
    else:
        w_vertex = np.inf  # point junction: no resonance (memoryless)
    return VertexCircuit(
        f=f,
        s_L=s_L,
        s_C=s_C,
        L_j_over_Lprime_ell=Lj,
        C_j_over_Cprime_ell=Cj,
        omega_vertex_over_omega_C=w_vertex,
    )


# ─────────────────────────────────────────────────────────────────────────────
# The loaded dispersion (EXACT lumped-equivalent ABCD, no truncation).
# Dressed bond = [series X/2] - [line theta] - [series X/2], shunt jB at node.
#   A_dress = cos t - (x/2) sin t
#   B_dress = j Z0 ( sin t + x cos t - (x^2/4) sin t )
#   KCL Bloch:  mu = 3 A_dress + j B_shunt B_dress
#            = 3[cos t - (x/2) sin t] - p[ sin t + x cos t - (x^2/4) sin t ]
# with x = s_L f t, p = s_C f t.  (f->0 -> mu = 3 cos t -> memoryless arccos map.)
# ─────────────────────────────────────────────────────────────────────────────
def loaded_mu_of_theta(theta, f: float, s_L: float = 1.0, s_C: float = 1.0):
    """mu(theta) of the loaded srs nodal-KCL dispersion. Pure geometry."""
    t = np.asarray(theta, dtype=float)
    x = s_L * f * t  # = X * Y_0 (dimensionless)
    p = s_C * f * t  # = B * Z_0 (dimensionless)
    A_dress = np.cos(t) - 0.5 * x * np.sin(t)
    B_dress = np.sin(t) + x * np.cos(t) - 0.25 * x * x * np.sin(t)
    return 3.0 * A_dress - p * B_dress


# Scan the bond electrical length PAST the memoryless zone edge (pi) so that a
# LIFT (ceiling ABOVE the memoryless top) is VISIBLE, not clipped. (Adversarial
# review R3: a [0, pi] scan structurally cannot report a lift.) A low-pass ceiling
# still lands at its first crossing < pi; a lift/bypass lands > pi.
THETA_MAX_SCAN = 1.5 * np.pi


def band_ceiling_diagnosis(f: float, s_L: float = 1.0, s_C: float = 1.0, n_scan: int = 200000) -> dict:
    """Diagnose the connected-band ceiling with an HONEST, lift-visible detector.

    Scans mu(theta) from the acoustic point (theta=0, mu=+3) up to THETA_MAX_SCAN
    (> pi) for the FIRST crossing of the adjacency floor mu=-3 (the connected-band
    ceiling). Returns a status that CAN report a lift:
      'memoryless'          f=0 (theta_top=pi exactly);
      'low-pass'            first crossing < pi   (ceiling pinned DOWN);
      'transparent'         first crossing == pi  (to tol);
      'lift'                first crossing > pi    (ceiling LIFTED above memoryless);
      'no-crossing'         no crossing <= THETA_MAX_SCAN (mu never reaches the
                            floor -> lift candidate; ceiling at/above the scan cap);
      'unresolved-thin-dip' mu dips below the floor but the crossing could not be
                            resolved even after local refinement (small-f razor dip).
    Pure geometry. This replaces the old [0, pi]-clipped scan (review R3).
    """
    if f == 0.0:
        return {"theta_top": float(np.pi), "status": "memoryless"}

    def _mu_floor(t):
        return loaded_mu_of_theta(t, f, s_L, s_C) - MU_FLOOR  # zero at mu = -3

    def _first_crossing(t_arr):
        vals = _mu_floor(t_arr)
        sc = np.where(np.sign(vals[:-1]) != np.sign(vals[1:]))[0]
        if len(sc) == 0:
            return None
        i = int(sc[0])
        return float(brentq(_mu_floor, t_arr[i], t_arr[i + 1]))

    # Pass 1: coarse scan PAST pi (lift-visible). Catches well-resolved dips
    # (low-pass, first crossing < pi) AND lifts (first crossing > pi).
    ts = np.linspace(1e-5, THETA_MAX_SCAN, n_scan)
    theta = _first_crossing(ts)

    # Pass 2 (resolution guard, review R3): a small-f zone-edge dip is both THIN
    # (width ~ kappa*f*pi) and SHALLOW (depth ~ f^2), so it can fall entirely
    # between coarse grid points -> gmin stays > 0 and the naive guard never fires,
    # silently mis-reading a negligible low-pass drop as a lift. So ALWAYS re-scan
    # the neighbourhood of the memoryless zone edge theta=pi at high density before
    # concluding "no crossing". (The physical dip for a passive loading sits just
    # below pi, since mu(pi) = -3 + s_L s_C f^2 pi^2 >= -3.)
    if theta is None:
        edge = np.linspace(np.pi - 0.2, np.pi + 1e-6, 300000)
        theta = _first_crossing(edge)

    if theta is None:
        # Genuinely no crossing anywhere up to the scan cap. Distinguish a tangent
        # touch (mu grazes the floor at pi -> transparent/memoryless-to-tol) from a
        # true lift (mu stays clear of the floor -> ceiling at/above the cap).
        gmin = float(np.min(_mu_floor(ts)))
        if abs(_mu_floor(np.pi)) < 1e-9 or gmin < 1e-9:
            return {"theta_top": float(np.pi), "status": "transparent"}
        return {"theta_top": float(THETA_MAX_SCAN), "status": "no-crossing", "min_floor_margin": gmin}

    tol = 1e-6
    if theta < np.pi - tol:
        status = "low-pass"
    elif theta > np.pi + tol:
        status = "lift"
    else:
        status = "transparent"
    return {"theta_top": theta, "status": status}


def connected_band_top_theta(f: float, s_L: float = 1.0, s_C: float = 1.0, n_scan: int = 200000) -> float:
    """Connected-band ceiling theta_top (the FIRST mu=-3 crossing from the acoustic
    branch). Thin wrapper over band_ceiling_diagnosis (lift-visible). Pure geometry.
    """
    return band_ceiling_diagnosis(f, s_L, s_C, n_scan)["theta_top"]


def g_scalar(f: float, s_L: float = 1.0, s_C: float = 1.0) -> float:
    """g_scalar = omega_top / omega_C = sqrt(3) * theta_top for the loaded srs
    scalar band. sqrt(3) is the geometric network factor (reporting), NOT a scale.
    """
    return OMEGA_LINK_OVER_OMEGA_C * connected_band_top_theta(f, s_L, s_C)


def g_scalar_linear(f: float, s_L: float = 1.0, s_C: float = 1.0) -> float:
    """SINGLE-CHANNEL analytic anchor: g = pi*sqrt(3)*(1 - kappa f),
    kappa = s_L + (2/3) s_C, from the local-mu linearization mu = 3 cos t -
    f t (3 s_L/2 + s_C) sin t. Pure geometry.

    VALID (exact-matching as f->0) for a SINGLE active channel — pure shunt-C
    (s_L=0) OR pure series-L (s_C=0). It is NON-ADDITIVE when BOTH channels are
    on: the connected-band ceiling is set by the FIRST mu=-3 crossing, and the
    re-entrant zone-edge gap (opened once s_C>0) absorbs the shunt contribution
    ABOVE that crossing, so the combined ceiling slope equals the STRONGER
    channel's slope, not the sum. Use the exact g_scalar() for the combined case;
    this anchor is the per-channel validation curve (derivation §4a).
    """
    kappa = s_L + (2.0 / 3.0) * s_C
    return OMEGA_LINK_OVER_OMEGA_C * np.pi * (1.0 - kappa * f)


def topology_class(f: float, s_L: float = 1.0, s_C: float = 1.0) -> str:
    """Read the topology class off the lift-visible ceiling diagnosis (review R3).

    Reports LOW-PASS / TRANSPARENT / LIFT (parallel-bypass) / unresolved. A LIFT
    is now REACHABLE (the detector scans past pi): e.g. a NEGATIVE-reactance
    (non-passive) loading lifts the ceiling and is reported as a bypass. For the
    passive positive-element class (s_L, s_C > 0) every stored-energy channel
    LOWERS the ceiling, so LOW-PASS is what the passive class gives.

    IMPORTANT SCOPE (review R1): this is the topology class of the leading-order
    POSITIVE two-element lumped equivalent; a fuller vertex model (evanescent-mode
    stub / finite junction volume = a resonant shunt branch) is NOT excluded and
    could present a bypass. The "no lift" statement holds only within this class.
    """
    status = band_ceiling_diagnosis(f, s_L, s_C)["status"]
    if status in ("memoryless", "transparent"):
        return "transparent-at-top (parasitic -> 0 or exactly memoryless)"
    if status == "low-pass":
        return (
            "reactive-low-pass (positive-element class: stored-energy channels "
            "pin the ceiling DOWN; zone-edge gap opens)"
        )
    if status in ("lift", "no-crossing"):
        return "parallel-bypass (ceiling LIFTS above memoryless)"
    return "unresolved (thin zone-edge dip — refine the scan)"


# ─────────────────────────────────────────────────────────────────────────────
# 1D two-node loaded line — the exactly-solvable closed-form cross-check the
# prereg §3.4 promised (adversarial review R2). z=2 monatomic chain, one node per
# cell (series X/2 both bond ends + shunt jB at the node), Bloch via the transfer-
# matrix trace. CLOSED FORM:
#     cos(k a) = (1 - p x / 2) cos(theta) - ((x + p)/2) sin(theta),
#     x = s_L f theta,  p = s_C f theta.
# f=0 -> cos(k a) = cos(theta) -> memoryless 1D top at theta=pi (g_1d = pi omega_C;
# NO sqrt(3) network factor for the 1D chain). Same junction physics as the srs,
# so it validates the srs numerics on a hand-checkable model. Pure geometry.
# ─────────────────────────────────────────────────────────────────────────────
def loaded_cos_ka_1d(theta, f: float, s_L: float = 1.0, s_C: float = 1.0):
    """Closed-form Bloch cos(k a) of the 1D loaded line (transfer-matrix trace/2)."""
    t = np.asarray(theta, dtype=float)
    x = s_L * f * t
    p = s_C * f * t
    return (1.0 - 0.5 * p * x) * np.cos(t) - 0.5 * (x + p) * np.sin(t)


def band_top_1d(f: float, s_L: float = 1.0, s_C: float = 1.0, n_scan: int = 200000) -> float:
    """1D connected-band top theta_top: FIRST theta where the closed-form cos(k a)
    crosses -1 (the acoustic-branch zone edge). f=0 -> pi. g_1d = theta_top (omega_C
    units). The exactly-solvable cross-check for the srs first-crossing logic.
    """
    if f == 0.0:
        return float(np.pi)
    ts = np.linspace(1e-5, THETA_MAX_SCAN, n_scan)
    h = loaded_cos_ka_1d(ts, f, s_L, s_C) + 1.0  # zero at cos(k a) = -1
    sc = np.where(np.sign(h[:-1]) != np.sign(h[1:]))[0]
    if len(sc) == 0:
        return float(THETA_MAX_SCAN)  # no zone edge <= scan cap -> lift candidate
    i = int(sc[0])
    return float(brentq(lambda t: loaded_cos_ka_1d(t, f, s_L, s_C) + 1.0, ts[i], ts[i + 1]))
