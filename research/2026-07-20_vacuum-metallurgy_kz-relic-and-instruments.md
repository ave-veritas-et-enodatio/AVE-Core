# Vacuum Metallurgy — KZ Relic Prediction (D3) + Boundary Objects as Instruments (D4)

**Date:** 2026-07-20 · **Lane:** VACUUM-METALLURGY (mapping) · **Branch:** `research/vacuum-metallurgy` ·
**Parent:** [`2026-07-20_vacuum-metallurgy_mapping.md`](2026-07-20_vacuum-metallurgy_mapping.md) (frame,
D1 toolkit import, D2 classification, provenance). Read the parent's SECTOR/CLASS banner first — the
same consistency-class, fail-closed-UNDETERMINED discipline governs this companion.

> **CLASS.** CONSISTENCY-class relabeling. The **only** candidate *forward* content in this lane is
> (D3) the KZ relic-scaling FORM and (D4a) the ringdown soft-mode-systematics question — **both
> flagged candidate-only, both fail-closed at their decisive step.** No `clm-`, no chord, no new value.

---

## D3 — The Kibble–Zurek relic prediction (FORM; values calibration/import-tagged)

### D3.0 — The quench rate: does the genesis story carry its own casting parameters?

KZ needs one number the substrate must supply from *its own* genesis story: the **quench rate** —
the expansion/cooling rate at the crystallization epoch, `τ_quench ≡ (dr/dt)⁻¹` evaluated at the
yield crossing `r → r_crit`. Locate what the corpus actually says about *when* and *how* the lattice
froze:

- The relaxation time **is** derivable: `τ_relax = ℓ_node/c ≈ 1.288×10⁻²¹ s` (the causal-minimum
  state-change time, doc-59 §1 / `substrate-hysteresis-index.md` §2). ✅
- The quench *rate* is **NOT** pinned. doc-59 §5.4 says the crystallization wavefront "propagates
  outward at **sound speed in the plasma (possibly c, possibly slower depending on plasma
  properties)**" — i.e. the front speed, and therefore the local `dr/dt` at any comoving crossing, is
  **explicitly left open**. §8.1 has only the qualitative "expansion/cooling reduces `r` smoothly
  across volumes." There is **no epoch, no temperature, no expansion rate** attached to the freeze.

> **★ FINDING D3-1 (the deliverable's first hard result — fail-closed).** **The genesis story lacks
> its own casting parameters.** The corpus can compute `τ_relax` (the *anneal* timescale) but not
> `τ_quench` (the *cast* timescale) — so the single dimensionless ratio KZ needs,
> `τ_quench/τ_relax`, is **undefined from within the axioms**. This is not an oversight to patch; it
> is **structural**, and the corpus already names *why*: **doc-59 Flag G** — "the pre-genesis plasma
> is, by definition, an Ax1-absent state … What axioms govern the plasma? Is there a pre-lattice
> effective action? This is genuinely outside Ax1–4's current scope" (`:291`, `:678`). **No
> pre-lattice effective action ⇒ no equation of motion for `r(t)` before the freeze ⇒ no quench
> rate.** The casting parameters live in the Ax0 layer the framework has not built. Fail-closed:
> **`τ_quench` UNDETERMINED (Ax0-gap, Flag G).**

### D3.1 — The KZ defect-density FORM (and why the exponent is unforced)

The standard KZ form for the frozen-in defect density:

```
n_defect  ~  ξ_KZ^(−D)        (D = spatial dimension of the defect network)
ξ_KZ      ~  ℓ_node · (τ_quench / τ_relax)^(ν / (1 + νz))
```

with `ν`, `z` the correlation-length and dynamic critical exponents. The **FORM** is standard and
imports as a candidate translation-row. The **exponent** `ν/(1+νz)` does **not** import clean:

- Its value is set by the **order and dynamics of the transition** — a *second-order* (continuous)
  transition gives the KZ power law; a *first-order* (discontinuous / nucleation-and-growth)
  transition gives **different** scaling (often linear-in-rate, set by nucleation kinetics, not by a
  diverging `ξ`).
- doc-59's own reading is **first-order**: "defect density from cool-from-above scales **LINEARLY**
  with the volumetric yield-crossing rate … **distinctly different from Kibble–Zurek power-law**
  `τ_Q^{-ν/(νz+1)}` because **Ax4 is a first-order transition, not second-order**" (`:650`,
  `P_phase5_cooling_rate_density`).
- **BUT** the first-order LINEAR reading rests on the first-order relaxation ODE (doc-59 Eq 2.1),
  which the J(ω) result shows is **unlicensed at `ωτ ~ 1`**, with the near-yield dynamics order left
  **DEGENERATE / UNDETERMINED** (Flag F: world-(c) resistor excluded; world-(a) lossless-reactive vs
  world-(b) transduction unforced; scope routed to Grant —
  [`2026-07-20_jomega-derivation_result.md`](2026-07-20_jomega-derivation_result.md) §0.1/§0.3).

> **★ FINDING D3-2 (fail-closed).** The KZ **relic-density exponent is UNFORCED.** The vacuum's
> defect-density scaling is **linear-in-rate IF the near-yield transition is first-order** (doc-59)
> and **KZ-power-law IF it is second-order/reactive** — and **which one holds is exactly the OPEN
> Flag F fork.** The corpus even carries *both* regimes side-by-side in doc-59's own crossover table
> (slow-cooling linear ↔ fast-cooling KZ-like, crossover at `τ_cool ≈ ξ_thermal/c`, `:386-390`). So
> the KZ FORM imports as a **candidate**, but its decisive numerical content (the exponent) is
> **doubly gated**: on `τ_quench` (D3-1, Ax0-gap) and on the transition order (Flag F). **Candidate
> forward content, fail-closed at the exponent.**

### D3.2 — The observed relic census: what ARE the vacuum's KZ-class defects?

KZ defects are **not** the equilibrium particles (electrons are boundary-equilibrium precipitates,
D2 #1 / D4c — law-class, not casting relics). The KZ-class relics are the **topological defects of
the genesis transition** — the domain walls / strings / monopole-class objects. Census:

- **Domain walls (chirality walls) — an OBSERVED-ABSENCE CONSTRAINT.** doc-59 §5.3 predicts chirality
  domain walls at `+h_local`/`−h_local` interfaces, with a density that crosses over from linear to
  KZ-like as cooling sharpens (`:382-394`). **Observationally, cosmic domain walls are absent**
  `[import — a wall network would over-close the universe / imprint the CMB; standard cosmology
  excludes stable domain walls above a very low tension]`. What this **excludes**: it excludes a
  *multi-domain* fast-quench genesis (many independently-seeded chirality domains with walls between
  them). It is **consistent with — indeed evidence FOR — the single-domain casting** of D2: doc-59
  §5.4's one-seed genesis (the whole observable universe inherits one chirality from one seed,
  wavefront now beyond the horizon) produces **no walls inside the horizon**. So the domain-wall
  absence is a genuine constraint, and it points the same way as the D2 seam: **single-domain
  casting** (texture correlation length > horizon).
- **Strings / monopole-class — not populated in-corpus.** The framework's genesis story is a
  *chirality* (Z₂-handedness) transition + a topological-*inheritance* baryon story, not a
  gauge-symmetry-breaking cascade — so it has no string or monopole prediction to census. Absence of
  a prediction, not a null.
- **Ω_freeze — the ONE observed global relic.** The frozen cosmic spin is the single KZ-class relic
  the framework actually banks as observed (via the CMB axis-of-evil pin, `omega-freeze-cosmic-grain-cascade.md`
  §1). It is texture-class (D2 #9). It is a *single* global quantity, not a *density* — consistent
  with single-domain casting (one frozen `Ω̂`, not a defect network).

### D3.3 — Can KZ-class reasoning reach the baryon asymmetry's order of magnitude? (honest attempt → fail-closed)

The candidate relic NUMBER is `η_B ~ 6×10⁻¹⁰` `[import — baryon-to-photon ratio, CMB + BBN]`. Attempt
the scaling honestly:

```
η_B  ~  n_defect / n_γ  ~  (ξ_KZ^{−3}) / (ρ_latent / k_B T_freeze)
```

Every factor on the right is **missing or unforced**:

1. `ξ_KZ` needs `τ_quench` — **UNDETERMINED** (Finding D3-1, Ax0-gap).
2. The exponent in `ξ_KZ` is **UNFORCED** (Finding D3-2, Flag F).
3. `n_γ` needs `ρ_latent` (the latent-heat floor density) — **numeric ABSENT** (D2 #6; the ρ_latent
   prerequisite is a standing gap, `_orchestration/index.md` F6 tier record).
4. **Wrong-instrument caveat (the decisive one).** doc-59 §5.4 says the baryon asymmetry is **NOT a
   defect density at all** — it is a **single-seed topological inheritance** (the whole domain is
   A-sublattice matter; the antimatter is beyond the horizon / in other-seed domains). A
   *single-domain* relic has no defect *census* to scale; `η_B`'s smallness is then reframed as
   "precipitated matter per volume ÷ latent-heat photons per volume," which is a **latent-heat
   ledger**, not a KZ defect count.

> **★ FINDING D3-3 (fail-closed, three-fold).** **KZ-class reasoning cannot reach `η_B`'s order of
> magnitude.** It fails for three *independent* reasons — a missing quench rate (D3-1), an unforced
> exponent (D3-2), and a wrong-instrument mismatch (doc-59 makes `η_B` a single-domain inheritance,
> not a KZ defect density). The baryon asymmetry is **texture-class (D2 #8) but of the single-domain
> / casting-inheritance kind**, not the KZ defect-density kind. The honest verdict is **not** "KZ
> predicts `η_B`"; it is "the framework's own genesis story routes `η_B` *away* from the KZ
> defect-census channel into the single-seed-inheritance channel, whose magnitude is un-computed
> (Ax0-gap + ρ_latent-gap)." **Mapping unforced ⇒ fail-closed UNDETERMINED.**

### D3 summary

| KZ deliverable | Status |
|---|---|
| Quench rate from the genesis story | **UNDETERMINED** — genesis lacks its own casting parameters (Ax0-gap, doc-59 Flag G) — **Finding D3-1** |
| Defect-density FORM | imports as candidate translation-row |
| Defect-density EXPONENT | **UNFORCED** — first-order-linear vs second-order-KZ = the OPEN Flag F fork — **Finding D3-2** |
| Domain-wall relic | observational ABSENCE = constraint → excludes multi-domain quench, evidence FOR single-domain casting |
| Ω_freeze relic | the one observed global relic (texture, single quantity not a density) |
| Baryon asymmetry via KZ | **UNREACHABLE** — 3 independent gaps; single-domain-inheritance, not KZ defect census — **Finding D3-3** |

---

## D4 — Boundary objects as instruments (what each Γ-boundary gives the classification)

The observable Γ-boundaries are the classification's hard data. Each is a *different reflectometer*
reading a *different channel* of the same medium at the same phase boundary.

### D4a — The black hole = `G_shear → 0` SOFT-MODE transition; the ringdown reread as soft-mode spectroscopy

A structural (displacive) transition's textbook signature is a **soft mode** — a vibrational mode
whose restoring force (a modulus) collapses to zero at the transition. The framework's BH interior
**is** exactly this: at `r_sat = 7 GM/c² = 3.5 r_s` the lattice reaches its elastic limit and the
**shear modulus `G_shear → 0`** (topology melts), so the shear/GW group velocity `c_shear = c√S → 0`
([`electron-bh-isomorphism.md:28-36`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md)).
The modulus collapse is now **quantified**: the srs Cauchy shear stiffness `C_44` collapses
`0.17661` (loaded-cold) → `0.02536` (at the `ν=2/7` crossing) → `4×10⁻⁵` as `A→1` — "the lattice
goes **floppy near the yield wall**" ([`2026-07-04_saturated-elastic-tensor_result.md`](2026-07-04_saturated-elastic-tensor_result.md)
§4, PR #521; quoted in `electron-bh-isomorphism.md:38`). **Modulus collapse = the soft-mode
signature, node-up.**

The framework already banks a **ringdown match** off this boundary: `−0.45%` mean `ω_R` and `−0.47%`
mean `τ` across 3 LIGO events, zero free parameters, with `τ` **outperforming** standard GR Kerr QNM
([`ave-merger-ringdown-eigenvalue.md:62,64`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md)).

> **🔴 CORRECTION (2026-07-20, per AVE-Core PR #774 kerr-table-canon-correction; surfaced by that lane's review, finding 2).** The banked `−0.45%`/`−0.47%`/"`τ` outperforms GR" ringdown match quoted above is **RETRACTED as a compensating-error artifact** (corrupt Kerr QNM reference table wrong at spin by −9 to −27% × source-vs-detector frame mixing). Honest state: **AVE-v2 sits −9.5% mean BELOW true Kerr** (frame-independent dimensionless ratio), and the τ chain rides a separately-corrupt ω_I table — the "outperforms GR" contrast does not survive. The cross-ref `:62,64` now points **into the retraction banner** (the AVE-side spin-mapping fork is additionally REOPENED — see PR #774 § FORK-REOPEN). **What this does to the D4a reread below:** the soft-mode *relabeling* survives as a framing, but its **AVE-specific corroboration leg (the sub-percent match) is gone** — the GR-observed no-hair / ringdown *universality* is an `[import — GR]` and is unaffected, but AVE no longer supplies a sub-percent match to reread. Treat the D4a soft-mode ringdown systematics below as **candidate-forward only** (as already tagged), not resting on a banked AVE match.

> **The reread (consistency-class relabeling, with real content).** The banked ringdown match is
> **shear-channel spectroscopy of a soft-mode transition** — the quasinormal modes are the shear
> waves ringing off the `G_shear → 0 / c_shear → 0` boundary. This is a *re-labeling* of an existing
> banked result in the soft-mode register (no new number), but it **organizes** the ringdown in a way
> generic-GR Kerr-QNM fitting does not.

> **★ CANDIDATE FORWARD CONTENT (D4a — surface, do NOT derive fully).** What would the soft-mode
> toolkit predict about ringdown **systematics** that generic Kerr-QNM fitting treats as free?
> 1. **Mode-ratio locking.** The saturated-elastic-tensor result found the **dimensionless ratios
>    freeze** (`ν`, Zener, `K/G` are degree-0 in the bond stiffnesses → unshifted by the saturation
>    magnitude) while the **absolute** moduli collapse — "a soft region with **locked proportions**"
>    (`:38`). Soft-mode prediction: the ringdown **overtone/mode-frequency RATIOS** should be set by
>    the frozen elastic ratios (fixed), while the **absolute** frequencies scale with `√C_44` — a
>    *ratio-locked* spectrum, not the Kerr geometric spectrum.
> 2. **Critical-slowing damping.** Near a soft-mode transition the mode frequency softens as
>    `ω ∝ √(modulus)` and the damping tracks the approach to the transition (critical slowing down).
>    The framework already reads the ringdown `Q`/`τ` as a **K4-lattice-impedance** property (rigid
>    Cosserat skeleton, invariant across cavity-radius refinements, `ave-merger-ringdown-eigenvalue.md:64`).
>    Soft-mode prediction: a specific `Q(approach-to-yield)` / `ω ∝ √C_44` near-boundary softening
>    systematic — testable against the high-`a*` LIGO catalog (where the corpus already notes
>    divergence onset at `a* ≥ 0.90`, the Option-B threshold).
>
> **Both are candidate-only** — surfaced for a follow-on lane, not derived here. They are the lane's
> second (and last) candidate forward object, alongside the D3 KZ FORM.

### D4b — The two-channel reflectometry reading (EM absorbed vs shear rings)

The BH is an **impedance-ratio measurement at the transition**, and it reads *differently in each
channel*:

- **EM channel: `Γ_EM = 0` — ABSORBED ("black").** Under Symmetric Gravity both `μ'` and `ε'` scale
  with `n(r)` together, so `Z_EM = √(μ'/ε') = Z₀` is **invariant at all radii** — no EM impedance
  step, no EM reflection. EM crosses the horizon without reflection and thermalizes inside (doc-59
  §8.5; [`electron-bh-isomorphism.md:24`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md);
  [`black-holes-impedance-mismatch.md`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/black-holes-impedance-mismatch.md)).
  **This is why a black hole is black, not a mirror** — the standard puzzle, resolved by the
  *symmetric* saturation.
- **Shear/bulk channel: `Γ_shear = Γ_bulk = −1` — RINGS.** `G_shear → 0` and `c_bulk → 0` collapse
  `Z_shear = ρ c_shear → 0`, a shear-channel impedance collapse: the saturated interior is a
  **perfect reflector for shear waves** (`electron-bh-isomorphism.md:36,43`). The shear channel
  **rings** — and that ring is the observed ringdown (D4a).

> The **two-channel contrast is the instrument**: same boundary, `Γ_EM = 0` (absorb) vs
> `Γ_shear = −1` (reflect). The picture-primer home for this BH-mechanism distinction is the
> trampoline framework ([`trampoline-framework.md`](../manuscript/ave-kb/common/trampoline-framework.md),
> now on main); the quantitative channel-split home is `electron-bh-isomorphism.md:24-47`.

### D4c — The electron wall = equilibrium precipitate (Gibbs–Thomson-class)

The electron is a **boundary-equilibrium precipitate**: a self-trapped `0₁`-unknot confined at
`ℓ_node ≈ 3.86×10⁻¹³ m` by a **bulk-channel** total-internal-reflection wall
(`Z_bulk → 0, Γ_bulk = −1`; current canon `electron-bh-isomorphism.md:26,43` — **not** the older
"EM/μ-only" wall of doc-59 §8.5, see parent Flag F-2). Its wall position is set by a
**boundary-energy-vs-bulk balance** — a Gibbs–Thomson-class precipitate condition (the balance locus
`R* ≈ 1.6 ℓ_node`, `hollow-vortex-binding.md:49`, cited via the tij-x44b charter).

> **What it gives the classification.** A Gibbs–Thomson precipitate size is set by the **interaction
> Hamiltonian** (surface tension vs bulk chemical potential), *not* by the casting history — so
> `m_e` (via `ℓ_node`) is a **law-class boundary-equilibrium quantity** (D2 #1). And because the
> precipitate condition is the *same* for every electron, **electron indistinguishability follows
> from the boundary-equilibrium condition** — closing the (i)→law-class inference of D2. This is the
> most physically evocative datum (n.b. its home leaf self-grades R* as SOFT-CONSISTENCY — m_e's law-class rests on the definitional anchor + indistinguishability, not on R*) in the classification: it is *why* particle properties are LAW.

### D4d — Schwinger = the lab coupon (controlled approach to the same wall)

The Schwinger limit is the **controlled, benchtop approach to the same yield wall** the electron and
BH reach uncontrolled — a *coupon test* of the medium's material limit. In AVE the accessible
readout is the **E-route vacuum birefringence coefficient** (`clm-pp3qwf`): a static-E bias loads the
`V`-keyed varactor toward `V_yield`, and the probe beam's differential index reads a **tree-level**
coefficient the QED vacuum only sources at `α²`-loop (Euler–Heisenberg) —
`δn_AVE/δn_QED = 3.75π/α² ≈ 2.2×10⁵` ([`vacuum-birefringence-e4.md`](../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md);
HIBEF facility point `:156`).

> **Pointer only (not this lane's object).** The E-route / HIBEF territory is the framework's one
> bankable forward *falsifier*; here it is the **coupon** that samples the classification's phase
> boundary in the lab. Honest split (from the leaf): the **CHORD** is that the vacuum *saturates at
> all* (a tree-level structure QED lacks); the **MAGNITUDE** `2.2×10⁵` is an **α-echo** (rides
> `α⁻²`; QED's coefficient is equally α-rooted). The coupon tests the *existence* of the wall (a
> FORM/law question), **not** its imported magnitude.

### D4 summary — the instrument ledger

| Instrument | Channel read | What it gives the classification |
|---|---|---|
| **Black hole** (re-melt → re-freeze) | shear/bulk `Γ=−1` (rings) + EM `Γ=0` (absorbs) | **NH**: moduli re-freeze identical ⇒ `K=2G`, moduli are **law-class** (D2 #5); soft-mode reread of the ringdown (D4a candidate) |
| **Electron wall** (Gibbs–Thomson precipitate) | bulk `Γ_bulk=−1` | **BE**: boundary-equilibrium precipitate ⇒ `m_e`, α-as-coupling **law-class** (D2 #1); grounds indistinguishability (D4c) |
| **Schwinger wall** (lab coupon) | E-route varactor near `V_yield` | tests wall *existence* (FORM/law), not magnitude (echo); the controlled sample of the phase boundary |
| **Ω_freeze / CMB axis** (the frozen cast) | cosmic-boundary winding `𝒥_cosmic` | **GEN**: the one observed global **texture** relic; the independent test that decides the D2 seam (pass=law, fail=texture) |
