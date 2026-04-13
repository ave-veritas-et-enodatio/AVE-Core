# Vol 8 — Phase 2 Extraction

**Volume:** `manuscript/vol_8_virtual_media/`
**Taxonomy reference:** `.claude/phase1-taxonomy/vol8_taxonomy.md`
**Extraction date:** 2026-04-02
**Status:** Complete — all skeleton positions mapped

---

## Source Directory Listing

```
vol_8_virtual_media/
  main.tex
  chapters/
    01_llm_topology.tex
    02_hardware_software_inversion.tex
    03_universal_operator.tex
    04_experimental_audit.tex
    05_global_ac_scope.tex
    06_continuous_smoothing.tex
    07_operator_unification.tex
    08_discrete_manifold_masking.tex
    09_gamma_scaling.tex
    10_attention_impedance.tex
    11_moe_impedance.tex
    12_sigmoid_saturation.tex
    appendix/ (pointer to ../common/appendix_experiments.tex)
```

---

## Skeleton-to-Source Mapping

Leaf boundaries are SECTION-level (`\section{}`). Each `\section{}` becomes one leaf.

| Skeleton leaf | Source file | Section title | `\label` / Notes |
|---|---|---|---|
| **foundations/ch1-llm-topology/** | | | Ch.1 uses `\subsection{}` not `\section{}` — see Ambiguity 1 |
| `swiglu-twoport.md` | `01_llm_topology.tex` | SwiGLU Two-Port Network | subsection-level boundary |
| `ac-thermodynamic.md` | `01_llm_topology.tex` | AC Thermodynamic Interpretation | subsection-level boundary |
| `axiom3-pruning.md` | `01_llm_topology.tex` | Axiom 3 and Pruning | subsection-level boundary |
| **foundations/ch2-hw-sw-inversion/** | | | |
| `inversion-split.md` | `02_hardware_software_inversion.tex` | Where the Isomorphism Inverts | `\label{sec:...}` |
| `breakdown-paradox.md` | `02_hardware_software_inversion.tex` | The Breakdown Paradox | `\label{sec:...}` |
| **foundations/ch3-universal-operator/** | | | |
| `axiomatic-correspondences.md` | `03_universal_operator.tex` | Axiomatic Correspondences | `\label{sec:...}` |
| `axiom2-attention.md` | `03_universal_operator.tex` | Axiom 2 and Attention | `\label{sec:...}` |
| `regime-map.md` | `03_universal_operator.tex` | Regime Map | `\label{sec:...}` |
| `ffn-twoport.md` | `03_universal_operator.tex` | FFN Two-Port | `\label{sec:...}` |
| **saturation-pruning/ch4-experimental-audit/** | | | |
| `saturation-operator.md` | `04_experimental_audit.tex` | Saturation Operator | `\label{sec:...}` |
| `quantitative-results.md` | `04_experimental_audit.tex` | Quantitative Results | `<!-- status: pending-autotune -->` — see below |
| `swiglu-density.md` | `04_experimental_audit.tex` | SwiGLU Density | `\label{sec:...}` |
| `head-pruning-audit.md` | `04_experimental_audit.tex` | Head Pruning Audit | `\label{sec:...}` |
| `current-limitations.md` | `04_experimental_audit.tex` | Current Limitations | `\label{sec:...}` |
| **saturation-pruning/ch5-global-ac-scope/** | | | |
| `per-layer-paradox.md` | `05_global_ac_scope.tex` | Per-Layer Paradox | `\label{sec:...}` |
| `global-ac-correction.md` | `05_global_ac_scope.tex` | Global AC Correction | `<!-- status: pending-autotune -->` — see below |
| `runtime-shift.md` | `05_global_ac_scope.tex` | Runtime Shift | `\label{sec:...}` |
| `gamma-per-layer.md` | `05_global_ac_scope.tex` | Gamma Per Layer | `\label{sec:...}` |
| **saturation-pruning/ch6-continuous-smoothing/** | | | |
| `gamma-prune-metric.md` | `06_continuous_smoothing.tex` | Gamma Prune Metric | `\label{sec:...}` |
| `saturation-sr.md` | `06_continuous_smoothing.tex` | Saturation SR | `\label{sec:...}` |
| **architecture-analysis/ch7-operator-unification/** | | | |
| `phase-tension.md` | `07_operator_unification.tex` | Phase Tension | `\label{sec:...}` |
| `operator-bindings.md` | `07_operator_unification.tex` | Operator Bindings | `\label{sec:...}` |
| `hamiltonian-cusp.md` | `07_operator_unification.tex` | Hamiltonian Cusp | `\label{sec:...}` |
| **architecture-analysis/ch8-discrete-masking/** | | | Ch.8 has `\subsection*{}` groups |
| `masking-protocol.md` | `08_discrete_manifold_masking.tex` | Masking Protocol | `\label{ch:discrete-manifold-masking}` (chapter, hyphens) |
| `zeff-telemetry.md` | `08_discrete_manifold_masking.tex` | Z_eff Telemetry | `\label{sec:...}` |
| `masking-failures.md` | `08_discrete_manifold_masking.tex` | Why Masking Fails | Groups: `\subsection*{Why Continuous Masking Fails}` + `\subsection*{Why Binary Masking Also Fails}` |
| `static-baking.md` | `08_discrete_manifold_masking.tex` | Static Baking | `\label{sec:...}` |
| `gamma-excision.md` | `08_discrete_manifold_masking.tex` | Gamma Excision | `\label{sec:...}` |
| `neuroplasticity.md` | `08_discrete_manifold_masking.tex` | Neuroplasticity | Groups starred subsections |
| **architecture-analysis/ch9-gamma-scaling/** | | | |
| `gamma-thresholds.md` | `09_gamma_scaling.tex` | Gamma Thresholds | `\label{sec:...}` |
| `autotune-results.md` | `09_gamma_scaling.tex` | Autotune Results | `<!-- status: pending-autotune -->` — see below |
| `cascade-transfer.md` | `09_gamma_scaling.tex` | Cascade Transfer Function | `\label{eq:gamma_scaling}`: $T=(1-\gamma)^N$ CONFIRMED |
| `transmission-budget.md` | `09_gamma_scaling.tex` | Transmission Budget | `\subsection*{}` (not `\section{}`) — see Ambiguity 3 |
| `density-constraint.md` | `09_gamma_scaling.tex` | Density Constraint | `\label{sec:...}` |
| **architecture-analysis/ch10-attention-impedance/** | | | Ch.10 has `\subsection*{}` groups |
| `qkv-impedance.md` | `10_attention_impedance.tex` | QKV Impedance | `\label{sec:...}` |
| `gqa-constraint.md` | `10_attention_impedance.tex` | GQA Constraint | `\label{sec:...}` |
| `impedance-distribution.md` | `10_attention_impedance.tex` | Impedance Distribution | `\label{sec:...}` |
| `intersection-constraint.md` | `10_attention_impedance.tex` | Intersection Constraint | `\label{sec:...}` |
| `axiom2-interpretation.md` | `10_attention_impedance.tex` | Axiom 2 Interpretation | `\label{sec:...}` |
| **architecture-analysis/ch11-moe-impedance/** | | | |
| `dynamic-impedance.md` | `11_moe_impedance.tex` | Dynamic Impedance | `\label{sec:...}` |
| `router-axiom3.md` | `11_moe_impedance.tex` | Router Axiom 3 | `\label{sec:...}` |
| `moe-vs-static.md` | `11_moe_impedance.tex` | MoE vs Static | `\label{sec:...}` |
| `moe-prediction.md` | `11_moe_impedance.tex` | MoE Prediction | Groups: testable prediction + hardware limitations (starred subsections) |
| **activation-geometry/ch12-sigmoid-saturation/** | | | Ch.12 has `\subsection*{}` groups |
| `unit-circle-identity.md` | `12_sigmoid_saturation.tex` | σ²+r²=1 Identity | `\label{eq:unit_circle}` CONFIRMED; starred subsections sub-included |
| `zero-bias-prediction.md` | `12_sigmoid_saturation.tex` | Zero-Bias Prediction | `\label{sec:...}` |
| `yield-limit-virtual.md` | `12_sigmoid_saturation.tex` | Yield Limit (Virtual Media) | `\label{sec:...}` |
| `regime-boundaries.md` | `12_sigmoid_saturation.tex` | Regime Boundaries | Overlaps with starred subsections — see Ambiguity 4 |
| `density-derivation.md` | `12_sigmoid_saturation.tex` | Density Derivation (97% via error function) | `\label{sec:...}` |
| `implications.md` | `12_sigmoid_saturation.tex` | Implications | `\label{sec:...}` |
| **appendix/** | | | |
| `unified-experiments-ref.md` | (pointer only) | — | Cross-ref to `ave-kb/common/appendix-experiments.md` |

---

## Pending-Autotune Evidence

| Leaf | Source section | Evidence |
|---|---|---|
| `quantitative-results.md` (ch4) | `04_experimental_audit.tex` | Table caption explicitly states "their calibrated maxima are pending" for 8B, 4B, 9B models. Strong source evidence. |
| `global-ac-correction.md` (ch5) | `05_global_ac_scope.tex` | No direct "pending" marker in this specific section; the pending items are in ch4 and ch9 tables. Taxonomy annotation is over-broad for this specific leaf. Include marker per taxonomy requirement; note it in leaf metadata. |
| `autotune-results.md` (ch9) | `09_gamma_scaling.tex` | Three table cells contain `\emph{pending}` + explicit `\textbf{Status:}` blockquote: "The 8B autotune is pending." Strongest source evidence. |

---

## All `\label{}` Found in Vol 8

**Equation labels (2 — as expected):**
- `eq:gamma_scaling` — in `09_gamma_scaling.tex` (`cascade-transfer.md`)
- `eq:unit_circle` — in `12_sigmoid_saturation.tex` (`unit-circle-identity.md`)

**Chapter labels (12):** One per chapter file. Anomaly: `\label{ch:discrete-manifold-masking}` (Ch.8) uses hyphens; all other chapter labels use underscores (e.g., `ch:attention_impedance`).

**Section labels (6):** Confirmed in chs. 2, 3, 7, 9, 10, 11.

**Table labels (5)** and **Figure labels (12):** Present; not PATH-STABLE.

No additional equation labels beyond `eq:gamma_scaling` and `eq:unit_circle`.

---

## tcolorbox Environments

**Zero instances confirmed.** No `\begin{resultbox}`, `\begin{axiombox}`, `\begin{simbox}`, `\begin{examplebox}`, `\begin{summarybox}`, `\begin{exercisebox}`, `\begin{circuitbox}`, `\begin{codebox}`, `\begin{objectivebox}` appear anywhere in `vol_8_virtual_media/`.

---

## NOTES.md Source Content

The Z∝A inversion and raw-form notation policy is sourced from:
- **Primary source:** `02_hardware_software_inversion.tex`, section "Where the Isomorphism Inverts"
- **Raw notation instance:** One `\Zvac` macro use found at `08_discrete_manifold_masking.tex` line 48. All other Vol 8 math uses raw forms ($Z_0$, $\mu_0$, etc.) directly.
- **Distiller rule:** Translate `\Zvac` → `$Z_0$` in `masking-protocol.md`.

NOTES.md content should cover:
1. Z∝A inversion (from ch2 "Where the Isomorphism Inverts" section)
2. Raw-form notation convention (all macros → raw forms)
3. Pending-autotune marker policy (3 leaves identified above)

---

## Starred Subsection Groups

| Leaf | Grouped `\subsection*{}` entries |
|---|---|
| `masking-failures.md` | "Why Continuous Masking Fails" + "Why Binary Masking Also Fails" |
| `moe-prediction.md` | "Testable Prediction" + "Hardware Limitations" |
| `unit-circle-identity.md` | Multiple starred subsections on the σ²+r²=1 derivation |
| `neuroplasticity.md` | Multiple starred subsections on neuroplasticity applications |
| `regime-boundaries.md` | Starred subsections potentially overlapping with `zero-bias-prediction` and `yield-limit-virtual` |

---

## Appendix

No original experimental content in Vol 8. The appendix position in `main.tex` inputs only `../common/appendix_experiments.tex`. `unified-experiments-ref.md` is a cross-ref leaf pointing to `ave-kb/common/appendix-experiments.md`.

---

## Unassigned `\section{Conclusion}` Entries

Five chapters contain `\section{Conclusion}` (or similar) as an explicit section but the taxonomy did not allocate a leaf for it. Affected chapters: 5, 6, 8, 10, 11. The coordinator must decide: include these as additional leaves, merge with the preceding content leaf, or exclude as boilerplate.

---

## Empty Skeleton Positions

NONE. All 43 leaf positions have confirmed source content.

---

## Leaf Boundary Notes

- **Ch.1 exception:** Leaf boundaries are `\subsection{}` not `\section{}` (Ch.1 uses only subsections, no top-level sections). This is the only chapter with this anomaly.
- **Ch.4–Ch.12 standard:** Each `\section{}` → one leaf.
- **Starred subsection groups:** Several leaves group multiple `\subsection*{}` entries — see table above.
- **`transmission-budget.md` boundary:** This leaf maps to a `\subsection*{}` rather than a `\section{}` in Ch.9. The distiller should treat it as a distinct leaf anyway, per the taxonomy specification.

---

## Notation and Macro Notes

Vol 8 uses raw forms for all physics notation. The single `\Zvac` instance in Ch.8 line 48 must be translated to `$Z_0$`. All other macro references from the shared `commands.tex` do not appear in Vol 8 source.

---

## Ambiguities Requiring Coordinator Decision

1. **Ch.1 subsection-level leaves:** Leaf boundaries are `\subsection{}` not `\section{}`. This is the only volume chapter where leaves are at subsection granularity. No structural change needed; distillers must use `\subsection{}` boundaries for Ch.1.

2. **5 unassigned `\section{Conclusion}` entries** (chs. 5, 6, 8, 10, 11): Include as additional leaves, merge, or exclude?

3. **`transmission-budget.md` is `\subsection*{}`:** Treat as leaf per taxonomy (already specified) or merge with adjacent section?

4. **Ch.12 `regime-boundaries.md` overlap:** Content boundaries with `zero-bias-prediction.md` and `yield-limit-virtual.md` are ambiguous due to starred subsection structure. Distiller needs explicit boundary rule for Ch.12.
