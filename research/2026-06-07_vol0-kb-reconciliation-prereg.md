# PREREG (frozen) — Vol 0 ↔ KB reconciliation ledger

**Date:** 2026-06-07
**Lane:** auditor/implementer hybrid — produce a READ-ONLY reconciliation ledger. **No Vol 0 edits, no KB edits.** The deliverable is the *worklist* for a future Vol 0 sync, not the sync.
**Branch:** `analysis/2026-06-07-vol0-kb-reconciliation-ledger` (off `main` @ `f1f927c8`), isolated worktree `/tmp/ave-vol0-recon-wt`.
**Trigger:** Grant — "should you start updating vol 0 from all the work being done?" → recommendation was *reconciliation ledger first, not prose sync*. Grant: "work in your own branch, use all relevant skills" + **"KB is the source of truth."**

## Source-of-truth axis (load-bearing)

**`manuscript/ave-kb/` is canonical.** Vol 0 (`vol_0_engineering_compendium`) is a *downstream synthesis* of the KB. Every reconciliation finding is anchored: `Vol 0 claim @ file:line` ⟷ `governing KB leaf @ file:line` ⟷ `current KB state`. Where Vol 0 and the KB disagree, **the KB wins** and Vol 0 is the drifted party (unless the KB leaf is itself under open adjudication — then HOLD).

## What I expect (pre-registration)

1. **Ch 2 analytical-summaries (28 ledger entries) is mostly Class A** (matches-KB): the canonical constants (ℓ_node, α=p_c/8π, p_c=0.1834, ν_vac=2/7, κ_FS=8π, m_p=1836, m_W/m_Z=√7/3, H_∞=69.32) are stable canon. The dual-reactance V_total=2.0 entry was *already* reconciled 2026-06-01 (FEM-provenance dropped) and propagated 2026-06-02 (`063e7c1b`) — expect Class A.
2. **The z=3/SRS-vs-z=4/Diamond split is the headline Class-D finding.** Confirmed pre-fan-out: `backmatter/02_full_derivation_chain.tex:510` ("3-connected") + SRS naming (`:918`, `:1206`, `03_geometric_inevitability.tex:506`) contradict the now-canonical 4-fold Axiom 1 (`eq_axiom_1.tex:20`, restated in the same Vol 0 at `12_mathematical_closure.tex:76`). **Caveat:** the connectivity *number* (z=4) is settled-on-main → Class D; but the *screening "3"* (Δc_crit) it feeds is the **contested Grant-call** from neutrino-3 → Class O. Must split these.
3. **Internal Vol 0 symbol collision:** `ν_vac` denotes BOTH "Kinematic Network Mutual Inductance" (≈8.45e-7 m²/s, `02_analytical_summaries.tex:13`) AND "Vacuum Poisson's Ratio" (≡2/7, `:30`), used together in the δ_th entry (`:22`). Expect Class M (needs KB grounding / disambiguation).
4. **Open-adjudication HOLDs (Class O), must NOT be queued for sync:**
   - **Gravity ppn (W1/W2/W3):** `(9/7) controls light deflection` outlier vs surviving `(2/7)` chain (`research/2026-06-05_gravity-ppn-coherence-result.md`; branch unmerged). Vol 0's 9/7's are *elastic* (1+ν_vac) — expect Class A, but verify none carry a deflection-attribution.
   - **Neutrino-3 Δc_crit:** z=3-vs-z=4 screening bottleneck (`research/2026-06-07_neutrino-3-regrounding-check.md`; merged but walk-back SURFACED-not-executed).
   - **BH Γ=−1 vs Γ=0:** flagged in doc-reconciles Finding 5; touches A-034 kernel catalog → check Vol 0 `backmatter/07_universal_saturation_kernel.tex`.
5. **Already-done (do NOT re-flag):** doc-reconciles Findings 5/6/7 (SU(2)→K4 4π relabel, BH-leaf title, closure-roadmap refs) — `research/2026-06-06_doc-reconciles-result.md`, merged `59ce0f09`.

## Class taxonomy (KB-as-source-of-truth reconciliation)

- **Class A (matches-KB)** — Vol 0 value/identity/status matches the current governing KB leaf. No action.
- **Class D (correctness drift)** — Vol 0 contradicts the current KB leaf (value changed / identity superseded / KB-walked-back-but-Vol-0-still-asserts). **Highest priority** — Vol 0 asserts something the source-of-truth no longer says.
- **Class B (status/provenance drift)** — value matches but KB reframed/rescoped/added-caveat/changed-provenance that Vol 0's framing doesn't reflect (e.g. "exact"→"conditional"; SRS→Diamond naming).
- **Class O (open-adjudication / HOLD)** — governing KB leaf is itself under open adjudication. **Flag, do NOT queue for sync** until KB closes.
- **Class M (KB-missing / Vol0-only / internal-inconsistency)** — Vol 0 asserts something with no governing KB leaf, or an internal Vol 0 collision. Needs KB grounding before trust.

**Worklist priority (for the eventual sync, NOT executed here):** D > B > O(hold) > M.

## What would discriminate

A finding is **real drift** only if an independent skeptic re-reads the governing KB leaf and confirms the disagreement (Vol 0 says X, KB-leaf-at-file:line says not-X). A finding is **Class O** only if a research-doc or claim-quality entry shows the leaf under unresolved adjudication. Every ledger row carries both file:lines + the skeptic verdict.

## Discipline applied

`ave-sweep-audit` (spine: class taxonomy + batch + closure-roadmap log), `ave-prereg` (this doc), `ave-audit` (pre-spawn grep-grounding — done: read doc-reconciles + gravity-ppn + neutrino-3 + Axiom 1 + Vol 0 chapters before fan-out), `verify-before-cite` (every row grep/Read-verified, adversarially), `ave-evidence-framing-discipline` (strongest-accurate class language), `flag-don't-fix` + `ave-walk-back` (read-only — ledger is the worklist, no propagation here), `self-isolate-worktree` (throwaway worktree off main).
