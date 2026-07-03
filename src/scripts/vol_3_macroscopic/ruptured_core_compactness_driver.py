#!/usr/bin/env python3
"""
Ruptured-core neutron-star compactness bound — parametric layered solve.
========================================================================

EXPLORATORY (frontier / potential chord). Prereg:
  research/2026-07-02_ruptured-core-compactness_prereg.md

QUESTION
--------
AVE's lattice-INTACT compactness bound is a SURFACE strain-yield threshold:
    epsilon_11(R) = 7 G M / (c^2 R) < 1   <=>   2GM/(c^2 R) < 2/7 = nu_vac
(ave-compactness-limit.md:12-24). PSR J0740+6620 has surface compactness
C ~ 0.47 (M=2.08 Msun, R=12.39 km, NICER) — ABOVE 2/7, INSIDE the predicted
Regime-IV-core + Regime-III-crust rupture regime. Corroborative at the intact
level. This driver asks: does AVE FORCE a distinct MAX compactness for the
LAYERED (ruptured-core) configuration, and is 0.47 below it?

THE LOAD-BEARING FORK (surfaced to Grant, prereg §3)
----------------------------------------------------
The Regime-IV (ruptured/melted-lattice) EOS is NOT canonically pinned. The
canonical rupture_solver.py shows the SHEAR channel support -> 0 at rupture
(c_shear = c0*sqrt(S) -> 0). The BULK-K channel behavior under COMPRESSION is
the open question. So this driver is PARAMETRIC in the core stiffness sign:

  Reading A (STIFF core):  ruptured core resists further compression with a
    hard floor -> a finite max surface compactness C_max in (2/7, 1) appears.
  Reading B (SOFT core):   shear gone, bulk soft -> no intermediate static
    solution; the only "max" is the Schwarzschild horizon (2GM/c^2R < 1) =
    ECHO, not a distinct chord.

We compute C_max(fork) so that when Grant collapses the fork the headline
verdict falls out immediately. We DO NOT posit the EOS silently.

substrate-native-check (prereg §4):
  CP1  strain-yield threshold, not GR-TOV minimization (TOV used only as a
       flagged non-native cross-check).
  CP2  bulk-K + shear gravitational sector, real-space radial IS native (CP4).
  CP3  objective = "surface compactness at which the layered strain profile
       first admits no static config" — a saturation-BOUNDARY question.
  CP10 rupture at r_t rendered as an interface/boundary condition, not a bulk
       confining force.

ave-canonical-source: NU_VAC, PHI, G, C_0, M_SUN imported from ave.core.constants;
  ruptured-medium behavior from ave.regime_4_rupture.rupture_solver (canonical).
"""

from __future__ import annotations

import numpy as np

# canonical-source cross-check
import ave.core.constants as _avc

# --- canonical imports (ave-canonical-source; no hard-coded physics) ---------
from ave.core.constants import C_0, M_SUN, NU_VAC, PHI, G
from ave.regime_4_rupture.rupture_solver import TopologicalRuptureSolver

assert _avc.__file__.endswith("ave/core/constants.py"), "not canonical constants"
assert abs(NU_VAC - 2.0 / 7.0) < 1e-15, "NU_VAC drift"
assert abs(PHI - (1.0 + np.sqrt(5.0)) / 2.0) < 1e-15, "PHI drift"

C2 = C_0 * C_0
BUCHDAHL_GR = 8.0 / 9.0  # GR incompressible-star Buchdahl bound
# AVE intact surface-yield bound: at yield eps11=7GM/(c^2 R)=1 => C=2GM/(c^2 R)=2/7.
# C_INTACT is the COMPACTNESS bound = NU_VAC = 2/7 (NOT 2*NU_VAC; eps11=(7/2)*C).
C_INTACT = NU_VAC  # = 2/7 ~ 0.2857  (ave-compactness-limit.md:23)


def compactness(M: float, R: float) -> float:
    """Surface compactness 2GM/(c^2 R)."""
    return 2.0 * G * M / (C2 * R)


def epsilon11_surface(M: float, R: float) -> float:
    """AVE principal radial strain at the surface, 7GM/(c^2 R)."""
    return 7.0 * G * M / (C2 * R)


# =====================================================================
# INTACT-BOUND SANITY CHECK (prereg §4 step 1 — must recover 2/7 exactly)
# =====================================================================
def sanity_intact_bound() -> dict:
    """epsilon_11(R)=1  <=>  C = 2/7. Recover exactly."""
    # at yield, 7GM/(c^2 R)=1 => 2GM/(c^2 R) = 2/7
    C_at_yield = 2.0 / 7.0
    # cross-check via strain formula at R = 7GM/c^2
    M = 1.4 * M_SUN
    R_min = 7.0 * G * M / C2
    return {
        "C_intact_yield": C_at_yield,
        "eps11_at_Rmin": epsilon11_surface(M, R_min),  # must be 1.0
        "R_min_1p4Msun_km": R_min / 1e3,  # must be ~14.5 km (leaf line 33)
    }


# =====================================================================
# LAYERED SOLVE — parametric in core stiffness (prereg §4 step 2-3)
# =====================================================================
#
# Model. Two zones sharing the AVE strain control parameter
#   eps11(r) = 7 G m(r) / (c^2 r),  m(r) = enclosed mass.
#
# CRUST (Regime III, r_t <= r <= R): near-yield elastic lattice. It can hold
#   strain up to eps11 = 1 at its INNER edge r_t (the shear-yield shell). The
#   surface sits at eps11(R) = C_surface * 7/2 (since C = 2/7 * eps11).
#
# CORE (Regime IV, 0 <= r <= r_t): shear dead (c_shear -> 0 per rupture_solver).
#   Structural support is bulk-K only. We parametrize the core's ability to
#   hold enclosed mass past yield by a stiffness exponent s >= 0:
#
#     Reading A (STIFF, s large): the ruptured bulk medium can pack additional
#       mass into the core while the *surface* strain stays finite, because the
#       stiffening kernel c_eff^2 = c0^2/sqrt(1-A^2) DIVERGES as A^2->1 — a hard
#       incompressible floor. Max packing -> surface can be pushed to a finite
#       C_max > 2/7 before even the crust yields at the surface.
#
#     Reading B (SOFT, s->0): the ruptured core cannot resist; any surface
#       inside r_sat continues to collapse. No static intermediate. The only
#       terminal state is the BH horizon at C = 1 (r_s), i.e. the "max" is the
#       Schwarzschild limit — an ECHO.
#
# We express the forced max surface compactness as a function of a core
# support fraction f_core in [0,1]:
#   f_core = 0  -> Reading B (soft): C_max -> horizon (C=1) degenerate echo.
#   f_core = 1  -> Reading A (stiff): C_max pinned by the bulk-K incompressible
#                  floor. The natural AVE-native candidate floor is set by the
#                  packing/Poisson structure; we test the two cleanest
#                  substrate-native candidates and report both:
#                    (i)  nu_vac-tied:   C_max = 2/(1+ 2/nu_vac?) ... (see below)
#                    (ii) phi-tied:      C_max related to 1/phi packing.
#
# CRITICAL HONESTY: which candidate (if any) is correct is GATED on the Grant
# fork ruling. We compute all and let the substrate + Grant decide. No silent
# EOS.
# =====================================================================


def layered_cmax_softhard(f_core: float) -> float:
    """
    Forced max surface compactness as a linear-in-support interpolation between
    the intact yield bound (2/7, at f_core=0 in the *no-ruptured-core* limit)
    and the Schwarzschild horizon (C=1, f_core=0 soft-collapse limit).

    NOTE: this is the SOFT-branch interpolation (Reading B family). It shows
    that WITHOUT a hard bulk floor, the ruptured-core "max" slides continuously
    from 2/7 to the horizon C=1 as the core softens — i.e. no distinct bound.
    A distinct chord requires a HARD floor (Reading A) that PINS C_max at a
    specific substrate value; see layered_cmax_hardfloor().
    """
    # soft branch: as the core provides less support, the terminal compactness
    # slides toward the horizon C=1 (pure collapse). No pinned intermediate.
    return C_INTACT + (1.0 - f_core) * (1.0 - C_INTACT)


def layered_cmax_hardfloor(candidate: str) -> float:
    """
    Reading A: a HARD bulk-K floor pins C_max at a substrate-native value.
    We test the cleanest AVE-native candidate floors. NONE is canonically
    derived as a compressed-Regime-IV EOS — they are the candidate anchors the
    substrate offers, reported for the Grant fork.

    Candidates:
      'nu_vac_incompress' : GR-Buchdahl-analog with AVE Poisson nu=2/7 instead
          of nu=1/2. GR Buchdahl 8/9 uses incompressible nu=1/2. Redoing the
          Buchdahl central-pressure-finiteness integral with an EFFECTIVE stiff
          core is what the corpus *labels* "AVE Buchdahl bound" but DERIVES only
          as the surface-yield 2/7. So the hard-floor interior analog would give
          exactly C_max = 2/7 again (the interior can't beat the surface yield)
          UNLESS the ruptured medium is STIFFER than the intact lattice.
      'phi_pack'          : golden-packing floor C_max = 1/phi ~ 0.618 (the same
          phi that sets the cavitation floor rho_cav=-1/phi on the OTHER extreme).
      'horizon'           : C_max = 1 (Schwarzschild), the degenerate echo.
    """
    if candidate == "nu_vac_incompress":
        # A stiff ruptured core that merely recovers the intact surface yield
        # gives back 2/7 — no gain. Reported to show the interior can't beat the
        # surface unless STRICTLY stiffer than intact.
        return C_INTACT
    if candidate == "phi_pack":
        return 1.0 / PHI  # ~0.618, golden-packing candidate
    if candidate == "horizon":
        return 1.0  # Schwarzschild r_s echo
    raise ValueError(candidate)


# =====================================================================
# GR-TOV cross-check (FLAGGED NON-NATIVE, prereg §4 CP1)
# =====================================================================
def gr_buchdahl_reference() -> float:
    """GR incompressible Buchdahl bound 8/9 — borrowed-GR reference only."""
    return BUCHDAHL_GR


# =====================================================================
# PSR J0740 anchor
# =====================================================================
def psr_j0740() -> dict:
    """NICER measurement (Fonseca+2021 / Riley+2021 / Miller+2021 band)."""
    M = 2.08 * M_SUN  # 2.08 +/- 0.07 Msun
    R_central = 12.39e3  # +1.30 -0.98 km
    R_lower = (12.39 - 0.98) * 1e3  # radius lower edge => higher compactness
    return {
        "C_central": compactness(M, R_central),
        "C_upper": compactness(M, R_lower),  # smallest R => largest C
        "eps11_central": epsilon11_surface(M, R_central),
    }


def main() -> None:
    print("=" * 68)
    print("RUPTURED-CORE COMPACTNESS BOUND — parametric layered solve")
    print("EXPLORATORY. Verdict GATED on the Regime-IV EOS fork (Grant).")
    print("=" * 68)

    s = sanity_intact_bound()
    print("\n[1] INTACT-BOUND SANITY (must recover corpus values)")
    print(f"    C_intact (2/7)            = {s['C_intact_yield']:.6f}  (=nu_vac; eps11=(7/2)*C)")
    print(f"    eps11 at R_min            = {s['eps11_at_Rmin']:.6f}  (must be 1.000000)")
    print(f"    R_min(1.4 Msun)           = {s['R_min_1p4Msun_km']:.2f} km  (leaf: 14.5)")

    p = psr_j0740()
    print("\n[2] PSR J0740+6620 (NICER) — the most-compact anchor")
    print(f"    C_surface (central)       = {p['C_central']:.4f}")
    print(f"    C_surface (R lower edge)  = {p['C_upper']:.4f}")
    print(f"    eps11(R) central          = {p['eps11_central']:.4f}  (>1 => ruptured core)")
    print(
        f"    => C = {p['C_central']:.3f} is {'ABOVE' if p['C_central']>C_INTACT else 'below'} 2/7 "
        f"({C_INTACT:.3f}): INSIDE predicted rupture regime (corroborative)"
    )

    print("\n[3] SOFT-branch (Reading B): C_max vs core support fraction f_core")
    print("    (linear slide 2/7 -> horizon; NO pinned intermediate = no chord)")
    for f in (0.0, 0.25, 0.5, 0.75, 1.0):
        print(f"      f_core={f:.2f}  C_max={layered_cmax_softhard(f):.4f}")

    print("\n[4] HARD-floor (Reading A): candidate pinned C_max values")
    for cand in ("nu_vac_incompress", "phi_pack", "horizon"):
        cm = layered_cmax_hardfloor(cand)
        below = "0.47 BELOW it (chord-compatible)" if p["C_central"] < cm else "0.47 ABOVE it (would FALSIFY)"
        distinct = "DISTINCT from Buchdahl 8/9" if abs(cm - BUCHDAHL_GR) > 1e-3 else "= Buchdahl"
        print(f"      {cand:20s} C_max={cm:.4f}  [{distinct}] -> {below}")

    print("\n[5] REFERENCES")
    print(f"    GR Buchdahl bound         = {gr_buchdahl_reference():.4f}")
    print(f"    AVE intact surface yield  = {C_INTACT:.4f}")

    print("\n[6] RUPTURED-MEDIUM SUBSTRATE BEHAVIOR (canonical rupture_solver)")
    # confirm the shear channel dies (soft) and EM is Gamma=0 absorber
    st = TopologicalRuptureSolver.evaluate_rupture_state(np.array([0.5, 0.99, 1.0, 1.2]))
    for i, r in enumerate(st["r"]):
        print(
            f"      r={r:.2f}  S={st['S'][i]:.4f}  c_shear/c0={st['c_shear'][i]/C_0:.4f}  "
            f"ruptured={bool(st['is_ruptured'][i])}"
        )
    print("    => shear (structural) support -> 0 at rupture: leans Reading B unless")
    print("       the BULK-K channel supplies a HARD floor (the Grant fork).")

    print("\n" + "=" * 68)
    print("HEADLINE (GATED): if Grant rules core STIFF + a substrate-clean")
    print("C_max in (2/7, 8/9) with 0.47 < C_max => forward-prediction CHORD.")
    print("If core SOFT => C_max degenerates to horizon => ECHO of Schwarzschild.")
    print("Absent a canonical Regime-IV compression EOS => EOS-GATED NEGATIVE.")
    print("=" * 68)


if __name__ == "__main__":
    main()
