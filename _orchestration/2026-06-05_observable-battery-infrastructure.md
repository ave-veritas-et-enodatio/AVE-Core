# Observable-Battery + Sweep Infrastructure (orchestration)

**Date:** 2026-06-05 · **Branch:** `analysis/2026-06-05-observable-battery-infra` (off the (2,3)-extractor branch → off `origin/main` `c1d7390f`; worktree `AVE-Core-obs-battery-wt`)
**Prereg (FROZEN):** [`research/2026-06-05_observable-battery-infrastructure-prereg.md`](../research/2026-06-05_observable-battery-infrastructure-prereg.md) · **MAP:** workflow `wf_631750cd-ab6`
**Session:** orchestration (Grant in-session). Branch + reviewed PR; no direct-to-main.

## §0 What

One reusable `ObservableBattery` (src/ave/core/) that instruments every sim with the full physical readout (14 channels, prereg §1) + a no-axis-privileged sweep harness. Composes shipped diagnostics (KEEP-BOTH), honesty-tags every channel. Subsumes the Γ open/short seam, the (2,3) coordinate, the V0 fork, single-vs-bond-pair, the C↔L state. **Headline:** `sign(Γ_at_max_A2_bond)` adjudicates the open/short seam (Grant resolves; battery measures). Physical interpretation guide (the 4 AVE-native principles) = prereg §2.

## §1 Phase plan

- **P1 — Build (PENDING; implementor).** 9-step plan (prereg §6), skeleton-first, **Γ-read live-fired first (step 2)** as the first orchestrator checkpoint; batch-end small-cube live-fire (step 8).
- **P2 — Run a real cube + read it (after build).** First instrumented sweep; per-sim OPEN/SHORT + (2,3)-confidence + Θ_RP → bring the Γ-sign evidence to Grant for the seam adjudication.

## §2 Implementor dispatch spec (P1)

Full skill discipline per prereg §5. Build to the prereg §1 channel table (the "physical reading" column drives the per-sim classification). KEEP-BOTH (compose, never redefine the shipped diagnostics or the (2,3) extractor). Constants from `ave.core.constants`. Honesty tags mandatory (Q/J=proxy, reactance-ω=engineering-input). Push branch; do NOT merge.

## §3 Orchestrator checkpoints / audit-verification

1. **Step-2 Γ live-fire** — confirm `sign(Γ_at_max_A2)` actually fires on the tiny imposed-(2,3) run before the rest of the battery is built (the headline must read before we invest).
2. **Step-8 small-cube live-fire** — independently confirm every channel populates + the per-sim OPEN/SHORT resolves + artifacts write, before accepting the build.
3. Reuse/honesty audit (zero literals; no redefinition; tags present). Then → reviewed PR.

## §4 Outcome

_(filled on implementor return)_
