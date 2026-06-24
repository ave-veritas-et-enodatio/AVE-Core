# RESULT — Mass-Sector Two-Body Scattering: validate-on-known (gravity) on the scalar A1 engine

**Date:** 2026-06-23
**Status:** DRIVER-COMPLETE, VERDICT GATED. The two-pronged validate-on-known leans **NULL/BELOW-FLOOR (O1) + phase-DEPENDENT field-overlap (O2)** on the smoke; the FROZEN multi-separation run is held pending Grant's §0.5 observable ruling (the centroid-drift readout is not viable on this transport-less engine — see Finding 2). Reported honestly per Rule 11; no rescue attempted.
**Prereg:** [`2026-06-23_mass-sector-two-body-scattering_prereg.md`](2026-06-23_mass-sector-two-body-scattering_prereg.md) (§0.5 gate open; §0.6 empirical findings).
**Driver:** [`src/scripts/vol_1_foundations/mass_sector_two_body_scattering.py`](../src/scripts/vol_1_foundations/mass_sector_two_body_scattering.py)
**Branch:** `analysis/soliton-mass-scattering` (PR for orchestrator audit + Grant merge pending; NO self-merge).

---

## 1. The two-pronged verdict (honest, gated)

The validate-on-known asks two questions at b=0, head-on, BOTH relative phases:
- **(i) attractive?** (matching AVE-gravity mass-mass sign, `optical-refraction-gravity.md:13`)
- **(ii) phase-independent (→ gravity) or phase-dependent (→ generic soliton)?**

**(i) sign — INCONCLUSIVE via centroid drift (all separations).** The O1 centroid-drift readout is **swamped by the radiation floor**: a single isolated breather's centroid wanders **2.3-2.9 cells** over the recording window (pure radiation/breathing jitter, zero initial velocity), while the two-body net drift is at or below that floor at every separation:

| d₀ (cells) | O0 floor | O1 in-phase net dsep | O1 out-phase net dsep | bin |
|---|---|---|---|---|
| 5 | 2.52 | +4.66 (repel-ish, but interference-dominated, A²_mid 0.82) | −1.12 (below floor) | MIXED/AMBIGUOUS |
| 7 | 2.34 | +0.88 (below floor) | −1.34 (below floor) | NULL/BELOW-FLOOR |
| 9 | 2.93 | −0.007 (≈0) | −0.049 (≈0) | NULL/BELOW-FLOOR |

The engine cannot transduce a two-body force into measurable centroid motion (corroborates DEV-6 zero-transport at integrator time). At d₀=9 the drift is essentially zero at BOTH phases. → **O1 verdict: NULL/BELOW-FLOOR (no measurable force).**

**(ii) phase-(in)dependence — PHASE-DEPENDENT on the only measurable field signal (all separations).** The O2 mechanism witness (midplane saturation depth A²) is sharply phase-dependent at every separation: in-phase midplane A² ≈ 0.56-0.82 (constructive fill); out-phase A² ≈ 1e-3 (destructive cancel). This is the **textbook generic-soliton coherent-overlap signature** — exactly the guard's P2-refute. It is field interference, not a transduced force. The O3 witness additionally caught the in-phase constructive overlap driving `core_A²_peak` to 1.21 at d₀=9 (Regime-III rupture territory, engine-clipped) — another generic-soliton, non-gravity signature (gravity does not push masses toward dielectric rupture by bringing them together). → **O2 verdict: PHASE-DEPENDENT (generic NLS overlap), NOT phase-independent gravity.**

**Combined:** on this scalar A1 engine, two-body scattering yields **no measurable force via centroid drift (O1 NULL)** and **a phase-dependent field-overlap (O2 generic-soliton)**. Neither prong supports a phase-independent gravitational attraction. **The engine cannot validate mass-mass gravity by two-body scattering** — a WALL-engine capability finding, NOT a gravity falsification (the gravity ontology is real per `optical-refraction-gravity.md`; this engine simply lacks the transport channel to convert the optical-refraction gradient into a measurable force).

---

## 2. CONSISTENCY vs CHORD label (ave-discrimination-check)

**Label: neither a CHORD nor a clean CONSISTENCY pass — a WALL-engine NULL.** The validate-on-known did not pass (no phase-independent attraction was measurable), so there is no positive result to label. Had it passed, it would have been a Class-C two-body gravity **CONSISTENCY** check (AVE-gravity is FORM-derived/VALUE-imported MIXED, `optical-refraction-gravity.md:52`; Newtonian gravity predicts the same attractive sign → no SM-discrimination). The chord-watch (short-range S(A)-saturation correction to 1/r) never came into reach because the force itself was unmeasurable.

**No over-claim.** This result is explicitly NOT "AVE gravity confirmed" and NOT "AVE gravity falsified." It is "this engine cannot run this test as a force measurement."

---

## 3. Two flagged findings (Rule 10 / flag-don't-fix)

**FINDING 1 — brief seed-spec mismatch (corrected).** The brief's stated Mode-I seed (N=32, 0.95·V_yield, R=2.0, center-cell metric, r10 Test C) FAILS r10 Test C's own C1 persistence gate on HEAD (`V_center_ratio=−0.089`, threshold 0.5; the bare sech disperses). The VALIDATED canonical Mode-I (`test_master_equation_v14_mode_i.py`, 5/5 PASS on HEAD) is the breathing soliton at N=24, DX=0.5, V_yield=1.0, amp=0.85, R=2.5, V_peak metric. Driver uses the validated config. *Engine + validated Mode-I are sound; the brief's seed numbers are the error.*

**FINDING 2 — centroid-drift is not a viable force readout on this engine.** Single-blob radiation floor (2.34 cells) exceeds any two-body drift at d₀∈{5,7,9}. Confirms DEV-6 (`annihilation_evaporation_run.py:46-50`). The viable observable, if any, is a momentum-flux / stress-tensor readout that does not require rigid transport — this is the §0.5 question to Grant.

---

## 4. Recommendation

**phase-dependent-so-not-gravity (on the measurable field signal) + WALL-engine on the force signal → do NOT proceed to the σ(b,v) sweep on this engine.** The scalar A1 engine's two-body interaction is generic-soliton field-overlap (phase-dependent), and its force readout (centroid drift) is below the radiation floor. Specifically:

1. **HOLD the σ(b, v_rel) sweep (§8 proposal).** It was conditional on a GRAVITY-CONSISTENT pass; the pass did not occur. Building the sweep now would be debugging-toward-a-rescue (Rule 11).
2. **Surface the §0.5 observable question to Grant** before any further work: is there a transport-independent force observable (momentum flux through the midplane, the field stress-tensor T_0x integrated over the gap) you'd accept on this engine? If yes, the test could be re-instrumented to discriminate gravity from generic-soliton WITHOUT requiring centroid transport. If no, this engine is the wrong instrument for two-body gravity and the (a)-route closes WALL-engine.
3. **Deferred-conditional follow-on (NOTE only, NOT built):** (b) charge-sector e-e scattering on the **Cosserat (2,3) engine** is the high-value forward target (a same-sign Coulomb repulsion would be an AVE-distinct test the mass sector cannot reach), requiring the winding carrier the scalar A1 engine lacks. Out of scope here per Grant's ruling; build only if fundamentally needed, in a later session.

---

## 5. What survives

- A clean, validated **driver** that runs both phases at multiple separations with PML-excluded V_peak centroids + A²-overlap witness + single-blob radiation-floor control — reusable the moment a transport-independent observable is chosen.
- The **seed-spec correction** (Finding 1): future mass-sector drivers should seed the validated v14 breather config, not the brief's r10-literal numbers.
- The **WALL-engine localization** (Finding 2): the scalar A1 engine measures field-overlap, not force — pinning exactly which capability the engine lacks (transport / momentum-flux instrumentation) for the next engine choice.
