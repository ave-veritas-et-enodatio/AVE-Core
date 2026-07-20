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

---

## Orphan / phantom index lists

_(populated during index-consistency pass)_

---

## NOT-SWEPT (honest disclosure)

_(populated at close)_
