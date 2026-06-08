# Cosmic Operating-Point Dilution-Trajectory — Hypothesis Scoping + Corpus Consistency/Tension Map

**Date:** 2026-06-07
**Branch:** `analysis/2026-06-07-cosmic-dilution-trajectory` (off `main` @ `63e6671a`)
**Type:** READ-heavy scoping research doc. NO engine code. NO corpus-leaf edits.
**Lane:** implementer (scoping deliverable; auditor lands any manual/matrix entries)
**Discipline fired:** `ave-prereg` (mapping-not-derivation path), `verify-before-cite` (every leaf grepped/read), `consistency-vs-emergence` (classification), `substrate-native-check` (imported-analogy check), `ave-discrimination-check` (α-drift vs static-relic), `flag-don't-fix` (tensions surfaced, not resolved)

> **Status of this doc:** SCOPING ONLY. It maps Grant's 2026-06-07 dilution-trajectory hypothesis against canonical corpus content, classifies it, and surfaces the load-bearing fork for Grant. It does **not** adjudicate the fork, edit any canonical leaf, or propose a new axiom. Per flag-don't-fix, tensions are surfaced with both file paths + verbatim content; none are silently reconciled.

---

## 0 — The hypothesis (Grant, 2026-06-07), verbatim restatement

**Core claim.** The cosmic operating point `A` (per-node saturation strain) is a **DILUTION TRAJECTORY DOWN** the Axiom-4 kernel `S(A) = √(1−A²)`. Early universe = FEW lattice nodes/springs → a fixed genesis load (cosmic rotation `Ω_freeze`, the chirality-stamping perturbation) concentrated over few springs → **HIGH per-node `A` (near yield, `A→1`, `S→0`, saturation / topological-reorganization regime)**. As the lattice crystallizes/expands (adds nodes), the fixed load **dilutes over growing N → `A` drops** → late universe is **LOW `A` (linear, `S→1`, Maxwell/Newtonian)**. The universe slides *down* `S(A)`.

**Load-bearing assumption (Grant's own flag).** New springs are added **RELAXED** at the crystallization front (so a fixed early load dilutes). *If each new cell is pre-loaded, `A` is intensive and there is no slide.*

**Three consequences to scope:**
1. **Early-saturation genesis epoch** — `A→1` early = where genesis / particle-formation / chirality-stamping happened (universal saturation `S→0`, "must reorganize topologically"). Explains *why* genesis was early AND why Fork A is hard to reproduce locally now.
2. **Chirality dilution-lock** — handedness stamped at early high-`A` (strong `Ω_freeze` driver); dilution drops `A` to linear → stamp frozen (the driver that could overwrite it diluted away). Mechanism for "expansion holds chirality."
3. **α-drift** — α projects from `A`/`u₀*` (Class-E joint constraint) → α drifted as `A` diluted; direction per the δ_strain α-vs-T mechanism.

---

## 1 — TL;DR verdict (the six checks + headline)

| # | Scoping check | Verdict |
|---|---|---|
| 1 | STATIC or DYNAMIC `u₀*`? | **The PROCESS is DYNAMIC; the operating-point VALUE `u₀* ≈ 0.187` is held FIXED at the K4 magic-angle.** Corpus phrase: "ongoing operating-point **process at** `u₀*`" (`op14-cosmic-horizon-profile.md:76`, `cosmic-epsilon-de-projection-scoping.md:9`). Dynamic crystallization that **maintains** the fixed point — homeostasis, not a slide. |
| 2 | Trampoline — dilution (extensive) or intensive strain? | **INTENSIVE.** `u₀ = (L₀−d)/d = ρΩ_freeze²r_node²/2K₀` is a per-bond rest-length-excess set locally at freeze-in (`trampoline-framework.md:103`); `k₀` is "intrinsic … not freeze-in dependent" (`:109`); only the **bulk** tension `T_EM` is extensive (`:110`). `S(A)` acts per-bond on `A² = ε²+κ²+V²`. **Tension with the dilution premise**, which needs `A` extensive. |
| 3 | "New springs added relaxed" — consistent with crystallization front? | **TENSION.** Corpus crystallization preserves **`∂_t ρ_n = 0`** (constant node density, `lattice-genesis-hubble-tension.md:12`) and the front is held **near saturation** `A²≈1` by latent-heat balance (`op14-cosmic-horizon-profile.md:68`). New nodes crystallize *into* homeostasis at `u₀*`, not relaxed-and-diluting. |
| 4 | **α-drift vs SYM-gravity α-invariance — tension or different axes?** | **DIFFERENT AXES. NOT a contradiction** — and the corpus already holds both simultaneously and reconciles them explicitly. SYM-invariance = gravitational-**potential** axis (`μ,ε` scale together → `Z₀` invariant → Δα/α null at different potentials, clm-3zz0f6). α-drift = cosmic-**temperature/time** axis via **ASYM** SYM-breaking (clm-hp7nlm §3). The working hypothesis in the brief is confirmed verbatim. **Caveat:** the corpus's α-drift axis is *thermal* (δ_strain), which is a **different mechanism** than the proposed *dilution* (operating-point-slide) — see §3.3. |
| 5 | Early-`A→1` epoch ↔ hot/dense early universe? Genesis redshift derivable? | **PARTIAL / NO.** Corpus genesis = one-shot K4 crystallization (A-034 Row 14 SYM*) directly into `u₀*`; the early high-energy state is the **pre-lattice plasma**, not a high-`A` lattice that then dilutes. No A-slide ⇒ **no genesis-redshift "knee" is derivable** from the dilution mechanism. A redshift-dependent α *does* exist in corpus but via the thermal `δ_strain(T) ∝ T` running (clm-hp7nlm §6.1), not dilution. |
| 6 | Derives a number, or lens-only? | **LENS-ONLY.** No new number falls out. The nearest corpus number — the α-drift magnitude `δ_strain ≈ 2.225×10⁻⁶` — was **CLOSED NEGATIVE as a derivation** (FT-1, 2026-05-31): undershoots by ~31 OOM, generic-thermal not AVE-distinct; it is a **definitional residual** `1 − CODATA/α_cold`. The α-vs-T *sign* is derived; the magnitude, genesis redshift, and dilution rate `dA/dN` are not. |

**Headline (check 4), one line:** the α-drift and SYM-gravity α-invariance are **not in tension** — they are orthogonal mechanism classes (ASYM temperature/time vs SYM gravitational-potential), and `delta-strain-cosmic-tcc.md` §3 already states both and reconciles them. The genuine tension is **elsewhere**: the dilution *premise itself* (a sliding operating point) vs three canonical pins — magic-angle `u₀*` fixity, `∂_t ρ_n = 0` homeostasis, and intensive per-bond `u₀`.

**Honest classification:** **consistency-class lens** (a re-framing over canonical Class-E operating-point + Class-B δ_strain content) that **currently sits in tension** with the magic-angle/homeostasis pins. It derives no number. Whether the lens is *admissible* turns on one fork Grant must collapse (§8): **are crystallization-front springs added slack (dilution allowed) or pre-loaded at `u₀*` (intensive, no slide)?**

## 2 — Corpus map (verified leaves, verbatim)

### 2.1 The operating point `u₀*` — what it is, and that it is FIXED

`omega-freeze-cosmic-grain-cascade.md:34` (verbatim):
> *"All three derive from a single substrate operating point `u₀* ≈ 0.187` (bond over-bracing at the K4 magic-angle `K(u₀*) = 2 G(u₀*)`). The framework's sharpest empirical commitment is that all three routes must converge on this same `u₀*` … or the single-cosmological-parameter framework is falsified."*

`omega-freeze-cosmic-grain-cascade.md:44-47` (verbatim): at lattice genesis, "Bond rest lengths lock at the rotating-frame equilibrium → `u₀*` over-bracing … Cosmic spin is locked into the substrate as both bond over-bracing `u₀*` AND the global chirality direction. **Survives forever** as the cosmological initial condition."

`trampoline-framework.md:161` (verbatim): *"The magic-angle condition forces `u₀ = u₀*` for the substrate to exist self-consistently (`K = 2G`)."*

→ **The operating-point VALUE is pinned at the magic angle and "survives forever."** Letting it slide *away* from `u₀*` (the dilution premise) means leaving the `K = 2G` self-consistency the substrate requires to exist.

### 2.2 STATIC-vs-DYNAMIC — the process is dynamic, the value is fixed

`cosmic-epsilon-de-projection-scoping.md:9` (Grant adjudication Q1, verbatim):
> *"DE static vs dynamic? → **DYNAMIC** … AVE's DE is the crystallization happening NOW at the cosmic horizon — substrate still phase-transitioning, latent heat still being released. **Class E framing already encodes this as ongoing operating-point process at `u₀*`.**"*

`op14-cosmic-horizon-profile.md:76` re-states it verbatim and adds the crystallization-front condition `op14-cosmic-horizon-profile.md:68`: at the horizon `A²` is *"Maintained near `A² = 1` by latent-heat balance."*

→ The answer to check 1 is **DYNAMIC PROCESS / FIXED VALUE.** Crystallization is ongoing (dynamic) but it is an *"ongoing operating-point process **at** `u₀*`"* — a steady-state that maintains the operating point, with the saturation **boundary** (the `Γ=−1` horizon wall) at `A²≈1` and the **bulk interior** at `u₀*≈0.187`. This is homeostasis, not the monotonic slide the hypothesis proposes.

### 2.3 Extensive vs intensive — the trampoline's own distinction

`trampoline-framework.md:103` (verbatim): `u₀ = (L₀ − d)/d = ρ Ω_freeze² r_node² / 2K₀` — a **per-bond** rest-length excess, set by the **local** rotation rate at the moment that bond crystallizes.

`trampoline-framework.md:109-110` (verbatim) makes the extensive/intensive split explicit:
> *"Fundamental bond stiffness `k₀` is intrinsic to the LC tank — set by Axiom 1 substrate structure. **Not freeze-in dependent.** … Bulk substrate tension `T_EM` is Machian — bulk integrated bond-tension density over the entire lattice. Depends on `u₀`: `T_EM = n_bonds · k₀ · d · u₀ · (K4 geometric factor)`."*

`trampoline-framework.md:374-388`: the saturation amplitude is per-bond Pythagorean `A² = ε² + κ² + V²`, and `S(A) = √(1−A²)` is "how much further [the bond] can be deformed before reaching the `A = 1` wall." Axiom-4 (KB CLAUDE.md INVARIANT-S2): `A` is a **per-node** state ("the field across ONE cell `ℓ_node`").

→ The corpus treats the operating-point strain (`u₀`, `A`) as **INTENSIVE** (per-bond, set locally at freeze-in); only `T_EM` is extensive. The dilution premise needs the *operating point itself* to be a fixed total quantity divided over `N` springs — i.e., extensive. **This is the intensive-vs-extensive fork, in the corpus's own words.**

### 2.4 Crystallization front preserves constant node density (homeostasis, not dilution)

`lattice-genesis-hubble-tension.md:10,12` (verbatim):
> *"metric expansion is modelled as the discrete, real-time **crystallisation of new electromagnetic nodes** … To preserve the invariant optical density of the condensate globally (`∂_t ρ_n = 0`), the Eulerian continuity equation dictates the discrete generative source term must match the macroscopic volumetric expansion divergence. … the Hubble Constant … is … the **LC Crystallisation Rate** required to maintain the vacuum's structural impedance."*

→ The corpus's expansion mechanism **adds nodes specifically to HOLD `ρ_n` constant** as volume grows. "Fixed load diluting over growing `N`" is the opposite of `∂_t ρ_n = 0`. `:25` even frames the early/late difference (Hubble tension) as a *measurement artefact across thermodynamic regimes* with the generation rate "asymptot[ing] to this geometric bound" — again homeostasis, not a slide.

### 2.5 The α-drift mechanism (δ_strain) — sign-derived, magnitude closed-negative

`delta-strain-cosmic-tcc.md:67-71` (verbatim) reconciles SYM-invariance and the α-drift IN THE SAME LEAF:
> *"Under canonical INVARIANT-S2 SYM scaling (both ε and μ scale identically by `nS`), α is **exactly invariant** per canonical clm-3zz0f6 … For thermal loading at `T_CMB`, however, the asymmetric thermal occupation of E vs B modes induces **asymmetric SYM-breaking**"* → α drifts.

`delta-strain-cosmic-tcc.md:15` (verbatim) on the magnitude:
> *"the candidate quantitative substrate-statistical-mechanics derivation … was **ATTEMPTED and CLOSED NEGATIVE** by FT-1 (2026-05-31): the E-mode Bose-Einstein occupation undershoots `η_ε` by **~31 OOM** … AND is **generic-thermal, not AVE-distinct** … δ_strain's magnitude is a **definitional residual** (`1 − CODATA/α_cold`) … the thermal mechanism holds in **sign only**."*

`delta-strain-cosmic-tcc.md:24` (sign, verbatim): *"E-mode jiggling counter-charges substrate ⇒ `ε_eff` decreases ⇒ `α_eff > α_0` ⇒ CODATA `α⁻¹ <` cold-lattice `α⁻¹` ✓ matches observation."*

### 2.6 The cold-lattice α is a GEOMETRIC identification (golden torus), not a function of `A`

`delta-strain-cosmic-tcc.md:65` + `:15` (verbatim): cold-lattice `α⁻¹_ideal = 4π³ + π² + π` is "a **named geometric identification**" (golden-torus bijection, 2026-06-04). The Class-E "α derives from `u₀*`" link (`omega-freeze:49`: "`u₀*` sets α via the Golden Torus") runs **through the magic-angle**: `u₀*` is the over-bracing that realizes `K = 2G`, the operating point at which the golden-torus geometry obtains. → α changes only if the *geometry* changes, i.e., only if `u₀*` leaves the magic angle. This is load-bearing for §3.3 and §5.

## 3 — Headline consistency check: α-drift vs SYM-gravity α-invariance

### 3.1 Verdict: DIFFERENT AXES, not a contradiction — and the corpus already says so

The brief's working hypothesis ("SYM-invariance is the gravitational-POTENTIAL axis; the dilution drift is the cosmic-TEMPERATURE/time axis; different mechanisms → maybe NOT a contradiction") is **confirmed verbatim** by canonical content. The two live in the corpus's explicit **SYM-vs-ASYM mechanism-class taxonomy** (KB CLAUDE.md INVARIANT-S2):

| Axis | Mechanism class | Scaling | α | Canonical source |
|---|---|---|---|---|
| Gravitational **potential** (multi-species clocks at different `Φ`) | **SYM** | `μ, ε` scale together → `Z₀` invariant | **EXACTLY invariant**; Δα/α null | `alpha-invariance-symmetric-gravity.md` clm-3zz0f6 (solidity 0.85) |
| Cosmic **temperature / time** (thermal bath at `T_CMB`) | **ASYM** (Cosserat-Curie thermal-mode-population) | `ε` thermally modulated, `μ` frozen (B-mode mass-gap) → SYM broken | **drifts** (sign-derived) | `delta-strain-cosmic-tcc.md` clm-hp7nlm |
| Strong-field large-amplitude saturation | ASYM | `μ, ε` scale by different factors | drifts | INVARIANT-S2 / clm-8nkvwy |

`alpha-invariance-symmetric-gravity.md:24` (verbatim): *"Multi-species clock comparisons at different gravitational potentials predict a **null result** for Δα/α, consistent with all current experimental bounds."* → This is a statement about the **potential** axis only. It says nothing about, and does not forbid, a temperature/time-axis drift. There is **no contradiction** to surface: the same corpus that asserts SYM-invariance also asserts the ASYM α-drift, and `delta-strain-cosmic-tcc.md:67-71` reconciles them in one paragraph.

### 3.2 The reconciliation is structural (Z₀-invariance is the discriminator)

The mechanism is clean: α-invariance holds **iff** `μ` and `ε` scale together (`Z₀ = √(μ/ε)` invariant). Gravity (SYM) does exactly that → α invariant. Anything that scales `ε` and `μ` *asymmetrically* (thermal E-vs-B occupation; strong-field; …) breaks it → α drifts. SYM-invariance and ASYM-drift are not competitors; they are the two branches of one `Z₀`-symmetry condition. (Note: the corpus also warns this is exactly where the `c_EM` vs `c_shear` category error bites — INVARIANT-S2 — but that pitfall is orthogonal to the dilution hypothesis.)

### 3.3 BUT — the dilution α-drift is a THIRD mechanism, not the corpus's thermal one (flag, do not resolve)

The brief's consequence #3 says α "drifted as `A` diluted; **direction per the δ_strain α-vs-T mechanism**." This **conflates two physically distinct mechanisms**:

- **Corpus α-drift (thermal, δ_strain):** at *fixed* `u₀*`, the thermal **E-mode population** modulates `ε` asymmetrically. The lattice operating point does not move; the *temperature* does.
- **Proposed α-drift (dilution):** the *operating point `u₀*` itself* slides → the golden-torus geometry that sets `α_cold` changes → α drifts. The temperature need not change at all.

These are not the same axis with a borrowed sign; they are different physics. Two specific frictions the dilution route inherits that the thermal route does not:

1. **`α_cold` is golden-torus geometry, not a smooth function of `A`** (§2.6). For a sliding `u₀*` to move α, the slide must change `K=2G` → change the torus geometry. But the magic-angle pin (`trampoline-framework.md:161`) says `u₀*` *cannot* leave `K=2G` without the substrate ceasing to be self-consistent. So the dilution route must either (a) keep `u₀*` at magic-angle (then α does not drift via dilution — only via the thermal δ_strain channel), or (b) let `u₀*` leave magic-angle (then it is no longer the canonical operating point, and `K=2G` breaks).
2. **The sign is not automatically inherited.** The δ_strain sign comes from a specific micro-mechanism (E-mode jiggling lowers `ε_eff`, `delta-strain:24`). A dilution-driven change in `u₀*` would change α through the *geometry/`K=2G`* channel, whose sign is a separate derivation — it is **not** given by the thermal sign check.

**Net:** the headline tension (α-drift vs SYM-invariance) is **resolved by the corpus as different axes** — no action needed there. The *real* open item is that the dilution hypothesis's α-drift is a **new, third α-mechanism** that is (i) underspecified in how `u₀*`-slide propagates to α, and (ii) in tension with the magic-angle pin. This is surfaced for Grant, not resolved here.

## 4 — The load-bearing tension: dilution-slide vs magic-angle homeostasis

This is the central finding. The dilution-trajectory's premise — a **monotonic slide of the bulk operating point from `A→1` down to `A→0`** over cosmic time — runs into **three independent canonical pins**, all pointing the same way (the operating point is held fixed/intensive, not diluted):

| Pin | Verbatim corpus statement | Direction of tension |
|---|---|---|
| **Magic-angle fixity** | `u₀*` is "bond over-bracing at the K4 magic-angle `K(u₀*) = 2G(u₀*)`" (`omega-freeze:34`); "forces `u₀ = u₀*` for the substrate to exist self-consistently" (`trampoline:161`); "**Survives forever** as the cosmological initial condition" (`omega-freeze:47`). | A sliding `u₀*` leaves `K=2G` → substrate loses self-consistency. Pin says **fixed**. |
| **Constant node density** | "To preserve the invariant optical density of the condensate globally (`∂_t ρ_n = 0`) …" (`lattice-genesis-hubble-tension.md:12`). | Crystallization *holds* `ρ_n` constant. Dilution *requires* a quantity to drop as `N` grows. Pin says **homeostatic**. |
| **Intensive per-bond strain** | `u₀ = ρΩ²r²/2K₀` is per-bond, set at local freeze-in (`trampoline:103`); `k₀` "not freeze-in dependent" (`:109`); only `T_EM` is extensive (`:110`). | The operating-point strain is intensive; you cannot dilute an intensive quantity by adding more cells. Pin says **intensive**. |

### 4.1 Where the hypothesis has a genuine substrate-native HOOK (steel-man)

It is not all tension. Two corpus features lean *toward* the hypothesis and are worth Grant's eye:

1. **Ongoing node-addition is real.** `lattice-genesis-hubble-tension.md:10` *does* model expansion as "real-time crystallisation of new electromagnetic nodes" — so "the lattice adds nodes as it expands" is canonical. The hypothesis correctly identifies the substrate-native expansion mechanism.
2. **`Ω_freeze` spin-down is implied but not yet written.** `Ω_freeze = 𝒥_cosmic/I_cosmic` (`trampoline:135`). If `𝒥_cosmic` is conserved and `I_cosmic` grows as the lattice grows, then `Ω_freeze` *spins down* — and since `u₀ ∝ Ω_freeze²` (`:103`), **bonds that crystallize later see a lower `Ω_freeze` → lower `u₀`.** That is a substrate-native realization of "new springs added more relaxed than old ones." *Synthesis flag (verify-before-cite): the corpus does NOT currently write an `Ω_freeze` spin-down / `I_cosmic`-growth dynamics — `grep -rniE "spin[- ]?down|dilut|operating point.*(evolv|slide|decreas|drift|time)"` across `vol3/cosmology` + `omega-freeze` + `trampoline` returns no temporal operating-point evolution. The spin-down is my inference from `J = Iω` + the canonical `u₀ ∝ Ω²`, not an existing leaf claim.*

### 4.2 Why the hook does not (yet) rescue the slide

Even granting `Ω_freeze` spin-down, the corpus's `∂_t ρ_n = 0` + magic-angle pins say the **bulk operating point is regulated back to `u₀*`** (homeostasis), so a spin-down of new-bond `u₀` would lower the *average* over a population that mixes old (high-`u₀`) and new (low-`u₀`) bonds — it would **not** lower the per-bond `u₀` of already-frozen bonds, and it would **not** by itself move the regulated bulk point off the magic angle. For the universe to "slide down `S(A)`" as a single global operating point, the corpus's homeostatic regulation (`∂_t ρ_n = 0`) and magic-angle pin would both have to be **relaxed** — which is precisely the fork in §8. Numerically the pins also bite: the corpus holds the bulk point at `u₀* ≈ 0.187`, which sits *above* the yield onset `A_yield = √α ≈ 0.085` (`trampoline:452`), not in the deep-linear `A→0` regime the late-universe end of the slide requires. *(Caveat: `u₀` over-bracing and `A` wave-amplitude are distinct quantities; the numerical juxtaposition is indicative, not a derivation — do not conflate.)*

## 5 — Does the trajectory derive a number?

**No — lens-only.** Walking each candidate number the trajectory might produce:

| Candidate number | Status in corpus | Does dilution derive it? |
|---|---|---|
| **α-drift magnitude** (`δ_strain` or a dilution analog) | `δ_strain ≈ 2.225×10⁻⁶` is a **definitional residual** `1 − CODATA/α_cold`; the forward derivation was **CLOSED NEGATIVE** (FT-1, 2026-05-31; undershoot ~31 OOM, generic-thermal) (`delta-strain-cosmic-tcc.md:15,165`). | **No.** Dilution would need a derived `dA/dN` × `dα/dA`; neither exists. `dα/dA` is also blocked by the golden-torus-geometry point (§2.6/§3.3). |
| **α-drift sign vs redshift** | Thermal route derives sign (`delta-strain:24`): higher `T` (earlier) → larger `δ_strain` → smaller α (`α⁻¹` larger early). | **Borrowed, not derived.** The dilution route's sign is a *separate* (geometry/`K=2G`) derivation, not the thermal sign (§3.3). |
| **Genesis-epoch redshift** ("knee" where `A` crossed yield) | Corpus genesis = one-shot crystallization into `u₀*`; no A-slide ⇒ no crossing-event redshift. The corpus *does* have a thermal turnover at `T ~ T_B-gap ~ 10¹⁰ K` where B-modes activate and SYM restores (`delta-strain:142`) — but that is thermal, not dilution. | **No.** Requires the (absent) `A(N)` or `A(z)` trajectory law. |
| **`u₀*` evolution** `u₀*(t)` | Corpus: `u₀*` fixed at magic-angle, "survives forever." | **No** — and asserting `u₀*(t)` contradicts the pin (§4). |
| **`H_∞` / DE magnitude** | `H_∞` is Class-E joint-projection; `ρ_Λ` projection is structural, "**No magnitude-matching attempted**" (`op14-cosmic-horizon-profile.md:112`). | **No.** Dilution adds no magnitude here either. |

→ The trajectory is a **unifying narrative lens** over already-canonical pieces (one-shot genesis crystallization; chirality lock; Class-E α–G–𝒥 joint constraint; thermal δ_strain α-running). It re-describes; it does not compute. To graduate from lens to derivation it would need, at minimum, a substrate law for `A(N)` (or `A(z)`) under the *extensive*-load assumption — which is exactly what the magic-angle/`∂_t ρ_n = 0` pins currently forbid.

---

## 6 — Classification (consistency-vs-emergence) + substrate-native + discrimination

### 6.1 consistency-vs-emergence — per-piece

Per the five-class taxonomy (identity / axiom-manifestation / consistency / emergence / operating-point-projection):

| Element | Class | Rationale |
|---|---|---|
| **Core dilution-trajectory hypothesis** | **Consistency-class LENS** over **Class E** operating-point projection — *with the sliding-point premise in tension with canonical fixity*. | Re-frames the Class-E `u₀*` projection as time-varying. Derives no number (§5). Not emergence (no CODATA-free observable falls out); not a clean consistency check either, because its premise conflicts with the magic-angle/`∂_t ρ_n=0` pins. Admissibility gated on the §8 fork. |
| **Consequence 1 — early-saturation genesis** | **Class B** axiom-manifestation (re-statement). | Re-describes A-034 Row 14 (cosmic K4 crystallization SYM*) + the universal `S(A)` "topological-reorganization at `A→1`" already canonical (`universal-saturation-kernel-catalog`, `trampoline:439`). Adds narrative, not substrate content. |
| **Consequence 2 — chirality dilution-lock** | **Class B / consistency** (re-statement, weaker mechanism). | Corpus already locks chirality via the **`I4₁32` chiral space-group topological invariant** set at genesis and "survives forever" (`omega-freeze:45-47`). That is a *topological* lock; the hypothesis's "driver diluted away" is a *dynamical* lock — plausible but not how the corpus holds chirality, and AVE-indistinct from the existing topological lock. |
| **Consequence 3 — α-drift** | **Class B** mechanism-manifestation, **magnitude CLOSED-NEGATIVE**; the dilution variant is a new underspecified mechanism. | Maps onto δ_strain (Class B; magnitude is a definitional residual, closed-negative as derivation). Dilution route adds a third α-mechanism (§3.3) that is underspecified + magic-angle-pinned. |

**No classification promotion.** Per consistency-vs-emergence v1.3 Step 8: this lens adds **no new substrate primitive** beyond the canonical Class-E `u₀*` projection + Class-B δ_strain mechanism. It must stay at the canonical sources' ceiling (Class E / Class B). Headlining it as an emergence-class result would be over-promotion.

### 6.2 substrate-native-check — is the dilution substrate-native or an imported cosmology analogy?

**Mostly imported, with one substrate-native hook.** The framing "a fixed total quantity divided over a growing number of cells → per-cell share dilutes" is the **ΛCDM extensive-density-dilution intuition** (energy density ∝ `a⁻³`), transplanted onto the lattice. The substrate-native picture is the opposite: `u₀`/`A` are **intensive** per-bond states set at local freeze-in (§2.3), and expansion is `∂_t ρ_n = 0` node-crystallization that *preserves* the intensive density (§2.4). The one genuinely substrate-native hook is **`Ω_freeze` spin-down → lower `u₀` for later-frozen bonds** (§4.1) — but that yields a *population mixture* of old/new bonds, not a single global operating point sliding down `S(A)`, and it is not yet a written corpus dynamics. **Verdict: the dilution-slide as stated leaks an SM/cosmology extensive-dilution default; the substrate-native version (if any) is the `Ω_freeze`-spin-down population effect, which is weaker than the hypothesis claims.**

### 6.3 ave-discrimination-check — α(z)-drift vs standard varying-α / static-relic

- **Step 1 (enumerate claims):** the dilution thread's only empirical handle is a redshift-dependent α, `Δα/α (z) ≠ 0`.
- **Step 2 (SM / competitor counterfactual):** a non-zero `Δα/α(z)` is the *generic* prediction of every varying-α theory (Bekenstein/dilaton/runaway-scalar). A monotonic α(z) drift is **not AVE-distinct** on its own.
- **Step 2.5 (discriminator axis — magnitude vs shape):** AVE shares the **FORM** (monotonic α(z)) with varying-α competitors → the discriminator would have to be **MAGNITUDE** — but AVE's α-drift magnitude is a **definitional residual / closed-negative** (§5), so AVE currently carries no calibrated magnitude to discriminate on. The would-be AVE-distinct **SHAPE** feature is the thermal **turnover at `T ~ 10¹⁰ K`** where SYM restores (`delta-strain:142`) — but that is the *thermal* mechanism, and the *dilution* mechanism sharpens neither the magnitude nor the turnover beyond what δ_strain already gives.
- **Verdict:** the dilution-α-drift is **NOT AVE-distinct** as currently scoped. It would be over-claim to frame an α(z) detection (or the Oklo/quasar bounds) as confirming the dilution trajectory specifically; at best it is consistency with the broader Class-E/δ_strain commitment.

---

## 7 — Discriminating prediction + test candidates

### 7.1 The cosmic-α-variation prediction (quasar lines / Oklo)

The trajectory's natural empirical handle is a **redshift-dependent fine-structure constant** `Δα/α(z)`. This is already the canonical δ_strain forward-prediction (`delta-strain-cosmic-tcc.md:140`, verbatim): *"Quasar absorption-line α measurements at higher redshift … should show `Δα/α` consistent with substrate TCC scaling. The Webb/King/Murphy multi-element absorber program is the canonical observational program; current bounds at `|Δα/α| ≲ 10⁻⁵` are loose enough that the substrate prediction is not yet falsified."*

**Candidate falsifiers (each must clear ave-discrimination-check before promotion):**

| Test | Observable | AVE-distinct? | Note |
|---|---|---|---|
| **Quasar absorption lines** (Webb/King/Murphy; ESPRESSO/VLT) | `Δα/α(z)` over `z ≈ 0.2–4` | **Not on magnitude** (AVE magnitude undefined/closed-negative) — *only* on the SHAPE if a thermal turnover or a dilution-specific `A(z)` law were derived. | The discriminator would be a *shape* (turnover / non-monotonic), not the mere existence of drift. |
| **Oklo natural reactor** (`z ≈ 0.14`, ~2 Gyr) | `Δα/α` bound at `~10⁻⁷–10⁻⁸` | Same — tighter magnitude bound, but AVE carries no calibrated magnitude to test. | Strong *bound*, weak *discriminator* for AVE specifically. |
| **Big-bang nucleosynthesis / very-early `T`** | α near `T ~ 10¹⁰ K` (SYM-restoration turnover) | **Potentially AVE-distinct** — the `δ_strain → max → decrease` turnover at the B-mode-gap temperature (`delta-strain:142`) is a shape feature ΛCDM/varying-α do not generically predict. | This is the *thermal* mechanism's signature, not the dilution mechanism's. |
| **CMB low-ℓ / E-B decoupling along `Ω̂_freeze`** | anisotropy axis `(l=60.28°, b=50.48°)` | AVE-distinct (Class-E joint axis), but tests the **chirality/axis** content, not the dilution-α drift. | Already pre-registered (`omega-freeze:65-68`); orthogonal to the dilution slide. |

**Discrimination honesty (Step 2.5):** because AVE shares the *form* (monotonic α(z)) with every varying-α theory and currently lacks a calibrated *magnitude*, **no quasar/Oklo result can confirm the dilution trajectory specifically** at present. The only path to an AVE-distinct test is to **derive a shape** — either the thermal SYM-restoration turnover (already corpus, thermal) or a dilution-specific `A(z)`/`u₀*(z)` law (does not exist; blocked by §4 pins). This is the gating work, and it is theoretical, not observational.

### 7.2 Test candidates that would actually move the hypothesis (theory-side, before any observation)

1. **Derive (or refute) `Ω_freeze` spin-down dynamics.** Write the `𝒥_cosmic = Ω_freeze · I_cosmic` conservation + `I_cosmic(t)` growth law and check whether per-bond `u₀ = ρΩ²r²/2K₀` produces a *population* drift in the bulk operating point — and whether that survives the `∂_t ρ_n = 0` homeostatic regulation. **This is the make-or-break theoretical test; it precedes any α(z) observation.**
2. **Check `u₀*`-slide against `K=2G`.** Quantify how far `u₀*` can move off magic-angle before `K=2G` (and hence the golden-torus α-geometry) breaks measurably — i.e., is there a *band* around `u₀*` within which the substrate stays self-consistent and α drifts smoothly? If the band is `~0`, the dilution-α route is dead; if finite, it is the dilution α-drift's actual amplitude.
3. **Population-average vs regulated-point.** Decide (engine or analytic) whether "the cosmic operating point" the observables project from is the *instantaneous regulated bulk point* (`u₀*`, fixed) or a *population average* over freeze epochs (could drift). This is the same fork as §8, made quantitative.

*(Per scope: these are NAMED candidates, not a build order. No engine code in this session.)*

---

## 8 — The load-bearing physical question for Grant

**One plumber-physical question, the fork the whole hypothesis turns on (Grant's own load-bearing flag, sharpened against corpus):**

> **When the lattice crystallizes a new cell at the expansion front, is that cell laid down SLACK (a fresh relaxed spring that a fixed early load then has to share itself across — so the per-node operating point dilutes as `N` grows), or is it laid down PRE-LOADED at the magic-angle `u₀* ≈ 0.187` (the `K=2G` self-consistency value — so the operating point is intensive and there is no slide, only homeostasis)?**

The corpus currently answers **PRE-LOADED / intensive / homeostatic** in three independent places (§4): magic-angle fixity (`trampoline:161`, "survives forever" `omega-freeze:47`), `∂_t ρ_n = 0` constant-density crystallization (`lattice-genesis-hubble-tension.md:12`), and intensive per-bond `u₀` (`trampoline:103,109`). The dilution trajectory needs the **SLACK / extensive** answer.

Sub-question if Grant leans toward admitting some slide:
> Does `Ω_freeze` **spin down** as `I_cosmic` grows (so later-frozen bonds genuinely freeze at lower `u₀`), and if so, is the cosmic operating point the **instantaneous regulated `u₀*`** (fixed) or a **population average over freeze epochs** (can drift)? The corpus writes neither the spin-down nor the population-average; both are needed for the slide and neither currently exists.

This is a Rule-16 *ask-before-design* surface: the answer collapses the hypothesis to either (a) inadmissible-as-stated (pre-loaded; the existing homeostasis picture stands, dilution is a mis-import), or (b) a scoped new dynamics workstream (`Ω_freeze` spin-down + population-average operating point) that would need its own derivation chain and would still owe a shape-level α(z) prediction to be AVE-distinct.

---

## 9 — Cited leaves (verify-before-cite ledger)

Every load-bearing citation in this doc was read or grepped in this session on branch `analysis/2026-06-07-cosmic-dilution-trajectory` @ `63e6671a`:

| Leaf / source | Lines used | Verified |
|---|---|---|
| `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md` (clm-3zz0f6) | 15-24 | Read full |
| `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md` (clm-hp7nlm) | 13-15, 24, 65-71, 140-142, 164-165 | Read full |
| `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/op14-cosmic-horizon-profile.md` (clm-48g5qf) | 68, 76, 112 | Read full |
| `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md` | 10, 12, 25, 35-37 | Grepped (§2.4/§4) |
| `manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md` (clm-dsb560…) | 11, 34, 44-49 | Read full |
| `manuscript/ave-kb/common/trampoline-framework.md` | 103, 109-110, 135, 161, 374-388, 452 | Read 1-519 + grep |
| `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2 (SYM/ASYM/δ_strain three-class) | block | Read (system context) |
| `_orchestration/theoretical/cosmic-epsilon-de-projection-scoping.md` | 9 (Grant Q1 DYNAMIC) | Read full |
| `research/2026-05-19_cosmic-epsilon-de-projection-mechanism.md` | — | Located (not load-bearing; scoping doc + op14 leaf sufficed for DYNAMIC verdict) |

**Absence check (verify-before-cite trigger 6):** `grep -rniE "dilut|spin[- ]?down|operating point.*(evolv|slide|slid|decreas|chang|drift|time)|u_?0.*(evolv|slide|decreas|dilut)"` over `manuscript/ave-kb/vol3/cosmology` + `omega-freeze-cosmic-grain-cascade.md` + `trampoline-framework.md` returned **no temporal operating-point dilution/slide and no `Ω_freeze` spin-down dynamics** (only spatial `1/r` gravity dilution + an unrelated DAMA DC operating-point). The dilution-trajectory and the `Ω_freeze`-spin-down hook are therefore **new** (not already-canonical), and the spin-down is flagged as synthesis in §4.1.

---

## 10 — Honest closure note

This is a clean scoping result, not a falsification and not a confirmation. The headline question (α-drift vs SYM-invariance) resolves cleanly to **different axes** with no corpus contradiction. The hypothesis as a whole is a **consistency-class lens** that **derives no number** and currently **conflicts with three canonical pins** (magic-angle fixity, `∂_t ρ_n=0` homeostasis, intensive per-bond `u₀`). It has one genuine substrate-native hook (`Ω_freeze` spin-down) that is weaker than the global-slide claim and not yet written in corpus. The branch is left open pending Grant's adjudication of the one fork in §8; per substitution-not-retraction discipline, nothing in the corpus is edited and no slot is refilled.
