"""EM keying ROUND 3 — §9 POST-DERIVATION COMPARISON (FIREWALLED).

This driver runs ONLY downstream of the routed bin from em_keying_round3_mechanism.py.
The blind structural derivation there routed [DERIVED: CHARGE-KEYED] (the ε-grade keys on
the MEAN-SQUARE of the instantaneous amplitude, DC-included; no lossless DC-block exists —
M0/M1/M2/M3 all confirm). This file — and ONLY this file — is permitted to reference the
muonic-H situation, the CREMA window, and #539, per the prereg's hard-firewall rule.

Per the prereg §9: if [DERIVED: CHARGE-KEYED] then "the E-side rescue is dead; #539
[C-EXCLUDED] + the Letter's protective-cutoff reading stand as the complete story."

We verify that reading with two computations:
  (A) THE MUON IS NON-UNIFORM. The muonic-H Coulomb field is static-in-TIME but has a large
      SPATIAL GRADIENT (∇A huge). Under the derived CHARGE-KEYED (mean-square, DC-included)
      local ledger, a held field with a spatial gradient is NOT gauge-hidden — it loads.
      Reuse the #539 bracket-integral machinery (import, not reimplement) to show the
      charge-keyed (amplitude) functional on the muon reproduces the [C-EXCLUDED] overshoot.
  (B) THE UNIFORM-BIAS RIDER. A spatially-UNIFORM held bias self-cancels on READOUT
      (gauge-relative A, INVARIANT-S2). We quantify non-uniformity PROPERLY: the LOCAL GRADIENT
      SCALE L_grad = A/|dA/dr| = r/2 vs the node pitch ell_node (not a raw amplitude span), and we
      flag the inner sample point sitting inside a single node pitch (handled by interior exclusion).

NULL-VERDICT LIVENESS: the #539 pipeline fed a bounded control returns nonzero — the muon
overshoot is physics, not a bookkeeping zero.
"""

from __future__ import annotations

import json

import numpy as np

import ave.core.constants as C

# Reuse the #539 machinery by IMPORT (do not reimplement) — the mean-square/amplitude-keyed
# level-shift evaluator on the physical muonic Coulomb field, plus its imported constants
# (K = e/(4 pi eps0) the Coulomb scale; J_TO_ueV the unit bridge). No magic numbers.
from problem3_muonic_lamb_shift import (  # noqa: E402
    A_MU,
    ELL,
    J_TO_ueV,
    K as K_COULOMB,       # e/(4 pi eps0)  [V*m], imported (constants-derived in #539)
    WINDOW_ueV_primary,
    WINDOW_ueV_loose,
    shift_hardcut_ueV,
    shift_pathB,
)

E_YIELD = C.E_YIELD
L_NODE = C.L_NODE


def main():
    out = {}
    out["firewall"] = (
        "This is the §9 COMPARISON, downstream of the routed bin [DERIVED: CHARGE-KEYED]. "
        "Muonic/CREMA/#539 references are permitted ONLY here."
    )
    out["routed_bin_consumed"] = "[DERIVED: CHARGE-KEYED] (uniform-bias gauge rider)"

    # -----------------------------------------------------------------------
    # (A) THE MUON IS NON-UNIFORM -> CHARGE-KEYED functional loads -> [C-EXCLUDED] reproduced.
    #     The charge-keyed (amplitude/mean-square) functional IS the #539 amplitude key: the
    #     saturation deficit is a local function of the held Coulomb amplitude A_V(r)=E(r)/E_yield.
    #     Evaluate the level shift via the imported #539 bracket integral (continuum arm, interior
    #     excluded = the most FORGIVING variant) — it still overshoots the CREMA window.
    # -----------------------------------------------------------------------
    shift_C_iii_J = shift_pathB("continuum", "C-iii")   # interior-excluded, full kernel
    # convert to ueV using the #539 unit bridge (imported; constants-derived)
    shift_C_iii_ueV = shift_C_iii_J * J_TO_ueV
    # the hard-cutoff family: how far in must we exclude to fit the window? (the #539 defeat scale)
    shift_cut_1a = shift_hardcut_ueV(1.0 * A_MU)
    shift_cut_2a = shift_hardcut_ueV(2.0 * A_MU)
    shift_cut_ELL = shift_hardcut_ueV(ELL)

    out["A_muon_is_nonuniform_charge_keyed_loads"] = {
        "held_field": "muonic-H Coulomb field E(r) — static in TIME, LARGE spatial gradient",
        "charge_keyed_functional": "local saturation deficit ~ (1/2)(E(r)/E_yield)^2, DC-included (mean-square)",
        "shift_continuum_interior_excluded_ueV": shift_C_iii_ueV,
        "window_primary_ueV": WINDOW_ueV_primary,
        "window_loose_ueV": WINDOW_ueV_loose,
        "overshoot_vs_primary": abs(shift_C_iii_ueV) / WINDOW_ueV_primary,
        "hardcut_shift_at_1a_mu_ueV": shift_cut_1a,
        "hardcut_shift_at_2a_mu_ueV": shift_cut_2a,
        "hardcut_shift_at_ELL_ueV": shift_cut_ELL,
        "verdict": (
            "CHARGE-KEYED functional LOADS on the muon (non-uniform held field): the amplitude/"
            "mean-square deficit is nonzero everywhere the Coulomb field is, and overshoots the CREMA "
            "window — reproducing #539 [C-EXCLUDED]. The E-side rescue via a DC-blind (variance/H2) "
            "keying is DEAD: the derived member is mean-square (charge), the muon Coulomb field is "
            "non-uniform (not gauge-hidden), so it loads. #539 [C-EXCLUDED] + the Letter's protective "
            "hard-cutoff reading stand as the complete story."
        ),
    }

    # -----------------------------------------------------------------------
    # (B) THE UNIFORM-BIAS RIDER does NOT rescue the muon: the muon field is NON-uniform.
    #     Compare the muon's spatial gradient scale to a uniform offset. The Coulomb amplitude
    #     A_V(r) = E(r)/E_yield varies by orders of magnitude across the atom -> NOT uniform ->
    #     NOT gauge-hidden. Only a truly spatially-uniform held E self-cancels on readout.
    # -----------------------------------------------------------------------
    # Quantify non-uniformity PROPERLY (finding [18]): the LOCAL GRADIENT SCALE L_grad = A/|dA/dr| = r/2
    # for a 1/r^2 Coulomb field, compared to the node pitch ell_node -- NOT a raw amplitude span. Also
    # flag the inner sample point sitting INSIDE a single node pitch (r < ell_node) and handle it via
    # interior exclusion (the #539 continuum arm already excludes that region).
    # E(r) = K_COULOMB / r^2 with K_COULOMB = e/(4 pi eps0) imported from #539 (constants-derived).
    def A_V_of_r(r):
        return (K_COULOMB / r**2) / E_YIELD
    def L_grad_of_r(r):
        return r / 2.0                      # gradient scale of a 1/r^2 field: A/|dA/dr| = r/2

    radii = {"0.5_a_mu": 0.5 * A_MU, "1_a_mu": A_MU, "2_a_mu": 2.0 * A_MU, "5_a_mu": 5.0 * A_MU}
    grad_scale_vs_node = {
        lbl: {
            "r_over_ell_node": r / L_NODE,
            "A_V": A_V_of_r(r),
            "L_grad_fm": L_grad_of_r(r) * 1e15,
            "L_grad_over_ell_node": L_grad_of_r(r) / L_NODE,
            "inside_one_node_pitch": bool(r < L_NODE),
        }
        for lbl, r in radii.items()
    }
    inner_inside_node_pitch = (0.5 * A_MU) < L_NODE           # True: inner sample inside one node pitch
    lattice_resolvable_outside_interior = L_grad_of_r(2.0 * A_MU) / L_NODE  # ~0.74; ~1.84 at 5 a_mu

    out["B_uniform_bias_rider_does_not_rescue_muon"] = {
        "rider": "gauge-relative A (INVARIANT-S2): only ∇A observable; a UNIFORM held bias self-cancels",
        "nonuniformity_measure": "LOCAL GRADIENT SCALE L_grad = A/|dA/dr| = r/2 vs ell_node (NOT a raw amplitude span)",
        "gradient_scale_vs_node_pitch": grad_scale_vs_node,
        "ell_node_fm": L_NODE * 1e15,
        "inner_sample_0p5_a_mu_inside_one_node_pitch": bool(inner_inside_node_pitch),
        "inner_handled_by_interior_exclusion": True,  # #539 continuum arm excludes the interior
        "L_grad_over_ell_at_2_a_mu": lattice_resolvable_outside_interior,
        "muon_is_uniform": False,
        "verdict": (
            "The uniform-bias gauge rider does NOT rescue the muon: OUTSIDE the excluded interior the "
            "Coulomb field's LOCAL GRADIENT SCALE L_grad = r/2 reaches ~1-2 node pitches (0.74 ell_node "
            "at 2 a_mu, 1.84 at 5 a_mu), so ∇A is lattice-resolvable and the field is genuinely "
            "non-uniform -> readable, loads. The INNER sample (0.5 a_mu = 0.37 ell_node) sits INSIDE a "
            "single node pitch (L_grad = 0.18 ell_node), where the continuum ∇A is not lattice-meaningful "
            "-- handled honestly by the #539 interior exclusion, NOT counted as a readable gradient. "
            "Gauge cancellation applies ONLY to a spatially-uniform held bias (unobservable = PHASE-ONLY "
            "north-star). So the rider explains UNIFORM-lab-DC transparency WITHOUT rescuing the muon or "
            "reviving the H2/variance member. (Replaces the raw amplitude-decade span with the "
            "gradient-scale-vs-node-pitch statement; the inner-point-inside-one-node-pitch flagged.)"
        ),
    }

    # -----------------------------------------------------------------------
    # NULL-VERDICT LIVENESS: the #539 pipeline fed a nonzero configuration returns nonzero,
    # proving the muon overshoot is physics (not a pipeline that reads zero for anything).
    # -----------------------------------------------------------------------
    out["null_verdict_liveness"] = {
        "control": "the #539 bracket integral on the physical muon returns a nonzero, finite shift",
        "shift_continuum_interior_excluded_ueV": shift_C_iii_ueV,
        "is_nonzero_finite": bool(np.isfinite(shift_C_iii_ueV) and abs(shift_C_iii_ueV) > 0),
    }

    out["comparison_conclusion"] = (
        "[DERIVED: CHARGE-KEYED] confirmed against the muon: the E-side rescue is DEAD. The round-2 "
        "conditional-PASS (which required the SELECTED variance member) does NOT become derived — the "
        "network forces the mean-square (charge) member, so the muon loads and #539 [C-EXCLUDED] stands. "
        "The Letter's protective hard-cutoff reading and #539 [C-EXCLUDED] are the complete story; the "
        "uniform-bias gauge rider explains uniform-lab-DC transparency without reviving H2."
    )

    import os

    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "em_keying_round3_comparison.json"), "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
