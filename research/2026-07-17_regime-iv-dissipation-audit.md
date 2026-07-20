# Regime-IV Dissipation Audit — the PRODUCT / TRANSITION split applied to the loss/irreversibility canon

> **SECTOR HEADER (read first).**
> - **MODE:** corpus audit. This document makes **no new physics claim**. It re-reads existing load-bearing prose against one discipline question and records verdicts; it originates no derivation, mints no `clm-`, and moves no value.
> - **REGIME:** the items span **Regimes I–IV**; each appendix row declares its own regime. The audit's organizing carve is orthogonal to regime — it is the **PRODUCT vs TRANSITION** split (below).
> - **PHASE-STATE:** items are adjudicated cold-reactive (sub-yield lossless) vs saturated/ruptured (near/at/above-yield) per their own declared regime; the default reading under test is the *existing dissipative* one.
> - **DISCIPLINE:** flag-don't-fix (the Op3 label-vs-code item is FLAGGED, not fixed); Rule-12 for any touched leaf (bodies preserved, dated notes only); verify-before-cite (every `file:line` below re-verified by `grep -F` at HEAD `525cf4a5`).

**Date:** 2026-07-17 · **Workflow run:** `wf_3f83fc66-6f5` · **Branch:** `docs/retention-transition-batch`
**Machine-readable sidecar:** `research/2026-07-17_regime-iv-dissipation-audit_items.json` (126 items; field schema in §6).
**Ratified context (Grant, in-chat 2026-07-17):** the PRODUCT/TRANSITION SPLIT as corpus discipline; retention lands as a new KEEP-BOTH ratings row (R13); the yield-fork ruling (lean recorded, fork OPEN).

---

## 1. Purpose + the ratified split

The corpus uses one vocabulary — "irreversible", "remanence", "plastic", "latch", "dissipates", "frozen", "erased" — for **two physically distinct moments** that had been silently conflated. Grant ratified the carve as corpus discipline (in-chat, 2026-07-17):

- **PRODUCT — persistence of a latched state.** Does a state (a winding integer, the charge on a `Γ=−1` cavity, a retained order parameter) *survive with the drive off*? Under canon this is **LOSSLESS**: a `Γ→−1` confined reactive mode on a lossless (Axiom-3) substrate "has **no loss channel** in the intrinsic (EM-port-CLOSED) eigenframe ... the intrinsic `Q→∞` ⇒ infinite lifetime ⇒ **the electron PERSISTS in an ideal vacuum**" (`resonant-lc-solitons.md:104`). Persistence "**partly follows from the lossless axiom itself**" (`resonant-lc-solitons.md:108`) — it is a *consistency-class* read of the wall, never an emergence chord, and it needs **no maintenance resistor**.
- **TRANSITION — irreversibility of the crossing.** Is the *act of crossing* the threshold arrow-of-time-bearing? An arrow here is **licensed only from counting**: mode-spreading with reconvergence ≈ 0, or the energy-conserving click. It is **never** licensed by inserting a valve/diode/`Re(Z)` friction. Tier-1 canon states it flat: "the arrow comes from **mode-count or a click, never a valve**" (`research/2026-07-13_f6-tier1-two-reservoir-ledger_CHARTER.md:256`; the honest F6 candidate is "irreversibility **by mode-spreading** — energy dispersed across many incommensurate `ω_m` with no return path ... NOT a smuggled friction", `research/2026-07-16_f6-bath-meter_CHARTER.md:57`).

The precedent for the split is already in the remanence charter: "the **retained order parameter**, not the crossing loss, is what must survive drive-off" (`research/2026-07-12_remanence-r10-fixed-n_CHARTER.md:108`). The audit's single job is to walk each "loss/irreversibility" item and say **which of the two moments it actually invokes** — and, where the invoked moment is PRODUCT, to record that the dissipative reading was a default that does not survive the split.

**What the audit decides:** for each item, one of {RETENTION-ONLY, RADIATIVE-PORT, LOSS-REQUIRED, RATE-CLAIM, AMBIGUOUS} + whether it structurally `requires_R` (a genuine resistor). **What it does not decide:** the open yield-fork (§5) — that is left to the registered discriminators, per the ruling; and it does not edit any body (Rule-12).

## 2. Method

1. **Two independent inventory scouts** swept the corpus for every load-bearing occurrence of the loss/irreversibility vocabulary across the KB leaves, the eight manuscript volumes, the orchestration docket, and the research preregs.
2. The two inventories were **deduped to 126 items** (`inventory_count` = 125 raw + 1 coverage-scope note).
3. The 126 items were grouped into **21 clusters of ≤6** so each adjudication pass held a bounded, comparable set.
4. **Bias-guarded adjudication.** Each item was adjudicated with the **default set to the existing dissipative reading** (i.e. the prior belief that "irreversible/plastic/dissipates" means real loss is the null the item had to *fail* to be reclassified). Each carries an **EE circuit analog** (`ee_analog`) and a **`requires_R` ∈ {yes, no, rate-only, port-only}** tag — does the physics structurally need a genuine resistor, a rate/clock only, a radiative port only, or nothing.
5. **Per-cluster adversarial refute-pass.** After adjudication, each cluster was re-read by an adversarial lens whose job was to *overturn* the adjudicated verdict at HEAD (`verify_outcome` ∈ {OVERTURNED, WEAKENED, UPHELD, NO-VERIFY}). The `verdict_final` is the post-refute verdict.

Run id: **`wf_3f83fc66-6f5`** (2026-07-17). Every `file:line` cited in §4–§5 below was independently re-verified by `grep -F` at worktree HEAD `525cf4a5` before being written here (verify-before-cite). Two citations resolved to a *different file* than the session's working memory suggested — recorded inline where they occur.

## 3. Verdict distribution

**Final verdict (post-refute), n = 126:**

| verdict_final | count | reading |
|---|---|---|
| **RETENTION-ONLY** | 49 | PRODUCT-moment only; lossless persistence of a latched state; no maintenance R |
| **RADIATIVE-PORT** | 24 | real loss, but located at a matched radiative/detector PORT (Ax3-legal `R_rad ≡ Z_0` or `Z_det`), not internal friction |
| **LOSS-REQUIRED** | 19 | structurally needs a genuine resistor (the loop-area / bulk mode-decay / Joule family) |
| **AMBIGUOUS** | 29 | prose invokes both moments or is under-determined; needs the split applied at leaf level |
| **RATE-CLAIM** | 5 | the "irreversibility" is a *timing/clock* condition (an autoresonant lock or a click-rate), not a dissipation |

**Adversarial verify outcome, n = 126:**

| verify_outcome | count | meaning |
|---|---|---|
| **UPHELD** | 38 | adjudicated verdict survived the refute-pass at HEAD |
| **WEAKENED** | 33 | verdict stood but a load-bearing qualifier was added / a dependency exposed |
| **OVERTURNED** | 8 | the refute-pass flipped the adjudicated verdict |
| **NO-VERIFY** | 47 | not independently re-verified in this pass (recorded, not banked) |

## 4. Key findings

### F1 — the Regime-IV "plastic" canon is RETENTION-ONLY (OVERTURNED)

The terminology leaf's plastic-row (`substrate-native-terminology.md:39`) licenses "irreversible plastic deformation" as the correct Regime-IV term and cites exactly **two** exemplars. The refute-pass **OVERTURNED** this row's adjudicated AMBIGUOUS to **RETENTION-ONLY**: both exemplars are *retained permanent offsets requiring no maintenance resistor* — PRODUCT-moment, not TRANSITION-loss.

- **Neutron-star remnant** (`07_stellar_interiors.tex:161`; the paragraph the leaf cites as `:159`) — item verdict RETENTION-ONLY, **UPHELD**:
  > "the vacuum LC lattice has crossed the Axiom 4 saturation phase transition (shear modulus `$G_{shear}\to0$`), **freezing at the transition boundary (Topological Halting)** rather than collapsing to a point."

  The retained control parameter is the *geometric* ratio `$\varepsilon_{11}=7GM/(c^2r)\approx1.46$` (computed from `G,M,c,r`), not a dissipation rate. A frozen topological defect is a held state; the freeze imports no `R`.
- **GW memory offset** (`first-principles-predictions.md:35`, formula at `:40`) — item verdict **AMBIGUOUS** (honest caveat: not fully collapsed):
  > "`$\Delta h_{memory} = h_{peak}(h_{peak}/h_{yield})^2$`, `$h_{yield}=\sqrt{\alpha}\approx0.085$`."

  The magnitude is a **geometric scaling from the Ax4 yield threshold — it imports no hysteresis-loop area and no dissipated-work term** (the "geometric no-loss-coefficient"), so a lossless topological-latch reading exists and is the natural one. The *item* is kept AMBIGUOUS rather than banked RETENTION-ONLY because the refute-pass could not fully exclude a dissipated-work reading at leaf level (`requires_R=yes` retained conservatively). The **word** "plastic" therefore stays licensed in Regime IV for the RETAINED-SET sense; the friction-sense is the open fork (§5).

### F2 — the dissipative branch consolidates to ONE object: the Vacuum Memristor Level-2 `τ_relax` loop

Across all 126 items, the genuinely LOSS-REQUIRED dissipative claims collapse onto a **single object** — the Level-2 (dynamic, at/above-yield) memristive `τ_relax` loop, where the magnitude is *computed from* the loss:

> "Hysteresis loop area | `$\oint S\,dr$` = dissipated energy per cycle" (`tau-relax-derivation.md:24`)
> "The **loop area IS** the integrated lag `$\times\,dr/dt$`, which equals the **dissipated energy per cycle**." (`tau-relax-derivation.md:89`)
> "encloses a **finite area proportional to the energy dissipated** during each thixotropic yield–heal cycle." (`nonlinear-vacuum-capacitance.md:66`; byte-mirror at `vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:339`)

**Load-bearing on:** `clm-n3un96` (the `$\tau_{relax}=\ell_{node}/c$` timescale, hosted by `tau-relax-derivation.md`); `clm-8nkvwy` + `clm-vjv4zf` (the SYM/ASYM saturation-kernel + memristor claims hosted in `nonlinear-vacuum-capacitance.md` frontmatter); and the **pre-registered, UNRUN** prediction `P_phase5_memristor_loop_area` (`tau-relax-derivation.md:109`: Loop area `$=\ell_{node}^2 m_e c^2\cdot f(\omega\tau)$`, `f` peaks at `$\omega\tau_{relax}\approx0.9$`). Honest scope: the audit found the *dissipative* memristor content is an **un-itemized tail** — `clm-8nkvwy` is fundamentally the saturation-kernel claim, and `clm-vjv4zf`'s listed specific-claims (`vol4/claim-quality.md:105–107`) cover only the **reactive** varactor divergence; the loss loop rides these leaves without its own itemized claim, and its magnitude prediction has never been run.

**★ The no-axiom-sourced-resistor flag.** The `R` that closes this loop is *not* an axiom primitive: `$\tau_{relax}=\ell_{node}/c$` derives from **lossless causal propagation** (the minimum state-change time from the K4 Lagrangian; "No faster relaxation mode is axiom-permitted", `tau-relax-derivation.md`). A single relaxation time produces a finite single-`τ` lag loop — but whether that lag is a *dissipated-work* loop (irreversible) or a *reversible reactive* lag depends on the yield-fork (§5). There is no independently-sourced resistor element; the loss is asserted of the crossing, not derived from an axiom `Re(Z)`.

**★ HEAD contradiction pair (flag, not resolved here).** The loop-area family sits directly opposite two standing walk-records:

- `translation-tables/translation-circuit.md:120`:
  > "ideal saturation **dissipates nothing** (lossless refusal, Ax3)"
- `envelope-anatomy.md:101`:
  > "**ideal saturation dissipates nothing** — it is a *lossless refusal*, Axiom-3-compatible" ... and (same line) already an **open-fork flag**: the vol_4 memristor prose "models the near-yield channel ... as *dissipative* / thixotropic / memristive ... That prose sits on the **opposite side of the open τ>τ_yield-vs-lossless fork** ... **standing open fork, not a contradiction introduced by this walk-record** — Grant leans reversible; the fork stays open."

The audit **confirms** this is a standing open fork (the loop-area family vs the lossless-refusal reading), not a defect introduced by either side. It is routed to §5, not adjudicated here.

### F3 — pair production is a RATE-CLAIM, not a loss (verified)

Pair production reads as irreversible, but the "irreversibility" is a **timing/clock condition**, not a dissipation. The mechanism is **energy-conserving `$A_1\to T_2$` impedance redirection** behind a **`$\Gamma=-1$` TOTAL INTERNAL reflection wall (not a radiative port)**:

> "at `$V>V_{yield}$` the local `$c_{local}\to0$` blocks linear KE which **shatters sideways into transverse curl**" (`pair-production-axiom-derivation.md:11`) — i.e. `$A_1$` longitudinal KE redirected into `$T_2$` Beltrami curl, no energy leaves the node pair; the `$\Gamma=-1$` wall is a "**Perfect Short-Circuit Boundary** ... 100% of the kinetic energy ... reflects internally" (`:45`), an internal mirror, not a leak.

The event is **gated by an autoresonant frequency-lock**, a clock:

> "C2 (frequency) | `$\Omega_{node}(A^2_{local})\approx\omega_{drive}$` — **autoresonant lock with driving frequency**" (`pair-production-axiom-derivation.md:22`); "Pair rupture does not fire merely when `$A^2$` crosses 1; it fires when the node pair's rotational resonance drops into the **autoresonant-lock window**" (`:65`).

So `$\Omega_{node}\to\omega_{drive}$` is a **clock, not a resistor** — `requires_R = rate-only`. This **converges with the F6 click-rate question**: an arrow licensed by a counting/clock event (the click), not by a valve — the same license the split grants the TRANSITION moment (§1).

### F4 — ★ Op3 label-vs-code contradiction (FLAGGED, not fixed)

The single sharpest contradiction the audit surfaced. The KB leaf says Op3 **dissipates**:

> `k4-port-irrep-decomposition.md:28`: "Op3 asymmetric dissipation | `$A_1$` **loses energy monotonically**; `$T_2$` settles into quasi-stable pattern"
> `:109`: "This impedance mismatch **dissipates energy asymmetrically** for the two sectors:" ... `:111`: "`$A_1$` **loses energy monotonically until it reaches zero**."

The **code** that implements Op3 is **unitary and power-conserving**:

> `src/ave/core/k4_tlm.py:396–398`: "Unitary: `V_inc_A[k] = Γ * V_ref_A[k] + T * V_ref_B[k]`, where `Γ = (Z_B - Z_A)/(Z_B + Z_A)`, `T = sqrt(1 - Γ²)`. Seen from B, the reflection is `-Γ` (opposite sign). **Conserves total power.**"

A lossless reactive scatter (`$|\Gamma|^2+|T|^2=1$`) cannot dissipate. The refute-pass **OVERTURNED** the Op3 item (`k4-port-irrep-decomposition.md:28`) from AMBIGUOUS to **RETENTION-ONLY**, `requires_R=no`.

- **Candidate re-read — common-mode rejection.** `$A_1$` is the common-mode ("DC across all ports"); its bond-reflection produces **destructive interference** with neighbours (`:111`). The `$A_1$` **mode** energy is *redistributed by counting* into the `$T_2$` pattern; the **system** conserves power. This is **common-mode rejection**, not dissipation.
- **The generalized split:** **LOSS-FROM-A-MODE** (redistribution across modes, an arrow-by-counting) **≠ LOSS-FROM-THE-SYSTEM** (a genuine `Re(Z)` sink). Op3 is the former; the leaf prose reads it as the latter. This is the MODE-vs-SYSTEM worked example that the new discipline leaf (D4) turns into a rule.
- **Consequence:** the terminology leaf's "four licensed loss channels" enumeration (`substrate-native-terminology.md:27`) lists "substrate-intrinsic mode-decay (Op3 `$A_1$`-mode monotonic loss)" as one of the four genuine channels. On the mode-vs-system reading that channel is **not a system-loss** and the enumeration **needs correction on the Op3 channel** (the other three — radiative port, boundary-Joule, Regime-IV rupture — are unaffected). Routed to the operator-physics lane via a dated 🔴 FLAG on the leaf itself (this batch, D6); **flag-don't-fix**.

### F5 — coherence flags routed (owners named; NOT fixed here)

Each of the following is surfaced with its owner; none is adjudicated in this batch.

- **Deep-space resistive-metric family — sub-yield BULK dissipation in tension with Ax3.** `vol_1_foundations/chapters/04_continuum_electrodynamics.tex:249`: diffuse matter "**rapidly dissipates its kinetic energy** into the surrounding lattice via **topological Joule heating** and becomes physically **stalled**" against "the resistive deep-space metric" (`:251`) — this is a *sub-yield* `Re(Z)` bulk loss, exactly the internal-friction the reactive regime is supposed to lack. Its macroscopic consumer, lunar inductive Joule heating `$\approx1.04$` TW (`vol_3_macroscopic/chapters/14_macroscopic_orbital_mechanics.tex:239`; `clm-av2o4v`), carries **solidity 0.20 "(do not build on, rework needed)"** (`vol3/claim-quality.md`). *Owner:* the continuum-electrodynamics / dark-sector lane. *(Verify-before-cite note: the 1.04 TW figure lives in the vol_3 orbital-mechanics chapter, NOT in vol_1 `04_continuum_electrodynamics.tex` — the two are separate items in the same family.)*
- **BH information-erased ↔ topological-retention tension (AMBIGUOUS, OVERTURNED).** `black-holes-impedance-mismatch.md:17`: "The **mass-energy is conserved strictly as latent heat**, but the **geometric quantum information is physically, mathematically, and permanently erased**." One sentence carries both moments — conserved energy (retention/latent-heat) and erased information (irreversibility). *Owner:* the generative-cosmology / BH-interior lane.
- **Three numerically distinct `$\tau_{yield}$` magnitudes under Bingham/plastic naming (+ a resurrected dropped claim).** `vol_0_engineering_compendium/chapters/02_analytical_summaries.tex:17`: "Macroscopic Rheological Yield Stress (**Bingham-Plastic Limit**): `$\tau_{yield}=\frac{\hbar c}{\ell_{node}^4}(1/\alpha^2)\approx7.21\times10^{34}$` Pa" — presented in a chapter titled "Summary of Exact Analytical Derivations", carrying the Bingham/plastic label the F1 split retires for the friction-sense. *Owner:* the vol_0 compendium reconciliation lane.
- **Muon-decay leaky-cavity needs the port-vs-bulk split.** `vol_4_engineering/chapters/14_particle_decay_spice.tex:22`: past `$V_{yield}$` the vacuum is "converting a lossless conservative field into an **absorptive, lossy 'Leaky Cavity'** (`$\Gamma=-1$`)." A `$\Gamma=-1$` boundary is a *reflector*; "leaky cavity" is a *radiative port* framing — the two need the RADIATIVE-PORT-vs-bulk carve applied before "lossy" is load-bearing. *Owner:* the particle-decay SPICE lane.
- **Detector-Joule family — adjudicated port-located, NO ACTION.** The Born-rule / which-path decoherence Joule extraction (`clm-ldmvwi`, Born rule from Ohmic measurement work, Class-4 observable-consistency) and the transmon/Nyquist-FDT damping are real dissipation **at a resistive DETECTOR load `$Z_{det}$` (a matched port)** — Ax3-legal, RADIATIVE-PORT, `requires_R=port-only`. Correctly located; **no correction owed**.

> **★ ADJUDICATED-DEMOTED 2026-07-19 (deep-space reactive-bulk ruling; dated bottom-append to F5, this section otherwise unedited).** The **deep-space resistive-metric family** flagged in the first F5 bullet above — items **85** (`magnetic-saturation.md:38`, galactic-boundary topological-Joule-stall, `clm-8ep2b4` prose), **89** (`04_continuum_electrodynamics.tex:249`, topological Joule heating of stalling matter), **90** (`14_macroscopic_orbital_mechanics.tex:239`, lunar inductive Joule heating `~1.04` TW, `clm-av2o4v`) — is now **ADJUDICATED**. Item 89's re-read note said the call was *"a physics ruling for Grant, not an auditor relabel"*; Grant ruled it in-chat (2026-07-19, verbatim, *sic*): *"it rings but i think theres a bulk reaction from the lattice that makes it lossless/pure reactance, and that there dofferent passpa danof frequencies for effects, like the rings of saturn vs electron orbitals."* **The audit's `LOSS-REQUIRED` verdict on the prose STANDS** — the prose genuinely asserts a sub-yield bulk resistor. The ruling **DEMOTES the prose**, not the audit: the bulk resistor is Ax3-forbidden (`eq_axiom_3.tex:24`) and contradicts the corpus's own Regime-I-lossless resolution (`06_solar_system.tex:203`, "0 Watts"); the deep-space bulk coupling is **lossless / pure-reactance** (added-mass, d'Alembert), with effects **band-structured** (structure-at-resonances, Kirkwood-gap grammar). Dated `🔴` demotion banners landed on all three sites + the KB consumer leaf (`lunar-inductive-heating.md`) + the vol4 boundary-trapping consumers (`clm-h55fy1`); claim-register notes on `clm-av2o4v` / `clm-8ep2b4` (scoped) / `clm-h55fy1`. The belt/Oort/lunar re-derivation as reactive band-structure is **SPEC'd, not run** (Grant-gated). Full arc + attribution + canon anchors: `research/2026-07-19_deep-space-reactive-bulk-walk_RECORD.md`. *(The inductance-vs-resistance conflation the item-85 second flag named is the mechanism the ruling resolves: same `η`, reactive for planets/dark-matter, wrongly resistive for diffuse-matter stall.)*

## 5. The fork record

**Grant ruling (2026-07-17, in-chat).** On the near-yield crossing: Grant's **reversible-reactive lean is RECORDED AS A LEAN**; the **fork stays OPEN**; resolution is by the substrate via the **registered discriminators**, not by fiat.

**The fork question, stated exactly:**

> **Finite-area memristive loop (`$\oint S\,dr\neq0$`, dissipative) vs zero-area saturating reactance (lossless refusal) at the near-yield crossing.**

**Resolution arc — the two registered discriminators (both verified to exist at HEAD `525cf4a5`):**

1. **The thixotropy amplitude-dependent-`τ` prereg** — `research/2026-06-09_thixotropy-amplitude-dependent-tau_prereg.md` (FROZEN, un-run): does `$\tau_{relax}(A)$` carry a `sign(dA/dt)` memory (true thixotropy → rectifies → a genuine loop) or is it an instantaneous `$\tau(A)$` (time-symmetric → no loop → lossless)?
2. **The pre-registered `P_phase5_memristor_loop_area` prediction** — `tau-relax-derivation.md:109` (UNRUN): if the dynamic Level-2 ODE is built and the enclosed loop area is **non-zero** at the predicted `$\omega\tau_{relax}\approx0.9$` peak, the dissipative branch is confirmed; a **zero** area confirms the lossless-refusal branch.

Until one of these fires, the memristive-loop object (F2) is **LOSS-REQUIRED *by construction of its own prose*** but **NOT axiom-forced** — the resistor is asserted at the crossing, not derived. Grant leans reversible; the substrate decides.

## 6. Appendix — full 126-item table

Generated programmatically from the machine-readable sidecar `research/2026-07-17_regime-iv-dissipation-audit_items.json` (full field set per row: `name / file / line / verdict_adjudicated / verify_outcome / verdict_final / requires_R / ee_analog / load_bearing / reasoning / reread_proposal / verify_reasoning`). The compact table below shows six columns; consult the sidecar for the full reasoning, EE-analog, and re-read fields. Rows are grouped by `verdict_final` (RETENTION-ONLY → RADIATIVE-PORT → RATE-CLAIM → LOSS-REQUIRED → AMBIGUOUS), then by file. Paths are abbreviated (`…/` = elided KB/volume prefix); the sidecar carries full paths.

| # | name | file:line | verdict | requires_R | verify | load-bearing (compact) |
|---|---|---|---|---|---|---|
| 1 | rrad-L rectification NULL (banked) | `2026-06-08_rrad-l-rectification_result.md:67` | RETENTION-ONLY | no | NO-VERIFY | Diode-class death #1 in the F6 depletion charter (f6-depletion:104-108) and the substrate… |
| 2 | Two-tank decoherence check — 'heat = reversible phase-scr… | `2026-07-15_two-tank-decoherence-check_NOTE.md:21` | RETENTION-ONLY | no | NO-VERIFY | thermal-phase-registers.md sec1/2/4/6 (PROPOSED-DEFINITIONAL #1 temperature=width, #2 ent… |
| 3 | pn-slipstream-lossless-resolution | `…/app-b-paradoxes/peierls-nabarro-paradox.md:12` | RETENTION-ONLY | no | UPHELD | clm-ghs75o. The PN-paradox resolution: forbids unprovoked Bremsstrahlung, permits smooth… |
| 4 | lattice-phase-transition-g-zero | `…/app-f-solver-toolchain/lattice-phase-transition.md:14` | RETENTION-ONLY | no | UPHELD | clm-d9ivj1 (leaf-hosted; lattice-phase-transition.md frontmatter claims: [clm-d9ivj1], so… |
| 5 | Backmatter SPICE memristor (thixotropic hysteresis) const… | `…/backmatter/06_spice_verification_manual.tex:142` | RETENTION-ONLY | no | NO-VERIFY | One of four SPICE constitutive models (:81); the AVE_VACUUM_CELL subcircuit; Ch18 LLCP me… |
| 6 | newtonian-inertia-as-lenz-memory | `…/ch01-topological-matter/newtonian-inertia-as-lenz.md:12` | RETENTION-ONLY | no | UPHELD | clm-jwyy6l (Mass IS Inductive Resistance); feeds tau-relax-derivation.md section 4 BEMF-f… |
| 7 | bh-event-horizon-dielectric-rupture | `…/ch03-macroscopic-relativity/dielectric-rupture-event-horizon.md:18` | RETENTION-ONLY | no | UPHELD | clm-ir8h78 (leaf-hosted; BH interior phase transition, solidity 0.55). Defines the EM-hor… |
| 8 | neutron-star-regime-iv-kb-row | `…/ch07-stellar-interiors/stellar-regime-classification.md:19` | RETENTION-ONLY | no | UPHELD | Table row in the leaf hosting clm-o6kgkz, but clm-o6kgkz is the MSW charged-current matte… |
| 9 | tau-relax-yield-heal-defect-freezing | `…/ch1-vacuum-circuit-analysis/tau-relax-derivation.md:99` | RETENTION-ONLY | no | NO-VERIFY | clm-n3un96; the phase-5 PRE-REGISTERED predictions P_phase5_yield_heal_residue + P_phase5… |
| 10 | horsemen-loss-only-near-rupture | `…/ch11-experimental-bench-falsification/horsemen-of-falsification.md:26` | RETENTION-ONLY | no | UPHELD | clm-fh6w3y. Load-bearing consumer = the LIGO 1.3 Gly no-absorption null (horsemen:28 'per… |
| 11 | arrow-of-time-geometric-irreversibility | `…/ch11-thermodynamics/arrow-of-time.md:12` | RETENTION-ONLY | no | WEAKENED | clm-t05mvx (shared leaf with entropy-redefinition + macroscopic-temperature-lc-noise); co… |
| 12 | discrete-lattice-entropy-constant | `…/ch11-thermodynamics/discrete-lattice-entropy-constant.md:10` | RETENTION-ONLY | no | UPHELD | clm-cfd5yf; leaf's own interpretation 'minimum phase-ambiguity information at the horizon… |
| 13 | four-entropy-scattering-irreversibility | `…/ch11-thermodynamics/four-entropy-distinction.md:29` | RETENTION-ONLY | no | UPHELD | clm-4o0f0h; consumed by common/statistics-under-ave.md. NOTE on task's 'row 19': the leaf… |
| 14 | kolmogorov-saturation-cutoff | `…/ch11-thermodynamics/kolmogorov-spectral-cutoff.md:41` | RETENTION-ONLY | no | UPHELD | clm-hk81zp (Kolmogorov spectral cutoff / bounded-enstrophy Navier-Stokes regularity resol… |
| 15 | autoresonant-dielectric-rupture-prediction | `…/ch12-falsifiable-predictions/autoresonant-dielectric-rupture.md:14` | RETENTION-ONLY | no | UPHELD | clm-9sujp8; the falsifiable ELI autoresonant sub-Schwinger bench prediction; cross-consum… |
| 16 | compactness-limit-regime-iv | `…/ch15-black-hole-orbitals/ave-compactness-limit.md:18` | RETENTION-ONLY | no | UPHELD | clm-x19btt (AVE Buchdahl/compactness limit R>7GM/c^2). claim-quality.md:174 explicitly: '… |
| 17 | vol1-dielectric-rupture-schwinger-consistency | `…/ch2-macroscopic-moduli/dielectric-rupture.md:12` | RETENTION-ONLY | no | UPHELD | clm-9s9apq (over-bracing / packing-fraction); the p_c = 8*pi*alpha consistency identity a… |
| 18 | dielectric-snap-limit-511kv | `…/ch2-macroscopic-moduli/dielectric-snap-limit.md:42` | RETENTION-ONLY | no | UPHELD | clm-2dwzib; the example-box lab-field-vs-snap ratio (~7.55e-9 -> deep Regime-I safety, di… |
| 19 | virtual-particles-dissipate-to-noise | `…/ch3-quantum-signal-dynamics/quantum-foam-virtual.md:28` | RETENTION-ONLY | no | WEAKENED | clm-t1okz0 + clm-unk0bd prose reframe of QFT quantum-foam / virtual particles (interpreti… |
| 20 | vacuum-rupture-temperature | `…/ch3-quantum-signal-dynamics/thermal-lattice-noise.md:11` | RETENTION-ONLY | no | UPHELD | clm-f4urxy (vacuum rupture temperature 3.44 MK), which depends on clm-viawy9 (K4 photon t… |
| 21 | photon-id-a1-dissipates | `…/ch4-continuum-electrodynamics/photon-identification.md:11` | RETENTION-ONLY | no | UPHELD | clm-3npynp / clm-i4p11y / clm-fr3mos (photon-identification). Consumed by vol1 ch3, vol2… |
| 22 | op3-a1-monotonic-dissipation | `…/ch6-universal-operators/k4-port-irrep-decomposition.md:28` | RETENTION-ONLY | no | OVERTURNED | clm-9kd2t3 (k4-port section 4, 'How Op3 dissipation breaks the symmetry'). Consumed by ph… |
| 23 | vol9-ch8-breakdown-consolidation | `…/ch8-breakdown-characteristics/index.md:11` | RETENTION-ONLY | no | UPHELD | prose-only. Vol-9 datasheet SYNTHESIS index (kind: index, subtree-claims: []); 'synthesis… |
| 24 | Miller avalanche nuclear binding model (Vol 6, batched fa… | `…/chapters/01_computational.tex:333` | RETENTION-ONLY | no | NO-VERIFY | The nuclear-mass formula eq:semiconductor_mass M_nucleus (:349-353); V_BR from 6 pair slo… |
| 25 | Peierls-Nabarro paradox resolution -- sub-yield lossless,… | `…/chapters/01_theoretical_stress_tests.tex:19` | RETENTION-ONLY | no | NO-VERIFY | The 'discrete lattice does not induce Bremsstrahlung' self-consistency defense (a Vol-0 '… |
| 26 | Orbital Friction Paradox resolution -- P_real=0, lossless… | `…/chapters/01_vacuum_circuit_analysis.tex:662` | RETENTION-ONLY | no | NO-VERIFY | Resolves the Orbital Friction Paradox; establishes the Lossless-LC-Tank orbit model + the… |
| 27 | Magnetar B_snap permeability collapse (mu_eff->0 perfect… | `…/chapters/02_absolute_maximum_ratings.tex:88` | RETENTION-ONLY | no | NO-VERIFY | constants.py B_SNAP + absolute-maximum-ratings table (clm-82dxbj); companion vol_1 07_reg… |
| 28 | d-block emergence from Regime IV vacuum yield limit (Vol… | `…/chapters/07_quantum_mechanics_and_orbitals.tex:4079` | RETENTION-ONLY | no | NO-VERIFY | The 'Regime IV Vacuum Yield Boundary' resultbox (:487-489); chapter-summary 'Transition M… |
| 29 | AVE compactness limit -- rupture below R=7GM/c^2 (stricte… | `…/chapters/07_regime_map.tex:166` | RETENTION-ONLY | no | NO-VERIFY | The AVE compactness limit R<7GM/c^2 (stricter than GR Buchdahl 9/4), the NS-interior-rupt… |
| 30 | Dark matter = Regime III->IV saturation-drag transition | `…/chapters/07_regime_map.tex:247` | RETENTION-ONLY | no | NO-VERIFY | Dark-matter-as-phase-transition; flat rotation curves g_eff=sqrt(g_N*a_0); MOND a_0. Batc… |
| 31 | Four-regime map: Regime III avalanche onset r2=sqrt(3)/2… | `…/chapters/07_regime_map.tex:59` | RETENTION-ONLY | no | NO-VERIFY | The whole regime-classification framework -- declared a 'prerequisite gate' (:26) consume… |
| 32 | neutron-star-permanent-defect | `…/chapters/07_stellar_interiors.tex:161` | RETENTION-ONLY | no | UPHELD | substrate-native-terminology.md:39 cites this as the canonical anchor for Regime-IV 'irre… |
| 33 | Vol 9 dielectric rupture (Regime IV) 'irreversible topolo… | `…/chapters/08_breakdown_characteristics.tex:91` | RETENTION-ONLY | no | NO-VERIFY | E_S (eq:vol9_schwinger_field), V_snap, tab:vol9_breakdown_spec; pair-production-axiom-der… |
| 34 | GW propagation without dissipation (LIGO defense) | `…/chapters/08_gravitational_waves.tex:65` | RETENTION-ONLY | no | NO-VERIFY | The LIGO defense: 'matching LIGO observations exactly, with zero free parameters' (:65-66… |
| 35 | 3D avalanche exponent n_3D = 38/21 (Kolmogorov cutoff cha… | `…/chapters/16_kolmogorov_spectral_cutoff.tex:59` | RETENTION-ONLY | no | NO-VERIFY | The 'Macroscopic Avalanche Exponent' resultbox n_3D = 2(1 - ν_vac/3) = 38/21 (:54-58); fi… |
| 36 | appendices-overview-pn-restatement | `…/common/appendices-overview.md:52` | RETENTION-ONLY | no | UPHELD | Overview restatement, verified byte-identical to peierls-nabarro-paradox.md:12, of clm-gh… |
| 37 | kink-trap-nonvolatile-memory | `…/common/appendix-vca-symbols.md:39` | RETENTION-ONLY | no | UPHELD | clm-io8hft (VCA schematic symbol catalogue); symbol-vocabulary reference only, no downstr… |
| 38 | dark-wake-lenz-freeze | `…/common/dark-wake-bemf-foc-synthesis.md:54` | RETENTION-ONLY | no | UPHELD | clm-exjfai (common/claim-quality.md:758; confidence 0.50, solidity 0.30 'do not build on,… |
| 39 | omega-freeze-crystallization-lock | `…/common/omega-freeze-cosmic-grain-cascade.md:42` | RETENTION-ONLY | no | WEAKENED | clm-a7cbqq (Ω_freeze freeze-in at lattice genesis, solidity 0.45), and downstream clm-dsb… |
| 40 | terminology-regimeIV-plastic-canon | `…/common/substrate-native-terminology.md:39` | RETENTION-ONLY | port-only | OVERTURNED | prose-only terminology license; governs the word 'plastic/irreversible plastic deformatio… |
| 41 | terminology-melt-regimeIV-phase | `…/common/substrate-native-terminology.md:41` | RETENTION-ONLY | no | WEAKENED | prose-only terminology license; governs 'melt/liquefy' as a Regime-IV phase noun; cites f… |
| 42 | Peierls-Nabarro no-Bremsstrahlung sub-yield (retired-plas… | `…/common/substrate-native-terminology.md:62` | RETENTION-ONLY | no | NO-VERIFY | prose-only (terminology case-law / discipline precedent); cross-ref by vocabulary-registe… |
| 43 | heat-equals-decoherence-not-dissipation | `…/common/thermal-phase-registers.md:23` | RETENTION-ONLY | no | WEAKENED | The ONE Ax3-derived line in an otherwise WALK-LEVEL / no-claim leaf; check-corroborated b… |
| 44 | Ax3-lossless canonical axiom source: vacuum stores and re… | `…/common_equations/eq_axiom_3.tex:24` | RETENTION-ONLY | no | NO-VERIFY | Axiom source (\input wherever Axiom 3 is formally restated); the 'Ax3-lossless' property… |
| 45 | nuclear-avalanche-breakdown-model | `…/computational-mass-defect/semiconductor-nuclear-analysis.md:22` | RETENTION-ONLY | no | UPHELD | clm-llqd1n + clm-jy8h1x: the definitive mass-validated nuclear masses (He-4 through Fe-56… |
| 46 | FLAG — 'Op3 dissipation: A1 loses energy' (figure + canon… | `…/figures/k4_irrep_decomposition.tex:33` | RETENTION-ONLY | no | NO-VERIFY | photon-identification.md (T2 = photon); k4-port-irrep-decomposition.md canonical leaf (cl… |
| 47 | FLAG: sub-yield 'plastic' register leak in the MOND/dark-… | `…/frontmatter/00_title.tex:28` | RETENTION-ONLY | no | NO-VERIFY | Prose-register only: the abstract (frontmatter/00_title.tex:28) and the mathematical-clos… |
| 48 | translation-circuit-bh-ruptured-plasma-row | `…/translation-tables/translation-circuit.md:142` | RETENTION-ONLY | no | WEAKENED | prose-only (translation-register catalog row; no clm consumes it for a magnitude). |
| 49 | KB dielectric-absorption (memory effect) translation row | `…/translation-tables/translation-circuit.md:494` | RETENTION-ONLY | no | NO-VERIFY | translation-circuit.md ideal-capacitor correction table (§ 'Ideal capacitor'); an EE-tran… |
| 50 | Atom-Q cascade gate: wall loss-Q = lossless endpoint (Q_w… | `2026-07-13_t1-atom-q-cascade-gate_RESULT.md:37` | RADIATIVE-PORT | port-only | NO-VERIFY | Routed auditor-lane relabel of the Q-ladder atom rung (keying-register-walk_framing.md:11… |
| 51 | cmb-thermal-attractor-heat-death | `…/ch04-generative-cosmology/cmb-thermal-attractor.md:10` | RADIATIVE-PORT | port-only | UPHELD | clm-3ii690 — the continuity equation (rho_dot_rad + 4H rho_rad = 3H rho_latent), the (3/4… |
| 52 | dark-energy-latent-heat-definition | `…/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:25` | RADIATIVE-PORT | port-only | WEAKENED | clm-3ii690 (Phantom Energy EoS w<-1, solidity 0.55, build_status input-only) — this leaf… |
| 53 | de-irreversibility-t2-expulsion-arm | `…/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:58` | RADIATIVE-PORT | port-only | WEAKENED | clm-3ii690 — this is the sector-clean placement sentence the whole DE-definition leaf (an… |
| 54 | cosmic-horizon-latent-heat-balance | `…/ch04-generative-cosmology/op14-cosmic-horizon-profile.md:68` | RADIATIVE-PORT | port-only | UPHELD | clm-48g5qf (Op14 Cosmic-Horizon Saturation Profile, solidity 0.45, build_status input-onl… |
| 55 | phantom-eos-latent-heat-expulsion | `…/ch04-generative-cosmology/phantom-energy-equation-of-state.md:10` | RADIATIVE-PORT | port-only | UPHELD | clm-3ii690 — this leaf is the canonical HOME of the w<-1 first-law derivation (the AVE-di… |
| 56 | measurement-probe-irreversible-budget | `…/ch1-vacuum-circuit-analysis/measurement-coupling-probe.md:124` | RADIATIVE-PORT | port-only | NO-VERIFY | clm-zp4kqr (lossless-port back-action energy ledger) + clm-zp7bds (bench-fleet READ/MEASU… |
| 57 | gw-inspiral-radiative-damping | `…/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md:34` | RADIATIVE-PORT | port-only | WEAKENED | clm-v6ti0v (orbital-friction-paradox). Serves as the LOSSY FOIL in the friction-paradox p… |
| 58 | electron-per-cycle-alpha-leak | `…/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md:96` | RADIATIVE-PORT | port-only | WEAKENED | clm-fd1e7a (SubstrateExcitation instance-1); the \|Gamma_EM\|^2=1-alpha relation baked in… |
| 59 | q-tank-reciprocal-alpha | `…/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:44` | RADIATIVE-PORT | port-only | WEAKENED | clm-rtdmsn; the alpha-keystone Q-factor reframe; downstream-consumed by DAMA matched-LC-c… |
| 60 | hubble-tension-latent-heat-choke | `…/ch11-experimental-bench/existing-signatures.md:30` | RADIATIVE-PORT | port-only | WEAKENED | clm-oiw6cb (solidity 0.40; SCOPE-CORRECTION at existing-signatures.md:12 = 'retrospective… |
| 61 | entropy-redefinition-geometric-spreading | `…/ch11-thermodynamics/entropy-redefinition.md:32` | RADIATIVE-PORT | port-only | WEAKENED | clm-t05mvx (shared with arrow-of-time); consumed by common/statistics-under-ave.md; dark-… |
| 62 | nyquist-fdt-derivation | `…/ch11-thermodynamics/nyquist-noise-fdt.md:12` | RADIATIVE-PORT | yes | OVERTURNED | clm-eaiqj1 (confidence 0.7, solidity 0.70 -- the highest-solidity item in this set); cons… |
| 63 | leaky-cavity-particle-decay | `…/ch14-leaky-cavity-particle-decay/theory.md:37` | RADIATIVE-PORT | port-only | NO-VERIFY | clm-c54kdd (muon half-life) + two Gamma=-1 shatter siblings clm-rd9cjm (vol3 gravity leak… |
| 64 | solar-flare-tension-snap | `…/ch14-orbital-mechanics/solar-flares-led-avalanche.md:22` | RADIATIVE-PORT | port-only | WEAKENED | A-034 stellar-scale saturation-kernel FORWARD prediction (0.46-yr FWHM danger-zone; N(E)… |
| 65 | hawking-leakage-imperfect-boundary | `…/ch15-black-hole-orbitals/hawking-temperature-nyquist-noise.md:20` | RADIATIVE-PORT | port-only | UPHELD | clm-c6k5om (T_H = hbar*c^3/(8*pi*G*M*k_B) reinterpreted as Nyquist noise temperature at t… |
| 66 | Vol 6 chemical-reactivity Q: 'dissipation' = acoustic dra… | `…/chapters/01_computational.tex:75` | RADIATIVE-PORT | port-only | NO-VERIFY | The computed Q-values (He-4 = 19.19, Li-7 = 2.85, Be-9 = 7.93) at vol_6/01_computational.… |
| 67 | Cosmology ledger — 'dissipation is frontier-only'; irreve… | `…/chapters/04_generative_cosmology.tex:90` | RADIATIVE-PORT | port-only | NO-VERIFY | dark-energy-latent-heat-definition.md (canonical); the phantom w<−1 result; the ΛCDM-dist… |
| 68 | Vol 5 solvent Stokes-friction damping (dissipative conduc… | `…/chapters/07_solvent_damping.tex:9` | RADIATIVE-PORT | port-only | NO-VERIFY | The folding RATE claim (Honest Limitation #2, :87: 'the Stokes friction determines the ra… |
| 69 | Hulse-Taylor orbital decay via phase-slip real-power blee… | `…/chapters/08_gravitational_waves.tex:79` | RADIATIVE-PORT | port-only | NO-VERIFY | The -2.402e-12 s/s Hulse-Taylor decay rate (:80), an explicit consistency reproduction ('… |
| 70 | Hawking radiation = Nyquist noise leakage through imperfe… | `…/chapters/15_black_hole_orbital_resonance.tex:176` | RADIATIVE-PORT | port-only | NO-VERIFY | T_H resultbox T_H=hbar c^3/(8 pi G M k_B) (:184-188) + evaporation cascade (:192-193) + f… |
| 71 | dark-wake-far-field-radiated-stress | `…/common/dark-back-reaction-taxonomy.md:23` | RADIATIVE-PORT | port-only | UPHELD | clm-7tynm2 (chiral-thrust-derivation.md, dark-wake thrust); the thrust momentum-conservat… |
| 72 | radiation-resistance-port | `…/common/dark-wake-bemf-foc-synthesis.md:13` | RADIATIVE-PORT | port-only | NO-VERIFY | The Rule-2 field/port taxonomy for the dark wake; underpins R_drag=Z_0 (section 1.4) and… |
| 73 | solver-toolchain-ruptured-fluid-reflector | `…/common/solver-toolchain.md:72` | RADIATIVE-PORT | port-only | UPHELD | clm-395gps (AVE merger ringdown omega_R M_g=18/49) and clm-d9ivj1 (Universal Regime-Bound… |
| 74 | pair-production-flux-tube-rupture | `…/ch01-topological-matter/pair-production-axiom-derivation.md:11` | RATE-CLAIM | rate-only | WEAKENED | clm-ezai5b (canonical pair-production mechanism; path-stable, cited by vol2 ch01, vol4 ch… |
| 75 | schwinger-wkb-structural-closure | `…/ch01-topological-matter/q-g18-schwinger-pair-wkb.md:10` | RATE-CLAIM | rate-only | WEAKENED | clm-lj4ok5; the 'structurally closed at WKB' status; the two AVE-distinct predictions it… |
| 76 | four-regimes-regime-iii | `…/ch7-regime-map/four-regimes.md:28` | RATE-CLAIM | rate-only | UPHELD | clm-b2anl4 (Universal Regime Classification, the resultbox/table at this leaf); consumed… |
| 77 | near-yield-dissipative-channel-tau-relax | `…/chapters/01_vacuum_circuit_analysis.tex:324` | RATE-CLAIM | rate-only | UPHELD | eq:relaxation_time (:327) tau_relax=ell_node/c, canonical at tau-relax-derivation.md (clm… |
| 78 | Solar-flare avalanche breakdown + 0.46-yr FWHM danger zon… | `…/chapters/14_macroscopic_orbital_mechanics.tex:197` | RATE-CLAIM | rate-only | NO-VERIFY | The 0.46-yr FWHM forward prediction (:197) + fig:solar_weather_iv (:190-195) + fig:noaa_g… |
| 79 | nvc-pinched-hysteresis-loop | `…/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md:66` | LOSS-REQUIRED | yes | WEAKENED | tau-relax-derivation.md:24 ('Hysteresis loop area = dissipated energy per cycle') and :89… |
| 80 | op14-uniform-damping-row | `…/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md:116` | LOSS-REQUIRED | yes | WEAKENED | prose-only / methodological CONTRAST FOIL. It is the middle row of the sec3 'Three regime… |
| 81 | tau-relax-loop-equals-dissipation | `…/ch1-vacuum-circuit-analysis/tau-relax-derivation.md:89` | LOSS-REQUIRED | yes | NO-VERIFY | clm-n3un96; the phase-5 PRE-REGISTERED prediction P_phase5_memristor_loop_area (Loop area… |
| 82 | transmon-ohmic-damping | `…/ch11-thermodynamics/transmon-decoherence.md:28` | LOSS-REQUIRED | yes | WEAKENED | clm-eaiqj1 (the Ohmic-damping / FDT-balance arm; damping coeff gamma = (Z_0/2)/(omega_0 L… |
| 83 | lunar-inductive-joule-heating | `…/ch14-orbital-mechanics/lunar-inductive-heating.md:22` | LOSS-REQUIRED | yes | UPHELD | clm-av2o4v (confidence 0.5, solidity 0.20 -- 'do not build on, rework needed'); condition… |
| 84 | ohmic-decoherence-born-rule | `…/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md:36` | LOSS-REQUIRED | yes | UPHELD | clm-ldmvwi (Born-rule click-probability derivation) and clm-zuf7g1 (the CHSH/Bell-correla… |
| 85 | galactic-boundary-topological-joule-stall | `…/ch4-continuum-electrodynamics/magnetic-saturation.md:38` | LOSS-REQUIRED | yes | UPHELD | Asteroid-Belt / Oort-Cloud mechanical-origin prediction (prose corollary inside clm-8ep2b… |
| 86 | thixotropic-yield-heal-loop-area-dissipated | `…/chapters/01_vacuum_circuit_analysis.tex:339` | LOSS-REQUIRED | yes | WEAKENED | eq:memristor_constitutive M(q)=dPhi/dq; pinched-hysteresis loop-area = dissipated energy… |
| 87 | crossover-frequency-direction-vs-level2-ode | `…/chapters/01_vacuum_circuit_analysis.tex:341` | LOSS-REQUIRED | yes | UPHELD | crossover-frequency setting the elastic-vs-lossy regime boundary; byte-duplicate KB leaf… |
| 88 | Born rule / which-path decoherence = Joule extraction by… | `…/chapters/03_quantum_and_signal_dynamics.tex:233` | LOSS-REQUIRED | yes | NO-VERIFY | clm-ldmvwi (Phase 2-A master-equation-derivation-path); the Deterministic Born Rule resul… |
| 89 | FLAG -- topological Joule heating of stalling matter in s… | `…/chapters/04_continuum_electrodynamics.tex:249` | LOSS-REQUIRED | yes | NO-VERIFY | Powers the Asteroid Belt / Oort Cloud prediction (04:251): low-mass objects 'stall agains… |
| 90 | Lunar inductive Joule heating ~1.04 TW (conditional consi… | `…/chapters/14_macroscopic_orbital_mechanics.tex:239` | LOSS-REQUIRED | yes | NO-VERIFY | The P_topo ≈ 1.04 TW resultbox 'Lunar Inductive Joule Heating' (:233-237) + figure fig:lu… |
| 91 | Muon decay = dissipative Leaky Cavity past threshold (Vol… | `…/chapters/14_particle_decay_spice.tex:22` | LOSS-REQUIRED | yes | NO-VERIFY | NOT prose-only. Half-life derivation itself (objectivebox:9 'Derive particle half-lives f… |
| 92 | BH interior = dissipative sink in EM channel (information… | `…/chapters/21_black_hole_interior_regime_iv.tex:162` | LOSS-REQUIRED | yes | NO-VERIFY | Information-paradox resolution (Step-6 testability :160-168 + Conclusions :185-196); the… |
| 93 | envelope-anatomy-open-dissipation-fork | `…/common/envelope-anatomy.md:101` | LOSS-REQUIRED | yes | WEAKENED | clm-3surfa / clm-ppasym (envelope wall physics). The dissipative model this leaf flags is… |
| 94 | hysteresis-index-level2-dissipation | `…/common/substrate-hysteresis-index.md:25` | LOSS-REQUIRED | yes | UPHELD | clm-n3un96 (tau-relax-derivation.md §3 Level 2); this leaf is a routing index (INVARIANT-… |
| 95 | terminology-four-licensed-loss-channels | `…/common/substrate-native-terminology.md:27` | LOSS-REQUIRED | port-only | OVERTURNED | prose-only (this is a definitional/no-claim terminology-discipline leaf; hosts no clm-);… |
| 96 | terminology-memristive-loop-electron-lock | `…/common/substrate-native-terminology.md:42` | LOSS-REQUIRED | yes | WEAKENED | clm-8nkvwy (nonlinear-vacuum-capacitance.md, the Vacuum Memristor) + clm-n3un96 (tau-rela… |
| 97 | temporal-classifier-lossy-regime | `…/common/temporal-saturation-regime-classifier.md:44` | LOSS-REQUIRED | yes | WEAKENED | clm-f0jwtk (the temporal classifier). Consumed by the cross-field analogue tables (fluid… |
| 98 | Coverage note — dissipation-family search scope at HEAD 2… | `/Users/grantlindblom/AVE-staging/AVE-Core` | AMBIGUOUS | no | NO-VERIFY | Scope declaration for this adjudication batch (cluster 21/21). |
| 99 | Thixotropy amplitude-dependent-tau prereg (open door Vol… | `2026-06-09_thixotropy-amplitude-dependent-tau_prereg.md:30` | AMBIGUOUS | no | NO-VERIFY | Consumed at HEAD by Vol 9 05_ac_electrical_characteristics.tex:599 (grep-verified) -- the… |
| 100 | Saturation-anatomy walk: 'ideal saturation dissipates not… | `2026-07-10_rulings-docket.md:1330` | AMBIGUOUS | no | NO-VERIFY | Landed in translation-circuit.md sec4 (:120 'ideal saturation dissipates nothing (lossles… |
| 101 | Remanence R10 Ax3 carve: remanence DOF = lossless-latch O… | `2026-07-12_ave-native-rulings_g-persist_x-ledger.md:104` | AMBIGUOUS | yes | NO-VERIFY | G-PERSIST ruling (CONFIRMS bin (ii) A-WEAKENED, Grant 2026-07-13); remanence-r10 CHARTER… |
| 102 | F6 = irreversible eps->T2 depletion; Re(Z)!=0 one-way (pr… | `2026-07-13_f6-depletion-tier1-charter-handoff.md:62` | AMBIGUOUS | port-only | NO-VERIFY | The DE-tracks-matter chord -- the one LambdaCDM-distinct thing AVE could carry (dark-ener… |
| 103 | F6 mode-count door -- irreversibility WITHOUT sub-yield f… | `2026-07-15_f6-mode-count-door_CHARTER.md:13` | AMBIGUOUS | no | NO-VERIFY | The legal in-Hamiltonian sink that BOTH the DE-tracks-matter chord AND the thermometer ga… |
| 104 | f6-irreversible-depletion-unbuilt | `…/ch02-general-relativity/saturating-modulus-and-backreaction.md:165` | AMBIGUOUS | yes | WEAKENED | clm-w5ez6i (Stage-3, BUILT, reversible: saturating-modulus-and-backreaction.md:150 \|dH/H… |
| 105 | bh-interior-melt-to-plasma | `…/ch04-generative-cosmology/black-holes-impedance-mismatch.md:15` | AMBIGUOUS | no | UPHELD | clm-ir8h78 (leaf-hosted, solidity 0.55) and clm-c6k5om (Hawking-Nyquist temperature, soli… |
| 106 | bh-information-permanently-erased | `…/ch04-generative-cosmology/black-holes-impedance-mismatch.md:17` | AMBIGUOUS | no | OVERTURNED | clm-ir8h78 (leaf-hosted) + clm-c6k5om (the 'information loss / AVE sides with Hawking' in… |
| 107 | dama-real-power-drag-coefficient | `…/ch05-dark-sector/dama-matched-lc-coupling.md:237` | AMBIGUOUS | yes | WEAKENED | clm-5em8fx. The REAL-power categorization is the STATED basis for EXCLUDING kappa_entrain… |
| 108 | nvc-thixotropic-liquefaction | `…/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md:50` | AMBIGUOUS | yes | OVERTURNED | Sits under clm-vjv4zf (vol4/claim-quality.md:98; conf 0.90, sol 0.90) but that claim's LI… |
| 109 | tau-relax-memristive-substrate | `…/ch1-vacuum-circuit-analysis/tau-relax-derivation.md:11` | AMBIGUOUS | rate-only | NO-VERIFY | clm-n3un96 (tau_relax=l_node/c timescale); consumed as the Op14-dynamics timescale and by… |
| 110 | tki-resistance-viscosity-row | `…/ch1-vacuum-circuit-analysis/topological-kinematics.md:93` | AMBIGUOUS | no | WEAKENED | clm-fy05jc: the six-row TKI dictionary (dimensionally-exact identities). This is the LICE… |
| 111 | vol9-ch14-bh-melt-daughter-cosmology | `…/ch14-phase-diagrams/index.md:23` | AMBIGUOUS | yes | WEAKENED | prose-only. Vol-9 datasheet SYNTHESIS index (kind: index, subtree-claims: []); 'Class B/C… |
| 112 | gw-memory-permanent-plastic-deformation | `…/ch15-black-hole-orbitals/first-principles-predictions.md:35` | AMBIGUOUS | yes | UPHELD | prose-only. The Delta-h_memory resultbox is an 'untapped first-principles prediction'; th… |
| 113 | photon-id-irreversible-lock-unresolved | `…/ch4-continuum-electrodynamics/photon-identification.md:32` | AMBIGUOUS | no | WEAKENED | Prose/gap-marker only -- the R1 evidence table 'unresolved' row (photon-identification.md… |
| 114 | bingham-plastic-yield | `…/ch6-universal-operators/saturation-operator.md:27` | AMBIGUOUS | no | WEAKENED | clm-gdd70j (the Universal Saturation Operator). The Bingham bullet is 1 of 4 illustrative… |
| 115 | four-regimes-regime-iv | `…/ch7-regime-map/four-regimes.md:29` | AMBIGUOUS | no | WEAKENED | clm-2dwzib, clm-b2anl4 (Regime-IV definitional row). Cross-linked to the zero-impedance-b… |
| 116 | four-regimes-melt-flag | `…/ch7-regime-map/four-regimes.md:31` | AMBIGUOUS | no | UPHELD | prose-only Rule-12 coordinate relabel (FLAG block). Supports the melt-predates-crystal /… |
| 117 | four-regimes-r3-breakdown-manifestations | `…/ch7-regime-map/four-regimes.md:58` | AMBIGUOUS | no | WEAKENED | r_3=1 boundary description supporting clm-2dwzib; the cross-domain UNIVERSALITY claim of… |
| 118 | AUDIT-SYNTHESIS-open-questions-and-lane-note | `…/ch7-regime-map/four-regimes.md:60` | AMBIGUOUS | no | UPHELD | META. Aggregates the yield-fork status across items 1-6. |
| 119 | FLAG: three numerically distinct 'yield stress' magnitude… | `…/chapters/02_analytical_summaries.tex:17` | AMBIGUOUS | no | NO-VERIFY | The tau_yield value carrying the yield/Bingham label across vols 0/1/4: vol_0/02_analytic… |
| 120 | Vol 9 thixotropic bulk τ_sat vs τ_desat asymmetry (record… | `…/chapters/05_ac_electrical_characteristics.tex:599` | AMBIGUOUS | rate-only | NO-VERIFY | Cites research/2026-06-09_thixotropy-amplitude-dependent-tau_prereg.md and records tab:vo… |
| 121 | Entropy operator + Ohmic damping FDT (irreversible cohere… | `…/chapters/11_thermodynamics_and_entropy.tex:131` | AMBIGUOUS | yes | NO-VERIFY | Entropy operator S-hat=-k_B sum ln(1-\|Gamma_i\|^2) (:53-59); Nyquist FDT resultboxes on… |
| 122 | GW memory = permanent plastic deformation (Delta_h_memory… | `…/chapters/15_black_hole_orbital_resonance.tex:318` | AMBIGUOUS | no | NO-VERIFY | resultbox Delta_h_memory = h_peak(h_peak/h_yield)^2, h_yield=sqrt(alpha) (:319-323) + fig… |
| 123 | dt-pair-production-topological-snap | `…/common/dark-wake-bemf-foc-synthesis.md:153` | AMBIGUOUS | port-only | WEAKENED | prose-only in this common synthesis doc, but feeds §7's consolidated 'DT pair-production… |
| 124 | lh-transition-plastic-bifurcation | `…/common/dark-wake-bemf-foc-synthesis.md:159` | AMBIGUOUS | no | OVERTURNED | prose-only in this common synthesis doc; feeds §7's 'L-H transition trigger 43.65 kV E x… |
| 125 | abandoned-interior-flash-irreversibility-hole | `…/common/the-abandoned-interior.md:115` | AMBIGUOUS | yes | WEAKENED | no-claim framing/lineage leaf (prose-only; frontmatter no-claim verified). The FLASH-vs-L… |
| 126 | nuclear-q-vacuum-friction | `…/computational-mass-defect/network-analytics.md:16` | AMBIGUOUS | port-only | OVERTURNED | clm-o9xphr Q-values (He-4 19.19, Be-9 7.93, Li-7 2.85, Tritium 3.27) + the high-Q-inert /… |

