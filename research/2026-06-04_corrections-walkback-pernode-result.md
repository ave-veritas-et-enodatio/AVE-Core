[↑ Research](index.md)

# Round-2 corrections — CPD walk-back + per-node-conflation sweep + content-anchor (RESULT)

**Status**: RESULT — all three work-items executed + committed. `make verify` (verify-kb-metadata + verify-md-links) PASS.
**Branch**: `analysis/2026-06-04-corrections-walkback-pernode` (off `main`); worktree-isolated (`/tmp/wt-corr-1`). Push, do NOT merge.
**Ledger**: [`_orchestration/experimental/2026-06-04_round2-adjudications.md`](../_orchestration/experimental/2026-06-04_round2-adjudications.md) §2 (#2), §3+§6 (#3), §4 (#4) — all AGREED 2026-06-04.
**Commits**: `f985fe03` (#2), `5c5bea45` (#3), `da4ffb90` (#4).

**Skills fired**: `ave-walk-back` (each corrected claim checked vs its claim-quality.md entry + .index); `ave-sweep-audit` (#3 inventory-first, class-taxonomy, honest-camp template); `consistency-vs-emergence` (CPD = classical-consistency background; PONDER-05 = material consistency-class analog); `verify-before-cite` (every site's current content confirmed before editing + the constants.py drift mapped); `ave-evidence-framing-discipline` (re-scope language precision); `phase-space-coordinate-check` (n/a — these are corrections, not new tests, but the per-node-vs-apparatus distinction IS a coordinate-discipline issue at the field-vs-voltage level).

---

## Work-item #2 — CPD correction (SM ≠ 0.0), Cleave 4-site walk-back

**Finding propagated.** Round-1 Cleave staked its P1 discriminator on *"Standard EM predicts 0.0 mV."* That is FALSE in any real bench: contact-potential-difference (CPD / moving-Kelvin-probe; surface patch potentials) gives a non-zero, polarity-ODD, gap-DEPENDENT charge — the dominant Casimir/Kelvin-probe metrology systematic.

**Corrected statement applied** (4 sites): *"the polarity-odd, gap-INDEPENDENT component is classically 0.0; the raw vacuum charge is NOT — CPD gives a polarity-odd, gap-DEPENDENT (∝ V_CPD/g²) term, separated from the floor by the gap-sweep."* This moves the discriminator from a MAGNITUDE argument (which CPD fakes) to the 4-corner SYMMETRY signature {linear ∧ polarity-odd ∧ material-indep ∧ gap-indep} (which no single classical mechanism fakes). The ξ_topo floor = e/ℓ_node is a pure constant ⇒ gap-INDEPENDENT, so the gap-sweep separates it from the ∝1/g² CPD background.

**Sites touched (4):**
| Site | What it was | Class |
|---|---|---|
| `project-cleave-01.md:22` | "Standard physics dictates… exactly zero electrical charge" (hypothesis) | SM-counterfactual → CPD-corrected |
| `project-cleave-01.md:44` | "Standard EM predicts 0.0 mV" (P1 presence) | SM-counterfactual → CPD-corrected |
| `research/2026-06-03_topological-charge-occupation-robustness.md:95` | "vs SM's 0.0 mV in clean vacuum" (P1/P2 framing) | SM-counterfactual → CPD-corrected |
| `exp-c15-cleave-01-phase-3-measurement-prereg.md:54` | "SM/linear electrostatics → exactly 0.0" (Level-1 binary) | SM-counterfactual → CPD-corrected |

**NOT touched (per directive carve-out + verified same class):** `project-cleave-01.md:65` and `:38`, the prereg Outcome-C line (`:78`), `exp-c15-cleave-01.md:11/19/27`, and `clm-ydksh6` falsification entry (`vol4/claim-quality.md:575`) — these are all **null-result cascade-triggers** ("IF 0.0 mV observed, the framework is falsified"), NOT SM counterfactuals. The cascade-trigger is what happens if the floor reads zero; it is not a claim that SM predicts zero. Left intact.

**Borderline-flag (surfaced, not touched):** the prereg's META-pointers at `:29` ("SM → exactly 0.0 counterfactual") and `:88` ("the SM-0.0 counterfactual") describe the framing as a settled citation. They now point at a corrected claim. They are meta-references (describing what's cited), and the directive scoped exactly 4 substantive sites. Surfaced for the auditor's awareness; not silently extended.

---

## Work-item #3 — per-node-V_yield / apparatus-voltage conflation sweep

**The conflation.** Reading an apparatus (gap) voltage as the PER-NODE ratio. V_YIELD ≈ 43.65 kV is the voltage across ONE node ℓ_node = 0.386 pm — i.e. the yield FIELD E_YIELD = V_YIELD/ℓ_node ≈ 1.13×10¹⁷ V/m — NOT a terminal voltage. The operating point A₀ = V_DC/V_yield = E_local·ℓ_node/V_YIELD is a per-CELL quantity. The 43.65 kV coincidence ("43 kV is bench-reachable!") is exactly why this is the most common Vol 4 reading error (`claim-quality.md:51`).

**Resolution (ledger §6, Grant 2026-06-04).** PONDER-05's "27.4% ε-collapse at V_DC/V_yield = 0.687, 30 kV" is the QUARTZ MATERIAL's voltage-coefficient-of-capacitance (any Class-II ceramic varactor) — a **consistency-class analog of the kernel SHAPE**, NOT a vacuum-kernel falsifier. Reaching A₀ = 0.687 needs 30 kV across 1.0 node-lengths; across real quartz (mm–µm) the vacuum per-node A₀ = 10⁻⁷–10⁻¹⁰ → vacuum-kernel collapse ~0. Appreciable vacuum per-node A₀ needs facility fields (~8×10¹⁶ V/m). The Ax4-cascade is DECOUPLED: a null quartz C(V) effect would falsify quartz dielectric data, not the vacuum kernel.

**Honest-camp template (cited as the model):** `trampoline-framework.md:439` (V_yield^apparatus = E_yield^substrate / G_geom, per Q-G42); `claim-quality.md:51` (V_yield-vs-V_snap + per-node-vs-apparatus discipline); `claim-quality.md:393` (the IMD prediction honestly stated as "depends on the apparatus reaching ~30% of V_yield/ℓ_node ~ 3×10¹⁶ V/m macroscopic field").

### #3 site inventory + classifications

**conflated-fix (re-scoped to consistency-class material analog + per-node note) — 11 KB files:**

| Site | What it asserted | Action |
|---|---|---|
| `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2 | "PONDER-05 … is the canonical bench-scale falsifier of this mechanism" | Re-scoped: material consistency analog of the kernel SHAPE; per-node ratio; facility-field caveat |
| `universal-saturation-kernel-catalog.md:72` | catalog row "27.4% collapse at 0.687, 30 kV" | Re-scoped: material voltage-coefficient row; vacuum per-node A₀ ~ 10⁻⁷–10⁻¹⁰ |
| `measurement-hierarchy-snr.md:66` (+ `:39` pointer) | "IVIM detects 27.4% ε collapse at 0.687, 30 kV" | Re-scoped: quartz material response, not vacuum-kernel; per-node note |
| `op14-local-clock-modulation.md:106` | "quartz at 0.687 → 27.4% slowing — falsifies if c_eff doesn't track kernel" | Re-scoped: material C(V)-arc shape, consistency-class; **path-corrected** (IVIM inventory mis-pathed as `common/op14-…`; canonical is `vol4/circuit-theory/ch1-vacuum-circuit-analysis/`) |
| `translation-circuit.md:111/191/481` | varactor + voltage-coefficient rows "PONDER-05 canonical bench tester at 0.687" | Re-scoped: `:481` is literally the Class-II-ceramic voltage-coefficient row → PONDER-05 IS that material coefficient, not a vacuum tester |
| `divergence-test-substrate-map.md:126` (B7 body) + `:466` (B7 matrix row) | "30 kV holds quartz at 68.7% V_yield … null at 68.7% V_yield falsifies Ax4 directly (F)" | Re-scoped: consistency-class; regime II↔III → consistency-class; **F → U-C**; Ax4 cascade DECOUPLED from B1/D4/C9 |
| `dual-reactance-storage-taxonomy.md:31` | V_DC row parenthetical "PONDER-05 at 0.687" | Re-scoped: A₀ is per-node; PONDER-05 = quartz voltage-coefficient |
| `vol9/ch5-ac-electrical-characteristics/index.md:35` | "PONDER-05 … canonical bench-scale falsifier of the operating-point mechanism" | Re-scoped: material consistency analog; facility-field caveat |
| `vol9/ch15-falsification-tests/index.md:25` | "PONDER-05 … bench-scale kill-switch at 0.687" | Re-scoped: consistency-class material analog, NOT a vacuum kill-switch; Ax4 cascade decoupled |
| `vol9/ch7-saturation-characteristics/index.md:11` (+ `:23` pointer) | chapter-intro "(5) the PONDER-05 bench-scale falsifier at 0.687" | Re-scoped: material consistency analog of the kernel SHAPE; per-node note |
| `vol9/ch4-dc-electrical-characteristics/index.md:44` | Ch.7 cross-ref pointer "PONDER-05 bench-tester at 0.687" | Re-scoped: consistency-class material varactor analog |

**Conflation-site count: 11 conflated-fix KB files** (the directive's known-sites list — measurement-hierarchy, kernel-catalog, translation-circuit×3, op14, divergence-map×2, INVARIANT-S2 — all verified + extended to the vol9 datasheet index echoes of INVARIANT-S2 + the dual-reactance taxonomy row).

**honest-leave (cited as the template, unchanged):** `trampoline-framework.md:439`; `vol4/claim-quality.md:51`; `vol4/claim-quality.md:393`. Q-G42 result (V_sign harden) is the worked honest-camp instance.

**borderline-flag (surfaced, NOT edited — separate blast-radius adjudication required):**

1. **Phase 2-NA aperture-aggregate edifice** — `parametric-coupling-kernel.md` §13/§14 (lines 458/470/540/542/548/570/603), `dama-matched-lc-coupling.md:269`, `_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md`, `research/2026-05-26_ax4-saturation-phase-{0c,2-na}-*`. This is a CLOSED Class-2-emergence sub-epic (κ₃/κ₄ amplitude-shape prediction) that ANCHORS on "PONDER-05's V_DC/V_yield = 0.687 at 30 kV is canonical evidence operating-point loading is achievable AND testable" (`ax4-saturation:38/45/323`). The per-node math (a = V_DC/A_c, parametrized by the dimensionless operating point) is internally correct; but the ANCHOR inherits the conflation — if reaching a = 0.687 needs 30 kV across 1.0 node-lengths, PONDER-05 is NOT bench-evidence that 0.687 is vacuum-achievable; it's evidence the QUARTZ hits 27.4% ε-collapse (its own coefficient). Re-scoping a closed Class-2-emergence claim is a separate adjudication (Rule 6 / Rule 11 — do not silently deflate a closed emergence headline). **The Phase 2-NA peak a^(2D) = 1/√2 = 0.707 "within 3% of PONDER-05's 0.687" alignment narrative is the load-bearing exposure** — if PONDER-05's 0.687 is a material-not-vacuum operating point, the "convergent operating-point selection is structural evidence" framing (`ax4-saturation:323`) needs re-examination.

2. **Regime-map taxonomy** — `experimental-design-space.md:23` ("HV Capacitor @ 30 kV → r = 0.687 → Regime II"), `domain-catalog.md:27`, `07_regime_map.tex:127/315/356` (incl. a Vol 1 textbook EXERCISE asking students to compute the error "where r ≈ 0.687"), `14_phase_diagrams.tex:64`. SAME conflation (terminal voltage read as the per-node r). **Load-bearing internal contradiction surfaced:** `14_phase_diagrams.tex:64` (the "Applied voltage V" row) gives "Lab capacitor 1 kV → r = 0.023" while `:65` (the "Local field E" row, same table) gives "Lab field 1e6 V/m → r ~ 10⁻¹¹" for the SAME apparatus (a 1 kV cap over a mm gap IS ~1e6 V/m). Row :65 is the HONEST one (per-node field); row :64 is conflated (terminal-voltage-as-per-node). Re-scoping the regime-map cascades into the four-regime worked examples + the textbook exercise + the vol_9 datasheet phase-diagram (the latter in another implementer's `15_falsification_tests.tex`-adjacent territory). Flagged per Rule 6; larger blast radius than the directive's scope.

3. **`.tex` source echoes** — `backmatter/07_universal_saturation_kernel.tex:107`, `vol_3_macroscopic/chapters/04_generative_cosmology.tex:364`, `vol_9_vacuum_datasheet/chapters/15_falsification_tests.tex:23/31/41/232` still carry the conflated PONDER-05 framing. The vol_9 `15_falsification_tests.tex` is another implementer's carve-out (WORK-ITEM 3 directive). The KB (.md) distillations are corrected; the .tex sources they distill from need a follow-up alignment pass (or the other implementer folds it).

**Coincidental collisions (verified NOT the conflation — left untouched):** the Beryllium IE-correction chain k_eff = 0.754/(1.454)^¼ = 0.687 (`hierarchical-cascade-correction.md:45`, `period-2/beryllium/ionization-energy-correction.md:16`, `vol6/claim-quality.md:103`, multiple .tex); the PREM Moho impedance Z = 27.4 (`prem-layers-waveguide.md:17/26`). Numeric coincidences, unrelated to V_DC/V_yield.

---

## Work-item #4 — content-anchor constants.py cites

**Convention adopted (ledger §4):** cite the SYMBOL (`XI_TOPO`), not the line. `src/ave/core/constants.py` has DRIFTED substantially — of the 7 head-sweep lines, only `:133` (ALPHA) still resolves to its symbol; the rest now point at comments/blanks:

| Symbol | Cited (stale) line | Current line |
|---|---|---|
| ALPHA | :133 | 133 (still correct) |
| C_0 | :78 | 95 |
| MU_0 | :79 | 96 |
| EPSILON_0 | :80 | 97 |
| L_NODE | :194 | 239 |
| XI_TOPO | :246 (was :205) | 251 |
| V_SNAP | :333 | 378 |
| V_YIELD | :342 | 387 |
| R_I | :402 | 407 |
| XI_MACHIAN | :432 | 516 |
| RHO_BULK | :619 | 624 |

**(a) ξ_topo lockstep** — the 3 `:246` cites, content-anchored to `XI_TOPO`. Because the citing tables also carried adjacent stale constants (the α-free provenance table in the bijection-result cited L_NODE/V_SNAP/V_YIELD at stale lines too), the WHOLE table was content-anchored in lockstep (fixing 1 of 4 while leaving 3 stale would be incoherent):
- `research/2026-06-04_alpha-class2-bijection-result.md:168–171` (L_NODE/XI_TOPO/V_SNAP/V_YIELD)
- `research/2026-06-03_topological-charge-occupation-robustness.md:20` + `:120`

**(b) High-traffic head-sweep** — :133/:79/:619/:432/:333/:194/:78 + the ranges (:78-206, :79-80). Grepped each cite, looked up the CURRENT symbol, rewrote `constants.py:NNN` → the symbol. **0 head-sweep-line cites remain in the active corpus.** Markdown-link cites: display text re-anchored, link target preserved (verify-md-links PASS, EXIT 0). Files: `divergence-test-substrate-map` (:133×5, :619×2), `claim-quality-closure-roadmap`, `project-roentgen-03`, `open-source-hardware`, `op21-multi-mode-mode-counting`, `vol9/ch2`, `vol9/ch5`, `vol1/claim-quality` (clm-zuf7g1 rationale), `vol_9` datasheet .tex (02/05/08/10/16), 8 research/orchestration docs, `coldfusion_eta_x_curve.py`.

**SKIPPED (directive carve-out — another implementer owns):** `claim-quality.md:387`, `vacuum-birefringence-e4.md`, `12_falsifiable_predictions.tex`, `15_falsification_tests.tex`.

**LEFT (self-healing tail per ledger §4):** ~146 scattered singleton `constants.py:NNN` cites at OTHER line numbers (:96/:98/:152/:301/:497/:580/:660/:733/:760/:770/etc.). A stale singleton is a 10-sec re-grep; the head-sweep covered ~50% of exposure via ~7 lines. `_orchestration/_archive/` h-infinity `:432` cites left frozen (archived).

---

## Verification

- `make verify` (= `verify-kb-metadata` + `verify-md-links`) **PASS** after `make refresh-kb-metadata` (the refresh rewrote 2 `.index` lines — the content-hash for `clm-zuf7g1` whose rationale was content-anchored; counts unchanged 327/327, 637/637).
- `verify-md-links` EXIT 0; no NEW broken links from any edit (the broken-inter warns are all pre-existing cross-repo references).
- `coldfusion_eta_x_curve.py` syntax verified after print-string edits.
- `git branch --show-current` confirmed `analysis/2026-06-04-corrections-walkback-pernode` before every commit.

## What stays open / for the auditor + Grant

- **#2:** the 2 prereg meta-pointers (`:29`, `:88`) now describe a corrected claim — borderline, surfaced not extended.
- **#3:** the two borderline blast-radius items (Phase 2-NA emergence anchor; regime-map taxonomy + the `14_phase_diagrams.tex:64`-vs-:65 internal contradiction) are SEPARATE adjudications, NOT folded into this sweep. The .tex source echoes (incl. the carved-out `15_falsification_tests.tex`) need a follow-up alignment pass.
- **#4:** the ~146-cite self-healing tail is by-design out of scope; if a hook/tracker is ever wanted, that is the trigger machinery the ledger §4 judged overkill for cosmetic debt.
