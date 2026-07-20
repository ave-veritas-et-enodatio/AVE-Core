#!/usr/bin/env python3
"""Scalar-GW bulk-channel far-field estimator (research/scalar-gw-port lane).

Reproducible arithmetic for the derivation
    research/2026-07-20_scalar-gw-bulk-channel_derivation.md

This driver evaluates FORMS derived analytically in that doc from [canon]
inputs; every dimensionful VALUE it prints is CODATA/astro-imported and tagged
in the JSON `provenance` field (consistency-vs-emergence: consistency-class, NOT
emergence). It mints no canon and computes no new physics primitive.

What it computes
----------------
1. The robust, calibration-free SPEED-suppression factors of the bulk/scalar
   channel radiated power relative to the shear/tensor (observed-GW) channel,
   for the two candidate longitudinal speeds the corpus distinguishes:
     * c_bulk = sqrt(2)   c  (A1-scalar bulk-modulus PORT mode; constants.py V_LONG)
     * c_P    = sqrt(10/3) c (isotropic-solid P-wave; constants.py:778, canon)
   Radiated power of a quadrupole source scales as 1/c_channel^5 for a fixed
   source moment => power ratio lower bound = (c_shear/c_channel)^5.
2. The corresponding amplitude-ratio scalings (sqrt of power ratio), which under
   an EQUAL-coupling assumption bracket h_scalar/h_tensor from the speed factor
   ALONE (the O(1) coupling x tensor-structure factor is the FLAGGED unforced
   quantity and is NOT asserted here).
3. The superluminal-precursor lead time for a fiducial GW170817-class source
   (imported luminosity distance), the "sqrt(2)c coexistence" causality note.

Nothing here decides the fork (does the A1/bulk channel have an independent
far-field radiative port?). It only quantifies the CONDITIONAL consequences.
"""
from __future__ import annotations

import json
import math
import os
import sys

# Import the canonical speed of light from the engine constants (ave-canonical-source).
# No hard-coded fallback: c MUST come from constants.py (anti-cheat DAG rule).
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))
from ave.core.constants import C_0  # noqa: E402

# ---------------------------------------------------------------------------
# Channel speed ratios (DERIVED forms from K = 2G magic angle; dimensionless).
# ---------------------------------------------------------------------------
R_BULK_PORT = math.sqrt(2.0)          # c_bulk / c_shear  (A1-scalar port mode, V_LONG)
R_PWAVE = math.sqrt(10.0 / 3.0)       # c_P    / c_shear  (isotropic-solid P-wave)

# Quadrupole radiated-power speed suppression = (c_shear/c_channel)^5 (fixed source moment).
POW_SUPPRESS_BULK_PORT = R_BULK_PORT ** (-5)
POW_SUPPRESS_PWAVE = R_PWAVE ** (-5)

# Amplitude-ratio scaling from the speed factor alone (equal-coupling bracket).
AMP_SCALE_BULK_PORT = math.sqrt(POW_SUPPRESS_BULK_PORT)   # = R^(-5/2)
AMP_SCALE_PWAVE = math.sqrt(POW_SUPPRESS_PWAVE)

# ---------------------------------------------------------------------------
# Superluminal precursor lead time for a fiducial GW170817-class source.
# Travel time at speed v over distance D is D/v; the (faster) scalar channel
# arrives earlier by dt = D/c_shear - D/c_channel = (D/c)(1 - c/c_channel).
# ---------------------------------------------------------------------------
MPC_M = 3.085_677_581e22               # metres per Mpc (IAU-derived, imported)
YR_S = 3.155_695_2e7                   # seconds per Julian year (imported)
D_GW170817_MPC = 40.0                  # luminosity distance, Abbott+ 2017 (imported ~40 Mpc)

D_m = D_GW170817_MPC * MPC_M
t_tensor_s = D_m / C_0                  # tensor/EM travel time
lead_bulk_s = (D_m / C_0) * (1.0 - 1.0 / R_BULK_PORT)
lead_pwave_s = (D_m / C_0) * (1.0 - 1.0 / R_PWAVE)

# ---------------------------------------------------------------------------
# Fiducial observed tensor strains (imported catalogue values), and the scalar
# admixture the equal-coupling speed-factor bracket would imply (FORM only; the
# O(1) coupling is flagged, so this is a bracket, not a prediction).
# ---------------------------------------------------------------------------
H_TENSOR = {"GW150914": 1.0e-21, "GW170817": 1.0e-22}   # imported, order-of-magnitude
scalar_admixture_bracket = {
    ev: {
        "h_tensor_imported": h,
        "h_scalar_bulk_port_equal_coupling": h * AMP_SCALE_BULK_PORT,
        "h_scalar_pwave_equal_coupling": h * AMP_SCALE_PWAVE,
    }
    for ev, h in H_TENSOR.items()
}

results = {
    "provenance": {
        "class": "consistency (FORMS derived; VALUES CODATA/astro-imported)",
        "canonical_c_source": "ave.core.constants.C_0",
        "imported_values": [
            "D_GW170817 ~= 40 Mpc (Abbott+ 2017, GW170817 discovery)",
            "h_tensor ~ 1e-21 (GW150914), ~1e-22 (GW170817) (LIGO catalogue, OOM)",
            "Mpc, Julian-year unit conversions (IAU)",
        ],
        "speed_forms_derived_from": "K = 2G magic angle (GR-imported ratio; constants.py V_LONG, :778)",
    },
    "speed_ratios": {
        "c_bulk_port_over_c_shear_sqrt2": R_BULK_PORT,
        "c_pwave_over_c_shear_sqrt_10_3": R_PWAVE,
    },
    "power_suppression_speed_only": {
        "bulk_port_sqrt2__(c_s/c_b)^5": POW_SUPPRESS_BULK_PORT,
        "pwave_sqrt_10_3__(c_s/c_P)^5": POW_SUPPRESS_PWAVE,
        "note": "LOWER-bound suppression; O(1) coupling x tensor-structure factor NOT included (flagged, unforced).",
    },
    "amplitude_ratio_speed_only_equal_coupling": {
        "bulk_port_sqrt2": AMP_SCALE_BULK_PORT,
        "pwave_sqrt_10_3": AMP_SCALE_PWAVE,
        "note": "h_scalar/h_tensor from the SPEED factor alone under equal coupling; the true O(1) coupling is the FLAGGED fork.",
    },
    "superluminal_precursor_GW170817": {
        "distance_Mpc_imported": D_GW170817_MPC,
        "tensor_EM_travel_time_yr": t_tensor_s / YR_S,
        "bulk_port_sqrt2_lead_yr": lead_bulk_s / YR_S,
        "pwave_sqrt_10_3_lead_yr": lead_pwave_s / YR_S,
        "note": "Lead time by which a superluminal scalar burst outruns the tensor GW/EM front; ~10^7-10^8 yr => the sqrt(2)c coexistence causality/observability flag.",
    },
    "scalar_admixture_bracket_equal_coupling": scalar_admixture_bracket,
}

if __name__ == "__main__":
    print(json.dumps(results, indent=2))
    out = os.path.join(os.path.dirname(__file__), "scalar_gw_bulk_channel_results.json")
    with open(out, "w") as fh:
        json.dump(results, fh, indent=2)
    print(f"\n[written] {out}", file=sys.stderr)
