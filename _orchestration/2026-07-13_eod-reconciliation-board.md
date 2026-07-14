# THE RECONCILIATION BOARD — 2026-07-13 EOD

**Class:** durable tracking doc (orchestration record). Reconciles the 2026-07-13
findings against merged HEAD, and tracks the open A/B/C items + nine Grant-decision
points to closure.
**Baseline:** all four reconciliation lanes ran against `origin/main` HEAD
`9bfc50ef6150e09c639ffa1117bea2d095ca6cd8` (merge of #674). No lane claim failed
verification; two nuances flagged inline (⚠).
**This PR:** `docs/eod-reconciliation-hygiene-batch` lands the gate-free hygiene batch
(items A1–A9) + task-C5 + the m_p/m_e audit card (C3). B-series correction notes and
all nine decision points are **Grant-gated and out of scope** here — tracked below.
**Companion doc:** the m_p/m_e value-blind audit card lands at
[`research/2026-07-13_mp-me-mass-ratio-audit.md`](../research/2026-07-13_mp-me-mass-ratio-audit.md)
(discharges receipt-debt C3; referenced by B2/B3).

---

## FINDINGS DISPOSITIONS

**UNLANDED REPAIRS: NONE.** Every confirmed finding across all six PRs (#666, #667,
#668, #669, #670, #674) has its repair commit as an ancestor of `origin/main` AND its
repair content grep-confirmed live at HEAD (two-method: commit ancestry +
content-at-HEAD).

| PR | Finding | Sev | Disposition | Receipt at HEAD |
|---|---|---|---|---|
| #666 | #1 primary discriminator: 3 inconsistent OFF-states, no comparison formula | MAJOR | REPAIRED `fef573a5` | §1.6 ledger spec + ARM-FRONTIER/ARM-Λ, CHARTER.md:100-105 |
| #666 | #2 §(iii) equated friction with non-conservation (false) | MAJOR | REPAIRED `6c578d3e` | R2: Ax3 class = cited premise, deferred tier-2 |
| #666 | #3 three §4.2 hard detectors consume state the 2-scalar ledger lacks | MAJOR | REPAIRED `13a1abac` | ★DEFERRED-to-tier-2, CHARTER.md:301-303 |
| #666 | #4 first-law/ΔE_cryst mis-anchored | MINOR | REPAIRED `94d8027e` | re-anchored → dark-energy-latent-heat-definition.md:130 |
| #666 | #5 bemf :94 ellipsis-spliced quote | MINOR | REPAIRED `94d8027e` | R5 receipt-fidelity cluster |
| #666 | #6 false math: constant rate→"Λ" (actually linear decay) | MAJOR | REPAIRED `fef573a5` | KEEP-BOTH correction, R1 cluster |
| #666 | #7 frontier default Γ=3Hρ ⇒ ρ∝a⁻³ exact w=0; signatures INVERTED | MAJOR | REPAIRED `e532a236` | §4.7 posture banked, CHARTER.md:180-183 |
| #666 | #8 cascade address missing ★QUARANTINE tags | MINOR | REPAIRED `94d8027e` | CHARTER.md:48-50 |
| #667 | R1/F4 adjacent stale n_eff∝S | MINOR | REPAIRED `0bdef1e6` | √S roll-off live, ee-bench-plateau.md:18,28 |
| #667 | R2 page-one ellipsis-splice | MINOR | REPAIRED `259baecf` | un-spliced, repointed to sve-vacuum-network-ee-analysis.md:68 |
| #667 | R3 trade-study missing not-AVE-confirming frame | MINOR | REPAIRED `ca96a135` | binding frame, cites CVR-REQ-FRAME by ID |
| #667 | R4 three cites shifted +3 by own F2 edit | MINOR | REPAIRED `259baecf` | :1843→:1846 etc. |
| #667 | R5 recap mispaired 10⁻¹⁷ with E~10⁸ V/m | MINOR | REPAIRED `259baecf` | corrected to 1.2×10⁻¹⁸ |
| #667 | R6 10 kV example violated own V_max≲9.1 kV | MINOR | REPAIRED `259baecf` | restated at 9 kV |
| #667 | slope-resolution formula | MINOR | CONFIRMED-KEPT (verified CONSERVATIVE) | PR body |
| #667 | whitespace-verbatim | NONE | DISCARDED (git is the trail) | PR body post-review |
| #668 | #1 bin gap mislabeled "(ii) degenerate" | MINOR | REPAIRED `83228a7b` | AMBIGUOUS/REWORK band, t1_…gate.py:243,266 |
| #668 | #2 "discharges the R2 rhyme" over-claim | MINOR | REPAIRED `83228a7b` | "instantiates R2's principle" |
| #668 | #3 prereg Outcome-B "chord" wording | MINOR | REPAIRED `83228a7b` | erratum; frozen prereg byte-unedited |
| #669 | #1 sabotage plant A inverted (fake R=1.0) | MINOR | REPAIRED `70551422` | zeros BACKWARD ports `keep=(w>=-1e-9)`, srs_…backscatter.py:161,164 |
| #669 | #2 bin-(iii) meter-blind sub-clause unimplemented | MINOR | REPAIRED `70551422` | INDETERMINATE if R_dis<0.15, :271-275 |
| #669 | #3 "band-edge characterization" over-promise | MINOR | REPAIRED `70551422` | "R(k) rise toward zone boundary" |
| #669 | 1 additional finding | — | REFUTED on verify (no repair owed) | PR review comment |
| #670 | #1,#3 frozen mechanism-note vs E≡1.0 data | MAJOR→MINOR | REPAIRED `bd4651e2` | dated ERRATUM, prereg_FROZEN.md:185 (frozen body untouched) |
| #670 | #2 φ≥0.80 floor one-sided (runaway passes) | MINOR | REPAIRED `bd4651e2` | RESULT §5 note |
| #670 | #4 "(ii) boundary-clean" self-conflict | MINOR | REPAIRED `bd4651e2` | reworded: φ-dispersion trend boundary-insensitive |
| #670 | #5 sabotage plant "valid" via E-lift proxy; φ-channel never exercised | MAJOR | REPAIRED `bd4651e2` | `phi_channel_exercised=False`, genesis_npersist_battery.py:194 |
| #674 | self-review: min_κ=0.088 coarse; true min ~0.046 | MINOR | REPAIRED `648cc5d1` | fine-κ robustness banked, RESULT §6 |
| #674 | R1 (1+3): Λ-degeneracy boundary unquantified | MINOR | REPAIRED `b1b3f0d0` | §6.1 two-limits map, result.md:235; `lambda_boundary_map` |
| #674 | R2 (2+4): MAGNITUDE-TUNE gate one-armed | MINOR | REPAIRED `b1b3f0d0` | `gate_input_provenance`, f6_…ledger.py:242 |

**Traceability notes (WARN-level, not unlanded repairs):**
1. **#668 repair commit `83228a7b` is unnamed in the PR body** (freeze table says "(this
   push)"; reachable only via second parent of merge `14f5faec`). The routed
   Q-ladder-relabel follow-on should cite `83228a7b` explicitly.
2. **#674 "28→30 tests" is collected-cases, not `def test_` count** (14 functions at
   HEAD; delta = parametrization). ✅ **ADDRESSED by this PR** (task-C5, commit
   `31e007a1`): F6 result:141 restated "30 tests" → "30 collected cases (14 test
   functions, parametrized)".

---

## THE OPEN-ITEMS LEDGER

### A. One-batch hygiene items — **LANDED BY THIS PR** (`docs/eod-reconciliation-hygiene-batch`)

| # | Item | Disposition + commit |
|---|---|---|
| A1 | thermal-softening.md:11 stale cold triplet (1185/1872/2%) vs live cold values | **LANDED `8d94ba52`** — corrected to live solver I_scalar^(cold)=1170.59 → 1849.70 (+0.7377%). ⚠ flag-don't-fix: board spec's "I_scalar≈1162" is the *softened* value; the cold trace is 1170.59 (used, with cold-vs-softened caution note) |
| A2 | (2,5)-phase vs 6₂³-real register conflation (trampoline:708 + boundary-observables-m-q-j.md:48) | **LANDED** — boundary-obs half `22948644`, trampoline:708 half `463dc3e1` |
| A3 | knot-mode-isomorphism.md:21-22 INVARIANT-N1 phase-space qualifier | **LANDED `22948644`** |
| A4 | cosmic-axes-and-frames-glossary.md:5 retired ℳ_A glyph → prose | **LANDED `9ed75c1d`** |
| A5 | native_cage_imex.py 6 cites of absent companion native_cage_fdtd.py | **LANDED `5706b5b0`** — annotated historical (companion built on git 050f1088, never landed to main) |
| A6 | 10 stale omega-freeze anchors (:13-16 → :11) + R_H/ℓ_node value normalization (~10^39 → precise 3.455×10^38, all bridge sites) | **LANDED** — batch (13 files) `eb79f9c5`, trampoline sites `463dc3e1`, glossary site `9ed75c1d`. ⚠ flag: board's log10=38.55 corrected to verified 38.54. .tex manuscript bridge sites (5 files) DEFERRED to a manuscript-side pass (KB-leaf-first lockstep) |
| A7 | program-arc-map.md:404 "0-for-6/7" hedge → canonical 0-for-7 | **LANDED `8477529d`** — booked 0-for-7; X43/C13b increments noted Grant-gated (Decision 9) |
| A8 | form-deriving-value-importing.md missing reciprocal pointer to identity-break-test-design.md | **LANDED `47ec8f36`** |
| A9 | Six-scale table node-count column (KEEP-BOTH, open rows not settled) | **LANDED `463dc3e1`** |
| A10 | leaky-cavity theory.md:14 muon rung optional "not a cascade cutoff" cross-ref | **NOT OWED** (anti-re-discovery hardening; deferred, optional) |

**A6 full touched-site enumeration** (anchor repoint `:13-16`/`:7,13-16` → `:11`, and/or
`~10^39` value annotation → precise `3.455×10^38`): predictions.yaml:164/165,
cosmological-constant-closure.md:100, op14-cosmic-horizon-profile.md:12/:106,
lattice-genesis-hubble-tension.md:37, hubble-tension.md:39, mond-hoop-stress.md:13
(anchor only), zero-parameter-universe.md:47, full-derivation-chain.md:704,
cosmic-axes-and-frames-glossary.md:118 (anchor only), divergence-test-substrate-map.md:764,
trampoline-framework.md:623/898, vol9/index.md:45, vol9/ch12-cosmological-characteristics/
index.md:15/:55, translation-circuit.md:127, claim-quality-closure-roadmap.md:41. Legit
non-`:13-16` cascade ranges (`:13-40`, `:46-58`, `:34-40`, `:77-100`, `:102-116`, `:26`,
`:7`) left untouched. **DEFERRED (.tex, manuscript-side):** 01_fundamental_axioms.tex:34/237,
10_open_problems.tex:261, 04_generative_cosmology.tex:53, 12_cosmological_characteristics.tex:7/16/24/27/52.

### B. Correction-note items — **GRANT-GATED / auditor-specced (OUT OF SCOPE for this PR)**

| # | Item | Gate |
|---|---|---|
| B1 | #670 "closed-box" mislabel: RESULT calls pml=0 a "reflecting box" but engine is `np.roll` periodic **torus** (k4_tlm.py:393) | Auditor-specced erratum; interacts with Decision 1's fork (fork phrased on wrong boundary ontology — erratum should precede/accompany the ruling) |
| B2 | proton-identification.md:73 "Zero fit parameters" bold headline vs §2.2 asserted I_scalar + p_c residual | Harmonize headline with its own :73 🔴 2026-06-08 framing-precision annotation. Cross-ref the audit card (D2). Grant-gated framing |
| B3 | 6π⁵ (1836.1181, corpus 33× closer than CODATA) + δ_th≈α (0.83% gap) adjacencies undisclosed in baryon sector | Auditor-specced disclosure note. **The audit card (D2) now carries the value-blind data**; the leaf-side disclosure is the Grant-gated follow-on |
| B4 | trampoline:685 "envelope size set by ℓ_node" vs nucleus row 1 fm = 386× below ℓ_node | Auditor call (unqualified internal tension) |
| B5 | F6 CHARTER correction note owed (#674 §4.3-vs-§1.6/§4.7 self-conflict + a-priori FALSIFIED) | Correction-PR pattern; inherits Decision 2's Grant framing gate |
| B6 | identity-break-test-design.md:184 stale "the only tier-1 chord-carrier" = a-priori #674 falsified | Inherits Decision 2's Grant framing gate |
| B7 | registers-walk_framing.md:129 atom-rung "pending" superseded by same doc :182/:189 (#668 kill ratified) | Auditor call: annotate-in-place vs forward-pointer (§5 may be KEEP-BOTH-frozen) |
| B8 | leaky-cavity theory.md:14 Q_μ≈3.5e17 leaf/framing-doc status disagreement (:282 cited-lean-only) | Auditor adjudicates whether the x43 receipt discharges the debt |
| B9 | ARC-33 fork-close propagation: program-arc-map.md:306 still "surfaced not landed" after #669 adjudicated peer-class | Soft Grant nod (Grant-surfaced fork); + homogenization-split cross-ref + open band-edge sub-item (k·ℓ≤0.83) — Decision 7 |
| B10 | Letter v6 provenance §13.A: II.C narrowed one clause beyond K.M.'s literal review | Outstanding auditor-review item, applied in v6, NOT submission-blocking |

### C. Receipt debts

| # | Item | Disposition |
|---|---|---|
| C1 | Muon "0.74-cell radial straddle" — UNRECEIPTED walk estimate, no corpus home | **OPEN** — derive-or-tag (registers-walk_framing.md:282; srs RESULT :203; prereg :230,267) |
| C2 | CVR T-D ~10¹¹ V/m field-evaporation ceiling — `[TAG: from-memory engineering bound — receipt OWED]` | **OPEN** — pin before the trade migrates to KB |
| C3 | m_p/m_e audit card — session-only, no repo home | **LANDED `01c9a24f`** — `research/2026-07-13_mp-me-mass-ratio-audit.md` (AUDIT-CARD class). Downstream items can now cite this anchor |
| C4 | Three census Grant-questions (which-skin/cold-vs-driven/which-dials) — zero tracked-corpus footprint | **OPEN** — session-only; write into the census walk card before any STAGE-2/prereg freeze (Decision 5) |
| C5 | #674 "30 tests" phrasing | **LANDED `31e007a1`** — restated as collected-cases (task-C5) |

---

## DECISION POINTS — all **PENDING-GRANT** (none actioned by this PR)

**1. G-PERSIST stamp flip + closed-box fork + two follow-ons.** Stamp still
★PROPOSED-RULED (docket :434, :476, :485); #670 MERGED, leans CONFIRMS bin (ii)
A-WEAKENED via φ-dispersion; flip explicitly PENDING-GRANT and does **not** require
the fork (PML φ-trend boundary-clean on its own). *Verbatim fork question* (RESULT §7):
*"in the closed reflecting box, is φ growing to 10× the flux self-amplifying into a
bound resonance (genuine, → A-SUPPORTED), or is it the cavity pumping the Φ_link mode
because the flux has nowhere to leave (artifact, → A-WEAKENED holds)?"* ⚠ Note B1: the
"reflecting box" is actually a periodic torus — the erratum should land before/with the
fork ruling so Grant rules on the right boundary ontology. *Follow-on candidates* (§8,
verbatim): (i) *"a boundary-insensitive localization observable — e.g. the fraction of
interior energy / Φ_link² inside a central core"* (KEEP-BOTH new axis); (ii) *"a
φ-channel negative control … sustains φ without destroying the Cosserat state, to test
whether the load-bearing φ-detector can be fooled by external sustenance."* *Unblocks:*
stamp flip → RULED; remanence-before-node-mint build-order basis; dispatch of either
follow-on; Propagation item 3's four tracked-file writes. ⚠ Lane-3 flag: docket :434
says stamps "become effective on his merge of #661" (merged), yet :476/:485 still list
the flip as PENDING-GRANT — operative reading is flip still owed; Grant resolves the
trigger-vs-gate conflict when ruling.

**2. F6 tier-1 corpus reading (#674 §5.4).** Landed bin (i) LEDGER-CONSISTENT, charter
a-priori FALSIFIED; result bars implementer from drafting the corpus entry (auditor lane
lands any corpus/manual entry; result :280-282, :296-297). *Verbatim question* (§5.4):
*"does the always-separable / §4.7-inverted structure mean the frozen bin (i) should be
read as a genuine tier-1 form-existence result, OR does it mean the `D[ON,FRONTIER]`
metric fails to operationalize the attribution degeneracy the charter conceptually
intended (in which case the informative closure is still the CHARTER §4.5(iii) statement
that the homogeneous ledger is the wrong instrument, with the chord's real home the
DESI/Euclid spatial cross-correlation, dark-energy-latent-heat-definition.md:159)?"*
*Key numbers* (§6.1, NON-FROZEN): D[ON,Λ] crosses tol_form=1e-2 at τ₀≈300; weak-κ
D[ON,Λ]≤1e-2 for all κ≤0.013; frontier-best-mimic PHYSICAL κ=3.28 → D[ON,FRONTIER]=0.0456,
D[ON,Λ]=0.8952; global fine-scan min 0.046 > tol_form. *Unblocks:* the KB/manual entry
(dark-energy-latent-heat-definition.md:128+§5, engine-capability-map.md:152-155,
_orchestration/index.md:204), B5 charter note, B6 identity-break:184 fix, whether F6
tier-2 is chartered.

**3. n-p mass split gate.** Nothing dispatched or frozen (two-method zero: no
prereg/driver/handoff/docket row; only the pre-existing canonical leaf
proton-neutron-mass-split.md, clm-bh9p6s, T_nuc=(m_p/m_e)·T_EM — an asserted identity,
not a test). Audit-card criteria: none in-repo; if they exist they are session-only. *No
verbatim exists to quote.* *Unblocks:* dispatch of any n-p driver/prereg. **Note:** the
m_p/m_e audit card (D2) names this the #1 discriminator carrying the entire δ_th
structural burden after the archive-provenance dig — nothing is queued.

**4. m_p/m_e CI gate fork.** Tightest empirical gate = 0.5% (test_ave_engine.py:118,
`abs(PROTON_ELECTRON_RATIO - 1836.15)/1836.15 < 0.005`); no 3e-5 gate exists (grep zero;
:427 `< 1e-10` is a self-consistency identity, not empirical). *Question:* tighten toward
PDG 1836.15267343 (~1e-5) or hold at 0.5%? *Unblocks:* any tightening dispatch (the
audit card D2 §"what would settle it" #4 frames the fork).

**5. Cavity-census prereg.** Nothing frozen (two-method zero). ⚠ Task-framing mismatch:
the "three Grant questions (which-skin/cold-vs-driven/which-dials)" are NOT in the docket
D3 row — corpus-wide grep zero, session-only (ledger C4). Docket :481 verbatim:
*"REGISTERED (Grant 2026-07-13): two-shape KEEP-BOTH battery (sphere null vs horn-torus
canon-lean); STAGE 1 census grounding LANDED; STAGE 2 self-consistency/balance audit
rides the T_ij register (task #45); walk-first — nothing frozen yet; the only outcome
class that genuinely re-opens D3 territory = a STAGE-2 balance failure requiring interior
structure the singularity forbids."* Precursor-vs-end-state sub-fork (clm-uatcql,
vol2/claim-quality.md:1159) explicitly OPEN. *Question:* are the three questions chat-only,
and should they be written into the census walk card before any STAGE-2/prereg freeze?

**6. D-V Letter submission.** v6 PDF at HEAD (blob d7a05ec9), content SHA-256
`598e7d4b9cef…1500be` matches claims_by_hash.md V6; OTS present; chain V1→V4→V5→V6 intact;
Table-I byte-unchanged; kill line P_flip<1e-8 unmoved. Docket :65,:220: *"PENDING
(weekend) — Grant + Keith + Benn."* *Question:* submit? *Unblocks:* task #41 comment-strip
(gated on the submission call). B10 (§13.A flag) outstanding-but-applied, NOT blocking.

**7. srs-1/9 / T4 fork.** NOT a pending Grant physics decision: #669 landed it peer-class
CONSISTENCY, "no Grant word owed" (docket :475,:486). What IS owed: the arc-map
propagation (ARC-33 :306 still "surfaced not landed") — ledger B9, with only a soft Grant
nod for stamping a Grant-surfaced fork "adjudicated".

**8. CVR trade study T-A/T-B/T-C.** All three verbatim *"STATUS: OPEN — decision pending
(Grant + collaborator). SELECT NOTHING."* (DECISIONS-OPEN doc, #667); T-D THEORY-RULED
(PLATES). Binding frame: validation-ladder/anomaly-bound bench, NOT AVE-confirming. T-A
gap-holding (a vacuum-gap / b fused-silica Class-I / c flexure; Class-II EXCLUDED); T-B
standoff (a series cap = sign-degenerate confound / b virtual-ground transimpedance
preferred / c guard-shield layered on b); T-C gap-sweep (a shims / b flexure+closed-loop
nanopositioner / c piezo closed-loop only). T-A freezes WITH T-C (+T-D); T-B with the
front-end. *Unblocks:* BOM roll-up + bench build spec. Receipt debt C2 must be pinned
before T-D migrates to KB.

**9. X43 + C13b miss-ledger increments.** Grant-gated, unbooked (docket :271,:272,:286):
X43 → 0-for-8, C13b → 0-for-9; canonical booked = 0-for-7 (:480,:491, which itself flags
a 0-for-7-vs-0-for-8 reconciliation gap). *Question:* classify and book the increments?
*Unblocks:* the canonical booking (this PR's A7 booked 0-for-7 and noted these increments
Grant-gated in place) + the docket's own reconciliation flag. Pipeline: auditor specify →
Grant classify → implementer book.

---

## THE PROPAGATION MAP

| Result | Current home | Owed | Lane | Grant gate |
|---|---|---|---|---|
| **T1 kill #668 + Q-ladder #672** | KB identity-break-test-design.md:44-72 + index:68; RESULT + relabel + registry :807 R6-KILLED; docket :474 ★RATIFIED | NONE (two-method: no cascade-as-spectrum canon in manuscript vols); residual = optional muon cross-ref (A10) + B7 stale annotation | auditor-verified complete | none |
| **k-sweep #669 HOMOGENIZATION-SPLIT** | research RESULT only | **YES — lockstep debt**: ARC-33 fork-close (arc-map:306 stale) + homogenization-split cross-ref on translation-circuit.md:180 (srs-vertex-scattering ↔ srs-band-structure); open band-edge sub-item (k·ℓ≤0.83) | auditor structures, implementer writes | **soft** (Grant-surfaced fork wants a nod) — B9 |
| **genesis battery #670** | research RESULT; E≡1 identity in identity-break:80; ruling leaf still ★PROPOSED-RULED | Stamp flip + φ-dispersion into: ruling leaf, docket :476/:485, _orchestration/index :10/:36/:41, R10 charter :4. Plus B1 closed-box erratum | implementer executes writes | **GRANT — stamp flip PENDING** (Decision 1) |
| **F6 tier-1 #674** | research result only; manuscript refs charter-only | Auditor-lane landing list: dark-energy-latent-heat-definition.md:128+§5/:158-161, engine-capability-map.md:152-155, _orchestration/index:204; + B5 charter note + B6 identity-break:184 | auditor decides framing, implementer writes | **GRANT — framing call** (Decision 2) gates ALL |
| **identity-break leaf #671** | KB common/ + index:68 + review-workflow wiring | ✅ A8 reciprocal companion link **LANDED `47ec8f36`**; §4 F6-lever fix (B6) inherits Decision 2 | implementer | none (link done); F6-lever inherits Decision 2 |
| **cascade+PFC kill #672 R6/R7 + #673** | registry :807/:808, docket :470-491 | NONE — shelving verified clean (vol9 thesis STANDS; two-method zero cascade refs in vol9) | auditor-verified | none |
| **m_p/m_e audit card** | ✅ **LANDED `01c9a24f`** — research/2026-07-13_mp-me-mass-ratio-audit.md | Downstream hygiene items can now cite this anchor; B2/B3 leaf-side disclosures inherit Grant gates | implementer drafted | none to create |

**KB↔manuscript note (A6):** the KB bridge sites are normalized this PR; the 5 `.tex`
manuscript bridge sites (`~10^39`) are the matching manuscript-side debt (KB-leaf-first
lockstep) — enumerated in the A-ledger, deferred to a manuscript pass.

**Lane attribution:** all reconciliation lanes operated read-only in auditor lane; this
PR (implementer lane) executes only the gate-free A/C-item writes above. Every B-item and
all nine decision points remain Grant-gated / auditor-specced and are untouched here.
