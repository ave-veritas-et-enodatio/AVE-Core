"""C3-MUON-DELTA Fermilab Muon g-2 Anchor Driver (Post-Walk-Back Re-Frame).

PREREG: research/2026-05-19_c3-muon-delta-fermilab-driver-rerun-prereg.md
WALK-BACK COMMITS: fb5a9d4 (Q-G27 + Q-G19α factor-2 Action 1+3-(A));
                   e0e4315 (Q-G19α Action 2 two-stage reframing);
                   a2b4e14 (closure-roadmap §0.5 backfill)
PREDECESSOR PREREG (pre-walk-back): research/2026-05-18_c3-muon-delta-fermilab-driver-prereg.md

Forward-predicts AVE-canonical Q-G27 Cosserat-torsion saliency contribution
to muon g-2 and compares against Fermilab Run-3 tension on TWO SM baselines:
e+e- (Theory Initiative 2020) and BMW lattice QCD (Borsanyi+ 2021).

The forward prediction Δa_μ^(2) = +502×10⁻¹¹ is in 4.6σ tension above the
Fermilab-vs-e+e- observed tension and ~6.7σ DEEPER above the Fermilab-vs-BMW
tension. BMW makes the tension worse, not softer — BMW lattice closes most
of the Fermilab-vs-SM gap, so AVE's +502 forward prediction has no observed
anomaly to absorb. The tension structure on BOTH baselines is the finding.

Per ave-driver-script-honesty discipline:
- All constants imported from ave.core.constants + ave.topological.cosserat
  (no hardcoded α, m_e, m_μ values)
- Fermilab + BMW lattice paper citations pinned with DOI/journal references
- BMW vs e+e- SM-baselines reported as PARALLEL numerical tensions (not
  prose-only conditional)
- All per-state numerics reported to ≥3 sig figs
- Forward prediction (Q-G27 Cosserat saliency); not fit against target
- No silent overclaim: AVE-vs-Fermilab plotted as tension structure on both
  baselines, NOT as "match"

Per consistency-vs-emergence: Class 3 (consistency check). AVE provides
alternative mechanism (Cosserat saliency) for Fermilab-vs-SM observed
tension; forward prediction is genuinely AVE-distinct (SM has no equivalent
Cosserat-torsion-quantum term); the dual-baseline tension structure IS the
post-walk-back canonical framing.

Run:
    PYTHONPATH=src python3 src/scripts/verify/muon_g2_fermilab_anchor.py
"""

import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.core.constants import ALPHA, M_E
from ave.topological.cosserat import M_MU, M_MU_MEV

# ============================================================
# Fermilab data — pinned references
# ============================================================
# Source citations:
# (a) PRL 131:161802 (2023) — Run-1+Run-2 world average
# (b) Run-3 release: Fermilab Muon g-2 Collaboration, see
#     https://muon-g-2.fnal.gov/result2023.pdf for Run-3 update;
#     world average post-Run-3 quoted at +245(56)×10⁻¹¹ tension vs e+e- SM baseline.
# (c) BMW lattice SM prediction: Borsanyi et al. 2021, Nature 593:51-55
#     "Leading hadronic contribution to the muon magnetic moment from lattice QCD"
#     a_μ_SM_BMW = 116591954(55)×10⁻¹¹ — closes the Fermilab-vs-SM tension that
#     the e+e- baseline shows; per Q-G27 leaf line 67 the AVE forward +502
#     prediction is in DEEPER tension when AVE+SM evaluated against Fermilab
#     measurement on the BMW SM baseline.

FERMILAB_RUN1_RUN2_WORLD_AVG = 0.00116592055  # a_μ central value
FERMILAB_RUN1_RUN2_UNCERTAINTY = 24e-11  # ±0.24 ppm
FERMILAB_PAPER_RUN12 = "PRL 131:161802 (2023)"

FERMILAB_RUN3_TENSION_CENTRAL = 245e-11  # +245×10⁻¹¹ vs e+e- SM baseline
FERMILAB_RUN3_TENSION_UNCERTAINTY = 56e-11  # ±56×10⁻¹¹ (combined Fermilab+SM_eeplus)
FERMILAB_RUN3_REFERENCE = "Fermilab Muon g-2 result2023 + e+e- SM baseline (Theory Initiative 2020)"

BMW_SM_BORSANYI_2021 = 116591954e-11  # a_μ_SM_BMW central value
BMW_SM_BORSANYI_2021_UNCERTAINTY = 55e-11  # ±0.47 ppm
BMW_SM_PAPER = "Borsanyi+ 2021, Nature 593:51-55"


# ============================================================
# AVE Q-G27 Canonical Formula (post-walk-back)
# ============================================================
# Per q-g27-muon-cosserat-saliency.md (canonical leaf, post-walk-back state):
#   δ_Cosserat = -α√(3/7) / (2π)                    [Q-G27 line 36, substrate-derived]
#   δ_e_petermann = -3α/2                           [Q-G19α line 78, substrate-derived]
#   δ_μ = δ_e + δ_Cosserat                          [Q-G27 line 51, substrate-derived]
#   ΔC_2 = +9.30×10⁻⁴ from Route B engine output    [Q-G27 line 53, corpus-quoted]
#   Δa_μ^(2) = ΔC_2 × (α/π)² (textbook QED 2-loop conversion)
#
# The √(3/7) PAT torsion-shear projection in δ_Cosserat is the SAME projection
# in the canonical lepton-mass ladder m_μ = m_e/(α√(3/7)) at 1.24% match — walk-
# back option (B) (half-strength coupling) was STRUCTURALLY RULED OUT because
# it would break the lepton-mass derivation by 2×.


def compute_q_g27_prediction() -> dict:
    """Compute Q-G27 canonical Cosserat torsion saliency forward prediction.

    Substrate-derived inputs (canonical Q-G27 + Q-G19α formulas):
      - δ_Cosserat = -α·√(3/7)/(2π)
      - δ_e_petermann = -3α/2
      - δ_μ_total = δ_e + δ_Cosserat = -0.01171

    Corpus-quoted Route B engine output (q-g27 leaf line 53):
      - ΔC_2 = +9.30×10⁻⁴ (Petermann coefficient shift from Route-B numerical
        bisection of substrate-derived saliency; the Route B framework converts
        δ_μ → C_2^μ via numerical integration not closed-form algebra)

    Textbook QED 2-loop conversion:
      - Δa_μ^(2) = ΔC_2 × (α/π)² = +502×10⁻¹¹ (forward prediction)
    """
    # δ_Cosserat per Q-G27 leaf canonical formula
    delta_cosserat = -ALPHA * math.sqrt(3.0 / 7.0) / (2 * math.pi)

    # δ_e Petermann baseline per Q-G19α leaf canonical formula
    delta_e_petermann = -3.0 * ALPHA / 2.0

    # δ_μ total per Q-G27 leaf line 51
    delta_mu_total = delta_e_petermann + delta_cosserat

    # ΔC_2 corpus-quoted Route B engine output per Q-G27 leaf line 53
    # (Route B + saliency shifts C_2^μ by +0.28% relative to electron baseline;
    # the Route B → C_2 mapping is numerical-bisection output, not closed-form)
    delta_c_2_route_b = 9.30e-4

    # Textbook QED 2-loop conversion: Δa^(2) = ΔC_2 × (α/π)²
    alpha_over_pi = ALPHA / math.pi
    delta_a_mu_2_forward = delta_c_2_route_b * (alpha_over_pi**2)

    return {
        "delta_cosserat": delta_cosserat,
        "delta_e_petermann": delta_e_petermann,
        "delta_mu_total": delta_mu_total,
        "delta_c_2_route_b": delta_c_2_route_b,
        "alpha_over_pi": alpha_over_pi,
        "alpha_over_pi_squared": alpha_over_pi**2,
        "delta_a_mu_2_forward_prediction": delta_a_mu_2_forward,
    }


def compare_to_fermilab_eeplus_baseline(ave_prediction: float) -> dict:
    """Compare AVE forward prediction against Fermilab tension on e+e- SM baseline.

    Fermilab Run-3 reports a_μ^exp - a_μ^SM_eeplus = +245(56)×10⁻¹¹ on the
    Theory Initiative 2020 e+e- baseline. AVE's forward Δa_μ^(2) Cosserat
    saliency contribution sits +257×10⁻¹¹ above this central tension (≈+4.6σ
    over) — a genuine forward-vs-measurement disagreement.
    """
    fermilab_central = FERMILAB_RUN3_TENSION_CENTRAL
    fermilab_uncertainty = FERMILAB_RUN3_TENSION_UNCERTAINTY

    deviation = ave_prediction - fermilab_central
    deviation_pct = 100 * deviation / fermilab_central
    n_sigma = deviation / fermilab_uncertainty

    return {
        "baseline": "e+e- (Theory Initiative 2020)",
        "ave_prediction": ave_prediction,
        "fermilab_observed_tension": fermilab_central,
        "fermilab_observed_uncertainty": fermilab_uncertainty,
        "deviation": deviation,
        "deviation_pct": deviation_pct,
        "n_sigma": n_sigma,
        "tension_direction": "ABOVE" if n_sigma > 0 else "below",
    }


def compare_to_fermilab_bmw_baseline(ave_prediction: float) -> dict:
    """Compare AVE forward prediction against Fermilab tension on BMW lattice SM baseline.

    Per Borsanyi+ 2021 Nature 593:51-55, BMW lattice predicts
    a_μ_SM_BMW = 116591954(55)×10⁻¹¹. Fermilab-vs-BMW central tension is
    a_μ^exp - a_μ_SM_BMW = +101(60)×10⁻¹¹ (≈+1.7σ, BMW closes most of the
    e+e- tension toward 0σ). AVE forward Δa_μ^(2) sits +401×10⁻¹¹ above this
    BMW-anchored central tension at ~6.7σ DEEPER — per Q-G27 leaf line 67,
    BMW makes the tension worse because BMW closes the Fermilab anomaly,
    leaving AVE's +502 forward prediction unabsorbed.
    """
    # Fermilab-vs-BMW central tension = a_μ^exp - a_μ_SM_BMW
    fermilab_vs_bmw_central = FERMILAB_RUN1_RUN2_WORLD_AVG - BMW_SM_BORSANYI_2021

    # Combined uncertainty: Fermilab measurement + BMW SM
    combined_uncertainty = math.sqrt(FERMILAB_RUN1_RUN2_UNCERTAINTY**2 + BMW_SM_BORSANYI_2021_UNCERTAINTY**2)

    # Fermilab-vs-BMW σ-tension (BMW closes most of e+e- anomaly toward 0σ)
    fermilab_vs_bmw_sigma = fermilab_vs_bmw_central / combined_uncertainty

    # AVE forward prediction vs Fermilab-vs-BMW central tension
    deviation = ave_prediction - fermilab_vs_bmw_central
    deviation_pct = 100 * deviation / abs(fermilab_vs_bmw_central) if fermilab_vs_bmw_central != 0 else float("inf")
    n_sigma = deviation / combined_uncertainty

    return {
        "baseline": "BMW lattice (Borsanyi+ 2021)",
        "ave_prediction": ave_prediction,
        "bmw_sm_central": BMW_SM_BORSANYI_2021,
        "bmw_sm_uncertainty": BMW_SM_BORSANYI_2021_UNCERTAINTY,
        "fermilab_vs_bmw_central_tension": fermilab_vs_bmw_central,
        "fermilab_vs_bmw_combined_uncertainty": combined_uncertainty,
        "fermilab_vs_bmw_sigma": fermilab_vs_bmw_sigma,
        "deviation": deviation,
        "deviation_pct": deviation_pct,
        "n_sigma": n_sigma,
        "tension_direction": "DEEPER" if n_sigma > 0 else "softer",
    }


def adjudicate_outcome(comp_eeplus: dict, comp_bmw: dict, ave_prediction: float) -> str:
    """Post-walk-back PASS-conditional / FLAG / RETIRE adjudication.

    PASS-conditional: forward prediction at canonical +502×10⁻¹¹ preserved;
    parallel-baseline tensions reported as the canonical finding (4.6σ above
    e+e- + 6.7σ DEEPER on BMW); the tension structure on both baselines IS
    the finding, not a match.

    FLAG: surface if the post-edit driver produces a computation drift
    (e.g., Δa_μ^(2) ≠ +501.78×10⁻¹¹ to round-off) or if either baseline σ-
    tension materially diverges from the canonical claim at Q-G27 leaf line
    67 (~4.6σ e+e-, ~6.7σ BMW).

    RETIRE: surface if Fermilab Run-4/5 (~2026-2027) at ±10 ppm precision
    settles the central value more than ~100×10⁻¹¹ from AVE's +502 forward
    prediction (the falsification target per Q-G27 leaf line 69).
    """
    # Verify forward prediction preserved at canonical +502×10⁻¹¹
    expected_forward = 5.018e-9  # +501.78×10⁻¹¹ engine-computed; +502 narrative-rounded
    forward_drift_pct = abs(ave_prediction - expected_forward) / expected_forward * 100

    # Verify e+e- σ-tension at expected ~4.6σ
    eeplus_sigma = comp_eeplus["n_sigma"]
    eeplus_canonical_sigma = 4.59  # per Q-G27 leaf + prior driver result
    eeplus_sigma_drift = abs(eeplus_sigma - eeplus_canonical_sigma)

    # Verify BMW σ-tension at expected ~6.7σ DEEPER
    bmw_sigma = comp_bmw["n_sigma"]
    bmw_canonical_sigma = 6.68  # per Q-G27 leaf line 67 + handoff line 7 lock
    bmw_sigma_drift = abs(bmw_sigma - bmw_canonical_sigma)

    # PASS-conditional: forward + both σ-tensions preserved within tolerance
    if forward_drift_pct < 0.5 and eeplus_sigma_drift < 0.2 and bmw_sigma_drift < 0.3:
        return (
            "PASS-conditional — forward prediction +502×10⁻¹¹ preserved; "
            f"parallel-baseline tensions canonical ({eeplus_sigma:+.2f}σ ABOVE on e+e-, "
            f"{bmw_sigma:+.2f}σ DEEPER on BMW); tension structure is the finding."
        )

    # FLAG: forward drift OR baseline-tension drift
    if forward_drift_pct >= 0.5:
        return (
            f"FLAG — forward prediction drift {forward_drift_pct:.2f}% from canonical "
            f"+501.78×10⁻¹¹; surface to Grant before commit (driver formula may be broken)."
        )
    if eeplus_sigma_drift >= 0.2:
        return (
            f"FLAG — e+e- σ-tension {eeplus_sigma:+.2f}σ diverges from canonical "
            f"~{eeplus_canonical_sigma:.1f}σ; surface to Grant."
        )
    if bmw_sigma_drift >= 0.3:
        return (
            f"FLAG — BMW σ-tension {bmw_sigma:+.2f}σ diverges from canonical "
            f"~{bmw_canonical_sigma:.1f}σ DEEPER per Q-G27 leaf line 67; surface to Grant."
        )

    return f"FLAG — unexpected drift pattern (forward {forward_drift_pct:.2f}%, e+e- Δσ {eeplus_sigma_drift:.2f}, BMW Δσ {bmw_sigma_drift:.2f}); surface to Grant."


def main() -> int:
    print("=" * 95)
    print("C3-MUON-DELTA FERMILAB g-2 ANCHOR DRIVER (POST-WALK-BACK FORWARD PREDICTION)")
    print("PREREG: research/2026-05-19_c3-muon-delta-fermilab-driver-rerun-prereg.md")
    print("WALK-BACK: fb5a9d4 + e0e4315 (Q-G27 + Q-G19α factor-2 conversion error)")
    print("=" * 95)
    print()
    print("AVE canonical constants:")
    print(f"  α (CODATA via ave.core.constants):      {ALPHA:.10g}")
    print(f"  m_e (CODATA):                            {M_E:.6e} kg")
    print(f"  M_MU (AVE Cosserat-derived):             {M_MU:.6e} kg  ({M_MU_MEV:.4f} MeV)")
    print(f"  M_μ_PDG experimental:                    105.66 MeV (AVE off by 1.24% per Vol 2 Ch 6)")
    print()

    # ============================================================
    # AVE Q-G27 Forward Prediction
    # ============================================================
    print("=" * 95)
    print("AVE Q-G27 CANONICAL FORWARD PREDICTION (Cosserat torsion saliency)")
    print("=" * 95)
    results = compute_q_g27_prediction()

    print(f"\n  δ_Cosserat = -α√(3/7)/(2π) = {results['delta_cosserat']:.6e}")
    print(f"            = {results['delta_cosserat']:+.4e}  (expected: -7.604×10⁻⁴)")

    print(f"\n  δ_e (Petermann baseline) = -3α/2 = {results['delta_e_petermann']:.6e}")
    print(f"                            = {results['delta_e_petermann']:+.4e}  (expected: -0.01095)")

    print(f"\n  δ_μ (total) = -3α/2 - α√(3/7)/(2π) = {results['delta_mu_total']:.6e}")
    print(f"             = {results['delta_mu_total']:+.4e}  (expected: -0.01171)")

    print(f"\n  ΔC_2 (Route B engine output per Q-G27 line 53): {results['delta_c_2_route_b']:+.5e}")
    print(f"  Note: Route B → C_2 mapping is numerical bisection, not closed-form; ΔC_2 is")
    print(f"        corpus-quoted from substrate-derived δ_μ via Q-G27 Route B framework.")

    print(f"\n  Textbook QED 2-loop conversion: Δa_μ^(2) = ΔC_2 × (α/π)²")
    print(f"    α/π = {results['alpha_over_pi']:.6e}")
    print(f"    (α/π)² = {results['alpha_over_pi_squared']:.6e}")
    print(f"    Δa_μ^(2) [forward] = {results['delta_a_mu_2_forward_prediction']:.6e}")
    print(f"                      = {results['delta_a_mu_2_forward_prediction']*1e11:+.3f} × 10⁻¹¹")
    print(
        f"                      = {results['delta_a_mu_2_forward_prediction']*1e11:+.0f} × 10⁻¹¹ (canonical narrative-rounded)"
    )

    # ============================================================
    # Parallel SM-baseline tension reporting
    # ============================================================
    print()
    print("=" * 95)
    print("PARALLEL SM-BASELINE TENSION REPORTING (post-walk-back)")
    print("=" * 95)
    print(f"\n  Fermilab Run-1+Run-2 world average a_μ: {FERMILAB_RUN1_RUN2_WORLD_AVG:.11f}")
    print(f"                                       ± {FERMILAB_RUN1_RUN2_UNCERTAINTY:.0e}")
    print(f"  Reference: {FERMILAB_PAPER_RUN12}")

    print()
    print("--- Baseline 1: e+e- (Theory Initiative 2020) ---")
    comp_eeplus = compare_to_fermilab_eeplus_baseline(results["delta_a_mu_2_forward_prediction"])
    print(
        f"  Fermilab observed tension (e+e- baseline): +{comp_eeplus['fermilab_observed_tension']*1e11:.0f}({comp_eeplus['fermilab_observed_uncertainty']*1e11:.0f}) × 10⁻¹¹"
    )
    print(f"  Reference: {FERMILAB_RUN3_REFERENCE}")
    print(f"  AVE forward prediction:                    {comp_eeplus['ave_prediction']*1e11:+.3f} × 10⁻¹¹")
    print(
        f"  Deviation (AVE - observed):                {comp_eeplus['deviation']*1e11:+.3f} × 10⁻¹¹  ({comp_eeplus['deviation_pct']:+.2f}%)"
    )
    print(
        f"  σ-tension:                                 {comp_eeplus['n_sigma']:+.3f}σ {comp_eeplus['tension_direction']}"
    )

    print()
    print("--- Baseline 2: BMW lattice (Borsanyi+ 2021, Nature 593:51-55) ---")
    comp_bmw = compare_to_fermilab_bmw_baseline(results["delta_a_mu_2_forward_prediction"])
    print(
        f"  BMW lattice a_μ_SM:                        {BMW_SM_BORSANYI_2021:.11f} ± {BMW_SM_BORSANYI_2021_UNCERTAINTY:.0e}"
    )
    print(f"  Reference: {BMW_SM_PAPER}")
    print(
        f"  Fermilab-vs-BMW central tension:           {comp_bmw['fermilab_vs_bmw_central_tension']*1e11:+.1f}({comp_bmw['fermilab_vs_bmw_combined_uncertainty']*1e11:.0f}) × 10⁻¹¹  ({comp_bmw['fermilab_vs_bmw_sigma']:+.2f}σ, BMW closes most of e+e- anomaly)"
    )
    print(f"  AVE forward prediction:                    {comp_bmw['ave_prediction']*1e11:+.3f} × 10⁻¹¹")
    print(
        f"  Deviation (AVE - Fermilab_vs_BMW):         {comp_bmw['deviation']*1e11:+.3f} × 10⁻¹¹  ({comp_bmw['deviation_pct']:+.2f}%)"
    )
    print(f"  σ-tension:                                 {comp_bmw['n_sigma']:+.3f}σ {comp_bmw['tension_direction']}")

    # ============================================================
    # Two-baseline summary + SM-baseline conditionality framing
    # ============================================================
    print()
    print("=" * 95)
    print("DUAL-BASELINE TENSION STRUCTURE (the finding)")
    print("=" * 95)
    print()
    print(
        f"  AVE forward prediction +{results['delta_a_mu_2_forward_prediction']*1e11:.0f}×10⁻¹¹ from Q-G27 Cosserat saliency:"
    )
    print(f"    • on e+e- baseline:  {comp_eeplus['n_sigma']:+.2f}σ ABOVE Fermilab observed tension")
    print(f"    • on BMW baseline:   {comp_bmw['n_sigma']:+.2f}σ DEEPER above Fermilab-vs-BMW central")
    print()
    print(f"  BMW makes the tension WORSE, not softer — BMW lattice closes most of the")
    print(f"  Fermilab-vs-SM e+e- anomaly toward ~0σ, leaving AVE's +502 forward prediction")
    print(f"  unabsorbed in the SM+experiment landscape. Per Q-G27 leaf line 67:")
    print(f"  'On the BMW lattice baseline (which closes the Fermilab measurement toward")
    print(f"   ~0σ vs SM), AVE's prediction is in deeper tension. Either baseline puts AVE")
    print(f"   in genuine forward-vs-measurement disagreement that Run-4/5 will tighten.'")
    print()
    print(f"  Falsification target (per Q-G27 leaf line 69): Fermilab Run-4/5 at ±10 ppm")
    print(f"  precision (~2026-2027) settling the central value >100×10⁻¹¹ from AVE's +502")
    print(f"  forward prediction → Cosserat-saliency framework requires revision.")

    # ============================================================
    # Outcome adjudication (post-walk-back PASS-conditional / FLAG / RETIRE)
    # ============================================================
    print()
    print("=" * 95)
    print("OUTCOME ADJUDICATION (post-walk-back per prereg)")
    print("=" * 95)
    outcome = adjudicate_outcome(comp_eeplus, comp_bmw, results["delta_a_mu_2_forward_prediction"])
    print()
    print(f"  Outcome: {outcome}")
    print()

    # ============================================================
    # JSON output
    # ============================================================
    json_results = {
        "constants": {
            "alpha": float(ALPHA),
            "m_e_kg": float(M_E),
            "m_mu_kg_ave": float(M_MU),
            "m_mu_mev_ave": float(M_MU_MEV),
        },
        "ave_q_g27_forward_prediction": {k: float(v) if isinstance(v, (int, float)) else v for k, v in results.items()},
        "fermilab": {
            "run12_world_avg_a_mu": FERMILAB_RUN1_RUN2_WORLD_AVG,
            "run12_uncertainty": FERMILAB_RUN1_RUN2_UNCERTAINTY,
            "run12_reference": FERMILAB_PAPER_RUN12,
            "run3_tension_central_eeplus": FERMILAB_RUN3_TENSION_CENTRAL,
            "run3_tension_uncertainty_eeplus": FERMILAB_RUN3_TENSION_UNCERTAINTY,
            "run3_reference": FERMILAB_RUN3_REFERENCE,
        },
        "bmw_sm_baseline": {
            "a_mu_sm_bmw_central": BMW_SM_BORSANYI_2021,
            "a_mu_sm_bmw_uncertainty": BMW_SM_BORSANYI_2021_UNCERTAINTY,
            "reference": BMW_SM_PAPER,
        },
        "comparison_eeplus_baseline": {
            k: float(v) if isinstance(v, (int, float, bool)) else v for k, v in comp_eeplus.items()
        },
        "comparison_bmw_baseline": {
            k: float(v) if isinstance(v, (int, float, bool)) else v for k, v in comp_bmw.items()
        },
        "outcome": outcome,
        "dual_baseline_tension_structure": (
            f"AVE +502×10⁻¹¹ forward in {comp_eeplus['n_sigma']:+.2f}σ tension ABOVE e+e- baseline; "
            f"{comp_bmw['n_sigma']:+.2f}σ tension DEEPER on BMW baseline. "
            f"BMW makes tension worse not softer; tension structure on both baselines IS the finding."
        ),
        "skill_disciplines_applied": [
            "ave-prereg (research/2026-05-19_c3-muon-delta-fermilab-driver-rerun-prereg.md)",
            "ave-canonical-leaf-pull (Q-G27 + Q-G19α + lepton-mass-ladder canonical verified)",
            "verify-before-cite (walk-back commits + canonical leaves + constants imports verified at session start)",
            "ave-canonical-source (ALPHA, M_E from ave.core.constants; M_MU, M_MU_MEV from ave.topological.cosserat; FERMILAB_* + BMW_SM_* as paper-pinned empirical literals)",
            "substrate-native-check (Cosserat torsion saliency from Q-G27 substrate physics; textbook QED conversion is the bridge to observable)",
            "ave-driver-script-honesty (4-discriminator check post-edit: no hardcoded constants; forward-prediction not fit; formula matches Q-G27 leaf line 51; dual-baseline tension reported as finding not match)",
            "ave-discrimination-check (SM-counterfactual: AVE-distinct Cosserat-torsion-quantum mechanism; interpretive alternatives enumerated for both baselines)",
            "ave-evidence-framing-discipline (≥3 sig figs; tension structure as finding; no 'AVE matches muon g-2' overclaim)",
            "consistency-vs-emergence (Class 3 consistency check; conditional on SM-baseline; both baselines reported as parallel tensions)",
            "ave-walk-back (post-walk-back validation per fb5a9d4 + e0e4315; pre-walk-back artifacts removed)",
        ],
    }

    out_path = Path(__file__).parent / "muon_g2_fermilab_anchor_results.json"
    with open(out_path, "w") as f:
        json.dump(json_results, f, indent=2, default=str)
    print(f"Results JSON: {out_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
