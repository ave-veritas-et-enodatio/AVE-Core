[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
subtree-experiments: []
-->

# Ch.8 Breakdown Characteristics

Chapter 8 of the Vol 9 datasheet documents the substrate's natural response to overdrive at the Axiom 4 kernel's Regime III/IV boundary. The chapter consolidates: (1) the two-threshold breakdown structure — $V_{yield} = \sqrt{\alpha}\, V_{snap} \approx 43.65$ kV at the macroscopic nonlinear onset (Regime II→III boundary) versus $V_{snap} = m_e c^2/e \approx 511$ kV at the absolute topological node-destruction limit (Regime IV); (2) the Miller multiplication identity $M(r) = 1/S(r)^2 = 1/(1-r^2)$ as the substrate's Regime III amplification law, structurally identical to the engineering avalanche-multiplication law at $n = 2$; (3) the Schwinger pair-production critical field $E_S = m_e^2 c^3/(e\hbar) \approx 1.32 \times 10^{18}$ V/m as the substrate-natural response to $A^2 \to 1$ at adjacent A/B K4 node pairs (saturated flux-tube rupture, NOT Breit–Wheeler); (4) the substrate-native bond-traversal time $\tau_{node} = \ell_{node}/c_0 \approx 1.29 \times 10^{-21}$ s as the lower bound on any breakdown-mediated switching event; (5) cosmological-scale rupture (BH event horizon = dielectric-rupture boundary; **BH interior = ruptured plasma**, NOT a separate sublattice, per the canonical translation-table entry at translation-circuit.md line 133); (6) the EE breakdown translation table (avalanche-photodiode gain / Geiger-mode / Zener / corona / arc / dielectric breakdown / TVS clamping) → substrate Regime III/IV primitives.

The chapter is a **synthesis chapter** per Vol 9 charter — no substrate primitive is re-derived. All derivations live in the cited canonical leaves; the chapter consolidates them into datasheet format.

## Primary canonical sources

- **Pair-production substrate mechanism (saturated flux-tube rupture; four-piece synthesis):** [`vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md`](../../vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md) (`clm-ezai5b`).
- **Schwinger / saturation-kernel WKB structural closure ($\exp(-\pi E_S/E)$ from $\int_0^1 \sqrt{1-A^2}\,dA = \pi/4$):** [`vol2/particle-physics/ch01-topological-matter/q-g18-schwinger-pair-wkb.md`](../../vol2/particle-physics/ch01-topological-matter/q-g18-schwinger-pair-wkb.md) (`clm-lj4ok5`).
- **Four-regime map (Regime III/IV boundary derivations; Miller multiplication identity; sector dependence):** [`vol1/operators-and-regimes/ch7-regime-map/four-regimes.md`](../../vol1/operators-and-regimes/ch7-regime-map/four-regimes.md) (`clm-2dwzib`, `clm-b2anl4`).
- **Two-threshold structure ($V_{yield}$ vs $V_{snap}$; engine-default selection):** [`vol4/circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md`](../../vol4/circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md) (`clm-0vxzfu`, `clm-trgqtf`).
- **Dielectric-rupture event horizon (cosmological-scale rupture; Schwarzschild radius = dielectric-saturation boundary):** [`vol3/gravity/ch03-macroscopic-relativity/dielectric-rupture-event-horizon.md`](../../vol3/gravity/ch03-macroscopic-relativity/dielectric-rupture-event-horizon.md) (`clm-ir8h78`).
- **Dielectric-rupture / $V_{snap}$ axiomatic-consistency identity ($p_c = 8\pi\alpha$ at QED Schwinger bound):** [`vol1/axioms-and-lattice/ch2-macroscopic-moduli/dielectric-rupture.md`](../../vol1/axioms-and-lattice/ch2-macroscopic-moduli/dielectric-rupture.md) (`clm-9s9apq`).
- **EE breakdown translation (Avalanche $V_{BR}$ row at line 353; BH-interior ruptured-plasma row at line 133):** [`common/translation-tables/translation-circuit.md`](../../common/translation-tables/translation-circuit.md) §9 (`clm-eemap1`).
- **Autoresonant Schwinger-bypass programme (bench-scale falsifier; Vol 4 PROJECT-ZENER-04):** [`vol4/falsification/ch12-falsifiable-predictions/autoresonant-dielectric-rupture.md`](../../vol4/falsification/ch12-falsifiable-predictions/autoresonant-dielectric-rupture.md).
- **Saturation-kernel context (Vol 9 Ch 7 datasheet counterpart):** [`vol9/ch7-saturation-characteristics/index.md`](../ch7-saturation-characteristics/index.md).
- **Absolute Maximum Ratings (Vol 9 Ch 2 datasheet counterpart; limit tabulation):** [`vol9/ch2-absolute-maximum-ratings/index.md`](../ch2-absolute-maximum-ratings/index.md).
- **Numerical constants:** `src/ave/core/constants.py` symbols `V_SNAP`, `V_YIELD`, `E_CRIT`, `E_YIELD`, `B_SNAP` per `ave-canonical-source` discipline (symbol-name cites; line numbers are unstable across `constants.py` renumbers).

## BH-interior framing (canonical preservation)

Per the canonical translation-table entry at [`translation-circuit.md`](../../common/translation-tables/translation-circuit.md) line 133 (**Black-hole-interior ruptured plasma** → **Plasma physics** at Vol 3 cosmology canonical), the BH interior is the substrate carried into Regime IV at cosmological strain — ruptured plasma, NOT a separate sublattice. The substrate is single-medium throughout; the Ch 8 chapter preserves this framing per project-memory canonical guidance.

## Manuscript counterpart

`manuscript/vol_9_vacuum_datasheet/chapters/08_breakdown_characteristics.tex` (populated Vol 9 Wave 2 sub-PR — Ch 8 buildout).

## Volume-scope classification

Per Vol 9 charter (synthesis volume; no primary derivations), this chapter's content is Class B (synthesis consolidation of canonical content) per `consistency-vs-emergence` v1.3. No emergence-class claims; no new substrate primitives proposed. The Miller multiplication identity $M = 1/S^2$ and the Schwinger field $E_S = m_e^2 c^3/(e\hbar)$ are both definitional identities of the Axiom 4 kernel evaluated at the Regime III and Regime IV operating points respectively, not measurements or emergence tests.

---
