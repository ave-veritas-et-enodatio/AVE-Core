# Vacuum Metallurgy — Toolkit Import + Law-vs-Texture Classification (mapping lane)

**Date:** 2026-07-20 · **Lane:** implementer / VACUUM-METALLURGY (Grant-fired 2026-07-20) ·
**Branch:** `research/vacuum-metallurgy` · **Scope:** `research/`-only (new files; no KB/tex edits) ·
**Companion:** [`2026-07-20_vacuum-metallurgy_kz-relic-and-instruments.md`](2026-07-20_vacuum-metallurgy_kz-relic-and-instruments.md) (D3 + D4).

> **SECTOR / REGIME / PHASE-STATE HEADER (read first).**
> - **MODE:** *mapping + classification*. No solver, no driver, no engine byte touched. The
>   object is a **classification** of the framework's calibration inputs and relics against an
>   imported materials-science toolkit (Landau law-vs-texture; Kibble–Zurek). No numerical code.
> - **REGIME / PHASE-STATE:** the whole lane lives at the **crystallization / phase-boundary**
>   register — lattice genesis (the freeze), the observable Γ-boundaries (electron wall, BH
>   horizon, Schwinger wall) as the accessible phase-boundary *samples*. Cold medium away from
>   those boundaries; near-yield / ruptured (Regime IV) *at* them.
> - **SECTOR:** cross-sector by construction (A1 dilatation-mass, T2 transverse, Cosserat winding,
>   bulk/shear/EM channels all appear as *different boundary instruments*). Ownership is tracked
>   per-entry; never cross-wired (mass = A1, charge = Cosserat winding, μ = sign-selector).
>
> **CLASS BANNER (consistency-vs-emergence, fired at design time).** This deliverable is
> **CONSISTENCY-class relabeling**. It maps the framework's *already-canonical* FORM-deriving /
> VALUE-importing finding ([`form-deriving-value-importing.md`](../manuscript/ave-kb/common/form-deriving-value-importing.md),
> `clm-acdc07`) onto the *imported* Landau **Hamiltonian-class vs texture-class** split. It mints
> **no `clm-`**, derives **no new value**, and headlines **no chord**. It is not an emergence test.
> The **only** candidate *forward* content it surfaces is (1) the Kibble–Zurek relic-scaling FORM
> (D3) and (2) the ringdown soft-mode-systematics question (D4a) — **both flagged candidate-only,
> both fail-closed UNDETERMINED at their decisive step**. Most of what follows is a re-labeling of
> the existing record in the materials-science register — *said so*, per the symmetric standard.
>
> **DISCIPLINE.** verify-before-cite two-method on every canon cite (anchor-checker run on the diff).
> Fail-closed **UNDETERMINED** wherever a classification is unforced. Flag-don't-fix (contradictions
> surfaced with both file paths, never silently reconciled). All external observational figures
> `[import]`-tagged with citation. Pure-corpus.

---

## 0. The frame (Grant-ratified walk wording — tagged as such; NOT Grant verbatim)

*(The following restates the lane's founding frame in the wording ratified for this lane. It is
tagged ratified-frame, not a Grant verbatim quote.)*

The **FORM/VALUE law** — the substrate FORCES the dimensionless FORMS (chords) but IMPORTS the
dimensionful VALUES of a handful of calibration constants (echoes)
([`form-deriving-value-importing.md`](../manuscript/ave-kb/common/form-deriving-value-importing.md)) —
begs a question it does not itself answer:

> **When the vacuum crystallized, could the values have come out differently?**

Materials science answers the analogous question with a **principled split** (Landau):

- **Hamiltonian-class quantities** — moduli, transition temperatures, the interaction couplings —
  are *law*: derivable from the interaction, the same for any sample regardless of how it was cast.
- **Texture-class quantities** — domain orientation, defect density, residual stress, the frozen
  handedness of a chiral casting — are *history*: derivable only *statistically*, via Kibble–Zurek
  quench-rate scaling; they are the **casting relics**, not the law.

**The lane's insight (ratified frame):** do not reinvent the wheel — **import the toolkit**. The
observable Γ-boundaries the framework already banks (the electron wall, the black-hole horizon, the
Schwinger wall) are the **accessible phase-boundary samples** and the classification's **first hard
data**: what boundary-equilibrium objects (electrons) and re-melted-then-re-frozen regions (black
holes) teach us is precisely *which side of the Landau split each of the framework's numbers lands
on*.

**One-line thesis (the classification's payload):**
**PARTICLE PROPERTIES = LAW** (boundary-equilibrium; identical across all formation histories);
**PARTICLE POPULATIONS = HISTORY** (casting relics; frozen at genesis, only statistically derivable).
The α/G *values* sit on the **seam** — law-*looking* (uniform everywhere) but texture-*rooted*
(they inherit from a single frozen casting parameter) — and the classification fails **closed**
there: UNDETERMINED between law and single-domain texture, discriminated only by a spatial/temporal
Δα/α measurement.

> **The unifying observation (consistency-class; the reason to bother importing the toolkit).**
> The Landau split is the **same cut** as the framework's own FORM/VALUE split, viewed through a
> second lens. **FORM = chord = Hamiltonian-class** (the dimensionless structure, forced by the
> interaction/topology, history-independent). **VALUE = echo = texture-class** (the calibration
> magnitudes, frozen in at casting, un-derivable from the interaction). What the import *adds* is a
> **principled REASON the values are un-derivable** — not "we happen to feed them in," but "they are
> texture-class quantities, and texture is not a theorem of the Hamiltonian; it is a theorem of the
> casting history." That is a re-labeling with explanatory content, **not** a new derivation and
> **not** a chord. Say so.

---

## D1 — Toolkit import at FORM level (each piece: Ax3-compatibility check)

Per the EE-first landing discipline, the elastic-mechanics sibling is **co-equal** to the EE
register. Each imported piece below is a **candidate translation-row** — *routed for canon
promotion, not landed here* — with an explicit **Ax3-compatibility check** (does the piece import
clean into a lossless-reactive substrate, or does it carry dissipation that needs adaptation?).

Ax3 is the **minimum-reflection / lossless-reactive** principle
([`ave-kb/CLAUDE.md`](../manuscript/ave-kb/CLAUDE.md) INVARIANT-S2, Axiom 3). The test for each
import: *is the argument kinematic (signal-speed, causality, geometry — Ax3-clean) or does it lean
on real dissipation (nucleation kinetics, plastic loss — needs lossless adaptation)?*

### (a) Solidification / quench–anneal — ALREADY IN-CORPUS (cite, do not reinvent)

The moving-front fast-freeze **sample-and-hold** mechanism is already derived and banked. On a fast
down-crossing through yield, the memristive state `S(t)` lags below `S_eq(r)` (the finite
relaxation time `τ_relax = ℓ_node/c ≈ 1.288×10⁻²¹ s`), and the lag *samples* the pre-crossing
topology and *holds* it — a defect that cannot unwind during the crossing freezes in.

- **Home:** [`2026-06-30_moving-front-freezein_result.md`](2026-06-30_moving-front-freezein_result.md)
  §mechanism (`:34`, "the memristive `S(t)` lags below `S_eq(r)`"; `:47`, "grounding-pass direction
  (fast → freeze) is CORRECT per the memristive-lag"); reproduction gate MATCH on current main
  ([`2026-07-19_moving-front-freezein_landing-addendum.md`](2026-07-19_moving-front-freezein_landing-addendum.md) §1).
- **doc-59 Flag B (cool-from-above):** the *cosmological* branch of the same memristive hysteresis
  loop — cooling reduces `r` smoothly across volumes and the yield-heal down-crossing freezes
  topology in
  ([`_archive/L3_electron_soliton/59_memristive_yield_crossing_derivation.md`](_archive/L3_electron_soliton/59_memristive_yield_crossing_derivation.md)
  §4 "Yield-heal branch (down-crossing, cool-from-above)"; Flag B `:666`).
- **Consolidation index:** [`substrate-hysteresis-index.md`](../manuscript/ave-kb/common/substrate-hysteresis-index.md)
  §4 (defect-freezing / matter-precipitation / ω-freeze), which itself routes to the Ω_freeze
  cascade + trampoline framework.
- **★ HONEST STATUS (flag-don't-fix).** The lasting-freeze claim is a **banked NEGATIVE**: real-space
  defect persistence tops out at **≤ 3–6 Compton periods** vs the pre-registered **≥ 100 Cp** target
  (~30× short), resolution-robust to N=32
  ([`genesis-chord-falsification-ledger.md:92-93`](../manuscript/ave-kb/common/genesis-chord-falsification-ledger.md)).
  The *sample-and-hold mechanism* is confirmed and rate-dependent; the *lasting cosmological freeze*
  is not demonstrated at driver scale. The toolkit-import uses the **mechanism** (confirmed), not
  the **persistence magnitude** (negative).
- **Ax3-compat:** **CLEAN with a caveat.** The memristive lag is a *reactive* memory (a diverging
  `L_eff` near `S→0`, Lenz-class) — Ax3-compatible as a lossless reactive latch. But whether the
  near-yield relaxation is genuinely lossless-reactive or carries transduction-to-bath dissipation
  is the **OPEN Flag F fork** (see (e) and D3): world-(c) axiom-resistor is *excluded*, world-(a)
  reactive-return vs world-(b) transduction is **DEGENERATE / UNDETERMINED**
  ([`2026-07-20_jomega-derivation_result.md`](2026-07-20_jomega-derivation_result.md) §0.1). So the
  sample-and-hold imports clean at the *latch* level; its *dissipative* content is unforced.

### (b) Residual stress — the history-vs-equilibrium discriminator

Residual stress is the materials-science archetype of a **texture-class** quantity: a stress field
locked in at solidification that is *not* the equilibrium state and is derivable only from the
casting history. The framework already has the exact analog — the **over-bracing `u_0* ≈ 0.187`**:
the bond rest-lengths lock at the *rotating-frame* equilibrium at genesis, leaving a frozen-in
over-bracing residual that is not the static-frame equilibrium
([`omega-freeze-cosmic-grain-cascade.md`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md)
§2, "Bond rest lengths lock at the rotating-frame equilibrium → `u_0*` over-bracing").

- **Candidate translation-row:** *residual over-bracing `u_0*` ↔ residual stress (casting relic)*.
  The discriminator materials science uses — measure the stress at points a formation-history model
  predicts differently, and compare against the equilibrium prediction — maps to the **three-route
  discriminator**: `u_0*` is back-solved from CODATA α, G (the fit inputs) and *tested* by the
  independent `𝒥_cosmic` route (§2 / D2).
- **Ax3-compat:** **CLEAN.** A residual *elastic* pre-stress is a stored reactive strain — Ax3-native
  (the loaded-cold elastic tensor is banked lossless, `research/2026-07-04_saturated-elastic-tensor_result.md`).
  Residual *plastic* stress would carry dissipation, but the STZ/plastic channel is already retired
  as Ax3-failing (memory `project_amorphous_retirement_two_senses.md`); the import uses the elastic
  (reactive) residual only.

### (c) Stress-coupled / martensitic transformations — structure selection by stress state

Martensitic transformations select the *product structure* by the **stress state during the
transition** (not by the equilibrium free energy alone) — the textbook mechanism for
**history-dependent structure selection**. The framework's analog is the **chirality selection at
genesis**: the *direction* of `Ω_freeze` becomes the direction of bond bowing, selecting the
right-handed `I4_132` chiral space group
([`omega-freeze-cosmic-grain-cascade.md`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md)
§2 step 2). The rotating-frame *stress state* (centrifugal, set by `Ω_freeze`) selects the product
handedness — a martensitic-class stress-coupled selection.

- **Candidate translation-row:** *`Ω_freeze` rotating-frame stress ↔ martensitic transformation
  stress-bias; product handedness ↔ selected variant*. This is the mechanism that makes the
  chirality handedness **texture-class** (see D2 entry 10).
- **Ax3-compat:** **MIXED — the selection is clean, the transformation kinetics are not.** The
  *selection rule* (stress-state → variant) is a geometric/energetic statement, Ax3-clean. But a
  martensitic transformation is *first-order* and its **nucleation kinetics carry latent heat /
  dissipation** — that piece needs lossless adaptation (it is exactly the Flag F fork again, and the
  Ax4 first-order-vs-reactive order question in D3). Tag: **selection imports clean; kinetics
  gated on Flag F.**

### (d) The Landau law-vs-texture split — the classification's engine

The organizing principle itself: partition the observables into Hamiltonian-class (law) vs
texture-class (history). **This is the D2 engine** — the import is the *criterion*, applied to the
framework's number-list using the boundary data (D2) as evidence.

- **Candidate translation-row:** *Landau Hamiltonian/texture split ↔ FORM/VALUE (chord/echo) split*
  — the unifying observation of §0. FORM = Hamiltonian-class, VALUE = texture-class, with the import
  supplying the *reason* the values are un-derivable (texture is not a Hamiltonian theorem).
- **Ax3-compat:** **CLEAN.** A classification criterion carries no dynamics; it is Ax3-agnostic. (The
  *quantities* it sorts carry their own Ax3 status; the criterion does not.)

### (e) ★ Kibble–Zurek — the relic-density scaling (the make-or-break import)

Kibble–Zurek (KZ) predicts the **topological-defect density** left by a phase transition scales as a
**power law in the quench rate**, `n ~ (τ_quench/τ_relax)^{-ν/(νz+1)}`. It was **built for cosmology**
and **verified in materials** (liquid crystals, superfluid ³He/⁴He, superconducting rings). Its two
load-bearing pieces import *differently*:

- **The causal core (Ax3-CLEAN).** The KZ argument's spine is **causality**: the correlation length
  `ξ` cannot grow faster than the signal speed allows (`ξ ≤ c·t`), so at a finite quench rate the
  system freezes with a *finite* correlation length and a *finite* defect density. This is a
  **signal-speed / reflection argument** — pure Ax3 (minimum-reflection, `c` as the propagation
  limit). **Imports clean.** The framework *already has this piece*: doc-59's regime table splits
  slow-cooling (`ξ_thermal ≫ c·τ_relax`, each cell independent, defect density **linear** in cooling
  rate) from fast-cooling (`ξ_thermal ≪ c·τ_relax`, **KZ-like** scaling), with the crossover at
  `τ_cool ≈ ξ_thermal(T_yield)/c`
  ([`_archive/L3_electron_soliton/59_memristive_yield_crossing_derivation.md`](_archive/L3_electron_soliton/59_memristive_yield_crossing_derivation.md)
  §5 regime table, `:386-390`). The causal crossover **is** the KZ causality piece, and it is
  in-corpus.
- **The nucleation kinetics (needs lossless adaptation).** Standard KZ's *exponent* `ν/(νz+1)` is set
  by the **critical-point relaxation dynamics** — in the canonical (model-A) treatment these are
  **overdamped / dissipative**. The framework's near-yield dynamics order is the **OPEN Flag F fork**:
  world-(c) rate-independent plastic resistor **EXCLUDED [DERIVED]**, world-(a) lossless-reactive vs
  world-(b) transduction **DEGENERATE / UNDETERMINED**, physical-scope routed to Grant
  ([`2026-07-20_jomega-derivation_result.md`](2026-07-20_jomega-derivation_result.md) §0.1, §0.3;
  Flag F PARTIALLY discharged, `2026-07-19_flag-f-s-dynamics-derivation.md` §0). **So the KZ
  *exponent* does not import clean** — it depends on the order of the near-yield transition, which is
  unforced. doc-59's own reading is that **Ax4 is first-order** (Bingham/yield), giving a **LINEAR**
  defect density "distinctly different from the KZ power-law … because Ax4 is a first-order
  transition, not second-order" (`:650`, `P_phase5_cooling_rate_density`). But the J(ω) result shows
  the first-order relaxation ODE that underwrites the LINEAR reading is itself **unlicensed at
  `ωτ ~ 1`**, so the LINEAR-vs-power-law verdict is **not currently forced**.
- **AVE-native KZ home (cite, do not reinvent):** the whole KZ treatment is *already* in doc-59 as
  "BEMF-driven defect freezing (AVE-native for Kibble–Zurek)" (§0 core claim). D3 uses it verbatim.
- **Ax3-compat verdict:** **causal core CLEAN; kinetics/exponent GATED on Flag F (needs lossless
  adaptation).** This split is the load-bearing D3 finding.

> **D1 summary — translation-row candidate ledger (routed for canon promotion, NOT landed):**
>
> | # | Import | Corpus analog (home) | Ax3-compat |
> |---|---|---|---|
> | (a) | solidification / quench-anneal sample-and-hold | moving-front freeze-in + doc-59 Flag B | CLEAN (latch); dissipative content unforced (Flag F) |
> | (b) | residual stress (history-vs-equilibrium) | over-bracing `u_0*` (rotating-frame residual) | CLEAN (elastic residual) |
> | (c) | martensitic / stress-coupled structure selection | `Ω_freeze` → chirality handedness selection | MIXED (selection clean; kinetics gated on Flag F) |
> | (d) | Landau law-vs-texture split | FORM/VALUE (chord/echo) split | CLEAN (criterion, Ax3-agnostic) |
> | (e) | ★ Kibble–Zurek relic scaling | doc-59 BEMF defect-freezing + regime table | causal core CLEAN; exponent GATED on Flag F |
>
> None is landed as canon by this lane; each is a routed candidate.

---

## D2 — The classification: Hamiltonian-class vs texture-class vs UNDETERMINED

**Method.** Sort the framework's number-list using the **boundary data** as evidence. Two data
carry most of the weight:

- **(i) Electron indistinguishability** `[import — standard QM: all electrons carry identical
  charge / mass / spin, to the precision of every test]`. Boundary-equilibrium objects that are
  *identical across all formation histories* ⇒ their per-object properties are **law-class** (the
  same interaction fixes them for any casting). The electron is the framework's boundary-equilibrium
  precipitate (D4c), so `m_e` and the per-electron operating point `A = √α` (α-as-coupling) inherit
  law-class *as observed*.
- **(ii) BH no-hair + ringdown universality.** A black hole is a region driven **past yield into
  Regime IV (re-melted plasma)** and then re-freezing at its boundary. The no-hair theorem `[import
  — GR]` + the observed **ringdown universality** (the framework's own banked match, D4a) say the
  re-frozen boundary physics is **identical regardless of what fell in** ⇒ the moduli that set the
  ringdown are **law-class (Hamiltonian)**, not casting-texture. Re-melt-and-re-freeze reaches the
  *same* moduli.

**★ The honest alternative both data admit — single-domain casting.** Neither (i) nor (ii) actually
*proves* law-class; both are **equally consistent with a single-domain casting** whose texture
correlation length exceeds the horizon. If the whole observable universe froze from **one seed**
(doc-59 §5.4: one crystallization event, one `Ω_freeze`, propagating outward past the causal
horizon), then every electron precipitates with the *same* imported value and every re-melted region
re-freezes to the *same* frozen texture — texture that **looks like law** because there is only one
domain to compare. The framework's *own* three-route mechanism says exactly this: α and G inherit
their values from the **single frozen casting parameter** `u_0*/Ω_freeze`
([`omega-freeze-cosmic-grain-cascade.md`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md)
§2: "The three downstream numbers (α, G, 𝒥_cosmic) all inherit from this single freezing event").

The **discriminator** between law and single-domain-texture is a **spatial or temporal variation of
the imported values** — a second casting domain, or drift over cosmic time:

- **Quasar Δα/α spatial-variation bounds** `[import]`. The Webb et al. dipole claims
  (Δα/α ~ 10⁻⁶ across the sky, from many-multiplet quasar absorption spectra) — carried here **with
  both sides**: the dipole is contested, and multiple independent re-analyses (VLT/UVES and Subaru
  data, and the Keck-vs-VLT systematic re-examinations) find **null** at the ~10⁻⁶ level. Carry the
  claim AND the null; the classification does not adjudicate the astronomy.
- **Atomic-clock α-drift bounds** `[import]`. Laboratory optical-clock comparisons bound
  `|α̇/α| ≲ 10⁻¹⁸ /yr` — a temporal-variation null at the current precision.

**Both discriminators are currently null / contested**, i.e. **consistent with single-domain
casting** (one frozen value, no second domain, no drift). So the α/G *value* classification
fails **closed: UNDETERMINED between Hamiltonian-law and single-domain-texture**, with the
discriminator dataset named. This is the elegant α rescope stated precisely (see the α row).

### The classification table

Evidence-class legend: **BE** = boundary-equilibrium / indistinguishability (i); **NH** = BH
no-hair + ringdown universality (ii); **GEN** = genesis-mechanism (doc-59 / Ω_freeze cascade);
**FV** = FORM/VALUE canonical verdict; **DISC** = discriminator dataset.

| # | Quantity | Landau class | FORM (law-side) | VALUE / origin (history-side) | Evidence |
|---|---|---|---|---|---|
| 1 | **m_e** | **HAMILTONIAN** (law) | — (the calibration anchor) | DEFINITIONAL — `ℓ_node ≡ ℏ/m_e c`; law-class *as observed* via electron indistinguishability | BE; FV (DEFINITIONAL) |
| 2 | **ℓ_node** | **HAMILTONIAN** (law) | — (rides m_e) | DEFINITIONAL — the calibration length; same status as m_e | BE; FV |
| 3 | **α** | FORM Hamiltonian; **VALUE UNDETERMINED** (law vs single-domain texture) | α-decomposition `4π³+π²+π` is topology-forced | continuum-axiom **ECHO** (proven; every lift-route closed-negative); interatomic-**law argued** (doc-59 Flag G — pre-lattice potential unspecified); single-domain **texture** via `u_0*/Ω_freeze` (three-route) | BE; GEN; FV (ECHO); DISC (quasar Δα/α + clock drift) |
| 4 | **G** | FORM Hamiltonian; **VALUE UNDETERMINED** (single-domain texture via boundary termination) | Achromatic-Lens `/7` PPN FORM (SYM ε·μ co-scaling → Z=Z₀, Γ=0) | **MIXED** (FV): ξ-termination back-solved from CODATA G; via three-route inherits from `u_0*/Ω_freeze`; G's value is a **cosmic-boundary** quantity → more texture-flavored than α | NH (moduli-adjacent); GEN; FV (MIXED); DISC (ΔG/G spatial, weak) |
| 5 | **K = 2G** (ν_vac = 2/7) | **HAMILTONIAN** (law) — a **modulus ratio**; moduli are the textbook law-class quantity | substrate forces `K/G = f(ρ)`; the value 2/7 is GR-IMPORTED | value GR-imported (FV) — orthogonal axis: *imported* ≠ *texture*; it is still a modulus (law-class quantity-type), evidenced law-class by NH | **NH** (ringdown universality → moduli re-freeze identical); FV (GR-IMPORTED) |
| 6 | **the floor level ρ** (ρ_latent / DE floor) | **UNDETERMINED** — per-transition latent heat Hamiltonian; observed floor *density* texture-leaned | latent heat is a thermodynamic property of the Ax4 transition (law) | observed floor density = ongoing-casting-rate quantity (texture); ρ_latent numeric **absent** | GEN (latent-heat-of-genesis); floor-level unforced |
| 7 | **N = 3** | **UNDETERMINED — referent-flagged** | if spatial-dims / coordination: structural (Hamiltonian-candidate, ties to #10) | if generations: "three Cosserat sectors → three generations … **NOT derived from Axioms 1–4 alone**" (structural assumption) | referent ambiguous (see flag F-1) |
| 8 | **the baryon asymmetry** | **TEXTURE** (casting relic) | — | **topological inheritance from the primordial seed** (a single chirality choice at genesis) — NOT a defect census; KZ-scaling does **not** reach its magnitude (see D3) | **GEN** (doc-59 §5.4) |
| 9 | **Ω_freeze** | **TEXTURE** (the one observed global relic) | — | the frozen casting parameter itself; value **NOT derived** ("cited not derived here", parent-BH spin) — the confessed frozen accident; α/G values *trace to this* | GEN; `clm-a7cbqq` (value not derived) |
| 10 | **the srs/K4 choice itself** | **SPLIT:** crystal-class STRUCTURE **UNDETERMINED**; chirality HANDEDNESS **TEXTURE** | K4/srs `z=3` is **axiom-posited** (Ax1), not shown to be the unique ground state | structure: law-vs-polymorph unforced (martensitic alt live, D1c); handedness: right-handed `I4_132` **set by sign(Ω_freeze)** = texture | GEN (handedness); Ax1-posited (structure) |

### The one-line split (payload, restated)

- **PARTICLE PROPERTIES = LAW** (boundary-equilibrium): `m_e`, `ℓ_node`, `K=2G` (modulus), α-as-
  coupling *as observed*. These are the same for every electron / every re-frozen boundary,
  evidenced by indistinguishability (BE) and ringdown universality (NH).
- **PARTICLE POPULATIONS = HISTORY** (casting relics): `Ω_freeze`, the baryon asymmetry, the
  chirality handedness, the DE floor level. These are frozen at genesis and only statistically /
  historically derivable.
- **THE SEAM (UNDETERMINED):** the α/G **values** and `N=3`. The α/G values are law-*looking*
  (uniform) but texture-*rooted* (they inherit from the single frozen `u_0*/Ω_freeze`); law-vs-
  single-domain-texture is **degenerate** absent a Δα/α detection or a `𝒥_cosmic`-route pass. The
  framework's own falsification net already turns on exactly this independent `𝒥_cosmic` test
  (`omega-freeze-cosmic-grain-cascade.md` §Falsification): **pass = law/chord, fail = texture/echo.**

> **The α rescope, stated cleanly (the elegant part).** α's value is:
> 1. a **continuum-axiom echo** — PROVEN (Ax1–4 do not select it; every named lift-route
>    closed-negative, `form-deriving-value-importing.md` α-row);
> 2. **interatomic-law** — ARGUED, not proven (a pre-lattice interatomic potential *could* fix it,
>    but the corpus has no pre-lattice effective action — **doc-59 Flag G** names this as an open
>    axiomatic gap: "the pre-genesis plasma is, by definition, an Ax1-absent state … genuinely
>    outside Ax1–4's current scope");
> 3. **single-domain casting texture** — the three-route mechanism's reading (value inherits from the
>    frozen `u_0*`).
> Readings (2) and (3) are the two "un-echo" possibilities; the boundary data are consistent with
> **both**, and the discriminator (Δα/α spatial+temporal) is null. **The axioms specify the crystal
> class, not the interatomic potential** — so whether α is law-at-the-interatomic-level or
> texture-at-the-casting-level is exactly the gap Flag G names, and it is **UNDETERMINED**.

---

## Flags surfaced (flag-don't-fix — recorded, NOT resolved)

- **F-1 — `N=3` referent ambiguity.** The lane brief lists `N=3` without specifying which "3." The
  corpus carries at least three distinct `3`s: (a) **3 spatial dimensions**; (b) **3 generations**
  = 3 Cosserat sectors ("three Cosserat sectors → three generations … NOT derived from Axioms 1–4
  alone", [`full-derivation-chain.md:366`](../manuscript/ave-kb/common/full-derivation-chain.md),
  [`common/claim-quality.md:51`](../manuscript/ave-kb/common/claim-quality.md)); (c) the **`z=3` srs
  coordination** (the K4/srs choice, D2 #10). The memory register also flags the electron's *two
  homonymous 3s* (A1 dilatation mass vs Cosserat (2,3) winding). Classified UNDETERMINED pending a
  referent ruling; **not silently picked.**
- **F-2 — doc-59 "μ-only / EM wall" for the electron is SUPERSEDED by the three-impedance law.**
  doc-59 §8.5 frames the electron wall as an **EM** impedance step (`saturates μ only, Z→0, Γ=−1`,
  `:487-500`). Current canon
  ([`electron-bh-isomorphism.md:24-26,43`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md))
  re-assigns it to the **BULK channel** (`Z_bulk→0, Γ_bulk=−1`; the EM channel is Γ_EM=0 even at the
  electron), post-dating the three-impedance-law channel subscripts. D4c cites the **current** canon;
  doc-59's EM-wall wording is the older, superseded framing. Surfaced, not edited (doc-59 is archive;
  Rule-12 preserves it).
- **F-3 — the BH info-loss vs topological-retention tension (pre-existing, un-adjudicated).** The BH
  leaf asserts geometric information is "permanently erased"
  ([`black-holes-impedance-mismatch.md:17,20,24-26`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/black-holes-impedance-mismatch.md)),
  in tension with topological-retention (no-hair M–Q–J as a retained label) elsewhere. This lane's
  D2 uses the no-hair *exterior* (M–Q–J) as **NH** evidence for moduli-law-class; that use is
  agnostic to the *interior* info-loss question, which the corpus itself routes to the
  generative-cosmology lane (`research/2026-07-17_regime-iv-dissipation-audit.md:127`, F5).
  **Recorded so the D2 NH-evidence use is not read as taking a side on info loss.**
- **F-4 — "texture-class" is NOT the same axis as "VALUE-imported."** A quantity can be
  VALUE-imported yet Hamiltonian-class (K=2G: value GR-imported, but a *modulus* — law-class
  quantity-type, NH-evidenced). Conversely a FORM-derived structure can be texture-selected (the
  handedness). The two axes are **orthogonal**; the §0 "FORM=Hamiltonian / VALUE=texture" unification
  holds for the *calibration inputs* but the K=2G and handedness rows show it is not a blanket
  identity. Flagged so the unifying observation is not over-read.

---

## Provenance (verify-before-cite; two-method on load-bearing cites)

Every canon cite below was grep-confirmed against the branch tree at build (a second method — the
anchor-checker — is run on the diff before commit; see the PR).

**Canonical (KB) homes:**
- FORM/VALUE law: `manuscript/ave-kb/common/form-deriving-value-importing.md` (per-constant table
  `:83-90`; AC/DC carve `clm-acdc07`).
- Ω_freeze three-route + mechanism + falsification net:
  `manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md` (§1 three numbers; §2 mechanism;
  Falsification row); the frozen-accident confession `manuscript/ave-kb/common/claim-quality.md:476-499`
  (`clm-a7cbqq`, "value … cited not derived here").
- Substrate hysteresis / defect-freezing index: `manuscript/ave-kb/common/substrate-hysteresis-index.md`
  (§4; Level-1-reversible vs Level-2-memristive headline).
- Kernel catalog (Ω_freeze = water→ice, same Ax4 kernel): `manuscript/ave-kb/common/universal-saturation-kernel-catalog.md:260`.
- BH soft-mode / two-channel: `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/black-holes-impedance-mismatch.md`
  + `manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md:24-47`
  (G_shear→0; Γ_EM=0 SYM; Γ_shear=Γ_bulk=−1; electron bulk-TIR).
- LIGO ringdown match: `manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md:62`
  (−0.45% ω_R), `:64` (−0.47% τ).
- Schwinger / E-route birefringence (the lab coupon): `manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md`
  (`clm-pp3qwf`; HIBEF facility point `:156`).
- N=3 generations structural assumption: `manuscript/ave-kb/common/full-derivation-chain.md:366`.
- DE / latent floor: `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/cmb-thermal-attractor.md:10`,
  `.../index.md:21` (u_rad with latent floor).

**Research-doc homes (cited as research-level, not canon):**
- doc-59 (the AVE-native Kibble–Zurek + genesis + BH treatment; **archive**, Rule-12 preserved,
  maintained through 2026-07-19): `research/_archive/L3_electron_soliton/59_memristive_yield_crossing_derivation.md`.
- moving-front freeze-in: `research/2026-06-30_moving-front-freezein_result.md` +
  `research/2026-07-19_moving-front-freezein_landing-addendum.md`; banked negative
  `manuscript/ave-kb/common/genesis-chord-falsification-ledger.md:92-93`.
- Flag F fork status: `research/2026-07-20_jomega-derivation_result.md` §0.1/§0.3 (bin (iii)
  DEGENERATE; world-(c) excluded; scope routed to Grant) + `research/2026-07-19_flag-f-s-dynamics-derivation.md` §0.
- quantified soft-mode (C_44 collapse): `research/2026-07-04_saturated-elastic-tensor_result.md` §4.

**External `[import]` (observational — carried with citation, both sides where contested):**
- Electron indistinguishability — standard QM (no single citation; the universality of electron
  charge/mass/spin across all measurements).
- BH no-hair — GR (Israel / Carter / Robinson uniqueness theorems).
- Quasar Δα/α — Webb et al. dipole claim **and** the null re-analyses (VLT/UVES; Keck-vs-VLT
  systematic re-examinations). **Both sides carried; astronomy not adjudicated here.**
- Atomic-clock α-drift — optical-clock comparison bounds `|α̇/α| ≲ 10⁻¹⁸/yr`.
