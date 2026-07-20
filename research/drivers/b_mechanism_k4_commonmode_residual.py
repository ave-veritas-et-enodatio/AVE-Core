#!/usr/bin/env python3
"""
B-mechanism derivation — reproducible checks for the Reading-B port-closure trace.

Lane fence: DERIVATION lane. Imports ave.core.constants READ-ONLY (L_NODE, C_0,
OMEGA_C). Touches NO engine primitive; builds the 4x4 K4-TLM scatter matrix from
its canonical closed form and does linear algebra only. Reproduces three numbers
the companion doc (research/2026-07-20_b-mechanism-derivation_result.md) cites:

  1. B1 forcing ingredient: the K4-TLM scatter S = (1/2)*ones - I has eigenvalues
     {+1, -1, -1, -1}; the +1 eigenvector is the A1 common-mode (1,1,1,1)/2 (the
     longitudinal/dilatation "DC" mode), the -1 triplet spans the traceless T2
     (shear) subspace. This is the group-theory fact (clm-j550uh) that makes the
     A1 longitudinal a common-mode-rejected / Gauss-constrained mode.

  2. B2-falsification cross-check: the rotating mass second-moment tensor of a
     circular binary has a NONZERO traceless (rotating) part -> a scalar field's
     quadrupole radiation IS driven (the naive "trace is constant so A1 cannot
     radiate" rescue FAILS). Confirms the source-vanishing trace-argument is dead.

  3. Residual (chord-potential): IF B1 governs (A1 common-mode-rejected exactly),
     the port closes with residual F_bulk/F_shear identically 0 at continuum order;
     any lattice leakage of A1 back out is bounded by the finite-k mode-mixing
     scale (omega * ell_node / c)^2, evaluated for Hulse-Taylor and the double
     pulsar. The bound is ~1e-48 -> unobservable at ANY pulsar-timing precision.

Run:  PYTHONPATH=<worktree>/src ./.venv/bin/python \
        research/drivers/b_mechanism_k4_commonmode_residual.py
"""
from __future__ import annotations

import json

import numpy as np

from ave.core.constants import C_0, L_NODE, OMEGA_C  # read-only canonical imports


def k4_scatter() -> np.ndarray:
    """Canonical K4-TLM 4-port scatter matrix S_ij = 1/2 - delta_ij  (z_local=1).

    S = (1/2)*ones - I   (all-ones matrix minus identity), per
    k4-port-irrep-decomposition.md:65-67 (clm-j550uh). Built from closed form;
    NOT read from any engine primitive.
    """
    return 0.5 * np.ones((4, 4)) - np.eye(4)


def check_1_scatter_eigenstructure() -> dict:
    S = k4_scatter()
    evals, evecs = np.linalg.eigh(S)  # symmetric
    a1 = np.ones(4) / 2.0  # (1,1,1,1)/2, the A1 common-mode basis vector
    # A1 eigenvalue: S @ a1 should be +1 * a1
    Sa1 = S @ a1
    a1_eigval = float(Sa1 @ a1 / (a1 @ a1))
    # T2 subspace = traceless (sum v = 0); pick a traceless test vector
    t2 = np.array([1.0, -1.0, 0.0, 0.0])
    St2 = S @ t2
    t2_eigval = float(St2 @ t2 / (t2 @ t2))
    return {
        "S_matrix": S.tolist(),
        "eigenvalues_sorted": sorted(round(float(x), 12) for x in evals),
        "A1_common_mode_eigenvalue": round(a1_eigval, 12),  # expect +1
        "T2_traceless_eigenvalue": round(t2_eigval, 12),    # expect -1
        "A1_is_plus1": abs(a1_eigval - 1.0) < 1e-12,
        "T2_is_minus1": abs(t2_eigval + 1.0) < 1e-12,
        "trace_S": round(float(np.trace(S)), 12),  # = -2 (= eigenvalue sum +1-1-1-1)
        "eigenvalue_sum_is_minus2": abs(float(np.trace(S)) + 2.0) < 1e-12,
    }


def _rotating_mass_second_moment(m1: float, m2: float, sep: float, phase: float) -> np.ndarray:
    """Mass second moment M_ij = sum_a m_a x_i x_j for a circular binary, in the
    reduced-mass frame (bodies at +/- along the line at angle=phase in the x-y plane).
    """
    mu = m1 * m2 / (m1 + m2)  # reduced mass
    # both bodies contribute mu * (r_vec outer r_vec) with r the SEPARATION vector
    r = np.array([np.cos(phase), np.sin(phase), 0.0]) * sep
    M = mu * np.outer(r, r)
    return M


def check_2_traceless_quadrupole_nonzero() -> dict:
    """The rotating traceless part of M_ij is nonzero => a scalar (A1) field's
    quadrupole radiation is DRIVEN. The naive B2 rescue ('the A1/breathing sees
    only the trace sum m r^2, which is constant for a circular orbit') FAILS,
    because scalar-field quadrupole radiation is governed by the traceless second
    moment of the scalar SOURCE, not by the trace.
    """
    m1, m2, sep = 1.4, 1.4, 1.0  # arbitrary units; only the tensor STRUCTURE matters
    phases = np.linspace(0.0, np.pi, 9)
    traces, tl_norms = [], []
    for ph in phases:
        M = _rotating_mass_second_moment(m1, m2, sep, ph)
        tr = float(np.trace(M))
        M_tl = M - (tr / 3.0) * np.eye(3)  # traceless part
        traces.append(round(tr, 6))
        tl_norms.append(round(float(np.linalg.norm(M_tl)), 6))
    trace_is_constant = float(np.std(traces)) < 1e-9
    traceless_rotates = float(np.std(tl_norms)) < 1e-9  # norm constant but the TENSOR rotates
    # confirm the traceless tensor genuinely rotates (its xx component varies)
    xx = [round(float(_rotating_mass_second_moment(m1, m2, sep, ph)[0, 0]
                      - np.trace(_rotating_mass_second_moment(m1, m2, sep, ph)) / 3.0), 6)
          for ph in phases]
    return {
        "trace_sum_m_r2_constant": trace_is_constant,        # True: the A1 TRACE is constant
        "traceless_norm_constant": traceless_rotates,        # norm fixed (circular)
        "traceless_xx_component_varies": float(np.std(xx)) > 1e-6,  # but the TENSOR rotates
        "verdict": ("B2-via-trace FALSIFIED: traceless second moment rotates "
                    "(xx varies) => scalar quadrupole radiation is DRIVEN; the "
                    "constant trace does NOT kill A1 radiation."),
    }


def check_3_lattice_leakage_residual() -> dict:
    """If B1 governs, the continuum-order residual F_bulk/F_shear = 0 exactly (the
    A1 common-mode is transduced into T2 by the exact/unitary K4 scatter). The only
    conceivable leakage is finite-k mode-mixing at the lattice scale, bounded by
    (omega * ell_node / c)^2. Evaluate for Hulse-Taylor and the double pulsar.
    """
    # GW angular frequency = 2 * orbital Omega. Orbital periods [s]:
    systems = {
        "Hulse-Taylor B1913+16": 7.751939 * 3600.0,   # P_b ~ 7.75 hr
        "double pulsar J0737-3039": 2.454 * 3600.0,    # P_b ~ 2.45 hr
    }
    out = {}
    for name, P_b in systems.items():
        Omega = 2.0 * np.pi / P_b
        omega_gw = 2.0 * Omega  # dominant quadrupole radiation at 2 Omega
        eps = omega_gw * L_NODE / C_0  # dimensionless lattice-frequency ratio
        out[name] = {
            "P_b_s": P_b,
            "omega_gw_rad_s": omega_gw,
            "omega_gw_over_omega_C": omega_gw / OMEGA_C,
            "lattice_ratio_eps": eps,
            "leakage_residual_bound_eps2": eps ** 2,
        }
    return out


def main() -> None:
    results = {
        "constants_used_readonly": {
            "C_0_m_s": C_0,
            "L_NODE_m": L_NODE,
            "OMEGA_C_rad_s": OMEGA_C,
        },
        "check_1_k4_scatter_eigenstructure": check_1_scatter_eigenstructure(),
        "check_2_traceless_quadrupole_nonzero": check_2_traceless_quadrupole_nonzero(),
        "check_3_lattice_leakage_residual": check_3_lattice_leakage_residual(),
    }
    print(json.dumps(results, indent=2))

    # Machine-checkable asserts (the load-bearing claims):
    c1 = results["check_1_k4_scatter_eigenstructure"]
    assert c1["A1_is_plus1"], "A1 common-mode must be the +1 eigenvector"
    assert c1["T2_is_minus1"], "T2 traceless triplet must be the -1 eigenvalue"
    assert c1["eigenvalues_sorted"] == [-1.0, -1.0, -1.0, 1.0], "spectrum must be {+1,-1,-1,-1}"
    c2 = results["check_2_traceless_quadrupole_nonzero"]
    assert c2["trace_sum_m_r2_constant"], "circular-orbit trace must be constant"
    assert c2["traceless_xx_component_varies"], "traceless quadrupole must rotate (B2-via-trace dead)"
    c3 = results["check_3_lattice_leakage_residual"]
    for name, d in c3.items():
        assert d["leakage_residual_bound_eps2"] < 1e-40, f"{name}: leakage bound not negligible"
    print("\nALL ASSERTS PASSED")


if __name__ == "__main__":
    main()
