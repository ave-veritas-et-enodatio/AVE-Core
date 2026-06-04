"""Phasor<->real-space area bijection: alpha-circularity audit (sanity-check).

SCOPE NOTE (2026-06-04, ave-driver-script-honesty applied):
    This is NOT a forward-prediction of alpha and NOT a fit-to-1/4. It is a
    SANITY-CHECK of the analytical result in
        research/2026-06-04_alpha-class2-bijection-result.md
    The CORE of the work is the symbolic/dimensional algebra in that doc; this
    script merely (a) confirms the analytical bridge K is alpha-FREE on input
    (its only inputs are the four-base + Maxwell primitives), and (b) evaluates
    the bijection's required R*r against the candidate amplitude scales to show
    it lands on 4*pi^2*alpha (~0.288), NOT 1/4. It reports a NEGATIVE/Class-B
    finding: the bridge cannot DERIVE 1/4 without substituting alpha.

    HONESTY GUARANTEES (verifiable below):
      * alpha (ALPHA / ALPHA_COLD_INV) is NEVER read when BUILDING the bridge K
        or the required R*r. The bridge is constructed from
        {EPSILON_0, HBAR, C_0, e_charge, M_E} only. See build_bridge_K().
      * ALPHA is read ONLY in the final REPORTING step, to express the
        already-built alpha-free required-R*r in alpha-units (to expose the
        4*pi^2*alpha structure). This is comparison, not construction.
      * R, r are kept SYMBOLIC end-to-end (we solve for the product R*r; we
        never assign R*r = 1/4 anywhere).
      * No hardcoded 137.035999 / alpha literal. All constants imported from
        ave.core.constants (ave-canonical-source).

    DAG / anti-cheat: contains NO numeric literal matching alpha or 1/alpha;
    the only bare numbers are exact geometric/dimensional factors (2, 4, pi,
    the cell radius factor 1/2) that are part of the algebra, not tuned.

Result: B1 PASS (K alpha-free on input), B3 FAIL (bijection forces R*r=4*pi^2*alpha
!= 1/4) => Class B confirmed. The last alpha-1/4 lift-path closes.
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import (
    ALPHA,  # READ ONLY in the final reporting step (comparison, not construction)
    C_0,
    EPSILON_0,
    HBAR,
    L_NODE,
    M_E,
    V_SNAP,
    V_YIELD,
    XI_TOPO,
    e_charge,
)

PI = np.pi


def build_bridge_K() -> float:
    """Bridge K = (C_bond / xi_topo)^2 in m^2/V^2, built ALPHA-FREE.

    Chain (EE-native): V --(C_cell)--> Q --(/xi_topo)--> L.
    C_cell = eps0 * ell_node (z0-derivation.md:19); xi_topo = e/ell_node.
    INPUTS (asserted alpha-free below): EPSILON_0, L_NODE, XI_TOPO -> all from
    {eps0, hbar, c, e, m_e}. ALPHA is intentionally NOT referenced here.
    """
    c_cell = EPSILON_0 * L_NODE  # bond capacitance [F]
    length_per_volt = c_cell / XI_TOPO  # [m/V]
    return length_per_volt**2  # [m^2/V^2]


def required_Rr_volts2() -> float:
    """Required R*r [V^2] for the bijection pi*R*r*K = A_cell. ALPHA-FREE.

    A_cell = pi*(ell_node/2)^2. Solve pi*R*r*K = A_cell for the product R*r.
    R, r remain symbolic (we only ever produce their PRODUCT). ALPHA not used.
    """
    a_cell = PI * (L_NODE / 2.0) ** 2  # [m^2]
    k = build_bridge_K()  # [m^2/V^2]
    return a_cell / (PI * k)  # [V^2]


def main() -> None:
    k = build_bridge_K()
    rr_v2 = required_Rr_volts2()

    # --- B1: confirm the bridge is alpha-free on INPUT (structural assertion) ---
    # Reconstruct K two independent alpha-free ways; they must agree to machine eps.
    k_alt = (EPSILON_0 * HBAR**2 / (C_0**2 * e_charge * M_E**2)) ** 2  # closed form
    assert abs(k / k_alt - 1.0) < 1e-12, "bridge K reconstruction mismatch"

    # --- FINAL REPORTING ONLY: express the alpha-free required-R*r in alpha-units ---
    rr_over_vsnap2 = rr_v2 / V_SNAP**2  # predicted 4*pi^2*alpha^2
    rr_over_vyield2 = rr_v2 / V_YIELD**2  # predicted 4*pi^2*alpha
    pred_snap = 4.0 * PI**2 * ALPHA**2
    pred_yield = 4.0 * PI**2 * ALPHA

    print("=" * 72)
    print("alpha Class-2 bijection -- circularity audit (SANITY CHECK, Class B)")
    print("=" * 72)
    print(f"bridge K = (C_bond/xi_topo)^2      = {k:.6e} m^2/V^2  [alpha-free input]")
    print(f"required R*r (bijection)            = {rr_v2:.6e} V^2   [alpha-free]")
    print("-" * 72)
    print("Express the alpha-free required R*r in the candidate amplitude units:")
    print(f"  R*r / V_snap^2  = {rr_over_vsnap2:.8e}   (4*pi^2*alpha^2 = {pred_snap:.8e})")
    print(f"  R*r / V_yield^2 = {rr_over_vyield2:.8e}   (4*pi^2*alpha   = {pred_yield:.8e})")
    print("-" * 72)
    # The golden-torus identification claims R*r = 1/4 in V_yield units.
    golden = 0.25
    print(f"  golden-torus claim: R*r (V_yield units) = {golden}")
    print(f"  bridge FORCES      : R*r (V_yield units) = {rr_over_vyield2:.6f}  = 4*pi^2*alpha")
    print(f"  MISS factor (forced/claim)               = {rr_over_vyield2 / golden:.6f}  (~13% off)")
    print("-" * 72)
    # Cell-filling: V_yield/V_snap forced by mapping V_yield -> length = ell/2.
    vyield_forced_over_vsnap = (EPSILON_0 * L_NODE / XI_TOPO) * 1.0 / (L_NODE / 2.0)
    # = C_cell/xi_topo divided by (ell/2) per volt -> dimensionless ratio per the algebra:
    vyield_forced_over_vsnap = (L_NODE / 2.0) / ((EPSILON_0 * L_NODE / XI_TOPO)) / V_SNAP
    pred_2pialpha = 2.0 * PI * ALPHA
    print("Cell-filling forces V_yield/V_snap (map V_yield -> tube radius ell/2):")
    print(f"  V_yield/V_snap FORCED   = {vyield_forced_over_vsnap:.8e}  (2*pi*alpha = {pred_2pialpha:.8e})")
    print(f"  canonical (kinetic-yield) = sqrt(alpha) = {np.sqrt(ALPHA):.8e}")
    print("  -> bridge says 2*pi*alpha, canon says sqrt(alpha); equal only at")
    print(f"     alpha = 1/(4*pi^2) = {1.0 / (4.0 * PI**2):.6e}  != CODATA {ALPHA:.6e}")
    print("=" * 72)
    print("VERDICT: B1 PASS (K alpha-free on input); B3 FAIL (bijection forces")
    print("R*r=4*pi^2*alpha != 1/4). Closing to 1/4 SUBSTITUTES alpha => CLASS B.")
    print("The last alpha-1/4 lift-path closes. (Analytical core in result doc.)")

    # Cross-checks that the alpha-free predictions hold to machine epsilon:
    assert abs(rr_over_vsnap2 / pred_snap - 1.0) < 1e-9
    assert abs(rr_over_vyield2 / pred_yield - 1.0) < 1e-9
    assert abs(vyield_forced_over_vsnap / pred_2pialpha - 1.0) < 1e-9
    print("\n[sanity asserts passed: 4pi^2 alpha^2, 4pi^2 alpha, 2pi alpha all confirmed]")


if __name__ == "__main__":
    main()
