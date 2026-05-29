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
- [x] **Epic CLOSED** (2026-05-28 EOD++)

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

### Deferred (post-epic-close, scoped follow-up)

- **C2** — `src/ave/ARCHITECTURE_REVIEW.md:12` reads "The framework claims three calibration inputs (M_E, ALPHA, G)" unguarded. Auditor judgment: Q1-historical-adjacent (audit-snapshot doc, not in `_archive/`). Two options for follow-up: (a) add header note "Audit snapshot dated 2026-XX-XX; framework-headline framing changed 2026-05-28 — see `src/ave/AGENTS.md §1`"; (b) leave as-is per Rule 12 body-preserve. **No code/manuscript correctness impact.** Pick up in next architectural-doc pass.

### Open Grant decisions (carried forward — NOT blocking; epic CLOSED)

1. **Title retitle vs gate-under-title**: e.g. `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md` retains its title under gate-language; should it be renamed (e.g. `zero-parameter-aspiration-gated.md`)? Phase 1 wrap-up flagged; Phase 2 left as-is (gate-under-title chosen by default). Grant to confirm or override.
2. **integration → main**: `analysis/integration` now contains 4 epic merges since the last main checkpoint (Path B-prime, Vol 9 buildout, Vol 9 formatting, param-gating Phase 1+2) + multiple smaller PRs. Per branching convention `main` stays frozen until Grant greenlights. Grant call on timing.

### What's recorded vs. what's NOT in this doc

- This doc is the canonical record for the param-count framing walk-back epic — Status block + merge table + this CLOSED section are load-bearing.
- The implementor + auditor full reports live in their respective agent transcripts (one-off, not persisted in the repo). Diff is fully reconstructable from the 5 commits + the audit tags.
- The sharpened §1.5 clause (canonical Phase 2 wording) is recorded in §1.5 with the Phase 1 draft preserved alongside for historical audit.
