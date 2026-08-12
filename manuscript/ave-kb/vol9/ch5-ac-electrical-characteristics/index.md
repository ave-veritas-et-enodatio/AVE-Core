[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
subtree-experiments: []
-->

# Ch.5 AC Electrical Characteristics

Chapter 5 of the Vol 9 datasheet documents the substrate's frequency-domain behaviour: bond LC resonance at $\omega_C = c_0/\ell_{node} \approx 7.76 \times 10^{20}$ rad/s ($f_C \approx 1.23 \times 10^{20}$ Hz, substrate Nyquist ceiling), bond TLM characteristic impedance $Z_0 \approx 376.73\,\Omega$, operating-point $A_0$ small-signal modulation of $\varepsilon_{eff}$ / $\mu_{eff}$ / $C_{eff}$ / $Z_{eff}$, dispersion at the K4 lattice Brillouin scale $k_{Brillouin} = \pi/\ell_{node}$, and the load-bearing distinction between the two substrate-native effective wave speeds $c_{EM}(A_0) = c_0/S(A_0)$ (Maxwell phase velocity, enters $\alpha$) and $c_{shear}(A_0) = c_0\sqrt{S(A_0)}$ (mechanical / group / rest-mass velocity, Schwarzschild reduction).

The chapter content is **Class B / Class C synthesis** per `consistency-vs-emergence` v1.3: $\omega_C = c_0/\ell_{node}$ is definitional from the canonical per-cell primitives $L_{cell} = \mu_0 \ell_{node}$, $C_{cell} = \varepsilon_0 \ell_{node}$ at `src/ave/core/constants.py` (`MU_0`, `EPSILON_0`, `L_NODE`, `C_0`) (Class C consistency); the operating-point small-signal table consolidates the canonical CLAUDE.md INVARIANT-S2 entry into datasheet AC format (Class B substrate-mechanism manifestation). No new substrate-physics primitives are introduced.

The $c_{EM}$ vs $c_{shear}$ disambiguation is preserved verbatim from CLAUDE.md INVARIANT-S2 — never substitute $c_{shear}$ into the $\alpha$ formula (canonical Pitfall #5 framework-leakage caught in the 2026-05-28 Phase 3-A3 WALK-BACK; canonical anchors `clm-3zz0f6` and `clm-8nkvwy`).

**Temporal / switching section (new, this chapter §Temporal Characteristics).** The clock quantum $\tau_0 = \ell_{node}/c_0 \approx 1.288 \times 10^{-21}$ s (the electron Compton time = voxel tick, `tau-relax-derivation.md`:11); the **three sector speeds** ($c_{EM} = c_0(1-A^2)^{-1/2}$ rises; $c_{shear} = c_0(1-A^2)^{+1/4}$ freezes — the matter clock; $c_{bulk} = c_0\sqrt{1+\bar{\rho}/(1-\bar{\rho}^2)}$ freezes at $\bar{\rho}_{cav} = -1/\varphi$); the **three sector clocks** (matter clock = shear, dilates as $(1-A^2)^{-1/4}$ → fixes the time-dilation exponent $p = \tfrac14$ with the physical why: matter is a packet riding $c_{shear}$); the **2×2 sat/desat** table over the shear/bulk K=2G pair (plus EM phase), with $\tau_{cycle} \propto 1/\sqrt{S}$ (`two-engine-architecture-a027.md`:28). Source: `research/2026-06-09_substrate-temporal-values-definition.md` (branch `analysis/2026-06-09-saturation-temporal-preregs`, dependency not yet on `main`). **OPEN:** bulk $\tau_{bulk,sat} \neq \tau_{bulk,desat}$ (thixotropy prereg, same branch; shear-sector asymmetry derived NEGATIVE). **STALE leaves cited only with flag:** `op14-local-clock-modulation.md`:17,31 (exponent ½, pre-split single-speed model — off by ×2) and `04_superluminal_transit.tex`:41 (clock mislabeled $c_{EM}$ — Pitfall #5). Both flagged for PR-gated walk-back at their home leaves.

## Primary canonical sources

| Source | Content |
|---|---|
| CLAUDE.md INVARIANT-S2 (small-signal block) | Operating-point modulation table; $c_{EM}$ vs $c_{shear}$ disambiguation; Pitfall #5 WARNING |
| `common/translation-tables/translation-circuit.md` §1 (`clm-fy05jc`) | Topo-kinematic identity; per-bond LC primitives $L_{cell} = \mu_0 \ell_{node}$, $C_{cell} = \varepsilon_0 \ell_{node}$ |
| `common/translation-tables/translation-circuit.md` §2 (`clm-eemap1`) | EE-as-substrate-native META framework; bond TLM as substrate-native |
| `common/operators.md` Op14 | Dynamic impedance $Z_{eff} = Z_0/\sqrt{S}$ (ASYM-class small-signal modulation) |
| `vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md` (`clm-1eg13f`) | Op14 local clock modulation; cross-volume parallel to gravitational time dilation |
| `common/operators.md` Op16 | Universal wave speed $c_{shear} = c_0 \sqrt{S}$ (mechanical / group velocity; Op16 canonical) |
| `vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md` (`clm-3zz0f6`) | SYM scaling: $\alpha$ EXACTLY invariant under joint $\mu, \varepsilon$ scaling; canonical Pitfall #5 anchor |
| `clm-8nkvwy` (lines 111 / 113) | $c_{EM} = c_0/S$ (Maxwell phase, line 111) vs $c_{shear} = c_0\sqrt{S}$ (mechanical / group, line 113) canonical disambiguation |
| `src/ave/core/constants.py` (via `ave-canonical-source` skill; symbols `MU_0`, `EPSILON_0`, `Z_0`, `C_0`, `L_NODE`) | $\mu_0$, $\varepsilon_0$, $Z_0$, $c_0$, $\ell_{node}$ canonical primitives |
| `vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md` | Substrate $Q$-factor at $\Gamma = -1$ saturation boundary; multi-mode mode-counting |
| `vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md` | Substrate $Q$-factor cold-lattice form |

## PONDER-05 reference

PONDER-05 (DC-biased quartz, 27.4% $\varepsilon_{eff}$ collapse at ~30 kV) is a **material-scale consistency analog of the operating-point $A_0$ kernel SHAPE** (the quartz / Class-II-ceramic voltage-coefficient-of-capacitance), **NOT a vacuum-kernel falsifier**. ⚠ Per-node-conflation correction (2026-06-04): $A_0 = V_{DC}/V_{yield}$ is a **per-node** ratio (field across ONE cell $\ell_{node} = 0.386$ pm relative to $E_{yield} = V_{YIELD}/\ell_{node} \approx 1.13\times10^{17}$ V/m); reaching $A_0 = 0.687$ needs 30 kV across 1.0 node-lengths. Across real quartz (mm–µm) the vacuum per-node $A_0 = 10^{-7}$–$10^{-10}$ → vacuum collapse ~0; the 27.4% is the quartz material's own response. The quartz LC-resonance shift vs zero-bias is the bench observable of the **material's** $C(V)$ arc (consistency-class), not the vacuum kernel; a genuine vacuum reading needs facility fields ($\sim 8\times10^{16}$ V/m). Per `vol4/claim-quality.md:51` + Q-G42 $V_{yield}^{(apparatus)} = E_{yield}^{(substrate)}/G_{geom}$. Canonical pointer at CLAUDE.md INVARIANT-S2 small-signal block (corrected). Hardened build artifacts live in the `ave-veritas-et-enodatio` private repository per `vol4/index.md` repo-scope note; the AC-characteristic spec that PONDER-05 tests is documented in this chapter. Cross-reference: Vol 9 Ch.15 falsification programme.

## Engine-acceptance suite coverage (L1 free modes + L2 EM-in-media, GREEN 2026-06-16/17)

The AC / propagation primitives this chapter specifies are gated GREEN by the
ground-up engine-acceptance suite (`src/tests/engine_acceptance/`, wired in
[`../ch17-engine-requirements/engine-acceptance-suite.md`](../ch17-engine-requirements/engine-acceptance-suite.md)):

- **L1 free modes** — T1.1 lossless transverse-EM propagation (`sup-su0h1a` →
  `clm-3npynp`, `clm-djpx2v`), T1.2 dispersionless band ω=ck (`sup-iryl5d`), T1.3
  transversality (`sup-xn9y6c`), T1.4 causality/front-speed (`sup-xey8a8`), T1.5
  lossless chiral optical activity (`sup-w6tjvs` → `def-7c3f9e`, `def-0pt1ac`), T1.6
  transverse-shear mode (`sup-oicgzy`). T1.7/T1.8 are STOP-and-report medium-extension
  FINDINGS (longitudinal-bulk + Cosserat micro-rotation modes NOT carried — the L3/L4 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**
  gaps; tracked by test-id, not wired).
- **L2 EM-in-media** — T2.1 refractive index c_EM=c₀/S (`sup-1sq5c1`), T2.4
  α-invariance under SYM (`sup-ftxwil` → `clm-3zz0f6`). (T2.2 achromatic lensing →
  Ch.12; T2.3 asymmetric mirror → Ch.3/Ch.7.)
- **c_EM/c_shear/c_bulk DEF-LOCK** carried in the suite docstrings; the suite ⚑FLAGS 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**
  the brief √S vs corpus S^(1/4) c_shear discrepancy (dormant at S=1; adjudicate before
  any saturated-shear test).

## Manuscript counterpart

`manuscript/vol_9_vacuum_datasheet/chapters/05_ac_electrical_characteristics.tex` (canonical Vol 9 chapter file).

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

- **`:50`** — stamped at `:50`. *(family: L3 gap finding)*
  Quoted claim, byte-exact at HEAD:
  ```text
  FINDINGS (longitudinal-bulk + Cosserat micro-rotation modes NOT carried — the L3/L4 gaps; tracked by test-id, not wired)
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  The absence-finding is correct behavior under the carve, not a medium-extension GAP — the gap label consumes the phantom (presumes the physical spectrum has the mode); re-label owed.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave.

- **`:55`** — stamped at `:55`. *(family: c_bulk def-lock ledger)*  ⚑ **BIAS-DEBT**
  Quoted claim, byte-exact at HEAD:
  ```text
  c_EM/c_shear/c_bulk DEF-LOCK carried in the suite docstrings
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  Def-locks c_bulk as a propagation-speed constant in the acceptance suite's frozen definitions — register/ledger row recording the imported reading (prereg-named class).
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

**Records.** Ruling **R40** (the demotion sweep) · the banked worklist
[`r40_sweep_worklist_verified.json`](../../../../research/drivers/r40_sweep_worklist_verified.json) · batch-0
scope verification and batch-1 execution records in `_orchestration/` · this batch's record
`_orchestration/2026-08-12_r40-sweep-batch2a.md`.

