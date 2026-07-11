# Collapse-batch execution — result (2026-07-11)

**Branch:** `analysis/collapse-batch` (off `origin/main` HEAD `222d9809`, post-#642) · **PR:** `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`
**Class:** register-hygiene / annotation execution. **NO physics claim minted beyond the registry's pre-verified specs.**
**Brief:** [`_orchestration/2026-07-11_collapse-batch-handoff.md`](../_orchestration/2026-07-11_collapse-batch-handoff.md). **Registry (physics source, post-#637):** [`research/2026-07-10_collapse-target-registry.md`](2026-07-10_collapse-target-registry.md).

This doc executes the fire-ready CLEAN subset the core planning session adjudicated. Every load-bearing receipt was
verified to fire verbatim at HEAD **before** its edit (a 10-target read-only receipt-verification pass; see §Receipt provenance).
`make verify` (KB-metadata + md-links + provenance-stamps + the physics drivers) is **green after every commit** (the commit gate re-runs it).

## Per-target ledger

| Target | Pattern | Action | Status | Commit | Key receipts (verified) |
|---|---|---|---|---|---|
| **T1** | P6 SPLIT | mint quantization-**triad** def-node `def-quant3` + de-broglie KEEP-BOTH pointer | **EXECUTED (mint staged)** | `a1b1768f` | de-broglie-standing-wave.md:181/223("Winding #" hdr)/236; hollow-vortex-binding.md:96; ch8-alpha-golden-torus.md:94; op21:130 |
| **T2** | P1 MERGE | KEEP-BOTH cross-links: "empty" slew catalog ↔ hysteresis-§1 **six-member** family; "slew" label A4-gated | **EXECUTED** | `d649a986` | kernel-catalog:148-152; hysteresis-index §1:49-56 (6 clm, incl #637's clm-p2tp9i); operators.md:137; cross-link ABSENCE confirmed |
| **T5** | P1 de-orthog. | annotate temporal-saturation:331 — θ↔EM-`tan δ` = one phasor (`tan δ=cot θ`); δ_AVE stays the :310 taxonomic bridge | **EXECUTED** | `ba6cac0a` | temporal-saturation-regime-classifier.md:17/32/310/331; θ-owner = orbital-friction-paradox.md |
| **T6** | P6 sector | demote 𝓜-row EE-projection "inductance L" → TKI translation-image (Grant ruling: A1 ownership governs) | **EXECUTED + FLAG-SCAN** | `742e787d` | boundary-observables-m-q-j.md:19; master-equation.md:20; dual-reactance:221; def-portmp/def-tk1xfm; TKI/X_L ABSENCE at :19 confirmed |
| **T7** | P8/P6 | correct the "Cauchy relation" mislabel on K=2G (genuine relation ⇒ ν=1/4); annotation (NOT a def-node) | **EXECUTED** | `8255ba33` | vol1/claim-quality.md:644/662; ch8:13; vol2/claim-quality.md:120 |
| **T8** | P1 deflation | add kernel-coupling **Axis C** (bins 1/2/4 → existing columns); **bin-3 logged GATED on X41** | **EXECUTED (ungated part) · bin-3 GATED** | `23d361f7` | impedance-register-walks_framing.md:15-20/19,24 (#627); lattice-model-register.md:22-26 |
| **T10** | P6 ownership | Q-glyph ownership map (annotation) + fix stale anti-coincidence-test cite (:119-124→:141-146) | **EXECUTED** | `acb930af` | theorem-3-1-q-factor.md:15/147; vacuum-varactor:185/188; test :141-146; op21:10; parametric-coupling:239/213 |
| **T12** | P6 SPLIT | mint `def-u0star` (SYM operating-point vs T-breaking bias) + **X40 homonym FLAG rider** | **EXECUTED (mint staged) · rider = FLAG-not-split** | `1018434e` | ch8:206; fast-sector-settling:155; kernel-catalog:216; common/claim-quality.md:888; op14:91; CLAUDE.md:75; u₀* ABSENCE confirmed |
| **T14** | P6 SPLIT | extend δ-glyph def-node `def-de17a0` with the un-guarded "strain"-word collision (δ_strain ↔ ε₁₁) | **EXECUTED (extension, NOT a new mint)** | `efa6d689` | delta-strain-cosmic-tcc.md:90; temporal-spatial-lattice-decomposition.md:14; vol3/claim-quality.md:59; def-de17a0 |
| **T16** | P6 SPLIT | register-of-registers hygiene note (ledger-index ⊥ impedance-content-bin) | **EXECUTED (annotation)** | `2a276c3e` | impedance-register-walks_framing.md:13,20 |
| **T19** | P6/P1 drift | reconcile the two vol5 conjugate-impedance tables to the solver term; **kill-test FLAGGED** | **EXECUTED + FLAG** | `e57bf045` | translation-protein.md:28; translation-protein-solver.md:20-21; solver-toolchain.md:477 |
| **Precision house rule** | — | land the 5 clauses as RATIFIED in `CONVENTIONS.md` | **EXECUTED (RATIFIED)** | `25c9b2e8` | board Continuation-2 §6 PROPOSED origin; rulings-docket item 15 |
| **δ_strain rider** | — | demote false-precision "2.225×10⁻⁶" prose → "≈2.22×10⁻⁶" (69 sites/36 files); constants.py carries digits | **EXECUTED** | `71aa6e72` | constants.py:279 computes 2.2234e-6 [2018]/2.2228e-6 [2022] |

## Mint-scope (the load-bearing scoping judgment — flagged for the reviewer/Grant)

Per the brief's DELIVERABLES ("Def-nodes minted ONLY where the registry says the mint is staged — T1, T12. Everything else is
annotation / cross-link / hygiene"), **only two new `def-` nodes were minted:** `def-quant3` (T1 triad) and `def-u0star` (T12).
The registry's per-target language for T7 ("register/def-node row") and T10 ("def-Q ownership row") was read **conservatively as
annotations, NOT new def-node mints**, to honor the mint-scope constraint (over-minting is the guarded-against direction):

- **T7** → an inline correction on `vol1/claim-quality.md:644` + a 3-way "Cauchy" homonym caveat in the same claim's Non-Claims (no new def-node).
- **T10** → a "Q-glyph ownership" section appended to `theorem-3-1-q-factor.md` (the Q home leaf) + the stale-cite fix (no new def-Q node).
- **T14** → an EXTENSION of the existing `def-de17a0` (a sub-flag + one `clm-rd9cjm` cross-link), not a new node.
- **T16** → a prose register-of-registers note in `vocabulary-register.md`, not a def-node.

If the reviewer prefers T7/T10 as full `def-` nodes, promoting an annotation to a def-node later is cheap; over-minting is not.

## Flags & gates recorded (flag-don't-fix)

- **T6 flag-scan (0 forbidden cross-wires).** The direct scan for "rest mass IS inductance in the X_L (spin) sector" returned
  **empty**. The "Mass IS inductive resistance" family (`newtonian-inertia-as-lenz.md:12` clm-jwyy6l; `vol2/claim-quality.md:703`;
  `dark-wake-bemf-foc-synthesis.md:29/56`; `ave-bh-horizon-area-theorem.md:71`; `magnetic-saturation.md:48`) is the
  **registry-classified Lenz / TKI-translation-image reading (side a, allowed)** that the T6 annotation covers — NOT the X_L
  flywheel cross-wire the ruling forbids. **Low-confidence watch (surfaced, not fixed):** `newtonian-inertia-as-lenz.md:12`
  frames the inertial reading specifically via "internal magnetic flux / localised μ₀ field / back-EMF" (the μ / X_L-adjacent
  picture) — per the registry this is the allowed side-(a) Lenz translation-image, but it is the one place a reader could slide
  from "translation-image" toward "X_L-sector physics." No edit; Grant's call if it wants the same TKI disambiguation.
- **T8 bin-3 GATED.** Only bins 1/2/4 landed as the kernel-coupling axis; the reactive-static / off-line bin-3 is the **X41
  K1-vs-K2 open fork (PENDING-GRANT, merged #627)** — logged as a gate, NOT resolved ("loads vs transparent" = Re(∮S·dA)≠0 vs =0).
- **T12 rider = FLAG, not split.** The X40 cut/cycle homonym (strain-u₀* T-even ⊥ flux-u₀* T-odd) rides `def-u0star` as a flag.
  X40 returned both components nonzero **only within the matched-bath model** (cut 9/10, cycle 1/10; model-conditional —
  `x40-ring-closure-transient_result.md:328-354`); Grant DEFERRED the split (rulings-docket item 8 = WAIT). No second def-node.
- **T19 kill-test FLAGGED.** Whether the salt bridge is a distinct `+jX/−jX` LC-resonance term or the same conjugate-matching
  term depends on the production `dc_analysis()` internals, which are **NOT visible from this checkout** (no `def dc_analysis` in
  `src`; the solver lives out-of-repo). Reconciling notes point to the solver ground truth `solver-toolchain.md:477`; the label
  question is flagged, not asserted. (Also noted: the solver-toolchain lump-row is physically odd — two hydrophobics should have
  similar, not opposite, reactances — so that grouping may itself be loose.)

## δ_strain sweep — scope & residuals

- **Demoted:** 69 prose sites across 36 LIVE files (KB leaves, `vol_*`/`backmatter` `.tex`, `docs/framing_and_presentation.md`),
  guarded regex `2.225(?![0-9])`; every live site was pre-verified as the δ_strain value (not an unrelated "2.225"). The per-site
  superseded strings are the commit `71aa6e72` diff (git = the KEEP-BOTH audit trail).
- **constants.py** made the authoritative digit-carrier (`:179` comment now `2.2234×10⁻⁶ [2018] / 2.2228×10⁻⁶ [2022]` + a note that
  `DELTA_STRAIN` computes the full double; `:263`/`:275` comments demoted; the computed def line left untouched per the brief).
- **Three residual "2.225" INTENTIONALLY LEFT (logged):** (1) the `DELTA_STRAIN` computed-def trailing comment (brief: untouched);
  (2) `CONVENTIONS.md` precision-rule text, which QUOTES the superseded string to illustrate the rule; (3)
  `src/scripts/vol_3_macroscopic/ft1_delta_strain_eta_epsilon_driver.py:10` — "eta_eps/2 ~ 2.225e-6" is internally-consistent
  derivation arithmetic (4.45e-6/2) in a closed-test (FT-1) driver comment; demoting only the result would break the shown arithmetic.
- **Q2 frozen-snapshot-exempt (NOT edited; logged):** frozen `research/` prereg+result snapshots (~28 files), the machine-generated
  `research/2026-06-11_annihilation-evaporation-run_results.json`, and `research/_archive/L3_electron_soliton/` docs — these record
  historical computed state and are not canonical prose asserting the value. `.index/claims.jsonl` is regenerated, never hand-edited.

## Receipt provenance

A read-only 10-target receipt-verification pass ran against the pinned worktree at `origin/main 222d9809` before any edit: **every
load-bearing receipt fires verbatim; no halts.** All ABSENCE receipts confirmed (T2 cross-link absent; T6 TKI/X_L absent at :19;
T10 no `def-Q`; T12 `u₀*` un-registered). Cosmetic-only notes: T1's op21 `Λ_line=π·d=π` formula sits at `:174` (the `:130` hit is
verbatim); two `\text{}` LaTeX transcription diffs in the registry's own quoting (content identical). The #637 corrections were
re-confirmed live: T2's hysteresis-§1 family is **six**-member (incl. `clm-p2tp9i` at `:56`); the T10 anti-coincidence test is at
`test_graded_vacuum_network_isolation.py:141-146`; T12's `common/claim-quality.md:888` is the **common** (not vol3) file.

## Gates

`make verify` (= KB-metadata + `verify-md-links` + `verify-provenance-stamps` + the physics drivers) is **green at the branch tip**
and was green after each of the 13 commits (the commit interlock re-runs it). `DELTA_STRAIN` value unchanged throughout (only
comments/prose touched, no constants.py code). Adversarial review (M4 wrapper, receipt-fidelity + mint-scope lenses) is the CLEARED gate.
