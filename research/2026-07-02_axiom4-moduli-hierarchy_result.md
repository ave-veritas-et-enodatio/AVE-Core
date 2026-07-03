# RESULT — Axiom-4 final gate: inextensibility FAILS (Outcome C/NEGATIVE); the √ form is robust but its yield-anchor inherits from GR-imported K=2G

**Date:** 2026-07-02
**Lane:** derivation (the FINAL gate of the Axiom-4 arc; prove-or-disprove). Analysis + adversarial verification.
**Branch:** `analysis/axiom4-moduli-hierarchy` (off `origin/main` @ `c9a1188c`)
**Prereg:** [`2026-07-02_axiom4-moduli-hierarchy_prereg.md`](2026-07-02_axiom4-moduli-hierarchy_prereg.md) (frozen @ `f372a159`)
**Parent:** buckling-kernel result (PR #459, Outcome B) — the √ is the fixed-length bond projection GIVEN inextensibility; this gate tests whether inextensibility (`k_stretch ≫ k_bend`) is Axiom-1-forced.
**Method:** 3 derive lenses (ρ-value+provenance / arc-length conservation / elastica-regime-save) → per-lens adversarial verify → an **Outcome-A-rescue super-adversary** tasked to *save* inextensibility via the elastica argument. 10 agents. All numerics + provenance citations re-verified against `origin/main`.

---

## 0. VERDICT (one line)

**Inextensibility is NOT Axiom-1-forced and NOT achieved at the vacuum operating point — Outcome C (inherits GR) / NEGATIVE (extensible). The Outcome-A rescue (Euler elastica) is decisively killed.** But the arc closes on a clean, honest note: the **√ FORM is *more* robust than the buckling result showed** — for *any* finite ρ, a compressible K4 strut sits at a self-consistent fixed arc-length `arc* = 4ρ/(4ρ+1)·ℓ_node`, so `S(A)=½·arc*·√(1−(A/arc*)²)` is an **exact quarter-arc in the renormalized amplitude `u=A/arc*`**. The √ shape needs neither `ρ≫1` nor the elastica limit. **What fails is the Axiom-1 closure:** the yield anchor is `arc* ≈ 0.89–0.96·ℓ_node` (4.5–11% short of the bare bond length), and `arc*` inherits from the **GR-imported K=2G** (ρ is K=2G-set). So Axiom-4's shape stays **SHAPE-DERIVED (conditional)**, count **4** — the √ *form* is a robust α-free theorem, but its *anchor* is a GR-imported value, not Axiom-1.

---

## 1. Why Outcome A is killed (the elastica got its real shot)

The super-adversary was tasked to *save* inextensibility via the strongest pro-A argument — the Euler **elastica** is inextensible by construction, so if the K4 bond qualifies, the √ is exact and ρ is irrelevant to the shape. It could not:

- **`ρ = k_a/k_s` IS the slenderness².** `ρ=2` → aspect ratio `ℓ/t=√2≈1.41` (a *stubby* strut, thickness ~ length); `ρ=5.3` → 2.30. Inextensibility (arc-length conserved to leading order) needs a *thin* rod, `ρ=(ℓ/t)²≫1`. A chunky strut of aspect 1.4–2.3 bends **and** stretches comparably. It is a **compressible strut, not an elastica.**
- **The elastica regime is affirmatively FORBIDDEN by K=2G.** A true elastica needs `ρ=20–100` → `K/G=6.6–31.6 ≫ 2`. The vacuum is locked at `K/G=2` (`ρ≈2–5.3`). Being an elastica would require *abandoning* the GR trace-reversal K=2G.
- **`ℓ_c/ℓ_node=√6` HURTS, it doesn't help.** `ℓ_c²=γ/G` is a *within-bend-sector* ratio (curvature vs shear modulus, both die as `k_s→0`) — **orthogonal** to the stretch/bend ratio `ρ=k_a/k_s` that inextensibility needs. A stiff couple-stress makes the bond *resist bending*, pushing the over-braced misfit into the **stretch** channel → arc-length *less* conserved. (The √6 tell, which looked like it could cut both ways, cuts *against*.)
- **Near-threshold / small-A give no save.** The arc-length deficit is a constant `O(1/ρ)` radius shrink that *floors* at `A=0` — worst near the yield end (`A→1`), which is exactly where Axiom 4 lives (the vertical-tangent saturation).

## 2. The provenance (Outcome C)

`ρ` is **not Axiom-1-forced.** The sub-isostatic `z=4 < 2d=6` Maxwell count makes `K/G` a ratio of two *independent* stiffnesses (`k_a` bulk/stretch, `k_s` shear/bend); Axiom-1 K4 geometry fixes only the **FORM** `K/G=f(ρ)`, **never the VALUE** (`k2g-crystalline-provenance_result.md:60-62`, verbatim: *"geometry fixes the form; it cannot fix the value; to land on K=2G you must supply ρ\* from outside"*). The vacuum `ρ` is pinned by `K=2G` — the GR trace-reversal condition (`q-g47:28` "required by General Relativity"; `u_0*≈0.187` retracted 2026-06-14 as back-fit). So even the modest `ρ=2` (`⟺ k_a=2k_s ⟺ K=2G`) inherits from GR. **Outcome C.**

## 3. The shape-save (the honest positive — M-3, both verifiers CONFIRMED)

Modeling the K4 bond substrate-natively as a 2-DOF strut (axial stiffness `k_a`, transverse bend `k_s`; tent kinematics `arc=2√((A/2)²+S²)`, `U=½k_a(arc−ℓ)²+½k_s S²`) and minimizing over the bow `S` at fixed axial projection `A` gives an **exact analytic result**: the bowed bond sits at a **fixed arc-length `arc* = 4ρ/(4ρ+1)`, independent of A**. Therefore

$$ S(A) = \tfrac12\sqrt{arc^{*2}-A^2} = \tfrac12\,arc^*\sqrt{1-(A/arc^*)^2}, $$

an **exact quarter-arc √ in the renormalized amplitude `u=A/arc*`, for ALL finite ρ** (grid-verified to 5 digits: `ρ=2→arc*=0.8889`; `ρ=5.3→arc*=0.9550`; `ρ=20→0.9877`; `ρ=100→0.9975`). **The √ FORM is regime-robust** — it does not require `ρ≫1`, does not need the elastica limit, and is exact (not approximate) once the amplitude is normalized to the true operating arc-length. *(Caveat: the prefactor `4ρ/(4ρ+1)` is specific to the tent 2-segment kinematic; a continuum-elastica curvature integral could shift the prefactor. The **structural** conclusions — `arc* < ℓ_node` by `O(1/ρ)`, and the √-in-`u` exactness — are model-robust.)*

**But this saves the SHAPE, not Outcome A:** (a) the Axiom-1-forced anchor `A_yield=ℓ_node` is **broken** — the true yield sits at `arc* ≈ 0.89–0.96·ℓ_node` (4.5–11% short); (b) `arc*=4ρ/(4ρ+1)` inherits from GR-imported K=2G (`ρ` is K=2G-set). So the exact √ is anchored to a GR-imported value, not Axiom-1.

## 4. Deviation quantified (a forward, falsifiable statement)

The buckling result's `A_yield=ℓ_node` is refined: the true yield anchor is `arc*`, so `S(A)` measured against the *bare* `ℓ_node` deviates from `√(1−A²)` by a constant `O(1/ρ)` radius deficit `ε_c=1−arc* = 1/(4ρ+1)`: **11.1% at `ρ=2`, 4.5% at `ρ=5.3`** (raw-`S` deviation reaches ~50% near `A→1` at `ρ=2`, where the true bow collapses at `A=arc*<1`). This is an AVE-internal prediction: the saturation kernel's *effective yield strain* is `arc*<ℓ_node`, set by the same `ρ` that sets K=2G.

## 5. Classification (consistency-vs-emergence) + the arc's meta-finding

- **DERIVED (α-free, robust):** the √ FORM `√(1−(A/arc*)²)` — a geometric theorem of *any* finite-ρ compressible strut at its self-consistent operating arc-length. A genuine **Class-B/consistency** structural result, more robust than "exact given inextensibility."
- **IMPORTED (value):** the yield anchor `arc*=4ρ/(4ρ+1)·ℓ_node` — inherits from GR-imported K=2G. NOT Axiom-1.
- **Net:** Axiom 4's shape stays **SHAPE-DERIVED (conditional)**, count **4**. Inextensibility (`k_stretch≫k_bend`) is *neither Axiom-1-forced nor achieved* — un-rescuable by the elastica route.

**This is the fourth+ instance of the corpus's own meta-finding — AVE forces FORMS, imports VALUES.** The kernel √ FORM is forced (geometric, α-free, robust across ρ); the VALUE that anchors it (`arc*`, via K=2G) is imported. The arc that began "is the L2 norm a posit?" ends: *the norm is the geometry (a robust √ constraint), but the geometry's anchor is a GR-imported value.*

## 6. The arc, complete (residual fully characterized)

| Stage | Axiom-4 residual |
|---|---|
| prior pass | "the L2 norm / fixed-radius energy constraint" (abstract posit) |
| epic #455 | the cross-sector combine rule |
| DP-3 #457 | per-yield-normalized; cross-grade aggregation underdetermined |
| buckling #459 | there's no combine — a load-response bifurcation; shape α-free GIVEN inextensibility; residual = `k_stretch≫k_bend` |
| **moduli (this)** | inextensibility FAILS (`ρ=slenderness²∈[2,5.3]`, stubby, K=2G-forbidden from being an elastica); the √ **form is robust for any ρ**, but its **yield anchor `arc*` inherits from GR-imported K=2G** — FORM-derived / VALUE-imported |

**The residual is now fully characterized and the arc is closed:** Axiom 4's shape is a robust α-free geometric √; what stays axiomatic (imported) is the yield anchor `arc*`, the same GR-imported K=2G value that anchors gravity throughout the framework. No further reduction is available without forward-deriving K=2G itself (a separate, standing open problem — the `Chain B′` flip-test in the interlock register).

## 7. Decision points → Grant

1. **Final canonical status of Axiom-4's shape:** SHAPE-DERIVED (conditional) — the √ form is a robust geometric theorem, the yield anchor `arc*` is GR-imported. Recommend the axiom-register `residual_content` be sharpened once more from "`k_stretch≫k_bend`" to "**the yield anchor `arc*=4ρ/(4ρ+1)·ℓ_node`, inherited from GR-imported K=2G** (the √ form itself is forced)." Grant rules.
2. **The forward prediction (§4):** the effective yield strain is `arc*<ℓ_node` (4.5–11% short) — a falsifiable AVE-internal statement. Canonize? Grant rules.
3. **The only remaining reduction** would be forward-deriving K=2G from Axiom-1 (currently GR-imported; the standing `Chain B′` problem) — out of this arc's scope.

## 8. Outputs

This result + the frozen prereg, via a branch + PR (research doc, **NOT a canon change**).
