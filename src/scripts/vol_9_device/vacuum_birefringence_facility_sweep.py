#!/usr/bin/env python3
"""
Vacuum-Birefringence FACILITY-SCALE SENSITIVITY SWEEP — AVE vs QED, hardened (#44/#318).
=========================================================================================

The facility-scale hardening of the vacuum-birefringence bench-model gate
(vacuum_birefringence_bench.py). Where the bench-model walked a handful of
representative (E, F) points, this driver sweeps the FULL 5-D facility design
space and extracts the DIVERGENCE WINDOW: the E x F x g region where the
realized AVE polarimeter ellipticity psi_AVE BOTH clears the polarimetry floor
AND is measurably above its co-computed QED counterpart.

THE FIVE SWEEP AXES (facility design space):
  E        — applied / probe peak field, 1e9 -> 3e16 V/m (lab-magnet-equivalent
             -> ELI-extreme laser focus; A = E/E_YIELD stays << 1 throughout,
             deep-linear regime, the ratified LINEAR-pump -> POLARIMETER).
  finesse  — Fabry-Perot probe-cavity finesse, 1e2 -> 1e5 (PVLAS/BMV lineage).
  lambda   — probe wavelength (Nd:YAG 1064 nm, doubled 532 nm, Ti:Sa 800 nm).
  L        — interaction / cavity length (overlap-limited mm -> cm).
  g        — pump-probe geometry coupling factor (field -> cavity-phase coupling),
             now the OQ-1 PINNED per-config g_eff (oq1_field_to_cavity_phase_-
             coupling.py): g_eff ~ 0.251 (full coherent finesse: CW pump high-F
             or ns-gated pulsed cavity) and g_eff ~ 3.95e-4 (single-pass /
             fs-gated cavity, g_spatial only — NO finesse recovery, the fs pump
             is gone before the recirculating probe returns), plus the
             worst-credible 1e-5 / 1e-8 tail. (Supersedes the first-cut DERIVE-1
             bound 7.9e-4; the OQ-1 derivation pins it as a Gaussian-focus x
             cavity-timing overlap.)

THE NO-STRAWMAN CONTRACT (ave.bench R1): at EVERY sweep point the QED
Euler-Heisenberg baseline is co-computed THROUGH THE SAME machinery
(same delta_n -> same induced_ellipticity(g, F, L, lambda) -> same shot-noise
floor) as the AVE prediction. The ONLY difference between the AVE and QED legs
is the index-shift coefficient (AVE O(1)/4 saturating kernel vs QED
a_EH*alpha^2 Euler-Heisenberg). There is no pre-baked SM array anywhere.

VALIDATE-ON-KNOWN GATE (HALT on fail):
  (a) substrate identity (E_crit/E_yield)^2 == 1/alpha (the ratio collapse);
  (b) PVLAS vacuum magnetic birefringence constant A_e == 1.32e-24 T^-2;
  (c) c*B_crit == E_crit (B<->E energy-density equivalence).

DISCIPLINE TAGS (consistency-vs-emergence, chord-vs-echo, symmetric-standard):
  - delta_n_AVE FORM (E^2-leading sqrt-S kernel): MANIFESTATION of Axiom 4.
  - The AVE/QED COEFFICIENT ratio ~1/(4 a_EH alpha^3) ~ 4.14e6: an ECHO at the
    value level (alpha^3-rooted), tagged per chord-vs-echo. The symmetric
    standard holds: QED's own a_EH*alpha^2 is equally alpha-rooted and QED does
    not derive alpha either. The discriminator's force is the ~6-OOM
    field-INDEPENDENT coefficient gap, not the precise prefactor.
  - g: an OPTICS/engineering coupling (consistency-class, correctly outside the
    AVE constants gate); the absolute psi rides g, the COEFFICIENT ratio does
    NOT (g cancels in ratio — same apparatus multiplies AVE and QED equally).
  - Coordinates: real-space / optical-path, matched to the real-space probe
    tensor (phase-space-coordinate-check PASS: no phi^2-vs-Cartesian mismatch).

FLAG (flag-don't-fix, surfaced to Grant/auditor, DERIVE-1 + DERIVE-2):
  (i)  The coefficient ratio 4.14e6 is g-INDEPENDENT; do NOT headline "1e4x QED
       at g~1e-3" — that conflates the g-independent ratio with the g-dependent
       absolute-signal margin. g sets only the ABSOLUTE realized signal vs floor.
  (ii) The A_EH_LITERATURE entry "PVLAS A_e differential (~1.45)" yields ratio
       4.42e5; DERIVE-2 flags this as a 1/(2*pi*alpha)=21.81 units artifact, NOT
       a physical EH coefficient. The physical single-mode band is
       [7/45 -> 4.14e6, 3/45 -> 9.65e6]; we report the band from the physical
       set and surface the artifact separately rather than anchor the band on it.

Run:  PYTHONPATH=src .venv/bin/python src/scripts/vol_9_device/vacuum_birefringence_facility_sweep.py
Sibling bench-model: src/scripts/vol_9_device/vacuum_birefringence_bench.py
Result doc:          research/2026-06-20_vacuum-birefringence-bench_result.md
Canonical leaf:      manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from ave.bench import (  # noqa: E402
    A_EH_LITERATURE,
    coefficient_ratio,
    delta_n_ave_exact,
    delta_n_qed,
    substrate_identity_holds,
    time_to_n_sigma,
    vacuum_magnetic_birefringence_constant,
)
from ave.core.constants import (  # noqa: E402
    ALPHA,
    C_0,
    E_CRIT,
    E_YIELD,
    HBAR,
)
from ave.viz import style  # noqa: E402

# ----------------------------------------------------------------------------
# Reference a_EH for the headline retardance comparison (single-mode parallel
# 7/45, DERIVE-2 LOCKED headline). The full physical band is reported.
# ----------------------------------------------------------------------------
A_EH_REF: float = 7.0 / 45.0

# Small-angle validity ceiling for the psi ~ dphi/2 linearization [rad]. Past
# this the first-cut ellipticity mapping is not credible (DERIVE-3 Rule-10
# finding: as-spec'd high-F + facility field drives psi out of small-angle).
SMALL_ANGLE_CEILING: float = 0.1

# Probe optical power on the polarimetry detector [W] (engineering input, the
# shot-noise resource). 1 W sits at the PVLAS/BMV achieved shot floor.
PROBE_POWER_W: float = 1.0

# Detection significance for time-to-Nsigma [sigma].
SIGMA_TARGET: float = 5.0

# Shot-noise-limited polarimetry ellipticity floor [rad]. Two references
# (DERIVE-3, PVLAS/BMV lineage): 1e-11 optimistic long-integration per-root-Hz
# class, 1e-9 realistic single-shot. These are ENGINEERING inputs (NOT derived,
# NOT validated-on-known against a specific published cavity — the OQ-1 owed
# next step), used as the static detectability margin.
PSI_FLOOR_OPTIMISTIC: float = 1.0e-11
PSI_FLOOR_REALISTIC: float = 1.0e-9


# ============================================================================
# Apparatus coupling: field -> realized polarimeter ellipticity (the SHARED
# machinery both AVE and QED legs ride — the no-strawman R1 contract).
# ============================================================================
def induced_ellipticity(
    delta_n: float, *, g: float, finesse: float, length_m: float, wavelength_m: float
) -> float:
    """Realized polarimeter ellipticity psi from an index shift delta_n.

    The shared field -> delta_n -> cavity round-trip phase -> ellipticity
    coupling (DERIVE-1/DERIVE-3 first-cut model):

        single-pass phase  dphi = (2 pi / lambda) * |g * delta_n| * L
        finesse build-up   enhancement = (2 F / pi)  for F > 1, else 1
        ellipticity        psi = 0.5 * dphi * enhancement

    g is the pump-probe geometry coupling (DERIVE-1, an optics/engineering
    residual, consistency-class). EVERY non-delta_n factor here is identical
    between the AVE and QED legs; the discrimination lives ENTIRELY in delta_n
    (the no-strawman R1 invariant). NOT the derived facility coupling (OQ-1).
    """
    single_pass_phase = (2.0 * np.pi / wavelength_m) * abs(g * delta_n) * length_m
    enhancement = (2.0 * finesse / np.pi) if finesse > 1.0 else 1.0
    return 0.5 * single_pass_phase * enhancement


def probe_photon_flux(wavelength_m: float, power_w: float = PROBE_POWER_W) -> float:
    """Probe-beam photon flux Phi = P / (hbar omega) = P lambda / (hbar 2 pi c) [Hz].

    The shot-noise resource for the polarimetric read-out. Built from HBAR and
    C_0 (ave.core.constants); no hardcoded h/c.
    """
    omega = 2.0 * np.pi * C_0 / wavelength_m
    return float(power_w / (HBAR * omega))


def ellipticity_signal_rate(psi: float, wavelength_m: float) -> float:
    """Effective shot-noise SIGNAL rate [Hz] for the ave.bench.snr time-to-Nsigma.

    Shot-noise-limited polarimetry has SNR = psi * sqrt(Phi * t); writing it in
    the ave.bench.snr contract SNR ~ sqrt(signal * t) (signal >> floor branch)
    gives signal_rate = psi^2 * Phi. time_to_n_sigma(signal_rate, floor~0) then
    returns the physical t = (Nsigma)^2 / (psi^2 Phi).
    """
    return float(psi**2 * probe_photon_flux(wavelength_m))


# ============================================================================
# VALIDATE-ON-KNOWN (HALT on fail)
# ============================================================================
def _validate_on_known() -> dict:
    """Run the validate-on-known gates; HALT (sys.exit 1) on any failure."""
    A_e = vacuum_magnetic_birefringence_constant()
    A_e_target = 1.32e-24  # PVLAS/Rizzo textbook value [T^-2] (LABELED literature)
    A_e_relerr = abs(A_e - A_e_target) / A_e_target
    identity_ok = substrate_identity_holds()
    A_e_ok = A_e_relerr < 0.01
    gates = {
        "substrate_identity_(Ecrit/Eyield)^2==1/alpha_and_cBcrit==Ecrit": identity_ok,
        "PVLAS_A_e_recovers_1.32e-24_Tinv2": A_e_ok,
        "A_e_value": A_e,
        "A_e_target": A_e_target,
        "A_e_relerr": A_e_relerr,
    }
    if not (identity_ok and A_e_ok):
        print("HALT: validate-on-known FAILED — model does not recover a known.")
        print(f"  substrate identity: {identity_ok}")
        print(f"  A_e = {A_e:.6e} vs target {A_e_target:.3e} (relerr {A_e_relerr:.3e})")
        sys.exit(1)
    return gates


# ============================================================================
# THE FACILITY-SCALE SWEEP GRID (the 5-D design space)
# ============================================================================
# E: lab-magnet-equivalent -> ELI-extreme laser focus. A = E/E_YIELD << 1
# everywhere (deep-linear; the ratified LINEAR-pump regime).
E_GRID = np.logspace(9.0, np.log10(3.0e16), 18)  # 1e9 -> 3e16 V/m
# Fabry-Perot probe-cavity finesse (PVLAS/BMV lineage).
FINESSE_GRID = np.array([1.0e2, 1.0e3, 1.0e4, 1.0e5])
# Probe wavelength: doubled Nd:YAG, Ti:Sa, Nd:YAG fundamental.
LAMBDA_GRID = np.array([532.0e-9, 800.0e-9, 1064.0e-9])
# Interaction / cavity length: overlap-limited mm -> cm.
LENGTH_GRID = np.array([1.0e-3, 1.0e-2])
# Geometry coupling g. UPDATED (OQ-1, oq1_field_to_cavity_phase_coupling.py): the
# PINNED per-config g_eff from the derived Gaussian-focus x cavity-timing chain
# replaces the first-cut DERIVE-1 bound. The two distinct derived operating
# points are: g_eff ~ 0.25 (full coherent finesse build-up: CW pump high-F, or a
# ns-gated pulsed cavity) and g_eff ~ 3.9e-4 (single-pass / fs-gated cavity:
# g_spatial only, NO finesse recovery — the fs pump is gone before the
# recirculating probe returns). We keep the worst-credible 1e-5 / 1e-8 tail so
# the divergence-window g-floor is still mapped. (See OQ-1 §3; g_eff is
# APPARATUS-INPUT-derived, consistency-class, OUTSIDE the AVE constants gate.)
G_GRID = np.array([2.51e-1, 3.95e-4, 1.0e-5, 1.0e-8])


@dataclass(frozen=True)
class SweepPoint:
    """A single co-computed (AVE, QED) facility-sweep point.

    Both psi_ave and psi_qed are produced by the IDENTICAL induced_ellipticity
    machinery (same g, F, L, lambda); only the index-shift coefficient differs
    (the no-strawman R1 invariant). 'in_window' is True iff psi_ave clears the
    polarimetry floor AND is measurably above its co-computed QED counterpart
    AND the small-angle linearization is still valid.
    """

    E: float
    A: float
    finesse: float
    wavelength_m: float
    length_m: float
    g: float
    dn_ave: float
    dn_qed: float
    psi_ave: float
    psi_qed: float
    psi_ratio: float
    small_angle_valid: bool
    above_floor_optimistic: bool
    above_floor_realistic: bool
    t_5sigma_s: float
    in_window: bool


def _sweep_point(
    E: float, finesse: float, wavelength_m: float, length_m: float, g: float,
    *, psi_floor: float = PSI_FLOOR_REALISTIC,
) -> SweepPoint:
    """Co-compute the AVE and QED legs at one facility point THROUGH THE SAME
    machinery (the no-strawman R1 contract).

    The QED delta_n is the REAL Euler-Heisenberg literature curve
    (a_EH alpha^2 (E/E_CRIT)^2), driven through the EXACT same
    induced_ellipticity(g, F, L, lambda) the AVE delta_n is — never a pre-baked
    SM array. Divergence is purely the index-shift coefficient.
    """
    dn_ave = float(delta_n_ave_exact(E))
    dn_qed = float(delta_n_qed(E, A_EH_REF))
    psi_ave = induced_ellipticity(
        dn_ave, g=g, finesse=finesse, length_m=length_m, wavelength_m=wavelength_m
    )
    psi_qed = induced_ellipticity(
        dn_qed, g=g, finesse=finesse, length_m=length_m, wavelength_m=wavelength_m
    )
    psi_ratio = (psi_ave / psi_qed) if psi_qed > 0 else float("inf")
    small_angle = psi_ave < SMALL_ANGLE_CEILING
    above_opt = psi_ave >= PSI_FLOOR_OPTIMISTIC
    above_real = psi_ave >= PSI_FLOOR_REALISTIC
    # time-to-Nsigma uses the shot-noise signal rate from psi (floor ~ 0; the
    # additive detector floor is folded into psi_floor as the static margin).
    sig_rate = ellipticity_signal_rate(psi_ave, wavelength_m)
    t_5sigma = time_to_n_sigma(sig_rate, 0.0, SIGMA_TARGET)
    # The DIVERGENCE WINDOW membership test: signal clears the (chosen) floor
    # AND is measurably above QED AND the small-angle mapping still holds.
    above_chosen = psi_ave >= psi_floor
    above_qed = psi_ratio > 1.0
    in_window = bool(above_chosen and above_qed and small_angle)
    return SweepPoint(
        E=float(E), A=float(E / E_YIELD), finesse=float(finesse),
        wavelength_m=float(wavelength_m), length_m=float(length_m), g=float(g),
        dn_ave=dn_ave, dn_qed=dn_qed, psi_ave=float(psi_ave), psi_qed=float(psi_qed),
        psi_ratio=float(psi_ratio), small_angle_valid=bool(small_angle),
        above_floor_optimistic=bool(above_opt), above_floor_realistic=bool(above_real),
        t_5sigma_s=float(t_5sigma), in_window=in_window,
    )


def run_full_sweep(psi_floor: float = PSI_FLOOR_REALISTIC) -> list[SweepPoint]:
    """Drive the full 5-D E x F x lambda x L x g grid, co-computing AVE+QED at
    every point through the shared machinery."""
    pts: list[SweepPoint] = []
    for E in E_GRID:
        for F in FINESSE_GRID:
            for lam in LAMBDA_GRID:
                for L in LENGTH_GRID:
                    for g in G_GRID:
                        pts.append(_sweep_point(E, F, lam, L, g, psi_floor=psi_floor))
    return pts


# ============================================================================
# DIVERGENCE-WINDOW EXTRACTION (computed from the swept data, not templated)
# ============================================================================
def extract_window(points: list[SweepPoint]) -> dict:
    """Extract the DIVERGENCE WINDOW: the E x F x g region where psi_AVE clears
    the polarimetry floor AND is measurably > QED AND small-angle holds.

    Every number returned is COMPUTED from the swept points (ave-driver-script-
    honesty: no templated bounds). The psi_ratio is the field-independent
    coefficient gap (~4.14e6); the window edges are set by the absolute-signal
    -vs-floor and small-angle constraints, which DO depend on (E, F, g).
    """
    in_win = [p for p in points if p.in_window]
    out: dict = {
        "n_points_total": len(points),
        "n_points_in_window": len(in_win),
        "psi_floor_used_rad": PSI_FLOOR_REALISTIC,
        "psi_floor_optimistic_rad": PSI_FLOOR_OPTIMISTIC,
        "small_angle_ceiling_rad": SMALL_ANGLE_CEILING,
    }
    if not in_win:
        out["window"] = None
        return out

    Es = np.array([p.E for p in in_win])
    Fs = np.array([p.finesse for p in in_win])
    gs = np.array([p.g for p in in_win])
    ratios = np.array([p.psi_ratio for p in in_win])
    psis = np.array([p.psi_ave for p in in_win])
    ts = np.array([p.t_5sigma_s for p in in_win])

    out["window"] = {
        "E_Vm": {"min": float(Es.min()), "max": float(Es.max())},
        "A_saturation": {"min": float(Es.min() / E_YIELD), "max": float(Es.max() / E_YIELD)},
        "finesse": {"min": float(Fs.min()), "max": float(Fs.max())},
        "g": {"min": float(gs.min()), "max": float(gs.max())},
        "psi_ave_rad": {"min": float(psis.min()), "max": float(psis.max())},
        "psi_ratio_ave_over_qed": {
            "min": float(ratios.min()),
            "max": float(ratios.max()),
            "median": float(np.median(ratios)),
        },
        "t_5sigma_s": {"min": float(ts.min()), "max": float(ts.max())},
    }
    # The field-independent coefficient ratio (the headline ECHO-tagged number,
    # g-independent — surfaced separately from the absolute-signal window).
    out["coefficient_ratio_field_independent"] = {
        "a_eh_7_45": coefficient_ratio(7.0 / 45.0),
        "a_eh_3_45_differential": coefficient_ratio(3.0 / 45.0),
        "a_eh_4_45_perp": coefficient_ratio(4.0 / 45.0),
    }
    # Physical single-mode band (DERIVE-2): exclude the 1.45 units artifact.
    physical_band = {
        k: coefficient_ratio(v)
        for k, v in A_EH_LITERATURE.items()
        if "PVLAS A_e" not in k
    }
    out["coefficient_ratio_physical_band"] = {
        "min": float(min(physical_band.values())),
        "max": float(max(physical_band.values())),
        "by_mode": physical_band,
    }
    out["coefficient_ratio_artifact_excluded"] = {
        "PVLAS A_e differential (~1.45)": coefficient_ratio(
            A_EH_LITERATURE["PVLAS A_e differential (~1.45)"]
        ),
        "note": "1/(2 pi alpha)=21.81 units artifact (DERIVE-2 flag-don't-fix); "
        "NOT a physical EH coefficient; excluded from the physical band.",
    }
    # The g-floor: the smallest g in the window at the best (E, F). The grid now
    # carries the OQ-1 PINNED g_eff points (0.251 full-finesse, 3.95e-4
    # single-pass/fs-gated) plus the worst-credible 1e-5/1e-8 tail.
    out["g_floor_in_window"] = float(gs.min())
    out["g_includes_pinned_single_pass_3.95e-4"] = bool(np.any(np.isclose(gs, 3.95e-4)))
    out["g_includes_pinned_full_finesse_0.251"] = bool(np.any(np.isclose(gs, 2.51e-1)))
    # Fastest 5-sigma in the window (the headline integration-time number).
    fastest = min(in_win, key=lambda p: p.t_5sigma_s)
    out["fastest_5sigma"] = {
        "E_Vm": fastest.E, "finesse": fastest.finesse, "g": fastest.g,
        "wavelength_m": fastest.wavelength_m, "length_m": fastest.length_m,
        "psi_ave_rad": fastest.psi_ave, "t_5sigma_s": fastest.t_5sigma_s,
        "psi_ratio": fastest.psi_ratio,
    }
    return out


# ============================================================================
# FIGURES (through ave.viz.style.apply(); no baked titles; legend outside;
# captions COMPUTED from the data, returned for the LaTeX \caption{})
# ============================================================================
def _fig_signal_vs_field(points: list[SweepPoint], out_stub: Path) -> tuple[list[Path], str]:
    """Panel: psi_AVE vs psi_QED across E at the sweet-spot g, with the two
    polarimetry floors. Both legs ride the SAME machinery (R1)."""
    # Slice the sweep at the headline geometry: the OQ-1 PINNED single-pass
    # g_eff=3.95e-4, F=1e3, 1064 nm, cm cavity — co-computed AVE and QED on the
    # identical grid.
    g0, F0, lam0, L0 = 3.95e-4, 1.0e3, 1064.0e-9, 1.0e-2
    sl = sorted(
        (p for p in points
         if np.isclose(p.g, g0) and np.isclose(p.finesse, F0)
         and np.isclose(p.wavelength_m, lam0) and np.isclose(p.length_m, L0)),
        key=lambda p: p.E,
    )
    E = np.array([p.E for p in sl])
    psi_a = np.array([p.psi_ave for p in sl])
    psi_q = np.array([p.psi_qed for p in sl])
    ratio_med = float(np.median(psi_a / np.maximum(psi_q, 1e-300)))

    fig, ax = plt.subplots(figsize=style.figsize("single"))
    ax.loglog(E, psi_a, color=style.COLORS["ave"], lw=2.0, marker="o", ms=3,
              label=r"AVE  $\psi$ (sqrt-$S$ kernel)")
    ax.loglog(E, psi_q, color=style.COLORS["comparison"], lw=2.0, ls="--", marker="s",
              ms=3, label=r"QED  $\psi$ (Euler-Heisenberg)")
    ax.axhline(PSI_FLOOR_OPTIMISTIC, color=style.COLORS["muted"], ls=":", lw=1.3,
               label=r"floor (optimistic)")
    ax.axhline(PSI_FLOOR_REALISTIC, color=style.COLORS["accent"], ls="-.", lw=1.3,
               label=r"floor (realistic)")
    ax.set_xlabel(style.axis_label("Peak field", "E", "V/m"))
    ax.set_ylabel(style.axis_label("Ellipticity", r"\psi", "rad"))
    style.legend(ax, where="right", fontsize=8)
    written = style.save(fig, out_stub, strict=True)
    plt.close(fig)
    caption = (
        f"Realized polarimeter ellipticity vs peak field at the sweet-spot "
        f"geometry (g={g0:.1e}, F={F0:.0e}, lambda={lam0*1e9:.0f} nm, "
        f"L={L0*1e2:.0f} cm). AVE and QED are co-computed through the IDENTICAL "
        f"induced_ellipticity machinery (no-strawman R1); the legs differ ONLY in "
        f"the index-shift coefficient. AVE sits a field-independent factor "
        f"{ratio_med:.2e} above QED across the swept field range. "
        f"Both polarimetry floors (optimistic {PSI_FLOOR_OPTIMISTIC:.0e} rad, "
        f"realistic {PSI_FLOOR_REALISTIC:.0e} rad) shown."
    )
    return written, caption


def _fig_window_E_vs_g(points: list[SweepPoint], out_stub: Path) -> tuple[list[Path], str]:
    """Panel: the DIVERGENCE WINDOW in (E, g) at fixed F=1e3, 1064 nm, cm —
    coloured by whether psi_AVE is in-window (clears floor AND > QED AND
    small-angle)."""
    F0, lam0, L0 = 1.0e3, 1064.0e-9, 1.0e-2
    sl = [p for p in points
          if np.isclose(p.finesse, F0) and np.isclose(p.wavelength_m, lam0)
          and np.isclose(p.length_m, L0)]
    Es = sorted({p.E for p in sl})
    gs = sorted({p.g for p in sl})
    Z = np.full((len(gs), len(Es)), np.nan)
    for p in sl:
        i = gs.index(p.g)
        j = Es.index(p.E)
        Z[i, j] = np.log10(max(p.psi_ratio, 1e-300)) if p.in_window else np.nan
    n_win = int(np.count_nonzero(~np.isnan(Z)))

    fig, ax = plt.subplots(figsize=style.figsize("square"))
    im = ax.pcolormesh(
        np.log10(Es), np.log10(gs), Z, cmap=style.CMAP_SEQ, shading="nearest"
    )
    ax.set_xlabel(style.axis_label(r"$\log_{10}$ peak field", r"\log_{10} E", "V/m"))
    ax.set_ylabel(style.axis_label(r"$\log_{10}$ geometry coupling", r"\log_{10} g", "dimensionless"))
    cb = fig.colorbar(im, ax=ax)
    cb.set_label(style.axis_label(r"$\log_{10}$ AVE/QED ellipticity ratio",
                                  r"\log_{10}(\psi_{AVE}/\psi_{QED})", "dimensionless"))
    written = style.save(fig, out_stub, strict=True)
    plt.close(fig)
    caption = (
        f"Divergence window in the (peak field, geometry coupling g) plane at "
        f"F={F0:.0e}, lambda={lam0*1e9:.0f} nm, L={L0*1e2:.0f} cm. Coloured cells "
        f"are IN-WINDOW: psi_AVE clears the realistic polarimetry floor "
        f"({PSI_FLOOR_REALISTIC:.0e} rad), exceeds its co-computed QED counterpart, "
        f"and stays inside the small-angle linearization (<{SMALL_ANGLE_CEILING} rad). "
        f"{n_win} of {len(Es)*len(gs)} (E, g) cells at this slice are in-window; the "
        f"window spans the OQ-1 PINNED g_eff points (3.95e-4 single-pass, 0.251 "
        f"full-finesse) and the worst-credible 1e-5/1e-8 tail. Cell colour is the "
        f"field-independent AVE/QED ratio (uniform across the window — g cancels in "
        f"the ratio)."
    )
    return written, caption


def _fig_time_to_5sigma(points: list[SweepPoint], out_stub: Path) -> tuple[list[Path], str]:
    """Panel: time-to-5sigma vs field across the four g tiers, at F=1e3, 1064 nm,
    cm — the integration-time map over the geometry-coupling lever."""
    F0, lam0, L0 = 1.0e3, 1064.0e-9, 1.0e-2
    fig, ax = plt.subplots(figsize=style.figsize("single"))
    cyc = [style.COLORS["ave"], style.COLORS["accent"], style.COLORS["comparison"],
           style.COLORS["muted"]]
    g_vals = sorted({p.g for p in points}, reverse=True)
    plotted_floor = False
    for k, g0 in enumerate(g_vals):
        sl = sorted(
            (p for p in points
             if np.isclose(p.g, g0) and np.isclose(p.finesse, F0)
             and np.isclose(p.wavelength_m, lam0) and np.isclose(p.length_m, L0)),
            key=lambda p: p.E,
        )
        E = np.array([p.E for p in sl])
        t = np.array([p.t_5sigma_s for p in sl])
        finite = np.isfinite(t) & (t > 0)
        ax.loglog(E[finite], t[finite], lw=1.8, marker="o", ms=3,
                  color=cyc[k % len(cyc)], label=f"g = {g0:.1e}")
        plotted_floor = True
    if plotted_floor:
        ax.axhline(1.0, color=style.COLORS["data"], ls=":", lw=1.2, label="1 s")
    ax.set_xlabel(style.axis_label("Peak field", "E", "V/m"))
    ax.set_ylabel(style.axis_label(r"Time to 5$\sigma$", "t", "s"))
    style.legend(ax, where="right", fontsize=8)
    written = style.save(fig, out_stub, strict=True)
    plt.close(fig)
    # Computed headline: fastest finite t across the plotted slices.
    cand = [p for p in points
            if np.isclose(p.finesse, F0) and np.isclose(p.wavelength_m, lam0)
            and np.isclose(p.length_m, L0) and np.isfinite(p.t_5sigma_s)
            and p.t_5sigma_s > 0]
    fastest = min(cand, key=lambda p: p.t_5sigma_s)
    caption = (
        f"Shot-noise-limited time to 5-sigma AVE detection vs peak field, across "
        f"the geometry-coupling tiers g in [{min(g_vals):.0e}, {max(g_vals):.0e}] "
        f"(F={F0:.0e}, lambda={lam0*1e9:.0f} nm, L={L0*1e2:.0f} cm, "
        f"{PROBE_POWER_W:.0f} W probe). The fastest in-grid detection is "
        f"{fastest.t_5sigma_s:.2e} s at E={fastest.E:.1e} V/m, g={fastest.g:.1e}. "
        f"g sets the absolute signal (and hence integration time); it does NOT "
        f"change the AVE/QED coefficient ratio."
    )
    return written, caption


def _make_figures(points: list[SweepPoint], out_dir: Path) -> dict:
    """Produce the three figures through the house style; return their paths +
    computed captions."""
    style.apply()  # print profile (white bg), house palette, no baked titles
    figs: dict = {}
    for name, fn in (
        ("signal_vs_field", _fig_signal_vs_field),
        ("window_E_vs_g", _fig_window_E_vs_g),
        ("time_to_5sigma", _fig_time_to_5sigma),
    ):
        stub = out_dir / f"vacuum_birefringence_facility_sweep_{name}"
        written, caption = fn(points, stub)
        figs[name] = {"paths": [str(p) for p in written], "caption": caption}
    return figs


def main() -> None:
    out: dict = {}
    print("=" * 78)
    print("VACUUM-BIREFRINGENCE FACILITY SWEEP — AVE vs QED (hardened, no-strawman)")
    print("=" * 78)

    # ---- (0) VALIDATE-ON-KNOWN (HALT on fail) -------------------------------
    gates = _validate_on_known()
    out["validate_on_known"] = gates
    print("\n[0] VALIDATE-ON-KNOWN (HALT if fail):")
    print(f"    substrate identity (E_crit/E_yield)^2==1/a, c*B_crit==E_crit: "
          f"{gates['substrate_identity_(Ecrit/Eyield)^2==1/alpha_and_cBcrit==Ecrit']}")
    print(f"    PVLAS A_e = {gates['A_e_value']:.4e} T^-2 vs textbook "
          f"{gates['A_e_target']:.3e} (relerr {gates['A_e_relerr']:.2e}) -> PASS")
    print(f"    anchors: E_YIELD={E_YIELD:.4e} V/m  E_CRIT={E_CRIT:.4e} V/m  "
          f"1/alpha={1.0/ALPHA:.4f}")

    # ---- (1) FULL 5-D SWEEP -------------------------------------------------
    print("\n[1] FULL 5-D SWEEP (E x finesse x lambda x L x g), co-computing QED "
          "through the SAME machinery (no-strawman R1):")
    points = run_full_sweep()
    out["grid"] = {
        "E_Vm": E_GRID.tolist(), "finesse": FINESSE_GRID.tolist(),
        "lambda_m": LAMBDA_GRID.tolist(), "length_m": LENGTH_GRID.tolist(),
        "g": G_GRID.tolist(), "n_points": len(points),
    }
    print(f"    swept {len(points)} points "
          f"({len(E_GRID)} E x {len(FINESSE_GRID)} F x {len(LAMBDA_GRID)} lambda "
          f"x {len(LENGTH_GRID)} L x {len(G_GRID)} g)")

    # ---- (2) DIVERGENCE WINDOW ----------------------------------------------
    win = extract_window(points)
    out["divergence_window"] = win
    print("\n[2] DIVERGENCE WINDOW (psi_AVE clears floor AND > QED AND small-angle):")
    print(f"    {win['n_points_in_window']} of {win['n_points_total']} swept points in-window")
    if win["window"] is not None:
        w = win["window"]
        cr = win["coefficient_ratio_field_independent"]
        pb = win["coefficient_ratio_physical_band"]
        print(f"    E window  : [{w['E_Vm']['min']:.2e}, {w['E_Vm']['max']:.2e}] V/m  "
              f"(A=[{w['A_saturation']['min']:.2e}, {w['A_saturation']['max']:.2e}], deep-linear)")
        print(f"    finesse   : [{w['finesse']['min']:.0e}, {w['finesse']['max']:.0e}]")
        print(f"    g         : [{w['g']['min']:.0e}, {w['g']['max']:.0e}]  "
              f"(PINNED g_eff: single-pass 3.95e-4={win['g_includes_pinned_single_pass_3.95e-4']}, "
              f"full-finesse 0.251={win['g_includes_pinned_full_finesse_0.251']})")
        print(f"    psi_AVE   : [{w['psi_ave_rad']['min']:.2e}, {w['psi_ave_rad']['max']:.2e}] rad")
        print(f"    AVE/QED   : ratio [{w['psi_ratio_ave_over_qed']['min']:.3e}, "
              f"{w['psi_ratio_ave_over_qed']['max']:.3e}] "
              f"(median {w['psi_ratio_ave_over_qed']['median']:.3e})")
        print(f"    t_5sigma  : [{w['t_5sigma_s']['min']:.2e}, {w['t_5sigma_s']['max']:.2e}] s")
        print(f"    COEFFICIENT RATIO (field-INDEPENDENT, g-independent, ECHO-tagged):")
        print(f"      a_EH=7/45  -> {cr['a_eh_7_45']:.3e}   a_EH=3/45 -> "
              f"{cr['a_eh_3_45_differential']:.3e}")
        print(f"      physical single-mode band: [{pb['min']:.3e}, {pb['max']:.3e}]")
        print(f"      (excluded artifact 'PVLAS A_e ~1.45' = "
              f"{win['coefficient_ratio_artifact_excluded']['PVLAS A_e differential (~1.45)']:.3e}, "
              f"a 1/(2 pi alpha) units artifact — DERIVE-2 flag)")
        f5 = win["fastest_5sigma"]
        print(f"    FASTEST 5sigma in-window: {f5['t_5sigma_s']:.2e} s at E={f5['E_Vm']:.1e} V/m, "
              f"F={f5['finesse']:.0e}, g={f5['g']:.1e}")
    else:
        print("    NO points in-window (no E x F x g clears the floor above QED).")

    # ---- (3) FIGURES --------------------------------------------------------
    out_dir = Path(__file__).resolve().parent / "_output"
    out_dir.mkdir(exist_ok=True)
    print("\n[3] FIGURES (house style, no baked titles, legend outside, computed captions):")
    figs = _make_figures(points, out_dir)
    out["figures"] = figs
    for name, info in figs.items():
        for p in info["paths"]:
            print(f"    wrote {p}")

    # ---- (4) WRITE JSON -----------------------------------------------------
    # Drop the full per-point list into JSON for downstream reuse (compact).
    out["points"] = [
        {
            "E": p.E, "A": p.A, "finesse": p.finesse, "wavelength_m": p.wavelength_m,
            "length_m": p.length_m, "g": p.g, "dn_ave": p.dn_ave, "dn_qed": p.dn_qed,
            "psi_ave": p.psi_ave, "psi_qed": p.psi_qed, "psi_ratio": p.psi_ratio,
            "small_angle_valid": p.small_angle_valid, "in_window": p.in_window,
            "t_5sigma_s": p.t_5sigma_s,
        }
        for p in points
    ]
    out_path = out_dir / "vacuum_birefringence_facility_sweep.json"
    out_path.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nResults written: {out_path}")
    print("=" * 78)


if __name__ == "__main__":
    main()
