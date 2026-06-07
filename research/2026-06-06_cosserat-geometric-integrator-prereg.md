# Is the V0 (2,3)-degradation a flat-ℝ³ Cosserat-ω integrator artifact? (PREREG, FROZEN)

**Date:** 2026-06-06
**Branch:** `analysis/2026-06-06-cosserat-geometric-integrator` (off `origin/main` `005e1574`; worktree `AVE-Core-integrator-wt`)
**Status:** PREREG FROZEN — Phase 0 (diagnostic) pending. Session: orchestration (Grant in-session).
**Origin:** Grant 2026-06-06 — "does the quaternion picture help a better simulation implementation?" → the engine integrates the **SO(3)-valued Cosserat ω as a flat ℝ³ vector via velocity-Verlet** (`cosserat_field_3d.py:818,825,841`); the quaternion form is used only for the *observable* `ω→n̂` projection (`:190-192`), never the integration. Hypothesis: the flat integrator leaks the topological winding (lattice-gauge-theory style), and that — not physics — is the open V0 fork (Arm-C evolved (2,3) modal coherence 12/12→5/12).

---

## §0 Open goal + the substrate-native sharpening

**Open goal:** prove-or-disprove that the V0 (2,3)-degradation under evolution is a **numerical artifact of integrating the Cosserat-ω rotation sector off-group** (flat ℝ³ velocity-Verlet), rather than physics-degradation or extractor-contamination.

**`substrate-native-check` Checkpoint-2 sharpening (load-bearing — re-scoped the test):** the (2,3) winding `2φ + 3ψ` lives in **two engine sectors**:
- **`φ` / the "2" (n̂-direction)** = Cosserat-ω rotation → **flat-ℝ³ velocity-Verlet** (off-group; *leaky candidate*).
- **`ψ` / the "3" (C↔L fibre)** = (V_inc, V_ref) phase → **K4-TLM scatter+connect**, which is **unitary by construction** (lossless network, eigenvalues on the unit circle; Axiom 3 lossless reactive cycling) → **already structure-preserving**.

So a quaternion/SO(3) integrator fixes ONLY the **"2"** half, and only matters if the leak is there. **Physical anchor (Grant):** the LC is the lossless reactive cycle that *projects* the phase-space winding to the real-space soliton — *conserving is its job* — so the **"3"/LC half should hold**; the **"2"/Cosserat half is the fragile one**. This is a falsifiable prediction, so we DIAGNOSE before building.

Substrate-native walk: **CP1** Cosserat dynamics is genuine *wave propagation* (the velocity-Verlet LC oscillator `L=½I_ω|ω̇|²−W`), NOT the gradient-descent *settling* mode at `:1285/:1384` — the geometric swap keeps it wave-propagation, group-respecting. **CP2** two-sector (above). **CP4** measure in phase-space coords — the extractor reports `w1`(the "2") and `w2`(the "3") separately, which IS the split we need.

---

## §1 Phase 0 — the diagnostic (cheap, NO new engine code)

Re-run the **Arm-C imposed-(2,3) evolution** (the V0 control; `_run_armC_full_field`) on the *existing* engine + the coordinate-correct extractor (`extract_2_3_spatial`), reading `w1_base` (the "2"/Cosserat-ω/n̂-direction) and `w2_fibre` (the "3"/C↔L/V-sector) **as a function of evolution time** (e.g. snapshots over n_periods), plus the modal-coherence/confidence (`modal_count`, `n_walks`) per half.

**Discriminator (the falsifiable prediction):**
- **(A) "2" degrades, "3" holds** → the flat Cosserat-ω integrator IS the culprit → build Phase 1.
- **(B) "3" also degrades** → surprising (TLM is unitary); the leak is the extractor-read or deeper — a geometric integrator would NOT help → STOP, redirect to the extractor/TLM (build saved).
- **(C) neither degrades cleanly** → the 12/12→5/12 was a measurement/threshold artifact, not winding loss → re-examine the extractor's modal-coherence metric.

Honest tags + forward reads only (`ave-driver-script-honesty`); no fitting. Report the `w1`/`w2`-vs-time curves + the per-half coherence.

---

## §2 Phase 1 — the geometric integrator (CONDITIONAL on Phase 0 = (A))

Only if Phase 0 shows the **"2"/Cosserat half leaks**: add an **SO(3)-geometric integrator option** to the Cosserat-ω update — integrate the rotation **on the group** via the quaternion exponential map (compose rotations: `q_{n+1}=exp(½Δθ)⊗q_n`), instead of flat-vector addition (`ω+=ω̇·dt`). **KEEP-BOTH:** the flat-Verlet stays the default behind a flag; the geometric scheme is opt-in. Respect the K4-bipartite + Cosserat structure (`substrate-native-check`); constants from `ave.core.constants`.

Then re-run Arm-C with **both** integrators (matched amplitude / n_periods / seed — the *only* difference is the ω-integration scheme), and compare `w1` survival.

**Discriminator:** does the geometric integrator **conserve the "2"** where flat-Verlet leaked it (12/12 retained vs →5/12)?
- **YES** → the V0 degradation was an integrator artifact; the (2,3) is physically conserved (vindicating the topological-protection argument); engine improved. Promote the geometric integrator.
- **NO** → the "2" leak is NOT integrator-induced (physics, or the Verlet wasn't the issue) → the geometric integrator is a (minor) numerical improvement but does not resolve V0.

---

## §3 Discipline + honest priors

`substrate-native-check` (CP1/2/4 walked; §0) · `phase-space-coordinate-check` (the "2"/"3" split IS the coordinate discipline) · `ave-prereg` (no prior AVE geometric-integrator work; new territory) · `ave-driver-script-honesty` (forward reads, no fit) · `consistency-vs-emergence` (this is a TOOL/integrator test + winding-CONSERVATION under the imposed Arm-C control, NOT an emergence/hosting claim — CP8 satisfied by the validated imposed control) · `ave-canonical-source` · `ave-evidence-framing` (do NOT pre-claim "the integrator fixes it" — Phase 0 must confirm the sector first).

**Honest priors:** the architecture + the LC-projects physics both predict outcome **(A)** then a Phase-1 **YES**. But it is genuinely falsifiable — outcome (B)/(C) (the leak is in the unitary V-sector or the metric) would REFUTE the integrator hypothesis and redirect to the extractor. Pre-commit to reporting (B)/(C) honestly and NOT building Phase 1 if Phase 0 ≠ (A).

**Deliverable:** `research/2026-06-06_cosserat-geometric-integrator-result.md` (the Phase-0 w1/w2-vs-time split + verdict; Phase-1 comparison if built). Reviewed PR; no merge.
