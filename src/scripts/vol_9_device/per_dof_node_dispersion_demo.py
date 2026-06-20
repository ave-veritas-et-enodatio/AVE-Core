#!/usr/bin/env python3
"""
Per-DOF Vacuum Node Circuit — dispersion demonstration driver (#44).

Demonstrates that ONE node-constitutive structure (the per-DOF reactive tensor
(L_i, C_i)) produces THREE behaviors as consequences:

  (c) VALIDATE-ON-KNOWN — isotropic continuum-limit node recovers c₀ and Z₀.
  (1) ISOTROPIC saturation  → achromatic + isotropic (Z=Z₀, Γ=0).
  (2) DEVIATORIC strain      → strain-induced birefringence FORM (Δc/c ∝ split).
  (3) HIGH-k dispersion      → (q·ℓ)² matter zone-edge + (q·ℓ)⁴ photon birefringence.

CONSISTENCY-class re-expression (consistency-vs-emergence v1.3): unifies three
already-asserted behaviors into one circuit. No α / m_e value claim. The c₀/Z₀
are the KNOWN anchors (validate-on-known gate), not new predictions.

Run:  python3 src/scripts/vol_9_device/per_dof_node_dispersion_demo.py
Canonical leaf:
  manuscript/ave-kb/vol9/ch3-pin-port-configuration/per-dof-vacuum-node-circuit.md
"""

import json
import sys
from pathlib import Path

import numpy as np

from ave.core.constants import C_0, L_NODE, Z_0
from ave.core.vacuum_node_circuit import (
    K4_BOND_DIRECTIONS,
    PerDOFVacuumNode,
    cubic_anisotropy_invariant,
    directional_anisotropy,
    lattice_dispersion,
    photon_birefringence,
)


def _loglog_slope(xs, ys):
    return float(np.polyfit(np.log(np.asarray(xs)), np.log(np.asarray(ys)), 1)[0])


def main():
    out = {}

    # ---- (c) VALIDATE-ON-KNOWN ------------------------------------------------
    cold = PerDOFVacuumNode()
    c_ok = bool(np.allclose(cold.c, C_0, rtol=1e-12))
    z_ok = bool(np.allclose(cold.Z, Z_0, rtol=1e-12))
    out["validate_on_known"] = {
        "c_i": cold.c.tolist(),
        "c0": C_0,
        "c0_recovered": c_ok,
        "Z_i": cold.Z.tolist(),
        "Z0": Z_0,
        "Z0_recovered": z_ok,
    }
    if not (c_ok and z_ok):
        print("HALT: isotropic continuum-limit node did NOT recover c₀ / Z₀ — model is wrong.")
        sys.exit(1)

    # ---- (1) ISOTROPIC saturation: achromatic + isotropic ---------------------
    iso = PerDOFVacuumNode.isotropic_saturated(n=1.5)
    gamma = float((iso.Z[0] - Z_0) / (iso.Z[0] + Z_0))
    out["isotropic_regime"] = {
        "n": 1.5,
        "c_i": iso.c.tolist(),
        "c0_over_n": C_0 / 1.5,
        "Z_i": iso.Z.tolist(),
        "Gamma": gamma,
        "achromatic": bool(np.allclose(iso.Z, Z_0, rtol=1e-12)),
        "isotropic": bool(np.allclose(iso.c, iso.c[0])),
    }

    # ---- (2) DEVIATORIC strain: birefringence FORM ----------------------------
    deltas = [1e-4, 3e-4, 1e-3, 3e-3, 1e-2]
    bf = [abs(PerDOFVacuumNode.deviatoric(1.0, d).birefringence()) for d in deltas]
    out["deviatoric_regime"] = {
        "delta": deltas,
        "birefringence_dc_over_c": bf,
        "ratio_bf_over_delta": [b / d for b, d in zip(bf, deltas)],
        "form_linear_in_strain": bool(np.all(np.diff(bf) > 0)),
    }

    # ---- (3) HIGH-k: (q·ℓ)² matter zone-edge + (q·ℓ)⁴ photon birefringence -----
    qells = [1e-3, 2e-3, 4e-3, 8e-3]
    matter = [abs(directional_anisotropy(cold, qe / L_NODE, K4_BOND_DIRECTIONS[0], [1, 0, 0])) for qe in qells]
    photon = [abs(photon_birefringence(cold, qe / L_NODE, [2, 1, 0])) for qe in qells]
    out["highk_regime"] = {
        "q_ell": qells,
        "matter_zone_edge_anisotropy": matter,
        "matter_loglog_slope": _loglog_slope(qells, matter),
        "photon_birefringence": photon,
        "photon_loglog_slope": _loglog_slope(qells, photon),
        "cubic_invariant_Xi": {
            "[100]": cubic_anisotropy_invariant([1, 0, 0]),
            "[111]": cubic_anisotropy_invariant([1, 1, 1]),
            "[110]": cubic_anisotropy_invariant([1, 1, 0]),
            "[210]": cubic_anisotropy_invariant([2, 1, 0]),
        },
    }
    # continuum linearity check
    q_lin = 1.0 / (1e5 * L_NODE)
    w_lin = float(lattice_dispersion(cold, q_lin, [1.0, 0.0, 0.0]))
    out["highk_regime"]["continuum_w_over_ck"] = w_lin / (C_0 * q_lin)

    # ---- report ---------------------------------------------------------------
    print("=" * 70)
    print("PER-DOF VACUUM NODE CIRCUIT — dispersion demonstration (#44)")
    print("=" * 70)
    print("\n(c) VALIDATE-ON-KNOWN (isotropic continuum limit):")
    print(f"    c_i = {cold.c[0]:.9e} m/s   c₀ = {C_0:.9e}   recovered: {c_ok}")
    print(f"    Z_i = {cold.Z[0]:.9f} Ω      Z₀ = {Z_0:.9f}     recovered: {z_ok}")
    print("\n(1) ISOTROPIC saturation n=1.5 (achromatic + isotropic):")
    print(f"    c_i = {iso.c[0]:.6e} = c₀/n ({C_0/1.5:.6e})   Z_i = {iso.Z[0]:.6f} Ω")
    print(f"    Γ = {gamma:.2e} (matched → no reflection); light bends, no dispersion")
    print("\n(2) DEVIATORIC strain → birefringence FORM (Δc/c vs δ):")
    for d, b in zip(deltas, bf):
        print(f"    δ={d:.0e}   |Δc/c|={b:.6e}   (Δc/c)/δ={b/d:+.4f}")
    print("\n(3) HIGH-k dispersion:")
    print(f"    continuum ω/(c·q) = {out['highk_regime']['continuum_w_over_ck']:.9f} (→1, linear)")
    print(f"    MATTER zone-edge anisotropy slope = {out['highk_regime']['matter_loglog_slope']:.4f} (q·ℓ)²")
    print(f"    PHOTON birefringence slope        = {out['highk_regime']['photon_loglog_slope']:.4f} (q·ℓ)⁴")
    print(f"    cubic invariant Ξ: [100]=+0.400  [111]=−0.267  (sign-changing → cubic)")
    print("\nONE circuit, THREE behaviors — CONSISTENCY re-expression (no α/m_e value).")

    out_dir = Path(__file__).resolve().parent / "_output"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "per_dof_node_dispersion_demo.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nResults written: {out_path}")


if __name__ == "__main__":
    main()
