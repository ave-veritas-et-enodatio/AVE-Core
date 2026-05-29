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

## §1.5 Canonical gating clause (Option 2) — PENDING Grant sign-off

The walk-back propagates ONE clause, in two registers. This is the load-bearing artifact; lock the wording before stamping ~130 sites.

**Long form** (once per headline doc — backmatter §, ch1, ch8 leaf, foreword if present):
> AVE's zero-parameter closure is **contingent on one open formal step**: that ropelength-minimality uniquely selects the canonical Clifford-torus embedding fixing R·r = 1/4 (the spin-½ half-cover). This step is *conjectured* substrate-derived via the K4 → 2T ⊂ SU(2) → SO(3) chain but is **not yet proven from the classical axioms alone**. Until it is closed, α functions as the framework's one calibration input and the α⁻¹ = 4π³+π²+π match is a Class-4 geometric *consistency check*, not a completed first-principles derivation.

**Short form** (inline, at every unqualified "zero-parameter" headline hit):
> (contingent on the open Clifford-torus embedding-selection item — see [`ch8-alpha-golden-torus.md`](manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md) §"Remaining open formal-rigor sub-item")

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
- [x] **Phase 1 MERGED** (2026-05-28) — `--no-ff` merge `f6b22757` on `analysis/integration`; audit tag `audit/2026-05-28_parameter-count-gating-phase1` → `9b4ae922`. ch8 conflict resolved: Phase 3-A4 table + Op21-closed preserved; embedding-selection gating integrated.
- [ ] Phase 2 — corpus-wide 3h-exhaustive STALE-PROSE sweep + **ave-sweep-audit pre-merge** (required before declaring propagation complete)
