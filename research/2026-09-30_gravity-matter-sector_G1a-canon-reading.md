# G1a: what canon as written assigns a bound massive body (blind to data)

**Status:** audit record, stage G1a of the R61 gravity audit lane. It is not canon and it edits no leaf, open item or audited branch.
**Criteria:** `_orchestration/2026-09-30_wave1-gravity-audit-brief.md@d55401e6e60db50b3a24e24fe57777c4fcac964c, section G1`.
**Canon read at:** `origin/main` = `cbc668e7219ec8a8b13407da7a7a33ed622ad95b`. `origin/main` did not move during the stage.
**Run:** 2026-11-01. One run of `.claude/workflows/ave-adversarial-pr-review.js` (`wf_e56bbac0-6b1`) with the brief's G1a lens and context, passed verbatim. One lens (`canon-reader`, read-only) and five verifiers. `refuted_count` = 1.

---

## §1. Bins and verify verdicts

**Held-bin rule (brief, G1).** A bin is held if its own verify verdict is CONFIRMED or DOWNGRADED; `corrected_severity` is ignored. A bin is not held if it is REFUTED or missing. The launching session assigns K and S from held bins only.

| Question | Reader's bin | Verify verdict | Status |
|---|---|---|---|
| Q0, regime(s) canon assigns Mercury's orbit | **CONFLICTING** | CONFIRMED | **held** |
| Q1, what a bound slow massive body's motion sees | **AMBIGUOUS** | CONFIRMED | **held** |
| Q4, neutrinos on the scalar channel | CANON-SILENT | **REFUTED** (the verifier names AMBIGUOUS, which is not a listed Q4 bin) | **not held** |

The workflow drops REFUTED findings from its return. The Q4 finding and its verdict are recovered here from the run's journal; the reader's Q4 answer is also in its `clean_report` ("Q0 = CONFLICTING. Q1 = AMBIGUOUS. Q4 = CANON-SILENT.").

**What the frozen rules do with these bins.**
- Q0 CONFLICTING: K5 fires, a STUCK-POINT for Grant, subject to K4's precedence. PANEL-AUDIT still states the conditional K bin under each regime reading.
- Q1 AMBIGUOUS: every quoted arm goes under test (§8).
- Q4 not held: **S5 is recorded now.** The K verdict is unaffected. The `sn1987a` lens scores both the scalar and light channels as candidates.

---

## §2. Q0 = CONFLICTING: evidence

All quotes re-read at `cbc668e7` by the launching session as well as by the lens and verifier.

| Reading | Regime | Control parameter | Source (verbatim) |
|---|---|---|---|
| A | not I; the row names no ruler | none stated | `manuscript/ave-kb/vol3/cosmology/ch14-orbital-mechanics/orbital-regime-table.md:16`: "| Mercury precession | II (Yield) | $\Delta\phi$ = 43''/century | Exact match with GR |". Print twin `manuscript/vol_3_macroscopic/chapters/14_macroscopic_orbital_mechanics.tex:23`. |
| B | I | A_gm | `manuscript/ave-kb/vol3/cosmology/ch06-solar-system/orbital-lc-friction-paradox.md:14`: "This establishes that the entire solar system operates infinitely deep inside **Regime I ($A_{gm} \ll 0.121$)**." Also `manuscript/ave-kb/common/temporal-saturation-regime-classifier.md:326`: "Solar system at $A_{gm} \sim 10^{-34}$ → Regime I". |
| C | I | ε11 / ΔS | `manuscript/ave-kb/vol1/operators-and-regimes/ch7-regime-map/domain-catalog.md:47`: "| Control parameter | $r = \varepsilon_{11}$ |"; `:50`: "- Solar surface: $\varepsilon_{11} = 1.486 \times 10^{-5}$ --- Regime I". The catalog lists no planetary orbit. The extension is at `manuscript/ave-kb/vol3/applied-physics/ch07-stellar-interiors/stellar-regime-classification.md:22`: "All terrestrial and main-sequence stellar physics operates deep in Regime I ($\Delta S < \alpha$), validating the use of unmodified Einstein gravity for all solar system applications." |
| D | past onset | g_N/a_0, on total local field | `domain-catalog.md:128`: "| Control parameter | $r = g_N / a_0$ |"; `:132` names stars only. Applied at the solar system by `manuscript/ave-kb/vol3/cosmology/ch06-solar-system/oort-cloud-saturation-boundary.md:32`: "so under total-local-field keying the Sun is already past the Axiom-4 onset and no transition exists anywhere inside the solar system". Canon does not print "Regime IV" for planets. |
| E (verifier addition) | past yield | τ/τ_yield | `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/magnetic-saturation.md:24`: "(e.g., the spatial envelope surrounding a planetary body), the local magnetic field exceeds this structural saturation limit ($\tau > \tau_{yield}$)."; `:28`: "yielding stable, conservative planetary orbits." No regime numeral is printed, and nothing links it to the ch14 row. |

**Verifier's refutation attempts, all failed.**
- SINGLE-NOT-I, on "the Mercury row beats general statements": the Regime I statements are universal over a set containing Mercury ("the entire solar system", "All solar system bodies").
- SINGLE-I, on "ch14 is a stale outlier": no canon text retracts the row; it stands in print and KB.
- "Channels dissolve the conflict": the row names no ruler, and the perihelion leaf has no regime statement. The per-channel rules that exist are scoped elsewhere: `einstein-field-equation.md:103` ("TWO PER-CHANNEL RULERS", its own table) and `common/wall-taxonomy.md:153` (walls).

**Corrections the verifier made to the finding's wording (bin unchanged).** Reading D's ratio is the total local field at the solar system, not "the solar field". The sentence "the only reconciliation language" fails on "only", as above. The regime labels themselves carry no dedicated registered claim, so the finding's "regime-column claim" overstates; `clm-qyn8t0` (0.55, input only) grades the perihelion content.

**Defect class:** EVIDENCE-VOID. The ch14 label has no stated ruler, so the demonstration of Mercury's regime is absent, not disproved.

---

## §3. Q1 = AMBIGUOUS: evidence

| Reading | Object | Source (verbatim) | Verifier's standing |
|---|---|---|---|
| 1 | `n_scalar` | `manuscript/vol_3_macroscopic/chapters/03_macroscopic_relativity.tex:54`: "Because a massive topological wave-packet acts as a 3D isotropic defect, it couples to the spatial volume via the $1/7$ Lagrangian isotropic projection (derived in Chapter 1). The effective scalar refractive index perceived by mass is $n_{scalar}(r)=1+\epsilon_{11}(r)/7=1+GM/c^{2}r$." KB twin `ponderomotive-equivalence.md:14`. Applied to the orbit at `anomalous-perihelion-advance.md:10`. | live |
| 2 | `(n_t, n_s)` metric | `14_macroscopic_orbital_mechanics.tex:71`: "The same perihelion advance is derivable directly from the canonical temporal/spatial refractive metric $(n_t, n_s)$ of Vol~3 Ch~1--Ch~2 (the PPN factor $(2-\beta+2\gamma)/3 = 1$ at $\beta = \gamma = 1$ reproduces $6\pi GM/c^2 a(1-e^2)$)". | live |
| 3 | `n_spatial` for matter waves | `manuscript/common_equations/eq_gravity_derived.tex:54`: "n_{spatial} &= 1 + \tfrac{9}{7}\,\varepsilon_{11} && (\text{controls matter-wave parallax, C11})". | weak: stated for an electron, not a bound slow body, and `double-deflection.md:33` separates "the ballistic matter soliton" from a matter wave |
| 4 | GR potential adopted, no lattice index | `14_macroscopic_orbital_mechanics.tex:71`: "General Relativity's effective-potential correction ... here \emph{adopted as a static potential}." | print half live; the KB half (`anomalous-perihelion-advance.md:8`) is overridden by the UPDATE at `:10` |
| 5 | unnamed gradient | `anomalous-perihelion-advance.md:28`: "As a planet orbits deep within the steep refractive gradient of a parent star". | not a reading: non-fixing text |

**Nearest fixing sentence, and its limit.** `double-deflection.md:20`: "**Matter (scalar coupling).** A fast-moving massive particle is an isotropic 3D volumetric wave packet". `manuscript/ave-kb/vol3/claim-quality.md:1149`: "The coupling-selection step — that a massive packet couples only to the scalar $1/7$ bulk while the photon, mechanically blind to bulk, couples only to the $2/7$ transverse sector — is asserted by **mechanical analogy**, not derived from a wave-equation projection."

**Verifier's attempt at FIXED-SCALAR, the strongest competing bin.** `tex 03:54` has no speed scope and leads directly to the Newtonian force; the perihelion leaf applies the index to the orbit; the claim card lists `clm-rd9cjm` as a dependency. It fails because the print warningbox on the exact observable names a different object, `(n_t, n_s)`, defined separately from `n_scalar`, and the box is not superseded in print. The roadmap entry also leaves the spatial part open (`claim-quality-closure-roadmap.md:205`): "spatial-metric contribution to substrate orbital mechanics (whether substrate Cosserat anisotropy reproduces GR's g_rr at PPN-1)". The stage rule then binds: "If canon supports more than one reading, the bin is AMBIGUOUS and every reading is quoted."

**Verifier's support the finding omitted.** The register does not fix the index either. `clm-qyn8t0` labels its dependency `clm-rd9cjm` as `n_scalar`, while the `clm-rd9cjm` card states the slope-2 index and calls it "the **temporal component**".

**Verifier's caution on one argument.** "Fast-moving" is one site's wording, not a demonstrated restriction: `double-deflection.md:18` and `:33` carry no speed scope. The bin rests on `tex 03:54` against `tex 14:71` with the stage rule applied, not on that word.

**Standard held.** GR names one metric for a slow body's geodesic; asking canon to name one object for the same motion is the same bar. **Defect class:** EVIDENCE-VOID. Nothing here refutes `n_scalar` as the eventual answer.

---

## §4. Q4 = CANON-SILENT, REFUTED

**The reader's case.** No manuscript line pairs "neutrino" with `n_scalar`, `n_t`, `n_s`, the 1/7 projection or a gravitational coupling. `n_scalar` is conditioned on "3D isotropic defect" (`tex 03:54`), which canon never applies to the neutrino, described instead as "a propagating open helix" (`manuscript/vol_2_subatomic/chapters/03_neutrino_sector.tex:15`) and "a pure torsional (screw) defect" (`manuscript/vol_2_subatomic/chapters/06_electroweak_and_higgs.tex:273`).

**The verifier's refutation.** The reasoning skips the class-level predicate. `manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex:179`: "A fast-moving massive particle is an isotropic 3D volumetric wave packet carrying finite rest energy. It couples to the \emph{scalar} (isotropic bulk) component of the lattice strain via the $1/7$ volumetric projection". Canon separately writes membership: `03_neutrino_sector.tex:15`, "Neutrinos are the most abundant massive particles in the universe". Both premises are written; only the conclusion is unstated. That is a canon reading, not silence.

A second reading is equally live, so the verifier does not move to CANON-ASSIGNS-SCALAR: the subject may be limited to Hopfions (`ch02:176`; `01_gravity_and_yield.tex:53`, "``Mass'' is simply localized, tightly confined electromagnetic wave energy (Hopfions)"), against `03_neutrino_sector.tex:13`, "the neutrino is a pure Cosserat-torsional excitation, not an electromagnetic one". CANON-ASSIGNS-OTHER fails because no line names an alternative index.

**Result under the frozen rule.** REFUTED means not held, whatever replacement bin is named. S5.

---

## §5. Flag findings (not bins)

**FLAG 1, DOWNGRADED.** The ch14 label "II (Yield)" uses the coarse Linear / Yield / Rupture family without naming its ladder and gives no Mercury control value. The verifier struck two sentences of the finding: "the Vol 1 r-bands do not apply at all" is contradicted by `clm-xy252u` ("the same physics expressed at different granularities"), which maps the coarse rung II onto Ch.7's II plus III, at solidity 0.63 with the mapping left open. The finding's "Vol 2 ladder" is also a Vol 1 ladder (`04_continuum_electrodynamics.tex:251-252`). The verifier added a further reading: the Vol 1 Ch.4 rungs are partly keyed by domain ("I: ... Newtonian gravity" against "II: ... GR"), so the row may be domain-keyed and not an amplitude statement. Q0's CONFLICTING does not rest on this internal II-versus-III question; it rests on the row's non-I label against the other rows.

**FLAG 2, CONFIRMED.** One observable carries conflicting status statements.
- Foreword, `manuscript/frontmatter/00_foreword.tex:111`: "the perihelion relativistic coefficient is not yet substrate-derived (named open gap)."
- KB scope-note, `anomalous-perihelion-advance.md:10`: "substrate-native derivation gap CLOSED at leading PPN-1 order via Ponderomotive Equivalence Principle pathway", "NOT borrowed from GR".
- Print, `tex 14:71`: "not an independent AVE derivation".

The verifier's narrowings: the print sentence has the static-potential coefficient as its subject and partly reconciles with the KB, so the hard conflict is foreword against KB and card. `n_s` is the 9/7 index by `divergence-test-substrate-map.md:261`, not an open either/or, so the live question is how that index yields the box's "$\beta = \gamma = 1$", and canon does not show the step.

**Adjacent drift seen by two verifiers, not acted on.** `manuscript/ave-kb/vol3/claim-quality.md:45` still reads "Light deflection couples to a **separate spatial component** $n_{spatial} = 1 + (9/7)\varepsilon_{11}$", against the correction at `temporal-spatial-lattice-decomposition.md:26`.

---

## §6. Findings on the frozen criteria (recorded, not re-posed)

1. **Q4 has no AMBIGUOUS bin, and the G1a context's general rule produces one.** The context says "If canon supports more than one reading, the bin is AMBIGUOUS", while Q4 lists three bins. The verifier followed the general rule. The frozen outcome is unaffected: REFUTED is not held, so S5.
2. **The brief's G1a context has no `{{FILL}}` value** to replace, despite the instruction. It was passed verbatim.

---

## §7. Stage integrity

- The reader and verifiers report reading `origin/main` only, with no PR branch, PR diff or `_orchestration/` file. After the run the launching session listed the files #1028 and #1029 change: none is a canon leaf, which closes the reader's stated inability to check this.
- **Coverage limit on Q4, reported by the reader.** The "massive" search was filtered to coupling keywords and "neutrino" was read as line windows. The Q4 verifier read Vol 2 Ch 3 and Ch 6 lines directly.
- **Departures from "no numbers", no observational value involved.** Neither touches a bin.
  - The reader ran one standalone symbolic expansion of the Item-5 Lagrangian and withheld the value.
  - The FLAG 2 verifier wrote out hand algebra as a "separate item": expanding the roadmap's Lagrangian gives "γ = 0 and β = 3/2", and the box's factor "evaluates to 1/6, not 1". It reached this without opening a PR. It is **quarantined**: not used here, labelled by its author as needing a re-run, and G1b re-derives it independently.

---

## §8. Fixed here for G1b, before any data stage

**Arms under test.** Q2 says AMBIGUOUS puts every quoted arm under test. The held Q1 verdict narrows the quoted readings: "at least two independent live readings remain: n_scalar (tex 03:54 plus leaf :10) and (n_t, n_s) (tex 14:71). Print additionally keeps "adopted" GR." The launching session's decision, on that verdict:

| Arm | Held reading | Note |
|---|---|---|
| `scalar` | Reading 1 | `a1 = 1` in #1029's notation |
| `ntns` | Reading 2 | Canon's defined indices. Reading 3's `n_spatial` is this pair's spatial half; its variant is computed in this lens as a sub-case, labelled characterization, because its quoted source does not reach a bound slow body. |
| `adopted-gr` | Reading 4, print half | No lattice index; γ and β are inputs |

Reading 5 is not an arm: it has no object to derive from. The light arm is **not** added as an arm of its own; Q2 adds it only under SILENT or a Q1 that is not held. Whether Reading 2 coincides with it is a question for the `ntns` lens to answer.

**SN1987A channels.** Q4 not held, so scalar and light, both as candidates.

**Regime rulers for G1b.** The held Q0 names A_gm, ε11 / ΔS, g_N/a_0 and, by verifier addition, τ/τ_yield.
