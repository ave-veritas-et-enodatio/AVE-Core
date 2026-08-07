# Signed-Γ census, re-derived and SHA-pinned (R1 treatment (i))

### ENTRY 2026-08-06-signed-gamma-census-at-sha

**Class:** doc-lane census. Mints no `clm-`/`def-`, moves no solidity, adjudicates no channel.
**Authority:** R1 (`_orchestration/docket-entries/2026-08-06-rulings-decision-batch.md`:13–19),
whose closing instruction is the load-bearing one: *"Census numbers cited in any brief must pin the
SHA (the 80%-figure drifted by 16 sites in ten commits)."*

**CENSUS-AT-SHA: every number in this fragment is measured at `origin/main` = `d129e7ac`**, in a
detached worktree at that commit, with the instrument
[`src/scripts/signed_gamma_census.py`](../../src/scripts/signed_gamma_census.py). Re-running it at
any other commit will return different numbers, and that is the point of the convention.

---

## 1. The universe, declared before the numbers

A "signed-Γ" count is not a well-formed quantity until its universe is stated — the instrument's
own module docstring exists because two prior sweeps disagreed 4× purely on knob settings. The
universe used here, every knob named:

```
roots=manuscript  exts=.tex,.md  gamma=all  relation=any  gap=adjacent-nested
signs=any  minus=unicode  glue=math  comments=include  magnitude_guard=True
```

**Two-method self-check: AGREE** (method A = Python `rglob` + `re`; method B = subprocess `grep -rInE`
on the byte-identical pattern). A = 2146 lines, B = 2146 lines, symmetric difference empty. A census
whose two methods disagree is not a census.

## 2. The numbers, at `d129e7ac`

| slice | sites | files |
|---|---|---|
| **TOTAL** — every Γ occurrence in the universe above | **2887** | **356** |
| **unspecified channel** — Γ carries no subscript (the *judgment* class) | **2332** | **330** |
| channel named (`bulk` / `shear` / `EM` / `other:<token>`) | 555 | 142 |
| channel named **and** signed ±1 (already declared) | 202 | 67 |
| **ACTIONABLE** — print `.tex`, rendered (not a `%`-comment), **unspecified channel**, asserting a **signed ±1** | **238** | **63** |
| … the same slice restricted to `= −1` | 184 | 57 |
| … the same slice in the KB (`.md`) rather than print | 994 | 168 |

"Actionable" is defined here, not inherited: **a signed Γ written in the printed manuscript with no
channel declared** — precisely the class §10 item 3 of `wall-taxonomy.md` governs ("the authority
for a wall's Γ phase is the branch-derived indicial wall row of a certified instrument").

## 3. Reconciliation with the figures R1 quotes — none of the three reproduces

R1 prints **216 / 60** actionable, **~2,998** total, **~2,230** judgment. The rescope-v2 correction
already tagged those `QUOTED-FROM-LANE-REPORT, non-authoritative` (C5) and instructed the executing
lane to re-derive. Re-derived:

| R1's figure | nearest slice at `d129e7ac` | delta |
|---|---|---|
| ~2,998 total | 2887 | −111 |
| ~2,230 judgment | 2332 (unspecified) | +102 |
| 216 / 60 actionable | 238 / 63 | +22 / +3 |

**Recorded as a non-reproduction, not reconciled by adjusting knobs until it matches.** The
corpus GREW between the lane report and this commit, so a smaller total at the later SHA cannot be
explained by drift alone — the original universe differed, and it was not stated. That is exactly
the failure mode R1's SHA-pin rule exists to end, and this fragment is the first census written
under it.

## 4. ⚑ TREATMENT (i) — the count is delivered, the EDIT is BLOCKED ON A DEFINITION

R1 rules *"Tag the 216 actionable sites / 60 files"* and routes execution to the doc lane as
*"(their proposal)"*. **That proposal is not in the repository.** It was carried in the upgrade
wave's final report, which was relayed in session and never landed as a tracked artifact; grep at
`d129e7ac` finds no definition of *actionable*, no specification of what a *tag* is, and no
worked example. What is recoverable from R1 is only the NEGATIVE half — treatment (ii),
mass-subscripting the judgment sites, is REJECTED because `wall-taxonomy.md` §10.1 records the
`Γ_shear` sign as unresolved and subscripting would hand-set a channel attribution canon has not
adjudicated.

**So this lane delivers the census and does NOT improvise the edit.** Writing a 238-site print
sweep against a reconstructed guess at the tag form would be the same class of error R1 rejected
for treatment (ii) — a hand-set convention entering print ahead of an adjudication. The two things
a resumed pass needs are one sentence each:

1. **What is the tag?** A pointer to `wall-taxonomy.md` §10's three declarations (plane /
   projection / profile)? A channel subscript only where mechanically determined? A marker for a
   later gate? Each is a different edit with a different blast radius.
2. **Is "actionable" §3's definition?** If the intended slice is different, the count changes and
   the site list changes with it.

**The census half of R1 is fully discharged and is the reusable half:** the slice is reproducible
by one command, at any SHA, with the universe attached.

## 5. What this census does NOT do

It adjudicates no channel, prefers no density branch, and touches the `Γ_shear` sign nowhere. It
counts.
