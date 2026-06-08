# Prereg: α-identity discriminator (AVE hypotheses vs short-term image)

**Status:** FROZEN PREREG before driver run.
**Branch:** `analysis/2026-06-07-two-node-alpha-projection`.
**Driver:** `src/scripts/vol_1_foundations/alpha_identity_discriminator.py`.
**Parent:** L5 (`2026-06-07_unified-l5-q-leakage-prereg.md`), two-node test, calibration-crux sweep.

---

## §0 Question

Under AVE, **what is α most likely to be** — by forward discriminator, not by Grant's short-term image?

Competing hypotheses (all AVE-native framings):

| ID | Hypothesis | α is… | Forward prediction on unified lane |
|----|------------|-------|----------------------------------|
| **H1** | **Cage leak** (Theorem 3.1', rotor §3) | Per-cycle TIR leak `ε = 1/Q` | `ε_Γ = 1−Γ²` at bond; **`ε → α` only when `Γ → −1`** (full short) |
| **H2** | **Complex-projector constant** (short-term image) | Screened quadrature residue in `(V_inc,V_ref)` | `screened_var ≈ α` or `screened_rms ≈ √α` on neighbor shell |
| **H3** | **Torque coupling** (short-term image) | Neighbor-gradient × phasor-twist coupling `k ≈ α` | `twist_rate / strain_asymmetry ≈ α` |
| **H4** | **4π radiation scale** (dark-wake / geometry lane) | Loss channel at `Q ≈ 4π` | `Q_Γ` or `Q_decay → 4π`, not 137 |
| **H5** | **Static mode-count** (Class B only) | `4π³+π²+π` geometry integral | `Q_Λ` field sum ≈ 137 **independent of Γ** |
| **H6** | **Fine-structure tidal** (rotor §7c) | **α²** spin–orbit coupling, not α | First-order torque/leak scales ≠ α; splitting would be α² (not testable on this scalar lane) |

**Primary prediction:** **H1 wins on mechanism; none hit α numerically on this lane yet.**

Reason: calibration crux — rest scale has no wall; wall scale stops at `Γ ≈ −0.63`, not `−1`. H1 predicts approach-to-α with wall strength; H2/H3 already have independent negatives; H4/H5 are different scales.

## §1 Test design

Alpha-free amplitude battery: `[0.48, 1.0, 2.0, 3.0, 3.5, 4.0]` on `MasterEquationFDTD + PhasorBridge`.

Per amplitude, measure (alpha-free):

1. `Γ_min` (trace, uncapped)
2. `ε_Γ = 1 − Γ_min²`
3. `Q_Γ = π / ε_Γ`
4. Neighbor-shell screened variance in `(V_inc, V_ref)` plane (H2)
5. `twist_rate / strain_asymmetry` at center (H3)
6. `Q_Λ` decomposition sum (H5)
7. `Q_decay` from center ring-down (H4/H1)

Score each hypothesis by **mean log₁₀ relative error** vs its forward target (comparison-only constants: `α`, `4π`, `137`, `0.5`, `√0.5`).

## §2 Outcome table

| Outcome | Criterion | Verdict |
|---------|-----------|---------|
| A | H1: `ε_Γ` monotonic with `|Γ|` AND closest approach to `α` at max amplitude | **CAGE_LEAK_MOST_LIKELY** |
| B | H2 or H3 lowest error across battery | Short-term image survives |
| C | H4 wins | **4π_LOSS_SCALE** |
| D | H5 wins at all amplitudes | **STATIC_GEOMETRY_ONLY** (Class B, not dynamic α) |
| E | No hypothesis within 1 decade at any point | **DISCRIMINATOR_INCONCLUSIVE** on this lane |

## §3 Honest limits

- Scalar + projection lane only; native coupled K4 may differ.
- H6 deferred (needs rotor-in-gradient solver).
- `α` imported comparison-only for scoring, never in dynamics.

---

## §4 Result

```bash
PYTHONPATH=src python src/scripts/vol_1_foundations/alpha_identity_discriminator.py
```

Output: `src/scripts/vol_1_foundations/_output/alpha_identity_discriminator_results.json`

## §5 Adjudication

**Verdict: `CAGE_LEAK_MECHANISM_WINS; SHORT_TERM_IMAGES_DEAD; NUMERICAL_α_NOT_REACHED`**

### What the battery says (alpha-free data, comparison-only scoring)

| Amplitude | Γ_min | ε = 1−Γ² | Screened var | Torque k = twist/asym |
|-----------|-------|----------|--------------|------------------------|
| 0.48 | −0.013 | 0.9998 | 0.093 | 13.1 |
| 1.0 | −0.552 | 0.695 | 0.114 | 2.6 |
| 3.0 | −0.634 | **0.598** | 0.121 | 0.76 |
| 4.0 | −0.634 | **0.597** | 0.193 | 1.1 |

**Closest ε to α:** amp 3.5, **|ε−α| ≈ 0.59** — still **~80× too large** (ε ≈ 0.6 vs α ≈ 0.007).

### Hypothesis scores (honest)

| Hypothesis | Result |
|------------|--------|
| **H1 Cage leak** | **Mechanism confirmed:** ε tracks `1−Γ²`. **Numerical α fails:** Γ **saturates ~−0.63**, never → −1, so ε **plateaus ~0.6**, not α. |
| **H2 Projector = α** | **Dead.** Screened variance ∈ [0.09, 0.19], not α (0.007) nor prior ½. |
| **H3 Torque k = α** | **Dead.** Coupling ratio unstable (0.76–13), no α scale. |
| **H4 Q ≈ 4π** | Q_Γ ≈ 5.3 at wall — closer to 4π than 137, but not a clean match either. |
| **H5 Static Q_Λ = 137** | Q_Λ drifts 56–118 with amplitude — not constant 137. |

### Answer to Grant's question

**Under AVE, α is most likely the cage-leak / per-cycle TIR coupling (H1, Theorem 3.1')** — not the node's torque constant in a complex projection (H3), not a bare screened covariance residue (H2).

Your short-term images are **ruled out on this lane**.

What we **cannot** yet claim: that the simulation **reads out** α ≈ 1/137. That requires **Γ → −1** (full short) + Op21 geometry — the calibration crux again.

### Next discriminator (if you want numerical α, not just identity)

1. **Native coupled K4** at amplitudes where Γ → −0.99+ (not scalar projection).
2. **Fine-structure tidal test** — if α enters, it should be **α²**, not α (rotor §7c) — kills torque-constant-at-α picture differently.
3. **Theorem 3.1' derived-vs-asserted audit** — is Q ≡ 1/α definition or emergence?
