# Epic: Parameter-count framing reconciliation (zero-parameter walk-back)

**Opened**: 2026-05-28 (orchestration session, Grant) — SCOPING ONLY, not greenlit for execution.
**Origin**: deep-dive audit of the `α⁻¹ = 4π³+π²+π` "Zero-Parameter Closure" flagship claim (this session). Receipts below all grep/Read-verified.
**Skill discipline applied**: `ave-walk-back` v1.2 (Step 3h-exhaustive), `verify-before-cite` v1.4 (trigger 7 temporal-currentness), `ave-evidence-framing-discipline`, `ave-directory-enumeration-discipline`, `ave-audit` (finding source).
**Classification**: Type D framing re-scope (mechanism/claim unchanged; headline framing narrowed) spanning code + KB + LaTeX. NOT a numerical-value walk-back.

> ✅ **DECISION (2026-05-28, Grant): Option 2 — "Zero-parameter, gated."** Keep the zero-parameter aspiration; make every unqualified instance explicitly conditional on the open Clifford-torus embedding-selection / spin-½ half-cover item. See §1.5 for the canonical gating clause (PENDING Grant sign-off on exact wording before propagation).

---

## §0 What the deep-dive found (verified receipts)

The corpus asserts **three mutually inconsistent parameter-count framings** at HEAD:

| # | Framing | Where (verified) |
|---|---|---|
| A | **Two inputs** (α + ℓ_node); "zero-parameter does not survive audit" | [`research/_archive/L3_electron_soliton/39_alpha_is_calibration.md`](research/_archive/L3_electron_soliton/39_alpha_is_calibration.md) (2026-04-22, archived) |
| B | **Three calibration inputs** {m_e, α, G} | `src/ave/core/constants.py:94`; `src/ave/AGENTS.md §1`; `backmatter/02_full_derivation_chain.tex` headline |
| C | **One cosmological parameter** (Ω_freeze; α & G "jointly cosmologically anchored") | `src/ave/core/constants.py:11–16` "structural closure framing" |

**Confirmed internal contradiction inside a single file** (`src/ave/core/constants.py`):
- `:94` header **"THREE CALIBRATION INPUTS"**, `:101` lists `ALPHA` as "Input 2"
- `:105` comment: *"Within the AVE framework α is **DERIVED, not input**"*
The most-imported module in the repo calls α both a calibration input and a derived quantity.

**Partial walk-back already landed (currentness-verified).** The honest reframing recommended by doc 39 (2026-04-22) **partially** propagated:
- ALREADY HONEST: [`ch8-alpha-golden-torus.md`](manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md) labels the `4π³+π²+π` match **"Class 4 observable consistency"** (not a derivation) and δ_strain **"Fitted (Class 1 identity)… not derived from substrate primitives"**; `constants.py:185` concedes δ_strain is *"definitional"*; `backmatter/02:450–454,961,972,1050` carry explicit "Honest framing" caveats ("25 of 26… one is the input scale").
- STILL OVERCLAIMS: same `backmatter/02` file titled *"From Three Limits to Zero Parameters"* (`:5`), *"derived from first principles"* (`:25`), *"closing the loop to genuinely zero parameters"* (`:37`), *"Zero-Parameter Closure"* (`:715`), *"structurally zero-parameter"* (`:785`). The headline was never demoted; caveats were bolted on underneath.

**The physics crux** (why this is a Grant decision, not a mechanical fix): the `R·r = 1/4` "spin-½ half-cover" step is where the closure rests. doc 39 §3/§6 found (a) the canonical Clifford torus is **not** the ropelength minimum for the (2,3) knot, and (b) the half-cover identification is *"equivalent to the SU(2) projective-ray postulate"* — i.e. not K4-native. The **current** `ch8` leaf disputes this, claiming the half-cover IS substrate-derived via the K4→A4→2T⊂SU(2)→SO(3) chain (Class 2), while its own "Remaining open formal-rigor sub-item" concedes the load-bearing embedding-selection step is unproven. **Whether α is genuinely substrate-predicted or a calibration input is an open physics question the corpus answers both ways.**

---

## §1 The gating decision (Grant)

Pick the canonical position; everything downstream follows:

- **Option 1 — "One-parameter, honest"** (doc-39 position): α is a calibration input; the Golden-Torus `4π³+π²+π` is a Class-4 geometric *consistency check*, not a derivation. Headline becomes "19→1 (or →2 w/ scale) parameter reduction." Walk-back demotes all "zero-parameter / derived from first principles" headline framing. **Largest propagation, most defensible externally.**
- **Option 2 — "Zero-parameter, gated"**: keep the zero-parameter aspiration but make every instance explicitly *conditional* on the open half-cover/embedding item (the `ch8` leaf's current Class-2 claim). Walk-back adds gating language + the open-item pointer wherever "zero-parameter" appears unqualified. **Medium propagation; preserves the ambition honestly.**
- **Option 3 — Reconcile to the "one cosmological parameter" (Ω_freeze) framing C** as canonical, with A/B as derived corollaries. **Requires the Ω_freeze→u_0*→α chain to be solid — which rests on the same unproven half-cover step; likely premature.**

**Independent of the choice**, two fixes are unconditional must-dos:
1. Kill the `constants.py` internal contradiction (`:94/:101` vs `:105`).
2. Collapse the three coexisting framings (A/B/C) to one stated consistently.

## §1.5 Canonical gating clause (Option 2)

The walk-back propagates ONE clause, in two registers. This is the load-bearing artifact.

### Phase 1 (drafted) — used for headline anchors already stamped

**Long form** (once per headline doc — backmatter §, ch1, ch8 leaf, foreword if present):
> AVE's zero-parameter closure is **contingent on one open formal step**: that ropelength-minimality uniquely selects the canonical Clifford-torus embedding fixing R·r = 1/4 (the spin-½ half-cover). This step is *conjectured* substrate-derived via the K4 → 2T ⊂ SU(2) → SO(3) chain but is **not yet proven from the classical axioms alone**. Until it is closed, α functions as the framework's one calibration input and the α⁻¹ = 4π³+π²+π match is a Class-4 geometric *consistency check*, not a completed first-principles derivation.

**Short form** (inline, at every unqualified "zero-parameter" headline hit):
> (contingent on the open Clifford-torus embedding-selection item — see [`ch8-alpha-golden-torus.md`](manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md) §"Remaining open formal-rigor sub-item")

### Phase 2 (SHARPENED — Grant 2026-05-28) — apply to NEW STALE-PROSE fixes only

Sharpens the half-cover-vs-embedding-selection distinction (Phase 1 clause conflates them; ch8 merge resolution preserved the distinction). Do NOT rewrite Phase-1-gated blocks unless grep shows they regressed.

**Long form** (new/edited headline sites):
> AVE's zero-parameter closure is contingent on one open formal step: that ropelength-minimality on K4 uniquely selects the canonical Clifford-torus embedding $r_1 = r_2 = 1/\sqrt{2}$ fixing $R \cdot r = 1/4$. The spin-½ half-cover itself is treated as substrate-derived via the K4 → 2T ⊂ SU(2) → SO(3) chain (see ch8 steps 1–4); the unproven piece is embedding-selection, not the half-cover postulate in isolation. Until embedding-selection is closed from the classical axioms alone, α is operationally the one calibration input and $4\pi^3 + \pi^2 + \pi$ is a Class-4 consistency check.

**Short form** (inline STALE-PROSE hits):
> (zero-parameter contingent on the open embedding-selection item — not the half-cover chain; see `ch8-alpha-golden-torus.md` §"Remaining open formal-rigor sub-item (THE gating item)")

**`constants.py` reconciliation under Option 2** (`:94/:101/:105`):
- Retitle `:94` block from "THREE CALIBRATION INPUTS" → "ONE SCALE + GATED CONSTANTS (zero-parameter contingent on open embedding item)".
- `:105` change "α is DERIVED, not input" → "α is *conjectured*-derived (gated on the open Clifford-torus embedding item); operationally the one calibration input until that step is closed."
- Keep framing C (`:11–16`) but mark Ω_freeze→α as resting on the SAME open step (no independent closure).

---

## §2 Step 3h-exhaustive methodology (for execution)

**3h-1 — pattern list** (forms the walked-back headline takes):
- `zero[- ]free[- ]parameter`, `zero[- ]parameter`, `Zero-Parameter Closure`, `Zero-Parameter Universe`
- `derived from first principles`, `genuinely zero`, `structurally zero-parameter`, `closing the loop`
- `THREE CALIBRATION INPUTS` / `three calibration inputs`, `α is DERIVED`, `is derived, not input`
- `26 / 26 derived`, `26/26`
- competing-honest forms (to locate already-done sites): `one-parameter`, `calibration input`, `Class 4 observable consistency`, `fitted`, `back-substituted`, `definitional`
- framing-C forms: `structural closure`, `one cosmological`, `Ω_freeze`, `jointly cosmologically anchored`

**3h-2 — grep scope**: `manuscript/ave-kb/` (canonical, FIRST), then `manuscript/vol_*` + `backmatter/` + `frontmatter/` (derived LaTeX), then `src/ave/` + `src/scripts/` (code/docstrings), then `research/` + `_orchestration/` (mostly Q1/Q2).

**3h-3 — Q1/Q2 + sense classification** (the critical triage; ~130 raw hits, most NOT load-bearing):
- **SENSE-2 LEGITIMATE (no change)**: "this solver/derivation uses zero free parameters" = no fitting knobs in *that* calculation. Defensible and distinct from the global headline. Pervasive in solver-toolchain / falsification chapters. Do NOT touch.
- **LOAD-BEARING (must fix)**: global-headline claims that all constants are derived / framework is zero-parameter without gating. The enumerated anchors in §3.
- **STALE-PROSE (fix)**: narrative repeating the headline overclaim.
- **PRESERVED-HISTORICAL Q1 (no change)**: `research/_archive/**`, doc 39 itself — audit trail.
- **FROZEN-SNAPSHOT Q2 (no change)**: `_orchestration/*handoff*`, preregs, session docs.

**3h-4 — gap inventory** + **3h-5 — post-cleanup sweep** with the same pattern list (per skill).

**Canonicality order** (per `src/ave/AGENTS.md §0`): KB leaf FIRST → then LaTeX mirror → then code docstrings. KB is canonical; LaTeX is a derived artifact.

---

## §3 Verified load-bearing anchor inventory (the must-fix core, decision-dependent)

| Site | Current state | Action (Opt 1 / Opt 2) |
|---|---|---|
| `src/ave/core/constants.py:94,101,105` | self-contradiction (input vs derived) | reconcile wording — UNCONDITIONAL |
| `src/ave/core/constants.py:11–16` | framing C asserted as "current" | align to chosen canonical framing |
| `src/ave/AGENTS.md §1` | "derive ALL constants from {M_E,ALPHA,G}" | align (α-as-input is consistent w/ this) |
| `backmatter/02_full_derivation_chain.tex:5,25,37,715,724,785` | headline overclaim | demote → "one-parameter" / add gating |
| `backmatter/02` `:450–454,961,972,1050` | already-honest caveats | promote to primary framing |
| `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md` | mostly honest (Class 4) but titled "Zero-Parameter Closure" | retitle / gate |
| `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md` | leaf name + content | rename/gate per doc 39 §5.3 |
| `manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex` | "Pathway to Zero-Parameter Universe" | rename per doc 39 §5.3 |
| `manuscript/ave-kb/common/full-derivation-chain.md` | Layer 7→8 closure | mirror backmatter |
| `manuscript/frontmatter/00_foreword.tex` | shared across all vols — check headline | gate if present |

(Anchor list is the *headline* set, not the full propagation graph; STALE-PROSE sites enumerate at execution time via 3h-2 grep.)

---

## §4 Execution recommendation

- **Do NOT bundle with the Vol 9 formatting epic** — different risk class (touches load-bearing physics framing + the most-imported module).
- Branch off `main`; KB-first then LaTeX then code.
- **Fire `ave-sweep-audit` PRE-merge** (the skill's own Phase 3-A4 lesson: pre-merge sweep turns a 3-PR cleanup into 1 PR; 5× miss-rate otherwise).
- Bidirectional closure-roadmap §0.5 changelog entry (3l) + supersede the original "Layer 8 closure" canonization entry in place.
- This is plausibly 2 sessions: (1) constants.py contradiction + framing reconciliation + backmatter/ch1/ch8 headline anchors; (2) corpus-wide 3h-exhaustive STALE-PROSE sweep + sweep-audit.

## Status
- [x] **GATING: Grant picked Option 2 — "Zero-parameter, gated"** (2026-05-28)
- [x] **Phase 1 MERGED** (2026-05-28) — `--no-ff` merge `f6b22757`; audit tag `audit/2026-05-28_parameter-count-gating-phase1` → `9b4ae922`
- [x] **Phase 2 MERGED** (2026-05-28 EOD++) — `--no-ff` merge `7e814523`; audit tag `audit/2026-05-28_parameter-count-gating-phase2` → `2c0ce429`; sweep-audit (agent `aef0a741`) PASS-WITH-FINDINGS → amendment `2c0ce429` resolved D1+B1+B2+C1; one C-class follow-up deferred (see "Deferred" block below)
- [x] ~~**Epic CLOSED** (2026-05-28 EOD++)~~ → **REOPENED 2026-05-31**: see §Phase 3 below
- [ ] **Phase 3 SCOPING** (2026-05-31) — coordinate-system walk-back: Phase 1+2 gating clause is in spatial-ropelength language; corpus retired that framing 2026-04-27/28 in favor of phase-space (V_inc, V_ref). PENDING Grant adjudication of replacement framing (a)/(b)/(c) — see §Phase 3 §"Framing decision required"

---

## Wrap-up handoff (2026-05-28 EOD)

**For:** next orchestration or implementor session picking up parameter-count framing.  
**Branch:** `analysis/integration` @ `435e8797` (or later). **Do not merge to `main`** until Grant greenlights integration→main (repo convention).

### Session arc (what happened)

1. Deep-dive on α / zero-parameter claims → scoped walk-back epic (Option 2).
2. **Phase 1** implementor landed + merged (headline anchors, `constants.py`, closure-roadmap §0.5).
3. **Vol 9 LaTeX formatting** implementor landed + merged in parallel (`a9ab377f`; audit tag → `3ca379fe`). Note: that merge brought **~155 commits** of prior integration work, not only 5 formatting commits — verify `git log 59c016e2..a9ab377f` if auditing scope.
4. **Phase 2** spawn **failed** (API limit) — corpus propagation **not** done.

### What is done (safe to treat as landed)

| Deliverable | Evidence |
|---|---|
| Option 2 decision recorded | This doc §1 |
| `constants.py` contradiction reconciled | Merge `f6b22757`; grep `ONE SCALE + GATED CONSTANTS`, `GATING NOTE (2026-05-28)` |
| KB/LaTeX headline gating (8 files) | Phase 1 commit `9b4ae922` + ch8 merge resolution on `integration` |
| closure-roadmap §0.5 bidirectional entry | `claim-quality-closure-roadmap.md` (path is **`claim-quality-closure-roadmap.md`**, NOT `common/closure-roadmap.md`) |
| Vol 9 formatting + margin gate 350→45pt | Merge `a9ab377f`; subagent verified 8/8 volumes ≤45pt in clean worktree |

**Gating markers currently in corpus (grep snapshot @ `435e8797`):** only **~9 files** contain `Gating note (2026-05-28)` / `contingent on the open Clifford` — while **~130+ manuscript files** still mention `zero-parameter` / `zero free parameter` (many are SENSE-2 legitimate; many are STALE-PROSE). **Phase 2 is required before calling propagation complete.**

### What is NOT done (load-bearing)

1. **Phase 2 — Step 3h-exhaustive STALE-PROSE sweep** (§2 methodology). Mandatory fixes called out in Phase 1 report:
   - `src/ave/AGENTS.md` §1 — still reads *"derive ALL physical constants from three calibration inputs (M_E, ALPHA, G)"* without gating / operational-α language.
   - Broken `\kbleaf{closure-roadmap.md}` in at least `vol_3_macroscopic/chapters/05_cosmology_dark_sector.tex` — should point to `claim-quality-closure-roadmap.md` (mechanical).
   - `vol*/claim-quality.md`, `mathematical-closure.md`, `zero-parameter-derivations.md`, driver docstrings, vol chapters not in Phase-1 set — triage per SENSE-2 vs STALE-PROSE.
2. **`ave-sweep-audit` pre-merge** on Phase 2 branch (skill lesson: 5× miss-rate without it).
3. **§1.5 wording sign-off** — Phase 1 used the drafted clause; Grant may want to sharpen ch8 *half-cover resolved vs embedding-selection open* distinction corpus-wide (implementor preserved it in ch8 merge).
4. **Optional:** retitle `"Zero-Parameter Closure"` headings vs gate-under-title only (Grant preference from Phase 1 report).

### Parallel work: PDF build (`make clean && make all`)

Grant running local full build. Known environmental gaps (pre-existing, not from formatting pass):

- `vol_2`: `electron_3d_knot.png` missing in clean checkout
- `vol_5`: `amino_acid_resonance.png` missing

**When build completes:** confirm margin gate passes (45pt) on all volumes; note any new overfulls from siunitx reflow.

### Phase 2 implementor brief (PENDING — copy to next session)

```
Branch: analysis/parameter-count-gating-phase2 off analysis/integration
Worktree: ../AVE-Core-paramgating-p2 (isolated)

Read: _orchestration/2026-05-28_parameter-count-framing-walkback.md §1.5 + §2

Deliverables:
1. Step 3h-exhaustive grep → classify (SENSE-2 / STALE-PROSE / Q1 / Q2)
2. Fix STALE-PROSE + LOAD-BEARING global headlines (KB first → LaTeX → src)
3. Mandatory: src/ave/AGENTS.md §1; closure-roadmap.md link fixes
4. Post-cleanup re-grep + gap inventory table in report
5. make refresh-kb-metadata && verify-kb-metadata && verify-md-links
6. Push branch; do NOT merge

Skills: ave-walk-back 3h-exhaustive, verify-before-cite, ave-evidence-framing-discipline
After push: orchestration runs ave-sweep-audit (or spawn) THEN audit-tag + --no-ff merge
```

### Recommended wrap-up order (next session)

| Step | Owner | Action |
|---|---|---|
| 1 | Grant / local | Let `make all` finish; capture pass/fail + missing figures |
| 2 | Implementor | Execute Phase 2 brief above (~1 session; KB-heavy) |
| 3 | Orchestration | `ave-sweep-audit` on Phase 2 diff **before** merge |
| 4 | Orchestration | `--no-ff` merge + `audit/2026-05-28_parameter-count-gating-phase2` tag + branch delete |
| 5 | Orchestration | Mark epic CLOSED in this doc; add one-line to `_orchestration/index.md` reconciliation |
| 6 | Grant (optional) | Decide title retitle vs gate-under-title; decide if integration→`main` is ready |

### Audit / merge reference (already landed)

| Workstream | Merge commit | Audit tag → tip |
|---|---|---|
| Vol 9 formatting | `a9ab377f` | `audit/2026-05-28_vol9-corpus-latex-formatting` → `3ca379fe` |
| Param-gating Phase 1 | `f6b22757` | `audit/2026-05-28_parameter-count-gating-phase1` → `9b4ae922` |
| Param-gating Phase 2 | `7e814523` | `audit/2026-05-28_parameter-count-gating-phase2` → `2c0ce429` |

### Physics note for external readers (unchanged crux)

The corpus **gates** zero-parameter on the **embedding-selection** open item while treating the **spinor half-cover** as substrate-derived (ch8 Class 2). Doc 39 (archive) disagrees on half-cover nativeness — that tension is **intentionally preserved** under Option 2, not resolved in this epic.

---

## CLOSED — Phase 2 outcome (2026-05-28 EOD++)

**Merge**: `7e814523` (`--no-ff` of `analysis/parameter-count-gating-phase2` → `analysis/integration`).
**Audit tag**: `audit/2026-05-28_parameter-count-gating-phase2` → `2c0ce429` (annotated tag obj `c1c4d383`); pushed to origin; branch deleted on origin.
**Files in merge**: 22 (incl. amendment) — see merge commit body for class breakdown.

### Sweep-audit cycle that produced the merge

1. Implementor (`ac6e8e8a`) — 4 commits (`508916da..dd3de8e8`), 18 files. Self-reported PASS with one observation (`src/scripts/` driver docstrings classified SENSE-2 LEGITIMATE per brief carve-out).
2. Sweep-audit (`aef0a741`) — PASS-WITH-FINDINGS: 1 Class D + 2 Class B + 2 Class C. `make verify-kb-metadata` PASS; `make verify-md-links` 0 gating errors. Recommended MERGE WITH FOLLOWUP COMMIT.
3. Amendment implementor (`ac15e60d`) — `2c0ce429`, +6 files:
   - **D1** `\label{sec:open_rigor}` added at `08_alpha_golden_torus.tex:119` (option-a target paragraph)
   - **B1** `vol2/index.md:14`, `vol5/index.md:14`, **`vol6/index.md:18`** (autonomous-scan addition with per-nucleus-fitted-R disclosure pointer) — sharpened short-form gating
   - **B2** `src/scripts/AGENTS.md §"The Zero-Free-Parameters Constraint"` reconciled (ASCII GATING NOTE mirroring chunk 1)
   - **C1** `src/ave/AGENTS.md` numeric line cites (`:94/:101/:105`) replaced with anchor language (`§ONE SCALE + GATED CONSTANTS header / ALPHA declaration / NOTE ON α block`)
   - autonomous-scan negative results: `vol3/index.md`, `vol4/index.md`, `vol9/index.md` — no equivalent headline claim, LEFT ALONE; `vol7/index.md`, `vol8/index.md` — files do not exist
4. Spot-check (orchestration, not full re-audit) — amendment diff verified clean: D1 label/ref pair resolves, B1 gating clauses present with sharpened wording, B2 mirror reads correctly, C1 anchor language verified against current `constants.py:105-138` state.

### Deferred (post-epic-close, scoped follow-up) — RESOLVED

- ~~**C2** — `src/ave/ARCHITECTURE_REVIEW.md:12`~~ **RESOLVED** via commit `c81aea0e` (2026-05-29): option (a) chosen — added a "Framing note" block between title and Critical Issues that marks the doc as audit-snapshot historical-record, points to current canonical gated framing (`src/ave/AGENTS.md §1`, `src/ave/core/constants.py §ONE SCALE + GATED CONSTANTS header`, vol1/ch8 open formal-rigor sub-item), and preserves body verbatim per Rule 12.

### Open Grant decisions (carried forward — NOT blocking; epic CLOSED)

1. **Title retitle vs gate-under-title**: e.g. `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md` retains its title under gate-language; should it be renamed (e.g. `zero-parameter-aspiration-gated.md`)? Phase 1 wrap-up flagged; Phase 2 left as-is (gate-under-title chosen by default). Grant to confirm or override.
2. **integration → main**: `analysis/integration` now contains 4 epic merges since the last main checkpoint (Path B-prime, Vol 9 buildout, Vol 9 formatting, param-gating Phase 1+2) + multiple smaller PRs. Per branching convention `main` stays frozen until Grant greenlights. Grant call on timing.

### What's recorded vs. what's NOT in this doc

- This doc is the canonical record for the param-count framing walk-back epic — Status block + merge table + this CLOSED section are load-bearing.
- The implementor + auditor full reports live in their respective agent transcripts (one-off, not persisted in the repo). Diff is fully reconstructable from the 5 commits + the audit tags.
- The sharpened §1.5 clause (canonical Phase 2 wording) is recorded in §1.5 with the Phase 1 draft preserved alongside for historical audit.

---

## Phase 3 — coordinate-system walk-back (2026-05-31)

**Opened**: 2026-05-31 (orchestration session, Grant) — re-opens this epic.
**Branch**: `analysis/q-embed-sel-1-investigation` off `main`.
**Skills fired this session**: `ave-prereg` (corpus-grep Step 2 dispatched), `pre-test-physics-check` (plumber question surfaced + Grant adjudicated), `verify-before-cite` (every cite below grep-confirmed), `phase-space-coordinate-check` (the missing skill in Phase 1+2 — now in scope), `ave-walk-back` (Step 3h-exhaustive in REVERSE).

### §3.0 Why reopening — the corpus context Phase 1 missed

The Phase 1 walkback scoping (§0 above) cited doc 39 as the dissenting voice but missed three load-bearing docs in the **same** `research/_archive/L3_electron_soliton/` directory PLUS a cross-repo bracketing in AVE-HOPF. Verified receipts (`verify-before-cite` 2026-05-31):

| Doc | What it says | Status when Phase 1 ran |
|---|---|---|
| [`38_ropelength_minimality.md`](research/_archive/L3_electron_soliton/38_ropelength_minimality.md) §2 | Direct numerical refutation. Canonical Clifford ($r_1 = r_2 = 1/\sqrt{2}$) ropelength = **26**; actual minimum at asymmetric $(0.75, 0.66)$ ropelength = **24**. Ch 8's Golden Torus maps to $(r_1 \approx 0.966, r_2 \approx 0.258)$ ropelength ≈ **50**, far from any minimum. | Already in archive. Not cited in Phase 1 walkback §0. |
| [`29_ch8_audit.md`](research/_archive/L3_electron_soliton/29_ch8_audit.md) F4–F9 + §2.4 | Explicit audit of ch8 with 6 structural problems. §2.4 verbatim: *"the minimum ropelength of the trefoil 3₁ in ℝ³ is ≈ 16.37... The Golden Torus as Ch 8 presents it has a trefoil of ropelength much smaller than that — **sub-ropelength, which is impossible for an embedded trefoil with unit-tube thickness**... If Ch 8 is genuinely making a real-space claim, it's falsified by elementary ropelength geometry. The phase-space reading is the only one that survives."* | Already in archive. Not cited in Phase 1 walkback §0. |
| [`28_two_node_electron_synthesis.md`](research/_archive/L3_electron_soliton/28_two_node_electron_synthesis.md) §5 | Phase-space reinterpretation: **R, r are (V_inc, V_ref) phasor coordinates, NOT spatial tube radii**. Same Ch 8 algebra reinterpreted. Path α v1 test ran 2026-04-27 commit `466d8c4` and **FAILED** (C1 R/r=3.84 vs target φ²=2.62 FAIL; C2 chirality 50% TIE FAIL) with 4 A59 methodology gaps surfaced. | Already in archive. Not cited in Phase 1 walkback §0. |
| [`AVE-HOPF/docs/glossary.md:32`](../../AVE-HOPF/docs/glossary.md) | *"Golden Torus / S₁₁-min — **Bracketed by Grant 2026-04-30** as a 'post-IP-separation patch-attempt.' Cite as bracketed-pending audit, NOT as the canonical parameter-free derivation."* | Already in sibling repo. Cross-repo inconsistency: Phase 1 stamped same claim as canonical anchor in AVE-Core 2026-05-28. |
| [VACUUM_ENGINE_MANUAL.md:3713](research/_archive/L3_electron_soliton/VACUUM_ENGINE_MANUAL.md) (Grant 2026-04-27 adjudication) | *"doc 28 §5.4 + doc 29 §3.2-§3.3 already canonized **R, r as PHASE-SPACE radii of (V_inc, V_ref) phasor on Clifford torus, NOT spatial bond-extent**."* | Already in archive. Phase 1 scoping did not cite this adjudication. |

**Net**: the corpus's own audit position (4+ weeks before Phase 1) is that the spatial-coordinate reading of $(R, r, \text{Clifford-torus embedding})$ is falsified; phase-space is the surviving reading. The Phase 1 gating clause was stamped in the falsified coordinate system. Phase 2 propagated that clause to ~30 sites corpus-wide.

### §3.1 Provenance of the spatial-ropelength gating clause

Traced via `git log -S 'ropelength-minimality uniquely selects'`:

1. **PR #36** (2026-05-26) + commit `ea798788` (Phase 3-A1 reframe) — **upstream cementing event**. Strengthened ch8's three-regime framing (Nyquist / Crossings / Screening half-cover) to "Class 2 axiom-manifestation" on the substrate-mechanism axis. Did NOT introduce the gating-clause wording; cemented the substrate-derivation claim that the gating clause sits on top of.
2. **Commit `a48b2cf0`** (2026-05-28) — walkback scoping; introduced the spatial-ropelength language in the §0 audit summary citing doc 39 as the corpus dissent.
3. **Commit `9b4ae922`** (2026-05-28, Phase 1 implementor; merged in `f6b22757`; **NO GitHub PR**) — first STAMP of the spatial-ropelength gating clause at headline anchors.
4. **Commits `508916da..2c0ce429`** (2026-05-28 EOD, Phase 2 + amendment; merged in `7e814523`; **NO GitHub PR**) — propagated corpus-wide.

### §3.2 Skills that should have fired but didn't

| Skill | Trigger that matched at Phase 1 scoping | What it would have caught |
|---|---|---|
| `ave-prereg` | The gating clause IS a new physics claim about what's settled vs open (not just re-scope). Trigger 5 (new structural argument) + Trigger 6 (audit-fix-applied-to-canonical-content) both match. | Docs 28/29/38 surfaced immediately on Step 2 corpus-grep dispatch (confirmed in this session). |
| `phase-space-coordinate-check` | Corpus claim describes R, r in phase-space (V_inc, V_ref) coordinates per Grant 2026-04-27 adjudication. Phase 1 was stamping a derivation framing on a phase-space claim using real-space-ropelength language. | Coordinate-system mismatch at scoping time, before any stamping. |
| `verify-before-cite` v1.4 Trigger 7 | Doc 39's claim "canonical Clifford is not the ropelength minimum" was directly numerically verified by doc 38 in the same archive directory. Phase 1 cited the assertion without finding its corpus-verification. | The "verified receipts" in §0 weren't actually verified across the archive. |

**Procedural gap** (not substantive): the skills weren't broken — the discipline was. Phase 1 was framed as "Type D framing re-scope" which the implementor's reading didn't match against the "new claim / new structural argument" triggers in `ave-prereg`. The walkback scoping treated docs 28/29/38's content as "existing corpus" rather than "corpus state that needs full enumeration before stamping."

### §3.3 Framing decision required (PENDING Grant)

The walk-back needs ONE replacement framing for the gating clause. Three live options:

#### Option (a) — Phase-space framing (recommended)

> AVE's zero-parameter closure is contingent on one open formal step in **phase-space coordinates**: that the (V_inc, V_ref) phasor on the Clifford torus uniquely realizes $R/r = \varphi^2$ at the substrate eigenmode. The spatial-coordinate reading of ropelength-minimality on the canonical Clifford embedding is **not** the load-bearing claim — that reading was retired by doc 29 (ch8 audit) which found the spatial Golden Torus is **sub-ropelength** for the (2,3) trefoil and concluded "the phase-space reading is the only one that survives." The phase-space test (Path α v1, commit `466d8c4`, 2026-04-27) **FAILED** (C1 R/r=3.84 vs target φ²=2.62; C2 chirality 50% TIE) with 4 A59 methodology gaps surfaced. The open formal step is either (i) re-run Path α (v2) with the A59 fixes, or (ii) analytical derivation that the (V_inc, V_ref) phasor on the Clifford torus uniquely has $R/r = \varphi^2$. Until one of these closes, α functions as the framework's one calibration input.

**Scope**: walk back ~30 gating-clause sites + add new phase-space-coordinate language + cite docs 28/29/38 in walkback §0 + reconcile AVE-HOPF position. New empirical sub-epic: Path α v2 prereg with A59 methodology fixes.

**Tradeoff**: preserves the zero-parameter aspiration honestly while gating on a concrete falsifiable next step. If Path α v2 also FAILS or the analytical proof doesn't close, the framework drops back to (b).

#### Option (b) — Doc-39 calibration-input framing

> α is one calibration input. The framework's parameter count is **one-parameter, honest** — α + the substrate Nyquist scale $\ell_{\text{node}}$ (collapsed to one via the unknot ground state). The $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$ match is a **Class-4 geometric consistency check**, not a derivation. The corpus's prior "zero-parameter" headline framing was an aspiration that the spatial-coordinate derivation chain failed to support (doc 38 numerical refutation; doc 29 audit; AVE-HOPF Grant bracketing 2026-04-30). Future closure of α from substrate axioms alone is an open framework-extension question, but the current canonical position is one-parameter.

**Scope**: walk back ~30 gating-clause sites + retire "zero-parameter" headline wherever it appears unqualified + retitle relevant sections (e.g., `zero-parameter-universe.md` → `one-parameter-honest.md`) + cross-repo: ratify AVE-HOPF Grant 2026-04-30 bracketing position. The title-retitle pass you flagged earlier becomes part of THIS walk-back.

**Tradeoff**: largest propagation but most defensible externally. Matches BOTH the AVE-HOPF Grant 2026-04-30 bracketing AND doc 39's audit position. Loses the aspiration but doesn't preclude future re-derivation if a phase-space proof ever lands.

#### Option (c) — Multi-path framing

> The framework's parameter-count is currently in **open adjudication** between two live corpus positions: (a) one-parameter with phase-space derivation of α as the open formal step (Path α v2 / analytical phase-space proof), and (b) one-parameter calibration-input position with α as a calibration scale. Both are honest readings of the corpus; the deeper close-out (which framing is right) is itself the open work.

**Scope**: walk back ~30 gating-clause sites + add multi-path gating language acknowledging both (a) and (b) as live + extensive cross-references between the two positions in the corpus + cross-repo: same as option (b).

**Tradeoff**: most honest, most awkward to propagate. Hard for external readers to parse. Useful as a temporary position if you want to delay the (a) vs (b) call until Path α v2 either passes or fails.

### §3.4 Recommendation

**Option (a) — phase-space framing.**

Reasoning:
1. **Faithful to corpus**: doc 29 explicitly says phase-space is "the only surviving reading." Option (a) ratifies that audit position rather than overriding it.
2. **Concrete falsifiable next step**: Path α v1 has 4 A59 methodology gaps documented; v2 is a tractable empirical sub-epic with a clear go/no-go.
3. **Preserves aspiration honestly**: option (b) is the fallback IF (a) fails; starting at (a) gives the framework a chance.
4. **Single coordinate system in the gating clause**: option (c) maintains two simultaneous framings corpus-wide, which is the same multi-framing problem Phase 1 was trying to solve in the first place.
5. **AVE-HOPF reconciliation**: under (a), the AVE-HOPF "bracketing" gets restated as "bracketed pending phase-space derivation v2" — still bracketed, but with a concrete close-out path. Under (b), the bracketing gets ratified as the canonical position. Under (c), the bracketing becomes ambiguous.

### §3.5 Implementor brief (PENDING Grant framing call)

```
Branch: analysis/q-embed-sel-1-investigation (already created)
Worktree: ../AVE-Core-q-embed-sel-1 (isolated)

Read: _orchestration/2026-05-28_parameter-count-framing-walkback.md §Phase 3 + §1.5 + §3 anchor inventory

Deliverables (under Option <a/b/c>):
1. Step 3h-exhaustive grep in REVERSE: identify all 30+ Phase-1+2-stamped sites; un-stamp; restamp with new framing
2. §0 walkback-doc audit-receipts update: cite docs 28/29/38 + AVE-HOPF glossary:32 + 2026-04-27 Grant adjudication
3. §1.5 new gating clause text (long-form + short-form per option chosen)
4. ch8 KB leaf: rewrite §"Remaining open formal-rigor sub-item" to phase-space framing (option a) OR retire the section (option b)
5. AVE-HOPF cross-repo reconciliation: open issue or PR in sibling repo updating glossary:32 to match new AVE-Core position
6. Run make refresh-kb-metadata && verify-kb-metadata && verify-md-links; fix any failures
7. PR-routed merge per memory v2: gh pr create --base main --head analysis/q-embed-sel-1-investigation --draft → review → merge

Skills: ave-walk-back 3h-exhaustive, verify-before-cite, ave-evidence-framing-discipline, phase-space-coordinate-check, ave-discipline-translate, consistency-vs-emergence

After push: orchestration runs ave-sweep-audit on diff THEN gh pr ready → merge via gh pr merge --squash (or --merge per coworker preference)
```

### §3.6 Phase 3 status

- [x] **§3.0 corpus-context audit complete** (this session) — docs 28/29/38/AVE-HOPF glossary:32 cited
- [x] **§3.1 provenance traced** (this session) — Phase 1 commit `9b4ae922`; no GitHub PR for either phase
- [x] **§3.2 skill-gap diagnosis complete** (this session) — `ave-prereg` + `phase-space-coordinate-check` + `verify-before-cite` Trigger 7 didn't fire at Phase 1 scoping
- [x] **§3.3 framing decision DEFERRED to downstream evaluation** (Grant 2026-05-31) — *"I don't want to reframe, I want to actually run out what's needed to evaluate/check for path a, what is left for us to model/simulate/derive."* Framing-choice adjudication waits on the concrete evaluation result. The evaluation epic is now scoped at [`2026-05-31_q-embed-sel-1-evaluation.md`](2026-05-31_q-embed-sel-1-evaluation.md)
- [ ] **Q-EMBED-SEL-1 evaluation epic** (downstream; resolves §3.3 by Phase 1+2 outcome) — see [`2026-05-31_q-embed-sel-1-evaluation.md`](2026-05-31_q-embed-sel-1-evaluation.md) §1
- [ ] **§3.5 implementor execution** — superseded by evaluation epic Phase 0 (C1/C2 fix) + Phase 1 (Path α v2-phasor) + Phase 2 (analytical) + Phase 3 (cross-repo)
- [ ] **Sweep-audit + PR-routed merge** — happens per-phase in evaluation epic
- [ ] **AVE-HOPF cross-repo reconciliation** — evaluation epic Phase 3, gated on Phase 1+2 outcomes
