# Vacuum-Birefringence COEFFICIENT Discriminator — RESULT

**Status:** RESULT (2026-06-04). Part B of ledger §5 (`_orchestration/experimental/2026-06-04_round2-adjudications.md`). Companion to the prereg `research/2026-06-04_birefringence-coefficient-prereg.md` and the forward driver `src/scripts/vol_4_engineering/birefringence_coefficient_discriminator.py`. Branch `analysis/2026-06-04-birefringence-coefficient-reframe`.
**Verdict:** the vacuum-birefringence test **SURVIVES** the √ε correction (Part A) with a stronger COEFFICIENT discriminator. AVE predicts an index shift `~10⁶×` the QED Euler-Heisenberg baseline, AVE-distinct at ALL fields, measurable at facility-class fields.
**Lane:** implementer.

---

## §1 — Headline

The vacuum-birefringence kill-switch (clm-pp3qwf) was **re-framed, not retracted**. Two findings:

1. **Determinate correction (Part A, commit `ad26d357`).** The leaf had mislabeled the permittivity saturation DEPTH `1−S = +A²/2` as the refractive-index shift `Δn`. The actual index shift, via the wave-speed identity `n = √(ε_eff/ε₀) = √S`, is `δn = √S − 1 ≈ −A²/4` (negative; the vacuum softens). Both `1−S` and `δn` are **E²-leading** — so the shipped claim "Δn ∝ E⁴; an E² slope falsifies AVE" was mathematically wrong. Killed at 5 sites including the shipped vol_9 datasheet.

2. **The surviving discriminator is the COEFFICIENT.** Both AVE and QED give an E²-leading index shift; the leading *exponent* carries no discriminating power. The discriminator is the *coefficient*:
   - AVE: `δn = −¼(E/E_yield)²`, an **O(1)** coefficient against the un-suppressed yield field `E_yield ≈ 1.13×10¹⁷ V/m`.
   - QED: `δn ≈ a_EH α²(E/E_crit)²`, an **α²-loop-suppressed** coefficient against the Schwinger field `E_crit ≈ 1.32×10¹⁸ V/m`.
   - **Ratio `δn_AVE/δn_QED = 1/(4 a_EH α³) ~ 10⁶`, field-INDEPENDENT.**

**The corpus undersold this test.** The prior framing made it a facility-only, regime-gated, exponent-fitting test with a `±0.5`-in-exponent target. The corrected framing makes it a `~6` OOM coefficient gap present at *every* field — a far stronger and cleaner AVE-distinct handle.
