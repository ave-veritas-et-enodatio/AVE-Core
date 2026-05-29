[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
subtree-experiments: []
-->

# Ch.2 Absolute Maximum Ratings

Chapter 2 of the Vol 9 datasheet documents the substrate's absolute rupture thresholds — the parameter values at which the Axiom 4 universal saturation kernel $S(A) = \sqrt{1 - (A/A_{yield})^2}$ reaches zero and the local topology is destroyed. Five canonical absolute-maximum ratings are tabulated: $V_{snap}$ (topological node-pair destruction voltage), $V_{yield}$ (macroscopic dielectric nonlinear-onset voltage), $E_S$ (Schwinger pair-production critical field), $B_{snap}$ (magnetic-rotation node-destruction field), $T_{melt}$ (pair-production thermal threshold). Per the four-regime map, all five correspond to the Regime~III/IV boundary $r = A/A_c = 1.0$ (substrate-topology destruction, not gradual degradation).

The chapter content is **Class B/C synthesis** per `consistency-vs-emergence` v1.3 — no new substrate-physics primitives are introduced; the content consolidates the canonical axiom-derived thresholds (per `CLAUDE.md` INVARIANT-S2 Axiom 4 + Axiom 2 dual derivation) and cites the existing canonical leaves where each threshold is derived. Numerical values are imported from `src/ave/core/constants.py` via the `ave-canonical-source` discipline; no hard-coded values appear in the chapter.

## Primary canonical sources

| Source | Content |
|---|---|
| [`vol1/.../dielectric-snap-limit.md`](../../vol1/axioms-and-lattice/ch2-macroscopic-moduli/dielectric-snap-limit.md), `clm-2dwzib` | $V_{snap} = m_e c^2/e \approx 511$ kV canonical derivation |
| [`vol4/claim-quality.md`](../../vol4/claim-quality.md) `clm-0vxzfu` | $V_{yield}$ vs $V_{snap}$ two-threshold distinction (load-bearing reading hazard, engine defaults) |
| [`vol4/.../regimes-of-operation.md`](../../vol4/circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md), `clm-trgqtf` | $V_{yield}$ macroscopic / $E_{yield}$ field-threshold canonical home; four-regime operating-margin table |
| [`vol1/.../dielectric-rupture.md`](../../vol1/axioms-and-lattice/ch2-macroscopic-moduli/dielectric-rupture.md), `clm-9s9apq` | QED Schwinger $u_{sat}$ ↔ $p_c = 8\pi\alpha$ packing-fraction identity (substrate-mechanism anchor for $E_S$) |
| [`vol2/.../pair-production-axiom-derivation.md`](../../vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md), `clm-ezai5b` | Schwinger pair-production substrate-mechanism: A-B node-pair flux-tube rupture (NOT Breit-Wheeler) |
| [`vol1/.../four-regimes.md`](../../vol1/operators-and-regimes/ch7-regime-map/four-regimes.md), `clm-b2anl4`, `clm-2dwzib` | Regime I/II/III/IV universal classification; rupture = Regime IV |
| [`vol1/.../domain-catalog.md`](../../vol1/operators-and-regimes/ch7-regime-map/domain-catalog.md), `clm-82dxbj` | Per-domain control-parameter catalog; $B_{snap}$ magnetic-sector canonical home |
| [`vol3/.../mode-counting-heat-capacity.md`](../../vol3/condensed-matter/ch11-thermodynamics/mode-counting-heat-capacity.md), `clm-uu6dl5` | $T \sim m_e c^2 / k_B \approx 5.93 \times 10^9$ K thermal pair-production threshold; vacuum heat-capacity Debye-class roll-off |
| [`common/temporal-saturation-regime-classifier.md`](../../common/temporal-saturation-regime-classifier.md) | $T_{pair} = 2 m_e c^2/k_B$ thermal-decoherence engineering threshold for topological qubits |
| `src/ave/core/constants.py:333` (`V_SNAP`), `:342` (`V_YIELD`), `:347` (`E_CRIT`), `:353` (`E_YIELD`), `:359` (`B_SNAP`) | Canonical numerical constants (per `ave-canonical-source`) |

## Manuscript counterpart

`manuscript/vol_9_vacuum_datasheet/chapters/02_absolute_maximum_ratings.tex` (Vol 9 canonical chapter file; populated at this PR landing).

---
