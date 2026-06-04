# Prereg — Direction-2 FT: re-extract α from the measured electron anomaly through AVE's own a_e(α) series

**Date**: 2026-05-31
**Branch**: `analysis/alpha-reextraction-direction-2` (off `main` @ 93823898)
**Status**: PREREG FROZEN — ready for implementor. Supersedes the dual-loading-*magnitude* derivation (A-031 horizon-blocked); this re-extracts instead of deriving the residual.
**Lineage**: the δ_strain arc — thermal (FT-1, 31 OOM, falsified) → α²/24 (coincidence, rejected) → dual-loading magnitude (A-031-inaccessible) → **Direction-2 (this): don't derive the correction; re-extract α from the raw measurement through AVE's framework.**

**Skills**: `ave-prereg` (inventory from the session's prior greps); `ave-canonical-source`; `ave-power-category-check` (a_e = real-power self-load); `ave-discrimination-check` (the discriminator IS AVE's A₂ vs QED's C₂); `ave-evidence-framing-discipline` (anti-tuning); `consistency-vs-emergence`; `verify-before-cite`.

---

## §1 — Target (the methodological inversion)

Every prior attempt ran **AVE → QED**: take the QED-extracted value (CODATA α⁻¹ = 137.035999) as a fixed target and *derive* AVE's correction to reach it from the bare geometric Q₀ = 4π³+π²+π = 137.0363038. That direction dead-ended (the correction's magnitude is A-031 horizon-inaccessible).

**Direction-2 runs it backward: QED-measurement → AVE.** The measured electron anomaly a_e (the raw cyclotron/anomaly frequency ratio ω_a/ω_c, theory-neutral) is converted to α by *inverting a self-coupling series* a_e(α). CODATA α is that needle read through **QED's faceplate** (the QED loop series). The task: **re-extract α from the same measured a_e through AVE's OWN faceplate** — AVE's a_e(α) series from the Axiom-4 back-reaction — and check where it lands.

- If α_AVE⁻¹ → **4π³+π²+π (137.0363038)**: δ_strain was never physical — it's the **QED-vs-AVE extraction-frame offset**. Dissolved.
- If α_AVE⁻¹ → **137.035999 (= QED)**: δ_strain is a **real internal inconsistency** — AVE's geometry (Q₀) disagrees with AVE's own measurement theory.

## §2 — Physical picture (EE)

Same instrument, different faceplate. The raw **needle** is a_e ≈ 1.15965218×10⁻³ (a frequency ratio — instrument-native, not framework-laden). The **faceplate** is the a_e(α) calibration curve used to read α off the needle:
- **QED faceplate**: a_e = C₁(α/π) + C₂(α/π)² + …, C₁ = ½ (Schwinger), C₂ = −0.328478965 (2-loop). Inverts → 137.035999.
- **AVE faceplate**: a_e = A₁(α/π) + A₂(α/π)² + …, with **A₁ = ½ already matching Schwinger** (`simulate_g2.py`). The difference, if any, is **at (α/π)²: AVE's A₂ vs QED's C₂.**

Sharp target (from inverting a_e at fixed needle): δ_strain dissolves iff AVE's A₂ differs from QED's C₂ by **ΔC₂ ≈ +4.8×10⁻⁴** (i.e. A₂ ≈ −0.3280, ~0.15% less negative than QED's −0.32848 — the value that re-extracts the measured a_e to Q₀). If AVE's A₂ = QED's −0.32848 exactly, no dissolution → δ_strain real.

## §3 — Corpus state (from this session's greps; re-verify at execution)

**EXISTS — the leading faceplate term is built:**
- `src/scripts/vol_2_subatomic/simulate_g2.py`: A₁ chain — V_peak/V_snap=√(4πα) → δC/C=−πα → δω/ω=πα/2 → ×(1/π² spin-orbit projection) → **a_e = α/2π** (= QED Schwinger; A₁=½). "No renormalization needed — the lattice IS the regulator."
- `weak-coupling.md:22`: the two-vertex α² self-energy structure (ε(φ)=ε₀(1+αf(φ)) single vertex → E_self ∝ α²) — the seed for A₂.

**BUILD — AVE's (α/π)² coefficient A₂:**
- Compute A₂ from AVE's two-vertex+ self-energy (the substrate analog of QED's 2-loop g-2) to ~4–5 sig figs — enough to distinguish "→ Q₀" (A₂≈−0.3280) from "→ QED" (A₂=−0.32848). This is the entire derivation.

**Anchors:** measured a_e = 1.15965218073×10⁻³; QED C₂ = −0.328478965; Q₀ = 4π³+π²+π = 137.0363038; QED extraction = 137.035999. Recoil cross-check: both standard routes give 137.035999 — but BOTH are QED-faceplate (recoil's R∞ is QED-fit), so they share any QED-vs-AVE offset (which would explain their agreement).

## §4 — Chain

(i) Confirm A₁ = ½ from `simulate_g2.py` (done — Schwinger leading).
(ii) **BUILD** A₂ from AVE's two-vertex self-energy + the 1/π² projection at second order, from substrate primitives — NO target fed in.
(iii) Invert a_e_measured = ½(α/π) + A₂(α/π)² + … for α_AVE.
(iv) Compare α_AVE⁻¹ to Q₀ (137.0363038) vs QED (137.035999).

## §5 — Prereg block

```
PREREG (target: re-extract α from measured a_e via AVE's a_e(α) series; land on Q₀ or QED's value?):
  Corpus state: A₁=½ built (simulate_g2); A₂ = the build (two-vertex self-energy to (α/π)²).
  Prediction: open two-sided. If AVE's substrate self-energy is QED-structurally-identical, A₂=C₂ → lands
              on 137.035999 (δ_strain real). If it differs at 2nd order (lattice cutoff / projection enters
              differently), A₂ shifts by ~ΔC₂ → could land on Q₀ (δ_strain dissolved).
  Discriminating outcomes:
    A (dissolution): α_AVE⁻¹ → 4π³+π²+π → δ_strain = QED-vs-AVE faceplate offset; α IS exactly Q₀; the
       residual was a calibration-frame artifact, not physics. Chord-relevant.
    B (internal inconsistency): α_AVE⁻¹ → 137.035999 (A₂=C₂) → δ_strain real; AVE geometry ≠ AVE
       measurement theory. Decisive (a genuine problem for AVE to confront).
    C (inconclusive): A₂ not computable to sufficient precision to separate A from B → need higher order.
  Falsifier of framing (HARD): if A₂ is TUNED to hit Q₀ rather than computed from substrate → circular,
       REJECT and report C. A₂ must be derived BEFORE the compare.
```

## §6 — Guards

1. **Anti-tuning (the crux).** Compute A₂ from the substrate self-energy FIRST; THEN invert + compare. Neither Q₀ nor 137.035999 nor δ_strain may enter the A₂ computation.
2. **`ave-power-category-check`.** a_e is the REAL-power self-load (the dissipative leg) — build it as such, not from the reactive Q-chain.
3. **`ave-discrimination-check`.** The AVE-distinct content is precisely "AVE's A₂ ≠ QED's C₂." State the SM-counterfactual: QED's C₂ = −0.328478965 is the established 2-loop g-2. If A₂ = C₂, AVE adds nothing here (and δ_strain is real).
4. **NO cosmic-magnitude smuggling (why this escapes the horizon).** This uses the MEASURED a_e + the LOCAL self-energy series — it must NOT invoke f_R / the A-031-inaccessible cosmic chirality fraction. If the A₂ calc finds it needs a cosmic parameter, FLAG it (would mean Direction-2 doesn't escape the horizon after all).
5. **`ave-canonical-source`** — primitives from constants.py; no round numbers.

## §7 — Why this supersedes the dual-loading-magnitude FT

The dual-loading approach tried to *derive δ_strain's magnitude* → traced to χ_1/K_0 (adjudicated O(1) at substrate scale, doc 122) and f_R behind the **A-031 horizon** → inaccessible. Direction-2 needs none of that: it re-extracts α from the *measured* anomaly through AVE's *local, computable* a_e(α) series. **The cosmic parameter never enters.** (The dual-loading *running* leg — the Π_AVE(q²) dielectric-dispersion repair, fixing the 200× coefficient + the thermal-SYM tension — remains a separate worthwhile AVE-QED consistency task, independent of this.)

## §8 — Effort

The work is computing **A₂** (the (α/π)² self-energy coefficient) to ~4–5 sig figs from the two-vertex+ substrate self-energy — a 2-loop-analog calculation. Moderate-to-hard, but **well-posed** (a definite number to compute), with the leading-order anchor (`simulate_g2.py`) and the two-vertex structure (`weak-coupling.md`) in hand, and crucially **not horizon-blocked**. Estimate: ~1–2 sessions for A₂ + the re-extraction; the outcome (A/B/C) is decisive either way.

## §9 — Cross-references

> → Primary: `src/scripts/vol_2_subatomic/simulate_g2.py` — A₁ = ½ (α/2π Schwinger) chain; the leading faceplate term
> → Primary: [`weak-coupling.md`](../manuscript/ave-kb/vol2/particle-physics/ch05-electroweak-mechanics/weak-coupling.md) — two-vertex α² self-energy (the A₂ seed)
> → Primary: [`theorem-3-1-q-factor.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) — α⁻¹ = Q₀ = 4π³+π²+π (the geometric value to test against)
> ↗ See also: [`2026-05-31_FT-1_delta-strain-eta-epsilon_result.md`](2026-05-31_FT-1_delta-strain-eta-epsilon_result.md) — the thermal route's falsification (why we inverted the direction)
> ↗ Method: this prereg is the prototype for the `ave-external-provenance-check` skill — "re-extract the raw observable through AVE's framework; never derive a correction to match the SM-extracted number."
