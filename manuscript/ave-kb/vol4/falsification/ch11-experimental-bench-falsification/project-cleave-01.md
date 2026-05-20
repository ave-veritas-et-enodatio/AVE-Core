[↑ Ch.11: Experimental Bench Falsification](../index.md)
<!-- leaf: verbatim -->

## Project CLEAVE-01: The Femto-Coulomb Electrometer

> ↗ See also: [`_orchestration/exp-c15-cleave-01.md`](../../../../_orchestration/exp-c15-cleave-01.md) — AVE-Core orchestration sub-epic for KiCad design + bench + measurement
>
> ↗ See also: [INVARIANT-C2 ξ_topo electromechanical transduction constant](../../../CLAUDE.md) — canonical definition of $\xi_{topo} = e/\ell_{node}$
>
> ↗ See also: [Translation-Tables: Circuit Analysis (Topo-Kinematic Identity)](../../../common/translation-tables/translation-circuit.md) — [Q]≡[L] full disciplinary translation

### The Hypothesis (Axiom 2 — Topo-Kinematic Isomorphism)

Per Axiom 2 (Topo-Kinematic Isomorphism, [Q] ≡ [L]) in [`vol1/axioms-and-lattice/ch1-fundamental-axioms/`](../../../vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md), Electrical Charge is mathematically identical to physical macroscopic spatial displacement: $Q \equiv \xi_{topo} \cdot x$ via the canonical electromechanical-transduction constant $\xi_{topo} = e/\ell_{node}$. Standard physics dictates that mechanically separating two uncharged plates in a hard vacuum generates exactly zero electrical charge. AVE explicitly predicts the generation of topological charge natively from the capacity of the spatial metric.

### The PCBA Implementation

An EE can validate this by designing a precision metrology board. The PCBA utilizes an ultra-low bias current electrometer operational amplifier (e.g., the Analog Devices ADA4530-1, 20 fA bias current). The non-inverting input is connected to an isolated, floating copper plate inside a vacuum chamber. The board utilizes strict guard rings and Teflon standoffs to eliminate parasitic leakage.

A commercial Piezoelectric (PZT) linear actuator is mounted to a grounded plate directly facing the floating plate. Using a high-precision DAC, the PZT actuator is stepped exactly $1.0\,\mu\text{m}$ away from the floating plate in under $100\,\text{ms}$.

### The Falsification Metric

By mechanically pulling the spatial gap apart by $1\,\mu\text{m}$, you are actively driving the fundamental capacitance of the discrete $\mathcal{M}_A$ LC network. The induced topological charge is analytically derived as:

$$
Q = \xi_{topo} \cdot x = (4.149 \times 10^{-7}\,\text{C/m}) \times 10^{-6}\,\text{m} = \mathbf{0.415\,\text{pC (picoCoulombs)}}
$$

Assuming a highly-controlled PCBA parasitic input capacitance of exactly $10\,\text{pF}$, the voltage readout step ($V = Q/C$) dictates a clean, instantaneous step of exactly **$41.5\,\text{mV}$** on the oscilloscope. If the oscilloscope registers $0.0\,\text{mV}$, the framework is falsified. If it reads exactly $41.5\,\text{mV}$ per micron of displacement, the foundational hardware constant of the universe has been validated on a tabletop.

### Discriminator vs standard piezoelectric / triboelectric effects

A standard capacitor with PZT actuator generates charge via mechanical strain on the dielectric (piezoelectric $d_{31}$ etc.) OR triboelectric contact charging. Both are dielectric-material-dependent. **The AVE-distinct discriminator**: the $\xi_{topo} \cdot x$ component scales LINEARLY with displacement (NOT with the dielectric's $d_{ij}$ coefficients) and is **dielectric-independent**. Discriminator test: vary dielectric without changing PZT displacement — standard EE predicts $Q$ varies with dielectric; AVE predicts the $\xi_{topo} \cdot x$ component is independent.

### Regime classification (per canonical regime taxonomy)

| Regime axis | C15-CLEAVE-01 classification |
|---|---|
| **Spatial Regime I-IV** (per [`four-regimes.md`](../../../vol1/operators-and-regimes/ch7-regime-map/four-regimes.md)) | **Regime I** — sub-yield linear; $E \ll E_{\text{yield}}$ at 41.5 mV / μm gap; $S(A) \to 1$ |
| **Power-Domain θ** (per [`orbital-friction-paradox.md`](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md)) | **Reactive cycling** — electrometer reads charge without dissipating; θ → 90° |
| **Temporal regime** (per [`temporal-saturation-regime-classifier.md`](../../../common/temporal-saturation-regime-classifier.md)) | **Lossless** — $\delta_{\text{AVE}} \to 0$; no saturation events during PZT step |

### ξ_topo cascade impact (largest single-row cascade in matrix per Matrix 1 Cascade column)

If C15-CLEAVE-01 fails (0.0 mV observed), the canonical ξ_topo electromechanical transduction constant fails → Ax2 dies → 6+ downstream rows fall:

- **B4-PROTEIN** (Ramachandran enforcement uses ξ_topo per Vol 5 protein-folding engine)
- **C9-LEVITATION** ($m_{max} = V_{yield} \cdot \xi_{topo} / g$)
- **C16-TORSION-05** (asymmetric sawtooth DC thrust uses ξ_topo)
- **B5-PONDER-01** (thrust uses ξ_topo at V_yield boundary)
- **B6-PONDER-02** (microwave bistatic probe uses ξ_topo)
- **B7-PONDER-05** (differential saturation parallax uses ξ_topo)

This is the **largest single-row cascade in the matrix**. F-severity (framework-killing) on a single observation.

### Outcome adjudication (Phase 4 of sub-epic [`exp-c15-cleave-01.md`](../../../../_orchestration/exp-c15-cleave-01.md))

| Outcome | Interpretation |
|---|---|
| **A**: $V_{out}$ matches $41.5 \,\text{mV/μm}$ within ADA4530-1 noise floor | **Ax2 confirmed at bench**. ξ_topo cascade (B4 + C9 + C16 + B5-7) all gain bench-scale corroboration. Major positive — foreword-promotion-grade. |
| **B**: $V_{out}$ detected but slope differs from $41.5 \,\text{mV/μm}$ | Partial — topological charge-length identity holds qualitatively; coefficient revision needed |
| **C**: $V_{out} \approx 0$ within noise floor | **Ax2 dies. Framework falsified at substrate-foundational axiom level.** Cascade walk-back across ξ_topo family. |
| **D**: Confound (parasitic leakage / triboelectric / outgassing) | Re-design with better guards; re-test |

### Engineering substrate status (2026-05-20)

PCBA spec exists in this leaf; **no KiCad / no hardware in any AVE repo** yet. Phase 1 of sub-epic is KiCad design from this spec + ADA4530-1 evaluation board reference + vacuum-chamber interface design. ~$1-5k bench cost. Per [`_orchestration/exp-c15-cleave-01.md`](../../../../_orchestration/exp-c15-cleave-01.md), Phase 0 scoping decision pending.

### Engine constants reference

$\xi_{topo} = e/\ell_{node}$ canonical numerical value at [`src/ave/core/constants.py`](../../../../../src/ave/core/constants.py) — verify before any KiCad design starts per `ave-canonical-source` discipline.

---
