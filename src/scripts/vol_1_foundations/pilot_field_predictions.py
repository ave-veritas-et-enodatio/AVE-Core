"""SYMBOLIC PREDICTION MODULE — the pilot-field co-moving companion arc.

Derives the coefficients Grant's hypothesis predicts, SYMBOLICALLY (sympy where a
closed form exists; analytic series otherwise), on an INDEPENDENT code path from the
time-domain dynamics driver (`pilot_field_wavetrain.py`).

FROZEN prereg: research/2026-07-05_pilot-field-comoving-companion_prereg_FROZEN.md.

THE #531 TAUTOLOGY GUARD (binding): the dynamics driver MUST NOT import this module.
The #528 ReconcileGate compares the two modules' OUTPUTS only.

Grant's hypothesis (verbatim in the prereg): a photon carries a CO-MOVING 2nd-order
longitudinal contraction companion (du approx -dy^2/2 under the envelope, the
free-host reading realized LOCALLY), compensating stretch spread over the unoccupied
lattice, so the #534 fixed/free trichotomy demotes to closure-scale bookkeeping.

The derived quantities (all cited/derived from the #533/#534 backbone + the cold
shear dispersion):
  1. FREE-HOST CONTRACTION COEFFICIENT   du_local = sqrt(1-dy^2) - 1 ~ -<dy^2>/2   (the ~-1/2)
  2. <dy^2> = y0^2 (1 - cos k)                                      (traveling-wave phase avg)
  3. COLD SHEAR DISPERSION  omega^2 = k_s (2 - 2 cos k)  =>  k, and GROUP VELOCITY v_g = domega/dk
  4. COMPENSATING-STRETCH DILUTION  du_far ~ -<dy^2>/2 * (L_env / N)   (whole-loop closure Sum du = 0)
  5. LONGITUDINAL SOUND SPEED c_long(rho) and the SONIC RATIO c_long/v_g  (subsonic/sonic/supersonic)

CONSISTENCY-vs-EMERGENCE: CONSISTENCY / geometric-kinematic. No VALUE derived (the 1/2
is the convexity coefficient; 2/7, 9.7734, /7 stay GR-imported).

alpha-CLEAN: no physical constant on this path.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import sympy as sp

# Kernel-unit convention (same as #526/#529/#531/#532/#533/#534: k0=1, ell=1, k_a=k_s=1).
K0 = 1.0
ELL = 1.0
K_S = 1.0

# Read-off operating point (axiom-register.md:189 arc* tent band; #527/#529). NEVER tuned.
Y0_TENT = 0.1428
OMEGA_PUMP = 1.2       # #532 run pump_omega (read-off)


# ─────────────────────────────────────────────────────────────────────────────
# 1 + 2 — the free-host contraction coefficient and <dy^2>, sympy-derived.
# ─────────────────────────────────────────────────────────────────────────────
def free_contraction_series():
    """SYMBOLIC: the free-host per-bond contraction du = sqrt(1 - dy^2) - 1 Taylor
    series in dy. Returns (leading_coeff, next_coeff) = (-1/2, -1/8): du = -dy^2/2
    - dy^4/8 - ... The LEADING -1/2 is the #534 backbone convexity coefficient (the
    'du approx -dy^2/2' of Grant's hypothesis), DERIVED here, not asserted."""
    dy = sp.symbols("dy", real=True)
    du = sp.sqrt(1 - dy**2) - 1
    ser = sp.series(du, dy, 0, 6).removeO()
    poly = sp.Poly(ser, dy)
    c2 = poly.coeff_monomial(dy**2)   # -1/2
    c4 = poly.coeff_monomial(dy**4)   # -1/8
    return {"c_dy2": sp.nsimplify(c2), "c_dy4": sp.nsimplify(c4),
            "c_dy2_float": float(c2), "c_dy4_float": float(c4)}


def mean_dy2(y0: float = Y0_TENT, k: float | None = None,
             omega: float = OMEGA_PUMP, k_s: float = K_S) -> float:
    """<dy^2> = y0^2 (1 - cos k) for a traveling mode y = y0 sin(kj - wt), phase-avg.
    SYMBOLIC identity (#534 backbone R3), evaluated at the dispersion-set k."""
    if k is None:
        k = wave_number(omega, k_s)
    return float(y0**2 * (1.0 - np.cos(k)))


def free_host_local_depth(y0: float = Y0_TENT, k: float | None = None,
                          omega: float = OMEGA_PUMP, k_s: float = K_S) -> float:
    """The LOCAL free-host contraction depth du_local = -<dy^2>/2 (leading order) —
    the companion depth Grant's pilot picture predicts under the envelope. This is the
    prediction the numeric wavetrain's du_min is reconciled against (bin criterion 2)."""
    return float(-0.5 * mean_dy2(y0=y0, k=k, omega=omega, k_s=k_s))


# ─────────────────────────────────────────────────────────────────────────────
# 3 — the cold shear dispersion, carrier k, and GROUP velocity (co-motion reference).
# ─────────────────────────────────────────────────────────────────────────────
def wave_number(omega: float = OMEGA_PUMP, k_s: float = K_S, m: float = 1.0) -> float:
    """k from the cold transverse (shear-branch) dispersion. omega^2 = k_s(2-2cos k)
    => cos k = 1 - omega^2/(2 k_s/m). At omega=1.2, k_s=1, m=1: k = 1.28700."""
    return float(np.arccos(1.0 - omega**2 / (2.0 * k_s / m)))


def group_velocity(omega: float = OMEGA_PUMP, k_s: float = K_S, m: float = 1.0) -> float:
    """v_g = domega/dk for the cold shear branch omega = sqrt(k_s/m)*sqrt(2-2cos k)
    = 2 sqrt(k_s/m) |sin(k/2)|. SYMBOLIC derivative, evaluated at the carrier k.
    This is the speed the co-moving companion must track (co-motion reference)."""
    ksym, ks, mm = sp.symbols("k k_s m", positive=True)
    omega_sym = sp.sqrt(ks / mm) * sp.sqrt(2 - 2 * sp.cos(ksym))
    vg_sym = sp.diff(omega_sym, ksym)
    k = wave_number(omega, k_s, m)
    vg = float(vg_sym.subs({ksym: k, ks: k_s, mm: m}))
    return vg


def phase_velocity(omega: float = OMEGA_PUMP, k_s: float = K_S, m: float = 1.0) -> float:
    """v_phase = omega/k (cold shear branch)."""
    return float(omega / wave_number(omega, k_s, m))


# ─────────────────────────────────────────────────────────────────────────────
# 4 — the compensating-stretch dilution law (the whole-loop closure prediction).
# ─────────────────────────────────────────────────────────────────────────────
def compensating_stretch_amplitude(y0: float = Y0_TENT, l_env: float = 80.0,
                                    n_nodes: int = 1024, k: float | None = None,
                                    omega: float = OMEGA_PUMP, k_s: float = K_S,
                                    envelope_area_frac: float = 0.5) -> float:
    """The far-field mean STRETCH the whole-loop closure Sum du = 0 demands, spread over
    the (N - occupied) empty lattice. The wavetrain removes total length
    ~ (<dy^2>/2) * (effective occupied bonds); closure spreads +that back over ALL bonds:
        du_far ~ +(<dy^2>/2) * (L_env_eff / N)
    where L_env_eff = envelope_area_frac * L_env is the effective occupied length (the
    envelope integral / peak). This is O(L_env/N) -> 0 as the ring lengthens: the
    pilot prediction that the compensating stretch DILUTES to nothing. SYMBOLIC form
    (algebraic), evaluated numerically. Sign: du_far > 0 (stretch), |du_far| << |du_local|."""
    dy2 = mean_dy2(y0=y0, k=k, omega=omega, k_s=k_s)
    l_eff = envelope_area_frac * l_env
    return float(0.5 * dy2 * l_eff / n_nodes)


# ─────────────────────────────────────────────────────────────────────────────
# 5 — the longitudinal sound speed and the SONIC ratio (the sweep reference).
# ─────────────────────────────────────────────────────────────────────────────
def c_long(k_long: float = K_S, m: float = 1.0) -> float:
    """Long-wavelength longitudinal (axial) sound speed on the 2-DOF chain:
    c_long = sqrt(k_long/m)*a0 (linearized axial branch, a0=1). The companion rides at
    v_g (the transverse group velocity); c_long/v_g is the Mach number of the
    co-moving source. rho_bond = k_long/k_shear; at rho=1 the two branches share the
    SAME small-k speed (photon point) -> the sonic coincidence (EXPECTED, KNIFE)."""
    return float(np.sqrt(k_long / m))


def sonic_ratio(k_long: float = K_S, omega: float = OMEGA_PUMP, k_s: float = K_S,
                m: float = 1.0) -> float:
    """Mach number of the co-moving companion: v_g (envelope group speed) / c_long.
    < 1 subsonic companion source (well can outrun-bound), = 1 sonic (Cherenkov
    threshold, EXPECTED at k_long=k_shear via the SMALL-k speeds; note the CARRIER k is
    finite so the coincidence is at the long-wave speeds), > 1 supersonic."""
    vg = group_velocity(omega, k_s, m)
    cl = c_long(k_long, m)
    return float(vg / cl)


# ─────────────────────────────────────────────────────────────────────────────
# The bundled prediction record (what the ReconcileGate consumes as `independent`).
# ─────────────────────────────────────────────────────────────────────────────
@dataclass(frozen=True)
class PilotPredictions:
    y0: float
    omega: float
    k_s: float
    k_carrier: float
    v_group: float
    v_phase: float
    mean_dy2: float
    free_local_depth: float          # -<dy^2>/2  (the companion depth under the envelope)
    c_dy2_coeff: float               # -1/2 (convexity, derived)
    c_dy4_coeff: float               # -1/8

    def as_dict(self) -> dict:
        return {
            "y0": self.y0, "omega": self.omega, "k_s": self.k_s,
            "k_carrier": self.k_carrier, "v_group": self.v_group,
            "v_phase": self.v_phase, "mean_dy2": self.mean_dy2,
            "free_local_depth": self.free_local_depth,
            "c_dy2_coeff": self.c_dy2_coeff, "c_dy4_coeff": self.c_dy4_coeff,
        }


def predict(y0: float = Y0_TENT, omega: float = OMEGA_PUMP, k_s: float = K_S) -> PilotPredictions:
    """Bundle the symbolic predictions at the operating point."""
    k = wave_number(omega, k_s)
    ser = free_contraction_series()
    return PilotPredictions(
        y0=y0, omega=omega, k_s=k_s, k_carrier=k,
        v_group=group_velocity(omega, k_s),
        v_phase=phase_velocity(omega, k_s),
        mean_dy2=mean_dy2(y0=y0, k=k),
        free_local_depth=free_host_local_depth(y0=y0, k=k),
        c_dy2_coeff=ser["c_dy2_float"],
        c_dy4_coeff=ser["c_dy4_float"],
    )


if __name__ == "__main__":
    import json

    p = predict()
    out = {
        "predictions": p.as_dict(),
        "free_contraction_series": {k: (str(v) if isinstance(v, sp.Basic) else v)
                                    for k, v in free_contraction_series().items()},
        "sonic_ratios": {f"rho={r}": sonic_ratio(k_long=r * K_S) for r in (0.5, 1.0, 2.0, 4.0)},
        "compensating_stretch": {
            f"L_env={le},N={n}": compensating_stretch_amplitude(l_env=le, n_nodes=n)
            for (le, n) in ((40, 512), (80, 1024), (160, 2048), (80, 512), (80, 2048))
        },
    }
    print(json.dumps(out, indent=2, default=float))
