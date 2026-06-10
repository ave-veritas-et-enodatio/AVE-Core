# PREREG — Cross-sector V→ω pump confirmation (the crux-unblock test)

**Date:** 2026-06-09 · **Branch:** `analysis/2026-06-09-saturation-temporal-preregs` (off `main`)
**Binding derivation:** [`2026-06-09_tracereversal-pump-derivation_result.md`](2026-06-09_tracereversal-pump-derivation_result.md) (branch `analysis/2026-06-09-tracereversal-pump-derivation` @ 70c57cdd) — verdict WALL-ENGINE/FIXABLE; the bounded V→ω **form** is derived + machine-checked, the cross-sector **run** is THIS test.
**Documentation home:** `research/` (result) + the figures + the [arc epic](../_orchestration/2026-06-09_ion-compression-rectifier-arc.md). No electron/genesis claim — this confirms the *pump*, not the (2,3).

> **SCAFFOLD.** The implementation prescription is derived (zero new free parameters); this is an IMPLEMENT + RUN + FIGURE test, not a new derivation.

---

## 1. Target (one sentence)
Implement the derived **bounded V→ω boundary-condition pump** in the **coupled** K4-Cosserat engine (zero-free-parameter prescription) and run the cross-sector test: **driving the K4 V (longitudinal-scalar) sector toward yield, does the topological boundary condition on ω at the Γ=−1 null cone (Op17/Möbius-bounded) DYNAMICALLY grow the Cosserat microrotation ω from V — bounded (R=Γ²≤1, no detonation), with the energy ledger closing?**

## 2. Mode / regime / phase-state (ave-regime-phase-state-check)
- **MODE:** the **Heaviside-deleted scalar/longitudinal V** sector → **microrotation ω** (Cosserat). This is the cross-sector trace-reversal channel.
- **REGIME:** drive V toward the **Γ=−1 / null-cone** boundary (near-yield → yield); the confinement is a BOUNDARY phenomenon (Op17 `R=Γ²=1−T²`), NOT a bulk force.
- **PHASE-STATE:** dynamical, V-driven; **Checkpoint 9 is load-bearing** — measure the engine-EVOLVED `engine.cos.omega`, NOT the algebraic `_compute_A2_mu` heuristic.

## 3. Implementation prescription (from the derivation §9, verbatim — zero new free params)
1. `disable_cosserat_lc_force=True` (kill the detonating bulk force) + `enable_cosserat_self_terms=True`.
2. Port the moving-Γ=−1 clamp `a_ω = −(K/I_ω)·relu(−Γ)·ω` into the **coupled** engine, reading `Z_eff = Z₀√(S_μ/S_ε)` (Op14 Meissner-asymmetric) so Γ is the cross-sector reflection — with **K4 V_sq LIVE** (so V sources ω, the cross-sector fire).
3. Drive the **V** sector toward yield; read ω buildup **dynamically**.
4. Adjudicate against `R(A)=Γ²` (bounded, ≤1) vs `|ω|→10⁵` (detonating).
All constants canonical (`ave-canonical-source`): K, I_ω, Z₀, the Op14/Op17 forms, S(A). No tuned parameters.

## 4. Discriminating outcomes
- **A — CONFIRMED (the pump fires):** cross-sector V→ω grows ω from V dynamically; bounded (`R=Γ²≤1`, Op17 closes, NO detonation); energy ledger closes (confinement paid by V's longitudinal energy). → the crux is unblocked at the dynamical level; the symmetric/electron/gravity branch is open (the (2,3) self-assembly is the next layer).
- **B — FORM-BUT-NO-FIRE:** the boundary condition is bounded but ω does **not** grow from V cross-sector (the channel exists in form but doesn't pump — e.g. the clamp confines a seeded ω but V doesn't source it). → localize the missing V→ω *source* term; partial.
- **C — STILL-DETONATES / LEDGER-VIOLATION:** the coupled implementation still detonates (`|ω|→10⁵`) or violates energy closure → the boundary-condition form was not the fix; re-examine the derivation.

## 5. Figures (ave-engineering-program-rigor — planned AHEAD, savefig, stamped)
1. **ω(t) buildup:** the bounded boundary-condition pump vs the bulk-force detonation **control**, side-by-side (the headline: bounded vs runaway).
2. **R(A) = Γ² vs A:** bounded in [0,1] through A→1 (the Op17/Möbius regulator at the null cone).
3. **Cross-sector V→ω:** ω vs the driven V (does ω grow as V is driven? the actual pump curve).
4. **Energy ledger bar:** W_in (V drive) vs ω-confinement energy + dissipation — closes, no free energy.
5. **SENSITIVITY SWEEP (the rescue-fill discriminator):** ω-buildup vs V-drive amplitude across the near-yield band — does the pump fire **robustly** (turns on across the band, bounded throughout) or only at a **tuned** point? Robust = real; tuned = artifact.

## 6. Guards (full skill stack)
- **substrate-native-check + Checkpoint 9** — measure DYNAMICAL ω (evolved), not the heuristic; the coupling is the cross-sector V→ω channel.
- **ave-regime-phase-state-check** — boundary (null-cone) confinement, not a bulk force; near-yield → yield, dynamical.
- **ave-resonant-amplification-check** — the pump is **bounded by Op17** (`R≤1`), NOT resonantly amplified; a divergence = the bulk-force bug, not a feature (the over-unity tell).
- **ave-driver-script-honesty** — the energy ledger + R(A) bound reported every run; detonation or ledger-violation → automatic C.
- **ave-canonical-source** — zero new free parameters; all constants canonical.
- **ave-discrimination-check** — is the cross-sector V→ω pump AVE-distinct (the deleted-scalar channel, transverse-EM-forbidden) or reducible to ordinary mechanics?
- **verify-before-cite** — do NOT cite the retracted `vacuum_engine.py:104` 1.009 anchor; verify the clamp / Op17 / Z_eff forms in source.
- **ave-evidence-framing-discipline + ave-discriminator-before-synthesis** — A confirms the PUMP, not the electron; the (2,3) stays a separate downstream gap. Frame honestly.

## 7. Deliverables
`2026-06-09_cross-sector-pump-confirmation_result.md` — A/B/C + the cross-sector ω-buildup + R(A)-bounded + energy ledger + the **sensitivity sweep** + the embedded figures + DERIVED/VERIFIED/BLOCKED + skills fired. Driver (the coupled-engine pump implementation + the 5 figures + the sweep + savefig). Commit on its own implementor branch off the pump-derivation branch; do NOT push/merge.
