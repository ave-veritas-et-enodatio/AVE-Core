[↑ Computational Mass Defect](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-o9xphr]
-->

## Network Analytics: Q-Factor and S-Parameters

By defining the topology natively as a reactive grid, the analysis can be pushed far beyond static mass to reveal the dynamic stability of the nuclei using classical RF (Radio Frequency) terminology: **Quality Factor ($Q$)** and **Scattering Cross-Section ($S_{11}$)**.

### Topological Quality Factor ($Q$) and Resonance

In an LC tank, the Quality Factor ($Q$) defines the ratio of stored reactive energy to the energy dissipated per rotational oscillating cycle. A high-$Q$ circuit rings perfectly and is highly stable; a low-$Q$ circuit is lossy and chemically reactive.

Within the AVE framework, "dissipation" here is **boundary/aperture radiative delivery** — energy leaving the defect *through its geometric perimeter* into the surrounding lattice, an Axiom-3-legal **port**, not a bulk friction inside the knot. $Q$ is calculated as the ratio of Total Internal Mutual Inductance ($U_{stored}$) to the Effective Topological Radius ($R_{eff}$).

> **⚑ Mechanism relabel — 2026-08-04 (ruling execution; the sentence above is the relabelled form, git carries the prior wording).** The prior wording read *"acoustic drag (vacuum friction)"*, which is bulk-loss vocabulary for a boundary object and invites a crossing-resistor reading Axiom 3 forbids (`eq_axiom_3.tex:24`: *"any apparent loss must be a boundary-radiation or mode-conversion channel, **never a bulk resistive one**"*). **The mechanism was identified, not invented here:** the 2026-07-17 Regime-IV dissipation audit graded this exact leaf **RADIATIVE-PORT / `requires_R` = port-only** and recommended, verbatim, *"relabel the loss term as boundary/aperture radiative loading to match the computation"* (`research/2026-07-17_regime-iv-dissipation-audit_items.json`). Under the [transfer-cost theorem](../../../common/transfer-cost-theorem.md) (`clm-xfrcst`) this is **delivery mode 1** — the far-field/radiative port — and delivery is **not** dissipation: the substrate does not heat, the energy leaves.
>
> **★ The honest caveat the audit also recorded, carried here rather than dropped.** The tabulated $Q$ **contains no dissipated-power term at all**: it is $U_{stored}/R_{eff}$, a stored-reactive-energy-over-geometric-length ratio, so it ranks **topological compactness / confinement**, not a computed leak rate. The port is therefore *named in prose and not computed* — the same evidence that rejects the bulk-friction reading also declines to certify a quantitative port. Read the $Q$ column as a confinement index (He-4 19.19 tight, Li-7 2.85 leaky), and do not read it as $\omega U/P$.



The symmetric Helium-4 core has the highest $Q$-factor ($19.19$) in this set, consistent with the alpha particle's exceptional stability. Conversely, the vast asymmetrical spatial gap in Lithium-7 causes its $Q$-factor to plummet ($2.85$), making its outer shell highly susceptible to decay or chemical bonding. Beryllium-9's endothermic bridge topology manages a moderate $Q$-factor ($7.93$).

### Topological S-Parameters ($S_{11}$)

When high-energy physicists measure the "Scattering Cross-Section" of a nucleus via particle bombardment, they are explicitly measuring its $S_{11}$ reflection parameter. This is a pure function of the topological bounding footprint (Area $\propto \pi r^2$) of the localized impedance defect.

Because of the massive $\sim 9.72d$ secondary shell offset in Lithium-7, it exhibits a markedly larger theoretical $S_{11}$ radar scattering cross-section compared to all preceding elements. A physical photon or neutron wave hitting $^7$Li has an exponentially higher probability of striking an impedance mismatch and scattering than it does hitting the ultra-compact $^4$He Alpha core.

[Figure: ee_network_analysis.png — see manuscript/vol_6_periodic_table/figures/]

**EE Network Parameter Analysis.** *Left:* The symmetric $^4$He Alpha topology holds the maximum theoretical $Q$-Factor (extreme stability), dwarfing the chemically reactive $^7$Li structure. *Right:* The massive secondary shell in Lithium-7 generates a catastrophic $S_{11}$ scattering cross-section relative to Helium's compact acoustic profile.

---
