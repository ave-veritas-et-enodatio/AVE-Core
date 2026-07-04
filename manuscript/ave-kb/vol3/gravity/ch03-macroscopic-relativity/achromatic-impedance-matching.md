[↑ Ch.3 Macroscopic Relativity](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-rd9cjm]
path-stable: "referenced from vol3 as sec:achromatic_matching"
-->

---

## Achromatic Impedance Matching

A critical property of astrophysical gravity is that it behaves as a transparent lens. If gravity is an optical dense metric where the speed of light decreases locally ($c' = 1/\sqrt{\epsilon' \mu'} = c/n(r)$), classical optics predicts that light should suffer partial reflection when crossing an impedance gradient ($Z_1 \neq Z_2$).

In the AVE framework, this is resolved because the geometric polarization of the LC network scales its dual reactive components symmetrically. The absolute values of local magnetic permeability ($\mu$) and dielectric permittivity ($\epsilon$) both scale directly and proportionately with the local scalar strain:

> **[Resultbox]** *Symmetric Impedance Scaling*
>
> $$
> \mu' = n(r)\mu_0 \quad \text{and} \quad \epsilon' = n(r)\epsilon_0
> $$

Consequently, while the local phase velocity is reduced ($c' = 1/\sqrt{n^2\mu_0 \epsilon_0} = c/n(r)$), the local characteristic transverse impedance of the vacuum **remains strictly invariant**:

> **[Resultbox]** *Achromatic Impedance Matching*
>
> $$
> Z_0' = \sqrt{\frac{\mu'}{\epsilon'}} = \sqrt{\frac{n(r)\mu_0}{n(r)\epsilon_0}} = \sqrt{\frac{\mu_0}{\epsilon_0}} \equiv Z_0 \approx 376.73\ \Omega
> $$

Because the transverse impedance ratio is preserved across all gravitational gradients, the spatial vacuum operates as an **Achromatic Impedance-Matched Lens**. This guarantees that propagating transverse light diffracts and bends through deep gravity wells without suffering chromatic dispersion, internal scattering, or boundary back-reflection.

> **↗ Sibling condition (2026-07-04, PR #516 MERGED — the parent-condition derivation): the elastic axial↔shear BALANCE is the translational-elastic sibling of this EM match.** The $\varepsilon\!=\!\mu$ symmetric scaling / $Z_0$-invariance ($\Gamma_{EM}=0$) that makes this the achromatic **EM** match, and the srs net's **elastic** bond-isotropy balance $k_s=k_a$ (axial-stiffness $k_a$ = shear-stiffness $k_s$), are **siblings under the same parent — Axiom 3 (the Minimum Reflection Principle, boundary form: minimise $|\Gamma|^2$ at every internal impedance boundary; [`axiom-definitions.md`](../../../vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md):48).** Different sectors (transverse-EM cap↔ind here; translational-elastic axial↔shear there), one principle: each is the operating point where the internal-boundary reflection vanishes. The elastic balance is derived knob-free ($\rho_{bond}=k_a/k_s=1$ to machine precision). (Honest flag, mirrored from the source: the elastic $\rho_{bond}=1$ match is a **lossless-reactive photon operating point** — $K<0$, mechanically **unstable** per the `srs-elastic-tensor` result ($K<0$ for $\rho<2$) — **not** a stable static elastic solid; the matter sector sits at a different, mechanically-stable $\rho^\ast$.) See also the EM-side twin [`z0-derivation.md`](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md). Provenance: [`research/2026-07-04_parent-condition-match-forces-balance_result.md`](../../../../../research/2026-07-04_parent-condition-match-forces-balance_result.md).

---
