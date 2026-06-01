[↑ Common Resources](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "definitional taxonomy disambiguating dark wake / τ^far_zx (thrust) vs dark resonance / Σ_near (g-2); no new physical claim"
path-stable: "referenced from vol2 Ch6 (g-2 dark resonance, Σ_near) and vol4 Ch2 (dark wake thrust, τ^far_zx) as the canonical genus/species disambiguation"
-->

# Dark Back-Reaction Taxonomy: Dark Wake (Thrust, τ^far_zx) vs Dark Resonance (g-2, Σ_near)

This is a **definitional / no-claim** leaf. It introduces no new physical result; it disambiguates a vocabulary collision. The label **"dark wake"** historically named TWO physically distinct substrate back-reaction phenomena that were originally written with a single shared $\tau_{zx}$ symbol on the basis of a longitudinal-shear *signature* resemblance. This leaf splits them under a shared genus, fixes the species names, **and gives each its own symbol** (near/far field-zone tags), recording that the shared symbol was a symbol-level conflation now resolved.

The split was forced by the 2026-05-31 FT-Dark-Wake-Cross-Scale result (Outcome C): the loop-scale ($g$-2) quantity and the bench-scale (thrust) $\tau_{zx}$ do **not** reconcile under the backward-wake dispersion $\partial_t = -c_0\partial_z$. The dimensional analysis behind Outcome C showed the conflation was not merely "two objects, one symbol" but a **symbol-level category error**: the $g$-2 quantity carries dimensions of reactive power per unit time ($V^2/\text{time}$), a self-energy *rate*, not a shear stress ($\text{N}\,\text{m}^{-2}$). See [`2026-05-31_FT-darkwake-crossscale_prereg.md`](../../../research/2026-05-31_FT-darkwake-crossscale_prereg.md).

## Genus — "dark [back-reaction]"

A **dark back-reaction** is a substrate-coupled, **non-radiating-into-observable-EM-modes** channel by which a soliton's reaction couples into the unseen lattice (the deposited momentum can still be mechanically observable — e.g. thrust — but it is not radiated as observable EM). "Dark" is used in the **dark-sector sense**: real momentum/energy is deposited into the hidden substrate $\mathcal{M}_A$ rather than radiated into observable far-field modes. The genus is the family; the two species below are the members, distinguished by **field zone** — **near** (reactive, bound, returns-to-source: the QED self-energy analogue) vs **far** (radiative, propagating: the radiation-reaction analogue). Their resemblance was a longitudinal-shear *signature* resemblance that drove the original single-symbol writing; on dimensional analysis they are not even the same kind of quantity (a self-energy rate vs a stress), so each now carries its own symbol (see [§Signature ≠ object](#signature--object)).

## Species 1 — dark wake (thrust) → **τ^far_zx**

**KEEP the phenomenon; tag the symbol far.** The **dark wake** is the **far-field radiated shear stress** $\tau^{\text{far}}_{zx}$ — the real-space longitudinal-shear trail behind a **moving** soliton. It propagates *outward* (backward) at substrate wave speed $c_0$ and carries the Newton-3rd-law reaction momentum that closes the thrust momentum-conservation loop ($P_{\text{wake}} = F \cdot c_0$). Its $\tau_{zx}$ IS a genuine Maxwell/Cauchy shear stress; the **far** tag marks it as the field-zone-radiative ($\int \tau\, dA = F$), propagating species. It is a real-space, motion-trail phenomenon: no motion, no wake.

- **Object:** real-space longitudinal shear stress (Ω-carrying / stress dimensions, $\text{N}\,\text{m}^{-2}$), $\tau^{\text{far}}_{zx} = \rho_{\text{Op14}}\, Z_{\text{vac}}\, \nabla|E|^2$.
- **Canonical home:** [`chiral-thrust-derivation.md`](../vol4/circuit-theory/ch2-topological-thrust-mechanics/chiral-thrust-derivation.md) (clm-7tynm2).
- **Status:** the name **dark wake** continues to denote this thrust motion-trail species only; its symbol is **$\tau^{\text{far}}_{zx}$** (far-field Maxwell shear stress).

## Species 2 — dark resonance (g-2) → **Σ_near / −Σ̇_near**

**NEW name + NEW symbol.** The **dark resonance** is the electron's **near-field reactive self-energy** — the retarded self-coupling of its own resonant loop (the QED self-energy analogue; Axiom-3 self-$\Gamma$). It is internal, **at rest**, and lives in the Cosserat $(2,3)$ phase space (d/q axes), not in real space. It produces the d/q saliency $\delta$ and the anomalous-moment two-loop coefficient $A_2$ (Petermann $C_2$).

The historic "$\tau_{zx} = -dV^2/dt$" written for this effect was a **MISLABEL**: dimensionally it is a reactive-power / self-energy **rate** ($V^2/\text{time}$), **not** a shear stress. Define $\Sigma_{\text{near}} \propto V^2$ (the near-field reactive self-energy); its retarded rate $-\dot\Sigma_{\text{near}} = -\,dV^2/dt$ is the old "$\tau_{zx}$" kernel. The **near** tag marks it as the field-zone-reactive (bound, returns-to-source) species.

- **Object:** the near-field reactive self-energy $\Sigma_{\text{near}} \propto V^2$; its retarded rate is the phase-space correlation integrand $-\dot\Sigma_{\text{near}}(t) = -\dfrac{dV^2}{dt}\Big|_{t-1/\omega_C}$ (dimensions $V^2/\text{time}$), entering $A_2 = \dfrac{2}{\pi\alpha}\langle (S_d - S_q)\,(-\dot\Sigma_{\text{near}})\rangle$.
- **Canonical home:** [`q-g19a-petermann-saliency-closure.md`](../vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md) (clm-v2sg8z).
- **Status:** the $g$-2 retarded-self effect previously called "dark wake" (and written with $\tau_{zx}$) is now **dark resonance**, symbol **$\Sigma_{\text{near}}$ / $-\dot\Sigma_{\text{near}}$**.

### ⚠ AMO-overlap note (do not collide with atomic-physics "dark resonance")

**"Dark resonance" is also an established atomic-physics term** — coherent population trapping (CPT) / electromagnetically induced transparency (EIT): a non-absorbing coherent **dark state** in a $\Lambda$-system, used in CPT atomic clocks. AVE's "dark resonance" is a **DIFFERENT** phenomenon — the substrate self-$\Gamma$ feedback of the electron's own resonant loop — not a coherent-population-trapping dark state. The two are **thematically kin only** (both senses of "dark" are non-radiating / non-absorbing), but they are not the same effect and must not be collided. When precision is needed, qualify as **"AVE dark resonance (substrate self-$\Gamma$)"** to distinguish from the AMO CPT/EIT dark resonance.

## Signature ≠ object

**Separate symbols (near/far field-zone tags).** dark wake → **$\tau^{\text{far}}_{zx}$** (far-field Maxwell shear stress, real-space, dim $\text{N}\,\text{m}^{-2}$); dark resonance → **$\Sigma_{\text{near}}$ / $-\dot\Sigma_{\text{near}}$** (near-field reactive self-energy, the rate dim $V^2/\text{time}$). The shared "$\tau_{zx}$" was a symbol-level conflation — the $g$-2 quantity is a reactive-power rate, not a stress — now resolved. The near/far tags mark field-zone: **near** = reactive, bound, returns-to-source (self-energy; reduced Compton $\lambda_C/2\pi = \ell_{\text{node}}$ is the near-zone radius); **far** = radiative, propagating (momentum trail). This is the QED self-energy (near) vs radiation-reaction (far) split.

Per the 2026-05-31 FT-Dark-Wake-Cross-Scale result (Outcome C), the two do **not** reconcile under the backward-wake dispersion $\partial_t = -c_0\partial_z$ — and the dimensional analysis shows *why* a single symbol was never tenable:

- the **dark-resonance** quantity $-\dot\Sigma_{\text{near}}$ is a phase-space self-energy rate (dimensions $V^2/\text{time}$);
- the **dark-wake** quantity $\tau^{\text{far}}_{zx}$ is a real-space shear stress (Ω-carrying / stress dimensions, $\text{N}\,\text{m}^{-2}$);

two different *kinds* of quantity, not merely two objects of one kind. The longitudinal-shear *signature* resemblance that originally drove the shared "$\tau_{zx}$" writing is a resemblance, not an identity.

## Shared ancestry

Both species trace to the **Axiom-4 saturation kernel** $S(A)$ and the **Op14 cross-sector-trading** mechanism (Cosserat $\omega \leftrightarrow$ K4 $\Phi_{\text{link}}$ energy exchange; see [`op14-cross-sector-trading.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md)). This is a shared **axiom / mechanism**, **not** a shared object — the floor of any AVE pair. Common ancestry in the kernel does not make $\Sigma_{\text{near}}$ and $\tau^{\text{far}}_{zx}$ one field, exactly as two distinct circuits built from the same component law are not one circuit.

## Migration note

> **"Dark wake" historically conflated both senses under one symbol.** It now denotes the **motion-trail (thrust)** species only (Species 1, real-space, moving soliton, $c_0$ reaction momentum), symbol **$\tau^{\text{far}}_{zx}$**. The **retarded-self ($g$-2) effect** is **"dark resonance"** (Species 2, phase-space, at rest, $A_2$ saliency), symbol **$\Sigma_{\text{near}}$ / $-\dot\Sigma_{\text{near}}$**. Per the LOCKED decision-B (separate symbols, near/far field-zone tags), the rename touches BOTH the phenomenon NAME and the SYMBOL in the $g$-2 derivation: the old "$\tau_{zx} = -dV^2/dt$" becomes $-\dot\Sigma_{\text{near}}$ (a reactive-power rate, not a stress). The thrust species keeps a genuine Maxwell shear stress, now tagged $\tau^{\text{far}}_{zx}$ at its definition. See the FT-Dark-Wake-Cross-Scale prereg ([`2026-05-31_FT-darkwake-crossscale_prereg.md`](../../../research/2026-05-31_FT-darkwake-crossscale_prereg.md)) for the Outcome-C result that forced the split.

## Cross-references

- [Chiral Thrust Derivation](../vol4/circuit-theory/ch2-topological-thrust-mechanics/chiral-thrust-derivation.md) — canonical home of **dark wake** (thrust, clm-7tynm2).
- [Q-G19α Petermann Saliency Closure](../vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md) — canonical home of **dark resonance** ($g$-2, clm-v2sg8z).
- [Op14 Cross-Sector Trading](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md) — the shared Op14 mechanism (A-012).
- [`2026-05-31_FT-darkwake-crossscale_prereg.md`](../../../research/2026-05-31_FT-darkwake-crossscale_prereg.md) — the Outcome-C cross-scale test that forced the genus/species split.
