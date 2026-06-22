#!/usr/bin/env python3
"""OQ-1 — the field -> cavity-phase coupling, DERIVED (clm-pp3qwf strengthen-by).
=================================================================================

Closes OQ-1: upgrade the leading-order pump-probe ``g`` from an ASSERTED
Gaussian-beam overlap parameter (induced_ellipticity first-cut, the #44/#318
sweep) to a PINNED coupling derived from the Axiom-4 kernel + cavity optics, for
THREE apparatus configs, with the QED Euler-Heisenberg leg co-derived through
the SAME chain (no-strawman) and a validate-on-known recovery of PVLAS A_e.

THE CHAIN (each step tagged DERIVED / APPARATUS-INPUT / ASSERTED):
  1. focal-E -> A=E/E_YIELD -> the UNIAXIAL probe-response tensor
     eps_ij = eps*delta_ij + 2 eps'*E0_i E0_j  (eps' = d eps/d(E^2) from the
     SCALAR Axiom-4 kernel eps(E^2)=eps0*sqrt(1-A^2)) -> n_par - n_perp =
     delta_n_bir(A), with the exact (1-A^2)^(1/4) arc and leading -1/4 A^2.
  2. delta_n_bir -> cavity round-trip birefringent phase / ellipticity
     psi = (1/2)(2 pi/lambda)|g delta_n_bir| L (2F/pi): round-trip birefringent
     phase accumulation in the focal-overlap region, finesse-enhanced.
  3. PIN g = (Gaussian-focus w0, z_R) x (cavity-mode overlap) x (temporal) for
     THREE configs: (i) CW high-F; (ii) pulsed single-pass; (iii) the COMBINED
     pulsed-in-gated-cavity (DD1's UNMODELED lever). Compute g + realized psi.
  4. CO-DERIVE the QED Euler-Heisenberg psi through the SAME chain; VALIDATE-ON-
     KNOWN: recover PVLAS A_e (1.32e-24 T^-2) + the QED-EH ellipticity.

Run: PYTHONPATH=src <venv>/python src/scripts/vol_9_device/oq1_field_to_cavity_phase_coupling.py
Sibling sweep: src/scripts/vol_9_device/vacuum_birefringence_facility_sweep.py
Canonical leaf: manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md
Derivation doc (not committed by this script): /tmp/oq1_derivation.md
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

import numpy as np

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from ave.bench import (  # noqa: E402
    coefficient_ratio,
    substrate_identity_holds,
    vacuum_magnetic_birefringence_constant,
)
from ave.core.constants import (  # noqa: E402
    ALPHA,
    C_0,
    E_CRIT,
    E_YIELD,
    EPSILON_0,
    HBAR,
)
from ave.viz import style  # noqa: E402


# ============================================================================
# STEP 1 — UNIAXIAL PROBE-RESPONSE TENSOR FROM THE SCALAR AXIOM-4 KERNEL
# ----------------------------------------------------------------------------
# DERIVED. The Axiom-4 kernel is a SCALAR permittivity in the field-energy
# invariant u = |E|^2:
#       eps(u) = eps0 * S(u),   S = sqrt(1 - u/E_YIELD^2),   A^2 = u/E_YIELD^2.
# The displacement is D_i = eps(u) E_i (isotropic constitutive law of the
# scalar kernel). A weak PROBE e on top of a strong linearly-polarized PUMP E0
# sees the small-signal tensor eps_ij = d D_i / d E_j |_{E=E0}:
#       eps_ij = eps(u0) delta_ij + 2 eps'(u0) E0_i E0_j,
# with eps'(u0) = d eps/d u |_{u0}. This is a UNIAXIAL tensor, optic axis || E0
# (DERIVED — it is the exact differential of the scalar kernel; no SM/QED form
# is imposed). The probe index along (par) and across (perp) the pump axis:
#       n_par^2  = (eps(u0) + 2 eps'(u0) E0^2)/eps0 = S + 2 S' E0^2 ... [in eps0 units]
#       n_perp^2 = eps(u0)/eps0 = S.
# Birefringence n_par - n_perp follows. We expose BOTH the exact arc and the
# leading small-A expansion, and show n_par-n_perp matches the corpus
# delta_n_bir to leading order.
# ============================================================================


def _S(A: float | np.ndarray) -> np.ndarray:
    """Universal saturation factor S = sqrt(1 - A^2) (Axiom 4). A = E/E_YIELD."""
    A = np.asarray(A, dtype=float)
    return np.sqrt(np.clip(1.0 - A**2, 0.0, None))


def eps_scalar_over_eps0(A: float | np.ndarray) -> np.ndarray:
    """Scalar relative permittivity eps(u)/eps0 = S = sqrt(1 - A^2) (DERIVED)."""
    return _S(A)


def eps_prime_times_E2_over_eps0(A: float | np.ndarray) -> np.ndarray:
    """The dimensionless anisotropy strength 2 eps'(u0) E0^2 / eps0 (DERIVED).

    With eps/eps0 = S(u), u = A^2 E_YIELD^2,  d(eps/eps0)/du = S'(u):
        S(u) = (1 - u/E_YIELD^2)^{1/2}
        dS/du = -1/(2 E_YIELD^2) (1 - u/E_YIELD^2)^{-1/2} = -1/(2 E_YIELD^2 S)
    so  2 eps'(u0) E0^2 / eps0 = 2 * dS/du * E0^2 = -A^2 / S.
    (Negative: the pump softens the response along its own axis — the optic
    axis is the SLOW... no, FAST axis; sign carried through below.)
    """
    A = np.asarray(A, dtype=float)
    return -(A**2) / _S(A)


def n_par_minus_perp_exact(A: float | np.ndarray) -> np.ndarray:
    """Exact uniaxial birefringence n_par - n_perp from the scalar kernel (DERIVED).

        n_perp = sqrt(eps/eps0)            = sqrt(S) = (1-A^2)^{1/4}
        n_par  = sqrt(eps/eps0 + 2eps'E0^2/eps0) = sqrt(S - A^2/S)
               = sqrt((S^2 - A^2)/S) = sqrt((1 - 2A^2)/sqrt(1-A^2))
    The probe-PARALLEL component sees the full uniaxial response; the
    probe-PERP component sees only the scalar background. Returns NaN where the
    radicand goes negative (past the optical-validity domain).
    """
    A = np.asarray(A, dtype=float)
    S = _S(A)
    rad_par = (1.0 - 2.0 * A**2)
    with np.errstate(invalid="ignore", divide="ignore"):
        n_par = np.where((rad_par > 0) & (S > 0), np.sqrt(rad_par / S), np.nan)
        n_perp = np.where(S > 0, np.sqrt(S), np.nan)
    return n_par - n_perp


def delta_n_bir_leading(A: float | np.ndarray) -> np.ndarray:
    """Leading-order birefringence n_par - n_perp ~ -(1/2) A^2 (DERIVED).

    Small-A: n_perp = (1-A^2)^{1/4} ~ 1 - A^2/4.
             n_par  = ((1-2A^2)(1-A^2)^{-1/2})^{1/2}
                    ~ (1 - 2A^2)^{1/2}(1 - A^2)^{-1/4}
                    ~ (1 - A^2)(1 + A^2/4) ~ 1 - 3A^2/4.
             n_par - n_perp ~ (1 - 3A^2/4) - (1 - A^2/4) = -A^2/2.
    So the LINEAR-pump uniaxial birefringence leads at -(1/2)A^2 — a FACTOR 2
    above the scalar single-arm shift delta_n_iso = -(1/4)A^2. The corpus
    'delta_n_bir' (the COEFFICIENT-channel discriminator, vacuum-birefringence-
    e4.md:14) is the scalar -1/4 A^2 single-arm shift; the polarimeter's
    PARALLEL-MINUS-PERP differential is -1/2 A^2. Both are O(1)/A^2; the AVE/QED
    ratio is taken at MATCHING observables (see Step 4).
    """
    A = np.asarray(A, dtype=float)
    return -0.5 * A**2


def delta_n_iso_exact(A: float | np.ndarray) -> np.ndarray:
    """Scalar single-arm AVE index shift delta_n_iso = (1-A^2)^{1/4} - 1 (DERIVED).

    The corpus retardance observable (vacuum-birefringence-e4.md:14): n=sqrt(S).
    Evaluated stably via expm1/log1p (small-A catastrophic-cancellation guard).
    """
    A2 = np.asarray(A, dtype=float) ** 2
    safe = np.where(A2 < 1.0, A2, 0.0)
    return np.where(A2 < 1.0, np.expm1(0.25 * np.log1p(-safe)), np.nan)


# ============================================================================
# STEP 2 — delta_n_bir -> CAVITY ROUND-TRIP BIREFRINGENT PHASE / ELLIPTICITY
# ----------------------------------------------------------------------------
# DERIVED (the coupling FORM) + APPARATUS-INPUT (lambda, L, F).
# A probe launched at 45deg to the pump-set optic axis splits into par/perp
# components that accumulate a DIFFERENTIAL phase per single pass through the
# focal-overlap region:
#       delta_phi_single = (2 pi / lambda) * |delta_n_bir| * L_overlap.
# We write L_overlap = g_spatial * L (the Gaussian-focus / cavity-mode overlap
# fraction, Step 3) so the single-pass differential phase referenced to the
# nominal cavity length L is
#       delta_phi_single = (2 pi / lambda) * g_spatial * |delta_n_bir| * L.
# In a Fabry-Perot of finesse F the field makes ~ (2F/pi) effective passes
# through the medium before exiting (the round-trip build-up factor: finesse F
# = pi sqrt(R)/(1-R) ~ pi/(1-R) and the intracavity intensity build-up / number
# of effective bounces ~ 2F/pi). The differential phase accumulates COHERENTLY
# over the build-up ONLY if the medium is present every round trip (a STATIC or
# slowly-varying birefringence): then
#       delta_phi_RT = delta_phi_single * (2F/pi).
# A linearly-polarized probe at 45deg acquires ellipticity psi = delta_phi_RT/2
# (small-angle). g_temporal (Step 3) multiplies in for a transient pump.
# WHY this is the right coupling (the ratified ontology): the observable is
# round-trip birefringent-PHASE accumulation in the focal-overlap region,
# finesse-enhanced — a linear-pump polarimeter. The finesse multiplies the
# COHERENT phase only while the birefringence persists across the build-up time
# tau_build ~ F L/(pi c); a pump shorter than tau_build does NOT get the full
# (2F/pi) (the gated-cavity subtlety, Step 3 config iii).
# ============================================================================


def single_pass_diff_phase(
    delta_n_bir: float, *, g_spatial: float, length_m: float, wavelength_m: float
) -> float:
    """Single-pass differential (par-perp) phase through the focal overlap [rad].

        delta_phi = (2 pi/lambda) * g_spatial * |delta_n_bir| * L.
    """
    return (2.0 * np.pi / wavelength_m) * g_spatial * abs(delta_n_bir) * length_m


def finesse_buildup(finesse: float) -> float:
    """Coherent round-trip build-up enhancement (2F/pi) for F>1, else 1 (DERIVED).

    F = pi sqrt(R)/(1-R); the number of effective coherent passes a field makes
    before exiting ~ 2F/pi. Caps the coherent-accumulation factor.
    """
    return (2.0 * finesse / np.pi) if finesse > 1.0 else 1.0


def ellipticity(
    delta_n_bir: float,
    *,
    g_spatial: float,
    g_temporal: float,
    finesse_coherent: float,
    length_m: float,
    wavelength_m: float,
) -> float:
    """Realized polarimeter ellipticity psi [rad] (the SHARED AVE/QED chain).

        psi = (1/2) * delta_phi_single * g_temporal * (2 F_coherent / pi).
    finesse_coherent is the finesse the build-up is allowed to COHERENTLY use
    (Step 3: full F for CW/static; 1 for single-pass pulsed; the gated value for
    config iii). g_temporal is the pump-overlap-in-time fraction. EVERY factor
    except delta_n_bir is identical between the AVE and QED legs (no-strawman).
    """
    dphi = single_pass_diff_phase(
        delta_n_bir, g_spatial=g_spatial, length_m=length_m, wavelength_m=wavelength_m
    )
    return 0.5 * dphi * g_temporal * finesse_buildup(finesse_coherent)


# ============================================================================
# STEP 3 — PIN g = (Gaussian focus) x (cavity-mode overlap) x (temporal),
#          FOR THREE APPARATUS CONFIGS
# ----------------------------------------------------------------------------
# DERIVED (the overlap integrals, given the beam geometry) + APPARATUS-INPUT
# (w0, tau_pump, F, L, lambda — engineering choices).
#
# SPATIAL OVERLAP (DERIVED given w0, L). The probe differential phase is the
# path integral of the LOCAL birefringence, and delta_n_bir ~ -1/2 A^2 ~ E^2,
# so it tracks the pump INTENSITY profile. A Gaussian pump focus on-axis has
#       I(z) = I_peak / (1 + (z/z_R)^2),   z_R = pi w0^2 / lambda_pump.
# The accumulated phase relative to "delta_n_peak uniform over L" is
#       g_spatial = (1/L) * int_{-L/2}^{+L/2} dz/(1+(z/z_R)^2)
#                 = (2 z_R / L) * arctan(L/(2 z_R)).
# For L >> z_R this -> pi z_R / L (the focal region is a thin slice of the
# cavity); for L << z_R it -> 1 (probe sees uniform peak field). A finite probe
# waist w_p adds the transverse mode-overlap dilution w0^2/(w0^2 + w_p^2).
#
# TEMPORAL OVERLAP (DERIVED given tau_pump, geometry). A pulsed pump of duration
# tau_pump illuminates the focal slice only for that window; a CW free-running
# probe averages the birefringence over the cavity round-trip / photon dwell.
#   - co-timed pulsed probe co-propagating with the pump: g_temporal = 1 (it
#     rides the pulse), but it makes a SINGLE pass (no finesse build-up).
#   - CW probe, transient pump: g_temporal = tau_pump / tau_dwell, where the
#     relevant dwell is the cavity round-trip L/c for a single-bounce average,
#     or the photon lifetime tau_phot = F L/(pi c) for the full build-up.
# ============================================================================


def z_rayleigh(w0_m: float, wavelength_pump_m: float) -> float:
    """Rayleigh range z_R = pi w0^2 / lambda_pump [m] (DERIVED, given w0)."""
    return np.pi * w0_m**2 / wavelength_pump_m


def g_spatial_axial(length_m: float, z_R_m: float) -> float:
    """Axial Gaussian-focus overlap fraction g_spatial (DERIVED, given w0, L).

        g_spatial = (2 z_R / L) arctan(L / (2 z_R)).
    Exact for the Lorentzian on-axis intensity I(z)=I_peak/(1+(z/z_R)^2).
    """
    return (2.0 * z_R_m / length_m) * np.arctan(length_m / (2.0 * z_R_m))


def g_spatial_transverse(w0_m: float, w_probe_m: float) -> float:
    """Transverse probe/pump mode-overlap dilution w0^2/(w0^2+w_p^2) (DERIVED).

    1.0 for a probe matched to (or tighter than) the pump waist; falls as the
    probe over-fills the pump focus.
    """
    return w0_m**2 / (w0_m**2 + w_probe_m**2)


@dataclass(frozen=True)
class ApparatusConfig:
    """An apparatus geometry/timing config (APPARATUS-INPUT engineering choices).

    pump_mode:
      'CW'                  -> CW pump, CW free-running probe (config i, full F)
      'pulse_single'        -> co-timed pulsed probe, single transit (config ii)
      'pulse_gated_cavity'  -> co-timed pulsed probe recirculated in a gated
                               resonant cavity (config iii; pump must persist to
                               imprint each pass)
    """

    name: str
    pump_mode: str         # 'CW' | 'pulse_single' | 'pulse_gated_cavity'
    w0_m: float            # pump focal waist
    w_probe_m: float       # probe waist (transverse overlap)
    length_m: float        # cavity / interaction length
    finesse: float         # cavity finesse (full available)
    wavelength_m: float    # probe wavelength
    wavelength_pump_m: float
    tau_pump_s: float      # pump duration (np.inf for CW pump)


@dataclass(frozen=True)
class CouplingResult:
    """The DERIVED coupling decomposition for one config (every field computed).

    g_eff is the sweep-independent EFFECTIVE coupling: the ratio of the realized
    differential phase to the canonical reference 'uniform delta_n over the full
    cavity length L, single pass'. It folds the spatial overlap, transverse
    dilution, temporal duty, AND the coherent-pass count into ONE number, so
    psi_realized = (1/2)(2 pi/lambda)|delta_n_bir| L * g_eff.
    """

    name: str
    pump_mode: str
    z_R_m: float
    g_spatial_axial: float
    g_spatial_transverse: float
    g_spatial: float
    tau_build_s: float        # cavity build-up time F L / (pi c)
    tau_rt_s: float           # single round-trip transit L / c
    g_temporal: float         # temporal duty fraction (pump-present share of dwell)
    n_coherent_passes: float  # passes whose differential phase adds COHERENTLY
    finesse_coherent: float   # = n_coherent_passes * pi/2 (the usable finesse)
    g_eff: float              # the PINNED sweep-independent coupling (see docstring)


def derive_coupling(cfg: ApparatusConfig) -> CouplingResult:
    """PIN the coupling for one config from the Gaussian focus + cavity timing.

    DERIVED (given the APPARATUS-INPUT geometry/timing): the realized polarimeter
    coupling decomposes as

        g_eff = g_spatial * g_temporal * n_coherent_passes,

    where
      g_spatial         = g_spatial_axial(L, z_R) * g_spatial_transverse(w0, w_p)
                          (the Gaussian-focus path integral + mode overlap);
      g_temporal        = pump-present fraction of the relevant probe dwell;
      n_coherent_passes = number of transits whose differential phases add
                          COHERENTLY (1 for single pass; 2F/pi for a CW probe in
                          a high-F cavity holding a static birefringence; but
                          capped by how many round trips the pump survives for a
                          transient pump).

    The three configs differ ONLY in the temporal/coherent factors; g_spatial is
    common (same focus, same cavity length).
    """
    z_R = z_rayleigh(cfg.w0_m, cfg.wavelength_pump_m)
    gs_ax = g_spatial_axial(cfg.length_m, z_R)
    gs_tr = g_spatial_transverse(cfg.w0_m, cfg.w_probe_m)
    g_spatial = gs_ax * gs_tr

    tau_build = cfg.finesse * cfg.length_m / (np.pi * C_0)  # photon lifetime
    tau_rt = cfg.length_m / C_0                              # single round-trip transit
    max_coherent_passes = 2.0 * cfg.finesse / np.pi          # full finesse build-up

    if cfg.pump_mode == "CW":
        # CW pump (always on), CW free-running probe. The standing intracavity
        # field builds up fully (n_coherent = 2F/pi); the birefringence is static
        # so every pass adds coherently; no temporal dilution.
        g_temporal = 1.0
        n_coherent = max_coherent_passes
    elif cfg.pump_mode == "pulse_single":
        # Co-timed pulsed probe co-propagating with the pump: rides the pulse
        # through the focal slice => full temporal overlap, but SINGLE transit
        # (no recirculation). Finesse is irrelevant.
        g_temporal = 1.0
        n_coherent = 1.0
    elif cfg.pump_mode == "pulse_gated_cavity":
        # Co-timed pulsed probe recirculated in a gated resonant cavity. For the
        # finesse build-up to add COHERENTLY, the pump must be PRESENT each time
        # the recirculating probe re-enters the focus (every tau_rt). A single
        # pump pulse survives only tau_pump; the recirculating probe re-enters
        # after tau_rt. The number of coherent passes the pump can gate is
        #   n_pump_gated = tau_pump / tau_rt   (how many round trips fit in the
        #                  pump window),
        # capped at the cavity build-up ceiling 2F/pi. g_temporal = 1 (the probe
        # rides the pump on the FIRST pass), but subsequent passes only add if
        # the pump persists.
        g_temporal = 1.0
        n_pump_gated = cfg.tau_pump_s / tau_rt if np.isfinite(cfg.tau_pump_s) else np.inf
        # At least one pass always happens (the co-timed first transit); the
        # cavity adds floor(n_pump_gated) further coherent passes, up to 2F/pi.
        n_coherent = float(np.clip(max(1.0, n_pump_gated), 1.0, max_coherent_passes))
    else:
        raise ValueError(f"unknown pump_mode {cfg.pump_mode!r}")

    finesse_coherent = n_coherent * np.pi / 2.0
    g_eff = g_spatial * g_temporal * n_coherent
    return CouplingResult(
        name=cfg.name,
        pump_mode=cfg.pump_mode,
        z_R_m=float(z_R),
        g_spatial_axial=float(gs_ax),
        g_spatial_transverse=float(gs_tr),
        g_spatial=float(g_spatial),
        tau_build_s=float(tau_build),
        tau_rt_s=float(tau_rt),
        g_temporal=float(g_temporal),
        n_coherent_passes=float(n_coherent),
        finesse_coherent=float(finesse_coherent),
        g_eff=float(g_eff),
    )


def realized_ellipticity(
    delta_n_bir: float, cr: CouplingResult, *, length_m: float, wavelength_m: float
) -> float:
    """Realized polarimeter ellipticity psi from the PINNED coupling (DERIVED).

        psi = (1/2)(2 pi/lambda)|delta_n_bir| L * g_eff.
    g_eff carries the full Gaussian-focus + cavity-timing decomposition.
    """
    return 0.5 * (2.0 * np.pi / wavelength_m) * abs(delta_n_bir) * length_m * cr.g_eff


# ============================================================================
# STEP 4 — CO-DERIVE the QED Euler-Heisenberg leg THROUGH THE SAME CHAIN, and
#          VALIDATE-ON-KNOWN (recover PVLAS A_e + the QED-EH ellipticity).
# ----------------------------------------------------------------------------
# NON-AVE LITERATURE baseline (Heisenberg-Euler 1936; PVLAS/Rizzo). The QED
# weak-field birefringence under a static linearly-polarized field:
#       n_par  - 1 = (7/45) alpha^2 (E/E_crit)^2     (probe || field)
#       n_perp - 1 = (4/45) alpha^2 (E/E_crit)^2     (probe _|_ field)
#       n_par - n_perp = (3/45) alpha^2 (E/E_crit)^2 (the DIFFERENTIAL).
# The polarimeter measures the DIFFERENTIAL (par-perp) ellipticity. To compare
# AVE-vs-QED AT THE MATCHED OBSERVABLE, both legs use their DIFFERENTIAL shift:
#   AVE differential  delta_n_bir = n_par - n_perp ~ -(1/2) A^2   (Step 1)
#   QED differential  delta_n_qed_diff = (3/45) alpha^2 (E/E_crit)^2.
# Both ride the IDENTICAL realized_ellipticity(delta_n, coupling) machinery; the
# ONLY difference is the index-shift coefficient (no-strawman R1).
# ============================================================================

A_EH_DIFFERENTIAL: float = 3.0 / 45.0  # QED par-minus-perp (the matched observable)
A_EH_PARALLEL: float = 7.0 / 45.0      # QED single-mode parallel (corpus headline)


def delta_n_qed_differential(E: float | np.ndarray) -> np.ndarray:
    """QED Euler-Heisenberg DIFFERENTIAL birefringence (3/45) alpha^2 (E/E_crit)^2.

    LITERATURE baseline; the par-minus-perp shift a PVLAS/BMV ellipsometer reads.
    """
    return A_EH_DIFFERENTIAL * ALPHA**2 * (np.asarray(E, dtype=float) / E_CRIT) ** 2


def ratio_differential_matched() -> float:
    """AVE/QED ratio at the MATCHED differential observable (DERIVED form, ECHO mag).

        delta_n_bir / delta_n_qed_diff
          = (1/2)/E_YIELD^2 / [(3/45) alpha^2 / E_CRIT^2]
          = (1/2)/((3/45) alpha^2) * (E_CRIT/E_YIELD)^2
          = (45/6)/alpha^3 = 7.5/alpha^3.
    Field-INDEPENDENT (both E^2-leading), riding the substrate identity
    (E_CRIT/E_YIELD)^2 = 1/alpha. The MAGNITUDE is an alpha-echo (symmetric
    standard: QED's coefficient is equally alpha-rooted); the FORM (tree-O(1)/2
    saturation vs alpha^2 loop) is the AVE-distinct chord.
    """
    return (0.5 / (A_EH_DIFFERENTIAL * ALPHA**2)) * (E_CRIT / E_YIELD) ** 2


def validate_on_known() -> dict:
    """HALT-gate: recover PVLAS A_e (1.32e-24 T^-2) + substrate identity.

    Co-derives the QED-EH magnetic differential constant A_e through the SAME
    closed form the bench uses (ave.bench), confirms it lands on the PVLAS
    textbook value, and confirms (E_CRIT/E_YIELD)^2 == 1/alpha and c B_crit ==
    E_CRIT (substrate_identity_holds). HALT (SystemExit 1) on any failure.
    """
    A_e = vacuum_magnetic_birefringence_constant()
    A_e_target = 1.32e-24
    A_e_relerr = abs(A_e - A_e_target) / A_e_target
    identity_ok = bool(substrate_identity_holds())
    A_e_ok = bool(A_e_relerr < 0.01)
    gate = {
        "A_e_value_Tinv2": float(A_e),
        "A_e_target_Tinv2": A_e_target,
        "A_e_relerr": float(A_e_relerr),
        "A_e_recovers_PVLAS": A_e_ok,
        "substrate_identity_(Ecrit/Eyield)^2==1/alpha_and_cBcrit==Ecrit": identity_ok,
    }
    if not (A_e_ok and identity_ok):
        print("HALT: validate-on-known FAILED.")
        print(f"  A_e = {A_e:.6e} vs {A_e_target:.3e} (relerr {A_e_relerr:.3e})")
        print(f"  substrate identity: {identity_ok}")
        sys.exit(1)
    return gate


# ============================================================================
# APPARATUS POINT (the headline facility operating point — APPARATUS-INPUTs)
# ============================================================================
# PW-class focus: I ~ 1e22 W/cm^2 -> E_peak = sqrt(2 I/(c eps0)) ~ 2.74e14 V/m.
I_PEAK_W_CM2: float = 1.0e22
LAMBDA_PROBE_M: float = 1064.0e-9   # Nd:YAG
LAMBDA_PUMP_M: float = 800.0e-9     # Ti:Sa
L_CAVITY_M: float = 1.0e-2          # cm cavity
FINESSE: float = 1.0e3              # modest finesse (stays in small-angle)
W0_PUMP_M: float = LAMBDA_PUMP_M    # diffraction-limited focus w0 ~ lambda_pump
W_PROBE_M: float = LAMBDA_PUMP_M    # mode-matched probe
TAU_PUMP_FS_S: float = 30.0e-15     # fs pump (config ii/iii)
TAU_PUMP_GATE_S: float = 20.0e-9    # ns pump that GATES the build-up (config iii-long)
SMALL_ANGLE_CEILING: float = 0.1


def peak_field_from_intensity(I_w_cm2: float) -> float:
    """Plane-wave peak field E = sqrt(2 I / (c eps0)) [V/m] (I in W/cm^2)."""
    I_si = I_w_cm2 * 1.0e4  # W/cm^2 -> W/m^2
    return float(np.sqrt(2.0 * I_si / (C_0 * EPSILON_0)))


def _build_configs() -> list[ApparatusConfig]:
    """The four apparatus configs (i, ii, iii-fs, iii-ns) — APPARATUS-INPUTs."""
    common = dict(
        w0_m=W0_PUMP_M, w_probe_m=W_PROBE_M, length_m=L_CAVITY_M,
        wavelength_m=LAMBDA_PROBE_M, wavelength_pump_m=LAMBDA_PUMP_M,
    )
    return [
        ApparatusConfig("(i) CW high-F", "CW", finesse=FINESSE,
                        tau_pump_s=float("inf"), **common),
        ApparatusConfig("(ii) pulsed single-pass", "pulse_single", finesse=1.0,
                        tau_pump_s=TAU_PUMP_FS_S, **common),
        ApparatusConfig("(iii-fs) pulsed gated-cavity (30 fs pump)",
                        "pulse_gated_cavity", finesse=FINESSE,
                        tau_pump_s=TAU_PUMP_FS_S, **common),
        ApparatusConfig("(iii-ns) pulsed gated-cavity (20 ns gate pump)",
                        "pulse_gated_cavity", finesse=FINESSE,
                        tau_pump_s=TAU_PUMP_GATE_S, **common),
    ]


def _per_config_report(E_peak: float) -> dict:
    """Compute the PINNED g + realized psi (AVE differential + QED differential)
    for each config at the headline field. DERIVED coupling, no-strawman QED."""
    A = E_peak / E_YIELD
    dn_ave_bir = float(delta_n_bir_leading(A))      # AVE par-perp differential
    dn_qed_bir = float(delta_n_qed_differential(E_peak))  # QED par-perp differential
    out: dict = {
        "E_peak_Vm": float(E_peak),
        "A_saturation": float(A),
        "dn_ave_differential_leading": dn_ave_bir,
        "dn_ave_differential_exact": float(n_par_minus_perp_exact(A)),
        "dn_qed_differential": dn_qed_bir,
        "ratio_differential_matched": float(ratio_differential_matched()),
        "configs": [],
    }
    for cfg in _build_configs():
        cr = derive_coupling(cfg)
        psi_ave = realized_ellipticity(
            dn_ave_bir, cr, length_m=cfg.length_m, wavelength_m=cfg.wavelength_m
        )
        psi_qed = realized_ellipticity(
            dn_qed_bir, cr, length_m=cfg.length_m, wavelength_m=cfg.wavelength_m
        )
        out["configs"].append({
            "name": cr.name,
            "pump_mode": cr.pump_mode,
            "z_R_m": cr.z_R_m,
            "g_spatial": cr.g_spatial,
            "g_temporal": cr.g_temporal,
            "n_coherent_passes": cr.n_coherent_passes,
            "tau_build_s": cr.tau_build_s,
            "tau_rt_s": cr.tau_rt_s,
            "g_eff": cr.g_eff,
            "psi_ave_rad": float(psi_ave),
            "psi_qed_rad": float(psi_qed),
            "psi_ratio_ave_over_qed": float(psi_ave / psi_qed) if psi_qed > 0 else float("inf"),
            "small_angle_valid": bool(abs(psi_ave) < SMALL_ANGLE_CEILING),
        })
    return out


def _recommend(report: dict) -> dict:
    """Pick the optimal config: largest realized psi_ave that stays in small-angle
    and is above the realistic 1e-9 rad polarimetry floor. Surfaces the
    fs-gated-cavity NULL finding (config iii-fs == config ii)."""
    floor = 1.0e-9
    valid = [
        c for c in report["configs"]
        if c["small_angle_valid"] and c["psi_ave_rad"] >= floor
    ]
    best = max(valid, key=lambda c: c["psi_ave_rad"]) if valid else None
    # The DD1 question: does the fs gated cavity recover anything beyond single-pass?
    c_single = next(c for c in report["configs"] if c["pump_mode"] == "pulse_single")
    c_gate_fs = next(c for c in report["configs"] if "iii-fs" in c["name"])
    c_gate_ns = next(c for c in report["configs"] if "iii-ns" in c["name"])
    fs_gate_recovers = c_gate_fs["g_eff"] > 1.001 * c_single["g_eff"]
    return {
        "recommended": best["name"] if best else None,
        "recommended_psi_ave_rad": best["psi_ave_rad"] if best else None,
        "recommended_g_eff": best["g_eff"] if best else None,
        "polarimetry_floor_rad": floor,
        "fs_gated_cavity_recovers_finesse": bool(fs_gate_recovers),
        "fs_gated_cavity_g_eff": c_gate_fs["g_eff"],
        "single_pass_g_eff": c_single["g_eff"],
        "ns_gated_cavity_g_eff": c_gate_ns["g_eff"],
        "ns_gated_cavity_n_coherent": c_gate_ns["n_coherent_passes"],
        "pump_duration_to_gate_full_F_s": c_gate_ns["tau_build_s"],
    }


# ============================================================================
# FIGURES (ave.viz.style; no baked titles; computed captions)
# ============================================================================
def _fig_birefringence_arc(out_stub: Path) -> tuple[list[Path], str]:
    """Panel: the DERIVED uniaxial differential n_par-n_perp(A) vs the leading
    -1/2 A^2 and the scalar single-arm -1/4 A^2, over the deep-linear range."""
    A = np.logspace(-4.0, np.log10(0.27), 200)
    bir_exact = -n_par_minus_perp_exact(A)        # plot magnitude (negative shift)
    bir_lead = -delta_n_bir_leading(A)
    iso_exact = -delta_n_iso_exact(A)
    fig, ax = plt.subplots(figsize=style.figsize("single"))
    ax.loglog(A, bir_exact, color=style.COLORS["ave"], lw=2.0,
              label=r"AVE differential $|n_\parallel-n_\perp|$ (exact)")
    ax.loglog(A, bir_lead, color=style.COLORS["accent"], lw=1.3, ls="--",
              label=r"leading $\frac{1}{2} A^2$")
    ax.loglog(A, iso_exact, color=style.COLORS["comparison"], lw=1.6, ls="-.",
              label=r"scalar single-arm $|(1-A^2)^{1/4}-1|$")
    ax.set_xlabel(style.axis_label("Pump saturation", "A=E/E_{yield}", "dimensionless"))
    ax.set_ylabel(style.axis_label("Index shift magnitude", r"|\delta n|", "dimensionless"))
    style.legend(ax, where="right", fontsize=8)
    written = style.save(fig, out_stub, strict=True)
    plt.close(fig)
    A_ref = 2.4e-3
    caption = (
        f"DERIVED uniaxial probe-response birefringence from the scalar Axiom-4 "
        f"kernel. The linearly-polarized pump turns the scalar permittivity "
        f"eps(|E|^2)=eps0 sqrt(1-A^2) into a uniaxial probe tensor "
        f"eps_ij=eps delta_ij+2eps' E0_i E0_j; the par-minus-perp differential "
        f"leads at -1/2 A^2 (a factor 2 above the scalar single-arm -1/4 A^2). "
        f"At the PW-class operating point A={A_ref:.1e}, "
        f"|n_par-n_perp|={float(-n_par_minus_perp_exact(A_ref)):.2e}."
    )
    return written, caption


def _fig_config_coupling(report: dict, out_stub: Path) -> tuple[list[Path], str]:
    """Panel: realized psi_ave per config (bar), with the small-angle ceiling and
    the realistic floor — the per-config pinned-coupling comparison."""
    names = [c["name"].split(" ", 1)[0] for c in report["configs"]]
    psis = [c["psi_ave_rad"] for c in report["configs"]]
    g_effs = [c["g_eff"] for c in report["configs"]]
    fig, ax = plt.subplots(figsize=style.figsize("single"))
    xs = np.arange(len(names))
    ax.bar(xs, psis, color=style.COLORS["ave"], width=0.6)
    ax.set_yscale("log")
    ax.axhline(SMALL_ANGLE_CEILING, color=style.COLORS["comparison"], ls="--", lw=1.3,
               label=f"small-angle ceiling {SMALL_ANGLE_CEILING} rad")
    ax.axhline(1.0e-9, color=style.COLORS["accent"], ls="-.", lw=1.3,
               label=r"realistic floor $10^{-9}$ rad")
    ax.set_xticks(xs)
    ax.set_xticklabels(names, rotation=0, fontsize=8)
    ax.set_ylabel(style.axis_label("Realized ellipticity", r"\psi_{AVE}", "rad"))
    style.legend(ax, where="right", fontsize=8)
    written = style.save(fig, out_stub, strict=True)
    plt.close(fig)
    rec = report["recommendation"]
    caption = (
        f"Realized AVE polarimeter ellipticity per apparatus config at the "
        f"PW-class operating point (E={report['E_peak_Vm']:.2e} V/m, "
        f"A={report['A_saturation']:.1e}), from the PINNED coupling "
        f"g_eff. g_eff per config: (i) {g_effs[0]:.2e}, (ii) {g_effs[1]:.2e}, "
        f"(iii-fs) {g_effs[2]:.2e}, (iii-ns) {g_effs[3]:.2e}. The 30 fs gated "
        f"cavity (iii-fs) recovers NOTHING beyond single-pass (g_eff identical to "
        f"(ii)) because the fs pump is gone before the recirculating probe returns "
        f"({report['configs'][2]['tau_rt_s']:.1e} s round trip); a "
        f"ns-class gate pump (iii-ns) recovers near-full finesse. Recommended: "
        f"{rec['recommended']}."
    )
    return written, caption


def _fig_gate_constraint(out_stub: Path) -> tuple[list[Path], str]:
    """Panel: the gated-cavity recovery — n_coherent_passes vs pump duration,
    showing the tau_build threshold above which the gate recovers full finesse."""
    tau = np.logspace(-15.0, -6.0, 200)
    cfgs = [
        ApparatusConfig("scan", "pulse_gated_cavity", w0_m=W0_PUMP_M, w_probe_m=W_PROBE_M,
                        length_m=L_CAVITY_M, finesse=FINESSE, wavelength_m=LAMBDA_PROBE_M,
                        wavelength_pump_m=LAMBDA_PUMP_M, tau_pump_s=t)
        for t in tau
    ]
    n_coh = np.array([derive_coupling(c).n_coherent_passes for c in cfgs])
    tau_build = FINESSE * L_CAVITY_M / (np.pi * C_0)
    fig, ax = plt.subplots(figsize=style.figsize("single"))
    ax.loglog(tau, n_coh, color=style.COLORS["ave"], lw=2.0,
              label=r"$n_{coherent}$ (gated cavity)")
    ax.axhline(2.0 * FINESSE / np.pi, color=style.COLORS["comparison"], ls="--", lw=1.3,
               label=r"full build-up $2F/\pi$")
    ax.axvline(tau_build, color=style.COLORS["accent"], ls="-.", lw=1.3,
               label=r"$\tau_{build}=FL/\pi c$")
    ax.axvline(TAU_PUMP_FS_S, color=style.COLORS["muted"], ls=":", lw=1.2,
               label="30 fs pump")
    ax.set_xlabel(style.axis_label("Pump duration", r"\tau_{pump}", "s"))
    ax.set_ylabel(style.axis_label("Coherent passes", "n_{coherent}", "dimensionless"))
    style.legend(ax, where="right", fontsize=8)
    written = style.save(fig, out_stub, strict=True)
    plt.close(fig)
    caption = (
        f"The gated-cavity finesse-recovery constraint (DD1's unmodeled lever, "
        f"now modeled). A co-timed pulsed probe recirculated in a resonant cavity "
        f"recovers the full finesse build-up (2F/pi={2.0*FINESSE/np.pi:.0f} passes "
        f"at F={FINESSE:.0e}) ONLY when the pump persists across the cavity "
        f"build-up time tau_build={tau_build:.2e} s. A 30 fs pump gates only "
        f"n_coherent=1 (single pass): it is gone before the recirculating probe "
        f"re-enters the focus ({L_CAVITY_M/C_0:.1e} s round trip). Recovering both "
        f"finesse AND temporal overlap requires a ns-class pump (a "
        f"{tau_build/TAU_PUMP_FS_S:.1e}x larger pulse energy at fixed peak field)."
    )
    return written, caption


def _make_figures(report: dict, out_dir: Path) -> dict:
    style.apply()
    figs: dict = {}
    for name, fn, needs_report in (
        ("birefringence_arc", _fig_birefringence_arc, False),
        ("config_coupling", _fig_config_coupling, True),
        ("gate_constraint", _fig_gate_constraint, False),
    ):
        stub = out_dir / f"oq1_field_to_cavity_phase_coupling_{name}"
        written, caption = (fn(report, stub) if needs_report else fn(stub))
        figs[name] = {"paths": [str(p) for p in written], "caption": caption}
    return figs


def main() -> None:
    out: dict = {}
    print("=" * 78)
    print("OQ-1 — FIELD -> CAVITY-PHASE COUPLING, DERIVED (clm-pp3qwf strengthen-by)")
    print("=" * 78)

    # ---- (0) VALIDATE-ON-KNOWN (HALT on fail) -------------------------------
    gate = validate_on_known()
    out["validate_on_known"] = gate
    print("\n[0] VALIDATE-ON-KNOWN (HALT if fail):")
    print(f"    PVLAS A_e = {gate['A_e_value_Tinv2']:.4e} T^-2 vs textbook "
          f"{gate['A_e_target_Tinv2']:.3e} (relerr {gate['A_e_relerr']:.2e}) -> PASS")
    print(f"    substrate identity (E_crit/E_yield)^2==1/alpha & c B_crit==E_crit: "
          f"{gate['substrate_identity_(Ecrit/Eyield)^2==1/alpha_and_cBcrit==Ecrit']}")
    print(f"    anchors: E_YIELD={E_YIELD:.4e}  E_CRIT={E_CRIT:.4e}  1/alpha={1.0/ALPHA:.4f}")

    # ---- (1) STEP 1: uniaxial tensor ----------------------------------------
    A_ref = peak_field_from_intensity(I_PEAK_W_CM2) / E_YIELD
    print("\n[1] STEP 1 — uniaxial probe-response tensor (DERIVED from scalar kernel):")
    print(f"    eps_ij = eps delta_ij + 2 eps' E0_i E0_j, optic axis || pump")
    print(f"    AVE differential n_par-n_perp leading = -1/2 A^2 (= 2x scalar single-arm -1/4 A^2)")
    print(f"    at A={A_ref:.3e}: differential(exact)={float(n_par_minus_perp_exact(A_ref)):.4e}, "
          f"leading={float(delta_n_bir_leading(A_ref)):.4e}")

    # ---- (2) STEP 4: matched-observable ratio -------------------------------
    r_diff = ratio_differential_matched()
    r_single = coefficient_ratio(A_EH_PARALLEL)
    out["ratios"] = {
        "differential_matched_AVE(-1/2)/QED(3/45)": float(r_diff),
        "differential_matched_closed_7.5_over_alpha3": float(7.5 / ALPHA**3),
        "corpus_single_arm_AVE(-1/4)/QED_parallel(7/45)": float(r_single),
    }
    print("\n[2] STEP 4 — matched-observable AVE/QED ratio (no-strawman, co-derived):")
    print(f"    DIFFERENTIAL (par-perp, the polarimeter observable): "
          f"AVE(-1/2 A^2)/QED(3/45) = {r_diff:.4e} = 7.5/alpha^3 (field-independent)")
    print(f"    corpus single-arm AVE(-1/4)/QED-parallel(7/45)       = {r_single:.4e}")
    print(f"    BOTH ride the substrate identity (E_crit/E_yield)^2=1/alpha; both "
          f"field-independent. FLAG: corpus headline pairs MISMATCHED observables "
          f"(AVE scalar single-arm vs QED parallel single-mode); differential-vs-"
          f"differential is the matched comparison -> {r_diff:.2e}.")

    # ---- (3) STEP 3: per-config pinned g + psi -------------------------------
    E_peak = peak_field_from_intensity(I_PEAK_W_CM2)
    report = _per_config_report(E_peak)
    rec = _recommend(report)
    report["recommendation"] = rec
    out["per_config"] = report
    print(f"\n[3] STEP 3 — per-config PINNED coupling g_eff + realized psi "
          f"(E_peak={E_peak:.3e} V/m, A={E_peak/E_YIELD:.3e}, PW-class focus):")
    for c in report["configs"]:
        flag = "" if c["small_angle_valid"] else "  [OUT OF SMALL-ANGLE]"
        print(f"    {c['name']}")
        print(f"        g_spatial={c['g_spatial']:.3e}  g_temporal={c['g_temporal']:.3e}  "
              f"n_coherent={c['n_coherent_passes']:.3e}  g_eff={c['g_eff']:.3e}")
        print(f"        psi_AVE={c['psi_ave_rad']:.3e} rad  psi_QED={c['psi_qed_rad']:.3e} rad  "
              f"AVE/QED={c['psi_ratio_ave_over_qed']:.3e}{flag}")
    print(f"\n    DD1 lever resolved: fs gated cavity recovers finesse beyond single-pass? "
          f"{rec['fs_gated_cavity_recovers_finesse']}")
    print(f"      (iii-fs) g_eff={rec['fs_gated_cavity_g_eff']:.3e} == (ii) single-pass "
          f"g_eff={rec['single_pass_g_eff']:.3e}  -> 30 fs pump gates only 1 pass")
    print(f"      (iii-ns) g_eff={rec['ns_gated_cavity_g_eff']:.3e} "
          f"(n_coherent={rec['ns_gated_cavity_n_coherent']:.1f}) -> ns gate recovers near-full F")
    print(f"      a pump >= tau_build={rec['pump_duration_to_gate_full_F_s']:.2e} s is needed "
          f"to gate the full finesse")
    print(f"\n    RECOMMENDED config: {rec['recommended']} "
          f"(psi_AVE={rec['recommended_psi_ave_rad']:.3e} rad, g_eff={rec['recommended_g_eff']:.3e})")

    # ---- (4) FIGURES --------------------------------------------------------
    out_dir = Path(__file__).resolve().parent / "_output"
    out_dir.mkdir(exist_ok=True)
    print("\n[4] FIGURES (house style, computed captions):")
    figs = _make_figures(report, out_dir)
    out["figures"] = figs
    for name, info in figs.items():
        for p in info["paths"]:
            print(f"    wrote {p}")

    # ---- (5) WRITE JSON -----------------------------------------------------
    out_path = out_dir / "oq1_field_to_cavity_phase_coupling.json"
    out_path.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nResults written: {out_path}")
    print("=" * 78)


if __name__ == "__main__":
    main()
