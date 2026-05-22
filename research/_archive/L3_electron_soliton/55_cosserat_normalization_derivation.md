# 55 — Cosserat Normalization Derivation (A1 Resolution)

> ## ⚠ SUPERSEDED 2026-04-23
>
> **This doc's R3 "dual-accessor / K4-outlier" conclusion is wrong.** It missed [Vol 4 Ch 1:711](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L711):
>
> > "Subatomic-scale simulations (e.g., bond energy solvers, Yang-Mills confinement) should override with v_yield=V_SNAP (≈ 511 kV)."
>
> VacuumEngine3D is subatomic-scale (K4 lattice at ℓ_node = Compton wavelength, pair-production use case). Under the subatomic override, **V_yield ≡ V_SNAP**, and the engine's `A² = V²/V_SNAP²` IS canonical `r² = V²/V_yield²` per Vol 1 Ch 7:12's universal form — **not** a macro-outlier needing dual accessors. Both Vol 1 Ch 7:104 (`r = V/V_yield`) and Vol 4 Ch 1:711 (`v_yield override to V_SNAP`) are correct; V_yield just takes different numerical values at different scales.
>
> **TKI verification closes under R4:** σ_yield = V_yield·e/ℓ_node³ with subatomic V_yield = V_SNAP gives σ_yield = m_ec²/ℓ_node³ = 1 in natural units; with G=1, ε_yield = σ_yield/G = **1 exactly** — matching the engine's current value. Under R3's macroscopic V_yield = √α·V_SNAP, ε_yield comes out to √α (off by 1/√α). The engine's ε_yield = 1 is **TKI-derived under R4**, not an empirical placeholder as this doc §5 claimed.
>
> **Vol 1 Ch 7:115 / :130 "inconsistency"** (flagged in §3, §10.3 below): is **not a manuscript defect** — it's scale-dependence. Vol 1 Ch 7:115 at r=1 describes AVE's pair-production onset in native convention (where V_yield and Schwinger collapse at subatomic scale). Vol 1 Ch 7:130 at r=11.7 describes the QED Schwinger field in macro-scale units (where V_SNAP/V_yield = 1/√α). Under subatomic override both collapse to r=1. §0.2 of [doc 50_ r3](50_autoresonant_pair_creation.md) has the corrected framing.
>
> **Authoritative resolution:** R4 = remove `/α` conversions from NodeResonanceObserver + BondObserver; direct sum as RegimeClassifierObserver already does. See [`~/.claude/plans/review-the-collaboration-md-and-lexical-wombat.md`](file:///Users/grantlindblom/.claude/plans/review-the-collaboration-md-and-lexical-wombat.md) Phase 3.5 17-step list.
>
> **What to do with this doc:** kept for audit trail (shows the R3 reasoning path and where it went wrong). DO NOT execute its §11 "Phase 3.5.B engine patches" — those implement R3. Use the plan file's R4 step list instead.
>
> **Content below is preserved as-written for historical record.** Do not use as authority going forward.

---

**Status:** Phase 3.5.A deliverable, Stage 6 (2026-04-22). **SUPERSEDED 2026-04-23 per R4 adjudication — see banner above.**
**Blocks:** Phase 4 (asymmetric μ/ε saturation tracks). Must land before Phase 4 begins.
**Resolves:** [VACUUM_ENGINE_MANUAL.md §17 A1](VACUUM_ENGINE_MANUAL.md). Independently re-derives the normalization question from the AVE axioms rather than accepting doc 54_'s assertions as authoritative.

**Directive from Grant (2026-04-22):** "find the AVE-native axiom and unit mappings — don't trust doc 54_ as authoritative." This document cites manuscript and engine-code directly with file:line for every load-bearing claim.

---

## 0. TL;DR — the canonical AVE-native convention

Per [Vol 1 Ch 7:12](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L12), every AVE domain reduces to a single dimensionless control parameter `r = A/A_c` where `A_c` is the domain's **Regime IV entry boundary** (NOT the Schwinger-equivalent deep-rupture point). The universal saturation operator `S(r) = √(1 − r²)` changes character at `r = 1` uniformly across domains.

**Canonical domain A_c values from [Vol 1 Ch 7 §domain-catalog (lines 96-217)]:**

| Domain | A_c | r = A/A_c |
|---|---|---|
| EM (voltage) | `V_yield = √α · V_SNAP ≈ 43.65 kV` | `r = V/V_yield` |
| EM (field) | `E_yield = V_yield/ℓ_node ≈ 1.13e17 V/m` | `r = E/E_yield` |
| Gravity | `unitary strain = 1` | `r = ε₁₁` |
| GW | `h_yield = √α ≈ 0.0854` | `r = h/√α` |
| Magnetic | `B_snap = m_e²c²/(eℏ) ≈ 1.89e9 T` | `r = B/B_snap` |
| Nuclear | `d_sat/r_sep = 1` (Pauli wall) | `r = d_sat/r_sep` |
| BCS | `T_c` | `r = T/T_c` |

Vol 1 Ch 7:130 explicitly states the Schwinger critical field `E_S` corresponds to `r = E_S/E_yield = 1/√α ≈ 11.7`, "deep in Regime IV" — NOT at r = 1.

**Reading of the engine:**

- **Cosserat sector** computes `A²_cos = ε²/ε_yield² + κ²/ω_yield²` with `ε_yield = 1`, `ω_yield = π` ([cosserat_field_3d.py:234, 530-531](../../src/ave/topological/cosserat_field_3d.py#L234)). These are the Cosserat sector's own Regime IV boundary values per Vol 1 Ch 7's universal convention. **CORRECT.**
- **K4 sector** computes `A²_K4 = V²/V_SNAP²` ([k4_tlm.py:237-238, k4_cosserat_coupling.py:208](../../src/ave/topological/k4_cosserat_coupling.py#L208)) — this is **V_SNAP-normalized, not V_yield-normalized**. Per Vol 1 Ch 7:104 the canonical EM `r = V/V_yield`, so engine's `A²_K4` differs from the canonical `r²` by a factor of α.
- **Regime boundaries** `_REGIME_I_BOUND_A2 = 2α`, `_REGIME_II_BOUND_A2 = 0.75`, `_RUPTURE_BOUND_A2 = 1.0` ([vacuum_engine.py:151-153](../../src/ave/topological/vacuum_engine.py#L151)) numerically match Vol 1 Ch 7's `r² = 2α, 3/4, 1` (lines 30-33) but are applied to SNAP-normalized `A²_K4` — this **MIXES conventions**.
- **`RegimeClassifierObserver` and `_update_z_local_total`** sum `A²_K4` (SNAP-normalized) + `A²_cos` (yield-normalized) directly. The two terms differ by a factor of α; summing them is **dimensionally incoherent** (in normalization terms, not physical units).

**Verdict: the K4 sector is the outlier.** Cosserat's yield-normalization matches Vol 1 Ch 7's universal regime map. The K4 sector's V_SNAP-normalization is a historical convention that diverges from the manuscript's canonical r = V/V_yield form.

**Two resolution options:**

- **R2 (canonical, invasive):** Migrate the K4 sector to yield-normalization natively: `A²_K4 = V²/V_yield² = (V²/V_SNAP²) / α`. All sectors in the same canonical yield units. Multiple engine + test files touched. Doc 50_'s headline `A²_K4 = 0.393` re-reports as `A²_K4_yield = 53.8`. High regression risk mid-Stage-6.
- **R3 (minimal, explicit):** Add dual accessors `VacuumEngine3D.A2_total_SNAP()` and `A2_total_yield()`. Deprecate `RegimeClassifierObserver.max_A2_total` as ambiguous. Update observer docstrings to be explicit about normalization. No engine-behavior change. Low regression risk. Flags the inconsistency without resolving it.

**Recommendation for Phase 3.5.B: R3.** Stage 6 Phases 4-6 are already pre-registered against the existing conventions; R2 would require re-registering P_phase4_asymmetric, P_phase5_nucleation, and P_phase6_autoresonant. R3 makes the ambiguity explicit for observer callers without breaking running work. **Track full R2 migration as FUTURE_WORK G-9** (post-Stage-6; no time pressure since the ambiguity is cosmetic for Phase 4+ once accessors are explicit).

---

## 1. Methodology

Investigation agenda (from Phase 3.5.A plan):

1. Axiom 2 TKI unit mappings — Vol 4 Ch 1 + Vol 1 Ch 1
2. Vol 1 Ch 7 universal regime map A_c extraction (every domain)
3. Origin trace for `ε_yield = 1.0`, `ω_yield = π`
4. Cosserat-EM duality in Vol 4 Ch 1:71-120
5. Axiom 4 universality — Vol 1 Ch 7:257-262
6. AVE-APU Ch 5 Pythagorean theorem — full context
7. Constitutive moduli in `cosserat_field_3d.py`

Auxiliary audit items added per Grant's 2026-04-22 pushback:

- **A0** — v2 reproducibility seed sweep (launched; results pending at time of writing)
- **A1 (reopened)** — Universal operator catalogue (universal_operators.py) vs KB INVARIANT-N3 naming consistency
- **A2 (new)** — KB invariants full audit (ave-kb/CLAUDE.md)

This document synthesizes all items.

---

## 2. Axiom 2 TKI unit mappings ([Vol 4 Ch 1:60-106](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L60))

The topo-kinematic isomorphism `ξ_topo = e/ℓ_node` is AVE's canonical unit bridge. Vol 4 Ch 1 derives six identities:

| Electrical | Mechanical | Identity |
|---|---|---|
| Q (charge) | L (length) | `Q = ξ_topo · x` |
| I (current) | v (velocity) | `I = ξ_topo · v` |
| V (voltage) | F (force) | `V = ξ_topo⁻¹ · F` |
| L (inductance) | m (mass) | `L = ξ_topo⁻² · m` |
| C (capacitance) | 1/k (compliance) | `C = ξ_topo² · (x/F)` |
| R (resistance) | η (viscosity) | `R = ξ_topo⁻² · η` |

**Voltage-to-force mapping:** `V_yield = ξ_topo⁻¹ · F_yield` where `F_yield` is the force at which the lattice yields (per Vol 4 Ch 1:65-69). `V_SNAP = ξ_topo⁻¹ · T_EM` where `T_EM = m_e c²/ℓ_node` is the electromagnetic string tension (line 65).

So: `F_yield = √α · T_EM ≈ √α · 0.212 N ≈ 0.018 N`.

For the Cosserat sector, the natural force per unit area is a stress `σ = G · ε` where G is the shear modulus and ε is the strain. Yield stress `σ_yield = G · ε_yield`. Without an explicit `G` calibration, we cannot derive `ε_yield` from V_yield via this route. (See §7 below.)

Vol 4 Ch 1 does NOT explicitly provide a rotational TKI mapping for microrotation ω or curvature κ. This is a gap in the canonical duality table. The engine treats ω as an independent field with its own yield threshold ω_yield = π (units rad/ℓ_node, per [VACUUM_ENGINE_MANUAL §17 A12](VACUUM_ENGINE_MANUAL.md)).

---

## 3. Vol 1 Ch 7 universal regime map — the authoritative source

Vol 1 Ch 7 is unambiguous:

> "Every physical domain in the AVE framework reduces to a single dimensionless control parameter `r = A/A_c`, where A is the local strain amplitude and A_c is the domain-specific critical threshold derived from the four axioms." ([line 12](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L12))

> "S(r) = √(1 − r²), r ≡ A/A_c" ([line 20](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L20))

> Regime IV (Ruptured): r ≥ 1.0, S = 0. ([line 33](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L33))

Per Vol 1 Ch 7:96 "In every case, A_c is derived from the four axioms — it is never a fitted or empirical parameter."

**For the EM voltage domain** ([lines 101-107](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L101)):

```
Amplitude A: Applied voltage V
Critical A_c: V_yield = √α · V_SNAP = √α · m_e c²/e ≈ 43.65 kV
Control parameter: r = V / V_yield
```

**Schwinger sits at r = 1/√α ≈ 11.7, deep Regime IV** (line 130).

**Universal master equation** ([Vol 1 Ch 7:258-262](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L258)):

```
∂²φ/∂t² = c_0² · (1 − r²)^(1/2) · ∇²φ
```

with `r = A/A_c` domain-specific. This equation applies to every domain uniformly at the r = 1 rupture boundary. EM at r = 1 ⇔ V = V_yield ⇔ **yield onset** (Regime IV boundary). NOT Schwinger.

**Note on Vol 1 Ch 7:115** ("Schwinger pair production: r = 1.0 — Regime IV boundary") — this is an **internal inconsistency** in the manuscript itself. Line 115 says Schwinger is at r=1; line 130 says Schwinger is at r=11.7. Line 130 is the dimensionally-consistent reading (V_SNAP/V_yield = 1/√α ≈ 11.7). Line 115 is a text error — probably intended to say "Schwinger pair production onset" at V_yield (where the varactor diverges and pair production becomes kinematically possible), distinct from "Schwinger critical field" at V_SNAP. Flagged for future manuscript cleanup.

---

## 4. Origin trace — `ε_yield = 1.0`, `ω_yield = π`

Agent investigation indicated these were first introduced in `33_phase3b_x3_energy_analysis.md` (Phase 3b X3 energy analysis). Direct grep returns no numerical definition there — the values were set as empirical placeholders in `cosserat_field_3d.py:530-531` without an explicit derivation document.

VACUUM_ENGINE_MANUAL.md §6.3 classifies them as "Empirical (placeholder)" with the note:

> "ε_yield = 1.0 (dimensionless strain threshold, Cosserat's Regime IV boundary)"
> "ω_yield = π (curvature threshold; units rad/ℓ_node — half-turn per lattice pitch)"

These values **satisfy Vol 1 Ch 7's universal convention as Regime IV boundary values:**
- `ε_yield = 1` matches gravity's `A_c = unitary strain = 1` ([Vol 1 Ch 7:138](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L138))
- `ω_yield = π` matches "curvature at half-turn per lattice pitch" — a kinematic saturation analog, reasonable as a Regime IV boundary (a full 2π turn per ℓ_node would be an unphysical over-rotation)

They are placeholders in the sense that no axiom-native derivation pins them to specific numerical values, BUT their convention (A²_cos = 1 at Regime IV) is correct per Vol 1 Ch 7. The values may need refinement (e.g., `ε_yield = √α` by analogy to GW, or `ω_yield = 2π/ℓ_node` for full turn) but this is a **calibration** question, not a convention question.

---

## 5. Cosserat-EM duality ([Vol 4 Ch 1:71-120](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L71))

Vol 4 Ch 1 derives the electron LC tank parameters:

```
L_e = ξ_topo⁻² · m_e ≈ 5.292e-18 H
C_e = e / V_SNAP = 3.13e-25 F
```

Resonance: `ω_C = 1/√(L_e·C_e) = c/ℓ_node = m_e c²/ℏ` (Compton).

**Yield stress from TKI:** `σ_yield = F_yield / ℓ_node² = ξ_topo · V_yield / ℓ_node² = V_yield · e / ℓ_node³`.

**Cosserat strain yield (naive derivation):** `ε_yield = σ_yield / G` where G is the shear modulus. In natural units with `G = 1` (engine default, cosserat_field_3d.py:521), `ε_yield` would numerically equal `σ_yield` in natural units.

**The engine sets `G = 1` as a placeholder** ([cosserat_field_3d.py:521](../../src/ave/topological/cosserat_field_3d.py#L521)). With G = 1 and `σ_yield = V_yield · e / ℓ_node³ = √α · V_SNAP · e / ℓ_node³`:

```
σ_yield (natural) = √α · V_SNAP · e / ℓ_node³ = √α · (m_e c² / e) · e / ℓ_node³
                  = √α · m_e c² / ℓ_node³
                  = √α  (in natural units where m_e = c = ℓ_node = 1)
                  ≈ 0.0854
```

**If G = 1 and σ_yield = √α, then the "physically-derived" ε_yield = √α ≈ 0.0854, NOT 1.0.**

The engine's ε_yield = 1.0 places the Cosserat Regime IV boundary at `ε = 1` (unitary strain, matching Vol 1 Ch 7's gravity convention). This is ~11.7× HIGHER strain than the TKI-derivation-of-ε_yield from V_yield would suggest.

**Two readings:**

- **Engine's reading (Vol 1 Ch 7 gravity-like):** `ε_yield = unitary strain = 1.0`, the Cosserat sector's own Regime IV boundary, NOT tied to V_yield via TKI. This is the convention currently used.

- **TKI-derived reading:** `ε_yield = √α ≈ 0.0854`, if we insist on dimensional consistency with V_yield via the Cosserat-EM duality and G = 1.

The two readings differ by a factor of 1/√α ≈ 11.7 in ε. **Neither is wrong** — they represent different choices for what the Cosserat sector's `A_c` physically MEANS:

- If Cosserat Regime IV is "the Cosserat analog of EM Regime IV" (mapped via TKI), ε_yield = √α.
- If Cosserat Regime IV is "unitary strain, i.e. the lattice itself stretches by 100%" (matching gravity's intuition), ε_yield = 1.0.

**The engine chose the gravity-like reading** (ε_yield = 1 matches Vol 1 Ch 7:138's gravity A_c = unitary strain). This is internally consistent with Vol 1 Ch 7's gravity-row but not derivable from V_yield via TKI.

**This is a legitimately open calibration question.** Not a bug, but a convention choice. Flagged for future derivation doc.

---

## 6. Constitutive moduli ([cosserat_field_3d.py:520-538](../../src/ave/topological/cosserat_field_3d.py#L520))

All constitutive moduli are set to unity natural-unit placeholders:

```python
self.G = 1.0            # shear modulus
self.G_c = 1.0          # Cosserat modulus (antisymmetric)
self.gamma = 1.0        # rotational stiffness
self.k_op10 = 1.0       # Op10 coupling
self.k_refl = 1.0       # reflection coupling
self.k_hopf = float(np.pi / 3.0)   # Hopf coupling (Q_H = 6 derivation)
self.omega_yield = float(np.pi)    # ω yield
self.epsilon_yield = 1.0           # ε yield
self.rho = 1.0                     # translational inertia
self.I_omega = 1.0                 # rotational inertia
```

**S4 gate resolution** ([S_GATES_OPEN.md:31](S_GATES_OPEN.md#L31)): "Option A — natural units `ρ = I_ω = 1`; SI calibration deferred post-Phase-III." The moduli are intentionally natural-unit placeholders per S4=A.

**Only k_hopf has an axiom-derived value** (`π/3` from the Hopf-invariant matching at `Q_H = 6` for the electron (2,3) winding; see [research/L3_electron_soliton/13_](13_) §3.2). The rest are `1.0` placeholders.

---

## 7. Axiom 4 universality — confirmed

Vol 1 Ch 7:257-262 explicit universality claim:

> "In every domain, when expressed in terms of the dimensionless control parameter r, the equations of motion take the same form... This is a single equation governing all of physics; the domain merely specifies the physical meaning of φ, A, and A_c."

For the coupled K4⊗Cosserat engine, the Pythagorean-strain theorem ([AVE-APU Vol 1 Ch 5:26-37](../../../AVE-APU/manuscript/vol_1_axiomatic_components/chapters/05_geometric_triodes.tex)) permits summing orthogonal-DoF contributions to the total `r²`:

```
r²_total = r²_K4 + r²_Cos
```

WHERE BOTH TERMS USE THE SAME DOMAIN-NORMALIZATION. If `r²_K4 = V²/V_yield²` and `r²_Cos = ε²/ε_yield² + κ²/ω_yield²`, the sum is valid. If instead `r²_K4 = V²/V_SNAP² = α · V²/V_yield²`, the sum mixes scales.

**The engine's current sum mixes scales** per [k4_cosserat_coupling.py:207-215](../../src/ave/topological/k4_cosserat_coupling.py#L207):

```python
A_sq_k4 = V_sq / (self.V_SNAP ** 2)     # SNAP-normalized
A_sq_cos = _cosserat_A_squared(...)      # yield-normalized
A_sq_total = A_sq_k4 + A_sq_cos          # mixed
A_sq_total = np.clip(A_sq_total, 0.0, 1.0 - 1e-12)   # clip as if all yield
```

The clip at 1.0 assumes both terms are yield-normalized; the K4 term isn't.

---

## 8. Universal operator catalogue — Rule-6 concern ([Grant's #2 audit point])

**KB [INVARIANT-N3](../../manuscript/ave-kb/CLAUDE.md):**
> "Known operators: Op2 (knot crossing correction), Op3 (small-signal impedance correction), Op4 (potential well / H-bond), Op8 (large-signal confirmation), Op9 (charge correction), Op14 (long-range coupling)."

**Engine [universal_operators.py](../../src/ave/core/universal_operators.py) docstring:**
> "Op1: Impedance (Z), Op2: Saturation (S), Op3: Reflection (Γ), Op4: Pairwise Energy (U), Op5: Y→S, Op6: Eigenvalue, Op7: FFT, Op8: Packing Reflection, Op9: Steric Reflection, Op10: Junction Projection Loss, Op14: Dynamic Impedance (Z_eff)."

**These are DIFFERENT OpN namings.** KB's Op14 (long-range coupling) ≠ engine's Op14 (Dynamic Impedance Z_eff). KB's Op2 (knot crossing) ≠ engine's Op2 (Saturation).

**This is a documentation drift, not a physics bug.** When VACUUM_ENGINE_MANUAL cites "Op14 = Z_eff", it's the engine's convention; when KB INVARIANT-N3 cites "Op14 = long-range coupling", it's the manuscript's cross-volume naming. Both conventions are internally consistent within their domain.

**Recommendation:** Track as FUTURE_WORK Y-8 — either reconcile the two numberings (engine adopts KB's OpN meanings, or KB acknowledges engine's internal OpN numbering) or add a translation table. Not blocking Stage 6.

---

## 9. KB invariants audit — ([Grant's #3 audit point])

Read [ave-kb/CLAUDE.md](../../manuscript/ave-kb/CLAUDE.md) in full. Relevant invariants for this investigation:

| Invariant | Content | Relevance to A1 |
|---|---|---|
| INVARIANT-N2 | `ℓ_node` notation (script ell in Vols 1-5) | Dimensional checks on natural-unit formulas |
| INVARIANT-N3 | OpN numbering | §8 above — flagged Rule-6 drift |
| INVARIANT-C1 | `V_yield ≈ 43.65 kV` in Vol 4 Ch 1 | **Canonical anchor for all yield normalization** |
| INVARIANT-C2 | `ξ_topo = e/ℓ_node` | TKI unit bridge |
| INVARIANT-C4 | `Z ∝ 1/A` (physical), `Z ∝ A` (virtual) | Hardware/software isomorphism; not directly relevant |

**No violations found.** The A1 normalization issue does NOT violate any KB invariant — it's a convention choice within the canonical yield-vs-SNAP range that INVARIANT-C1 establishes.

---

## 10. v2 reproducibility seed sweep results

[Pending at time of first draft — sweep launched 2026-04-22 23:41, ~30 min runtime. Will update this section with results.]

**Pre-check analysis (without data):** If the engine can still reach `max A²_cos ≥ 1.009` under some seed, doc 50_'s headline reproduces. If not, Stage 6 has a silent regression (likely from the Phase 3 `_connect_all` change or Phase 2's NodeResonanceObserver import chain perturbing JAX compilation).

**Regardless of sweep outcome, the normalization question is independent.** The sweep affects Stage 6's HEADLINE NUMBER, not the A1 ADJUDICATION (which is about what A²_cos = 1.009 MEANS, not whether it's reachable).

---

## 11. Resolution & engine patches (R3 for Phase 3.5.B)

**Chosen:** R3 (dual accessors + explicit deprecation). Full R2 migration tracked as FUTURE_WORK G-9 (post-Stage-6).

**Phase 3.5.B engine patches:**

1. **`VacuumEngine3D.A2_total_SNAP()`** — returns mixed-convention total as currently computed (preserves backward compatibility). Docstring explicitly documents the mixing.
2. **`VacuumEngine3D.A2_total_yield()`** — returns true yield-normalized total: `(A²_K4_SNAP / α) + A²_Cos`. This is the canonical Vol 1 Ch 7 r² value.
3. **`RegimeClassifierObserver.max_A2_total`** — emit DeprecationWarning on access; add new fields `max_A2_SNAP` and `max_A2_yield` with explicit conventions.
4. **NodeResonanceObserver** — clarify docstring: "A²_K4 converted to yield (÷α); A²_Cos already yield-normalized; total is yield-normalized per Vol 1 Ch 7:12."
5. **BondObserver** — same clarification.
6. **New unit test file `test_normalization_conventions.py`** — pins:
   - `VacuumEngine3D.A2_total_yield() = A2_total_SNAP() · ...something-involving-α` (verify the conversion is the α-factor it should be)
   - `NodeResonanceObserver.A2_yield_max` always uses yield convention
   - `RegimeClassifierObserver.max_A2_total` emits DeprecationWarning
7. **VACUUM_ENGINE_MANUAL §17 A1** — mark as CLOSED with R3 resolution + date.
8. **VACUUM_ENGINE_MANUAL §6.3** — add convention note: "All A² values in the manual refer to yield-normalization unless explicitly marked `_SNAP`."

---

## 12. Future work (G-9, post-Stage-6)

Full R2 migration to unified yield-normalization:

- Change `A²_K4 = V²/V_yield²` at source in [k4_tlm.py](../../src/ave/core/k4_tlm.py) and [k4_cosserat_coupling.py](../../src/ave/topological/k4_cosserat_coupling.py)
- Re-validate all regime-boundary numerical values (they match Vol 1 Ch 7's r² exactly under yield-normalization)
- Re-report all historical Phase III-B results in yield units (doc 50_'s `A²_K4 = 0.393` → `A²_K4_yield = 53.8`; `A²_cos = 1.009` unchanged)
- Re-register Stage 6 predictions in yield-normalized units

Estimated effort: ~3-5 days. Track as G-9 in FUTURE_WORK.md.

---

## 13. Cross-references

**Primary sources:**
- [Vol 1 Ch 7](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex) — universal regime map (§2, 3, 4, 7)
- [Vol 4 Ch 1:60-142](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L60) — TKI identities, Vacuum Varactor
- [ave-kb/CLAUDE.md INVARIANT-C1, C2, N3](../../manuscript/ave-kb/CLAUDE.md) — canonical values, operator numbering
- [AVE-APU Vol 1 Ch 5:26-37](../../../AVE-APU/manuscript/vol_1_axiomatic_components/chapters/05_geometric_triodes.tex) — Pythagorean strain theorem

**Engine sources:**
- [cosserat_field_3d.py:234, 520-538](../../src/ave/topological/cosserat_field_3d.py#L234) — A²_cos, constitutive moduli
- [k4_tlm.py:237-247](../../src/ave/core/k4_tlm.py#L237) — Op14 Z_eff, SNAP normalization
- [k4_cosserat_coupling.py:195-224](../../src/ave/topological/k4_cosserat_coupling.py#L195) — _update_z_local_total (A1 direct site)
- [vacuum_engine.py:151-153, 370-388](../../src/ave/topological/vacuum_engine.py#L151) — regime boundaries, RegimeClassifierObserver
- [universal_operators.py:57-85](../../src/ave/core/universal_operators.py#L57) — `universal_saturation(A, A_yield)`

**Research thread:**
- [45_lattice_impedance_first_principles.md §3.1](45_lattice_impedance_first_principles.md) — V_SNAP vs V_yield first flagged
- [54_pair_production_axiom_derivation.md §5](54_pair_production_axiom_derivation.md) — convention fix proposed (not authoritative per Grant's directive)
- [VACUUM_ENGINE_MANUAL §17 A1](VACUUM_ENGINE_MANUAL.md) — audit finding that triggered this doc
- [S_GATES_OPEN.md S4=A](S_GATES_OPEN.md) — natural-units placeholder deferral

---

## 14. What doc 55_ authorizes

Phase 3.5.B may proceed with R3 engine patches per §11. Phase 4 unblocked once 3.5.B lands.

**A1 closed with resolution R3.** The K4 sector uses V_SNAP-normalization as a historical convention; Cosserat uses V_yield normalization matching Vol 1 Ch 7's canonical form. Dual accessors make the distinction explicit for observer callers; `max_A2_total` is deprecated as inherently ambiguous. Full R2 migration deferred to G-9.

**ε_yield = 1.0 and ω_yield = π are valid placeholder values** for Cosserat Regime IV boundary in the unitary-strain convention (matching Vol 1 Ch 7 gravity). The TKI-derived alternative (`ε_yield = √α`) is a different convention choice, tracked as Phase 4 calibration option — not binding for Phase 4 start.

**Universal-operator catalogue naming drift (§8)** tracked as FUTURE_WORK Y-8.

**v2 reproducibility sweep results** to be inserted in §10 once complete.

Grant adjudication required before Phase 3.5.B code begins:
1. Accept R3 as the Phase 3.5.B approach?
2. Accept G-9 deferral of full R2 migration?
3. Are the Cosserat `ε_yield = 1, ω_yield = π` values acceptable for Phase 4's asymmetric saturation split, or do you want to recalibrate to the TKI-derived `ε_yield = √α` first?
