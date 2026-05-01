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
