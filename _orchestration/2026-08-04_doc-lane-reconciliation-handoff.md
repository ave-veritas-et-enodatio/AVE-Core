# Documentation-lane reconciliation handoff — 2026-08-04

From: core orchestrator session. This brief answers the doc lane's 2026-08-04 status report
(11 input-needed items + 7 outstanding + 1 blocked) and supersedes the pending "reissue the
core-session handoff?" question — **do not reissue; this brief is the current state.**

**Rule zero (pointers-not-values):** every number referenced here lives in the pointed-at
artifact. Read it there at use time; re-derive, don't trust. Before deep-diving anything
Petermann- or cold-Q-adjacent, check `_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md`
first — your factor-2 audit independently re-derived its row 22, which predates your report.
That duplication was the cost of a stale handoff, not an error by your lane.

---

## 1. Staleness corrections — stand down on these

**Cold-Q / ringdown ("BLOCKED").** Superseded. The v2.4-root instrument CERTIFIED and its
verdict merged (PR #861). Artifacts on main:
`research/2026-08-03_coldq-pole-v2.4-root_prereg-FROZEN.md`, `..._result.md`,
`research/drivers/coldq_pole_v2p4_root.py`. The ringdown wave is no longer cert-blocked; it is
**HELD-BY-SEQUENCE**: it fires together with the memory-rescope wave after the polar-family
lane returns (core session signals the go). Action now: PRE-STAGE the wave (vol3 ch08+ch15,
`backmatter/07:{85,211,213}`, vol9/vol1 mirrors) against the v2.4 result doc — pull numbers
from the result doc at fire time, do not transcribe them into staging notes.

**Petermann items 1–3.** Your recommendation (demote the C₂ headline) was already executed:
PR #857 (merged) struck the ppm labels corpus-wide and fixed the truncated-`int()` retardation
artifact. Your factor-2 finding = frontier-queue **row 22** (`:199`; the double-cover is flagged
at `:216` as the only theorem-capable candidate). Your delay question (one-lap vs
radius-crossing) is the same fork in per-lap-vs-per-4π phrasing. The normalization-ledger lane
is GO'd with frozen target = **total a_e, not the C₂ slot**, and runs from the core session.
Your lossy-vs-reactive item (taxonomy "returns-to-source" vs power-lock "dissipative") is
routed INTO that lane under the transfer-cost frame — do not adjudicate it in the doc lane.

---

## 2. Grant rulings, 2026-08-04

Verbatim: **"4 rebuild white, 5 canonize circuits/, 6 carve-outs, 7/8/11 confirmed, trailer
per-session."**

- **R4 — five latent figures (b11, be9, he4, li7, n14): sources CANONICAL, REBUILD WHITE.**
  The artwork change on the five printed pages is accepted as the price of restored
  build-provenance. Execution note: all five are **generator-emitted** (board finding v-b:
  byte-matched to the `darkbg` preamble of
  `src/scripts/vol_6_periodic_table/circuits/generate_all_semiconductor_circuits.py` at
  `:286`/`:295`) — so the fix is **GENERATOR-FIRST**: white the generator per house style
  (white background, Okabe-Ito, honest axes), regenerate the `.tex`, rebuild the PDFs.
- **R5 — `circuit_c12`: `circuits/circuit_c12.tex` (builds printed p.92) = CANONICAL.**
  Retire `figures/circuit_c12.*` strike-don't-delete with a dated Rule-12 header. Note the
  canonical source is one of the 3 NON-generator dark files, so it needs its own hand white-port
  in the figure batch. (The 2026-06-07 ledger `:76` pre-flagged exactly this reconcile.)
- **R6 — orphan carve-outs stand.** `research/2026-06-07_figure-audit-ledger.md:84`
  (be8_decay PLACE-NEW → vol6 beryllium) and `:76` (dt_fusion KEEP) remain LIVE; the
  retire-sweep must exclude both. The ~9 June PLACE-NEWs are two months unexecuted — add an
  **"execute or re-rule"** row to the board rather than silently retiring any of them.
  Coupling: the hulse_taylor PLACE-NEW targets vol3 ch08 — if executed, it rides the ringdown
  wave (one-print-touch rule).
- **R7 (A3) — CONFIRMED**, and this is the explicit corpus-sweep GO for wave-3: rendered
  current-status notes stay in print; verbatim prior-wording `%` duplication drops (git is the
  trail).
- **R8 (A4) — CONFIRMED**: "byte-identical" only when a diff/md5 was actually run, method cited
  inline at the claim site; otherwise state the weaker true thing.
- **R9/R10 — no veto exercised** in the 2026-08-04 reply; your ratifications stand (the veto
  remains Grant's to exercise later).
- **R11 (the `07` seam) — CONFIRMED: HOLD the fix**; it fires inside the ringdown wave.
  Disclosed contradiction accepted for the interim (now a days-scale interim, not months).
- **Trailer — per-session actual model** (your sessions: Opus 5). Do NOT rewrite affected
  merged commits.

---

## 3. Work sequence (arc-serial, tiered)

Verification tiers per the 2026-08-04 truth-per-token ruling: hygiene work gets Tier-0
(machine checker only) or Tier-1 (single auditor) — no adversarial panels for polish.

1. **Register self-contradiction fix, ALONE first** — the "NOT yet canonical" scaffold banner
   in `manuscript/ave-kb/common/vocabulary-register.md` sitting above the ratified
   `def-tk1xfm` block. Small fix, highest blast radius (every status-sync cites the node).
   Tier-1.
2. **KB-lockstep batch 2 + the vol6 cite-shift touch-up as ONE wave.** Tier-0/1,
   checker-verified.
3. **Dark-TikZ: generator-first**, then the print-visible set under R4/R5. Tier-1 (print
   artwork).
4. **Cite items as you routed them** — drift-triage lane keeps the 13; cite-rot lean
   (2)+(3) now, (1) after FP-triage: approved.

**Item 7 (src/scripts mirror) is NOT a go — it's a physics-value fork.** Same formula, two
values: `manuscript/vol_6_periodic_table/chapters/04_helium.tex:98` and
`src/scripts/vol_6_periodic_table/simulations/semiconductor_binding_engine.py:141` both compute
$V_{BR} = 6\alpha\hbar c/D_{\text{intra}}$ yet print different MeV values — the drift is
upstream, in $D_{\text{intra}}$ or the constants. A mechanical sync in either direction would
launder whichever number is wrong. Route a **Tier-1 provenance re-derivation** (recompute from
the canonical chain, report which side is chain-true), THEN sync. Sites: generator `:409`/`:541`
+ engine `:141` vs manuscript `04_helium.tex:98`, `02_chemistry.tex:74`,
`01_computational.tex:295`.
