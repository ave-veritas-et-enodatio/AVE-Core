# Cosserat SO(3)-geometric integrator (orchestration)

**Date:** 2026-06-06 · **Branch:** `analysis/2026-06-06-cosserat-geometric-integrator` (off `origin/main` `005e1574`; worktree `AVE-Core-integrator-wt`)
**Prereg (FROZEN):** [`research/2026-06-06_cosserat-geometric-integrator-prereg.md`](../research/2026-06-06_cosserat-geometric-integrator-prereg.md)
**Session:** orchestration (Grant in-session). Branch + reviewed PR; no direct-to-main.

## §0 What

Test whether the V0-fork (2,3) degradation (Arm-C evolved, modal coherence 12/12→5/12) is a **flat-ℝ³ Cosserat-ω integrator artifact**. `substrate-native-check` CP2 sharpening: the (2,3)=2φ+3ψ is two-sector — the **"2"/φ (Cosserat-ω)** is on the leaky flat velocity-Verlet; the **"3"/ψ (C↔L fibre)** is on the **unitary** K4-TLM scatter (already structure-preserving — "conserving is the LC's job," Grant). **Diagnose-first.**

## §1 Phase plan

- **P0 — diagnostic (PENDING; implementor; NO new engine code).** Re-run Arm-C evolution + the extractor; split the degradation into `w1`(the "2"/Cosserat) vs `w2`(the "3"/LC) vs time. Prediction: "2" leaks, "3" holds (A). Outcomes (B) "3" also leaks → integrator won't help, redirect; (C) neither → metric artifact.
- **P1 — geometric integrator (CONDITIONAL on P0=(A)).** Add SO(3)/quaternion-exp-map ω-integrator (KEEP-BOTH flag); re-run Arm-C flat-Verlet vs geometric; does it conserve the "2"?

## §2 Orchestrator checkpoints

1. **P0 verdict** — which half degrades (A/B/C)? Gates whether P1 is built at all (don't build the integrator unless the leak is in its sector).
2. **P1 discriminator** — geometric conserves the "2" where flat-Verlet leaked? → V0 resolved + engine improved, or integrator-not-the-cause.
3. `ave-evidence-framing` — no "integrator fixes it" until P0 confirms the sector + P1 measures it.

## §3 Outcome

_(filled on implementor return)_
