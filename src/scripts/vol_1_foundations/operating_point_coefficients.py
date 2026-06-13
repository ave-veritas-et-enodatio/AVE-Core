#!/usr/bin/env python3
"""
Operating-point coefficient scout — electron datasheet column (consistency-class).

Forward-computes the saturation-kernel derivatives and reactive parameters at the
electron operating point (A² ≈ 0.23 from swept-gamma characterization) without
fitting or retrofitting. The falsifiable AVE-distinct column: dc/dA, dα/dT, dε/dE
starts here with the sub-yield varactor/inductor slopes at the imposed amplitude.

Discipline: ave-canonical-source (constants imported); consistency-vs-emergence
(all outputs are consistency-class — α enters only as the canonical loss calibration).

Outputs: assets/sim_outputs/operating_point_coefficients.json
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from ave.core.constants import (
    ALPHA,
    C_0,
    EPSILON_0,
    MU_0,
    R_I,
    R_II,
    R_III,
    V_SNAP,
    V_YIELD,
    Z_0,
)

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"

# Electron operating point from swept-gamma characterization (m_ec²-calibrated impose)
A2_ELECTRON_OP = 0.23
A_ELECTRON_OP = math.sqrt(A2_ELECTRON_OP)


def s_kernel(a2: float) -> float:
    """S(A) = √(1 − A²), A² normalized to A_yield."""
    return math.sqrt(max(1.0 - a2, 1e-15))


def ds_da2(a2: float) -> float:
    """∂S/∂A² = −1/(2S) for S = √(1−A²)."""
    s = s_kernel(a2)
    return -0.5 / s


def c_eff_over_c0(a2: float) -> float:
    """Metric varactor: C_eff/C₀ = 1/S."""
    return 1.0 / s_kernel(a2)


def dc_eff_da(a2: float) -> float:
    """d(C_eff/C₀)/dA with A² as the control parameter."""
    s = s_kernel(a2)
    # C_eff/C₀ = (1-A²)^(-1/2) => d/dA = A / (1-A²)^(3/2) = A / S³
    return A_ELECTRON_OP / (s**3)


def l_eff_over_l0(i_norm: float) -> float:
    """Relativistic inductor: L_eff/L₀ = 1/S, I normalized like A."""
    return 1.0 / s_kernel(i_norm**2)


def q_at_loss(gamma_over_omega: float) -> float:
    """Tank Q = ω/γ."""
    return 1.0 / gamma_over_omega


def main() -> None:
    a2 = A2_ELECTRON_OP
    s = s_kernel(a2)
    a = A_ELECTRON_OP

    # Loss calibration: Q = 1/α at ω_C (theorem-3-1; swept-gamma structural result)
    gamma_over_omega = ALPHA
    q_loss_calibrated = q_at_loss(gamma_over_omega)

    # Toy bounded locus from swept-gamma (α-encoded via loss, not geometry)
    a2_self_bounded = 8.0 * ALPHA  # A²_self ≈ 8α at Q=1/α

    # Regime ladder (R_I = √(2α), etc.)
    if a >= R_III:
        regime = "IV"
    elif a >= R_II:
        regime = "III"
    elif a >= R_I:
        regime = "II"
    else:
        regime = "I"

    # Varactor slope at OP (normalized units)
    c_ratio = c_eff_over_c0(a2)
    dc_da = dc_eff_da(a2)

    # Physical voltage at OP
    v_op = a * V_YIELD
    v_over_vsnap = v_op / V_SNAP

    # Small-signal ε_eff slope: ε_eff = ε₀ S => dε/dE ~ (dS/dA)(dA/dV) at fixed normalization
    deps_de_fractional = ds_da2(a2) * 2.0 * a  # dS/dA = 2A·dS/dA²

    results = {
        "class": "consistency-class scout — not a forward prediction doc",
        "electron_operating_point": {
            "A2": a2,
            "A": a,
            "S": s,
            "regime": regime,
            "R_I": R_I,
            "R_II": R_II,
            "R_III": R_III,
            "V_op_V": v_op,
            "V_op_over_V_yield": a,
            "V_op_over_V_snap": v_over_vsnap,
        },
        "reactive_calibration": {
            "Q_at_alpha_loss": q_loss_calibrated,
            "alpha": ALPHA,
            "Q_inverse_equals_alpha": abs(q_loss_calibrated * ALPHA - 1.0) < 1e-9,
            "A2_self_bounded_toy_loss": a2_self_bounded,
            "A2_op_over_A2_self": a2 / a2_self_bounded,
        },
        "varactor_coefficients": {
            "C_eff_over_C0": c_ratio,
            "d_Ceff_ratio_dA": dc_da,
            "dS_dA2": ds_da2(a2),
            "fractional_deps_dE_proxy": deps_de_fractional,
        },
        "impedance": {
            "Z_EM_ohm": Z_0,
            "Z_eff_EM_over_Z0_sym": 1.0,
        },
        "notes": [
            "A2≈0.23 is the m_ec²-calibrated impose from swept-gamma characterization.",
            "Q=1/α uses α as loss calibration (consistency-class), not emergence.",
            "dε/dE proxy uses ∂S/∂A at fixed A≡V/V_yield normalization.",
            "Full dark-wake τ_zx loss feed is the genuine emergence gate (not computed here).",
        ],
    }

    OUT.mkdir(parents=True, exist_ok=True)
    out_path = OUT / "operating_point_coefficients.json"
    out_path.write_text(json.dumps(results, indent=2) + "\n")

    print("=" * 72)
    print("OPERATING-POINT COEFFICIENT SCOUT")
    print("=" * 72)
    print(f"  A² = {a2:.4f}  S = {s:.6f}  regime = {regime}")
    print(f"  C_eff/C₀ = {c_ratio:.6f}  d(C_eff/C₀)/dA = {dc_da:.6f}")
    print(f"  Q (α-loss) = {q_loss_calibrated:.2f}  1/Q = {ALPHA:.6e}")
    print(f"  A²_op / A²_self(toy) = {a2 / a2_self_bounded:.2f}")
    print(f"  V_op = {v_op/1e3:.2f} kV  ({100*a:.1f}% of V_yield)")
    print(f"  Wrote {out_path}")
    print("=" * 72)


if __name__ == "__main__":
    main()
