# FROZEN PREREG — Axiom-4 buckling-kernel: does K4 bond geometry DERIVE S(A)=√(1−A²) (α-free)?

**Date:** 2026-07-02
**Lane:** derivation (foundational; closes the DP-3 arc + attempts the open Q-G47 shape-gate). Analysis + adversarial verification.
**Branch:** `analysis/axiom4-buckling-kernel` (off `origin/main` @ `c9a1188c`)
**Parent arc:** Axiom-4 reduction epic (PR #455) → DP-3 combine-rule (PR #457) → strain reconciliation (PR #458). Grant's steer (2026-07-02): the combine is not a norm — *"what does the K4 bond angle say?"* → the bond is an Euler-buckling strut; `S(A)` is the transverse shear stiffness, argument `A` the axial dilatation load; the L2 "fixed radius" may just be the fixed bond length. **Grant confirmed this hunch.**
**Disciplines:** `ave-prereg`, `substrate-native-check`, `pre-test-physics-check`, `consistency-vs-emergence`.

> **SHA-PIN (Rule-16).** The thesis (§1), discriminator (§3), acceptance checks (§4), and classification axis (§6) are LOCKED before the verdict.

---

## 0. The gate being attempted (the corpus marks it OPEN)

`trampoline-analogy-primer.md:180-192` has the Pythagorean buckling picture — a bond's tip obeys `vertical(A)²+A²=const²` ⟹ `S(A)=√(1−A²)` — but explicitly rules it **"a pedagogical correspondence, NOT a first-principles derivation… a network-level elastic calculation (Q-G47) is required to derive the kernel form from buckling."** Q-G47 (`q-g47-…closure.md`) closed only the **operating point** `u_0*`, NOT the shape. **This derivation attempts to CLOSE that shape-gate** — to upgrade the "pedagogical correspondence" to a first-principles derivation.

## 1. The thesis (Grant-confirmed 2026-07-02; to PROVE or BREAK)

**The Pythagorean "constant" in `vertical²+A²=const²` IS the fixed K4 bond length `ℓ_node` (inextensibility) — an Axiom-1 geometric primitive — so `S(A)=√(1−(A/A_yield)²)` with `A_yield=ℓ_node` is a THEOREM of Axiom-1 bond geometry, α-free.** If so, the "fixed-radius L2 energy constraint" the prior pass called Axiom-4's residual axiom **is not an independent posit** — it is the fixed bond length (Axiom-1). And the cross-grade "combine" is not a norm (L∞ vs L2) but the **Euler-buckling bifurcation**: the axial dilatation (A1) load drives the transverse shear (T2) stiffness `S→0` at the buckling instability (the vertical tangent = the √-law bifurcation onset).

Supporting corpus geometry (α-free, O(1)): the bond is a **pre-compressed spring that Euler-buckles** (`trampoline-framework.md:85`, bowing = helicity); **π² = Euler buckling, E-irrep 2-dim** (`trampoline-framework.md:304`); the **E-irrep soft-shear eigenvalue `(4/3)k_s`** (`q-g47:104`); over-bracing puts the bond midpoint at `A=1` (`secondary-scale-shared-b-node.md:38`).

## 2. Corpus state (ave-prereg)

| Anchor | Content | Bears on |
|---|---|---|
| `trampoline-analogy-primer.md:180-192` | Pythagorean buckling → √(1−A²); "pedagogical, NOT first-principles"; Q-G47 gate OPEN | the gate |
| `trampoline-framework.md:85,304,407` | bond = pre-compressed Euler-buckling spring; π²=Euler; bond-as-spring-under-tension | the mechanism |
| `q-g47:104`, `secondary-scale-shared-b-node.md:31-38` | E-irrep soft shear `(4/3)k_s`; over-bracing `u_0` at bond-midpoint `A=1` | the geometry |
| **`secondary-scale-shared-b-node.md:35` (2026-06-14 walk-back)** | **`u_0*≈0.187` is asserted/back-fit, NOT forward-derived; K=2G is GR-imported** | **the smuggling trap** |
| DP-3 result (PR #457) | combine is per-yield-normalized; cross-grade aggregation underdetermined; √α imported | downstream |
| `def-vyvsn1` | electron A1 at `A=√α`; SYM Pd/water rupture at `√(2α)` | downstream checks |

## 3. The discriminator (LOCKED)

**The buckling √ is first-principles-DERIVED iff the Pythagorean "constant" (inextensibility) is FORCED by Axiom-1, WITHOUT importing K=2G, `u_0*`, or an independent L2-norm posit.** Pre-registered outcomes:

- **Outcome A (gate CLOSES — the strong result).** The Pythagorean constant = the fixed bond length `ℓ_node` (Axiom-1); inextensibility is FORCED by the Axiom-1 stretch-stiff / bend-soft hierarchy (`k_stretch ≫ k_bend`: the bond bows without stretching — Keating covalent bond-stretch stiff, Cosserat couple-stress bend soft); NO K=2G / `u_0*` used; α-free. ⟹ `S(A)=√(1−A²)` is a **theorem of Axiom-1 bond geometry**, and the L2 norm demotes from residual-axiom to Axiom-1-consequence. The primer's "pedagogical correspondence" upgrades to a derivation; the Q-G47 shape-gate closes.
- **Outcome B (partial — the honest expected).** The single-bond Pythagorean gives the √ FORM, but the "constant"/inextensibility (or the exact `A_yield=ℓ_node` identification, or the network-level closure the primer demands) requires an assumption **not forced by Axiom-1 alone** (e.g. the stretch-stiff hierarchy is posited, or the network elastic calc re-introduces a norm). ⟹ the primer's "pedagogical correspondence, not first-principles" verdict STANDS, sharpened: named exactly which step is the residual.
- **Outcome C (smuggled / breaks — retract).** The √ requires K=2G (GR-imported), the back-fit `u_0*`, or the L2-norm re-enters as an independent posit; OR the naive Euler stiffness (linear `1−P/P_crit`) is conflated with the inextensible-rod projection (√); OR inextensibility is false (the bond stretches, breaking the exact √). Report the negative; do NOT force the reduction.

**Critical distinction to hold (a known trap):** the Euler *effective lateral stiffness* is **linear** `k(P)=k_0(1−P/P_crit)`, NOT the √. The √ comes ONLY from the **inextensible-rod tip projection** (fixed arc-length → Pythagoras). The derivation must use the geometric projection, and the load-bearing claim is that the fixed length is Axiom-1. Conflating the two is Outcome C.

## 4. Acceptance checks (LOCKED — downstream, NOT inputs)

The derived α-free buckling kernel must, as **consequences** (not refits): (1) give the vertical tangent at `A=1` as the buckling bifurcation √-law onset; (2) be **consistent** with the electron `A=√α` operating point and the SYM `√(2α)` rupture as *downstream projections* of the geometry (the √α/√(2α) enter via the yield calibration, NOT the shape); (3) reproduce the Maxwell `S→1` small-A limit. If the √α/√(2α) must be *input* to get the shape, that is Outcome C (circular).

## 5. Method / lanes (LOCKED)

- Analysis + adversarial verification. Small numpy geometry checks (the inextensible-rod projection vs Euler-linear-stiffness; the `(4/3)k_s` E-irrep) in agent scratch. Engine READ permitted (the K4 Cosserat moduli / Keating discretization) to characterize the stretch-vs-bend stiffness hierarchy.
- **substrate-native-check:** the derivation is K4-bond-geometry native (Euler buckling, Keating stretch/bend, Cosserat couple-stress); the rupture is a Γ=−1 boundary / bifurcation (CP10), NOT a bulk force; guard the A1⊥T2 grade orthogonality (no shared phasor).
- **The super-adversary's sole job:** show the √ is **smuggled** — either (a) inextensibility is assumed not Axiom-1-forced, (b) K=2G / `u_0*` sneaks in, or (c) the L2-norm re-enters. The corpus's standing "pedagogical, not first-principles" verdict is the null hypothesis; overturning it requires surviving this attack.
- **do-not-force-a-positive:** Outcome A would be the strongest result of the whole arc — which is exactly why it must survive the smuggling super-adversary, not be assumed. **retract-don't-refill.**

## 6. Classification commitment (consistency-vs-emergence)

If Outcome A: the kernel SHAPE becomes a **theorem of Axiom-1 bond geometry** — name the NEW primitive explicitly (the fixed bond length `ℓ_node` + the Axiom-1 stretch-stiff/bend-soft hierarchy) and verify it traces to Axiom 1 and is NOT already an independent posit. This would move Axiom-4's residual from "the L2-norm posit" to "Axiom-1 geometry" — a genuine content reduction (but still NOT a count reduction: Axiom 1 carries the residual). Do NOT inflate: if the hierarchy is posited (Outcome B), classification stays at the primer's "pedagogical correspondence" ceiling.

## 7. Decision points → Grant

1. **If Outcome A** — closing the Q-G47 shape-gate + demoting the L2 norm to Axiom-1 geometry is a canonical change to `trampoline-analogy-primer.md:190` ("Axiom 4 remains postulated") and the axiom-register. Recommend, Grant rules.
2. **If Outcome B/C** — report the sharpened residual / the negative; the primer's standing verdict holds.

## 8. Outputs

This prereg + `2026-07-02_axiom4-buckling-kernel_result.md` (the buckling derivation, the inextensibility/Axiom-1 audit, the smuggling-adversary outcome, the downstream √α/√(2α) checks, the classification). Branch + PR (research doc). Report to Grant with the verdict.
