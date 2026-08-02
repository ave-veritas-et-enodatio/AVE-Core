### ENTRY 2026-08-02-mechanical-closeout

**Lane:** implementer · **Branch:** `docs/mechanical-closeout-batch` · **Class:** mechanical closeout — two Grant rulings + a queued zero-decision micro-batch. **No physics adjudicated, no claim minted, no verdict moved, no status promoted.** Every content change is either a ruling execution, a marker flip to an already-merged reference, a cite repaired to its own stated target, or a supersession stamp mirroring one already merged elsewhere.

**Provenance.** Grant 2026-08-02, verbatim `[sic]`: **"4, follow rec"** (ITEM A) and **"5, yes"** (ITEM B). ITEMs C/D/E are the zero-decision micro-batch routed by merged `#823` (cite-rot lane + its 2026-08-02 addendum), merged `#820` (the `#782` basis-note insert), merged `#821` (which unblocked the thesaurus tripwire), and merged `#819` (the v3 birefringence supersession).

---

#### ITEM A (ruling 4) — the divergence-map priority block reduced to a pointer

`manuscript/ave-kb/common/divergence-test-substrate-map.md` restated the orchestration-tier ordering that `_orchestration/2026-07-15_hardware-ratings-map.md` §2/§3 owns. **Rationale, one line: KB leaves catalog physics; orchestration owns process ordering.**

A second copy goes stale on its own clock, and this one did twice — the pre-2026-08-01 ranking went stale in four of five entries, and `#823` ITEM 2's re-derivation fixed that only by restating another doc's priority marks, which is the same failure mode one iteration later. The five-item ordering is therefore **removed**, not re-patched, and replaced by ONE pointer naming the ratings map as the canonical action-ordering surface with an explicit *"do not restate it here"*.

**Kept locally (map-row-scoped, which is what this leaf owns):** the four rows of *this* map with no ratings-table row (A1-HOPF, C1-BH-RING, C5-CMB-AXIS, C3-MUON-DELTA) under the original *AVE-distinctness × accessibility × decisiveness* rule, plus the explicitly-NOT-ranked retired/regime-artifact paragraph.

**Rule 12:** the `#823` re-derived block is preserved verbatim in a new dated `<details>` citing this ruling verbatim; the pre-2026-08-01 block's existing `<details>` is untouched. **+22 lines, all below `:428`.**

#### ITEM B (ruling 5) — the 2026-08-01/02 ruling batch enumerated

New dated §1-continuation block in `_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md`: eleven rulings, each with its verbatim word, what it decided, its executing PR/lane and its state. **D1** "(ii)" #819 merged · **D2** "follow rec" #821 · **D3** "rec" #821 · **D4** "follow rec" #821 · **D5** "wait" (no action — the cold-`Q` derivation supersedes any tag applied now; a sequencing decision, not a capacity deferral) · **D6** "recs" #821 · **D7** "follow your rec" + "go" #822 in flight · **D8** "correct plus note" in flight · κ desk-calc "go" in flight · ℓ handshake "adopt and split" in flight · "4, follow rec" + "5, yes" this PR.

**Why the block exists — the `D1`-label collision, verified two-method at HEAD.** A bare `D1` already denotes **five** unrelated things in this corpus: the **D1-CHSH** divergence-map Tier-D row (`:380`, Matrix-1 `:542`); the **sector-of-storage** question (**item 13 of that same file**, `:30`; `research/2026-07-26_d1-sector-and-inertia-route_scoping.md`; `vocabulary-register.md:1150`); the **field-definition lane** (`_orchestration/2026-06-15_k2g-crystalline-provenance.md:142`); the standing-decisions **Smith-chart ontology** item (`_orchestration/2026-06-16_standing-decisions-audit-lane.md:32`); and a decision label inside a frozen astro sweep (`research/2026-07-11_astro-adjudicator-sweep_branch-signature-map_FROZEN.md:17`). **The date disambiguates, not the letter.**

> ★**Two corrections to the dispatch, recorded rather than absorbed.** (1) It said *"four older unrelated `D1` uses"*; the sweep found **five**. (2) It attributed the collision finding to *"the #819 audit"* — **that does not verify.** PR #819's body and its reviews carry no D1-label-collision item (checked via `gh pr view 819 --json body` and the reviews API). The collision is real; its provenance is this lane's own sweep, and the block says so.

**Receipt discipline in-block:** six verbatims were re-read from existing repo receipts (D1/D2/D3/D4/D6 fragments; **D7 read READ-ONLY from `origin/src/repoint-pvlas-v3`**, whose fragment that branch owns and which was **not** edited). Five are chat-only and first-recorded here — the tracker gap this closes.

#### ITEM C — the thesaurus marker sweep (tripwire 2's own deliverable, DISCHARGED)

All three cited branches are on `main` (`#800` 2026-07-28 · `#802` 2026-07-28 · `#804` 2026-07-30) and every `★UNMERGED` marker was stale at HEAD. Each was **content-located on `main`** before flipping — never offset arithmetic.

**Anchor set (all verified at HEAD):** `translation-tables/translation-circuit.md` §4.7 `:313`, rows **D/E/F/G** `:332`/`:333`/`:334`/`:335`, object dictionary `:337` (Hill's-lemma `:348`, KCL `:349`), §4.7.3 `:354` (EXACT para `:356`, disanalogy 3 `:362`), §6 row **#32** `:467` · `research/2026-07-28_subc-kubc-bracket_prereg-FROZEN.md` §1.1 `:40` (`:46`), §1.3 `:59` (`:63`/`:64`/`:65`), §9 `:277` (`:279`) · `..._result.md` `:70` · `research/2026-07-26_d1-sector-and-inertia-route_scoping.md` §2 `:17` (`:26`/`:32`), §3 `:41` (`:43`), §4 `:69` (`:76`), §8 `:240`.

**Three defects found in the process, each stated rather than folded in silently:**

1. **TH-3's `[derived]`-textbook-theorem quote was cited to the prereg's §1.3 and is not there** — it lives in **§9** (`:279`, the frozen ledger-tags block). §1.3 carries the *variational argument*, which is what TH-1/TH-2 cite. Re-pointed by content.
2. **Two *"no on-`main` site"* negatives EXPIRED at the `#804` merge** — §6's Rayleigh row and TH-8's naming provenance. ★**The Foster one survived invisibly, and the reason is worth the record:** the on-`main` form is the **hyphenated compound** `Foster's-reactance-theorem` (`translation-circuit.md:362`), which the space-separated pattern `"reactance theorem"` **cannot match**. A grep-shape false negative, recorded in-row; two-method re-verified 2026-08-02.
3. **§5's two *"re-evaluate on merge"* triggers have FIRED** (the constraint lemma; Hill's lemma). Both stamped as fired; **neither candidate re-admitted** — admission is the §7 Owner call, not a sweep's. Flag-don't-fix.

**The cascading instance the tripwire named is discharged in the same pass:** `translation-circuit.md` `:196` / `:370` / `:467` flipped from *"PR #802 OPEN — cite by path, not yet on `main`"* to merged. ★**The VOID-AS-FROZEN verdict is untouched — merging banks nothing**, and each repair says so in-line.

**Also re-pointed:** the §6 class-label row's ship-time cite-currency note. It predicted `:124 → ≈:130` on `#820`'s merge; `#820`'s diff against that doc is `+6` after `:12` and `+1` after `:124`, so the `#782` §7.1 bullet is at **`:130`** — prediction exact, re-verified by **reading** the target rather than applying the predicted offset.

**Rule 12:** dated verification negatives preserved with dated updates appended; no flag text struck. ★**Grep receipt:** `grep -c '★UNMERGED'` returns **4**, all four *about* the marker rather than *being* one (schema rule `:80`, a preserved ship-time quote `:290`, the preserved flag `:300`, the discharge note `:301`). **Zero live markers.** New sweep prose was written **without** the glyph so a future grep does not false-positive on the record of the sweep that removed them.

#### ITEM D (i) — the six wrong-target cites repaired by content

| Citing site | Label | Old target | New target (content-located at HEAD) |
|---|---|---|---|
| `manuscript/vol_9_vacuum_datasheet/figures/gen_bankable_falsification_windows.py`:12 | C1-BH-RING | map `:143` | map `:165` (§C1) + `:167` (`r_sat = 7GM/c² = 3.5 r_s`) |
| same `:17` | C12-G-STAR | map `:245,247` | map `:269` (§C12) + `:271` + `:273` |
| `.../preferred-frame-and-emergent-lorentz.md`:235 | C7 matrix row | map `:399` | map `:538` (Matrix-1 C7 row) |
| `manuscript/ave-kb/claim-quality-closure-roadmap.md`:85 | C5-CMB-AXIS rows | map `:514`+`:554`+`:428`+`:907` | map `:536` + `:622` + `:662` + `:204` |
| same `:100` | C15 pred/§/exec rows | map `:497` + `:298-303` + `:599` | map `:579` + `:322-331` + `:681` |
| same `:115` | C5 axis-coordinate sites | map `:153,160,949` | map `:204` + `:211` + `:1057` |

> ★**FLAG (surfaced, not reframed): the `#823` docket's *"Actually lands in"* column does not reproduce against `origin/main`.** It reproduces **exactly** against the **pre-`#823`** map (1107 lines, `3009adee^`) — `#823`'s own `+43` moved every one of those landings again *before* it merged. A reader repairing from that table alone would repair to the wrong place. The fragment is left **byte-identical** (one lane, one file); recorded here so the table is read as the dated snapshot it is.

**Also repaired, disclosed as a SEVENTH instance not in the docket's six:** `preferred-frame-and-emergent-lorentz.md`:102 cites map `:456` for the **same** Matrix-1 C7 row as `:235` — a blockquote-marker/blank line at every revision checked. Found while content-locating `:399`; repaired in the same pass rather than leave one file carrying one repaired and one rotten cite to one target.

**Honest caveat carried in-text at roadmap:85:** the quoted cell values (*"frozen 2026-05-15 / spec-only / MISSING — no driver"*) are the **2026-05-19 pre-walk-back state**; all three C5 rows now read **DRIVER EXECUTED 2026-05-19**. That is the walk-back working, not a stale claim.

#### ITEM D (ii) — the 13-site trampoline-framework class

Re-verified at HEAD before touching anything: the Q-G42 template `V_yield^(apparatus) = E_yield^(substrate)/G_geom` is at `trampoline-framework.md:465`; `:439` is the §2.4 cross-reference bullet and `:455` is the `### 3.1 The saturation kernel` heading. Same reading as the audit — **re-confirmed, not assumed**.

**Six LIVE sites repaired** (`:439 → :465`, except the driver `:455 → :465`): `manuscript/ave-kb/CLAUDE.md`:75 · `.../ch11-.../project-zener-04.md`:51 · `.../project-torsion-05.md`:54 · `.../metric-levitation-limit.md`:47 (those three inherited the wrong target from the walk-back doc, per `#823`) · `manuscript/ave-kb/common/divergence-test-substrate-map.md`:152 · `src/scripts/vol_4_engineering/rrad_l_phased_array_compression.py`:24.

**Seven DATED-RECORD sites disclosed, not rewritten** (per the `#823` cite-repair policy carve): `research/2026-06-04_corrections-walkback-pernode-result.md`:40, :62 (**the upstream source the three banners inherited from**) · `research/2026-06-03_ivim-RA-adjudication.md`:73 · `research/2026-06-04_ivim-interferometric-rescope-result.md`:159 · `research/2026-06-08_rrad-l-phased-array-phase4_result.md`:165 · `_orchestration/2026-06-03_experimental-protocol-revamp-orchestration.md`:173 · `_orchestration/experimental/2026-06-04_round2-adjudications.md`:80.

**Zero residual `:439`/`:455` cites in `manuscript/` or `src/`** (re-grepped after the edits). No physics changed — template, scope and every banner's arithmetic byte-untouched.

#### ITEM D (iii) — the stale "only occurrence" comment

`research/drivers/subc_kubc_bracket_number_check.py` justified token `"114"` as *"the ONLY occurrence of 'cross-class' in that document"*. True when written, **false at HEAD**: `#820` merged 2026-08-01 inserting `+6` after `:12` and `+1` after `:124` in `research/2026-07-21_rve-aggregation-bench_result.md`. Two-method re-verified 2026-08-02 — the BIN-4 `cross-class` verdict line moved `:114 → :120`, **three further occurrences now exist at `:14`, `:16`, `:17`** (inside `#820`'s own inline Rule-12 block), and `:114` now lands on a bin table row.

Also noted in the same comment block, since leaving a known-stale sibling next to a repaired one is the defect this lane closes: token `"124"`'s §7.1 bullet moved `:124 → :130`.

**COMMENT-ONLY.** No token, no key, no allow-list entry, no gate changed. The line numbers are deliberately **not** re-pointed — they are quoted from a dated result doc, and this registry justifies the token appearing in the **lane** doc; it is not a third document's line-number maintainer.

#### ITEM E — the v3-supersession stamp on the Stage-2 QED-extension ledger

`research/2026-06-29_grqed-stage2-qed-extension_result.md` taught the v1 magnitude `7.5/α³ ≈ 1.93e7` un-stamped while its code twin has carried the `==== … ====` v3 banner since `#819` merged (Grant ruling D1(ii)).

The ruling named `:50` and `:94`. Content-location found **five more** un-stamped instances (`:28`, `:36`, `:74`, `:184-186`, `:275`). Stamping only the two named rows would have reproduced inside this doc **the exact self-contradiction `#819`'s own D1-completion had to repair inside `src/ave/qed/`** (module header says live; function 80 lines below says SUPERSEDED). So: **one document-scoped dated banner** in the `#819` form carrying the boxed v3 `15π/(4α²) = 3.75π/α² ≈ 2.2e5` cited to `vacuum-birefringence-e4.md`:104 (with `:106` for the v1 convention history) and enumerating all seven sites, **plus in-cell stamps on exactly the two rows the ruling names**. Bodies preserved verbatim — dated record, appended notes only.

★**The load-bearing part, stated in the banner:** only the **QED normalization** moved (`α⁻³ → α⁻²`). The AVE numerator `δn_bir ≈ −½A²`, the eigen-indices, the reused Op14 kernel and **both two-test legs** are unaffected; the magnitude was an adjudicated **α-echo under v1 AND under v3**. **The chord is still the EXISTENCE.**

★**Self-inflicted-shift check:** the banner is `+14` lines and moved the very sites it enumerates, so the enumeration states **post-stamp** numbers with the `+14` offset disclosed. No other file cites this doc by line (grep clean).

---

#### Cite-shift re-sweep (run AFTER all content settled)

Seven files changed line count: `pending-rulings-and-frontier-queue.md` 128→181 (from `:97`) · `divergence-test-substrate-map.md` 1150→1172 (from `:429`) · `theorem-thesaurus.md` 305→307 (`+1` from `:185`, `+1` more from `:301`) · `gen_bankable_falsification_windows.py` 136→145 (from `:12`) · `grqed-stage2-…_result.md` 281→295 (from `:10`) · `subc_kubc_bracket_number_check.py` 672→686 (from `:415`) · `rrad_l_phased_array_compression.py` 673→675 (from `:24`).

Swept **both** cite forms (`filename:NNN` **and** the bare `line NNN` / `lines NNN-MMM` form) over `*.md` / `*.tex` / `*.py`. **51 shift-exposed cite sites** classified.

**REPAIRED (live KB leaves; every target verified by reading it):** `physics-lineage-map.md`:115/:196/:453/:461 · `claim-quality-closure-roadmap.md`:105 (map `:735 → :757`) · `vol9/ch15-falsification-tests/index.md`:35 and :37.

**★THREE MORE WRONG-TARGET CITES surfaced by the sweep — a naive `+22` bump would have preserved every one:**

1. `physics-lineage-map`'s four `:603` cites were **never** a `D1-CHSH` row — on `origin/main` `:603` is the **C8-BARYON-LADDER** Matrix-2 row, three lines above the D1-CHSH one. Re-pointed by content: the verbatim *"matches QM by construction; no novel comparison source"* has **exactly one** corpus occurrence, the **Matrix-3** D1-CHSH row (`:668`); the open/NULL-framing cites go to the **Matrix-1** row (`:542`).
2. `vol9/ch15`:35 cited map `:448,67` as B1-VAC-BIREFRINGE. `:448` landed **in the priority-order block this branch replaced**, so the bump would have aimed at a blank line inside a collapsed `<details>`; `:67` landed on a bare *"Test type: new experiment."* in §A1. → `:87`,`:89`,`:91`,`:528`.
3. `vol9/ch15`:37 cited map `:469` as C11 — a blank line, same block. → `:259`,`:549`.

> ★**FLAG-DON'T-FIX (surfaced in-text at `physics-lineage-map`:115, NOT rewritten).** The parenthetical *"GHZ/contextual scenarios named as open"* **does not verify** against the divergence map: that map's only five `GHZ` hits are the **10 GHz microwave** unit in the B6-PONDER-02 rows (`:141`, `:143`, `:547`, `:668`, `:673`), and `contextual` returns **zero**. Whether the open-scenario pointer belongs elsewhere or should be struck is a content call for the owning lane.

**DISCLOSED, not rewritten (~40):** shifted cites inside dated `research/` result+prereg docs, `_orchestration/` boards, docket fragments and `_orchestration/experimental/` protocols.

> ★**HANDOVER — the reconciliation lane's board cites into `theorem-thesaurus.md`, deliberately not edited from here.**
> **The shift rule for that leaf:** lines `< 185` unmoved · `185`–`300` **`+1`** (the TH-8 dated-update bullet) · `> 301` **`+2`** (the tripwire-2 discharge bullet).
> **Content-located anchor moves** (verified by reading both revisions, not by arithmetic): §5 Fluctuation–dissipation row `:205 → :206` · §5 Hill's-lemma candidate row `:207 → :208` *(its cell text also changed — ITEM C's fired-trigger stamp)* · `### Hill — three distinct objects` heading `:223 → :224` · the Voigt–Reuss–Hill **AVERAGE** row, which carries *"Not a theorem and not a bound"*, `:227 → :228` · the Hill *"live hazard, stated plainly"* blockquote `:231 → :232` · §6 admission-bar preamble `:211 → :212` · the D6 `Q`-row placement block `:270 → :271`.
> **Board sites exposed:** `:88`, `:89` (both cite `:223`), `:147`, `:170` (both cite `:227`), `:548` (cites `:205`), `:549` (a VERIFY NOTE citing `:207` and the `Q`-row block as `:264-:274`).
> ★**Pre-existing, NOT created here — flag-don't-fix:** two of those board cites did not resolve at `origin/main` before this branch either. `:88`/`:89` cite **`:223`** for the *Voigt–Reuss–Hill AVERAGE* row and for the string *"Not a theorem and not a bound"*, but on `origin/main` `:223` is the **`### Hill — three distinct objects` heading** and both quoted items are at **`:227`** — off by four, independent of any shift. That is the reconciliation lane's own item.
> **Handed over, not applied:** that board belongs to the reconciliation lane and is live; editing it from here would be a drive-by on another lane's working surface.

---

#### Battery

`make verify` **exit 0** at every commit (pre-commit gate fires per-worktree) · `verify-md-links` counters **identical to `origin/main`**: gating **0**, warn-only **206**, broken inter **42**, `kbleaf` **1095 checked / gating 0 / waived 1** ⇒ **zero new debt** · `verify-lane-number-checks` clean · `subc_kubc_bracket_number_check.py` **PASS** (UNACCOUNTED 0; 369 auto-verified + 19 pinned + 79 allow-listed + 6 digest-shaped) · `make refresh-kb-metadata` **idempotent** · `verify-docket-keys` no new duplicate keys · pure-corpus observed.

**Overlap fence — zero file overlap with every live branch, re-checked at their current tips before push.** `src/repoint-pvlas-v3` (#822, 11 files incl. `src/ave/bench/birefringence.py`, `adopters.py`, `papers/…/provenance.md`, `vol4/claim-quality.md`, its docket + scoping): **empty intersection** — its `2026-08-01-d7-repoint-pvlas.md` fragment was **read** (`git show origin/src/repoint-pvlas-v3:…`) and **not** written. `docs/rulings-d8-and-ell-split` (`domain-catalog.md`, `identity-break-test-design.md`, its docket): **none touched** — local branch is at `origin/main` with no commits yet. `research/pasteur-kappa-desk-calc`: **branch does not exist** locally or on origin; ★**fence-adjacency disclosed** — ITEM D(iii) touches `research/drivers/subc_kubc_bracket_number_check.py`, which sits inside that lane's declared `research/ + drivers` fence footprint. It was **explicitly routed to this lane by the dispatch**, the change is **comment-only**, and it is named here so the κ lane can see it on arrival. `analysis/2026-08-02-bell-quote-provenance` (merged #824; its `-repairs` sibling owns `common/the-abandoned-interior.md`): **not touched**. `bench/sigma-repeat-and-sweep-spec`: different repo (AVE-HOPF), no risk.
