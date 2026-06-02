# INVESTIGATION BRIEF — Does τ_yield *scale with* the dual-reactance count? (the last open thread from the V2 reframe)

**Date:** 2026-06-02
**Type:** Substrate-physics derivation — provenance upgrade + cross-scale unification candidate
**Status:** READY — run in a focused session (R2-style; Grant-in-the-loop for the crux)
**Branch:** branch off `main` (suggested `analysis/tau-yield-reactance-count`); push; do **NOT** merge — orchestration merges
**Closes:** the τ_yield open item recorded at [`common/dual-reactance-storage-taxonomy.md:155`](../manuscript/ave-kb/common/dual-reactance-storage-taxonomy.md) (§τ_yield open item) + clm-8ep2b4 / clm-o2shcn — the last open thread from the 2026-06-02 dual-reactance reframe (merge `b7913bf7`)
**Origin:** the fabricated-FEM walk-back reframed the τ_yield sites to "V_total = 2 = dual-reactance count," but whether the yield stress physically **scales with** that count (vs merely inherits the value 2) was parked as the genuine open question.

## The question
`τ_yield = e²·V_total/(8πε₀ℓ_node⁴)` with `V_total = 2`. Is the factor of 2 there because the dielectric yield physically scales with the **count of reactance sectors** (forced, axiom-derived) — or does the formula merely **inherit the value 2** (a re-interpretation)?

## The clean candidate (why closure is plausible — not green-field)
EE/substrate picture: **yield stress = the total stored reactive energy density at the saturation limit.** A node is an LC tank storing energy in two sectors — capacitive `E_C` and inductive `E_L`. The total at breakdown is `E_C + E_L`. The formula cooperates:
- `e²/(8πε₀ℓ⁴)` is the **capacitive (per-sector) energy density** at the node scale (Coulomb self-energy `e²/8πε₀ℓ` over `ℓ³`; dimensionally J/m³ = Pa).
- So `τ_yield = 2·e²/(8πε₀ℓ⁴)` reads as **`E_C + E_L` at breakdown** — and the **2 IS the reactance-sector count** (`X_C + X_L`), the same two sectors as the baryon `V=2`.

The equipartition that gives the clean ×2 has a **robust basis**: in a lossless resonant LC tank, energy conservation forces the time-averaged `E_C = E_L = E_total/2` regardless of the Axiom-4 saturation modulation of C and L (the tank swaps energy 50/50). So the ×2 is not fragile **if** the yield is a resonant-tank event.

## The crux — the one load-bearing physics question
**Is the dielectric yield a *resonant-tank* saturation, a *static single-sector* saturation, or *saturation-skewed*?**
- **Resonant-tank** (the tank is oscillating, swapping energy, when it hits `A_yield`): energy conservation → `E_C = E_L` → `τ_yield = 2·E_sector` → **the 2 is forced** (the reactance count). → CLOSE.
- **Static single-sector** (one sector maxes out at rupture while the other is empty): `E_C ≠ E_L`, no clean ×2 → stays inherited.
- **Saturation-skewed** (the Axiom-4 kernel `S(A)=√(1−A²)` — `C_eff=C_0/S`, `ε_eff=ε_0 S`, `μ_eff=μ_0 S` — modulates the two sectors *oppositely* near `A→A_yield` in a way that overrides the energy-conservation 50/50): a *modulated* factor → REFINE.

The genuine tension to resolve: **energy-conservation says 50/50, but the Axiom-4 kernel modulates C up and L down as `S→0`** — does the conservation argument survive to the breakdown point? That's the whole ballgame, and it's Grant's physical call once the substrate-walk lays out the candidates.

## Proof obligations
1. **Per-sector energy density** `e²/(8πε₀ℓ⁴)` derived **independently** (NOT read back from the τ_yield formula — the non-circularity guard; `consistency-vs-emergence`).
2. **The yield-event class** — resonant-tank vs static-single-sector vs saturation-skewed (the crux). Walk the Axiom-4 saturation of the LC tank at `A→A_yield` with explicit reactance-pair tracking (`C_eff=C_0/S`; `L_eff` via `μ_eff=μ_0 S`); does the energy-conservation 50/50 hold?
3. **Yield = sum over both sectors** (not first-to-saturate), grounded in the resonant-tank / energy-conservation argument.
4. **Unification earned** — the τ_yield 2 grounded in the SAME `X_C + X_L` sectors as the baryon `V=2`, shown not asserted (the "don't-fuse-the-2's" discipline; here a *genuine* shared mechanism if it closes).

## Discriminating outcomes
- **CLOSE** — yield is a resonant-tank event; conservation forces `E_C=E_L`; `τ_yield = 2·E_sector`, the 2 = reactance count → **axiom-derived**, and it **unifies** the baryon dual-reactance loop (fm scale) with the macroscopic yield stress (~10²² Pa) through the same two sectors.
- **REFINE** — the factor is saturation-modulated (not a clean integer 2) → report the modulated form; still a real substrate result.
- **STAYS-INHERITED** — yield is single-sector / no clean sector-summation → open item stands; value 2 remains honestly inherited.

## Canonical hooks (verify each)
- τ_yield formula + its "derived from {ρ_bulk c², ρ_threshold, V_total=2}" claim: `vol1/dynamics/ch4-continuum-electrodynamics/magnetic-saturation.md:10,:20`; `backmatter/01_appendices.tex:71`; `common/appendices-overview.md:66`; `vol_1_foundations/chapters/04_continuum_electrodynamics.tex:219,:228`.
- The open item + the reframe: `common/dual-reactance-storage-taxonomy.md:155` (§τ_yield open item) + clm-8ep2b4 / clm-o2shcn + `research/2026-06-02_fabricated-FEM-walkback-and-tau-yield-fork.md`.
- Dual-reactance sectors + `E_C`/`E_L`/`X_C`/`X_L` + small-signal equipartition: `common/dual-reactance-storage-taxonomy.md` + `common/translation-tables/translation-circuit.md` §4.
- Axiom-4 kernel + reactance modulation (`S=√(1−A²)`, `C_eff=C_0/S`, `ε_eff=ε_0 S`, `μ_eff=μ_0 S`; `∫₀¹√(1−A²)dA=π/4`): KB `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2.
- The unification target (baryon V=2): `research/2026-06-01_baryon-V2-dual-reactance-closure.md`.

## Skill discipline (write a skill-selection plan first)
`ave-prereg` (grep the existing τ_yield derivation + any `E_C`/`E_L`-at-saturation work) → `ave-ee-first-mapping` (yield-as-stored-reactive-energy is EE-native; run it at entry) → `substrate-native-check` (the resonant-vs-static yield-event walk + reactance-pair tracking) → `consistency-vs-emergence` (classify as provenance-upgrade/derivation, NOT a new empirical prediction; non-circularity guard) → `pre-test-physics-check` Trigger 7 (on repeated negatives, surface the plumber-reframe before concluding "negative").

## Scope guard
Derivation closure only — a **provenance upgrade + unification**, same class as R2 (inherited → derived), **NOT** a new empirical prediction (there are always two sectors; the count can't be varied empirically). Output: a `research/` prereg + result doc + (if CLOSE) propagate the "derived, not inherited" status to the τ_yield sites + the open-item record. Branch off `main`, push, do **NOT** merge.
