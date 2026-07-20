# Vol-9 Vacuum-Datasheet Update — 2026-07-19 (07-01 → 07-19 merged-arc absorption + fork-open caveats)

**Lane:** implementer (VOL-9 MANUSCRIPT UPDATE), Grant-ordered 2026-07-19 ("do an update to vol 9s manuscript").
**Branch:** `docs/vol9-update-2026-07-19` (self-isolated worktree off `origin/main`).
**Baseline (ground truth = MERGED main ONLY):** `origin/main` @ `1be045a1` (Merge PR #735, yield-fork-discriminators).
**Scope fence:** `manuscript/vol_9_vacuum_datasheet/**` tex + this ledger ONLY. No ave-kb edits, no other volumes, no engine, no unmerged-branch files.

Follows the established per-volume datasheet-update pattern (Vol-5 #344/#347/#352; Vol-1 rulings). Rule-12 KEEP-BOTH additive-only (zero deletions of existing physics prose); verify-before-cite two-method; pure-corpus.

---

## Method

1. Read the full volume (`chapters/*.tex`, `main.tex`, `_manifest.tex`) + the four MERGED ground-truth docs:
   - `research/2026-07-19_yield-fork-discriminators_result.md` (Leg A = B; Leg B = NEITHER; fork OPEN @ #59 Flag F)
   - `research/2026-07-19_f6-thermal-floor-arm_result.md` (tri-form verdict; arrow OPEN)
   - `research/2026-07-19_deep-space-reactive-bulk-walk_RECORD.md` (bulk = lossless reactance; demotions)
   - `manuscript/ave-kb/common/retention-transition-split.md`; `manuscript/ave-kb/common/engine-capability-map.md` §8c
2. Keyword sweep of the full vol_9 tree for every near-yield / dissipative-loop / deep-space-stall / F6 / thermal-floor / arrow site (two-method: `grep -rniE` on chapters + full-tree pass).
3. Land the routed C2-FLAG-2 item + the F6-arc / fork-open currency notes as dated KEEP-BOTH additive banners on EXISTING structure. Null items recorded with NOT-SWEPT honesty.
4. `make verify` green + vol_9 `pdflatex -halt-on-error` compile check before push.

### Provenance caveat (verify-before-cite; flag-don't-fix)

The routing document that names C2-FLAG-2 — `_orchestration/2026-07-19_manuscript-cleanup-ledger.md` — is **NOT on merged main**; it lives on the unmerged branch `docs/manuscript-cleanup-2026-07-19` (the #738/#739 family excluded by the task fence). Its C2-FLAG-2 *content* is reproduced in the dispatch and the underlying physics ground-truth (the yield-fork result) IS merged. **Disposition:** the tex banners cite the MERGED result docs (`research/2026-07-19_yield-fork-discriminators_result.md`, `research/2026-07-19_f6-thermal-floor-arm_result.md`) and `engine-capability-map.md §8c` — NOT the unmerged cleanup ledger. This is a deviation from the dispatch's "cite the ledger" instruction, taken to keep every tex citation resolvable on merged main (verify-md-links gating). Flagged here, not silently substituted.

---

## Per-item disposition

| # | Dispatch item | Target in vol_9 | Disposition |
|---|---|---|---|
| 1 | Read volume + ledger | — | DONE |
| 2 | C2-FLAG-2 (ch5 ~:599 thixotropy cite) | `chapters/05_ac_electrical_characteristics.tex` :598–599 | **LANDED** (commit 2) |
| 3 | Memristor/hysteresis fork-open caveat | none separate — folds into #2 | **FOLDED** (no memristor/hysteresis/anelastic/loop-area row exists anywhere in vol_9; the ONLY near-yield dissipative-loop banking in the whole tree is ch5:599) |
| 4 | F6-arc absorption (engine-requirements test status) | `chapters/17_engine_requirements.tex` §Conservation Canaries | **LANDED** (commit 3) |
| 5 | Deep-space/bulk-dissipation demotion | **NO TARGET** | **NULL (clean)** — see NOT-SWEPT below |
| 6 | General currency sweep | remaining chapters | **NO PROPAGATION FIX NEEDED** — see NOT-SWEPT below |
| 7 | This ledger | `_orchestration/2026-07-19_vol9-update-ledger.md` | DONE |

Docket append: **not made** — no rulings-relevant NEW disposition was produced (the C2-FLAG-2 landing is a KEEP-BOTH additive currency note authorized by Grant's vol-9 order, not a new ruling; the fork stays OPEN and the ruling stays Grant's).

---

## NOT-SWEPT honesty (what this pass did NOT touch, and why)

- **Item 5 (deep-space bulk-dissipation) — NO TARGET in vol_9.** Two-method grep (`resistive metric | topological joule | diffuse matter | deep.space | slipstream | stall | P_drag | lunar.*joule | 1.04.*TW`) across the full vol_9 tree returns ZERO sub-yield bulk-dissipation assertions of the demoted type. Every "Joule"/"dissipat" hit in vol_9 is either (a) boundary-Joule extraction at a Γ-port (ch13 Born-rule; Ax3-LEGAL, not a bulk resistor), (b) Johnson-Nyquist FDT at a resistive BOUNDARY (ch06; port, Ax3-legal), (c) the ch5:461 warningbox that CORRECTLY states "below threshold Axiom-3-lossless forbids the dissipative carrier machinery" (already aligned with the walk-record's ruling), or (d) Regime-IV cosmological rupture (ch08/ch12/ch14 BH-interior melt; not sub-yield bulk). The demoted "topological Joule stall / resistive deep-space metric" prose lives in Vol-1/Vol-3, NOT here. Nothing to demote in vol_9.
- **Item 6 (general currency sweep) — already current.** The 07-01→07-19 merged FORM-deriving/VALUE-importing framings are already correctly present in vol_9: α = Class-B echo at the value level (ch5 §CVR echo-scope, ch5 :304 √α; ch17 req-17 Q=1/α value-echo), G = mixed / ξ back-fit (ch12 :204, ch13 :9, ch19 :82), K=2G = GR-imported (ch19 :49). No stale overclaim found requiring a pure-propagation fix. Anything judgment-class was routed here, not edited in place.
- **Band-map absorption (follow-on, GATED).** The deep-space reactive band-map re-derivation (`research/2026-07-19_deep-space-reactive-bulk-walk_RECORD.md` §5, SPEC'd/Grant-gated) and its unmerged band-map derivation (PR #741 family) are NOT this lane's job. When #741 merges, a follow-on lane may absorb a reactive-band-structure note into ch12 (cosmological) / a Kirkwood-gap cross-ref. Recorded as a gated follow-on, NOT swept here.
- **ch06 thermal-floor cross-ref (candidate follow-on, NOT taken).** Grant's noise-floor ruling maps the T2 sink to the Johnson-Nyquist static floor (ch06 §Johnson-Nyquist). A cross-ref from ch06 to the F6 thermal-floor arm was considered and DEFERRED: the thermal-floor arm is an arrow-of-time RESULT, not a datasheet temperature line; adding it risks over-claiming a connection. Candidate for a future pass if Grant wants the noise-floor↔F6 link surfaced datasheet-side.

---

## Contradictions / flags surfaced (flag-don't-fix)

- **[C2-FLAG-2, ch5:599] Object-mapping subtlety (judgment-class) — SURFACED, not resolved.** The ch5:599 open question is framed on the datasheet's BULK amplitude-limit asymmetry (`τ_bulk,sat` toward compression ceiling `ρ̄→+1` vs `τ_bulk,desat` toward cavitation floor `ρ̄_cav=−1/φ`). Leg A of #735 tested the prereg's DIRECTIONAL two-τ `sign(dr/dt)` rate-memory. These are related but NOT verbatim the same object. #735 excludes the directional sign-memory rectifier by derivation; it does NOT by itself close the ceiling-vs-floor amplitude-limit asymmetry (which could still be carried reactively by the second-order S-structure = Flag F). The KEEP-BOTH note preserves the 2×2 structure and flags this for Grant/auditor, per the dispatch's explicit "judgment-class — flag not silently resolve" instruction. No contradiction between engine output and corpus — the datasheet's "not asserted" stance is UNCHANGED; the note adds the run-status + the fork-open scope-caveat additively.
- **No engine-vs-corpus contradiction found in the C2-FLAG-2 landing.** The merged result (fork OPEN, Leg A = B) is fully consistent with the datasheet's pre-existing "Open (not asserted)" stance; the note is pure currency + scope-caveat, zero physics-prose deleted.
</content>
</invoke>
