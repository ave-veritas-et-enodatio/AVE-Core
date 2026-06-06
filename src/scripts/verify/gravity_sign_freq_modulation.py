#!/usr/bin/env python
"""Verify the gravity-sign frequency-modulation derivation (Class C internal-coherence).

Pre-reg: research/2026-06-05_gravity-sign-frequency-modulation-prereg.md
Result : research/2026-06-05_gravity-sign-frequency-modulation-result.md

Tests Grant's reactive-LC-frequency-modulation framing for weak-field gravity:
gravitational loading drops the per-node LC frequency omega = 1/sqrt(L_eff C_eff)
at INVARIANT impedance Z = sqrt(L_eff/C_eff), and the SIGNAL (group) velocity --
not the phase velocity -- is the lensing observable.

Discipline (ave-canonical-source): G, C_0, L_NODE, Z_0, MU_0, EPSILON_0, M_SUN
are imported from ave.core.constants. NO hard-coded GR targets: the GR deflection
is recomputed from the SAME imported G/C_0/M_SUN via the standard 4GM/bc^2 so the
comparison is apples-to-apples (and the agreement is structural / Class C, NOT a
distinctness claim -- the corpus already classifies weak-field gravity as
'AVE = GR at O(GM/c^2 r)').

NOTE on what this script does and does NOT confirm (Rule 7 honest-closure):
- It CONFIRMS H1 (sign): every candidate SIGNAL speed drops under loading -> n>1.
- It CONFIRMS the c_shear=c_0 sqrt(S) -> index 1/sqrt(S) map exactly.
- It FLAGS H2: the canonical c_EM=c_0/S maps to an index S (<1), NOT 1/S; and the
  canonical Op16 universal wave speed for a propagating wave is c_0 sqrt(S)
  (index 1/sqrt(S)), the SAME index as matter -> the {1/S, 1/sqrt(S)} reactance-
  counting factor-2 does NOT map cleanly from {c_EM, c_shear} and conflicts with
  the canonical 2/7:1/7 Poisson-projection factor-2 (printed side-by-side).
"""

import json
import os
from dataclasses import asdict, dataclass

import numpy as np

from ave.core.constants import (  # canonical AVE constants
    C_0,
    EPSILON_0,
    G,
    L_NODE,
    M_SUN,
    MU_0,
    Z_0,
)

# External observational input (not an AVE constant): solar radius, IAU 2015.
R_SUN_M = 6.957e8


@dataclass
class Check:
    label: str
    detail: str
    passed: bool
    numbers: dict


def sat_kernel(A):
    """Axiom 4 universal saturation kernel S(A) = sqrt(1 - A^2), A = A/A_yield."""
    return np.sqrt(1.0 - A**2)


def phase1_sign():
    """H1 -- does loading drop the SIGNAL speed and give n>1 (light bends toward mass)?

    Model the per-node LC tank under symmetric (gravity-class) loading at operating
    point A (A = A/A_yield in [0,1)); S = sqrt(1-A^2) in (0,1].

    Two lumped reactances each rise as 1/S under their own-sector drive (canonical):
      C_eff = C_0 / S   (metric varactor,  vol4 ch1 eq:varactor)
      L_eff = L_0 / S   (relativistic inductor, vol4 ch1 eq:relativistic_inductor)
    => node LC frequency  omega_node = 1/sqrt(L_eff C_eff) = (1/sqrt(L_0 C_0)) * S
                                     = omega_node,0 * S        -> DROPS as S->0  [time dilation]
    => signal speed through the full LC product (light, both reactances loaded):
         c_light = ell / sqrt(L_eff C_eff) = c_0 * S           -> DROPS  => n_light = 1/S > 1

    Constitutive (small-signal transverse probe) parameters move the OTHER way:
      eps_eff = eps_0 * S,  mu_eff = mu_0 * S   (both < 1)
      => Z = sqrt(mu_eff/eps_eff) = Z_0          (INVARIANT)              [reflectionless]
      => c_EM (phase) = 1/sqrt(mu_eff eps_eff) = c_0/S  -> RISES (>c_0)   [phase racing ahead]
      => c_shear (group/mass) = c_0 sqrt(S)     -> DROPS                  [canonical Op16]

    H1 PASS criterion: every SIGNAL/group candidate (c_light, c_shear, omega_node)
    drops monotonically under loading and yields n>1; the only quantity that rises
    is the phase velocity c_EM, which is NOT the ray observable.
    """
    A = np.linspace(0.0, 0.95, 20)
    S = sat_kernel(A)

    omega_node = S  # in units of omega_node,0 = c_0/ell_node
    c_light = C_0 * S  # both reactances loaded (signal)
    c_shear = C_0 * np.sqrt(S)  # group / mass-freeze (canonical Op16)
    c_EM = C_0 / S  # Maxwell PHASE velocity (constitutive)
    Z_local = np.sqrt((MU_0 * S) / (EPSILON_0 * S))  # invariant check

    n_light = C_0 / c_light  # = 1/S
    n_shear = C_0 / c_shear  # = 1/sqrt(S)
    n_EM = C_0 / c_EM  # = S  (<1, NOT a bending index)

    # Monotonic drops (ignore A=0 where derivative is 0).
    dd = lambda x: np.all(np.diff(x[1:]) < 0)
    signal_drops = dd(omega_node) and dd(c_light) and dd(c_shear)
    indices_gt1 = np.all(n_light[1:] > 1.0) and np.all(n_shear[1:] > 1.0)
    phase_rises = np.all(np.diff(c_EM[1:]) > 0)
    Z_invariant = np.allclose(Z_local, Z_0)

    passed = bool(signal_drops and indices_gt1 and phase_rises and Z_invariant)
    return Check(
        label="Phase1 SIGN: loading drops signal speed -> n>1 (bends toward mass)",
        detail=(
            "omega_node, c_light, c_shear all DROP under loading; n_light=1/S>1, "
            "n_shear=1/sqrt(S)>1; phase c_EM=c_0/S RISES (not the ray observable); "
            "Z=Z_0 invariant (reflectionless)."
        ),
        passed=passed,
        numbers={
            "signal_speeds_drop_monotonically": bool(signal_drops),
            "bending_indices_gt_1": bool(indices_gt1),
            "phase_velocity_c_EM_rises": bool(phase_rises),
            "Z_local_invariant_eq_Z0": bool(Z_invariant),
            "Z_local_over_Z0_max_dev": float(np.max(np.abs(Z_local / Z_0 - 1.0))),
            "at_A_0p5": {
                "S": float(sat_kernel(0.5)),
                "omega_node_over_omega0": float(sat_kernel(0.5)),
                "c_light_over_c0": float(sat_kernel(0.5)),
                "c_shear_over_c0": float(np.sqrt(sat_kernel(0.5))),
                "c_EM_over_c0": float(1.0 / sat_kernel(0.5)),
                "n_light": float(1.0 / sat_kernel(0.5)),
                "n_shear": float(1.0 / np.sqrt(sat_kernel(0.5))),
                "n_EM": float(sat_kernel(0.5)),
            },
        },
    )


def phase2_factor2_and_map():
    """H2 -- exact c_EM/c_shear <-> index map, and the {1/S,1/sqrt(S)} factor-2.

    EXACT index map from the canonical speeds (n = c_0 / c_signal):
       c_shear = c_0 sqrt(S)  ->  n_shear = 1/sqrt(S)          [matter / group / clock]
       c_EM    = c_0 / S      ->  n_EM    = S   (<1)            [phase; NOT a bending index]
       c_light = c_0 S        ->  n_light = 1/S                 [both-reactance signal]

    The brief's H2 reactance-counting factor-2:
       (n_light - 1)/(n_shear - 1) = (1/S - 1)/(1/sqrt(S) - 1)  -> 2 as S->1  (verified)

    FLAG (flag-don't-fix): this reactance-counting ratio is 2 in the weak-loading
    limit, but it is a DIFFERENT mechanism from the canonical 2/7:1/7 Poisson
    projection, and it conflicts with canonical Op16 (the universal wave speed of a
    PROPAGATING wave is c_0 sqrt(S) -> index 1/sqrt(S), i.e. light would share the
    matter index 1/sqrt(S), giving ratio 1, not 2). Also c_EM=c_0/S maps to index S,
    NOT 1/S -- so 'n_light=1/S' cannot be the c_EM index. Both facts are asserted
    here and checked, NOT reconciled.
    """
    # exact map at a sample S
    S0 = 0.8
    n_shear_map = 1.0 / np.sqrt(S0)
    n_EM_map = S0  # c_EM = c_0/S -> index S
    n_light_map = 1.0 / S0
    map_exact = (
        np.isclose(n_shear_map, C_0 / (C_0 * np.sqrt(S0)))
        and np.isclose(n_EM_map, C_0 / (C_0 / S0))
        and np.isclose(n_light_map, C_0 / (C_0 * S0))
    )

    # factor-2 in the weak-loading limit (S = 1 - eps, eps->0)
    eps = np.array([1e-2, 1e-3, 1e-4, 1e-5, 1e-6])
    S = 1.0 - eps
    ratio = (1.0 / S - 1.0) / (1.0 / np.sqrt(S) - 1.0)
    ratio_limit = ratio[-1]
    factor2_limit = np.isclose(ratio_limit, 2.0, atol=1e-4)

    # canonical Op16 says a propagating wave uses c_0 sqrt(S) -> index 1/sqrt(S):
    # if light ALSO used 1/sqrt(S), the matter:light ratio would be 1.
    op16_light_index = 1.0 / np.sqrt(S0)  # == n_shear_map
    op16_conflict = np.isclose(op16_light_index, n_shear_map)  # True => same index

    # canonical 2/7 : 1/7 Poisson factor-2 (C8) -- the corpus mechanism
    poisson_ratio = (2.0 / 7.0) / (1.0 / 7.0)
    poisson_factor2 = np.isclose(poisson_ratio, 2.0)

    passed = bool(map_exact and factor2_limit and poisson_factor2)
    return Check(
        label="Phase2 MAP+factor2: c_EM/c_shear<->index exact; {1/S,1/sqrt S} ratio->2 (FLAGGED)",
        detail=(
            "c_shear->1/sqrt(S), c_EM->S (NOT 1/S), c_light(both reactances)->1/S exactly. "
            "Reactance-counting (n_light-1)/(n_shear-1)->2 in weak limit, BUT this is a "
            "different mechanism than canonical 2/7:1/7 Poisson, and conflicts with Op16 "
            "(propagating-wave index = 1/sqrt(S) = matter index -> ratio 1). NOT reconciled."
        ),
        passed=passed,
        numbers={
            "index_map_exact": bool(map_exact),
            "n_shear_from_c_shear": float(n_shear_map),
            "n_EM_from_c_EM_is_S_not_inv_S": float(n_EM_map),
            "n_light_from_c_light": float(n_light_map),
            "reactance_ratio_weaklimit": float(ratio_limit),
            "reactance_factor2_in_limit": bool(factor2_limit),
            "reactance_ratio_vs_eps": {f"{e:.0e}": float(r) for e, r in zip(eps, ratio)},
            "op16_light_index_equals_matter_index_FLAG": bool(op16_conflict),
            "canonical_poisson_2_7_over_1_7": float(poisson_ratio),
            "canonical_poisson_factor2": bool(poisson_factor2),
        },
    )


def phase4_lensing_numbers():
    """Lensing numbers via the canonical Snell-gradient kernel delta = 2K*GM/(bc^2).

    Canonical photon index (C8/companion PPN audit): n_perp = 1 + (2/7)*chi_vol,
    chi_vol = 7GM/(c^2 r) => slope K=2 => delta_light = 4GM/bc^2 (Einstein).
    Matter (Soldner / scalar 1/7 projection): slope K=1 => delta_matter = 2GM/bc^2.

    GR target recomputed from the SAME imported G/C_0/M_SUN (no hard-coded GR value).
    This is a Class C consistency check (AVE = GR at this order BY CONSTRUCTION).
    """
    b = R_SUN_M
    # canonical Snell-gradient deflection for n = 1 + K*GM/(c^2 r): delta = 2K*GM/(bc^2)
    K_light = 2.0  # (2/7) photon index, slope 2
    K_matter = 1.0  # (1/7) matter index, slope 1
    delta_light = 2.0 * K_light * G * M_SUN / (b * C_0**2)  # = 4GM/bc^2
    delta_matter = 2.0 * K_matter * G * M_SUN / (b * C_0**2)  # = 2GM/bc^2
    gr_einstein = 4.0 * G * M_SUN / (b * C_0**2)  # recomputed from imported constants

    to_arcsec = 180.0 / np.pi * 3600.0
    light_as = delta_light * to_arcsec
    matter_as = delta_matter * to_arcsec
    gr_as = gr_einstein * to_arcsec

    ratio_light_matter = delta_light / delta_matter  # must be 2 (Einstein/Soldner)
    ratio_light_gr = delta_light / gr_einstein  # must be 1 (Class C, by construction)

    passed = bool(
        np.isclose(ratio_light_matter, 2.0)
        and np.isclose(ratio_light_gr, 1.0)
        and np.isclose(light_as, 1.75, atol=0.02)
    )
    return Check(
        label="Phase4 LENSING: canonical (2/7) photon index -> 4GM/bc^2 = GR (Class C)",
        detail=(
            "Snell-gradient delta=2K*GM/bc^2; light K=2 (2/7 index) -> 1.75'' = Einstein; "
            "matter K=1 (1/7) -> Soldner; ratio 2. GR recomputed from imported G (no target)."
        ),
        passed=passed,
        numbers={
            "delta_light_arcsec": float(light_as),
            "delta_matter_arcsec": float(matter_as),
            "GR_einstein_arcsec_recomputed": float(gr_as),
            "ratio_light_over_matter": float(ratio_light_matter),
            "ratio_light_over_GR": float(ratio_light_gr),
            "observed_solar_deflection_arcsec": 1.75,
        },
    )


def main():
    checks = [phase1_sign(), phase2_factor2_and_map(), phase4_lensing_numbers()]

    out = {
        "constants_imported": {
            "G": G,
            "C_0": C_0,
            "L_NODE": L_NODE,
            "Z_0": Z_0,
            "MU_0": MU_0,
            "EPSILON_0": EPSILON_0,
            "M_SUN": M_SUN,
            "source": "ave.core.constants",
        },
        "external_inputs": {"R_SUN_M": R_SUN_M, "source": "IAU 2015 solar radius"},
        "checks": [asdict(c) for c in checks],
        "verdict": {
            "H1_sign_confirmed": checks[0].passed,
            "H2_map_exact_but_factor2_mechanism_FLAGGED": checks[1].passed,
            "lensing_class_C_consistency": checks[2].passed,
            "note": (
                "H1 (sign) PASS: signal speed drops -> n>1 -> bends toward mass, Z invariant. "
                "c_EM (phase) rises but is not the ray observable. "
                "H2 FLAG: {1/S,1/sqrt(S)} reactance-counting gives the NUMBER 2 but is a "
                "different mechanism than canonical 2/7:1/7 Poisson and conflicts with Op16 "
                "(propagating-wave index = 1/sqrt(S) = matter index). c_EM=c_0/S maps to "
                "index S, NOT 1/S. NOT reconciled -- surfaced for Grant adjudication."
            ),
        },
    }

    here = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(here, "gravity_sign_freq_modulation_results.json")
    with open(json_path, "w") as f:
        json.dump(out, f, indent=2)

    print("=" * 72)
    print("GRAVITY SIGN via reactive LC frequency-modulation -- verification")
    print("=" * 72)
    print(f"Imported from ave.core.constants: G={G:.6e}  C_0={C_0:.6e}")
    print(f"  L_NODE={L_NODE:.6e}  Z_0={Z_0:.4f}")
    print("-" * 72)
    for c in checks:
        status = "PASS" if c.passed else "FLAG/REVIEW"
        print(f"[{status}] {c.label}")
        print(f"        {c.detail}")
        for k, v in c.numbers.items():
            print(f"          {k}: {v}")
        print()
    print("-" * 72)
    v = out["verdict"]
    print(f"H1 sign confirmed                : {v['H1_sign_confirmed']}")
    print(f"H2 map exact / factor2 FLAGGED   : {v['H2_map_exact_but_factor2_mechanism_FLAGGED']}")
    print(f"Lensing Class-C consistency      : {v['lensing_class_C_consistency']}")
    print(f"\nWrote {json_path}")
    # Exit 0 always: this is a research-verification artifact, not a CI gate, and the
    # H2 FLAG is an intentional surfaced finding (Rule 6 flag-don't-fix), not a failure.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
