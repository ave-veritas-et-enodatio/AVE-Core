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

---

## §3 — The prefactor band (⚑ flag-don't-fix)

The headline ratio rides on the QED Euler-Heisenberg prefactor `a_EH`, which is convention-dependent (single-mode vs differential vs order-of-magnitude). The structural form `1/(4 a_EH α³)` is exact; the number spans ~1 OOM:

```
a_EH convention                     a_EH   ratio 1/(4 a alpha^3)
single-mode parallel  (7/45)      0.1556              4.1358e+06
single-mode perp      (4/45)      0.0889              7.2376e+06
differential birefr.  (3/45)      0.0667              9.6502e+06
prefactor-1 reference (a=1)       1.0000              6.4335e+05
order-of-mag EH       (~1.5)      1.5000              4.2890e+05
=> headline band: [4.29e+05, 9.65e+06]
```

**The ledger §5 / dispatch headline "~4.4×10⁵×" (with worked `δn_QED ≈ 4.5×10⁻¹³ at 10¹⁴ V/m`) corresponds to the `a_EH ≈ 1.5` (order-of-magnitude EH) end of the band**, NOT the textbook single-mode `7/45` (which gives `δn_QED ≈ 4.7×10⁻¹⁴` and ratio `4.1×10⁶`). Per flag-don't-fix, I did NOT silently collapse to one number:
- The reframed corpus leaves (Part A) state **"`~10⁶`"** — robust across the entire band, `ave-evidence-framing-discipline`-correct until the convention is pinned.
- The driver reports the **full band** so the corpus headline can be pinned (Grant/auditor decision) without re-running.
- **The physics verdict is identical at every point in the band:** AVE is `~10⁵–10⁶×` QED, a `~6` OOM gap. The ~1-OOM prefactor spread is immaterial to the discrimination (the verdict has ~6 OOM of margin).

**Decision surfaced (not resolved):** which `a_EH` convention the corpus headline pins. Recommend the single-mode `7/45` (the standard textbook weak-field birefringence coefficient, most defensible as a literature citation) → headline `~4×10⁶`; OR keep the convention-free "`~10⁶`" framing already landed in the leaves. The "4.4×10⁵" figure should NOT be quoted as if it were the single-mode value.

---

## §4 — Measurability + classification

### 4.1 Measurability verdict: MEASURABLE at facility-class fields

```
E=1.00e+13 V/m -> |dn_AVE|=1.956e-09  (SNR vs ~1e-15 floor 1.96e+06)  [MEASURABLE]
E=1.00e+14 V/m -> |dn_AVE|=1.956e-07  (SNR 1.96e+08)                   [MEASURABLE]
E=1.00e+16 V/m -> |dn_AVE|=1.962e-03  (SNR 1.96e+12)                   [MEASURABLE]
```

At `E ~ 10¹⁴ V/m` (extreme-laser-reachable; ELI/petawatt-class focal fields), `δn_AVE ≈ 2.0×10⁻⁷` — well above a representative high-finesse-cavity index-shift floor `~10⁻¹⁵`. The QED baseline there is `~5×10⁻¹⁴`, so the `~10⁶` coefficient gap is the AVE-distinct margin. **The test is facility-class but the AVE signal is comfortably measurable; the discrimination lives in the coefficient, present at all fields, not in reaching a near-yield regime.**

### 4.2 Classification (`consistency-vs-emergence`)

| Quantity | Class | Note |
|---|---|---|
| `δn_AVE = √S − 1 ≈ −A²/4` | **manifestation** of Axiom 4 | the wave-speed identity `n=√(ε/ε₀)` on the Ax-4 kernel; not a fit, not a CODATA-substitution identity. |
| `(E_crit/E_yield)² = 1/α` | **identity** (structural) | algebraic from the constant definitions (`V_yield=√α V_snap`, `E_crit=V_snap/L_node`). |
| ratio `1/(4 a_EH α³)` | **discriminating forward prediction** | AVE-distinct: un-suppressed (tree-level saturation) vs QED loop-suppressed (α²). Differs from QED by `~10⁶`. |

**Headline-class verdict:** the coefficient ratio is a *discriminating forward prediction*, two-sided. NOT headlined as "α emerges" — α enters as an *input* (the QED loop factor and the substrate-field identity both carry α); what is AVE-distinct is the *un-suppressed-vs-suppressed contrast*, a `~6` OOM coefficient gap.
