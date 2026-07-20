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

| Class | Fixed | Ledgered (flag-don't-fix / observation) | APPLY-POST-#738 |
|---|---|---|---|
| C1 mechanical hygiene | 10 links + 2 index rows = **12** edits across 9 files (C1-A links ×10, C1-index ×2 rows) | 6 orphan leaves + 3 no-H1 leaves + `clm-9oazz0` phantom + 2 CONVENTIONS observations | claims.jsonl (fenced) untouched — `clm-9oazz0` routed |
| C2 propagation-lag drift | **3** dated Rule-12 notes (photon-identification RULING-21; cosmology/index deep-space tag; retention-transition-split #735) | `nonlinear-vacuum-capacitance.md:66` (fork-side); vol3/index.md:63 (bare ToC) | 4 (engine-capability-map §8c.10 arm-result; tau-relax-derivation caveats ×2; substrate-hysteresis-index; #59 archive) |

**Fixed files (9):** `photon-identification.md`, `vol3/cosmology/index.md`, `retention-transition-split.md`, `claim-quality-closure-roadmap.md`, `baryon-mass-predictions.md`, `vol4/.../ch14-.../theory.md`, `torus-knot-uniqueness.md`, `q-g19a-petermann-saliency-closure.md`, `vol9/ch11+ch13 index.md`, `vol4/falsification/ch12-.../index.md`. (Plus the ledger.)

---

## COLLISION FENCE — PR #738 (open, under review)

Do NOT edit these files; findings on them go here tagged **APPLY-POST-#738**:
`manuscript/ave-kb/.index/claims.jsonl`, `common/claim-quality.md`, `common/dark-wake-bemf-foc-synthesis.md`, `common/engine-capability-map.md`, `common/substrate-hysteresis-index.md`, `common/trampoline-analogy-primer.md`, `vol3/cosmology/ch05-dark-sector/effective-galactic-acceleration-mond.md`, `vol4/circuit-theory/ch1-vacuum-circuit-analysis/tau-relax-derivation.md`, plus `_orchestration/2026-07-10_rulings-docket.md`, `_orchestration/2026-07-15_hardware-ratings-map.md`, `research/_archive/L3_electron_soliton/59_memristive_yield_crossing_derivation.md`.

### APPLY-POST-#738 findings

_(populated during sweep)_

---

## CLASS 1 — MECHANICAL HYGIENE

### C1-A · Broken markdown links (FIXED 10; 70 out-of-scope residue characterized)

**Method:** wrote a KB relative-link resolver (`scratchpad/check_kb_links.py`) — parses `[text](target)` links across all 802 KB `.md` files (skips http/mailto/anchors/`{}`-templates and the `tools/` test-fixture tree), checks each target file exists. 6784 links checked; 80 broken → 70 after fixes.

**FIXED (8 file:line-in-href anomalies + 2 depth errors = 10 links across 7 files):**
- The KB convention is line-in-LABEL, plain-file href (781 backtick cites; e.g. `[`q-g19a-...:108`](...q-g19a-...md)`). A rare minority (10) leaked the `:NN` into the href too → non-resolving. All target files verified to exist with valid line counts. Fixed by dropping `:NN` from the href (label keeps the line): `claim-quality-closure-roadmap.md` (×4: topological-fractionalization.md:6 ×2, constants.py:680, riemann-hypothesis.md:52), `vol4/.../baryon-mass-predictions.md:12` (constants.py:733), `vol4/simulation/ch14-.../theory.md:43` (topological:6), `vol2/.../torus-knot-uniqueness.md:112` (topological:6), `vol2/.../q-g19a-petermann-saliency-closure.md:115` (topological:6).
- **vol9→tex depth errors (2):** `vol9/ch11-topological-characteristics/index.md:38` + `vol9/ch13-application-examples/index.md:67` used `../../../../vol_9_vacuum_datasheet/...` (up 4 = repo-root) → target is under `manuscript/` (up 3). Fixed to `../../../`. Both `.tex` targets verified present.

**70 remaining broken — ALL out-of-scope (characterized, NOT fixed):**
- **22 cross-repo cites** (`../../../../../../AVE-QED/...`, `AVE-HOPF/...`, `AVE-Tangents/...`) — correctly-formed pointers into sibling repos under `AVE-staging/` (verified depth: e.g. flyby-anomaly leaf's 6-up reaches `AVE-staging/AVE-QED`). Resolve in Grant's workspace layout; not broken there. Per workspace cross-repo citation rules.
- **20 template/example placeholders** in `CONVENTIONS.md` / `CLAUDE.md` / `README.md` / `.index/SCHEMA.md` (`../index.md`, `path.md`, `relative/path/to/target.md`, `<rel-path>`) — documentation syntax examples, NOT real links. CONVENTIONS.md §Auditing explicitly lists these as known false positives.
- **9 asset PNGs** in `common/trampoline-framework.md` (`../../../assets/sim_outputs/trampoline_framework/*.png`) — `assets/sim_outputs/` is not committed (only `src/scripts/trampoline_framework` exists); generated-figure output dir. Cannot fix (can't create assets); left for the figure-generation lane. LEDGERED.
- **19 in `session/axiom-homologation.md`** — a DEPRECATED archive doc carrying its own banner: *"moved to session/ to preserve its content for evaluation until it can be deleted ... DO NOT MAKE SWEEPING CHANGES."* Stale relative paths from when it lived under `common/`. Not fixed (churn against a to-be-deleted doc). LEDGERED.

---

## CLASS 2 — PROPAGATION-LAG DRIFT

### C2-A · RULING-21 Op3 = LOSSLESS TRANSDUCTION residual (FIXED — pure propagation)

**Ground truth:** RULING 21 (docket `_orchestration/2026-07-10_rulings-docket.md:1809`) — Op3's $A_1$ behaviour is LOSSLESS TRANSDUCTION (mode-projection loss ≠ system loss). Tier-1 batch fixed 3 leaves (`k4-port-irrep-decomposition.md`, `substrate-native-terminology.md:27/:31`, `retention-transition-split.md:47`). Brief: "find any others."

**Sweep method:** `grep -rl "Op3"` → 40+ leaves; filtered to Op3-near-loss/dissipat within 80 chars; each read for transduction-correction presence.

**Already-current (verified carry the RULING-21 note):** `k4-port-irrep-decomposition.md` (owning leaf, :28 row + §4 :109 RULED block + :199 blanket note), `substrate-native-terminology.md` (:31 🟢 RULED), `retention-transition-split.md` (:47 🟢 RULED), `common/index.md` (:68 already "common-mode-rejection worked example"), `vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md` (:102-104 already cites RULING 21), `translation-circuit.md:188` (already "Axiom 3 — reactive, not loss"), `biquaternion-...-network-equations.md:224` (already "lossless reactive boundary (Op3/Op14 wall)").

**RESIDUAL FIXED — `vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md`.** Carried the exact superseded wording at 6+ sites (line 11 "dissipates monotonically"; §1 scope-note :38 "$A_1$ monotonic dissipation (Op3)"; Primary xref :49 "Op3 asymmetric-dissipation mechanism"; §3 :82 "$A_1$ ... loses energy monotonically" / "asymmetric dissipation"; §2 :86/:120 "$A_1$ exactly/fully dissipated"; See-also :252 "Op3 dissipation"). Applied a dated 🟢 RULING-21 reading-note (after the G2 banner) mirroring the owning leaf's blanket-note pattern: read all as lossless transduction (mode-emptying into $T_2$; system conserves power); wording preserved unedited (Rule-12). **Zero-judgment:** RULING-21 is unambiguous + already executed on the owning leaf; this is consumer-leaf propagation, not adjudication.

### C2-B · Deep-space reactive-bulk demotion completeness (#733) — COMPLETE on leaves; 1 index residue FIXED, 1 ledgered

**Ground truth:** `research/2026-07-19_deep-space-reactive-bulk-walk_RECORD.md` + docket continuation (2026-07-19) — the topological-Joule-stall / resistive-deep-space-metric mechanism (asteroid-belt/Oort stall, lunar 1.04 TW) is DEMOTED (Ax3-forbidden bulk resistor); band-map re-derivation SPEC'd not run. Dark-matter added-mass reading SURVIVES (scope-fenced).

**Verified COMPLETE (leaves + registers carry 2026-07-19 demotion banners):** `vol1/.../magnetic-saturation.md:34` (comprehensive banner covering the whole belt/Oort subsection incl. preserved :36/:42 "resistive deep-space metric" body; dark-matter :30 survivor scope-fenced), `vol3/cosmology/ch14-orbital-mechanics/lunar-inductive-heating.md`, `vol4/.../boundary-trapping-test.md`, `vol4/.../advanced-protocols.md` (Protocol 10), + `vol3/claim-quality.md`, `vol1/claim-quality.md`, `vol4/claim-quality.md`. Key Results table rows in `vol3/index.md:52`, `vol3/cosmology/index.md:31`, `vol3/cosmology/ch14-orbital-mechanics/index.md:21,:33` all DEMOTED-tagged.

**RESIDUE FIXED — `vol3/cosmology/index.md:40`** (Ch.14 Derivations-and-Detail description quoted "lunar inductive heating ($P_{topo} \approx 1.04$ TW)" as a chapter headline WITHOUT the demotion tag its sibling Key Results row at :31 carries). Added a compact "🔴 mechanism DEMOTED 2026-07-19" pointer. Zero-judgment (sibling row in same file already tagged).

**RESIDUE LEDGERED (deliberate leave) — `vol3/index.md:63`** — the Cosmology-volume flavor blurb names "lunar inductive heating" in a long parenthetical topic-list with **no number and no result-claim**; it is a pure table-of-contents pointer. The load-bearing Key Results row at :52 (same file) IS DEMOTED-tagged, and the chapter index + leaf carry the banner. Left untagged (a mid-parenthetical tag would be clumsy and the load-bearing cells are covered); recorded here for completeness.

**No other deep-space drift:** vol4 "stall" hits (`applied-telemetry.md:14` aerodynamic-stall analogy; `autoresonant-helicity.md:14` / `autoresonant-dielectric-rupture.md:12` "cascade stalls" = Duffing detuning) are unrelated to the demoted bulk mechanism. `oort-cloud-saturation-boundary.md` = the reactive saturation-boundary sibling (SURVIVES).

### C2-C · Memristive loop-area (#735 yield-fork discriminators) — 1 pure-propagation FIX; 1 flag-don't-fix; primary caveats APPLY-POST-#738

**Ground truth:** `research/2026-07-19_yield-fork-discriminators_result.md` (#735) — Leg B (memristor loop-area, `P_phase5`, host `tau-relax-derivation.md:109`) = NEITHER; the (r,S)-plane window test is INFORMATION-FREE (peak pinned at linear Debye ≈1.00 for any first-order kernel); the (V,I) plane peaks INSIDE the window at ωτ=0.911; the `[0.85,0.95]` window was MIS-REGISTERED (imported from doc-48's `A²_cos`); F-B3 the finite ∮'s *dissipative* character is ASSUMED by the first-order model, not measured; fork stays OPEN, crux relocated to `#59` Flag F. NOT "P_phase5 falsified."

**FIXED (pure propagation) — `common/retention-transition-split.md`** (the open-yield-fork row at :63). The prose said "resolution is by the registered discriminators (audit §5)." Added a dated status note: the discriminators RAN (#735); Leg A = B (two-τ thixotropic sub-branch closed by derivation), Leg B = NEITHER; neither adjudicates against Grant's lean; crux RELOCATED to #59 Flag F (a derivation, not a driver); fork STAYS OPEN; "do not bank either way" unchanged. **Zero-judgment:** does not touch the ruling or Grant's lean — records the merged fact that the named resolution-path relocated. Fork remains OPEN.

**FLAG-DON'T-FIX (routed to Grant/auditor) — `vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md:66`.** The leaf asserts the dissipative reading as settled; correcting it takes a side of the OPEN fork. NOT edited.
> **Leaf side (`nonlinear-vacuum-capacitance.md:66`, verbatim):** "Under high-frequency AC topological stress, the memristive vacuum produces a classic **Pinched Hysteresis Loop**: the $V$–$I$ Lissajous figure passes through the origin but encloses a finite area proportional to the energy **dissipated** during each thixotropic yield–heal cycle."
> **Ground-truth side (#735, verbatim):** F-B2 — "the (V,I) 'pinched hysteresis' registration does not apply at the near-yield point. `nonlinear-vacuum-capacitance.md:66` registers a Lissajous that 'passes through the origin.' At `r_0=0.7, Δr=0.3` the drive `r∈[0.4,1.0]` **never crosses `r=0`**, so `min|I|=0.354 ≠ 0` → the loop is **offset, not origin-pinched**." F-B3 — "the finite `∮` is a **rate-dependent Debye lag** ... **the finite `∮` alone does not require a resistor.** Its *dissipative* reading is inherited from the **first-order overdamped** model structure ... which `#59` §12 **Flag F** flags as *asserted, not derived*." Fork OPEN; Grant leans reversible-reactive.
> **Routing:** the auditor lands the coordinated caveat here together with the FENCED `tau-relax-derivation.md` primary caveat (below) post-#738; the origin-pinch does not apply at the near-yield operating point, and the "dissipated" character is model-assumed not measured. Do NOT resolve the fork.

### APPLY-POST-#738 (memristive loop-area — owed corrections on FENCED files)

Per #735 "owed to auditor lane" (result §6 + docket continuation 2026-07-19). All three are on FENCED files:
- **`vol4/circuit-theory/ch1-vacuum-circuit-analysis/tau-relax-derivation.md`** (FENCED — PR #738). Owes: (i) the P_phase5 **BOTH-AND demotion (R-2), NOT "falsified"** caveat on `:109`-area — the (r,S) window test was information-free AND the `[0.85,0.95]`/`0.9` window was mis-registered (imported from doc-48's `A²_cos`; `#59` Eq 6.3 yields `~0.954–0.978` at the registered drive, not `0.9`); the one testable plane (V,I) landed INSIDE the mis-registered window at `0.911`. (ii) the **doc-staleness flag** at `:117` — "dynamic Level-2 `S(t)` ODE unbuilt" is STALE (engine built it via `use_memristive_saturation`, `k4_tlm.py:266–296`).
- **`common/substrate-hysteresis-index.md`** (FENCED). Any memristive-loop / hysteresis-row that registers the loop-area as a confirmed/open dissipative prediction owes the #735 fork-OPEN / crux=Flag-F context. (Ledger-only pending #738; also carries the separate #733 clm-exjfai/moving-front residue per the branch-scrub follow-up — see NOT-SWEPT.)
- **`research/_archive/L3_electron_soliton/59_memristive_yield_crossing_derivation.md`** (FENCED — the `#59` source). Owes: §10/§28 "unbuilt" staleness flag + the Flag-F relocation context (auditor lands).

### C2-D · Noise-floor arrow + counting-arrow / #724 meter-validity — NO non-fenced KB drift; 1 APPLY-POST-#738

**Ground truth:** `research/2026-07-19_f6-thermal-floor-arm_result.md` tri-form verdict (STRONG floor-arrow excluded ~5σ; reactive-floor mechanism structurally inexpressible; partial unconstrained; ARROW QUESTION stays OPEN; bare NO-SUPPRESSION label DEGENERATE). #724 flipped the meter to VALID[0.030,0.030]; #727 INSTRUMENT-INCOMPATIBLE. `noise-floor-arrow-walk_RECORD.md` mints NOTHING new canon.

**Verified: NO non-fenced KB leaf carries the drift.** Two-method (regex + `grep -F`): zero hits for "NO-SUPPRESSION" / "ride-on-top" / "floor sets the arrow" / decided-counting-arrow / "meter invalid at κ" / "sweep BLOCKED" outside the FENCED `common/engine-capability-map.md`. The F6-program leaves that DO exist are consistent with ground truth: `thermal-phase-registers.md` (§2/§6 "temperature = phase-diffusion width RE-GATED on the unbuilt F6 irreversible ε→T2 depletion channel; a lossless kernel gives only bounded reversible dephasing") is CORROBORATED by the arm (which found exactly bounded reversible dephasing on a lossless bath) — no edit; `dark-energy-latent-heat-definition.md` (F6 = UNBUILT DE-tracks-matter chord) unchanged by the arm; `identity-break-test-design.md` / `cmb-thermal-attractor.md` reference the F6 tier-1 charter (Γ=3Hρ_latent), not the counting/floor arm.

**FENCED engine-capability-map.md §8c** is itself current up to the arm-in-flight point: §8c.7/§8c.9 correctly say "counting-arrow QUESTION OPEN"; §8c.3/§8c.6 carry the #726/#724 corrections; §8c.8 correctly softens DOS-balance to RECOMMENDED-not-RULED and marks it MOOT; §8c.10 records the thermal-floor arm as **"in flight"** (pre-result).

**APPLY-POST-#738 (`common/engine-capability-map.md` §8c.10):** the section records the thermal-floor arm as in-flight; the arm has since FIRED and was re-banked post-review to the **tri-form verdict** (`research/2026-07-19_f6-thermal-floor-arm_result.md`): (a) STRONG floor-arrow EXCLUDED ~5σ, (b) reactive-floor arrow mechanism STRUCTURALLY INEXPRESSIBLE (identity-class, #721-W2 shape), (c) mild ≤~30% partial UNCONSTRAINED; the bare **"NO-SUPPRESSION" tree label is DEGENERATE** (interior clips to 0; verdict decided by artifact residuals); **ARROW QUESTION stays OPEN** (interacting-bath thermalization + X40-class click = the open candidates, SPEC only). The auditor appends this arm result to §8c (a new §8c.11 or §8c.10 tail) once #738 lands. NB: the FENCED docket ENTRY 21 (`_orchestration/2026-07-10_rulings-docket.md:2006-2022`) carries the **pre-review "NO-SUPPRESSION (FLOOR-ARROW falsified)" framing**, superseded by the tri-form re-bank — a coordinated APPLY-POST-#738 reconciliation for the orchestrator/auditor (docket is fenced; not a KB leaf).

### C2-E · Retention/transition conflation (Regime-IV audit) — VERIFIED COMPLETE, no residual drift

**Ground truth:** `research/2026-07-17_regime-iv-dissipation-audit.md` + governing split leaf `common/retention-transition-split.md`. Brief: fix conflation (persistence-of-latched-state vs irreversibility-of-crossing) in leaves the audit marked, where the split leaf now governs.

**All audit-marked conflation/tension sites already carry dated notes (verified):**
- **F1 plastic-row** — `common/substrate-native-terminology.md:50` carries the "Audit per-sense note (2026-07-17, §F1)" overturning the row's license to RETENTION-ONLY (retained-set sense licensed; friction-sense = open fork). CURRENT.
- **F4 Op3** — RULED (see C2-A); `k4-port-irrep-decomposition.md`, `substrate-native-terminology.md:31`, `retention-transition-split.md:47`. CURRENT.
- **F5 deep-space** — DEMOTED (see C2-B). CURRENT.
- **BH erased-vs-conserved** — `vol3/cosmology/ch04-generative-cosmology/black-holes-impedance-mismatch.md:24-26` carries a dated "🔴 FLAG (2026-07-19, Tier-2.5 hygiene — flag-don't-fix)" recording the "mass-energy conserved as latent heat (PRODUCT) but information permanently erased (TRANSITION)" one-sentence conflation and routing it to the generative-cosmology / BH-interior lane (audit §F5, item #105/#244). Body UNTOUCHED, NOT adjudicated. CURRENT (judgment item, correctly flagged not fixed).

The 49 RETENTION-ONLY audit items were adjudicated clean (correctly PRODUCT-moment lossless — no conflation to correct). **No residual retention/transition drift found.**

---

## Orphan / phantom index lists

### Phantom rows (index links a leaf that does not exist)
**NONE in-KB.** Phantom rows surface as broken links; the broken-link scan (C1-A) found zero in-KB missing-leaf targets (all 70 residual broken links are cross-repo / template / uncommitted-asset / deprecated-archive). Index→leaf integrity is clean.

### Orphan leaves (exist + cross-referenced, but NOT listed in any `index.md` table)
Method: `scratchpad/check_orphans.py` (0 truly-orphaned — every leaf is linked from *somewhere*) + a stricter `check_indexed.py` (referenced by an `index.md` specifically). 8 leaves are cross-referenced by siblings but absent from any index table:

**ADDED index rows (2 — unambiguous canonical ch12 prediction leaves, siblings of already-indexed leaves):**
- `vol4/falsification/ch12-falsifiable-predictions/vacuum-photon-photon-channel.md` (clm-gg4wmx, path-stable "FOURTH testable consequence", sibling of the indexed `vacuum-birefringence-e4.md`) → added to the ch12 Benn Derivations table with a faithful one-line description from the leaf's own "What this leaf is" summary.
- `vol4/falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md` (clm-k4d4ph, the weak-C surviving forward prediction, CONSISTENCY/FORM-class) → added to the same table.

**LEDGERED (6 — NOT auto-indexed; special-class docs or status-adjudication needed, per "only add rows where unambiguous"):**
- `common/engine-capability-map.md` — FENCED content; a whole-engine "map" doc (like a sidecar/register), widely cross-referenced; index-membership for a map-class doc is a judgment for the auditor. NOT added.
- `common/numerical-provenance-manifest.md` — a "manifest" artifact (special-class), not a standard content leaf.
- `common/dual-reactance-storage-taxonomy.md` — a taxonomy leaf (title: "V_TOROIDAL_HALO = 2 is a reactance-sector COUNT, not a volume"); candidate common/index add but the correct Key-Results-vs-Derivations placement + description is judgment.
- `vol4/circuit-theory/ch1-vacuum-circuit-analysis/unified-engine-design-doctrine.md` — a "doctrine" doc (special-class; also **lacks an H1 heading** — see CONVENTIONS note below).
- `vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md` — a vol4 circuit operator leaf (Op21 at the Γ=−1 boundary); plausible ch1-circuit-index add but status/description need auditor verification.
- `vol1/axioms-and-lattice/ch1-fundamental-axioms/single-substrate-scale.md` — a vol1 ch1 foundational leaf (also **lacks an H1 heading**); plausible ch1 index add, but a foundational-axiom leaf's index placement + description warrants care.

**CONVENTIONS observation (not fixed — ledgered):** three leaves deviate from the "leaf begins with an H1 `# Title`" convention — `single-substrate-scale.md` and `unified-engine-design-doctrine.md` (no `#`/`##` title found by grep) and `k4-bloch-dispersion-quartic.md` (uses `## ` H2, not `# ` H1). Not corrected (heading-level changes can break external section-anchor cites; low-value; routed to the auditor with the orphan-index adjudication).

### C1-B · Claim-id cross-check (prose ↔ `.index/claims.jsonl`)

Method: extracted all `clm-[a-z0-9]{6}` ids from prose (345 distinct) vs `.index/claims.jsonl` (322 clm- + `axiom-*`/`ilk-*`/`def-*` framework ids). Direction B (index-claim never referenced in prose) = **0**. Direction A (prose ref not in index) = 23, of which 20 are non-issues:
- **18 documentation placeholders** (`clm-111111`, `clm-222222`, `clm-aa1111`..`clm-hh8888`, `clm-co1111`, `clm-sb1111`..`clm-sb7777`, `clm-xxxxxx`, `clm-zzzzzz`) — live only in `CLAUDE.md` / `.index/SCHEMA.md` / `claim-quality.md` example rows / `tools/tests/fixtures/` — format illustrations, not references. Out of scope.
- **`clm-ground`** — a false extraction (first 6 chars of the metadata field name `clm-grounded`), not a claim id.
- **`clm-trf3bd`** — a deliberately-RETIRED position, correctly absent from the index: `vol1/claim-quality.md:12` reads "superseding the former `clm-trf3bd` real-space-trefoil-body position, **which is retired**"; also a query-API example in `.index/SCHEMA.md`. No action (correct as-is).

**FLAG-DON'T-FIX (routed to auditor) — `clm-9oazz0` is a genuine PHANTOM claim-id.** Cited in **3 vol9 index leaves** (`vol9/ch19-calibration-justification/index.md:26`, `vol9/ch12-cosmological-characteristics/index.md:50`, `vol9/ch13-application-examples/index.md:22,:44*,:57`) as the canonical id for `common/full-derivation-chain.md`'s Machian-G / zero-parameter content — but it exists NOWHERE: not in `full-derivation-chain.md`'s frontmatter (which declares `claims: [clm-sxn6eo, clm-ibfyda]`), and 0 hits in `.index/claims.jsonl`. The correct replacement is **ambiguous** because the phantom is cited for a *mix* of content spanning three real ids:
> - `clm-sxn6eo` — "Mathematical Closure Status — 'Structurally Zero-Parameter,' Not Absolutely" (matches ch19:26 "From Three Limits to Zero Parameters; 26→{m_e,α,G} reduction");
> - `clm-ibfyda` — "Full Derivation Chain — Acyclicity and Identified Methodology Disclosures";
> - `ilk-gravmb` — "G ← Machian-boundary-impedance termination (Achromatic-Lens far-field)" (matches ch12:50 / ch13:57 "closed-form $G=\hbar c/(7\xi m_e^2)$; gravity as Machian boundary impedance").
> **Tell:** `vol9/ch13-.../index.md:44` correctly cites `ilk-gravmb` for the same Machian-G MIXED ruling, while `:22`/`:57` cite the phantom `clm-9oazz0` — an internal inconsistency in the same file, suggesting `clm-9oazz0` is a stale/mis-minted id. Per-citation the right id is likely `ilk-gravmb` (the Machian-G rows) or `clm-sxn6eo` (the zero-parameter-closure row), but which-per-row is a judgment the auditor should adjudicate against the claim register. **NOT fixed** (the vol9 index leaves are editable, but the replacement id is ambiguous and load-bearing — Machian-G / G-ruling `ilk-gravmb` MIXED). Routed to auditor.

### C1-C · CONVENTIONS.md compliance — CLEAN (2 observations ledgered)

Machine-checkable invariants all PASS:
- `## Resultbox:` heading-form: 0 real hits (the 1 grep match is CONVENTIONS.md:355 documenting the check command itself).
- `leaf: placeholder`: 0 real hits (the 1 match is CONVENTIONS.md:360, the check-command doc).
- Bootstrap directives (`⛔ **Bootstrap`): PRESENT on entry-point.md + all volume indexes + common/index.md (9/9).
- Up-link (`^[↑ ` on line 1): 0 leaves/indexes missing it (full sweep, excluding entry-point/sidecars/session/.index/tools).

**Observation 1 (ledgered, not fixed) — frontmatter-migration residue.** The KB has migrated to `<!-- kb-frontmatter` (798 leaves); 5 migrated leaves retain a redundant legacy `<!-- leaf: verbatim -->` marker alongside their kb-frontmatter: `vol3/condensed-matter/ch11-thermodynamics/kolmogorov-spectral-cutoff.md`, `vol3/applied-physics/ch14-sonoluminescence/sonoluminescence-derivation.md`, `vol4/simulation/ch18-universal-vacuum-cell/spice-subcircuit.md`, `vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md`, `vol2/quantum-orbitals/ch07-quantum-mechanics/orbital-penetration-penalties.md`. NOT removed — CONVENTIONS.md itself still documents `<!-- leaf: verbatim -->` as the line-2 marker, so the legacy marker is not "wrong" against current (stale) CONVENTIONS, and tooling dependence is unverified. (README.md/CONVENTIONS.md "leaf: verbatim" hits are documentation text, not markers.)

**Observation 2 (ledgered) — CONVENTIONS.md is stale vs the kb-frontmatter migration.** CONVENTIONS.md §Document-Types / INVARIANT-S5 still specifies the old `Line 2: <!-- leaf: verbatim -->` leaf-marker format, but 798/803 leaves now use the `<!-- kb-frontmatter ... -->` block. Updating CONVENTIONS.md to document the kb-frontmatter format is a spec-authoring judgment (not a mechanical fix) — routed to the auditor / KB-maintainer, NOT applied here.

---

## NOT-SWEPT (honest disclosure)

- **FENCED files (PR #738) — read-only ground truth, findings routed as APPLY-POST-#738:** `.index/claims.jsonl`, `common/claim-quality.md`, `common/dark-wake-bemf-foc-synthesis.md`, `common/engine-capability-map.md`, `common/substrate-hysteresis-index.md`, `common/trampoline-analogy-primer.md`, `vol3/cosmology/ch05-dark-sector/effective-galactic-acceleration-mond.md`, `vol4/circuit-theory/ch1-vacuum-circuit-analysis/tau-relax-derivation.md`, `_orchestration/2026-07-10_rulings-docket.md`, `_orchestration/2026-07-15_hardware-ratings-map.md`, `research/_archive/L3_electron_soliton/59_memristive_yield_crossing_derivation.md`. Not edited; drift on them is in the APPLY-POST-#738 sections above.
- **Branch-scrub follow-ups (docket 2026-07-19 continuation) — NOT this lane's sweep:** the 3 KEEP-branch KB-debt items (clm-exjfai moving-front refutation at `dark-wake-bemf-foc-synthesis.md:54` [FENCED] + `substrate-hysteresis-index.md:51` [FENCED]; the trampoline-analogy-primer.md:280 over-unification [FENCED]; the MOND kernel-conflict at `effective-galactic-acceleration-mond.md:15` [FENCED]) are all on FENCED files and are routed via their own PRs per the docket; not swept here (out of scope + fenced).
- **`session/` tree** — deliberately excluded from leaf/orphan/CONVENTIONS sweeps: `session/axiom-homologation.md` carries a self-declared "DEPRECATED, do not make sweeping changes, to-be-deleted" banner; its 19 broken links are characterized (C1-A) but not fixed.
- **`tools/` tree** — test fixtures + tooling (intentional broken-link/placeholder fixtures); excluded from all checks.
- **Manuscript tex volumes (`manuscript/vol_0..vol_9`, `common_equations/`)** — the sibling lane's domain; not touched (KB→tex outbound links were fixed only *in the KB file*, e.g. the vol9 depth corrections).
- **Deep banner-integrity audit (does every "preserved verbatim below" banner actually still contain the preserved text):** spot-checked on the load-bearing Class-2 leaves (all well-formed) but NOT exhaustively verified across all 169 status-marker-bearing files — a full preserved-text integrity audit is judgment-heavy and was not performed.
- **Claim-quality sidecar solidity/depends-on re-scoring** — out of scope (that is the sidecar-refresh cadence, a `generalist-coder` dispatch per CONVENTIONS §maintenance-cadence, not doc-hygiene).
- **Full CONVENTIONS.md rewrite for the kb-frontmatter migration** — spec-authoring judgment, routed to the auditor (C1-C Observation 2).

*Count reconciliation (review, 2026-07-19): summary headers previously said 12/14 links; the itemization and the broken-link delta (80→70) both prove 8 :NN + 2 depth = 10. Headers reconciled down to the itemization.*
