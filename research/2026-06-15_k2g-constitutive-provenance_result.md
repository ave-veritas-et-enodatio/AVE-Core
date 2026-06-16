# RESULT — K=2G constitutive provenance: the chiral LC tank does NOT force K=2G either

**Date:** 2026-06-15. **Phase 2 of PR #261.** **Branch:** `analysis/2026-06-15-k2g-crystalline-provenance`.
**Prereg:** [`2026-06-15_k2g-constitutive-provenance_prereg_FROZEN.md`](2026-06-15_k2g-constitutive-provenance_prereg_FROZEN.md) (Rule-11 + Rule-12 A1).
**Driver:** [`src/scripts/verify/k2g_constitutive_rho.py`](../src/scripts/verify/k2g_constitutive_rho.py).
**Outcome:** **A** (predicted) — K=2G is NOT constitutively forced. **GR-imported — end of line.**

> **FLAG-DON'T-FIX → Grant.** Two calls are yours: (1) the **verdict** (constitutively-forced vs
> imported) — the computation says **imported**; (2) the **Keating-vs-Cosserat model choice** — I derive
> both; the verdict is **robust to it** (the choice only sets the numerical target ρ*). No canonical
> claim edited. This **closes the last route to a substrate-forced K=2G** that Phase 1 left open.

---

## 1. The bridge, derived (Grant's load-bearing flag)

| Step | Statement | Provenance |
|---|---|---|
| capacitive sector | `k_a = ξ²/C_eff` (elastance) | **corpus-canonical** — `common/translation-tables/translation-circuit.md:23` `C=ξ²·compliance=ξ²/stiffness` |
| inductive sector (the new step) | `k_s ∝ 1/L_eff` (magnetic reluctance ℛ=1/permeance; microrotation↔flux, E=½ℛΦ²) | **derived by EE duality** — flag for scrutiny |
| ⟹ | **ρ = k_a/k_s ∝ L_eff/C_eff = Z_eff²** | the bond-stiffness ratio IS local impedance, squared |

**Robustness:** the verdict needs only the *mild* half of the bridge — that k_a and k_s are the
elastances of the **ε-sector and μ-sector respectively**, scaling the same functional way with their
sector. The exact reluctance prefactor is not load-bearing.

## 2. The decisive structure: ρ = 𝒢 · (Z_eff/Z₀)²

A cold **geometric prefactor 𝒢** × an **operating-point impedance factor** (Z_eff/Z₀)².

- **K=2G is IDENTIFIED with the SYM operating point** (`backmatter/07:40` "SYM = vacuum K=2G; ε,μ
  saturate together") — the impedance-matched, reflectionless **Γ=0 gravity null** where ε_eff=ε₀S,
  μ_eff=μ₀S co-scale so **Z_eff=Z₀ stays invariant**. **This identification is itself the GR-imported
  trace-reversal** (`q-g47-…closure.md:28` "required by GR"; 2026-06-14 audit:18) — NOT a substrate
  derivation of where K=2G sits. The SYM-invariance argument below is therefore *"given the GR
  identification, the operating point adds nothing,"* not an independent derivation of the locus — which
  is exactly why the verdict is "imported."
- **On the K=2G branch, ρ = L_eff/C_eff = (μ₀S)/(ε₀S) = Z₀² for ALL S** (the common scaling cancels —
  driver §2, ρ=1.000 across S=1.0→0.05). **The saturation operating point cannot tune ρ.** The 2:1 of
  K=2G must therefore live in 𝒢 — and Phase 1 showed 𝒢 is an **unforced one-parameter family**.
- **Independent constitutive-side corroboration of the u₀*≈0.187 ECHO** (2026-06-14 audit): the
  "magic-angle operating point" cannot be where K=2G is forced, because on the SYM branch ρ is
  operating-point-invariant. The corpus had no such argument (grep-confirmed) — this is new.

## 3. The decisive read (driver §3) — and the ρ=1-vs-ρ=2 resolution

**Be precise about which "1" is pinned.** ρ = 𝒢_geom · (Z_eff/Z₀)². The OPERATING-POINT FACTOR
(Z_eff/Z₀)² is pinned to **1** on the SYM branch (this result). ρ itself = 𝒢_geom, the **cold geometric
prefactor** = the Phase-1 free ratio. So the table below sweeps ρ=𝒢_geom; the operating point is NOT a
knob on it.

| ρ = 𝒢_geom | Cosserat (native) K/G, ν | Keating (x-check) K/G, ν | meaning |
|---|---|---|---|
| **1.00** | 1.50, ν=0.227 | 0.67, ν=0.000 | 𝒢_geom=1 reference — a *pure balanced LC line* (no geometric ε/μ asymmetry); illustrative, NOT a claim the substrate sits here |
| **2.00** | **2.00, ν=2/7** | 0.97, ν=0.117 | Cosserat K=2G — the corpus's ASSERTED point (`k_a=2/7,k_s=1/7`); needs 𝒢_geom=2 |
| 1.52 | 1.76, ν=0.261 | **0.82, ν=0.068** | real z=4 diamond (Phase-1 reference) — 𝒢_geom≈1.5 |
| 5.30 | 3.65, ν=0.375 | **2.00, ν=2/7** | Keating K=2G (Voigt) — needs 𝒢_geom=5.3 |

**Resolving the auditor's question (is the substrate at the corpus ρ=2 or this result's ρ=1?).** Neither
is "forced." The operating-point factor is 1 either way, so **ρ = 𝒢_geom**. The corpus *posits* ρ=2
(`k_a=2/7, k_s=1/7`; `clm-bjceop:1073` — k_s=1/7 an explicit "normalization choice," taken as given to
land K=2G). My analysis shows ρ=2 cannot come from the operating-point factor (SYM-pinned to 1); it
would have to come from **𝒢_geom=2 — the Phase-1 cold-geometry question, answered NEGATIVE** (unforced
one-parameter family; real z=4 gives 𝒢_geom≈1.5, ν≈0.07–0.23). The ρ=1 row is the *illustrative
𝒢_geom=1 limit* (a featureless balanced LC line gives ν=0.227 in the native model, the nearest natural
miss of 2/7), **not** a claim the substrate sits at ρ=1. **Bottom line: the corpus's ρ=2 is asserted,
not forced — neither by the operating point (factor=1) nor by the geometry (Phase-1). Imported either
way.**

## 4. Model choice (Grant's flag) — verdict is robust

- **Cosserat micropolar** (Axiom 1, substrate-native): K₀=4k_a+8k_s, G₀=8k_s ⟹ K=2G ⟺ **ρ=2**.
- **Keating central-force** (Phase-1, validated vs carbon diamond C₄₄ to −0.36%): K=2G ⟺ **ρ*∈{3.67,5.30,6.62}**.

Both are sub-isostatic (G→0 as k_s→0). The model choice changes only the **numerical target ρ\***; in
**both**, the constitutive operating-point factor is pinned at Z_eff=Z₀ (ρ-contribution = 1) and cannot
reach ρ\*. **Cosserat is primary; Keating is the validated cross-check.** Flag-don't-fix: if you prefer
the Cosserat target ρ=2, note its impedance-matched ν=0.227 is the nearest natural miss.

## 5. The coupling Grant asked about — and a genuine new linkage

The two outputs of the one constitutive law are **coupled through the impedance factor**, and the
linkage is itself a finding:

> **The open crio Branch-R-vs-F monotonicity Q (C_eff rising/ASYM vs ε_eff falling/SYM,
> `research/2026-06-10_crio-ceff-saturation-onset_prereg-draft.md`, DRAFT-FOR-GRANT) IS the
> SYM-vs-ASYM operating-point Q IS the "does saturation tune ρ" Q.** Same physical question wearing
> three hats. On SYM (Branch F): ρ invariant (this result). On ASYM (Branch R): ρ moves with S, but
> its **direction is sign-ambiguous = exactly the open crio call**, and K=2G is not defined off-SYM
> (Z≠Z₀). **The verdict does not depend on resolving it** (Rule-12 A1). But: resolving crio also fixes
> the off-SYM ρ behaviour — one adjudication, two payoffs.

## 6. Verdict & adjudication (Grant's call)

**K=2G is NOT constitutively forced.** ρ = 𝒢·(Z_eff/Z₀)²: the constitutive law's only handle (the
operating-point impedance factor) is **SYM-pinned to 1** on the K=2G branch and so contributes nothing
to selecting it; the residual 𝒢 is the **Phase-1 unforced geometric ratio**. The chiral coupling does
not rescue it: `01_appendices.tex:131` "K=2G emergent from Chiral LC coupling" is backed only by a **tuned
simulation** (lines 132–135: low coupling → K/G≈1.67 Cauchy; high coupling → K/G≈1.78–2.0) that reaches
the range only at high `k_couple`, with **no first-principles fixing of `k_couple` and no clean landing on
2.0** — corroborated by the corpus's own **chirality-blind λ_G=4/21** (`closure-roadmap.md:32,191`,
invariant to 14 dp across k_χ∈[0,1]). **Both the geometry (Phase 1) and the constitutive law (Phase 2) fail
to force K=2G ⟹ it is GR-imported, end of line.** Forks (a) and the constitutive route both resolve to
IMPORTED, consistent with the standing 2026-06-14 audit.

**Recommended disposition (extends Phase-1 rec):**
1. **Ratify the two-phase NEGATIVE.** Log **Q-G41 closed-NEGATIVE** with both legs: *not* a K4
   topological inevitability (Phase 1) AND *not* a chiral-LC constitutive inevitability (Phase 2) — the
   constitutive operating-point factor is SYM-pinned to Z₀; K=2G is the GR trace-reversal, imported.
   *(Recommended.)*
2. **Land the new constitutive-side u₀* corroboration** as a one-line note where the 2026-06-14 audit's
   "u₀* ECHO" lives (flag-don't-fix; I did NOT edit it): "on the SYM branch ρ=Z_eff²=Z₀² is
   operating-point-invariant, so the saturation operating point cannot select K=2G — independent of the
   EMT back-fit argument."
3. **Cross-link the crio lane:** note the Branch-R-vs-F = SYM-vs-ASYM = does-saturation-tune-ρ linkage
   in the crio draft so resolving it picks up the off-SYM ρ behaviour for free.

## 7. Honest scope / limits

- The `k_s ∝ 1/L_eff` dual is the one **derived** (non-corpus) step; flagged for scrutiny. It is not
  merely absent from the corpus — it is in **mild tension with the canonical `translation-circuit.md:22`
  row L↔mass** (inductance as the *inertial* analog, not a stiffness). So the verdict does **not** lean on
  it: it rests on the **same-co-scaling fallback** (k_a, k_s are the ε/μ-sector elastances scaling the
  same way under SYM ⟹ the common factor cancels ⟹ operating-point-invariance), which is corpus-clean and
  needs no L↔stiffness identification. The `ρ=Z_eff²` reading is the interpretive picture, not load-bearing.
- This is the **linear small-signal** constitutive law. The chiral κ_chiral channel is nonlinear
  above-yield (corpus) and does not enter the linear K/G ratio; if a future derivation shows the chiral
  cross-term forces 𝒢=2 at the *cold linear* level, that would lift the verdict — none exists.
- The off-SYM (ASYM) ρ direction is **not resolved** here (it is the open crio Grant Q); the verdict is
  built to not need it.

## 8. Auditor-gate (2026-06-15) — PASS

Read-only ave-auditor, against worktree HEAD: **all 4 load-bearing citations verbatim-VERIFIED**
(`translation-circuit.md:23` C=ξ²/stiffness, `backmatter/07:40` SYM=K=2G, INVARIANT-S2 ε/μ scaling,
`q-g47-…closure.md:58` Cosserat moduli). **SYM-invariance argument judged SOUND** — the S-cancellation
is structural and confirmed for BOTH the F-form and the corpus R-form (`C_eff=C₀/S`), so it survives the
open crio sign. **The derived `k_s∝1/L` step judged honestly flagged AND robustly dispensable** — the
same-co-scaling fallback is genuinely sufficient; the verdict does not secretly depend on the dual.
**flag-don't-fix confirmed** (commit touched only the 4 lane files; no canonical edit). Four refinements
folded in here: (i) path-qualified `translation-circuit.md:23`; (ii) §2 now states K=2G=SYM is the
GR-imported identification (not an independent locus derivation); (iii) §7 sharpened the `k_s∝1/L` flag
to the `:22` L↔mass tension + leans on the fallback; (iv) §6 softened `01_appendices.tex:131` from "bare
assertion" to "tuned simulation, no first-principles `k_couple`." The auditor's sharp question (substrate
at ρ=1 or corpus ρ=2?) is resolved in §3: **operating-point factor=1 ⟹ ρ=𝒢_geom; ρ=2 is asserted, needs
𝒢_geom=2 = Phase-1 NEGATIVE.** No verdict change.
