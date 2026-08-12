[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
subtree-experiments: []
-->

# Ch.9 Mechanical Characteristics

Chapter 9 of the Vol 9 datasheet documents the natural vacuum substrate as a Cosserat micropolar continuum (Axiom 1: 6 DOF per K4 node = 3 translational $\to$ $\mathbf{E}$ + 3 microrotational $\to$ $\mathbf{B}$; intrinsic spin originates from the Cosserat microrotational DOF). Spec entries: shear modulus $G_{vac}$, bulk modulus $K_{vac} = 2 G_{vac}$, vacuum Poisson ratio $\nu_{vac} = 2/7$ (Axiom 1 LC + Axiom 2 $\alpha$ interlink), Cosserat couple-stress modulus $\gamma_c$, bulk mass density $\rho_{bulk} = \xi_{topo}^2 \mu_0 / (P_C \ell_{node}^2)$, transverse mechanical wave speed $v_T = c_0$ at the cold-lattice limit (modulated to $v_T(A_0) = c_{shear}(A_0) = c_0\sqrt{S(A_0)}$ under saturation), two distinct longitudinal speeds (KEEP-BOTH, 2026-06-08 $c_L$ reconciliation, Rule 12) — the **bulk-modulus dilatational / A1-scalar port-mode** $v_{bulk} = \sqrt{2}\, c_0 = \sqrt{K/\rho}$ (drops the $4G/3$ shear term) **distinct from** the **solid longitudinal P-wave** $c_L = \sqrt{(K + 4G/3)/\rho} = \sqrt{10/3}\, c_0 \approx 1.83\, c_0$ at $\nu_{vac} = 2/7$ — and Cosserat characteristic length $l_c = \sqrt{\gamma_c / G_{vac}}$ identified with the weak-force range $r_W$. 🔴 **[DEMOTED 2026-08-11 — R40-B1; dated demotion note at the end of this file]** 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**

## Node-model channel tags (session add — bulk = MASS-"3"/A1, shear = CHARGE-"3"/Cosserat)

Per the corrected graded-vacuum-impedance-network device model ([`device-circuit-models.md`](../ch3-pin-port-configuration/device-circuit-models.md):143-149, on main), the mechanical primitives map onto the two CONFINED channels of the 2-domain N-port: the **bulk channel** carries the **MASS-"3"** (A1 dilatation, $Z_{bulk} = \rho_{bulk}\, c_{bulk} = \sqrt{2}\,\rho_{bulk}\, c_0$ at $K = 2G$, $\Gamma_{bulk} \to -1$ CONFINED — a *mechanical/acoustic* impedance $\rho \times$ speed, NOT in $Z_0$ units), and the **shear channel** carries the **CHARGE-"3"** (Cosserat micro-rotation winding, $Z_{shear} = \rho_{bulk}\, c_{shear}$, $\Gamma_{shear} \to -1$ CONFINED). The EM channel ($Z_{EM} \equiv Z_0 = \sqrt{\mu_0/\varepsilon_0} \approx 376.73\,\Omega$, $\Gamma_{EM} = 0$) is the sole external MATCHED radiative PORT — not a mechanical primitive (it lives in $\Omega$, an electrical-impedance DOMAIN distinct from the $\rho c$ mechanical impedances). $A1 \perp T2$: the mass (A1 dilatation) and charge/spin (Cosserat $(2,3)$ micro-rotation) grades are orthogonal, never wired into one shared phasor (the two-"3"s fence, [`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20). 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**

The chapter content is **Class B/C synthesis** per `consistency-vs-emergence` v1.3 --- no new substrate-physics primitives are introduced; the content consolidates canonical mechanical-sector derivations (CLAUDE.md INVARIANT-S2 Axiom 1; $\nu_{vac} = 2/7$ at `vol3/gravity/ch01-gravity-yield/vacuum-poisson-ratio.md`; $K_{vac} = 2 G_{vac}$ at the EMT $p^* = 8\pi\alpha$ packing fraction; weak-force range $l_c$ at `vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md` line 39; $c_{EM}$-vs-$c_{shear}$ semantic distinction at `clm-8nkvwy`) into datasheet Mechanical-Characteristics format, with the EE-substrate-native projection per `common/translation-tables/translation-circuit.md` $\S4$ added as the EE mechanical translation table.

## Primary canonical sources

| Source | Content |
|---|---|
| CLAUDE.md INVARIANT-S2 (Axiom 1) | Cosserat micropolar 6 DOF per node; intrinsic spin from microrotational DOF; $c_{EM}$ vs $c_{shear}$ distinction; SYM-class $\alpha$ invariance |
| Vol 1 Ch 1 (`vol_1_foundations/chapters/01_fundamental_axioms.tex`) | Canonical chapter-form derivation of Axiom 1 |
| Vol 1 Ch 4 §`sec:cosserat_primer` | Cosserat primer (manuscript) |
| [`vol3/gravity/ch01-gravity-yield/vacuum-poisson-ratio.md`](../../vol3/gravity/ch01-gravity-yield/vacuum-poisson-ratio.md) (`clm-x19btt`) | $\nu_{vac} = 2/7$ derivation from $K_{vac} = 2 G_{vac}$ + standard isotropic identity |
| [`vol3/gravity/ch01-gravity-yield/topological-packing-fraction.md`](../../vol3/gravity/ch01-gravity-yield/topological-packing-fraction.md) | EMT $p^* = 8\pi\alpha$ packing fraction (input to $K/G = 2$) |
| [`vol3/gravity/ch01-gravity-yield/one-seventh-impedance-projection.md`](../../vol3/gravity/ch01-gravity-yield/one-seventh-impedance-projection.md) | 1D $\to$ 3D volumetric bulk projection = 1/7 |
| [`vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md`](../../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md) (`clm-5zuo7g`, `clm-q8un7j`) | $l_c = \sqrt{\gamma_c / G_{vac}}$ weak-force range; $W/Z$ evanescent cutoff masses; $m_W/m_Z = \sqrt{7}/3$ |
| [`common/appendix-derived-numerology.md`](../../common/appendix-derived-numerology.md) (`clm-zi6t1e`) | Derived hardware numerology incl. $\nu_{vac} = 2/7$, $K = 2G$ at $p^* = 8\pi\alpha$, $n_{3D} = 38/21$ |
| [`common/translation-tables/translation-circuit.md`](../../common/translation-tables/translation-circuit.md) (`clm-eemap1`) | EE-substrate-native META framework + comprehensive substrate-primitive-to-EE-component mapping table |
| [`common/trampoline-framework.md`](../../common/trampoline-framework.md) line 192 | Cosserat rotation-sector mass-gap $m_\omega \sim 1$ MeV (consequence for Ch.10) |
| [`vol9/ch3-pin-port-configuration/device-circuit-models.md`](../ch3-pin-port-configuration/device-circuit-models.md):143-149 | Node-model channel tags: bulk = MASS-"3"/A1 dilatation ($Z_{bulk}$), shear = CHARGE-"3"/Cosserat micro-rotation ($Z_{shear}$), EM = matched radiative PORT ($Z_0$, $\Gamma_{EM} = 0$); $A1 \perp T2$ orthogonality fence |
| `src/ave/core/constants.py` | symbols `NU_VAC`, `RHO_BULK`, `G_VAC`, `V_LONG`, `XI_TOPO`, `P_C`, `L_NODE` (symbol-name cites; line numbers unstable across renumbers) |

## Manuscript counterpart

`manuscript/vol_9_vacuum_datasheet/chapters/09_mechanical_characteristics.tex` (canonical Vol 9 chapter file; populated in this PR)

## Cross-chapter dependencies within Vol 9

- **Ch 1 (General Description and Features)** establishes the substrate identity + 6-DOF Cosserat micropolar framing; Ch 9 spec'es the resulting bulk mechanical primitives.
- **Ch 6 (Temperature Characteristics)** documents the Cosserat-Curie thermal-asymmetry $\delta_{strain}$ at $T_{CMB}$ as a consequence of the rotation-sector mass-gap thermally freezing $\mu$ while $\varepsilon$ remains thermally populated --- the same Cosserat couple-stress $\gamma_c$ that sets the weak-force range in this chapter.
- **Ch 7 (Saturation Characteristics)** sets the Axiom 4 kernel $S(A_0) = \sqrt{1 - (A_0/A_{yield})^2}$ that modulates $v_T(A_0) = c_{shear}(A_0) = c_0\sqrt{S(A_0)}$ at finite operating point.
- **Ch 10 (Magnetic / Microrotational Characteristics)** develops the magnetic-sector consequences of the Cosserat couple-stress $\gamma_c$ spec'd here: flywheel inductance, rotation-sector mass-gap, weak-force range as a magnetic-sector spec entry.

## Cross-volume canonical-derivation pointers

- Vol 3 Ch.~`ch:gravity_and_yield` (manuscript) --- canonical derivation of $\nu_{vac} = 2/7$ + the gravitational-time-dilation $c_{shear} = c_0\sqrt{S}$ Schwarzschild reduction in the SYM-class gravity-class limit.
- Vol 2 Ch.~`ch:electroweak` (manuscript) --- canonical $l_c$ + Yukawa-cutoff derivation; $W/Z$ mass ratio from $\nu_{vac}$.
- Vol 1 Ch.~`ch:regime_map` --- four-regime kernel context for $S(A_0)$ saturation modulation.

---

---

### 🔴 Dated demotion note — 2026-08-11 (R40 demotion sweep, batch 1)

**Class: DIES-WITH-THE-PHANTOM.** Status change only — the claim text is **preserved
verbatim** (honesty-lag pattern, Rule 12) and stamped in place; it is **no longer live
canon**. Nothing is deleted.

**Demoted in this file:**

- **`:11`** — *"the solid longitudinal P-wave c_L = √((K + 4G/3)/ρ) = √(10/3) c_0 ≈ 1.83 c_0 at ν_vac = 2/7"*
  Stamped in place at `:11`.
  **⚑ MIXED-BIN LINE — read the stamp as scoped, not blanket (disclosure added 2026-08-11 at review).**
  `:11` is one long scope paragraph carrying MORE than the demoted claim, and the banked worklist
  hosts a **second, co-resident row on this same line** binned **NEEDS-RE-DERIVATION**, not DIES:
  quote *"the bulk-modulus dilatational / A1-scalar port-mode v_bulk = √2 c_0 = √(K/ρ) (drops the
  4G/3 shear term)"*, rationale *"The √2c PORT object survives as the near-field/A1 port reading
  (prereg §6), but v_bulk=√(K/ρ) as a SPEED formula consumes the K-reservoir-to-wave-speed mechanism
  — formula-level re-derivation owed."* **That row is BATCH 2 and is not demoted here.** The
  line-terminal stamp demotes exactly the quoted `c_L = √(10/3) c_0` P-wave member above and nothing
  else; `K_vac = 2G_vac`, `ν_vac = 2/7`, `v_T = c_0` and `ℓ_c = r_W` on the same line are **not**
  ruled on by R40 and are untouched.
  **Why it dies (audited row rationale, verbatim):** The KEEP-BOTH row's P-wave member is a bulk propagation speed as a physical transit speed — the prereg's expected DIES class for √(10/3) rows.

**The arc, complete — the framing R40 rules every demotion note carries:**

1. **The kill fired** (#930) — the walk-back that closed the bulk radiative-port reading.
2. **The premise localized to the #261 K = 2G import** (G-RECON, unchallenged): the compressible
   far-field branch was minted by a GR-imported elastic modulus, not forced by the axioms.
3. **The axioms underdetermine the bulk sector** — the #935 flat-direction finding: the written
   action conserves the Gauss function pointwise and never fixes its value.
4. **The replacement is the RATIFIED bound-sector law — Axiom 5, Substrate DC Bias**
   (BC-SRC clauses **S** / **G** / **Q**), ratified per `_orchestration/docket-entries/2026-08-10-ruling-r43-ratification.md`, as reconciled by `_orchestration/docket-entries/2026-08-10-ruling-r44-r43-reconciliation.md` (R44 — the
   full-scope R43 record is FINAL and authoritative; the partial
   `_orchestration/docket-entries/2026-08-10-ruling-r43-sg-ratified.md` is SUPERSEDED and is **not**
   the resolution). Under the ratified law the A1 / bulk slot is a **bound response** — mechanism
   gloss **back-reaction** — with no independent propagating branch, no port, and zero longitudinal
   characteristic speed. A bulk *wave speed*, a bulk *radiative port*, a bulk *band-branch* and a
   bulk *transit clock* therefore have **no referent**.

**Standing named-open debt (the honest rider).** The ratified axiom does **not** discharge
everything: **THE BIAS PROPAGATION THEOREM** is Axiom 5's standing named-open entry — clause G's
elliptic law is the *static abstraction* of underived finite-speed bias dynamics (`_orchestration/2026-08-10_bias-propagation-brief.md`). Where a
demoted claim's replacement depends on finite-speed bias dynamics, the resolution is the ratified
axiom **with that debt open**, not a closed replacement.

**Records.** R40 ruling `_orchestration/docket-entries/2026-08-10-rulings-r40-r42.md` · verified worklist `research/drivers/r40_sweep_worklist_verified.json` · scope verification `_orchestration/2026-08-10_r40-sweep-scope-verification.md` ·
batch-1 record `_orchestration/2026-08-11_r40-sweep-batch1.md` · vocabulary R50 `_orchestration/docket-entries/2026-08-10-ruling-r50-vocab.md` (canonical: the displacement pattern u₀ around a
deposit is **the bound response**, mechanism gloss **back-reaction**; ε₁₁ is **the bias**;
"dress", "grade"-as-canonical-noun and "halo"-for-the-physics are retired; and the owed theorem is
renamed **THE BIAS PROPAGATION THEOREM**) · vocabulary **R49(b)** `_orchestration/docket-entries/2026-08-10-rulings-r48-r49.md` (*"retardation"
is RETIRED from this role. The canonical term is **propagation delay / finite propagation speed*** —
the retardation retirement is R49(b)'s, NOT R50's; corrected 2026-08-11 at review).

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

- **`:11`** — stamped at `:11`. *(family: √2c port-mode speed form)*  ⚑ **BIAS-DEBT**
  Quoted claim, byte-exact at HEAD:
  ```text
  the bulk-modulus dilatational / A1-scalar port-mode v_bulk = √2 c_0 = √(K/ρ) (drops the 4G/3 shear term)
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  The √2c PORT object survives as the near-field/A1 port reading (prereg §6), but v_bulk=√(K/ρ) as a SPEED formula consumes the K-reservoir-to-wave-speed mechanism — formula-level re-derivation owed.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

- **`:15`** — stamped at `:15`. *(family: Z_bulk=ρc_bulk formula)*  ⚑ **BIAS-DEBT**
  Quoted claim, byte-exact at HEAD:
  ```text
  the bulk channel carries the MASS-"3" (A1 dilatation, Z_bulk = ρ_bulk c_bulk = √2 ρ_bulk c_0 at K = 2G, Γ_bulk → -1 CONFINED
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  Both-hosting: MASS-"3" accounting + Γ confined reading survive; ρc_bulk formula consumes the phantom (note: same line's 'EM = sole external MATCHED radiative PORT' corroborates the carve).
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

**Records.** Ruling **R40** (the demotion sweep) · the banked worklist
[`r40_sweep_worklist_verified.json`](../../../../research/drivers/r40_sweep_worklist_verified.json) · batch-0
scope verification and batch-1 execution records in `_orchestration/` · this batch's record
`_orchestration/2026-08-12_r40-sweep-batch2a.md`.

