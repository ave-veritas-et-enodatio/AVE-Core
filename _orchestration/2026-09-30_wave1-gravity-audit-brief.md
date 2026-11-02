# Handoff brief — PR-triage wave 1, gravity audit lane (#1028 + #1029 panel; #1031 and #1032 single auditors)

**Date:** 2026-09-30 · **Lane:** audit. It writes audit records only. It never edits canon, open items or the audited branches, and never comments on the audited PRs. **Authority:** R61 ([`docket-entries/2026-09-30-ruling-r61-pr-triage-wave1.md`](docket-entries/2026-09-30-ruling-r61-pr-triage-wave1.md)). **Author:** orchestrator. **Grant launches and picks model and effort.** Suggestion: the strongest model at high effort for G1; G2 and G3 can run cheaper.

**For Grant's launch message:** include "run the ave-adversarial-pr-review workflow for G1a and G1b" (the saved workflow at `.claude/workflows/ave-adversarial-pr-review.js`). Budget: one workflow run per stage. If a stage fails or times out twice, that is a STUCK-POINT; do not hand-roll a substitute panel.

**Expected truth-yield:** high for G1. It decides whether a printed canon claim ("Exact match with GR" for Mercury) survives canon's own written assignment, confronted with data that already exist. Medium for G2 (a code-vs-ruling mismatch) and G3 (a routing item bearing on a public README score).

**Mission and regime framing**
- **R51 §6** (`docket-entries/2026-08-12-ruling-r51-a1-two-objects-carve.md`), verbatim: *"peer-with-GR/QED/SM inside a regime is the expected result, not a disappointment; the program's targets are the regime boundaries (yield, saturation, cutoff, quench conditions)"*.
- **DISPATCH-GLOSS:** the decision line Grant approved called Mercury "an in-regime must-pass test". Canon's own ch14 row labels Mercury "II (Yield)", so the regime is itself a frozen question (Q0). Canon may assign Mercury more than one regime through different control parameters. If its readings disagree, the verdict is K5 (a STUCK-POINT for Grant), with the conditional verdict under each reading recorded. A wrong-regime reading is never explained away.
- **MODE / REGIME / PHASE-STATE:** every derivation declares all three. MODE is matter clock vs EM carrier. REGIME comes from the computed ε11 at the orbit. PHASE-STATE is the cold / sub-yield branch vs a saturated one. One audit holds one declaration across routes.

**Every number and line number in this brief is DISPATCH-GLOSS.** Re-derive or re-read it. Where the repo disagrees, the repo wins, and you report the difference.

---

## Step −1 — preconditions

1. `git fetch origin`. Both `git cat-file -e origin/main:_orchestration/2026-09-30_wave1-gravity-audit-brief.md` and the same check on the R61 docket file must succeed. Record the **freeze SHA** of these criteria: `git log -1 --format=%H origin/main -- _orchestration/2026-09-30_wave1-gravity-audit-brief.md`. Every record cites the criteria as `<path>@<freeze SHA>, section G1`.
2. The heads must match this table. A moved head is a STUCK-POINT.

| PR | branch | head at 2026-09-30 | files under audit (besides the generated BOARD.md) |
|---|---|---|---|
| #1028 | `research/2026-08-27-ppn-tensor-derivation` | `2f19d551` | `research/2026-08-27_ppn-tensor-derivation_result.md`; open items `eps11-four-objects`, `ppn-matter-sector-walkback` |
| #1029 | `research/2026-08-27-two-knob-gravity-repair` | `c0e5fd75` | `research/2026-08-27_two-knob-gravity-repair_result.md`; `research/drivers/two_knob_gravity_repro.py` + results JSON; six open items |
| #1031 | `research/2026-08-27-x44-unblock` | `8b53eaa2` | the FROZEN prereg, result, two drivers + JSON, `src/ave/gravity/backreaction.py`, `src/tests/engine_acceptance/_nordtvedt.py`, open item `x44-unblock` |
| #1032 | `machian-boundary-first-principles-audit` | `84d6fb3c` | open item `2026-08-28-machian-form-half-adjudication.md` **only** (see G3) |

3. Do not disturb `50cb25c7` or `849f6a97`: open PR #1030 pins those two SHAs.

**Where results go.** Create branch `research/2026-09-30-gravity-wave1-audit` off `origin/main` in a throwaway worktree. It carries the records named below. Do not commit the generated `BOARD.md`.

---

## G1 — Tier-2 panel on #1028 + #1029, in two stages

**Why two stages.** The saved workflow runs its lenses concurrently and gives every lens the same context. Canon must be read *before* anyone sees a data comparison. So the canon reading runs alone and is committed and pushed (freeze-by-push); only then does the data stage start.

**How bins are verified and counted**
- The workflow verifies *findings*. Every lens therefore emits **each bin it owns as a finding** titled `BIN <name> = <bin>`, severity **MINOR**, with verbatim evidence. It also **lists every bin answer in its `clean_report`**, because the workflow drops REFUTED findings from its return and keeps only `refuted_count`.
- A bin is **held** if its verify verdict (`verdict.verdict`) is CONFIRMED or DOWNGRADED. Ignore `corrected_severity`: a bin is not a defect. A bin is **not held** if it is REFUTED or missing. Note that the workflow's `confirmed` array includes DOWNGRADED findings; read each finding's own verdict.
- **Verifier instruction** (in both contexts below): for a finding titled `BIN` or `CENSUS`, CONFIRMED means the bin is correct, and REFUTED means a different bin is correct (name it). Never DOWNGRADE a bin for severity.
- The launching session assigns K and S from held bins only, and writes the rule into the record.

### Frozen criteria (frozen at the freeze SHA; do not re-bin after reading data)

**Q0 — Regime(s) canon assigns to Mercury's orbit.** Read every canon statement that places Solar-System orbits on the regime ladder:
- the Mercury row of `manuscript/ave-kb/vol3/cosmology/ch14-orbital-mechanics/orbital-regime-table.md`;
- the gravitational row of `manuscript/ave-kb/vol1/operators-and-regimes/ch7-regime-map/domain-catalog.md` (control parameter ε11);
- that catalog's galactic-dynamics row (control parameter g_N/a_0), if canon applies it to orbits;
- any other regime statement the canon-reader finds.

Bins:
- **SINGLE-I**;
- **SINGLE-NOT-I** (name the regime);
- **CONFLICTING** (list each reading, with its control parameter and source).

In G1b, the rederive lens computes each named control parameter at Mercury's orbit from canon's own formulas, and reports the regime each one gives.

**Q1 — Canon's assignment.** For a bound, slowly moving massive body in a static weak field, what does canon as written say sets its coupling to the lattice strain, i.e. which index or metric its motion sees? Answer from canon text only, with verbatim quotes and paths.
- **FIXED-SCALAR** — the scalar-index route; `a1 = 1` in #1029's notation.
- **FIXED-LIGHT** — light's characteristic; `a1 = 2`.
- **FIXED-OTHER**.
- **AMBIGUOUS** — canon supports more than one route; quote each.
- **SILENT**.

**Q2 — Reproduction, per arm.** Re-derive γ_matter, β and the perihelion factor F independently, by at least two routes (metric PPN; metric-free WKB/ray), for each arm under test.
- **Arms under test:**
  - FIXED → the fixed arm;
  - AMBIGUOUS → every quoted arm;
  - SILENT → the scalar and light arms, both labelled *non-canon candidates*.
- **Re-runs:** #1029's `two_knob_gravity_repro.py` and #1028's §9 reproduction snippet, in a throwaway worktree.
- **Divergence step:** name the step where canon's own scalar-route derivation (Foundation Item 5 in `anomalous-perihelion-advance.md`) and the PRs' F = 1/6 part ways.
- Bins per arm:
  - **REPRODUCED**.
  - **CORRECTED** — the derivation completes, and both routes agree with each other but not with the PRs. This includes the case where canon's own Item-5 route is right and the PRs erred. The corrected values go to Q3.
  - **FAILED** — the derivation cannot be completed, or the two routes disagree with each other.

**Q3 — Data, with the carrier fixed before data.** Use primary observational values, with sources.
- **Matter sector, per arm:** Mercury perihelion (IAU GM_sun), and LLR scored on the Nordtvedt η = 4β − γ_matter − 3 computed from the arm's own matter-sector values. Never score it against a published β, which already folds in a light-sector γ.
- **Light sector, arm-independent:** Cassini γ, scored against canon's light-sector γ only. A matter-sector γ is **never** compared with Cassini.
- Bins per observable:
  - **EXCLUDED** — |predicted − observed| > 5 σ_obs. This threshold is an ENGINEERING-CHOICE, fixed before the audit's data stage. The author knows the PRs' headline values; the threshold is not load-bearing for any of them.
  - **CONSISTENT** — within 5 σ_obs.
  - **UNTESTABLE**.

**Q4 — SN1987A channel.** Does canon as written place neutrinos on the scalar channel? Read the bullet beginning `**Matter (scalar coupling).**` in `manuscript/ave-kb/vol3/gravity/ch02-general-relativity/double-deflection.md` against any neutrino-specific text in canon.
- Bins: **CANON-ASSIGNS-SCALAR** / **CANON-SILENT** / **CANON-ASSIGNS-OTHER**.

**Q5 — Site census.** Every canon surface that asserts matter-sector agreement with GR.
- **Seed list:** the audited PR's own census, not independently enumerated. It is the Group A–E sites in #1028's `_orchestration/open-items/2026-08-27-ppn-matter-sector-walkback.md` on its branch.
- Verify each seed site, then extend the list by a second search method across KB leaves, `.tex`, `claims.jsonl`, the root README and `manuscript/consistency-manifest.yaml`.
- Emit `CENSUS: <n> sites`, with the table in its evidence.

**Q6 — Repair-round integrity.** Check the 2026-09-06/07 self-repair and self-audit commits on both branches. Are their receipts true at the tip, and did they introduce defects?

**Q7 — Routed-item numerics.** Re-run the numerics behind #1029's `preferred-frame-boost-channel` and `lattice-momentum-umklapp` items, or report them as not reproducible from the tree.

**Pair verdict: exactly one K bin.** An arm's values means its REPRODUCED or CORRECTED values. Precedence: **K4 > K5 > K3 > {K0, K1, K2}**.
- **K4 — NO CONSENSUS:** any of:
  - Q1 is not held;
  - Q1 is FIXED, and Q2 or Mercury on the fixed arm is not held;
  - Q1 is AMBIGUOUS or SILENT, and Q2 or Mercury is not held on any arm under test.
  A non-held Q4 affects S only.
- **K5 — REGIME / UNBINNED:** a STUCK-POINT for Grant; never assign the nearest bin. It fires when any of these holds:
  - Q0 is SINGLE-NOT-I or CONFLICTING;
  - Q0 is not held;
  - a computed control parameter puts Mercury outside Regime I;
  - Cassini (light) is EXCLUDED;
  - the combination is not listed here.

  The PANEL-AUDIT record still states the **conditional** K bin that K0–K3 would give under each regime reading. This is characterization, not verdict, so the regime question reaches Grant with its consequences attached.
- **K3 — DERIVATION FAILED:** Q2 is FAILED (the derivation cannot be completed, or the routes disagree) on an arm that K0–K2 need. Canon is untouched; the PRs are repaired or closed.
- **K0 — CANON SURVIVES AS WRITTEN:** either case below.
  - Q1 is FIXED on an arm whose Mercury and LLR are CONSISTENT.
  - Q1 is AMBIGUOUS and every quoted arm is CONSISTENT.
- **K1 — KILL ON CANON AS WRITTEN:** Q1 is FIXED on an arm whose Mercury or LLR is EXCLUDED.
- **K2 — OVERCLAIM:** either case below. The printed agreement rests on a choice canon never makes.
  - Q1 is AMBIGUOUS and at least one quoted arm is EXCLUDED.
  - Q1 is SILENT, whatever Q3 says.

**SN1987A verdict: exactly one S bin.**
- The session assigns it from held bins: G1a's Q4, and the sn1987a lens's `BIN ARITH = HOLDS | REFUTED` (whether #1029's arithmetic reproduces) and `BIN SN-PRED[<channel>] = WITHIN | EXCEEDS` (predicted photon–neutrino differential vs the observed bound).
- Precedence: S5 > S3 > the rest.
  - **S0 — CANON PASSES:** Q4 is CANON-ASSIGNS-SCALAR and the scalar prediction is WITHIN.
  - **S1 — LIVE KILL:** Q4 is CANON-ASSIGNS-SCALAR and the scalar prediction EXCEEDS.
  - **S2 — GATED:** Q4 is CANON-SILENT.
  - **S3 — ARITHMETIC REFUTED:** ARITH = REFUTED.
  - **S4 — OTHER CHANNEL:** Q4 is CANON-ASSIGNS-OTHER; scored under that channel, pass or fail recorded.
  - **S5 — NO CONSENSUS:** any of Q4, ARITH, or the SN-PRED bin on the channel Q4 assigns is not held.

**If a G1a bin is not held:**
- **Q1 not held:** record K4. Run G1b anyway, with `rederive` lenses for both the scalar and light arms, labelled **characterization, not verdict**.
- **Q4 not held:** record S5. The K verdict is unaffected.
- **Q0 not held:** record K5 with conditional bins.

If G1b cannot run cleanly, stop with a STUCK-POINT.

**Standing constraints**
- **The a1 = 2 / (2, 1, ½) repair is CONSISTENCY-CLASS unless Q1 is FIXED-LIGHT.** It was chosen with Mercury in view, and #1029's own words are "Nothing yet FORCES it". If canon itself fixes light's characteristic, that arm is canon's assignment and is scored as canon. **The audit recommends no arm.**
- **a1 = 2 banking note.** Decision 2 says a1 = 2 "banks as a new hypothesis with its own prereg", and R61 §3 lists a proposed wave-2 slot for it (an orchestrator proposal, not a ruling). The PANEL-AUDIT record ends with a short note that:
  - proposes a **lane-owned** item for that hypothesis (KEEP-BOTH, own prereg), cross-linking #1029's `two-knob-constitutive-forcing`;
  - flags that the existing item's ROUTED-TO-GRANT status conflicts with decision line 2.
  Do not create the item.
- **Symmetric standard.** GR gets β = γ = 1 from its field equations. Hold AVE's derivation to the same bar, no stricter and no looser.
- **Both-ways seduction.** A clean kill is a narrative too. Test the wrong-regime, wrong-carrier and wrong-coordinate readings of the negative with the same force as a positive.
- **Duplicates to collapse** (record them, don't fix them):
  - #1028 `eps11-four-objects` consequence 3 and #1029 `bias-to-index-photoelastic-map` result 3 are one finding.
  - #1028's L/C-grading question and #1029's a1 question are one fork.
  - #1029's "two knobs" (c_eff vs Ω) are not the #1020 signed "two knobs" (kernel A vs Op19 n).

### G1a — canon reading, blind to data

Run the workflow with `pr: 1028`, the **G1a context**, and this lens list:

```json
[{"key": "canon-reader", "run": false, "prompt": "CANON-ONLY LENS. Ignore the instruction to review the PR diff. Do NOT open any file changed by PR #1028 or #1029, anything under _orchestration/, or any PR branch, and do not look up any observational value. Read end to end, on origin/main: manuscript/ave-kb/vol3/cosmology/ch14-orbital-mechanics/anomalous-perihelion-advance.md (every Foundation Item scope-note); manuscript/vol_3_macroscopic/chapters/14_macroscopic_orbital_mechanics.tex (the warningbox titled 'Provenance of the ``3'' coefficient'); manuscript/ave-kb/vol3/cosmology/ch14-orbital-mechanics/orbital-regime-table.md; manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/ponderomotive-equivalence.md; manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/gordon-optical-metric.md; manuscript/ave-kb/vol3/gravity/ch02-general-relativity/double-deflection.md; manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md; manuscript/ave-kb/common/operators.md (Op19); manuscript/ave-kb/vol1/operators-and-regimes/ch7-regime-map/domain-catalog.md; manuscript/ave-kb/claim-quality-closure-roadmap.md (the perihelion row); claim clm-qyn8t0 in manuscript/ave-kb/.index/claims.jsonl and its card in manuscript/ave-kb/vol3/claim-quality.md. Then search manuscript/ for 'perihelion', 'n_{scalar}', 'n_t', 'massive' and 'neutrino' and read each hit's paragraph. For Q0, read the domain-catalog gravitational row (control parameter epsilon_11) and its galactic-dynamics row (control parameter g_N/a_0), and say whether canon applies each to planetary orbits. Emit exactly three bin findings at severity MINOR: 'BIN Q0 = <SINGLE-I|SINGLE-NOT-I|CONFLICTING>', 'BIN Q1 = <FIXED-SCALAR|FIXED-LIGHT|FIXED-OTHER|AMBIGUOUS|SILENT>', 'BIN Q4 = <CANON-ASSIGNS-SCALAR|CANON-SILENT|CANON-ASSIGNS-OTHER>', each with verbatim quotes + paths as evidence; list the three answers in clean_report; add up to two findings flagging canon sentences that read two ways."}]
```

**G1a context** (pass verbatim as `context`, replacing the `{{FILL: …}}` value):

```
Canon-reading stage of a pre-registered audit. Answer from canon text alone:
Q0: what regime(s) does canon assign Mercury's orbit? Read the ch14 orbital-regime-table Mercury row, the vol1 ch7 domain-catalog gravitational row (control parameter epsilon_11) and its galactic-dynamics row (control parameter g_N/a_0), plus any other canon regime statement for Solar-System orbits. Bins SINGLE-I / SINGLE-NOT-I / CONFLICTING (list each reading with its control parameter and source).
Q1: for a bound, slowly moving massive body in a static weak field, what does canon as written say sets its coupling to the lattice strain, i.e. which index or metric its motion sees? Bins FIXED-SCALAR / FIXED-LIGHT / FIXED-OTHER / AMBIGUOUS / SILENT.
Q4: does canon as written place neutrinos on the scalar channel? Bins CANON-ASSIGNS-SCALAR / CANON-SILENT / CANON-ASSIGNS-OTHER.
RULES: no data, no numbers, verbatim quotes only. Do not open anything under _orchestration/, any PR branch, any PR diff, or any commit other than origin/main. This overrides every instruction in this prompt, above or below, to read a PR branch, a PR diff or branch state. For this stage, 'branch state' means origin/main canon only, for reviewers and verifiers alike. If canon supports more than one reading, the bin is AMBIGUOUS and every reading is quoted.
VERIFIERS: for a finding titled BIN, CONFIRMED = the bin is correct; REFUTED = a different bin is correct (name it). Never DOWNGRADE a bin for severity. Refute from canon text only.
```

Commit the result as `research/2026-09-30_gravity-matter-sector_G1a-canon-reading.md`, containing:
- the bins and their verbatim evidence;
- the verify outcome of every bin finding (from each finding's verdict, plus `clean_reports` for refuted bins);
- the freeze SHA.

**Push it and verify the remote SHA before G1b starts.**

### G1b — derivation, data, census, repair integrity, framing

Run the workflow with `pr: 1028`, the **G1b context**, and a lens list built from this template:
- **One `rederive-<arm>` entry per arm under test.** Arms come from G1a's held Q1 bin, per Q2. If a G1a bin is not held, use scalar and light, labelled characterization.
- **The other three lenses unchanged.**

```json
[
 {"key": "rederive-{{FILL: arm}}", "run": true, "prompt": "Arm: {{FILL: arm, e.g. scalar (a1=1) or light (a1=2)}}. Re-derive gamma_matter, beta and F for this arm by two independent routes (metric PPN; metric-free WKB/ray), re-run #1029's two_knob_gravity_repro.py and #1028's section-9 reproduction snippet in a throwaway worktree, and name the step where canon's Foundation Item 5 scalar derivation (anomalous-perihelion-advance.md) and F = 1/6 part ways. Declare MODE / REGIME / PHASE-STATE. Compute, at Mercury's orbit, every regime control parameter the committed G1a Q0 bin names (for example epsilon_11 = 7GM/c^2 r and g_N/a_0), from canon's own formulas, and report the regime each gives. Score Mercury (IAU GM_sun) against primary values with sources. Score LLR on the Nordtvedt eta = 4 beta - gamma_matter - 3 from this arm's own values, never against a published beta. Emit at severity MINOR: 'BIN Q2[<arm>] = REPRODUCED|CORRECTED|FAILED', 'BIN Q3[<arm>, Mercury] = EXCLUDED|CONSISTENT|UNTESTABLE', 'BIN Q3[<arm>, LLR-eta] = ...', 'BIN REGIME[Mercury, <control parameter>] = <regime> (computed)'. List all bin answers in clean_report."},
 {"key": "sn1987a", "run": true, "prompt": "Score #1029's SN1987A photon-neutrino differential. Take the channel from the committed G1a Q4 bin quoted in context; if Q4 is CANON-SILENT or not held, score both scalar and light channels as candidates. Also score Cassini gamma against canon's LIGHT-sector gamma only (arm-independent; never a matter-sector gamma). Emit at severity MINOR: 'BIN ARITH = HOLDS|REFUTED', 'BIN SN-PRED[<channel>] = WITHIN|EXCEEDS', 'BIN Q3[light, Cassini] = EXCLUDED|CONSISTENT|UNTESTABLE'. List them in clean_report."},
 {"key": "census-and-repairs", "run": true, "prompt": "Q5: verify every site in the seed list (#1028's ppn-matter-sector-walkback item, Groups A-E, on its branch; this is the audited PR's own census) and extend it by a second search method across KB leaves, .tex, claims.jsonl, the root README and manuscript/consistency-manifest.yaml; emit 'CENSUS: <n> sites' at MINOR with the file:line + class table as evidence. Q6: are the receipts asserted by the 2026-09-06/07 self-repair and self-audit commits on both branches true at the tip, and did those commits introduce defects? Q7: re-run the numerics behind #1029's preferred-frame-boost-channel and lattice-momentum-umklapp items, or report them as not reproducible from the tree. One finding each for Q6 and Q7."},
 {"key": "framing", "run": false, "prompt": "Check verdict language against the bins: Q0's consequences, the symmetric standard (GR gets beta = gamma = 1 from its field equations), both-ways seduction (wrong-regime, wrong-carrier, wrong-coordinate readings of the negative), grade labels in PR titles and open items, and the duplicate collapse listed in the frozen criteria. Flag any wording the bins do not support."}
]
```

**G1b context** (pass verbatim as `context`, replacing each `{{FILL: …}}`; everything in `<…>` stays literal):

```
ALSO FIRST: git fetch origin research/2026-08-27-two-knob-gravity-repair and read PR #1029 via git diff origin/main...origin/research/2026-08-27-two-knob-gravity-repair and git show origin/research/2026-08-27-two-knob-gravity-repair:<path>. This is a JOINT audit of #1028 and #1029.
CLAIM UNDER REVIEW (the PRs' claim, not a finding): under canon's written massive-body assignment the matter-sector PPN parameters are gamma_matter = 0, beta = 3/2, perihelion factor F = 1/6, so Mercury comes out near 7.16"/cy against ~42.98 observed, while canon prints "Exact match with GR" (ch14 orbital-regime-table Mercury row and related sites). #1029 adds an SN1987A photon-neutrino differential falsifier and a (2,1,1/2) repair. All numbers here are to be re-derived, not trusted.
CANON READING (committed before this stage; challenge it only as a flagged finding): {{FILL: G1a record path @ pushed SHA}}; held bins: {{FILL: Q0, Q1, Q4 as committed, with verify verdicts}}.
FROZEN CRITERIA: _orchestration/2026-09-30_wave1-gravity-audit-brief.md @ {{FILL: freeze SHA}}, section G1. Carriers are fixed: Mercury and LLR (scored on eta = 4 beta - gamma_matter - 3 from the arm's own values) score the matter sector per arm; Cassini gamma scores the light sector only and is arm-independent; a matter-sector gamma is never compared with Cassini. EXCLUDED means > 5 sigma_obs (engineering choice). Emit every bin you own as a finding titled 'BIN <name> = <bin>' at severity MINOR, and list all your bin answers in clean_report. Do not invent bins.
VERIFIERS: for a finding titled BIN or CENSUS, CONFIRMED = the bin is correct; REFUTED = a different bin is correct (name it). Never DOWNGRADE a bin for severity.
STANDING: the a1=2 repair is CONSISTENCY-CLASS unless the canon reading is FIXED-LIGHT; recommend no arm. Symmetric standard vs GR's field-equation derivation of beta = gamma = 1. A clean kill is a narrative too: test wrong-regime, wrong-carrier and wrong-coordinate readings.
```

Write `research/2026-09-30_gravity-matter-sector_PANEL-AUDIT.md`. It contains:
- the K and S assignments, with the held-bin rule and the precedence applied;
- every bin with its verify verdict, including REFUTED bins recovered from `clean_reports`, plus `refuted_count`;
- the Q5 table;
- the Q6 and Q7 results;
- the framing findings;
- the a1 = 2 banking note.

---

## G2 — single auditor on #1031

**Scope.** The PR as it stands at `8b53eaa2`. The X44 physics itself stays parked: the stated default is to park until the T_ij register exists, and T_ij has no owner.

- **F-3.** On main, `komar_weight` in `src/ave/gravity/backreaction.py` is two lines: `S = saturation_kernel(A, exponent=0.5, S_min=S_min)`, then `return np.sqrt(S)`.
  - Confirm this equals (1 − A²)^¼ wherever S ≥ S_min (read `saturation_kernel`).
  - Compare it with the docket heading `### Ruling 1 — F6 Komar-clock register: √S (slope-1) IS the clock — CONFIRMED` in `_orchestration/2026-07-10_rulings-docket.md`. The ruling is recorded as a paraphrase.
  - Bins: **F3-MISMATCH-REAL** / **F3-NO-MISMATCH**.
- **Frozen-prereg compliance.** Check the run's BIN Z (ARTIFACT) verdict against `research/2026-08-27_x44-unblock_prereg_FROZEN.md` as frozen at `44e0315a`.
  - First verify that the frozen prefix's blob hash is unchanged at the tip.
  - Is detector Z1 a gate that can fire, or an identity of its own target?
  - Bins: **BIN-Z-UPHELD** / **BIN-Z-OVERTURNED**.
- **Engine safety.** Check two things:
  - bit-identity of the komar default (KEEP-BOTH);
  - the legacy `Delta_clock` key under `source_mode="ponderomotive"`, versus `Delta_clock_src`.

  From the tip, in a throwaway worktree, with no `-m` filter, run `python -m pytest src/tests/test_grqed_stage3_backreaction.py src/tests/engine_acceptance/test_nordtvedt_eta.py src/tests/test_categorization_guards.py --timeout=1800 --timeout-method=thread`, then `make test`.
  - Bins: **ENGINE-EDIT-SAFE** / **ENGINE-EDIT-UNSAFE**.
- **Scope of "unreachable at ANY amplitude."** `research/drivers/x44_unblock_regime_map.py` fixes `SIGMA = 1.8`. #1031's FROZEN prereg lists the FAM-A family as `σ ∈ {1.4, 1.8, 2.2, 2.6}` (search `FAM-A`).
  - Copy the driver into your worktree and change only `SIGMA` to 2.6, then 1.4 if runtime allows.
  - Re-run it, and record the diff and the result.
- **Out:** repairs. Making the engine edits line-neutral is wave-2 implementer work.
- **Grant question.** Write F-3 as at most two lines, picture-first, for a later sitting, paired with #1033's clock-as-S(A) reading (archived at `archive/research/2026-08-28-qpoint-constitutive` once the mechanical lane has run). Route it nowhere.

**Record:** `research/2026-09-30_x44-unblock_AUDIT.md`.

## G3 — single auditor on #1032's re-posed open item only

Audit `_orchestration/open-items/2026-08-28-machian-form-half-adjudication.md` at `84d6fb3c`. Do **not** audit the RECORD body, which is a frozen record preserved with its BLOCK banner. The item has had no second pass since the commit that wrote it.

- **Self-contradiction.** The item says it "needs no physics call" and also that it "decides DECISION 1's physics half". Reconcile the two.
- **Missing caveat.** The companion `research/2026-08-28_machian-boundary-first-principles-audit_BLIND-AUDIT.md` carries a §6 caveat (the lossless uniform-line model assumption). The item calls Γ = −1 "strictly LOAD-BEARING" without it. Should it be restored?
- **x = x identity.** Reproduce by algebra that the G ↔ H∞ "agreement" is an identity, from `src/ave/core/constants.py` (`H_INFINITY`, `R_HUBBLE`, `G`).
- **H∞ double-booking.** Reproduce the arithmetic by which the root `README.md` row `| 23 | H∞ (Hubble asymptote)` ("0.7% vs TRGB") becomes about +24.4% under the fixed-asymptote reading. Cross-check P23 in `manuscript/consistency-manifest.yaml`.
- **DECISION 2 vs the docket.** Compare DECISION 2 with the row `| **G-Ġ** *(stub booking row)*` in `_orchestration/2026-07-10_rulings-docket.md`. Is it a second home for the same fork?
- **Documentary correction.** Take the arm of the sentence beginning `**The decision:** does the taxonomy layer get corrected to match`, which concerns `ilk-gravmb` (see `manuscript/ave-kb/common/interlock-register.md`). Is it already covered by the 2026-06-14 G-ruling? If so it is orchestrator polish, not a Grant call.
- **Bins:** **ITEM-SOUND** / **ITEM-NEEDS-REPAIR** (list the repairs) / **ITEM-WRONG**.

**Record:** `research/2026-09-30_machian-form-half-item_AUDIT.md`.

---

## Finish

1. **Open the audit PR.** Use a body file so backticks survive, then verify the remote SHA:

   ```
   gh pr create --base main --title '[DO-NOT-MERGE][REVIEW: pending-orchestrator] audit: gravity wave 1 — #1028/#1029 panel, #1031, #1032 item (R61)' --body-file <file>
   ```

2. **Do not comment on #1028, #1029, #1031 or #1032.** This repo is public. Verdicts are posted there only after the orchestrator's review of these records.
3. **Report.** Your final message is the report; Grant relays it. Post the same report as one comment on your own audit PR, through `--body-file`. It contains:
   - for each of G1, G2 and G3: the bins and verdict, the top findings with file:line, where the verdict departs from the PR's own claims, at most two proposed Grant lines (picture-first), and every STUCK-POINT;
   - the audit PR number and head SHA.

## Out of scope

- Repairs to any audited PR; any gravity walk-back or canon edit.
- Choosing an a1 arm.
- Creating or editing open items.
- #1030, which lands in wave 2 after this audit.
- The X44 / F6 / T_ij physics.
- The mechanical lane's work.

## Binding disciplines

- **Skill plan:**
  - `ave-audit` (a grounded starting state before each auditor);
  - `verify-before-cite`;
  - `consistency-vs-emergence` (classify the repair and every agreement claim);
  - `ave-discrimination-check` (SM counterfactual, both polarities);
  - `ave-regime-phase-state-check`;
  - `phase-space-coordinate-check`, wherever a coordinate choice carries a verdict;
  - `ave-worktree-paths` on the first call of every worktree;
  - `ave-assertion-gate` before any claim leaves the records as fact.
- **Self-isolation.** Never check out a branch in the main checkout. Run code only in throwaway worktrees, and remove them when done.
- **Frozen criteria stay frozen.** If a criterion is ill-posed, record that as a finding. Do not silently re-pose it.
- **Pushes.** Push from a named branch only, and verify the remote SHA after every push.
- **STOP-AND-ASK.** The triggers:
  - a fork the frozen criteria don't resolve (K5 is one);
  - a corpus contradiction;
  - a question about what something physically is;
  - the same step failing twice.

  At a trigger, end your turn with a STUCK-POINT report:
  1. the blocker, exact, file:line;
  2. what was tried (≤2 attempts);
  3. the ONE physical question whose answer unblocks, phrased plumber-physical;
  4. candidate readings, one line each.

  A clean STUCK-POINT report is a successful turn. The other sub-audits continue.
- **Pure-AVE-corpus rule** on every tracked byte and PR comment.
