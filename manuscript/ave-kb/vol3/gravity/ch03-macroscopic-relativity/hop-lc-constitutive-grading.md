[↑ Ch.3 Macroscopic Relativity](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "WALK-GRADE ontology + constitutive-inventory leaf (Grant-signed 2026-08-28). Records (i) ε11 as DC Q-point of the A1 tank on a frozen graph, (ii) SYM pinning of hop L/C, (iii) the three non-interchangeable senses of 'linear' for L,C vs strain. Mints no clm-/def- here (the linear-homonym lives as def-ln3str in the vocabulary register). Every quantitative statement is a POINTER to an existing claim or a named open fork. Does not plant (2,1,1/2) or slide vertices."
path-stable: "referenced from vol3 ch3 as the hop-LC constitutive companion of achromatic-impedance-matching; vocabulary home def-ln3str"
-->

# Hop \(L\), \(C\) constitutive grading — Q-point, SYM, and which "linear"

**Status: WALK-GRADE.** Grant signed the lattice picture 2026-08-28 (session; PR #1033). This leaf is the KB home of that picture and of the regime answer to *"under what strain do \(L\) and \(C\) scale linearly?"* It originates **no** new claim-id. Forks F1–F3 of the frozen prereg stay Grant-routed.

> **Vocabulary.** Reuse [`def-q1escn`](../../../common/vocabulary-register.md) (Q-point). Do not coin "Q-point gravity." The three senses of "linear" for hop \(L,C\) are the disambiguation node [`def-ln3str`](../../../common/vocabulary-register.md).

---

## §1 — Signed ontology (Grant, 2026-08-28)

1. **The lattice is the space.** A node is a graph vertex (six Cosserat DOFs + operating point \(A\)). There is no embedding \(\mathbb{R}^3\) the bricks fly through.
2. **Observed matter and light are AC** on that net. All measurement is AC ([`clm-acdc07`](../../../common/form-deriving-value-importing.md)).
3. **\(\varepsilon_{11}\) is the DC Q-point** of the A1 tank at that vertex — allowed AC swing — **not** a slide of the vertex. Canon already names this noun at two scopes ([`def-q1escn`](../../../common/vocabulary-register.md); source-law clause Q).
4. **Uniform \(A\) is gauge-relative.** Only \(\nabla A\) / \(\nabla\varepsilon_{11}\) is readable ([`CLAUDE.md`](../../../CLAUDE.md):75 INVARIANT-S2 operating-point clause).
5. **Vertices stay put on this lane.** Bound response \(\mathbf{u}_0 = -\mathcal{A}_g\nabla\varepsilon_{11}\) is a second layer, **unvalued** (R48). Geometric \(\theta=\nabla\cdot\mathbf{u}\) is not consumed here.
6. **The relative frame down-regulates** via the local cell \((\Omega,\,c_{\mathrm{eff}},\,Z)\) without vertices leaving the graph.

Microrotation \(\to\) inductive flywheel; translation / bond-stretch \(\to\) capacitance; the **bond** is a distributed TL (\(L'\) and \(C'\)) ([`translation-circuit.md`](../../../common/translation-tables/translation-circuit.md):98–104). Session "micropolar inductance" maps onto the **Cosserat shunt stiffness** \(S\) in \(\Omega^2=S/C\), not onto the TL series \(L\). That naming is Fork F1 of the prereg, not a silent rewrite.

---

## §2 — SYM pins the ratio, not the product

A hop has two combinations:

\[
Z=\sqrt{\frac{L}{C}},\qquad c=\frac{1}{\sqrt{LC}}.
\]

Gravity-class loading is **SYM**: \(\mu\) and \(\varepsilon\) take the **same** factor so \(Z'=Z_0\) and \(\Gamma_{\mathrm{EM}}=0\) ([`achromatic-impedance-matching.md`](achromatic-impedance-matching.md):20–28; [`clm-07kd5v`](../../claim-quality.md); Axiom 3). Independent TL \(L\) vs \(C\) (different scale factors) would move \(Z\) and make the well a reflector. That is the **ASYM** channel (static-\(E\), Meissner-asymmetric), not gravity.

So hop \(L\) and \(C\) **may both grade**; they **may not grade apart**. The leftover candidate knob is the gap \(\Omega^2=S/C\), which no impedance theorem constrains.

---

## §3 — Under what strain do \(L\) and \(C\) scale linearly?

**They do not, from Axiom 4.** The kernel is even. "Linear" here is a homonym ([`def-ln3str`](../../../common/vocabulary-register.md)). Three senses:

### Sense K — kernel (Ax4): no linear term; Regime I \(\approx\) constant

\[
S(r)=\sqrt{1-r^2}=1-\frac{r^2}{2}-\frac{r^4}{8}-\cdots
\]

([`four-regimes.md`](../../../vol1/operators-and-regimes/ch7-regime-map/four-regimes.md):110–114.) First correction is \(O(r^2)\). The A1 varactor is the same even expansion: \(C_{\mathrm{eff}}=C_0/S=C_0\bigl(1+\tfrac12(V/V_{\mathrm{snap}})^2+\cdots\bigr)\) ([`nonlinear-vacuum-capacitance.md`](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md):33–34).

**Regime I** is \(r<\sqrt{2\alpha}\approx0.1208\), where \(\Delta S=r^2/2\) is sub-\(\alpha\) and is dropped ([`four-regimes.md`](../../../vol1/operators-and-regimes/ch7-regime-map/four-regimes.md):26, :35–41). The SYM constitutive table then reads \(\varepsilon_{\mathrm{eff}}=\varepsilon_0\), \(\mu_{\mathrm{eff}}=\mu_0\), \(C_{\mathrm{eff}}=C_0\) ([`regime-equation-sets.md`](../../../vol1/operators-and-regimes/ch7-regime-map/regime-equation-sets.md):19–25). Solar-surface gravitational strain is \(\varepsilon_{11}=1.486\times10^{-5}\) — **deep Regime I** ([`domain-catalog.md`](../../../vol1/operators-and-regimes/ch7-regime-map/domain-catalog.md):50). Mercury is \(\sim10^{-7}\). Kernel-sourced \(\delta L/L\) and \(\delta C/C\) at the limb are \(O(10^{-10})\), not \(O(\varepsilon_{11})\).

Solar-system gravity is therefore **kernel-linear in the Regime I sense**: the kernel is frozen, hop \(L\) and \(C\) from Ax4 are **constant to working precision**. That is not "\(L,C\propto\varepsilon_{11}\)."

### Sense P — photoelastic / Op19: linear in \(\varepsilon_{11}\), still Regime I, different object

Op19 is \(n=1+\nu_{\mathrm{vac}}\cdot\varepsilon_{11}\) ([`operators.md`](../../../common/operators.md):59). Under SYM, \(\mu'=n\mu_0\), \(\varepsilon'=n\varepsilon_0\), so hop \(L\) and \(C\) **co-scale with \(n\)** and the leading correction is **linear in \(\varepsilon_{11}\)**. At the limb, \((2/7)\varepsilon_{11}=4.25\times10^{-6}\) — the \(O(m)\) gravitational index.

This is **not** the kernel's Taylor series. Photoelasticity is linear in strain; the kernel's index shift is quadratic in amplitude ([`research/2026-07-31_anisotropy-observable_scoping.md`](../../../../../research/2026-07-31_anisotropy-observable_scoping.md):893). The gravity-linearity audit: GR-exact observables are licensed by a **linear projection** of strain; **the Ax4 kernel appears nowhere in that chain** ([`research/2026-08-11_gravity-linearity-audit_result.md`](../../../../../research/2026-08-11_gravity-linearity-audit_result.md):24). \(\nu_{\mathrm{vac}}=2/7\) is **GR-imported** (#261). The rank-4 map \(p_{ijkl}\) that would convert strain to index in a real medium is **unnamed** (F-B4).

**Regime of Sense P:** the same weak-field / cold / sub-yield band as Sense K (solar-system \(\varepsilon_{11}\ll\sqrt{2\alpha}\)). The coupling is linear **because it is Op19**, not because Regime I linearized the kernel.

### Sense Z — SYM co-scale: \(L\propto C\) at every gravity-class strain

Until the loading class leaves SYM, hop \(L\) and \(C\) remain **proportional** (ratio \(=Z_0^2\)) from Regime I through yield. That is "linear in each other," not linear in strain. Near \(A\to1\), both still co-scale; \(c_{\mathrm{eff}}\) and \(\Omega\) grade strongly via \(S(A)\). Independent TL \(L\) vs \(C\) stays forbidden.

---

## §4 — What this leaf does not do

- Does not derive \((a_1,b_1,b_2)=(2,1,\tfrac12)\).
- Does not value \(\mathcal{A}_g\) or slide nodes.
- Does not treat the Gordon optical metric as the spatial PPN answer. The imported strain field is [`gordon-optical-metric.md`](gordon-optical-metric.md):33. The metric-read \(\gamma=0\) diagnosis lives on unmerged #1028; this leaf does not restack it.
- Does not identify A1 \(C_{\mathrm{eff}}=C_0/S\) with T2 \(\varepsilon_{\mathrm{eff}}=\varepsilon_0 S\) (INVARIANT-S2 sector split).

**Canonical homes for the pieces:** Q-point [`def-q1escn`](../../../common/vocabulary-register.md); achromatic match [`achromatic-impedance-matching.md`](achromatic-impedance-matching.md); regime ladder [`four-regimes.md`](../../../vol1/operators-and-regimes/ch7-regime-map/four-regimes.md); Op19 [`operators.md`](../../../common/operators.md):59; frozen prereg [`research/2026-08-28_qpoint-lc-constitutive_prereg-FROZEN.md`](../../../../../research/2026-08-28_qpoint-lc-constitutive_prereg-FROZEN.md).
