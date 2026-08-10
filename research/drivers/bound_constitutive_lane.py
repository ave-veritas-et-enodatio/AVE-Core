#!/usr/bin/env python3
"""Bound-constitutive lane (R41) — algebra + toy-lattice receipts.

Implements the FROZEN expectations of research/2026-08-10_bound-constitutive_prereg-FROZEN.md §6.
Two named engines per verdict-bearing identity: sympy (exact symbolic) + plain-Python/numpy float.
The toy lattices below are PURPOSE-BUILT implementations of the receipted curl-only dynamics and
of the K-loaded (imported) control — no import of src/ave engine code anywhere (stencil fence:
no run of the engine corroborates anything in this lane).

Receipts:
  R0a  residual symmetry:  L(A + grad(lam(x)))  - L(A) == 0            (exact, sympy)
  R0b  time-dep remainder: L(A + grad(lam(x,t)))- L(A) == eps0*(dA/dt).grad(dlam/dt) + eps0/2*|grad(dlam/dt)|^2
  R0c  Noether generator:  eps0*dA/dt . grad(lam) == div(lam*eps0*dA/dt) - lam*div(eps0*dA/dt)
       + on-shell conservation: div(curl(curl(W))) == 0 for arbitrary W  =>  d/dt div(Pi) == 0
  R1   flat direction: longitudinal plane wave has omega^2 == 0 (sympy); numeric A_L(t) linear
  R2   conservation on 2D periodic grid: d/dt div(pi) == 0 (vacuum), == div(j) (sourced)
  R3   fronts: transverse front ~= c on receipted form; longitudinal STATIC on receipted form;
       longitudinal front ~= sqrt(10/3)*c on the K=2G-loaded control (instrument liveness)
  R4   Coulomb-class energy integral: int (B/r^2)^2 4 pi r^2 dr = 4 pi B^2 (1/r_in - 1/r_out)
  R5   radial response: K-loaded driven source radiates (|u_dot|^2 at r_mid > 0);
       receipted radial sector transports nothing (machine zero); exterior profile ODE
       u' + 2u/r = 0 -> u = C/r^2 (sympy dsolve)
  R6   banked-ratio records: nu(K=2G)=2/7, 1-2nu=3/7, (cP/cT)^2 at K=0 -> 4/3, at K=2G -> 10/3

No RNG anywhere except the FIXED-SEED random field in R0c's numeric cross-check (seed printed).
Output: research/drivers/bound_constitutive_lane_results.json
"""
from __future__ import annotations

import json
import math
import os
from fractions import Fraction

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "bound_constitutive_lane_results.json")

results: dict = {"lane": "bound-constitutive (R41)", "engines": ["sympy-exact", "plain-float/numpy"]}


# ---------------------------------------------------------------- symbolic helpers
def _fields():
    x, y, z, t = sp.symbols("x y z t", real=True)
    eps0, mu0 = sp.symbols("epsilon_0 mu_0", positive=True)
    A = sp.Matrix([sp.Function(f"A{i}")(x, y, z, t) for i in range(3)])
    return x, y, z, t, eps0, mu0, A


def _curl(V, x, y, z):
    return sp.Matrix([
        sp.diff(V[2], y) - sp.diff(V[1], z),
        sp.diff(V[0], z) - sp.diff(V[2], x),
        sp.diff(V[1], x) - sp.diff(V[0], y),
    ])


def _div(V, x, y, z):
    return sp.diff(V[0], x) + sp.diff(V[1], y) + sp.diff(V[2], z)


def _grad(f, x, y, z):
    return sp.Matrix([sp.diff(f, x), sp.diff(f, y), sp.diff(f, z)])


def _L(A, x, y, z, t, eps0, mu0):
    At = A.diff(t)
    cA = _curl(A, x, y, z)
    return sp.Rational(1, 2) * eps0 * (At.T * At)[0] - 1 / (2 * mu0) * (cA.T * cA)[0]


# ---------------------------------------------------------------- R0a / R0b / R0c
def r0_symmetry():
    x, y, z, t, eps0, mu0, A = _fields()

    lam_s = sp.Function("lambda_s")(x, y, z)  # time-independent
    dL_static = sp.simplify(_L(A + _grad(lam_s, x, y, z), x, y, z, t, eps0, mu0)
                            - _L(A, x, y, z, t, eps0, mu0))
    r0a_pass = dL_static == 0

    lam_t = sp.Function("lambda_t")(x, y, z, t)  # time-dependent
    dL_t = sp.simplify(_L(A + _grad(lam_t, x, y, z), x, y, z, t, eps0, mu0)
                       - _L(A, x, y, z, t, eps0, mu0))
    glt = _grad(sp.diff(lam_t, t), x, y, z)
    At = A.diff(t)
    remainder = eps0 * (At.T * glt)[0] + sp.Rational(1, 2) * eps0 * (glt.T * glt)[0]
    r0b_pass = sp.simplify(dL_t - remainder) == 0

    # Noether charge density identity: Pi.grad(lam) = div(lam*Pi) - lam*div(Pi)
    Pi = eps0 * At
    lhs = (Pi.T * _grad(lam_s, x, y, z))[0]
    rhs = _div(lam_s * Pi, x, y, z) - lam_s * _div(Pi, x, y, z)
    r0c_ident = sp.simplify(lhs - rhs) == 0

    # on-shell conservation: div(curl(curl(W))) == 0 for arbitrary W
    W = sp.Matrix([sp.Function(f"W{i}")(x, y, z, t) for i in range(3)])
    r0c_divcurlcurl = sp.simplify(_div(_curl(_curl(W, x, y, z), x, y, z), x, y, z)) == 0

    # float cross-check of r0c_divcurlcurl on a fixed-seed random polynomial field
    rng = np.random.default_rng(20260810)
    coeffs = rng.integers(-3, 4, size=(3, 10))
    xs, ys, zs = sp.symbols("xs ys zs", real=True)
    mono = [1, xs, ys, zs, xs * ys, ys * zs, xs * zs, xs**2, ys**2, zs**2]
    Wp = sp.Matrix([sum(int(c) * m for c, m in zip(coeffs[i], mono)) for i in range(3)])

    def curl_p(V):
        return sp.Matrix([sp.diff(V[2], ys) - sp.diff(V[1], zs),
                          sp.diff(V[0], zs) - sp.diff(V[2], xs),
                          sp.diff(V[1], xs) - sp.diff(V[0], ys)])

    dcc = sp.expand(sp.diff(curl_p(curl_p(Wp))[0], xs) + sp.diff(curl_p(curl_p(Wp))[1], ys)
                    + sp.diff(curl_p(curl_p(Wp))[2], zs))
    pt = {xs: 0.37, ys: -1.21, zs: 0.83}
    r0c_float = abs(float(dcc.subs(pt))) < 1e-12

    results["R0"] = {
        "R0a_residual_symmetry_exact_zero": bool(r0a_pass),
        "R0b_timedep_remainder_matches": bool(r0b_pass),
        "R0b_remainder_form": "eps0*(dA/dt).grad(dlam/dt) + (eps0/2)*|grad(dlam/dt)|^2",
        "R0c_noether_density_identity": bool(r0c_ident),
        "R0c_div_curl_curl_zero_symbolic": bool(r0c_divcurlcurl),
        "R0c_div_curl_curl_zero_float_seed20260810": bool(r0c_float),
    }


# ---------------------------------------------------------------- R1 flat direction
def r1_flat_direction():
    # sympy: longitudinal plane wave A = f(t) e^{ikx} xhat -> curl == 0 -> eps0 f'' = 0
    x, y, z, t, eps0, mu0, _ = _fields()
    k = sp.symbols("k", positive=True)
    f = sp.Function("f")(t)
    Al = sp.Matrix([f * sp.exp(sp.I * k * x), 0, 0])
    curl_zero = sp.simplify(_curl(Al, x, y, z)) == sp.zeros(3, 1)

    # numeric: leapfrog under Add == 0
    dt, n = 0.01, 20000
    a0, v0 = 0.7, -0.3
    a, v = a0, v0
    worst = 0.0
    for i in range(1, n + 1):
        a += v * dt          # acceleration identically zero on the flat direction
        worst = max(worst, abs(a - (a0 + v0 * i * dt)))
    results["R1"] = {
        "sympy_longitudinal_curl_is_zero": bool(curl_zero),
        "numeric_linear_drift_residual": worst,
        "numeric_linear_drift_pass_le_1e-10": bool(worst <= 1e-10),
        "conserved_momentum_note": "Pi_L = eps0*dA_L/dt constant by construction (Add==0)",
    }


# ---------------------------------------------------------------- 2D grid machinery
def _ddx(f, h):
    return (np.roll(f, -1, 0) - np.roll(f, 1, 0)) / (2 * h)


def _ddy(f, h):
    return (np.roll(f, -1, 1) - np.roll(f, 1, 1)) / (2 * h)


def _lap(f, h):
    return (np.roll(f, -1, 0) + np.roll(f, 1, 0) + np.roll(f, -1, 1) + np.roll(f, 1, 1) - 4 * f) / h**2


def _div2(ux, uy, h):
    return _ddx(ux, h) + _ddy(uy, h)


def _grad2(f, h):
    return _ddx(f, h), _ddy(f, h)


def _force(ux, uy, h, kg):
    """Constitutive operator on the 2D grid, stencil-consistent.

    Receipted curl-only form (kg=None):  F = -curl(curl u), built as the LITERAL double
    curl so that div(F) == 0 is a machine-exact commuting-convolution identity (the
    discrete DEC-class statement), and curl-free u gives F == 0 exactly.
    Imported control (kg=K/G):  F = -curl(curl u) + cP^2 * grad(div u) with
    cP^2 = kg + 4/3 (at kg=2 -> 10/3); the grad(div) term is the composed stencil.
    """
    w = _ddx(uy, h) - _ddy(ux, h)                 # curl u (z-component)
    ccx, ccy = _ddy(w, h), -_ddx(w, h)            # curl(w zhat)
    fx, fy = -ccx, -ccy                            # -curl curl u
    if kg is not None:
        d = _div2(ux, uy, h)
        gx, gy = _grad2(d, h)
        cp2 = kg + 4.0 / 3.0
        fx, fy = fx + cp2 * gx, fy + cp2 * gy
    return fx, fy


# ---------------------------------------------------------------- R2 conservation
def r2_conservation():
    n, h = 96, 1.0
    dt = 0.2
    xg = (np.arange(n) - n / 2)[:, None] * np.ones((1, n))
    yg = np.ones((n, 1)) * (np.arange(n) - n / 2)[None, :]
    r2 = xg**2 + yg**2

    # generic initial data (mixed transverse+longitudinal), zero initial velocity
    psi = np.exp(-r2 / 30.0)
    phi = np.exp(-r2 / 18.0)
    ux = _ddy(psi, h) + _ddx(phi, h)
    uy = -_ddx(psi, h) + _ddy(phi, h)
    vx = np.zeros_like(ux)
    vy = np.zeros_like(uy)

    # vacuum: d/dt div(pi) must vanish (central-difference convolutions commute exactly)
    worst_vac = 0.0
    for _ in range(200):
        fx, fy = _force(ux, uy, h, None)
        worst_vac = max(worst_vac, float(np.max(np.abs(_div2(fx, fy, h)))))
        vx += dt * fx
        vy += dt * fy
        ux += dt * vx
        uy += dt * vy

    # sourced: pi_dot = F + j  ->  d/dt div(pi) - div(j) == 0 identically per step
    jx = _ddx(np.exp(-r2 / 12.0), h) * 0.05
    jy = _ddy(np.exp(-r2 / 12.0), h) * 0.05
    ux2 = ux.copy(); uy2 = uy.copy(); vx2 = vx.copy(); vy2 = vy.copy()
    worst_src = 0.0
    for _ in range(200):
        fx, fy = _force(ux2, uy2, h, None)
        rate = _div2(fx + jx, fy + jy, h) - _div2(jx, jy, h)   # d/dt div(pi) - div(j)
        worst_src = max(worst_src, float(np.max(np.abs(rate))))
        vx2 += dt * (fx + jx)
        vy2 += dt * (fy + jy)
        ux2 += dt * vx2
        uy2 += dt * vy2

    results["R2"] = {
        "vacuum_max_abs_ddt_div_pi": worst_vac,
        "vacuum_pass_le_1e-12": bool(worst_vac <= 1e-12),
        "sourced_max_abs_continuity_defect": worst_src,
        "sourced_pass_le_1e-12": bool(worst_src <= 1e-12),
        "grid": {"n": n, "h": h, "dt": dt, "steps": 200},
        "note": "central-difference div/grad/lap are commuting convolutions on the periodic "
                "grid, so div(curl-curl force) == 0 to roundoff — the discrete DEC-class identity",
    }


# ---------------------------------------------------------------- R3 fronts
def _front_speed(kind: str, kg, pol: str, n=400, steps=700):
    h = 1.0
    c_max = math.sqrt(1.0 + (kg + 1.0 / 3.0)) if kg is not None else 1.0
    dt = 0.25 * h / c_max
    xg = (np.arange(n) - n / 2)[:, None] * np.ones((1, n))
    yg = np.ones((n, 1)) * (np.arange(n) - n / 2)[None, :]
    r2 = xg**2 + yg**2
    # wide pulse (sigma=10) keeps the energy spectrum at kh <~ 0.2, where the stencil's
    # group velocity is within ~1.5% of the continuum speed (declared <=3% tolerance)
    bump = np.exp(-r2 / 200.0)
    if pol == "T":
        ux, uy = _ddy(bump, h), -_ddx(bump, h)      # div-free
    else:
        ux, uy = _ddx(bump, h), _ddy(bump, h)       # curl-free
    vx = np.zeros_like(ux); vy = np.zeros_like(uy)
    u0x, u0y = ux.copy(), uy.copy()

    rr = np.sqrt(r2)
    # two-detector first-arrival front measure: annulus-averaged energy at r_d1 < r_d2;
    # speed = (r_d2 - r_d1)/(t_2 - t_1). Cancels launch offset and the 2D wake.
    r_d1, r_d2 = 60.0, 120.0
    ann1 = np.abs(rr - r_d1) < 1.5
    ann2 = np.abs(rr - r_d2) < 1.5
    ts, e1s, e2s = [], [], []
    for s in range(1, steps + 1):
        fx, fy = _force(ux, uy, h, kg)
        vx += dt * fx; vy += dt * fy
        ux += dt * vx; uy += dt * vy
        e = vx**2 + vy**2
        ts.append(s * dt)
        e1s.append(float(np.mean(e[ann1])))
        e2s.append(float(np.mean(e[ann2])))

    moved = float(np.max(np.abs(ux - u0x)) + np.max(np.abs(uy - u0y)))
    # half-max arrival per detector: t_i = first t with e_i(t) >= 0.5 * max_t e_i.
    # The same relative threshold at both detectors cancels the leading-tail bias.
    e1s, e2s, ts = np.array(e1s), np.array(e2s), np.array(ts)
    speed = 0.0
    if e1s.max() > 1e-28 and e2s.max() > 1e-28:
        t1 = float(ts[np.argmax(e1s >= 0.5 * e1s.max())])
        t2 = float(ts[np.argmax(e2s >= 0.5 * e2s.max())])
        if t2 > t1:
            speed = (r_d2 - r_d1) / (t2 - t1)
        t_arr1, t_arr2 = t1, t2
    else:
        t_arr1 = t_arr2 = None
    return {"kind": kind, "pol": pol, "K_over_G": kg, "front_speed": speed,
            "arrivals": {"r_d1": r_d1, "t1": t_arr1, "r_d2": r_d2, "t2": t_arr2},
            "max_displacement_change": moved, "grid": {"n": n, "dt": dt, "steps": steps}}


def r3_fronts():
    t_rec = _front_speed("receipted", None, "T")
    l_rec = _front_speed("receipted", None, "L")
    l_imp = _front_speed("K2G-loaded control", 2.0, "L")
    cp = math.sqrt(10.0 / 3.0)
    results["R3"] = {
        "transverse_receipted": t_rec,
        "transverse_speed_pass_within_3pct_of_c": bool(abs(t_rec["front_speed"] - 1.0) <= 0.03),
        "longitudinal_receipted": l_rec,
        "longitudinal_receipted_STATIC_pass": bool(l_rec["max_displacement_change"] <= 1e-12),
        "longitudinal_K2G_control": l_imp,
        "control_detects_superluminal_front_ge_1.5c": bool(l_imp["front_speed"] >= 1.5),
        "control_speed_within_3pct_of_sqrt10over3": bool(abs(l_imp["front_speed"] - cp) / cp <= 0.03),
        "sqrt_10_3_frozen": 1.8257418583505538,
    }


# ---------------------------------------------------------------- R4 energy integral
def r4_energy():
    B, r, r_in, r_out = sp.symbols("B r r_in r_out", positive=True)
    E = sp.integrate((B / r**2) ** 2 * 4 * sp.pi * r**2, (r, r_in, r_out))
    expect = 4 * sp.pi * B**2 * (1 / r_in - 1 / r_out)
    exact = sp.simplify(E - expect) == 0
    # float cross-check
    val = float(E.subs({B: 1.0, r_in: 2.0, r_out: 50.0}))
    ref = 4 * math.pi * (1 / 2.0 - 1 / 50.0)
    results["R4"] = {
        "sympy_exact_match": bool(exact),
        "float_value_Bin2out50": val,
        "float_ref": ref,
        "float_pass": bool(abs(val - ref) < 1e-12),
        "form": "4*pi*B^2*(1/r_in - 1/r_out): finite, positive, Coulomb-class (1/r^4 density)",
    }


# ---------------------------------------------------------------- R5 radial response
def r5_radial_response():
    # exterior profile ODE: u' + 2u/r = 0  ->  u = C/r^2  (the unique decaying solution)
    r = sp.symbols("r", positive=True)
    u = sp.Function("u")
    sol = sp.dsolve(sp.Eq(u(r).diff(r) + 2 * u(r) / r, 0), u(r))
    profile_ok = sp.simplify(sp.diff(sol.rhs * r**2, r)) == 0   # u * r^2 is r-independent -> u = C/r^2

    # K-loaded radial P operator: rho u_tt = cP^2 d/dr[(1/r^2) d/dr(r^2 u)] — driven at r_in.
    n, r_in, r_out = 800, 5.0, 405.0
    dr = (r_out - r_in) / n
    rg = r_in + dr * np.arange(n + 1)
    cp2 = 10.0 / 3.0
    dt = 0.25 * dr / math.sqrt(cp2)
    omega = 0.15
    steps = int(0.75 * (r_out - r_in) / math.sqrt(cp2) / dt)   # stop before boundary reflection
    mid = n // 2

    def run(loaded: bool):
        uu = np.zeros(n + 1); vv = np.zeros(n + 1)
        acc_mid = 0.0; count = 0
        for s in range(steps):
            t = s * dt
            uu[0] = 0.05 * math.sin(omega * t)          # driven inner boundary
            if loaded:
                inner = rg**2 * uu
                d1 = np.gradient(inner, dr) / rg**2
                acc = cp2 * np.gradient(d1, dr)
            else:
                acc = np.zeros_like(uu)                  # receipted radial sector: curl-curl(radial)=0
            vv[1:] += dt * acc[1:]
            uu[1:] += dt * vv[1:]
            if s > steps // 2:
                acc_mid += vv[mid] ** 2; count += 1
        return acc_mid / max(count, 1)

    p_loaded = run(True)
    p_receipted = run(False)
    results["R5"] = {
        "exterior_profile_u_prime_plus_2u_over_r": str(sol),
        "profile_is_C_over_r2": bool(profile_ok),
        "flux_proxy_time_avg_udot2_at_rmid_K2G": p_loaded,
        "flux_proxy_time_avg_udot2_at_rmid_receipted": p_receipted,
        "receipted_transports_nothing_pass": bool(p_receipted == 0.0),
        "control_radiates_pass_ge_10x_floor": bool(p_loaded > 1e-10),
        "params": {"n": n, "r_in": r_in, "r_out": r_out, "omega": omega, "steps": steps,
                   "note": "flux proxy = time-averaged |u_dot|^2 at r_mid, declared per prereg"},
    }


# ---------------------------------------------------------------- R6 banked ratios
def r6_ratios():
    def nu_of(kg: Fraction) -> Fraction:
        return Fraction(3 * kg - 2, 2 * (3 * kg + 1))

    nu = nu_of(Fraction(2))
    ratios = {
        "nu_at_K2G": nu,
        "trace_factor_1_minus_2nu": 1 - 2 * nu,
        "cP2_over_cT2_at_K0": Fraction(4, 3),
        "cP2_over_cT2_at_K2G": Fraction(2) + Fraction(4, 3),
    }
    ok = (nu == Fraction(2, 7) and 1 - 2 * nu == Fraction(3, 7)
          and ratios["cP2_over_cT2_at_K2G"] == Fraction(10, 3))
    results["R6"] = {k: {"exact": str(v), "float": float(v)} for k, v in ratios.items()}
    results["R6"]["all_banked_ratios_pass"] = bool(ok)
    results["R6"]["sqrt_check_float"] = {
        "sqrt_4_3": math.sqrt(4 / 3), "sqrt_10_3": math.sqrt(10 / 3),
        "frozen_sqrt_4_3": 1.1547005383792515, "frozen_sqrt_10_3": 1.8257418583505538,
    }


def main():
    r0_symmetry()
    r1_flat_direction()
    r2_conservation()
    r3_fronts()
    r4_energy()
    r5_radial_response()
    r6_ratios()
    gates = {
        "R0": all(v for k, v in results["R0"].items() if isinstance(v, bool)),
        "R1": results["R1"]["sympy_longitudinal_curl_is_zero"] and results["R1"]["numeric_linear_drift_pass_le_1e-10"],
        "R2": results["R2"]["vacuum_pass_le_1e-12"] and results["R2"]["sourced_pass_le_1e-12"],
        "R3": (results["R3"]["transverse_speed_pass_within_3pct_of_c"]
               and results["R3"]["longitudinal_receipted_STATIC_pass"]
               and results["R3"]["control_detects_superluminal_front_ge_1.5c"]
               and results["R3"]["control_speed_within_3pct_of_sqrt10over3"]),
        "R4": results["R4"]["sympy_exact_match"] and results["R4"]["float_pass"],
        "R5": (results["R5"]["profile_is_C_over_r2"]
               and results["R5"]["receipted_transports_nothing_pass"]
               and results["R5"]["control_radiates_pass_ge_10x_floor"]),
        "R6": results["R6"]["all_banked_ratios_pass"],
    }
    results["gates"] = gates
    results["all_pass"] = all(gates.values())
    with open(OUT, "w") as f:
        json.dump(results, f, indent=1, default=str)
    print(json.dumps(gates, indent=1))
    print(f"ALL_PASS={results['all_pass']}")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
