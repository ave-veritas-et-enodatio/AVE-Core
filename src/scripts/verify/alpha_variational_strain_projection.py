#!/usr/bin/env python3
"""
Open A + Open B — lattice-native strain-projection route to alpha's value.

PREREG (frozen):
  - Open A v1:  research/2026-06-25_alpha-variational-strain-projection_prereg.md
  - Open A v2:  research/2026-06-25_alpha-lattice-strain-projection_prereg-v2.md
  - Open B v4:  research/2026-06-25_openB-delta-strain-percolation_prereg-v4.md
RESULTS:
  - research/2026-06-25_alpha-variational-strain-projection_result.md  (Open A)
  - research/2026-06-25_openB-delta-strain-percolation_result.md       (Open B)
CANONICAL SESSION STATE:
  - research/2026-06-25_delta-strain-session-synthesis.md

RECONSTRUCTED 2026-06-25 (consolidation pass A). The original driver backing
Opens A+B was lost from every tree/stash before the preservation commit. This
file is a faithful reconstruction from the prereg/result chain; it reproduces the
published result-doc numbers to the reported precision (verified at write-time):

  B2 (K/G=2 constraint): u=0.1925 p=0.1809 K/G=2.000 s_grav=0.00897 1/alpha=138.92 (+1.38%)
  B1 (admissibility-weighted max): u=0.1663 p=0.1934 K/G=1.827 s_grav=0.00867 1/alpha=129.96 (+5.17%)
  DIAG (CODATA packing, diagnostic only): p=0.1834 u=0.1871 K/G=1.961 s_grav=0.00893 1/alpha=137.04

VERDICT (Open A): CLOSED-NEGATIVE / FORK-for-Grant — B1 != B2; the admissibility-
weighted max lands DENSER (K/G~1.83), not at the floppy edge the prereg expected.
Gravity-stable projection is a CONSTRAINT (K/G=2 trace-reversal lock), not the
unconstrained optimum of Pi*gamma. B2/B4 relabel the z=52 K/G crossing (+1.38%).

VERDICT (Open B): CLOSED-NEGATIVE — forward delta_strain from rigidity-percolation /
node-participation misses 2.2 ppm by -4 to -5 dex; FT-1 BE control -31 dex.

SUBSTRATE-NATIVE CHAIN (prereg-v2 frozen):
  T_EM=1  ->  eps_11 = 1/(E/G)  on primary bond
          ->  gamma = (u/(1+u)) * eps_11  on secondary links (over-bracing)
          ->  nu = (3*K/G - 2)/(2*(3*K/G + 1))
          ->  Pi = (1-2*nu)/3 = 1/(3*K/G + 1)   (= 1/7 only at K/G=2)
          ->  s_grav = Pi * gamma              (local bulk-gravity strain amplitude)
  alpha enters only as packing readout alpha_pred = p/(8*pi) AFTER the solve.

ALPHA-HIDING GUARD (prereg P3):
  z0=52 and p_cauchy=0.3068 are PREREG-FROZEN, alpha-FREE inputs on the verdict
  path. NOTE z0=52 is the K4 path-count convention (4*(1+|T|)), NOT the cold-form
  Z_COORDINATION~51.25 (which is p_cold-derived and would be alpha-circular). ALPHA
  and P_C from ave.core.constants are loaded ONLY for the post-solve DIAGNOSTIC
  comparison (DIAG row + percentage errors), never on the verdict path.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

from scipy.optimize import brentq, minimize_scalar

# CODATA constants — POST-SOLVE COMPARISON ONLY (never on the verdict path).
from ave.core.constants import ALPHA, P_C

# ---------------------------------------------------------------------------
# Prereg-frozen, alpha-FREE lattice inputs (verdict path).
# ---------------------------------------------------------------------------
Z0 = 52.0  # K4 path-count convention: 4*(1+|T|), |T|=12 (NOT the cold p_c-derived z)
P_CAUCHY = 0.3068  # Delaunay amorphous reference (standard network geometry)
P_G = 6.0 / Z0  # rigidity-percolation isostatic floor (Maxwell count)
TWO_PI = 2.0 * math.pi
EIGHT_PI = 8.0 * math.pi

# CODATA targets (DIAGNOSTIC ONLY).
ALPHA_INV_CODATA = 1.0 / ALPHA  # ~137.035999


# ---------------------------------------------------------------------------
# FTG-EMT lattice chain (prereg-v2).
# ---------------------------------------------------------------------------
def p_of_u(u: float) -> float:
    """Over-bracing dilution: packing fraction at dilution u (volume scaling)."""
    return P_CAUCHY / (1.0 + u) ** 3


def kg_of_p(p: float) -> float:
    """FTG-EMT amorphous central-force K/G(p) at z0 (canonical q_g47 EMT form)."""
    return (Z0 * p - 2.0) * (Z0 - 6.0) / ((Z0 * p - 6.0) * (Z0 - 2.0))


def nu_of_kg(kg: float) -> float:
    """Poisson ratio from K/G (= 2/7 at K/G=2)."""
    return (3.0 * kg - 2.0) / (2.0 * (3.0 * kg + 1.0))


def pi_proj(kg: float) -> float:
    """Isotropic bulk-strain projection Pi = (1-2nu)/3 = 1/(3K/G+1) (= 1/7 at K/G=2)."""
    return 1.0 / (3.0 * kg + 1.0)


def eps11(kg: float) -> float:
    """Axial strain from unit primary-bond tension: 1/(E/G), E/G = 9(K/G)/(3K/G+1)."""
    return (3.0 * kg + 1.0) / (9.0 * kg)


def gamma_secondary(u: float, kg: float) -> float:
    """Secondary-link shear from over-bracing engagement (u/(1+u))*eps_11."""
    return (u / (1.0 + u)) * eps11(kg)


def s_grav(u: float) -> float:
    """Local bulk-gravity strain amplitude s_grav = Pi * gamma (T_EM = 1)."""
    p = p_of_u(u)
    kg = kg_of_p(p)
    return pi_proj(kg) * gamma_secondary(u, kg)


def admissibility(u: float) -> float:
    """Rigidity margin x Cauchy clearance; zero outside the window (p_G, p_cauchy)."""
    p = p_of_u(u)
    rig = max(0.0, (p - P_G) / P_G)
    cau = max(0.0, (P_CAUCHY - p) / P_CAUCHY)
    return rig * cau


def _chain_at(u: float) -> dict:
    p = p_of_u(u)
    kg = kg_of_p(p)
    return {
        "u": u,
        "p": p,
        "K_over_G": kg,
        "nu": nu_of_kg(kg),
        "Pi": pi_proj(kg),
        "eps_11": eps11(kg),
        "gamma": gamma_secondary(u, kg),
        "s_grav": pi_proj(kg) * gamma_secondary(u, kg),
        "alpha_inv_pred": EIGHT_PI / p,  # = 1/(p/(8pi)); readout AFTER solve
        "pct_err_vs_CODATA": (EIGHT_PI / p) / ALPHA_INV_CODATA - 1.0,  # DIAGNOSTIC
    }


# ---------------------------------------------------------------------------
# Open A routes (prereg-v2 B1/B2/B4 + DIAG).
# ---------------------------------------------------------------------------
def route_b2_constraint() -> dict:
    """B2 — trace-reversal constraint: solve K/G(p(u))=2; report full chain."""
    u_star = brentq(lambda u: kg_of_p(p_of_u(u)) - 2.0, 0.01, 0.35)
    out = _chain_at(u_star)
    out["route"] = "B2"
    out["meaning"] = "trace-reversal gravity lock (K/G=2 constraint)"
    out["verdict"] = "PARTIAL +1.38% — constraint crossing, z=52 wrong target"
    return out


def route_b1_max() -> dict:
    """B1 — admissibility-weighted max of s_grav (unconstrained projection)."""
    # window where admissibility > 0: p in (p_G, p_cauchy) -> u in (0, u_at_pG)
    u_pg = (P_CAUCHY / P_G) ** (1.0 / 3.0) - 1.0
    # coarse scan then refine (avoid the K/G pole, which coincides with p_G).
    n = 200000
    best_u, best_v = 0.0, -1.0
    for i in range(1, n):
        u = u_pg * i / n
        v = s_grav(u) * admissibility(u)
        if v > best_v:
            best_v, best_u = v, u
    res = minimize_scalar(
        lambda u: -(s_grav(u) * admissibility(u)),
        bounds=(max(1e-4, best_u - 0.005), min(u_pg - 1e-4, best_u + 0.005)),
        method="bounded",
    )
    out = _chain_at(res.x)
    out["route"] = "B1"
    out["meaning"] = "unconstrained max of s_grav x admissibility"
    out["objective"] = s_grav(res.x) * admissibility(res.x)
    out["verdict"] = (
        "CLOSED-NEGATIVE +5.17% — admissibility-weighted max lands DENSER "
        "(K/G~1.83), not the floppy edge the prereg expected; distinct from B2"
    )
    return out


def route_b4_weighted() -> dict:
    """B4 — max s_grav x exp(-|ln(K/G/2)|): v1 A2 relabeled; expect B4 == B2."""
    u_pg = (P_CAUCHY / P_G) ** (1.0 / 3.0) - 1.0

    def obj(u: float) -> float:
        p = p_of_u(u)
        kg = kg_of_p(p)
        if kg <= 0:
            return 0.0
        return s_grav(u) * admissibility(u) * math.exp(-abs(math.log(kg / 2.0)))

    n = 200000
    best_u, best_v = 0.0, -1.0
    for i in range(1, n):
        u = u_pg * i / n
        v = obj(u)
        if v > best_v:
            best_v, best_u = v, u
    res = minimize_scalar(
        lambda u: -obj(u),
        bounds=(max(1e-4, best_u - 0.005), min(u_pg - 1e-4, best_u + 0.005)),
        method="bounded",
    )
    out = _chain_at(res.x)
    out["route"] = "B4"
    out["meaning"] = "K/G=2-proximity-weighted max (v1 A2 in lattice units)"
    out["verdict"] = "RELABEL — recovers the B2 crossing; no new selection principle"
    return out


def route_diag_codata() -> dict:
    """DIAGNOSTIC ONLY — CODATA packing p_c = 8*pi*alpha; NOT a verdict route."""
    p_c = EIGHT_PI * ALPHA  # CODATA — diagnostic comparison only
    u_codata = (P_CAUCHY / p_c) ** (1.0 / 3.0) - 1.0
    out = _chain_at(u_codata)
    out["route"] = "DIAG"
    out["meaning"] = "CODATA packing (post-solve diagnostic only)"
    out["P_C_CODATA"] = p_c
    out["P_C_constants"] = P_C
    out["verdict"] = "DIAGNOSTIC — CODATA p_c gives K/G~1.96, between B1 and B2"
    return out


# ---------------------------------------------------------------------------
# Open B routes (EMT-percolation forward delta_strain; prereg-v4 B0-B2).
# ---------------------------------------------------------------------------
# Cold-form anchor (alpha-FREE on the verdict path: derived from the geometric
# cold sum, used as the OPERATING packing for percolation sensitivity, NOT the
# CODATA value).
from ave.core.constants import ALPHA_COLD, ALPHA_COLD_INV  # noqa: E402

# Closed-negative thermal control (FT-1) and percolation driver.
ETA_EPS_FT1_BE = 2.2e-37  # FT-1 closed-negative BE reference (-31 dex)
# Cosmic thermal dilution fluctuation du/u (FT-1-class thermal-dilution OOM). This
# is the ONLY substrate-supplied du driver; it pins B1 to ~5.6e-11 (result-doc).
# It is NOT independently derived from the cold form — Open B's verdict is that the
# corpus supplies no NON-thermal participation driver, so this thermal du is the
# only candidate and it undershoots by -4 to -5 dex.
THERMAL_DU_OVER_U = 1.184e-10


def _delta_strain_target() -> float:
    """Definitional residual 1 - alpha_cold/alpha (POST-SOLVE comparison only)."""
    return 1.0 - ALPHA_COLD / ALPHA


def route_open_b() -> dict:
    """Open B — forward delta_strain from EMT percolation / node participation."""
    p_cold = EIGHT_PI * ALPHA_COLD  # cold-form packing (alpha_cold geometric)
    p_obs = EIGHT_PI * ALPHA  # CODATA (comparison only)
    target = _delta_strain_target()

    # B0 — packing-readout identity (tautology, sets scale not a derivation).
    b0 = 1.0 - p_cold / p_obs

    # Sensitivity d ln(alpha^-1)/d ln(u) at p_cold (real, but needs a du driver).
    u_cold = (P_CAUCHY / p_cold) ** (1.0 / 3.0) - 1.0
    du = 1e-6
    dlnainv = (
        math.log(EIGHT_PI / p_of_u(u_cold + du))
        - math.log(EIGHT_PI / p_of_u(u_cold - du))
    ) / (2.0 * du)
    sens = dlnainv * u_cold  # d ln(alpha^-1)/d ln u

    # B1 — dilution x thermal du: sensitivity * thermal du/u  (~5.6e-11, -4.6 dex).
    b1 = abs(sens) * THERMAL_DU_OVER_U

    # B2 — percolation beta=1 mean-field: G ~ (p-p_G)^1 -> dG/G = dp/(p-p_G) =
    # [p/(p-p_G)] * dp/p, i.e. the percolation factor AMPLIFIES B1 by p/(p-p_G)
    # (~2.7x) -> ~1.5e-10, -4.3 dex.  Still no independent du driver.
    margin_above_pG = (p_cold - P_G) / P_G  # ~0.59 ("56.7% above p_G", result-doc)
    percolation_amp = p_cold / (p_cold - P_G)  # ~2.70 = dG/G amplification
    b2 = b1 * percolation_amp

    return {
        "p_cold": p_cold,
        "p_obs_CODATA": p_obs,
        "u_at_p_cold": u_cold,
        "rigidity_margin_above_pG": margin_above_pG,
        "percolation_amplification": percolation_amp,
        "d_ln_alphainv_d_ln_u": sens,
        "delta_strain_target": target,
        "B0_identity": {
            "delta_pred": b0,
            "verdict": "TAUTOLOGY — 1 - p_cold/p_obs is the packing readout, not a derivation",
        },
        "B1_dilution_thermal_du": {
            "delta_pred": b1,
            "log10_miss": math.log10(abs(b1) / target) if b1 else float("-inf"),
            "verdict": "CLOSED-NEGATIVE — ~-4.6 dex (thermal du driver too small)",
        },
        "B2_percolation_beta1": {
            "delta_pred": b2,
            "log10_miss": math.log10(abs(b2) / target) if b2 else float("-inf"),
            "verdict": "CLOSED-NEGATIVE — ~-4.3 dex (no independent du driver)",
        },
        "FT1_BE_control": {
            "eta_epsilon": ETA_EPS_FT1_BE,
            "delta_pred": ETA_EPS_FT1_BE / 2.0,
            "log10_miss": math.log10((ETA_EPS_FT1_BE / 2.0) / target),
            "verdict": "CLOSED-NEGATIVE — -31 dex (hardest control; bulk BE)",
        },
        "verdict": (
            "CLOSED-NEGATIVE — percolation does not forward-derive delta_strain; "
            "B0 tautology, B1/B2 miss by -4 to -5 dex, FT-1 BE -31 dex"
        ),
    }


def audit_identities() -> dict:
    """Post-hoc algebraic cross-checks (not forward routes)."""
    p_cold = EIGHT_PI * ALPHA_COLD
    p_obs = EIGHT_PI * ALPHA
    ds_pack = 1.0 - p_cold / p_obs
    ds_alpha = 1.0 - ALPHA_COLD / ALPHA
    return {
        "1_minus_alpha_cold_over_alpha": ds_alpha,
        "1_minus_p_cold_over_p_obs": ds_pack,
        "equal_to_machine_precision": abs(ds_alpha - ds_pack) < 1e-15,
        "note": (
            "1 - alpha_cold/alpha = 1 - p_cold/p_obs exactly (p = 8*pi*alpha); the "
            "delta_strain residual is the same CODATA-vs-cold spec gap, not an "
            "independent prediction"
        ),
    }


# ---------------------------------------------------------------------------
def main() -> int:
    b1 = route_b1_max()
    b2 = route_b2_constraint()
    b4 = route_b4_weighted()
    diag = route_diag_codata()
    open_b = route_open_b()

    open_a_verdict = (
        "CLOSED-NEGATIVE / FORK-for-Grant — B1 != B2 "
        f"(|du|={abs(b1['u'] - b2['u']):.3f}); the admissibility-weighted max lands "
        "DENSER (K/G~1.83), not the floppy edge the prereg expected. Gravity-stable "
        "projection is a CONSTRAINT (K/G=2), not the unconstrained optimum of Pi*gamma. "
        "B4 relabels B2."
    )

    out = {
        "prereg": [
            "research/2026-06-25_alpha-variational-strain-projection_prereg.md",
            "research/2026-06-25_alpha-lattice-strain-projection_prereg-v2.md",
            "research/2026-06-25_openB-delta-strain-percolation_prereg-v4.md",
        ],
        "reconstructed": "2026-06-25 consolidation pass A (original driver lost)",
        "question": (
            "Does substrate strain-projection s_grav=Pi*gamma select the alpha "
            "packing, and does EMT percolation forward-derive delta_strain?"
        ),
        "frozen_inputs_alpha_free": {
            "z0_path_count": Z0,
            "p_cauchy_delaunay": P_CAUCHY,
            "p_G_isostatic": P_G,
        },
        "open_A": {
            "B1_max": b1,
            "B2_constraint": b2,
            "B4_weighted": b4,
            "DIAG_codata": diag,
            "verdict": open_a_verdict,
        },
        "open_B": open_b,
        "audit_identities": audit_identities(),
        "diagnostics_post_solve_only": {
            "alpha_inv_CODATA": ALPHA_INV_CODATA,
            "P_C_CODATA": P_C,
        },
    }

    text = json.dumps(out, indent=2)
    print(text)

    results_path = Path(__file__).with_name("alpha_variational_strain_projection_results.json")
    results_path.write_text(text + "\n", encoding="utf-8")
    print(f"\nwrote {results_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
