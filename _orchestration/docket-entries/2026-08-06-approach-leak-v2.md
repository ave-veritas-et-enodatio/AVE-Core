# Docket fragment — the approach-leak v2 rerun (2026-08-06, EXECUTION RECORD)

**Key:** `approach-leak-v2` · **Branch:** `research/approach-leak-v2` · **Base:** `research/approach-leak` = `5e2694c0` (PR #903, `[REVIEW: CLEARED]`, **UNMERGED**) · **Written against `origin/main` = `c4fdced0`**
**Dispatch:** re-anchor exactly ONE mis-sized negative-control tolerance and adjudicate the bins v1's global consequence clause suppressed.
**Predecessor:** [`research/2026-08-05_approach-leak_result.md`](../../research/2026-08-05_approach-leak_result.md) §1.3 (the `G-NC-SLAST` diagnosis) and §7 (`FLAG-FREEZE`, which routed this lane).
**Artifacts:** [`research/2026-08-06_approach-leak-v2_prereg-FROZEN.md`](../../research/2026-08-06_approach-leak-v2_prereg-FROZEN.md) (`ebd1f4c7`, pushed with **no code**) · [`research/2026-08-06_approach-leak-v2_result.md`](../../research/2026-08-06_approach-leak-v2_result.md) · `research/drivers/approach_leak_v2.py` (`4d9e5176`, committed before any v2 JSON existed) · `research/drivers/approach_leak_v2_results.json` (`9c9e2185`) · `research/drivers/approach_leak_v2_number_check.py` (gating via `make verify`).
**SVA pilot case 9** (v0.2 header, eleven rows; per-row notes at result §7).

---

## Outcome, one screen

**`LEAK-CERTIFIED-V2`. THE BINS ARE ADJUDICATED.** All seven v2 gates PASS, `FT-SLAST` fires on both
parts, and the **entire v1 record reproduces with `0` mismatches over `1431` leaves** at exact string
equality, recomputed digest `2af8acfe23aabb96` identical to v1's.

**The re-anchor, and why it is a repair and not a retune.** A reproduction gate's tolerance is
bounded by the precision **the SOURCE SHIPPED at**, not the precision the consumer computes in. v1
froze `1e-40` against a comparand rendered at `30` significant digits, seeded from a rung carrying
`17` — `10` orders below one floor and `23` below the other, **unsatisfiable by any correct
instrument**, i.e. **ARTIFACT-class**. Both v2 tolerances derive from **digit counts of the shipped
strings and nothing else** and were frozen before the run:

| leg | comparison | bound (derivation) | frozen tol | measured |
|---|---|---|---|---|
| **A** seed-exact | `S_last` recomputed from the SHIPPED seed through the identical cancellation-free form | `5e-30` = ½ unit in the 30th sig digit of `mp.nstr(·,30)` | `1e-27` (200× headroom) | `7.74183e-31` |
| **B(x)** seed-bounded | this lane's `ℓ_node/r_sat` at `62 M_⊙` vs the shipped seed | `5e-16` = ½ unit in the 17th sig digit × a declared `10`× safety factor | `5e-16` | `4.08817e-17` |
| **B(S)** seed-bounded | this lane's `S_1` vs the shipped `S_last` | `2.5e-16` (× `∂lnS/∂lnx = ½`) | `5e-16` | `2.04408e-17` |

- **The error model confirmed itself**: LEG-A landed *below* its own `5e-30` rendering bound, and the
  30-digit rendering is **string-identical** to the shipped `S_last` (non-gated diagnostic — the gate
  rides the derived tolerance, never a tie).
- **v1's own numbers are unchanged**: `4.08817e-17` / `2.04408e-17` are v1's, to the digit. Both also
  sit below the *bare* `5e-17` rendering bound, so the safety factor was insurance, not a crutch.
- **The gate can fail.** COARSE (seed × `1+1e-12`) ⇒ LEG-A `5.00000e-13` and LEG-B(x) `9.99959e-13`,
  both FAIL. FINE (comparand × `1+1e-26`) ⇒ LEG-A `1.00008e-26` FAILS while LEG-B still passes —
  which is what proves the `1e-27` leg is **non-vacuous at its own scale**.

## The adjudication (v1's frozen §7 bin definitions, VERBATIM — no boundary moved)

| `p` | provenance | `N_open` | **BIN** |
|---|---|---|---|
| `0.5` | the DISPATCH's stated expectation | `[0]` | **`GAP-CLOSED`** |
| `1.0` | the ENGINE's coded `a = 2` | `[0]` | **`GAP-CLOSED`** |
| `1.5` | filler | `[0]` | **`GAP-CLOSED`** |
| `2.0` | ANALOGY, not canon | `[0, 1]` | **`CHANNEL-OPENS`** *(SPLIT overlay: `[0]` at `θ=1`, `[0,1]` at `θ=0.5`)* |
| `2.5` | ANALOGY, not canon | `485`…`3228` | **`CHANNEL-OPENS`** |
| `3.0` | ANALOGY, not canon | `84316`…`881448` | **`CHANNEL-OPENS`** |

**The bracket does not agree, so no single headline bin is reported.** Per the frozen bin-arithmetic,
both are reported with members named:

> **`GAP-CLOSED` on `{0.5, 1.0, 1.5}` — which includes EVERY member canon or the engine actually
> states — CO-FIRING with `UNDERDETERMINED-CANON`; `CHANNEL-OPENS` on `{2.0, 2.5, 3.0}`, every one of
> which requires the unwritten `I_ω(A)` law. `SCALE-UNDERDETERMINED` co-fires on the residual
> back-action prefactor `2(G_c/G)` and on that field alone.**

**The asymmetry is the content:** the closed arm is populated by members the corpus *states*; the
open arm entirely by members needing a grading law absent from `4418` tracked files. `P3` and `P4`
return `0` hits on **both** engines — **re-verified on this branch, not inherited.**

**`p = 2.0` discipline note.** This lane's prereg §6.1(1) says a splitting member is "reported as
SPLIT"; v1's frozen §7 says `CHANNEL-OPENS` = `N_open ≥ 1` at *any* row. **The frozen boundary
governs**; SPLIT is recorded as an annotation beside it. A reporting instruction in a successor's
prereg does not move the predecessor's bin boundary.

## Negative controls — the zero-mismatch statement

`1431` JSON leaves at exact string equality · `9` passing gate verdicts · `1` failing gate verdict
(v1's `G-NC-SLAST` at v1's own `1e-40` siting, `2.04408e-17`, reproduced byte-exact — the strongest
available proof that only the ANCHOR moved and not the instrument) · `2` null verdicts · `6` firing
self-tests · `4418` scanned files · `5` two-engine pattern agreements · `10` artifact blob hashes at
`5e2694c0`. **Total mismatches: `0`.**

**Declared, not discovered:** this is a **reproduction**, NOT an independent re-derivation. The v2
driver *imports the v1 module and calls the v1 module's own `main()`*. The `p`-bracket physics
carries **v1's** provenance; nothing here is a second confirmation of it.

## Flags

**Carried by POINTER, not restated, not repaired:** `FLAG-EXP`, `FLAG-IOMEGA`, `FLAG-MECH`,
`FLAG-ROTTOP` — bodies at `2026-08-05_approach-leak_result.md` §7, byte-untouched and gated.

**`FLAG-FREEZE` DISCHARGED** — both halves of its named repair executed inside this lane's freeze
(second-method check extended to the negative-control tolerances; gate at the source's shipped
precision). The v1 body stays byte-untouched (Rule 12). **The routed SVA row-9 amendment is still
routed and still NOT drafted — the auditor lands SVA amendments.**

**THREE NEW FLAGS, ALL SURFACED, NONE REPAIRED IN THE PREDECESSOR:**

1. **`FLAG-RUNGPROV`** — v1's §1.3 calls the last-bond rung *"the float64 literal … (a
   17-significant-figure `repr`)"*. **Not supported by any shipped artifact**: the string is not the
   shortest round-tripping `repr` of any double (Python's is `6.023898309025099e-19`, `16` digits),
   and nothing records how it was produced. **v1 is right in KIND, unsupported in specifics.** This
   is why LEG-B carries a declared safety factor. ROUTED.
2. **`FLAG-SCANFRAG`** ★ **— orchestrator-actionable, and it BLOCKS extension of the v1 branch.**
   v1's `verify-approach-leak-number-check` machine-gates `G-DET` by re-running the v1 driver, whose
   digest is a function of **how many tracked files exist under `manuscript/ research/ src/`**.
   Measured with only the v2 prereg added: digest `2af8acfe23aabb96` → `973458b3a1648c2a`,
   `n_files_scanned` `4418` → `4419`, `scan.P5` `5` → `6` on both methods. **`make verify` goes RED
   on ANY commit adding a single tracked file in that tree — this lane's, a concurrent lane's, or
   main's after merge.** Named structural repair, **NOT executed**: pin the scan surface to a
   **commit** (`git ls-tree -r <ship-commit>`), not to the worktree. It belongs in the v1 driver,
   which this lane may not edit.
3. **`FLAG-FENCEBLIND`** — the v1 checker pairs back-ticks over the whole document; a triple-backtick
   fence shifts the pairing and moves numerals into the unchecked gaps. On this lane's own doc,
   pre-repair, the entire §4 adjudication table escaped. Repaired **in this lane's own checker only**
   (registered values `59` → `73`). Non-gated diagnostic on v1's doc: exactly **one** numeral escaped
   its gate — `520`, a bookkeeping count, not a physics number. **NOT repaired there** (predecessor
   artifact) and **NOT gated against v1's doc** — gating it would add a gate to a predecessor's
   certification set, which this lane's freeze forbids.

## The forced build-wiring change, disclosed

`verify-approach-leak-number-check` is **RETAINED verbatim as a target** and replaced in the
`verify:` prerequisite list by **`verify-approach-leak-v2-number-check`, a STRICT SUPERSET**: it runs
v1's doc-numeral registry, v1's gate reconciliations, v1's three-mutation receipt and v1's `G-DET`
(in-process under the prereg §3.2 wrapper, where it can still be true), plus the v2 checks and the
v2 five-mutation receipt. **No check dropped, no tolerance moved, v1's number-check module
byte-untouched.** The freeze commit itself trips `FLAG-SCANFRAG`, so it carried **one** wiring line
and **no code**; the very next commit restored the gate as the superset.

**Union-conflict class, DISCLOSED and unchanged:** the `.PHONY` line, the `verify:` prerequisite line
and the `help` block are shared with every other lane's number-check target; the correct resolution
is the **UNION**, never a pick-one. The standing umbrella-glob proposal **REMAINS PENDING** and is
not adopted unilaterally.

## Propagation consequence — RECORDED, NOT EXECUTED

The channel-scoped kernel-collapse ruling's leak clause
([`2026-08-05-ruling-kernel-collapse-rescope.md`](2026-08-05-ruling-kernel-collapse-rescope.md):16-18)
**resolves to the bounded evanescent form with the knife-edge caveat** — the resolved wording is
drafted at result §5 for the **gated propagation pass**. **This lane edits no KB leaf, no manuscript
file, no ruling docket entry, no solidity, no matrix row and no falsification ledger.** The auditor
lands corpus-state entries. **Single hinge, named not buried:** if an `I_ω(A)` law is ever ruled at
`b = 3` while the engine's `a = 2` stands, `p = 2.5` and the resolution inverts.

## What this lane does NOT license

- **Any claim that the v1 physics was independently re-derived.** It was **reproduced**.
- Nothing about the rotational channel AT or INSIDE `r_sat`; **MeV-scale rotational radiation is out
  of scope**, one cross-reference line only.
- No adjudication of the cross-grade aggregation fork, FORK-3(b), the `β` bracket, the `K(A)` fork,
  `FLAG-CAUSAL`, or any predecessor's other bins.
- No promotion of the engine's coded `a = 2` to canon; no invention of an `I_ω(A)` law. The RHO-B
  `1/S³` grading on the micro-inertia is an **ANALOGY, labelled as one at every site**.
- No AVE-vs-competitor discriminator: the ECO free-reflectivity degeneracy applies unchanged.
- **`research/` + this docket fragment + the Makefile only.** No KB, no manuscript, no `src/ave`.
  Engine byte-untouched and never imported. **All ten read-only predecessor artifacts byte-identical
  to their blobs at `5e2694c0`, and that is GATED (`NC-BYTES`).**
- Mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`; moves no solidity; edits no falsification ledger; no
  SVA amendment drafted.
