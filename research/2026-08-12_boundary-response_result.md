# THE BOUNDARY-RESPONSE DERIVATION (R51 §4) — RESULT

**Date:** 2026-08-12 · **Branch:** `lane/2026-08-12-r51-boundary-response` · **Base:** `origin/main` @ `ecf91aec`
**Frozen prereg:** [`2026-08-12_boundary-response_prereg-FROZEN.md`](2026-08-12_boundary-response_prereg-FROZEN.md),
committed **ALONE** and **PUSHED** at `b05ec6bd` before any derivation content, algebra, or
lane-produced number existed (freeze-by-push). The §2 verdict grammar was frozen at that commit.
**Premise (cited, not re-derived):** `_orchestration/docket-entries/2026-08-12-ruling-r51-a1-two-objects-carve.md`.

**Class:** DERIVATION (analytic, symbolic). **Mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`; edits no KB
leaf, register, ledger, axiom, or ruling; changes no solidity; propagates nothing — all findings
ROUTED.** Engine `src/ave` byte-untouched; **no engine run was consulted or consumed** (#935 stencil
fence: `crystal_engine.py` codes a bulk scalar V and would carry the very import under test).

---

## §0 — SVA header (restated at the point of reading; the frozen prereg §0 governs)

**SECTOR** — driven coordinate = **A1 dilatation** (defect size `R`, the `(1,1,1,1)/2` common mode);
fixed content = **T2 Cosserat winding** `n`, which stays an integer parameter throughout and never
becomes a dynamical DOF inside the A1 phasor (`master-equation.md:20` fence held; R51 §7 held).
**REGIME** — cold, sub-yield, crystalline, lossless-reactive (Regime-I); past-wall and de-bonded
**OUT OF SCOPE**. **ENERGY LEDGER** — everything is **rim**: no port, no arrow, no loss word; the A1
near-field is the banked reactive NOT-A-PORT store (`port-register.md:77`). **PROVENANCE** — every
step tagged in §3; **no `K` and no `K = 2G` anywhere in the chain**.

---

## HEADLINE

> ### **VERDICT: `RESPONSE-EXISTS(E = a·R + b·R⁻¹)`**
>
> A pure common-mode boundary drive on a fixed-content defect **does** meet a restoring response.
> `E(R)` has exactly one stationary point at finite `R* > 0`, and it is a **minimum**
> (`E''(R*) = 2b/R*³ > 0`). The chain is **K-free**: it runs on `G_vac` (DERIVED, `= ρ_bulk c²`,
> cross-checked by `v_T = √(G/ρ) = c` exact), the receipted Axiom-3 curl-only action, the fixed
> topological content, and geometry. **R51 item 2 SURVIVES its own §5(ii) kill-check.**
>
> **But its mechanism attribution in R51 item 2 is WRONG, and the correction matters.** R51 writes
> the tank as *"fixed charge on a tank whose C is the medium's bulk compliance seen at the defect
> boundary."* The medium's bulk compliance is **infinite** (the A1 channel has exactly zero
> stiffness — #935's flat direction, re-derived here as P1) and therefore contributes **nothing**.
> The restoring stiffness is the **defect's own A1 self-field energy at fixed enclosed content**,
> and the collapsing tension is the **T2 winding's gradient energy**. The tank is real; its `C` is
> not the medium's.
>
> **Why the boundary response differs from the bond response — the one-sentence answer to the
> question the lane was posed.** The flat direction is flat *in the field*, but the A1 field's
> energy depends on the **source geometry**, and `R` is exactly what parameterises the source
> geometry. The bulk does not push back on a longitudinal *wave*; the defect's own constrained
> self-field pushes back on the defect's *size*. **Those are different questions, and #935
> answered only the first.**

**What is NOT claimed.** No value, no number, no frequency magnitude (the brief asked for symbols).
No chord: the balance is structurally the classical Coulomb-vs-tension (Poincaré-stress) problem, and
its phenomenology is peer with standard physics — see §7's discrimination note. The §9-pass/#955
clock connection is **FLAGGED, NOT BANKED** (§6). Axiom 5 clause (c1)'s owed theorem is **NOT
discharged and NOT assumed** — but §6 shows the *frequency* leg depends on it (§8 FLAG-3).

---

## §1 — P1: the bulk A1 channel has no restoring force — **DEMONSTRATED, not adjudicated**

Frozen as ENTAILED in prereg §4 P1; the honest verb is therefore *demonstrated*. Recorded because the
rest of the derivation is built on it, not as this lane's result.

Axiom 3's action (`eq_axiom_3.tex:22`) is **curl-only in the potential**:

```
L_node = ½ ε₀ |∂_t A|²  −  (1/2μ₀) |∇ × A|²
```

Helmholtz-split `A = A_L + A_T` with `∇ × A_L = 0`, `∇ · A_T = 0`:

| sector | potential term `(1/2μ₀)|∇×A|²` | kinetic term `½ε₀|∂_tA|²` |
|---|---|---|
| longitudinal `A_L` | **identically 0** (`∇ × A_L ≡ 0`) | `½ε₀|∂_tA_L|²` ≠ 0 |
| transverse `A_T` | `(1/2μ₀)|∇×A_T|²` | `½ε₀|∂_tA_T|²` |

So the longitudinal sector carries **inertia but no stiffness**. In EE dress: a **pure inductor to
ground, no shunt capacitance** — not a tank. Equation of motion `ε₀∂²_t A_L = 0`; the Noether content
of the residual gauge family is the pointwise conservation of the Gauss function
`∇·(ε₀∂_tA)` — exactly as `eq_axiom_3.tex` states. **Effective `K = 0` on the receipted set**, and
Axiom 5 does not repair it: the axiom explicitly *"adds no kinetic or potential term on the flat
direction"* (`eq_axiom_5.tex:88`). No longitudinal wave, no pole, no branch. ✔ consistent with #935.

**Nothing below overturns this.** The result in §3 adds no longitudinal stiffness to the bulk and no
propagating branch; the pole-absence results survive untouched, and the response derived here is
**below cutoff — bound to the defect, ringing in place** (R51 item 2's own scope).

---

## §2 — FORK-SP resolved: **PARALLEL**, and the medium is transparent

Frozen open in prereg §0 row 4 / §4 P4 with both branches; resolved by derivation, not convenience.

The defect's self-stiffness and the medium's A1 compliance act **at one common coordinate `R`**:
displacing the boundary by `δR` does work against both simultaneously, so the energies add at fixed
`R` and the stiffnesses compose in **PARALLEL** (`k_tot = k_defect + k_medium`). The balloon test:
inflating by `δR` stretches the rubber *and* loads the outside medium; both resist at the same
coordinate. SERIES would require an intermediate coordinate with the medium in the load path
transmitting the defect's own internal restoring force — there is none, because the defect's
self-energy gradient acts directly on its own boundary.

**Consequence.** `k_medium = 0` (§1) is **transparent** under PARALLEL, not fatal. Had FORK-SP
resolved SERIES, the zero would have been a short and F4 would have fired `NO-RESPONSE`. **The fork
was load-bearing and it could have gone the other way.**

---

## §3 — The derivation (every step provenance-tagged)

**Setup.** A defect of fixed topological content sits in the cold lattice. Its size `R` is the single
A1 collective coordinate. Fixed content, held constant under the drive:
- `n` — the T2 Cosserat winding integer (topological, cannot change continuously);
- `𝒬` — the defect's conserved A1 monopole content, i.e. the source the Gauss function is pinned to.
  **`𝒬`'s IDENTITY rides the DEFERRED FORK-1** (`eq_axiom_3.tex:22`: *"which clause of Axiom 5 pins
  it is deliberately left open"*). **The derivation below is FORK-1-invariant** — the `1/r²` monopole
  geometry and the quadratic energy form are the same under either reading, so only the *label* of
  `𝒬` depends on the fork, never the form. FORK-1 is **not** resolved here.

Write `𝒞_A1` for the A1 sector's quadratic-form coefficient (`ε₀` in the EM dress; the corresponding
inertial coefficient in the mechanical `u` dress). Geometric `O(1)` factors are carried as
`c₁, c₂, c₃ > 0` and are **not** evaluated — this lane produces forms, not values.

### Term 1 — the T2 winding's gradient energy (the collapsing tension)

A fixed winding `n` compressed into size `R` has angular gradient `|∇θ| ~ n/R`. With `γ_c` the
couple-stress modulus (`[γ_c] = N`):

```
E_shear(R) = c₁ · γ_c · n² · R                                    [exponent +1]
```

Dimensions: `γ_c (n/R)² · R³ = γ_c n² R` ✔ (J). **This is the classical Hobart–Derrick `L^(d−2) = L¹`
scaling for a fixed-winding gradient energy in `d = 3`. Alone it is monotone increasing ⇒ collapse.**
**PROVENANCE: DERIVED.** `γ_c = G_vac ℓ_c²`, `G_vac = ρ_bulk c²` — the mechanical dress of Axiom 3's
*curl* term (the same term that gives `c = √(G/ρ)`), so this is receipted, not imported. `ℓ_c` is
defined against `2(μ+κ)` through the `ξ_K` relations (`common-mode-twist-ledger.md:186`) — a
**shear-family** combination, **K-free**. ⚠ `ℓ_c` carries a known 10.667× shear-modulus-choice
bracket (R1a vs R1b, `common-mode-twist-ledger.md:274`); this affects the frequency *magnitude* only,
never the existence verdict (see §5 robustness ladder).

**Cross-check against corpus prior.** `research/2026-07-01_electron-unifier-cocompress_result.md`
measured `E_tank_w ∝ R⁺¹` from conserved circulation. **My `+1` agrees.** (Only that lane's *analytic*
Part 1 is cited; its Part 2 is downgraded to near-tautology by its own verdict and is not evidence
here.)

### Term 2 — the A1 self-field energy at fixed content (the restoring term)

This is the step the question turns on. The longitudinal field is **constrained**, not free:
`∇·(𝒞_A1 ∂_tA_L) = 𝒬`-source, pinned. For a monopole content `𝒬` with the defect boundary at `R`,
the exterior field is the free-geometry `1/r²` solution and the interior is screened by the content:

```
E_A1(R) = ∫ ½ 𝒞_A1⁻¹ |D|² d³x ,   D_r = 𝒬/(4πr²) for r > R
        = (𝒬²/8π𝒞_A1) ∫_R^∞ dr/r²
        = c₂ · 𝒬² / (𝒞_A1 · R)                                   [exponent −1]
```

**PROVENANCE: DERIVED** from Axiom 3's kinetic term + the Gauss constraint + geometry. `𝒞_A1` is
Axiom-1 native. **No `K`. No `κ = c⁴/7G`** — clause G's elliptic law is *not* used; this runs off the
constrained-field energy directly.

> **The category check, run explicitly (this is the load-bearing step and the one most likely to be
> wrong).** §1 says the longitudinal sector has *no potential energy*. §3 Term 2 uses a longitudinal
> field energy *as* a potential. Is that a contradiction? **No.** §1's statement is that the energy is
> flat **as a function of `A_L`** — the field direction is free. Term 2's statement is that the
> constrained field's energy depends on the **source geometry**, and `R` parameterises the source, not
> the field direction. This is ordinary electrostatics: the self-energy of a charged shell,
> `U(R) = Q²/8πε₀R`, is a genuine potential for the collective coordinate `R` even though the
> Coulomb field itself is constrained and non-propagating. **The two statements are compatible, and
> their compatibility is exactly why the boundary response differs from the bond response.**

### The balance

```
E(R) = a·R + b/R ,      a = c₁ γ_c n²  > 0 ,      b = c₂ 𝒬²/𝒞_A1  > 0
E'(R) = a − b/R²  = 0   ⇒   R* = √(b/a)        (exactly one stationary point, finite, > 0)
E''(R*) = 2b/R*³ > 0                            ⇒   MINIMUM — a restoring response
```

```
R*  =  √( c₂ 𝒬² / (c₁ 𝒞_A1 γ_c n²) )   =   (1/(n ℓ_c)) · √(c₂/c₁) · 𝒬/√(𝒞_A1 G_vac)
```

Dimensional check: `[b] = [𝒬²/𝒞_A1] = J·m`; `[a] = [γ_c] = J/m`; `[b/a] = m²` ⇒ `[R*] = m` ✔.

**Prefactor check (prereg §0 row 11 hazard, armed):** neither `a` nor `b` vanishes identically —
`a = 0` only for `n = 0` (no winding, no defect) and `b = 0` only for `𝒬 = 0` (no content). Both are
nonzero exactly when a defect of fixed content exists, which is the stated premise. **F6 does not
fire.**

### The candidate stabilizers that DON'T carry the result (recorded, because the negatives matter)

| Candidate (corpus Derrick bypass) | Verdict | Why |
|---|---|---|
| **Faddeev–Skyrme quartic** (`relativistic-inductor-newtonian-limit.md:62`) | **NOT USED** | Axiom 3's action is quadratic; there is no 4-derivative term in the receipted set. Its coefficient is recorded as *"imported from Vol 2 / Axiom 1 rather than re-derived"* (`vol4/claim-quality.md:1587`). Admitting it would have been an untagged import — the anti-rescue guard's named failure. **The result does not need it.** |
| **Axiom-4 saturation, small-`A` expansion** | **DOES NOT COUNTER** | The expansion `1/S ≈ 1 + ½(A/A_y)²` generates `|∇×A|²A²` — more *field powers*, same *derivative count*, so it scales as `R⁺¹` like Term 1. Derrick counting is about derivatives, not powers. A real negative. |
| **Axiom-4 saturation, full kernel** | **REAL, but a WALL not a tank** | `H ~ |D|²/(2ε₀S)` diverges as `A → A_y`, i.e. as `R → R_sat⁺`. K-free and genuine, but a divergence, not a smooth curvature. See **FORK-W** below. |
| **Lattice floor `ℓ_node`** (bypass #1) | **REAL, but a WALL and IC-class** | A hard one-sided constraint, not a harmonic minimum; and `ℓ_node = ħ/(m_e c)` is an imported calibration. Had this been the *only* stabilizer the verdict would have been `CANNOT-CLOSE-WITHOUT-IC`. |
| **Bilateral chiral / two strain axes** (bypass #3) | **DOES NOT COUNTER** | Derrick's scaling argument is insensitive to field multiplicity: two 2-derivative sectors both scale as `R⁺¹`. Adding axes does not add a counter-term. A real negative. |

> **FORK-W (flagged open, not resolved).** Two independent K-free bounds exist: the smooth `1/R`
> minimum at `R*` (§3) and the saturation divergence at `R_sat`. Which is operative depends on
> whether `R* > R_sat`. **Existence of a bound response holds either way** (both bound the defect),
> but the *character* differs: `R* > R_sat` ⇒ a harmonic tank with the §6 frequency; `R* < R_sat` ⇒
> the defect rests against the saturation wall and the response is anharmonic with no small-signal
> frequency. **Resolving FORK-W requires a value comparison this lane is scoped out of.** Routed.

---

## §4 — Verdict assembly against the frozen bins

| Falsifier | Fired? | Note |
|---|---|---|
| F1 `E(R)` monotone | **NO** | exactly one stationary point at finite `R* > 0` |
| F2 counter-term chain contains `K` | **NO** | Term 2 runs off Axiom 3 + Gauss + geometry; audited step-by-step in §3 |
| F3 counter-term coefficient is a genesis/`ℓ_node` datum | **NO** for existence; ⚠ **PARTIAL for scale** | the *existence* needs no IC; `R*`'s **value** is set by `𝒬`, which is clause-S genesis-deposited data — see §7 |
| F4 FORK-SP ⇒ SERIES | **NO** | resolved PARALLEL (§2) |
| F5 stationary point is a maximum | **NO** | `E'' = 2b/R*³ > 0` |
| F6 vanishing prefactor | **NO** | checked explicitly in §3 |
| F7 `n` forced dynamical | **NO** | `n` stays an integer parameter throughout; fence held |
| F8 positive control fails | **NO** | see §5 |

**⇒ `RESPONSE-EXISTS(E = a·R + b·R⁻¹)`.**

**Bin-3 boundary, stated precisely** (the honest edge of this verdict): `RESPONSE-EXISTS` is booked on
**existence**, which is IC-free. The **scale** `R*` is not — it rides `𝒬`, which is genesis-deposited
boundary data by Axiom 5 clause S's own wording. Per the frozen grammar this is `RESPONSE-EXISTS`
(bin 3 requires the *existence or scale* to be IC-set **and the response to be underivable without
it**; here existence is derivable and only the scale is IC-set). **The split is the finding, and it is
the FORM-derived / VALUE-imported signature landing a fifth time.**

---

## §5 — Controls (frozen in prereg §5; run)

**POSITIVE CONTROL — restore `K`, expect a restoring response.** With `K ≠ 0` the medium acquires
`½K θ²`, adding a strictly positive stiffness at the coordinate `R`; the machinery reports a restoring
response, as the textbook acoustic monopole requires. ✔ **PASS** — the machinery is not structurally
blind to stiffness, so its nulls are meaningful.

**POSITIVE CONTROL 2 — T2 transverse sector.** The same curl term reproduces the known
`c = √(G/ρ)` restoring structure. ✔ **PASS.**

**NEGATIVE CONTROL — empty lattice, no fixed content (`n = 0`, `𝒬 = 0`).** Then `a = b = 0` and
`E(R) ≡ 0`: no restoring force, no stationary point. ✔ **PASS**, and this is the decisive one — the
machinery returns **zero when there is no content and nonzero when there is**, so the response is
attributable to the fixed content and is **not manufactured by the formalism**.

**Structural-degeneracy self-check (prereg §4) discharged.** The named trap was that a
curl-only-by-construction zero would make `NO-RESPONSE` circular. That trap is **not** what happened:
the verdict is positive, and it survives *because* the energy depends on source geometry rather than
on the flat field direction (§3 category check). The negative control confirms the positive is not an
artifact of the formalism.

**Robustness ladder (frozen).** PRIMARY = **existence** ✔ booked. SECONDARY = **form/exponents**
(`+1` / `−1`) ✔ booked, and the `+1` agrees with the independent corpus prior. **Supplementary, not
booked** = any magnitude; `ℓ_c`'s 10.667× bracket sits entirely in this rung.

---

## §6 — The tank frequency, as a FORM (symbols, not values)

With `M_eff = c₃ ρ_bulk R*³` (the A1 inertia of the breathing coordinate):

```
ω_tank² = E''(R*) / M_eff = 2b / (c₃ ρ_bulk R*⁶) = 2a / (c₃ ρ_bulk R*⁴)
```

Substituting `a = c₁γ_c n²`, `γ_c = G_vac ℓ_c²`, `G_vac = ρ_bulk c²` — **`ρ_bulk` cancels**:

> ### `ω_tank  =  K_geo · n · c · ℓ_c / R*²`,  `K_geo = √(2c₁/c₃)`

**`M_eff` fork — the two frozen branches are degenerate, reported as such.** Branch (i) medium
added-mass `4πρ_bulk R*³` and branch (ii) the defect's own dilatation inertia **both** give
`M_eff ∝ ρ_bulk R*³` and differ only in the `O(1)` factor absorbed into `c₃`. **The separator does not
separate at form level.** Recorded honestly rather than presented as a choice.

**Robustness note.** `ρ_bulk` cancels and `𝒞_A1` does not appear (it enters only through `R*`, an
output). The frequency form therefore depends on `{n, c, ℓ_c, R*}` alone.

### The clock chain — **FLAGGED, NOT BANKED**

If `ℓ_c ~ R*`, then `ω_tank ~ n·c/R*` — the defect's own light-crossing rate; at `R* ~ ℓ_node` this is
`c/ℓ_node = m_ec²/ħ`, the Compton rate. **That is a suggestive shape and nothing more.** R51 §5(iii)
requires the size-vs-bias relation to reproduce the ratified clock chain **quantitatively** at the
§9/#955 adversarial pass, and *"sign agreement alone does not bank it."* This lane produces no
quantitative comparison and **claims none**; the connection is named as a routed follow-on. Per the
tautology filter: `ℓ_node` is *defined* as `ħ/(m_ec)`, so recovering the Compton rate from
`R* ~ ℓ_node` is **at risk of being an identity, not a prediction** — that risk must be adjudicated
before any §9 use.

---

## §7 — Discrimination (run before any framing)

**SM/classical counterfactual.** The structure `E = aR + b/R` balancing self-field repulsion against
a topological line tension is the **classical electron-radius problem**, with the winding tension
playing the role Poincaré stresses played historically. Standard physics reaches an equilibrium radius
the same way. **The phenomenon is PEER, not AVE-distinct** — as R51 §6 says it should be: peer
in-regime is the expected result. **Consistency-class.** No chord is claimed and none should be read
in.

**Where the distinct content actually sits** (if anywhere): AVE supplies the stabilising tension from
**receipted topological content** rather than postulating it, and does so **without a bulk modulus**.
That is a provenance difference, not a phenomenological one, and it is a **FORM** result.

**Symmetric standard applied.** "AVE imports `K`" is not by itself an AVE-specific defect — standard
elasticity measures its moduli too. The load-bearing question was only ever whether **AVE's own chain
needs `K`**, and the answer is no.

---

## §8 — Flags (surfaced, not fixed) and routing

- **FLAG-1 — R51 item 2's mechanism attribution is wrong (the conclusion survives).** *"a tank whose
  C is the medium's bulk compliance seen at the defect boundary"* — the medium's bulk compliance is
  infinite and contributes nothing; the `C` is the defect's own A1 self-field compliance. **Item 2
  passes its kill-check with a corrected mechanism.** Routed to the ruling author; no record edited.
- **FLAG-2 — `master-equation.md`'s 2026-07-20 sector-dynamics tag is stale at HEAD.** It asserts
  `θ` *"carries a genuine bulk restoring force (½K(∇·u)², K = 2G) on the gapless lattice-computed
  P-branch"* and *"∇·u propagates"*. #935 (2026-08-09) and the R40 sweep (2026-08-11) removed that
  branch. The tag is a Rule-12 preserved block; **flag-don't-fix**, routed to the auditor lane.
  Same content is live at `vocabulary-register.md:594` (dated 2026-08-07, same pre-#935 vintage).
- **FLAG-3 — the frequency leg depends on Axiom 5's owed theorem; the existence leg does not.**
  §6 uses the quasi-static `E(R)`, i.e. it assumes the constrained field tracks the boundary faster
  than `ω_tank`. That is precisely what **THE BIAS PROPAGATION THEOREM** (clause c1) would establish,
  and it is **owed, not held**. Clause (c1) is **neither discharged nor assumed** as an input: the
  §3/§4 **existence** verdict is a statement about a static energy functional and needs no
  propagation law. **Only §6's frequency inherits the debt.** Routed to
  `_orchestration/2026-08-10_bias-propagation-brief.md`.
- **FLAG-4 — the freeze-in formula consumes a nonzero `K₀`.** `trampoline-framework.md:95-125` writes
  `u₀ = ρ Ω²_freeze r²_node / (2K₀)`. If `K₀` there is the bulk modulus, the freeze-in derivation
  consumes exactly the object #935 removed; if it is the bond stiffness `k₀` (which that same passage
  distinguishes: *"Bond stiffness k₀ is intrinsic to the LC tank … Not freeze-in dependent"*), it is
  clean. **The symbols are not disambiguated in the source.** Surfaced, not resolved — this is
  load-bearing for R51 §3 reading (ii). Routed.
- **FORK-W** (§3) and **FORK-1** (§3, `𝒬`'s identity) remain **open**; neither is resolved here and
  neither blocks the existence verdict.

**Consistency-vs-emergence ledger.** §1 P1: **DEMONSTRATED** (entailed, background). §2 FORK-SP:
**ADJUDICATED** (fireable, could have gone SERIES). §3 existence + exponents: **DERIVED (Class-C
CONSISTENCY** — form-level, peer phenomenology per §7). §6 frequency: **DERIVED-CONDITIONAL** on
FLAG-3. §7: no chord. **No solidity moves anywhere.**
