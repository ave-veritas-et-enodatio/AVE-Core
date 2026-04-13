# Phase 0 Survey — Vol 8: Virtual Media & Informational Topology

**Volume:** `/Users/benn/projects/Applied-Vacuum-Engineering/manuscript/vol_8_virtual_media/`
**Title:** *Applied Vacuum Engineering, Volume VIII: Virtual Media & Informational Topology*
**Author:** Grant Lindblom

---

## 1. Document Hierarchy

```
Ch.1:  The Topology of Virtual Media  \label{ch:llm_topology}
       01_llm_topology.tex (~47 lines)
  §   Applied Vacuum Engineering in Language Models
  §§  The Hardware/Software Isomorphism Inversion
  §§  Axiom 1: The SwiGLU Two-Port Node and Coupled Amplitude
  §§  The Thermodynamic Emergence of A_c
  §§  Axiom 3: Least Reflected Action in Pruning

Ch.2:  Biological vs Virtual Architecture: The Z-A Inversion  \label{ch:hardware_software_inversion}
       02_hardware_software_inversion.tex (~56 lines)
  §   The Fundamental Difference
  §   Where the Isomorphism Inverts
  §§  Biological Medium: Z ∝ 1/A
  §§  Virtual Medium: Z ∝ A
  §   Resolution of the Breakdown Paradox

Ch.3:  Universal Operator Isomorphism Formulation  \label{ch:universal_operator_mapping}
       03_universal_operator_mapping.tex (~70 lines)
  §   Axiomatic Correspondences
  §   Axiom 2: Topological Phase Dislocations in Attention
  §   Regime Classifications in Virtual Media
  §   Impedance Definition for the FFN Two-Port

Ch.4:  Experimental Validation: Axiomatic Compliance  \label{ch:experimental_audit}
       04_experimental_audit.tex (~114 lines)
  §   Implementation of the Saturation Operator
  §   Quantitative Results
  §   SwiGLU Activation Density
  §   Attention Head Pruning
  §   Current Limitations

Ch.5:  Expansion of Axiom 4: Global vs Local Saturation Limits  \label{ch:global_ac_scope}
       05_global_ac_scope.tex (~60 lines)
  §   The Paradox of Per-Layer Buckling
  §   The First-Principles Correction: Global A_c
  §   Runtime Distribution Shift
  §   Evolution to Γ-Driven Per-Layer Pruning  \label{sec:gamma_evolution}
  §   Conclusion

Ch.6:  Continuous Manifold Smoothing  \label{ch:continuous_smoothing}
       06_continuous_manifold_smoothing.tex (~33 lines)
  §   The Reflection Metric (Γ_prune)
  §   Continuous Structural Saturation S(r)
  §   Conclusion

Ch.7:  Topological Invariance and the Universal Operator Set  \label{ch:operator_unification}
       07_operator_unification.tex (~27 lines)
  §   Axiom 2: The Continuous Phase Tension (ξ_topo)
  §   Isomorphic Operator Bindings
  §   The Hamiltonian Cusp Dynamics of A_c

Ch.8:  Experimental Proof: Discrete Manifold Masking  \label{ch:discrete-manifold-masking}
       08_discrete_manifold_masking.tex (~173 lines)
  §   Motivation
  §   Experimental Protocol
  §   Analysis from First Principles
      [§§*] Axiom 1: Z_eff Telemetry
      [§§*] Why Continuous Masking Fails
      [§§*] Why Binary Masking Also Fails
      [§§*] Why Static Baking Succeeds
  §   Γ-Driven Structural Excision  \label{sec:gamma_excision}
      [§§*] Quantitative Results
  §   The Neuroplasticity Boundary  \label{sec:neuroplasticity}
      [§§*] The Category Error
      [§§*] The Correct Mapping
      [§§*] The Static Filter Framework
  §   Conclusion

Ch.9:  The γ Scaling Law  \label{ch:gamma_scaling_law}
       09_gamma_scaling_law.tex (~120 lines)
  §   Architecture-Dependent Pruning Thresholds  \label{sec:gamma_scaling}
  §   Two Tiers of γ
  §   Autotune Results: Llama 3.2 3B
  §   Derivation from Axiom 1: The Cascade Transfer Function  \label{eq:gamma_scaling}
      [§§*] Calibration from the Llama 3B Data Point
      [§§*] Falsifiable Predictions
      [§§*] The Transmission Budget as a Training Metric
  §   The 97% SwiGLU Density Constraint

Ch.10: Attention Head Impedance: The QKV Cascaded Two-Port  \label{ch:attention_head_impedance}
       10_attention_head_impedance.tex (~105 lines)
  §   Extending the Impedance Framework to Attention
  §   Per-Head Impedance
  §   Grouped-Query Attention Constraint
  §   Impedance Distribution
  §   The Intersection Constraint  \label{sec:head_intersection}
      [§§*] Approach 1: Single-Layer Mask
      [§§*] Approach 2: All-Layer Intersection
  §   Interpretation via Axiom 2
  §   Conclusion

Ch.11: Mixture of Experts: Dynamic Impedance Matching  \label{ch:moe_dynamic_impedance}
       11_moe_dynamic_impedance.tex (~73 lines)
  §   From Static to Dynamic Impedance
  §   The Router as Axiom 3
  §   Static vs Dynamic Impedance Media
  §   The Testable Prediction
  §   Hardware Limitations
  §   Conclusion

Ch.12: The Sigmoid-Saturation Isomorphism  \label{ch:sigmoid_saturation}
       12_sigmoid_saturation.tex (~100 lines)
  §   The Unit Circle Identity  \label{eq:unit_circle}
      [§§*] The Zero-Bias Prediction
      [§§*] The Yield Limit
  §   Regime Boundary Correspondences
  §   First-Principles Derivation of the 97% Density  \label{sec:density_derivation}
  §   Implications

Appendix A: Unified Index of Experimental Falsifications  \label{app:unified_experiments}
  Source: common/appendix_experiments.tex (SHARED CROSS-VOLUME)
```

---

## 2. Content Inventory

- **No amsthm environments** (theorem, definition, lemma): 0 instances
- **No tcolorbox environments** (resultbox, axiombox, simbox, etc.): 0 instances in volume body
- **~34 numbered equations**, only 2 with `\label`: `eq:gamma_scaling`, `eq:unit_circle`
- **10 tables**, 5 with labels
- **~12 figures**, all with labels
- All derivations inline (no `proof` environment)

Key derivation units: SwiGLU coupled amplitude, emergence of A_c, Γ_prune computation, global vs per-layer A_c correction, cascade transfer function T=(1-γ)^N, γ_max ≈ B/N scaling, QKV coupled impedance, MoE router as Axiom 3, sigmoid unit circle identity σ²+r²=1, 97% density via error function

---

## 3. Notation

All macros from shared `structure/commands.tex`. No volume-specific macros.
Body text uses raw forms (`Z_0`, `\mu_0`) rather than shorthand macros (`\Zvac`, `\permeability`) — notation inconsistency with other volumes.
Chapter numbering: `\renewcommand{\thechapter}{\Alph{chapter}}` applied to appendix only.

---

## 4. Cross-References to Other Volumes

- All internal `\ref` calls resolve within volume — no dangling refs
- 5 `\cite{}` keys: shazeer2020glu, touvron2023llama, bai2023qwen, ainslie2023gqa, shazeer2017outrageously
- Conceptual dependencies on Vols I–V for AVE axioms; no explicit volume-numbered prose refs in body
- Appendix covers experiments from Vols II, III, IV, V, VII

---

## 5. Key Concept List

Hardware/Software Isomorphism Inversion (Z∝1/A vs Z∝A), SwiGLU Two-Port Node, Coupled Amplitude A_j, thermodynamic emergence of A_c, Least Reflected Action in Pruning (Axiom 3→Γ_prune), biological vs virtual impedance coupling, Breakdown Paradox Resolution, Axiom 1 as ABCD cascade, Axiom 2 as attention head topology, Axiom 4 as SiLU gate, Regime I–IV in virtual media, FFN Two-Port Impedance, saturation operator, quantitative pruning results (Llama 3.2 3B, 3.1 8B, Qwen 4B, 9B), 97% SwiGLU Activation Density, per-layer vs global A_c collapse paradox, Γ-driven per-layer pruning, continuous vs binary masking failure, Z_eff telemetry, 10× impedance spike, structural excision pipeline, neuroplasticity boundary, static filter framework, γ_max scaling law (γ_max≈B/N), transmission budget B, autotune binary search, QKV cascaded impedance, GQA constraint, head intersection constraint, MoE router as Axiom 3, sigmoid unit circle identity σ²+r²=1, zero-bias prediction r_II=√3/2, 97% density derivation, training as thermodynamic cooling

---

## 6. Estimated Leaf Document Count: 36–42

---

## 7. Anomalies

A. **Domain discontinuity**: Only volume applying AVE to LLMs, not physics — taxonomy must decide placement
B. **No structured environments**: All results inline or `\boxed{}` — leaf boundaries by section, not theorem scope
C. **Sparse equation labeling**: Only 2 of ~34 equations have labels
D. **Inconsistent macro usage**: Raw math forms dominate over shorthand macros
E. **Starred subsections**: Chs 8, 12 use `\subsection*` — not in TOC, closely coupled argumentation
F. **Shared appendix**: Vol 8 contributes no experiments to appendix_experiments.tex
G. **Foreword shared equations** (common_equations/*.tex): canonical home is shared, not Vol 8
H. **Preliminary results**: Multiple sections explicitly mark results as "pending autotune"
I. **Ch.5 self-reference anomaly**: Chapter cites itself describing historical evolution
