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

---

## DATED ADDITION 2026-08-07 (R32) — the MAGNITUDE-ASSERTION class

**Appended, never a rewrite.** Nothing above this rule is edited; the census recorded at
`d129e7ac` stands as measured. Ruled at
[`2026-08-07-rulings-r31-r33.md`](2026-08-07-rulings-r31-r33.md) (R32), Grant verbatim *"Agree."*

### The class

**MAGNITUDE-ASSERTION** — a site whose asserted quantity is the **unsigned magnitude** `|Γ|`, not a
signed Γ. Surface forms in this corpus: `|\Gamma| = 1`, `|\Gamma|=1`, `|\Gamma| \to 1`.

**Unsigned-magnitude assertions are channel-independent by construction.** Axiom 3 forces
`|Γ| = 1` at a saturation boundary in every channel — the magnitude is what the axiom fixes, and it
fixes it the same way everywhere. Only a **SIGNED** Γ requires the plane / projection / profile
declarations that `wall-taxonomy.md` §10 enumerates, because only the sign depends on where the
reference plane is cut, which projection is taken, and which density profile is assumed. **The
signed-channel-declaration debt therefore does NOT attach to these sites.**

This is the **fourth finding class**, alongside the three the #923 execution recorded
(MIS-ASSOCIATION, TRUNCATED-VALUE, NOT-THE-LEFT-OPERAND) and the two §4.4 do-not-touch classes. It
differs from all of them in kind: those sites are **not actionable** — this class **is** actionable
under spec §1 and **is** tagged, and what the class records is that its tags carry **no channel
debt to discharge**.

### The 15 sites

Re-derived at `origin/main` = **`644a4546`**, in a worktree verified clean before any edit.
**Two-method receipt — engines and tree-state both named.**

- **Engine A** — Python `pathlib.rglob` + `re`: for each of the 205 merged `\gammaundeclared{}`
  markers, extract the asserting expression it terminates and classify the left operand.
  Result: **15 MAGNITUDE-ASSERTION / 190 SIGNED-BARE / 0 SQUARED / 0 unclassified**.
- **Engine B** — `git grep -F -o -f <pattern-file>` over four literal shapes, the patterns passed
  through a FILE rather than the shell so a shell-escaped `$`/`\` cannot silently false-negative.
  All four named with their measured hit counts, so the receipt is reproducible as written:

  | # | pattern | hits |
  |---|---|---|
  | 1 | `\|\Gamma\| \to 1$\gammaundeclared{}` | 5 |
  | 2 | `\|\Gamma\| = 1$\gammaundeclared{}` | 5 |
  | 3 | `\|\Gamma\|=1$\gammaundeclared{}` | 4 |
  | 4 | `\|\Gamma\| \to 1\gammaundeclared{}` — the DISPLAY-math form, no closing `$` before the marker | 1 |

  Result: **15 occurrences on 14 lines** (5+5+4+1), site set identical to Engine A. Pattern 4's one
  hit is `11_thermodynamics_and_entropy.tex`:324, whose magnitude assertion lives inside an
  `equation` environment where there is no `$` to close — which is why the `|\Gamma| \to 1` shape
  totals 6 (5 inline + 1 display) rather than 5.
- **Tree-state** — worktree at `644a4546`, `git status --porcelain` = 0, measured before any edit
  in this branch.

| site | shape |
|---|---|
| `backmatter/02_full_derivation_chain.tex`:1223 | `|\Gamma| \to 1` |
| `common_equations/eq_axiom_4.tex`:55 | `|\Gamma| = 1` |
| `vol_1_foundations/chapters/04_continuum_electrodynamics.tex`:105 | `|\Gamma|=1` |
| `vol_3_macroscopic/chapters/06_solar_system.tex`:12 | `|\Gamma| \to 1` |
| `vol_3_macroscopic/chapters/06_solar_system.tex`:392 | `|\Gamma| \to 1` |
| `vol_3_macroscopic/chapters/11_thermodynamics_and_entropy.tex`:324 | `|\Gamma| \to 1` |
| `vol_3_macroscopic/chapters/11_thermodynamics_and_entropy.tex`:389 | `|\Gamma| \to 1` |
| `vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex`:68 | `|\Gamma| = 1` |
| `vol_3_macroscopic/chapters/21_black_hole_interior_regime_iv.tex`:203 | `|\Gamma| = 1` |
| `vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex`:161 | `|\Gamma| = 1` |
| `vol_5_biology/chapters/02_organic_circuitry.tex`:624 | `|\Gamma| \to 1` |
| `vol_9_vacuum_datasheet/chapters/03a_device_circuit_models.tex`:82 | `|\Gamma| = 1` |
| `vol_9_vacuum_datasheet/chapters/05_ac_electrical_characteristics.tex`:172 | `|\Gamma|=1` |
| `vol_9_vacuum_datasheet/chapters/05_ac_electrical_characteristics.tex`:172 | `|\Gamma|=1` |
| `vol_9_vacuum_datasheet/chapters/05_ac_electrical_characteristics.tex`:241 | `|\Gamma|=1` |

Breakdown: `|\Gamma| \to 1` ×6 · `|\Gamma| = 1` ×5 · `|\Gamma|=1` ×4 = **15**. Two sites share
`05_ac_electrical_characteristics.tex`:172, which is why the 15 occurrences sit on 14 lines.

**Two of them are the sentences that make the class self-evident:**
`15_black_hole_orbital_resonance.tex`:68 — *"Axiom~3 forces only $|\Gamma| = 1$; a signed $\Gamma$
additionally requires its **reference plane**"* — and `03a_device_circuit_models.tex`:82 —
*"**Axiom~3 forces only $|\Gamma| = 1$**; the authority for a wall's $\Gamma$ **phase** is the
branch-derived indicial wall row of a certified instrument"*. The corpus already draws the
magnitude/sign line exactly where R32 draws it.

### Population split

At `644a4546` the 205 merged tags are **190 signed-bare Γ + 15 magnitude**, with **zero** `\Gamma^2`
tagged (all four `T^2 = 1 - \Gamma^2 \to 1` sites are NOT-THE-LEFT-OPERAND findings). The discharge
workstream inherits **190 sites carrying channel debt**, not 205.

### What this addition does NOT do

It untags nothing — the 15 markers stay exactly where they are, because they are actionable under
spec §1 and the census marks the population, not the debt. It adjudicates no channel, mints no id,
moves no solidity, and leaves the `Γ_shear` sign unresolved where canon has it
(`wall-taxonomy.md` §10.1).

### What R33 supersedes above — and this addition is what stales it

**Read §2 and §3 above with this note.** The instrument that produced them had the three defects
R33 repaired, so **four of §2's seven rows and §3's actionable row are superseded** — by *this*
lane's own change, which is why the note belongs here rather than nowhere. The rows are **not
rewritten**: the body above stands as measured, and the sentence in this addition that the census
"stands as measured" means exactly that — *those numbers are what that instrument reported* — not
that they are the current slice.

Re-measured on the **`91a910f8` corpus with the tip instrument** (corpus held fixed, instrument
swapped, so the delta is the repair and nothing else):

| §2 row | as recorded (pre-R33) | with the repaired instrument | moved by |
|---|---|---|---|
| channel named **and** signed ±1 | 202 / 67 | **147 / 58** | −55 / −9 |
| **ACTIONABLE** | **238 / 63** | **206 / 61** | −32 / −2 |
| … restricted to `= −1` | 184 / 57 | **177 / 56** | −7 / −1 |
| … the same slice in the KB (`.md`) | 994 / 168 | **675 / 145** | −319 / −23 |

| §3 row | as recorded | with the repaired instrument |
|---|---|---|
| `216 / 60` actionable → nearest slice / delta | 238 / 63 · +22 / +3 | **206 / 61 · −10 / +1** |

**The three §2 rows that did NOT move** — TOTAL `2887 / 356`, unspecified-channel `2332 / 330`,
channel-named `555 / 142` — are detection-and-subscript slices only. Their stability is the receipt
that **R33 changed classification and nothing else**.

**Why this note exists.** The frozen spec protects itself — §4 item 1 says *"Do not carry the
238/63 figure forward as truth — it is a measurement, and the convention it demonstrates is that
measurements are re-taken."* This record carried no such caveat, so a reader arriving at §2 would
take a superseded slice as current. Nothing above is edited; the supersession is recorded beside it.

**Full derivation, the mutation receipt, and the reconciliation identity
(`206 = 205 tagged + 1 §4.4 site-selection exclusion`):**
[`2026-08-07-gamma-tag-spec-correction.md`](2026-08-07-gamma-tag-spec-correction.md) §3–4.

### DATED SUPERSESSION 2026-08-09 (R39) — the inheritance number moved

**Appended, never a rewrite.** The R32 block above states at `:180` that *"the discharge
workstream inherits **190 sites carrying channel debt**, not 205"*, and the note above it
states the identity as `206 = 205 tagged + 1 exclusion`. Both are superseded — **by this
lane's own later change** — and it is recorded here rather than left as an honesty lag.

Ruled at [`2026-08-09-ruling-r39-sixtags.md`](2026-08-09-ruling-r39-sixtags.md), Grant
verbatim *"a on the six tags."*: six markers found by the R36 audit sitting inside Rule-12
preserved spans were **REMOVED**. Re-measured at `origin/main` = `e338743e`, two methods
(`git grep -o` scoped to `manuscript` net of the definition; independent Python `rglob`+`re`):

| quantity | as written above | at `e338743e` |
|---|---|---|
| tagged population | 205 | **199** |
| signed-bare | 190 | **185** |
| MAGNITUDE-ASSERTION | 15 | **14** |
| **discharge-workstream inheritance** | 190 | **185** |
| census identity | `206 = 205 + 1` | **`206 = 199 + 7`** (1 quoted + 6 §4.4-preserved) |

**The magnitude class lost one member, and that is why the inheritance is 185 and not 184.**
Of the six removed markers five were signed-bare and one —
`vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex`:161, `$|\Gamma| = 1$` — is a
MAGNITUDE-ASSERTION site from the fifteen listed above. Per this block's own reasoning the
magnitude class carries **no** signed-channel-declaration debt, so removing a magnitude site
does not reduce the debt count; only the five signed-bare removals do.

Full execution, the six byte-restoration receipts and the re-derived split:
[`2026-08-07-gamma-tag-spec-correction.md`](2026-08-07-gamma-tag-spec-correction.md),
addendum dated 2026-08-09.
