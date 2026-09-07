<!-- Landed on docs/2026-09-06-manuscript-kb-sync. Ten volume lanes, each with a
     refute-by-default verifier, re-validating the 2026-08-02 board's 154 findings
     against main @ 6b8b49a0. Adjudicates no physics; proposes no repair. -->

**Orchestrator spot-checks, run directly at `6b8b49a0` before relaying** (each
changes what gets dispatched, so none was taken on the lanes' receipts):
the ringdown wave **did** fire (7 `docs(ringdown)` commits on vol3 ch15);
`backmatter/07:145` reads *"RESOLVED 2026-08-05 (R11 … has now fired)"* and
`:212-214` reads *"Seam resolved … withdrawn with no replacement"*, so §6's
"seam still open" is stale; `bh_untapped_predictions.png` has **0** commits
since the board base; and vol3 `ch15:252` carries the one `13\%` form in the
file on a non-comment `\noindent\textbf{Limits}` line, against
`ave-merger-ringdown-eigenvalue.md:115` which strikes that diagnosis as
**RETRACTED 2026-07-20**. All four confirmed.

# BOARD RE-VALIDATION AGAINST `main` @ `6b8b49a0`
### 2026-08-02 manuscript-reconciliation board, §5 — 154 findings, ten lanes each verified refute-by-default

> **[SCOPE NOTE 2026-09-07 — the board cites in this document are pinned to `6b8b49a0`, and the same
> push that landed this file also rewrote the board.]** Nine bare `:NNN` cites here address the
> reconciliation board rather than a `.tex` file: `:45`, `:60`, `:124`, `:532`, `:635`, `:710`, `:761`,
> `:785`, `:835`. All nine were checked at `6b8b49a0` — the base this re-validation names and was run
> against — and all nine hold the content claimed for them there. None of them holds it at the branch
> tip; the board went from 877 lines at `6b8b49a0` to 1,222 across this push. They are left as
> measured rather than re-pinned, because re-pinning a dated measurement onto a later tree makes the
> measurement unreproducible. **Re-derive board line numbers before acting on any of them.** One item here is
> already discharged and should not be chased: the vol0 §5 header, reported below at board `:124` as an
> H2 that a `^### vol` enumeration would silently skip, is an H3 at the tip.

**Headline: the epic worked. 108 of 154 are discharged. 38 are still in print. 0 regressed. And board §6 is stale in two places that would have mis-routed the next lane — the ringdown gate FIRED on 2026-08-05, and all four OWED corrections were applied on 2026-08-03 to a list that still says they're owed.**

---

## 1. THE LEDGER

| Volume | Findings | DISCHARGED | STILL-LIVE | REGRESSED | VACATED | SUPERSEDED | GATED |
|---|---:|---:|---:|---:|---:|---:|---:|
| vol0 | 12 | 7 | 4 | 0 | 0 | 1 | 0 |
| vol1 | 18 | 12 | 6 | 0 | 0 | 0 | 0 |
| vol2 | 13 | 9 | 3 | 0 | 0 | 1 | 0 |
| vol3 | 21 | 16 | 3 ★ | 0 | 0 | 2 | 0 |
| vol4 | 11 | 10 | 1 | 0 | 0 | 0 | 0 |
| vol5 | 13 | 5 | 8 | 0 | 0 | 0 | 0 |
| vol6 | 19 | 12 | 7 | 0 | 0 | 0 | 0 |
| vol9 | 23 | 18 | 2 | 0 | 1 | 1 | 1 |
| backmatter | 17 | 15 | 2 | 0 | 0 | 0 | 0 |
| papers | 7 | 4 | 2 | 0 | 0 | 1 | 0 |
| **TOTAL** | **154** | **108** | **38** | **0** | **1** | **6** | **1** |

★ vol3's third STILL-LIVE is a **split**: finding #6 (ch15:337) had its caption discharged and its raster left plotting retracted numbers. Booked live, not discharged — see §2 and §9.

**Plainly: 108 discharged (70%). 46 still need something — 38 that are wrong in print right now, 6 whose prescribed fix is now the wrong fix, 1 whose argument is dead, 1 correctly held.**

**The counts sum to 154 exactly.** I verified the arithmetic myself rather than trusting the lanes: the board carries **158 `####` blocks**, of which **4 are `[REFUTED — dropped]`** (vol3 ch15:23, ch15:27; vol6 A_heavy:20; papers main.tex:128), leaving **154 live findings**. Per-volume headers sum to 154 (12+18+13+21+11+13+19+23+17+7).

**One discrepancy worth fixing in the board file itself.** The vol0 block header at board `:124` is `## vol0 — 12 findings` — an **H2**, while every other volume header is H3. Any enumeration keyed on `^### vol` silently drops all 12 vol0 findings. That is exactly what happened to the backmatter verifier, which reported "142 live / 146 blocks, neither is 154" and could not close the gap. It is a formatting defect in the board, not a missing-findings problem.

---

## 2. ★ THE LIVE SET — 38 findings still wrong in print

Sorted HIGH → MEDIUM → LOW. Line numbers are **current at `6b8b49a0`**, not the board's 2026-08-02 anchors.

### HIGH (10)

| # | Current site | What is still wrong |
|---|---|---|
| 1 | `vol_0/chapters/03_computational_graph.tex:33` | Poisson-disk asserted as the genesis carrier; D1 ratified `srs z=3`. Route-to-core, docket item (i) unruled since 2026-08-02. Printed seam-disclosure exists at `:74`; the sentence itself is unqualified. |
| 2 | `vol_1/chapters/02_macroscopic_moduli.tex:133` | "the substrate-scale derivation **closes** the magic-angle equation" — KB Q-G47 framing RETRACTED 2026-06-14, `u₀*≈0.187` back-fit. clm-iouqn9 solidity 0.55, do-not-build-deeper. |
| 3 | `vol_1/chapters/08_alpha_golden_torus.tex:79` | spin-½ "substrate-derived **end-to-end**"; KB carve says STRUCTURE derived / SELECTION posited, PEER-WITH-SM. File untouched by the wave. |
| 4 | `vol_3/chapters/15_black_hole_orbital_resonance.tex:252` | Prints "over-predicted spin correction by ~13% mean" — **that diagnosis was RETRACTED 2026-07-20**; the KB twin got the fix, the print did not. ★The ringdown wave rewrote `:273/:292/:294/:408` and stepped over this line. |
| 5 | `vol_3/.../15_...tex:354` (raster `bh_untapped_predictions.png`) | Raster still plots the retracted LIGO-catalog comparison. **0 commits since board base**, md5 unchanged. Caption at `:355` now discloses it honestly; the artwork does not. |
| 6 | `vol_4/chapters/15_autoresonant_breakdown_spice.tex:34` | 43.65 kV / 60 kV two-threshold framing, whole chapter. Governing KB leaf opens **"⛔ INVALIDATED — RECOMPUTATION REQUIRED."** Zero banners in the file. Routed hold, never ruled. |
| 7 | `vol_5/chapters/02_organic_circuitry.tex:546` | "$K=2G$ selects the dense FCC layout" vs Axiom 1's chiral K4 `I4₁32`. ★Its own KB home **mirrors the defect** (hbond-op4-equilibrium.md:69/:121, membrane-phase-buffering.md:66) — this is a KB+print lockstep fix, not a print edit. |
| 8 | `vol_5/chapters/07_solvent_damping.tex:37` | $G_{solvent}\approx10^{-24}$ S against the ratified `def-tk1xfm` bridge $R=\xi^{-2}\eta$. Carries "**This is the key result.**" at `:96`. |
| 9 | `vol_5/chapters/07_solvent_damping.tex:102` | "astronomically larger" where the chapter's own inputs give factor ~1.55. |
| 10 | `vol_6/chapters/B_high_z_boundary.tex:74` | B/A = 11.2–11.8 MeV, ~30% above the empirical Fe-56 peak (8.79), no disclosure. File predates the board base — never touched. |

### MEDIUM (13)

| # | Current site | What is still wrong |
|---|---|---|
| 11 | `vol_0/chapters/04_dcve.tex:114-116` | Announces "the non-linear AQUAL Lagrangian definition:" — colon, blank line, orphaned "Where" clause. **Zero equation environments in the section**; `:116` is EOF. Byte-verified. |
| 12 | `vol_1/chapters/03_quantum_and_signal_dynamics.tex:464` + `:516` | CHSH "no imported quantum postulates" vs `[SPIN-HALF-POSITED]`. Note: the KB mirror carries the same phrase — corpus-wide ruling, not a print lag. |
| 13 | `vol_1/chapters/05_universal_spatial_tension.tex:41` (+`:98`,`:113`) | Muon torsional-coupling $\alpha\sqrt{3/7}$ label under a live 🔴 OPEN FLAG. **Zero commits to this file in the whole epic.** |
| 14 | `vol_2/chapters/07_quantum_mechanics_and_orbitals.tex:243` | $N_{eff}=1.0+0.5=1.5$ and +72%→−2.6% — **no KB home anywhere** (0 hits in 858 leaves) — and contradicts $N_{eff}=2.0$ ten lines later at `:253`, which *is* KB-homed. Also carries the third un-swept "Axiom 3 rigidly mandates $G=K/2$" site. |
| 15 | `vol_2/chapters/11_standard_model_overdrive.tex:66` | "vs months on a supercomputer for Lattice QCD **at comparable accuracy**" — clm-dboxok explicitly non-claims head-to-head accuracy. `git diff` on ch11 is **empty** since board base. |
| 16 | `vol_2/chapters/11_standard_model_overdrive.tex:123` | "The universe is structurally scale-invariant… U-235 and protein folding" — arc-map books N13 protein impedance-folding NEGATIVE; Core walk-back STAGED, not landed, 34 days. |
| 17 | `vol_3/chapters/08_gravitational_waves.tex:11` + `:372` | "~28 orders of magnitude below snap" while the same chapter's resultbox at `:362` prints $2\times10^{-25}$ and `:365` says twenty-five. ★ch08 was *passed over*, not gated — its only ringdown commit is a figure regen. |
| 18 | `vol_5/chapters/07_solvent_damping.tex:1` | Whole 142-line chapter has **no KB home leaf** (39-file vol5 tree enumerated by name, 0 commits in range). Prints "This is the key result" and a 20-orders margin with no truth-source card. |
| 19 | `vol_6/chapters/01_computational.tex:157` | "matching the CODATA empirical limit… to within 0.001%" — no σ, no vintage; CONVENTIONS 302(b)/304(d) ban bare "matches". Exemplar of a volume-wide pattern. |
| 20 | `vol_6/chapters/B_high_z_boundary.tex:1-98` | In print via `main.tex:81`; **zero `\kbleaf`, zero claim-id in 98 lines**; no KB counterpart (two-method search). |
| 21 | `vol_6/chapters/B_high_z_boundary.tex:10` | S-32 is simultaneously the Fibonacci regime's *worst* case (0.41%) and an exact Cube solution (0.000%) in the same volume. **Plus** Cl-35 at 1.465% inside the declared band, vs a stated 0.41% maximum. |
| 22 | `backmatter/05_universal_solver_toolchain.tex:712` | "proves that **biological shape is a direct mechanical consequence of electronic feedline geometry**" — KB internally inconsistent (leaf asserts it unbannered at `solver-toolchain.md:553`; arc-map books N13 NEGATIVE). The 2026-08-11 R40 sweep passed through this file and demoted `:214`/`:468`, not `:553`. |
| 23 | `papers/2026_birefringence_letter/main.tex:1108` | Fig. 1's QED leg rides $\alpha/(15\pi)$ while Table I's caption declares $2\alpha/(15\pi)$. ★In the observable it's **4×**, not 2× ($P\propto\delta n^2$): figure JSON gives $P_{qed}=2.757\!\times\!10^{-14}$, Table I prints $1.10\!\times\!10^{-13}$. |

### LOW (15)

`vol_0/01_theoretical_stress_tests.tex:81` (Holographic "recovers/emerges" on clm-nhlo1e, solidity 0.3 — contestable, banner grades at 0.75) · `vol_0/04_dcve.tex:101` (Vakulenko-Kapitanski, no adopted-not-derived carve; bound is vacuous for the 0₁ unknot) · `vol_1/01_fundamental_axioms.tex:198` ("3D amorphous central-force network", open D3) · `manuscript/ave-kb/vol4/.../op21-multi-mode-mode-counting.md:205` (KB→print pointer, drift widened 31→50 lines *by* the vol1 fix) · `vol_5/common/translation_protein.tex:31` (salt-bridge T19 flag, explicitly not adjudicated) · `vol_5/01_biophysics_intro.tex:36` (+`:11`,`:70`,`:133`) ($Q_{backbone}\approx7$ un-caveated; the AVE-Protein disclosure box covers the folding engine, not this) · `vol_5/02_organic_circuitry.tex:662` ($n_{coop}=9$ from $z=4$ vs carrier $z=3$) · `vol_5/06_biophysics_pharmacology.tex:477-479` (cancer/red-light/methylene-blue flat assertions; clm-8zwyl3 solidity **0.10**, `build_status: refuted, do not use`; file has 0 commits in range) · `vol_6/00_introduction.tex:46` ($K$ = coupling **and** bulk modulus in one chapter, no thesaurus row) · `vol_6/10_oxygen.tex:19` vs `:65` ($R_{tet}$ 33.393 vs 33.383, no record in print *or* KB — strictly worse than the neon case the wave fixed) · `vol_6/14_magnesium.tex:94` (Op3 reflection as loss vs RULING 21 lossless transduction) · `vol_9/06_temperature_characteristics.tex:225` ("one substance" vs the ratified ontology-grade convention) · `vol_9/14_phase_diagrams.tex:279` (+ mirror `vol_3/12_cosmological_characteristics.tex:195`) (18/49 with no cold-$a_*{=}0$ scope; **byte-identical** to board base) · `backmatter/12_mathematical_closure.tex:61`/`:65` ("62/62 PASSED", "168/168 framework files" under a "Dynamic Output — Generated from constants.py" label; measured 264 test files / 3200 tests / 202 `.py` — **further from truth than when the board measured it**; propagates to `:261` + 3 KB mirror lines) · `papers/.../main.tex:1114` (figure legend says "Demonstrated purity floor 8e-11" while the body reserves "demonstrated" for 2.4e-10; the generator's own comment calls it "record").

---

## 3. ★ REGRESSED — **ZERO**

No finding fixed by the wave has drifted back. I take this seriously enough to say what was actually tested rather than assert it:

- **backmatter lane called one REGRESSED and its verifier overturned it.** `04_physics_engine_architecture.tex` — the board's quoted rows (`mechanics/`, `hardware/`) are gone from live print; what is stale are *different lines* (`:165` viz 1-vs-2, `:168` solvers 31-vs-34, drifted by four `src/ave/` commits on 2026-08-24/25). Under the vacated-cite rule that is a **fresh finding**, not the board's finding regressing. The caption is a dated snapshot ("verified against `src/ave/` at HEAD **(2026-08-02)**") and was accurate when written.
- **vol0** re-diffed both post-wave commits (a ρ_bulk re-pin, a γ-tag) — additive.
- **vol2** swept 17 board-defect phrases across 16 files with `%`-comment filtering — every survivor is inside a Rule-12 preservation block.
- **vol6** found only one revert in the 24-commit window, and it is the *intentional* revert of the mis-dispatched REFUTED finding.
- **vol4's verifier** widened the regression sweep from 5 chapter files to all 45 files in the volume and found the same answer.

**Caveat on the strength of this zero:** every lane tested "is the fix present at HEAD," not "was it un-fixed and re-fixed inside the window." A transient regression that self-healed would not show. The zero is a statement about the tip, not about the path.

**The real argument for a gate rather than a sweep is not REGRESSED — it is SUPERSEDED (§5).** Nothing drifted back; instead the ground moved under six fixes, and in one case under the wave's own replacement text.

---

## 4. VACATED — 1

**vol9 finding #13 (board `:710`) — `vol_9/chapters/10_magnetic_microrotational_characteristics.tex:64`.**

**The PRINT half vacated — and it never existed.** At the board's own base commit `19285c5d`, line `:64` of that file is the literal string `\begin{itemize}`. Lines `:65-67` are the R1/R2/R3 drive-regime bullets. The board's PRINTED excerpt ("The Cosserat microrotational DOF is the substrate-native origin of intrinsic spin-½") lives at `:196` — which is finding **#15**, a separate entry, correctly discharged.

Three independent tells that this is a board-assembly defect, not a physics finding: (a) the anchor holds unrelated content at the board's own base; (b) #13's PRINTED + KB TRUTH fields are **byte-identical** to #15's (`diff` empty); (c) #13's VERIFY NOTE is a **byte-identical copy-paste of #11's** note, which is about $\sqrt{10/3}$ and ch03a:75 and has nothing to do with spin.

**Do not re-derive it — strike it.** Its substance is fully carried and discharged at #15. This is a **fifth owed board correction** beyond §6's four.

---

## 5. SUPERSEDED — 6. The KB moved; the board's fix is now wrong.

| Site (current) | Board wanted | What landed after 2026-08-02 |
|---|---|---|
| `vol_0/02_analytical_summaries.tex:35` | Carve $K{=}2G$ out of "zero further free parameters beyond those three" | **Grant Ruling 1**, `7a6f4ba6`, **2026-08-03** — one day after the board: "$K{=}2G$ is a constitutive-FORM import edge, **NOT a 4th calibration input; count stays 3**"; `expected-independent-count: 3` confirmed at `interlock-register.md:12`. Executing the board would land an edit the ruling forbids. |
| `vol_2/06_electroweak_and_higgs.tex:363-365` | Repair the $\Delta c_{crit}$ provenance to "K4 connectivity = trefoil crossing number" | ★**The KB then carved the wave's own replacement text.** `3ea79311` (2026-08-23/24, Grant "proceed"): leg 2 "Connectivity = trefoil crossing number: **ASSERTED — and in tension with canon**"; leg 1's transfer premise "asserted, not derived". Verified myself at `chiral-screening.md:28-48` + register carve `vol2/claim-quality.md:227`. **Un-propagated to print, and the ch03 mirror at `03_neutrino_sector.tex:159` carries all three legs including the one that fails its counterfactual.** |
| `vol_3/04_generative_cosmology.tex:186`,`:189-190` | Route to core, not adjudicated | **WHICH-MOMENT declaration, 2026-08-03: "THE DECLARATION: PRODUCT."** with a named (a)/(b) fork for these exact clauses, plus a radius caveat on arm (b). *Note the verifier's correction:* the routing **STANDS** — the ruling constrains the FORM of any answer, it does not pick one. |
| `vol_3/08_gravitational_waves.tex:371` | Soften "exclusively transverse" to admit an O(1) bulk admixture | **R40/#930/ratified Axiom 5 killed the bulk radiative port outright (2026-08-11).** The admixture-honest wording is now the **DEMOTED** text (`:107`, `:262`); "exclusively transverse" is what survives. `:391` already prints $F_{bulk}\equiv0$. **Executing this finding would re-introduce a killed claim.** |
| `vol_9/01_general_description.tex:45` | Reconcile the print to a LIVE independent bulk radiative port | `port-register.md:87` now ends **`🔴 [DEMOTED 2026-08-11 — R40-B2a]`** with ⚑BIAS-DEBT. ★**Trap:** the leaf's frontmatter at `:5` still asserts the old exclusion verbatim — a `:5`-only re-check reads the finding as still-good and is wrong. |
| `papers/.../main.tex:488` | Pull $I_{max}\simeq116$ A toward the KB's 124.4 A | Board compared two different objects. At the board's **own base**, `operators.md:145` already carried 116 A as **CANONICAL** for the slew-μ kernel the Letter prints. Then `theorem-thesaurus.md` §6 (2026-08-03/04) minted a **three-sense $I_{max}$ row** naming both values, differing by exactly $4\pi\sqrt\alpha$, and cites *the Letter's own ledger* as sense-1's receipt. New requirement the board never stated: `:312` — "a quoted $I_{max}$ must name its TIER." |

**Cross-reference to the 2026-09-06 scan:** the scan's tool and output live on the **unmerged branch `docs/2026-09-06-manuscript-kb-sync`** (tip `bc9d6c20`), not on `main` — which is why all ten lanes reported it missing and **not one of them could run the prescribed intersection**. I recovered it and ran the intersection myself; see §8. Of the 6 supersessions, **4 of the 6 files appear in the 190** (`vol_0/02_analytical_summaries.tex`, `vol_2/06_electroweak_and_higgs.tex`, `vol_3/08_gravitational_waves.tex`, `vol_9/01_general_description.tex`), but at **different lines** — the scan flagged the same *files* through different cites. So the 6 SUPERSEDED were found by reading, not by the scan, and the scan would not have named them.

---

## 6. THE GATED SET — the gate FIRED. §6 is stale.

**Board §6 asserts:** *"The gate therefore HOLDS: vol3 ch08 + ch15, `backmatter/07:{85,211,213}`… stay unexecuted. The known cost, disclosed in print: `backmatter/07` prints a withdrawal at `:145` while `:211/:213` still print the withdrawn claim."*

**Both halves are false at `6b8b49a0`. I verified this directly.**

The ringdown wave fired **2026-08-05** — PR #883 (`docs/ringdown-wave-0805`) and PR #898. `vol3 ch15` took **seven** `docs(ringdown)` commits; `backmatter/07` took two (`974537cd`, `96a57eba`).

| Gated finding | Status at HEAD |
|---|---|
| vol3 ch15:250 | **STILL-LIVE** — the wave rewrote `:273/:292/:294/:408` and skipped this one |
| vol3 ch15:271, :290, :292 (×2), :354, :387 | DISCHARGED (6) |
| vol3 ch15:337 | **SPLIT** — caption discharged, raster untouched (0 commits) |
| vol9 ch03:205 | DISCHARGED — the release commit's own body names it as "the one site #842 explicitly held as gated-ringdown" |
| backmatter/07:85, :211, :213 | DISCHARGED (3) |

**10 of 12 clean, 1 still-live, 1 split.**

**The `07:145` vs `:211/:213` in-print seam is CLOSED.** Read at HEAD:
- `:85` — "**1.7\% GR** (cold $a_*=0$; LIGO-catalog column withdrawn 2026-08-05, B1)"
- `:212-214` — "**Seam resolved 2026-08-05 (R11).** The ``10--18\% agreement with three LIGO events'' clause and the ``most direct experimental validation…'' grade that stood here are **withdrawn with no replacement**"
- `:145` — "*In-chapter seam --- RESOLVED 2026-08-05 (R11…)*… the seam this note used to disclose is **closed rather than disclosed**."

**What did NOT fire:** the ch08 half of the chapter-level rule. `vol3 ch08`'s only ringdown-lane commit is a `hulse_taylor` figure regeneration. Its saturation-ratio rulers (`:11`, `:372`) were passed over, not held — which is why I book them STILL-LIVE, not GATED.

**The one genuine GATED item is not ringdown at all:** vol9 #17, `vol_9/14_phase_diagrams.tex:105`, held by two docket receipts (`2026-08-03-mr-handoff-mechanical.md:5` held-list with a blob-level hold check; `2026-08-02-mr-ringdown-adjacent.md:4` — "the RULING requested is on the LEAF pair, not the print"). Still owed.

**Also flagged, not adjudicated (backmatter verifier, and I confirm the receipts exist):** `backmatter/07:145` now prints that a ROOT-CERTIFIED instrument's pre-registered rider **fired**, falsifying $r_{eff}=r_{sat}/(1+\nu_{vac})$ as a derivation of the eigenfrequency — while `vol3/claim-quality.md:198` still books that exact chain as a zero-free-parameter derivation and `:217` grades it "Solidity 0.55 UNCHANGED — anchored by the cold 18/49." Print is now **ahead** of KB, inverted from the usual direction. The result doc withholds propagation by design. This is a routed-open adjudication seam nobody owns.

---

## 7. WHAT THE BOARD OWES ITSELF

**All four OWED corrections: APPLIED to §5. §6's list is what's stale.**

| # | Item | Status |
|---|---|---|
| 1 | `backmatter/01_appendices.tex:{132,135,196}` → crib-covered-mechanical | **DONE** — `14ba1806`, 2026-08-03. §5 headers at `:761`, `:785`, `:835` all carry `~~[route-to-core]~~ → **[crib-covered-mechanical]**` |
| 2 | vol5 `07_solvent_damping.tex:41` → flip to routed | **DONE** — `87aacc31`, 2026-08-03. §5 `:532` carries the re-tag; §4(ii) at `:60` carries the ×9.96 re-derivation |
| 3 | finding-16 neon cite is `:53` not `:54` | **DONE** — `04e0c41f`. §5 `:635` carries the struck clause + Rule-12 correction |
| 4 | `A_heavy_element_catalog.tex:20` dispatched while REFUTED | **DONE** — `c9735ee3` recorded it *and* added the §4 REFUTED-blocks-dispatch gate; the edit was reverted in #852 and `:20` reads its full paragraph at HEAD |

**The defect:** §6's OWED list was written by the close-out commit `745b5951` (2026-08-03, 05:47), and commits `14ba1806` (06:50) and `87aacc31` (06:52) discharged items 1 and 2 **inside the same PR (#855)** without updating the list. So the board records as owed what it already paid.

**A consequence worth knowing:** because #855 merged 84 seconds before #862, the vol5 k_HB re-tag was never in #862's branch — that lane executed the site as `[mechanical]` while a route-to-core re-tag existed on `main`. Outcome was right (11.2 → 1.12 N/m, matching INVARIANT-C3) and the KB-home half was left routed in-file. But it was a **concurrent-branch race**, not a lane ignoring a standing tag. The vol5 lane's governance write-up inverted this; its verifier caught it.

**A FIFTH correction is now owed:** strike vol9 finding #13 (§4, above).

**Addenda — all six done:**

| Addendum | Status |
|---|---|
| vol1 `07_regime_map.tex:19` (B1 tag) | DONE — `b5fc6bee`, PR **#862** |
| vol2 `09_computational_proof.tex:50` (sub-3 Å) | DONE — Rule-12 scope note now at `:55-60` |
| vol6 `circuits/circuit_h1.tex:18` (INVARIANT-N1) | DONE — `36058f25`; `:38` reads "$0_1$ unknot body; $(2,3)$ phase-space winding"; both PDFs regenerated, md5-identical |
| `backmatter/12_mathematical_closure.tex:201` (CRIB-4 superlative) | DONE — `c7657ff9`, PR #859; now "three empirical anchors at zero free parameters" |
| vol4 status-sync (4 leaves) | DONE — `6d5e0ddc`, "addendum 5 — def-tk1xfm status-sync at the 4 vol4 sites #847 flagged" |
| dark-TikZ sweep | DONE — PR **#893** (post-close-out, so §6 could not know). Count corrected 23→22 of 29; 8 remain, each with a disclosed carve-out (2 R6, 1 R5 strike-don't-delete, 5 STOPPED on a named provenance blocker) |

**Two PRs post-date §6's table and are absent from it: #862 and #893.** Anything reading §6's PR list as the execution record is missing both.

---

## 8. ★ RECOMMENDATION ON SEQUENCING

**The question: does the 38-item live set already cover the 190 material-lag sites, or is a new reading lane warranted?**

**Answer: they are disjoint. Dispatch the lane. It is not duplicative work.**

I recovered the scan from the unmerged branch and intersected it myself:

- The 190 rows resolve to **159 distinct `file:line` cite-sites across 56 files**.
- **Exact `file:line` overlap with the 38-item live set: ZERO.**
- Only **12 of the 34 live manuscript files** appear anywhere in the scan, and at different lines.
- Distribution is lopsided: **vol9 79, backmatter 21, vol2 19, vol3 12, vol0 11, vol4 7, vol1 6, frontmatter 2, vol6 1, vol5 1.** Half the debt is in one volume.
- Top drivers: `delta-strain-cosmic-tcc.md` (18), `vocabulary-register.md` (17), `form-deriving-value-importing.md` (14), `device-circuit-models.md` (12).

**The two populations measure different things.** The board asked *"does the print contradict the KB as of 2026-08-02?"* The scan asks *"has the cited leaf gained a demotion marker since the .tex was last touched?"* The wave answered the first question and, by touching those files on 2026-08-02, mostly **reset the clock** on them. The 190 is what accumulated in the five weeks *after*.

**Three things that must travel with the dispatch, or the lane will be worth less than its cost:**

1. **The tool is not on `main`.** `manuscript/ave-kb/tools/audit-tex-kb-staleness.py` and both output files live only on `docs/2026-09-06-manuscript-kb-sync`. All ten lanes reported it missing and all ten substituted ad-hoc per-leaf checks. Land the branch or hand the lane the raw scan.

2. **A mechanical flag is a candidate, not a defect — and the sample so far says most are benign.** Three scan-flagged sites were adjudicated by reading in this pass and **all three came back benign**: vol5's `ch02:58 → vocabulary-register.md` (the `def-tk1xfm` block is byte-identical; only a build-scaffold comment above it moved), vol6's and vol0's `srs-band-structure.md:116` (the R40-B1 demotion kills the $\sqrt{10/3}$ *speed-ratio* reading; the `K=2G RE-EXPRESSION` provenance the cites lean on **explicitly survives** at `:188`). Three of three, on a sample of three — that is a caution about yield, not a measurement of it. The scan's own RESULT doc says so: *"It does not decide whether any given site is wrong — that needs reading, and it is the next stage."*

3. **Scope it. Do not run 159 sites as one lane.** vol9 alone is 79 (half the population, one volume, one owner) and is also where the 5 undisclosed `do-not-build` cites sit. `frontmatter` (2) and vol5/vol6 (1 each) are noise at this granularity.

**Sequencing I would put to you:** the 38 live findings are *known-wrong print* and cost nothing to adjudicate — they need lanes, not investigation. The 159 sites are *unknown* and need reading before anyone knows if they are work. Those are different queues and can run in parallel without collision, because they do not share a single line.

**One caveat against my own recommendation, stated because it cuts:** the 6 SUPERSEDED findings — the class that argues hardest for the lane — were **all found by reading, none by the scan**, and the scan would not have named them (it flagged 4 of the 6 files at *other* lines). If what you actually want is "find the fixes whose ground moved," the scan is an imperfect instrument for it. It measures cite-level marker addition; supersession is a semantic property of the argument. The vol2 case is the sharpest example: the KB carved **the wave's own replacement text**, a failure mode the board's schema cannot express and the scan flagged only obliquely.

---

## 9. WHERE THE VERIFIERS OVERTURNED THE LANES

**Three verdict flips out of 154, plus two tally corrections. Nine verified overturns were evidence-level, not verdict-level.**

| Lane | Verdict flips | Other corrections |
|---|---|---|
| vol0 | 0 | ★**Tally**: summary said 8D/3SL, its own array says **7D/4SL**. The lost finding is ch01:81. 2 sub-claim overturns: the graph-architecture.md co-lag was already CLOSED (lane copied the .tex's own 2026-08-02 comment instead of opening the leaf); the backmatter mirror is **not `\input` by anything**, so its un-reconciled twins don't reach a reader. |
| vol1 | 0 | 0 missed. Verifier read every candidate qualifier token in each host file, upgrading "not fixed at the site" to "not fixed anywhere in the file". |
| vol2 | **1** — F8 `06:363-365` DISCHARGED → **SUPERSEDED** | Found by diffing the citing `.tex`'s last commit against each cited leaf. The carve sits below a `---` rule, 22 lines after the sentence it demotes, with that sentence preserved verbatim above — invisible to a top-down read. |
| vol3 | **1** — F6 ch15:337 DISCHARGED → **SPLIT** | Got the receipt the lane lacked (raster: 0 commits, md5 unchanged), which turns the fix into a caption-only fix — exactly what the board's frozen criterion pre-empted: *"NOT dischargeable by any caption edit"*. Also: F9's note over-stated the ruling as an adjudication; the routing **STANDS**. |
| vol4 | 0 | Closed the lane's own blind spot (verified manifest inclusion) and widened the regression sweep from 5 files to 45. |
| vol5 | 0 | **5 evidence-level overturns.** Two matter: (a) the k_HB governance claim was **inverted** — the re-tag *was* applied; §6's list is what's stale; (b) finding 2's KB home **mirrors the FCC defect** in near-identical bytes, so it is a KB+print lockstep fix, not a print edit. |
| vol6 | 0 | ★**Tally**: summary said 13D/6SL, array says **12D/7SL** — the lost finding is the $K$ glyph collision. Also: F18's reasoning was inverted (the new leaf's §5 is Op3 as the theorem's *negative control*, not a boundary port), and F15's KB enumeration was short by 2 sites. |
| vol9 | 0 | Verifier ran a substitute staleness intersection and confirmed the VACATED call at the board's own base. |
| backmatter | **1** — `04:99` REGRESSED → **DISCHARGED** + fresh item | Board's PRINTED excerpt no longer exists (vacated cite); the stale rows are different lines. Also surfaced the `07:145` print-ahead-of-KB seam (§6). |
| papers | 0 | 2 evidence-level: a mis-assigned `provenance.md:854`; and the Fig.1/Table-I gap is **4×**, not 2×, in the observable. |

**What I checked myself, at `6b8b49a0`, in a throwaway worktree (tip asserted before every read, worktree removed after):**

1. Board arithmetic: 158 `####` blocks, 4 REFUTED, 154 live; per-volume headers sum to 154.
2. The vol0 `##`-vs-`###` header defect that broke one verifier's count.
3. The gated-set enumeration at board `:45` and the full §6 close-out text.
4. `backmatter/07` at `:85`, `:144-146`, `:210-215` **read in full**, plus its 10-commit log since board base — the gate fired, the seam is closed.
5. `vol3 ch15:252` — the retracted 13% diagnosis still in print — plus the 18-commit ringdown-wave log on that file, and `bh_untapped_predictions.png` at **0 commits**.
6. All four OWED corrections present in §5, and the `git log` proving §6's list self-discharged inside PR #855.
7. Four of the six addenda read at HEAD (vol2 sub-3 Å, vol6 circuit_h1, backmatter ch12, vol4 status-sync).
8. The staleness tool's actual location — branch `docs/2026-09-06-manuscript-kb-sync`, tip `bc9d6c20` — and the scan's composition and headline.
9. The live-set × 190-site intersection (zero exact matches), computed from the scan's raw rows.
10. The vol2 F8 supersession: `chiral-screening.md:28-37` carve read directly against print `06:363-365`, plus the carve commit `3ea79311`.

---

## 10. METHOD AND BLIND SPOTS OF *THIS* DOCUMENT

**Method.** Ten lanes each read their slice at `6b8b49a0` in isolated worktrees; ten verifiers re-checked refute-by-default, and every verifier re-opened more than the required minimum (several checked all 100% of their slice). I did not re-read all 154 findings. I synthesized their reports, applied every verifier overturn to the ledger, and independently verified the ten items above — chosen because each one, if wrong, changes what gets dispatched next.

**Blind spots, stated as limits on specific claims, not as absolutes:**

1. **The ledger is a synthesis, not a re-read.** 108 DISCHARGED rests on the lanes' reads plus their verifiers' spot-checks (which ranged from 3-of-N to all-of-N). I verified 10 items directly. If a lane and its verifier shared a blind spot, I inherited it.
2. **No build was run by anyone.** Every "in print" and "discharged" judgment in all twenty reports is a source-level judgment. `%`-comment position and manifest inclusion were checked in several volumes; no PDF was compiled. One live consequence: `04_physics_engine_architecture.tex`'s repair note discloses that its Tier-3 block was **already** clipping ~21 lines to an overfull vbox — so at least one item may not reach a reader at all, in either direction.
3. **The intersection in §8 is exact-`file:line` matching.** Two findings could address the same passage at adjacent lines and register as disjoint. I also matched at file granularity (12 of 34) and report both. The 190 covers `manuscript/` only — `papers/` is outside its scan scope entirely, so the 2 live papers findings could not have overlapped by construction.
4. **The board's own §5 fields are hard-truncated** at ~415-500 characters, mid-word, with no ellipsis — confirmed by four independent lanes measuring the raw bytes. Several findings were adjudicated against a partial statement of their own argument. Named casualties: vol0 findings 2 and 9, vol2 finding 10 (its "MISSED FOURTH SITE" clause is unreadable), vol5 findings 2 and 13, vol9's multi-site enumerations, papers' terminal REASON field. Where a disposition lives in a truncated tail, no lane saw it.
5. **The `0 REGRESSED` is a tip measurement, not a path measurement** (§3).
6. **The `6 SUPERSEDED` is a floor.** No lane could run the prescribed intersection (tool off-`main`); each substituted a per-leaf check over only the leaves its own findings cite. A supersession in a leaf reachable only transitively is invisible to all ten.
7. **Two verdicts in the set are contestable and were flagged as such by their own lanes rather than presented as settled**: vol0's ch01:81 Holographic (STILL-LIVE vs discharged-under-a-chapter-banner-graded-three-tiers-higher) and vol3's ch15:337 raster split. Both were resolved conservatively — toward more work, not less — so nothing is deleted by the call.
8. **I adjudicated no physics and propose no repair.** The Δc=3 carve, the A4 $I_{max}$ tier ruling, the WHICH-MOMENT fork, the cold-Q pole falsification, the spec-vs-carrier register split — all reported as corpus state with dates and file:lines, all left to you.