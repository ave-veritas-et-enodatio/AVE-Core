"""
ft1_delta_strain_eta_epsilon_driver.py
=======================================

FT-1 (Q-DELTA-MAP-1-quant) — forward-derive eta_epsilon from substrate
E-mode dispersion + substrate-Bose-Einstein occupation at T_CMB, with NO
back-substitution from CODATA.

Prereg: research/2026-05-31_FT-1_delta-strain-eta-epsilon_prereg.md
Target (NOT an input): eta_eps ~ 4.45e-6 ; delta_strain ~ eta_eps/2 ~ 2.225e-6.

The 4-step chain (Q-DELTA-MAP-1-quant):
  (i)   E-mode dispersion omega_E(k) = c_E |k| at T_CMB from (l_node, G_vac).
  (ii)  BUILD substrate-Bose-Einstein occupation <A_E^2> over the gapless
        E-spectrum at k_B T_CMB.
  (iii) BUILD E-mode -> eps_eff microscopic coupling (Ax-1 primitives) -> eta_eps.
  (iv)  Compare to 4.45e-6 (DERIVE INDEPENDENTLY; do not tune).

HARD GUARDS (per prereg sec.6):
  - c_EM (=c_0/sqrt(S)), NOT c_shear. The alpha-modulation OUTPUT form is
    reused, not rebuilt; this driver only supplies eta_eps as its input.
  - Anti-tuning: the target 4.45e-6 is the back-substituted value. It is NOT
    used anywhere in the forward chain. It enters only at the final compare.
  - Canonical primitives from src/ave/core/constants.py; no round numbers.

This driver computes the substrate thermal-mode amplitude <A_E^2> three ways
(classical equipartition FOIL, Bose-Einstein Debye integral, and the per-cell
strain-fraction the eps-coupling needs) so the OOM gap vs 4.45e-6 is explicit
and the amplification diagnostic is dispositive.
"""

import json
from pathlib import Path

import numpy as np

from ave.core import constants as C

# -----------------------------------------------------------------------------
# Cosmic operating temperature (defining the epoch; NOT a free parameter, and
# NOT the back-substituted alpha residual). T_CMB is the measured CMB monopole.
# -----------------------------------------------------------------------------
T_CMB: float = 2.725  # K

# Anti-tuning firewall: the target is recorded for the FINAL compare ONLY.
# It is never read by any forward-chain function below.
ETA_EPS_TARGET: float = 2.0 * C.DELTA_STRAIN  # ~4.45e-6 (back-substituted; compare-only)


def step_i_dispersion() -> dict:
    """(i) E-mode dispersion omega_E(k) = c_E |k| from substrate primitives.

    The substrate transverse wave speed is c_0: photons propagate at c on the
    LC lattice because v_transverse = sqrt(G_vac / rho_bulk) = c_0 (canonical
    constants.py: G_VAC = RHO_BULK * C_0**2). So the gapless E-mode (acoustic,
    long-wavelength) phase/group speed is c_E = c_0. No CODATA-alpha enters:
    G_vac and rho_bulk are both built from (l_node, m_e, c) topological inputs.

    Brillouin-zone edge: k_max = pi / l_node (one lattice pitch). Debye-like
    cutoff frequency omega_D = c_E * k_max, energy hbar*omega_D ~ pi * m_e c^2.
    """
    c_E = float(np.sqrt(C.G_VAC / C.RHO_BULK))  # = c_0 by construction

    # Debye cutoff fixed self-consistently by the mode count: 3 E-branches,
    # one node per l_node^3 -> 3 modes per cell. The Debye sphere radius is
    #   k_D = (6 pi^2 n)^(1/3),  n = number density of NODES = 1 / l_node^3,
    # so that int_0^{omega_D} 3*(omega^2/(2 pi^2 c^3)) d(omega) = 3 n = 3/l_node^3.
    # (Using k_max = pi/l_node directly would be the simple-cubic BZ-edge, which
    #  over-counts the Debye sphere by (6 pi^2)/pi^3 -> the n_dof check exposes it;
    #  the Debye closure is the physically correct one for a DOS integral.)
    n_node = 1.0 / C.L_NODE**3
    k_D = (6.0 * np.pi**2 * n_node) ** (1.0 / 3.0)
    omega_D = c_E * k_D
    hbar_omega_D = C.HBAR * omega_D
    return {
        "c_E_mps": c_E,
        "c_E_over_c0": c_E / C.C_0,
        "k_D_per_m": float(k_D),
        "k_D_over_pi_per_l": float(k_D / (np.pi / C.L_NODE)),
        "omega_D_rad_s": float(omega_D),
        "hbar_omega_D_J": float(hbar_omega_D),
        "hbar_omega_D_over_mec2": float(hbar_omega_D / (C.M_E * C.C_0**2)),
        "Theta_Debye_K": float(hbar_omega_D / C.K_B),
    }


def step_ii_occupation(disp: dict, n_k: int = 2_000_000) -> dict:
    """(ii) Substrate-Bose-Einstein occupation of the gapless E-spectrum.

    Three thermal energy densities, all over the SAME Debye E-mode spectrum
    (3 acoustic E-branches, gapless, linear omega = c_E |k|, BZ edge k_max):

      u_classical : classical equipartition FOIL (the leaf at
                    mode-counting-heat-capacity.md): every mode carries k_B T
                    (k_B T per mode = (1/2 k_B T) x 2 quadratures). This is the
                    Dulong-Petit / Rayleigh-Jeans high-T limit. THE FOIL TO BEAT.

      u_BE        : Bose-Einstein occupation, u = integral g(omega) hbar*omega
                    n_BE(omega) d(omega), n_BE = 1/(exp(hbar*omega/kT) - 1).
                    This is the substrate-Bose-Einstein build. At T << Theta_D
                    it is the Debye-T^4 (radiation-like) law.

      u_BE_zpe    : BE + zero-point (hbar*omega/2 per mode). ZPE is T-independent
                    -> cannot contribute to a THERMAL modulation eta_eps(T); shown
                    for completeness, excluded from the thermal coupling.

    The MEAN-SQUARE E-mode amplitude that the eps-coupling sees is built from
    the THERMAL energy density only (the part that vanishes as T -> 0): a
    dimensionless strain-fraction (thermal energy density) / (substrate
    rest-energy density m_e c^2 / l_node^3). No CODATA-alpha enters.

    Debye DOS for 3 acoustic branches in 3D:
        g(omega) d(omega) = 3 * (omega^2 / (2 pi^2 c_E^3)) d(omega),  omega in [0, omega_D]
    with the Debye cutoff fixed by mode-count = 3 / l_node^3 (3 E-DOF per node,
    1 node per l_node^3):  integral_0^{omega_D} g d(omega) = 3 / l_node^3.
    """
    c_E = disp["c_E_mps"]
    omega_D = disp["omega_D_rad_s"]
    kT = C.K_B * T_CMB

    # Verify Debye cutoff reproduces 3 E-DOF per cell (consistency check, not a fit).
    n_modes_per_vol = 3.0 * omega_D**3 / (6.0 * np.pi**2 * c_E**3)  # = omega_D^3/(2pi^2 c^3)
    n_dof_per_cell = n_modes_per_vol * C.L_NODE**3

    # Numerical integration over the spectrum. Populated band is omega << omega_D
    # (x_D ~ 1e10), so use a log-spaced grid concentrated near the thermal scale
    # plus a linear tail to the cutoff. Integrate u = int g(w) hbar w * occ(w) dw.
    w_lo = 1e-6 * (kT / C.HBAR)
    w_grid = np.concatenate([
        np.logspace(np.log10(w_lo), np.log10(omega_D), n_k),
    ])
    x = C.HBAR * w_grid / kT
    g = 3.0 * w_grid**2 / (2.0 * np.pi**2 * c_E**3)  # 3-branch Debye DOS

    # Occupation factors
    # n_BE = 1/(exp(x)-1); guard overflow for large x (exp -> inf => n_BE -> 0).
    with np.errstate(over="ignore", divide="ignore", invalid="ignore"):
        n_BE = np.where(x < 700.0, 1.0 / np.expm1(np.clip(x, 1e-300, 700.0)), 0.0)
    occ_classical = np.full_like(w_grid, 1.0)  # <n> -> kT/(hbar w): energy = kT per mode

    hw = C.HBAR * w_grid
    # Thermal energy densities (J/m^3)
    u_BE = float(np.trapezoid(g * hw * n_BE, w_grid))
    # classical: energy per mode = k_B T  => integrand g * kT
    u_classical = float(np.trapezoid(g * kT, w_grid))
    u_zpe = float(np.trapezoid(g * 0.5 * hw, w_grid))  # T-independent (reference only)

    # Substrate rest-energy density: m_e c^2 per cell volume l_node^3.
    u_rest = (C.M_E * C.C_0**2) / C.L_NODE**3

    # Closed-form Debye-T^4 cross-check (the standard low-T phonon result):
    #   u_BE(T<<Theta_D) = 3 * (pi^2/30) * (kT)^4 / (hbar c_E)^3
    u_BE_closed = 3.0 * (np.pi**2 / 30.0) * kT**4 / (C.HBAR * c_E) ** 3

    return {
        "kT_J": float(kT),
        "x_D": float(C.HBAR * omega_D / kT),
        "n_dof_per_cell_check": float(n_dof_per_cell),  # expect ~3.0
        "u_classical_J_per_m3": u_classical,
        "u_BE_J_per_m3": u_BE,
        "u_BE_closed_T4_J_per_m3": float(u_BE_closed),
        "u_zpe_J_per_m3": u_zpe,
        "u_rest_J_per_m3": float(u_rest),
        # dimensionless strain-fractions (thermal energy / rest energy density)
        "frac_classical": u_classical / float(u_rest),
        "frac_BE": u_BE / float(u_rest),
        "BE_over_classical": u_BE / u_classical,
    }


def step_iii_eps_coupling(occ: dict) -> dict:
    """(iii) E-mode -> eps_eff microscopic coupling (Ax-1 + Ax-4 primitives).

    The substrate dielectric stiffness is set by the per-node LC tank at its
    operating point A along the Axiom-4 saturation kernel S(A)=sqrt(1-(A/A_yield)^2).
    Small-signal: eps_eff = eps_0 * S(A) ~ eps_0 (1 - (1/2)(A/A_yield)^2). So a
    thermal E-mode amplitude A_th drives a fractional dielectric softening

        eta_eps = 1 - eps_eff/eps_0 ~ (1/2) <(A_th/A_yield)^2>.

    The mean-square thermal strain (A_th/A_yield)^2 is the thermal energy stored
    in the E-modes divided by the yield-energy scale of the node tank. Two honest
    normalizations bracket the coupling (no CODATA-alpha in either):

      (a) rest-energy normalization: yield energy ~ m_e c^2 per cell
          -> eta_eps = (1/2) * frac_thermal,  frac_thermal = u_thermal / u_rest.

      (b) kinetic-yield normalization: the Axiom-4 dielectric yield is the
          KINETIC yield E_yield = sqrt(alpha_cold) m_e c^2 (V_yield = sqrt(alpha) V_snap;
          E_YIELD_KINETIC in constants.py). Using alpha_cold (NOT CODATA-alpha,
          NOT delta_strain) keeps the chain forward. The per-cell yield energy
          density is then E_yield / l_node^3, giving
          eta_eps = (1/2) * u_thermal / (E_yield/l_node^3).

    Both are reported for BE-occupation AND for the classical-equipartition foil.
    The factor-of-2 and the alpha_cold^(1/2) ~ 0.085 prefactors are O(1)-O(0.1):
    they cannot bridge a 28-30 OOM gap, so the OUTCOME is set by step (ii), not (iii).
    """
    u_rest = occ["u_rest_J_per_m3"]
    # kinetic-yield energy density (Ax-4 dielectric saturation scale, cold-lattice)
    u_yield_kin = C.E_YIELD_KINETIC / C.L_NODE**3  # = sqrt(alpha_cold) * u_rest (alpha_cold input)

    out = {}
    for label, u_th in (("BE", occ["u_BE_J_per_m3"]), ("classical", occ["u_classical_J_per_m3"])):
        # (a) rest-energy normalization
        eta_a = 0.5 * u_th / u_rest
        # (b) kinetic-yield normalization
        eta_b = 0.5 * u_th / u_yield_kin
        out[f"eta_eps_{label}_restnorm"] = float(eta_a)
        out[f"eta_eps_{label}_yieldnorm"] = float(eta_b)
    out["u_yield_kin_J_per_m3"] = float(u_yield_kin)
    out["sqrt_alpha_cold"] = float(np.sqrt(C.ALPHA_COLD))
    return out


def step_iv_compare_and_adjudicate(occ: dict, coup: dict) -> dict:
    """(iv) Compare the INDEPENDENTLY-derived eta_eps to the target; adjudicate A/B/C.

    The forward prediction is the Bose-Einstein result (the substrate-physics
    chain the prereg specifies). The classical-equipartition value is the FOIL.
    The target 4.45e-6 enters HERE ONLY (anti-tuning firewall).
    """
    target = ETA_EPS_TARGET
    # Forward prediction = BE-occupation, both normalizations bracket it.
    eta_BE_lo = min(coup["eta_eps_BE_restnorm"], coup["eta_eps_BE_yieldnorm"])
    eta_BE_hi = max(coup["eta_eps_BE_restnorm"], coup["eta_eps_BE_yieldnorm"])
    eta_cl_lo = min(coup["eta_eps_classical_restnorm"], coup["eta_eps_classical_yieldnorm"])
    eta_cl_hi = max(coup["eta_eps_classical_restnorm"], coup["eta_eps_classical_yieldnorm"])

    def oom_gap(eta):
        return float(np.log10(target / eta)) if eta > 0 else float("inf")

    oom_BE_hi = oom_gap(eta_BE_hi)  # smallest gap on the BE side
    oom_cl_hi = oom_gap(eta_cl_hi)  # smallest gap on the classical side

    # Outcome logic per prereg sec.5:
    #   A: |oom| <= 1 on the forward (BE) chain
    #   B: right sign/mechanism, bounded factor off (1 < |oom| <= ~2)
    #   C: inherits the 3-20 OOM undershoot
    if abs(oom_BE_hi) <= 1.0:
        outcome = "A"
    elif abs(oom_BE_hi) <= 2.0:
        outcome = "B"
    else:
        outcome = "C"

    return {
        "eta_eps_target": float(target),
        "eta_eps_BE_forward_range_lo": float(eta_BE_lo),
        "eta_eps_BE_forward_range_hi": float(eta_BE_hi),
        "eta_eps_classical_foil_lo": float(eta_cl_lo),
        "eta_eps_classical_foil_hi": float(eta_cl_hi),
        "OOM_gap_BE_best": oom_BE_hi,
        "OOM_gap_classical_best": oom_cl_hi,
        "BE_below_classical_by_OOM": float(np.log10(eta_cl_hi / eta_BE_hi)),
        "OUTCOME": outcome,
    }


if __name__ == "__main__":
    print("=" * 72)
    print("FT-1 (Q-DELTA-MAP-1-quant) — eta_epsilon forward derivation")
    print("=" * 72)
    di = step_i_dispersion()
    print("\n(i) E-mode dispersion:")
    for k, v in di.items():
        print(f"    {k:28s} = {v:.6e}" if isinstance(v, float) else f"    {k:28s} = {v}")

    dii = step_ii_occupation(di)
    print("\n(ii) Thermal occupation (Debye E-spectrum):")
    for k, v in dii.items():
        print(f"    {k:28s} = {v:.6e}" if isinstance(v, float) else f"    {k:28s} = {v}")

    diii = step_iii_eps_coupling(dii)
    print("\n(iii) E-mode -> eps_eff coupling (Ax-1/Ax-4):")
    for k, v in diii.items():
        print(f"    {k:28s} = {v:.6e}" if isinstance(v, float) else f"    {k:28s} = {v}")

    div = step_iv_compare_and_adjudicate(dii, diii)
    print("\n(iv) Compare to target + adjudicate:")
    for k, v in div.items():
        print(f"    {k:28s} = {v:.6e}" if isinstance(v, float) else f"    {k:28s} = {v}")

    # Persist full result for the result-doc.
    repo_root = Path(__file__).resolve().parent.parent.parent.parent
    out_dir = repo_root / "results"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_json = out_dir / "ft1_delta_strain_eta_epsilon.json"
    payload = {
        "T_CMB_K": T_CMB,
        "eta_eps_target_compare_only": ETA_EPS_TARGET,
        "step_i_dispersion": di,
        "step_ii_occupation": dii,
        "step_iii_eps_coupling": diii,
        "step_iv_adjudication": div,
    }
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, default=str)
    print(f"\n  Output: {out_json}")
