# 🚀 Phase 2: Open Research Frontier

> ## 📜 HISTORICAL — 2026-04-19
>
> **This document predates the kb_audit remediation effort and is retained only for historical context.**
>
> - The opening claim *"the framework is strictly parameter-free and mathematically rigorous"* was **aspirational** at the time this was written. The kb_audit subsequently surfaced substantive gaps that have since been addressed via PRs #3–#9. The framework is **now genuinely parameter-free for α** (via the Ch 8 Golden Torus derivation in PR #3) but this document was written before that closure existed in the public repo.
> - **P2.8 (Running α)** is **partially addressed** by Ch 8 §sec:alpha_thermal_running, which derives the CMB-induced thermal running of α. The QED energy-scale running (different mechanism) remains open and is re-captured in `FUTURE_WORK.md` as G-3.
> - **P2.9b (Neutrino Δm² splitting)** remains open and is re-captured in `FUTURE_WORK.md` as G-4.
> - All other entries (Island of Stability, Dielectric Plateau hardware, Transient Solvers, Protein Folding Rate, Topological Entropy) remain open and are re-captured in `FUTURE_WORK.md` as G-5.
>
> **Canonical successor for the active queue:** [`FUTURE_WORK.md`](FUTURE_WORK.md).
> **Canonical current state:** [`CURRENT_STATE.md`](CURRENT_STATE.md).

---

The comprehensive peer-review and remediation phases for the Applied Vacuum Engineering framework are complete. The manuscript and codebase are structurally sound, strictly parameter-free, and mathematically rigorous.

This document serves as the sole tracking manifest for the remaining theoretical boundaries. These items are *not* broken code or logical contradictions; they are genuine research domains that require novel extensions to the mathematical operator set.

## 🔴 Primary Theoretical Frontiers (Core Physics)

These two items represent the final gaps in predicting the standard model particle properties from pure vacuum metrics:

- [ ] **P2.8: The Running Fine Structure Constant (Vacuum Polarization)**
  - **Objective:** Derive the precise energy-dependent scaling of the fine structure constant ($\alpha$).
  - **Blocker:** Requires formulating the vacuum polarization tensor ($\Pi_{\mu\nu}$) purely from LC lattice deformation mechanics, without borrowing from QED perturbation integrals.
  - **Handoff Context:** [Book 2: Ch 10 - Open Problems.](file:///manuscript/vol_2_subatomic/chapters/10_open_problems.tex)

- [ ] **P2.9b: Neutrino Mass-Squared Splitting Mechanics (Lemma 5)**
  - **Objective:** Prove the relationship $\Delta m^2_{31} = M_\nu^2$, allowing the derived junction coupling ratio ($7/235 = 0.0298$) to perfectly close against the $\Delta m^2_{21} / \Delta m^2_{31}$ PDG measurements.
  - **Blocker:** The three conventional routes (MSW resonance, Superconducting Saturation, SSH Zero Mode) were rigorously evaluated and proved structurally impossible within the current framework. Establishing this metric link remains a deep mathematical frontier.
  - **Handoff Context:** [Book 2: Ch 06 - Electroweak Theory.](file:///manuscript/vol_2_subatomic/chapters/06_electroweak_and_higgs.tex)

## 🔬 Target Application Frontiers (Volumes 3-6)

These are specific applied milestones targeted for future feature branches:

- [ ] **1C: Island of Stability Formulation**
  - **Objective:** Predict $1/d_{ij}$ summation mass-defect limits for theoretical superheavy elements (e.g., $Z=114, 120, 126$) to serve as future falsifiable targets.
- [ ] **2C: Dielectric Plateau Hardware Blueprint**
  - **Objective:** Produce a definitive hardware specification (with component SPICE validation) capable of reliably measuring the topological $S_{11}$ shift without material breakdown at high node voltages.
- [ ] **3B: Transient State Solvers**
  - **Objective:** Upgrade the macroscopic numerical $S_{11}$ minimization engine to track continuous conformational transient trajectories, rather than just solving for absolute topological minima.
- [ ] **3C: Protein Folding Rate ($k_f$) Derivations**
  - **Objective:** Analytically derive classical protein folding speeds and continuous thermodynamic friction using Kuramoto phase-locking logic applied across massive molecular arrays.
- [ ] **4A-4C: Topological Entropy & Black-Body Continuums**
  - **Objective:** Formally define statistical irreversibility (The Second Law) strictly as a deterministic impedance mismatch and phase dissipation metric inside the $\mathcal{M}_A$ lattice. Write the explicit `Topological Entropy Operator` into the Python engine.
