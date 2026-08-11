# THE BIAS PROPAGATION THEOREM (R49b/R50) — DERIVATION COMPANION

**Date:** 2026-08-11 (review-cycle repair pass) · **Branch:** `lane/2026-08-10-bias-propagation` · **Base:** `origin/main` @ `ad376e9a`
**Parent result:** [`2026-08-10_bias-propagation_result.md`](2026-08-10_bias-propagation_result.md) · **Frozen prereg:** [`2026-08-10_bias-propagation_prereg-FROZEN.md`](2026-08-10_bias-propagation_prereg-FROZEN.md) (byte-untouched)
**Driver legs:** `L5` (widened lemma), `L6` (pole-test scope), `L2` (GR force object) in [`drivers/bias_propagation_lane.py`](drivers/bias_propagation_lane.py); every equation below is machine-checked by [`drivers/bias_propagation_number_check.py`](drivers/bias_propagation_number_check.py) and every quote by [`drivers/bias_propagation_quotes_number_check.py`](drivers/bias_propagation_quotes_number_check.py).
**Class:** DERIVATION. Mints nothing; edits no KB leaf, register, ledger, ruling, or manuscript file; changes no solidity; all propagation ROUTED. Engine `src/ave` byte-untouched.
**Presentation state:** `[DO-NOT-MERGE]`. **Nothing in this document reads CLEARED.**

---

## §0 — WHAT THIS COMPANION IS, AND WHAT IT IS NOT

**IS:** the equations, in full, for the four pieces of derivation content the 2026-08-11 review-cycle repair pass produced — the widened kernel-clock lemma, the corpus `√S` collision it exposes, the GR force-object distinction, and the pole test's validity scope. Each is stated with its proof and its machine check.

**IS NOT:** a reconstruction of the lane's three original D1 routes (variational / multiple-scales / slaving-map) or of the per-finding Tier-2 dispositions. **Those records were not committed by the route lane, which has closed.** The result doc's §5 aggregate is the only surviving record, and it is left as the record. Reconstructing a per-finding table from a summary would manufacture provenance — the exact failure mode of this lane's two withdrawn phantoms. **What survives of the routes is restated in §5 below, attributed to the result doc, and nothing is added to it.**

**REGIME / SECTOR / PHASE-STATE.** Unchanged from the parent (`result.md` §0): crystalline cold-linear Regime-I, sub-yield, lossless-reactive, exterior `D(A) → 1`; A1 bulk/dilatation slot; T2 shear/EM and Cosserat micro-rotation byte-untouched. **Everything below is a WEAK-FIELD statement** (`A → 0`); the `A → 1` wall is out of scope and is evaluated nowhere.

---

## §1 — THE WIDENED KERNEL-CLOCK LEMMA

### §1.1 Setup

Canon's gravitational dialect (Ax4 `:10`, *"the same $S(A)$ function governs strain expressed as … $r_s/r$ (gravitational metric strain)"*):

```
A(r) = r_s/r ,        r_s = 2GM/c²
S(A) = √(1 − A²)                       (Axiom 4 kernel, eq_axiom_4.tex)
```

A trapped resonance of rest frequency `ω₀` sitting at `r` reads out at infinity as `ω_∞ = ω₀·W(A)` for some clock law `W`, and its energy at infinity is `E = ħω_∞` (counter-arm **C7** — that `E` tracks the local clock linearly with no further bias dependence — remains **LIVE and undischarged**; everything below is conditional on it, exactly as `result.md` §2.4 states).

The radial force is the energy gradient:

```
F(r) = −∂_r E = −ħω₀ · (dW/dA) · (dA/dr) = +ħω₀ · (dW/dA) · r_s/r²          (1)
```

Newtonian gravity on that resonator (`m = ħω₀/c²`) is

```
F_N = −GMm/r² = −ħω₀ r_s /(2r²)                                              (2)
```

so **(1) reproduces (2) if and only if `dW/dA|₀ = −1/2`.** The whole lemma is the observation that a large, natural class of clock laws gives `dW/dA|₀ = 0` instead.

### §1.2 The lemma

> **LEMMA.** Let `W = f(S(A))` with `f` differentiable at `S = 1` and `f′(1)` **finite**. Then
>
> ```
> dW/dA = f′(S) · dS/dA = f′(S) · ( −A/√(1−A²) )
> dW/dA|₀ = f′(1) · 0 = 0                                                    (3)
> ```
>
> **identically, for every such `f`** — because the kernel is *quadratic* in `A` at the origin:
>
> ```
> S = √(1−A²) = 1 − A²/2 + O(A⁴)                                             (4)
> ```

The leading surviving behaviour is second order. Expanding `f` about `S = 1` and substituting (4):

```
W ≈ f(1) + f′(1)·(S − 1) = f(1) − ½ f′(1) A² + O(A⁴)                        (5)
```

so `dW/dA ≈ −f′(1)A`, and (1) gives

```
F ≈ −ħω₀ f′(1) · A · r_s/r² = −ħω₀ f′(1) · r_s²/r³                          (6)
```

> **★ `F ∝ 1/r³`, for every admissible `f`. There is no `1/r²` term at all — not a wrong coefficient, an absent power.**

**The `S^p` family is the special case `f(S) = S^p`, `f′(1) = p`,** recovering the previously-shipped `F = −p ħω₀ r_s²/r³`. The class that dies is strictly larger: **every `C¹` function of the Axiom-4 kernel.**

*Machine check (driver `L5`, number check `LEMMA …`):* `dW/dA|₀` computed for an undefined sympy `Function` returns exactly `0`; the leading force is `-4*G**2*M**2*fprime1*hbar*omega_0/(c**4*r**3)` `= −f′(1)ħω₀r_s²/r³`; the radial power is recomputed in plain `math` as `3.000000000` from two-radius samples; the `S^p` specialisation is verified to reproduce the same expression with `f′(1) → p`.

### §1.3 The escape condition, stated positively

> **ESCAPE.** A clock survives iff **`dW/dA|₀ ≠ 0`** — iff it is **leading-order LINEAR in `A`**.

By (4), `S` has **no linear term in `A`**, so no `C¹` function of `S` can supply one. An escape therefore requires `f′(1) → ∞`: a **non-`C¹` branch point at `S = 1`**.

Canon's surviving clock is exactly that. The slope-1 lapse

```
W = √(1 − A) ,        dW/dA|₀ = −1/2                                        (7)
```

is `−1/2` on the nose — the coefficient (2) demands. Written as a function of the kernel it is `f(S) = √(1 − √(1 − S²))`, whose derivative diverges as `S → 1`. **That divergence is not a pathology; it is the entire content of the escape.**

*Machine check:* `slope1_lapse_dW_dA_at_zero = "-1/2"`, `slope1_lapse_escapes = true`.

### §1.4 The `|∇ε₁₁|` NON-escape (named, because it is the obvious rescue)

Canon's own observability rule — *"only spatial gradients of $A$ across the substrate are physically observable"* (KB `CLAUDE.md`) — suggests re-keying the clock on the **observable gradient** instead of on `A`. On the canon profile `ε₁₁ = 7GM/c²r`:

```
|∇ε₁₁| = 7GM/(c² r²)                                                        (8)
```

A clock linear in that observable, `W = 1 − λ|∇ε₁₁|`, gives

```
E = ħω₀ ( 1 − λ·7GM/c²r² )
F = −∂_r E = −2λ ħω₀ (7GM/c²) / r³                                          (9)
```

> **★ `1/r³` again — for every coupling `λ`.** The radial power is `λ`-independent, so no choice of coupling *strength* recovers `1/r²`. **The gradient-observable rescue fails by the same arithmetic as the kernel family.**

The structural reason is one line: any clock keyed on a quantity that falls as `1/r²` produces a force that falls as `1/r³`. Newtonian gravity needs the clock itself to fall as `1/r`, i.e. to be linear in `A` — which is (7).

*Machine check:* `grad_eps_route_force = "-14*G*M*hbar*lambda_g*omega_0/(c**2*r**3)"`, recomputed radial power `3.000000000`, `grad_eps_route_can_never_be_1_over_r2 = true`.

### §1.5 What the lemma does and does not license

- **DOES:** rule out, in the weak field, every `C¹`-function-of-the-kernel gravitational clock, on the ground that canon has Newtonian gravity. This is an **internal-coherence adjudication** and the run could have come out otherwise.
- **DOES NOT:** say anything about the strong field (`A → 1`), where the expansions above are void and where the two candidate `S`-readings do genuinely differ in kind.
- **DOES NOT:** discharge C7. If a resonance's energy carries additional bias dependence (mode volume, `D(A)`-graded confinement, `c_eff`-graded size), `E = ħω_∞` is not the whole energy and (1) is not the whole force.
- **DOES NOT:** pick a winner in §2's collision. It shows one reading is weak-field-falsified *as a clock*; it says nothing about what that same function's role **would be** as a **constitutive modulus** — which would be a different job for the same symbol, and is **not** a resolution this lane is proposing (the modulus-and-lapse split was shipped as fact in the first cut, and is withdrawn; §2.2a of the result doc).

---

## §2 — THE `√S` SYMBOL COLLISION IN CANON (named, ROUTED, unresolved)

Two canon sites use `√S` inside the **same** `E = ħω` construction and mean **different functions**:

| # | file:line | verbatim | forced meaning of `S` |
|---|---|---|---|
| 1 | `manuscript/ave-kb/vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md:128` | *"deeper in the well the compliance reduces ($S\downarrow$, bulk stiffens), the local clock $\omega_{\text{local}}=\omega\sqrt{S}$ down-regulates; since $E=\hbar\omega$ and $m=E/c^2$, matter in the well weighs less (the mass defect)"* | the **Axiom-4 kernel** `S = √(1−A²)`; the clock law is `W = S^{1/2}`, i.e. `f′(1) = ½` |
| 2 | `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md:28` | *"The genuine local clock rate / gravitational redshift is a slope-1 quantity: $\sqrt{g_{00}} = \sqrt{S} \approx 1 - GM/rc^2$, so $z = GM/rc^2$"* | the **metric lapse-squared** `S = g₀₀ = 1 − r_s/r` |

Numerically, at small `A`:

```
site 1:  √S = (1−A²)^{1/4} = 1 − A²/4 + O(A⁴)        →  F ∝ 1/r³   (dies by §1.2)
site 2:  √S = (1−A)^{1/2}  = 1 − A/2  + O(A²)        →  F ∝ 1/r²   (survives by §1.3)
```

**The two agree only at `A = 0` and `A = 1`.** They differ at *first* order in `A` — the order gravity lives at.

**⚑ The collision is load-bearing downstream.** `saturating-modulus-and-backreaction.md:174-176` states the Stage-4 strong-field target as *"it is the saturation of the frequency down-regulation in the strong field, where $S\to0$ at the yield shell, $\omega_{\text{local}}\to0$ (the clock freezes) and AVE's $\sqrt{S}$ can peel from GR's $\sqrt{1-r_s/r}$"*. **That sentence presupposes site 1's reading** — it names `√S` and `√(1−r_s/r)` as two things that can come apart. On site 2's reading they are the same object and **there is nothing to peel**.

**This companion rules nothing.** A two-`S` resolution (kernel for the constitutive modulus, lapse for the clock) is *available* and would preserve both sites — but **it is not written in the corpus**, and the parent result doc's earlier closing clause asserted it as though it were. That assertion is withdrawn there and is not reinstated here. **Routed to the auditor lane bundled with the `ε₁₁`/`A` collision of `result.md` §2.4** (`eq_axiom_4.tex:10` writes the gravitational strain as `r_s/r`; `:24` and `:56` write `ε₁₁` for the same quantity; the missing factor is `ν_vac = 2/7`).

---

## §3 — THE GR COMPARISON OBJECT, NAMED CORRECTLY

Deliverable 2 computes `F = −∂_r E_∞` with `E_∞ = ħω₀√(1−r_s/r)` and `r` the **Schwarzschild coordinate**. That equals

```
F = −(GMm/r²)(1 − r_s/r)^{−1/2}   =   m·a ,   the STATIC-OBSERVER PROPER FORCE       (10)
```

— the force a local static observer must exert to hold the mass in place. **It is not the force at infinity.** The force applied at infinity through an ideal string is obtained by converting the coordinate derivative to a proper-length derivative, `dl = dr/√(1−r_s/r)`:

```
F_∞ = √(1 − r_s/r) · m·a = GMm/r²      EXACTLY, no correction at any order            (11)
```

(Wald §6.3.) So the lane's result reproduces (10), not (11).

**Consequence for the import statement, scoped.** What CLOCK-1 reproduces exactly is **the `g₀₀` function in Schwarzschild coordinates** — that is the whole content of the "every post-Newtonian order is imported" claim, and it should be stated that way. **The spatial-metric sector is untouched:** the PPN parameter `γ` never enters this construction, is neither imported nor tested by it, and no claim about it follows.

*Machine check:* `matches_GR_static_observer_PROPER_force_EXACTLY = true` with residuals `< 1e-40` at three radii; `force_AT_INFINITY_ratio_expression = "1"` and `force_AT_INFINITY_is_exactly_newtonian = true`, i.e. (11) is verified symbolically as well as asserted.

---

## §4 — THE POLE TEST'S VALIDITY SCOPE

**Banked input** (`port-register.md:93`, not this lane's arithmetic): *"excluded at 9–110σ Hulse-Taylor / 100–1400× the double-pulsar bound"* — **10²–10³×**, for a Reading-A **quadrupole** (`:89`, *"monopole + dipole killed by conservation, but the **quadrupole radiates**"*) radiating at a speed of order `c`.

**Scope law.** Multipole-`ℓ` radiated power carries `(v/c_g)^{2ℓ+1}`, so the exclusion of a pole-bearing completion carries

```
suppression = (c/c_g)^{2ℓ+1} ,      ℓ = 2  ⇒  fifth power                              (12)
```

**At this lane's own forced speed.** Paying the LC-hyperbolic admission price with the only substrate-native inertia candidate forces

```
c_g/c = √(2 ξ_Machian) = 1.2771×10²²                                                   (13)
```

whence, from (12) at `ℓ = 2`:

```
(c/c_g)⁵ = 2.94×10⁻¹¹¹                                                                 (14)
exclusion ratio ≈ 10⁻¹⁰⁷        (order only; digits not banked)                        (15)
```

> **★ ~107 orders BELOW the comparator, instead of ~4 above. A superluminal pole-bearing completion is NOT excluded by pulsar timing.** The constraint *"whatever completes clause G cannot be a radiating line"* holds **only for `c_g ≲ O(c)`**, and must travel with that scope.

**★The two arms, reconciled (corrected 2026-08-11 — the first cut of this paragraph stated the wrong reason).** The review's arithmetic quotes `~1.5×10⁻¹⁰⁷` for (15) and this driver's returns `~2.6×10⁻¹⁰⁷`. They did **not** run on the same central, and the gap is exact arithmetic rather than unexplained residue. The exclusion ratio is a radiated compression fraction `κ²` divided by the observational cap `κ_max² = 1.3×10⁻⁴` (`result.md` §3 item b), so

```
driver arm  : κ² implied by 8974× = 8974 × 1.3×10⁻⁴ = 1.1666
review arm  : κ² = 0.666
1.1666 / 0.666 = 1.7517 = 2.6416×10⁻¹⁰⁷ / 1.5081×10⁻¹⁰⁷                                (16)
```

`κ²` is the O(1)-coupling coefficient the lane's one **not-refuted** Tier-2 MAJOR contests (§5) — the coefficient whose Lagrangian normalisation was fixed by a check structurally blind to it. **The difference between the two arms IS that open coefficient and nothing else.** That is why only the **order** is banked, why neither leading digit is, and why this lane picks neither `κ²`. *(Machine-reconciled: the number check recomputes both arms and (16) from the JSON's own `8974` input.)*

*Machine check (driver `L6`):* (13) recomputed independently from `XI_MACHIAN`; (12) recomputed per `ℓ ∈ {1,2,3}`; (15) bracketed in `[1e-108, 1e-106]`.

---

## §5 — TIER-2 DISPOSITION (restated from the parent; nothing added)

**Provenance, stated plainly:** the per-finding Tier-2 records were not committed by the route lane, which has closed. The table below is a **restatement of `result.md` §5's own aggregate and of the dispositions already written into the parent's body** — it is not an independent record, and no per-finding detail is reconstructed.

| Tier-2 aggregate (`result.md` §5) | Count |
|---|---|
| Verdicts total | 18 |
| CRITICAL | 9 |
| MAJOR, refuted | 8 |
| **MAJOR, NOT refuted** | **1** |

**The 1 not-refuted MAJOR, named:** the **exclusion-arithmetic** finding against `result.md` §1.3's radiated-fraction number — that the route's Lagrangian normalisation was fixed by a check structurally blind to the coefficient, and that the O(1)-coupling bracket was transferred from the envelope lane as a declared deviation. **It stands.** Standing disposition: the exclusion figure is **ORDER-OF-MAGNITUDE ONLY**, its digits are **not banked**, and the `port-register.md:87` Q1-row question is routed with **no recommendation** for the same reason. **This pass adds a second, independent limitation to the same number** — the `(c/c_g)^{2ℓ+1}` scope of §4 — which narrows where the constraint reads at all and is logically independent of the coefficient objection.

**What the Tier-2 caught, as recorded in the parent (§5, unchanged):** (1) a fabricated-by-attribution quote; (2) a stale-blob citation manufacturing a phantom axiom ambiguity; (3) an invented verdict branch routing an arc-level kill into a benign null; (4) a cherry-picked one-of-two data points reported as "verified"; (5) a bench requirement computed for a source the axioms forbid; (6) the common instantaneous-kernel defect that inverted all three D1 stories.

**What the three D1 routes were, at the grade the surviving record supports** (`result.md` §1.1 table — restated, not re-derived, and all three bins WITHDRAWN):

- **R1, variational.** Its Euler–Lagrange equation `∂²ₓ[ρ𝒜_g²ε̈ + κε] = −T₀₀` is an **elliptic spatial operator times a temporal ODE** — the signature of infinite propagation speed. A step source produces `ε₁₁(r,t) = (1−cos ω_b t)·P(r)` at every radius simultaneously.
- **R2, multiple scales.** Refuted by its own slaving map, whose kernel contains the entire transverse `c`-sector (divergence vanishes identically). Its `p = 2.0` leg was reported ANALYTIC and not bookable.
- **R3, slaving map.** Clause G is a **vector** relation; holding it at all times imposes 3 constraints on a fast layer whose longitudinal sector obeys `ρü = f_L`. For a moving source the system is over-determined. The route's clean answer came from projecting the 3-DOF constraint onto its 1-DOF divergence, where the contradiction cancels exactly.

**Common defect:** all three delivered a law with **zero delay at every `ω` and every `r`** — which is the elliptic abstraction re-installed, not completed. Hence `D1 = NOT-DERIVABLE(missing structure enumerated)`.

---

> **Companion provenance.** Written in the 2026-08-11 review-cycle repair pass, after the parent's Tier-2 and after the orchestrator verify whose findings this pass executes. Every equation above is machine-checked in the lane driver and its number check; every quotation is byte-verified two-engine by the committed quote gate, with the axiom text retrieved at a **pinned rev** rather than through a branch name. **This companion carries the pass's NEW derivation content only; it reconstructs no record that was not committed.** Mints nothing, edits no corpus file, rules nothing. **Nothing in this document reads CLEARED.** `[DO-NOT-MERGE]`.
