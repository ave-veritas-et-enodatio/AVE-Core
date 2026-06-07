# Is the V0 (2,3)-degradation a flat-ℝ³ Cosserat-ω integrator artifact? (RESULT)

**Date:** 2026-06-06
**Branch:** `analysis/2026-06-06-cosserat-geometric-integrator` (worktree `AVE-Core-integrator-wt`)
**Prereg (FROZEN):** [`2026-06-06_cosserat-geometric-integrator-prereg.md`](2026-06-06_cosserat-geometric-integrator-prereg.md)
**Driver (Phase 0, NO new engine code):** `src/scripts/vol_1_foundations/r10_2_3_winding_sector_evolution_diagnostic.py`
**Reuses (UNMODIFIED):** `src/scripts/vol_1_foundations/r10_2_3_winding_extractor_coordinate.py` (the coordinate-correct extractor + Arm-C imposed control validated in [`2026-06-05_2-3-winding-extractor-result.md`](2026-06-05_2-3-winding-extractor-result.md)).

**Phases in this doc:** **§0–§5 = Phase 0** (sector-split diagnostic → verdict **(B)**: over-saturation, not integrator-leak; Phase 1 saved). **Phase 0.5** (appended below, REDIRECT) re-tests survival in a quasi-stable sub-saturation regime → verdict **(II)**: the regime exists and the imposed (2,3) **degrades genuinely** there (amplitude-independent), refining (B) — the degradation is NOT merely an over-saturation artifact.

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

---

# Phase 0.5 — quasi-stable (2,3) survival re-test (REDIRECT, Grant-greenlit 2026-06-06)

**Driver (Phase 0.5, NO new engine code):** `src/scripts/vol_1_foundations/r10_2_3_winding_quasistable_survival.py`
**Reuses (UNMODIFIED):** `r10_2_3_winding_extractor_coordinate.py` (the validated extractor + the Arm-C imposed control + `initialize_2_3_voltage_ansatz`).

## §0.5 Headline — VERDICT (II)

**A quasi-stable (sub-saturation) (2,3) regime DOES exist — and the imposed (2,3) DEGRADES in it, at every amplitude.** Phase-0 (B) diagnosed the Arm-C blow-up as over-saturation and left open whether the (2,3) is *conserved-but-untested-in-a-too-violent-regime*. Phase 0.5 builds the gentle regime (sources-OFF free evolution + an amplitude sweep) and re-tests survival there. Result: the imposed (2,3) is disrupted within ~2–10 Compton periods **even at `A²max ≈ 0.07` — 14× below the rupture wall** — at the same rate as at the over-driven config. So the V0 degradation is **genuine and amplitude-independent, NOT an over-saturation artifact** (the discriminator-(I) "the (2,3) is innocent" reading is REFUTED).

**Honest scope (load-bearing — flagged, not buried).** This (II) is a finding about **the imposed all-C-state (2,3) PLANT** (the exact V0 Arm-C initial condition: `initialize_2_3_voltage_ansatz` writes `V_inc` only, `Φ_link=0` at the seed). It does **NOT** by itself refute winding-conservation for a *properly-hosted* (precursor-grown) electron. It shows the planted finished-composite (2,3) is **not a self-consistent standing solution** of the K4+Cosserat engine — exactly the `substrate-native-check` CP8 anti-pattern outcome (plant-the-end-state → degrades). Two untested variants (a balanced-LC seed; a precursor-grown (2,3)) are surfaced in §0.5.5, NOT scaffolded (lane discipline + Rule 16).

## §0.5.1 Method — sources-OFF free evolution + amplitude sweep

The **key variable** is the pumping: build the SAME imposed-(2,3) seed on the SAME golden-torus shell, then evolve **WITHOUT** the counter-propagating `SpatialDipoleCPSource` sources AND without the `PairNucleationGate` injection (a saturation-triggered side-effect observer, `vacuum_engine.py:1172`), so `A²max` cannot be pumped past saturation — it can only settle/decay. **Faithful-reuse audit (pre-commit):** the sources-off engine `from_args(...)` config and the ansatz placement (`R=0.22N`, `r=R/φ²`) are **byte-identical** to Arm-C (`_run_armC_full_field`); the ONLY difference is the absence of the sources + gate, so sources-ON vs sources-OFF is a single-variable comparison at matched amplitude.

The ansatz envelope is linear in `amplitude` (`tlm_…_eigenmode.py:78,121`), so seed `A²max ∝ amplitude²` — a **forward prediction** (NOT a fit): measured seeds `{0.106, 0.238, 0.423, 0.662, 0.953, 1.694}` vs predicted `1.69·(amp/0.40)² = {0.106, 0.238, 0.422, 0.660, 0.951, 1.690}` — exact. `A²max=1` (the rupture wall) ≈ amp 0.31.

**Anchored validity check (determinism + reuse correctness) — PASS.** At `t=0`, ALL six amplitudes read **w1=2 (12/12), w2=3 (11/12), c=3** — reproducing the 2026-06-05 clean-ansatz anchor and the Phase-0 seed exactly. The deterministic engine + unchanged extractor → the `t>0` evolution is a genuine effect, not a tool change.

## §0.5.2 `A²max(t)` — sources-ON (Arm-C) vs sources-OFF (free evolution)

| config | t=0 | t=2 | t=5 | t=10 | regime |
|---|---|---|---|---|---|
| **ON amp 0.40** (Arm-C, Phase-0) | **1.69** | 4.45 | 5.94 | 5.84 | blows to ~6 (pumped) |
| **OFF amp 0.40** (free) | **1.69** | 3.11 (peak) | — | — | self-blows to ~3 (no sources) |
| **ON amp 0.20** | **0.42** | 0.38 | 0.42 | 0.29 | stays ~0.4 (sub-wall) |
| **OFF amp 0.20** (free) | **0.42** | → 0.61 (peak) | — | — | stays sub-wall, settles |

Two findings: (i) **the sources only over-saturate an already-near/over-wall seed** — at amp 0.40 they push `A²max` 3→6, but at amp 0.20 the field stays sub-wall (~0.4) with OR without sources; (ii) an **over-wall seed self-amplifies even sources-OFF** (amp 0.40: 1.69→3.11). So Phase-0's "Arm-C over-saturates" is the amp-0.40 high-seed config specifically, and the over-amplitude is partly intrinsic to the over-wall seed, not solely the sources.

## §0.5.3 Goldilocks-band map (sources-OFF)

`quasi-stable` ≡ `A²max(t)` never reaches the wall `A²→1` over the whole evolution. `survived` ≡ winding integers (2,3) hold at the **last two** snapshots (sustained — robust to the LC-equilibration transient; a single-frame recovery does NOT count). Figure: `r10_2_3_winding_quasistable_survival.png`.

| amp | A²seed | A²peak | Φ²peak | quasi-stable | **survived** | seed→evolved (w1,w2) | t_first_loss |
|---|---|---|---|---|---|---|---|
| **0.10** | 0.106 | **0.152** | 0.074 | ✅ | ❌ | (2,3)→(0,1) | 10 T |
| **0.15** | 0.238 | **0.343** | 0.166 | ✅ | ❌ | (2,3)→(0,1) | 10 T |
| **0.20** | 0.423 | **0.612** | 0.701 | ✅ | ❌ | (2,3)→(0,1) | 2 T |
| **0.25** | 0.662 | **0.964** | 9.18 | ✅ | ❌ | (2,3)→(0,1) | 2 T |
| 0.30 | 0.953 | 1.405 | 1.9e4 | ❌ (self-blows) | ❌ | (2,3)→(1,1) | 2 T |
| 0.40 | 1.694 | 3.108 | 4.5e4 | ❌ (self-blows) | ❌ | (2,3)→(1,1) | 2 T |

**Quasi-stable band = amps {0.10, 0.15, 0.20, 0.25}** (`A²max` stays 0.07–0.96, never detonates). **Survived band = ∅.** The (2,3) degrades in 100 % of the quasi-stable band.

**Self-amplification edge (new finding).** The `Φ²max` (L-store) column is the tell: sub-wall seeds (amp ≤ 0.20) keep `Φ²` bounded (≤ 0.70); the near-wall seed (0.25) starts climbing (9.2); over-wall seeds (0.30, 0.40) **explode** (1.9e4, 4.5e4). A **sources-free** near-wall instability: as the C-store (`A²`) approaches saturation, the L-store (`Φ_link`) runs away. This is distinct from the Phase-0 sources-pumped blow-up and is its own (separately-reported) result.

## §0.5.4 Survival re-test — `w1/w2` per snapshot (the quasi-stable band)

Per-snapshot winding integers (sources-OFF); seed coherence is 12/12, 11/12 at every amplitude:

| amp | t=0 | t=2 | t=5 | t=10 | t=20 | t=40 |
|---|---|---|---|---|---|---|
| 0.10 | (2,3) | (2,3) | (2,3) | (1,2) | (2,3) | **(0,1)** |
| 0.15 | (2,3) | (2,3) | (2,3) | (1,2) | (2,2) | **(0,1)** |
| 0.20 | (2,3) | (2,2) | (2,3) | (1,0) | (0,2) | **(0,1)** |
| 0.25 | (2,3) | (2,2) | (2,3) | (1,0) | (1,1) | **(0,1)** |

The winding integers hold cleanly only for the first ~5 T, then **wander off (2,3)** and never sustainably return; the modal **coherence collapses immediately** — 12/12 → 5–8/12 by t=2 and stays split for the rest of the evolution (it never recovers to the unanimous 12/12 of the seed). The unanimous-12/12-vote → split-5/12-vote IS the degradation signal: the field is disrupted into a low-coherence state where the (2,3) is no longer a clean single winding. This is genuine field evolution (the load-bearing `w1/w2` read `V_inc`'s spatial 2φ+3ψ pattern, which is disrupted as the field evolves), not extractor noise.

## §0.5.5 Verdict (II) + mechanism + honest scope

**VERDICT (II): a quasi-stable sub-saturation (2,3) regime exists, and the imposed (2,3) degrades there — genuine physics degradation, independent of amplitude.** The driver's transparent rule returns (II): band `{0.10, 0.15, 0.20, 0.25}` is quasi-stable + (2,3)-formed; goldilocks (survived) = ∅.

**Single explanatory mechanism (Rule 11 honest closure).** The imposed (2,3) is a **non-eigenmode plant**: it is not a self-consistent standing solution of the K4+Cosserat engine, so it relaxes/wanders within ~2–10 Compton periods regardless of amplitude. The degradation is present at `A²max ≈ 0.07` (amp 0.10) just as at `A²max ≈ 6` (Arm-C) — so the **single cause is "the planted (2,3) is not a stable structure," NOT over-saturation and NOT a flat-Cosserat-ω integrator leak.** This is precisely the `substrate-native-check` CP8 anti-pattern outcome: plant-the-finished-composite → degrades even in the gentle regime.

**What this resolves about the V0 fork.** Phase-0 (B) named over-saturation as the mechanism and *saved* the conservation question ("too violent to test"). Phase 0.5 tests it in the gentle regime and finds the (2,3) **still** degrades → the over-saturation explanation is **incomplete**: over-saturation is real at amp ≥ 0.30 (and was severe at the amp-0.40 Arm-C config), but it is **not the cause** of the winding degradation, which reproduces sub-saturation. The V0 "12/12→5/12 fail" is therefore **genuine degradation of the imposed all-C (2,3) ansatz**, not a measurement artifact.

**What this does NOT establish (honest scope — flag-don't-fix).**
1. **NOT "winding is non-conserved."** This is a property of the imposed PLANT, not of a precursor-grown electron. CP8: to test conservation, seed the generative precursor and let the (2,3) FORM, then test persistence — do not plant the finished knot.
2. **All-C unbalanced initial condition.** The ansatz plants only `V_inc` (C-state); `Φ_link=0` at the seed — *not* a balanced-LC standing-mode IC (like releasing a pendulum from max displacement, zero velocity). The first ~2 T are visibly LC-equilibration. A **balanced-LC (2,3) seed** (`V_inc` + `Φ_link` in quadrature via `initialize_phi_link_2_3_ansatz`, which exists at `tlm_…_eigenmode.py:127` but is unused by Arm-C) is an **untested variant** that might survive better — a candidate next test, surfaced for orchestrator/Grant adjudication.

**Phase-1 (geometric integrator) warrant: still NO.** Phase-0 (B) already saved the build; Phase 0.5 reinforces it — the degradation is amplitude-independent disruption of a non-eigenmode plant in BOTH sectors, not an off-group Cosserat-ω leak a geometric integrator would fix.

### Redirect (indicated, NOT scaffolded — lane discipline + Rule 16)

1. **Balanced-LC (2,3) seed** — plant `V_inc` + `Φ_link` in quadrature (a standing-mode IC), re-test survival sources-OFF. Distinguishes "the (2,3) winding is unstable" from "the all-C IC sloshes apart."
2. **Precursor-grown (2,3)** (the CP8-correct test) — seed the generative precursor, let the dynamics build the (2,3), THEN test persistence. The substrate-native way to ask the conservation question.
3. **Sources-free near-wall self-amplification** (the `Φ_link` runaway at seed `A² ≳ 0.95`) is a separate, newly-surfaced engine behavior worth its own characterization.

## §0.5.6 Discipline walk (which skills fired)

- **`substrate-native-check`** — CP1: NO solver written; snapshot cadence on the engine's own velocity-Verlet step. CP5: the engine applies `ω_local(r)=ω_global·√(1−A²(r))` natively; `A²max(t)` reported as the saturation driver; no uniform-global-σ eigsolve (a forward time-domain read). CP6: **reactance PAIR tracked** — C-state `A²max` (`V_inc`) AND L-state `Φ²max` (`Φ_link`) every logged step; the pair is what surfaced the sources-free `Φ_link` runaway and confirmed the sub-wall settling is genuine (not C-settles-while-L-grows). CP7: extractor PML-excludes every ring point + density-crest shell location (reused unchanged). CP8: **the imposed (2,3) is a PLANT** — sources-off free evolution is closer to seed-the-precursor but is still a plant; the (II) is explicitly scoped as a plant-not-a-grown-composite finding, and the precursor-grown test is named as the CP8-correct redirect.
- **`phase-space-coordinate-check`** — load-bearing winding read in phase-space `Θ=2φ+3ψ` (the extractor's internal U(1) phase, matching the corpus (2,3) on the Clifford torus); `A²max`/`Φ²max` are scalars (saturation magnitude, frame-free); real-space `(R,r)` is diagnostic-only (where to walk). MATCH.
- **`ave-canonical-source`** — `ALPHA` from `ave.core.constants`; `PHI`/`DT`/`COMPTON`/`A2_OP14` reused from the extractor. `A2_WALL=1.0` is the saturation kernel's own rupture normalization (tagged). `N`/`PML`/amplitudes/cadence are honestly-tagged engineering choices.
- **`ave-driver-script-honesty`** — forward READ of a KNOWN-imposed signal; NO `minimize`/`curve_fit`, NO parameter tuned toward (2,3). The seed `A²max∝amp²` is a forward prediction (verified). The I/II/III verdict is a transparent printed rule on seed→evolved deltas. The fragile single-frame "survived" metric was caught and strengthened to *sustained* (last-two-snapshots) before the production run (flag-don't-fix on my own driver).
- **`consistency-vs-emergence`** — CONSERVATION-under-free-evolution of an IMPOSED control + a regime characterization: **consistency** class, NOT emergence; no α / hosting / CODATA claim.
- **`ave-evidence-framing-discipline`** — (II) is stated honestly as the data shows; survival was NOT pre-claimed; the scope limits (plant-not-grown, all-C IC) are flagged, not buried.

## §0.5.7 Artifacts

- Phase 0.5 driver: `src/scripts/vol_1_foundations/r10_2_3_winding_quasistable_survival.py`
- Results JSON: `src/scripts/vol_1_foundations/r10_2_3_winding_quasistable_survival_results.json`
- Figure: `src/scripts/vol_1_foundations/r10_2_3_winding_quasistable_survival.png` (A²max(t) on-vs-off · Goldilocks-band map · survival w1/w2)
- Reused (unmodified) extractor: `src/scripts/vol_1_foundations/r10_2_3_winding_extractor_coordinate.py`
