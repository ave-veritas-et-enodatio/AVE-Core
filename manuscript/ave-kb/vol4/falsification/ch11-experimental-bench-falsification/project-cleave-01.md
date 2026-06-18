[↑ Ch.11: Experimental Bench Falsification](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-ydksh6]
exp-id: exp-742kv5
status: pending
strengthens:
  - clm-ydksh6: 1.0
-->

## Project CLEAVE-01: The Femto-Coulomb Electrometer

> ↗ See also: [`_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01.md`](../../../../../_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01.md) — AVE-Core orchestration sub-epic for KiCad design + bench + measurement
>
> ↗ See also: [INVARIANT-C2 ξ_topo electromechanical transduction constant](../../../CLAUDE.md) — canonical definition of $\xi_{topo} = e/\ell_{node}$
>
> ↗ See also: [Translation-Tables: Circuit Analysis (Topo-Kinematic Identity)](../../../common/translation-tables/translation-circuit.md) — [Q]≡[L] full disciplinary translation

### The Hypothesis (Axiom 2 — Topo-Kinematic Isomorphism)

Per Axiom 2 (Topo-Kinematic Isomorphism, [Q] ≡ [L]) in [`vol1/axioms-and-lattice/ch1-fundamental-axioms/`](../../../vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md), Electrical Charge is mathematically identical to physical macroscopic spatial displacement: $Q \equiv \xi_{topo} \cdot x$ via the canonical electromechanical-transduction constant $\xi_{topo} = e/\ell_{node}$. The polarity-odd, gap-INDEPENDENT charge component is classically $0.0$ — mechanically separating two equipotential, single-work-function, patch-free plates in hard vacuum liberates no net *gap-independent* charge. The raw vacuum charge, however, is NOT classically zero: contact-potential-difference (CPD / moving-Kelvin-probe, the dominant Casimir/Kelvin-probe systematic) gives a polarity-odd, gap-DEPENDENT term $\propto V_{CPD}/g^2$ (surface patch potentials), which the gap-sweep separates from the floor. AVE explicitly predicts the generation of topological charge natively from the capacity of the spatial metric, gap-independent, on top of (and separable from) the classical CPD background.

### The PCBA Implementation

An EE can validate this by designing a precision metrology board. The PCBA utilizes an ultra-low bias current electrometer operational amplifier (e.g., the Analog Devices ADA4530-1, 20 fA bias current). The non-inverting input is connected to an isolated, floating copper plate inside a vacuum chamber. The board utilizes strict guard rings and Teflon standoffs to eliminate parasitic leakage.

A commercial Piezoelectric (PZT) linear actuator is mounted to a grounded plate directly facing the floating plate. Using a high-precision DAC, the PZT actuator is stepped exactly $1.0\,\mu\text{m}$ away from the floating plate in under $100\,\text{ms}$.

### The Falsification Metric

By mechanically pulling the spatial gap apart by $1\,\mu\text{m}$, you are actively driving the fundamental capacitance of the discrete substrate LC network. The induced topological charge is analytically derived as:

$$
Q = \xi_{topo} \cdot x = (4.149 \times 10^{-7}\,\text{C/m}) \times 10^{-6}\,\text{m} = \mathbf{0.415\,\text{pC (picoCoulombs)}}
$$

Assuming a highly-controlled PCBA parasitic input capacitance of exactly $10\,\text{pF}$, the voltage readout step ($V = Q/C$) dictates a clean, instantaneous step of exactly **$41.5\,\text{mV}$** on the oscilloscope. If the oscilloscope registers $0.0\,\text{mV}$, the framework is falsified. If it reads exactly $41.5\,\text{mV}$ per micron of displacement, the foundational hardware constant of the universe has been validated on a tabletop.

### Discriminator vs standard piezoelectric / triboelectric effects (two-sided)

A standard capacitor with PZT actuator generates charge via mechanical strain on the dielectric (piezoelectric $d_{31}$ etc.) OR triboelectric contact charging. Both are dielectric-material-dependent. **The AVE-distinct discriminator is two-sided**, framed on the $\xi_{topo}$ floor at **fixed input capacitance $C_{in}$**:

- **P1 (presence):** is there a non-zero, **gap-independent** charge floor at all from displacement of *uncharged* matter in clean vacuum? The polarity-odd, gap-INDEPENDENT component is classically $0.0$ mV; the raw vacuum charge is NOT — contact-potential-difference (CPD) gives a polarity-odd, gap-DEPENDENT term ($\propto V_{CPD}/g^2$, the dominant Casimir/Kelvin-probe systematic), separated from the floor by the gap-sweep. AVE predicts the $\xi_{topo}\cdot x = 41.5$ mV/μm floor as the **gap-independent** ($e/\ell_{node}$ is a pure constant) residue surviving the gap-sweep.
- **P2 (dielectric-invariance):** swap the dielectric in the gap at fixed $C_{in}$ — standard EE predicts $Q$ varies with the dielectric's $d_{ij}$ (the piezo/tribo piece rides material); AVE predicts the $\xi_{topo}\cdot x$ floor is the **fixed** (dielectric-invariant) component, with the material-dependent piece riding on top of it. The two-sided test reads the floor as the invariant residue under material swap.

**Node-occupation gap — CLOSED (2026-06-03).** P2's dielectric-invariance rests on the solid-dielectric **node-occupation** case (does the Pauli-saturated occupancy of the dielectric's atoms perturb the floor?). This was green-field; it is now closed by substrate-native derivation at [`research/2026-06-03_topological-charge-occupation-robustness.md`](../../../../../research/2026-06-03_topological-charge-occupation-robustness.md). Result: the floor **LOCKS**. The charge $\mathcal{Q} = \mathrm{Link}(\partial\Omega, \mathbf{F}_{\text{substrate}}) \in \mathbb{Z}$ is a **gap-protected integer** (boundary linking number — the no-hair observable, [`boundary-observables-m-q-j.md`](../../../common/boundary-observables-m-q-j.md)); the dielectric's atoms are bounded $\Gamma=-1$ soliton assemblies whose Pauli-filled interior occupancy is no-hair-INVISIBLE to the swept boundary loop (Atom row of the boundary-observables table). The conversion $\xi_{topo} = e/\ell_{node}$ is a **frozen-metric unit-bridge** ($\ell_{node} = \hbar/m_e c$ is the electron Compton wavelength, unchanged by a slab in the gap). So the occupied-node fraction enters neither factor → the floor is dielectric-invariant. Grant's spine: node-occupation = Pauli exclusion = the Axiom-4 saturation ceiling (corpus-derived; boundary-collision form canonical at [`resonant-lc-solitons.md`](../../circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md), per-node-budget form PROVISIONAL per `vol2/claim-quality.md:1178`).

**Gap-protection precondition (itself a measurable prediction).** The protection holds *iff the dielectric preserves the substrate's topological gap.* Ordinary insulators (PTFE, fused silica, residual gas — deep Regime I, $S(A)\to1$) do, so the floor locks. A **gap-closing material** that drives the inter-atomic bulk toward the rupture boundary ($A^2\to1$, $V\to V_{snap}$) would break the continuous-deformation protection and shift the floor — a distinct, AVE-distinct, falsifiable boundary with no standard-physics counterpart. See derivation §4.

> **F2 precision note.** The gap-protection is on $\mathcal{Q}$ (the **integer** linking charge), NOT on $\xi_{topo}$ (the **unit-bridge**). The floor's invariance is "$\mathcal{Q}$ is a gap-protected integer + the conversion is a frozen-metric constant" — $\xi_{topo}$ is not itself a Chern number / topological invariant.

> **F3 $\sqrt{\alpha}$ note.** $\xi_{topo} = \sqrt{\alpha}$ in native units ([`research/_archive/L3_electron_soliton/45_lattice_impedance_first_principles.md` line 117](../../../../../research/_archive/L3_electron_soliton/45_lattice_impedance_first_principles.md)), so an isolated-$\xi_{topo}$ slope deviation (floor present but slope off — Outcome B) is also an $\alpha$-chain signal: cross-check against the $\alpha$-dependent rows before attributing a slope offset to $\xi_{topo}$ alone.

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

### Outcome adjudication (Phase 4 of sub-epic [`exp-c15-cleave-01.md`](../../../../../_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01.md))

| Outcome | Interpretation |
|---|---|
| **A**: $V_{out}$ matches $41.5 \,\text{mV/μm}$ within ADA4530-1 noise floor | **Ax2 confirmed at bench**. ξ_topo cascade (B4 + C9 + C16 + B5-7) all gain bench-scale corroboration. Major positive — foreword-promotion-grade. |
| **B**: $V_{out}$ detected but slope differs from $41.5 \,\text{mV/μm}$ | Partial — topological charge-length identity holds qualitatively; coefficient revision needed |
| **C**: $V_{out} \approx 0$ within noise floor | **Ax2 dies. Framework falsified at substrate-foundational axiom level.** Cascade walk-back across ξ_topo family. |
| **D**: Confound (parasitic leakage / triboelectric / outgassing) | Re-design with better guards; re-test |

### Engineering substrate status (2026-05-20 EOD++++++++++++++)

**Phase 1a-rev1 ✓ MERGED** at `AVE-Bench-FemtoElectrometer` main @ `7f9c721` (audit tag `audit/2026-05-20_phase-1a-rev1-atopile-walkback`). Clean atopile module-level imports from `AVE-Hardware-Modules` main @ `8b0626b` (audit tag `audit/2026-05-20_q-c15-12-stage-a-fix`). All C15 open questions Q-C15-01 through Q-C15-12 + Q1.2 + Q-HWMOD-04 CLOSED. Phase 1b PCB layout pending Grant manual KiCad GUI work; Phase 1c Gerbers via `kicad-cli`; Phase 2 fab + assembly (~$7670 BOM mid-range).

### Engineering substrate status (2026-05-20 EOD+++++++++)

PCBA spec exists in this leaf; **sibling repo `AVE-Bench-FemtoElectrometer` is LIVE at `https://github.com/ave-veritas-et-enodatio/AVE-Bench-FemtoElectrometer`** (private). Phase 0 ✓ COMPLETE + Phase 1a ✓ MERGED to main 2026-05-20 EOD+++++++++ at `331a778` (audit tag `audit/2026-05-20_phase-1a-kicad-design` at `6d6552f`). Phase 1a delivered: D1.1 ADA4530-1 reference-design notes + D1.2 finalized BOM ($7670 mid-range) with concrete Mouser/Digi-Key/KJL/LabX/PI/PiezoDrive SKUs + D1.3 KiCad schematic DRAFT + ASCII companion + D1.7 TEST_PROCEDURE refresh (KB-leaf prediction wording preserved verbatim) + D1.8 procurement SKU population + D1.9 ORDERING skeleton + D1.10 DESIGN_LOG. Grant adjudications: Q-C15-01 ✓ dedicated chamber (bell-jar/4''-6'' CF refurb, ≤10⁻⁶ Torr); Q-C15-07 ✓ dedicated FT2 PZT-drive feedthrough; Q-C15-08 ✓ dedicated PTFE-socket explicit floating-plate return; Q-C15-09 ✓ external-only ground via FT1 BNC shield (combined Q-C15-08+09 → all grounds explicit dedicated paths, no chamber wall in ground network); Q1.2 ✓ off-PCBA DAC + HV amp. Phase 1b pending Grant manual KiCad GUI (schematic ERC clean + PCB layout + guard-ring polygon + DRC); Phase 1c Gerbers via `kicad-cli`; Phase 2 fab + assembly (~$7670 full BOM mid-range). Per [`_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01.md`](../../../../../_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01.md) + [`_orchestration/experimental/c15-cleave-01/_archive/exp-c15-cleave-01-phase-0-scaffolding.md`](../../../../../_orchestration/experimental/c15-cleave-01/_archive/exp-c15-cleave-01-phase-0-scaffolding.md) + [`_orchestration/experimental/c15-cleave-01/_archive/exp-c15-cleave-01-phase-1-kicad-brief.md`](../../../../../_orchestration/experimental/c15-cleave-01/_archive/exp-c15-cleave-01-phase-1-kicad-brief.md) + [`_orchestration/experimental/c15-cleave-01/_archive/exp-c15-cleave-01-q-c15-01-chamber-scoping.md`](../../../../../_orchestration/experimental/c15-cleave-01/_archive/exp-c15-cleave-01-q-c15-01-chamber-scoping.md) + [`_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01-sim-audit.md`](../../../../../_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01-sim-audit.md).

### Engine constants reference

$\xi_{topo} = e/\ell_{node}$ canonical numerical value at [`src/ave/core/constants.py`](../../../../../src/ave/core/constants.py) — verify before any KiCad design starts per `ave-canonical-source` discipline.

---
