---
name: peer-review
description: "Agent directive for conducting rigorous mathematical and scientific peer reviews of AVE documents, focusing on axiomatic compliance, falsifiability, and academic honesty."
---

# Agent Directive: Scientific & Mathematical Peer Review

This directive governs how agents should conduct peer reviews on Applied Vacuum Engineering (AVE) theoretical documents, derivations, and experimental blueprints. The ultimate goal is to hold the framework to the highest possible standard of scientific rigor, academic honesty, and empirical falsifiability.

## Prerequisites & Cross-Workflow Awareness

Before beginning a peer review, the agent MUST:
1. Read `LIVING_REFERENCE.md` and `src/ave/core/constants.py` for canonical constant definitions.
2. Check whether `/audit-math`, `/audit-latex`, or `/audit-code` has already been run against the target volume. If prior audit output exists, read it first and build on those findings — do not duplicate or contradict them.
3. The `/audit-full` orchestrator (`audit-full.md`) covers code → math → LaTeX hygiene. The peer review is a **higher-order scientific evaluation** that sits above those mechanical audits. It should reference their findings but focus on theoretical coherence, falsifiability, and pedagogical clarity.

---

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
- **Logical Bridging:** Actively search for "hand-waving" or missing derivation steps. The reviewer must adopt an adversarial posture towards logical leaps. If an equation bridges $A \to C$ without explicitly defining $B$, flag it as a pedagogical failure. **Cite the specific file and line number of every gap found.**
- **Formatting Compliance:** Open at least one source document per volume (`.md` or `.tex`) and verify internal reference links resolve, tables render, and variable nomenclature is consistent. Report broken references by file and line.
- **Ease of Follow:** Is the argument cleanly accessible to a critical academic audience? Reject dense, convoluted phrasing in favor of crisp, structural modularity.

## 10. Numeric Spot-Check Mandate
**Claims of accuracy must be independently verified, not taken on faith.**
- For each volume reviewed, the agent must independently compute at least **3 flagship constants or predictions** using `src/ave/core/constants.py` (or equivalent engine scripts) and compare against the manuscript's stated values.
- Document each spot-check as a table row:

| Constant | Manuscript Value | Engine Value | Match? |
|----------|-----------------|--------------|--------|

- If the engine cannot reproduce a manuscript value, flag it as a `SPOT-CHECK FAILURE` and escalate.

## 11. Minimum Depth Requirement
**Shallow reviews are worse than no review — they create false confidence.**
- Every chapter within the reviewed volume must receive at least one dedicated subsection in the review document.
- Each chapter subsection must contain:
    1. At least one specific equation or constant citation (not just a summary of the topic).
    2. A verdict on zero-parameter compliance for that chapter.
    3. At least one specific pedagogical or structural observation.
- If a volume has N chapters, the review document must have at least N topical subsections. Reviews that cover an entire volume in 2-3 broad paragraphs are rejected as insufficient.

---

## 12. Output Review Structure
When generating a peer review, strictly structure the report as follows:
1. **Theoretical Claim:** A concise summary of the hypothesis being tested.
2. **Mathematical Review:** An audit of the derivations, topological mapping, and parameter-free status.
3. **Contextual Comparison:** How it relates to/departs from Standard Model physics.
4. **Numeric Spot-Checks:** Table of independently verified constants.
5. **Structural & Logical Hygiene:** Evaluation of the derivation clarity, missing steps, and formatting compliance — with file/line citations.
6. **Experimental Viability & Falsifiability:** Evaluation of the falsification criteria ("kill-switch") and the practical noise floor challenges.

## 13. Mandatory Coverage Gap Tracking
**A theoretical boundary is only as strong as its known vulnerabilities.**
- At the conclusion of any peer review cycle (or multi-volume peer review), the agent must explicitly summarize the theoretical gaps, untested assumptions, or pragmatic hardware limits identified during the review.
- The agent must proactively update the `.agents/handoffs/peer-reviews/coverage-gaps-tracker.md` document, translating these vulnerabilities into trackable, actionable investigation objectives with checkbox milestones.
- **Priority tagging is mandatory.** Every gap must be tagged with a severity level:
    - `[P0 - Release Blocker]`: Must be resolved before public release (e.g., IP migration tasks).
    - `[P1 - Next Cycle]`: Should be addressed in the next review cycle (e.g., missing derivation steps).
    - `[P2 - Research Frontier]`: Long-term theoretical work (e.g., Thermodynamic Isomorphism).

## 14. IP Migration & Cross-Repo Tracking
**Proprietary hardware IP must be tracked with surgical precision.**
- When flagging content for migration to a private repository, the reviewer must specify:
    1. The **source file and line range** in `AVE-Core`.
    2. The **target repository** (e.g., `ave-veritas-et-enodatio/AVE-Hardware`).
    3. A **verification step** to confirm the migration was completed (e.g., "Verify file exists at `AVE-Hardware/docs/sagnac-rlve/`").
- IP migration items are always `[P0 - Release Blocker]`.

## 15. Strategic Condensation & Recursive Review
**Peer review is an iterative immunological process; documents must evolve, not proliferate.**
- **Single Source of Truth:** All peer reviews MUST be stored exclusively in the `.agents/handoffs/peer-reviews/` subfolder. No stray output documents should reside in the parent directory.
- **Naming Convention:** Volume-level reviews must follow the pattern `volX-<descriptor>-review.md`. Chapter-level deep dives, if needed, must be prefixed with their volume: `volX-chY-<descriptor>.md`. Orphaned files that break this convention must be merged or renamed.
- **Intelligent Condensation:** Agents must *never* arbitrarily overwrite an existing peer review document, nor should they create parallel fragmented documents (like `audit_volX.md`). Instead, all back-to-back reviews must be **merged** into the canonical volume review.
- **Merge Strategy:** 
    1. Look for redundant insights. If a new audit discovers the same mathematical triumph or gap as the existing review, do not append a duplicate bullet point. Instead, seamlessly integrate the new terminology or confirmation into the existing paragraph.
    2. Additive formatting: If applying a new analytical lens (e.g., a "Hygiene Pass" or an "Experimental Noise Review"), add a dedicated subsection for it to preserve the structural history.
    3. If an older gap identified in the document is resolved by a newer audit, the agent should cross it out or append an "[UPDATE: Resolved in Pass N]" note, preserving the context of the framework's evolution.

## 16. Manifest Compliance Matrix
**The manifest must prove what was actually audited, not just summarize results.**
- The `ave-comprehensive-peer-review-manifest.md` must include a compliance matrix showing which directive sections (1–15) were applied to each volume. Example:

| Volume | §1 Zero-Param | §3 Kill-Switch | §9 Hygiene | §10 Spot-Check | ... |
|--------|:---:|:---:|:---:|:---:|:---:|
| Vol 1 | ✅ | ✅ | ✅ | ❌ | ... |

- An `❌` in any cell is not a failure — it is an honest disclosure that guides the next review cycle.

---

By maintaining these strict analytical standards, agents will ensure the AVE manuscript is fortified against genuine scientific critique, structural ambiguity, and remains intellectually bulletproof.
