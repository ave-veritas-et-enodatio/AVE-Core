### ENTRY 2026-08-02-paperclip-canonization (2026-08-02): implementer — canonize the paperclip twist analogy as a walk-ratified physical picture, fenced on open item 13

- **Class: pedagogical canonization. NOT adjudication.** No physics question re-opens, no grade moves, no `clm-` / `def-` / `exp-` / `sup-` / `ilk-` is minted, nothing is re-binned, no solidity is assigned. Per `ave-discrimination-check`: the picture is a **rendering of in-corpus structure**, **not** a cross-domain chord and **not** a discriminating connection — it is explicitly tagged so in the leaf and is **not** logged as one. Per Grant's order 2026-08-02, verbatim `[sic]`: *"we should probably canonize the paper clip expample"*.

#### What landed (3 edits, exactly the ordered placement)

**(a) PRIMARY — [`manuscript/ave-kb/common/electron-plumbing-primer.md`](../../manuscript/ave-kb/common/electron-plumbing-primer.md), new `## Step 3.5 (walk-ratified physical analogy, 2026-08-02)`.**
Content-located **after Step 3** (the $0_1$-unknot / $(2,3)$-phase-winding electron) and **before Step 4** — the picture is about the electron's stored twist, which is the object Step 3 introduces. Numbering matches the house pattern in the sister primer ([`trampoline-analogy-primer.md`](../../manuscript/ave-kb/common/trampoline-analogy-primer.md) uses `Step 2.5 / 2.6 / 3.5 / 4.5 / 5.5 / 6.5` for exactly this kind of insertion), and the primer's frontmatter `no-claim` register-role is unchanged.

**(b) CROSS-REF 1 — [`chirality-and-antimatter.md`](../../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/chirality-and-antimatter.md), one `↗` line inside the Călugăreanu adjudication section**, inserted immediately **after** the `:58` Physical-note blockquote. One line, pointer only, explicitly "no claim minted, no re-adjudication of anything on this leaf."

**(c) CROSS-REF 2 — [`_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md`](../2026-07-20_pending-rulings-and-frontier-queue.md) item 13**, one appended `- **Pointer (2026-08-02)**` sub-bullet at the **end of item 13's block**. It states that the walk produced a **picture**, not a ruling, and that **item 13's status is UNCHANGED at OPEN-IN-WALK**.

Nothing else was touched.

#### Attribution discipline — the verbatim is never blended with the refinements

The leaf carries **two separately-headed blocks**, by design:

- `### The picture (Grant, 2026-08-02, verbatim [sic])` — Grant's words, reproduced exactly, including `eachother` and the trailing question mark. **Not paraphrased, not corrected, not merged with anything.**
- `### Walk-level refinements (orchestrator, 2026-08-02)` — the three sharpenings, opened by an explicit italic disclaimer that they are *"refinements added in the walk, not part of the verbatim above."*

#### The three refinements, and the canon each one renders

| # | Refinement | Canon it renders (verified verbatim, this branch) |
|---|---|---|
| 1 | **the catch is a linking number → cannot unsnap without cutting; the only release is the mirror clip (annihilation); charge conservation and electron stability are one statement** | `chirality-and-antimatter.md:14` *"matter-antimatter annihilation is topologically impossible because geometrical lines cannot mechanically pass through each other"*; `:18` *"The topological optical boundary condition confining the resonant loop snaps"* / *"unspools into linear transverse vector waves"*; `:58` *"the conserved far-field quantity the electron **projects/broadcasts** … is the linking number $\mathrm{Lk}$ (= charge)"* |
| 2 | **stored energy is POSITIVE; "negative tension" names the pre-load's DIRECTION** | this primer `:34` *"**wound but not spinning** ($\omega = 0$): cocked springs storing the chirality (parity)"*; [`trampoline-framework.md`](../../manuscript/ave-kb/common/trampoline-framework.md)`:370` *"the winding is stored elastic energy, not circulation"* |
| 3 | **generation ladder = the same clip cranked one quantum tighter; decay = the extra twist letting go** | [`torus-knot-uniqueness.md`](../../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md)`:102` *"**The lepton family climbs a Cosserat-torsion ladder on fixed (2,3) topology**"*, `:110` *"they climb the Cosserat-torsion excitation ladder"*; [`theory.md`](../../manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md)`:43` *"the same $(2, 3)$ phase-space winding pattern as the electron, but with **one quantum of Cosserat torsional excitation** added on top"*, `:47` *"the localized vacuum undergoes continuous impedance rupture"* |

The brief named `theory.md:43` for refinement 3 and asked for verbatim verification — **`:43` is confirmed exact** (`grep -n "one quantum of Cosserat torsional excitation"` → `43`).

#### ★ THE FENCE (the load-bearing part of this entry)

The leaf carries a headed `### ★ THE FENCE` block stating that **whether the base twist's spring energy sits INSIDE $m_ec^2$ is OPEN** — it is tracked **item 13 (sector-of-storage)**, quoted from the tracker as *"WHERE the compression store lives (A1 canon vs the T2/swing label) … **⚑ OPEN-IN-WALK** — Grant is walking it; NOT ruled"* — and that the section **does not pre-empt it**: no sector assignment, no energy magnitude. It states explicitly that **the analogy is pedagogically live under EITHER outcome** (spring-energy-inside → a wound spring you weigh; spring-energy-elsewhere → a wound spring held by a latch), because the three things the picture teaches (integer catch / pre-load direction / mirror-clip release) are unchanged by the ledger. `A1 ⊥ T2` is named so nothing is silently cross-wired.

##### ★FLAGGED — the auditing lane's branch does not resolve on `origin`

The brief names the twist-ledger lane as in flight at branch `research/twist-ledger-audit`. **That branch does not exist on this REMOTE as of this commit** — `git ls-remote --heads origin` returns no match (the remote carries `14` heads total). The leaf therefore cites it as **a lane, pending, explicitly not a readable tree**, with the verification stated inline and scoped to `origin`: *"Do not cite it as a source until it lands."* Surfaced rather than silently written as a live cite — a pointer to an unreadable tree is exactly the stale-cite class `verify-before-cite` exists to catch.

> **↺ Self-correction, same session (2026-08-02, post-commit `53c9e608`).** The paragraph above originally added two further receipts — *"`git branch -a` shows no local or remote-tracking ref"* and *"a corpus-wide `grep -rn "twist-ledger"` returns **0** hits."* **Both were true when run and are now FALSE**: the twist-ledger lane materialized as a **local worktree** (`…/scratchpad/wt-twist`, branch `research/twist-ledger-audit`) *during* this lane's execution, as did `research/coldq-pole-derivation` and `research/biased-tensor-scoping`. The stale sub-claims are struck rather than left standing. **The load-bearing claim is UNAFFECTED and re-verified after the fact:** the branch is still **not on `origin`**, so the in-leaf citation (which was written scoped to `origin` and is therefore still exactly correct) stands unchanged — **no edit to any KB leaf was required by this correction.** **Overlap re-checked against all three now-existing lanes:** each has a **zero-file** committed diff vs `origin/main` and only untracked new files (`research/2026-08-02_twist-ledger-audit.md` + driver + docket fragment `2026-08-02-twist-ledger.md`; `research/2026-08-02_coldq-pole-derivation_prereg-FROZEN.md`; `research/2026-08-02_biased-tensor-scoping.md` + pilot + driver) — **none touches this lane's four paths, and no docket key collides** (`2026-08-02-twist-ledger` ≠ `2026-08-02-paperclip-canonization`). The *methodological* point stands regardless: a concurrent-branch absence check is a **snapshot**, not a durable fact, and the honest way to write one is to scope it (as the leaf does) to what is actually citable — `origin`.

##### ★FLAGGED, not fixed — canon carries TWO electron-stability accounts

Refinement 1 compresses charge conservation and electron stability into one statement on the **topological** gate (an integer cannot relax away). But [`theory.md`](../../manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md)`:41` gives an **energetic** account of the same fact: the electron's standing wave *"sits safely below the $43.65\,\text{kV}$ saturation threshold. Because it doesn't break the local vacuum elasticity, it can ring forever (infinite half-life)."* Topology-vs-sub-yield-amplitude are **different gates**, and they are not obviously the same statement. **This lane does not pick between them** — the leaf carries a `⚑ Flag (surfaced, not resolved)` block naming both with their cites and stating that the analogy is unharmed either way. Flag-don't-fix; routed for adjudication.

##### ★DISCLOSED — the $540°$ quantification is real, and it has a closed-negative history

The brief's "`Tw = q/p = 540°/rev` quantification" **exists and is exact**, but **not in the KB** — a first grep scoped to `manuscript/ave-kb/` returned **0** hits and would have been a false negative. A second-method scan (python walk over all `git ls-files`, regex `540\s*(°|\\circ|deg)` plus a `Tw`↔`q/p` proximity pattern) found **8** hits, all in `research/` + `_orchestration/` + one figure driver. The two cited anchors are [`research/2026-06-07_alpha-twist-framing-test.md`](../../research/2026-06-07_alpha-twist-framing-test.md)`:177` (*"$q/p = 3/2$ turns $= 540°$ = $9.42478$ rad per toroidal revolution — exact, and geometry-independent"*) and [`research/2026-06-07_vacuum-characterization-program.md`](../../research/2026-06-07_vacuum-characterization-program.md)`:59`. **The leaf carries the negative alongside the number**: the α-twist test is a **CLEAN NEGATIVE** — the framing twist is the full winding, `~1292×` α-radians and `~205×` 1/137-of-a-turn, *"not even a near-miss"* (`:190`, `:193`) — with the banked separation *gross twist = spin/structure, small per-revolution slip = loss*. Written in so nobody re-runs a closed route off a pretty number. The class-tag blockquote also discloses that these two anchors are **research-lane docs, not KB leaves**, cited as receipts for a number.

##### Also disclosed, not imported

The muon **mass value** on the Cosserat ladder is not carried through the analogy; the leaf states so and points at its own leaf's tag (`torus-knot-uniqueness.md:107`, *"echo/import … a fit-echo, not a chord"*). The annihilation **mechanism** status is likewise left exactly as `chirality-and-antimatter.md:28` tags it (asserted peer re-interpretation, `clm-hb2xmj` confidence `0.30`) and is restated in the leaf so the picture cannot be read as strengthening it.

#### Line-drift + merge-order

- **Zero inbound-cite drift.** The `chirality-and-antimatter.md` insert lands **after** `:58`, so every line an inbound cite names is unmoved. Inbound cites were enumerated corpus-wide (`grep -rn "chirality-and-antimatter"` across `*.md` / `*.py` / `*.tex`, `21` citing sites): they name `:6`, `:10`, `:12`, `:16`, `:24-25`, `:38`, `:42`, `:43`, `:45`, `:58` — **all at or above `:58`**, none at `:60`+. The primer insert lands **after** its own `:34` (Step 1 rest-state caveat), which the new section cites, so that self-cite is correct post-edit.
- **⚑ MERGE-ORDER NOTE on the pending-rulings tracker.** That file falls under the blanket `*.md merge=ours`, where a concurrent lane's edit is **silently dropped** rather than conflicting (hazard recorded at [`README.md`](README.md) and re-stated in the tracker's own §1 header). The brief flagged `docs/mechanical-closeout-batch` as a possible concurrent toucher for the D-enum. **Checked at branch time:** that branch's committed diff vs `origin/main` is **one file**, `manuscript/ave-kb/common/divergence-test-substrate-map.md`, plus one uncommitted working-tree mod to `manuscript/ave-kb/common/theorem-thesaurus.md` — **it does not touch the tracker**. My pointer is nevertheless placed at the **end of item 13's block**, a location distinct from the D-enum (which lives in **item 17**, `~40` lines below), so the two edits cannot textually collide. **If the closeout batch lands a tracker edit first, re-read the merged file and confirm this pointer survived** — under `merge=ours` its absence would be silent.
- **Overlap sweep, all branches.** Every local and remote-tracking branch was diffed against `origin/main` and filtered for this lane's four paths. Two hits, **both stale, neither live**: `analysis/2026-06-08-electron-plumbing-primer` (`3685` commits behind `main`, the original primer-authoring branch, unmerged leftover) and `sim-merge` (`391` behind). `src/repoint-pvlas-v3` (`13` files) and `docs/mechanical-closeout-batch` (`1` file) have **zero** path overlap. All sibling worktrees were `git status`-checked for uncommitted work on these paths — none. **Re-run post-commit** once `research/twist-ledger-audit` / `research/coldq-pole-derivation` / `research/biased-tensor-scoping` appeared as local worktrees mid-session: all three are **zero-file** committed diffs with untracked-only new files, **no path overlap, no docket-key collision** (see the self-correction block above).

#### Discipline skills applied

`verify-before-cite` (every `file:line` re-grepped on this branch; caught the non-existent `research/twist-ledger-audit` branch and the KB-scoped `540°` false negative) · `ave-discrimination-check` (class-tagged pedagogical, NOT a chord, NOT logged as a discriminating connection) · `consistency-vs-emergence` (consistency-class rendering; no emergence framing, no new number) · `flag-don't-fix` (the two-stability-accounts tension surfaced with both cites, not resolved) · grep-completeness two-method discipline (the `540°` scan) · Rule 12 (nothing overwritten; the item-13 pointer adds, it does not flip a status).

#### Battery

`make verify` exit `0`; `make refresh-kb-metadata` idempotent (`0` subtree-claims, `0` solidity, `0` footers, `0` index files rewritten on the confirming re-run); `make verify-kb-metadata` PASS; `verify-md-links` gating `0`; `verify-docket-keys` PASS (key `2026-08-02-paperclip-canonization` unique); `verify-provenance-stamps` / `verify-frozen-provenance` / `verify-lane-number-checks` PASS. **Anchor-content advisory delta MEASURED at `0`** (`verify-anchor-content --top 5000`, finding-count diffed across a `git stash` of this branch's working tree: `1006` → `1006`; the two pre-existing flags touching this lane's paths — `2026-08-02_manuscript-reconciliation-board.md:19 → …pending-rulings…:26` and `substrate-native-terminology.md:17 → electron-plumbing-primer.md:24` — are byte-identical on both sides and pre-date this lane). No `Frozen`-labelled text, no prereg, and no result doc was edited. Pure-corpus.

---

#### ↺ ADDENDUM (2026-08-02) — audit repair pass, PR #832 verdict CLEAR-WITH-REPAIRS

*Appended, not rewritten. The self-correction block at the `★FLAGGED` heading above stands unedited; this addendum adds what that block did not cover.*

##### (a) The THIRD struck assertion — quoted, not silently deleted

The self-correction block quoted **two** withdrawn sub-claims (`git branch -a` and the corpus `grep`). The correction commit `53c9e608 → b6340d5e` **deleted a third outright, without quoting it** — from the *Overlap sweep* bullet, verbatim as removed:

> *"The named live lanes `research/coldq-pole-derivation`, `research/biased-tensor-scoping`, `research/twist-ledger-audit` **do not exist on this remote at all**"*

**That assertion was true when run and is now FALSE**, and it is the same failure the block already owns — recorded here so the docket's own diff is self-describing. Re-verified at repair time (2026-08-02T23:01:44Z): `git ls-remote --heads origin` returns `10883990  refs/heads/research/twist-ledger-audit`; the remote now carries `18` heads, not the `14` recorded at branch time. Quoting a struck claim is the whole point of a self-correction block; deleting one silently defeats it.

##### (b) The two in-place softenings — form defect only

Two further edits in that commit were **in-place rewrites**, neither marked as a change:

| was (`53c9e608`) | became (`b6340d5e`) |
|---|---|
| *"a pointer to a **non-existent tree**"* | *"a pointer to an **unreadable tree**"* |
| *"with the verification **stated inline**"* | *"with the verification **stated inline and scoped to `origin`**"* |

**Form defect only.** The origin-scoping claim was checked against `53c9e608` and is **accurate** — the leaf's parenthetical did say `origin` at that commit, so the second rewrite describes the leaf correctly rather than retrofitting it. But an unmarked in-place softening inside a block whose subject *is* honest withdrawal should have been marked. Marked now.

##### (c) Receipt nit corrected — the item-17 distance

The merge-order note says the D-enum *"lives in **item 17**, `~40` lines below"* this lane's pointer. **Re-measured on this branch: `21` lines**, not `~40` — this lane's pointer is `_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md`:36 (end of item 13's block) and item 17's heading is `:57`. **The substantive claim stands**: the two edits sit in textually disjoint blocks and cannot collide hunk-wise. Only the number was wrong.

##### ⚑ MERGE-ORDER CONSTRAINT (recorded, NOT resolved) — two shared `merge=ours` files

**Confirmed by `git check-attr merge`** on this branch: `manuscript/ave-kb/common/theorem-thesaurus.md`, `manuscript/ave-kb/common/electron-plumbing-primer.md`, `_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md` and this fragment all return `merge: ours`. Under that attribute a concurrent lane's copy of a shared file is **taken whole or dropped whole** — there is no hunk-level merge and **no conflict marker to warn anyone**.

**The branch-time receipt above is now stale and is superseded here.** It recorded `docs/mechanical-closeout-batch` as *"one file … it does not touch the tracker"*. That branch is now at `19ff95c5` (the audit brief named `294ffb87` **or later**; its lane is still running) with a **17-file / +297-line** committed diff vs `main`, and it rewrites **both** files this PR also rewrites:

| shared file | `#832` (this PR) writes | `docs/mechanical-closeout-batch@19ff95c5` writes |
|---|---|---|
| `manuscript/ave-kb/common/theorem-thesaurus.md` | 3 inbound primer anchors re-pointed `:101 → :159` (sites `:67`, `:122`, `:217`) | `44` lines changed; **preserves the stale `:101`** at its `:122` site and shifts the TH-2 row `:217 → :218`, still reading `:101` |
| `_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md` | `+1` line — the item-13 pointer at `:36` | `+53` lines; its copy contains **no `paperclip` string at all** (`git show …:… \| grep paperclip` → no match), i.e. it does not carry this lane's pointer |

**The constraint.** Whichever of `#832` / `docs/mechanical-closeout-batch` merges **SECOND** silently drops the other's copy of **both** shared files. Concretely: if the closeout lands second, the `:101 → :159` anchor repair is reverted and the item-13 pointer disappears; if `#832` lands second, the closeout's thesaurus rewrite and its `+53` tracker lines disappear.

- **(i) Merge order is Grant's decision.** This lane does **not** pick it and has **not** touched the closeout's paths. No tracker row was added by this repair pass on purpose — the tracker is `merge=ours` and concurrently edited.
- **(ii) Required of whichever merges SECOND** (not optional — under `merge=ours` the loss is silent):
  1. **Re-run the primer-inbound anchor verify in BOTH syntaxes** — bare `electron-plumbing-primer.md:NNN` *and* markdown-link `](electron-plumbing-primer.md):NNN` — over `git ls-files`, not by grep alone. The automated battery does not see the second form (next section).
  2. **Re-derive the thesaurus line numbers from the merged primer**, do not carry `:159` forward on faith. `:159` is correct *for this branch's primer*; any further insert above the Thomson's-principle sentence moves it again. This lane already hit that twice in one session: the Step-3.5 insert moved it `:101 → :156`, and this repair pass's own R2/R3 text moved it `:156 → :159`.
  3. **Confirm the item-13 pointer survived** in the merged tracker; its absence is silent.

##### Named follow-on, NOT repaired here — `verify-anchor-content.py` is blind to link-form anchors

`manuscript/ave-kb/tools/verify-anchor-content.py`:119–121 defines `CITE_RE` so that the line number must follow the extension **immediately**:

```
CITE_RE = re.compile(
    r"(?P<path>(?:[\w.+-]+/)*[\w.+-]+\.(?:" + "|".join(TARGET_EXTS) + r")):(?P<line>\d+)(?!\d)"
)
```

A markdown-link cite renders as `](electron-plumbing-primer.md):159` — the `)` sits between the extension and the colon, so the **entire markdown-link-form cite class is invisible to the drift checker**. That is exactly how all three broken anchors repaired in this pass survived a battery that reported an anchor-content advisory delta of `0`: the tool never scanned them. Candidate fix is roughly one regex character-class (allow an optional `)` before the colon), but it will re-classify an unknown number of previously-unscanned cites corpus-wide and needs its own baseline diff.

**Named as a follow-on for a closeout-class lane. Out of scope for this PR** — this lane repairs its own breakage, it does not change shared tooling mid-audit.

##### Cross-lane note — the two lanes partition "the three refinements" differently

Same content set, different cut, recorded so nobody reads it as a discrepancy:

- **This PR** (`electron-plumbing-primer.md` Step 3.5): **{ (1) linking-catch **+** topologically-gated release, (2) positive energy / "negative tension" = pre-load direction, (3) the generation ladder }**.
- **The twist-ledger lane** (`_orchestration/docket-entries/2026-08-02-twist-ledger.md`:3, on `research/twist-ledger-audit`): *"the catch = a linking number; annihilation = the topologically-gated release; the stored energy is **positive**, 'negative tension' names the pre-load's direction"* — **{ linking-catch, gated release, positive energy }**, with the generation connection promoted out of the refinement list and carried as **that doc's spine finding** (*"★THE GENERATION CONNECTION (the doc's spine)"*, same file `:9`).

**No leaf edit.** The union is identical; only the grouping differs, because the generation rung is a pedagogical *refinement* here and the *result* there.

##### Repair-pass battery

`make verify` **EXIT `0`, ALL PHYSICS PROTOCOLS PASSED**; `verify-md-links` gating `0` (warn-only `206`, kbleaf `1095` cites checked, gating `0`, waived `1`); `verify-docket-keys` entries `98` / unique keys `96` / **no new duplicate keys** (grandfathered numeric dups `['22','32']` unchanged); `make refresh-kb-metadata` **idempotent** across two consecutive runs — `0` subtree-claims, `0` solidity, `0` footers, `0` index files rewritten (`6` unchanged) — porcelain clean apart from this fragment's own in-flight edit. **Anchor-content advisory delta MEASURED at `0`** (`1006 → 1006`, checked cites `1368` both sides), i.e. the repairs added no new drift.

**Manual anchor check (the automated battery cannot see these — see the follow-on above).** Each repaired site was resolved by printing its target line: `theorem-thesaurus.md`:67, :122, :217 → `electron-plumbing-primer.md`:159, all three landing on *"The deep point: **nothing chooses the path.** … **minimizes total dissipation** (Thomson's principle)"*. The `:122` excerpt was byte-diffed against `:159` and is **verbatim-present**.

**Two-method sweep, both syntaxes, for any remaining stale inbound anchor.** Method A = `grep -rn` over the whole tree; Method B = python over `git ls-files` (`4217` text files scanned of `4891`; the `674` skipped are all binary — `png` `478`, `pdf` `131`, `stl` `24`, `gif` `22`, `npz` `10`, `ots` `4`, `mp4` `2`, `gz`/`bak`/extensionless `3`). **Both methods agree exactly:**

| syntax | hits | primer lines named | stale (`≥66` and not `:159`) |
|---|---|---|---|
| bare `…primer.md:NNN` | `3` | `:24` ×2, `:26` ×1 — all **below** the Step-3.5 insert point (`:66`), therefore unshifted | **`0`** |
| link `](…primer.md):NNN` | `4` | `:159` ×4 | **`0`** |

The 4th link-form hit is this fragment's own **illustrative example** in the follow-on section above, not an inbound cite. Pre-existing and **not touched** (out of scope, and one lives in a `FROZEN` prereg): `research/2026-06-15_k2g-constitutive-provenance_prereg_FROZEN.md`:16 cites `…primer.md:26` for *"twist/microrotation ↔ couple-stress ↔ inductive/μ-sector"*, but the microrotation line is `:27` (`:26` is the E-field/translational-stretch bullet) — an **off-by-one that pre-dates this lane and is unaffected by it**. Surfaced, not fixed.

**NOT repaired, flagged (flag-don't-fix).** The `theorem-thesaurus.md`:122 excerpt is labelled *verbatim* and renders `**global**` where the primer source has `*global*`. Word-for-word the quote is byte-exact (verified with emphasis markers stripped); the marker differs because the excerpt sits inside an enclosing `*"…"*` italic span, where a nested `*global*` would terminate it early. House style carries **no** underscore-emphasis convention (`0` occurrences of `_"` anywhere under `manuscript/ave-kb/`), so there is no clean byte-exact rendering without a style decision. **Pre-dates this lane** (present at `ac165cf2`). Left for the auditor / Grant.
