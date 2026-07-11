# Engine-refresh satellite — handoff brief (2026-07-11)

**Kind:** Grant-launched satellite orchestration brief (self-contained). Grant
picks the model + effort and directs the session himself; the core session
chips in only on request. **Register:** mixed — six docs/housekeeping units
(mid-tier model at moderate effort suits these) + **one M-cost engine test**
(U5, the EP-CMRR acceptance test — the CMRR unit wants care; treat it as the
physics unit of the session).

**Provenance of the mission units:** the 2026-07-11 engine-state audit. **Every
file:line receipt below was re-verified (grep/Read) at write time** against
`origin/main` `4bc11298`; the two receipts that did NOT survive re-verification
are flagged in-unit and consolidated in the **Receipt ledger** at the foot of
this brief. Re-verify again at your own HEAD before editing (verify-before-cite;
stale line numbers drift by a few lines under intervening merges).

**Sector-declaration (mandatory, for the physics unit U5).** SECTOR = A1
dilatation / gravity (the longitudinal-bulk `V` scalar, `crystal_engine.py:18-20`);
does the engine carry the DOF? YES — the certified Master-Equation medium
(`master_equation_fdtd.py`) is the A1 bulk-trap. REGIME = sub-yield (linear,
`S(A)≈1`; NOT the near-yield saturated regime). DRIVE = uniform (common-mode)
vs tidal/gradient (differential). The kernel variable is **strain** `A=|V|/V_yield`
(`master_equation_fdtd.py:156-161`), not force magnitude — that distinction is
the whole content of U5.

---

## ★ MANDATORY TOOLING LINE (read before any adversarial review)

> For any adversarial review, invoke `.claude/workflows/ave-adversarial-pr-review.js`
> via a scriptPath WRAPPER that inlines args and calls workflow({scriptPath}, ARGS)
> — the Workflow tool's named-path args forwarding is broken (verified 4× on
> 2026-07-11); do not pass args to a named workflow directly.

---

## ★ LAUNCH-TIME INPUTS (four questions Grant answers when he launches)

The **C13b γ-confirmed pattern**: surface the stale-gate / already-decided
adjudications as explicit launch-time questions so the satellite freezes on a
confirmed answer rather than re-litigating (the model: `_orchestration/2026-07-10_rulings-docket.md`
Grant-input-round item 14 — the C13b prereg's α/β/γ gate was stale because Grant
had already adjudicated (γ) at `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dm-mechanism-unification.md:54`,
"rewritten 2026-05-17 per Grant adjudication (γ)"). The four here follow the same
shape — each gates a specific unit below.

1. **ch14 walk-back header — now, or after the low-duty-cycle reconciliation is
   adjudicated?** The `clm-c54kdd` leaky-cavity decay leaf models the muon as
   continuous above-yield RC-discharge (`Q~1`) vs the observed `Q_μ≈3.5×10¹⁷`
   (~17.5 OOM), flagged by X43 (`_orchestration/2026-07-10_rulings-docket.md`
   four-lane continuation §walk-back-queue item 1). A reconciliation is available
   (the breakdown is the rare terminal jump; its low duty cycle IS the nearly-
   closed high-`Q` port). Gates the **U7** ch14-header sub-item.
2. **Firewall-amendment ratification block backfill — verbal YES?** The block at
   `_orchestration/index.md:243-247` is blank (`Date: ___`) though downstream
   work (the crystal_engine / master_equation cage-test platform, the harness
   amendment) proceeded as-if-YES. Verbal YES to backfill the date, or leave
   blank pending a real sign-off? Gates the **U7** firewall sub-item.
3. **Band-survey (PR #609) — own epic doc, or ratify boards-as-record?** Does the
   band-survey get its own epic tracker, or is the existing board record
   (`_orchestration/2026-07-09_orchestration-board.md` / `2026-07-10_orchestration-board.md`)
   the sufficient home? Gates the **U7** band-survey sub-item.
4. **`axiom-register.md:229` z=3 identity filed under ASSERTED/OPEN — cosmetic
   re-scope or real migration sub-question?** D1 was RATIFIED (srs-z3 = production
   carrier, `_orchestration/index.md` §2026-07-03), yet the Axiom-1 row's
   ASSERTED/OPEN column (`manuscript/ave-kb/common/axiom-register.md:229`) still
   files "the D1 z=3-vs-z=4 production identity" as open. Is that a cosmetic
   re-scope (D1 settled the carrier → move it out of OPEN), or a real
   still-open migration sub-question (the continuum-limit / production-engine
   migration is genuinely unfinished)? Gates the **U7** axiom-register sub-item.

---

## MISSION UNITS

**One PR, one commit per unit.** DO-NOT-MERGE title; only Grant merges;
worktree self-isolation; incremental commits. Def-nodes minted: **NONE** (U6 is
a table row, not a def-node).

### U1 — index refresh block (S, highest leverage)

`_orchestration/index.md` is ~40 merged PRs stale — the newest section is the
**2026-07-09 Session board** (`index.md:8`, authoritative-for-current-state
header). Add a **dated 2026-07-10/11 block** at the top (above the 2026-07-09
section), carrying:

- the **vertex arc** (x33–x38: tethered-pivot + junction extraction; solvers
  `tethered_pivot_winding.py`, `tethered_pivot_x34b.py`, `core/junction_parasitics.py`
  = X37, `core/junction_scattering.py` = X38);
- **x40** (ring-closure transient / cut-cycle split), **x42** (eigencavity),
  **x43** (ringdown-port);
- the **collapse registry + batch** (`_orchestration/2026-07-11_collapse-batch-handoff.md`);
- the **astro sweep** (`_orchestration/2026-07-11_astro-adjudicator-sweep-handoff.md`);
- **C13b** (`_orchestration/2026-07-11_c13b-bullet-cluster-run-handoff.md`);
- the **#608–#648 merge ledger** (compile from `git log`/`gh` at your HEAD —
  this range is the audit's estimate, not a re-verified receipt; report the
  actual merged set);
- the **X36 / X38 / X41 PENDING-GRANT rows** (the install-tautology / bore-fork /
  radiative-scoping items still awaiting Grant);
- **pointers to the two boards** (`2026-07-09_orchestration-board.md`,
  `2026-07-10_orchestration-board.md`) **+ the rulings docket**
  (`2026-07-10_rulings-docket.md`, now with four 2026-07-11 continuations).

Then **re-stamp the index header** (the "newest section" / staleness notice at
`index.md:6-8`). This is append-of-a-new-top-section, not a rewrite of the
historical sections (KEEP-BOTH: older reconciliations stay verbatim as the
arc record).

### U2 — close the S-exponent honesty-lag (S)

The `c_shear` / refractive-index S-exponent flag is **FIXED IN CODE** but two KB
sites still list it OPEN. Re-verified receipts:

- **CODE is fixed.** `src/ave/core/master_equation_fdtd.py` carries the in-code
  correction note at **`:172-183`** (the `WAVE-TYPED INDEX` block: "Legacy
  magnitude was S^{1/4} (an exponent defect — half the physical power);
  corrected to ½ here", `:176-177`); `n_em_index()` now returns `S**0.5`
  (`:184-188`). Matches the Grant F1 ruling per
  `research/2026-07-07_electron-lock_design-note.md:316-319` ("the apparent
  √S-vs-S^{1/4} ambiguity was an already-corrected code defect … resolved by
  Grant's F1 ruling") and `src/ave/core/crystal_engine.py:431-432` ("The legacy
  magnitude was S^{1/4} (an exponent defect — half the physical power).
  Corrected to ½ here").
- **KB still says OPEN (both to be flipped to RESOLVED with the code cite):**
  - `manuscript/ave-kb/vol9/ch17-engine-requirements/index.md:31` (requirement 13,
    "The S-exponent must be single-sourced") still describes `master_equation_fdtd.py:169`
    as returning `n=S^{0.25}` and calls it "a physics-review item to adjudicate
    before any L3/L4 build" — **stale**: the current code returns `S**0.5` at
    `:184-188` and the correction note is at `:172-183` (the old `:165-169` line
    anchors have drifted). Update to RESOLVED, cite the current code + the F1
    ruling.
  - `manuscript/ave-kb/common/engine-capability-map.md:127` ("Exponent defect
    (flagged, physics-review item)") likewise still cites `refractive_index()`
    returning `S^0.25` at the stale `:169`. Update to RESOLVED.
- **PROMOTE the genuinely-surviving flag to its own line: `n_eff` symbol
  OVERLOADED (√S EM vs 1/√S gravitational).** This is the real open item and it
  is NOT the exponent defect — the code itself surfaces it and declines to
  silently reconcile it: `master_equation_fdtd.py:178-180` ("the KB symbol n_eff
  is OVERLOADED (√S EM at `vacuum-birefringence-e4.md:12` vs 1/√S gravitational
  at `substrate-perspective-electron.md:58`) — FLAGGED to the KB owner … not
  silently reconciled") and `crystal_engine.py:433-435` (same flag). When you
  flip the exponent rows to RESOLVED, split this out so the closed item and the
  live item are not conflated. (flag-don't-fix: surface the overload as its own
  KB-owner decision; do NOT pick a symbol for them.)

### U3 — re-scope the DAG header + the CLAUDE.md src line (S)

- **DAG header.** `_orchestration/2026-06-12_loop-gap-engine-dag.md:3` reads
  "**Status:** LIVE — canonical capability manifest for K4⊗Cosserat electron
  closure". Re-scope "canonical capability manifest" → "**loop-gap-platform
  manifest**; the whole-engine manifest = `manuscript/ave-kb/common/engine-capability-map.md`".
  Rationale: the DAG is the loop-gap harness capability graph (its Platform-rule
  table names only CoupledK4Cosserat/VacuumEngine3D + frozen srs), whereas the
  engine-capability-map is the N-engine whole-engine home. Two homes with the
  same "capability manifest" label is a drift generator; the re-scope disambiguates.
- **CLAUDE.md src/ave line.** `AVE-Core/CLAUDE.md:23` still reads
  `| src/ave/ | Engine code (K4Lattice3D, Cosserat field, solvers, observers,
  integrators) |` — **pre-facade vocabulary**. Replace with a line that names
  the current architecture: the **regime-organized platform tree**
  (`regime_1_linear` … `regime_4_rupture`, plus `core/`, `solvers/`,
  `topological/`, `gravity/`, `qed/`) **+ the dispatch facade** at
  `src/ave/facade/unified_engine.py` (the regime-dispatch unified engine over
  the certified cores — the SINGLE-GRID bet, Rule-14 anti-rebuild; docstring
  `src/ave/facade/__init__.py`). Cross-check the platform inventory against
  `manuscript/ave-kb/common/engine-capability-map.md` §2 (the canonical engine
  list) before finalizing the wording — the audit named it "three platforms +
  facade" but the map §2 is the authoritative inventory; use its names, don't
  invent a count.

### U4 — engine-capability-map refresh (M)

Add rows to `manuscript/ave-kb/common/engine-capability-map.md` for this week's
instruments, then re-confirm the map's status stamps. The map's own no-claim
header (`engine-capability-map.md:3-11`) requires every §2 cell be grounded
against a file:line / PR anchor — hold the new rows to that bar. Re-verified
instrument receipts:

- `src/ave/core/junction_scattering.py` — **X38** srs vertex S₁₁ extraction +
  canonical Op6 bore selection (route d); carries the anti-install boundary
  (G-A gate: consumes only geometry). Prereg `research/2026-07-10_x38-s11-bore-selection_prereg_FROZEN.md`.
- `src/ave/core/junction_parasitics.py` — **X37** srs vertex junction-parasitic
  extraction (the vertex equivalent circuit DERIVED from bond geometry, not
  installed); anti-install boundary. Prereg `research/2026-07-10_x37-junction-parasitics_prereg_FROZEN.md`.
- `src/ave/solvers/tethered_pivot_x34b.py` — **x34b** control-subtracted excess
  detector, frozen a-priori; a THIN driver over the merged x34 solver (Rule-14,
  no fork-copy). Prereg `research/2026-07-10_tethered-pivot-rerun_prereg.md`.
- `src/ave/topological/srs_dec.py` — the **x40 srs-girth witness** additions:
  the srs net is girth-10 / (10,3)-a; `enumerate_girth_faces()` (`:140`)
  enumerates the girth-10 rings as the 2-cells (`SRS_GIRTH`, `:127-157`). This
  is the witness behind R-B's `trapped = 1/girth` theorem (N=10 girth → 1/10).
- the **x42 eigencavity driver machinery** — ⚠ **could NOT be pinned to a
  `src/ave/` file at write time** (grep for `eigencavity`/`x42` in `src/ave/`
  returned only incidental hits). Locate the actual x42 driver from the #634/#639
  landings (the docket lists X42 = eigencavity, #634/#639) before writing its
  row; if it lives under `src/scripts/` or a research driver, cite that path.
  Do NOT invent a `src/ave/` cite.

**NO new engine-state leaf** (audit verdict: a third home — after the DAG and the
engine-capability-map — would be a drift generator; U3 is de-conflating the two
that exist, not adding a third).

### U5 — ★ the EP-CMRR acceptance test (M — THE PHYSICS UNIT; Grant GO 2026-07-11)

A differential-pair unit test in the Vol9-Ch17 acceptance style
(`src/tests/engine_acceptance/`, `sup-`-node discipline per ch17 INVARIANT-S9/S10),
on the **certified Master-Equation medium** (`src/ave/core/master_equation_fdtd.py`).

**Sector header (repeat at the top of the prereg):** SECTOR = A1 dilatation /
gravity; DOF carried = YES (bulk `V` scalar); REGIME = sub-yield (`S(A)≈1`);
DRIVE = uniform (common-mode) vs tidal/gradient (differential). Kernel variable
= strain `A=|V|/V_yield`, NOT force magnitude.

- **LEG-A (common-mode):** apply a **uniform body-force drive** to the lattice →
  assert **rigid acceleration only — ZERO strain, ZERO kernel loading** (`S=1`
  everywhere). A spatially-uniform body force on the translation-invariant
  medium produces rigid translation, no differential strain, so a strain-keyed
  kernel does not load: infinite CMRR by construction.
- **LEG-B (differential):** apply a **gradient / tidal drive** → **strain ∝ the
  gradient**, kernel loads per the strain (`S<1` where the tide is nonzero).
- **P11 sabotage arm:** plant a common-mode-sensitive coupling — deliberately
  **key the kernel on `|g|`** (force magnitude) instead of strain → **LEG-A must
  FIRE** (the sabotaged kernel loads under the uniform drive; the test detects it).
  This is the falsifiable teeth: a passing LEG-A on the certified medium AND a
  firing LEG-A on the sabotage arm together certify the instrument.

- **P10 honesty (binding framing — state verbatim in the prereg):** this test
  **CERTIFIES-AND-EXPOSES; it does NOT adjudicate T4.** Per the **X36
  install-tautology** (`research/2026-07-09_x36-node-bottleneck_result.md:54,89,215`:
  "the engine returns whatever node model is installed; it cannot adjudicate the
  fork by itself") the engine returns whatever keying is installed — the test's
  value is making the **installed keying's EP-status VISIBLE**, not deciding
  which keying is physical. Concretely: the banked **galactic `η_eff(g_N)`**
  MOND keying (T4, `_orchestration/2026-07-10_rulings-docket.md` four-lane
  continuation §A T4 row; the surviving branches are acceleration-keyed after
  the tide sub-branch's X43-A0 dimensional kill), installed as **local-|g|
  keying, will FAIL LEG-A BY DESIGN of MOND phenomenology** (a₀ is a
  local-acceleration scale; a uniform body-force drive produces uniform |g|, so
  a |g|-keyed kernel loads under common-mode). **That failure is the honest
  exposure, not a bug — state it in the prereg** so the LEG-A "fail" on a
  MOND-keyed medium reads as the designed visibility of a WEP-violating keying,
  not as a defect of the test. The test cleanly separates a strain-keyed medium
  (WEP-exact, LEG-A passes) from a |g|-keyed medium (WEP-violating, LEG-A fires)
  — that IS its whole content.

- **Freeze discipline:** prereg + freeze-by-push (push the frozen prereg BEFORE
  the driver exists; claim the freeze by commit ordering, the `tethered_pivot_x34b.py`
  pattern) + the sector header above. Consistency/certification class — no chord
  mint (per P10 this cannot adjudicate T4).

### U6 — ★ the CMRR register row (S; Grant GO 2026-07-11)

Add ONE row to `manuscript/ave-kb/common/translation-tables/translation-circuit.md`
**§4** (the "Comprehensive substrate-primitive ↔ EE-component mapping" META
catalog, header at `:91`; the `clm-eemap1` home) per the **ave-ee-first-mapping
Step-6 landing discipline** (`~/.claude/skills/ave-ee-first-mapping/SKILL.md:186-199`:
land the row in the canonical leaf §4, regime-tag it, add the originating-leaf
cross-ref):

- **EQUIVALENCE PRINCIPLE ↔ coupling-level common-mode rejection.** CMRR
  **infinite BY IDENTITY** — gravitational charge ≡ inertial mass, nothing to
  mismatch; the **tide = the differential mode**. Spec anchors: Eötvös /
  MICROSCOPE = **WEP-CMRR ~1e-15**; LLR-Nordtvedt = **SEP-CMRR ~1e-4**.
- **DISTINGUISH from the ε-sector gauge rider = READOUT-level CMRR** (a DIFFERENT
  mechanism, same instrument word): a common-mode / uniform-bias E **LOADS the
  Q-point but reflects nothing** (`∇A=0`) — cross-ref the rider site
  `manuscript/ave-kb/vol4/claim-quality.md:1856` ("The uniform-bias gauge rider
  does NOT rescue the muon (`∇A≠0`)"). Coupling-level (EP) vs readout-level
  (gauge rider) is the axis to make explicit in the row.
- **KEEP-BOTH (do NOT edit the existing CMRR row).** `translation-circuit.md`
  already carries a CMRR entry at **`:512`** — but in the **§9 op-amp
  non-ideality catalog** (CMRR as an op-amp datasheet spec ↔ SYM-class
  substrate-invariance, `clm-3zz0f6`). That is a distinct context (op-amp spec)
  from the new EP↔CMRR coupling-level row in §4. Leave `:512` verbatim; add the
  new row in §4.
- **Mirror.** Step-6 requires mirroring the row into the skill's Step-2 table
  (`SKILL.md`, "the skill body mirrors the leaf; the leaf is authoritative",
  `:190-191`). ⚠ The skill is a **user-level, Grant-gated file** outside the repo
  (per the harness Posture-B / AVE-Skills-Grant-gated standing). **Land the leaf
  row in this PR; flag the skill-mirror as a Grant-gated follow-on — do NOT edit
  `~/.claude/skills/` from the satellite session.**
- Mark **consistency / register class; no claim mint beyond the row.**

### U7 — housekeeping batch (S)

- **`constants.py` trailing comment.** `src/ave/core/constants.py:281` reads
  `DELTA_STRAIN: float = 1.0 - (1.0 / ALPHA) / ALPHA_COLD_INV  # ≈ 2.225e-6`.
  Align the trailing `≈ 2.225e-6` with the **:179 digit-carrier**
  (`δ_strain ≈ 2.2234 × 10⁻⁶ [CODATA-2018 α pin; 2.2228 × 10⁻⁶ vs CODATA-2022]`)
  — the trailing comment rounds to 2.225e-6 where the digit-carrier says 2.2234e-6;
  bring the comment to `≈ 2.2234e-6` (or the precision-house-rule form the :179
  carrier uses). (The day-3 close already caught the `:279→:281` drift; re-confirm
  the line at your HEAD.)
- **vol_6 undefined cross-ref — ⚠ RECEIPT DID NOT VERIFY; BUILD-FIRST.** The
  audit named `fig:mass_error_vs_Z` as "one missing \label". **It is NOT missing:**
  `manuscript/vol_6_periodic_table/chapters/A_heavy_element_catalog.tex:26` has
  `\label{fig:mass_error_vs_Z}`, the `\ref` is at `:20`, and the chapter is
  `\input` at `main.tex:80`. A full sweep of vol_6 refs found **every in-volume
  `\label` resolves** (`box:internal_peer_scope`, `eq:semiconductor_mass`,
  `sec:high_z_frontier`, `sub:R_coupled_cavity`, `ch:fluorine`, `sec:two_models`,
  `sec:semiconductor_nuclear`, `ch:intro` all present). Do NOT "fix" a phantom.
  **Run `make vol6` (or the vol_6 latexmk build) FIRST**; only if it reports a
  genuinely-undefined ref, fix that one (candidate: the cross-volume
  `ch:alpha_golden_torus`, whose resolution rides `main.tex:12`'s namespace
  import). If the build is clean, this sub-item is **DROPPED** (honest closure —
  no manufactured fix).
- **Full-path the `cvr_model.py` cites in the ch17 flags.** ch17 requirement 17
  (`ch17-engine-requirements/index.md:40`) cites `cvr_model.py:72` and `:364`
  by bare name; the file is `src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py`.
  Replace bare `cvr_model.py` with the full path.
- **`axiom-register.md:229` handling — per launch-time answer (4).** Either a
  cosmetic re-scope (move the D1 z=3-vs-z=4 identity out of the ASSERTED/OPEN
  column, since D1 is ratified) or leave-and-re-word as a genuine open
  migration sub-question. Do the version Grant picks; do NOT decide it yourself.
- **ch14 walk-back header — per launch-time answer (1).**
- **firewall blank (`index.md:243-247`) — per launch-time answer (2).**
- **band-survey (PR #609) — per launch-time answer (3).**

---

## DELIVERABLES / DISCIPLINE

- **One PR** (DO-NOT-MERGE title), **one commit per unit** (U1…U7).
- **Def-nodes minted: NONE** — U6 is a table row, not a def-node.
- **Adversarial review before CLEARED** — receipt-fidelity lens (every flipped
  status + new row grounded against a re-verified file:line) **+ the U5
  test-honesty lens** (does the prereg state the P10 CERTIFIES-AND-EXPOSES
  framing? does it name the MOND-keyed LEG-A "fail" as designed visibility, not
  a defect?). Invoke via the **WRAPPER pattern** (see the mandatory tooling line
  above) — inline the args into a scriptPath wrapper; the named-path forwarding
  is broken.
- **Only Grant merges.** Worktree self-isolation; incremental commits.
- **KEEP-BOTH** everywhere a legacy row/label exists (U1 index sections, U6
  `:512` op-amp CMRR row).
- **verify-before-cite** at your own HEAD before each edit (line numbers drift).

---

## Receipt ledger — re-verification at write time (`origin/main` 4bc11298)

**Verified (safe to write as-is, re-confirm line at HEAD):**

| Unit | Receipt | State |
|---|---|---|
| U1 | `index.md:8` newest section = 2026-07-09; `index.md:243-247` firewall block blank | ✓ |
| U2 | `master_equation_fdtd.py:172-183` correction note, `:184-188` returns `S**0.5`; `design-note:316-319` F1 ruling; `crystal_engine.py:431-432` "corrected to ½"; `ch17…/index.md:31` + `engine-capability-map.md:127` still OPEN (stale `:169`); n_eff overload at `fdtd:178-180` + `crystal_engine:433-435` | ✓ |
| U3 | `loop-gap-engine-dag.md:3` "canonical capability manifest"; `CLAUDE.md:23` stale src line; facade `src/ave/facade/unified_engine.py` | ✓ |
| U4 | `junction_scattering.py` (X38), `junction_parasitics.py` (X37), `tethered_pivot_x34b.py` (x34b), `srs_dec.py:140` girth-10 witness | ✓ |
| U5 | X36 install-tautology `x36-node-bottleneck_result.md:54,89,215`; T4 keying `2026-07-10_rulings-docket.md` §A | ✓ |
| U6 | `translation-circuit.md:91` §4, `:512` existing op-amp CMRR (KEEP-BOTH); gauge rider `vol4/claim-quality.md:1856`; Step-6 `SKILL.md:186-199` | ✓ |
| U7 | `constants.py:281` `# ≈ 2.225e-6` vs `:179` `2.2234×10⁻⁶`; `axiom-register.md:229` z=3 under ASSERTED/OPEN; `cvr_model.py` full path | ✓ |

**Failed / partial re-verification (do NOT write as-stated):**

- **U7 `fig:mass_error_vs_Z` "missing \label" — FAILED.** Label present at
  `A_heavy_element_catalog.tex:26`; all vol_6 in-volume labels resolve. Re-scoped
  to BUILD-FIRST; drop if the build is clean.
- **U4 x42 eigencavity driver — PARTIAL.** No `src/ave/` file pinned; locate from
  the #634/#639 landings before writing the row.

---

*Cross-refs (all backtick pointer-cites, verify-before-cite'd this session):
`_orchestration/index.md`, `_orchestration/2026-07-10_rulings-docket.md`,
`_orchestration/2026-06-12_loop-gap-engine-dag.md`, the two boards
(`2026-07-09_orchestration-board.md` / `2026-07-10_orchestration-board.md`), the
four 2026-07-11 satellite handoffs (astro sweep / collapse batch / c13b / x43).
This brief records queue-state + re-verified receipts, not adjudicated physics;
nothing here canonizes.*
