#!/usr/bin/env python3
"""X38 — srs vertex S₁₁ EXTRACTION + canonical Op6 bore selection (route d for the
bond-bore fork X37 sharpened). Does the substrate SELECT the junction extent f by
minimizing junction reflection, or not?

Prereg (FROZEN): research/2026-07-10_x38-s11-bore-selection_prereg_FROZEN.md
Derivation:      research/2026-07-10_x38-s11-bore-selection_derivation.md

═══════════════════════════════════════════════════════════════════════════════
THE ANTI-INSTALL BOUNDARY (G-A) — READ BEFORE EDITING
═══════════════════════════════════════════════════════════════════════════════
This module is THE S₁₁ EXTRACTION PATH. It is the code the G-A gate scans. It may
consume ONLY geometry:
    { L' = mu_0, C' = eps_0 (they CANCEL — see below), the coordination z (=3 srs),
      theta = omega*ell_node/c (dimensionless), the extent fraction f = d/ell_node,
      the shape factors s_L, s_C }
It MUST NOT import or reference any physical SCALE:
    FORBIDDEN: OMEGA_C, M_E, L_CELL, C_CELL, `from ave.core.constants import ...`,
    and any assignment setting 1/sqrt(L_j*C_j) == omega_C (the #613 INSTALL).

WHY THE EXTRACTION IS PURE GEOMETRY (dimensionless). The junction of extent
d = f*ell is a lump of the SAME medium: series throat L_j = s_L*mu_0*d (arms) and
shunt accumulator C_j = s_C*eps_0*d (node). S₁₁ depends on them ONLY through the
dimensionless products
    x = omega*L_j / Z_0  = s_L * f * (omega ell / c) = s_L*f*theta   (arm reactance / Z0)
    p = omega*C_j * Z_0  = s_C * f * (omega ell / c) = s_C*f*theta   (node susceptance * Z0)
so mu_0 and eps_0 CANCEL and ell folds into theta = omega/omega_C (a reporting
unit). This module imports NO scale from ave.core.constants.

THE OBJECTIVE IS CANON'S, NOT OURS. obj-1 uses Universal Operator #6
(`universal_operators.universal_eigenvalue_target`, lambda_min(S†S)->0,
manuscript/ave-kb/vol1/.../ch6-universal-operators/eigenvalue-target.md,
clm-gdd70j) — the SAME operator that selected the trefoil R.r=1/4
(constants.py:191-206). For the 1x1 reflection block it reduces to |S11|^2.
Importing that operator introduces NO physical scale (it is a linear-algebra
operator on the dimensionless S-block; the per-file G-A AST scan sees only the
Names/imports in THIS file).

CLASS: MIXED. The selected f* is derived-geometric (this module). The SCALE
omega_C = c/ell_node is dimensional-forced / identity, and lives only in the
driver's REPORTING layer — never here.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# CANONICAL Op6 evaluator ONLY (a linear-algebra operator on the dimensionless
# S-block — NOT a physical scale). This is the anti-install-clean way to compute
# obj-1 through canon's own code path (faithful to the trefoil R.r=1/4 usage).
from ave.core.universal_operators import universal_eigenvalue_target

# The srs vertex coordination (3 bonds per vertex, z = 3). GEOMETRY, not a scale.
SRS_COORDINATION = 3

# Extent-fraction sweep endpoints (GEOMETRY; canon fixes no bare-bond transverse
# scale, so f is not a canonical number — X37 branch iii). f=0 = point junction,
# f=0.5 = Wigner-Seitz upper bound. These are the argmin search bounds.
F_POINT_JUNCTION = 0.0
F_WIGNER_SEITZ = 0.5

# The band-top mode (mu = -3): theta = pi. The load-bearing ceiling mode X37/X33
# care about; obj-1 (Op6) is evaluated here. GEOMETRY of the srs graph.
THETA_BAND_TOP = np.pi
# The mid-band single frequency for obj-3 (robustness comparator).
THETA_MID_BAND = 0.5 * np.pi


# ─────────────────────────────────────────────────────────────────────────────
# The exact isolated-junction S₁₁ (symmetric z-port, matched far arms).
# Derivation §3:
#   x = s_L f theta,  p = s_C f theta
#   z_far  = 1 + j x                         (far arm: series throat then matched Z0 line)
#   y_node = (z-1)/z_far + j p               ((z-1) far arms in parallel + shunt accumulator)
#   z_in   = j x + 1/y_node                  (series throat on incident arm + node)
#   S11    = (z_in - 1)/(z_in + 1)
#   f->0 or theta->0 -> S11 = (2 - z)/z  (= -1/3 for z=3, the bare-junction baseline)
# All quantities normalized to Z0; mu_0/eps_0/ell CANCEL. Pure geometry.
# ─────────────────────────────────────────────────────────────────────────────
def s11_junction(theta, f: float, s_L: float = 1.0, s_C: float = 1.0, z: int = SRS_COORDINATION):
    """Complex S₁₁ of the symmetric z-port vertex loaded with the X37 parasitics.

    theta = omega*ell_node/c (dimensionless). Returns complex reflection (ndarray
    if theta is an array). Pure geometry — no physical scale.
    """
    t = np.asarray(theta, dtype=float)
    x = s_L * f * t  # arm series reactance / Z0
    p = s_C * f * t  # node shunt susceptance * Z0
    z_far = 1.0 + 1j * x
    y_node = (z - 1) / z_far + 1j * p
    z_in = 1j * x + 1.0 / y_node
    return (z_in - 1.0) / (z_in + 1.0)


def bare_junction_s11(z: int = SRS_COORDINATION) -> float:
    """Analytic memoryless-junction reflection S11 = (2 - z)/z (real). z=3 -> -1/3.

    The wave incident on one of z matched lines sees the other (z-1) in parallel,
    Z_load = Z0/(z-1), Gamma = (Z_load - Z0)/(Z_load + Z0) = (2-z)/z. Pure geometry.
    """
    return (2 - z) / z


# ─────────────────────────────────────────────────────────────────────────────
# The reflection OPERATOR block (for the canonical Op6 evaluator).
# The vertex-as-1-port reflection is the 1x1 matrix [S11]; the other (z-1) arms
# radiate power away, so the 1-port is NOT lossless and lambda_min(S†S)=|S11|^2
# CAN reach 0. (The FULL zxz S is unitary => lambda_min == 1, degenerate — the
# named ambiguity in prereg §4; NOT used as the objective.)
# ─────────────────────────────────────────────────────────────────────────────
def reflection_operator(theta: float, f: float, s_L: float = 1.0, s_C: float = 1.0, z: int = SRS_COORDINATION):
    """The 1x1 reflection block [S11(theta;f)] fed to the canonical Op6 operator."""
    return np.array([[s11_junction(theta, f, s_L, s_C, z)]], dtype=complex)


def op6_lambda_min(theta: float, f: float, s_L: float = 1.0, s_C: float = 1.0, z: int = SRS_COORDINATION) -> float:
    """Universal Operator #6 lambda_min(S†S) on the 1x1 reflection block = |S11|^2,
    computed through canon's own `universal_eigenvalue_target`. (eigenvalue-target.md,
    clm-gdd70j; the SAME operator that selected the trefoil R.r=1/4.)
    """
    return float(universal_eigenvalue_target(reflection_operator(theta, f, s_L, s_C, z)))


# ─────────────────────────────────────────────────────────────────────────────
# The three frozen objectives (prereg §4). obj-1 primary (canonical Op6);
# obj-2 band-integrated + obj-3 single-frequency are ROBUSTNESS COMPARATORS only.
# ─────────────────────────────────────────────────────────────────────────────
def objective_op6(f: float, s_L: float = 1.0, s_C: float = 1.0, z: int = SRS_COORDINATION) -> float:
    """obj-1 (PRIMARY, canonical Op6): J1(f) = lambda_min(S†S)|_{theta=pi} = |S11(pi;f)|^2.
    Evaluated at the band-top mode (mu=-3). Uses the canonical operator code path."""
    return op6_lambda_min(THETA_BAND_TOP, f, s_L, s_C, z)


def objective_band_integrated(
    f: float, s_L: float = 1.0, s_C: float = 1.0, z: int = SRS_COORDINATION, n: int = 4000
) -> float:
    """obj-2 (comparator): mean |S11|^2 over the connected band theta in (0, theta_top].
    theta_top is the loaded connected-band ceiling; at f=0 it is pi (memoryless)."""
    theta_top = connected_band_top_theta(f, s_L, s_C, z)
    ts = np.linspace(1e-6, theta_top, n)
    mags2 = np.abs(s11_junction(ts, f, s_L, s_C, z)) ** 2
    return float(np.trapezoid(mags2, ts) / theta_top)


def objective_single_freq(f: float, s_L: float = 1.0, s_C: float = 1.0, z: int = SRS_COORDINATION) -> float:
    """obj-3 (comparator): |S11(theta=pi/2; f)|^2 at fixed mid-band frequency."""
    return op6_lambda_min(THETA_MID_BAND, f, s_L, s_C, z)


# ─────────────────────────────────────────────────────────────────────────────
# The connected-band ceiling theta_top(f) — the FIRST theta where the loaded srs
# nodal-KCL dispersion mu(theta) reaches the adjacency floor mu=-3 (X37 physics),
# used to bound obj-2's integral. Reuses the X37 loaded-mu form (identical
# parasitics x,p) so obj-2 integrates over the physically connected band, not a
# fixed [0,pi]. Pure geometry. f=0 -> pi.
# ─────────────────────────────────────────────────────────────────────────────
def _loaded_mu_of_theta(theta, f: float, s_L: float, s_C: float, z: int):
    t = np.asarray(theta, dtype=float)
    x = s_L * f * t
    p = s_C * f * t
    a_dress = np.cos(t) - 0.5 * x * np.sin(t)
    b_dress = np.sin(t) + x * np.cos(t) - 0.25 * x * x * np.sin(t)
    return z * a_dress - p * b_dress


def connected_band_top_theta(
    f: float, s_L: float = 1.0, s_C: float = 1.0, z: int = SRS_COORDINATION, n: int = 40000
) -> float:
    """theta_top: first crossing of mu(theta) = -z from the acoustic point (theta=0).
    f=0 -> pi exactly (memoryless). Bounds obj-2's connected-band integral."""
    if f == 0.0:
        return float(np.pi)
    ts = np.linspace(1e-6, 1.2 * np.pi, n)
    g = _loaded_mu_of_theta(ts, f, s_L, s_C, z) + z  # zero at mu = -z
    sc = np.where(np.sign(g[:-1]) != np.sign(g[1:]))[0]
    if len(sc) == 0:
        return float(np.pi)  # no crossing below the cap -> fall back to memoryless edge
    i = int(sc[0])
    # linear interpolation of the crossing (adequate for an integration bound)
    t0, t1 = ts[i], ts[i + 1]
    g0, g1 = g[i], g[i + 1]
    return float(t0 - g0 * (t1 - t0) / (g1 - g0))


# ─────────────────────────────────────────────────────────────────────────────
# The bore selection: f* = argmin over f in [0, 0.5] of a given objective.
# BOUNDARY-INCLUSIVE grid search (f=0 is a candidate — X37 R3 no-early-return
# discipline for the analogous solver; the minimum here is EXPECTED at a boundary,
# so an interior optimizer that skips the endpoints would be a dead-actuator bug).
# ─────────────────────────────────────────────────────────────────────────────
OBJECTIVES = {
    "obj1_op6": objective_op6,
    "obj2_band_integrated": objective_band_integrated,
    "obj3_single_freq": objective_single_freq,
}


@dataclass(frozen=True)
class BoreSelection:
    """f* under one objective + the objective value there. Dimensionless geometry."""

    objective: str
    f_star: float
    j_at_f_star: float
    s_L: float
    s_C: float


def argmin_bore(
    objective: str, s_L: float = 1.0, s_C: float = 1.0, z: int = SRS_COORDINATION, n_grid: int = 501
) -> BoreSelection:
    """f* = argmin over f in [F_POINT_JUNCTION, F_WIGNER_SEITZ] of the named objective.
    Boundary-inclusive dense grid (f=0 IS a candidate). Pure geometry."""
    fn = OBJECTIVES[objective]
    fs = np.linspace(F_POINT_JUNCTION, F_WIGNER_SEITZ, n_grid)
    js = np.array([fn(f, s_L, s_C, z) for f in fs])
    i = int(np.argmin(js))
    return BoreSelection(objective=objective, f_star=float(fs[i]), j_at_f_star=float(js[i]), s_L=s_L, s_C=s_C)


def objective_spread(s_L: float = 1.0, s_C: float = 1.0, z: int = SRS_COORDINATION, n_grid: int = 501) -> dict:
    """The branch-(iv) detector (G-C): f* under all three frozen objectives + the
    spread max(f*)-min(f*). Small spread => robust selection; large => objective-
    dependent scatter (branch iv). Pure geometry."""
    sels = {name: argmin_bore(name, s_L, s_C, z, n_grid) for name in OBJECTIVES}
    fstars = {name: sel.f_star for name, sel in sels.items()}
    spread = max(fstars.values()) - min(fstars.values())
    return {"f_stars": fstars, "spread": float(spread), "selections": sels}


# ─────────────────────────────────────────────────────────────────────────────
# The deepest-notch diagnostic (the Op6 named-limitation, prereg §4 / derivation
# §5c): min over the band of |S11|^2. Pinned at the trivial theta->0 floor
# ((2-z)/z)^2 = 1/9 for ALL f => the reflectionless target lambda_min->0 is
# UNREACHABLE at the vertex (the z=3 intrinsic branch-backscatter). Diagnostic,
# NOT the objective. Pure geometry.
# ─────────────────────────────────────────────────────────────────────────────
def deepest_notch(f: float, s_L: float = 1.0, s_C: float = 1.0, z: int = SRS_COORDINATION, n: int = 40000) -> float:
    """min over theta in (0, 1.5 pi] of |S11(theta;f)|^2 (the closest the vertex gets
    to the Op6 reflectionless target at extent f). Pure geometry."""
    ts = np.linspace(1e-6, 1.5 * np.pi, n)
    return float(np.min(np.abs(s11_junction(ts, f, s_L, s_C, z)) ** 2))
