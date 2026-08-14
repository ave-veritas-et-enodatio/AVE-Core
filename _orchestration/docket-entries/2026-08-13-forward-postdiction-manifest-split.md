### ENTRY 2026-08-13-forward-postdiction-manifest-split

**Grant, verbatim `[sic]`:** *"the predictions yaml should be forward only, we should make a postdiction yaml, and make sure all tooling/gates are consistent and planned out well."*

**What landed.** `manuscript/predictions.yaml` is now FORWARD-ONLY (2 entries); the 35 postdiction
entries moved to the new `manuscript/consistency-manifest.yaml`. One public table,
two backing files: the validator's parity checks read the UNION, so all 47 table rows still resolve.

> ★ **CORRECTION 2026-08-13.** An earlier version of the sentence above said the 35 entries moved
> "wholesale and unedited". **That was false and is withdrawn.** Six rows were edited in the move:
> `P47`, `P19`, `P20_21`, `P42`, `P44_45` (each `type` and/or `calibration_role` plus notes) and
> `P04` (notes). Field-level base→tip diff, not an eyeball. The withdrawal originally landed only in
> the manifest header, leaving this entry — the durable timeline record — still asserting the
> receipt. Recorded here because a receipt that is corrected somewhere else is still wrong where a
> reader will find it.

**Why the split was mostly already made.** `README.md:41` had ruled it in prose — of 47 slots,
*"leaving **45 consistency-class entries**; the **1 armed forward falsifier** (the birefringence
Letter) lives on the falsification surface, **outside** the 47"* — with the badges encoding it. The
file structure now matches the sentence the README already shipped.

**What it deliberately did NOT do.**
- It does **not** key on `calibration_role`. Grant ruled 2026-08-05 that that axis is
  value-provenance and *"orthogonal to `type`"*. Membership is by FILE.
- It did **not** re-type those four rows *as first written*. ⚠ **SUPERSEDED LATER IN THIS SAME
  PR**: Grant ruled *"fold into 966"* and all four flipped to `consistency_check`. Preserved for
  the sequence, not as current state — see the rulings block below.

**Accounting (RATIFIED rule preserved).** 36 → 35 postdiction + 1 moved (`P_A034_solar_flare`,
never one of the 47 slots) + 1 NEW (`P_biref_coefficient`) = 37. The 33 numbered entries that
expand to 1–47 all moved together, so the 47↔36 disposition table still resolves against one file.
README badge line verified byte-identical (md5 unchanged).

**★ The new row.** `P_biref_coefficient` bridges `clm-pp3qwf` — the armed birefringence falsifier,
carried in README prose since before this split but never machine-tracked. Landed as
`calibration_role: mixed`, **not `chord`**: its own card carves CHORD = tree-level saturation
exists / ECHO = the α-rooted magnitude, which is `def-fmv001`'s shape exactly. Declaring `chord`
would re-open the axis Grant closed 2026-08-05.

**★ GATE DEFECT FOUND AND FIXED — the reconciler was blind to the word "echo".** Of 20 provenance
markers, none matched it, so `clm-pp3qwf` scanned to ZERO markers and reported UNRECONCILED —
meaning a `chord` declaration on the framework's one AVE-distinct forward claim would have PASSED
the critical gate. Its card says the opposite verbatim: *"the MAGNITUDE $1.93\times10^7=7.5/\alpha^3$
is an $\alpha$-echo at the value level."* It would have passed because the regex missed, not because
the corpus agreed. New `VALUE_ECHOED` marker added (forbids `chord`), snapshot updated, scope
measured before landing: fires on 2 live cards, full census across BOTH manifests gives
**CONTRADICTED = 0**, so the gate goes green on merge rather than red.

**★ P19 relabelled — PENDING-GRANT-CONFIRM, not a new ruling.** It was the LAST row carrying
`calibration_role: forward-prediction`, the exact label struck off P42 on 2026-08-05 as *"wrong on
all three axes"*, while carrying `error_percent: 1.6` and notes reading *"NEAR-shape prediction
**validated**"*. Applied on the P42 precedent; `type` untouched; one word from Grant reverts it.

**Tooling brought into step.** `predictions_manifest_refresh.py` now drives BOTH manifests (it
writes back, so a missed path would have silently stopped regenerating `axioms_used` — drift the
`axioms` check then gates on at critical). `Makefile` runs the validator twice. Both manifest
headers corrected: they named `claim_graph_validator.py` (renamed away) and claimed 4 checks (8).

**Cite repointing.** Shrinking `predictions.yaml` 1110 → 148 lines killed 5 line-pinned citations
into it. All repointed by ENTRY ID rather than line. Recorded honestly: three of them had **already
drifted before the move** — the prose named P23 while `:126-142` resolved to P05/P06 — so the
vacated-cite rule applied and they were re-derived fresh, not re-adjudicated. Two more line pins
into the validator were repointed to a symbol name.

**Receipts.** `make verify` EXIT=0 · `make test` 2966 passed / 3 skipped / 9 xfailed · both
manifests validate independently with 0 criticals · `verify-md-links` EXIT=0 with **zero new
errors** vs clean `origin/main` (verified by full-report diff, not the truncated console output) ·
README badge md5 unchanged · board `--check` green.

**Routed, not closed:** the P19 note in `consistency-manifest.yaml` (the routed item was RULED and EXECUTED the same day, so no tracker was ever created — see the rulings block below) (the four rows) and
`open-items/postdiction-vocabulary` (the term now sits in a tracked filename with no `def-` node,
while `chord`/`echo`/`mixed` each have one plus an ambiguity flag).

**★ RULING 2026-08-13 (Grant, verbatim `[sic]`): *"i like consistency manifest"*.** The postdiction
manifest is named **`manuscript/consistency-manifest.yaml`**, matching the README's own *"45
consistency-class entries"*. This DISCHARGES the vocabulary question the split raised: "postdiction"
is used in ~15 Rule-12 walk-backs but has never been minted as a `def-` node, while its siblings
`chord`/`echo`/`mixed` each have one plus an `open-ambiguity-flag`. Naming the file for what it
GATES rather than for an unminted term avoids minting vocabulary by filename. The
`open-items/postdiction-vocabulary` fragment is deleted accordingly (closing an item deletes its
file; git holds the history, this entry holds the ruling).

**★ RULINGS 2026-08-13 (Grant), folded into this PR.**
- **"1. confirmed"** — P19's `calibration_role: forward-prediction → consistency` is RATIFIED. The
  PENDING-GRANT-CONFIRM stamp is lifted; the row now reads CONFIRMED.
- **"3. fold into 966"** — the `type` re-typing owed *"across four rows, not a rider on this one"*
  is DISCHARGED. P42, P47, P20_21, P44_45 all flip `type: derived_prediction → consistency_check`
  in one pass, on the basis the P42 ruling itself stated: the schema defines `derived_prediction`
  as *"genuine forward prediction (Class D)"* while `consistency_check` (*"reproduces a known
  result (Class C)"*) *"is the closer fit"*. All four already carried `calibration_role:
  consistency`, so field and type now agree. Mechanism-class relabel only — no value, axiom,
  bridge or solidity moved. the routed item was RULED and EXECUTED the same day, so no tracker was ever created.
- **"2. lets add the 7th in a new PR"** — a SEVENTH `calibration_role` is authorized, in its own PR,
  for the class this split exposed: **form forced by the substrate + value computed from a declared
  calibration input measured in a DIFFERENT experiment + output never fit to the observable being
  predicted**. That is a genuine forward value and the current vocabulary has no slot for it —
  `echo`/`mixed` collapse it together with the definitional case. The discriminator is *"was the
  observable being predicted used to set any input?"*, not *"does α appear?"*. Symmetric-standard
  note: every SM prediction consumes measured inputs (α, G_F, m_Z) and is called predictive;
  applying `echo` to ourselves for the same structure is the consensus-bias trap.
  ⚠ Scoped explicitly: **this row (`P_biref_coefficient`) does NOT qualify** and stays `mixed`.
  `E_YIELD ≡ √α·E_CRIT` by definition (`constants.py`, the `E_YIELD` definition), so `(E_CRIT/E_YIELD)² = 1/α` holds to
  **0.00e+00 relative error** — the α-power in its magnitude ratio is algebra, not prediction. The
  chord is the FORM (tree-level saturation vs QED's α² loop), which is what HIBEF would test.

**★ CORRECTIONS 2026-08-13, from the cold read of this PR (findings F6–F9, F11).** Recorded rather
than silently amended:
- **F6 — five self-referential line pins broke inside the manifest this PR created**, including the
  two the re-typing decision cites as its basis (*"line 29"*, *"line 35"*). All repointed to the
  **content** they name (`calibration_role` / `type` schema comments) rather than to new line
  numbers, which would drift again. Two validator pins repointed to function names.
- **F7 — the birefringence row recorded a SUPERSEDED magnitude.** It quoted v1
  (`7.5/α³ ≈ 1.93×10⁷`) as *"the card states it verbatim"*; that sentence is real but sits inside the
  card's **preserved historical note**, and the live headline is **v3 = `3.75π/α² ≈ 2.2×10⁵`** (the
  2026-07-07 OPTION-B footing consolidation). Corrected to v3 with the full convention history.
  Quoting preserved history as current is the vacated-cite pattern.
- **F8 — `make test` manifest coverage silently fell 36 → 2.** Ten live-manifest tests loaded
  `MANIFEST_PATH` alone, which the split left holding 2 entries. A 94% coverage drop with every test
  still green — the degrades-to-a-pass shape those tests exist to catch. They now load the union
  (37 entries, asserted by a receipt, not by eye).
- **F9 — P19 was left the sole `type`/`role` mismatch in the union**, routing to a tracker that was
  never created. `type` flipped to `consistency_check`, initially stamped PENDING-GRANT-CONFIRM and since **CONFIRMED** by Grant (*"lets label it correctly"*): this is
  a FIFTH row and Grant's *"fold into 966"* named four. Flagged, not folded in silently.
- **F11 — the `constants.py:499` receipt named the wrong symbol.** The physics is right
  (`(E_CRIT/E_YIELD)² · α = 1.0` exactly), but `:499` is `E_YIELD_KINETIC` (Joules); `E_YIELD` (V/m)
  is elsewhere in that file. Now cited by symbol, not line.

**★ RULING 2026-08-13 (Grant, verbatim `[sic]`): *"lets label it correctly but add it to our
followups/backlog to readjudicate"*.** P19's `type: derived_prediction → consistency_check` is
CONFIRMED — a fifth row beyond the four named in *"fold into 966"*, ruled explicitly because it was
outside that set only by minutes. The CLAIM is separately routed to
`open-items/p19-flyby-readjudication`: correct labelling of a weak row is not an endorsement of it.
