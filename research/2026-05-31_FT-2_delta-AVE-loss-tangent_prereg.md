# Prereg — FT-2: forward-derive water tan δ at 1 GHz from S(A) (lift δ_AVE to predictive)

**Date**: 2026-05-31
**Branch**: `analysis/statistics-under-ave-definition` (off `main` @ 7529f7ce, isolated worktree)
**Status**: PREREG FROZEN — corpus inventory complete; derivation NOT executed (execution gated, see §7).
**Parent**: [`2026-05-31_statistics-under-ave_prereg_and_corpus_audit.md`](2026-05-31_statistics-under-ave_prereg_and_corpus_audit.md) §6 FT-2; leaf [`common/statistics-under-ave.md`](../manuscript/ave-kb/common/statistics-under-ave.md) §8.

**Skills fired**: `ave-prereg` (this prereg + corpus inventory below); `ave-canonical-leaf-pull` (S(A)/loss machinery enumerated); `ave-power-category-check` (LOAD-BEARING — see §6 guard); `substrate-native-check`; `ave-canonical-source` (canonical primitives, no round numbers); `consistency-vs-emergence` (target = lift δ_AVE Class-1→Class-4 emergence); `ave-evidence-framing-discipline`; `verify-before-cite` (load-bearing citations re-verified at execution).

---

## §1 — Target

Forward-predict the dielectric loss tangent **tan δ of liquid water at 1 GHz** from the AVE saturation kernel `S(A) = √(1 − (A/A_yield)²)` + the `δ_AVE = t_sat/t_period` structure, with **no datasheet loss input** — concretely, replace the hard-coded `eps_imag = 10.0` literal in `src/scripts/vol_4_engineering/knot_water_amplification_mechanisms.py:234` with a kernel-derived value. Success lifts `δ_AVE` (clm-f0jwtk) from **Class-1 definitional/taxonomic to a falsifiable Class-4 predictor** and closes the formally-open strengthen-by item (§3).

## §2 — Physical picture (mechanical, pre-derivation)

- Water at 1 GHz = H-bond-network LC tanks driven by the EM field. The Debye relaxation loss is, in AVE terms, the fraction of each drive cycle the local bond amplitude `A(t)` spends **above the yield/saturation threshold** (Γ→−1), where the substrate flips from reactive (lossless) to absorptive (real-power Joule dissipation).
- `δ_AVE = t_sat/t_period` **is** the loss tangent in the small-loss limit: `tan δ ≈ δ_AVE`, both being the dissipative/reactive ratio per cycle.
- Derivation arc: integrate `t_sat(A₀, ω)` = time-above-yield per drive cycle from `S(A)` → map to `σ`/`ε''` → `tan δ` → compare to measured (the driver implies `tan δ = ε''/ε' = 10/80 ≈ 0.125` at 1 GHz).
- Scaling intuition: below yield → `t_sat = 0` → lossless. The Debye loss peak is where `t_sat/t_period` is maximized as drive frequency sweeps against the bond relaxation.

## §3 — Corpus state: OPEN (formally registered), ~70% scaffolding exists

Per the 2026-05-31 corpus-grep inventory (file:line from inventory; load-bearing ones re-verified at execution):

**The target is a formally-OPEN, unclaimed item** — `.index/strengthen-by.jsonl:221` (clm-f0jwtk item_idx 0): *"Forward-predict one classical value (e.g. tan δ of water at 1 GHz) from S(A)+t_sat/t_period to lift it past taxonomy"*, `mentioned_ids: []` (no resolving doc). The instruction is verbatim in `temporal-saturation-regime-classifier.md:310`.

**Exists — do NOT reinvent:**
| Ingredient | Location | Class |
|---|---|---|
| Real-part dielectric specialization ε_eff=ε₀S, C_eff=C₀/S, A=Δφ/α, V_yield | INVARIANT-S2; `dielectric-plateau-prediction.md:25` (clm-trgqtf); PONDER-05 `04_ponder_05_dc_biased_quartz.tex` | (a) closed |
| Reactive energy landscape U_eff(V)=C₀V_y²[1−S(V/V_y)] | `research/2026-05-26_ax4-saturation-phase-0c-pdelta-v-derivation-result.md:16` | (b) |
| Water static ε_real via Kirkwood-Frohlich (g=1+z cos²(θ/2)f_I) | `water-anomaly-lc-partition.md:36` (clm-jpfbm6) | (a) real part |
| Water-1 GHz absorption driver scaffold | `knot_water_amplification_mechanisms.py:234` (`eps_imag=10.0` hard-coded — the line to replace) | (b) |
| Time-fraction-of-period template f=(2/π)[arcsin√u − √(u(1−u))] | `radial-eigenvalue-solver.md:78` | (c) form |
| Dissipation seed: "below yield purely reactive; loss switches on AT Γ=−1" | `leaky-cavity-particle-decay/theory.md:12` | (c) mechanism |

**The GAP (what must be derived — all absent):**
1. **`t_sat(A₀, ω)`** — integrate time-above-yield per cycle from `S(A)`. No corpus instance; `t_sat` is not even operationally defined for grazing trajectories (`strengthen-by.jsonl:223` item_idx 2). Ingredients: the arcsin time-fraction template + the leaky-cavity dissipation-at-yield seed.
2. **`t_sat → σ → ε'' → tan δ`** — the dissipative leg. Entirely absent: every existing Q is *reactive* (Q=α⁻¹, P_real=0) and every loss value is a datasheet literal.
3. **Numerical forward-prediction of water tan δ at 1 GHz** — replacing the `eps_imag=10.0` hard-code.

## §4 — Derivation chain (the missing piece, to execute)

1. Water H-bond LC tank: A_yield from the Op4 H-bond well (INVARIANT-C3: d_HB=1.754 Å, E_HB=4.98 kcal/mol) via A=Δφ/α; drive amplitude A₀ from the 1 GHz field in ε_r≈80 medium.
2. `t_sat/t_period` for a sinusoidal drive grazing/exceeding A_yield → arcsin time-fraction form (`radial-eigenvalue-solver.md:78` template), evaluated at A₀/A_yield.
3. Map dissipated-fraction-per-cycle → ε''/σ → `tan δ = ε''/ε'` (ε' from the Kirkwood-Frohlich static value).
4. Compare predicted tan δ to measured (~0.1–0.13 at 1 GHz).

## §5 — Prereg block

```
PREREG (target: tan δ_water(1 GHz) from S(A) + t_sat/t_period; lift δ_AVE Class-1 → Class-4):
  Corpus state: OPEN — clm-f0jwtk strengthen-by item_idx 0, unclaimed, no resolving doc.
                ~70% scaffolding exists (real-part dielectric + water static ε + driver scaffold +
                arcsin template + dissipation-at-yield seed); dissipative leg (t_sat→ε''→tanδ) absent.
  Prediction: tan δ_AVE(water, 1 GHz) derivable to within order-of-magnitude of measured (~0.1)
              IF time-above-yield is the correct dissipation mechanism.
  Discriminating outcomes:
    A: tan δ within ~2× of measured → δ_AVE lifts to predictive; Reynolds-unification becomes
       load-bearing; strengthen-by item_idx 0 closes.
    B (most likely first pass): right OOM, wrong prefactor → mechanism plausibly right, normalization
       open (the Q-G19α "right shape, wrong magnitude" pattern → check prefactor/normalization next).
    C (null/falsify): wrong by OOMs, or t_sat structure cannot produce a loss tangent at all →
       δ_AVE = tan δ is taxonomic-only; the Reynolds-unification does NOT become predictive.
  Falsifier of framing: if matching requires feeding back a datasheet loss (circular), the
       derivation is not load-bearing — reject.
```

## §6 — Step-3.5 dimensional analysis + GUARDS

**Dimensional ingredients** (evaluate at CANONICAL primitives — no round numbers; the ax4-saturation epic burned 2.7 OOM on a wrong C₀): `S(A)` (dimensionless), `A_yield` via A=Δφ/α + V_yield (INVARIANT-C1 43.65 kV) + Op4 H-bond well (INVARIANT-C3), drive `A₀` (from 1 GHz field in ε_r≈80), `ω = 2π·10⁹ s⁻¹`, `t_period = 1/f`.
**Power-counting**: `tan δ ≈ δ_AVE = t_sat/t_period`; for a sinusoid amplitude A₀ crossing A_yield, `t_sat/t_period = (2/π)·arccos(A_yield/A₀)`-class form (zero below yield). Magnitude is set by `A₀/A_yield` at water primitives — the load-bearing number to evaluate.

**GUARD 1 — `ave-power-category-check` (the single biggest pitfall).** This derivation lives on the **REAL-POWER (dissipative)** side. ALL existing AVE Q-machinery is **reactive** (Q=α⁻¹, P_real=0, 90° phase — `theorem-3-1-q-factor.md`, the C14-DAMA chain that *created* `ave-power-category-check`). Do **NOT** reuse the reactive chain; build the dissipative complement. Conflating them reproduces the exact error that skill exists to prevent.

**GUARD 2 — substrate-native t_sat.** `t_sat` must come from `S(A)` crossing yield, not from an external `Z_det`/FDT boundary impedance (the ax4 P(δV) chain routes loss through `γ_n=Z_det⁻¹`, an *input* — that is the substitution to replace, not reuse).

## §7 — Execution dependencies (why this is prereg-only now)

- **Phase 4 / constants.py**: FT-2 execution reads canonical constants (V_yield, α, H-bond) from `src/ave/core/constants.py`, which is in the in-flight **Phase 4** uncommitted set. Execute **after Phase 4 lands** to use stable constants (verify Phase 4 didn't change V_yield / the kernel form — it shouldn't; Phase 4 is the α regime-(c) provenance walk-back).
- This prereg (scoping) is Phase-4-independent and complete now.

## §8 — Cross-references

> → Primary: [`temporal-saturation-regime-classifier.md`](../manuscript/ave-kb/common/temporal-saturation-regime-classifier.md) — δ_AVE (clm-f0jwtk); :310 the forward-derivation instruction
> → Primary: [`common/statistics-under-ave.md`](../manuscript/ave-kb/common/statistics-under-ave.md) §8 — the lift this prereg executes
> ↗ See also: `knot_water_amplification_mechanisms.py:234` — the `eps_imag=10.0` literal to replace
> ↗ See also: `leaky-cavity-particle-decay/theory.md:12` — dissipation-at-Γ=−1 mechanistic seed
