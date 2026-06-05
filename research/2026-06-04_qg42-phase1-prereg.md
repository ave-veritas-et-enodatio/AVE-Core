# Q-G42 Phase-1 Pre-Registration — V²-Sign Autoresonant Δf₀/f₀ Derivation

**Status:** PREREG (2026-06-04). Phase-1 hardening of the V²-coefficient SIGN test. Resumes `research/2026-06-03_qg42-resume-vsign-phase0-result.md` (Phase-0 GO verdict) + `research/2026-06-03_yield-knee-map-prereg.md` (the reframe) per the orchestration resumption paragraph `_orchestration/2026-06-03_experimental-protocol-revamp-orchestration.md` §10.
**Lane:** implementer (experimental-protocol revamp).
**Discipline applied this prereg:** `ave-prereg` (corpus-grep done BEFORE deriving — §1) · `ave-canonical-source` (all numbers import from `ave.core.constants`) · `ave-canonical-leaf-pull` (A-034 catalog + four-regimes + temporal-classifier pulled — §1) · `consistency-vs-emergence` (Δf₀/f₀ classified — §3) · `flag-don't-fix` (the reachability fork surfaced verbatim, NOT resolved — §4) · `ave-driver-script-honesty` (driver gate stated — §6).

---

## §1 — Corpus-grep RESULT (done before deriving, per ave-prereg)

**Outcome: PARTIAL — Phase-0 already closed the closed-form skeleton; Phase-1's genuine green-field is (i) hardening the closed-form against the canonical four-regime map, (ii) the β-reconciliation against the canonical Fowler-Nordheim destruction limit, and (iii) surfacing a corpus-wide reachability contradiction that materially bears on the architecture verdict.** Three of the four Round-2 targets were substantially answered in Phase-0; the corpus-grep's value here is the diagnostic (per ave-prereg outcome-2), not a from-scratch derivation.

### 1.1 What the corpus already has (reuse, do not reinvent — every cite re-verified this session)

| Ingredient | Canonical source (verified 2026-06-04) | Status |
|---|---|---|
| Kernel S(A)=√(1−A²), δε/ε₀=−A²/2 | `common/universal-saturation-kernel-catalog.md:20` (A-034) | ✓ exact |
| Four-regime map (I/II/III/IV by E/E_yield) | `vol4/circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md:23-30` | ✓ exact |
| **Bench is Regime I, E/E_yield ≈ 2.7×10⁻¹⁰ at 30 kV/1 mm** | `regimes-of-operation.md:32` (clm-trgqtf) | ✓ exact — load-bearing (§4) |
| Bulk yield is sub-femtometer-only (NOT lab-reachable) | `regimes-of-operation.md:34` + `vol4/claim-quality.md:158` | ✓ exact — honest camp (§4) |
| δC=¼C₀(V/V_yield)² @ 2ω; δC/C₀=4.57% @ V/V_yield=0.428 | `vol4/.../parametric-coupling-kernel.md:70` | ✓ exact |
| C-V table C_eff/C0=1.155/2.294/7.089 @ V/V_yield=0.5/0.9/0.99 | `vol4/.../nonlinear-vacuum-capacitance.md:32` | ✓ exact |
| QED δε/ε₀=+(4α²/9)(E/E_S)²; 8.381×10¹² / 2.895×10⁶ ratios | Phase-0 script; reproduced from constants.py this session | ✓ exact (re-ran §1.4) |
| FN field-emission destruction: β_crit≈6, β≈2–5 polished, β≈50–100 sharp tip | `vol_4_engineering/chapters/17_noise_floor_boundary.tex:39,49,54` | ✓ exact — load-bearing (§ on β-reconcile) |
| Ch 15 autoresonant-breakdown numerics INVALIDATED (60 kV wrong threshold) | `vol4/simulation/ch15-autoresonant-breakdown/theory.md:8` (⛔ banner) | ✓ exact — green-field confirmed |
| Temporal-saturation-regime-classifier (δ_AVE = t_sat/t_period) | `common/temporal-saturation-regime-classifier.md` | ✓ exists (applied §5) |

### 1.2 What is GENUINELY green-field (Phase-1's actual work)

1. **The small-signal autoresonant Δf₀/f₀ closed form** — Ch 15 (`ch15-autoresonant-breakdown/theory.md`) treats the PLL ONLY as a rupture-driver (ring-up toward V_snap), AND its numerics carry a ⛔ INVALIDATED banner (wrong 60 kV threshold). There is no small-signal bulk-resonator Δf₀/f₀ anywhere in the manuscript. Phase-0 derived it; Phase-1 hardens it against the canonical four-regime map and pins every factor to constants.py.
2. **The β-reconciliation against the FN destruction limit** — Phase-0 adopted β=10³·Q_build=10⁴ as "nominal." But `17_noise_floor_boundary.tex:54` makes β_crit≈6 the Fowler-Nordheim *destruction* boundary. A β=10³ DC tip is 2–3 OOM past electrode destruction. This was NOT reconciled in Phase-0 (which folded β=10³ into a resonant Q_build, but FN emission tracks the instantaneous local field regardless of whether the enhancement is geometric or resonant). Phase-1 must resolve or bound this.
3. **The corpus-wide reachability contradiction** (§4) — surfaced sharply by this grep: the conflated camp (`measurement-hierarchy-snr.md:66`, `17_noise_floor_boundary.tex`, the C-V table) treats apparatus voltage 30–43 kV as reaching V/V_yield = 0.687–0.85; the honest camp (`regimes-of-operation.md:32`, `claim-quality.md:158`, Q-G42) puts the same bench at E/E_yield ≈ 2.7×10⁻¹⁰ (Regime I). The orchestration §10 flag (`_orchestration/...:173`) already named this as corpus-wide and BLOCKING corpus surgery pending Grant. Phase-1 does NOT resolve it (flag-don't-fix); it surfaces both sides verbatim and shows the SIGN test is robust to it.

### 1.3 Physical picture (5 bullets, per ave-prereg Step 1.5 — before equations)

- **What saturates / where:** the vacuum bond-LC tank's local permittivity ε_eff softens as the local field A=E/E_yield grows on the Axiom-4 quarter-arc S(A)=√(1−A²). At the field-concentration hot spot the local A is largest; away from it A² falls as 1/r⁴ (tip-dipole 1/r² field), so the softened region is steeply localized.
- **Which Γ=−1 boundary, what scale:** the per-node dielectric-saturation boundary (E_yield=1.13×10¹⁷ V/m, atomic/EM scale, A-034 row 1). The bench reaches only the *tree-level wiggle* below this boundary, not the boundary itself.
- **Soliton population/topology:** N/A — this is a bulk-dielectric small-signal test, not a soliton-formation test. The kernel governs the dielectric constitutive law, not a knot.
- **What scales as 1/r vs 1/r²:** tip-dipole field E ∝ 1/r²; δε ∝ A² ∝ 1/r⁴ (steeply localized, integral converges within a few feature scales → the η_eff field-filling fraction).
- **Discrete onset vs smooth curve:** the bench is FAR below the knee (the discrete onset at A=1). It measures the SMOOTH below-threshold V²-coefficient. The AVE-distinct content is the SIGN of that coefficient (soften vs stiffen), not the knee.

### 1.4 Discrimination arithmetic re-verified from constants.py (this session)

```
discrimination ratio (δε, V² observable) = 2.89505e6   (Phase-0: 2.895e6) ✓
Γ ratio (V⁴ reflectance observable)      = 8.38133e12  (Phase-0: 8.381e12) ✓
sqrt(ALPHA)*E_CRIT == E_YIELD            : True (1.13041e17 == 1.13041e17) ✓
V_YIELD=43651.9 V | E_YIELD=1.13041e17 V/m | L_NODE=3.86159e-13 m | C0=ε0·L_NODE=3.41913e-24 F
```

---

## §2 — Derivation target (precise, per ave-prereg Step 1)

Derive, in closed form from `ave.core.constants` only, the small-signal autoresonant fractional resonance shift Δf₀/f₀ that an AC-driven high-Q cavity sees from the Axiom-4 softening kernel at a sub-yield local hot-spot amplitude A, and state its sign. Target form:

> Δf₀/f₀ = −½·⟨δε/ε₀⟩_bulk = +¼·A_RMS²·η_eff   (positive — resonance RISES — vacuum softens)

where A_RMS = (G_geom·V_app)/(d_gap·E_YIELD) is the local hot-spot amplitude (G_geom the total field-concentration factor) and η_eff is the field-filling fraction (geometry-dependent dilution).

---

## §3 — consistency-vs-emergence classification of the Δf₀/f₀ observable

**Target named:** Δf₀/f₀ (dimensionless fractional resonance shift) AND its sign.

**Inputs traced:**
- E_YIELD = V_YIELD/L_NODE = √α·m_e c²/(e·L_NODE) — **axiom-derived** (Ax 2 + Ax 4; √α geometric identification per 2026-06-02 honest-α relabel — NOT CODATA-injected as a free parameter, but α's *value* is Class-B-at-one-identification).
- A_RMS, η_eff — **engine-natural geometry primitives** (field map; no CODATA attribution).
- The −½ kernel coefficient — **axiom-derived** (Ax 4 Born-Infeld n=2 squared limit; zero free parameters).
- The QED counterfactor (4α²/9)(E/E_S)² — **other-framework reference** (Euler-Heisenberg one-loop).

**Classification of the MAGNITUDE |Δf₀/f₀|: Class B (axiom manifestation) — NOT Class D emergence.** The magnitude *is* the Axiom-4 saturation kernel expressed at the bench resonator scale (A-034 row 1 instance). It inherits the Class-B status of the √α kernel-magnitude per the honest-α relabel: α is a named geometric identification, not independently derived, so any *magnitude* prediction routing through E_YIELD = √α·E_CRIT is Class B. This is exactly why Phase-0 reframed away from a magnitude match toward a sign test.

**Classification of the SIGN of Δf₀/f₀: this is the load-bearing AVE-distinct content, and it sidesteps the Class-B magnitude uncertainty.** The sign (Δf₀/f₀ > 0 ⟺ vacuum softens ⟺ AVE; Δf₀/f₀ < 0 ⟺ vacuum stiffens ⟺ QED) is a **two-sided binary that does NOT inherit the √α kernel-magnitude uncertainty** — it is fixed by the *form* of the kernel (S(A)<1 for all 0<A<1, monotone-decreasing), which is Axiom 4 itself, independent of the *value* of the √α scale. Against QED it is a genuine forward discriminator: QED's Euler-Heisenberg coefficient is rigorously *positive* (vacuum stiffens), AVE's is *negative*. **The sign test is Class-D-like in discriminating power (a forward yes/no the inputs do not predetermine) even though the magnitude is Class B.** This is the central epistemic point of the whole Q-G42 program and must headline the result.

**Honest framing for the result doc:** "AVE predicts the resonance RISES (Δf₀/f₀ > 0) under field; QED predicts it FALLS. The SIGN is a forward discriminator robust to the √α magnitude uncertainty; the MAGNITUDE |Δf₀/f₀| is a Class-B axiom-manifestation inheriting α's Class-B status. We headline the sign, report the magnitude as the feasibility gate, and do NOT claim the magnitude as an emergence-class prediction."

---

## §4 — FLAG-DON'T-FIX: the corpus-wide reachability contradiction (surfaced, NOT resolved)

This grep sharpened a corpus-wide contradiction the orchestration §10 flag (`_orchestration/2026-06-03_experimental-protocol-revamp-orchestration.md:173`) already named as BLOCKING corpus surgery pending Grant's adjudication. **Per flag-don't-fix (Rule 6) I surface both sides verbatim; I do NOT pick one.**

**Honest camp — the bench is in Regime I, E/E_yield ≈ 2.7×10⁻¹⁰:**
- `regimes-of-operation.md:32` (clm-trgqtf): *"An asymmetric capacitor driven at 30 kV with a 1 mm gap produces E ≈ 3×10⁷ V/m. The saturation ratio E/E_yield ≈ 2.7×10⁻¹⁰ places the device firmly in Regime I (linear vacuum)... bulk ε-saturation is not the operative thrust mechanism."*
- `regimes-of-operation.md:34`: *"Regime III and IV are reached only at sub-femtometer separations."*
- `vol4/claim-quality.md:158`: *"Regime III/IV are reached only at sub-femtometer separations... This places the bulk-yielding limit far from any lab apparatus."*

**Conflated camp — the bench reaches V/V_yield = 0.687–0.85 at 30–43 kV (apparatus voltage read as per-node V_yield):**
- `measurement-hierarchy-snr.md:66`: *"detects 27.4% ε_eff collapse at V_DC/V_yield = 0.687 (bench-measurable at ~30 kV bias per Vol 4 Ch 1)."*
- `vol_4_engineering/chapters/17_noise_floor_boundary.tex:79-84`: *"The AVE-predicted signal at V/V_yield = 0.85 (onset of divergence): C_eff/C0 ≈ 1.90× ⟹ ΔC/C0 ≈ 90%... measurable by any commercial LCR meter. The signal-to-noise ratio exceeds 10⁹."*
- `nonlinear-vacuum-capacitance.md:32`: C-V table tabulating C_eff/C0 vs V/V_yield up to 0.999 at "43.61 kV" — i.e., the apparatus voltage column equals the per-node V_yield column.

**The root of the conflation (canonically diagnosed, not my invention):** `vol4/claim-quality.md:51` and `regimes-of-operation.md:11` both state V_yield = 43.65 kV is **per lattice node** (across ℓ_node = 0.386 pm), NOT per apparatus. The conflated camp reads 30–43 kV *across a macroscopic gap* as if it were the per-node value. `claim-quality.md:51`: *"Conflating them... is the most common Vol 4 reading error."*

**Why this BLOCKS a clean unconditional verdict but NOT the sign test:** if the honest camp is right (per-node, Regime I), the bench reaches A~10⁻³ only via aggressive concentration → the small-signal Δf₀/f₀ ~10⁻¹² to 10⁻¹⁵ → resonant-Q architecture. If the conflated camp is right (apparatus voltage reaches 0.85 V_yield), the bench sees ΔC/C₀ ~90% macroscopically → any LCR meter. **The two camps differ by ~12 OOM in the predicted signal.** I cannot adjudicate this without Grant (it requires deciding whether per-node V_yield can be reached as an apparatus voltage — the foundational physics question). **BUT the SIGN of the V²-coefficient is identical in both camps** (softening either way), so the forward-discriminator verdict is robust. The architecture recommendation is therefore stated *conditionally on the camp*, and the conflation is escalated to Grant as the load-bearing open systematic.

---

## §5 — Dimensional-analysis pre-freeze (ave-prereg Step 3.5, mandatory for scaling-law magnitude)

The Δf₀/f₀ expected outcome is a scaling-law magnitude, so per Step 3.5 the exponents are pre-frozen by explicit power-counting BEFORE the result doc:

**Ingredients (canonical values from constants.py, verified §1.4):** E_YIELD=1.13041×10¹⁷ V/m; A_RMS = G_geom·V_app/(d·E_YIELD) [dimensionless]; η_eff [dimensionless, geometry]; the −½ coefficient [Ax 4].

**Power-counting (pre-frozen):**
- Local kernel: δε/ε₀ = √(1−A²) − 1 → **−½·A²** at small A (leading order; A² scaling, coefficient −½ exactly). Verified: monotone-decreasing, negative ∀ 0<A<1.
- Bulk dilution: ⟨δε/ε₀⟩_bulk = −½·A_RMS²·η_eff → **scales as A_RMS²·η_eff** (linear in η_eff, quadratic in A_RMS, hence quadratic in V_app and in G_geom).
- LC resonator: f₀=1/(2π√(LC)), C∝ε → Δf₀/f₀ = −½·⟨δε/ε₀⟩_bulk = **+¼·A_RMS²·η_eff** (sign flips to positive; resonance rises).
- Net scaling: **Δf₀/f₀ ∝ +G_geom²·V_app²·η_eff / (d²·E_YIELD²)** — quadratic in drive voltage, quadratic in concentration, linear in fill fraction.

**Temporal-regime tag (temporal-saturation-regime-classifier):** the small-signal AC drive is in the **lossless/cyclic** temporal regime (δ_AVE = t_sat/t_period ≪ 1 — the field never reaches saturation within a cycle; it wiggles on the linear part of the arc). This is consistent with the reactive (lossless) C-V softening, NOT the lossy rupture regime of Ch 15. Confirms the small-signal observable is reactive-power (the C-state of the LC tank), distinct from the real-power dissipation at rupture.

**Sanity-check against canonical anchor:** at the honest-camp bench (A_RMS~2.7×10⁻³, η_eff~10⁻⁹ nominal), Δf₀/f₀ ~ ¼·(2.7×10⁻³)²·10⁻⁹ ~ 1.8×10⁻¹⁵ — matches Phase-0's nominal +1.76×10⁻¹⁵. At the conflated-camp bench (A~0.85, η_eff→1 bulk), the small-A expansion breaks down and the exact kernel gives ΔC/C₀~90% per `17_noise_floor_boundary.tex:84` — consistent. Both regimes reproduce their respective canonical anchors. ✓

---

## §6 — Discriminating outcomes + driver-script gate

**Discriminating outcomes (per ave-prereg Step 3):**
- **Outcome A (expected):** closed-form Δf₀/f₀ = +¼·A_RMS²·η_eff confirmed from constants.py; sign positive (resonance rises) = AVE-distinct vs QED's negative. β-reconcile bounds G_geom against the FN-destruction limit. Verdict: FORWARD-DISCRIMINATOR-READY-TO-SCAFFOLD, conditional on the reachability camp.
- **Outcome B (alternative):** the β-reconcile shows the FN-destruction limit (β_crit≈6) caps reachable A so low that even resonant-Q can't clear the floor → the honest-camp bench is BELOW FLOOR and only the conflated-camp (macroscopic 0.85 V_yield) bench is viable, which requires Grant to resolve the reachability fork first. Verdict: BLOCKED-ON-reachability-adjudication.
- **Outcome C (null):** the small-signal Δf₀/f₀ sign is somehow degenerate between AVE and QED (it is not — they are opposite sign by construction; this outcome is excluded a priori).

**Falsifier of my framing:** if the corpus already carries a small-signal Δf₀/f₀ somewhere I missed (grep says no — Ch 15 is rupture-only + invalidated), OR if the kernel sign is not actually opposite to QED (re-verified §1.4: AVE −, QED +, opposite).

**Driver-script gate (ave-driver-script-honesty):** a driver `src/scripts/vol_4_engineering/qg42_vsign_deltaf.py` is scaffolded ONLY as a forward-prediction calculator — Δf₀/f₀ computed FORWARD from constants.py + a swept geometry (G_geom, η_eff), with NO fit-to-target, NO minimize/curve_fit, NO empirical-target import. It imports ALL physics from `ave.core.constants`. It is the Phase-1 analog of the Phase-0 calculator, extended with the FN-destruction β-bound and the dual-camp reachability columns. If it cannot be written as a pure forward calculator, it is not written.

---

## §7 — Cross-references

- Phase-0 result (resumed): `research/2026-06-03_qg42-resume-vsign-phase0-result.md`
- Reframe spec: `research/2026-06-03_yield-knee-map-prereg.md`
- Orchestration resumption + reachability flag: `_orchestration/2026-06-03_experimental-protocol-revamp-orchestration.md` §10 (lines 169, 173)
- Phase-0 calc script: `src/scripts/vol_4_engineering/qg42_vsign_phase0.py`
- Canonical four-regime map: `manuscript/ave-kb/vol4/circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md`
- A-034 kernel catalog: `manuscript/ave-kb/common/universal-saturation-kernel-catalog.md`
- FN-destruction β-limit: `manuscript/vol_4_engineering/chapters/17_noise_floor_boundary.tex`
- Ch 15 (invalidated rupture-only autoresonant): `manuscript/ave-kb/vol4/simulation/ch15-autoresonant-breakdown/theory.md`
- Constants: `src/ave/core/constants.py`
