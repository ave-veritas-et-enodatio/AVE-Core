# Charter — testing-infra gate (model-any-bench → bankable divergent-from-SM prediction)

**Session:** Cleave-01 orchestration, 2026-06-23. **Status:** GAP-1 (spine) green-lit; lead-target fork GATED (see Fork-1). **Reviewed:** a cross-session audit reviewed the grounding synthesis and concurred (build→point reframe, FORM-not-magnitude cut, cRIO-as-validate-on-known, GAP-1-first all hold); it surfaced one collision (optical-activity channel may be ill-defined) and one elevation (the 7.5/α³ ratio may be under-graded). Both are folded in below.

---

## 1. The reframe: B is a *composition + targeting* problem, not a build

Discovery (workflow `wf_a37b5518`, 4-agent fan-out) found the "model-any-bench" infra is **~70% built and in production.** The deliberate spine is **`ave.bench`** (`src/ave/bench/__init__.py`), 4 bench-agnostic contracts:
- `sweep.run_divergence_sweep` (`bench/sweep.py:77`) — co-computes AVE **and** an SM baseline on **one shared grid**; hard no-strawman invariant (SM must be a callable on the same grid). The load-bearing honest-divergence engine.
- `apparatus` (`bench/apparatus.py:54`) — geometry → saturation A₀ + Fowler-Nordheim breakdown ceiling.
- `snr` (`bench/snr.py:57`) — shot-noise SNR → time-to-Nσ.
- `validate` (`bench/validate.py:141`) — recover-a-known gate.

Plus the legs: `observable_battery.py` (14-channel universal readout), `observable_sweep.py` (N-D parameter cube), `fdtd_3d.py`/`fdtd_3d_jax.py` (EM substrate engine), `regime_map.py`, `graded_vacuum_network.py` (3-channel impedance, Build-A only), SPICE solvers. AVE-Bench-Birefringence already rides `ave.bench` (the adoption proof-of-concept).

## 2. The gaps

- **GAP-1 (this charter) — no top-level `BenchModel` spine** composing the legs into one "given a bench spec → model AVE + SM, sweep, score" pipeline. (Zero hits for `BenchModel`/`bench.registry`.) The legs exist; nothing wires them.
- **GAP-2 — no reusable SM-model library.** The same-grid *contract* exists; each bench hand-writes its QED/classical baseline (4 fragmented copies). Co-computed-no-strawman is enforced as discipline, not shared code.
- **GAP-3 — no config-*ranker*.** Sweeps verdict each config; nothing scores by a figure-of-merit and returns best-N. (No `rank`/`argsort`/`pareto`/`FOM` in bench dirs.)
- Lesser: GAP-4 `SubstrateExcitation` class-tree trapped in one Vol-9 driver (`cvr_model.py:291`), not promoted to `src/ave/`; GAP-5 `graded_vacuum_network` Build-A only (no `H_couple`/coupled-solve); GAP-6 cRIO has prereg DRAFT, no driver, blocked on a Branch-R/F sign tension.

## 3. GAP-1 scope — the `BenchModel` spine

Compose the existing legs into one pipeline: **bench-spec → (substrate engine + coupling) → observable → SM-baseline co-sweep → bankability record.** Channel-agnostic (it models whatever prediction survives — see Fork-1). Reference adopter: AVE-Bench-Birefringence (already on `ave.bench`). Defer GAP-3 (ranker) and GAP-4 (class-tree promotion) until the spine + one real prediction-sweep prove the shape.

The spine's output record is the **bankability schema** — the 8 methodology gates (§4) as machine-checkable fields, not prose.

## 4. The bankability bar (8 gates → the `BenchModel` record schema)

From the methodology-bar discovery agent (each gate SHA-pinned to a source):
- **G1 validate-on-known** — every kill-verdict carries a modeled positive-control leg through the *identical* chain (named known reference + resolution-margin + an explicit INCONCLUSIVE bin). `cleave-01-requirements-boundary-conditions.md:42,157`.
- **G2 bankable = forced FORM, not echoed VALUE** — per-axis chord/echo tag; the infra refuses to label an *echo* axis as the falsifiable discriminator.
- **G3 SM co-computed, same machinery** — store {AVE leg, SM leg, discriminator-axis (MAGNITUDE|RATIO|SLOPE), verdict}; a prediction whose discriminator axis is *shared* with the counterpart auto-flags NON-bankable. `ave-discrimination-check` Step 2.5.
- **G4 derived-vs-asserted ledger** — 4 mandatory rows (coupling / probe / magnitude / observable), each DERIVED(file:line) | ENGINEERING-CHOICE(rationale) | ASSERTED(flag). Any ASSERTED row → FORK-status, not bankable. `feedback_experiments_fully_lattice_derived`.
- **G5 sensitivity sweep, not single-point** — plotted response surface over each load-bearing parameter; in-window fraction; verdict-flip boundary; a tuned-point-only positive books NEGATIVE. `ave-engineering-program-rigor:19`.
- **G6 symmetric standard** — per-cell "does the counterpart also import/fit/assert?" → PEER not demote; genuine AVE-only shortfall STANDS. `feedback_consensus_bias_symmetric_standard`.
- **G7 frozen prereg before measurement** — expected magnitude WITH canonical-primitive dimensional eval; outcome bins incl. INCONCLUSIVE; amendment runs the orphan-check. `ave-prereg` Step 3/3.5/3.6.
- **G8 evidence-framing** — explicit gating-vs-non-gating axis; binding-spec class (LEVEL-STABILITY/drift | SINGLE-SHOT | SNR-floor); full sweep denominator (no selection-from-pool). `ave-evidence-framing-discipline`.

## 5. The bankable shortlist — current state (the brutal cut)

AVE's cleanest SM-divergences are all **FORM / existence / zero-vs-nonzero**; every *magnitude* is an α-echo or an unpinned engineering scale. So the infra is built to bank FORMS, not magnitude-matches. Of the four named candidates:

| Prediction | Verdict | Bank? |
|---|---|---|
| **Optical-activity sign-flip** | CHORD (form); QED ≡ 0 (cleanest divergence, no free-param escape) | **AT RISK** — Phase-1 OUTCOME C: degree-3 srs may have **no isolated transverse photon band** (no clean photon to rotate). GATED on the chiral-OA verify `a5997007978673e33` (fundamental → channel closed; premature-numerical → transfer-matrix could still bank it). |
| **Birefringence coefficient** | CHORD (tree-vs-loop FORM) **+ forced-given-α quantitative ratio**; magnitude = symmetric α-echo | E-route/HIBEF, facility-class; PVLAS resolved (static-B δn≡0 exactly). ~2×10⁸ over floor. **7.5-trace RESOLVED (`a94672de`):** 7.5 = (lattice-derived ½)/(textbook 3/45) is FORCED; α⁻³ = α⁻²(structural tree-vs-loop, AVE-distinct) × α⁻¹(AVE's own `E_yield≡√α·E_crit` import). Bankable as "AVE sits ~10⁷× QED, field-independent, tree-vs-loop"; NOT as an emergent number (α imported both sides). Sturdier than existence-only. |
| (q·ℓ_node)⁴ dispersion | form-real, **sub-bound**; physical-photon slope-4 hardcoded (eigensolve gives 2, rides weak-C) | No (near-term) |
| GW-echo | zero-knob chord but forced ~4 ms **fails** the only (contested) 0.29 s by 68×; not validated; *shear* channel, already LIGO-instrumented | No |

## 6. The strategic squeeze (named plainly)

The genuinely AVE-distinct channel (**bulk / V-sector longitudinal**, the common-mode breathe) is **uninstrumented** (transverse detectors blind to it; impedance-probe Phase-A confirmed it's a future-physics gap, not a near-term instrument). The cheap-to-read channels (**EM, shear**) are **peer-with-SM**. The one EM-photon zero-vs-nonzero chord (**optical-activity**) is **at-risk/ill-defined**. So the near-term bankable target may collapse to **birefringence-coefficient — now confirmed (7.5-trace) as a forced-given-α quantitative ratio + tree-vs-loop chord, a real discriminator rather than a weak existence test.** The squeeze is real (facility-gated; the magnitude is not emergent — α imported both sides) but the fallback is sturdier than it first appeared.

**Escapability caveat (do not let the squeeze calcify):** the squeeze is on the *current hand-enumerated* shortlist. Part of the gate's job — specifically GAP-3 (the config-ranker) — is to test whether it's escapable: a bulk/V-sector observable a clever bench could reach, or an EM-config not yet enumerated. The infra should be able to *say* "no escapable config in the swept space," not assume it.

## 7. Forks

- **Fork-1 (lead target) — GATED on one remaining input.** Optical-activity (benchtop, cleanest divergence, "does it present?") vs birefringence-coefficient (facility, designated-bankable).
  - **Input (b) RESOLVED** — the 7.5/α³ trace (`a94672de`): birefringence is a **forced-given-α quantitative ratio + tree-vs-loop FORM chord** (7.5 forced = lattice ½ ÷ textbook 3/45; α⁻³ = α⁻² structural tree-vs-loop × α⁻¹ AVE's E_yield≡√α·E_crit import; magnitude a symmetric α-echo). So the birefringence fallback is a real **quantitative discriminator** ("~10⁷× QED, field-independent, tree-vs-loop"), **not** a weak existence test.
  - **Input (a) STILL PENDING** — the chiral-OA verify `a5997007978673e33` (fundamental → OA channel closed; premature-numerical → transfer-matrix could still bank it).
  - **Resolution rule:** if OA is fundamental → lead = birefringence-as-quantitative-ratio (sturdy, facility-gated). If OA is premature-numerical → both EM-photon observables stay live; spine models both, sensitivity sweep decides. Spine built **channel-agnostic** regardless, so it's correct either way.
- **Fork-2 (bankability quorum) — proposed default, Grant to confirm.** Graded ladder: G1–G5 hard-gating + G6–G8 framing-discipline. Mint an intermediate tier "bankable AS DISCRIMINATOR / first-cut absolute sizing" (the corpus's own phrasing) for predictions that pass the discriminator gates with an open G4 sizing row (birefringence today).
- **Fork-3 (force-name-the-gating-axis?) — proposed default: YES.** The infra refuses to model a prediction whose declared falsifiable axis is an echo (the Cleave move). Cheap discipline, high payoff.

## 8. Pilot — cRIO C_eff(V) as validate-on-known (NOT a physics test)

The only **in-hand** bench; vacuum kernel unreachable by ~18–24 OOM → it is the **validate-on-known positive control** (learn the lock-in/drift-rejection/floor-attribution chain on a known nonlinear cap before betting it on the EM-photon prediction). Caveat: its Branch-R/F sign tension (GAP-6) blocks *bin-pinning* and any future cRIO *physics* work, but **not** the validate-on-known pilot (the ladder runs regardless of sign). Keep the sign tension on the board.

## 9. Sequencing

1. Build the `BenchModel` spine (GAP-1), 8-gate record baked in, channel-agnostic. Reference adopter = AVE-Bench-Birefringence.
2. Validate the chain on **cRIO** (pilot).
3. Point the spine at the **EM-photon channel** (birefringence + optical-activity), full sensitivity sweeps, frozen prereg → bankability verdict — *after* Fork-1 lands.
4. Defer GAP-3 (ranker) + GAP-4 (class-tree promotion) until the spine + one prediction-sweep prove the shape; revisit GAP-3 specifically to test squeeze-escapability (§6).

## 10. Cross-session dependencies (in flight)

- **Chiral-OA verify `a5997007978673e33`** — settles Fork-1's optical-activity branch. Lands shortly. **Do not duplicate.**
- **7.5/α³ provenance trace `a94672de`** — DONE: 7.5 FORCED (lattice ½ ÷ textbook 3/45); birefringence = forced-given-α quantitative ratio + tree-vs-loop chord, magnitude a symmetric α-echo. Fork-1 input (b) resolved.
- **Impedance-probe Phase-A** — INFEASIBLE near-term but gated-not-dead; informs the bulk/V-sector "uninstrumented channel" squeeze. `research/2026-06-23_vacuum-impedance-probe-phase-a-feasibility_result.md`. Probe-primitive canonization brief: `_orchestration/2026-06-23_vacuum-impedance-probe-primitive-handoff.md`.

## 11. Source

Discovery workflow `wf_a37b5518` (infra inventory, prediction dossiers, bench readiness, methodology bar) — all file:line in that run's agents. Synthesis + this charter: Cleave-01 session. The build→point reframe, the FORM-not-magnitude cut, cRIO-pilot, and GAP-1-first were independently concurred by a cross-session audit.
