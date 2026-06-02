# WALK-BACK BRIEF — Fabricated-FEM completion: the "3D FEM integration" narrative + the τ_yield fork

**Date:** 2026-06-02
**Type:** Corpus-honesty walk-back — substrate-physics untangling + exhaustive propagation
**Status:** READY — run in a focused session; **CONTINUES the existing PR-B branch**
**Branch:** `analysis/parameter-ledger-v2-reframe` (already carries PR-B commits `f9bd8da2` + `063e7c1b`; add to it, push, do **NOT** merge — orchestration merges the comprehensive unit)
**Feeds:** completes the Parameter-Ledger-v2 reframe so it merges as ONE consistent unit (no mixed FEM/dual-reactance framing on main)
**Origin:** 2026-06-02 PR-B exhaustive sweep — TWO `ave-walk-back` "5×-miss" surprises revealed the fabricated-FEM framing is far more pervasive than the initial enumeration.

## Why this exists
PR-B reframed **18 baryon-context sites**: `V_TOROIDAL_HALO = 2` is the **dual-reactance count** (Axiom 1's two reactance sectors `X_C` + `X_L`), NOT a geometric "toroidal halo volume"; the fabricated "FEM-verified 2.001±0.003 / Richardson N→∞" labels were dropped. The exhaustive sweep then surfaced two held buckets that must be scrubbed BEFORE merge (else main carries a visible mixed-framing inconsistency).

## The load-bearing physics untangling — DO THIS FIRST (it drives every edit)
The corpus **fused two distinct quantities** and anchored both to a fabricated computation. Separate them:
- **`V_total = 2`** — the **dual-reactance count**. Forced by Axiom 1 (two reactance sectors). **Profile-INDEPENDENT.** Mass-confirmed via `m_p`. NOT a FEM result, NOT derived from the flux-tube profile. Canonical: [`common/dual-reactance-storage-taxonomy.md`](../manuscript/ave-kb/common/dual-reactance-storage-taxonomy.md).
- **`ρ_threshold ≈ 1.106`** — the **saturation density threshold**. Derived from the **Gaussian flux-tube ansatz** (FWHM = ℓ_node). This IS a **legitimate open derivation gap** (the Gaussian profile is unproven; Axiom 1 fixes the FWHM but not the functional form). **KEEP this rigour-gap disclosure — it is honest.**
- The corpus error: it ties `V_total=2` to "FEM convergence of the Gaussian-ansatz integration," making V_total look *profile-dependent* and *FEM-derived*. Both false. **Decouple: `V_total=2` is the forced reactance count; the Gaussian-ansatz gap binds `ρ_threshold` only.**

## Bucket B — retire the fabricated "3D FEM integration" narrative (~8 sites)
**Source claims** (the apparent canonical "FEM source"):
- `manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/thermal-softening.md:99` + `manuscript/vol_2_subatomic/chapters/02_baryon_sector.tex:156` — *"**FEM convergence.** High-resolution 3D finite-element integration of the full Borromean topology … yields V_total=2.0."* **RETIRE** — no such computation exists (V2-closure §3 + the 2026-06-01 `compute_*`-literal engine sweep found `tensors.py::compute_toroidal_halo_volume()` is a hardcoded `return 2.0`).

**Echo claims:**
- `manuscript/backmatter/12_mathematical_closure.tex:144` + `manuscript/ave-kb/common/mathematical-closure.md:167` (the rigour-gap table) — "V_total=2.0 (FEM-converged to 0.13%) … binding on whatever profile emerges." Reframe: V_total=2 is the forced reactance count (profile-independent); the Gaussian-ansatz gap binds `ρ_threshold`, not V_total.
- `manuscript/ave-kb/vol2/claim-quality.md:50, :65` — "FEM convergence to V_total=2.0 is binding."
- `manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/thermal-softening.md:77` + `manuscript/vol_2_subatomic/chapters/02_baryon_sector.tex:137` — "V_total=2.0 at FEM convergence remains binding on whatever profile emerges."

## Bucket A — the τ_yield physics fork (7 sites) — GRANT'S CALL within this session
Sites: `vol1/claim-quality.md:492, :506`; `vol1/dynamics/ch4-continuum-electrodynamics/magnetic-saturation.md:10, :20`; `vol_1_foundations/chapters/04_continuum_electrodynamics.tex:219, :228`; `vol4/circuit-theory/ch1-vacuum-circuit-analysis/tvs-transition.md:27`; `vol4/claim-quality.md:977, :993`; `common/appendices-overview.md:66`.

These embed V_total=2 in the dielectric-yield-stress formula `τ_yield = e²·V_total/(8πε₀ℓ⁴)`, where the local sites derive it as **"6 Borromean crossings × ⅓ = 2"** — a *geometric* story, distinct from the baryon-mass "2 reactance sectors."

**The fork:** does τ_yield genuinely scale with the **dual-reactance count** (the dielectric yield IS an Axiom-4 saturation event; saturation = reactance hitting its limit; 2 sectors → factor 2), or is the τ_yield "2" a **separate geometric factor** that coincidentally = 2 (the "don't-fuse-the-2's" risk)?

**Grant's lean (2026-06-02): apply the dual-reactance reframe + a NAMED open item** ("derive that τ_yield ∝ the dual-reactance count, vs merely inheriting the value 2") — physically natural (yield = saturation) and canonically consistent (V_total is the count everywhere), but a *re-interpretation* not a derivation. Confirm or revise in-session.

## Procedure
1. **Fresh EXHAUSTIVE grep FIRST** — the enumeration missed sites TWICE (5×-miss). Patterns across ALL of `manuscript/` AND `src/`: `FEM`, `finite.element`, `Richardson`, `2\.001`, `FEM.?conver`, `FEM.?verif`, plus `V_total`/`toroidal`/`halo` context. Cross-check against the Bucket A+B lists — **expect MORE.**
2. **Verify no 3D-FEM script exists** — `grep -rniE "finite.element|FEM" src/` + inspect `src/scripts/`. The canonical position is no-FEM (V2-closure), but confirm airtight before retiring the "3D FEM integration" claims (`verify-before-cite`).
3. **Do the untangling** (`V_total`=forced-count vs `ρ_threshold`=Gaussian-ansatz) — `substrate-native-check`.
4. **Adjudicate the τ_yield fork** (Grant) — apply-with-flag per his lean, or hold.
5. **Propagate** to all Bucket A+B sites + any the fresh grep adds (incl. the `.tex` ↔ `.md` mirror pairs — `mathematical-closure`, `continuum-electrodynamics`, `02_baryon_sector` all have both).
6. Commit on the PR-B branch, push, do **NOT** merge.

## Skill discipline (write a skill-selection plan first)
`ave-walk-back` (exhaustive propagation — load-bearing; two 5×-misses already), `substrate-native-check` (the V_total-vs-ρ_threshold untangling), `consistency-vs-emergence` (classify V_total=2 + the τ_yield reframe), `verify-before-cite` (the no-FEM-script confirmation), `ave-prereg` (if "τ_yield ∝ count" warrants a derivation).

## Scope guard
Continues PR-B on `analysis/parameter-ledger-v2-reframe`. Output: the edits + a short research note on the `V_total`-vs-`ρ_threshold` decoupling + the τ_yield adjudication. Do **NOT** merge — orchestration merges the comprehensive Parameter-Ledger-v2 unit (PR-B core `f9bd8da2` + propagation `063e7c1b` + this scrub) as ONE. **NOT in scope:** `vol6/claim-quality.md:38` (correct per-result He-4 claim — leave it).
