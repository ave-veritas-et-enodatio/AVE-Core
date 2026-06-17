"""BH accretion-disk inner-edge vs GR Kerr ISCO — forward-prereg driver.

Backs PRONG 2 of `research/2026-06-17_bh-shear-echo-forward-prereg.md`
(FROZEN, SHA-pinned to main @ 04bcb4ac).

AVE prediction: matter cannot exist inside r_sat = 7 G M/c^2 = 7 r_g (Regime-IV
ruptured topology), so the inner disk edge sits at/just outside r_sat.
  - r_sat = (2/nu_vac) r_g = 7 r_g, nu_vac = 2/7      (parameter-free)
  - GR Kerr ISCO r_isco(a_*) runs 6 r_g (a_*=0) down to ~1 r_g (prograde,
    a_*->1) and up to ~9 r_g (retrograde) -- Bardeen-Press-Teukolsky 1972.

This driver tabulates the AVE 7 r_g floor against the GR Kerr ISCO across spin,
and flags where the discriminator is CLEAN (AVE outside GR ISCO) vs DEGENERATE
(retrograde high-spin: GR ISCO outside 7 r_g, offset sign flips).

substrate-first: nu_vac = 2/7 from ave.core.constants (parameter-free); the GR
ISCO is the GR-counterfactual comparison target (ave-discrimination-check).
"""

from __future__ import annotations

import json

import numpy as np

from ave.core import constants as K

NU_VAC = K.NU_VAC  # 2/7
R_SAT_OVER_RG = 2.0 / NU_VAC  # = 7  (AVE matter floor, in units of r_g = GM/c^2)


def r_isco_kerr(a: float, prograde: bool = True) -> float:
    """GR Kerr ISCO radius in units of r_g = GM/c^2 (Bardeen-Press-Teukolsky 1972)."""
    z1 = 1.0 + (1.0 - a**2) ** (1.0 / 3.0) * (
        (1.0 + a) ** (1.0 / 3.0) + (1.0 - a) ** (1.0 / 3.0)
    )
    z2 = np.sqrt(3.0 * a**2 + z1**2)
    sign = -1.0 if prograde else 1.0
    return 3.0 + z2 + sign * np.sqrt((3.0 - z1) * (3.0 + z1 + 2.0 * z2))


def main() -> None:
    spins = [0.0, 0.3, 0.5, 0.67, 0.74, 0.9, 0.998]
    rows = []
    for a in spins:
        rp = r_isco_kerr(a, prograde=True)
        rr = r_isco_kerr(a, prograde=False)
        rows.append(
            {
                "a_star": a,
                "gr_isco_prograde_rg": round(rp, 3),
                "gr_isco_retrograde_rg": round(rr, 3),
                "ave_floor_rg": R_SAT_OVER_RG,
                # clean discriminator iff AVE floor is OUTSIDE the GR ISCO
                "prograde_clean": bool(R_SAT_OVER_RG > rp),
                "retrograde_clean": bool(R_SAT_OVER_RG > rr),
            }
        )

    out = {
        "nu_vac": NU_VAC,
        "ave_matter_floor_rg": R_SAT_OVER_RG,
        "gr_a0_isco_rg": 6.0,
        "ave_vs_gr_a0_ratio": R_SAT_OVER_RG / 6.0,  # = 7/6 frozen offset
        "rows": rows,
        "note": (
            "AVE 7 r_g is OUTSIDE every prograde GR ISCO (clean), but INSIDE the "
            "retrograde GR ISCO for a_* >~ 0.45 (degenerate / sign-flipped). Clean "
            "discriminator requires independently-known or jointly-fit spin; "
            "frozen falsifier scoped to a_*=0 / low-spin / known-spin systems."
        ),
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
