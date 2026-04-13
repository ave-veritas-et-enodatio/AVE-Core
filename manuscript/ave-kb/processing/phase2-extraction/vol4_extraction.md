# Phase 2 Extraction Report — Vol 4 (Engineering)

**Volume**: `manuscript/vol_4_engineering/`
**Taxonomy skeleton**: `.claude/phase1-taxonomy/vol4_taxonomy.md`
**Base KB path**: `ave-kb/vol4/`
**Extraction date**: 2026-04-02
**Status:** Complete — all skeleton positions mapped

---

## 1. Source Directory Listing

All 18 chapter files confirmed present and mapped. One orphaned file confirmed excluded.

```
manuscript/vol_4_engineering/
  main.tex
  chapters/
    _manifest.tex                              (authoritative chapter list)
    01_vacuum_circuit_analysis.tex             → ch01
    02_topological_thrust_mechanics.tex        → ch02
    03_hopf_01_chiral_verification.tex         → ch03
    04_high_voltage_vhf_drive.tex              → ch04  [filename/slug mismatch — see §9]
    05_ponder_05_dc_biased_quartz.tex          → ch05
    06_vacuum_torsion_metrology.tex            → ch06
    07_topological_smes.tex                    → ch07
    08_applied_fusion.tex                      → ch08
    09_antimatter_annihilation.tex             → ch09
    10_quantum_computing_and_decoherence.tex   → ch10
    11_experimental_falsification.tex          → ch11
    12_falsifiable_predictions.tex             → ch12
    13_future_geometries.tex                   → ch13
    14_particle_decay_spice.tex                → ch14
    15_autoresonant_breakdown_spice.tex        → ch15
    16_sagnac_inductive_drag_spice.tex         → ch16
    17_hardware_netlists_spice.tex             → ch17
    18_active_topological_metamaterials.tex    → ch18
    circuit_sagnac_rlvg.tex                    ORPHANED — not in _manifest.tex
```

Shared input (pulled in from Ch.01):
- `manuscript/common/translation_circuit.tex` → `ave-kb/common/translation-circuit.md`

---

## 2. Domain Structure (from source)

| Domain slug | Source chapters |
|---|---|
| `circuit-theory` | Ch.01, Ch.02 |
| `hardware-programs` | Ch.03, Ch.04, Ch.05, Ch.06 |
| `advanced-applications` | Ch.07, Ch.08, Ch.09, Ch.10, Ch.18 |
| `falsification` | Ch.11, Ch.12 |
| `future-geometries` | Ch.13 |
| `simulation` | Ch.14, Ch.15, Ch.16, Ch.17 |

---

## 3. Skeleton-to-Source Mapping

### Domain: circuit-theory

#### ch01-vacuum-circuit-analysis
Source: `chapters/01_vacuum_circuit_analysis.tex`
Chapter label: none (no `\label{ch:...}` at chapter command)

| Skeleton leaf | Section / source region | Key label(s) |
|---|---|---|
| `index.md` | Chapter-level summary | — |
| `topological-kinematics.md` | sec:topo_kinematic (line 4) | `\label{sec:topo_kinematic}`, `\label{eq:xi_topo_vca}`, `\label{eq:charge_displacement}` |
| `nonlinear-vacuum-capacitance.md` | sec:vca_nonlinear (line 114) | `\label{sec:vca_nonlinear}`, `\label{eq:varactor}` |
| `z0-derivation.md` | sec:z0_derivation (line 243) | `\label{sec:z0_derivation}`, `\label{eq:cell_elements}`, `\label{eq:z0_cell}`, `\label{eq:c_from_lc}`, `\label{eq:z_mech}` |
| `relativistic-inductor.md` | Subsection within sec:z0_derivation | `\label{eq:relativistic_inductor}` |
| `tvs-transition.md` | Subsection within sec:z0_derivation | `\label{eq:tvs_transition}`, `\label{eq:skin_depth}` |
| `intermodulation-distortion.md` | sec:imd (line 553) | `\label{sec:imd}`, `\label{eq:im3_frequencies}`, `\label{eq:ip3}` |
| `translation-circuit.md` | `\input{../common/translation_circuit.tex}` (end of ch01) | `\label{tab:trans_circuit}` |

Note: `translation-circuit.md` maps to `ave-kb/common/translation-circuit.md` (shared), not a vol4-local leaf.

#### ch02-topological-thrust-mechanics
Source: `chapters/02_topological_thrust_mechanics.tex`
Chapter label: none

| Skeleton leaf | Section / source region | Key label(s) |
|---|---|---|
| `index.md` | Chapter-level summary | — |
| `regimes-of-operation.md` | sec:regimes_of_operation (line 10) | `\label{sec:regimes_of_operation}`, `\label{eq:e_yield}`, `\label{eq:jensen_rect}`, `\label{eq:e_local_peak}` |
| `chiral-thrust-derivation.md` | sec:chiral_thrust (line 50) | `\label{sec:chiral_thrust}`, `\label{eq:chiral_thrust}` |
| `thrust-summary.md` | summarybox + exercisebox boilerplate | boilerplate — see §7 |

---

### Domain: hardware-programs

#### ch03-hopf-01-chiral-verification
Source: `chapters/03_hopf_01_chiral_verification.tex`
Chapter label: `\label{ch:hopf_01}`

| Skeleton leaf | Section / source region | Key label(s) |
|---|---|---|
| `index.md` | Chapter-level summary | `\label{ch:hopf_01}` |
| `n-ave-derivation.md` | Winding number / arc-length derivation | `\label{eq:n_ave}`, `\label{eq:arc_length}` |
| `z0-wire-geometry.md` | Characteristic impedance of chiral wire | `\label{eq:z0_wire}` |
| `cross-section-moment.md` | Magnetic cross-section moment | `\label{eq:m_cross}` |
| `sm-baseline-table.md` | Comparison table | `\label{tab:sm_baseline}` |
| `sm-vs-ave-table.md` | SM vs AVE discriminators | `\label{tab:sm_vs_ave}`, `\label{tab:discriminators}` |
| `verification-protocol.md` | Experimental verification protocol section | — |

#### ch04-ponderomotive-program
Source: `chapters/04_high_voltage_vhf_drive.tex`
Chapter label: `\label{ch:design_evolution}`

| Skeleton leaf | Section / source region | Key label(s) |
|---|---|---|
| `index.md` | Chapter-level summary | `\label{ch:design_evolution}` |
| `pcba-to-quartz-evolution.md` | Program evolution narrative (full chapter prose) | — |
| `vhf-drive-topology.md` | High-voltage VHF drive topology section | — |

#### ch05-ponder-05-dc-biased-quartz
Source: `chapters/05_ponder_05_dc_biased_quartz.tex`
Chapter label: `\label{ch:ponder_05}`

| Skeleton leaf | Section / source region | Key label(s) |
|---|---|---|
| `index.md` | Chapter-level summary | `\label{ch:ponder_05}` |
| `dc-bias-mechanism.md` | DC bias theory section | — |
| `quartz-resonator-model.md` | Quartz LC model | — |
| `nonlinear-permittivity.md` | Nonlinear permittivity under bias | — |
| `drive-circuit-design.md` | Drive circuit design section | — |
| `experimental-results.md` | Experimental results / resultboxes | — |

#### ch06-torsion-metrology
Source: `chapters/06_vacuum_torsion_metrology.tex`
Chapter label: `\label{ch:torsion_metrology}`

| Skeleton leaf | Section / source region | Key label(s) |
|---|---|---|
| `index.md` | Chapter-level summary | `\label{ch:torsion_metrology}` |
| `torsion-balance-geometry.md` | Torsion balance geometry section | — |
| `vacuum-torque-derivation.md` | Torque derivation | — |
| `noise-floor-analysis.md` | Noise floor and sensitivity section | — |
| `metrology-protocol.md` | Measurement protocol section | — |

---

### Domain: advanced-applications

#### ch07-topological-smes
Source: `chapters/07_topological_smes.tex`
Chapter label: none (~57 lines total, confirmed brief)

| Skeleton leaf | Section / source region | Key label(s) |
|---|---|---|
| `index.md` | Chapter-level summary | — |
| `smes-topology.md` | Full chapter content (single resultbox + brief prose) | — |

Note: Ch.07 is confirmed sparse (57 lines). Only 2 leaves warranted.

#### ch08-applied-fusion
Source: `chapters/08_applied_fusion.tex`
Chapter label: `\label{ch:applied_fusion}`

| Skeleton leaf | Section / source region | Key label(s) |
|---|---|---|
| `index.md` | Chapter-level summary | `\label{ch:applied_fusion}` |
| `tokamak-paradox.md` | sec:tokamak_paradox (line 43) | `\label{sec:tokamak_paradox}` |
| `radius-scaling.md` | Radius scaling derivation | `\label{eq:radius_scaling}` |
| `temperature-scaling.md` | Temperature scaling derivation | `\label{eq:temp_scaling}` |
| `vtopo-scaling.md` | Topological velocity scaling | `\label{eq:vtopo_scaling}` |
| `gamow-compressed.md` | Gamow factor under compression | `\label{eq:gamow_compressed}` |
| `ignition-criterion.md` | n* ignition criterion | `\label{eq:n_star}` |
| `ave-fusion-device.md` | AVE-derived fusion device design section | — |
| `fusion-comparison-table.md` | Comparison table resultbox | — |

#### ch09-antimatter
Source: `chapters/09_antimatter_annihilation.tex`
Chapter label: `\label{ch:antimatter}`

| Skeleton leaf | Section / source region | Key label(s) |
|---|---|---|
| `index.md` | Chapter-level summary | `\label{ch:antimatter}` |
| `annihilation-mechanism.md` | Full chapter content (annihilation theory + resultboxes) | — |

Note: Ch.09 is brief; 2 leaves (index + single content leaf) as per taxonomy.

#### ch10-quantum-computing
Source: `chapters/10_quantum_computing_and_decoherence.tex`
Chapter label: `\label{ch:quantum_computing}`

| Skeleton leaf | Section / source region | Key label(s) |
|---|---|---|
| `index.md` | Chapter-level summary | `\label{ch:quantum_computing}` |
| `decoherence-as-impedance.md` | Decoherence reframed as impedance mismatch | — |
| `topological-qubit-model.md` | Topological qubit LC model | — |
| `error-correction-geometry.md` | Geometric error correction section | — |

#### ch18-active-topological-metamaterials
Source: `chapters/18_active_topological_metamaterials.tex`
Chapter label: `\label{ch:active_topological_metamaterials}`

| Skeleton leaf | Section / source region | Key label(s) |
|---|---|---|
| `index.md` | Chapter-level summary | `\label{ch:active_topological_metamaterials}` |
| `metamaterial-band-structure.md` | Band structure / topological band gap section | — |
| `active-feedback-design.md` | Active feedback topology section | — |

Note: Figure paths in this chapter reference `../../assets/sim_outputs/` — see Anomaly 9.

---

### Domain: falsification

#### ch11-experimental-bench-falsification
Source: `chapters/11_experimental_falsification.tex`
Chapter label: none

| Skeleton leaf | Section / source region | Key label(s) |
|---|---|---|
| `index.md` | Chapter-level summary | — |
| `achromatic-lens-test.md` | sec:achromatic_lens (line 416) | `\label{sec:achromatic_lens}` |
| `boundary-trapping-test.md` | sec:boundary_trapping (line 433) | `\label{sec:boundary_trapping}` |
| `vacuum-impedance-mirror.md` | sec:induced_vacuum_impedance_mirror (line 448) | `\label{sec:induced_vacuum_impedance_mirror}` |
| [19 additional leaves] | Earlier sections of Ch.11 (lines 1–415) | Various resultbox / tcolorbox environments |

Note: Ch.11 is the largest falsification chapter. The final three labeled sections map cleanly to leaves; the preceding ~415 lines contain the bulk of the bench test descriptions. Exact subsection-level boundaries should be confirmed by the distiller.

Dangling references confirmed in sec:induced_vacuum_impedance_mirror:
- `\ref{sec:topological_defects_lc}` — not defined anywhere in Vol 4
- `\ref{sec:point_yield}` — not defined anywhere in Vol 4
- `\ref{eq:dielectric_saturation}` — not defined anywhere in Vol 4

These likely resolve to Vol 3. Distiller should note as unresolved for `vacuum-impedance-mirror.md`.

#### ch12-falsifiable-predictions
Source: `chapters/12_falsifiable_predictions.tex`
Chapter label: `\label{ch:falsifiable_predictions}`

| Skeleton leaf | Section / source region | Key label(s) |
|---|---|---|
| `index.md` | Chapter-level summary | `\label{ch:falsifiable_predictions}` |
| `dielectric-plateau-prediction.md` | "The EE Bench: The Macroscopic Dielectric Plateau" section | NO `\label{}` — see Anomaly 8 |
| [7 additional leaves] | Remaining prediction sections in Ch.12 | Various |

Note: `sec:ee_bench` label is absent from Ch.12 source. Inbound `\ref{sec:ee_bench}` from Ch.11 is a dangling reference.

---

### Domain: future-geometries

#### ch13-future-geometries
Source: `chapters/13_future_geometries.tex`
Chapter label: `\label{ch:future_geometries}`

| Skeleton leaf | Section / source region | Key label(s) |
|---|---|---|
| `index.md` | Chapter-level summary | `\label{ch:future_geometries}` |
| `high-q-chiral-antenna.md` | sec:high_q_chiral (line 88), sec:rx_antenna (line 112), sec:tx_coil (line 124) | `\label{sec:high_q_chiral}`, `\label{sec:rx_antenna}`, `\label{sec:tx_coil}`, `\label{eq:chiral_fom}`, `\label{eq:beltrami_lambda}` |
| `cem-methods-survey.md` | sec:cem_methods (line 165) | `\label{sec:cem_methods}`, `\label{eq:mom}`, `\label{eq:fem}`, `\label{eq:cma}` |
| `k4-tlm-simulator.md` | sec:k4_tlm (line 311) | `\label{sec:k4_tlm}`, `\label{eq:k4_scatter}` |
| `open-universe-boundaries.md` | Sections following sec:k4_tlm on PML/open-universe boundaries | — |

---

### Domain: simulation

#### ch14-leaky-cavity-particle-decay
Source: `chapters/14_particle_decay_spice.tex`
Chapter label: `\label{ch:particle_decay}`

| Skeleton leaf | Section / source region | Key label(s) |
|---|---|---|
| `index.md` | Chapter-level summary | `\label{ch:particle_decay}` |
| `theory.md` | Theory sections (LC cavity decay model) | — |
| `spice-netlist.md` | verbatim SPICE netlist `leaky_cavity.cir` in tcolorbox | — |

#### ch15-autoresonant-breakdown
Source: `chapters/15_autoresonant_breakdown_spice.tex`
Chapter label: `\label{ch:schwinger_autoresonance}`

| Skeleton leaf | Section / source region | Key label(s) |
|---|---|---|
| `index.md` | Chapter-level summary | `\label{ch:schwinger_autoresonance}` |
| `theory.md` | sec:nonlinear_ma_lattice + sec:spice_pll (lines 8–32) | — |
| `spice-netlist.md` | verbatim SPICE netlist `pll_breakdown.cir` (lines 54–79) | `\ref{fig:autoresonance_pll}` |

Key source for `spice-netlist.md` leaf:

```
\begin{tcolorbox}[colback=black!95!white, coltext=white, fontupper=\ttfamily,
    title=SPICE Netlist: Autoresonance (pll\_breakdown.cir)]
* Autoresonant PLL (Schwinger Limit) SPICE Model *
...
B1 N_VAC GND Q = {C0 * sqrt(1 - min((V(N_VAC)/V_yield)**2, 0.999))} * V(N_VAC)
L1 N_VAC GND {L0}
B_FREQ N_FREQ GND V = 1 / sqrt({L0} * {C0 * sqrt(1 - min((V(N_VAC)/V_yield)**2, 0.999))})
C_INT N_FREQ GND 1
R_INT N_FREQ GND 1G
B_DRIVE 0 N_VAC I = {Drive_Amp} * cos(V(N_FREQ))
.TRAN 10ns 200us
.END
\end{tcolorbox}
```

#### ch16-sagnac-inductive-drag
Source: `chapters/16_sagnac_inductive_drag_spice.tex`
Chapter label: `\label{ch:sagnac_inductive_drag}`

| Skeleton leaf | Section / source region | Key label(s) |
|---|---|---|
| `index.md` | Chapter-level summary | `\label{ch:sagnac_inductive_drag}` |
| `theory.md` | sec:rotating_lc_frame + sec:spice_differential_ring (lines 12–26) | — |
| `spice-netlist.md` | verbatim SPICE netlist `sagnac_ring.cir` (lines 50–71) | `\ref{fig:sagnac_inductive_drag}` |

Key source for `spice-netlist.md` leaf:

```
\begin{tcolorbox}[colback=black!95!white, coltext=white, fontupper=\ttfamily,
    title=SPICE Netlist: Sagnac Inductive Drag (sagnac\_ring.cir) - Single Node]
* Sagnac Effect SPICE Model (Node N Segment) *
...
.param L0=1uH C0=1pF S_DRAG=0.05
C_N NODE_N GND {C0}
V_SENSE NODE_N NODE_INT 0
B_IND NODE_INT NODE_N_PLUS_1 I = sdt( V(NODE_INT, NODE_N_PLUS_1) /
+ { IF( I(V_SENSE) > 0, L0*(1 - S_DRAG), L0*(1 + S_DRAG) ) } )
.TRAN 1ns 2us
.END
\end{tcolorbox}
```

#### ch17-hardware-netlists
Source: `chapters/17_hardware_netlists_spice.tex`
Chapter label: `\label{ch:hardware_netlists}`

| Skeleton leaf | Section / source region | Key label(s) |
|---|---|---|
| `index.md` | Chapter-level summary | `\label{ch:hardware_netlists}` |
| `ee-bench-netlist.md` | verbatim SPICE netlist `ee_bench.cir` in codebox | — |
| `ponder-01-stack-netlist.md` | verbatim SPICE netlist `ponder_01_stack.cir` in codebox | — |

Note: Ch.17 uses `codebox` (not `resultbox`) as the primary content environment. No resultboxes present.

---

## 4. PATH-STABLE Anchor Confirmation

**Item**: `vol4/future-geometries/ch13-future-geometries/k4-tlm-simulator.md`
**Required anchor**: `\label{sec:k4_tlm}`

**Status: CONFIRMED**

Source file: `manuscript/vol_4_engineering/chapters/13_future_geometries.tex`, **line 311**.

```latex
\section{K4-TLM: Native Lattice Dynamics Simulator}
\label{sec:k4_tlm}
```

This section contains the K4 scattering matrix definition (`\label{eq:k4_scatter}`):

$$S^{(0)}_{ij} = \frac{1}{2} - \delta_{ij}$$

The KB leaf at this path must carry a prose anchor comment referencing `sec:k4_tlm` so that inbound links from Vol 3 resolve correctly.

---

## 5. Outbound Reference Search: ch:network_solver (Vol 5)

**Query**: Does any file in `vol_4_engineering/` reference `ch:network_solver` or otherwise cite Vol 5?

**Result: NOT FOUND**

Searches performed across all `.tex` files in `manuscript/vol_4_engineering/`:
- `\ref{ch:network_solver}` — no matches
- `Volume~V`, `Volume V`, `Vol.*5`, `vol_5` — no matches

The outbound reference to Vol 5 listed in the taxonomy does not appear in the current Vol 4 source. Either a forward reference planned but not yet written, or a taxonomy annotation error. The taxonomy architect should adjudicate.

---

## 6. Empty Skeleton Positions

No skeleton positions are empty. All 18 chapters have source files. All leaf categories have identifiable source regions.

The following leaves require distiller judgment on exact subsection boundaries:

- `vol4/falsification/ch11-experimental-bench-falsification/` — leaves 4 through 21 (lines 1–415 of Ch.11): numerous bench test descriptions separated by prose headers but lacking `\label{}` keys. Distiller should use resultbox and tcolorbox environment boundaries as leaf boundaries.
- `vol4/hardware-programs/ch05-ponder-05-dc-biased-quartz/` — internal subsection boundaries not labeled.
- `vol4/hardware-programs/ch06-torsion-metrology/` — same as Ch.05.

---

## 7. Leaf Boundary Notes

**summarybox and exercisebox are boilerplate — do not become KB leaves.**

Every chapter ends with a `\begin{summarybox}` and `\begin{exercisebox}`. These are structurally identical across chapters 14–17 (boilerplate). They should not be extracted as leaf content.

**Primary named-result environments by domain**:
- `circuit-theory`, `hardware-programs`, `advanced-applications`, `falsification`, `future-geometries`: primary display environment is `resultbox{Title}`.
- `simulation` (Ch.14–Ch.17): primary display environment is `tcolorbox` (for SPICE netlists) or `codebox`. No `resultbox` environments in Ch.17.
- Ch.11 also uses bare `tcolorbox` (not `resultbox`) for the Sagnac phase equation and levitation mass equation — treat as leaf-level content.

**Figure references in Ch.18**: Figures reference `../../assets/sim_outputs/` relative to the chapter file. The distiller should replace figure references in Ch.18 leaves with a bracketed note: `[Figure: <filename> — see manuscript/assets/sim_outputs/]`.

---

## 8. Notation and Macro Notes

All custom macros are defined in `manuscript/structure/commands.tex` (shared across all volumes).

| Macro | Definition | Markdown rendering |
|---|---|---|
| `\Lvac` | Vacuum inductance per unit length | `$L_\text{vac}$` |
| `\Cvac` | Vacuum capacitance per unit length | `$C_\text{vac}$` |
| `\Zvac` | Vacuum characteristic impedance | `$Z_\text{vac}$` |
| `\Wcut` | Cutoff angular frequency | `$\omega_\text{cut}$` |
| `\lp` | Planck length | `$\ell_P$` |
| `\vacuum` | Vacuum operator (context-dependent) | `$\mathcal{M}_A$` |
| `\slew` | Slew rate | `$\dot{V}$` |
| `\planck` | Planck constant | `$\hbar$` |
| `\permeability` | Vacuum permeability | `$\mu_0$` |
| `\permittivity` | Vacuum permittivity | `$\varepsilon_0$` |
| `\impedance` | Impedance operator | `$\mathcal{Z}$` |

All defined with `\providecommand` — safe to re-input.

---

## 9. Anomalies

**Anomaly 1 (orphaned file)**: `chapters/circuit_sagnac_rlvg.tex` is present in the chapters directory but absent from `_manifest.tex`. Excluded from the KB.

**Anomaly 2 (missing ch: labels on Ch.01, Ch.02, Ch.07, Ch.11)**: Four chapters have no `\label{ch:...}` at their `\chapter{}` command. These chapters cannot be cross-referenced by label from other documents.

**Anomaly 3 (dangling refs in Ch.11 sec:induced_vacuum_impedance_mirror)**: Three references not defined anywhere in Vol 4: `\ref{sec:topological_defects_lc}`, `\ref{sec:point_yield}`, `\ref{eq:dielectric_saturation}`. Presumed Vol 3 forward references.

**Anomaly 4 (Ch.11 chapter reference error)**: Ch.11 prose states "as shown in Chapter 13" when referring to the charge-displacement identity defined in Ch.01. Source authoring error; distiller should use correct chapter number (Ch.01).

**Anomaly 5 (Ch.04 filename/slug mismatch)**: Source file is `04_high_voltage_vhf_drive.tex` but the chapter title is "The Ponderomotive Program: From PCBA to Quartz" and the skeleton slug is `ch04-ponderomotive-program`. Chapter label `\label{ch:design_evolution}` also does not match either.

**Anomaly 6 (Ch.15 summarybox boilerplate identical to Ch.16)**: The summarybox and exercisebox text in Ch.15 and Ch.16 are word-for-word identical except for the chapter-specific noun. Both are boilerplate and should not become KB leaves.

**Anomaly 7 (Ch.17 no resultboxes)**: Ch.17 uses only `codebox` environments for its SPICE netlists. The two leaves map directly to the two codebox environments.

**Anomaly 8 (sec:ee_bench label absent in Ch.12)**: The section "The EE Bench: The Macroscopic Dielectric Plateau" in Ch.12 has no `\label{}` command. The reference `\ref{sec:ee_bench}` in Ch.11 is therefore dangling. The distiller should add a prose note that this section is the target of the unresolved Ch.11 reference.

**Anomaly 9 (Ch.18 figure paths)**: Figures in Ch.18 reference `../../assets/sim_outputs/`. The distiller should replace figure references with bracketed notes.

**Anomaly 10 (ch:network_solver outbound reference not found)**: The taxonomy skeleton listed an outbound reference to `ch:network_solver` (Vol 5) expected in Vol 4. No such reference exists anywhere in the Vol 4 source. See §5.
