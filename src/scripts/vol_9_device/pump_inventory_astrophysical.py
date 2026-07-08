"""pump_inventory_astrophysical.py — PUMP INVENTORY (P6 make-or-break gate).

Does any astrophysical environment PUMP the AVE nonlinear vacuum birefringence to
an observable level, thereby turning existing observations (IXPE magnetar
birefringence, GRB polarization, cosmic birefringence) into real bounds on the
AVE sidereal Lorentz-violation flagship — or does AVE's own physics make space
transparent?

Grounded functionals (cited, NOT re-derived here):
  µ-grade (magnetic):  S_B = sqrt(1 - A_I^2), A_I = |curl H| * l_node^2 / I_max
                       (P5, research/2026-07-08_p5-radiative-far-field-keying_RESULT.md).
                       STATIC B => curl H = 0 => A_I = 0 => S_B = 1 => dn_mu = 0  (FORK-1).
  eps-grade (electric): S_eps = sqrt(1 - A_V^2), A_V = |E|/E_YIELD, charge-keyed
                       mean-square (round-3, .../2026-07-06_em-keying-round3-...RESULT.md).
  birefringence:       dn_bir = -1/2 A^2 on the loaded coordinate (ave.bench.birefringence).

ALL astrophysical field / luminosity / distance values are EXTERNAL literature
inputs, tagged EXTERNAL and cited by result. Constants imported from
ave.core.constants; birefringence from ave.bench.birefringence (ave-canonical-source).

Run:  PYTHONPATH=src python3 src/scripts/vol_9_device/pump_inventory_astrophysical.py
"""

from __future__ import annotations

import json
import math
import os
from dataclasses import asdict, dataclass

import numpy as np

from ave.bench.birefringence import (
    delta_n_ave_differential_exact,
    delta_n_qed_magnetic,
    vacuum_magnetic_birefringence_constant,
)
from ave.core.constants import (
    ALPHA,
    B_SNAP,
    C_0,
    E_CRIT,
    E_YIELD,
    EPSILON_0,
    K_B,
    L_NODE,
    XI_TOPO,
    e_charge,
)

# Derived canonical scales (imported provenance; NOT re-minted)
I_MAX = XI_TOPO * C_0          # e c / l_node  ~ 124.4 A  (P5 series-inductor I_max)
B_DUAL = E_YIELD / C_0         # field-amplitude-matched magnetic duality scale ~ 3.77e8 T

# ---- standard (non-AVE) physical constants used for blackbody radiation fields ----
# K_B and e_charge imported from ave.core.constants (canonical); SIGMA_SB / A_RAD are
# radiation constants not in the AVE canon (standard CODATA, external).
SIGMA_SB = 5.670374419e-8      # Stefan-Boltzmann [W m^-2 K^-4]  (CODATA, standard)
A_RAD = 7.565733e-16           # radiation-density constant [J m^-3 K^-4] (= 4 sigma/c)
KEV_TO_K = 1.0e3 * e_charge / K_B  # 1 keV in Kelvin ~ 1.16e7 K

A_LAB_SQ = 6.0e-7              # flagship lab pump A^2 (the Letter's own pump; comparison anchor)


# ============================================================================
# 0. CANONICAL SELF-CHECK (verify_constants surrogate — ave-canonical-source)
# ============================================================================
def canonical_self_check() -> dict:
    checks = {
        "E_YIELD~1.13e17": math.isclose(E_YIELD, 1.13e17, rel_tol=5e-3),
        "I_max~124.4A": math.isclose(I_MAX, 124.4, rel_tol=5e-3),
        "B_dual~3.77e8T": math.isclose(B_DUAL, 3.77e8, rel_tol=5e-3),
        "B_SNAP~1.89e9T": math.isclose(B_SNAP, 1.89e9, rel_tol=5e-3),
        "A_e~1.32e-24": math.isclose(vacuum_magnetic_birefringence_constant(), 1.32e-24, rel_tol=1e-2),
    }
    assert all(checks.values()), f"canonical self-check FAILED: {checks}"
    return checks


# ============================================================================
# helpers — radiation E-field from luminosity / flux / energy density (EXTERNAL)
# ============================================================================
def e_rms_from_intensity(intensity_w_m2: float) -> float:
    """RMS E-field of an EM radiation field of given intensity: I = eps0 c E_rms^2."""
    return math.sqrt(intensity_w_m2 / (EPSILON_0 * C_0))


def intensity_from_luminosity(lum_w: float, radius_m: float) -> float:
    return lum_w / (4.0 * math.pi * radius_m**2)


def e_rms_from_energy_density(u_j_m3: float) -> float:
    """RMS E-field of a radiation bath of energy density u: u = eps0 E_rms^2 (plane-wave avg)."""
    return math.sqrt(u_j_m3 / EPSILON_0)


def a_v_of_E(E_v_m: float) -> float:
    return E_v_m / E_YIELD


# ============================================================================
# 1. FORK-1 — COMPUTE S_B(magnetar B) from curl H.  Do NOT assume A_I = 0.
# ============================================================================
def curl_center(field: np.ndarray, h: float) -> np.ndarray:
    """Discrete curl of a vector field sampled on a uniform 3D grid, at the center cell.

    field shape (3, N, N, N). Returns the 3-vector curl at the central node using
    numpy central differences (O(h^2))."""
    Fx, Fy, Fz = field[0], field[1], field[2]
    # np.gradient axis order: axis0->x, axis1->y, axis2->z
    dFz_dy = np.gradient(Fz, h, axis=1)
    dFy_dz = np.gradient(Fy, h, axis=2)
    dFx_dz = np.gradient(Fx, h, axis=2)
    dFz_dx = np.gradient(Fz, h, axis=0)
    dFy_dx = np.gradient(Fy, h, axis=0)
    dFx_dy = np.gradient(Fx, h, axis=1)
    curl = np.stack([dFz_dy - dFy_dz, dFx_dz - dFz_dx, dFy_dx - dFx_dy])
    c = (field.shape[1] - 1) // 2
    return curl[:, c, c, c]


def uniform_static_B(B_mag: float, n: int, h: float) -> np.ndarray:
    """A source-free spatially-uniform static B along z, magnitude B_mag."""
    fld = np.zeros((3, n, n, n))
    fld[2, :, :, :] = B_mag
    return fld


def dipole_field(n: int, h: float, r0: float) -> np.ndarray:
    """A magnetic dipole (moment along z) sampled on an n^3 grid centered at (r0,0,0),
    grid spacing h (same units as r0).  Source-free in the sampled region (grid excludes
    the origin) => curl B = 0 analytically; the discrete curl is an O(h^2) residual that
    -> 0 as h -> 0 WHEN the source is RESOLVED (grid extent a finite fraction of r0)."""
    c = (n - 1) // 2
    axis = (np.arange(n) - c) * h
    X, Y, Z = np.meshgrid(axis + r0, axis, axis, indexing="ij")
    r = np.sqrt(X**2 + Y**2 + Z**2)
    rx, ry, rz = X / r, Y / r, Z / r
    mdotr = rz  # m = z_hat
    Bx = (3 * mdotr * rx) / r**3
    By = (3 * mdotr * ry) / r**3
    Bz = (3 * mdotr * rz - 1.0) / r**3
    return np.stack([Bx, By, Bz])


def curl_over_field_center(field: np.ndarray, h: float) -> float:
    """|curl B| / |B| at the center cell (dimensionless operator residual)."""
    curl = curl_center(field, h)
    c = (field.shape[1] - 1) // 2
    Bc = math.sqrt(field[0, c, c, c] ** 2 + field[1, c, c, c] ** 2 + field[2, c, c, c] ** 2)
    return float(np.linalg.norm(curl) / Bc)


def circulation_control_field(B0: float, n: int, h: float, r_scale: float) -> np.ndarray:
    """POSITIVE CONTROL (can-fire): a field WITH genuine circulation,
    B = (B0/r_scale) * (-y, x, 0)  =>  curl B = (0,0, 2 B0/r_scale) != 0.
    Physically this is what a current-carrying / AC-driven region looks like
    (curl H = J_free + dD/dt != 0). Proves the curl operator returns NONZERO
    when circulation is present -- so the static-B zero is an informative null."""
    c = (n - 1) // 2
    axis = (np.arange(n) - c) * h
    X, Y, _ = np.meshgrid(axis, axis, axis, indexing="ij")
    Bx = -(B0 / r_scale) * Y
    By = (B0 / r_scale) * X
    Bz = np.zeros_like(X)
    return np.stack([Bx, By, Bz])


def a_I_from_field(field: np.ndarray, h: float) -> float:
    """A_I = |curl H| * l_node^2 / I_max, H = B/mu0 (mu0 cancels in the ratio to I_max
    since I_max = curl-of-H bandwidth). We compute |curl B|/mu0 * l_node^2 / I_max."""
    from ave.core.constants import MU_0

    curlB = curl_center(field, h)
    curlH_mag = np.linalg.norm(curlB) / MU_0
    return curlH_mag * L_NODE**2 / I_MAX


def fork1_static_B_test() -> dict:
    """COMPUTE A_I and S_B for a static magnetar-strength B. The null must EMERGE
    from curl H, not be asserted. Four pieces:
      (a) uniform static B at 1e11 T   -> A_I = 0 EXACTLY (physical magnetar-local case);
      (b) dipole at magnetar geometry  -> A_I machine-zero (true residual ~(l_node/r0)^2);
      (c) resolvable-dipole convergence-> |curl B|/|B| -> 0 as O(h^2) (operator returns the
          source-free zero, not a dead operator);
      (d) POSITIVE CONTROL (circulation field) -> A_I > 0 (curl operator CAN fire)."""
    B_MAGNETAR = 1.0e11  # EXTERNAL: magnetar surface B ~ 1e14-1e15 G = 1e10-1e11 T
    n, h = 11, L_NODE

    # (a) uniform static B -> A_I from curl H of a uniform field
    fld_u = uniform_static_B(B_MAGNETAR, n, h)
    A_I_uniform = a_I_from_field(fld_u, h)
    S_B_uniform = math.sqrt(max(0.0, 1.0 - A_I_uniform**2))
    dn_mu_uniform = delta_n_from_A(A_I_uniform)

    # (b) dipole at true magnetar geometry (source at r0 = 1e4 m; grid = node scale),
    #     center |B| normalized to B_MAGNETAR so A_I is the PHYSICAL residual.
    r0_phys = 1.0e4
    fld_d0 = dipole_field(n, L_NODE, r0_phys)
    Bc0 = math.sqrt(sum(fld_d0[k, n // 2, n // 2, n // 2] ** 2 for k in range(3)))
    fld_d = fld_d0 * (B_MAGNETAR / Bc0)
    A_I_dipole_magnetar = a_I_from_field(fld_d, L_NODE)

    # (c) resolvable-dipole O(h^2) convergence (dimensionless: source at r0=1, halve h)
    conv = [curl_over_field_center(dipole_field(n, hh, 1.0), hh)
            for hh in (0.1, 0.05, 0.025)]
    ratio = conv[0] / conv[1] if conv[1] > 0 else float("nan")
    ratio2 = conv[1] / conv[2] if conv[2] > 0 else float("nan")

    # (d) positive control: a field WITH circulation -> A_I > 0 (can-fire)
    fld_c = circulation_control_field(B_MAGNETAR, n, L_NODE, r_scale=100 * L_NODE)
    A_I_control = a_I_from_field(fld_c, L_NODE)

    # anti-tautology counterfactual: IF the mu-grade keyed on |B| magnitude
    A_mag_snap_sq = (B_MAGNETAR / B_SNAP) ** 2      # kernel-scale (constants.py: this IS the ratio scale)
    A_mag_dual_sq = (B_MAGNETAR / B_DUAL) ** 2      # field-amplitude duality scale
    A_mag_dual_1e7 = (1.0e7 / B_DUAL) ** 2          # task's stated 1e7 T cross-check

    return {
        "B_magnetar_T_EXTERNAL": B_MAGNETAR,
        "A_I_uniform_static": A_I_uniform,
        "S_B_uniform_static": S_B_uniform,
        "dn_mu_uniform_static": dn_mu_uniform,
        "A_I_dipole_magnetar_geometry": A_I_dipole_magnetar,
        "resolvable_dipole_curl_over_B": conv,
        "dipole_Oh2_ratio_h_to_h2": ratio,
        "dipole_Oh2_ratio_h2_to_h4": ratio2,
        "positive_control_A_I_circulation_field": A_I_control,
        "positive_control_fires": bool(A_I_control > 1e-3),
        "fork1_holds": bool((A_I_uniform < 1e-9) and (A_I_dipole_magnetar < 1e-9)
                            and (dn_mu_uniform > -1e-16)),
        "counterfactual_magnitude_keyed_A2_via_B_SNAP": A_mag_snap_sq,
        "counterfactual_magnitude_keyed_A2_via_B_dual": A_mag_dual_sq,
        "counterfactual_magnitude_keyed_super_yield": bool(A_mag_snap_sq > 1.0),
        "crosscheck_1e7T_A2_via_B_dual": A_mag_dual_1e7,
    }


def delta_n_from_A(A: float) -> float:
    """AVE par-perp birefringence at loaded coordinate amplitude A (E = A*E_YIELD)."""
    return float(delta_n_ave_differential_exact(A * E_YIELD))


# ============================================================================
# 2. ENVIRONMENT TABLE — apply the AVE keying to each (EXTERNAL values tagged)
# ============================================================================
@dataclass
class Env:
    tag: str
    name: str
    kind: str            # "static-B" | "static-E" | "radiation"
    external_value: str
    A2_active: float     # AVE-active (correctly-keyed) pump strength
    dn_ave: float        # AVE birefringence at A2_active
    note: str


def build_environment_table() -> list[Env]:
    envs: list[Env] = []

    # --- static magnetic (E1-E4): mu-grade keys on circulation => A_I = 0 (FORK-1) ---
    static_B = [
        ("E1", "magnetar surface B", 1.0e11, "1e10-1e11 T (1e14-1e15 G)"),
        ("E2", "ordinary pulsar B", 1.0e8, "1e8 T (1e12 G)"),
        ("E3", "galactic B", 1.0e-10, "~1e-10 T (uG)"),
        ("E4", "intergalactic B", 1.0e-13, "~1e-13 T (nG upper)"),
    ]
    for tag, name, B, ext in static_B:
        # AVE-active response of a STATIC B: A_I = 0 (FORK-1, computed in fork1 test).
        A2 = 0.0
        mag_cf = (B / B_SNAP) ** 2
        envs.append(Env(tag, name, "static-B", ext, A2, 0.0,
                        f"STATIC => A_I=0 => transparent (FORK-1). "
                        f"magnitude-keyed counterfactual (B/B_SNAP)^2={mag_cf:.2e} "
                        f"({'SUPER-YIELD' if mag_cf > 1 else 'sub-yield'}, excluded)."))

    # --- static / quasi-static electric (E5-E6): eps-grade charge-keyed on |E| ---
    # E5 polar-cap gap E: strongest static-E candidate; two rows (unscreened max, screened real)
    E_gap_unscreened = 1.0e15   # EXTERNAL: co-rotation E at a magnetar polar cap (unscreened)
    E_gap_screened = 1.0e10     # EXTERNAL: realistic pair-screened gap E (~ dV/h)
    envs.append(Env("E5a", "polar-cap gap E (unscreened max)", "static-E",
                    "~1e15 V/m (unscreened co-rotation)",
                    a_v_of_E(E_gap_unscreened) ** 2, delta_n_from_A(a_v_of_E(E_gap_unscreened)),
                    "loads eps LOCALLY, but pair-screened on cm-m scales + thin gap + short path "
                    "+ not on the clean observational path => negligible integrated observable."))
    envs.append(Env("E5b", "polar-cap gap E (screened real)", "static-E",
                    "~1e10 V/m (pair-screened)",
                    a_v_of_E(E_gap_screened) ** 2, delta_n_from_A(a_v_of_E(E_gap_screened)),
                    "realistic screened gap: negligible."))
    envs.append(Env("E6", "interstellar / intergalactic medium E", "static-E",
                    "~0 (quasi-neutral, Debye-screened)",
                    0.0, 0.0,
                    "bulk space is quasi-neutral plasma => macroscopic static E screened to ~0 "
                    "=> no eps pump on any long-baseline path."))

    # --- radiation (E7-E12): loads BOTH sectors; A_V = A_I = E_rms/E_YIELD ---
    # E7 magnetar thermal surface X-ray
    kT_keV = 0.5
    T_K = kT_keV * KEV_TO_K
    F_surface = SIGMA_SB * T_K**4
    E7 = e_rms_from_intensity(F_surface)
    envs.append(Env("E7", "magnetar thermal surface X-ray", "radiation",
                    f"kT~0.5 keV, F=sigma T^4~{F_surface:.1e} W/m^2",
                    a_v_of_E(E7) ** 2, delta_n_from_A(a_v_of_E(E7)),
                    "persistent surface emission; A^2 far below lab pump."))
    # E8 magnetar giant-flare peak at the surface (strongest transient radiation pump)
    L_flare, r_flare = 1.0e40, 1.0e4
    E8 = e_rms_from_intensity(intensity_from_luminosity(L_flare, r_flare))
    L_flare_mag, r_flare_mag = 1.0e40, 1.0e6
    E8m = e_rms_from_intensity(intensity_from_luminosity(L_flare_mag, r_flare_mag))
    envs.append(Env("E8", "magnetar giant-flare peak (surface)", "radiation",
                    "L~1e47 erg/s at R_NS~1e4 m (transient)",
                    a_v_of_E(E8) ** 2, delta_n_from_A(a_v_of_E(E8)),
                    f"NUMERICALLY-STRONGEST radiation pump (A^2~{a_v_of_E(E8)**2:.2e}); "
                    f"at magnetosphere r~1e6 m A^2~{a_v_of_E(E8m)**2:.2e}. BUT radial outflow "
                    "=> co-propagating probe sees collinear (projection-suppressed) pump; rare "
                    "transient; no polarimetric bound reaches it. Non-constraining."))
    # E9 accreting NS / ULX inner region
    L_ulx, r_ulx = 1.0e39, 1.0e6
    E9 = e_rms_from_intensity(intensity_from_luminosity(L_ulx, r_ulx))
    envs.append(Env("E9", "accreting NS / ULX inner region", "radiation",
                    "L~1e39 W at r~1e6 m",
                    a_v_of_E(E9) ** 2, delta_n_from_A(a_v_of_E(E9)),
                    "near-source; collinear + no clean birefringence bound."))
    # E10 GRB prompt emission
    L_grb, r_grb = 1.0e47, 1.0e11
    E10 = e_rms_from_intensity(intensity_from_luminosity(L_grb, r_grb))
    L_grb_n, r_grb_n = 1.0e47, 1.0e9
    E10n = e_rms_from_intensity(intensity_from_luminosity(L_grb_n, r_grb_n))
    envs.append(Env("E10", "GRB prompt emission", "radiation",
                    "L_iso~1e54 erg/s at r~1e11 m (emission radius)",
                    a_v_of_E(E10) ** 2, delta_n_from_A(a_v_of_E(E10)),
                    f"at emission radius A^2~{a_v_of_E(E10)**2:.2e} (below lab); near-zone r~1e9 m "
                    f"A^2~{a_v_of_E(E10n)**2:.2e}. Radial outflow => collinear w/ escaping photons; "
                    "GRB polarization bounds do not reach the birefringence."))
    # E11 CMB
    u_cmb = A_RAD * (2.725) ** 4
    E11 = e_rms_from_energy_density(u_cmb)
    envs.append(Env("E11", "CMB radiation bath", "radiation",
                    f"T=2.725 K, u~{u_cmb:.1e} J/m^3",
                    a_v_of_E(E11) ** 2, delta_n_from_A(a_v_of_E(E11)),
                    "the cosmological photon bath; A^2 utterly negligible."))
    # E12 ISRF
    u_isrf = 1.0e-13
    E12 = e_rms_from_energy_density(u_isrf)
    envs.append(Env("E12", "interstellar radiation field", "radiation",
                    "u~1e-13 J/m^3",
                    a_v_of_E(E12) ** 2, delta_n_from_A(a_v_of_E(E12)),
                    "starlight bath; negligible."))
    return envs


# ============================================================================
# 3. IXPE COMPARISON — AVE (static-B transparent) vs QED baseline vs observation
# ============================================================================
def ixpe_comparison() -> dict:
    """A static magnetar B: QED predicts dn_QED = 3 A_e B^2 (IXPE consistent with this);
    AVE (FORK-1) adds dn_mu = 0. So AVE does NOT overshoot IXPE — and crucially does NOT
    predict the catastrophic 1e6x-QED enhancement (which would require the nonlinearity to
    fire on static B, which it does not)."""
    B = 1.0e11  # EXTERNAL magnetar surface
    dn_qed = float(delta_n_qed_magnetic(B))
    dn_ave_static = 0.0  # FORK-1
    # what AVE WOULD predict if its 1e6x coefficient fired on static B (magnitude-keyed):
    dn_ave_if_magnitude_keyed = delta_n_from_A(B / B_DUAL)  # NaN if super-yield (A>1)
    return {
        "B_T_EXTERNAL": B,
        "dn_QED_magnetic_static": dn_qed,
        "dn_AVE_static_FORK1": dn_ave_static,
        "dn_AVE_if_magnitude_keyed": dn_ave_if_magnitude_keyed,
        "AVE_overshoots_IXPE": False,
        "note": "AVE adds 0 to the static-B magnetar birefringence (FORK-1); the residual "
                "birefringence IXPE sees is the ordinary QED Euler-Heisenberg value. "
                "Magnitude-keying would give A>1 (past yield) => vacuum rupture, excluded.",
    }


# ============================================================================
# 4. STRONGEST PUMP + CMB COINCIDENCE + VERDICT
# ============================================================================
def resolve(envs: list[Env], fork1: dict) -> dict:
    # strongest AVE-active pump on any path (report separately: clean-path vs near-source)
    clean_path_tags = {"E3", "E4", "E6", "E7", "E10", "E11", "E12"}  # long-baseline / persistent
    near_source_tags = {"E1", "E2", "E5a", "E5b", "E8", "E9"}         # localized / transient
    by_A2 = sorted(envs, key=lambda e: e.A2_active, reverse=True)
    strongest = by_A2[0]
    strongest_clean = max((e for e in envs if e.tag in clean_path_tags),
                          key=lambda e: e.A2_active)

    # CMB coincidence: intergalactic path pumps? (E4 static-B, E6 IGM-E, E11 CMB-rad)
    cmb_path = {e.tag: e.A2_active for e in envs if e.tag in ("E4", "E6", "E11")}
    cmb_path_pumps = any(v >= A_LAB_SQ for v in cmb_path.values())
    ave_sidereal = 4.937e-3   # = 4 beta, P6 result (radiation-Doppler order of CMB boost)
    cmb_biref = 5.2e-3        # EXTERNAL: detected isotropic cosmic birefringence ~0.3 deg [rad]
    cmb_verdict = "REAL" if cmb_path_pumps else "SPURIOUS"

    # VERDICT routing (frozen bins)
    fork1_holds = fork1["fork1_holds"]
    # clean-path radiation all below lab?
    clean_rad_below_lab = all(
        e.A2_active < A_LAB_SQ for e in envs
        if e.kind == "radiation" and e.tag in clean_path_tags
    )
    # near-source radiation above lab but collinear/unconstrained (E8/E9/E10-near) -> allowed
    if not fork1_holds:
        verdict = "FORK-1-BREAK"
    elif clean_rad_below_lab and not cmb_path_pumps:
        verdict = "PUMP-SAFE"
    else:
        verdict = "PUMP-CONSTRAINED"

    return {
        "strongest_pump_any_path": {"tag": strongest.tag, "name": strongest.name,
                                    "A2": strongest.A2_active, "kind": strongest.kind},
        "strongest_pump_clean_path": {"tag": strongest_clean.tag, "name": strongest_clean.name,
                                      "A2": strongest_clean.A2_active},
        "A_lab_sq": A_LAB_SQ,
        "cmb_path_A2": cmb_path,
        "cmb_path_pumps": bool(cmb_path_pumps),
        "ave_sidereal_4beta": ave_sidereal,
        "cmb_birefringence_EXTERNAL": cmb_biref,
        "cmb_coincidence": cmb_verdict,
        "clean_path_radiation_all_below_lab": bool(clean_rad_below_lab),
        "fork1_holds": bool(fork1_holds),
        "VERDICT": verdict,
    }


def main() -> dict:
    checks = canonical_self_check()
    fork1 = fork1_static_B_test()
    envs = build_environment_table()
    ixpe = ixpe_comparison()
    verdict = resolve(envs, fork1)

    out = {
        "canonical_self_check": checks,
        "constants": {
            "E_YIELD": E_YIELD, "B_SNAP": B_SNAP, "B_dual": B_DUAL,
            "I_max": I_MAX, "E_CRIT": E_CRIT, "L_NODE": L_NODE, "ALPHA": ALPHA,
            "A_e_Tm2": vacuum_magnetic_birefringence_constant(), "A_lab_sq": A_LAB_SQ,
        },
        "fork1_static_B": fork1,
        "environment_table": [asdict(e) for e in envs],
        "ixpe_comparison": ixpe,
        "resolution": verdict,
    }

    # ---- print human-readable summary ----
    print("=" * 78)
    print("PUMP INVENTORY — astrophysical pump audit of AVE nonlinear birefringence")
    print("=" * 78)
    print(f"canonical self-check: {checks}")
    print("\n-- FORK-1 static-B transparency at magnetar B = 1e11 T --")
    print(f"  A_I (uniform static B)       = {fork1['A_I_uniform_static']:.3e}")
    print(f"  S_B (uniform static B)       = {fork1['S_B_uniform_static']:.12f}")
    print(f"  dn_mu (uniform static B)     = {fork1['dn_mu_uniform_static']:.3e}")
    print(f"  A_I (dipole, magnetar geom)  = {fork1['A_I_dipole_magnetar_geometry']:.3e}")
    print(f"  resolvable-dipole |curlB|/B  = {['%.3e' % x for x in fork1['resolvable_dipole_curl_over_B']]}")
    print(f"  O(h^2) ratios (~4 each)      = {fork1['dipole_Oh2_ratio_h_to_h2']:.2f}, "
          f"{fork1['dipole_Oh2_ratio_h2_to_h4']:.2f}")
    print(f"  POS CONTROL A_I (circulation)= {fork1['positive_control_A_I_circulation_field']:.3e} "
          f"(fires={fork1['positive_control_fires']})")
    print(f"  FORK-1 HOLDS                 = {fork1['fork1_holds']}")
    print(f"  magnitude-keyed cf (B/B_SNAP)^2 = {fork1['counterfactual_magnitude_keyed_A2_via_B_SNAP']:.2e} "
          f"(SUPER-YIELD={fork1['counterfactual_magnitude_keyed_super_yield']})")
    print(f"  crosscheck (1e7 T / B_dual)^2   = {fork1['crosscheck_1e7T_A2_via_B_dual']:.2e}  (task's ~7e-4)")

    print("\n-- ENVIRONMENT TABLE --")
    print(f"{'tag':4} {'environment':38} {'kind':10} {'A2_active':>11} {'dn_ave':>11}")
    for e in envs:
        print(f"{e.tag:4} {e.name[:38]:38} {e.kind:10} {e.A2_active:11.3e} {e.dn_ave:11.3e}")

    print("\n-- IXPE (static-B magnetar) --")
    print(f"  dn_QED (magnetic, 1e11 T) = {ixpe['dn_QED_magnetic_static']:.3e}")
    print(f"  dn_AVE (static, FORK-1)   = {ixpe['dn_AVE_static_FORK1']:.3e}  (adds nothing)")
    print(f"  dn_AVE if magnitude-keyed = {ixpe['dn_AVE_if_magnitude_keyed']}  (NaN=past yield)")

    print("\n-- RESOLUTION --")
    print(f"  strongest pump (any path)   : {verdict['strongest_pump_any_path']}")
    print(f"  strongest pump (clean path) : {verdict['strongest_pump_clean_path']}")
    print(f"  CMB path A2                 : {verdict['cmb_path_A2']}  pumps={verdict['cmb_path_pumps']}")
    print(f"  AVE sidereal 4beta={verdict['ave_sidereal_4beta']:.3e} vs CMB biref "
          f"{verdict['cmb_birefringence_EXTERNAL']:.3e} => {verdict['cmb_coincidence']}")
    print(f"\n  >>> VERDICT: [{verdict['VERDICT']}] <<<")

    return out


if __name__ == "__main__":
    result = main()
    outdir = os.path.join(os.path.dirname(__file__), "_output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "pump_inventory_astrophysical.json"), "w") as f:
        json.dump(result, f, indent=2, default=str)
    print(f"\n[json] {os.path.join(outdir, 'pump_inventory_astrophysical.json')}")
