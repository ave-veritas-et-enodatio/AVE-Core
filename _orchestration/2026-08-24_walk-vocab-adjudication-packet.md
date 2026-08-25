# Adjudication packet — seven vocabulary items from the 2026-08-24 walks (Grant)

Seven terms from the frame-invariance walk record and the smith-annulus / Class-C
arc, drafted as PROPOSED def-nodes in `register-additions.md` (same directory).
Everything below is at PROPOSED status — nothing lands SOLID, nothing moves
solidity, and the walk-grade physics under several of these stays WALK. Per term:
the proposed noun, the physical picture in two lines, then what needs your ruling
versus what a lane can already execute at PROPOSED status.

> **★ REPAIRED TWICE, 2026-08-24. Round 1: a two-lens adversarial audit (18
> findings, 1 BLOCKER). Round 2: a re-audit of the repair (18 more — 3 MAJOR,
> 9 MINOR, 3 FLAG, 3 NIT, no BLOCKER).** Everything is now pinned to
> `origin/main` @ **`fc154aa6b2df26285f1406ed1ac39dee85678b96`**.
>
> **FIVE of the seven items changed *class*, not just wording** — **T1**
> (`def-cmdiff`) and **T4** (`def-rtlock`) were drafted as coinages and are not
> (the corpus already owns both carves); **T7** (`def-stexst`)'s "no collision"
> was false; **T3** (`def-tubalf`) and **T5** (`def-rspmap`) are **arc-adoptions**,
> not coinages, because their terms were already in lane use. **T6 gained a
> fourth sense.** *(Round 1 of this packet said "three"; that was an undercount
> that predated its own T3/T5 re-framings. The register said five and was right.)*
>
> **TWO items survive as clean coinages** — **T2** (`def-dtpres`) and **T6**'s
> lead candidate (`def-prstor`), each re-verified **0-hit at `fc154aa6` by three
> methods**. *(Round 1 of this packet called T2 "the one term that survived
> clean"; that was the same undercount.)*
>
> The finding-by-finding record with re-run commands is the **§REPAIR** log at the
> end of `register-additions.md` — now two tables, 24 + 18 = **42** findings
> addressed. Where an entry's verified state now contradicts what an earlier draft
> told you, the contradiction is stated here rather than smoothed over.

**Standing flag first: the collision-register-home decision is STILL un-ruled.**
*(Repair: this was written as a bare "W4", which resolves to at least four
unrelated objects in `_orchestration/`. The referent is:)*
**the 2026-08-24 opens walk**, item **W4** —
`_orchestration/docket-entries/2026-08-24-opens-walk-framing.md`, heading
`## W4 — the cheap batch` (currently `:47`), whose fourth sub-item reads
*"**collision-register home** → def-nodes under `ave-vocab-discipline` (already
A6-confirmed; needs only the go)"*. The item itself is
`_orchestration/open-items/2026-08-24-collision-register-home.md`
(`status: ROUTED-TO-GRANT`), which frames the choice as
`theorem-thesaurus.md` §6 homonym rows (prose, ungated) **vs**
`vocabulary-register.md` `def-` nodes (CI-gated via `open_ambiguity` /
`conflicting_sites`), with the orchestrator recommendation — *not a ruling* —
being the gated `def-` home plus pointer rows in §6. Four dependents wait on it:
`a0-glyph-collision`, `gammac-gc-modulus-identity`, `axiom5-b-glyph`,
`kernel-argument-normalization`.

This package is drafted to land via the `def-` node route. If you rule a
different home, these entries migrate whole; nothing here forecloses that.

*(The decoys, listed so the label cannot re-collide: the 2026-06-05 gravity-sweep
`W4` (`2026-06-05_gravity-sector-session-handoff.md:38`); the W1–W6
nonlinear-battery leg (`2026-07-10_rulings-docket.md:1636`); the anisotropy
residual `W4` (`open-items/2026-07-28-anisotropy-observable.md:48`); the
2026-08-03 wall-taxonomy `(W4, W5)` placement item. The docket's own D1 lesson
applies — the date disambiguates, not the letter.)*

**Branch fence — ★ NOW EMPTY. Nothing in this package is branch-pending.**

- **smith-annulus: PR #1007 MERGED** (`044a10cf`). The Class-C result and the
  frozen expectations are **on `origin/main`**; every receipt is on a main path,
  re-verified at its current line number. `[branch:smith-annulus @ 9e302b10]`
  tags retired.
- **static-existence epic: PR #1009 MERGED** (`fc154aa6`) — **changed since the
  last version of this packet, which said "still branch-pending".** The walk
  record, the epic, the build-brief, the G1 walk packet and the P0 capability
  report are all **on `origin/main`**. Every
  `[branch:static-existence-epic @ f29cb576]` tag is **retired** and replaced by
  a main relative link. **One measured drift:** epic **guard 8 moved from
  `:139-145` to `:149-155`** and is re-pinned; the walk-record line numbers did
  **not** move and were re-read byte-for-byte.
- **engine Γ means-test: PR #1010 MERGED** (`119ef8f2`) — **new since the last
  version of this packet.** The frozen prereg and the result are on
  `origin/main`. **This one has teeth: it bears directly on T5's rider (a) —
  see the Grant question there.**

**Consequences for counts you were shown**, all re-run at `fc154aa6`:
`response map` **21 hits / 7 files** (was 0 at first drafting, 4 at round 1);
`tube phase` **7 hits / 7 files, all on main** (was "0", then "1 on main + 7 on
the branch"); `ratio lock` **26 / 10**; `static existence` **12 / 6**;
`common-mode` **441 / 164**; `SmithTrefoil` **1**, not 0. Every one of these
deltas was enumerated and is **same-sense, same-arc** — no term's sense
classification changed between the two pins, only the numbers. The two clean
coinages (`presentation torus`, `detuned presentation`) are **still 0** by three
methods each, now measured *after* the branch merged, which is the stronger
test.

---

## T1 — "common-mode" / "differential" (def-cmdiff) — ★ NOT a coinage; re-scoped

Proposed noun: **common-mode / differential**, as a **disambiguation view**, not a
new class. Physical picture: the instrumentation-amp carve — an influence that
rescales every reference together cancels out of everything observable
(clause-Q, gauge); one that couples asymmetrically across modes or sites is the
physical one (clause-G).

**★ What the audit found, stated plainly: the carve you were told this entry
would coin is already canon.**
`common/translation-tables/translation-circuit.md:115-116` carries both rows —
*"Uniform external field | **Common-mode bias** — a uniform DC offset on the whole
ladder"* and *"External field gradient | **Differential bias** — a bias gradient
across the ladder"* — and the :115 row's own third column already says
*"a uniform DC bias is gauge-relative and self-cancels (the common-mode component
a differential measurement rejects)"* (`clm-acdc07` (i)). `envelope-anatomy.md:88`
restates it. So the physics is CANON; the entry is now RESTATEMENT-grade and
points at those rows.

**★ Second audit finding, and the one with teeth: a fourth register that runs the
opposite way.** In the port/irrep register, "common-mode" names the **+1
symmetric port-sum eigenspace = the A1 scalar/dilatation grade** — i.e. **the
physical mass sector** (`fork_b_saturation_tank.py:30`,
`node_scattering_multiplicity.py:95,193`, `port-register.md:93`). The draft's
unqualified *"common-mode = gauge-class, self-cancelling, non-physical"* would
have cross-wired a MODE grade with an INFLUENCE class — the sector-ownership
A1⊥T2 hazard. The entry now carves it explicitly.

- **Needs your ruling:** whether a RESTATEMENT-grade disambiguation view earns a
  register slot at all, given the physics is already canon and the only *new*
  content is the three-instance assembly (chart floor MEASURED / ratio-invariance
  algebra / vertex counting CANON). The honest case **for** it is the fourth
  register above: without an entry, nothing stops the next lane from reading an
  A1 common-mode *mode* as a self-cancelling *influence*. The honest case
  **against**: an entry that restates canon rows can rot away from them.
- **Lane-executable at PROPOSED:** citing the carve by def-id in prereg guard
  text (the static-existence epic's guard 4 needs exactly this vocabulary);
  listing new instances against it without promotion.
- Declined alongside: a standalone "differential" entry — the pair is one carve,
  and bare "differential" collides with ubiquitous calculus/EE senses for no gain.
- ⚑ Withdrawn from the draft: the "71 prior corpus hits" figure (irreproducible —
  the real count is 429 lines / 161 files, scope now stated) and the implicit
  claim that all prior hits fall under the two senses shown.

## T2 — "detuned presentation" (def-dtpres) — name negotiable

Proposed noun: **detuned presentation**. Physical picture: a (2,3) winding at
fixed frequency ratio paints the same knot forever; only a differentially-detuned
reference smears it into the torus — the torus is how the invariant *appears* in
that reference, not what the object *is*. The scope analogy is exact: the ratio is
the property, the filled Lissajous band is the presentation.

This is **one of the two** terms in the package that survived both audits
**clean** as coinages — the other is T6's lead candidate, "presentation torus".
*(An earlier version of this packet called T2 "the one term"; that was an
undercount and is corrected.)* Re-verified **0 hits at `origin/main` @
`fc154aa6` by three methods** — regex, fixed-string, and hyphen-variant —
measured **after** the epic branch merged, so the old "0 on the branch" check is
subsumed by a stronger on-main one.

- **Needs your ruling:** the name itself (you flagged it negotiable), and whether
  T2 and T6 should be ONE entry — if the T6 noun is "presentation torus", T2 is
  the relation and T6 the object, and they could collapse into a single def-node
  with two registers. Options:
  - keep both (relation + object, cross-linked — as drafted);
  - merge into one "presentation" entry carrying both;
  - a different noun entirely for the relation ("reference-smeared appearance",
    "presentation under detuning").
- **Lane-executable at PROPOSED:** using the carve to keep #416/#417 readings
  straight in lane docs (charge static, carrier precesses) — that leg is measured
  canon either way.
- Honesty line: the physics reading is WALK (the record's own header); the
  def-node names it, it does not upgrade it. The envelope≈probability-cloud
  resemblance stays OUT (echo-check never run — the record's own counter-arm).
- ⚑ Repaired: the draft's EE line called this "a locked p:q pair". The register's
  own **LOCK vocabulary** entry fences that language (see T4). Reworded to a
  **fixed frequency ratio**; nothing here needs an Adler/PLL attractor.

## T3 — the tube phase "α" (def-tubalf) — ★ arc-adoption, not a coinage

Proposed noun: **tube phase**. Physical picture: the free phase of the (2,3)
family — ψ → ψ + α slides you along the family without changing the winding
class. Not an invariant; imposing a specific value imposes more than the winding
(epic guard 8, verbatim in the entry).

**★ Audit correction:** the draft said 0 prior hits. At `fc154aa6` it is **7
lines across 7 files, all on `origin/main`** (the FROZEN expectations `:75`, the
epic `:151`, the build-brief `:77`, the G1 walk packet `:90`, the P0 capability
report `:346`, the frame-invariance RECORD `:54`, the G1 AC-steady-state RECORD
`:103`). All the same sense, all this arc — so the entry is framed as bringing
**already-in-use lane vocabulary** under the gated register.

**★★ ROUND-2: THE GLYPH MENU YOU WERE SHOWN IS WITHDRAWN. Both candidates
collide. I am not offering a replacement.**

The last version of this packet offered you two mints and told you both were
free. Neither claim carried a command, a scope, or a SHA — and **both fail on
re-grep at `origin/main` @ `fc154aa6`**:

- **ϑ** was offered as *"theta-variant, currently unclaimed"*. It is not.
  `git grep -nIF '\vartheta' origin/main | wc -l` → **7 lines / 2 files**, of
  which **six** are `$\vartheta_{\mathrm{coll}}$` — **the photon-collision angle
  in the published birefringence Letter**,
  `papers/2026_birefringence_letter/main.tex:594,595,630,635,685,689`. That is
  the *same file* this package's own T1 entry cites for its optical common-mode
  register. The unicode form `git grep -nIF 'ϑ' origin/main` → **1**
  (`research/2026-07-08_paper-hardening-ledger.md:358`, `ϑ_coll`, same object).
- **φ_t** was offered as *"zero corpus collision"*. Pattern-dependent, and the
  honest reading is a collision: the LaTeX form `git grep -nIF '\phi_t'
  origin/main` → **0**, but `git grep -nIF 'φ_t' origin/main` → **5 lines / 4
  files**, and one of them is a **literal torus phase in the standing-mode
  formula** — `src/ave/utils/fast_winding_extractor.py:53`,
  `cos(qψ)·cos(φ_t)` — i.e. the *same phase-space (p,q)-winding machinery this
  term lives in. The other four are prefix matches (`φ_tor`, `φ_toroidal`,
  `Δφ_total`) and are **not** collisions; I am giving you both figures rather
  than the one that flatters the candidate.

This is the grep-completeness failure the whole repair round was about,
reproduced inside a collision-hygiene package. **No third candidate is minted
here** — the lane that mis-measured twice does not get to pick the third time.
The next candidate, if you want one, arrives with its pattern, scope and SHA
stated before it is offered.

- **Needs your ruling — the glyph, now a two-way choice with the menu removed:**
  the walks write it "α", which collides with the fine-structure constant in the
  very documents where both appear (the electron sits at $A=\sqrt\alpha$ while
  its family parameter is "α"). Live options:
  - **keep "α" but mandate the words "tube phase" at every use** (what the entry
    interim-mandates anyway — the zero-new-collision option);
  - **order a fresh glyph search**, run under the stated-pattern/scope/SHA rule,
    and rule on what comes back.
- **Also yours — a word-level question the draft buried in a space declaration:**
  bare **"tube"** now straddles the A46 fence. Canon's *tube radius* is a
  real-space length (`electron-identification.md:30` — *"Tube circumference
  $\ell_{node}$, tube radius $\ell_{node}/(2\pi)$"*; the draft cited `:77`, which
  is a different row entirely, now corrected). "Tube **phase**" is a phase-space
  angle. The entry's interim rule is *never use bare "tube"*; confirm or replace it.
- **Lane-executable at PROPOSED:** guard 8 enforcement in the G1 imposition walk
  is already epic-ratified process and does not wait on the glyph.
- ⚑ Repaired: the draft's *"a synthesizer locked N:M"* EE line is withdrawn (see
  T4's Adler note).

## T4 — "ratio lock" (def-rtlock) — ★ BLOCKER-class repair; **DECLINE is live**

Proposed noun: **ratio lock**. Physical picture: the p:q ratio is what survives
every common-mode change — rescale the whole clock and 3:2 is still 3:2; only
differential drift between the modes changes it.

**★ This is the item the audit hit hardest. Three things you were told are wrong:**

1. **"0 prior hits" is false.** `git grep -niIE 'ratio[- ]lock' origin/main` →
   **25 lines / 9 files**, including a full derivation doc headed
   *"§1 — ORG-1: MODE-RATIO LOCKING"*, a frozen prereg, a checks script with
   *"Damping-ratio locking"*, and the manuscript **FOREWORD** (`00_foreword.tex:133`,
   *"multipole ratio-locking"*) where it is a named **forward falsifier**. A reader
   meets two different technical "ratio lock" objects. The entry is re-scoped to
   `status: ambiguous` with a full disambiguation row.
2. **The EE line violated the register's own cage.** The draft wrote *"injection
   locking / PLL ratio lock is bedrock EE"*. The standing **LOCK vocabulary** entry
   in the same register rules the opposite: *"Literal PLL / injection locking
   imports a **dissipative attractor**: Adler locking needs a limit cycle, i.e.
   gain plus loss. **Axiom 3 forbids that in the cold phase** — two lossless
   coupled oscillators beat, they do not Adler-lock."* — with **FORBIDDEN
   LANGUAGE:** *"settling into lock"*, and *"a lock word with no phase attached is
   a mis-use"*. The Adler carve now travels inside T4, T2 and T3.
3. **The canon label was smuggled.** The draft's canonical-home said *"the (2,3)
   lock the term names is CANON (`boundary-observables-m-q-j.md`)"*. That leaf
   contains **no lock language** — one "lock" token, and it is *"lockstep"* in a
   $k_{\max}$ relabel note. What is canon there is the **winding** (`:54`). Worse,
   canon owns the (2,3) as a **STATIC imposed Link** (#416), and the nearest
   *dynamical* lock test reads **NEGATIVE** — `def-satrim` records
   *"#59 phase-space carrier-lock"* among the negatives. The entry now reads
   **"the WINDING is CANON; the frequency-LOCK reading is WALK"** and carries the
   #59 negative.

- **Needs your ruling — two options, and I am not picking for you:**
  - **(a) KEEP as re-scoped** — an `ambiguous` disambiguation entry that points at
    the ORG-1 family and mandates *"ORG-1 mode-ratio locking"* vs *"the (2,3)
    carrier-ratio invariance"*, never bare "ratio lock".
  - **(b) DECLINE the term** — the ORG-1 family owns the words and will not stop
    using them; the (2,3) invariance is one sentence of elementary algebra that
    could live as a clause inside `def-dtpres` instead of minting a colliding
    surface form. Cost: nothing then warns a reader that two objects share the
    phrase.
- Secondary: the entry names (without promoting) your
  identity-lives-in-the-frame-invariant-part reading as WALK; strike that sentence
  if you want the entry purely mechanical.
- **Lane-executable at PROPOSED:** nothing beyond citing the disambiguation. ⚑
  *Repaired:* the draft claimed the walk-record §5 channel sentence *"uses exactly
  this vocabulary"* — it does not; that sentence is T1/T2/T6 vocabulary and has
  been moved to T6 below.

## T5 — "response map" vs "orbit" (def-rspmap)

Proposed noun: **response map**. Physical picture: Γ(A) is the medium's curve,
like an S11-vs-drive sweep on a network analyzer — a property of the DUT. The
electron doesn't ride it: it sits parked at $|\Gamma_J(\sqrt\alpha)| = 0.334147$,
0.12% into the annulus, and does not sweep. The annulus is the image of the map,
not anybody's trajectory — the `vcanon-3` MAJOR repair is the precedent this
entry fossilizes.

**★★ ROUND-2: rider (a) is contradicted at the `A=0` endpoint by a run that
merged AFTER this packet was last built. Surfacing, not resolving.**

PR **#1010** (`119ef8f2`) landed the **engine Γ(A) means-test** — the same map,
measured **on the lattice** rather than as a lumped step family. Three verbatim
lines from `research/2026-08-24_engine-gamma-meanstest_result.md`:

- `:214-215` — *"the outcome the prereg's own floor-honesty note foresaw (T4
  homogenization: the −1/3 intercept belongs to the isolated vertex, **which
  does not exist in-lattice**)"*
- `:305-306` — *"no floor was measurable at either stepped config; no crossing
  existed to compare"*
- `:447-449` — *"no measurable −1/3 floor — and quantitatively it draws the
  **core** locus (z = √S plane-interface reflection) to ~1 %"*

Against rider (a) as drafted: *"only the endpoints ($|\Gamma| = 1/3$ and $1$)
are profile-robust"*. The two are **not formally the same object** — one is a
lumped analytic map, the other a lattice measurement — but a def-node exists to
be cited **without** its context, and this one's whole purpose is preventing
map-vs-orbit conflation. So the entry now carries an **in-lattice caveat** (never
cite `1/3` as a measured in-lattice value) and its canonical home is now a
**pair**: the smith-annulus doc as the *analytic* home, the means-test
prereg/result as the *measured* home. **I have not reworded the annulus framing
to make the disagreement go away** — that call is yours, below.

**Rider (b) SURVIVES and is now doubly sourced.** Same result doc, `:298-300`,
verbatim: *"**No §6.4 row fires for the J/B pair; the J/B side-assignment fork
is NOT adjudicated by this run and remains open on the B side.**"* (G-B returned
INVALID-EXTRACTION — neither "draws B-class" nor "NONE".) The run that amended
rider (a) **confirms** rider (b).

- **Needs your ruling:** ratification, plus confirming the two riders travel as
  part of the term's meaning: (a) **lumped-step caveat + the new in-lattice
  caveat** — intermediate-A values are step-family artifacts, and the `1/3`
  endpoint is an isolated-vertex idealization with no measured lattice floor;
  (b) **FORM J-vs-B side-assignment (STUCK-POINT #2) stays open**, so "the
  response map" off the endpoints is underspecified without a FORM tag.
- **And the question the re-audit put to you verbatim:**
  > `def-rspmap`'s `1/3` endpoint (M3) — does the lumped-map "profile-robust
  > endpoints" rider survive a lattice run that measured no floor and drew the
  > core locus instead, or does the term need an in-lattice caveat before it can
  > be ratified?
- **Lane-executable at PROPOSED:** the orbit/response-map carve as a review lens
  on any Smith-chart figure or claim (it already caught one MAJOR).
- ⚑ Staleness repaired twice: with #1007 and then #1010 merged, the term is no
  longer 0-hit — **21 hits / 7 files at `fc154aa6`, all this arc, one sense**
  (0 → 4 → 21 across the three pins). The entry is re-framed as an adoption and
  every receipt is cited to a `origin/main` path, re-verified at its current line
  number. The draft's "lane claim-ids attach at merge" note is **withdrawn**:
  neither the smith-annulus lane nor the means-test lane mints a `clm-`, so there
  is nothing to attach, and the entry's `clm-cross-links` field now says exactly
  that. *(Round-2 fix: the field had still carried the withdrawn promise in its
  text while the log said it was withdrawn — register and packet now match.)*

## T6 — ★ THE ENVELOPE COLLISION (fatal-class): def-prstor + disambiguation block

The word "envelope" carries **FOUR** def-noded / canon-rowed senses crossing the
A46 fence. *(The draft showed you three. The audit's fourth-sense hunt came back
POSITIVE and it is a SOLID node, so the inventory is four and the old "sense 3"
is now sense 4.)*

1. **real-space three-surface anatomy / the wall** — `def-anat3s` + `def-envl0p`
   Sense A; `envelope-anatomy.md:13`, quoted byte-exact (*"the three surfaces
   below are **radial loci on the real-space saturation profile** $S(A(r))$, NOT
   phase-space contours"* — round-2 fix: the earlier version opened mid-phrase
   and dropped *"radial loci on the"*); $r_{env}$ `def-088f0d`; and your
   2026-07-15 word-level ruling: "envelope" canonically denotes the wall.
2. **reactive-amplitude envelope $A$** — DP-1, your 2026-07-02 ratification:
   *"reactive-amplitude **envelope** (the cycle time-average / conserved reactive
   energy of the $(V_{inc},\Phi_{link})$-type tank), NOT an instantaneous phase
   snapshot"*, `substrate-perspective-electron.md:62`; the `def-envl0p` Sense-B
   family.
3. ★ **the A1 breather's slow envelope $A(r,t)$** — **`def-envcar`**,
   `vocabulary-register.md:1051-1062`: *"a slow **ENVELOPE** $A(r,t)$ = the
   energy-density / operating-point **bias pattern** (what gravitates; what
   translates when the star orbits)"*, **SOLID for the decomposition**. This is a
   **real-space** bias texture, so it is not separated from sense 1 by the A46
   fence at all — only by level-of-description. **The draft missed it entirely.**
4. **the phase-space tube-phase-family torus** — the un-owned squatter: the
   2026-08-24 walks (*"The torus/envelope appears only under differential
   detuning"*) and the channel's `SmithTrefoilEnvelope` class name.

Sense 4 against sense 1 is a direct phase-space-vs-real-space collision — the
exact A46 failure mode the register exists to catch, in the word your ruling
already assigned to the wall. KEEP-BOTH treatment as drafted: senses 1–3 are
untouched, sense 4 gets a new name plus a four-row disambiguation block
(extension, never redefinition-in-place).

- **Needs your ruling — the new noun.** Candidates, with the register's naming
  conventions applied (0-prior-hit check re-run on main **and** on the branch, no
  reuse of a colliding token, no colliding glyph, space-declared):
  - **"presentation torus"** (drafted lead) — 0 corpus hits, both states; pairs
    naturally with T2; says what the object IS (a presentation) and WHERE it lives
    (a torus in the portrait); no banned tokens.
  - **"detuned presentation"** as the noun doing double duty — merges T2/T6 into
    one entry; loses the torus-shape information.
  - **"tube-phase family torus"** — maximally literal, clunky; note it inherits
    T3's unresolved glyph/word question, so it is only "safe" after T3 is ruled.
  - **"α-family envelope" — recommend DECLINE:** keeps the colliding word
    "envelope" AND the colliding glyph α; fails the naming convention twice.
- **Also yours — the channel-repo candidate sentence.** The walk record §5 offers,
  for the channel (their court): *"common-mode changes can't paint the torus; only
  a differential detuning precesses the knot into its envelope."* ⚑ **That
  sentence violates the very rule T6 proposes** — bare "envelope" for sense 4.
  Under the proposed rule it would read: *"common-mode changes can't paint the
  presentation torus; only a differential detuning precesses the winding into
  it."* Accept, reject, or exempt the channel.
- **Also yours:** whether the channel repo should rename `SmithTrefoilEnvelope`
  (their court — the entry flags, doesn't police). ⚑ **Round-2 count correction:**
  the earlier version said the name has **0** in-corpus hits. At `fc154aa6` it has
  **1** — `research/2026-08-24_frame-invariance-observer-walk_RECORD.md:52`, which
  arrived with #1009: **this arc's own walk record naming the channel class**, not
  an independent corpus use. The class still lives outside this corpus, so the
  conclusion is unchanged — nothing here depends on it — but the count now matches
  the corpus.
- **Lane-executable at PROPOSED:** the never-bare-"envelope"-for-sense-4 rule as
  a review lens; the disambiguation block as a reading aid in lane docs.
- ⚑ Also repaired: the block's sense-2 receipt inherited `def-envl0p`'s
  `substrate-hysteresis-index.md:24,136` cite. `:136` has drifted (it now holds an
  unrelated `#744` note); the block cites `:24` only and **flags** the stale half
  for whoever owns `def-envl0p` rather than silently editing that node.
  **★ Round-2 widening: the stale `:136` is in THREE of that node's fields, not
  one** — `vocabulary-register.md:425` (`canonical-home`), `:427`
  (`open-ambiguity-flag`) and `:428` (`verification`, twice). Routed to the
  auditor lane in **§CORPUS-FLAGS F3** below; still not edited here.

## T7 — "static existence" (def-stexst) — ★ collision found; re-scoped

Proposed noun: **static existence**. Physical picture: three different questions
about the railed core — can the dynamics build it (formation: **leans-falsified /
closed-negative**, the energize-LOCK route — ⚑ round-2 fix, the hedge now travels
because canon's own leaf carries both words at
`saturation-rim-inversion.md:57`: *"the **leans-falsified energize-LOCK formation
route** (pumped genesis from a free precursor, closed-negative…)"*, and a def-node
gets cited without its context),
how does the medium react when probed (response: measured, Class-C — now on main
as PR #1010), and does the
configuration exist as a self-consistent stationary state at all (existence:
open). EE version: start-up transient vs small-signal response vs whether the DC
bias point exists — existence of the operating point is not reachability by any
start-up path.

**★ Audit correction:** the draft said *"exactly 1 prior main-corpus hit"* and
*"no collision"*. Both false. There are **12 hits across 6 files** at `fc154aa6`
(10 / 5 at the round-1 pin; the +2 is the epic itself arriving on main with
#1009, same sense as ours), and the worst
one runs the **opposite way**: `research/2026-06-23_engine-stage2-native-cage_prereg.md`
uses the same phrase for a sibling object with the opposite verdict word —
*"the **settled** static existence"* (`:894`), *"(static existence
**established**)"* (`:898`) — for
the engine-stage2 `c_eff(V)` cage question. A grep-consumer of a new
OPEN-by-definition term would land straight on "established" text. The entry is
re-scoped to `status: ambiguous` with a KEEP-BOTH row separating the settled
stage-2 object from the OPEN (2,3) railed-core object, plus a third object
neither audit named (the compactness-limit *"STATIC existence inequality"*).

- **Needs your ruling:** ratification of the carve (which is unchanged and is your
  own epic §1, GO recorded verbatim), **plus** whether you want the three-way
  disambiguation carried in the register or the phrase retired in favour of an
  unambiguous one (e.g. "railed-core eigenmode existence"). The entry deliberately
  prefers neither §2 branch.
- **Lane-executable at PROPOSED:** the epic's own phases already run on this
  vocabulary; the def-node makes it citable by id, including the P0(b) guard that
  the phase-space→real-space imposition map cannot be presumed.
- ⚑ Flagged, not fixed: `saturation-rim-inversion.md:55` cites the open-item
  wording as `program-arc-map.md:118`; on `origin/main` the quoted text is at
  `:119`. The entry cites the correct line and surfaces the corpus off-by-one for
  the auditor lane.

---

## Roll-up of what is yours vs the lanes'

- **Yours (rulings):**
  - **T1** — does a RESTATEMENT-grade disambiguation view earn a register slot,
    given the carve is already canon at `translation-circuit.md:115-116`? (The
    case for: the A1 common-mode *mode-grade* cross-wiring hazard.)
  - **T2** — the name; and the T2/T6 merge question.
  - **T3** — ★ the glyph, **with the candidate menu withdrawn**: keep-α-with-
    mandated-words, or order a fresh glyph search under the
    stated-pattern/scope/SHA rule. **Both previously-offered mints collide**
    (ϑ = the birefringence Letter's collision angle, 6 hits; φ_t = the winding
    extractor's torus phase). **And** the bare "tube" word rule.
  - **T4** — ★ **KEEP-as-re-scoped vs DECLINE.** This is the one item where the
    draft you were shown was materially wrong three ways.
  - **T5** — ratification, with its two riders — ★ **and now the annulus-framing
    question the merged means-test forces** (rider (a)'s `1/3` endpoint).
  - **T6** — ★ the fatal-class item: the new noun, **now against a four-sense
    inventory**; plus the reworded channel sentence.
  - **T7** — ratification of the carve, plus keep-the-phrase-with-disambiguation
    vs retire-the-phrase.
  - **Standing:** the collision-register-home question (opens-walk W4) above.
- **Lanes' (at PROPOSED, no ruling needed):** guard-8 enforcement; the
  orbit/response-map review lens; the never-bare-"envelope"-for-sense-4 rule;
  citing any entry by def-id with its PROPOSED/ambiguous status shown.
- **Declined (no entry drafted):** standalone "differential" (folded into T1);
  "orbit" (standard usage owns it; the T5 entry carries the carve).
- **Withdrawn from the drafts you were shown (all false or irreproducible):**
  *Round 1* — T4's "0 prior hits"; T7's "exactly 1 prior hit / no collision";
  T1's "71 hits" and its "the class definition is a coinage"; T3's "0 prior
  hits". *Round 2* — **T3's entire glyph menu** ("φ_t … zero corpus collision"
  and "ϑ … currently unclaimed", both false); T6's "`SmithTrefoilEnvelope` has 0
  in-corpus hits" (now 1); T5's "4 hits / 2 files" (now 21 / 7). Commands and
  replacement counts, every one with its SHA: `register-additions.md`
  §VERIFICATION LEDGER (V1–V13).

---

## ★ THE TWO OPEN QUESTIONS, verbatim as the re-audit put them

Reproduced word-for-word rather than paraphrased, because a dispatch paraphrase
that drifts becomes the lane's verdict pivot:

> 1. `def-rspmap`'s `1/3` endpoint (M3) — does the lumped-map "profile-robust
>    endpoints" rider survive a lattice run that measured no floor and drew the
>    core locus instead, or does the term need an in-lattice caveat before it can
>    be ratified?
>
> 2. The T3 glyph menu is now a two-option menu with both options colliding (M2).
>    Re-derive candidates, or drop the menu and rule on "keep α with mandated
>    words"?

*(Question 1 also sits in T5 above, at the point of decision; question 2 in T3.
Both are repeated here so the roll-up is complete on its own.)*

---

## ★ §CORPUS-FLAGS — three findings ABOUT the corpus, routed to the auditor lane

**These are not package defects and are NOT fixed here.** Each is another node's
field or another lane's leaf; editing them from this package would exceed its
scope and erase the drift signal. Recorded with file:line and verbatim content so
the auditor lane can act without re-deriving.

**F1 — 12 live `def-` entries with `open-ambiguity: YES` materialize an EMPTY
`conflicting_sites` array.** Measured, not inferred: `parse_definition_entries`
run on the **unmodified live** `vocabulary-register.md` at `origin/main` @
`fc154aa6` → **62 nodes**, **36** with the ambiguity flag truthy, **12** of those
with `conflicting_sites == []`: `def-quant3`, `def-de17a0`, `def-095760`,
`def-u0star`, `def-envl0p`, `def-portmp`, `def-4b1a2c`, `def-ch0rd1`,
`def-ech0v1`, `def-0penlp`, `def-t2ph01`, `def-mstar1`.
**Cause, verified at `vocabulary-register.md:1167`** (`def-mstar1`'s sub-bullet):
cites are written as `` `19_silicon_design_engine.tex`:45 `` — **the line number
falls outside the backticks**, and `_DEF_CITE_RE` (`kb_index_lib.py:102`,
`` `([^`]+:\d[\d,\-]*)` ``) only matches a `path:line` **inside** them. The entry
parses and lands; its collision record just silently evaporates.
**Why this matters here:** `def-satrim` and `def-mstar1` are the two exemplars
this package copied its template from — `def-satrim` materializes 4 sites,
**`def-mstar1` materializes 0**. This package's own four YES entries use the
in-backtick form and all four materialize (**`def-cmdiff` 8 / `def-tubalf` 12 /
`def-rtlock` 9 / `def-stexst` 6**), so the package is
clean; the corpus exemplar is not. This is precisely the silent-rot failure the
`collision-register-home` open item names as the reason a CI-gated home is the
right home — happening inside the gated home.

**F2 — the trimmed COUNTING-fact quote this package fixed in itself is now on
main, in two files.** Canon leaf `manuscript/ave-kb/common/translation-tables/translation-circuit.md:189`
reads *"a COUNTING fact — one bond feeding two, immune to symmetric
transformation"*. Two 2026-08-24 research docs now on main carry it trimmed:
- `research/2026-08-24_frame-invariance-observer-walk_RECORD.md:32` — *"a
  COUNTING fact — immune to symmetric transformation"* (the middle clause elided
  with no ellipsis — the exact defect round-1 findings A1-6 / A2-6 flagged in
  this package);
- `research/2026-08-24_smith-annulus_result.md:83` — *"a COUNTING fact"* alone.
*(Not every shortening is a defect: `_orchestration/open-items/2026-08-24-smith-annulus-tube-ratio-pin.md:8`
uses `anchor: "a COUNTING fact — one bond feeding two"` as an explicit anchor
field, and `src/ave/viz/ave_chart.py:48,129` is code commentary. The two above
are prose quoting the leaf.)*

**F3 — `def-envl0p`'s stale `substrate-hysteresis-index.md:136` appears in THREE
fields, not one.** At `origin/main` @ `fc154aa6`, `:136` carries the `#744
(merged) … THREE-WAY DEGENERATE` note and no envelope content
(`git grep -niI 'envelope' origin/main -- '*substrate-hysteresis-index.md'` →
`:18,:24,:27,:41,:92,:104,:123,:132,:149` — **no `:136`**). The dead cite is at:
- `vocabulary-register.md:425` — `canonical-home`, as `:24,136`;
- `vocabulary-register.md:427` — `open-ambiguity-flag`, as `:24,27,136`;
- `vocabulary-register.md:428` — `verification`, **twice**, as `:24,27,136`
  (*"re-grepped two-method … THIS session at the cited sites"* — the verification
  field asserts the stale cite was checked).
Round 1 of this package named only the first. Per the vacated-cite pattern, all
three want re-pinning or dropping by whoever owns that node.

**F4 (minor, same class) — `_orchestration/2026-08-24_static-existence-epic.md:20`
says the means-test result is *"(research pair, PR pending)"*.** That PR is
**#1010, merged** (`119ef8f2`). One-word staleness on a leaf this package cites;
surfaced for the owning lane.
