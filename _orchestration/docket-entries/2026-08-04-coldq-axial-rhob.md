# Docket — cold-Q AXIAL family under RHO-B (FORK-3(b), certified axial class)

**Date:** 2026-08-04
**Lane:** `research/coldq-axial-rhob` · PR `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`
**Prereg:** `research/2026-08-04_coldq-axial-rhob_prereg-FROZEN.md` @ `e3a4181d` (COMMIT 1, pushed **ALONE**, one file, before any driver code and before any number existed)
**Result:** `research/2026-08-04_coldq-axial-rhob_result.md`
**Driver / JSON / checker:** `research/drivers/coldq_axial_rhob{.py,_results.json,_number_check.py}`
**Freeze base:** `origin/main` = `10213df3`

---

## Why this lane exists

v2.4's own §7 FLAG-4: FORK-3(b) (`ρ_eff = ρ_bulk/S³`) was fenced by `X6`, never run in the axial class, and *"would move the eigenvalue"*. The polar lane ran it once in an **uncertified coupled** instrument (`CFG-SOFT-B`), found no root, and adjudicated nothing. **The certified-axial debt was unpaid. This lane pays it — as a measurement, not yet as a certification.**

## Outcome, one line per configuration

| configuration | bin | certification |
|---|---|---|
| `CFG-A-CONTROL` (RHO-A negative control) | — | **`ROOT-NOT-CERTIFIED`** — `G2` FAILS at the `n = 32` rung; `FT-2`, `FT-2c` do not fire. **`G-NC` PASSES both limbs, so the STOP rule did not fire.** |
| `CFG-BOUND-POLY` | **`BIN-B-N`** ARTIFACT-class | no located root |
| `CFG-BOUND-FROB` | **`BIN-B-N`** PHYSICS-class | no located root |
| `CFG-IN-FROB` | **`BIN-B-S`** | **`ROOT-NOT-CERTIFIED`** — **every gate PASSES**; `FT-2`, `FT-2c`, `FT-W` do not fire |

**No physics bin is adjudicated on any configuration.** `BIN-B-STOP` and `BIN-B-W` did not fire.

## The deliverables that survived

1. **The negative control is exact.** `G-NC(a)` operator difference exactly `0`; `G-NC(b)` root relsep `2.139211445202149e-40`. Four v2.4-published gate values reproduced **to all digits**: `G1 4.726832751705419e-50`, `G3 3.332294747541498e-14`, `G4(a) 5.277782707837865e-47`, `G10(b) 9.273121713408482e-47`.
2. **The RHO-B wall row is DERIVED and certified as derived.** `G-IND` exactly `0`; `G-FROB` ratio `1.0000000003434282e-10` against a first-order zero's exact `1e-10`; all four `G-W` limbs hold. `FT-SHORT` **fires at `0.2739562093388408`** — the rejected RHO-A row moves the root by 27 per cent.
3. **The wall changes in KIND**: `Z_shear = 1/S → ∞` (RHO-A: `sqrt(S) → 0`); infinite optical distance (RHO-A: finite); regular singular point (RHO-A: ordinary); **traction diverges on both branches at the located root**, so no traction-free condition is satisfiable.
4. **Two nulls with a derived mechanism**: `ROW-BOUND` = the emerging-from-the-wall branch (acausal for a ringdown) has no `n`-stable root; `ROW-IN` = the ingoing branch has two.
5. **NOT-ADJUDICATED diagnostics**: `Ω = 1.0210587... − 0.3138716...i`, `n`-stable to `3.665073726334936e-13`; `ω_R M_g = 0.1458655300936263`; `Q = 1.6265545939814532`; direction `BIN-B-P3-RESCUE-PARTIAL` (`|D_Q|` improves `0.5619 → 0.2255`, `|D_omega|` worsens `0.2913 → 0.6096`); `BIN-B-P3-RESCUE-DECISIVE` does **not** fire.
6. **FLAG-W derived-consequence appendix** (flag output only, adjudicates nothing): under RHO-B **both** bulk branches JAM (`Z → ∞`); the FLAG-W sign split that exists under RHO-A **disappears** under RHO-B. `flag_w_sign_split_under_RHO_A = true`, `flag_w_sign_split_under_RHO_B = false`.

## Routed to the successor — four freeze-time sizing errors, NOT retuned

| # | defect | repair named |
|---|---|---|
| **S1** | `FT-2` threshold frozen at `1e-3`, mutation measures `4.4e-4` | freeze at `1e-6` as v2.4 did; size a self-test threshold against the mutation's measured effect, **never** against the gate's tolerance |
| **S2** | `FT-2c` stagnation `1e-12` too small and the law floor `1.0` non-discriminating | stagnate at the reference rung's own error scale; freeze the floor as a band edge |
| **S3** | `FT-W`'s mutation point can only break one of the two limbs it must break | extend limb (iv) to `k = 0`, **or** freeze the firing condition as *at least one limb fails* |
| **S4** | `G2`'s certification ladder includes `n = 32`, which v2.4 excluded on a fitted-law argument | carry v2.4's ladder placement or derive the tolerance from the ladder used |

## Routed to Grant / the auditor lane

- **`FLAG-CANON`** — `vol3/claim-quality.md:122` (`Z_shear = ρ c_shear → 0 ⇒ Γ_shear = −1`, unnamed `ρ`) and `:124` (`ρ_eff → ∞`) are three bullets apart in one leaf and **invert each other under substitution**. Verified two-method. **No leaf edited.** The downstream `:123` *"echoes are predicted"* is RHO-A-conditional.
- **`FLAG-CAUSAL`** (new) — the §0 plumber question is live: is an infinite-electrical-length lossless termination a legitimate Ax-3 radiative port? The prereg froze `ROW-BOUND`/`ROW-IN` co-primary; only one supports a resonance. **Grant's call owed; neither branch retired.**
- **`FLAG-MU`** — the `μ`-primary vs `c`-primary fork inside RHO-B, forced and disclosed at freeze.
- **`FLAG-ROWCLASS`** — `ROW-IN` needs an instrument that **excludes** rather than approximates the rejected branch. **Same exterior-complex-scaling build the polar lane's §6.2 and v2.4's FLAG-10 route: one build discharges three routings.**
- **FLAG-W NOT TOUCHED.** Shear-channel-only lane; the appendix is input to the core session's walk, not a contribution to its adjudication.

## Two implementation defects, repaired between the first execution and the shipped one — TIGHTENINGS, no criterion changed

- **D1** — the certified root was taken at `N_REF` rather than `N_PRIMARY`, so `G1` evaluated the `n = 48` operator at the `n = 80` root and `G10(b)` mirrored across two orders. After repair both read **v2.4's published values to all digits**, which is the receipt that the repair restored the frozen measurement.
- **D2** — `G-W` limb (iv) computed `||Δ| − k|` where the freeze specifies the **complex** `|Δ − k|`. Verdict unchanged at the located root.

## Validation receipts

- **Determinism.** Two full runs, digest `49c8c09cea8491b2` twice; shipped objects **byte-identical apart from `_runtime_sec`** (verified programmatically). Runtimes 816.98 s and 819.95 s. `G9` emits **no** `pass` field.
- **Number check.** 183 sites, 114 distinct tokens, 123 registered, 60 allow-listed, 0 unregistered, all 88 registered keys exercised. Wired into `make verify` as its own target, `verify-coldq-axial-rhob-number-check`.
- **Mutation receipts (4).** Single-digit drift of `1.0000000003434282e-10` (§HEADLINE), `0.2739562093388408` (§HEADLINE) and `9.273121713408482e-47` (§HEADLINE) each return **exit 1**, naming the token and the line; the unmutated document returns **exit 0**. Fourth receipt: re-writing one registered numeral with the Unicode minus U+2212 fires this lane's **ASCII-MINUS GUARD**, while a back-ticked verbatim quotation of frozen prereg text carrying U+2212 does **not** — the guard is narrowed to spans that become numerals once ASCII-fied.
- **`make verify`** exits `0` with the new gate wired in.
- **Fences.** Engine `src/ave` byte-untouched. Every predecessor file blob-pinned in prereg §P.1 byte-untouched (empty `git diff --stat` against the freeze base). `coldq_pole_v2p4_root.py` **imported read-only**, never edited, never executed as a battery. Pure-corpus fence clean.
- **Makefile.** Own target, no recipe body shared. **FLAG-12 carried forward: the `.PHONY` line and the `verify:` prerequisite line ARE shared with the polar-family branch (PR #869) and are a REAL two-line conflict, not an append-only merge.**

## What this lane does NOT claim

No `clm-`/`def-` minted, no KB or manuscript leaf touched, no solidity changed, no falsification-ledger row written. **No bin adjudicated.** No claim about which inertia canon means — **FORK-3 is exactly as open as it was.** No completeness or mode-count statement. No implementation independence from v2.4. No isolation claim for either Frobenius configuration. No cross-instrument corroboration for any `ROW-IN` number.
