# Round 13 entry: Layer 3 K4 V_inc/V_ref test — corpus-precondition status finding + Rule 16 ask-Grant

**Date:** 2026-05-01
**Predecessor:** [doc 103 §6 Round 13 candidates](103_substrate_perspective_electron.md) + [doc 102 §7.4 Round 13 forward direction](102_round_12_unknot_cosserat_working.md)
**Status:** entry doc — Round 13 pre-registration BLOCKED on Rule 16 question to Grant after A43 v2 grep-finding on prior canonical seeder usage

---

## §1 — Round 13 candidate framing per prior docs

Doc 102 §7.4 + doc 103 §6 + auditor pass-3 named Round 13 path:

> **K4 V_inc/V_ref Layer 3 test** using the existing `initialize_quadrature_2_3_eigenmode` seeder per A47 v7 + doc 28 §5.1.

The framing rested on A47 v7's claim (catalogued in COLLABORATION_NOTES.md, added 2026-04-30):

> *"the corpus-canonical eigenmode IC has been sitting in the codebase unused across the entire L3 arc; every test used `initialize_2_3_voltage_ansatz` (V_inc-only, V_ref=0 implicitly) instead."*

Auditor pass-3 endorsed the path: *"Round 13 path naming A47 v7's `initialize_quadrature_2_3_eigenmode` as the K4-side Layer 3 test is correct... This is independent forward progress."*

## §2 — A43 v2 grep finding: A47 v7's "unused" framing is outdated

Pre-Round-13 corpus-precondition grep (this turn) — Rule 16 + A45 + A43 v2 discipline:

```
$ grep -rn "initialize_quadrature_2_3_eigenmode\b" --include="*.py" .
```

Returns (filtered to non-definition usages):

- [`src/scripts/vol_1_foundations/r10_path_alpha_v9_bond_pair_quadrature.py`](../../src/scripts/vol_1_foundations/r10_path_alpha_v9_bond_pair_quadrature.py) — E-094 bond-pair-scale rerun, IC at line 231
- [`src/scripts/vol_1_foundations/coupled_s11_eigenmode.py`](../../src/scripts/vol_1_foundations/coupled_s11_eigenmode.py) — coupled K4-Cosserat S11 eigenmode driver, four invocations at lines 259, 584, 874, 998
- [`src/scripts/vol_1_foundations/r10_v8_o1f_quadrature_eigenmode.py`](../../src/scripts/vol_1_foundations/r10_v8_o1f_quadrature_eigenmode.py) — O.1f chair-ring quadrature eigenmode test, IC at line 97

**The seeder is in use across three drivers, not "sitting unused."** A47 v7 catalog entry was correct that the seeder existed — but the "unused" framing was outdated by 2026-04-30 work.

## §3 — Prior empirical state of `initialize_quadrature_2_3_eigenmode` tests

### §3.1 — Bond-pair scale (R=2, ℓ_node-pair) per `r10_path_alpha_v9_bond_pair_quadrature.py`

Driver docstring lines 21-29: pre-registered dual-criterion (R_phase/r_phase=φ² ± 5% AND chirality consensus ≥ 75%); Mode I/II/III adjudication per doc 28 §5.1 + doc 79 v5.1 §6.

**Result per recent commit `f120ad0` (2026-04-30): Mode III at bond-pair scale.** Closes A-016 caveat: substrate cannot host corpus electron at any tested object class up to bond-pair scale.

### §3.2 — Chair-ring scale (R≈8, R_anchor at chair-ring perimeter) per O.1f + v9 work

- **O.1f** (`r10_v8_o1f_quadrature_eigenmode.py`): launched 2026-04-30; status per `VACUUM_ENGINE_MANUAL.md:3195+3974` is "in flight" / "agent-reported uncommitted at this manual edit." No committed result document found via grep.
- **v9 chair-ring discrete-eigenmode IC** (`r10_path_alpha_v9_bond_pair_quadrature.py`-adjacent work, doc 91): used different IC (discrete eigenmode from chair-ring spectrum, not quadrature seeder), but at chair-ring scale. **Result: Mode III, 1/4 PASS strict per doc 91 §3.2.**

### §3.3 — Multi-cell torus / bond-cluster scale per path α v1-v4(b)

Used `initialize_2_3_voltage_ansatz` (V_inc-only) seeder, NOT quadrature. Per A-016 caveat: "Mode III at bond-cluster scale, but V_inc-only IC — A47 v7 quadrature requirement not met." E-094 (§3.1 above) closed this caveat by re-running at bond-pair scale with quadrature → still Mode III.

### §3.4 — Structural closure per doc 92 §6 (Round 11 (vi) closure)

**Per doc 92 §6**: the corpus electron at K4-substrate-at-ℓ_node sampling has been EMPIRICALLY ELIMINATED at all tested scales. The (1,1) Beltrami at corpus geometry has wavelength λ ≈ 0.16·ℓ_node — sub-Nyquist for K4-substrate at ℓ_node spacing. Discrete chair-ring + 1-step K4 spectrum max k = 0.52 in 1/ℓ_node units, **12× below** continuum (1,1) prediction k = 6.36.

**Closure: K4-substrate-at-ℓ_node cannot resolve the corpus electron's tube structure regardless of seeder choice.** Structural, not refinable via different seeder or finer pre-reg.

## §4 — Re-scoping Round 13: what's actually new

Given §3 prior empirical state, the original Round 13 framing as "first canonical Layer 3 test" cannot stand — the canonical seeder has been tested at bond-pair, chair-ring, and bond-cluster scales, all Mode III, and the structural closure in doc 92 §6 says K4-at-ℓ_node cannot host the corpus electron at any of those scales.

What's POTENTIALLY new for Round 13 (candidates, not pre-registered):

### §4.1 — Lattice-resolved Layer 3 phase-space test (independent of corpus-electron scale)

Run `initialize_quadrature_2_3_eigenmode` at a scale where the K4 lattice DOES resolve the eigenmode (e.g., R = 8, r = 4 lattice cells — well above ℓ_node but well below corpus-electron sub-ℓ_node). Pre-register against the (V_inc, V_ref) (2,3)-winding eigenmode persistence criterion.

**This tests Layer 3's eigenmode existence on the K4 substrate at a scale where the test is well-posed**, separate from whether the corpus electron at sub-ℓ_node can be hosted. Honest framing: this is a Layer-3-EIGENMODE-EXISTENCE test, not a CORPUS-ELECTRON-EXISTENCE test.

If Mode I → K4 substrate sustains the (2,3) phase-space eigenmode at lattice-resolved scale; canonical electron is sub-ℓ_node-only-blocking, not framework-blocking.

If Mode III → K4 substrate doesn't sustain the (2,3) phase-space eigenmode at ANY scale; deeper framework question (per A44 missing-axiom-vs-engine-bug diagnostic + Rule 9 v2 right-kind-of-question pivot).

### §4.2 — Coupled K4-Cosserat at lattice-resolved scale (Round 14 pre-work)

Already exists via `coupled_s11_eigenmode.py`. Hits the 4M× energy runaway from session 2026-04-22. Round 14 candidate, not Round 13.

### §4.3 — Layer 2 SU(2) bundle deeper diagnostic on the Round 12 unknot

Per doc 102 §7.4 candidate (3): rerun Round 12's unknot validation but add C7 deeper diagnostic — extract n_hat AT loop centerline (not at sampling circle), track spinor phase progression around loop, verify 4π closure. Stays in Cosserat sector.

### §4.4 — C3 Lorentzian-fit closure on the Round 12 unknot

Per doc 102 §7.4 candidate (4): replace HWHM-based `extract_shell_radii` with Lorentzian-fit-based extraction (per doc 100 §23 driver). Closes C3 binary criterion to <1% deviation. Methodology improvement, not new physics.

### §4.5 — Reframe Layer 3 entirely (Rule 9 v2 right-kind-of-question)

Per doc 92 §6 + doc 100 §25 bracket-Golden-Torus + auditor pass-4 ("α derivation finding still open"): is Layer 3 phase-space (V_inc, V_ref) (2,3) winding STILL the right canonical test, or has the L3 arc accumulated enough negative results that the question pattern itself needs pivoting?

Rule 9 v2 trigger: 5+ pre-registered tests at varied configurations all returning Mode III suggests the question pattern is wrong, not the answer.

## §5 — Rule 16 question for Grant

Per Rule 16 (ask-Grant-fundamental-physics-questions BEFORE designing tests/closures), this entry doc surfaces the corpus-precondition status finding rather than pre-registering tests directly. The Rule 16 question:

**Q (Round 13 entry):** Given that:

1. The canonical (V_inc, V_ref) quadrature seeder IS used (3+ drivers since 2026-04-30, NOT unused)
2. Tests at bond-pair + chair-ring + bond-cluster scales all return Mode III
3. Doc 92 §6 closes K4-at-ℓ_node cannot host the corpus electron at any tested scale (structural, Nyquist limit)
4. The corpus electron is sub-ℓ_node per Reading A canonical (R = ℓ_node/(2π) ≈ 0.16 cells)

**What does Round 13 actually test that hasn't been done?** Four candidate framings (§4.1-§4.4 above):

- **(α)** Lattice-resolved Layer 3 phase-space test (NOT corpus-electron-scale test) — tests Layer 3 eigenmode existence at K4-resolved scale, separate question from corpus electron
- **(β)** Skip to Round 14 coupled-engine work (4M× runaway resolution) — engineering blocker, not Layer 3 test
- **(γ)** Layer 2 SU(2) bundle deeper diagnostic — Cosserat-sector improvement on Round 12, not K4 sector
- **(δ)** C3 Lorentzian-fit closure — methodology improvement on Round 12, not new physics
- **(ε)** Rule 9 v2 reframe — accumulated Mode III pattern suggests question pattern is wrong; pivot

**Implementer-lane lean:** (α) lattice-resolved Layer 3 phase-space test is the cleanest forward physics work — tests a well-posed substrate question (does K4 host the (2,3) eigenmode at any resolved scale?) without re-running the closed-by-doc-92-§6 corpus-electron-at-K4 test. Mode I would unblock the structural closure interpretation; Mode III would be the cumulative signal Rule 9 v2 (ε) is watching for.

But the question is whether (α) is informative enough to be worth the test, or whether (ε) Rule 9 v2 says we should pivot to a different framing entirely. That's plumber-physics for Grant.

**Auditor-lane consideration:** the auditor pass-3 endorsed Round 13 forward progress without grep-verifying the seeder's prior usage. Per A43 v2 anyone-must-grep, the auditor + implementer were both on outdated A47 v7. The grep-finding here closes that gap — but it changes the Round 13 scope question from "first canonical test" to "what's still informative given prior closure."

## §6 — Discipline notes (pre-registration framework, pending §5 adjudication)

Same disciplines as Round 12 (doc 101 §5):

- A39 v2 dual-criterion required if test is run
- A40 multi-N required (32³ + 48³ minimum)
- A42 corpus-canonical topology measure (c=3 via Op10 OR equivalent K4 V-sector winding measure)
- A43 v2 anyone-must-grep — closing the seeder-usage grep gap with this doc
- A45 corpus-canonical-test-precondition + A47 v7 — re-evaluated per §3 prior empirical state
- A46 phase-space-vs-real-space coordinate discipline
- A47 v11d axiom-chain-required-in-docstring for any new test code
- Rule 11 clean-falsification — no post-hoc reframes
- Rule 12 retraction-preserves-body
- Rule 14 substrate-derives-the-answer
- **Rule 16 ask-Grant-first** — applied via §5 question above
- Rule 9 v2 — explicitly considered as candidate (ε)

## §7 — What this doc does NOT do

- Does NOT pre-register Round 13 tests (§5 question gates pre-reg)
- Does NOT modify CosseratField3D, K4Lattice3D, or any production code
- Does NOT close any of the doc 102 §7.4 ⏸ items
- Does NOT touch manuscript prose (Rule 15 lane discipline)
- Does NOT proceed with §4.1 (α) framing without Grant's adjudication on whether it's informative given doc 92 §6 closure

This is Round 13 entry doc surfacing corpus-precondition status finding via A43 v2 grep + Rule 16 question framework. Round 13 pre-registration follows Grant's adjudication.

— Doc 104 created 2026-05-01 per Grant directive 2026-04-30 ("start it now, plan out and research any opens for it"). The "open" surfaced by research is: prior canonical seeder usage closes the original Round 13 framing; what's actually informative now is the Rule 16 question. Per the L3 arc discipline pattern (Round 12 entry → visualization gap → Grant adjudication → pre-reg), Round 13 follows the same pattern.

---

## §8 — Round 13 (α) executed: Mode III decisive at lattice-resolved scale with canonical quadrature IC

### §8.1 — Test configuration

Per Grant directive 2026-05-01 ("proceed"): executed candidate (α) — the existing `r10_v8_o1f_quadrature_eigenmode.py` driver, which was launched 2026-04-30 + uncommitted per VEM. Driver pre-registers PRIMARY (1) frequency criterion + PRIMARY (2) phase-space (V_inc, V_ref) PCA aspect criterion + SECONDARY energy retention.

**Configuration:**
- N = 48 (lattice-resolved 48³ grid)
- PML thickness = 4
- IC: `initialize_quadrature_2_3_eigenmode(R=8, r=4, amplitude=0.05, chirality=1.0)`
- Cosserat ON but unsourced (Cosserat ω = 0; pure K4 V_inc/V_ref test)
- Run: 50 Compton periods (444 steps at DT = 1/√2)
- 5 sample cells at varied (φ, ψ) on the chair-ring
- IC verification: V_inc RMS = 9.67e-3, V_ref RMS = 9.59e-3 (~equal per quadrature ✓), A²_max(t=0) = 0.032

### §8.2 — PRIMARY (1) frequency criterion: Mode III

Median peak ω across 5 sample cells: **0.0000**. Verdict per pre-reg: **DC-dominated quasi-static residual — same failure mode as V_inc-only IC.**

| Cell | Peak ω | Peak amp | DC amp |
|---|---|---|---|
| (35,23,23) | 0.0000 | 4.66e-2 | **4.66e-2** |
| (23,35,23) | 0.0000 | 7.17e-2 | **7.17e-2** |
| (15,23,27) | 4.4301 | 3.78e-2 | 1.75e-2 |
| (23,19,23) | 0.0000 | 2.91e-2 | **2.91e-2** |
| (31,31,26) | 0.0000 | 0.0 | 0.0 |

4 of 5 cells DC-dominated; 1 cell at ω = 4.43 (lattice Nyquist artifact per A-010 corollary in COLLABORATION_NOTES — sub-lattice mode aliased). NONE of the predicted physical modes (ω_C, 1.5·ω_C, 2.96·ω_C) detected.

### §8.3 — PRIMARY (2) phase-space topology criterion: Mode III

| Cell | PCA aspect (V_inc, V_ref) | Target φ² | Match |
|---|---|---|---|
| (35,23,23) | 29.65 | 2.618 | ✗ FAIL |
| (23,35,23) | 10.97 | 2.618 | ✗ FAIL |
| (15,23,27) | 61.79 | 2.618 | ✗ FAIL |
| (23,19,23) | 18.44 | 2.618 | ✗ FAIL |
| (31,31,26) | inf | 2.618 | ✗ FAIL |

Median PCA aspect = 24.0; target φ² = 2.618 (Vol 1 Ch 8 specific value, brackets per doc 100 §25). All cells FAIL the topology criterion. The phase-space (V_inc, V_ref) trajectory is highly elongated (R/r ≫ 10), NOT a closed (2,3) winding pattern.

Note: even ignoring the φ² specific value (bracket-Golden-Torus), an aspect ratio of 10-60 indicates the trajectory is essentially linear, not a 2D closed orbit. The (2,3) winding pattern is structurally absent regardless of specific R/r ratio.

### §8.4 — SECONDARY: energy retention

50P retention = 0.485 (slight improvement over V_inc-only IC's 0.395, ~half retention vs ~40%). Better than V_inc-only but still substantial energy loss; closed-system shouldn't lose energy.

### §8.5 — Round 13 (α) verdict: Mode III decisive

**Both primary criteria FAIL:**
- Frequency: DC-dominated, no ω_C / 1.5·ω_C / 2.96·ω_C / any oscillating mode
- Topology: phase-space (V_inc, V_ref) trajectory is essentially linear, not (2,3) winding

The canonical (V_inc, V_ref) quadrature IC at lattice-resolved chair-ring scale (R=8, r=4) produces the SAME DC-dominated quasi-static residual as the V_inc-only IC. **The eigenmode framing per doc 28 §5.1 doesn't manifest empirically at K4-resolved scale.**

This reinforces doc 92 §6 structural closure: K4-substrate-at-ℓ_node-spacing cannot host the corpus electron's Beltrami eigenmode at any tested scale, with any tested IC.

### §8.6 — Rule 9 v2 trigger

Per Rule 9 v2 (right-kind-of-question; "5+ pre-registered tests at varied configurations all returning Mode III in the same direction → suspect question pattern, not answer"):

Cumulative Mode III tests in K4 V_inc/V_ref space:
1. Round 11 (vi) v6 (chair-ring, uniform-amplitude spatial-phase IC, in-ring) — Mode III
2. Round 11 (vi) v7 (chair-ring, refined IC) — Mode III
3. Round 11 (vi) v8 (chair-ring, further refined IC) — Mode III
4. Round 11 (vi) v9 (chair-ring + 1-step K4, discrete eigenmode IC) — Mode III, 1/4 PASS strict
5. Round 11 (vi) v10 (finer K4 sampling) — structurally eliminated per doc 92 §6
6. Path α v1-v4(b) (bond-cluster, V_inc-only IC) — Mode III
7. E-094 path α v9 (bond-pair, quadrature IC) — Mode III per commit f120ad0
8. **Round 13 (α) O.1f (chair-ring lattice-resolved, canonical quadrature IC) — Mode III** (this turn)

8 tests. All Mode III. Varied configurations: chair-ring + bond-pair + bond-cluster scales × V_inc-only + uniform-amplitude + discrete-eigenmode + canonical-quadrature ICs.

**Per Rule 9 v2: this IS the cumulative pattern signal.** The question pattern "specify a corpus configuration → seed (V_inc, V_ref) ansatz → test if (2,3) phase-space winding eigenmode persists → Mode III → propose another configuration" is an unbounded search through configuration × IC space. The cumulative Mode III pattern strongly suggests the canonical electron is NOT testable at K4-substrate-at-ℓ_node sampling regardless of configuration choice.

This is consistent with:
- Doc 92 §6 Nyquist structural closure (corpus electron is sub-ℓ_node)
- Reading A canonical R = ℓ_node/(2π) ≈ 0.16 cells (sub-grid)
- Auditor pass-3: K4-side Layer 3 test "is independent forward progress" but framed before the cumulative pattern was evident

**Rule 9 v2 reframe pattern (per COLLABORATION_NOTES.md):** *"switch from 'verify-against-corpus-at-config-X' to 'characterize-the-engine's-natural-output-as-itself.'"* For the K4 V_inc/V_ref sector at lattice-resolved scale: the engine's natural output IS the DC-dominated quasi-static residual. Characterizing THAT as itself (not as a failed eigenmode test) might be the right next move.

### §8.7 — Doc 100 §25 ⏸ items resolution under Round 13 (α)

| ⏸ Item | Pre-Round-13 status | Post-Round-13 status |
|---|---|---|
| Cosserat ⚠ scaffold-preservation | Reframed via three-layer; Round 12 validated layer-1+2 | Unchanged (Round 13 is K4-only, doesn't touch Cosserat) |
| Theorem 3.1 Method 2 (multipole sum) | ⏸ pending Layer 3 audit | **Mode III at canonical Layer 3 test** — the multipole sum's Vol 1 Ch 8 (R, r) values do NOT correspond to an empirically-realized (V_inc, V_ref) eigenmode; layer-3-canonical-test-fails is empirical evidence Method 2's geometric values aren't load-bearing for the K4 sector |
| §22 Cosserat-AVE-HOPF cross-anchor | ⏸ pending Layer 3 audit | Unchanged at the cross-anchor framing level; Round 13 closes the K4-only Layer 3 test as Mode III |

### §8.8 — Net empirical state of fundamental electron model post-Round 13

| Anchor | Status |
|---|---|
| Parent's `39e1232` electron-is-unknot canonical | ✅ |
| Parent's α = p_c/8π packing-fraction canonical | ✅ |
| Atomic IE 14/14 manuscript precision | ✅ |
| TLM xfail-clean per Rule 11 | ✅ |
| Theorem 3.1 Method 1 (LC-tank reactance) | ✅ |
| AVE-HOPF λ(p,q) framework | ✅ |
| Cosserat unknot Layer 1+2 (Round 12) | ✅ at lattice-resolved scale |
| g-2 corpus-canonical per Vol 2 Ch 6 §6.2 | 🟡 |
| **K4 V_inc/V_ref Layer 3 canonical eigenmode test** | **🔴 Mode III decisive at lattice-resolved scale + canonical IC** |
| Theorem 3.1 Method 2 (multipole sum) | ⏸ — bracketed; informed by §8.7 layer-3-canonical-test-fails |
| §22 Cosserat-AVE-HOPF cross-anchor | ⏸ pending |
| Cosserat ⚠ scaffold-preservation Lorentzian | ⏸ methodology only |
| Sub-ℓ_node corpus-electron-as-physical-object | ⏸ structurally blocked at K4-at-ℓ_node sampling per doc 92 §6 |

**Net: 7 ✅ + 1 🟡 + 1 🔴 + 4 ⏸.** Up one 🔴 from doc 102 §7.3 baseline (the Layer 3 K4 canonical test is now empirically falsified at lattice-resolved scale, a real finding rather than a bracketed item).

Per Rule 11 clean-falsification: this is the framework working at full strength. The Layer 3 K4 canonical test was pre-registered (driver docstring + doc 28 §5.1); the prediction was an oscillating eigenmode at ω_C with phase-space (2,3) winding; the empirical result is DC-dominated linear-trajectory; clean falsification.

### §8.9 — Forward direction post-Round 13

The structural picture stabilizes:
- Real-space Cosserat unknot Layer 1+2 — lattice-resolved test ✅ (Round 12)
- Phase-space K4 V_inc/V_ref Layer 3 — lattice-resolved test 🔴 Mode III (Round 13 (α))
- Coupling K4-Cosserat via Op14 — structurally available; engineering-blocked on 4M× runaway

**Round 14 candidates** (per doc 102 §7.4 + §8.6 Rule 9 v2 reframe):

- **(α') Characterize engine's natural output:** the DC-dominated quasi-static residual that K4 V_inc/V_ref produces is real engine behavior. Characterize-as-itself (frequency content, spatial structure, coupling response) per Rule 10 corollary. Honest physics, not a failed test.

- **(β) CoupledK4Cosserat 4M× runaway resolution:** still open. Per A44, likely engine bug (T_kinetic not saturating); engineering work.

- **(γ) Sub-ℓ_node infrastructure:** spectral solver / mesh-refined K4-TLM for sub-ℓ_node corpus-electron testing. Real engineering work; would resolve the structural-closure caveat per doc 92 §6.

- **(δ) Framework reflection:** per Rule 9 v2 + auditor's α-derivation finding + cumulative Mode III pattern in K4 V_inc/V_ref space — is the framework's claim "corpus electron at K4-substrate" still defensible? If not, what reframe? This is manuscript-author lane (Grant), not implementer.

**Implementer-lean for Round 14:** (α') characterize-engine's-natural-output. The DC residual is real; understanding it is forward physics. Doesn't require new infrastructure; doesn't pre-suppose any framing the cumulative Mode III pattern hasn't already falsified.

(β) is engineering blocker work; (γ) is hours of new infrastructure; (δ) is Grant's lane.

— §8 closure of Round 13 (α) execution per Grant directive 2026-05-01 ("proceed"). Mode III decisive at lattice-resolved scale + canonical quadrature IC. Rule 9 v2 trigger fired (8 cumulative Mode III tests). Forward-direction recommendation: characterize-engine's-natural-output per Rule 10 corollary; defer pre-registration of Round 14 to Grant's reflection.

---

## §8.10 — Self-audit corrections per Grant directive 2026-05-01 (Rule 12 + A47 v11b)

Grant prompted self-audit on the §8 framing: "do you agree?" — Rule 9 v2 strategic-pivot signal asking implementer to step back. Honest answer: **partial agreement; substantial reservations on §8 framing.** Four corrections owed per Rule 12 preserve-body discipline. §8.1-§8.9 preserved verbatim above; corrections appended here.

### §8.10.1 — 🔴 promotion in §8.8 was premature

§8.8 promoted "K4 V_inc/V_ref Layer 3 canonical eigenmode test" to 🔴 status post-Round 13 (α). This was over-reach. Round 13 (α) tested at chair-ring scale (R=8 cells) which IS a corpus-electron-related geometry. Per doc 92 §6, K4-substrate-at-ℓ_node cannot host the corpus electron at any tested corpus-related scale (Nyquist limit, sub-ℓ_node corpus electron). **Round 13 (α) is one more confirmation of doc 92 §6's already-known structural closure, not a new 🔴 finding.**

The honest contribution of Round 13 (α) narrows to: confirms that swapping V_inc-only IC for canonical-quadrature IC at the SAME chair-ring scale produces the SAME DC-dominated residual. Closes the narrow question "does the V_inc-only seeder differentiate from quadrature?" — answer: no, both produce identical failure mode at corpus-electron-scale geometry. That's narrower than a Layer 3 falsification.

**Corrected entry:** Layer 3 K4 canonical eigenmode test status remains ⏸ with structural-context per doc 92 §6 closure. NOT 🔴.

### §8.10.2 — Rule 9 v2 trigger framing in §8.6 was over-stated

§8.6 listed 8 cumulative Mode III tests and claimed Rule 9 v2 trigger fires per "varied configurations all returning Mode III in the same direction → suspect question pattern." But the 8 tests are all at corpus-electron-related scales (chair-ring, bond-pair, bond-cluster — all targeting corpus-electron geometry on K4-at-ℓ_node). They're 8 manifestations of doc 92 §6's structural Nyquist closure, not 8 independent failures spanning "varied configurations" in the Rule 9 v2 sense.

The cumulative pattern signal IS doc 92 §6's closure showing up across tests, NOT a new question-pattern signal that requires Rule 9 v2 reframe. The reframe was already documented in doc 92 §6: K4-at-ℓ_node-spacing cannot host sub-ℓ_node corpus electron.

**Layer 3 phase-space (V_inc, V_ref) (2,3)-winding eigenmode at scales INDEPENDENT of corpus-electron geometry has NOT been tested.** So claiming "Layer 3 falsified" overstates what was empirically tested.

**Corrected reading:** Round 13 (α) at chair-ring is a confirmation event for doc 92 §6, not a new Rule 9 v2 trigger. Layer 3 testing at scales independent of corpus-electron geometry is genuinely-not-yet-tested and remains a candidate forward direction.

### §8.10.3 — A47 v11b substitution-not-retraction near-miss caught

I substituted the dramatic reading ("🔴 Layer 3 falsified" + "Rule 9 v2 reframe required") for the simpler accurate reading ("Round 13 (α) confirms doc 92 §6 with canonical IC; closes the V_inc-vs-quadrature differentiation question; doesn't extend the closure beyond what's already known").

This is the same A47 v11b pattern caught in §16 / §22 / §23 / §24 last round — labeling-as-closure (or, here, labeling-as-falsification) rather than reporting-as-data. The Rule 12 preserve-body fix: keep §8.6 + §8.8 verbatim, append this §8.10 with the corrected reading.

### §8.10.4 — Rule 14 substrate-derives skipped

§8 reported the DC-dominated residual + labeled it Mode III but did NOT walk substrate-physics for WHY the residual occurs. Per Rule 14 (substrate-derives-the-answer), this is the disciplined first move.

Substrate-physics candidate explanations (Rule 14 walk, this turn):

- **Saturation engagement is marginal.** IC has A²_max(t=0) = 0.032. V_yield engine-natural ≈ √α ≈ 0.0854 → A²_yield ≈ 0.0073, so the IC IS above yield. But the saturation cusp (per A47 v2) is at A²_op14 = √(2α) ≈ 0.121, well above the IC's 0.032. **Saturation is engaged but not at the cusp** — Op14 reflection coefficient |Γ|² is small but nonzero.

- **Cosserat unsourced → no Op14 K4-Cosserat coupling target.** Per doc 103 §4.6: the canonical electron requires BOTH Cosserat ω AND K4 V_inc/V_ref structure simultaneously coupled via Op14. With Cosserat ω = 0, Op14 cross-block is one-sided (K4 → Cosserat radiation but no return); V_inc/V_ref energy disperses without a coupling-target to refresh.

- **Chair-ring R=8 cells is ~50× corpus-electron scale.** If a K4 cavity mode exists, this scale isn't where it sits. The IC is exciting bulk waves on the K4 substrate at a wavelength much larger than the corpus-electron's tube radius.

- **PML absorption.** N=48 lattice with PML thickness=4 leaves active region 40³. Energy retention 50P = 0.485 means ~half the energy was absorbed by the PML — consistent with bulk waves dispersing outward to the absorbing boundary instead of being trapped.

**Honest substrate-physics interpretation:** the engine evolved the IC into bulk waves that disperse outward, leaving a low-amplitude DC residual at the IC's spatial pattern. This is straightforward K4-TLM behavior at ℓ_node sampling for an unbound IC at sub-saturation amplitude with no Cosserat coupling. **NOT a falsification of any specific corpus-canonical claim** — it's the engine doing exactly what the substrate allows under these conditions.

The corpus electron's claim is a SELF-MAINTAINING TRAP (per doc 103 §4.2 + §3.2): saturation IS where the field IS, the field IS where saturation traps it, topologically protected. Round 13 (α) at sub-cusp A² + no Cosserat coupling cannot test the trap mechanism — neither the saturation-cusp threshold nor the K4-Cosserat coupling channel is engaged.

### §8.10.5 — Revised honest empirical state

Per §8.10.1 + §8.10.2 corrections, the §8.8 table:

| Anchor | Status |
|---|---|
| Parent's `39e1232` electron-is-unknot canonical | ✅ |
| Parent's α = p_c/8π packing-fraction canonical | ✅ |
| Atomic IE 14/14 manuscript precision | ✅ |
| TLM xfail-clean per Rule 11 | ✅ |
| Theorem 3.1 Method 1 (LC-tank reactance) | ✅ |
| AVE-HOPF λ(p,q) framework | ✅ |
| Cosserat unknot Layer 1+2 (Round 12) | ✅ |
| g-2 corpus-canonical per Vol 2 Ch 6 §6.2 | 🟡 |
| K4 V_inc/V_ref Layer 3 canonical eigenmode test | ⏸ structural-context per doc 92 §6 closure (corpus-electron-scale only; Layer 3 at scales independent of corpus-electron not yet tested) |
| Theorem 3.1 Method 2 (multipole sum) | ⏸ pending |
| §22 Cosserat-AVE-HOPF cross-anchor | ⏸ pending |
| Cosserat ⚠ scaffold-preservation Lorentzian | ⏸ methodology only |
| Sub-ℓ_node corpus-electron-as-physical-object | ⏸ structurally blocked at K4-at-ℓ_node sampling per doc 92 §6 |

**Revised net: 7 ✅ + 1 🟡 + 5 ⏸.** NOT 7 ✅ + 1 🟡 + 1 🔴 + 4 ⏸. The 🔴 promotion was premature; the cleaner reading is ⏸ with structural-context.

### §8.10.6 — Corrected forward direction for Round 14

The §8.9 forward direction (α'/β/γ/δ) framings were sound in spirit but follow from the corrected (not-falsified) Round 13 reading:

- **(α')** Characterize-engine's-natural-output: still right per Rule 9 v2 catalog text *"characterize THAT object as itself"*. The DC residual at chair-ring with canonical quadrature IC IS an attractor (stable across 50P). Characterize: spatial distribution, port structure, FFT content beyond DC, sensitivity to IC amplitude / chirality / scale. **This was the disciplined Round 13 follow-up that should have been done in §8 itself, not labeled as Round 14 candidate.**

- **(β)** CoupledK4Cosserat 4M× runaway: per §8.10.4 substrate walk — the canonical electron requires K4-Cosserat coupling. Round 13 (α) without Cosserat seed is a one-sided test. Round 14 (β) would address the coupling-channel question that Round 13's substrate walk surfaces.

- **(γ)** Sub-ℓ_node infrastructure: still relevant for testing corpus-electron-at-canonical-scale.

- **(δ)** Framework reflection: per the corrected reading, no new Rule 9 v2 trigger fires. Doc 92 §6 closure stands; the cumulative Mode III pattern is doc 92 §6 manifesting in subsequent tests, not new evidence of question-pattern wrongness. Framework reflection on α-derivation finding (auditor's prior critique) remains its own separate audit item.

**Implementer-lean revised:** (α') as immediate forward — characterize the DC residual as itself per Rule 14 + Rule 9 v2 catalog text. Use the data already collected by Round 13 (α) — spatial structure of the residual, FFT content per cell beyond DC, sensitivity scan if needed. Then (β) coupling-channel work as Round 15+, (γ) sub-ℓ_node infrastructure as longer-term.

— §8.10 self-audit corrections per Rule 12 preserve-body + A47 v11b substitution-not-retraction discipline + Rule 14 substrate-derives + Rule 9 v2 catalog-text-precision. §8.1-§8.9 body preserved; corrected reading appended.
