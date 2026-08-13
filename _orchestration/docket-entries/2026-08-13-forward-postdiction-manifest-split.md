### ENTRY 2026-08-13-forward-postdiction-manifest-split

**Grant, verbatim `[sic]`:** *"the predictions yaml should be forward only, we should make a postdiction yaml, and make sure all tooling/gates are consistent and planned out well."*

**What landed.** `manuscript/predictions.yaml` is now FORWARD-ONLY (2 entries); the 35 postdiction
entries moved wholesale and unedited to the new `manuscript/consistency-manifest.yaml`. One public table,
two backing files: the validator's parity checks read the UNION, so all 47 table rows still resolve.

**Why the split was mostly already made.** `README.md:41` had ruled it in prose — of 47 slots,
*"leaving **45 consistency-class entries**; the **1 armed forward falsifier** (the birefringence
Letter) lives on the falsification surface, **outside** the 47"* — with the badges encoding it. The
file structure now matches the sentence the README already shipped.

**What it deliberately did NOT do.**
- It does **not** key on `calibration_role`. Grant ruled 2026-08-05 that that axis is
  value-provenance and *"orthogonal to `type`"*. Membership is by FILE.
- It does **not** re-type the four rows whose `type` says `derived_prediction` while they mean
  `consistency_check`. That was routed *"across four rows, not a rider on this one"* and stays
  routed → `open-items/manifest-type-retyping`.

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

**Cite repointing.** Shrinking `predictions.yaml` 1110 → 138 lines killed 5 line-pinned citations
into it. All repointed by ENTRY ID rather than line. Recorded honestly: three of them had **already
drifted before the move** — the prose named P23 while `:126-142` resolved to P05/P06 — so the
vacated-cite rule applied and they were re-derived fresh, not re-adjudicated. Two more line pins
into the validator were repointed to a symbol name.

**Receipts.** `make verify` EXIT=0 · `make test` 2966 passed / 3 skipped / 9 xfailed · both
manifests validate independently with 0 criticals · `verify-md-links` EXIT=0 with **zero new
errors** vs clean `origin/main` (verified by full-report diff, not the truncated console output) ·
README badge md5 unchanged · board `--check` green.

**Routed, not closed:** `open-items/manifest-type-retyping` (the four rows) and
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
