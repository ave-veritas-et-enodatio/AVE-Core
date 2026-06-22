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

Assuming a highly-controlled PCBA parasitic input capacitance of exactly $10\,\text{pF}$, the voltage readout step ($V = Q/C$) projects to a clean step of approximately **$41.5\,\text{mV}$** on the oscilloscope at $1\,\mu\text{m}$ — but **the slope magnitude is NOT the falsifiable axis** (see below). The slope is a consistency-class echo: $\xi_{topo} = \sqrt{\alpha}$ in native units AND $\ell_{node}$ is the electron Compton wavelength, so the $41.5\,\text{mV/µm}$ figure is doubly over-determined and a slope-match cannot by itself distinguish chord from $\alpha$-chain (F3 note). **What the bench tests — the chord — is the topological integer-charge floor**: a gap-INDEPENDENT, polarity-odd, material-independent, linear-in-$x$ charge component ($\mathcal{Q} = \mathrm{Link}(\partial\Omega,\mathbf{F}) \in \mathbb{Z}$) surviving a $\ge 4\times$ gap-sweep at fixed $C_{in}$, which no single classical mechanism can fake (the 4-corner conjunction). If no such gap-independent floor survives the sweep, the framework is falsified at Axiom-2. If the 4-corner floor survives, the **topological integer-charge chord** ($[Q] \equiv [L]$) has been validated on a tabletop — a two-sided, non-fakeable result. The slope value ($41.5\,\text{mV/µm}$) is a secondary corroborator of the over-determined $\xi_{topo}$ magnitude, not the test.

### Discriminator vs standard piezoelectric / triboelectric effects (two-sided)

A standard capacitor with PZT actuator generates charge via mechanical strain on the dielectric (piezoelectric $d_{31}$ etc.) OR triboelectric contact charging. Both are dielectric-material-dependent. **The AVE-distinct discriminator is two-sided**, framed on the $\xi_{topo}$ floor at **fixed input capacitance $C_{in}$**:

- **P1 (presence):** is there a non-zero, **gap-independent** charge floor at all from displacement of *uncharged* matter in clean vacuum? The polarity-odd, gap-INDEPENDENT component is classically $0.0$ mV; the raw vacuum charge is NOT — contact-potential-difference (CPD) gives a polarity-odd, gap-DEPENDENT term ($\propto V_{CPD}/g^2$, the dominant Casimir/Kelvin-probe systematic), separated from the floor by the gap-sweep. AVE predicts the $\xi_{topo}\cdot x = 41.5$ mV/μm floor as the **gap-independent** ($e/\ell_{node}$ is a pure constant) residue surviving the gap-sweep.
- **P2 (dielectric-invariance):** swap the dielectric in the gap at fixed $C_{in}$ — standard EE predicts $Q$ varies with the dielectric's $d_{ij}$ (the piezo/tribo piece rides material); AVE predicts the $\xi_{topo}\cdot x$ floor is the **fixed** (dielectric-invariant) component, with the material-dependent piece riding on top of it. The two-sided test reads the floor as the invariant residue under material swap.

**The 4-corner chord + mundane-faker rejection.** The non-fakeable signature is the conjunction of FOUR corners — {**linear**-in-$x$ ∧ **polarity-odd** ∧ **material-independent** ∧ **gap-INDEPENDENT**} surviving a $\ge4\times$ gap-sweep — because no single classical mechanism survives all four ([`2026-06-04_round2-adjudications.md:54`](../../../../../_orchestration/experimental/2026-06-04_round2-adjudications.md)):

| Mundane faker | Corner it fails | How separated |
|---|---|---|
| CPD / moving-Kelvin-probe (~21%-of-floor, itself polarity-odd) | gap-INDEPENDENT (CPD is $\propto V_{CPD}/g^2$) | $\ge4\times$ **gap-sweep**: CPD drops $\propto1/g^2$, floor stays flat |
| electrostriction / flexoelectric / secondary-piezo | polarity-ODD (these are even-in-$V$) | **polarity-reversal**: even fakers don't flip sign |
| triboelectric contact charging | static (tribo step **decays**) | **time-gating**: record relaxation profile |
| direct piezoelectric ($d_{ij}$) | material-INDEPENDENT (rides dielectric; zero in vacuum) | **dielectric-material swap** at fixed $C_{in}$ |

> **C_in-held-fixed subtlety (load-bearing).** The measured *voltage* floor is gap-independent only at **fixed readout capacitance** $C_{in}$. The gap-sweep MUST hold $C_{in}$ fixed (or explicitly account for it) or the gap-independence corner is contaminated (`2026-06-04_round2-adjudications.md:60`). This is a protocol-design requirement on the gap-sweep, not a separate physics claim.

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

If C15-CLEAVE-01 fails (no gap-independent integer charge floor survives the gap-sweep — Outcome C), the canonical ξ_topo electromechanical transduction constant fails → Ax2 dies → 6+ downstream rows fall:

- **B4-PROTEIN** (Ramachandran enforcement uses ξ_topo per Vol 5 protein-folding engine)
- **C9-LEVITATION** ($m_{max} = V_{yield} \cdot \xi_{topo} / g$)
- **C16-TORSION-05** (asymmetric sawtooth DC thrust uses ξ_topo)
- **B5-PONDER-01** (thrust uses ξ_topo at V_yield boundary)
- **B6-PONDER-02** (microwave bistatic probe uses ξ_topo)
- **B7-PONDER-05** (differential saturation parallax uses ξ_topo)

This is the **largest single-row cascade in the matrix**. F-severity (framework-killing) on a single observation.

### Outcome adjudication (Phase 4 of sub-epic [`exp-c15-cleave-01.md`](../../../../../_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01.md))

The GO/NO-GO gates on the **chord** (the 4-corner gap-independent integer floor), NOT the slope (the echo). The slope is a non-gating secondary corroborator inside Outcome A.

| Outcome | Adjudication axis | Interpretation |
|---|---|---|
| **A — chord confirmed (GO)** | 4-corner conjunction {linear-in-$x$ ∧ polarity-odd ∧ material-indep ∧ gap-INDEPENDENT} survives the $\ge4\times$ gap-sweep at fixed $C_{in}$; calibrated positive-control passed in-session | **Ax2 ([Q]≡[L]) topological-integer-charge chord confirmed at bench.** ξ_topo cascade (B4 + C9 + C16 + B5-7) gains bench-scale corroboration. Foreword-promotion-grade. *Secondary (non-gating): slope-match to 0.415 pC/µm strengthens the $\sqrt{\alpha}$/Compton echo; a slope deviation books as A-with-$\alpha$-chain-flag (F3), it does NOT demote the GO.* |
| **B — partial (chord ambiguous)** | floor detected (non-zero, polarity-odd, material-indep) but gap-sweep inconclusive ($C_{in}$ drift / too few gaps / floor not separated from $1/g^2$ CPD) | Integer-charge chord suggested but gap-independence corner not established. Re-run gap-sweep at fixed $C_{in}$, wider span. **NOT a GO.** |
| **C — null (chord falsified, NO-GO)** | no gap-INDEPENDENT floor survives the sweep — displacement charge absent within noise OR fully explained by the $\propto1/g^2$ CPD background — all §5 corners checked + positive-control passing | **Ax2 dies. Framework falsified at substrate-foundational axiom level.** Cascade walk-back across ξ_topo family. *A slope-deviation with the floor still gap-independent is A-with-flag, NOT C.* |
| **D — confound** | floor fails a corner (tracks dielectric / fails polarity-reversal / decaying tribo / fails zero-displacement null) OR positive-control did NOT register (dead-instrument null) | Re-design guards; re-test. NOT adjudicated A or C. |

### Femto-side (cross-repo) propagation status (2026-06-22)

The bench-engineering sibling `AVE-Bench-FemtoElectrometer` holds the hardware/test-procedure artifacts. The Femto repo's own round-2 analysis IS cured (`docs/analysis/2026-06-04_cleave-round2-smcounterfactual-result.md` + `prereg.md` on its **`main`**: SM "exactly 0.0" found FALSE at ~21%-of-floor CPD; gap-independence cure; 4-corner + faker tables; calibrated positive-control). **FLAG (SEPARATE session):** the Femto repo's default checkout still carries STALE round-1 framing in `hardware/TEST_PROCEDURE.md` / `docs/open_questions.md` / `docs/glossary.md` ("standard EE predicts Q→0"; slope/linearity discriminator, NOT 4-corner). Landing the gap-independence / 4-corner / positive-control framing across those stale Femto sites is a **Femto-repo edit, flagged for a SEPARATE session per cross-repo-session-scope — NOT performed in the AVE-Core revision that landed this leaf.** The round-2 doc itself flags this un-landed remainder (F-R2-3).

### Engineering substrate status (2026-05-20 EOD++++++++++++++)

**Phase 1a-rev1 ✓ MERGED** at `AVE-Bench-FemtoElectrometer` main @ `7f9c721` (audit tag `audit/2026-05-20_phase-1a-rev1-atopile-walkback`). Clean atopile module-level imports from `AVE-Hardware-Modules` main @ `8b0626b` (audit tag `audit/2026-05-20_q-c15-12-stage-a-fix`). All C15 open questions Q-C15-01 through Q-C15-12 + Q1.2 + Q-HWMOD-04 CLOSED. Phase 1b PCB layout pending Grant manual KiCad GUI work; Phase 1c Gerbers via `kicad-cli`; Phase 2 fab + assembly (~$7670 BOM mid-range).

### Engineering substrate status (2026-05-20 EOD+++++++++)

PCBA spec exists in this leaf; **sibling repo `AVE-Bench-FemtoElectrometer` is LIVE at `https://github.com/ave-veritas-et-enodatio/AVE-Bench-FemtoElectrometer`** (private). Phase 0 ✓ COMPLETE + Phase 1a ✓ MERGED to main 2026-05-20 EOD+++++++++ at `331a778` (audit tag `audit/2026-05-20_phase-1a-kicad-design` at `6d6552f`). Phase 1a delivered: D1.1 ADA4530-1 reference-design notes + D1.2 finalized BOM ($7670 mid-range) with concrete Mouser/Digi-Key/KJL/LabX/PI/PiezoDrive SKUs + D1.3 KiCad schematic DRAFT + ASCII companion + D1.7 TEST_PROCEDURE refresh (KB-leaf prediction wording preserved verbatim) + D1.8 procurement SKU population + D1.9 ORDERING skeleton + D1.10 DESIGN_LOG. Grant adjudications: Q-C15-01 ✓ dedicated chamber (bell-jar/4''-6'' CF refurb, ≤10⁻⁶ Torr); Q-C15-07 ✓ dedicated FT2 PZT-drive feedthrough; Q-C15-08 ✓ dedicated PTFE-socket explicit floating-plate return; Q-C15-09 ✓ external-only ground via FT1 BNC shield (combined Q-C15-08+09 → all grounds explicit dedicated paths, no chamber wall in ground network); Q1.2 ✓ off-PCBA DAC + HV amp. Phase 1b pending Grant manual KiCad GUI (schematic ERC clean + PCB layout + guard-ring polygon + DRC); Phase 1c Gerbers via `kicad-cli`; Phase 2 fab + assembly (~$7670 full BOM mid-range). Per [`_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01.md`](../../../../../_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01.md) + [`_orchestration/experimental/c15-cleave-01/_archive/exp-c15-cleave-01-phase-0-scaffolding.md`](../../../../../_orchestration/experimental/c15-cleave-01/_archive/exp-c15-cleave-01-phase-0-scaffolding.md) + [`_orchestration/experimental/c15-cleave-01/_archive/exp-c15-cleave-01-phase-1-kicad-brief.md`](../../../../../_orchestration/experimental/c15-cleave-01/_archive/exp-c15-cleave-01-phase-1-kicad-brief.md) + [`_orchestration/experimental/c15-cleave-01/_archive/exp-c15-cleave-01-q-c15-01-chamber-scoping.md`](../../../../../_orchestration/experimental/c15-cleave-01/_archive/exp-c15-cleave-01-q-c15-01-chamber-scoping.md) + [`_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01-sim-audit.md`](../../../../../_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01-sim-audit.md).

### Engine constants reference

$\xi_{topo} = e/\ell_{node}$ canonical numerical value at [`src/ave/core/constants.py`](../../../../../src/ave/core/constants.py) — verify before any KiCad design starts per `ave-canonical-source` discipline.

---
