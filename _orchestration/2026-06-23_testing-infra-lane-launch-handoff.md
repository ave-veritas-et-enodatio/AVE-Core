# LAUNCH HANDOFF — Testing-Infra Lane (model-any-bench → bankable divergent-from-SM prediction)

**Created:** 2026-06-23 · **Role:** separate orchestration lane (workstream B) · **Posture:** refute-by-default, FORM-not-magnitude
**Merge model:** you produce **reviewed PRs**; you do **NOT** self-merge. A separate orchestrator session adversarially audits each diff; **Grant merges.** Surface every framing-level call inline. You have no memory of the originating conversation — this handoff is self-contained; verify every pointer with grep.

## 0. What this lane is
You execute the **testing-infra charter** — the strategic spine of AVE's testing pivot. The premise (established, not up for re-litigation): AVE **forces FORMS / imports VALUES**, so the AVE-distinct chord lives **only in forward predictions**, and the job is infra-first — build the apparatus that can model *any* bench, co-compute an honest SM baseline on the same grid, sweep sensitivity, and return a **bankability verdict** for a divergent-from-SM prediction *before* any hardware. This lane runs in parallel with the live engine-consolidation lane.

## 1. Read first (the substance lives in the charter)
1. **`/Users/grantlindblom/AVE-staging/AVE-Core/_orchestration/2026-06-23_testing-infra-gate-charter.md`** — the full charter (reframe, the 3 gaps, GAP-1 scope, the 8-gate bankability bar, the bankable shortlist + the strategic squeeze, the forks, sequencing). **This is your primary spec.** (Read it from that absolute path — it is on `main` once PR #378 merges, but readable from the main checkout regardless; reading is not a git op.)
2. `AVE-Core/CLAUDE.md` (repo orientation), `manuscript/ave-kb/CLAUDE.md` (KB invariants).
3. Skills: `ave-discrimination-check`, `ave-evidence-framing-discipline`, `ave-prereg`, `ave-canonical-source`, `consistency-vs-emergence`, `substrate-native-check`.

## 2. First deliverable — GAP-1: the `BenchModel` spine
Compose the legs that already exist (the `ave.bench` contracts — `sweep.run_divergence_sweep`, `apparatus`, `snr`, `validate` — plus `observable_battery`, `observable_sweep`, `fdtd_3d`, `regime_map`, `graded_vacuum_network`, SPICE) into ONE channel-agnostic pipeline:

> **bench-spec → (substrate engine + coupling) → observable → SM-baseline co-sweep → bankability record.**

- **Channel-agnostic** (models whatever prediction survives Fork-1 — do not hard-wire to one channel).
- **The output record IS the bankability schema** — the 8 gates (charter §4) as machine-checkable fields, not prose. (G1 validate-on-known · G2 forced-FORM-not-echoed-VALUE · G3 SM co-computed same-machinery + discriminator-axis tag MAGNITUDE|RATIO|SLOPE · G4 derived-vs-asserted 4-row ledger · G5 sensitivity-sweep-not-single-point · G6 symmetric-standard · G7 frozen-prereg · G8 evidence-framing.)
- **Reference adopter** = AVE-Bench-Birefringence (already rides `ave.bench` — the adoption proof-of-concept; mirror its shape).
- **Defer GAP-3 (config-ranker) and GAP-4 (SubstrateExcitation class-tree promotion)** until the spine + one real prediction-sweep prove the shape.
- Then: **validate the chain on cRIO** (the only in-hand bench; vacuum kernel unreachable by ~18-24 OOM → it is the *validate-on-known positive control*, NOT a physics test; its Branch-R/F sign tension blocks bin-pinning but not the validate-on-known pilot). Then point the spine at the EM-photon channel (birefringence + optical-activity) with full sensitivity sweeps + frozen prereg — *after* Fork-1 lands.

## 3. Fork resolutions (charter §7)
- **Fork-2 (bankability quorum) — DEFAULT APPLIED (Grant baked-in, may revisit):** graded ladder — **G1–G5 hard-gating + G6–G8 framing-discipline**, with an intermediate tier **"bankable AS DISCRIMINATOR / first-cut absolute sizing"** for a prediction that passes the discriminator gates with an open G4 sizing row (birefringence today).
- **Fork-3 (force-name-the-gating-axis) — DEFAULT APPLIED (= YES):** the infra refuses to model a prediction whose declared falsifiable axis is an *echo*. Cheap discipline, high payoff — bake it into the schema (G2/G3).
- **Fork-1 (lead target) — input (b) RESOLVED** (the 7.5/α³ trace: birefringence is a forced-given-α quantitative ratio + tree-vs-loop FORM chord, magnitude a symmetric α-echo). **Input (a) PENDING** — the chiral-OA verify `a5997007978673e33` (fundamental → OA channel closed; premature-numerical → transfer-matrix could still bank it). **Non-blocking** — the spine is built channel-agnostic, correct either way. **Do NOT duplicate that verify** (cross-session, lands shortly).

## 4. The bankability reality (do not let it calcify, do not over-claim past it)
The genuinely AVE-distinct channel (**bulk / V-sector longitudinal**) is **uninstrumented** (transverse detectors blind to it; impedance-probe Phase-A confirmed it's a future-physics gap, not a near-term bench). The cheap-to-read channels (**EM, shear**) are **peer-with-SM**. The one EM-photon zero-vs-nonzero chord (**optical-activity**) is at-risk/ill-defined pending Fork-1(a). So the near-term bankable target likely collapses to **birefringence-coefficient** — a forced-given-α quantitative ratio + tree-vs-loop chord (~10⁷× QED, field-independent), facility-gated (E-route/HIBEF; PVLAS resolved, static-B δn≡0 exactly), magnitude NOT emergent (α imported both sides). **Escapability caveat:** the squeeze is on the *current hand-enumerated* shortlist — part of the gate's job (GAP-3, later) is to test whether a clever bench reaches a bulk/V-sector observable or an un-enumerated EM-config. The infra should be able to *say* "no escapable config in the swept space," not assume it.

## 5. Standing gate + constraints
- **Refute-by-default** before any landing; deflate-then-document. **Symmetric-standard** both ways (peer-with-SM honesty; G6). The infra's whole point is to refuse to over-claim — an audit that finds a bankable magnitude everywhere has too-permissive a lens.
- `main` PROTECTED; **NO self-merge.** Self-isolate git-mutating work in a `/tmp` worktree off `origin/main` (workspace root is not a git repo; AVE-Core is one level down).
- **NEVER put the substring `build` in a worktree/branch name** (trips `predictions_manifest_validator.py:136`) — e.g. `analysis/benchmodel-spine`, NOT `analysis/build-spine`. (The word is fine in prose/docs; only branch/worktree *names* are gated.)
- verify-before-cite (re-confirm file:line against HEAD); run the local `make verify` gate (worktree-aware) before committing. PURE-AVE-CORPUS (physics only). `ave-canonical-source` (import from `constants.py`). audit-trail-in-git: do NOT edit `_archive`, `*_FROZEN` preregs, SESSION_STATE, or result/walk-back docs. Flag-don't-fix for framing-level physics calls.

## 6. Check-in / audit interface
Produce reviewed PRs (the spine likely lands incrementally — skeleton first, then one contract per commit; large single Writes hit socket timeouts). Mark each "for review — orchestrator audit + Grant merge pending." Surface all Grant-calls in PR bodies. The originating orchestrator adversarially audits each diff before Grant merges — write so that audit is easy (per-contract provenance, honest self-flagging).

## 7. Cross-session dependencies (in flight — do not duplicate)
- **Chiral-OA verify `a5997007978673e33`** — settles Fork-1's OA branch; lands shortly.
- **Engine-consolidation lane** — live in parallel (`ave-ec/*` worktrees); its `SubstrateExcitation` / ledger work may inform GAP-4 later. Coordinate via the orchestrator, don't collide.
- **Impedance-probe Phase-A** (`research/2026-06-23_vacuum-impedance-probe-phase-a-feasibility_result.md`) — INFEASIBLE near-term, informs the bulk/V-sector squeeze.
