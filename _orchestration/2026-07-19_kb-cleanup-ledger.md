# KB Documentation Cleanup Ledger — 2026-07-19

**Lane:** KB documentation cleanup (implementer). **Scope:** `manuscript/ave-kb/` ONLY (the knowledge base). A sibling lane cleans the manuscript tex volumes (`manuscript/vol_0..vol_9`) — this lane does NOT touch anything outside `manuscript/ave-kb/` except this ledger.

**Branch:** `docs/kb-cleanup-2026-07-19` (worktree off `origin/main` @ `1be045a1`, PR #735 merged).

**Window swept:** 2026-07-01 → 2026-07-19 (the last full honesty-lag sweep was 2026-07-01; this covers the 07-01→07-19 propagation window plus mechanical hygiene).

---

## Method

- **Two-method verify-before-cite on every finding:** grep (content pattern) + Read (context). Never arithmetic line offsets. Any load-bearing zero-hit re-checked with a second method (markdown `**` and `$..$` patterns silently false-negative in grep — use `-F` fixed-string and word-fragment cross-checks).
- **Rule-12 preservation:** no deletions of claims/status. Corrections are dated notes/banners preserving old text verbatim. KEEP-BOTH: frozen rows/axes never redefined in place.
- **Pure-corpus:** physics rationale only, everywhere.
- **Flag-don't-fix:** any correction requiring judgment → ledger entry with both sides quoted verbatim + provenance, routed to Grant. Only zero-judgment pure-propagation corrections applied directly.

### Ground-truth docs (merged on main; the 07-01→07-19 window's authorities)

- `research/2026-07-19_f6-thermal-floor-arm_result.md` — tri-form verdict: (a) STRONG floor-arrow EXCLUDED ~5σ, (b) reactive-floor arrow mechanism STRUCTURALLY INEXPRESSIBLE (identity-class, #721-W2 shape), (c) mild ≤~30% partial UNCONSTRAINED. "Empirical falsification" is DEMOTED, NOT the headline. Bare "NO-SUPPRESSION" tree label is DEGENERATE. **ARROW QUESTION stays OPEN** (two candidates: interacting-bath thermalization + X40-class click; both SPEC only).
- `research/2026-07-19_yield-fork-discriminators_result.md` — yield fork stays OPEN; crux relocated to `#59` Flag F (first-order overdamped vs second-order reactive `S`-dynamics). Leg A = B; Leg B = NEITHER (frozen bins), memristive neither confirmed nor falsified.
- `research/2026-07-19_deep-space-reactive-bulk-walk_RECORD.md` — resistive-stall / lunar-Joule mechanism DEMOTED (lossless/pure-reactance ruling); band-map re-derivation SPEC'd not run.
- `research/2026-07-19_noise-floor-arrow-walk_RECORD.md` — the walk this arm tested; NOTHING new canon.
- `_orchestration/2026-07-10_rulings-docket.md` — RULING 21 (Op3 = LOSSLESS TRANSDUCTION), RULING 22 (KEEP the instrument; DOS-balance MOOT under noise-floor ruling), ENTRIES 16–22 (F6 arc), noise-floor + deep-space continuations. **[FENCED — PR #738; read-only ground truth]**
- `manuscript/ave-kb/common/retention-transition-split.md` — PRODUCT/TRANSITION split; the split leaf that now governs retention/transition conflation. Already current (RULING-21 block, yield-fork-open note).
- F6 arc PRs: #721 (nonlinear envelope), #724 (κ-band flip VALID[0.030,0.030]), #726 (FOREIGN-EATER + corrected-observable favorable evidence), #727 (INSTRUMENT-INCOMPATIBLE).

---

## Counts (running)

| Class | Fixed | Ledgered (flag-don't-fix) | APPLY-POST-#738 |
|---|---|---|---|
| C1 mechanical hygiene | TBD | TBD | TBD |
| C2 propagation-lag drift | TBD | TBD | TBD |

---

## COLLISION FENCE — PR #738 (open, under review)

Do NOT edit these files; findings on them go here tagged **APPLY-POST-#738**:
`manuscript/ave-kb/.index/claims.jsonl`, `common/claim-quality.md`, `common/dark-wake-bemf-foc-synthesis.md`, `common/engine-capability-map.md`, `common/substrate-hysteresis-index.md`, `common/trampoline-analogy-primer.md`, `vol3/cosmology/ch05-dark-sector/effective-galactic-acceleration-mond.md`, `vol4/circuit-theory/ch1-vacuum-circuit-analysis/tau-relax-derivation.md`, plus `_orchestration/2026-07-10_rulings-docket.md`, `_orchestration/2026-07-15_hardware-ratings-map.md`, `research/_archive/L3_electron_soliton/59_memristive_yield_crossing_derivation.md`.

### APPLY-POST-#738 findings

_(populated during sweep)_

---

## CLASS 1 — MECHANICAL HYGIENE

_(populated per category commit)_

---

## CLASS 2 — PROPAGATION-LAG DRIFT

_(populated per category commit; flag-don't-fix items carry both sides verbatim + provenance)_

---

## Orphan / phantom index lists

_(populated during index-consistency pass)_

---

## NOT-SWEPT (honest disclosure)

_(populated at close)_
