"""Run both yield-fork discriminator legs and write the combined JSON sidecar.

Usage:  <venv>/bin/python research/2026-07-19_yield-fork-discriminators/run_all.py
Writes: research/2026-07-19_yield-fork-discriminators_result.json
"""

from __future__ import annotations

import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leg_a_thixotropy as leg_a  # noqa: E402
import leg_b_loop_area as leg_b  # noqa: E402


def main() -> None:
    a = leg_a.run()
    b = leg_b.run()

    fork = {
        "fork_question": (
            "finite-area memristive loop (dissipative) vs zero-area saturating "
            "reactance (lossless) at the near-yield crossing"
        ),
        "fork_record": "research/2026-07-17_regime-iv-dissipation-audit.md sec5",
        "grant_lean": "reversible-reactive (recorded as a lean; fork OPEN; ruling stays Grant's)",
        "leg_A_verdict": a["final_verdict"],
        "leg_B_verdict": b["adjudication"],
        "leg_B_peak_rS": b["peak_rS"]["peak_refined"],
        "leg_B_peak_VI": b["peak_VI"]["peak_refined"],
        "leg_B_loop_area_at_peak": b["peak_rS"]["area_at_peak"],
        "leg_B_zero_tolerance": b["zero_tolerance"]["tol"],
        "combined_for_grant": (
            "Leg A: canonical kernel has NO genuine sign(dr/dt) memory and is dissipative -> "
            "rectification-thrust door CLOSED (B); bin A (reactive rectifier) is unreachable in the "
            "first-order framework and requires the second-order reactive = Flag F = lossless branch. "
            "Leg B: the loop area is FINITE (not zero) and Debye-shaped, but the (r,S)-plane peak sits "
            "at wt~1.0 (linear value), OUTSIDE the P_phase5 [0.85,0.95] window -> NEITHER/fail-closed; "
            "the P_phase5 nonlinear peak-shift to 0.9 is NOT reproduced in its stated plane. NEITHER "
            "leg adjudicates the fork against Grant's lean: both relocate the crux to Flag F (first-order "
            "overdamped [dissipative] vs second-order reactive [lossless]), a DERIVATION question upstream "
            "of the drivers. Fork stays OPEN; routed to Grant."
        ),
    }

    out = {
        "run_date": "2026-07-19",
        "lane": "yield-fork discriminators (implementer)",
        "branch": "feat/yield-fork-discriminators",
        "engine_meter": "byte-UNTOUCHED; kernel byte-locked to src/ave/core/k4_tlm.py:283,291",
        "leg_A": a,
        "leg_B": b,
        "fork_adjudication_for_grant": fork,
    }

    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    dest = os.path.join(repo_root, "2026-07-19_yield-fork-discriminators_result.json")
    def _default(o):
        if isinstance(o, np.bool_):
            return bool(o)
        if isinstance(o, np.integer):
            return int(o)
        if isinstance(o, np.floating):
            return float(o)
        raise TypeError(f"not serializable: {type(o)}")

    with open(dest, "w") as f:
        json.dump(out, f, indent=2, default=_default)
    print("wrote", dest)
    print("\nLeg A verdict:", json.dumps(fork["leg_A_verdict"]["bin"]))
    print("Leg B verdict:", json.dumps(fork["leg_B_verdict"]["bin"]))
    print("Leg B (r,S) peak:", round(fork["leg_B_peak_rS"], 4), " (V,I) peak:", round(fork["leg_B_peak_VI"], 4))


if __name__ == "__main__":
    main()
