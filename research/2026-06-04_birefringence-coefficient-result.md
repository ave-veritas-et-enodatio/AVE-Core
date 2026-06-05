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

---

## §2 — The derivation, reproduced by the forward driver

The driver (`birefringence_coefficient_discriminator.py`) computes everything forward from `ave.core.constants`; the QED Euler-Heisenberg prefactor is the only non-AVE input (labeled literature, not fit). Validated output (`PYTHONPATH=src python3 ...`):

### 2.1 The substrate identity (the field-scale gap is an α-power)

```
E_CRIT == V_SNAP/L_NODE         : True   (V_SNAP/L_NODE = 1.32329e+18 V/m)
E_YIELD == sqrt(ALPHA)*E_CRIT   : True
(E_CRIT/E_YIELD)^2 = 137.036    vs   1/ALPHA = 137.036   [match: True]
```

This is the key structural result. `E_crit = m_e²c³/(eℏ) = V_SNAP/L_NODE` exactly (Schwinger field = snap-voltage per node-length), and `E_yield = V_YIELD/L_NODE = √α·V_SNAP/L_NODE = √α·E_crit`. Therefore `(E_crit/E_yield)² = 1/α` **exactly** — the gap between the AVE yield field and the QED Schwinger field is *itself* an α-power, not an independent number.

### 2.2 The AVE index shift (manifestation of Axiom 4)

```
   E (V/m)   A=E/E_yield   dn_AVE(exact)   dn_AVE(lead)
  1.00e+13    8.8463e-05    -1.9564e-09    -1.9564e-09
  1.00e+14    8.8463e-04    -1.9564e-07    -1.9564e-07
  1.00e+16    8.8463e-02    -1.9622e-03    -1.9564e-03
  3.00e+16    2.6539e-01    -1.8093e-02    -1.7608e-02
```

`δn = √S − 1 = (1−A²)^¼ − 1`, NEGATIVE (the vacuum softens), E²-leading. The exact-arc and leading-term agree to ~3 sig figs below `E = 10¹⁶ V/m`; the arc steepens near yield (the higher-order `−3A⁴/32` term).

### 2.3 The ratio (field-INDEPENDENT)

```
leading-term ratio across the sweep (a_EH=0.1556): min=4.1358e+06  max=4.1358e+06
field-INDEPENDENT (leading): True  ->  constant = 4.1358e+06 = 1/(4 a_EH alpha^3)
```

`δn_AVE/δn_QED = 1/(4 a_EH α³)`, constant in E to the leading-term approximation. This is the whole point: a *coefficient* discriminator, present identically at every field — not an exponent or regime gate.
