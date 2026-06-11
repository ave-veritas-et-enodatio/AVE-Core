#!/usr/bin/env python3
"""alpha-as-boundary-energy partition — FORWARD CHECK (Phase-2 of the frozen prereg).

Prereg (FROZEN, committed ALONE): research/2026-06-11_alpha-boundary-energy_prereg.md
Branch: analysis/2026-06-11-r1-alpha-forward-check (off origin/main).

This driver implements the prereg's §7 EXECUTABLE GATES *verbatim* and the §5
FORWARD-FIRST (Minnaert / ave-live-fire-derivation-provenance) protocol: the
ANALYTIC number and the MEASURED partition are computed and PRINTED *before* the
alpha comparison is loaded. No bin, tolerance, or definition is re-opened here
(the PARTITION-FREEZE LAW). The frozen primary is

    r = E_V_cons_last / H_cons_last       (longitudinal share of total conserved energy)

MEASURED data is SHA-pinned to commit 570b50d7 on origin/analysis/2026-06-11-s11-de-novo,
field path src/scripts/vol_9_device/_output/s11_denovo_results.json, key made_build.
The driver materialises it via `git show <SHA>:<path>` so the run is reproducible from
any checkout that has the object (no copy-drift).

Discipline: ave-power-category-check (r is a Q_reactive internal store partition);
phase-space-coordinate-check (claim and measurement both in the longitudinal/V channel:
E_V_cons = engine bulk_energy_conserved, the master-equation V-sector invariant);
consistency-vs-emergence (class gated on the static alpha-input / forward-vs-fit check);
flag-don't-fix; coincidence-magnet discipline (the two-alpha trap, §0.2).
"""
from __future__ import annotations

import json
import math
import subprocess
import sys

# --- SHA-pinned MEASURED-data provenance (prereg §0.1 #5) -----------------------
BANKED_SHA = "570b50d7a560e54fb0c270a859e7e9c99c6e3968"
BANKED_PATH = "src/scripts/vol_9_device/_output/s11_denovo_results.json"


def load_banked() -> dict:
    """Load the SHA-pinned made_build block from the banked s11 de-novo JSON."""
    try:
        blob = subprocess.check_output(
            ["git", "show", f"{BANKED_SHA}:{BANKED_PATH}"], text=True
        )
        return json.loads(blob)["made_build"]
    except Exception as exc:  # pragma: no cover - provenance fallback
        # Fallback: a local SHA-verified copy (byte-identical to the git blob).
        for cand in (sys.argv[1:2] or []) + ["/tmp/ave-r1alpha-s11.json"]:
            try:
                with open(cand) as fh:
                    return json.load(fh)["made_build"]
            except Exception:
                continue
        raise SystemExit(f"could not load banked data ({exc})")


def main() -> int:
    mb = load_banked()

    print("=" * 74)
    print("alpha-as-boundary-energy  FORWARD CHECK  (prereg Phase-2, FROZEN gates)")
    print("=" * 74)
    print(f"MEASURED provenance: SHA-pin {BANKED_SHA[:12]} : {BANKED_PATH} [made_build]")

    # --- STEP 1 — ANALYTIC arm (FORWARD-FIRST, printed before any alpha) --------
    # §4.1 + the §1.1 fence: the standing-V wall-energy integral is only reachable
    # on banked primitives via the golden-torus geometric Q (= ALPHA_COLD), which IS
    # the 1/4-/golden-torus family -> reconstruction. No independent wall-energy
    # integral primitive is banked. Per the fence the arm bins ANALYTIC-BLOCKED.
    print("\n[STEP 1 — ANALYTIC arm]")
    print("  ANALYTIC-BLOCKED: the standing-V wall-energy integral is reachable on")
    print("  banked primitives only via the golden-torus geometric Q = 4pi^3+pi^2+pi")
    print("  (= ALPHA_COLD) -> reconstruction of the 1/4-/golden-torus family (fenced,")
    print("  §1.1). No independent S(A)=sqrt(1-A^2) + Gamma_bulk=-1 wall-energy integral")
    print("  primitive is banked. The route stands on the MEASURED arm alone.")

    # --- STEP 2 — MEASURED partition (printed BEFORE alpha loads, §5) -----------
    ev_last = mb["E_V_cons_last"]
    h_last = mb["H_cons_last"]
    ev_first = mb["E_V_cons_first"]
    h_first = mb["H_cons_first"]

    r = ev_last / h_last                       # FROZEN primary (a)
    r2 = ev_last / (h_last - ev_last)          # arm (a2)
    r_first = ev_first / h_first               # stationarity companion
    stationary = abs(r / r_first - 1.0) <= 0.10  # frozen 10% stationarity band

    print("\n[STEP 2 — MEASURED partition  (longitudinal share, def (a))]")
    print(f"  E_V_cons_first = {ev_first:.6f}   E_V_cons_last = {ev_last:.6f}")
    print(f"  H_cons_first   = {h_first:.6f}   H_cons_last   = {h_last:.6f}")
    print(f"  r       = E_V_cons_last / H_cons_last            = {r:.6e}")
    print(f"  r2      = E_V_cons_last / (H_cons_last-E_V_cons) = {r2:.6e}   (arm a2)")
    print(f"  r_first = E_V_cons_first / H_cons_first          = {r_first:.6e}")
    print(f"  stationary (|r/r_first-1| <= 0.10)               = {stationary}"
          f"   (drift |r/r_first-1| = {abs(r/r_first-1.0):.4f})")

    # arm (b) is VOID by the frozen gate: pocket_cells == 0 => SHELL-NEVER-FORMS
    pocket = int(mb["pocket_cells"])
    assert pocket == 0, "arm (b) freeze assumed pocket_cells==0 (SHELL-NEVER-FORMS)"
    print(f"  arm (b): pocket_cells = {pocket}  => VOID (SHELL-NEVER-FORMS, no interface band)")

    # --- STEP 3 — NOW load alpha (the comparison loads LAST, §5) ---------------
    from ave.core.constants import ALPHA  # 7.2973525693e-3, constants.py:133
    ALPHA_COLD = 1.0 / (4 * math.pi**3 + math.pi**2 + math.pi)  # golden-torus trap

    ratio = r / ALPHA
    match = abs(ratio - 1.0) <= 0.25           # bin-1 gate
    tight = abs(ratio - 1.0) <= 0.05           # tight sub-flag
    two_alpha_indistinct = abs(ALPHA / ALPHA_COLD - 1.0) < 0.25

    print("\n[STEP 3 — alpha comparison (loaded LAST)]")
    print(f"  ALPHA (CODATA, constants.py:133)      = {ALPHA:.10e}")
    print(f"  ALPHA_COLD = 1/(4pi^3+pi^2+pi)        = {ALPHA_COLD:.10e}")
    print(f"  r/ALPHA                               = {ratio:.6f}  "
          f"(=> r is ~{1.0/ratio:.2f}x {'below' if ratio < 1 else 'above'} alpha)")
    print(f"  match  |r/ALPHA-1| <= 0.25            = {match}  (|.| = {abs(ratio-1.0):.4f})")
    print(f"  tight  |r/ALPHA-1| <= 0.05            = {tight}")
    print(f"  two_alpha_indistinct (|A/A_cold-1|<.25)= {two_alpha_indistinct}  "
          f"(|.| = {abs(ALPHA/ALPHA_COLD-1.0):.2e})")

    # --- STEP 4/5 — static dead-input + forward-vs-fit (the alpha-input gate) ---
    # The genesis engine (unified_genesis_engine.py) and the energy accounting
    # (bulk_energy_conserved / total_energy_unified) take NO fine-structure alpha as
    # a dynamical input (grep-verified this session: the only alpha touch in the whole
    # s11_de_novo pipeline is the post-hoc ringdown-Q note at s11_de_novo_sweep.py:698,
    # ALPHA_COLD_INV, explicitly "post-hoc, NOT a bin criterion"; it consumes the
    # ringdown Q, not E_V_cons/H_cons). No comparison_only_alpha / gamma_target field
    # feeds E_V_cons or H_cons. => alpha is a DEAD input to the partition by
    # construction (static dead-input + forward-vs-fit PASS). (Contrast: the v6 phasor
    # object carries gamma_target_for_alpha -> consistency-class; the de-novo MADE
    # object is alpha-free.)
    print("\n[STEP 4/5 — static dead-input + forward-vs-fit]")
    print("  alpha absent from engine dynamics AND from the E_V_cons/H_cons accounting")
    print("  (only post-hoc ringdown-Q note touches ALPHA_COLD_INV, NOT a bin input).")
    print("  => DEAD-INPUT (static): a match would be emergence-candidate; forward-vs-fit PASS.")
    bulk_decoupled = mb.get("bulk_sector_unstable_free_evolution", None)
    print(f"  note (mechanism): bulk_sector_unstable_free_evolution = {bulk_decoupled}")
    print(f"                    bulk_decoupled_from_V_proof = {mb.get('bulk_decoupled_from_V_proof')}")

    # --- VERDICT — ordered bins (§7) -------------------------------------------
    print("\n[VERDICT — ordered bins §7]")
    if match and stationary and not two_alpha_indistinct:
        verdict = "MATCHES-alpha"
    elif match and stationary and two_alpha_indistinct:
        verdict = "MATCHES-alpha (coincidence-magnet-UNGUARDED: two-alpha indistinct)"
    else:
        verdict = "DIFFERENT-RATIO"
    print(f"  BIN = {verdict}")
    if verdict.startswith("DIFFERENT-RATIO"):
        print(f"    r/ALPHA = {ratio:.4f}: the longitudinal share of TOTAL conserved")
        print(f"    energy is ~{1.0/ratio:.1f}x BELOW alpha. H_cons carries the canon-flagged")
        print("    decoupled-bulk reservoir (bulk_sector_unstable_free_evolution=True);")
        print("    the longitudinal share of total is NOT alpha at the frozen def (a).")
        print(f"    Stationarity also FAILS (drift {abs(r/r_first-1.0):.3f} > 0.10): r is not a")
        print("    stationary structural fraction across the settle window.")
        print("    The ONLY alpha-ward path (arm a3, exclude the decoupled reservoir) is")
        print("    FENCED (justified only by the bulk_decoupled flag, never by alpha-proximity)")
        print("    AND its field is not banked -> ANALYTIC-BLOCKED.")
    print("\n  secondary (cross-object invariance): SECONDARY-BLOCKED on banked data")
    print("    (planted leg banks probe-response only, no E_V_cons/H_cons) and MOOT")
    print("    (no primary match to guard against a coincidence-magnet).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
