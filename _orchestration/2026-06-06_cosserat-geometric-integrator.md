# Cosserat SO(3)-geometric integrator (orchestration)

**Date:** 2026-06-06 · **Branch:** `analysis/2026-06-06-cosserat-geometric-integrator` (off `origin/main` `005e1574`; worktree `AVE-Core-integrator-wt`)
**Prereg (FROZEN):** [`research/2026-06-06_cosserat-geometric-integrator-prereg.md`](../research/2026-06-06_cosserat-geometric-integrator-prereg.md)
**Session:** orchestration (Grant in-session). Branch + reviewed PR; no direct-to-main.

## §0 What

Test whether the V0-fork (2,3) degradation (Arm-C evolved, modal coherence 12/12→5/12) is a **flat-ℝ³ Cosserat-ω integrator artifact**. `substrate-native-check` CP2 sharpening: the (2,3)=2φ+3ψ is two-sector — the **"2"/φ (Cosserat-ω)** is on the leaky flat velocity-Verlet; the **"3"/ψ (C↔L fibre)** is on the **unitary** K4-TLM scatter (already structure-preserving — "conserving is the LC's job," Grant). **Diagnose-first.**

## §1 Phase plan

- **P0 — diagnostic (PENDING; implementor; NO new engine code).** Re-run Arm-C evolution + the extractor; split the degradation into `w1`(the "2"/Cosserat) vs `w2`(the "3"/LC) vs time. Prediction: "2" leaks, "3" holds (A). Outcomes (B) "3" also leaks → integrator won't help, redirect; (C) neither → metric artifact.
- **P1 — geometric integrator (CONDITIONAL on P0=(A)).** Add SO(3)/quaternion-exp-map ω-integrator (KEEP-BOTH flag); re-run Arm-C flat-Verlet vs geometric; does it conserve the "2"?

## §1.5 Phase 0.5 — quasi-stable (2,3) survival test (REDIRECT, Grant-greenlit 2026-06-06)

Phase-0 (B) showed the Arm-C control over-saturates (`A²max=1.69` seed → ~6 pumped), so V0 never had a clean conservation regime. Find one and re-test survival.
- **Key variable: sources-OFF free evolution** (impose the (2,3), kill the pumping sources → `A²max` can't be pumped past saturation) × an **amplitude sweep** (~0.10–0.40; `A²max=1` ≈ amp 0.31). Use the observable battery channels (saturation/regime + `A²max(t)`, the (2,3) extractor `w1/w2`, retention) — the amplitude-sweep is finally pointed at its purpose.
- **Find the Goldilocks band:** amplitude (sources-off) where the (2,3) *forms* (extractor recovers 2,3 at seed) AND `A²max(t) ≈ const` (sub-saturation, quasi-stable).
- **Re-test survival there:** does `w1=2 / w2=3` hold over evolution, or degrade?

**Discriminators:** **(I)** band exists + (2,3) survives → physically conserved; V0 "fail" was purely over-saturation → fork RESOLVED (the (2,3) is innocent). **(II)** band exists + (2,3) degrades → genuine physics degradation, independent of amplitude. **(III)** no band (the (2,3) only forms *with* saturation) → the imposed-(2,3) ansatz can't be both formed and stable (a seed/ansatz finding). Honest report of whichever; `substrate-native-check` CP8 (sources-off free evolution is closer to precursor-not-plant; note the imposed-(2,3) is still a plant).

## §2 Orchestrator checkpoints

1. **P0 verdict** — which half degrades (A/B/C)? Gates whether P1 is built at all (don't build the integrator unless the leak is in its sector).
2. **P1 discriminator** — geometric conserves the "2" where flat-Verlet leaked? → V0 resolved + engine improved, or integrator-not-the-cause.
3. `ave-evidence-framing` — no "integrator fixes it" until P0 confirms the sector + P1 measures it.

## §3 Outcome (2026-06-06) — verdict (B): REFUTED; Phase 1 NOT built; V0 re-diagnosed

**Diagnose-first worked — it refuted the hypothesis cheaply, before any engine surgery.** Verdict **(B)**: the "3"/LC half does NOT hold. **Both** sectors collapse together within ~2 Compton periods (`w1`/"2": 2→0 @ 12/12→**5/12**; `w2`/"3": 3→1 @ 11/12→**6/12**; both coherence-collapse confirmed). NOT a localized flat-Cosserat-ω leak.

**Real mechanism (Rule 11 honest closure):** the Arm-C control is **over-saturated** — `A²max = 1.69` at the *seed* (>1!), blows to ~6 under the pumping sources. The (2,3) is *destroyed by over-amplitude in both sectors simultaneously*, not leaked from one by the integrator. A geometric ω-integrator fixes only the "2" → cannot resolve V0. **Phase 1 build SAVED** per the (B)=STOP pre-commitment.

**V0 fork re-diagnosed (a 4th possibility):** the evolved-Arm-C "12/12→5/12 fail" is a **bad-test-regime artifact (over-saturation)**, NOT physics-degradation / tool-contamination / integrator-leak. The original V0 tested winding-survival on a *blown-up* field — so it says nothing about whether the (2,3) is physically conserved. (The LC-projects intuition is NOT refuted — the regime is just too violent to test conservation at all. Aligns with `substrate-native-check` CP8: Arm-C plants the *over-amplitude finished composite* — the anti-pattern.)

**Redirect (indicated, not built):** to test (2,3) survival (and any integrator), need a **quasi-stable (2,3)** where `A²max ≈ const` — via lower amplitude (obs-battery amplitude-sweep; my earlier mini-sweep had amp 0.30 sub-saturation) and/or sources-off free evolution. THEN re-test survival.

**Validity checks PASS:** t=0 seed reproduces the 2026-06-05 clean-ansatz anchor exactly (determinism confirmed); shell does not disperse (extractor not at fault). **Citation-fix:** prereg cited `:818,825,841` (state *declarations*); actual flat-vector ω-integration is `step_velocity_verlet:1561` (substantive claim confirmed). Branch `analysis/2026-06-06-cosserat-geometric-integrator` (commits 9216d8f4, eb5d7ebb); `make verify` passed.
