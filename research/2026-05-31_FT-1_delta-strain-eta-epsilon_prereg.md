# Prereg — FT-1 (Q-DELTA-MAP-1-quant): forward-derive δ_strain's η_ε from E-mode Bose-Einstein occupation

**Date**: 2026-05-31
**Branch**: `analysis/ft-1-delta-strain-eta-epsilon` (off `main` @ 93823898)
**Status**: PREREG FROZEN — ready for implementor. Corpus inventory complete (2026-05-31 grep). Derivation NOT executed.
**Parent**: leaf [`common/statistics-under-ave.md`](../manuscript/ave-kb/common/statistics-under-ave.md) §8; corpus-audit [`2026-05-31_statistics-under-ave_prereg_and_corpus_audit.md`](2026-05-31_statistics-under-ave_prereg_and_corpus_audit.md) §6 FT-1.

**Skills fired**: `ave-prereg` (this prereg + corpus inventory); `ave-canonical-leaf-pull` (δ_strain + dispersion + occupation machinery enumerated); `ave-canonical-source` (canonical primitives; no round numbers); `substrate-native-check` (E/B bipartite mode structure); `consistency-vs-emergence` (target = Class B → Class 2 lift); `ave-discrimination-check` (the SM-counterfactual that FT-2 skipped — mandatory here); `ave-evidence-framing-discipline` (anti-tuning honesty bar — §6); `verify-before-cite` (load-bearing citations re-verified at execution).

---

## §1 — Target (the highest-stakes chord-test)

Forward-derive the **magnitude** η_ε (≈ 4.45×10⁻⁶ at T_CMB; δ_strain ≈ η_ε/2 ≈ 2.225×10⁻⁶) from substrate primitives — E-mode dispersion + **substrate-Bose-Einstein occupation** at T_CMB — with **NO back-substitution from CODATA**. δ_strain is currently the framework's **one fitted scalar** (back-substituted: `δ_strain ≡ 1 − α⁻¹_CODATA/α⁻¹_ideal`). Deriving it independently turns α from "match a known number minus a fitted correction" into "match a known number AND predict its correction" — the single highest-stakes lift on the board (closes Q-DELTA-MAP-1-quant; lifts clm-009nkt Class B → Class 2, confidence 0.55 → >0.60).

## §2 — Physical picture (mechanical)

- K4 node: 6 DOF = 3 translational **E-modes** (gapless, thermally populated at any T>0) + 3 microrotational **B-modes** (gapped, Cosserat mass-gap ω_m ~ 1 MeV; thermally FROZEN at T_CMB, Boltzmann factor ~exp(−4×10⁹)).
- At T_CMB only E-modes populate → **asymmetric** occupation → ε thermally modulates while μ stays cold-lattice → SYM-class α-invariance is broken (ASYM) → α drifts by δ_strain.
- The magnitude is set by the thermal mean-square E-mode amplitude ⟨A_E²⟩ at T_CMB, coupled into ε.

## §3 — Corpus state: OPEN with a sharp diagnostic (2026-05-31 grep; sibling repos + archive ZERO hits — AVE-Core-canonical only)

**EXISTS — do NOT rebuild:**
| Piece | Location | Status |
|---|---|---|
| α-modulation form η_ε→δ_strain (ASYM single-√S, CORRECT) | `delta-strain-cosmic-tcc.md:73-92` (clm-hp7nlm): ε_eff=ε₀(1−η_ε), μ frozen → α_eff/α₀≈1/(1−η_ε)^{1/2}≈1+η_ε/2 → δ_strain≈η_ε/2 | (a) usable — the OUTPUT form is done |
| c_EM discipline (Pitfall #5) | INVARIANT-S2 `CLAUDE.md:64-66,70`; clm-8nkvwy `claim-quality.md:111-113,119` | (a) — α uses c_EM=c₀/√S (ASYM), NEVER c_shear |
| Dispersion-band solver (T₂ branch at c) | `src/scripts/vol_1_foundations/test_lattice_layer_1_dispersion.py` | (b) group-velocity solver — gives E-mode band, not thermal ⟨A_E²⟩ |
| B-mode gap (Verlet-validated) | `common/trampoline-framework.md:188` (m_ω²=4G_c/I_ω) | (c) WRONG sector (B freezes) |
| Classical g_* equipartition energy density | `mode-counting-heat-capacity.md:34-46` (clm-uu6dl5): ½g_*k_BT/ℓ_node³ | (c) — this is the ½kT form that UNDERSHOT (see diagnostic) |

**THE BUILD (absent — this is FT-1's real work):**
- **(ii) substrate-Bose-Einstein occupation** `⟨A_E²⟩` via `1/(e^{ℏω/k_BT}−1)` of the gapless E-spectrum — **no BE form exists anywhere in the corpus** (only the open work-item descriptions). This is the unbuilt core.
- **(iii) E-mode → ε_eff microscopic coupling** — wholly open, zero existing machinery.
- (i) E-mode dispersion `ω_E(k)=c_E|k|` is **asserted** (`delta-strain-cosmic-tcc.md:32`) but `c_E` from (ℓ_node, G_vac) is underived — tractable via the existing solver.

**THE FAILURE DIAGNOSTIC (Phase 3-A3, the load-bearing prior result):** `research/2026-05-28_phase-3-a3-delta-strain-machian-projection-result.md`. The Machian-G SYM cascade died at the Step-3.5 audit on **Pitfall #5** (used `1/S^{3/2}` = c_shear where c_EM belongs; SYM makes α exactly invariant → no δ_strain). Then **three candidate paths all failed at order-of-magnitude** before any mechanism was set (`result.md:103-109`):
- P2 (ASYM at thermal-bath ⟨A²⟩~k_BT_CMB/(ε₀ℓ³E_yield)): **~20 OOM too small**.
- P3 (bond rest-length thermal contraction): **~3 OOM too small**.
- P1 (EM-thermal-bath third class): not numerically attempted.

Walk-back conclusion (`result.md:109`): naive estimates undershoot; the real mechanism is "structurally different … or one of the candidates with a substrate-specific amplification factor not captured by naive estimates."

## §4 — Derivation chain (Q-DELTA-MAP-1-quant 4-step spec, verbatim `strengthen-by.jsonl:285`)

(i) compute E-mode dispersion ω_E(k) at T_CMB from substrate primitives (ℓ_node, G_vac) — *solver exists*;
(ii) compute thermal occupation ⟨A_E²⟩ via substrate-Bose-Einstein occupation of the E-mode spectrum at k_B T_CMB — **BUILD**;
(iii) couple to substrate dielectric response via Ax-1 microscopic primitives to extract η_ε — **BUILD (least-specified)**;
(iv) match to canonical η_ε ≈ 4.45×10⁻⁶ — **match, do not tune (see §6)**.

## §5 — Prereg block

```
PREREG (target: η_ε from E-mode BE-occupation + ε-coupling; lift δ_strain fit → prediction):
  Corpus state: OPEN. α-modulation OUTPUT form done; the BE-occupation (ii) + E-mode→ε coupling (iii)
                are the unbuilt core. Prior naive-equipartition attempts (P2/P3) undershot by 3–20 OOM.
  Prediction: an INDEPENDENT BE-occupation + ε-coupling calc (no knowledge of 4.45e-6) lands at
              η_ε within ~1 OOM of 4.45e-6 IF the BE-occupation of the gapless E-spectrum supplies the
              amplification the naive ½kT equipartition lacked.
  Discriminating outcomes:
    A (the prize): independent calc lands η_ε ~ 4.45e-6 (within ~1 OOM) → α's fitted scalar becomes a
       prediction; δ_strain Class B → Class 2; chord STRUMMED.
    B (partial): right mechanism/sign, magnitude off by a bounded factor → mechanism supported, prefactor open.
    C (most likely, per the diagnostic): calc inherits the 3–20 OOM undershoot → δ_strain stays a fit;
       the Cosserat-thermal mechanism does not supply the magnitude. Honest NEGATIVE.
  Falsifier of framing (HARD): if the calc only "matches" by feeding 4.45e-6 (or δ_strain, or the CODATA
       residual) back in as an input → circular, NOT a derivation. REJECT and report C.
```

## §6 — GUARDS + Step-3.5 + anti-tuning honesty bar

1. **`ave-discrimination-check` (mandatory — FT-2 skipped it and it was decisive).** Before claiming AVE-distinct: does the η_ε scale follow from generic thermal physics any framework shares, or specifically from the substrate E/B-asymmetry + BE-occupation? State the SM-counterfactual explicitly.
2. **c_EM not c_shear (Pitfall #5).** α uses c_EM = c₀/√S (ASYM, only ε scales). The Phase 3-A3 death was using c_shear (`1/S^{3/2}`). Re-verify against INVARIANT-S2 + clm-8nkvwy at execution.
3. **Anti-tuning (the honesty crux).** The target η_ε ≈ 4.45×10⁻⁶ IS the back-substituted value. "Matching" it only counts if the calc derives it from (ℓ_node, G_vac, T_CMB, Ax-1 ε-coupling) WITHOUT the target entering. Pre-register the predicted η_ε from the independent chain BEFORE comparing to 4.45e-6.
4. **The OOM-amplification diagnostic IS the test.** Naive ½kT equipartition gave P2/P3 undershoots of 3–20 OOM. FT-1 PASSES only if BE-occupation of the gapless E-spectrum (which differs from ½kT equipartition by the occupation factor + the spectral integral) supplies that gap from first principles — NOT by a fitted amplification.
5. `ave-canonical-source`: ℓ_node, G_vac, T_CMB, K_B from constants.py; no round numbers.

## §7 — Scope (what to build vs reuse)

- **Reuse:** the α-modulation form (§3 row 1), the c_EM discipline, the dispersion-band solver (step i input), the classical g_* leaf (as the explicit foil to beat).
- **Build:** (ii) substrate-Bose-Einstein occupation `⟨A_E²⟩(T_CMB)` over the gapless E-spectrum; (iii) the E-mode→ε_eff microscopic coupling. These two are the entire derivation.
- **Honest expectation:** this is the highest-stakes AND hardest FT (the prior attempt failed at OOM). Outcome C is a real possibility and a valid, valuable result. Do not force A.

## §8 — Cross-references

> → Primary: [`delta-strain-cosmic-tcc.md`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) — clm-hp7nlm; α-modulation form (:73-92), E/B structure (:32-33), Class-2-lift spec (:116-119)
> → Primary: KB [`CLAUDE.md`](../manuscript/ave-kb/CLAUDE.md) INVARIANT-S2 (:64-70) — c_EM vs c_shear (Pitfall #5)
> ↗ See also: [`2026-05-28_phase-3-a3-delta-strain-machian-projection-result.md`](2026-05-28_phase-3-a3-delta-strain-machian-projection-result.md) — the failed attempt + the 3–20 OOM diagnostic
> ↗ See also: [`mode-counting-heat-capacity.md`](../manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/mode-counting-heat-capacity.md) — clm-uu6dl5, classical g_* equipartition (the foil)
> ↗ See also: `src/scripts/vol_1_foundations/test_lattice_layer_1_dispersion.py` — dispersion-band solver (step i input)
