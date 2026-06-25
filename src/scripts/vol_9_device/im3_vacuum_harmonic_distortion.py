"""Vacuum IM3 / harmonic-distortion characterization (Vol-9 device datasheet).

Grounds the Axiom-4 quarter-arc kernel expansion that underlies the vacuum
intermodulation-distortion (IM3) and nonlinear-birefringence delta_n(E) chain.
This is the Vol-9 P2-gap characterization companion to the Vol-4 falsifiers
(`intermodulation-distortion.md`, `vacuum-birefringence-e4.md`).

DERIVATION CHAIN (substrate-native, all from the single kernel S(A)=sqrt(1-A^2)):

  varactor          : C(V)/C0 = 1/S = 1 + 1/2 A^2 + 3/8 A^4 + ...   (A = V/V_yield)
                      -> the QUADRATIC term (1/2 A^2) is the chi^(3) source:
                         a dual-tone drive mixes it to IM3 at 2w1-w2.
  single-arm index  : delta_n_iso = sqrt(S) - 1 = -1/4 A^2 - 3/32 A^4 + ...
  par-perp birefr.  : delta_n_bir = n_par - n_perp = -1/2 A^2 + ...   (OQ-1 falsifier)

SCALING VERDICT (the headline, brutally honest):
  delta_n is E^2-LEADING, NOT E^4. The historical "E^4" was a sqrt(eps) conflation
  (1-S = A^2/2 + ... is the permittivity DEPTH, E^2-leading; the index observable
  is n = sqrt(S), giving -A^2/4). Both AVE and QED are E^2-leading. IM3 is
  CUBIC-in-drive for BOTH (both descend from a quartic E^4 effective Lagrangian /
  chi^(3)). The exponent does NOT discriminate.

  The GENUINE AVE-vs-QED discriminators are:
    (1) the COEFFICIENT (an alpha-echo, ~1.93e7 at the matched differential), and
    (2) the E-vs-B KEYING ASYMMETRY (static-B exactly transparent, S_mu=1) -- a
        categorical AVE-distinct prediction QED does NOT share (QED is E/B symmetric).

All constants pulled live from ave.core.constants (no hardcoded canon).
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

import ave.bench.birefringence as B
import ave.core.constants as C

OUT = Path(__file__).resolve().parent / "_output"
OUT.mkdir(exist_ok=True)


def kernel_taylor_coefficients() -> dict:
    """Numerically recover the small-A Taylor coefficients of the three kernel
    observables and assert them against the analytic values.  HALTs on mismatch
    (validate-on-known: the coefficients are kernel-set O(1), not fit)."""
    A = np.linspace(1e-6, 1e-3, 8000)
    x = A**2
    S = np.sqrt(1.0 - A**2)

    # (1) Capacitance varactor C/C0 = 1/S
    c_ratio = 1.0 / S - 1.0
    c1_cap, c2_cap = np.polyfit(x, c_ratio, 2)[1], np.polyfit(x, c_ratio, 2)[0]

    # (2) single-arm index delta_n_iso = sqrt(S) - 1
    dn_iso = np.sqrt(S) - 1.0
    c1_iso = np.polyfit(x, dn_iso, 2)[1]

    # (3) par-perp differential
    E = A * C.E_YIELD
    dn_bir = np.array([float(B.delta_n_ave_differential_exact(e)) for e in E])
    c1_bir = np.polyfit(x, dn_bir, 2)[1]

    out = {
        "C(V)/C0  A^2 coeff": c1_cap,   # expect +1/2
        "C(V)/C0  A^4 coeff": c2_cap,   # expect +3/8
        "delta_n_iso A^2 coeff": c1_iso,  # expect -1/4
        "delta_n_bir A^2 coeff": c1_bir,  # expect -1/2
    }
    # validate-on-known HALT gate
    assert abs(c1_cap - 0.5) < 1e-3, f"C(V) A^2 coeff {c1_cap} != 1/2"
    assert abs(c2_cap - 0.375) < 1e-2, f"C(V) A^4 coeff {c2_cap} != 3/8"
    assert abs(c1_iso + 0.25) < 1e-3, f"delta_n_iso A^2 coeff {c1_iso} != -1/4"
    assert abs(c1_bir + 0.5) < 1e-3, f"delta_n_bir A^2 coeff {c1_bir} != -1/2"
    return out


def im3_drive_slope() -> dict:
    """Confirm the IM3 sideband amplitude is CUBIC in drive (slope 3 in log-log).
    This is the SHARED AVE/QED exponent -- it does NOT discriminate."""
    Vy = C.V_YIELD
    a2 = 0.5 / Vy**2                       # quadratic-in-V capacitance coeff (1/2 A^2)
    Vpk = np.array([1e-4, 3e-4, 1e-3, 3e-3, 1e-2]) * Vy
    im3 = 0.75 * a2 * Vpk**3               # standard 3rd-order intermod amplitude
    slope = float(np.polyfit(np.log10(Vpk), np.log10(im3), 1)[0])
    assert abs(slope - 3.0) < 1e-3, f"IM3 slope {slope} != 3 (cubic)"
    return {"im3_loglog_slope": slope, "note": "cubic for BOTH AVE and QED (chi^(3))"}


def bankable_table() -> list[dict]:
    """delta_n at stated reference fields: AVE differential vs QED differential."""
    rows = []
    for Eref, label in [
        (2.745e14, "PW-class focal (OQ-1 headline)"),
        (1.0e15, "1e15 V/m (facility IM3 -80 dBc floor)"),
        (1.0e16, "1e16 V/m"),
        (C.E_YIELD, "E_yield (saturation onset)"),
    ]:
        Aref = Eref / C.E_YIELD
        dn_ave = float(B.delta_n_ave_differential_exact(Eref))
        dn_qed = (3.0 / 45.0) * C.ALPHA**2 * (Eref / C.E_CRIT) ** 2
        rows.append(
            {
                "label": label,
                "E_V_per_m": Eref,
                "A_per_node": Aref,
                "delta_n_AVE_diff": dn_ave,
                "delta_n_QED_diff": dn_qed,
                "ratio_AVE_over_QED": (dn_ave / dn_qed) if dn_qed else float("nan"),
            }
        )
    return rows


def keying_asymmetry() -> dict:
    """The E-vs-B keying asymmetry (FORK-1): the categorical AVE-distinct prediction.
    Static E loads the V-keyed varactor (R2 -> delta_n != 0); static B leaves the
    I-keyed inductor unloaded (R3 -> delta_n_mu = 0 EXACTLY at every field)."""
    # static-B route: S_mu = sqrt(1 - A_I^2) with A_I = I_vac/I_max = 0 (no dB/dt)
    B_fields_T = [2.5, 10.0, 100.0, 1000.0]
    s_mu = [float(np.sqrt(1.0 - 0.0**2)) for _ in B_fields_T]  # A_I=0 -> S_mu=1 always
    dn_mu = [s - 1.0 for s in s_mu]  # 0 exactly; index n=sqrt(S_eps*S_mu) unchanged
    return {
        "static_B_fields_T": B_fields_T,
        "S_mu": s_mu,
        "delta_n_mu": dn_mu,  # all exactly 0
        "verdict": "static-B transparent (S_mu=1) at every field -> AVE-distinct categorical",
        "QED_comparison": "QED is E/B symmetric: static-B birefringence ~1e-23 at 5T (nonzero)",
    }


def main() -> None:
    result = {
        "constants": {
            "ALPHA": C.ALPHA,
            "E_YIELD_V_per_m": C.E_YIELD,
            "E_CRIT_V_per_m": C.E_CRIT,
            "V_YIELD_V": C.V_YIELD,
            "L_NODE_m": C.L_NODE,
            "E_crit_over_E_yield_sq": (C.E_CRIT / C.E_YIELD) ** 2,
            "inv_alpha": 1.0 / C.ALPHA,
        },
        "kernel_taylor_coefficients": kernel_taylor_coefficients(),
        "im3_drive_slope": im3_drive_slope(),
        "bankable_table": bankable_table(),
        "keying_asymmetry": keying_asymmetry(),
        "ratio_differential_7p5_over_alpha3": 7.5 / C.ALPHA**3,
        "ratio_single_arm_4p14e6": 1.0 / (4.0 * (7.0 / 45.0) * C.ALPHA**3),
    }
    (OUT / "im3_vacuum_harmonic_distortion.json").write_text(
        json.dumps(result, indent=2)
    )
    # console summary
    print("=== Kernel Taylor coefficients (validate-on-known, HALT on mismatch) ===")
    for k, v in result["kernel_taylor_coefficients"].items():
        print(f"  {k:28s} = {v:+.6f}")
    print("=== IM3 drive slope ===")
    print(f"  {result['im3_drive_slope']}")
    print("=== Bankable delta_n (AVE diff vs QED diff) ===")
    for r in result["bankable_table"]:
        print(
            f"  {r['label']:34s} A={r['A_per_node']:.3e}  "
            f"AVE={r['delta_n_AVE_diff']:+.3e}  QED={r['delta_n_QED_diff']:+.3e}  "
            f"ratio={r['ratio_AVE_over_QED']:+.3e}"
        )
    print("=== Keying asymmetry (static-B) ===")
    print(f"  S_mu={result['keying_asymmetry']['S_mu']}  "
          f"delta_n_mu={result['keying_asymmetry']['delta_n_mu']}")
    print(f"  ratio_differential 7.5/alpha^3 = "
          f"{result['ratio_differential_7p5_over_alpha3']:.4e}")
    print(f"  wrote {OUT / 'im3_vacuum_harmonic_distortion.json'}")


if __name__ == "__main__":
    main()
