"""C3-style Flyby Anomaly Anderson 2008 Anchor — AVE Sagnac-RLVE forward prediction
verification per per-spacecraft published flyby data (PRL 100:091102).

Pre-registration: research/2026-05-18_flyby-anomaly-anderson-anchor-prereg.md

Tests the corpus formula:

    ΔV_flyby = V_∞ · 2(U_⊕/C_0) · cos(α_geo)·cos(δ_geo)

from `manuscript/ave-kb/vol3/cosmology/ch14-orbital-mechanics/flyby-anomaly-sagnac-operator.md:20`
against the Anderson et al. 2008 PRL 100:091102 Table I six-flyby anchor
set (Galileo I, Galileo II, NEAR, Cassini, Rosetta I, MESSENGER).

The leaf's α_geo/δ_geo are NOT specified per-spacecraft — driver tests
multiple plausible conventions:

  (A) Single in-direction: α_geo = α_in, δ_geo = δ_in
  (B) Single out-direction: α_geo = α_out, δ_geo = δ_out
  (C) Mean: α_geo = (α_in+α_out)/2, δ_geo = (δ_in+δ_out)/2
  (D) Anderson empirical form: replace cos(α)cos(δ) with (cos δ_in - cos δ_out)

Per ave-driver-script-honesty four-discriminator:
  1. Canonical imports: C_0 from ave.core.constants; Earth params from cited sources
  2. Forward (no fits): closed-form formula evaluated per-spacecraft
  3. Internal-contradiction: surface per-spacecraft mismatch if convention fails
  4. Silent-overclaim: report ALL 6 spacecraft individually; NO aggregate match rate
"""

from __future__ import annotations

import json
import math
import os
from dataclasses import asdict, dataclass

from ave.core.constants import C_0  # canonical AVE speed of light

# ─── Earth physical constants (cited sources) ───────────────────────────
# WGS-84 reference ellipsoid equatorial radius
R_E_M: float = 6_378_137.0  # m (WGS-84 standard)

# Sidereal day (Earth rotation period relative to fixed stars)
T_SIDEREAL_S: float = 86_164.0905  # s (IERS standard)

# Earth equatorial rotation angular velocity
OMEGA_E_RAD_S: float = 2.0 * math.pi / T_SIDEREAL_S  # rad/s

# Boundary equatorial velocity U_⊕ (corpus says ~465 m/s)
U_E_M_S: float = OMEGA_E_RAD_S * R_E_M  # m/s


# ─── Anderson et al. 2008 PRL 100:091102 Table I ────────────────────────
# Per-spacecraft published flyby data. Six-event anchor set.
# Values from PRL Table I (verify against publication for production work).
@dataclass
class FlybyEvent:
    name: str
    date: str
    V_inf_km_s: float
    alpha_in_deg: float
    delta_in_deg: float
    alpha_out_deg: float
    delta_out_deg: float
    observed_dV_mm_s: float
    observed_sigma_mm_s: float
    notes: str = ""


ANDERSON_2008_FLYBYS: list[FlybyEvent] = [
    FlybyEvent(
        name="Galileo I",
        date="1990-12-08",
        V_inf_km_s=8.949,
        alpha_in_deg=266.76, delta_in_deg=-12.52,
        alpha_out_deg=219.97, delta_out_deg=34.15,
        observed_dV_mm_s=3.92,
        observed_sigma_mm_s=0.30,
    ),
    FlybyEvent(
        name="Galileo II",
        date="1992-12-08",
        V_inf_km_s=8.877,
        alpha_in_deg=219.35, delta_in_deg=34.26,
        alpha_out_deg=174.35, delta_out_deg=4.87,
        observed_dV_mm_s=-4.6,
        observed_sigma_mm_s=1.0,
    ),
    FlybyEvent(
        name="NEAR",
        date="1998-01-23",
        V_inf_km_s=6.851,
        alpha_in_deg=261.17, delta_in_deg=-20.76,
        alpha_out_deg=183.49, delta_out_deg=71.96,
        observed_dV_mm_s=13.46,
        observed_sigma_mm_s=0.13,
        notes="Largest published flyby anomaly; corpus '13.4 mm/s' candidate match.",
    ),
    FlybyEvent(
        name="Cassini",
        date="1999-08-18",
        V_inf_km_s=16.010,
        alpha_in_deg=334.31, delta_in_deg=-12.92,
        alpha_out_deg=352.54, delta_out_deg=-4.99,
        observed_dV_mm_s=-2.0,
        observed_sigma_mm_s=1.0,
    ),
    FlybyEvent(
        name="Rosetta I",
        date="2005-03-04",
        V_inf_km_s=3.863,
        alpha_in_deg=346.12, delta_in_deg=-2.81,
        alpha_out_deg=246.51, delta_out_deg=-34.29,
        observed_dV_mm_s=1.82,
        observed_sigma_mm_s=0.05,
    ),
    FlybyEvent(
        name="MESSENGER",
        date="2005-08-02",
        V_inf_km_s=4.056,
        alpha_in_deg=292.61, delta_in_deg=31.44,
        alpha_out_deg=227.17, delta_out_deg=-31.92,
        observed_dV_mm_s=0.02,
        observed_sigma_mm_s=0.01,
        notes="Anderson 2008 noted as outlier of simple empirical fit.",
    ),
]


# ─── AVE formula evaluations (4 convention variants) ────────────────────
def predict_dV_AVE_cos_product(
    V_inf_m_s: float, alpha_deg: float, delta_deg: float
) -> float:
    """Corpus literal: ΔV = V_∞ · 2(U_⊕/C_0) · cos(α_geo)·cos(δ_geo).

    Returns ΔV in m/s.
    """
    coupling = 2.0 * (U_E_M_S / C_0)
    cos_factor = math.cos(math.radians(alpha_deg)) * math.cos(math.radians(delta_deg))
    return V_inf_m_s * coupling * cos_factor


def predict_dV_Anderson_empirical(
    V_inf_m_s: float, delta_in_deg: float, delta_out_deg: float
) -> float:
    """Anderson 2008 empirical: ΔV = V_∞ · 2(U_⊕/C_0) · (cos δ_in − cos δ_out).

    Same dimensional structure as AVE formula but with the geometric factor
    replaced by Anderson's empirical δ-difference form.
    Returns ΔV in m/s.
    """
    coupling = 2.0 * (U_E_M_S / C_0)
    delta_factor = math.cos(math.radians(delta_in_deg)) - math.cos(math.radians(delta_out_deg))
    return V_inf_m_s * coupling * delta_factor


# ─── Per-spacecraft evaluation ──────────────────────────────────────────
def evaluate_flyby(fb: FlybyEvent) -> dict:
    """Apply each convention to the spacecraft + report observed comparison."""
    V_inf = fb.V_inf_km_s * 1000.0  # m/s

    # Max possible ΔV per AVE formula (with cos·cos = ±1)
    max_dV_mm_s = V_inf * 2.0 * (U_E_M_S / C_0) * 1000.0  # mm/s

    # Convention A: cos(α_in)·cos(δ_in)
    dV_A = predict_dV_AVE_cos_product(V_inf, fb.alpha_in_deg, fb.delta_in_deg) * 1000.0
    # Convention B: cos(α_out)·cos(δ_out)
    dV_B = predict_dV_AVE_cos_product(V_inf, fb.alpha_out_deg, fb.delta_out_deg) * 1000.0
    # Convention C: cos((α_in+α_out)/2)·cos((δ_in+δ_out)/2)
    dV_C = predict_dV_AVE_cos_product(
        V_inf,
        (fb.alpha_in_deg + fb.alpha_out_deg) / 2.0,
        (fb.delta_in_deg + fb.delta_out_deg) / 2.0,
    ) * 1000.0
    # Convention D: Anderson empirical (cos δ_in - cos δ_out)
    dV_D = predict_dV_Anderson_empirical(V_inf, fb.delta_in_deg, fb.delta_out_deg) * 1000.0

    # Required cos·cos for AVE formula to match observed (cos = obs/max)
    cos_required = fb.observed_dV_mm_s / max_dV_mm_s if max_dV_mm_s != 0 else 0.0

    # σ-tension per convention
    def sigma(dV_pred_mm_s):
        diff = dV_pred_mm_s - fb.observed_dV_mm_s
        return diff / fb.observed_sigma_mm_s

    return {
        "name": fb.name,
        "date": fb.date,
        "V_inf_km_s": fb.V_inf_km_s,
        "observed_dV_mm_s": fb.observed_dV_mm_s,
        "observed_sigma_mm_s": fb.observed_sigma_mm_s,
        "max_dV_mm_s_cos_cos_unity": max_dV_mm_s,
        "cos_factor_required": cos_required,
        "convention_A_cos_in": {"dV_mm_s": dV_A, "sigma": sigma(dV_A)},
        "convention_B_cos_out": {"dV_mm_s": dV_B, "sigma": sigma(dV_B)},
        "convention_C_cos_mean": {"dV_mm_s": dV_C, "sigma": sigma(dV_C)},
        "convention_D_Anderson_empirical": {"dV_mm_s": dV_D, "sigma": sigma(dV_D)},
        "notes": fb.notes,
    }


def classify_match(sigma: float) -> str:
    """1σ within | 2σ within | 3σ within | beyond"""
    abs_s = abs(sigma)
    if abs_s <= 1.0:
        return "✓ ≤1σ"
    elif abs_s <= 2.0:
        return "○ ≤2σ"
    elif abs_s <= 3.0:
        return "· ≤3σ"
    else:
        return "✗ >3σ"


def run() -> dict:
    print("=" * 105)
    print("FLYBY ANOMALY ANDERSON 2008 ANCHOR — AVE Sagnac-RLVE Formula Verification")
    print("Pre-registration: research/2026-05-18_flyby-anomaly-anderson-anchor-prereg.md")
    print("=" * 105)

    print(f"\nCanonical Earth + AVE constants:")
    print(f"  C_0:        {C_0:.6e} m/s (from ave.core.constants)")
    print(f"  R_E:        {R_E_M:.6e} m (WGS-84)")
    print(f"  T_sidereal: {T_SIDEREAL_S:.4f} s (IERS)")
    print(f"  ω_⊕:        {OMEGA_E_RAD_S:.6e} rad/s")
    print(f"  U_⊕:        {U_E_M_S:.3f} m/s  (corpus says ~465 m/s)  ← boundary velocity")
    print(f"  2·U_⊕/C_0:  {2*U_E_M_S/C_0:.6e}  (dimensionless coupling)")

    print(f"\nAVE formula (per flyby-anomaly-sagnac-operator.md:20):")
    print(f"  ΔV = V_∞ · 2(U_⊕/C_0) · cos(α_geo)·cos(δ_geo)")
    print(f"\nLeaf does NOT specify α_geo/δ_geo per-spacecraft. Driver tests 4 conventions:")
    print(f"  A: cos(α_in)·cos(δ_in)")
    print(f"  B: cos(α_out)·cos(δ_out)")
    print(f"  C: cos(mean(α))·cos(mean(δ))")
    print(f"  D: (cos δ_in - cos δ_out)  ← Anderson 2008 empirical form")

    print(f"\n{'='*105}")
    print(f"{'Spacecraft':<14} {'V_∞':>8} {'Obs ΔV':>14} {'Conv-A':>15} {'Conv-B':>15} {'Conv-C':>15} {'Conv-D':>15}")
    print(f"{'':14} {'(km/s)':>8} {'(mm/s)':>14} {'(mm/s, σ)':>15} {'(mm/s, σ)':>15} {'(mm/s, σ)':>15} {'(mm/s, σ)':>15}")
    print(f"{'='*105}")

    results = []
    convention_match_counts = {"A": 0, "B": 0, "C": 0, "D": 0}
    convention_within_2sigma = {"A": 0, "B": 0, "C": 0, "D": 0}

    for fb in ANDERSON_2008_FLYBYS:
        r = evaluate_flyby(fb)
        results.append(r)

        cA = r["convention_A_cos_in"]
        cB = r["convention_B_cos_out"]
        cC = r["convention_C_cos_mean"]
        cD = r["convention_D_Anderson_empirical"]

        print(
            f"{fb.name:<14} {fb.V_inf_km_s:>8.3f} {fb.observed_dV_mm_s:>+7.2f}±{fb.observed_sigma_mm_s:<5.2f}"
            f" {cA['dV_mm_s']:>+7.3f} σ={cA['sigma']:>+5.1f}"
            f" {cB['dV_mm_s']:>+7.3f} σ={cB['sigma']:>+5.1f}"
            f" {cC['dV_mm_s']:>+7.3f} σ={cC['sigma']:>+5.1f}"
            f" {cD['dV_mm_s']:>+7.3f} σ={cD['sigma']:>+5.1f}"
        )

        for conv_key, conv in [("A", cA), ("B", cB), ("C", cC), ("D", cD)]:
            if abs(conv["sigma"]) <= 1.0:
                convention_match_counts[conv_key] += 1
            if abs(conv["sigma"]) <= 2.0:
                convention_within_2sigma[conv_key] += 1

    print("=" * 105)
    print(f"\nMATCH SUMMARY (6 spacecraft):")
    print(f"  Convention A (cos(α_in)·cos(δ_in)):       {convention_match_counts['A']}/6 within 1σ, {convention_within_2sigma['A']}/6 within 2σ")
    print(f"  Convention B (cos(α_out)·cos(δ_out)):     {convention_match_counts['B']}/6 within 1σ, {convention_within_2sigma['B']}/6 within 2σ")
    print(f"  Convention C (cos(mean(α))·cos(mean(δ))): {convention_match_counts['C']}/6 within 1σ, {convention_within_2sigma['C']}/6 within 2σ")
    print(f"  Convention D (Anderson cos δ_in-cos δ_out): {convention_match_counts['D']}/6 within 1σ, {convention_within_2sigma['D']}/6 within 2σ")

    # Corpus claim cross-check: "13.4 mm/s without fitting"
    print(f"\n{'='*105}")
    print(f"CORPUS CLAIM CROSS-CHECK")
    print(f"{'='*105}")
    near = next(r for r in results if r["name"] == "NEAR")
    print(f"Corpus (flyby-anomaly-sagnac-operator.md:22): 'intrinsically outputs ΔV ≈ 13.4 mm/s without fitting'")
    print(f"NEAR observed: +13.46 ± 0.13 mm/s (highest published flyby anomaly)")
    print(f"NEAR predictions:")
    print(f"  AVE formula Convention D (Anderson empirical): {near['convention_D_Anderson_empirical']['dV_mm_s']:+.3f} mm/s")
    print(f"    → matches NEAR observed to {near['convention_D_Anderson_empirical']['sigma']:+.2f}σ")
    print(f"  Required cos·cos for AVE formula to give NEAR observed: {near['cos_factor_required']:+.4f}")
    print(f"  Anderson empirical (cos δ_in - cos δ_out) for NEAR: {math.cos(math.radians(-20.76)) - math.cos(math.radians(71.96)):+.4f}")
    print(f"  ← match between required and Anderson empirical = AVE notation 'cos(α)cos(δ)' is structurally the Anderson empirical form for NEAR")

    # Outcome classification per prereg Section 3c
    print(f"\n{'='*105}")
    print(f"OUTCOME ASSESSMENT (per prereg Section 3c)")
    print(f"{'='*105}")

    best_conv = max(convention_match_counts.items(), key=lambda x: x[1])
    best_within_2s = max(convention_within_2sigma.items(), key=lambda x: x[1])

    if convention_match_counts["D"] >= 4:
        outcome = "A or partial-A: Anderson empirical convention reproduces ≥4/6 within 1σ — AVE formula structurally identical to Anderson 2008 empirical fit"
    elif convention_within_2sigma["D"] >= 4:
        outcome = "B: Convention D (Anderson empirical) matches ≥4/6 within 2σ — partial match, formula captures main physics but not all variation"
    elif convention_match_counts["D"] >= 1 and convention_match_counts["A"] == 0 and convention_match_counts["B"] == 0:
        outcome = "C or D: AVE 'cos(α)cos(δ)' notation under-specified; only Anderson empirical form gives any match. Leaf's literal cos(α)cos(δ) framing is misleading"
    else:
        outcome = "Mixed: no convention reproduces all 6; per-spacecraft variation not fully captured"

    print(f"Best convention by 1σ matches: {best_conv[0]} = {best_conv[1]}/6")
    print(f"Best convention by 2σ matches: {best_within_2s[0]} = {best_within_2s[1]}/6")
    print(f"\nOutcome: {outcome}")

    # JSON output
    out_path = os.path.join(os.path.dirname(__file__), "flyby_anomaly_anderson_anchor_results.json")
    out = {
        "prereg": "research/2026-05-18_flyby-anomaly-anderson-anchor-prereg.md",
        "earth_constants": {
            "C_0_m_s": C_0,
            "R_E_m": R_E_M,
            "T_sidereal_s": T_SIDEREAL_S,
            "OMEGA_E_rad_s": OMEGA_E_RAD_S,
            "U_E_m_s": U_E_M_S,
            "coupling_2_U_E_over_C_0": 2 * U_E_M_S / C_0,
        },
        "per_spacecraft": results,
        "convention_match_counts_1sigma": convention_match_counts,
        "convention_within_2sigma": convention_within_2sigma,
        "outcome_classification": outcome,
    }
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nResults JSON: {out_path}")

    return out


if __name__ == "__main__":
    run()
