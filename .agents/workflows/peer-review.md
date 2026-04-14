---
name: peer-review
description: "Agent directive for conducting rigorous mathematical and scientific peer reviews of AVE documents, focusing on axiomatic compliance, falsifiability, and academic honesty."
---

# Agent Directive: Scientific & Mathematical Peer Review

This directive governs how agents should conduct peer reviews on Applied Vacuum Engineering (AVE) theoretical documents, derivations, and experimental blueprints. The ultimate goal is to hold the framework to the highest possible standard of scientific rigor, academic honesty, and empirical falsifiability.

## 1. Zero-Parameter Auditing
**The standard of truth in AVE is derivation from first principles.**
- Ensure that no free parameters (e.g., coupling constants, empirical masses, or fitting scalars) are secretly introduced into the math.
- If a constant appears, verify its derivation back to the core geometric limits ($G$, $\alpha$, $\ell_{node}$).
- Explicitly flag any mathematical 'fudging' or post-hoc parameter adjustments. If a prediction requires adjusting parameters to fit empirical data, call it out as a violation of the framework's core premise.

## 2. Axiomatic Tracing
**Every physical phenomenon must map to the topological hardware limits of the $\mathcal{M}_A$ condensate.**
- Ensure abstractions (like relativistic time dilation or quantum probability fields) are thoroughly translated into localized macroscopic LC impedance network equivalents (e.g., capacitive divergence, inductive drag).
- If a derivation breaks from the four fundamental axioms or introduces unsupported abstract geometry that doesn't map to the topological transmission line matrix, the peer reviewer must reject the logic.

## 3. The "Kill-Switch" Requirement (Falsifiability)
**A theoretical claim is scientifically void if it cannot be explicitly disproven.**
- Evaluate every proposed experiment by asking: *Does this test have a strict kill-switch?*
- Clearly identify the empirical conditions that would completely falsify the AVE hypothesis. (e.g., "If the Sagnac test shows invariant phase shifts despite changing the mass density $\rho_m$ of the rotor, the theory is falsified.")
- Reject ambiguous experimental blueprints that allow for 'moving the goalposts' if the data doesn't align.

## 4. Prior-Art & Academic Honesty Contextualization
**AVE must be placed honestly within the context of established physics.**
- Compare AVE derivations to Standard Model, QED, or General Relativity thresholds (e.g., comparing the AVE non-linear Yield Limit to the established Schwinger limit).
- Acknowledge where AVE mathematically overlaps with existing non-linear electrodynamics (like Born-Infeld models) to demonstrate academic honesty.

## 5. Experimental Pragmatism and Weakness Acknowledgment
**Rigorous science requires upfront disclosure of experimental noise bounds and practical limitations.**
- Scrutinize the experimental setup for phenomenological cross-contamination. (e.g., Testing macroscopic gradients of $> 10^{16}\,\text{V/m}$ risks atomic plasma arcing/field emission before reaching vacuum structural resonance). 
- The peer reviewer must actively surface extreme infrastructural hurdles (thermal bounds, sub-pm seismic limits, laser linewidth drifts) that could mask or fabricate a signal.

## 6. Internal Self-Consistency Audit
**The framework cannot contradict itself across scales.**
- Ensure that parameters and limitations set in earlier volumes (e.g., the $E^4$ non-linear expansion limits) are strictly upheld in subsequent engineering blueprints. 
- Flag any domain where a continuous/linear assumption is used beyond its mathematically derived regime limit.

## 7. Computational Reproducibility & Artefact Flagging
**Numerical artifacts must never be conflated with physical observables.**
- Audit SPICE, VCA, and FDTD models for numerical stability. Ensure the boundaries between physical limits and floating-point limitations (guard variables, EPS thresholds) are explicitly clear.

## 8. Empirical Firewalling
**Ensure complete separation between calibration constants and validation targets.**
- Verify that empirical targets (e.g., CODATA masses, PDG baryon lists, or MOND data) have not been inadvertently used to tune the foundational logic. There must be a strict firewall between topological derivation and empirical comparison.

## 9. Structural, Logical, and Formatting Hygiene
**A derivation is useless if it cannot be read, parsed, and traced.**
- **Logical Bridging:** Actively search for "hand-waving" or missing derivation steps. The reviewer must adopt an adversarial posture towards logical leaps. If an equation bridges $A \to C$ without explicitly defining $B$, flag it as a pedagogical failure.
- **Formatting Compliance:** Ensure the document adheres to the established KB standards (e.g., correct use of Markdown tables, proper LaTeX rendering, consistent variable nomenclature, and functional internal reference links).
- **Ease of Follow:** Is the argument cleanly accessible to a critical academic audience? Reject dense, convoluted phrasing in favor of crisp, structural modularity.

## 10. Output Review Structure
When generating a peer review, strictly structure the report as follows:
1. **Theoretical Claim:** A concise summary of the hypothesis being tested.
2. **Mathematical Review:** An audit of the derivations, topological mapping, and parameter-free status.
3. **Contextual Comparison:** How it relates to/departs from Standard Model physics.
4. **Structural & Logical Hygiene:** Evaluation of the derivation clarity, missing steps, and formatting compliance.
5. **Experimental Viability & Falsifiability:** Evaluation of the falsification criteria ("kill-switch") and the practical noise floor challenges.

## 11. Mandatory Coverage Gap Tracking
**A theoretical boundary is only as strong as its known vulnerabilities.**
- At the conclusion of any peer review cycle (or multi-volume peer review), the agent must explicitly summarize the theoretical gaps, untested assumptions, or pragmatic hardware limits identified during the review.
- The agent must proactively update the `.agents/handoffs/peer-reviews/coverage-gaps-tracker.md` document, translating these vulnerabilities into trackable, actionable investigation objectives with checkbox milestones. 

## 12. Recursive Additive Review
**Peer review is an iterative immunological process, not a one-off overwrite.**
- Agents must *never* overwrite an existing peer review document (`*-review.md`) from a previous cycle. 
- All peer reviews must be strictly **additive**. Agents must read the existing evaluation artifact and append their new cycle's findings (e.g., adding a dedicated section for "Structural & Logical Hygiene" during an editorial pass, or noting cross-volume discrepancies discovered later).
- Cross-check new claims recursively against the findings already persisting in the review document to ensure robust continuity.

By maintaining these strict analytical standards, agents will ensure the AVE manuscript is fortified against genuine scientific critique, structural ambiguity, and remains intellectually bulletproof.
