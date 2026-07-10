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

THE OBJECTIVE IS CANON'S, applied HERE as a CANDIDATE selector. obj-1 uses
Universal Operator #6 (`universal_operators.universal_eigenvalue_target`,
lambda_min(S†S)->0, manuscript/ave-kb/vol1/.../ch6-universal-operators/
eigenvalue-target.md, clm-gdd70j). For the 1x1 reflection block it reduces to
|S11|^2. Importing that operator introduces NO physical scale (linear-algebra on
the dimensionless S-block; the per-file G-A AST scan sees only THIS file).
  R6 CORRECTION (PR #619 review): the earlier claim that this is "the SAME
  operator that selected the trefoil R.r=1/4 (constants.py:191-206)" is WRONG per
  canon's OWN honest-scope note (constants.py, HONEST SCOPE 2026-06-14): the S11
  landscape was found FLAT in R.r and "S11 minimization does NOT select R.r=1/4."
  Op6 is here a CANDIDATE selector applied to the vertex; it did not select the
  trefoil geometry. (This mischaracterization entered via the orchestrator brief.)

RECIPROCITY SCOPE (R3, PR #619 review). Every result of this module — the 1/3
floor, the "no bore matches", the Op6-target-unreachable diagnostic — holds for
the LOSSLESS RECIPROCAL vertex class only (this s11_junction builds a reciprocal
L/C network). Matched lossless 3-ports DO exist NON-reciprocally (the ideal
circulator: unitary, C3-symmetric, S11=0). The lattice is chiral at Axiom-1 level
(right-handed I4_1 32, axiom-definitions.md:16) — parity-broken — but circulation
needs a TIME-REVERSAL-breaking bias (candidate: the frozen-bias sector
u0*/Omega_freeze), a PENDING-GRANT walk; this module asserts nothing there.

CLASS: MIXED. The selected f* is derived-geometric (this module). The SCALE
omega_C = c/ell_node is dimensional-forced / identity, and lives only in the
driver's REPORTING layer — never here.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# CANONICAL loaded srs dispersion (#616 merged): the connected-band ceiling that
# bounds obj-2 and recovers pi*sqrt3 (G-B) is the X37 routine, IMPORTED not
# re-implemented (R10, PR #619 review). junction_parasitics imports no physical
# scale (only the ANALYTIC_NETWORK_FACTOR geometry factor), so G-A stays clean.
from ave.core import junction_parasitics as _jp

# CANONICAL Op6 evaluator ONLY (a linear-algebra operator on the dimensionless
# S-block — NOT a physical scale). This is the anti-install-clean way to compute
# obj-1 through canon's own code path (Op6 as a candidate selector — R6).
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
    computed through canon's own `universal_eigenvalue_target` (eigenvalue-target.md,
    clm-gdd70j). Op6 is applied here as a CANDIDATE selector; per canon's own
    honest-scope note it did NOT select the trefoil geometry (R6, PR #619 review).
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


def connected_band_top_theta(f: float, s_L: float = 1.0, s_C: float = 1.0) -> float:
    """theta_top of the loaded connected band — the CANONICAL X37 routine, IMPORTED
    from ave.core.junction_parasitics (#616 merged; R10). f=0 -> pi. Bounds obj-2."""
    return _jp.connected_band_top_theta(f, s_L, s_C)


def objective_band_integrated(
    f: float, s_L: float = 1.0, s_C: float = 1.0, z: int = SRS_COORDINATION, n: int = 2000
) -> float:
    """obj-2 (comparator): mean |S11|^2 over the connected band theta in [0, theta_top].
    theta_top is the CANONICAL X37 connected-band ceiling (imported; R10); at f=0 it
    is pi. D4 FIX (PR #619 review): the integration LOWER BOUND is theta=0 EXACTLY
    (|S11(0)|^2 = ((2-z)/z)^2 is well defined), not 1e-6 — the earlier 1e-6 bound +
    theta_top-shrink produced a ~6e-10 integration-cutoff systematic that float-tied
    the argmin to f=0.010 at strong-accumulator cells. With the exact lower bound
    obj-2 is >1/9 for every f>0 (|S11|^2>=1/9, equality only at isolated points), so
    it uniquely and cleanly selects f*=0."""
    theta_top = connected_band_top_theta(f, s_L, s_C)
    ts = np.linspace(0.0, theta_top, n)
    mags2 = np.abs(s11_junction(ts, f, s_L, s_C, z)) ** 2
    return float(np.trapezoid(mags2, ts) / theta_top)


def objective_single_freq(f: float, s_L: float = 1.0, s_C: float = 1.0, z: int = SRS_COORDINATION) -> float:
    """obj-3 (comparator): |S11(theta=pi/2; f)|^2 at fixed mid-band frequency.
    A SINGLE-FREQUENCY objective -> shares the half-wave-invisible degeneracy
    (touches 1/9 at f=2*f_touch; R1). At s=1 that touch (0.900) is OUTSIDE [0,0.5]."""
    return op6_lambda_min(THETA_MID_BAND, f, s_L, s_C, z)


# ─────────────────────────────────────────────────────────────────────────────
# THE HALF-WAVE-INVISIBLE TOUCH (R1, PR #619 review — the load-bearing correction).
# Symbolically (sympy, perfect-square numerator):
#     |S11(theta;f)|^2 - 1/9 = 8 t^2 (s_C s_L^2 t^2 + s_C - 3 s_L)^2 / [...],  t = f*theta
# so |S11| touches the bare 1/3 floor EXACTLY (not just at theta->0) also at the
# finite extent where the junction section is HALF-WAVE at the probe tone:
#     f_touch(theta_probe) = sqrt((3 s_L - s_C)/s_C) / (s_L * theta_probe),   s_C < 3 s_L.
# A half-wave section is impedance-transparent AT that tone, so the bore is
# "invisible" there and |S11| returns to 1/3 -> the single-frequency objectives
# (obj-1 at pi, obj-3 at pi/2) are EXACTLY DEGENERATE along {0, f_touch}. This is a
# single-tone trick; broadband matching (obj-2) cannot use it. Pure geometry.
# ─────────────────────────────────────────────────────────────────────────────
def half_wave_invisible_touch(theta_probe: float, s_L: float = 1.0, s_C: float = 1.0) -> float:
    """The finite extent f>0 at which |S11(theta_probe;f)| = 1/3 EXACTLY (the junction
    is half-wave at theta_probe). Returns NaN when s_C >= 3 s_L (no real touch)."""
    disc = (3.0 * s_L - s_C) / s_C
    if disc <= 0.0:
        return float("nan")
    return float(np.sqrt(disc) / (s_L * theta_probe))


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


# Probe frequency of each objective (for the half-wave-invisible degeneracy test).
_OBJ_PROBE_THETA = {"obj1_op6": THETA_BAND_TOP, "obj3_single_freq": THETA_MID_BAND}


def objective_is_degenerate(objective: str, s_L: float = 1.0, s_C: float = 1.0) -> dict:
    """TWO-AXIS detector (R1, PR #619 review). A single-frequency objective is EXACTLY
    DEGENERATE if its half-wave-invisible touch f_touch lies inside the search domain
    (0, 0.5] — it then has co-equal global minima {0, f_touch} (both = 1/9), so it
    does NOT uniquely select f*=0 (the grid argmin lands on 0 only by resolution
    luck). The band-integrated obj-2 has no such touch (single-tone trick washed out
    by integration) -> it is the ONLY objective that uniquely selects f*=0. Pure geometry."""
    if objective == "obj2_band_integrated":
        return {"degenerate": False, "f_touch": float("nan"), "in_domain": False}
    theta_probe = _OBJ_PROBE_THETA[objective]
    f_touch = half_wave_invisible_touch(theta_probe, s_L, s_C)
    in_domain = bool(np.isfinite(f_touch) and F_POINT_JUNCTION < f_touch <= F_WIGNER_SEITZ)
    return {"degenerate": in_domain, "f_touch": f_touch, "in_domain": in_domain}


def objective_spread(s_L: float = 1.0, s_C: float = 1.0, z: int = SRS_COORDINATION, n_grid: int = 151) -> dict:
    """The branch-(iv) detector (G-C), TWO-AXIS (R1). Reports (a) each objective's grid
    argmin f* + the spread, AND (b) per-objective EXACT degeneracy (half-wave-invisible
    touch in domain). obj-1 (primary, single-freq at pi) is degenerate whenever
    f_touch(pi) in (0,0.5]; obj-2 (band-integrated) uniquely selects f*=0. Pure geometry."""
    sels = {name: argmin_bore(name, s_L, s_C, z, n_grid) for name in OBJECTIVES}
    fstars = {name: sel.f_star for name, sel in sels.items()}
    spread = max(fstars.values()) - min(fstars.values())
    degen = {name: objective_is_degenerate(name, s_L, s_C) for name in OBJECTIVES}
    return {
        "f_stars": fstars,
        "spread": float(spread),
        "selections": sels,
        "degeneracy": degen,
        "primary_degenerate": degen["obj1_op6"]["degenerate"],
        "band_integrated_unique_f0": bool(fstars["obj2_band_integrated"] == F_POINT_JUNCTION),
    }


# ─────────────────────────────────────────────────────────────────────────────
# The deepest-notch diagnostic (the Op6 named-limitation, prereg §4 / derivation
# §5c): min over the band of |S11|^2. Pinned at ((2-z)/z)^2 = 1/9 for ALL f => the
# reflectionless target lambda_min->0 is UNREACHABLE by any bore of the LOSSLESS
# RECIPROCAL vertex class (R3/R5) — the z=3 intrinsic reactive BACK-SCATTER /
# redistribution (R9: no dissipation, Ax3 lossless-reactive). This is the classic
# matched-lossless-reciprocal-3-port theorem (Pozar §7.1 class; |S11|>=1/3 symmetric
# corollary), confirmed at the vertex. Diagnostic, NOT the objective. Pure geometry.
# ─────────────────────────────────────────────────────────────────────────────
def deepest_notch(f: float, s_L: float = 1.0, s_C: float = 1.0, z: int = SRS_COORDINATION, n: int = 40000) -> float:
    """min over theta in (0, 1.5 pi] of |S11(theta;f)|^2 (the closest the LOSSLESS
    RECIPROCAL vertex gets to the Op6 reflectionless target at extent f). Pure geometry."""
    ts = np.linspace(1e-6, 1.5 * np.pi, n)
    return float(np.min(np.abs(s11_junction(ts, f, s_L, s_C, z)) ** 2))


# ─────────────────────────────────────────────────────────────────────────────
# The NON-RECIPROCAL escape (R3/R4, PR #619 review): matched lossless C3-symmetric
# 3-ports EXIST — but ONLY non-reciprocally. The ideal circulator is the witness;
# ANY lossless+reciprocal+C3 network (any complexity, incl. evanescent-stub /
# finite-volume resonant branches) obeys the 1/3 theorem, so the ONLY escape class
# is non-reciprocity, which needs a T-breaking bias (PENDING-GRANT). Pure algebra.
# ─────────────────────────────────────────────────────────────────────────────
def ideal_circulator_s_matrix() -> np.ndarray:
    """The ideal 3-port circulator S = [[0,0,1],[1,0,0],[0,1,0]]: unitary (lossless),
    C3-symmetric (cyclic), NON-reciprocal (S != S^T), S11 = 0 (matched). The witness
    that the 1/3 floor is a RECIPROCITY result, not a topology one."""
    return np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
