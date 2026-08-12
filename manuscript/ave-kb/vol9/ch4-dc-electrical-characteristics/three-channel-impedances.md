[↑ Ch.4 DC Electrical Characteristics](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Vol-9 Class B/C synthesis leaf — three-channel DC impedance assignments at K/G=2. Renders registry §3.11 for the datasheet; no new substrate primitive."
-->

## Three-Channel DC Impedances (canonical leaf)

Per the **three-impedance law** (Grant-ratified 2026-06-11; field-symbol registry §3.11; vocab-operator-unification audit §4a), $Z_0 \equiv Z_{\mathrm{EM}}$ is the **transverse-EM channel only**. Shear and bulk channels carry separate device-port impedances.

This leaf is the **source of truth** for Vol 9 Ch.4 §Three-channel acoustic impedances. LaTeX table `tab:vol9_dc_three_channel` renders this content.

**Skills applied (2026-06-12 pass):** `verify-before-cite` v1.4 · `consistency-vs-emergence` v1.3 Step 8 (**Class C** definitional table) · `ave-canonical-source` · `ave-dimensional-provenance-check` ($Z_{shear}$, $Z_{bulk}$ are $\rho\times$speed, not $Z_0$).

### Cold-lattice assignments ($K/G = 2$ operating point)

| Channel | Impedance | Typical (cold lattice) | $\Gamma$ at saturation |
|---|---|---|---|
| EM-transverse | $Z_{\mathrm{EM}} \equiv Z_0$ | $\approx 376.73\,\Omega$ | $\Gamma_{\mathrm{EM}}=0$ (SYM gravity) |
| Shear / GW | $Z_{\mathrm{shear}} = \rho_{\mathrm{bulk}}\,c_{\mathrm{shear}}$ | $\rho_{\mathrm{bulk}}\,c_0$ at $S=1$ | $\Gamma_{\mathrm{shear}}\to -1$ |
| Bulk-longitudinal | $Z_{\mathrm{bulk}} = \rho_{\mathrm{bulk}}\,c_{\mathrm{bulk}}$ | $\sqrt{2}\,\rho_{\mathrm{bulk}}\,c_0$ | $\Gamma_{\mathrm{bulk}}\to -1$ 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]** |

At $K_{\mathrm{bulk}} = 2G_{\mathrm{vac}}$: $c_{\mathrm{bulk}} = \sqrt{2}\,c_0$ (bulk dilatational speed, not full P-wave). Verified: `src/tests/test_vacuum_moduli_and_channels.py` (lines 66–70, 108–112).

### Canonical sources

| Anchor | Content |
|---|---|
| `src/ave/core/constants.py` | symbols `Z_0`, `RHO_BULK`, `G_VAC`, `V_LONG` |
| [`z0-derivation.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md) | $Z_{\mathrm{EM}} = Z_0$ derivation |
| [`bulk-impedance-at-saturation-boundary.md`](../../vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md) | $\Gamma_{\mathrm{bulk}}=-1$ at $r_{\mathrm{sat}}$ |
| [`device-circuit-models.md`](../ch3-pin-port-configuration/device-circuit-models.md) | Electron TIR barriers = bulk channel, not EM $\Gamma$ at $Z_0$ |
| Ch.9 mechanical characteristics | $\rho_{\mathrm{bulk}}$, $G_{\mathrm{vac}}$, $\nu_{\mathrm{vac}}=2/7$ |

### Discipline note

Electron confinement uses **bulk-channel** ports (Fig. `fig:vol9_circuit_electron_barrier`). Equating particle TIR with EM short circuit at $Z_0$ is a **mis-scope** (vocab audit §4b #4).

### Verify-before-cite audit log (2026-06-12)

| Quantity | Source | Match |
|---|---|---|
| $Z_0 \approx 376.73\,\Omega$ | `constants.py` symbol `Z_0` (`np.sqrt(MU_0/EPSILON_0)`) | ✓ |
| $c_{\mathrm{bulk}}=\sqrt{2}\,c_0$ | `test_vacuum_moduli_and_channels.py`:66–70 | ✓ pytest gate |
| $\Gamma_{\mathrm{EM}}=0$ SYM | `clm-3zz0f6` / `electron-bh-isomorphism.md`:24 | ✓ |

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

- **`:22`** — stamped at `:22`. *(family: Z_bulk=ρc_bulk formula)*  ⚑ **BIAS-DEBT**
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  Bulk-longitudinal | Z_bulk = ρ_bulk c_bulk | √2 ρ_bulk c_0 | Γ_bulk→-1
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  Source-of-truth table for the three-channel law: Γ_bulk→-1 confined reading survives; the ρc_bulk formula and :24's 'c_bulk=√2 c_0 (bulk dilatational speed, not full P-wave)' speed label consume the phantom at formula level (prereg-named class).
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

**Records.** Ruling **R40** (the demotion sweep) · the banked worklist
[`r40_sweep_worklist_verified.json`](../../../../research/drivers/r40_sweep_worklist_verified.json) · batch-0
scope verification and batch-1 execution records in `_orchestration/` · this batch's record
`_orchestration/2026-08-12_r40-sweep-batch2a.md`.

