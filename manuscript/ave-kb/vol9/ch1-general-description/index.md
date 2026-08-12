[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
subtree-experiments: []
-->

# Ch.1 General Description and Features

Chapter 1 of the Vol 9 datasheet establishes the substrate identity (the substrate — natural 3D chiral Laves K4 Cosserat crystal), enumerates the load-bearing structural features (intrinsic LC oscillators at each node; bond transmission lines; Cosserat micropolar 6 DOF/node = 3E + 3B; Axiom 4 saturation kernel; $\Gamma$ boundary semantics; saturable yield + breakdown thresholds; $\xi_{topo}$ topological transduction), defines the spec-table column convention used in subsequent chapters, and establishes the epistemic position: the substrate is natural, engineering observation characterizes its limits, AVE substrate-physics derives the mechanism.

The chapter content is **Class B/C synthesis** per `consistency-vs-emergence` v1.3 — no new substrate-physics primitives are introduced; the content consolidates the canonical axiom statements (CLAUDE.md INVARIANT-S2) and the EE-as-substrate-native META framework (canonical leaf `common/translation-tables/translation-circuit.md` §2, `clm-eemap1`) into datasheet General-Description-and-Features format.

## The vacuum as a component (opening narrative)

The General Description opens with the component-identity statement (consistency-class; every clause traces to merged canon):

- **A chiral crystal of LC resonators.** The medium is the `srs` net ($z=3$, $I4_132$; ratified production carrier per D1, Grant 2026-07-03, [`_orchestration/index.md`](../../../../_orchestration/index.md)); every node is a lossless LC resonator with 6 DOF (3 translational-capacitive $\to \mathbf E$; 3 microrotational-inductive $\to \mathbf B$; Axiom 1) plus a per-node operating point (the saturation state $A$, a DC bias on the node's own nonlinearity — *not* a 7th spatial DOF). $Z_0=\sqrt{\mu_0/\varepsilon_0}\approx377\,\Omega$ (`constants.py` `Z_0`) is the network characteristic impedance.
- **z=3 vs the 4-port (reconciliation).** The physical connectivity is $z=3$ (three nearest-neighbour bonds). The "K4 4-port" $A_1\oplus T_2$ irrep decomposition (ch3/ch11) is the abstract $T_d$ scattering-amplitude decomposition of the K4-TLM scatter matrix ($\dim 4 = 1+3$), *not* a physical bond count — the documented "K4" three-way overload (axiom-named chiral Laves K4 = degree-3 srs; engine "K4" = degree-4 diamond instrument; rotation group $K_4$). The $z=3$ net and the abstract 4-port are separate referents, not a contradiction (ch3 disambiguation).
- **Transparency (governing law).** Axiom 3 minimizes $|\Gamma|^2$ at every internal boundary ([`axiom-register.md`](../../common/axiom-register.md) `axiom-3`); a matched line ($\Gamma=0$) neither reflects nor stores net bias, so light (pure AC on the ground state) crosses without a trace. The stronger chain *min-reflection $\Rightarrow$ bond-stiffness balance ($k_s=k_a$) $\Rightarrow$ isotropy + distortionless* ("one condition, three protections") is now **derived** on the srs-$z=3$ net: minimizing $\Gamma_{\mathrm{internal}}(\rho_{\mathrm{bond}}{=}k_a/k_s)$ lands knob-free on $\rho_{\mathrm{bond}}{=}1$ to machine precision, where match / isotropy / distortionlessness / Zener-$A{=}1$ co-locate — Axiom 3 IS the parent (`research/2026-07-04_parent-condition-match-forces-balance_result.md`, **[MECHANISM-DERIVED]**). **Grade note:** merged research result; canonical KB-leaf + claim-id propagation is a gated follow-on, so it is stated as a derived verdict, not yet a canonized claim. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**
- **Absolute-maximum ratings.** The Axiom-4 kernel $S(A)=\sqrt{1-A^2}$ has $p=2$ **shape-derived** (the lossless bond-LC L2 energy invariant forces the quarter-arc; `research/2026-07-02_axiom4-forced_result.md`, CONDITIONALLY-FORCED; count stays 4). $V_{yield}=\sqrt\alpha V_{snap}\approx43.65$ kV (T2 wall) and $V_{snap}=m_ec^2/e\approx511$ kV (A1 completion; `def-vyvsn1`) are the max ratings.
- **Matter = standing-wave state.** The electron is a phase-winding knot self-trapped at its yield wall by TIR ($\Gamma=-1$, lossless); mass = the trap's stored energy; spin/moment = its circulation; charge = a topological `Link` integer the lattice forces (winding-quantized, globally neutral), field strength a $\xi_{topo}$ calibration, static Coulomb field **locally unsourced** (four-lock no-go cascade at derivation grade, `clm-nogo4l`, [`the-sourced-charge-no-go-cascade.md`](../../common/the-sourced-charge-no-go-cascade.md)).
- **Honesty ledger.** Structure derived, scales imported ($\alpha$, $m_e$, $G$ — as every framework imports them; [`form-deriving-value-importing.md`](../../common/form-deriving-value-importing.md)). The one pre-registered measurable divergence: the electric response saturates at **tree level** (classical constitutive saturation, not a loop effect) — the vacuum-birefringence falsifier, whose discriminator is the field-**independent coefficient** ratio, NOT an $E^4$-vs-$E^2$ exponent (both are $E^2$-leading; the "$E^4$" framing was retracted as a $\sqrt\varepsilon$ conflation, `clm-pp3qwf`).

The matter-stiffening / state-diagram content is deliberately EXCLUDED (arc still computing — not canon).

## Primary canonical sources

| Source | Content |
|---|---|
| CLAUDE.md INVARIANT-S2 (Axioms 1–4) | Substrate identity; 6 DOF/node decomposition; saturation kernel; minimum-reflection principle |
| Vol 1 Ch 1 (`vol_1_foundations/chapters/01_fundamental_axioms.tex`) | Canonical chapter-form derivation of the four axioms |
| `common/translation-tables/translation-circuit.md` §2 (`clm-eemap1`) | EE-as-substrate-native META framework; minimal-DOF substrate-electrical-network claim |
| `vol4/claim-quality.md` `clm-i9l284` | $\xi_{topo} = e/\ell_{node}$ topological conversion constant |
| `vol4/claim-quality.md` `clm-0vxzfu` | $V_{yield}$ / $V_{snap}$ two-threshold distinction (load-bearing reading hazard) |

## Manuscript counterpart

`manuscript/vol_9_vacuum_datasheet/chapters/01_general_description.tex` (canonical Vol 9 chapter file)

---

---

## R40 batch-2a — NEEDS-RE-DERIVATION status note (2026-08-11)

**Class:** status demotion under **R40**. This note mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`,
**moves no solidity number**, adjudicates no channel and opens no fork. Every byte of each demoted
claim is preserved; the stamped line gains a status marker only (honesty-lag pattern, Rule 12).

**The arc, in four clauses (R40's header form; clause 4 points at the LANDED artifact, not at a
ruling record).**

1. **The kill fired** — the walk-back that closed the bulk radiative-port reading.
2. **The premise localized to the imported `K = 2G` elastic modulus** — the compressible far-field
   branch was minted by a GR-imported modulus, not forced by the axioms.
3. **The axioms underdetermine the bulk sector** — the flat-direction finding: the written action
   conserves the Gauss function pointwise and never fixes its value.
4. **The replacement is the LANDED ratified bound-sector law — Axiom 5, Substrate DC Bias**, clauses
   **S** (deposit), **G** (bias coupling / bridge) and **Q** (quiescence), canonical at
   [`eq_axiom_5.tex`](../../../common_equations/eq_axiom_5.tex) with its register entry in
   [`axiom-register.md`](../../common/axiom-register.md) (§ *Axiom 5 — Substrate DC Bias*). Under
   clause **G** the A1 / bulk slot is a **bound response** — $\mathbf{u}_0 =
   -\mathcal{A}_g\nabla\varepsilon_{11}$, mechanism gloss **back-reaction** — with **no independent
   propagating branch, no port and zero longitudinal characteristic speed**. A bulk *wave speed*, a
   bulk *radiative port*, a bulk *band-branch* and a bulk *transit clock* therefore have **no
   referent**, and each row below owes its re-derivation on that footing.
   $\mathcal{A}_g$ (the **bias-coupling area**) is an `UNVALUED-RATIFIED-CONSTANT` per **R48**
   ([`interlock-register.md`](../../common/interlock-register.md), § *𝒜_g — the bias-coupling
   area*): it is **not valued here or anywhere**, and **the calibration count stays 3**.

**Standing named-open debt — the honesty rider.** The ratified axiom does **not** discharge
everything. **THE BIAS PROPAGATION THEOREM is Axiom 5's standing named-open debt**, stated by the
axiom's own phase-structure paragraph, clause **(c1)**: clause G's elliptic law is the *static
abstraction of underived finite-speed bias dynamics*, and the $(u,\pi)$ no-signalling theorem does
**not** cover the bias read — the bias's finite propagation speed is *owed, not held*. Every row
tagged **⚑ BIAS-DEBT** below re-derives against the ratified axiom **with that debt standing**, never
against a closed replacement.

**Vocabulary.** Canonical nouns authored here: **the bound response** ($\mathbf{u}_0$), **the bias**
($\varepsilon_{11}$), the **DC operating point / quiescent point (Q-point)**; **back-reaction** is
the mechanism gloss. *"dress"*, *"grade"* as $\varepsilon_{11}$'s canonical noun, and *"halo"* for
the physics (the physics noun is the **near-field store / added-mass**) are RETIRED by **R50**;
*"retardation"* is retired by **R49(b)** in favour of **propagation delay / finite propagation
speed**. Corpus text quoted below is byte-exact and is never reworded.

**Rows carried in this file.**

- **`:21`** — stamped at `:21`. *(family: parent-condition acoustic boundary; banked `uncertain`)*  ⚑ **BIAS-DEBT**
  Quoted claim, byte-exact at HEAD:
  ```text
  minimizing Γ_internal(ρ_bond=k_a/k_s) lands knob-free on ρ_bond=1 to machine precision
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  Same parent-condition mechanism as vol4/claim-quality:161 — uncertain whether the internal-boundary reflection object is a propagating axial branch; mechanism check owed at the owning leaf.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

**Records.** Ruling **R40** (the demotion sweep) · the banked worklist
[`r40_sweep_worklist_verified.json`](../../../../research/drivers/r40_sweep_worklist_verified.json) · batch-0
scope verification and batch-1 execution records in `_orchestration/` · this batch's record
`_orchestration/2026-08-12_r40-sweep-batch2a.md`.

