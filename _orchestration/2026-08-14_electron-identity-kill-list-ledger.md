# Electron-identity kill-list ledger — Phase A inventory (2026-08-14)

**Status:** EVIDENCE — read-only inventory. **Adjudicates nothing.**
**Phase:** A (implementor) of `_orchestration/2026-08-14_electron-identity.md`.
**Fence:** `research/2026-08-14_electron-identity-checkpoint1-walk_RECORD.md` §2 (signed kills + held-out amends).
**Branch:** `analysis/electron-identity-phase-a`, worktree-isolated, base `554c5ec0`.

This ledger **quotes; it does not rewrite** (A2). Every live-wrong row carries a path,
a verbatim fragment, and the reason the page offers the corpse as *current* (A3).
No canon edit, no tracker Status flip, no banner is applied here.

---

## §0 — What "live-wrong" means in this lane

Per `ave-walk-back` Step 3h-exhaustive-3, adapted to a kill-list (the LOAD-BEARING /
STALE-PROSE analog is **offered-as-current**):

| Class | Test | Action class |
|---|---|---|
| **live-wrong** | The page offers a **signed kill** as a *current* mechanism, *current* manufacture path, or *current* identity — a reader at HEAD would take it as the standing AVE position or the next thing to do. | Phase B (tracker Status) or Phase C (canon Type D banner) |
| **Q1 preserved-historical** | Rule-12 audit trail, dated close, arc-map negative, "we tried X and it died". The corpse is named *as dead*. | none (audit trail; expected) |
| **Q2 frozen snapshot** | Journal entry, frozen prereg, result doc, session handoff, docket entry, audit-tag-preserved body, L3 archive body. Snapshot-in-time by design, not a knowledge claim. | none (Q2 exempt) |

**Ambiguity default (from the skill):** Q1 requires the corpse to be clearly named as
dead. A page that merely *mentions* a corpse historically but frames the route as
**open** defaults to live-wrong. Genuinely undecidable sites are listed in §5 and
**not picked** (flag-don't-fix).

### Fence held (not violated)

- **Held out — NOT classified as killed anywhere in this ledger:** Poincaré-class bulk
  cohesion (K1 amend; FLAG-W + exterior Coulomb) and cosmic node-injection (K3 amend,
  a *different* hypothesis). Where a live-wrong row sits on a page that *also* carries
  the Poincaré framing (row C2), the row scopes the finding to the **dynamical-lock
  clause only** and says so.
- **A5 (Grant 2026-08-14):** \(\{m_e,\alpha,G\}\) are calibration inputs and the
  **minimum set**. "Layer-8 OPEN" / "derive \(m_e\)" is **NOT** inventoried as a K4
  corpse. `research/2026-06-11_nyquist-binding-route_CLOSED.md:4` names an "OPEN
  successor … Layer-8 acceptance test" — **excluded by A5**, not a row. G's MIXED
  `/7` FORM is not touched.
- **Flag-don't-fix, not picked:** two-node vs \(0_1\); topology vs sub-yield stability;
  compositeness item vs Gate-0.

---

## §1 — Method (two-method grep, commands as run)

All commands run from the worktree root
`/Users/grantlindblom/AVE-staging/AVE-Core-worktrees/electron-identity-phase-a`
on 2026-08-14 at `554c5ec0`. Scope per the Phase A boundary: `manuscript/ave-kb/`,
`_orchestration/`, `research/2026-*.md`, plus `src/` screened for docstring status only.
`research/_archive/L3_electron_soliton/` bodies are **out** (Q1 by default; no KB leaf
was found citing an L3 body as a current mechanism).

### Method 1 — fixed-string, per K-row

```bash
# K1
rg -F -l -i -e "remanence" -e "dynamical lock" -e "LIVE THREAT" \
  -e "electron-lock" -e "reactive binding" -e "reactive LC-binding" \
  manuscript/ave-kb/ _orchestration/ research/ src/
# K2
rg -F -l -i -e "self-trap" -e "self-focus" -e "MODE-III" -e "MODE III" \
  -e "bulk localizer" manuscript/ave-kb/
# K3
rg -F -l -i -e "genesis" -e "self-assembly" -e "manufacture path" -e "genesis_v" \
  manuscript/ave-kb/
# K4
rg -l -i -e "Q ?= ?137" -e "cage-emergent" -e "Q_ringdown" manuscript/ave-kb/
# K5
rg -F -l -i -e "LOOP GAP" -e "loop-gap" -e "unified-harness" -e "loop_gap" \
  manuscript/ave-kb/
# K6
rg -F -l -i -e "mass-pin" -e "mass pin" -e "dynamical pin" -e "pins the mass" \
  -e "winding pins" manuscript/ave-kb/ _orchestration/ research/ src/
```

Line-level follow-ups used the same patterns with `-n` and without `-l`.

### Method 2 — word-fragment / regex (plurals, hyphenation, en-dash, current-offer phrasing)

```bash
for p in 'remanen(ce|t)' '(dynamical|reactive|energize)[-– ]?locks?' \
         'self[-– ]?(trap|traps|trapping|trapped|focus|focusing|assembl[a-z]*)' \
         'manufactur[a-z]*' 'loop[-_ ]?gap' 'mass[-– ]?pins?' \
         'pins? the (mass|A1|core)' 'Q\s*=\s*137' 'rank[-– ]?[1-4]'; do
  printf "%-58s %s\n" "$p" \
    "$(rg -l -i -e "$p" manuscript/ave-kb/ _orchestration/ research/2026-*.md src/ | wc -l)"
done

rg -n -i -e "still (live|the candidate|open as|a live)" \
  -e "current(ly)? (candidate|path|route|target)" -e "candidate = " \
  -e "targets P1" -e "next work" \
  manuscript/ave-kb/ _orchestration/ research/2026-*.md
```

Method-2 file counts (2026-08-14): `remanen(ce|t)` 96 · `(dynamical|reactive|energize)[-– ]?locks?` 79 ·
`self[-– ]?(trap|…|assembl[a-z]*)` 274 · `manufactur[a-z]*` 176 · `loop[-_ ]?gap` 131 ·
`mass[-– ]?pins?` 4 · `pins? the (mass|A1|core)` 15 · `Q\s*=\s*137` 64 · `rank[-– ]?[1-4]` 159.

**Method 2 surfaced no live-wrong site that Method 1 had missed.** Its extra hits were
off-fence arcs (BH-ringdown \(Q=\ell\) law, muon g-2 / FI-13, `K=2G`) — recorded here so
the negative is auditable rather than assumed.

### Screening vs counting universe (recall/precision split, stated honestly)

The broad recall union (Method 1 ∪ Method 2, all scopes) is **1028 files** — dominated by
two false-positive families that are **not** the signed corpses:

- **"genesis"** in the *cosmological lattice-genesis / node-birth* sense (the K3 **held-out
  amend**, and the \(G\)/\(H_\infty\) node-heat gloss);
- **"self-trap"** in the **\(\Gamma=-1\) / \(V_{\text{yield}}\) boundary-wall** sense — the
  **surviving** localizer, explicitly *not* the K2 bulk-interior corpse.

Counting therefore uses a **precision** pattern set (terms that name a signed corpse
specifically), which is the universe for §4:

```bash
P='remanen(ce|t)|dynamical lock|LIVE THREAT|electron-lock|reactive (LC-)?binding|energize-(and-)?lock|bulk self-(trap|focus)|self-focus(ing)?|bulk localizer|MODE-III|self-assembl[a-z]*|manufacture path|electron manufacture|manufacturing traveler|free precursor|Q ?= ?137|cage-emergent|Q_?\{?ringdown|LOOP GAP|loop-gap|loop_gap|unified-harness|mass-pins?|dynamical pin|pins? the (mass|A1|core)'
rg -l -i -e "$P" manuscript/ave-kb/ _orchestration/ src/ research/2026-*.md | wc -l
```

---

## §2 — Live-wrong rows, canon (`manuscript/ave-kb/`) → Phase C

Ten rows, nine distinct files. **Phase C = Type D Rule-12 banner** (body preserved).

### C1 — `common/the-abandoned-interior.md:65` (+ `:78`) · **K1** · live-wrong · **highest load**

> **The AVE answer-candidate (2026-06-10 adjudication — HYPOTHESIS-CLASS): the lock is the MOTION.**

and, same block, the three-part mechanism offered as that candidate:

> a three-part dynamic lock

**Why current:** the leaf presents the dynamical lock as *the standing AVE
answer-candidate* to the Poincaré question, in the present tense, with only
2026-06-10 panel results attached (`LOCK-FAIL` / `CLIP-undecided`). It closes
with the route still open (`:78`) —

> the snap channel that would birth the lock is, as of 2026-06-10, UNRESOLVED

— i.e. undecided-but-live, not closed. The arc **CLOSED NEGATIVE 2026-07-08**
(`research/2026-07-08_electron-lock-arc_CLOSE.md:3-5`: *"**CLOSED — NEGATIVE.** The
hypothesis that the electron is held together by a *dynamical binding mechanism* is
falsified across five independent loci."*). The leaf carries **no reference to that
close** (verified: `rg -c "2026-07-08" manuscript/ave-kb/common/the-abandoned-interior.md`
→ no match). Note the **held-out amend is on this same page** (Thread B's Poincaré
history + the named hole) — the finding is scoped to the *dynamical-lock candidate
clause*, not to Thread B.

### C2 — `common/physics-lineage-map.md:302` · **K1** · live-wrong

> candidate = dynamical lock (Γ=−1 wall + conserved circulation + topological quantization), graded HYPOTHESIS-class, two adversarial panels LOCK-FAIL/CLIP-undecided

**Why current:** the row's own schema column is *"AVE evasion / live threat"* and the
cell grades the dynamical lock as the **current HYPOTHESIS-class candidate** against a
STANDING killer. A reader at HEAD takes the lock as AVE's live answer. Named as
banner-fodder by the walk RECORD §3 (`:53`). **Scope guard:** the same cell's Poincaré
sentence (*"AVE's stabilizer is a modern Poincaré stress"*) is the **held-out amend** —
Phase C must banner the lock clause and **must not** banner the Poincaré clause.

### C3 — `common/loop-gap-electron-resonator-closure-doctrine.md` (whole leaf) · **K5** + **K1** · live-wrong

Present-tense offer, no status banner anywhere in the file:

- `:12` — > **WHEN TO USE:** before claiming any genesis/kernel change "closes the LOOP GAP," before scoping v11+ engine work
- `:114` — > **Meta rule:** advance LOOP GAP **ranks** (doctrine §2), not genesis version numbers.
- `:112` — > | **K4⊗Cosserat** via `VacuumEngine3D` | **ACTIVE** |
- `:31` (rank 4, K1) — > | **4** | **Constitutive remanence** | … | R2 bench **not run** |
- `:30` (rank 3, K1) — > graft-v4 energize-LOCK path **candidate**
- `:79`–`:89` — a numbered **"Engine upgrades (ordered)"** list under *"§6 — v11 direction"*

**Why current:** this is the canonical *routing aid* for the ranks. It instructs the
reader to scope v11+ work, names the platform ACTIVE, and carries an ordered
next-steps list — the K5 corpse ("ranks as *current* manufacture path") in its purest
form, with rank 3/4 carrying the K1 corpse. **The single most load-bearing canon site.**

### C4 — `common/substrate-hysteresis-index.md:155,159` · **K1** + **K5** · live-wrong

> **The LOOP GAP remains open until a mechanism supplies zero-drive persistence with nonzero enclosed loop area** — either (a) the v10 snap verdict shows retention without drive, and/or (b) the R2 ferrite B–H bench maps remanence/coercivity/loop-area to mass/annihilation/latent-heat.

Plus `:159`: > **v11 charter (2026-06-12):** prereg DRAFT … primary falsifier **P11 zero-drive persistence**

**Why current:** states an **open** condition with two enumerated live routes and a
charter pointer — offers ferrite remanence as the current path to mass.

### C5 — `vol9/ch3-pin-port-configuration/device-circuit-models.md:123,127` · **K1** + **K3** + **K5** · live-wrong

- `:123` heading — > ### 5. LOOP GAP — manufacture closure pointer (2026-06-12)
- `:127` — > Electron manufacture requires **bulk** \(\Gamma_{\mathrm{bulk}}\to -1\) confinement …, Compton-scale ring-up, conservative energize-lock, and Level-2 remanence … v11 targets P11 quiescence gate.

**Why current:** present-tense requirements for *"Electron manufacture"* (K3) built out
of energize-lock + remanence (K1), closing on a forward-looking *"v11 targets"* (K5).

### C6 — `common/engine-capability-map.md:32,67,82,112,127` · **K1** · live-wrong

- `:32` — > mass persists at zero drive (ferrite \(B_r\) analogue); the canonical kernel is anhysteretic, so this is the open R10 gap
- `:82` — > **R10 (anhysteretic↔loop / remanence, §3.3) stays the SEPARATE retention wall**
- `:112` — > add constitutive loop (remanence)     ← OPEN: must be emergent, not an imposed latch
- `:127` — > The loop (R10 remanence) is the deepest: the kernel is anhysteretic, and every "retention" so far is imposed

**Why current:** the leaf's §2 matrix is self-declared **VERIFIED-STATE**, and it lists
remanence as an **OPEN capability gap the engine must still close** — i.e. remanence is
still the named mechanism for retention. The file carries three 2026-06-24/07-03
banners about the **localizer** (K2/K6) but **none** about K1 remanence.

### C7 — `common/engine-capability-map.md:109` · **K2** + **K3** · live-wrong

> seed photon precursor → self-trap     ← cage AND winding emerge together (not planted)

**Why current:** a staged-growth build order presented as the program's construction
path — a **free-precursor seed** (K3) whose next step is **self-trap** (K2, the
bulk-interior reading). The §1 reframe banners sit ~80 lines above and scope the *DOF
table*; this ASCII build-order block is outside their stated reach and reads as the
current plan.

### C8 — `common/figures/engine_capability_matrix.yaml:31,39` · **K1** + **K2** · live-wrong

- `:31` — > why: "rest mass = self-trapped LONGITUDINAL-bulk wall; c_eff->inf at the saturated core self-creates the Gamma=-1 TIR cage"
- `:39` — > name: "constitutive loop (remanence)"

**Why current:** the machine-readable backing data for the capability figure. It carries
**no banner mechanism at all** (YAML), so the bulk self-trap phrasing the prose leaf
banners at `:13`/`:15` is un-scoped here — and this is the artifact a figure or a
downstream tool reads.

### C9 — `common/historical-precedents.md:56` · **K3** · live-wrong

> The **full `(2,3)` self-assembly** (needs the coupled K4+Cosserat engine) + the stiff-wall integrator are the *localized* remaining gaps.

and

> full graduation toward a load-bearing photon↔electron-split leaf is gated on the `(2,3)` self-assembling.

**Why current:** self-assembly is offered as a **remaining gap** and as an **active
gate** on a canon promotion — i.e. a live manufacture path, when the five self-assembly
routes are signed FAILED (K3).

### C10 — `common/index.md:63` · **K5** · live-wrong

> Routing-aid synthesis (2026-06-12): ranked plumber closure order, three genesis lanes (cosmic / manufacture / emission), three-channel routing, v9–v15 directions

**Why current:** the common-resources index — the front door to canon — advertises the
doctrine (C3) as a current routing aid with *"v9–v15 directions"*, with no superseded
marker. Whatever Phase C does to C3 must land here too or the index re-offers it.

---

## §3 — Live-wrong rows, trackers → Phase B (Status only, no canon rewrite)

Seventeen rows. All are **status-language** findings: the physics bodies stay (Rule 12 /
"do not delete"); only the ACTIVE/LIVE/PENDING framing is at issue.

| # | Path : line | K# | Verbatim fragment | Why offered as current |
|---|---|---|---|---|
| B1 | `_orchestration/2026-06-12_loop-gap-unified-harness.md:3,6` | K5 | `**Status:** ACTIVE` + `**Next work:** D-lite … → C′ scalar restoration` | The K5 epic is ACTIVE and names the next two branches. Epic Phase B names this row explicitly. |
| B2 | `_orchestration/2026-06-12_loop-gap-engine-dag.md:3` | K5 | `**Status:** LIVE — **loop-gap-platform manifest** for K4⊗Cosserat electron closure` + Platform-rule `**ACTIVE** \| All rank-1–4 closure work` | Declares the rank platform LIVE and routes *all* rank-1–4 work to it. |
| B3 | `_orchestration/2026-06-12_loop-gap-orchestration-plan.md:3` | K5 | `**Status:** ACTIVE — authoritative execution sequence for the K4 harness pivot` | Self-declared **authoritative execution sequence**. |
| B4 | `_orchestration/2026-06-12_loop-gap-first-principles-implementor-brief.md:3` | K5 | `**Status:** ACTIVE — canonical handoff for orchestration + implementor sessions` | A dispatchable implementor brief for the killed path. |
| B5 | `_orchestration/2026-06-12_loop-gap-v11-charter.md:4` | K5 + K1 | `**Status:** CHARTER ACTIVE — prereg DRAFT; implementor **PENDING** freeze` | Charter awaiting freeze = queued work; its falsifier is P11 zero-drive remanence. |
| B6 | `_orchestration/2026-06-12_loop-gap-v12-charter.md:4` | K5 | `**Status:** CHARTER ACTIVE — prereg DRAFT; implementor in-session` | "in-session" reads as work in flight. |
| B7 | `_orchestration/2026-06-12_loop-gap-v13-charter.md:4` | K5 | `**Status:** CHARTER ACTIVE — prereg DRAFT; implementor in-session` | Same. |
| B8 | `_orchestration/2026-06-12_loop-gap-v14-charter.md:4` | K5 | `**Status:** CHARTER COMPLETE — CAVITY-BREAK landed; v14b pocket-frame peak OPEN` | COMPLETE, but leaves **v14b … OPEN** as a live successor. |
| B9 | `_orchestration/2026-06-12_loop-gap-v15-charter.md:4` | K5 | `**Status:** CHARTER ACTIVE — Phase 1 COMPLETE (HEAL-CONFIRMED); Phase 1b ablation PENDING` | A PENDING ablation phase on the killed path. |
| B10 | `_orchestration/2026-06-13_loop-gap-corpus-engine-coverage.md:3` | K5 | `**Status:** LIVE — orchestrator-maintained belief map` | A **LIVE belief map** for the killed arc. |
| B11 | `_orchestration/2026-07-12_remanence-r10-charter.md:3` | K1 | `**Status.** CHARTER + FREEZE — no driver yet.` | A frozen charter **awaiting a driver** = remanence is queued, not closed. Post-dates the 2026-07-08 close by four days. |
| B12 | `_orchestration/2026-06-04_full-electron-option-B-discrete-emergence.md:3` | K3 | `**Status:** PENDING — implementor dispatch (worktree-isolated).` | An undispatched implementor brief for discrete electron emergence. |
| B13 | `research/2026-06-12_genesis-program-status.md:3` | K3 + K5 | `**Status:** LIVE LEDGER — single routing doc for discrete srs genesis stack` | Self-declared **LIVE** routing doc for the genesis stack. Epic Phase B names it SUPERSEDED. |
| B14 | `research/2026-06-12_loop-gap-harness-phase2_result.md:4` | K5 | `**Status:** IMPLEMENTOR — pending production battery fill` | A result doc left **pending a production fill** = an unfinished live run. |
| B15 | `research/2026-06-12_genesis-v13-eigen-cavity_prereg_DRAFT.md:3` | K5 + K3 | `**Status:** DRAFT — Grant freeze pending` | **DRAFT, not FROZEN** — so the Q2 frozen-prereg exemption does **not** apply; it sits in the queue awaiting a freeze. |
| B16 | `research/2026-06-12_genesis-v14-cavity-transport_prereg_DRAFT.md:3` | K5 + K3 | `**Status:** DRAFT — Grant freeze pending` | Same. |
| B17 | `research/2026-06-12_genesis-v15-nucleation-from-latent_prereg_DRAFT.md:3` | K5 + K3 | `**Status:** DRAFT — Grant freeze pending` | Same. Epic Phase E: *"No genesis \(vN\)"*. |

Listing command for B15–B17:

```bash
rg -l "^\*\*Status:\*\* DRAFT" research/2026-*.md | rg -i "genesis|loop-gap"   # → 3
```

---

## §4 — Counts

**Counting universe** = files matching the §1 precision pattern set in the IN-scope
paths. `src/` is screened but **excluded from Q-classification** (Phase A scope: engine
code is OUT except docstring status presenting manufacture as live — none found, see §6).

```bash
# run 2026-08-14 from the worktree root, at 554c5ec0
for d in manuscript/ave-kb _orchestration src; do
  printf "%-22s %s\n" "$d" "$(rg -l -i -e "$P" "$d" | wc -l)"
done
printf "%-22s %s\n" "research/2026-*" "$(rg -l -i -e "$P" research/2026-*.md | wc -l)"
rg -l -i -e "$P" manuscript/ave-kb/ _orchestration/ src/ research/2026-*.md | wc -l
# → manuscript/ave-kb 43 · _orchestration 61 · src 90 · research/2026-* 188 · TOTAL 382
```

| Class | Files | Rows | Basis |
|---|---:|---:|---|
| **live-wrong** | **26** | **27** | §2 (9 files / 10 rows) + §3 (17 files / 17 rows) |
| **Q1 preserved-historical** | **114** | — | 292 − 26 − 152 |
| **Q2 frozen snapshot** | **152** | — | 132 research frozen + 20 `_orchestration` journal |
| *(screened, out of Q-scope)* | *90* | — | `src/` engine code |
| **IN-scope universe** | **292** | | 43 + 61 + 188 |

Q2 subset listing commands:

```bash
rg -l -i -e "$P" research/2026-*.md \
  | rg -i "_prereg|_result|_RECORD|FROZEN|handoff|_design|_smoke|_CLOSE|adjudication|_note" | wc -l
# → 136, minus the 4 that are live-wrong rows B14–B17 → 132
rg -l -i -e "$P" _orchestration/ | rg -i "handoff|docket|session|trace|_archive|prework" | wc -l
# → 20
```

Q1 is a **residual** count, not an enumeration: 292 in-scope files minus the 26
live-wrong minus the 152 Q2. Spot-verified Q1 exemplars (each names the corpse *as
dead*, so each is correctly no-action):

- `vol2/…/electron-identification.md:13,15` — two stacked Rule-12 banners; `:64` states the genesis/self-lock arc is **closed-negative** and \(Q=1/\alpha\) is an identity, not a derivation.
- `vol2/…/mass-closure-theorem.md:24,26` — CLOSURE-MECHANISM SCOPING + LOCALIZER RELABEL (K2 + K6 both correctly retired).
- `vol4/…/unified-engine-design-doctrine.md:145,328,339,352` — bulk self-trap named a *"ruled-out Cartesian artifact"*, and re-running it is called **substitution-not-retraction**. Exemplary.
- `common/program-arc-map.md:97,357` — ARC-08 with a bounded window and *Verdict:* **NEGATIVE (leans-falsified)**.
- `common/saturation-rim-inversion.md:57` — a GUARD that separates the `clm-satnec` static test from the *"falsified energize-LOCK formation route"*.
- `common/genesis-chord-falsification-ledger.md` — the negatives ledger itself (but see §5.1).

---

## §5 — Unsure: Q1 vs live-wrong. **Not picked** (flag-don't-fix)

These four are listed, not classified. Each is a Rule-12/historical container that
*also* carries a forward-looking clause — the exact boundary the skill's ambiguity
default does not cleanly resolve.

**5.1 — `common/genesis-chord-falsification-ledger.md:26` (K3).** Inside a 🔴 SECTION
REFRAME banner (Q1-shaped) sits:

> the substrate-correct test — does a self-trapped Γ=−1 region carry 𝓜=m_e, 𝓠=e, 𝓙=ℏ/2 with the winding EMERGING α-free — was **never run**; it is the open re-aim

Live-wrong reading: a *named open re-aim* for genesis. Q1 reading: it is the diagnostic
half of a negative ("what these negatives do and don't rule out"), which is the ledger's
whole job. Also note the α-free FORM-emergence framing is **not** an A5 violation (it does
not ask for \(m_e\)).

**5.2 — `common/program-arc-map.md:97` ARC-08 `Opened:` field (K3).**
> *Opened:* the α-free boundary-observable re-aim; the two-sector engine.
Same clause as 5.1, in a dated arc row with `Verdict: NEGATIVE` — I lean Q1 on the
container (bounded window, explicit negative) but the field does state an opened route.
Consistency with 5.1 is an orchestrator call.

**5.3 — `common/the-abandoned-interior.md:52` and `:228` (K3).**
> Kelvin resumed is a **hypothesis with a working confinement step and an open self-assembly step**
Read as honest-negative prose ("the named hole, no triumphalism") it is Q1; read as a
status claim it offers self-assembly as open (live-wrong, and adjacent to C9 which I did
classify live-wrong). C1 on the same page is unambiguous; these two are not.

**5.4 — `vol2/…/electron-bound-resonator-coverage.md:103` — not classified under any K-row.**
> ### THE load-bearing next step (do this ONE thing first)
Epic Phase B names this for demotion, and it does present a coupled-network \(Q\)
derivation as *"the single load-bearing next move for the whole network"*. But it is
**not a K4 corpse**: it explicitly disavows the corpse — *"The honest target is the
**OBSERVED** electron \(Q\), **NOT** the baked \(137\)"* and *"slot stays EMPTY"*. Forcing it
into K4 would violate the fence, so **no K-row is asserted**. Phase B's basis for
demoting it is priority-ordering, independent of this ledger.

---

## §6 — Negative findings (asserted with the command that justifies them)

- **K4 is clean in canon.** Every `Q ?= ?137` / `cage-emergent` / `Q_ringdown` hit found
  by the K4 grep states the corpse **as dead**: *"Q=137 slot stays EMPTY"*, *"Q_ringdown≈30.8,
  **NOT 137**"*, *"instance-baked ECHO, not a cage-emergent chord"*
  (`vol2/…/electron-bound-resonator-coverage.md:222`; `vol9/claim-quality.md:507-521`;
  `vol9/ch17-engine-requirements/index.md:41`, `engine-acceptance-suite.md:217-245`;
  `common/interlock-register.md:302`; `vol4/…/resonant-lc-solitons.md:145`;
  `vol4/…/node-up-small-large-signal.md:385`; `vol4/…/unified-engine-design-doctrine.md:384`).
  **0 live-wrong K4 rows.** Per A5, "Layer-8 OPEN" is not counted as a K4 corpse.
- **K6 is clean in canon.** `rg -n -i -e "mass-pin" -e "pins the mass" -e "winding pins" -e "dynamical pin"`
  over `manuscript/ave-kb/ _orchestration/ research/ src/` returns the fence docs
  themselves, the two Rule-12 LOCALIZER RELABEL banners
  (`mass-closure-theorem.md:26`, `electron-identification.md:15`,
  `master-equation.md:110`, `engine-capability-map.md` §1) — all Q1 — and one
  false positive (`vol4/…/project-torsion-05.md:34`, a *potted winding* in apparatus
  geometry). **0 live-wrong K6 rows.**
- **`src/` carries no live manufacture claim.** `rg -n -i -e "manufactur" -e "genesis" -e "remanence" -e "loop gap" src/ave/ src/scripts/ -g '*.py'`
  filtered for `TODO|next|target|pending|current|active|closes the` returns 7 hits, all
  either prereg-anchored driver docstrings (Q2, e.g. `electron_genesis_finish.py:2`
  cites its frozen prereg) or an explicit flag-don't-fix OPEN fork on seed strain
  (`loop_gap_seeds.py:45`), which is a strain-register question, not a manufacture
  claim. **0 live-wrong `src/` rows.**
- **The K1 close never propagated to canon.** `rg -l "2026-07-08_electron-lock-arc_CLOSE" manuscript/ave-kb/ _orchestration/ research/ src/`
  returns **4 files, none of them a KB leaf**: `_orchestration/2026-08-14_electron-identity.md`,
  `research/2026-07-08_chiral-drive-selforbit_prereg.md`,
  `research/2026-07-08_chiral-drive-selforbit_result.md`,
  `research/2026-07-20_envelope-sector-reduction_prereg-FROZEN.md`. This is the
  structural cause of C1/C2/C4/C6 rather than nine independent drifts.
- **No L3 archive body is cited as a current mechanism** by any KB leaf, so the
  out-of-scope default (Q1) holds without exception. Checked via the K1/K2/K3 file
  lists — no `manuscript/ave-kb/` hit routes to `research/_archive/L3_electron_soliton/`
  as a live route.

---

## §7 — Verification

- `make verify` — **green** from this worktree (`ALL PHYSICS PROTOCOLS PASSED`, exit 0).
  No physics change in this PR, as expected for a read-only inventory.
- `BOARD.md` — **not edited** in this PR (per the Phase A brief).
- `ave-ip-divide-discipline` — pre-commit check run: this ledger is L0 public theory
  (substrate mechanisms + corpus hygiene). No private-app repo paths, no application
  detail, no external context. All cited paths are AVE-Core-internal.

---

## Phase A outcome

**The inventory is done and it is lopsided in a useful way.**

The signed kills split cleanly into **two that propagated and four that did not.**
**K2** (bulk self-trap) and **K4** (\(Q=137\)) are *already* correctly retired in canon —
K2 by stacked Rule-12 banners across `electron-identification.md`,
`mass-closure-theorem.md`, `master-equation.md`, `l3-electron-soliton-synthesis.md`, and
an exemplary `unified-engine-design-doctrine.md` that names re-running it
substitution-not-retraction; K4 by a corpus-wide *"slot stays EMPTY"* discipline that
holds at every one of its hits. **K6** is retired by the same 2026-06-24 relabel pass.
Those three cost Phase C nothing.

**K1, K3 and K5 are the waste**, and they share one root cause: the
**2026-07-08 lock-arc close was never cited by a single KB leaf.** Nine canon rows and
seventeen tracker rows are downstream of that one un-propagated close. The heaviest
single site is `loop-gap-electron-resonator-closure-doctrine.md`, which still instructs
a reader to *scope v11+ engine work* and to *advance ranks*, with no banner at all; the
heaviest single sentence is `the-abandoned-interior.md:66`, which still offers *"the lock
is the MOTION"* as the AVE answer-candidate to Poincaré's question five weeks after the
mechanism was falsified across five loci.

**Phase B has a clean 17-row Status-only backlog** (twelve `_orchestration` trackers,
five `research/` status lines) with no physics-body edits required. **Phase C has ten
canon rows across nine files**, of which two (`common/index.md`, the figure YAML) are
mirrors that will silently re-offer the corpse if only the prose leaves are bannered —
worth doing in the same pass as the exhaustive walk-back grep.

Three cautions carried forward. First, **the fence held but it is narrow on two pages**:
`the-abandoned-interior.md` and `physics-lineage-map.md:302` each carry the K1 corpse
*and* the held-out Poincaré amend in the same block, so Phase C must banner a clause,
not a page. Second, **"self-trap" and "genesis" are both homonyms across the fence** —
the \(\Gamma=-1\)/\(V_{\text{yield}}\) boundary self-trap is the *surviving* localizer and
cosmological lattice-genesis is the *held-out* amend, which is why the recall union is
1028 files and the precision universe is 382; a Phase C grep that does not carry that
distinction will banner surviving physics. Third, **four sites in §5 are genuinely
undecidable between Q1 and live-wrong** and are left unpicked for the orchestrator,
including the one (`electron-bound-resonator-coverage.md:103`) that Phase B already names
but that **no K-row can honestly claim**.

Filter check for this PR: (1) *did we stop a killed mechanism from being offered as
current?* — **not yet; this PR is the map, and it commits nothing to canon.** (2) *did we
add a sentence about what an electron is, or an honest negative?* — **an honest negative:
the K1 close never reached canon, and K2/K4/K6 need no work.** (3) *did we open a new
surface?* — **no.**
