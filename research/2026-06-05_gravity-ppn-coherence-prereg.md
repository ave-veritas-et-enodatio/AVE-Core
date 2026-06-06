# PREREG — AVE gravity PPN internal-coherence test (light deflection + perihelion from one strain field)

**Status:** FROZEN pre-registration, 2026-06-05. Written BEFORE the derivation per `ave-prereg`. Orchestration session; implementor executes in a worktree off `main`.

**Origin:** foreword challenge thread 2026-06-05 (Part A perihelion finding + Grant's "are light-bending and perihelion both one mechanism at different speeds?"). Companion artifacts: [`2026-06-05_foreword-register-inversion-draft.md`](2026-06-05_foreword-register-inversion-draft.md) (Part A), this prereg.

## 1. The question

Does AVE's canonical temporal/spatial gravitational decomposition — **one strain field ε₁₁, projected by ν_vac=2/7 into**
- n_temporal = 1 + (2/7)ε₁₁ = 1 + 2GM/rc²  (redshift / g₀₀ sector)
- n_spatial = 1 + (9/7)ε₁₁  (lensing / g_ij sector)

— reproduce **BOTH** the weak-field light deflection (4GM/bc²) **AND** the Mercury perihelion advance (43″/century) **with one self-consistent ε₁₁ calibration**, and is that consistent with the two other gravity structures the corpus already states (the 4GM/bc² deflection claim and Ch 14's hand-set coeff-3 V_tidal)?

**This is a CONSISTENCY-COHERENCE audit, not an emergence test.** The corpus already classifies gravitational lensing/Shapiro as "AVE = GR at O(GM/c²r), no AVE-distinct observable" (consistency-class; [`divergence-test-substrate-map.md`](manuscript/ave-kb/common/divergence-test-substrate-map.md) C18, vol3 ch5). The question is whether the consistency reproduction is **internally coherent** across its three coefficient-bearing statements.

## 2. Corpus inventory (ave-prereg; grep-confirmed 2026-06-05)

Prior work that MUST be read + reconciled (do NOT reinvent):
- **Temporal/spatial split (the unifying-law candidate):** n_t=1+(2/7)ε₁₁, n_s=1+(9/7)ε₁₁ — [`common/translation_gravity.tex`](manuscript/common/translation_gravity.tex), [`common_equations/eq_gravity_derived.tex`](manuscript/common_equations/eq_gravity_derived.tex), `ave-kb/vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md`, `ave-kb/session/axiom-homologation.md`.
- **Light deflection / optical metric:** `ave-kb/vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md`, `ave-kb/vol3/gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md` (n(r) "mathematically identical to the spatial transverse trace of the Gordon optical metric"), [`vol_3_macroscopic/chapters/03_macroscopic_relativity.tex`](manuscript/vol_3_macroscopic/chapters/03_macroscopic_relativity.tex) (Snell's-law ray-trace → 4GM/bc²), [`predictions.yaml`](manuscript/predictions.yaml) ("δ = 4GM/bc²").
- **Perihelion (separate structure):** [`vol_3_macroscopic/chapters/14_macroscopic_orbital_mechanics.tex:60-77`](manuscript/vol_3_macroscopic/chapters/14_macroscopic_orbital_mechanics.tex) — static V_tidal = −GM/r(1+3GM/c²r), coeff 3 hand-set (no L²/velocity coupling; does NOT use n_s).
- **Two-speed substrate structure:** c_EM=c₀/S, c_shear=c₀√S (INVARIANT-S2, `ave-kb/CLAUDE.md`); Op16 (`operators.md`). c_shear "tracks Schwarzschild c√(1−r_s/r)."
- **SYM-scaling:** [`alpha-invariance-symmetric-gravity.md`](manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md) (Z₀ invariant under SYM; α exactly invariant); `trace-reversal-mechanism.md`, `vacuum-poisson-ratio.md` (ν_vac=2/7 origin).
- **Gordon optical metric form:** n(r)=(1+r_s/2r)³/(1−r_s/2r) ([`translation-tables/translation-gravity.md`](manuscript/ave-kb/common/translation-tables/translation-gravity.md)).

## 3. What I expect (honest prior — HYPOTHESIS, not conclusion)

A **tension**, with three candidate outcomes:
- **(H1) Internal inconsistency [my leading prior]:** calibrating n_t to GR forces ε₁₁ = 7GM/rc², making the spatial excess (9/7)ε₁₁ = **9GM/rc²** → effective PPN γ ≈ 4.5 → light deflection ≈ **11GM/bc²**, ~2.75× the corpus's own 4GM/bc² claim. If so, the (9/7) spatial metric, the 4GM/bc² deflection, and the coeff-3 perihelion cannot all be right → a genuine coherence gap requiring walk-back.
- **(H2) Coherent reproduction:** the deflection derivation combines n_t and n_s (e.g. via the Gordon-metric photon index √(g_ij/−g₀₀)) in a way that yields γ=1 and 4GM/bc² AND the perihelion 43″ from one ε₁₁ — in which case the unifying law holds, Ch 14's hand-set V_tidal is redundant, and Part A's challenge is answered. (I currently can't see how 9/7 yields γ=1, but the actual derivation may.)
- **(H3) Partial:** one observable reproduces, the other needs the separate structure → scopes exactly what's unified vs independently fit.

I am NOT confident in H1 — my PPN arithmetic is in-head and the n_s→deflection map may differ. The point of the derivation is to settle it.

## 4. Method (implementor phases)

- **Phase 0 — verify + read.** Re-grep all §2 citations at HEAD; read the decomposition leaf, the optical-refraction/refractive-index leaves, Ch 14, INVARIANT-S2. Confirm the exact definitions of ε₁₁, n_t, n_s, and how the canonical deflection derivation maps indices → deflection. `verify-before-cite`.
- **Phase 1 — light deflection from the canonical metric.** Using the canonical (n_t, n_s) optical metric (Gordon form), derive the weak-field photon deflection symbolically. Extract the implied PPN γ. Compare to GR (γ=1, 4GM/bc²) AND to the corpus's stated 4GM/bc². Report the γ the (2/7,9/7) split actually implies.
- **Phase 2 — perihelion from the SAME metric.** Derive the massive-particle perihelion advance from the same (n_t, n_s) metric (NOT the Ch 14 static potential). Extract PPN β. Compute Δφ for Mercury. Compare to 43″/century AND to Ch 14's coeff-3 result.
- **Phase 3 — coherence verdict.** Do Phases 1+2 follow from ONE ε₁₁ calibration? Are they consistent with (a) the 4GM/bc² deflection claim and (b) the Ch 14 coeff-3 perihelion? Classify per `consistency-vs-emergence`: internally-coherent-consistency / internally-inconsistent-needs-walkback / partial. If inconsistent, identify which of the three structures is the outlier.
- **Phase 4 — verification + honest framing.** Verification script (`ave-canonical-source`: import G, c, M_sun, M_mercury, a, e from canonical constants; compute deflection + Δφ numerically; NO hard-coded targets). Result doc. `ave-discrimination-check` (note: consistency-class, not distinct — do not over-frame). `ave-evidence-framing-discipline` on all strength language. Push branch; **do NOT merge**.

## 5. Discriminating outcomes / falsifiers

- If the canonical (2/7,9/7) decomposition yields **γ≠1 / deflection ≠ 4GM/bc²**, the corpus's gravity sector carries an internal inconsistency (the 9/7-spatial vs the 4GM/bc² claim) → walk-back queued; foreword gravity scoping in the Part A draft is vindicated AND sharpened.
- If it yields **γ=1 + 43″ from one ε₁₁**, the unifying law holds; Ch 14's hand-set V_tidal is a redundant re-statement and should be rederived from n_s; Part A's "coefficient hand-set" critique softens to "stated redundantly, derivable from the canonical metric."
- Either way the result is a coherence fact about the gravity sector, feeding the foreword rewrite's gravity section.

## 6. Skill discipline (implementor)

`verify-before-cite` (all citations) · `consistency-vs-emergence` (Phase 3 classification is load-bearing) · `substrate-native-check` (ε₁₁ / c_EM / c_shear structure) · `ave-canonical-source` (verification script constants) · `ave-ee-first-mapping` (two-sector index = two-impedance-sector TL) · `ave-discrimination-check` (do NOT frame a consistency reproduction as distinct) · `ave-evidence-framing-discipline` · `pre-test-physics-check` (if a new load-bearing framing question surfaces mid-derivation — e.g. ε₁₁ is defined such that the whole framing shifts — STOP and report, do not push through) · Pure-AVE-corpus rule.

## 7. Scope guards

- Weak-field PPN only (O(GM/rc²)); no strong-field, no BH-interior.
- This is an INTERNAL-COHERENCE audit. Do NOT claim AVE-distinctness (corpus already says AVE=GR here). The deliverable is "do the three gravity structures cohere?", not "is AVE right about gravity."
- If Phase 1 already shows a clean inconsistency, still run Phase 2 (the perihelion-from-n_s result is needed to know which structure is the outlier).
- Do NOT edit canonical leaves or Ch 14. Result + prereg only; walk-backs (if any) are queued for a separate adjudicated session.
