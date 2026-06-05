#!/usr/bin/env python3
"""
AVE Falsification Surface — the round-2-hardened survivors
==========================================================
Prints the HONEST experimental falsification surface of the Applied Vacuum
Engineering framework, AFTER the 2026-06-04 round-2 adversarial hardening.

The earlier "4 binary tabletop kill switches" framing is SUPERSEDED:
  - Sagnac (Ψ≈7.15)            → RETIRED (corroborative-null; RLG geodesy excludes
                                  the Earth-rotor bias ~7e4×; the Ψ-ratio is not a
                                  discriminator — GR scales with density too).
  - "C/C₀→∞ at 43 kV"          → per-node conflation (apparatus voltage read as the
                                  per-node yield; the vacuum per-node A at 43 kV is
                                  ~1e-9). The plateau is facility-class (~1e16 V/m),
                                  not a 43 kV bench. PONDER-05 = quartz material.
  - Cleave "SM = 0.0 mV"       → FALSE (contact-potential gives a gap-dependent
                                  charge); the discriminator is the gap-INDEPENDENT
                                  4-corner symmetry, not "presence vs 0".
  - HOPF medium-indep/enantiomer → CONSISTENCY-class (form-shared with classical
                                  reciprocal-Pasteur chiral media); the surviving
                                  AVE-distinct leg is the 2-port reciprocity sweep.

The recurring lesson: an AVE-distinct falsifier survives only when it is a
SYMMETRY / SIGN / zero-free-parameter corner classical physics is forbidden to
enter AND a bench can reach — not a magnitude.

References:
  - README.md  "Experimental Falsification"
  - manuscript/ave-kb/claim-quality-closure-roadmap.md  §0.5
  - _orchestration/experimental/2026-06-04_round2-adjudications.md
Detailed forward drivers:
  - src/scripts/vol_4_engineering/birefringence_coefficient_discriminator.py
  - src/scripts/vol_4_engineering/qg42_vsign_deltaf.py

Run:
    python src/scripts/run_kill_switches.py

All AVE arithmetic imports canonical constants (src/ave/core/constants.py);
no fit-to-target, no magic numbers. Non-AVE literature inputs (the QED
Euler-Heisenberg prefactor; the bench readout capacitance) are labeled.
"""
from ave.core.constants import ALPHA, E_CRIT, E_YIELD, V_YIELD, XI_TOPO

BOLD, CYAN, GREEN, YELLOW, RED, RESET = (
    "\033[1m", "\033[96m", "\033[92m", "\033[93m", "\033[91m", "\033[0m",
)


def header(title: str) -> None:
    print(f"\n{'=' * 76}\n{BOLD}{CYAN}{title}{RESET}\n{'=' * 76}")


def result(label: str, value: str, unit: str = "") -> None:
    print(f"  {GREEN}→{RESET} {label}: {BOLD}{value}{RESET}{(' ' + unit) if unit else ''}")


def compare(ave_val: str, sm_val: str) -> None:
    print(f"  {YELLOW}AVE-distinct:{RESET} {ave_val}")
    print(f"  {RED}Standard:   {RESET} {sm_val}")


def falsifier_1_cleave() -> None:
    header("FALSIFIER 1 — Axiom 2 (ξ_topo): Cleave-01 + gap-sweep   [NEAR-TERM BENCH ~$7.7k]")
    C_IN = 10e-12  # bench readout capacitance, F (engineering literal — NP0/C0G)
    mv_per_um = (XI_TOPO * 1e-6 / C_IN) * 1e3  # (e/ℓ_node) × 1µm / C_in → mV
    result("Charge-floor slope ξ_topo = e/ℓ_node", f"{XI_TOPO:.4e}", "C/m")
    result("Voltage floor (C_in = 10 pF)", f"{mv_per_um:.3f}", "mV/μm")
    print("  AVE-distinct signature: the floor is GAP-INDEPENDENT — it survives a ≥4×")
    print("  gap-sweep. Classical fakers (contact-potential / electrostriction / tribo)")
    print("  are gap-DEPENDENT (∝ 1/g²); the gap-independence corner is the one none can fake.")
    compare(f"a gap-independent floor (~{mv_per_um:.0f} mV/μm) surviving the gap-sweep",
            "a gap-DEPENDENT contact-potential background (SM is NOT 0 — round-2 CPD correction)")


def falsifier_2_hopf() -> None:
    header("FALSIFIER 2 — Axiom 1 (chiral lattice): HOPF 2-port reciprocity   [CHEAP ~$123]")
    print("  Test: |S21| vs |S12| on the existing HOPF-02a board — field off, non-magnetic,")
    print("  power-independent, full 2-port SOLT, null floor 0.05 dB (do NOT relax post-hoc).")
    print("  NB the medium-independence + enantiomer-sign legs are CONSISTENCY-class")
    print("  (reciprocal-Pasteur); the genuine non-reciprocity is corpus-tied to the")
    print("  above-yield regime, so the linear bench likely reads reciprocal.")
    compare("a passive, zero-field, power-independent non-reciprocity |S21| ≠ |S12| (> 0.05 dB)",
            "|S21| = |S12| (reciprocal) — classically forbidden to break without a magnet")


def falsifier_3_qg42() -> None:
    header("FALSIFIER 3 — Axiom 4 (saturation SIGN): Q-G42 autoresonant V²   [FORWARD]")
    result("Tree-level Δf₀/f₀ sign — AVE", "+ (vacuum softens → resonance RISES)")
    result("Tree-level Δf₀/f₀ sign — QED", "− (vacuum stiffens, Euler-Heisenberg)")
    print("  AVE-distinct signature: the SIGN is robust to the √α magnitude uncertainty.")
    print("  Magnitude form Δf₀/f₀ = +¼·A_RMS²·η_eff (see qg42_vsign_deltaf.py).")
    compare("Δf₀/f₀ > 0 (softening)", "Δf₀/f₀ < 0 (stiffening)")


def falsifier_4_birefringence() -> None:
    header("FALSIFIER 4 — Axiom 4 (saturation COEFFICIENT): vacuum birefringence   [FACILITY]")
    a_EH = 7.0 / 45.0  # QED Euler-Heisenberg single-mode prefactor (LITERATURE input)
    # Substrate identity (E_crit/E_yield)² = 1/α (since E_yield = √α·E_crit) collapses the
    # field dependence: δn_AVE/δn_QED = (1/4)/(a_EH·α²) · (E_crit/E_yield)² = 1/(4·a_EH·α³).
    ratio = 1.0 / (4.0 * a_EH * ALPHA**3)
    result("AVE index shift", f"−¼·(E/E_yield)²   [O(1) coeff; E_yield ≈ {E_YIELD:.2e} V/m]")
    result("QED index shift", f"a_EH·α²·(E/E_crit)²   [α²-suppressed; E_crit ≈ {E_CRIT:.2e} V/m]")
    result("AVE / QED coefficient ratio", f"{ratio:.2e}", "× (field-INDEPENDENT)")
    print("  AVE-distinct signature: a vacuum index shift ~10⁶× QED's at any field. BOTH are")
    print("  E²-leading — the discriminator is the COEFFICIENT, not an 'E² vs E⁴ exponent'")
    print("  (the prior exponent framing was a √ε conflation; corrected round-2).")
    compare(f"δn ~ {ratio:.0e}× QED at high-intensity-laser fields (~1e16 V/m)",
            "QED-sized (α²-suppressed) coefficient")


def falsifier_5_u0() -> None:
    header("FALSIFIER 5 — single-parameter (Ω_freeze): the u₀* three-route check   [FRAMEWORK]")
    print("  α, G, and 𝒥_cosmic must all land at the SAME operating point u₀* set by Ω_freeze.")
    print("  Honest scope: the α-route is a NAMED geometric identification (α⁻¹=4π³+π²+π —")
    print("  the substrate does not independently select it); the G and 𝒥_cosmic routes are")
    print("  framework-structural, quantitatively open. The three-route CONSISTENCY is the")
    print("  falsifier; 'all derive from Ω_freeze' is not claimed.")


def main() -> None:
    header("AVE FALSIFICATION SURVIVORS — round-2-hardened (2026-06-04)")
    print("  The pre-2026-06 '4 binary kill switches' framing is superseded (see module")
    print("  docstring + README). Survivors below — symmetry/sign/zero-free-param corners")
    print(f"  survive; magnitudes deflate. (α⁻¹ = {1.0 / ALPHA:.6f} is a named identification.)")
    falsifier_1_cleave()
    falsifier_2_hopf()
    falsifier_3_qg42()
    falsifier_4_birefringence()
    falsifier_5_u0()
    header("SUMMARY")
    print("  Near-term bench : Cleave (gap-independent 4-corner) + HOPF reciprocity sweep")
    print("  Forward/facility: Q-G42 V²-sign · vacuum birefringence coefficient (~10⁶× QED)")
    print("  Framework-level : the u₀* three-route check")
    print("  NO deprecated framings (Sagnac Ψ=7.15, C/C₀→∞ at 43 kV, SM=0.0 mV) are computed.")


if __name__ == "__main__":
    main()
