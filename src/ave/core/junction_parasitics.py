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


def connected_band_top_theta(f: float, s_L: float = 1.0, s_C: float = 1.0, n_scan: int = 200000) -> float:
    """Connected-band ceiling: the FIRST theta>0 (scanning up from the acoustic
    point theta=0, mu=+3) at which the descending mu(theta) reaches the adjacency
    floor mu=-3. The parasitic drives mu below -3 just under pi, OPENING a
    zone-edge stop-band, so the connected manifold tops out below the memoryless
    pi. f=0 recovers theta_top=pi exactly (memoryless). Pure geometry.
    """
    if f == 0.0:
        return float(np.pi)  # memoryless: mu = 3 cos t = -3 -> t = pi
    ts = np.linspace(1e-5, np.pi, n_scan)
    g = loaded_mu_of_theta(ts, f, s_L, s_C) - MU_FLOOR  # zero at mu = -3
    sign_change = np.where(np.sign(g[:-1]) != np.sign(g[1:]))[0]
    if len(sign_change) == 0:
        return float(np.pi)
    i = int(sign_change[0])  # FIRST crossing = connected-band ceiling
    return float(brentq(lambda t: loaded_mu_of_theta(t, f, s_L, s_C) - MU_FLOOR, ts[i], ts[i + 1]))


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
    """Read the topology class off the sign of the ceiling shift vs memoryless.

    LOW-PASS (pins ceiling DOWN) if the loaded ceiling < memoryless; BYPASS
    (lifts) if >; TRANSPARENT if equal to tolerance. Both accumulator and throat
    are reactive energy stores => LOW-PASS is the derivation-level expectation.
    """
    memoryless = OMEGA_LINK_OVER_OMEGA_C * np.pi
    loaded = g_scalar(f, s_L, s_C)
    rel = (loaded - memoryless) / memoryless
    if abs(rel) < 1e-9:
        return "transparent-at-top (parasitic -> 0)"
    if rel < 0.0:
        return "reactive-low-pass (accumulator+throat pin the ceiling DOWN; zone-edge gap opens)"
    return "parallel-bypass (ceiling LIFTS)"
