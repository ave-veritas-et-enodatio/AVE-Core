# Manuscript-Reconciliation Epic — Board + Ratified Cribs (2026-08-02)

**Lane:** manuscript-reconciliation orchestrator (separate epic session; handoff = [`2026-08-01_manuscript-reconciliation-epic_handoff.md`](2026-08-01_manuscript-reconciliation-epic_handoff.md), delivered #818).
**Base:** `main` @ `19285c5d`. **KB is the truth source** (standing G-ruling); physics divergences where the KB is unsettled are ROUTED via `docket-entries/` fragments, never adjudicated in-lane.
**Ratification:** the classified board below + the sequencing + the crib rulings were presented to Grant 2026-08-02 and ratified, verbatim `[sic]`: **"proceed"**. Mechanical items fire without per-item rulings; crib-covered items fire as mechanical under the crib texts in §3; route-to-core items get docket fragments only (no manuscript edits in this epic until the core session rules).

## §1 Sweep method (receipts)

- Grounding: 29-topic KB-delta inventory over the post-2026-07-01 window (441 merge commits scanned; 368 distinct PR merges #445→#818; 363 non-merge KB commits), every topic anchor two-method verified at HEAD.
- 10 read-only auditor lanes (Vols 0–6, 9, backmatter, papers), two-method receipts required per finding.
- 10 independent refute-by-default verifier lanes re-derived every finding (quote fidelity / KB-truth currency / real-divergence / class / disposition). One verifier under-returned by one verdict; that finding was verified inline by the orchestrator (recorded in §5 vol9).
- Result: **158 raw findings → 154 surviving** (83 CONFIRMED / 70 CORRECTED / 4 REFUTED). Final dispositions: **47 mechanical / 58 ruling-needed (mostly crib-covered) / 36 route-to-core / 12 gated-ringdown / 1 defer-to-live-lane**. Severity: 39 high / 76 medium / 39 low.

## §2 Routed-backlog verification (the brief said verify-at-launch; 4 of 7 rows corrected)

| # | Brief item | Verified state |
|---|---|---|
| 1 | ch08 physics prose rewrite owed | **DISCHARGED** — #771 (2026-07-21, `b39bd9cc`) rewrote item-3 admixture-honest. Two NEW debts replace it: (a) deep-rail sites `08_gravitational_waves.tex:240,:242,:284,:288,:298,:301` still say "outcome is not presumed" though #775 landed BIN 3 (MIXED / FORM-UNDETERMINED); (b) **INVERSION** — ch08 print is AHEAD of the KB: `manuscript/ave-kb/vol3/gravity/ch08-gravitational-waves/gw-propagation-lossless.md` carries no admixture note / no Reading-A banner. KB-ward propagation lane opened (§4). |
| 2 | ch08 item-3 rewording (F4→(a)) | **EXECUTED** in #771; docket EXECUTED stamp at `2026-07-10_rulings-docket.md:2649`. Cite-shift found: `08_gravitational_waves.tex:250-251` and `rulings-docket.md:2649` cite `2026-07-20_pending-rulings-and-frontier-queue.md:26`; the ruling lives at `:113` at HEAD (items 13–20 appended 2026-07-26 shifted it). Repair rides the gated ch08 lane (tex) + a tracker touch-up. |
| 3 | ch15 four sub-2%/spin-range sites | **CONFIRMED exactly 4**: `15_black_hole_orbital_resonance.tex:{27,271,292,387}` (`:31` = the interim note itself; `:270`/`:289` are %-comments — not rewrite targets). Per-occurrence rewrite still owed, gated (§4). |
| 4 | Vol 6 + Vol 9 datasheet cleanup "never run" | **FALSE** — Vol 6 ran (#348, 2026-06-22); Vol 9 ran twice (#332 2026-06-21; #745 2026-07-20). All volumes are drift re-sweeps. |
| 5 | Backmatter mirror-trio class | **CONFIRMED** — trio = `common/solver-toolchain.md` + `vol2/appendices/app-f-solver-toolchain/*.md` + `backmatter/05_universal_solver_toolchain.tex`; #809/#810/#816 each touched all three. |
| 6 | "No systematic diff since 2026-07-01" | **PREMISE STALE** — the 2026-07-19 two-lane sweep ran (ledgers: `2026-07-19_manuscript-cleanup-ledger.md`, `2026-07-19_kb-cleanup-ledger.md`, windowed 07-01→07-19). This sweep audited against HEAD, superset window — coverage unaffected. |
| 7 | papers/ v3 provenance | Letter **IS v3-current** (`main.tex:81,:750,:1136` = 3.75π/α²) but #815's receipt did not establish it, and `provenance.md:121` still carries the v2-form ratio row. Repo-side pointer repairs approved (§4); `main.tex` untouched (submission-gated). |

## §3 Ratified wording cribs (Grant 2026-08-02; sites become MECHANICAL under these)

- **CRIB-1 — K=2G / ν_Hill / "Cauchy".** Replacement pattern: *"the K = 2G operating point (form-derived; value GR-imported — see `common/form-deriving-value-importing.md`) with ν_Hill = 2/7 (isotropic Voigt–Reuss–Hill average; an averaging choice, not a lattice-emergent bound)"*. Never label the AVE lock "the Cauchy relation" (three-way homonym; `vol1/claim-quality.md:652`); never "simulation confirms … emergent" (κ_rot micropolar-grade test returned negative; `vol1/claim-quality.md:665`, PR #508 STAYS-OPEN). First printed "Hill" instances are minted by this epic (grep-verified zero manuscript precedent).
- **CRIB-2 — carrier + T2-photon vocabulary.** (a) photon = the massless transverse-TRANSLATIONAL u-family T2 (`def-t2ph01`, vocabulary-register watch-rule: never write microrotation = the photon); (b) production carrier = chiral **srs-z3** (D1 ratified 2026-07-03); K4-diamond z=4 = historical, statics-pathological instrument (`def-4b1a2c`); FCC/"z = 4 coordination" carrier wording is corrected to the srs-z3 statement with an instrument-history parenthetical where the text is about the engine.
- **CRIB-3 — spin-½ carve.** *"the SU(2)/SO(3) double-cover STRUCTURE is axiom-derived; the fermionic spin-½ SELECTION is posited/import (PEER-WITH-SM)"* — `[SPIN-HALF-POSITED]` #584/#585, `electron-identification.md:89-90`. Applies to every "spin-½ is substrate-derived end-to-end / IS the substrate-native origin" site.
- **CRIB-4 — validation-headline scope.** BCS "0.00% error" → definitional identity at per-material calibration, not a fit (`ave-kb/claim-quality.md:171-182`); ringdown "1.7%" → cold Schwarzschild a\*=0 single-point anchor, spin scope per Ruling B1; "10–18% LIGO match" → retracted frame-mixed artifact (#774/#780) — strike per Rule 12, no replacement number; Petermann "50 ppm" → the landed q-g19a numbers + scope (`q-g19a-petermann-saliency-closure.md:92,:121`); "most direct experimental validation"-class sentences demoted to the claim-quality grade.
- **CRIB-5 — TKI transformer status.** Sites citing the EM-Ω ↔ mechanical-ρc isomorphism carry `def-tk1xfm` **RATIFIED SOLID (2026-07-21)** with its REGIME FENCE and strength ceiling, quoted from `common/vocabulary-register.md:435-441` — not the pre-ratification "exact dimensional isomorphism" absolutism.

Discipline riders on every crib application: Rule 12 strike-don't-delete with dated banners; **no value refills** into struck slots unless independently verified; frozen preregs byte-untouched; cite-shift sweep AFTER content settles.

## §4 Sequencing + lane tracker (ratified)

| Wave | Lane | Scope | Status |
|---|---|---|---|
| now | orchestration-docs | this board + 8 docket fragments (`docket-entries/2026-08-02-mr-*.md`) | THIS PR |
| now | KB-ward ch08 | admixture propagation to `gw-propagation-lossless.md` (already-ruled Reading-A; #771's owed note; fixes the §2-item-1 inversion) | DISPATCHED |
| 0 (pilot) | vol4 | mechanical + crib-covered items; `:720` and `15_autoresonant:34` EXCLUDED (routed) | DISPATCHED |
| 1 | vol0, vol1, vol2, vol9 | after pilot review validates the pattern; vol1 ch07 + vol9 ch14 EXCLUDED (live-lane collision, `docs/factor7-and-782-basis-notes`); vol9 ringdown sites EXCLUDED (gated) | queued |
| 2 | vol5, vol6, backmatter, vol3-non-ringdown | backmatter/07 ringdown block EXCLUDED (gated); vol3 ch07 EXCLUDED (collision); vol3 ch08/ch15 EXCLUDED (gated) | queued |
| gated (LAST) | ringdown set | vol3 ch08+ch15 (incl. the four §2-item-3 sites + deep-rail BIN-3 + cite-shift), backmatter/07:{85,145,211,213}, vol9 ch07:195/ch03:175/ch14:105-adjacent, vol1 ch04:116/ch07:19, vol5 ch02:717 | gated on the cold-Q derivation arc landing (core session) |
| repo-side | papers pointers | `provenance.md:114,:121` + `outline.md:156,:220` pointer rows ONLY; `main.tex` untouched | queued (wave 2) |

Collision ledger: `docs/factor7-and-782-basis-notes` (vol1 ch07 / vol3 ch07 / vol9 ch14 + 2 KB leaves) and `docs/rulings-d2-d3-d4` (theorem-thesaurus + translation-tables README) are live mid-flight lanes — their files are excluded from every wave until they land. `#819` = src-only, no overlap.

Refuted-finding note: the four REFUTED findings are dropped from execution but listed in §5 with reasons. The two ch15 refutations are CLASS-level only (the interim note at `:31` already discloses the retraction); the #780 per-occurrence rewrite obligation is unaffected and lives in the gated wave.

## §5 The classified board (154 findings, post-verify)

(Appended below verbatim from the sweep+verify pipeline output; per-finding format: severity / class / disposition / file:line / printed excerpt / KB truth / verify note.)
