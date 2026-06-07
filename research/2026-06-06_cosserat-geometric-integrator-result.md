# Is the V0 (2,3)-degradation a flat-ℝ³ Cosserat-ω integrator artifact? (RESULT)

**Date:** 2026-06-06
**Branch:** `analysis/2026-06-06-cosserat-geometric-integrator` (worktree `AVE-Core-integrator-wt`)
**Prereg (FROZEN):** [`2026-06-06_cosserat-geometric-integrator-prereg.md`](2026-06-06_cosserat-geometric-integrator-prereg.md)
**Driver (Phase 0, NO new engine code):** `src/scripts/vol_1_foundations/r10_2_3_winding_sector_evolution_diagnostic.py`
**Reuses (UNMODIFIED):** `src/scripts/vol_1_foundations/r10_2_3_winding_extractor_coordinate.py` (the coordinate-correct extractor + Arm-C imposed control validated in [`2026-06-05_2-3-winding-extractor-result.md`](2026-06-05_2-3-winding-extractor-result.md)).

---

## §0 Headline

**VERDICT (B) — the prereg's (A) hypothesis is REFUTED. Phase 1 is NOT warranted.**

The "3"/LC half does **not** hold. Under evolution **both** halves lose their winding integer within ~2 Compton periods (w1/"2": 2→0; w2/"3": 3→1) and **both** modal coherences collapse together — w1/"2" 12/12→**5/12** (reproducing the prereg's headline number *exactly*), w2/"3" 11/12→**6/12**. The crossing invariant collapses c: 3→0 immediately. The seed (t=0) reproduces the 2026-06-05 clean-ansatz anchor exactly (w1=2 @ 12/12, w2=3 @ 11/12, c=3), so the read is the same validated tool — confirming this is a genuine evolution effect, not a tool change.

**Single mechanism (Rule 11 honest closure):** the field amplitude `A²max` blows up **>3×** (1.69 → 4.45 → 5.94, sustained ~5-6) within the first ~2-5 periods, driven by the active counter-propagating photon-precursor sources (on to ~6.5 T) atop an already-over-amplitude seed. The imposed (2,3) is **grossly disrupted in both sectors simultaneously and immediately** — not slowly leaked from the Cosserat-ω half. Because the supposedly-unitary "3"/LC half degrades just as fast as the "2"/Cosserat half, the degradation is **not** an off-group flat-Verlet integrator artifact; a geometric ω integrator addresses only the "2" half and would not prevent the "3" half's collapse. Per the prereg's pre-commitment, Phase 0 = (B) ⇒ **STOP, do not build Phase 1 (build saved); redirect to the test config / extractor**, not to the integrator.

---

## §1 Phase 0 — the diagnostic (what was run)

**The question (prereg §1).** The imposed (2,3) winding `2φ + 3ψ` splits across two engine sectors. Which half degrades under evolution?

| half | winding | substrate sector | integrator | prereg prediction |
|---|---|---|---|---|
| **w1 / "2"** | φ (major), n̂-direction | **Cosserat-ω** rotation | **flat-ℝ³ velocity-Verlet** (`cosserat_field_3d.py:1561`, half-kicks `:1555-1556/:1570-1571`) — off-group | **leaky candidate** |
| **w2 / "3"** | ψ (minor), C↔L fibre | **K4-TLM** (V_inc,V_ref) | **unitary scatter+connect** (lossless, Axiom 3) | **holds** |

**Method (reuse, not rebuild).** The driver re-runs the *unmodified* validated Arm-C imposed control (`_run_armC_full_field`, `initialize_2_3_voltage_ansatz` on the golden-torus shell, `N=48, PML=4, amplitude=0.40` — the exact original V0 config) at increasing evolution times `n_periods ∈ {0, 2, 5, 10, 20, 40}` Compton periods, and runs the coordinate-correct extractor (`shell_params_from_field` + `extract_2_3_spatial`) at each. The engine is deterministic (`temperature=0.0`, absolute-time source schedule), so each truncated run reconstructs the trajectory at that time; the `t=0` snapshot is the pristine planted ansatz (the clean-ansatz anchor). The extractor *already* reports the per-half modal coherence separately — `w1_base_modal_count / w1_base_n_walks` from the **major-φ** circle walk (the "2"), `w2_fibre_modal_count / w2_fibre_n_walks` from the **minor-ψ** circle walk (the "3") — i.e. the **12/12→5/12 metric, already split by axis**.

**Honest scope (load-bearing — flagged, not buried).** Both load-bearing windings `w1`/`w2` are read from the *same* `V_inc` internal U(1) phase `Θ = 2φ+3ψ`, decomposed by *which torus circle is walked* (major φ → w1, minor ψ → w2). This is the prereg's accepted **proxy** for the two-sector split — it is **NOT** a direct read of the Cosserat-ω state array vs the TLM V-array. The closest-to-literal sector reads (`diag_nhat_w1` from the V_inc-weighted n̂-direction; `diag_CL_w2` from the V_inc-vs-Φ_link reactance pair) are recorded alongside so a proxy/literal divergence stays visible.

---

## §2 The data — w1(t), w2(t), per-half coherence vs evolution time

Config: `N=48, PML=4, amplitude=0.40` (the exact original V0 config); total wall ≈ 644 s. Coherence shown as `modal_count / n_walks` (the 12/12→5/12 metric). `diag n̂` = `diag_nhat_w1` (n̂-direction azimuth winding); `diag CL` = `diag_CL_w2` (V_inc-vs-Φ_link reactance-pair fibre winding).

| t (T) | steps | **w1 "2"** | **coh w1** | raw w1 | **w2 "3"** | **coh w2** | raw w2 | c | diag n̂ | diag CL | R | sites | **A²max** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **0 (seed)** | 0 | **2** | **12/12** | 1.99 | **3** | **11/12** | 2.99 | **3** | 1 | 0 | 10.7 | 508 | **1.69** |
| 2 | 17 | 0 | 6/12 | 0.44 | 0 | 7/12 | 0.02 | 0 | 2 | 1 | 10.5 | 489 | 4.45 |
| 5 | 44 | 1 | 5/12 | 0.98 | 1 | 8/12 | 1.00 | 0 | 1 | 0 | 10.5 | 489 | 5.94 |
| 10 | 88 | 0 | 7/12 | 0.02 | 1 | 4/12 | 1.00 | 0 | 1 | 4 | 10.0 | 432 | 5.84 |
| 20 | 177 | 0 | 4/12 | 0.99 | 0 | 5/12 | 0.98 | 0 | 2 | 3 | 10.0 | 432 | 5.27 |
| **40 (evolved)** | 355 | **0** | **5/12** | 0.74 | **1** | **6/12** | 1.00 | **0** | 2 | 3 | 9.9 | 420 | **5.84** |

Figure: `src/scripts/vol_1_foundations/r10_2_3_winding_sector_evolution_diagnostic.png` (3 panels — winding integers w1/w2/c; per-half modal coherence with the 12/12 and 5/12 anchors; confound context A²max + n_shell_sites).

**Anchor check (determinism + reuse correctness) — PASS.** The t=0 snapshot reads **w1=2 (12/12), w2=3 (11/12), c=3** — reproducing the 2026-06-05 §2 clean-ansatz anchor (w1=2 modal 12/12, w2=3 modal 11/12) *exactly*. This confirms (i) the deterministic re-run faithfully reconstructs the trajectory, (ii) the reused extractor is unchanged, and therefore (iii) the t>0 collapse is a genuine evolution effect, not a tool artifact.

**Shell-dispersal confound check — winding loss is genuine, not "extractor lost the track".** The shell does NOT disperse: R contracts modestly 10.7→9.9 (~7 %) and n_shell_sites declines 508→420 (~17 %), so the extractor still locates a coherent ~420-site shell at t=40. The winding is genuinely scrambled *on a still-present (if eroded) shell* — ruling out the trivial "the extractor walked off the shell" explanation for the coherence drop.

---

## §3 VERDICT — (A) / (B) / (C)

_(filled on run completion)_

The discriminator is read on **two orthogonal axes**, both reported (neither buried):
- **coherence degrade** — coherence_frac (modal_count/n_walks) crossing the floor 0.60 (which separates the prereg anchors 12/12=1.00 and 5/12=0.42);
- **winding-integer loss** — the modal integer drifting off (2,3): the *genuine* topological loss, vs a coherence-only softening (the prereg's (C) "metric artifact, not winding loss").

- **(A)** w1/"2" coherence degrades, w2/"3" holds → flat Cosserat-ω velocity-Verlet is the culprit sector → Phase 1 warranted.
- **(B)** w2/"3" degrades → the supposedly-unitary V-sector or the extractor-read leaks → Phase 1 would NOT help.
- **(C)** neither winding integer drifts → 12/12→5/12 was a metric/threshold artifact, not winding loss.

### Verdict: **(B)** — both halves degrade; the "3"/LC half does not hold.

| half | seed (t=0) | evolved (t=40) | integer lost? | coherence collapse? |
|---|---|---|---|---|
| **w1 / "2"** (Cosserat-ω · flat-Verlet) | **2**, coh **12/12** | **0**, coh **5/12** | **YES** (2→0) | **YES** (1.00→0.42) |
| **w2 / "3"** (LC · unitary K4-TLM) | **3**, coh **11/12** | **1**, coh **6/12** | **YES** (3→1) | **YES** (0.92→0.50) |

`genuine_winding_loss = True` (both integers drift). The discriminator letter is **(B)**: the supposedly-unitary "3"/LC half degrades — and in fact degrades *together with*, and as fast as, the "2"/Cosserat half. **This refutes the prereg's (A) prediction that the "3"/LC half holds while only the flat-Cosserat-ω "2" half leaks.**

**The prereg's "12/12→5/12" observation is real, and it IS the w1/"2" half** (12/12→5/12 reproduced to the digit at t=40). But the (A) *interpretation* — that this is an off-group Cosserat-ω integrator leak localizable away from the unitary "3" — is wrong: the "3" half collapses 11/12→6/12 (integer 3→1) on the same ~2-period timescale.

**Single explanatory mechanism (one cause for all failures — Rule 11):** `A²max` blows up **>3×** at once (1.69→4.45 by t=2, sustained ~5-6), so the field is in a strongly over-driven, non-conserving regime from the first periods — pumped by the active counter-propagating sources (on to ~6.5 T) atop a seed whose raw port-energy density (1.69) is *already* above 1 (likely past the Op14 saturation/rupture scale A²→1; raw-Σ_p V_inc² normalization not independently re-verified here, flagged as a config observation). The (2,3) is **grossly disrupted in both sectors simultaneously**, coincident with the amplitude blow-up — not a subtle off-group winding leak. Both the `diag_nhat_w1` (n̂-direction) and `diag_CL_w2` (V_inc-vs-Φ_link reactance) literal-sector reads also wander (n̂: 1,2,1,1,2,2; CL: 0,1,0,4,3,3), consistent with global disruption rather than a clean single-sector signature.

**(C)-flavoured caveat (reported, not buried):** because the winding is read on a field driven to A²max ≈ 6, the coherence metric is partly measuring a ruptured/disrupted field rather than a coherent (2,3) — so "12/12→5/12" is *also* in part a metric-on-disrupted-field signal, not a clean conservation measurement. (B) and this (C)-caveat agree on the actionable conclusion.

**Phase-1 warrant: NO.** Phase 1 (an SO(3)-geometric ω integrator) addresses only the "2"/Cosserat half. Since the "3"/LC half degrades just as fast (and the whole field is over-driven), a geometric integrator cannot resolve the V0 degradation. Per the prereg's pre-commitment (Phase 0 = (B) ⇒ STOP), the geometric-integrator build is **saved**, not undertaken.

### Redirect (per prereg (B): "redirect to the extractor/TLM, build saved")

The indicated next questions — *surfaced for orchestrator/Grant adjudication, NOT scaffolded here* (lane discipline + Rule 16):
1. **Test config / conservation regime.** The Arm-C control (amplitude 0.40 + active counter-propagating sources) over-drives the field past saturation, so it is **not a clean conservation test** of any integrator's group-preservation. A genuine integrator-conservation test needs a quasi-stable (2,3) where `A²max` stays ≈ constant (lower amplitude, sources off / relaxed bound state). Whether such a regime exists for the imposed (2,3) is the prior open question.
2. **Extractor on an over-saturated field.** Characterize the modal-coherence metric's behaviour when A²max ≫ 1 (is the 12/12→5/12 the metric reading disruption-noise?).
3. The flat-vs-geometric ω integrator comparison remains *physically motivated* (off-group integration is a real numerical defect) but is **not the cause of V0** and would not be evidenced by this control.

---

## §4 Discipline walk (which skills fired)

- **`substrate-native-check`** — CP1: the driver writes NO solver; it controls *snapshot cadence* on the engine's own velocity-Verlet wave-propagation step (no gradient-descent/energy-min construct introduced; the leaky candidate is the Verlet ω-add `:1561`, diagnosed not changed). CP2: the (2,3) splits V-sector (K4-TLM, unitary) × Cos-sector (Cosserat-ω, Verlet); `w1`="2"=Cos (candidate), `w2`="3"=V (holds). CP4: load-bearing winding read in phase-space `Θ=2φ+3ψ` (matches the corpus claim); the torus circle is located in real-space from `|V_inc|²` density crest — the *validated* hybrid extractor design, flagged not assumed. CP6: both reactance halves recorded — `V_inc` (C-state) drives w1/w2 + `diag_nhat_w1`; `Φ_link` (L-state) drives `diag_CL_w2` (degenerate at the seed: the ansatz plants `V_inc≡Φ_link` in phase, so `diag_CL` only sharpens as `Φ_link` develops quadrature). CP7: extractor PML-excludes every ring point + locates the shell by density crest, not centroid (reused unchanged). CP8: **N/A** — the (2,3) is IMPOSED; this is winding-CONSERVATION-under-evolution, not a hosting test.
- **`phase-space-coordinate-check`** — corpus claim (2,3) lives in phase-space `Θ` on the Clifford torus; the test reads `Θ` winding (major→w1, minor→w2). MATCH on the winding observable. The "2"↔Cosserat / "3"↔LC sector attribution is the prereg's accepted spatial-circle **proxy**, not a direct ω-array vs V-array read; the literal-sector diagnostics (`diag_nhat_w1`, `diag_CL_w2`) are reported so a proxy/literal divergence is visible.
- **`ave-canonical-source`** — `ALPHA` imported from `ave.core.constants` (`0.0072973525693`); `PHI`/`DT`/`COMPTON_PERIOD` reused from the extractor module. No fresh physics literals. (`N`, `PML`, `amplitude`, snapshot cadence are honestly-tagged engineering/config choices.)
- **`ave-driver-script-honesty`** — forward READ of a KNOWN-imposed signal: NO `minimize`/`curve_fit`, NO parameter tuned toward (2,3). The verdict is computed from seed→evolved deltas via a transparent printed rule (`classify_verdict`), not hand-set.
- **`consistency-vs-emergence`** — TOOL/integrator diagnostic on an IMPOSED control: **consistency** class, not emergence; no α / hosting / CODATA claim.
- **`ave-evidence-framing-discipline`** — the verdict A/B/C is stated from the data; per the prereg pre-commitment, (B)/(C) honestly **refute** the integrator hypothesis (a valid, expected outcome) and Phase 1 is NOT built unless (A).

**Citation-fix flag (verify-before-cite / flag-don't-fix).** The prereg cites `cosserat_field_3d.py:818,825,841` for the velocity-Verlet ω-integration. Those lines are the state **declarations** (`self.omega = np.zeros(...)` `:818`, `self.omega_dot = np.zeros_like(...)` `:825`, the Lagrangian comment `:841`). The actual flat-vector ω **integration step** is in `step_velocity_verlet` at `:1533-1571` — specifically `self.omega = self.omega + dt * self.omega_dot` (`:1561`) with half-kicks at `:1555-1556` / `:1570-1571`, and the quaternion form is used only for the observable `ω→n̂` projection (`_project_omega_to_nhat`, `:188-192`), never the integration. The prereg's substantive claim (flat-ℝ³ velocity-Verlet integrates ω off-group; quaternion only for the observable) is **CONFIRMED**; only the line references needed correcting.

---

## §5 Artifacts

- Phase-0 driver: `src/scripts/vol_1_foundations/r10_2_3_winding_sector_evolution_diagnostic.py`
- Results JSON: `src/scripts/vol_1_foundations/r10_2_3_winding_sector_evolution_diagnostic_results.json`
- Figure: `src/scripts/vol_1_foundations/r10_2_3_winding_sector_evolution_diagnostic.png`
- Reused (unmodified) extractor: `src/scripts/vol_1_foundations/r10_2_3_winding_extractor_coordinate.py`
