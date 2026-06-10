#!/usr/bin/env python3
"""
Electron-manufacturing FBD: the FORWARD R/r radial-balance check (§4 of the
2026-06-10 electron-manufacturing-process-flow research doc).

QUESTION (forward, never reverse-fit):
    Given the canonical inner boundary condition rho_bar = rho_cav = -1/phi
    (the cavitation floor = the c_eff^2 = 0 root of the CANDIDATE Propulsion EOS
    c_eff^2(rho_bar) = c0^2 * (1 + rho_bar/(1 - rho_bar^2)),
    AVE-Propulsion vol_propulsion/chapters/04_superluminal_transit.tex:86,89),
    a saturation wall at the outer radius, hoop tension from circulation, and
    centrifugal load --- does the static radial force balance PIN the equilibrium
    ratio R/r, and if so does that ratio equal the Golden-Torus phi^2 = 2.618?

DISCIPLINE (ave-live-fire-derivation-provenance, ave-fundamental-ground-up-
implementation, ave-driver-script-honesty):
  * Nothing is printed that was not computed in this run.
  * rho_cav is DERIVED here (root of the candidate EOS), not asserted.
  * phi^2 (= R_GOLDEN_TORUS / R_GOLDEN_TORUS_MINOR) is imported COMPARISON-ONLY,
    never used as an input to the balance.
  * The forward-vs-fit residual test (Step 4 of ave-live-fire-derivation-
    provenance) is run explicitly: we back-solve the outer-wall density that
    WOULD make R/r = phi^2 and show it is non-canonical -> the match is fitted,
    not forward.
  * Bins are frozen: MATCHES-PHI2 / DIFFERENT-VALUE / UNDERDETERMINED. We do NOT
    debug toward phi^2.

OUTPUT: prints the verdict and writes _output/electron_mfg_rr_balance_results.json
"""
import json
import os
import sys

import numpy as np

# Defensive path insert so the script runs standalone AND under `make` (.venv).
_REPO_SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
for _p in (os.path.join(_REPO_SRC, "src"), _REPO_SRC):
    if os.path.isdir(os.path.join(_p, "ave")) and _p not in sys.path:
        sys.path.insert(0, _p)

# Canonical-source imports (ave-canonical-source). PHI is Core-canonical
# (constants.py:199). The Golden-Torus radii are Core-canonical
# (constants.py:200-201); their ratio R/r = phi^2 is the COMPARISON target only.
from ave.core.constants import PHI, R_GOLDEN_TORUS, R_GOLDEN_TORUS_MINOR

PHI2_COMPARISON = R_GOLDEN_TORUS / R_GOLDEN_TORUS_MINOR  # == PHI**2, comparison-only


# ---------------------------------------------------------------------------
# Block 1 -- the cavitation floor as the c_eff^2 = 0 root (DERIVED, parameter-free)
# ---------------------------------------------------------------------------
def c_eff_sq_over_c0sq(rho_bar):
    """Candidate Propulsion EOS, normalized: c_eff^2 / c0^2 = 1 + rho/(1-rho^2)."""
    return 1.0 + rho_bar / (1.0 - rho_bar**2)


def cavitation_root():
    """Negative root of 1 + rho/(1-rho^2) = 0  <=>  rho^2 - rho - 1 = 0.

    Solved from the EOS, NOT asserted as -1/phi. The match to -1/phi is then
    checked.
    """
    # rho^2 - rho - 1 = 0  ->  rho = (1 +/- sqrt(5))/2 ; the physical (tensile,
    # in (-1,0)) root is the negative one.
    roots = np.roots([1.0, -1.0, -1.0])  # coeffs of rho^2 - rho - 1
    neg = float(min(roots))  # (1 - sqrt5)/2 = -0.618...
    return neg


# ---------------------------------------------------------------------------
# Block 2 -- the forward radial balance (hydrostatic + centrifugal), integrated
# ---------------------------------------------------------------------------
# Radial momentum balance for a circulating compressible core (the FBD wedge,
# Sec 3 of the doc): dP/dr = rho * v_theta(r)^2 / r  (centripetal demand met by
# the radial pressure gradient + hoop reaction). With the barotropic EOS
# c_eff^2 = dP/drho and rho = rho0*(1 + rho_bar), this becomes a 1st-order ODE
# in rho_bar(r). Two profile laws are tested as EXPLICIT, NON-CANONICAL choices:
#   (A) v_theta = c0           (rigid lock at the trapped-photon speed)
#   (B) v_theta = Omega*r      (solid-body rotation, the cavprobe's actual config)
# The point of the script is to show what each closure does to R/r.


def G_const_v(rho_bar):
    """Antiderivative of g(rho) = c_eff_sq/c0sq / (1+rho) for the v=const closure.

    For v_theta = c0 the c0^2 cancels and ln(R/r) = G(rho_wall) - G(rho_cav),
    with g(rho) = (1 + rho - rho^2)/((1-rho)(1+rho)^2)
                = 0.25/(1-rho) + 1.25/(1+rho) - 0.5/(1+rho)^2  (partial fractions).
    """
    return -0.25 * np.log(1.0 - rho_bar) + 1.25 * np.log(1.0 + rho_bar) + 0.5 / (1.0 + rho_bar)


def rr_const_v(rho_cav, rho_wall):
    """R/r under the v_theta = c0 closure (the ONLY scale-free closure here)."""
    return float(np.exp(G_const_v(rho_wall) - G_const_v(rho_cav)))


def solid_body_combination(rho_cav, rho_wall):
    """For v_theta = Omega*r the balance pins (Omega^2/2c0^2)*(R^2 - r^2), NOT R/r.

    Returns the dimensionless LHS = G_sb(rho_wall) - G_sb(rho_cav) that equals
    (Omega^2/2c0^2)*(R^2 - r^2). R/r is therefore a free function of the
    unspecified edge Mach Omega*r/c0 -> UNDERDETERMINED by construction.
    """
    # g_sb(rho) = c_eff_sq/c0sq / (1+rho)  (same integrand; here it sets R^2-r^2)
    return float(G_const_v(rho_wall) - G_const_v(rho_cav))


def main():
    out = {}

    # --- Block 1: cavitation floor ---
    rho_cav = cavitation_root()
    minus_inv_phi = -1.0 / PHI
    out["cavitation_floor"] = {
        "rho_cav_from_EOS_root": rho_cav,
        "minus_one_over_phi": minus_inv_phi,
        "abs_diff": abs(rho_cav - minus_inv_phi),
        "one_minus_rhocav_sq": 1.0 - rho_cav**2,
        "equals_one_over_phi": abs((1.0 - rho_cav**2) - 1.0 / PHI),
        "c_eff_sq_at_root_over_c0sq": c_eff_sq_over_c0sq(rho_cav),
        "class": "IDENTITY (parameter-free root of the CANDIDATE Propulsion EOS)",
    }

    # --- Block 2: forward balance under each closure ---
    # Canonical-candidate density landmarks for the OUTER wall, tested honestly:
    landmarks = {
        "plus_1_over_phi (symmetric mirror of floor)": 1.0 / PHI,
        "plus_1_over_phi_sq": 1.0 / PHI**2,
        "plus_one_half": 0.5,
    }
    rr_v_const = {name: rr_const_v(rho_cav, val) for name, val in landmarks.items()}

    # Forward-vs-fit residual test (ave-live-fire Step 4): back-solve the wall
    # density that WOULD yield R/r = phi^2 under the v=const closure.
    from scipy.optimize import brentq

    target = np.log(PHI2_COMPARISON) + G_const_v(rho_cav)
    rho_wall_fit = float(brentq(lambda r: G_const_v(r) - target, 1e-6, 1.0 - 1e-9))

    out["forward_balance"] = {
        "closure_A_v_const": {
            "description": "v_theta = c0 (rigid lock at trapped-photon speed); "
            "the ONLY scale-free closure (c0^2, rho0, Omega all cancel)",
            "RR_at_canonical_landmarks": rr_v_const,
            "none_equals_phi2": all(
                abs(v - PHI2_COMPARISON) > 1e-3 for v in rr_v_const.values()
            ),
            "rho_wall_that_forces_phi2": rho_wall_fit,
            "rho_wall_is_canonical": False,
            "fit_tell": "R/r = phi^2 requires rho_wall ~= %.4f, which is NOT a "
            "canonical density (not 1/phi, not 1/phi^2, not a saturation root). "
            "Forcing phi^2 is therefore FITTED, not forward." % rho_wall_fit,
        },
        "closure_B_solid_body": {
            "description": "v_theta = Omega*r (cavprobe config); the balance pins "
            "(Omega^2/2c0^2)*(R^2 - r^2), a dimensional combination, NOT the ratio R/r",
            "dimensionless_LHS_floor_to_symmetric_wall": solid_body_combination(
                rho_cav, 1.0 / PHI
            ),
            "RR_pinned": False,
            "free_input": "edge Mach M_edge = Omega*r/c0 (sets R/r at fixed R^2-r^2)",
        },
    }

    # --- Verdict (frozen bins) ---
    # The single radial-balance scalar equation + the canonical INNER boundary
    # condition is ONE constraint short of a pure RATIO. Closing it needs a
    # SECOND boundary condition (the outer saturation-wall density rho_wall) AND
    # a circulation-profile law v_theta(r). Neither is fixed by canonical
    # constants; no canonical pair lands on phi^2 parameter-free.
    verdict = "UNDERDETERMINED"
    missing_input = (
        "the OUTER saturation-wall density rho_wall AND the circulation/velocity "
        "profile law v_theta(r). The cavitation-floor inner BC (rho_cav=-1/phi) is "
        "one constraint; a pure ratio R/r needs a second independent canonical BC. "
        "No canonical pair tested lands on phi^2; forcing it needs rho_wall~=0.440 "
        "(non-canonical) -> fitted."
    )
    out["verdict"] = {
        "bin": verdict,
        "rr_forward_value": "not pinned (function of profile + rho_wall)",
        "phi2_comparison": PHI2_COMPARISON,
        "missing_physical_input": missing_input,
        "class": "cannot be graded emergence; inputs do not close the ratio",
        "coordinate_check": "UNADJUDICATED (flagged, not asserted): constants.py:200-201 "
        "labels the Golden-Torus radii real-space major/minor (which, at face value, "
        "would make R/r coordinate-matched to phi^2), BUT vapor-lock doc 24cf3aa4 "
        "framing.md:118 says the two roots are physically unrelated constructions (a "
        "phasor-area embedding vs a bulk-stiffness zero), the torus form appearing only "
        "under a post-hoc x=2R substitution -- i.e. phi^2 may be a PHASE-space "
        "(phasor-area) ratio, making the R/r-vs-phi^2 comparison a coordinate MISMATCH. "
        "Does NOT change the UNDERDETERMINED bin; strengthens do-not-cite-the-phi-link. "
        "The (2,3) phase winding does NOT enter this balance regardless. Real-space-vs-"
        "phasor-area provenance of R_GOLDEN_TORUS surfaced to Grant.",
    }

    # --- emit ---
    outdir = os.path.join(os.path.dirname(__file__), "_output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "electron_mfg_rr_balance_results.json"), "w") as fh:
        json.dump(out, fh, indent=2)

    # --- honest console report (everything below was computed above) ---
    print("=" * 72)
    print("ELECTRON-MANUFACTURING FBD -- FORWARD R/r RADIAL-BALANCE CHECK")
    print("=" * 72)
    print("[Block 1] Cavitation floor (DERIVED root of candidate EOS):")
    print(f"  rho_cav (EOS root)   = {rho_cav:.16f}")
    print(f"  -1/phi               = {minus_inv_phi:.16f}")
    print(f"  |diff|               = {abs(rho_cav - minus_inv_phi):.2e}  -> IDENTITY")
    print(f"  c_eff^2/c0^2 at root = {c_eff_sq_over_c0sq(rho_cav):.2e}  (=0)")
    print("[Block 2] Forward radial balance:")
    print("  closure A (v=c0), R/r at canonical wall landmarks:")
    for name, val in rr_v_const.items():
        print(f"    rho_wall={landmarks[name]:+.4f} [{name}] -> R/r = {val:.4f}")
    print(f"  phi^2 (comparison)   = {PHI2_COMPARISON:.4f}")
    print(f"  rho_wall forcing phi^2 = {rho_wall_fit:.4f}  (NON-canonical -> FITTED)")
    print("  closure B (solid-body): R/r NOT pinned (free edge Mach)")
    print("-" * 72)
    print(f"VERDICT: {verdict}")
    print(f"  missing input: {missing_input}")
    print("=" * 72)


if __name__ == "__main__":
    main()
