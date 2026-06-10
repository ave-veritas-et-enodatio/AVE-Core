#!/usr/bin/env python3
"""
Z_rad,L = R_rad,L + jX_L — dark-wake longitudinal-shear radiation impedance.

Replaces the HEURISTIC dark-wake observer (vacuum_engine.py:1457,
tau_zx = z_local * d(A^2)/dx, prefactor = empirical rho_Op14 = 0.990) with a
REAL Cosserat elastodynamic-flux + reactive-energy extraction:

  - Re{Z_rad,L} = R_rad,L : time-averaged REAL energy flux of the shear wave
        through a PML-excluded far-field surface.  Cosserat acoustic intensity
        (the elastodynamic Poynting vector):
            I_k = -( sigma_kj * u_dot_j  +  m_kj * omega_dot_j )
        with the constitutive stresses from the engine's own Cosserat energy
        density (cosserat_field_3d.py:588 _energy_density_bare, linear part):
            W = G[ (2/3)(tr eps)^2 + |eps_sym|^2 ] + G_c|eps_antisym|^2 + gamma|kappa|^2
            sigma_ij = (4/3)G tr(eps) d_ij + 2G eps_sym,ij + 2 G_c eps_antisym,ij
            m_ij     = 2 gamma kappa_ij
  - Im{Z_rad,L} = X_L : near-field reactive stored elastic energy (Sigma_near).
  - Radiation Q = omega_drive * <U_stored_near> / P_rad  (normalization-INDEPENDENT
        resonator Q; adjudicates the radiated-vs-reactive fork, brief sec 0.5).

Drives a chiral CosseratBeltramiSource (kappa_chiral = 1.2 alpha, (2,3) winding) in
both handednesses to exercise the parity selection rule (03_neutrino_sector.tex:66:
RH torsional waves evanescent below k_crit = gamma_c/c^2; LH propagate at all k).

HONEST SCOPE (ave-driver-script-honesty): this is a flagged-OPEN load-bearing
analytical gap.  This driver demonstrates the real-flux machinery RUNS and yields
the robust, normalization-independent observables (sign of net flux, RH-vs-LH chiral
asymmetry, radiation Q order-of-magnitude).  Absolute R/X normalization (the source
"current" I_ref) and the index/sign convention of the flux tensor are NOT yet
validated; first-pass smoke numbers only.  See
research/2026-06-08_rrad-l-darkwake_result.md for the DERIVED/VERIFIED/BLOCKED split.

Prereg: research/2026-06-08_rrad-l-darkwake_prereg.md
Brief : AVE-Propulsion-ionpump/research/2026-06-08_NEXT-STEP_Rrad-L_core-brief.md
"""

import argparse
import json

import numpy as np

# Canonical-source imports (ave-canonical-source: never hard-code constants):
from ave.core.constants import ALPHA, C_0, M_E, N_NU, Z_0
import ave.core.constants as _avc

PI = np.pi

from ave.topological.cosserat_field_3d import _compute_curvature, _compute_strain
from ave.topological.vacuum_engine import (
    CosseratBeltramiSource,
    EngineConfig,
    VacuumEngine3D,
)

# ------------------------------------------------------------------ canonical-source verify
def verify_constants() -> None:
    """ave-canonical-source Step 4 cross-check — fail loudly on drift."""
    assert _avc.__file__.endswith("ave/core/constants.py"), \
        "ave.core.constants is not the AVE-Core canonical source"
    assert abs(N_NU - 2.0 / 7.0) < 1e-12, f"N_NU (Poisson ratio) drifted: {N_NU}"
    assert abs(Z_0 - np.sqrt(_avc.MU_0 / _avc.EPSILON_0)) < 1e-6, "Z_0 drift"
    assert abs(ALPHA - 7.2973525693e-3) < 1e-12, "ALPHA drift from CODATA"
    # Transverse template R_perp = Z_0/(4 pi) (theorem-3-1-q-factor.md:75).
    nu_sq = N_NU ** 2  # 4/49, the B-order candidate
    assert abs(nu_sq - 4.0 / 49.0) < 1e-12
    print(f"[verify_constants] OK  Z_0={Z_0:.4f} ohm  nu_vac={N_NU:.6f}  "
          f"nu_vac^2={nu_sq:.6f}  alpha={ALPHA:.6e}")


# ------------------------------------------------------------------ real elastodynamic flux
def cosserat_energy_flux(cos) -> np.ndarray:
    """REAL Cosserat acoustic-intensity vector I_k at every site, shape (N,N,N,3).

    I_k = -( sigma_kj u_dot_j + m_kj omega_dot_j ).  Constitutive stresses from the
    engine's own linear Cosserat energy density (the quadratic elastic part that
    carries the propagating shear wave; op10/refl/hopf self-terms are the nonlinear
    topology-stabilizers, not the radiating-wave flux).
    """
    G, G_c, gamma, dx = cos.G, cos.G_c, cos.gamma, cos.dx
    eps = np.asarray(_compute_strain(cos.u, cos.omega, dx))      # eps[...,i,j] = d_j u_i - e_ijk w_k
    kappa = np.asarray(_compute_curvature(cos.omega, dx))        # kappa[...,i,j] = d_j w_i

    eps_T = np.swapaxes(eps, -1, -2)
    eps_sym = 0.5 * (eps + eps_T)
    eps_antisym = 0.5 * (eps - eps_T)
    tr_eps = eps[..., 0, 0] + eps[..., 1, 1] + eps[..., 2, 2]
    I3 = np.eye(3)
    sigma = ((4.0 / 3.0) * G * tr_eps[..., None, None] * I3
             + 2.0 * G * eps_sym
             + 2.0 * G_c * eps_antisym)                          # sigma[...,i,j]
    m = 2.0 * gamma * kappa                                      # m[...,i,j]

    flux = -(np.einsum("...ij,...j->...i", sigma, cos.u_dot)
             + np.einsum("...ij,...j->...i", m, cos.omega_dot))  # (N,N,N,3)
    return flux


def elastic_energy_density(cos) -> np.ndarray:
    """Linear elastic strain-energy density (for the near-field reactive store)."""
    G, G_c, gamma, dx = cos.G, cos.G_c, cos.gamma, cos.dx
    eps = np.asarray(_compute_strain(cos.u, cos.omega, dx))
    kappa = np.asarray(_compute_curvature(cos.omega, dx))
    eps_T = np.swapaxes(eps, -1, -2)
    eps_sym = 0.5 * (eps + eps_T)
    eps_antisym = 0.5 * (eps - eps_T)
    tr_eps = eps[..., 0, 0] + eps[..., 1, 1] + eps[..., 2, 2]
    W = (G * ((2.0 / 3.0) * tr_eps ** 2 + np.sum(eps_sym ** 2, axis=(-1, -2)))
         + G_c * np.sum(eps_antisym ** 2, axis=(-1, -2))
         + gamma * np.sum(kappa ** 2, axis=(-1, -2)))
    # kinetic part
    T = 0.5 * cos.rho * np.sum(cos.u_dot ** 2, axis=-1) + \
        0.5 * cos.I_omega * np.sum(cos.omega_dot ** 2, axis=-1)
    return W + T


# ------------------------------------------------------------------ one chiral run
def run_handedness(handedness: str, N: int, pml: int, omega_drive: float,
                   amp: float, n_steps: int, record_frac: float) -> dict:
    cfg = EngineConfig(
        N=N, pml=pml, temperature=0.0,
        use_asymmetric_saturation=True,     # chiral (S_mu != S_eps) path
        disable_cosserat_lc_force=True,     # A28-corrected: bounded |omega| under drive
        enable_cosserat_self_terms=True,    # restore topology-stabilizing self-terms
    )
    engine = VacuumEngine3D(cfg)
    prop_axis = 0
    engine.add_source(CosseratBeltramiSource(
        x0=pml + 2, propagation_axis=prop_axis, amplitude=amp,
        omega=omega_drive, handedness=handedness, sigma_yz=max(2.0, N / 8.0),
        t_ramp=15.0, t_sustain=float(n_steps), t_decay=0.0,
    ))

    cos = engine.cos
    Nn = N
    interior = slice(pml, Nn - pml)
    # near-field shell: within ~6 cells downstream of source; far surface: a plane
    src_x = pml + 2
    near_lo, near_hi = src_x + 1, min(src_x + 7, Nn - pml - 1)
    far_x = Nn - pml - 2                  # far-field measurement plane (PML-excluded)

    record_start = int(n_steps * (1.0 - record_frac))
    flux_far_series, u_near_series = [], []
    for step in range(n_steps):
        engine.step()
        if step >= record_start and (step % 2 == 0):
            flux = cosserat_energy_flux(cos)
            alive = cos.mask_alive
            # far-field plane: average |flux_x| over the transverse plane at far_x,
            # net (signed) flux_x = the radiated component along the back axis
            plane = (slice(far_x, far_x + 1), interior, interior)
            fx = flux[..., prop_axis]
            far_signed = float(np.sum((fx * alive)[plane]))
            flux_far_series.append(far_signed)
            # near-field reactive store
            U = elastic_energy_density(cos)
            near_slab = (slice(near_lo, near_hi), interior, interior)
            u_near_series.append(float(np.sum((U * alive)[near_slab])))

    flux_far_series = np.array(flux_far_series)
    u_near_series = np.array(u_near_series)

    # P_rad = time-averaged REAL far-field flux (signed, along back axis).
    P_rad = float(np.mean(flux_far_series))
    P_rad_abs = float(np.mean(np.abs(flux_far_series)))
    U_near_mean = float(np.mean(u_near_series))
    U_near_osc = float(np.std(u_near_series))  # reactive (oscillating) store amplitude

    # radiation Q (normalization-independent): omega * <U_stored> / P_rad
    Q_rad = float(omega_drive * U_near_mean / abs(P_rad)) if abs(P_rad) > 1e-30 else float("inf")

    return {
        "handedness": handedness,
        "P_rad_signed": P_rad,
        "P_rad_abs": P_rad_abs,
        "U_near_mean": U_near_mean,
        "U_near_osc": U_near_osc,
        "Q_rad": Q_rad,
        "n_record": int(len(flux_far_series)),
        "omega_max": float(np.abs(cos.omega).max()),  # stability check
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=24)
    ap.add_argument("--pml", type=int, default=4)
    ap.add_argument("--steps", type=int, default=140)
    ap.add_argument("--lam", type=float, default=4.0, help="drive wavelength (cells)")
    ap.add_argument("--amp", type=float, default=0.25)
    ap.add_argument("--record-frac", type=float, default=0.4)
    ap.add_argument("--json", type=str, default="")
    args = ap.parse_args()

    verify_constants()
    omega_drive = 2.0 * PI / args.lam

    print(f"\n=== Z_rad,L driver (SMOKE; N={args.N} pml={args.pml} steps={args.steps} "
          f"lam={args.lam} amp={args.amp}) ===")
    print(f"transverse template R_perp = Z_0/(4pi) = {Z_0/(4*PI):.4f} ohm  "
          f"(theorem-3-1-q-factor.md:75)")
    print(f"crux candidates: nu_vac={N_NU:.4f}  nu_vac^2={N_NU**2:.4f}\n")

    results = {}
    for hand in ("LH", "RH"):
        r = run_handedness(hand, args.N, args.pml, omega_drive, args.amp,
                           args.steps, args.record_frac)
        results[hand] = r
        print(f"[{hand}] P_rad(signed)={r['P_rad_signed']:+.4e}  "
              f"P_rad(|.|)={r['P_rad_abs']:.4e}  U_near={r['U_near_mean']:.4e}  "
              f"Q_rad={r['Q_rad']:.3f}  |omega|max={r['omega_max']:.3e}  "
              f"(n_rec={r['n_record']})")

    # chiral asymmetry (parity selection rule signature)
    pl, pr = abs(results["LH"]["P_rad_abs"]), abs(results["RH"]["P_rad_abs"])
    asym = (pl - pr) / (pl + pr) if (pl + pr) > 1e-30 else float("nan")
    print(f"\nchiral far-field asymmetry (LH-RH)/(LH+RH) = {asym:+.4f}  "
          f"[expect >0 if LH (substrate-grain) radiates more; 03_neutrino_sector.tex:59]")
    print("radiated-vs-reactive fork: Q_rad << 1 -> radiates (antenna); "
          ">> 1 -> near-field reactance dominates")
    print("\nCAVEAT: smoke run.  Robust observables = sign(asymmetry), Q_rad "
          "order-of-magnitude, P_rad finite/nonzero (propagating).  Absolute "
          "R/X normalization + flux index convention NOT validated this pass.")

    if args.json:
        with open(args.json, "w") as f:
            json.dump({"args": vars(args), "results": results,
                       "R_perp_template": Z_0 / (4 * PI),
                       "chiral_asym": asym}, f, indent=2)
        print(f"\nwrote {args.json}")


if __name__ == "__main__":
    main()
