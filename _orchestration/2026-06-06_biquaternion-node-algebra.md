# Biquaternion node-algebra (orchestration)

**Date:** 2026-06-06 · **Branch:** `analysis/2026-06-06-biquaternion-node-algebra` (off `origin/main` `63190d35`; worktree `AVE-Core-quaternion-wt`)
**Prereg (FROZEN):** [`research/2026-06-06_biquaternion-node-algebra-prereg.md`](../research/2026-06-06_biquaternion-node-algebra-prereg.md)
**Session:** orchestration (Grant in-session). Branch + reviewed PR; no direct-to-main.

## §0 What

Prove-or-disprove: is the AVE node's natural number-system a **biquaternion**? Map 7 DOF + charge → biquaternion (E+B = complex 3-vector, breathing = real scalar, charge/winding = imaginary scalar); unit-quaternion closure = SU(2) spin-½ (2,3) double cover; the longitudinal 7th mode = Maxwell's Heaviside-deleted scalar; Γ-reflection = Smith-chart Möbius = SL(2,C) spinor action.

**Honest prior:** consistency-class (re-expression of canonical SU(2)/Cosserat/Hopf). The load-bearing **`(e)-genuinely-new` gate** (prereg §3): G1 structural-unification / G2 derives `α⁻¹=4π³+π²+π` / G3 longitudinal-mode discriminator. If none pass → "notation aid," not new physics (a valid verdict).

## §1 Phase plan

- **P1 — Derivation (PENDING; implementor).** The 4 derivations (closure / longitudinal / Möbius / α-structure) + the G-gate verdict + consistency-vs-emergence classification + discrimination-check (prereg §4).
- **P2 — Adjudicate (after).** Grant reviews the G-gate verdict → canonize (if a G-gate passed) or land as notation-aid result-doc.

## §2 Implementor dispatch spec (P1)

Analytical derivation, not simulation. Full discipline per prereg §5. The §3 G-gate verdict is the deliverable's spine — state it explicitly and honestly. NO target-fitting to 137.036 (forward only). Pre-commit to "consistency-class" if G1–G3 fail. Push branch; do NOT merge.

## §3 Orchestrator checkpoints

1. **G-gate verdict** — is the biquaternion genuinely-new (G1/G2/G3 passed) or consistency-class re-expression? The honest classification is the whole point.
2. **Longitudinal-mode discrimination** — is "Maxwell's deleted scalar = AVE's 7th mode" AVE-distinct + testable, or just identifiable?
3. **No overclaim** — `ave-evidence-framing` on the result-doc strength language before accepting.

## §4 Outcome (2026-06-06) — CONSISTENCY-CLASS (echo, not chord)

**Verdict: all three G-gates FAIL → the biquaternion is a notation/pedagogy aid, NOT the substrate's number system.** The pre-registered "most likely" outcome, landed honestly. Orchestrator-audited the crux verbatim.

- **G1 (unification) FAIL** — the algebra makes 4 canonical facts co-occur with algebra-internal necessity (steelmanned fully), but algebra-necessity ≠ substrate-necessity: the substrate has each for independent physical reasons; the bridge is notational. No new substrate primitive.
- **G2 (α-structure) FAIL** — **audited load-bearing finding:** the corpus EXPLICITLY makes the `4π` in `α⁻¹=4π³+π²+π` the **K4 bipartite lobe-count**, demoting "SU(2) double-cover" to a *standard-physics translation reference* ([`theorem-3-1-q-factor.md:48`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md), verbatim) — and the `π²` spin-½ provenance is *retired* (now Clifford-torus area at `R·r=¼`). The algebra generates none of the π-powers. Quaternions/SU(2) = the shadow; K4 = the thing. **EE-first vindicated.**
- **G3 (longitudinal discriminator) FAIL** — the algebra forces the scalar slot, but the substrate's 7th mode is forced by Ax 1+4. Critical no-overclaim catch: standard-Maxwell's deleted scalar is *gauge* (non-physical), AVE's 7th mode is a *real acoustic DOF* — same algebraic home, NOT a physical identity. No new number/dispersion/coupling.

**Salvaged value (consistency-class but worth keeping):** (a) the `|Γ|=1` saturation wall **is** the biquaternion null cone (zero divisors) — the Γ=−1 boundary is *why* it would be the *bi*-quaternion (real ℍ has no zero divisors); (b) **T3 holds and closes the open/short relabel** — the Smith chart IS the `SL(2,ℂ)`/Möbius spinor action; the open/short **sign is a Möbius `Z↔1/Z` convention** (sends Γ→−Γ). This is the algebraic proof behind the measured "sign is convention" conclusion.

**Prereg errors caught (KEEP-BOTH, corrected in result doc):** Γ = **Op3** not Op17 (prereg §1); §2 bundled real-space 720° with phase-space (2,3) across coordinate systems (phase-space-coordinate-check miss).

**Corpus impact: none** (cross-links only). Result doc: [`research/2026-06-06_biquaternion-node-algebra-result.md`](../research/2026-06-06_biquaternion-node-algebra-result.md). Verification script (forward-only, passes `make verify`): `src/scripts/vol_1_foundations/verify_biquaternion_node_algebra.py`. Commits 8b56961a→dea3182f.

**Follow-ons (Grant-adjudicated):** open/short primer relabel = PROCEED (T3-backed); entrainment = REFRAME substrate-native (K4/Cosserat/Kuramoto/κ_entrain), NOT biquaternion-dynamics.
